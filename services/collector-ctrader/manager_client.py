"""cTrader Manager API TCP/Protobuf client.

Implements the bare-metal Protobuf-over-TCP protocol used by Spotware's Manager API.
No grpc dependency — raw socket + manual protobuf encoding/decoding.

Authentication uses MANAGER_AUTH_REQ (payloadType 301) with MD5-hashed password.
All monetary values in API responses are cents. All volumes are cents of lot size.
Timestamps are Unix milliseconds.

Reference: .claude/references/ctrader/manager-api/
"""

import hashlib
import json
import socket
import ssl
import struct
import time
import threading
from typing import Any

import structlog

log = structlog.get_logger()

# ── Protobuf wire codec ───────────────────────────────────────────────────────

def _encode_varint(v: int) -> bytes:
    v = int(v)
    if v < 0:
        v += (1 << 64)
    result = []
    while True:
        bits = v & 0x7F
        v >>= 7
        if v:
            result.append(0x80 | bits)
        else:
            result.append(bits)
            break
    return bytes(result)


def _decode_varint(data: bytes, pos: int) -> tuple[int, int]:
    result, shift = 0, 0
    while True:
        b = data[pos]; pos += 1
        result |= (b & 0x7F) << shift
        if not (b & 0x80):
            return result, pos
        shift += 7


def _encode_tag(field_num: int, wire_type: int) -> bytes:
    return _encode_varint((field_num << 3) | wire_type)


def encode_uint32(field_num: int, value: int) -> bytes:
    return _encode_tag(field_num, 0) + _encode_varint(value)


def encode_int64(field_num: int, value: int) -> bytes:
    return _encode_tag(field_num, 0) + _encode_varint(value)


def encode_string(field_num: int, value: str) -> bytes:
    encoded = value.encode("utf-8")
    return _encode_tag(field_num, 2) + _encode_varint(len(encoded)) + encoded


def encode_bytes(field_num: int, value: bytes) -> bytes:
    return _encode_tag(field_num, 2) + _encode_varint(len(value)) + value


def parse_message(data: bytes) -> dict:
    """Parse protobuf bytes into {field_number: [values]}."""
    fields: dict[int, list] = {}
    pos = 0
    while pos < len(data):
        tag, pos = _decode_varint(data, pos)
        field_num = tag >> 3
        wire_type = tag & 0x7
        if wire_type == 0:
            val, pos = _decode_varint(data, pos)
            fields.setdefault(field_num, []).append(val)
        elif wire_type == 2:
            length, pos = _decode_varint(data, pos)
            val = data[pos:pos + length]; pos += length
            fields.setdefault(field_num, []).append(val)
        elif wire_type == 1:
            val = data[pos:pos + 8]; pos += 8
            fields.setdefault(field_num, []).append(val)
        elif wire_type == 5:
            val = data[pos:pos + 4]; pos += 4
            fields.setdefault(field_num, []).append(val)
        else:
            break
    return fields


def fields_to_dict(fields: dict) -> dict:
    """
    Convert parsed protobuf fields to a JSON-serializable dict.
    Nested length-delimited fields (wire type 2) are parsed recursively.
    Bytes that look like text are decoded as UTF-8; others kept as hex.
    """
    result: dict[str, Any] = {}
    for field_num, values in fields.items():
        converted = []
        for val in values:
            if isinstance(val, bytes):
                try:
                    inner = parse_message(val)
                    if inner:
                        converted.append(fields_to_dict(inner))
                    else:
                        try:
                            converted.append(val.decode("utf-8"))
                        except UnicodeDecodeError:
                            converted.append(val.hex())
                except Exception:
                    converted.append(val.hex())
            else:
                converted.append(val)
        result[str(field_num)] = converted[0] if len(converted) == 1 else converted
    return result


# ── ProtoMessage envelope ─────────────────────────────────────────────────────

def _proto_wrap(payload_type: int, payload: bytes = b"", client_msg_id: str | None = None) -> bytes:
    msg = encode_uint32(1, payload_type)
    if payload:
        msg += encode_bytes(2, payload)
    if client_msg_id:
        msg += encode_string(3, client_msg_id)
    return struct.pack(">I", len(msg)) + msg


def _proto_unwrap(data: bytes) -> tuple[int, bytes, str | None]:
    fields = parse_message(data)
    payload_type  = fields.get(1, [0])[0]
    payload       = fields.get(2, [b""])[0]
    client_msg_id = None
    if 3 in fields:
        try:
            client_msg_id = fields[3][0].decode("utf-8")
        except Exception:
            pass
    return payload_type, payload, client_msg_id


# ── Payload type registry ─────────────────────────────────────────────────────

PT = {
    "HEARTBEAT_EVENT":              51,
    "ERROR_RES":                    50,
    "HELLO_EVENT":                  990,
    "MANAGER_AUTH_REQ":             301,
    "MANAGER_AUTH_RES":             302,
    "EXECUTION_EVENT":              300,
    "SERVER_TIME_REQ":              313,
    "SERVER_TIME_RES":              314,
    "TRADER_LIST_REQ":              403,
    "TRADER_LIST_RES":              404,
    "POSITION_LIST_REQ":            407,
    "POSITION_LIST_RES":            408,
    "CLOSED_POSITION_LIST_REQ":     720,
    "CLOSED_POSITION_LIST_RES":     721,
    "PENDING_ORDER_LIST_REQ":       409,
    "PENDING_ORDER_LIST_RES":       410,
    "DEAL_LIST_REQ":                431,
    "DEAL_LIST_RES":                432,
    "LIGHT_GROUP_LIST_REQ":         473,
    "LIGHT_GROUP_LIST_RES":         474,
    "SYMBOL_LIST_REQ":              467,
    "SYMBOL_LIST_RES":              468,
    "MANAGER_LIST_REQ":             411,
    "MANAGER_LIST_RES":             412,
    "BALANCE_HISTORY_LIST_REQ":     417,
    "BALANCE_HISTORY_LIST_RES":     418,
    "EXPOSURE_SYMBOL_LIST_REQ":     419,
    "EXPOSURE_SYMBOL_LIST_RES":     420,
    "SERVER_SETTINGS_REQ":          423,
    "SERVER_SETTINGS_RES":          424,
}
PT_REVERSE = {v: k for k, v in PT.items()}


# ── ManagerAPIClient ──────────────────────────────────────────────────────────

class ManagerAPIClient:
    """
    Low-level Spotware Manager API TCP client.

    Usage:
        c = ManagerAPIClient(host, port, plant_id, env_name, login, password)
        c.connect()
        fields = c.request(PT["TRADER_LIST_REQ"], PT["TRADER_LIST_RES"], inner_payload)
        result = fields_to_dict(fields)
        c.close()
    """

    def __init__(
        self,
        host: str,
        port: int,
        plant_id: str,
        env_name: str,
        login: int,
        password: str,
        timeout: int = 30,
    ):
        self.host     = host
        self.port     = port
        self.plant_id = plant_id
        self.env_name = env_name
        self.login    = login
        self.password = password
        self.timeout  = timeout

        self._ssl_sock = None
        self._msg_id   = 0
        self.connected = False
        self._lock     = threading.Lock()

    def _next_id(self) -> str:
        self._msg_id += 1
        return str(self._msg_id)

    def connect(self) -> None:
        raw_sock = socket.create_connection((self.host, self.port), timeout=self.timeout)
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        self._ssl_sock = ctx.wrap_socket(raw_sock, server_hostname=self.host)
        self._ssl_sock.settimeout(self.timeout)
        self._authenticate()
        self.connected = True

    def close(self) -> None:
        self.connected = False
        if self._ssl_sock:
            try:
                self._ssl_sock.close()
            except Exception:
                pass
            self._ssl_sock = None

    def _send(self, data: bytes) -> None:
        total = 0
        while total < len(data):
            sent = self._ssl_sock.send(data[total:])
            if sent == 0:
                raise ConnectionError("Socket closed during send")
            total += sent

    def _recv_frame(self) -> bytes:
        header = self._recv_exactly(4)
        length = struct.unpack(">I", header)[0]
        return self._recv_exactly(length)

    def _recv_exactly(self, n: int) -> bytes:
        buf = b""
        while len(buf) < n:
            chunk = self._ssl_sock.recv(n - len(buf))
            if not chunk:
                raise ConnectionError("Socket closed during recv")
            buf += chunk
        return buf

    def _authenticate(self) -> None:
        # Read HELLO_EVENT
        frame = self._recv_frame()
        pt, payload, _ = _proto_unwrap(frame)
        if pt != PT["HELLO_EVENT"]:
            raise ConnectionError(f"Expected HELLO_EVENT (990), got {pt}")

        # Parse server version from hello
        fields = parse_message(payload)

        # Send MANAGER_AUTH_REQ
        pwd_hash = hashlib.md5(self.password.encode()).hexdigest()
        inner = (
            encode_string(1, self.plant_id) +
            encode_string(2, self.env_name) +
            encode_int64(3, self.login) +
            encode_string(4, pwd_hash)
        )
        msg_id = self._next_id()
        self._send(_proto_wrap(PT["MANAGER_AUTH_REQ"], inner, msg_id))

        # Read AUTH_RES
        while True:
            frame = self._recv_frame()
            pt, payload, cid = _proto_unwrap(frame)
            if pt == PT["HEARTBEAT_EVENT"]:
                continue
            if pt == PT["ERROR_RES"]:
                err = fields_to_dict(parse_message(payload))
                raise PermissionError(f"Authentication failed: {err}")
            if pt == PT["MANAGER_AUTH_RES"]:
                break
            raise ConnectionError(f"Unexpected response during auth: {pt}")

        log.info("ctrader.client.authenticated", host=self.host, login=self.login)

    def request(
        self,
        req_type: int,
        res_type: int,
        inner: bytes = b"",
        timeout_override: int | None = None,
    ) -> dict:
        """Send a request and return the parsed response fields dict."""
        with self._lock:
            msg_id = self._next_id()
            self._send(_proto_wrap(req_type, inner, msg_id))

            old_timeout = self._ssl_sock.gettimeout()
            if timeout_override:
                self._ssl_sock.settimeout(timeout_override)

            try:
                while True:
                    frame = self._recv_frame()
                    pt, payload, cid = _proto_unwrap(frame)
                    if pt == PT["HEARTBEAT_EVENT"]:
                        continue
                    if cid != msg_id:
                        continue  # event or different request
                    if pt == PT["ERROR_RES"]:
                        err = fields_to_dict(parse_message(payload))
                        raise RuntimeError(f"API error for {PT_REVERSE.get(req_type, req_type)}: {err}")
                    if pt == res_type:
                        return parse_message(payload)
                    raise RuntimeError(f"Unexpected response type {pt} (expected {res_type})")
            finally:
                self._ssl_sock.settimeout(old_timeout)

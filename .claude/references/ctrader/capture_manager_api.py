"""
cTrader Manager API — Live Capture Script
Connects, authenticates, calls all read-only endpoints,
captures real responses, writes structured markdown reference files.

Usage:
    python capture_manager_api.py

Output:
    .claude/references/ctrader/manager-api/*.md
"""

import ssl, socket, struct, hashlib, time, json, os, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')
from datetime import datetime, timezone

# ─── Credentials ──────────────────────────────────────────────────────────────
HOST        = "live-managerapi.p.ctrader.com"
PORT        = 5011
PLANT_ID    = "opofinance"
ENV_NAME    = "live"
LOGIN       = 10023
PASSWORD    = "Vista1234$"

OUT_DIR = os.path.join(os.path.dirname(__file__), "manager-api")
os.makedirs(OUT_DIR, exist_ok=True)

# ─── Protobuf wire encoder / decoder ─────────────────────────────────────────
# Wire types: 0=varint, 1=64bit, 2=length-delimited, 5=32bit

def encode_varint(v):
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

def decode_varint(data, pos):
    result, shift = 0, 0
    while True:
        b = data[pos]; pos += 1
        result |= (b & 0x7F) << shift
        if not (b & 0x80):
            return result, pos
        shift += 7

def encode_tag(field_num, wire_type):
    return encode_varint((field_num << 3) | wire_type)

def encode_string(field_num, value):
    encoded = value.encode('utf-8')
    return encode_tag(field_num, 2) + encode_varint(len(encoded)) + encoded

def encode_bytes(field_num, value):
    return encode_tag(field_num, 2) + encode_varint(len(value)) + value

def encode_uint32(field_num, value):
    return encode_tag(field_num, 0) + encode_varint(value)

def encode_int64(field_num, value):
    return encode_tag(field_num, 0) + encode_varint(value)

def encode_bool(field_num, value):
    return encode_tag(field_num, 0) + encode_varint(1 if value else 0)

def parse_message(data):
    """Parse protobuf message into {field_number: [values]}"""
    fields = {}
    pos = 0
    while pos < len(data):
        tag, pos = decode_varint(data, pos)
        field_num = tag >> 3
        wire_type = tag & 0x7
        if wire_type == 0:
            val, pos = decode_varint(data, pos)
            fields.setdefault(field_num, []).append(val)
        elif wire_type == 2:
            length, pos = decode_varint(data, pos)
            val = data[pos:pos+length]; pos += length
            fields.setdefault(field_num, []).append(val)
        elif wire_type == 1:
            val = data[pos:pos+8]; pos += 8
            fields.setdefault(field_num, []).append(val)
        elif wire_type == 5:
            val = data[pos:pos+4]; pos += 4
            fields.setdefault(field_num, []).append(val)
        else:
            break
    return fields

def proto_message_wrap(payload_type, payload=b'', client_msg_id=None):
    """Wrap inner message in ProtoMessage envelope"""
    msg = encode_uint32(1, payload_type)
    if payload:
        msg += encode_bytes(2, payload)
    if client_msg_id:
        msg += encode_string(3, client_msg_id)
    return struct.pack('>I', len(msg)) + msg

def proto_message_unwrap(data):
    """Unwrap ProtoMessage → (payload_type, payload_bytes, client_msg_id)"""
    fields = parse_message(data)
    payload_type = fields.get(1, [0])[0]
    payload      = fields.get(2, [b''])[0]
    client_msg_id = None
    if 3 in fields:
        try:
            client_msg_id = fields[3][0].decode('utf-8')
        except Exception:
            pass
    return payload_type, payload, client_msg_id

# ─── Manager API Payload Types (v2 numbering) ────────────────────────────────
PT = {
    'HEARTBEAT_EVENT':              51,
    'ERROR_RES':                    50,
    'HELLO_EVENT':                  990,
    'MANAGER_AUTH_REQ':             301,
    'MANAGER_AUTH_RES':             302,
    'EXECUTION_EVENT':              300,
    'SERVER_TIME_REQ':              313,
    'SERVER_TIME_RES':              314,
    'TRADER_LIST_REQ':              403,
    'TRADER_LIST_RES':              404,
    'TRADER_BY_ID_REQ':             703,
    'TRADER_BY_ID_RES':             704,
    'POSITION_LIST_REQ':            407,
    'POSITION_LIST_RES':            408,
    'CLOSED_POSITION_LIST_REQ':     720,
    'CLOSED_POSITION_LIST_RES':     721,
    'PENDING_ORDER_LIST_REQ':       409,
    'PENDING_ORDER_LIST_RES':       410,
    'ORDER_MANAGER_LIST_REQ':       443,
    'ORDER_MANAGER_LIST_RES':       444,
    'DEAL_LIST_REQ':                431,
    'DEAL_LIST_RES':                432,
    'GET_DEAL_REQ':                 709,
    'GET_DEAL_RES':                 711,
    'BALANCE_HISTORY_LIST_REQ':     417,
    'BALANCE_HISTORY_LIST_RES':     418,
    'BONUS_HISTORY_LIST_REQ':       786,
    'BONUS_HISTORY_LIST_RES':       787,
    'LIGHT_GROUP_LIST_REQ':         473,
    'LIGHT_GROUP_LIST_RES':         474,
    'GROUP_BY_ID_REQ':              475,
    'GROUP_BY_ID_RES':              476,
    'SYMBOL_LIST_REQ':              467,
    'SYMBOL_LIST_RES':              468,
    'SYMBOL_CATEGORY_LIST_REQ':     463,
    'SYMBOL_CATEGORY_LIST_RES':     464,
    'ASSET_LIST_REQ':               465,
    'ASSET_LIST_RES':               466,
    'ASSET_CLASS_LIST_REQ':         437,
    'ASSET_CLASS_LIST_RES':         438,
    'MANAGER_LIST_REQ':             411,
    'MANAGER_LIST_RES':             412,
    'COUNTRY_LIST_REQ':             435,
    'COUNTRY_LIST_RES':             436,
    'EXPOSURE_SYMBOL_LIST_REQ':     419,
    'EXPOSURE_SYMBOL_LIST_RES':     420,
    'LIQUIDITY_FEED_LIST_REQ':      429,
    'LIQUIDITY_FEED_LIST_RES':      430,
    'LIQUIDITY_FEED_SYMBOL_LIST_REQ': 489,
    'LIQUIDITY_FEED_SYMBOL_LIST_RES': 490,
    'SERVER_SETTINGS_REQ':          423,
    'SERVER_SETTINGS_RES':          424,
    'DEALING_SETTINGS_REQ':         816,
    'DEALING_SETTINGS_RES':         817,
    'MANUAL_DEAL_LIST_REQ':         821,
    'MANUAL_DEAL_LIST_RES':         822,
    'SCHEDULE_PROFILE_LIST_REQ':    363,
    'SCHEDULE_PROFILE_LIST_RES':    364,
    'COMMISSION_PROFILE_LIST_REQ':  368,
    'COMMISSION_PROFILE_LIST_RES':  369,
    'VOLUME_PROFILE_LIST_REQ':      378,
    'VOLUME_PROFILE_LIST_RES':      379,
    'EXECUTION_PROFILE_LIST_REQ':   383,
    'EXECUTION_PROFILE_LIST_RES':   384,
    'PROTECTION_PROFILE_LIST_REQ':  388,
    'PROTECTION_PROFILE_LIST_RES':  389,
    'SWAP_FREE_PROFILE_LIST_REQ':   393,
    'SWAP_FREE_PROFILE_LIST_RES':   394,
    'HOLIDAY_LIST_REQ':             398,
    'HOLIDAY_LIST_RES':             399,
    'HOLIDAY_PROFILE_LIST_REQ':     447,
    'HOLIDAY_PROFILE_LIST_RES':     448,
    'DYNAMIC_LEVERAGE_LIST_REQ':    469,
    'DYNAMIC_LEVERAGE_LIST_RES':    470,
    'GSL_SCHEDULE_LIST_REQ':        471,
    'GSL_SCHEDULE_LIST_RES':        472,
    'LIGHT_SWAP_PROFILE_LIST_REQ':  493,
    'LIGHT_SWAP_PROFILE_LIST_RES':  494,
    'PRICE_STREAM_LIST_REQ':        427,
    'PRICE_STREAM_LIST_RES':        428,
    'ORDER_DETAILS_REQ':            321,
    'ORDER_DETAILS_RES':            322,
    'DEAL_LIST_BY_POSITION_ID_REQ': 459,
    'DEAL_LIST_BY_POSITION_ID_RES': 460,
    'POSITION_DETAILS_LITE_REQ':    754,
    'POSITION_DETAILS_LITE_RES':    755,
    'MANAGER_GET_AUTH_TOKEN_REQ':   850,
    'MANAGER_GET_AUTH_TOKEN_RES':   851,
    'RECALC_ACCOUNT_MARGIN_REQ':    336,
    'RECALC_ACCOUNT_MARGIN_RES':    337,
}
PT_REVERSE = {v: k for k, v in PT.items()}

# ─── Connection ───────────────────────────────────────────────────────────────
class ManagerAPIClient:
    def __init__(self):
        self.sock = None
        self.ssl_sock = None
        self._msg_id = 0
        self.connected = False
        self.permissions = []
        self.server_version = None
        self.raw_captures = {}  # endpoint_name -> raw parsed fields

    def _next_id(self):
        self._msg_id += 1
        return str(self._msg_id)

    def connect(self):
        print(f"Connecting to {HOST}:{PORT} ...")
        raw_sock = socket.create_connection((HOST, PORT), timeout=30)
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        self.ssl_sock = ctx.wrap_socket(raw_sock, server_hostname=HOST)
        self.ssl_sock.settimeout(30)
        print("SSL handshake complete")

        # Read HelloEvent
        hello_data = self._recv_frame()
        pt, payload, _ = proto_message_unwrap(hello_data)
        print(f"  HelloEvent payloadType={pt} (expected {PT['HELLO_EVENT']})")

        # Authenticate
        self._authenticate()
        self.connected = True

    def _recv_frame(self):
        header = self._recv_exactly(4)
        length = struct.unpack('>I', header)[0]
        if length > 10 * 1024 * 1024:
            raise ValueError(f"Frame too large: {length}")
        return self._recv_exactly(length)

    def _recv_exactly(self, n):
        buf = b''
        while len(buf) < n:
            chunk = self.ssl_sock.recv(n - len(buf))
            if not chunk:
                raise ConnectionError("Connection closed")
            buf += chunk
        return buf

    def _send(self, payload_type, inner_payload=b'', client_msg_id=None):
        frame = proto_message_wrap(payload_type, inner_payload, client_msg_id)
        self.ssl_sock.sendall(frame)

    def _recv_response(self, expected_pt, timeout=15):
        deadline = time.time() + timeout
        while time.time() < deadline:
            self.ssl_sock.settimeout(max(0.5, deadline - time.time()))
            try:
                data = self._recv_frame()
            except socket.timeout:
                continue
            pt, payload, cid = proto_message_unwrap(data)
            if pt == PT['HEARTBEAT_EVENT']:
                self._send(PT['HEARTBEAT_EVENT'])
                continue
            if pt == PT['ERROR_RES']:
                fields = parse_message(payload)
                err_code = fields.get(1, [0])[0]
                err_desc = fields.get(2, [b'unknown'])[0]
                try:
                    err_desc = err_desc.decode('utf-8')
                except Exception:
                    pass
                raise RuntimeError(f"ERROR_RES code={err_code} desc={err_desc}")
            if pt == expected_pt:
                return pt, payload
            # store unsolicited events for later
            name = PT_REVERSE.get(pt, f"UNKNOWN_{pt}")
            print(f"    [recv unsolicited {name}({pt})]")
        raise TimeoutError(f"Timeout waiting for payloadType={expected_pt}")

    def _authenticate(self):
        pw_hash = hashlib.md5(PASSWORD.encode('ascii')).hexdigest()
        inner = (
            encode_string(2, PLANT_ID) +
            encode_string(3, ENV_NAME) +
            encode_int64(4, LOGIN) +
            encode_string(5, pw_hash)
        )
        cid = self._next_id()
        self._send(PT['MANAGER_AUTH_REQ'], inner, cid)
        print("  Sent ProtoManagerAuthReq")
        pt, payload = self._recv_response(PT['MANAGER_AUTH_RES'])
        fields = parse_message(payload)
        self.permissions = fields.get(2, [])
        print(f"  Authenticated ✓  permissions={self.permissions}")

    def heartbeat(self):
        self._send(PT['HEARTBEAT_EVENT'])

    def request(self, req_pt, res_pt, inner=b'', label=None):
        """Send a request and return parsed response fields"""
        cid = self._next_id()
        self._send(req_pt, inner, cid)
        pt, payload = self._recv_response(res_pt)
        fields = parse_message(payload)
        if label:
            self.raw_captures[label] = fields
        return fields

    def reconnect(self):
        """Close and re-establish connection + authentication"""
        try:
            self.close()
        except Exception:
            pass
        self.ssl_sock = None
        self.connected = False
        self.connect()

    def now_ms(self):
        return int(time.time() * 1000)

    def one_hour_ago_ms(self):
        return int((time.time() - 3600) * 1000)

    def seven_days_ago_ms(self):
        return int((time.time() - 7 * 86400) * 1000)

    def close(self):
        if self.ssl_sock:
            try:
                self.ssl_sock.close()
            except Exception:
                pass

# ─── Field decoder ────────────────────────────────────────────────────────────
def decode_field(val):
    """Try to decode bytes as utf-8 string, else hex"""
    if isinstance(val, bytes):
        try:
            return val.decode('utf-8')
        except Exception:
            return val.hex()
    return val

def fields_to_dict(fields, depth=0):
    result = {}
    for k, vals in fields.items():
        decoded_vals = []
        for v in vals:
            if isinstance(v, bytes) and len(v) > 2:
                try:
                    inner = parse_message(v)
                    if inner and depth < 3:
                        decoded_vals.append(fields_to_dict(inner, depth+1))
                        continue
                except Exception:
                    pass
            decoded_vals.append(decode_field(v))
        result[k] = decoded_vals[0] if len(decoded_vals) == 1 else decoded_vals
    return result

# ─── Markdown writer ──────────────────────────────────────────────────────────
def write_md(filename, content):
    path = os.path.join(OUT_DIR, filename)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"  Wrote {path}")

def json_block(data):
    return "```json\n" + json.dumps(data, indent=2, default=str) + "\n```"

# ─── Capture all endpoints ────────────────────────────────────────────────────
def run_capture():
    c = ManagerAPIClient()
    c.connect()

    now   = c.now_ms()
    h1    = c.one_hour_ago_ms()
    d7    = c.seven_days_ago_ms()
    d30   = now - 30 * 86400 * 1000
    epoch = 0

    captures = {}

    def cap(label, req_pt, res_pt, inner=b'', reconnect_on_fail=False):
        print(f"  [{label}] ...", end=' ', flush=True)
        try:
            fields = c.request(req_pt, res_pt, inner, label=label)
            captures[label] = {'ok': True, 'fields': fields_to_dict(fields)}
            count = sum(len(v) if isinstance(v, list) else 1 for v in fields.values())
            print(f"ok ({count} field values)")
        except Exception as e:
            captures[label] = {'ok': False, 'error': str(e)}
            print(f"ERROR: {e}")
            if reconnect_on_fail or 'Connection' in str(e) or 'closed' in str(e).lower():
                print(f"    [reconnecting...]")
                try:
                    c.reconnect()
                except Exception as re:
                    print(f"    [reconnect failed: {re}]")
        try:
            c.heartbeat()
        except Exception:
            try:
                c.reconnect()
            except Exception:
                pass
        time.sleep(0.5)

    print("\n── Session ──────────────────────────────────────────────────────")
    cap("server_time", PT['SERVER_TIME_REQ'], PT['SERVER_TIME_RES'])
    cap("auth_token",  PT['MANAGER_GET_AUTH_TOKEN_REQ'], PT['MANAGER_GET_AUTH_TOKEN_RES'])

    print("\n── Accounts (Traders) ───────────────────────────────────────────")
    # Paginate traders: all registered in last 30 days
    trader_req = encode_int64(2, d30) + encode_int64(3, now)
    cap("trader_list", PT['TRADER_LIST_REQ'], PT['TRADER_LIST_RES'], trader_req)

    # Grab a traderId from the list for subsequent requests
    sample_trader_id = None
    if captures.get('trader_list', {}).get('ok') and 2 in c.raw_captures.get('trader_list', {}):
        raw_traders = c.raw_captures['trader_list'].get(2, [])
        if raw_traders:
            first_raw = raw_traders[0] if isinstance(raw_traders, list) else raw_traders
            inner_f = parse_message(first_raw)
            sample_trader_id = inner_f.get(1, [None])[0]
            print(f"    sample traderId: {sample_trader_id}")

    if sample_trader_id:
        tid_req = encode_int64(2, sample_trader_id)
        cap("trader_by_id", PT['TRADER_BY_ID_REQ'], PT['TRADER_BY_ID_RES'], tid_req)

    print("\n── Groups ───────────────────────────────────────────────────────")
    cap("group_list", PT['LIGHT_GROUP_LIST_REQ'], PT['LIGHT_GROUP_LIST_RES'])

    # Grab a groupId for subsequent requests
    sample_group_id = None
    if captures.get('group_list', {}).get('ok'):
        raw_grp = c.raw_captures.get('group_list', {}).get(2, [])
        if raw_grp:
            first_raw = raw_grp[0] if isinstance(raw_grp, list) else raw_grp
            inner_f = parse_message(first_raw)
            sample_group_id = inner_f.get(1, [None])[0]
            print(f"    sample groupId: {sample_group_id}")

    if sample_group_id:
        gid_req = encode_int64(2, sample_group_id)
        cap("group_by_id", PT['GROUP_BY_ID_REQ'], PT['GROUP_BY_ID_RES'], gid_req)

    print("\n── Symbols ──────────────────────────────────────────────────────")
    cap("symbol_list",          PT['SYMBOL_LIST_REQ'],          PT['SYMBOL_LIST_RES'])
    cap("symbol_category_list", PT['SYMBOL_CATEGORY_LIST_REQ'], PT['SYMBOL_CATEGORY_LIST_RES'])

    print("\n── Assets ───────────────────────────────────────────────────────")
    cap("asset_list",       PT['ASSET_LIST_REQ'],       PT['ASSET_LIST_RES'])
    cap("asset_class_list", PT['ASSET_CLASS_LIST_REQ'], PT['ASSET_CLASS_LIST_RES'])

    print("\n── Managers ─────────────────────────────────────────────────────")
    cap("manager_list", PT['MANAGER_LIST_REQ'], PT['MANAGER_LIST_RES'])

    print("\n── Countries ────────────────────────────────────────────────────")
    cap("country_list", PT['COUNTRY_LIST_REQ'], PT['COUNTRY_LIST_RES'])

    print("\n── Positions ────────────────────────────────────────────────────")
    pos_req = encode_int64(3, d7) + encode_int64(4, now)
    cap("open_position_list", PT['POSITION_LIST_REQ'], PT['POSITION_LIST_RES'], pos_req)

    closed_req = encode_int64(2, d7) + encode_int64(3, now)
    cap("closed_position_list", PT['CLOSED_POSITION_LIST_REQ'], PT['CLOSED_POSITION_LIST_RES'], closed_req)

    # position details - use sample position if any
    sample_position_id = None
    if captures.get('open_position_list', {}).get('ok'):
        raw_pos = c.raw_captures.get('open_position_list', {}).get(3, [])
        if raw_pos:
            first_raw = raw_pos[0] if isinstance(raw_pos, list) else raw_pos
            inner_f = parse_message(first_raw)
            sample_position_id = inner_f.get(1, [None])[0]
    if not sample_position_id and captures.get('closed_position_list', {}).get('ok'):
        raw_pos = c.raw_captures.get('closed_position_list', {}).get(2, [])
        if raw_pos:
            first_raw = raw_pos[0] if isinstance(raw_pos, list) else raw_pos
            inner_f = parse_message(first_raw)
            sample_position_id = inner_f.get(1, [None])[0]

    if sample_position_id:
        print(f"    sample positionId: {sample_position_id}")
        pdl_req = encode_int64(2, sample_position_id)
        cap("position_details_lite", PT['POSITION_DETAILS_LITE_REQ'], PT['POSITION_DETAILS_LITE_RES'], pdl_req)
        dbyp_req = encode_int64(2, sample_position_id) + encode_int64(3, d30) + encode_int64(4, now)
        cap("deal_list_by_position", PT['DEAL_LIST_BY_POSITION_ID_REQ'], PT['DEAL_LIST_BY_POSITION_ID_RES'], dbyp_req)

    print("\n── Orders ───────────────────────────────────────────────────────")
    ord_req = encode_int64(3, d7) + encode_int64(4, now)
    cap("pending_order_list", PT['PENDING_ORDER_LIST_REQ'], PT['PENDING_ORDER_LIST_RES'], ord_req)

    ord_mgr_req = encode_int64(2, d7) + encode_int64(3, now)
    cap("order_manager_list", PT['ORDER_MANAGER_LIST_REQ'], PT['ORDER_MANAGER_LIST_RES'], ord_mgr_req)

    # Get sample order
    sample_order_id = None
    for key in ('pending_order_list', 'order_manager_list'):
        if captures.get(key, {}).get('ok') and not sample_order_id:
            raw_ord = c.raw_captures.get(key, {}).get(3 if key == 'pending_order_list' else 2, [])
            if raw_ord:
                first_raw = raw_ord[0] if isinstance(raw_ord, list) else raw_ord
                inner_f = parse_message(first_raw)
                sample_order_id = inner_f.get(1, [None])[0]
    if sample_order_id:
        print(f"    sample orderId: {sample_order_id}")
        od_req = encode_int64(2, sample_order_id)
        cap("order_details", PT['ORDER_DETAILS_REQ'], PT['ORDER_DETAILS_RES'], od_req)

    print("\n── Deals ────────────────────────────────────────────────────────")
    deal_req = encode_int64(3, d7) + encode_int64(4, now)
    cap("deal_list", PT['DEAL_LIST_REQ'], PT['DEAL_LIST_RES'], deal_req)

    sample_deal_id = None
    if captures.get('deal_list', {}).get('ok'):
        raw_deals = c.raw_captures.get('deal_list', {}).get(2, [])
        if raw_deals:
            first_raw = raw_deals[0] if isinstance(raw_deals, list) else raw_deals
            inner_f = parse_message(first_raw)
            sample_deal_id = inner_f.get(1, [None])[0]
    if sample_deal_id:
        print(f"    sample dealId: {sample_deal_id}")
        gd_req = encode_int64(2, sample_deal_id)
        cap("get_deal", PT['GET_DEAL_REQ'], PT['GET_DEAL_RES'], gd_req)

    print("\n── Balance History ──────────────────────────────────────────────")
    bal_req = encode_int64(3, d7) + encode_int64(4, now)
    cap("balance_history_list", PT['BALANCE_HISTORY_LIST_REQ'], PT['BALANCE_HISTORY_LIST_RES'], bal_req)

    bonus_req = encode_int64(3, d7) + encode_int64(4, now)
    cap("bonus_history_list", PT['BONUS_HISTORY_LIST_REQ'], PT['BONUS_HISTORY_LIST_RES'], bonus_req)

    print("\n── Server / Configuration ───────────────────────────────────────")
    cap("server_settings",   PT['SERVER_SETTINGS_REQ'],   PT['SERVER_SETTINGS_RES'])
    cap("dealing_settings",  PT['DEALING_SETTINGS_REQ'],  PT['DEALING_SETTINGS_RES'])
    cap("manual_deal_list",  PT['MANUAL_DEAL_LIST_REQ'],  PT['MANUAL_DEAL_LIST_RES'])
    # field2=1 is required; empty payload returns INVALID_REQUEST
    cap("exposure_symbols",  PT['EXPOSURE_SYMBOL_LIST_REQ'], PT['EXPOSURE_SYMBOL_LIST_RES'], encode_int64(2, 1), reconnect_on_fail=True)
    cap("liquidity_feeds",   PT['LIQUIDITY_FEED_LIST_REQ'], PT['LIQUIDITY_FEED_LIST_RES'], reconnect_on_fail=True)
    cap("liquidity_feed_symbols", PT['LIQUIDITY_FEED_SYMBOL_LIST_REQ'], PT['LIQUIDITY_FEED_SYMBOL_LIST_RES'], reconnect_on_fail=True)
    cap("price_stream_list", PT['PRICE_STREAM_LIST_REQ'],  PT['PRICE_STREAM_LIST_RES'], reconnect_on_fail=True)

    print("\n── Profiles ─────────────────────────────────────────────────────")
    cap("schedule_profiles",  PT['SCHEDULE_PROFILE_LIST_REQ'],  PT['SCHEDULE_PROFILE_LIST_RES'],  reconnect_on_fail=True)
    cap("commission_profiles",PT['COMMISSION_PROFILE_LIST_REQ'],PT['COMMISSION_PROFILE_LIST_RES'], reconnect_on_fail=True)
    cap("volume_profiles",    PT['VOLUME_PROFILE_LIST_REQ'],    PT['VOLUME_PROFILE_LIST_RES'],     reconnect_on_fail=True)
    cap("execution_profiles", PT['EXECUTION_PROFILE_LIST_REQ'], PT['EXECUTION_PROFILE_LIST_RES'],  reconnect_on_fail=True)
    cap("protection_profiles",PT['PROTECTION_PROFILE_LIST_REQ'],PT['PROTECTION_PROFILE_LIST_RES'], reconnect_on_fail=True)
    cap("swap_free_profiles", PT['SWAP_FREE_PROFILE_LIST_REQ'], PT['SWAP_FREE_PROFILE_LIST_RES'],  reconnect_on_fail=True)
    cap("holiday_list",       PT['HOLIDAY_LIST_REQ'],           PT['HOLIDAY_LIST_RES'],            reconnect_on_fail=True)
    cap("holiday_profiles",   PT['HOLIDAY_PROFILE_LIST_REQ'],   PT['HOLIDAY_PROFILE_LIST_RES'],    reconnect_on_fail=True)
    cap("dynamic_leverage_list", PT['DYNAMIC_LEVERAGE_LIST_REQ'], PT['DYNAMIC_LEVERAGE_LIST_RES'], reconnect_on_fail=True)
    cap("gsl_schedule_list",  PT['GSL_SCHEDULE_LIST_REQ'],      PT['GSL_SCHEDULE_LIST_RES'],       reconnect_on_fail=True)
    cap("light_swap_profiles",PT['LIGHT_SWAP_PROFILE_LIST_REQ'],PT['LIGHT_SWAP_PROFILE_LIST_RES'], reconnect_on_fail=True)

    print("\n── Margin Recalc ────────────────────────────────────────────────")
    if sample_trader_id:
        rm_req = encode_int64(2, sample_trader_id)
        cap("recalc_account_margin", PT['RECALC_ACCOUNT_MARGIN_REQ'], PT['RECALC_ACCOUNT_MARGIN_RES'], rm_req)

    c.close()
    return captures

# ─── Markdown generator ───────────────────────────────────────────────────────
def sample_to_table(data, depth=0):
    if not isinstance(data, dict):
        return f"```\n{data}\n```"
    rows = []
    for k, v in data.items():
        if isinstance(v, dict):
            rows.append(f"| `{k}` | *(nested object)* |")
        elif isinstance(v, list):
            rows.append(f"| `{k}` | `{v}` |")
        else:
            rows.append(f"| `{k}` | `{v}` |")
    if not rows:
        return "_empty_"
    return "| Field | Value |\n|-------|-------|\n" + "\n".join(rows)

ENDPOINT_DOCS = {
    "server_time": {
        "title": "Server Time",
        "category": "session",
        "req": "ProtoServerTimeReq",
        "res": "ProtoServerTimeRes",
        "req_pt": 313, "res_pt": 314,
        "description": "Returns the current server timestamp in milliseconds. Use to synchronize clocks and validate session.",
        "req_fields": [],
        "res_fields": [("timeInMillis", "int64", "Server Unix timestamp in milliseconds")],
        "notes": "No request fields needed — send empty payload. Good first call after auth to verify connectivity."
    },
    "auth_token": {
        "title": "Get Auth Token",
        "category": "session",
        "req": "ProtoManagerGetAuthTokenReq",
        "res": "ProtoManagerGetAuthTokenRes",
        "req_pt": 850, "res_pt": 851,
        "description": "Retrieves a short-lived bearer token for use with the Reporting API HTTP endpoints.",
        "req_fields": [],
        "res_fields": [("token", "string", "Bearer token for HTTP Reporting API")],
        "notes": "Token is time-limited. Store and reuse within TTL. Renew before expiry."
    },
    "trader_list": {
        "title": "Trader List (Accounts)",
        "category": "accounts",
        "req": "ProtoTraderListReq",
        "res": "ProtoTraderListRes",
        "req_pt": 403, "res_pt": 404,
        "description": "Returns a paginated list of trader accounts registered within the given timestamp window.",
        "req_fields": [
            ("fromTimestamp", "int64", "required", "Start of window — Unix ms"),
            ("toTimestamp",   "int64", "required", "End of window — Unix ms"),
            ("groupId",       "int64", "optional", "Filter by group ID"),
            ("hideIbParameters", "bool", "optional", "Exclude IB-specific fields"),
            ("onlySubAccounts",  "bool", "optional", "Return sub-accounts only"),
        ],
        "res_fields": [
            ("trader",   "ProtoTrader[]", "List of trader objects"),
            ("hasMore",  "bool",          "true = more pages exist; advance fromTimestamp"),
        ],
        "notes": "Paginate by advancing `fromTimestamp` to the last record's `registrationTimestamp`. Keep looping while `hasMore == true`."
    },
    "trader_by_id": {
        "title": "Trader By ID",
        "category": "accounts",
        "req": "ProtoTraderByIdReq",
        "res": "ProtoTraderByIdRes",
        "req_pt": 703, "res_pt": 704,
        "description": "Fetch one or more specific traders by their internal traderId.",
        "req_fields": [("traderId", "int64[]", "required", "Repeated — can batch multiple IDs")],
        "res_fields": [("trader", "ProtoTrader[]", "Trader objects matching requested IDs")],
        "notes": "Batching is supported — send multiple traderId fields in one request."
    },
    "group_list": {
        "title": "Group List (Light)",
        "category": "groups",
        "req": "ProtoLightGroupListReq",
        "res": "ProtoLightGroupListRes",
        "req_pt": 473, "res_pt": 474,
        "description": "Returns a lightweight list of all trader groups (no symbol configuration).",
        "req_fields": [],
        "res_fields": [("group", "ProtoLightGroup[]", "Group ID, name, and basic metadata")],
        "notes": "Use for lookups and dropdowns. For full group config including symbol overrides, use GroupById."
    },
    "group_by_id": {
        "title": "Group By ID (Full)",
        "category": "groups",
        "req": "ProtoGroupByIdReq",
        "res": "ProtoGroupByIdRes",
        "req_pt": 475, "res_pt": 476,
        "description": "Returns the full group object including all symbol-level configuration overrides.",
        "req_fields": [("groupId", "int64", "required", "Group internal ID")],
        "res_fields": [("group", "ProtoGroup", "Full group object with symbol overrides")],
        "notes": "Heavy response — cache aggressively. Use LightGroupList for lists."
    },
    "symbol_list": {
        "title": "Symbol List",
        "category": "symbols",
        "req": "ProtoManagerSymbolListReq",
        "res": "ProtoManagerSymbolListRes",
        "req_pt": 467, "res_pt": 468,
        "description": "Returns all symbols configured on the trading server.",
        "req_fields": [],
        "res_fields": [("symbol", "ProtoManagerSymbol[]", "All symbols with full configuration")],
        "notes": "Includes all fields: spread, swaps, commissions, margins, trading hours, LP routing."
    },
    "symbol_category_list": {
        "title": "Symbol Category List",
        "category": "symbols",
        "req": "ProtoSymbolCategoryListReq",
        "res": "ProtoSymbolCategoryListRes",
        "req_pt": 463, "res_pt": 464,
        "description": "Returns all symbol categories used to organize the symbol tree in cTrader.",
        "req_fields": [],
        "res_fields": [("symbolCategory", "ProtoSymbolCategory[]", "Category ID, name, sorting")],
        "notes": "Used to build the symbol tree in trading terminals."
    },
    "asset_list": {
        "title": "Asset List",
        "category": "assets",
        "req": "ProtoAssetListReq",
        "res": "ProtoAssetListRes",
        "req_pt": 465, "res_pt": 466,
        "description": "Returns all assets (currencies, commodities, indices) configured on the server.",
        "req_fields": [],
        "res_fields": [("asset", "ProtoAsset[]", "Asset ID, name, digits, display name")],
        "notes": "Assets are referenced by symbolId in deals and positions via depositAssetId."
    },
    "asset_class_list": {
        "title": "Asset Class List",
        "category": "assets",
        "req": "ProtoAssetClassListReq",
        "res": "ProtoAssetClassListRes",
        "req_pt": 437, "res_pt": 438,
        "description": "Returns all asset classes (Forex, Indices, Commodities, etc.).",
        "req_fields": [],
        "res_fields": [("assetClass", "ProtoAssetClass[]", "Asset class ID and name")],
        "notes": "Asset classes group assets and symbols for display and margin purposes."
    },
    "manager_list": {
        "title": "Manager List",
        "category": "managers",
        "req": "ProtoManagerListReq",
        "res": "ProtoManagerListRes",
        "req_pt": 411, "res_pt": 412,
        "description": "Returns all manager accounts configured on the server.",
        "req_fields": [],
        "res_fields": [("manager", "ProtoManager[]", "Manager ID, login, name, permissions")],
        "notes": "Includes all managers regardless of group scope. Use to audit manager permissions."
    },
    "country_list": {
        "title": "Country List",
        "category": "reference",
        "req": "ProtoCountryListReq",
        "res": "ProtoCountryListRes",
        "req_pt": 435, "res_pt": 436,
        "description": "Returns all countries available for trader registration.",
        "req_fields": [],
        "res_fields": [("country", "ProtoCountry[]", "Country ID, name, two-letter code")],
        "notes": "Country IDs are used in ProtoTrader.countryId."
    },
    "open_position_list": {
        "title": "Open Position List",
        "category": "positions",
        "req": "ProtoPositionListReq",
        "res": "ProtoPositionListRes",
        "req_pt": 407, "res_pt": 408,
        "description": "Returns open positions opened within the given time window.",
        "req_fields": [
            ("traderId",       "int64",  "optional", "Filter by trader — omit for all"),
            ("fromTimestamp",  "int64",  "required", "Window start — Unix ms"),
            ("toTimestamp",    "int64",  "required", "Window end — Unix ms"),
        ],
        "res_fields": [
            ("traderId",  "int64",          "Echoed from request (if filtered)"),
            ("position",  "ProtoPosition[]","Open position objects"),
            ("hasMore",   "bool",           "Paginate by advancing fromTimestamp"),
        ],
        "notes": "Only returns currently open positions. For closed positions use ManagerClosedPositionList."
    },
    "closed_position_list": {
        "title": "Closed Position List",
        "category": "positions",
        "req": "ProtoManagerClosedPositionListReq",
        "res": "ProtoManagerClosedPositionListRes",
        "req_pt": 720, "res_pt": 721,
        "description": "Returns closed positions within the given time window.",
        "req_fields": [
            ("fromTimestamp", "int64", "required", "Close time window start — Unix ms"),
            ("toTimestamp",   "int64", "required", "Close time window end — Unix ms"),
            ("traderId",      "int64", "optional", "Filter by trader"),
        ],
        "res_fields": [
            ("position", "ProtoPosition[]", "Closed position objects"),
            ("hasMore",  "bool",            "Paginate if true"),
        ],
        "notes": "Timestamps refer to position close time. For P&L details see closePositionDetail inside deals."
    },
    "position_details_lite": {
        "title": "Position Details Lite",
        "category": "positions",
        "req": "ProtoPositionDetailsLiteReq",
        "res": "ProtoPositionDetailsLiteRes",
        "req_pt": 754, "res_pt": 755,
        "description": "Returns swap history and SL/TP change history for a specific position.",
        "req_fields": [("positionId", "int64", "required", "Position internal ID")],
        "res_fields": [
            ("position",                      "ProtoPosition",                      "The position snapshot"),
            ("stopLossTakeProfitChangeRecord", "ProtoStopLossTakeProfitChangeRecord[]", "SL/TP modification history"),
            ("swapCalculationRecord",          "ProtoSwapCalculationRecord[]",        "Daily swap charge records"),
        ],
        "notes": "Useful for audit trails and P&L breakdown by swap vs. price movement."
    },
    "deal_list_by_position": {
        "title": "Deal List By Position ID",
        "category": "deals",
        "req": "ProtoManagerDealListByPositionIdReq",
        "res": "ProtoManagerDealListByPositionIdRes",
        "req_pt": 459, "res_pt": 460,
        "description": "Returns all deals associated with a specific position.",
        "req_fields": [
            ("positionId",    "int64", "required", "Position internal ID"),
            ("fromTimestamp", "int64", "required", "Window start — Unix ms"),
            ("toTimestamp",   "int64", "required", "Window end — Unix ms"),
        ],
        "res_fields": [
            ("deal",    "ProtoDeal[]", "Deals linked to this position"),
            ("hasMore", "bool",       "Paginate if true"),
        ],
        "notes": "Includes opening deal, partial closes, and the final closing deal."
    },
    "pending_order_list": {
        "title": "Pending Order List",
        "category": "orders",
        "req": "ProtoPendingOrderListReq",
        "res": "ProtoPendingOrderListRes",
        "req_pt": 409, "res_pt": 410,
        "description": "Returns all pending (limit/stop) orders within the time window.",
        "req_fields": [
            ("traderId",      "int64", "optional", "Filter by trader"),
            ("fromTimestamp", "int64", "required", "Window start — Unix ms"),
            ("toTimestamp",   "int64", "required", "Window end — Unix ms"),
        ],
        "res_fields": [
            ("traderId", "int64",       "Echoed from request"),
            ("order",    "ProtoOrder[]","Pending orders"),
            ("hasMore",  "bool",        "Paginate if true"),
        ],
        "notes": "Only returns PENDING orders (LIMIT, STOP, STOP_LIMIT). Use OrderManagerList for executed orders."
    },
    "order_manager_list": {
        "title": "Order Manager List (All Orders)",
        "category": "orders",
        "req": "ProtoOrderManagerListReq",
        "res": "ProtoOrderManagerListRes",
        "req_pt": 443, "res_pt": 444,
        "description": "Returns all orders (pending + executed + cancelled) within the time window.",
        "req_fields": [
            ("fromTimestamp", "int64", "required", "Window start — Unix ms"),
            ("toTimestamp",   "int64", "required", "Window end — Unix ms"),
            ("traderId",      "int64", "optional", "Filter by trader"),
        ],
        "res_fields": [
            ("order",   "ProtoOrder[]", "All order objects"),
            ("hasMore", "bool",         "Paginate if true"),
        ],
        "notes": "Broadest order query. Useful for full activity audit."
    },
    "order_details": {
        "title": "Order Details",
        "category": "orders",
        "req": "ProtoOrderDetailsReq",
        "res": "ProtoOrderDetailsRes",
        "req_pt": 321, "res_pt": 322,
        "description": "Returns the full snapshot, associated deals, and action history for a single order.",
        "req_fields": [("orderId", "int64", "required", "Order internal ID")],
        "res_fields": [
            ("orderSnapshot", "ProtoOrder",        "Order state snapshot"),
            ("deal",          "ProtoDeal[]",        "Execution deals"),
            ("action",        "ProtoOrderAction[]", "Lifecycle action log"),
        ],
        "notes": "The most complete single-order view. Use for audit and investigation."
    },
    "deal_list": {
        "title": "Deal List",
        "category": "deals",
        "req": "ProtoManagerDealListReq",
        "res": "ProtoManagerDealListRes",
        "req_pt": 431, "res_pt": 432,
        "description": "Returns deals within the time window. Supports filtering by trader, group, and deal type.",
        "req_fields": [
            ("traderId",                "int64[]", "optional", "Repeated — filter by one or more traders"),
            ("fromTimestamp",           "int64",   "required", "Window start — Unix ms"),
            ("toTimestamp",             "int64",   "required", "Window end — Unix ms"),
            ("maxRows",                 "int32",   "optional", "Cap result set (default: server max)"),
            ("closingDealsOnly",        "bool",    "optional", "Return only closing deals (default: false)"),
            ("includeAdditionalVolumes","bool",    "optional", "Include volume breakdown (default: false)"),
            ("withFilledVolumeOnly",    "bool",    "optional", "Exclude zero-fill deals (default: false)"),
            ("groupId",                 "int64[]", "optional", "Repeated — filter by group"),
        ],
        "res_fields": [
            ("deal",    "ProtoDeal[]", "Deal objects"),
            ("hasMore", "bool",        "Paginate by advancing fromTimestamp using last deal's createTimestamp"),
        ],
        "notes": "Paginate by advancing fromTimestamp to the last deal's createTimestamp. Always set maxRows to avoid huge responses."
    },
    "get_deal": {
        "title": "Get Deal By ID",
        "category": "deals",
        "req": "ProtoManagerGetDealReq",
        "res": "ProtoManagerGetDealRes",
        "req_pt": 709, "res_pt": 711,
        "description": "Fetches a single deal by its ID.",
        "req_fields": [("dealId", "uint64", "required", "Deal internal ID")],
        "res_fields": [("deal", "ProtoDeal", "The deal object")],
        "notes": "Fast single-deal lookup. Prefer this over DealList when you have the dealId."
    },
    "balance_history_list": {
        "title": "Balance History List",
        "category": "balance",
        "req": "ProtoBalanceHistoryListReq",
        "res": "ProtoBalanceHistoryListRes",
        "req_pt": 417, "res_pt": 418,
        "description": "Returns deposit, withdrawal, and balance adjustment records.",
        "req_fields": [
            ("traderId",      "int64", "optional", "Filter by trader"),
            ("fromTimestamp", "int64", "required", "Window start — Unix ms"),
            ("toTimestamp",   "int64", "required", "Window end — Unix ms"),
        ],
        "res_fields": [
            ("traderId",         "int64",                 "Echoed from request"),
            ("depositWithdraw",  "ProtoDepositWithdraw[]","Balance operation records"),
            ("hasMore",          "bool",                   "Paginate if true"),
        ],
        "notes": "Includes deposits, withdrawals, manual balance adjustments, and realized P&L from closed positions."
    },
    "bonus_history_list": {
        "title": "Bonus History List",
        "category": "balance",
        "req": "ProtoBonusHistoryListReq",
        "res": "ProtoBonusHistoryListRes",
        "req_pt": 786, "res_pt": 787,
        "description": "Returns bonus credit/debit history.",
        "req_fields": [
            ("traderId",      "int64", "optional", "Filter by trader"),
            ("fromTimestamp", "int64", "required", "Window start — Unix ms"),
            ("toTimestamp",   "int64", "required", "Window end — Unix ms"),
        ],
        "res_fields": [("bonusDepositWithdraw", "ProtoBonusDepositWithdraw[]", "Bonus operation records")],
        "notes": "Bonus balances are separate from cash balance. isWithdrawable=false means non-withdrawable bonus."
    },
    "server_settings": {
        "title": "Server Settings",
        "category": "configuration",
        "req": "ProtoServerSettingsReq",
        "res": "ProtoServerSettingsRes",
        "req_pt": 423, "res_pt": 424,
        "description": "Returns the global server configuration including trading rules, margining, and session times.",
        "req_fields": [],
        "res_fields": [("settings", "ProtoServerSettings", "Full server settings object")],
        "notes": "Rarely changes. Cache and invalidate on ProtoServerSettingsChangedEvent."
    },
    "dealing_settings": {
        "title": "Dealing Settings",
        "category": "configuration",
        "req": "ProtoDealingSettingsReq",
        "res": "ProtoDealingSettingsRes",
        "req_pt": 816, "res_pt": 817,
        "description": "Returns current manual dealing configuration: which symbols require manual execution, timeouts, gap tolerances.",
        "req_fields": [],
        "res_fields": [
            ("alwaysManualEnabled",    "bool",                  "Global manual dealing flag"),
            ("minGapTolerance",        "int32",                 "Minimum gap tolerance in points"),
            ("maxGapTolerance",        "int32",                 "Maximum gap tolerance in points"),
            ("symbol",                 "ProtoDealingSymbol[]",  "Per-symbol manual dealing config"),
            ("manualDealTimeout",      "int64",                 "Timeout before auto-action (ms)"),
            ("manualDealTimeoutAction","ProtoManualDealTimeoutAction", "Action on timeout"),
        ],
        "notes": "Required before building a dealer workstation. Subscribe to ProtoDealingSettingsUpdatedEvent for real-time changes."
    },
    "manual_deal_list": {
        "title": "Manual Deal List (Dealer Queue)",
        "category": "dealing",
        "req": "ProtoManualDealListReq",
        "res": "ProtoManualDealListRes",
        "req_pt": 821, "res_pt": 822,
        "description": "Returns pending manual deals awaiting dealer execution or rejection.",
        "req_fields": [],
        "res_fields": [("deal", "ProtoManualDeal[]", "Pending manual deals in the dealer queue")],
        "notes": "Real-time updates arrive via ProtoNewManualDealEvent. This call is for initial queue state. Claim deals with ManualDealClaimReq before executing."
    },
    "exposure_symbols": {
        "title": "Exposure Symbol List",
        "category": "risk",
        "req": "ProtoExposureSymbolListReq",
        "res": "ProtoExposureSymbolListRes",
        "req_pt": 419, "res_pt": 420,
        "description": "Returns the current net exposure per symbol across all open positions.",
        "req_fields": [],
        "res_fields": [("exposureSymbol", "ProtoExposureSymbol[]", "Symbol ID + net volume + net side")],
        "notes": "Critical for risk monitoring. Updated in near real-time. Use ProtoExecutionEvent to maintain live state."
    },
    "liquidity_feeds": {
        "title": "Liquidity Feed List",
        "category": "configuration",
        "req": "ProtoLiquidityFeedListReq",
        "res": "ProtoLiquidityFeedListRes",
        "req_pt": 429, "res_pt": 430,
        "description": "Returns all configured liquidity provider feeds.",
        "req_fields": [],
        "res_fields": [("liquidityFeed", "ProtoLiquidityFeed[]", "LP feed name, ID, type, status")],
        "notes": "LiquidityFeedId is referenced in symbol routing configuration."
    },
    "liquidity_feed_symbols": {
        "title": "Liquidity Feed Symbol List",
        "category": "configuration",
        "req": "ProtoLiquidityFeedSymbolListReq",
        "res": "ProtoLiquidityFeedSymbolListRes",
        "req_pt": 489, "res_pt": 490,
        "description": "Returns the symbol-to-LP-feed mapping for execution routing.",
        "req_fields": [],
        "res_fields": [("liquidityFeedSymbol", "ProtoLiquidityFeedSymbol[]", "Symbol ID + feed ID + routing config")],
        "notes": "Used to understand B-book / A-book routing per symbol."
    },
    "price_stream_list": {
        "title": "Price Stream List",
        "category": "configuration",
        "req": "ProtoPriceStreamListReq",
        "res": "ProtoPriceStreamListRes",
        "req_pt": 427, "res_pt": 428,
        "description": "Returns all configured price streams (internal price feeds from LPs).",
        "req_fields": [],
        "res_fields": [("priceStream", "ProtoPriceStream[]", "Price stream name, ID, source type")],
        "notes": "Price streams aggregate quotes from LPs and are distributed to symbols."
    },
    "schedule_profiles": {
        "title": "Schedule Profile List",
        "category": "profiles",
        "req": "ProtoScheduleProfileListReq",
        "res": "ProtoScheduleProfileListRes",
        "req_pt": 363, "res_pt": 364,
        "description": "Returns all trading schedule profiles defining market hours per symbol.",
        "req_fields": [],
        "res_fields": [("scheduleProfile", "ProtoScheduleProfile[]", "Profile ID, name, sessions, holidays")],
        "notes": "Assigned to symbols to control when trading is open/closed."
    },
    "commission_profiles": {
        "title": "Commission Profile List",
        "category": "profiles",
        "req": "ProtoCommissionProfileListReq",
        "res": "ProtoCommissionProfileListRes",
        "req_pt": 368, "res_pt": 369,
        "description": "Returns all commission profiles defining fees per trade.",
        "req_fields": [],
        "res_fields": [("commissionProfile", "ProtoCommissionProfile[]", "Profile ID, name, tiers, calc type")],
        "notes": "Commission profiles are assigned to groups and override at symbol level."
    },
    "volume_profiles": {
        "title": "Volume Profile List",
        "category": "profiles",
        "req": "ProtoVolumeProfileListReq",
        "res": "ProtoVolumeProfileListRes",
        "req_pt": 378, "res_pt": 379,
        "description": "Returns all volume (lot size) profiles.",
        "req_fields": [],
        "res_fields": [("volumeProfile", "ProtoVolumeProfile[]", "Profile ID, name, lot step, min/max volume")],
        "notes": "Controls minimum lot size, lot step, and maximum lot size per symbol group."
    },
    "execution_profiles": {
        "title": "Execution Profile List",
        "category": "profiles",
        "req": "ProtoExecutionProfileListReq",
        "res": "ProtoExecutionProfileListRes",
        "req_pt": 383, "res_pt": 384,
        "description": "Returns all execution profiles defining how orders are filled.",
        "req_fields": [],
        "res_fields": [("executionProfile", "ProtoExecutionProfile[]", "Profile ID, name, slippage, requote policy")],
        "notes": "Execution mode (instant/market), max deviation, and partial fill policy."
    },
    "protection_profiles": {
        "title": "Protection Profile List",
        "category": "profiles",
        "req": "ProtoProtectionProfileListReq",
        "res": "ProtoProtectionProfileListRes",
        "req_pt": 388, "res_pt": 389,
        "description": "Returns all protection (margin / stop-out) profiles.",
        "req_fields": [],
        "res_fields": [("protectionProfile", "ProtoProtectionProfile[]", "Profile ID, name, margin call %, stop-out %")],
        "notes": "Controls when margin call warnings are issued and when stop-outs occur."
    },
    "swap_free_profiles": {
        "title": "Swap-Free Profile List",
        "category": "profiles",
        "req": "ProtoSwapFreeProfileListReq",
        "res": "ProtoSwapFreeProfileListRes",
        "req_pt": 393, "res_pt": 394,
        "description": "Returns swap-free (Islamic account) profiles.",
        "req_fields": [],
        "res_fields": [("swapFreeProfile", "ProtoSwapFreeProfile[]", "Profile ID, name, storage charge settings")],
        "notes": "Swap-free accounts pay a storage charge instead of overnight swap."
    },
    "holiday_list": {
        "title": "Holiday List",
        "category": "profiles",
        "req": "ProtoHolidayListReq",
        "res": "ProtoHolidayListRes",
        "req_pt": 398, "res_pt": 399,
        "description": "Returns all configured market holidays.",
        "req_fields": [],
        "res_fields": [("holiday", "ProtoHoliday[]", "Date, name, affected symbols/profiles")],
        "notes": "Holidays override trading schedules. Referenced by ProtoScheduleProfile."
    },
    "holiday_profiles": {
        "title": "Holiday Profile List",
        "category": "profiles",
        "req": "ProtoHolidayProfileListReq",
        "res": "ProtoHolidayProfileListRes",
        "req_pt": 447, "res_pt": 448,
        "description": "Returns holiday profiles that bundle multiple holidays.",
        "req_fields": [],
        "res_fields": [("holidayProfile", "ProtoHolidayProfile[]", "Profile ID, name, holidays list")],
        "notes": "Holiday profiles are assigned to schedule profiles."
    },
    "dynamic_leverage_list": {
        "title": "Dynamic Leverage List",
        "category": "profiles",
        "req": "ProtoDynamicLeverageListReq",
        "res": "ProtoDynamicLeverageListRes",
        "req_pt": 469, "res_pt": 470,
        "description": "Returns dynamic leverage tiers — where leverage decreases as position size grows.",
        "req_fields": [],
        "res_fields": [("dynamicLeverage", "ProtoDynamicLeverage[]", "Profile ID, name, volume tiers + leverage values")],
        "notes": "Applied per-symbol. Required for risk management in heavily leveraged accounts."
    },
    "gsl_schedule_list": {
        "title": "GSL Schedule List",
        "category": "profiles",
        "req": "ProtoGslScheduleListReq",
        "res": "ProtoGslScheduleListRes",
        "req_pt": 471, "res_pt": 472,
        "description": "Returns Guaranteed Stop Loss (GSL) schedules defining when GSL orders are available.",
        "req_fields": [],
        "res_fields": [("gslSchedule", "ProtoGslSchedule[]", "Schedule ID, name, availability windows")],
        "notes": "GSL is a premium feature where the broker guarantees SL execution at the specified price."
    },
    "light_swap_profiles": {
        "title": "Swap & Dividend Profile List (Light)",
        "category": "profiles",
        "req": "ProtoLightSwapAndDividendProfileListReq",
        "res": "ProtoLightSwapAndDividendProfileListRes",
        "req_pt": 493, "res_pt": 494,
        "description": "Returns a lightweight list of swap and dividend profiles (ID + name only).",
        "req_fields": [],
        "res_fields": [("profile", "ProtoLightSwapAndDividendProfile[]", "Profile ID and name")],
        "notes": "For full swap rates per symbol, use SwapAndDividendProfileById."
    },
    "recalc_account_margin": {
        "title": "Recalculate Account Margin",
        "category": "risk",
        "req": "ProtoRecalculateAccountMarginReq",
        "res": "ProtoRecalculateAccountMarginRes",
        "req_pt": 336, "res_pt": 337,
        "description": "Triggers a margin recalculation for a specific trader account.",
        "req_fields": [("traderId", "int64", "required", "Trader to recalculate")],
        "res_fields": [("usedMargin", "uint64", "Recalculated used margin in cents")],
        "notes": "Use sparingly — triggers a server-side recalculation. Good for debugging margin discrepancies."
    },
}

def generate_md_file(endpoint_key, meta, capture_result, all_captures):
    title       = meta.get("title", endpoint_key)
    category    = meta.get("category", "misc")
    req_name    = meta.get("req", "")
    res_name    = meta.get("res", "")
    req_pt      = meta.get("req_pt", 0)
    res_pt      = meta.get("res_pt", 0)
    description = meta.get("description", "")
    req_fields  = meta.get("req_fields", [])
    res_fields  = meta.get("res_fields", [])
    notes       = meta.get("notes", "")

    ok      = capture_result.get("ok", False)
    err_msg = capture_result.get("error", "")
    raw     = capture_result.get("fields", {})

    # ── Request fields table
    if req_fields:
        req_table = "| Field | Type | Required | Description |\n|-------|------|----------|-------------|\n"
        for row in req_fields:
            if len(row) == 4:
                req_table += f"| `{row[0]}` | `{row[1]}` | {row[2]} | {row[3]} |\n"
            elif len(row) == 2:
                req_table += f"| `{row[0]}` | `{row[1]}` | — | — |\n"
            else:
                req_table += f"| `{row[0]}` | `{row[1]}` | {row[2]} | — |\n"
    else:
        req_table = "_No request fields — send empty payload._"

    # ── Response fields table
    if res_fields:
        res_table = "| Field | Type | Description |\n|-------|------|-------------|\n"
        for row in res_fields:
            res_table += f"| `{row[0]}` | `{row[1]}` | {row[2]} |\n"
    else:
        res_table = "_Response fields not yet documented._"

    # ── Live response sample
    if ok and raw:
        live_sample = json_block({k: (v[:2] if isinstance(v, list) and len(v) > 2 else v) for k, v in raw.items()})
        status_badge = "✅ Live"
    elif ok:
        live_sample = "_Connected successfully but response was empty._"
        status_badge = "✅ Live (empty)"
    else:
        live_sample = f"```\nERROR: {err_msg}\n```"
        status_badge = "⚠️ Error captured"

    # ── Python example code
    py_inner_args = ""
    for row in req_fields:
        if len(row) >= 3 and "required" in row[2].lower():
            fname = row[0]
            ftype = row[1] if len(row) > 1 else "int64"
            if "timestamp" in fname.lower():
                py_inner_args += f"\n    + encode_int64({get_field_num(fname)}, from_ts)  # fromTimestamp"
            elif "bool" in ftype:
                py_inner_args += f"\n    + encode_bool({get_field_num(fname)}, False)"
            else:
                py_inner_args += f"\n    + encode_int64({get_field_num(fname)}, value)"

    py_code = f'''```python
import ssl, socket, struct, hashlib, time
from capture_manager_api import (
    ManagerAPIClient, encode_int64, encode_string,
    PT, parse_message, fields_to_dict
)

c = ManagerAPIClient()
c.connect()  # authenticates automatically

now_ms = int(time.time() * 1000)
from_ms = now_ms - 7 * 86400 * 1000  # 7 days ago

inner = (
    b""  # add fields here, e.g. encode_int64(2, from_ms) + encode_int64(3, now_ms)
)

fields = c.request(
    PT["{next((k for k,v in PT.items() if v==req_pt), str(req_pt))}"],
    PT["{next((k for k,v in PT.items() if v==res_pt), str(res_pt))}"],
    inner
)
result = fields_to_dict(fields)
print(result)

c.close()
```'''

    content = f"""# {title}

**Category:** {category} &nbsp;|&nbsp; **Status:** {status_badge}

## Description

{description}

---

## Request — `{req_name}` (payloadType `{req_pt}`)

### Request Fields

{req_table}

### Python Example

{py_code}

---

## Response — `{res_name}` (payloadType `{res_pt}`)

### Response Fields

{res_table}

### Live Response Sample

{live_sample}

---

## Error Handling

| Scenario | Error | Action |
|----------|-------|--------|
| Invalid credentials | `AUTHENTICATION_FAILED (3)` | Re-authenticate |
| Wrong traderId / ID | `TRADER_NOT_FOUND (11)` or `ENTITY_NOT_FOUND (6)` | Validate ID exists first |
| Rate limit hit | `REQUEST_FREQUENCY_EXCEEDED (23)` | Back off and retry with jitter |
| Permissions denied | `NOT_ENOUGH_RIGHTS (2)` | Check manager permission list |
| Connection dropped | `ConnectionError` / socket timeout | Reconnect with exponential backoff |
| Frame too large | `FRAME_TOO_LONG (8)` | Reduce time window / add `maxRows` |

```python
try:
    fields = c.request(
        PT["{next((k for k,v in PT.items() if v==req_pt), str(req_pt))}"],
        PT["{next((k for k,v in PT.items() if v==res_pt), str(res_pt))}"],
        inner
    )
except RuntimeError as e:
    if "AUTHENTICATION_FAILED" in str(e):
        c.connect()   # re-authenticate
    elif "REQUEST_FREQUENCY_EXCEEDED" in str(e):
        time.sleep(1)
    else:
        raise
except TimeoutError:
    # reconnect
    c.close()
    c.connect()
```

---

## Notes

{notes}

---

*Captured: {datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")} — OpoFinance live environment*
"""
    return content

def get_field_num(fname):
    mapping = {
        "fromTimestamp": 2, "toTimestamp": 3, "traderId": 2, "positionId": 2,
        "orderId": 2, "dealId": 2, "groupId": 2, "managerId": 2, "symbolId": 2,
    }
    return mapping.get(fname, 2)

# ─── Generate all files ───────────────────────────────────────────────────────
def generate_all_files(captures):
    print("\n── Writing markdown files ───────────────────────────────────────")

    for key, meta in ENDPOINT_DOCS.items():
        cap = captures.get(key, {'ok': False, 'error': 'Not captured'})
        md = generate_md_file(key, meta, cap, captures)
        write_md(f"{key}.md", md)

    # ── Index / README
    categories = {}
    for key, meta in ENDPOINT_DOCS.items():
        cat = meta.get("category", "misc")
        categories.setdefault(cat, []).append((key, meta.get("title", key), captures.get(key, {})))

    summary_rows = []
    for cat, items in sorted(categories.items()):
        for key, title, cap in items:
            ok = cap.get("ok", False)
            badge = "✅" if ok else "⚠️"
            summary_rows.append(f"| {badge} | [{title}]({key}.md) | `{ENDPOINT_DOCS[key]['req']}` | {cat} |")

    readme = f"""# cTrader Manager API — Complete Reference

Captured live from the OpoFinance environment on {datetime.now(timezone.utc).strftime("%Y-%m-%d")}.

## Connection

| Parameter | Value |
|-----------|-------|
| Host | `live-managerapi.p.ctrader.com` |
| Port | `5011` |
| Protocol | Protobuf over TCP + TLS |
| Auth | MD5 password hash + plantId + environmentName |
| Heartbeat | Every 25 seconds (payloadType=51) |

## Quick Start

```python
from capture_manager_api import ManagerAPIClient, PT, encode_int64, fields_to_dict
import time

c = ManagerAPIClient()
c.connect()

now_ms = int(time.time() * 1000)
fields = c.request(
    PT['SERVER_TIME_REQ'],
    PT['SERVER_TIME_RES']
)
print(fields_to_dict(fields))
c.close()
```

## All Endpoints

| Status | Endpoint | Request Message | Category |
|--------|----------|-----------------|----------|
{"".join(r + chr(10) for r in summary_rows)}

## Wire Format

```
[4 bytes big-endian length N][N bytes: serialized ProtoMessage]

ProtoMessage {{
  field 1 (uint32):  payloadType   ← identifies inner message
  field 2 (bytes):   payload       ← serialized inner message
  field 3 (string):  clientMsgId   ← optional, for req/res matching
}}
```

## Pagination Pattern

All list endpoints that return `hasMore=true` must be paginated:

```python
from_ts = 30_days_ago_ms
while True:
    inner = encode_int64(2, from_ts) + encode_int64(3, now_ms)
    fields = c.request(PT['DEAL_LIST_REQ'], PT['DEAL_LIST_RES'], inner)
    process(fields)
    has_more = fields.get(3, [False])[0]
    if not has_more:
        break
    # Advance cursor to last record's timestamp
    last_deal = parse_message(fields[2][-1])
    from_ts = last_deal[8][0]  # createTimestamp
```

## Key Entity Cross-Reference

| Entity | Request | payloadType | Key ID field |
|--------|---------|-------------|--------------|
| Trader (Account) | `ProtoTraderListReq` | 403 | `traderId` |
| Group | `ProtoLightGroupListReq` | 473 | `groupId` |
| Symbol | `ProtoManagerSymbolListReq` | 467 | `symbolId` |
| Asset | `ProtoAssetListReq` | 465 | `assetId` |
| Position | `ProtoPositionListReq` | 407 | `positionId` |
| Deal | `ProtoManagerDealListReq` | 431 | `dealId` |
| Order | `ProtoOrderManagerListReq` | 443 | `orderId` |
| Balance Op | `ProtoBalanceHistoryListReq` | 417 | `balanceHistoryId` |

See [error-codes.md](../error-codes.md) for full error reference.
See [events.md](events.md) for all server-pushed events.
"""
    write_md("README.md", readme)

    # ── Error codes file
    write_md("error-codes.md", ERROR_CODES_MD)

    # ── Events file
    write_md("events.md", EVENTS_MD)

    # ── Enums file
    write_md("enums.md", ENUMS_MD)

    # ── Entity structures
    write_md("entities.md", ENTITIES_MD)

# ─── Static docs ──────────────────────────────────────────────────────────────
ERROR_CODES_MD = """# Error Codes

## ProtoErrorCode (Transport-level — from ErrorRes payloadType=50)

| Code | Name | Description |
|------|------|-------------|
| 1 | UNKNOWN_ERROR | Unknown error |
| 2 | UNSUPPORTED_MESSAGE | Message type not supported by this server |
| 3 | INVALID_REQUEST | Malformed or missing required fields |
| 4 | WRONG_PASSWORD | Authentication failure |
| 5 | TIMEOUT_ERROR | Server-side timeout |
| 6 | ENTITY_NOT_FOUND | Referenced entity does not exist |
| 7 | CANT_ROUTE_REQUEST | Internal routing failure |
| 8 | FRAME_TOO_LONG | Message frame exceeds server limit — reduce time window |
| 9 | MARKET_CLOSED | Trading not available |
| 10 | CONCURRENT_MODIFICATION | Optimistic lock conflict — retry |
| 11 | BLOCKED_PAYLOAD_TYPE | This payload type is not permitted |
| 12 | DATASTORE_IS_NOT_AVAILABLE | Server datastore unavailable |

## ProtoCSErrorCode (Business-level — from ProtoExecutionEvent.errorCode)

| Code | Name | Description |
|------|------|-------------|
| 1 | NOT_ENOUGH_MONEY | Insufficient balance |
| 2 | NOT_ENOUGH_RIGHTS | Permission denied |
| 3 | AUTHENTICATION_FAILED | Wrong credentials or expired session |
| 4 | POSITION_NOT_FOUND | Invalid position ID |
| 5 | POSITION_LOCKED | Position being modified by another process |
| 6 | CHANGE_BALANCE_BAD_AMOUNT | Invalid balance operation amount |
| 7 | NO_QUOTES | No market data available |
| 8 | TRADING_DISABLED | Trading disabled on symbol or server |
| 9 | TRADING_NOT_ALLOWED | Trader does not have trading permission |
| 10 | TRADING_BAD_VOLUME | Volume outside allowed min/max/step |
| 11 | TRADER_NOT_FOUND | Invalid trader ID |
| 12 | TRADER_GROUP_NOT_FOUND | Invalid group ID |
| 13 | RECONCILIATION_IN_PROGRESS | System undergoing reconciliation |
| 14 | ALREADY_LOGGED_IN | Connection already established |
| 16 | TOO_MANY_POSITIONS | Position limit reached |
| 17 | ORDER_NOT_FOUND | Invalid order ID |
| 18 | TRADING_BAD_STOPS | SL/TP outside allowed distance |
| 19 | ALREADY_DELETED | Entity already deleted |
| 20 | WRONG_LEVERAGE | Leverage value not allowed |
| 21 | TRADING_BAD_EXPIRATION_DATE | Expiration time invalid |
| 22 | ALREADY_SUBSCRIBED | Already subscribed to this feed |
| 23 | REQUEST_FREQUENCY_EXCEEDED | **Rate limit** — back off and retry |
| 24 | POSITION_NOT_OPEN | Position already closed |
| 25 | WRONG_TIME_SEQUENCE | Timestamp out of order |
| 26 | FORBID_WITH_TRADING_ENABLED | Operation not allowed while trading active |
| 27 | INCORRECT_POSITION_ID | Position ID format error |
| 28 | TRADER_HAS_POSITIONS | Cannot delete trader with open positions |
| 29 | UNKNOWN_LIQIDITY_FEED | Invalid liquidity feed ID |
| 30 | ASSET_CLASS_ALREADY_EXIST | Duplicate asset class name |
| 31 | ASSET_CLASS_IS_NOT_EMPTY | Asset class has symbols assigned |
| 32 | TRADING_BAD_PRICES | Price outside valid range |
| 33 | UNABLE_TO_FORWARD_COMMAND | Internal routing failure |
| 34 | UNKNOWN_SYMBOL | Invalid symbol ID |
| 35 | INCORRECT_BOUNDARIES | Boundary validation failed |
| 36 | SYMBOL_NOT_FOUND | Symbol not found |
| 37 | DEAL_NOT_FOUND | Invalid deal ID |
| 38 | POSITION_CONCURRENT_CHANGE | Concurrent position modification |
| 39 | NOT_INTRODUCING_BROKER | Account is not an IB |
| 40 | INTRODUCING_BROKER_CYCLE | IB relationship cycle detected |
| 41 | UNABLE_TO_CANCEL_ORDER | Order cannot be cancelled in current state |
| 42 | UNABLE_TO_AMEND_ORDER | Order cannot be amended in current state |
| 43 | UNKNOWN_DEPOSIT_CURRENCY | Deposit currency not recognized |
| 44 | DEPOSIT_CURRENCY_NOT_ALLOWED | Currency not allowed for this account |
| 45 | SHORT_SELLING_NOT_ALLOWED | Short selling disabled for this symbol/account |
| 46 | CHANGE_BONUS_BAD_AMOUNT | Invalid bonus amount |
| 47 | SERVER_IS_UNDER_MAINTENANCE | Server in maintenance mode |
| 48 | TRADING_BAD_STAKE | Invalid stake (spread betting) |
| 50 | PROTECTION_IS_TOO_CLOSE_TO_MARKET | GSL protection too close to current price |
| 51 | ORDER_TYPE_NOT_ALLOWED | Order type not permitted on this symbol |
| 52 | INVALID_DATA | Generic invalid data error |
| 53 | NO_SUCH_LOGIN | Login number does not exist |
| 54 | MAX_EXPOSURE_REACHED | Broker exposure limit reached |
| 55 | PENDING_EXECUTION | Execution pending — await ExeCution event |
| 63 | CHANNEL_IS_BLOCKED | Trading channel (e.g. API) is blocked |
| 67 | CONNECTIONS_LIMIT_EXCEEDED | Too many simultaneous manager connections |
| 68 | WORSE_GSL_NOT_ALLOWED | Cannot move GSL to a worse price |
| 69 | SYMBOL_HAS_HOLIDAY | Symbol is on a configured holiday |

## Error Handling Pattern

```python
try:
    fields = c.request(req_pt, res_pt, inner)
except RuntimeError as e:
    msg = str(e)
    if "AUTHENTICATION_FAILED" in msg or "WRONG_PASSWORD" in msg:
        # Re-authenticate
        c.close()
        c.connect()
    elif "REQUEST_FREQUENCY_EXCEEDED" in msg:
        # Rate limited — exponential backoff
        time.sleep(random.uniform(1, 3))
    elif "TRADER_NOT_FOUND" in msg or "ENTITY_NOT_FOUND" in msg:
        # Bad ID — skip this record
        log.warning("entity_not_found", id=requested_id)
    elif "FRAME_TOO_LONG" in msg:
        # Shrink time window
        window = window // 2
    else:
        raise
except TimeoutError:
    c.close()
    c.connect()
except ConnectionError:
    c.close()
    time.sleep(5)
    c.connect()
```
"""

EVENTS_MD = """# Server-Pushed Events

Events arrive without a `clientMsgId`. They must be handled by a dispatch loop
separate from request/response correlation.

## Dispatch Pattern

```python
import threading

def event_loop(client):
    while client.connected:
        try:
            data = client._recv_frame()
            pt, payload, cid = proto_message_unwrap(data)
            if cid:
                client._pending[cid] = (pt, payload)  # response to a request
            else:
                dispatch_event(pt, payload)            # unsolicited event
        except Exception as e:
            handle_error(e)

def dispatch_event(payload_type, payload):
    handler = EVENT_HANDLERS.get(payload_type)
    if handler:
        handler(parse_message(payload))
    elif payload_type == PT['HEARTBEAT_EVENT']:
        pass  # ignore or echo back
    else:
        log.debug("unknown_event", pt=payload_type)
```

## All Events

| payloadType | Name | Trigger | Key Fields |
|-------------|------|---------|------------|
| 990 | `ProtoHelloEvent` | Sent immediately on connect | — |
| 51 | `ProtoHeartbeatEvent` | Every 25s if no other traffic | — |
| 300 | `ProtoExecutionEvent` | Any order/position/balance change | `executionType`, `position`, `order`, `deal`, `depositWithdraw` |
| 335 | `ProtoPositionMarginChangedEvent` | Position margin recalculated | `positionId`, `usedMargin`, `traderId` |
| 503 | `ProtoTraderChangedEvent` | Trader created/updated/deleted | `trader` (ProtoTrader) |
| 506 | `ProtoGroupChangedEvent` | Group created/updated/deleted | `group` (ProtoGroup) |
| 558 | `ProtoManagerSymbolChangedEvent` | Symbol created/updated/deleted | `symbol` (ProtoManagerSymbol) |
| 512 | `ProtoManagerChangedEvent` | Manager created/updated/deleted | `manager` (ProtoManager) |
| 518 | `ProtoServerSettingsChangedEvent` | Server settings updated | `settings` |
| 533 | `ProtoPriceStreamChangedEvent` | Price stream updated | `priceStream` |
| 561 | `ProtoDynamicLeverageChangedEvent` | Dynamic leverage profile updated | `dynamicLeverage` |
| 565 | `ProtoGSLScheduleChangedEvent` | GSL schedule updated | `gslSchedule` |
| 562 | `ProtoTraderPermissionLoseEvent` | Manager lost access to trader | `traderId` |
| 540 | `ProtoAssetChangedEvent` | Asset created/updated/deleted | `asset` |
| 547 | `ProtoLiquidityFeedSymbolChangedEvent` | LP feed-symbol link changed | `liquidityFeedSymbol` |
| 515 | `ProtoSwapAndDividendProfileChangedEvent` | Swap profile changed | profile ID |
| 730 | `ProtoTraderLogonEvent` | Trader logged in | `traderId`, `login`, timestamp |
| 731 | `ProtoTraderLogoutEvent` | Trader logged out | `traderId`, `login`, timestamp |
| 843 | `ProtoDealingSettingsUpdatedEvent` | Dealing config changed | full settings |
| 820 | `ProtoNewManualDealEvent` | New order queued for manual dealing | deal details |
| 825 | `ProtoManualDealClaimedEvent` | Manual deal claimed by manager | `dealId`, `managerId` |
| 828 | `ProtoManualDealUnclaimedEvent` | Manual deal released | `dealId` |
| 835 | `ProtoManualDealProcessedEvent` | Manual deal executed or rejected | `dealId`, result |
| 885 | `ProtoMaxAutoExecutionSizeProfileChangedEvent` | Max auto exec profile changed | profile data |
| 846 | `ProtoAssetClassChangedEvent` | Asset class created/updated | `assetClass` |
| 847 | `ProtoAssetClassDeletedEvent` | Asset class deleted | `assetClassId` |
| 848 | `ProtoSymbolCategoryChangedEvent` | Symbol category changed | `symbolCategory` |
| 849 | `ProtoSymbolCategoryDeletedEvent` | Symbol category deleted | `symbolCategoryId` |
| 575 | `ProtoSymbolArchivedEvent` | Symbol archived | `symbolId` |
| 580 | `ProtoSymbolRestoredEvent` | Symbol restored from archive | `symbolId` |
| 583 | `ProtoCrudTradeNotificationProfileChangedEvent` | Trade notification profile changed | profile data |

## ProtoExecutionEvent — Key Fields

```
field 2 (executionType)     — ProtoExecutionType enum
field 4 (position)          — ProtoPosition (optional)
field 5 (order)             — ProtoOrder (optional)
field 6 (errorCode)         — string, ProtoCSErrorCode name (optional)
field 7 (depositWithdraw)   — ProtoDepositWithdraw (optional, for balance ops)
field 8 (deal)              — ProtoDeal (optional)
field 9 (eventId)           — uint64 (optional)
field 11 (isServerEvent)    — bool
field 12 (depositToUsdRate) — double
```

## ProtoExecutionType Enum

| Value | Name |
|-------|------|
| 2 | ORDER_ACCEPTED |
| 3 | ORDER_FILLED |
| 4 | ORDER_CANCELLED |
| 5 | ORDER_EXPIRED |
| 6 | ORDER_AMENDED |
| 7 | ORDER_REJECTED |
| 8 | TRADE_OPENED |
| 9 | TRADE_CLOSED |
| 11 | BALANCE_DEPOSIT |
| 12 | BALANCE_WITHDRAW |
| 14 | STOP_OUT |
| 15 | CLOSE_POSITION |
| 16 | SWAP |
| 17 | ROLLOVER |
"""

ENUMS_MD = """# Enums

## ProtoOrderType
| Value | Name |
|-------|------|
| 1 | MARKET |
| 2 | LIMIT |
| 3 | STOP |
| 4 | STOP_LOSS_TAKE_PROFIT |
| 5 | MARKET_RANGE |
| 6 | STOP_LIMIT |

## ProtoTradeSide
| Value | Name |
|-------|------|
| 1 | BUY |
| 2 | SELL |

## ProtoTimeInForce
| Value | Name |
|-------|------|
| 1 | GOOD_TILL_DATE |
| 2 | GOOD_TILL_CANCEL |
| 3 | IMMEDIATE_OR_CANCEL |
| 4 | FILL_OR_KILL |
| 5 | MARKET_ON_OPEN |

## ProtoOrderStatus
| Value | Name |
|-------|------|
| 1 | ACCEPTED |
| 2 | FILLED |
| 3 | PARTIALLY_FILLED |
| 4 | CANCELLED |
| 5 | REJECTED |
| 6 | EXPIRED |
| 7 | INACTIVE |

## ProtoDealStatus
| Value | Name |
|-------|------|
| 2 | FILLED |
| 3 | PARTIALLY_FILLED |
| 4 | REJECTED |

## ProtoDealType
| Value | Name |
|-------|------|
| 1 | BUY |
| 2 | SELL |
| 3 | BUY_CANCELLED |
| 4 | SELL_CANCELLED |
| 5 | BALANCE_DEPOSIT |
| 6 | BALANCE_WITHDRAWAL |
| 7 | BONUS_DEPOSIT |
| 8 | BONUS_WITHDRAWAL |
| 9 | INITIAL_DEPOSIT |
| 10 | INITIAL_LOAD |
| 11 | AUTO_ROLLOVER_CLOSE |
| 12 | AUTO_ROLLOVER_OPEN |
| 34 | SWAP |
| 35 | COMMISSION |

## ProtoPositionStatus
| Value | Name |
|-------|------|
| 1 | OPEN |
| 2 | CLOSED |
| 3 | CREATED |

## ProtoBookType
| Value | Name |
|-------|------|
| 1 | BOOK_A |
| 2 | BOOK_B |

## ProtoAccountType
| Value | Name |
|-------|------|
| 1 | HEDGED |
| 2 | NETTED |

## ProtoAccessRights
| Value | Name |
|-------|------|
| 1 | FULL_ACCESS |
| 2 | CLOSE_ONLY |
| 3 | NO_TRADING |
| 4 | NO_LOGIN |

## ProtoCrudOperation
| Value | Name |
|-------|------|
| 1 | CREATE |
| 2 | UPDATE |
| 3 | DELETE |

## ProtoChangeBalanceType
| Value | Name |
|-------|------|
| 0 | BALANCE_DEPOSIT |
| 1 | BALANCE_WITHDRAW |
| 2 | BONUS_DEPOSIT |
| 3 | BONUS_WITHDRAW |
| 4 | INITIAL_DEPOSIT |
| 5 | INITIAL_LOAD |
| 6 | REVERSE_BALANCE_DEPOSIT |
| 7 | REVERSE_BALANCE_WITHDRAWAL |
| 8 | BONUS_CANCEL |
| 9 | MANAGER_BONUS_DEPOSIT |
| 10 | MANAGER_BONUS_WITHDRAW |

## ProtoOrderTriggerMethod
| Value | Name |
|-------|------|
| 1 | TRADE |
| 2 | OPPOSITE |
| 3 | DOUBLE_TRADE |
| 4 | DOUBLE_OPPOSITE |

## ProtoTotalMarginCalculationType
| Value | Name |
|-------|------|
| 1 | MAX |
| 2 | SUM |
| 3 | NET |

## ProtoManagerPermission
| Value | Name |
|-------|------|
| 1 | TRADE |
| 2 | ACCOUNT |
| 3 | HISTORY |
| 4 | REPORTING |
| 5 | SETTINGS |
| 6 | DEALING |
| 7 | LP |
| 8 | ADMIN |
"""

ENTITIES_MD = """# Core Entity Structures

## ProtoTrader (Account)

| Field # | Field Name | Type | Notes |
|---------|-----------|------|-------|
| 1 | traderId | int64 | Internal unique ID |
| 2 | login | int64 | Login number shown in cTrader |
| 3 | groupId | int64 | Group assignment |
| 8 | balance | int64 | Balance in cents |
| 9 | accountType | ProtoAccountType | HEDGED or NETTED |
| 10 | name | string | First name |
| 56 | lastName | string | Last name |
| 11 | passwordHash | string | MD5 hex |
| 12 | description | string | Internal note |
| 14 | countryId | int64 | Country reference |
| 16 | city | string | |
| 17 | address | string | |
| 18 | zipCode | string | |
| 19 | phone | string | |
| 21 | email | string | |
| 22 | documentId | string | KYC document number |
| 25 | registrationTimestamp | int64 | Unix ms |
| 26 | lastConnectTimestamp | int64 | Unix ms |
| 27 | online | bool | Currently connected |
| 28 | utcLastUpdateTimestamp | int64 | Unix ms |
| 29 | deleted | bool | Soft-deleted |
| 30 | balanceVersion | int64 | Optimistic lock |
| 47 | managerBonus | int64 | Manager bonus cents |
| 48 | ibBonus | int64 | IB bonus cents |
| 59 | accessRights | ProtoAccessRights | Trading permissions |
| 61 | depositAssetId | int64 | Deposit currency asset ID |
| 64 | swapFree | bool | Islamic account |
| 65 | nonWithdrawableBonus | int64 | Cents |
| 66 | leverageInCents | uint32 | e.g. 5000 = 50x |
| 74 | version | int64 | Entity version |
| 75 | subAccountOf | int64 | Parent account ID |
| 78 | isLimitedRisk | bool | No negative balance |
| 80 | moneyDigits | uint32 | Precision exponent |
| 85 | fairStopOut | bool | |

## ProtoDeal (Execution Record)

| Field # | Field Name | Type | Notes |
|---------|-----------|------|-------|
| 1 | dealId | int64 | |
| 2 | orderId | int64 | |
| 3 | positionId | int64 | |
| 4 | traderId | int64 | |
| 5 | volume | int64 | Ordered volume (cents of lot) |
| 6 | filledVolume | int64 | Actual filled (cents of lot) |
| 7 | symbolId | int64 | |
| 8 | createTimestamp | int64 | Unix ms — use for pagination |
| 9 | executionTimestamp | int64 | Unix ms |
| 10 | utcLastUpdateTimestamp | int64 | Unix ms |
| 11 | executionPrice | double | With markup |
| 12 | limitPrice | double | Requested price (if limit) |
| 13 | tradeSide | ProtoTradeSide | BUY or SELL |
| 14 | dealStatus | ProtoDealStatus | |
| 15 | dealType | ProtoDealType | |
| 16 | marginRate | double | Base-to-deposit conversion rate |
| 17 | commission | int64 | Cents |
| 19 | bookType | ProtoBookType | A or B |
| 20 | lpExecutionPrice | double | Without markup |
| 22 | label | string | Strategy label |
| 23 | channel | string | Execution channel |
| 24 | comment | string | |
| 32 | closePositionDetail | ProtoClosePositionDetail | Closing deals only |
| 35 | introducingBrokerCommission | int64 | Cents |
| 43 | markup | int64 | USD |
| 52 | manual | bool | Manually executed |
| 57 | equity | int64 | Account equity at deal time, cents |
| 58 | moneyDigits | uint32 | |

## ProtoPosition (Open/Closed Position)

| Field # | Field Name | Type | Notes |
|---------|-----------|------|-------|
| 1 | positionId | int64 | |
| 3 | tradeData | ProtoTradeData | Embedded — symbolId, volume, side, timestamps |
| 4 | positionStatus | ProtoPositionStatus | OPEN / CLOSED |
| 5 | swap | int64 | Accumulated swap cents |
| 6 | price | double | VWAP open price |
| 7 | stopLoss | double | 0 = none |
| 8 | takeProfit | double | 0 = none |
| 10 | utcLastUpdateTimestamp | int64 | Unix ms |
| 11 | bookType | ProtoBookType | |
| 13 | commission | int64 | Cents |
| 23 | usedMargin | uint64 | Cents |
| 24 | trailingStopLoss | bool | |
| 25 | stopLossTriggerMethod | ProtoOrderTriggerMethod | |
| 30 | moneyDigits | uint32 | |

## ProtoTradeData (embedded in Position and Order)

| Field # | Field Name | Type | Notes |
|---------|-----------|------|-------|
| 1 | symbolId | int64 | |
| 2 | volume | int64 | Cents of lot size |
| 3 | tradeSide | ProtoTradeSide | BUY or SELL |
| 4 | traderId | int64 | |
| 7 | openTimestamp | int64 | Unix ms |
| 8 | closeTimestamp | int64 | Unix ms (closed positions) |
| 12 | label | string | |
| 13 | comment | string | |
| 14 | channel | string | |
| 16 | lotSize | int64 | |

## ProtoOrder (Order)

| Field # | Field Name | Type | Notes |
|---------|-----------|------|-------|
| 1 | orderId | int64 | |
| 2 | tradeData | ProtoTradeData | |
| 3 | orderType | ProtoOrderType | |
| 4 | orderStatus | ProtoOrderStatus | |
| 6 | expirationTimestamp | int64 | Unix ms |
| 9 | executionPrice | double | |
| 10 | executedVolume | int64 | Cents |
| 11 | stopLoss | double | |
| 12 | takeProfit | double | |
| 13 | utcLastUpdateTimestamp | int64 | Unix ms |
| 14 | bookType | ProtoBookType | |
| 20 | closingOrder | bool | Closes a position |
| 21 | limitPrice | double | |
| 22 | stopPrice | double | |
| 23 | clientOrderId | string | Max 50 chars |
| 24 | commission | int64 | Cents |
| 26 | timeInForce | ProtoTimeInForce | |
| 30 | positionId | int64 | |
| 45 | isStopOut | bool | Triggered by stop-out |
| 46 | trailingStopLoss | bool | |
| 54 | moneyDigits | uint32 | |

## ProtoDepositWithdraw (Balance Operation)

| Field # | Field Name | Type | Notes |
|---------|-----------|------|-------|
| 1 | operationType | ProtoChangeBalanceType | |
| 2 | balanceHistoryId | int64 | |
| 3 | traderId | int64 | |
| 4 | balance | int64 | Balance after operation (cents) |
| 5 | delta | int64 | Operation amount (cents, + or -) |
| 6 | changeBalanceTimestamp | int64 | Unix ms |
| 7 | comment | string | Manager-only |
| 8 | externalNote | string | Visible to trader |
| 9 | balanceVersion | int64 | |
| 10 | equity | int64 | Account equity at time, cents |
| 14 | source | string | e.g. "VISA", "WIRE" |
| 15 | externalId | string | Reconciliation / CRM reference ID |
| 16 | moneyDigits | uint32 | |

## ProtoClosePositionDetail (inside ProtoDeal for closing deals)

| Field # | Field Name | Type | Notes |
|---------|-----------|------|-------|
| 2 | entryPrice | double | Original open price |
| 3 | swap | int64 | Realized swap at close (cents) |
| 4 | commission | int64 | Closing commission (cents) |
| 7 | profit | int64 | Gross profit (cents) |
| 8 | balance | int64 | Balance after close (cents) |
| 16 | closedVolume | int64 | |
| 18 | balanceVersion | int64 | |
| 23 | equity | int64 | Cents |
| 25 | netProfit | int64 | Cents |
| 43 | moneyDigits | uint32 | |
| 44 | pnlConversionFee | int64 | Cents |

## Money / Volume Encoding

All monetary values are stored as **integers in cents**:

```python
# Amount in currency units → cents
amount_cents = int(amount_float * 10 ** money_digits)

# Cents → currency units
amount_float = amount_cents / 10 ** money_digits

# moneyDigits=2 (USD, EUR): 123456 = $1,234.56
# moneyDigits=5 (BTC):      12345678 = 0.12345678 BTC
```

Volume is stored as **cents of the lot size**:
```python
# 1.00 lot, lotSize=100000 → volume = 100000 * 100 = 10000000
```
"""

# ─── Main ─────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print("=" * 60)
    print(" cTrader Manager API — Live Capture")
    print(f" {HOST}:{PORT}  login={LOGIN}  env={ENV_NAME}")
    print("=" * 60)

    try:
        captures = run_capture()
    except Exception as e:
        print(f"\nFATAL: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

    ok_count  = sum(1 for v in captures.values() if v.get('ok'))
    err_count = sum(1 for v in captures.values() if not v.get('ok'))
    print(f"\n── Capture summary: {ok_count} ok, {err_count} errors ──────────────────────")
    for k, v in captures.items():
        status = "✅" if v.get('ok') else f"❌ {v.get('error','?')[:50]}"
        print(f"  {k:<35} {status}")

    generate_all_files(captures)
    print(f"\n✅ All files written to: {OUT_DIR}")

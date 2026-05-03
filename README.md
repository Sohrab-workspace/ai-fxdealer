# AI FXDealer

Multi-tenant SaaS platform for Forex Brokers and Prop Trading Firms. Collects trading data from MT4, MT5, and cTrader, scores accounts with a rule engine, and surfaces results in a real-time dashboard.

**Stack:** FastAPI · Next.js 14 · PostgreSQL + TimescaleDB · Redis · Docker (via WSL2) · MT4/MT5 native on Windows

---

## Deployment Target: Google Cloud Windows Server 2022

This README is written as instructions for Claude Code to execute on a fresh Windows Server 2022 GCP VM. Claude Code runs locally on the server — not via RDP remote control.

Architecture on this server:
- Docker services (DB, Redis, API, Dashboard, cTrader collector) run inside WSL2 Ubuntu
- MT5 and MT4 collectors run natively on Windows (they require Windows DLLs)
- All services communicate over localhost — WSL2 automatically bridges ports to Windows

---

## MANUAL STEPS — Claude Code cannot do these

Complete all of these before starting Claude Code. Claude Code has no access to the GCP console, cannot see a screen, and cannot accept interactive GUI prompts.

### 1. Create the GCP VM

In the GCP Console:
- Machine type: `e2-standard-4` (4 vCPU, 16 GB RAM) — minimum for build performance
- OS: Windows Server 2022 Datacenter
- Boot disk: 80 GB SSD (Docker images + DB data need space)
- Allow HTTP and HTTPS traffic

### 2. Open firewall ports

GCP Console → VPC Network → Firewall → Create Rule:
- Name: `fxdealer-ports`
- Targets: All instances
- Source IP ranges: `0.0.0.0/0`
- Protocols and ports: TCP `3000, 8000`

Do NOT expose port 5432 (Postgres) or 6379 (Redis) publicly.

### 3. RDP into the server and install prerequisites

Connect via RDP. Open PowerShell as Administrator and run:

**Install Git for Windows:**
```powershell
winget install --id Git.Git -e --source winget --silent
```
If winget is not available, download Git from https://git-scm.com/download/win and install with defaults.

**Install Node.js (required for Claude Code):**
```powershell
winget install OpenJS.NodeJS.LTS --silent
```
Close and reopen PowerShell to reload PATH.

**Install Claude Code:**
```powershell
npm install -g @anthropic-ai/claude-code
```

**Authenticate Claude Code:**
```powershell
claude
```
Follow the browser authentication prompt.

### 4. Clone the repo

In PowerShell:
```powershell
cd C:\
git clone https://github.com/Sohrab-workspace/ai-fxdealer
cd ai-fxdealer
```

### 5. Start Claude Code inside the repo

```powershell
cd C:\ai-fxdealer
claude
```

Tell Claude Code: "My VM's external IP is X.X.X.X — follow the README deployment instructions."

From this point, Claude Code can take over.

---

## PART A — WSL2 Setup (Claude Code, Session 1)

NOTE FOR CLAUDE CODE: Run these commands in PowerShell as Administrator. After enabling WSL2, a reboot is required. Warn the user, then stop. They will restart Claude Code after rebooting to continue with Part B.

### Step A1 — Check if WSL2 is already installed

```powershell
wsl --status
```

If the output shows `Default Version: 2` and Ubuntu is listed, skip to Part B.

### Step A2 — Enable WSL2 Windows features

```powershell
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
```

### Step A3 — Download the WSL2 kernel update

```powershell
$url = "https://wslstorestorage.blob.core.windows.net/wslblob/wsl_update_x64.msi"
$out = "$env:TEMP\wsl_update_x64.msi"
Invoke-WebRequest -Uri $url -OutFile $out
Start-Process msiexec.exe -ArgumentList "/i $out /quiet /norestart" -Wait
```

### Step A4 — Set WSL2 as default

```powershell
wsl --set-default-version 2
```

---

## REBOOT REQUIRED

NOTE FOR CLAUDE CODE: At this point tell the user:

> "WSL2 features are enabled. A reboot is required before continuing.
> Please restart the server, RDP back in, open PowerShell, cd to C:\ai-fxdealer, and start Claude Code again.
> When you restart Claude Code tell me 'WSL2 reboot done' and I will continue with Part B."

Claude Code cannot survive a reboot. This is the only interruption in the setup.

---

## PART B — Ubuntu, Docker, and Full Stack (Claude Code, Session 2)

NOTE FOR CLAUDE CODE: The user has rebooted and restarted Claude Code. Continue from here.

### Step B1 — Install Ubuntu 22.04 in WSL2

```powershell
wsl --install -d Ubuntu-22.04
```

This downloads and installs Ubuntu. When it asks for a UNIX username and password, the user must enter these manually — Claude Code cannot type into interactive WSL prompts. Tell the user to set username `ubuntu` and any password they choose, then come back.

After Ubuntu is set up, verify:
```powershell
wsl -l -v
```
Expected output: Ubuntu-22.04 running, VERSION 2.

### Step B2 — Install Docker Engine inside WSL2

Run all commands below inside WSL2. To enter WSL2:
```powershell
wsl
```

Inside WSL2 bash:
```bash
sudo apt-get update -y
sudo apt-get install -y ca-certificates curl gnupg lsb-release
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
sudo chmod a+r /etc/apt/keyrings/docker.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] \
  https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" \
  | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update -y
sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
sudo service docker start
sudo usermod -aG docker $USER
```

Verify Docker works:
```bash
sudo docker run hello-world
```

### Step B3 — Clone the repo inside WSL2

Clone into the WSL2 filesystem (NOT /mnt/c — Docker performance is much better here):
```bash
cd ~
git clone https://github.com/Sohrab-workspace/ai-fxdealer
cd ai-fxdealer
```

### Step B4 — Generate a JWT secret

```bash
openssl rand -hex 32
```

Copy the output. Use it in the next step.

### Step B5 — Create the environment file

Replace `<VM_EXTERNAL_IP>` with the GCP VM's external IP address (provided by the user).
Replace `<JWT_SECRET>` with the value from Step B4.

```bash
cat > .env.local << 'ENVEOF'
FXDEALER_DB_URL=postgresql://fxdealer:fxdealer@db:5432/fxdealer
FXDEALER_REDIS_URL=redis://redis:6379/0
FXDEALER_JWT_SECRET=<JWT_SECRET>
FXDEALER_JWT_EXPIRY_SECONDS=86400
FXDEALER_LOG_LEVEL=INFO
NEXT_PUBLIC_API_URL=http://<VM_EXTERNAL_IP>:8000
ENVEOF
```

### Step B6 — Build and start the full stack

This builds all images and starts every service. First build takes 8–15 minutes.

```bash
sudo docker compose \
  --env-file .env.local \
  -f docker/docker-compose.yml \
  up -d --build
```

Service startup order (automatic):
1. TimescaleDB — waits until healthy
2. Redis — waits until healthy
3. Migrate — runs all Alembic migrations (40), then exits with code 0
4. API (FastAPI :8000) — starts after migrations complete
5. Dashboard (Next.js :3000) — starts after API
6. Collector-worker (ARQ, Linux collectors) — starts after DB + Redis

### Step B7 — Check all services are running

```bash
sudo docker compose -f docker/docker-compose.yml ps
```

Expected — all services `running`, migrate shows `exited (0)`:
```
NAME                      STATUS
fxdealer-db               running (healthy)
fxdealer-redis            running (healthy)
fxdealer-migrate          exited (0)
fxdealer-api              running
fxdealer-dashboard        running
fxdealer-collector-worker running
```

If any service is in `restarting` state:
```bash
sudo docker compose -f docker/docker-compose.yml logs <service-name> --tail 50
```

### Step B8 — Create the admin user

```bash
sudo docker compose -f docker/docker-compose.yml exec api \
  /app/.venv/bin/python /app/scripts/create_test_user.py
```

This creates:
- Broker: `test-broker`
- Email: `admin@test.com`
- Password: `admin123`
- Role: `admin`

### Step B9 — Verify the dashboard is accessible

From the WSL2 terminal, test the API:
```bash
curl http://localhost:8000/health
```
Expected: `{"status":"ok"}`

Test login:
```bash
curl -s -X POST http://localhost:8000/api/v1/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email":"admin@test.com","password":"admin123","broker_slug":"test-broker"}' \
  | python3 -m json.tool
```
Expected: JSON with `access_token` field.

Open in browser: `http://<VM_EXTERNAL_IP>:3000`

Login with:
- Email: `admin@test.com`
- Password: `admin123`
- Broker: `test-broker`

---

## PART C — MT5 Collector (Windows native, only if broker credentials available)

NOTE FOR CLAUDE CODE: This part requires the user to provide broker credentials. Claude Code cannot know the MT5 server address, login, or password. Ask the user for these before proceeding. If they don't have them yet, skip this part.

### Step C1 — Install Python for Windows

In PowerShell (not WSL2):
```powershell
winget install Python.Python.3.12 --silent
```
Close and reopen PowerShell to reload PATH. Verify:
```powershell
python --version
```

### Step C2 — Install uv package manager

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```
Close and reopen PowerShell.

### Step C3 — Install MT5 collector dependencies

From `C:\ai-fxdealer`:
```powershell
uv pip install --system MT5Manager sqlalchemy psycopg2-binary structlog python-dotenv
```

### Step C4 — Configure MT5 credentials

Add to `C:\ai-fxdealer\.env.local` (Windows version — uses localhost since WSL2 bridges the port):
```
FXDEALER_DB_URL=postgresql://fxdealer:fxdealer@localhost:5432/fxdealer
FXDEALER_MT5_SERVER=<broker-mt5-server-ip>:<port>
FXDEALER_MT5_LOGIN=<manager-login>
FXDEALER_MT5_PASSWORD=<manager-password>
```

NOTE FOR CLAUDE CODE: The values for MT5_SERVER, MT5_LOGIN, and MT5_PASSWORD must come from the user. These are provided by the broker. Do not guess or invent them.

### Step C5 — Verify MT5 connection

```powershell
cd C:\ai-fxdealer
python services\collector-mt5\test_connection.py
```

---

## PART D — MT4 Collector (Windows native, only if broker DLL and credentials available)

NOTE FOR CLAUDE CODE: MT4 requires a DLL file that the broker provides. The DLL must already be present in `C:\ai-fxdealer\dlls\<broker-name>\`. Ask the user if they have it before proceeding. The dlls/ directory is in .gitignore and is never committed to git.

### Step D1 — Verify DLL is present

```powershell
ls C:\ai-fxdealer\dlls\
```

There should be a subdirectory named after the broker containing `mtmanapi.dll` or similar. If it's missing, the user must obtain it from their broker's MT4 Server installation.

### Step D2 — Configure MT4 credentials

Add to `.env.local`:
```
FXDEALER_MT4_DLL_PATH=C:\ai-fxdealer\dlls\<broker-name>\mtmanapi.dll
FXDEALER_MT4_SERVER=<broker-mt4-server-ip>:<port>
FXDEALER_MT4_LOGIN=<manager-login>
FXDEALER_MT4_PASSWORD=<manager-password>
```

### Step D3 — Install MT4 collector dependencies

```powershell
uv pip install --system sqlalchemy psycopg2-binary structlog python-dotenv
```

### Step D4 — Test MT4 connection

```powershell
cd C:\ai-fxdealer
python services\collector-mt4\test_connection.py
```

---

## Updating After git pull

Inside WSL2:
```bash
cd ~/ai-fxdealer
git pull origin main
sudo docker compose --env-file .env.local -f docker/docker-compose.yml up -d --build
sudo docker compose -f docker/docker-compose.yml run --rm migrate
```

---

## Stopping and Restarting

```bash
# Inside WSL2

# Stop all services (data is preserved in volumes)
sudo docker compose -f docker/docker-compose.yml down

# Start again
sudo docker compose --env-file .env.local -f docker/docker-compose.yml up -d

# Full reset — deletes all data
sudo docker compose -f docker/docker-compose.yml down -v
```

Note: WSL2 does not start automatically on Windows reboot. After a server restart, open PowerShell and run:
```powershell
wsl
```
Then inside WSL2:
```bash
sudo service docker start
cd ~/ai-fxdealer
sudo docker compose --env-file .env.local -f docker/docker-compose.yml up -d
```

---

## Troubleshooting

**Dashboard cannot reach the API (blank screen or login fails)**

`NEXT_PUBLIC_API_URL` is baked into the dashboard image at build time. It must be the external IP your browser uses, not `localhost`. Rebuild the dashboard:
```bash
sudo docker compose --env-file .env.local -f docker/docker-compose.yml up -d --build dashboard
```

**`wsl --install` hangs or fails**

On some Windows Server configurations, WSL2 requires the store to be enabled or the package to be downloaded manually:
```powershell
wsl --install --no-distribution
wsl --install -d Ubuntu-22.04 --web-download
```

**Docker `permission denied` inside WSL2**

The group membership update requires a new shell session:
```bash
newgrp docker
# or prefix all docker commands with sudo
```

**migrate container exits with non-zero code**

```bash
sudo docker compose -f docker/docker-compose.yml logs migrate
```
Most common cause: the db container was not yet healthy when migrate started. Re-run:
```bash
sudo docker compose -f docker/docker-compose.yml run --rm migrate
```

**MT5 collector: `ImportError: No module named 'MT5Manager'`**

MT5Manager is a Windows-only `.whl`. It cannot be installed inside WSL2 (Linux). Run the collector from Windows PowerShell, not WSL2.

**Port 3000 or 8000 unreachable from browser**

1. Check the GCP firewall rule allows TCP 3000 and 8000 from `0.0.0.0/0`
2. Check the service is running: `sudo docker compose -f docker/docker-compose.yml ps`
3. Check Windows Defender Firewall allows inbound on those ports:
```powershell
netsh advfirewall firewall add rule name="FXDealer API" dir=in action=allow protocol=TCP localport=8000
netsh advfirewall firewall add rule name="FXDealer Dashboard" dir=in action=allow protocol=TCP localport=3000
```

**WSL2 ports not reachable from Windows browser**

WSL2 bridges ports automatically, but occasionally needs a reset:
```powershell
netsh winsock reset
```
Then restart WSL2:
```powershell
wsl --shutdown
wsl
```

---

## What Claude Code Cannot Do — Summary

| Task | Why |
|---|---|
| Connect via RDP | RDP is a graphical protocol — no screen visibility |
| Open GCP Console | No browser access to external web interfaces |
| Open GCP firewall rules | Requires GCP Console or gcloud CLI auth |
| Survive a server reboot | Process is killed on reboot — must be restarted |
| Provide MT5/MT4 broker credentials | These are secrets known only to you and your broker |
| Provide the MT4 Manager DLL | Provided by the broker, never committed to git |
| Type into interactive WSL2 username/password prompt | Interactive terminal prompts block non-interactive execution |
| Install Docker Desktop | Not supported on Windows Server |

---

## Architecture Overview

```
Windows Server 2022 (GCP VM)
│
├── WSL2 Ubuntu 22.04
│   └── Docker Engine
│       ├── fxdealer-db         (TimescaleDB :5432)
│       ├── fxdealer-redis      (Redis :6379)
│       ├── fxdealer-api        (FastAPI :8000)
│       ├── fxdealer-dashboard  (Next.js :3000)
│       └── fxdealer-collector-worker  (cTrader + bridge collectors)
│
├── Windows native (PowerShell)
│   ├── MT5 collector  (MT5Manager.dll — Windows only)
│   └── MT4 collector  (mtmanapi.dll from broker — Windows only)
│
└── Port bridge (automatic)
    WSL2 :5432 → Windows localhost:5432
    WSL2 :8000 → Windows localhost:8000
    WSL2 :3000 → Windows localhost:3000
```

Data flow:
```
MT5/MT4 collectors (Windows) ─┐
cTrader collector (Docker)   ─┤─→ raw_* tables → norm_* tables → re_account_scores
                               │
                               └─→ Dashboard (Users, Accounts, Positions, Deals, Risk Scores)
```

---

## Project Structure

```
services/api/              FastAPI service
services/rule-engine/      Rule engine (LARB, SFA, PGE scoring)
services/collector-mt5/    MT5 collector (Windows native)
services/collector-mt4/    MT4 collector (Windows native, needs broker DLL)
services/collector-ctrader/ cTrader collector (Docker/Linux)
dashboard/                 Next.js 14 App Router frontend
packages/db/               SQLAlchemy models + Alembic migrations (40 migrations)
packages/shared/           Shared Pydantic models, BaseCollector contract
packages/queue/            Redis Streams client + ARQ workers
docker/                    Dockerfiles + docker-compose.yml
scripts/                   create_test_user.py (seeds admin account)
dlls/                      Broker DLL files — gitignored, never committed
bases/                     Broker data files — gitignored, never committed
```

# AI FXDealer

Multi-tenant SaaS platform for Forex Brokers and Prop Trading Firms. Collects trading data from MT4, MT5, and cTrader, scores accounts with a rule engine, and surfaces results in a real-time dashboard.

**Stack:** FastAPI · Next.js · PostgreSQL + TimescaleDB · Redis · Docker

---

## For Claude Code: GCP VM Deployment

This section is written as step-by-step instructions for Claude Code to execute on a fresh GCP VM after the repo has been cloned.

---

## STOP — Things Claude Code CANNOT Do (Manual Steps Required First)

Before asking Claude Code to set anything up, the human must complete these steps manually. Claude Code has no access to the GCP console, no ability to accept interactive prompts, and no knowledge of your broker credentials.

**1. Create the GCP VM (GCP Console — manual)**

Recommended spec:
- Machine type: `e2-standard-4` (4 vCPU, 16 GB RAM) — build takes ~8 min on e2-standard-2
- OS: Ubuntu 22.04 LTS
- Boot disk: 50 GB SSD
- Region: closest to your broker's trading server

**2. Open firewall ports (GCP Console → VPC Network → Firewall — manual)**

Create a firewall rule allowing inbound TCP on:
- Port `3000` — Dashboard
- Port `8000` — API

Port 22 (SSH) is already open by default. Do NOT open 5432 (Postgres) or 6379 (Redis) publicly.

**3. SSH into the VM and install Claude Code (manual)**

```bash
# On your local machine
ssh ubuntu@<VM_EXTERNAL_IP>

# On the VM — install Node.js (required for Claude Code)
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
sudo apt-get install -y nodejs

# Install Claude Code
npm install -g @anthropic-ai/claude-code

# Authenticate
claude
```

**4. Clone the repo (manual or Claude Code)**

```bash
git clone https://github.com/Sohrab-workspace/ai-fxdealer
cd ai-fxdealer
```

**5. Tell Claude Code your VM's external IP**

When you start Claude Code in the repo directory, tell it:
> "My VM's external IP is X.X.X.X — follow the README deployment instructions."

Claude Code cannot discover your external IP on its own.

---

## What Claude Code CAN Do From Here

Once you are SSHed in, inside the `ai-fxdealer` directory, with Claude Code running, it can execute every step below automatically.

---

## Step-by-Step Deployment Instructions

### Step 1 — Install Docker

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
```

Verify:
```bash
sudo docker --version
sudo docker compose version
```

### Step 2 — Generate a JWT secret

```bash
openssl rand -hex 32
```

Copy the output — this is your `FXDEALER_JWT_SECRET`. Use it in the next step.

### Step 3 — Create the environment file

Create `.env.local` in the repo root. Replace `<VM_EXTERNAL_IP>` and `<JWT_SECRET>` with real values:

```bash
cat > .env.local << 'EOF'
FXDEALER_DB_URL=postgresql://fxdealer:fxdealer@db:5432/fxdealer
FXDEALER_REDIS_URL=redis://redis:6379/0
FXDEALER_JWT_SECRET=<JWT_SECRET>
FXDEALER_JWT_EXPIRY_SECONDS=86400
FXDEALER_LOG_LEVEL=INFO
NEXT_PUBLIC_API_URL=http://<VM_EXTERNAL_IP>:8000
EOF
```

### Step 4 — Build and start the full stack

This builds all Docker images and starts every service. The first build takes 5–10 minutes (downloads base images, installs Python/Node deps).

```bash
sudo docker compose \
  --env-file .env.local \
  -f docker/docker-compose.yml \
  up -d --build
```

Service startup order (automatic):
1. `db` (TimescaleDB) — waits for healthy
2. `redis` — waits for healthy
3. `migrate` — runs all 40 Alembic migrations, then exits
4. `api` (FastAPI :8000) — waits for migrate to complete
5. `dashboard` (Next.js :3000) — waits for api
6. `collector-worker` (ARQ Linux workers) — waits for db + redis

### Step 5 — Verify all services are running

```bash
sudo docker compose -f docker/docker-compose.yml ps
```

Expected output — all services should show `running` or `exited (0)` for migrate:

```
NAME                      STATUS
fxdealer-db               running (healthy)
fxdealer-redis            running (healthy)
fxdealer-migrate          exited (0)
fxdealer-api              running
fxdealer-dashboard        running
fxdealer-collector-worker running
```

If any service is in `restarting` state, check logs:
```bash
sudo docker compose -f docker/docker-compose.yml logs <service-name>
```

### Step 6 — Create the admin user

Run the seed script inside the API container:

```bash
sudo docker compose -f docker/docker-compose.yml exec api \
  /app/.venv/bin/python /app/scripts/create_test_user.py
```

This creates:
- Broker: `test-broker`
- Email: `admin@test.com`
- Password: `admin123`
- Role: `admin`

**Change this password immediately** if this is a real deployment.

### Step 7 — Open the dashboard

Navigate to: `http://<VM_EXTERNAL_IP>:3000`

Login credentials:
- Email: `admin@test.com`
- Password: `admin123`
- Broker: `test-broker`

API docs: `http://<VM_EXTERNAL_IP>:8000/api/docs`

---

## Troubleshooting

**Dashboard shows "Cannot connect to API"**
The `NEXT_PUBLIC_API_URL` is baked into the dashboard image at build time. If you used `localhost` instead of the VM's external IP, rebuild:
```bash
sudo docker compose --env-file .env.local -f docker/docker-compose.yml up -d --build dashboard
```

**migrate container exits with error**
Check migration logs:
```bash
sudo docker compose -f docker/docker-compose.yml logs migrate
```
Common cause: DB not ready. Re-run migrate only:
```bash
sudo docker compose -f docker/docker-compose.yml run --rm migrate
```

**API returns 401 on all requests**
The JWT secret in `.env.local` doesn't match what was used to issue tokens. Clear browser localStorage and log in again.

**Port 3000 / 8000 unreachable from browser**
GCP firewall rule is missing. Go to GCP Console → VPC Network → Firewall → add rule allowing TCP 3000 and 8000 from `0.0.0.0/0`.

**Disk full during build**
Docker build layers can use 10–15 GB. Check space:
```bash
df -h
sudo docker system prune -f  # remove unused layers
```

---

## Connecting Real Broker Data

The dashboard works immediately after setup but shows no trading data until collectors are connected.

### MT5 (Linux VM — works out of the box)

MT5Manager requires Windows. It **cannot run on a Linux GCP VM**. Options:
- Run the MT5 collector on a separate Windows VM
- Run it on a Windows machine with network access to the DB

### MT4 (Windows only)

The MT4 Manager API DLL is Windows-only. Same constraint as MT5.

### cTrader (Linux — works on this VM)

The cTrader collector runs on Linux. Configure credentials in `.env.local`:
```
FXDEALER_CTRADER_HOST=<broker-ctrader-server-ip>
FXDEALER_CTRADER_PORT=5392
FXDEALER_CTRADER_PLANT_ID=<plant-id>
FXDEALER_CTRADER_ENV_NAME=<env>
FXDEALER_CTRADER_LOGIN=<login>
FXDEALER_CTRADER_PASSWORD=<password>
```

Claude Code cannot fill in these values — they come from your broker.

---

## Updating the Running Stack

After pulling new code from git:

```bash
git pull origin main

# Rebuild changed services only
sudo docker compose --env-file .env.local -f docker/docker-compose.yml up -d --build

# Run any new migrations
sudo docker compose -f docker/docker-compose.yml run --rm migrate
```

---

## Stopping the Stack

```bash
# Stop all services (data is preserved in volumes)
sudo docker compose -f docker/docker-compose.yml down

# Stop and delete all data (full reset)
sudo docker compose -f docker/docker-compose.yml down -v
```

---

## Architecture Overview

```
Browser → :3000 (Next.js dashboard)
              ↓ API calls
           :8000 (FastAPI)
              ↓
     PostgreSQL + TimescaleDB (:5432)
     Redis (:6379)
              ↑
     Collector Worker (ARQ)
     [MT5/MT4 collectors run separately on Windows]
```

Data flow:
```
Collector → raw_mt5_* / raw_mt4_* / raw_ctrader_* tables
         → norm_accounts / norm_deals / norm_positions (normalizer)
         → re_account_scores (rule engine — LARB/SFA/PGE)
         → Dashboard (Users, Accounts, Risk Scores pages)
```

---

## Project Structure

```
services/api/          FastAPI service (routes, middleware, models)
services/rule-engine/  Rule engine (LARB, SFA, PGE)
services/collector-mt5/  MT5 collector (Windows only)
services/collector-mt4/  MT4 collector (Windows only)
services/collector-ctrader/  cTrader collector (Linux)
dashboard/             Next.js 14 App Router frontend
packages/db/           SQLAlchemy models + Alembic migrations (40 migrations)
packages/shared/       Shared Pydantic models, BaseCollector
packages/queue/        Redis Streams client + ARQ workers
docker/                Dockerfiles + docker-compose
scripts/               Seed scripts (create_test_user.py)
```

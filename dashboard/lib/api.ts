const API_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000"

let _token: string | null = null

export function setToken(t: string) { _token = t }
export function getToken() { return _token || (typeof window !== 'undefined' ? localStorage.getItem('fxdealer_token') : null) }
export function clearToken() { _token = null; if (typeof window !== 'undefined') localStorage.removeItem('fxdealer_token') }

async function apiFetch<T>(path: string, options: RequestInit = {}): Promise<T> {
  const token = getToken()
  const res = await fetch(`${API_URL}${path}`, {
    ...options,
    headers: {
      "Content-Type": "application/json",
      ...(token ? { Authorization: `Bearer ${token}` } : {}),
      ...options.headers,
    },
  })
  if (res.status === 401) {
    clearToken()
    if (typeof window !== 'undefined') window.location.href = '/login'
    throw new Error('Unauthorized')
  }
  if (!res.ok) {
    const body = await res.text()
    throw new Error(`API error ${res.status}: ${body}`)
  }
  return res.json()
}

// Auth
export async function login(email: string, password: string, brokerSlug: string) {
  const data = await apiFetch<{ access_token: string; broker_id: string; role: string }>('/api/v1/auth/login', {
    method: 'POST',
    body: JSON.stringify({ email, password, broker_slug: brokerSlug }),
  })
  setToken(data.access_token)
  if (typeof window !== 'undefined') localStorage.setItem('fxdealer_token', data.access_token)
  return data
}

// Overview
export async function getOverview() {
  return apiFetch<{
    total_accounts: number
    total_deals: number
    open_positions: number
    flagged_accounts: number
    abuse_candidates: number
    live_ticks_mt5: number
    live_ticks_mt4: number
    collectors_healthy: number
    collectors_total: number
  }>('/api/v1/overview/')
}

// Accounts
export async function getAccounts(params: {
  page?: number
  page_size?: number
  source_system?: string
  search?: string
  swap_free?: number
}) {
  const q = new URLSearchParams()
  if (params.page) q.set('page', String(params.page))
  if (params.page_size) q.set('page_size', String(params.page_size))
  if (params.source_system) q.set('source_system', params.source_system)
  if (params.search) q.set('search', params.search)
  if (params.swap_free !== undefined) q.set('swap_free', String(params.swap_free))
  return apiFetch<{
    total: number
    page: number
    page_size: number
    items: Account[]
  }>(`/api/v1/accounts/?${q}`)
}

// Deals
export async function getDeals(params: {
  page?: number
  page_size?: number
  source_system?: string
  login?: number
  symbol?: string
}) {
  const q = new URLSearchParams()
  if (params.page) q.set('page', String(params.page))
  if (params.page_size) q.set('page_size', String(params.page_size))
  if (params.source_system) q.set('source_system', params.source_system)
  if (params.login) q.set('login', String(params.login))
  if (params.symbol) q.set('symbol', params.symbol)
  return apiFetch<{
    total: number
    page: number
    page_size: number
    items: Deal[]
  }>(`/api/v1/deals/?${q}`)
}

// Positions
export async function getPositions(params: {
  page?: number
  page_size?: number
  source_system?: string
  login?: number
  symbol?: string
}) {
  const q = new URLSearchParams()
  if (params.page) q.set('page', String(params.page))
  if (params.page_size) q.set('page_size', String(params.page_size))
  if (params.source_system) q.set('source_system', params.source_system)
  if (params.login) q.set('login', String(params.login))
  if (params.symbol) q.set('symbol', params.symbol)
  return apiFetch<{
    total: number
    page: number
    page_size: number
    items: Position[]
  }>(`/api/v1/positions/?${q}`)
}

// Ticks
export async function getLatestTicks(source_system?: string) {
  const q = source_system ? `?source_system=${source_system}` : ''
  return apiFetch<{ items: Tick[] }>(`/api/v1/ticks/latest${q}`)
}

// Rules
export async function getRuleScoresSummary() {
  return apiFetch<{
    normal: number
    monitor: number
    suspicious: number
    abuse_candidate: number
    total_scored: number
  }>('/api/v1/rules/scores/summary')
}

export async function getRuleScores(params: {
  page?: number
  page_size?: number
  severity?: string
  min_score?: number
}) {
  const q = new URLSearchParams()
  if (params.page) q.set('page', String(params.page))
  if (params.page_size) q.set('page_size', String(params.page_size))
  if (params.severity) q.set('severity', params.severity)
  if (params.min_score) q.set('min_score', String(params.min_score))
  return apiFetch<{
    total: number
    page: number
    page_size: number
    items: RuleScore[]
  }>(`/api/v1/rules/scores?${q}`)
}

// Collectors
export async function getCollectorStatus() {
  return apiFetch<{ items: CollectorRun[] }>('/api/v1/collectors/status')
}

export async function getDbCounts() {
  return apiFetch<{
    raw_mt5_accounts: number
    raw_mt5_deals: number
    raw_mt4_accounts: number
    raw_mt4_deals: number
    raw_ctrader_accounts: number
    raw_ctrader_deals: number
    norm_accounts: number
    norm_deals: number
    norm_positions: number
    raw_mt5_ticks: number
    raw_mt4_ticks: number
  }>('/api/v1/collectors/db-counts')
}

// Raw Tables
export async function getRawTable(tableName: string, params: {
  page?: number
  page_size?: number
  search?: string
}) {
  const q = new URLSearchParams()
  if (params.page) q.set('page', String(params.page))
  if (params.page_size) q.set('page_size', String(params.page_size))
  if (params.search) q.set('search', params.search)
  return apiFetch<{
    table: string
    total: number
    page: number
    page_size: number
    columns: string[]
    items: Record<string, unknown>[]
  }>(`/api/v1/raw/${tableName}?${q}`)
}

// Types
export interface Account {
  id: string
  source_system: string
  source_account_id: string
  login: number | null
  account_name: string | null
  group_name: string | null
  balance: number | null
  equity: number | null
  credit: number | null
  leverage: number | null
  currency: string | null
  country: string | null
  swap_free: number | null
  is_demo: number | null
  account_status: string | null
  registration_ts: number | null
  last_access_ts: number | null
}

export interface Deal {
  id: string
  source_system: string
  source_deal_id: string
  source_account_id: string
  login: number | null
  symbol: string | null
  direction: number | null
  volume_lots: number | null
  price: number | null
  profit: number | null
  commission: number | null
  swap: number | null
  deal_time_msc: number
  duration_ms: number | null
  deal_type: string | null
  deal_time: string
}

export interface Position {
  id: string
  source_system: string
  source_position_id: string
  source_account_id: string
  login: number | null
  symbol: string | null
  direction: number | null
  volume_lots: number | null
  price_open: number | null
  price_current: number | null
  profit: number | null
  swap: number | null
  open_time_msc: number | null
}

export interface Tick {
  symbol: string
  bid: number | null
  ask: number | null
  source_system: string
  collected_at: string
}

export interface RuleScore {
  id: string
  source_account_id: string
  login: number | null
  total_score: number
  severity: string
  evaluated_at: string
  rule_engine_id: string
}

export interface CollectorRun {
  id: string
  source_system: string
  entity: string | null
  sync_mode: string
  status: string
  records_fetched: number | null
  records_saved: number | null
  duration_ms: number | null
  error_message: string | null
  collected_at: string
}

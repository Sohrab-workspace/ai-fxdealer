"use client"

import { useState } from "react"
import { useQuery } from "@tanstack/react-query"
import { getUserStats, getUserCharts, getUsers } from "@/lib/api"
import { StatCard } from "@/components/ui/StatCard"
import { fmtTs } from "@/lib/utils"
import { Search, Download } from "lucide-react"
import {
  PieChart, Pie, Cell, Tooltip, ResponsiveContainer,
  BarChart, Bar, XAxis, YAxis, CartesianGrid,
} from "recharts"

const RISK_COLORS: Record<string, string> = {
  abuse_candidate: "var(--risk-critical)",
  suspicious:      "var(--risk-high)",
  monitor:         "var(--risk-medium)",
  normal:          "var(--accent-green)",
  unscored:        "var(--text-secondary)",
}

const SYSTEM_COLORS: Record<string, string> = {
  mt5:     "var(--color-primary)",
  mt4:     "var(--accent-green)",
  ctrader: "#a855f7",
}

function riskLabel(r: string) {
  return {
    abuse_candidate: "Abuse",
    suspicious: "Suspicious",
    monitor: "Monitor",
    normal: "Normal",
    unscored: "Unscored",
  }[r] ?? r
}

function riskColor(r: string) {
  return RISK_COLORS[r] ?? "var(--text-secondary)"
}

function RiskBadge({ level }: { level: string }) {
  return (
    <span
      className="px-2 py-0.5 rounded text-xs font-medium capitalize"
      style={{ background: `${riskColor(level)}20`, color: riskColor(level) }}
    >
      {riskLabel(level)}
    </span>
  )
}

function SourceBadge({ sys }: { sys: string }) {
  const color = SYSTEM_COLORS[sys] ?? "var(--text-secondary)"
  return (
    <span
      className="px-1.5 py-0.5 rounded text-xs font-medium uppercase"
      style={{ background: `${color}20`, color }}
    >
      {sys}
    </span>
  )
}

const CHART_COLORS = ["var(--color-primary)", "var(--accent-green)", "#a855f7", "#f59e0b", "#ef4444"]

export default function UsersPage() {
  const [page, setPage] = useState(1)
  const [search, setSearch] = useState("")
  const [searchInput, setSearchInput] = useState("")
  const [sourceSystem, setSourceSystem] = useState("")
  const [riskFilter, setRiskFilter] = useState("")
  const PAGE_SIZE = 50

  const { data: stats } = useQuery({ queryKey: ["user-stats"], queryFn: getUserStats })
  const { data: charts } = useQuery({ queryKey: ["user-charts"], queryFn: getUserCharts })
  const { data, isLoading } = useQuery({
    queryKey: ["users", page, search, sourceSystem, riskFilter],
    queryFn: () => getUsers({
      page,
      page_size: PAGE_SIZE,
      search: search || undefined,
      source_system: sourceSystem || undefined,
      risk_level: riskFilter || undefined,
    }),
    placeholderData: prev => prev,
  })

  const totalPages = data ? Math.ceil(data.total / PAGE_SIZE) : 1

  const handleSearch = (e: React.FormEvent) => {
    e.preventDefault()
    setSearch(searchInput)
    setPage(1)
  }

  const exportCsv = () => {
    if (!data?.items.length) return
    const headers = ["Login", "Name", "System", "Country", "Currency", "Status", "Risk", "Last Access"]
    const rows = data.items.map(u => [
      u.login ?? "", u.account_name ?? "", u.source_system, u.country ?? "",
      u.currency ?? "", u.account_status ?? "", riskLabel(u.risk_level), fmtTs(u.last_access_ts),
    ])
    const csv = [headers, ...rows].map(r => r.join(",")).join("\n")
    const a = document.createElement("a")
    a.href = URL.createObjectURL(new Blob([csv], { type: "text/csv" }))
    a.download = "users.csv"
    a.click()
  }

  return (
    <div>
      {/* Header */}
      <div className="mb-6 flex items-start justify-between">
        <div>
          <h1 className="text-xl font-bold text-white">Users</h1>
          <p className="text-sm mt-1" style={{ color: "var(--text-secondary)" }}>
            Monitor and manage trader accounts
          </p>
        </div>
        <button
          onClick={exportCsv}
          className="flex items-center gap-2 px-3 py-2 rounded-lg text-sm font-medium"
          style={{ background: "#141414", border: "1px solid var(--color-border)", color: "white" }}
        >
          <Download size={14} />
          Export
        </button>
      </div>

      {/* Stat cards */}
      <div className="grid grid-cols-2 lg:grid-cols-4 gap-4 mb-6">
        <StatCard
          label="Total Users"
          value={stats?.total ?? "—"}
          sub={stats ? `${stats.live.toLocaleString()} live · ${stats.demo.toLocaleString()} demo` : undefined}
        />
        <StatCard
          label="Live Accounts"
          value={stats?.live ?? "—"}
          color="var(--accent-green)"
        />
        <StatCard
          label="Demo Accounts"
          value={stats?.demo ?? "—"}
          color="var(--color-primary)"
        />
        <StatCard
          label="High Risk"
          value={stats?.high_risk ?? "—"}
          color="var(--risk-critical)"
          sub="abuse + suspicious"
        />
      </div>

      {/* Charts */}
      {charts && (
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-4 mb-6">
          {/* Source distribution */}
          <div className="rounded-xl p-5" style={{ border: "1px solid var(--color-border)", background: "#0a0a0a" }}>
            <h2 className="text-sm font-semibold text-white mb-4">Accounts by Platform</h2>
            <ResponsiveContainer width="100%" height={180}>
              <PieChart>
                <Pie
                  data={charts.status_dist}
                  dataKey="count"
                  nameKey="label"
                  cx="50%"
                  cy="50%"
                  innerRadius={45}
                  outerRadius={75}
                  paddingAngle={3}
                >
                  {charts.status_dist.map((entry, i) => (
                    <Cell key={entry.label} fill={SYSTEM_COLORS[entry.label] ?? CHART_COLORS[i % CHART_COLORS.length]} />
                  ))}
                </Pie>
                <Tooltip
                  contentStyle={{ background: "#111", border: "1px solid #1a1a1a", borderRadius: 8, fontSize: 12 }}
                  itemStyle={{ color: "white" }}
                  formatter={(v: number) => v.toLocaleString()}
                />
              </PieChart>
            </ResponsiveContainer>
            <div className="flex flex-wrap gap-3 mt-2 justify-center">
              {charts.status_dist.map((d, i) => (
                <div key={d.label} className="flex items-center gap-1.5">
                  <div className="w-2 h-2 rounded-full" style={{ background: SYSTEM_COLORS[d.label] ?? CHART_COLORS[i % CHART_COLORS.length] }} />
                  <span className="text-xs uppercase" style={{ color: "var(--text-secondary)" }}>{d.label} ({d.count.toLocaleString()})</span>
                </div>
              ))}
            </div>
          </div>

          {/* Risk distribution */}
          <div className="rounded-xl p-5" style={{ border: "1px solid var(--color-border)", background: "#0a0a0a" }}>
            <h2 className="text-sm font-semibold text-white mb-4">Risk Level Distribution</h2>
            <ResponsiveContainer width="100%" height={180}>
              <BarChart data={charts.risk_dist} layout="vertical" margin={{ left: 16, right: 16 }}>
                <CartesianGrid horizontal={false} stroke="#1a1a1a" />
                <XAxis type="number" tick={{ fill: "var(--text-secondary)", fontSize: 11 }} axisLine={false} tickLine={false} tickFormatter={v => v.toLocaleString()} />
                <YAxis type="category" dataKey="label" tick={{ fill: "var(--text-secondary)", fontSize: 11 }} axisLine={false} tickLine={false}
                  tickFormatter={l => riskLabel(l)} width={72} />
                <Tooltip
                  contentStyle={{ background: "#111", border: "1px solid #1a1a1a", borderRadius: 8, fontSize: 12 }}
                  itemStyle={{ color: "white" }}
                  formatter={(v: number) => v.toLocaleString()}
                />
                <Bar dataKey="count" radius={[0, 4, 4, 0]}>
                  {charts.risk_dist.map(entry => (
                    <Cell key={entry.label} fill={riskColor(entry.label)} />
                  ))}
                </Bar>
              </BarChart>
            </ResponsiveContainer>
          </div>
        </div>
      )}

      {/* Filters */}
      <div className="flex flex-wrap gap-3 mb-4">
        <form onSubmit={handleSearch} className="flex gap-2">
          <div className="relative">
            <Search size={14} className="absolute left-3 top-1/2 -translate-y-1/2" style={{ color: "var(--text-secondary)" }} />
            <input
              type="text"
              placeholder="Search login, name..."
              value={searchInput}
              onChange={e => setSearchInput(e.target.value)}
              className="pl-8 pr-3 py-2 rounded-lg text-sm text-white outline-none"
              style={{ background: "#0f0f0f", border: "1px solid var(--color-border)", minWidth: 200 }}
            />
          </div>
          <button type="submit" className="px-3 py-2 rounded-lg text-sm font-medium text-white"
            style={{ background: "var(--color-primary)" }}>Search</button>
          {search && (
            <button type="button" onClick={() => { setSearch(""); setSearchInput(""); setPage(1) }}
              className="px-3 py-2 rounded-lg text-sm"
              style={{ background: "#141414", border: "1px solid var(--color-border)", color: "var(--text-secondary)" }}>Clear</button>
          )}
        </form>

        <select value={sourceSystem} onChange={e => { setSourceSystem(e.target.value); setPage(1) }}
          className="px-3 py-2 rounded-lg text-sm text-white outline-none"
          style={{ background: "#0f0f0f", border: "1px solid var(--color-border)" }}>
          <option value="">All Platforms</option>
          <option value="mt5">MT5</option>
          <option value="mt4">MT4</option>
          <option value="ctrader">cTrader</option>
        </select>

        <select value={riskFilter} onChange={e => { setRiskFilter(e.target.value); setPage(1) }}
          className="px-3 py-2 rounded-lg text-sm text-white outline-none"
          style={{ background: "#0f0f0f", border: "1px solid var(--color-border)" }}>
          <option value="">All Risk Levels</option>
          <option value="abuse_candidate">Abuse</option>
          <option value="suspicious">Suspicious</option>
          <option value="monitor">Monitor</option>
          <option value="normal">Normal</option>
          <option value="unscored">Unscored</option>
        </select>
      </div>

      {/* Table */}
      <div className="rounded-xl overflow-hidden" style={{ border: "1px solid var(--color-border)" }}>
        <table className="w-full text-xs">
          <thead>
            <tr style={{ background: "#0d0d0d", borderBottom: "1px solid var(--color-border)" }}>
              {["Login", "Name", "Platform", "Country", "Currency", "Demo", "Risk Level", "Last Access"].map(h => (
                <th key={h} className="px-4 py-3 text-left font-medium uppercase tracking-wide"
                  style={{ color: "var(--text-secondary)", whiteSpace: "nowrap" }}>{h}</th>
              ))}
            </tr>
          </thead>
          <tbody>
            {isLoading
              ? Array.from({ length: 12 }).map((_, i) => (
                <tr key={i} style={{ borderBottom: "1px solid #0d0d0d" }}>
                  {Array.from({ length: 8 }).map((_, j) => (
                    <td key={j} className="px-4 py-3">
                      <div className="h-3.5 rounded" style={{ background: "#141414", width: `${40 + (j * 9) % 45}%` }} />
                    </td>
                  ))}
                </tr>
              ))
              : data?.items.map(u => (
                <tr key={u.id} style={{ borderBottom: "1px solid #0d0d0d" }}
                  className="hover:bg-[#0d0d0d] cursor-pointer transition-colors">
                  <td className="px-4 py-3 font-mono font-medium text-white">{u.login ?? "—"}</td>
                  <td className="px-4 py-3 text-white" style={{ maxWidth: 160, overflow: "hidden", textOverflow: "ellipsis", whiteSpace: "nowrap" }}>
                    {u.account_name || "—"}
                  </td>
                  <td className="px-4 py-3"><SourceBadge sys={u.source_system} /></td>
                  <td className="px-4 py-3" style={{ color: "var(--text-secondary)" }}>{u.country || "—"}</td>
                  <td className="px-4 py-3 font-mono" style={{ color: "var(--text-secondary)" }}>{u.currency || "—"}</td>
                  <td className="px-4 py-3">
                    {u.is_demo === 1
                      ? <span className="px-1.5 py-0.5 rounded text-xs font-medium" style={{ background: "rgba(45,97,255,0.15)", color: "var(--color-primary)" }}>Demo</span>
                      : <span className="px-1.5 py-0.5 rounded text-xs font-medium" style={{ background: "rgba(59,164,104,0.15)", color: "var(--accent-green)" }}>Live</span>
                    }
                  </td>
                  <td className="px-4 py-3"><RiskBadge level={u.risk_level} /></td>
                  <td className="px-4 py-3 font-mono" style={{ color: "var(--text-secondary)", whiteSpace: "nowrap" }}>
                    {fmtTs(u.last_access_ts)}
                  </td>
                </tr>
              ))
            }
          </tbody>
        </table>

        {!isLoading && !data?.items.length && (
          <div className="py-12 text-center">
            <p className="text-sm" style={{ color: "var(--text-secondary)" }}>No users found</p>
          </div>
        )}
      </div>

      {/* Pagination */}
      {data && totalPages > 1 && (
        <div className="flex items-center justify-between mt-4">
          <p className="text-xs" style={{ color: "var(--text-secondary)" }}>
            Page {page} of {totalPages} ({data.total.toLocaleString()} total)
          </p>
          <div className="flex gap-2">
            <button onClick={() => setPage(p => Math.max(1, p - 1))} disabled={page === 1}
              className="px-3 py-1.5 rounded-lg text-xs font-medium disabled:opacity-40"
              style={{ background: "#141414", border: "1px solid var(--color-border)", color: "white" }}>Prev</button>
            <button onClick={() => setPage(p => Math.min(totalPages, p + 1))} disabled={page === totalPages}
              className="px-3 py-1.5 rounded-lg text-xs font-medium disabled:opacity-40"
              style={{ background: "#141414", border: "1px solid var(--color-border)", color: "white" }}>Next</button>
          </div>
        </div>
      )}
    </div>
  )
}

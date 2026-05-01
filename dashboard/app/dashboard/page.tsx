"use client"

import { useQuery } from "@tanstack/react-query"
import { getOverview, getRuleScoresSummary, getCollectorStatus, getLatestTicks } from "@/lib/api"
import { StatCard } from "@/components/ui/StatCard"
import { fmtTs } from "@/lib/utils"

export default function DashboardPage() {
  const { data: overview } = useQuery({ queryKey: ["overview"], queryFn: getOverview, refetchInterval: 30_000 })
  const { data: scores } = useQuery({ queryKey: ["scores-summary"], queryFn: getRuleScoresSummary, refetchInterval: 60_000 })
  const { data: collectors } = useQuery({ queryKey: ["collector-status"], queryFn: getCollectorStatus, refetchInterval: 30_000 })
  const { data: ticks } = useQuery({ queryKey: ["ticks", "mt5"], queryFn: () => getLatestTicks("mt5"), refetchInterval: 5_000 })

  return (
    <div>
      <div className="mb-6">
        <h1 className="text-xl font-bold text-white">Overview</h1>
        <p className="text-sm mt-1" style={{ color: "var(--text-secondary)" }}>
          Platform-wide summary — refreshes every 30s
        </p>
      </div>

      {/* Main stats */}
      <div className="grid grid-cols-2 lg:grid-cols-4 gap-4 mb-6">
        <StatCard label="Total Accounts" value={overview?.total_accounts ?? "—"} />
        <StatCard label="Total Deals" value={overview?.total_deals ?? "—"} />
        <StatCard label="Open Positions" value={overview?.open_positions ?? "—"} />
        <StatCard
          label="Flagged Accounts"
          value={overview?.flagged_accounts ?? "—"}
          color={overview?.flagged_accounts ? "var(--risk-medium)" : undefined}
        />
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-4 mb-6">
        {/* Rule engine summary */}
        <div className="rounded-xl p-5 col-span-1" style={{ border: "1px solid var(--color-border)", background: "#0a0a0a" }}>
          <h2 className="text-sm font-semibold text-white mb-4">Risk Scores</h2>
          {scores ? (
            <div className="space-y-3">
              {[
                { label: "Abuse Candidates", key: "abuse_candidate" as const, color: "var(--risk-critical)" },
                { label: "Suspicious", key: "suspicious" as const, color: "var(--risk-high)" },
                { label: "Monitor", key: "monitor" as const, color: "var(--risk-medium)" },
                { label: "Normal", key: "normal" as const, color: "var(--risk-low)" },
              ].map(row => (
                <div key={row.key} className="flex items-center justify-between">
                  <div className="flex items-center gap-2">
                    <div className="w-2 h-2 rounded-full" style={{ background: row.color }} />
                    <span className="text-sm" style={{ color: "var(--text-secondary)" }}>{row.label}</span>
                  </div>
                  <span className="text-sm font-mono font-medium text-white">{scores[row.key].toLocaleString()}</span>
                </div>
              ))}
              <div className="pt-2" style={{ borderTop: "1px solid var(--color-border)" }}>
                <div className="flex justify-between text-sm">
                  <span style={{ color: "var(--text-secondary)" }}>Total scored</span>
                  <span className="font-mono font-medium text-white">{scores.total_scored.toLocaleString()}</span>
                </div>
              </div>
            </div>
          ) : (
            <div className="space-y-2">
              {[1,2,3,4].map(i => <div key={i} className="h-5 rounded" style={{ background: "#141414" }} />)}
            </div>
          )}
        </div>

        {/* Collector status */}
        <div className="rounded-xl p-5 col-span-1" style={{ border: "1px solid var(--color-border)", background: "#0a0a0a" }}>
          <h2 className="text-sm font-semibold text-white mb-4">Collectors</h2>
          {collectors?.items.length ? (
            <div className="space-y-3">
              {collectors.items.map(c => (
                <div key={c.id} className="flex items-center justify-between">
                  <div className="flex items-center gap-2">
                    <div
                      className="w-2 h-2 rounded-full"
                      style={{ background: c.status === "success" ? "var(--accent-green)" : "var(--risk-critical)" }}
                    />
                    <span className="text-sm font-medium text-white">{c.source_system.toUpperCase()}</span>
                  </div>
                  <div className="text-right">
                    <p className="text-xs font-mono" style={{ color: "var(--text-secondary)" }}>
                      {(c.records_saved ?? 0).toLocaleString()} records
                    </p>
                    <p className="text-xs" style={{ color: "var(--text-secondary)" }}>
                      {c.duration_ms ? `${(c.duration_ms / 1000).toFixed(1)}s` : "—"}
                    </p>
                  </div>
                </div>
              ))}
            </div>
          ) : (
            <p className="text-sm" style={{ color: "var(--text-secondary)" }}>No collector runs found</p>
          )}
        </div>

        {/* Live ticks */}
        <div className="rounded-xl p-5 col-span-1" style={{ border: "1px solid var(--color-border)", background: "#0a0a0a" }}>
          <h2 className="text-sm font-semibold text-white mb-4">Live Prices (MT5)</h2>
          <div className="space-y-1.5 overflow-auto" style={{ maxHeight: 200 }}>
            {ticks?.items.slice(0, 20).map(t => (
              <div key={t.symbol} className="flex items-center justify-between text-xs">
                <span className="font-mono font-medium" style={{ color: "var(--text-secondary)", width: 80 }}>{t.symbol}</span>
                <span className="font-mono text-white">{t.bid?.toFixed(5) ?? "—"}</span>
                <span className="font-mono" style={{ color: "var(--text-secondary)" }}>{t.ask?.toFixed(5) ?? "—"}</span>
              </div>
            ))}
            {!ticks?.items.length && (
              <p className="text-sm" style={{ color: "var(--text-secondary)" }}>No tick data</p>
            )}
          </div>
        </div>
      </div>

      {/* Latest deals */}
      <LatestDealsSection />
    </div>
  )
}

function LatestDealsSection() {
  const { data } = useQuery({
    queryKey: ["deals-recent"],
    queryFn: () => import("@/lib/api").then(m => m.getDeals({ page_size: 10 })),
    refetchInterval: 30_000,
  })

  return (
    <div className="rounded-xl p-5" style={{ border: "1px solid var(--color-border)", background: "#0a0a0a" }}>
      <h2 className="text-sm font-semibold text-white mb-4">Recent Deals</h2>
      <div className="overflow-x-auto">
        <table className="w-full text-xs">
          <thead>
            <tr style={{ borderBottom: "1px solid var(--color-border)" }}>
              {["Login", "Symbol", "Direction", "Volume", "Price", "Profit", "Time"].map(h => (
                <th key={h} className="pb-2 text-left font-medium uppercase tracking-wide pr-4"
                  style={{ color: "var(--text-secondary)" }}>{h}</th>
              ))}
            </tr>
          </thead>
          <tbody>
            {data?.items.map(d => (
              <tr key={d.id} style={{ borderBottom: "1px solid #0f0f0f" }}>
                <td className="py-2 pr-4 font-mono text-white">{d.login ?? "—"}</td>
                <td className="py-2 pr-4 font-mono font-medium text-white">{d.symbol || "—"}</td>
                <td className="py-2 pr-4">
                  <span className="px-1.5 py-0.5 rounded text-xs font-medium"
                    style={{
                      background: d.direction === 0 ? "rgba(59,164,104,0.15)" : "rgba(239,68,68,0.15)",
                      color: d.direction === 0 ? "var(--accent-green)" : "var(--risk-critical)",
                    }}>
                    {d.direction === 0 ? "BUY" : d.direction === 1 ? "SELL" : "—"}
                  </span>
                </td>
                <td className="py-2 pr-4 font-mono" style={{ color: "var(--text-secondary)" }}>
                  {d.volume_lots?.toFixed(2) ?? "—"}
                </td>
                <td className="py-2 pr-4 font-mono" style={{ color: "var(--text-secondary)" }}>
                  {d.price?.toFixed(5) ?? "—"}
                </td>
                <td className="py-2 pr-4 font-mono"
                  style={{ color: (d.profit ?? 0) >= 0 ? "var(--accent-green)" : "var(--risk-critical)" }}>
                  {d.profit != null ? (d.profit >= 0 ? "+" : "") + d.profit.toFixed(2) : "—"}
                </td>
                <td className="py-2 pr-4 font-mono" style={{ color: "var(--text-secondary)" }}>
                  {d.deal_time.slice(0, 19)}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
        {!data?.items.length && (
          <p className="text-sm py-4 text-center" style={{ color: "var(--text-secondary)" }}>No deals found</p>
        )}
      </div>
    </div>
  )
}

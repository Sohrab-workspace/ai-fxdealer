"use client"

import { useQuery } from "@tanstack/react-query"
import { getCollectorStatus, getDbCounts } from "@/lib/api"

export default function CollectorsPage() {
  const { data: status } = useQuery({ queryKey: ["collector-status"], queryFn: getCollectorStatus, refetchInterval: 15_000 })
  const { data: counts } = useQuery({ queryKey: ["db-counts"], queryFn: getDbCounts, refetchInterval: 30_000 })

  return (
    <div>
      <div className="mb-6">
        <h1 className="text-xl font-bold text-white">Collectors</h1>
        <p className="text-sm mt-1" style={{ color: "var(--text-secondary)" }}>
          Data collection status and raw DB counts
        </p>
      </div>

      {/* Collector runs */}
      <div className="rounded-xl p-5 mb-6" style={{ border: "1px solid var(--color-border)", background: "#0a0a0a" }}>
        <h2 className="text-sm font-semibold text-white mb-4">Latest Collector Runs</h2>
        <div className="space-y-4">
          {status?.items.map(c => (
            <div key={c.id} className="flex items-start justify-between">
              <div className="flex items-center gap-3">
                <div
                  className="w-2.5 h-2.5 rounded-full flex-shrink-0 mt-0.5"
                  style={{ background: c.status === "success" ? "var(--accent-green)" : "var(--risk-critical)" }}
                />
                <div>
                  <p className="text-sm font-medium text-white">{c.source_system.toUpperCase()}</p>
                  <p className="text-xs mt-0.5" style={{ color: "var(--text-secondary)" }}>
                    {c.sync_mode} • {c.status}
                  </p>
                  {c.error_message && (
                    <p className="text-xs mt-1 font-mono" style={{ color: "var(--risk-critical)" }}>
                      {c.error_message.slice(0, 100)}
                    </p>
                  )}
                </div>
              </div>
              <div className="text-right">
                <p className="text-sm font-mono text-white">
                  {(c.records_saved ?? 0).toLocaleString()} saved
                </p>
                <p className="text-xs font-mono" style={{ color: "var(--text-secondary)" }}>
                  {c.duration_ms ? `${(c.duration_ms / 1000).toFixed(1)}s` : "—"}
                </p>
                <p className="text-xs font-mono" style={{ color: "var(--text-secondary)" }}>
                  {c.collected_at.slice(0, 19)}
                </p>
              </div>
            </div>
          ))}
          {!status?.items.length && (
            <p className="text-sm" style={{ color: "var(--text-secondary)" }}>No collector runs found</p>
          )}
        </div>
      </div>

      {/* DB Counts */}
      {counts && (
        <div className="rounded-xl p-5" style={{ border: "1px solid var(--color-border)", background: "#0a0a0a" }}>
          <h2 className="text-sm font-semibold text-white mb-4">Raw DB Counts</h2>
          <div className="grid grid-cols-2 lg:grid-cols-3 gap-4">
            {[
              { label: "MT5 Accounts (raw)", value: counts.raw_mt5_accounts },
              { label: "MT5 Deals (raw)", value: counts.raw_mt5_deals },
              { label: "MT5 Ticks", value: counts.raw_mt5_ticks },
              { label: "MT4 Accounts (raw)", value: counts.raw_mt4_accounts },
              { label: "MT4 Deals (raw)", value: counts.raw_mt4_deals },
              { label: "MT4 Ticks", value: counts.raw_mt4_ticks },
              { label: "cTrader Accounts", value: counts.raw_ctrader_accounts },
              { label: "cTrader Deals", value: counts.raw_ctrader_deals },
              { label: "Norm Accounts", value: counts.norm_accounts },
              { label: "Norm Deals", value: counts.norm_deals },
              { label: "Norm Positions", value: counts.norm_positions },
            ].map(row => (
              <div key={row.label} className="p-3 rounded-lg" style={{ background: "#111", border: "1px solid #1a1a1a" }}>
                <p className="text-xs" style={{ color: "var(--text-secondary)" }}>{row.label}</p>
                <p className="text-lg font-mono font-bold text-white mt-1">{row.value.toLocaleString()}</p>
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  )
}

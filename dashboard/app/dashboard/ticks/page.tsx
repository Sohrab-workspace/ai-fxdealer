"use client"

import { useState } from "react"
import { useQuery } from "@tanstack/react-query"
import { getLatestTicks } from "@/lib/api"

export default function TicksPage() {
  const [sourceSystem, setSourceSystem] = useState("mt5")
  const [search, setSearch] = useState("")

  const { data, isLoading } = useQuery({
    queryKey: ["ticks", sourceSystem],
    queryFn: () => getLatestTicks(sourceSystem || undefined),
    refetchInterval: 3_000,
  })

  const filtered = data?.items.filter(t =>
    !search || t.symbol.toLowerCase().includes(search.toLowerCase())
  )

  const spread = (t: { bid: number | null; ask: number | null }) => {
    if (t.bid == null || t.ask == null) return null
    return ((t.ask - t.bid) * 100000).toFixed(1)
  }

  return (
    <div>
      <div className="mb-6 flex items-start justify-between">
        <div>
          <h1 className="text-xl font-bold text-white">Price Feed</h1>
          <p className="text-sm mt-1" style={{ color: "var(--text-secondary)" }}>
            {filtered?.length ?? "—"} symbols — refreshes every 3s
          </p>
        </div>
        <div className="flex items-center gap-2">
          <div className="w-2 h-2 rounded-full" style={{ background: "var(--accent-green)", boxShadow: "0 0 6px var(--accent-green)" }} />
          <span className="text-xs" style={{ color: "var(--accent-green)" }}>LIVE</span>
        </div>
      </div>

      <div className="flex gap-3 mb-4">
        <input
          type="text"
          placeholder="Filter symbol..."
          value={search}
          onChange={e => setSearch(e.target.value)}
          className="px-3 py-2 rounded-lg text-sm text-white outline-none max-w-xs"
          style={{ background: "#0f0f0f", border: "1px solid var(--color-border)" }}
        />
        <select
          value={sourceSystem}
          onChange={e => setSourceSystem(e.target.value)}
          className="px-3 py-2 rounded-lg text-sm text-white outline-none"
          style={{ background: "#0f0f0f", border: "1px solid var(--color-border)" }}
        >
          <option value="mt5">MT5</option>
          <option value="mt4">MT4</option>
          <option value="">All</option>
        </select>
      </div>

      <div className="rounded-xl overflow-hidden" style={{ border: "1px solid var(--color-border)" }}>
        <table className="w-full text-xs">
          <thead>
            <tr style={{ background: "#0d0d0d", borderBottom: "1px solid var(--color-border)" }}>
              {["Symbol", "Bid", "Ask", "Spread (pips)", "Source", "Updated"].map(h => (
                <th key={h} className="px-4 py-3 text-left font-medium uppercase tracking-wide"
                  style={{ color: "var(--text-secondary)" }}>{h}</th>
              ))}
            </tr>
          </thead>
          <tbody>
            {isLoading
              ? Array.from({ length: 15 }).map((_, i) => (
                <tr key={i} style={{ borderBottom: "1px solid #0d0d0d" }}>
                  {Array.from({ length: 6 }).map((_, j) => (
                    <td key={j} className="px-4 py-3">
                      <div className="h-3.5 rounded" style={{ background: "#141414", width: "70%" }} />
                    </td>
                  ))}
                </tr>
              ))
              : filtered?.map(t => (
                <tr key={`${t.source_system}-${t.symbol}`} style={{ borderBottom: "1px solid #0d0d0d" }}
                  className="hover:bg-[#0d0d0d] transition-colors">
                  <td className="px-4 py-3 font-mono font-medium text-white">{t.symbol}</td>
                  <td className="px-4 py-3 font-mono" style={{ color: "var(--accent-green)" }}>
                    {t.bid?.toFixed(5) ?? "—"}
                  </td>
                  <td className="px-4 py-3 font-mono" style={{ color: "var(--risk-critical)" }}>
                    {t.ask?.toFixed(5) ?? "—"}
                  </td>
                  <td className="px-4 py-3 font-mono" style={{ color: "var(--text-secondary)" }}>
                    {spread(t) ?? "—"}
                  </td>
                  <td className="px-4 py-3">
                    <span className="px-1.5 py-0.5 rounded text-xs font-medium uppercase"
                      style={{
                        background: t.source_system === "mt5" ? "rgba(45,97,255,0.15)" : "rgba(59,164,104,0.15)",
                        color: t.source_system === "mt5" ? "var(--color-primary)" : "var(--accent-green)",
                      }}>
                      {t.source_system}
                    </span>
                  </td>
                  <td className="px-4 py-3 font-mono" style={{ color: "var(--text-secondary)" }}>
                    {t.collected_at.slice(0, 19)}
                  </td>
                </tr>
              ))
            }
          </tbody>
        </table>

        {!isLoading && !filtered?.length && (
          <div className="py-12 text-center">
            <p className="text-sm" style={{ color: "var(--text-secondary)" }}>No tick data available</p>
          </div>
        )}
      </div>
    </div>
  )
}

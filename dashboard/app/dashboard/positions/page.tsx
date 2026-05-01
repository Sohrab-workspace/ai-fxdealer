"use client"

import { useState } from "react"
import { useQuery } from "@tanstack/react-query"
import { getPositions } from "@/lib/api"
import { fmtTs } from "@/lib/utils"

export default function PositionsPage() {
  const [page, setPage] = useState(1)
  const PAGE_SIZE = 50

  const { data, isLoading } = useQuery({
    queryKey: ["positions", page],
    queryFn: () => getPositions({ page, page_size: PAGE_SIZE }),
    placeholderData: prev => prev,
  })

  const totalPages = data ? Math.ceil(data.total / PAGE_SIZE) : 1

  return (
    <div>
      <div className="mb-6">
        <h1 className="text-xl font-bold text-white">Open Positions</h1>
        <p className="text-sm mt-1" style={{ color: "var(--text-secondary)" }}>
          {data?.total.toLocaleString() ?? "—"} open positions
        </p>
      </div>

      <div className="rounded-xl overflow-hidden" style={{ border: "1px solid var(--color-border)" }}>
        <table className="w-full text-xs">
          <thead>
            <tr style={{ background: "#0d0d0d", borderBottom: "1px solid var(--color-border)" }}>
              {["Login", "Symbol", "Side", "Volume", "Open Price", "Current Price", "Profit", "Swap", "Opened"].map(h => (
                <th key={h} className="px-4 py-3 text-left font-medium uppercase tracking-wide"
                  style={{ color: "var(--text-secondary)" }}>{h}</th>
              ))}
            </tr>
          </thead>
          <tbody>
            {isLoading
              ? Array.from({ length: 10 }).map((_, i) => (
                <tr key={i} style={{ borderBottom: "1px solid #0d0d0d" }}>
                  {Array.from({ length: 9 }).map((_, j) => (
                    <td key={j} className="px-4 py-3">
                      <div className="h-3.5 rounded" style={{ background: "#141414", width: "70%" }} />
                    </td>
                  ))}
                </tr>
              ))
              : data?.items.map(p => (
                <tr key={p.id} style={{ borderBottom: "1px solid #0d0d0d" }}
                  className="hover:bg-[#0d0d0d] transition-colors">
                  <td className="px-4 py-3 font-mono font-medium text-white">{p.login ?? "—"}</td>
                  <td className="px-4 py-3 font-mono font-medium text-white">{p.symbol || "—"}</td>
                  <td className="px-4 py-3">
                    <span className="px-1.5 py-0.5 rounded text-xs font-medium"
                      style={{
                        background: p.direction === 0 ? "rgba(59,164,104,0.15)" : "rgba(239,68,68,0.15)",
                        color: p.direction === 0 ? "var(--accent-green)" : "var(--risk-critical)",
                      }}>
                      {p.direction === 0 ? "BUY" : p.direction === 1 ? "SELL" : "—"}
                    </span>
                  </td>
                  <td className="px-4 py-3 font-mono" style={{ color: "var(--text-secondary)" }}>
                    {p.volume_lots?.toFixed(2) ?? "—"}
                  </td>
                  <td className="px-4 py-3 font-mono" style={{ color: "var(--text-secondary)" }}>
                    {p.price_open?.toFixed(5) ?? "—"}
                  </td>
                  <td className="px-4 py-3 font-mono" style={{ color: "var(--text-secondary)" }}>
                    {p.price_current?.toFixed(5) ?? "—"}
                  </td>
                  <td className="px-4 py-3 font-mono font-medium"
                    style={{ color: (p.profit ?? 0) >= 0 ? "var(--accent-green)" : "var(--risk-critical)" }}>
                    {p.profit != null ? (p.profit >= 0 ? "+" : "") + p.profit.toLocaleString("en-US", { minimumFractionDigits: 2, maximumFractionDigits: 2 }) : "—"}
                  </td>
                  <td className="px-4 py-3 font-mono" style={{ color: "var(--text-secondary)" }}>
                    {p.swap?.toFixed(2) ?? "—"}
                  </td>
                  <td className="px-4 py-3 font-mono" style={{ color: "var(--text-secondary)" }}>
                    {fmtTs(p.open_time_msc)}
                  </td>
                </tr>
              ))
            }
          </tbody>
        </table>

        {!isLoading && !data?.items.length && (
          <div className="py-12 text-center">
            <p className="text-sm" style={{ color: "var(--text-secondary)" }}>No open positions</p>
          </div>
        )}
      </div>

      {data && totalPages > 1 && (
        <div className="flex items-center justify-between mt-4">
          <p className="text-xs" style={{ color: "var(--text-secondary)" }}>
            Page {page} of {totalPages}
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

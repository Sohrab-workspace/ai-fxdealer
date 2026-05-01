"use client"

import { useState } from "react"
import { useQuery } from "@tanstack/react-query"
import { getAccounts } from "@/lib/api"
import { fmtTs } from "@/lib/utils"
import { Search } from "lucide-react"

export default function AccountsPage() {
  const [page, setPage] = useState(1)
  const [search, setSearch] = useState("")
  const [sourceSystem, setSourceSystem] = useState("")
  const PAGE_SIZE = 50

  const { data, isLoading } = useQuery({
    queryKey: ["accounts", page, search, sourceSystem],
    queryFn: () => getAccounts({ page, page_size: PAGE_SIZE, search: search || undefined, source_system: sourceSystem || undefined }),
    placeholderData: prev => prev,
  })

  const totalPages = data ? Math.ceil(data.total / PAGE_SIZE) : 1

  return (
    <div>
      <div className="mb-6">
        <h1 className="text-xl font-bold text-white">Accounts</h1>
        <p className="text-sm mt-1" style={{ color: "var(--text-secondary)" }}>
          {data?.total.toLocaleString() ?? "—"} total accounts across all source systems
        </p>
      </div>

      {/* Filters */}
      <div className="flex gap-3 mb-4">
        <div className="relative flex-1 max-w-xs">
          <Search size={14} className="absolute left-3 top-1/2 -translate-y-1/2" style={{ color: "var(--text-secondary)" }} />
          <input
            type="text"
            placeholder="Search login, name..."
            value={search}
            onChange={e => { setSearch(e.target.value); setPage(1) }}
            className="w-full pl-8 pr-3 py-2 rounded-lg text-sm text-white outline-none"
            style={{ background: "#0f0f0f", border: "1px solid var(--color-border)" }}
          />
        </div>
        <select
          value={sourceSystem}
          onChange={e => { setSourceSystem(e.target.value); setPage(1) }}
          className="px-3 py-2 rounded-lg text-sm text-white outline-none"
          style={{ background: "#0f0f0f", border: "1px solid var(--color-border)" }}
        >
          <option value="">All Systems</option>
          <option value="mt5">MT5</option>
          <option value="mt4">MT4</option>
          <option value="ctrader">cTrader</option>
        </select>
      </div>

      {/* Table */}
      <div className="rounded-xl overflow-hidden" style={{ border: "1px solid var(--color-border)" }}>
        <table className="w-full text-xs">
          <thead>
            <tr style={{ background: "#0d0d0d", borderBottom: "1px solid var(--color-border)" }}>
              {["Login", "Name", "Group", "System", "Balance", "Equity", "Leverage", "Country", "Last Access"].map(h => (
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
                      <div className="h-3.5 rounded" style={{ background: "#141414", width: `${60 + Math.random() * 40}%` }} />
                    </td>
                  ))}
                </tr>
              ))
              : data?.items.map(a => (
                <tr key={a.id} style={{ borderBottom: "1px solid #0d0d0d" }}
                  className="hover:bg-[#0d0d0d] cursor-pointer transition-colors">
                  <td className="px-4 py-3 font-mono font-medium text-white">{a.login ?? "—"}</td>
                  <td className="px-4 py-3 text-white" style={{ maxWidth: 150, overflow: "hidden", textOverflow: "ellipsis", whiteSpace: "nowrap" }}>
                    {a.account_name || "—"}
                  </td>
                  <td className="px-4 py-3 font-mono" style={{ color: "var(--text-secondary)" }}>
                    {a.group_name || "—"}
                  </td>
                  <td className="px-4 py-3">
                    <span className="px-1.5 py-0.5 rounded text-xs font-medium uppercase"
                      style={{
                        background: a.source_system === "mt5" ? "rgba(45,97,255,0.15)" : "rgba(59,164,104,0.15)",
                        color: a.source_system === "mt5" ? "var(--color-primary)" : "var(--accent-green)",
                      }}>
                      {a.source_system}
                    </span>
                  </td>
                  <td className="px-4 py-3 font-mono" style={{ color: (a.balance ?? 0) >= 0 ? "var(--accent-green)" : "var(--risk-critical)" }}>
                    {a.balance?.toLocaleString("en-US", { minimumFractionDigits: 2, maximumFractionDigits: 2 }) ?? "—"}
                  </td>
                  <td className="px-4 py-3 font-mono" style={{ color: "var(--text-secondary)" }}>
                    {a.equity?.toLocaleString("en-US", { minimumFractionDigits: 2, maximumFractionDigits: 2 }) ?? "—"}
                  </td>
                  <td className="px-4 py-3 font-mono" style={{ color: "var(--text-secondary)" }}>
                    {a.leverage ? `1:${a.leverage}` : "—"}
                  </td>
                  <td className="px-4 py-3" style={{ color: "var(--text-secondary)" }}>{a.country || "—"}</td>
                  <td className="px-4 py-3 font-mono" style={{ color: "var(--text-secondary)" }}>
                    {fmtTs(a.last_access_ts)}
                  </td>
                </tr>
              ))
            }
          </tbody>
        </table>

        {!isLoading && !data?.items.length && (
          <div className="py-12 text-center">
            <p className="text-sm" style={{ color: "var(--text-secondary)" }}>No accounts found</p>
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
            <button
              onClick={() => setPage(p => Math.max(1, p - 1))}
              disabled={page === 1}
              className="px-3 py-1.5 rounded-lg text-xs font-medium disabled:opacity-40"
              style={{ background: "#141414", border: "1px solid var(--color-border)", color: "white" }}
            >
              Prev
            </button>
            <button
              onClick={() => setPage(p => Math.min(totalPages, p + 1))}
              disabled={page === totalPages}
              className="px-3 py-1.5 rounded-lg text-xs font-medium disabled:opacity-40"
              style={{ background: "#141414", border: "1px solid var(--color-border)", color: "white" }}
            >
              Next
            </button>
          </div>
        </div>
      )}
    </div>
  )
}

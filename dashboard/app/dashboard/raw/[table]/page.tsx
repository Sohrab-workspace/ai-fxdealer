"use client"

import { useState } from "react"
import { useParams } from "next/navigation"
import { useQuery } from "@tanstack/react-query"
import { getRawTable } from "@/lib/api"

function tableTitle(name: string) {
  const parts = name.replace(/^raw_/, "").split("_")
  const src = parts[0]
  const entity = parts.slice(1).join(" ")
  const srcLabel =
    src === "mt5" ? "MT5"
    : src === "mt4" ? "MT4"
    : src === "ctrader" ? "cTrader"
    : src.toUpperCase()
  return `${srcLabel} ${entity.charAt(0).toUpperCase() + entity.slice(1)}`
}

function fmtCell(val: unknown): string {
  if (val === null || val === undefined) return "—"
  const s = String(val)
  return s.length > 42 ? s.slice(0, 39) + "…" : s
}

function fmtColHeader(col: string) {
  return col.replace(/_/g, " ")
}

function isIdCol(col: string) {
  return col === "id" || col.endsWith("_id") || col === "broker_id"
}

export default function RawTablePage() {
  const params = useParams()
  const tableName = params.table as string
  const [page, setPage] = useState(1)
  const [search, setSearch] = useState("")
  const [searchInput, setSearchInput] = useState("")
  const PAGE_SIZE = 50

  const { data, isLoading, error } = useQuery({
    queryKey: ["raw-table", tableName, page, search],
    queryFn: () => getRawTable(tableName, { page, page_size: PAGE_SIZE, search: search || undefined }),
    placeholderData: prev => prev,
    retry: 1,
  })

  const totalPages = data ? Math.ceil(data.total / PAGE_SIZE) : 1

  const handleSearch = (e: React.FormEvent) => {
    e.preventDefault()
    setSearch(searchInput)
    setPage(1)
  }

  return (
    <div>
      <div className="mb-5 flex items-start justify-between">
        <div>
          <h1 className="text-xl font-bold text-white">{tableTitle(tableName)}</h1>
          <p className="text-xs mt-1 font-mono" style={{ color: "var(--text-secondary)" }}>
            {tableName}
            {data && <span> · {data.total.toLocaleString()} rows</span>}
          </p>
        </div>
      </div>

      <form onSubmit={handleSearch} className="flex gap-2 mb-4">
        <input
          type="text"
          placeholder="Search text columns..."
          value={searchInput}
          onChange={e => setSearchInput(e.target.value)}
          className="px-3 py-2 rounded-lg text-sm text-white outline-none"
          style={{ background: "#0f0f0f", border: "1px solid var(--color-border)", minWidth: 220 }}
        />
        <button
          type="submit"
          className="px-4 py-2 rounded-lg text-sm font-medium text-white"
          style={{ background: "var(--color-primary)" }}
        >
          Search
        </button>
        {search && (
          <button
            type="button"
            onClick={() => { setSearch(""); setSearchInput(""); setPage(1) }}
            className="px-4 py-2 rounded-lg text-sm font-medium"
            style={{ background: "#141414", border: "1px solid var(--color-border)", color: "var(--text-secondary)" }}
          >
            Clear
          </button>
        )}
      </form>

      {error && (
        <div className="rounded-xl p-4 mb-4" style={{ background: "#1a0a0a", border: "1px solid var(--risk-critical)" }}>
          <p className="text-sm font-mono" style={{ color: "var(--risk-critical)" }}>
            {String(error)}
          </p>
        </div>
      )}

      <div className="rounded-xl overflow-x-auto" style={{ border: "1px solid var(--color-border)" }}>
        <table className="text-xs" style={{ minWidth: "100%" }}>
          <thead>
            <tr style={{ background: "#0d0d0d", borderBottom: "1px solid var(--color-border)" }}>
              {isLoading
                ? Array.from({ length: 7 }).map((_, i) => (
                  <th key={i} className="px-4 py-3 text-left" style={{ whiteSpace: "nowrap" }}>
                    <div className="h-3 rounded" style={{ background: "#1a1a1a", width: 60 + i * 8 }} />
                  </th>
                ))
                : data?.columns.map(col => (
                  <th
                    key={col}
                    className="px-4 py-3 text-left font-medium uppercase tracking-wide"
                    style={{ color: "var(--text-secondary)", whiteSpace: "nowrap" }}
                  >
                    {fmtColHeader(col)}
                  </th>
                ))
              }
            </tr>
          </thead>
          <tbody>
            {isLoading
              ? Array.from({ length: 15 }).map((_, i) => (
                <tr key={i} style={{ borderBottom: "1px solid #0d0d0d" }}>
                  {Array.from({ length: 7 }).map((_, j) => (
                    <td key={j} className="px-4 py-3">
                      <div className="h-3.5 rounded" style={{ background: "#141414", width: `${35 + (j * 11) % 45}%` }} />
                    </td>
                  ))}
                </tr>
              ))
              : data?.items.map((row, i) => (
                <tr
                  key={i}
                  style={{ borderBottom: "1px solid #0d0d0d" }}
                  className="hover:bg-[#0d0d0d] transition-colors"
                >
                  {data.columns.map(col => (
                    <td
                      key={col}
                      className="px-4 py-3 font-mono"
                      style={{
                        color: isIdCol(col) ? "var(--text-secondary)" : "white",
                        whiteSpace: "nowrap",
                      }}
                      title={String(row[col] ?? "")}
                    >
                      {fmtCell(row[col])}
                    </td>
                  ))}
                </tr>
              ))
            }
          </tbody>
        </table>

        {!isLoading && !error && data?.items.length === 0 && (
          <div className="py-12 text-center">
            <p className="text-sm" style={{ color: "var(--text-secondary)" }}>No data in this table</p>
          </div>
        )}
      </div>

      {data && totalPages > 1 && (
        <div className="flex items-center justify-between mt-4">
          <p className="text-xs" style={{ color: "var(--text-secondary)" }}>
            Page {page} of {totalPages} ({data.total.toLocaleString()} rows)
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

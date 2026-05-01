"use client"

import { useState } from "react"
import { useQuery } from "@tanstack/react-query"
import { getRuleScores, getRuleScoresSummary } from "@/lib/api"
import { severityColor, severityLabel } from "@/lib/utils"

export default function RulesPage() {
  const [page, setPage] = useState(1)
  const [severity, setSeverity] = useState("")
  const PAGE_SIZE = 50

  const { data: summary } = useQuery({ queryKey: ["scores-summary"], queryFn: getRuleScoresSummary })
  const { data, isLoading } = useQuery({
    queryKey: ["rule-scores", page, severity],
    queryFn: () => getRuleScores({ page, page_size: PAGE_SIZE, severity: severity || undefined }),
    placeholderData: prev => prev,
  })

  const totalPages = data ? Math.ceil(data.total / PAGE_SIZE) : 1

  return (
    <div>
      <div className="mb-6">
        <h1 className="text-xl font-bold text-white">Risk Scores</h1>
        <p className="text-sm mt-1" style={{ color: "var(--text-secondary)" }}>
          Latest rule engine evaluation per account
        </p>
      </div>

      {/* Summary cards */}
      {summary && (
        <div className="grid grid-cols-2 lg:grid-cols-4 gap-4 mb-6">
          {[
            { label: "Abuse Candidates", key: "abuse_candidate" as const, color: "var(--risk-critical)" },
            { label: "Suspicious", key: "suspicious" as const, color: "var(--risk-high)" },
            { label: "Monitor", key: "monitor" as const, color: "var(--risk-medium)" },
            { label: "Normal", key: "normal" as const, color: "var(--risk-low)" },
          ].map(row => (
            <button
              key={row.key}
              onClick={() => { setSeverity(severity === row.key ? "" : row.key); setPage(1) }}
              className="rounded-xl p-4 text-left transition-all"
              style={{
                border: `1px solid ${severity === row.key ? row.color : "var(--color-border)"}`,
                background: severity === row.key ? `${row.color}15` : "#0a0a0a",
              }}
            >
              <p className="text-xs font-medium uppercase tracking-wide" style={{ color: "var(--text-secondary)" }}>
                {row.label}
              </p>
              <p className="text-2xl font-bold font-mono mt-2" style={{ color: row.color }}>
                {summary[row.key].toLocaleString()}
              </p>
            </button>
          ))}
        </div>
      )}

      {/* Filter bar */}
      {severity && (
        <div className="flex items-center gap-2 mb-4">
          <span className="text-sm" style={{ color: "var(--text-secondary)" }}>Filtering:</span>
          <span className="px-2 py-0.5 rounded text-xs font-medium" style={{ background: `${severityColor(severity)}20`, color: severityColor(severity) }}>
            {severityLabel(severity)}
          </span>
          <button onClick={() => setSeverity("")} className="text-xs" style={{ color: "var(--text-secondary)" }}>Clear ✕</button>
        </div>
      )}

      {/* Table */}
      <div className="rounded-xl overflow-hidden" style={{ border: "1px solid var(--color-border)" }}>
        <table className="w-full text-xs">
          <thead>
            <tr style={{ background: "#0d0d0d", borderBottom: "1px solid var(--color-border)" }}>
              {["Account", "Login", "Score", "Severity", "Evaluated At"].map(h => (
                <th key={h} className="px-4 py-3 text-left font-medium uppercase tracking-wide"
                  style={{ color: "var(--text-secondary)" }}>{h}</th>
              ))}
            </tr>
          </thead>
          <tbody>
            {isLoading
              ? Array.from({ length: 10 }).map((_, i) => (
                <tr key={i} style={{ borderBottom: "1px solid #0d0d0d" }}>
                  {Array.from({ length: 5 }).map((_, j) => (
                    <td key={j} className="px-4 py-3">
                      <div className="h-3.5 rounded" style={{ background: "#141414", width: "60%" }} />
                    </td>
                  ))}
                </tr>
              ))
              : data?.items.map(s => (
                <tr key={s.id} style={{ borderBottom: "1px solid #0d0d0d" }}
                  className="hover:bg-[#0d0d0d] transition-colors">
                  <td className="px-4 py-3 font-mono" style={{ color: "var(--text-secondary)" }}>
                    {s.source_account_id}
                  </td>
                  <td className="px-4 py-3 font-mono font-medium text-white">{s.login ?? "—"}</td>
                  <td className="px-4 py-3">
                    <div className="flex items-center gap-2">
                      <div
                        className="h-1.5 rounded-full"
                        style={{
                          width: 60,
                          background: "#1a1a1a",
                        }}
                      >
                        <div
                          className="h-full rounded-full"
                          style={{
                            width: `${Math.min(100, s.total_score)}%`,
                            background: severityColor(s.severity),
                          }}
                        />
                      </div>
                      <span className="font-mono font-medium" style={{ color: severityColor(s.severity) }}>
                        {s.total_score}
                      </span>
                    </div>
                  </td>
                  <td className="px-4 py-3">
                    <span
                      className="px-1.5 py-0.5 rounded text-xs font-medium capitalize"
                      style={{
                        background: `${severityColor(s.severity)}20`,
                        color: severityColor(s.severity),
                      }}
                    >
                      {severityLabel(s.severity)}
                    </span>
                  </td>
                  <td className="px-4 py-3 font-mono" style={{ color: "var(--text-secondary)" }}>
                    {s.evaluated_at.slice(0, 19)}
                  </td>
                </tr>
              ))
            }
          </tbody>
        </table>

        {!isLoading && !data?.items.length && (
          <div className="py-12 text-center">
            <p className="text-sm" style={{ color: "var(--text-secondary)" }}>No scored accounts</p>
          </div>
        )}
      </div>

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

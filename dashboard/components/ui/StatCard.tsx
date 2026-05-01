interface StatCardProps {
  label: string
  value: string | number
  sub?: string
  color?: string
}

export function StatCard({ label, value, sub, color }: StatCardProps) {
  return (
    <div
      className="rounded-xl p-5"
      style={{ border: "1px solid var(--color-border)", background: "#0a0a0a" }}
    >
      <p className="text-xs font-medium uppercase tracking-wide" style={{ color: "var(--text-secondary)" }}>
        {label}
      </p>
      <p className="text-2xl font-bold mt-2 font-mono" style={{ color: color || "white" }}>
        {typeof value === "number" ? value.toLocaleString() : value}
      </p>
      {sub && (
        <p className="text-xs mt-1" style={{ color: "var(--text-secondary)" }}>{sub}</p>
      )}
    </div>
  )
}

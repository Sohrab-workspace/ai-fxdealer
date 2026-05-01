import { type ClassValue, clsx } from "clsx"
import { twMerge } from "tailwind-merge"

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs))
}

export function fmtNumber(n: number | null | undefined, decimals = 2): string {
  if (n == null) return "—"
  return n.toLocaleString("en-US", { minimumFractionDigits: decimals, maximumFractionDigits: decimals })
}

export function fmtPrice(n: number | null | undefined, decimals = 5): string {
  if (n == null) return "—"
  return n.toFixed(decimals)
}

export function fmtLots(n: number | null | undefined): string {
  if (n == null) return "—"
  return n.toFixed(2)
}

export function fmtProfit(n: number | null | undefined): string {
  if (n == null) return "—"
  const s = fmtNumber(n, 2)
  return n >= 0 ? `+${s}` : s
}

export function fmtTs(ms: number | null | undefined): string {
  if (!ms) return "—"
  // Detect ms vs seconds (ms > year-2000 in ms = ~9.5e11)
  const d = ms > 1e12 ? new Date(ms) : new Date(ms * 1000)
  return d.toISOString().replace('T', ' ').slice(0, 19)
}

export function severityColor(s: string): string {
  switch (s) {
    case "abuse_candidate": return "var(--risk-critical)"
    case "suspicious":      return "var(--risk-high)"
    case "monitor":         return "var(--risk-medium)"
    case "normal":          return "var(--risk-low)"
    default:                return "var(--risk-none)"
  }
}

export function severityLabel(s: string): string {
  switch (s) {
    case "abuse_candidate": return "Abuse"
    case "suspicious":      return "Suspicious"
    case "monitor":         return "Monitor"
    case "normal":          return "Normal"
    default:                return s
  }
}

export function directionLabel(d: number | null): string {
  if (d === 0) return "BUY"
  if (d === 1) return "SELL"
  return "—"
}

export function sourceSystemBadge(s: string): string {
  switch (s) {
    case "mt5":     return "MT5"
    case "mt4":     return "MT4"
    case "ctrader": return "CT"
    default:        return s.toUpperCase()
  }
}

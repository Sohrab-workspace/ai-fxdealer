"use client"

import { useState } from "react"
import Link from "next/link"
import { usePathname } from "next/navigation"
import {
  LayoutDashboard,
  Users,
  BarChart2,
  TrendingUp,
  AlertTriangle,
  Activity,
  Settings,
  Database,
  ChevronDown,
  ChevronRight,
} from "lucide-react"
import { cn } from "@/lib/utils"

const navItems = [
  { label: "Dashboard", href: "/dashboard", icon: LayoutDashboard },
  { label: "Accounts", href: "/dashboard/accounts", icon: Users },
  { label: "Positions", href: "/dashboard/positions", icon: TrendingUp },
  { label: "Deals", href: "/dashboard/deals", icon: BarChart2 },
  { label: "Price Feed", href: "/dashboard/ticks", icon: Activity },
  { label: "Risk Scores", href: "/dashboard/rules", icon: AlertTriangle },
  { label: "Collectors", href: "/dashboard/collectors", icon: Settings },
]

const rawGroups = [
  {
    label: "MT5",
    tables: [
      "raw_mt5_accounts",
      "raw_mt5_deals",
      "raw_mt5_positions",
      "raw_mt5_orders",
      "raw_mt5_ticks",
      "raw_mt5_server_logs",
    ],
  },
  {
    label: "MT4",
    tables: [
      "raw_mt4_accounts",
      "raw_mt4_deals",
      "raw_mt4_orders",
      "raw_mt4_server_logs",
    ],
  },
  {
    label: "cTrader",
    tables: [
      "raw_ctrader_deals",
      "raw_ctrader_positions",
      "raw_ctrader_symbols",
      "raw_ctrader_groups",
    ],
  },
]

function tableLabel(name: string) {
  return name.replace(/^raw_(mt5|mt4|ctrader)_/, "").replace(/_/g, " ")
}

export function Sidebar() {
  const pathname = usePathname()
  const [rawOpen, setRawOpen] = useState(pathname.includes("/dashboard/raw"))

  return (
    <aside
      className="fixed left-0 top-0 h-full w-56 flex flex-col z-30"
      style={{ background: "#080808", borderRight: "1px solid var(--color-border)" }}
    >
      <div className="px-4 py-5 flex items-center gap-2" style={{ borderBottom: "1px solid var(--color-border)" }}>
        <div className="w-7 h-7 rounded-md flex items-center justify-center text-white font-bold text-sm"
          style={{ background: "var(--color-primary)" }}>
          FX
        </div>
        <span className="font-semibold text-white text-sm">AI FXDealer</span>
      </div>

      <nav className="flex-1 px-2 py-4 space-y-0.5 overflow-y-auto">
        {navItems.map(item => {
          const active = pathname === item.href || (item.href !== "/dashboard" && pathname.startsWith(item.href))
          return (
            <Link
              key={item.href}
              href={item.href}
              className={cn(
                "flex items-center gap-3 px-3 py-2 rounded-lg text-sm font-medium transition-colors",
                active
                  ? "text-white"
                  : "text-[--text-secondary] hover:text-white hover:bg-[#111]"
              )}
              style={active ? {
                background: "var(--bg-sidebar-active)",
                borderLeft: "2px solid var(--color-primary)",
                color: "white",
              } : {}}
            >
              <item.icon size={16} />
              {item.label}
            </Link>
          )
        })}

        {/* Raw Tables section */}
        <div className="pt-2">
          <p className="px-3 pb-1 text-xs font-semibold uppercase tracking-wider" style={{ color: "#333" }}>
            Dev Tools
          </p>
          <button
            onClick={() => setRawOpen(o => !o)}
            className="flex items-center justify-between w-full px-3 py-2 rounded-lg text-sm font-medium transition-colors"
            style={{
              color: rawOpen ? "white" : "var(--text-secondary)",
              background: rawOpen ? "var(--bg-sidebar-active)" : "transparent",
            }}
          >
            <span className="flex items-center gap-3">
              <Database size={16} />
              Raw Tables
            </span>
            {rawOpen ? <ChevronDown size={13} /> : <ChevronRight size={13} />}
          </button>

          {rawOpen && (
            <div className="mt-1 space-y-2 pl-2">
              {rawGroups.map(group => (
                <div key={group.label}>
                  <p className="px-3 py-1 text-xs font-semibold uppercase tracking-wide"
                    style={{ color: "#444" }}>
                    {group.label}
                  </p>
                  {group.tables.map(table => {
                    const href = `/dashboard/raw/${table}`
                    const active = pathname === href
                    return (
                      <Link
                        key={table}
                        href={href}
                        className={cn(
                          "flex items-center px-3 py-1.5 rounded-lg text-xs font-medium transition-colors pl-5",
                          active
                            ? "text-white"
                            : "text-[--text-secondary] hover:text-white hover:bg-[#111]"
                        )}
                        style={active ? {
                          background: "var(--bg-sidebar-active)",
                          borderLeft: "2px solid var(--color-primary)",
                          color: "white",
                        } : {}}
                      >
                        {tableLabel(table)}
                      </Link>
                    )
                  })}
                </div>
              ))}
            </div>
          )}
        </div>
      </nav>

      <div className="px-4 py-4" style={{ borderTop: "1px solid var(--color-border)" }}>
        <p className="text-xs" style={{ color: "var(--text-secondary)" }}>Test Broker</p>
        <p className="text-xs font-medium text-white mt-0.5">admin@test.com</p>
      </div>
    </aside>
  )
}

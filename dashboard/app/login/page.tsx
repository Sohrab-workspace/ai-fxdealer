"use client"

import { useState } from "react"
import { useRouter } from "next/navigation"
import { login } from "@/lib/api"

export default function LoginPage() {
  const router = useRouter()
  const [email, setEmail] = useState("admin@test.com")
  const [password, setPassword] = useState("admin123")
  const [slug, setSlug] = useState("test-broker")
  const [error, setError] = useState("")
  const [loading, setLoading] = useState(false)

  async function handleSubmit(e: React.FormEvent) {
    e.preventDefault()
    setLoading(true)
    setError("")
    try {
      await login(email, password, slug)
      router.push("/dashboard")
    } catch {
      setError("Invalid credentials. Check email, password and broker slug.")
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="min-h-screen flex items-center justify-center" style={{ background: "var(--bg-base)" }}>
      <div className="w-full max-w-md p-8 rounded-xl border" style={{ borderColor: "var(--color-border)", background: "#0a0a0a" }}>
        <div className="mb-8">
          <h1 className="text-2xl font-bold text-white">AI FXDealer</h1>
          <p className="text-sm mt-1" style={{ color: "var(--text-secondary)" }}>FX Risk & Compliance Platform</p>
        </div>

        <form onSubmit={handleSubmit} className="space-y-4">
          <div>
            <label className="block text-sm font-medium mb-1.5" style={{ color: "var(--text-secondary)" }}>
              Broker Slug
            </label>
            <input
              type="text"
              value={slug}
              onChange={e => setSlug(e.target.value)}
              className="w-full px-3 py-2 rounded-lg text-sm text-white outline-none focus:ring-1"
              style={{ background: "#141414", border: "1px solid var(--color-border)", "--tw-ring-color": "var(--color-primary)" } as React.CSSProperties}
              placeholder="test-broker"
            />
          </div>
          <div>
            <label className="block text-sm font-medium mb-1.5" style={{ color: "var(--text-secondary)" }}>
              Email
            </label>
            <input
              type="email"
              value={email}
              onChange={e => setEmail(e.target.value)}
              className="w-full px-3 py-2 rounded-lg text-sm text-white outline-none focus:ring-1"
              style={{ background: "#141414", border: "1px solid var(--color-border)" } as React.CSSProperties}
            />
          </div>
          <div>
            <label className="block text-sm font-medium mb-1.5" style={{ color: "var(--text-secondary)" }}>
              Password
            </label>
            <input
              type="password"
              value={password}
              onChange={e => setPassword(e.target.value)}
              className="w-full px-3 py-2 rounded-lg text-sm text-white outline-none focus:ring-1"
              style={{ background: "#141414", border: "1px solid var(--color-border)" } as React.CSSProperties}
            />
          </div>

          {error && (
            <div className="text-sm rounded-lg px-3 py-2" style={{ background: "#2a0a0a", color: "var(--risk-critical)", border: "1px solid #4a1010" }}>
              {error}
            </div>
          )}

          <button
            type="submit"
            disabled={loading}
            className="w-full py-2.5 rounded-lg text-sm font-medium text-white transition-opacity"
            style={{ background: "var(--color-primary)", opacity: loading ? 0.7 : 1 }}
          >
            {loading ? "Signing in..." : "Sign in"}
          </button>
        </form>
      </div>
    </div>
  )
}

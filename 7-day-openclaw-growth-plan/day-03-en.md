# Day 3 — Stabilization: Security Baseline

> **Phase**: Stabilization (Day 3–4)  
> **User Goal**: Trust — "My agent is safe to run"  
> **Agent Milestone**: Security health check passed. Claw Health Report generated.  
> **Psychological Payoff**: Confidence — "I know what I've given this agent access to"

---

## Why Today Matters

Your agent is now running real tasks autonomously.

That's exactly when security stops being optional.

Most OpenClaw users skip this step. They configure their agent, watch it run, and move on — until something goes wrong. A leaked API key. An agent that responds to strangers. A skill that has more access than it should.

Day 3 is about three things, in order:

1. **See your current state** — run a health check, understand what you have
2. **Lock the front door** — control who can talk to your agent and trigger actions
3. **Protect your credentials and limit execution** — so a mistake doesn't become a crisis

> 💡 **The right mental model for agent security:**
> This isn't about defending against hackers. It's about **preventing your own agent from going out of bounds** — through misconfiguration, a bad skill, or a prompt injection attack.
> *Agent security = preventing model loss of control, not just keeping bad actors out.*

---

## Task 1 — Run BotLearn Doctor (Security Mode)

You already ran BotLearn Doctor on Day 1 for a system overview. Today you run it again with a security focus — it will surface specific configuration gaps and tell you exactly what to fix.

```
Run BotLearn doctor security
```

Your agent returns a **Security Diagnostic Report**:

```
🔒 BotLearn Doctor — Security Diagnostic
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

AUTHENTICATION
  Gateway Auth: ✅ Enabled
  ACP Token: ✅ Secured (file-based)
  Web Interface Password: ⚠️ Default detected — CHANGE THIS

NETWORK EXPOSURE
  Gateway Port: ✅ Not publicly exposed
  SSRF Protection: ✅ Enabled (trusted-network mode)

ACCESS CONTROL
  admin_ids configured: ⚠️ Not set — all users can trigger exec
  Allowed users list: ⚠️ Not configured

CREDENTIALS
  API Keys in code or SKILL.md: ⚠️ Detected — move to .env
  .env in .gitignore: ✅ Yes

SKILL AUDIT
  Total installed: 5 · Verified source: 5/5
  Suspicious permissions: 0

RISK SCORE: ⚠️ MEDIUM — 3 items need attention

REQUIRED ACTIONS
  1. Set admin_ids to restrict who can trigger agent actions
  2. Move API keys out of SKILL.md into .env
  3. Change web interface password
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

Work through the flagged items in Tasks 2 and 3 below. BotLearn Doctor will re-scan after each fix to confirm the issue is resolved.

---

## Task 2 — Lock the Front Door: Access Control

By default, your OpenClaw agent may respond to anyone who can reach it. That means anyone who discovers your endpoint can trigger commands — including `exec` (run shell commands) and `write` (modify files).

This is the first red line to enforce.

### Configure who your agent listens to

OpenClaw supports multiple message channels — Telegram, Discord, WhatsApp, Slack, WeChat, and others. Regardless of which channel you use, the access control principle is the same: explicitly declare who counts as an authorized user, and restrict sensitive permissions to that list only.

In your `openclaw.json` or `.env`:

```json
{
  "admin_ids": ["your-user-id"],
  "allowed_users": ["your-user-id"]
}
```

How to find your user ID depends on your channel:
- **Telegram:** message `@userinfobot`
- **Discord:** enable Developer Mode → right-click your username → Copy User ID
- **Slack:** profile page → More → Copy member ID
- Other channels: check your platform's developer or account settings

**What this enforces:**
- Only listed users can trigger agent actions
- Anyone else who reaches your endpoint gets no response to sensitive commands
- `exec` and `write` permissions are restricted to admin tier only

### Close your public network exposure

Your agent should not be visible to the open internet.

```bash
openclaw doctor --check-network
```

If you're running on a VPS, use Tailscale or ZeroTier for private access instead of opening ports directly. Your messaging channel acts as the controlled public surface — your bot token or webhook URL is the only thing that needs to be externally reachable. Keep those credentials secret.

> **Red line:** No unauthorized user should ever be able to trigger `exec` or `write` on your agent.

> **A note on performance:** These restrictions will make some tasks feel slightly slower or more cautious — that's intentional. As you spend more time with your agent and develop a clearer picture of how it behaves, you can gradually expand its permissions. Trust is earned through observation. Start tight, loosen deliberately.

---

## Task 3 — Protect Credentials + Limit Execution

### Move API keys out of your code

Every API key in your setup — OpenAI, Anthropic, Telegram, Google, AWS — belongs in a `.env` file, not in `SKILL.md`, not in your config, not in a GitHub repo.

If your key is in a file that could be shared, pasted, or pushed, it's already at risk.

**The right pattern:**

```bash
# .env  ← never commit this file
OPENAI_API_KEY=sk-...
TELEGRAM_BOT_TOKEN=...
ANTHROPIC_API_KEY=sk-ant-...
```

```bash
# .gitignore  ← always include these
.env
openclaw.json
```

Set spending limits on your API accounts as a second line of defense. A leaked key with a $10/day cap causes far less damage than one without.

> **Red line:** API key leaked = reset it immediately. Don't investigate first. Reset first.

### Limit what your agent can execute

Your agent has the technical ability to run shell commands on your machine. Restrict its boundary to a defined workspace:

```bash
openclaw configure --set exec.allowed_paths="/home/youruser/openclaw-workspace"
openclaw configure --set exec.deny_paths="/etc,/usr,/System,/var"
```

If you're running OpenClaw in Docker, mount only what your agent actually needs:

```bash
docker run -v ~/openclaw-workspace:/app/workspace openclaw/openclaw
```

> **Red line:** Your agent should never have write access to system directories. A model that hallucinates with root access is one bad prompt away from a real incident.

---

## Task 4 — Require Approval for New Skills

```
Require my approval before installing any new skills
```

Your agent confirms:

```
✅ Skill installation approval required.
I'll ask before installing anything new.
```

This closes the most common supply chain attack vector. Nothing installs without your review.

---

## Today's Observable Output

By the end of Day 3, you should have:

- ✅ **BotLearn Doctor** security diagnostic complete
- ✅ `admin_ids` configured — only you can trigger agent actions
- ✅ API keys in `.env`, out of code and SKILL.md
- ✅ Execution paths restricted to your workspace
- ✅ Skill install approval enabled
- ✅ BotLearn Doctor re-scan: Risk score GREEN

---

## Extended Reading (Optional)

- [The Four-Layer Security Model](./agent-security-layers.md) — Network isolation, permission minimization, secrets management, and execution control

---

## Tomorrow: Day 4 — Personalize Your Agent

Security baseline is set. Now comes the most important day of the protocol.

You'll inject your personal context — who you are, how you work, what you care about — and execute your first advanced, high-frequency scenario.

Three paths. You choose.

→ [Continue to Day 4](./day-04.md)

---

*BotLearn 7-Day Agent Activation Protocol · [botlearn.ai](https://botlearn.ai)*

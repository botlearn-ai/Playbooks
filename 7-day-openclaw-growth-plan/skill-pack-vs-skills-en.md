# More Skills Is Not What You Need — You Need a Skill Pack

> **Related to**: Day 2 — First Real Task  
> **Reading time**: ~6 minutes  
> **What you'll understand after reading**: Why installing more skills makes your agent worse — and the right mental model for choosing what to install

---

When people first discover ClawHub, the instinct is natural: more skills = smarter agent. Browse the registry, install everything that looks useful, and watch your agent level up.

This is exactly wrong.

Here's why — and what to do instead.

---

## The 4 Hidden Costs of Too Many Skills

### 1. Intelligence Degradation (Confusion)

Before your agent answers any question, it reads the description of every installed skill and loads them into its context window. This is how it knows what tools are available.

With 700 skills, 80% of your agent's working memory is consumed just reading the tool list — before it's done any actual thinking. Less context for reasoning means worse outputs. Your agent doesn't get smarter by having more options. It gets confused.

### 2. Decision Paralysis (Ambiguity)

Many skills overlap in function. `write_file`, `edit_file`, `append_file` — all write to files. `web_fetch`, `web_scrape`, `browser_use` — all retrieve web content.

When your agent has 10 tools that can "write a file," it wastes reasoning cycles choosing between them. In ambiguous cases, it may pick the wrong one, or stall. Fewer, cleaner tools lead to faster, more reliable execution.

### 3. Security Risk

Every third-party skill you install is code running on your machine with access to your agent's context, your file system, and potentially your credentials. More installed skills means a larger attack surface.

In February 2026, security researchers identified 341+ malicious skills on ClawHub that exfiltrated SSH keys and API tokens from affected machines. Each one looked legitimate. The attack vector was simply: install, run, exfiltrate.

The fewer third-party skills you have installed, the smaller your exposure.

### 4. Cost Explosion (Token Burn)

Every conversation sends your full skill list to the LLM. More skills = more tokens per request = higher API costs. With a large skill registry, you may be paying for hundreds of tool descriptions on every single message — including simple ones that don't use tools at all.

---

## The Right Principle: Start Minimal, Add Deliberately

> Install only what you need. Use bundled skills first. Add third-party skills only when bundled options genuinely can't do the job.

### Principle 1 — Use Bundled Skills First

OpenClaw ships with a set of built-in (bundled) skills that are pre-verified, have minimal dependencies, and are maintained by the OpenClaw team. These are your defaults.

Before installing anything from ClawHub, check whether a bundled skill already covers your need. Most common tasks — web search, file management, sending messages, reading documents — are handled by bundled skills out of the box.

### Principle 2 — The 3-Filter Test for New Skills

Before installing any skill, apply this test:

**Frequent use** — Will you use this skill every day or every week? If it's for a one-off task, consider doing it manually or composing it from existing skills.

**Replaces real effort** — Does this skill meaningfully reduce repetitive manual work? Automation that saves 5 seconds isn't worth the complexity it adds.

**Controlled permissions** — Does the skill require more access than the task demands? Avoid skills that request broad file system access, network access to unknown endpoints, or access to your credentials for reasons that aren't clear.

If a skill doesn't pass all three, don't install it.

---

## How to Install Skills (4 Methods, Ranked by Safety)

### Method 1 — Bundled Skills (Recommended)

Pre-installed with OpenClaw. Enable them directly without any installation step. Focus on whether local dependencies (e.g., `brew` packages) are required.

These are verified, low-risk, and should be your first resort.

### Method 2 — Dashboard / GUI

Browse and install from OpenClaw's built-in skill library via the dashboard. Convenient and relatively safe — the library is curated. Still: check the author, install count, and skill source before installing anything.

### Method 3 — CLI / Registry (`clawhub install`)

Installing via ClawHub or other external registries gives you access to the full community skill ecosystem. This is the most flexible option — and the highest risk.

Only install skills from authors you recognize or have verified. Read the `SKILL.md` source before running anything. When in doubt, don't.

```bash
clawhub install author/skill-name
```

### Method 4 — Local Manual Installation

Because a skill is just a directory + `SKILL.md`, you can manage skills entirely as local assets:

- Clone from a trusted repository into your local skills directory
- Version-control with Git
- Review every change before it runs

This gives you full auditability and is the right approach for production environments or any deployment where security matters.

---

## Skills vs. Skill Packs: What's the Difference?

A **skill** is a single capability: `web_fetch`, `send_telegram`, `summarize_pdf`.

A **skill pack** is a composed set of skills designed to work together for a specific workflow. The Morning Brief you set up on Day 2 isn't a single skill — it's a pipeline of ingestion + curation + synthesis + delivery skills working in sequence.

The distinction matters because:

- Installing individual skills and hoping they compose well leads to the fragmentation problems described above
- A well-designed skill pack handles the composition for you — the skills are chosen to work together, tested as a unit, and optimized for the workflow end-to-end

When you evaluate what to install, think in workflows, not individual capabilities. "I need a morning brief" is the right starting point — not "I need an RSS reader and a summarizer and a Telegram sender."

---

## The Minimal Viable Skill Set

For most users going through the 7-Day Protocol, this is the reference set — organized by category, not by day.

**BotLearn Protocol Skills** (install as you progress through each day)

| Skill | Day | Purpose |
|---|---|---|
| `botlearn-doctor` | Day 1 | System health diagnostic + OpenClaw Health Report |
| `botlearn-examiner` | Day 1 | 8-dimension capability assessment + baseline score |
| `botlearn-autodidact` | Day 6 | Self-analysis and improvement proposal cycle |
| `botlearn-graduate` | Day 7 | Before/after comparison + 7-Day Growth Summary |

**Morning Brief Pipeline** (pick one, not all)

| Skill | Best for |
|---|---|
| `dinstein/tech-news-digest` | Tech & AI focus, fastest setup |
| `kevinho/clawfeed` | Long-term, team-grade intelligence |
| `steipete/blogwatcher` | Monitoring specific sources / niche feeds |

**Day 5 Advanced Scenario** (pick one scenario)

| Skill | Scenario |
|---|---|
| `psmamm/social-media-agent` | Social media monitoring + drafting |
| `market-environment-analysis` + `finnhub-pro` | Market / opportunity radar |
| `gog` + `audsmith28/meeting-prep-agent` | Inbox triage + meeting prep |

**Channel Integration** (your messaging layer — already configured from Day 1)

Telegram, Discord, WhatsApp, Feishu, Slack — whichever you set up with OpenClaw. This is not an additional install; it's your existing channel connection.

**Everything else: bundled first.** Web search, file management, document reading — check bundled skills before going to ClawHub. Most common tasks are already covered.

---

*BotLearn 7-Day Agent Activation Protocol · [botlearn.ai](https://botlearn.ai)*

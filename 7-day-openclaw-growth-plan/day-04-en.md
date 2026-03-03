# Day 4 — Stabilization: Personalize Your Agent

> **Phase**: Stabilization (Day 3–4)  
> **User Goal**: "My agent knows me — and acts like it"  
> **Agent Milestone**: Core context files configured. Agent behaves as an executor, not a consultant.  
> **Psychological Payoff**: Belonging — "This is my agent"

---

## What Happens Today

Up to now, your agent has been generic — it could be anyone's agent.

Today you change that. You'll configure the context files that shape how your agent thinks, decides, and acts. By the end of Day 4, your agent will know who you are, what you value, and — critically — that its job is to **do things**, not just advise on them.

This last point matters more than most people realize. Without proper configuration, agents default to consulting mode: they ask clarifying questions, offer options, hedge recommendations, and wait for approval. That behavior is safe — and mostly useless for getting real work done.

Day 4 is where you fix that.

---

## The Context Files: What They Do

OpenClaw uses a set of workspace files to give your agent persistent identity and behavioral direction. Think of them as your agent's operating manual — written by you, read by it on every interaction.

**P0 — Configure these today:**

| File | Purpose |
|------|---------|
| `SOUL.md` | Core values, priorities, and behavioral principles — the "why" behind how your agent acts |
| `USER.md` | Who you are: name, role, background, communication style, context |
| `AGENTS.md` | How your agent should operate: execution bias, permission scope, decision-making style |

**P1 — Add when ready:**

| File | Purpose |
|------|---------|
| `HEARTBEAT.md` | Your routines: working hours, peak focus time, recurring commitments |
| `MEMORY.md` | Persistent facts your agent should always carry: key people, ongoing projects, preferences |

---

## Task 1 — Configure SOUL.md

`SOUL.md` is your agent's value system. It answers: *when this agent faces a decision, what does it optimize for?*

```
Set up my agent's soul file
```

Or write it directly. A strong `SOUL.md` is short and opinionated:

```markdown
# Soul

## Core Values
- Move fast. A done task is worth more than a perfect plan.
- Be direct. No filler, no hedging, no unnecessary caveats.
- Default to action. When in doubt, attempt and report back.

## Priorities
1. Complete the task as requested
2. Flag blockers immediately — don't sit on them
3. Ask clarifying questions only when genuinely blocked, not as a default behavior

## Communication Style
- Short responses unless detail is explicitly needed
- Conclusions first, reasoning second
- Never ask multiple questions in one message
```

The last section — *ask clarifying questions only when genuinely blocked* — is what separates an executor from a consultant. Set this explicitly.

---

## Task 2 — Configure USER.md

`USER.md` gives your agent the personal context it needs to make good judgments on your behalf.

```
Set up my user profile
```

Or send a paragraph and let your agent parse it:

```
Here's my context: I'm a product manager at an AI startup, based in 
San Jose, UTC-8. I work best in the mornings. I have 3 direct reports. 
I care about moving fast, clear communication, and not wasting time in 
meetings. I'm focused on BotLearn's 7-day activation protocol right now.
```

Your agent will extract and write a structured `USER.md`. Review it and correct anything that's off.

---

## Task 3 — Configure AGENTS.md (Most Important)

`AGENTS.md` is the most operationally important file you'll configure today. It defines your agent's **execution behavior** — how it handles ambiguity, what it's allowed to do without asking, and where it should pause for human input.

This is where most agents fail. Left unconfigured, an agent will:
- Ask for confirmation before every action
- Offer 3 options instead of doing the obvious one
- Hedge everything with "it depends"
- Never actually run anything without explicit instruction

That's not an agent. That's a chatbot with better memory.

```
Set up my agents configuration file
```

A working `AGENTS.md` explicitly grants execution authority:

```markdown
# Agents Configuration

## Execution Bias
Default to execution over consultation. When a task is clear, do it.
When a task is ambiguous, make a reasonable assumption, execute, 
and report what you assumed. Do not ask for permission to begin.

## What I Can Do Without Asking
- Send messages via configured channels
- Read and summarize files and emails
- Search the web and compile research
- Run scheduled tasks (morning brief, monitoring)
- Create, edit, and organize files within the workspace

## What Requires My Approval
- Sending emails externally on my behalf
- Making purchases or API calls with cost implications
- Deleting files or data
- Anything that can't be easily undone

## Decision-Making Style
- If a task has one obvious path: take it
- If a task has multiple valid paths: pick the best one and tell me why
- If genuinely blocked: ask one specific question, not a list

## Permission Scope
Refer to Day 3 security configuration for execution boundaries.
Within those boundaries, operate with full autonomy.
```

**The key principle:** permissions and autonomy are not in conflict — they define each other. Clear boundaries let your agent move fast *within* them, without second-guessing every step.

---

## Task 4 — Verify Personalization Is Working

After configuring the three P0 files, test whether your agent has absorbed them:

```
What should I prioritize this morning?
```

A well-configured agent gives you a direct answer based on your role, your current focus, and your working style — not a generic list of productivity tips.

If it responds with questions or hedges, your `AGENTS.md` execution bias isn't set strongly enough. Tighten it.

```
Summarize my current situation and suggest one thing to do next.
```

This is the gold standard test: does your agent act like it knows you, or does it act like it just met you?

---

## P1 (Optional): HEARTBEAT.md + MEMORY.md

When you're ready to go deeper:

**HEARTBEAT.md** — your daily and weekly rhythms:
```
Set up my heartbeat file — I work 9am–6pm PT, 
focused work in the mornings, meetings on Tuesday and Thursday afternoons,
and I do a weekly review every Friday at 4pm.
```

**MEMORY.md** — persistent facts worth carrying everywhere:
```
Add to my memory: 
- My main project right now is BotLearn
- Key stakeholder: [name], focused on growth metrics
- We're targeting 50 activated agents by end of Q1
```

These two files make your agent progressively smarter about your context over time. They're not required today — but the earlier you start, the faster it compounds.

---

## Today's Observable Output

By the end of Day 4, you should have:

- ✅ `SOUL.md` configured — your agent has values and communication principles
- ✅ `USER.md` configured — your agent knows who you are
- ✅ `AGENTS.md` configured — your agent is biased toward execution, not consultation
- ✅ Personalization verified: agent responds with context-aware, action-oriented answers
- ✅ (Optional) `HEARTBEAT.md` and `MEMORY.md` started

---

## Tomorrow: Day 5 — First Advanced Task

Personalization is done. Tomorrow you'll put your configured agent to work on its first real high-frequency scenario.

Three paths based on how you work. You choose.

→ [Continue to Day 5](./day-05.md)

---

*BotLearn 7-Day Agent Activation Protocol · [botlearn.ai](https://botlearn.ai)*

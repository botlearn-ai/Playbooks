# Day 5 — Optimization: First Advanced Task

> **Phase**: Optimization (Day 5–6)  
> **User Goal**: "My agent just handled something I would have done myself"  
> **Agent Milestone**: First high-frequency, real-world workflow executed  
> **Psychological Payoff**: Capability — "This agent is actually useful"

---

## What Happens Today

Your agent knows you. It's configured to execute, not consult.

Today you give it a real job — one that was previously costing you time, attention, or money.

Pick the scenario that matches your actual pain point. Run it end to end. You're not testing your agent anymore. You're deploying it.

---

## Choose Your Scenario (Pick 1)

---

### 🟠 Scenario A — Social Media Monitoring Stack

**Your pain:** You're missing what's happening on Reddit, YouTube, and Twitter/X — trends, sentiment shifts, emerging topics — because you can't monitor all three manually.

**What your agent does:** Monitors social platforms for signals relevant to your domain. Each skill covers one platform. No content publishing in this stack — this is pure monitoring and intelligence gathering.

| Skill | Platform | What it does |
|---|---|---|
| `reddit-readonly` | Reddit | Monitors trending posts and keyword mentions without login |
| `youtube-full` | YouTube | Fetches video data, comment sentiment, subtitles via API |
| `psmamm/social-media-agent` | Twitter/X + others | Browser-based agent that operates social platforms like a real user |

**Best for:** Researchers, founders, marketers, and anyone who needs early signal on what's moving online.

**Install the stack:**

```bash
clawhub install reddit-readonly
clawhub install youtube-full           # ⚠️ confirm install success before proceeding
clawhub install psmamm/social-media-agent
```

---

**`reddit-readonly` — Reddit monitoring**

```
Monitor r/ArtificialIntelligence for new trending posts about "OpenAI" in the last 24 hours. Summarize the top 3 and send them to me.
```
```
Find posts mentioning "Bitcoin" in r/CryptoCurrency from the past 48 hours. What is the overall sentiment?
```
```
Identify the fastest-growing topics in r/wallstreetbets today.
```

---

**`youtube-full` — YouTube intelligence**

```
Using youtube-full, analyze this video [URL]. What are people complaining about in the comments?
```
```
Download subtitles from this video [URL] and summarize the key arguments made.
```
```
Summarize the top 10 comments on this channel [channel name] from the past 7 days.
```

---

**`psmamm/social-media-agent` — Twitter/X monitoring**

```
Use social-media-agent to check Twitter. What are the top trending topics right now?
```
```
Search Twitter for discussions about "AI agents" in the last 48 hours. List the top 5 posts by engagement.
```
```
Use social-media-agent to check replies under this tweet [URL] and summarize the main reactions.
```

---

### 🟠 Scenario B — Financial Intelligence Stack

**Your pain:** You're afraid of missing market signals — insider moves, sentiment shifts, macro changes, or prediction market odds. By the time you see it, it's already priced in.

**What your agent does:** Monitors financial markets and news across three data sources, each covering a distinct intelligence layer. Every task is explicitly mapped to the skill that handles it.

| Skill | Data source | What it covers |
|---|---|---|
| `finnhub` | Finnhub API | Stock news, news sentiment, insider trading data |
| `fmp` | Financial Modeling Prep | Macro market analysis, stock fundamentals, valuation |
| `polymarket` | Polymarket | Prediction market odds on political and macro events |

**Best for:** Traders, investors, growth hackers, and competitive intelligence operators.

**Install the stack:**

```bash
clawhub install finnhub
clawhub install fmp
clawhub install polymarket
```

---

**`finnhub` — News & insider trading**

```
Using Finnhub, check recent insider trading activity for NVDA in the past 30 days.
```
```
Using Finnhub, find the latest news sentiment score for AAPL. Is it positive or negative?
```
```
Using Finnhub, list all insider transactions for MSFT in the past 30 days.
```

---

**`fmp` — Macro & fundamentals**

```
Using FMP, give me a macro market environment report for today. What are the key signals?
```
```
Using FMP, analyze TSLA fundamentals. What are the current valuation metrics?
```
```
Using FMP, provide valuation metrics for META — P/E, EV/EBITDA, and revenue growth.
```

---

**`polymarket` — Prediction markets**

```
Using Polymarket, what are the current odds for the 2026 US midterm election outcomes?
```
```
Using Polymarket, what is the current probability of a US recession in 2026?
```
```
Using Polymarket, check any macro events with odds above 70% right now.
```

---

### 🟠 Scenario C — The Inbox Defence System

**Your pain:** Information overload. Important emails get buried. You walk into meetings unprepared. Your inbox is a to-do list you never chose.

**What your agent does:**
- Reads your Gmail and triages automatically: newsletters → archive, invoices → finance folder, investor emails → highlighted and pushed to your phone
- Generates a **pre-meeting brief** 15 minutes before each calendar event: pulls attendee LinkedIn profiles and sends you a one-page "cheat sheet" — who they are, what to bring up, what to watch for

**Best for:** Executives, busy professionals, business development, anyone in back-to-back meetings.

**Install the stack:**

```bash
clawhub install gog                              # Google suite (Gmail + Calendar + Drive)
clawhub install tonimelisma/email-to-calendar    # auto-create calendar events from emails
clawhub install audsmith28/meeting-prep-agent    # pre-meeting intel: LinkedIn research + cheat sheet
clawhub install biostartechnology/linkedin       # optional: manual LinkedIn lookup if needed
```

**First task:**

```
Triage my Gmail inbox from the last 48 hours.
Archive newsletters, flag investor emails, and file any 
invoices to my finance folder.
Then check my calendar for tomorrow and send me a 
pre-meeting brief for each event.
```

---

## After Running Your Scenario: Iterate Once

Don't accept the first output as final. Run it, read it, send one round of feedback:

- *"The Reddit summary is too long — 3 bullet points per post, no more"*
- *"Add a sentiment score to each Finnhub news item"*
- *"The pre-meeting brief is too long — bullet points only, max 5"*

Your agent will adjust and re-run. The difference between output 1 and output 2 is your first visible **capability delta**.

---

## Today's Observable Output

By the end of Day 5, you should have:

- ✅ One scenario chosen and executed end to end
- ✅ First output reviewed and iterated at least once
- ✅ Workflow confirmed repeatable — agent can run it again on command
- ✅ Task 2 complete *(first high-frequency workflow running)*

---

## Tomorrow: Day 6 — Self-Improvement

Your agent is running real work. Day 6 introduces the mechanism that makes it keep getting better — without you doing all the tuning manually.

→ [Continue to Day 6](./day-06.md)

---

*BotLearn 7-Day Agent Activation Protocol · [botlearn.ai](https://botlearn.ai)*

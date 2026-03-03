# How Morning Brief Works: Anatomy of an Intelligence Pipeline

> **Related to**: Day 2 — First Real Task  
> **Reading time**: ~8 minutes  
> **What you'll understand after reading**: What your agent is doing under the hood — and when to build your own pipeline instead of using an off-the-shelf skill

---

A Morning Brief looks simple from the outside. Under the hood, it's a four-stage pipeline. Understanding each stage helps you choose the right skill, diagnose problems, and know when you need to go custom.

---

## Stage 1 — Ingestion: Getting the Raw Material

Before your agent can summarize anything, it needs to collect it.

**RSS/Atom parsing** is the most reliable method — structured data, low friction, works for most established publications. Skills like `steipete/blogwatcher` operate purely at this layer.

**Web scraping** handles sources without RSS feeds: Twitter/X accounts, company announcement pages, niche forums. This is harder — it requires dealing with anti-scraping measures and dynamically rendered pages (headless browser). `dinstein/tech-news-digest` handles this layer for social sources.

**API integration** connects to premium or structured data sources: GitHub Trending, Product Hunt, Bloomberg, Arxiv. Higher quality but requires credentials and setup.

*Atomic skills at this stage: `web_fetch`, `rss_reader`, `twitter_scraper`*

---

## Stage 2 — Curation: Signal vs. Noise (the real moat)

This is where 80% of the quality difference lives. Raw ingestion gives you hundreds of items. Curation decides what's worth your attention.

**Deduplication** is non-negotiable. When five outlets cover the same OpenAI announcement, a good pipeline recognizes it as one story and either collapses it or surfaces the best version with supplementary links. Bad pipelines surface all five — your brief becomes a repetition machine.

**Semantic filtering** goes beyond keyword matching. It understands intent: "new model released" is different from "opinion piece about AI models." You can configure rules like: *retain technical announcements, discard commentary unless it's from a primary source.*

**Quality scoring** weights items by source authority, engagement signals, and recency. A post from a credible researcher's personal blog can outrank a listicle from a major outlet.

*Atomic skills at this stage: `semantic_search`, `content_classifier`*

---

## Stage 3 — Synthesis: Turning Content into Intelligence

Raw articles become your brief here.

**LLM summarization** condenses each item to 2–3 bullet points. Quality here comes from the prompt design: a good summarizer extracts *why it matters*, not just *what happened*.

**Cross-source validation** (advanced) compares coverage across sources to surface reporting gaps or conflicting facts. Useful for high-stakes monitoring.

**Translation** converts foreign-language sources into your preferred language mid-pipeline — so your brief stays coherent even when pulling from global sources.

*Atomic skills at this stage: `llm_chain_of_thought`, `translator`*

---

## Stage 4 — Delivery: The Last Mile

How your brief arrives shapes whether you actually read it.

Format matters: a wall of text gets skimmed and closed. Structured Markdown with emoji category headers, bold highlights, and clickable links gets read. `kevinho/clawfeed` is optimized specifically at this layer — it's why it looks and feels better than simpler alternatives.

Multi-channel delivery lets your brief reach you wherever you are: messaging channel, email, voice (TTS), or a Notion/Feishu page.

*Atomic skills at this stage: `feishu_card_builder`, `tts_generator`*

---

## How to Evaluate a Morning Brief Skill

One metric captures most of the quality difference: **signal-to-noise ratio**.

| Dimension | Low-quality skill | High-quality skill |
|-----------|------------------|-------------------|
| **Deduplication** | Same story appears 5 times from 5 outlets | 5 reports collapsed into 1, with "other angles" linked |
| **Summary depth** | First 50 words copied, or title restated | *Why it matters* extracted, not just *what happened* |
| **Source breadth** | Mainstream outlets only, homogeneous coverage | Includes "deep cuts": personal blogs, GitHub commits, Discord threads |
| **Resilience** | One failed source crashes the whole run | Skips failed sources, reports partial completion, keeps running |
| **Readability** | Plain text wall | Structured: emoji categories, bold highlights, clickable links |

**One-line test:** A good brief makes you feel like you understand the landscape. A bad one makes you feel like you have 50 more things to read.

---

## Off-the-Shelf vs. Custom: When to Build Your Own

**Start with an existing skill if:**
- You want broad tech/business coverage — what happened today
- You're a manager who needs talking points and macro trends, not technical depth
- Your use case is standard: "top Product Hunt launches" or "Hacker News Top 30"

`dinstein/tech-news-digest` is built for this. Install and go.

**Build or customize if:**
- You need domain-specific filtering: "only papers with a new Transformer architecture, not AI commentary"
- You need to combine private data: "merge industry news with my calendar — tell me what to bring up in today's client meeting"
- You need sub-minute alerting on specific conditions: "any Tesla news with negative sentiment, push immediately"
- Your sources are non-standard: private RSS feeds, internal wikis, specific GitHub repos

`steipete/blogwatcher` gives you the reliable pipe. Write your own curation and synthesis logic on top.

---

*BotLearn 7-Day Agent Activation Protocol · [botlearn.ai](https://botlearn.ai)*

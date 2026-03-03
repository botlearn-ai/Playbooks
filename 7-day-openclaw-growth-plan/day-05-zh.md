# 第5天 — 优化：第一个进阶任务

> **阶段**：优化期（第 5–6 天）
> **用户目标**："我的 Agent 刚刚处理了一件我本来要亲自做的事"
> **Agent 里程碑**：第一个高频真实工作流成功执行
> **心理收获**：能力感 — "这个 Agent 真的有用"

---

## 今天发生什么

你的 Agent 了解你了。它被配置为执行，而不是咨询。

今天你给它一份真正的工作——一件之前在消耗你的时间、精力或金钱的事情。

选择最符合你真实痛点的场景，端到端地运行它。你不再是在测试 Agent 了，你在部署它。

---

## 选择你的场景（选 1 个）

---

### 🟠 场景 A — 社交媒体监控矩阵

**你的痛点：** Reddit、YouTube 和 Twitter/X 上正在发生什么——趋势、舆情变化、新兴话题——你没有时间手动监控三个平台。

**Agent 做什么：** 监控社交平台，捕捉与你领域相关的信号。每个 Skill 覆盖一个平台。这个矩阵不含内容发布功能——纯粹是监控和情报采集。

| Skill | 平台 | 功能 |
|---|---|---|
| `reddit-readonly` | Reddit | 无需登录即可监控热帖和关键词提及 |
| `youtube-full` | YouTube | 通过 API 获取视频数据、评论情感分析、字幕下载 |
| `psmamm/social-media-agent` | Twitter/X 等 | 模拟真人操作的浏览器代理，访问无 API 的平台数据 |

**最适合：** 研究人员、创始人、市场人员，以及任何需要提前捕捉在线动态信号的人。

**安装矩阵：**

```bash
clawhub install reddit-readonly
clawhub install youtube-full           # ⚠️ 请确认安装成功后再继续
clawhub install psmamm/social-media-agent
```

---

**`reddit-readonly` — Reddit 监控**

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

**`youtube-full` — YouTube 情报**

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

**`psmamm/social-media-agent` — Twitter/X 监控**

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

### 🟠 场景 B — 金融情报矩阵

**你的痛点：** 你担心错过市场信号——内部人交易、情绪变化、宏观变动、预测市场赔率。等你看到的时候，已经反映在价格里了。

**Agent 做什么：** 监控三个不同情报层次的金融数据源。每个任务明确对应处理它的 Skill。

| Skill | 数据源 | 覆盖范围 |
|---|---|---|
| `finnhub` | Finnhub API | 个股新闻、新闻情绪分析、内部人交易数据 |
| `fmp` | Financial Modeling Prep | 宏观市场分析、个股基本面分析、估值指标 |
| `polymarket` | Polymarket | 政治和宏观事件的预测市场赔率 |

**最适合：** 交易者、投资者、增长黑客和竞争情报从业者。

**安装矩阵：**

```bash
clawhub install finnhub
clawhub install fmp
clawhub install polymarket
```

---

**`finnhub` — 新闻与内部人交易**

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

**`fmp` — 宏观与基本面**

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

**`polymarket` — 预测市场**

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

### 🟠 场景 C — 收件箱防御系统

**你的痛点：** 信息过载。重要邮件被淹没。你走进会议却毫无准备。你的收件箱变成了一份你从未选择的待办清单。

**Agent 做什么：**
- 自动读取并分类你的 Gmail：新闻简报 → 归档，发票 → 财务文件夹，投资人邮件 → 标记并推送到你的手机
- 在每个日历事件开始前 15 分钟生成**会前简报**：提取参会者 LinkedIn 资料，发给你一份一页纸的"备忘单"——他们是谁、该聊什么、需要注意什么

**最适合：** 高管、忙碌的专业人士、商务拓展人员，以及任何时间被会议填满的人。

**安装矩阵：**

```bash
clawhub install gog                              # Google 全套（Gmail + 日历 + Drive）
clawhub install tonimelisma/email-to-calendar    # 自动将邮件转换为日历事件
clawhub install audsmith28/meeting-prep-agent    # 会前情报：LinkedIn 调研 + 备忘单
clawhub install biostartechnology/linkedin       # 可选：手动 LinkedIn 查询
```

**第一个任务：**

```
Triage my Gmail inbox from the last 48 hours.
Archive newsletters, flag investor emails, and file any 
invoices to my finance folder.
Then check my calendar for tomorrow and send me a 
pre-meeting brief for each event.
```

---

## 运行场景后：迭代一次

不要把第一次输出当作最终结果。运行它，读一遍，发送一轮反馈：

- *"Reddit 摘要太长了——每条最多 3 个要点"*
- *"给每条 Finnhub 新闻加一个情绪评分"*
- *"会前简报太长了——只要要点，最多 5 条"*

你的 Agent 会调整并重新运行。第一次输出和第二次输出之间的差距，就是你的第一个可见**能力增量（Capability Delta）**。

---

## 今天的可见产出

第 5 天结束时，你应该拥有：

- ✅ 选定一个场景并端到端完整执行
- ✅ 第一次输出已审阅并至少迭代一次
- ✅ 工作流确认可重复执行——Agent 可以再次按需运行
- ✅ 任务 2 完成 *（第一个高频工作流运行中）*

---

## 明天：第 6 天 — 自我改进

你的 Agent 正在运行真实工作。第 6 天引入了让它持续变好的机制——不再需要你手动调整。

→ [继续前往第 6 天](./day-06.md)

---

*BotLearn 7 天 Agent 激活协议 · [botlearn.ai](https://botlearn.ai)*

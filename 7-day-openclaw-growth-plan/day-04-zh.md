# 第4天 — 稳定化：个性化你的 Agent

> **阶段**：稳定化（第 3–4 天）
> **用户目标**："我的 Agent 了解我，并且按照这个来行动"
> **Agent 里程碑**：核心上下文文件已配置，Agent 表现为执行者而非顾问
> **心理收获**：归属感 — "这是我的 Agent"

---

## 今天发生什么

到目前为止，你的 Agent 是通用的——它可以是任何人的 Agent。

今天你来改变这一点。你将配置塑造 Agent 思维、决策和行动方式的上下文文件。第 4 天结束时，你的 Agent 将知道你是谁、你重视什么，以及——最关键的——它的工作是**做事情**，而不只是给建议。

最后这一点比大多数人意识到的更重要。没有适当配置的情况下，Agent 会默认进入顾问模式：提问澄清、提供选项、模糊推荐、等待审批。这种行为很安全——但对于完成真正的工作来说几乎没有用。

第 4 天就是来解决这个问题的。

---

## 上下文文件：它们的作用

OpenClaw 使用一套工作区文件，为你的 Agent 提供持久的身份识别和行为方向。把它们理解为你的 Agent 的操作手册——由你撰写，每次交互时由它读取。

**P0 — 今天必须配置：**

| 文件 | 用途 |
|------|------|
| `SOUL.md` | 核心价值观、优先级和行为原则 — Agent 行动背后的"为什么" |
| `USER.md` | 你是谁：姓名、角色、背景、沟通风格、个人情况 |
| `AGENTS.md` | Agent 应如何运作：执行偏好、权限范围、决策风格 |

**P1 — 准备好了再添加：**

| 文件 | 用途 |
|------|------|
| `HEARTBEAT.md` | 你的日常节奏：工作时间、高效时间段、定期承诺 |
| `MEMORY.md` | Agent 应始终携带的持久信息：关键联系人、进行中的项目、个人偏好 |

---

## 任务 1 — 配置 SOUL.md

`SOUL.md` 是你的 Agent 的价值体系。它回答的问题是：*当这个 Agent 面临决策时，它优化的是什么？*

```
Set up my agent's soul file
```

或者直接写。一份好的 `SOUL.md` 简短而有立场：

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

最后一条——*只有在真正卡住时才提问澄清*——是区分执行者和顾问的关键。请明确设置这一条。

---

## 任务 2 — 配置 USER.md

`USER.md` 为你的 Agent 提供代表你做出正确判断所需的个人背景。

```
Set up my user profile
```

或者发送一段话，让你的 Agent 自动解析：

```
Here's my context: I'm a product manager at an AI startup, based in 
San Jose, UTC-8. I work best in the mornings. I have 3 direct reports. 
I care about moving fast, clear communication, and not wasting time in 
meetings. I'm focused on BotLearn's 7-day activation protocol right now.
```

你的 Agent 将提取信息并生成结构化的 `USER.md`。检查一遍，纠正任何不准确的地方。

---

## 任务 3 — 配置 AGENTS.md（最重要）

`AGENTS.md` 是今天你要配置的最关键文件。它定义了你的 Agent 的**执行行为**——如何处理模糊情况、哪些事情可以自主执行、哪些地方应该暂停等待人工介入。

大多数 Agent 在这里失败。没有配置的情况下，Agent 会：
- 在每次操作前要求确认
- 给出 3 个选项而不是直接执行明显的那个
- 对所有事情都以"视情况而定"来模糊回应
- 没有明确指令就不执行任何操作

那不是 Agent，那是一个记忆力更好的聊天机器人。

```
Set up my agents configuration file
```

一份有效的 `AGENTS.md` 明确授予执行权限：

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

**核心原则：** 权限和自主性并不矛盾——它们相互定义。清晰的边界让你的 Agent 在边界*内*快速行动，而不需要在每一步都重新思考。

---

## 任务 4 — 验证个性化是否生效

配置好三个 P0 文件后，测试你的 Agent 是否真的吸收了这些配置：

```
What should I prioritize this morning?
```

配置良好的 Agent 会根据你的角色、当前专注点和工作风格给出直接答案——而不是一份通用的生产力建议清单。

如果它的回应是反问或模糊，说明你的 `AGENTS.md` 执行偏好设置得不够强。加强它。

```
Summarize my current situation and suggest one thing to do next.
```

这是黄金测试：你的 Agent 表现得像认识你，还是像刚刚见到你？

---

## P1（可选）：HEARTBEAT.md + MEMORY.md

当你准备好深入时：

**HEARTBEAT.md** — 你的日常和每周节奏：
```
Set up my heartbeat file — I work 9am–6pm PT, 
focused work in the mornings, meetings on Tuesday and Thursday afternoons,
and I do a weekly review every Friday at 4pm.
```

**MEMORY.md** — 值得随时携带的持久信息：
```
Add to my memory: 
- My main project right now is BotLearn
- Key stakeholder: [name], focused on growth metrics
- We're targeting 50 activated agents by end of Q1
```

这两个文件会让你的 Agent 随着时间推移越来越了解你的处境。今天不是必须配置的——但越早开始，复利效果越快显现。

---

## 今天的可见产出

第 4 天结束时，你应该拥有：

- ✅ `SOUL.md` 已配置 — Agent 拥有价值观和沟通原则
- ✅ `USER.md` 已配置 — Agent 知道你是谁
- ✅ `AGENTS.md` 已配置 — Agent 偏向执行而非咨询
- ✅ 个性化验证通过：Agent 能给出有上下文、行动导向的回答
- ✅ （可选）`HEARTBEAT.md` 和 `MEMORY.md` 已开始填写

---

## 明天：第 5 天 — 第一个进阶任务

个性化完成了。明天你将让已配置好的 Agent 投入第一个真实的高频场景工作。

三条路径，根据你的工作方式选择。

→ [继续前往第 5 天](./day-05.md)

---

*BotLearn 7 天 Agent 激活协议 · [botlearn.ai](https://botlearn.ai)*

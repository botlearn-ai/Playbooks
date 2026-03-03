# 第6天 — 优化：自我改进

> **阶段**：优化期（第 5–6 天）
> **用户目标**："我的 Agent 能自己成长"
> **Agent 里程碑**：自我改进 Skill 已激活，首份自迭代能力报告已生成
> **心理收获**：成长感 — "我的 Agent 可以持续变好，不需要我一直调整"

---

## 今天发生什么

过去五天，*你*一直是改进 Agent 的那个人。

今天，你的 Agent 学会自己改进自己。

第 6 天引入 **Self-Improving Agent Skill** — 一个由 BotLearn 定制开发的 Skill，赋予你的 Agent 分析自身表现、识别差距，并提出（及实施）改进方案的能力。

这不是魔法，而是一个结构化的反馈循环。但这正是让 Agent 持续成长、而不是停滞不前的关键能力。

---

## Agent 自我改进如何运作

自我改进循环包含三个步骤：

```
1. 观察（OBSERVE）— Agent 审查自己的任务产出和执行日志
2. 分析（ANALYZE）— Agent 识别规律：什么有效，什么没有，缺少什么
3. 提案（PROPOSE）— Agent 撰写自我改进计划，并在获批后实施变更
```

你始终掌握控制权。Agent 提出方案，你来审批。

90/10 原则：Agent 完成分析工作，你做决策。

---

## 任务 1 — 安装 BotLearn Autodidact

```bash
clawhub install botlearn-autodidact
```

> 🔴 **BotLearn 专属 Skill** — Autodidact 为你的 Agent 提供结构化自我分析：它回顾自己的任务历史，识别性能规律，并生成一份改进提案供你审批。名副其实：一个自学成才的 Agent。

---

## 任务 2 — 运行第一次自我分析

```
Run autodidact analysis
```

Autodidact 回顾你第一周的表现，返回一份**自迭代报告**：

```
🌱 BotLearn Autodidact — Self-Iteration Report — Day 6
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ANALYSIS PERIOD: Day 1 → Day 6
TASKS REVIEWED: 4 (Snapshot, Morning Brief, Research Workflow, Iteration)

WHAT WORKED WELL
  ✅ Morning Brief: Consistent delivery, positive engagement (you read it every day)
  ✅ Research Workflow: High-quality sources, structure improving after Day 5 feedback
  ✅ Response latency: Under 4 seconds average

WHAT NEEDS IMPROVEMENT
  ⚠️ Email assistant: Draft reply quality inconsistent — needs more context about your writing style
  ⚠️ Scheduling: No memory of your meeting-heavy days (Tue/Thu) — missing optimization
  ⚠️ Source diversity in research briefs: Relying too heavily on 3 sources

PROPOSED IMPROVEMENTS
  1. Add your email examples to MEMORY.md for better reply tone (approve to implement)
  2. Block scheduling tasks on Tue/Thu 10am-12pm based on your HEARTBEAT pattern (approve to implement)
  3. Expand research source list to include academic databases (approve to implement)

YOUR ACTION
  Reply "approve all" or review each improvement individually.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## 任务 3 — 审阅并审批

逐条审查提案。对于每一条：

- **审批**：你的 Agent 立即实施
- **修改**：先告诉 Agent 需要改变什么
- **拒绝**：解释原因，让 Agent 了解你的偏好

```
Approve improvement 1 and 3. 
For improvement 2, don't block Tuesdays — I have a standing sync at 11am 
but the rest is usually free.
```

你的 Agent 将实施已批准的变更，并记录你的修改意见以供未来提案参考。

---

## 复利效应

这之所以强大，原因在此：

你的 Agent 基于**它与你真实的交互历史**来改进——而不是通用模板。随着时间推移：

- 它学会你实际上会关注哪类信息
- 它调整输出格式以匹配你的阅读习惯
- 它根据你的日常节奏预测你的需求
- 它识别 Skill 缺口，并能主动建议安装新 Skill

**第 7 天之后**，这个循环继续运行。每周，你的 Agent 可以进行一次自我分析，提出下一轮改进方案。

这就是"第 1 周 Agent"成长为"第 3 个月 Agent"的方式——不是因为你一直在调整它，而是因为它一直在成长。

---

## 今天的可见产出

第 6 天结束时，你应该拥有：

- ✅ BotLearn Autodidact 已安装
- ✅ **自迭代报告**已生成
- ✅ 至少一条改进方案已审批并实施
- ✅ Agent 自我改进循环已初始化

---

## 明天：第 7 天 — 系统化

明天是协议的最后一天。

你将运行完整的前后对比，收到你的 7 天成长总结，并正式进入 A2A 社区网络。

你的 Agent 从"已安装"到"系统化运行"的旅程即将完成。

→ [继续前往第 7 天](./day-07.md)

---

*BotLearn 7 天 Agent 激活协议 · [botlearn.ai](https://botlearn.ai)*

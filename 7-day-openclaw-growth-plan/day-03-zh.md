# 第3天 — 稳定化：安全基线

> **阶段**：稳定化（第 3–4 天）
> **用户目标**：信任 — "我的 Agent 可以安全运行"
> **Agent 里程碑**：安全健康检查通过，Claw 健康报告已生成
> **心理收获**：信心 — "我清楚地知道我给了这个 Agent 哪些权限"

---

## 为什么今天很重要

你的 Agent 现在正在自主运行真实任务。

这正是安全问题不再可选的时刻。

大多数 OpenClaw 用户会跳过这一步。他们配置好 Agent，看着它运行，然后继续——直到出了问题。API Key 泄露。Agent 开始回应陌生人。某个 Skill 拥有了超出需要的权限。

第 3 天关注三件事，按顺序：

1. **看清现状** — 运行健康检查，了解你当前的配置
2. **锁好前门** — 控制谁可以和你的 Agent 对话、触发操作
3. **保护凭证，限制执行范围** — 让一个小错误不会演变成危机

> 💡 **Agent 安全的正确心智模型：**
> 这不是在防范黑客攻击，而是在**防止你自己的 Agent 越界**——无论是因为配置错误、有问题的 Skill，还是提示词注入攻击。
> *Agent 安全 = 防止模型失控，而不仅仅是防止坏人入侵。*

---

## 任务 1 — 运行 BotLearn Doctor（安全模式）

你在第 1 天已经运行过 BotLearn Doctor 进行系统概览。今天你再次运行它，但专注于安全检查——它会暴露具体的配置缺口，并告诉你需要修复什么。

```
Run BotLearn doctor security
```

你的 Agent 返回一份**安全诊断报告**：

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

按照下方任务 2 和任务 3 逐项处理被标记的问题。BotLearn Doctor 在每次修复后会重新扫描，确认问题已解决。

---

## 任务 2 — 锁好前门：访问控制

默认情况下，你的 OpenClaw Agent 可能会响应任何能连接到它的人。这意味着任何发现你端点的人，都可以触发命令——包括 `exec`（执行 shell 命令）和 `write`（修改文件）。

这是第一条必须守住的红线。

### 配置 Agent 只响应谁

OpenClaw 支持多种消息渠道——Telegram、Discord、WhatsApp、Slack、微信等。无论你使用哪个渠道，访问控制原则是相同的：明确声明谁是授权用户，并将敏感权限限制在该列表内。

在你的 `openclaw.json` 或 `.env` 中：

```json
{
  "admin_ids": ["your-user-id"],
  "allowed_users": ["your-user-id"]
}
```

如何获取你的用户 ID 取决于你使用的渠道：
- **Telegram：** 发消息给 `@userinfobot`
- **Discord：** 开启开发者模式 → 右键点击你的用户名 → 复制用户 ID
- **Slack：** 个人资料页 → 更多 → 复制成员 ID
- 其他渠道：查阅平台的开发者或账户设置

**这样做的效果：**
- 只有列表中的用户可以触发 Agent 操作
- 其他人连接到你的端点后，对敏感命令不会得到响应
- `exec` 和 `write` 权限仅限管理员级别

### 关闭公网暴露

你的 Agent 不应该对公开互联网可见。

```bash
openclaw doctor --check-network
```

如果你在 VPS 上运行，使用 Tailscale 或 ZeroTier 进行私网访问，而不是直接开放端口。你的消息渠道充当受控的公开入口——只有你的 bot token 或 webhook URL 需要对外可达。妥善保管这些凭证。

> **红线：** 任何未授权用户都不应该能够在你的 Agent 上触发 `exec` 或 `write`。

> **关于性能的说明：** 这些限制会让某些任务感觉稍慢或更谨慎——这是刻意为之的。随着你对 Agent 行为越来越熟悉，可以逐步扩展权限。信任来自观察。从严格开始，有意地放宽。

---

## 任务 3 — 保护凭证 + 限制执行范围

### 把 API Key 移出代码

你的所有 API Key——OpenAI、Anthropic、Telegram、Google、AWS——都应该放在 `.env` 文件中，而不是 `SKILL.md`、配置文件，更不是 GitHub 仓库。

如果你的 Key 在一个可能被分享、粘贴或推送的文件里，它就已经处于风险之中。

**正确的做法：**

```bash
# .env  ← 永远不要提交这个文件
OPENAI_API_KEY=sk-...
TELEGRAM_BOT_TOKEN=...
ANTHROPIC_API_KEY=sk-ant-...
```

```bash
# .gitignore  ← 始终包含这些
.env
openclaw.json
```

在你的 API 账户上设置消费限额，作为第二道防线。一个每天上限 $10 的泄露 Key，造成的损失远比没有限额的小得多。

> **红线：** API Key 泄露 = 立即重置。不要先调查，先重置。

### 限制 Agent 的执行范围

你的 Agent 在技术上有能力在你的机器上运行 shell 命令。将其执行边界限制在一个定义好的工作区内：

```bash
openclaw configure --set exec.allowed_paths="/home/youruser/openclaw-workspace"
openclaw configure --set exec.deny_paths="/etc,/usr,/System,/var"
```

如果你在 Docker 中运行 OpenClaw，只挂载 Agent 实际需要的内容：

```bash
docker run -v ~/openclaw-workspace:/app/workspace openclaw/openclaw
```

> **红线：** 你的 Agent 永远不应该对系统目录有写权限。一个拥有 root 权限却产生幻觉的模型，只需一条错误的提示词就可能引发真实事故。

---

## 任务 4 — 要求审批新 Skill 安装

```
Require my approval before installing any new skills
```

你的 Agent 确认：

```
✅ Skill installation approval required.
I'll ask before installing anything new.
```

这关闭了最常见的供应链攻击入口。没有你的审批，任何东西都无法安装。

---

## 今天的可见产出

第 3 天结束时，你应该拥有：

- ✅ **BotLearn Doctor** 安全诊断完成
- ✅ `admin_ids` 已配置 — 只有你可以触发 Agent 操作
- ✅ API Key 已移入 `.env`，从代码和 SKILL.md 中移除
- ✅ 执行路径已限制在你的工作区
- ✅ Skill 安装审批已启用
- ✅ BotLearn Doctor 重新扫描：风险评分为绿色

---

## 延伸阅读（可选）

- [四层安全模型](./agent-security-layers.md) — 网络隔离、最小权限、凭证管理和执行控制

---

## 明天：第 4 天 — 个性化你的 Agent

安全基线已建立。接下来是协议中最重要的一天。

你将注入个人上下文——你是谁、你如何工作、你在乎什么——让 Agent 真正认识你。

三条路径，你来选择。

→ [继续前往第 4 天](./day-04.md)

---

*BotLearn 7 天 Agent 激活协议 · [botlearn.ai](https://botlearn.ai)*

![Thinking Toolkit — 久经考验的思维模型，AI 智能体的实战手册](assets/banner.png)

# 🧠 Thinking Toolkit（思维工具箱）

[English](README.md) · [Русский](README.ru.md) · **中文**

**30 个久经考验的思维模型，打包为一个可移植的技能，适用于任何 AI 智能体。**

Thinking Toolkit 教会智能体*如何思考「思考」本身*：面对一个现实中的复杂请求——
做一个决定、诊断一个问题、理解一个系统、组织一条信息——它会挑选最小够用的
结构化思维模型组合，逐步严格执行，并返回具体的产出物：加权矩阵、因果图、
事前验尸（premortem）表、逆向规划、信息草稿。

它是纯 Markdown，零运行时依赖。只要你的智能体能读文件，就能使用这个技能。

## 为什么

任由 LLM 智能体自行发挥，它会用听起来可信的行文一带而过，跳过关键步骤。
与此同时，工程、战略、情报分析和组织学习几十年来一直在把智能体每天面对的
场景——比较选项、寻找根因、无数据估算、给计划做压力测试——沉淀成有名字、
经过检验的操作程序。这个技能把这些程序变成智能体可以逐步执行的指令，并附上
从业者一路记录下来的陷阱。

设计围绕三个决定展开：

1. **选择。** 知道什么是决策矩阵不难；代价高昂的错误是在不合适的时机拿起它。
   目录编码了选择信号、对比规则（「Five Whys 追一条因果链，Ishikawa 铺开
   广度，Connection Circles 画反馈回路」），以及每个模型的反模式。
2. **流程。** 每个模型都是一张完整的操作卡片：输入、编号步骤、引导性问题、
   输出格式、完整示例、从业者记录在案的陷阱。智能体照卡片执行，不围着名词
   即兴发挥。
3. **诚实。** 核心契约区分观察到的事实与假设，标记未知而不编造证据，对重要
   结果做敏感性检验，并让每个产出物都以行动和复查触发条件收尾。

## 工作原理

当用户明确点名某个模型时，智能体加载该卡片并照做。当请求是开放式的，智能体
先识别任务类型（决策、诊断、估算、建图、化解冲突、传达信息），再经由目录中
的选择信号和对比规则路由，选出一个主模型，至多加两个补充模型。随后它界定
情境——利害、可逆性、证据——以快速、标准或深入三档执行卡片流程，检验结果中
的隐藏假设与敏感性，最后以产出物、行动和复查触发条件收尾。

技能采用**渐进式披露**以节省上下文：智能体先只读 `SKILL.md`（约 180 行），
选择不明确时查阅路由目录，并且*只*加载真正需要的模型卡片。三十个模型在被
使用之前不占任何成本。

## 模型目录

### 决策 — 12 个模型

| 模型 | 适用场景 |
|---|---|
| Six Thinking Hats（六顶思考帽） | 选择需要均衡的视角而不是争论 |
| Eisenhower Matrix（艾森豪威尔矩阵） | 任务在紧急与重要程度上各不相同 |
| Second-Order Thinking（二阶思维） | 眼前的收益可能掩盖后续影响 |
| Decision Matrix（决策矩阵） | 多个选项需按加权标准比较 |
| Impact-Effort Matrix（影响-投入矩阵） | 待办清单需要粗粒度的组合优先级 |
| Ladder of Inference（推论阶梯） | 结论可能已经超出了证据 |
| Hard Choice Model（艰难选择模型） | 不清楚该为决策投入多少精力 |
| OODA Loop（OODA 循环） | 行动进行中条件仍在变化 |
| Cynefin Framework（Cynefin 框架） | 应对方式必须匹配情境的因果性质 |
| Confidence → Speed vs. Quality | 产品工作需在速度与打磨间权衡 |
| Pareto Analysis（帕累托分析） | 少数因素可能贡献了大部分可测效应 |
| Backcasting（逆向规划） | 远期目标需要一条从终点倒推到今天的路径 |

### 解决问题 — 11 个模型

| 模型 | 适用场景 |
|---|---|
| Ishikawa Diagram（鱼骨图） | 一个明确的效应有多种可能原因 |
| Five Whys（五个为什么） | 单个事故需沿因果链追到流程级修复 |
| Abstraction Laddering（抽象阶梯） | 问题表述可能过窄或过于模糊 |
| Conflict Resolution Diagram（冲突消解图） | 对立诉求看似互不相容 |
| Zwicky Box（形态学盒） | 解决方案可由独立维度组装而成 |
| Productive Thinking Model（高效思维模型） | 已明确的问题需要完整的创造性流程 |
| Inversion（逆向思维） | 失败模式反过来揭示成功路径 |
| Red Teaming（红队演练） | 信心满满的计划需要独立的对抗性挑战 |
| Issue Trees（问题树） | 大问题需要不重叠的分解 |
| First Principles（第一性原理） | 惯例与类比限制了方案质量 |
| Fermi Estimation（费米估算） | 缺少直接数据时必须估算一个量 |

### 系统思维 — 5 个模型

| 模型 | 适用场景 |
|---|---|
| Iceberg Model（冰山模型） | 反复出现的事件指向更深层的结构与信念 |
| Connection Circles（关联环） | 变量及其反馈关系需要建图 |
| Concept Map（概念图） | 概念及其语义关系需要澄清 |
| Balancing Feedback Loop（调节回路） | 系统抵抗变化或趋向某个目标 |
| Reinforcing Feedback Loop（增强回路） | 增长或衰退自我强化 |

### 沟通 — 2 个模型

| 模型 | 适用场景 |
|---|---|
| Situation-Behavior-Impact（情境-行为-影响） | 反馈必须具体且不带评判 |
| Minto Pyramid(金字塔原理) | 忙碌的受众需要先看到结论 |

除单个模型外，目录还提供**组合配方**——经过验证的序列，如 *Consequential
choice*（Hard Choice Model → Decision Matrix → Red Teaming）或 *Root-cause
investigation*（Pareto → Iceberg → Ishikawa → Five Whys → OODA）——并附有
护栏，防止为显得全面而堆砌模型的经典错误。

## 逻辑分析（`/logic`）

30 张卡片帮你*选择如何思考*。`/logic` 做的是相反的事：它*审计已经存在的推理*
——一个论断、一段论证、一份草稿——并就其有效性给出裁决。

它交付的是**纪律，不是教科书**。模型早就知道什么是 modus tollens；`/logic`
补上的是固定流程（重建论证 → 检验形式 → 区分形式与真值 → 裁决）、一套名称稳定
的英文+拉丁文谬误分类，以及可复现的裁决格式。三种模式，按措辞路由，支持任意
语言：

- **review**（默认）——诊断并给出裁决，不改写。
- **fix**——以最小干预修复推理，保留作者语气。
- **solve**——处理教科书任务（检验三段论、构建真值表、应用密尔方法、还原省略
  三段论）。

> *「检查一下逻辑：我们上线了改版，注册量涨了，所以改版起作用了。」*
> → **1 个严重错误。** *Post hoc ergo propter hoc*——同一周上线的营销活动是未被
> 排除的原因。形式上无效；前提也许为真，但这段论证并未证明它。

模块由四个精简文件支撑：[overview](logic/overview.md)（流程 + 裁决格式）、
[谬误分类](logic/fallacies.md)、[形式有效性](logic/formal-validity.md)（三段论 +
命题逻辑）、[归纳](logic/induction.md)（密尔方法、类比、假设）。

## 安装

技能遵循 [Agent Skills](https://simonwillison.net/2025/Dec/12/openai-skills/)
约定（`SKILL.md` + 资源文件），Claude Code、OpenAI Codex CLI、OpenClaw 及
其他 SKILL.md 运行时均已支持。稳定安装会从固定且不可变的发布版本复制载荷。

### 推荐方式：验证发布版本

```bash
gh release download v1.0.0 --repo ponomr/thinking-toolkit \
  --pattern 'thinking-toolkit-v1.0.0.tar.gz' --pattern SHA256SUMS
gh release verify v1.0.0 --repo ponomr/thinking-toolkit
gh release verify-asset v1.0.0 thinking-toolkit-v1.0.0.tar.gz \
  --repo ponomr/thinking-toolkit
tar -xzf thinking-toolkit-v1.0.0.tar.gz
./thinking-toolkit/install.sh
```

需要 [GitHub CLI](https://cli.github.com/)。它会在运行安装程序前验证下载内容
确实属于已发布版本。安装程序把载荷复制到检测到的智能体目录，打印每个路径，
并把被替换的安装保留为相邻备份。

选项：

- 指定宿主：`./install.sh claude`、`codex`、`openclaw` 或自定义路径。
- `--force` 不询问直接替换已有安装，但仍会保留备份。

### 更新

更新不会在智能体会话中自动运行，必须从已安装副本中显式启动：

```bash
python3 ~/.claude/skills/thinking-toolkit/update.py --dry-run
python3 ~/.claude/skills/thinking-toolkit/update.py
```

更新程序会验证不可变发布版本及其归档，列出新增、删除和修改的文件，并在替换
前请求确认。完成后会打印备份路径和准确的回滚命令。若更新 Codex 或 OpenClaw
副本，请使用相应的安装路径。

### 手动安装

| 智能体 | 个人技能目录 | 项目级 |
|---|---|---|
| Claude Code | `~/.claude/skills/thinking-toolkit/` | `.claude/skills/thinking-toolkit/` |
| OpenAI Codex CLI | `~/.codex/skills/thinking-toolkit/` | `.codex/skills/thinking-toolkit/` |
| OpenClaw | `~/.openclaw/skills/thinking-toolkit/` | `.openclaw/skills/thinking-toolkit/` |
| 其他任意环境 | 你的运行时发现 `SKILL.md` 的位置 | — |

从解压后的发布版本中，把 `thinking-toolkit/` 目录复制到所选技能目录。仓库中的
`scripts/` 和 `tests/` 是开发工具，不会进入发布归档。使用技能无需 API 密钥、
网络或代码执行；只有在用户显式安装或更新时才会访问网络。

对于自托管网关和自定义环境：把 `SKILL.md` 注入系统上下文并使 `references/`
可读；技能除了读文件之外不做任何假设。

### 开发检出

贡献者可以克隆 `main` 并运行 `./install.sh`，但 `main` 是开发线，而不是经过审计
的发布版本。稳定用户应安装带版本号的发布版本。项目有意不支持符号链接安装，
因为它会让所有智能体绑定到可变工作目录的变化。

## 安全模型

Thinking Toolkit 是智能体会执行的指令代码，应像软件更新一样对待 Markdown 的
变化。已发布版本不可变，CI 会验证技能和归档的可复现性，更新始终需要用户显式
启动并确认。信任边界、验证命令和漏洞报告方式见 [SECURITY.md](SECURITY.md)。
发布流程和仓库保护设置记录在 [MAINTAINING.md](MAINTAINING.md)。

## 使用

按名字点用模型：

> *「对这个发布计划做一次 premortem。」*
> *「用加权矩阵比较这三家供应商。」*
> *「从三年后 newsletter 应到达的位置做 backcasting。」*

或者只描述情况，交给路由：

> *「支持工单一直在涨，我不知道从哪下手。」*
> → 用 Pareto Analysis 找出关键少数，再对最大类别做 Five Whys。

> *「我们一直在争要不要重写计费服务。」*
> → 用 Six Thinking Hats 组织讨论，选项稳定后用 Decision Matrix，
> 拍板前用 Red Teaming。

智能体会说明选择了哪个模型及原因，执行卡片流程，并返回带有假设与复查触发
条件的产出物。

## 仓库结构

```
thinking-toolkit/
├── SKILL.md                  # 入口：契约、路由、工作流
├── VERSION                   # 安装与发布版本
├── references/
│   ├── catalog.md            # 索引、别名、选择信号、组合配方
│   └── <model>.md            # 30 张操作卡片，每模型一张
├── logic/                    # /logic 流程及专项参考
├── agents/openai.yaml        # 可选的宿主发现元数据
├── scripts/                  # 验证与可复现发布构建
├── tests/                    # 回归与供应链测试
├── MAINTAINING.md            # 发布流程与仓库保护设置
├── install.sh                # 将载荷复制到技能目录
└── update.py                 # 经验证的显式更新与回滚
```

### 开发

```bash
python3 scripts/validate_skill.py .        # 结构与内容不变量
python3 -m unittest discover -s tests -v   # 验证器回归测试
python3 scripts/build_release.py           # 可复现载荷归档 + SHA256SUMS
```

验证器守护着让技能可靠的不变量：每张卡片包含全部十个操作章节，每个链接都
在仓库内部可解析，技能 payload 不含外部 URL（必须完全离线可用），目录与
卡片集合严格一致。

## 设计原则

- **构造上的供应商中立。** 不调用工具、不浏览网页、不执行代码、不假设记忆。
  任何有文件访问能力的合格 LLM 均可使用。
- **最小够用的模型组合。** 默认一个模型，至多三个，且明确允许一个都不用：
  只有在底层分析站得住脚之后，才选择沟通类模型。
- **保留用户的能动性。** 模型产出帮助做决定，决定权始终在用户手里。技能绝不
  制造证据中不存在的确定性。
- **深度匹配利害。** 可逆的低风险决定走快速通道；重大或不可逆的决定走深入
  通道——附带敏感性检验和反证搜寻。
- **确定性的质量闸门。** 仅用标准库的验证器保证 30 张卡片结构完整、路由表
  与卡片集合同步。

## 许可证

MIT — 见 [LICENSE](LICENSE)。

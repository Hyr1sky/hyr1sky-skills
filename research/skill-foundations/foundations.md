# 四个个人 Codex Skills 的理论基础与边界设计

## 研究目的

本文为以下四个待建 skills 提供设计基线：

- `software-system-mastery`
- `requirements-reality-check`
- `project-narrative-builder`
- `architecture-drift-audit`

本文不是书单摘要。每个理论只在能够改变 skill 的触发条件、分析步骤、证据要求或输出契约时才被保留。资料优先采用原作者、正式标准、权威机构页面或论文原文。

当前仓库已有两个 skills：

- `deep-reading-tutor`：围绕一篇明确的文章、论文或文档，通过导航、逐题抽问和定制笔记帮助用户学习。
- `research-codebase-to-wiki`：围绕代码库或研究实现，产出带代码锚点的静态解释型 Wiki。

新 skills 的首要设计约束不是“覆盖更多能力”，而是让调用者可以根据**中心对象和用户要完成的工作**稳定选择。

## 总体结论：用中心对象而不是分析手法划分 skills

| Skill | 中心对象 | 用户真正要完成的工作 | 核心判定问题 |
| --- | --- | --- | --- |
| `software-system-mastery` | 一个已经存在或正在形成的软件系统 | 建立能够迁移、预测和解释的系统心智模型 | “我是否已经能跨抽象层解释它为何如此工作，并预测改变的影响？” |
| `requirements-reality-check` | 一个尚未被证实的需求、方案或承诺 | 判断它在真实业务与软硬件环境中是否成立、是否值得做、如何安全落地 | “这是真需求吗；在当前约束下能否实现、验证、运维和承担后果？” |
| `project-narrative-builder` | 受众、情境与期望行动之间的关系 | 选择并组织事实，使特定受众能够理解、判断或行动 | “谁需要因这次沟通发生什么变化，哪些事实和结构最能促成它？” |
| `architecture-drift-audit` | 声明的架构意图与实际系统之间的映射关系 | 找出一致、偏离、缺失和已经失效的意图，并决定修代码还是修蓝图 | “实现是否仍兑现已接受的意图；如果没有，错的是实现、意图，还是二者之间的证据？” |

这四个对象形成一条常见但并非强制的链路：

```text
理解当前系统
    ↓
验证候选改变
    ↓
向特定受众解释决定
    ↓
持续核对实现是否兑现决定
```

链路不意味着合并。每个 skill 必须能够独立触发、独立收敛，并把相邻问题显式移交给另一个 skill。

## 理论来源以及它们具体改变什么

### 1. Domain-Driven Design：先确定意义边界，再讨论代码边界

**一手来源**

- Eric Evans，[Domain-Driven Design Reference: Definitions and Pattern Summaries](https://www.domainlanguage.com/wp-content/uploads/2016/05/DDD_Reference_2015-03.pdf)
- Eric Evans / Domain Language，[DDD Resources](https://www.domainlanguage.com/ddd/)

**采用的核心思想**

Evans 将 DDD 概括为：聚焦核心领域；由领域实践者与软件实践者共同探索模型；在明确的限界上下文内使用统一语言。限界上下文不仅可以是子系统边界，也可能与团队工作的边界重合；Context Map 则让不同模型及其上下游关系可见。DDD 的价值因此不等于实体、值对象、聚合等战术模式，而首先是对**模型适用范围、词义和协作关系**的管理。

**对 skills 的设计改变**

- `software-system-mastery` 必须先识别系统服务的领域、核心价值、关键业务词汇和模型适用范围，再进入包、类、服务等代码结构。它不得默认“仓库目录 = 领域边界”。
- `software-system-mastery` 的术语表必须允许“同一个词在不同上下文含义不同”，不能强行生成全局唯一词典。
- `requirements-reality-check` 必须先把业务语言、当前做法和目标状态讲清楚，再接受一个技术方案作为需求。一个“需要 Kafka/向量库/Agent”的句子应先还原为领域事件、信息流或决策需要。
- `project-narrative-builder` 应使用受众所在上下文中的语言，但不能为了易懂而抹去不同上下文之间真实的语义差异。
- `architecture-drift-audit` 的预期边界不仅包括技术模块，还包括限界上下文、上下游关系、翻译层和关键领域规则。边界漂移可能是模型污染，而不仅是 import 违规。
- 四个 skills 都应优先标出核心领域与通用/支撑部分，避免把分析精力平均分配给所有代码和文档。

**明确不采用的简化**

- 不把 DDD 变成所有项目必须遵循的架构模板。
- 不通过类名中是否出现 `Entity`、`Repository` 判断是否“符合 DDD”。
- 不在缺少领域复杂度时强制建立完整 Context Map。

### 2. A Philosophy of Software Design：系统掌握的目标是降低表观复杂度

**一手来源**

- John Ousterhout，[A Philosophy of Software Design 官方页面与第二版说明](https://web.stanford.edu/~ouster/cgi-bin/book.php)
- John Ousterhout，[The Nature of Complexity 课程讲义](https://web.stanford.edu/~ouster/cgi-bin/cs190-winter18/lecture.php?topic=complexity)
- John Ousterhout，[Managing Complexity 课程讲义](https://web.stanford.edu/~ouster/cgi-bin/cs190-spring15/lecture.php?topic=complexity)

**采用的核心思想**

Ousterhout 用三个症状描述开发者实际感受到的复杂性：变化放大、认知负荷和未知的未知；其主要来源是依赖与晦涩。深模块以较小接口隐藏较多复杂性，信息隐藏则让局部决策不必扩散到其他模块。设计是持续活动，不能假设第一次就能得到最终架构。

**对 skills 的设计改变**

- `software-system-mastery` 的成功标准不是“读过所有文件”，而是用户能用较少概念解释较多行为，并知道进一步查证应去哪里。
- 系统掌握过程必须显式寻找三类学习风险：一次改动会扩散到哪里、完成任务必须同时记住什么、哪些影响目前甚至不知道去哪里找。
- 输出应优先呈现深模块、公共契约、信息隐藏点和高扇出依赖，而不是按目录逐项复述。
- `architecture-drift-audit` 除结构违规外，还应检查接口是否泄漏实现知识、责任是否被迫跨多个模块协调，以及“看似局部的改变”是否持续放大。
- 漂移审计不能把任何与最初设计不同的实现都判错；持续设计意味着有些变化应通过新 ADR 或更新蓝图合法化。

### 3. 架构视图、关注点与质量属性：没有一张万能架构图

**一手来源**

- ISO，[ISO/IEC/IEEE 42010:2022 — Architecture Description](https://www.iso.org/standard/74393.html)
- CMU Software Engineering Institute，[Documenting Software Architectures: Views and Beyond](https://insights.sei.cmu.edu/library/documenting-software-architectures-views-and-beyond-second-edition/)
- Nick Rozanski 与 Eoin Woods，[Viewpoints and Perspectives 官方资料](https://www.viewpoints-and-perspectives.info/home/book/)
- Rozanski 与 Woods，[Architectural Perspectives](https://www.viewpoints-and-perspectives.info/home/perspectives/)
- CMU Software Engineering Institute，[Reasoning About Software Quality Attributes](https://www.sei.cmu.edu/library/reasoning-about-software-quality-attributes/)
- CMU Software Engineering Institute，[Software Architecture in Practice, Fourth Edition](https://www.sei.cmu.edu/library/software-architecture-in-practice-fourth-edition/)

**采用的核心思想**

ISO 42010 区分“实体真实拥有的架构”和“表达该架构的架构描述”，并通过 stakeholder、concern、viewpoint、view 与 model kind 组织描述。SEI 的 Views and Beyond 同样强调：先判断利益相关者要完成什么工作，再选择有价值的视图。Rozanski 与 Woods 进一步区分结构性的 viewpoints 与跨多个视图施加影响的 perspectives，例如安全、性能、可用性和演进性。

SEI 的质量属性研究还指出，仅说“系统要高性能/高可用/易扩展”不足以分析架构；需要用情境把刺激源、刺激、环境、受影响对象、响应和可度量响应具体化，并考虑一种架构策略对其他质量属性的副作用。

**对 skills 的设计改变**

- `software-system-mastery` 不固定产出一套大而全的章节。它应根据用户问题选择视图，候选集合包括：使命/上下文、领域、功能、信息、运行时、代码模块、部署、开发与决策历史。
- 每个视图必须写明它服务的关注点和证据来源；图只是模型的表达，不得被当作系统本身。
- 性能、安全、可用性、可观测性、可修改性、可测试性等应作为跨视图 perspective 动态选择，而不是每次机械遍历完整清单。
- `requirements-reality-check` 必须把抽象质量词改写成可观察场景，至少包含环境、触发条件、期望行为和验收尺度。
- `architecture-drift-audit` 的基准不能只有一张静态图；它还应包括跨视图约束和质量属性场景。某项结构仍“长得一样”，也可能已经无法满足原本的性能或恢复目标。
- 所有 skills 在证据不足时必须区分“系统事实”“架构描述中的声明”和“分析者的推断”。

### 4. 需求工程与系统工程：同时检查“把设计做对”和“做的是对的设计”

**一手来源**

- ISO，[ISO/IEC/IEEE 29148:2018 — Requirements Engineering](https://www.iso.org/standard/72089.html)
- NASA，[Systems Engineering Handbook: Fundamentals](https://www.nasa.gov/reference/2-0-fundamentals-of-systems-engineering/)
- NASA，[Systems Engineering Handbook, Rev. 2 PDF](https://www.nasa.gov/wp-content/uploads/2018/09/nasa_systems_engineering_handbook_0.pdf)
- NASA，[Systems Engineering Handbook Appendix：需求与 V&V 检查表](https://www.nasa.gov/reference/system-engineering-handbook-appendix/)

**采用的核心思想**

ISO 29148 将需求工程放在系统和软件的完整生命周期内，并区分业务/使命分析、利益相关者需要、系统或软件需求及其管理，而非直接从一句诉求跳到规格。NASA 的系统工程方法把 ConOps、系统边界、需求分配、接口、技术权衡、风险、验证与确认，以及成本和进度放在同一个全局视角中。NASA 特别区分：验证证明产品符合需求，确认则证明得到的系统能够满足客户期望和预期用途。

**对 skills 的设计改变**

- `requirements-reality-check` 必须从业务/使命、利益相关者和现状开始，禁止把用户提出的实现手段直接升级为已确认需求。
- 检查对象必须覆盖真实基础：现有流程、人员与权限、数据可得性和质量、设备与传感器、算力/网络/存储、第三方系统、接口、部署环境、维护能力、预算与时间。
- 每个关键需求都应拥有上游理由、责任人、依赖、验收方法和生命周期影响；无法追溯的需求标记为假设，而不是补写成事实。
- 分析至少覆盖正常、峰值、降级、恢复和维护场景；对安全关键或强物理约束系统，再增加事故、误用和环境边界场景。
- 输出必须分别回答：需求是否真实、方案是否可行、系统是否可验证、上线后是否可操作与维护、失败由谁承担。
- `software-system-mastery` 在理解系统时可借用 ConOps 和接口分析，但不得因此替代需求判断。

### 5. 修辞情境与 Diátaxis：受众不是人口标签，而是能够促成变化的人

**一手来源**

- Lloyd F. Bitzer，[The Rhetorical Situation 原文](https://wac.gmu.edu/wp-content/uploads/bitzer.pdf)
- Daniele Procida，[Diátaxis 官方指南](https://diataxis.fr/)
- Daniele Procida，[Diátaxis: Start Here](https://diataxis.fr/start-here/)

**采用的核心思想**

Bitzer 将修辞情境组织为 exigence、audience 和 constraints。这里的受众并不是“看到文本的人”，而是有能力促成所需变化的人；事实、信念、利益、文档、关系和表达者自身都会约束决策与行动。Diátaxis 则按用户需要区分教程、操作指南、参考和解释，指出学习与工作、行动与认知是不同沟通任务，混合它们常常使文档失焦。

**对 skills 的设计改变**

- `project-narrative-builder` 的第一输入不是文档格式，而是修辞简报：需要改变的现实、能够促成改变的受众、期望决策/行动、既有信念、主要阻力、证据门槛和时间约束。
- “给老板看”“面向客户”仍然太粗。skill 必须继续问或推断：此人能批准、采用、评审、资助还是执行什么。
- 叙事结构应由沟通任务决定：教学、完成工作、查询事实和建立理解不能共享同一模板。
- skill 的职责是证据选择、主张顺序、异议处理和行动闭环；PPT、网页或文档的视觉排版应交给相应制品 skill。
- 叙事不能倒置证据关系：可以根据受众改变粒度、术语和顺序，但不能改变事实状态或隐藏关键不确定性。
- `software-system-mastery` 面向用户本人建立能力；`project-narrative-builder` 面向一个需要被推动的外部或内部受众。即便产物都包含“解释”，中心任务仍不同。

### 6. Software Reflexion Models：用显式映射比较意图和现实

**一手来源**

- Gail C. Murphy、David Notkin、Kevin Sullivan，[Software Reflexion Models: Bridging the Gap Between Source and High-Level Models](https://www.cs.ubc.ca/~murphy/papers/rm/fse95.html)
- Murphy、Notkin、Sullivan，[Extending and Managing Software Reflexion Models](https://www.cs.ubc.ca/sites/default/files/tr/1997/TR-97-15_0.pdf)

**采用的核心思想**

Reflexion Models 不要求先得到完整精确的逆向工程模型。工程师先给出一个高层模型，再把源代码实体映射到高层实体，工具据此汇总高层关系与源代码关系一致或不一致的部分。这种方法把“不完整但有意义的架构假设”作为观察代码的透镜，并允许通过迭代映射逐步提高认识。

**对 skills 的设计改变**

- `architecture-drift-audit` 必须要求一个可辨认的“意图基线”和从实现证据到基线元素的映射；没有意图基线时只能先重建候选蓝图，不能宣称发现“漂移”。
- 审计的最小分类应保留 Reflexion Models 的精神：
  - **convergence**：预期关系在实现中有证据；
  - **divergence**：实现出现基线不允许或未预期的关系；
  - **absence**：基线期待的关系在实现中没有证据；
  - **unmapped / unresolved**：实现元素或基线元素尚无法可靠映射。
- 本 skill 额外增加 **stale intent**：证据表明实现改变可能合理，但旧基线没有被更新。该类别属于判断扩展，不应伪装成原论文的自动判定。
- 每个发现必须包含基线声明、实现证据、映射规则、置信度和影响范围。不能只凭目录名称或架构图视觉相似度判定。
- 审计应允许从粗粒度开始，优先检查高风险边界，再迭代细化；不要求第一次遍历全部代码。

### 7. ADR：让原始意图、约束和代价保持可见

**一手来源**

- Michael Nygard，[Documenting Architecture Decisions](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions)

**采用的核心思想**

Nygard 将架构显著决定界定为影响结构、非功能特性、依赖、接口或构建方式的决定，并建议用小型、模块化的 ADR 保留 Context、Decision、Status 和 Consequences。旧决定被替代时应保留并标记 superseded，因为历史语境仍然有价值。后果必须包含正面、负面和中性影响。

**对 skills 的设计改变**

- `architecture-drift-audit` 必须把 ADR 当作意图证据之一，而不是把当前 README 或代码注释自动视为最高权威。
- 发现偏离后不能统一建议“改回去”。可选处置至少包括：修正实现、更新蓝图、补写/替代 ADR、接受临时例外并设置期限、增加自动约束。
- 如果背景条件已经变化，skill 应指出需要重开决定，而不是以历史 ADR 压制演进。
- `requirements-reality-check` 的重大权衡在被接受后可以移交为 ADR 候选；在需求尚未证实时，不应过早生成“Accepted”决定。
- `project-narrative-builder` 可以把 ADR 的 context—decision—consequences 转成决策叙事，但不能改写其状态。

### 8. C4：建立可缩放的静态结构地图，但不把地图当全貌

**一手来源**

- Simon Brown，[C4 Model Introduction](https://c4model.com/introduction)
- Simon Brown，[C4 Model Abstractions](https://c4model.com/abstractions)

**采用的核心思想**

C4 用 Person、Software System、Container、Component 和 Code 提供层级化、abstraction-first 的静态结构语言，并通过 Context、Container、Component、Code 等图逐层缩放。其目标之一是避免临时“方框与箭头”图中的抽象层混杂、未标注关系和模糊命名。

**对 skills 的设计改变**

- `software-system-mastery` 和 `architecture-drift-audit` 应建立清晰的缩放层级，禁止在同一视图中把企业系统、进程、类和数据表当作同级方框。
- 图上元素至少写明名称、类型、责任，关系写明方向与含义；“业务逻辑”“公共模块”之类名称不能代替责任。
- C4 主要表达静态结构，运行时序列、状态、数据生命周期、质量属性和决策仍需其他视图。skills 不得把生成 C4 图等同于完成系统掌握或架构审计。
- Code 级视图只有在能回答当前问题时才生成；能够从代码自动查询的细节无需手工维护成永久蓝图。

### 9. Evolutionary Architecture：从一次性审计走向可持续约束

**一手来源**

- Neal Ford、Rebecca Parsons、Patrick Kua，[Building Evolutionary Architectures 官方概要](https://evolutionaryarchitecture.com/precis.html)

**采用的核心思想**

作者将 evolutionary architecture 定义为支持多维度、受引导的增量变化。Architectural fitness function 对重要架构特征提供客观的完整性评估，可以通过测试、指标、部署流水线或其他工程机制持续执行。关注点不局限于技术结构，还包括数据、安全、可扩展性、可测试性和运维等维度。

**对 skills 的设计改变**

- `architecture-drift-audit` 的最终目标不是一份静态报告，而是为高价值、可客观判断的架构规则提出 fitness function 候选。
- 只有明确、重要且可测量的规则才自动化。含糊的设计品味或尚未接受的意图不能伪装成 CI 门禁。
- 每个自动约束建议需注明检测对象、执行时机、失败阈值、误报风险和规则所有者。
- `requirements-reality-check` 应前瞻性询问“哪项成功条件上线后需要持续监测”，把一次性验收与运行期保障区分开。
- 演进发生在多个维度；不能因为模块依赖合规，就忽略数据质量、恢复能力或安全边界的退化。

## 四个 skill 的建议契约

### `software-system-mastery`

#### 中心对象

一个需要被真正掌握的软件系统，包括其使命、领域模型、运行行为、代码与部署结构、质量属性和决策历史。

#### 核心问题

用户能否在相关抽象层之间来回移动，解释系统为什么如此工作，用证据区分事实与假设，并预测一个变化可能影响什么？

#### 适用

- 接手陌生项目、遗留系统或跨团队系统。
- 希望为开发、架构评审、故障排查或面试建立系统级理解。
- 已经有代码和文档，但心智模型碎片化。
- 用户希望通过追问、解释和实际任务检验掌握程度。

#### 不适用

- 只想学习一篇明确论文或文章：使用 `deep-reading-tutor`。
- 只想生成一次性代码库 Wiki：使用 `research-codebase-to-wiki`。
- 主要问题是判断一个新需求是否可行：使用 `requirements-reality-check`。
- 已有明确架构基线，需要检查实现是否偏离：使用 `architecture-drift-audit`。

#### 必要输入

- 系统范围或仓库路径。
- 用户当前角色、近期要完成的任务和已有理解。
- 可用事实来源：代码、配置、运行证据、架构文档、ADR、问题记录等。

#### 核心流程

1. 定义掌握目的和系统边界，建立事实/声明/未知项台账。
2. 先建立使命、领域和系统上下文，再按问题选择视图。
3. 追踪一至数条代表性端到端路径，把静态结构与运行行为连接起来。
4. 选择真正相关的质量属性场景，检查故障、恢复、状态与可观测性。
5. 通过解释、预测、变更影响题或实操任务检验用户心智模型。
6. 针对暴露出的误解迭代，而不是机械完成固定章节。

#### 最小输出

- 系统掌握地图：使命、上下文、核心领域、关键视图及其联系。
- 证据台账：implemented / partial / planned / inferred / unknown。
- 关键契约、深模块、高风险依赖和运行路径。
- 用户掌握度检查结果、盲点和下一步练习。

#### 成功标准

不是文档篇幅，而是用户能够：

- 用自己的话解释关键机制；
- 指出模型或结论的证据；
- 区分当前实现、计划与推断；
- 对一个合理变化给出初步影响范围和查证路径。

### `requirements-reality-check`

#### 中心对象

一个尚未获得充分证据的需求、功能设想、技术方案或交付承诺。

#### 核心问题

它是否源自真实业务需要；在现有人员、流程、数据、软硬件、接口、预算、时间与运维能力下能否成立；哪些潜在问题应在承诺前暴露？

#### 适用

- 模糊需求澄清、立项前评估、方案评审或投标边界检查。
- 涉及设备、数据、模型、第三方、线下流程或多团队协作的功能。
- 用户担心“技术上能做”却无法部署、验收、维护或产生业务价值。
- 需要形成风险、假设、待验证事项和最低可行承诺。

#### 不适用

- 需求已确认，只需写成规范或实现任务。
- 主要目标是学习当前系统：使用 `software-system-mastery`。
- 主要目标是把已经确认的方案讲给特定受众：使用 `project-narrative-builder`。
- 主要目标是检查实现是否遵守已经接受的意图：使用 `architecture-drift-audit`。

#### 必要输入

- 原始诉求及提出者。
- 业务场景、当前流程、受益者和成功/失败后果。
- 现有技术与组织基础；缺失部分可以作为待调查项。

#### 核心流程

1. 把“解决方案句子”还原为业务/使命、行为者、痛点与期望结果。
2. 描述当前状态、目标状态和差距，统一关键术语。
3. 建立 reality stack：人员流程、数据、软件、硬件、网络、接口、权限、运维、合规、成本与进度。
4. 对正常、峰值、降级、恢复和维护场景逐一演绎。
5. 检查真实性、可行性、可验证性、可操作性、可维护性与责任归属。
6. 形成 go / conditional go / experiment first / no-go 建议，以及承诺边界。

#### 最小输出

- 需求重述与业务证据。
- 当前状态—目标状态—差距。
- 已知事实、关键假设、依赖、未知项和责任人。
- 场景化质量与验收条件。
- 风险链：触发条件、后果、可观测信号、缓解与兜底。
- 决策建议、最小验证实验及“不承诺什么”。

#### 成功标准

决策者能够看见隐藏成本和前置条件，并且不会把未经验证的技术路径、数据来源或组织配合写成确定事实。

### `project-narrative-builder`

#### 中心对象

一个具体受众在一个具体情境中，面对项目事实、主张和期望行动的关系。

#### 核心问题

为了让能够促成变化的人理解、相信、决定或行动，应该选择哪些事实，以什么顺序呈现，如何处理其约束与异议？

#### 适用

- 把同一项目分别讲给管理者、客户、评审者、开发者、合作方或公众。
- 准备汇报、立项说明、架构说明、演示脚本、发布叙事或交接材料。
- 已有大量项目事实，但不知道该删什么、强调什么、如何形成主线。
- 用户明确关心受众、决策、说服或行动，而非单纯润色。

#### 不适用

- 事实本身尚未被研究清楚：先使用 `software-system-mastery` 或 `research-codebase-to-wiki`。
- 需求真实性和可行性尚未确认：先使用 `requirements-reality-check`。
- 只做措辞、语法或视觉样式美化。
- 只学习一篇材料：使用 `deep-reading-tutor`。

#### 必要输入

- 受众及其可采取的行动。
- 沟通目的、情境、时间/篇幅/媒介约束。
- 受众已有认知、利益、主要异议和证据门槛。
- 项目事实及其证据状态。

#### 核心流程

1. 建立 audience-action brief：exigence、可行动受众、期望变化、约束。
2. 明确这是教学、操作、参考、解释、评审还是决策任务。
3. 将事实分为必须知道、用于证明、用于回应异议、可延后和应删除。
4. 建立 narrative spine：现状/张力—关键洞见—方案或结果—证据—代价—行动。
5. 检查每个主张的证据、受众可理解性和诚实的不确定性。
6. 把内容规格移交给文档、幻灯片、网页或演讲制品工具。

#### 最小输出

- Audience-action brief。
- 一句话核心主张与叙事主线。
- 主张—证据—异议—回应矩阵。
- 内容结构、信息优先级和行动闭环。
- 媒介/制品的内容规格，不强制负责最终视觉渲染。

#### 成功标准

受众能够在有限时间内理解“为什么与我有关、凭什么相信、需要做什么”，且没有因简化而混淆事实、计划和推断。

### `architecture-drift-audit`

#### 中心对象

已经接受或至少被明确声明的架构意图，与当前实现和运行事实之间的映射关系。

#### 核心问题

哪些意图仍被兑现、哪些出现偏离或缺失、哪些实现无法映射、哪些旧意图已经失效；下一步应修改实现、更新蓝图还是建立持续约束？

#### 适用

- 架构文档、ADR、模块契约与当前代码可能不一致。
- 大规模改造、多人/多 Agent 开发后需要检查整体一致性。
- 用户担心模块职责、依赖方向、数据所有权、接口或质量属性逐渐侵蚀。
- 希望从一次性审计建立可持续 architecture fitness functions。

#### 不适用

- 没有任何意图基线，只想理解系统：先使用 `software-system-mastery` 重建候选蓝图。
- 只做通用代码质量或 PR diff review。
- 新需求尚未确认：使用 `requirements-reality-check`。
- 只是重新绘制架构图而不比较实现证据。

#### 必要输入

- 意图基线：架构描述、ADR、模块契约、质量属性场景、接口规范或明确的设计声明。
- 实现证据：代码依赖、接口、配置、数据库、部署、运行 trace、测试与指标。
- 审计范围、风险优先级和允许的例外。

#### 核心流程

1. 评估基线权威性、状态、时间和适用范围，区分 accepted / proposed / superseded。
2. 将基线整理为可检查元素、关系、责任、契约和质量约束。
3. 建立实现实体到高层模型的显式映射，并记录无法映射项。
4. 分类 convergence / divergence / absence / stale intent / unresolved。
5. 评估偏离对领域、运行时、数据、部署和质量属性的影响。
6. 为每项发现选择处置：修实现、修蓝图、补/替代 ADR、限时例外或 fitness function。

#### 最小输出

- 意图基线及权威性说明。
- 高层蓝图、模块职责、依赖方向和契约表。
- 映射规则与覆盖率/未知项。
- 漂移发现：类别、证据、风险、置信度、影响范围和建议。
- 决策待办与可自动化约束候选。

#### 成功标准

原始意图和当前现实都保持可见；团队可以区分“实现违规”和“蓝图过期”，并知道如何防止关键属性继续无声退化。

## 与现有 skills 的边界

| 用户任务 | 首选 skill | 为什么不是其他 skill | 允许的移交 |
| --- | --- | --- | --- |
| 深入学习一篇 DDD 文章或架构论文，并接受逐题抽问 | `deep-reading-tutor` | 中心对象是一份学习材料，不是现实软件系统 | 学到的概念可作为 `software-system-mastery` 或 drift audit 的分析词汇 |
| 把陌生代码库整理成带文件锚点的说明 Wiki | `research-codebase-to-wiki` | 交付物是静态事实型 Wiki，不要求验证用户是否形成可迁移的心智模型 | Wiki 可成为 mastery 的初始证据包 |
| 接手系统并希望以后能独立开发、解释和判断变化 | `software-system-mastery` | 目标是用户能力与动态心智模型，不是单份材料或静态 Wiki | 可调用 Wiki 研究产物，但必须继续做跨视图推理和掌握度验证 |
| 判断“给设备增加 AI 自动识别”是否是真需求且能否落地 | `requirements-reality-check` | 中心对象是候选需求及真实环境，不是掌握现有系统 | 可请求 mastery 补足现状证据；确认后移交 ADR 或叙事 |
| 把项目讲给投资人、评审专家或内部架构委员会 | `project-narrative-builder` | 核心是受众行动和证据组织，不是重新研究全部事实 | 若事实不足，回退到 Wiki/mastery/requirements；内容确定后移交制品 skill |
| 对照架构蓝图和 ADR 检查代码偏离 | `architecture-drift-audit` | 存在显式“应然—实然”比较，不是一般理解或代码审查 | 基线缺失时先做 mastery；意图本身有争议时回到 requirements/ADR 决策 |

### 与 `deep-reading-tutor` 的硬边界

- `deep-reading-tutor` 的会话状态围绕**来源材料的覆盖度和用户盲点**。
- `software-system-mastery` 的状态围绕**系统模型的证据、跨视图连接和用户能否预测现实系统行为**。
- 前者可以把论文中的架构讲透，却不负责证明仓库是否实现了论文；后者必须把结论锚定到系统证据。
- 新 skills 不应复制其“三阶段阅读—抽问—笔记”固定流程；需要抽问时只复用“以暴露盲点为目的”的原则。

### 与 `research-codebase-to-wiki` 的硬边界

- Wiki skill 以**可查阅的解释制品**为完成条件；mastery 以**用户获得可迁移理解**为完成条件。
- Wiki skill 默认从仓库事实出发重建“是什么”；drift audit 必须额外拥有“本应是什么”的权威基线。
- Wiki skill 可以报告 gaps/risks，但不负责判定候选需求的业务真实性，也不负责把内容改造成面向特定受众的决策叙事。
- `software-system-mastery` 不应重复生成完整 Task/Method/Dataset/Metric/Result Wiki；可以引用现成 Wiki，只补足当前掌握目标需要的视图、追问和验证任务。

## 四个新 skills 的两两冲突矩阵

| 组合 | 容易混淆的共同表象 | 决胜问题 | 主 skill / 次 skill 规则 |
| --- | --- | --- | --- |
| mastery × requirements | 都会分析业务、系统边界和技术基础 | 中心是“理解已经存在的系统”，还是“判断尚未确认的改变”？ | 已有系统心智模型为 mastery；候选改变的真实性与可行性为 requirements。requirements 可请求 mastery 提供现状证据。 |
| mastery × narrative | 都会解释系统并选择抽象层 | 接受者是正在建立能力的用户本人，还是需要被推动采取行动的受众？ | 学会推理为 mastery；沟通促成决定/行动为 narrative。 |
| mastery × drift | 都会读取代码、架构与运行证据 | 是否存在可以比较的已声明意图基线？ | 无基线或目标是理解时用 mastery；有基线且要判一致性时用 drift。 |
| requirements × narrative | 都关注利益相关者、异议和表达 | 当前需要先决定“是否应做”，还是已经有可靠结论、需要“让谁据此行动”？ | 真实性与可行性未定时 requirements 优先；结论已稳时 narrative。不得用叙事包装替代验证。 |
| requirements × drift | 都会发现接口、约束和风险问题 | 对象是尚未接受的未来意图，还是已经接受却可能未兑现的意图？ | 未接受的需求/方案用 requirements；accepted intent 对 as-built 用 drift。若审计发现基线上游假设失效，移交 requirements 重新评估。 |
| narrative × drift | 都可能产出蓝图、模块说明和决策材料 | 用户要改变受众认知，还是要证明架构符合性？ | 审计证据由 drift 产生；narrative 只负责按受众组织，不得自行把 unresolved 改成 compliant。 |

## 路由规则：触发与不触发的最短判定

建议每个未来 `SKILL.md` 的 description 和开头都保留以下路由逻辑：

1. **先找中心名词**：已有系统、候选需求、受众行动、还是意图—实现关系。
2. **再找完成条件**：用户掌握、风险前置、沟通促变、还是符合性处置。
3. **最后看制品**：Wiki、报告、图或幻灯片只是结果形态，不能单独决定 skill。

正向触发示例：

- “我要真正接手这个支付系统，帮我建立能用于开发和排障的整体理解。” → `software-system-mastery`
- “客户要求离线环境实时识别，但现场设备和数据都没确认，先帮我把坑找出来。” → `requirements-reality-check`
- “同一个项目我要分别讲给院领导和开发团队，帮我重新组织论证。” → `project-narrative-builder`
- “ADR 规定领域层不能依赖数据库实现，帮我检查现在是否已经侵蚀。” → `architecture-drift-audit`

负向或回退示例：

- “逐段读这篇 DDD 文章并考我。” → `deep-reading-tutor`
- “给这个研究仓库生成带代码引用的 Wiki。” → `research-codebase-to-wiki`
- “把这段话润色得更简洁。” → 不触发 `project-narrative-builder`，除非用户还要求重构受众与行动逻辑。
- “看看代码架构怎么样。” → 信息不足以直接触发 drift；若无明确基线，应先做系统理解或一般设计评审。

## 共同证据纪律

四个 skills 可以共享下面的证据状态词，但不能共享一个笼统工作流：

| 状态 | 含义 |
| --- | --- |
| `implemented` | 在代码、配置、部署或运行证据中可验证 |
| `partial` | 只实现了声明的一部分，或仅在部分路径/环境成立 |
| `planned` | 有明确计划或 proposed decision，但当前实现尚无证据 |
| `declared` | 文档或口头声明存在，但权威性、状态或实现情况未确认 |
| `inferred` | 根据证据作出的分析推断，必须附理由与置信度 |
| `unknown` | 当前证据不足，不应用合理猜测填空 |
| `superseded` | 曾经有效但已被后续决定替代，仍保留历史价值 |

共同规则：

- 本地代码与运行事实优先回答“现在是什么”，ADR 与架构文档优先回答“为何如此/本应是什么”；两类证据不能互相覆盖。
- 外部书籍、框架和标准提供分析问题，不提供当前项目事实。
- 任何图表、总结或叙事都必须保留关键不确定性。
- 不为了输出完整而平均分析所有模块、需求、受众或质量属性；根据核心领域、风险和用户任务分配精力。

## 对后续实现的直接建议

1. 先实现 `software-system-mastery`，但将其描述限定为“帮助用户形成和验证系统级心智模型”，避免出现 `wiki`、`overview generator` 等静态制品导向词。
2. 第二个实现 `requirements-reality-check`。它应拥有最强的前置质疑和场景推演能力，并明确其输出不是 PRD，而是进入规格化之前的现实性判断。
3. 第三个实现 `project-narrative-builder`。它先产出 audience-action brief 和 claim-evidence spine，再与 PPT、文档、网页等制品能力组合。
4. 最后实现 `architecture-drift-audit`，因为它会复用前面形成的系统视图、需求意图和决策证据，但必须维持独立的“显式映射与符合性处置”中心。
5. 每个 skill 都编写正向、负向和相邻 skill 竞争测试；尤其测试用户只说“分析项目”“写架构文档”“评估方案”时是否会先识别中心对象，而不是四个 skills 同时触发。
6. 新 skills 暂时保留在本仓库路径中验证，不把它们自动安装或复制到 Codex 全局 skills 目录。理论基础文档本身也不应被塞入每个 `SKILL.md`；只把执行所需的判断原则写入 skill，长篇依据留在研究目录或按需拆入 references。

## 来源—设计决策追溯表

| 一手来源 | 在本文中的证据角色 | 直接改变的 skill 决策 |
| --- | --- | --- |
| Evans, [DDD Reference](https://www.domainlanguage.com/wp-content/uploads/2016/05/DDD_Reference_2015-03.pdf) | 给出 domain、model、Ubiquitous Language、Bounded Context、Context Map 与 Core Domain 的原始定义和模式摘要 | 四个 skills 先处理语义和上下文边界；不得把代码目录、全局术语表或 DDD 战术类名当作领域模型本身 |
| Domain Language, [DDD Resources](https://www.domainlanguage.com/ddd/) | 说明 DDD 是面向复杂领域的设计决策框架和共同词汇，而非单一架构模板 | 仅在领域复杂度足以影响判断时启用 DDD 深度分析，不强迫所有项目套用完整 DDD |
| Ousterhout, [A Philosophy of Software Design](https://web.stanford.edu/~ouster/cgi-bin/book.php) | 作者对第二版重点的说明，包括一般性深模块与“决定什么重要” | mastery 以解释压缩和重要性排序为目标；不平均铺陈所有文件和功能 |
| Ousterhout, [The Nature of Complexity](https://web.stanford.edu/~ouster/cgi-bin/cs190-winter18/lecture.php?topic=complexity) | 定义 change amplification、cognitive load、unknown unknowns 及依赖/晦涩 | mastery 用三类复杂度检验用户理解；drift 把复杂度上升纳入风险，而不只扫描禁止依赖 |
| Ousterhout, [Managing Complexity](https://web.stanford.edu/~ouster/cgi-bin/cs190-spring15/lecture.php?topic=complexity) | 解释接口、信息隐藏和深模块 | mastery 和 drift 都必须检查模块隐藏的知识与对外契约，而非只列模块名称 |
| ISO, [ISO/IEC/IEEE 42010:2022](https://www.iso.org/standard/74393.html) | 区分 architecture 与 architecture description，并给出 stakeholder/concern/viewpoint/view 框架 | mastery 按关注点选视图；drift 分开“系统事实、意图和意图的历史描述” |
| SEI, [Views and Beyond](https://insights.sei.cmu.edu/library/documenting-software-architectures-views-and-beyond-second-edition/) | 提供面向利益相关者选择、记录并组合架构视图的方法 | 不生成固定大而全架构包；只选择能帮助当前用户完成工作的视图，并补充跨视图信息 |
| Rozanski 与 Woods, [Viewpoints and Perspectives](https://www.viewpoints-and-perspectives.info/home/book/) | 区分结构 viewpoints 与跨结构质量 perspectives | 性能、安全、可用性等作为跨视图分析动态选择，不与功能/部署视图混为一张万能图 |
| Rozanski 与 Woods, [Architectural Perspectives](https://www.viewpoints-and-perspectives.info/home/perspectives/) | 说明质量属性需要在多个结构视图上共同施加活动与策略 | mastery 与 drift 必须跨视图追踪关键质量属性，不能因静态结构合规就结束 |
| SEI, [Reasoning About Software Quality Attributes](https://www.sei.cmu.edu/library/reasoning-about-software-quality-attributes/) | 给出质量属性一般场景及架构策略副作用的推理方式 | requirements 把“高性能/高可用”等形容词改写成环境、刺激、响应和度量；四个 skills 显式处理 trade-off |
| SEI, [Software Architecture in Practice, Fourth Edition](https://www.sei.cmu.edu/library/software-architecture-in-practice-fourth-edition/) | 确认架构与业务环境、技术环境、组织实践和多种质量属性相互影响 | skills 不把架构缩减为技术栈与方框图，并按项目动态选择 architecturally significant concerns |
| ISO, [ISO/IEC/IEEE 29148:2018](https://www.iso.org/standard/72089.html) | 将业务/使命、利益相关者需要、系统/软件需求和管理置于全生命周期过程 | requirements 保留 raw request → need → analyzed requirement → acceptance evidence 链，不从一句诉求直接生成规格 |
| NASA, [Systems Engineering Handbook Fundamentals](https://www.nasa.gov/reference/2-0-fundamentals-of-systems-engineering/) | 把 ConOps、边界、接口、权衡、风险、V&V、成本和进度放在同一全局视角 | requirements 的 reality stack 必须覆盖技术、组织、成本和进度，并同时检查“做对设计”和“设计做对” |
| NASA, [Systems Engineering Handbook PDF](https://www.nasa.gov/wp-content/uploads/2018/09/nasa_systems_engineering_handbook_0.pdf) | 提供系统设计、需求分解、产品实现及生命周期 V&V 的完整过程依据 | requirements 分开确认真实用途与验证规格符合性；mastery 纳入运行、维护、降级和恢复场景 |
| NASA, [Handbook Appendix](https://www.nasa.gov/reference/system-engineering-handbook-appendix/) | 提供好需求、需求确认、验证矩阵和确认计划的检查项 | requirements 为关键需求记录单一陈述、追溯、验证方法、确认情境和责任，不以文字通顺代替可验证性 |
| Bitzer, [The Rhetorical Situation](https://wac.gmu.edu/wp-content/uploads/bitzer.pdf) | 给出 exigence、能够促成变化的 audience 与 constraints | narrative 的首个制品必须是 audience-action brief；职位、年龄或语气偏好不足以定义受众 |
| Procida, [Diátaxis](https://diataxis.fr/) 与 [Start Here](https://diataxis.fr/start-here/) | 区分教程、操作指南、参考与解释所服务的用户需要 | narrative 先判定沟通工作；不得默认生成四件套，也不把学习、查阅和行动混入同一结构 |
| Murphy、Notkin、Sullivan, [Software Reflexion Models](https://www.cs.ubc.ca/~murphy/papers/rm/fse95.html) | 原始方法：高层模型 + 源码映射 → convergence/divergence/absence | drift 没有显式意图和映射就不能宣称发现漂移；发现必须附映射规则和实现证据 |
| Murphy、Notkin、Sullivan, [Extending and Managing Software Reflexion Models](https://www.cs.ubc.ca/sites/default/files/tr/1997/TR-97-15_0.pdf) | 支持迭代改进模型、映射和大系统应用 | drift 从高风险粗粒度映射开始逐步细化，保留 unmapped/unresolved，而不伪造完整覆盖 |
| Nygard, [Documenting Architecture Decisions](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions) | 给出轻量 ADR 的 Context、Decision、Status、Consequences 与 supersede 原则 | drift 保留原始意图并允许修代码、更新蓝图或替代 ADR；requirements 只为已充分分析的显著选择提出 ADR 候选 |
| Brown, [C4 Introduction](https://c4model.com/introduction) 与 [Abstractions](https://c4model.com/abstractions) | 给出可缩放的静态结构层级和图示纪律 | mastery/drift 禁止混杂抽象层，图必须标明责任和关系；C4 不替代领域、动态、数据与质量视图 |
| Ford、Parsons、Kua, [Building Evolutionary Architectures](https://evolutionaryarchitecture.com/precis.html) | 定义受引导、多维、增量演进和 architectural fitness function | drift 为仍有效且可客观测量的关键意图提出持续约束；不把含糊偏好或未接受意图自动变成 CI 门禁 |

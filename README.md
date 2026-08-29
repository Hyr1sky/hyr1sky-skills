# hyr1sky-skills

个人 Codex Skills 仓库，用来集中维护和安装自定义技能。

## 当前技能

| 技能 | 状态 | 说明 |
| --- | --- | --- |
| `deep-reading-tutor` | 已使用 | 对单篇论文、文章或文档进行导航、抽问与定制笔记。 |
| `research-codebase-to-wiki` | 已使用 | 将代码库研究为有证据锚点的解释型 Wiki。 |
| `software-system-mastery` | 孵化中 | 围绕真实任务建立跨领域、运行时、数据、模块、部署和质量属性的系统心智模型。 |
| `requirements-reality-check` | 孵化中 | 在规格与实现前，从业务流程和真实软硬件环境检验需求。 |
| `project-narrative-builder` | 孵化中 | 把既有项目事实转化为面向特定受众与决策的叙事。 |
| `architecture-drift-audit` | 孵化中 | 对照架构意图与实际实现，恢复蓝图并审计有后果的漂移。 |

四个“孵化中”技能目前仅保存在本仓库，不安装到全局 Codex skills 目录。试用时直接在任务中指定对应 `SKILL.md` 的绝对路径；行为稳定后再决定是否常驻安装。

## 目录结构

```text
skills/
  <skill-name>/
    SKILL.md              # 必需，技能入口说明
    agents/               # 可选，agent 配置
    references/           # 可选，长文档或参考资料
    scripts/              # 可选，辅助脚本
    assets/               # 可选，模板或静态资源
scripts/
  install-local.sh        # 本地安装脚本
```

每个 `skills/` 下的子目录都是一个独立 Codex skill。新增技能时优先保持目录精简：只有确实需要时再加入 `references/`、`scripts/` 或 `assets/`。

## 本地安装

安装或更新全部本地技能到 `${CODEX_HOME:-~/.codex}/skills`：

```bash
./scripts/install-local.sh
```

脚本会遍历 `skills/` 下的每个技能目录，并覆盖安装到本地 Codex skills 目录。

## 校验技能

使用 Codex 自带的 skill creator 校验器检查单个技能：

```bash
python3 /Users/hyriskyhe/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/deep-reading-tutor
```

校验其他技能时，把最后的路径替换成对应技能目录即可。

## 维护约定

- `SKILL.md` 应说明技能的触发场景、工作流程和需要读取的补充资源。
- 参考资料放在 `references/`，避免把长文档直接塞进 `SKILL.md`。
- 可复用脚本放在 `scripts/`，生成产物不要提交到仓库，除非它本身是技能资产。
- 修改技能后先运行校验。孵化中的技能先通过绝对路径试用；只有决定常驻后，才执行本地安装脚本。

跨技能的正向、负向和组合路由用例记录在 `tests/skill-routing-cases.md`。

# hyr1sky-skills

个人 Codex Skills 仓库，用来集中维护和安装自定义技能。

## 当前技能

| 技能 | 说明 |
| --- | --- |
| `deep-reading-tutor` | 深度阅读辅导技能，包含 `SKILL.md` 和 OpenAI agent 配置。 |
| `research-codebase-to-wiki` | 代码库研究与 Wiki 生成技能，包含参考资料、模板和辅助脚本。 |

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
- 修改技能后先运行校验，再执行本地安装脚本进行试用。

# Mistery 趋势交易

基于《Mistery趋势交易论》整理的 Codex skill，将原文压缩为可执行的趋势交易与市场分析框架。

## 覆盖内容

- 大势判断与月线、周线、日线三周期共振
- 趋势票与情绪票的分类和选股
- 均线、量价、MACD、RSI、筹码与形态分析
- 买卖点、突破回踩、止损止盈和仓位管理
- 复盘流程、交易纪律、流动性与产业周期

## 安装

Windows PowerShell：

```powershell
$d=if($env:CODEX_HOME){$env:CODEX_HOME}else{Join-Path $env:USERPROFILE '.codex'}; git clone https://github.com/Beney88/mistery-trend-trading.git (Join-Path $d 'skills\mistery-trend-trading')
```

macOS/Linux：

```bash
git clone https://github.com/Beney88/mistery-trend-trading.git "${CODEX_HOME:-$HOME/.codex}/skills/mistery-trend-trading"
```

安装后重启 Codex，调用 `$mistery-trend-trading`。

## 推荐调用方式

请使用 Mistery 趋势交易框架分析这笔交易：先判大势，再看板块和个股结构，最后给出触发条件、失效条件、仓位与退出方案。

## 文件结构

- `SKILL.md`：主规则与调用流程
- `agents/openai.yaml`：Codex 展示和默认提示词
- `references/`：理论总纲、技术分析、风险流程、宏观周期和原文索引
- `scripts/extract_docx_sections.py`：按段落或标题检索原始 DOCX

## 使用边界

本项目表达的是原文作者的交易思想，不代表必胜方法，也不构成投资建议。涉及实时价格、新闻、政策、财报和宏观数据时，应重新核验最新信息；技术指标只能作为辅助证据。

<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6588aabccabec8ef9b85eb92f3e7143d",
  "translation_date": "2025-10-28T20:34:02+00:00",
  "source_file": "Workshop/Session05-AIPoweredAgents.md",
  "language_code": "zh"
}
-->
# 第五节：使用 Foundry Local 快速构建 AI 驱动的代理

## 摘要

利用 Foundry Local 的低延迟、保护隐私的运行时，设计和编排多角色 AI 代理。您将定义代理角色、记忆策略、工具调用模式和执行图。本节介绍了可以通过 Chainlit 或 LangGraph 扩展的脚手架模式。入门项目扩展现有的代理架构示例，添加记忆持久化和评估钩子。

## 学习目标

- **定义角色**：系统提示和能力边界
- **实现记忆**：短期（对话）、长期（向量/文件）、临时记事本
- **搭建工作流**：顺序、分支和并行的代理步骤
- **集成工具**：轻量级函数工具调用模式
- **评估**：基本的追踪 + 基于评分标准的结果评分

## 前置条件

- 完成第 1–4 节
- Python 环境，安装 `foundry-local-sdk`、`openai`，可选安装 `chainlit`
- 本地模型运行（至少 `phi-4-mini`）

### 跨平台环境代码片段

Windows:
```powershell
py -m venv .venv
 .\.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install foundry-local-sdk openai
```

macOS:
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install foundry-local-sdk openai
```

如果从 macOS 运行代理连接到远程 Windows 主机服务：
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```


## 演示流程（30 分钟）

### 1. 定义代理角色和记忆（7 分钟）

创建 `samples/05-agents/agents_core.py`：

```python
#!/usr/bin/env python3
"""Minimal multi-agent scaffolding using Foundry Local (OpenAI-compatible)."""
from openai import OpenAI
from dataclasses import dataclass, field
from typing import List, Dict, Any, Callable
import time, json

client = OpenAI(base_url="http://localhost:5273/v1", api_key="not-needed")

@dataclass
class AgentMessage:
    role: str
    content: str
    meta: Dict[str, Any] = field(default_factory=dict)

@dataclass
class Agent:
    name: str
    system_prompt: str
    tools: Dict[str, Callable] = field(default_factory=dict)
    memory: List[AgentMessage] = field(default_factory=list)

    def remember(self, role: str, content: str, **meta):
        self.memory.append(AgentMessage(role=role, content=content, meta=meta))

    def context(self, window:int=8):
        recent = self.memory[-window:]
        msgs = [ {"role": "system", "content": self.system_prompt}]
        msgs += [ {"role": m.role, "content": m.content} for m in recent ]
        return msgs

    def act(self, user_input: str, model: str = "phi-4-mini", temperature: float=0.4):
        self.remember("user", user_input)
        resp = client.chat.completions.create(
            model=model,
            messages=self.context() + [{"role": "user", "content": user_input}],
            temperature=temperature,
            max_tokens=400
        )
        answer = resp.choices[0].message.content
        self.remember("assistant", answer, model=model)
        return answer

researcher = Agent(
    name="Researcher",
    system_prompt="You gather factual, structured insights concisely."
)
writer = Agent(
    name="Writer",
    system_prompt="You rewrite content for clarity and engagement while preserving facts."
)

def demo():
    q = "Explain why edge inference matters for privacy and latency."
    r = researcher.act(q)
    print("Researcher ->", r[:200], "...\n")
    w = writer.act(f"Rewrite more user-friendly: {r}")
    print("Writer ->", w[:200], "...")

if __name__ == "__main__":
    demo()
```


### 2. CLI 脚手架模式（3 分钟）

```powershell
python samples/05-agents/agents_core.py
```


### 3. 添加工具调用（7 分钟）

扩展 `samples/05-agents/tools.py`：

```python
from datetime import datetime
import math, json

def tool_time(_:str)->str:
    return f"Current UTC time: {datetime.utcnow().isoformat()}"

def tool_estimate_tokens(text:str)->str:
    approx = len(text.split()) * 1.35
    return f"Estimated tokens ~ {int(approx)}"

TOOLS = {
    "get_time": tool_time,
    "estimate_tokens": tool_estimate_tokens
}
```


修改 `agents_core.py` 以允许简单的工具语法：用户输入 `#tool:get_time`，代理在生成之前将工具输出扩展到上下文中。

### 4. 编排工作流（6 分钟）

创建 `samples/05-agents/orchestrator.py`：

```python
from agents_core import researcher, writer, Agent
from tools import TOOLS
from openai import OpenAI

client = OpenAI(base_url="http://localhost:5273/v1", api_key="not-needed")

def inject_tools(agent: Agent, user_input: str) -> str:
    if user_input.startswith('#tool:'):
        name = user_input.split(':',1)[1].strip()
        if name in TOOLS:
            out = TOOLS[name](../../../Workshop/"")
            agent.remember("tool", out, tool=name)
            return f"Tool[{name}] => {out}"
    return None

def pipeline(question: str):
    tool_note = inject_tools(researcher, '#tool:get_time')
    r = researcher.act(question)
    w = writer.act(f"Improve readability:\n{r}\nAdd a friendly summary line.")
    return {"raw": r, "refined": w, "tool": tool_note}

if __name__ == '__main__':
    result = pipeline("List three concrete benefits of local SLM inference for regulated industries.")
    for k,v in result.items():
        print(f"== {k.upper()} ==\n{v}\n")
```


### 5. 入门项目：扩展 `05-agent-architecture`（7 分钟）

添加：
1. 持久化记忆层（例如，追加对话的 JSON 行）
2. 简单的评估标准：事实性/清晰度/风格占位符
3. 可选的 Chainlit 前端（两个标签页：对话和追踪）
4. 可选的 LangGraph 风格状态机（如果添加依赖）用于分支决策

## 验证清单

```powershell
foundry model run phi-4-mini
python samples/05-agents/orchestrator.py
```

期望输出结构化的管道结果，并包含工具注入说明。

## 记忆策略概述

| 层级 | 目的 | 示例 |
|------|------|------|
| 短期 | 对话连续性 | 最近 N 条消息 |
| 情节性 | 会话回忆 | 每个会话的 JSON |
| 语义 | 长期检索 | 摘要的向量存储 |
| 记事本 | 推理步骤 | 内联思维链（私密） |

## 评估钩子（概念）

```python
evaluation = {
  "factuality": None,  # manual or heuristic
  "clarity": None,
  "style": None,
  "latency_sec": generation_time,
  "model": model_used
}
```


## 故障排除

| 问题 | 原因 | 解决方案 |
|------|------|----------|
| 答复重复 | 上下文窗口过大/过小 | 调整记忆窗口参数 |
| 工具未调用 | 语法错误 | 使用 `#tool:tool_name` 格式 |
| 编排速度慢 | 多个冷启动模型 | 预运行预热提示 |

## 参考资料

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- LangGraph（可选概念）：https://github.com/langchain-ai/langgraph
- Chainlit: https://docs.chainlit.io

---

**课程时长**：30 分钟  
**难度**：高级

## 示例场景与工作坊映射

| 工作坊脚本 | 场景 | 目标 | 示例提示 |
|------------|------|------|----------|
| `samples/session05/agents_orchestrator.py` / `notebooks/session05_agents_orchestrator.ipynb` | 知识研究机器人生成适合高管的摘要 | 双代理管道（研究 → 编辑润色），可选使用不同模型 | 解释为什么边缘推理对合规性很重要。 |
| （扩展）`tools.py` 概念 | 添加时间和令牌估算工具 | 展示轻量级工具调用模式 | #tool:get_time |

### 场景叙述
合规文档团队需要快速的内部简报，从本地知识中获取，而无需将草稿发送到云服务。研究代理收集简洁的事实性要点；编辑代理重新编写以适应高管的清晰度需求。可以分配不同的模型别名以优化延迟（快速 SLM）与风格化润色（仅在需要时使用更大的模型）。

### 示例多模型环境
```powershell
cd Workshop/samples
set AGENT_MODEL_PRIMARY=phi-4-mini
set AGENT_MODEL_EDITOR=gpt-oss-20b
python -m session05.agents_orchestrator
```


### 追踪结构（可选）
```json
{
    "step": 1,
    "agent": "Researcher",
    "latency_ms": 412.3,
    "tokens_in": 22,
    "tokens_out": 168,
    "model": "phi-4-mini"
}
```

将每一步保存到 JSONL 文件中，以便后续评分标准评估。

### 可选增强功能

| 主题 | 增强功能 | 好处 | 实现草图 |
|------|----------|------|----------|
| 多模型角色 | 每个代理使用不同模型（`AGENT_MODEL_PRIMARY`，`AGENT_MODEL_EDITOR`） | 专业化与速度 | 选择别名环境变量，使用每个角色别名调用 `chat_once` |
| 结构化追踪 | 每个动作（工具、输入、延迟、令牌）的 JSON 追踪 | 调试与评估 | 将字典追加到列表；结束时写入 `.jsonl` |
| 记忆持久化 | 可重新加载的对话上下文 | 会话连续性 | 将 `Agent.memory` 转储到 `sessions/<ts>.json` |
| 工具注册表 | 动态工具发现 | 可扩展性 | 维护 `TOOLS` 字典并检查名称/描述 |
| 重试与回退 | 稳健的长链 | 减少瞬时故障 | 用 try/except 包裹 `act` 并添加指数回退 |
| 评分标准 | 自动化定性标签 | 跟踪改进 | 二次传递提示模型："评分清晰度 1-5" |
| 向量记忆 | 语义回忆 | 丰富的长期上下文 | 嵌入摘要，检索 top-k 到系统消息中 |
| 流式回复 | 更快的感知响应 | 用户体验改进 | 使用流式传输并刷新部分令牌 |
| 确定性测试 | 回归控制 | 稳定的持续集成 | 使用 `temperature=0`，固定提示种子运行 |
| 并行分支 | 更快的探索 | 吞吐量 | 使用 `concurrent.futures` 处理独立的代理步骤 |

#### 追踪记录示例

```python
trace.append({
    "agent": agent.name,
    "input": prompt,
    "output_tokens": getattr(usage,'completion_tokens',None),
    "latency_ms": round((end-start)*1000,2),
    "tools_used": list(tool_calls)
})
```


#### 简单评估提示

```python
score_prompt = f"Rate clarity (1-5) ONLY as a number for this answer:\n{answer}"
rating, _ = chat_once(PRIMARY_ALIAS, messages=[{"role":"user","content":score_prompt}], max_tokens=4, temperature=0)
```

保存（`answer`，`rating`）对以构建历史质量图表。

---

**免责声明**：  
本文档使用AI翻译服务[Co-op Translator](https://github.com/Azure/co-op-translator)进行翻译。尽管我们努力确保翻译的准确性，但请注意，自动翻译可能包含错误或不准确之处。原始语言的文档应被视为权威来源。对于关键信息，建议使用专业人工翻译。我们对因使用此翻译而产生的任何误解或误读不承担责任。
# 第六节：Foundry Local – 模型作为工具

## 摘要

将模型视为本地 AI 操作层中的可组合工具。本节课展示如何串联多个专用 SLM/LLM 调用，选择性地路由任务，并向应用程序公开统一的 SDK 接口。您将构建一个轻量级模型路由器和任务规划器，将其集成到应用脚本中，并概述向 Azure AI Foundry 扩展以支持生产工作负载的路径。

## 学习目标

- **概念化**模型为具有声明能力的原子工具
- **路由**基于意图/启发式评分的请求
- **串联**跨多步骤任务的输出（分解 → 解决 → 精炼）
- **集成**统一的客户端 API 以供下游应用使用
- **扩展**设计到云端（与 OpenAI 兼容的合同）

## 前置条件

- 完成第 1–5 节
- 缓存多个本地模型（例如，`phi-4-mini`，`deepseek-coder-1.3b`，`qwen2.5-0.5b`）

### 跨平台环境代码片段

Windows PowerShell:
```powershell
py -m venv .venv
 .\.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install foundry-local-sdk openai
```

macOS / Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install foundry-local-sdk openai
```

从 macOS 远程/虚拟机服务访问：
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```


## 演示流程（30 分钟）

### 1. 工具能力声明（5 分钟）

创建 `samples/06-tools/models_catalog.py`：

```python
CATALOG = {
  "phi-4-mini": {
    "capabilities": ["general", "reasoning", "summarize"],
    "priority": 2
  },
  "deepseek-coder-1.3b": {
    "capabilities": ["code", "refactor", "explain_code"],
    "priority": 1
  },
  "qwen2.5-0.5b": {
    "capabilities": ["fast", "classification", "lightweight"],
    "priority": 3
  }
}
```


### 2. 意图检测与路由（8 分钟）

创建 `samples/06-tools/router.py`：

```python
#!/usr/bin/env python3
"""Model-as-tool router using Foundry Local OpenAI-compatible endpoint."""
from openai import OpenAI
from models_catalog import CATALOG
import re

client = OpenAI(base_url="http://localhost:5273/v1", api_key="not-needed")

INTENT_RULES = [
  (re.compile(r"code|function|refactor|bug|optimi", re.I), "code"),
  (re.compile(r"summari|abstract|tl;dr", re.I), "summarize"),
  (re.compile(r"classif|label|category", re.I), "classification"),
]

def detect_intent(prompt: str) -> str:
    for pat, intent in INTENT_RULES:
        if pat.search(prompt):
            return intent
    return "general"

def select_model(intent: str) -> str:
    # Score catalog: capability match first, then priority
    scored = []
    for name, meta in CATALOG.items():
        caps = meta["capabilities"]
        match = intent in caps
        scored.append((name, match, meta["priority"]))
    # Sort: match True first, then lowest priority value
    scored.sort(key=lambda t: (not t[1], t[2]))
    return scored[0][0]

def run(prompt: str):
    intent = detect_intent(prompt)
    model = select_model(intent)
    resp = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=400,
        temperature=0.5
    )
    return {"intent": intent, "model": model, "output": resp.choices[0].message.content}

if __name__ == "__main__":
    tests = [
        "Refactor this Python function for readability",
        "Summarize the importance of local AI governance",
        "Classify this feedback: 'The UI is slow and confusing'"
    ]
    for t in tests:
        r = run(t)
        print(f"Prompt: {t}\nModel: {r['model']} (intent={r['intent']})\nOutput: {r['output'][:160]}...\n")
```


### 3. 多步骤任务串联（7 分钟）

创建 `samples/06-tools/pipeline.py`：

```python
#!/usr/bin/env python3
"""Multi-step pipeline: plan -> solve -> refine using specialized models."""
from openai import OpenAI
from router import detect_intent, select_model

client = OpenAI(base_url="http://localhost:5273/v1", api_key="not-needed")

def chat(model, content, temp=0.4):
    r = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": content}],
        max_tokens=350,
        temperature=temp
    )
    return r.choices[0].message.content

def pipeline(task: str):
    plan_model = select_model("general")
    plan = chat(plan_model, f"Break the task into 3 ordered steps. Task: {task}")
    steps = [s for s in plan.split('\n') if s.strip()][:3]
    outputs = []
    for step in steps:
        intent = detect_intent(step)
        model = select_model(intent)
        out = chat(model, step)
        outputs.append((step, model, out))
    refine_model = select_model("summarize")
    combined = '\n'.join(o[2] for o in outputs)
    refined = chat(refine_model, f"Condense results into a cohesive answer:\n{combined}")
    return {"plan": plan, "steps": outputs, "final": refined}

if __name__ == '__main__':
    result = pipeline("Generate a refactored version of a slow Python loop and summarize performance gains.")
    print("PLAN:\n", result['plan'])
    print("FINAL:\n", result['final'][:400])
```


### 4. 初始项目：改进 `06-models-as-tools`（5 分钟）

增强功能：
- 添加流式令牌支持（渐进式 UI 更新）
- 添加置信评分：词汇重叠或提示规则
- 导出追踪 JSON（意图 → 模型 → 延迟 → 令牌使用）
- 实现缓存重用以支持重复的子步骤

### 5. 向 Azure 扩展路径（5 分钟）

| 层级 | 本地（Foundry） | 云端（Azure AI Foundry） | 转换策略 |
|------|----------------|--------------------------|----------|
| 路由 | 启发式 Python | 持久化微服务 | 容器化并部署 API |
| 模型 | 缓存的 SLMs | 托管部署 | 将本地名称映射到部署 ID |
| 可观测性 | CLI 统计/手动 | 集中日志和指标 | 添加结构化追踪事件 |
| 安全性 | 仅限本地主机 | Azure 认证/网络 | 引入密钥库以管理密钥 |
| 成本 | 设备资源 | 消耗计费 | 添加预算保护措施 |

## 验证检查表

```powershell
foundry model run phi-4-mini
foundry model run deepseek-coder-1.3b
python samples/06-tools/router.py
python samples/06-tools/pipeline.py
```

预期基于意图的模型选择和最终精炼输出。

## 故障排除

| 问题 | 原因 | 解决方法 |
|------|------|----------|
| 所有任务都路由到同一模型 | 规则弱 | 丰富 INTENT_RULES 正则表达式集 |
| 管道在中间步骤失败 | 缺少加载的模型 | 运行 `foundry model run <model>` |
| 输出一致性低 | 没有精炼阶段 | 添加总结/验证步骤 |

## 参考资料

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- Azure AI Foundry 文档: https://learn.microsoft.com/azure/ai-foundry
- 提示质量模式：参见第 2 节

---

**课程时长**：30 分钟  
**难度**：专家级

## 示例场景与工作坊映射

| 工作坊脚本/笔记本 | 场景 | 目标 | 数据集/目录来源 |
|-------------------|------|------|-----------------|
| `samples/session06/models_router.py` / `notebooks/session06_models_router.ipynb` | 开发助手处理混合意图提示（重构、总结、分类） | 启发式意图 → 模型别名路由与令牌使用 | 内联 `CATALOG` + 正则表达式 `RULES` |
| `samples/session06/models_pipeline.py` / `notebooks/session06_models_pipeline.ipynb` | 复杂编码辅助任务的多步骤规划与精炼 | 分解 → 专用执行 → 总结精炼步骤 | 相同的 `CATALOG`；步骤从规划输出中派生 |

### 场景叙述
一个工程生产力工具接收异构任务：代码重构、总结架构笔记、分类反馈。为了最小化延迟和资源使用，一个小型通用模型负责规划和总结，一个专门的代码模型处理重构，一个轻量级分类模型标记反馈。管道脚本展示了串联和精炼；路由脚本隔离了自适应单提示路由。

### 目录快照
```python
CATALOG = {
    "phi-4-mini": {"capabilities": ["general", "summarize"], "priority": 2},
    "deepseek-coder-1.3b": {"capabilities": ["code", "refactor"], "priority": 1},
    "qwen2.5-0.5b": {"capabilities": ["classification", "fast"], "priority": 3}
}
```


### 示例测试提示
```json
[
    "Refactor this Python function for readability",
    "Summarize the importance of small language models",
    "Classify this feedback: The UI is slow but pretty",
    "Generate a refactored version of a slow Python loop and summarize performance gains."
]
```


### 追踪扩展（可选）
为 `models_pipeline.py` 添加每步骤追踪 JSON 行：
```python
trace.append({
    "step": step_idx,
    "intent": intent,
    "alias": alias,
    "latency_ms": round((end-start)*1000,2),
    "tokens": getattr(usage,'total_tokens',None)
})
```


### 升级启发式（想法）
如果规划包含关键词如“优化”、“安全”或步骤长度 > 280 字符 → 仅对该步骤升级到更大的模型（例如，`gpt-oss-20b`）。

### 可选增强功能

| 区域 | 增强功能 | 价值 | 提示 |
|------|----------|------|------|
| 缓存 | 重用管理器和客户端对象 | 降低延迟，减少开销 | 使用 `workshop_utils.get_client` |
| 使用指标 | 捕获令牌和每步骤延迟 | 分析和优化 | 计时每次路由调用；存储在追踪列表中 |
| 自适应路由 | 考虑置信度/成本 | 提高质量-成本平衡 | 添加评分：如果提示 > N 字符或正则表达式匹配领域 → 升级到更大的模型 |
| 动态能力注册表 | 热加载目录 | 无需重启重新部署 | 在运行时加载 `catalog.json`；监控文件时间戳 |
| 回退策略 | 故障情况下的鲁棒性 | 提高可用性 | 尝试主模型 → 异常时回退到别名 |
| 流式管道 | 提前反馈 | 改善用户体验 | 流式处理每个步骤并缓冲最终精炼输入 |
| 向量意图嵌入 | 更细致的路由 | 提高意图准确性 | 嵌入提示，聚类并映射质心 → 能力 |
| 追踪导出 | 可审计链 | 合规性/报告 | 输出 JSON 行：步骤、意图、模型、延迟_ms、令牌 |
| 成本模拟 | 云端前估算 | 预算规划 | 为每个模型分配假设的令牌成本并按任务汇总 |
| 确定性模式 | 可重复性 | 稳定的基准测试 | 环境：`temperature=0`，固定步骤计数 |

#### 追踪结构示例

```python
trace.append({
  "step": idx,
  "intent": intent,
  "alias": alias,
  "latency_ms": round((end-start)*1000,2),
  "tokens": getattr(usage,'total_tokens',None)
})
```


#### 自适应升级草图

```python
if len(prompt) > 280 or 'compliance' in prompt.lower():
    # escalate to larger reasoning model if available
    alias = 'gpt-oss-20b'
```


#### 模型目录热加载

```python
import json, time, os
CATALOG_PATH = 'catalog.json'
last_mtime = 0
def get_catalog():
    global last_mtime, CATALOG
    m = os.path.getmtime(CATALOG_PATH)
    if m != last_mtime:
        CATALOG = json.load(open(CATALOG_PATH))
        last_mtime = m
    return CATALOG
```

---

**免责声明**：  
本文档使用AI翻译服务[Co-op Translator](https://github.com/Azure/co-op-translator)进行翻译。尽管我们努力确保翻译的准确性，但请注意，自动翻译可能包含错误或不准确之处。原始语言的文档应被视为权威来源。对于重要信息，建议使用专业人工翻译。我们不对因使用此翻译而产生的任何误解或误读承担责任。
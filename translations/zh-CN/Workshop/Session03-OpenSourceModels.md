# 第三节：在 Foundry Local 中使用开源模型

## 摘要

了解如何将 Hugging Face 和其他开源模型引入 Foundry Local。学习模型选择策略、社区贡献工作流程、性能比较方法，以及如何通过自定义模型注册扩展 Foundry。本节内容与每周的“模型星期一”探索主题相关，帮助您在扩展到 Azure 之前，在本地评估和运营开源模型。

## 学习目标

完成本节后，您将能够：

- **发现与评估**：通过质量与资源权衡，识别候选模型（mistral、gemma、qwen、deepseek）。
- **加载与运行**：使用 Foundry Local CLI 下载、缓存并启动社区模型。
- **基准测试**：应用一致的延迟 + 令牌吞吐量 + 质量评估方法。
- **扩展**：按照与 SDK 兼容的模式注册或调整自定义模型包装器。
- **比较**：为 SLM 与中型 LLM 的选择决策生成结构化比较。

## 前置条件

- 已完成第一节和第二节
- 安装了 `foundry-local-sdk` 的 Python 环境
- 至少有 15GB 的磁盘空间用于多个模型缓存

### 跨平台环境快速启动

Windows PowerShell:
```powershell
py -m venv .venv
 .\.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install foundry-local-sdk openai numpy
```

macOS / Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install foundry-local-sdk openai numpy
```

在 macOS 上对 Windows 主机服务进行基准测试时，设置：
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```


## 演示流程（30分钟）

### 1. 通过 CLI 加载 Hugging Face 模型（8分钟）

```powershell
# List catalog entries (filter manually if needed)
foundry model list

# Download a set of comparison targets
foundry model download mistral-7b
foundry model download gemma-2-2b
foundry model download qwen2.5-0.5b

# Verify cache
foundry cache list
```


### 2. 运行与快速探测（5分钟）

```powershell
foundry model run qwen2.5-0.5b
foundry model run qwen2.5-0.5b --prompt "List three benefits of local inference."

foundry model run mistral-7b
foundry model run mistral-7b --prompt "Explain retrieval augmented generation in one paragraph."
```


### 3. 基准测试脚本（8分钟）

创建 `samples/03-oss-models/benchmark_models.py`：

```python
#!/usr/bin/env python3
"""Lightweight benchmarking for open-source models in Foundry Local.
Metrics: first token latency, total latency, tokens/sec (approx via usage), model size indicator.
Reference SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
"""

import time, statistics, json
from openai import OpenAI

MODELS = [
    "qwen2.5-0.5b",
    "gemma-2-2b",
    "mistral-7b",
]

PROMPT = "Explain the principle of retrieval augmented generation in 2 sentences."
ROUNDS = 3

client = OpenAI(base_url="http://localhost:5273/v1", api_key="not-needed")

def run_round(model: str):
    start = time.time()
    resp = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": PROMPT}],
        max_tokens=150,
        temperature=0.2,
        stream=False
    )
    end = time.time()
    usage = getattr(resp, "usage", None)
    total_tokens = usage.total_tokens if usage else None
    return {
        "latency_sec": end - start,
        "total_tokens": total_tokens,
        "tokens_per_sec": (total_tokens / (end - start)) if (total_tokens and (end-start) > 0) else None,
        "sample_response": resp.choices[0].message.content[:160].replace("\n", " ")
    }

def benchmark_model(model: str):
    results = [run_round(model) for _ in range(ROUNDS)]
    latencies = [r["latency_sec"] for r in results]
    tps = [r["tokens_per_sec"] for r in results if r["tokens_per_sec"]]
    return {
        "model": model,
        "rounds": ROUNDS,
        "latency_avg": statistics.mean(latencies),
        "latency_p95": statistics.quantiles(latencies, n=20)[-1] if len(latencies) > 1 else latencies[0],
        "tokens_per_sec_avg": statistics.mean(tps) if tps else None,
        "sample": results[-1]["sample_response"]
    }

def main():
    summary = [benchmark_model(m) for m in MODELS]
    print(json.dumps(summary, indent=2))
    print("\nInterpretation Tips:\n- latency_avg: lower better\n- tokens_per_sec_avg: higher better\n- Compare quality manually on sample outputs.")

if __name__ == "__main__":
    main()
```

运行：

```powershell
python samples/03-oss-models/benchmark_models.py
```


### 4. 比较性能（5分钟）

讨论权衡：加载时间、内存占用（观察任务管理器 / `nvidia-smi` / 操作系统资源监视器）、输出质量与速度。使用 Python 基准测试脚本（第三节）进行延迟和吞吐量测试；启用 GPU 加速后重复测试。

### 5. 初始项目（4分钟）

创建一个模型比较报告生成器（扩展基准测试脚本，支持导出为 Markdown）。

## 初始项目：扩展 `03-huggingface-models`

通过以下方式增强现有示例：

1. 添加基准测试聚合 + CSV/Markdown 输出。
2. 实现简单的定性评分（提示对 + 手动注释存根文件）。
3. 引入 JSON 配置文件（`models.json`），支持可插拔的模型列表和提示集。

## 验证清单

```powershell
foundry cache list
foundry model run qwen2.5-0.5b
curl http://localhost:5273/v1/models
```

所有目标模型应出现并响应探测聊天请求。

## 示例场景与工作坊映射

| 工作坊脚本 | 场景 | 目标 | 提示 / 数据集来源 |
|------------|------|------|-------------------|
| `samples/session03/benchmark_oss_models.py` / `notebooks/session03_benchmark_oss_models.ipynb` | 边缘平台团队选择嵌入式摘要器的默认 SLM | 生成候选模型的延迟 + p95 + 每秒令牌数比较 | 内联 `PROMPT` 变量 + 环境 `BENCH_MODELS` 列表 |

### 场景叙述

产品工程团队需要为离线会议记录功能选择一个默认的轻量级摘要模型。他们在固定的提示集上运行受控的确定性基准测试（temperature=0），并收集启用和未启用 GPU 加速时的延迟和吞吐量指标。

### 示例提示集 JSON（可扩展）

```json
[
    "Explain the principle of retrieval augmented generation in 2 sentences.",
    "List 3 privacy benefits of local inference.",
    "Summarize why model size impacts latency on consumer hardware.",
    "Provide two scenarios where an SLM is preferable to an LLM."
]
```

对每个模型循环每个提示，捕获每个提示的延迟以推导分布指标并检测异常值。

## 模型选择框架

| 维度 | 指标 | 重要性 |
|------|------|--------|
| 延迟 | 平均 / p95 | 用户体验一致性 |
| 吞吐量 | 每秒令牌数 | 批量与流式扩展性 |
| 内存 | 常驻大小 | 设备适配与并发能力 |
| 质量 | 评分提示 | 任务适用性 |
| 占用 | 磁盘缓存 | 分发与更新 |
| 许可证 | 使用许可 | 商业合规性 |

## 使用自定义模型扩展

高级模式（伪代码）：

```python
# pseudo_adapter.py (conceptual)
class CustomModelAdapter:
    def load(self, weights_path: str): ...
    def generate(self, prompt: str, **params) -> str: ...

# Register with local routing (future extensibility point)
```

请参考官方仓库以获取不断更新的适配器接口：
https://github.com/microsoft/Foundry-Local/tree/main/sdk/python

## 故障排除

| 问题 | 原因 | 解决方法 |
|------|------|----------|
| mistral-7b 内存不足 | RAM/GPU 不足 | 停止其他模型；尝试较小的变体 |
| 首次响应缓慢 | 冷启动加载 | 使用周期性轻量提示保持热启动 |
| 下载卡住 | 网络不稳定 | 重试；在非高峰时预取 |

## 参考资料

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- 模型星期一: https://aka.ms/model-mondays
- Hugging Face 模型发现: https://huggingface.co/models

---

**课程时长**：30分钟（+ 可选深入探讨）  
**难度**：中级

### 可选增强功能

| 增强功能 | 优势 | 方法 |
|----------|------|------|
| 流式首令牌延迟 | 测量感知响应速度 | 使用 `BENCH_STREAM=1` 运行基准测试（增强脚本位于 `Workshop/samples/session03`） |
| 确定性模式 | 稳定的回归比较 | `temperature=0`，固定提示集，捕获 JSON 输出并进行版本控制 |
| 质量评分标准 | 增加定性维度 | 维护 `prompts.json`，包含预期方面；手动或通过辅助模型注释评分（1–5） |
| CSV / Markdown 导出 | 可共享报告 | 扩展脚本以生成包含表格和重点内容的 `benchmark_report.md` |
| 模型能力标签 | 有助于后续自动路由 | 维护 `models.json`，包含 `{alias: {capabilities:[], size_mb:..}}` |
| 缓存预热阶段 | 减少冷启动偏差 | 在计时循环前执行一次预热（已实现） |
| 百分位准确性 | 稳健的尾部延迟 | 使用 numpy 百分位（已在重构脚本中实现） |
| 令牌成本估算 | 经济比较 | 估算成本 = （每秒令牌数 * 每次请求的平均令牌数）* 能耗估算 |
| 自动跳过失败的模型 | 批量运行的弹性 | 在每个基准测试中使用 try/except 包裹，并标记状态字段 |

#### 最小 Markdown 导出片段

```python
with open("benchmark_report.md", "w") as f:
        f.write("|Model|Avg Latency|p95|TPS|\n|---|---|---|---|\n")
        for row in summary:
                f.write(f"|{row['alias']}|{row['latency_avg']:.2f}|{row['latency_p95']:.2f}|{(row.get('tokens_per_sec_avg') or 0):.1f}|\n")
```


#### 确定性提示集示例

```json
[
    "Summarize retrieval augmented generation.",
    "List 3 privacy benefits of local inference.",
    "Explain when to choose an SLM over an LLM."
]
```

循环静态列表而非随机提示，以便在不同提交间进行可比的指标测试。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免责声明**：  
本文档使用AI翻译服务[Co-op Translator](https://github.com/Azure/co-op-translator)进行翻译。尽管我们努力确保翻译的准确性，但请注意，自动翻译可能包含错误或不准确之处。原始语言的文档应被视为权威来源。对于重要信息，建议使用专业人工翻译。我们对因使用此翻译而产生的任何误解或误读不承担责任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
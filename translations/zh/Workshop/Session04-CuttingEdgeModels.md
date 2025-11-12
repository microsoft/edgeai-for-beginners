<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "fea4cb0f47a5011f0df128f5635133a5",
  "translation_date": "2025-11-11T21:48:50+00:00",
  "source_file": "Workshop/Session04-CuttingEdgeModels.md",
  "language_code": "zh"
}
-->
# 第四节：探索前沿模型——LLM、SLM及设备端推理

## 摘要

比较大型语言模型（LLM）与小型语言模型（SLM）在本地与云端推理场景中的表现。学习利用ONNX Runtime加速、WebGPU执行以及混合RAG体验的部署模式。包括一个使用本地模型的Chainlit RAG演示以及可选的OpenWebUI探索。您将调整一个WebGPU推理入门项目，并评估Phi与GPT-OSS-20B的能力及成本/性能权衡。

## 学习目标

- **对比** SLM与LLM在延迟、内存和质量方面的表现
- **部署** 使用ONNXRuntime和（支持的情况下）WebGPU的模型
- **运行** 基于浏览器的推理（隐私保护的交互式演示）
- **集成** 一个带有本地SLM后端的Chainlit RAG管道
- **评估** 使用轻量化的质量和成本启发式方法

## 前置条件

- 已完成第一至第三节课程
- 已安装`chainlit`（已包含在Module08的`requirements.txt`中）
- 支持WebGPU的浏览器（Windows 11上的最新Edge/Chrome）
- Foundry Local已运行（`foundry service status`）

### 跨平台注意事项

Windows仍是主要目标环境。对于等待原生二进制文件的macOS开发者：
1. 在Windows 11虚拟机（Parallels / UTM）或远程Windows工作站中运行Foundry Local。
2. 暴露服务（默认端口5273），并在macOS上设置：
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```

3. 使用与之前课程相同的Python虚拟环境步骤。

Chainlit安装（适用于两个平台）：
```bash
pip install chainlit
```


## 演示流程（30分钟）

### 1. 比较Phi（SLM）与GPT-OSS-20B（LLM）（6分钟）

```powershell
foundry model run phi-4-mini
foundry model run gpt-oss-20b

# Quick capability probes (one-shot non-interactive)
foundry model run phi-4-mini   --prompt "Summarize retrieval augmented generation in 2 sentences."
foundry model run gpt-oss-20b --prompt "Summarize retrieval augmented generation in 2 sentences."

# Basic token / latency test (repeat a few times for intuition)
foundry model run phi-4-mini   --prompt "List 5 creative IoT edge AI ideas."
foundry model run gpt-oss-20b --prompt "List 5 creative IoT edge AI ideas."
```

跟踪：响应深度、事实准确性、风格丰富性、延迟。

观察启用GPU与仅使用CPU后的吞吐量变化。

### 3. 浏览器中的WebGPU推理（6分钟）

调整入门项目`04-webgpu-inference`（创建`samples/04-cutting-edge/webgpu_demo.html`）：

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>Foundry Local WebGPU Demo</title>
  <style>body{font-family:system-ui;margin:2rem;max-width:820px;} textarea{width:100%;height:120px;} pre{background:#111;color:#eee;padding:1rem;} .resp{white-space:pre-wrap;margin-top:1rem;border:1px solid #444;padding:1rem;border-radius:6px;}</style>
</head>
<body>
  <h1>WebGPU Inference (Experimental)</h1>
  <p>Demonstration placeholder for a WebGPU-backed transformer (concept). Replace with actual JS runtime once exposed by Foundry Local or associated runtime libs.</p>
  <textarea id="prompt" placeholder="Enter your prompt..."></textarea>
  <button id="run">Generate</button>
  <div id="out" class="resp"></div>
  <script>
    document.getElementById('run').onclick = async () => {
      const p = document.getElementById('prompt').value.trim();
      if(!p) return;
      document.getElementById('out').textContent = 'Running (simulated)...';
      // Placeholder: in a real implementation you'd call into a WASM/WebGPU pipeline or local gateway endpoint.
      const resp = await fetch('http://localhost:5273/v1/chat/completions', {
        method: 'POST', headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          model: 'phi-4-mini',
          messages: [ { role: 'user', content: p } ],
          max_tokens: 200, temperature: 0.5
        })
      }).then(r=>r.json()).catch(e=>({error:e.toString()}));
      if(resp.error){
        document.getElementById('out').textContent = 'Error: '+resp.error;
      } else {
        document.getElementById('out').textContent = resp.choices?.[0]?.message?.content || JSON.stringify(resp,null,2);
      }
    };
  </script>
</body>
</html>
```

在浏览器中打开文件，观察低延迟的本地往返。

### 4. Chainlit RAG聊天应用（7分钟）

最小化的`samples/04-cutting-edge/chainlit_app.py`：

```python
#!/usr/bin/env python3
"""Chainlit RAG demo using Foundry Local SLM as backend."""
import chainlit as cl
from openai import OpenAI

DOCS = [
  "Foundry Local enables local model execution with OpenAI-compatible APIs.",
  "RAG combines retrieval and generation for grounded answers.",
  "SLMs provide efficiency advantages on constrained hardware."  
]

client = OpenAI(base_url="http://localhost:5273/v1", api_key="not-needed")

def build_context(query: str):
    # Naive lexical scoring
    scored = sorted(DOCS, key=lambda d: sum(w in d.lower() for w in query.lower().split()), reverse=True)
    return "\n".join(scored[:2])

@cl.on_message
async def main(message: cl.Message):
    ctx = build_context(message.content)
    resp = client.chat.completions.create(
        model="phi-4-mini",
        messages=[
            {"role": "system", "content": "Answer using ONLY the provided context. If insufficient, say so."},
            {"role": "user", "content": f"Context:\n{ctx}\n\nQuestion: {message.content}"}
        ],
        max_tokens=300,
        temperature=0.3
    )
    await cl.Message(content=resp.choices[0].message.content).send()
```

运行：

```powershell
chainlit run samples/04-cutting-edge/chainlit_app.py -w
```


### 5. 入门项目：调整`04-webgpu-inference`（6分钟）

交付内容：
- 用流式令牌替换占位符获取逻辑（启用后使用`stream=True`端点变体）
- 添加延迟图表（客户端）用于Phi与GPT-OSS-20B切换
- 内嵌RAG上下文（参考文档的文本区域）

## 评估启发式方法

| 类别 | Phi-4-mini | GPT-OSS-20B | 观察 |
|------|------------|-------------|------|
| 延迟（冷启动） | 快速 | 较慢 | SLM启动迅速 |
| 内存 | 低 | 高 | 设备可行性 |
| 上下文遵循 | 良好 | 强 | 较大的模型可能更详细 |
| 成本（本地） | 极低 | 较高（资源） | 能耗/时间权衡 |
| 最佳使用场景 | 边缘应用 | 深度推理 | 可实现混合管道 |

## 环境验证

```powershell
# List catalog (no --running flag; loaded models are those you have previously run)
foundry model list

# For runtime metrics use the Python benchmark script (Session 3) and OS tools (Task Manager / nvidia-smi) instead of 'model stats'
# Example:
#   cd Workshop/samples
#   set BENCH_MODELS=phi-4-mini,gpt-oss-20b
#   python -m session03.benchmark_oss_models
```


## 故障排除

| 症状 | 原因 | 解决措施 |
|------|------|----------|
| 网页获取失败 | CORS或服务中断 | 使用`curl`验证端点；如有需要启用CORS代理 |
| Chainlit空白 | 环境未激活 | 激活虚拟环境并重新安装依赖 |
| 高延迟 | 模型刚加载 | 使用小型提示序列预热 |

## 参考资料

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- Chainlit文档: https://docs.chainlit.io
- RAG评估（Ragas）: https://docs.ragas.io

---

**课程时长**：30分钟  
**难度**：高级

## 示例场景与工作坊映射

| 工作坊成果 | 场景 | 目标 | 数据/提示来源 |
|------------|------|------|---------------|
| `samples/session04/model_compare.py` / `notebooks/session04_model_compare.ipynb` | 评估SLM与LLM用于高管摘要生成的架构团队 | 量化延迟与令牌使用差异 | 单一`COMPARE_PROMPT`环境变量 |
| `chainlit_app.py`（RAG演示） | 内部知识助手原型 | 用最少的词汇检索生成简短答案 | 文件中的内嵌`DOCS`列表 |
| `webgpu_demo.html` | 未来设备端浏览器推理预览 | 展示低延迟本地往返及用户体验叙述 | 仅实时用户提示 |

### 场景叙述

产品团队需要一个高管简报生成器。轻量化SLM（phi-4-mini）起草摘要；较大的LLM（gpt-oss-20b）可能仅用于优化高优先级报告。课程脚本捕获经验性延迟和令牌指标以证明混合设计的合理性，同时Chainlit演示展示了如何通过检索保持小型模型答案的准确性。WebGPU概念页面为浏览器加速成熟时的完全客户端处理提供了愿景路径。

### 最小RAG上下文（Chainlit）

```python
DOCS = [
  "Foundry Local enables local model execution with OpenAI-compatible APIs.",
  "RAG combines retrieval and generation for grounded answers.",
  "SLMs provide efficiency advantages on constrained hardware."
]
```


### 混合起草→优化流程（伪代码）

```python
draft, _ = chat_once('phi-4-mini', messages=[{"role":"user","content":prompt}], max_tokens=280)
if len(draft) < 600:  # heuristic: escalate only for longer briefs or flagged topics
    final = draft
else:
    final, _ = chat_once('gpt-oss-20b', messages=[{"role":"user","content":f"Refine and polish:\n{draft}"}], max_tokens=220)
```

跟踪两个延迟组件以报告混合平均成本。

### 可选增强

| 重点 | 增强 | 原因 | 实现提示 |
|------|------|------|---------|
| 比较指标 | 跟踪令牌使用+首令牌延迟 | 全面性能视图 | 使用增强的基准脚本（第三节）并设置`BENCH_STREAM=1` |
| 混合管道 | SLM起草→LLM优化 | 降低延迟与成本 | 使用phi-4-mini生成，使用gpt-oss-20b优化摘要 |
| 流式UI | Chainlit中更好的用户体验 | 增量反馈 | 一旦本地流式推理暴露，使用`stream=True`；累积块 |
| WebGPU缓存 | 更快的JS初始化 | 减少重新编译开销 | 缓存已编译的着色器工件（未来运行时功能） |
| 确定性QA集 | 公平的模型比较 | 消除变量 | 固定提示列表+评估运行时设置`temperature=0` |
| 输出评分 | 结构化质量视角 | 超越主观评价 | 简单评分标准：连贯性/事实性/简洁性（1–5分） |
| 能耗/资源说明 | 课堂讨论 | 展示权衡 | 使用操作系统监控（任务管理器，`nvidia-smi`）+基准脚本输出 |
| 成本模拟 | 云端前的论证 | 规划扩展 | 将令牌映射到假设的云定价以构建总拥有成本叙述 |
| 延迟分解 | 识别瓶颈 | 定位优化 | 测量提示准备、请求发送、首令牌、完整完成 |
| RAG+LLM回退 | 质量安全网 | 改善复杂查询 | 如果SLM答案长度低于阈值或信心低→升级处理 |

#### 示例混合起草/优化模式

```python
draft, _ = chat_once('phi-4-mini', messages=[{"role":"user","content":task}], max_tokens=300, temperature=0.4)
refine, _ = chat_once('gpt-oss-20b', messages=[{"role":"user","content":f"Improve clarity but keep facts:\n{draft}"}], max_tokens=220, temperature=0.3)
```


#### 延迟分解示意图

```python
import time
t0 = time.time(); # build messages
prep_ms = (time.time()-t0)*1000
t1 = time.time(); text,_ = chat_once(alias, messages=msgs, max_tokens=180)
full_ms = (time.time()-t1)*1000
print({"prep_ms": prep_ms, "full_gen_ms": full_ms})
```

在模型间使用一致的测量框架以确保公平比较。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免责声明**：  
本文档使用AI翻译服务[Co-op Translator](https://github.com/Azure/co-op-translator)进行翻译。尽管我们努力确保翻译的准确性，但请注意，自动翻译可能包含错误或不准确之处。原始语言的文档应被视为权威来源。对于重要信息，建议使用专业人工翻译。我们不对因使用此翻译而产生的任何误解或误读负责。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
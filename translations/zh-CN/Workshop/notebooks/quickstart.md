# 工作坊笔记本 - 快速入门指南

## 目录

- [前置条件](../../../../Workshop/notebooks)
- [初始设置](../../../../Workshop/notebooks)
- [第04节：模型比较](../../../../Workshop/notebooks)
- [第05节：多代理协调器](../../../../Workshop/notebooks)
- [第06节：基于意图的模型路由](../../../../Workshop/notebooks)
- [环境变量](../../../../Workshop/notebooks)
- [常用命令](../../../../Workshop/notebooks)

---

## 前置条件

### 1. 安装 Foundry Local

**Windows:**
```bash
winget install Microsoft.FoundryLocal
```

**macOS:**
```bash
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**验证安装:**
```bash
foundry --version
```


### 2. 安装 Python 依赖项

```bash
cd Workshop
pip install -r requirements.txt
```

或者单独安装：
```bash
pip install foundry-local-sdk openai numpy requests
```


---

## 初始设置

### 启动 Foundry Local 服务

**运行任何笔记本之前必须启动：**

```bash
# Start the service
foundry service start

# Verify it's running
foundry service status
```

预期输出：
```
✅ Service started successfully
Endpoint: http://localhost:59959
```


### 下载并加载模型

笔记本默认使用以下模型：

```bash
# Download models (first time only - may take several minutes)
foundry model download phi-4-mini
foundry model download qwen2.5-3b
foundry model download phi-3.5-mini
foundry model download qwen2.5-0.5b

# Load models into memory
foundry model run phi-4-mini
foundry model run qwen2.5-3b
foundry model run phi-3.5-mini
```


### 验证设置

```bash
# List loaded models
foundry model ls

# Check service health
curl http://localhost:59959/v1/models
```


---

## 第04节：模型比较

### 目的
比较小型语言模型（SLM）和大型语言模型（LLM）的性能。

### 快速设置

```bash
# Start service (if not already running)
foundry service start

# Load required models
foundry model run phi-4-mini
foundry model run qwen2.5-3b
```


### 运行笔记本

1. **打开** `session04_model_compare.ipynb`（在 VS Code 或 Jupyter 中）
2. **重启内核**（内核 → 重启内核）
3. **按顺序运行所有单元格**

### 关键配置

**默认模型：**
- **SLM:** `phi-4-mini`（约4GB RAM，速度更快）
- **LLM:** `qwen2.5-3b`（约3GB RAM，内存优化）

**环境变量（可选）：**
```python
import os
os.environ['SLM_ALIAS'] = 'phi-4-mini'
os.environ['LLM_ALIAS'] = 'qwen2.5-3b'
os.environ['FOUNDRY_LOCAL_ENDPOINT'] = 'http://localhost:59959/v1'
```


### 预期输出

```
================================================================================
COMPARISON SUMMARY
================================================================================
Alias                Latency(s)      Tokens     Route               
--------------------------------------------------------------------------------
phi-4-mini           1.234           150        chat.completions    
qwen2.5-3b           2.456           180        chat.completions    
================================================================================

💡 SLM is 1.99x faster than LLM for this prompt
```


### 自定义

**使用不同模型：**
```python
os.environ['SLM_ALIAS'] = 'phi-3.5-mini'
os.environ['LLM_ALIAS'] = 'qwen2.5-1.5b'
```

**自定义提示：**
```python
os.environ['COMPARE_PROMPT'] = 'Explain quantum computing in simple terms'
```


### 验证清单

- [ ] 单元格12显示正确的模型（phi-4-mini, qwen2.5-3b）
- [ ] 单元格12显示正确的端点（端口59959）
- [ ] 单元格16诊断通过（✅ 服务正在运行）
- [ ] 单元格20预检通过（两个模型正常）
- [ ] 单元格22比较完成并显示延迟值
- [ ] 单元格24验证显示 🎉 所有检查通过！

### 时间估计
- **首次运行：** 5-10分钟（包括模型下载）
- **后续运行：** 1-2分钟

---

## 第05节：多代理协调器

### 目的
使用 Foundry Local SDK 展示多代理协作，代理共同工作以生成优化输出。

### 快速设置

```bash
# Start service
foundry service start

# Load models
foundry model run phi-4-mini  # Primary model
foundry model run qwen2.5-7b  # Optional: higher quality editor
```


### 运行笔记本

1. **打开** `session05_agents_orchestrator.ipynb`
2. **重启内核**
3. **按顺序运行所有单元格**

### 关键配置

**默认设置（两个代理使用相同模型）：**
```python
PRIMARY_ALIAS = 'phi-4-mini'
EDITOR_ALIAS = 'phi-4-mini'  # Uses same model
```

**高级设置（不同模型）：**
```python
import os
os.environ['AGENT_MODEL_PRIMARY'] = 'phi-4-mini'     # Fast for research
os.environ['AGENT_MODEL_EDITOR'] = 'qwen2.5-7b'      # High quality for editing
```


### 架构

```
User Question
    ↓
Researcher Agent (phi-4-mini)
  → Gathers bullet points
    ↓
Editor Agent (phi-4-mini or qwen2.5-7b)
  → Refines into executive summary
    ↓
Final Output
```


### 预期输出

```
================================================================================
[Pipeline] Question: Explain why edge AI matters for compliance.
================================================================================

[Stage 1: Research]
Output: • Edge AI processes data locally, reducing transmission...

[Stage 2: Editorial Refinement]
Output: Executive Summary: Edge AI enhances compliance by keeping data...

[FINAL OUTPUT]
Executive Summary: Edge AI enhances compliance by keeping sensitive data 
on-premises and reduces latency through local processing.

[METADATA]
Models used: {'researcher': 'phi-4-mini', 'editor': 'phi-4-mini'}
```


### 扩展

**添加更多代理：**
```python
critic = Agent(
    name='Critic',
    system='Review content for accuracy',
    client=client,
    model_id=model_id
)
```

**批量测试：**
```python
test_questions = [
    "What are benefits of local AI?",
    "How does RAG improve accuracy?",
]

for q in test_questions:
    result = pipeline(q, verbose=False)
    print(result['final'])
```


### 时间估计
- **首次运行：** 3-5分钟
- **后续运行：** 每个问题1-2分钟

---

## 第06节：基于意图的模型路由

### 目的
根据检测到的意图智能地将提示路由到专用模型。

### 快速设置

```bash
# Start service
foundry service start

# Load all routing models (CPU variants recommended)
foundry model run phi-4-mini-cpu
foundry model run qwen2.5-0.5b-cpu
foundry model run phi-3.5-mini-cpu
```

**注意：** 第06节默认使用CPU模型以确保最大兼容性。

### 运行笔记本

1. **打开** `session06_models_router.ipynb`
2. **重启内核**
3. **按顺序运行所有单元格**

### 关键配置

**默认目录（CPU模型）：**
```python
CATALOG = {
    'phi-4-mini-cpu': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','refactor'],'priority':3},
}
```

**替代目录（GPU模型）：**
```python
# Uncomment GPU catalog in Cell #6 if you have sufficient VRAM (8GB+)
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini': {'capabilities':['code','refactor'],'priority':3},
}
```


### 意图检测

路由器使用正则表达式模式检测意图：

| 意图 | 模式示例 | 路由到 |
|------|----------|--------|
| `code` | "重构", "实现函数" | phi-3.5-mini-cpu |
| `classification` | "分类", "对这个进行分类" | qwen2.5-0.5b-cpu |
| `summarize` | "总结", "tl;dr" | phi-4-mini-cpu |
| `general` | 其他所有内容 | phi-4-mini-cpu |

### 预期输出

```
✓ Using CPU-optimized models (default configuration)
  Models: phi-4-mini-cpu, qwen2.5-0.5b-cpu, phi-3.5-mini-cpu

Routing prompts to specialized models...
============================================================

Prompt: Refactor this Python function for readability
  Intent: code           | Model: phi-3.5-mini-cpu
  Output: Here's a refactored version...
  Tokens: 156

Prompt: Categorize this email as urgent or normal
  Intent: classification | Model: qwen2.5-0.5b-cpu
  Output: Category: Normal
  Tokens: 45

✓ Success! All prompts routed correctly.
```


### 自定义

**添加自定义意图：**
```python
import re

# Add to RULES
RULES.append((re.compile('translate|翻译', re.I), 'translation'))

# Add capability to catalog
CATALOG['phi-4-mini-cpu']['capabilities'].append('translation')
```

**启用令牌跟踪：**
```python
import os
os.environ['SHOW_USAGE'] = '1'
```


### 切换到GPU模型

如果您有8GB以上的显存：

1. 在 **单元格#6** 中，注释掉CPU目录
2. 取消注释GPU目录
3. 加载GPU模型：
   ```bash
   foundry model run phi-4-mini
   foundry model run qwen2.5-0.5b
   foundry model run phi-3.5-mini
   ```

4. 重启内核并重新运行笔记本

### 时间估计
- **首次运行：** 5-10分钟（加载模型）
- **后续运行：** 每次测试30-60秒

---

## 环境变量

### 全局配置

在启动 Jupyter/VS Code 之前设置：

**Windows（命令提示符）：**
```cmd
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:59959/v1
set SHOW_USAGE=1
set RETRY_ON_FAIL=1
```

**Windows（PowerShell）：**
```powershell
$env:FOUNDRY_LOCAL_ENDPOINT="http://localhost:59959/v1"
$env:SHOW_USAGE="1"
$env:RETRY_ON_FAIL="1"
```

**macOS/Linux：**
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://localhost:59959/v1
export SHOW_USAGE=1
export RETRY_ON_FAIL=1
```


### 笔记本内配置

在任何笔记本开始时设置：

```python
import os

# Foundry Local configuration
os.environ['FOUNDRY_LOCAL_ENDPOINT'] = 'http://localhost:59959/v1'

# Model selection
os.environ['SLM_ALIAS'] = 'phi-4-mini'
os.environ['LLM_ALIAS'] = 'qwen2.5-3b'

# Agent models
os.environ['AGENT_MODEL_PRIMARY'] = 'phi-4-mini'
os.environ['AGENT_MODEL_EDITOR'] = 'qwen2.5-7b'

# Debugging
os.environ['SHOW_USAGE'] = '1'       # Show token usage
os.environ['RETRY_ON_FAIL'] = '1'    # Enable retries
os.environ['RETRY_BACKOFF'] = '2.0'  # Retry delay
```


---

## 常用命令

### 服务管理

```bash
# Start service
foundry service start

# Check status
foundry service status

# Stop service
foundry service stop

# View logs
foundry service logs
```


### 模型管理

```bash
# List all available models in catalog
foundry model catalog

# List loaded models
foundry model ls

# Download a model
foundry model download phi-4-mini

# Load a model
foundry model run phi-4-mini

# Unload a model
foundry model unload phi-4-mini

# Remove a model
foundry model remove phi-4-mini

# Get model info
foundry model info phi-4-mini
```


### 测试端点

```bash
# Check service health
curl http://localhost:59959/health

# List available models via API
curl http://localhost:59959/v1/models

# Test model completion
curl http://localhost:59959/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "phi-4-mini",
    "messages": [{"role":"user","content":"Hello"}],
    "max_tokens": 50
  }'
```


### 诊断命令

```bash
# Check everything
foundry --version
foundry service status
foundry model ls
foundry device info

# GPU status (NVIDIA)
nvidia-smi

# NPU status (Qualcomm)
foundry device info
```


---

## 最佳实践

### 开始任何笔记本之前

1. **检查服务是否运行：**
   ```bash
   foundry service status
   ```

2. **验证模型是否已加载：**
   ```bash
   foundry model ls
   ```

3. **如果重新运行，重启笔记本内核**

4. **清除所有输出**以确保干净运行

### 资源管理

1. **默认使用CPU模型**以确保兼容性
2. **仅在显存8GB以上时切换到GPU模型**
3. **运行前关闭其他GPU应用程序**
4. **在笔记本会话之间保持服务运行**
5. **使用任务管理器或 nvidia-smi 监控资源使用情况**

### 故障排除

1. **在调试代码之前始终检查服务状态**
2. **如果看到过时配置，重启内核**
3. **在任何更改后重新运行诊断单元格**
4. **检查模型名称是否与加载的模型匹配**
5. **验证端点端口是否与服务状态匹配**

---

## 快速参考：模型别名

### 常用模型

| 别名 | 大小 | 最适合 | RAM/VRAM | 变体 |
|------|------|--------|----------|------|
| `phi-4-mini` | ~4B | 通用聊天、总结 | 4-6GB | `-cpu`, `-cuda-gpu`, `-npu` |
| `phi-3.5-mini` | ~3.5B | 代码生成、重构 | 3-5GB | `-cpu`, `-cuda-gpu`, `-npu` |
| `qwen2.5-3b` | ~3B | 通用任务、高效 | 3-4GB | `-cpu`, `-cuda-gpu` |
| `qwen2.5-1.5b` | ~1.5B | 快速、低资源 | 2-3GB | `-cpu`, `-cuda-gpu` |
| `qwen2.5-0.5b` | ~0.5B | 分类、资源最少 | 1-2GB | `-cpu`, `-cuda-gpu` |

### 变体命名

- **基础名称**（例如，`phi-4-mini`）：自动选择最适合硬件的变体
- **`-cpu`**：CPU优化，适用于所有环境
- **`-cuda-gpu`**：NVIDIA GPU优化，需8GB以上显存
- **`-npu`**：Qualcomm NPU优化，需安装NPU驱动

**推荐：** 使用基础名称（不带后缀），让 Foundry Local 自动选择最佳变体。

---

## 成功指标

当您看到以下内容时，说明准备就绪：

✅ `foundry service status` 显示“运行中”  
✅ `foundry model ls` 显示所需模型  
✅ 服务可在正确的端点访问  
✅ 健康检查返回200 OK  
✅ 笔记本诊断单元格通过  
✅ 输出中无连接错误  

---

## 获取帮助

### 文档
- **主仓库：** https://github.com/microsoft/Foundry-Local
- **Python SDK：** https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **CLI参考：** https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-cli.md
- **故障排除：** 请参阅本目录中的 `troubleshooting.md`

### GitHub问题
- https://github.com/microsoft/Foundry-Local/issues
- https://github.com/microsoft/edgeai-for-beginners/issues

---

**最后更新：** 2025年10月8日  
**版本：** Workshop Notebooks 2.0

---

**免责声明**：  
本文档使用AI翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。尽管我们努力确保翻译的准确性，但请注意，自动翻译可能包含错误或不准确之处。原始语言的文档应被视为权威来源。对于关键信息，建议使用专业人工翻译。我们不对因使用此翻译而产生的任何误解或误读承担责任。
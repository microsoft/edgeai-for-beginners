# 研讨会笔记本 - 快速入门指南

## 目录

- [先决条件](#先决条件)
- [初始设置](#codeblock3-或者单独安装：-codeblock4)
- [第四课：模型比较](#验证设置)
- [第五课：多智能体协调器](#验证检查表)
- [第六课：基于意图的模型路由](#拓展)
- [环境变量](#切换至-gpu-模型)
- [常用命令](#全局配置)

---

## 先决条件

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

**验证安装：**
```bash
foundry --version
```

### 2. 安装 Python 依赖

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

**在运行任何笔记本之前必须执行：**

```bash
# 启动服务
foundry service start

# 验证它是否在运行
foundry service status
```

预期输出：
```
✅ Service started successfully
Endpoint: http://localhost:59959
```

### 下载并加载模型

笔记本默认使用这些模型：

```bash
# 下载模型（仅限首次 - 可能需要几分钟）
foundry model download phi-4-mini
foundry model download qwen2.5-3b
foundry model download phi-3.5-mini
foundry model download qwen2.5-0.5b

# 将模型加载到内存中
foundry model run phi-4-mini
foundry model run qwen2.5-3b
foundry model run phi-3.5-mini
```

### 验证设置

```bash
# 列出已加载的模型
foundry model ls

# 检查服务健康状态
curl http://localhost:59959/v1/models
```

---

## 第四课：模型比较

### 目的
比较小型语言模型（SLM）和大型语言模型（LLM）的性能。

### 快速设置

```bash
# 启动服务（如果尚未运行）
foundry service start

# 加载所需模型
foundry model run phi-4-mini
foundry model run qwen2.5-3b
```

### 运行笔记本

1. <strong>打开</strong> `session04_model_compare.ipynb` 在 VS Code 或 Jupyter 中
2. <strong>重启内核</strong>（Kernel → Restart Kernel）
3. <strong>按顺序运行所有单元格</strong>

### 关键配置

**默认模型：**
- **SLM:** `phi-4-mini` （约4GB内存，更快）
- **LLM:** `qwen2.5-3b` （约3GB内存，内存优化）

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

### 验证检查表

- [ ] 单元格12显示正确模型（phi-4-mini, qwen2.5-3b）
- [ ] 单元格12显示正确端口（端口59959）
- [ ] 单元格16诊断通过（✅ 服务正在运行）
- [ ] 单元格20预检通过（两个模型均正常）
- [ ] 单元格22比较完成并显示延迟数值
- [ ] 单元格24验证显示 🎉 全部检查通过！

### 时间预估
- **首次运行：** 5-10分钟（包含模型下载）
- **后续运行：** 1-2分钟

---

## 第五课：多智能体协调器

### 目的
演示使用 Foundry Local SDK 的多智能体协作—多个智能体协同工作以生成优化输出。

### 快速设置

```bash
# 启动服务
foundry service start

# 加载模型
foundry model run phi-4-mini  # 主要模型
foundry model run qwen2.5-7b  # 可选：更高质量的编辑器
```

### 运行笔记本

1. <strong>打开</strong> `session05_agents_orchestrator.ipynb`
2. <strong>重启内核</strong>
3. <strong>按顺序运行所有单元格</strong>

### 关键配置

**默认设置（两个智能体使用相同模型）：**
```python
PRIMARY_ALIAS = 'phi-4-mini'
EDITOR_ALIAS = 'phi-4-mini'  # 使用相同的模型
```

**高级设置（不同模型）：**
```python
import os
os.environ['AGENT_MODEL_PRIMARY'] = 'phi-4-mini'     # 适合研究
os.environ['AGENT_MODEL_EDITOR'] = 'qwen2.5-7b'      # 适合编辑的高质量
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

### 拓展

**添加更多智能体：**
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

### 时间预估
- **首次运行：** 3-5分钟
- **后续运行：** 每个问题1-2分钟

---

## 第六课：基于意图的模型路由

### 目的
根据检测到的意图智能地将提示路由到专门模型。

### 快速设置

```bash
# 启动服务
foundry service start

# 加载所有路由模型（推荐使用CPU版本）
foundry model run phi-4-mini-cpu
foundry model run qwen2.5-0.5b-cpu
foundry model run phi-3.5-mini-cpu
```

**注意：** 第六课默认使用 CPU 模型以获得最大兼容性。

### 运行笔记本

1. <strong>打开</strong> `session06_models_router.ipynb`
2. <strong>重启内核</strong>
3. <strong>按顺序运行所有单元格</strong>

### 关键配置

**默认目录（CPU 模型）：**
```python
CATALOG = {
    'phi-4-mini-cpu': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','refactor'],'priority':3},
}
```

**备用方案（GPU 模型）：**
```python
# 如果您的显存充足（8GB以上），请取消注释第6单元格中的GPU目录
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini': {'capabilities':['code','refactor'],'priority':3},
}
```

### 意图检测

路由器使用正则表达式检测意图：

| 意图 | 示例匹配 | 路由至 |
|--------|-----------------|-----------|
| `code` | "重构", "实现函数" | phi-3.5-mini-cpu |
| `classification` | "分类", "给它分类" | qwen2.5-0.5b-cpu |
| `summarize` | "总结", "tl;dr" | phi-4-mini-cpu |
| `general` | 其他所有情况 | phi-4-mini-cpu |

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

# 添加到规则
RULES.append((re.compile('translate|翻译', re.I), 'translation'))

# 添加编目功能
CATALOG['phi-4-mini-cpu']['capabilities'].append('translation')
```

**启用令牌跟踪：**
```python
import os
os.environ['SHOW_USAGE'] = '1'
```

### 切换至 GPU 模型

如果你有8GB以上的显存：

1. 在 **单元格#6** 中注释掉 CPU 目录
2. 取消注释 GPU 目录
3. 加载 GPU 模型：
   ```bash
   foundry model run phi-4-mini
   foundry model run qwen2.5-0.5b
   foundry model run phi-3.5-mini
   ```
4. 重启内核并重新运行笔记本

### 时间预估
- **首次运行：** 5-10分钟（模型加载）
- **后续运行：** 每次测试30-60秒

---

## 环境变量

### 全局配置

在启动 Jupyter/VS Code 前设置：

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

在任何笔记本开头设置：

```python
import os

# Foundry 本地配置
os.environ['FOUNDRY_LOCAL_ENDPOINT'] = 'http://localhost:59959/v1'

# 模型选择
os.environ['SLM_ALIAS'] = 'phi-4-mini'
os.environ['LLM_ALIAS'] = 'qwen2.5-3b'

# 代理模型
os.environ['AGENT_MODEL_PRIMARY'] = 'phi-4-mini'
os.environ['AGENT_MODEL_EDITOR'] = 'qwen2.5-7b'

# 调试
os.environ['SHOW_USAGE'] = '1'       # 显示令牌使用情况
os.environ['RETRY_ON_FAIL'] = '1'    # 启用重试
os.environ['RETRY_BACKOFF'] = '2.0'  # 重试延迟
```

---

## 常用命令

### 服务管理

```bash
# 启动服务
foundry service start

# 检查状态
foundry service status

# 停止服务
foundry service stop

# 查看日志
foundry service logs
```

### 模型管理

```bash
# 列出目录中所有可用的模型
foundry model catalog

# 列出已加载的模型
foundry model ls

# 下载一个模型
foundry model download phi-4-mini

# 加载一个模型
foundry model run phi-4-mini

# 卸载一个模型
foundry model unload phi-4-mini

# 删除一个模型
foundry model remove phi-4-mini

# 获取模型信息
foundry model info phi-4-mini
```

### 测试端点

```bash
# 检查服务健康状况
curl http://localhost:59959/health

# 通过API列出可用模型
curl http://localhost:59959/v1/models

# 测试模型完成情况
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
# 检查所有内容
foundry --version
foundry service status
foundry model ls
foundry device info

# GPU 状态（NVIDIA）
nvidia-smi

# NPU 状态（高通）
foundry device info
```

---

## 最佳实践

### 启动任何笔记本前

1. **检查服务是否运行：**
   ```bash
   foundry service status
   ```

2. **验证模型已加载：**
   ```bash
   foundry model ls
   ```

3. **如果重新运行，重启笔记本内核**

4. <strong>清除所有输出</strong> 以获得干净运行

### 资源管理

1. **默认使用 CPU 模型** 以保证兼容性
2. **仅在拥有 8GB+ 显存时切换到 GPU 模型**
3. **运行前关闭其他 GPU 应用**
4. <strong>保持服务运行</strong> 以便多次使用
5. **使用任务管理器 / nvidia-smi 监控资源使用**

### 故障排除

1. <strong>调试代码前先检查服务</strong>
2. <strong>见到过期配置时重启内核</strong>
3. <strong>更改后重新运行诊断单元格</strong>
4. <strong>确认模型名称与已加载匹配</strong>
5. <strong>确认端点端口与服务状态一致</strong>

---

## 快速参考：模型别名

### 常用模型

| 别名 | 大小 | 最适用 | RAM/显存 | 变体 |
|-------|------|----------|----------|----------|
| `phi-4-mini` | ~4B | 通用聊天，摘要 | 4-6GB | `-cpu`, `-cuda-gpu`, `-npu` |
| `phi-3.5-mini` | ~3.5B | 代码生成，重构 | 3-5GB | `-cpu`, `-cuda-gpu`, `-npu` |
| `qwen2.5-3b` | ~3B | 通用任务，高效 | 3-4GB | `-cpu`, `-cuda-gpu` |
| `qwen2.5-1.5b` | ~1.5B | 快速，低资源 | 2-3GB | `-cpu`, `-cuda-gpu` |
| `qwen2.5-0.5b` | ~0.5B | 分类，极少资源 | 1-2GB | `-cpu`, `-cuda-gpu` |

### 变体命名

- <strong>基础名称</strong>（如 `phi-4-mini`）：根据硬件自动选择最佳变体
- **`-cpu`**：CPU 优化，适用于所有环境
- **`-cuda-gpu`**：NVIDIA GPU 优化，要求 8GB+ 显存
- **`-npu`**：高通 NPU 优化，要求安装 NPU 驱动

**推荐：** 使用基础名称（无后缀），让 Foundry Local 自动选择最佳变体。

---

## 成功指标

当你看到以下内容，即表示准备就绪：

✅ `foundry service status` 显示“running”
✅ `foundry model ls` 显示所需模型
✅ 服务可通过正确端点访问
✅ 健康检查返回 200 OK
✅ 笔记本诊断单元格通过
✅ 输出中无连接错误

---

## 获取帮助

### 文档
- <strong>主仓库</strong>: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **CLI 参考**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-cli.md
- <strong>故障排除</strong>: 参见本目录中的 `troubleshooting.md`

### GitHub Issues
- https://github.com/microsoft/Foundry-Local/issues
- https://github.com/microsoft/edgeai-for-beginners/issues

---

**最后更新：** 2025年10月8日
**版本：** 研讨会笔记本 2.0

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免责声明**：
本文件由 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻译完成。尽管我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始语言版文件应视为权威来源。对于重要信息，建议使用专业人工翻译。我们对因使用本翻译而产生的任何误解或误释不承担责任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
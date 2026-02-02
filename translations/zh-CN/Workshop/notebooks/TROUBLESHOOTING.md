# 工作坊笔记本 - 故障排查指南

## 目录

- [常见问题及解决方案](../../../../Workshop/notebooks)
- [第04节特定问题](../../../../Workshop/notebooks)
- [第05节特定问题](../../../../Workshop/notebooks)
- [第06节特定问题](../../../../Workshop/notebooks)
- [硬件相关问题](../../../../Workshop/notebooks)
- [诊断命令](../../../../Workshop/notebooks)
- [获取帮助](../../../../Workshop/notebooks)

---

## 常见问题及解决方案

### 🔴 CUDA内存不足

**错误信息：**
```
CUDA failure 2: out of memory
```
  
**根本原因：** GPU没有足够的显存加载模型。

**解决方案：**

#### 选项1：使用CPU版本（推荐）
```python
# In your notebook, update the CATALOG to use CPU variants
CATALOG = {
    'phi-4-mini-cpu': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','refactor'],'priority':3},
}
```
  
#### 选项2：在GPU上使用较小的模型
```python
# Use only the smallest model
CATALOG = {
    'qwen2.5-0.5b': {'capabilities':['general','code','summarize','classification'],'priority':1},
}
```
  
#### 选项3：清理GPU内存
```bash
# Close other GPU-intensive applications
# Check GPU memory usage
nvidia-smi

# Restart Foundry Local service
foundry service stop
foundry service start
```
  
#### 选项4：增加GPU内存（如果可能）
- 关闭浏览器标签页、视频编辑器或其他使用GPU的应用程序
- 减少Windows视觉效果
- 如果有集成显卡和独立显卡，使用独立显卡

---

### 🔴 APIConnectionError: 连接错误

**错误信息：**
```
APIConnectionError: Connection error
[Retry 1/2] Setup failed for 'phi-4-mini': APIConnectionError: Connection error.
```
  
**根本原因：** Foundry Local服务未运行或无法访问。

**解决方案：**

#### 步骤1：检查服务状态
```bash
foundry service status
```
  
#### 步骤2：如果服务已停止，启动服务
```bash
foundry service start
```
  
#### 步骤3：验证端点
```bash
# Check what port the service is using
foundry service status

# Test with curl (adjust port if different)
curl http://localhost:59959/health
curl http://localhost:55769/health
```
  
#### 步骤4：加载所需模型
```bash
foundry model run phi-4-mini
foundry model run qwen2.5-3b
foundry model run phi-3.5-mini
```
  
#### 步骤5：重启笔记本内核  
在启动服务并加载模型后，重启笔记本内核并重新运行所有单元格。

---

### 🔴 模型未在目录中找到

**错误信息：**
```
ValueError: Model phi-3.5-mini-cpu not found in the catalog.
[ERROR] Model 'phi-4-mini' not found in the catalog
```
  
**根本原因：** 模型未下载或未加载到Foundry Local中。

**解决方案：**

#### 选项1：下载并加载模型
```bash
# List available models
foundry model ls

# Download the model if not present
foundry model download phi-4-mini
foundry model download qwen2.5-3b
foundry model download phi-3.5-mini

# Load the model into memory
foundry model run phi-4-mini
foundry model run qwen2.5-3b
foundry model run phi-3.5-mini
```
  
#### 选项2：使用自动选择模式  
更新您的CATALOG以使用基础模型名称（不带`-cpu`后缀）：

```python
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini': {'capabilities':['code','refactor'],'priority':3},
}
```
  
Foundry Local SDK将根据您的硬件自动选择最佳版本（CPU、GPU或NPU）。

---

### 🔴 HttpResponseError: 500 - 加载模型失败

**错误信息：**
```
HttpResponseError: 500 - Failed loading model
```
  
**根本原因：** 模型文件已损坏或与硬件不兼容。

**解决方案：**

#### 重新下载模型
```bash
# Remove corrupted model
foundry model remove phi-3.5-mini

# Download fresh copy
foundry model download phi-3.5-mini
```
  
#### 使用不同版本
```bash
# Try CPU variant instead
foundry model download phi-3.5-mini-cpu
```
  
---

### 🔴 ImportError: 未找到模块

**错误信息：**
```
ModuleNotFoundError: No module named 'foundry_local'
```
  
**根本原因：** 未安装foundry-local-sdk包。

**解决方案：**

```bash
# Install SDK
pip install foundry-local-sdk

# Verify installation
pip show foundry-local-sdk
python -c "from foundry_local import FoundryLocalManager; print('SDK OK')"
```
  
---

### � 首次请求缓慢

**症状：** 第一次完成请求需要30秒以上，后续请求速度较快。

**根本原因：** 这是正常现象——服务在首次请求时将模型加载到内存中。

**解决方案：**

#### 预加载模型
```bash
# Download and load all models you'll use before running notebooks
foundry model download phi-4-mini
foundry model download qwen2.5-3b
foundry model download phi-3.5-mini

foundry model run phi-4-mini
foundry model run qwen2.5-3b
```
  
#### 保持服务运行
```bash
# Start service manually and leave it running
foundry service start
```
  
---

## 第04节特定问题

### 端口配置错误

**问题：** 笔记本连接到错误的端口（55769 vs 59959 vs 57127）

**解决方案：**

1. 检查Foundry Local使用的端口：
```bash
foundry service status
# Note the port number displayed
```
  
2. 更新笔记本中的单元格10：
```python
ENDPOINT = os.getenv('FOUNDRY_LOCAL_ENDPOINT', 'http://localhost:59959/v1')
# Replace 59959 with your actual port
```
  
3. 重启内核并重新运行单元格6、8、10、12、16、20、22

---

### 模型选择错误

**问题：** 笔记本显示gpt-oss-20b或qwen2.5-7b而不是qwen2.5-3b

**解决方案：**

1. 重启笔记本内核（清除旧变量状态）
2. 重新运行单元格10（设置模型别名）
3. 重新运行单元格12（显示配置）
4. **验证：** 单元格12应显示`LLM Model: qwen2.5-3b`

---

### 诊断单元失败

**问题：** 单元格16显示“❌ Foundry Local服务未找到！”

**解决方案：**

1. 验证服务是否正在运行：
```bash
foundry service status
```
  
2. 手动测试端点：
```bash
curl http://localhost:59959/v1/models
```
  
3. 如果curl工作但笔记本不工作：
   - 重启笔记本内核
   - 按顺序重新运行单元格：6、8、10、12、14、16

4. 如果curl失败：
   - 启动服务：`foundry service start`
   - 加载模型：`foundry model run phi-4-mini` 和 `foundry model run qwen2.5-3b`

---

### 预检失败

**问题：** 单元格20显示连接错误，即使诊断通过

**解决方案：**

1. 检查模型是否已加载：
```bash
foundry model ls
# Should show phi-4-mini and qwen2.5-3b
```
  
2. 如果模型缺失：
```bash
foundry model run phi-4-mini
foundry model run qwen2.5-3b
```
  
3. 在加载模型后重新运行单元格20

---

### 比较失败并显示None值

**问题：** 单元格22完成但显示延迟为None

**解决方案：**

1. 首先检查预检是否通过（单元格20）
2. 重新运行单元格22——模型可能需要在首次请求时预热
3. 验证两个模型是否已加载：`foundry model ls`

---

## 第05节特定问题

### 代理使用错误的模型

**问题：** 代理未使用预期的模型

**解决方案：**

验证配置：
```python
# Check which models are assigned
print(f"Researcher: {researcher.model_id}")
print(f"Editor: {editor.model_id}")
```
  
如果模型不正确，重启内核。

---

### 内存上下文溢出

**问题：** 代理响应质量随着时间下降

**解决方案：** 已自动处理——代理仅保留最近6条消息在内存中。

---

## 第06节特定问题

### CPU与GPU模型混淆

**问题：** 使用默认配置时出现CUDA错误

**解决方案：** 默认配置现在使用CPU模型。如果出现CUDA错误：

1. 验证您正在使用默认的CPU目录：
```python
# Cell should show CPU variants
CATALOG = {
    'phi-4-mini-cpu': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','refactor'],'priority':3},
}
```
  
2. 重启内核并重新运行所有单元格

---

### 意图检测不起作用

**问题：** 提示被路由到错误的模型

**解决方案：**

测试意图检测：
```python
# Run the intent detection test cell
for prompt in test_prompts:
    intent = detect_intent(prompt)
    print(f"{prompt[:50]}... → {intent}")
```
  
如果需要调整模式，请更新RULES。

---

## 硬件相关问题

### NVIDIA GPU

**检查GPU状态：**
```bash
nvidia-smi
```
  
**常见问题：**
- **驱动程序过时：** 更新NVIDIA驱动程序
- **CUDA版本不匹配：** 重新安装Foundry Local
- **GPU内存碎片化：** 重启系统

### Qualcomm NPU

**检查NPU状态：**
```bash
foundry device info
```
  
**常见问题：**
- **未安装NPU驱动程序：** 安装Qualcomm NPU驱动程序
- **NPU版本不可用：** 使用CPU版本
- **Windows版本过旧：** 更新到最新的Windows 11

### 仅支持CPU的系统

**推荐模型：**
```python
CATALOG = {
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','general'],'priority':2},
}
```
  
**性能提示：**
- 使用最小的模型
- 减少max_tokens
- 对首次请求保持耐心

---

## 诊断命令

### 检查所有内容
```bash
# Service status
foundry service status

# List models
foundry model ls

# Device info
foundry device info

# Version info
foundry --version

# Health check
curl http://localhost:55769/health
```
  
### 在Python中
```python
# Check SDK import
try:
    from foundry_local import FoundryLocalManager
    print('✓ SDK imported')
except ImportError as e:
    print(f'✗ SDK import failed: {e}')

# Check service connectivity
from openai import OpenAI

try:
    client = OpenAI(base_url='http://localhost:59959/v1', api_key='test')
    models = client.models.list()
    print(f'✓ Service reachable, {len(list(models.data))} models available')
except Exception as e:
    print(f'✗ Service not reachable: {e}')
```
  
---

## 获取帮助

### 1. 检查日志
```bash
# Windows
foundry service logs

# Or check Windows Event Viewer
# Application Logs -> Microsoft-FoundryLocal
```
  
### 2. GitHub问题
- 搜索现有问题：https://github.com/microsoft/Foundry-Local/issues
- 创建新问题并提供以下信息：
  - 错误信息（完整文本）
  - `foundry service status`的输出
  - `foundry --version`的输出
  - GPU/NPU信息（nvidia-smi等）
  - 重现步骤

### 3. 文档
- **主仓库：** https://github.com/microsoft/Foundry-Local
- **Python SDK：** https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **CLI参考：** https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-cli.md
- **故障排查：** https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-troubleshooting.md

---

## 快速修复检查表

当出现问题时，请按以下顺序尝试：

- [ ] 检查服务是否正在运行：`foundry service status`
- [ ] 重启服务：`foundry service stop && foundry service start`
- [ ] 验证模型是否存在：`foundry model ls | grep phi-4-mini`
- [ ] 加载所需模型：`foundry model run phi-4-mini`
- [ ] 检查GPU内存：`nvidia-smi`（如果使用NVIDIA）
- [ ] 尝试CPU版本：使用`phi-4-mini-cpu`代替`phi-4-mini`
- [ ] 重启笔记本内核
- [ ] 清除笔记本输出并重新运行所有单元格
- [ ] 重新安装SDK：`pip install --upgrade --force-reinstall foundry-local-sdk`
- [ ] 重启系统（最后的手段）

---

## 预防提示

### 最佳实践

1. **始终先检查服务：**
   ```bash
   foundry service status
   ```
  
2. **默认使用CPU版本：**
   ```python
   CATALOG = {
       'phi-4-mini-cpu': {...},
       'qwen2.5-0.5b-cpu': {...},
   }
   ```
  
3. **在运行笔记本之前预加载模型：**
   ```bash
   foundry model run phi-4-mini
   foundry model run qwen2.5-3b
   ```
  
4. **保持服务运行：**
   - 不要不必要地停止/启动服务
   - 在会话之间让服务在后台运行

5. **监控资源：**
   - 在运行之前检查GPU内存
   - 关闭不必要的GPU应用程序
   - 使用任务管理器 / nvidia-smi

6. **定期更新：**
   ```bash
   winget upgrade Microsoft.FoundryLocal
   pip install --upgrade foundry-local-sdk
   ```
  
---

**最后更新日期：** 2025年10月8日

---

**免责声明**：  
本文档使用AI翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。尽管我们努力确保翻译的准确性，但请注意，自动翻译可能包含错误或不准确之处。原始语言的文档应被视为权威来源。对于关键信息，建议使用专业人工翻译。我们对因使用此翻译而产生的任何误解或误读不承担责任。
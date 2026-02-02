# 工作坊筆記本 - 故障排除指南

## 目錄

- [常見問題及解決方法](../../../../Workshop/notebooks)
- [第 04 節特定問題](../../../../Workshop/notebooks)
- [第 05 節特定問題](../../../../Workshop/notebooks)
- [第 06 節特定問題](../../../../Workshop/notebooks)
- [硬件相關問題](../../../../Workshop/notebooks)
- [診斷指令](../../../../Workshop/notebooks)
- [尋求幫助](../../../../Workshop/notebooks)

---

## 常見問題及解決方法

### 🔴 CUDA 記憶體不足

**錯誤訊息：**
```
CUDA failure 2: out of memory
```
  
**根本原因：** GPU 的 VRAM 不足以載入模型。

**解決方法：**

#### 方法 1：使用 CPU 版本（推薦）
```python
# In your notebook, update the CATALOG to use CPU variants
CATALOG = {
    'phi-4-mini-cpu': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','refactor'],'priority':3},
}
```
  
#### 方法 2：在 GPU 上使用較小的模型
```python
# Use only the smallest model
CATALOG = {
    'qwen2.5-0.5b': {'capabilities':['general','code','summarize','classification'],'priority':1},
}
```
  
#### 方法 3：清理 GPU 記憶體
```bash
# Close other GPU-intensive applications
# Check GPU memory usage
nvidia-smi

# Restart Foundry Local service
foundry service stop
foundry service start
```
  
#### 方法 4：增加 GPU 記憶體（如果可能）
- 關閉瀏覽器標籤頁、視頻編輯器或其他使用 GPU 的應用程式
- 減少 Windows 視覺效果
- 如果有集成 GPU 和獨立 GPU，請使用獨立 GPU

---

### 🔴 APIConnectionError：連接錯誤

**錯誤訊息：**
```
APIConnectionError: Connection error
[Retry 1/2] Setup failed for 'phi-4-mini': APIConnectionError: Connection error.
```
  
**根本原因：** Foundry Local 服務未運行或無法訪問。

**解決方法：**

#### 步驟 1：檢查服務狀態
```bash
foundry service status
```
  
#### 步驟 2：如果服務停止，啟動服務
```bash
foundry service start
```
  
#### 步驟 3：驗證端點
```bash
# Check what port the service is using
foundry service status

# Test with curl (adjust port if different)
curl http://localhost:59959/health
curl http://localhost:55769/health
```
  
#### 步驟 4：載入所需模型
```bash
foundry model run phi-4-mini
foundry model run qwen2.5-3b
foundry model run phi-3.5-mini
```
  
#### 步驟 5：重啟筆記本內核
在啟動服務並載入模型後，重啟筆記本內核並重新執行所有單元格。

---

### 🔴 模型未在目錄中找到

**錯誤訊息：**
```
ValueError: Model phi-3.5-mini-cpu not found in the catalog.
[ERROR] Model 'phi-4-mini' not found in the catalog
```
  
**根本原因：** 模型未下載或未載入到 Foundry Local。

**解決方法：**

#### 方法 1：下載並載入模型
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
  
#### 方法 2：使用自動選擇模式
更新您的 CATALOG 以使用基礎模型名稱（不帶 `-cpu` 後綴）：

```python
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini': {'capabilities':['code','refactor'],'priority':3},
}
```
  
Foundry Local SDK 將自動為您的硬件選擇最佳版本（CPU、GPU 或 NPU）。

---

### 🔴 HttpResponseError：500 - 模型載入失敗

**錯誤訊息：**
```
HttpResponseError: 500 - Failed loading model
```
  
**根本原因：** 模型文件已損壞或與硬件不兼容。

**解決方法：**

#### 重新下載模型
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

### 🔴 ImportError：未找到模組

**錯誤訊息：**
```
ModuleNotFoundError: No module named 'foundry_local'
```
  
**根本原因：** 未安裝 foundry-local-sdk 套件。

**解決方法：**

```bash
# Install SDK
pip install foundry-local-sdk

# Verify installation
pip show foundry-local-sdk
python -c "from foundry_local import FoundryLocalManager; print('SDK OK')"
```
  
---

### � 首次請求速度慢

**症狀：** 首次完成請求需要 30 秒以上，後續請求速度較快。

**根本原因：** 這是正常現象——服務在首次請求時將模型載入記憶體。

**解決方法：**

#### 預載模型
```bash
# Download and load all models you'll use before running notebooks
foundry model download phi-4-mini
foundry model download qwen2.5-3b
foundry model download phi-3.5-mini

foundry model run phi-4-mini
foundry model run qwen2.5-3b
```
  
#### 保持服務運行
```bash
# Start service manually and leave it running
foundry service start
```
  
---

## 第 04 節特定問題

### 錯誤的端口配置

**問題：** 筆記本連接到錯誤的端口（55769 vs 59959 vs 57127）

**解決方法：**

1. 檢查 Foundry Local 使用的端口：
```bash
foundry service status
# Note the port number displayed
```
  
2. 更新筆記本中的第 10 單元格：
```python
ENDPOINT = os.getenv('FOUNDRY_LOCAL_ENDPOINT', 'http://localhost:59959/v1')
# Replace 59959 with your actual port
```
  
3. 重啟內核並重新執行第 6、8、10、12、16、20、22 單元格

---

### 錯誤的模型選擇

**問題：** 筆記本顯示 gpt-oss-20b 或 qwen2.5-7b，而非 qwen2.5-3b

**解決方法：**

1. 重啟筆記本內核（清除舊的變數狀態）
2. 重新執行第 10 單元格（設置模型別名）
3. 重新執行第 12 單元格（顯示配置）
4. **驗證：** 第 12 單元格應顯示 `LLM Model: qwen2.5-3b`

---

### 診斷單元格失敗

**問題：** 第 16 單元格顯示 "❌ Foundry Local service not found!"

**解決方法：**

1. 驗證服務是否正在運行：
```bash
foundry service status
```
  
2. 手動測試端點：
```bash
curl http://localhost:59959/v1/models
```
  
3. 如果 curl 可用但筆記本不可用：
   - 重啟筆記本內核
   - 按順序重新執行單元格：6、8、10、12、14、16

4. 如果 curl 失敗：
   - 啟動服務：`foundry service start`
   - 載入模型：`foundry model run phi-4-mini` 和 `foundry model run qwen2.5-3b`

---

### 預檢失敗

**問題：** 第 20 單元格顯示連接錯誤，即使診斷通過

**解決方法：**

1. 檢查模型是否已載入：
```bash
foundry model ls
# Should show phi-4-mini and qwen2.5-3b
```
  
2. 如果模型缺失：
```bash
foundry model run phi-4-mini
foundry model run qwen2.5-3b
```
  
3. 在模型載入後重新執行第 20 單元格

---

### 比較失敗並顯示 None 值

**問題：** 第 22 單元格完成但顯示延遲為 None

**解決方法：**

1. 首先檢查預檢是否通過（第 20 單元格）
2. 重新執行第 22 單元格——模型可能需要在首次請求時進行預熱
3. 驗證兩個模型是否已載入：`foundry model ls`

---

## 第 05 節特定問題

### Agent 使用錯誤的模型

**問題：** Agent 未使用預期的模型

**解決方法：**

驗證配置：
```python
# Check which models are assigned
print(f"Researcher: {researcher.model_id}")
print(f"Editor: {editor.model_id}")
```
  
如果模型不正確，請重啟內核。

---

### 記憶上下文溢出

**問題：** Agent 的回應隨時間推移而下降

**解決方法：** 已自動處理——Agent 只保留最近的 6 條消息在記憶中。

---

## 第 06 節特定問題

### CPU 與 GPU 模型混淆

**問題：** 使用默認配置時出現 CUDA 錯誤

**解決方法：** 默認配置現在使用 CPU 模型。如果您看到 CUDA 錯誤：

1. 驗證您正在使用默認的 CPU 目錄：
```python
# Cell should show CPU variants
CATALOG = {
    'phi-4-mini-cpu': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','refactor'],'priority':3},
}
```
  
2. 重啟內核並重新執行所有單元格

---

### 意圖檢測無效

**問題：** 提示被路由到錯誤的模型

**解決方法：**

測試意圖檢測：
```python
# Run the intent detection test cell
for prompt in test_prompts:
    intent = detect_intent(prompt)
    print(f"{prompt[:50]}... → {intent}")
```
  
如果需要調整模式，請更新 RULES。

---

## 硬件相關問題

### NVIDIA GPU

**檢查 GPU 狀態：**
```bash
nvidia-smi
```
  
**常見問題：**
- **驅動過時：** 更新 NVIDIA 驅動
- **CUDA 版本不匹配：** 重新安裝 Foundry Local
- **GPU 記憶體碎片化：** 重啟系統

### Qualcomm NPU

**檢查 NPU 狀態：**
```bash
foundry device info
```
  
**常見問題：**
- **未安裝 NPU 驅動：** 安裝 Qualcomm NPU 驅動
- **NPU 版本不可用：** 使用 CPU 版本
- **Windows 版本過舊：** 更新至最新的 Windows 11

### 僅使用 CPU 的系統

**推薦模型：**
```python
CATALOG = {
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','general'],'priority':2},
}
```
  
**性能提示：**
- 使用最小的模型
- 減少 max_tokens
- 對首次請求保持耐心

---

## 診斷指令

### 檢查所有內容
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
  
### 在 Python 中
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

## 尋求幫助

### 1. 檢查日誌
```bash
# Windows
foundry service logs

# Or check Windows Event Viewer
# Application Logs -> Microsoft-FoundryLocal
```
  
### 2. GitHub 問題
- 搜索現有問題：https://github.com/microsoft/Foundry-Local/issues
- 創建新問題並提供以下信息：
  - 錯誤訊息（完整文本）
  - `foundry service status` 的輸出
  - `foundry --version` 的輸出
  - GPU/NPU 信息（nvidia-smi 等）
  - 重現步驟

### 3. 文件
- **主倉庫：** https://github.com/microsoft/Foundry-Local
- **Python SDK：** https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **CLI 參考：** https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-cli.md
- **故障排除：** https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-troubleshooting.md

---

## 快速修復檢查表

當出現問題時，按以下順序嘗試：

- [ ] 檢查服務是否正在運行：`foundry service status`
- [ ] 重啟服務：`foundry service stop && foundry service start`
- [ ] 驗證模型是否存在：`foundry model ls | grep phi-4-mini`
- [ ] 載入所需模型：`foundry model run phi-4-mini`
- [ ] 檢查 GPU 記憶體：`nvidia-smi`（如果使用 NVIDIA）
- [ ] 嘗試 CPU 版本：使用 `phi-4-mini-cpu` 而非 `phi-4-mini`
- [ ] 重啟筆記本內核
- [ ] 清除筆記本輸出並重新執行所有單元格
- [ ] 重新安裝 SDK：`pip install --upgrade --force-reinstall foundry-local-sdk`
- [ ] 重啟系統（最後手段）

---

## 預防提示

### 最佳實踐

1. **始終先檢查服務：**
   ```bash
   foundry service status
   ```
  
2. **默認使用 CPU 版本：**
   ```python
   CATALOG = {
       'phi-4-mini-cpu': {...},
       'qwen2.5-0.5b-cpu': {...},
   }
   ```
  
3. **在運行筆記本之前預載模型：**
   ```bash
   foundry model run phi-4-mini
   foundry model run qwen2.5-3b
   ```
  
4. **保持服務運行：**
   - 不要不必要地停止/啟動服務
   - 在會話之間讓其在背景中運行

5. **監控資源：**
   - 在運行之前檢查 GPU 記憶體
   - 關閉不必要的 GPU 應用程式
   - 使用任務管理器 / nvidia-smi

6. **定期更新：**
   ```bash
   winget upgrade Microsoft.FoundryLocal
   pip install --upgrade foundry-local-sdk
   ```
  
---

**最後更新日期：** 2025 年 10 月 8 日

---

**免責聲明**：  
本文件已使用人工智能翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於提供準確的翻譯，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要信息，建議使用專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或錯誤解釋概不負責。
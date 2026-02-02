# 工作坊筆記本 - 快速入門指南

## 目錄

- [先決條件](../../../../Workshop/notebooks)
- [初始設定](../../../../Workshop/notebooks)
- [第 04 節：模型比較](../../../../Workshop/notebooks)
- [第 05 節：多代理協作器](../../../../Workshop/notebooks)
- [第 06 節：基於意圖的模型路由](../../../../Workshop/notebooks)
- [環境變數](../../../../Workshop/notebooks)
- [常用指令](../../../../Workshop/notebooks)

---

## 先決條件

### 1. 安裝 Foundry Local

**Windows:**
```bash
winget install Microsoft.FoundryLocal
```

**macOS:**
```bash
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**驗證安裝：**
```bash
foundry --version
```

### 2. 安裝 Python 依賴項

```bash
cd Workshop
pip install -r requirements.txt
```

或單獨安裝：
```bash
pip install foundry-local-sdk openai numpy requests
```

---

## 初始設定

### 啟動 Foundry Local 服務

**在執行任何筆記本之前必須啟動：**

```bash
# Start the service
foundry service start

# Verify it's running
foundry service status
```

預期輸出：
```
✅ Service started successfully
Endpoint: http://localhost:59959
```

### 下載並載入模型

筆記本預設使用以下模型：

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

### 驗證設定

```bash
# List loaded models
foundry model ls

# Check service health
curl http://localhost:59959/v1/models
```

---

## 第 04 節：模型比較

### 目的
比較小型語言模型 (SLM) 和大型語言模型 (LLM) 的性能。

### 快速設定

```bash
# Start service (if not already running)
foundry service start

# Load required models
foundry model run phi-4-mini
foundry model run qwen2.5-3b
```

### 執行筆記本

1. **打開** `session04_model_compare.ipynb`（使用 VS Code 或 Jupyter）
2. **重啟內核**（Kernel → Restart Kernel）
3. **按順序執行所有單元格**

### 關鍵配置

**預設模型：**
- **SLM:** `phi-4-mini`（約 4GB RAM，速度較快）
- **LLM:** `qwen2.5-3b`（約 3GB RAM，記憶體優化）

**環境變數（可選）：**
```python
import os
os.environ['SLM_ALIAS'] = 'phi-4-mini'
os.environ['LLM_ALIAS'] = 'qwen2.5-3b'
os.environ['FOUNDRY_LOCAL_ENDPOINT'] = 'http://localhost:59959/v1'
```

### 預期輸出

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

### 自訂化

**使用不同模型：**
```python
os.environ['SLM_ALIAS'] = 'phi-3.5-mini'
os.environ['LLM_ALIAS'] = 'qwen2.5-1.5b'
```

**自訂提示：**
```python
os.environ['COMPARE_PROMPT'] = 'Explain quantum computing in simple terms'
```

### 驗證清單

- [ ] 第 12 單元格顯示正確模型（phi-4-mini, qwen2.5-3b）
- [ ] 第 12 單元格顯示正確端點（埠 59959）
- [ ] 第 16 單元格診斷通過（✅ 服務正在運行）
- [ ] 第 20 單元格預檢通過（兩個模型均正常）
- [ ] 第 22 單元格比較完成並顯示延遲值
- [ ] 第 24 單元格驗證顯示 🎉 所有檢查通過！

### 時間估算
- **首次運行：** 5-10 分鐘（包括模型下載）
- **後續運行：** 1-2 分鐘

---

## 第 05 節：多代理協作器

### 目的
使用 Foundry Local SDK 展示多代理協作，代理共同合作生成精煉輸出。

### 快速設定

```bash
# Start service
foundry service start

# Load models
foundry model run phi-4-mini  # Primary model
foundry model run qwen2.5-7b  # Optional: higher quality editor
```

### 執行筆記本

1. **打開** `session05_agents_orchestrator.ipynb`
2. **重啟內核**
3. **按順序執行所有單元格**

### 關鍵配置

**預設設定（兩個代理使用相同模型）：**
```python
PRIMARY_ALIAS = 'phi-4-mini'
EDITOR_ALIAS = 'phi-4-mini'  # Uses same model
```

**進階設定（使用不同模型）：**
```python
import os
os.environ['AGENT_MODEL_PRIMARY'] = 'phi-4-mini'     # Fast for research
os.environ['AGENT_MODEL_EDITOR'] = 'qwen2.5-7b'      # High quality for editing
```

### 架構

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

### 預期輸出

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

### 擴展

**添加更多代理：**
```python
critic = Agent(
    name='Critic',
    system='Review content for accuracy',
    client=client,
    model_id=model_id
)
```

**批量測試：**
```python
test_questions = [
    "What are benefits of local AI?",
    "How does RAG improve accuracy?",
]

for q in test_questions:
    result = pipeline(q, verbose=False)
    print(result['final'])
```

### 時間估算
- **首次運行：** 3-5 分鐘
- **後續運行：** 每個問題 1-2 分鐘

---

## 第 06 節：基於意圖的模型路由

### 目的
根據檢測到的意圖智能地將提示路由到專門的模型。

### 快速設定

```bash
# Start service
foundry service start

# Load all routing models (CPU variants recommended)
foundry model run phi-4-mini-cpu
foundry model run qwen2.5-0.5b-cpu
foundry model run phi-3.5-mini-cpu
```

**注意：** 第 06 節預設使用 CPU 模型以最大化兼容性。

### 執行筆記本

1. **打開** `session06_models_router.ipynb`
2. **重啟內核**
3. **按順序執行所有單元格**

### 關鍵配置

**預設目錄（CPU 模型）：**
```python
CATALOG = {
    'phi-4-mini-cpu': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','refactor'],'priority':3},
}
```

**替代選項（GPU 模型）：**
```python
# Uncomment GPU catalog in Cell #6 if you have sufficient VRAM (8GB+)
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini': {'capabilities':['code','refactor'],'priority':3},
}
```

### 意圖檢測

路由器使用正則表達式模式檢測意圖：

| 意圖 | 模式範例 | 路由至 |
|------|----------|--------|
| `code` | "refactor", "implement function" | phi-3.5-mini-cpu |
| `classification` | "categorize", "classify this" | qwen2.5-0.5b-cpu |
| `summarize` | "summarize", "tl;dr" | phi-4-mini-cpu |
| `general` | 其他所有 | phi-4-mini-cpu |

### 預期輸出

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

### 自訂化

**添加自訂意圖：**
```python
import re

# Add to RULES
RULES.append((re.compile('translate|翻译', re.I), 'translation'))

# Add capability to catalog
CATALOG['phi-4-mini-cpu']['capabilities'].append('translation')
```

**啟用令牌追蹤：**
```python
import os
os.environ['SHOW_USAGE'] = '1'
```

### 切換至 GPU 模型

如果您有 8GB+ VRAM：

1. 在 **第 6 單元格**中，註解掉 CPU 目錄
2. 取消註解 GPU 目錄
3. 載入 GPU 模型：
   ```bash
   foundry model run phi-4-mini
   foundry model run qwen2.5-0.5b
   foundry model run phi-3.5-mini
   ```
4. 重啟內核並重新運行筆記本

### 時間估算
- **首次運行：** 5-10 分鐘（模型載入）
- **後續運行：** 每次測試 30-60 秒

---

## 環境變數

### 全域配置

在啟動 Jupyter/VS Code 之前設置：

**Windows（命令提示字元）：**
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

### 筆記本內配置

在任何筆記本開始時設置：

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

## 常用指令

### 服務管理

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

### 測試端點

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

### 診斷指令

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

## 最佳實踐

### 在啟動任何筆記本之前

1. **檢查服務是否正在運行：**
   ```bash
   foundry service status
   ```

2. **驗證模型是否已載入：**
   ```bash
   foundry model ls
   ```

3. **如果重新運行，重啟筆記本內核**

4. **清除所有輸出**以確保乾淨運行

### 資源管理

1. **預設使用 CPU 模型**以確保兼容性
2. **僅在擁有 8GB+ VRAM 時切換至 GPU 模型**
3. **在運行之前關閉其他 GPU 應用程式**
4. **在筆記本會話之間保持服務運行**
5. **使用任務管理器或 nvidia-smi 監控資源使用情況**

### 疑難排解

1. **在調試代碼之前，始終先檢查服務**
2. **如果看到過時配置，重啟內核**
3. **在任何更改後重新運行診斷單元格**
4. **檢查模型名稱是否與載入的匹配**
5. **驗證端點埠是否與服務狀態匹配**

---

## 快速參考：模型別名

### 常用模型

| 別名 | 大小 | 最適用途 | RAM/VRAM | 變體 |
|------|------|----------|----------|------|
| `phi-4-mini` | ~4B | 一般聊天、摘要 | 4-6GB | `-cpu`, `-cuda-gpu`, `-npu` |
| `phi-3.5-mini` | ~3.5B | 代碼生成、重構 | 3-5GB | `-cpu`, `-cuda-gpu`, `-npu` |
| `qwen2.5-3b` | ~3B | 一般任務、高效 | 3-4GB | `-cpu`, `-cuda-gpu` |
| `qwen2.5-1.5b` | ~1.5B | 快速、低資源 | 2-3GB | `-cpu`, `-cuda-gpu` |
| `qwen2.5-0.5b` | ~0.5B | 分類、資源需求低 | 1-2GB | `-cpu`, `-cuda-gpu` |

### 變體命名

- **基礎名稱**（例如 `phi-4-mini`）：自動選擇最適合硬體的變體
- **`-cpu`**：CPU 優化，適用於所有環境
- **`-cuda-gpu`**：NVIDIA GPU 優化，需要 8GB+ VRAM
- **`-npu`**：Qualcomm NPU 優化，需要 NPU 驅動

**建議：** 使用基礎名稱（不帶後綴），讓 Foundry Local 自動選擇最佳變體。

---

## 成功指標

當您看到以下內容時，表示準備就緒：

✅ `foundry service status` 顯示 "running"  
✅ `foundry model ls` 顯示所需模型  
✅ 服務可在正確端點訪問  
✅ 健康檢查返回 200 OK  
✅ 筆記本診斷單元格通過  
✅ 輸出中無連接錯誤  

---

## 獲取幫助

### 文件
- **主存儲庫：** https://github.com/microsoft/Foundry-Local
- **Python SDK：** https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **CLI 參考：** https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-cli.md
- **疑難排解：** 請參閱此目錄中的 `troubleshooting.md`

### GitHub 問題
- https://github.com/microsoft/Foundry-Local/issues
- https://github.com/microsoft/edgeai-for-beginners/issues

---

**最後更新日期：** 2025 年 10 月 8 日  
**版本：** Workshop Notebooks 2.0

---

**免責聲明**：  
本文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於提供準確的翻譯，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於關鍵資訊，建議使用專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或錯誤解釋不承擔責任。
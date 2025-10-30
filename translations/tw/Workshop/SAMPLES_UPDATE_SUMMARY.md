<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d49922db25659f398bae92011305e9dc",
  "translation_date": "2025-10-28T20:50:18+00:00",
  "source_file": "Workshop/SAMPLES_UPDATE_SUMMARY.md",
  "language_code": "tw"
}
-->
# 工作坊範例 - Foundry Local SDK 更新摘要

## 概述

`Workshop/samples` 目錄中的所有 Python 範例已更新，以遵循 Foundry Local SDK 的最佳實踐，並確保工作坊範例的一致性。

**日期**：2025年10月8日  
**範圍**：涵蓋6個工作坊課程的9個Python檔案  
**主要重點**：錯誤處理、文件撰寫、SDK模式、使用者體驗

---

## 更新的檔案

### 課程 01：入門
- ✅ `chat_bootstrap.py` - 基本聊天和串流範例

### 課程 02：RAG 解決方案
- ✅ `rag_pipeline.py` - 使用嵌入的RAG實現
- ✅ `rag_eval_ragas.py` - 使用RAGAS指標進行RAG評估

### 課程 03：開源模型
- ✅ `benchmark_oss_models.py` - 多模型基準測試

### 課程 04：尖端模型
- ✅ `model_compare.py` - SLM與LLM比較

### 課程 05：AI 驅動代理
- ✅ `agents_orchestrator.py` - 多代理協調

### 課程 06：模型作為工具
- ✅ `models_router.py` - 基於意圖的模型路由
- ✅ `models_pipeline.py` - 多步驟路由管道

### 支援基礎架構
- ✅ `workshop_utils.py` - 已遵循最佳實踐（無需更改）

---

## 主要改進

### 1. 增強的錯誤處理

**之前：**
```python
manager, client, model_id = get_client(alias)
```

**之後：**
```python
try:
    manager, client, model_id = get_client(alias, endpoint=endpoint)
except Exception as e:
    print(f"[ERROR] Failed to initialize Foundry Local client: {e}")
    print("[INFO] Ensure Foundry Local is running: foundry service status")
    sys.exit(1)
```

**好處：**
- 提供清晰的錯誤訊息以優雅處理錯誤
- 可操作的故障排除提示
- 為腳本提供正確的退出代碼

### 2. 更好的匯入管理

**之前：**
```python
from sentence_transformers import SentenceTransformer
```

**之後：**
```python
try:
    from sentence_transformers import SentenceTransformer
except ImportError:
    print("[ERROR] sentence-transformers is required. Install with: pip install sentence-transformers")
    sys.exit(1)
```

**好處：**
- 當依賴項缺失時提供清晰的指導
- 防止晦澀的匯入錯誤
- 使用者友好的安裝指示

### 3. 全面的文件撰寫

**新增至所有範例：**
- 文件字串中環境變數的說明
- SDK參考連結
- 使用範例
- 詳細的函數/參數說明
- 提供更好的IDE支援的型別提示

**範例：**
```python
def pipeline(task: str) -> Dict[str, Any]:
    """Execute multi-step routed pipeline for complex task.
    
    Args:
        task: User task description
    
    Returns:
        Dictionary with plan, step outputs, and final summary
    
    Raises:
        Exception: If any pipeline stage fails
    """
```

### 4. 改善使用者回饋

**新增資訊性日誌：**
```python
print(f"[INFO] Using model alias: {alias} -> id: {model_id}")
print(f"[INFO] Endpoint: {manager.endpoint}")
print(f"[INFO] Loaded model: {alias} -> {model_id}")
```

**進度指示器：**
```python
print(f"[INFO] Benchmarking {alias}...")
print(f"  Round {round_num + 1}/{ROUNDS}: {latency:.3f}s")
print(f"[INFO] Completed {alias}\n")
```

**結構化輸出：**
```python
print("\n[BENCHMARK RESULTS]")
print(json.dumps(summary, indent=2))
```

### 5. 強大的基準測試

**課程 03 改進：**
- 每個模型的錯誤處理（失敗後繼續）
- 詳細的進度報告
- 正確執行預熱回合
- 支援首個標記延遲測量
- 階段的清晰分離

### 6. 一致的型別提示

**全程新增：**
```python
from typing import Dict, List, Tuple, Any, Optional

def run(alias: str) -> Tuple[float, str, Optional[int]]:
    """Run comparison for given model alias."""
```

**好處：**
- 更好的IDE自動完成
- 提早錯誤檢測
- 自我描述的程式碼

### 7. 增強的模型路由器

**課程 06 改進：**
- 全面的意圖檢測文件
- 模型選擇演算法解釋
- 詳細的路由日誌
- 測試輸出格式化
- 批量測試中的錯誤恢復

### 8. 多代理協調

**課程 05 改進：**
- 階段性進度報告
- 每個代理的錯誤處理
- 清晰的管道結構
- 更好的記憶體管理文件

---

## 測試清單

### 先決條件
```bash
# Ensure Foundry Local is running
foundry service status

# Load required models
foundry model run phi-4-mini
foundry model run qwen2.5-0.5b

# Install dependencies
pip install -r Workshop/requirements.txt
```

### 測試每個範例

#### 課程 01
```bash
cd Workshop/samples
python -m session01.chat_bootstrap "What is edge AI?"
```

#### 課程 02
```bash
cd Workshop/samples

# RAG pipeline
python -m session02.rag_pipeline

# RAG evaluation (requires ragas)
set RAG_QUESTION="What is local inference?"
python -m session02.rag_eval_ragas
```

#### 課程 03
```bash
cd Workshop/samples

# Quick benchmark (2 rounds)
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
set BENCH_ROUNDS=2
python -m session03.benchmark_oss_models
```

#### 課程 04
```bash
cd Workshop/samples

# SLM vs LLM comparison
set SLM_ALIAS=phi-4-mini
set LLM_ALIAS=qwen2.5-7b
python -m session04.model_compare
```

#### 課程 05
```bash
cd Workshop/samples

# Multi-agent orchestration
set AGENT_QUESTION="Why use local AI for healthcare?"
python -m session05.agents_orchestrator
```

#### 課程 06
```bash
cd Workshop/samples

# Intent-based routing
python -m session06.models_router

# Multi-step pipeline
set PIPELINE_TASK="Create a Python function and explain its performance"
python -m session06.models_pipeline
```

---

## 環境變數參考

### 全域（所有範例）
| 變數 | 描述 | 預設值 |
|------|------|--------|
| `FOUNDRY_LOCAL_ALIAS` | 使用的模型別名 | 根據範例而異 |
| `FOUNDRY_LOCAL_ENDPOINT` | 覆蓋服務端點 | 自動檢測 |
| `SHOW_USAGE` | 顯示令牌使用情況 | `0` |
| `RETRY_ON_FAIL` | 啟用重試邏輯 | `1` |
| `RETRY_BACKOFF` | 初始重試延遲 | `1.0` |

### 特定範例
| 變數 | 使用範例 | 描述 |
|------|----------|------|
| `EMBED_MODEL` | 課程 02 | 嵌入模型名稱 |
| `RAG_QUESTION` | 課程 02 | RAG測試問題 |
| `BENCH_MODELS` | 課程 03 | 逗號分隔的基準測試模型 |
| `BENCH_ROUNDS` | 課程 03 | 基準測試回合數 |
| `BENCH_PROMPT` | 課程 03 | 基準測試的測試提示 |
| `BENCH_STREAM` | 課程 03 | 測量首個標記延遲 |
| `SLM_ALIAS` | 課程 04 | 小型語言模型 |
| `LLM_ALIAS` | 課程 04 | 大型語言模型 |
| `COMPARE_PROMPT` | 課程 04 | 比較測試提示 |
| `AGENT_MODEL_PRIMARY` | 課程 05 | 主要代理模型 |
| `AGENT_MODEL_EDITOR` | 課程 05 | 編輯代理模型 |
| `AGENT_QUESTION` | 課程 05 | 代理測試問題 |
| `PIPELINE_TASK` | 課程 06 | 管道任務 |

---

## 重大變更

**無** - 所有更改均向後相容。

現有腳本將繼續運作。新增功能包括：
- 可選的環境變數
- 增強的錯誤訊息（不影響功能）
- 新增的日誌（可選擇隱藏）
- 更好的型別提示（無運行時影響）

---

## 實施的最佳實踐

### 1. 始終使用 Workshop Utils
```python
from workshop_utils import get_client, chat_once

# Provides caching, retry, and endpoint management
manager, client, model_id = get_client(alias, endpoint=endpoint)
```

### 2. 正確的錯誤處理模式
```python
try:
    # Initialize client
    manager, client, model_id = get_client(alias)
except Exception as e:
    print(f"[ERROR] Initialization failed: {e}")
    print("[INFO] Check: foundry service status")
    sys.exit(1)
```

### 3. 資訊性日誌
```python
print(f"[INFO] Starting process...")  # Info
print(f"[ERROR] Operation failed: {e}")  # Errors
print(f"[RESULT] Final output")  # Results
```

### 4. 型別提示
```python
from typing import Dict, List, Optional

def process(data: List[str]) -> Dict[str, Any]:
    """Process data with type safety."""
```

### 5. 全面的文件字串
```python
def function(arg: str) -> str:
    """Short description.
    
    Args:
        arg: Argument description
    
    Returns:
        Return value description
    
    Raises:
        Exception: When it fails
    """
```

### 6. 支援環境變數
```python
import os

alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-4-mini")
endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT")  # None if not set
```

### 7. 優雅降級
```python
# In benchmarks - continue on individual failures
for model in models:
    try:
        result = benchmark(model)
        results.append(result)
    except Exception as e:
        print(f"[ERROR] {model} failed: {e}")
        print(f"[INFO] Skipping {model}...")
```

---

## 常見問題與解決方案

### 問題：匯入錯誤
**解決方案：** 安裝缺失的依賴項
```bash
pip install sentence-transformers ragas datasets numpy
```

### 問題：連線錯誤
**解決方案：** 確保 Foundry Local 正在運行
```bash
foundry service status
foundry model run phi-4-mini
```

### 問題：找不到模型
**解決方案：** 檢查可用模型
```bash
foundry model ls
foundry model download <alias>
```

### 問題：性能緩慢
**解決方案：** 使用較小的模型或調整參數
```bash
set FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b
set BENCH_ROUNDS=2
```

---

## 下一步

### 1. 測試所有範例
按照上述測試清單逐一驗證所有範例是否正常運作。

### 2. 更新文件
- 更新課程的Markdown檔案，加入新的範例
- 在主README中新增故障排除部分
- 建立快速參考指南

### 3. 建立整合測試
```python
# Workshop/tests/test_samples.py
def test_all_samples():
    """Run smoke tests on all samples."""
```

### 4. 新增性能基準測試
追蹤錯誤處理改進帶來的性能提升。

### 5. 使用者回饋
收集工作坊參與者的回饋意見，關於：
- 錯誤訊息的清晰度
- 文件的完整性
- 使用的便利性

---

## 資源

- **Foundry Local SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **快速參考**: `Workshop/FOUNDRY_SDK_QUICKREF.md`
- **遷移說明**: `Workshop/SDK_MIGRATION_NOTES.md`
- **主存儲庫**: https://github.com/microsoft/Foundry-Local

---

## 維護

### 新增範例
在建立新範例時，請遵循以下模式：

1. 使用 `workshop_utils` 管理客戶端
2. 新增全面的錯誤處理
3. 支援環境變數
4. 新增型別提示和文件字串
5. 提供資訊性日誌
6. 在文件字串中包含使用範例
7. 連結至SDK文件

### 審查更新
在審查範例更新時，檢查以下項目：
- [ ] 所有I/O操作的錯誤處理
- [ ] 公共函數的型別提示
- [ ] 全面的文件字串
- [ ] 環境變數文件
- [ ] 資訊性使用者回饋
- [ ] SDK參考連結
- [ ] 一致的程式碼風格

---

**摘要**：所有工作坊的Python範例現已遵循Foundry Local SDK最佳實踐，並增強了錯誤處理、全面的文件撰寫以及改善的使用者體驗。無重大變更 - 所有現有功能均保留並得到提升。

---

**免責聲明**：  
本文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。儘管我們致力於提供準確的翻譯，請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於關鍵資訊，建議使用專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或誤釋不承擔責任。
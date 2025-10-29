<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a5bfedb0d4694a0b3a95d69b159b1a5a",
  "translation_date": "2025-10-28T20:41:26+00:00",
  "source_file": "Workshop/SDK_MIGRATION_NOTES.md",
  "language_code": "mo"
}
-->
# Foundry Local SDK 遷移注意事項

## 概述

Workshop 資料夾中的所有 Python 文件已更新，以遵循官方 [Foundry Local Python SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local) 的最新模式。

## 變更摘要

### 核心基礎架構 (`workshop_utils.py`)

#### 增強功能：
- **端點覆蓋支持**：新增 `FOUNDRY_LOCAL_ENDPOINT` 環境變數支持
- **改進的錯誤處理**：更詳細的錯誤訊息和例外處理
- **增強的快取功能**：快取鍵現在包含端點以支持多端點場景
- **指數回退**：重試邏輯現在使用指數回退以提高可靠性
- **類型註解**：新增全面的類型提示以改善 IDE 支持

#### 新增功能：
```python
# Now supports endpoint override
manager, client, model_id = get_client(alias, endpoint="http://localhost:8000")

# Better error messages
RuntimeError: Client initialization failed for 'phi-4-mini': <detailed_error>
```

### 範例應用

#### Session 01: 聊天啟動 (`chat_bootstrap.py`)
- 預設模型從 `phi-3.5-mini` 更新為 `phi-4-mini`
- 新增端點覆蓋支持
- 增強文件，加入 SDK 參考

#### Session 02: RAG 管道 (`rag_pipeline.py`)
- 預設模型更新為 `phi-4-mini`
- 新增端點覆蓋支持
- 改進文件，加入環境變數細節

#### Session 02: RAG 評估 (`rag_eval_ragas.py`)
- 更新模型預設值
- 新增端點配置
- 增強錯誤處理

#### Session 03: 基準測試 (`benchmark_oss_models.py`)
- 預設模型列表更新，包含 `phi-4-mini`
- 新增全面的環境變數文件
- 改進函數文件
- 全面新增端點覆蓋支持

#### Session 04: 模型比較 (`model_compare.py`)
- 預設 LLM 從 `gpt-oss-20b` 更新為 `qwen2.5-7b`
- 新增端點配置
- 增強文件

#### Session 05: 多代理協作 (`agents_orchestrator.py`)
- 新增類型提示（將 `str | None` 改為 `Optional[str]`）
- 增強 Agent 類文件
- 新增端點覆蓋支持
- 改進初始化模式

#### Session 06: 模型路由器 (`models_router.py`)
- 新增端點配置
- 增強意圖檢測文件
- 改進路由邏輯文件

#### Session 06: 管道 (`models_pipeline.py`)
- 新增全面的函數文件
- 改進逐步文件
- 增強錯誤處理

### 腳本

#### 基準匯出 (`export_benchmark_markdown.py`)
- 新增端點覆蓋支持
- 更新預設模型
- 增強函數文件
- 改進錯誤處理

#### CLI Linter (`lint_markdown_cli.py`)
- 新增 SDK 參考連結
- 改進使用文件

### 測試

#### 煙霧測試 (`smoke.py`)
- 新增端點覆蓋支持
- 增強文件
- 改進測試案例文件
- 更好的錯誤報告

## 環境變數

所有範例現在支持以下環境變數：

### 核心配置
- `FOUNDRY_LOCAL_ALIAS` - 使用的模型別名（預設值因範例而異）
- `FOUNDRY_LOCAL_ENDPOINT` - 覆蓋服務端點（可選）
- `SHOW_USAGE` - 顯示 token 使用統計（預設值："0"）
- `RETRY_ON_FAIL` - 啟用重試邏輯（預設值："1"）
- `RETRY_BACKOFF` - 初始重試延遲（秒）（預設值："1.0"）

### 範例特定
- `EMBED_MODEL` - RAG 範例的嵌入模型
- `BENCH_MODELS` - 基準測試的逗號分隔模型
- `BENCH_ROUNDS` - 基準測試輪次
- `BENCH_PROMPT` - 基準測試的測試提示
- `BENCH_STREAM` - 測量首 token 延遲
- `RAG_QUESTION` - RAG 範例的測試問題
- `AGENT_MODEL_PRIMARY` - 主代理模型
- `AGENT_MODEL_EDITOR` - 編輯代理模型
- `SLM_ALIAS` - 小型語言模型別名
- `LLM_ALIAS` - 大型語言模型別名

## SDK 已實施的最佳實踐

### 1. 正確的客戶端初始化
```python
# Old pattern
manager = FoundryLocalManager(alias)
client = OpenAI(base_url=manager.endpoint, api_key="not-needed")

# New pattern (with endpoint override)
manager = FoundryLocalManager(alias, endpoint=endpoint) if endpoint else FoundryLocalManager(alias)
client = OpenAI(
    base_url=manager.endpoint,
    api_key=manager.api_key or "not-needed"
)
```

### 2. 模型信息檢索
```python
# Proper model ID resolution
model_info = manager.get_model_info(alias)
model_id = model_info.id
```

### 3. 錯誤處理
```python
# Comprehensive error handling
try:
    manager = FoundryLocalManager(alias)
    # ... operations
except Exception as e:
    logger.error(f"Failed to initialize: {e}")
    raise RuntimeError(f"Initialization failed: {e}") from e
```

### 4. 使用指數回退的重試邏輯
```python
delay = initial_delay
for attempt in range(max_retries):
    try:
        # ... operation
        break
    except Exception:
        time.sleep(delay)
        delay *= 2  # Exponential backoff
```

### 5. 流式支持
```python
stream = client.chat.completions.create(
    model=model_id,
    messages=messages,
    stream=True,
    max_tokens=120
)
for chunk in stream:
    if chunk.choices and chunk.choices[0].delta:
        # Process chunk
```

## 自定範例的遷移指南

如果您正在創建新範例或更新現有範例：

1. **使用 `workshop_utils.py` 助手**：
   ```python
   from workshop_utils import get_client, chat_once
   ```

2. **支持端點覆蓋**：
   ```python
   endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT")
   manager, client, model_id = get_client(alias, endpoint=endpoint)
   ```

3. **新增全面的文件**：
   - 文件中加入環境變數
   - SDK 參考連結
   - 使用範例

4. **使用類型提示**：
   ```python
   from typing import Optional, List, Dict, Any
   ```

5. **實施正確的錯誤處理**：
   ```python
   try:
       result = operation()
   except Exception as e:
       logger.error(f"Operation failed: {e}")
       raise
   ```

## 測試

所有範例可使用以下方式進行測試：

```bash
# Set environment variables
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Run individual samples
cd Workshop/samples
python -m session01.chat_bootstrap "Test question"
python -m session02.rag_pipeline

# Run benchmark
python -m session03.benchmark_oss_models

# Run smoke tests
python -m Workshop.tests.smoke
```

## SDK 文件參考

- **主倉庫**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **API 文件**: 請查看 SDK 倉庫以獲取最新 API 文件

## 重大變更

### 無預期重大變更
所有變更均向後兼容。更新主要包括：
- 新增可選功能（端點覆蓋）
- 改進錯誤處理
- 增強文件
- 更新預設模型名稱至最新推薦

### 可選增強
您可能希望更新代碼以使用：
- `FOUNDRY_LOCAL_ENDPOINT` 進行明確的端點控制
- `SHOW_USAGE=1` 以顯示 token 使用情況
- 更新的模型預設值（`phi-4-mini` 替代 `phi-3.5-mini`）

## 常見問題及解決方案

### 問題: "客戶端初始化失敗"
**解決方案**: 確保 Foundry Local 服務正在運行：
```bash
foundry service start
foundry model run phi-4-mini
```

### 問題: "模型未找到"
**解決方案**: 檢查可用模型：
```bash
foundry model list
```

### 問題: 端點連接錯誤
**解決方案**: 驗證端點：
```bash
# Check service status
foundry service status

# Or set explicit endpoint
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000
```

## 下一步

1. **更新 Module08 範例**: 將相似模式應用於 Module08/samples
2. **新增整合測試**: 創建全面的測試套件
3. **性能基準測試**: 比較更新前後的性能
4. **文件更新**: 更新主 README，加入新模式

## 貢獻指南

新增範例時：
1. 使用 `workshop_utils.py` 以保持一致性
2. 遵循現有範例的模式
3. 新增全面的文件
4. 包含 SDK 參考連結
5. 支持端點覆蓋
6. 新增正確的類型提示
7. 在文件中加入使用範例

## 版本兼容性

這些更新兼容：
- `foundry-local-sdk`（最新版本）
- `openai>=1.30.0`
- Python 3.8+

---

**最後更新日期**: 2025-01-08  
**維護者**: EdgeAI Workshop 團隊  
**SDK 版本**: Foundry Local SDK (最新 0.7.117+67073234e7)

---

**免責聲明**：  
本文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。儘管我們努力確保翻譯的準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於關鍵信息，建議使用專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或誤釋不承擔責任。
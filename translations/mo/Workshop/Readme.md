<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "45923ada94573fee7c82cc4f0c3bb344",
  "translation_date": "2025-10-28T20:39:39+00:00",
  "source_file": "Workshop/Readme.md",
  "language_code": "mo"
}
-->
# EdgeAI 初學者工作坊

> **構建生產級邊緣 AI 應用的實踐學習路徑**
>
> 通過 Microsoft Foundry Local，從初步的聊天生成到多代理協作，掌握本地 AI 部署的技能，分六個進階課程進行。

---

## 🎯 簡介

歡迎參加 **EdgeAI 初學者工作坊** - 這是一個實踐性強的指南，幫助您構建完全在本地硬件上運行的智能應用。本工作坊將理論性的邊緣 AI 概念轉化為實際技能，通過使用 Microsoft Foundry Local 和小型語言模型（SLMs）進行逐步挑戰的練習。

### 為什麼選擇這個工作坊？

**邊緣 AI 革命已經到來**

全球組織正在從依賴雲端的 AI 轉向邊緣計算，原因有三：

1. **隱私與合規性** - 在本地處理敏感數據，無需通過雲端傳輸（符合 HIPAA、GDPR、金融法規）
2. **性能** - 消除網絡延遲（本地 50-500ms vs 雲端往返 500-2000ms）
3. **成本控制** - 消除每次使用 API 的費用，並在無需雲端支出的情況下擴展

**但邊緣 AI 與眾不同**

在本地運行 AI 需要新的技能：
- 為資源受限環境選擇和優化模型
- 本地服務管理和硬件加速
- 為小型模型設計提示工程
- 邊緣設備的生產部署模式

**這個工作坊將教授這些技能**

在 6 堂課（約 3 小時）中，您將從 "Hello World" 開始，逐步學習如何部署生產級的多代理系統 - 全部在您的本地機器上運行。

---

## 📚 學習目標

完成本工作坊後，您將能夠：

### 核心能力
1. **部署和管理本地 AI 服務**
   - 安裝和配置 Microsoft Foundry Local
   - 為邊緣部署選擇合適的模型
   - 管理模型生命周期（下載、加載、緩存）
   - 監控資源使用並優化性能

2. **構建 AI 驅動的應用**
   - 在本地實現兼容 OpenAI 的聊天生成
   - 為小型語言模型設計有效的提示
   - 處理流式響應以改善用戶體驗
   - 將本地模型集成到現有應用中

3. **創建 RAG（檢索增強生成）系統**
   - 使用嵌入構建語義搜索
   - 在特定領域知識的基礎上生成 LLM 響應
   - 使用行業標準指標評估 RAG 質量
   - 從原型擴展到生產

4. **優化模型性能**
   - 為您的使用案例基準測試多個模型
   - 測量延遲、吞吐量和首字元時間
   - 根據速度/質量權衡選擇最佳模型
   - 在實際場景中比較 SLM 和 LLM 的權衡

5. **協作多代理系統**
   - 為不同任務設計專門代理
   - 實現代理記憶和上下文管理
   - 在複雜工作流程中協調代理
   - 在多個模型間智能路由請求

6. **部署生產級解決方案**
   - 實現錯誤處理和重試邏輯
   - 監控令牌使用和系統資源
   - 使用模型作為工具模式構建可擴展架構
   - 計劃從邊緣到混合（邊緣 + 雲端）的遷移路徑

---

## 🎓 學習成果

### 您將構建的內容

到工作坊結束時，您將完成以下項目：

| 課程 | 成果 | 展示技能 |
|------|------|---------|
| **1** | 流式聊天應用 | 服務設置、基本生成、流式 UX |
| **2** | 帶評估的 RAG 系統 | 嵌入、語義搜索、質量指標 |
| **3** | 多模型基準測試套件 | 性能測量、模型比較 |
| **4** | SLM vs LLM 比較器 | 權衡分析、優化策略 |
| **5** | 多代理協作器 | 代理設計、記憶管理、協調 |
| **6** | 智能路由系統 | 意圖檢測、模型選擇、可擴展性 |

### 能力矩陣

| 技能水平 | 課程 1-2 | 課程 3-4 | 課程 5-6 |
|----------|----------|----------|----------|
| **初學者** | ✅ 設置與基礎 | ⚠️ 挑戰性 | ❌ 太高級 |
| **中級** | ✅ 快速回顧 | ✅ 核心學習 | ⚠️ 延伸目標 |
| **高級** | ✅ 輕鬆完成 | ✅ 精細化 | ✅ 生產模式 |

### 職業技能

**完成本工作坊後，您將能夠：**

✅ **構建隱私優先的應用**
- 處理 PHI/PII 的醫療應用
- 符合合規要求的金融服務
- 擁有數據主權的政府系統

✅ **為邊緣環境優化**
- 資源有限的 IoT 設備
- 離線優先的移動應用
- 低延遲的實時系統

✅ **設計智能架構**
- 用於複雜工作流程的多代理系統
- 混合邊緣-雲端部署
- 成本優化的 AI 基礎設施

✅ **領導邊緣 AI 項目**
- 評估項目的邊緣 AI 可行性
- 選擇合適的模型和框架
- 設計可擴展的本地 AI 解決方案

---

## 🗺️ 工作坊結構

### 課程概覽（6 堂課 × 30 分鐘 = 3 小時）

| 課程 | 主題 | 重點 | 時長 |
|------|------|------|------|
| **1** | 開始使用 Foundry Local | 安裝、驗證、首次生成 | 30 分鐘 |
| **2** | 使用 RAG 構建 AI 解決方案 | 提示工程、嵌入、評估 | 30 分鐘 |
| **3** | 開源模型 | 模型發現、基準測試、選擇 | 30 分鐘 |
| **4** | 前沿模型 | SLM vs LLM、優化、框架 | 30 分鐘 |
| **5** | AI 驅動的代理 | 代理設計、協作、記憶 | 30 分鐘 |
| **6** | 模型作為工具 | 路由、鏈接、擴展策略 | 30 分鐘 |

---

## 🚀 快速開始

### 先決條件

**系統要求：**
- **操作系統**：Windows 10/11、macOS 11+ 或 Linux (Ubuntu 20.04+)
- **內存**：最低 8GB，推薦 16GB+
- **存儲**：模型需要 10GB+ 可用空間
- **CPU**：支持 AVX2 的現代處理器
- **GPU**（可選）：支持 CUDA 的 GPU 或 Qualcomm NPU 加速

**軟件要求：**
- **Python 3.8+** ([下載](https://www.python.org/downloads/))
- **Microsoft Foundry Local** ([安裝指南](../../../Workshop))
- **Git** ([下載](https://git-scm.com/downloads))
- **Visual Studio Code**（推薦）([下載](https://code.visualstudio.com/))

### 3 步設置

#### 1. 安裝 Foundry Local

**Windows:**
```powershell
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
foundry service status
```

**確保 Azure AI Foundry Local 使用固定端口運行**

```bash
# Set FoundryLocal to use port 58123 (default)
foundry service set --port 58123 --show

# Or use a different port
foundry service set --port 58000 --show
```

**驗證是否正常工作：**
```bash
# Check service status
foundry service status

# Test the endpoint
curl http://127.0.0.1:58123/v1/models
```
**查找可用模型**
要查看 Foundry Local 實例中的可用模型，您可以查詢模型端點：

```bash
# cmd/bash/powershell
foundry model list
```

使用 Web 端點 

```bash
# Windows PowerShell
powershell -Command "Invoke-RestMethod -Uri 'http://127.0.0.1:58123/v1/models' -Method Get"

# Or using curl (if available)
curl http://127.0.0.1:58123/v1/models
```

#### 2. 克隆倉庫並安裝依賴項

```bash
# Clone repository
git clone https://github.com/microsoft/edgeai-for-beginners.git
cd edgeai-for-beginners/Workshop

# Create virtual environment
python -m venv .venv

# Activate virtual environment
# Windows:
.\.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

#### 3. 運行您的第一個示例

```bash
# Start Foundry Local and load a model
foundry model run phi-4-mini

# Run the chat bootstrap sample
cd samples
python -m session01.chat_bootstrap "What is edge AI?"
```

**✅ 成功！** 您應該看到關於邊緣 AI 的流式響應。

---

## 📦 工作坊資源

### Python 示例

逐步演示每個概念的實踐示例：

| 課程 | 示例 | 描述 | 運行時間 |
|------|------|------|---------|
| 1 | [`chat_bootstrap.py`](../../../Workshop/samples/session01/chat_bootstrap.py) | 基本與流式聊天 | ~30秒 |
| 2 | [`rag_pipeline.py`](../../../Workshop/samples/session02/rag_pipeline.py) | 帶嵌入的 RAG | ~45秒 |
| 2 | [`rag_eval_ragas.py`](../../../Workshop/samples/session02/rag_eval_ragas.py) | RAG 質量評估 | ~60秒 |
| 3 | [`benchmark_oss_models.py`](../../../Workshop/samples/session03/benchmark_oss_models.py) | 多模型基準測試 | ~2-3分鐘 |
| 4 | [`model_compare.py`](../../../Workshop/samples/session04/model_compare.py) | SLM vs LLM 比較 | ~45秒 |
| 5 | [`agents_orchestrator.py`](../../../Workshop/samples/session05/agents_orchestrator.py) | 多代理系統 | ~60秒 |
| 6 | [`models_router.py`](../../../Workshop/samples/session06/models_router.py) | 基於意圖的路由 | ~45秒 |
| 6 | [`models_pipeline.py`](../../../Workshop/samples/session06/models_pipeline.py) | 多步管道 | ~60秒 |

### Jupyter Notebooks

帶有解釋和可視化的交互式探索：

| 課程 | Notebook | 描述 | 難度 |
|------|----------|------|------|
| 1 | [`session01_chat_bootstrap.ipynb`](./notebooks/session01_chat_bootstrap.ipynb) | 聊天基礎與流式 | ⭐ 初學者 |
| 2 | [`session02_rag_pipeline.ipynb`](./notebooks/session02_rag_pipeline.ipynb) | 構建 RAG 系統 | ⭐⭐ 中級 |
| 2 | [`session02_rag_eval_ragas.ipynb`](./notebooks/session02_rag_eval_ragas.ipynb) | 評估 RAG 質量 | ⭐⭐ 中級 |
| 3 | [`session03_benchmark_oss_models.ipynb`](./notebooks/session03_benchmark_oss_models.ipynb) | 模型基準測試 | ⭐⭐ 中級 |
| 4 | [`session04_model_compare.ipynb`](./notebooks/session04_model_compare.ipynb) | 模型比較 | ⭐⭐ 中級 |
| 5 | [`session05_agents_orchestrator.ipynb`](./notebooks/session05_agents_orchestrator.ipynb) | 代理協作 | ⭐⭐⭐ 高級 |
| 6 | [`session06_models_router.ipynb`](./notebooks/session06_models_router.ipynb) | 意圖路由 | ⭐⭐⭐ 高級 |
| 6 | [`session06_models_pipeline.ipynb`](./notebooks/session06_models_pipeline.ipynb) | 管道協作 | ⭐⭐⭐ 高級 |

### 文檔

全面的指南和參考：

| 文檔 | 描述 | 使用時機 |
|------|------|---------|
| [QUICK_START.md](./QUICK_START.md) | 快速設置指南 | 從零開始 |
| [QUICK_REFERENCE.md](./QUICK_REFERENCE.md) | 命令與 API 速查表 | 需要快速答案時 |
| [FOUNDRY_SDK_QUICKREF.md](./FOUNDRY_SDK_QUICKREF.md) | SDK 模式與示例 | 編寫代碼時 |
| [ENV_CONFIGURATION.md](./ENV_CONFIGURATION.md) | 環境變量指南 | 配置示例時 |
| [SAMPLES_UPDATE_SUMMARY.md](./SAMPLES_UPDATE_SUMMARY.md) | 最新示例改進 | 理解變更時 |
| [SDK_MIGRATION_NOTES.md](./SDK_MIGRATION_NOTES.md) | 遷移指南 | 升級代碼時 |
| [notebooks/TROUBLESHOOTING.md](./notebooks/TROUBLESHOOTING.md) | 常見問題與解決方案 | 調試問題時 |

---

## 🎓 學習路徑建議

### 初學者（3-4 小時）
1. ✅ 課程 1：入門（專注於設置和基本聊天）
2. ✅ 課程 2：RAG 基礎（初期跳過評估）
3. ✅ 課程 3：簡單基準測試（僅測試 2 個模型）
4. ⏭️ 暫時跳過課程 4-6
5. 🔄 完成第一個應用後再回到課程 4-6

### 中級開發者（3 小時）
1. ⚡ 課程 1：快速設置驗證
2. ✅ 課程 2：完整 RAG 管道及評估
3. ✅ 課程 3：完整基準測試套件
4. ✅ 課程 4：模型優化
5. ✅ 課程 5-6：專注於架構模式

### 高級實踐者（2-3 小時）
1. ⚡ 課程 1-3：快速回顧與驗證
2. ✅ 課程 4：深入優化
3. ✅ 課程 5：多代理架構
4. ✅ 課程 6：生產模式與擴展
5. 🚀 延伸：構建自定義路由邏輯和混合部署

---

## 工作坊課程包（專注的 30 分鐘實驗室）

如果您正在參加濃縮的 6 堂課工作坊格式，請使用這些專門指南（每個指南與上述更廣泛的模塊文檔相對應並補充）：

| 工作坊課程 | 指南 | 核心重點 |
|-----------|------|---------|
| 1 | [Session01-GettingStartedFoundryLocal](./Session01-GettingStartedFoundryLocal.md) | 安裝、驗證、運行 phi & GPT-OSS-20B、加速 |
| 2 | [Session02-BuildAISolutionsRAG](./Session02-BuildAISolutionsRAG.md) | 提示工程、RAG 模式、CSV 和文檔基礎、遷移 |
| 3 | [Session03-OpenSourceModels](./Session03-OpenSourceModels.md) | Hugging Face 集成、基準測試、模型選擇 |
| 4 | [Session04-CuttingEdgeModels](./Session04-CuttingEdgeModels.md) | SLM 與 LLM 比較、WebGPU、Chainlit RAG、ONNX 加速 |
| 5 | [Session05-AIPoweredAgents](./Session05-AIPoweredAgents.md) | 智能代理角色、記憶、工具、編排 |
| 6 | [Session06-ModelsAsTools](./Session06-ModelsAsTools.md) | 路由、鏈接、擴展至 Azure 的路徑 |

每個課程文件包括：摘要、學習目標、30 分鐘演示流程、入門項目、驗證清單、故障排除以及官方 Foundry Local Python SDK 的參考資料。

### 範例腳本

安裝工作坊依賴項（Windows）：

```powershell
cd Workshop
py -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

macOS / Linux：

```bash
cd Workshop
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

如果 Foundry Local 服務在不同的（Windows）機器或虛擬機上運行，並從 macOS 進行操作，請導出端點：

```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```

| 課程 | 腳本 | 描述 |
|------|------|------|
| 1 | `samples/session01/chat_bootstrap.py` | 啟動服務與流式聊天 |
| 2 | `samples/session02/rag_pipeline.py` | 最小化 RAG（內存嵌入） |
|   | `samples/session02/rag_eval_ragas.py` | 使用 ragas 指標進行 RAG 評估 |
| 3 | `samples/session03/benchmark_oss_models.py` | 多模型延遲與吞吐量基準測試 |
| 4 | `samples/session04/model_compare.py` | SLM 與 LLM 比較（延遲與樣本輸出） |
| 5 | `samples/session05/agents_orchestrator.py` | 兩代理研究 → 編輯管道 |
| 6 | `samples/session06/models_router.py` | 基於意圖的路由演示 |
|   | `samples/session06/models_pipeline.py` | 多步計劃/執行/改進鏈 |

### 環境變數（適用於所有範例）

| 變數 | 用途 | 範例 |
|------|------|------|
| `FOUNDRY_LOCAL_ALIAS` | 基本範例的默認單模型別名 | `phi-4-mini` |
| `SLM_ALIAS` / `LLM_ALIAS` | 明確的 SLM 與較大模型比較 | `phi-4-mini` / `gpt-oss-20b` |
| `BENCH_MODELS` | 要基準測試的模型別名列表 | `qwen2.5-0.5b,mistral-7b` |
| `BENCH_ROUNDS` | 每個模型的基準測試次數 | `3` |
| `BENCH_PROMPT` | 基準測試中使用的提示 | `Explain retrieval augmented generation briefly.` |
| `EMBED_MODEL` | Sentence-transformers 嵌入模型 | `sentence-transformers/all-MiniLM-L6-v2` |
| `RAG_QUESTION` | 覆蓋 RAG 管道的測試查詢 | `Why use RAG with local inference?` |
| `AGENT_QUESTION` | 覆蓋代理管道查詢 | `Explain why edge AI matters for compliance.` |
| `AGENT_MODEL_PRIMARY` | 用於研究代理的模型別名 | `phi-4-mini` |
| `AGENT_MODEL_EDITOR` | 用於編輯代理的模型別名（可不同） | `gpt-oss-20b` |
| `SHOW_USAGE` | 當設為 `1` 時，打印每次完成的 token 使用量 | `1` |
| `RETRY_ON_FAIL` | 當設為 `1` 時，在暫時性聊天錯誤時重試一次 | `1` |
| `RETRY_BACKOFF` | 重試前等待的秒數 | `1.0` |

如果未設置變數，腳本會回退到合理的默認值。對於單模型演示，通常只需要設置 `FOUNDRY_LOCAL_ALIAS`。

### 工具模組

所有範例現在共享一個輔助模組 `samples/workshop_utils.py`，提供：

* 緩存的 `FoundryLocalManager` + OpenAI 客戶端創建
* 帶可選重試和使用量打印的 `chat_once()` 輔助函數
* 簡單的 token 使用量報告（通過設置 `SHOW_USAGE=1` 啟用）

這減少了重複並突出了高效本地模型編排的最佳實踐。

## 可選增強功能（跨課程）

| 主題 | 增強功能 | 課程 | 環境變數 / 切換 |
|------|----------|------|----------------|
| 確定性 | 固定溫度 + 穩定提示集 | 1–6 | 設置 `temperature=0`, `top_p=1` |
| Token 使用量可見性 | 一致的成本/效率教學 | 1–6 | `SHOW_USAGE=1` |
| 流式首 token | 感知延遲指標 | 1,3,4,6 | `BENCH_STREAM=1`（基準測試） |
| 重試韌性 | 處理暫時性冷啟動 | 全部 | `RETRY_ON_FAIL=1` + `RETRY_BACKOFF` |
| 多模型代理 | 異構角色專業化 | 5 | `AGENT_MODEL_PRIMARY`, `AGENT_MODEL_EDITOR` |
| 自適應路由 | 意圖 + 成本啟發式 | 6 | 擴展路由器以包含升級邏輯 |
| 向量記憶 | 長期語義回憶 | 2,5,6 | 集成 FAISS/Chroma 嵌入索引 |
| 跟蹤導出 | 審計與評估 | 2,5,6 | 每步追加 JSON 行 |
| 質量標準 | 定性跟蹤 | 3–6 | 次要評分提示 |
| 煙霧測試 | 快速工作坊前驗證 | 全部 | `python Workshop/tests/smoke.py` |

### 確定性快速開始

```powershell
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
python Workshop\tests\smoke.py
```

預期在相同輸入的重複測試中保持穩定的 token 數量。

### RAG 評估（課程 2）

使用 `rag_eval_ragas.py` 計算答案的相關性、真實性和上下文精確度，基於一個小型合成數據集：

```powershell
cd Workshop/samples
python -m session02.rag_eval_ragas
```

通過提供更大的 JSONL 文件（包含問題、上下文和真實答案），然後轉換為 Hugging Face 的 `Dataset`，進行擴展。

## CLI 命令準確性附錄

工作坊僅使用當前已記錄/穩定的 Foundry Local CLI 命令。

### 參考的穩定命令

| 類別 | 命令 | 用途 |
|------|------|------|
| 核心 | `foundry --version` | 顯示已安裝版本 |
| 核心 | `foundry init` | 初始化配置 |
| 服務 | `foundry service start` | 啟動本地服務（如果未自動啟動） |
| 服務 | `foundry status` | 顯示服務狀態 |
| 模型 | `foundry model list` | 列出目錄/可用模型 |
| 模型 | `foundry model download <alias>` | 將模型權重下載到緩存 |
| 模型 | `foundry model run <alias>` | 本地啟動（加載）模型；結合 `--prompt` 進行一次性操作 |
| 模型 | `foundry model unload <alias>` / `foundry model stop <alias>` | 從內存中卸載模型（如果支持） |
| 緩存 | `foundry cache list` | 列出已緩存（下載）的模型 |
| 系統 | `foundry system info` | 硬件與加速能力快照 |
| 系統 | `foundry system gpu-info` | GPU 診斷信息 |
| 配置 | `foundry config list` | 顯示當前配置值 |
| 配置 | `foundry config set <key> <value>` | 更新配置 |

### 一次性提示模式

取代已棄用的 `model chat` 子命令，使用：

```powershell
foundry model run <alias> --prompt "Your question here"
```

這執行一次提示/回應循環後退出。

### 移除/避免的模式

| 棄用/未記錄 | 替代/指導 |
|-------------|----------|
| `foundry model chat <model> "..."` | `foundry model run <model> --prompt "..."` |
| `foundry model list --running` | 使用普通 `foundry model list` + 最近活動/日誌 |
| `foundry model list --cached` | `foundry cache list` |
| `foundry model stats <model>` | 使用基準測試 Python 腳本 + 操作系統工具（任務管理器 / `nvidia-smi`） |
| `foundry model benchmark ...` | `samples/session03/benchmark_oss_models.py` |

### 基準測試與遙測

- 延遲、p95、tokens/sec：`samples/session03/benchmark_oss_models.py`
- 首 token 延遲（流式）：設置 `BENCH_STREAM=1`
- 資源使用：操作系統監控工具（任務管理器、活動監視器、`nvidia-smi`）+ `foundry system info`。

隨著新的 CLI 遙測命令在上游穩定，它們可以以最小的修改集成到課程 markdown 文件中。

### 自動化語法檢查

一個自動化語法檢查工具防止在 markdown 文件的代碼塊中重新引入棄用的 CLI 模式：

腳本：`Workshop/scripts/lint_markdown_cli.py`

代碼塊內的棄用模式會被阻止。

推薦替代：
| 棄用 | 替代 |
|------|------|
| `foundry model chat <a> "..."` | `foundry model run <a> --prompt "..."` |
| `model list --running` | `model list` |
| `model list --cached` | `cache list` |
| `model stats` | 基準測試腳本 + 系統工具 |
| `model benchmark` | `samples/session03/benchmark_oss_models.py` |
| `model list --available` | `model list` |

本地運行：
```powershell
python Workshop\scripts\lint_markdown_cli.py --verbose
```

GitHub Action：`.github/workflows/markdown-cli-lint.yml` 在每次推送和 PR 時運行。

可選的 pre-commit hook：
```bash
echo "python Workshop/scripts/lint_markdown_cli.py" > .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```

## 快速 CLI → SDK 遷移表

| 任務 | CLI 單行命令 | SDK（Python）等效 | 備註 |
|------|-------------|------------------|------|
| 運行模型一次（提示） | `foundry model run phi-4-mini --prompt "Hello"` | `manager=FoundryLocalManager("phi-4-mini"); client=OpenAI(base_url=manager.endpoint, api_key=manager.api_key or "not-needed"); client.chat.completions.create(model=manager.get_model_info("phi-4-mini").id, messages=[{"role":"user","content":"Hello"}])` | SDK 自動啟動服務與緩存 |
| 下載（緩存）模型 | `foundry model download qwen2.5-0.5b` | `FoundryLocalManager("qwen2.5-0.5b")  # 觸發下載/加載` | 管理器在別名映射到多個版本時選擇最佳版本 |
| 列出目錄 | `foundry model list` | `# 使用管理器獲取每個別名或維護已知列表` | CLI 聚合；SDK 目前每個別名初始化 |
| 列出已緩存模型 | `foundry cache list` | `manager.list_cached_models()` | 在管理器初始化後（任何別名） |
| 啟用 GPU 加速 | `foundry config set compute.onnx.enable_gpu true` | `# CLI 操作；SDK 假設配置已應用` | 配置是外部副作用 |
| 獲取端點 URL | （隱式） | `manager.endpoint` | 用於創建 OpenAI 兼容客戶端 |
| 預熱模型 | `foundry model run <alias>` 然後首次提示 | `chat_once(alias, messages=[...])`（工具） | 工具處理初始冷延遲預熱 |
| 測量延遲 | `python -m session03.benchmark_oss_models` | `import benchmark_oss_models`（或新導出腳本） | 優先使用腳本以獲得一致的指標 |
| 停止/卸載模型 | `foundry model unload <alias>` | （未暴露 – 重啟服務/進程） | 通常不需要在工作坊流程中 |
| 獲取 token 使用量 | （查看輸出） | `resp.usage.total_tokens` | 如果後端返回使用量對象則提供 |

## 基準測試 Markdown 導出

使用腳本 `Workshop/scripts/export_benchmark_markdown.py` 運行新的基準測試（邏輯與 `samples/session03/benchmark_oss_models.py` 相同），並生成 GitHub 友好的 Markdown 表格以及原始 JSON。

### 範例

```powershell
python Workshop\scripts\export_benchmark_markdown.py --models "qwen2.5-0.5b,mistral-7b" --prompt "Explain retrieval augmented generation briefly." --rounds 3 --output benchmark_report.md
```

生成的文件：
| 文件 | 內容 |
|------|------|
| `benchmark_report.md` | Markdown 表格 + 解釋提示 |
| `benchmark_report.json` | 原始指標數組（用於差異/趨勢跟蹤） |

在環境中設置 `BENCH_STREAM=1` 以包含首 token 延遲（如果支持）。

---

**免責聲明**：  
本文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。儘管我們努力確保翻譯的準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於關鍵信息，建議使用專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或誤釋不承擔責任。
# 工作坊筆記本

> **互動式 Jupyter 筆記本，學習邊緣 AI 的實作**
>
> 循序漸進、自主學習的教程，從基礎的聊天完成到使用 Microsoft Foundry Local 和小型語言模型的高級多代理系統。

---

## 📖 簡介

歡迎來到 **邊緣 AI 初學者工作坊筆記本** 集合。這些互動式 Jupyter 筆記本提供了實作學習的體驗，您可以即時撰寫、執行並試驗邊緣 AI 的程式碼。

### 為什麼選擇 Jupyter 筆記本？

與傳統教程不同，這些筆記本提供：

- **互動式學習**：執行程式碼單元並立即查看結果
- **試驗性**：修改參數並即時觀察變化
- **文件化**：內嵌的解釋和 Markdown 單元引導您理解概念
- **可重現性**：完整的工作範例供您參考和重用
- **可視化**：直接查看性能指標、嵌入和結果

### 這些筆記本有什麼特別之處？

每個筆記本都遵循 **生產就緒的最佳實踐** 設計：

✅ **全面的錯誤處理** - 優雅降級和資訊豐富的錯誤訊息  
✅ **類型提示與文件化** - 清晰的函數簽名和文檔字符串  
✅ **性能監控** - 追蹤 Token 使用量和延遲測量  
✅ **模組化設計** - 可重用的模式，適應您的專案  
✅ **漸進式複雜性** - 系統性地建立在前一課程的基礎上  

---

## 🎯 學習目標

### 您將掌握的核心技能

透過這些筆記本，您將精通：

1. **本地 AI 服務管理**
   - 配置和管理 Microsoft Foundry Local 服務
   - 根據硬體選擇並載入適合的模型
   - 監控資源使用並優化性能
   - 處理服務發現和健康檢查

2. **AI 應用程式開發**
   - 本地實作 OpenAI 兼容的聊天完成
   - 建立流式介面以提升使用者體驗
   - 為小型語言模型設計有效的提示
   - 將本地模型整合到應用程式中

3. **檢索增強生成 (RAG)**
   - 使用向量嵌入建立語義搜索
   - 在特定領域文件中基於 LLM 回應
   - 使用 RAGAS 指標評估 RAG 質量
   - 從原型擴展到生產環境

4. **性能優化**
   - 系統性地基準測試多個模型
   - 測量延遲、吞吐量和首 Token 時間
   - 比較小型語言模型與大型語言模型
   - 根據性能/質量權衡選擇最佳模型

5. **多代理協作**
   - 為不同任務設計專門代理
   - 實作代理記憶和上下文管理
   - 在複雜工作流程中協調多個代理
   - 建立代理協作的協調模式

6. **智能模型路由**
   - 實作意圖檢測和模式匹配
   - 自動將查詢路由到適合的模型
   - 建立多步管道（計劃 → 執行 → 精煉）
   - 設計可擴展的模型工具架構

---

## 🎓 學習成果

### 您將建立的內容

| 筆記本 | 成果 | 展示技能 | 難度 |
|--------|------|----------|------|
| **Session 01** | 支援流式的聊天應用程式 | 服務設置、基礎完成、流式 UX | ⭐ 初學者 |
| **Session 02 (RAG)** | RAG 管道及評估 | 嵌入、語義搜索、質量指標 | ⭐⭐ 中級 |
| **Session 02 (Eval)** | RAG 質量評估器 | RAGAS 指標、系統性評估 | ⭐⭐ 中級 |
| **Session 03** | 多模型基準測試 | 性能測量、模型比較 | ⭐⭐ 中級 |
| **Session 04** | SLM 與 LLM 比較器 | 權衡分析、優化策略 | ⭐⭐⭐ 高級 |
| **Session 05** | 多代理協調器 | 代理設計、記憶、協作 | ⭐⭐⭐ 高級 |
| **Session 06 (Router)** | 智能路由系統 | 意圖檢測、模型選擇 | ⭐⭐⭐ 高級 |
| **Session 06 (Pipeline)** | 多步管道 | 計劃/執行/精煉工作流 | ⭐⭐⭐ 高級 |

### 能力進展

```
Session 01 ────► Session 02 ────► Session 03 ────► Session 04 ────► Session 05-06
   Basic            RAG             Benchmarking      Comparison      Multi-Agent
   Chat             Systems         & Performance     & Optimization  Orchestration
   
Foundation    │   Intermediate   │   Advanced       │   Expert
──────────────┴──────────────────┴──────────────────┴──────────────►
```

---

## 📅 工作坊時間表

### 🚀 半日工作坊 (3.5 小時)

**適合：團隊培訓、黑客松、大會工作坊**

| 時間 | 時長 | 課程 | 主題 | 活動 |
|------|------|------|------|------|
| **0:00** | 30 分鐘 | 設置與簡介 | 環境設置、Foundry Local 安裝 | 安裝依賴項，驗證設置 |
| **0:30** | 30 分鐘 | Session 01 | 基礎聊天完成、流式 | 執行筆記本，修改提示 |
| **1:00** | 45 分鐘 | Session 02 | RAG 管道、嵌入、評估 | 建立 RAG 系統，測試查詢 |
| **1:45** | 15 分鐘 | 休息 | ☕ 咖啡與提問 | — |
| **2:00** | 30 分鐘 | Session 03 | 多模型基準測試 | 比較 3+ 模型 |
| **2:30** | 30 分鐘 | Session 04 | SLM 與 LLM 的權衡 | 分析性能/質量 |
| **3:00** | 30 分鐘 | Session 05-06 | 多代理系統與路由 | 探索高級模式 |

**成果**：參與者將完成 6 個邊緣 AI 應用程式及生產就緒的程式碼模式。

---

### 🎓 全日工作坊 (6 小時)

**適合：深入培訓、訓練營、大學課程**

| 時間 | 時長 | 課程 | 主題 | 活動 |
|------|------|------|------|------|
| **0:00** | 45 分鐘 | 設置與理論 | 環境設置、邊緣 AI 基礎 | 安裝、驗證、討論用例 |
| **0:45** | 45 分鐘 | Session 01 | 聊天完成深入探討 | 實作基礎與流式聊天 |
| **1:30** | 30 分鐘 | 休息 | ☕ 咖啡與交流 | — |
| **2:00** | 60 分鐘 | Session 02 (兩者) | RAG 管道 + RAGAS 評估 | 建立完整 RAG 系統 |
| **3:00** | 30 分鐘 | 實作實驗室 1 | 為您的領域定制 RAG | 應用於自己的文件 |
| **3:30** | 30 分鐘 | 午餐 | 🍽️ | — |
| **4:00** | 45 分鐘 | Session 03 | 基準測試方法 | 系統性模型比較 |
| **4:45** | 45 分鐘 | Session 04 | 優化策略 | SLM 與 LLM 分析 |
| **5:30** | 60 分鐘 | Session 05-06 | 高級協作 | 多代理系統、路由 |
| **6:30** | 30 分鐘 | 實作實驗室 2 | 建立自定義代理系統 | 設計自己的協調器 |

**成果**：深入理解邊緣 AI 模式及 2 個自定義專案。

---

### 📚 自主學習 (2 週)

**適合：個人學習者、線上課程、自學**

#### 第 1 週：基礎 (6 小時)

| 天 | 重點 | 時長 | 筆記本 | 作業 |
|----|------|------|--------|------|
| **週一** | 設置與基礎 | 1.5 小時 | Session 01 | 修改提示，測試流式 |
| **週三** | RAG 基礎 | 2 小時 | Session 02 (兩者) | 添加自己的文件 |
| **週五** | 基準測試 | 1.5 小時 | Session 03 | 比較額外模型 |
| **週六** | 回顧與練習 | 1 小時 | 第 1 週所有 | 完成練習，除錯 |

#### 第 2 週：高級 (5 小時)

| 天 | 重點 | 時長 | 筆記本 | 作業 |
|----|------|------|--------|------|
| **週一** | 優化 | 1.5 小時 | Session 04 | 文件化權衡 |
| **週三** | 多代理系統 | 2 小時 | Session 05 | 設計自定義代理 |
| **週五** | 智能路由 | 1.5 小時 | Session 06 (兩者) | 建立路由邏輯 |
| **週六** | 最終專案 | 2 小時 | 整合 | 結合多種模式 |

**成果**：掌握邊緣 AI 模式及作品集專案。

---

## 📔 筆記本描述

### 📘 Session 01: 聊天啟動
**檔案**：`session01_chat_bootstrap.ipynb`  
**時長**：20-30 分鐘  
**先決條件**：無  
**難度**：⭐ 初學者

**您將學到**：
- 安裝並配置 Foundry Local Python SDK
- 使用 `FoundryLocalManager` 進行自動服務發現
- 使用 OpenAI 兼容 API 實作基礎聊天完成
- 建立流式回應以提升使用者體驗
- 優雅處理錯誤及服務不可用情況

**關鍵概念**：服務管理、聊天完成、流式、錯誤處理

**您將建立**：支援流式的互動聊天應用程式

---

### 📗 Session 02: RAG 管道
**檔案**：`session02_rag_pipeline.ipynb`  
**時長**：30-45 分鐘  
**先決條件**：Session 01  
**難度**：⭐⭐ 中級

**您將學到**：
- 實作檢索增強生成 (RAG) 模式
- 使用 sentence-transformers 建立向量嵌入
- 使用餘弦相似度進行語義搜索
- 在特定領域文件中基於 LLM 回應
- 使用導入保護處理可選依賴項

**關鍵概念**：RAG 架構、嵌入、語義搜索、向量相似度

**您將建立**：基於文件的問答系統

---

### 📗 Session 02: 使用 RAGAS 進行 RAG 評估
**檔案**：`session02_rag_eval_ragas.ipynb`  
**時長**：30-45 分鐘  
**先決條件**：Session 02 RAG 管道  
**難度**：⭐⭐ 中級

**您將學到**：
- 使用業界標準指標評估 RAG 質量
- 測量上下文相關性、答案相關性、真實性
- 使用 RAGAS 框架進行系統性評估
- 識別並修復 RAG 質量問題
- 為您的領域建立評估數據集

**關鍵概念**：RAG 評估、RAGAS 指標、質量測量、系統性測試

**您將建立**：RAG 質量評估框架

---

### 📙 Session 03: 基準測試開源模型
**檔案**：`session03_benchmark_oss_models.ipynb`  
**時長**：30-45 分鐘  
**先決條件**：Session 01  
**難度**：⭐⭐ 中級

**您將學到**：
- 系統性地基準測試多個模型
- 測量延遲、吞吐量、首 Token 時間
- 為模型故障實作優雅降級
- 比較不同模型系列的性能
- 可視化並分析基準測試結果

**關鍵概念**：性能基準測試、延遲測量、模型比較、統計分析

**您將建立**：多模型基準測試套件

---

### 📙 Session 04: 模型比較 (SLM vs LLM)
**檔案**：`session04_model_compare.ipynb`  
**時長**：30-45 分鐘  
**先決條件**：Session 01, 03  
**難度**：⭐⭐⭐ 高級

**您將學到**：
- 比較小型語言模型與大型語言模型
- 分析性能與質量的權衡
- 測量邊緣適用性指標
- 選擇適合部署限制的最佳模型
- 文件化模型選擇的決策標準

**關鍵概念**：模型選擇、權衡分析、優化策略、部署規劃

**您將建立**：SLM 與 LLM 比較框架

---

### 📕 Session 05: 多代理協調器
**檔案**：`session05_agents_orchestrator.ipynb`  
**時長**：45-60 分鐘  
**先決條件**：Session 01-02  
**難度**：⭐⭐⭐ 高級

**您將學到**：
- 為不同任務設計專門代理
- 實作代理記憶和上下文管理
- 建立代理協作的協調模式
- 處理代理間的通信與交接
- 監控多代理系統性能

**關鍵概念**：代理架構、協調模式、記憶管理、代理協作

**您將建立**：具有協調器和專家代理的多代理系統

---

### 📕 Session 06: 模型路由器
**檔案**：`session06_models_router.ipynb`  
**時長**：30-45 分鐘  
**先決條件**：Session 01, 03  
**難度**：⭐⭐⭐ 高級

**您將學到**：
- 實作意圖檢測和模式匹配
- 建立基於關鍵字的模型路由
- 自動將查詢路由到適合的模型
- 配置多模型註冊表
- 監控路由決策與性能

**關鍵概念**：意圖檢測、模型路由、模式匹配、智能選擇

**您將建立**：智能模型路由系統

---

### 📕 Session 06: 多步管道
**檔案**：`session06_models_pipeline.ipynb`  
**時長**：30-45 分鐘  
**先決條件**：Session 01, 06 Router  
**難度**：⭐⭐⭐ 高級

**您將學到**：
- 建立多步 AI 管道（計劃 → 執行 → 精煉）
- 整合路由器進行智能模型選擇
- 實作管道錯誤處理與恢復
- 監控管道性能與階段
- 設計可擴展的模型工具架構

**核心概念**: 管道架構、多階段處理、錯誤恢復、可擴展性模式

**你將構建**: 帶有路由功能的多步智能管道

---

## 🚀 快速開始

### 先決條件

**系統需求**:
- **作業系統**: Windows 10/11、macOS 11+ 或 Linux (Ubuntu 20.04+)
- **記憶體**: 最少 8GB，建議 16GB 以上
- **儲存空間**: 至少 10GB 的空閒空間用於模型
- **硬體**: 支援 AVX2 的 CPU；可選 GPU (CUDA, Qualcomm NPU)

**軟體需求**:
- **Python 3.8+** 並安裝 pip
- **Jupyter Notebook** 或 **VS Code** 並安裝 Jupyter 擴展
- **Microsoft Foundry Local** 已安裝並配置
- **Git** (用於複製倉庫)

### 安裝步驟

#### 1. 安裝 Foundry Local

**Windows**:
```cmd
winget install Microsoft.FoundryLocal
```

**macOS**:
```bash
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**驗證安裝**:
```bash
foundry --version
```

#### 2. 設置 Python 環境

```bash
# Navigate to Workshop directory
cd Workshop

# Create virtual environment
python -m venv .venv

# Activate virtual environment
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

#### 3. 啟動 Foundry Local

```bash
# Load a model (auto-downloads if needed)
foundry model run phi-4-mini

# Verify service is running
foundry service status
```

#### 4. 啟動 Jupyter

```bash
# Start Jupyter Notebook
jupyter notebook notebooks/

# Or use VS Code with Jupyter extension
code notebooks/
```

### 快速驗證

在 Python cell 中執行以下代碼以驗證設置：

```python
from foundry_local import FoundryLocalManager
import openai

# Initialize manager (auto-discovers service)
manager = FoundryLocalManager("phi-4-mini")

# Configure OpenAI client
client = openai.OpenAI(
    base_url=manager.endpoint,
    api_key=manager.api_key
)

# Test chat completion
response = client.chat.completions.create(
    model=manager.get_model_info("phi-4-mini").id,
    messages=[{"role": "user", "content": "Hello!"}]
)

print(response.choices[0].message.content)
```

**預期輸出**: 從本地模型返回的問候回應。

---

## 📝 工作坊最佳實踐

### 對於講師

**工作坊前**:
- ✅ 提前一週發送安裝指導
- ✅ 在目標硬體上測試所有筆記本
- ✅ 準備常見問題的故障排除指南
- ✅ 準備備用模型 (如果 phi-4-mini 失敗，則使用 phi-3.5-mini)
- ✅ 設置共享聊天頻道以回答問題

**工作坊期間**:
- ✅ 開始時進行快速環境檢查 (5 分鐘)
- ✅ 立即分享故障排除資源
- ✅ 鼓勵實驗和修改
- ✅ 策略性地安排休息時間 (每兩節課後)
- ✅ 提供助教進行一對一幫助

**工作坊後**:
- ✅ 分享完整的工作筆記本和解決方案
- ✅ 提供額外資源的鏈接
- ✅ 創建反饋調查以改進
- ✅ 提供後續問題的辦公時間

### 對於學員

**最大化學習效果**:
- ✅ 在工作坊開始前完成設置
- ✅ 自己執行每個代碼單元 (不要僅僅閱讀)
- ✅ 嘗試調整參數和提示
- ✅ 記錄洞察和注意事項
- ✅ 遇到問題時提問 (其他人可能有相同的問題)

**常見錯誤避免**:
- ❌ 跳過代碼單元的執行順序 (需按順序執行)
- ❌ 不仔細閱讀錯誤訊息
- ❌ 匆忙進行而未理解內容
- ❌ 忽略 markdown 的解釋
- ❌ 未保存修改後的筆記本

**故障排除提示**:
1. **服務未運行**: 檢查 `foundry service status`
2. **導入錯誤**: 確保虛擬環境已激活
3. **模型未找到**: 執行 `foundry model ls` 列出已加載的模型
4. **性能緩慢**: 檢查記憶體使用情況，關閉其他應用程式
5. **結果異常**: 重啟內核並從頭執行所有代碼單元

---

## 🔗 附加資源

### 工作坊材料

- **[工作坊主指南](../Readme.md)** - 概述、學習目標、職業成果
- **[Python 範例](../../../../Workshop/samples)** - 每節課對應的 Python 腳本
- **[課程指南](../../../../Workshop)** - 詳細的 markdown 指南 (Session01-06)
- **[腳本](../../../../Workshop/scripts)** - 驗證和測試工具
- **[故障排除](./TROUBLESHOOTING.md)** - 常見問題及解決方案
- **[快速入門](./quickstart.md)** - 快速開始指南

### 文件

- **[Foundry Local 文件](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)** - 微軟官方文件
- **[OpenAI Python SDK](https://github.com/openai/openai-python)** - OpenAI SDK 參考
- **[Sentence Transformers](https://www.sbert.net/)** - 嵌入模型文件
- **[RAGAS 框架](https://docs.ragas.io/)** - RAG 評估指標

### 社群

- **[GitHub 討論](https://github.com/microsoft/edgeai-for-beginners/discussions)** - 提問、分享項目
- **[Azure AI Foundry Discord](https://discord.com/invite/ByRwuEEgH4)** - 即時社群支援
- **[Stack Overflow](https://stackoverflow.com/questions/tagged/foundry-local)** - 技術問答

---

## 🎯 學習路徑推薦

### 初學者路徑 (從這裡開始)

1. **Session 01** - 聊天啟動
2. **Session 02** - RAG 管道
3. **Session 03** - 模型基準測試

**時間**: 約 2 小時 | **重點**: 基礎模式

---

### 中級路徑

1. 完成初學者路徑
2. **Session 02** - RAG 評估
3. **Session 04** - 模型比較

**時間**: 約 4 小時 | **重點**: 質量和優化

---

### 高級路徑 (完整工作坊)

1. 完成中級路徑
2. **Session 05** - 多代理協調器
3. **Session 06** - 模型路由器
4. **Session 06** - 多步管道

**時間**: 約 6 小時 | **重點**: 生產模式

---

### 自定義項目路徑

1. 完成初學者路徑 (Session 01-03)
2. 根據目標選擇一個高級課程:
   - **構建 RAG 應用?** → Session 02 評估
   - **優化性能?** → Session 04 比較
   - **複雜工作流程?** → Session 05 協調器
   - **可擴展架構?** → Session 06 路由器 + 管道

**時間**: 約 3 小時 | **重點**: 項目特定技能

---

## 📊 成功指標

通過以下里程碑追蹤進度：

- [ ] **設置完成** - Foundry Local 運行，所有依賴已安裝
- [ ] **首次聊天** - 完成 Session 01，流式聊天正常運行
- [ ] **RAG 構建** - 完成 Session 02，文檔問答系統功能正常
- [ ] **模型基準測試** - 完成 Session 03，收集性能數據
- [ ] **分析權衡** - 完成 Session 04，記錄模型選擇標準
- [ ] **代理協調** - 完成 Session 05，多代理系統正常運行
- [ ] **路由實現** - 完成 Session 06，智能模型選擇功能正常
- [ ] **自定義項目** - 將工作坊模式應用於自己的使用案例

---

## 🤝 貢獻

發現問題或有建議？我們歡迎您的貢獻！

- **報告問題**: [GitHub Issues](https://github.com/microsoft/edgeai-for-beginners/issues)
- **提出改進建議**: [GitHub Discussions](https://github.com/microsoft/edgeai-for-beginners/discussions)
- **提交 PR**: 請遵循 [貢獻指南](../../AGENTS.md)

---

## 📄 授權

此工作坊屬於 [EdgeAI for Beginners](https://github.com/microsoft/edgeai-for-beginners) 倉庫的一部分，並遵循 [MIT 授權](../../../../LICENSE)。

---

**準備好構建生產級的 Edge AI 應用程式了嗎？**  
**從 [Session 01: 聊天啟動](./session01_chat_bootstrap.ipynb) 開始 →**

---

*最後更新日期: 2025 年 10 月 8 日 | 工作坊版本: 2.0*

---

**免責聲明**：  
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。我們致力於提供準確的翻譯，但請注意，自動翻譯可能包含錯誤或不準確之處。應以原文文件作為權威來源。對於關鍵資訊，建議尋求專業人工翻譯。我們對因使用本翻譯而引起的任何誤解或誤釋不承擔責任。
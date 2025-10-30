<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "78ca68df03ae43371b203ea43d346dec",
  "translation_date": "2025-10-30T11:20:14+00:00",
  "source_file": "CHANGELOG.md",
  "language_code": "tw"
}
-->
# 更新日誌

所有與 EdgeAI for Beginners 相關的重要更新都記錄於此。本專案採用基於日期的條目以及 Keep a Changelog 樣式（新增、變更、修復、移除、文件、移動）。

## 2025-10-30

### 新增 - Module06 AI Agents 全面增強
- **Microsoft Agent Framework 整合** (`Module06/01.IntroduceAgent.md`):
  - 完整介紹 Microsoft Agent Framework，用於開發生產級代理
  - 詳細的 Foundry Local 與邊緣部署整合模式
  - 使用專門的 SLM 模型進行多代理協作範例
  - 企業部署模式，包括資源管理與監控
  - 邊緣代理系統的安全性與合規性功能
  - 真實案例實施範例（零售、醫療、客戶服務）

- **生產級 SLM 代理部署策略**：
  - **Foundry Local**：完整的企業級邊緣 AI 運行時文件，包括安裝、配置和生產模式
  - **Ollama**：增強的社群導向部署，包含全面的監控與模型管理
  - **VLLM**：高效能推理引擎，具備先進的優化技術與企業功能
  - 生產部署檢查清單及三個平台的比較表

- **邊緣優化 SLM 框架增強**：
  - **ONNX Runtime**：新增跨平台 SLM 代理部署的完整章節
  - 通用部署模式，涵蓋 Windows、Linux、macOS、iOS 和 Android
  - 硬體加速選項（CPU、GPU、NPU），具備自動檢測功能
  - 生產級功能與代理專屬優化
  - 完整的實施範例，包含 Microsoft Agent Framework 整合

- **參考資料與進一步閱讀**：
  - 包含超過 100 個權威資源的綜合資源庫
  - 關於 AI 代理和小型語言模型的核心研究論文
  - 所有主要框架和工具的官方文件
  - 行業報告、市場分析和技術基準
  - 教育資源、會議和社群論壇
  - 標準、規範和合規框架

### 變更 - Module06 內容現代化
- **增強學習目標**：新增 Microsoft Agent Framework 精通與邊緣部署能力
- **生產導向**：從概念轉向實施準備的指導，包含生產範例
- **程式碼範例**：更新所有範例以使用現代 SDK 模式和最佳實踐
- **架構模式**：新增分層代理架構和邊緣到雲端協作
- **效能優化**：增強資源管理和自動擴展建議

### 文件 - Module06 結構增強
- **全面的代理框架覆蓋**：從基本概念到企業部署
- **生產部署策略**：Foundry Local、Ollama 和 VLLM 的完整指南
- **跨平台優化**：新增 ONNX Runtime 用於通用部署
- **資源庫**：廣泛的參考資料，用於持續學習和實施

### 新增 - Module06 Model Context Protocol (MCP) 文件更新
- **MCP 介紹現代化** (`Module06/03.IntroduceMCP.md`):
  - 更新至 modelcontextprotocol.io 的最新 MCP 規範（2025-06-18 版本）
  - 新增官方 USB-C 類比，用於標準化 AI 應用程式連接
  - 更新架構章節，包含官方的雙層設計（資料層 + 傳輸層）
  - 增強核心原語文件，包含伺服器原語（工具、資源、提示）和客戶端原語（取樣、引導、記錄）

- **全面的 MCP 參考資料與資源**：
  - 新增 **MCP for Beginners** 連結 (https://aka.ms/mcp-for-beginners)
  - 官方 MCP 文件與規範 (modelcontextprotocol.io)
  - 開發資源，包括 MCP Inspector 和參考實現
  - 技術標準（JSON-RPC 2.0、JSON Schema、OpenAPI、Server-Sent Events）

### 新增 - Module04 Qualcomm QNN 整合
- **新增第 7 節：Qualcomm QNN 優化套件** (`Module04/05.QualcommQNN.md`):
  - 涵蓋 Qualcomm 統一 AI 推理框架的完整 400+ 行指南
  - 詳細介紹異構計算（Hexagon NPU、Adreno GPU、Kryo CPU）
  - 針對 Snapdragon 平台的硬體感知優化，具備智能工作負載分配
  - 先進的量化技術（INT8、INT16、混合精度），用於移動部署
  - 用於電池供電設備和即時應用的高效能推理優化
  - 包含 QNN SDK 安裝和環境配置的完整指南
  - 實用範例：PyTorch 到 QNN 轉換、多後端優化、上下文二進制生成
  - 高級使用模式：自定義後端配置、動態量化、效能分析
  - 全面的故障排除章節和社群資源

- **增強 Module04 結構**：
  - 更新 README.md，包含 7 個漸進式章節（原為 6 個）
  - 在效能基準表中新增 Qualcomm QNN（5-15 倍速度提升，50-80% 記憶體減少）
  - 增強移動 AI 部署和功耗優化的學習成果

### 變更 - Module04 文件更新
- **Microsoft Olive 文件增強** (`Module04/03.MicrosoftOlive.md`):
  - 新增全面的 "Olive Recipes Repository" 章節，涵蓋 100+ 預建優化方案
  - 詳細介紹支援的模型系列（Phi、Llama、Qwen、Gemma、Mistral、DeepSeek）
  - 實用範例，用於方案自定義和社群貢獻
  - 增強效能基準和整合指導

- **Module04 章節重新排序**：
  - Apple MLX 移至第 5 節（原為第 6 節）
  - Workflow Synthesis 移至第 6 節（原為第 7 節）
  - Qualcomm QNN 定位為第 7 節（專注於移動/邊緣）
  - 更新所有文件參考和導航連結

### 修復 - 工作坊範例驗證
- **chat_bootstrap.py 驗證與修復**：
  - 修復損壞的匯入語句 (`util.util.workshop_utils` → `util.workshop_utils`)
  - 在 util 套件中建立缺失的 `__init__.py`，以正確解析 Python 模組
  - 在 conda 環境中安裝所需的依賴項（openai、foundry-local-sdk）
  - 成功驗證範例執行，包含預設和自定義提示
  - 確認與 Foundry Local 服務的整合以及模型加載（phi-4-mini，使用 CUDA 優化）

### 文件 - 全面指南更新
- **Module04 README.md 完整重構**：
  - 新增 Qualcomm QNN 作為主要優化框架，與 OpenVINO、Olive、MLX 並列
  - 更新章節學習成果，包含移動 AI 部署和功耗優化
  - 增強效能比較表，包含 QNN 指標和移動/邊緣使用案例
  - 保持從企業解決方案到平台專屬優化的邏輯進程

- **交叉參考與導航**：
  - 更新所有內部連結和文件參考，適應新章節編號
  - 增強工作流程綜合描述，包含移動、桌面和雲端環境
  - 新增 Qualcomm 開發者生態系統的全面資源連結

## 2025-10-08

### 新增 - 工作坊全面更新
- **工作坊 README.md 完整重寫**：
  - 新增全面介紹，解釋 Edge AI 的價值主張（隱私、效能、成本）
  - 建立 6 個核心學習目標，包含詳細能力
  - 新增學習成果表，包含交付物和能力矩陣
  - 包含行業相關的職業技能部分
  - 新增快速入門指南，包含先決條件和 3 步設置
  - 建立資源表，用於 Python 範例（8 個文件及執行時間）
  - 新增 Jupyter 筆記本表（8 個筆記本及難度評級）
  - 建立文件表（7 個關鍵文件及 "使用時機" 指導）
  - 新增不同技能水平的學習路徑建議

- **工作坊驗證與測試基礎設施**：
  - 建立 `scripts/validate_samples.py` - 用於語法、匯入和最佳實踐的全面驗證工具
  - 建立 `scripts/test_samples.py` - 用於所有 Python 範例的煙霧測試執行器
  - 新增驗證文件至 `scripts/README.md`

- **全面文件**：
  - 建立 `SAMPLES_UPDATE_SUMMARY.md` - 400+ 行詳細指南，涵蓋所有改進
  - 建立 `UPDATE_COMPLETE.md` - 更新完成的執行摘要
  - 建立 `QUICK_REFERENCE.md` - 工作坊的快速參考卡

### 變更 - 工作坊 Python 範例現代化
- **所有 8 個 Python 範例更新至最佳實踐**：
  - 增強錯誤處理，於所有 I/O 操作周圍加入 try-except 塊
  - 新增型別提示和全面的文件字符串
  - 實施一致的 [INFO]/[ERROR]/[RESULT] 日誌模式
  - 使用安裝提示保護可選匯入
  - 改善所有範例中的使用者反饋

- **session01/chat_bootstrap.py**：
  - 增強客戶端初始化，提供全面的錯誤訊息
  - 改善流式錯誤處理，加入塊驗證
  - 新增服務不可用的更佳例外處理

- **session02/rag_pipeline.py**：
  - 為 sentence-transformers 的匯入加入保護，並提供安裝提示
  - 增強嵌入和生成操作的錯誤處理
  - 改善輸出格式，提供結構化結果

- **session02/rag_eval_ragas.py**：
  - 保護可選匯入（ragas、datasets），提供使用者友好的錯誤訊息
  - 新增評估指標的錯誤處理
  - 增強評估結果的輸出格式

- **session03/benchmark_oss_models.py**：
  - 實施優雅降級（在模型失敗時繼續執行）
  - 新增詳細的進度報告和逐模型錯誤處理
  - 增強統計計算，提供全面的錯誤恢復

- **session04/model_compare.py**：
  - 新增型別提示（Tuple 返回型別）
  - 改善輸出格式，提供結構化 JSON 結果
  - 實施逐模型錯誤處理，具備恢復功能

- **session05/agents_orchestrator.py**：
  - 增強 Agent.act()，提供全面的文件字符串
  - 新增管道錯誤處理，具備逐階段日誌記錄
  - 改善記憶體管理與狀態追蹤

- **session06/models_router.py**：
  - 增強所有路由元件的函數文件
  - 在 route() 函數中新增詳細日誌記錄
  - 改善測試輸出，提供結構化結果

- **session06/models_pipeline.py**：
  - 新增 chat() 輔助函數的錯誤處理
  - 增強 pipeline()，具備階段日誌記錄與進度報告
  - 改善 main()，提供全面的錯誤恢復

### 文件 - 工作坊文件增強
- 更新主 README.md，新增工作坊部分，突顯實踐學習路徑
- 增強 STUDY_GUIDE.md，新增全面的工作坊部分，包括：
  - 學習目標與學習重點領域
  - 自我評估問題
  - 實踐練習及時間估算
  - 集中與兼職學習的時間分配
  - 新增工作坊至進度追蹤模板
- 更新時間分配指南，從 20 小時增至 30 小時（包含工作坊）
- 新增工作坊範例描述及學習成果至 README

### 修復
- 解決工作坊範例中不一致的錯誤處理模式
- 修復可選依賴匯入錯誤，加入適當的保護
- 修正關鍵函數中缺失的型別提示
- 解決錯誤場景中使用者反饋不足的問題
- 修復驗證問題，加入全面的測試基礎設施

---

## 2025-09-23

### 變更 - Module 08 重大現代化
- **全面對齊 Microsoft Foundry-Local 儲存庫模式**：
  - 更新所有程式碼範例，使用現代 `FoundryLocalManager` 和 OpenAI SDK 整合
  - 用正確的 SDK 使用取代過時的手動 `requests` 呼叫
  - 將實施模式與官方 Microsoft 文件和範例對齊

- **05.AIPoweredAgents.md 現代化**：
  - 更新多代理協作，使用現代 SDK 模式
  - 增強協調器實施，加入高級功能（反饋迴路、效能監控）
  - 新增全面的錯誤處理與服務健康檢查
  - 正確整合本地範例（`samples/05/multi_agent_orchestration.ipynb`）
  - 更新函數調用範例，使用現代 `tools` 參數取代過時的 `functions`
  - 新增生產級模式，具備監控與統計追蹤

- **06.ModelsAsTools.md 完整重寫**：
  - 用智能模型路由器實施取代基本工具註冊
  - 新增基於關鍵字的模型選擇，用於不同任務類型（通用、推理、程式碼、創意）
  - 整合基於環境的配置，具備靈活的模型分配
  - 增強服務健康監控與錯誤處理
  - 新增生產部署模式，具備請求監控與效能追蹤
  - 與本地實施對齊（`samples/06/router.py` 和 `samples/06/model_router.ipynb`）

- **文件結構改進**：
  - 新增概述章節，突顯現代化與 SDK 對齊
  - 增強格式，加入表情符號，提升可讀性
  - 新增本地範例文件的正確參考
  - 包含生產級實施指導與最佳實踐

### 新增
- Module 08 文件中的全面概述章節，突顯現代 SDK 整合
- 架構亮點，展示高級功能（多代理系統、智能路由）
- 直接參考本地範例實施，用於實踐經驗
- 生產部署指導，具備監控與錯誤處理模式
- 互動式 Jupyter 筆記本範例，具備高級功能與基準測試

### 修復
- 文件與實際範例實施之間的對齊差異
- Module 08 中過時的 SDK 使用模式
- 缺失全面的本地範例庫參考
- 不一致的實施方法，跨不同章節

---

## 2025-09-18

### 新增
- Module 08: Microsoft Foundry Local – 完整開發者工具包
  - 六個課程：設置、Azure AI Foundry 整合、開源模型、尖端演示、代理和模型作為工具
  - 可執行範例位於 `Module08/samples/01`–`06`，附有 Windows cmd 指令
    - `01` REST 快速聊天 (`chat_quickstart.py`)
    - `02` SDK 快速入門，支援 OpenAI/Foundry Local 和 Azure OpenAI (`sdk_quickstart.py`)
    - `03` CLI 列表與基準測試 (`list_and_bench.cmd`)
    - `04` Chainlit 示範 (`app.py`)
    - `05` 多代理協作 (`python -m samples.05.agents.coordinator`)
    - `06` 模型作為工具的路由器 (`router.py`)
- Session 2 SDK 範例中支援 Azure OpenAI，並透過環境變數進行配置
- `.vscode/settings.json` 指向 `Module08/.venv`，以改善 Python 分析解析
- `.env` 提供 `PYTHONPATH` 提示，增強 VS Code/Pylance 的辨識能力

### 已更改
- Module 08 文件和範例中的預設模型更新為 `phi-4-mini`，移除了剩餘的 `phi-3.5` 提及
- 路由器 (`Module08/samples/06/router.py`) 改進：
  - 通過 `foundry service status` 進行端點發現，並使用正則表達式解析
  - 啟動時進行 `/v1/models` 健康檢查
  - 可通過環境變數配置的模型註冊表 (`GENERAL_MODEL`, `REASONING_MODEL`, `CODE_MODEL`, `TOOL_REGISTRY` JSON)
- 更新需求：`Module08/requirements.txt` 現已包含 `openai`（與 `requests`、`chainlit` 一同列入）
- 明確了 Chainlit 範例指導並新增故障排除；透過工作區設定解決導入問題

### 已修復
- 解決了導入問題：
  - 路由器不再依賴不存在的 `utils` 模組；功能已內嵌
  - 協調器使用相對導入 (`from .specialists import ...`)，並通過模組路徑調用
  - VS Code/Pylance 配置以解決 `chainlit` 和套件導入問題
- 修正了 `STUDY_GUIDE.md` 中的小錯字，並新增 Module 08 的涵蓋範圍

### 已移除
- 刪除了未使用的 `Module08/infra/obs.py`，並移除了空的 `infra/` 目錄；觀察性模式作為可選項保留在文件中

### 已移動
- 將 Module 08 示範統一整合至 `Module08/samples`，並按會話編號分文件夾
  - 將 Chainlit 應用移至 `samples/04`
  - 將代理移至 `samples/05`，並新增 `__init__.py` 文件以解決套件解析問題

### 文件
- Module 08 會話文件及所有範例 README 增加了 Microsoft Learn 和可信供應商的參考資料
- 更新了 `Module08/README.md`，新增範例概述、路由器配置及驗證提示
- 驗證了 `Module07/README.md` 中的 Windows Foundry Local 部分，與 Learn 文件一致
- 更新了 `STUDY_GUIDE.md`：
  - 在概述、時間表、進度追蹤中新增 Module 08
  - 增加了全面的參考資料部分（Foundry Local、Azure AI、Olive、ONNX Runtime、OpenVINO、MLX、Llama.cpp、vLLM、Ollama、AI Toolkit、Windows ML）

---

## 歷史（摘要）
- 建立課程架構和模組（Modules 01–07）
- 持續進行內容現代化、格式標準化，並新增案例研究
- 擴展優化框架涵蓋範圍（Llama.cpp、Olive、OpenVINO、Apple MLX）

## 未發布 / 待辦事項（提案）
- 為每個範例新增可選的煙霧測試，以驗證 Foundry Local 的可用性
- 審查翻譯以確保模型參考（例如 `phi-4-mini`）一致
- 如果團隊偏好工作區範圍的嚴格性，則新增最小的 pyright 配置

---

**免責聲明**：  
本文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。儘管我們致力於提供準確的翻譯，請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於關鍵信息，建議使用專業人工翻譯。我們對因使用此翻譯而產生的任何誤解或錯誤解釋不承擔責任。
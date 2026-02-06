# EdgeAI 初學者指南


![課程封面](../../translated_images/zh-MO/cover.eb18d1b9605d754b.webp)

[![GitHub 貢獻者](https://img.shields.io/github/contributors/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/graphs/contributors)
[![GitHub 問題](https://img.shields.io/github/issues/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/issues)
[![GitHub 拉取請求](https://img.shields.io/github/issues-pr/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/pulls)
[![歡迎 PR](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

[![GitHub 觀察者](https://img.shields.io/github/watchers/microsoft/edgeai-for-beginners.svg?style=social&label=Watch)](https://GitHub.com/microsoft/edgeai-for-beginners/watchers)
[![GitHub 派生](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork)
[![GitHub 星標](https://img.shields.io/github/stars/microsoft/edgeai-for-beginners?style=social&label=Star)](https://GitHub.com/microsoft/edgeai-for-beginners/stargazers)


[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

跟隨以下步驟開始使用這些資源：

1. **分支此儲存庫 (Fork the Repository)**：點擊 [![GitHub 派生](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork)
2. **克隆儲存庫 (Clone the Repository)**：`git clone https://github.com/microsoft/edgeai-for-beginners.git`
3. [**加入 Azure AI Foundry Discord，與專家及開發者交流**](https://discord.com/invite/ByRwuEEgH4)


### 🌐 多語言支援

#### 透過 GitHub Actions 支援 (自動且保持最新)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[阿拉伯語](../ar/README.md) | [孟加拉語](../bn/README.md) | [保加利亞語](../bg/README.md) | [緬甸語（Myanmar）](../my/README.md) | [中文（簡體）](../zh-CN/README.md) | [中文（繁體，香港）](../zh-HK/README.md) | [中文（繁體，澳門）](./README.md) | [中文（繁體，台灣）](../zh-TW/README.md) | [克羅地亞語](../hr/README.md) | [捷克語](../cs/README.md) | [丹麥語](../da/README.md) | [荷蘭語](../nl/README.md) | [愛沙尼亞語](../et/README.md) | [芬蘭語](../fi/README.md) | [法語](../fr/README.md) | [德語](../de/README.md) | [希臘語](../el/README.md) | [希伯來語](../he/README.md) | [印地語](../hi/README.md) | [匈牙利語](../hu/README.md) | [印度尼西亞語](../id/README.md) | [意大利語](../it/README.md) | [日語](../ja/README.md) | [卡納達語](../kn/README.md) | [韓語](../ko/README.md) | [立陶宛語](../lt/README.md) | [馬來語](../ms/README.md) | [馬拉雅拉姆語](../ml/README.md) | [馬拉地語](../mr/README.md) | [尼泊爾語](../ne/README.md) | [奈及利亞皮欽語](../pcm/README.md) | [挪威語](../no/README.md) | [波斯語 (Farsi)](../fa/README.md) | [波蘭語](../pl/README.md) | [葡萄牙語 (巴西)](../pt-BR/README.md) | [葡萄牙語 (葡萄牙)](../pt-PT/README.md) | [旁遮普語 (Gurmukhi)](../pa/README.md) | [羅馬尼亞語](../ro/README.md) | [俄語](../ru/README.md) | [塞爾維亞語 (西里爾字母)](../sr/README.md) | [斯洛伐克語](../sk/README.md) | [斯洛文尼亞語](../sl/README.md) | [西班牙語](../es/README.md) | [斯瓦希里語](../sw/README.md) | [瑞典語](../sv/README.md) | [塔加洛語 (菲律賓語)](../tl/README.md) | [泰米爾語](../ta/README.md) | [泰盧固語](../te/README.md) | [泰語](../th/README.md) | [土耳其語](../tr/README.md) | [烏克蘭語](../uk/README.md) | [烏爾都語](../ur/README.md) | [越南語](../vi/README.md)

> **偏好本地克隆？**

> 此儲存庫包含 50 多種語言翻譯，會大幅增加下載大小。若想在不下載翻譯的情況下進行克隆，請使用稀疏檢出：
> ```bash
> git clone --filter=blob:none --sparse https://github.com/microsoft/edgeai-for-beginners.git
> cd edgeai-for-beginners
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
> 這將提供你完成課程所需的一切，同時加快下載速度。
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

**如希望支援更多翻譯語言，清單請見 [這裡](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md)**
## 簡介

歡迎來到 **EdgeAI 初學者指南** — 這是你踏入邊緣人工智能 (Edge AI) 變革世界的完整旅程。此課程銜接強大 AI 能力與邊緣裝置的實際部署，讓你能直接於數據產生及決策發生的場域使用 AI 的潛能。

### 你將掌握的技能

本課程將引領你從基礎概念到可投入生產環境的實作，涵蓋：
- 為邊緣部署優化的 **小型語言模型 (SLMs)**
- 跨多種平臺的 **硬體感知優化**
- 支援隱私保護的 **即時推論**
- 適用企業應用的 **生產部署策略**

### 為什麼 EdgeAI 重要

Edge AI 是應對現代關鍵挑戰的範式轉變：
- **隱私與安全**：敏感資料在本地處理，避免上傳雲端
- **即時性能**：消除網路延遲，適用時間關鍵的應用
- **成本效益**：減少頻寬及雲端運算開銷
- **韌性運作**：網路斷線時仍保持功能
- **法規遵循**：滿足數據主權要求

### Edge AI 是什麼

Edge AI 指在硬體裝置（資料產生端附近）本地執行 AI 演算法及語言模型，而非依賴雲端資源來進行推論。它減少延遲、強化隱私，並實現即時決策。

### 核心原則：
- **裝置內推論**：AI 模型於邊緣裝置運行（手機、路由器、微控制器、工業電腦）
- **離線功能**：無需持續網絡連線即可運作
- **低延遲**：即時回應，適用於即時系統
- **數據主權**：敏感資訊保留於本地，提升安全與合規性

### 小型語言模型 (SLMs)

如 Phi-4、Mistral-7B 和 Gemma 等 SLM，是大型 LLMs 的優化版本，透過訓練或蒸餾來實現：
- **降低記憶體占用**：有效利用有限的邊緣裝置記憶體
- **減少運算需求**：優化 CPU 與邊緣 GPU 性能
- **更快啟動時間**：迅速初始化以提供即時回應

它們解鎖強大自然語言處理能力，同時適應以下限制：
- **嵌入式系統**：物聯網裝置與工業控制器
- **行動裝置**：具備離線功能的智慧手機和平板
- **物聯網設備**：資源有限的感測器與智慧裝置
- **邊緣伺服器**：有限 GPU 資源的本地運算單元
- **個人電腦**：桌機及筆電的部署場景

## 課程模組與導航

| 模組 | 主題 | 焦點領域 | 主要內容 | 等級 | 時長 |
|--------|-------|------------|-------------|--------|----------|
| [📖 00 ](./introduction.md) | [EdgeAI 簡介](./introduction.md) | 基礎與背景 | EdgeAI 概覽 • 產業應用 • SLM 簡介 • 學習目標 | 初學者 | 1-2 小時 |
| [📚 01](../../Module01) | [EdgeAI 基礎](./Module01/README.md) | 雲端與邊緣 AI 比較 | EdgeAI 基礎 • 真實案例研究 • 實作指南 • 邊緣部署 | 初學者 | 3-4 小時 |
| [🧠 02](../../Module02) | [SLM 模型基礎](./Module02/README.md) | 模型家族與架構 | Phi 家族 • Qwen 家族 • Gemma 家族 • BitNET • μModel • Phi-Silica | 初學者 | 4-5 小時 |
| [🚀 03](../../Module03) | [SLM 部署實作](./Module03/README.md) | 本地與雲端部署 | 進階學習 • 本地環境 • 雲端部署 | 中階 | 4-5 小時 |
| [⚙️ 04](../../Module04) | [模型優化工具箱](./Module04/README.md) | 跨平台優化 | 介紹 • Llama.cpp • Microsoft Olive • OpenVINO • Apple MLX • 工作流程合成 | 中階 | 5-6 小時 |
| [🔧 05](../../Module05) | [SLMOps 生產環境](./Module05/README.md) | 生產運營 | SLMOps 介紹 • 模型蒸餾 • 微調 • 生產部署 | 進階 | 5-6 小時 |
| [🤖 06](../../Module06) | [AI Agent 與函數調用](./Module06/README.md) | Agent 框架與 MCP | Agent 介紹 • 函數呼叫 • 模型上下文協定 | 進階 | 4-5 小時 |
| [💻 07](../../Module07) | [平臺實作](./Module07/README.md) | 跨平台範例 | AI 工具箱 • Foundry Local • Windows 開發 | 進階 | 3-4 小時 |
| [🏭 08](../../Module08) | [Foundry Local 工具箱](./Module08/README.md) | 生產準備範例 | 範例應用（詳情見下方） | 專家 | 8-10 小時 |

### 🏭 **模組 08：範例應用**

- [01: REST Chat 快速入門](./Module08/samples/01/README.md)
- [02: OpenAI SDK 整合](./Module08/samples/02/README.md)
- [03: 模型發現與基準測試](./Module08/samples/03/README.md)
- [04: Chainlit RAG 應用](./Module08/samples/04/README.md)
- [05: 多 Agent 協調](./Module08/samples/05/README.md)
- [06: Models-as-Tools 路由器](./Module08/samples/06/README.md)
- [07: 直接 API 用戶端](./Module08/samples/07/README.md)
- [08: Windows 11 聊天應用](./Module08/samples/08/README.md)
- [09: 進階多 Agent 系統](./Module08/samples/09/README.md)
- [10: Foundry 工具框架](./Module08/samples/10/README.md)

### 🎓 **工作坊：實作學習路徑**

完整的實作工作坊材料，包含生產級實作：

- **[工作坊指南](./Workshop/Readme.md)** - 完整的學習目標、成果與資源導航
- **Python 範例**（6 節） - 更新最佳實踐、錯誤處理及完整文件
- **Jupyter 筆記本**（8 節互動式） - 分步教學附基準測試和性能監控
- **課程指導** - 每堂工作坊課程詳盡的 Markdown 指南
- **驗證工具** - 用於檢驗程式碼品質及執行煙霧測試的腳本

**你將建置：**
- 支援串流的本地 AI 聊天應用
- 搭配質量評估的 RAG 流程（RAGAS）
- 多模型的基準與比較工具
- 多 Agent 協調系統
- 智能模型路由與任務選擇

### 🎙️ **Agentic 工作坊：實作 - AI 播客製作室**

從零開始建構一個由 AI 推動的播客製作流程！此沉浸式工作坊將教你建立完整的多 Agent 系統，把創意轉化為專業播客節目。
**[🎬 開始 AI 播客工作室工作坊](./WorkshopForAgentic/README.md)**

**你的任務**：啟動「Future Bytes」— 一個完全由你自行建構的 AI 代理驅動的科技播客。無需雲端依賴，無 API 費用 — 一切均在本機執行。

**獨特之處：**
- **🤖 真正的多代理協調** — 建立專門的 AI 代理進行研究、撰寫和音訊製作
- **🎯 完整製作流程** — 從主題選擇到最終播客音訊輸出
- **💻 100% 本地部署** — 使用 Ollama 和本地模型（Qwen-3-8B）保障隱私與掌控
- **🎤 文字轉語音整合** — 將腳本轉換為自然多說者對話
- **✋ 人工審核流程** — 審批關卡保證品質，同時維持自動化

**三幕學習旅程：**

| 幕 | 重點 | 主要技能 | 時長 |
|-----|-------|------------|----------|
| **[幕 1：認識你的 AI 助手](./WorkshopForAgentic/md/01.BuildAIAgentWithSLM.md)** | 建立你的第一個 AI 代理 | 工具整合 • 網絡搜索 • 問題解決 • 代理推理 | 2-3 小時 |
| **[幕 2：組建你的製作團隊](./WorkshopForAgentic/md/02.AIAgentOrchestrationAndWorkflows.md)** | 多代理協調 | 團隊協作 • 審批工作流程 • DevUI 介面 • 人工監督 | 3-4 小時 |
| **[幕 3：讓你的播客活起來](./WorkshopForAgentic/md/03.Multi-SpeakerPodcastGenerationWithVibeVoice.md)** | 產生播客音訊 | 文字轉語音 • 多說者合成 • 長格式音訊 • 完全自動化 | 2-3 小時 |

**使用技術：**
- **Microsoft 代理框架** — 多代理編排與協調
- **Ollama** — 本地 AI 模型運行時（無需雲端）
- **Qwen-3-8B** — 為代理任務優化的開源語言模型
- **文字轉語音 API** — 用於播客生成的自然語音合成

**硬件支援：**
- ✅ **CPU 模式** — 適用於任何現代電腦（建議 8GB+ 記憶體）
- 🚀 **GPU 加速** — NVIDIA/AMD GPU 顯著加快推理速度
- ⚡ **NPU 支援** — 下一代神經處理單元加速

**適合對象：**
- 學習多代理 AI 系統的開發者
- 有興趣 AI 自動化與工作流程的人士
- 探索 AI 輔助製作的內容創作者
- 學習實務 AI 編排模式的學生

**立即開始**：[🎙️ AI 播客工作室工作坊 →](./WorkshopForAgentic/README.md)

### 📊 **學習路徑總結**
- **總時長**：36-45 小時
- **初學者路徑**：模組 01-02（7-9 小時）  
- **中級路徑**：模組 03-04（9-11 小時）
- **進階路徑**：模組 05-07（12-15 小時）
- **專家路徑**：模組 08（8-10 小時）

## 你將學會

### 🎯 核心能力
- **Edge AI 架構**：設計以本地為先的 AI 系統並結合雲端
- **模型優化**：模型量化與壓縮以實現邊緣部署（速度提升 85%，體積縮減 75%）
- **跨平台部署**：Windows、手機、嵌入式與雲邊混合系統
- **生產運營**：邊緣 AI 監控、擴展及維護

### 🏗️ 實務專案
- **Foundry 本地聊天應用**：Windows 11 原生應用並支援模型切換
- **多代理系統**：協調員與專家代理用於複雜工作流程  
- **RAG 應用**：本地文件處理與向量檢索
- **模型路由器**：基於任務分析智能選擇模型
- **API 框架**：具備串流與健康監控的生產級客戶端
- **跨平台工具**：LangChain/Semantic Kernel 整合範例

### 🏢 產業應用
**製造業** • **醫療健康** • **自動駕駛** • **智慧城市** • **移動應用**

## 快速開始

**推薦學習路徑**（總計 20-30 小時）：

0. **📖 介紹** ([Introduction.md](./introduction.md))：EdgeAI 基礎 + 產業背景 + 學習架構
1. **📚 基礎**（模組 01-02）：EdgeAI 概念 + SLM 模型系列
2. **⚙️ 優化**（模組 03-04）：部署 + 量化框架  
3. **🚀 生產**（模組 05-06）：SLMOps + AI 代理 + 函數調用
4. **💻 實作**（模組 07-08）：平台範例 + Foundry 本地工具包

每個模組均包含理論、實作練習與生產級範例程式碼。

## 職涯影響

**技術職務**：EdgeAI 解決方案架構師 • 邊緣 ML 工程師 • 物聯網 AI 開發者 • 行動 AI 開發者

**產業領域**：製造業 4.0 • 醫療科技 • 自動系統 • 金融科技 • 消費電子

**作品集專案**：多代理系統 • 生產 RAG 應用 • 跨平台部署 • 效能優化

## 倉庫結構

```
edgeai-for-beginners/
├── 📖 introduction.md  # Foundation: EdgeAI Overview & Learning Framework
├── 📚 Module01-04/     # Fundamentals → SLMs → Deployment → Optimization  
├── 🔧 Module05-06/     # SLMOps → AI Agents → Function Calling
├── 💻 Module07/        # Platform Samples (VS Code, Windows, Jetson, Mobile)
├── 🏭 Module08/        # Foundry Local Toolkit + 10 Comprehensive Samples
│   ├── samples/01-06/  # Foundation: REST, SDK, RAG, Agents, Routing
│   └── samples/07-10/  # Advanced: API Client, Windows App, Enterprise Agents, Tools
├── 🌐 translations/    # Multi-language support (8+ languages)
└── 📋 STUDY_GUIDE.md   # Structured learning paths & time allocation
```

## 課程重點

✅ **循序漸進學習**：理論 → 實務 → 生產部署  
✅ **真實案例研究**：微軟、日本航空、企業實施  
✅ **實作範例豐富**：50+ 範例，10 個完整 Foundry 本地演示  
✅ **性能優化**：速度提升 85%，體積縮減 75%  
✅ **跨平台適用**：Windows、手機、嵌入式、雲邊混合  
✅ **生產準備**：監控、擴展、安全、合規框架

📖 **[學習指南](STUDY_GUIDE.md)**：20 小時結構化路徑，含時間分配指導與自評工具。

---

**EdgeAI 代表 AI 部署的未來**：本地優先、保護隱私且高效。在此掌握技能，打造下一代智慧應用。

## 其他課程

我們團隊還製作其他課程！歡迎查看：

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j for Beginners](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js for Beginners](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)
[![LangChain for Beginners](https://img.shields.io/badge/LangChain%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://github.com/microsoft/langchain-for-beginners?WT.mc_id=m365-94501-dwahlin)
---

### Azure / Edge / MCP / Agents
[![AZD for Beginners](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Edge AI for Beginners](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP for Beginners](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![AI Agents for Beginners](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### 生成式 AI 系列
[![Generative AI for Beginners](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Generative AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![Generative AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![Generative AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### 核心學習
[![ML for Beginners](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![Data Science for Beginners](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![AI for Beginners](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![Cybersecurity for Beginners](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![Web Dev for Beginners](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![IoT for Beginners](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![XR Development for Beginners](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Copilot 系列
[![Copilot for AI Paired Programming](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot for C#/.NET](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot Adventure](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## 尋求協助

如果你遇到困難或有關於建立 AI 應用程序的任何問題，歡迎加入：

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

如果你在建置過程中有產品反饋或錯誤，請訪問：

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。儘管我們致力於準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件之母語版本應視為權威來源。對於重要資訊，建議採用專業人工翻譯。因使用本翻譯所引致之任何誤解或誤釋，我們概不負責。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
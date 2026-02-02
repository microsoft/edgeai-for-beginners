# EdgeAI 初學者指南


![Course cover image](../../translated_images/zh-HK/cover.eb18d1b9605d754b.webp)

[![GitHub contributors](https://img.shields.io/github/contributors/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/graphs/contributors)
[![GitHub issues](https://img.shields.io/github/issues/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/issues)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/pulls)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

[![GitHub watchers](https://img.shields.io/github/watchers/microsoft/edgeai-for-beginners.svg?style=social&label=Watch)](https://GitHub.com/microsoft/edgeai-for-beginners/watchers)
[![GitHub forks](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork)
[![GitHub stars](https://img.shields.io/github/stars/microsoft/edgeai-for-beginners?style=social&label=Star)](https://GitHub.com/microsoft/edgeai-for-beginners/stargazers)


[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

請依照以下步驟開始使用這些資源：

1. **Fork 本儲存庫**：點擊 [![GitHub forks](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork)
2. **Clone 本儲存庫**：   `git clone https://github.com/microsoft/edgeai-for-beginners.git`
3. [**加入 Azure AI Foundry Discord，與專家及其他開發者交流**](https://discord.com/invite/ByRwuEEgH4)


### 🌐 多語言支援

#### 透過 GitHub Action 支援（自動且即時更新）

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh-CN/README.md) | [Chinese (Traditional, Hong Kong)](./README.md) | [Chinese (Traditional, Macau)](../zh-MO/README.md) | [Chinese (Traditional, Taiwan)](../zh-TW/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../pt-BR/README.md) | [Portuguese (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

> **偏好本地克隆？**

> 本儲存庫包含50多種語言的翻譯，會大幅增加下載大小。若要不包含翻譯而使用稀疏檢出，請使用：
> ```bash
> git clone --filter=blob:none --sparse https://github.com/microsoft/edgeai-for-beginners.git
> cd edgeai-for-beginners
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
> 這將使您以更快的速度下載完成課程所有必要內容。
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

**若您希望支援更多翻譯語言，請參閱[這裡](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md)**
## 簡介

歡迎來到**EdgeAI 初學者指南**──帶您全面探索邊緣人工智能的變革世界。本課程彌合了強大AI能力與實際邊緣設備部署間的鴻溝，助力您直接在數據生成地點執行AI，實現當地即時決策。

### 你將精通的內容

本課程從基本概念引導至生產級實作，涵蓋：
- 為邊緣部署優化的**小型語言模型（SLM）**
- 跨多種平台的**硬體感知優化**
- 具備隱私保護功能的**即時推理**
- 企業應用的**生產部署策略**

### 為何 EdgeAI 重要

Edge AI 代表一種解決現代關鍵挑戰的範式轉變：
- **隱私與安全**：在本地處理敏感數據，避免雲端暴露
- **即時效能**：消除網絡延遲以適用時效性高的應用
- **成本效益**：減少頻寬與雲計算支出
- **韌性運作**：斷網時仍可維持功能
- **法規遵從**：符合資料主權要求

### 邊緣 AI

邊緣 AI 指在硬體本地即數據生成地附近運行 AI 演算法及語言模型，不依賴雲端推理。它降低延遲、提升隱私，支持即時決策。

### 核心原則：
- **裝置端推理**：AI 模型在邊緣裝置（手機、路由器、微控制器、工控機）上運行
- **離線能力**：無需持續網絡連線
- **低延遲**：即時反應，適用於即時系統
- **資料主權**：敏感資料保留於本地，提高安全與合規性

### 小型語言模型（SLM）

SLM 如 Phi-4、Mistral-7B 與 Gemma 是大型模型的精簡優化版本──訓練或蒸餾目標為：
- **降低記憶體占用**：有效利用有限的邊緣設備記憶體
- **減少運算需求**：優化 CPU 及邊緣 GPU 表現
- **更快啟動時間**：快速初始化保證響應速度

它們在滿足以下限制下，解鎖強大 NLP 功能：
- **嵌入式系統**：物聯網裝置與工業控制器
- **行動裝置**：具備離線能力的智慧手機和平板
- **物聯網裝置**：資源有限的感測器與智慧設備
- **邊緣伺服器**：有限 GPU 資源的本地處理單元
- **個人電腦**：桌面及筆記型電腦部署情境

## 課程模組與導航

| 模組 | 主題 | 專注領域 | 主要內容 | 水平 | 時長 |
|--------|-------|------------|-------------|--------|----------|
| [📖 00 ](./introduction.md) | [EdgeAI 簡介](./introduction.md) | 基礎與背景 | EdgeAI 概述 • 行業應用 • 小型語言模型介紹 • 學習目標 | 入門 | 1-2 小時 |
| [📚 01](../../Module01) | [EdgeAI 基礎](./Module01/README.md) | 雲端與邊緣 AI 比較 | EdgeAI 基礎 • 實例研究 • 實作指引 • 邊緣部署 | 入門 | 3-4 小時 |
| [🧠 02](../../Module02) | [SLM 模型基礎](./Module02/README.md) | 模型家族與架構 | Phi 系列 • Qwen 系列 • Gemma 系列 • BitNET • μModel • Phi-Silica | 入門 | 4-5 小時 |
| [🚀 03](../../Module03) | [SLM 部署實作](./Module03/README.md) | 本地與雲端部署 | 高階學習 • 本地環境 • 雲端部署 | 中階 | 4-5 小時 |
| [⚙️ 04](../../Module04) | [模型優化工具包](./Module04/README.md) | 跨平台優化 | 介紹 • Llama.cpp • Microsoft Olive • OpenVINO • Apple MLX • 工作流程合成 | 中階 | 5-6 小時 |
| [🔧 05](../../Module05) | [SLMOps 生產](./Module05/README.md) | 生產運營 | SLMOps 介紹 • 模型蒸餾 • 微調 • 生產部署 | 進階 | 5-6 小時 |
| [🤖 06](../../Module06) | [AI 代理與函數呼叫](./Module06/README.md) | 代理框架與 MCP | 代理介紹 • 函數呼叫 • 模型上下文協定 | 進階 | 4-5 小時 |
| [💻 07](../../Module07) | [平台實作](./Module07/README.md) | 跨平台範例 | AI 工具包 • Foundry Local • Windows 開發 | 進階 | 3-4 小時 |
| [🏭 08](../../Module08) | [Foundry Local 工具包](./Module08/README.md) | 生產級範例 | 範例應用程式（詳見下方） | 專家 | 8-10 小時 |

### 🏭 **模組 08：示範應用**

- [01：REST 聊天快速入門](./Module08/samples/01/README.md)
- [02：OpenAI SDK 整合](./Module08/samples/02/README.md)
- [03：模型發現與基準測試](./Module08/samples/03/README.md)
- [04：Chainlit RAG 應用](./Module08/samples/04/README.md)
- [05：多代理協調](./Module08/samples/05/README.md)
- [06：Models-as-Tools 路由器](./Module08/samples/06/README.md)
- [07：直接 API 客戶端](./Module08/samples/07/README.md)
- [08：Windows 11 聊天應用程式](./Module08/samples/08/README.md)
- [09：進階多代理系統](./Module08/samples/09/README.md)
- [10：Foundry 工具框架](./Module08/samples/10/README.md)

### 🎓 **工作坊：實作學習路徑**

綜合實作工作坊素材與生產級實作：

- **[工作坊指南](./Workshop/Readme.md)** - 完整學習目標、成果及資源導覽
- **Python 範例**（6 堂） - 採用最佳實務、錯誤處理與完整文件
- **Jupyter 筆記本**（8 互動式） - 分步教學與基準測試、效能監測
- **課程指引** - 每堂工作坊課程的詳細 Markdown 指南
- **驗證工具** - 驗證程式碼品質與執行簡易測試

**您將構建：**
- 支援串流的本地 AI 聊天應用程式
- 具質量評估的 RAG 管線（RAGAS）
- 多模型基準與比較工具
- 多代理協調系統
- 以任務為基礎的智能模型路由

### 🎙️ **Agentic 工作坊：實作 - AI 播客工作室**

從零開始打造 AI 支援的播客製作管線！此沈浸式工作坊教你創建完整多代理系統，將想法轉變成專業播客節目。
**[🎬 開始 AI Podcast Studio 工作坊](./WorkshopForAgentic/README.md)**

**你的任務**：推出「Future Bytes」— 一個完全由你自行構建的 AI 代理所驅動的科技播客。無需雲端依賴，無 API 費用 — 所有流程均在你的本機運行。

**這個項目的獨特之處：**
- **🤖 真正的多代理協調** - 建立專門的 AI 代理來進行研究、撰寫和音頻製作
- **🎯 完整製作流程** - 從主題選擇到最終播客音頻輸出
- **💻 100% 本地部署** - 使用 Ollama 及本地模型 (Qwen-3-8B)，實現完全隱私與掌控
- **🎤 文字轉語音整合** - 將腳本轉換為自然、多角色對話的語音
- **✋ 人工審核流程** - 審批關卡確保品質，同時維持自動化

**三幕學習之旅：**

| 幕 | 重點 | 主要技能 | 時長 |
|-----|-------|------------|----------|
| **[幕一：認識你的AI助手](./WorkshopForAgentic/md/01.BuildAIAgentWithSLM.md)** | 構建你的第一個 AI 代理 | 工具整合 • 網頁搜尋 • 問題解決 • 代理推理 | 2-3 小時 |
| **[幕二：組建你的製作團隊](./WorkshopForAgentic/md/02.AIAgentOrchestrationAndWorkflows.md)** | 多代理協調 | 團隊協調 • 審批流程 • DevUI 介面 • 人工監督 | 3-4 小時 |
| **[幕三：打造你的播客生命力](./WorkshopForAgentic/md/03.Multi-SpeakerPodcastGenerationWithVibeVoice.md)** | 生成播客音頻 | 文字轉語音 • 多角色合成 • 長格式音頻 • 全自動化 | 2-3 小時 |

**使用技術：**
- **Microsoft 代理框架** - 多代理編排與協調
- **Ollama** - 本地 AI 模型運行時 (不需雲端)
- **Qwen-3-8B** - 專為代理任務優化的開源語言模型
- **文字轉語音 API** - 用於自然語音合成的播客生成

**硬體支援：**
- ✅ **CPU 模式** - 適用於任何現代電腦（建議 8GB+ 記憶體）
- 🚀 **GPU 加速** - 使用 NVIDIA/AMD GPU 可大幅提高推理速度
- ⚡ **NPU 支援** - 下一代神經網路處理單元加速

**適合對象：**
- 想學習多代理 AI 系統的開發者
- 對 AI 自動化與工作流程有興趣者
- 尋求 AI 輔助製作的內容創作者
- 研究實務 AI 編排模式的學生

**開始動手**：[🎙️ AI Podcast Studio 工作坊 →](./WorkshopForAgentic/README.md)

### 📊 **學習路線摘要**
- **總時長**：36-45 小時
- **初學者路線**：模組 01-02（7-9 小時）  
- **中級路線**：模組 03-04（9-11 小時）
- **進階路線**：模組 05-07（12-15 小時）
- **專家路線**：模組 08（8-10 小時）

## 你將構建甚麼

### 🎯 核心能力
- **邊緣 AI 架構**：設計本地優先與雲端整合的 AI 系統
- **模型優化**：對模型進行量化和壓縮以進行邊緣部署（提升 85% 速度，減少 75% 尺寸）
- **多平台部署**：Windows、行動裝置、嵌入式和雲邊融合系統
- **生產運營**：監控、擴展及維護邊緣 AI 於生產環境

### 🏗️ 實作專案
- **Foundry 本地聊天應用**：Windows 11 原生應用，具模型切換功能
- **多代理系統**：協調者搭配專業代理以處理複雜工作流程  
- **RAG 應用**：本地文檔處理與向量搜尋
- **模型路由器**：根據任務分析智能選擇模型
- **API 框架**：具串流及健康監控的生產準備客戶端
- **跨平台工具**：LangChain / Semantic Kernel 整合方案

### 🏢 行業應用
**製造業** • **醫療保健** • **自駕車** • **智慧城市** • **行動應用**

## 快速開始

**推薦學習路線**（共 20-30 小時）：

0. **📖 簡介** ([Introduction.md](./introduction.md))：EdgeAI 基礎 + 行業背景 + 學習框架
1. **📚 基礎**（模組 01-02）：EdgeAI 概念 + SLM 模型家族
2. **⚙️ 優化**（模組 03-04）：部署與量化框架  
3. **🚀 生產**（模組 05-06）：SLMOps + AI 代理 + 函數調用
4. **💻 實作**（模組 07-08）：平台樣本 + Foundry 本地工具包

每個模組包含理論、實作練習與生產級範例程式碼。

## 職涯影響

**技術職位**：EdgeAI 解決方案架構師 • ML 工程師 (Edge) • 物聯網 AI 開發者 • 行動 AI 開發者

**產業領域**：製造 4.0 • 醫療技術 • 自主系統 • 金融科技 • 消費電子

**作品集專案**：多代理系統 • 生產 RAG 應用 • 跨平台部署 • 性能優化

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

## 課程亮點

✅ **漸進式學習**：理論 → 實作 → 生產部署  
✅ **真實案例研究**：微軟、日本航空、企業實作  
✅ **操作範例**：50+ 範例，10 個完整 Foundry 本地示範  
✅ **性能聚焦**：提升 85% 速度，減少 75% 尺寸  
✅ **多平台支持**：Windows、行動、嵌入式、雲邊融合  
✅ **生產準備**：監控、擴展、安全、合規框架

📖 **[學習指南](STUDY_GUIDE.md)**：結構化 20 小時學習路徑，含時間分配指引與自我評估工具。

---

**EdgeAI 代表 AI 部署的未來**：本地優先，保護隱私，高效能。掌握這些技能，打造下一代智慧應用。

## 其他課程

我們團隊還有其他課程！請查看：

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j for Beginners](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js for Beginners](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)

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

## 獲取支援

如果你遇到困難或對建立 AI 應用程式有任何疑問，請加入：

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

如果你在建立過程中有產品反饋或錯誤，請訪問：

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：  
本文件是使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯的。雖然我們努力追求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原文檔的母語版本應被視為權威來源。對於關鍵資訊，建議採用專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或曲解承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
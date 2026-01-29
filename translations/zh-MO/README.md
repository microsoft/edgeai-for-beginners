# EdgeAI 初學者指南


![課程封面圖片](../../translated_images/zh-MO/cover.eb18d1b9605d754b.webp)

[![GitHub 貢獻者](https://img.shields.io/github/contributors/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/graphs/contributors)
[![GitHub 問題](https://img.shields.io/github/issues/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/issues)
[![GitHub 拉取請求](https://img.shields.io/github/issues-pr/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/pulls)
[![歡迎 PR](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

[![GitHub 觀看者](https://img.shields.io/github/watchers/microsoft/edgeai-for-beginners.svg?style=social&label=Watch)](https://GitHub.com/microsoft/edgeai-for-beginners/watchers)
[![GitHub 分支](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork)
[![GitHub 星標](https://img.shields.io/github/stars/microsoft/edgeai-for-beginners?style=social&label=Star)](https://GitHub.com/microsoft/edgeai-for-beginners/stargazers)


[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

跟隨以下步驟開始使用這些資源：

1. **分支儲存庫**：點擊 [![GitHub 分支](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork)
2. **複製儲存庫**：   `git clone https://github.com/microsoft/edgeai-for-beginners.git`
3. [**加入 Azure AI Foundry Discord，與專家及其他開發者會面**](https://discord.com/invite/ByRwuEEgH4)


### 🌐 多語言支持

#### 透過 GitHub Action 支持（自動且始終保持更新）

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[阿拉伯語](../ar/README.md) | [孟加拉語](../bn/README.md) | [保加利亞語](../bg/README.md) | [緬甸語 (Myanmar)](../my/README.md) | [中文 (簡體)](../zh-CN/README.md) | [中文 (繁體，香港)](../zh-HK/README.md) | [中文 (繁體，澳門)](./README.md) | [中文 (繁體，台灣)](../zh-TW/README.md) | [克羅地亞語](../hr/README.md) | [捷克語](../cs/README.md) | [丹麥語](../da/README.md) | [荷蘭語](../nl/README.md) | [愛沙尼亞語](../et/README.md) | [芬蘭語](../fi/README.md) | [法語](../fr/README.md) | [德語](../de/README.md) | [希臘語](../el/README.md) | [希伯來語](../he/README.md) | [印地語](../hi/README.md) | [匈牙利語](../hu/README.md) | [印尼語](../id/README.md) | [意大利語](../it/README.md) | [日語](../ja/README.md) | [坎納達語](../kn/README.md) | [韓語](../ko/README.md) | [立陶宛語](../lt/README.md) | [馬來語](../ms/README.md) | [馬拉雅拉姆語](../ml/README.md) | [馬拉地語](../mr/README.md) | [尼泊爾語](../ne/README.md) | [奈及利亞皮欽語](../pcm/README.md) | [挪威語](../no/README.md) | [波斯語 (法爾西語)](../fa/README.md) | [波蘭語](../pl/README.md) | [葡萄牙語 (巴西)](../pt-BR/README.md) | [葡萄牙語 (葡萄牙)](../pt-PT/README.md) | [旁遮普語 (龔穆克希體)](../pa/README.md) | [羅馬尼亞語](../ro/README.md) | [俄語](../ru/README.md) | [塞爾維亞語 (西里爾字母)](../sr/README.md) | [斯洛伐克語](../sk/README.md) | [斯洛文尼亞語](../sl/README.md) | [西班牙語](../es/README.md) | [斯瓦希里語](../sw/README.md) | [瑞典語](../sv/README.md) | [他加祿語 (菲律賓語)](../tl/README.md) | [泰米爾語](../ta/README.md) | [泰盧固語](../te/README.md) | [泰語](../th/README.md) | [土耳其語](../tr/README.md) | [烏克蘭語](../uk/README.md) | [烏爾都語](../ur/README.md) | [越南語](../vi/README.md)

> **想要本地複製嗎？**

> 此儲存庫包含超過 50 種語言翻譯，顯著增加了下載大小。如欲不包括翻譯內容，請使用稀疏檢出：
> ```bash
> git clone --filter=blob:none --sparse https://github.com/microsoft/edgeai-for-beginners.git
> cd edgeai-for-beginners
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
> 這樣能讓你以更快速的速度下載完成課程所需全部資源。
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

**若您希望支援其他翻譯語言，列於 [此處](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md)**
## 簡介

歡迎來到 **EdgeAI 初學者指南** —— 您進入 Edge 人工智能變革世界的全面旅程。此課程橋接了強大 AI 能力與實際、真實世界中邊緣設備部署間的鴻溝，讓您能夠直接在資料生成及決策所需之處，發揮 AI 的潛能。

### 您將掌握的內容

本課程帶您從基礎概念邁向生產級應用，涵蓋：
- **小型語言模型 (SLMs)**，針對邊緣部署做出最佳化
- **硬件感知優化**，跨多元平台
- **實時推理**，兼具隱私保護功能
- **企業級生產部署** 策略

### 為何 EdgeAI 重要

Edge AI 代表一種範式轉移，解決現代多項關鍵挑戰：
- **隱私與安全**：敏感資料本地處理，避免雲端曝露
- **實時性能**：消除針對時效性強應用的網絡延遲
- **成本效益**：減少頻寬與雲端運算支出
- **韌性運作**：網絡中斷時依然維持功能
- **符合規範**：遵守資料主權要求

### Edge AI

Edge AI 指於硬件上本地執行 AI 演算法及語言模型，靠近資料產生源，不依賴雲端資源進行推理。它能降低延遲、增強隱私，並支持實時決策。

### 核心原則：
- **裝置端推理**：AI 模型在邊緣設備（手機、路由器、微控制器、工業電腦）上運行
- **離線能力**：可在無持續網絡連接下運作
- **低延遲**：即時回應，適用於實時系統
- **資料主權**：將敏感資料保留在本地，提升安全與合規性

### 小型語言模型（SLMs）

像是 Phi-4、Mistral-7B 與 Gemma 範例的 SLM，是大型 LLMs 的最佳化版本，透過訓練或精簡以達成：
- **記憶體佔用降低**：有效利用有限邊緣設備資源
- **計算需求減少**：針對 CPU 與邊緣 GPU 優化
- **啟動速度加快**：快速初始化以達即時回應

它們在以下限制條件中解鎖強大 NLP 能力：
- **嵌入式系統**：物聯網設備及工業控制器
- **行動設備**：具離線功能的智能手機及平板
- **物聯網設備**：有限資源的感測器及智慧裝置
- **邊緣伺服器**：具有限制 GPU 資源的本地處理單元
- **個人電腦**：桌機及筆電部署場景

## 課程模組與導航

| 模組 | 主題 | 焦點區域 | 重要內容 | 難度 | 時長 |
|--------|-------|------------|-------------|--------|----------|
| [📖 00 ](./introduction.md) | [EdgeAI 簡介](./introduction.md) | 基礎與背景 | EdgeAI 概述 • 行業應用 • SLM 簡介 • 學習目標 | 初學者 | 1-2 小時 |
| [📚 01](../../Module01) | [EdgeAI 基礎](./Module01/README.md) | 雲端與邊緣 AI 比較 | EdgeAI 基礎 • 實例研究 • 實施指引 • 邊緣部署 | 初學者 | 3-4 小時 |
| [🧠 02](../../Module02) | [SLM 模型基礎](./Module02/README.md) | 模型家族與架構 | Phi 家族 • Qwen 家族 • Gemma 家族 • BitNET • μModel • Phi-Silica | 初學者 | 4-5 小時 |
| [🚀 03](../../Module03) | [SLM 部署實務](./Module03/README.md) | 本地與雲端部署 | 進階學習 • 本地環境 • 雲端部署 | 中階 | 4-5 小時 |
| [⚙️ 04](../../Module04) | [模型優化工具箱](./Module04/README.md) | 跨平台優化 | 介紹 • Llama.cpp • Microsoft Olive • OpenVINO • Apple MLX • 工作流程整合 | 中階 | 5-6 小時 |
| [🔧 05](../../Module05) | [SLMOps 生產](./Module05/README.md) | 生產運維 | SLMOps 介紹 • 模型蒸餾 • 細調 • 生產部署 | 進階 | 5-6 小時 |
| [🤖 06](../../Module06) | [AI 代理人與函式呼叫](./Module06/README.md) | 代理框架與 MCP | 代理介紹 • 函式呼叫 • 模型上下文協定 | 進階 | 4-5 小時 |
| [💻 07](../../Module07) | [平台實作](./Module07/README.md) | 跨平台範例 | AI 工具箱 • Foundry Local • Windows 開發 | 進階 | 3-4 小時 |
| [🏭 08](../../Module08) | [Foundry Local 工具箱](./Module08/README.md) | 生產級範例 | 範例應用（詳見下方） | 專家 | 8-10 小時 |

### 🏭 **模組 08：範例應用**

- [01：REST 聊天快速入門](./Module08/samples/01/README.md)
- [02：OpenAI SDK 整合](./Module08/samples/02/README.md)
- [03：模型發現與基準測試](./Module08/samples/03/README.md)
- [04：Chainlit RAG 應用](./Module08/samples/04/README.md)
- [05：多代理協同編排](./Module08/samples/05/README.md)
- [06：模型即工具路由器](./Module08/samples/06/README.md)
- [07：直接 API 用戶端](./Module08/samples/07/README.md)
- [08：Windows 11 聊天應用](./Module08/samples/08/README.md)
- [09：進階多代理系統](./Module08/samples/09/README.md)
- [10：Foundry 工具框架](./Module08/samples/10/README.md)

### 🎓 **工作坊：實作學習路徑**

全面的實戰工作坊教材，含生產級實作：

- **[工作坊指南](./Workshop/Readme.md)** — 完整學習目標、成果及資源導航
- **Python 範例**（6 堂課）— 更新最佳實踐、錯誤處理與完整文件
- **Jupyter 筆記本**（8 個互動式教學）— 逐步教學含基準測試與效能監控
- **課程指南** — 每場工作坊詳細 Markdown 指南
- **驗證工具** — 用以檢驗程式碼品質及執行煙霧測試的腳本

**您將建立：**
- 支援串流的本地 AI 聊天應用
- 具品質評估的 RAG 管線（RAGAS）
- 多模型基準測試與比較工具
- 多代理協同系統
- 智慧模型路由與任務選擇

### 🎙️ **Agentic 工作坊：實作 — AI Podcast 工作室**

從零開始建立 AI 驅動的播客製作管線！此沉浸式工作坊教您創建完整多代理系統，將構想轉化為專業播客集數。
**[🎬 開始 AI Podcast Studio 工作坊](./WorkshopForAgentic/README.md)**

**你的任務**：推出「Future Bytes」— 完全由你自己建立的 AI 代理驅動的科技播客。無需雲端依賴，無 API 成本 — 一切都在你本地機器上運行。

**獨特之處：**
- **🤖 真正的多代理協調** - 建立專門的 AI 代理來研究、撰寫和製作音頻
- **🎯 完整製作流程** - 從主題選擇到最終播客音訊輸出
- **💻 100% 本地部署** - 使用 Ollama 和本地模型（Qwen-3-8B）保障隱私和控制
- **🎤 文本轉語音整合** - 將腳本轉換成自然多講者對話
- **✋ 人類介入工作流程** - 審核關卡確保品質同時保持自動化

**三幕學習旅程：**

| 幕  | 內容焦點 | 關鍵技能 | 時長 |
|-----|-------|------------|----------|
| **[第一幕：認識你的 AI 助手](./WorkshopForAgentic/md/01.BuildAIAgentWithSLM.md)** | 建立你的第一個 AI 代理 | 工具整合 • 網路搜尋 • 問題解決 • 代理推理 | 2-3 小時 |
| **[第二幕：組建你的製作團隊](./WorkshopForAgentic/md/02.AIAgentOrchestrationAndWorkflows.md)** | 協調多個代理 | 團隊協作 • 審核流程 • DevUI 介面 • 人類監督 | 3-4 小時 |
| **[第三幕：讓你的播客成形](./WorkshopForAgentic/md/03.Multi-SpeakerPodcastGenerationWithVibeVoice.md)** | 產生播客音訊 | 文本轉語音 • 多講者合成 • 長格式音訊 • 全自動化 | 2-3 小時 |

**使用技術：**
- **Microsoft Agent Framework** - 多代理協調與配合
- **Ollama** - 本地 AI 模型運行時（無需雲端）
- **Qwen-3-8B** - 為代理任務優化的開源語言模型
- **文本轉語音 API** - 用於自然音色合成播客

**硬體支援：**
- ✅ **CPU 模式** - 適用於任何現代電腦（建議 8GB+ 記憶體）
- 🚀 **GPU 加速** - 使用 NVIDIA/AMD GPU 大幅提升推論速度
- ⚡ **NPU 支援** - 次世代神經處理單元加速

**適合對象：**
- 學習多代理 AI 系統的開發者
- 對 AI 自動化與工作流程有興趣者
- AI 輔助製作的內容創作者
- 研究實務 AI 協調範例的學生

**開始建置**: [🎙️ AI Podcast Studio 工作坊 →](./WorkshopForAgentic/README.md)

### 📊 **學習路徑總結**
- **總時長**：36-45 小時
- **初階路徑**：模組 01-02 (7-9 小時)  
- **中階路徑**：模組 03-04 (9-11 小時)
- **高階路徑**：模組 05-07 (12-15 小時)
- **專家路徑**：模組 08 (8-10 小時)

## 你將建立的內容

### 🎯 核心能力
- **邊緣 AI 架構**：設計以本地為主、雲端整合的 AI 系統
- **模型優化**：量化與壓縮模型以利邊緣部署（85% 加速，75% 縮小體積）
- **多平台部署**：Windows、行動、嵌入式及雲邊混合系統
- **生產運維**：邊緣 AI 的監控、擴展與維護

### 🏗️ 實際專案
- **Foundry 本地聊天應用**：Windows 11 原生應用，包含模型切換功能
- **多代理系統**：協調員與專家代理組成複雜工作流程  
- **RAG 應用**：本地文檔處理與向量搜尋
- **模型路由器**：基於任務分析智慧選擇模型
- **API 框架**：具備串流與健康監控的生產級客戶端
- **跨平台工具**：LangChain/Semantic Kernel 整合範式

### 🏢 產業應用
**製造業** • **醫療保健** • **自動駕駛車輛** • **智慧城市** • **行動應用程式**

## 快速開始

**建議學習路徑**（共 20-30 小時）：

0. **📖 入門** ([Introduction.md](./introduction.md))：EdgeAI 基礎 + 產業背景 + 學習架構
1. **📚 基礎**（模組 01-02）：EdgeAI 概念 + SLM 模型系列
2. **⚙️ 優化**（模組 03-04）：部署 + 量化框架  
3. **🚀 生產**（模組 05-06）：SLMOps + AI 代理 + 函式調用
4. **💻 實作**（模組 07-08）：平台範例 + Foundry Local 工具包

每個模組包含理論、實作練習及生產就緒程式碼範例。

## 職涯影響

**技術職位**：EdgeAI 解決方案架構師 • ML 工程師（邊緣）• IoT AI 開發者 • 行動 AI 開發者

**產業領域**：製造 4.0 • 醫療科技 • 自動系統 • 金融科技 • 消費電子

**作品集專案**：多代理系統 • 生產 RAG 應用 • 跨平台部署 • 性能優化

## 專案結構

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

✅ **漸進學習**：理論 → 實踐 → 生產部署  
✅ **真實案例研究**：微軟、日本航空、企業實作  
✅ **實作範例**：50+ 範例，10 個完整 Foundry Local 演示  
✅ **性能優化**：85% 加速、75% 體積減少  
✅ **多平台支援**：Windows、行動、嵌入式、雲邊混合  
✅ **生產就緒**：監控、擴展、安全性、合規框架

📖 **[可用學習指南](STUDY_GUIDE.md)**：結構化 20 小時學習路徑，包含時間分配指引與自我評量工具。

---

**EdgeAI 代表 AI 部署的未來**：以本地為先，保護隱私，高效能。掌握這些技能，打造下一代智慧應用。

## 其他課程

我們團隊還有其他課程！歡迎參考：

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j 適合初學者](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js 適合初學者](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)

---

### Azure / Edge / MCP / 代理
[![AZD 適合初學者](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Edge AI 適合初學者](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP 適合初學者](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![AI 代理 適合初學者](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### 生成式 AI 系列
[![生成式 AI 適合初學者](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![生成式 AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![生成式 AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![生成式 AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### 核心學習
[![ML 適合初學者](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![數據科學適合初學者](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![AI 適合初學者](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![資安適合初學者](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![網頁開發適合初學者](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![物聯網適合初學者](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![XR 開發適合初學者](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Copilot 系列
[![為 AI 配對程式設計的 Copilot](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot for C#/.NET](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot Adventure](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## 獲取協助

如果你遇到困難或對建立 AI 應用程式有任何疑問，請加入：

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

如果你在構建過程中有產品反饋或錯誤，請訪問：

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件是使用人工智能翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯而成。雖然我們致力於確保準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資料，建議使用專業人工翻譯。本公司不對因使用此翻譯而引起的任何誤解或誤譯負責。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
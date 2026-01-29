# EdgeAI 初學者指南


![課程封面圖片](../../translated_images/zh-TW/cover.eb18d1b9605d754b.webp)

[![GitHub 貢獻者](https://img.shields.io/github/contributors/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/graphs/contributors)
[![GitHub 問題](https://img.shields.io/github/issues/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/issues)
[![GitHub 拉取請求](https://img.shields.io/github/issues-pr/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/pulls)
[![歡迎 PR](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

[![GitHub 追蹤者](https://img.shields.io/github/watchers/microsoft/edgeai-for-beginners.svg?style=social&label=Watch)](https://GitHub.com/microsoft/edgeai-for-beginners/watchers)
[![GitHub 分支](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork)
[![GitHub 星標](https://img.shields.io/github/stars/microsoft/edgeai-for-beginners?style=social&label=Star)](https://GitHub.com/microsoft/edgeai-for-beginners/stargazers)


[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

請依照以下步驟開始使用這些資源：

1. **分支此倉庫**：點擊 [![GitHub 分支](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork)
2. **克隆此倉庫**：`git clone https://github.com/microsoft/edgeai-for-beginners.git`
3. [**加入 Azure AI Foundry Discord 社群並與專家及開發者交流**](https://discord.com/invite/ByRwuEEgH4)


### 🌐 多語言支援

#### 透過 GitHub Action 支援（自動且始終維持最新）

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[阿拉伯語](../ar/README.md) | [孟加拉語](../bn/README.md) | [保加利亞語](../bg/README.md) | [緬甸語（緬甸）](../my/README.md) | [中文（簡體）](../zh-CN/README.md) | [中文（繁體，香港）](../zh-HK/README.md) | [中文（繁體，澳門）](../zh-MO/README.md) | [中文（繁體，臺灣）](./README.md) | [克羅埃西亞語](../hr/README.md) | [捷克語](../cs/README.md) | [丹麥語](../da/README.md) | [荷蘭語](../nl/README.md) | [愛沙尼亞語](../et/README.md) | [芬蘭語](../fi/README.md) | [法語](../fr/README.md) | [德語](../de/README.md) | [希臘語](../el/README.md) | [希伯來語](../he/README.md) | [印地語](../hi/README.md) | [匈牙利語](../hu/README.md) | [印尼語](../id/README.md) | [義大利語](../it/README.md) | [日語](../ja/README.md) | [坎納達語](../kn/README.md) | [韓語](../ko/README.md) | [立陶宛語](../lt/README.md) | [馬來語](../ms/README.md) | [馬拉雅拉姆語](../ml/README.md) | [馬拉地語](../mr/README.md) | [尼泊爾語](../ne/README.md) | [尼日利亞皮欽語](../pcm/README.md) | [挪威語](../no/README.md) | [波斯語（法爾西語）](../fa/README.md) | [波蘭語](../pl/README.md) | [葡萄牙語（巴西）](../pt-BR/README.md) | [葡萄牙語（葡萄牙）](../pt-PT/README.md) | [旁遮普語（古爾穆奇文字）](../pa/README.md) | [羅馬尼亞語](../ro/README.md) | [俄語](../ru/README.md) | [塞爾維亞語（西里爾字母）](../sr/README.md) | [斯洛伐克語](../sk/README.md) | [斯洛維尼亞語](../sl/README.md) | [西班牙語](../es/README.md) | [斯瓦希里語](../sw/README.md) | [瑞典語](../sv/README.md) | [他加祿語（菲律賓語）](../tl/README.md) | [泰米爾語](../ta/README.md) | [泰盧固語](../te/README.md) | [泰語](../th/README.md) | [土耳其語](../tr/README.md) | [烏克蘭語](../uk/README.md) | [烏爾都語](../ur/README.md) | [越南語](../vi/README.md)

> **偏好本地克隆？**

> 此倉庫包含 50 多種語言翻譯，顯著增加下載大小。若要克隆時不含翻譯，請使用 sparse checkout：
> ```bash
> git clone --filter=blob:none --sparse https://github.com/microsoft/edgeai-for-beginners.git
> cd edgeai-for-beginners
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
> 這樣可以讓你用更快的速度下載完成課程所需全部內容。
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

**若希望新增更多翻譯語言，支援語言列表請見 [此處](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md)**

## 介紹

歡迎來到 **EdgeAI 初學者指南** —— 您進入變革性邊緣人工智慧世界的完整旅程。此課程架起強大 AI 能力與邊緣裝置實務部署之間的橋樑，使您能直接在資料產生與決策所需的現場，發揮 AI 的潛力。

### 您將掌握的技能

本課程涵蓋從基礎概念到生產級實現，包括：
- 適合邊緣部署的 **小型語言模型 (SLMs)**
- 跨多元平台的 **硬體感知優化**
- 具備隱私保護能力的 **即時推論**
- 企業應用的 **生產環境部署策略**

### 為何 EdgeAI 重要

邊緣 AI 代表一種新範式，解決當代重要挑戰：
- **隱私與安全**：本地處理敏感資料，避免雲端暴露
- **即時效能**：消除網路延遲，適用於時間敏感應用
- **成本效益**：降低頻寬及雲端運算費用
- **韌性運作**：網路中斷時依然維持功能
- **法規遵循**：符合資料主權要求

### 邊緣 AI

邊緣 AI 指在硬體裝置上本地執行 AI 演算法與語言模型，靠近資料產生處，而不依賴雲端資源進行推論。它降低延遲、強化隱私，實現即時決策。

### 核心原則：
- **裝置端推論**：AI 模型在邊緣裝置（手機、路由器、微控制器、工業電腦）上運行
- **離線能力**：無需持續網路連接也可運作
- **低延遲**：即時回應，適合即時系統
- **資料主權**：敏感資料保留本地，提高安全性與合規性

### 小型語言模型 (SLMs)

像 Phi-4、Mistral-7B、Gemma 等 SLM 是大型 LLM 的優化版本，透過訓練或蒸餾達成：
- **記憶體占用減少**：有效使用有限邊緣裝置記憶體
- **計算需求降低**：優化 CPU 與邊緣 GPU 效能
- **啟動時間縮短**：快速初始化，提升反應速度

它們在滿足以下限制條件下，釋放強大 NLP 功能：
- **嵌入式系統**：物聯網裝置與工業控制器
- **行動裝置**：具離線能力的智慧型手機和平板
- **物聯網設備**：資源有限的感測器與智慧裝置
- **邊緣伺服器**：搭載有限 GPU 資源的本地處理單元
- **個人電腦**：桌機與筆記型電腦部署場景

## 課程模組與導覽

| 模組 | 主題 | 專注領域 | 主要內容 | 等級 | 預計時長 |
|--------|-------|------------|-------------|--------|----------|
| [📖 00 ](./introduction.md) | [EdgeAI 介紹](./introduction.md) | 基礎與背景 | EdgeAI 概覽 • 產業應用 • SLM 簡介 • 學習目標 | 初學者 | 1-2 小時 |
| [📚 01](../../Module01) | [EdgeAI 基礎](./Module01/README.md) | 雲端與邊緣 AI 比較 | EdgeAI 基礎 • 實際案例 • 實作指南 • 邊緣部署 | 初學者 | 3-4 小時 |
| [🧠 02](../../Module02) | [SLM 模型基礎](./Module02/README.md) | 模型家族與架構 | Phi 家族 • Qwen 家族 • Gemma 家族 • BitNET • μModel • Phi-Silica | 初學者 | 4-5 小時 |
| [🚀 03](../../Module03) | [SLM 部署實作](./Module03/README.md) | 本地與雲端部署 | 進階學習 • 本地環境 • 雲端部署 | 中階 | 4-5 小時 |
| [⚙️ 04](../../Module04) | [模型優化工具包](./Module04/README.md) | 跨平台優化 | 介紹 • Llama.cpp • Microsoft Olive • OpenVINO • Apple MLX • 工作流程整合 | 中階 | 5-6 小時 |
| [🔧 05](../../Module05) | [SLMOps 生產運維](./Module05/README.md) | 生產環境運維 | SLMOps 介紹 • 模型蒸餾 • 微調 • 生產部署 | 進階 | 5-6 小時 |
| [🤖 06](../../Module06) | [AI 代理及函式呼叫](./Module06/README.md) | 代理框架與 MCP | 代理介紹 • 函式呼叫 • 模型上下文協議 | 進階 | 4-5 小時 |
| [💻 07](../../Module07) | [平台實作範例](./Module07/README.md) | 跨平台範例 | AI 工具包 • Foundry Local • Windows 開發 | 進階 | 3-4 小時 |
| [🏭 08](../../Module08) | [Foundry Local 工具包](./Module08/README.md) | 生產就緒範例 | 範例應用（詳情如下） | 專家 | 8-10 小時 |

### 🏭 **模組 08：範例應用**

- [01: REST 聊天快速入門](./Module08/samples/01/README.md)
- [02: OpenAI SDK 整合](./Module08/samples/02/README.md)
- [03: 模型發現與基準測試](./Module08/samples/03/README.md)
- [04: Chainlit RAG 應用](./Module08/samples/04/README.md)
- [05: 多代理協調](./Module08/samples/05/README.md)
- [06: 作為工具的模型路由器](./Module08/samples/06/README.md)
- [07: 直接 API 客戶端](./Module08/samples/07/README.md)
- [08: Windows 11 聊天應用](./Module08/samples/08/README.md)
- [09: 進階多代理系統](./Module08/samples/09/README.md)
- [10: Foundry 工具框架](./Module08/samples/10/README.md)

### 🎓 **工作坊：實作學習路徑**

完整的實作工作坊教材與生產級實作：

- **[工作坊指南](./Workshop/Readme.md)** — 完整學習目標、成果與資源導覽
- **Python 範例**（6 堂課）— 更新最佳實踐、錯誤處理與完整文件
- **Jupyter 筆記本**（8 個互動式）— 詳細步驟教學含基準與效能監測
- **課程指南** — 每堂課詳細 Markdown 講義
- **驗證工具** — 驗證碼品質及進行基本測試的腳本

**您將打造：**
- 支援串流的本地 AI 聊天應用
- RAG 資料搜尋管線與品質評估 (RAGAS)
- 多模型基準測試與比較工具
- 多代理協調系統
- 基於任務選擇的智慧模型路由

### 🎙️ **Agentic 工作坊：實作 - AI 播客製作室**

從零開始打造 AI 驅動的播客製作流程！這個沉浸式工作坊教你制造完整多代理系統，將創意轉化為專業播客節目。
**[🎬 開始 AI 播客工作室工作坊](./WorkshopForAgentic/README.md)**

**您的任務**：啟動「Future Bytes」— 一個完全由您自行建立的 AI 代理驅動的科技播客。無需雲端依賴，無 API 費用 — 一切皆在您的本機上運行。

**獨特之處：**
- **🤖 真正的多代理協調** — 建立專門的 AI 代理來研究、撰寫及製作音訊
- **🎯 完整的製作流程管線** — 從主題選擇到最終播客音訊輸出
- **💻 100% 本地部署** — 使用 Ollama 及本地模型（Qwen-3-8B），保障隱私與控制權
- **🎤 文字轉語音整合** — 將腳本轉換為自然且多角色的對話音訊
- **✋ 人工介入流程** — 審核閘道確保品質同時維持自動化

**三幕學習旅程：**

| 幕次 | 焦點 | 主要技能 | 時間長度 |
|-----|-------|------------|----------|
| **[第一幕：認識您的 AI 助手](./WorkshopForAgentic/md/01.BuildAIAgentWithSLM.md)** | 建立您的第一個 AI 代理 | 工具整合 • 網路搜尋 • 問題解決 • 代理推理 | 2-3 小時 |
| **[第二幕：組建您的製作團隊](./WorkshopForAgentic/md/02.AIAgentOrchestrationAndWorkflows.md)** | 協調多個代理 | 團隊協作 • 審核流程 • DevUI 介面 • 人員監督 | 3-4 小時 |
| **[第三幕：讓您的播客生動起來](./WorkshopForAgentic/md/03.Multi-SpeakerPodcastGenerationWithVibeVoice.md)** | 產生播客音訊 | 文字轉語音 • 多角色合成 • 長格式音訊 • 完全自動化 | 2-3 小時 |

**採用技術：**
- **Microsoft Agent Framework** — 多代理協調與管理
- **Ollama** — 本地 AI 模型運行時環境（無需雲端）
- **Qwen-3-8B** — 為代理任務優化的開源語言模型
- **文字轉語音 API** — 自然語音合成，適合播客生成

**硬體支援：**
- ✅ **CPU 模式** — 適用任何現代電腦（建議 8GB+ 記憶體）
- 🚀 **GPU 加速** — 使用 NVIDIA / AMD GPU 顯著提速推論
- ⚡ **NPU 支援** — 次世代神經處理器加速

**適合對象：**
- 學習多代理 AI 系統的開發者
- 對 AI 自動化和工作流程有興趣的人
- 探索 AI 協助製作的內容創作者
- 研究實務 AI 協調模式的學生

**開始建立**：[🎙️ AI 播客工作室工作坊 →](./WorkshopForAgentic/README.md)

### 📊 **學習路徑摘要**
- **總計時長**：36-45 小時
- **初學者路徑**：模組 01-02（7-9 小時）  
- **中級路徑**：模組 03-04（9-11 小時）
- **進階路徑**：模組 05-07（12-15 小時）
- **專家路徑**：模組 08（8-10 小時）

## 您將打造什麼

### 🎯 核心能力
- **邊緣 AI 架構**：設計以本地為先且含雲端整合的 AI 系統
- **模型優化**：量化與壓縮模型以利邊緣部署（速度提升 85%、大小縮減 75%）
- **多平台部署**：Windows、行動、嵌入式及雲端-邊緣混合系統
- **生產運營**：邊緣 AI 監控、擴展與維護

### 🏗️ 實作專案
- **Foundry 本地聊天應用**：Windows 11 原生應用含模型切換功能
- **多代理系統**：協調者和專家代理實現複雜工作流程  
- **RAG 應用**：本地文件處理與向量檢索
- **模型路由器**：根據任務分析智能選擇模型
- **API 框架**：生產級客戶端，支援串流與健康監控
- **跨平台工具**：LangChain / Semantic Kernel 整合範例

### 🏢 業界應用
**製造業** • **醫療保健** • **自主車輛** • **智慧城市** • **行動應用**

## 快速開始

**推薦學習路徑**（共 20-30 小時）：

0. **📖 介紹** ([Introduction.md](./introduction.md))：EdgeAI 基礎 + 產業背景 + 學習框架
1. **📚 基礎**（模組 01-02）：EdgeAI 概念 + SLM 模型家族
2. **⚙️ 優化**（模組 03-04）：部署 + 量化框架  
3. **🚀 生產**（模組 05-06）：SLMOps + AI 代理 + 函數呼叫
4. **💻 實作**（模組 07-08）：平台範例 + Foundry Local 工具包

每個模組包含理論、實作練習及適用生產的程式碼範例。

## 職涯影響

**技術職務**：邊緣 AI 解決方案架構師 • 機器學習工程師（邊緣） • 物聯網 AI 開發者 • 行動 AI 開發者

**行業領域**：製造業 4.0 • 醫療科技 • 自主系統 • 金融科技 • 消費性電子

**作品集專案**：多代理系統 • 生產級 RAG 應用 • 跨平台部署 • 性能優化

## 資料庫結構

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
✅ **實作範例**：超過 50 個示例，10 個完整 Foundry Local 示範  
✅ **性能導向**：速度提升 85%、大小減少 75%  
✅ **多平台支援**：Windows、行動、嵌入式、雲端邊緣混合  
✅ **生產就緒**：監控、擴展、安全與合規架構

📖 **[學習指南](STUDY_GUIDE.md)**：結構化的 20 小時學習路徑，含時間分配建議與自我評估工具。

---

**EdgeAI 代表 AI 部署的未來：**本地優先、隱私保護、高效能。掌握這些技能，打造下一代智慧應用。

## 其他課程

我們團隊還推出其他課程！敬請參考：

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j 入門](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js 入門](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)

---

### Azure / Edge / MCP / 代理
[![AZD 入門](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Edge AI 入門](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP 入門](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![AI 代理入門](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### 生成式 AI 系列
[![生成式 AI 入門](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![生成式 AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![生成式 AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![生成式 AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### 核心學習
[![機器學習入門](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![資料科學入門](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![AI 入門](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![資安入門](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![網頁開發入門](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![物聯網入門](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![XR 開發入門](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Copilot 系列
[![AI 配對程式設計 Copilot](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot for C#/.NET](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot Adventure](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## 尋求協助

如果您在建立 AI 應用程式時遇到困難或有任何問題，請加入：

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

如果您在開發過程中有產品回饋或錯誤，請造訪：

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意自動翻譯可能包含錯誤或不準確之處。原文之母語版本應視為權威資料來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯所產生之任何誤解或誤釋負責。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
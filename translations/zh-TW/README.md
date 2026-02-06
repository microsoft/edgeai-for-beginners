# EdgeAI 初學者指南


![課程封面圖片](../../translated_images/zh-TW/cover.eb18d1b9605d754b.webp)

[![GitHub 貢獻者](https://img.shields.io/github/contributors/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/graphs/contributors)
[![GitHub 問題](https://img.shields.io/github/issues/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/issues)
[![GitHub 拉取請求](https://img.shields.io/github/issues-pr/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/pulls)
[![歡迎拉取請求](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

[![GitHub 觀察者](https://img.shields.io/github/watchers/microsoft/edgeai-for-beginners.svg?style=social&label=Watch)](https://GitHub.com/microsoft/edgeai-for-beginners/watchers)
[![GitHub 分支](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork)
[![GitHub 星標](https://img.shields.io/github/stars/microsoft/edgeai-for-beginners?style=social&label=Star)](https://GitHub.com/microsoft/edgeai-for-beginners/stargazers)


[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

按照以下步驟開始使用這些資源：

1. **Fork 倉庫**：點擊 [![GitHub 分支](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork)
2. **Clone 倉庫**：`git clone https://github.com/microsoft/edgeai-for-beginners.git`
3. [**加入 Azure AI Foundry Discord 與專家和其他開發者交流**](https://discord.com/invite/ByRwuEEgH4)


### 🌐 多語言支援

#### 透過 GitHub Action 支援（自動且始終保持最新）

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[阿拉伯語](../ar/README.md) | [孟加拉語](../bn/README.md) | [保加利亞語](../bg/README.md) | [緬甸語 (Myanmar)](../my/README.md) | [中文 (簡體)](../zh-CN/README.md) | [中文 (繁體, 香港)](../zh-HK/README.md) | [中文 (繁體, 澳門)](../zh-MO/README.md) | [中文 (繁體, 台灣)](./README.md) | [克羅埃西亞語](../hr/README.md) | [捷克語](../cs/README.md) | [丹麥語](../da/README.md) | [荷蘭語](../nl/README.md) | [愛沙尼亞語](../et/README.md) | [芬蘭語](../fi/README.md) | [法語](../fr/README.md) | [德語](../de/README.md) | [希臘語](../el/README.md) | [希伯來語](../he/README.md) | [印地語](../hi/README.md) | [匈牙利語](../hu/README.md) | [印尼語](../id/README.md) | [義大利語](../it/README.md) | [日語](../ja/README.md) | [卡納達語](../kn/README.md) | [韓語](../ko/README.md) | [立陶宛語](../lt/README.md) | [馬來語](../ms/README.md) | [馬拉雅拉姆語](../ml/README.md) | [馬拉地語](../mr/README.md) | [尼泊爾語](../ne/README.md) | [奈及利亞皮欽語](../pcm/README.md) | [挪威語](../no/README.md) | [波斯語 (法爾西語)](../fa/README.md) | [波蘭語](../pl/README.md) | [葡萄牙語 (巴西)](../pt-BR/README.md) | [葡萄牙語 (葡萄牙)](../pt-PT/README.md) | [旁遮普語 (古魯穆奇文)](../pa/README.md) | [羅馬尼亞語](../ro/README.md) | [俄語](../ru/README.md) | [塞爾維亞語 (西里爾字母)](../sr/README.md) | [斯洛伐克語](../sk/README.md) | [斯洛文尼亞語](../sl/README.md) | [西班牙語](../es/README.md) | [斯瓦希里語](../sw/README.md) | [瑞典語](../sv/README.md) | [他加祿語 (菲律賓語)](../tl/README.md) | [泰米爾語](../ta/README.md) | [泰盧固語](../te/README.md) | [泰語](../th/README.md) | [土耳其語](../tr/README.md) | [烏克蘭語](../uk/README.md) | [烏爾都語](../ur/README.md) | [越南語](../vi/README.md)

> **偏好本地 Clone？**

> 這個倉庫包含 50 多種語言的翻譯，會顯著增加下載大小。若想排除翻譯內容，可以使用稀疏檢出功能：
> ```bash
> git clone --filter=blob:none --sparse https://github.com/microsoft/edgeai-for-beginners.git
> cd edgeai-for-beginners
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
> 這樣你可以更快地完成下載並具備課程所需的所有資源。
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

**如果您希望支援更多翻譯語言，請參考列表 [這裡](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md)**

## 簡介

歡迎來到 **EdgeAI 初學者指南** — 您進入邊緣人工智慧變革世界的全面旅程。本課程架起強大 AI 能力與邊緣設備上實際部署的橋樑，助您直接在數據產生和決策所需的位置掌握 AI 潛力。

### 您將學會什麼

本課程帶您從基本概念到生產就緒的實作，涵蓋：
- 適合邊緣部署的**小型語言模型 (SLMs)**
- 跨平台**硬體感知優化**
- 具備隱私保護功能的**即時推斷**
- 企業應用的**生產部署策略**

### 為什麼 EdgeAI 重要

Edge AI 代表了解決現代重大挑戰的轉捩點：
- **隱私與安全**：在本地處理敏感數據，避免雲端曝露
- **即時效能**：消除網路延遲，適合時間敏感應用
- **成本效率**：減少頻寬與雲端計算支出
- **強健運作**：在網路斷線時仍保持功能
- **法規遵從**：符合數據主權規定

### 邊緣人工智慧 (Edge AI)

邊緣人工智慧是指在靠近數據產生地點的硬體本地執行 AI 演算法和語言模型，推斷過程不依賴雲端資源。它降低延遲、強化隱私、實現即時決策。

### 核心原則：
- **裝置端推斷**：AI 模型在邊緣設備（手機、路由器、微控制器、工業電腦）上執行
- **離線能力**：無需持續網路連線即可運作
- **低延遲**：適用即時系統的快速回應
- **數據主權**：敏感數據保留本地，提升安全和合規

### 小型語言模型 (SLMs)

像 Phi-4、Mistral-7B 和 Gemma 這類 SLM 是經過優化的小型大語言模型（LLM）版本，經過訓練或蒸餾以達成：
- **減少記憶體佔用**：有效利用有限邊緣設備的記憶體
- **降低運算需求**：優化適合 CPU 與邊緣 GPU 效能
- **啟動更快**：快速初始化以提供響應能力

它們在符合以下條件時，釋放強大的自然語言處理能力：
- **嵌入式系統**：物聯網設備和工業控制器
- **行動設備**：具離線功能的智慧手機和平板
- **物聯網設備**：資源有限的感測器和智慧裝置
- **邊緣伺服器**：有限 GPU 資源的本地處理單元
- **個人電腦**：桌面和筆記型電腦部署場景

## 課程模組與導航

| 模組 | 主題 | 焦點領域 | 主要內容 | 等級 | 時長 |
|--------|-------|------------|-------------|--------|----------|
| [📖 00 ](./introduction.md) | [EdgeAI 簡介](./introduction.md) | 基礎及背景 | EdgeAI 總覽 • 產業應用 • SLM 介紹 • 學習目標 | 初學者 | 1-2 小時 |
| [📚 01](../../Module01) | [EdgeAI 基礎](./Module01/README.md) | 雲端與邊緣 AI 比較 | EdgeAI 基礎 • 真實案例 • 實作指南 • 邊緣部署 | 初學者 | 3-4 小時 |
| [🧠 02](../../Module02) | [SLM 模型基礎](./Module02/README.md) | 模型家族與架構 | Phi 系列 • Qwen 系列 • Gemma 系列 • BitNET • μModel • Phi-Silica | 初學者 | 4-5 小時 |
| [🚀 03](../../Module03) | [SLM 部署實務](./Module03/README.md) | 本地與雲端部署 | 進階學習 • 本地環境 • 雲端部署 | 中階 | 4-5 小時 |
| [⚙️ 04](../../Module04) | [模型優化工具包](./Module04/README.md) | 跨平台優化 | 介紹 • Llama.cpp • Microsoft Olive • OpenVINO • Apple MLX • 工作流程綜合 | 中階 | 5-6 小時 |
| [🔧 05](../../Module05) | [SLMOps 生產](./Module05/README.md) | 生產運營 | SLMOps 介紹 • 模型蒸餾 • 微調 • 生產部署 | 進階 | 5-6 小時 |
| [🤖 06](../../Module06) | [AI 代理與函式呼叫](./Module06/README.md) | 代理框架與 MCP | 代理介紹 • 函式呼叫 • 模型語境協議 | 進階 | 4-5 小時 |
| [💻 07](../../Module07) | [平台實作](./Module07/README.md) | 跨平台範例 | AI 工具包 • Foundry Local • Windows 開發 | 進階 | 3-4 小時 |
| [🏭 08](../../Module08) | [Foundry Local 工具包](./Module08/README.md) | 生產就緒範例 | 範例應用程式（詳見下方） | 專家 | 8-10 小時 |

### 🏭 **模組 08：範例應用程式**

- [01: REST 聊天快速入門](./Module08/samples/01/README.md)
- [02: OpenAI SDK 整合](./Module08/samples/02/README.md)
- [03: 模型發現與基準測試](./Module08/samples/03/README.md)
- [04: Chainlit RAG 應用](./Module08/samples/04/README.md)
- [05: 多代理協調](./Module08/samples/05/README.md)
- [06: 模型即工具路由](./Module08/samples/06/README.md)
- [07: 直接 API 客戶端](./Module08/samples/07/README.md)
- [08: Windows 11 聊天應用程式](./Module08/samples/08/README.md)
- [09: 進階多代理系統](./Module08/samples/09/README.md)
- [10: Foundry 工具框架](./Module08/samples/10/README.md)

### 🎓 **工作坊：實作學習路線**

包含生產就緒實作的完整實務工作坊素材：

- **[工作坊指南](./Workshop/Readme.md)** — 完整學習目標、成效與資源導覽
- **Python 範例**（6 節）— 更新最佳實務、錯誤處理與完整文件
- **Jupyter 筆記本**（8 節互動式）— 逐步教學及基準和效能監控
- **講義指引** — 詳細的每節工作坊 Markdown 指導
- **驗證工具** — 用於驗證程式碼品質和執行初步測試的腳本

**您將會打造：**
- 支援串流的本地 AI 聊天應用
- 帶品質評估的 RAG 流水線 (RAGAS)
- 多模型基準測試與比較工具
- 多代理協調系統
- 任務驅動的智能模型路由

### 🎙️ **Agentic 工作坊：實作 - AI Podcast 工作室**

從零開始打造 AI 驅動的播客製作流程！這個沉浸式工作坊教您創建完整的多代理系統，將構思轉化為專業播客集數。
**[🎬 開始 AI 播客工作室工作坊](./WorkshopForAgentic/README.md)**

**你的任務**：啟動「Future Bytes」——一個完全由你自己打造的 AI 代理人驅動的科技播客。無需雲端依賴，無 API 費用——所有一切皆於本地機器運行。

**獨特之處：**
- **🤖 真正的多代理人協調** – 建立專門的 AI 代理人負責研究、撰寫與製作音頻
- **🎯 完整產製流程** – 從主題選擇到最終播客音頻輸出
- **💻 100% 本地部署** – 使用 Ollama 與本地模型 (Qwen-3-8B) 以確保隱私與控制權
- **🎤 文字轉語音整合** – 將腳本轉換為自然聲音的多說話者對話
- **✋ 人工審核工作流程** – 審核關卡確保品質同時維持自動化

**三幕式學習旅程：**

| 幕別 | 焦點 | 主要技能 | 時長 |
|-----|-------|------------|----------|
| **[第一幕：認識你的 AI 助手](./WorkshopForAgentic/md/01.BuildAIAgentWithSLM.md)** | 建立你的第一個 AI 代理人 | 工具整合 • 網絡搜索 • 問題解決 • 代理人推理 | 2-3 小時 |
| **[第二幕：組建你的製作團隊](./WorkshopForAgentic/md/02.AIAgentOrchestrationAndWorkflows.md)** | 協調多個代理人 | 團隊協作 • 審核流程 • DevUI 介面 • 人工監督 | 3-4 小時 |
| **[第三幕：賦予你的播客生命](./WorkshopForAgentic/md/03.Multi-SpeakerPodcastGenerationWithVibeVoice.md)** | 產生播客音頻 | 文字轉語音 • 多說話者合成 • 長篇音頻 • 完全自動化 | 2-3 小時 |

**使用技術：**
- **Microsoft Agent Framework** – 多代理人協調與整合
- **Ollama** – 本地化 AI 模型運行時（無需雲端）
- **Qwen-3-8B** – 為代理任務優化的開源語言模型
- **文字轉語音 API** – 自然語音合成用於播客創作

**硬體支援：**
- ✅ **CPU 模式** – 適用任何現代電腦（建議 8GB 以上記憶體）
- 🚀 **GPU 加速** – NVIDIA/AMD GPU 大幅提升推論速度
- ⚡ **NPU 支援** – 次世代神經處理器加速

**適合對象：**
- 學習多代理 AI 系統的開發者
- 對 AI 自動化與工作流程感興趣的人
- 探索 AI 輔助手段製作內容的創作者
- 研究實務 AI 協調模式的學生

**開始打造**: [🎙️ AI 播客工作室工作坊 →](./WorkshopForAgentic/README.md)

### 📊 **學習路徑總結**
- **總時長**：36-45 小時
- **初學者路徑**：模組 01-02（7-9 小時）  
- **中階路徑**：模組 03-04（9-11 小時）
- **高階路徑**：模組 05-07（12-15 小時）
- **專家路徑**：模組 08（8-10 小時）

## 你將打造什麼

### 🎯 核心能力
- **邊緣 AI 架構**：設計以本地優先且可整合雲端的 AI 系統
- **模型優化**：量化與壓縮模型以符合邊緣部署（速度提升 85%、大小減少 75%）
- **多平台部署**：Windows、行動裝置、嵌入式及雲端邊緣混合系統
- **生產運維**：監控、擴展與維護邊緣 AI 於生產環境

### 🏗️ 實務專案
- **Foundry 本地聊天應用**：Windows 11 原生應用搭配模型切換功能
- **多代理系統**：具備專家代理的協調者以處理複雜工作流程  
- **RAG 應用**：本地文件處理與向量檢索
- **模型路由器**：根據任務分析智慧選擇模型
- **API 框架**：生產用客戶端，支援串流與健康監控
- **跨平台工具**：LangChain/Semantic Kernel 整合模式

### 🏢 產業應用
**製造業** • **醫療保健** • **自駕車** • **智慧城市** • **行動應用**

## 快速上手

**推薦學習路徑**（總計 20-30 小時）：

0. **📖 入門介紹** ([Introduction.md](./introduction.md))：邊緣 AI 基礎 + 產業背景 + 學習架構
1. **📚 基礎**（模組 01-02）：邊緣 AI 概念 + SLM 模型系列
2. **⚙️ 優化**（模組 03-04）：部署 + 量化框架  
3. **🚀 生產**（模組 05-06）：SLMOps + AI 代理人 + 函式調用
4. **💻 實作**（模組 07-08）：平台範例 + Foundry 本地工具包

每個模組包含理論、實作練習與生產級原始碼範例。

## 職涯影響

**技術職務**：邊緣 AI 解決方案架構師 • 邊緣機器學習工程師 • IoT AI 開發者 • 行動 AI 開發者

**產業領域**：製造 4.0 • 醫療科技 • 自主系統 • 金融科技 • 消費性電子

**作品集專案**：多代理系統 • 生產級 RAG 應用 • 跨平台部署 • 性能優化

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

✅ **循序漸進學習**：理論 → 實作 → 生產部署  
✅ **真實案例研究**：微軟、日本航空、企業實作  
✅ **動手範例**：50+ 範例，10 個完整 Foundry Local 示範  
✅ **性能優先**：速度提升 85%、容量縮減 75%  
✅ **多平台支援**：Windows、行動、嵌入式、雲端邊緣混合  
✅ **生產就緒**：監控、擴展、安全與合規框架

📖 **[學習指南](STUDY_GUIDE.md)**：結構化 20 小時學習路徑，含時間分配建議與自我評估工具。

---

**邊緣 AI 代表 AI 部署的未來**：以本地為先、保護隱私且高效。掌握這些技能，打造下一代智慧應用。

## 其他課程

我們的團隊還製作其他課程！歡迎參考：

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j 入門](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js 入門](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)
[![LangChain 入門](https://img.shields.io/badge/LangChain%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://github.com/microsoft/langchain-for-beginners?WT.mc_id=m365-94501-dwahlin)
---

### Azure / 邊緣 / MCP / 代理人
[![AZD 入門](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![邊緣 AI 入門](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP 入門](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![AI 代理人入門](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

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
[![人工智慧入門](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![資安入門](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![網頁開發入門](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![物聯網入門](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![XR 開發入門](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Copilot 系列
[![Copilot for AI Paired Programming](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot for C#/.NET](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot Adventure](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## 獲取幫助

如果你卡住了或在構建 AI 應用程式時有任何問題，請加入：

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

如果你有產品反饋或在構建過程中遇到錯誤，請訪問：

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：  
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的原文版本應視為權威來源。對於關鍵資訊，建議採用專業人工翻譯。我們不對因使用本翻譯所產生的任何誤解或誤讀負責。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
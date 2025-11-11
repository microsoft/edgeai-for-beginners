<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2e61ee5b6cb0bff11495c72afb37a9e8",
  "translation_date": "2025-11-11T16:47:43+00:00",
  "source_file": "README.md",
  "language_code": "tw"
}
-->
# EdgeAI 初學者指南

![課程封面圖片](../../translated_images/cover.eb18d1b9605d754b30973f4e17c6e11ea4f8473d9686ee378d6e7b44e3c70ac7.tw.png)

[![GitHub 貢獻者](https://img.shields.io/github/contributors/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/graphs/contributors)
[![GitHub 問題](https://img.shields.io/github/issues/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/issues)
[![GitHub 拉取請求](https://img.shields.io/github/issues-pr/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/pulls)
[![歡迎 PR](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

[![GitHub 觀察者](https://img.shields.io/github/watchers/microsoft/edgeai-for-beginners.svg?style=social&label=Watch)](https://GitHub.com/microsoft/edgeai-for-beginners/watchers)
[![GitHub 分叉](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork)
[![GitHub 星星](https://img.shields.io/github/stars/microsoft/edgeai-for-beginners?style=social&label=Star)](https://GitHub.com/microsoft/edgeai-for-beginners/stargazers)

[![Microsoft Azure AI Foundry Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

按照以下步驟開始使用這些資源：

1. **分叉倉庫**：點擊 [![GitHub 分叉](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork)
2. **克隆倉庫**：`git clone https://github.com/microsoft/edgeai-for-beginners.git`
3. [**加入 Azure AI Foundry Discord，與專家和其他開發者交流**](https://discord.com/invite/ByRwuEEgH4)

### 🌐 多語言支持

#### 通過 GitHub Action 支持（自動化且始終保持最新）

[阿拉伯語](../ar/README.md) | [孟加拉語](../bn/README.md) | [保加利亞語](../bg/README.md) | [緬甸語](../my/README.md) | [中文（簡體）](../zh/README.md) | [中文（繁體，香港）](../hk/README.md) | [中文（繁體，澳門）](../mo/README.md) | [中文（繁體，台灣）](./README.md) | [克羅地亞語](../hr/README.md) | [捷克語](../cs/README.md) | [丹麥語](../da/README.md) | [荷蘭語](../nl/README.md) | [愛沙尼亞語](../et/README.md) | [芬蘭語](../fi/README.md) | [法語](../fr/README.md) | [德語](../de/README.md) | [希臘語](../el/README.md) | [希伯來語](../he/README.md) | [印地語](../hi/README.md) | [匈牙利語](../hu/README.md) | [印尼語](../id/README.md) | [意大利語](../it/README.md) | [日語](../ja/README.md) | [韓語](../ko/README.md) | [立陶宛語](../lt/README.md) | [馬來語](../ms/README.md) | [馬拉地語](../mr/README.md) | [尼泊爾語](../ne/README.md) | [尼日利亞皮欽語](../pcm/README.md) | [挪威語](../no/README.md) | [波斯語（法爾西語）](../fa/README.md) | [波蘭語](../pl/README.md) | [葡萄牙語（巴西）](../br/README.md) | [葡萄牙語（葡萄牙）](../pt/README.md) | [旁遮普語（古木基文）](../pa/README.md) | [羅馬尼亞語](../ro/README.md) | [俄語](../ru/README.md) | [塞爾維亞語（西里爾文）](../sr/README.md) | [斯洛伐克語](../sk/README.md) | [斯洛文尼亞語](../sl/README.md) | [西班牙語](../es/README.md) | [斯瓦希里語](../sw/README.md) | [瑞典語](../sv/README.md) | [塔加洛語（菲律賓語）](../tl/README.md) | [泰米爾語](../ta/README.md) | [泰語](../th/README.md) | [土耳其語](../tr/README.md) | [烏克蘭語](../uk/README.md) | [烏爾都語](../ur/README.md) | [越南語](../vi/README.md)

**如果您希望支持其他翻譯語言，請參考 [此處](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md)**

## 簡介

歡迎來到 **EdgeAI 初學者指南**——這是一個全面的旅程，帶您進入邊緣人工智慧的變革世界。本課程將強大的 AI 能力與邊緣設備上的實際部署相結合，幫助您直接在數據生成和需要做出決策的地方發揮 AI 的潛力。

### 您將掌握的內容

本課程涵蓋從基礎概念到生產就緒的實施，包括：
- **小型語言模型（SLMs）**，針對邊緣部署進行優化
- **硬體感知優化**，適用於多種平台
- **隱私保護的即時推理**
- **生產部署**策略，適用於企業應用

### 為什麼邊緣 AI 很重要

邊緣 AI 代表了一種解決現代關鍵挑戰的範式轉變：
- **隱私與安全**：在本地處理敏感數據，避免雲端暴露
- **即時性能**：消除網絡延遲，適用於時間敏感的應用
- **成本效益**：減少帶寬和雲計算開支
- **運行穩定性**：在網絡中斷期間保持功能
- **法規合規性**：滿足數據主權要求

### 邊緣 AI

邊緣 AI 是指在硬體上本地運行 AI 算法和語言模型，靠近數據生成的地方，而不依賴雲端資源進行推理。它減少了延遲，增強了隱私，並實現了即時決策。

### 核心原則：
- **設備上的推理**：AI 模型在邊緣設備（手機、路由器、微控制器、工業 PC）上運行
- **離線能力**：無需持續的網絡連接即可運行
- **低延遲**：即時響應，適合即時系統
- **數據主權**：保持敏感數據本地化，提高安全性和合規性

### 小型語言模型（SLMs）

像 Phi-4、Mistral-7B 和 Gemma 這樣的 SLMs 是更大 LLMs 的優化版本——經過訓練或蒸餾以實現：
- **減少內存佔用**：有效利用有限的邊緣設備內存
- **降低計算需求**：針對 CPU 和邊緣 GPU 性能進行優化
- **更快的啟動時間**：快速初始化，適用於響應式應用

它們在滿足以下限制的同時解鎖了強大的 NLP 功能：
- **嵌入式系統**：物聯網設備和工業控制器
- **移動設備**：具有離線功能的智能手機和平板電腦
- **物聯網設備**：資源有限的傳感器和智能設備
- **邊緣伺服器**：具有有限 GPU 資源的本地處理單元
- **個人電腦**：桌面和筆記本電腦的部署場景

## 課程模組與導航

| 模組 | 主題 | 重點領域 | 主要內容 | 等級 | 時長 |
|--------|-------|------------|-------------|--------|----------|
| [📖 00 ](./introduction.md) | [邊緣 AI 簡介](./introduction.md) | 基礎與背景 | 邊緣 AI 概述 • 行業應用 • SLM 簡介 • 學習目標 | 初學者 | 1-2 小時 |
| [📚 01](../../Module01) | [邊緣 AI 基礎](./Module01/README.md) | 雲端與邊緣 AI 比較 | 邊緣 AI 基礎 • 真實案例研究 • 實施指南 • 邊緣部署 | 初學者 | 3-4 小時 |
| [🧠 02](../../Module02) | [SLM 模型基礎](./Module02/README.md) | 模型家族與架構 | Phi 家族 • Qwen 家族 • Gemma 家族 • BitNET • μModel • Phi-Silica | 初學者 | 4-5 小時 |
| [🚀 03](../../Module03) | [SLM 部署實踐](./Module03/README.md) | 本地與雲端部署 | 高級學習 • 本地環境 • 雲端部署 | 中級 | 4-5 小時 |
| [⚙️ 04](../../Module04) | [模型優化工具包](./Module04/README.md) | 跨平台優化 | 簡介 • Llama.cpp • Microsoft Olive • OpenVINO • Apple MLX • 工作流程綜合 | 中級 | 5-6 小時 |
| [🔧 05](../../Module05) | [SLMOps 生產](./Module05/README.md) | 生產運營 | SLMOps 簡介 • 模型蒸餾 • 微調 • 生產部署 | 高級 | 5-6 小時 |
| [🤖 06](../../Module06) | [AI 代理與功能調用](./Module06/README.md) | 代理框架與 MCP | 代理簡介 • 功能調用 • 模型上下文協議 | 高級 | 4-5 小時 |
| [💻 07](../../Module07) | [平台實施](./Module07/README.md) | 跨平台範例 | AI 工具包 • Foundry Local • Windows 開發 | 高級 | 3-4 小時 |
| [🏭 08](../../Module08) | [Foundry Local 工具包](./Module08/README.md) | 生產就緒範例 | 範例應用（詳情見下文） | 專家 | 8-10 小時 |

### 🏭 **模組 08：範例應用**

- [01: REST 聊天快速入門](./Module08/samples/01/README.md)
- [02: OpenAI SDK 集成](./Module08/samples/02/README.md)
- [03: 模型發現與基準測試](./Module08/samples/03/README.md)
- [04: Chainlit RAG 應用](./Module08/samples/04/README.md)
- [05: 多代理協作](./Module08/samples/05/README.md)
- [06: 作為工具的模型路由器](./Module08/samples/06/README.md)
- [07: 直接 API 客戶端](./Module08/samples/07/README.md)
- [08: Windows 11 聊天應用](./Module08/samples/08/README.md)
- [09: 高級多代理系統](./Module08/samples/09/README.md)
- [10: Foundry 工具框架](./Module08/samples/10/README.md)

### 🎓 **工作坊：實踐學習路徑**

提供全面的實踐工作坊材料，包含生產就緒的實施：

- **[工作坊指南](./Workshop/Readme.md)** - 完整的學習目標、成果和資源導航
- **Python 範例**（6 節課） - 更新最佳實踐、錯誤處理和全面文檔
- **Jupyter 筆記本**（8 個互動式） - 步驟教學，包含基準測試和性能監控
- **課程指南** - 每節工作坊的詳細 Markdown 指南
- **驗證工具** - 用於驗證代碼質量和運行煙霧測試的腳本

**您將構建的內容：**
- 支持流式的本地 AI 聊天應用
- 帶有質量評估的 RAG 管道（RAGAS）
- 多模型基準測試和比較工具
- 多代理協作系統
- 智能模型路由，基於任務選擇

### 📊 **學習路徑摘要**
- **總時長**：36-45 小時
- **初學者路徑**：模組 01-02（7-9 小時）  
- **中級路徑**：模組 03-04（9-11 小時）
- **高級路徑**：模組 05-07（12-15 小時）
- **專家路徑**：模組 08（8-10 小時）

## 您將構建的內容

### 🎯 核心能力
- **邊緣 AI 架構**：設計本地優先的 AI 系統，並與雲端集成
- **模型優化**：量化和壓縮模型以進行邊緣部署（提升 85% 的速度，減少 75% 的大小）
- **多平台部署**：Windows、行動裝置、嵌入式系統及雲端邊緣混合系統  
- **生產運營**：監控、擴展及維護生產中的邊緣 AI  

### 🏗️ 實作專案  
- **Foundry 本地聊天應用程式**：Windows 11 原生應用程式，支援模型切換  
- **多代理系統**：協調器與專業代理，用於複雜工作流程  
- **RAG 應用程式**：本地文件處理搭配向量搜尋  
- **模型路由器**：根據任務分析智能選擇模型  
- **API 框架**：具備串流及健康監控的生產就緒客戶端  
- **跨平台工具**：LangChain/Semantic Kernel 整合模式  

### 🏢 產業應用  
**製造業** • **醫療保健** • **自動駕駛車輛** • **智慧城市** • **行動應用程式**  

## 快速入門  

**推薦學習路徑**（總計 20-30 小時）：  

0. **📖 簡介** ([Introduction.md](./introduction.md))：邊緣 AI 基礎 + 產業背景 + 學習框架  
1. **📚 基礎**（模組 01-02）：邊緣 AI 概念 + SLM 模型家族  
2. **⚙️ 優化**（模組 03-04）：部署 + 量化框架  
3. **🚀 生產**（模組 05-06）：SLMOps + AI 代理 + 函數調用  
4. **💻 實作**（模組 07-08）：平台範例 + Foundry Local 工具包  

每個模組包含理論、實作練習及生產就緒的程式碼範例。  

## 職業影響  

**技術職位**：邊緣 AI 解決方案架構師 • 機器學習工程師（邊緣） • IoT AI 開發者 • 行動 AI 開發者  

**產業領域**：製造業 4.0 • 醫療科技 • 自主系統 • 金融科技 • 消費電子  

**作品集專案**：多代理系統 • 生產 RAG 應用程式 • 跨平台部署 • 性能優化  

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
✅ **真實案例研究**：Microsoft、日本航空、企業實施案例  
✅ **實作範例**：超過 50 個範例，10 個完整的 Foundry Local 演示  
✅ **性能專注**：提升速度 85%，減少大小 75%  
✅ **多平台支持**：Windows、行動裝置、嵌入式系統、雲端邊緣混合  
✅ **生產就緒**：監控、擴展、安全性及合規框架  

📖 **[學習指南](STUDY_GUIDE.md)**：結構化的 20 小時學習路徑，包含時間分配指導及自我評估工具。  

---

**邊緣 AI 代表了 AI 部署的未來**：本地優先、隱私保護及高效能。掌握這些技能，打造下一代智能應用程式。  

## 其他課程  

我們的團隊還提供其他課程！查看以下內容：  

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

## 尋求幫助  

如果您遇到困難或有任何關於構建 AI 應用程式的問題，請加入：  

[![Azure AI Foundry Discord](https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)  

如果您有產品反饋或在構建過程中遇到錯誤，請訪問：  

[![Azure AI Foundry Developer Forum](https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)  

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：  
本文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。儘管我們努力確保翻譯的準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於關鍵信息，建議使用專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或誤釋不承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
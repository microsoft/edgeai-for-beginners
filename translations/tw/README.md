<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8f958250b0b94976c721e6cbdc541581",
  "translation_date": "2025-10-24T09:15:59+00:00",
  "source_file": "README.md",
  "language_code": "tw"
}
-->
# 初學者的邊緣人工智慧課程

![課程封面圖片](../../translated_images/cover.eb18d1b9605d754b30973f4e17c6e11ea4f8473d9686ee378d6e7b44e3c70ac7.tw.png)

[![GitHub contributors](https://img.shields.io/github/contributors/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/graphs/contributors)
[![GitHub issues](https://img.shields.io/github/issues/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/issues)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/pulls)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

[![Microsoft Azure AI Foundry Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

按照以下步驟開始使用這些資源：

1. **Fork 此儲存庫**：點擊 [![GitHub forks](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork)
2. **Clone 此儲存庫**：`git clone https://github.com/microsoft/edgeai-for-beginners.git`
3. [**加入 Azure AI Foundry Discord，與專家和其他開發者交流**](https://discord.com/invite/ByRwuEEgH4)

### 🌐 多語言支持

#### 通過 GitHub Action 支持（自動化且始終保持最新）

[阿拉伯語](../ar/README.md) | [孟加拉語](../bn/README.md) | [保加利亞語](../bg/README.md) | [緬甸語](../my/README.md) | [中文（簡體）](../zh/README.md) | [中文（繁體，香港）](../hk/README.md) | [中文（繁體，澳門）](../mo/README.md) | [中文（繁體，台灣）](./README.md) | [克羅埃西亞語](../hr/README.md) | [捷克語](../cs/README.md) | [丹麥語](../da/README.md) | [荷蘭語](../nl/README.md) | [愛沙尼亞語](../et/README.md) | [芬蘭語](../fi/README.md) | [法語](../fr/README.md) | [德語](../de/README.md) | [希臘語](../el/README.md) | [希伯來語](../he/README.md) | [印地語](../hi/README.md) | [匈牙利語](../hu/README.md) | [印尼語](../id/README.md) | [意大利語](../it/README.md) | [日語](../ja/README.md) | [韓語](../ko/README.md) | [立陶宛語](../lt/README.md) | [馬來語](../ms/README.md) | [馬拉地語](../mr/README.md) | [尼泊爾語](../ne/README.md) | [挪威語](../no/README.md) | [波斯語](../fa/README.md) | [波蘭語](../pl/README.md) | [葡萄牙語（巴西）](../br/README.md) | [葡萄牙語（葡萄牙）](../pt/README.md) | [旁遮普語（古木基文）](../pa/README.md) | [羅馬尼亞語](../ro/README.md) | [俄語](../ru/README.md) | [塞爾維亞語（西里爾文）](../sr/README.md) | [斯洛伐克語](../sk/README.md) | [斯洛文尼亞語](../sl/README.md) | [西班牙語](../es/README.md) | [斯瓦希里語](../sw/README.md) | [瑞典語](../sv/README.md) | [塔加洛語（菲律賓語）](../tl/README.md) | [泰米爾語](../ta/README.md) | [泰語](../th/README.md) | [土耳其語](../tr/README.md) | [烏克蘭語](../uk/README.md) | [烏爾都語](../ur/README.md) | [越南語](../vi/README.md)

**如果您希望支持其他翻譯語言，請參考 [此處](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md)**

## 簡介

歡迎來到 **初學者的邊緣人工智慧課程**——這是一個全面探索邊緣人工智慧世界的旅程。本課程將強大的人工智慧能力與實際的邊緣設備部署相結合，幫助您直接在數據生成和需要做出決策的地方發揮人工智慧的潛力。

### 您將掌握的技能

本課程將帶您從基礎概念到生產級實施，涵蓋：
- **小型語言模型（SLMs）**，針對邊緣部署進行優化
- **硬體感知優化**，適用於多種平台
- **隱私保護的即時推理**
- **生產部署**策略，適用於企業應用

### 為什麼邊緣人工智慧很重要

邊緣人工智慧代表了一種解決現代關鍵挑戰的全新模式：
- **隱私與安全**：在本地處理敏感數據，避免雲端暴露
- **即時性能**：消除網絡延遲，適用於時間敏感的應用
- **成本效益**：降低帶寬和雲端計算成本
- **韌性運作**：在網絡中斷期間保持功能
- **法規遵從**：滿足數據主權要求

### 邊緣人工智慧

邊緣人工智慧是指在硬體上本地運行人工智慧算法和語言模型，靠近數據生成的地方，而不依賴雲端資源進行推理。它減少了延遲，增強了隱私，並實現了即時決策。

### 核心原則：
- **設備上的推理**：人工智慧模型在邊緣設備（如手機、路由器、微控制器、工業電腦）上運行
- **離線能力**：無需持續的網絡連接即可運行
- **低延遲**：適合即時系統的快速響應
- **數據主權**：保持敏感數據本地化，提高安全性和合規性

### 小型語言模型（SLMs）

像 Phi-4、Mistral-7B 和 Gemma 這樣的 SLMs 是更大 LLMs 的優化版本——通過訓練或蒸餾實現：
- **減少內存佔用**：有效利用有限的邊緣設備內存
- **降低計算需求**：針對 CPU 和邊緣 GPU 性能進行優化
- **更快的啟動時間**：快速初始化，適合響應式應用

它們在滿足以下限制的同時解鎖了強大的自然語言處理能力：
- **嵌入式系統**：物聯網設備和工業控制器
- **移動設備**：具有離線功能的智能手機和平板電腦
- **物聯網設備**：資源有限的傳感器和智能設備
- **邊緣伺服器**：具有有限 GPU 資源的本地處理單元
- **個人電腦**：桌面和筆記本電腦的部署場景

## 課程模組與導航

| 模組 | 主題 | 重點領域 | 主要內容 | 等級 | 時長 |
|--------|-------|------------|-------------|--------|----------|
| [📖 00 ](./introduction.md) | [邊緣人工智慧簡介](./introduction.md) | 基礎與背景 | 邊緣人工智慧概述 • 行業應用 • SLM 簡介 • 學習目標 | 初學者 | 1-2 小時 |
| [📚 01](../../Module01) | [邊緣人工智慧基礎](./Module01/README.md) | 雲端與邊緣人工智慧比較 | 邊緣人工智慧基礎 • 真實案例研究 • 實施指南 • 邊緣部署 | 初學者 | 3-4 小時 |
| [🧠 02](../../Module02) | [SLM 模型基礎](./Module02/README.md) | 模型家族與架構 | Phi 家族 • Qwen 家族 • Gemma 家族 • BitNET • μModel • Phi-Silica | 初學者 | 4-5 小時 |
| [🚀 03](../../Module03) | [SLM 部署實踐](./Module03/README.md) | 本地與雲端部署 | 高級學習 • 本地環境 • 雲端部署 | 中級 | 4-5 小時 |
| [⚙️ 04](../../Module04) | [模型優化工具包](./Module04/README.md) | 跨平台優化 | 簡介 • Llama.cpp • Microsoft Olive • OpenVINO • Apple MLX • 工作流程綜合 | 中級 | 5-6 小時 |
| [🔧 05](../../Module05) | [SLMOps 生產](./Module05/README.md) | 生產運營 | SLMOps 簡介 • 模型蒸餾 • 微調 • 生產部署 | 高級 | 5-6 小時 |
| [🤖 06](../../Module06) | [人工智慧代理與功能調用](./Module06/README.md) | 代理框架與 MCP | 代理簡介 • 功能調用 • 模型上下文協議 | 高級 | 4-5 小時 |
| [💻 07](../../Module07) | [平台實施](./Module07/README.md) | 跨平台範例 | 人工智慧工具包 • Foundry Local • Windows 開發 | 高級 | 3-4 小時 |
| [🏭 08](../../Module08) | [Foundry Local 工具包](./Module08/README.md) | 生產級範例 | 範例應用（詳情見下） | 專家 | 8-10 小時 |

### 🏭 **模組 08：範例應用**

- [01: REST 聊天快速入門](./Module08/samples/01/README.md)
- [02: OpenAI SDK 集成](./Module08/samples/02/README.md)
- [03: 模型發現與基準測試](./Module08/samples/03/README.md)
- [04: Chainlit RAG 應用](./Module08/samples/04/README.md)
- [05: 多代理協調](./Module08/samples/05/README.md)
- [06: 作為工具的模型路由器](./Module08/samples/06/README.md)
- [07: 直接 API 客戶端](./Module08/samples/07/README.md)
- [08: Windows 11 聊天應用](./Module08/samples/08/README.md)
- [09: 高級多代理系統](./Module08/samples/09/README.md)
- [10: Foundry 工具框架](./Module08/samples/10/README.md)

### 🎓 **工作坊：實踐學習路徑**

提供全面的實踐工作坊材料，包含生產級實施：

- **[工作坊指南](./Workshop/Readme.md)** - 完整的學習目標、成果和資源導航
- **Python 範例**（6 節課）- 更新最佳實踐、錯誤處理和全面文檔
- **Jupyter 筆記本**（8 個互動式）- 包含基準測試和性能監控的逐步教程
- **課程指南** - 每節工作坊課程的詳細 Markdown 指南
- **驗證工具** - 用於驗證代碼質量和運行煙霧測試的腳本

**您將構建的內容：**
- 支持流式傳輸的本地人工智慧聊天應用
- 帶有質量評估（RAGAS）的 RAG 管道
- 多模型基準測試和比較工具
- 多代理協調系統
- 智能模型路由，基於任務選擇

### 📊 **學習路徑摘要**
- **總時長**：36-45 小時
- **初學者路徑**：模組 01-02（7-9 小時）  
- **中級路徑**：模組 03-04（9-11 小時）
- **高級路徑**：模組 05-07（12-15 小時）
- **專家路徑**：模組 08（8-10 小時）

## 您將構建的內容

### 🎯 核心能力
- **邊緣人工智慧架構**：設計本地優先的人工智慧系統，並與雲端集成
- **模型優化**：量化和壓縮模型以進行邊緣部署（提升速度 85%，減少大小 75%）
- **多平台部署**：Windows、移動設備、嵌入式系統和雲端-邊緣混合系統
- **生產運營**：監控、擴展及維護生產中的邊緣人工智能

### 🏗️ 實踐項目
- **Foundry 本地聊天應用**：Windows 11 原生應用，支持模型切換
- **多代理系統**：協調器與專家代理，用於複雜工作流程
- **RAG 應用**：使用向量搜索進行本地文件處理
- **模型路由器**：基於任務分析的智能模型選擇
- **API 框架**：具備流式傳輸和健康監控功能的生產級客戶端
- **跨平台工具**：LangChain/Semantic Kernel 集成模式

### 🏢 行業應用
**製造業** • **醫療保健** • **自動駕駛車輛** • **智慧城市** • **移動應用**

## 快速入門

**推薦學習路徑**（總計 20-30 小時）：

0. **📖 介紹** ([Introduction.md](./introduction.md))：邊緣人工智能基礎 + 行業背景 + 學習框架  
1. **📚 基礎**（模組 01-02）：邊緣人工智能概念 + SLM 模型家族  
2. **⚙️ 優化**（模組 03-04）：部署 + 量化框架  
3. **🚀 生產**（模組 05-06）：SLMOps + 人工智能代理 + 函數調用  
4. **💻 實施**（模組 07-08）：平台範例 + Foundry 本地工具包  

每個模組包含理論、實踐練習及生產級代碼範例。

## 職業影響

**技術職位**：邊緣人工智能解決方案架構師 • 機器學習工程師（邊緣） • 物聯網人工智能開發者 • 移動人工智能開發者  

**行業領域**：製造業 4.0 • 醫療技術 • 自動化系統 • 金融科技 • 消費電子  

**作品集項目**：多代理系統 • 生產級 RAG 應用 • 跨平台部署 • 性能優化  

## 資源結構

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

✅ **漸進式學習**：理論 → 實踐 → 生產部署  
✅ **真實案例研究**：Microsoft、日本航空、企業實施案例  
✅ **動手範例**：50+ 範例，10 個全面的 Foundry 本地演示  
✅ **性能優化**：提升 85% 的速度，減少 75% 的大小  
✅ **多平台支持**：Windows、移動端、嵌入式、雲邊緣混合  
✅ **生產準備**：監控、擴展、安全性、合規框架  

📖 **[學習指南](STUDY_GUIDE.md)**：結構化的 20 小時學習路徑，包含時間分配指導和自我評估工具。

---

**邊緣人工智能代表了人工智能部署的未來**：本地優先、保護隱私、高效。掌握這些技能，打造下一代智能應用。

## 其他課程

我們的團隊還提供其他課程！查看以下內容：

### Azure / Edge / MCP / Agents
[![AZD 初學者指南](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)  
[![邊緣人工智能初學者指南](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)  
[![MCP 初學者指南](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)  
[![人工智能代理初學者指南](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---

### 生成式人工智能系列
[![生成式人工智能初學者指南](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)  
[![生成式人工智能 (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)  
[![生成式人工智能 (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)  
[![生成式人工智能 (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---

### 核心學習
[![機器學習初學者指南](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)  
[![數據科學初學者指南](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)  
[![人工智能初學者指南](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)  
[![網絡安全初學者指南](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)  
[![Web 開發初學者指南](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)  
[![物聯網初學者指南](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)  
[![XR 開發初學者指南](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---

### Copilot 系列
[![Copilot AI 配對編程](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)  
[![Copilot C#/.NET](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)  
[![Copilot 冒險](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)

## 獲取幫助

如果您遇到困難或有關於構建人工智能應用的問題，請加入：

[![Azure AI Foundry Discord](https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

如果您有產品反饋或在構建過程中遇到錯誤，請訪問：

[![Azure AI Foundry Developer Forum](https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

**免責聲明**：  
本文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。儘管我們致力於提供準確的翻譯，請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於關鍵信息，建議使用專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或誤釋不承擔責任。
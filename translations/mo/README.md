<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c8de8ce76af1af156b1c2dee24ed23b0",
  "translation_date": "2025-12-24T23:10:26+00:00",
  "source_file": "README.md",
  "language_code": "mo"
}
-->
# EdgeAI 入門 


![課程封面圖片](../../translated_images/cover.eb18d1b9605d754b30973f4e17c6e11ea4f8473d9686ee378d6e7b44e3c70ac7.mo.png)

[![GitHub 貢獻者](https://img.shields.io/github/contributors/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/graphs/contributors)
[![GitHub 問題](https://img.shields.io/github/issues/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/issues)
[![GitHub 拉取請求](https://img.shields.io/github/issues-pr/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/pulls)
[![歡迎 PRs](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

請按以下步驟開始使用這些資源：

1. **Fork 倉庫**: 按一下 [![GitHub forks](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork)
2. **複製倉庫**:   `git clone https://github.com/microsoft/edgeai-for-beginners.git`
3. [**加入 Azure AI Foundry Discord 並與專家及其他開發者交流**](https://discord.com/invite/ByRwuEEgH4)


### 🌐 多語言支援

#### 透過 GitHub Action 支援（自動化且始終保持最新）

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[阿拉伯語](../ar/README.md) | [孟加拉語](../bn/README.md) | [保加利亞語](../bg/README.md) | [緬甸語（緬甸）](../my/README.md) | [中文（簡體）](../zh/README.md) | [中文（繁體，香港）](../hk/README.md) | [中文（繁體，澳門）](./README.md) | [中文（繁體，台灣）](../tw/README.md) | [克羅地亞語](../hr/README.md) | [捷克語](../cs/README.md) | [丹麥語](../da/README.md) | [荷蘭語](../nl/README.md) | [愛沙尼亞語](../et/README.md) | [芬蘭語](../fi/README.md) | [法語](../fr/README.md) | [德語](../de/README.md) | [希臘語](../el/README.md) | [希伯來語](../he/README.md) | [印地語](../hi/README.md) | [匈牙利語](../hu/README.md) | [印尼語](../id/README.md) | [義大利語](../it/README.md) | [日語](../ja/README.md) | [坎納達語](../kn/README.md) | [韓語](../ko/README.md) | [立陶宛語](../lt/README.md) | [馬來語](../ms/README.md) | [馬拉雅拉姆語](../ml/README.md) | [馬拉地語](../mr/README.md) | [尼泊爾語](../ne/README.md) | [尼日利亞皮欽語](../pcm/README.md) | [挪威語](../no/README.md) | [波斯語（Farsi）](../fa/README.md) | [波蘭語](../pl/README.md) | [葡萄牙語（巴西）](../br/README.md) | [葡萄牙語（葡萄牙）](../pt/README.md) | [旁遮普語（Gurmukhi）](../pa/README.md) | [羅馬尼亞語](../ro/README.md) | [俄語](../ru/README.md) | [塞爾維亞語（西里爾字母）](../sr/README.md) | [斯洛伐克語](../sk/README.md) | [斯洛文尼亞語](../sl/README.md) | [西班牙語](../es/README.md) | [斯瓦希里語](../sw/README.md) | [瑞典語](../sv/README.md) | [塔加洛語（菲律賓）](../tl/README.md) | [泰米爾語](../ta/README.md) | [泰盧固語](../te/README.md) | [泰語](../th/README.md) | [土耳其語](../tr/README.md) | [烏克蘭語](../uk/README.md) | [烏爾都語](../ur/README.md) | [越南語](../vi/README.md)
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

**如果您希望支援其他翻譯語言，請在[此處](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md) 查看支援清單**
## 介紹

歡迎閱讀 **EdgeAI for Beginners** — 帶你全面探索邊緣人工智慧（Edge AI）的變革性世界。本課程連結強大 AI 能力與在邊緣裝置上的實務部署，讓你能夠直接在資料生成與需要做出決策的地方運用 AI 的潛力。

### 你將掌握的內容

本課程將帶領你從基本概念到可投入生產的實作，涵蓋：
- **小型語言模型 (SLMs)**，為邊緣部署最佳化
- **跨不同平台的硬體感知優化**
- **具隱私保護能力的即時推論**
- **企業應用的生產部署策略**

### 為何 EdgeAI 很重要

Edge AI 代表一項範式轉移，能夠解決當代關鍵挑戰：
- **隱私與安全**：在本地處理敏感資料，不必曝露至雲端
- **即時效能**：為時間敏感的應用消除網路延遲
- **成本效益**：降低頻寬與雲端運算費用
- **韌性操作**：在網路中斷期間維持功能
- **法規遵循**：符合資料主權的要求

### 邊緣 AI

邊緣 AI 指的是在靠近資料生成來源的硬體上本地執行 AI 演算法與語言模型，在推論時不依賴雲端資源。它能降低延遲、提升隱私，並啟用即時決策。

### 核心原則:
- **裝置端推論**：AI 模型在邊緣裝置上執行（手機、路由器、微控制器、工業電腦）
- **離線能力**：在無持續網際網路連線下仍能運作
- **低延遲**：即時回應，適合即時系統
- **資料主權**：將敏感資料保留於本地，提升安全性與合規性

### 小型語言模型（SLMs）

像 Phi-4、Mistral-7B 與 Gemma 等 SLMs，是較大型 LLMs 的優化版本——透過訓練或蒸餾達成：
- **降低記憶體佔用**：有效使用受限的邊緣裝置記憶體
- **降低計算需求**：針對 CPU 與邊緣 GPU 的效能進行最佳化
- **更快速的啟動時間**：快速初始化以提供響應式應用

它們在滿足下列限制條件的同時，釋放強大的自然語言處理能力：
- **嵌入式系統**：物聯網裝置與工業控制器
- **行動裝置**：具有離線能力的智慧型手機和平板
- **物聯網裝置**：資源受限的感測器與智慧裝置
- **邊緣伺服器**：具有有限 GPU 資源的本地處理單元
- **個人電腦**：桌上型與筆電的部署情境

## 課程模組與導覽

| 模組 | 主題 | 焦點領域 | 主要內容 | 等級 | 時長 |
|--------|-------|------------|-------------|--------|----------|
| [📖 00 ](./introduction.md) | [EdgeAI 介紹](./introduction.md) | 基礎與脈絡 | EdgeAI 概述 • 產業應用 • SLM 介紹 • 學習目標 | 初學者 | 1-2 小時 |
| [📚 01](../../Module01) | [EdgeAI 基礎](./Module01/README.md) | 雲端與邊緣 AI 比較 | EdgeAI 基礎 • 實務案例研究 • 實作指南 • 邊緣部署 | 初學者 | 3-4 小時 |
| [🧠 02](../../Module02) | [SLM 模型基礎](./Module02/README.md) | 模型家族與架構 | Phi 家族 • Qwen 家族 • Gemma 家族 • BitNET • μModel • Phi-Silica | 初學者 | 4-5 小時 |
| [🚀 03](../../Module03) | [SLM 部署實務](./Module03/README.md) | 本地與雲端部署 | 進階學習 • 本地環境 • 雲端部署 | 中階 | 4-5 小時 |
| [⚙️ 04](../../Module04) | [模型優化工具組](./Module04/README.md) | 跨平台優化 | 介紹 • Llama.cpp • Microsoft Olive • OpenVINO • Apple MLX • 工作流程整合 | 中階 | 5-6 小時 |
| [🔧 05](../../Module05) | [SLMOps 生產](./Module05/README.md) | 生產營運 | SLMOps 介紹 • 模型蒸餾 • 微調 • 生產部署 | 進階 | 5-6 小時 |
| [🤖 06](../../Module06) | [AI 代理與函數呼叫](./Module06/README.md) | 代理框架與 MCP | 代理介紹 • 函數呼叫 • 模型上下文協議 | 進階 | 4-5 小時 |
| [💻 07](../../Module07) | [平台實作](./Module07/README.md) | 跨平台範例 | AI 工具組 • Foundry Local • Windows 開發 | 進階 | 3-4 小時 |
| [🏭 08](../../Module08) | [Foundry Local 工具組](./Module08/README.md) | 可投入生產的範例 | 範例應用（見下方詳情） | 專家 | 8-10 小時 |

### 🏭 **模組 08：範例應用**

- [01: REST 聊天 快速入門](./Module08/samples/01/README.md)
- [02: OpenAI SDK 整合](./Module08/samples/02/README.md)
- [03: 模型探索與基準測試](./Module08/samples/03/README.md)
- [04: Chainlit RAG 應用](./Module08/samples/04/README.md)
- [05: 多代理協同編排](./Module08/samples/05/README.md)
- [06: 模型即工具路由器](./Module08/samples/06/README.md)
- [07: 直接 API 用戶端](./Module08/samples/07/README.md)
- [08: Windows 11 聊天應用](./Module08/samples/08/README.md)
- [09: 進階多代理系統](./Module08/samples/09/README.md)
- [10: Foundry 工具框架](./Module08/samples/10/README.md)

### 🎓 **工作坊：實作學習路徑**

完整的實作工作坊教材，包含可投入生產的實作：

- **[工作坊指南](./Workshop/Readme.md)** - 完整的學習目標、成果與資源導覽
- **Python 範例** (6 堂課) - 已更新最佳實務、錯誤處理與完整文件
- **Jupyter 筆記本** (8 個互動式) - 逐步教學，包含基準測試與效能監控
- **課程指南** - 每堂工作坊課程的詳細 Markdown 指南
- **驗證工具** - 用於驗證程式碼品質與執行冒煙測試的腳本

你將建立的項目：
- 支援串流的本地 AI 聊天應用程式
- 具品質評估的 RAG 流程（RAGAS）
- 多模型基準測試與比較工具
- 多代理編排系統
- 具任務導向選擇的智慧模型路由

### 📊 **學習路徑摘要**
- **總時長**：36-45 小時
- **入門路徑**：模組 01-02（7-9 小時）  
- **中階路徑**：模組 03-04（9-11 小時）
- **進階路徑**：模組 05-07（12-15 小時）
- **專家路徑**：模組 08（8-10 小時）

## 你將建立的項目

### 🎯 核心能力
- **邊緣 AI 架構**：設計以本地為先、並整合雲端的 AI 系統
- **模型優化**: 量化並壓縮模型以用於邊緣部署 (85% 加速, 75% 大小縮減)
- **多平台部署**: Windows、行動裝置、嵌入式，與雲端-邊緣混合系統
- **生產運維**: 在生產環境中監控、擴展及維護邊緣 AI

### 🏗️ 實務專案
- **Foundry 本地聊天應用程式**: Windows 11 原生應用程式，支援模型切換
- **多智能體系統**: 協調者與專家代理人以處理複雜工作流程  
- **RAG 應用程式**: 本地文件處理，結合向量搜尋
- **模型路由器**: 基於任務分析在模型之間進行智慧選擇
- **API 框架**: 生產就緒的客戶端，具串流與健康監控
- **跨平台工具**: LangChain/Semantic Kernel 整合模式

### 🏢 產業應用
**製造業** • **醫療保健** • **自駕車** • **智慧城市** • **行動應用程式**

## 快速上手

**推薦學習路徑** (總計20-30小時):

0. **📖 介紹** ([Introduction.md](./introduction.md)): 邊緣 AI 基礎 + 產業脈絡 + 學習框架
1. **📚 基礎** (Modules 01-02): 邊緣 AI 概念 + SLM 模型家族
2. **⚙️ 優化** (Modules 03-04): 部署 + 量化框架  
3. **🚀 生產** (Modules 05-06): SLMOps + AI 代理人 + 函數呼叫
4. **💻 實作** (Modules 07-08): 平台範例 + Foundry Local 工具包

Each module includes theory, hands-on exercises, and production-ready code samples.

## 職涯影響

**技術職務**: 邊緣 AI 解決方案架構師 • 機器學習工程師（邊緣） • 物聯網 AI 開發者 • 行動 AI 開發者

**產業領域**: 工業 4.0 • 醫療科技 • 自主系統 • 金融科技 • 消費性電子

**作品集專案**: 多智能體系統 • 生產級 RAG 應用 • 跨平台部署 • 效能優化

## 儲存庫結構

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

✅ **循序漸進學習**: 理論 → 實作 → 生產部署  
✅ **實際案例研究**: Microsoft、日本航空、企業實作  
✅ **實作範例**: 50+ 範例, 10 個完整 Foundry Local 示範  
✅ **效能導向**: 85% 加速, 75% 大小縮減  
✅ **多平台**: Windows、行動、嵌入式、雲端-邊緣混合  
✅ **生產就緒**: 監控、擴展、安全、合規框架

📖 **[學習指南可用](STUDY_GUIDE.md)**: 結構化 20 小時學習路徑，包含時間分配指引與自我評估工具。

---

**邊緣 AI 代表 AI 部署的未來**: 本地優先、保護隱私且高效率。掌握這些技能以建構下一代智慧應用。

## 其他課程

Our team produces other courses! Check out:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j 入門](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js 入門](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)

---

### Azure / Edge / MCP / Agents
[![AZD 入門](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![邊緣 AI 入門](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP 入門](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![AI 代理人入門](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### 生成式 AI 系列
[![生成式 AI 入門](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![生成式 AI（.NET）](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![生成式 AI（Java）](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![生成式 AI（JavaScript）](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### 核心學習
[![機器學習入門](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![資料科學入門](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![AI 入門](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![網路安全入門](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![網頁開發入門](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![物聯網入門](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![XR 開發入門](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Copilot 系列
[![Copilot 用於 AI 配對程式設計](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot（C#/.NET）](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot 冒險](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## 尋求協助

If you get stuck or have any questions about building AI apps, join:

[![Microsoft Foundry 的 Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

If you have product feedback or errors while building visit:

[![Microsoft Foundry 開發者論壇](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
免責聲明：
本文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意自動翻譯可能包含錯誤或不準確之處。原文（原始語言版本）應視為具權威性的來源。對於關鍵資訊，建議採用專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或錯誤詮釋承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
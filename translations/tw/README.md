<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8421c922085232ba081c848d98f69f35",
  "translation_date": "2026-01-01T10:21:59+00:00",
  "source_file": "README.md",
  "language_code": "tw"
}
-->
# EdgeAI 入門 


![課程封面圖片](../../translated_images/cover.eb18d1b9605d754b.tw.png)

[![GitHub 貢獻者](https://img.shields.io/github/contributors/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/graphs/contributors)
[![GitHub 問題](https://img.shields.io/github/issues/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/issues)
[![GitHub 拉取請求](https://img.shields.io/github/issues-pr/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/pulls)
[![歡迎 PRs](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

按照以下步驟開始使用這些資源：

1. **Fork 這個儲存庫**：點擊 [![GitHub forks](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork)
2. **複製儲存庫**：   `git clone https://github.com/microsoft/edgeai-for-beginners.git`
3. [**加入 Azure AI Foundry Discord，與專家和其他開發者互動**](https://discord.com/invite/ByRwuEEgH4)


### 🌐 多語言支援

#### 透過 GitHub Action 支援（自動化且持續更新）

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[阿拉伯語](../ar/README.md) | [孟加拉語](../bn/README.md) | [保加利亞語](../bg/README.md) | [緬甸語 (Myanmar)](../my/README.md) | [中文（簡體）](../zh/README.md) | [中文（繁體，香港）](../hk/README.md) | [中文（繁體，澳門）](../mo/README.md) | [中文（繁體，台灣）](./README.md) | [克羅埃西亞語](../hr/README.md) | [捷克語](../cs/README.md) | [丹麥語](../da/README.md) | [荷蘭語](../nl/README.md) | [愛沙尼亞語](../et/README.md) | [芬蘭語](../fi/README.md) | [法語](../fr/README.md) | [德語](../de/README.md) | [希臘語](../el/README.md) | [希伯來語](../he/README.md) | [印地語](../hi/README.md) | [匈牙利語](../hu/README.md) | [印尼語](../id/README.md) | [義大利語](../it/README.md) | [日語](../ja/README.md) | [卡納達語](../kn/README.md) | [韓語](../ko/README.md) | [立陶宛語](../lt/README.md) | [馬來語](../ms/README.md) | [馬拉雅拉姆語](../ml/README.md) | [馬拉地語](../mr/README.md) | [尼泊爾語](../ne/README.md) | [尼日利亞皮欽語](../pcm/README.md) | [挪威語](../no/README.md) | [波斯語（Farsi）](../fa/README.md) | [波蘭語](../pl/README.md) | [葡萄牙語（巴西）](../br/README.md) | [葡萄牙語（葡萄牙）](../pt/README.md) | [旁遮普語（Gurmukhi）](../pa/README.md) | [羅馬尼亞語](../ro/README.md) | [俄語](../ru/README.md) | [塞爾維亞語（西里爾字母）](../sr/README.md) | [斯洛伐克語](../sk/README.md) | [斯洛文尼亞語](../sl/README.md) | [西班牙語](../es/README.md) | [斯瓦希里語](../sw/README.md) | [瑞典語](../sv/README.md) | [他加祿語（菲律賓）](../tl/README.md) | [泰米爾語](../ta/README.md) | [泰盧固語](../te/README.md) | [泰語](../th/README.md) | [土耳其語](../tr/README.md) | [烏克蘭語](../uk/README.md) | [烏爾都語](../ur/README.md) | [越南語](../vi/README.md)
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

**如果您希望新增其他翻譯語言，支援清單列在 [這裡](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md)**
## 介紹

歡迎來到 **EdgeAI 入門** – 您進入邊緣人工智慧變革世界的完整學習旅程。本課程銜接強大 AI 能力與在邊緣裝置上實際部署的實務，讓您能在資料產生與決策需要發生的地方直接運用 AI 的潛力。

### 你將掌握的內容

本課程將帶您從基本概念到可投入生產的實作，涵蓋：
- **小型語言模型 (SLMs)**，針對邊緣部署最佳化
- **硬體感知的優化**，適用多樣化平台
- **即時推論**，具備隱私保護能力
- **生產部署** 策略，應用於企業場景

### 為什麼 EdgeAI 重要

邊緣 AI 代表一種範式轉移，可解決現代關鍵挑戰：
- **隱私與安全**：在本地處理敏感資料，避免上傳雲端
- **即時效能**：消除網路延遲，適用於時效要求高的應用
- **成本效益**：降低頻寬與雲端運算支出
- **韌性營運**：在網路中斷時仍維持功能
- **法規遵循**：滿足資料主權需求

### 邊緣 AI

邊緣 AI 指的是在接近資料產生來源的硬體上本地執行 AI 演算法與語言模型，而不依賴雲端資源進行推論。它能降低延遲、強化隱私，並實現即時決策。

### 核心原則：
- **裝置端推論**：AI 模型在邊緣裝置上執行（手機、路由器、微控制器、工業電腦）
- **離線能力**：可在無持續網際網路連線下運行
- **低延遲**：對即時系統提供快速回應
- **資料主權**：將敏感資料保留在本地，提升安全性與合規性

### 小型語言模型 (SLMs)

像 Phi-4、Mistral-7B 與 Gemma 等 SLMs，是經過優化的較大型 LLMs 版本—透過訓練或蒸餾達成：
- **降低記憶體佔用**：在有限的邊緣裝置記憶體中更有效率
- **降低運算需求**：針對 CPU 與邊緣 GPU 的效能最佳化
- **更快啟動時間**：快速初始化以達到即時回應

它們在滿足以下限制條件的同時，解鎖強大的自然語言處理能力：
- **嵌入式系統**：物聯網裝置與工業控制器
- **行動裝置**：具離線能力的智慧型手機和平板
- **物聯網裝置**：資源有限的感測器與智慧裝置
- **邊緣伺服器**：具有限 GPU 資源的在地處理單元
- **個人電腦**：桌機與筆電的部署情境

## 課程模組與導覽

| Module | Topic | Focus Area | Key Content | Level | Duration |
|--------|-------|------------|-------------|--------|----------|
| [📖 00 ](./introduction.md) | [EdgeAI 介紹](./introduction.md) | 基礎與背景 | EdgeAI 概述 • 產業應用 • SLM 介紹 • 學習目標 | 初學者 | 1-2 hrs |
| [📚 01](../../Module01) | [EdgeAI 基礎](./Module01/README.md) | 雲端與邊緣 AI 比較 | EdgeAI 基礎 • 真實案例研究 • 實作指南 • 邊緣部署 | 初學者 | 3-4 hrs |
| [🧠 02](../../Module02) | [SLM 模型基礎](./Module02/README.md) | 模型家族與架構 | Phi 系列 • Qwen 系列 • Gemma 系列 • BitNET • μModel • Phi-Silica | 初學者 | 4-5 hrs |
| [🚀 03](../../Module03) | [SLM 部署實作](./Module03/README.md) | 本地與雲端部署 | 進階學習 • 本地環境 • 雲端部署 | 中階 | 4-5 hrs |
| [⚙️ 04](../../Module04) | [模型最佳化工具包](./Module04/README.md) | 跨平台最佳化 | 介紹 • Llama.cpp • Microsoft Olive • OpenVINO • Apple MLX • 工作流程綜合 | 中階 | 5-6 hrs |
| [🔧 05](../../Module05) | [SLMOps 生產運維](./Module05/README.md) | 生產運維作業 | SLMOps 介紹 • 模型蒸餾 • 微調 • 生產部署 | 進階 | 5-6 hrs |
| [🤖 06](../../Module06) | [AI 代理人與函數呼叫](./Module06/README.md) | 代理框架與 MCP | 代理人介紹 • 函數呼叫 • 模型上下文協定 | 進階 | 4-5 hrs |
| [💻 07](../../Module07) | [平台實作](./Module07/README.md) | 跨平台範例 | AI 工具包 • Foundry Local • Windows 開發 | 進階 | 3-4 hrs |
| [🏭 08](../../Module08) | [Foundry Local 工具包](./Module08/README.md) | 生產就緒範例 | 範例應用（詳情見下） | 專家 | 8-10 hrs |

### 🏭 **模組 08：範例應用**

- [01: REST Chat 快速上手](./Module08/samples/01/README.md)
- [02: OpenAI SDK 整合](./Module08/samples/02/README.md)
- [03: 模型發現與基準測試](./Module08/samples/03/README.md)
- [04: Chainlit RAG 應用](./Module08/samples/04/README.md)
- [05: 多代理人協調](./Module08/samples/05/README.md)
- [06: Models-as-Tools 路由器](./Module08/samples/06/README.md)
- [07: 直接 API 客戶端](./Module08/samples/07/README.md)
- [08: Windows 11 聊天應用](./Module08/samples/08/README.md)
- [09: 進階多代理系統](./Module08/samples/09/README.md)
- [10: Foundry 工具框架](./Module08/samples/10/README.md)

### 🎓 **工作坊：實作學習路徑**

完整的實作工作坊教材，含可投入生產的實作範例：

- **[工作坊指南](./Workshop/Readme.md)** - 完整的學習目標、成果與資源導覽
- **Python 範例** (6 堂) - 已更新最佳實務、錯誤處理與完整文件
- **Jupyter 筆記本** (8 個互動式) - 逐步教學含基準與效能監控
- **課程指南** - 每個工作坊場次的詳細 markdown 指南
- **驗證工具** - 驗證程式碼品質與執行煙霧測試的腳本

**你將會建置：**
- 支援串流的本地 AI 聊天應用
- 具品質評估的 RAG 管線（RAGAS）
- 多模型基準比較工具
- 多代理人協調系統
- 基於任務選擇的智慧模型路由

### 📊 **學習路徑摘要**
- **總時長**：36-45 小時
- **初學者路徑**：模組 01-02（7-9 小時）  
- **中階路徑**：模組 03-04（9-11 小時）
- **進階路徑**：模組 05-07（12-15 小時）
- **專家路徑**：模組 08（8-10 小時）

## 你將會建置

### 🎯 核心能力
- **Edge AI 架構**：設計以本地為先並結合雲端的 AI 系統
- **模型最佳化**：對模型進行量化與壓縮以利邊緣部署（加速 85%，縮減大小 75%）
- **多平台部署**：Windows、行動、嵌入式與雲端-邊緣混合系統
- **生產營運**：監控、擴展與維運邊緣 AI 於生產環境

### 🏗️ Practical Projects
- **Foundry Local 聊天應用程式**：具模型切換功能的 Windows 11 原生應用程式
- **多代理系統**：由協調者與專精代理組成以處理複雜工作流程  
- **RAG 應用程式**：具向量搜尋的本地文件處理
- **模型路由**：根據任務分析於模型之間進行智慧選擇
- **API 框架**：具串流與健康監控的生產可用客戶端
- **跨平台工具**：LangChain/Semantic Kernel 整合範式

### 🏢 Industry Applications
**製造業** • **醫療** • **自駕車** • **智慧城市** • **行動應用程式**

## Quick Start

**建議學習路徑** (總計 20-30 小時):

0. **📖 介紹** ([Introduction.md](./introduction.md)): EdgeAI 基礎 + 產業脈絡 + 學習框架
1. **📚 基礎** (Modules 01-02): EdgeAI 概念 + SLM 模型家族
2. **⚙️ 最佳化** (Modules 03-04): 部署 + 量化框架  
3. **🚀 生產** (Modules 05-06): SLMOps + AI 代理 + 函數呼叫
4. **💻 實作** (Modules 07-08): 平台範例 + Foundry Local 工具包

每個模組包含理論、實作練習與可投入生產的程式碼範例。

## Career Impact

**技術職務**：EdgeAI 解決方案架構師 • ML 工程師（Edge） • IoT AI 開發者 • 行動 AI 開發者

**產業領域**：智慧製造 4.0 • 醫療科技 • 自主系統 • 金融科技 • 消費性電子

**作品集專案**：多代理系統 • 生產級 RAG 應用 • 跨平台部署 • 效能最佳化

## Repository Structure

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

✅ **漸進式學習**：理論 → 實作 → 投產部署  
✅ **實際案例研究**：Microsoft、Japan Airlines、企業實作  
✅ **實作範例**：50+ 範例、10 個完整的 Foundry Local 示範  
✅ **效能重點**：加速 85%、縮減大小 75%  
✅ **多平台支援**：Windows、行動、嵌入式、雲端-邊緣混合  
✅ **可投入生產**：監控、擴展、安全性、合規性框架

📖 **[學習指南](STUDY_GUIDE.md)**: 有結構的 20 小時學習路徑，包含時間分配指引與自我評估工具。

---

**EdgeAI 代表 AI 部署的未來**：以本地為優先、保護隱私且高效率。掌握這些技能以打造下一代智慧應用。

## 其他課程

Our team produces other courses! Check out:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j 入門](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js 入門](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)

---

### Azure / Edge / MCP / Agents
[![AZD 入門](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Edge AI 入門](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP 入門](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![AI Agents 入門](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Generative AI Series
[![Generative AI 入門](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Generative AI (.NET) 入門](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![Generative AI (Java) 入門](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![Generative AI (JavaScript) 入門](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### 核心學習
[![ML 入門](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![資料科學 入門](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![AI 入門](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![資安 入門](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![網頁開發 入門](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![IoT 入門](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![XR 開發 入門](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Copilot 系列
[![Copilot：AI 配對程式設計](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot：C#/.NET](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot 冒險](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## 取得協助

如果你遇到卡關或對建立 AI 應用有任何問題，加入：

[![Microsoft Foundry Discord 伺服器](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

如果你在開發時有產品回饋或遭遇錯誤，請造訪：

[![Microsoft Foundry 開發者論壇](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原文應被視為具權威性的版本。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤譯負責。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
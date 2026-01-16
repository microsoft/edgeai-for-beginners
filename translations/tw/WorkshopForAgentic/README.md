<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f94e745264597bc5d8df967ead2eff97",
  "translation_date": "2026-01-05T10:26:36+00:00",
  "source_file": "WorkshopForAgentic/README.md",
  "language_code": "tw"
}
-->
# 🎙️ AI 播客工作室工作坊

> 🌏 [中文版 (Chinese Version)](translation/zh-cn/README.md)

![logo](../../../translated_images/tw/logo.8711e39dc8257d7b.webp)

## 你的任務

歡迎來到 **AI 播客工作室**！你即將啟動自己的科技播客，名為「Future Bytes」——但有個轉折點：你將建立一支 AI 驅動的製作團隊來幫助你創作它。不需再花費無盡時間做研究、撰寫腳本和音頻編輯。取而代之的是，你將以程式設計的方式，成為擁有 AI 超能力的播客製作人。

## 故事背景

想像一下：你和朋友想開一個聊最酷科技趨勢的播客，但大家都忙於課業、工作，還有生活。如果你能打造一組 AI 代理人來分擔重任怎麼辦？一個代理人負責研究主題，另一個撰寫吸引人的腳本，第三個將文字變成自然流暢的對話。聽起來像科幻嗎？讓我們把它變成現實。

## 你將學到什麼

完成此工作坊後，你將知道如何：
- 🤖 部署你自己的本地 AI 模型（無 API 費用，無雲端依賴！）
- 🔧 建立實際合作的專屬 AI 代理人
- 🎬 從構想到音訊，打造完整播客製作流程

## 你的旅程：三幕劇

![arch](../../../translated_images/tw/arch.5965fe504e4a3a93.webp)

像所有好故事一樣，我們分成三幕。每幕逐步建立你的 AI 播客工作室：

| 集數 | 你的任務 | 發生什麼事 | 解鎖技能 |
|---------|-----------|--------------|----------------|
| **第一幕** | [認識你的 AI 助手](md/01.BuildAIAgentWithSLM.md) | 你將學會如何創造能聊天、搜尋網路、甚至解決問題的 AI 代理人。想像它們是永不停歇的研究實習生。 | 🎯 建立你的第一個代理人<br>🛠️ 賦予超能力（工具！）<br>🧠 教它思考<br>🌐 連接網際網路 |
| **第二幕** | [組建你的製作團隊](md/02.AIAgentOrchestrationAndWorkflows.md) | 現在事情變有趣了！你將協調多個 AI 代理人像真正的播客團隊一樣合作。一個研究，一個寫作，你來審核——團隊合作才能完成夢想。 | 🎭 協調多個代理人<br>🔄 建立審核工作流程<br>🖥️ 使用 DevUI 介面測試<br>✋ 保持人為掌控 |
| **第三幕** | [讓你的播客活起來](md/03.Multi-SpeakerPodcastGenerationWithVibeVoice.md) | 大結局！將你的文字腳本轉換成真實的播客音訊，擁有逼真的聲音和自然的對話。你的「Future Bytes」播客準備好發佈了！ | 🎤 文字轉語音魔法<br>👥 多說話者聲音<br>⏱️ 長音頻輸出<br>🚀 完全自動化 |

每幕都會解鎖新能力。若你夠勇敢可以直接跳過，但我們建議跟著故事走！

## 環境需求

本工作坊支援多種硬體環境：
- **CPU**：適合測試與小規模使用
- **GPU**：建議用於生產環境，大幅提升推理速度
- **NPU**：支援次世代神經處理器加速

## 你需要準備什麼

### 軟體清單 ✅
- **Python 3.10+**（你的程式語言）
- **Ollama**（在本機執行 AI 模型）
- **VS Code**（你的程式編輯器）
- **Python 擴充套件**（讓 VS Code 更智慧）
- **Git**（用來抓程式碼）

### 硬體檢查 💻
- **能跑嗎？**：8GB 記憶體，10GB 可用空間（可用但可能較慢）
- **理想配置**：16GB 以上記憶體，良好 GPU（順暢體驗！）
- **有 NPU 嗎？**：更棒！解鎖次世代效能 🚀

## 建置你的工作室 🎬

### 第一步：Python 加速

確保你已安裝 Python 3.10 或更新版本：

```bash
python --version
# 應顯示 Python 3.10.x 或更高版本
```

還沒裝 Python？到 [python.org](https://python.org) 下載——完全免費！

### 第二步：取得 Ollama（你的 AI 模型執行器）

前往 [ollama.ai](https://ollama.ai) 下載適用你作業系統的 Ollama。它就像本地執行 AI 模型的引擎。

檢查是否已準備就緒：

```bash
ollama --version
```

### 第三步：下載你的 AI 大腦 🧠

現在下載 Qwen-3-8B 模型（就像是聘請你的第一位 AI 助手）：

```bash
ollama pull qwen3:8b
```

*這可能需要幾分鐘，是喝杯咖啡的好時機！☕*

### 第四步：安裝 VS Code

如果沒有的話，下載 [Visual Studio Code](https://code.visualstudio.com/)，這是最棒的程式編輯器（敢戰！😄）。

### 第五步：Python 擴充套件

在 VS Code 裡：
1. 按下 `Ctrl+Shift+X`（Mac 則是 `Cmd+Shift+X`）
2. 搜尋「Python」
3. 安裝官方 Microsoft Python 擴充套件

### 第六步：全部準備好了！🎉

認真說，你已經準備就緒，開始打造 AI 魔法吧！

### 第七步：安裝 Microsoft Agent Framework 與相關套件 📦

安裝所有工作坊需要的依賴：

```bash
pip install -r ./Installations/requirements.txt -U
```

*這會安裝 Microsoft Agent Framework 及所有必要套件。沖杯咖啡吧——第一次安裝可能要等幾分鐘！☕*

## 工作坊說明

詳細的專案結構、設定步驟以及執行方式都會在工作坊中逐步說明。

## 疑難排解（當狀況不如預期時）🔧

###「哎呀，模型下載速度超慢！」
**解決方法**：使用 VPN 或將 Ollama 設定為鏡像源。有時候網路就是不配合。

###「我的電腦快撐不住了！記憶體不足！」
**解決方法**：改用較小的模型，或調整 `num_ctx` 參數以減少記憶體佔用。可以把 AI 調整成輕量模式。

###「可以用 GPU 讓速度更快嗎？」
**解決方法**：Ollama 會自動偵測 GPU！只要確保 GPU 驅動是最新版本，就能免費提速！🏎️

## 額外資源（給好奇的你）📚

- [Ollama 文件](https://github.com/ollama/ollama) — 深入探討本地 AI 模型
- [Microsoft Agent Framework](https://microsoft.github.io/autogen/) — 了解更多關於建立代理人團隊
- [Qwen 模型資訊](https://qwenlm.github.io/) — 認識你的 AI 助手大腦

## 授權條款

MIT 授權條款——打造酷炫的東西，分享它，讓世界更美好！🌍

## 想要貢獻嗎？

發現漏洞？有好點子？歡迎提出 Issue 或 PR！我們熱愛社群互動。✨

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意自動翻譯可能包含錯誤或不準確之處。文件原文版本應視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯而產生之任何誤解或誤譯負責。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
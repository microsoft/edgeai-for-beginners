<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "aa775a734bda4590ecbe3a94a3b62197",
  "translation_date": "2026-01-05T17:28:24+00:00",
  "source_file": "WorkshopForAgentic/translation/zh-cn/README.md",
  "language_code": "hk"
}
-->
# 🎙️ AI 播客工作室工作坊

![logo](../../../../../translated_images/logo.8711e39dc8257d7b.hk.png)

## 你的任務

歡迎來到 **AI 播客工作室**！你即將推出自己的科技播客「未來字節」——但這裡有個轉折：你將構建一個 AI 驅動的製作團隊來幫助你創建它。不再需要無休止的研究、腳本編寫和音頻編輯。相反，你將透過編程成為擁有 AI 超能力的播客製作人。

## 故事背景

想像一下:你和朋友想開始一個關於最酷科技趨勢的播客,但每個人都忙於學習、工作或生活。如果你能構建一個 AI 智能體團隊來完成繁重的工作會怎樣?一個智能體負責研究主題,另一個編寫引人入勝的腳本,第三個將文本轉換為自然流暢的對話。聽起來像科幻小說?讓我們把它變成現實。

## 你將學到什麼

在本工作坊結束時,你將知道如何:
- 🤖 部署你自己的本地 AI 模型(無 API 費用,無雲依賴!)
- 🔧 構建實際協同工作的專業 AI 智能體
- 🎬 創建從創意到音頻的完整播客製作流程

## 你的旅程：三幕劇

就像任何好故事一樣，我們有三幕。每一幕都會逐步構建你的 AI 播客工作室：

| 章節 | 你的任務 | 發生什麼 | 解鎖技能 |
|---------|-----------|--------------|----------------|
| **第一幕** | [認識你的 AI 助手](01.BuildAIAgentWithSLM.md) | 你將發現如何創建能夠聊天、搜尋網絡、甚至解決問題的 AI 智能體。把它們想象成永不睡覺的研究實習生。 | 🎯 構建你的第一個智能體<br>🛠️ 賦予它超能力(工具!)<br>🧠 教它思考<br>🌐 連接到互聯網 |
| **第二幕** | [組建你的製作團隊](02.AIAgentOrchestrationAndWorkflows.md) | 現在事情變得有趣了!你將編排多個 AI 智能體像真正的播客團隊一樣協同工作。一個研究,一個寫作,你審批——團隊合作成就夢想。 | 🎭 協調多個智能體<br>🔄 構建審批工作流<br>🖥️ 使用 DevUI 界面測試<br>✋ 保持人類控制 |
| **第三幕** | [讓你的播客活起來](03.Multi-SpeakerPodcastGenerationWithVibeVoice.md) | 大結局！將你的文本腳本轉換成具有逼真聲音和自然對話的真實播客音頻。你的「未來字節」播客準備發布了！ | 🎤 文本轉語音魔法<br>👥 多說話人聲音<br>⏱️ 長格式音頻<br>🚀 完全自動化 |

每一幕都會解鎖新能力。如果你夠勇敢可以跳著看，但我們建議按順序學習！

## 環境要求

本工作坊支持各種硬體環境：
- **CPU**：適合測試和小規模使用
- **GPU**：推薦用於生產環境，顯著提升推理速度
- **NPU**：支持下一代神經處理單元加速

## 你需要什麼

### 軟體清單 ✅
- **Python 3.10+**（你的編程語言）
- **Ollama**（在你的機器上運行 AI 模型）
- **VS Code**（你的代碼編輯器）
- **Python 擴展**（讓 VS Code 更智能）
- **Git**（用於獲取代碼）

### 硬體檢查 💻
- **我能運行嗎？**：8GB 記憶體，10GB 可用空間（能用，但可能有點慢）
- **理想配置**：16GB+ 記憶體，一塊不錯的 GPU（順暢運行！）
- **有 NPU 嗎？**：那就更好了！解鎖下一代性能 🚀

## 搭建你的工作室 🎬

### 步驟 1：Python 升級

確保你有 Python 3.10 或更新版本：

```bash
python --version
# 應該顯示 Python 3.10.x 或更高版本
```

沒有 Python？從 [python.org](https://python.org) 獲取——它是免費的！

### 步驟 2：獲取 Ollama（你的 AI 模型運行器）

前往 [ollama.ai](https://ollama.ai) 下載適合你操作系統的 Ollama。把它想象成在本地運行 AI 模型的引擎。

檢查是否準備就緒：

```bash
ollama --version
```

### 步驟 3：下載你的 AI 大腦 🧠

是時候獲取 Qwen-3-8B 模型了（就像僱用你的第一個 AI 助手）：

```bash
ollama pull qwen3:8b
```

*這可能需要幾分鐘。完美的咖啡時間！☕*

### 步驟 4：設置 VS Code

如果你還沒有，獲取 [Visual Studio Code](https://code.visualstudio.com/)。這是最好的代碼編輯器（不服來辯 😄）。

### 步驟 5：Python 擴展

在 VS Code 中：
1. 按 `Ctrl+Shift+X`（Mac 上是 `Cmd+Shift+X`）
2. 搜尋 "Python"
3. 安裝官方的 Microsoft Python 擴展

### 步驟 6：大功告成！🎉

說真的，你準備好了。讓我們構建一些 AI 魔法吧！

### 步驟 7：安裝 Microsoft Agent Framework 和相關包 📦

安裝工作坊所需的所有依賴項：

```bash
pip install -r ./Installations/requirements.txt -U
```

*這將安裝 Microsoft Agent Framework 和所有必要的包。喝杯咖啡吧 —— 首次安裝可能需要幾分鐘！☕*

## 工作坊說明

詳細的項目結構、配置步驟和執行方法將在工作坊期間逐步講解。

## 故障排除（當事情出錯時）🔧

### "唉，模型下載太慢了！"
**解決方案**：使用 VPN 或配置 Ollama 鏡像源。有時候網絡就是給力不起來。

### "我的電腦快掛了！記憶體不足！"
**解決方案**：切換到更小的模型或調整 `num_ctx` 設置以使用更少記憶體。把它想象成給你的 AI 節食。

### "我能用 GPU 讓它更快嗎？"
**解決方案**：Ollama 會自動檢測 GPU！只需確保你的 GPU 驅動是最新的。免費的速度提升！🏎️

## 額外資源（給好奇的你）📚

- [Ollama 文檔](https://github.com/ollama/ollama) —— 深入了解本地 AI 模型
- [Microsoft Agent Framework](https://microsoft.github.io/autogen/) —— 了解更多關於構建智能體團隊
- [Qwen 模型信息](https://qwenlm.github.io/) —— 認識你的 AI 助手的大腦

## 許可證

MIT 許可證 —— 構建酷東西，分享它，讓世界更美好！🌍

## 想要貢獻？

發現了 bug？有想法？提交 Issue 或 PR！我們喜歡社群氛圍。✨

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我哋致力確保準確性，但請注意，自動翻譯可能存在錯誤或不準確之處。原文文件以其母語版本為權威資料來源。對於重要資訊，建議採用專業人工翻譯。本公司對因使用此翻譯而引起之任何誤解或曲解概不負責。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
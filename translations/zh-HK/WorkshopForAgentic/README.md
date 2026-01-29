# 🎙️ AI 播客工作室工作坊

> 🌏 [中文版 (Chinese Version)](translation/zh-cn/README.md)

![logo](../../../translated_images/zh-HK/logo.8711e39dc8257d7b.webp)

## 你的任務

歡迎來到 **AI 播客工作室**！你即將推出名為「Future Bytes」的科技播客 — 但有個轉折點：你將打造一支由 AI 助理組成的製作團隊協助你完成。告別無止境的資料搜集、撰稿和音訊編輯，你將以程式碼讓自己成為擁有 AI 超能力的播客製作人。

## 故事背景

想像一下：你和朋友想開一個聊最酷科技趨勢的播客，但大家都忙著讀書、工作或生活。假如你能打造一支由 AI 代理人組成的團隊幫你做繁重工作呢？一個代理人負責主題研究，另一個撰寫引人入勝的腳本，第三個則將文字轉成自然的對話。聽起來像科幻小說？讓我們把它變成現實。

## 你將學到什麼

在工作坊結束時，你會知道如何：
- 🤖 部署自己的本地 AI 模型（不需 API 費用，也不依賴雲端！）
- 🔧 建造彼此能合作的專業 AI 代理人
- 🎬 從點子到音檔，全方位建立播客製作流程

## 你的旅程：三幕劇

![arch](../../../translated_images/zh-HK/arch.5965fe504e4a3a93.webp)

像任何好故事，我們有三幕劇。每一幕都逐步建構你的 AI 播客工作室：

| 集數 | 你的任務 | 發生什麼事 | 解鎖的技能 |
|---------|-----------|--------------|----------------|
| **第一幕** | [認識你的 AI 助理](md/01.BuildAIAgentWithSLM.md) | 你將學會如何建立能聊天、網絡搜尋、甚至解決問題的 AI 代理人。把他們當成永遠不會睡覺的研究助理。 | 🎯 建立你的第一個代理人<br>🛠️ 賦予超能力（工具！）<br>🧠 教它思考<br>🌐 連上網路 |
| **第二幕** | [組建你的製作團隊](md/02.AIAgentOrchestrationAndWorkflows.md) | 有趣的開始了！你將協調多個 AI 代理人協作，宛如真正的播客團隊工作。一個研究，一個撰稿，你把關 — 團隊合作成就夢想。 | 🎭 協調多個代理人<br>🔄 建立審核流程<br>🖥️ 使用 DevUI 介面測試<br>✋ 保持人類掌控 |
| **第三幕** | [讓你的播客活起來](md/03.Multi-SpeakerPodcastGenerationWithVibeVoice.md) | 終章！將文字稿轉變為真實播客音訊，搭配逼真的聲音與自然對話。「Future Bytes」播客準備好發布囉！ | 🎤 文字轉語音魔法<br>👥 多聲道講者<br>⏱️ 長時音訊<br>🚀 全自動化 |

每幕劇解鎖新能力。敢挑戰就跳過，但我們建議跟著故事走！

## 環境需求

此工作坊支持多種硬件環境：
- **CPU**：適合測試與小規模使用
- **GPU**：建議生產環境使用，大幅提升推理速度
- **NPU**：支援新世代神經處理器加速

## 你需要準備

### 軟件清單 ✅
- **Python 3.10+**（你的程式語言）
- **Ollama**（在本機運行 AI 模型）
- **VS Code**（你的程式編輯器）
- **Python 擴充套件**（讓 VS Code 更智能）
- **Git**（下載程式碼）

### 硬件條件 💻
- **能跑嗎？**: 8GB 記憶體，10GB 可用空間（可行，但可能慢）
- **理想配置**: 16GB+ 記憶體，優良 GPU（順暢無阻！）
- **有 NPU 嗎？**: 更棒！開啟次世代效能 🚀

## 設定你的工作室 🎬

### 步驟 1：Python 強化

確認你安裝 Python 3.10 或更新版本：

```bash
python --version
# 應該顯示 Python 3.10.x 或以上版本
```
  
沒有 Python？來 [python.org](https://python.org) 下載 — 免費！

### 步驟 2：取得 Ollama（你的 AI 模型引擎）

造訪 [ollama.ai](https://ollama.ai) 並下載適合你作業系統的 Ollama。把它想成在本機運行 AI 模型的引擎。

檢查是否準備好：

```bash
ollama --version
```
  
### 步驟 3：下載你的 AI 頭腦 🧠

現在下載 Qwen-3-8B 模型（就像雇用你的第一個 AI 助理）：

```bash
ollama pull qwen3:8b
```
  
*這可能需要幾分鐘。正好喝杯咖啡休息一下！☕*

### 步驟 4：安裝 VS Code

如果還沒裝，趕快下載 [Visual Studio Code](https://code.visualstudio.com/)。這是最棒的程式編輯器（敢挑戰的來戰 😄）。

### 步驟 5：Python 擴充套件

在 VS Code 內：  
1. 按下 `Ctrl+Shift+X` （Mac 上是 `Cmd+Shift+X`）  
2. 搜尋「Python」  
3. 安裝官方 Microsoft Python 擴充套件

### 步驟 6：一切就緒！🎉

真的準備好了。讓我們開始打造 AI 魔法！

### 步驟 7：安裝 Microsoft Agent Framework 及相關套件 📦

安裝本工作坊所需的所有依賴：

```bash
pip install -r ./Installations/requirements.txt -U
```
  
*這會安裝 Microsoft Agent Framework 和所有必要套件。第一次設置可能需花幾分鐘，喝杯咖啡吧！☕*

## 工作坊指示

詳細的專案結構、配置步驟及執行方式會在工作坊中一步步說明。

## 疑難排解（出狀況時）🔧

### 「啊，模型下載超級慢！」
**解決方法**：使用 VPN 或設定 Ollama 使用鏡像源。網路有時候真的會讓人崩潰。

### 「我的電腦快掛了！記憶體不足！」
**解決方法**：改用更小型的模型或調整 `num_ctx` 參數以降低記憶體使用。想像你在幫 AI 節食。

### 「能用 GPU 加速嗎？」
**解決方法**：Ollama 會自動偵測 GPU！確保你 GPU 驅動程式是最新版本。免費速度提升！🏎️

## 額外資源（給好奇的你）📚

- [Ollama Docs](https://github.com/ollama/ollama) — 深入了解本地 AI 模型  
- [Microsoft Agent Framework](https://microsoft.github.io/autogen/) — 學習更多代理人團隊建立技術  
- [Qwen Model Info](https://qwenlm.github.io/) — 認識你的 AI 助理大腦  

## 授權條款

MIT 授權 — 建造酷炫的東西，分享出去，讓世界更美好！🌍

## 想貢獻？

發現錯誤？有好點子？開個 Issue 或 PR！我們喜歡社群的力量。✨

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：  
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯所產生的任何誤解或誤釋承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
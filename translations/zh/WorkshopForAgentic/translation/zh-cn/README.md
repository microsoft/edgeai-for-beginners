<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "aa775a734bda4590ecbe3a94a3b62197",
  "translation_date": "2026-01-05T17:26:43+00:00",
  "source_file": "WorkshopForAgentic/translation/zh-cn/README.md",
  "language_code": "zh"
}
-->
# 🎙️ AI 播客工作室工作坊

![logo](../../../../../translated_images/zh/logo.8711e39dc8257d7b.png)

## 你的任务

欢迎来到 **AI 播客工作室**！你即将推出自己的科技播客「未来字节」——但这里有个转折：你将构建一个 AI 驱动的制作团队来帮助你创建它。不再需要无休止的研究、脚本编写和音频编辑。相反，你将通过编程成为拥有 AI 超能力的播客制作人。

## 故事背景

想象一下:你和朋友想开始一个关于最酷科技趋势的播客,但每个人都忙于学习、工作或生活。如果你能构建一个 AI 智能体团队来完成繁重的工作会怎样?一个智能体负责研究主题,另一个编写引人入胜的脚本,第三个将文本转换为自然流畅的对话。听起来像科幻小说?让我们把它变成现实。

## 你将学到什么

在本工作坊结束时,你将知道如何:
- 🤖 部署你自己的本地 AI 模型(无 API 费用,无云依赖!)
- 🔧 构建实际协同工作的专业 AI 智能体
- 🎬 创建从创意到音频的完整播客制作流程

## 你的旅程：三幕剧

就像任何好故事一样，我们有三幕。每一幕都会逐步构建你的 AI 播客工作室：

| 章节 | 你的任务 | 发生什么 | 解锁技能 |
|---------|-----------|--------------|----------------|
| **第一幕** | [认识你的 AI 助手](01.BuildAIAgentWithSLM.md) | 你将发现如何创建能够聊天、搜索网络、甚至解决问题的 AI 智能体。把它们想象成永不睡觉的研究实习生。 | 🎯 构建你的第一个智能体<br>🛠️ 赋予它超能力(工具!)<br>🧠 教它思考<br>🌐 连接到互联网 |
| **第二幕** | [组建你的制作团队](02.AIAgentOrchestrationAndWorkflows.md) | 现在事情变得有趣了!你将编排多个 AI 智能体像真正的播客团队一样协同工作。一个研究,一个写作,你审批——团队合作成就梦想。 | 🎭 协调多个智能体<br>🔄 构建审批工作流<br>🖥️ 使用 DevUI 界面测试<br>✋ 保持人类控制 |
| **第三幕** | [让你的播客活起来](03.Multi-SpeakerPodcastGenerationWithVibeVoice.md) | 大结局！将你的文本脚本转换成具有逼真声音和自然对话的真实播客音频。你的「未来字节」播客准备发布了！ | 🎤 文本转语音魔法<br>👥 多说话人声音<br>⏱️ 长格式音频<br>🚀 完全自动化 |

每一幕都会解锁新能力。如果你够勇敢可以跳着看，但我们建议按顺序学习！

## 环境要求

本工作坊支持各种硬件环境：
- **CPU**：适合测试和小规模使用
- **GPU**：推荐用于生产环境，显著提升推理速度
- **NPU**：支持下一代神经处理单元加速

## 你需要什么

### 软件清单 ✅
- **Python 3.10+**（你的编程语言）
- **Ollama**（在你的机器上运行 AI 模型）
- **VS Code**（你的代码编辑器）
- **Python 扩展**（让 VS Code 更智能）
- **Git**（用于获取代码）

### 硬件检查 💻
- **我能运行吗？**：8GB 内存，10GB 可用空间（能用，但可能有点慢）
- **理想配置**：16GB+ 内存，一块不错的 GPU（顺畅运行！）
- **有 NPU 吗？**：那就更好了！解锁下一代性能 🚀

## 搭建你的工作室 🎬

### 步骤 1：Python 升级

确保你有 Python 3.10 或更新版本：

```bash
python --version
# Should display Python 3.10.x or higher version
```

没有 Python？从 [python.org](https://python.org) 获取——它是免费的！

### 步骤 2：获取 Ollama（你的 AI 模型运行器）

前往 [ollama.ai](https://ollama.ai) 下载适合你操作系统的 Ollama。把它想象成在本地运行 AI 模型的引擎。

检查是否准备就绪：

```bash
ollama --version
```

### 步骤 3：下载你的 AI 大脑 🧠

是时候获取 Qwen-3-8B 模型了（就像雇佣你的第一个 AI 助手）：

```bash
ollama pull qwen3:8b
```

*这可能需要几分钟。完美的咖啡时间！☕*

### 步骤 4：设置 VS Code

如果你还没有，获取 [Visual Studio Code](https://code.visualstudio.com/)。这是最好的代码编辑器（不服来辩 😄）。

### 步骤 5：Python 扩展

在 VS Code 中：
1. 按 `Ctrl+Shift+X`（Mac 上是 `Cmd+Shift+X`）
2. 搜索 "Python"
3. 安装官方的 Microsoft Python 扩展

### 步骤 6：大功告成！🎉

说真的，你准备好了。让我们构建一些 AI 魔法吧！

### 步骤 7：安装 Microsoft Agent Framework 和相关包 📦

安装工作坊所需的所有依赖项：

```bash
pip install -r ./Installations/requirements.txt -U
```

*这将安装 Microsoft Agent Framework 和所有必要的包。喝杯咖啡吧 —— 首次安装可能需要几分钟！☕*

## 工作坊说明

详细的项目结构、配置步骤和执行方法将在工作坊期间逐步讲解。

## 故障排除（当事情出错时）🔧

### "唉，模型下载太慢了！"
**解决方案**：使用 VPN 或配置 Ollama 镜像源。有时候网络就是不给力。

### "我的电脑快挂了！内存不足！"
**解决方案**：切换到更小的模型或调整 `num_ctx` 设置以使用更少内存。把它想象成给你的 AI 节食。

### "我能用 GPU 让它更快吗？"
**解决方案**：Ollama 会自动检测 GPU！只需确保你的 GPU 驱动是最新的。免费的速度提升！🏎️

## 额外资源（给好奇的你）📚

- [Ollama 文档](https://github.com/ollama/ollama) —— 深入了解本地 AI 模型
- [Microsoft Agent Framework](https://microsoft.github.io/autogen/) —— 了解更多关于构建智能体团队
- [Qwen 模型信息](https://qwenlm.github.io/) —— 认识你的 AI 助手的大脑

## 许可证

MIT 许可证 —— 构建酷东西，分享它，让世界更美好！🌍

## 想要贡献？

发现了 bug？有想法？提交 Issue 或 PR！我们喜欢社区氛围。✨

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免责声明**：  
本文件使用 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。虽然我们力求准确，但请注意自动翻译可能包含错误或不准确之处。原始文件的原文版本应被视为权威来源。对于重要信息，建议采用专业人工翻译。我们不对因使用本翻译而产生的任何误解或错误理解承担责任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
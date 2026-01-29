# 🎙️ AI Podcast Studio Workshop

![logo](../../../../../translated_images/en/logo.8711e39dc8257d7b.webp)

## Your Task

Welcome to **AI Podcast Studio**! You are about to launch your own tech podcast "Future Bytes" — but here's the twist: you will build an AI-powered production team to help you create it. No more endless research, scripting, and audio editing. Instead, you will become a podcast producer with AI superpowers through programming.

## Story Background

Imagine: you and your friends want to start a podcast about the coolest tech trends, but everyone is busy studying, working, or living life. What if you could build a team of AI agents to do the heavy lifting? One agent researches topics, another writes engaging scripts, a third converts text into natural, fluent conversations. Sounds like sci-fi? Let’s make it real.

## What You Will Learn

By the end of this workshop, you will know how to:
- 🤖 Deploy your own local AI models (no API fees, no cloud dependency!)
- 🔧 Build professional AI agents that collaborate effectively
- 🎬 Create a complete podcast production workflow from idea to audio

## Your Journey: Three Acts

Like any good story, we have three acts. Each one gradually builds your AI podcast studio:

| Chapter | Your Task | What Happens | Skills Unlocked |
|---------|-----------|--------------|----------------|
| **Act 1** | [Meet Your AI Assistant](01.BuildAIAgentWithSLM.md) | You will discover how to create AI agents that can chat, search the web, and even solve problems. Think of them as research interns who never sleep. | 🎯 Build your first agent<br>🛠️ Give it superpowers (tools!)<br>🧠 Teach it to think<br>🌐 Connect it to the internet |
| **Act 2** | [Build Your Production Team](02.AIAgentOrchestrationAndWorkflows.md) | Now things get interesting! You will orchestrate multiple AI agents to collaborate like a real podcast team. One researches, one writes, you approve — teamwork makes the dream work. | 🎭 Coordinate multiple agents<br>🔄 Build approval workflows<br>🖥️ Test with DevUI interface<br>✋ Keep human control |
| **Act 3** | [Bring Your Podcast to Life](03.Multi-SpeakerPodcastGenerationWithVibeVoice.md) | The grand finale! Convert your text scripts into real podcast audio with lifelike voices and natural conversation. Your "Future Bytes" podcast is ready to launch! | 🎤 Text-to-speech magic<br>👥 Multiple speaker voices<br>⏱️ Long-form audio<br>🚀 Fully automated |

Each act unlocks new abilities. If you’re brave, you can skip around, but we recommend learning in order!

## Environment Requirements

This workshop supports a variety of hardware environments:
- **CPU**: Suitable for testing and small-scale use
- **GPU**: Recommended for production, dramatically speeds up inference
- **NPU**: Supports next-generation neural processing unit acceleration

## What You Need

### Software Checklist ✅
- **Python 3.10+** (your programming language)
- **Ollama** (runs AI models on your machine)
- **VS Code** (your code editor)
- **Python extension** (makes VS Code smarter)
- **Git** (to get the code)

### Hardware Check 💻
- **Can I run it?**: 8GB RAM, 10GB free space (usable, but might be slow)
- **Ideal Setup**: 16GB+ RAM, a decent GPU (smooth operation!)
- **Got an NPU?**: Even better! Unlock next-gen performance 🚀

## Set Up Your Studio 🎬

### Step 1: Upgrade Python

Make sure you have Python 3.10 or later:

```bash
python --version
# It should display Python 3.10.x or a higher version
```

No Python? Get it from [python.org](https://python.org) — it’s free!

### Step 2: Get Ollama (your AI model runner)

Go to [ollama.ai](https://ollama.ai) and download Ollama for your operating system. Think of it as your local AI model engine.

Check if it’s ready:

```bash
ollama --version
```

### Step 3: Download Your AI Brain 🧠

It’s time to get the Qwen-3-8B model (like hiring your first AI assistant):

```bash
ollama pull qwen3:8b
```

*This may take a few minutes. Perfect coffee break! ☕*

### Step 4: Set Up VS Code

If you don’t have it yet, get [Visual Studio Code](https://code.visualstudio.com/). It’s the best code editor (no debate 😄).

### Step 5: Python Extension

In VS Code:  
1. Press `Ctrl+Shift+X` (or `Cmd+Shift+X` on Mac)  
2. Search for "Python"  
3. Install the official Microsoft Python extension

### Step 6: You’re Done! 🎉

Seriously, you’re ready. Let’s build some AI magic!

### Step 7: Install Microsoft Agent Framework and Related Packages 📦

Install all dependencies required for the workshop:

```bash
pip install -r ./Installations/requirements.txt -U
```

*This will install the Microsoft Agent Framework and all necessary packages. Grab a coffee — first-time install might take a few minutes! ☕*

## Workshop Instructions

Detailed project structure, setup steps, and execution methods will be explained progressively throughout the workshop.

## Troubleshooting (When Things Go Wrong) 🔧

### “Ugh, the model download is too slow!”  
**Solution**: Use a VPN or configure Ollama mirror sources. Sometimes networks just don’t cooperate.

### “My computer is dying! Not enough memory!”  
**Solution**: Switch to a smaller model or adjust `num_ctx` settings to use less memory. Think of it as putting your AI on a diet.

### “Can I use my GPU to speed things up?”  
**Solution**: Ollama auto-detects GPUs! Just make sure your GPU drivers are up to date. Free speed boost! 🏎️

## Extra Resources (For the Curious) 📚

- [Ollama Documentation](https://github.com/ollama/ollama) — Deep dive into local AI models  
- [Microsoft Agent Framework](https://microsoft.github.io/autogen/) — Learn more about building agent teams  
- [Qwen Model Info](https://qwenlm.github.io/) — Get to know your AI assistant’s brain

## License

MIT License — Build cool stuff, share it, and make the world better! 🌍

## Want to Contribute?

Found a bug? Got ideas? Submit an Issue or PR! We love a vibrant community. ✨

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we strive for accuracy, please be aware that automated translations may contain errors or inaccuracies. The original document in its native language should be considered the authoritative source. For critical information, professional human translation is recommended. We are not liable for any misunderstandings or misinterpretations arising from the use of this translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
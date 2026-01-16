<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "aa775a734bda4590ecbe3a94a3b62197",
  "translation_date": "2026-01-05T18:06:16+00:00",
  "source_file": "WorkshopForAgentic/translation/zh-cn/README.md",
  "language_code": "pcm"
}
-->
# 🎙️ AI Pọdkast Wọkshọp

![logo](../../../../../translated_images/pcm/logo.8711e39dc8257d7b.webp)

## Your Task

Welcome to **AI Pọdkast Wọkshọp**! You dey go launch your own tech pọọdkast wey dem dey call "Future Bytes" — but one turn dey: you go build one AI-powered pọọdkast team to help you make am. No more plenty ntutu research, script writing and audio editing. Instead, you go use programming become pọọdkast producer wey get AI superpower.

## Story Background

Make you imagine: you and your friends wan start pọọdkast about the coolest techno trends, but everybody busy with school, work or life. If you fit build AI agent team to carry all that work, how e go be? One agent go do research, another one go write fine script, third one go change text to natural sounding conversation. E dey sound like sci-fi? Make we turn am for real.

## Wetin You Go Learn

By the time this workshop finish, you go sabi how to:
- 🤖 Deploy your own local AI models (no API fee, no cloud dependency!)
- 🔧 Build professional AI agents wey fit collaborate well well
- 🎬 Create full pọọdkast production process from idea reach audio

## Your Journey: Three Acts

Like beta story, we get three acts. Each act go build your AI pọọdkast studio step by step:

| Chapter | Your Task | Wetin Go Happen | Skills Unlock |
|---------|-----------|-----------------|---------------|
| **Act One** | [Meet Your AI Assistant](01.BuildAIAgentWithSLM.md) | You go learn how to create AI agents wey fit chat, search web, even solve problem. Think of dem as tireless research interns. | 🎯 Build your first agent<br>🛠️ Give am superpowers (tools!)<br>🧠 Teach am to think<br>🌐 Connect am to internet |
| **Act Two** | [Build Your Production Team](02.AIAgentOrchestrationAndWorkflows.md) | Things go sweet wella! You go coordinate many AI agents to work like real pọọdkast team. One go research, one go write, you go approve — teamwork dey make dream real. | 🎭 Coordinate multiple agents<br>🔄 Build approval workflows<br>🖥️ Test inside DevUI interface<br>✋ Keep human control |
| **Act Three** | [Bring Your Pọdkast To Life](03.Multi-SpeakerPodcastGenerationWithVibeVoice.md) | Grand finale! You go turn text script to real pọọdkast audio with natural voice and real talk. Your "Future Bytes" pọọdkast ready to publish! | 🎤 Text to speech magic<br>👥 Multi-speaker voices<br>⏱️ Long format audio<br>🚀 Fully automated |

Each act go unlock new skill. If you bold, you fit skip, but we recommend make you follow order learn!

## Environment Requirements

This workshop support plenty hardware:
- **CPU**: Suitable for small test and light usage
- **GPU**: Recommended for production, significant speed boost for inference
- **NPU**: Support next-gen Neural Processing Unit acceleration

## Wetin You Need

### Software List ✅
- **Python 3.10+** (your programming language)
- **Ollama** (run AI models on your device)
- **VS Code** (your code editor)
- **Python Extension** (make VS Code smarter)
- **Git** (for download code)

### Hardware Check 💻
- **Fit run am?**: 8GB RAM, 10GB free space (e fit run but e fit slow)
- **Ideal Setup**: 16GB+ RAM, correct GPU (smooth running!)
- **Get NPU?**: Better! Unlock next-gen power 🚀

## Build Your Studio 🎬

### Step 1: Update Python

Make sure say you get Python 3.10 or later:

```bash
python --version
# E suppose show Python 3.10.x or beta version pass am
```

No get Python? Collect am from [python.org](https://python.org) — e dey free!

### Step 2: Get Ollama (your AI model runner)

Go [ollama.ai](https://ollama.ai) download Ollama wey fit your OS. Think am like AI model engine wey dey run locally.

Check if e ready:

```bash
ollama --version
```

### Step 3: Download Your AI Brain 🧠

Time don reach to get Qwen-3-8B model (like you dey hire your first AI assistant):

```bash
ollama pull qwen3:8b
```

*E fit take small time. Perfect coffee break! ☕*

### Step 4: Setup VS Code

If you never get am, download [Visual Studio Code](https://code.visualstudio.com/). Na best code editor (no argue 😄).

### Step 5: Python Extension

Inside VS Code:
1. Press `Ctrl+Shift+X` (Mac na `Cmd+Shift+X`)
2. Search "Python"
3. Install official Microsoft Python extension

### Step 6: All set! 🎉

No joke, you don ready. Make we start build some AI magic!

### Step 7: Install Microsoft Agent Framework and packages 📦

Install all dependencies for workshop:

```bash
pip install -r ./Installations/requirements.txt -U
```

*This one go install Microsoft Agent Framework plus all packages wey dey required. Sip coffee — first time fit take small time! ☕*

## Workshop Instructions

Project structure, configuration steps and how to run go dey explained well well during workshop.

## Troubleshooting (If Wahala Happen) 🔧

### "Ah, model dey download slow o!"
**Solution**: Use VPN or configure Ollama mirror source. Sometimes network no too good.

### "My PC nearly hang! Not enough RAM!"
**Solution**: Switch to smaller model or adjust `num_ctx` to use less memory. Think am like make your AI dey diet.

### "Fit use GPU to make am faster?"
**Solution**: Ollama go detect GPU automatically! Just make sure your GPU driver dey updated. Free speed boost! 🏎️

## Extra Resources (For the Curious) 📚

- [Ollama Docs](https://github.com/ollama/ollama) — Deep dive into local AI models
- [Microsoft Agent Framework](https://microsoft.github.io/autogen/) — Learn more about building agent team
- [Qwen Model Info](https://qwenlm.github.io/) — Know your AI assistant brain

## License

MIT License — Build cool tins, share am, make world better! 🌍

## Want Contribute?

Find bug? Get idea? Submit Issue or PR! We like community spirit. ✨

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis dokument don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg sabi say automated translations fit get some mistakes or no too correct. Di original dokument wey dey dia for dia own language na di real correct one. For important mata, better make human professional translate am. We no go responsible if you no understand well or you use am wrong because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
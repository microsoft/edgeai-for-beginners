# EdgeAI for Beginners 


![Course cover image](../../translated_images/pcm/cover.eb18d1b9605d754b.webp)

[![GitHub contributors](https://img.shields.io/github/contributors/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/graphs/contributors)
[![GitHub issues](https://img.shields.io/github/issues/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/issues)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/pulls)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

[![GitHub watchers](https://img.shields.io/github/watchers/microsoft/edgeai-for-beginners.svg?style=social&label=Watch)](https://GitHub.com/microsoft/edgeai-for-beginners/watchers)
[![GitHub forks](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork)
[![GitHub stars](https://img.shields.io/github/stars/microsoft/edgeai-for-beginners?style=social&label=Star)](https://GitHub.com/microsoft/edgeai-for-beginners/stargazers)


[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Follow dis steps to start to use dis resources:

1. **Fork the Repository**: Click [![GitHub forks](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork)
2. **Clone the Repository**:   `git clone https://github.com/microsoft/edgeai-for-beginners.git`
3. [**Join The Azure AI Foundry Discord and meet experts and fellow developers**](https://discord.com/invite/ByRwuEEgH4)


### 🌐 Multi-Language Support

#### Supported via GitHub Action (Automated & Always Up-to-Date)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh-CN/README.md) | [Chinese (Traditional, Hong Kong)](../zh-HK/README.md) | [Chinese (Traditional, Macau)](../zh-MO/README.md) | [Chinese (Traditional, Taiwan)](../zh-TW/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](./README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../pt-BR/README.md) | [Portuguese (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

> **Prefer to Clone Locally?**

> Dis repository get 50+ language translations wey dey add the size of wetin you go download. To clone without translations, use sparse checkout:
> ```bash
> git clone --filter=blob:none --sparse https://github.com/microsoft/edgeai-for-beginners.git
> cd edgeai-for-beginners
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
> Dis go give you everytin wey you need to complete the course sharp sharp.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

**If you want make we add more translations, di languages wey fit still join dey listed [here](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md)**
## Introduction

Welcome to **EdgeAI for Beginners** – your complete journey into di changing world of Edge Artificial Intelligence. Dis course go join di powerful AI skills with how to use am for real-life edge devices, make you fit use AI power for place wey data dey come from and where decision suppose happen.

### Wetin You Go Master

Dis course go carry you from di basics enter full production way, e go cover:
- **Small Language Models (SLMs)** wey dem optimize for edge deployment
- **Hardware-aware optimization** for different platforms
- **Real-time inference** wey dey protect privacy
- **Production deployment** ways for big company use

### Why EdgeAI Matter

Edge AI na new way wey fit solve big problems for now:
- **Privacy & Security**: Make you fit handle important data for your side without put am for cloud
- **Real-time Performance**: No delay from internet for apps weh need quick work
- **Cost Efficiency**: Save money on internet use and cloud computer work
- **Resilient Operations**: Make things still dey work when internet go down
- **Regulatory Compliance**: Follow law about where data suppose stay

### Edge AI

Edge AI mean say AI algorithms and language models go run for hardware close to where data dey come from, without need cloud to help run dem. E reduce delay, make privacy better, and allow quick decision making.

### Core Principles:
- **On-device inference**: AI models go run for edge devices (phone, routers, microcontrollers, industrial PCs)
- **Offline capability**: E fit work without internet connection all di time
- **Low latency**: E respond quick for real-time system
- **Data sovereignty**: Keep sensitive data local, make security and law obeying beta

### Small Language Models (SLMs)

SLMs like Phi-4, Mistral-7B, and Gemma na small versions of big LLMs—dem train or distill for:
- **Reduced memory footprint**: Use small space on edge device memory well
- **Lower compute demand**: Make e work fine for CPU and edge GPU
- **Faster startup times**: Quick start so app go respond fast

Dem fit give strong NLP powers plus meet requirement for:
- **Embedded systems**: IoT devices and industrial control
- **Mobile devices**: Smartphones and tablets wey fit work offline
- **IoT Devices**: Sensors and clever devices wey no get plenty resource
- **Edge servers**: Local computers wey no get big GPU power
- **Personal Computers**: Desktop and laptop way to deploy

## Course Modules & Navigation

| Module | Topic | Focus Area | Key Content | Level | Duration |
|--------|-------|------------|-------------|--------|----------|
| [📖 00 ](./introduction.md) | [Introduction to EdgeAI](./introduction.md) | Foundation & Context | EdgeAI Overview • Industry Applications • SLM Introduction • Learning Objectives | Beginner | 1-2 hrs |
| [📚 01](../../Module01) | [EdgeAI Fundamentals](./Module01/README.md) | Cloud vs Edge AI comparison | EdgeAI Fundamentals • Real World Case Studies • Implementation Guide • Edge Deployment | Beginner | 3-4 hrs |
| [🧠 02](../../Module02) | [SLM Model Foundations](./Module02/README.md) | Model families & architecture | Phi Family • Qwen Family • Gemma Family • BitNET • μModel • Phi-Silica | Beginner | 4-5 hrs |
| [🚀 03](../../Module03) | [SLM Deployment Practice](./Module03/README.md) | Local & cloud deployment | Advanced Learning • Local Environment • Cloud Deployment | Intermediate | 4-5 hrs |
| [⚙️ 04](../../Module04) | [Model Optimization Toolkit](./Module04/README.md) | Cross-platform optimization | Introduction • Llama.cpp • Microsoft Olive • OpenVINO • Apple MLX • Workflow Synthesis | Intermediate | 5-6 hrs |
| [🔧 05](../../Module05) | [SLMOps Production](./Module05/README.md) | Production operations | SLMOps Introduction • Model Distillation • Fine-tuning • Production Deployment | Advanced | 5-6 hrs |
| [🤖 06](../../Module06) | [AI Agents & Function Calling](./Module06/README.md) | Agent frameworks & MCP | Agent Introduction • Function Calling • Model Context Protocol | Advanced | 4-5 hrs |
| [💻 07](../../Module07) | [Platform Implementation](./Module07/README.md) | Cross-platform samples | AI Toolkit • Foundry Local • Windows Development | Advanced | 3-4 hrs |
| [🏭 08](../../Module08) | [Foundry Local Toolkit](./Module08/README.md) | Production-ready samples | Sample applications (see details below) | Expert | 8-10 hrs |

### 🏭 **Module 08: Sample Applications**

- [01: REST Chat Quickstart](./Module08/samples/01/README.md)
- [02: OpenAI SDK Integration](./Module08/samples/02/README.md)
- [03: Model Discovery & Benchmarking](./Module08/samples/03/README.md)
- [04: Chainlit RAG Application](./Module08/samples/04/README.md)
- [05: Multi-Agent Orchestration](./Module08/samples/05/README.md)
- [06: Models-as-Tools Router](./Module08/samples/06/README.md)
- [07: Direct API Client](./Module08/samples/07/README.md)
- [08: Windows 11 Chat App](./Module08/samples/08/README.md)
- [09: Advanced Multi-Agent System](./Module08/samples/09/README.md)
- [10: Foundry Tools Framework](./Module08/samples/10/README.md)

### 🎓 **Workshop: Hands-On Learning Path**

Complete hands-on workshop materials with production-ready work:

- **[Workshop Guide](./Workshop/Readme.md)** - Full learning goals, results, and resource directions
- **Python Samples** (6 sessions) - Updated with best way to do am, error handling, and full docs
- **Jupyter Notebooks** (8 interactive) - Step-by-step lessons with benchmark and performance check
- **Session Guides** - Full markdown guides for each workshop session
- **Validation Tools** - Scripts to check code quality and run simple tests

**Wetin You Go Build:**
- Local AI chat apps wey get streaming support
- RAG pipelines wey get quality check (RAGAS)
- Multi-model benchmarking and comparison tools
- Multi-agent systems wey fit work together
- Smart model routing wey choose task well

### 🎙️ **Workshop For Agentic: Hands-On - The AI Podcast Studio**

Build AI-powered podcast production pipeline from start! Dis workshop go teach you how to create full multi-agent system wey go turn ideas into pro podcast episodes.
**[🎬 Start The AI Podcast Studio Workshop](./WorkshopForAgentic/README.md)**

**Your Mission**: Launch "Future Bytes" — a tech podcast wey AI agents weh you go build by yourself dey power am. No cloud dependencies, no API costs — everything dey run local for your machine.

**Wetyn Make This Different:**
- **🤖 Real Multi-Agent Orchestration** - Build specialized AI agents wey go do research, write, and produce audio
- **🎯 Complete Production Pipeline** - From topic selection reach final podcast audio output
- **💻 100% Local Deployment** - Use Ollama and local models (Qwen-3-8B) for full privacy and control
- **🎤 Text-to-Speech Integration** - Turn scripts to natural-sounding multi-speaker conversations
- **✋ Human-in-the-Loop Workflows** - Approval gates wey dey make sure quality dey while automation still dey work

**Three-Act Learning Journey:**

| Act | Focus | Key Skills | Duration |
|-----|-------|------------|----------|
| **[Act 1: Meet Your AI Assistants](./WorkshopForAgentic/md/01.BuildAIAgentWithSLM.md)** | Build your first AI agent | Tool integration • Web search • Problem-solving • Agentic reasoning | 2-3 hrs |
| **[Act 2: Assemble Your Production Team](./WorkshopForAgentic/md/02.AIAgentOrchestrationAndWorkflows.md)** | Orchestrate multiple agents | Team coordination • Approval workflows • DevUI interface • Human oversight | 3-4 hrs |
| **[Act 3: Bring Your Podcast to Life](./WorkshopForAgentic/md/03.Multi-SpeakerPodcastGenerationWithVibeVoice.md)** | Generate podcast audio | Text-to-speech • Multi-speaker synthesis • Long-form audio • Full automation | 2-3 hrs |

**Technologies We Dey Use:**
- **Microsoft Agent Framework** - Multi-agent orchestration and coordination
- **Ollama** - Local AI model runtime (no cloud required)
- **Qwen-3-8B** - Open-source language model wey dem optimize for agentic tasks
- **Text-to-Speech APIs** - Natural voice synthesis for podcast generation

**Hardware Support:**
- ✅ **CPU Mode** - E dey work for any modern computer (8GB+ RAM recommended)
- 🚀 **GPU Acceleration** - E dey reason well well wit NVIDIA/AMD GPUs, e go quick pass
- ⚡ **NPU Support** - Next-generation neural processing unit acceleration

**Perfect For:**
- Developers wey dey learn multi-agent AI systems
- People wey get interest for AI automation and workflows
- Content creators wey dey explore AI-assisted production
- Students wey dey study practical AI orchestration patterns

**Start Building**: [🎙️ The AI Podcast Studio Workshop →](./WorkshopForAgentic/README.md)

### 📊 **Learning Path Summary**
- **Total Duration**: 36-45 hours
- **Beginner Path**: Modules 01-02 (7-9 hours)  
- **Intermediate Path**: Modules 03-04 (9-11 hours)
- **Advanced Path**: Modules 05-07 (12-15 hours)
- **Expert Path**: Module 08 (8-10 hours)

## Wetin You Go Build

### 🎯 Core Competencies
- **Edge AI Architecture**: Design local-first AI systems with cloud integration
- **Model Optimization**: Quantize and compress models for edge deployment (85% speed boost, 75% size reduction)
- **Multi-Platform Deployment**: Windows, mobile, embedded, and cloud-edge hybrid systems
- **Production Operations**: Monitoring, scaling, and maintaining edge AI for production

### 🏗️ Practical Projects
- **Foundry Local Chat Apps**: Windows 11 native app wey fit switch model
- **Multi-Agent Systems**: Coordinator with specialist agents for complex workflows  
- **RAG Applications**: Local document processing with vector search
- **Model Routers**: Intelligent selection between models based on task analysis
- **API Frameworks**: Production-ready clients with streaming and health monitoring
- **Cross-Platform Tools**: LangChain/Semantic Kernel integration patterns

### 🏢 Industry Applications
**Manufacturing** • **Healthcare** • **Autonomous Vehicles** • **Smart Cities** • **Mobile Apps**

## Quick Start

**Recommended Learning Path** (20-30 hours total):

0. **📖 Introduction** ([Introduction.md](./introduction.md)): EdgeAI foundation + industry context + learning framework
1. **📚 Foundation** (Modules 01-02): EdgeAI concepts + SLM model families
2. **⚙️ Optimization** (Modules 03-04): Deployment + quantization frameworks  
3. **🚀 Production** (Modules 05-06): SLMOps + AI agents + function calling
4. **💻 Implementation** (Modules 07-08): Platform samples + Foundry Local toolkit

Every module get theory, hands-on exercises, and production-ready code samples.

## Career Impact

**Technical Roles**: EdgeAI Solutions Architect • ML Engineer (Edge) • IoT AI Developer • Mobile AI Developer

**Industry Sectors**: Manufacturing 4.0 • Healthcare Tech • Autonomous Systems • FinTech • Consumer Electronics

**Portfolio Projects**: Multi-agent systems • Production RAG apps • Cross-platform deployment • Performance optimization

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

## Course Highlights

✅ **Progressive Learning**: Theory → Practice → Production deployment  
✅ **Real Case Studies**: Microsoft, Japan Airlines, enterprise implementations  
✅ **Hands-on Samples**: 50+ examples, 10 comprehensive Foundry Local demos  
✅ **Performance Focus**: 85% speed improvements, 75% size reductions  
✅ **Multi-Platform**: Windows, mobile, embedded, cloud-edge hybrid  
✅ **Production Ready**: Monitoring, scaling, security, compliance frameworks

📖 **[Study Guide Available](STUDY_GUIDE.md)**: Structured 20-hour learning path with time allocation guidance and self-assessment tools.

---

**EdgeAI na di future of AI deployment**: local-first, privacy-preserving, and efficient. Master dis skills to build di next generation of intelligent applications.

## Other Courses

Our team dey produce other courses! Check am out:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j for Beginners](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js for Beginners](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)

---

### Azure / Edge / MCP / Agents
[![AZD for Beginners](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Edge AI for Beginners](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP for Beginners](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![AI Agents for Beginners](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Generative AI Series
[![Generative AI for Beginners](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Generative AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![Generative AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![Generative AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### Core Learning
[![ML for Beginners](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![Data Science for Beginners](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![AI for Beginners](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![Cybersecurity for Beginners](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![Web Dev for Beginners](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![IoT for Beginners](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![XR Development for Beginners](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Copilot Series
[![Copilot for AI Paired Programming](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot for C#/.NET](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot Adventure](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## How to Get Help

If you jam or get any question about how to build AI apps, join:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

If you get product feedback or error wen you dey build, check:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis dokumment don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even though we dey try make am correct, abeg sabi say automated translation fit get some errors or dem no too correct. Di original dokumment wey dem write for di og language na di main one wey get authority. For important mata dem, make person wey sabi do proper human translation help you. We no go responsible for any wahala or wrong understanding wey fit happen because you use dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1e49c901b8a8e953904d655ae4630bfe",
  "translation_date": "2025-11-18T18:21:03+00:00",
  "source_file": "README.md",
  "language_code": "pcm"
}
-->
# EdgeAI for Beginners 


![Course cover image](../../translated_images/cover.eb18d1b9605d754b30973f4e17c6e11ea4f8473d9686ee378d6e7b44e3c70ac7.pcm.png)

[![GitHub contributors](https://img.shields.io/github/contributors/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/graphs/contributors)
[![GitHub issues](https://img.shields.io/github/issues/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/issues)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/pulls)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

[![GitHub watchers](https://img.shields.io/github/watchers/microsoft/edgeai-for-beginners.svg?style=social&label=Watch)](https://GitHub.com/microsoft/edgeai-for-beginners/watchers)
[![GitHub forks](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork)
[![GitHub stars](https://img.shields.io/github/stars/microsoft/edgeai-for-beginners?style=social&label=Star)](https://GitHub.com/microsoft/edgeai-for-beginners/stargazers)


[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Follow dis steps to start wit dis resources:

1. **Fork di Repository**: Click [![GitHub forks](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork)
2. **Clone di Repository**:   `git clone https://github.com/microsoft/edgeai-for-beginners.git`
3. [**Join di Azure AI Foundry Discord make you meet experts and oda developers**](https://discord.com/invite/ByRwuEEgH4)


### 🌐 Multi-Language Support

#### Supported wit GitHub Action (Automated & Always Up-to-Date)

[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh/README.md) | [Chinese (Traditional, Hong Kong)](../hk/README.md) | [Chinese (Traditional, Macau)](../mo/README.md) | [Chinese (Traditional, Taiwan)](../tw/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](./README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../br/README.md) | [Portuguese (Portugal)](../pt/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

**If you wan make dem add more translations, di languages wey dem support dey listed [here](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md)**
## Introduction

Welcome to **EdgeAI for Beginners** – dis na your full journey into di world of Edge Artificial Intelligence. Dis course go show you how AI fit work well for real-life use on edge devices, so you fit use AI power where data dey generated and decisions dey needed.

### Wetin You Go Learn

Dis course go carry you from di basics go reach di level wey you fit deploy AI for production, e go cover:
- **Small Language Models (SLMs)** wey dem optimize for edge deployment
- **Hardware-aware optimization** for different platforms
- **Real-time inference** wey dey protect privacy
- **Production deployment** strategies for enterprise applications

### Why EdgeAI Important

Edge AI dey change di way we dey solve big problems for today world:
- **Privacy & Security**: Process sensitive data for di device, no need cloud
- **Real-time Performance**: No network delay for applications wey need quick response
- **Cost Efficiency**: Reduce bandwidth and cloud computing cost
- **Resilient Operations**: E go still work even if network no dey
- **Regulatory Compliance**: E go meet di rules for data protection

### Edge AI

Edge AI na wen AI dey run for di device wey dey close to where data dey generated, e no dey depend on cloud resources for inference. E dey reduce delay, improve privacy, and e dey allow real-time decision-making.

### Core Principles:
- **On-device inference**: AI models dey run for edge devices like phones, routers, microcontrollers, industrial PCs
- **Offline capability**: E dey work even if internet no dey
- **Low latency**: Quick response wey fit work for real-time systems
- **Data sovereignty**: E keep sensitive data local, e dey improve security and compliance

### Small Language Models (SLMs)

SLMs like Phi-4, Mistral-7B, and Gemma na smaller versions of big LLMs—dem train or distill dem for:
- **Reduced memory footprint**: E dey use small memory for edge devices
- **Lower compute demand**: E dey work well for CPU and edge GPU
- **Faster startup times**: E dey start quick for applications wey need fast response

Dem dey give strong NLP power and dem fit work for:
- **Embedded systems**: IoT devices and industrial controllers
- **Mobile devices**: Smartphones and tablets wey fit work offline
- **IoT Devices**: Sensors and smart devices wey no get plenty resources
- **Edge servers**: Local processing units wey no get plenty GPU resources
- **Personal Computers**: Desktop and laptop deployment scenarios

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

Full hands-on workshop materials wit production-ready implementations:

- **[Workshop Guide](./Workshop/Readme.md)** - Full learning objectives, outcomes, and resource navigation
- **Python Samples** (6 sessions) - Updated wit best practices, error handling, and full documentation
- **Jupyter Notebooks** (8 interactive) - Step-by-step tutorials wit benchmarks and performance monitoring
- **Session Guides** - Detailed markdown guides for each workshop session
- **Validation Tools** - Scripts to check code quality and run smoke tests

**Wetin You Go Build:**
- Local AI chat applications wit streaming support
- RAG pipelines wit quality evaluation (RAGAS)
- Multi-model benchmarking and comparison tools
- Multi-agent orchestration systems
- Intelligent model routing wit task-based selection

### 📊 **Learning Path Summary**
- **Total Duration**: 36-45 hours
- **Beginner Path**: Modules 01-02 (7-9 hours)  
- **Intermediate Path**: Modules 03-04 (9-11 hours)
- **Advanced Path**: Modules 05-07 (12-15 hours)
- **Expert Path**: Module 08 (8-10 hours)

## Wetin You Go Build

### 🎯 Core Competencies
- **Edge AI Architecture**: Design local-first AI systems wit cloud integration
- **Model Optimization**: Quantize and compress models for edge deployment (85% speed boost, 75% size reduction)
- **Multi-Platform Deployment**: Windows, mobile, embedded, and cloud-edge hybrid systems
- **Production Operations**: Dey monitor, scale, and maintain edge AI wey dey for production

### 🏗️ Practical Projects
- **Foundry Local Chat Apps**: Windows 11 app wey fit switch model
- **Multi-Agent Systems**: Coordinator wey dey use specialist agents for complex workflows  
- **RAG Applications**: Local document processing wey get vector search
- **Model Routers**: Smart way to choose model based on task analysis
- **API Frameworks**: Clients wey ready for production, streaming, and health monitoring
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

Each module get theory, hands-on exercises, and production-ready code samples.

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

✅ **Progressive Learning**: From theory → practice → production deployment  
✅ **Real Case Studies**: Microsoft, Japan Airlines, enterprise implementations  
✅ **Hands-on Samples**: Over 50 examples, 10 full Foundry Local demos  
✅ **Performance Focus**: 85% speed improvement, 75% size reduction  
✅ **Multi-Platform**: Windows, mobile, embedded, cloud-edge hybrid  
✅ **Production Ready**: Monitoring, scaling, security, compliance frameworks

📖 **[Study Guide Available](STUDY_GUIDE.md)**: Structured 20-hour learning path with time allocation guidance and self-assessment tools.

---

**EdgeAI na the future of AI deployment**: local-first, privacy-preserving, and efficient. Learn these skills to fit build the next generation of smart apps.

## Other Courses

Our team dey produce other courses! Check dem out:

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

## Getting Help

If you dey stuck or you get any question about how to build AI apps, join:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

If you get product feedback or you see error while you dey build, visit:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis dokyument don use AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator) take translate am. Even though we dey try make sure say e correct, abeg sabi say automatic translation fit get mistake or no dey accurate well. Di original dokyument for im native language na di main correct source. For important information, e go beta make professional human translator check am. We no go fit take blame for any misunderstanding or wrong interpretation wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
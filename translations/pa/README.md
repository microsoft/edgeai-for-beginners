# EdgeAI for Beginners 


![Course cover image](../../translated_images/pa/cover.eb18d1b9605d754b.webp)

[![GitHub contributors](https://img.shields.io/github/contributors/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/graphs/contributors)
[![GitHub issues](https://img.shields.io/github/issues/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/issues)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/pulls)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

[![GitHub watchers](https://img.shields.io/github/watchers/microsoft/edgeai-for-beginners.svg?style=social&label=Watch)](https://GitHub.com/microsoft/edgeai-for-beginners/watchers)
[![GitHub forks](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork)
[![GitHub stars](https://img.shields.io/github/stars/microsoft/edgeai-for-beginners?style=social&label=Star)](https://GitHub.com/microsoft/edgeai-for-beginners/stargazers)


[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Follow these steps to get started using these resources:

1. **Fork the Repository**: Click [![GitHub forks](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork)
2. **Clone the Repository**:   `git clone https://github.com/microsoft/edgeai-for-beginners.git`
3. [**Join The Azure AI Foundry Discord and meet experts and fellow developers**](https://discord.com/invite/ByRwuEEgH4)


### 🌐 Multi-Language Support

#### Supported via GitHub Action (Automated & Always Up-to-Date)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh-CN/README.md) | [Chinese (Traditional, Hong Kong)](../zh-HK/README.md) | [Chinese (Traditional, Macau)](../zh-MO/README.md) | [Chinese (Traditional, Taiwan)](../zh-TW/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../pt-BR/README.md) | [Portuguese (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](./README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

> **Prefer to Clone Locally?**

> This repository includes 50+ language translations which significantly increases the download size. To clone without translations, use sparse checkout:
> ```bash
> git clone --filter=blob:none --sparse https://github.com/microsoft/edgeai-for-beginners.git
> cd edgeai-for-beginners
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
> This gives you everything you need to complete the course with a much faster download.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

**If you wish to have additional translations languages supported are listed [here](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md)**
## Introduction

Welcome to **EdgeAI for Beginners** – your comprehensive journey into the transformative world of Edge Artificial Intelligence. This course bridges the gap between powerful AI capabilities and practical, real-world deployment on edge devices, empowering you to harness AI's potential directly where data is generated and decisions need to be made.

### What You'll Master

This course takes you from fundamental concepts to production-ready implementations, covering:
- **Small Language Models (SLMs)** optimized for edge deployment
- **Hardware-aware optimization** across diverse platforms
- **Real-time inference** with privacy-preserving capabilities
- **Production deployment** strategies for enterprise applications

### Why EdgeAI Matters

Edge AI represents a paradigm shift that addresses critical modern challenges:
- **Privacy & Security**: Process sensitive data locally without cloud exposure
- **Real-time Performance**: Eliminate network latency for time-critical applications
- **Cost Efficiency**: Reduce bandwidth and cloud computing expenses
- **Resilient Operations**: Maintain functionality during network outages
- **Regulatory Compliance**: Meet data sovereignty requirements

### Edge AI

Edge AI refers to running AI algorithms and language models locally on hardware, close to where data is generated without relying on cloud resources for inference. It reduces latency, enhances privacy, and enables real-time decision-making.

### Core Principles:
- **On-device inference**: AI models run on edge devices (phones, routers, microcontrollers, industrial PCs)
- **Offline capability**: Functions without persistent internet connectivity
- **Low latency**: Immediate responses suited for real-time systems
- **Data sovereignty**: Keeps sensitive data local, improving security and compliance

### Small Language Models (SLMs)

SLMs like Phi-4, Mistral-7B, and Gemma are optimized versions of larger LLMs—trained or distilled for:
- **Reduced memory footprint**: Efficient use of limited edge device memory
- **Lower compute demand**: Optimized for CPU and edge GPU performance
- **Faster startup times**: Quick initialization for responsive applications

They unlock powerful NLP capabilities while meeting the constraints of:
- **Embedded systems**: IoT devices and industrial controllers
- **Mobile devices**: Smartphones and tablets with offline capabilities
- **IoT Devices**: Sensors and smart devices with limited resources
- **Edge servers**: Local processing units with limited GPU resources
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

Comprehensive hands-on workshop materials with production-ready implementations:

- **[Workshop Guide](./Workshop/Readme.md)** - Complete learning objectives, outcomes, and resource navigation
- **Python Samples** (6 sessions) - Updated with best practices, error handling, and comprehensive documentation
- **Jupyter Notebooks** (8 interactive) - Step-by-step tutorials with benchmarks and performance monitoring
- **Session Guides** - Detailed markdown guides for each workshop session
- **Validation Tools** - Scripts to verify code quality and run smoke tests

**What You'll Build:**
- Local AI chat applications with streaming support
- RAG pipelines with quality evaluation (RAGAS)
- Multi-model benchmarking and comparison tools
- Multi-agent orchestration systems
- Intelligent model routing with task-based selection

### 🎙️ **Workshop For Agentic: Hands-On - The AI Podcast Studio**

Build an AI-powered podcast production pipeline from scratch! This immersive workshop teaches you to create a complete multi-agent system that transforms ideas into professional podcast episodes.
**[🎬 AI ਪੋਡਕਾਸਟ ਸਟੂਡੀਓ ਵਰਕਸ਼ਾਪ ਸ਼ੁਰੂ ਕਰੋ](./WorkshopForAgentic/README.md)**

**ਤੁਹਾਡਾ ਮਿਸ਼ਨ**: "Future Bytes" ਲਾਂਚ ਕਰੋ — ਇੱਕ ਤਕਨਾਲੋਜੀ ਪੋਡਕਾਸਟ ਜੋ ਪੂਰੀ ਤਰ੍ਹਾਂ ਤੁਹਾਡੇ ਦੁਆਰਾ ਬਣਾਏ ਗਏ AI ਏਜੰਟਾਂ ਨਾਲ ਚਲਾਇਆ ਜਾਏਗਾ। ਕੋਈ ਕਲਾਉਡ ਨਿਰਭਰਤਾ ਨਹੀਂ, ਕੋਈ API ਖ਼ਰਚ ਨਹੀਂ — ਸਾਰਾ ਕੁਝ ਤੁਹਾਡੇ ਮਸ਼ੀਨ 'ਤੇ ਲੋਕਲ ਚਲਦਾ ਹੈ।

**ਇਹਨੂੰ ਵਿਲੱਖਣ ਬਨਾਉਣ ਵਾਲੀ ਗੱਲ:**
- **🤖 ਅਸਲ ਮਲਟੀ-ਏਜੰਟ ਆਰਕਸਟਰੈਸ਼ਨ** - ਖ਼ਾਸ AI ਏਜੰਟ ਬਣਾਓ ਜੋ ਰਿਸਰਚ, ਲਿਖਣ ਅਤੇ ਆਡੀਓ ਉਤਪਾਦਨ ਕਰਦੇ ਹਨ  
- **🎯 ਪੂਰੀ ਉਤਪਾਦਨ ਪਾਈਪਲਾਈਨ** - ਵਿਸ਼ੇ ਦੀ ਚੋਣ ਤੋਂ ਲੈ ਕੇ ਅੰਤਿਮ ਪੋਡਕਾਸਟ ਆਡੀਓ ਤੱਕ  
- **💻 100% ਲੋਕਲ ਡਿਪਲਾਇਮੈਂਟ** - ਪੂਰੀ ਗੁਪਤਤਾ ਅਤੇ ਕੰਟਰੋਲ ਲਈ Ollama ਅਤੇ ਲੋਕਲ ਮਾਡਲ (Qwen-3-8B) ਵਰਤੇ ਜਾਂਦੇ ਹਨ  
- **🎤 ਟੈਕਸਟ-ਟੂ-ਸਪੀਚ ਇਨਟੀਗ੍ਰੇਸ਼ਨ** - ਸਕ੍ਰਿਪਟਾਂ ਨੂੰ ਕੁਦਰਤੀ ਆਵਾਜ਼ ਵਾਲੀ ਬਹੁਲੇਖਕ ਗੱਲਬਾਤਾਂ ਵਿੱਚ ਬਦਲੋ  
- **✋ ਮਨੁੱਖੀ-ਰੂਪ ਅੰਦਰ ਵਾਲੇ ਵਰਕਫਲੋਜ਼** - ਮਾਨਤਾ ਦੇ ਦਰਵਾਜ਼ੇ ਗੁਣਵੱਤਾ ਯਕੀਨੀ ਬਣਾ ਰਹੇ ਹਨ ਅਤੇ ਆਟੋਮੇਸ਼ਨ ਨੂੰ ਜਾਰੀ ਰੱਖਦੇ ਹਨ  

**ਤਿੰਨ ਅਧਿਆਇ ਸਿੱਖਣ ਯਾਤਰਾ:**

| ਅਧਿਆਇ | ਧਿਆਨ | ਮੁੱਖ ਕੁਸ਼ਲਤਾ | ਸਮਾਂ ਅਵਧੀ |
|-----|-------|------------|----------|
| **[ਅਧਿਆਇ 1: ਆਪਣੇ AI ਸਹਾਇਕਾਂ ਨਾਲ ਮਿਲੋ](./WorkshopForAgentic/md/01.BuildAIAgentWithSLM.md)** | ਆਪਣਾ ਪਹਿਲਾ AI ਏਜੰਟ ਬਣਾਓ | ਕੁਝ ਚੀਜ਼ਾਂ ਦਾ ਇਨਟੀਗ੍ਰੇਸ਼ਨ • ਵੈੱਬ ਖੋਜ • ਸਮੱਸਿਆ ਸਮਾਧਾਨ • ਏਜੰਟਿਕ ਵਿਚਾਰਧਾਰਾ | 2-3 ਘੰਟੇ |
| **[ਅਧਿਆਇ 2: ਆਪਣੀ ਉਤਪਾਦਨ ਟੀਮ ਜੋੜੋ](./WorkshopForAgentic/md/02.AIAgentOrchestrationAndWorkflows.md)** | ਕਈ ਏਜੰਟਾਂ ਦੀ ਆਰਕੀਸਟ੍ਰੇਸ਼ਨ | ਟੀਮ ਸਹਿਯੋਗ • ਮਾਨਤਾ ਵਰਕਫਲੋਜ਼ • DevUI ਇੰਟਰਫੇਸ • ਮਨੁੱਖੀ ਨਿਗਰਾਨੀ | 3-4 ਘੰਟੇ |
| **[ਅਧਿਆਇ 3: ਆਪਣਾ ਪੋਡਕਾਸਟ ਜੀਵੰਤ ਬਣਾਓ](./WorkshopForAgentic/md/03.Multi-SpeakerPodcastGenerationWithVibeVoice.md)** | ਪੋਡਕਾਸਟ ਆਡੀਓ ਤਿਆਰ ਕਰੋ | ਟੈਕਸਟ-ਟੂ-ਸਪੀਚ • ਬਹੁਲੇਖਕ ਸੁਤੰਤਰਤਾ • ਲੰਬੀ ਸ਼ੈਲੀ ਆਡੀਓ • ਪੂਰੀ ਆਟੋਮੇਸ਼ਨ | 2-3 ਘੰਟੇ |

**ਟੈਕਨੋਲੋਜੀਆਂ ਵਰਤੀ ਗਈਆਂ:**
- **Microsoft Agent Framework** - ਮਲਟੀ-ਏਜੰਟ ਆਰਕਸਟਰੈਸ਼ਨ ਅਤੇ ਸਹਿਯੋਗ  
- **Ollama** - ਲੋਕਲ AI ਮਾਡਲ ਰਨਟਾਈਮ (ਕੋਈ ਕਲਾਉਡ కావਾਂ ਨਹੀਂ)  
- **Qwen-3-8B** - ਏਜੰਟਿਕ ਕੰਮਾਂ ਲਈ ਓਪਨ-ਸੋਰਸ ਭਾਸ਼ਾ ਮਾਡਲ  
- **ਟੈਕਸਟ-ਟੂ-ਸਪੀਚ API** - ਪੋਡਕਾਸਟ ਬਣਾਉਣ ਲਈ ਕੁਦਰਤੀ ਆਵਾਜ਼ ਬਣਾਉਣਾ  

**ਹਾਰਡਵੇਅਰ ਸਹਾਇਤਾ:**
- ✅ **CPU ਮੋਡ** - ਕਿਸੇ ਵੀ ਅਧੁਨਿਕ ਕੰਪਿਊਟਰ 'ਤੇ ਕੰਮ ਕਰਦਾ ਹੈ (8GB+ RAM ਦੀ ਸਿਫਾਰਸ਼)  
- 🚀 **GPU ਤੀਜ਼ੀ** - NVIDIA/AMD GPUs ਨਾਲ ਬਹੁਤ ਤੇਜ਼ ਇੰਫਰੈਂਸ  
- ⚡ **NPU ਸਹਾਇਤਾ** - ਅਗਲੀ ਪੀੜੀ ਦਾ ਨਿਊਰਲ ਪ੍ਰੋਸੈਸਿੰਗ ਯੂਨਿਟ ਤੇਜ਼ੀ  

**ਇਹ ਕਿਸ ਲਈ ਬੇਹਤਰੀਨ ਹੈ:**
- ਮਲਟੀ-ਏਜੰਟ AI ਪ੍ਰਣਾਲੀਆਂ ਸਿੱਖਣ ਵਾਲੇ ਵਿਕਾਸਕਾਰ  
- AI ਆਟੋਮੇਸ਼ਨ ਅਤੇ ਵਰਕਫਲੋਜ਼ ਵਿੱਚ ਰੁਚੀ ਰੱਖਣ ਵਾਲੇ  
- AI ਸਹਾਇਤਾ ਪ੍ਰੋਡਕਸ਼ਨ ਵਿੱਚ ਦਿਲਚਸਪੀ ਰੱਖਣ ਵਾਲੇ ਸਮੱਗਰੀ ਸਿਰਜਣਹਾਰ  
- ਪ੍ਰਯੋਗਾਤਮਕ AI ਆਰਕਸਟਰੈਸ਼ਨ ਪੈਟਰਨ ਦਾ ਅਧਿਐਨ ਕਰਨ ਵਾਲੇ ਵਿਦਿਆਰਥੀ  

**ਸਿਲੇਬਸ ਸ਼ੁਰੂ ਕਰੋ**: [🎙️ AI ਪੋਡਕਾਸਟ ਸਟੂਡੀਓ ਵਰਕਸ਼ਾਪ →](./WorkshopForAgentic/README.md)

### 📊 **ਸਿੱਖਣ ਰਾਹ ਦਾ ਸਾਰ**
- **ਮੁੱਲ ਸਮਾਂ**: 36-45 ਘੰਟੇ  
- **ਸ਼ੁਰੂਆਤੀ ਰਾਹ**: ਮੋਡਿਊਲ 01-02 (7-9 ਘੰਟੇ)  
- **ਮੱਧਮ ਦਰਜੇ ਦਾ ਰਾਹ**: ਮੋਡਿਊਲ 03-04 (9-11 ਘੰਟੇ)  
- **ਉੱਚ ਦਰਜੇ ਦਾ ਰਾਹ**: ਮੋਡਿਊਲ 05-07 (12-15 ਘੰਟੇ)  
- **ਮਾਹਰ ਰਾਹ**: ਮੋਡਿਊਲ 08 (8-10 ਘੰਟੇ)  

## ਤੁਸੀਂ ਜੋ ਬਣਾਉਂਦੇ ਹੋ

### 🎯 ਮੁੱਖ ਕੁਸ਼ਲਤਾਵਾਂ
- **ਐਜ AI ਵਾਸ਼ਤਵਿਕਤਾ**: ਕਲਾਉਡ ਇਨਟੀਗ੍ਰੇਸ਼ਨ ਵਾਲੇ ਲੋਕਲ-ਪਹਿਲਾਂ AI ਪ੍ਰਣਾਲੀ डिजाइन ਕਰੋ  
- **ਮਾਡਲ ਅਪਟੀਮਾਈਜ਼ੇਸ਼ਨ**: ਏਜ ਡਿਪਲਾਇਮੈਂਟ ਲਈ ਮਾਡਲਾਂ ਨੂੰ ਕਵਾਂਟਾਈਜ਼ ਅਤੇ ਕੰਪ੍ਰੈਸ ਕਰੋ (85% ਤੇਜ਼, 75% ਅਕਾਰ ਘਟਾਓ)  
- **ਮਲਟੀ-ਪਲੇਟਫਾਰਮ ਡਿਪਲਾਇਮੈਂਟ**: ਵਿਂਡੋਜ਼, ਮੋਬਾਈਲ, ਐਮਬੈਡਡ ਅਤੇ ਕਲਾਉਡ-ਇਜ ਹਾਈਬ੍ਰਿਡ ਪ੍ਰਣਾਲੀਆਂ  
- **ਉਤਪਾਦਨ ਕਾਰਜ**: ਉਤਪਾਦਨ ਵਿੱਚ ਐਜ AI ਦਾ ਨਿਰੀਖਣ, ਪੈਮਾਨਾ ਅਤੇ ਬਨਾਏ ਰੱਖਣਾ  

### 🏗️ ਪ੍ਰਯੋਗਿਕ ਪ੍ਰਾਜੈਕਟ
- **Foundry ਲੋਕਲ ਚੈਟ ਐਪਲਿਕੇਸ਼ਨ**: ਮਾਡਲ ਬਦਲਣ ਵਾਲਾ ਵਿੰਡੋਜ਼ 11 ਮੂਲ ਐਪ  
- **ਮਲਟੀ-ਏਜੰਟ ਪ੍ਰਣਾਲੀਆਂ**: ਜਟਿਲ ਵਰਕਫਲੋਜ਼ ਲਈ ਕੋਆਰਡੀਨੇਟਰ ਅਤੇ ਖ਼ਾਸ ਏਜੰਟ  
- **RAG ਐਪਲੀਕੇਸ਼ਨ**: ਲੋਕਲ ਦਸਤਾਵੇਜ਼ ਪ੍ਰਕਿਰਿਆਵਾਂ ਅਤੇ ਵੇਕਟਰ ਖੋਜ  
- **ਮਾਡਲ ਰੂਟਰ**: ਕੰਮ ਦੇ ਵਿਸ਼ਲੇਸ਼ਣ ਦੇ ਆਧਾਰ 'ਤੇ ਮਾਡਲ ਚੁਣਨਾ  
- **API ਫਰੇਮਵਰਕਸ**: ਸਟ੍ਰੀਮਿੰਗ ਅਤੇ ਹੈਲਥ ਮੋਨੀਟਰਿੰਗ ਨਾਲ ਪ੍ਰੋਡਕਸ਼ਨ-ਤਿਆਰ ਕਲਾਇੰਟ  
- **ਕ੍ਰਾਸ-ਪਲੇਟਫਾਰਮ ਟੂਲਜ਼**: LangChain/ਸੈਮੈਂਟਿਕ ਕਰਨਲ ਇਨਟੀਗ੍ਰੇਸ਼ਨ ਪੈਟਰਨ  

### 🏢 ਉਦਯੋਗਿਕ ਐਪਲੀਕੇਸ਼ਨ
**ਉਤਪਾਦਨ** • **ਹੈਲਥਕੇਅਰ** • **ਆਟੋਨੋਮਸ ਵਾਹਨ** • **ਸਮਾਰਟ ਸ਼ਹਿਰ** • **ਮੋਬਾਈਲ ਐਪਸ**

## ਤੁਰੰਤ ਸ਼ੁਰੂਆਤ

**ਸਿਫਾਰਸ਼ੀ ਸਿੱਖਣ ਰਾਹ** (20-30 ਘੰਟੇ ਕੁੱਲ):

0. **📖 ਪਰਿਚਯ** ([Introduction.md](./introduction.md)): EdgeAI ਬੁਨਿਆਦ + ਉਦਯੋਗ ਸੰਦਰਭ + ਸਿੱਖਣ ਦਾ ਫਰੇਮਵਰਕ  
1. **📚 ਬੁਨਿਆਦ** (ਮੋਡਿਊਲ 01-02): EdgeAI ਧਾਰਣਾਵਾਂ + SLM ਮਾਡਲ ਪਰਿਵਾਰ  
2. **⚙️ ਅਪਟੀਮਾਈਜ਼ੇਸ਼ਨ** (ਮੋਡਿਊਲ 03-04): ਡਿਪਲਾਇਮੈਂਟ + ਕਵਾਂਟਾਈਜ਼ੇਸ਼ਨ ਫਰੇਮਵਰਕ  
3. **🚀 ਉਤਪਾਦਨ** (ਮੋਡਿਊਲ 05-06): SLMOps + AI ਏਜੰਟ + ਫੰਕਸ਼ਨ ਕਾਲਿੰਗ  
4. **💻 ਲਾਗੂ ਕਰਨ ਦੀ ਕਾਰਵਾਈ** (ਮੋਡਿਊਲ 07-08): ਪਲੇਟਫਾਰਮ ਨਮੂਨੇ + Foundry ਲੋਕਲ ਟੂਲਕਿਟ  

ਹਰੇਕ ਮੋਡਿਊਲ ਵਿੱਚ ਥਿਊਰੀ, ਪ੍ਰੈਟਿਕਲ ਅਭਿਆਸ ਅਤੇ ਪ੍ਰੋਡਕਸ਼ਨ-ਤਿਆਰ ਗਿਣਤੀ ਦੇ ਉਦਾਹਰਣ ਸ਼ਾਮਲ ਹਨ।

## ਕਰੀਅਰ ਪ੍ਰਭਾਵ

**ਟੈਕਨੀਕਲ ਭੂਮਿਕਾਵਾਂ**: EdgeAI ਸੌਲੂਸ਼ਨ ਆਰਕੀਟੈਕਟ • ML ਇੰਜੀਨੀਅਰ (ਐਜ) • IoT AI ਡਿਵੈਲਪਰ • ਮੋਬਾਈਲ AI ਡਿਵੈਲਪਰ

**ਉਦਯੋਗ ਖੇਤਰ**: ਉਤਪਾਦਨ 4.0 • ਹੈਲਥਕੇਅਰ ਤਕਨਾਲੋਜੀ •ਆਟੋਨੋਮਸ ਪ੍ਰਣਾਲੀਆਂ • ਫਿਨਟੈਕ • ਉਪਭੋਗਤਾ ਇਲੈਕਟ੍ਰਾਨਿਕਸ

**ਪੋਰਟਫੋਲਿਓ ਪ੍ਰਾਜੈਕਟ**: ਮਲਟੀ-ਏਜੰਟ ਪ੍ਰਣਾਲੀਆਂ • ਉਤਪਾਦਨ RAG ਐਪ • ਕ੍ਰਾਸ-ਪਲੇਟਫਾਰਮ ਡਿਪਲਾਇਮੈਂਟ • ਕਾਰਗੁਜ਼ਾਰੀ ਅਪਟੀਮਾਈਜ਼ੇਸ਼ਨ

## ਰਿਪੋਜ਼ਿਟਰੀ ਢਾਂਚਾ

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

## ਕੋਰਸ ਹਾਈਲਾਈਟਸ

✅ **ਤਰੱਕੀਸ਼ੀਲ ਸਿੱਖਿਆ**: ਥਿਊਰੀ → ਅਮਲ → ਉਤਪਾਦਨ ਡਿਪਲਾਇਮੈਂਟ  
✅ **ਅਸਲੀ ਕੇਸ ਅਧਿਐਨ**: Microsoft, ਜਪਾਨ ਏਅਰਲਾਇਨਜ਼, ਉਦਯੋਗ ਅਮਲ  
✅ **ਹੈਂਡਸ-ਆਨ ਉਦਾਹਰਣ**: 50+ ਉਦਾਹਰਣ, 10 ਵਿਆਪਕ Foundry ਲੋਕਲ ਡੈਮੋਜ਼  
✅ **ਕਾਰਗੁਜ਼ਾਰੀ ਧਿਆਨ**: 85% ਤੇਜ਼ੀ, 75% ਅਕਾਰ ਘਟਾਓ  
✅ **ਮਲਟੀ-ਪਲੇਟਫਾਰਮ**: ਵਿਂਡੋਜ਼, ਮੋਬਾਈਲ, ਐਮਬੈਡਡ, ਕਲਾਉਡ-ਇਜ ਹਾਈਬ੍ਰਿਡ  
✅ **ਉਤਪਾਦਨ ਤਿਆਰ**: ਨਿਗਰਾਨੀ, ਮਾਪਬੰਦੀ, ਸੁਰੱਖਿਆ, ਅਨੁਕੂਲਤਾ ਫਰੇਮਵਰਕ  

📖 **[ਅਧਿਐਨ ਗਾਈਡ ਉਪਲਬਧ](STUDY_GUIDE.md)**: ਢਾਂਚਾਬੱਧ 20 ਘੰਟਿਆਂ ਦਾ ਸਿੱਖਣ ਰਾਹ ਸਮੇਂ ਦੀ ਵੰਡ ਅਤੇ ਸਵੈ-ਮੂਲਾਂਕਣ ਸੰਦ ਦੇ ਨਾਲ।

---

**EdgeAI ਭਵਿੱਖ ਦੀ AI ਡਿਪਲਾਇਮੈਂਟ ਦਾ ਪ੍ਰਤੀਕ ਹੈ**: ਲੋਕਲ-ਪਹਿਲਾਂ, ਗੁਪਤਤਾ ਸੰਭਾਲਦਾ ਅਤੇ ਪ੍ਰਭਾਵਸ਼ਾਲੀ। ਇਹ ਕੁਸ਼ਲਤਾਵਾਂ ਸਿੱਖੋ ਤੇ ਅਗਲੀ ਪੀੜੀ ਦੇ ਬੁੱਧੀਮਾਨ ਐਪਲੀਕੇਸ਼ਨਾਂ ਦਾ ਨਿਰਮਾਣ ਕਰੋ।

## ਹੋਰ ਕੋਰਸ

ਸਾਡੇ ਟੀਮ ਹੋਰ ਕੋਰਸ ਤਿਆਰ ਕਰਦੀ ਹੈ! ਵੇਖੋ:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j ਲਈ ਸ਼ੁਰੂਆਤੀ](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js ਲਈ ਸ਼ੁਰੂਆਤੀ](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)
[![LangChain ਲਈ ਸ਼ੁਰੂਆਤੀ](https://img.shields.io/badge/LangChain%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://github.com/microsoft/langchain-for-beginners?WT.mc_id=m365-94501-dwahlin)
---

### Azure / Edge / MCP / Agents
[![AZD ਲਈ ਸ਼ੁਰੂਆਤੀ](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Edge AI ਲਈ ਸ਼ੁਰੂਆਤੀ](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP ਲਈ ਸ਼ੁਰੂਆਤੀ](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![AI Agents ਲਈ ਸ਼ੁਰੂਆਤੀ](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---

### ਜਨਰੇਟਿਵ AI ਸਿਰੀਜ਼
[![ਜਨਰੇਟਿਵ AI ਲਈ ਸ਼ੁਰੂਆਤੀ](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![ਜਨਰੇਟਿਵ AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![ਜਨਰੇਟਿਵ AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![ਜਨਰੇਟਿਵ AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---

### ਮੂਲ ਸਿੱਖਿਆ
[![ML ਲਈ ਸ਼ੁਰੂਆਤੀ](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![ਡਾਟਾ ਸਕਾਇੰਸ ਲਈ ਸ਼ੁਰੂਆਤੀ](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![AI ਲਈ ਸ਼ੁਰੂਆਤੀ](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![ਸਾਈਬਰਸੁਰੱਖਿਆ ਲਈ ਸ਼ੁਰੂਆਤੀ](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![ਵੈੱਬ ਡੈਵ ਲਈ ਸ਼ੁਰੂਆਤੀ](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![IoT ਲਈ ਸ਼ੁਰੂਆਤੀ](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![XR ਵਿਕਾਸ ਲਈ ਸ਼ੁਰੂਆਤੀ](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---

### ਕੋਪਾਇਲਟ ਸਿਰੀਜ਼
[![Copilot for AI Paired Programming](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot for C#/.NET](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot Adventure](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## ਮਦਦ ਪ੍ਰਾਪਤ ਕਰਨਾ

ਜੇ ਤੁਸੀਂ ਅਟਕ ਜਾਂਦੇ ਹੋ ਜਾਂ AI ਐਪ ਬਣਾਉਣ ਬਾਰੇ ਕੋਈ ਸਵਾਲ ਹੈ, ਤਾਂ ਸ਼ਾਮਲ ਹੋਵੋ:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

ਜੇ ਤੁਹਾਡੇ ਕੋਲ ਉਤਪਾਦ 'ਤੇ ਪ੍ਰਤੀਕ੍ਰਿਆ ਜਾਂ ਗਲਤੀਆਂ ਹਨ ਤਾਂ ਜਦੋਂ ਤੁਸੀਂ ਬਣਾਉਂਦੇ ਹੋ ਉਦੋਂ ਜਾਓ:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ਅਸਵੀਕਾਰੋਪੱਤਰ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਨਾਲ ਅਨੁਵਾਦਿਤ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਤਾ ਲਈ ਯਤਨਸ਼ੀਲ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਸਵਚालित ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਮਰਥਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੇ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਅਧਿਕਾਰਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਣ ਜਾਣਕਾਰੀ ਲਈ, ਪ੍ਰੋਫੈਸ਼ਨਲ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਉਪਜੀਆਂ ਸਮਝਦਾਰੀਆਂ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆਵਾਂ ਲਈ ਅਸੀਂ ਜ਼ਿੰਮੇਵਾਰ ਨਾਹੀਂ ਹਾਂ।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
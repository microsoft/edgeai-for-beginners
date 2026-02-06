# EdgeAI for Beginners 


![Course cover image](../../translated_images/my/cover.eb18d1b9605d754b.webp)

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
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](./README.md) | [Chinese (Simplified)](../zh-CN/README.md) | [Chinese (Traditional, Hong Kong)](../zh-HK/README.md) | [Chinese (Traditional, Macau)](../zh-MO/README.md) | [Chinese (Traditional, Taiwan)](../zh-TW/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../pt-BR/README.md) | [Portuguese (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

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
**[🎬 AI Podcast Studio အလုပ်ရုံဆွေးနွေးပွဲ စတင်ရန်](./WorkshopForAgentic/README.md)**

**သင်၏ မစ်ရှင်**: "Future Bytes" ဟုခေါ်သော AI အေဂျင့်များဖြင့် တည်ဆောက်ထားသည့် နည်းပညာပေါ်ဒ်ကတ်စ်ကို စတင်မိတ်ဆက်ပါ။ တိတိကျကျက်ျပ်၍ ကမ်းလှမ်းချက်မရှိ၊ API ကုန်ကျစရိတ်မရှိ— အားလုံးကို သင်၏ ကွန်ပျူတာတွင် တစ်ပြိုင်နက် ပြေးဆဲဖြစ်စေပါ။

**ဤအရာကို ထူးခြားစေသည့် အချက်များ:**
- **🤖 အမှန်တကယ် Multi-Agent စီမံခန့်ခွဲမှု** - သုတေသနလုပ်၊ ရေးသား၊ အသံထုတ်လုပ်မှုကို စီမံပေးသည့် အထူးပြု AI အေဂျင့်များတည်ဆောက်ပါ
- **🎯 အပြည့်အစုံ ဖော်ပြည့်စုံသော ထုတ်လုပ်မှု လမ်းကြောင်း** - ခေါင်းစဉ်ရွေးချယ်မှုမှ နောက်ဆုံး Podcast အသံထုတ်ရလဒ်အထိ
- **💻 ၁၀၀% ဒေသတွင်း စက်ပေါ်တွင် စစ်ဆေးအသုံးပြုမှု** - Ollama နှင့် ဒေသတွင်း မော်ဒယ်များ (Qwen-3-8B) ကို သုံး၍ လုံခြုံရေးနှင့် ထိန်းချုပ်မှုအပြည့်အဝ
- **🎤 စာသားမှ အသံပြောင်းသွားခြင်း အတွဲအဆက်** - စာသားများကို သဘာဝကျပြီး စကားပြောသည်များစွာပါဝင်သော စကားဝိုင်းတစ်ခုအဖြစ် ပြောင်းလဲပေးသည်
- **✋ လူ့စွမ်းအားပါ အလုပ်ဆောင်ခြင်းလမ်းကြောင်းများ** - အရည်အသွေးအတည်ပြုရန် ခွင့်ပြုချက်တံခါးများဖြင့် အလိုအလျောက် ဆောင်ရွက်မှုကို ထိန်းသိမ်းသည်

**သံုးဆု အတွဲသင်ယူခရီး:**

| အတွဲ | အာရုံစိုက်ရာ | အဓိက ကျွမ်းကျင်မှုများ | ကြာချိန် |
|-----|-------|------------|----------|
| **[အတွဲ ၁: သင်၏ AI အကူအညီများနှင့် မိတ်ဆက်ခြင်း](./WorkshopForAgentic/md/01.BuildAIAgentWithSLM.md)** | သင်၏ ပထမဆုံး AI အေဂျင့် တည်ဆောက်ခြင်း | ကိရိယာ ပေါင်းစပ်မှု • ဝက်ဘ် ရှာဖွေရေး • ပြဿနာဖြေရှင်းမှု • Agentic စဉ်းစားမှု | ၂-၃ နာရီ |
| **[အတွဲ ၂: သင်၏ ထုတ်လုပ်ရေး အဖွဲ့ကို စုစည်းခြင်း](./WorkshopForAgentic/md/02.AIAgentOrchestrationAndWorkflows.md)** | အစိတ်အပိုင်း အများအပြားကို စီမံခန့်ခွဲခြင်း | အဖွဲ့ညီညွတ်မှု • ခွင့်ပြုလမ်းကြောင်းများ • DevUI မျက်နှာပြင် • လူ့ကြီးကြပ်ခြင်း | ၃-၄ နာရီ |
| **[အတွဲ ၃: သင်၏ ပြောကြားပွဲကို ဘဝသို့ ဖန်တီးခြင်း](./WorkshopForAgentic/md/03.Multi-SpeakerPodcastGenerationWithVibeVoice.md)** | ပေါ်ဒ်ကတ်စ် အသံထုတ်လုပ်ခြင်း | စာသားမှ အသံပြောင်းခြင်း • စကားပြောသူများစွာပါဝင်ခြင်း • ရုပ်သံတစ်လျှောက်အသံ • အလိုအလျောက်ပြုလုပ်မှု | ၂-၃ နာရီ |

**အသုံးပြုသော နည်းပညာများ:**
- **Microsoft Agent Framework** - Multi-agent စီမံခန့်ခွဲမှုနှင့် ညှိနှိုင်းမှု
- **Ollama** - ဒေသတွင်း AI မော်ဒယ် လည်ပတ်မှု (Cloud မလိုအပ်ပါ)
- **Qwen-3-8B** - agentic လုပ်ဆောင်မှုများအတွက် အထူးတင်ပြု လွတ်လပ်သောဘာသာစကားမော်ဒယ်
- **စာသားမှ အသံပြောင်း API များ** - ပေါ်ဒ်ကတ်စ် ဖန်တီးမှုအတွက် သဘာဝအသံဖြင့် ပေါင်းစပ်ခြင်း

**ဟာ့ဒ်ဝဲ ထောက်ပံ့မှု:**
- ✅ **CPU မုဒ်** - ခေတ္တကွန်ပျူတာ များပေါ်တွင် လည်ပတ်နိုင်သည် (8GB+ RAM အကြံပြု)
- 🚀 **GPU အားမြှင့်နှုန်း** - NVIDIA/AMD GPU များဖြင့် အလွန်လျင်မြန်သော မှတ်ချက်တင်မှု
- ⚡ **NPU ထောက်ပံ့မှု** - နောက်တန်း Neural Processing Unit အမြန်မြှင့်မှု

**အတော်လေး သင့်တော်သောသူများ:**
- Multi-agent AI စနစ်များ သင်ယူလိုသူများ
- AI အလိုအလျောက်လုပ်ဆောင်မှုနှင့် လုပ်ငန်းစဉ်များ စိတ်ဝင်စားသူ
- AI အကူအညီဖြင့် ထုတ်လုပ်မှု ရေးသားသူများ
- တက်ကြွစွာ AI စီမံခန့်ခွဲမှု နည်းပညာများ လေ့လာနေသူ ကျောင်းသားများ

**တည်ဆောက်ရန် စတင်ပါ**: [🎙️ AI Podcast Studio အလုပ်ရုံဆွေးနွေးပွဲ →](./WorkshopForAgentic/README.md)

### 📊 **သင်ယူမှုလမ်းကြောင်း အကျဉ်းချုပ်**
- **စုစုပေါင်း ကြာချိန်**: ၃၆-၄၅ နာရီ
- **အစပြုလမ်းကြောင်း**: အပိုင်း ၀၁-၀၂ (၇-၉ နာရီ)  
- **အလတ်အလတ်လမ်းကြောင်း**: အပိုင်း ၀၃-၀၄ (၉-၁၁ နာရီ)
- **အဆင့်မြင့်လမ်းကြောင်း**: အပိုင်း ၀၅-၀၇ (၁၂-၁၅ နာရီ)
- **ကျွမ်းကျင်မှုလမ်းကြောင်း**: အပိုင်း ၀၈ (၈-၁၀ နာရီ)

## သင် တည်ဆောက်မည့် အရာများ

### 🎯 အဓိက ကျွမ်းကျင်မှုများ
- **Edge AI ဖွဲ့စည်းမှု**: ဒေသတွင်းပထမ AI စနစ်များ လက်တင်တပ်ဆင်၍ Cloud ပေါင်းစပ်မှုပါ
- **မော်ဒယ်များ ဖော်ပြင်တိုးတက်မှု**: မော်ဒယ်များကို အတိုအပွှာနှင့် မှုတ်ချ၍ Edge စနစ်တွင် အသုံးပြုရမည့်အတွက်တိုးမြှင့်ခြင်း (အမြန်နှုန်း ၈၅% ပိုမိုမြန်၊ အရွယ်အစား ၇၅% လျော့နည်းခြင်း)
- **စက်ပလက်ဖောင်းများစွာ အကောင်အထည်ဖော်ခြင်း**: Windows, မိုဘိုင်း, ထည့်သွင်းထားသောစနစ်များနှင့် Cloud-Edge ပေါင်းစပ်စနစ်များ
- **ထုတ်လုပ်မှု လုပ်ငန်းစဉ်များ**: ထုတ်လုပ်မှုအတွင်း Edge AI ကို ကြည့်ရှု့ခြင်း၊ တိုးချဲ့ခြင်းနှင့် ထိန်းသိမ်းခြင်း

### 🏗️ လက်တွေ့ ပရောဂျက်များ
- **Foundry ဒေသတွင်း စကားပြော App များ**: Windows 11 သဘာဝ native application များနှင့် မော်ဒယ်များရွေးချယ်မှု
- **Multi-Agent စနစ်များ**: လုပ်ငန်းစဉ်ရှုပ်ထွေးမှုများအတွက် အထူးကွက်ဆက်တူအရေးပါတဲ့ အေဂျင့်များဖြင့်ညှိနှိုင်းသူ
- **RAG အက်ပ်များ**: ဒေသတွင်း စာရွက်စာတမ်းများကို လက်တွဲ ရှာဖွေရေးဖြင့် ကိုင်တွယ်ခြင်း
- **မော်ဒယ် ရွေးချယ်သူများ**: တာဝန်အရနည်းပညာမျိုးစုံမှ မော်ဒယ်ကို ထူးခြားသိမြင်ရွေးချယ်မှု
- **API ဖရိမ်ဝန်များ**: ထုတ်လုပ်ရန် အသင့်ပြင်သော client များ၊ စီးဆင်းမှုနှင့် ကျန်းမာရေး ထိန်းသိမ်းမှုတို့ပါဝင်သည်
- **Cross-Platform ကိရိယာများ**: LangChain/Semantic Kernel ပေါင်းစပ်အသုံးပြုမှု နည်းပညာ များ

### 🏢 စက်မှုလုပ်ငန်း အက်ပ်လီကေးရှင်းများ
**ထုတ်လုပ်မှု** • **ကျန်းမာရေး** • **အလိုအလျောက် ယာဉ်များ** • **Smart မြို့ပြ** • **မိုဘိုင်း အက်ပ်များ**

## မျက်နှာဖုံး စတင်ခြင်း

**အကြံပြုသင်ယူမှု လမ်းကြောင်း** (စုစုပေါင်း ၂၀-၃၀ နာရီ):

0. **📖 နိဒါန်း** ([Introduction.md](./introduction.md)): EdgeAI အခြေခံ + စက်မှုလုပ်ငန်း ပတ်ဝန်းကျင် + သင်ယူမှု ဖွဲ့စည်းချက်  
1. **📚 အခြေခံ** (Module 01-02): EdgeAI မှတ်သားချက်များ + SLM မော်ဒယ် မျိုးစုံ  
2. **⚙️ ဖွဲ့စည်းတိုးတက်မှု** (Module 03-04): တပ်ဆင်မှု + မော်ဒယ် အတိုအပွှာ ဖွဲ့စည်းမှု  
3. **🚀 ထုတ်လုပ်မှု** (Module 05-06): SLMOps + AI အေဂျင့်များ + Function Calling  
4. **💻 အကောင်အထည်ဖော်ခြင်း** (Module 07-08): ပလက်ဖောင်း ဥပမာများ + Foundry ဒေသတွင်း ကိရိယာများ

အသီးသီး မော်ဂျူးများမှာ သဘောတရား၊ လက်တွေ့ လေ့ကျင့်မှုများနှင့် ထုတ်လုပ်မှု အသုံးပြုရန် ကုဒ် နမူနာများ ပါဝင်သည်။

## အလုပ်အကိုင် အကျိုးသက်ရောက်မှု

**နည်းပညာဆိုင်ရာ အခန်းကဏ္ဍများ**: EdgeAI ဖြေရှင်းရေး ဆောက်လုပ်သူ • ML အင်ဂျင်နီယာ (Edge) • IoT AI ဖော်ပြသူ • မိုဘိုင်း AI ဖော်ပြသူ

**စက်မှုလုပ်ငန်း ဌာနများ**: ထုတ်လုပ်မှု 4.0 • ကျန်းမာရေး နည်းပညာ • အလိုအလျောက် စနစ်များ • FinTech • စားသုံးသူ လျှပ်စစ်ပစ္စည်းများ

**ပေါ်ဘုတ်ဖိုလ်ရာ ပရောဂျက်များ**: Multi-agent စနစ်များ • ထုတ်လုပ်ရေး RAG အက်ပ်များ • Cross-platform တပ်ဆင်မှု • လုပ်ဆောင်မှု တိုးတက်မှု

## Repository ဖွဲ့စည်းမှု

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

## သင်တန်း အထူးအချက်များ

✅ **တိုးတက်မှု သင်ယူမှု**: သဘောတရား → လက်တွေ့ → ထုတ်လုပ်မှု တပ်ဆင်မှု  
✅ **လက်တွေ့ ဥပမာ များ**: Microsoft, Japan Airlines, စက်မှုလုပ်ငန်း လုပ်ဆောင်မှုများ  
✅ **လက်တွေ့ နမူနာများ**: ၅၀+ ဥပမာများ၊ Foundry ဒေသတွင်း ၁၀ ခုပေါင်းစပ်  
✅ **လုပ်ဆောင်မှု အာရုံစိုက်မှု**: အမြန်နှုန်း ၈၅% တိုးတက်မှု၊ အရွယ်အစား ၇၅% လျော့ချမှု  
✅ **စက်ပလက်ဖောင်း များစွာ**: Windows, မိုဘိုင်း, ထည့်သွင်းစနစ်များ, Cloud-Edge ပေါင်းစပ်  
✅ **ထုတ်လုပ်ရန် အသင့်ပြင်**: ကြည့်ရှု့မှု၊ တိုးချဲ့မှု၊ လုံခြုံရေး၊ သတ်မှတ်ချက်များအားဖြင့်

📖 **[လေ့လာမှု လမ်းညွှန် ရရှိနိုင်သည်](STUDY_GUIDE.md)**: သတ်မှတ်ထားသော ၂၀ နာရီ သင်ယူမှု လမ်းကြောင်း၊ အချိန် ခွဲဝေမှု လမ်းညွှန်ချက်များနှင့် ကိုယ်တိုင် အကဲဖြတ်ခြင်းကိရိယာများပါရှိသည်။

---

**EdgeAI သည် AI တပ်ဆင်မှု၏ အနာဂတ် ကိုယ်စားလှယ် ဖြစ်သည်**: ဒေသတွင်း ပထမ၊ ကိုယ်ရေးကိုယ်တာ လုံခြုံမှုနှင့် ထိရောက်မှုရှိသည်။ ဤကျွမ်းကျင်မှုများကို ကျွမ်းကျင်မှုပြု၍ အနာဂတ်နည်းပညာဆန်းသစ်မှုများ ဖန်တီးပါ။

## အခြား သင်တန်းများ

ကျွန်ုပ်တို့အဖွဲ့ အခြား သင်တန်းများ ထုတ်လုပ်ပေးသည်! ကြည့်ရှုပါ:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j စတင်သူများအတွက်](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js စတင်သူများအတွက်](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)
[![LangChain စတင်သူများအတွက်](https://img.shields.io/badge/LangChain%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://github.com/microsoft/langchain-for-beginners?WT.mc_id=m365-94501-dwahlin)
---

### Azure / Edge / MCP / Agents
[![AZD စတင်သူများအတွက်](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Edge AI စတင်သူများအတွက်](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP စတင်သူများအတွက်](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![AI Agents စတင်သူများအတွက်](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Generative AI စီးရီး
[![Generative AI စတင်သူများအတွက်](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Generative AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![Generative AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![Generative AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### အခြေခံသင်ယူမှု
[![ML စတင်သူများအတွက်](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![ဒေတာသိပ္ပံ စတင်သူများအတွက်](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![AI စတင်သူများအတွက်](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![Cybersecurity စတင်သူများအတွက်](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![Web Dev စတင်သူများအတွက်](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![IoT စတင်သူများအတွက်](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![XR ဖွံ့ဖြိုးတိုးတက်မှု စတင်သူများအတွက်](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Copilot စီးရီး
[![Copilot for AI Paired Programming](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot for C#/.NET](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot Adventure](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## အကူအညီရယူခြင်း

AI အက်ပ်များ ဖန်တီးရာတွင် အခက်အခဲရှိပါက သို့မဟုတ် မေးခွန်းများရှိပါက ဝင်ရောက်ပါ-

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

ထုတ်ကုန်တုံ့ပြန်ချက်များ သို့မဟုတ် တည်ဆောက်စဉ်တွင် အမှားများရှိပါက အောက်တွင် သွားရောက်ပါ-

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**အသိပေးချက်**  
ဤစာရွက်ကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ဖြင့် ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးပမ်းပေမယ့်၊ အလိုအလျောက်ဘာသာပြန်ခြင်းကြောင့် ထွက်ပေါ်နိုင်သည့် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ရှိနိုင်ပါကြောင်း သတိပြုပါရန်။ မူလစာရွက်ကို မိမိဘာသာဖြင့်သာ တရားဝင်အချက်အလက်အမြစ်အနေဖြင့် ယူဆသင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် ကျွမ်းကျင်သော လူမှုဘာသာပြန်၏ ဘာသာပြန်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်အသုံးပြုမှုကြောင့် ဖြစ်ပေါ်နိုင်သည့် နားလည်မှုလွဲမှားမှုများအတွက် ကျွန်ုပ်တို့ တာဝန်မယူပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
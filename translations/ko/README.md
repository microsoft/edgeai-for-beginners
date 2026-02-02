# EdgeAI for Beginners 


![Course cover image](../../translated_images/ko/cover.eb18d1b9605d754b.webp)

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
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh-CN/README.md) | [Chinese (Traditional, Hong Kong)](../zh-HK/README.md) | [Chinese (Traditional, Macau)](../zh-MO/README.md) | [Chinese (Traditional, Taiwan)](../zh-TW/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Korean](./README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../pt-BR/README.md) | [Portuguese (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

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
**[🎬 AI 팟캐스트 스튜디오 워크숍 시작하기](./WorkshopForAgentic/README.md)**

**당신의 미션**: AI 에이전트를 직접 만들어 구동하는 완전 AI 기반 기술 팟캐스트 "Future Bytes"를 시작하세요. 클라우드 의존도 없고 API 비용도 없으며 모든 것이 로컬 컴퓨터에서 실행됩니다.

**이 워크숍이 특별한 이유:**
- **🤖 진짜 멀티 에이전트 오케스트레이션** - 조사, 글쓰기, 오디오 제작을 담당하는 전문 AI 에이전트 구축
- **🎯 완전한 제작 파이프라인** - 주제 선정부터 최종 팟캐스트 오디오 출력까지
- **💻 100% 로컬 배포** - Ollama와 로컬 모델(Qwen-3-8B)을 사용해 완벽한 개인정보 보호와 제어 제공
- **🎤 텍스트-투-스피치 통합** - 스크립트를 자연스럽고 다중 화자가 대화하는 듯한 음성으로 변환
- **✋ 인간 개입 워크플로우** - 승인 단계로 품질 보장과 자동화 동시 유지

**3막 학습 여정:**

| 막 | 집중 분야 | 주요 기술 | 소요 시간 |
|-----|-------|------------|----------|
| **[막 1 : AI 비서 만들기](./WorkshopForAgentic/md/01.BuildAIAgentWithSLM.md)** | 첫 AI 에이전트 구축 | 도구 통합 • 웹 검색 • 문제 해결 • 에이전틱 추론 | 2-3 시간 |
| **[막 2 : 제작팀 구성하기](./WorkshopForAgentic/md/02.AIAgentOrchestrationAndWorkflows.md)** | 여러 에이전트 오케스트레이션 | 팀 협력 • 승인 절차 • DevUI 인터페이스 • 인간 감독 | 3-4 시간 |
| **[막 3 : 팟캐스트 완성하기](./WorkshopForAgentic/md/03.Multi-SpeakerPodcastGenerationWithVibeVoice.md)** | 팟캐스트 오디오 생성 | 텍스트-투-스피치 • 다중 화자 합성 • 장시간 오디오 • 완전 자동화 | 2-3 시간 |

**사용 기술:**
- **Microsoft Agent Framework** - 멀티 에이전트 오케스트레이션 및 조정
- **Ollama** - 로컬 AI 모델 런타임 (클라우드 불필요)
- **Qwen-3-8B** - 에이전틱 작업에 최적화된 오픈소스 언어 모델
- **텍스트-투-스피치 API** - 팟캐스트 생성용 자연 음성 합성

**하드웨어 지원:**
- ✅ **CPU 모드** - 최신 컴퓨터에서 작동 (8GB 이상 RAM 권장)
- 🚀 **GPU 가속** - NVIDIA/AMD GPU 활용 시 추론 속도 대폭 향상
- ⚡ **NPU 지원** - 차세대 뉴럴 프로세싱 유닛 가속

**적합 대상:**
- 멀티 에이전트 AI 시스템 학습 개발자
- AI 자동화 및 워크플로우에 관심 있는 모든 분
- AI 지원 제작을 경험하고 싶은 콘텐츠 크리에이터
- 실용 AI 오케스트레이션 패턴을 공부하는 학생들

**지금 시작하세요**: [🎙️ AI 팟캐스트 스튜디오 워크숍 →](./WorkshopForAgentic/README.md)

### 📊 **학습 경로 요약**
- **전체 소요 시간**: 36-45 시간
- **초급 경로**: 모듈 01-02 (7-9 시간)  
- **중급 경로**: 모듈 03-04 (9-11 시간)
- **고급 경로**: 모듈 05-07 (12-15 시간)
- **전문가 경로**: 모듈 08 (8-10 시간)

## 당신이 만들게 될 것

### 🎯 핵심 역량
- **엣지 AI 아키텍처**: 클라우드 통합이 가능한 로컬 퍼스트 AI 시스템 설계
- **모델 최적화**: 엣지 배포용 모델 양자화 및 압축 (속도 85% 향상, 크기 75% 감소)
- **멀티 플랫폼 배포**: 윈도우, 모바일, 임베디드, 클라우드-엣지 하이브리드 시스템
- **운영 및 관리**: 엣지 AI 모니터링, 확장, 유지보수

### 🏗️ 실습 프로젝트
- **Foundry 로컬 채팅 앱**: 모델 전환이 가능한 Windows 11 네이티브 앱
- **멀티 에이전트 시스템**: 복합 워크플로우 조정을 위한 코디네이터 및 전문가 에이전트  
- **RAG 애플리케이션**: 벡터 검색을 활용한 로컬 문서 처리
- **모델 라우터**: 작업 분석에 따른 지능형 모델 선택
- **API 프레임워크**: 스트리밍 및 상태 모니터링이 포함된 프로덕션 클라이언트
- **크로스 플랫폼 도구**: LangChain/semantic Kernel 통합 패턴

### 🏢 산업별 적용
**제조업** • **헬스케어** • **자율주행 차량** • **스마트 시티** • **모바일 앱**

## 빠른 시작

**추천 학습 경로** (총 20-30 시간):

0. **📖 소개** ([Introduction.md](./introduction.md)): EdgeAI 기본 + 산업 배경 + 학습 프레임워크
1. **📚 기초** (모듈 01-02): EdgeAI 개념 + SLM 모델군
2. **⚙️ 최적화** (모듈 03-04): 배포 + 양자화 프레임워크  
3. **🚀 운영** (모듈 05-06): SLMOps + AI 에이전트 + 함수 호출
4. **💻 구현** (모듈 07-08): 플랫폼 샘플 + Foundry Local 툴킷

각 모듈은 이론, 실습, 프로덕션 수준 코드 샘플을 포함합니다.

## 경력 효과

**기술 직군**: EdgeAI 솔루션 아키텍트 • ML 엔지니어(엣지) • IoT AI 개발자 • 모바일 AI 개발자

**산업 분야**: 제조업 4.0 • 헬스케어 기술 • 자율 시스템 • 핀테크 • 소비자 전자제품

**포트폴리오 프로젝트**: 멀티 에이전트 시스템 • 프로덕션 RAG 앱 • 크로스 플랫폼 배포 • 성능 최적화

## 저장소 구조

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

## 강좌 하이라이트

✅ **점진적 학습**: 이론 → 실습 → 프로덕션 배포  
✅ **실제 사례 연구**: Microsoft, 일본항공, 기업 적용 사례  
✅ **체험 샘플**: 50개 이상 예제, 10개의 종합 Foundry Local 데모  
✅ **성능 집중**: 85% 속도 향상, 75% 크기 축소  
✅ **멀티 플랫폼 지원**: 윈도우, 모바일, 임베디드, 클라우드-엣지 하이브리드  
✅ **프로덕션 준비 완료**: 모니터링, 스케일링, 보안, 컴플라이언스 프레임워크

📖 **[학습 가이드 제공](STUDY_GUIDE.md)**: 20시간 구조화된 학습 경로와 시간 배분 가이드, 자기평가 도구 포함.

---

**EdgeAI는 AI 배포의 미래를 대표합니다**: 로컬 퍼스트, 개인정보 보호, 효율성. 이 역량을 마스터하여 차세대 지능형 애플리케이션을 구축하세요.

## 다른 강좌

저희 팀이 제작한 다른 강좌도 확인해 보세요!

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j for Beginners](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js for Beginners](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)
[![LangChain for Beginners](https://img.shields.io/badge/LangChain%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://github.com/microsoft/langchain-for-beginners?WT.mc_id=m365-94501-dwahlin)
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
 
### 핵심 학습
[![ML for Beginners](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![Data Science for Beginners](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![AI for Beginners](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![Cybersecurity for Beginners](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![Web Dev for Beginners](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![IoT for Beginners](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![XR Development for Beginners](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### 코파일럿 시리즈
[![Copilot for AI Paired Programming](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot for C#/.NET](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot Adventure](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## 도움 받기

AI 앱 개발 중 막히거나 질문이 있으면 다음에 참여하세요:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

제품 피드백이나 개발 중 오류가 있으면 방문하세요:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 저희는 정확성을 위해 노력하고 있으나, 자동 번역에는 오류나 부정확성이 포함될 수 있음을 유의하시기 바랍니다. 원문은 해당 문서의 권위 있는 기준으로 간주되어야 합니다. 중요한 정보의 경우 전문적인 사람 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 저희는 책임을 지지 않습니다.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
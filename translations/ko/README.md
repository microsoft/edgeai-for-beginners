<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c8de8ce76af1af156b1c2dee24ed23b0",
  "translation_date": "2025-12-24T23:23:22+00:00",
  "source_file": "README.md",
  "language_code": "ko"
}
-->
# 초보자를 위한 EdgeAI 


![코스 표지 이미지](../../translated_images/cover.eb18d1b9605d754b30973f4e17c6e11ea4f8473d9686ee378d6e7b44e3c70ac7.ko.png)

[![GitHub 기여자](https://img.shields.io/github/contributors/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/graphs/contributors)
[![GitHub 이슈](https://img.shields.io/github/issues/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/issues)
[![GitHub 풀 리퀘스트](https://img.shields.io/github/issues-pr/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/pulls)
[![PR 환영](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

[![Microsoft Foundry 디스코드](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

이 자료를 사용해 시작하려면 다음 단계를 따르세요:

1. **저장소 포크하기**: 클릭 [![GitHub 포크](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork)
2. **저장소 클론하기**:   `git clone https://github.com/microsoft/edgeai-for-beginners.git`
3. [**Azure AI Foundry 디스코드에 가입하여 전문가와 동료 개발자를 만나세요**](https://discord.com/invite/ByRwuEEgH4)


### 🌐 다국어 지원

#### GitHub Action을 통해 지원 (자동화 및 항상 최신 상태)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[아랍어](../ar/README.md) | [벵골어](../bn/README.md) | [불가리아어](../bg/README.md) | [버마어(미얀마)](../my/README.md) | [중국어(간체)](../zh/README.md) | [중국어(번체, 홍콩)](../hk/README.md) | [중국어(번체, 마카오)](../mo/README.md) | [중국어(번체, 대만)](../tw/README.md) | [크로아티아어](../hr/README.md) | [체코어](../cs/README.md) | [덴마크어](../da/README.md) | [네덜란드어](../nl/README.md) | [에스토니아어](../et/README.md) | [핀란드어](../fi/README.md) | [프랑스어](../fr/README.md) | [독일어](../de/README.md) | [그리스어](../el/README.md) | [히브리어](../he/README.md) | [힌디어](../hi/README.md) | [헝가리어](../hu/README.md) | [인도네시아어](../id/README.md) | [이탈리아어](../it/README.md) | [일본어](../ja/README.md) | [칸나다어](../kn/README.md) | [한국어](./README.md) | [리투아니아어](../lt/README.md) | [말레이어](../ms/README.md) | [말라얄람어](../ml/README.md) | [마라티어](../mr/README.md) | [네팔어](../ne/README.md) | [나이지리아 피진어](../pcm/README.md) | [노르웨이어](../no/README.md) | [페르시아어(파르시)](../fa/README.md) | [폴란드어](../pl/README.md) | [포르투갈어(브라질)](../br/README.md) | [포르투갈어(포르투갈)](../pt/README.md) | [펀자브어(구르무키)](../pa/README.md) | [루마니아어](../ro/README.md) | [러시아어](../ru/README.md) | [세르비아어(키릴문자)](../sr/README.md) | [슬로바키아어](../sk/README.md) | [슬로베니아어](../sl/README.md) | [스페인어](../es/README.md) | [스와힐리어](../sw/README.md) | [스웨덴어](../sv/README.md) | [타갈로그어(필리핀)](../tl/README.md) | [타밀어](../ta/README.md) | [텔루구어](../te/README.md) | [태국어](../th/README.md) | [터키어](../tr/README.md) | [우크라이나어](../uk/README.md) | [우르두어](../ur/README.md) | [베트남어](../vi/README.md)
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

**추가 번역을 원하시면 지원되는 언어 목록은 [여기](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md)에 있습니다**
## 소개

**EdgeAI for Beginners**에 오신 것을 환영합니다 – 엣지 인공지능의 변혁적인 세계로의 포괄적인 여정입니다. 이 과정은 강력한 AI 기능과 엣지 디바이스에서의 실무적, 실제 배포 간의 격차를 연결하여, 데이터가 생성되고 의사결정이 이루어져야 하는 곳에서 직접 AI의 잠재력을 활용할 수 있도록 합니다.

### 학습 목표

이 과정은 기초 개념부터 프로덕션 준비 구현까지 안내하며 다음을 다룹니다:
- **엣지 배포에 최적화된 소형 언어 모델(SLMs)**
- **하드웨어 인식 최적화**(다양한 플랫폼 전반)
- **개인정보 보호 기능을 갖춘 실시간 추론**
- **엔터프라이즈 애플리케이션을 위한 프로덕션 배포 전략**

### 엣지AI가 중요한 이유

엣지 AI는 다음과 같은 중요한 현대 과제를 해결하는 패러다임 전환을 의미합니다:
- **개인정보 보호 및 보안**: 민감한 데이터를 클라우드에 노출하지 않고 로컬에서 처리
- **실시간 성능**: 시간에 민감한 애플리케이션에서 네트워크 지연 제거
- **비용 효율성**: 대역폭 및 클라우드 컴퓨팅 비용 절감
- **복원력 있는 운영**: 네트워크 장애 시에도 기능 유지
- **규제 준수**: 데이터 주권 요건 충족

### 엣지 AI

엣지 AI는 추론을 위해 클라우드 리소스에 의존하지 않고 데이터가 생성되는 곳 근처의 하드웨어에서 AI 알고리즘과 언어 모델을 로컬로 실행하는 것을 말합니다. 지연을 줄이고 개인정보 보호를 강화하며 실시간 의사결정을 가능하게 합니다.

### 핵심 원칙:
- **디바이스 내 추론(On-device inference)**: AI 모델이 엣지 디바이스(휴대폰, 라우터, 마이크로컨트롤러, 산업용 PC)에서 실행
- **오프라인 기능**: 지속적인 인터넷 연결 없이 동작
- **저지연**: 실시간 시스템에 적합한 즉각적인 응답
- **데이터 주권**: 민감한 데이터를 로컬에 보관하여 보안 및 규정 준수 개선

### 소형 언어 모델(SLMs)

Phi-4, Mistral-7B, Gemma와 같은 SLM은 더 큰 LLM의 최적화된 버전으로, 다음을 위해 훈련되었거나 증류된 모델입니다:
- **메모리 사용량 감소**: 제한된 엣지 디바이스 메모리를 효율적으로 사용
- **연산 요구량 감소**: CPU 및 엣지 GPU 성능에 맞게 최적화
- **빠른 시작 시간**: 반응형 애플리케이션을 위한 빠른 초기화

이들은 다음과 같은 제약사항을 충족하면서 강력한 NLP 기능을 제공합니다:
- **임베디드 시스템**: IoT 디바이스 및 산업용 컨트롤러
- **모바일 디바이스**: 오프라인 기능이 있는 스마트폰 및 태블릿
- **IoT 디바이스**: 자원이 제한된 센서 및 스마트 디바이스
- **엣지 서버**: GPU 자원이 제한된 로컬 처리 유닛
- **개인용 컴퓨터**: 데스크톱 및 노트북 배포 시나리오

## 강좌 모듈 및 탐색

| 모듈 | 주제 | 중점 영역 | 주요 내용 | 난이도 | 기간 |
|--------|-------|------------|-------------|--------|----------|
| [📖 00 ](./introduction.md) | [엣지AI 소개](./introduction.md) | 기초 및 맥락 | EdgeAI 개요 • 산업 적용 사례 • SLM 소개 • 학습 목표 | 초급 | 1-2 시간 |
| [📚 01](../../Module01) | [엣지AI 기초](./Module01/README.md) | 클라우드 vs 엣지 AI 비교 | 엣지AI 핵심 • 실제 사례 연구 • 구현 가이드 • 엣지 배포 | 초급 | 3-4 시간 |
| [🧠 02](../../Module02) | [SLM 모델 기초](./Module02/README.md) | 모델 계열 및 아키텍처 | Phi Family • Qwen Family • Gemma Family • BitNET • μModel • Phi-Silica | 초급 | 4-5 시간 |
| [🚀 03](../../Module03) | [SLM 배포 실습](./Module03/README.md) | 로컬 및 클라우드 배포 | 심화 학습 • 로컬 환경 • 클라우드 배포 | 중급 | 4-5 시간 |
| [⚙️ 04](../../Module04) | [모델 최적화 툴킷](./Module04/README.md) | 크로스 플랫폼 최적화 | 소개 • Llama.cpp • Microsoft Olive • OpenVINO • Apple MLX • 워크플로우 합성 | 중급 | 5-6 시간 |
| [🔧 05](../../Module05) | [SLMOps 프로덕션](./Module05/README.md) | 프로덕션 운영 | SLMOps 소개 • 모델 증류 • 파인튜닝 • 프로덕션 배포 | 고급 | 5-6 시간 |
| [🤖 06](../../Module06) | [AI 에이전트 및 함수 호출](./Module06/README.md) | 에이전트 프레임워크 및 MCP | 에이전트 소개 • 함수 호출 • 모델 컨텍스트 프로토콜 | 고급 | 4-5 시간 |
| [💻 07](../../Module07) | [플랫폼 구현](./Module07/README.md) | 크로스 플랫폼 샘플 | AI 툴킷 • Foundry Local • Windows 개발 | 고급 | 3-4 시간 |
| [🏭 08](../../Module08) | [Foundry 로컬 툴킷](./Module08/README.md) | 프로덕션 준비된 샘플 | 샘플 애플리케이션 (아래 세부사항 참조) | 전문가 | 8-10 시간 |

### 🏭 **모듈 08: 샘플 애플리케이션**

- [01: REST 채팅 빠른 시작](./Module08/samples/01/README.md)
- [02: OpenAI SDK 통합](./Module08/samples/02/README.md)
- [03: 모델 탐색 및 벤치마킹](./Module08/samples/03/README.md)
- [04: Chainlit RAG 애플리케이션](./Module08/samples/04/README.md)
- [05: 다중 에이전트 오케스트레이션](./Module08/samples/05/README.md)
- [06: 도구로서의 모델 라우터](./Module08/samples/06/README.md)
- [07: 직접 API 클라이언트](./Module08/samples/07/README.md)
- [08: Windows 11 채팅 앱](./Module08/samples/08/README.md)
- [09: 고급 다중 에이전트 시스템](./Module08/samples/09/README.md)
- [10: Foundry 도구 프레임워크](./Module08/samples/10/README.md)

### 🎓 **워크숍: 실습 학습 경로**

프로덕션 수준 구현을 포함한 종합적인 실습 워크숍 자료:

- **[워크숍 가이드](./Workshop/Readme.md)** - 학습 목표, 결과 및 리소스 탐색을 모두 포함
- Python 샘플 (6세션) - 모범 사례, 오류 처리 및 포괄적인 문서로 업데이트됨
- Jupyter 노트북 (인터랙티브 8개) - 벤치마크 및 성능 모니터링을 포함한 단계별 튜토리얼
- 세션 가이드 - 각 워크숍 세션에 대한 상세한 마크다운 가이드
- 검증 도구 - 코드 품질을 확인하고 스모크 테스트를 실행하는 스크립트

**만들게 될 것들:**
- 스트리밍 지원이 있는 로컬 AI 채팅 애플리케이션
- 품질 평가가 포함된 RAG 파이프라인 (RAGAS)
- 다중 모델 벤치마킹 및 비교 도구
- 다중 에이전트 오케스트레이션 시스템
- 작업 기반 선택을 통한 지능형 모델 라우팅

### 📊 **학습 경로 요약**
- **총 소요 시간**: 36-45 시간
- **초급 경로**: 모듈 01-02 (7-9 시간)  
- **중급 경로**: 모듈 03-04 (9-11 시간)
- **고급 경로**: 모듈 05-07 (12-15 시간)
- **전문가 경로**: 모듈 08 (8-10 시간)

## 만들게 될 것들

### 🎯 핵심 역량
- **엣지 AI 아키텍처**: 클라우드 통합을 포함한 로컬 우선 AI 시스템 설계
- **모델 최적화**: 엣지 배포를 위한 모델 양자화 및 압축 (속도 85% 향상, 크기 75% 감소)
- **다중 플랫폼 배포**: Windows, 모바일, 임베디드 및 클라우드-엣지 하이브리드 시스템
- **프로덕션 운영**: 엣지 AI의 모니터링, 스케일링 및 유지 관리

### 🏗️ 실습 프로젝트
- **Foundry Local Chat Apps**: 모델 전환 기능이 있는 Windows 11 네이티브 애플리케이션
- **Multi-Agent Systems**: 복잡한 워크플로우를 위한 전문 에이전트와 코디네이터  
- **RAG Applications**: 벡터 검색을 통한 로컬 문서 처리
- **Model Routers**: 작업 분석에 따른 모델 간 지능적 선택
- **API Frameworks**: 스트리밍 및 상태 모니터링을 갖춘 프로덕션 준비 클라이언트
- **Cross-Platform Tools**: LangChain/Semantic Kernel 통합 패턴

### 🏢 산업 적용 분야
**제조업** • **헬스케어** • **자율주행** • **스마트 시티** • **모바일 앱**

## 빠른 시작

**권장 학습 경로** (총 20-30시간):

0. **📖 소개** ([Introduction.md](./introduction.md)): EdgeAI 기초 + 산업 맥락 + 학습 프레임워크
1. **📚 기초** (모듈 01-02): EdgeAI 개념 + SLM 모델 계열
2. **⚙️ 최적화** (모듈 03-04): 배포 + 양자화 프레임워크  
3. **🚀 프로덕션** (모듈 05-06): SLMOps + AI 에이전트 + 함수 호출
4. **💻 구현** (모듈 07-08): 플랫폼 샘플 + Foundry Local 툴킷

각 모듈에는 이론, 실습 과제 및 프로덕션 준비 코드 샘플이 포함됩니다.

## 경력 영향

**기술 역할**: EdgeAI 솔루션 아키텍트 • ML 엔지니어(엣지) • IoT AI 개발자 • 모바일 AI 개발자

**산업 분야**: 제조 4.0 • 헬스케어 기술 • 자율 시스템 • 핀테크 • 소비자 전자제품

**포트폴리오 프로젝트**: 다중 에이전트 시스템 • 프로덕션 RAG 앱 • 크로스 플랫폼 배포 • 성능 최적화

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

## 코스 하이라이트

✅ **단계적 학습**: 이론 → 실습 → 프로덕션 배포  
✅ **실제 사례 연구**: Microsoft, Japan Airlines, 엔터프라이즈 구현  
✅ **실습 샘플**: 50개 이상의 예제, 10개의 종합 Foundry Local 데모  
✅ **성능 집중**: 속도 85% 향상, 크기 75% 감소  
✅ **다중 플랫폼**: Windows, 모바일, 임베디드, 클라우드-엣지 하이브리드  
✅ **프로덕션 준비**: 모니터링, 스케일링, 보안, 규정 준수 프레임워크

📖 **[학습 가이드 보기](STUDY_GUIDE.md)**: 시간 배분 가이드와 자기 평가 도구가 포함된 구조화된 20시간 학습 경로.

---

**EdgeAI는 AI 배포의 미래를 의미합니다**: 로컬 우선, 개인정보 보호 중심, 효율적입니다. 이러한 기술을 마스터하여 차세대 지능형 애플리케이션을 구축하세요.

## 기타 강좌

우리 팀은 다른 강좌도 제공하고 있습니다! 확인해보세요:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![초보자를 위한 LangChain4j](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![초보자를 위한 LangChain.js](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)

---

### Azure / Edge / MCP / Agents
[![초보자를 위한 AZD](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![초보자를 위한 Edge AI](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![초보자를 위한 MCP](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![초보자를 위한 AI 에이전트](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### 생성형 AI 시리즈
[![초보자를 위한 생성형 AI](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![생성형 AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![생성형 AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![생성형 AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### 핵심 학습
[![초보자를 위한 ML](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![초보자를 위한 데이터 과학](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![초보자를 위한 AI](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![초보자를 위한 사이버보안](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![초보자를 위한 웹 개발](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![초보자를 위한 IoT](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![초보자를 위한 XR 개발](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Copilot 시리즈
[![AI 페어 프로그래밍을 위한 Copilot](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![C#/.NET을 위한 Copilot](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot 어드벤처](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## 도움 받기

AI 앱 개발 중 막히거나 질문이 있으면 참여하세요:

[![Microsoft Foundry 디스코드](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

제품 피드백이나 빌드 중 오류가 있으면 방문하세요:

[![Microsoft Foundry 개발자 포럼](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
면책 조항:
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있으나 자동 번역에는 오류나 부정확성이 포함될 수 있음을 알려드립니다. 원문(원어) 문서를 권위 있는 출처로 간주하시기 바랍니다. 중요한 정보의 경우 전문 번역사의 번역을 권장합니다. 본 번역의 사용으로 인해 발생한 오해나 잘못된 해석에 대해서는 당사가 책임을 지지 않습니다.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
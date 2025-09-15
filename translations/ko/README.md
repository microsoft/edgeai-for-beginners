<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "56dfdb5231720282ba90359277270086",
  "translation_date": "2025-09-15T15:18:04+00:00",
  "source_file": "README.md",
  "language_code": "ko"
}
-->
# 초보자를 위한 EdgeAI

![코스 커버 이미지](../../translated_images/cover.eb18d1b9605d754b30973f4e17c6e11ea4f8473d9686ee378d6e7b44e3c70ac7.ko.png)

[![GitHub contributors](https://img.shields.io/github/contributors/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/graphs/contributors)  
[![GitHub issues](https://img.shields.io/github/issues/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/issues)  
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/pulls)  
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)  

[![GitHub watchers](https://img.shields.io/github/watchers/microsoft/edgeai-for-beginners.svg?style=social&label=Watch)](https://GitHub.com/microsoft/edgeai-for-beginners/watchers)  
[![GitHub forks](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork)  
[![GitHub stars](https://img.shields.io/github/stars/microsoft/edgeai-for-beginners?style=social&label=Star)](https://GitHub.com/microsoft/edgeai-for-beginners/stargazers)  

[![Microsoft Azure AI Foundry Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

다음 단계를 따라 이 리소스를 시작하세요:

1. **저장소 포크하기**: 클릭 [![GitHub forks](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork)  
2. **저장소 클론하기**: `git clone https://github.com/microsoft/edgeai-for-beginners.git`  
3. [**Azure AI Foundry Discord에 가입하여 전문가 및 다른 개발자들과 만나기**](https://discord.com/invite/ByRwuEEgH4)  

### 🌐 다국어 지원

#### GitHub Action을 통해 지원 (자동화 및 항상 최신 상태 유지)

[프랑스어](../fr/README.md) | [스페인어](../es/README.md) | [중국어 (간체)](../zh/README.md) | [중국어 (마카오 번체)](../mo/README.md) | [중국어 (홍콩 번체)](../hk/README.md) | [중국어 (대만 번체)](../tw/README.md) | [일본어](../ja/README.md) | [한국어](./README.md) |  
**추가 번역 언어를 원하시면 [여기](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md)에 나열된 지원 언어를 확인하세요.**

## 소개

초보자를 위한 EdgeAI에 오신 것을 환영합니다. 이 코스는 언어 모델의 강력함과 로컬 디바이스의 효율성을 결합합니다. 이 과정에서는 소형 최적화 언어 모델(SLM)이 클라우드 접근 없이 스마트폰, IoT 보드, 소형 서버와 같은 엣지 하드웨어에서 직접 실행되는 방법을 소개합니다. 실시간, 개인정보 보호 중심의 AI 추론이 스마트 홈, 산업 모니터링, 오프라인 애플리케이션을 혁신하는 방법을 탐구하며, 속도, 보안, 모듈성을 위해 설계된 경량 배포를 통해 이를 실현합니다.

### Edge AI

Edge AI는 클라우드 리소스에 의존하지 않고 데이터가 생성되는 가까운 하드웨어에서 AI 알고리즘과 언어 모델을 로컬로 실행하는 것을 의미합니다. 이는 지연 시간을 줄이고, 개인정보를 강화하며, 실시간 의사 결정을 가능하게 합니다.

### 핵심 원칙:
- 디바이스 내 추론: AI 모델이 엣지 디바이스(휴대폰, 라우터, 마이크로컨트롤러, 산업용 PC)에서 실행됩니다.
- 오프라인 기능: 지속적인 인터넷 없이 작동합니다.
- 낮은 지연 시간: 실시간 시스템에 적합한 즉각적인 응답.
- 데이터 주권: 민감한 데이터를 로컬에 유지하여 보안과 규정을 개선합니다.

**소형 언어 모델(SLMs)**  
Phi-4, Mistral-7B, Gemma와 같은 SLM은 더 큰 LLM을 훈련하거나 축소하여 최적화된 버전입니다:
- 메모리 사용량 감소
- 계산 요구량 감소
- 빠른 시작 시간

이들은 다음과 같은 제약 조건을 충족하면서 강력한 NLP 기능을 제공합니다:
- 임베디드 시스템
- 모바일 디바이스
- IoT 디바이스
- 제한된 GPU를 가진 엣지 서버
- 개인용 컴퓨터

## 코스 구조

### [모듈 01: EdgeAI 기본 및 변혁](./Module01/README.md)  
**주제**: 엣지 AI 배포의 변혁적 변화  

#### 챕터 구조:
- [**섹션 1: EdgeAI 기본**](./Module01/01.EdgeAIFundamentals.md)  
  - 전통적인 클라우드 AI와 엣지 AI 비교  
  - 엣지 컴퓨팅의 과제와 제약  
  - 주요 기술: 모델 양자화, 압축 최적화, 소형 언어 모델(SLMs)  
  - 하드웨어 가속: NPU, GPU 최적화, CPU 최적화  
  - 장점: 개인정보 보호, 낮은 지연 시간, 오프라인 기능, 비용 효율성  

- [**섹션 2: 실제 사례 연구**](./Module01/02.RealWorldCaseStudies.md)  
  - Microsoft Phi & Mu 모델 생태계  
  - 일본항공 AI 보고 시스템 사례 연구  
  - 시장 영향 및 미래 방향  
  - 배포 고려사항 및 모범 사례  

- [**섹션 3: 실용적 구현 가이드**](./Module01/03.PracticalImplementationGuide.md)  
  - 개발 환경 설정 (Python 3.10+, .NET 8+)  
  - 하드웨어 요구사항 및 권장 구성  
  - 핵심 모델 가족 리소스  
  - 양자화 및 최적화 도구 (Llama.cpp, Microsoft Olive, Apple MLX)  
  - 평가 및 검증 체크리스트  

- [**섹션 4: 엣지 AI 배포 하드웨어 플랫폼**](./Module01/04.EdgeDeployment.md)  
  - 엣지 AI 배포 고려사항 및 요구사항  
  - Intel 엣지 AI 하드웨어 및 최적화 기술  
  - 모바일 및 임베디드 시스템을 위한 Qualcomm AI 솔루션  
  - NVIDIA Jetson 및 엣지 컴퓨팅 플랫폼  
  - NPU 가속이 포함된 Windows AI PC 플랫폼  
  - 하드웨어별 최적화 전략  

---

### [모듈 02: 소형 언어 모델 기초](./Module02/README.md)  
**주제**: SLM 이론적 원칙, 구현 전략 및 생산 배포  

#### 챕터 구조:
- [**섹션 1: Microsoft Phi 모델 가족 기초**](./Module02/01.PhiFamily.md)  
  - 디자인 철학의 진화 (Phi-1에서 Phi-4까지)  
  - 효율성 중심의 아키텍처 디자인  
  - 특화된 기능 (추론, 멀티모달, 엣지 배포)  

- [**섹션 2: Qwen 가족 기초**](./Module02/02.QwenFamily.md)  
  - 오픈 소스 우수성 (Qwen 1.0에서 Qwen3까지) - Hugging Face에서 제공  
  - 사고 모드 기능을 갖춘 고급 추론 아키텍처  
  - 확장 가능한 배포 옵션 (0.5B-235B 매개변수)  

- [**섹션 3: Gemma 가족 기초**](./Module02/03.GemmaFamily.md)  
  - 연구 중심 혁신 (Gemma 3 & 3n)  
  - 멀티모달 우수성  
  - 모바일 중심 아키텍처  

- [**섹션 4: BitNET 가족 기초**](./Module02/04.BitNETFamily.md)  
  - 혁신적인 양자화 기술 (1.58-bit)  
  - https://github.com/microsoft/BitNet에서 제공되는 특화된 추론 프레임워크  
  - 극한의 효율성을 통한 지속 가능한 AI 리더십  

- [**섹션 5: Microsoft Mu 모델 기초**](./Module02/05.mumodel.md)  
  - Windows 11에 내장된 디바이스 중심 아키텍처  
  - Windows 11 설정과의 시스템 통합  
  - 개인정보 보호를 위한 오프라인 운영  

- [**섹션 6: Phi-Silica 기초**](./Module02/06.phisilica.md)  
  - Windows 11 Copilot+ PC에 내장된 NPU 최적화 아키텍처  
  - 뛰어난 효율성 (1.5W에서 초당 650 토큰)  
  - Windows App SDK와의 개발자 통합  

---

### [모듈 03: 소형 언어 모델 배포](./Module03/README.md)  
**주제**: 이론부터 생산 환경까지 SLM 전체 라이프사이클 배포  

#### 챕터 구조:
- [**섹션 1: SLM 고급 학습**](./Module03/01.SLMAdvancedLearning.md)  
  - 매개변수 분류 프레임워크 (Micro SLM 100M-1.4B, Medium SLM 14B-30B)  
  - 고급 최적화 기술 (양자화 방법, BitNET 1-bit 양자화)  
  - 모델 획득 전략 (Phi 모델은 Azure AI Foundry, 선택된 모델은 Hugging Face)  

- [**섹션 2: 로컬 환경 배포**](./Module03/02.DeployingSLMinLocalEnv.md)  
  - Ollama 범용 플랫폼 배포  
  - Microsoft Foundry 로컬 엔터프라이즈급 솔루션  
  - 프레임워크 비교 분석  

- [**섹션 3: 컨테이너화된 클라우드 배포**](./Module03/03.DeployingSLMinCloud.md)  
  - vLLM 고성능 추론 배포  
  - Ollama 컨테이너 오케스트레이션  
  - ONNX Runtime 엣지 최적화 구현  

---

### [모듈 04: 모델 형식 변환 및 양자화](./Module04/README.md)  
**주제**: 플랫폼 간 엣지 배포를 위한 완전한 모델 최적화 도구  

#### 챕터 구조:
- [**섹션 1: 모델 형식 변환 및 양자화 기초**](./Module04/01.Introduce.md)  
  - 정밀도 분류 프레임워크 (초저, 저, 중간 정밀도)  
  - GGUF 및 ONNX 형식의 장점과 사용 사례  
  - 운영 효율성을 위한 양자화 이점  
  - 성능 벤치마크 및 메모리 사용량 비교  

- [**섹션 2: Llama.cpp 구현 가이드**](./Module04/02.Llamacpp.md)  
  - 크로스 플랫폼 설치 (Windows, macOS, Linux)  
  - GGUF 형식 변환 및 양자화 수준 (Q2_K에서 Q8_0까지)  
  - 하드웨어 가속 (CUDA, Metal, OpenCL, Vulkan)  
  - Python 통합 및 REST API 배포  

- [**섹션 3: Microsoft Olive 최적화 스위트**](./Module04/03.MicrosoftOlive.md)  
  - 40개 이상의 내장 구성 요소를 활용한 하드웨어 인식 모델 최적화  
  - 동적 및 정적 양자화를 통한 자동 최적화  
  - Azure ML 워크플로와의 엔터프라이즈 통합  
  - 인기 모델 지원 (Llama, Phi, 선택된 Qwen 모델, Gemma)  

- [**섹션 4: Apple MLX 프레임워크 심층 분석**](./Module04/04.AppleMLX.md)  
  - Apple Silicon을 위한 통합 메모리 아키텍처  
  - LLaMA, Mistral, Phi-3, 선택된 Qwen 모델 지원  
  - LoRA 미세 조정 및 모델 맞춤화  
  - 4-bit/8-bit 양자화를 활용한 Hugging Face 통합  

---

### [모듈 05: SLMOps - 소형 언어 모델 운영](./Module05/README.md)  
**주제**: 증류부터 생산 배포까지 SLM 전체 라이프사이클 운영  

#### 챕터 구조:
- [**섹션 1: SLMOps 소개**](./Module05/01.IntroduceSLMOps.md)  
  - AI 운영에서의 SLMOps 패러다임 변화  
  - 비용 효율성과 개인정보 보호 중심 아키텍처  
  - 전략적 비즈니스 영향 및 경쟁 우위  
  - 실제 구현 과제와 해결책  

- [**섹션 2: 모델 증류 - 이론에서 실습까지**](./Module05/02.SLMOps-Distillation.md)  
  - 교사 모델에서 학생 모델로의 지식 전이  
  - 두 단계 증류 프로세스 구현  
  - Azure ML 증류 워크플로와 실용적 예제  
  - 85% 추론 시간 감소와 92% 정확도 유지  

- [**섹션 3: 미세 조정 - 특정 작업을 위한 모델 맞춤화**](./Module05/03.SLMOps-Finetuing.md)  
  - 매개변수 효율적 미세 조정 (PEFT) 기술  
  - LoRA 및 QLoRA 고급 방법  
  - Microsoft Olive 미세 조정 구현  
  - 다중 어댑터 훈련 및 하이퍼파라미터 최적화  

- [**섹션 4: 배포 - 생산 준비 구현**](./Module05/04.SLMOps.Deployment.md)  
  - 생산을 위한 모델 변환 및 양자화  
  - Foundry Local 배포 구성  
  - 성능 벤치마킹 및 품질 검증  
  - 75% 크기 감소와 생산 모니터링  

---

### [모듈 06: SLM 에이전트 시스템 - AI 에이전트 및 함수 호출](./Module06/README.md)  
**주제**: SLM 에이전트 시스템 구현, 기초부터 고급 함수 호출 및 모델 컨텍스트 프로토콜 통합  

#### 챕터 구조:
- [**섹션 1: AI 에이전트와 소형 언어 모델 기초**](./Module06/01.IntroduceAgent.md)  
  - 에이전트 분류 프레임워크 (반사형, 모델 기반, 목표 기반, 학습 에이전트)  
  - SLM 기초 및 최적화 전략 (GGUF, 양자화, 엣지 프레임워크)  
  - SLM vs LLM 트레이드오프 분석 (10-30× 비용 절감, 70-80% 작업 효과성)  
- Ollama, VLLM, Microsoft Edge 솔루션을 활용한 실질적인 배포

- [**섹션 2: 소형 언어 모델에서의 함수 호출**](./Module06/02.FunctionCalling.md)
  - 체계적인 워크플로우 구현 (의도 감지, JSON 출력, 외부 실행)
  - 플랫폼별 구현 (Phi-4-mini, 선택된 Qwen 모델, Microsoft Foundry Local)
  - 고급 예제 (다중 에이전트 협업, 동적 도구 선택)
  - 프로덕션 고려사항 (속도 제한, 감사 로그, 보안 조치)

- [**섹션 3: 모델 컨텍스트 프로토콜(MCP) 통합**](./Module06/03.IntroduceMCP.md)
  - 프로토콜 아키텍처 및 계층적 시스템 설계
  - 다중 백엔드 지원 (개발용 Ollama, 프로덕션용 vLLM)
  - 연결 프로토콜 (STDIO 및 SSE 모드)
  - 실제 응용 사례 (웹 자동화, 데이터 처리, API 통합)

---

### [모듈 07: EdgeAI 구현 샘플](./Module07/README.md)
**주제**: 다양한 플랫폼과 프레임워크를 활용한 포괄적인 EdgeAI 구현

#### 챕터 구성:
- [**NVIDIA Jetson Orin Nano에서의 EdgeAI**](./Module07/README.md#1-edgeai-in-nvidia-jetson-orin-nano)
  - 신용카드 크기 폼팩터에서 67 TOPS AI 성능
  - 생성형 AI 모델 지원 (비전 트랜스포머, LLM, 비전-언어 모델)
  - 로봇, 드론, 지능형 카메라, 자율 장치에서의 응용
  - AI 개발을 민주화하는 $249의 경제적인 플랫폼

- [**.NET MAUI와 ONNX Runtime GenAI를 활용한 모바일 애플리케이션에서의 EdgeAI**](./Module07/README.md#2-edgeai-in-mobile-applications-with-net-maui-and-onnx-runtime-genai)
  - 단일 C# 코드베이스를 활용한 크로스 플랫폼 모바일 AI
  - 하드웨어 가속 지원 (CPU, GPU, 모바일 AI 프로세서)
  - 플랫폼별 최적화 (iOS용 CoreML, Android용 NNAPI)
  - 완전한 생성형 AI 루프 구현

- [**소형 언어 모델 엔진을 활용한 Azure에서의 EdgeAI**](./Module07/README.md#3-edgeai-in-azure-with-small-language-models-engine)
  - 클라우드-엣지 하이브리드 배포 아키텍처
  - ONNX Runtime과 Azure AI 서비스 통합
  - 엔터프라이즈 규모 배포 및 지속적인 모델 관리
  - 지능형 문서 처리를 위한 하이브리드 AI 워크플로우

- [**Windows ML을 활용한 EdgeAI**](./Module07/README.md#4-edgeai-with-windows-ml)
  - 온디바이스 추론 성능을 위한 Windows AI Foundry 기반
  - 범용 하드웨어 지원 (AMD, Intel, NVIDIA, Qualcomm 실리콘)
  - 자동 하드웨어 추상화 및 최적화
  - 다양한 Windows 하드웨어 생태계를 위한 통합 프레임워크

- [**Foundry Local 애플리케이션을 활용한 EdgeAI**](./Module07/README.md#5-edgeai-with-foundry-local-applications)
  - 로컬 리소스를 활용한 프라이버시 중심 RAG 구현
  - Phi-3 언어 모델과 의미 검색 통합 (Phi 모델 전용)
  - 로컬 벡터 데이터베이스 지원 (SQLite, Qdrant)
  - 데이터 주권 및 오프라인 운영 기능

## 학습 결과 개요

### 모듈 01 학습 결과:
- 클라우드와 엣지 AI 아키텍처의 근본적인 차이를 이해
- 엣지 배포를 위한 핵심 최적화 기술 숙달
- 실제 응용 사례와 성공 사례 인식
- EdgeAI 솔루션 구현을 위한 실질적인 기술 습득

### 모듈 02 학습 결과:
- 다양한 SLM 설계 철학과 배포 영향에 대한 깊은 이해
- 계산 제약 및 성능 요구 사항에 기반한 전략적 의사결정 능력 숙달
- 배포 유연성의 트레이드오프 이해
- 효율적인 AI 아키텍처에 대한 미래 지향적 통찰력 보유

### 모듈 03 학습 결과:
- 전략적 모델 선택 능력
- 최적화 기술 숙달
- 배포 유연성 숙달
- 프로덕션 준비 구성 능력

### 모듈 04 학습 결과:
- 양자화 경계와 실제 응용에 대한 깊은 이해
- 다양한 최적화 프레임워크(Llama.cpp, Olive, MLX)를 활용한 실습 경험
- 하드웨어 인식 최적화 선택 능력
- 크로스 플랫폼 엣지 컴퓨팅 환경을 위한 프로덕션 배포 기술

### 모듈 05 학습 결과:
- SLMOps 패러다임과 운영 원칙 숙달
- 지식 전이 및 효율성 최적화를 위한 모델 증류 구현
- 도메인별 모델 맞춤화를 위한 파인 튜닝 기술 적용
- 모니터링 및 유지보수 전략을 포함한 프로덕션 준비 SLM 솔루션 배포

### 모듈 06 학습 결과:
- AI 에이전트와 소형 언어 모델 아키텍처의 기본 개념 이해
- 다양한 플랫폼과 프레임워크에서의 함수 호출 구현 숙달
- 외부 도구와의 표준화된 상호작용을 위한 모델 컨텍스트 프로토콜(MCP) 통합
- 최소한의 인간 개입 요구사항으로 복잡한 에이전트 시스템 구축

### 모듈 07 학습 결과:
- 다양한 EdgeAI 플랫폼과 구현 전략에 대한 실습 경험
- NVIDIA, 모바일, Azure, Windows 플랫폼 전반에 걸친 하드웨어별 최적화 기술 숙달
- 성능, 비용, 프라이버시 요구사항 간의 배포 트레이드오프 이해
- 다양한 생태계에서 실제 EdgeAI 애플리케이션을 구축하기 위한 실질적인 기술 개발

## 파일 구조 트리 다이어그램

```
edgeai-for-beginners/
├── imgs/
│   └── cover.png
├── Module01/ (EdgeAI Fundamentals and Transformation)
│   ├── 01.EdgeAIFundamentals.md
│   ├── 02.RealWorldCaseStudies.md
│   ├── 03.PracticalImplementationGuide.md
│   ├── 04.EdgeDeployment.md
│   └── README.md
├── Module02/ (Small Language Model Foundations)
│   ├── 01.PhiFamily.md
│   ├── 02.QwenFamily.md
│   ├── 03.GemmaFamily.md
│   ├── 04.BitNETFamily.md
│   ├── 05.mumodel.md
│   ├── 06.phisilica.md
│   └── README.md
├── Module03/ (SLM Deployment Practice)
│   ├── 01.SLMAdvancedLearning.md
│   ├── 02.DeployingSLMinLocalEnv.md
│   ├── 03.DeployingSLMinCloud.md
│   └── README.md
├── Module04/ (Model Format Conversion and Quantization)
│   ├── 01.Introduce.md
│   ├── 02.Llamacpp.md
│   ├── 03.MicrosoftOlive.md
│   ├── 04.AppleMLX.md
│   └── README.md
├── Module05/ (SLMOps - Small Language Model Operations)
│   ├── 01.IntroduceSLMOps.md
│   ├── 02.SLMOps-Distillation.md
│   ├── 03.SLMOps-Finetuing.md
│   ├── 04.SLMOps.Deployment.md
│   └── README.md
├── Module06/ (SLM Agentic Systems)
│   ├── 01.IntroduceAgent.md
│   ├── 02.FunctionCalling.md
│   ├── 03.IntroduceMCP.md
│   └── README.md
├── Module07/ (EdgeAI Implementation Samples)
│   └── README.md
├── CODE_OF_CONDUCT.md
├── LICENSE
├── README.md (This file)
├── SECURITY.md
├── STUDY_GUIDE.md
└── SUPPORT.md
```

## 코스 특징

- **점진적 학습**: 기본 개념에서 고급 배포까지 점진적으로 발전
- **이론과 실습 통합**: 각 모듈은 이론적 기초와 실질적 운영을 포함
- **실제 사례 연구**: Microsoft, Alibaba, Google 등의 실제 사례 기반
- **실습 경험**: 완전한 구성 파일, API 테스트 절차, 배포 스크립트 포함
- **성능 벤치마크**: 추론 속도, 메모리 사용량, 리소스 요구사항에 대한 상세 비교
- **엔터프라이즈급 고려사항**: 보안 관행, 준수 프레임워크, 데이터 보호 전략

## 시작하기

추천 학습 경로:
1. **모듈01**로 시작하여 EdgeAI의 기본 이해를 구축
2. **모듈02**로 진행하여 다양한 SLM 모델 패밀리를 깊이 이해
3. **모듈03**을 학습하여 실질적인 배포 기술 숙달
4. **모듈04**로 계속하여 고급 모델 최적화 및 형식 변환 학습
5. **모듈05**를 완료하여 프로덕션 준비 구현을 위한 SLMOps 숙달
6. **모듈06**을 탐구하여 SLM 에이전트 시스템 및 함수 호출 기능 이해
7. **모듈07**을 마무리하여 다양한 EdgeAI 구현 샘플에 대한 실질적인 경험 획득

각 모듈은 독립적으로 완결되도록 설계되었지만, 순차적 학습이 최상의 결과를 제공합니다.

## 학습 가이드

포괄적인 [학습 가이드](STUDY_GUIDE.md)가 제공되어 학습 경험을 극대화할 수 있도록 돕습니다. 학습 가이드는 다음을 제공합니다:

- **구조화된 학습 경로**: 20시간 내 코스를 완료하기 위한 최적화된 일정
- **시간 할당 지침**: 읽기, 연습, 프로젝트 간 균형을 맞추기 위한 구체적 추천
- **핵심 개념 집중**: 각 모듈의 우선 학습 목표
- **자기 평가 도구**: 이해도를 테스트하기 위한 질문 및 연습
- **미니 프로젝트 아이디어**: 학습을 강화하기 위한 실질적 응용

학습 가이드는 집중 학습(1주)과 파트타임 학습(3주)을 모두 수용하도록 설계되었으며, 코스에 10시간만 할애할 수 있는 경우에도 효과적으로 시간을 배분할 수 있는 명확한 지침을 제공합니다.

---

**EdgeAI의 미래는 모델 아키텍처, 양자화 기술, 배포 전략의 지속적인 개선에 달려 있습니다. 효율성과 전문화를 일반 목적 능력보다 우선시하는 패러다임 전환을 수용하는 조직은 데이터와 운영을 통제하면서 AI의 변혁적 잠재력을 활용할 수 있는 좋은 위치에 있게 될 것입니다.**

## 기타 코스

우리 팀은 다른 코스도 제작합니다! 확인해보세요:

- [MCP 초보자용](https://github.com/microsoft/mcp-for-beginners)
- [AI 에이전트 초보자용](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)
- [.NET을 활용한 생성형 AI 초보자용](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
- [JavaScript를 활용한 생성형 AI 초보자용](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)
- [생성형 AI 초보자용](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
- [ML 초보자용](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
- [데이터 과학 초보자용](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
- [AI 초보자용](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
- [사이버 보안 초보자용](https://github.com/microsoft/Security-101??WT.mc_id=academic-96948-sayoung)
- [웹 개발 초보자용](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
- [IoT 초보자용](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
- [XR 개발 초보자용](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)
- [AI 페어드 프로그래밍을 위한 GitHub Copilot 마스터하기](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
- [C#/.NET 개발자를 위한 GitHub Copilot 마스터하기](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
- [자신만의 Copilot 모험 선택하기](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)

---

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있으나, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원본 문서의 원어 버전을 신뢰할 수 있는 권위 있는 자료로 간주해야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 책임을 지지 않습니다.
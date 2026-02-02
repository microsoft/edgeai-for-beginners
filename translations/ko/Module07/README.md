# Chapter 07 : EdgeAI 샘플

Edge AI는 인공지능과 엣지 컴퓨팅의 융합을 통해 클라우드 연결 없이도 디바이스에서 직접 지능형 처리를 가능하게 합니다. 이 장에서는 다양한 플랫폼과 프레임워크를 활용한 다섯 가지 독창적인 EdgeAI 구현 사례를 탐구하며, 엣지에서 AI 모델을 실행하는 데 있어 그 다양성과 강력함을 보여줍니다.

## 1. NVIDIA Jetson Orin Nano에서의 EdgeAI

NVIDIA Jetson Orin Nano는 엣지 AI 컴퓨팅의 새로운 돌파구를 제공하며, 신용카드 크기의 컴팩트한 형태로 최대 67 TOPS의 AI 성능을 제공합니다. 이 강력한 엣지 AI 플랫폼은 취미 개발자, 학생, 전문 개발자 모두를 위한 생성형 AI 개발을 민주화합니다.

### 주요 특징
- 최대 67 TOPS의 AI 성능 제공 - 이전 모델 대비 1.7배 향상
- 1024 CUDA 코어와 최대 32 Tensor 코어를 활용한 AI 처리
- 최대 주파수 1.5GHz의 6코어 Arm Cortex-A78AE v8.2 64비트 CPU
- 단 $249의 가격으로 개발자, 학생, 제작자에게 가장 저렴하고 접근 가능한 플랫폼 제공

### 응용 분야
Jetson Orin Nano는 비전 트랜스포머, 대형 언어 모델, 비전-언어 모델을 포함한 최신 생성형 AI 모델 실행에 탁월합니다. 특히 GenAI 사용 사례에 최적화되어 있으며, 이제 손바닥 크기의 디바이스에서 여러 LLM을 실행할 수 있습니다. 주요 사용 사례로는 AI 기반 로봇, 스마트 드론, 지능형 카메라, 자율 엣지 디바이스 등이 있습니다.

**자세히 알아보기**: [NVIDIA의 Jetson Orin Nano 슈퍼컴퓨터: EdgeAI의 다음 혁신](https://medium.com/data-science-in-your-pocket/nvidias-jetson-orin-nano-supercomputer-the-next-big-thing-in-edgeai-e9eff687ae62)

## 2. .NET MAUI와 ONNX Runtime GenAI를 활용한 모바일 애플리케이션에서의 EdgeAI

이 솔루션은 .NET MAUI(멀티 플랫폼 앱 UI)와 ONNX Runtime GenAI를 사용하여 생성형 AI와 대형 언어 모델(LLM)을 크로스 플랫폼 모바일 애플리케이션에 통합하는 방법을 보여줍니다. 이를 통해 .NET 개발자는 Android 및 iOS 디바이스에서 네이티브로 실행되는 정교한 AI 기반 모바일 애플리케이션을 구축할 수 있습니다.

### 주요 특징
- Android 및 iOS 애플리케이션을 위한 단일 코드베이스를 제공하는 .NET MAUI 프레임워크 기반
- ONNX Runtime GenAI 통합으로 모바일 디바이스에서 생성형 AI 모델 실행 가능
- CPU, GPU 및 모바일 AI 프로세서와 같은 다양한 하드웨어 가속기 지원
- ONNX Runtime을 통해 iOS의 CoreML 및 Android의 NNAPI와 같은 플랫폼별 최적화 지원
- 생성형 AI 루프 전체 구현: 전처리 및 후처리, 추론, 로짓 처리, 검색 및 샘플링, KV 캐시 관리 포함

### 개발 혜택
.NET MAUI 접근법은 개발자가 기존의 C# 및 .NET 기술을 활용하여 크로스 플랫폼 AI 애플리케이션을 구축할 수 있도록 합니다. ONNX Runtime GenAI 프레임워크는 Llama, Mistral, Phi, Gemma 등 다양한 모델 아키텍처를 지원합니다. ARM64 커널 최적화로 INT4 양자화 행렬 곱셈을 가속화하여 모바일 하드웨어에서 효율적인 성능을 제공하며, 익숙한 .NET 개발 경험을 유지합니다.

### 사용 사례
이 솔루션은 .NET 기술을 사용하여 AI 기반 모바일 애플리케이션을 구축하려는 개발자에게 적합합니다. 지능형 챗봇, 이미지 인식 앱, 언어 번역 도구, 개인화된 추천 시스템 등 디바이스에서 완전히 실행되어 프라이버시를 강화하고 오프라인 기능을 제공하는 애플리케이션에 적합합니다.

**자세히 알아보기**: [.NET MAUI ONNX Runtime GenAI 예제](https://github.com/microsoft/onnxruntime-genai/tree/jialli/genny-maui/examples/csharp/GennyMaui)

## 3. Azure에서의 EdgeAI와 Small Language Models Engine

Microsoft의 Azure 기반 EdgeAI 솔루션은 Small Language Models(SLM)을 클라우드-엣지 하이브리드 환경에서 효율적으로 배포하는 데 초점을 맞추고 있습니다. 이 접근법은 클라우드 규모의 AI 서비스와 엣지 배포 요구 사항 간의 격차를 연결합니다.

### 아키텍처 장점
- Azure AI 서비스와의 원활한 통합
- ONNX Runtime을 통해 디바이스와 클라우드에서 SLM/LLM 및 멀티모달 모델 실행
- 엔터프라이즈 규모 배포에 최적화
- 지속적인 모델 업데이트 및 관리 지원

### 사용 사례
Azure EdgeAI 구현은 클라우드 관리 기능을 갖춘 엔터프라이즈급 AI 배포가 필요한 시나리오에서 뛰어납니다. 여기에는 지능형 문서 처리, 실시간 분석, 클라우드와 엣지 컴퓨팅 리소스를 모두 활용하는 하이브리드 AI 워크플로우가 포함됩니다.

**자세히 알아보기**: [Azure EdgeAI SLM Engine](https://github.com/microsoft/onnxruntime-genai/tree/main/examples/slm_engine)

## [4. Windows ML을 활용한 EdgeAI](./windowdeveloper.md)

Windows ML은 Microsoft의 최신 런타임으로, 디바이스에서 모델 추론을 최적화하고 배포를 간소화하며 Windows AI Foundry의 기반을 제공합니다. 이 플랫폼은 PC 하드웨어의 전체 스펙트럼을 활용하는 AI 기반 Windows 애플리케이션을 개발할 수 있도록 합니다.

### 플랫폼 기능
- Windows 11 버전 24H2(빌드 26100) 이상을 실행하는 모든 PC에서 작동
- NPU나 GPU가 없는 PC를 포함한 모든 x64 및 ARM64 PC 하드웨어에서 작동
- 개발자가 자신의 모델을 가져와 AMD, Intel, NVIDIA, Qualcomm 등 CPU, GPU, NPU를 포함한 실리콘 파트너 생태계 전반에 효율적으로 배포 가능
- 인프라 API를 활용하여 개발자가 다양한 실리콘을 대상으로 여러 앱 빌드를 생성할 필요 없음

### 개발자 혜택
Windows ML은 하드웨어와 실행 제공자를 추상화하여 코드 작성에 집중할 수 있도록 합니다. 또한 Windows ML은 새로운 NPU, GPU, CPU가 출시될 때마다 자동으로 업데이트됩니다. 이 플랫폼은 다양한 Windows 하드웨어 생태계에서 AI 개발을 위한 통합 프레임워크를 제공합니다.

**자세히 알아보기**: 
- [Windows ML 개요](https://learn.microsoft.com/en-us/windows/ai/new-windows-ml/overview)
- [Windows EdgeAI 개발 가이드](./windowdeveloper.md) - Windows Edge AI 개발을 위한 종합 가이드

## [5. Foundry Local 애플리케이션을 활용한 EdgeAI](./foundrylocal.md)

Foundry Local은 Windows 및 Mac 개발자가 .NET을 사용하여 Retrieval Augmented Generation(RAG) 애플리케이션을 로컬 리소스를 활용해 구축할 수 있도록 합니다. 이 접근법은 로컬 언어 모델과 의미 검색 기능을 결합하여 프라이버시 중심의 AI 솔루션을 제공합니다.

### 기술 아키텍처
- Phi 언어 모델, 로컬 임베딩, Semantic Kernel을 결합하여 RAG 시나리오 생성
- 콘텐츠와 그 의미를 나타내는 벡터(배열)로 임베딩 사용
- Semantic Kernel이 Phi와 Smart Components를 통합하여 원활한 RAG 파이프라인 생성
- SQLite 및 Qdrant을 포함한 로컬 벡터 데이터베이스 지원

### 구현 혜택
RAG는 "정보를 검색하여 프롬프트에 넣는 것"을 의미하는 간단한 방식입니다. 이 로컬 구현은 데이터 프라이버시를 보장하면서 사용자 정의 지식 기반에 근거한 지능형 응답을 제공합니다. 이 접근법은 데이터 주권과 오프라인 운영 기능이 필요한 엔터프라이즈 시나리오에 특히 유용합니다.

**자세히 알아보기**: 
- [Foundry Local](./foundrylocal.md)
- [Foundry Local RAG 샘플](https://github.com/microsoft/Foundry-Local/tree/main/samples/dotNET/rag)

### Windows Foundry Local

Microsoft Foundry Local은 ONNX Runtime으로 구동되는 OpenAI 호환 REST 서버를 제공하여 Windows에서 로컬로 모델을 실행할 수 있습니다. 아래는 간단한 요약이며, 자세한 내용은 공식 문서를 참조하세요.

- 시작하기: https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started
- 아키텍처: https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture
- CLI 참조: https://learn.microsoft.com/azure/ai-foundry/foundry-local/reference/reference-cli
- 이 저장소의 전체 Windows 가이드: [foundrylocal.md](./foundrylocal.md)

Windows에서 설치 또는 업그레이드(cmd.exe):
```cmd
winget install Microsoft.FoundryLocal
winget upgrade --id Microsoft.FoundryLocal
foundry --version
```

CLI 카테고리 탐색:
```cmd
foundry model --help
foundry service --help
foundry cache --help
```

모델 실행 및 동적 엔드포인트 발견:
```cmd
foundry model run gpt-oss-20b
foundry service status
```

REST를 사용하여 모델 목록 확인(상태에서 PORT 교체):
```cmd
curl -s http://localhost:PORT/v1/models
```

팁:
- SDK 통합: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks
- 사용자 모델 가져오기(컴파일): https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models

## Windows EdgeAI 개발 리소스

Windows 플랫폼을 대상으로 하는 개발자를 위해 Windows EdgeAI 생태계를 완전히 다루는 종합 가이드를 제작했습니다. 이 리소스는 Windows AI Foundry에 대한 자세한 정보, API, 도구 및 Windows에서의 EdgeAI 개발을 위한 모범 사례를 제공합니다.

### Windows AI Foundry 플랫폼
Windows AI Foundry 플랫폼은 Windows 디바이스에서 Edge AI 개발을 위해 특별히 설계된 도구와 API를 포괄적으로 제공합니다. 여기에는 NPU 가속 하드웨어 지원, Windows ML 통합, 플랫폼별 최적화 기술이 포함됩니다.

**종합 가이드**: [Windows EdgeAI 개발 가이드](../windowdeveloper.md)

이 가이드에는 다음 내용이 포함됩니다:
- Windows AI Foundry 플랫폼 개요 및 구성 요소
- NPU 하드웨어에서 효율적인 추론을 위한 Phi Silica API
- 이미지 처리 및 OCR을 위한 컴퓨터 비전 API
- Windows ML 런타임 통합 및 최적화
- 로컬 개발 및 테스트를 위한 Foundry Local CLI
- Windows 디바이스를 위한 하드웨어 최적화 전략
- 실용적인 구현 예제 및 모범 사례

### [Edge AI 개발을 위한 AI Toolkit](./aitoolkit.md)
Visual Studio Code를 사용하는 개발자를 위해 AI Toolkit 확장은 Edge AI 애플리케이션을 구축, 테스트 및 배포하기 위한 종합적인 개발 환경을 제공합니다. 이 툴킷은 VS Code 내에서 전체 Edge AI 개발 워크플로우를 간소화합니다.

**개발 가이드**: [Edge AI 개발을 위한 AI Toolkit](./aitoolkit.md)

AI Toolkit 가이드에는 다음 내용이 포함됩니다:
- 엣지 배포를 위한 모델 검색 및 선택
- 로컬 테스트 및 최적화 워크플로우
- 엣지 모델을 위한 ONNX 및 Ollama 통합
- 모델 변환 및 양자화 기술
- 엣지 시나리오를 위한 에이전트 개발
- 성능 평가 및 모니터링
- 배포 준비 및 모범 사례

## 결론

이 다섯 가지 EdgeAI 구현 사례는 오늘날 이용 가능한 엣지 AI 솔루션의 성숙도와 다양성을 보여줍니다. Jetson Orin Nano와 같은 하드웨어 가속 엣지 디바이스에서 ONNX Runtime GenAI 및 Windows ML과 같은 소프트웨어 프레임워크에 이르기까지, 개발자는 엣지에서 지능형 애플리케이션을 배포할 수 있는 전례 없는 옵션을 갖게 되었습니다.

이 플랫폼들 간의 공통점은 AI 기능의 민주화로, 다양한 기술 수준과 사용 사례를 가진 개발자들이 정교한 머신러닝을 활용할 수 있도록 한다는 점입니다. 모바일 애플리케이션, 데스크톱 소프트웨어, 임베디드 시스템을 구축하든, 이러한 EdgeAI 솔루션은 엣지에서 효율적이고 프라이버시를 보장하는 차세대 지능형 애플리케이션을 위한 기반을 제공합니다.

각 플랫폼은 고유한 장점을 제공합니다: Jetson Orin Nano는 하드웨어 가속 엣지 컴퓨팅에, ONNX Runtime GenAI는 크로스 플랫폼 모바일 개발에, Azure EdgeAI는 엔터프라이즈 클라우드-엣지 통합에, Windows ML은 Windows 네이티브 애플리케이션에, Foundry Local은 프라이버시 중심의 RAG 구현에 적합합니다. 이들은 함께 EdgeAI 개발을 위한 포괄적인 생태계를 대표합니다.

[다음 AI Toolkit](aitoolkit.md)

---

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있으나, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원본 문서의 원어 버전을 권위 있는 자료로 간주해야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.
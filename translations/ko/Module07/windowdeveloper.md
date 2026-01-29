# Windows Edge AI 개발 가이드

## 소개

Windows Edge AI 개발에 오신 것을 환영합니다. 이 가이드는 Microsoft의 Windows AI Foundry 플랫폼을 활용하여 디바이스 내 AI의 강력한 기능을 활용하는 지능형 애플리케이션을 구축하는 데 필요한 모든 것을 제공합니다. Windows 개발자를 위해 설계된 이 가이드는 최첨단 Edge AI 기능을 애플리케이션에 통합하면서 Windows 하드웨어 가속의 전체 스펙트럼을 활용하는 방법을 안내합니다.

### Windows AI의 장점

Windows AI Foundry는 모델 선택과 세부 조정에서부터 최적화 및 CPU, GPU, NPU, 하이브리드 클라우드 아키텍처에 걸친 배포까지 AI 개발자 라이프사이클 전체를 지원하는 통합적이고 신뢰할 수 있으며 안전한 플랫폼을 제공합니다. 이 플랫폼은 다음을 통해 AI 개발을 민주화합니다:

- **하드웨어 추상화**: AMD, Intel, NVIDIA, Qualcomm 실리콘 전반에 걸친 원활한 배포
- **디바이스 내 지능**: 로컬 하드웨어에서 완전히 실행되는 프라이버시 보호 AI
- **최적화된 성능**: Windows 하드웨어 구성에 최적화된 모델
- **엔터프라이즈 준비**: 생산 등급의 보안 및 규정 준수 기능

### Windows ML
Windows Machine Learning (ML)은 C#, C++, Python 개발자가 ONNX Runtime을 통해 Windows PC에서 ONNX AI 모델을 로컬로 실행할 수 있도록 하며, 다양한 하드웨어(CPU, GPU, NPU)에 대한 자동 실행 제공자 관리를 제공합니다. [ONNX Runtime](https://onnxruntime.ai/docs/)은 PyTorch, Tensorflow/Keras, TFLite, scikit-learn 및 기타 프레임워크의 모델과 함께 사용할 수 있습니다.

![WindowsML ONNX 모델이 Windows ML을 통해 NPU, GPU, CPU에 도달하는 과정을 보여주는 다이어그램](https://learn.microsoft.com/en-us/windows/ai/images/winml-diagram.png)

Windows ML은 Windows 전체에서 공유되는 ONNX Runtime 복사본과 실행 제공자(EP)를 동적으로 다운로드할 수 있는 기능을 제공합니다.

### Edge AI를 위한 Windows 선택 이유

**범용 하드웨어 지원**
Windows ML은 Windows 생태계 전체에서 자동 하드웨어 최적화를 제공하여 기본 실리콘 아키텍처에 관계없이 AI 애플리케이션이 최적의 성능을 발휘하도록 보장합니다.

**통합 AI 런타임**
내장된 Windows ML 추론 엔진은 복잡한 설정 요구 사항을 제거하여 개발자가 인프라 문제 대신 애플리케이션 로직에 집중할 수 있도록 합니다.

**Copilot+ PC 최적화**
전용 신경 처리 장치(NPU)를 갖춘 차세대 Windows 디바이스를 위해 특별히 설계된 API는 뛰어난 성능과 전력 효율을 제공합니다.

**개발자 생태계**
Visual Studio 통합, 포괄적인 문서, 샘플 애플리케이션 등 풍부한 도구를 통해 개발 주기를 가속화합니다.

## 학습 목표

이 Windows Edge AI 개발 가이드를 완료하면 Windows 플랫폼에서 생산 준비된 AI 애플리케이션을 구축하는 데 필요한 핵심 기술을 습득하게 됩니다.

### 핵심 기술 역량

**Windows AI Foundry 숙련**
- Windows AI Foundry 플랫폼의 아키텍처와 구성 요소 이해
- Windows 생태계 내에서 AI 개발 라이프사이클 탐색
- 디바이스 내 AI 애플리케이션을 위한 보안 모범 사례 구현
- 다양한 Windows 하드웨어 구성에 대한 애플리케이션 최적화

**API 통합 전문성**
- 텍스트, 비전, 멀티모달 애플리케이션을 위한 Windows AI API 숙달
- Phi Silica 언어 모델 통합을 통한 텍스트 생성 및 추론 구현
- 내장 이미지 처리 API를 사용한 컴퓨터 비전 기능 배포
- LoRA(저순위 적응) 기술을 사용하여 사전 학습된 모델 맞춤화

**Foundry Local 구현**
- Foundry Local CLI를 사용하여 오픈소스 언어 모델 탐색, 평가 및 배포
- 로컬 배포를 위한 모델 최적화 및 양자화 이해
- 인터넷 연결 없이 작동하는 오프라인 AI 기능 구현
- 프로덕션 환경에서 모델 라이프사이클 및 업데이트 관리

**Windows ML 배포**
- Windows ML을 사용하여 Windows 애플리케이션에 맞춤형 ONNX 모델 도입
- CPU, GPU, NPU 아키텍처 전반에 걸친 자동 하드웨어 가속 활용
- 최적의 리소스 활용을 통한 실시간 추론 구현
- 다양한 Windows 디바이스 카테고리를 위한 확장 가능한 AI 애플리케이션 설계

### 애플리케이션 개발 기술

**크로스 플랫폼 Windows 개발**
- .NET MAUI를 사용하여 범용 Windows 배포를 위한 AI 기반 애플리케이션 구축
- Win32, UWP, 프로그레시브 웹 애플리케이션에 AI 기능 통합
- AI 처리 상태에 적응하는 반응형 UI 디자인 구현
- 적절한 사용자 경험 패턴을 사용하여 비동기 AI 작업 처리

**성능 최적화**
- 다양한 하드웨어 구성에서 AI 추론 성능 프로파일링 및 최적화
- 대형 언어 모델을 위한 효율적인 메모리 관리 구현
- 사용 가능한 하드웨어 기능에 따라 우아하게 성능을 저하시키는 애플리케이션 설계
- 자주 사용하는 AI 작업에 대한 캐싱 전략 적용

**프로덕션 준비**
- 포괄적인 오류 처리 및 대체 메커니즘 구현
- AI 애플리케이션 성능을 위한 텔레메트리 및 모니터링 설계
- 로컬 AI 모델 저장 및 실행을 위한 보안 모범 사례 적용
- 엔터프라이즈 및 소비자 애플리케이션을 위한 배포 전략 계획

### 비즈니스 및 전략적 이해

**AI 애플리케이션 아키텍처**
- 로컬 및 클라우드 AI 처리를 최적화하는 하이브리드 아키텍처 설계
- 모델 크기, 정확도, 추론 속도 간의 트레이드오프 평가
- 프라이버시를 유지하면서 지능을 가능하게 하는 데이터 흐름 아키텍처 계획
- 사용자 요구에 따라 확장 가능한 비용 효율적인 AI 솔루션 구현

**시장 포지셔닝**
- Windows 네이티브 AI 애플리케이션의 경쟁 우위 이해
- 디바이스 내 AI가 우수한 사용자 경험을 제공하는 사용 사례 식별
- AI 강화 Windows 애플리케이션을 위한 시장 진입 전략 개발
- Windows 생태계의 이점을 활용할 수 있도록 애플리케이션 포지셔닝

## Windows App SDK AI 샘플

Windows App SDK는 여러 프레임워크 및 배포 시나리오에 걸친 AI 통합을 보여주는 포괄적인 샘플을 제공합니다. 이러한 샘플은 Windows AI 개발 패턴을 이해하는 데 필수적인 참고 자료입니다.

### Windows AI Foundry 샘플

| 샘플 | 프레임워크 | 초점 영역 | 주요 기능 |
|--------|-----------|------------|-------------|
| [cs-winui](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsAIFoundry/cs-winui) | C# WinUI 3 | Windows AI API 통합 | Windows AI API, ARM64 최적화, 패키지 배포를 보여주는 완전한 WinUI 앱 |

**주요 기술:**
- Windows AI API
- WinUI 3 프레임워크
- ARM64 플랫폼 최적화
- Copilot+ PC 호환성
- 패키지 앱 배포

**필수 조건:**
- Copilot+ PC가 권장되는 Windows 11
- Visual Studio 2022
- ARM64 빌드 구성
- Windows App SDK 1.8.1+

### Windows ML 샘플

#### C++ 샘플

| 샘플 | 유형 | 초점 영역 | 주요 기능 |
|--------|------|------------|-------------|
| [CppConsoleDesktop](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | 콘솔 앱 | 기본 Windows ML | EP 검색, 명령줄 옵션, 모델 컴파일 |
| [CppConsoleDesktop.FrameworkDependent](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | 콘솔 앱 | 프레임워크 배포 | 공유 런타임, 작은 배포 크기 |
| [CppConsoleDesktop.SelfContained](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | 콘솔 앱 | 독립형 배포 | 독립형 배포, 런타임 종속성 없음 |
| [CppConsoleDll](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | DLL | 라이브러리 사용 | 공유 라이브러리에서 WindowsML 사용, 메모리 관리 |
| [CppResnetBuildDemo](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | 데모 | ResNet 튜토리얼 | 모델 변환, EP 컴파일, Build 2025 튜토리얼 |

#### C# 샘플

**콘솔 애플리케이션**

| 샘플 | 유형 | 초점 영역 | 주요 기능 |
|--------|------|------------|-------------|
| [CSharpConsoleDesktop](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs) | 콘솔 앱 | 기본 C# 통합 | 공유 헬퍼 사용, 명령줄 인터페이스 |
| [ResnetBuildDemoCS](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs) | 데모 | ResNet 튜토리얼 | 모델 변환, EP 컴파일, Build 2025 튜토리얼 |

**GUI 애플리케이션**

| 샘플 | 프레임워크 | 초점 영역 | 주요 기능 |
|--------|-----------|------------|-------------|
| [cs-wpf](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs-wpf) | WPF | 데스크톱 GUI | WPF 인터페이스를 사용한 이미지 분류 |
| [cs-winforms](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs-winforms) | Windows Forms | 전통적인 GUI | Windows Forms를 사용한 이미지 분류 |
| [cs-winui](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs-winui) | WinUI 3 | 현대적인 GUI | WinUI 3 인터페이스를 사용한 이미지 분류 |

#### Python 샘플

| 샘플 | 언어 | 초점 영역 | 주요 기능 |
|--------|----------|------------|-------------|
| [SqueezeNetPython](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/python) | Python | 이미지 분류 | WinML Python 바인딩, 배치 이미지 처리 |

### 샘플 필수 조건

**시스템 요구 사항:**
- Windows 11 PC, 버전 24H2(빌드 26100) 이상 실행
- C++ 및 .NET 워크로드가 포함된 Visual Studio 2022
- Windows App SDK 1.8.1 이상
- x64 및 ARM64 디바이스에서 Python 샘플을 위한 Python 3.10-3.13

**Windows AI Foundry 관련:**
- 최적의 성능을 위한 Copilot+ PC 권장
- Windows AI 샘플을 위한 ARM64 빌드 구성
- 패키지 ID 필요(패키지화되지 않은 앱은 더 이상 지원되지 않음)

### 공통 샘플 워크플로

대부분의 Windows ML 샘플은 다음 표준 패턴을 따릅니다:

1. **환경 초기화** - ONNX Runtime 환경 생성
2. **실행 제공자 등록** - 사용 가능한 하드웨어 가속기(CPU, GPU, NPU) 검색 및 등록
3. **모델 로드** - ONNX 모델 로드, 선택적으로 대상 하드웨어에 대해 컴파일
4. **입력 전처리** - 이미지/데이터를 모델 입력 형식으로 변환
5. **추론 실행** - 모델 실행 및 예측 얻기
6. **결과 처리** - 소프트맥스 적용 및 상위 예측 표시

### 사용된 모델 파일

| 모델 | 목적 | 포함 여부 | 비고 |
|-------|---------|----------|-------|
| SqueezeNet | 경량 이미지 분류 | ✅ 포함됨 | 사전 학습, 바로 사용 가능 |
| ResNet-50 | 높은 정확도의 이미지 분류 | ❌ 변환 필요 | 변환을 위해 [AI Toolkit](https://code.visualstudio.com/docs/intelligentapps/modelconversion) 사용 |

### 하드웨어 지원

모든 샘플은 사용 가능한 하드웨어를 자동으로 감지하고 활용합니다:
- **CPU** - 모든 Windows 디바이스에서 범용 지원
- **GPU** - 사용 가능한 그래픽 하드웨어에 대한 자동 감지 및 최적화
- **NPU** - 지원되는 디바이스(Copilot+ PC)에서 신경 처리 장치 활용

## Windows AI Foundry 플랫폼 구성 요소

### 1. Windows AI API

Windows AI API는 최소한의 설정으로 Copilot+ PC 디바이스에서 효율성과 성능에 최적화된 디바이스 내 모델을 통해 바로 사용할 수 있는 AI 기능을 제공합니다.

#### 핵심 API 카테고리

**Phi Silica 언어 모델**
- 텍스트 생성 및 추론을 위한 작지만 강력한 언어 모델
- 최소 전력 소비로 실시간 추론에 최적화
- LoRA 기술을 사용한 맞춤형 세부 조정 지원
- Windows 의미 검색 및 지식 검색과 통합

**컴퓨터 비전 API**
- **텍스트 인식(OCR)**: 이미지에서 텍스트를 높은 정확도로 추출
- **이미지 초해상도**: 로컬 AI 모델을 사용하여 이미지 업스케일링
- **이미지 분할**: 이미지에서 특정 객체 식별 및 분리
- **이미지 설명**: 시각적 콘텐츠에 대한 상세 텍스트 설명 생성
- **객체 제거**: AI 기반 인페인팅으로 이미지에서 불필요한 객체 제거

**멀티모달 기능**
- **비전-언어 통합**: 텍스트와 이미지 이해 결합
- **의미 검색**: 멀티미디어 콘텐츠에 대한 자연어 쿼리 활성화
- **지식 검색**: 로컬 데이터를 사용하여 지능형 검색 경험 구축

### 2. Foundry Local

Foundry Local은 Windows Silicon에서 로컬 애플리케이션에 모델을 탐색, 테스트, 상호작용 및 배포할 수 있는 준비된 오픈소스 언어 모델에 빠르게 액세스할 수 있도록 합니다.

#### Foundry Local 샘플 애플리케이션

[Foundry Local 리포지토리](https://github.com/microsoft/Foundry-Local/tree/main/samples)는 다양한 프로그래밍 언어 및 프레임워크에 걸친 포괄적인 샘플을 제공하며, 다양한 통합 패턴 및 사용 사례를 보여줍니다.

| 샘플 | 언어/프레임워크 | 초점 영역 | 주요 기능 |
|--------|-------------------|------------|-------------|
| [dotNET/rag](https://github.com/microsoft/Foundry-Local/tree/main/samples/dotNET/rag) | C# / .NET | RAG 구현 | Semantic Kernel 통합, Qdrant 벡터 저장소, JINA 임베딩, 문서 수집, 스트리밍 채팅 |
| [electron/foundry-chat](https://github.com/microsoft/Foundry-Local/tree/main/samples/electron/foundry-chat) | JavaScript / Electron | 데스크톱 채팅 앱 | 크로스 플랫폼 채팅, 로컬/클라우드 모델 전환, OpenAI SDK 통합, 실시간 스트리밍 |
| [js/hello-foundry-local](https://github.com/microsoft/Foundry-Local/tree/main/samples/js/hello-foundry-local) | JavaScript / Node.js | 기본 통합 | 간단한 SDK 사용, 모델 초기화, 기본 채팅 기능 |
| [python/hello-foundry-local](https://github.com/microsoft/Foundry-Local/tree/main/samples/python/hello-foundry-local) | Python | 기본 통합 | Python SDK 사용, 스트리밍 응답, OpenAI 호환 API |
| [rust/hello-foundry-local](https://github.com/microsoft/Foundry-Local/tree/main/samples/rust/hello-foundry-local) | Rust | 시스템 통합 | 저수준 SDK 사용, 비동기 작업, reqwest HTTP 클라이언트 |

#### 사용 사례별 샘플 카테고리

**RAG (Retrieval-Augmented Generation)**
- **dotNET/rag**: Semantic Kernel, Qdrant 벡터 데이터베이스, JINA 임베딩을 활용한 완전한 RAG 구현
- **아키텍처**: 문서 수집 → 텍스트 분할 → 벡터 임베딩 → 유사성 검색 → 컨텍스트 기반 응답
- **기술**: Microsoft.SemanticKernel, Qdrant.Client, BERT ONNX 임베딩, 스트리밍 채팅 완료

**데스크톱 애플리케이션**
- **electron/foundry-chat**: 로컬/클라우드 모델 전환 기능을 갖춘 프로덕션 준비 채팅 애플리케이션
- **기능**: 모델 선택기, 스트리밍 응답, 오류 처리, 크로스 플랫폼 배포
- **아키텍처**: Electron 메인 프로세스, IPC 통신, 안전한 프리로드 스크립트

**SDK 통합 예제**
- **JavaScript (Node.js)**: 기본 모델 상호작용 및 스트리밍 응답
- **Python**: 비동기 스트리밍을 지원하는 OpenAI 호환 API 사용
- **Rust**: reqwest와 tokio를 활용한 저수준 비동기 작업 통합

#### Foundry Local 샘플을 위한 사전 요구사항

**시스템 요구사항:**
- Foundry Local이 설치된 Windows 11
- JavaScript/Electron 샘플용 Node.js v16+
- C# 샘플용 .NET 8.0+
- Python 샘플용 Python 3.10+
- Rust 샘플용 Rust 1.70+

**설치:**
```powershell
# Install Foundry Local
winget install Microsoft.FoundryLocal

# Verify installation
foundry --version
foundry model list
```

#### 샘플별 설정

**dotNET RAG 샘플:**
```powershell
# Install required packages via NuGet
# Microsoft.SemanticKernel.Connectors.Onnx
# Microsoft.SemanticKernel.Connectors.Qdrant
# Qdrant.Client

# Start Qdrant vector database
docker run -p 6333:6333 qdrant/qdrant

# Run Jupyter notebook
jupyter notebook rag_foundrylocal_demo.ipynb
```

**Electron 채팅 샘플:**
```powershell
# Set environment variables for cloud fallback
$env:YOUR_API_KEY="your-cloud-api-key"
$env:YOUR_ENDPOINT="your-cloud-endpoint"
$env:YOUR_MODEL_NAME="your-cloud-model"

# Install dependencies and run
npm install
npm start
```

**JavaScript/Python/Rust 샘플:**
```powershell
# Download model (example with phi-3.5-mini)
foundry model run phi-3.5-mini

# Run respective sample
node src/app.js          # JavaScript
python src/app.py        # Python
cargo run               # Rust
```

#### 주요 기능

**모델 카탈로그**
- 사전 최적화된 오픈소스 모델의 포괄적인 컬렉션
- CPU, GPU, NPU에 최적화된 모델로 즉시 배포 가능
- Llama, Mistral, Phi 및 전문 도메인 모델을 포함한 인기 모델 지원

**CLI 통합**
- 모델 관리 및 배포를 위한 명령줄 인터페이스
- 자동화된 최적화 및 양자화 워크플로
- 인기 있는 개발 환경 및 CI/CD 파이프라인과 통합

**로컬 배포**
- 클라우드 의존성 없이 완전한 오프라인 작동
- 사용자 정의 모델 형식 및 구성 지원
- 자동 하드웨어 최적화를 통한 효율적인 모델 제공

### 3. Windows ML

Windows ML은 Windows의 핵심 AI 플랫폼이자 통합 추론 런타임으로, 개발자가 광범위한 Windows 하드웨어 생태계에서 사용자 정의 모델을 효율적으로 배포할 수 있도록 지원합니다.

#### 아키텍처 이점

**범용 하드웨어 지원**
- AMD, Intel, NVIDIA, Qualcomm 실리콘에 대한 자동 최적화
- CPU, GPU, NPU 실행 지원 및 투명한 전환
- 플랫폼별 최적화 작업을 제거하는 하드웨어 추상화

**모델 유연성**
- 인기 있는 프레임워크에서 자동 변환되는 ONNX 모델 형식 지원
- 생산 등급 성능을 갖춘 사용자 정의 모델 배포
- 기존 Windows 애플리케이션 아키텍처와 통합

**엔터프라이즈 통합**
- Windows 보안 및 규정 준수 프레임워크와 호환
- 엔터프라이즈 배포 및 관리 도구 지원
- Windows 장치 관리 및 모니터링 시스템과 통합

## 개발 워크플로

### 1단계: 환경 설정 및 도구 구성

**개발 환경 준비**
1. C++ 및 .NET 워크로드가 포함된 Visual Studio 2022 설치
2. Windows App SDK 1.8.1 이상 설치
3. Windows AI Foundry CLI 도구 구성
4. Visual Studio Code용 AI Toolkit 확장 설치
5. 성능 프로파일링 및 모니터링 도구 설정
6. Copilot+ PC 최적화를 위한 ARM64 빌드 구성 보장

**샘플 리포지토리 설정**
1. [Windows App SDK 샘플 리포지토리](https://github.com/microsoft/WindowsAppSDK-Samples) 클론
2. Windows AI API 예제를 위해 `Samples/WindowsAIFoundry/cs-winui`로 이동
3. 포괄적인 Windows ML 예제를 위해 `Samples/WindowsML`로 이동
4. 대상 플랫폼에 대한 [빌드 요구사항](https://learn.microsoft.com/windows/apps/windows-app-sdk/system-requirements) 검토

**AI 개발 갤러리 탐색**
- 샘플 애플리케이션 및 참조 구현 탐색
- Windows AI API를 사용한 대화형 데모 테스트
- 모범 사례 및 패턴에 대한 소스 코드 검토
- 특정 사용 사례에 적합한 샘플 식별

### 2단계: 모델 선택 및 통합

**요구사항 분석**
- AI 기능에 대한 기능적 요구사항 정의
- 성능 제약 조건 및 최적화 목표 설정
- 개인정보 보호 및 보안 요구사항 평가
- 배포 아키텍처 및 확장 전략 계획

**모델 평가**
- Foundry Local을 사용하여 사용 사례에 적합한 오픈소스 모델 테스트
- 사용자 정의 모델 요구사항에 대한 Windows AI API 벤치마킹
- 모델 크기, 정확도, 추론 속도 간의 트레이드오프 평가
- 선택한 모델로 통합 접근 방식 프로토타입 제작

### 3단계: 애플리케이션 개발

**핵심 통합**
- 적절한 오류 처리를 포함한 Windows AI API 통합 구현
- AI 처리 워크플로를 수용하는 사용자 인터페이스 설계
- 모델 추론을 위한 캐싱 및 최적화 전략 구현
- AI 운영 성능을 위한 텔레메트리 및 모니터링 추가

**테스트 및 검증**
- 다양한 Windows 하드웨어 구성에서 애플리케이션 테스트
- 다양한 부하 조건에서 성능 메트릭 검증
- AI 기능 신뢰성을 위한 자동화된 테스트 구현
- AI 강화 기능을 사용한 사용자 경험 테스트 수행

### 4단계: 최적화 및 배포

**성능 최적화**
- 대상 하드웨어 구성에서 애플리케이션 성능 프로파일링
- 메모리 사용량 및 모델 로딩 전략 최적화
- 사용 가능한 하드웨어 기능에 따라 적응형 동작 구현
- 다양한 성능 시나리오에 맞춘 사용자 경험 미세 조정

**프로덕션 배포**
- 적절한 AI 모델 종속성을 포함한 애플리케이션 패키징
- 모델 및 애플리케이션 로직에 대한 업데이트 메커니즘 구현
- 프로덕션 환경을 위한 모니터링 및 분석 구성
- 엔터프라이즈 및 소비자 배포를 위한 롤아웃 전략 계획

## 실용적인 구현 예제

### 예제 1: 지능형 문서 처리 애플리케이션

다양한 AI 기능을 활용하여 문서를 처리하는 Windows 애플리케이션 구축:

**사용 기술:**
- 문서 요약 및 질문 응답을 위한 Phi Silica
- 스캔된 문서에서 텍스트를 추출하기 위한 OCR API
- 차트 및 다이어그램 분석을 위한 이미지 설명 API
- 문서 분류를 위한 사용자 정의 ONNX 모델

**구현 접근법:**
- 플러그형 AI 구성 요소를 갖춘 모듈형 아키텍처 설계
- 대규모 문서 배치를 위한 비동기 처리 구현
- 장기 실행 작업을 위한 진행 표시기 및 취소 지원 추가
- 민감한 문서 처리를 위한 오프라인 기능 포함

### 예제 2: 소매 재고 관리 시스템

소매 애플리케이션을 위한 AI 기반 재고 시스템 생성:

**사용 기술:**
- 제품 식별을 위한 이미지 분할
- 브랜드 및 카테고리 분류를 위한 사용자 정의 비전 모델
- 전문 소매 언어 모델의 Foundry Local 배포
- 기존 POS 및 재고 시스템과의 통합

**구현 접근법:**
- 실시간 제품 스캔을 위한 카메라 통합 구축
- 바코드 및 시각적 제품 인식 구현
- 로컬 언어 모델을 사용한 자연어 재고 쿼리 추가
- 다중 매장 배포를 위한 확장 가능한 아키텍처 설계

### 예제 3: 의료 문서 작성 도우미

개인정보를 보호하는 의료 문서 작성 도구 개발:

**사용 기술:**
- 의료 노트 생성 및 임상 의사결정 지원을 위한 Phi Silica
- 손으로 쓴 의료 기록을 디지털화하기 위한 OCR
- Windows ML을 통해 배포된 사용자 정의 의료 언어 모델
- 의료 지식 검색을 위한 로컬 벡터 저장소

**구현 접근법:**
- 환자 개인정보 보호를 위한 완전한 오프라인 작동 보장
- 의료 용어 검증 및 제안 구현
- 규정 준수를 위한 감사 로그 추가
- 기존 전자 건강 기록 시스템과의 통합 설계

## 성능 최적화 전략

### 하드웨어 인식 개발

**NPU 최적화**
- Copilot+ PC에서 NPU 기능을 활용하도록 애플리케이션 설계
- NPU가 없는 장치에서 GPU/CPU로 우아하게 대체
- NPU 특정 가속화를 위한 모델 형식 최적화
- NPU 활용 및 열 특성 모니터링

**메모리 관리**
- 효율적인 모델 로딩 및 캐싱 전략 구현
- 시작 시간을 줄이기 위해 대규모 모델에 메모리 매핑 사용
- 리소스가 제한된 장치를 위한 메모리 의식 애플리케이션 설계
- 메모리 최적화를 위한 모델 양자화 구현

**배터리 효율성**
- 최소 전력 소비를 위한 AI 작업 최적화
- 배터리 상태에 따라 적응형 처리 구현
- 지속적인 AI 작업을 위한 효율적인 백그라운드 처리 설계
- 에너지 사용을 최적화하기 위한 전력 프로파일링 도구 사용

### 확장성 고려사항

**멀티스레딩**
- 동시 처리를 위한 스레드 안전 AI 작업 설계
- 사용 가능한 코어에 효율적인 작업 분배 구현
- 비차단 AI 작업을 위한 async/await 패턴 사용
- 다양한 하드웨어 구성에 대한 스레드 풀 최적화 계획

**캐싱 전략**
- 자주 사용되는 AI 작업에 대한 지능형 캐싱 구현
- 모델 업데이트를 위한 캐시 무효화 전략 설계
- 비용이 많이 드는 전처리 작업에 대한 지속적인 캐싱 사용
- 다중 사용자 시나리오를 위한 분산 캐싱 구현

## 보안 및 개인정보 보호 모범 사례

### 데이터 보호

**로컬 처리**
- 민감한 데이터가 로컬 장치를 벗어나지 않도록 보장
- AI 모델 및 임시 데이터에 대한 안전한 저장소 구현
- 애플리케이션 샌드박싱을 위한 Windows 보안 기능 사용
- 저장된 모델 및 중간 처리 결과에 암호화 적용

**모델 보안**
- 로딩 및 실행 전에 모델 무결성 검증
- 안전한 모델 업데이트 메커니즘 구현
- 변조를 방지하기 위한 서명된 모델 사용
- 모델 파일 및 구성에 대한 액세스 제어 적용

### 규정 준수 고려사항

**규제 정렬**
- GDPR, HIPAA 및 기타 규제 요구사항을 충족하도록 애플리케이션 설계
- AI 의사결정 프로세스에 대한 감사 로그 구현
- AI 생성 결과에 대한 투명성 기능 제공
- AI 데이터 처리에 대한 사용자 제어 활성화

**엔터프라이즈 보안**
- Windows 엔터프라이즈 보안 정책과 통합
- 엔터프라이즈 관리 도구를 통한 관리형 배포 지원
- AI 기능에 대한 역할 기반 액세스 제어 구현
- AI 기능에 대한 관리 제어 제공

## 문제 해결 및 디버깅

### 일반적인 개발 문제

**빌드 구성 문제**
- Windows AI API 샘플에 대한 ARM64 플랫폼 구성 보장
- Windows App SDK 버전 호환성 확인 (1.8.1+ 필요)
- Windows AI API에 필요한 패키지 ID가 올바르게 구성되었는지 확인
- 대상 프레임워크 버전을 지원하는 빌드 도구 검증

**모델 로딩 문제**
- Windows ML과의 ONNX 모델 호환성 검증
- 모델 파일 무결성 및 형식 요구사항 확인
- 특정 모델에 대한 하드웨어 기능 요구사항 검증
- 모델 로딩 중 메모리 할당 문제 디버깅
- 하드웨어 가속을 위한 실행 공급자 등록 보장

**배포 모드 고려사항**
- **자체 포함 모드**: 더 큰 배포 크기로 완전히 지원
- **프레임워크 종속 모드**: 더 작은 크기지만 공유 런타임 필요
- **비포장 애플리케이션**: Windows AI API에 대해 더 이상 지원되지 않음
- 자체 포함 ARM64 배포를 위해 `dotnet run -p:Platform=ARM64 -p:SelfContained=true` 사용

**성능 문제**
- 다양한 하드웨어 구성에서 애플리케이션 성능 프로파일링
- AI 처리 파이프라인의 병목 현상 식별
- 데이터 전처리 및 후처리 작업 최적화
- 성능 모니터링 및 경고 구현

**통합 어려움**
- 적절한 오류 처리를 포함한 API 통합 문제 디버깅
- 입력 데이터 형식 및 전처리 요구사항 검증
- 엣지 케이스 및 오류 조건 철저히 테스트
- 프로덕션 문제 디버깅을 위한 포괄적인 로깅 구현

### 디버깅 도구 및 기술

**Visual Studio 통합**
- 모델 실행 분석을 위한 AI Toolkit 디버거 사용
- AI 작업에 대한 성능 프로파일링 구현
- 적절한 예외 처리를 포함한 비동기 AI 작업 디버깅
- 최적화를 위한 메모리 프로파일링 도구 사용

**Windows AI Foundry 도구**
- 모델 테스트 및 검증을 위한 Foundry Local CLI 활용
- 통합 검증을 위한 Windows AI API 테스트 도구 사용
- AI 작업 모니터링을 위한 사용자 정의 로깅 구현
- AI 기능 신뢰성을 위한 자동화된 테스트 생성

## 애플리케이션의 미래 대비

### 신기술

**차세대 하드웨어**
- 향후 NPU 기능을 활용하도록 애플리케이션 설계
- 증가하는 모델 크기 및 복잡성을 계획
- 진화하는 하드웨어를 위한 적응형 아키텍처 구현
- 미래 호환성을 위한 양자 준비 알고리즘 고려

**고급 AI 기능**
- 더 많은 데이터 유형에 걸친 멀티모달 AI 통합 준비
- 여러 장치 간 실시간 협업 AI 계획
- 연합 학습 기능 설계
- 엣지-클라우드 하이브리드 인텔리전스 아키텍처 고려

### 지속적인 학습 및 적응

**모델 업데이트**
- 원활한 모델 업데이트 메커니즘 구현
- 개선된 모델 기능에 적응하도록 애플리케이션 설계
- 기존 모델과의 하위 호환성 계획
- 모델 성능 평가를 위한 A/B 테스트 구현

**기능 진화**
- 새로운 AI 기능을 수용하는 모듈형 아키텍처 설계
- 새로운 Windows AI API 통합 계획
- 점진적 기능 출시를 위한 기능 플래그 구현
- 향상된 AI 기능에 적응하는 사용자 인터페이스 설계

## 결론

Windows Edge AI 개발은 강력한 AI 기능과 견고하고 안전하며 확장 가능한 Windows 플랫폼의 융합을 나타냅니다. Windows AI Foundry 생태계를 마스터함으로써 개발자는 뛰어난 사용자 경험을 제공하면서도 개인정보 보호, 보안 및 성능의 최고 기준을 유지하는 지능형 애플리케이션을 만들 수 있습니다.

Windows AI API, Foundry Local 및 Windows ML의 조합은 차세대 지능형 Windows 애플리케이션을 구축하기 위한 비할 데 없는 기반을 제공합니다. AI가 계속 발전함에 따라 Windows 플랫폼은 애플리케이션이 새로운 기술과 함께 확장되면서도 다양한 Windows 하드웨어 생태계에서 호환성과 성능을 유지하도록 보장합니다.

소비자 애플리케이션, 엔터프라이즈 솔루션 또는 전문 산업 도구를 구축하든 관계없이 Windows Edge AI 개발은 현대 Windows 장치의 잠재력을 최대한 활용하여 지능적이고 반응적이며 깊이 통합된 경험을 창출할 수 있도록 지원합니다.

## 추가 리소스

### 문서 및 학습
- [Windows AI Foundry 문서](https://learn.microsoft.com/windows/ai/)
- [Windows AI API 참조](https://learn.microsoft.com/windows/ai/apis/)
- [Windows AI API를 사용하여 앱 빌드 시작하기](https://learn.microsoft.com/windows/ai/apis/model-setup)
- [Foundry Local 시작하기](https://learn.microsoft.com/windows/ai/foundry-local/get-started/)
- [Windows ML 개요](https://learn.microsoft.com/windows/ai/new-windows-ml/overview/)
- [Windows App SDK 시스템 요구 사항](https://docs.microsoft.com/windows/apps/windows-app-sdk/system-requirements)
- [Windows App SDK 개발 환경 설정](https://docs.microsoft.com/windows/apps/windows-app-sdk/set-up-your-development-environment)
- 

### 샘플 저장소 및 코드
- [Windows App SDK 샘플 - Windows AI Foundry](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsAIFoundry)
- [Windows App SDK 샘플 - Windows ML](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML)
- [ONNX Runtime 추론 예제](https://github.com/microsoft/onnxruntime-inference-examples)
- [Windows App SDK 샘플 저장소](https://github.com/microsoft/WindowsAppSDK-Samples)

### 개발 도구
- [Visual Studio Code용 AI 툴킷](https://learn.microsoft.com/windows/ai/toolkit/)
- [AI 개발 갤러리](https://learn.microsoft.com/windows/ai/ai-dev-gallery/)
- [Windows AI 샘플](https://learn.microsoft.com/windows/ai/samples/)
- [모델 변환 도구](https://code.visualstudio.com/docs/intelligentapps/modelconversion)

### 기술 지원
- [Windows ML 문서](https://learn.microsoft.com/windows/ai/new-windows-ml/overview)
- [ONNX Runtime 문서](https://onnxruntime.ai/docs/)
- [Windows App SDK 문서](https://docs.microsoft.com/windows/apps/windows-app-sdk/)
- [문제 보고 - Windows App SDK 샘플](https://github.com/microsoft/WindowsAppSDK-Samples/issues)

### 커뮤니티 및 지원
- [Windows 개발자 커뮤니티](https://developer.microsoft.com/en-us/windows/)
- [Windows AI Foundry 블로그](https://blogs.windows.com/windowsdeveloper/)
- [Microsoft Learn AI 교육](https://learn.microsoft.com/training/browse/?products=windows&subjects=artificial-intelligence)

---

*이 가이드는 빠르게 발전하는 Windows AI 생태계에 맞춰 진화하도록 설계되었습니다. 정기적인 업데이트를 통해 최신 플랫폼 기능과 개발 모범 사례에 맞춰 조정됩니다.*

[08. Microsoft Foundry Local 실습 - 완벽한 개발자 툴킷](../Module08/README.md)

---

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있으나, 자동 번역에는 오류나 부정확한 내용이 포함될 수 있습니다. 원본 문서의 원어 버전을 신뢰할 수 있는 권위 있는 자료로 간주해야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.
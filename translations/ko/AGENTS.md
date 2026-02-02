# AGENTS.md

> **초보자를 위한 EdgeAI 기여 개발자 가이드**
> 
> 이 문서는 이 저장소에서 작업하는 개발자, AI 에이전트 및 기여자를 위한 포괄적인 정보를 제공합니다. 설정, 개발 워크플로우, 테스트 및 모범 사례를 다룹니다.
> 
> **최종 업데이트**: 2025년 10월 30일 | **문서 버전**: 3.0

## 목차

- [프로젝트 개요](../..)
- [저장소 구조](../..)
- [필수 조건](../..)
- [설정 명령어](../..)
- [개발 워크플로우](../..)
- [테스트 지침](../..)
- [코드 스타일 가이드라인](../..)
- [풀 리퀘스트 가이드라인](../..)
- [번역 시스템](../..)
- [Foundry Local 통합](../..)
- [빌드 및 배포](../..)
- [일반적인 문제 및 문제 해결](../..)
- [추가 자료](../..)
- [프로젝트 관련 메모](../..)
- [도움 받기](../..)

## 프로젝트 개요

EdgeAI for Beginners는 소형 언어 모델(SLM)을 사용한 Edge AI 개발을 교육하는 포괄적인 학습 저장소입니다. 이 과정은 EdgeAI의 기본 개념, 모델 배포, 최적화 기술 및 Microsoft Foundry Local과 다양한 AI 프레임워크를 사용한 프로덕션 준비 구현을 다룹니다.

**주요 기술:**
- Python 3.8+ (AI/ML 샘플의 주요 언어)
- .NET C# (AI/ML 샘플)
- JavaScript/Node.js 및 Electron (데스크톱 애플리케이션용)
- Microsoft Foundry Local SDK
- Microsoft Windows ML 
- VSCode AI Toolkit
- OpenAI SDK
- AI 프레임워크: LangChain, Semantic Kernel, Chainlit
- 모델 최적화: Llama.cpp, Microsoft Olive, OpenVINO, Apple MLX

**저장소 유형:** 8개의 모듈과 10개의 포괄적인 샘플 애플리케이션을 포함한 교육 콘텐츠 저장소

**아키텍처:** Edge AI 배포 패턴을 보여주는 실용적인 샘플을 포함한 다중 모듈 학습 경로

## 저장소 구조

```
edgeai-for-beginners/
├── introduction.md          # Course introduction and overview
├── Module01-07/            # Core educational modules (Markdown)
├── Module08/               # Foundry Local toolkit with 10 samples
│   ├── samples/01-06/     # Foundation samples (Python)
│   ├── samples/07/        # API client (Python)
│   ├── samples/08/        # Windows 11 chat app (Electron)
│   └── samples/09-10/     # Advanced multi-agent systems (Python)
├── Workshop/               # Hands-on workshop materials
│   ├── samples/           # Workshop Python samples with utilities
│   │   ├── session01/     # Chat bootstrap samples
│   │   ├── session02-06/  # Progressive workshop sessions
│   │   └── util/          # Workshop utility modules
│   ├── notebooks/         # Jupyter notebook tutorials
│   └── scripts/           # Validation and testing tools
├── translations/          # Multi-language translations (50+ languages)
├── translated_images/     # Localized images
└── imgs/                  # Course images and assets
```

## 필수 조건

### 필수 도구

- **Python 3.8+** - AI/ML 샘플 및 노트북용
- **Node.js 16+** - Electron 샘플 애플리케이션용
- **Git** - 버전 관리용
- **Microsoft Foundry Local** - AI 모델을 로컬에서 실행하기 위해 필요

### 권장 도구

- **Visual Studio Code** - Python, Jupyter, Pylance 확장 포함
- **Windows Terminal** - 더 나은 명령줄 경험을 위해 (Windows 사용자)
- **Docker** - 컨테이너화된 개발을 위해 (선택 사항)

### 시스템 요구 사항

- **RAM**: 최소 8GB, 다중 모델 시나리오를 위해 16GB 이상 권장
- **저장 공간**: 모델 및 종속성을 위해 10GB 이상의 여유 공간
- **운영 체제**: Windows 10/11, macOS 11+, 또는 Linux (Ubuntu 20.04+)
- **하드웨어**: AVX2 지원 CPU; GPU (CUDA, Qualcomm NPU) 선택 사항이지만 권장

### 지식 요구 사항

- Python 프로그래밍에 대한 기본 이해
- 명령줄 인터페이스에 대한 친숙함
- AI/ML 개념에 대한 이해 (샘플 개발용)
- Git 워크플로우 및 풀 리퀘스트 프로세스

## 설정 명령어

### 저장소 설정

```bash
# Clone the repository
git clone https://github.com/microsoft/edgeai-for-beginners.git
cd edgeai-for-beginners

# No build step required - this is primarily an educational content repository
```

### Python 샘플 설정 (Module08 및 워크숍 샘플)

```bash
# Create and activate virtual environment
python -m venv .venv
# On Windows
.venv\Scripts\activate
# On macOS/Linux
source .venv/bin/activate

# Install Foundry Local SDK and dependencies
pip install foundry-local-sdk openai

# Install additional dependencies for Module08 samples
cd Module08
pip install -r requirements.txt

# Install Workshop dependencies
cd ../Workshop
pip install -r requirements.txt
```

### Node.js 샘플 설정 (샘플 08 - Windows 채팅 앱)

```bash
cd Module08/samples/08
npm install

# Start in development mode
npm run dev

# Build for production
npm run build

# Create installer
npm run dist
```

### Foundry Local 설정

Foundry Local은 샘플을 실행하는 데 필요합니다. 공식 저장소에서 다운로드 및 설치하세요:

**설치:**
- **Windows**: `winget install Microsoft.FoundryLocal`
- **macOS**: `brew tap microsoft/foundrylocal && brew install foundrylocal`
- **수동 설치**: [릴리즈 페이지](https://github.com/microsoft/Foundry-Local/releases)에서 다운로드

**빠른 시작:**
```bash
# Run your first model (auto-downloads if needed)
foundry model run phi-4-mini

# List available models
foundry model ls

# Check service status
foundry service status
```

**참고**: Foundry Local은 하드웨어에 가장 적합한 모델 변형을 자동으로 선택합니다 (CUDA GPU, Qualcomm NPU, 또는 CPU).

## 개발 워크플로우

### 콘텐츠 개발

이 저장소는 주로 **Markdown 교육 콘텐츠**를 포함합니다. 변경 시:

1. 적절한 모듈 디렉토리에서 `.md` 파일을 편집합니다
2. 기존 형식 패턴을 따릅니다
3. 코드 예제가 정확하고 테스트되었는지 확인합니다
4. 필요한 경우 해당 번역 콘텐츠를 업데이트합니다 (또는 자동화에 맡깁니다)

### 샘플 애플리케이션 개발

Module08 Python 샘플 (샘플 01-07, 09-10):
```bash
cd Module08
python samples/01/chat_quickstart.py "Test message"
```

워크숍 Python 샘플:
```bash
cd Workshop/samples/session01
python chat_bootstrap.py "Test message"
```

Electron 샘플 (샘플 08):
```bash
cd Module08/samples/08
npm run dev  # Development with hot reload
```

### 샘플 애플리케이션 테스트

Python 샘플은 자동화된 테스트가 없지만 실행하여 유효성을 확인할 수 있습니다:
```bash
# Test basic chat functionality
python samples/01/chat_quickstart.py "Hello"

# Test with specific model
set MODEL=phi-4-mini
python samples/02/openai_sdk_client.py
```

Electron 샘플은 테스트 인프라를 포함합니다:
```bash
cd Module08/samples/08
npm test           # Run unit tests
npm run test:e2e   # Run end-to-end tests
npm run lint       # Check code style
```

## 테스트 지침

### 콘텐츠 유효성 검사

저장소는 자동 번역 워크플로우를 사용합니다. 번역에 대한 수동 테스트는 필요하지 않습니다.

**콘텐츠 변경에 대한 수동 유효성 검사:**
1. `.md` 파일을 미리보기하여 Markdown 렌더링을 검토합니다
2. 모든 링크가 유효한 대상에 연결되는지 확인합니다
3. 문서에 포함된 코드 스니펫을 테스트합니다
4. 이미지가 올바르게 로드되는지 확인합니다

### 샘플 애플리케이션 테스트

**Module08/samples/08 (Electron 앱)는 포괄적인 테스트를 포함합니다:**
```bash
cd Module08/samples/08

# Run all tests
npm test

# Run unit tests only
npm test -- --testPathPattern=unit

# Run integration tests
npm run test:integration

# Run E2E tests
npm run test:e2e

# Check test coverage
npm test -- --coverage
```

**Python 샘플은 수동으로 테스트해야 합니다:**
```bash
# Module08 samples
python samples/01/chat_quickstart.py "Test prompt"
python samples/04/chainlit_rag.py
python samples/09/multi_agent_system.py

# Workshop samples
cd Workshop/samples/session01
python chat_bootstrap.py "Test prompt"

# Use Workshop validation tools
cd Workshop/scripts
python validate_samples.py  # Validate syntax and imports
python test_samples.py      # Run smoke tests
```

## 코드 스타일 가이드라인

### Markdown 콘텐츠

- 일관된 제목 계층 구조 사용 (#는 제목, ##는 주요 섹션, ###는 하위 섹션)
- 언어 지정자를 포함한 코드 블록 사용: ```python, ```bash, ```javascript
- 표, 목록 및 강조 표시에 기존 형식을 따르세요
- 읽기 쉽게 줄을 유지하세요 (~80-100자 목표, 엄격하지 않음)
- 내부 참조에 상대 링크 사용

### Python 코드 스타일

- PEP 8 규칙 준수
- 적절한 곳에 타입 힌트 사용
- 함수 및 클래스에 docstring 포함
- 의미 있는 변수 이름 사용
- 함수는 집중적이고 간결하게 유지

### JavaScript/Node.js 코드 스타일

```bash
# Electron sample follows ESLint configuration
cd Module08/samples/08
npm run lint        # Check for style issues
npm run lint:fix    # Auto-fix style issues
npm run format      # Format with Prettier
```

**주요 규칙:**
- 샘플 08에 제공된 ESLint 구성 사용
- Prettier를 사용하여 코드 포맷팅
- 최신 ES6+ 문법 사용
- 코드베이스의 기존 패턴 준수

## 풀 리퀘스트 가이드라인

### 기여 워크플로우

1. **저장소를 포크**하고 `main`에서 새 브랜치를 생성합니다
2. **코드 스타일 가이드라인을 따라 변경 사항을 적용**합니다
3. **위의 테스트 지침을 사용하여 철저히 테스트**합니다
4. **명확한 메시지로 커밋**하며, 규칙적인 커밋 형식을 따릅니다
5. **포크에 푸시**하고 풀 리퀘스트를 생성합니다
6. **리뷰 중 유지보수자의 피드백에 응답**합니다

### 브랜치 명명 규칙

- `feature/<module>-<description>` - 새로운 기능 또는 콘텐츠 추가
- `fix/<module>-<description>` - 버그 수정
- `docs/<description>` - 문서 개선
- `refactor/<description>` - 코드 리팩토링

### 커밋 메시지 형식

[Conventional Commits](https://www.conventionalcommits.org/)을 따르세요:

```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

**예시:**
```
feat(Module08): add intent-based routing notebook
docs(AGENTS): update Foundry Local setup instructions
fix(samples/08): resolve Electron build issue
```

### 제목 형식
```
[ModuleXX] Brief description of change
```
 또는
```
[Module08/samples/XX] Description for sample changes
```

### 행동 강령

모든 기여자는 [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/)를 따라야 합니다. 기여하기 전에 [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md)를 검토하세요.

### 제출 전 확인 사항

**콘텐츠 변경의 경우:**
- 수정된 모든 Markdown 파일을 미리보기
- 링크와 이미지가 작동하는지 확인
- 철자 및 문법 오류 확인

**샘플 코드 변경의 경우 (Module08/samples/08):**
```bash
npm run lint
npm test
```

**Python 샘플 변경의 경우:**
- 샘플이 성공적으로 실행되는지 테스트
- 오류 처리가 작동하는지 확인
- Foundry Local과의 호환성 확인

### 리뷰 프로세스

- 교육 콘텐츠 변경은 정확성과 명확성을 기준으로 검토됩니다
- 코드 샘플은 기능성을 기준으로 테스트됩니다
- 번역 업데이트는 GitHub Actions에 의해 자동으로 처리됩니다

## 번역 시스템

**중요:** 이 저장소는 GitHub Actions를 통한 자동 번역을 사용합니다.

- 번역은 `/translations/` 디렉토리에 저장됩니다 (50개 이상의 언어 지원)
- `co-op-translator.yml` 워크플로우를 통해 자동화됩니다
- **번역 파일을 수동으로 수정하지 마세요** - 덮어쓰기가 발생합니다
- 루트 및 모듈 디렉토리의 영어 원본 파일만 수정하세요
- 번역은 `main` 브랜치에 푸시 시 자동으로 생성됩니다

## Foundry Local 통합

대부분의 Module08 샘플은 Microsoft Foundry Local이 실행 중이어야 합니다.

### 설치 및 설정

**Foundry Local 설치:**
```bash
# Windows
winget install Microsoft.FoundryLocal

# macOS
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**Python SDK 설치:**
```bash
pip install foundry-local-sdk openai
```

### Foundry Local 시작
```bash
# Start service and run a model (auto-downloads if needed)
foundry model run phi-3.5-mini

# Or use model aliases for automatic hardware optimization
foundry model run phi-4-mini
foundry model run qwen2.5-0.5b
foundry model run qwen2.5-coder-0.5b

# Check service status
foundry service status

# List available models
foundry model ls
```

### SDK 사용법 (Python)
```python
from foundry_local import FoundryLocalManager
import openai

# Use model alias for automatic hardware optimization
alias = "phi-4-mini"

# Create manager (auto-starts service and loads model)
manager = FoundryLocalManager(alias)

# Configure OpenAI client for local Foundry service
client = openai.OpenAI(
    base_url=manager.endpoint,
    api_key=manager.api_key
)

# Use the model
response = client.chat.completions.create(
    model=manager.get_model_info(alias).id,
    messages=[{"role": "user", "content": "Hello!"}]
)
```

### Foundry Local 확인
```bash
# Service status and endpoint
foundry service status

# List loaded models (REST API)
curl http://localhost:<port>/v1/models

# Note: Port is displayed when running 'foundry service status'
```

### 샘플용 환경 변수

대부분의 샘플은 다음 환경 변수를 사용합니다:
```bash
# Foundry Local configuration
# Note: The SDK (FoundryLocalManager) automatically detects endpoint
set MODEL=phi-4-mini  # or phi-3.5-mini, qwen2.5-0.5b, qwen2.5-coder-0.5b
set API_KEY=            # Not required for local usage

# Manual endpoint (if not using SDK)
# Port is shown via 'foundry service status'
set BASE_URL=http://localhost:<port>

# For Azure OpenAI fallback (optional)
set AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
set AZURE_OPENAI_API_KEY=your-api-key
set AZURE_OPENAI_API_VERSION=2024-08-01-preview
```

**참고**: `FoundryLocalManager`를 사용할 때 SDK는 서비스 검색 및 모델 로드를 자동으로 처리합니다. 모델 별칭(예: `phi-3.5-mini`)은 하드웨어에 가장 적합한 변형을 선택합니다.

## 빌드 및 배포

### 콘텐츠 배포

이 저장소는 주로 문서로 구성되어 있어 콘텐츠에 대한 빌드 프로세스가 필요하지 않습니다.

### 샘플 애플리케이션 빌드

**Electron 애플리케이션 (Module08/samples/08):**
```bash
cd Module08/samples/08

# Development build
npm run dev

# Production build
npm run build

# Create Windows installer
npm run dist

# Create portable executable
npm run pack
```

**Python 샘플:**
빌드 프로세스 없음 - Python 인터프리터로 직접 실행됩니다.

## 일반적인 문제 및 문제 해결

> **팁**: [GitHub Issues](https://github.com/microsoft/edgeai-for-beginners/issues)에서 알려진 문제와 해결책을 확인하세요.

### 주요 문제 (차단)

#### Foundry Local이 실행되지 않음
**문제:** 샘플이 연결 오류로 실패함

**해결책:**
```bash
# Check if service is running
foundry service status

# Start service with a model
foundry model run phi-4-mini

# Or explicitly start service
foundry service start

# List loaded models
foundry model ls

# Verify via REST API (port shown in 'foundry service status')
curl http://localhost:<port>/v1/models
```

### 일반적인 문제 (중간)

#### Python 가상 환경 문제
**문제:** 모듈 가져오기 오류

**해결책:**
```bash
# Ensure virtual environment is activated
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt
```

#### Electron 빌드 문제
**문제:** npm 설치 또는 빌드 실패

**해결책:**
```bash
cd Module08/samples/08
# Clean install
npm run clean
rm -rf node_modules package-lock.json
npm install
```

### 워크플로우 문제 (경미)

#### 번역 워크플로우 충돌
**문제:** 번역 PR이 변경 사항과 충돌함

**해결책:**
- 영어 원본 파일만 수정
- 자동 번역 워크플로우가 번역을 처리하도록 함
- 충돌이 발생하면 번역이 병합된 후 `main`을 브랜치에 병합

#### 모델 다운로드 실패
**문제:** Foundry Local이 모델 다운로드에 실패함

**해결책:**
```bash
# Check internet connectivity
# Clear model cache and retry
foundry model remove <model-alias>
foundry model run <model-alias>

# Check available disk space (models can be 2-16GB)
# Verify firewall settings allow downloads
```

## 추가 자료

### 학습 경로
- **초급 경로:** 모듈 01-02 (7-9시간)
- **중급 경로:** 모듈 03-04 (9-11시간)
- **고급 경로:** 모듈 05-07 (12-15시간)
- **전문가 경로:** 모듈 08 (8-10시간)
- **실습 워크숍:** 워크숍 자료 (6-8시간)

### 주요 모듈 콘텐츠
- **Module01:** EdgeAI 기본 개념 및 실제 사례 연구
- **Module02:** 소형 언어 모델(SLM) 계열 및 아키텍처
- **Module03:** 로컬 및 클라우드 배포 전략
- **Module04:** 다양한 프레임워크를 활용한 모델 최적화 (Llama.cpp, Microsoft Olive, OpenVINO, Qualcomm QNN, Apple MLX)
- **Module05:** SLMOps - 프로덕션 운영
- **Module06:** AI 에이전트 및 함수 호출
- **Module07:** 플랫폼별 구현
- **Module08:** Foundry Local 툴킷과 10개의 포괄적인 샘플

### 외부 종속성
- [Microsoft Foundry Local](https://github.com/microsoft/Foundry-Local) - OpenAI 호환 API를 갖춘 로컬 AI 모델 런타임
  - [문서](https://github.com/microsoft/Foundry-Local/blob/main/docs/README.md)
  - [Python SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/python)
  - [JavaScript SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/javascript)
- [Llama.cpp](https://github.com/ggml-org/llama.cpp) - 최적화 프레임워크
- [Microsoft Olive](https://microsoft.github.io/Olive/) - 모델 최적화 툴킷
- [OpenVINO](https://docs.openvino.ai/) - Intel의 최적화 툴킷

## 프로젝트 관련 메모

### Module08 샘플 애플리케이션

저장소에는 10개의 포괄적인 샘플 애플리케이션이 포함되어 있습니다:

1. **01-REST Chat Quickstart** - 기본 OpenAI SDK 통합
2. **02-OpenAI SDK Integration** - 고급 SDK 기능
3. **03-Model Discovery & Benchmarking** - 모델 비교 도구
4. **04-Chainlit RAG Application** - 검색 증강 생성
5. **05-Multi-Agent Orchestration** - 기본 에이전트 조정
6. **06-Models-as-Tools Router** - 지능형 모델 라우팅
7. **07-Direct API Client** - 저수준 API 통합
8. **08-Windows 11 Chat App** - 네이티브 Electron 데스크톱 애플리케이션
9. **09-Advanced Multi-Agent System** - 복잡한 에이전트 조정
10. **10-Foundry Tools Framework** - LangChain/Semantic Kernel 통합

### 워크숍 샘플 애플리케이션

워크숍은 실용적인 구현을 포함한 6개의 점진적인 세션으로 구성됩니다:

1. **세션 01** - Foundry Local 통합을 활용한 채팅 부트스트랩
2. **세션 02** - RAG 파이프라인 및 RAGAS를 활용한 평가
3. **세션 03** - 오픈 소스 모델 벤치마킹
4. **세션 04** - 모델 비교 및 선택
5. **세션 05** - 멀티 에이전트 오케스트레이션 시스템
6. **세션 06** - 모델 라우팅 및 파이프라인 관리

각 샘플은 Foundry Local을 활용한 엣지 AI 개발의 다양한 측면을 보여줍니다.

### 성능 고려사항

- SLM은 엣지 배포를 위해 최적화됨 (2-16GB RAM)
- 로컬 추론은 50-500ms 응답 시간을 제공
- 양자화 기술로 75% 크기 감소와 85% 성능 유지 달성
- 로컬 모델을 활용한 실시간 대화 기능

### 보안 및 개인정보 보호

- 모든 처리는 로컬에서 이루어짐 - 클라우드로 데이터 전송 없음
- 개인정보 보호가 중요한 애플리케이션(의료, 금융)에 적합
- 데이터 주권 요구사항 충족
- Foundry Local은 완전히 로컬 하드웨어에서 실행됨

## 도움 받기

### 문서

- **메인 README**: [README.md](README.md) - 리포지토리 개요 및 학습 경로
- **학습 가이드**: [STUDY_GUIDE.md](STUDY_GUIDE.md) - 학습 자료 및 일정
- **지원**: [SUPPORT.md](SUPPORT.md) - 도움 받는 방법
- **보안**: [SECURITY.md](SECURITY.md) - 보안 문제 보고

### 커뮤니티 지원

- **GitHub Issues**: [버그 보고 또는 기능 요청](https://github.com/microsoft/edgeai-for-beginners/issues)
- **GitHub Discussions**: [질문하고 아이디어 공유](https://github.com/microsoft/edgeai-for-beginners/discussions)
- **Foundry Local Issues**: [Foundry Local 관련 기술 문제](https://github.com/microsoft/Foundry-Local/issues)

### 연락처

- **유지관리자**: [CODEOWNERS](https://github.com/microsoft/edgeai-for-beginners/blob/main/.github/CODEOWNERS) 참조
- **보안 문제**: [SECURITY.md](SECURITY.md)에서 책임 있는 공개 절차 따르기
- **Microsoft 지원**: 기업 지원은 Microsoft 고객 서비스에 문의

### 추가 자료

- **Microsoft Learn**: [AI 및 머신 러닝 학습 경로](https://learn.microsoft.com/training/browse/?products=ai-services)
- **Foundry Local 문서**: [공식 문서](https://github.com/microsoft/Foundry-Local/blob/main/docs/README.md)
- **커뮤니티 샘플**: 커뮤니티 기여는 [GitHub Discussions](https://github.com/microsoft/edgeai-for-beginners/discussions)에서 확인

---

**이 리포지토리는 엣지 AI 개발 교육에 중점을 둔 교육용 리포지토리입니다. 주요 기여 패턴은 교육 콘텐츠를 개선하고 엣지 AI 개념을 보여주는 샘플 애플리케이션을 추가/강화하는 것입니다.**

---

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있지만, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원본 문서의 원어를 권위 있는 출처로 간주해야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 책임지지 않습니다.
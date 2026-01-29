# 모듈 08: Microsoft Foundry Local - 완벽한 개발자 도구 키트 실습

## 개요

[Microsoft Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)은 엣지 AI 개발의 차세대 기술을 대표하며, 개발자들이 강력한 도구를 활용해 AI 애플리케이션을 로컬에서 구축, 배포, 확장할 수 있도록 지원합니다. 이 모듈은 Foundry Local의 설치부터 고급 에이전트 개발까지 포괄적으로 다룹니다.

**핵심 기술:**
- Microsoft Foundry Local CLI 및 SDK
- Azure AI Foundry 통합
- 디바이스 내 모델 추론
- 로컬 모델 캐싱 및 최적화
- 에이전트 기반 아키텍처

## 학습 목표

이 모듈을 완료하면 다음을 수행할 수 있습니다:

- **Foundry Local 숙달**: Windows 11 개발을 위한 설치, 구성 및 최적화
- **다양한 모델 배포**: CLI 명령을 사용하여 phi, qwen, deepseek, GPT 모델을 로컬에서 실행
- **생산 솔루션 구축**: 고급 프롬프트 엔지니어링 및 데이터 통합을 활용한 AI 애플리케이션 생성
- **오픈소스 생태계 활용**: Hugging Face 모델 및 커뮤니티 기여 통합
- **AI 에이전트 개발**: 기반 및 오케스트레이션 기능을 갖춘 지능형 에이전트 구축
- **엔터프라이즈 패턴 구현**: 모듈형, 확장 가능한 AI 솔루션을 생산 배포를 위해 설계

## 세션 구조

### [1: Foundry Local 시작하기](./01.FoundryLocalSetup.md)
**초점**: 설치, CLI 설정, 모델 배포 및 하드웨어 최적화

**핵심 주제**: 설치 완료 • CLI 명령어 • 모델 캐싱 • 하드웨어 가속 • 다중 모델 배포

**샘플**: [REST Chat Quickstart](./samples/01/README.md) • [OpenAI SDK Integration](./samples/02/README.md) • [Model Discovery & Benchmarking](./samples/03/README.md)

**소요 시간**: 2-3시간 | **난이도**: 초급

---

### [2: Azure AI Foundry로 AI 솔루션 구축](./02.AzureAIFoundryIntegration.md)
**초점**: 고급 프롬프트 엔지니어링, 데이터 통합 및 클라우드 연결

**핵심 주제**: 프롬프트 엔지니어링 • 데이터 통합 • Azure 워크플로우 • 성능 최적화 • 모니터링

**샘플**: [Chainlit RAG Application](./samples/04/README.md)

**소요 시간**: 2-3시간 | **난이도**: 중급

---

### [3: Foundry Local에서 오픈소스 모델 활용](./03.OpenSourceModels.md)
**초점**: Hugging Face 통합, BYOM 전략 및 커뮤니티 모델

**핵심 주제**: HuggingFace 통합 • BYOM(Bring-your-own-model) • Model Mondays 인사이트 • 커뮤니티 기여 • 모델 선택

**샘플**: [Multi-Agent Orchestration](./samples/05/README.md)

**소요 시간**: 2-3시간 | **난이도**: 중급

---

### [4: 최첨단 모델 탐구](./04.CuttingEdgeModels.md)
**초점**: LLMs vs SLMs, EdgeAI 구현 및 고급 데모

**핵심 주제**: 모델 비교 • 엣지 vs 클라우드 추론 • Phi + ONNX Runtime • Chainlit RAG 앱 • WebGPU 최적화

**샘플**: [Models-as-Tools Router](./samples/06/README.md)

**소요 시간**: 3-4시간 | **난이도**: 고급

---

### [5: 빠르게 AI 기반 에이전트 구축](./05.AIPoweredAgents.md)
**초점**: 에이전트 아키텍처, 시스템 프롬프트, 기반 및 오케스트레이션

**핵심 주제**: 에이전트 설계 패턴 • 시스템 프롬프트 엔지니어링 • 기반 기술 • 다중 에이전트 시스템 • 생산 배포

**샘플**: [Multi-Agent Orchestration](./samples/05/README.md) • [Advanced Multi-Agent System](./samples/09/README.md)

**소요 시간**: 3-4시간 | **난이도**: 고급

---

### [6: Foundry Local - 도구로서의 모델](./06.ModelsAsTools.md)
**초점**: 모듈형 AI 솔루션, 엔터프라이즈 확장 및 생산 패턴

**핵심 주제**: 도구로서의 모델 • 디바이스 내 배포 • SDK/API 통합 • 엔터프라이즈 아키텍처 • 확장 전략

**샘플**: [Models-as-Tools Router](./samples/06/README.md) • [Foundry Tools Framework](./samples/10/README.md)

**소요 시간**: 3-4시간 | **난이도**: 전문가

---

### [7: 직접 API 통합 패턴](./samples/07/README.md)
**초점**: SDK 의존성 없이 순수 REST API 통합으로 최대 제어

**핵심 주제**: HTTP 클라이언트 구현 • 사용자 정의 인증 • 모델 상태 모니터링 • 스트리밍 응답 • 생산 오류 처리

**샘플**: [Direct API Client](./samples/07/README.md)

**소요 시간**: 2-3시간 | **난이도**: 중급

---

### [8: Windows 11 네이티브 채팅 애플리케이션](./samples/08/README.md)
**초점**: Foundry Local 통합을 활용한 현대적인 네이티브 채팅 애플리케이션 구축

**핵심 주제**: Electron 개발 • Fluent Design System • 네이티브 Windows 통합 • 실시간 스트리밍 • 채팅 인터페이스 설계

**샘플**: [Windows 11 Chat Application](./samples/08/README.md)

**소요 시간**: 3-4시간 | **난이도**: 고급

---

### [9: 고급 다중 에이전트 오케스트레이션](./samples/09/README.md)
**초점**: 정교한 에이전트 조정, 전문화된 작업 위임 및 협업 AI 워크플로우

**핵심 주제**: 지능형 에이전트 조정 • 함수 호출 패턴 • 에이전트 간 통신 • 워크플로우 오케스트레이션 • 품질 보증 메커니즘

**샘플**: [Advanced Multi-Agent System](./samples/09/README.md)

**소요 시간**: 4-5시간 | **난이도**: 전문가

---

### [10: Foundry Local을 도구 프레임워크로 활용](./samples/10/README.md)
**초점**: 기존 애플리케이션 및 프레임워크에 Foundry Local을 통합하기 위한 도구 중심 아키텍처

**핵심 주제**: LangChain 통합 • Semantic Kernel 함수 • REST API 프레임워크 • CLI 도구 • Jupyter 통합 • 생산 배포 패턴

**샘플**: [Foundry Tools Framework](./samples/10/README.md)

**소요 시간**: 4-5시간 | **난이도**: 전문가

## 사전 요구사항

### 시스템 요구사항
- **운영 체제**: Windows 11 (22H2 이상)
- **메모리**: 16GB RAM (대형 모델의 경우 32GB 권장)
- **저장 공간**: 모델 캐싱을 위한 50GB의 여유 공간
- **하드웨어**: NPU 지원 디바이스 권장 (Copilot+ PC), GPU 선택 사항
- **네트워크**: 초기 모델 다운로드를 위한 고속 인터넷

### 개발 환경
- AI Toolkit 확장이 포함된 Visual Studio Code
- Python 3.10+ 및 pip
- 버전 관리를 위한 Git
- PowerShell 또는 명령 프롬프트
- Azure CLI (클라우드 통합 옵션)

### 지식 요구사항
- AI/ML 개념에 대한 기본 이해
- 명령줄 사용 경험
- Python 프로그래밍 기초
- REST API 개념
- 프롬프트 및 모델 추론에 대한 기본 지식

## 모듈 타임라인

**총 예상 시간**: 30-38시간

| 세션 | 초점 영역 | 샘플 | 시간 | 복잡도 |
|------|-----------|-------|------|--------|
|  1 | 설정 및 기본 사항 | 01, 02, 03 | 2-3시간 | 초급 |
|  2 | AI 솔루션 | 04 | 2-3시간 | 중급 |
|  3 | 오픈소스 | 05 | 2-3시간 | 중급 |
|  4 | 고급 모델 | 06 | 3-4시간 | 고급 |
|  5 | AI 에이전트 | 05, 09 | 3-4시간 | 고급 |
|  6 | 엔터프라이즈 도구 | 06, 10 | 3-4시간 | 전문가 |
|  7 | 직접 API 통합 | 07 | 2-3시간 | 중급 |
|  8 | Windows 11 채팅 앱 | 08 | 3-4시간 | 고급 |
|  9 | 고급 다중 에이전트 | 09 | 4-5시간 | 전문가 |
| 10 | 도구 프레임워크 | 10 | 4-5시간 | 전문가 |

## 주요 리소스

**공식 문서:**
- [Microsoft Foundry Local GitHub](https://github.com/microsoft/Foundry-Local) - 소스 코드 및 공식 샘플
- [Azure AI Foundry 문서](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/) - 설치 및 사용 가이드
- [Model Mondays 시리즈](https://aka.ms/model-mondays) - 주간 모델 하이라이트 및 튜토리얼

**커뮤니티 및 지원:**
- [Foundry Local Discussions](https://github.com/microsoft/Foundry-Local/discussions) - 커뮤니티 Q&A 및 기능 요청
- [Microsoft AI 개발자 커뮤니티](https://techcommunity.microsoft.com/category/artificialintelligence) - 최신 뉴스 및 모범 사례

## 학습 결과

이 모듈을 완료하면 다음을 수행할 수 있습니다:

### 기술 숙련도
- **배포 및 관리**: 개발 및 생산 환경에서 Foundry Local 설치 관리
- **모델 통합**: Microsoft, Hugging Face 및 커뮤니티 소스의 다양한 모델을 원활하게 활용
- **애플리케이션 구축**: 고급 기능 및 최적화를 갖춘 생산 준비 AI 애플리케이션 생성
- **에이전트 개발**: 기반, 추론 및 도구 통합을 갖춘 정교한 AI 에이전트 구현

### 전략적 이해
- **아키텍처 결정**: 로컬 vs 클라우드 배포 간의 정보에 입각한 선택
- **성능 최적화**: 다양한 하드웨어 구성에서 추론 성능 최적화
- **엔터프라이즈 확장**: 로컬 프로토타입에서 엔터프라이즈 배포로 확장 가능한 애플리케이션 설계
- **프라이버시 및 보안**: 로컬 추론을 활용한 프라이버시 보호 AI 솔루션 구현

### 혁신 역량
- **빠른 프로토타이핑**: 모든 10가지 샘플 패턴을 통해 AI 애플리케이션 개념을 빠르게 구축 및 테스트
- **커뮤니티 통합**: 오픈소스 모델 활용 및 생태계 기여
- **고급 패턴**: RAG, 에이전트 및 도구 통합을 포함한 최첨단 AI 패턴 구현
- **프레임워크 숙련도**: LangChain, Semantic Kernel, Chainlit 및 Electron과의 전문 통합
- **생산 배포**: 로컬 프로토타입에서 엔터프라이즈 시스템으로 확장 가능한 AI 솔루션 배포
- **미래 대비 개발**: 신흥 AI 기술 및 패턴에 대비한 애플리케이션 구축

## 시작하기

1. **환경 설정**: 권장 하드웨어를 갖춘 Windows 11 준비 (사전 요구사항 참조)
2. **Foundry Local 설치**: 세션 1을 따라 설치 및 구성 완료
3. **샘플 01 실행**: 기본 REST API 통합으로 설정 확인
4. **샘플 진행**: 샘플 01-10을 완료하여 포괄적인 숙련도 확보

## 성공 지표

10가지 포괄적인 샘플을 통해 진행 상황을 추적하세요:

### 기초 수준 (샘플 01-03)
- [ ] Foundry Local 설치 및 구성 성공
- [ ] REST API 통합 완료 (샘플 01)
- [ ] OpenAI SDK 호환성 구현 (샘플 02)
- [ ] 모델 탐색 및 벤치마킹 수행 (샘플 03)

### 애플리케이션 수준 (샘플 04-06)
- [ ] 최소 4가지 모델 패밀리 배포 및 실행
- [ ] 기능적인 RAG 채팅 애플리케이션 구축 (샘플 04)
- [ ] 다중 에이전트 오케스트레이션 시스템 생성 (샘플 05)
- [ ] 지능형 모델 라우팅 구현 (샘플 06)

### 고급 통합 수준 (샘플 07-10)
- [ ] 생산 준비 API 클라이언트 구축 (샘플 07)
- [ ] Windows 11 네이티브 채팅 애플리케이션 개발 (샘플 08)
- [ ] 고급 다중 에이전트 시스템 구현 (샘플 09)
- [ ] 포괄적인 도구 프레임워크 생성 (샘플 10)

### 숙련도 지표
- [ ] 모든 10가지 샘플을 오류 없이 성공적으로 실행
- [ ] 특정 사용 사례를 위해 최소 3가지 샘플 사용자 정의
- [ ] 생산 환경과 유사한 환경에서 2개 이상의 샘플 배포
- [ ] 샘플 코드 개선 또는 확장 기여
- [ ] 개인/전문 프로젝트에 Foundry Local 패턴 통합

## 빠른 시작 가이드 - 모든 10가지 샘플

### 환경 설정 (모든 샘플에 필요)

```powershell
# 1. Clone and navigate to Module08
cd Module08

# 2. Create Python virtual environment
py -m venv .venv
.\.venv\Scripts\activate

# 3. Install base dependencies
pip install -r requirements.txt

# 4. Install Foundry Local (if not already installed)
winget install Microsoft.FoundryLocal

# 5. Verify Foundry Local installation
foundry --version
foundry model list
```

### 핵심 기초 샘플 (01-06)

**샘플 01: REST Chat Quickstart**
```powershell
# Start Foundry Local service
foundry model run phi-4-mini

# Run REST chat demo
python samples/01/chat_quickstart.py
```

**샘플 02: OpenAI SDK Integration**
```powershell
# Ensure model is running
foundry status

# Run SDK demo
python samples/02/sdk_quickstart.py
```

**샘플 03: Model Discovery & Benchmarking**
```powershell
# Run comprehensive model testing
samples/03/list_and_bench.cmd

# Or run individual components
foundry model list --available
foundry model download qwen2.5-0.5b
foundry model benchmark phi-4-mini
```

**샘플 04: Chainlit RAG Application**
```powershell
# Install Chainlit dependencies
pip install chainlit langchain chromadb

# Start RAG chat application
chainlit run samples/04/app.py -w
# Opens browser at http://localhost:8000
```

**샘플 05: Multi-Agent Orchestration**
```powershell
# Run agent coordinator demo
python -m samples.05.agents.coordinator

# Run specific agent examples
python samples/05/examples/specialists_demo.py
```

**샘플 06: Models-as-Tools Router**
```powershell
# Configure environment
set BASE_URL=http://localhost:8000
set GENERAL_MODEL=phi-4-mini
set CODE_MODEL=qwen2.5-7b

# Run intelligent router
python samples/06/router.py "Analyze this Python code for performance issues"
```

### 고급 통합 샘플 (07-10)

**샘플 07: Direct API Client**
```powershell
# Navigate to sample directory
cd samples/07

# Install additional dependencies
pip install -r requirements.txt

# Run basic API examples
python examples/basic_usage.py

# Try streaming responses
python examples/streaming.py

# Test production patterns
python examples/production.py
```

**샘플 08: Windows 11 Chat Application**
```powershell
# Navigate to sample directory
cd samples/08

# Install Node.js dependencies
npm install

# Start Electron application
npm start

# Or build for production
npm run build
```

**샘플 09: Advanced Multi-Agent System**
```powershell
# Navigate to sample directory
cd samples/09

# Install agent system dependencies
pip install -r requirements.txt

# Run basic coordination example
python examples/basic_coordination.py

# Try complex workflow
python examples/complex_workflow.py

# Interactive agent demo
python examples/interactive_demo.py
```

**샘플 10: Foundry Tools Framework**
```powershell
# Navigate to sample directory
cd samples/10

# Install framework dependencies
pip install -r requirements.txt

# Run basic tools demo
python examples/basic_tools.py

# Start REST API server
python examples/rest_api_server.py
# API available at http://localhost:8080

# Try CLI application
python examples/cli_application.py --help

# Launch Jupyter notebook
jupyter notebook examples/jupyter_notebook.ipynb

# Test LangChain integration
python examples/langchain_demo.py
```

### 일반적인 문제 해결

**Foundry Local 연결 오류**
```powershell
# Check service status
foundry status

# Restart if needed
foundry restart

# Verify endpoint accessibility
curl http://localhost:5273/v1/models
```

**모델 로딩 문제**
```powershell
# Check available models
foundry model list --cached

# Download missing models
foundry model download phi-4-mini
foundry model download qwen2.5-0.5b

# Force reload if needed
foundry model unload --all
foundry model run phi-4-mini
```

**종속성 문제**
```powershell
# Upgrade pip and reinstall
python -m pip install --upgrade pip
pip install -r requirements.txt --force-reinstall

# For Node.js samples
npm cache clean --force
npm install
```

## 요약
이 모듈은 Microsoft의 엔터프라이즈급 도구와 오픈소스 생태계의 유연성과 혁신을 결합하여 엣지 AI 개발의 최첨단을 대표합니다. Foundry Local의 10가지 포괄적인 샘플을 모두 익히면 AI 애플리케이션 개발의 선두에 설 수 있습니다.

**완전한 학습 경로:**
- **기초** (샘플 01-03): API 통합 및 모델 관리
- **응용** (샘플 04-06): RAG, 에이전트, 지능형 라우팅
- **고급** (샘플 07-10): 프로덕션 프레임워크 및 엔터프라이즈 통합

Azure OpenAI 통합(Session 2)의 경우, 필요한 환경 변수와 API 버전 설정은 각 샘플의 README 파일을 참조하세요.

---

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있으나, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원본 문서의 원어 버전을 신뢰할 수 있는 권위 있는 자료로 간주해야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.
# 변경 로그

EdgeAI for Beginners의 모든 주요 변경 사항은 여기에서 문서화됩니다. 이 프로젝트는 날짜 기반 항목과 Keep a Changelog 스타일(추가됨, 변경됨, 수정됨, 제거됨, 문서화됨, 이동됨)을 사용합니다.

## 2025-10-30

### 추가됨 - Module06 AI 에이전트 종합 강화
- **Microsoft Agent Framework 통합** (`Module06/01.IntroduceAgent.md`):
  - Microsoft Agent Framework을 활용한 프로덕션 준비 에이전트 개발 섹션 완성
  - Foundry Local과의 엣지 배포를 위한 상세 통합 패턴
  - 특화된 SLM 모델을 활용한 다중 에이전트 오케스트레이션 예제
  - 리소스 관리 및 모니터링을 포함한 엔터프라이즈 배포 패턴
  - 엣지 에이전트 시스템을 위한 보안 및 규정 준수 기능
  - 실제 구현 사례(소매, 의료, 고객 서비스)

- **프로덕션 SLM 에이전트 배포 전략**:
  - **Foundry Local**: 엔터프라이즈급 엣지 AI 런타임 문서화(설치, 구성, 프로덕션 패턴 포함)
  - **Ollama**: 커뮤니티 중심 배포 강화 및 종합적인 모니터링 및 모델 관리
  - **VLLM**: 고성능 추론 엔진과 고급 최적화 기술 및 엔터프라이즈 기능
  - 모든 플랫폼에 대한 프로덕션 배포 체크리스트 및 비교표

- **엣지 최적화 SLM 프레임워크 강화**:
  - **ONNX Runtime**: 크로스 플랫폼 SLM 에이전트 배포를 위한 새로운 종합 섹션
  - Windows, Linux, macOS, iOS, Android 전반에 걸친 범용 배포 패턴
  - 자동 감지 기능을 갖춘 하드웨어 가속 옵션(CPU, GPU, NPU)
  - 프로덕션 준비 기능 및 에이전트 특화 최적화
  - Microsoft Agent Framework 통합을 포함한 완전한 구현 예제

- **참고 자료 및 추가 읽기**:
  - 100개 이상의 권위 있는 자료를 포함한 종합적인 리소스 라이브러리
  - AI 에이전트 및 소형 언어 모델에 대한 핵심 연구 논문
  - 주요 프레임워크 및 도구의 공식 문서
  - 산업 보고서, 시장 분석 및 기술 벤치마크
  - 교육 자료, 컨퍼런스 및 커뮤니티 포럼
  - 표준, 사양 및 규정 준수 프레임워크

### 변경됨 - Module06 콘텐츠 현대화
- **학습 목표 강화**: Microsoft Agent Framework 숙달 및 엣지 배포 능력 추가
- **프로덕션 중심**: 개념적 가이드에서 구현 준비 가이드로 전환, 프로덕션 예제 포함
- **코드 예제**: 모든 예제를 최신 SDK 패턴 및 모범 사례로 업데이트
- **아키텍처 패턴**: 계층적 에이전트 아키텍처 및 엣지-클라우드 협력 추가
- **성능 최적화**: 리소스 관리 및 자동 확장 권장 사항으로 강화

### 문서화됨 - Module06 구조 강화
- **종합적인 에이전트 프레임워크 커버리지**: 기본 개념부터 엔터프라이즈 배포까지
- **프로덕션 배포 전략**: Foundry Local, Ollama, VLLM에 대한 완전한 가이드
- **크로스 플랫폼 최적화**: 범용 배포를 위한 ONNX Runtime 추가
- **리소스 라이브러리**: 지속적인 학습 및 구현을 위한 광범위한 참고 자료

### 추가됨 - Module06 모델 컨텍스트 프로토콜(MCP) 문서 업데이트
- **MCP 소개 현대화** (`Module06/03.IntroduceMCP.md`):
  - modelcontextprotocol.io의 최신 MCP 사양(2025-06-18 버전)으로 업데이트
  - 표준화된 AI 애플리케이션 연결을 위한 공식 USB-C 비유 추가
  - 공식적인 2계층 디자인(데이터 계층 + 전송 계층)을 포함한 아키텍처 섹션 업데이트
  - 서버 원시 데이터(도구, 리소스, 프롬프트) 및 클라이언트 원시 데이터(샘플링, 유도, 로깅)를 포함한 핵심 원시 데이터 문서 강화

- **종합적인 MCP 참고 자료 및 리소스**:
  - **MCP for Beginners** 링크 추가 (https://aka.ms/mcp-for-beginners)
  - MCP 공식 문서 및 사양(modelcontextprotocol.io)
  - MCP Inspector 및 참조 구현을 포함한 개발 리소스
  - 기술 표준(JSON-RPC 2.0, JSON Schema, OpenAPI, Server-Sent Events)

### 추가됨 - Module04 Qualcomm QNN 통합
- **새로운 섹션 7: Qualcomm QNN 최적화 스위트** (`Module04/05.QualcommQNN.md`):
  - Qualcomm의 통합 AI 추론 프레임워크를 다룬 400+ 라인 종합 가이드
  - 이기종 컴퓨팅(Hexagon NPU, Adreno GPU, Kryo CPU)에 대한 상세 설명
  - Snapdragon 플랫폼을 위한 하드웨어 인식 최적화 및 지능형 작업 분배
  - 모바일 배포를 위한 고급 양자화 기술(INT8, INT16, 혼합 정밀도)
  - 배터리 구동 장치 및 실시간 애플리케이션을 위한 전력 효율적인 추론 최적화
  - QNN SDK 설정 및 환경 구성에 대한 완전한 설치 가이드
  - 실용적인 예제: PyTorch에서 QNN으로의 변환, 다중 백엔드 최적화, 컨텍스트 바이너리 생성
  - 고급 사용 패턴: 사용자 정의 백엔드 구성, 동적 양자화, 성능 프로파일링
  - 종합적인 문제 해결 섹션 및 커뮤니티 리소스

- **Module04 구조 강화**:
  - README.md를 업데이트하여 6개 섹션에서 7개 섹션으로 확장
  - 성능 벤치마크 테이블에 Qualcomm QNN 추가(5-15배 속도 향상, 50-80% 메모리 감소)
  - 모바일 AI 배포 및 전력 최적화를 위한 종합적인 학습 결과 추가

### 변경됨 - Module04 문서 업데이트
- **Microsoft Olive 문서 강화** (`Module04/03.MicrosoftOlive.md`):
  - 100개 이상의 사전 구축된 최적화 레시피를 다룬 "Olive Recipes Repository" 섹션 추가
  - 지원되는 모델 계열(Phi, Llama, Qwen, Gemma, Mistral, DeepSeek)에 대한 상세 설명
  - 레시피 사용자 정의 및 커뮤니티 기여를 위한 실용적인 사용 예제
  - 성능 벤치마크 및 통합 가이드로 강화

- **Module04 섹션 재배치**:
  - Apple MLX를 섹션 5로 이동(기존 섹션 6)
  - Workflow Synthesis를 섹션 6으로 이동(기존 섹션 7)
  - Qualcomm QNN을 섹션 7로 배치(모바일/엣지 특화)
  - 모든 파일 참조 및 탐색 링크를 이에 맞게 업데이트

### 수정됨 - 워크숍 샘플 검증
- **chat_bootstrap.py 검증 및 수정**:
  - 손상된 import 문 수정(`util.util.workshop_utils` → `util.workshop_utils`)
  - Python 모듈 해석을 위한 util 패키지에 누락된 `__init__.py` 생성
  - conda 환경에 필요한 종속성(openai, foundry-local-sdk) 설치
  - 기본 및 사용자 정의 프롬프트 모두로 샘플 실행 성공적으로 검증
  - Foundry Local 서비스 및 모델 로딩(phi-4-mini with CUDA optimization)과의 통합 확인

### 문서화됨 - 종합 가이드 업데이트
- **Module04 README.md 완전한 재구성**:
  - OpenVINO, Olive, MLX와 함께 주요 최적화 프레임워크로 Qualcomm QNN 추가
  - 모바일 AI 배포 및 전력 최적화를 포함한 챕터 학습 결과 업데이트
  - QNN 메트릭 및 모바일/엣지 사용 사례를 포함한 성능 비교 테이블 강화
  - 엔터프라이즈 솔루션에서 플랫폼 특화 최적화로의 논리적 진행 유지

- **교차 참조 및 탐색**:
  - 새로운 섹션 번호에 대한 모든 내부 링크 및 파일 참조 업데이트
  - 모바일, 데스크톱 및 클라우드 환경을 포함한 Workflow Synthesis 설명 강화
  - Qualcomm 개발자 생태계에 대한 종합적인 리소스 링크 추가

## 2025-10-08

### 추가됨 - 워크숍 종합 업데이트
- **워크숍 README.md 완전한 재작성**:
  - Edge AI의 가치 제안(프라이버시, 성능, 비용)을 설명하는 종합적인 소개 추가
  - 상세한 역량을 포함한 6개의 핵심 학습 목표 생성
  - 결과물 및 역량 매트릭스를 포함한 학습 결과 테이블 추가
  - 산업 관련성을 위한 경력 준비 기술 섹션 추가
  - 사전 요구 사항 및 3단계 설정을 포함한 빠른 시작 가이드 추가
  - Python 샘플에 대한 리소스 테이블 생성(8개 파일 및 실행 시간 포함)
  - Jupyter 노트북 테이블 추가(난이도 등급 포함 8개 노트북)
  - "사용 시기" 가이드를 포함한 주요 문서 테이블 생성(7개 주요 문서)
  - 다양한 기술 수준에 대한 학습 경로 추천 생성

- **워크숍 검증 및 테스트 인프라**:
  - `scripts/validate_samples.py` 생성 - 구문, import 및 모범 사례를 위한 종합적인 검증 도구
  - `scripts/test_samples.py` 생성 - 모든 Python 샘플에 대한 스모크 테스트 실행기
  - `scripts/README.md`에 검증 문서 추가

- **종합적인 문서화**:
  - `SAMPLES_UPDATE_SUMMARY.md` 생성 - 모든 개선 사항을 다룬 400+ 라인 상세 가이드
  - `UPDATE_COMPLETE.md` 생성 - 업데이트 완료에 대한 요약 보고서
  - `QUICK_REFERENCE.md` 생성 - 워크숍에 대한 빠른 참조 카드

### 변경됨 - 워크숍 Python 샘플 현대화
- **모든 8개 Python 샘플을 모범 사례로 업데이트**:
  - 모든 I/O 작업에 대해 try-except 블록을 활용한 오류 처리 강화
  - 타입 힌트 및 종합적인 docstring 추가
  - 일관된 [INFO]/[ERROR]/[RESULT] 로깅 패턴 구현
  - 설치 힌트를 포함한 선택적 import 보호
  - 모든 샘플에서 사용자 피드백 개선

- **session01/chat_bootstrap.py**:
  - 종합적인 오류 메시지를 포함한 클라이언트 초기화 강화
  - 청크 검증을 통한 스트리밍 오류 처리 개선
  - 서비스 이용 불가에 대한 예외 처리 강화

- **session02/rag_pipeline.py**:
  - sentence-transformers에 대한 import 가드 추가 및 설치 힌트 제공
  - 임베딩 및 생성 작업에 대한 오류 처리 강화
  - 구조화된 결과를 활용한 출력 형식 개선

- **session02/rag_eval_ragas.py**:
  - 선택적 import(ragas, datasets)를 사용자 친화적인 오류 메시지로 보호
  - 평가 메트릭에 대한 오류 처리 추가
  - 평가 결과에 대한 출력 형식 개선

- **session03/benchmark_oss_models.py**:
  - 우아한 강등 구현(모델 실패 시 계속 진행)
  - 상세한 진행 보고 및 모델별 오류 처리 추가
  - 종합적인 오류 복구를 포함한 통계 계산 강화

- **session04/model_compare.py**:
  - 타입 힌트 추가(Tuple 반환 타입)
  - 구조화된 JSON 결과를 활용한 출력 형식 개선
  - 모델별 오류 처리 및 복구 구현

- **session05/agents_orchestrator.py**:
  - Agent.act()에 종합적인 docstring 추가
  - 단계별 로깅을 포함한 파이프라인 오류 처리 강화
  - 메모리 관리 및 상태 추적 개선

- **session06/models_router.py**:
  - 모든 라우팅 구성 요소에 대한 함수 문서화 강화
  - route() 함수에 상세한 로깅 추가
  - 구조화된 결과를 활용한 테스트 출력 개선

- **session06/models_pipeline.py**:
  - chat() 헬퍼 함수에 대한 오류 처리 추가
  - 단계별 로깅 및 진행 보고를 포함한 pipeline() 개선
  - 종합적인 오류 복구를 포함한 main() 개선

### 문서화됨 - 워크숍 문서 강화
- 주요 README.md를 업데이트하여 워크숍 섹션을 강조하며 실습 학습 경로 추가
- STUDY_GUIDE.md를 업데이트하여 워크숍 섹션을 포함한 종합적인 학습 가이드 추가:
  - 학습 목표 및 학습 초점 영역
  - 자기 평가 질문
  - 시간 추정이 포함된 실습 과제
  - 집중 및 파트타임 학습을 위한 시간 할당
  - 진행 추적 템플릿에 워크숍 추가
- 시간 할당 가이드를 20시간에서 30시간으로 업데이트(워크숍 포함)
- README에 워크숍 샘플 설명 및 학습 결과 추가

### 수정됨
- 워크숍 샘플 전반에 걸친 일관되지 않은 오류 처리 패턴 해결
- 선택적 종속성 import 오류를 적절한 가드로 수정
- 주요 함수에서 누락된 타입 힌트 수정
- 오류 시 사용자 피드백 부족 문제 해결
- 종합적인 테스트 인프라를 활용한 검증 문제 수정

---

## 2025-09-23

### 변경됨 - 주요 Module 08 현대화
- **Microsoft Foundry-Local 저장소 패턴과의 종합적인 정렬**
  - 모든 코드 예제를 최신 `FoundryLocalManager` 및 OpenAI SDK 통합으로 업데이트
  - 사용되지 않는 수동 `requests` 호출을 적절한 SDK 사용으로 대체
  - 공식 Microsoft 문서 및 샘플과 구현 패턴 정렬

- **05.AIPoweredAgents.md 현대화**:
  - 최신 SDK 패턴을 활용한 다중 에이전트 오케스트레이션 업데이트
  - 고급 기능(피드백 루프, 성능 모니터링)을 포함한 코디네이터 구현 강화
  - 종합적인 오류 처리 및 서비스 상태 확인 추가
  - 로컬 샘플(`samples/05/multi_agent_orchestration.ipynb`)에 대한 적절한 참조 통합
  - 사용되지 않는 `functions` 대신 최신 `tools` 매개변수를 활용한 함수 호출 예제 업데이트
  - 모니터링 및 통계 추적을 포함한 프로덕션 준비 패턴 추가

- **06.ModelsAsTools.md 완전한 재작성**:
  - 기본 도구 레지스트리를 지능형 모델 라우터 구현으로 대체
  - 다양한 작업 유형(일반, 추론, 코드, 창의적)을 위한 키워드 기반 모델 선택 추가
  - 유연한 모델 할당이 가능한 환경 기반 구성 통합
  - 종합적인 서비스 상태 모니터링 및 오류 처리 강화
  - 요청 모니터링 및 성능 추적을 포함한 프로덕션 배포 패턴 추가
  - 로컬 구현(`samples/06/router.py` 및 `samples/06/model_router.ipynb`)과 정렬

- **문서 구조 개선**:
  - 현대화 및 SDK 정렬을 강조하는 개요 섹션 추가
  - 읽기 용이성을 높이기 위한 이모지 및 더 나은 포맷 추가
  - 문서 전반에 걸쳐 로컬 샘플 파일에 대한 적절한 참조 포함
  - 프로덕션 준비 구현 가이드 및 모범 사례 포함

### 추가됨
- Module 08 파일에 현대적인 SDK 통합을 강조하는 종합적인 개요 섹션
- 고급 기능(다중 에이전트 시스템, 지능형 라우팅)을 보여주는 아키텍처 하이라이트
- 실습 경험을 위한 로컬 샘플 구현에 대한 직접 참조
- 모니터링 및 오류 처리 패턴을 포함한 프로덕션 배포 가이드
- 고급 기능 및 벤치마크를 포함한 대화형 Jupyter 노트북 예제

### 수정됨
- 문서와 실제 샘플 구현 간의 정렬 불일치 해결
- Module 08 전반에 걸친 사용되지 않는 SDK 사용 패턴 수정
- 종합적인 로컬 샘플 라이브러리에 대한 누락된 참조 해결
- 섹션 간 일관되지 않은 구현 접근 방식 수정

---

## 2025-09-18

### 추가됨
- Module 08: Microsoft Foundry Local – 완전한 개발자 툴킷
  - 여섯 세션: 설정, Azure AI Foundry 통합, 오픈 소스 모델, 최첨단 데모, 에이전트, 모델-도구
- `Module08/samples/01`–`06`의 실행 가능한 샘플과 Windows cmd 명령어
  - `01` REST 빠른 채팅 (`chat_quickstart.py`)
  - `02` OpenAI/Foundry Local 및 Azure OpenAI 지원을 포함한 SDK 빠른 시작 (`sdk_quickstart.py`)
  - `03` CLI 목록 및 벤치마크 (`list_and_bench.cmd`)
  - `04` Chainlit 데모 (`app.py`)
  - `05` 다중 에이전트 오케스트레이션 (`python -m samples.05.agents.coordinator`)
  - `06` 도구로서의 모델 라우터 (`router.py`)
- 환경 변수 구성을 통한 Session 2 SDK 샘플에서 Azure OpenAI 지원
- `.vscode/settings.json`을 `Module08/.venv`로 지정하여 Python 분석 해상도 개선
- VS Code/Pylance 인식을 위한 `PYTHONPATH` 힌트를 포함한 `.env`

### 변경 사항
- Module 08 문서 및 샘플 전반에서 기본 모델을 `phi-4-mini`로 업데이트; Module 08 내 남아 있던 `phi-3.5` 언급 제거
- 라우터 (`Module08/samples/06/router.py`) 개선:
  - 정규식 파싱을 통한 `foundry service status`로 엔드포인트 검색
  - 시작 시 `/v1/models` 상태 확인
  - 환경 변수로 구성 가능한 모델 레지스트리 (`GENERAL_MODEL`, `REASONING_MODEL`, `CODE_MODEL`, `TOOL_REGISTRY` JSON)
- 요구 사항 업데이트: `Module08/requirements.txt`에 `openai` 추가 (`requests`, `chainlit`와 함께)
- Chainlit 샘플 가이드 명확화 및 문제 해결 추가; 워크스페이스 설정을 통한 import 해결

### 수정 사항
- import 문제 해결:
  - 라우터가 더 이상 존재하지 않는 `utils` 모듈에 의존하지 않음; 함수가 인라인 처리됨
  - Coordinator가 상대 import 사용 (`from .specialists import ...`) 및 모듈 경로를 통해 호출
  - VS Code/Pylance 설정으로 `chainlit` 및 패키지 import 해결
- `STUDY_GUIDE.md`의 사소한 오타 수정 및 Module 08 커버리지 추가

### 제거된 항목
- 사용되지 않는 `Module08/infra/obs.py` 삭제 및 빈 `infra/` 디렉터리 제거; 관찰 가능성 패턴은 문서에서 선택적으로 유지

### 이동된 항목
- Module 08 데모를 `Module08/samples` 아래 세션 번호 폴더로 통합
  - Chainlit 앱을 `samples/04`로 이동
  - 에이전트를 `samples/05`로 이동하고 패키지 해석을 위한 `__init__.py` 파일 추가

### 문서
- Module 08 세션 문서 및 모든 샘플 README에 Microsoft Learn 및 신뢰할 수 있는 벤더 참조 추가
- `Module08/README.md`에 샘플 개요, 라우터 구성 및 검증 팁 업데이트
- `Module07/README.md`의 Windows Foundry Local 섹션을 Learn 문서와 검증
- `STUDY_GUIDE.md` 업데이트:
  - 개요, 일정, 진행 상황 추적기에 Module 08 추가
  - 포괄적인 참조 섹션 추가 (Foundry Local, Azure AI, Olive, ONNX Runtime, OpenVINO, MLX, Llama.cpp, vLLM, Ollama, AI Toolkit, Windows ML)

---

## 히스토리 (요약)
- 코스 아키텍처 및 모듈 설정 (Modules 01–07)
- 반복적인 콘텐츠 현대화, 형식 표준화 및 사례 연구 추가
- 최적화 프레임워크 범위 확장 (Llama.cpp, Olive, OpenVINO, Apple MLX)

## 미출시 / 백로그 (제안)
- Foundry Local 가용성을 검증하기 위한 샘플별 선택적 스모크 테스트
- 모델 참조를 정렬하기 위해 번역 검토 (예: `phi-4-mini`)
- 팀이 워크스페이스 전반의 엄격성을 선호하는 경우 최소한의 pyright 구성 추가

---

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있지만, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원본 문서의 원어 버전을 권위 있는 출처로 간주해야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 책임지지 않습니다.
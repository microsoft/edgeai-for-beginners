# EdgeAI 초보자를 위한 워크숍

> **생산 준비가 완료된 Edge AI 애플리케이션 구축을 위한 실습 학습 경로**
>
> Microsoft Foundry Local을 활용하여 첫 번째 채팅 완료부터 다중 에이전트 오케스트레이션까지 6단계의 세션을 통해 로컬 AI 배포를 마스터하세요.

---

## 🎯 소개

**EdgeAI 초보자를 위한 워크숍**에 오신 것을 환영합니다. 이 워크숍은 이론적인 Edge AI 개념을 Microsoft Foundry Local과 소형 언어 모델(SLM)을 활용한 점진적으로 어려운 실습을 통해 실제 기술로 변환하는 실용적인 가이드입니다.

### 왜 이 워크숍인가요?

**Edge AI 혁명이 시작되었습니다**

전 세계 조직들은 세 가지 주요 이유로 클라우드 의존 AI에서 엣지 컴퓨팅으로 전환하고 있습니다:

1. **프라이버시 및 규정 준수** - 민감한 데이터를 클라우드 전송 없이 로컬에서 처리 (HIPAA, GDPR, 금융 규정)
2. **성능** - 네트워크 지연 제거 (로컬 50-500ms vs 클라우드 왕복 500-2000ms)
3. **비용 관리** - 토큰당 API 비용 제거 및 클라우드 비용 없이 확장 가능

**하지만 Edge AI는 다릅니다**

온프레미스에서 AI를 실행하려면 새로운 기술이 필요합니다:
- 리소스 제약에 맞는 모델 선택 및 최적화
- 로컬 서비스 관리 및 하드웨어 가속
- 소형 모델을 위한 프롬프트 엔지니어링
- 엣지 디바이스를 위한 생산 배포 패턴

**이 워크숍은 이러한 기술을 제공합니다**

6개의 집중 세션(~총 3시간)에서 "Hello World"부터 생산 준비가 완료된 다중 에이전트 시스템 배포까지 진행하며, 모든 작업은 로컬 머신에서 실행됩니다.

---

## 📚 학습 목표

이 워크숍을 완료하면 다음을 수행할 수 있습니다:

### 핵심 역량
1. **로컬 AI 서비스 배포 및 관리**
   - Microsoft Foundry Local 설치 및 구성
   - 엣지 배포에 적합한 모델 선택
   - 모델 라이프사이클 관리 (다운로드, 로드, 캐시)
   - 리소스 사용 모니터링 및 성능 최적화

2. **AI 기반 애플리케이션 구축**
   - 로컬에서 OpenAI 호환 채팅 완료 구현
   - 소형 언어 모델을 위한 효과적인 프롬프트 설계
   - 더 나은 UX를 위한 스트리밍 응답 처리
   - 기존 애플리케이션에 로컬 모델 통합

3. **RAG (Retrieval Augmented Generation) 시스템 생성**
   - 임베딩을 활용한 의미 검색 구축
   - 도메인별 지식에 기반한 LLM 응답
   - 업계 표준 메트릭을 사용한 RAG 품질 평가
   - 프로토타입에서 생산으로 확장

4. **모델 성능 최적화**
   - 사용 사례에 맞는 여러 모델 벤치마크
   - 지연 시간, 처리량, 첫 번째 토큰 시간 측정
   - 속도/품질 트레이드오프에 기반한 최적 모델 선택
   - 실제 시나리오에서 SLM vs LLM 트레이드오프 비교

5. **다중 에이전트 시스템 오케스트레이션**
   - 다양한 작업을 위한 전문화된 에이전트 설계
   - 에이전트 메모리 및 컨텍스트 관리 구현
   - 복잡한 워크플로에서 에이전트 조정
   - 여러 모델 간 요청을 지능적으로 라우팅

6. **생산 준비 솔루션 배포**
   - 오류 처리 및 재시도 로직 구현
   - 토큰 사용량 및 시스템 리소스 모니터링
   - 모델-도구 패턴을 활용한 확장 가능한 아키텍처 구축
   - 엣지에서 하이브리드(엣지 + 클라우드)로의 마이그레이션 경로 계획

---

## 🎓 학습 결과

### 당신이 구축할 것

워크숍이 끝날 때까지 다음을 구축하게 됩니다:

| 세션 | 결과물 | 시연된 기술 |
|------|--------|------------|
| **1** | 스트리밍이 가능한 채팅 애플리케이션 | 서비스 설정, 기본 완료, 스트리밍 UX |
| **2** | 평가 가능한 RAG 시스템 | 임베딩, 의미 검색, 품질 메트릭 |
| **3** | 다중 모델 벤치마크 스위트 | 성능 측정, 모델 비교 |
| **4** | SLM vs LLM 비교 도구 | 트레이드오프 분석, 최적화 전략 |
| **5** | 다중 에이전트 오케스트레이터 | 에이전트 설계, 메모리 관리, 조정 |
| **6** | 지능형 라우팅 시스템 | 의도 감지, 모델 선택, 확장성 |

### 역량 매트릭스

| 기술 수준 | 세션 1-2 | 세션 3-4 | 세션 5-6 |
|-----------|----------|----------|----------|
| **초보자** | ✅ 설정 및 기본 | ⚠️ 도전적 | ❌ 너무 고급 |
| **중급** | ✅ 빠른 복습 | ✅ 핵심 학습 | ⚠️ 스트레치 목표 |
| **고급** | ✅ 쉽게 진행 | ✅ 세부 조정 | ✅ 생산 패턴 |

### 직업 준비 기술

**이 워크숍 후, 다음을 준비할 수 있습니다:**

✅ **프라이버시 우선 애플리케이션 구축**
- PHI/PII를 로컬에서 처리하는 헬스케어 앱
- 규정 준수를 갖춘 금융 서비스
- 데이터 주권 요구를 충족하는 정부 시스템

✅ **엣지 환경에 최적화**
- 제한된 리소스를 가진 IoT 디바이스
- 오프라인 우선 모바일 애플리케이션
- 저지연 실시간 시스템

✅ **지능형 아키텍처 설계**
- 복잡한 워크플로를 위한 다중 에이전트 시스템
- 하이브리드 엣지-클라우드 배포
- 비용 최적화 AI 인프라

✅ **Edge AI 이니셔티브 주도**
- 프로젝트에 대한 Edge AI 가능성 평가
- 적합한 모델 및 프레임워크 선택
- 확장 가능한 로컬 AI 솔루션 설계

---

## 🗺️ 워크숍 구조

### 세션 개요 (6세션 × 30분 = 3시간)

| 세션 | 주제 | 초점 | 소요 시간 |
|------|------|------|----------|
| **1** | Foundry Local 시작하기 | 설치, 검증, 첫 번째 완료 | 30분 |
| **2** | RAG를 활용한 AI 솔루션 구축 | 프롬프트 엔지니어링, 임베딩, 평가 | 30분 |
| **3** | 오픈 소스 모델 | 모델 탐색, 벤치마킹, 선택 | 30분 |
| **4** | 최첨단 모델 | SLM vs LLM, 최적화, 프레임워크 | 30분 |
| **5** | AI 기반 에이전트 | 에이전트 설계, 오케스트레이션, 메모리 | 30분 |
| **6** | 도구로서의 모델 | 라우팅, 체이닝, 확장 전략 | 30분 |

---

## 🚀 빠른 시작

### 사전 요구 사항

**시스템 요구 사항:**
- **OS**: Windows 10/11, macOS 11+, 또는 Linux (Ubuntu 20.04+)
- **RAM**: 최소 8GB, 권장 16GB 이상
- **저장 공간**: 모델을 위한 10GB 이상의 여유 공간
- **CPU**: AVX2 지원 최신 프로세서
- **GPU** (선택 사항): CUDA 호환 또는 Qualcomm NPU 가속기

**소프트웨어 요구 사항:**
- **Python 3.8+** ([다운로드](https://www.python.org/downloads/))
- **Microsoft Foundry Local** ([설치 가이드](../../../Workshop))
- **Git** ([다운로드](https://git-scm.com/downloads))
- **Visual Studio Code** (권장) ([다운로드](https://code.visualstudio.com/))

### 3단계 설정

#### 1. Foundry Local 설치

**Windows:**
```powershell
winget install Microsoft.FoundryLocal
```

**macOS:**
```bash
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**설치 확인:**
```bash
foundry --version
foundry service status
```

**Azure AI Foundry Local이 고정된 포트로 실행 중인지 확인**

```bash
# Set FoundryLocal to use port 58123 (default)
foundry service set --port 58123 --show

# Or use a different port
foundry service set --port 58000 --show
```

**작동 확인:**
```bash
# Check service status
foundry service status

# Test the endpoint
curl http://127.0.0.1:58123/v1/models
```
**사용 가능한 모델 찾기**
Foundry Local 인스턴스에서 사용 가능한 모델을 확인하려면 모델 엔드포인트를 쿼리하세요:

```bash
# cmd/bash/powershell
foundry model list
```

웹 엔드포인트 사용 

```bash
# Windows PowerShell
powershell -Command "Invoke-RestMethod -Uri 'http://127.0.0.1:58123/v1/models' -Method Get"

# Or using curl (if available)
curl http://127.0.0.1:58123/v1/models
```

#### 2. 리포지토리 클론 및 종속성 설치

```bash
# Clone repository
git clone https://github.com/microsoft/edgeai-for-beginners.git
cd edgeai-for-beginners/Workshop

# Create virtual environment
python -m venv .venv

# Activate virtual environment
# Windows:
.\.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

#### 3. 첫 번째 샘플 실행

```bash
# Start Foundry Local and load a model
foundry model run phi-4-mini

# Run the chat bootstrap sample
cd samples
python -m session01.chat_bootstrap "What is edge AI?"
```

**✅ 성공!** Edge AI에 대한 스트리밍 응답을 볼 수 있어야 합니다.

---

## 📦 워크숍 리소스

### Python 샘플

각 개념을 시연하는 점진적 실습 예제:

| 세션 | 샘플 | 설명 | 실행 시간 |
|------|------|------|----------|
| 1 | [`chat_bootstrap.py`](../../../Workshop/samples/session01/chat_bootstrap.py) | 기본 및 스트리밍 채팅 | ~30초 |
| 2 | [`rag_pipeline.py`](../../../Workshop/samples/session02/rag_pipeline.py) | 임베딩을 활용한 RAG | ~45초 |
| 2 | [`rag_eval_ragas.py`](../../../Workshop/samples/session02/rag_eval_ragas.py) | RAG 품질 평가 | ~60초 |
| 3 | [`benchmark_oss_models.py`](../../../Workshop/samples/session03/benchmark_oss_models.py) | 다중 모델 벤치마킹 | ~2-3분 |
| 4 | [`model_compare.py`](../../../Workshop/samples/session04/model_compare.py) | SLM vs LLM 비교 | ~45초 |
| 5 | [`agents_orchestrator.py`](../../../Workshop/samples/session05/agents_orchestrator.py) | 다중 에이전트 시스템 | ~60초 |
| 6 | [`models_router.py`](../../../Workshop/samples/session06/models_router.py) | 의도 기반 라우팅 | ~45초 |
| 6 | [`models_pipeline.py`](../../../Workshop/samples/session06/models_pipeline.py) | 다단계 파이프라인 | ~60초 |

### Jupyter 노트북

설명과 시각화를 포함한 대화형 탐색:

| 세션 | 노트북 | 설명 | 난이도 |
|------|-------|------|-------|
| 1 | [`session01_chat_bootstrap.ipynb`](./notebooks/session01_chat_bootstrap.ipynb) | 채팅 기본 및 스트리밍 | ⭐ 초보자 |
| 2 | [`session02_rag_pipeline.ipynb`](./notebooks/session02_rag_pipeline.ipynb) | RAG 시스템 구축 | ⭐⭐ 중급 |
| 2 | [`session02_rag_eval_ragas.ipynb`](./notebooks/session02_rag_eval_ragas.ipynb) | RAG 품질 평가 | ⭐⭐ 중급 |
| 3 | [`session03_benchmark_oss_models.ipynb`](./notebooks/session03_benchmark_oss_models.ipynb) | 모델 벤치마킹 | ⭐⭐ 중급 |
| 4 | [`session04_model_compare.ipynb`](./notebooks/session04_model_compare.ipynb) | 모델 비교 | ⭐⭐ 중급 |
| 5 | [`session05_agents_orchestrator.ipynb`](./notebooks/session05_agents_orchestrator.ipynb) | 에이전트 오케스트레이션 | ⭐⭐⭐ 고급 |
| 6 | [`session06_models_router.ipynb`](./notebooks/session06_models_router.ipynb) | 의도 라우팅 | ⭐⭐⭐ 고급 |
| 6 | [`session06_models_pipeline.ipynb`](./notebooks/session06_models_pipeline.ipynb) | 파이프라인 오케스트레이션 | ⭐⭐⭐ 고급 |

### 문서

포괄적인 가이드 및 참조:

| 문서 | 설명 | 사용 시점 |
|------|------|----------|
| [QUICK_START.md](./QUICK_START.md) | 빠른 설정 가이드 | 처음 시작할 때 |
| [QUICK_REFERENCE.md](./QUICK_REFERENCE.md) | 명령 및 API 치트 시트 | 빠른 답변이 필요할 때 |
| [FOUNDRY_SDK_QUICKREF.md](./FOUNDRY_SDK_QUICKREF.md) | SDK 패턴 및 예제 | 코드 작성 시 |
| [ENV_CONFIGURATION.md](./ENV_CONFIGURATION.md) | 환경 변수 가이드 | 샘플 구성 시 |
| [notebooks/TROUBLESHOOTING.md](./notebooks/TROUBLESHOOTING.md) | 일반적인 문제 및 해결책 | 문제 디버깅 시 |

---

## 🎓 학습 경로 추천

### 초보자를 위한 학습 경로 (3-4시간)
1. ✅ 세션 1: 시작하기 (설정 및 기본 채팅에 집중)
2. ✅ 세션 2: RAG 기본 (평가는 처음에는 생략)
3. ✅ 세션 3: 간단한 벤치마킹 (모델 2개만)
4. ⏭️ 세션 4-6은 나중에 진행
5. 🔄 첫 번째 애플리케이션을 구축한 후 세션 4-6으로 돌아가기

### 중급 개발자를 위한 학습 경로 (3시간)
1. ⚡ 세션 1: 빠른 설정 검증
2. ✅ 세션 2: 평가를 포함한 전체 RAG 파이프라인
3. ✅ 세션 3: 전체 벤치마킹 스위트
4. ✅ 세션 4: 모델 최적화
5. ✅ 세션 5-6: 아키텍처 패턴에 집중

### 고급 실무자를 위한 학습 경로 (2-3시간)
1. ⚡ 세션 1-3: 빠른 복습 및 검증
2. ✅ 세션 4: 최적화 심화 학습
3. ✅ 세션 5: 다중 에이전트 아키텍처
4. ✅ 세션 6: 생산 패턴 및 확장
5. 🚀 확장: 사용자 정의 라우팅 로직 및 하이브리드 배포 구축

---

## 워크숍 세션 팩 (집중 30분 실습)

압축된 6세션 워크숍 형식을 따르는 경우, 아래의 전용 가이드를 사용하세요 (각 가이드는 위의 광범위한 모듈 문서를 보완합니다):

| 워크숍 세션 | 가이드 | 핵심 초점 |
|------------|-------|----------|
| 1 | [Session01-GettingStartedFoundryLocal](./Session01-GettingStartedFoundryLocal.md) | 설치, 검증, phi 및 GPT-OSS-20B 실행, 가속화 |
| 2 | [Session02-BuildAISolutionsRAG](./Session02-BuildAISolutionsRAG.md) | 프롬프트 엔지니어링, RAG 패턴, CSV 및 문서 기반, 마이그레이션 |
| 3 | [Session03-OpenSourceModels](./Session03-OpenSourceModels.md) | Hugging Face 통합, 벤치마킹, 모델 선택 |
| 4 | [Session04-CuttingEdgeModels](./Session04-CuttingEdgeModels.md) | SLM vs LLM, WebGPU, Chainlit RAG, ONNX 가속화 |
| 5 | [Session05-AIPoweredAgents](./Session05-AIPoweredAgents.md) | 에이전트 역할, 메모리, 도구, 오케스트레이션 |
| 6 | [Session06-ModelsAsTools](./Session06-ModelsAsTools.md) | Azure로의 라우팅, 체이닝, 확장 경로 |

각 세션 파일에는 다음이 포함됩니다: 개요, 학습 목표, 30분 데모 흐름, 시작 프로젝트, 검증 체크리스트, 문제 해결, 그리고 공식 Foundry Local Python SDK에 대한 참조.

### 샘플 스크립트

워크숍 종속성 설치 (Windows):

```powershell
cd Workshop
py -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

macOS / Linux:

```bash
cd Workshop
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Foundry Local 서비스를 macOS에서 다른 (Windows) 머신 또는 VM에서 실행하는 경우, 엔드포인트를 내보내십시오:

```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```

| 세션 | 스크립트 | 설명 |
|------|----------|------|
| 1 | `samples/session01/chat_bootstrap.py` | 부트스트랩 서비스 및 스트리밍 채팅 |
| 2 | `samples/session02/rag_pipeline.py` | 최소 RAG (메모리 내 임베딩) |
|   | `samples/session02/rag_eval_ragas.py` | ragas 메트릭을 사용한 RAG 평가 |
| 3 | `samples/session03/benchmark_oss_models.py` | 다중 모델 지연 시간 및 처리량 벤치마킹 |
| 4 | `samples/session04/model_compare.py` | SLM vs LLM 비교 (지연 시간 및 샘플 출력) |
| 5 | `samples/session05/agents_orchestrator.py` | 두 에이전트 연구 → 편집 파이프라인 |
| 6 | `samples/session06/models_router.py` | 의도 기반 라우팅 데모 |
|   | `samples/session06/models_pipeline.py` | 다단계 계획/실행/수정 체인 |

### 환경 변수 (샘플 공통)

| 변수 | 목적 | 예시 |
|------|------|------|
| `FOUNDRY_LOCAL_ALIAS` | 기본 단일 모델 별칭 (기본 샘플용) | `phi-4-mini` |
| `SLM_ALIAS` / `LLM_ALIAS` | 비교를 위한 명시적 SLM vs 대형 모델 | `phi-4-mini` / `gpt-oss-20b` |
| `BENCH_MODELS` | 벤치마킹할 별칭 목록 (콤마로 구분) | `qwen2.5-0.5b,mistral-7b` |
| `BENCH_ROUNDS` | 모델당 벤치마킹 반복 횟수 | `3` |
| `BENCH_PROMPT` | 벤치마킹에 사용된 프롬프트 | `Explain retrieval augmented generation briefly.` |
| `EMBED_MODEL` | 문장 변환기 임베딩 모델 | `sentence-transformers/all-MiniLM-L6-v2` |
| `RAG_QUESTION` | RAG 파이프라인 테스트 쿼리 재정의 | `Why use RAG with local inference?` |
| `AGENT_QUESTION` | 에이전트 파이프라인 쿼리 재정의 | `Explain why edge AI matters for compliance.` |
| `AGENT_MODEL_PRIMARY` | 연구 에이전트 모델 별칭 | `phi-4-mini` |
| `AGENT_MODEL_EDITOR` | 편집 에이전트 모델 별칭 (다를 수 있음) | `gpt-oss-20b` |
| `SHOW_USAGE` | `1`일 때, 완료당 토큰 사용량 출력 | `1` |
| `RETRY_ON_FAIL` | `1`일 때, 일시적인 채팅 오류 시 한 번 재시도 | `1` |
| `RETRY_BACKOFF` | 재시도 전 대기 시간 (초) | `1.0` |

변수가 설정되지 않은 경우, 스크립트는 적절한 기본값으로 대체됩니다. 단일 모델 데모에서는 일반적으로 `FOUNDRY_LOCAL_ALIAS`만 필요합니다.

### 유틸리티 모듈

모든 샘플은 이제 `samples/workshop_utils.py`라는 헬퍼를 공유하며 다음을 제공합니다:

* 캐시된 `FoundryLocalManager` + OpenAI 클라이언트 생성
* 선택적 재시도 및 사용량 출력이 가능한 `chat_once()` 헬퍼
* 간단한 토큰 사용량 보고 (환경 변수 `SHOW_USAGE=1`로 활성화)

이는 중복을 줄이고 효율적인 로컬 모델 오케스트레이션을 위한 모범 사례를 강조합니다.

## 선택적 향상 기능 (세션 간)

| 주제 | 향상 기능 | 세션 | 환경 변수 / 토글 |
|------|----------|------|------------------|
| 결정론 | 고정된 온도 + 안정적인 프롬프트 세트 | 1–6 | `temperature=0`, `top_p=1` 설정 |
| 토큰 사용량 가시성 | 일관된 비용/효율성 교육 | 1–6 | `SHOW_USAGE=1` |
| 스트리밍 첫 번째 토큰 | 지연 시간 지표 | 1,3,4,6 | `BENCH_STREAM=1` (벤치마킹) |
| 재시도 복원력 | 일시적인 초기 시작 처리 | 모든 세션 | `RETRY_ON_FAIL=1` + `RETRY_BACKOFF` |
| 다중 모델 에이전트 | 이질적인 역할 전문화 | 5 | `AGENT_MODEL_PRIMARY`, `AGENT_MODEL_EDITOR` |
| 적응형 라우팅 | 의도 + 비용 휴리스틱 | 6 | 라우터를 확장하여 에스컬레이션 로직 추가 |
| 벡터 메모리 | 장기적인 의미 기억 | 2,5,6 | FAISS/Chroma 임베딩 인덱스 통합 |
| 추적 내보내기 | 감사 및 평가 | 2,5,6 | 단계별 JSON 라인 추가 |
| 품질 루브릭 | 질적 추적 | 3–6 | 보조 점수 프롬프트 |
| 스모크 테스트 | 워크숍 사전 검증 | 모든 세션 | `python Workshop/tests/smoke.py` |

### 결정론적 빠른 시작

```powershell
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
python Workshop\tests\smoke.py
```

동일한 입력 반복 시 안정적인 토큰 수를 기대하십시오.

### RAG 평가 (세션 2)

`rag_eval_ragas.py`를 사용하여 작은 합성 데이터셋에서 답변 관련성, 신뢰성, 컨텍스트 정확도를 계산하십시오:

```powershell
cd Workshop/samples
python -m session02.rag_eval_ragas
```

질문, 컨텍스트, 정답의 더 큰 JSONL을 제공한 후 Hugging Face `Dataset`으로 변환하여 확장하십시오.

## CLI 명령 정확성 부록

워크숍은 현재 문서화된 / 안정적인 Foundry Local CLI 명령만 사용합니다.

### 참조된 안정적인 명령

| 카테고리 | 명령 | 목적 |
|----------|------|------|
| 핵심 | `foundry --version` | 설치된 버전 표시 |
| 서비스 | `foundry service start` | 로컬 서비스 시작 (자동이 아닌 경우) |
| 서비스 | `foundry service status` | 서비스 상태 표시 |
| 모델 | `foundry model list` | 카탈로그 / 사용 가능한 모델 목록 |
| 모델 | `foundry model download <alias>` | 모델 가중치를 캐시에 다운로드 |
| 모델 | `foundry model run <alias>` | 로컬에서 모델 실행 (로드); `--prompt`와 결합하여 단일 실행 |
| 모델 | `foundry model unload <alias>` / `foundry model stop <alias>` | 메모리에서 모델 언로드 (지원되는 경우) |
| 캐시 | `foundry cache list` | 캐시에 다운로드된 모델 목록 |

### 단일 실행 프롬프트 패턴

더 이상 사용되지 않는 `model chat` 하위 명령 대신 다음을 사용하십시오:

```powershell
foundry model run <alias> --prompt "Your question here"
```

이 명령은 단일 프롬프트/응답 사이클을 실행한 후 종료합니다.

### 제거된 / 피해야 할 패턴

| 사용 중단 / 문서화되지 않음 | 대체 / 가이드라인 |
|---------------------------|-------------------|
| `foundry model chat <model> "..."` | `foundry model run <model> --prompt "..."` |
| `foundry model list --running` | 일반 `foundry model list` + 최근 활동 / 로그 사용 |
| `foundry model list --cached` | `foundry cache list` |
| `foundry model stats <model>` | 벤치마크 Python 스크립트 + OS 도구 (작업 관리자 / `nvidia-smi`) 사용 |
| `foundry model benchmark ...` | `samples/session03/benchmark_oss_models.py` |

### 벤치마킹 및 텔레메트리

- 지연 시간, p95, 초당 토큰: `samples/session03/benchmark_oss_models.py`
- 첫 번째 토큰 지연 시간 (스트리밍): 환경 변수 `BENCH_STREAM=1` 설정
- 리소스 사용량: OS 모니터 (작업 관리자, Activity Monitor, `nvidia-smi`).

새로운 CLI 텔레메트리 명령이 상류에서 안정화되면, 세션 마크다운에 최소한의 수정으로 통합할 수 있습니다.

### 자동 린트 가드

자동 린터는 마크다운 파일의 코드 블록 내부에서 사용 중단된 CLI 패턴의 재도입을 방지합니다:

스크립트: `Workshop/scripts/lint_markdown_cli.py`

코드 펜스 내부에서 사용 중단된 패턴이 차단됩니다.

권장 대체:
| 사용 중단 | 대체 |
|----------|------|
| `foundry model chat <a> "..."` | `foundry model run <a> --prompt "..."` |
| `model list --running` | `model list` |
| `model list --cached` | `cache list` |
| `model stats` | 벤치마크 스크립트 + 시스템 도구 |
| `model benchmark` | `samples/session03/benchmark_oss_models.py` |
| `model list --available` | `model list` |

로컬 실행:
```powershell
python Workshop\scripts\lint_markdown_cli.py --verbose
```

GitHub 액션: `.github/workflows/markdown-cli-lint.yml`가 모든 푸시 및 PR에서 실행됩니다.

선택적 pre-commit 훅:
```bash
echo "python Workshop/scripts/lint_markdown_cli.py" > .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```

## 빠른 CLI → SDK 마이그레이션 테이블

| 작업 | CLI 원라이너 | SDK (Python) 동등 | 참고 |
|------|-------------|------------------|------|
| 모델 한 번 실행 (프롬프트) | `foundry model run phi-4-mini --prompt "Hello"` | `manager=FoundryLocalManager("phi-4-mini"); client=OpenAI(base_url=manager.endpoint, api_key=manager.api_key or "not-needed"); client.chat.completions.create(model=manager.get_model_info("phi-4-mini").id, messages=[{"role":"user","content":"Hello"}])` | SDK는 서비스 및 캐싱을 자동으로 부트스트랩 |
| 모델 다운로드 (캐시) | `foundry model download qwen2.5-0.5b` | `FoundryLocalManager("qwen2.5-0.5b")  # 다운로드/로드 트리거` | 별칭이 여러 빌드에 매핑되는 경우 관리자가 최적의 변형 선택 |
| 카탈로그 목록 | `foundry model list` | `# 각 별칭에 대해 관리자를 사용하거나 알려진 목록 유지` | CLI는 집계; SDK는 현재 별칭별 초기화 |
| 캐시된 모델 목록 | `foundry cache list` | `manager.list_cached_models()` | 관리자 초기화 후 (어떤 별칭이든) |
| 엔드포인트 URL 가져오기 | (암시적) | `manager.endpoint` | OpenAI 호환 클라이언트 생성에 사용 |
| 모델 예열 | `foundry model run <alias>` 후 첫 번째 프롬프트 | `chat_once(alias, messages=[...])` (유틸리티) | 유틸리티는 초기 냉시작 지연 시간 예열 처리 |
| 지연 시간 측정 | `python -m session03.benchmark_oss_models` | `import benchmark_oss_models` (또는 새로운 내보내기 스크립트) | 일관된 메트릭을 위해 스크립트 선호 |
| 모델 중지 / 언로드 | `foundry model unload <alias>` | (노출되지 않음 – 서비스 / 프로세스 재시작) | 워크숍 흐름에서는 일반적으로 필요하지 않음 |
| 토큰 사용량 검색 | (출력 보기) | `resp.usage.total_tokens` | 백엔드가 사용량 객체를 반환하는 경우 제공 |

## 벤치마크 마크다운 내보내기

스크립트 `Workshop/scripts/export_benchmark_markdown.py`를 사용하여 새 벤치마크를 실행하고 (논리는 `samples/session03/benchmark_oss_models.py`와 동일) GitHub 친화적인 마크다운 테이블과 원시 JSON을 생성하십시오.

### 예시

```powershell
python Workshop\scripts\export_benchmark_markdown.py --models "qwen2.5-0.5b,mistral-7b" --prompt "Explain retrieval augmented generation briefly." --rounds 3 --output benchmark_report.md
```

생성된 파일:
| 파일 | 내용 |
|------|------|
| `benchmark_report.md` | 마크다운 테이블 + 해석 힌트 |
| `benchmark_report.json` | 원시 메트릭 배열 (차이 비교 / 추세 추적용) |

환경 변수 `BENCH_STREAM=1`을 설정하여 첫 번째 토큰 지연 시간을 포함하십시오 (지원되는 경우).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있지만, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원본 문서의 원어 버전을 권위 있는 출처로 간주해야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 책임지지 않습니다.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
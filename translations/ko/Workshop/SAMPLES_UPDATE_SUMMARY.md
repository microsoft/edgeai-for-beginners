<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d49922db25659f398bae92011305e9dc",
  "translation_date": "2025-10-28T20:59:38+00:00",
  "source_file": "Workshop/SAMPLES_UPDATE_SUMMARY.md",
  "language_code": "ko"
}
-->
# 워크숍 샘플 - Foundry Local SDK 업데이트 요약

## 개요

`Workshop/samples` 디렉토리의 모든 Python 샘플이 Foundry Local SDK의 모범 사례를 따르도록 업데이트되었으며 워크숍 전반에 걸쳐 일관성을 보장합니다.

**날짜**: 2025년 10월 8일  
**범위**: 6개의 워크숍 세션에서 9개의 Python 파일  
**주요 초점**: 오류 처리, 문서화, SDK 패턴, 사용자 경험

---

## 업데이트된 파일

### 세션 01: 시작하기
- ✅ `chat_bootstrap.py` - 기본 채팅 및 스트리밍 예제

### 세션 02: RAG 솔루션
- ✅ `rag_pipeline.py` - 임베딩을 활용한 RAG 구현
- ✅ `rag_eval_ragas.py` - RAGAS 지표를 활용한 RAG 평가

### 세션 03: 오픈 소스 모델
- ✅ `benchmark_oss_models.py` - 다중 모델 벤치마킹

### 세션 04: 첨단 모델
- ✅ `model_compare.py` - SLM과 LLM 비교

### 세션 05: AI 기반 에이전트
- ✅ `agents_orchestrator.py` - 다중 에이전트 조정

### 세션 06: 도구로서의 모델
- ✅ `models_router.py` - 의도 기반 모델 라우팅
- ✅ `models_pipeline.py` - 다단계 라우팅 파이프라인

### 지원 인프라
- ✅ `workshop_utils.py` - 이미 모범 사례를 따르고 있음 (변경 필요 없음)

---

## 주요 개선 사항

### 1. 향상된 오류 처리

**이전:**
```python
manager, client, model_id = get_client(alias)
```

**이후:**
```python
try:
    manager, client, model_id = get_client(alias, endpoint=endpoint)
except Exception as e:
    print(f"[ERROR] Failed to initialize Foundry Local client: {e}")
    print("[INFO] Ensure Foundry Local is running: foundry service status")
    sys.exit(1)
```

**혜택:**
- 명확한 오류 메시지를 통한 우아한 오류 처리
- 실행 가능한 문제 해결 힌트 제공
- 스크립팅을 위한 적절한 종료 코드

### 2. 개선된 Import 관리

**이전:**
```python
from sentence_transformers import SentenceTransformer
```

**이후:**
```python
try:
    from sentence_transformers import SentenceTransformer
except ImportError:
    print("[ERROR] sentence-transformers is required. Install with: pip install sentence-transformers")
    sys.exit(1)
```

**혜택:**
- 종속성이 누락된 경우 명확한 안내 제공
- 난해한 Import 오류 방지
- 사용자 친화적인 설치 지침

### 3. 포괄적인 문서화

**모든 샘플에 추가됨:**
- docstring에 환경 변수 문서화
- SDK 참조 링크
- 사용 예제
- 상세한 함수/매개변수 문서화
- IDE 지원을 위한 타입 힌트

**예시:**
```python
def pipeline(task: str) -> Dict[str, Any]:
    """Execute multi-step routed pipeline for complex task.
    
    Args:
        task: User task description
    
    Returns:
        Dictionary with plan, step outputs, and final summary
    
    Raises:
        Exception: If any pipeline stage fails
    """
```

### 4. 개선된 사용자 피드백

**정보성 로깅 추가:**
```python
print(f"[INFO] Using model alias: {alias} -> id: {model_id}")
print(f"[INFO] Endpoint: {manager.endpoint}")
print(f"[INFO] Loaded model: {alias} -> {model_id}")
```

**진행 상태 표시기:**
```python
print(f"[INFO] Benchmarking {alias}...")
print(f"  Round {round_num + 1}/{ROUNDS}: {latency:.3f}s")
print(f"[INFO] Completed {alias}\n")
```

**구조화된 출력:**
```python
print("\n[BENCHMARK RESULTS]")
print(json.dumps(summary, indent=2))
```

### 5. 강력한 벤치마킹

**세션 03 개선 사항:**
- 모델별 오류 처리 (실패 시 계속 진행)
- 상세한 진행 상태 보고
- 워밍업 라운드 적절히 실행
- 첫 번째 토큰 지연 측정 지원
- 단계별 명확한 분리

### 6. 일관된 타입 힌트

**전체적으로 추가됨:**
```python
from typing import Dict, List, Tuple, Any, Optional

def run(alias: str) -> Tuple[float, str, Optional[int]]:
    """Run comparison for given model alias."""
```

**혜택:**
- IDE 자동 완성 향상
- 초기 오류 감지
- 자체 문서화 코드

### 7. 개선된 모델 라우터

**세션 06 개선 사항:**
- 포괄적인 의도 감지 문서화
- 모델 선택 알고리즘 설명
- 상세한 라우팅 로그
- 테스트 출력 형식화
- 배치 테스트에서 오류 복구

### 8. 다중 에이전트 오케스트레이션

**세션 05 개선 사항:**
- 단계별 진행 상태 보고
- 에이전트별 오류 처리
- 명확한 파이프라인 구조
- 향상된 메모리 관리 문서화

---

## 테스트 체크리스트

### 사전 준비
```bash
# Ensure Foundry Local is running
foundry service status

# Load required models
foundry model run phi-4-mini
foundry model run qwen2.5-0.5b

# Install dependencies
pip install -r Workshop/requirements.txt
```

### 각 샘플 테스트

#### 세션 01
```bash
cd Workshop/samples
python -m session01.chat_bootstrap "What is edge AI?"
```

#### 세션 02
```bash
cd Workshop/samples

# RAG pipeline
python -m session02.rag_pipeline

# RAG evaluation (requires ragas)
set RAG_QUESTION="What is local inference?"
python -m session02.rag_eval_ragas
```

#### 세션 03
```bash
cd Workshop/samples

# Quick benchmark (2 rounds)
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
set BENCH_ROUNDS=2
python -m session03.benchmark_oss_models
```

#### 세션 04
```bash
cd Workshop/samples

# SLM vs LLM comparison
set SLM_ALIAS=phi-4-mini
set LLM_ALIAS=qwen2.5-7b
python -m session04.model_compare
```

#### 세션 05
```bash
cd Workshop/samples

# Multi-agent orchestration
set AGENT_QUESTION="Why use local AI for healthcare?"
python -m session05.agents_orchestrator
```

#### 세션 06
```bash
cd Workshop/samples

# Intent-based routing
python -m session06.models_router

# Multi-step pipeline
set PIPELINE_TASK="Create a Python function and explain its performance"
python -m session06.models_pipeline
```

---

## 환경 변수 참조

### 글로벌 (모든 샘플)
| 변수 | 설명 | 기본값 |
|------|------|--------|
| `FOUNDRY_LOCAL_ALIAS` | 사용할 모델 별칭 | 샘플별로 다름 |
| `FOUNDRY_LOCAL_ENDPOINT` | 서비스 엔드포인트 재정의 | 자동 감지 |
| `SHOW_USAGE` | 토큰 사용량 표시 | `0` |
| `RETRY_ON_FAIL` | 재시도 로직 활성화 | `1` |
| `RETRY_BACKOFF` | 초기 재시도 지연 | `1.0` |

### 샘플별
| 변수 | 사용 세션 | 설명 |
|------|----------|------|
| `EMBED_MODEL` | 세션 02 | 임베딩 모델 이름 |
| `RAG_QUESTION` | 세션 02 | RAG 테스트 질문 |
| `BENCH_MODELS` | 세션 03 | 벤치마킹할 모델 목록 (쉼표로 구분) |
| `BENCH_ROUNDS` | 세션 03 | 벤치마킹 라운드 수 |
| `BENCH_PROMPT` | 세션 03 | 벤치마킹 테스트 프롬프트 |
| `BENCH_STREAM` | 세션 03 | 첫 번째 토큰 지연 측정 |
| `SLM_ALIAS` | 세션 04 | 소형 언어 모델 |
| `LLM_ALIAS` | 세션 04 | 대형 언어 모델 |
| `COMPARE_PROMPT` | 세션 04 | 비교 테스트 프롬프트 |
| `AGENT_MODEL_PRIMARY` | 세션 05 | 주요 에이전트 모델 |
| `AGENT_MODEL_EDITOR` | 세션 05 | 편집기 에이전트 모델 |
| `AGENT_QUESTION` | 세션 05 | 에이전트 테스트 질문 |
| `PIPELINE_TASK` | 세션 06 | 파이프라인 작업 |

---

## 주요 변경 사항

**없음** - 모든 변경 사항은 이전 버전과 호환됩니다.

기존 스크립트는 계속 작동합니다. 새로운 기능은 다음과 같습니다:
- 선택적 환경 변수
- 향상된 오류 메시지 (기능에 영향을 주지 않음)
- 추가 로깅 (억제 가능)
- 개선된 타입 힌트 (런타임 영향 없음)

---

## 구현된 모범 사례

### 1. 항상 Workshop Utils 사용
```python
from workshop_utils import get_client, chat_once

# Provides caching, retry, and endpoint management
manager, client, model_id = get_client(alias, endpoint=endpoint)
```

### 2. 적절한 오류 처리 패턴
```python
try:
    # Initialize client
    manager, client, model_id = get_client(alias)
except Exception as e:
    print(f"[ERROR] Initialization failed: {e}")
    print("[INFO] Check: foundry service status")
    sys.exit(1)
```

### 3. 정보성 로깅
```python
print(f"[INFO] Starting process...")  # Info
print(f"[ERROR] Operation failed: {e}")  # Errors
print(f"[RESULT] Final output")  # Results
```

### 4. 타입 힌트
```python
from typing import Dict, List, Optional

def process(data: List[str]) -> Dict[str, Any]:
    """Process data with type safety."""
```

### 5. 포괄적인 Docstring
```python
def function(arg: str) -> str:
    """Short description.
    
    Args:
        arg: Argument description
    
    Returns:
        Return value description
    
    Raises:
        Exception: When it fails
    """
```

### 6. 환경 변수 지원
```python
import os

alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-4-mini")
endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT")  # None if not set
```

### 7. 우아한 성능 저하
```python
# In benchmarks - continue on individual failures
for model in models:
    try:
        result = benchmark(model)
        results.append(result)
    except Exception as e:
        print(f"[ERROR] {model} failed: {e}")
        print(f"[INFO] Skipping {model}...")
```

---

## 일반적인 문제 및 해결책

### 문제: Import 오류
**해결책:** 누락된 종속성 설치
```bash
pip install sentence-transformers ragas datasets numpy
```

### 문제: 연결 오류
**해결책:** Foundry Local이 실행 중인지 확인
```bash
foundry service status
foundry model run phi-4-mini
```

### 문제: 모델을 찾을 수 없음
**해결책:** 사용 가능한 모델 확인
```bash
foundry model ls
foundry model download <alias>
```

### 문제: 느린 성능
**해결책:** 더 작은 모델 사용 또는 매개변수 조정
```bash
set FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b
set BENCH_ROUNDS=2
```

---

## 다음 단계

### 1. 모든 샘플 테스트
위의 테스트 체크리스트를 따라 모든 샘플이 올바르게 작동하는지 확인하세요.

### 2. 문서 업데이트
- 새로운 예제를 세션 마크다운 파일에 업데이트
- 주요 README에 문제 해결 섹션 추가
- 빠른 참조 가이드 작성

### 3. 통합 테스트 생성
```python
# Workshop/tests/test_samples.py
def test_all_samples():
    """Run smoke tests on all samples."""
```

### 4. 성능 벤치마크 추가
오류 처리 개선으로 인한 성능 향상을 추적하세요.

### 5. 사용자 피드백
워크숍 참가자들로부터 다음에 대한 피드백을 수집하세요:
- 오류 메시지 명확성
- 문서화 완성도
- 사용 편의성

---

## 리소스

- **Foundry Local SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **빠른 참조**: `Workshop/FOUNDRY_SDK_QUICKREF.md`
- **마이그레이션 노트**: `Workshop/SDK_MIGRATION_NOTES.md`
- **메인 저장소**: https://github.com/microsoft/Foundry-Local

---

## 유지 관리

### 새로운 샘플 추가
새로운 샘플을 생성할 때 다음 패턴을 따르세요:

1. `workshop_utils`를 사용하여 클라이언트 관리
2. 포괄적인 오류 처리 추가
3. 환경 변수 지원 포함
4. 타입 힌트와 docstring 추가
5. 정보성 로깅 제공
6. docstring에 사용 예제 포함
7. SDK 문서 링크 추가

### 업데이트 검토
샘플 업데이트를 검토할 때 다음을 확인하세요:
- [ ] 모든 I/O 작업에서 오류 처리
- [ ] 공개 함수에 타입 힌트 추가
- [ ] 포괄적인 docstring
- [ ] 환경 변수 문서화
- [ ] 정보성 사용자 피드백
- [ ] SDK 참조 링크
- [ ] 일관된 코드 스타일

---

**요약**: 모든 워크숍 Python 샘플이 이제 Foundry Local SDK 모범 사례를 따르며, 향상된 오류 처리, 포괄적인 문서화, 개선된 사용자 경험을 제공합니다. 기존 기능은 그대로 유지되며, 추가된 기능은 선택적으로 사용할 수 있습니다.

---

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하지만, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원본 문서의 원어 버전을 권위 있는 출처로 간주해야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 책임을 지지 않습니다.
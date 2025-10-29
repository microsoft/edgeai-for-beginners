<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a5bfedb0d4694a0b3a95d69b159b1a5a",
  "translation_date": "2025-10-28T20:59:54+00:00",
  "source_file": "Workshop/SDK_MIGRATION_NOTES.md",
  "language_code": "ko"
}
-->
# Foundry Local SDK 마이그레이션 노트

## 개요

Workshop 폴더의 모든 Python 파일이 공식 [Foundry Local Python SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local)의 최신 패턴을 따르도록 업데이트되었습니다.

## 변경 사항 요약

### 핵심 인프라 (`workshop_utils.py`)

#### 향상된 기능:
- **엔드포인트 오버라이드 지원**: `FOUNDRY_LOCAL_ENDPOINT` 환경 변수를 추가하여 지원
- **개선된 오류 처리**: 상세한 오류 메시지를 포함한 예외 처리 개선
- **향상된 캐싱**: 다중 엔드포인트 시나리오를 위해 캐시 키에 엔드포인트 포함
- **지수적 백오프**: 신뢰성을 높이기 위해 지수적 백오프를 사용하는 재시도 로직 추가
- **타입 주석**: IDE 지원을 위한 포괄적인 타입 힌트 추가

#### 새로운 기능:
```python
# Now supports endpoint override
manager, client, model_id = get_client(alias, endpoint="http://localhost:8000")

# Better error messages
RuntimeError: Client initialization failed for 'phi-4-mini': <detailed_error>
```

### 샘플 애플리케이션

#### 세션 01: 채팅 부트스트랩 (`chat_bootstrap.py`)
- 기본 모델을 `phi-3.5-mini`에서 `phi-4-mini`로 업데이트
- 엔드포인트 오버라이드 지원 추가
- SDK 참조를 포함한 문서 개선

#### 세션 02: RAG 파이프라인 (`rag_pipeline.py`)
- 기본 모델을 `phi-4-mini`로 업데이트
- 엔드포인트 오버라이드 지원 추가
- 환경 변수 세부사항을 포함한 문서 개선

#### 세션 02: RAG 평가 (`rag_eval_ragas.py`)
- 모델 기본값 업데이트
- 엔드포인트 구성 추가
- 오류 처리 개선

#### 세션 03: 벤치마킹 (`benchmark_oss_models.py`)
- 기본 모델 목록에 `phi-4-mini` 추가
- 포괄적인 환경 변수 문서 추가
- 함수 문서 개선
- 전체적으로 엔드포인트 오버라이드 지원 추가

#### 세션 04: 모델 비교 (`model_compare.py`)
- 기본 LLM을 `gpt-oss-20b`에서 `qwen2.5-7b`로 업데이트
- 엔드포인트 구성 추가
- 문서 개선

#### 세션 05: 멀티 에이전트 오케스트레이션 (`agents_orchestrator.py`)
- 타입 힌트 추가 (`str | None`을 `Optional[str]`로 변경)
- 에이전트 클래스 문서 개선
- 엔드포인트 오버라이드 지원 추가
- 초기화 패턴 개선

#### 세션 06: 모델 라우터 (`models_router.py`)
- 엔드포인트 구성 추가
- 의도 감지 문서 개선
- 라우팅 로직 문서 개선

#### 세션 06: 파이프라인 (`models_pipeline.py`)
- 포괄적인 함수 문서 추가
- 단계별 문서 개선
- 오류 처리 개선

### 스크립트

#### 벤치마크 내보내기 (`export_benchmark_markdown.py`)
- 엔드포인트 오버라이드 지원 추가
- 기본 모델 업데이트
- 함수 문서 개선
- 오류 처리 개선

#### CLI 린터 (`lint_markdown_cli.py`)
- SDK 참조 링크 추가
- 사용법 문서 개선

### 테스트

#### 스모크 테스트 (`smoke.py`)
- 엔드포인트 오버라이드 지원 추가
- 문서 개선
- 테스트 케이스 문서 개선
- 오류 보고 개선

## 환경 변수

모든 샘플은 다음 환경 변수를 지원합니다:

### 핵심 구성
- `FOUNDRY_LOCAL_ALIAS` - 사용할 모델 별칭 (샘플별 기본값 다름)
- `FOUNDRY_LOCAL_ENDPOINT` - 서비스 엔드포인트 오버라이드 (선택 사항)
- `SHOW_USAGE` - 토큰 사용 통계 표시 (기본값: "0")
- `RETRY_ON_FAIL` - 재시도 로직 활성화 (기본값: "1")
- `RETRY_BACKOFF` - 초기 재시도 지연 시간 (초) (기본값: "1.0")

### 샘플별
- `EMBED_MODEL` - RAG 샘플용 임베딩 모델
- `BENCH_MODELS` - 벤치마킹용 쉼표로 구분된 모델 목록
- `BENCH_ROUNDS` - 벤치마크 라운드 수
- `BENCH_PROMPT` - 벤치마크 테스트 프롬프트
- `BENCH_STREAM` - 첫 번째 토큰 지연 시간 측정
- `RAG_QUESTION` - RAG 샘플용 테스트 질문
- `AGENT_MODEL_PRIMARY` - 주요 에이전트 모델
- `AGENT_MODEL_EDITOR` - 에디터 에이전트 모델
- `SLM_ALIAS` - 소형 언어 모델 별칭
- `LLM_ALIAS` - 대형 언어 모델 별칭

## SDK 모범 사례 구현

### 1. 적절한 클라이언트 초기화
```python
# Old pattern
manager = FoundryLocalManager(alias)
client = OpenAI(base_url=manager.endpoint, api_key="not-needed")

# New pattern (with endpoint override)
manager = FoundryLocalManager(alias, endpoint=endpoint) if endpoint else FoundryLocalManager(alias)
client = OpenAI(
    base_url=manager.endpoint,
    api_key=manager.api_key or "not-needed"
)
```

### 2. 모델 정보 검색
```python
# Proper model ID resolution
model_info = manager.get_model_info(alias)
model_id = model_info.id
```

### 3. 오류 처리
```python
# Comprehensive error handling
try:
    manager = FoundryLocalManager(alias)
    # ... operations
except Exception as e:
    logger.error(f"Failed to initialize: {e}")
    raise RuntimeError(f"Initialization failed: {e}") from e
```

### 4. 지수적 백오프를 사용한 재시도 로직
```python
delay = initial_delay
for attempt in range(max_retries):
    try:
        # ... operation
        break
    except Exception:
        time.sleep(delay)
        delay *= 2  # Exponential backoff
```

### 5. 스트리밍 지원
```python
stream = client.chat.completions.create(
    model=model_id,
    messages=messages,
    stream=True,
    max_tokens=120
)
for chunk in stream:
    if chunk.choices and chunk.choices[0].delta:
        # Process chunk
```

## 사용자 정의 샘플 마이그레이션 가이드

새로운 샘플을 생성하거나 기존 샘플을 업데이트하려면:

1. **`workshop_utils.py` 헬퍼 사용**:
   ```python
   from workshop_utils import get_client, chat_once
   ```

2. **엔드포인트 오버라이드 지원**:
   ```python
   endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT")
   manager, client, model_id = get_client(alias, endpoint=endpoint)
   ```

3. **포괄적인 문서 추가**:
   - 환경 변수에 대한 docstring
   - SDK 참조 링크
   - 사용 예제

4. **타입 힌트 사용**:
   ```python
   from typing import Optional, List, Dict, Any
   ```

5. **적절한 오류 처리 구현**:
   ```python
   try:
       result = operation()
   except Exception as e:
       logger.error(f"Operation failed: {e}")
       raise
   ```

## 테스트

모든 샘플은 다음을 사용하여 테스트할 수 있습니다:

```bash
# Set environment variables
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Run individual samples
cd Workshop/samples
python -m session01.chat_bootstrap "Test question"
python -m session02.rag_pipeline

# Run benchmark
python -m session03.benchmark_oss_models

# Run smoke tests
python -m Workshop.tests.smoke
```

## SDK 문서 참조

- **메인 저장소**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **API 문서**: 최신 API 문서는 SDK 저장소에서 확인하세요

## 주요 변경 사항

### 예상 없음
모든 변경 사항은 이전 버전과 호환됩니다. 업데이트는 주로:
- 새로운 선택적 기능 추가 (엔드포인트 오버라이드)
- 오류 처리 개선
- 문서 개선
- 기본 모델 이름을 최신 권장 사항으로 업데이트

### 선택적 개선 사항
코드를 업데이트하여 다음을 사용할 수 있습니다:
- 명시적 엔드포인트 제어를 위한 `FOUNDRY_LOCAL_ENDPOINT`
- 토큰 사용 가시성을 위한 `SHOW_USAGE=1`
- 업데이트된 모델 기본값 (`phi-3.5-mini` 대신 `phi-4-mini`)

## 일반적인 문제 및 해결책

### 문제: "클라이언트 초기화 실패"
**해결책**: Foundry Local 서비스가 실행 중인지 확인:
```bash
foundry service start
foundry model run phi-4-mini
```

### 문제: "모델을 찾을 수 없음"
**해결책**: 사용 가능한 모델 확인:
```bash
foundry model list
```

### 문제: 엔드포인트 연결 오류
**해결책**: 엔드포인트 확인:
```bash
# Check service status
foundry service status

# Or set explicit endpoint
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000
```

## 다음 단계

1. **Module08 샘플 업데이트**: Module08/samples에 유사한 패턴 적용
2. **통합 테스트 추가**: 포괄적인 테스트 스위트 생성
3. **성능 벤치마킹**: 업데이트 전후 성능 비교
4. **문서 업데이트**: 새로운 패턴을 포함하여 메인 README 업데이트

## 기여 지침

새로운 샘플을 추가할 때:
1. 일관성을 위해 `workshop_utils.py` 사용
2. 기존 샘플의 패턴을 따름
3. 포괄적인 docstring 추가
4. SDK 참조 링크 포함
5. 엔드포인트 오버라이드 지원
6. 적절한 타입 힌트 추가
7. docstring에 사용 예제 포함

## 버전 호환성

이 업데이트는 다음과 호환됩니다:
- `foundry-local-sdk` (최신 버전)
- `openai>=1.30.0`
- Python 3.8+

---

**최종 업데이트**: 2025-01-08  
**담당자**: EdgeAI Workshop 팀  
**SDK 버전**: Foundry Local SDK (최신 0.7.117+67073234e7)

---

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있지만, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원본 문서의 원어 버전을 권위 있는 출처로 간주해야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 책임을 지지 않습니다.
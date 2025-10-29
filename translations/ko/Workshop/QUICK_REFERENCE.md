<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "93615ab69c8773b52c4437d537f6acea",
  "translation_date": "2025-10-28T20:59:30+00:00",
  "source_file": "Workshop/QUICK_REFERENCE.md",
  "language_code": "ko"
}
-->
# 워크숍 샘플 - 빠른 참조 카드

**최종 업데이트**: 2025년 10월 8일

---

## 🚀 빠른 시작

```bash
# 1. Ensure Foundry Local is running
foundry service status
foundry model run phi-4-mini

# 2. Install dependencies
pip install -r Workshop/requirements.txt

# 3. Run a sample
cd Workshop/samples
python -m session01.chat_bootstrap "What is edge AI?"
```

---

## 📂 샘플 개요

| 세션 | 샘플 | 목적 | 시간 |
|------|------|------|------|
| 01 | `chat_bootstrap.py` | 기본 채팅 + 스트리밍 | ~30초 |
| 02 | `rag_pipeline.py` | 임베딩을 활용한 RAG | ~45초 |
| 02 | `rag_eval_ragas.py` | RAG 평가 | ~60초 |
| 03 | `benchmark_oss_models.py` | 모델 벤치마킹 | ~2분 |
| 04 | `model_compare.py` | SLM vs LLM 비교 | ~45초 |
| 05 | `agents_orchestrator.py` | 다중 에이전트 시스템 | ~60초 |
| 06 | `models_router.py` | 의도 라우팅 | ~45초 |
| 06 | `models_pipeline.py` | 다단계 파이프라인 | ~60초 |

---

## 🛠️ 환경 변수

### 필수
```bash
# Choose model
set FOUNDRY_LOCAL_ALIAS=phi-4-mini

# Override endpoint (optional)
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Show token usage
set SHOW_USAGE=1
```

### 세션별
```bash
# Session 02: RAG
set RAG_QUESTION="What is local inference?"
set EMBED_MODEL=sentence-transformers/all-MiniLM-L6-v2

# Session 03: Benchmarking
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
set BENCH_ROUNDS=3
set BENCH_STREAM=1

# Session 04: Comparison
set SLM_ALIAS=phi-4-mini
set LLM_ALIAS=qwen2.5-7b

# Session 05: Agents
set AGENT_MODEL_PRIMARY=phi-4-mini
set AGENT_QUESTION="Why use edge AI?"

# Session 06: Pipeline
set PIPELINE_TASK="Your task here"
```

---

## ✅ 검증 및 테스트

```bash
# Validate syntax and imports
python scripts/validate_samples.py

# Validate specific session
python scripts/validate_samples.py --session 01

# Run smoke tests
python scripts/test_samples.py --quick

# Verbose testing
python scripts/test_samples.py --verbose
```

---

## 🐛 문제 해결

### 연결 오류
```bash
# Check Foundry Local
foundry service status

# Start if needed
foundry service start
foundry model run phi-4-mini
```

### 가져오기 오류
```bash
# Install missing dependencies
pip install sentence-transformers ragas datasets

# Or install all
pip install -r Workshop/requirements.txt
```

### 모델을 찾을 수 없음
```bash
# List available models
foundry model ls

# Download model
foundry model download phi-4-mini
```

### 느린 성능
```bash
# Use smaller model
set FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b

# Reduce benchmark rounds
set BENCH_ROUNDS=1
```

---

## 📖 일반적인 패턴

### 기본 채팅
```python
from workshop_utils import chat_once

text, usage = chat_once(
    'phi-4-mini',
    messages=[{"role": "user", "content": "Hello"}],
    max_tokens=100,
    temperature=0.7
)
```

### 클라이언트 가져오기
```python
from workshop_utils import get_client

manager, client, model_id = get_client(
    alias='phi-4-mini',
    endpoint=None  # Auto-detect
)
```

### 오류 처리
```python
try:
    manager, client, model_id = get_client(alias)
except Exception as e:
    print(f"[ERROR] Failed: {e}")
    print("[INFO] Check: foundry service status")
    sys.exit(1)
```

### 스트리밍
```python
stream = client.chat.completions.create(
    model=model_id,
    messages=messages,
    stream=True
)

for chunk in stream:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="", flush=True)
```

---

## 📊 모델 선택

| 모델 | 크기 | 적합한 용도 | 속도 |
|------|------|------------|------|
| `qwen2.5-0.5b` | 0.5B | 빠른 분류 | ⚡⚡⚡ |
| `qwen2.5-coder-0.5b` | 0.5B | 빠른 코드 생성 | ⚡⚡⚡ |
| `gemma-2-2b` | 2B | 창의적 글쓰기 | ⚡⚡ |
| `phi-3.5-mini` | 3.5B | 코드, 리팩토링 | ⚡⚡ |
| `phi-4-mini` | 4B | 일반 작업, 요약 | ⚡⚡ |
| `qwen2.5-7b` | 7B | 복잡한 추론 | ⚡ |

---

## 🔗 리소스

- **SDK 문서**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **빠른 참조**: `Workshop/FOUNDRY_SDK_QUICKREF.md`
- **업데이트 요약**: `Workshop/SAMPLES_UPDATE_SUMMARY.md`
- **마이그레이션 노트**: `Workshop/SDK_MIGRATION_NOTES.md`

---

## 💡 팁

1. **클라이언트 캐시 사용**: `workshop_utils`가 자동으로 캐시 처리
2. **작은 모델 사용**: 테스트 시 `qwen2.5-0.5b`로 시작
3. **사용 통계 활성화**: `SHOW_USAGE=1` 설정으로 토큰 추적
4. **배치 처리**: 여러 프롬프트를 순차적으로 처리
5. **max_tokens 줄이기**: 빠른 응답을 위해 지연 시간 감소

---

## 🎯 샘플 워크플로우

### 모든 항목 테스트
```bash
python scripts/validate_samples.py
python scripts/test_samples.py --quick
```

### 모델 벤치마킹
```bash
cd samples
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
set BENCH_ROUNDS=3
python -m session03.benchmark_oss_models
```

### RAG 파이프라인
```bash
cd samples
set RAG_QUESTION="What is RAG?"
python -m session02.rag_pipeline
```

### 다중 에이전트 시스템
```bash
cd samples
set AGENT_QUESTION="Why edge AI for healthcare?"
python -m session05.agents_orchestrator
```

---

**빠른 도움말**: `samples` 디렉토리에서 `--help`를 사용하거나 docstring을 확인하세요:
```bash
python -c "import session01.chat_bootstrap; help(session01.chat_bootstrap)"
```

---

**모든 샘플은 2025년 10월에 Foundry Local SDK 모범 사례로 업데이트되었습니다** ✨

---

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있지만, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원본 문서의 원어 버전을 권위 있는 출처로 간주해야 합니다. 중요한 정보에 대해서는 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 책임을 지지 않습니다.
<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "fd656d9068e1459dae855bd47075f2fb",
  "translation_date": "2025-10-28T20:56:05+00:00",
  "source_file": "Workshop/QUICK_START.md",
  "language_code": "ko"
}
-->
# 워크숍 빠른 시작 가이드

## 사전 준비

### 1. Foundry Local 설치

공식 설치 가이드를 따르세요:  
https://github.com/microsoft/Foundry-Local

```bash
# Start Foundry Local service
foundry service start

# Load a model (phi-4-mini recommended for workshop)
foundry model run phi-4-mini

# Verify service is running
foundry service status
```

### 2. Python 종속성 설치

워크숍 디렉토리에서 실행:

```bash
# Create virtual environment (recommended)
python -m venv .venv

# Activate virtual environment
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# Install requirements
pip install -r requirements.txt
```

## 워크숍 샘플 실행

### 세션 01: 기본 채팅

```bash
cd Workshop/samples
python -m session01.chat_bootstrap "What are the benefits of local AI?"
```

**환경 변수:**  
```bash
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
```

### 세션 02: RAG 파이프라인

```bash
cd Workshop/samples
python -m session02.rag_pipeline
```

**환경 변수:**  
```bash
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set RAG_QUESTION="Why use RAG with local inference?"
set EMBED_MODEL=sentence-transformers/all-MiniLM-L6-v2
```

### 세션 02: RAG 평가 (Ragas)

```bash
cd Workshop/samples
python -m session02.rag_eval_ragas
```

**참고**: `requirements.txt`를 통해 추가 종속성을 설치해야 합니다.

### 세션 03: 벤치마킹

```bash
cd Workshop/samples
python -m session03.benchmark_oss_models
```

**환경 변수:**  
```bash
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
set BENCH_ROUNDS=5
set BENCH_PROMPT="Explain RAG briefly"
set BENCH_STREAM=1
```

**출력**: 지연 시간, 처리량, 첫 번째 토큰 메트릭을 포함한 JSON

### 세션 04: 모델 비교

```bash
cd Workshop/samples
python -m session04.model_compare
```

**환경 변수:**  
```bash
set SLM_ALIAS=phi-4-mini
set LLM_ALIAS=qwen2.5-7b
set COMPARE_PROMPT="List 5 benefits of local AI inference"
```

### 세션 05: 다중 에이전트 오케스트레이션

```bash
cd Workshop/samples
python -m session05.agents_orchestrator
```

**환경 변수:**  
```bash
set AGENT_MODEL_PRIMARY=phi-4-mini
set AGENT_MODEL_EDITOR=phi-4-mini
set AGENT_QUESTION="Explain why edge AI matters for compliance"
```

### 세션 06: 모델 라우터

```bash
cd Workshop/samples
python -m session06.models_router
```

**라우팅 로직 테스트**: 여러 의도 (코드, 요약, 분류)

### 세션 06: 파이프라인

```bash
python -m session06.models_pipeline
```

**복잡한 다단계 파이프라인**: 계획, 실행, 수정 포함

## 스크립트

### 벤치마크 보고서 내보내기

```bash
cd Workshop/scripts
python export_benchmark_markdown.py \
    --models "phi-4-mini,qwen2.5-0.5b" \
    --prompt "Explain RAG briefly" \
    --rounds 3 \
    --output benchmark_report.md
```

**출력**: Markdown 테이블 + JSON 메트릭

### Markdown CLI 패턴 검사

```bash
python lint_markdown_cli.py --verbose
```

**목적**: 문서에서 사용되지 않는 CLI 패턴 감지

## 테스트

### 스모크 테스트

```bash
cd Workshop
python -m tests.smoke
```

**테스트**: 주요 샘플의 기본 기능

## 문제 해결

### 서비스가 실행되지 않음

```bash
# Check status
foundry service status

# Start if not running
foundry service start

# Load a model
foundry model run phi-4-mini
```

### 모듈 가져오기 오류

```bash
# Ensure virtual environment is activated
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux

# Reinstall dependencies
pip install -r requirements.txt
```

### 연결 오류

```bash
# Check endpoint
foundry service status

# Set explicit endpoint if needed
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000
```

### 모델을 찾을 수 없음

```bash
# List available models
foundry model list

# Download and run a model
foundry model run phi-4-mini
```

## 환경 변수 참조

### 핵심 구성
| 변수 | 기본값 | 설명 |
|------|--------|------|
| `FOUNDRY_LOCAL_ALIAS` | 다양함 | 사용할 모델 별칭 |
| `FOUNDRY_LOCAL_ENDPOINT` | 자동 | 서비스 엔드포인트 재정의 |
| `SHOW_USAGE` | `0` | 토큰 사용 통계 표시 |
| `RETRY_ON_FAIL` | `1` | 재시도 로직 활성화 |
| `RETRY_BACKOFF` | `1.0` | 초기 재시도 지연 시간 (초) |

### 세션별
| 변수 | 기본값 | 설명 |
|------|--------|------|
| `EMBED_MODEL` | `sentence-transformers/all-MiniLM-L6-v2` | 임베딩 모델 |
| `RAG_QUESTION` | 샘플 참조 | RAG 테스트 질문 |
| `BENCH_MODELS` | 다양함 | 쉼표로 구분된 모델 |
| `BENCH_ROUNDS` | `3` | 벤치마크 반복 횟수 |
| `BENCH_PROMPT` | 샘플 참조 | 벤치마크 프롬프트 |
| `BENCH_STREAM` | `0` | 첫 번째 토큰 지연 시간 측정 |
| `AGENT_MODEL_PRIMARY` | `phi-4-mini` | 주요 에이전트 모델 |
| `AGENT_MODEL_EDITOR` | 주요 | 편집기 에이전트 모델 |
| `SLM_ALIAS` | `phi-4-mini` | 소형 언어 모델 |
| `LLM_ALIAS` | `qwen2.5-7b` | 대형 언어 모델 |
| `COMPARE_PROMPT` | 샘플 참조 | 비교 프롬프트 |

## 추천 모델

### 개발 및 테스트
- **phi-4-mini** - 품질과 속도의 균형
- **qwen2.5-0.5b** - 분류에 매우 빠름
- **gemma-2-2b** - 양호한 품질, 적당한 속도

### 프로덕션 시나리오
- **phi-4-mini** - 일반 목적
- **deepseek-coder-1.3b** - 코드 생성
- **qwen2.5-7b** - 고품질 응답

## SDK 문서

- **Foundry Local**: https://github.com/microsoft/Foundry-Local  
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local  

## 도움 받기

1. 서비스 상태 확인: `foundry service status`  
2. 로그 보기: Foundry Local 서비스 로그 확인  
3. SDK 문서 확인: https://github.com/microsoft/Foundry-Local  
4. 샘플 코드 검토: 모든 샘플에 자세한 docstring 포함  

## 다음 단계

1. 모든 워크숍 세션을 순서대로 완료하세요.  
2. 다양한 모델을 실험해 보세요.  
3. 샘플을 수정하여 사용 사례에 맞게 조정하세요.  
4. 고급 패턴을 위해 `SDK_MIGRATION_NOTES.md`를 검토하세요.  

---

**최종 업데이트**: 2025-01-08  
**워크숍 버전**: 최신  
**SDK**: Foundry Local Python SDK  

---

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있지만, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원본 문서를 해당 언어로 작성된 권위 있는 자료로 간주해야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 책임을 지지 않습니다.
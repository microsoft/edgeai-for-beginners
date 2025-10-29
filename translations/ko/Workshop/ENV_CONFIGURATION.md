<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "da0a7a09670d5ab535141d121ea043fe",
  "translation_date": "2025-10-28T20:56:32+00:00",
  "source_file": "Workshop/ENV_CONFIGURATION.md",
  "language_code": "ko"
}
-->
# 환경 구성 가이드

## 개요

워크숍 샘플은 환경 변수를 사용하여 구성되며, 이는 저장소 루트에 있는 `.env` 파일에 중앙 집중화되어 있습니다. 이를 통해 코드를 수정하지 않고도 쉽게 사용자 정의가 가능합니다.

## 빠른 시작

### 1. 필수 조건 확인

```bash
# Check Foundry Local is installed
foundry --version

# Check service is running
foundry service status

# Load a model
foundry model run phi-4-mini
```

### 2. 환경 구성

`.env` 파일은 이미 적절한 기본값으로 구성되어 있습니다. 대부분의 사용자는 아무것도 변경할 필요가 없습니다.

**선택 사항**: 설정을 검토하고 사용자 정의:
```bash
# Edit .env file
notepad .env  # Windows
nano .env     # macOS/Linux
```

### 3. 구성 적용

**Python 스크립트의 경우:**
```bash
cd Workshop/samples
python -m session01.chat_bootstrap "Your question here"
# Environment variables automatically loaded
```

**노트북의 경우:**
```python
# Restart kernel after .env changes
# Variables are loaded when cells execute
```

## 환경 변수 참조

### 핵심 구성

| 변수 | 기본값 | 설명 |
|------|--------|------|
| `FOUNDRY_LOCAL_ALIAS` | `phi-4-mini` | 샘플의 기본 모델 |
| `FOUNDRY_LOCAL_ENDPOINT` | (비어 있음) | 서비스 엔드포인트 재정의 |
| `PYTHONPATH` | 워크숍 경로 | Python 모듈 검색 경로 |

**FOUNDRY_LOCAL_ENDPOINT를 설정해야 하는 경우:**
- 원격 Foundry Local 인스턴스
- 사용자 지정 포트 구성
- 개발/운영 환경 분리

**예시:**
```bash
# Local custom port
FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Remote instance
FOUNDRY_LOCAL_ENDPOINT=http://192.168.1.50:5273/v1
```

### 세션별 변수

#### 세션 02: RAG 파이프라인
| 변수 | 기본값 | 목적 |
|------|--------|------|
| `EMBED_MODEL` | `sentence-transformers/all-MiniLM-L6-v2` | 임베딩 모델 |
| `RAG_QUESTION` | 사전 구성됨 | 테스트 질문 |

#### 세션 03: 벤치마킹
| 변수 | 기본값 | 목적 |
|------|--------|------|
| `BENCH_MODELS` | `phi-4-mini,qwen2.5-0.5b` | 벤치마킹할 모델 |
| `BENCH_ROUNDS` | `3` | 모델당 반복 횟수 |
| `BENCH_PROMPT` | 사전 구성됨 | 테스트 프롬프트 |
| `BENCH_STREAM` | `0` | 첫 번째 토큰 지연 시간 측정 |

#### 세션 04: 모델 비교
| 변수 | 기본값 | 목적 |
|------|--------|------|
| `SLM_ALIAS` | `phi-4-mini` | 소형 언어 모델 |
| `LLM_ALIAS` | `qwen2.5-7b` | 대형 언어 모델 |
| `COMPARE_PROMPT` | 사전 구성됨 | 비교 프롬프트 |
| `COMPARE_RETRIES` | `2` | 재시도 횟수 |

#### 세션 05: 다중 에이전트 오케스트레이션
| 변수 | 기본값 | 목적 |
|------|--------|------|
| `AGENT_MODEL_PRIMARY` | `phi-4-mini` | 연구자 에이전트 모델 |
| `AGENT_MODEL_EDITOR` | `phi-4-mini` | 편집자 에이전트 모델 |
| `AGENT_QUESTION` | 사전 구성됨 | 테스트 질문 |

### 신뢰성 구성

| 변수 | 기본값 | 목적 |
|------|--------|------|
| `SHOW_USAGE` | `1` | 토큰 사용량 출력 |
| `RETRY_ON_FAIL` | `1` | 재시도 로직 활성화 |
| `RETRY_BACKOFF` | `1.0` | 재시도 지연 시간 (초) |

## 일반적인 구성

### 개발 환경 설정 (빠른 반복)
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=phi-4-mini
BENCH_MODELS=phi-4-mini
SHOW_USAGE=1
```

### 운영 환경 설정 (품질 중심)
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-7b
AGENT_MODEL_PRIMARY=phi-4-mini
AGENT_MODEL_EDITOR=qwen2.5-7b
SHOW_USAGE=0
```

### 벤치마킹 설정
```bash
BENCH_MODELS=phi-4-mini,qwen2.5-0.5b,qwen2.5-7b
BENCH_ROUNDS=5
BENCH_STREAM=1
```

### 다중 에이전트 특화
```bash
AGENT_MODEL_PRIMARY=phi-4-mini        # Fast for research
AGENT_MODEL_EDITOR=qwen2.5-7b         # Quality for editing
```

### 원격 개발
```bash
FOUNDRY_LOCAL_ENDPOINT=http://dev-server.local:5273/v1
FOUNDRY_LOCAL_ALIAS=phi-4-mini
```

## 추천 모델

### 사용 사례별

**일반 목적:**
- `phi-4-mini` - 품질과 속도의 균형

**빠른 응답:**
- `qwen2.5-0.5b` - 매우 빠르며 분류에 적합
- `phi-4-mini` - 빠르면서도 품질이 우수

**고품질:**
- `qwen2.5-7b` - 최고의 품질, 높은 자원 사용
- `phi-4-mini` - 우수한 품질, 낮은 자원 사용

**코드 생성:**
- `deepseek-coder-1.3b` - 코드에 특화됨
- `phi-4-mini` - 일반 목적 코딩

### 자원 가용성별

**저자원 (< 8GB RAM):**
```bash
FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b
SLM_ALIAS=qwen2.5-0.5b
LLM_ALIAS=phi-4-mini
```

**중간 자원 (8-16GB RAM):**
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-7b
```

**고자원 (16GB+ RAM):**
```bash
FOUNDRY_LOCAL_ALIAS=qwen2.5-7b
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-14b
```

## 고급 구성

### 사용자 정의 엔드포인트

```bash
# Development environment
FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Staging environment
FOUNDRY_LOCAL_ENDPOINT=http://staging.internal:5273/v1

# Production environment
FOUNDRY_LOCAL_ENDPOINT=http://prod.internal:5273/v1
```

### 온도 및 샘플링 (코드에서 재정의)

```python
# In your scripts/notebooks
os.environ['TEMPERATURE'] = '0.7'
os.environ['TOP_P'] = '0.9'
```

### Azure OpenAI 하이브리드 설정

```bash
# Use local for development
FOUNDRY_LOCAL_ALIAS=phi-4-mini

# Configure Azure for production fallback
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
AZURE_OPENAI_API_KEY=your-key-here
AZURE_OPENAI_API_VERSION=2024-08-01-preview
```

## 문제 해결

### 환경 변수가 로드되지 않음

**증상:**
- 스크립트가 잘못된 모델을 사용
- 연결 오류
- 변수가 인식되지 않음

**해결책:**
```bash
# 1. Verify .env exists in repository root
ls -la .env  # macOS/Linux
dir .env     # Windows

# 2. Check file is not .env.txt (Windows)
# Ensure no hidden extension

# 3. For notebooks: Restart kernel
# Kernel > Restart

# 4. For scripts: Check working directory
pwd  # Should be in Workshop or repository root
```

### 서비스 연결 문제

**증상:**
- "연결 거부" 오류
- "서비스를 사용할 수 없음"
- 시간 초과 오류

**해결책:**
```bash
# 1. Check service status
foundry service status

# 2. Start if not running
foundry service start

# 3. Verify endpoint
# Check port in status output
foundry service status | grep "Port"

# 4. Update .env if needed
FOUNDRY_LOCAL_ENDPOINT=http://localhost:<port>
```

### 모델을 찾을 수 없음

**증상:**
- "모델을 찾을 수 없음" 오류
- "별칭을 인식할 수 없음"

**해결책:**
```bash
# 1. List available models
foundry model list

# 2. Load required model
foundry model run phi-4-mini

# 3. Update .env with available model
FOUNDRY_LOCAL_ALIAS=<available-model>
```

### 가져오기 오류

**증상:**
- "모듈을 찾을 수 없음" 오류

**해결책:**

```bash
# 1. Activate virtual environment
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux

# 2. Install dependencies
pip install -r requirements.txt
```

## 구성 테스트

### 환경 로딩 확인

```python
# test_env.py
import os
from dotenv import load_dotenv

load_dotenv()

print("Core Configuration:")
print(f"  FOUNDRY_LOCAL_ALIAS: {os.getenv('FOUNDRY_LOCAL_ALIAS')}")
print(f"  FOUNDRY_LOCAL_ENDPOINT: {os.getenv('FOUNDRY_LOCAL_ENDPOINT') or 'auto'}")

print("\nSession 04:")
print(f"  SLM_ALIAS: {os.getenv('SLM_ALIAS')}")
print(f"  LLM_ALIAS: {os.getenv('LLM_ALIAS')}")

print("\nSession 05:")
print(f"  AGENT_MODEL_PRIMARY: {os.getenv('AGENT_MODEL_PRIMARY')}")
print(f"  AGENT_MODEL_EDITOR: {os.getenv('AGENT_MODEL_EDITOR')}")
```

### Foundry Local 연결 테스트

```python
# test_connection.py
import os
from foundry_local import FoundryLocalManager

alias = os.getenv('FOUNDRY_LOCAL_ALIAS', 'phi-4-mini')
endpoint = os.getenv('FOUNDRY_LOCAL_ENDPOINT')

try:
    if endpoint:
        manager = FoundryLocalManager(alias, endpoint=endpoint)
    else:
        manager = FoundryLocalManager(alias)
    
    print(f"✓ Connected to {manager.endpoint}")
    print(f"✓ Model: {manager.get_model_info(alias).id}")
    print(f"✓ Available models: {len(manager.list_models())}")
except Exception as e:
    print(f"✗ Connection failed: {e}")
```

## 보안 모범 사례

### 1. 비밀을 커밋하지 않기

```bash
# .gitignore should include:
.env
.env.local
*.key
```

### 2. 별도의 .env 파일 사용

```bash
.env              # Default configuration
.env.local        # Local overrides (gitignored)
.env.production   # Production config (secure storage)
```

### 3. API 키 주기적으로 변경

```bash
# For Azure OpenAI or other cloud services
# Regularly rotate keys and update .env
```

### 4. 환경별 구성 사용

```bash
# Development
FOUNDRY_LOCAL_ENDPOINT=http://localhost:5273/v1

# Production (use secrets management)
FOUNDRY_LOCAL_ENDPOINT=${PROD_FOUNDRY_ENDPOINT}
```

## SDK 문서

- **메인 저장소**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **API 문서**: 최신 정보는 SDK 저장소 확인

## 추가 자료

- `QUICK_START.md` - 시작 가이드
- `SDK_MIGRATION_NOTES.md` - SDK 업데이트 세부사항
- `Workshop/samples/*/README.md` - 샘플별 가이드

---

**최종 업데이트**: 2025-01-08  
**버전**: 2.0  
**SDK**: Foundry Local Python SDK (최신)

---

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있지만, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원본 문서의 원어 버전을 권위 있는 출처로 간주해야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 책임지지 않습니다.
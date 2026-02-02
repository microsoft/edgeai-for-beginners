# 워크숍 노트북 - 빠른 시작 가이드

## 목차

- [필수 조건](../../../../Workshop/notebooks)
- [초기 설정](../../../../Workshop/notebooks)
- [세션 04: 모델 비교](../../../../Workshop/notebooks)
- [세션 05: 멀티 에이전트 오케스트레이터](../../../../Workshop/notebooks)
- [세션 06: 의도 기반 모델 라우팅](../../../../Workshop/notebooks)
- [환경 변수](../../../../Workshop/notebooks)
- [공통 명령어](../../../../Workshop/notebooks)

---

## 필수 조건

### 1. Foundry Local 설치

**Windows:**
```bash
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
```

### 2. Python 종속성 설치

```bash
cd Workshop
pip install -r requirements.txt
```

개별적으로 설치하려면:
```bash
pip install foundry-local-sdk openai numpy requests
```

---

## 초기 설정

### Foundry Local 서비스 시작

**모든 노트북 실행 전에 필요:**

```bash
# Start the service
foundry service start

# Verify it's running
foundry service status
```

예상 출력:
```
✅ Service started successfully
Endpoint: http://localhost:59959
```

### 모델 다운로드 및 로드

노트북은 기본적으로 다음 모델을 사용합니다:

```bash
# Download models (first time only - may take several minutes)
foundry model download phi-4-mini
foundry model download qwen2.5-3b
foundry model download phi-3.5-mini
foundry model download qwen2.5-0.5b

# Load models into memory
foundry model run phi-4-mini
foundry model run qwen2.5-3b
foundry model run phi-3.5-mini
```

### 설정 확인

```bash
# List loaded models
foundry model ls

# Check service health
curl http://localhost:59959/v1/models
```

---

## 세션 04: 모델 비교

### 목적
소형 언어 모델(SLM)과 대형 언어 모델(LLM)의 성능을 비교합니다.

### 빠른 설정

```bash
# Start service (if not already running)
foundry service start

# Load required models
foundry model run phi-4-mini
foundry model run qwen2.5-3b
```

### 노트북 실행

1. VS Code 또는 Jupyter에서 `session04_model_compare.ipynb` **열기**
2. **커널 재시작** (커널 → 커널 재시작)
3. 모든 셀을 **순서대로 실행**

### 주요 설정

**기본 모델:**
- **SLM:** `phi-4-mini` (~4GB RAM, 빠름)
- **LLM:** `qwen2.5-3b` (~3GB RAM, 메모리 최적화)

**환경 변수 (선택 사항):**
```python
import os
os.environ['SLM_ALIAS'] = 'phi-4-mini'
os.environ['LLM_ALIAS'] = 'qwen2.5-3b'
os.environ['FOUNDRY_LOCAL_ENDPOINT'] = 'http://localhost:59959/v1'
```

### 예상 출력

```
================================================================================
COMPARISON SUMMARY
================================================================================
Alias                Latency(s)      Tokens     Route               
--------------------------------------------------------------------------------
phi-4-mini           1.234           150        chat.completions    
qwen2.5-3b           2.456           180        chat.completions    
================================================================================

💡 SLM is 1.99x faster than LLM for this prompt
```

### 사용자 정의

**다른 모델 사용:**
```python
os.environ['SLM_ALIAS'] = 'phi-3.5-mini'
os.environ['LLM_ALIAS'] = 'qwen2.5-1.5b'
```

**사용자 지정 프롬프트:**
```python
os.environ['COMPARE_PROMPT'] = 'Explain quantum computing in simple terms'
```

### 검증 체크리스트

- [ ] 셀 12에 올바른 모델 표시 (phi-4-mini, qwen2.5-3b)
- [ ] 셀 12에 올바른 엔드포인트 표시 (포트 59959)
- [ ] 셀 16 진단 통과 (✅ 서비스 실행 중)
- [ ] 셀 20 사전 점검 통과 (두 모델 모두 확인됨)
- [ ] 셀 22 비교 완료 및 지연 시간 값 표시
- [ ] 셀 24 검증 결과 🎉 모든 체크 통과!

### 소요 시간
- **첫 실행:** 5-10분 (모델 다운로드 포함)
- **추가 실행:** 1-2분

---

## 세션 05: 멀티 에이전트 오케스트레이터

### 목적
Foundry Local SDK를 사용하여 멀티 에이전트 협업을 시연 - 에이전트가 협력하여 정제된 결과를 생성합니다.

### 빠른 설정

```bash
# Start service
foundry service start

# Load models
foundry model run phi-4-mini  # Primary model
foundry model run qwen2.5-7b  # Optional: higher quality editor
```

### 노트북 실행

1. `session05_agents_orchestrator.ipynb` **열기**
2. **커널 재시작**
3. 모든 셀을 **순서대로 실행**

### 주요 설정

**기본 설정 (두 에이전트에 동일한 모델 사용):**
```python
PRIMARY_ALIAS = 'phi-4-mini'
EDITOR_ALIAS = 'phi-4-mini'  # Uses same model
```

**고급 설정 (다른 모델 사용):**
```python
import os
os.environ['AGENT_MODEL_PRIMARY'] = 'phi-4-mini'     # Fast for research
os.environ['AGENT_MODEL_EDITOR'] = 'qwen2.5-7b'      # High quality for editing
```

### 아키텍처

```
User Question
    ↓
Researcher Agent (phi-4-mini)
  → Gathers bullet points
    ↓
Editor Agent (phi-4-mini or qwen2.5-7b)
  → Refines into executive summary
    ↓
Final Output
```

### 예상 출력

```
================================================================================
[Pipeline] Question: Explain why edge AI matters for compliance.
================================================================================

[Stage 1: Research]
Output: • Edge AI processes data locally, reducing transmission...

[Stage 2: Editorial Refinement]
Output: Executive Summary: Edge AI enhances compliance by keeping data...

[FINAL OUTPUT]
Executive Summary: Edge AI enhances compliance by keeping sensitive data 
on-premises and reduces latency through local processing.

[METADATA]
Models used: {'researcher': 'phi-4-mini', 'editor': 'phi-4-mini'}
```

### 확장

**에이전트 추가:**
```python
critic = Agent(
    name='Critic',
    system='Review content for accuracy',
    client=client,
    model_id=model_id
)
```

**배치 테스트:**
```python
test_questions = [
    "What are benefits of local AI?",
    "How does RAG improve accuracy?",
]

for q in test_questions:
    result = pipeline(q, verbose=False)
    print(result['final'])
```

### 소요 시간
- **첫 실행:** 3-5분
- **추가 실행:** 질문당 1-2분

---

## 세션 06: 의도 기반 모델 라우팅

### 목적
감지된 의도에 따라 프롬프트를 전문화된 모델로 지능적으로 라우팅합니다.

### 빠른 설정

```bash
# Start service
foundry service start

# Load all routing models (CPU variants recommended)
foundry model run phi-4-mini-cpu
foundry model run qwen2.5-0.5b-cpu
foundry model run phi-3.5-mini-cpu
```

**참고:** 세션 06은 최대 호환성을 위해 기본적으로 CPU 모델을 사용합니다.

### 노트북 실행

1. `session06_models_router.ipynb` **열기**
2. **커널 재시작**
3. 모든 셀을 **순서대로 실행**

### 주요 설정

**기본 카탈로그 (CPU 모델):**
```python
CATALOG = {
    'phi-4-mini-cpu': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','refactor'],'priority':3},
}
```

**대안 (GPU 모델):**
```python
# Uncomment GPU catalog in Cell #6 if you have sufficient VRAM (8GB+)
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini': {'capabilities':['code','refactor'],'priority':3},
}
```

### 의도 감지

라우터는 정규 표현식 패턴을 사용하여 의도를 감지합니다:

| 의도 | 패턴 예시 | 라우팅 대상 |
|------|-----------|-------------|
| `code` | "refactor", "implement function" | phi-3.5-mini-cpu |
| `classification` | "categorize", "classify this" | qwen2.5-0.5b-cpu |
| `summarize` | "summarize", "tl;dr" | phi-4-mini-cpu |
| `general` | 기타 모든 것 | phi-4-mini-cpu |

### 예상 출력

```
✓ Using CPU-optimized models (default configuration)
  Models: phi-4-mini-cpu, qwen2.5-0.5b-cpu, phi-3.5-mini-cpu

Routing prompts to specialized models...
============================================================

Prompt: Refactor this Python function for readability
  Intent: code           | Model: phi-3.5-mini-cpu
  Output: Here's a refactored version...
  Tokens: 156

Prompt: Categorize this email as urgent or normal
  Intent: classification | Model: qwen2.5-0.5b-cpu
  Output: Category: Normal
  Tokens: 45

✓ Success! All prompts routed correctly.
```

### 사용자 정의

**사용자 지정 의도 추가:**
```python
import re

# Add to RULES
RULES.append((re.compile('translate|翻译', re.I), 'translation'))

# Add capability to catalog
CATALOG['phi-4-mini-cpu']['capabilities'].append('translation')
```

**토큰 추적 활성화:**
```python
import os
os.environ['SHOW_USAGE'] = '1'
```

### GPU 모델로 전환

8GB 이상의 VRAM이 있는 경우:

1. **셀 #6**에서 CPU 카탈로그 주석 처리
2. GPU 카탈로그 주석 해제
3. GPU 모델 로드:
   ```bash
   foundry model run phi-4-mini
   foundry model run qwen2.5-0.5b
   foundry model run phi-3.5-mini
   ```
4. 커널 재시작 및 노트북 재실행

### 소요 시간
- **첫 실행:** 5-10분 (모델 로드 포함)
- **추가 실행:** 테스트당 30-60초

---

## 환경 변수

### 글로벌 설정

Jupyter/VS Code 시작 전에 설정:

**Windows (명령 프롬프트):**
```cmd
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:59959/v1
set SHOW_USAGE=1
set RETRY_ON_FAIL=1
```

**Windows (PowerShell):**
```powershell
$env:FOUNDRY_LOCAL_ENDPOINT="http://localhost:59959/v1"
$env:SHOW_USAGE="1"
$env:RETRY_ON_FAIL="1"
```

**macOS/Linux:**
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://localhost:59959/v1
export SHOW_USAGE=1
export RETRY_ON_FAIL=1
```

### 노트북 내 설정

모든 노트북 시작 시 설정:

```python
import os

# Foundry Local configuration
os.environ['FOUNDRY_LOCAL_ENDPOINT'] = 'http://localhost:59959/v1'

# Model selection
os.environ['SLM_ALIAS'] = 'phi-4-mini'
os.environ['LLM_ALIAS'] = 'qwen2.5-3b'

# Agent models
os.environ['AGENT_MODEL_PRIMARY'] = 'phi-4-mini'
os.environ['AGENT_MODEL_EDITOR'] = 'qwen2.5-7b'

# Debugging
os.environ['SHOW_USAGE'] = '1'       # Show token usage
os.environ['RETRY_ON_FAIL'] = '1'    # Enable retries
os.environ['RETRY_BACKOFF'] = '2.0'  # Retry delay
```

---

## 공통 명령어

### 서비스 관리

```bash
# Start service
foundry service start

# Check status
foundry service status

# Stop service
foundry service stop

# View logs
foundry service logs
```

### 모델 관리

```bash
# List all available models in catalog
foundry model catalog

# List loaded models
foundry model ls

# Download a model
foundry model download phi-4-mini

# Load a model
foundry model run phi-4-mini

# Unload a model
foundry model unload phi-4-mini

# Remove a model
foundry model remove phi-4-mini

# Get model info
foundry model info phi-4-mini
```

### 엔드포인트 테스트

```bash
# Check service health
curl http://localhost:59959/health

# List available models via API
curl http://localhost:59959/v1/models

# Test model completion
curl http://localhost:59959/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "phi-4-mini",
    "messages": [{"role":"user","content":"Hello"}],
    "max_tokens": 50
  }'
```

### 진단 명령어

```bash
# Check everything
foundry --version
foundry service status
foundry model ls
foundry device info

# GPU status (NVIDIA)
nvidia-smi

# NPU status (Qualcomm)
foundry device info
```

---

## 모범 사례

### 모든 노트북 시작 전에

1. **서비스 실행 여부 확인:**
   ```bash
   foundry service status
   ```

2. **모델 로드 여부 확인:**
   ```bash
   foundry model ls
   ```

3. **노트북 커널 재시작** (재실행 시)

4. **모든 출력 지우기** (깨끗한 실행을 위해)

### 리소스 관리

1. **기본적으로 CPU 모델 사용** (호환성)
2. **GPU 모델로 전환** (8GB 이상의 VRAM이 있는 경우)
3. **다른 GPU 애플리케이션 닫기** (실행 전)
4. **서비스 유지 실행** (노트북 세션 간)
5. **리소스 사용량 모니터링** (작업 관리자 / nvidia-smi)

### 문제 해결

1. **코드 디버깅 전에 항상 서비스 확인**
2. **구성이 오래된 경우 커널 재시작**
3. **변경 후 진단 셀 재실행**
4. **모델 이름 확인** (로드된 모델과 일치)
5. **엔드포인트 포트 확인** (서비스 상태와 일치)

---

## 빠른 참조: 모델 별칭

### 일반 모델

| 별칭 | 크기 | 최적 용도 | RAM/VRAM | 변형 |
|------|------|-----------|----------|------|
| `phi-4-mini` | ~4B | 일반 채팅, 요약 | 4-6GB | `-cpu`, `-cuda-gpu`, `-npu` |
| `phi-3.5-mini` | ~3.5B | 코드 생성, 리팩토링 | 3-5GB | `-cpu`, `-cuda-gpu`, `-npu` |
| `qwen2.5-3b` | ~3B | 일반 작업, 효율적 | 3-4GB | `-cpu`, `-cuda-gpu` |
| `qwen2.5-1.5b` | ~1.5B | 빠르고 저자원 | 2-3GB | `-cpu`, `-cuda-gpu` |
| `qwen2.5-0.5b` | ~0.5B | 분류, 최소 자원 | 1-2GB | `-cpu`, `-cuda-gpu` |

### 변형 이름

- **기본 이름** (예: `phi-4-mini`): 하드웨어에 최적화된 변형 자동 선택
- **`-cpu`**: CPU 최적화, 모든 환경에서 작동
- **`-cuda-gpu`**: NVIDIA GPU 최적화, 8GB 이상의 VRAM 필요
- **`-npu`**: Qualcomm NPU 최적화, NPU 드라이버 필요

**추천:** 기본 이름(접미사 없이)을 사용하고 Foundry Local이 최적의 변형을 자동 선택하도록 설정.

---

## 성공 지표

준비 완료 상태:

✅ `foundry service status`가 "running" 표시
✅ `foundry model ls`가 필요한 모델 표시
✅ 서비스가 올바른 엔드포인트에서 접근 가능
✅ 상태 확인이 200 OK 반환
✅ 노트북 진단 셀이 통과
✅ 출력에 연결 오류 없음

---

## 도움 받기

### 문서
- **메인 저장소**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **CLI 참조**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-cli.md
- **문제 해결**: 이 디렉토리의 `troubleshooting.md` 참조

### GitHub 이슈
- https://github.com/microsoft/Foundry-Local/issues
- https://github.com/microsoft/edgeai-for-beginners/issues

---

**최종 업데이트:** 2025년 10월 8일  
**버전:** 워크숍 노트북 2.0

---

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있으나, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원본 문서의 원어 버전이 권위 있는 출처로 간주되어야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.
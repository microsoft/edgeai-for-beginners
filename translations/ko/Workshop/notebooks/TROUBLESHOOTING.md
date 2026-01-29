# 워크숍 노트북 - 문제 해결 가이드

## 목차

- [일반적인 문제와 해결책](../../../../Workshop/notebooks)
- [세션 04 특정 문제](../../../../Workshop/notebooks)
- [세션 05 특정 문제](../../../../Workshop/notebooks)
- [세션 06 특정 문제](../../../../Workshop/notebooks)
- [하드웨어 관련 문제](../../../../Workshop/notebooks)
- [진단 명령어](../../../../Workshop/notebooks)
- [도움 받기](../../../../Workshop/notebooks)

---

## 일반적인 문제와 해결책

### 🔴 CUDA 메모리 부족

**에러 메시지:**
```
CUDA failure 2: out of memory
```

**원인:** GPU의 VRAM이 부족하여 모델을 로드할 수 없습니다.

**해결책:**

#### 옵션 1: CPU 버전 사용 (권장)
```python
# In your notebook, update the CATALOG to use CPU variants
CATALOG = {
    'phi-4-mini-cpu': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','refactor'],'priority':3},
}
```

#### 옵션 2: GPU에서 더 작은 모델 사용
```python
# Use only the smallest model
CATALOG = {
    'qwen2.5-0.5b': {'capabilities':['general','code','summarize','classification'],'priority':1},
}
```

#### 옵션 3: GPU 메모리 정리
```bash
# Close other GPU-intensive applications
# Check GPU memory usage
nvidia-smi

# Restart Foundry Local service
foundry service stop
foundry service start
```

#### 옵션 4: GPU 메모리 늘리기 (가능한 경우)
- 브라우저 탭, 비디오 편집기 또는 기타 GPU 앱 닫기
- Windows 시각 효과 줄이기
- 통합 + 전용 GPU가 있는 경우 전용 GPU 사용

---

### 🔴 APIConnectionError: 연결 오류

**에러 메시지:**
```
APIConnectionError: Connection error
[Retry 1/2] Setup failed for 'phi-4-mini': APIConnectionError: Connection error.
```

**원인:** Foundry Local 서비스가 실행 중이 아니거나 접근할 수 없습니다.

**해결책:**

#### 단계 1: 서비스 상태 확인
```bash
foundry service status
```

#### 단계 2: 중지된 경우 서비스 시작
```bash
foundry service start
```

#### 단계 3: 엔드포인트 확인
```bash
# Check what port the service is using
foundry service status

# Test with curl (adjust port if different)
curl http://localhost:59959/health
curl http://localhost:55769/health
```

#### 단계 4: 필요한 모델 로드
```bash
foundry model run phi-4-mini
foundry model run qwen2.5-3b
foundry model run phi-3.5-mini
```

#### 단계 5: 노트북 커널 재시작
서비스를 시작하고 모델을 로드한 후, 노트북 커널을 재시작하고 모든 셀을 다시 실행하세요.

---

### 🔴 카탈로그에서 모델을 찾을 수 없음

**에러 메시지:**
```
ValueError: Model phi-3.5-mini-cpu not found in the catalog.
[ERROR] Model 'phi-4-mini' not found in the catalog
```

**원인:** 모델이 다운로드되거나 Foundry Local에 로드되지 않았습니다.

**해결책:**

#### 옵션 1: 모델 다운로드 및 로드
```bash
# List available models
foundry model ls

# Download the model if not present
foundry model download phi-4-mini
foundry model download qwen2.5-3b
foundry model download phi-3.5-mini

# Load the model into memory
foundry model run phi-4-mini
foundry model run qwen2.5-3b
foundry model run phi-3.5-mini
```

#### 옵션 2: 자동 선택 모드 사용
CATALOG를 기본 모델 이름(예: `-cpu` 접미사 없이)으로 업데이트하세요:

```python
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini': {'capabilities':['code','refactor'],'priority':3},
}
```

Foundry Local SDK가 하드웨어에 가장 적합한 버전(CPU, GPU 또는 NPU)을 자동으로 선택합니다.

---

### 🔴 HttpResponseError: 500 - 모델 로드 실패

**에러 메시지:**
```
HttpResponseError: 500 - Failed loading model
```

**원인:** 모델 파일이 손상되었거나 하드웨어와 호환되지 않습니다.

**해결책:**

#### 모델 다시 다운로드
```bash
# Remove corrupted model
foundry model remove phi-3.5-mini

# Download fresh copy
foundry model download phi-3.5-mini
```

#### 다른 버전 사용
```bash
# Try CPU variant instead
foundry model download phi-3.5-mini-cpu
```

---

### 🔴 ImportError: 모듈을 찾을 수 없음

**에러 메시지:**
```
ModuleNotFoundError: No module named 'foundry_local'
```

**원인:** foundry-local-sdk 패키지가 설치되지 않았습니다.

**해결책:**

```bash
# Install SDK
pip install foundry-local-sdk

# Verify installation
pip show foundry-local-sdk
python -c "from foundry_local import FoundryLocalManager; print('SDK OK')"
```

---

### � 첫 요청이 느림

**증상:** 첫 번째 요청이 30초 이상 걸리며, 이후 요청은 빠릅니다.

**원인:** 서비스가 첫 번째 요청 시 모델을 메모리에 로드하기 때문에 발생하는 정상적인 현상입니다.

**해결책:**

#### 모델 미리 로드
```bash
# Download and load all models you'll use before running notebooks
foundry model download phi-4-mini
foundry model download qwen2.5-3b
foundry model download phi-3.5-mini

foundry model run phi-4-mini
foundry model run qwen2.5-3b
```

#### 서비스 실행 유지
```bash
# Start service manually and leave it running
foundry service start
```

---

## 세션 04 특정 문제

### 잘못된 포트 설정

**문제:** 노트북이 잘못된 포트(55769, 59959, 57127 등)에 연결됨

**해결책:**

1. Foundry Local이 사용하는 포트를 확인하세요:
```bash
foundry service status
# Note the port number displayed
```

2. 노트북의 셀 10을 업데이트하세요:
```python
ENDPOINT = os.getenv('FOUNDRY_LOCAL_ENDPOINT', 'http://localhost:59959/v1')
# Replace 59959 with your actual port
```

3. 커널을 재시작하고 셀 6, 8, 10, 12, 16, 20, 22를 다시 실행하세요.

---

### 잘못된 모델 선택

**문제:** 노트북이 gpt-oss-20b 또는 qwen2.5-7b를 표시하며 qwen2.5-3b가 아님

**해결책:**

1. 노트북 커널을 재시작하세요 (이전 변수 상태를 초기화)
2. 셀 10을 다시 실행하세요 (모델 별칭 설정)
3. 셀 12를 다시 실행하세요 (구성 표시)
4. **확인:** 셀 12에 `LLM Model: qwen2.5-3b`가 표시되어야 합니다.

---

### 진단 셀이 실패함

**문제:** 셀 16에서 "❌ Foundry Local service not found!"가 표시됨

**해결책:**

1. 서비스가 실행 중인지 확인하세요:
```bash
foundry service status
```

2. 엔드포인트를 수동으로 테스트하세요:
```bash
curl http://localhost:59959/v1/models
```

3. curl이 작동하지만 노트북이 작동하지 않는 경우:
   - 노트북 커널을 재시작하세요.
   - 셀을 순서대로 다시 실행하세요: 6, 8, 10, 12, 14, 16

4. curl이 실패하는 경우:
   - 서비스 시작: `foundry service start`
   - 모델 로드: `foundry model run phi-4-mini` 및 `foundry model run qwen2.5-3b`

---

### 사전 점검 실패

**문제:** 셀 20에서 진단이 통과했음에도 연결 오류가 표시됨

**해결책:**

1. 모델이 로드되었는지 확인하세요:
```bash
foundry model ls
# Should show phi-4-mini and qwen2.5-3b
```

2. 모델이 누락된 경우:
```bash
foundry model run phi-4-mini
foundry model run qwen2.5-3b
```

3. 모델이 로드된 후 셀 20을 다시 실행하세요.

---

### 비교가 None 값으로 실패함

**문제:** 셀 22가 완료되지만 지연 시간이 None으로 표시됨

**해결책:**

1. 먼저 사전 점검이 통과했는지 확인하세요 (셀 20)
2. 셀 22를 다시 실행하세요 - 첫 요청 시 모델이 예열될 수 있습니다.
3. 두 모델이 모두 로드되었는지 확인하세요: `foundry model ls`

---

## 세션 05 특정 문제

### 에이전트가 잘못된 모델 사용

**문제:** 에이전트가 예상 모델을 사용하지 않음

**해결책:**

구성을 확인하세요:
```python
# Check which models are assigned
print(f"Researcher: {researcher.model_id}")
print(f"Editor: {editor.model_id}")
```

모델이 잘못된 경우 커널을 재시작하세요.

---

### 메모리 컨텍스트 초과

**문제:** 시간이 지남에 따라 에이전트 응답 품질이 저하됨

**해결책:** 이미 자동으로 처리됨 - 에이전트는 최근 6개의 메시지만 메모리에 유지합니다.

---

## 세션 06 특정 문제

### CPU와 GPU 모델 혼동

**문제:** 기본 설정을 사용할 때 CUDA 오류 발생

**해결책:** 기본 설정은 이제 CPU 모델을 사용합니다. CUDA 오류가 발생하면:

1. 기본 CPU 카탈로그를 사용 중인지 확인하세요:
```python
# Cell should show CPU variants
CATALOG = {
    'phi-4-mini-cpu': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','refactor'],'priority':3},
}
```

2. 커널을 재시작하고 모든 셀을 다시 실행하세요.

---

### 의도 감지가 작동하지 않음

**문제:** 프롬프트가 잘못된 모델로 라우팅됨

**해결책:**

의도 감지를 테스트하세요:
```python
# Run the intent detection test cell
for prompt in test_prompts:
    intent = detect_intent(prompt)
    print(f"{prompt[:50]}... → {intent}")
```

패턴이 조정이 필요하면 RULES를 업데이트하세요.

---

## 하드웨어 관련 문제

### NVIDIA GPU

**GPU 상태 확인:**
```bash
nvidia-smi
```

**일반적인 문제:**
- **드라이버가 오래됨**: NVIDIA 드라이버를 업데이트하세요.
- **CUDA 버전 불일치**: Foundry Local을 재설치하세요.
- **GPU 메모리 단편화**: 시스템을 재시작하세요.

### Qualcomm NPU

**NPU 상태 확인:**
```bash
foundry device info
```

**일반적인 문제:**
- **NPU 드라이버가 설치되지 않음**: Qualcomm NPU 드라이버를 설치하세요.
- **NPU 버전이 없음**: CPU 버전을 사용하세요.
- **Windows 버전이 너무 오래됨**: 최신 Windows 11로 업데이트하세요.

### CPU 전용 시스템

**권장 모델:**
```python
CATALOG = {
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','general'],'priority':2},
}
```

**성능 팁:**
- 가장 작은 모델 사용
- max_tokens 줄이기
- 첫 요청에 대한 대기 시간 증가

---

## 진단 명령어

### 모든 것 확인
```bash
# Service status
foundry service status

# List models
foundry model ls

# Device info
foundry device info

# Version info
foundry --version

# Health check
curl http://localhost:55769/health
```

### Python에서
```python
# Check SDK import
try:
    from foundry_local import FoundryLocalManager
    print('✓ SDK imported')
except ImportError as e:
    print(f'✗ SDK import failed: {e}')

# Check service connectivity
from openai import OpenAI

try:
    client = OpenAI(base_url='http://localhost:59959/v1', api_key='test')
    models = client.models.list()
    print(f'✓ Service reachable, {len(list(models.data))} models available')
except Exception as e:
    print(f'✗ Service not reachable: {e}')
```

---

## 도움 받기

### 1. 로그 확인
```bash
# Windows
foundry service logs

# Or check Windows Event Viewer
# Application Logs -> Microsoft-FoundryLocal
```

### 2. GitHub 이슈
- 기존 이슈 검색: https://github.com/microsoft/Foundry-Local/issues
- 새 이슈 생성 시 다음 정보 포함:
  - 에러 메시지 (전체 텍스트)
  - `foundry service status` 출력
  - `foundry --version` 출력
  - GPU/NPU 정보 (nvidia-smi 등)
  - 재현 단계

### 3. 문서
- **메인 저장소**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **CLI 참조**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-cli.md
- **문제 해결**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-troubleshooting.md

---

## 빠른 해결 체크리스트

문제가 발생하면 다음을 순서대로 시도하세요:

- [ ] 서비스가 실행 중인지 확인: `foundry service status`
- [ ] 서비스 재시작: `foundry service stop && foundry service start`
- [ ] 모델 존재 확인: `foundry model ls | grep phi-4-mini`
- [ ] 필요한 모델 로드: `foundry model run phi-4-mini`
- [ ] GPU 메모리 확인: `nvidia-smi` (NVIDIA인 경우)
- [ ] CPU 버전 시도: `phi-4-mini-cpu` 사용
- [ ] 노트북 커널 재시작
- [ ] 노트북 출력 지우고 모든 셀 다시 실행
- [ ] SDK 재설치: `pip install --upgrade --force-reinstall foundry-local-sdk`
- [ ] 시스템 재부팅 (최후의 수단)

---

## 예방 팁

### 모범 사례

1. **항상 먼저 서비스 확인:**
   ```bash
   foundry service status
   ```

2. **기본적으로 CPU 버전 사용:**
   ```python
   CATALOG = {
       'phi-4-mini-cpu': {...},
       'qwen2.5-0.5b-cpu': {...},
   }
   ```

3. **노트북 실행 전에 모델 미리 로드:**
   ```bash
   foundry model run phi-4-mini
   foundry model run qwen2.5-3b
   ```

4. **서비스 실행 유지:**
   - 서비스 불필요하게 중지/시작하지 않기
   - 세션 간 백그라운드에서 실행 유지

5. **리소스 모니터링:**
   - 실행 전에 GPU 메모리 확인
   - 불필요한 GPU 애플리케이션 닫기
   - 작업 관리자 / nvidia-smi 사용

6. **정기적으로 업데이트:**
   ```bash
   winget upgrade Microsoft.FoundryLocal
   pip install --upgrade foundry-local-sdk
   ```

---

**최종 업데이트:** 2025년 10월 8일

---

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있으나, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원본 문서의 원어 버전이 권위 있는 출처로 간주되어야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.
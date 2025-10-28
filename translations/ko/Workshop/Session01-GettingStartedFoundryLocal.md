<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0ab7d0dee137f224a011d9db00f0d2a2",
  "translation_date": "2025-10-28T17:16:34+00:00",
  "source_file": "Workshop/Session01-GettingStartedFoundryLocal.md",
  "language_code": "ko"
}
-->
# 세션 1: Foundry Local 시작하기

## 개요

Windows 11에서 Foundry Local을 설치하고 설정하며 여정을 시작하세요. CLI를 설정하고 하드웨어 가속을 활성화하며, 빠른 로컬 추론을 위해 모델을 캐시하는 방법을 배웁니다. 이 실습 세션에서는 Phi, Qwen, DeepSeek, GPT-OSS-20B와 같은 모델을 재현 가능한 CLI 명령을 사용하여 실행하는 과정을 안내합니다.

## 학습 목표

이 세션이 끝날 때까지 다음을 할 수 있습니다:

- **설치 및 설정**: Windows 11에서 Foundry Local을 최적의 성능 설정으로 설치 및 설정
- **CLI 작업 숙달**: Foundry Local CLI를 사용하여 모델 관리 및 배포
- **하드웨어 가속 활성화**: ONNXRuntime 또는 WebGPU를 사용하여 GPU 가속 설정
- **다중 모델 배포**: phi-4, GPT-OSS-20B, Qwen, DeepSeek 모델을 로컬에서 실행
- **첫 번째 앱 구축**: 기존 샘플을 Foundry Local Python SDK를 사용하도록 수정

# 모델 테스트 (비대화형 단일 프롬프트)
foundry model run phi-4-mini --prompt "안녕하세요, 자기소개 부탁드립니다"

- Windows 11 (22H2 이상)
# 사용 가능한 카탈로그 모델 목록 (실행된 모델은 실행 후 표시됨)
foundry model list
## NOTE: 현재 `--running` 플래그는 제공되지 않습니다; 로드된 모델을 확인하려면 채팅을 시작하거나 서비스 로그를 검사하세요.
- Python 3.10+ 설치됨
- Python 확장이 포함된 Visual Studio Code
- 설치를 위한 관리자 권한

### (선택 사항) 환경 변수

스크립트를 이동 가능하게 만들기 위해 `.env` 파일을 생성하거나 셸에서 설정:
# 응답 비교 (비대화형)
foundry model run gpt-oss-20b --prompt "엣지 AI를 간단히 설명해주세요"
| 변수 | 목적 | 예시 |
|------|------|------|
| `FOUNDRY_LOCAL_ALIAS` | 선호하는 모델 별칭 (카탈로그가 최적의 변형을 자동 선택) | `phi-3.5-mini` |
| `FOUNDRY_LOCAL_ENDPOINT` | 엔드포인트 재정의 (기본적으로 매니저에서 자동 설정) | `http://localhost:5273/v1` |
| `FOUNDRY_LOCAL_STREAM` | 스트리밍 데모 활성화 | `true` |

> `FOUNDRY_LOCAL_ENDPOINT=auto` (또는 설정되지 않음)인 경우 SDK 매니저에서 이를 유도합니다.

## 데모 흐름 (30분)

### 1. Foundry Local 설치 및 CLI 설정 확인 (10분)

# 캐시된 모델 목록
foundry cache list

```powershell
# Install via winget (recommended)
winget install Microsoft.FoundryLocal

# Or download from Microsoft Learn
# https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install
```

**macOS (미리보기 / 지원되는 경우)**

네이티브 macOS 패키지가 제공되는 경우 (최신 공식 문서를 확인):

```bash
# Homebrew (if/when available)
brew update
brew install foundry-local  # hypothetical formula name

# Or manual download (tarball)
curl -L -o foundry-local.tar.gz "https://download.microsoft.com/foundry-local/latest/macos/foundry-local.tar.gz"
tar -xzf foundry-local.tar.gz
sudo ./install.sh
```

macOS 네이티브 바이너리가 아직 제공되지 않는 경우, 다음을 수행할 수 있습니다:
1. Windows 11 ARM/Intel VM (Parallels / UTM)을 사용하고 Windows 단계를 따르세요.
2. 컨테이너를 통해 모델 실행 (컨테이너 이미지가 게시된 경우) 및 `FOUNDRY_LOCAL_ENDPOINT`를 노출된 포트로 설정.

**Python 가상 환경 생성 (크로스 플랫폼)**

Windows PowerShell:
```powershell
py -m venv .venv
 .\.venv\Scripts\Activate.ps1
```

macOS / Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

pip 업그레이드 및 핵심 종속성 설치:
```bash
python -m pip install --upgrade pip
pip install foundry-local-sdk openai
```

#### 단계 1.2: 설치 확인

```powershell
# Check version
foundry --version

# Initialize configuration
foundry init

# View available commands
foundry --help
```

#### 단계 1.3: 환경 설정

```powershell
# Set up Python environment for Module08
cd Module08
py -m venv .venv
.\.venv\Scripts\activate

# Install Foundry Local Python SDK and dependencies
pip install foundry-local-sdk openai requests
```

### SDK 부트스트래핑 (권장)

서비스를 수동으로 시작하고 모델을 실행하는 대신, **Foundry Local Python SDK**가 모든 것을 부트스트래핑할 수 있습니다:

```python
from foundry_local import FoundryLocalManager
from openai import OpenAI
import os

alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-3.5-mini")

# Bootstraps service + downloads + loads most suitable variant for hardware
manager = FoundryLocalManager(alias)

print("Service running:", manager.is_service_running())
print("Endpoint:", manager.endpoint)
print("Cached models:", manager.list_cached_models())

client = OpenAI(base_url=manager.endpoint, api_key=manager.api_key or "not-needed")

resp = client.chat.completions.create(
    model=manager.get_model_info(alias).id,
    messages=[
        {"role": "system", "content": "You are a helpful local assistant."},
        {"role": "user", "content": "Hello"}
    ],
    max_tokens=120,
    temperature=0.5
)
print(resp.choices[0].message.content)
```

명시적 제어를 선호하는 경우, 이후에 보여지는 CLI + OpenAI 클라이언트를 사용할 수 있습니다.

### 2. CLI를 통해 로컬에서 모델 실행 (10분)

#### 단계 3.1: Phi-4 모델 배포

```powershell
# Download and run phi-4-mini
foundry model run phi-4-mini

# Test the model (one-shot prompt)
foundry model run phi-4-mini --prompt "Hello, introduce yourself"

# NOTE: There is no `--running` flag; use `foundry model list` and recent activity to infer loaded models.
```

#### 단계 3.2: GPT-OSS-20B 배포

```powershell
# Download and run GPT-OSS-20B
foundry model run gpt-oss-20b

# Compare responses (one-shot prompt)
foundry model run gpt-oss-20b --prompt "Explain edge AI in simple terms"
```

#### 단계 3.3: 추가 모델 로드

```powershell
# Download Qwen model family
foundry model download qwen2.5-0.5b
foundry model download qwen2.5-7b

# Download DeepSeek models
foundry model download deepseek-coder-1.3b

# List cached models
foundry cache list
```

### 4. 시작 프로젝트: Foundry Local에 맞게 01-run-phi 수정 (5분)

#### 단계 4.1: 기본 채팅 애플리케이션 생성

`samples/01-foundry-quickstart/chat_quickstart.py` 생성 (가능하면 매니저를 사용하도록 업데이트):

```python
#!/usr/bin/env python3
"""
Foundry Local Chat Quickstart
Demo: Basic chat interaction using Foundry Local Python SDK
Reference: https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/reference/reference-sdk?pivots=programming-language-python
"""

import os, sys
from openai import OpenAI
try:
    from foundry_local import FoundryLocalManager  # control-plane SDK
except ImportError:
    FoundryLocalManager = None

def main():
    """Main chat function using Foundry Local SDK"""
    
    # Preferred: bootstrap via SDK manager (auto start + download + load)
    alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-3.5-mini")
    if FoundryLocalManager:
        manager = FoundryLocalManager(alias)
        endpoint = manager.endpoint
        model_id = manager.get_model_info(alias).id
        api_key = manager.api_key or "not-needed"
    else:
        # Fallback: assume default endpoint & alias already running via CLI
        endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT", "http://localhost:5273/v1")
        model_id = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-4-mini")
        api_key = "not-needed"

    client = OpenAI(base_url=endpoint, api_key=api_key)
    
    # Get user input
    if len(sys.argv) > 1:
        user_message = " ".join(sys.argv[1:])
    else:
        user_message = input("Enter your message: ")
    
    try:
        # Make chat completion request
        response = client.chat.completions.create(
            model=model_id,
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant powered by Microsoft Foundry Local."},
                {"role": "user", "content": user_message}
            ],
            max_tokens=500,
            temperature=0.7
        )
        
        # Display response
        print(f"\nModel: {response.model}")
        print(f"Response: {response.choices[0].message.content}")
        print(f"Tokens used: {response.usage.total_tokens if response.usage else 'N/A'}")
        
    except Exception as e:
        print(f"Error: {e}")
        print("\nTroubleshooting:")
    print("1. Ensure Foundry Local is running: foundry status")
    print("2. List models: foundry model list")
    print(f"3. Start model if needed: foundry model run {model_id}")
    print("4. Or let SDK bootstrap: pip install foundry-local-sdk")

if __name__ == "__main__":
    main()
```

#### 단계 4.2: 애플리케이션 테스트

```powershell
# Ensure phi-4-mini is running
foundry model run phi-4-mini

# Run the quickstart app
python samples/01-foundry-quickstart/chat_quickstart.py "What is Microsoft Foundry Local?"

# Try interactive mode
python samples/01-foundry-quickstart/chat_quickstart.py
```

## 주요 개념

### 1. Foundry Local 아키텍처

- **로컬 추론 엔진**: 모델을 완전히 장치에서 실행
- **OpenAI SDK 호환성**: 기존 OpenAI 코드와 원활한 통합
- **모델 관리**: 여러 모델을 효율적으로 다운로드, 캐시 및 실행
- **하드웨어 최적화**: GPU, NPU, CPU 가속 활용

### 2. CLI 명령 참조

```powershell
# Core Commands
foundry --version              # Check installation
# Model Management
foundry model list             # List available models
foundry model unload <name>    # Unload from memory

foundry config list            # Current configuration
```

### 3. Python SDK 통합

```python
# Basic client setup
from foundry_local import FoundryLocalManager
from openai import OpenAI
import os

alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-3.5-mini")
manager = FoundryLocalManager(alias)
client = OpenAI(base_url=manager.endpoint, api_key=manager.api_key or "not-needed")

response = client.chat.completions.create(
    model=manager.get_model_info(alias).id,
    messages=[{"role": "user", "content": "Hello!"}],
    max_tokens=50
)
print(response.choices[0].message.content)

# Streaming example
stream = client.chat.completions.create(
    model=manager.get_model_info(alias).id,
    messages=[{"role": "user", "content": "Give a 1-sentence definition of edge AI."}],
    stream=True,
    max_tokens=60,
    temperature=0.4
)
for chunk in stream:
    delta = chunk.choices[0].delta
    if delta and delta.content:
        print(delta.content, end="", flush=True)
print()
```

## 일반적인 문제 해결

### 문제 1: "Foundry 명령을 찾을 수 없음"

**해결 방법:**
```powershell
# Restart PowerShell after installation
# Or manually add to PATH
$env:PATH += ";C:\Program Files\Microsoft\FoundryLocal"
```

### 문제 2: "모델 로드 실패"

**해결 방법:**
```powershell
# Check available memory
foundry system info

# Try smaller model first
foundry model run phi-4-mini

# Check disk space for model cache
dir "$env:USERPROFILE\.foundry\models"
```

### 문제 3: "localhost:5273에서 연결 거부됨"

**해결 방법:**
```powershell
# Check if service is running
foundry status

# Start service if needed
foundry service start

# Check for port conflicts
netstat -an | findstr 5273
```

## 성능 최적화 팁

### 1. 모델 선택 전략

- **Phi-4-mini**: 일반 작업에 최적, 낮은 메모리 사용량
- **Qwen2.5-0.5b**: 가장 빠른 추론, 최소 자원 사용
- **GPT-OSS-20B**: 최고 품질, 더 많은 자원 필요
- **DeepSeek-Coder**: 프로그래밍 작업에 최적화

### 2. 하드웨어 최적화

```powershell
# Enable all acceleration options
foundry config set compute.onnx.enable_gpu true
foundry config set compute.webgpu.enabled true
foundry config set compute.cpu.threads auto

# Optimize memory usage
foundry config set model.cache.max_size 10GB
foundry config set model.preload false
```

### 3. 성능 모니터링

```powershell
# Performance & latency measurement
# Use the Python benchmark script (Session 3) instead of legacy 'model stats' or 'model benchmark' commands.
# Example:
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
python Workshop\samples\session03\benchmark_oss_models.py

# Re-run after enabling GPU acceleration to compare:
foundry config set compute.onnx.enable_gpu true
python Workshop\samples\session03\benchmark_oss_models.py
```

### 선택적 개선

| 개선 | 내용 | 방법 |
|------|------|------|
| 공유 유틸리티 | 중복 클라이언트/부트스트랩 로직 제거 | `Workshop/samples/workshop_utils.py` 사용 (`get_client`, `chat_once`) |
| 토큰 사용 가시성 | 비용/효율성 사고를 조기에 교육 | `SHOW_USAGE=1` 설정하여 프롬프트/완료/총 토큰 출력 |
| 결정론적 비교 | 안정적인 벤치마킹 및 회귀 검사 | `temperature=0`, `top_p=1`, 일관된 프롬프트 텍스트 사용 |
| 첫 번째 토큰 지연 | 인지된 응답성 메트릭 | 스트리밍을 사용하여 벤치마크 스크립트 수정 (`BENCH_STREAM=1`) |
| 일시적 오류 재시도 | 초기 시작 시 복원력 있는 데모 | `RETRY_ON_FAIL=1` (기본값) 및 `RETRY_BACKOFF` 조정 |
| 스모크 테스트 | 주요 흐름에 대한 빠른 점검 | 워크숍 전에 `python Workshop/tests/smoke.py` 실행 |
| 모델 별칭 프로필 | 기기 간 모델 세트 빠르게 전환 | `.env` 유지 (`FOUNDRY_LOCAL_ALIAS`, `SLM_ALIAS`, `LLM_ALIAS`) |
| 캐싱 효율성 | 다중 샘플 실행에서 반복된 웜업 방지 | 유틸리티 캐시 매니저; 스크립트/노트북 간 재사용 |
| 첫 실행 웜업 | p95 지연 스파이크 감소 | `FoundryLocalManager` 생성 후 작은 프롬프트 실행 |

결정론적 웜업 기준 예시 (PowerShell):

```powershell
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
python Workshop\samples\session01\chat_bootstrap.py "List two privacy benefits of local inference." | Out-Null
python Workshop\samples\session01\chat_bootstrap.py "List two privacy benefits of local inference."
```

두 번째 실행에서 유사한 출력 및 동일한 토큰 수를 확인할 수 있으며, 결정론이 확인됩니다.

## 다음 단계

이 세션을 완료한 후:

1. **세션 2 탐색**: Azure AI Foundry RAG를 사용하여 AI 솔루션 구축
2. **다양한 모델 시도**: Qwen, DeepSeek 및 기타 모델 패밀리 실험
3. **성능 최적화**: 특정 하드웨어에 맞게 설정 조정
4. **맞춤형 애플리케이션 구축**: Foundry Local SDK를 사용하여 자체 프로젝트 개발

## 추가 자료

### 문서
- [Foundry Local Python SDK 참조](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/reference/reference-sdk?pivots=programming-language-python)
- [Foundry Local 설치 가이드](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install)
- [모델 카탈로그](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/models)

### 샘플 코드
- [Module08 Sample 01](./samples/01/README.md) - REST 채팅 빠른 시작
- [Module08 Sample 02](./samples/02/README.md) - OpenAI SDK 통합
- [Module08 Sample 03](./samples/03/README.md) - 모델 탐색 및 벤치마킹

### 커뮤니티
- [Foundry Local GitHub Discussions](https://github.com/microsoft/Foundry-Local/discussions)
- [Azure AI 커뮤니티](https://techcommunity.microsoft.com/category/artificialintelligence)

---

**세션 시간**: 30분 실습 + 15분 Q&A  
**난이도**: 초급  
**사전 요구 사항**: Windows 11, Python 3.10+, 관리자 권한

## 샘플 시나리오 및 워크숍 매핑

| 워크숍 스크립트 / 노트북 | 시나리오 | 목표 | 예제 입력 | 필요한 데이터셋 |
|--------------------------|----------|------|----------|----------------|
| `samples/session01/chat_bootstrap.py` / `notebooks/session01_chat_bootstrap.ipynb` | 내부 IT 팀이 기기 내 추론을 평가하여 개인정보 보호 평가 포털을 위한 테스트 | 로컬 SLM이 표준 프롬프트에서 초단위 응답을 제공하는지 증명 | "로컬 추론의 두 가지 이점을 나열하세요." | 없음 (단일 프롬프트) |
| 빠른 시작 수정 코드 블록 | 기존 OpenAI 스크립트를 Foundry Local로 마이그레이션하는 개발자 | 드롭인 호환성 증명 | "로컬 추론의 두 가지 이점을 제공하세요." | 인라인 프롬프트만 |

### 시나리오 내러티브
보안 및 컴플라이언스 팀은 민감한 프로토타입 데이터를 로컬에서 처리할 수 있는지 검증해야 합니다. 이들은 부트스트랩 스크립트를 여러 프롬프트(개인정보 보호, 지연 시간, 비용)로 실행하며 결정론적 temperature=0 모드를 사용하여 나중에 비교를 위한 기본 출력을 캡처합니다 (세션 3 벤치마킹 및 세션 4 SLM vs LLM 대비).

### 최소 프롬프트 세트 JSON (선택 사항)
```json
[
    "List two benefits of local inference.",
    "Summarize why keeping data on device improves privacy.",
    "Give one trade‑off when choosing an SLM over a large model."
]
```

이 목록을 사용하여 재현 가능한 평가 루프를 생성하거나 향후 회귀 테스트 하네스를 시드하세요.

---

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있지만, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원본 문서를 해당 언어로 작성된 권위 있는 자료로 간주해야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 책임지지 않습니다.
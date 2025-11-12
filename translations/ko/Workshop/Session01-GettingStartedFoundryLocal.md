<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8c30436578b1bd604c48233ecdd39701",
  "translation_date": "2025-11-11T22:11:22+00:00",
  "source_file": "Workshop/Session01-GettingStartedFoundryLocal.md",
  "language_code": "ko"
}
-->
# 세션 1: Foundry Local 시작하기

## 개요

Microsoft Foundry Local을 사용하여 첫 번째 AI 모델을 설치, 구성 및 실행하는 방법을 배워보세요. 이 실습 세션에서는 설치부터 Phi-4, Qwen, DeepSeek와 같은 모델을 사용하여 첫 번째 채팅 애플리케이션을 구축하는 단계별 로컬 추론 과정을 소개합니다.

## 학습 목표

이 세션이 끝날 때까지 다음을 수행할 수 있습니다:

- **설치 및 구성**: Foundry Local을 설치하고 올바르게 설치되었는지 확인
- **CLI 작업 숙달**: Foundry Local CLI를 사용하여 모델 관리 및 배포
- **첫 번째 모델 실행**: 로컬 AI 모델을 성공적으로 배포하고 상호작용
- **채팅 앱 구축**: Foundry Local Python SDK를 사용하여 기본 채팅 애플리케이션 생성
- **로컬 AI 이해**: 로컬 추론 및 모델 관리의 기본 개념 파악

## 사전 요구 사항

### 시스템 요구 사항

- **Windows**: Windows 11 (22H2 이상) 또는 **macOS**: macOS 11+ (제한적 지원)
- **RAM**: 최소 8GB, 권장 16GB 이상
- **저장 공간**: 모델을 위한 10GB 이상의 여유 공간
- **Python**: 3.10 이상 설치
- **관리자 권한**: 설치를 위한 관리자 권한

### 개발 환경

- Python 확장이 포함된 Visual Studio Code (권장)
- 명령줄 액세스 (Windows에서는 PowerShell, macOS에서는 Terminal)
- Git을 사용한 리포지토리 클론 (선택 사항)

## 워크숍 흐름 (30분)

### 1단계: Foundry Local 설치 (5분)

#### Windows 설치

Windows 패키지 관리자를 사용하여 Foundry Local 설치:

```powershell
# Install via winget (recommended)
winget install Microsoft.FoundryLocal
```

대안: [Microsoft Learn](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install)에서 직접 다운로드

#### macOS 설치 (제한적 지원)

> [!NOTE]  
> macOS 지원은 현재 미리보기 상태입니다. 최신 가용성을 확인하려면 공식 문서를 참조하세요.

Homebrew를 사용하여 설치:

```bash
# If Homebrew formula is available
brew update
brew install foundry-local

# Or manual download (check official docs for latest)
curl -L -o foundry-local.tar.gz "https://download.microsoft.com/foundry-local/latest/macos/foundry-local.tar.gz"
tar -xzf foundry-local.tar.gz
sudo ./install.sh
```

**macOS 사용자 대안:**
- Windows 11 VM (Parallels/UTM)을 사용하고 Windows 단계를 따르세요
- 컨테이너를 사용하여 실행 가능하며 `FOUNDRY_LOCAL_ENDPOINT`를 구성

### 2단계: 설치 확인 (3분)

설치 후 터미널을 다시 시작하고 Foundry Local이 작동하는지 확인:

```powershell
# Check if Foundry Local is installed correctly
foundry --version

# View available commands
foundry --help
```

예상 출력은 버전 정보와 사용 가능한 명령을 표시해야 합니다.

### 3단계: Python 환경 설정 (5분)

이 워크숍을 위한 전용 Python 환경 생성:

**Windows:**
```powershell
# Create virtual environment
py -m venv .venv

# Activate environment
.\.venv\Scripts\Activate.ps1

# Upgrade pip and install dependencies
python -m pip install --upgrade pip
pip install foundry-local-sdk openai
```

**macOS/Linux:**
```bash
# Create virtual environment
python3 -m venv .venv

# Activate environment
source .venv/bin/activate

# Upgrade pip and install dependencies
python -m pip install --upgrade pip
pip install foundry-local-sdk openai
```


### 4단계: 첫 번째 모델 실행 (7분)

이제 첫 번째 AI 모델을 로컬에서 실행해 봅시다!

#### Phi-4 Mini로 시작 (추천 첫 모델)

```powershell
# Download and start phi-4-mini (lightweight, fast)
foundry model run phi-4-mini

# Test the model with a simple prompt
foundry model run phi-4-mini --prompt "Hello, introduce yourself in one sentence"
```

> [!TIP]  
> 이 명령은 모델을 다운로드(첫 실행 시)하고 Foundry Local 서비스를 자동으로 시작합니다.

#### 실행 중인 항목 확인

```powershell
# List available models (shows downloaded models)
foundry model list

# Check service status
foundry service status

# See what models are cached locally
foundry cache list
```


#### 다른 모델 시도

phi-4-mini가 작동하면 다른 모델을 실험해 보세요:

```powershell
# Larger model with better capabilities
foundry model run gpt-oss-20b --prompt "Explain edge AI in simple terms"

# Fast, efficient model
foundry model run qwen2.5-0.5b --prompt "What are the benefits of local AI inference?"
```


### 5단계: 첫 번째 채팅 애플리케이션 구축 (10분)

이제 방금 시작한 모델을 사용하는 Python 애플리케이션을 만들어 봅시다.

#### 채팅 스크립트 생성

`my_first_chat.py`라는 새 파일을 생성하거나 제공된 샘플을 사용하세요:

```python
#!/usr/bin/env python3
"""
My First Foundry Local Chat Application
Using FoundryLocalManager for automatic service management
"""

import os
from foundry_local import FoundryLocalManager
from openai import OpenAI

def main():
    # Get model alias from environment or use default
    alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-4-mini")
    
    try:
        # Initialize Foundry Local Manager (auto-starts service, downloads model)
        manager = FoundryLocalManager(alias)
        
        # Create OpenAI client pointing to local endpoint
        client = OpenAI(
            base_url=manager.endpoint,
            api_key=manager.api_key or "not-needed"
        )
        
        # Get the actual model ID for this alias
        model_id = manager.get_model_info(alias).id
        
        print("🤖 Welcome to your first local AI chat!")
        print(f"� Using model: {alias} -> {model_id}")
        print(f"🌐 Endpoint: {manager.endpoint}")
        print("�💡 Type 'quit' to exit\n")
        
    except Exception as e:
        print(f"❌ Failed to initialize Foundry Local: {e}")
        print("💡 Make sure Foundry Local is installed: foundry --version")
        return
    
    while True:
        # Get user input
        user_message = input("You: ").strip()
        
        if user_message.lower() in ['quit', 'exit', 'bye']:
            print("👋 Goodbye!")
            break
            
        if not user_message:
            continue
            
        try:
            # Send message to local AI model
            response = client.chat.completions.create(
                model=model_id,
                messages=[
                    {"role": "system", "content": "You are a helpful AI assistant running locally."},
                    {"role": "user", "content": user_message}
                ],
                max_tokens=200,
                temperature=0.7
            )
            
            # Display the response
            ai_response = response.choices[0].message.content
            print(f"🤖 AI: {ai_response}\n")
            
        except Exception as e:
            print(f"❌ Error: {e}")
            print("💡 Check service status: foundry service status\n")

if __name__ == "__main__":
    main()
```

> [!TIP]  
> **관련 예제**: 더 고급 사용법은 다음을 참조하세요:
>
> - **Python 샘플**: `Workshop/samples/session01/chat_bootstrap.py` - 스트리밍 응답 및 오류 처리 포함
> - **Jupyter Notebook**: `Workshop/notebooks/session01_chat_bootstrap.ipynb` - 상세 설명이 포함된 인터랙티브 버전

#### 채팅 애플리케이션 테스트

```powershell
# No need to manually start models - FoundryLocalManager handles this!
# Just run your chat application
python my_first_chat.py
```

대안: 제공된 샘플을 직접 사용

```powershell
# Try the complete sample with streaming support
cd Workshop/samples
python -m session01.chat_bootstrap "Your question here"
```

또는 인터랙티브 노트북 탐색  
Workshop/notebooks/session01_chat_bootstrap.ipynb를 VS Code에서 열기

다음 예제 대화를 시도해 보세요:

- "Microsoft Foundry Local이 무엇인가요?"
- "AI 모델을 로컬에서 실행하는 3가지 이점을 나열하세요"
- "엣지 AI에 대해 이해를 돕는 설명을 해주세요"

## 달성한 내용

축하합니다! 성공적으로:

1. ✅ **Foundry Local 설치** 및 작동 확인
2. ✅ **첫 번째 AI 모델**(phi-4-mini)을 로컬에서 시작
3. ✅ **다양한 모델 테스트** 명령줄을 통해
4. ✅ **채팅 애플리케이션 구축** 로컬 AI에 연결
5. ✅ **클라우드 의존성 없이 로컬 AI 추론 경험**

## 이해한 내용

### 로컬 AI 추론

- AI 모델이 완전히 컴퓨터에서 실행됩니다
- 데이터가 클라우드로 전송되지 않습니다
- 응답은 CPU/GPU를 사용하여 로컬에서 생성됩니다
- 개인정보 및 보안이 유지됩니다

### 모델 관리

- `foundry model run`은 모델을 다운로드하고 시작합니다
- **FoundryLocalManager SDK**는 서비스 시작 및 모델 로딩을 자동으로 처리합니다
- 모델은 향후 사용을 위해 로컬에 캐시됩니다
- 여러 모델을 다운로드할 수 있지만 일반적으로 한 번에 하나만 실행됩니다
- 서비스는 자동으로 모델 수명을 관리합니다

### SDK vs CLI 접근 방식

- **CLI 접근 방식**: `foundry model run <model>`을 사용한 수동 모델 관리
- **SDK 접근 방식**: `FoundryLocalManager(alias)`를 사용한 자동 서비스 및 모델 관리
- **추천**: 애플리케이션에는 SDK를, 테스트 및 탐색에는 CLI를 사용하세요

## 주요 명령어 참조

### 필수 CLI 명령어

```powershell
# Installation & Setup
foundry --version              # Check installation
foundry --help                 # View all commands

# Model Management
foundry model list             # List available models
foundry model run <model>      # Download and start a model
foundry model run <model> --prompt "text"  # One-shot prompt
foundry cache list             # Show downloaded models

# Service Management
foundry service status         # Check if service is running
foundry service start          # Start the service manually
foundry service stop           # Stop the service
```


### 모델 추천

- **phi-4-mini**: 초보자에게 적합 - 빠르고 가벼우며 품질이 우수
- **qwen2.5-0.5b**: 가장 빠른 추론, 최소 메모리 사용
- **gpt-oss-20b**: 높은 품질의 응답, 더 많은 리소스 필요
- **deepseek-coder-1.3b**: 프로그래밍 및 코드 작업에 최적화

## 문제 해결

### "Foundry 명령을 찾을 수 없음"

**해결 방법:**

```powershell
# Restart your terminal after installation
# Or manually add to PATH (Windows)
$env:PATH += ";C:\Program Files\Microsoft\FoundryLocal"
```


### "모델 로드 실패"

**해결 방법:**

```powershell
# Check available system memory
foundry service status

# Try a smaller model first
foundry model run phi-4-mini

# Check disk space for model downloads
# Models are stored in: %USERPROFILE%\.foundry\models (Windows)
```


### "localhost에서 연결 거부됨"

**해결 방법:**

```powershell
# Check if service is running
foundry service status

# Start service if needed
foundry service start

# Verify the port (default is 5273)
# Check for port conflicts with: netstat -an | findstr 5273
```


## 다음 단계

### 즉각적인 다음 작업

1. **다양한 모델과 프롬프트 실험**
2. **채팅 애플리케이션 수정**하여 다른 모델 시도
3. **자신만의 프롬프트 생성** 및 응답 테스트
4. **세션 2 탐색**: RAG 애플리케이션 구축

### 고급 학습 경로

1. **세션 2**: RAG (Retrieval-Augmented Generation)를 활용한 AI 솔루션 구축
2. **세션 3**: 다양한 오픈소스 모델 비교
3. **세션 4**: 최첨단 모델 작업
4. **세션 5**: 다중 에이전트 AI 시스템 구축

## 환경 변수 (선택 사항)

더 고급 사용을 위해 다음 환경 변수를 설정할 수 있습니다:

| 변수 | 목적 | 예시 |
|------|------|------|
| `FOUNDRY_LOCAL_ALIAS` | 사용할 기본 모델 | `phi-4-mini` |
| `FOUNDRY_LOCAL_ENDPOINT` | 엔드포인트 URL 재정의 | `http://localhost:5273/v1` |

프로젝트 디렉터리에 `.env` 파일 생성:
```
FOUNDRY_LOCAL_ALIAS=phi-4-mini
FOUNDRY_LOCAL_ENDPOINT=auto
```


## 추가 자료

### 문서

- [Foundry Local Python SDK 참조](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/reference/reference-sdk?pivots=programming-language-python)
- [Foundry Local 설치 가이드](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install)
- [모델 카탈로그](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/models)

### 샘플 코드

- **Session01 Python Sample**: `Workshop/samples/session01/chat_bootstrap.py` - 스트리밍이 포함된 완전한 채팅 앱
- **Session01 Notebook**: `Workshop/notebooks/session01_chat_bootstrap.ipynb` - 인터랙티브 튜토리얼  
- [Module08 Sample 01](../Module08/samples/01/README.md) - REST 채팅 빠른 시작
- [Module08 Sample 02](../Module08/samples/02/README.md) - OpenAI SDK 통합
- [Module08 Sample 03](../Module08/samples/03/README.md) - 모델 탐색 및 벤치마킹

### 커뮤니티

- [Foundry Local GitHub Discussions](https://github.com/microsoft/Foundry-Local/discussions)
- [Azure AI 커뮤니티](https://techcommunity.microsoft.com/category/artificialintelligence)

---

**세션 시간**: 실습 30분 + Q&A 15분  
**난이도**: 초급  
**사전 요구 사항**: Windows 11/macOS 11+, Python 3.10+, 관리자 권한

## 워크숍 예제 시나리오

### 실제 사례

**시나리오**: 기업 IT 팀이 민감한 직원 피드백을 외부 서비스로 데이터를 전송하지 않고 처리하기 위해 디바이스 내 AI 추론을 평가해야 합니다.

**목표**: 로컬 AI 모델이 데이터 프라이버시를 완전히 유지하면서 초 단위의 지연 시간으로 품질 높은 응답을 제공할 수 있음을 입증하세요.

### 테스트 프롬프트

다음 프롬프트를 사용하여 설정을 검증하세요:

```json
[
    "List two benefits of local inference.",
    "Summarize why keeping data on device improves privacy.",
    "Give one trade-off when choosing a small model over a large model."
]
```


### 성공 기준

- ✅ 모든 프롬프트가 2초 이내에 응답을 받음
- ✅ 데이터가 로컬 컴퓨터를 벗어나지 않음
- ✅ 응답이 관련성 있고 유용함
- ✅ 채팅 애플리케이션이 원활하게 작동함

이 검증은 세션 2-6의 고급 워크숍을 위한 Foundry Local 설정이 준비되었음을 보장합니다.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있지만, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원본 문서의 원어 버전을 권위 있는 출처로 간주해야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 책임을 지지 않습니다.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
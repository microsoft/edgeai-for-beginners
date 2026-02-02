# Sample 01: OpenAI SDK를 활용한 빠른 채팅

Microsoft Foundry Local을 사용하여 로컬 AI 추론을 수행하는 OpenAI SDK 사용법을 보여주는 간단한 채팅 예제입니다.

## 개요

이 샘플에서는 다음을 보여줍니다:
- Foundry Local과 함께 OpenAI Python SDK 사용
- Azure OpenAI 및 로컬 Foundry 설정 처리
- 적절한 오류 처리 및 대체 전략 구현
- 서비스 관리를 위한 FoundryLocalManager 사용

## 사전 요구 사항

- **Foundry Local**: 설치되어 PATH에 추가됨
- **Python**: 3.8 이상
- **모델**: Foundry Local에 로드된 모델(예: `phi-4-mini`)

## 설치

1. **Python 환경 설정:**
   ```cmd
   cd Module08
   py -m venv .venv
   .venv\Scripts\activate
   ```

2. **종속성 설치:**
   ```cmd
   pip install -r requirements.txt
   ```

3. **Foundry Local 서비스 시작 및 모델 로드:**
   ```cmd
   foundry model run phi-4-mini
   ```


## 사용법

### Foundry Local (기본 설정)

```cmd
# Using FoundryLocalManager (recommended)
python samples\01\chat_quickstart.py "Explain what Foundry Local is"

# Using manual configuration
set BASE_URL=http://localhost:8000
set MODEL=phi-4-mini
set API_KEY=
python samples\01\chat_quickstart.py "Write a welcome message"
```

### Azure OpenAI

```cmd
set AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
set AZURE_OPENAI_API_KEY=your-api-key
set AZURE_OPENAI_API_VERSION=2024-08-01-preview
set MODEL=your-deployment-name
python samples\01\chat_quickstart.py "Hello from Azure OpenAI"
```


## 코드 기능

### FoundryLocalManager 통합

이 샘플은 서비스 관리를 위해 공식 Foundry Local SDK를 사용합니다:

```python
from foundry_local import FoundryLocalManager
from openai import OpenAI

# Initialize Foundry Local
manager = FoundryLocalManager(alias)
model_info = manager.get_model_info(alias)

# Configure OpenAI client
client = OpenAI(
    base_url=manager.endpoint,
    api_key=manager.api_key
)
```


### 오류 처리

SDK가 사용 불가능한 경우 수동 설정으로 대체하는 강력한 오류 처리:
- 자동 서비스 검색
- SDK가 없을 경우 점진적 저하 처리
- 문제 해결을 위한 명확한 오류 메시지 제공

## 환경 변수

| 변수 | 설명 | 기본값 | 필수 여부 |
|------|------|--------|-----------|
| `MODEL` | 모델 별칭 또는 이름 | `phi-4-mini` | 아니요 |
| `BASE_URL` | Foundry Local 기본 URL | `http://localhost:8000` | 아니요 |
| `API_KEY` | API 키(로컬에서는 일반적으로 필요 없음) | `""` | 아니요 |
| `AZURE_OPENAI_ENDPOINT` | Azure OpenAI 엔드포인트 | - | Azure용 |
| `AZURE_OPENAI_API_KEY` | Azure OpenAI API 키 | - | Azure용 |
| `AZURE_OPENAI_API_VERSION` | Azure API 버전 | `2024-08-01-preview` | 아니요 |

## 문제 해결

### 일반적인 문제

1. **"Foundry SDK를 사용할 수 없습니다" 경고:**
   - Foundry Local SDK 설치: `pip install foundry-local-sdk`
   - 또는 수동 설정을 위한 환경 변수 설정

2. **연결 거부됨:**
   - Foundry Local이 실행 중인지 확인: `foundry service status`
   - 모델이 로드되었는지 확인: `foundry service ps`

3. **모델을 찾을 수 없음:**
   - 사용 가능한 모델 목록 확인: `foundry model list`
   - 모델 로드: `foundry model run phi-4-mini`

### 검증

```cmd
# Check Foundry Local status
foundry service status

# List loaded models
foundry service ps

# Test API endpoint
curl http://localhost:8000/v1/models
```


## 참고 자료

- [Foundry Local 문서](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [OpenAI Python SDK](https://github.com/openai/openai-python)
- [Foundry Local GitHub](https://github.com/microsoft/Foundry-Local)
- [OpenAI 호환 API 참조](https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks)

---


# 샘플 02: OpenAI SDK 통합

Microsoft Foundry Local과 Azure OpenAI를 지원하며 스트리밍 응답과 적절한 오류 처리를 포함한 OpenAI Python SDK의 고급 통합을 보여줍니다.

## 개요

이 샘플은 다음을 보여줍니다:
- Foundry Local과 Azure OpenAI 간의 원활한 전환
- 사용자 경험을 개선하기 위한 스트리밍 채팅 응답
- FoundryLocalManager SDK의 적절한 사용
- 견고한 오류 처리 및 대체 메커니즘
- 프로덕션 준비 코드 패턴

## 사전 요구사항

- **Foundry Local**: 설치 및 실행 중 (로컬 추론용)
- **Python**: OpenAI SDK가 포함된 3.8 이상
- **Azure OpenAI**: 유효한 엔드포인트 및 API 키 (클라우드 추론용)

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

3. **Foundry Local 시작 (로컬 모드용):**
   ```cmd
   foundry model run phi-4-mini
   ```


## 사용 시나리오

### Foundry Local (기본값)

**옵션 1: FoundryLocalManager 사용 (권장)**
```cmd
# Automatic service discovery and model management
set MODEL=phi-4-mini
python samples\02\sdk_quickstart.py
```

**옵션 2: 수동 구성**
```cmd
# Manual endpoint configuration
set BASE_URL=http://localhost:8000
set MODEL=phi-4-mini
set API_KEY=
python samples\02\sdk_quickstart.py
```


### Azure OpenAI

```cmd
# Azure OpenAI configuration
set AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
set AZURE_OPENAI_API_KEY=your-api-key
set AZURE_OPENAI_API_VERSION=2024-08-01-preview
set MODEL=your-deployment-name
python samples\02\sdk_quickstart.py
```


## 코드 아키텍처

### 클라이언트 팩토리 패턴

이 샘플은 적절한 클라이언트를 생성하기 위해 팩토리 패턴을 사용합니다:

```python
def create_foundry_client():
    """Create Foundry Local client with SDK management."""
    manager = FoundryLocalManager(alias)
    client = OpenAI(
        base_url=manager.endpoint,
        api_key=manager.api_key
    )
    return client, manager.get_model_info(alias).id

def create_azure_client():
    """Create Azure OpenAI client."""
    client = OpenAI(
        base_url=f"{endpoint}/openai",
        api_key=api_key,
        default_query={"api-version": api_version}
    )
    return client, model
```


### 스트리밍 응답

이 샘플은 실시간 응답 생성을 위한 스트리밍을 보여줍니다:

```python
stream = client.chat.completions.create(
    model=model,
    messages=[{"role": "user", "content": prompt}],
    stream=True
)

for chunk in stream:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="", flush=True)
```


## 환경 변수

### Foundry Local 구성

| 변수 | 설명 | 기본값 | 필수 여부 |
|------|------|--------|-----------|
| `MODEL` | 사용할 모델 별칭 | `phi-4-mini` | 아니요 |
| `BASE_URL` | Foundry Local 엔드포인트 | `http://localhost:8000` | 아니요 |
| `API_KEY` | API 키 (로컬에서는 선택 사항) | `""` | 아니요 |

### Azure OpenAI 구성

| 변수 | 설명 | 기본값 | 필수 여부 |
|------|------|--------|-----------|
| `AZURE_OPENAI_ENDPOINT` | Azure OpenAI 리소스 엔드포인트 | - | 예 |
| `AZURE_OPENAI_API_KEY` | Azure OpenAI API 키 | - | 예 |
| `AZURE_OPENAI_API_VERSION` | API 버전 | `2024-08-01-preview` | 아니요 |
| `MODEL` | Azure 배포 이름 | `your-deployment-name` | 예 |

## 고급 기능

### 자동 서비스 탐지

이 샘플은 환경 변수를 기반으로 적절한 서비스를 자동으로 감지합니다:

1. **Azure 모드**: `AZURE_OPENAI_ENDPOINT`와 `AZURE_OPENAI_API_KEY`가 설정된 경우
2. **Foundry SDK 모드**: Foundry Local SDK가 사용 가능한 경우
3. **수동 모드**: 수동 구성으로 대체

### 오류 처리

- SDK에서 수동 구성으로의 원활한 대체
- 문제 해결을 위한 명확한 오류 메시지
- 네트워크 문제에 대한 적절한 예외 처리
- 필수 환경 변수의 유효성 검사

## 성능 고려사항

### 로컬 vs 클라우드 비교

**Foundry Local 장점:**
- ✅ API 비용 없음
- ✅ 데이터 프라이버시 (데이터가 장치를 떠나지 않음)
- ✅ 지원되는 모델에 대한 낮은 지연 시간
- ✅ 오프라인 작동 가능

**Azure OpenAI 장점:**
- ✅ 최신 대형 모델 접근 가능
- ✅ 높은 처리량
- ✅ 로컬 컴퓨팅 요구 사항 없음
- ✅ 엔터프라이즈급 SLA

## 문제 해결

### 일반적인 문제

1. **"Foundry SDK를 사용할 수 없습니다" 경고:**
   ```cmd
   pip install foundry-local-sdk
   ```

2. **Azure 인증 오류:**
   ```cmd
   # Verify your endpoint format
   echo %AZURE_OPENAI_ENDPOINT%
   # Should be: https://your-resource.openai.azure.com
   ```

3. **모델을 사용할 수 없음:**
   ```cmd
   # For Foundry Local
   foundry model list
   foundry model run your-model-name
   
   # For Azure OpenAI
   # Check your deployment name in Azure Portal
   ```


### 상태 확인

```cmd
# Foundry Local
foundry service status
curl http://localhost:8000/v1/models

# Azure OpenAI
curl -H "api-key: %AZURE_OPENAI_API_KEY%" "%AZURE_OPENAI_ENDPOINT%/openai/deployments?api-version=2024-08-01-preview"
```


## 다음 단계

- **샘플 03**: 모델 탐색 및 벤치마킹
- **샘플 04**: Chainlit RAG 애플리케이션 구축
- **샘플 05**: 다중 에이전트 오케스트레이션
- **샘플 06**: 도구로서의 모델 라우팅

## 참고 자료

- [Azure OpenAI 문서](https://learn.microsoft.com/azure/ai-services/openai/)
- [Foundry Local SDK 참조](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [OpenAI Python SDK 문서](https://github.com/openai/openai-python)
- [스트리밍 응답 가이드](https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/integrate-with-inference-sdks)

---


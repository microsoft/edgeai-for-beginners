# Foundry Local을 API로 활용한 샘플

이 샘플은 Microsoft Foundry Local을 OpenAI SDK에 의존하지 않고 REST API 서비스로 사용하는 방법을 보여줍니다. 최대한의 제어와 맞춤화를 위해 직접적인 HTTP 통합 패턴을 제공합니다.

## 개요

Microsoft의 공식 Foundry Local 패턴을 기반으로 이 샘플은 다음을 제공합니다:
- FoundryLocalManager와의 직접적인 REST API 통합
- 사용자 정의 HTTP 클라이언트 구현
- 모델 관리 및 상태 모니터링
- 스트리밍 및 비스트리밍 응답 처리
- 프로덕션 환경에 적합한 오류 처리 및 재시도 로직

## 사전 요구사항

1. **Foundry Local 설치**
   ```powershell
   # Install from GitHub releases
   winget install Microsoft.FoundryLocal
   ```

2. **Python 종속성**
   ```bash
   pip install foundry-local-sdk requests asyncio aiohttp
   ```

## 아키텍처

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Your App      │───▶│  REST API Client │───▶│  Foundry Local  │
│                 │    │                  │    │   Service       │
│ - Custom Logic  │    │ - HTTP Requests  │    │ - Model Loading │
│ - Business Rules│    │ - Authentication │    │ - Inference     │
│ - Data Pipeline │    │ - Error Handling │    │ - Health Check  │
└─────────────────┘    └──────────────────┘    └─────────────────┘
```

## 주요 기능

### 1. **직접적인 HTTP 통합**
- SDK 의존성 없이 순수 REST API 호출
- 사용자 정의 인증 및 헤더
- 요청/응답 처리에 대한 완전한 제어

### 2. **모델 관리**
- 동적 모델 로딩 및 언로딩
- 상태 모니터링 및 상태 확인
- 성능 메트릭 수집

### 3. **프로덕션 패턴**
- 지수 백오프를 활용한 재시도 메커니즘
- 장애 허용을 위한 서킷 브레이커
- 포괄적인 로깅 및 모니터링

### 4. **유연한 응답 처리**
- 실시간 애플리케이션을 위한 스트리밍 응답
- 고처리량 시나리오를 위한 배치 처리
- 사용자 정의 응답 파싱 및 검증

## 사용 예제

### 기본 API 통합
```python
from api_client import FoundryAPIClient

# Initialize the API client
client = FoundryAPIClient()

# Simple completion
response = await client.complete(
    prompt="Explain quantum computing",
    model="phi-4-mini",
    max_tokens=500
)
print(response.content)
```

### 스트리밍 통합
```python
# Stream responses for real-time applications
async for chunk in client.stream_complete(
    prompt="Write a story about AI",
    model="phi-4-mini"
):
    print(chunk.content, end="", flush=True)
```

### 상태 모니터링
```python
# Check service health
health = await client.health_check()
print(f"Service Status: {health.status}")
print(f"Active Models: {health.loaded_models}")
print(f"Memory Usage: {health.memory_usage}")
```

## 파일 구조

```
07/
├── README.md              # This documentation
├── requirements.txt       # Python dependencies
├── api_client.py         # Core API client implementation
├── health_monitor.py     # Health checking and monitoring
├── examples/
│   ├── basic_usage.py    # Simple API integration example
│   ├── streaming.py      # Streaming response example
│   ├── batch_processing.py # Batch processing example
│   └── production.py     # Production-ready implementation
└── tests/
    ├── test_api_client.py    # Unit tests for API client
    └── test_integration.py   # Integration tests
```

## Microsoft Foundry Local 통합

이 샘플은 Microsoft의 공식 패턴을 따릅니다:

1. **SDK 통합**: 서비스 관리를 위해 `FoundryLocalManager` 사용
2. **REST 엔드포인트**: `/v1/chat/completions` 및 기타 엔드포인트에 직접 호출
3. **인증**: 로컬 서비스에 적합한 API 키 처리
4. **모델 관리**: 카탈로그 목록, 다운로드 및 로딩 패턴
5. **오류 처리**: Microsoft 권장 오류 코드 및 응답

## 시작하기

1. **종속성 설치**
   ```bash
   pip install -r requirements.txt
   ```

2. **기본 예제 실행**
   ```bash
   python examples/basic_usage.py
   ```

3. **스트리밍 시도**
   ```bash
   python examples/streaming.py
   ```

4. **프로덕션 설정**
   ```bash
   python examples/production.py
   ```

## 구성

환경 변수를 사용한 맞춤화:
- `FOUNDRY_MODEL`: 사용할 기본 모델 (기본값: "phi-4-mini")
- `FOUNDRY_TIMEOUT`: 요청 타임아웃(초) (기본값: 30)
- `FOUNDRY_RETRIES`: 재시도 횟수 (기본값: 3)
- `FOUNDRY_LOG_LEVEL`: 로깅 수준 (기본값: "INFO")

## 모범 사례

1. **연결 관리**: 성능 향상을 위해 HTTP 연결 재사용
2. **오류 처리**: 지수 백오프를 활용한 적절한 재시도 로직 구현
3. **리소스 모니터링**: 모델 메모리 사용량 및 성능 추적
4. **보안**: 로컬 서비스에도 적절한 인증 사용
5. **테스트**: 단위 테스트와 통합 테스트 포함

## 문제 해결

### 일반적인 문제

**서비스 실행 안 됨**
```bash
# Check Foundry Local status
foundry status

# Start if needed
foundry start
```

**모델 로딩 문제**
```bash
# List available models
foundry model list

# Download specific model
foundry model download phi-4-mini
```

**연결 오류**
- Foundry Local이 올바른 포트에서 실행 중인지 확인
- 방화벽 설정 확인
- 적절한 인증 헤더 사용 여부 확인

## 성능 최적화

1. **연결 풀링**: 여러 요청을 위해 세션 객체 사용
2. **비동기 작업**: asyncio를 활용한 동시 요청 처리
3. **캐싱**: 적절한 경우 모델 응답 캐싱
4. **모니터링**: 응답 시간을 추적하고 타임아웃 조정

## 학습 결과

이 샘플을 완료하면 다음을 이해할 수 있습니다:
- Foundry Local과의 직접적인 REST API 통합
- 사용자 정의 HTTP 클라이언트 구현 패턴
- 프로덕션 환경에 적합한 오류 처리 및 모니터링
- Microsoft Foundry Local 서비스 아키텍처
- 로컬 AI 서비스의 성능 최적화 기술

## 다음 단계

- 샘플 08: Windows 11 채팅 애플리케이션 탐색
- 샘플 09: 멀티 에이전트 오케스트레이션 시도
- 샘플 10: Foundry Local을 도구로 통합 학습

---


# Foundry Local SDK - 빠른 참조

## 설치

```bash
# Install SDK
pip install foundry-local-sdk openai

# Install Foundry Local service
# Windows
winget install Microsoft.FoundryLocal

# macOS
brew tap microsoft/foundrylocal
brew install foundrylocal
```

## 서비스 관리

```bash
# Start service
foundry service start

# Check status
foundry service status

# Stop service
foundry service stop

# List models
foundry model ls

# Download model
foundry model download phi-4-mini

# Get model info
foundry model info phi-4-mini
```

## 기본 사용 패턴

```python
from foundry_local import FoundryLocalManager
from openai import OpenAI

# Initialize manager (starts service if needed)
alias = "phi-4-mini"
manager = FoundryLocalManager(alias)

# Create OpenAI-compatible client
client = OpenAI(
    base_url=manager.endpoint,
    api_key=manager.api_key
)

# Get model ID
model_id = manager.get_model_info(alias).id

# Chat completion
response = client.chat.completions.create(
    model=model_id,
    messages=[{"role": "user", "content": "Hello!"}]
)

print(response.choices[0].message.content)
```

## 스트리밍 응답

```python
stream = client.chat.completions.create(
    model=model_id,
    messages=[{"role": "user", "content": "Tell me a story"}],
    stream=True
)

for chunk in stream:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="", flush=True)
```

## 워크숍 유틸리티 (간소화된 버전)

```python
from workshop_utils import chat_once

# Single call with caching and retry
text, usage = chat_once(
    'phi-4-mini',
    messages=[{"role": "user", "content": "What is AI?"}],
    max_tokens=100,
    temperature=0.7
)

print(text)
print(f"Tokens used: {usage.total_tokens}")
```

## 환경 변수

```python
import os

# Show token usage
os.environ['SHOW_USAGE'] = '1'

# Enable retries
os.environ['RETRY_ON_FAIL'] = '1'

# Set retry delay
os.environ['RETRY_BACKOFF'] = '2.0'

# Custom endpoint
os.environ['FOUNDRY_LOCAL_ENDPOINT'] = 'http://localhost:8000'
```

## 공통 모델 별칭

| 별칭 | 크기 | 최적 용도 |
|-------|------|----------|
| `phi-4-mini` | ~4B | 일반적인 작업, 요약 |
| `phi-3.5-mini` | ~3.5B | 코드, 리팩토링 |
| `qwen2.5-0.5b` | ~0.5B | 빠른 분류 |
| `qwen2.5-coder-0.5b` | ~0.5B | 코드 생성 |
| `gemma-2b` | ~2B | 창의적 글쓰기 |

## 오류 처리

```python
from openai import OpenAIError

try:
    text, usage = chat_once('phi-4-mini', messages=[...])
except RuntimeError as e:
    print(f"Manager initialization failed: {e}")
    print("Check: foundry service status")
except OpenAIError as e:
    print(f"API call failed: {e}")
    print("Check: foundry model ls")
except Exception as e:
    print(f"Unexpected error: {e}")
```

## 문제 해결

### 연결 오류
```bash
# Check service
foundry service status

# Restart
foundry service stop
foundry service start

# Test endpoint
curl http://localhost:55769/health
```

### 모델을 찾을 수 없음
```bash
# List available
foundry model ls

# Download if needed
foundry model download phi-4-mini
```

### 가져오기 오류
```bash
# Reinstall SDK
pip uninstall foundry-local-sdk
pip install foundry-local-sdk
```

## 고급: 다중 모델

```python
from workshop_utils import get_client

# Initialize multiple models
models = ['phi-4-mini', 'qwen2.5-0.5b', 'phi-3.5-mini']

clients = {}
for alias in models:
    manager, client, model_id = get_client(alias)
    clients[alias] = (client, model_id)

# Use different models
for alias, (client, model_id) in clients.items():
    response = client.chat.completions.create(
        model=model_id,
        messages=[{"role": "user", "content": "Hello"}],
        max_tokens=50
    )
    print(f"{alias}: {response.choices[0].message.content}")
```

## 성능 팁

1. **클라이언트 캐싱**: `FoundryLocalManager` 인스턴스를 재사용하세요
2. **배치 요청**: 여러 프롬프트를 순차적으로 처리하세요
3. **max_tokens 조정**: 낮을수록 응답 속도가 빨라집니다
4. **모델 미리 로드**: 프로덕션 사용 전에 다운로드하세요
5. **사용량 모니터링**: `SHOW_USAGE=1`로 토큰 사용량을 추적하세요

## 리소스

- **GitHub**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **Discord**: https://aka.ms/foundry-local-discord
- **Issues**: https://github.com/microsoft/Foundry-Local/issues

---

**빠른 시작:**
```bash
# Install everything
winget install Microsoft.FoundryLocal
pip install foundry-local-sdk openai

# Start service
foundry service start

# Test in Python
python -c "from foundry_local import FoundryLocalManager; from openai import OpenAI; m = FoundryLocalManager('phi-4-mini'); c = OpenAI(base_url=m.endpoint, api_key=m.api_key); r = c.chat.completions.create(model=m.get_model_info('phi-4-mini').id, messages=[{'role':'user','content':'Hi'}]); print(r.choices[0].message.content)"
```

---

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있으나, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원본 문서의 원어 버전을 권위 있는 자료로 간주해야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.
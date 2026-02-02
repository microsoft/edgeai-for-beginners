# Foundry Local ကို API အဖြစ် အသုံးပြုခြင်း နမူနာ

ဒီနမူနာက Microsoft Foundry Local ကို REST API ဝန်ဆောင်မှုအဖြစ် OpenAI SDK ကိုမသုံးဘဲ အသုံးပြုနည်းကို ပြသထားပါတယ်။ HTTP ကိုတိုက်ရိုက် ပေါင်းစည်းသုံးစွဲခြင်းနည်းလမ်းများကို ပြသပြီး အမြင့်ဆုံးထိန်းချုပ်မှုနှင့် အပြင်အဆင်ပြုလုပ်နိုင်စွမ်းကို ပေးစွမ်းပါတယ်။

## အကျဉ်းချုပ်

Microsoft ရဲ့ Foundry Local ပုံစံများအပေါ် အခြေခံပြီး ဒီနမူနာက အောက်ပါအရာများကို ပေးစွမ်းပါတယ်။
- FoundryLocalManager နှင့် REST API ကိုတိုက်ရိုက် ပေါင်းစည်းခြင်း
- Custom HTTP client အကောင်အထည်ဖော်ခြင်း
- မော်ဒယ်စီမံခန့်ခွဲမှုနှင့် ကျန်းမာရေးအခြေအနေ စစ်ဆေးခြင်း
- Streaming နှင့် non-streaming အဖြေများကို ကိုင်တွယ်ခြင်း
- ထုတ်လုပ်မှုအဆင်သင့် အမှားကိုင်တွယ်မှုနှင့် ပြန်လည်ကြိုးစားမှု လိုက်နာမှု

## လိုအပ်ချက်များ

1. **Foundry Local Installation**
   ```powershell
   # Install from GitHub releases
   winget install Microsoft.FoundryLocal
   ```

2. **Python Dependencies**
   ```bash
   pip install foundry-local-sdk requests asyncio aiohttp
   ```


## Architecture

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Your App      │───▶│  REST API Client │───▶│  Foundry Local  │
│                 │    │                  │    │   Service       │
│ - Custom Logic  │    │ - HTTP Requests  │    │ - Model Loading │
│ - Business Rules│    │ - Authentication │    │ - Inference     │
│ - Data Pipeline │    │ - Error Handling │    │ - Health Check  │
└─────────────────┘    └──────────────────┘    └─────────────────┘
```


## အဓိက အင်္ဂါရပ်များ

### 1. **HTTP ကိုတိုက်ရိုက် ပေါင်းစည်းခြင်း**
- SDK မလိုအပ်ဘဲ REST API ကို သုံးခြင်း
- Custom authentication နှင့် headers
- Request/response ကို ကိုယ်တိုင်ထိန်းချုပ်နိုင်ခြင်း

### 2. **မော်ဒယ်စီမံခန့်ခွဲမှု**
- မော်ဒယ်များကို dynamic loading နှင့် unloading
- ကျန်းမာရေးအခြေအနေ စစ်ဆေးခြင်း
- စွမ်းဆောင်ရည် metrics စုဆောင်းခြင်း

### 3. **ထုတ်လုပ်မှု ပုံစံများ**
- Exponential backoff ဖြင့် ပြန်လည်ကြိုးစားမှု mechanism
- Fault tolerance အတွက် circuit breaker
- Comprehensive logging နှင့် monitoring

### 4. **Flexible Response ကို ကိုင်တွယ်ခြင်း**
- Real-time application အတွက် streaming responses
- High-throughput scenarios အတွက် batch processing
- Custom response parsing နှင့် validation

## အသုံးပြုနည်း နမူနာများ

### Basic API Integration
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

### Streaming Integration
```python
# Stream responses for real-time applications
async for chunk in client.stream_complete(
    prompt="Write a story about AI",
    model="phi-4-mini"
):
    print(chunk.content, end="", flush=True)
```

### Health Monitoring
```python
# Check service health
health = await client.health_check()
print(f"Service Status: {health.status}")
print(f"Active Models: {health.loaded_models}")
print(f"Memory Usage: {health.memory_usage}")
```


## ဖိုင်ဖွဲ့စည်းပုံ

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


## Microsoft Foundry Local Integration

ဒီနမူနာက Microsoft ရဲ့ တရားဝင်ပုံစံများကို လိုက်နာထားပါတယ်။

1. **SDK Integration**: `FoundryLocalManager` ကို ဝန်ဆောင်မှုစီမံခန့်ခွဲမှုအတွက် အသုံးပြုခြင်း
2. **REST Endpoints**: `/v1/chat/completions` နှင့် အခြား endpoints ကို တိုက်ရိုက် ခေါ်ယူခြင်း
3. **Authentication**: Local services အတွက် API key ကို သင့်တော်စွာ ကိုင်တွယ်ခြင်း
4. **Model Management**: Catalog listing, downloading, နှင့် loading ပုံစံများ
5. **Error Handling**: Microsoft အကြံပြုထားသော error codes နှင့် responses

## စတင်အသုံးပြုခြင်း

1. **Dependencies ကို Install လုပ်ပါ**
   ```bash
   pip install -r requirements.txt
   ```

2. **Basic Example ကို Run လုပ်ပါ**
   ```bash
   python examples/basic_usage.py
   ```

3. **Streaming ကို စမ်းသပ်ပါ**
   ```bash
   python examples/streaming.py
   ```

4. **Production Setup**
   ```bash
   python examples/production.py
   ```


## Configuration

အပြင်အဆင်ပြုလုပ်နိုင်စွမ်းအတွက် Environment variables:
- `FOUNDRY_MODEL`: အသုံးပြုမည့် default model (default: "phi-4-mini")
- `FOUNDRY_TIMEOUT`: Request timeout အချိန် (default: 30)
- `FOUNDRY_RETRIES`: Retry ကြိုးစားမှုအရေအတွက် (default: 3)
- `FOUNDRY_LOG_LEVEL`: Logging level (default: "INFO")

## အကောင်းဆုံး လုပ်ဆောင်မှုများ

1. **Connection Management**: HTTP connections ကို ထပ်ခါတလဲလဲ အသုံးပြုခြင်း
2. **Error Handling**: Exponential backoff ဖြင့် retry logic ကို အကောင်းဆုံးအကောင်အထည်ဖော်ခြင်း
3. **Resource Monitoring**: မော်ဒယ် memory အသုံးပြုမှုနှင့် စွမ်းဆောင်ရည်ကို စောင့်ကြည့်ခြင်း
4. **Security**: Local services အတွက် သင့်တော်သော authentication ကို အသုံးပြုခြင်း
5. **Testing**: Unit နှင့် integration tests နှစ်မျိုးလုံး ပါဝင်စေရန်

## Troubleshooting

### Common Issues

**Service Not Running**
```bash
# Check Foundry Local status
foundry status

# Start if needed
foundry start
```

**Model Loading Issues**
```bash
# List available models
foundry model list

# Download specific model
foundry model download phi-4-mini
```

**Connection Errors**
- Foundry Local ကို မှန်ကန်သော port တွင် run လုပ်နေကြောင်း စစ်ဆေးပါ
- Firewall settings ကို စစ်ဆေးပါ
- Authentication headers ကို သေချာစွာ ထည့်သွင်းပါ

## စွမ်းဆောင်ရည် တိုးတက်အောင်လုပ်ဆောင်ခြင်း

1. **Connection Pooling**: မကြာခဏ request များအတွက် session objects ကို အသုံးပြုပါ
2. **Async Operations**: Concurrent requests အတွက် asyncio ကို အသုံးပြုပါ
3. **Caching**: မော်ဒယ် response များကို သင့်တော်သောနေရာတွင် cache လုပ်ပါ
4. **Monitoring**: Response times ကို စောင့်ကြည့်ပြီး timeout ကို ပြင်ဆင်ပါ

## သင်ယူရရှိနိုင်သော အကျိုးကျေးဇူးများ

ဒီနမူနာကို ပြီးမြောက်ပြီးနောက် သင်သည် အောက်ပါအရာများကို နားလည်နိုင်ပါမည်။
- Foundry Local နှင့် REST API ကို တိုက်ရိုက် ပေါင်းစည်းခြင်း
- Custom HTTP client အကောင်အထည်ဖော်ခြင်း ပုံစံများ
- ထုတ်လုပ်မှုအဆင်သင့် error handling နှင့် monitoring
- Microsoft Foundry Local ဝန်ဆောင်မှု architecture
- Local AI services အတွက် စွမ်းဆောင်ရည် တိုးတက်အောင်လုပ်ဆောင်နည်းများ

## နောက်တစ်ဆင့်

- Sample 08: Windows 11 Chat Application ကို စမ်းသပ်ပါ
- Sample 09: Multi-Agent Orchestration ကို စမ်းသပ်ပါ
- Sample 10: Foundry Local as Tools Integration ကို လေ့လာပါ

---


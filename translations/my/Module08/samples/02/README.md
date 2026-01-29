# နမူနာ 02: OpenAI SDK ပေါင်းစည်းမှု

Microsoft Foundry Local နှင့် Azure OpenAI နှစ်ခုလုံးကို ပေါင်းစည်းပြီး Streaming Responses နှင့် မှန်ကန်သော Error Handling ကို ပံ့ပိုးပေးသော OpenAI Python SDK နှင့် အဆင့်မြင့်ပေါင်းစည်းမှုကို ပြသထားသည်။

## အကျဉ်းချုပ်

ဒီနမူနာမှာ ပြသထားတာတွေက:
- Foundry Local နဲ့ Azure OpenAI အကြား အဆင်ပြေပြေ ပြောင်းလဲနိုင်မှု
- အသုံးပြုသူအတွေ့အကြုံကို ပိုမိုကောင်းမွန်စေတဲ့ Streaming Chat Completions
- FoundryLocalManager SDK ကို မှန်ကန်စွာ အသုံးပြုခြင်း
- Error Handling နှင့် Fallback Mechanisms ကို ခိုင်မာစွာ ဆောင်ရွက်ခြင်း
- ထုတ်လုပ်မှုအဆင့် Code ပုံစံများ

## ကြိုတင်လိုအပ်ချက်များ

- **Foundry Local**: Local Inference အတွက် Install လုပ်ပြီး Run လုပ်ထားရမည်
- **Python**: OpenAI SDK ပါဝင်သော 3.8 သို့မဟုတ် အထက်
- **Azure OpenAI**: Cloud Inference အတွက် သက်တမ်းရှိ Endpoint နှင့် API Key

## Installation

1. **Python Environment ကို Set Up လုပ်ပါ:**
   ```cmd
   cd Module08
   py -m venv .venv
   .venv\Scripts\activate
   ```

2. **Dependencies တွေ Install လုပ်ပါ:**
   ```cmd
   pip install -r requirements.txt
   ```

3. **Foundry Local ကို Start လုပ်ပါ (Local Mode အတွက်):**
   ```cmd
   foundry model run phi-4-mini
   ```


## အသုံးပြုနိုင်သော အခွင့်အရေးများ

### Foundry Local (Default)

**Option 1: FoundryLocalManager ကို အသုံးပြုခြင်း (အကြံပြုထားသည်)**
```cmd
# Automatic service discovery and model management
set MODEL=phi-4-mini
python samples\02\sdk_quickstart.py
```

**Option 2: Manual Configuration**
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


## Code Architecture

### Client Factory Pattern

ဒီနမူနာမှာ Factory Pattern ကို အသုံးပြုပြီး သင့်တော်သော Clients တွေကို ဖန်တီးထားသည်:

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


### Streaming Responses

ဒီနမူနာမှာ Real-Time Response Generation အတွက် Streaming ကို ပြသထားသည်:

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


## Environment Variables

### Foundry Local Configuration

| Variable | Description | Default | Required |
|----------|-------------|---------|----------|
| `MODEL` | အသုံးပြုမည့် Model Alias | `phi-4-mini` | No |
| `BASE_URL` | Foundry Local Endpoint | `http://localhost:8000` | No |
| `API_KEY` | API Key (Local အတွက် optional) | `""` | No |

### Azure OpenAI Configuration

| Variable | Description | Default | Required |
|----------|-------------|---------|----------|
| `AZURE_OPENAI_ENDPOINT` | Azure OpenAI Resource Endpoint | - | Yes |
| `AZURE_OPENAI_API_KEY` | Azure OpenAI API Key | - | Yes |
| `AZURE_OPENAI_API_VERSION` | API Version | `2024-08-01-preview` | No |
| `MODEL` | Azure Deployment Name | `your-deployment-name` | Yes |

## အဆင့်မြင့် Features

### Automatic Service Discovery

ဒီနမူနာမှာ Environment Variables အပေါ် မူတည်ပြီး သင့်တော်သော Service ကို အလိုအလျောက် ရှာဖွေသည်:

1. **Azure Mode**: `AZURE_OPENAI_ENDPOINT` နှင့် `AZURE_OPENAI_API_KEY` ရှိပါက
2. **Foundry SDK Mode**: Foundry Local SDK ရရှိနိုင်ပါက
3. **Manual Mode**: Manual Configuration ကို fallback လုပ်သည်

### Error Handling

- SDK မှ Manual Configuration သို့ Graceful Fallback
- Troubleshooting အတွက် ရှင်းလင်းသော Error Messages
- Network Issues အတွက် Exception Handling မှန်ကန်စွာ ဆောင်ရွက်ခြင်း
- လိုအပ်သော Environment Variables တွေကို Validate လုပ်ခြင်း

## Performance Considerations

### Local vs Cloud Trade-offs

**Foundry Local အကျိုးကျေးဇူးများ:**
- ✅ API ကုန်ကျစရိတ်မရှိ
- ✅ ဒေတာကို Device မှ အပြင်မထွက်သော Data Privacy
- ✅ Supported Models အတွက် အနိမ့်ဆုံး Latency
- ✅ Offline အနေဖြင့် အလုပ်လုပ်နိုင်

**Azure OpenAI အကျိုးကျေးဇူးများ:**
- ✅ နောက်ဆုံးပေါ် Large Models တွေကို အသုံးပြုနိုင်
- ✅ မြင့်မားသော Throughput
- ✅ Local Compute Requirements မရှိ
- ✅ Enterprise-grade SLA

## Troubleshooting

### Common Issues

1. **"Could not use Foundry SDK" warning:**
   ```cmd
   pip install foundry-local-sdk
   ```

2. **Azure authentication errors:**
   ```cmd
   # Verify your endpoint format
   echo %AZURE_OPENAI_ENDPOINT%
   # Should be: https://your-resource.openai.azure.com
   ```

3. **Model not available:**
   ```cmd
   # For Foundry Local
   foundry model list
   foundry model run your-model-name
   
   # For Azure OpenAI
   # Check your deployment name in Azure Portal
   ```


### Health Checks

```cmd
# Foundry Local
foundry service status
curl http://localhost:8000/v1/models

# Azure OpenAI
curl -H "api-key: %AZURE_OPENAI_API_KEY%" "%AZURE_OPENAI_ENDPOINT%/openai/deployments?api-version=2024-08-01-preview"
```


## Next Steps

- **Sample 03**: Model Discovery နှင့် Benchmarking
- **Sample 04**: Chainlit RAG Application တည်ဆောက်ခြင်း
- **Sample 05**: Multi-agent Orchestration
- **Sample 06**: Models-as-tools Routing

## References

- [Azure OpenAI Documentation](https://learn.microsoft.com/azure/ai-services/openai/)
- [Foundry Local SDK Reference](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [OpenAI Python SDK Documentation](https://github.com/openai/openai-python)
- [Streaming Completions Guide](https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/integrate-with-inference-sdks)

---


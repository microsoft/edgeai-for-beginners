# Open WebUI + Foundry Local အတူတကွ ပေါင်းစပ်အသုံးပြုရန် လမ်းညွှန်

ဤလမ်းညွှန်သည် Open WebUI ကို Microsoft Foundry Local နှင့် ချိတ်ဆက်ပြီး သင့်ဒေသခံ AI မော်ဒယ်များအား အားထားနိုင်သော ChatGPT ပုံစံမျိုးဖြင့် အသုံးပြုရန် လမ်းညွှန်ပေးသည်။

## အကျဉ်းချုပ်

Open WebUI သည် ခေတ်မီသော၊ အသုံးပြုရလွယ်ကူသော chat interface ကို ပေးစွမ်းပြီး OpenAI-compatible API များနှင့် ချိတ်ဆက်နိုင်သည်။ Foundry Local နှင့် ချိတ်ဆက်ခြင်းအားဖြင့် သင်ရရှိနိုင်သည်မှာ:

- **ပရော်ဖက်ရှင်နယ် UI**: ChatGPT ပုံစံ interface နှင့် ခေတ်မီဒီဇိုင်း
- **ဒေသခံကိုယ်ရေးအချက်အလက်လုံခြုံမှု**: အားလုံးကို သင့်စက်ပေါ်တွင်သာ အလုပ်လုပ်သည်
- **မော်ဒယ်ပြောင်းလဲမှု**: မော်ဒယ်များကို လွယ်ကူစွာ ပြောင်းလဲနိုင်ခြင်း
- **စကားဝိုင်းမှတ်တမ်း**: စကားဝိုင်းမှတ်တမ်းနှင့် context ကို ထိန်းသိမ်းထားနိုင်ခြင်း
- **ဖိုင်တင်သွင်းမှု**: စာရွက်စာတမ်းများကို ခွဲခြမ်းစိတ်ဖြာနိုင်ခြင်း
- **စိတ်ကြိုက် Personas**: System prompts နှင့် role customization

## လိုအပ်ချက်များ

### လိုအပ်သော Software

```cmd
# Verify Foundry Local installation
foundry --version

# Verify Docker installation
docker --version

# Start Foundry Local service
foundry service start
```

### မော်ဒယ်တစ်ခု Load လုပ်ရန်

```cmd
# List available models
foundry model list

# Load your preferred model
foundry model run phi-4-mini

# Verify model is running
foundry service ps
```

## အမြန်စတင်ခြင်း (အကြံပြုထားသည်)

### အဆင့် ၁: Open WebUI ကို Docker ဖြင့် Run လုပ်ပါ

```cmd
# Pull the latest Open WebUI image
docker pull ghcr.io/open-webui/open-webui:main

# Run Open WebUI connected to Foundry Local
docker run -d \
  --name open-webui \
  -p 3000:8080 \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-local-key \
  -v open-webui-data:/app/backend/data \
  ghcr.io/open-webui/open-webui:main
```

**Windows PowerShell:**
```powershell
docker run -d `
  --name open-webui `
  -p 3000:8080 `
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 `
  -e OPENAI_API_KEY=foundry-local-key `
  -v open-webui-data:/app/backend/data `
  ghcr.io/open-webui/open-webui:main
```

### အဆင့် ၂: စတင်တပ်ဆင်ခြင်း

1. **Browser ဖွင့်ပါ**: `http://localhost:3000` သို့ သွားပါ
2. **အကောင့်ဖွင့်ပါ**: admin user ကို စတင်တည်ဆောက်ပါ (ပထမ user သည် admin ဖြစ်သည်)
3. **ချိတ်ဆက်မှုကို အတည်ပြုပါ**: မော်ဒယ်များသည် dropdown တွင် အလိုအလျောက် ပေါ်လာသင့်သည်

### အဆင့် ၃: ချိတ်ဆက်မှုကို စမ်းသပ်ပါ

1. Dropdown မှ မော်ဒယ်ကို ရွေးပါ (ဥပမာ - "phi-4-mini")
2. စမ်းသပ်မက်ဆေ့ချ်ရေးပါ: "Hello! Can you introduce yourself?"
3. သင့်ဒေသခံမော်ဒယ်မှ streaming response ကို မြင်ရပါမည်

## အဆင့်မြှင့်တင်ထားသော Configuration

### Environment Variables

| Variable | ရည်ရွယ်ချက် | Default | ဥပမာ |
|----------|-------------|---------|-------|
| `OPENAI_API_BASE_URL` | Foundry Local endpoint | - | `http://host.docker.internal:51211/v1` |
| `OPENAI_API_KEY` | API key (လိုအပ်သော်လည်း ဒေသတွင် မသုံးပါ) | - | `foundry-local-key` |
| `WEBUI_SECRET_KEY` | Session encryption key | auto-generated | `your-secret-key` |
| `ENABLE_SIGNUP` | အသုံးပြုသူအသစ်များကို စာရင်းသွင်းခွင့်ပြုခြင်း | `True` | `False` |

### Manual Configuration (အခြားရွေးချယ်မှု)

Environment variables မအလုပ်လုပ်ပါက Manual configuration ပြုလုပ်ပါ:

1. **Settings ဖွင့်ပါ**: Settings (gear icon) ကို နှိပ်ပါ
2. **Connections သို့ သွားပါ**: Settings → Connections → OpenAI
3. **API အသေးစိတ်ကို သတ်မှတ်ပါ**:
   - API Base URL: `http://host.docker.internal:51211/v1`
   - API Key: `foundry-local-key` (တန်ဖိုးမည်သည့်အရာမဆို အလုပ်လုပ်သည်)
4. **Save နှင့် စမ်းသပ်ပါ**: "Save" ကို နှိပ်ပြီး မော်ဒယ်ဖြင့် စမ်းသပ်ပါ

### Persistent Data Storage

စကားဝိုင်းများနှင့် settings ကို ထိန်းသိမ်းရန်:

```cmd
# Windows - Create data directory
mkdir %USERPROFILE%\openwebui-data

# Run with persistent storage
docker run -d \
  --name open-webui \
  -p 3000:8080 \
  -v "%USERPROFILE%\openwebui-data:/app/backend/data" \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-local-key \
  ghcr.io/open-webui/open-webui:main
```

## ပြဿနာဖြေရှင်းခြင်း

### ချိတ်ဆက်မှုပြဿနာများ

**ပြဿနာ**: "Connection refused" သို့မဟုတ် မော်ဒယ်များ မပေါ်ခြင်း

**ဖြေရှင်းနည်းများ**:
```cmd
# 1. Verify Foundry Local is running
foundry service status
foundry service ps

# 2. Test API endpoint directly
curl http://localhost:51211/v1/models

# 3. Check Docker container logs
docker logs open-webui

# 4. Restart Open WebUI container
docker restart open-webui
```

### မော်ဒယ် မပေါ်ခြင်း

**ပြဿနာ**: Open WebUI တွင် dropdown မှာ မော်ဒယ်များ မပေါ်ခြင်း

**Debugging အဆင့်များ**:
```cmd
# Check if model is loaded in Foundry Local
foundry model list

# Test API response
curl -X GET http://localhost:51211/v1/models \
  -H "Content-Type: application/json"

# Verify correct port (should be 51211 for Foundry Local)
netstat -ano | findstr :51211
```

**ဖြေရှင်းနည်း**: မော်ဒယ်ကို သေချာစွာ load လုပ်ထားပါ:
```cmd
# Stop and restart model
foundry model stop phi-4-mini
foundry model run phi-4-mini

# Wait for model to fully load, then refresh Open WebUI
```

### Docker Network ပြဿနာများ

**ပြဿနာ**: `host.docker.internal` မဖြေရှင်းနိုင်ခြင်း

**Windows ဖြေရှင်းနည်း**:
```cmd
# Use localhost alternative (may need admin privileges)
docker run -d \
  --name open-webui \
  -p 3000:8080 \
  --add-host=host.docker.internal:host-gateway \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-local-key \
  ghcr.io/open-webui/open-webui:main
```

**အခြားရွေးချယ်မှု**: သင့်စက်၏ IP ကို ရှာပါ:
```cmd
ipconfig | findstr IPv4
# Use your actual IP instead of host.docker.internal
# Example: http://192.168.1.100:51211/v1
```

### Performance ပြဿနာများ

**တုံ့ပြန်မှုနှေးကွေးခြင်း**:
1. မော်ဒယ်သည် GPU acceleration ကို အသုံးပြုနေသည်ကို စစ်ဆေးပါ: `foundry service ps`
2. စနစ်အရင်းအမြစ်များ (RAM/GPU memory) လုံလောက်မှုကို စစ်ဆေးပါ
3. စမ်းသပ်ရန် မော်ဒယ်အသေးကို အသုံးပြုပါ

**မှတ်ဉာဏ်ပြဿနာများ**:
```cmd
# Check Docker container memory usage
docker stats open-webui

# Restart Docker if needed
docker restart open-webui
```

## အသုံးပြုရန် လမ်းညွှန်

### အခြေခံ Chat

1. **မော်ဒယ်ကို ရွေးပါ**: Dropdown မှ Foundry Local မော်ဒယ်များကို ရွေးပါ
2. **မက်ဆေ့ချ်ရေးပါ**: အောက်ခြေရှိ text input ကို အသုံးပြုပါ
3. **ပို့ပါ**: Enter ကို နှိပ်ပါ သို့မဟုတ် Send button ကို နှိပ်ပါ
4. **တုံ့ပြန်မှုကို ကြည့်ပါ**: Streaming response ကို အချိန်နှင့်တပြေးညီ မြင်နိုင်ပါမည်

### အဆင့်မြင့် Features

**ဖိုင်တင်သွင်းမှု**:
1. Paperclip icon ကို နှိပ်ပါ
2. စာရွက်စာတမ်းတင်ပါ (PDF, TXT, စသည်)
3. အကြောင်းအရာကို မေးမြန်းပါ
4. မော်ဒယ်သည် စာရွက်စာတမ်းကို ခွဲခြမ်းစိတ်ဖြာပြီး တုံ့ပြန်ပါမည်

**စိတ်ကြိုက် System Prompts**:
1. Settings → Personalization
2. စိတ်ကြိုက် system prompt ကို သတ်မှတ်ပါ
3. AI personality/behavior ကို တည်ငြိမ်စေပါ

**စကားဝိုင်းစီမံခန့်ခွဲမှု**:
- **New Chat**: "+" ကို နှိပ်ပြီး စကားဝိုင်းအသစ်စတင်ပါ
- **Chat History**: Sidebar မှ ယခင်စကားဝိုင်းများကို ဝင်ရောက်ကြည့်ရှုပါ
- **Export**: စကားဝိုင်းမှတ်တမ်းကို text/JSON အဖြစ် download လုပ်ပါ

**မော်ဒယ်နှိုင်းယှဉ်မှု**:
1. Browser tabs များစွာကို Open WebUI တစ်ခုတည်းတွင် ဖွင့်ပါ
2. တစ် tab စီတွင် မော်ဒယ်များကို ရွေးပါ
3. တူညီသော prompts များကို တုံ့ပြန်မှုများနှိုင်းယှဉ်ပါ

### Integration Patterns

**ဖွံ့ဖြိုးတိုးတက်မှု Workflow**:
```cmd
# Terminal 1: Start Foundry Local with development model
foundry model run phi-4-mini

# Terminal 2: Start Open WebUI for testing
docker run --rm -p 3000:8080 \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=dev-key \
  ghcr.io/open-webui/open-webui:main

# Terminal 3: Test API directly for debugging
curl -X POST http://localhost:51211/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"model":"phi-4-mini","messages":[{"role":"user","content":"test"}]}'
```

## Production Deployment

### လုံခြုံစွာတပ်ဆင်ခြင်း

```cmd
# Generate secure secret key
openssl rand -base64 32

# Production deployment with security
docker run -d \
  --name open-webui-prod \
  -p 3000:8080 \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-local-prod \
  -e WEBUI_SECRET_KEY=your-secure-key-here \
  -e ENABLE_SIGNUP=False \
  -v /path/to/secure/storage:/app/backend/data \
  --restart unless-stopped \
  ghcr.io/open-webui/open-webui:main
```

### Multi-User Setup

```cmd
# Allow controlled user registration
docker run -d \
  --name open-webui-team \
  -p 3000:8080 \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-team \
  -e ENABLE_SIGNUP=True \
  -e WEBUI_SECRET_KEY=team-secret-key \
  -v team-data:/app/backend/data \
  ghcr.io/open-webui/open-webui:main
```

### Monitoring နှင့် Logging

```cmd
# View real-time logs
docker logs -f open-webui

# Monitor container resources
docker stats open-webui

# Check container health
docker inspect open-webui | grep -i health
```

## ရှင်းလင်းမှု

```cmd
# Stop Open WebUI
docker stop open-webui

# Remove container
docker rm open-webui

# Remove data volume (WARNING: deletes all chats)
docker volume rm open-webui-data

# Remove image
docker rmi ghcr.io/open-webui/open-webui:main
```

## နောက်တစ်ဆင့်များ

### တိုးတက်မှုအကြံပြုချက်များ

1. **စိတ်ကြိုက်မော်ဒယ်များ**: Foundry Local တွင် သင့်ကိုယ်ပိုင် fine-tuned မော်ဒယ်များ ထည့်သွင်းပါ
2. **API Integration**: Open WebUI functions မှတစ်ဆင့် အပြင် API များနှင့် ချိတ်ဆက်ပါ
3. **စာရွက်စာတမ်းများကို ခွဲခြမ်းစိတ်ဖြာခြင်း**: အဆင့်မြင့် RAG pipelines တပ်ဆင်ပါ
4. **Multi-Modal**: ရုပ်ပုံခွဲခြမ်းစိတ်ဖြာရန် vision models ကို configure လုပ်ပါ

### Scaling အတွေးအခေါ်များ

- **Load Balancing**: Reverse proxy အောက်တွင် Foundry Local instances များစွာ
- **မော်ဒယ် Routing**: အသုံးပြုမှုအမျိုးအစားအလိုက် မော်ဒယ်များကို ခွဲခြားအသုံးပြုခြင်း
- **Resource Management**: Concurrent users အတွက် GPU memory ကို အကောင်းဆုံးအသုံးပြုခြင်း
- **Backup Strategy**: စကားဝိုင်းဒေတာနှင့် configurations ကို အကြိမ်ကြိမ် backup လုပ်ခြင်း

## References

- [Open WebUI Documentation](https://docs.openwebui.com/)
- [Open WebUI GitHub Repository](https://github.com/open-webui/open-webui)
- [Foundry Local Documentation](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [Docker Installation Guide](https://docs.docker.com/get-docker/)

---


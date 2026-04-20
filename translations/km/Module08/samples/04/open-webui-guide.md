# Open WebUI + Foundry Local មគ្គុទេសក៍សម្រាប់ការរួមបញ្ចូល

មគ្គុទេសក៍នេះបង្ហាញពីរបៀបភ្ជាប់ Open WebUI ទៅ Microsoft Foundry Local សម្រាប់ផ្ទាំងចាតដែលមានលក្ខណៈដូច ChatGPT សម្រាប់ការប្រើប្រាស់វិជ្ជាជីវៈ ដែលប្រើម៉ូឌែល AI ផ្ទាល់ក្នុងម៉ាស៊ីនរបស់អ្នក។

## ទិដ្ឋភាពទូទៅ

Open WebUI ផ្តល់ផ្ទាំងចាតទាន់សម័យ និងងាយស្រួលប្រើ ដែលអាចភ្ជាប់ទៅ API ដែលសមស្របនឹង OpenAI ណាមួយបាន។ ដោយភ្ជាប់វាទៅ Foundry Local អ្នកនឹងទទួលបាន៖

- **ផ្ទាំង UI វិជ្ជាជីវៈ**: ផ្ទាំងប្រើប្រាស់ដែលមានរចនាសម្ព័ន្ធដូច ChatGPT
- **ភាពឯកជនក្នុងស្រុក**: ការកែលម្អទាំងអស់កើតឡើងលើឧបករណ៍របស់អ្នក
- **ការប្ដូរម៉ូឌែល**: ការប្ដូរម៉ូឌែលក្នុងស្រុកយ៉ាងងាយស្រួល
- **ប្រវត្តិសារ​ជជែក**: ប្រវត្តិការជជែក និងបរិបទដែលធន់ទ្រាំ
- **ការផ្ទុកឯកសារ**: ការវិភាគឯកសារ និងសមត្ថភាពដំណើរការឯកសារ
- **បញ្ចូលបុគ្គលិកភាព**: ការកំណត់ប្រព័ន្ធ Prompt និងតួនាទីផ្ទាល់ខ្លួន

## លក្ខខ័ណ្ឌមុនចាប់ផ្តើម

### កម្មវិធីត្រូវការ

```cmd
# Verify Foundry Local installation
foundry --version

# Verify Docker installation
docker --version

# Start Foundry Local service
foundry service start
```

### ផ្ទុកម៉ូឌែល

```cmd
# List available models
foundry model list

# Load your preferred model
foundry model run phi-4-mini

# Verify model is running
foundry service ps
```

## ការកំណត់យ៉ាងរហ័ស (ណែនាំ)

### ជំហាន 1: ដំណើរការ Open WebUI ជាមួយ Docker

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

### ជំហាន 2: ការកំណត់ដំបូង

1. **Open Browser**: បើកទៅកាន់ `http://localhost:3000`
2. **Create Account**: តម្លើងអ្នកប្រើប្រាស់រដ្ឋបាល (អ្នកប្រើប្រាស់ជាលើកដំបូងនឹងក្លាយជាអ្នករដ្ឋបាល)
3. **Verify Connection**: ម៉ូឌែលគួរតែបង្ហាញក្នុងបញ្ជីចុះជ្រើសដោយស្វ័យប្រវត្តិ

### ជំហាន 3: សាកល្បងការភ្ជាប់

1. ជ្រើសម៉ូឌែលរបស់អ្នកពីបញ្ជីចុះជ្រើស (ឧ. "phi-4-mini")
2. វាយសារ​សាកល្បង៖ "សួស្តី! តើ​អ្នក​អាចណែនាំខ្លួនឯងបានទេ?"
3. អ្នកគួរតែឃើញចម្លើយចាក់ដោយបន្តពីម៉ូឌែលក្នុងស្រុករបស់អ្នក

## ការកំណត់កម្រិតខ្ពស់

### Environment Variables

| Variable | Purpose | Default | Example |
|----------|---------|---------|----------|
| `OPENAI_API_BASE_URL` | តំណចុងបញ្ចប់ Foundry Local | - | `http://host.docker.internal:51211/v1` |
| `OPENAI_API_KEY` | កូនសោ API (ត្រូវការ ប៉ុន្តែមិនបានប្រើក្នុងស្រុក) | - | `foundry-local-key` |
| `WEBUI_SECRET_KEY` | កូនសោអ៊ិនគ្រីបសេស្ស្យង | auto-generated | `your-secret-key` |
| `ENABLE_SIGNUP` | អនុញ្ញាតឱ្យចុះឈ្មោះអ្នកប្រើថ្មី | `True` | `False` |

### ការកំណត់ដោយដៃ (ជាជម្រើស)

បើ environment variables មិនដំណើរការ សូមកំណត់ដោយដៃ៖

1. **Open Settings**: ចុច Settings (រូបតួថេរ)
2. **Navigate to Connections**: Settings → Connections → OpenAI
3. **Set API Details**:
   - API Base URL: `http://host.docker.internal:51211/v1`
   - API Key: `foundry-local-key` (តម្លៃណាមួយក៏ដំណើរការ)
4. **Save and Test**: ចុច "Save" បន្ទាប់មកសាកល្បងជាមួយម៉ូឌែលមួយ

### ការផ្ទុកទិន្នន័យដោយចាំទុក

ដើម្បីរក្សាសារ​ជជែក និងការកំណត់៖

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

## ការដោះស្រាយបញ្ហា

### បញ្ហាការភ្ជាប់

**Problem**: "Connection refused" ឬម៉ូឌែលមិនបានផ្ទុក

**Solutions**:
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

### ម៉ូឌែលមិនបង្ហាញ

**Problem**: Open WebUI មិនបង្ហាញម៉ូឌែលក្នុងបញ្ជីចុះជ្រើស

**Debugging Steps**:
```cmd
# Check if model is loaded in Foundry Local
foundry model list

# Test API response
curl -X GET http://localhost:51211/v1/models \
  -H "Content-Type: application/json"

# Verify correct port (should be 51211 for Foundry Local)
netstat -ano | findstr :51211
```

**Fix**: សូមប្រាកដថាម៉ូឌែលត្រូវបានផ្ទុកបានយ៉ាងសមរម្យ:
```cmd
# Stop and restart model
foundry model stop phi-4-mini
foundry model run phi-4-mini

# Wait for model to fully load, then refresh Open WebUI
```

###បញ្ហាបណ្ដាញ Docker

**Problem**: `host.docker.internal` មិនបានដោះសោរ

**Windows Solution**:
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

**ជំនួស**: ស្វែងរកអាសយដ្ឋាន IP របស់ម៉ាស៊ីនរបស់អ្នក:
```cmd
ipconfig | findstr IPv4
# Use your actual IP instead of host.docker.internal
# Example: http://192.168.1.100:51211/v1
```

### បញ្ហាការសម្តែង

**Slow Responses**:
1. ពិនិត្យមើលថាម៉ូឌែលកំពុងប្រើការបង្គកGPU ឬទេ: `foundry service ps`
2. ពិនិត្យធនធានប្រព័ន្ធគ្រប់គ្រាន់ (RAM/យ៉ាងហោចណាស់ GPU memory)
3. សូមពិចារណាប្រើម៉ូឌែលតិចជាងសម្រាប់សាកល្បង

**Memory Issues**:
```cmd
# Check Docker container memory usage
docker stats open-webui

# Restart Docker if needed
docker restart open-webui
```

## មគ្គុទេសក៍ការប្រើ

### ជជែកមូលដ្ឋាន

1. **Select Model**: ជ្រើសពីបញ្ជីចុះជ្រើស (បង្ហាញម៉ូឌែល Foundry Local)
2. **Type Message**: ប្រើប្រអប់បញ្ចូលអក្សរនៅខាងក្រោម
3. **Send**: ចុច Enter ឬចុចប៊ូតុង Send
4. **View Response**: មើលចម្លើយចាក់ជាបន្តក្នុងម៉ោងពេលពិត

### លក្ខណៈពិសេសកម្រិតខ្ពស់

**File Upload**:
1. ចុចរូបតំណក់ក្រដាស (paperclip)
2. ដាក់ឯកសារ (PDF, TXT, លឿន)
3. សួរទាក់ទងអំពីមាតិកា
4. ម៉ូឌែលនឹងវិភាគ និងឆ្លើយបញ្ចេញលទ្ធផលដោយផ្អែកលើឯកសារ

**Custom System Prompts**:
1. Settings → Personalization
2. កំណត់ system prompt ផ្ទាល់ខ្លួន
3. បង្កើតបុគ្គលិកភាព/អាកប្បិរមាជាមួយ AI ដែលមានរចនាបថស្ថायी

**Conversation Management**:
- **New Chat**: ចុច "+" ដើម្បីចាប់ផ្តើមជជែកថ្មី
- **Chat History**: ចូលប្រើសារជជែកពីមុនពី sidebar
- **Export**: ទាញយកប្រវត្តិការជជែកជាឯកសារ text/JSON

**Model Comparison**:
1. បើកផ្ទាំងបរភ្ជាប់បើកទំព័រពហុដដែលទៅ Open WebUI
2. ជ្រើសម៉ូឌែលខុសៗគ្នាក្នុងមួយទំព័រ
3. ប្រៀបធៀបចម្លើយចំពោះ prompt ដូចគ្នា

### លំនាំការរួមបញ្ចូល

**Development Workflow**:
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

## ផ្ដល់បញ្ចូលលើម៉ាស៊ីនផលិត

### ការកំណត់សុវត្ថិភាព

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

### ការកំណត់ច្រើនអ្នកប្រើ

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

### ការតាមដាន និងការចាប់សារ

```cmd
# View real-time logs
docker logs -f open-webui

# Monitor container resources
docker stats open-webui

# Check container health
docker inspect open-webui | grep -i health
```

## សំអាត

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

## ជំហានបន្ទាប់

### គំនិតសម្រាប់បង្កើន

1. **Custom Models**: បន្ថែមម៉ូឌែល fine-tuned របស់អ្នកទៅ Foundry Local
2. **API Integration**: ភ្ជាប់ទៅ API ខាងក្រៅតាមលក្ខណៈ Open WebUI functions
3. **Document Processing**: កំណត់បណ្តាញ RAG پیشرفته (advanced RAG pipelines)
4. **Multi-Modal**: កំណត់ម៉ូឌែលវិស័យវិចិត្រសម្រាប់វិភាគរូបភាព

### ការពិចារណាសម្រាប់ការពង្រីក

- **Load Balancing**: គម្លាត Foundry Local ច្រើនក្រោយ reverse proxy
- **Model Routing**: ម៉ូឌែលខុសគ្នាសម្រាប់ករណីប្រើប្រាស់ខុសៗគ្នា
- **Resource Management**: ការបង្កើនប្រសិទ្ធភាពម៉ូម៉ែរី GPU សម្រាប់អ្នកប្រើ​ច្រើន
- **Backup Strategy**: ការបម្រុងទុកទិន្នន័យប្រវត្តិជជែក និងការកំណត់​ជា​ទៀងទាត់

## ឧទាហរណ៍យោង

- [ឯកសារ Open WebUI](https://docs.openwebui.com/)
- [ផ្ទុកគម្រោង GitHub របស់ Open WebUI](https://github.com/open-webui/open-webui)
- [ឯកសារ Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [មគ្គុទេសក៍ដំឡើង Docker](https://docs.docker.com/get-docker/)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការមិនទទួលខុសត្រូវ**:
ឯកសារនេះត្រូវបានបកប្រែដោយប្រើសេវាកម្មបកប្រែ AI [Co-op Translator](https://github.com/Azure/co-op-translator). ខណៈពេលដែលយើងខិតខំប្រឹងប្រែងដើម្បីភាពត្រឹមត្រូវ សូមយកចិត្តទុកដាក់ថាការបកប្រែដោយស្វ័យប្រវត្តិអាចមានកំហុស ឬភាពមិនត្រឹមត្រូវ។ សូមចាត់ទុកឯកសារដើមក្នុងភាសាមូលដ្ឋានរបស់វាថាជាប្រភពផ្លូវការដែលអាចយោងបាន។ សម្រាប់ព័ត៌មានសំខាន់ៗ យើងសូមណែនាំឱ្យប្រើការបកប្រែដោយមនុស្សជំនាញវិជ្ជាជីវៈ។ យើងមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកអត្ថន័យខុស ដែលកើតមានពីការប្រើប្រាស់ការបកប្រែនេះទេ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
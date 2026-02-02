# Foundry Local SDK - สรุปข้อมูลแบบรวดเร็ว

## การติดตั้ง

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

## การจัดการบริการ

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

## รูปแบบการใช้งานพื้นฐาน

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

## การตอบกลับแบบสตรีม

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

## Workshop Utils (แบบง่าย)

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

## ตัวแปรสภาพแวดล้อม

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

## ชื่อเรียกทั่วไปของโมเดล

| ชื่อเรียก | ขนาด | เหมาะสำหรับ |
|-----------|-------|-------------|
| `phi-4-mini` | ~4B | การใช้งานทั่วไป, การสรุปข้อมูล |
| `phi-3.5-mini` | ~3.5B | โค้ด, การปรับปรุงโค้ด |
| `qwen2.5-0.5b` | ~0.5B | การจัดประเภทที่รวดเร็ว |
| `qwen2.5-coder-0.5b` | ~0.5B | การสร้างโค้ด |
| `gemma-2b` | ~2B | การเขียนเชิงสร้างสรรค์ |

## การจัดการข้อผิดพลาด

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

## การแก้ไขปัญหา

### ข้อผิดพลาดในการเชื่อมต่อ
```bash
# Check service
foundry service status

# Restart
foundry service stop
foundry service start

# Test endpoint
curl http://localhost:55769/health
```

### ไม่พบโมเดล
```bash
# List available
foundry model ls

# Download if needed
foundry model download phi-4-mini
```

### ข้อผิดพลาดในการนำเข้า
```bash
# Reinstall SDK
pip uninstall foundry-local-sdk
pip install foundry-local-sdk
```

## ขั้นสูง: การใช้งานหลายโมเดล

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

## เคล็ดลับด้านประสิทธิภาพ

1. **แคชไคลเอนต์**: ใช้ `FoundryLocalManager` ซ้ำ
2. **คำขอแบบแบทช์**: ประมวลผลคำถามหลายคำถามต่อเนื่องกัน
3. **ปรับ max_tokens**: ค่าต่ำ = การตอบกลับที่เร็วขึ้น
4. **โหลดโมเดลล่วงหน้า**: ดาวน์โหลดก่อนใช้งานในระบบจริง
5. **ติดตามการใช้งาน**: ตรวจสอบโทเค็นด้วย `SHOW_USAGE=1`

## แหล่งข้อมูล

- **GitHub**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **Discord**: https://aka.ms/foundry-local-discord
- **Issues**: https://github.com/microsoft/Foundry-Local/issues

---

**เริ่มต้นอย่างรวดเร็ว:**
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

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) แม้ว่าเราจะพยายามให้การแปลมีความถูกต้องมากที่สุด แต่โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางควรถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ ขอแนะนำให้ใช้บริการแปลภาษามนุษย์ที่มีความเชี่ยวชาญ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดที่เกิดจากการใช้การแปลนี้
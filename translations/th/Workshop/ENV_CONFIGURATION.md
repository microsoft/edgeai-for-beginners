<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "05db93129bdc4889e0c5dd3c5ea21498",
  "translation_date": "2025-11-11T23:08:20+00:00",
  "source_file": "Workshop/ENV_CONFIGURATION.md",
  "language_code": "th"
}
-->
# คู่มือการตั้งค่าสภาพแวดล้อม

## ภาพรวม

ตัวอย่างใน Workshop ใช้ตัวแปรสภาพแวดล้อมสำหรับการตั้งค่า ซึ่งรวมศูนย์อยู่ในไฟล์ `.env` ที่อยู่ในรากของ repository เพื่อให้สามารถปรับแต่งได้ง่ายโดยไม่ต้องแก้ไขโค้ด

## เริ่มต้นอย่างรวดเร็ว

### 1. ตรวจสอบข้อกำหนดเบื้องต้น

```bash
# Check Foundry Local is installed
foundry --version

# Check service is running
foundry service status

# Load a model
foundry model run phi-4-mini
```

### 2. ตั้งค่าสภาพแวดล้อม

ไฟล์ `.env` ได้รับการตั้งค่าด้วยค่ามาตรฐานที่เหมาะสมแล้ว ผู้ใช้ส่วนใหญ่ไม่จำเป็นต้องเปลี่ยนแปลงอะไร

**ตัวเลือกเพิ่มเติม**: ตรวจสอบและปรับแต่งการตั้งค่า:
```bash
# Edit .env file
notepad .env  # Windows
nano .env     # macOS/Linux
```

### 3. ใช้การตั้งค่า

**สำหรับสคริปต์ Python:**
```bash
cd Workshop/samples
python -m session01.chat_bootstrap "Your question here"
# Environment variables automatically loaded
```

**สำหรับ Notebooks:**
```python
# Restart kernel after .env changes
# Variables are loaded when cells execute
```

## อ้างอิงตัวแปรสภาพแวดล้อม

### การตั้งค่าหลัก

| ตัวแปร | ค่าเริ่มต้น | คำอธิบาย |
|--------|-------------|-----------|
| `FOUNDRY_LOCAL_ALIAS` | `phi-4-mini` | โมเดลเริ่มต้นสำหรับตัวอย่าง |
| `FOUNDRY_LOCAL_ENDPOINT` | (ว่าง) | กำหนดค่า endpoint ของบริการ |
| `PYTHONPATH` | เส้นทาง Workshop | เส้นทางการค้นหาโมดูล Python |

**เมื่อควรตั้งค่า FOUNDRY_LOCAL_ENDPOINT:**
- การใช้งาน Foundry Local ระยะไกล
- การตั้งค่าพอร์ตแบบกำหนดเอง
- การแยกการพัฒนา/การผลิต

**ตัวอย่าง:**
```bash
# Local custom port
FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Remote instance
FOUNDRY_LOCAL_ENDPOINT=http://192.168.1.50:5273/v1
```

### ตัวแปรเฉพาะเซสชัน

#### เซสชัน 02: RAG Pipeline
| ตัวแปร | ค่าเริ่มต้น | วัตถุประสงค์ |
|--------|-------------|---------------|
| `EMBED_MODEL` | `sentence-transformers/all-MiniLM-L6-v2` | โมเดล embedding |
| `RAG_QUESTION` | ตั้งค่าไว้แล้ว | คำถามทดสอบ |

#### เซสชัน 03: Benchmarking
| ตัวแปร | ค่าเริ่มต้น | วัตถุประสงค์ |
|--------|-------------|---------------|
| `BENCH_MODELS` | `phi-4-mini,qwen2.5-0.5b` | โมเดลสำหรับการทดสอบ |
| `BENCH_ROUNDS` | `3` | จำนวนรอบต่อโมเดล |
| `BENCH_PROMPT` | ตั้งค่าไว้แล้ว | คำสั่งทดสอบ |
| `BENCH_STREAM` | `0` | วัดความล่าช้าของ token แรก |

#### เซสชัน 04: การเปรียบเทียบโมเดล
| ตัวแปร | ค่าเริ่มต้น | วัตถุประสงค์ |
|--------|-------------|---------------|
| `SLM_ALIAS` | `phi-4-mini` | โมเดลภาษาขนาดเล็ก |
| `LLM_ALIAS` | `qwen2.5-7b` | โมเดลภาษาขนาดใหญ่ |
| `COMPARE_PROMPT` | ตั้งค่าไว้แล้ว | คำสั่งเปรียบเทียบ |
| `COMPARE_RETRIES` | `2` | จำนวนครั้งที่ลองใหม่ |

#### เซสชัน 05: การจัดการหลายตัวแทน
| ตัวแปร | ค่าเริ่มต้น | วัตถุประสงค์ |
|--------|-------------|---------------|
| `AGENT_MODEL_PRIMARY` | `phi-4-mini` | โมเดลตัวแทนนักวิจัย |
| `AGENT_MODEL_EDITOR` | `phi-4-mini` | โมเดลตัวแทนบรรณาธิการ |
| `AGENT_QUESTION` | ตั้งค่าไว้แล้ว | คำถามทดสอบ |

### การตั้งค่าความน่าเชื่อถือ

| ตัวแปร | ค่าเริ่มต้น | วัตถุประสงค์ |
|--------|-------------|---------------|
| `SHOW_USAGE` | `1` | แสดงการใช้งาน token |
| `RETRY_ON_FAIL` | `1` | เปิดใช้งานการลองใหม่ |
| `RETRY_BACKOFF` | `1.0` | ความล่าช้าก่อนลองใหม่ (วินาที) |

## การตั้งค่าทั่วไป

### การตั้งค่าสำหรับการพัฒนา (การวนซ้ำเร็ว)
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=phi-4-mini
BENCH_MODELS=phi-4-mini
SHOW_USAGE=1
```

### การตั้งค่าสำหรับการผลิต (เน้นคุณภาพ)
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-7b
AGENT_MODEL_PRIMARY=phi-4-mini
AGENT_MODEL_EDITOR=qwen2.5-7b
SHOW_USAGE=0
```

### การตั้งค่าสำหรับการทดสอบประสิทธิภาพ
```bash
BENCH_MODELS=phi-4-mini,qwen2.5-0.5b,qwen2.5-7b
BENCH_ROUNDS=5
BENCH_STREAM=1
```

### การปรับแต่งหลายตัวแทน
```bash
AGENT_MODEL_PRIMARY=phi-4-mini        # Fast for research
AGENT_MODEL_EDITOR=qwen2.5-7b         # Quality for editing
```

### การพัฒนาระยะไกล
```bash
FOUNDRY_LOCAL_ENDPOINT=http://dev-server.local:5273/v1
FOUNDRY_LOCAL_ALIAS=phi-4-mini
```

## โมเดลที่แนะนำ

### ตามกรณีการใช้งาน

**การใช้งานทั่วไป:**
- `phi-4-mini` - สมดุลระหว่างคุณภาพและความเร็ว

**การตอบสนองเร็ว:**
- `qwen2.5-0.5b` - เร็วมาก เหมาะสำหรับการจัดประเภท
- `phi-4-mini` - เร็วและคุณภาพดี

**คุณภาพสูง:**
- `qwen2.5-7b` - คุณภาพดีที่สุด ใช้ทรัพยากรมากขึ้น
- `phi-4-mini` - คุณภาพดี ใช้ทรัพยากรน้อยกว่า

**การสร้างโค้ด:**
- `deepseek-coder-1.3b` - เชี่ยวชาญด้านโค้ด
- `phi-4-mini` - การเขียนโค้ดทั่วไป

### ตามทรัพยากรที่มี

**ทรัพยากรต่ำ (< 8GB RAM):**
```bash
FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b
SLM_ALIAS=qwen2.5-0.5b
LLM_ALIAS=phi-4-mini
```

**ทรัพยากรปานกลาง (8-16GB RAM):**
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-7b
```

**ทรัพยากรสูง (16GB+ RAM):**
```bash
FOUNDRY_LOCAL_ALIAS=qwen2.5-7b
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-14b
```

## การตั้งค่าขั้นสูง

### Endpoint แบบกำหนดเอง

```bash
# Development environment
FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Staging environment
FOUNDRY_LOCAL_ENDPOINT=http://staging.internal:5273/v1

# Production environment
FOUNDRY_LOCAL_ENDPOINT=http://prod.internal:5273/v1
```

### อุณหภูมิและการสุ่มตัวอย่าง (ปรับในโค้ด)

```python
# In your scripts/notebooks
os.environ['TEMPERATURE'] = '0.7'
os.environ['TOP_P'] = '0.9'
```

### การตั้งค่า Azure OpenAI Hybrid

```bash
# Use local for development
FOUNDRY_LOCAL_ALIAS=phi-4-mini

# Configure Azure for production fallback
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
AZURE_OPENAI_API_KEY=your-key-here
AZURE_OPENAI_API_VERSION=2024-08-01-preview
```

## การแก้ไขปัญหา

### ตัวแปรสภาพแวดล้อมไม่ได้โหลด

**อาการ:**
- สคริปต์ใช้โมเดลผิด
- ข้อผิดพลาดการเชื่อมต่อ
- ตัวแปรไม่ได้รับการยอมรับ

**วิธีแก้ไข:**
```bash
# 1. Verify .env exists in repository root
ls -la .env  # macOS/Linux
dir .env     # Windows

# 2. Check file is not .env.txt (Windows)
# Ensure no hidden extension

# 3. For notebooks: Restart kernel
# Kernel > Restart

# 4. For scripts: Check working directory
pwd  # Should be in Workshop or repository root
```

### ปัญหาการเชื่อมต่อบริการ

**อาการ:**
- ข้อผิดพลาด "Connection refused"
- "Service not available"
- ข้อผิดพลาด timeout

**วิธีแก้ไข:**
```bash
# 1. Check service status
foundry service status

# 2. Start if not running
foundry service start

# 3. Verify endpoint
# Check port in status output
foundry service status | grep "Port"

# 4. Update .env if needed
FOUNDRY_LOCAL_ENDPOINT=http://localhost:<port>
```

### โมเดลไม่พบ

**อาการ:**
- ข้อผิดพลาด "Model not found"
- "Alias not recognized"

**วิธีแก้ไข:**
```bash
# 1. List available models
foundry model list

# 2. Load required model
foundry model run phi-4-mini

# 3. Update .env with available model
FOUNDRY_LOCAL_ALIAS=<available-model>
```

### ข้อผิดพลาดการนำเข้า

**อาการ:**
- ข้อผิดพลาด "Module not found"

**วิธีแก้ไข:**

```bash
# 1. Activate virtual environment
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux

# 2. Install dependencies
pip install -r requirements.txt
```

## การทดสอบการตั้งค่า

### ตรวจสอบการโหลดสภาพแวดล้อม

```python
# test_env.py
import os
from dotenv import load_dotenv

load_dotenv()

print("Core Configuration:")
print(f"  FOUNDRY_LOCAL_ALIAS: {os.getenv('FOUNDRY_LOCAL_ALIAS')}")
print(f"  FOUNDRY_LOCAL_ENDPOINT: {os.getenv('FOUNDRY_LOCAL_ENDPOINT') or 'auto'}")

print("\nSession 04:")
print(f"  SLM_ALIAS: {os.getenv('SLM_ALIAS')}")
print(f"  LLM_ALIAS: {os.getenv('LLM_ALIAS')}")

print("\nSession 05:")
print(f"  AGENT_MODEL_PRIMARY: {os.getenv('AGENT_MODEL_PRIMARY')}")
print(f"  AGENT_MODEL_EDITOR: {os.getenv('AGENT_MODEL_EDITOR')}")
```

### ทดสอบการเชื่อมต่อ Foundry Local

```python
# test_connection.py
import os
from foundry_local import FoundryLocalManager

alias = os.getenv('FOUNDRY_LOCAL_ALIAS', 'phi-4-mini')
endpoint = os.getenv('FOUNDRY_LOCAL_ENDPOINT')

try:
    if endpoint:
        manager = FoundryLocalManager(alias, endpoint=endpoint)
    else:
        manager = FoundryLocalManager(alias)
    
    print(f"✓ Connected to {manager.endpoint}")
    print(f"✓ Model: {manager.get_model_info(alias).id}")
    print(f"✓ Available models: {len(manager.list_models())}")
except Exception as e:
    print(f"✗ Connection failed: {e}")
```

## แนวทางปฏิบัติที่ดีที่สุดด้านความปลอดภัย

### 1. อย่าคอมมิตข้อมูลลับ

```bash
# .gitignore should include:
.env
.env.local
*.key
```

### 2. ใช้ไฟล์ .env แยกต่างหาก

```bash
.env              # Default configuration
.env.local        # Local overrides (gitignored)
.env.production   # Production config (secure storage)
```

### 3. หมุนเวียน API Keys

```bash
# For Azure OpenAI or other cloud services
# Regularly rotate keys and update .env
```

### 4. ใช้การตั้งค่าที่เฉพาะเจาะจงกับสภาพแวดล้อม

```bash
# Development
FOUNDRY_LOCAL_ENDPOINT=http://localhost:5273/v1

# Production (use secrets management)
FOUNDRY_LOCAL_ENDPOINT=${PROD_FOUNDRY_ENDPOINT}
```

## เอกสาร SDK

- **Repository หลัก**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **เอกสาร API**: ตรวจสอบ repository SDK สำหรับข้อมูลล่าสุด

## แหล่งข้อมูลเพิ่มเติม

- `QUICK_START.md` - คู่มือเริ่มต้นใช้งาน
- `Workshop/samples/*/README.md` - คู่มือเฉพาะตัวอย่าง

---

**อัปเดตล่าสุด**: 2025-01-08  
**เวอร์ชัน**: 2.0  
**SDK**: Foundry Local Python SDK (ล่าสุด)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) แม้ว่าเราจะพยายามให้การแปลมีความถูกต้อง แต่โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาดั้งเดิมควรถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ ขอแนะนำให้ใช้บริการแปลภาษามืออาชีพ เราจะไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดที่เกิดจากการใช้การแปลนี้
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
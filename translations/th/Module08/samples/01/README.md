# ตัวอย่าง 01: แชทอย่างรวดเร็วผ่าน OpenAI SDK

ตัวอย่างแชทง่ายๆ ที่แสดงวิธีการใช้ OpenAI SDK ร่วมกับ Microsoft Foundry Local สำหรับการประมวลผล AI ในเครื่อง

## ภาพรวม

ตัวอย่างนี้แสดงวิธีการ:
- ใช้ OpenAI Python SDK กับ Foundry Local
- จัดการทั้งการตั้งค่าของ Azure OpenAI และ Foundry Local
- ใช้การจัดการข้อผิดพลาดและกลยุทธ์สำรองอย่างเหมาะสม
- ใช้ FoundryLocalManager สำหรับการจัดการบริการ

## สิ่งที่ต้องเตรียม

- **Foundry Local**: ติดตั้งและสามารถใช้งานได้ผ่าน PATH
- **Python**: เวอร์ชัน 3.8 หรือใหม่กว่า
- **โมเดล**: โมเดลที่โหลดใน Foundry Local (เช่น `phi-4-mini`)

## การติดตั้ง

1. **ตั้งค่าสภาพแวดล้อม Python:**
   ```cmd
   cd Module08
   py -m venv .venv
   .venv\Scripts\activate
   ```

2. **ติดตั้ง dependencies:**
   ```cmd
   pip install -r requirements.txt
   ```

3. **เริ่มบริการ Foundry Local และโหลดโมเดล:**
   ```cmd
   foundry model run phi-4-mini
   ```

## การใช้งาน

### Foundry Local (ค่าเริ่มต้น)

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

## คุณสมบัติของโค้ด

### การผสาน FoundryLocalManager

ตัวอย่างนี้ใช้ Foundry Local SDK อย่างเป็นทางการสำหรับการจัดการบริการอย่างเหมาะสม:

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

### การจัดการข้อผิดพลาด

การจัดการข้อผิดพลาดที่มีประสิทธิภาพพร้อมกลยุทธ์สำรอง:
- การค้นหาบริการอัตโนมัติ
- การลดระดับการทำงานอย่างราบรื่นหาก SDK ไม่พร้อมใช้งาน
- ข้อความแสดงข้อผิดพลาดที่ชัดเจนสำหรับการแก้ไขปัญหา

## ตัวแปรสภาพแวดล้อม

| ตัวแปร | คำอธิบาย | ค่าเริ่มต้น | จำเป็น |
|--------|-----------|-------------|--------|
| `MODEL` | ชื่อหรือ alias ของโมเดล | `phi-4-mini` | ไม่ |
| `BASE_URL` | URL ฐานของ Foundry Local | `http://localhost:8000` | ไม่ |
| `API_KEY` | API key (โดยปกติไม่จำเป็นสำหรับการใช้งานในเครื่อง) | `""` | ไม่ |
| `AZURE_OPENAI_ENDPOINT` | Endpoint ของ Azure OpenAI | - | สำหรับ Azure |
| `AZURE_OPENAI_API_KEY` | API key ของ Azure OpenAI | - | สำหรับ Azure |
| `AZURE_OPENAI_API_VERSION` | เวอร์ชัน API ของ Azure | `2024-08-01-preview` | ไม่ |

## การแก้ไขปัญหา

### ปัญหาทั่วไป

1. **"ไม่สามารถใช้ Foundry SDK" คำเตือน:**
   - ติดตั้ง foundry-local-sdk: `pip install foundry-local-sdk`
   - หรือกำหนดตัวแปรสภาพแวดล้อมสำหรับการตั้งค่าด้วยตนเอง

2. **การเชื่อมต่อถูกปฏิเสธ:**
   - ตรวจสอบว่า Foundry Local กำลังทำงานอยู่: `foundry service status`
   - ตรวจสอบว่ามีการโหลดโมเดลแล้ว: `foundry service ps`

3. **ไม่พบโมเดล:**
   - แสดงรายการโมเดลที่มีอยู่: `foundry model list`
   - โหลดโมเดล: `foundry model run phi-4-mini`

### การตรวจสอบ

```cmd
# Check Foundry Local status
foundry service status

# List loaded models
foundry service ps

# Test API endpoint
curl http://localhost:8000/v1/models
```

## อ้างอิง

- [เอกสาร Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [OpenAI Python SDK](https://github.com/openai/openai-python)
- [Foundry Local GitHub](https://github.com/microsoft/Foundry-Local)
- [เอกสาร API ที่เข้ากันได้กับ OpenAI](https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks)

---


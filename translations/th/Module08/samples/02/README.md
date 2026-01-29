# ตัวอย่าง 02: การผสานรวม OpenAI SDK

แสดงการผสานรวมขั้นสูงกับ OpenAI Python SDK ที่รองรับทั้ง Microsoft Foundry Local และ Azure OpenAI พร้อมการตอบกลับแบบสตรีมและการจัดการข้อผิดพลาดอย่างเหมาะสม

## ภาพรวม

ตัวอย่างนี้แสดงให้เห็น:
- การสลับระหว่าง Foundry Local และ Azure OpenAI อย่างไร้รอยต่อ
- การตอบกลับแบบสตรีมเพื่อประสบการณ์ผู้ใช้ที่ดียิ่งขึ้น
- การใช้งาน FoundryLocalManager SDK อย่างเหมาะสม
- การจัดการข้อผิดพลาดและกลไกสำรองที่แข็งแกร่ง
- รูปแบบโค้ดที่พร้อมใช้งานในระดับการผลิต

## ข้อกำหนดเบื้องต้น

- **Foundry Local**: ติดตั้งและทำงานอยู่ (สำหรับการประมวลผลในเครื่อง)
- **Python**: เวอร์ชัน 3.8 หรือใหม่กว่าพร้อม OpenAI SDK
- **Azure OpenAI**: Endpoint และ API key ที่ถูกต้อง (สำหรับการประมวลผลบนคลาวด์)

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

3. **เริ่มต้น Foundry Local (สำหรับโหมดในเครื่อง):**
   ```cmd
   foundry model run phi-4-mini
   ```


## สถานการณ์การใช้งาน

### Foundry Local (ค่าเริ่มต้น)

**ตัวเลือกที่ 1: ใช้ FoundryLocalManager (แนะนำ)**
```cmd
# Automatic service discovery and model management
set MODEL=phi-4-mini
python samples\02\sdk_quickstart.py
```

**ตัวเลือกที่ 2: การตั้งค่าด้วยตนเอง**
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


## สถาปัตยกรรมโค้ด

### รูปแบบ Client Factory

ตัวอย่างนี้ใช้รูปแบบ factory ในการสร้าง client ที่เหมาะสม:

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


### การตอบกลับแบบสตรีม

ตัวอย่างนี้แสดงการตอบกลับแบบสตรีมเพื่อการสร้างคำตอบแบบเรียลไทม์:

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


## ตัวแปรสภาพแวดล้อม

### การตั้งค่า Foundry Local

| ตัวแปร | คำอธิบาย | ค่าเริ่มต้น | จำเป็น |
|--------|-----------|-------------|--------|
| `MODEL` | ชื่อโมเดลที่จะใช้ | `phi-4-mini` | ไม่ |
| `BASE_URL` | Endpoint ของ Foundry Local | `http://localhost:8000` | ไม่ |
| `API_KEY` | API key (ไม่จำเป็นสำหรับโหมดในเครื่อง) | `""` | ไม่ |

### การตั้งค่า Azure OpenAI

| ตัวแปร | คำอธิบาย | ค่าเริ่มต้น | จำเป็น |
|--------|-----------|-------------|--------|
| `AZURE_OPENAI_ENDPOINT` | Endpoint ของทรัพยากร Azure OpenAI | - | ใช่ |
| `AZURE_OPENAI_API_KEY` | API key ของ Azure OpenAI | - | ใช่ |
| `AZURE_OPENAI_API_VERSION` | เวอร์ชัน API | `2024-08-01-preview` | ไม่ |
| `MODEL` | ชื่อการปรับใช้ของ Azure | `your-deployment-name` | ใช่ |

## ฟีเจอร์ขั้นสูง

### การค้นหาบริการอัตโนมัติ

ตัวอย่างนี้ตรวจจับบริการที่เหมาะสมโดยอัตโนมัติจากตัวแปรสภาพแวดล้อม:

1. **โหมด Azure**: หากตั้งค่า `AZURE_OPENAI_ENDPOINT` และ `AZURE_OPENAI_API_KEY`
2. **โหมด Foundry SDK**: หาก Foundry Local SDK พร้อมใช้งาน
3. **โหมด Manual**: สำรองไปยังการตั้งค่าด้วยตนเอง

### การจัดการข้อผิดพลาด

- การสำรองจาก SDK ไปยังการตั้งค่าด้วยตนเองอย่างราบรื่น
- ข้อความแสดงข้อผิดพลาดที่ชัดเจนสำหรับการแก้ไขปัญหา
- การจัดการข้อยกเว้นอย่างเหมาะสมสำหรับปัญหาเครือข่าย
- การตรวจสอบตัวแปรสภาพแวดล้อมที่จำเป็น

## การพิจารณาด้านประสิทธิภาพ

### การเปรียบเทียบระหว่างในเครื่องและคลาวด์

**ข้อดีของ Foundry Local:**
- ✅ ไม่มีค่าใช้จ่าย API
- ✅ ความเป็นส่วนตัวของข้อมูล (ข้อมูลไม่ออกจากอุปกรณ์)
- ✅ ความหน่วงต่ำสำหรับโมเดลที่รองรับ
- ✅ ใช้งานได้แบบออฟไลน์

**ข้อดีของ Azure OpenAI:**
- ✅ เข้าถึงโมเดลขนาดใหญ่ล่าสุด
- ✅ อัตราการประมวลผลสูงกว่า
- ✅ ไม่ต้องการทรัพยากรคอมพิวเตอร์ในเครื่อง
- ✅ SLA ระดับองค์กร

## การแก้ไขปัญหา

### ปัญหาทั่วไป

1. **คำเตือน "ไม่สามารถใช้ Foundry SDK":**
   ```cmd
   pip install foundry-local-sdk
   ```

2. **ข้อผิดพลาดการตรวจสอบสิทธิ์ Azure:**
   ```cmd
   # Verify your endpoint format
   echo %AZURE_OPENAI_ENDPOINT%
   # Should be: https://your-resource.openai.azure.com
   ```

3. **โมเดลไม่พร้อมใช้งาน:**
   ```cmd
   # For Foundry Local
   foundry model list
   foundry model run your-model-name
   
   # For Azure OpenAI
   # Check your deployment name in Azure Portal
   ```


### การตรวจสอบสถานะ

```cmd
# Foundry Local
foundry service status
curl http://localhost:8000/v1/models

# Azure OpenAI
curl -H "api-key: %AZURE_OPENAI_API_KEY%" "%AZURE_OPENAI_ENDPOINT%/openai/deployments?api-version=2024-08-01-preview"
```


## ขั้นตอนถัดไป

- **ตัวอย่าง 03**: การค้นหาโมเดลและการวัดประสิทธิภาพ
- **ตัวอย่าง 04**: การสร้างแอปพลิเคชัน Chainlit RAG
- **ตัวอย่าง 05**: การจัดการหลายตัวแทน
- **ตัวอย่าง 06**: การกำหนดเส้นทางโมเดลเป็นเครื่องมือ

## อ้างอิง

- [เอกสาร Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/)
- [เอกสารอ้างอิง Foundry Local SDK](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [เอกสาร OpenAI Python SDK](https://github.com/openai/openai-python)
- [คู่มือการตอบกลับแบบสตรีม](https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/integrate-with-inference-sdks)

---


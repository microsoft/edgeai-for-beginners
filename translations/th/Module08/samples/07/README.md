# ตัวอย่างการใช้ Foundry Local เป็น API

ตัวอย่างนี้แสดงวิธีการใช้ Microsoft Foundry Local เป็นบริการ REST API โดยไม่ต้องพึ่งพา OpenAI SDK ซึ่งแสดงรูปแบบการผสานรวม HTTP โดยตรงเพื่อการควบคุมและปรับแต่งสูงสุด

## ภาพรวม

อ้างอิงจากรูปแบบ Foundry Local อย่างเป็นทางการของ Microsoft ตัวอย่างนี้มี:
- การผสานรวม REST API โดยตรงกับ FoundryLocalManager
- การใช้งาน HTTP client แบบกำหนดเอง
- การจัดการโมเดลและการตรวจสอบสุขภาพ
- การจัดการการตอบกลับแบบสตรีมและไม่ใช่สตรีม
- การจัดการข้อผิดพลาดและตรรกะการลองใหม่ที่พร้อมใช้งานในระดับการผลิต

## สิ่งที่ต้องเตรียม

1. **การติดตั้ง Foundry Local**
   ```powershell
   # Install from GitHub releases
   winget install Microsoft.FoundryLocal
   ```

2. **ไลบรารี Python ที่จำเป็น**
   ```bash
   pip install foundry-local-sdk requests asyncio aiohttp
   ```

## สถาปัตยกรรม

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Your App      │───▶│  REST API Client │───▶│  Foundry Local  │
│                 │    │                  │    │   Service       │
│ - Custom Logic  │    │ - HTTP Requests  │    │ - Model Loading │
│ - Business Rules│    │ - Authentication │    │ - Inference     │
│ - Data Pipeline │    │ - Error Handling │    │ - Health Check  │
└─────────────────┘    └──────────────────┘    └─────────────────┘
```

## คุณสมบัติสำคัญ

### 1. **การผสานรวม HTTP โดยตรง**
- การเรียก REST API โดยไม่ต้องพึ่ง SDK
- การรับรองความถูกต้องและการตั้งค่า headers แบบกำหนดเอง
- การควบคุมเต็มรูปแบบในการจัดการคำขอและการตอบกลับ

### 2. **การจัดการโมเดล**
- การโหลดและยกเลิกการโหลดโมเดลแบบไดนามิก
- การตรวจสอบสุขภาพและสถานะ
- การรวบรวมข้อมูลประสิทธิภาพ

### 3. **รูปแบบการใช้งานในระดับการผลิต**
- กลไกการลองใหม่พร้อมการเพิ่มเวลารอแบบทวีคูณ
- Circuit breaker เพื่อความทนทานต่อข้อผิดพลาด
- การบันทึกและการตรวจสอบที่ครอบคลุม

### 4. **การจัดการการตอบกลับที่ยืดหยุ่น**
- การตอบกลับแบบสตรีมสำหรับแอปพลิเคชันเรียลไทม์
- การประมวลผลแบบแบทช์สำหรับสถานการณ์ที่มีปริมาณงานสูง
- การแยกวิเคราะห์และการตรวจสอบการตอบกลับแบบกำหนดเอง

## ตัวอย่างการใช้งาน

### การผสานรวม API พื้นฐาน
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

### การผสานรวมแบบสตรีม
```python
# Stream responses for real-time applications
async for chunk in client.stream_complete(
    prompt="Write a story about AI",
    model="phi-4-mini"
):
    print(chunk.content, end="", flush=True)
```

### การตรวจสอบสุขภาพ
```python
# Check service health
health = await client.health_check()
print(f"Service Status: {health.status}")
print(f"Active Models: {health.loaded_models}")
print(f"Memory Usage: {health.memory_usage}")
```

## โครงสร้างไฟล์

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

## การผสานรวม Microsoft Foundry Local

ตัวอย่างนี้ปฏิบัติตามรูปแบบอย่างเป็นทางการของ Microsoft:

1. **การผสานรวม SDK**: ใช้ `FoundryLocalManager` สำหรับการจัดการบริการ
2. **REST Endpoints**: การเรียก `/v1/chat/completions` และ endpoints อื่น ๆ โดยตรง
3. **การรับรองความถูกต้อง**: การจัดการ API key อย่างเหมาะสมสำหรับบริการในเครื่อง
4. **การจัดการโมเดล**: การแสดงรายการ การดาวน์โหลด และรูปแบบการโหลดโมเดล
5. **การจัดการข้อผิดพลาด**: รหัสข้อผิดพลาดและการตอบกลับที่แนะนำโดย Microsoft

## เริ่มต้นใช้งาน

1. **ติดตั้งไลบรารีที่จำเป็น**
   ```bash
   pip install -r requirements.txt
   ```

2. **เรียกใช้งานตัวอย่างพื้นฐาน**
   ```bash
   python examples/basic_usage.py
   ```

3. **ลองใช้งานแบบสตรีม**
   ```bash
   python examples/streaming.py
   ```

4. **ตั้งค่าการใช้งานในระดับการผลิต**
   ```bash
   python examples/production.py
   ```

## การตั้งค่า

ตัวแปรสภาพแวดล้อมสำหรับการปรับแต่ง:
- `FOUNDRY_MODEL`: โมเดลเริ่มต้นที่จะใช้ (ค่าเริ่มต้น: "phi-4-mini")
- `FOUNDRY_TIMEOUT`: เวลารอคำขอในวินาที (ค่าเริ่มต้น: 30)
- `FOUNDRY_RETRIES`: จำนวนครั้งที่ลองใหม่ (ค่าเริ่มต้น: 3)
- `FOUNDRY_LOG_LEVEL`: ระดับการบันทึก (ค่าเริ่มต้น: "INFO")

## แนวทางปฏิบัติที่ดีที่สุด

1. **การจัดการการเชื่อมต่อ**: ใช้การเชื่อมต่อ HTTP ซ้ำเพื่อประสิทธิภาพที่ดีขึ้น
2. **การจัดการข้อผิดพลาด**: ใช้ตรรกะการลองใหม่ที่เหมาะสมพร้อมการเพิ่มเวลารอแบบทวีคูณ
3. **การตรวจสอบทรัพยากร**: ติดตามการใช้งานหน่วยความจำโมเดลและประสิทธิภาพ
4. **ความปลอดภัย**: ใช้การรับรองความถูกต้องที่เหมาะสมแม้สำหรับบริการในเครื่อง
5. **การทดสอบ**: รวมการทดสอบหน่วยและการทดสอบการผสานรวม

## การแก้ไขปัญหา

### ปัญหาทั่วไป

**บริการไม่ทำงาน**
```bash
# Check Foundry Local status
foundry status

# Start if needed
foundry start
```

**ปัญหาการโหลดโมเดล**
```bash
# List available models
foundry model list

# Download specific model
foundry model download phi-4-mini
```

**ข้อผิดพลาดการเชื่อมต่อ**
- ตรวจสอบว่า Foundry Local ทำงานบนพอร์ตที่ถูกต้อง
- ตรวจสอบการตั้งค่าไฟร์วอลล์
- ตรวจสอบ headers การรับรองความถูกต้อง

## การปรับปรุงประสิทธิภาพ

1. **การจัดกลุ่มการเชื่อมต่อ**: ใช้ session objects สำหรับคำขอหลายรายการ
2. **การดำเนินการแบบอะซิงโครนัส**: ใช้ asyncio สำหรับคำขอพร้อมกัน
3. **การแคช**: แคชการตอบกลับโมเดลในกรณีที่เหมาะสม
4. **การตรวจสอบ**: ติดตามเวลาตอบกลับและปรับเวลารอ

## ผลลัพธ์การเรียนรู้

หลังจากทำตัวอย่างนี้เสร็จ คุณจะเข้าใจ:
- การผสานรวม REST API โดยตรงกับ Foundry Local
- รูปแบบการใช้งาน HTTP client แบบกำหนดเอง
- การจัดการข้อผิดพลาดและการตรวจสอบที่พร้อมใช้งานในระดับการผลิต
- สถาปัตยกรรมบริการ Microsoft Foundry Local
- เทคนิคการปรับปรุงประสิทธิภาพสำหรับบริการ AI ในเครื่อง

## ขั้นตอนถัดไป

- สำรวจตัวอย่างที่ 08: แอปพลิเคชันแชท Windows 11
- ลองตัวอย่างที่ 09: การจัดการหลายเอเจนต์
- เรียนรู้ตัวอย่างที่ 10: การผสานรวม Foundry Local เป็นเครื่องมือ

---


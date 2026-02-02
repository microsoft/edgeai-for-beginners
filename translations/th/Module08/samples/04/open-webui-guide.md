# คู่มือการเชื่อมต่อ Open WebUI + Foundry Local

คู่มือนี้จะแสดงวิธีการเชื่อมต่อ Open WebUI กับ Microsoft Foundry Local เพื่อสร้างอินเทอร์เฟซแบบมืออาชีพที่คล้าย ChatGPT โดยใช้โมเดล AI ในเครื่องของคุณ

## ภาพรวม

Open WebUI มอบอินเทอร์เฟซการแชทที่ทันสมัยและใช้งานง่าย ซึ่งสามารถเชื่อมต่อกับ API ที่เข้ากันได้กับ OpenAI โดยการเชื่อมต่อกับ Foundry Local คุณจะได้รับ:

- **UI ระดับมืออาชีพ**: อินเทอร์เฟซที่คล้าย ChatGPT พร้อมดีไซน์ทันสมัย
- **ความเป็นส่วนตัวในเครื่อง**: การประมวลผลทั้งหมดเกิดขึ้นในอุปกรณ์ของคุณ
- **การสลับโมเดล**: สลับระหว่างโมเดลในเครื่องได้ง่าย
- **ประวัติการสนทนา**: บันทึกประวัติการแชทและบริบทอย่างต่อเนื่อง
- **การอัปโหลดไฟล์**: วิเคราะห์เอกสารและประมวลผลไฟล์
- **บุคลิกเฉพาะตัว**: ปรับแต่งคำสั่งระบบและบทบาท

## สิ่งที่ต้องเตรียม

### ซอฟต์แวร์ที่จำเป็น

```cmd
# Verify Foundry Local installation
foundry --version

# Verify Docker installation
docker --version

# Start Foundry Local service
foundry service start
```

### โหลดโมเดล

```cmd
# List available models
foundry model list

# Load your preferred model
foundry model run phi-4-mini

# Verify model is running
foundry service ps
```

## การตั้งค่าแบบรวดเร็ว (แนะนำ)

### ขั้นตอนที่ 1: รัน Open WebUI ด้วย Docker

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

### ขั้นตอนที่ 2: การตั้งค่าเริ่มต้น

1. **เปิดเบราว์เซอร์**: ไปที่ `http://localhost:3000`
2. **สร้างบัญชี**: ตั้งค่าผู้ใช้แอดมิน (ผู้ใช้คนแรกจะกลายเป็นแอดมิน)
3. **ตรวจสอบการเชื่อมต่อ**: โมเดลควรปรากฏในเมนูแบบเลื่อนลงโดยอัตโนมัติ

### ขั้นตอนที่ 3: ทดสอบการเชื่อมต่อ

1. เลือกโมเดลจากเมนูแบบเลื่อนลง (เช่น "phi-4-mini")
2. พิมพ์ข้อความทดสอบ: "สวัสดี! คุณช่วยแนะนำตัวเองได้ไหม?"
3. คุณควรเห็นการตอบกลับแบบสตรีมจากโมเดลในเครื่องของคุณ

## การตั้งค่าขั้นสูง

### ตัวแปรสภาพแวดล้อม

| ตัวแปร | วัตถุประสงค์ | ค่าเริ่มต้น | ตัวอย่าง |
|--------|---------------|--------------|-----------|
| `OPENAI_API_BASE_URL` | จุดเชื่อมต่อ Foundry Local | - | `http://host.docker.internal:51211/v1` |
| `OPENAI_API_KEY` | คีย์ API (จำเป็นแต่ไม่ได้ใช้ในเครื่อง) | - | `foundry-local-key` |
| `WEBUI_SECRET_KEY` | คีย์การเข้ารหัสเซสชัน | สร้างอัตโนมัติ | `your-secret-key` |
| `ENABLE_SIGNUP` | อนุญาตการลงทะเบียนผู้ใช้ใหม่ | `True` | `False` |

### การตั้งค่าด้วยตนเอง (ทางเลือก)

หากตัวแปรสภาพแวดล้อมไม่ทำงาน ให้ตั้งค่าด้วยตนเอง:

1. **เปิดการตั้งค่า**: คลิกที่ไอคอนการตั้งค่า (รูปเฟือง)
2. **ไปที่การเชื่อมต่อ**: การตั้งค่า → การเชื่อมต่อ → OpenAI
3. **ตั้งค่ารายละเอียด API**:
   - API Base URL: `http://host.docker.internal:51211/v1`
   - API Key: `foundry-local-key` (ค่าใดก็ได้)
4. **บันทึกและทดสอบ**: คลิก "บันทึก" แล้วทดสอบด้วยโมเดล

### การจัดเก็บข้อมูลแบบถาวร

เพื่อบันทึกการสนทนาและการตั้งค่า:

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

## การแก้ไขปัญหา

### ปัญหาการเชื่อมต่อ

**ปัญหา**: "Connection refused" หรือโมเดลไม่โหลด

**วิธีแก้ไข**:
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

### โมเดลไม่ปรากฏ

**ปัญหา**: Open WebUI ไม่แสดงโมเดลในเมนูแบบเลื่อนลง

**ขั้นตอนการแก้ไข**:
```cmd
# Check if model is loaded in Foundry Local
foundry model list

# Test API response
curl -X GET http://localhost:51211/v1/models \
  -H "Content-Type: application/json"

# Verify correct port (should be 51211 for Foundry Local)
netstat -ano | findstr :51211
```

**วิธีแก้ไข**: ตรวจสอบว่าโมเดลโหลดอย่างถูกต้อง:
```cmd
# Stop and restart model
foundry model stop phi-4-mini
foundry model run phi-4-mini

# Wait for model to fully load, then refresh Open WebUI
```

### ปัญหาเครือข่าย Docker

**ปัญหา**: `host.docker.internal` ไม่สามารถแก้ไขได้

**วิธีแก้ไขสำหรับ Windows**:
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

**ทางเลือก**: ค้นหา IP ของเครื่องของคุณ:
```cmd
ipconfig | findstr IPv4
# Use your actual IP instead of host.docker.internal
# Example: http://192.168.1.100:51211/v1
```

### ปัญหาด้านประสิทธิภาพ

**การตอบกลับช้า**:
1. ตรวจสอบว่าโมเดลใช้ GPU acceleration: `foundry service ps`
2. ตรวจสอบทรัพยากรระบบเพียงพอ (RAM/หน่วยความจำ GPU)
3. ลองใช้โมเดลที่เล็กลงสำหรับการทดสอบ

**ปัญหาหน่วยความจำ**:
```cmd
# Check Docker container memory usage
docker stats open-webui

# Restart Docker if needed
docker restart open-webui
```

## คู่มือการใช้งาน

### การแชทพื้นฐาน

1. **เลือกโมเดล**: เลือกจากเมนูแบบเลื่อนลง (แสดงโมเดล Foundry Local)
2. **พิมพ์ข้อความ**: ใช้ช่องข้อความที่ด้านล่าง
3. **ส่งข้อความ**: กด Enter หรือคลิกปุ่มส่ง
4. **ดูการตอบกลับ**: ดูการตอบกลับแบบสตรีมแบบเรียลไทม์

### ฟีเจอร์ขั้นสูง

**การอัปโหลดไฟล์**:
1. คลิกไอคอนคลิปหนีบกระดาษ
2. อัปโหลดเอกสาร (PDF, TXT ฯลฯ)
3. ถามคำถามเกี่ยวกับเนื้อหา
4. โมเดลจะวิเคราะห์และตอบกลับตามเอกสาร

**คำสั่งระบบแบบกำหนดเอง**:
1. การตั้งค่า → การปรับแต่ง
2. ตั้งค่าคำสั่งระบบแบบกำหนดเอง
3. สร้างบุคลิก/พฤติกรรม AI ที่สม่ำเสมอ

**การจัดการการสนทนา**:
- **เริ่มแชทใหม่**: คลิก "+" เพื่อเริ่มการสนทนาใหม่
- **ประวัติการแชท**: เข้าถึงการสนทนาก่อนหน้าในแถบด้านข้าง
- **ส่งออก**: ดาวน์โหลดประวัติการแชทเป็นข้อความ/JSON

**การเปรียบเทียบโมเดล**:
1. เปิดแท็บเบราว์เซอร์หลายแท็บไปยัง Open WebUI เดียวกัน
2. เลือกโมเดลต่างๆ ในแต่ละแท็บ
3. เปรียบเทียบการตอบกลับต่อคำถามเดียวกัน

### รูปแบบการผสานรวม

**เวิร์กโฟลว์การพัฒนา**:
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

## การปรับใช้ในระบบจริง

### การตั้งค่าที่ปลอดภัย

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

### การตั้งค่าหลายผู้ใช้

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

### การตรวจสอบและบันทึก

```cmd
# View real-time logs
docker logs -f open-webui

# Monitor container resources
docker stats open-webui

# Check container health
docker inspect open-webui | grep -i health
```

## การล้างข้อมูล

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

## ขั้นตอนถัดไป

### แนวคิดการปรับปรุง

1. **โมเดลแบบกำหนดเอง**: เพิ่มโมเดลที่ปรับแต่งเองใน Foundry Local
2. **การเชื่อมต่อ API**: เชื่อมต่อกับ API ภายนอกผ่านฟังก์ชัน Open WebUI
3. **การประมวลผลเอกสาร**: ตั้งค่าท่อ RAG ขั้นสูง
4. **มัลติโหมด**: ตั้งค่าโมเดลภาพสำหรับการวิเคราะห์ภาพ

### การพิจารณาด้านการขยาย

- **การปรับสมดุลโหลด**: หลายอินสแตนซ์ Foundry Local หลังพร็อกซีแบบย้อนกลับ
- **การกำหนดเส้นทางโมเดล**: โมเดลต่างๆ สำหรับกรณีการใช้งานที่แตกต่างกัน
- **การจัดการทรัพยากร**: การปรับแต่งหน่วยความจำ GPU สำหรับผู้ใช้พร้อมกัน
- **กลยุทธ์การสำรองข้อมูล**: สำรองข้อมูลการสนทนาและการตั้งค่าเป็นประจำ

## อ้างอิง

- [เอกสาร Open WebUI](https://docs.openwebui.com/)
- [ที่เก็บ GitHub ของ Open WebUI](https://github.com/open-webui/open-webui)
- [เอกสาร Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [คู่มือการติดตั้ง Docker](https://docs.docker.com/get-docker/)

---


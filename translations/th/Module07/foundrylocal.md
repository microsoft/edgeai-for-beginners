# Foundry Local บน Windows และ Mac

คู่มือนี้ช่วยคุณติดตั้ง, รัน และรวม Microsoft Foundry Local บน Windows และ Mac ขั้นตอนและคำสั่งทั้งหมดได้รับการตรวจสอบกับเอกสาร Microsoft Learn แล้ว

- เริ่มต้นใช้งาน: https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started
- สถาปัตยกรรม: https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture
- อ้างอิง CLI: https://learn.microsoft.com/azure/ai-foundry/foundry-local/reference/reference-cli
- รวม SDKs: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks
- คอมไพล์โมเดล HF (BYOM): https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models
- Windows AI: Local vs Cloud: https://learn.microsoft.com/windows/ai/cloud-ai#key-decision-factors-for-app-developers

## 1) ติดตั้ง / อัปเกรดบน Windows

- ติดตั้ง:
```cmd
winget install Microsoft.FoundryLocal
```
- อัปเกรด:
```cmd
winget upgrade --id Microsoft.FoundryLocal
```
- ตรวจสอบเวอร์ชัน:
```cmd
foundry --version
```
     
**ติดตั้ง / Mac**

**MacOS**: 
เปิด terminal และรันคำสั่งต่อไปนี้:
```bash
   brew tap microsoft/foundrylocal
   brew install foundrylocal
```

## 2) พื้นฐาน CLI (สามหมวดหมู่)

- โมเดล:
```cmd
foundry model --help
foundry model list
foundry model run gpt-oss-20b
```
- บริการ:
```cmd
foundry service --help
foundry service status
foundry service ps
```
- แคช:
```cmd
foundry cache --help
foundry cache list
```

หมายเหตุ:
- บริการนี้เปิดเผย REST API ที่เข้ากันได้กับ OpenAI พอร์ต endpoint จะถูกจัดสรรแบบไดนามิก ใช้ `foundry service status` เพื่อค้นหา
- ใช้ SDKs เพื่อความสะดวก; SDKs จะจัดการการค้นหา endpoint โดยอัตโนมัติในกรณีที่รองรับ

## 3) ค้นหา Local Endpoint (Dynamic Port)

Foundry Local จะกำหนดพอร์ตแบบไดนามิกทุกครั้งที่บริการเริ่มต้น:
```cmd
foundry service status
```
ใช้ `http://localhost:<PORT>` ที่รายงานเป็น `base_url` ของคุณพร้อมเส้นทางที่เข้ากันได้กับ OpenAI (เช่น `/v1/chat/completions`)

## 4) ทดสอบอย่างรวดเร็วผ่าน OpenAI Python SDK

```cmd
set BASE_URL=http://localhost:PORT
python - <<PY
from openai import OpenAI
client = OpenAI(base_url="%BASE_URL%/v1", api_key="")
resp = client.chat.completions.create(
    model="gpt-oss-20b",
    messages=[{"role":"user","content":"Say hello from Foundry Local."}],
    max_tokens=64,
)
print(resp.choices[0].message.content)
PY
```
อ้างอิง:
- การรวม SDK: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

## 5) นำโมเดลของคุณมาเอง (คอมไพล์ด้วย Olive)

หากคุณต้องการโมเดลที่ไม่มีในแคตตาล็อก ให้คอมไพล์เป็น ONNX สำหรับ Foundry Local โดยใช้ Olive

ขั้นตอนระดับสูง (ดูเอกสารสำหรับรายละเอียด):
```cmd
foundry cache cd models
foundry cache list
foundry model run llama-3.2 --verbose
```
เอกสาร:
- คอมไพล์ BYOM: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models

## 6) การแก้ไขปัญหา

- ตรวจสอบสถานะและล็อกของบริการ:
```cmd
foundry service status
foundry service diag
```
- ล้างหรือย้ายแคช:
```cmd
foundry cache list
foundry cache remove <model>
foundry cache cd <path>
```
- อัปเดตเป็นตัวอย่างล่าสุด:
```cmd
winget upgrade --id Microsoft.FoundryLocal
```

## 7) ประสบการณ์นักพัฒนาที่เกี่ยวข้องกับ Windows

- ตัวเลือก AI บน Windows ระหว่าง local และ cloud รวมถึง Foundry Local และ Windows ML:
  https://learn.microsoft.com/windows/ai/cloud-ai#key-decision-factors-for-app-developers
- VS Code AI Toolkit กับ Foundry Local (ใช้ `foundry service status` เพื่อรับ URL endpoint ของ chat):
  https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture#key-components

[นักพัฒนาบน Windows ถัดไป](./windowdeveloper.md)

---

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) แม้ว่าเราจะพยายามให้การแปลมีความถูกต้อง แต่โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางควรถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ ขอแนะนำให้ใช้บริการแปลภาษามืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดที่เกิดจากการใช้การแปลนี้
# ตัวอย่าง Session 6: ใช้โมเดลเป็นเครื่องมือ

ตัวอย่างนี้แสดงการใช้งาน router + tool registry แบบง่าย ๆ ที่เลือกโมเดลตามคำสั่งของผู้ใช้และเรียกใช้งาน endpoint ของ Foundry Local ที่เข้ากันได้กับ OpenAI

## ไฟล์
- `router.py`: registry และ heuristic routing แบบง่าย ๆ; การค้นหา endpoint + ตรวจสอบสถานะ

## การรัน (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
REM Start whatever models you plan to route to
foundry model run phi-4-mini
foundry model run qwen2.5-7b
foundry model run deepseek-r1-7b

python samples\06\router.py "Explain how local-first AI improves privacy in two sentences."
```

## หมายเหตุ
- router ใช้ heuristic แบบคำสำคัญง่าย ๆ เพื่อเลือกเครื่องมือระหว่าง `general`, `reasoning` และ `code` และจะแสดง `/v1/models` เมื่อเริ่มต้น
- ตั้งค่าผ่าน environment variables:
```cmd
set BASE_URL=http://localhost:8000
set API_KEY=
REM Override models per tool
set GENERAL_MODEL=phi-4-mini
set REASONING_MODEL=deepseek-r1-7b
set CODE_MODEL=qwen2.5-7b
REM Or provide a full JSON registry
set TOOL_REGISTRY={"general":{"model":"phi-4-mini"},"reasoning":{"model":"deepseek-r1-7b"},"code":{"model":"qwen2.5-7b"}}
```

## อ้างอิง
- Foundry Local (เรียนรู้เพิ่มเติม): https://learn.microsoft.com/azure/ai-foundry/foundry-local/
- การผสานรวมกับ SDK การอนุมาน: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

---

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) แม้ว่าเราจะพยายามให้การแปลมีความถูกต้องมากที่สุด แต่โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาดั้งเดิมควรถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ ขอแนะนำให้ใช้บริการแปลภาษามนุษย์ที่มีความเชี่ยวชาญ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดที่เกิดจากการใช้การแปลนี้
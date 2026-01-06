<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4d17537bea40917b825c06fd0bba5baf",
  "translation_date": "2026-01-05T14:05:27+00:00",
  "source_file": "WorkshopForAgentic/code/02.Workflow-MultiAgent/03.Application/README.md",
  "language_code": "th"
}
-->
# Podcast Application

แอปพลิเคชันคอนโซลสำหรับสร้างสคริปต์พอดแคสต์โดยใช้เอเย่นต์ AI

## Usage

```bash
python podcast_app.py
```

## Workflow

1. **Welcome** - แอปพลิเคชันทักทายผู้ใช้
2. **Topic Input** - ผู้ใช้ระบุหัวข้อสำหรับพอดแคสต์
3. **Search Agent** - ค้นหาข้อมูลที่เกี่ยวข้อง
4. **Generate Script Agent** - สร้างสคริปต์พอดแคสต์
5. **Review** - ผู้ใช้ตรวจสอบและอนุมัติ/ปฏิเสธสคริปต์
6. **Save** - สคริปต์ที่ได้รับการอนุมัติจะถูกบันทึกใน `podcast.md`

## Requirements

- Python 3.12+
- agent_framework
- All dependencies from 02.WorkflowDevUI

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ข้อจำกัดความรับผิดชอบ**:
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษาอัตโนมัติ [Co-op Translator](https://github.com/Azure/co-op-translator) แม้เราจะพยายามให้มีความถูกต้อง แต่โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความคลาดเคลื่อน เอกสารต้นฉบับในภาษาดั้งเดิมควรถูกพิจารณาเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลสำคัญ แนะนำให้ใช้บริการแปลโดยมืออาชีพเท่านั้น เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดพลาดใด ๆ ที่เกิดขึ้นจากการใช้การแปลนี้
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
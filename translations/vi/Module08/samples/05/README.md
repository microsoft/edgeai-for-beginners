# Phiên 5 Mẫu: Điều phối Đa Tác Nhân

Mẫu này minh họa mô hình điều phối viên + chuyên gia sử dụng điểm cuối tương thích OpenAI của Foundry Local.

## Chạy (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
foundry model run phi-4-mini
python -m samples.05.agents.coordinator
```

## Xác minh
```cmd
curl http://localhost:8000/v1/models
```

## Xử lý sự cố
- Nếu VS Code báo lỗi `import specialists` không được giải quyết trong `coordinator.py`, hãy đảm bảo bạn chạy dưới dạng module và trình thông dịch trỏ đến `Module08/.venv`:
	- Chạy: `python -m samples.05.agents.coordinator`
	- Chọn trình thông dịch: `Module08/.venv/Scripts/python.exe` (Ctrl+Shift+P → Python: Select Interpreter)

## Tài liệu tham khảo
- Foundry Local (Học): https://learn.microsoft.com/azure/ai-foundry/foundry-local/
- Tổng quan về Azure AI Agents: https://learn.microsoft.com/azure/ai-services/agents/overview
- Mẫu gọi hàm (Foundry Local): https://github.com/microsoft/Foundry-Local/tree/main/samples/python/functioncalling

---


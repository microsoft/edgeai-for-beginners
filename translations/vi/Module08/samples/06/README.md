# Phiên 6 Mẫu: Mô hình như Công cụ

Mẫu này triển khai một bộ định tuyến tối giản + đăng ký công cụ, chọn mô hình dựa trên lời nhắc của người dùng và gọi điểm cuối tương thích OpenAI của Foundry Local.

## Tệp
- `router.py`: đăng ký đơn giản và định tuyến theo phương pháp heuristic; khám phá điểm cuối + kiểm tra sức khỏe.

## Chạy (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
REM Start whatever models you plan to route to
foundry model run phi-4-mini
foundry model run qwen2.5-7b
foundry model run deepseek-r1-7b

python samples\06\router.py "Explain how local-first AI improves privacy in two sentences."
```

## Ghi chú
- Bộ định tuyến sử dụng các phương pháp heuristic từ khóa đơn giản để chọn giữa các công cụ `general`, `reasoning`, và `code`, đồng thời in `/v1/models` khi khởi động.
- Cấu hình thông qua các biến môi trường:
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

## Tham khảo
- Foundry Local (Học): https://learn.microsoft.com/azure/ai-foundry/foundry-local/
- Tích hợp với SDK suy luận: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

---

**Tuyên bố miễn trừ trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn thông tin chính thức. Đối với các thông tin quan trọng, khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm cho bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.
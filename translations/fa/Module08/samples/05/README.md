# نمونه جلسه ۵: هماهنگی چند عامل

این نمونه الگوی هماهنگ‌کننده + متخصصان را با استفاده از نقطه پایانی سازگار با OpenAI در Foundry Local نشان می‌دهد.

## اجرا (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
foundry model run phi-4-mini
python -m samples.05.agents.coordinator
```

## اعتبارسنجی
```cmd
curl http://localhost:8000/v1/models
```

## رفع اشکال
- اگر VS Code خطای `import specialists` را در فایل `coordinator.py` نشان داد، مطمئن شوید که به‌عنوان یک ماژول اجرا می‌کنید و مفسر به مسیر `Module08/.venv` اشاره می‌کند:
	- اجرا کنید: `python -m samples.05.agents.coordinator`
	- مفسر را انتخاب کنید: `Module08/.venv/Scripts/python.exe` (Ctrl+Shift+P → Python: Select Interpreter)

## منابع
- Foundry Local (آموزش): https://learn.microsoft.com/azure/ai-foundry/foundry-local/
- نمای کلی عوامل Azure AI: https://learn.microsoft.com/azure/ai-services/agents/overview
- نمونه فراخوانی تابع (Foundry Local): https://github.com/microsoft/Foundry-Local/tree/main/samples/python/functioncalling

---


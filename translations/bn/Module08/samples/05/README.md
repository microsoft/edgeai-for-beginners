# সেশন ৫ নমুনা: মাল্টি-এজেন্ট অর্কেস্ট্রেশন

এই নমুনাটি Foundry Local-এর OpenAI-সামঞ্জস্যপূর্ণ এন্ডপয়েন্ট ব্যবহার করে কোঅর্ডিনেটর + বিশেষজ্ঞদের প্যাটার্ন প্রদর্শন করে।

## চালান (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
foundry model run phi-4-mini
python -m samples.05.agents.coordinator
```

## যাচাই করুন
```cmd
curl http://localhost:8000/v1/models
```

## সমস্যা সমাধান
- যদি VS Code `coordinator.py`-এ `import specialists`-কে অমীমাংসিত হিসেবে চিহ্নিত করে, নিশ্চিত করুন যে আপনি এটি একটি মডিউল হিসেবে চালাচ্ছেন এবং ইন্টারপ্রেটারটি `Module08/.venv`-এ নির্দেশ করছে:
	- চালান: `python -m samples.05.agents.coordinator`
	- ইন্টারপ্রেটার নির্বাচন করুন: `Module08/.venv/Scripts/python.exe` (Ctrl+Shift+P → Python: Select Interpreter)

## রেফারেন্স
- Foundry Local (শিখুন): https://learn.microsoft.com/azure/ai-foundry/foundry-local/
- Azure AI Agents ওভারভিউ: https://learn.microsoft.com/azure/ai-services/agents/overview
- ফাংশন কলিং নমুনা (Foundry Local): https://github.com/microsoft/Foundry-Local/tree/main/samples/python/functioncalling

---


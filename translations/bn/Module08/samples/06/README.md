# সেশন ৬ উদাহরণ: টুল হিসেবে মডেল

এই উদাহরণটি একটি ন্যূনতম রাউটার + টুল রেজিস্ট্রি বাস্তবায়ন করে যা ব্যবহারকারীর প্রম্পটের উপর ভিত্তি করে একটি মডেল নির্বাচন করে এবং Foundry Local-এর OpenAI-সামঞ্জস্যপূর্ণ এন্ডপয়েন্টকে কল করে।

## ফাইলসমূহ
- `router.py`: সহজ রেজিস্ট্রি এবং হিউরিস্টিক রাউটিং; এন্ডপয়েন্ট আবিষ্কার + স্বাস্থ্য পরীক্ষা।

## চালান (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
REM Start whatever models you plan to route to
foundry model run phi-4-mini
foundry model run qwen2.5-7b
foundry model run deepseek-r1-7b

python samples\06\router.py "Explain how local-first AI improves privacy in two sentences."
```

## নোটসমূহ
- রাউটারটি `general`, `reasoning`, এবং `code` টুলগুলোর মধ্যে নির্বাচন করতে সহজ কীওয়ার্ড হিউরিস্টিক ব্যবহার করে এবং শুরুতে `/v1/models` প্রিন্ট করে।
- পরিবেশ ভেরিয়েবলগুলোর মাধ্যমে কনফিগার করুন:
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

## রেফারেন্সসমূহ
- Foundry Local (শিখুন): https://learn.microsoft.com/azure/ai-foundry/foundry-local/
- ইনফারেন্স SDK-এর সাথে ইন্টিগ্রেট করুন: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

---

**অস্বীকৃতি**:  
এই নথিটি AI অনুবাদ পরিষেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনুবাদ করা হয়েছে। আমরা যথাসাধ্য সঠিকতার জন্য চেষ্টা করি, তবে অনুগ্রহ করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। এর মূল ভাষায় থাকা নথিটিকে প্রামাণিক উৎস হিসেবে বিবেচনা করা উচিত। গুরুত্বপূর্ণ তথ্যের ক্ষেত্রে, পেশাদার মানব অনুবাদ সুপারিশ করা হয়। এই অনুবাদ ব্যবহারের ফলে কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যা হলে আমরা দায়বদ্ধ থাকব না।
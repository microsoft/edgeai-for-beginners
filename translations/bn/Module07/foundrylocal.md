# উইন্ডোজ এবং ম্যাক-এ Foundry Local

এই গাইডটি আপনাকে উইন্ডোজ এবং ম্যাক-এ Microsoft Foundry Local ইনস্টল, চালানো এবং ইন্টিগ্রেট করতে সাহায্য করবে। সমস্ত ধাপ এবং কমান্ড Microsoft Learn ডকুমেন্টেশনের সাথে যাচাই করা হয়েছে।

- শুরু করুন: https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started
- আর্কিটেকচার: https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture
- CLI রেফারেন্স: https://learn.microsoft.com/azure/ai-foundry/foundry-local/reference/reference-cli
- SDK ইন্টিগ্রেশন: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks
- HF মডেল কম্পাইল (BYOM): https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models
- উইন্ডোজ AI: লোকাল বনাম ক্লাউড: https://learn.microsoft.com/windows/ai/cloud-ai#key-decision-factors-for-app-developers

## ১) উইন্ডোজে ইনস্টল / আপগ্রেড

- ইনস্টল:
```cmd
winget install Microsoft.FoundryLocal
```
- আপগ্রেড:
```cmd
winget upgrade --id Microsoft.FoundryLocal
```
- ভার্সন চেক:
```cmd
foundry --version
```
     
**ম্যাক-এ ইনস্টল**

**MacOS**: 
একটি টার্মিনাল খুলুন এবং নিচের কমান্ডটি চালান:
```bash
   brew tap microsoft/foundrylocal
   brew install foundrylocal
```

## ২) CLI বেসিকস (তিনটি ক্যাটাগরি)

- মডেল:
```cmd
foundry model --help
foundry model list
foundry model run gpt-oss-20b
```
- সার্ভিস:
```cmd
foundry service --help
foundry service status
foundry service ps
```
- ক্যাশ:
```cmd
foundry cache --help
foundry cache list
```

নোট:
- সার্ভিসটি একটি OpenAI-সামঞ্জস্যপূর্ণ REST API উন্মুক্ত করে। এন্ডপয়েন্ট পোর্টটি ডাইনামিকভাবে বরাদ্দ করা হয়; এটি খুঁজে পেতে `foundry service status` ব্যবহার করুন।
- সুবিধার জন্য SDK ব্যবহার করুন; এটি যেখানে সমর্থিত, সেখানে এন্ডপয়েন্ট আবিষ্কার স্বয়ংক্রিয়ভাবে পরিচালনা করে।

## ৩) লোকাল এন্ডপয়েন্ট আবিষ্কার (ডাইনামিক পোর্ট)

Foundry Local প্রতিবার সার্ভিস শুরু হলে একটি ডাইনামিক পোর্ট বরাদ্দ করে:
```cmd
foundry service status
```
প্রতিবেদনকৃত `http://localhost:<PORT>` কে OpenAI-সামঞ্জস্যপূর্ণ পাথ (যেমন, `/v1/chat/completions`) সহ আপনার `base_url` হিসাবে ব্যবহার করুন।

## ৪) OpenAI পাইথন SDK এর মাধ্যমে দ্রুত পরীক্ষা

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
রেফারেন্স:
- SDK ইন্টিগ্রেশন: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

## ৫) আপনার নিজস্ব মডেল আনুন (Olive দিয়ে কম্পাইল করুন)

যদি ক্যাটালগে আপনার প্রয়োজনীয় মডেল না থাকে, তাহলে Olive ব্যবহার করে এটি ONNX-এ কম্পাইল করুন Foundry Local এর জন্য।

উচ্চ-স্তরের ফ্লো (ধাপগুলির জন্য ডকুমেন্টেশন দেখুন):
```cmd
foundry cache cd models
foundry cache list
foundry model run llama-3.2 --verbose
```
ডকস:
- BYOM কম্পাইল: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models

## ৬) সমস্যা সমাধান

- সার্ভিস স্ট্যাটাস এবং লগ চেক করুন:
```cmd
foundry service status
foundry service diag
```
- ক্যাশ পরিষ্কার বা সরান:
```cmd
foundry cache list
foundry cache remove <model>
foundry cache cd <path>
```
- সর্বশেষ প্রিভিউতে আপডেট করুন:
```cmd
winget upgrade --id Microsoft.FoundryLocal
```

## ৭) সংশ্লিষ্ট উইন্ডোজ ডেভেলপার অভিজ্ঞতা

- উইন্ডোজ লোকাল বনাম ক্লাউড AI পছন্দসমূহ, যার মধ্যে Foundry Local এবং Windows ML অন্তর্ভুক্ত:
  https://learn.microsoft.com/windows/ai/cloud-ai#key-decision-factors-for-app-developers
- Foundry Local সহ VS Code AI টুলকিট (চ্যাট এন্ডপয়েন্ট URL পেতে `foundry service status` ব্যবহার করুন):
  https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture#key-components

[পরবর্তী উইন্ডোজ ডেভেলপার](./windowdeveloper.md)

---

**অস্বীকৃতি**:  
এই নথিটি AI অনুবাদ পরিষেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনুবাদ করা হয়েছে। আমরা যথাসাধ্য সঠিকতার জন্য চেষ্টা করি, তবে অনুগ্রহ করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল ভাষায় থাকা নথিটিকে প্রামাণিক উৎস হিসেবে বিবেচনা করা উচিত। গুরুত্বপূর্ণ তথ্যের জন্য, পেশাদার মানব অনুবাদ সুপারিশ করা হয়। এই অনুবাদ ব্যবহারের ফলে কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যা হলে আমরা দায়বদ্ধ থাকব না।
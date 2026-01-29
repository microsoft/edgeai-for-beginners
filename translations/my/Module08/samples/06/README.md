# အခန်း ၆ နမူနာ: ကိရိယာများအဖြစ် မော်ဒယ်များ

ဒီနမူနာမှာ အသုံးပြုသူရဲ့ prompt အပေါ်မူတည်ပြီး မော်ဒယ်ကို ရွေးချယ်ပြီး Foundry Local ရဲ့ OpenAI-compatible endpoint ကို ခေါ်ယူတဲ့ အနည်းဆုံး router + tool registry ကို အကောင်အထည်ဖော်ထားပါတယ်။

## ဖိုင်များ
- `router.py`: ရိုးရှင်းတဲ့ registry နဲ့ heuristic routing; endpoint ရှာဖွေမှု + ကျန်းမာရေးစစ်ဆေးမှု။

## အလုပ်လုပ်ရန် (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
REM Start whatever models you plan to route to
foundry model run phi-4-mini
foundry model run qwen2.5-7b
foundry model run deepseek-r1-7b

python samples\06\router.py "Explain how local-first AI improves privacy in two sentences."
```

## မှတ်ချက်များ
- router က `general`, `reasoning`, နဲ့ `code` tools တွေကို ရွေးချယ်ဖို့ ရိုးရှင်းတဲ့ keyword heuristics ကို အသုံးပြုပြီး စတင်ချိန်မှာ `/v1/models` ကို print လုပ်ပါတယ်။
- Environment variables တွေကို အသုံးပြုပြီး အဆင်ပြေစွာ ပြင်ဆင်နိုင်ပါတယ်:
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

## ရင်းမြစ်များ
- Foundry Local (သင်ယူရန်): https://learn.microsoft.com/azure/ai-foundry/foundry-local/
- Inference SDKs တွေနဲ့ ပေါင်းစည်းရန်: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

---

**အကြောင်းကြားချက်**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှုအတွက် ကြိုးစားနေသော်လည်း အလိုအလျောက် ဘာသာပြန်မှုများတွင် အမှားများ သို့မဟုတ် မမှန်ကန်မှုများ ပါဝင်နိုင်သည်ကို သတိပြုပါ။ မူရင်းဘာသာစကားဖြင့် ရေးသားထားသော စာရွက်စာတမ်းကို အာဏာရှိသော ရင်းမြစ်အဖြစ် သတ်မှတ်သင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူက ဘာသာပြန်မှုကို အသုံးပြုရန် အကြံပြုပါသည်။ ဤဘာသာပြန်မှုကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော အလွဲအမှားများ သို့မဟုတ် အနားယူမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။
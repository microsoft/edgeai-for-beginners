<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4d17537bea40917b825c06fd0bba5baf",
  "translation_date": "2026-01-05T14:10:17+00:00",
  "source_file": "WorkshopForAgentic/code/02.Workflow-MultiAgent/03.Application/README.md",
  "language_code": "my"
}
-->
# Podcast Application

AI ကို အကျုံးပြု၍ podcast script များကို ဖန်တီးပေးသော console application ဖြစ်သည်။

## Usage

```bash
python podcast_app.py
```

## Workflow

1. **Welcome** - အသုံးပြုသူအား application မှ ကြိုဆိုသည်
2. **Topic Input** - အသုံးပြုသူသည် podcast အတွက် ခေါင်းစဉ် တစ်ခု ပေးသည်
3. **Search Agent** - သက်ဆိုင်သော အချက်အလက်များ ရှာဖွေသည်
4. **Generate Script Agent** - podcast script တစ်ခု ဖန်တီးသည်
5. **Review** - အသုံးပြုသူ script ကို ပြန်လည်ဆန်းစစ်၍ အတည်ပြု/ငြင်းပယ်သည်
6. **Save** - အတည်ပြုထားသော script ကို `podcast.md` တွင် သိမ်းဆည်းသည်

## Requirements

- Python 3.12+
- agent_framework
- 02.WorkflowDevUI မှ အားလုံးသော dependencies များ

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**သတိပြုချက်**  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှုဖြစ်သော [Co-op Translator](https://github.com/Azure/co-op-translator) ဖြင့် ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးစားပေမယ့်၊ မော်တော်မောင်းဘာသာပြန်မှုများတွင် မှားယွင်းချက်များ သို့မဟုတ် မမှန်ကန်မှုများ ဖြစ်ပေါ်နိုင်ကြောင်း သိရှိထားပေးပါ။ မူလစာရွက်စာတမ်းကို သူ၏ မူလဘာသာဖြင့် တိကျစွာအာရုံစိုက်မှုရှိသော အရင်းအမြစ်အဖြစ် ယူဆသင့်ပါသည်။ အရေးကြီးသောအချက်အလက်များအတွက် ပရော်ဖက်ရှင်နယ် လူ့ဘာသာပြန်ကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက် အသုံးပြုမှုကြောင့် ဖြစ်ပေါ်လာနိုင်သည့် မှားယွင်းသဘောထားများ သို့မဟုတ် မှားသုံးနားလည်မှုများအတွက် ကျွန်ုပ်တို့ တာဝန်မပေးနိုင်ပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
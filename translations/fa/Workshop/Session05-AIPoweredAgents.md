<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6588aabccabec8ef9b85eb92f3e7143d",
  "translation_date": "2025-10-28T20:23:52+00:00",
  "source_file": "Workshop/Session05-AIPoweredAgents.md",
  "language_code": "fa"
}
-->
# جلسه ۵: ساخت سریع عوامل هوش مصنوعی با Foundry Local

## خلاصه

طراحی و هماهنگی عوامل هوش مصنوعی چندنقشی با استفاده از محیط اجرایی کم‌تاخیر و حفظ حریم خصوصی Foundry Local. در این جلسه نقش‌های عوامل، استراتژی‌های حافظه، الگوهای فراخوانی ابزار و نمودارهای اجرایی را تعریف خواهید کرد. همچنین الگوهای پایه‌ای معرفی می‌شوند که می‌توانید با Chainlit یا LangGraph گسترش دهید. پروژه شروع‌کننده معماری نمونه عوامل موجود را گسترش می‌دهد تا حافظه پایدار و قلاب‌های ارزیابی اضافه کند.

## اهداف یادگیری

- **تعریف نقش‌ها**: پیام‌های سیستمی و مرزهای قابلیت‌ها
- **پیاده‌سازی حافظه**: کوتاه‌مدت (مکالمه)، بلندمدت (برداری/فایل)، یادداشت‌های موقت
- **ساختاردهی جریان کار**: مراحل عوامل به صورت ترتیبی، شاخه‌ای و موازی
- **ادغام ابزارها**: الگوی سبک فراخوانی ابزارهای تابع
- **ارزیابی**: ردگیری پایه + امتیازدهی نتایج بر اساس معیارها

## پیش‌نیازها

- تکمیل جلسات ۱ تا ۴
- پایتون با `foundry-local-sdk`، `openai`، و اختیاری `chainlit`
- مدل‌های محلی در حال اجرا (حداقل `phi-4-mini`)

### قطعه کد محیط چندپلتفرمی

ویندوز:
```powershell
py -m venv .venv
 .\.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install foundry-local-sdk openai
```

مک‌او‌اس:
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install foundry-local-sdk openai
```

اگر عوامل را از مک‌او‌اس در برابر سرویس میزبان ویندوز از راه دور اجرا می‌کنید:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```


## جریان دمو (۳۰ دقیقه)

### ۱. تعریف نقش‌های عوامل و حافظه (۷ دقیقه)

ایجاد فایل `samples/05-agents/agents_core.py`:

```python
#!/usr/bin/env python3
"""Minimal multi-agent scaffolding using Foundry Local (OpenAI-compatible)."""
from openai import OpenAI
from dataclasses import dataclass, field
from typing import List, Dict, Any, Callable
import time, json

client = OpenAI(base_url="http://localhost:5273/v1", api_key="not-needed")

@dataclass
class AgentMessage:
    role: str
    content: str
    meta: Dict[str, Any] = field(default_factory=dict)

@dataclass
class Agent:
    name: str
    system_prompt: str
    tools: Dict[str, Callable] = field(default_factory=dict)
    memory: List[AgentMessage] = field(default_factory=list)

    def remember(self, role: str, content: str, **meta):
        self.memory.append(AgentMessage(role=role, content=content, meta=meta))

    def context(self, window:int=8):
        recent = self.memory[-window:]
        msgs = [ {"role": "system", "content": self.system_prompt}]
        msgs += [ {"role": m.role, "content": m.content} for m in recent ]
        return msgs

    def act(self, user_input: str, model: str = "phi-4-mini", temperature: float=0.4):
        self.remember("user", user_input)
        resp = client.chat.completions.create(
            model=model,
            messages=self.context() + [{"role": "user", "content": user_input}],
            temperature=temperature,
            max_tokens=400
        )
        answer = resp.choices[0].message.content
        self.remember("assistant", answer, model=model)
        return answer

researcher = Agent(
    name="Researcher",
    system_prompt="You gather factual, structured insights concisely."
)
writer = Agent(
    name="Writer",
    system_prompt="You rewrite content for clarity and engagement while preserving facts."
)

def demo():
    q = "Explain why edge inference matters for privacy and latency."
    r = researcher.act(q)
    print("Researcher ->", r[:200], "...\n")
    w = writer.act(f"Rewrite more user-friendly: {r}")
    print("Writer ->", w[:200], "...")

if __name__ == "__main__":
    demo()
```


### ۲. الگوی ساختاردهی CLI (۳ دقیقه)

```powershell
python samples/05-agents/agents_core.py
```


### ۳. افزودن فراخوانی ابزار (۷ دقیقه)

گسترش با فایل `samples/05-agents/tools.py`:

```python
from datetime import datetime
import math, json

def tool_time(_:str)->str:
    return f"Current UTC time: {datetime.utcnow().isoformat()}"

def tool_estimate_tokens(text:str)->str:
    approx = len(text.split()) * 1.35
    return f"Estimated tokens ~ {int(approx)}"

TOOLS = {
    "get_time": tool_time,
    "estimate_tokens": tool_estimate_tokens
}
```

تغییر فایل `agents_core.py` برای اجازه دادن به نحو ساده ابزار: کاربر می‌نویسد `#tool:get_time` و عامل خروجی ابزار را قبل از تولید به زمینه اضافه می‌کند.

### ۴. جریان کار هماهنگ‌شده (۶ دقیقه)

ایجاد فایل `samples/05-agents/orchestrator.py`:

```python
from agents_core import researcher, writer, Agent
from tools import TOOLS
from openai import OpenAI

client = OpenAI(base_url="http://localhost:5273/v1", api_key="not-needed")

def inject_tools(agent: Agent, user_input: str) -> str:
    if user_input.startswith('#tool:'):
        name = user_input.split(':',1)[1].strip()
        if name in TOOLS:
            out = TOOLS[name](../../../Workshop/"")
            agent.remember("tool", out, tool=name)
            return f"Tool[{name}] => {out}"
    return None

def pipeline(question: str):
    tool_note = inject_tools(researcher, '#tool:get_time')
    r = researcher.act(question)
    w = writer.act(f"Improve readability:\n{r}\nAdd a friendly summary line.")
    return {"raw": r, "refined": w, "tool": tool_note}

if __name__ == '__main__':
    result = pipeline("List three concrete benefits of local SLM inference for regulated industries.")
    for k,v in result.items():
        print(f"== {k.upper()} ==\n{v}\n")
```


### ۵. پروژه شروع‌کننده: گسترش `05-agent-architecture` (۷ دقیقه)

افزودن:
1. لایه حافظه پایدار (مثلاً افزودن خطوط JSON از مکالمات)
2. معیار ارزیابی ساده: جایگزین‌های واقعیت‌گرایی / وضوح / سبک
3. رابط کاربری اختیاری Chainlit (دو تب: مکالمه و ردگیری‌ها)
4. ماشین حالت سبک LangGraph اختیاری (در صورت افزودن وابستگی) برای تصمیمات شاخه‌ای

## چک‌لیست اعتبارسنجی

```powershell
foundry model run phi-4-mini
python samples/05-agents/orchestrator.py
```

انتظار خروجی خط لوله ساختاریافته با یادداشت تزریق ابزار.

## مرور استراتژی‌های حافظه

| لایه | هدف | مثال |
|------|------|------|
| کوتاه‌مدت | تداوم مکالمه | آخرین N پیام |
| اپیزودیک | یادآوری جلسه | JSON برای هر جلسه |
| معنایی | بازیابی بلندمدت | ذخیره برداری خلاصه‌ها |
| یادداشت موقت | مراحل استدلال | زنجیره تفکر داخلی (خصوصی) |

## قلاب‌های ارزیابی (مفهومی)

```python
evaluation = {
  "factuality": None,  # manual or heuristic
  "clarity": None,
  "style": None,
  "latency_sec": generation_time,
  "model": model_used
}
```


## رفع اشکال

| مشکل | علت | راه‌حل |
|------|-----|-------|
| پاسخ‌های تکراری | پنجره زمینه خیلی بزرگ/کوچک | تنظیم پارامتر پنجره حافظه |
| ابزار فراخوانی نشده | نحو اشتباه | استفاده از فرمت `#tool:tool_name` |
| هماهنگی کند | مدل‌های سرد متعدد | اجرای اولیه درخواست‌های گرم‌کننده |

## منابع

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- LangGraph (مفهوم اختیاری): https://github.com/langchain-ai/langgraph
- Chainlit: https://docs.chainlit.io

---

**مدت زمان جلسه**: ۳۰ دقیقه  
**سطح دشواری**: پیشرفته

## سناریوی نمونه و نقشه‌برداری کارگاه

| اسکریپت کارگاه | سناریو | هدف | مثال درخواست |
|----------------|--------|-----|--------------|
| `samples/session05/agents_orchestrator.py` / `notebooks/session05_agents_orchestrator.ipynb` | ربات تحقیق دانش که خلاصه‌های مناسب مدیران تولید می‌کند | خط لوله دو عاملی (تحقیق → ویرایش نهایی) با مدل‌های اختیاری متفاوت | توضیح دهید چرا استنتاج لبه برای رعایت قوانین مهم است. |
| (گسترش‌یافته) مفهوم `tools.py` | افزودن ابزارهای زمان و تخمین توکن | نمایش الگوی سبک فراخوانی ابزار | #tool:get_time |

### روایت سناریو
تیم مستندسازی رعایت قوانین به خلاصه‌های داخلی سریع نیاز دارد که از دانش محلی استخراج شده‌اند بدون اینکه پیش‌نویس‌ها به سرویس‌های ابری ارسال شوند. یک عامل محقق گلوله‌های واقعی مختصر جمع‌آوری می‌کند؛ یک عامل ویرایشگر برای وضوح اجرایی بازنویسی می‌کند. می‌توان به مدل‌های متفاوت برای بهینه‌سازی تأخیر (مدل سریع) در مقابل پالایش سبک (مدل بزرگ‌تر فقط در صورت نیاز) اختصاص داد.

### محیط چندمدلی نمونه
```powershell
cd Workshop/samples
set AGENT_MODEL_PRIMARY=phi-4-mini
set AGENT_MODEL_EDITOR=gpt-oss-20b
python -m session05.agents_orchestrator
```


### ساختار ردگیری (اختیاری)
```json
{
    "step": 1,
    "agent": "Researcher",
    "latency_ms": 412.3,
    "tokens_in": 22,
    "tokens_out": 168,
    "model": "phi-4-mini"
}
```

هر مرحله را به یک فایل JSONL برای امتیازدهی معیار بعدی ذخیره کنید.

### بهبودهای اختیاری

| موضوع | بهبود | مزیت | طرح پیاده‌سازی |
|-------|-------|------|----------------|
| نقش‌های چندمدلی | مدل‌های متفاوت برای هر عامل (`AGENT_MODEL_PRIMARY`, `AGENT_MODEL_EDITOR`) | تخصص و سرعت | انتخاب متغیرهای محیطی مستعار، فراخوانی `chat_once` با مستعار نقش |
| ردگیری ساختاریافته | ردگیری JSON از هر عمل (ابزار، ورودی، تأخیر، توکن‌ها) | اشکال‌زدایی و ارزیابی | افزودن دیکشنری به لیست؛ نوشتن `.jsonl` در پایان |
| پایداری حافظه | زمینه مکالمه قابل بارگذاری | تداوم جلسه | ذخیره `Agent.memory` به `sessions/<ts>.json` |
| ثبت ابزار | کشف ابزار پویا | قابلیت گسترش | نگهداری دیکشنری `TOOLS` و بررسی نام‌ها/توضیحات |
| تلاش مجدد و تأخیر | زنجیره‌های طولانی مقاوم | کاهش خطاهای گذرا | پوشش `act` با try/except + تأخیر نمایی |
| امتیازدهی معیار | برچسب‌های کیفی خودکار | پیگیری بهبودها | درخواست ثانویه از مدل: "وضوح را از ۱ تا ۵ امتیاز دهید" |
| حافظه برداری | یادآوری معنایی | زمینه بلندمدت غنی | جاسازی خلاصه‌ها، بازیابی برترین‌ها به پیام سیستمی |
| پاسخ‌های جریان‌دار | پاسخ سریع‌تر محسوس | بهبود تجربه کاربری | استفاده از جریان زمانی که در دسترس است و تخلیه توکن‌های جزئی |
| آزمون‌های قطعی | کنترل رگرسیون | CI پایدار | اجرا با `temperature=0`، بذرهای درخواست ثابت |
| شاخه‌بندی موازی | اکتشاف سریع‌تر | توان عملیاتی | استفاده از `concurrent.futures` برای مراحل مستقل عوامل |

#### مثال ثبت ردگیری

```python
trace.append({
    "agent": agent.name,
    "input": prompt,
    "output_tokens": getattr(usage,'completion_tokens',None),
    "latency_ms": round((end-start)*1000,2),
    "tools_used": list(tool_calls)
})
```


#### درخواست ارزیابی ساده

```python
score_prompt = f"Rate clarity (1-5) ONLY as a number for this answer:\n{answer}"
rating, _ = chat_once(PRIMARY_ALIAS, messages=[{"role":"user","content":score_prompt}], max_tokens=4, temperature=0)
```

جفت‌های (`answer`, `rating`) را ذخیره کنید تا نمودار کیفیت تاریخی ایجاد کنید.

---

**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما تلاش می‌کنیم دقت را حفظ کنیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا نادرستی‌ها باشند. سند اصلی به زبان اصلی آن باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما مسئولیتی در قبال سوء تفاهم‌ها یا تفسیرهای نادرست ناشی از استفاده از این ترجمه نداریم.
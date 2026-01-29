# מפגש 4: חקר מודלים מתקדמים – LLMs, SLMs והסקה מקומית

## תקציר

השוואה בין מודלים לשוניים גדולים (LLMs) לבין מודלים לשוניים קטנים (SLMs) בתרחישי הסקה מקומית מול ענן. למדו דפוסי פריסה תוך ניצול האצת ONNX Runtime, ביצוע WebGPU וחוויות RAG היברידיות. כולל הדגמת Chainlit RAG עם מודל מקומי ובחירה אופציונלית לחקור את OpenWebUI. תתאימו התחלה להסקת WebGPU ותעריכו את היכולות והאיזון בין עלות/ביצועים של Phi מול GPT-OSS-20B.

## מטרות למידה

- **השוואה** בין SLM ל-LLM בצירים של זמן תגובה, זיכרון ואיכות
- **פריסה** של מודלים עם ONNXRuntime ו-(כאשר נתמך) WebGPU
- **הרצה** של הסקה מבוססת דפדפן (הדגמה אינטראקטיבית השומרת על פרטיות)
- **שילוב** של צינור Chainlit RAG עם SLM מקומי
- **הערכה** באמצעות מדדי איכות + עלות קלים

## דרישות מוקדמות

- סיום מפגשים 1–3
- `chainlit` מותקן (כבר ב-`requirements.txt` עבור Module08)
- דפדפן תומך WebGPU (Edge / Chrome גרסה אחרונה על Windows 11)
- Foundry Local פועל (`foundry service status`)

### הערות חוצות פלטפורמות

Windows נשארת סביבת היעד העיקרית. למפתחים ב-macOS שממתינים לבינארים מקוריים:
1. הריצו את Foundry Local ב-VM של Windows 11 (Parallels / UTM) או תחנת עבודה מרוחקת של Windows.
2. חשפו את השירות (פורט ברירת מחדל 5273) והגדירו ב-macOS:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```
3. השתמשו באותם צעדים של סביבת Python וירטואלית כמו במפגשים הקודמים.

התקנת Chainlit (שתי הפלטפורמות):
```bash
pip install chainlit
```

## זרימת הדגמה (30 דקות)

### 1. השוואת Phi (SLM) מול GPT-OSS-20B (LLM) (6 דקות)

```powershell
foundry model run phi-4-mini
foundry model run gpt-oss-20b

# Quick capability probes (one-shot non-interactive)
foundry model run phi-4-mini   --prompt "Summarize retrieval augmented generation in 2 sentences."
foundry model run gpt-oss-20b --prompt "Summarize retrieval augmented generation in 2 sentences."

# Basic token / latency test (repeat a few times for intuition)
foundry model run phi-4-mini   --prompt "List 5 creative IoT edge AI ideas."
foundry model run gpt-oss-20b --prompt "List 5 creative IoT edge AI ideas."
```

עקבו: עומק תגובה, דיוק עובדתי, עושר סגנוני, זמן תגובה.

שימו לב לשינויים בתפוקה לאחר הפעלת GPU מול CPU בלבד.

### 3. הסקת WebGPU בדפדפן (6 דקות)

התאימו התחלה `04-webgpu-inference` (צרו `samples/04-cutting-edge/webgpu_demo.html`):

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>Foundry Local WebGPU Demo</title>
  <style>body{font-family:system-ui;margin:2rem;max-width:820px;} textarea{width:100%;height:120px;} pre{background:#111;color:#eee;padding:1rem;} .resp{white-space:pre-wrap;margin-top:1rem;border:1px solid #444;padding:1rem;border-radius:6px;}</style>
</head>
<body>
  <h1>WebGPU Inference (Experimental)</h1>
  <p>Demonstration placeholder for a WebGPU-backed transformer (concept). Replace with actual JS runtime once exposed by Foundry Local or associated runtime libs.</p>
  <textarea id="prompt" placeholder="Enter your prompt..."></textarea>
  <button id="run">Generate</button>
  <div id="out" class="resp"></div>
  <script>
    document.getElementById('run').onclick = async () => {
      const p = document.getElementById('prompt').value.trim();
      if(!p) return;
      document.getElementById('out').textContent = 'Running (simulated)...';
      // Placeholder: in a real implementation you'd call into a WASM/WebGPU pipeline or local gateway endpoint.
      const resp = await fetch('http://localhost:5273/v1/chat/completions', {
        method: 'POST', headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          model: 'phi-4-mini',
          messages: [ { role: 'user', content: p } ],
          max_tokens: 200, temperature: 0.5
        })
      }).then(r=>r.json()).catch(e=>({error:e.toString()}));
      if(resp.error){
        document.getElementById('out').textContent = 'Error: '+resp.error;
      } else {
        document.getElementById('out').textContent = resp.choices?.[0]?.message?.content || JSON.stringify(resp,null,2);
      }
    };
  </script>
</body>
</html>
```

פתחו את הקובץ בדפדפן; שימו לב לסבב מקומי בעל זמן תגובה נמוך.

### 4. אפליקציית צ'אט Chainlit RAG (7 דקות)

`samples/04-cutting-edge/chainlit_app.py` מינימלי:

```python
#!/usr/bin/env python3
"""Chainlit RAG demo using Foundry Local SLM as backend."""
import chainlit as cl
from openai import OpenAI

DOCS = [
  "Foundry Local enables local model execution with OpenAI-compatible APIs.",
  "RAG combines retrieval and generation for grounded answers.",
  "SLMs provide efficiency advantages on constrained hardware."  
]

client = OpenAI(base_url="http://localhost:5273/v1", api_key="not-needed")

def build_context(query: str):
    # Naive lexical scoring
    scored = sorted(DOCS, key=lambda d: sum(w in d.lower() for w in query.lower().split()), reverse=True)
    return "\n".join(scored[:2])

@cl.on_message
async def main(message: cl.Message):
    ctx = build_context(message.content)
    resp = client.chat.completions.create(
        model="phi-4-mini",
        messages=[
            {"role": "system", "content": "Answer using ONLY the provided context. If insufficient, say so."},
            {"role": "user", "content": f"Context:\n{ctx}\n\nQuestion: {message.content}"}
        ],
        max_tokens=300,
        temperature=0.3
    )
    await cl.Message(content=resp.choices[0].message.content).send()
```

הריצו:

```powershell
chainlit run samples/04-cutting-edge/chainlit_app.py -w
```

### 5. פרויקט התחלה: התאמת `04-webgpu-inference` (6 דקות)

Deliverables:
- החליפו את לוגיקת הבאת הנתונים עם זרימת טוקנים (השתמשו ב-`stream=True` כאשר מופעל)
- הוסיפו גרף זמן תגובה (בצד הלקוח) עבור Phi מול GPT-OSS-20B
- הטמיעו הקשר RAG באופן ישיר (שדה טקסט למסמכי עזר)

## מדדי הערכה

| קטגוריה | Phi-4-mini | GPT-OSS-20B | תצפית |
|---------|------------|-------------|--------|
| זמן תגובה (קר) | מהיר | איטי יותר | SLM מתחמם במהירות |
| זיכרון | נמוך | גבוה | היתכנות במכשיר |
| התאמה להקשר | טובה | חזקה | מודל גדול עשוי להיות יותר מפורט |
| עלות (מקומית) | מינימלית | גבוהה (משאבים) | איזון אנרגיה/זמן |
| שימוש מיטבי | אפליקציות קצה | ניתוח מעמיק | אפשרי צינור היברידי |

## אימות סביבה

```powershell
# List catalog (no --running flag; loaded models are those you have previously run)
foundry model list

# For runtime metrics use the Python benchmark script (Session 3) and OS tools (Task Manager / nvidia-smi) instead of 'model stats'
# Example:
#   cd Workshop/samples
#   set BENCH_MODELS=phi-4-mini,gpt-oss-20b
#   python -m session03.benchmark_oss_models
```

## פתרון בעיות

| סימפטום | סיבה | פעולה |
|---------|-------|-------|
| כשל בהבאת דף אינטרנט | CORS או שירות לא פעיל | השתמשו ב-`curl` לאימות נקודת הקצה; הפעילו פרוקסי CORS אם נדרש |
| Chainlit ריק | סביבה לא פעילה | הפעילו venv והתקינו מחדש תלות |
| זמן תגובה גבוה | מודל רק נטען | חממו עם רצף הנחיה קטן |

## מקורות

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- Chainlit Docs: https://docs.chainlit.io
- RAG Evaluation (Ragas): https://docs.ragas.io

---

**משך המפגש**: 30 דקות  
**רמת קושי**: מתקדם

## תרחיש לדוגמה ומיפוי סדנה

| פריטי סדנה | תרחיש | מטרה | מקור נתונים / הנחיה |
|------------|--------|-------|---------------------|
| `samples/session04/model_compare.py` / `notebooks/session04_model_compare.ipynb` | צוות ארכיטקטורה מעריך SLM מול LLM עבור מחולל סיכומים למנהלים | כימות זמן תגובה + שימוש בטוקנים | משתנה סביבה `COMPARE_PROMPT` יחיד |
| `chainlit_app.py` (הדגמת RAG) | אבטיפוס עוזר ידע פנימי | הנחת תשובות קצרות עם שליפה לקסיקלית מינימלית | רשימת `DOCS` מוטמעת בקובץ |
| `webgpu_demo.html` | תצוגה מקדימה של הסקה בדפדפן על המכשיר | הצגת סבב מקומי בעל זמן תגובה נמוך + נרטיב UX | הנחיית משתמש חיה בלבד |

### נרטיב תרחיש
ארגון המוצר רוצה מחולל תדרוך למנהלים. SLM קל משקל (phi‑4‑mini) מנסח סיכומים; LLM גדול יותר (gpt‑oss‑20b) עשוי ללטש רק דוחות בעלי עדיפות גבוהה. סקריפטים של המפגש לוכדים מדדי זמן תגובה וטוקנים אמפיריים להצדקת עיצוב היברידי, בעוד שהדגמת Chainlit ממחישה כיצד שליפה מבוססת שומרת על תשובות המודל הקטן עובדתיות. דף הקונספט של WebGPU מספק נתיב חזון לעיבוד מלא בצד הלקוח כאשר האצת דפדפן מתבגרת.

### הקשר RAG מינימלי (Chainlit)
```python
DOCS = [
  "Foundry Local enables local model execution with OpenAI-compatible APIs.",
  "RAG combines retrieval and generation for grounded answers.",
  "SLMs provide efficiency advantages on constrained hardware."
]
```

### זרימת טיוטה→ליטוש היברידית (פסאודו)
```python
draft, _ = chat_once('phi-4-mini', messages=[{"role":"user","content":prompt}], max_tokens=280)
if len(draft) < 600:  # heuristic: escalate only for longer briefs or flagged topics
    final = draft
else:
    final, _ = chat_once('gpt-oss-20b', messages=[{"role":"user","content":f"Refine and polish:\n{draft}"}], max_tokens=220)
```

עקבו אחר שני רכיבי זמן התגובה כדי לדווח על עלות ממוצעת משולבת.

### שיפורים אופציונליים

| מיקוד | שיפור | למה | רמז ליישום |
|-------|-------|-----|------------|
| מדדים השוואתיים | עקבו אחר שימוש בטוקנים + זמן תגובה של הטוקן הראשון | מבט ביצועים הוליסטי | השתמשו בסקריפט benchmark משופר (מפגש 3) עם `BENCH_STREAM=1` |
| צינור היברידי | טיוטת SLM → ליטוש LLM | הפחתת זמן תגובה ועלות | יצירת טיוטה עם phi-4-mini, ליטוש סיכום עם gpt-oss-20b |
| ממשק משתמש זורם | UX טוב יותר ב-Chainlit | משוב הדרגתי | השתמשו ב-`stream=True` כאשר זרימה מקומית נחשפת; צברו חלקים |
| קאשינג WebGPU | אתחול JS מהיר יותר | הפחתת עומס קומפילציה | קאשינג של ארטיפקטים של שיידר מקומפל (יכולת ריצה עתידית) |
| סט QA דטרמיניסטי | השוואת מודלים הוגנת | הסרת שונות | רשימת הנחיות קבועה + `temperature=0` להרצות הערכה |
| דירוג תוצאות | עדשת איכות מובנית | מעבר לאנקדוטות | מדד פשוט: קוהרנטיות / עובדתיות / תמציתיות (1–5) |
| הערות אנרגיה / משאבים | דיון בכיתה | הצגת איזונים | השתמשו במוניטורים של מערכת הפעלה (Task Manager, `nvidia-smi`) + פלטי סקריפט benchmark |
| הדמיית עלות | הצדקה לפני ענן | תכנון סקיילינג | מיפוי טוקנים לתמחור ענן היפותטי לנרטיב TCO |
| פירוק זמן תגובה | זיהוי צווארי בקבוק | מיקוד אופטימיזציות | מדידת הכנת הנחיה, שליחת בקשה, טוקן ראשון, השלמה מלאה |
| RAG + LLM גיבוי | רשת ביטחון איכות | שיפור שאילתות קשות | אם אורך תשובת SLM < סף או ביטחון נמוך → הסלמה |

#### דוגמת דפוס טיוטה/ליטוש היברידי

```python
draft, _ = chat_once('phi-4-mini', messages=[{"role":"user","content":task}], max_tokens=300, temperature=0.4)
refine, _ = chat_once('gpt-oss-20b', messages=[{"role":"user","content":f"Improve clarity but keep facts:\n{draft}"}], max_tokens=220, temperature=0.3)
```

#### סקיצה לפירוק זמן תגובה

```python
import time
t0 = time.time(); # build messages
prep_ms = (time.time()-t0)*1000
t1 = time.time(); text,_ = chat_once(alias, messages=msgs, max_tokens=180)
full_ms = (time.time()-t1)*1000
print({"prep_ms": prep_ms, "full_gen_ms": full_ms})
```

השתמשו במבנה מדידה עקבי בין מודלים להשוואות הוגנות.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**הצהרת אחריות**:  
מסמך זה תורגם באמצעות שירות תרגום AI [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עשויים להכיל שגיאות או אי דיוקים. המסמך המקורי בשפתו המקורית צריך להיחשב כמקור סמכותי. למידע קריטי, מומלץ להשתמש בתרגום מקצועי אנושי. איננו נושאים באחריות לכל אי הבנות או פרשנויות שגויות הנובעות משימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
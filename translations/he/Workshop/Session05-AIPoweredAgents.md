# מפגש 5: בניית סוכנים מבוססי AI במהירות עם Foundry Local

## תקציר

עצבו ותזמנו סוכני AI מרובי תפקידים תוך שימוש ב-Foundry Local עם זמן תגובה נמוך ושמירה על פרטיות. תגדירו תפקידי סוכנים, אסטרטגיות זיכרון, דפוסי קריאה לכלים וגרפים לביצוע. המפגש מציג דפוסי בנייה שתוכלו להרחיב באמצעות Chainlit או LangGraph. פרויקט ההתחלה מרחיב את דוגמת הארכיטקטורה הקיימת של הסוכן כדי להוסיף שכבת זיכרון מתמשכת + ווים להערכה.

## מטרות למידה

- **הגדרת תפקידים**: הנחיות מערכת וגבולות יכולת
- **מימוש זיכרון**: קצר טווח (שיחה), ארוך טווח (וקטור / קובץ), מחברות זמניות
- **בניית תהליכי עבודה**: שלבים עוקבים, מתפצלים ומקבילים של סוכנים
- **שילוב כלים**: דפוס קריאה קל לכלי פונקציונלי
- **הערכה**: מעקב בסיסי + דירוג תוצאות מבוסס קריטריונים

## דרישות מקדימות

- השלמת מפגשים 1–4
- Python עם `foundry-local-sdk`, `openai`, אופציונלי `chainlit`
- מודלים מקומיים פועלים (לפחות `phi-4-mini`)

### קטע קוד לסביבת עבודה חוצת פלטפורמות

Windows:  
```powershell
py -m venv .venv
 .\.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install foundry-local-sdk openai
```
  
macOS:  
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install foundry-local-sdk openai
```
  
אם מפעילים סוכנים מ-macOS מול שירות מארח מרוחק ב-Windows:  
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```
  

## זרימת הדגמה (30 דקות)

### 1. הגדרת תפקידי סוכן וזיכרון (7 דקות)

צרו `samples/05-agents/agents_core.py`:  
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
  

### 2. דפוס בניית CLI (3 דקות)

```powershell
python samples/05-agents/agents_core.py
```
  

### 3. הוספת קריאה לכלים (7 דקות)

הרחיבו עם `samples/05-agents/tools.py`:  
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
  
שנו את `agents_core.py` כדי לאפשר תחביר פשוט לקריאה לכלים: המשתמש כותב `#tool:get_time` והסוכן מרחיב את פלט הכלי להקשר לפני יצירה.

### 4. תהליך עבודה מתוזמן (6 דקות)

צרו `samples/05-agents/orchestrator.py`:  
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
  

### 5. פרויקט התחלה: הרחבת `05-agent-architecture` (7 דקות)

הוסיפו:  
1. שכבת זיכרון מתמשכת (לדוגמה, הוספת שורות JSON של שיחות)  
2. קריטריונים פשוטים להערכה: דיוק, בהירות, סגנון  
3. ממשק קדמי אופציונלי של Chainlit (שני טאבים: שיחה ומעקב)  
4. מכונת מצבים בסגנון LangGraph (אם מוסיפים תלות) להחלטות מתפצלות  

## רשימת בדיקות לאימות

```powershell
foundry model run phi-4-mini
python samples/05-agents/orchestrator.py
```
  
צפו בפלט צינור מובנה עם הערת הזרקת כלים.

## סקירה של אסטרטגיות זיכרון

| שכבה | מטרה | דוגמה |
|------|-------|-------|
| קצר טווח | רציפות שיחה | N הודעות אחרונות |
| אפיזודית | זיכרון מפגש | JSON לכל מפגש |
| סמנטית | אחזור ארוך טווח | חנות וקטור של סיכומים |
| מחברת | שלבי חשיבה | שרשרת מחשבות פרטית |

## ווים להערכה (קונספטואלי)

```python
evaluation = {
  "factuality": None,  # manual or heuristic
  "clarity": None,
  "style": None,
  "latency_sec": generation_time,
  "model": model_used
}
```
  

## פתרון בעיות

| בעיה | סיבה | פתרון |
|------|------|-------|
| תשובות חוזרות | חלון הקשר גדול/קטן מדי | כוונון פרמטר חלון הזיכרון |
| כלי לא הופעל | תחביר שגוי | השתמשו בפורמט `#tool:tool_name` |
| תזמור איטי | מודלים קרים מרובים | הרצת הנחיות חימום מראש |

## מקורות

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python  
- LangGraph (קונספט אופציונלי): https://github.com/langchain-ai/langgraph  
- Chainlit: https://docs.chainlit.io  

---

**משך המפגש**: 30 דקות  
**רמת קושי**: מתקדם  

## תרחיש לדוגמה ומיפוי סדנה

| תסריט סדנה | תרחיש | מטרה | דוגמת הנחיה |
|-------------|--------|-------|-------------|
| `samples/session05/agents_orchestrator.py` / `notebooks/session05_agents_orchestrator.ipynb` | בוט מחקר ידע המפיק סיכומים ידידותיים למנהלים | צינור דו-סוכני (מחקר → ליטוש עריכה) עם מודלים נפרדים אופציונליים | הסבר מדוע הסקת קצה חשובה לציות. |
| (מורחב) קונספט `tools.py` | הוספת כלים להערכת זמן ומספר טוקנים | הדגמת דפוס קריאה קל לכלים | #tool:get_time |

### נרטיב תרחיש
צוות תיעוד הציות זקוק לתדריכים פנימיים מהירים המבוססים על ידע מקומי מבלי לשלוח טיוטות לשירותי ענן. סוכן מחקר אוסף נקודות עובדתיות תמציתיות; סוכן עורך משכתב בהירות למנהלים. ניתן להקצות כינויים למודלים נפרדים כדי לייעל זמן תגובה (SLM מהיר) מול ליטוש סגנוני (מודל גדול רק כשצריך).

### דוגמת סביבה מרובת מודלים
```powershell
cd Workshop/samples
set AGENT_MODEL_PRIMARY=phi-4-mini
set AGENT_MODEL_EDITOR=gpt-oss-20b
python -m session05.agents_orchestrator
```
  

### מבנה מעקב (אופציונלי)
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
  
שמרו כל שלב לקובץ JSONL לצורך דירוג קריטריונים מאוחר יותר.

### שיפורים אופציונליים

| נושא | שיפור | יתרון | סקיצה ליישום |
|------|-------|-------|--------------|
| תפקידי מודלים מרובים | מודלים נפרדים לכל סוכן (`AGENT_MODEL_PRIMARY`, `AGENT_MODEL_EDITOR`) | התמחות ומהירות | בחירת משתני סביבה כינויים, קריאה ל-`chat_once` עם כינוי לפי תפקיד |
| מעקב מובנה | מעקב JSON לכל פעולה (כלי, קלט, זמן תגובה, טוקנים) | ניפוי שגיאות והערכה | הוספת מילון לרשימה; כתיבה ל-`.jsonl` בסיום |
| שימור זיכרון | הקשר שיחה נטען מחדש | רציפות מפגש | שמירת `Agent.memory` ל-`sessions/<ts>.json` |
| רישום כלים | גילוי כלים דינמי | הרחבה | תחזוקת מילון `TOOLS` ובדיקת שמות/תיאורים |
| נסיונות חוזרים והמתנה | שרשראות ארוכות עמידות | הפחתת כשלים זמניים | עטיפת `act` עם try/except + המתנה אקספוננציאלית |
| דירוג קריטריונים | תוויות איכות אוטומטיות | מעקב אחר שיפורים | מעבר משני עם מודל: "דרג בהירות 1-5" |
| זיכרון וקטורי | אחזור סמנטי | הקשר ארוך טווח עשיר | הטמעת סיכומים, אחזור top-k להודעת מערכת |
| תשובות זורמות | תגובה מהירה יותר | שיפור חוויית משתמש | שימוש בתשדורת ברגע שהיא זמינה ושחרור טוקנים חלקיים |
| בדיקות דטרמיניסטיות | בקרת רגרסיה | CI יציב | הרצה עם `temperature=0`, זרעי הנחיה קבועים |
| הסתעפות מקבילה | חקר מהיר יותר | תפוקה | שימוש ב-`concurrent.futures` לשלבי סוכן עצמאיים |

#### דוגמת רשומת מעקב

```python
trace.append({
    "agent": agent.name,
    "input": prompt,
    "output_tokens": getattr(usage,'completion_tokens',None),
    "latency_ms": round((end-start)*1000,2),
    "tools_used": list(tool_calls)
})
```
  

#### הנחיית הערכה פשוטה

```python
score_prompt = f"Rate clarity (1-5) ONLY as a number for this answer:\n{answer}"
rating, _ = chat_once(PRIMARY_ALIAS, messages=[{"role":"user","content":score_prompt}], max_tokens=4, temperature=0)
```
  
שמרו זוגות (`answer`, `rating`) כדי לבנות גרף איכות היסטורי.

---

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום AI [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש להיות מודעים לכך שתרגומים אוטומטיים עשויים להכיל שגיאות או אי דיוקים. המסמך המקורי בשפתו המקורית צריך להיחשב כמקור סמכותי. עבור מידע קריטי, מומלץ להשתמש בתרגום מקצועי אנושי. איננו נושאים באחריות לאי הבנות או לפרשנויות שגויות הנובעות משימוש בתרגום זה.
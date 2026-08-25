# Συνεδρία 5: Δημιουργήστε γρήγορα Αντιπροσώπους με Τεχνητή Νοημοσύνη χρησιμοποιώντας το Foundry Local

## Περίληψη

Σχεδιάστε και οργανώστε πολυ-ρόλους αντιπροσώπων ΤΝ αξιοποιώντας τον χρόνο εκτέλεσης χαμηλής καθυστέρησης και προστασίας απορρήτου του Foundry Local. Θα ορίσετε ρόλους αντιπροσώπων, στρατηγικές μνήμης, μοτίβα κλήσεων εργαλείων και διαγράμματα εκτέλεσης. Η συνεδρία παρουσιάζει μοτίβα δομής που μπορείτε να επεκτείνετε με Chainlit ή LangGraph. Το αρχικό έργο επεκτείνει το υπάρχον παράδειγμα αρχιτεκτονικής αντιπροσώπου για να προσθέσει μόνιμη μνήμη + στοιχεία αξιολόγησης.

## Στόχοι Μάθησης

- **Ορισμός Ρόλων**: Συστήματα εντολών & όρια ικανοτήτων
- **Υλοποίηση Μνήμης**: Βραχυπρόθεσμη (διάλογος), μακροπρόθεσμη (vector / αρχείο), προσωρινά scratchpads
- **Δομή Workflows**: Διαδοχικά, διακλαδιζόμενα, και παράλληλα βήματα αντιπροσώπων
- **Ενσωμάτωση Εργαλείων**: Ελαφρύ μοτίβο κλήσης λειτουργιών εργαλείων
- **Αξιολόγηση**: Βασική ιχνηλάτηση + βαθμολόγηση αποτελεσμάτων με κριτήρια

## Προαπαιτούμενα

- Ολοκληρωμένες Συνεδρίες 1–4
- Python με `foundry-local-sdk`, `openai`, προαιρετικά `chainlit`
- Τοπικά μοντέλα σε λειτουργία (τουλάχιστον `phi-4-mini`)

### Απόσπασμα Περιβάλλοντος Cross-Platform

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

Αν εκτελείτε αντιπροσώπους από macOS απέναντι σε απομακρυσμένο Windows host service:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```

## Ροή Demo (30 λεπτά)

### 1. Ορισμός Ρόλων & Μνήμης Αντιπροσώπων (7 λεπτά)

Δημιουργήστε `samples/05-agents/agents_core.py`:

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

### 2. Μοτίβο Δομής CLI (3 λεπτά)

```powershell
python samples/05-agents/agents_core.py
```

### 3. Προσθήκη Κλήσης Εργαλείου (7 λεπτά)

Επεκτείνετε με `samples/05-agents/tools.py`:

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

Τροποποιήστε το `agents_core.py` για να επιτρέψετε απλή σύνταξη εργαλείων: ο χρήστης γράφει `#tool:get_time` και ο αντιπρόσωπος αναπτύσσει την έξοδο εργαλείου στο πλαίσιο πριν από τη γεννήτρια.

### 4. Οργανωμένη Ροή Εργασιών (6 λεπτά)

Δημιουργήστε `samples/05-agents/orchestrator.py`:

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

### 5. Αρχικό Έργο: Επέκταση `05-agent-architecture` (7 λεπτά)

Προσθέστε:
1. Μόνιμο επίπεδο μνήμης (π.χ., append γραμμές JSON συνομιλιών)
2. Απλό κριτήριο αξιολόγησης: placeholders αλήθειας / σαφήνειας / στυλ
3. Προαιρετικό front-end Chainlit (δύο καρτέλες: συνομιλία & ιχνηλασίες)
4. Προαιρετική μηχανή κατάστασης τύπου LangGraph (αν προσθέσετε εξάρτηση) για διακλαδώσεις αποφάσεων

## Λίστα Ελέγχου Επικύρωσης

```powershell
foundry model run phi-4-mini
python samples/05-agents/orchestrator.py
```

Αναμένετε δομημένη έξοδο pipeline με σημείωση ένεσης εργαλείου.

## Επισκόπηση Στρατηγικών Μνήμης

| Επίπεδο | Σκοπός | Παράδειγμα |
|-------|---------|---------|
| Βραχυπρόθεσμη | Συνέχεια διαλόγου | Τελευταία Ν μηνύματα |
| Επεισοδιακή | Ανάκληση συνεδρίας | JSON ανά συνεδρία |
| Σημασιολογική | Μακροπρόθεσμη ανάκτηση | Αποθήκη διανυσμάτων συνοψίσεων |
| Scratchpad | Βήματα συλλογισμού | Ενσωματωμένη αλυσίδα σκέψης (ιδιωτικό) |

## Άγκυρες Αξιολόγησης (Εννοιολογικά)

```python
evaluation = {
  "factuality": None,  # χειροκίνητο ή ευρετικό
  "clarity": None,
  "style": None,
  "latency_sec": generation_time,
  "model": model_used
}
```

## Επιλύσεις Προβλημάτων

| Πρόβλημα | Αιτία | Επίλυση |
|-------|------|------------|
| Επαναλαμβανόμενες απαντήσεις | Παράθυρο πλαισίου πολύ μεγάλο/μικρό | Ρυθμίστε την παράμετρο παραθύρου μνήμης |
| Το εργαλείο δεν καλείται | Λάθος σύνταξη | Χρησιμοποιήστε τη μορφή `#tool:tool_name` |
| Αργή ορχήστρωση | Πολλαπλά ψυχρά μοντέλα | Προθερμάνετε με προκαταρκτικές εντολές |

## Αναφορές

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- LangGraph (προαιρετική έννοια): https://github.com/langchain-ai/langgraph
- Chainlit: https://docs.chainlit.io

---

**Διάρκεια Συνεδρίας**: 30 λεπτά  
**Δυσκολία**: Προχωρημένο

## Παράδειγμα Σενάριου & Χαρτογράφηση Εργαστηρίου

| Σενάριο Εργαστηρίου | Σενάριο | Στόχος | Παράδειγμα Εντολής |
|-----------------|----------|-----------|----------------|
| `samples/session05/agents_orchestrator.py` / `notebooks/session05_agents_orchestrator.ipynb` | Bot έρευνας γνώσης που παράγει συνοπτικές αναφορές φιλικές προς στελέχη | Pipeline δύο αντιπροσώπων (έρευνα → επεξεργασία) με προαιρετικά διακριτά μοντέλα | Εξηγήστε γιατί η inference στο edge είναι σημαντική για τη συμμόρφωση. |
| (Επεκταμένο) concept `tools.py` | Προσθήκη εργαλείων εκτίμησης χρόνου & tokens | Επίδειξη ελαφρύ μοτίβου κλήσης εργαλείων | #tool:get_time |

### Αφήγηση Σεναρίου
Η ομάδα τεκμηρίωσης συμμόρφωσης χρειάζεται γρήγορες εσωτερικές ενημερώσεις βασισμένες σε τοπική γνώση χωρίς να στέλνει προσχέδια σε υπηρεσίες σύννεφου. Ένας agent ερευνητής συγκεντρώνει συνοπτικά πραγματικά σημεία; ένας agent επεξεργαστής ξαναγράφει για σαφήνεια εκτελεστικού. Διακριτά ψευδώνυμα μοντέλων μπορούν να ανατεθούν για βελτιστοποίηση καθυστέρησης (γρήγορο SLM) έναντι στιλιστικής επεξεργασίας (μεγαλύτερο μοντέλο μόνο όταν χρειάζεται).

### Παράδειγμα Πολυ-Μοντέλου Περιβάλλοντος
```powershell
cd Workshop/samples
set AGENT_MODEL_PRIMARY=phi-4-mini
set AGENT_MODEL_EDITOR=gpt-oss-20b
python -m session05.agents_orchestrator
```

### Δομή Ιχνηλατήσεων (Προαιρετικό)
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

Αποθηκεύστε κάθε βήμα σε αρχείο JSONL για βαθμολόγηση με κριτήρια αργότερα.

### Προαιρετικές Βελτιώσεις

| Θέμα | Βελτίωση | Όφελος | Σχεδίαση Υλοποίησης |
|-------|------------|---------|-----------------------|
| Ρόλοι Πολυ-Μοντέλου | Διακριτά μοντέλα ανά agent (`AGENT_MODEL_PRIMARY`, `AGENT_MODEL_EDITOR`) | Εξειδίκευση & ταχύτητα | Επιλογή ψευδωνύμων env vars, κλήση `chat_once` με ανά ρόλο ψευδώνυμο |
| Δομημένες Ιχνηλατήσεις | JSON ιχνηλάτηση κάθε act(tool,input,latency,tokens) | Ανίχνευση σφαλμάτων & αξιολόγηση | Επισύναψη dict σε λίστα; εγγραφή `.jsonl` στο τέλος |
| Μόνιμη Μνήμη | Επαναφορτιζόμενο πλαίσιο διαλόγου | Συνέχεια συνεδρίας | Αποθήκευση `Agent.memory` σε `sessions/<ts>.json` |
| Μητρώο Εργαλείων | Δυναμική ανίχνευση εργαλείων | Επεκτασιμότητα | Συντήρηση λεξικού `TOOLS` & διερεύνηση ονομάτων/περιγραφών |
| Επαναπροσπάθεια & Backoff | Ανθεκτικές μακριές αλυσίδες | Μείωση διακοπτόμενων αποτυχιών | Περιτύλιγμα `act` με try/except + εκθετικό backoff |
| Βαθμολόγηση με Κριτήριο | Αυτόματες ποιοτικές ετικέτες | Παρακολούθηση βελτιώσεων | Δευτερεύουσα παρέμβαση με prompt μοντέλου: "Βαθμολογήστε σαφήνεια 1-5" |
| Διανυσματική Μνήμη | Σημασιολογική ανάκληση | Πλούσιο μακροπρόθεσμο πλαίσιο | Ενσωμάτωση συνοψίσεων, ανάκτηση top-k σε σύστημα μηνύματος |
| Streaming Απαντήσεις | Γρηγορότερη αντιληπτή ανταπόκριση | Βελτίωση UX | Χρήση streaming μόλις είναι διαθέσιμο και εκκένωση μερικών tokens |
| Ντετερμινιστικά Τεστ | Έλεγχος παλινδρόμησης | Σταθερό CI | Εκτέλεση με `temperature=0`, σταθερά seeds prompt |
| Παράλληλη Διακλάδωση | Γρηγορότερη εξερεύνηση | Μέγιστος ρυθμός | Χρήση `concurrent.futures` για ανεξάρτητα βήματα agent |

#### Παράδειγμα Καταγραφής Ιχνηλάτησης

```python
trace.append({
    "agent": agent.name,
    "input": prompt,
    "output_tokens": getattr(usage,'completion_tokens',None),
    "latency_ms": round((end-start)*1000,2),
    "tools_used": list(tool_calls)
})
```

#### Απλό Prompt Αξιολόγησης

```python
score_prompt = f"Rate clarity (1-5) ONLY as a number for this answer:\n{answer}"
rating, _ = chat_once(PRIMARY_ALIAS, messages=[{"role":"user","content":score_prompt}], max_tokens=4, temperature=0)
```

Αποθηκεύστε τα ζεύγη (`answer`, `rating`) για να δημιουργήσετε ιστορικό γράφημα ποιότητας.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Αποποίηση ευθυνών**:
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία μετάφρασης με τεχνητή νοημοσύνη [Co-op Translator](https://github.com/Azure/co-op-translator). Ενώ επιδιώκουμε την ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτοματοποιημένες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
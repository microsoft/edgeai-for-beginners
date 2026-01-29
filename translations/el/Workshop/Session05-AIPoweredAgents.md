# Συνεδρία 5: Δημιουργία Πρακτόρων με Τεχνητή Νοημοσύνη Γρήγορα με το Foundry Local

## Περίληψη

Σχεδιάστε και οργανώστε πολυ-ρόλους πρακτόρων AI αξιοποιώντας το περιβάλλον εκτέλεσης χαμηλής καθυστέρησης και προστασίας ιδιωτικότητας του Foundry Local. Θα ορίσετε ρόλους πρακτόρων, στρατηγικές μνήμης, μοτίβα κλήσης εργαλείων και γραφήματα εκτέλεσης. Η συνεδρία παρουσιάζει μοτίβα σκαλωσιάς που μπορείτε να επεκτείνετε με το Chainlit ή το LangGraph. Το αρχικό έργο επεκτείνει το υπάρχον δείγμα αρχιτεκτονικής πρακτόρων για να προσθέσει διατήρηση μνήμης και γάντζους αξιολόγησης.

## Στόχοι Μάθησης

- **Ορισμός Ρόλων**: Προτροπές συστήματος & όρια δυνατοτήτων
- **Υλοποίηση Μνήμης**: Βραχυπρόθεσμη (συνομιλία), μακροπρόθεσμη (vector / αρχείο), προσωρινά scratchpads
- **Σκαλωσιά Ροών Εργασίας**: Διαδοχικά, διακλαδισμένα και παράλληλα βήματα πρακτόρων
- **Ενσωμάτωση Εργαλείων**: Ελαφρύ μοτίβο κλήσης εργαλείων λειτουργίας
- **Αξιολόγηση**: Βασική ανίχνευση + βαθμολόγηση αποτελεσμάτων με βάση κριτήρια

## Προαπαιτούμενα

- Ολοκληρωμένες συνεδρίες 1–4
- Python με `foundry-local-sdk`, `openai`, προαιρετικά `chainlit`
- Τοπικά μοντέλα σε λειτουργία (τουλάχιστον `phi-4-mini`)

### Απόσπασμα Περιβάλλοντος Πολλαπλών Πλατφορμών

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

Αν εκτελείτε πράκτορες από macOS σε απομακρυσμένη υπηρεσία Windows:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```


## Ροή Επίδειξης (30 λεπτά)

### 1. Ορισμός Ρόλων Πρακτόρων & Μνήμης (7 λεπτά)

Δημιουργήστε το `samples/05-agents/agents_core.py`:

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


### 2. Μοτίβο Σκαλωσιάς CLI (3 λεπτά)

```powershell
python samples/05-agents/agents_core.py
```


### 3. Προσθήκη Κλήσης Εργαλείων (7 λεπτά)

Επεκτείνετε με το `samples/05-agents/tools.py`:

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


Τροποποιήστε το `agents_core.py` για να επιτρέψετε απλή σύνταξη εργαλείων: ο χρήστης γράφει `#tool:get_time` και ο πράκτορας επεκτείνει την έξοδο του εργαλείου στο πλαίσιο πριν από τη δημιουργία.

### 4. Οργανωμένη Ροή Εργασίας (6 λεπτά)

Δημιουργήστε το `samples/05-agents/orchestrator.py`:

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


### 5. Αρχικό Έργο: Επέκταση του `05-agent-architecture` (7 λεπτά)

Προσθέστε:
1. Στρώμα μνήμης διατήρησης (π.χ., προσθήκη γραμμών JSON συνομιλιών)
2. Απλό κριτήριο αξιολόγησης: placeholders για πραγματικότητα / σαφήνεια / στυλ
3. Προαιρετικό front-end Chainlit (δύο καρτέλες: συνομιλία & ανιχνεύσεις)
4. Προαιρετική μηχανή κατάστασης τύπου LangGraph (αν προστεθεί εξάρτηση) για αποφάσεις διακλάδωσης

## Λίστα Ελέγχου Επικύρωσης

```powershell
foundry model run phi-4-mini
python samples/05-agents/orchestrator.py
```


Αναμένετε δομημένη έξοδο αγωγού με σημείωση έγχυσης εργαλείου.

## Επισκόπηση Στρατηγικών Μνήμης

| Στρώμα | Σκοπός | Παράδειγμα |
|-------|---------|---------|
| Βραχυπρόθεσμη | Συνέχεια διαλόγου | Τελευταία N μηνύματα |
| Επεισοδιακή | Ανάκληση συνεδρίας | JSON ανά συνεδρία |
| Σημασιολογική | Μακροπρόθεσμη ανάκτηση | Vector store περιλήψεων |
| Scratchpad | Βήματα συλλογισμού | Ενσωματωμένη αλυσίδα σκέψης (ιδιωτική) |

## Γάντζοι Αξιολόγησης (Εννοιολογικά)

```python
evaluation = {
  "factuality": None,  # manual or heuristic
  "clarity": None,
  "style": None,
  "latency_sec": generation_time,
  "model": model_used
}
```


## Επίλυση Προβλημάτων

| Πρόβλημα | Αιτία | Λύση |
|-------|------|------------|
| Επαναλαμβανόμενες απαντήσεις | Το παράθυρο περιεχομένου είναι πολύ μεγάλο/μικρό | Ρυθμίστε την παράμετρο παραθύρου μνήμης |
| Το εργαλείο δεν καλείται | Λανθασμένη σύνταξη | Χρησιμοποιήστε τη μορφή `#tool:tool_name` |
| Αργή οργάνωση | Πολλαπλά κρύα μοντέλα | Εκτελέστε προτροπές προθέρμανσης εκ των προτέρων |

## Αναφορές

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- LangGraph (προαιρετική έννοια): https://github.com/langchain-ai/langgraph
- Chainlit: https://docs.chainlit.io

---

**Διάρκεια Συνεδρίας**: 30 λεπτά  
**Δυσκολία**: Προχωρημένο

## Δείγμα Σεναρίου & Χαρτογράφηση Εργαστηρίου

| Σενάριο Εργαστηρίου | Σενάριο | Στόχος | Παράδειγμα Προτροπής |
|-----------------|----------|-----------|----------------|
| `samples/session05/agents_orchestrator.py` / `notebooks/session05_agents_orchestrator.ipynb` | Bot έρευνας γνώσης που παράγει περιλήψεις φιλικές προς στελέχη | Αγωγός δύο πρακτόρων (έρευνα → επεξεργασία) με προαιρετικά ξεχωριστά μοντέλα | Εξηγήστε γιατί η τοπική επεξεργασία είναι σημαντική για τη συμμόρφωση. |
| (Επέκταση) έννοια `tools.py` | Προσθήκη εργαλείων εκτίμησης χρόνου & tokens | Επίδειξη ελαφρού μοτίβου κλήσης εργαλείων | #tool:get_time |

### Αφήγηση Σεναρίου

Η ομάδα τεκμηρίωσης συμμόρφωσης χρειάζεται γρήγορες εσωτερικές περιλήψεις που προέρχονται από τοπική γνώση χωρίς να στέλνουν προσχέδια σε υπηρεσίες cloud. Ένας πράκτορας ερευνητής συλλέγει συνοπτικά πραγματικά σημεία, ενώ ένας πράκτορας συντάκτης ξαναγράφει για εκτελεστική σαφήνεια. Μπορούν να ανατεθούν ξεχωριστά ψευδώνυμα μοντέλων για βελτιστοποίηση καθυστέρησης (γρήγορο SLM) έναντι στιλιστικής βελτίωσης (μεγαλύτερο μοντέλο μόνο όταν χρειάζεται).

### Παράδειγμα Περιβάλλοντος Πολλαπλών Μοντέλων

```powershell
cd Workshop/samples
set AGENT_MODEL_PRIMARY=phi-4-mini
set AGENT_MODEL_EDITOR=gpt-oss-20b
python -m session05.agents_orchestrator
```


### Δομή Ανίχνευσης (Προαιρετική)

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


Αποθηκεύστε κάθε βήμα σε ένα αρχείο JSONL για μεταγενέστερη βαθμολόγηση με κριτήρια.

### Προαιρετικές Βελτιώσεις

| Θέμα | Βελτίωση | Όφελος | Σχεδιάγραμμα Υλοποίησης |
|-------|------------|---------|-----------------------|
| Ρόλοι Πολλαπλών Μοντέλων | Ξεχωριστά μοντέλα ανά πράκτορα (`AGENT_MODEL_PRIMARY`, `AGENT_MODEL_EDITOR`) | Εξειδίκευση & ταχύτητα | Επιλέξτε ψευδώνυμα περιβάλλοντος, καλέστε `chat_once` με ψευδώνυμο ανά ρόλο |
| Δομημένες Ανιχνεύσεις | JSON ανίχνευση κάθε πράξης (εργαλείο, είσοδος, καθυστέρηση, tokens) | Εντοπισμός σφαλμάτων & αξιολόγηση | Προσθέστε dict σε λίστα; γράψτε `.jsonl` στο τέλος |
| Διατήρηση Μνήμης | Επαναφορτώσιμο πλαίσιο διαλόγου | Συνέχεια συνεδρίας | Αποθηκεύστε το `Agent.memory` σε `sessions/<ts>.json` |
| Καταχώρηση Εργαλείων | Δυναμική ανακάλυψη εργαλείων | Επεκτασιμότητα | Διατηρήστε το dict `TOOLS` & εξετάστε ονόματα/περιγραφές |
| Επανάληψη & Ανάκαμψη | Ανθεκτικές μακρές αλυσίδες | Μείωση προσωρινών αποτυχιών | Τυλίξτε το `act` με try/except + εκθετική ανάκαμψη |
| Βαθμολόγηση με Κριτήρια | Αυτοματοποιημένες ποιοτικές ετικέτες | Παρακολούθηση βελτιώσεων | Δευτερεύουσα προτροπή μοντέλου: "Βαθμολογήστε τη σαφήνεια 1-5" |
| Σημασιολογική Μνήμη | Ανάκληση μακροπρόθεσμου περιεχομένου | Πλούσιο μακροπρόθεσμο πλαίσιο | Ενσωματώστε περιλήψεις, ανακτήστε top-k στο μήνυμα συστήματος |
| Ροές Απαντήσεων | Ταχύτερη αντιληπτή απόκριση | Βελτίωση UX | Χρησιμοποιήστε streaming όταν είναι διαθέσιμο και αποθηκεύστε μερικά tokens |
| Ντετερμινιστικά Τεστ | Έλεγχος παλινδρόμησης | Σταθερό CI | Εκτελέστε με `temperature=0`, σταθερούς σπόρους προτροπής |
| Παράλληλη Διακλάδωση | Ταχύτερη εξερεύνηση | Απόδοση | Χρησιμοποιήστε το `concurrent.futures` για ανεξάρτητα βήματα πρακτόρων |

#### Παράδειγμα Εγγραφής Ανίχνευσης

```python
trace.append({
    "agent": agent.name,
    "input": prompt,
    "output_tokens": getattr(usage,'completion_tokens',None),
    "latency_ms": round((end-start)*1000,2),
    "tools_used": list(tool_calls)
})
```


#### Απλή Προτροπή Αξιολόγησης

```python
score_prompt = f"Rate clarity (1-5) ONLY as a number for this answer:\n{answer}"
rating, _ = chat_once(PRIMARY_ALIAS, messages=[{"role":"user","content":score_prompt}], max_tokens=4, temperature=0)
```


Αποθηκεύστε ζεύγη (`answer`, `rating`) για να δημιουργήσετε ένα ιστορικό γράφημα ποιότητας.

---

**Αποποίηση ευθύνης**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία αυτόματης μετάφρασης [Co-op Translator](https://github.com/Azure/co-op-translator). Παρόλο που καταβάλλουμε προσπάθειες για ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτόματες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα θα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή εσφαλμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.
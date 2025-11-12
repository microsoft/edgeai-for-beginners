<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "fea4cb0f47a5011f0df128f5635133a5",
  "translation_date": "2025-11-11T23:02:55+00:00",
  "source_file": "Workshop/Session04-CuttingEdgeModels.md",
  "language_code": "el"
}
-->
# Συνεδρία 4: Εξερεύνηση Σύγχρονων Μοντέλων – LLMs, SLMs & Τοπική Επεξεργασία

## Περίληψη

Συγκρίνετε Μεγάλα Γλωσσικά Μοντέλα (LLMs) και Μικρά Γλωσσικά Μοντέλα (SLMs) για σενάρια επεξεργασίας τοπικά και στο cloud. Μάθετε μοτίβα ανάπτυξης αξιοποιώντας την επιτάχυνση του ONNX Runtime, την εκτέλεση WebGPU και υβριδικές εμπειρίες RAG. Περιλαμβάνει επίδειξη Chainlit RAG με τοπικό μοντέλο και προαιρετική εξερεύνηση OpenWebUI. Θα προσαρμόσετε ένα αρχικό WebGPU inference και θα αξιολογήσετε τις δυνατότητες και τις συμβιβαστικές λύσεις κόστους/απόδοσης μεταξύ Phi και GPT-OSS-20B.

## Στόχοι Μάθησης

- **Σύγκριση** SLM και LLM ως προς την καθυστέρηση, τη μνήμη και την ποιότητα
- **Ανάπτυξη** μοντέλων με ONNXRuntime και (όπου υποστηρίζεται) WebGPU
- **Εκτέλεση** επεξεργασίας μέσω browser (διαδραστική επίδειξη με προστασία ιδιωτικότητας)
- **Ενσωμάτωση** ενός pipeline Chainlit RAG με τοπικό backend SLM
- **Αξιολόγηση** χρησιμοποιώντας ελαφριά ποιοτικά και οικονομικά κριτήρια

## Προαπαιτούμενα

- Ολοκληρωμένες συνεδρίες 1–3
- Εγκατεστημένο `chainlit` (περιλαμβάνεται ήδη στο `requirements.txt` για το Module08)
- Browser με δυνατότητα WebGPU (Edge / Chrome τελευταίες εκδόσεις σε Windows 11)
- Ενεργό Foundry Local (`foundry service status`)

### Σημειώσεις Διαλειτουργικότητας

Τα Windows παραμένουν το κύριο περιβάλλον στόχος. Για προγραμματιστές macOS που περιμένουν εγγενείς δυαδικούς κώδικες:
1. Εκτελέστε το Foundry Local σε VM Windows 11 (Parallels / UTM) Ή σε απομακρυσμένο σταθμό εργασίας Windows.
2. Ενεργοποιήστε την υπηρεσία (προεπιλεγμένη θύρα 5273) και ρυθμίστε στο macOS:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```
3. Χρησιμοποιήστε τα ίδια βήματα για το Python virtual environment όπως στις προηγούμενες συνεδρίες.

Εγκατάσταση Chainlit (και στις δύο πλατφόρμες):
```bash
pip install chainlit
```

## Ροή Επίδειξης (30 λεπτά)

### 1. Σύγκριση Phi (SLM) και GPT-OSS-20B (LLM) (6 λεπτά)

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

Παρακολουθήστε: βάθος απάντησης, ακρίβεια γεγονότων, πλούτο ύφους, καθυστέρηση.

Παρατηρήστε αλλαγές στην απόδοση μετά την ενεργοποίηση GPU έναντι μόνο CPU.

### 3. Επεξεργασία WebGPU στον Browser (6 λεπτά)

Προσαρμόστε το αρχικό `04-webgpu-inference` (δημιουργήστε `samples/04-cutting-edge/webgpu_demo.html`):

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

Ανοίξτε το αρχείο σε browser και παρατηρήστε την τοπική επεξεργασία με χαμηλή καθυστέρηση.

### 4. Εφαρμογή Chainlit RAG Chat (7 λεπτά)

Ελάχιστο `samples/04-cutting-edge/chainlit_app.py`:

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

Εκτέλεση:

```powershell
chainlit run samples/04-cutting-edge/chainlit_app.py -w
```

### 5. Αρχικό Έργο: Προσαρμογή `04-webgpu-inference` (6 λεπτά)

Παραδοτέα:
- Αντικαταστήστε τη λογική fetch placeholder με streaming tokens (χρησιμοποιήστε την παραλλαγή endpoint `stream=True` μόλις ενεργοποιηθεί)
- Προσθέστε διάγραμμα καθυστέρησης (client-side) για εναλλαγές μεταξύ phi και gpt-oss-20b
- Ενσωματώστε το RAG context inline (textarea για έγγραφα αναφοράς)

## Κριτήρια Αξιολόγησης

| Κατηγορία | Phi-4-mini | GPT-OSS-20B | Παρατήρηση |
|----------|------------|-------------|-------------|
| Καθυστέρηση (κρύο) | Γρήγορη | Αργή | Το SLM ζεσταίνεται γρήγορα |
| Μνήμη | Χαμηλή | Υψηλή | Εφικτότητα συσκευής |
| Προσκόλληση στο πλαίσιο | Καλή | Ισχυρή | Το μεγαλύτερο μοντέλο μπορεί να είναι πιο περιγραφικό |
| Κόστος (τοπικό) | Ελάχιστο | Υψηλότερο (πόροι) | Συμβιβασμός ενέργειας/χρόνου |
| Καλύτερη χρήση | Εφαρμογές Edge | Βαθιά ανάλυση | Πιθανή υβριδική λύση |

## Επικύρωση Περιβάλλοντος

```powershell
# List catalog (no --running flag; loaded models are those you have previously run)
foundry model list

# For runtime metrics use the Python benchmark script (Session 3) and OS tools (Task Manager / nvidia-smi) instead of 'model stats'
# Example:
#   cd Workshop/samples
#   set BENCH_MODELS=phi-4-mini,gpt-oss-20b
#   python -m session03.benchmark_oss_models
```

## Επίλυση Προβλημάτων

| Σύμπτωμα | Αιτία | Ενέργεια |
|---------|-------|--------|
| Αποτυχία fetch ιστοσελίδας | CORS ή υπηρεσία εκτός λειτουργίας | Χρησιμοποιήστε `curl` για επαλήθευση του endpoint; ενεργοποιήστε CORS proxy αν χρειάζεται |
| Κενό Chainlit | Env μη ενεργό | Ενεργοποιήστε το venv και επανεγκαταστήστε τις εξαρτήσεις |
| Υψηλή καθυστέρηση | Το μοντέλο μόλις φορτώθηκε | Ζεστάνετε με μικρή ακολουθία προτροπών |

## Αναφορές

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- Chainlit Docs: https://docs.chainlit.io
- RAG Evaluation (Ragas): https://docs.ragas.io

---

**Διάρκεια Συνεδρίας**: 30 λεπτά  
**Δυσκολία**: Προχωρημένο

## Δείγμα Σεναρίου & Χαρτογράφηση Εργαστηρίου

| Τεχνουργήματα Εργαστηρίου | Σενάριο | Στόχος | Πηγή Δεδομένων / Προτροπών |
|--------------------|----------|-----------|----------------------|
| `samples/session04/model_compare.py` / `notebooks/session04_model_compare.ipynb` | Ομάδα αρχιτεκτονικής που αξιολογεί SLM και LLM για γεννήτρια εκτελεστικών περιλήψεων | Ποσοτικοποίηση καθυστέρησης + διαφορά χρήσης token | Μοναδική μεταβλητή περιβάλλοντος `COMPARE_PROMPT` |
| `chainlit_app.py` (επίδειξη RAG) | Πρωτότυπο εσωτερικού βοηθού γνώσης | Εδραίωση σύντομων απαντήσεων με ελάχιστη λεξική ανάκτηση | Ενσωματωμένη λίστα `DOCS` στο αρχείο |
| `webgpu_demo.html` | Προεπισκόπηση μελλοντικής επεξεργασίας στον browser | Εμφάνιση τοπικής επεξεργασίας με χαμηλή καθυστέρηση + αφήγηση UX | Μόνο ζωντανή προτροπή χρήστη |

### Αφήγηση Σεναρίου
Η ομάδα προϊόντων θέλει μια γεννήτρια εκτελεστικών περιλήψεων. Ένα ελαφρύ SLM (phi‑4‑mini) δημιουργεί προσχέδια περιλήψεων, ενώ ένα μεγαλύτερο LLM (gpt‑oss‑20b) μπορεί να βελτιώσει μόνο αναφορές υψηλής προτεραιότητας. Τα σενάρια συνεδρίας καταγράφουν εμπειρικά δεδομένα καθυστέρησης και token για να δικαιολογήσουν έναν υβριδικό σχεδιασμό, ενώ η επίδειξη Chainlit δείχνει πώς η εδραίωση ανάκτησης διατηρεί τις απαντήσεις του μικρού μοντέλου ακριβείς. Η σελίδα concept WebGPU παρέχει ένα μονοπάτι όρασης για πλήρως client-side επεξεργασία όταν η επιτάχυνση του browser ωριμάσει.

### Ελάχιστο RAG Context (Chainlit)
```python
DOCS = [
  "Foundry Local enables local model execution with OpenAI-compatible APIs.",
  "RAG combines retrieval and generation for grounded answers.",
  "SLMs provide efficiency advantages on constrained hardware."
]
```

### Υβριδική Ροή Προσχέδιο→Βελτίωση (Ψευδοκώδικας)
```python
draft, _ = chat_once('phi-4-mini', messages=[{"role":"user","content":prompt}], max_tokens=280)
if len(draft) < 600:  # heuristic: escalate only for longer briefs or flagged topics
    final = draft
else:
    final, _ = chat_once('gpt-oss-20b', messages=[{"role":"user","content":f"Refine and polish:\n{draft}"}], max_tokens=220)
```

Παρακολουθήστε και τα δύο στοιχεία καθυστέρησης για να αναφέρετε το μέσο κόστος.

### Προαιρετικές Βελτιώσεις

| Εστίαση | Βελτίωση | Γιατί | Υπόδειξη Υλοποίησης |
|-------|------------|-----|---------------------|
| Συγκριτικά Μετρικά | Παρακολούθηση χρήσης token + καθυστέρηση πρώτου token | Ολιστική άποψη απόδοσης | Χρησιμοποιήστε βελτιωμένο script benchmark (Συνεδρία 3) με `BENCH_STREAM=1` |
| Υβριδικό Pipeline | Προσχέδιο SLM → Βελτίωση LLM | Μείωση καθυστέρησης & κόστους | Δημιουργία με phi-4-mini, βελτίωση περίληψης με gpt-oss-20b |
| Streaming UI | Καλύτερο UX στο Chainlit | Σταδιακή ανατροφοδότηση | Χρησιμοποιήστε `stream=True` μόλις εκτεθεί το τοπικό streaming; συσσώρευση chunks |
| WebGPU Caching | Γρηγορότερη JS αρχικοποίηση | Μείωση κόστους επανασύνθεσης | Αποθήκευση compiled shader artifacts (μελλοντική δυνατότητα runtime) |
| Καθορισμένο QA Set | Δίκαιη σύγκριση μοντέλων | Αφαίρεση μεταβλητότητας | Σταθερή λίστα προτροπών + `temperature=0` για αξιολογήσεις |
| Βαθμολόγηση Αποτελεσμάτων | Δομημένος φακός ποιότητας | Πέρα από ανέκδοτα | Απλή βαθμολογία: συνοχή / ακρίβεια / συντομία (1–5) |
| Σημειώσεις Ενέργειας / Πόρων | Συζήτηση στην τάξη | Εμφάνιση συμβιβασμών | Χρησιμοποιήστε OS monitors (Task Manager, `nvidia-smi`) + εξόδους script benchmark |
| Εξομοίωση Κόστους | Δικαιολόγηση πριν το cloud | Σχεδιασμός κλιμάκωσης | Χαρτογράφηση tokens σε υποθετική τιμολόγηση cloud για αφήγηση TCO |
| Ανάλυση Καθυστέρησης | Εντοπισμός bottlenecks | Στόχευση βελτιστοποιήσεων | Μέτρηση προετοιμασίας προτροπής, αποστολής αιτήματος, πρώτου token, πλήρους ολοκλήρωσης |
| RAG + LLM Fallback | Δίχτυ ασφαλείας ποιότητας | Βελτίωση δύσκολων ερωτήσεων | Αν το μήκος απάντησης SLM < όριο ή χαμηλή εμπιστοσύνη → κλιμάκωση |

#### Παράδειγμα Υβριδικού Προτύπου Προσχέδιο/Βελτίωση

```python
draft, _ = chat_once('phi-4-mini', messages=[{"role":"user","content":task}], max_tokens=300, temperature=0.4)
refine, _ = chat_once('gpt-oss-20b', messages=[{"role":"user","content":f"Improve clarity but keep facts:\n{draft}"}], max_tokens=220, temperature=0.3)
```

#### Σκίτσο Ανάλυσης Καθυστέρησης

```python
import time
t0 = time.time(); # build messages
prep_ms = (time.time()-t0)*1000
t1 = time.time(); text,_ = chat_once(alias, messages=msgs, max_tokens=180)
full_ms = (time.time()-t1)*1000
print({"prep_ms": prep_ms, "full_gen_ms": full_ms})
```

Χρησιμοποιήστε συνεπή πλαίσια μέτρησης μεταξύ μοντέλων για δίκαιες συγκρίσεις.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Αποποίηση ευθύνης**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία μετάφρασης AI [Co-op Translator](https://github.com/Azure/co-op-translator). Παρόλο που καταβάλλουμε προσπάθειες για ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτοματοποιημένες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα θα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή εσφαλμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
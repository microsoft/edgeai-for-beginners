<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "15a93babfc2b8a0bf8dadb2418637629",
  "translation_date": "2025-11-11T23:06:14+00:00",
  "source_file": "Workshop/Session03-OpenSourceModels.md",
  "language_code": "el"
}
-->
# Συνεδρία 3: Μοντέλα Ανοιχτού Κώδικα στο Foundry Local

## Περίληψη

Ανακαλύψτε πώς να ενσωματώσετε μοντέλα Hugging Face και άλλα μοντέλα ανοιχτού κώδικα στο Foundry Local. Μάθετε στρατηγικές επιλογής, διαδικασίες συνεισφοράς στην κοινότητα, μεθοδολογία σύγκρισης απόδοσης και πώς να επεκτείνετε το Foundry με προσαρμοσμένες εγγραφές μοντέλων. Αυτή η συνεδρία συνδέεται με τα εβδομαδιαία θέματα εξερεύνησης "Model Mondays" και σας εξοπλίζει για να αξιολογήσετε και να λειτουργήσετε μοντέλα ανοιχτού κώδικα τοπικά πριν από την κλιμάκωση στο Azure.

## Στόχοι Μάθησης

Μέχρι το τέλος θα μπορείτε να:

- **Ανακαλύψετε & Αξιολογήσετε**: Να εντοπίσετε υποψήφια μοντέλα (mistral, gemma, qwen, deepseek) χρησιμοποιώντας την ισορροπία ποιότητας έναντι πόρων.
- **Φορτώσετε & Εκτελέσετε**: Να χρησιμοποιήσετε το Foundry Local CLI για λήψη, προσωρινή αποθήκευση και εκκίνηση μοντέλων της κοινότητας.
- **Αξιολογήσετε**: Να εφαρμόσετε συνεπείς ευρετικές μεθόδους για καθυστέρηση + ρυθμό επεξεργασίας tokens + ποιότητα.
- **Επεκτείνετε**: Να εγγράψετε ή να προσαρμόσετε ένα προσαρμοσμένο wrapper μοντέλου σύμφωνα με τα πρότυπα συμβατά με το SDK.
- **Συγκρίνετε**: Να δημιουργήσετε δομημένες συγκρίσεις για αποφάσεις επιλογής SLM έναντι μεσαίου μεγέθους LLM.

## Προαπαιτούμενα

- Ολοκληρωμένες οι Συνεδρίες 1 & 2
- Περιβάλλον Python με εγκατεστημένο το `foundry-local-sdk`
- Τουλάχιστον 15GB ελεύθερου χώρου στο δίσκο για πολλαπλές προσωρινές αποθηκεύσεις μοντέλων

### Γρήγορη Εκκίνηση Περιβάλλοντος Πολλαπλών Πλατφορμών

Windows PowerShell:
```powershell
py -m venv .venv
 .\.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install foundry-local-sdk openai numpy
```

macOS / Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install foundry-local-sdk openai numpy
```

Όταν κάνετε benchmarking από macOS σε υπηρεσία host Windows, ορίστε:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```


## Ροή Επίδειξης (30 λεπτά)

### 1. Φόρτωση Μοντέλων Hugging Face μέσω CLI (8 λεπτά)

```powershell
# List catalog entries (filter manually if needed)
foundry model list

# Download a set of comparison targets
foundry model download mistral-7b
foundry model download gemma-2-2b
foundry model download qwen2.5-0.5b

# Verify cache
foundry cache list
```


### 2. Εκτέλεση & Γρήγορη Δοκιμή (5 λεπτά)

```powershell
foundry model run qwen2.5-0.5b
foundry model run qwen2.5-0.5b --prompt "List three benefits of local inference."

foundry model run mistral-7b
foundry model run mistral-7b --prompt "Explain retrieval augmented generation in one paragraph."
```


### 3. Σενάριο Benchmark (8 λεπτά)

Δημιουργήστε το `samples/03-oss-models/benchmark_models.py`:

```python
#!/usr/bin/env python3
"""Lightweight benchmarking for open-source models in Foundry Local.
Metrics: first token latency, total latency, tokens/sec (approx via usage), model size indicator.
Reference SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
"""

import time, statistics, json
from openai import OpenAI

MODELS = [
    "qwen2.5-0.5b",
    "gemma-2-2b",
    "mistral-7b",
]

PROMPT = "Explain the principle of retrieval augmented generation in 2 sentences."
ROUNDS = 3

client = OpenAI(base_url="http://localhost:5273/v1", api_key="not-needed")

def run_round(model: str):
    start = time.time()
    resp = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": PROMPT}],
        max_tokens=150,
        temperature=0.2,
        stream=False
    )
    end = time.time()
    usage = getattr(resp, "usage", None)
    total_tokens = usage.total_tokens if usage else None
    return {
        "latency_sec": end - start,
        "total_tokens": total_tokens,
        "tokens_per_sec": (total_tokens / (end - start)) if (total_tokens and (end-start) > 0) else None,
        "sample_response": resp.choices[0].message.content[:160].replace("\n", " ")
    }

def benchmark_model(model: str):
    results = [run_round(model) for _ in range(ROUNDS)]
    latencies = [r["latency_sec"] for r in results]
    tps = [r["tokens_per_sec"] for r in results if r["tokens_per_sec"]]
    return {
        "model": model,
        "rounds": ROUNDS,
        "latency_avg": statistics.mean(latencies),
        "latency_p95": statistics.quantiles(latencies, n=20)[-1] if len(latencies) > 1 else latencies[0],
        "tokens_per_sec_avg": statistics.mean(tps) if tps else None,
        "sample": results[-1]["sample_response"]
    }

def main():
    summary = [benchmark_model(m) for m in MODELS]
    print(json.dumps(summary, indent=2))
    print("\nInterpretation Tips:\n- latency_avg: lower better\n- tokens_per_sec_avg: higher better\n- Compare quality manually on sample outputs.")

if __name__ == "__main__":
    main()
```

Εκτελέστε:

```powershell
python samples/03-oss-models/benchmark_models.py
```


### 4. Σύγκριση Απόδοσης (5 λεπτά)

Συζητήστε τα trade-offs: χρόνος φόρτωσης, αποτύπωμα μνήμης (παρατηρήστε το Task Manager / `nvidia-smi` / παρακολούθηση πόρων OS), ποιότητα εξόδου έναντι ταχύτητας. Χρησιμοποιήστε το Python benchmark script (Συνεδρία 3) για καθυστέρηση & ρυθμό επεξεργασίας; επαναλάβετε μετά την ενεργοποίηση της επιτάχυνσης GPU.

### 5. Έργο Εκκίνησης (4 λεπτά)

Δημιουργήστε έναν δημιουργό αναφορών σύγκρισης μοντέλων (επεκτείνετε το σενάριο benchmarking με εξαγωγή markdown).

## Έργο Εκκίνησης: Επέκταση `03-huggingface-models`

Βελτιώστε το υπάρχον δείγμα με:

1. Προσθήκη συγκέντρωσης benchmark + εξαγωγή CSV/Markdown.
2. Εφαρμογή απλής ποιοτικής βαθμολόγησης (σετ ερωτήσεων + αρχείο σχολιασμού χειροκίνητης βαθμολόγησης).
3. Εισαγωγή JSON config (`models.json`) για λίστα μοντέλων και σετ ερωτήσεων που μπορούν να προσαρμοστούν.

## Λίστα Ελέγχου Επικύρωσης

```powershell
foundry cache list
foundry model run qwen2.5-0.5b
curl http://localhost:5273/v1/models
```

Όλα τα μοντέλα-στόχοι πρέπει να εμφανίζονται και να ανταποκρίνονται σε ένα αίτημα συνομιλίας δοκιμής.

## Σενάριο Δείγματος & Χαρτογράφηση Εργαστηρίου

| Σενάριο Εργαστηρίου | Σενάριο | Στόχος | Πηγή Ερωτήσεων / Δεδομένων |
|---------------------|---------|--------|---------------------------|
| `samples/session03/benchmark_oss_models.py` / `notebooks/session03_benchmark_oss_models.ipynb` | Ομάδα πλατφόρμας edge που επιλέγει το προεπιλεγμένο SLM για ενσωματωμένο εργαλείο περίληψης | Δημιουργία σύγκρισης καθυστέρησης + p95 + tokens/sec μεταξύ υποψήφιων μοντέλων | Ενσωματωμένη μεταβλητή `PROMPT` + λίστα περιβάλλοντος `BENCH_MODELS` |

### Αφήγηση Σεναρίου

Η ομάδα μηχανικών προϊόντων πρέπει να επιλέξει ένα προεπιλεγμένο ελαφρύ μοντέλο περίληψης για μια offline λειτουργία σημειώσεων συναντήσεων. Εκτελούν ελεγχόμενα ντετερμινιστικά benchmarks (temperature=0) σε ένα σταθερό σετ ερωτήσεων (δείτε το παράδειγμα παρακάτω) και συλλέγουν μετρήσεις καθυστέρησης + ρυθμού επεξεργασίας με και χωρίς επιτάχυνση GPU.

### Παράδειγμα JSON Σετ Ερωτήσεων (επεκτάσιμο)

```json
[
    "Explain the principle of retrieval augmented generation in 2 sentences.",
    "List 3 privacy benefits of local inference.",
    "Summarize why model size impacts latency on consumer hardware.",
    "Provide two scenarios where an SLM is preferable to an LLM."
]
```

Επαναλάβετε κάθε ερώτηση ανά μοντέλο, καταγράψτε την καθυστέρηση ανά ερώτηση για να εξάγετε μετρήσεις κατανομής και να εντοπίσετε αποκλίσεις.

## Πλαίσιο Επιλογής Μοντέλου

| Διάσταση | Μετρική | Γιατί Είναι Σημαντική |
|----------|---------|-----------------------|
| Καθυστέρηση | avg / p95 | Συνέπεια εμπειρίας χρήστη |
| Ρυθμός Επεξεργασίας | tokens/sec | Κλιμακούμενη επεξεργασία παρτίδων & ροών |
| Μνήμη | μέγεθος κατοικίας | Συμβατότητα συσκευής & ταυτόχρονη χρήση |
| Ποιότητα | ερωτήσεις αξιολόγησης | Καταλληλότητα για την εργασία |
| Αποτύπωμα | προσωρινή αποθήκευση δίσκου | Διανομή & ενημερώσεις |
| Άδεια | επιτρεπτότητα χρήσης | Συμμόρφωση με εμπορικούς όρους |

## Επέκταση με Προσαρμοσμένο Μοντέλο

Υψηλού επιπέδου μοτίβο (ψευδοκώδικας):

```python
# pseudo_adapter.py (conceptual)
class CustomModelAdapter:
    def load(self, weights_path: str): ...
    def generate(self, prompt: str, **params) -> str: ...

# Register with local routing (future extensibility point)
```

Συμβουλευτείτε το επίσημο αποθετήριο για εξελισσόμενες διεπαφές προσαρμογέα:
https://github.com/microsoft/Foundry-Local/tree/main/sdk/python

## Αντιμετώπιση Προβλημάτων

| Πρόβλημα | Αιτία | Λύση |
|----------|-------|------|
| OOM στο mistral-7b | Ανεπαρκής RAM/GPU | Σταματήστε άλλα μοντέλα; δοκιμάστε μικρότερη παραλλαγή |
| Αργή πρώτη απόκριση | Ψυχρή φόρτωση | Διατηρήστε ζεστό με περιοδική ελαφριά ερώτηση |
| Καθυστέρηση λήψης | Αστάθεια δικτύου | Επαναλάβετε; προφορτώστε εκτός αιχμής |

## Αναφορές

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- Model Mondays: https://aka.ms/model-mondays
- Ανακάλυψη Μοντέλων Hugging Face: https://huggingface.co/models

---

**Διάρκεια Συνεδρίας**: 30 λεπτά (+ προαιρετική εμβάθυνση)  
**Δυσκολία**: Μεσαία

### Προαιρετικές Βελτιώσεις

| Βελτίωση | Όφελος | Πώς |
|----------|--------|-----|
| Καθυστέρηση Πρώτου Token σε Ροή | Μετρά την αντιληπτή ανταπόκριση | Εκτελέστε benchmark με `BENCH_STREAM=1` (βελτιωμένο σενάριο στο `Workshop/samples/session03`) |
| Ντετερμινιστική Λειτουργία | Σταθερές συγκρίσεις παλινδρόμησης | `temperature=0`, σταθερό σετ ερωτήσεων, καταγραφή εξόδων JSON υπό έλεγχο έκδοσης |
| Βαθμολόγηση Ποιότητας | Προσθέτει ποιοτική διάσταση | Διατηρήστε το `prompts.json` με αναμενόμενες πτυχές; σχολιάστε βαθμολογίες (1–5) χειροκίνητα ή μέσω δευτερεύοντος μοντέλου |
| Εξαγωγή CSV / Markdown | Κοινόχρηστη αναφορά | Επεκτείνετε το σενάριο για να γράψετε `benchmark_report.md` με πίνακα & επισημάνσεις |
| Ετικέτες Δυνατοτήτων Μοντέλου | Βοηθά στην αυτοματοποιημένη δρομολόγηση αργότερα | Διατηρήστε το `models.json` με `{alias: {capabilities:[], size_mb:..}}` |
| Φάση Προθέρμανσης Cache | Μείωση προκατάληψης ψυχρής εκκίνησης | Εκτελέστε έναν γύρο προθέρμανσης πριν από τον βρόχο χρονισμού (ήδη υλοποιημένο) |
| Ακρίβεια Ποσοστού | Ανθεκτική καθυστέρηση ουράς | Χρησιμοποιήστε το numpy percentile (ήδη στο αναδιαμορφωμένο σενάριο) |
| Εκτίμηση Κόστους Token | Οικονομική σύγκριση | Εκτίμηση κόστους = (tokens/sec * avg tokens ανά αίτημα) * ενεργειακή εκτίμηση |
| Αυτόματη Παράκαμψη Αποτυχημένων Μοντέλων | Ανθεκτικότητα σε παρτίδες | Τυλίξτε κάθε benchmark σε try/except και σημειώστε πεδίο κατάστασης |

#### Ελάχιστο Απόσπασμα Εξαγωγής Markdown

```python
with open("benchmark_report.md", "w") as f:
        f.write("|Model|Avg Latency|p95|TPS|\n|---|---|---|---|\n")
        for row in summary:
                f.write(f"|{row['alias']}|{row['latency_avg']:.2f}|{row['latency_p95']:.2f}|{(row.get('tokens_per_sec_avg') or 0):.1f}|\n")
```


#### Παράδειγμα Ντετερμινιστικού Σετ Ερωτήσεων

```json
[
    "Summarize retrieval augmented generation.",
    "List 3 privacy benefits of local inference.",
    "Explain when to choose an SLM over an LLM."
]
```

Επαναλάβετε τη στατική λίστα αντί για τυχαίες ερωτήσεις για συγκρίσιμες μετρήσεις μεταξύ των commits.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Αποποίηση ευθύνης**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία αυτόματης μετάφρασης [Co-op Translator](https://github.com/Azure/co-op-translator). Παρόλο που καταβάλλουμε προσπάθειες για ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτόματες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα θα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή εσφαλμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
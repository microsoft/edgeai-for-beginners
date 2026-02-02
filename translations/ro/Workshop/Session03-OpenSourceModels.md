# Sesiunea 3: Modele Open-Source în Foundry Local

## Rezumat

Descoperiți cum să integrați modelele Hugging Face și alte modele open-source în Foundry Local. Aflați strategii de selecție, fluxuri de lucru pentru contribuțiile comunității, metodologii de comparare a performanței și cum să extindeți Foundry cu înregistrări personalizate de modele. Această sesiune se aliniază temelor săptămânale de explorare "Model Mondays" și vă echipează să evaluați și să operaționalizați modelele open-source local înainte de a le scala pe Azure.

## Obiective de învățare

Până la finalul sesiunii veți putea:

- **Descoperiți & Evaluați**: Identificați modele candidate (mistral, gemma, qwen, deepseek) utilizând compromisuri între calitate și resurse.
- **Încărcați & Rulați**: Utilizați Foundry Local CLI pentru a descărca, cache-ui și lansa modele din comunitate.
- **Evaluați Performanța**: Aplicați euristici consistente pentru latență + debit de tokeni + calitate.
- **Extindeți**: Înregistrați sau adaptați un wrapper personalizat pentru model, urmând modele compatibile cu SDK.
- **Comparați**: Produceți comparații structurate pentru decizii de selecție între SLM și LLM de dimensiuni medii.

## Cerințe preliminare

- Finalizarea sesiunilor 1 și 2
- Mediu Python cu `foundry-local-sdk` instalat
- Cel puțin 15GB spațiu liber pe disc pentru cache-uri multiple de modele

### Ghid rapid pentru medii cross-platform

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
  
Când efectuați benchmarking de pe macOS pe un serviciu gazdă Windows, setați:  
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```
  

## Fluxul demonstrației (30 min)

### 1. Încărcați modele Hugging Face prin CLI (8 min)

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
  

### 2. Rulați & Testați rapid (5 min)

```powershell
foundry model run qwen2.5-0.5b
foundry model run qwen2.5-0.5b --prompt "List three benefits of local inference."

foundry model run mistral-7b
foundry model run mistral-7b --prompt "Explain retrieval augmented generation in one paragraph."
```
  

### 3. Script de Benchmarking (8 min)

Creați `samples/03-oss-models/benchmark_models.py`:  

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
  

Rulați:  

```powershell
python samples/03-oss-models/benchmark_models.py
```
  

### 4. Comparați performanța (5 min)

Discutați compromisurile: timpul de încărcare, consumul de memorie (observați Task Manager / `nvidia-smi` / monitorul de resurse al sistemului de operare), calitatea ieșirii vs viteza. Utilizați scriptul de benchmarking Python (Sesiunea 3) pentru latență și debit; repetați după activarea accelerării GPU.

### 5. Proiect de început (4 min)

Creați un generator de rapoarte de comparație a modelelor (extindeți scriptul de benchmarking cu export în format markdown).

## Proiect de început: Extindeți `03-huggingface-models`

Îmbunătățiți exemplul existent prin:

1. Adăugarea agregării benchmark-urilor + export în format CSV/Markdown.
2. Implementarea unui sistem simplu de scoruri calitative (set de perechi de prompturi + fișier de adnotare manuală).
3. Introducerea unui fișier de configurare JSON (`models.json`) pentru o listă de modele și seturi de prompturi configurabile.

## Lista de verificare pentru validare

```powershell
foundry cache list
foundry model run qwen2.5-0.5b
curl http://localhost:5273/v1/models
```
  
Toate modelele țintă ar trebui să apară și să răspundă la o cerere de chat de test.

## Scenariu exemplu & Mapare workshop

| Script Workshop | Scenariu | Obiectiv | Sursă Prompt / Set de date |
|-----------------|----------|----------|----------------------------|
| `samples/session03/benchmark_oss_models.py` / `notebooks/session03_benchmark_oss_models.ipynb` | Echipa platformei Edge selectează SLM-ul implicit pentru un sumarizator încorporat | Produceți o comparație a latenței + p95 + tokeni/sec pentru modelele candidate | Variabila `PROMPT` inline + lista de mediu `BENCH_MODELS` |

### Narațiunea scenariului

Echipa de inginerie a produsului trebuie să aleagă un model implicit de sumarizare ușoară pentru o funcție offline de notițe de întâlnire. Aceștia efectuează benchmark-uri deterministe controlate (temperature=0) pe un set fix de prompturi (vezi exemplul de mai jos) și colectează metrici de latență + debit cu și fără accelerare GPU.

### Exemplu de set de prompturi JSON (extensibil)

```json
[
    "Explain the principle of retrieval augmented generation in 2 sentences.",
    "List 3 privacy benefits of local inference.",
    "Summarize why model size impacts latency on consumer hardware.",
    "Provide two scenarios where an SLM is preferable to an LLM."
]
```
  
Parcurgeți fiecare prompt pentru fiecare model, capturați latența per prompt pentru a deriva metrici de distribuție și a detecta valorile anormale.

## Cadru pentru selecția modelelor

| Dimensiune | Metrică | De ce contează |
|------------|---------|----------------|
| Latență | medie / p95 | Consistența experienței utilizatorului |
| Debit | tokeni/sec | Scalabilitate pentru loturi și streaming |
| Memorie | dimensiune rezidentă | Compatibilitate cu dispozitivul & concurență |
| Calitate | rubrică de prompturi | Potrivire pentru sarcină |
| Amprentă | cache pe disc | Distribuție & actualizări |
| Licență | permisiuni de utilizare | Conformitate comercială |

## Extinderea cu un model personalizat

Model general (pseudo):  

```python
# pseudo_adapter.py (conceptual)
class CustomModelAdapter:
    def load(self, weights_path: str): ...
    def generate(self, prompt: str, **params) -> str: ...

# Register with local routing (future extensibility point)
```
  

Consultați depozitul oficial pentru interfețe de adaptare în evoluție:  
https://github.com/microsoft/Foundry-Local/tree/main/sdk/python  

## Depanare

| Problemă | Cauză | Soluție |
|----------|-------|---------|
| OOM pe mistral-7b | RAM/GPU insuficient | Opriți alte modele; încercați o variantă mai mică |
| Răspuns lent la prima cerere | Încărcare la rece | Mențineți activ cu un prompt ușor periodic |
| Descărcare blocată | Instabilitate rețea | Reîncercați; predescărcați în afara orelor de vârf |

## Referințe

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python  
- Model Mondays: https://aka.ms/model-mondays  
- Descoperirea modelelor Hugging Face: https://huggingface.co/models  

---

**Durata sesiunii**: 30 min (+ aprofundare opțională)  
**Dificultate**: Intermediar  

### Îmbunătățiri opționale

| Îmbunătățire | Beneficiu | Cum |
|--------------|-----------|-----|
| Latența primului token în streaming | Măsoară receptivitatea percepută | Rulați benchmark-ul cu `BENCH_STREAM=1` (script îmbunătățit în `Workshop/samples/session03`) |
| Mod determinist | Comparări stabile de regresie | `temperature=0`, set fix de prompturi, capturați ieșirile JSON sub controlul versiunilor |
| Scorare rubrică de calitate | Adaugă o dimensiune calitativă | Mențineți `prompts.json` cu fațete așteptate; adnotați scoruri (1–5) manual sau printr-un model secundar |
| Export CSV / Markdown | Raport partajabil | Extindeți scriptul pentru a scrie `benchmark_report.md` cu tabel și evidențieri |
| Etichete de capabilități ale modelului | Ajută la rutarea automată ulterioară | Mențineți `models.json` cu `{alias: {capabilities:[], size_mb:..}}` |
| Fază de încălzire a cache-ului | Reduce părtinirea la pornire la rece | Executați o rundă de încălzire înainte de bucla de cronometrare (deja implementată) |
| Acuratețea percentilă | Latență robustă la coadă | Utilizați percentila numpy (deja în scriptul refăcut) |
| Aproximarea costului pe token | Comparație economică | Cost aprox = (tokeni/sec * medie tokeni per cerere) * euristică energetică |
| Sărirea automată a modelelor eșuate | Reziliență în rulările pe loturi | Încadrați fiecare benchmark în try/except și marcați câmpul de stare |

#### Fragment minim pentru export Markdown

```python
with open("benchmark_report.md", "w") as f:
        f.write("|Model|Avg Latency|p95|TPS|\n|---|---|---|---|\n")
        for row in summary:
                f.write(f"|{row['alias']}|{row['latency_avg']:.2f}|{row['latency_p95']:.2f}|{(row.get('tokens_per_sec_avg') or 0):.1f}|\n")
```
  

#### Exemplu de set de prompturi determinist

```json
[
    "Summarize retrieval augmented generation.",
    "List 3 privacy benefits of local inference.",
    "Explain when to choose an SLM over an LLM."
]
```
  
Parcurgeți lista statică în loc de prompturi aleatorii pentru metrici comparabili între commit-uri.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să asigurăm acuratețea, vă rugăm să fiți conștienți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa maternă ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
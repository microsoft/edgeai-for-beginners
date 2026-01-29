# Sessione 3: Modelli Open-Source in Foundry Local

## Abstract

Scopri come integrare modelli di Hugging Face e altri modelli open-source in Foundry Local. Impara strategie di selezione, flussi di lavoro per il contributo della comunità, metodologie di confronto delle prestazioni e come estendere Foundry con registrazioni di modelli personalizzati. Questa sessione si collega ai temi di esplorazione settimanali "Model Mondays" e ti prepara a valutare e operativizzare modelli open-source localmente prima di scalarli su Azure.

## Obiettivi di Apprendimento

Alla fine sarai in grado di:

- **Scoprire & Valutare**: Identificare modelli candidati (mistral, gemma, qwen, deepseek) utilizzando il compromesso tra qualità e risorse.
- **Caricare & Eseguire**: Usare Foundry Local CLI per scaricare, memorizzare nella cache e avviare modelli della comunità.
- **Benchmark**: Applicare euristiche consistenti per latenza + throughput di token + qualità.
- **Estendere**: Registrare o adattare un wrapper di modello personalizzato seguendo pattern compatibili con l'SDK.
- **Confrontare**: Produrre confronti strutturati per decisioni di selezione tra SLM e LLM di medie dimensioni.

## Prerequisiti

- Completamento delle sessioni 1 e 2
- Ambiente Python con `foundry-local-sdk` installato
- Almeno 15GB di spazio libero su disco per più cache di modelli

### Avvio Rapido Ambiente Cross-Platform

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
  
Quando si esegue il benchmarking da macOS contro un servizio host Windows, impostare:  
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```
  

## Flusso Demo (30 min)

### 1. Caricare Modelli Hugging Face tramite CLI (8 min)

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
  

### 2. Eseguire & Sondare Velocemente (5 min)

```powershell
foundry model run qwen2.5-0.5b
foundry model run qwen2.5-0.5b --prompt "List three benefits of local inference."

foundry model run mistral-7b
foundry model run mistral-7b --prompt "Explain retrieval augmented generation in one paragraph."
```
  

### 3. Script di Benchmark (8 min)

Creare `samples/03-oss-models/benchmark_models.py`:  
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
  
Eseguire:  
```powershell
python samples/03-oss-models/benchmark_models.py
```
  

### 4. Confrontare le Prestazioni (5 min)

Discutere compromessi: tempo di caricamento, utilizzo della memoria (osservare Task Manager / `nvidia-smi` / monitor delle risorse del sistema operativo), qualità dell'output rispetto alla velocità. Utilizzare lo script di benchmark Python (Sessione 3) per latenza e throughput; ripetere dopo aver abilitato l'accelerazione GPU.

### 5. Progetto Iniziale (4 min)

Creare un generatore di report di confronto dei modelli (estendere lo script di benchmarking con esportazione in markdown).

## Progetto Iniziale: Estendere `03-huggingface-models`

Migliorare il campione esistente aggiungendo:

1. Aggregazione dei benchmark + output CSV/Markdown.
2. Implementazione di una semplice valutazione qualitativa (set di prompt + file stub di annotazione manuale).
3. Introduzione di una configurazione JSON (`models.json`) per lista di modelli plug-in e set di prompt.

## Checklist di Validazione

```powershell
foundry cache list
foundry model run qwen2.5-0.5b
curl http://localhost:5273/v1/models
```
  
Tutti i modelli target dovrebbero apparire e rispondere a una richiesta di chat di prova.

## Scenario di Esempio & Mappatura Workshop

| Script del Workshop | Scenario | Obiettivo | Fonte Prompt / Dataset |
|---------------------|----------|-----------|-------------------------|
| `samples/session03/benchmark_oss_models.py` / `notebooks/session03_benchmark_oss_models.ipynb` | Team della piattaforma edge che seleziona SLM predefinito per il riassunto integrato | Produrre un confronto di latenza + p95 + token/sec tra modelli candidati | Variabile `PROMPT` inline + lista `BENCH_MODELS` dell'ambiente |

### Narrazione dello Scenario

Il team di ingegneria del prodotto deve scegliere un modello di riassunto leggero predefinito per una funzione di note di riunione offline. Eseguono benchmark deterministici controllati (temperature=0) su un set di prompt fisso (vedi esempio sotto) e raccolgono metriche di latenza + throughput con e senza accelerazione GPU.

### Esempio di Set di Prompt JSON (espandibile)

```json
[
    "Explain the principle of retrieval augmented generation in 2 sentences.",
    "List 3 privacy benefits of local inference.",
    "Summarize why model size impacts latency on consumer hardware.",
    "Provide two scenarios where an SLM is preferable to an LLM."
]
```
  
Eseguire un ciclo su ogni prompt per modello, catturare la latenza per prompt per derivare metriche di distribuzione e rilevare outlier.

## Framework di Selezione dei Modelli

| Dimensione | Metrica | Perché è Importante |
|------------|---------|---------------------|
| Latenza | media / p95 | Coerenza dell'esperienza utente |
| Throughput | token/sec | Scalabilità batch e streaming |
| Memoria | dimensione residente | Adattamento al dispositivo e concorrenza |
| Qualità | rubric prompts | Idoneità al compito |
| Impronta | cache disco | Distribuzione e aggiornamenti |
| Licenza | permessi d'uso | Conformità commerciale |

## Estensione con Modello Personalizzato

Pattern di alto livello (pseudo):  
```python
# pseudo_adapter.py (conceptual)
class CustomModelAdapter:
    def load(self, weights_path: str): ...
    def generate(self, prompt: str, **params) -> str: ...

# Register with local routing (future extensibility point)
```
  
Consultare il repository ufficiale per interfacce adapter in evoluzione:  
https://github.com/microsoft/Foundry-Local/tree/main/sdk/python  

## Risoluzione dei Problemi

| Problema | Causa | Soluzione |
|----------|-------|-----------|
| OOM su mistral-7b | RAM/GPU insufficiente | Fermare altri modelli; provare variante più piccola |
| Risposta iniziale lenta | Caricamento a freddo | Mantenere caldo con un prompt leggero periodico |
| Download bloccato | Instabilità di rete | Riprova; prefetch durante le ore di minor traffico |

## Riferimenti

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python  
- Model Mondays: https://aka.ms/model-mondays  
- Scoperta Modelli Hugging Face: https://huggingface.co/models  

---

**Durata della Sessione**: 30 min (+ approfondimento opzionale)  
**Difficoltà**: Intermedia  

### Miglioramenti Opzionali

| Miglioramento | Beneficio | Come |
|---------------|-----------|------|
| Latenza del Primo Token in Streaming | Misura la reattività percepita | Eseguire benchmark con `BENCH_STREAM=1` (script migliorato in `Workshop/samples/session03`) |
| Modalità Deterministica | Confronti di regressione stabili | `temperature=0`, set di prompt fisso, catturare output JSON sotto controllo versione |
| Valutazione Rubrica Qualità | Aggiunge una dimensione qualitativa | Mantenere `prompts.json` con aspetti attesi; annotare punteggi (1–5) manualmente o tramite modello secondario |
| Esportazione CSV / Markdown | Report condivisibile | Estendere script per scrivere `benchmark_report.md` con tabella e punti salienti |
| Tag Capacità Modello | Aiuta il routing automatico successivo | Mantenere `models.json` con `{alias: {capabilities:[], size_mb:..}}` |
| Fase di Riscaldamento Cache | Riduce il bias di avvio a freddo | Eseguire un round di riscaldamento prima del ciclo di temporizzazione (già implementato) |
| Accuratezza Percentile | Latenza robusta di coda | Usare percentile numpy (già nello script rifattorizzato) |
| Approssimazione Costo Token | Confronto economico | Costo approssimativo = (token/sec * token medi per richiesta) * euristica energetica |
| Salto Automatico Modelli Falliti | Resilienza nelle esecuzioni batch | Avvolgere ogni benchmark in try/except e contrassegnare il campo di stato |

#### Snippet di Esportazione Markdown Minima

```python
with open("benchmark_report.md", "w") as f:
        f.write("|Model|Avg Latency|p95|TPS|\n|---|---|---|---|\n")
        for row in summary:
                f.write(f"|{row['alias']}|{row['latency_avg']:.2f}|{row['latency_p95']:.2f}|{(row.get('tokens_per_sec_avg') or 0):.1f}|\n")
```
  

#### Esempio di Set di Prompt Deterministico

```json
[
    "Summarize retrieval augmented generation.",
    "List 3 privacy benefits of local inference.",
    "Explain when to choose an SLM over an LLM."
]
```
  
Eseguire il ciclo sulla lista statica invece di prompt casuali per metriche comparabili tra commit.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire l'accuratezza, si prega di notare che le traduzioni automatiche potrebbero contenere errori o imprecisioni. Il documento originale nella sua lingua nativa dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale umana. Non siamo responsabili per eventuali incomprensioni o interpretazioni errate derivanti dall'uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
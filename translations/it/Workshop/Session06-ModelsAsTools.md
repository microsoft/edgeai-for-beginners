# Sessione 6: Foundry Locale – Modelli come Strumenti

## Abstract

Tratta i modelli come strumenti componibili all'interno di un livello operativo AI locale. Questa sessione mostra come collegare più chiamate specializzate SLM/LLM, indirizzare selettivamente i compiti ed esporre un'interfaccia SDK unificata alle applicazioni. Costruirai un instradatore leggero di modelli + planner di compiti, lo integrerai in uno script app e delineerai il percorso di scalabilità verso Azure AI Foundry per carichi di lavoro di produzione.

## Obiettivi di Apprendimento

- **Concettualizzare** i modelli come strumenti atomici con capacità dichiarate
- **Instradare** le richieste basate sull'intento / punteggio euristico
- **Collegare** gli output attraverso compiti multi-step (decomporre → risolvere → perfezionare)
- **Integrare** un'API cliente unificata per applicazioni a valle
- **Scalare** il design sul cloud (stesso contratto compatibile OpenAI)

## Prerequisiti

- Sessioni 1–5 completate
- Molti modelli locali in cache (es. `phi-4-mini`, `deepseek-coder-1.3b`, `qwen2.5-0.5b`)

### Snippet Ambiente Cross-Platform

Windows PowerShell:
```powershell
py -m venv .venv
 .\.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install foundry-local-sdk openai
```

macOS / Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install foundry-local-sdk openai
```

Accesso servizio remoto/VM da macOS:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```

## Flusso Demo (30 min)

### 1. Dichiarazione Capacità Strumento (5 min)

Crea `samples/06-tools/models_catalog.py`:

```python
CATALOG = {
  "phi-4-mini": {
    "capabilities": ["general", "reasoning", "summarize"],
    "priority": 2
  },
  "deepseek-coder-1.3b": {
    "capabilities": ["code", "refactor", "explain_code"],
    "priority": 1
  },
  "qwen2.5-0.5b": {
    "capabilities": ["fast", "classification", "lightweight"],
    "priority": 3
  }
}
```

### 2. Rilevamento Intento & Instradamento (8 min)

Crea `samples/06-tools/router.py`:

```python
#!/usr/bin/env python3
"""Model-as-tool router using Foundry Local OpenAI-compatible endpoint."""
from openai import OpenAI
from models_catalog import CATALOG
import re

client = OpenAI(base_url="http://localhost:5273/v1", api_key="not-needed")

INTENT_RULES = [
  (re.compile(r"code|function|refactor|bug|optimi", re.I), "code"),
  (re.compile(r"summari|abstract|tl;dr", re.I), "summarize"),
  (re.compile(r"classif|label|category", re.I), "classification"),
]

def detect_intent(prompt: str) -> str:
    for pat, intent in INTENT_RULES:
        if pat.search(prompt):
            return intent
    return "general"

def select_model(intent: str) -> str:
    # Catalogo dei punteggi: prima combacia la capacità, poi la priorità
    scored = []
    for name, meta in CATALOG.items():
        caps = meta["capabilities"]
        match = intent in caps
        scored.append((name, match, meta["priority"]))
    # Ordinamento: prima combacia True, poi il valore di priorità più basso
    scored.sort(key=lambda t: (not t[1], t[2]))
    return scored[0][0]

def run(prompt: str):
    intent = detect_intent(prompt)
    model = select_model(intent)
    resp = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=400,
        temperature=0.5
    )
    return {"intent": intent, "model": model, "output": resp.choices[0].message.content}

if __name__ == "__main__":
    tests = [
        "Refactor this Python function for readability",
        "Summarize the importance of local AI governance",
        "Classify this feedback: 'The UI is slow and confusing'"
    ]
    for t in tests:
        r = run(t)
        print(f"Prompt: {t}\nModel: {r['model']} (intent={r['intent']})\nOutput: {r['output'][:160]}...\n")
```

### 3. Collegamento Compiti Multi-Step (7 min)

Crea `samples/06-tools/pipeline.py`:

```python
#!/usr/bin/env python3
"""Multi-step pipeline: plan -> solve -> refine using specialized models."""
from openai import OpenAI
from router import detect_intent, select_model

client = OpenAI(base_url="http://localhost:5273/v1", api_key="not-needed")

def chat(model, content, temp=0.4):
    r = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": content}],
        max_tokens=350,
        temperature=temp
    )
    return r.choices[0].message.content

def pipeline(task: str):
    plan_model = select_model("general")
    plan = chat(plan_model, f"Break the task into 3 ordered steps. Task: {task}")
    steps = [s for s in plan.split('\n') if s.strip()][:3]
    outputs = []
    for step in steps:
        intent = detect_intent(step)
        model = select_model(intent)
        out = chat(model, step)
        outputs.append((step, model, out))
    refine_model = select_model("summarize")
    combined = '\n'.join(o[2] for o in outputs)
    refined = chat(refine_model, f"Condense results into a cohesive answer:\n{combined}")
    return {"plan": plan, "steps": outputs, "final": refined}

if __name__ == '__main__':
    result = pipeline("Generate a refactored version of a slow Python loop and summarize performance gains.")
    print("PLAN:\n", result['plan'])
    print("FINAL:\n", result['final'][:400])
```

### 4. Progetto Starter: Adatta `06-models-as-tools` (5 min)

Miglioramenti:
- Aggiungi supporto token streaming (aggiornamento UI progressivo)
- Aggiungi punteggio di confidenza: sovrapposizione lessicale o rubric prompt
- Esporta trace JSON (intento → modello → latenza → uso token)
- Implementa riuso cache per sub-step ripetuti

### 5. Percorso di Scalabilità verso Azure (5 min)

| Layer | Locale (Foundry) | Cloud (Azure AI Foundry) | Strategia Transizione |
|-------|-----------------|--------------------------|---------------------|
| Instradamento | Python euristico | Microservizio duraturo | Containerizza & distribuisci API |
| Modelli | SLM in cache | Distribuzioni gestite | Mappa nomi locali a ID distribuzione |
| Osservabilità | Statistiche CLI/manuale | Logging centrale & metriche | Aggiungi eventi trace strutturati |
| Sicurezza | Solo host locale | Autenticazione Azure / rete | Introduci key vault per segreti |
| Costo | Risorse dispositivo | Fatturazione a consumo | Aggiungi limiti budget |

## Lista di Controllo Validazione

```powershell
foundry model run phi-4-mini
foundry model run deepseek-coder-1.3b
python samples/06-tools/router.py
python samples/06-tools/pipeline.py
```

Aspettarsi selezione modello basata su intento e output finale raffinato.

## Risoluzione Problemi

| Problema | Causa | Soluzione |
|---------|-------|-----|
| Tutti i compiti instradati allo stesso modello | Regole deboli | Arricchire insieme regex INTENT_RULES |
| Pipeline fallisce a metà passo | Modello mancante caricato | Esegui `foundry model run <model>` |
| Bassa coesione output | Niente fase di perfezionamento | Aggiungi passaggio di sintesi/validazione |

## Riferimenti

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- Documentazione Azure AI Foundry: https://learn.microsoft.com/azure/ai-foundry
- Pattern di Qualità Prompt: Vedi Sessione 2

---

**Durata Sessione**: 30 min  
**Difficoltà**: Esperto

## Scenario Campione & Mappatura Workshop

| Script Workshop / Notebook | Scenario | Obiettivo | Dataset / Fonte Catalogo |
|------------------------------|----------|-----------|---------------------------|
| `samples/session06/models_router.py` / `notebooks/session06_models_router.ipynb` | Assistente sviluppatore che gestisce prompt con intenti misti (rifattorizzare, sintetizzare, classificare) | Instradamento alias modello basato su intento euristico con uso token | `CATALOG` inline + regex `RULES` |
| `samples/session06/models_pipeline.py` / `notebooks/session06_models_pipeline.ipynb` | Pianificazione multi-step e perfezionamento per compito complesso di assistenza al coding | Decomporre → esecuzione specializzata → passaggio di sintesi e perfezionamento | Stesso `CATALOG`; passi derivati dall'output del piano |

### Narrazione Scenario
Uno strumento di produttività ingegneristica riceve compiti eterogenei: rifattorizzare codice, sintetizzare note architettoniche, classificare feedback. Per minimizzare latenza & uso risorse, un modello generale piccolo pianifica e sintetizza, un modello specializzato nel codice gestisce il refactoring, un modello leggero capace di classificazione etichetta il feedback. Lo script pipeline dimostra concatenazione + perfezionamento; lo script router isola instradamenti adattativi a singolo prompt.

### Snapshot Catalogo
```python
CATALOG = {
    "phi-4-mini": {"capabilities": ["general", "summarize"], "priority": 2},
    "deepseek-coder-1.3b": {"capabilities": ["code", "refactor"], "priority": 1},
    "qwen2.5-0.5b": {"capabilities": ["classification", "fast"], "priority": 3}
}
```

### Prompt di Test Esempio
```json
[
    "Refactor this Python function for readability",
    "Summarize the importance of small language models",
    "Classify this feedback: The UI is slow but pretty",
    "Generate a refactored version of a slow Python loop and summarize performance gains."
]
```

### Estensione Trace (Opzionale)
Aggiungi linee JSON trace per passo in `models_pipeline.py`:
```python
trace.append({
    "step": step_idx,
    "intent": intent,
    "alias": alias,
    "latency_ms": round((end-start)*1000,2),
    "tokens": getattr(usage,'total_tokens',None)
})
```

### Euristica Escalation (Idea)
Se il piano contiene parole chiave come "ottimizza", "sicurezza", o la lunghezza passo > 280 caratteri → escalare solo quel passo su un modello più grande (es. `gpt-oss-20b`).

### Miglioramenti Opzionali

| Area | Miglioramento | Valore | Suggerimento |
|------|-------------|-------|------|
| Caching | Riutilizzo manager + oggetti client | Minor latenza, meno overhead | Usa `workshop_utils.get_client` |
| Metriche Uso | Cattura token & latenza per passo | Profilazione & ottimizzazione | Cronometra ogni chiamata instradata; memorizza in lista trace |
| Instradamento Adattativo | Consapevole di confidenza / costo | Miglior compromesso qualità-costo | Aggiungi punteggio: se prompt > N caratteri o regex combacia dominio → escalare a modello più grande |
| Registro Capacità Dinamico | Hot reload catalogo | Nessun riavvio o ridistribuzione | Carica `catalog.json` a runtime; monitora timestamp file |
| Strategia Fallback | Robustezza in caso di errori | Maggior disponibilità | Prova primario → in caso di eccezione usa alias fallback |
| Pipeline Streaming | Feedback precoce | Miglioramento UX | Streamma ogni passo e bufferizza input finale da perfezionare |
| Embedding Vettoriali Intent | Instradamento più fine | Maggior accuratezza intento | Embed prompt, raggruppa & mappa centroide → capacità |
| Esportazione Trace | Catena auditabile | Conformità/Reportistica | Emetti linee JSON: passo, intento, modello, latenza_ms, token |
| Simulazione Costo | Stima pre-cloud | Pianificazione budget | Assegna costo nominale/token per modello & aggrega per compito |
| Modalità Deterministica | Riproducibilità | Benchmark stabile | Env: `temperature=0`, conteggio passi fisso |

#### Esempio Struttura Trace

```python
trace.append({
  "step": idx,
  "intent": intent,
  "alias": alias,
  "latency_ms": round((end-start)*1000,2),
  "tokens": getattr(usage,'total_tokens',None)
})
```

#### Schizzo Escalation Adattativa

```python
if len(prompt) > 280 or 'compliance' in prompt.lower():
    # passare a un modello di ragionamento più ampio se disponibile
    alias = 'gpt-oss-20b'
```

#### Hot Reload Catalogo Modelli

```python
import json, time, os
CATALOG_PATH = 'catalog.json'
last_mtime = 0
def get_catalog():
    global last_mtime, CATALOG
    m = os.path.getmtime(CATALOG_PATH)
    if m != last_mtime:
        CATALOG = json.load(open(CATALOG_PATH))
        last_mtime = m
    return CATALOG
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire la precisione, si prega di notare che le traduzioni automatizzate possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un essere umano. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
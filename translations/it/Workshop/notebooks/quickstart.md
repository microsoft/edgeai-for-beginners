# Workshop Notebooks - Guida Rapida

## Indice

- [Prerequisiti](../../../../Workshop/notebooks)
- [Configurazione Iniziale](../../../../Workshop/notebooks)
- [Sessione 04: Confronto Modelli](../../../../Workshop/notebooks)
- [Sessione 05: Orchestratore Multi-Agente](../../../../Workshop/notebooks)
- [Sessione 06: Routing Basato su Intent](../../../../Workshop/notebooks)
- [Variabili d'Ambiente](../../../../Workshop/notebooks)
- [Comandi Comuni](../../../../Workshop/notebooks)

---

## Prerequisiti

### 1. Installare Foundry Local

**Windows:**
```bash
winget install Microsoft.FoundryLocal
```

**macOS:**
```bash
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**Verifica dell'Installazione:**
```bash
foundry --version
```

### 2. Installare le Dipendenze Python

```bash
cd Workshop
pip install -r requirements.txt
```

Oppure installare singolarmente:
```bash
pip install foundry-local-sdk openai numpy requests
```

---

## Configurazione Iniziale

### Avviare il Servizio Foundry Local

**Necessario prima di eseguire qualsiasi notebook:**

```bash
# Start the service
foundry service start

# Verify it's running
foundry service status
```

Output previsto:
```
✅ Service started successfully
Endpoint: http://localhost:59959
```

### Scaricare e Caricare i Modelli

I notebook utilizzano questi modelli di default:

```bash
# Download models (first time only - may take several minutes)
foundry model download phi-4-mini
foundry model download qwen2.5-3b
foundry model download phi-3.5-mini
foundry model download qwen2.5-0.5b

# Load models into memory
foundry model run phi-4-mini
foundry model run qwen2.5-3b
foundry model run phi-3.5-mini
```

### Verifica della Configurazione

```bash
# List loaded models
foundry model ls

# Check service health
curl http://localhost:59959/v1/models
```

---

## Sessione 04: Confronto Modelli

### Scopo
Confrontare le prestazioni tra Small Language Models (SLM) e Large Language Models (LLM).

### Configurazione Rapida

```bash
# Start service (if not already running)
foundry service start

# Load required models
foundry model run phi-4-mini
foundry model run qwen2.5-3b
```

### Esecuzione del Notebook

1. **Aprire** `session04_model_compare.ipynb` in VS Code o Jupyter
2. **Riavviare il kernel** (Kernel → Restart Kernel)
3. **Eseguire tutte le celle** in ordine

### Configurazione Principale

**Modelli Predefiniti:**
- **SLM:** `phi-4-mini` (~4GB RAM, più veloce)
- **LLM:** `qwen2.5-3b` (~3GB RAM, ottimizzato per la memoria)

**Variabili d'Ambiente (opzionali):**
```python
import os
os.environ['SLM_ALIAS'] = 'phi-4-mini'
os.environ['LLM_ALIAS'] = 'qwen2.5-3b'
os.environ['FOUNDRY_LOCAL_ENDPOINT'] = 'http://localhost:59959/v1'
```

### Output Previsto

```
================================================================================
COMPARISON SUMMARY
================================================================================
Alias                Latency(s)      Tokens     Route               
--------------------------------------------------------------------------------
phi-4-mini           1.234           150        chat.completions    
qwen2.5-3b           2.456           180        chat.completions    
================================================================================

💡 SLM is 1.99x faster than LLM for this prompt
```

### Personalizzazione

**Utilizzare modelli diversi:**
```python
os.environ['SLM_ALIAS'] = 'phi-3.5-mini'
os.environ['LLM_ALIAS'] = 'qwen2.5-1.5b'
```

**Prompt personalizzato:**
```python
os.environ['COMPARE_PROMPT'] = 'Explain quantum computing in simple terms'
```

### Checklist di Validazione

- [ ] La cella 12 mostra i modelli corretti (phi-4-mini, qwen2.5-3b)
- [ ] La cella 12 mostra l'endpoint corretto (porta 59959)
- [ ] La cella 16 diagnostica correttamente (✅ Servizio in esecuzione)
- [ ] La cella 20 pre-flight check supera (entrambi i modelli ok)
- [ ] La cella 22 completa il confronto con valori di latenza
- [ ] La cella 24 validazione mostra 🎉 TUTTI I CONTROLLI SUPERATI!

### Stima del Tempo
- **Prima esecuzione:** 5-10 minuti (incluso il download dei modelli)
- **Esecuzioni successive:** 1-2 minuti

---

## Sessione 05: Orchestratore Multi-Agente

### Scopo
Dimostrare la collaborazione multi-agente utilizzando Foundry Local SDK - gli agenti lavorano insieme per produrre output raffinati.

### Configurazione Rapida

```bash
# Start service
foundry service start

# Load models
foundry model run phi-4-mini  # Primary model
foundry model run qwen2.5-7b  # Optional: higher quality editor
```

### Esecuzione del Notebook

1. **Aprire** `session05_agents_orchestrator.ipynb`
2. **Riavviare il kernel**
3. **Eseguire tutte le celle** in ordine

### Configurazione Principale

**Configurazione Predefinita (Stesso Modello per Entrambi gli Agenti):**
```python
PRIMARY_ALIAS = 'phi-4-mini'
EDITOR_ALIAS = 'phi-4-mini'  # Uses same model
```

**Configurazione Avanzata (Modelli Diversi):**
```python
import os
os.environ['AGENT_MODEL_PRIMARY'] = 'phi-4-mini'     # Fast for research
os.environ['AGENT_MODEL_EDITOR'] = 'qwen2.5-7b'      # High quality for editing
```

### Architettura

```
User Question
    ↓
Researcher Agent (phi-4-mini)
  → Gathers bullet points
    ↓
Editor Agent (phi-4-mini or qwen2.5-7b)
  → Refines into executive summary
    ↓
Final Output
```

### Output Previsto

```
================================================================================
[Pipeline] Question: Explain why edge AI matters for compliance.
================================================================================

[Stage 1: Research]
Output: • Edge AI processes data locally, reducing transmission...

[Stage 2: Editorial Refinement]
Output: Executive Summary: Edge AI enhances compliance by keeping data...

[FINAL OUTPUT]
Executive Summary: Edge AI enhances compliance by keeping sensitive data 
on-premises and reduces latency through local processing.

[METADATA]
Models used: {'researcher': 'phi-4-mini', 'editor': 'phi-4-mini'}
```

### Estensioni

**Aggiungere più agenti:**
```python
critic = Agent(
    name='Critic',
    system='Review content for accuracy',
    client=client,
    model_id=model_id
)
```

**Test in batch:**
```python
test_questions = [
    "What are benefits of local AI?",
    "How does RAG improve accuracy?",
]

for q in test_questions:
    result = pipeline(q, verbose=False)
    print(result['final'])
```

### Stima del Tempo
- **Prima esecuzione:** 3-5 minuti
- **Esecuzioni successive:** 1-2 minuti per domanda

---

## Sessione 06: Routing Basato su Intent

### Scopo
Instradare in modo intelligente i prompt verso modelli specializzati in base all'intent rilevato.

### Configurazione Rapida

```bash
# Start service
foundry service start

# Load all routing models (CPU variants recommended)
foundry model run phi-4-mini-cpu
foundry model run qwen2.5-0.5b-cpu
foundry model run phi-3.5-mini-cpu
```

**Nota:** La Sessione 06 utilizza modelli CPU per massima compatibilità.

### Esecuzione del Notebook

1. **Aprire** `session06_models_router.ipynb`
2. **Riavviare il kernel**
3. **Eseguire tutte le celle** in ordine

### Configurazione Principale

**Catalogo Predefinito (Modelli CPU):**
```python
CATALOG = {
    'phi-4-mini-cpu': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','refactor'],'priority':3},
}
```

**Alternativa (Modelli GPU):**
```python
# Uncomment GPU catalog in Cell #6 if you have sufficient VRAM (8GB+)
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini': {'capabilities':['code','refactor'],'priority':3},
}
```

### Rilevamento Intent

Il router utilizza pattern regex per rilevare l'intent:

| Intent | Esempi di Pattern | Instradato a |
|--------|-------------------|--------------|
| `code` | "refactor", "implement function" | phi-3.5-mini-cpu |
| `classification` | "categorize", "classify this" | qwen2.5-0.5b-cpu |
| `summarize` | "summarize", "tl;dr" | phi-4-mini-cpu |
| `general` | Tutto il resto | phi-4-mini-cpu |

### Output Previsto

```
✓ Using CPU-optimized models (default configuration)
  Models: phi-4-mini-cpu, qwen2.5-0.5b-cpu, phi-3.5-mini-cpu

Routing prompts to specialized models...
============================================================

Prompt: Refactor this Python function for readability
  Intent: code           | Model: phi-3.5-mini-cpu
  Output: Here's a refactored version...
  Tokens: 156

Prompt: Categorize this email as urgent or normal
  Intent: classification | Model: qwen2.5-0.5b-cpu
  Output: Category: Normal
  Tokens: 45

✓ Success! All prompts routed correctly.
```

### Personalizzazione

**Aggiungere intent personalizzati:**
```python
import re

# Add to RULES
RULES.append((re.compile('translate|翻译', re.I), 'translation'))

# Add capability to catalog
CATALOG['phi-4-mini-cpu']['capabilities'].append('translation')
```

**Abilitare il tracciamento dei token:**
```python
import os
os.environ['SHOW_USAGE'] = '1'
```

### Passaggio ai Modelli GPU

Se disponi di 8GB+ di VRAM:

1. Nella **Cella #6**, commenta il catalogo CPU
2. Decommenta il catalogo GPU
3. Carica i modelli GPU:
   ```bash
   foundry model run phi-4-mini
   foundry model run qwen2.5-0.5b
   foundry model run phi-3.5-mini
   ```
4. Riavvia il kernel e riesegui il notebook

### Stima del Tempo
- **Prima esecuzione:** 5-10 minuti (caricamento modelli)
- **Esecuzioni successive:** 30-60 secondi per test

---

## Variabili d'Ambiente

### Configurazione Globale

Impostare prima di avviare Jupyter/VS Code:

**Windows (Prompt dei Comandi):**
```cmd
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:59959/v1
set SHOW_USAGE=1
set RETRY_ON_FAIL=1
```

**Windows (PowerShell):**
```powershell
$env:FOUNDRY_LOCAL_ENDPOINT="http://localhost:59959/v1"
$env:SHOW_USAGE="1"
$env:RETRY_ON_FAIL="1"
```

**macOS/Linux:**
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://localhost:59959/v1
export SHOW_USAGE=1
export RETRY_ON_FAIL=1
```

### Configurazione nel Notebook

Impostare all'inizio di qualsiasi notebook:

```python
import os

# Foundry Local configuration
os.environ['FOUNDRY_LOCAL_ENDPOINT'] = 'http://localhost:59959/v1'

# Model selection
os.environ['SLM_ALIAS'] = 'phi-4-mini'
os.environ['LLM_ALIAS'] = 'qwen2.5-3b'

# Agent models
os.environ['AGENT_MODEL_PRIMARY'] = 'phi-4-mini'
os.environ['AGENT_MODEL_EDITOR'] = 'qwen2.5-7b'

# Debugging
os.environ['SHOW_USAGE'] = '1'       # Show token usage
os.environ['RETRY_ON_FAIL'] = '1'    # Enable retries
os.environ['RETRY_BACKOFF'] = '2.0'  # Retry delay
```

---

## Comandi Comuni

### Gestione del Servizio

```bash
# Start service
foundry service start

# Check status
foundry service status

# Stop service
foundry service stop

# View logs
foundry service logs
```

### Gestione dei Modelli

```bash
# List all available models in catalog
foundry model catalog

# List loaded models
foundry model ls

# Download a model
foundry model download phi-4-mini

# Load a model
foundry model run phi-4-mini

# Unload a model
foundry model unload phi-4-mini

# Remove a model
foundry model remove phi-4-mini

# Get model info
foundry model info phi-4-mini
```

### Test degli Endpoint

```bash
# Check service health
curl http://localhost:59959/health

# List available models via API
curl http://localhost:59959/v1/models

# Test model completion
curl http://localhost:59959/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "phi-4-mini",
    "messages": [{"role":"user","content":"Hello"}],
    "max_tokens": 50
  }'
```

### Comandi Diagnostici

```bash
# Check everything
foundry --version
foundry service status
foundry model ls
foundry device info

# GPU status (NVIDIA)
nvidia-smi

# NPU status (Qualcomm)
foundry device info
```

---

## Migliori Pratiche

### Prima di Iniziare Qualsiasi Notebook

1. **Verificare che il servizio sia in esecuzione:**
   ```bash
   foundry service status
   ```

2. **Verificare che i modelli siano caricati:**
   ```bash
   foundry model ls
   ```

3. **Riavviare il kernel del notebook** se si esegue nuovamente

4. **Cancellare tutti gli output** per un'esecuzione pulita

### Gestione delle Risorse

1. **Utilizzare modelli CPU di default** per compatibilità
2. **Passare ai modelli GPU** solo se si dispone di 8GB+ di VRAM
3. **Chiudere altre applicazioni GPU** prima di eseguire
4. **Mantenere il servizio in esecuzione** tra le sessioni notebook
5. **Monitorare l'utilizzo delle risorse** con Task Manager / nvidia-smi

### Risoluzione dei Problemi

1. **Controllare sempre il servizio prima** di eseguire il debug del codice
2. **Riavviare il kernel** se si notano configurazioni obsolete
3. **Rieseguire le celle diagnostiche** dopo eventuali modifiche
4. **Verificare che i nomi dei modelli** corrispondano a quelli caricati
5. **Controllare che la porta dell'endpoint** corrisponda allo stato del servizio

---

## Riferimento Rapido: Alias Modelli

### Modelli Comuni

| Alias | Dimensione | Ideale per | RAM/VRAM | Varianti |
|-------|------------|------------|----------|----------|
| `phi-4-mini` | ~4B | Chat generali, riassunti | 4-6GB | `-cpu`, `-cuda-gpu`, `-npu` |
| `phi-3.5-mini` | ~3.5B | Generazione codice, refactoring | 3-5GB | `-cpu`, `-cuda-gpu`, `-npu` |
| `qwen2.5-3b` | ~3B | Attività generali, efficiente | 3-4GB | `-cpu`, `-cuda-gpu` |
| `qwen2.5-1.5b` | ~1.5B | Veloce, basso consumo | 2-3GB | `-cpu`, `-cuda-gpu` |
| `qwen2.5-0.5b` | ~0.5B | Classificazione, risorse minime | 1-2GB | `-cpu`, `-cuda-gpu` |

### Nomenclatura delle Varianti

- **Nome base** (es. `phi-4-mini`): Seleziona automaticamente la variante migliore per il tuo hardware
- **`-cpu`**: Ottimizzato per CPU, funziona ovunque
- **`-cuda-gpu`**: Ottimizzato per GPU NVIDIA, richiede 8GB+ di VRAM
- **`-npu`**: Ottimizzato per NPU Qualcomm, richiede driver NPU

**Raccomandazione:** Utilizzare i nomi base (senza suffisso) e lasciare che Foundry Local selezioni automaticamente la variante migliore.

---

## Indicatori di Successo

Sei pronto quando vedi:

✅ `foundry service status` mostra "running"  
✅ `foundry model ls` mostra i modelli richiesti  
✅ Servizio accessibile all'endpoint corretto  
✅ Health check restituisce 200 OK  
✅ Celle diagnostiche del notebook superate  
✅ Nessun errore di connessione nell'output  

---

## Ottenere Aiuto

### Documentazione
- **Repository Principale**: https://github.com/microsoft/Foundry-Local  
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python  
- **Riferimento CLI**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-cli.md  
- **Risoluzione Problemi**: Vedi `troubleshooting.md` in questa directory  

### Problemi su GitHub
- https://github.com/microsoft/Foundry-Local/issues  
- https://github.com/microsoft/edgeai-for-beginners/issues  

---

**Ultimo Aggiornamento:** 8 ottobre 2025  
**Versione:** Workshop Notebooks 2.0  

---

**Clausola di esclusione della responsabilità**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire l'accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un traduttore umano. Non siamo responsabili per eventuali incomprensioni o interpretazioni errate derivanti dall'uso di questa traduzione.
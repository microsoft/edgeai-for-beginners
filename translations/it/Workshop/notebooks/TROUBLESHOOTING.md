# Workshop Notebooks - Guida alla Risoluzione dei Problemi

## Indice

- [Problemi Comuni e Soluzioni](../../../../Workshop/notebooks)
- [Problemi Specifici della Sessione 04](../../../../Workshop/notebooks)
- [Problemi Specifici della Sessione 05](../../../../Workshop/notebooks)
- [Problemi Specifici della Sessione 06](../../../../Workshop/notebooks)
- [Problemi Specifici dell'Hardware](../../../../Workshop/notebooks)
- [Comandi Diagnostici](../../../../Workshop/notebooks)
- [Ottenere Aiuto](../../../../Workshop/notebooks)

---

## Problemi Comuni e Soluzioni

### 🔴 CUDA Out of Memory

**Messaggio di Errore:**
```
CUDA failure 2: out of memory
```

**Causa Principale:** La GPU non ha abbastanza VRAM per caricare il modello.

**Soluzioni:**

#### Opzione 1: Utilizzare Varianti CPU (Consigliato)
```python
# In your notebook, update the CATALOG to use CPU variants
CATALOG = {
    'phi-4-mini-cpu': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','refactor'],'priority':3},
}
```

#### Opzione 2: Utilizzare Modelli più Piccoli sulla GPU
```python
# Use only the smallest model
CATALOG = {
    'qwen2.5-0.5b': {'capabilities':['general','code','summarize','classification'],'priority':1},
}
```

#### Opzione 3: Liberare Memoria GPU
```bash
# Close other GPU-intensive applications
# Check GPU memory usage
nvidia-smi

# Restart Foundry Local service
foundry service stop
foundry service start
```

#### Opzione 4: Aumentare la Memoria GPU (se possibile)
- Chiudere schede del browser, editor video o altre app che utilizzano la GPU
- Ridurre gli effetti visivi di Windows
- Utilizzare la GPU dedicata se si dispone di GPU integrata + dedicata

---

### 🔴 APIConnectionError: Errore di Connessione

**Messaggio di Errore:**
```
APIConnectionError: Connection error
[Retry 1/2] Setup failed for 'phi-4-mini': APIConnectionError: Connection error.
```

**Causa Principale:** Il servizio Foundry Local non è in esecuzione o non è accessibile.

**Soluzioni:**

#### Passo 1: Verificare lo Stato del Servizio
```bash
foundry service status
```

#### Passo 2: Avviare il Servizio se è Fermato
```bash
foundry service start
```

#### Passo 3: Verificare l'Endpoint
```bash
# Check what port the service is using
foundry service status

# Test with curl (adjust port if different)
curl http://localhost:59959/health
curl http://localhost:55769/health
```

#### Passo 4: Caricare i Modelli Necessari
```bash
foundry model run phi-4-mini
foundry model run qwen2.5-3b
foundry model run phi-3.5-mini
```

#### Passo 5: Riavviare il Kernel del Notebook
Dopo aver avviato il servizio e caricato i modelli, riavviare il kernel del notebook e rieseguire tutte le celle.

---

### 🔴 Modello Non Trovato nel Catalogo

**Messaggio di Errore:**
```
ValueError: Model phi-3.5-mini-cpu not found in the catalog.
[ERROR] Model 'phi-4-mini' not found in the catalog
```

**Causa Principale:** Il modello non è stato scaricato o caricato in Foundry Local.

**Soluzioni:**

#### Opzione 1: Scaricare e Caricare i Modelli
```bash
# List available models
foundry model ls

# Download the model if not present
foundry model download phi-4-mini
foundry model download qwen2.5-3b
foundry model download phi-3.5-mini

# Load the model into memory
foundry model run phi-4-mini
foundry model run qwen2.5-3b
foundry model run phi-3.5-mini
```

#### Opzione 2: Utilizzare la Modalità di Selezione Automatica
Aggiornare il CATALOGO per utilizzare i nomi base dei modelli (senza il suffisso `-cpu`):

```python
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini': {'capabilities':['code','refactor'],'priority':3},
}
```

Foundry Local SDK selezionerà automaticamente la variante migliore (CPU, GPU o NPU) per il tuo hardware.

---

### 🔴 HttpResponseError: 500 - Errore nel Caricamento del Modello

**Messaggio di Errore:**
```
HttpResponseError: 500 - Failed loading model
```

**Causa Principale:** Il file del modello è corrotto o incompatibile con l'hardware.

**Soluzioni:**

#### Riscaricare il Modello
```bash
# Remove corrupted model
foundry model remove phi-3.5-mini

# Download fresh copy
foundry model download phi-3.5-mini
```

#### Utilizzare una Variante Differente
```bash
# Try CPU variant instead
foundry model download phi-3.5-mini-cpu
```

---

### 🔴 ImportError: Nessun Modulo Trovato

**Messaggio di Errore:**
```
ModuleNotFoundError: No module named 'foundry_local'
```

**Causa Principale:** Il pacchetto foundry-local-sdk non è installato.

**Soluzioni:**

```bash
# Install SDK
pip install foundry-local-sdk

# Verify installation
pip show foundry-local-sdk
python -c "from foundry_local import FoundryLocalManager; print('SDK OK')"
```

---

### � Prima Richiesta Lenta

**Sintomo:** La prima completamento richiede più di 30 secondi, le richieste successive sono veloci.

**Causa Principale:** Questo comportamento è normale: il servizio sta caricando il modello in memoria alla prima richiesta.

**Soluzioni:**

#### Pre-caricare i Modelli
```bash
# Download and load all models you'll use before running notebooks
foundry model download phi-4-mini
foundry model download qwen2.5-3b
foundry model download phi-3.5-mini

foundry model run phi-4-mini
foundry model run qwen2.5-3b
```

#### Mantenere il Servizio in Esecuzione
```bash
# Start service manually and leave it running
foundry service start
```

---

## Problemi Specifici della Sessione 04

### Configurazione della Porta Errata

**Problema:** Il notebook si connette alla porta sbagliata (55769 vs 59959 vs 57127)

**Soluzione:**

1. Verificare quale porta sta utilizzando Foundry Local:
```bash
foundry service status
# Note the port number displayed
```

2. Aggiornare la Cella 10 nel notebook:
```python
ENDPOINT = os.getenv('FOUNDRY_LOCAL_ENDPOINT', 'http://localhost:59959/v1')
# Replace 59959 with your actual port
```

3. Riavviare il kernel e rieseguire le celle 6, 8, 10, 12, 16, 20, 22

---

### Selezione del Modello Errata

**Problema:** Il notebook mostra gpt-oss-20b o qwen2.5-7b invece di qwen2.5-3b

**Soluzione:**

1. Riavviare il kernel del notebook (per cancellare lo stato delle variabili vecchie)
2. Rieseguire la Cella 10 (Impostare Alias Modello)
3. Rieseguire la Cella 12 (Mostrare Configurazione)
4. **Verificare:** La Cella 12 dovrebbe mostrare `LLM Model: qwen2.5-3b`

---

### Cella Diagnostica Fallisce

**Problema:** La Cella 16 mostra "❌ Foundry Local service not found!"

**Soluzione:**

1. Verificare che il servizio sia in esecuzione:
```bash
foundry service status
```

2. Testare manualmente l'endpoint:
```bash
curl http://localhost:59959/v1/models
```

3. Se curl funziona ma il notebook no:
   - Riavviare il kernel del notebook
   - Rieseguire le celle nell'ordine: 6, 8, 10, 12, 14, 16

4. Se curl fallisce:
   - Avviare il servizio: `foundry service start`
   - Caricare i modelli: `foundry model run phi-4-mini` e `foundry model run qwen2.5-3b`

---

### Controllo Preliminare Fallisce

**Problema:** La Cella 20 mostra errori di connessione anche se la diagnostica è passata

**Soluzione:**

1. Verificare che i modelli siano caricati:
```bash
foundry model ls
# Should show phi-4-mini and qwen2.5-3b
```

2. Se i modelli mancano:
```bash
foundry model run phi-4-mini
foundry model run qwen2.5-3b
```

3. Rieseguire la Cella 20 dopo che i modelli sono stati caricati

---

### Confronto Fallisce con Valori None

**Problema:** La Cella 22 si completa ma mostra la latenza come None

**Soluzione:**

1. Verificare che il controllo preliminare sia passato (Cella 20)
2. Rieseguire la Cella 22 - i modelli potrebbero aver bisogno di essere "riscaldati" alla prima richiesta
3. Verificare che entrambi i modelli siano caricati: `foundry model ls`

---

## Problemi Specifici della Sessione 05

### L'Agente Utilizza il Modello Sbagliato

**Problema:** L'agente non utilizza il modello previsto

**Soluzione:**

Verificare la configurazione:
```python
# Check which models are assigned
print(f"Researcher: {researcher.model_id}")
print(f"Editor: {editor.model_id}")
```

Riavviare il kernel se i modelli sono errati.

---

### Overflow del Contesto di Memoria

**Problema:** Le risposte dell'agente peggiorano nel tempo

**Soluzione:** Già gestito automaticamente - gli agenti mantengono solo gli ultimi 6 messaggi in memoria.

---

## Problemi Specifici della Sessione 06

### Confusione tra Modelli CPU e GPU

**Problema:** Errori CUDA durante l'utilizzo della configurazione predefinita

**Soluzione:** La configurazione predefinita ora utilizza modelli CPU. Se si verificano errori CUDA:

1. Verificare di utilizzare il catalogo CPU predefinito:
```python
# Cell should show CPU variants
CATALOG = {
    'phi-4-mini-cpu': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','refactor'],'priority':3},
}
```

2. Riavviare il kernel e rieseguire tutte le celle

---

### Rilevamento dell'Intento Non Funziona

**Problema:** I prompt vengono indirizzati ai modelli sbagliati

**Soluzione:**

Testare il rilevamento dell'intento:
```python
# Run the intent detection test cell
for prompt in test_prompts:
    intent = detect_intent(prompt)
    print(f"{prompt[:50]}... → {intent}")
```

Aggiornare le REGOLE se i pattern necessitano di modifiche.

---

## Problemi Specifici dell'Hardware

### GPU NVIDIA

**Verificare lo Stato della GPU:**
```bash
nvidia-smi
```

**Problemi Comuni:**
- **Driver obsoleto**: Aggiornare i driver NVIDIA
- **Incompatibilità versione CUDA**: Reinstallare Foundry Local
- **Memoria GPU frammentata**: Riavviare il sistema

### NPU Qualcomm

**Verificare lo Stato della NPU:**
```bash
foundry device info
```

**Problemi Comuni:**
- **Driver NPU non installati**: Installare i driver Qualcomm NPU
- **Variante NPU non disponibile**: Utilizzare la variante CPU
- **Versione di Windows troppo vecchia**: Aggiornare all'ultima versione di Windows 11

### Sistemi Solo CPU

**Modelli Consigliati:**
```python
CATALOG = {
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','general'],'priority':2},
}
```

**Suggerimenti per le Prestazioni:**
- Utilizzare modelli più piccoli
- Ridurre max_tokens
- Avere pazienza per la prima richiesta

---

## Comandi Diagnostici

### Verificare Tutto
```bash
# Service status
foundry service status

# List models
foundry model ls

# Device info
foundry device info

# Version info
foundry --version

# Health check
curl http://localhost:55769/health
```

### In Python
```python
# Check SDK import
try:
    from foundry_local import FoundryLocalManager
    print('✓ SDK imported')
except ImportError as e:
    print(f'✗ SDK import failed: {e}')

# Check service connectivity
from openai import OpenAI

try:
    client = OpenAI(base_url='http://localhost:59959/v1', api_key='test')
    models = client.models.list()
    print(f'✓ Service reachable, {len(list(models.data))} models available')
except Exception as e:
    print(f'✗ Service not reachable: {e}')
```

---

## Ottenere Aiuto

### 1. Controllare i Log
```bash
# Windows
foundry service logs

# Or check Windows Event Viewer
# Application Logs -> Microsoft-FoundryLocal
```

### 2. Problemi su GitHub
- Cercare problemi esistenti: https://github.com/microsoft/Foundry-Local/issues
- Creare un nuovo problema includendo:
  - Messaggio di errore (testo completo)
  - Output di `foundry service status`
  - Output di `foundry --version`
  - Informazioni su GPU/NPU (nvidia-smi, ecc.)
  - Passaggi per riprodurre il problema

### 3. Documentazione
- **Repository Principale**: https://github.com/microsoft/Foundry-Local
- **SDK Python**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **Riferimento CLI**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-cli.md
- **Risoluzione dei Problemi**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-troubleshooting.md

---

## Checklist per Soluzioni Rapide

Quando qualcosa va storto, prova questi passaggi in ordine:

- [ ] Verificare che il servizio sia in esecuzione: `foundry service status`
- [ ] Riavviare il servizio: `foundry service stop && foundry service start`
- [ ] Verificare che il modello esista: `foundry model ls | grep phi-4-mini`
- [ ] Caricare i modelli richiesti: `foundry model run phi-4-mini`
- [ ] Controllare la memoria GPU: `nvidia-smi` (se NVIDIA)
- [ ] Provare la variante CPU: Utilizzare `phi-4-mini-cpu` invece di `phi-4-mini`
- [ ] Riavviare il kernel del notebook
- [ ] Cancellare gli output del notebook e rieseguire tutte le celle
- [ ] Reinstallare l'SDK: `pip install --upgrade --force-reinstall foundry-local-sdk`
- [ ] Riavviare il sistema (ultima risorsa)

---

## Suggerimenti per la Prevenzione

### Migliori Pratiche

1. **Controllare sempre il servizio prima:**
   ```bash
   foundry service status
   ```

2. **Utilizzare varianti CPU di default:**
   ```python
   CATALOG = {
       'phi-4-mini-cpu': {...},
       'qwen2.5-0.5b-cpu': {...},
   }
   ```

3. **Pre-caricare i modelli prima di eseguire i notebook:**
   ```bash
   foundry model run phi-4-mini
   foundry model run qwen2.5-3b
   ```

4. **Mantenere il servizio in esecuzione:**
   - Non fermare/avviare il servizio inutilmente
   - Lasciarlo in esecuzione in background tra le sessioni

5. **Monitorare le risorse:**
   - Controllare la memoria GPU prima di eseguire
   - Chiudere applicazioni GPU non necessarie
   - Utilizzare Task Manager / nvidia-smi

6. **Aggiornare regolarmente:**
   ```bash
   winget upgrade Microsoft.FoundryLocal
   pip install --upgrade foundry-local-sdk
   ```

---

**Ultimo Aggiornamento:** 8 ottobre 2025

---

**Disclaimer (Avvertenza)**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire l'accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale umana. Non siamo responsabili per eventuali incomprensioni o interpretazioni errate derivanti dall'uso di questa traduzione.
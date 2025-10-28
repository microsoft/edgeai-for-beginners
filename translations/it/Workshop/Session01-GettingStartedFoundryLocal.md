<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0ab7d0dee137f224a011d9db00f0d2a2",
  "translation_date": "2025-10-28T17:19:45+00:00",
  "source_file": "Workshop/Session01-GettingStartedFoundryLocal.md",
  "language_code": "it"
}
-->
# Sessione 1: Introduzione a Foundry Local

## Abstract

Inizia il tuo percorso con Foundry Local installandolo e configurandolo su Windows 11. Scopri come configurare la CLI, abilitare l'accelerazione hardware e memorizzare i modelli nella cache per un'inferenza locale rapida. Questa sessione pratica ti guiderà nell'esecuzione di modelli come Phi, Qwen, DeepSeek e GPT-OSS-20B utilizzando comandi CLI riproducibili.

## Obiettivi di Apprendimento

Alla fine di questa sessione, sarai in grado di:

- **Installare e Configurare**: Configurare Foundry Local su Windows 11 con impostazioni di prestazioni ottimali
- **Padroneggiare le Operazioni CLI**: Utilizzare la CLI di Foundry Local per la gestione e il deployment dei modelli
- **Abilitare l'Accelerazione Hardware**: Configurare l'accelerazione GPU con ONNXRuntime o WebGPU
- **Distribuire Modelli Multipli**: Eseguire i modelli phi-4, GPT-OSS-20B, Qwen e DeepSeek localmente
- **Creare la tua Prima App**: Adattare esempi esistenti per utilizzare il Foundry Local Python SDK

# Test del modello (prompt singolo non interattivo)
foundry model run phi-4-mini --prompt "Ciao, presentati"

- Windows 11 (22H2 o successivo)
# Elenco dei modelli disponibili nel catalogo (i modelli caricati appaiono dopo l'esecuzione)
foundry model list
## NOTE: Attualmente non esiste un flag dedicato `--running`; per vedere quali sono caricati, avvia una chat o ispeziona i log del servizio.
- Python 3.10+ installato
- Visual Studio Code con estensione Python
- Privilegi di amministratore per l'installazione

### (Opzionale) Variabili d'Ambiente

Crea un file `.env` (o impostalo nella shell) per rendere gli script portabili:
# Confronta le risposte (non interattivo)
foundry model run gpt-oss-20b --prompt "Spiega l'edge AI in termini semplici"
| Variabile | Scopo | Esempio |
|-----------|-------|---------|
| `FOUNDRY_LOCAL_ALIAS` | Alias preferito del modello (il catalogo seleziona automaticamente la variante migliore) | `phi-3.5-mini` |
| `FOUNDRY_LOCAL_ENDPOINT` | Sovrascrive l'endpoint (altrimenti auto dal manager) | `http://localhost:5273/v1` |
| `FOUNDRY_LOCAL_STREAM` | Abilita la demo di streaming | `true` |

> Se `FOUNDRY_LOCAL_ENDPOINT=auto` (o non impostato), lo deriviamo dal manager SDK.

## Flusso Demo (30 minuti)

### 1. Installare Foundry Local e Verificare la Configurazione CLI (10 minuti)

# Elenco dei modelli memorizzati nella cache
foundry cache list

```powershell
# Install via winget (recommended)
winget install Microsoft.FoundryLocal

# Or download from Microsoft Learn
# https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install
```

**macOS (Anteprima / Se Supportato)**

Se è disponibile un pacchetto nativo per macOS (controlla la documentazione ufficiale per le ultime novità):

```bash
# Homebrew (if/when available)
brew update
brew install foundry-local  # hypothetical formula name

# Or manual download (tarball)
curl -L -o foundry-local.tar.gz "https://download.microsoft.com/foundry-local/latest/macos/foundry-local.tar.gz"
tar -xzf foundry-local.tar.gz
sudo ./install.sh
```

Se i binari nativi per macOS non sono ancora disponibili, puoi comunque: 
1. Utilizzare una VM Windows 11 ARM/Intel (Parallels / UTM) e seguire i passaggi per Windows. 
2. Eseguire i modelli tramite container (se l'immagine del container è pubblicata) e impostare `FOUNDRY_LOCAL_ENDPOINT` sulla porta esposta. 

**Creare un Ambiente Virtuale Python (Cross‑Platform)**

Windows PowerShell:
```powershell
py -m venv .venv
 .\.venv\Scripts\Activate.ps1
```

macOS / Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

Aggiorna pip e installa le dipendenze principali:
```bash
python -m pip install --upgrade pip
pip install foundry-local-sdk openai
```

#### Passo 1.2: Verificare l'Installazione

```powershell
# Check version
foundry --version

# Initialize configuration
foundry init

# View available commands
foundry --help
```

#### Passo 1.3: Configurare l'Ambiente

```powershell
# Set up Python environment for Module08
cd Module08
py -m venv .venv
.\.venv\Scripts\activate

# Install Foundry Local Python SDK and dependencies
pip install foundry-local-sdk openai requests
```

### Bootstrapping SDK (Consigliato)

Invece di avviare manualmente il servizio e eseguire i modelli, il **Foundry Local Python SDK** può avviare tutto automaticamente:

```python
from foundry_local import FoundryLocalManager
from openai import OpenAI
import os

alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-3.5-mini")

# Bootstraps service + downloads + loads most suitable variant for hardware
manager = FoundryLocalManager(alias)

print("Service running:", manager.is_service_running())
print("Endpoint:", manager.endpoint)
print("Cached models:", manager.list_cached_models())

client = OpenAI(base_url=manager.endpoint, api_key=manager.api_key or "not-needed")

resp = client.chat.completions.create(
    model=manager.get_model_info(alias).id,
    messages=[
        {"role": "system", "content": "You are a helpful local assistant."},
        {"role": "user", "content": "Hello"}
    ],
    max_tokens=120,
    temperature=0.5
)
print(resp.choices[0].message.content)
```

Se preferisci un controllo esplicito, puoi comunque utilizzare la CLI + client OpenAI come mostrato in seguito.

### 2. Eseguire Modelli Localmente tramite CLI (10 minuti)

#### Passo 3.1: Distribuire il Modello Phi-4

```powershell
# Download and run phi-4-mini
foundry model run phi-4-mini

# Test the model (one-shot prompt)
foundry model run phi-4-mini --prompt "Hello, introduce yourself"

# NOTE: There is no `--running` flag; use `foundry model list` and recent activity to infer loaded models.
```

#### Passo 3.2: Distribuire GPT-OSS-20B

```powershell
# Download and run GPT-OSS-20B
foundry model run gpt-oss-20b

# Compare responses (one-shot prompt)
foundry model run gpt-oss-20b --prompt "Explain edge AI in simple terms"
```

#### Passo 3.3: Caricare Modelli Aggiuntivi

```powershell
# Download Qwen model family
foundry model download qwen2.5-0.5b
foundry model download qwen2.5-7b

# Download DeepSeek models
foundry model download deepseek-coder-1.3b

# List cached models
foundry cache list
```

### 4. Progetto Iniziale: Adattare 01-run-phi per Foundry Local (5 minuti)

#### Passo 4.1: Creare un'Applicazione di Chat di Base

Crea `samples/01-foundry-quickstart/chat_quickstart.py` (aggiornato per utilizzare il manager se disponibile):

```python
#!/usr/bin/env python3
"""
Foundry Local Chat Quickstart
Demo: Basic chat interaction using Foundry Local Python SDK
Reference: https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/reference/reference-sdk?pivots=programming-language-python
"""

import os, sys
from openai import OpenAI
try:
    from foundry_local import FoundryLocalManager  # control-plane SDK
except ImportError:
    FoundryLocalManager = None

def main():
    """Main chat function using Foundry Local SDK"""
    
    # Preferred: bootstrap via SDK manager (auto start + download + load)
    alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-3.5-mini")
    if FoundryLocalManager:
        manager = FoundryLocalManager(alias)
        endpoint = manager.endpoint
        model_id = manager.get_model_info(alias).id
        api_key = manager.api_key or "not-needed"
    else:
        # Fallback: assume default endpoint & alias already running via CLI
        endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT", "http://localhost:5273/v1")
        model_id = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-4-mini")
        api_key = "not-needed"

    client = OpenAI(base_url=endpoint, api_key=api_key)
    
    # Get user input
    if len(sys.argv) > 1:
        user_message = " ".join(sys.argv[1:])
    else:
        user_message = input("Enter your message: ")
    
    try:
        # Make chat completion request
        response = client.chat.completions.create(
            model=model_id,
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant powered by Microsoft Foundry Local."},
                {"role": "user", "content": user_message}
            ],
            max_tokens=500,
            temperature=0.7
        )
        
        # Display response
        print(f"\nModel: {response.model}")
        print(f"Response: {response.choices[0].message.content}")
        print(f"Tokens used: {response.usage.total_tokens if response.usage else 'N/A'}")
        
    except Exception as e:
        print(f"Error: {e}")
        print("\nTroubleshooting:")
    print("1. Ensure Foundry Local is running: foundry status")
    print("2. List models: foundry model list")
    print(f"3. Start model if needed: foundry model run {model_id}")
    print("4. Or let SDK bootstrap: pip install foundry-local-sdk")

if __name__ == "__main__":
    main()
```

#### Passo 4.2: Testare l'Applicazione

```powershell
# Ensure phi-4-mini is running
foundry model run phi-4-mini

# Run the quickstart app
python samples/01-foundry-quickstart/chat_quickstart.py "What is Microsoft Foundry Local?"

# Try interactive mode
python samples/01-foundry-quickstart/chat_quickstart.py
```

## Concetti Chiave Trattati

### 1. Architettura di Foundry Local

- **Motore di Inferenza Locale**: Esegue i modelli interamente sul tuo dispositivo
- **Compatibilità SDK OpenAI**: Integrazione senza problemi con il codice OpenAI esistente
- **Gestione dei Modelli**: Scarica, memorizza nella cache ed esegui più modelli in modo efficiente
- **Ottimizzazione Hardware**: Sfrutta l'accelerazione GPU, NPU e CPU

### 2. Riferimento ai Comandi CLI

```powershell
# Core Commands
foundry --version              # Check installation
# Model Management
foundry model list             # List available models
foundry model unload <name>    # Unload from memory

foundry config list            # Current configuration
```

### 3. Integrazione SDK Python

```python
# Basic client setup
from foundry_local import FoundryLocalManager
from openai import OpenAI
import os

alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-3.5-mini")
manager = FoundryLocalManager(alias)
client = OpenAI(base_url=manager.endpoint, api_key=manager.api_key or "not-needed")

response = client.chat.completions.create(
    model=manager.get_model_info(alias).id,
    messages=[{"role": "user", "content": "Hello!"}],
    max_tokens=50
)
print(response.choices[0].message.content)

# Streaming example
stream = client.chat.completions.create(
    model=manager.get_model_info(alias).id,
    messages=[{"role": "user", "content": "Give a 1-sentence definition of edge AI."}],
    stream=True,
    max_tokens=60,
    temperature=0.4
)
for chunk in stream:
    delta = chunk.choices[0].delta
    if delta and delta.content:
        print(delta.content, end="", flush=True)
print()
```

## Risoluzione dei Problemi Comuni

### Problema 1: "Comando Foundry non trovato"

**Soluzione:**
```powershell
# Restart PowerShell after installation
# Or manually add to PATH
$env:PATH += ";C:\Program Files\Microsoft\FoundryLocal"
```

### Problema 2: "Caricamento del modello fallito"

**Soluzione:**
```powershell
# Check available memory
foundry system info

# Try smaller model first
foundry model run phi-4-mini

# Check disk space for model cache
dir "$env:USERPROFILE\.foundry\models"
```

### Problema 3: "Connessione rifiutata su localhost:5273"

**Soluzione:**
```powershell
# Check if service is running
foundry status

# Start service if needed
foundry service start

# Check for port conflicts
netstat -an | findstr 5273
```

## Consigli per l'Ottimizzazione delle Prestazioni

### 1. Strategia di Selezione del Modello

- **Phi-4-mini**: Ideale per compiti generali, utilizzo di memoria ridotto
- **Qwen2.5-0.5b**: Inferenza più veloce, risorse minime
- **GPT-OSS-20B**: Qualità più alta, richiede più risorse
- **DeepSeek-Coder**: Ottimizzato per compiti di programmazione

### 2. Ottimizzazione Hardware

```powershell
# Enable all acceleration options
foundry config set compute.onnx.enable_gpu true
foundry config set compute.webgpu.enabled true
foundry config set compute.cpu.threads auto

# Optimize memory usage
foundry config set model.cache.max_size 10GB
foundry config set model.preload false
```

### 3. Monitoraggio delle Prestazioni

```powershell
# Performance & latency measurement
# Use the Python benchmark script (Session 3) instead of legacy 'model stats' or 'model benchmark' commands.
# Example:
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
python Workshop\samples\session03\benchmark_oss_models.py

# Re-run after enabling GPU acceleration to compare:
foundry config set compute.onnx.enable_gpu true
python Workshop\samples\session03\benchmark_oss_models.py
```

### Miglioramenti Opzionali

| Miglioramento | Cosa | Come |
|---------------|------|------|
| Utilità Condivise | Rimuovi logica duplicata client/bootstrap | Usa `Workshop/samples/workshop_utils.py` (`get_client`, `chat_once`) |
| Visibilità sull'Uso dei Token | Insegna il pensiero su costi/efficienza | Imposta `SHOW_USAGE=1` per stampare prompt/completion/token totali |
| Confronti Deterministici | Benchmarking stabile e controlli di regressione | Usa `temperature=0`, `top_p=1`, testo del prompt coerente |
| Latenza del Primo Token | Metrica di reattività percepita | Adatta script di benchmark con streaming (`BENCH_STREAM=1`) |
| Retry su Errori Transitori | Demo resilienti al primo avvio | `RETRY_ON_FAIL=1` (default) & regola `RETRY_BACKOFF` |
| Test di Fumo | Controllo rapido su flussi chiave | Esegui `python Workshop/tests/smoke.py` prima di un workshop |
| Profili Alias Modello | Cambia rapidamente set di modelli tra macchine | Mantieni `.env` con `FOUNDRY_LOCAL_ALIAS`, `SLM_ALIAS`, `LLM_ALIAS` |
| Efficienza della Cache | Evita ripetuti warmup in esecuzioni multi-sample | Utilità cache manager; riutilizza tra script/notebook |
| Warmup al Primo Avvio | Riduci picchi di latenza p95 | Esegui un prompt minimo dopo la creazione di `FoundryLocalManager` |

Esempio di baseline deterministico caldo (PowerShell):

```powershell
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
python Workshop\samples\session01\chat_bootstrap.py "List two privacy benefits of local inference." | Out-Null
python Workshop\samples\session01\chat_bootstrap.py "List two privacy benefits of local inference."
```

Dovresti vedere output simile e conteggi di token identici alla seconda esecuzione, confermando la determinazione.

## Prossimi Passi

Dopo aver completato questa sessione:

1. **Esplora la Sessione 2**: Crea soluzioni AI con Azure AI Foundry RAG
2. **Prova Modelli Diversi**: Sperimenta con Qwen, DeepSeek e altre famiglie di modelli
3. **Ottimizza le Prestazioni**: Affina le impostazioni per il tuo hardware specifico
4. **Crea Applicazioni Personalizzate**: Usa il Foundry Local SDK nei tuoi progetti

## Risorse Aggiuntive

### Documentazione
- [Riferimento SDK Python di Foundry Local](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/reference/reference-sdk?pivots=programming-language-python)
- [Guida all'Installazione di Foundry Local](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install)
- [Catalogo Modelli](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/models)

### Codice di Esempio
- [Modulo08 Esempio 01](./samples/01/README.md) - Quickstart Chat REST
- [Modulo08 Esempio 02](./samples/02/README.md) - Integrazione SDK OpenAI
- [Modulo08 Esempio 03](./samples/03/README.md) - Scoperta e Benchmarking Modelli

### Community
- [Discussioni su Foundry Local GitHub](https://github.com/microsoft/Foundry-Local/discussions)
- [Community Azure AI](https://techcommunity.microsoft.com/category/artificialintelligence)

---

**Durata della Sessione**: 30 minuti di pratica + 15 minuti di Q&A
**Livello di Difficoltà**: Principiante
**Prerequisiti**: Windows 11, Python 3.10+, Accesso da amministratore

## Scenario di Esempio e Mappatura Workshop

| Script / Notebook del Workshop | Scenario | Obiettivo | Input di Esempio | Dataset Necessario |
|--------------------------------|----------|-----------|------------------|--------------------|
| `samples/session01/chat_bootstrap.py` / `notebooks/session01_chat_bootstrap.ipynb` | Team IT interno che valuta l'inferenza on‑device per un portale di valutazione della privacy | Dimostrare che SLM locale risponde con latenza sub‑secondo su prompt standard | "Elenca due vantaggi dell'inferenza locale." | Nessuno (prompt singolo) |
| Codice di adattamento quickstart | Sviluppatore che migra uno script OpenAI esistente a Foundry Local | Mostrare compatibilità immediata | "Dai due vantaggi dell'inferenza locale." | Solo prompt inline |

### Narrazione dello Scenario
Il team sicurezza e conformità deve validare se i dati sensibili del prototipo possono essere elaborati localmente. Eseguono lo script bootstrap con diversi prompt (privacy, latenza, costo) utilizzando una modalità deterministica temperature=0 per catturare output di base per confronti futuri (benchmarking Sessione 3 e contrasto SLM vs LLM Sessione 4).

### Set di Prompt Minimi JSON (opzionale)
```json
[
    "List two benefits of local inference.",
    "Summarize why keeping data on device improves privacy.",
    "Give one trade‑off when choosing an SLM over a large model."
]
```

Usa questa lista per creare un ciclo di valutazione riproducibile o per avviare un futuro test di regressione.

---

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire l'accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale umana. Non siamo responsabili per eventuali incomprensioni o interpretazioni errate derivanti dall'uso di questa traduzione.
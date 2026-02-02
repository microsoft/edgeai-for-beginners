# Sessione 1: Introduzione a Foundry Local

## Abstract

Impara a installare, configurare e utilizzare i tuoi primi modelli di intelligenza artificiale con Microsoft Foundry Local. Questa sessione pratica offre un'introduzione passo-passo all'inferenza locale, dall'installazione alla creazione della tua prima applicazione di chat utilizzando modelli come Phi-4, Qwen e DeepSeek.

## Obiettivi di apprendimento

Alla fine di questa sessione, sarai in grado di:

- **Installare e configurare**: Configurare Foundry Local con verifica dell'installazione corretta
- **Gestire operazioni CLI**: Utilizzare il CLI di Foundry Local per la gestione e il deployment dei modelli
- **Eseguire il tuo primo modello**: Distribuire e interagire con un modello AI locale
- **Creare un'app di chat**: Realizzare una semplice applicazione di chat utilizzando il Foundry Local Python SDK
- **Comprendere l'AI locale**: Apprendere i fondamenti dell'inferenza locale e della gestione dei modelli

## Prerequisiti

### Requisiti di sistema

- **Windows**: Windows 11 (22H2 o successivo) O **macOS**: macOS 11+ (supporto limitato)
- **RAM**: Minimo 8GB, consigliati 16GB+
- **Spazio di archiviazione**: Almeno 10GB liberi per i modelli
- **Python**: Versione 3.10 o successiva installata
- **Accesso amministrativo**: Privilegi di amministratore per l'installazione

### Ambiente di sviluppo

- Visual Studio Code con estensione Python (consigliato)
- Accesso alla riga di comando (PowerShell su Windows, Terminale su macOS)
- Git per clonare repository (opzionale)

## Flusso del workshop (30 minuti)

### Passo 1: Installare Foundry Local (5 minuti)

#### Installazione su Windows

Installa Foundry Local utilizzando il gestore di pacchetti di Windows:

```powershell
# Install via winget (recommended)
winget install Microsoft.FoundryLocal
```

Alternativa: Scarica direttamente da [Microsoft Learn](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install)

#### Installazione su macOS (Supporto limitato)

> [!NOTE] 
> Il supporto per macOS è attualmente in anteprima. Consulta la documentazione ufficiale per le ultime novità.

Se disponibile, installa utilizzando Homebrew:

```bash
# If Homebrew formula is available
brew update
brew install foundry-local

# Or manual download (check official docs for latest)
curl -L -o foundry-local.tar.gz "https://download.microsoft.com/foundry-local/latest/macos/foundry-local.tar.gz"
tar -xzf foundry-local.tar.gz
sudo ./install.sh
```

**Alternativa per utenti macOS:**
- Usa una VM Windows 11 (Parallels/UTM) e segui i passaggi per Windows
- Esegui tramite container, se disponibile, e configura `FOUNDRY_LOCAL_ENDPOINT`

### Passo 2: Verifica dell'installazione (3 minuti)

Dopo l'installazione, riavvia il terminale e verifica che Foundry Local funzioni:

```powershell
# Check if Foundry Local is installed correctly
foundry --version

# View available commands
foundry --help
```

L'output previsto dovrebbe mostrare informazioni sulla versione e i comandi disponibili.

### Passo 3: Configurare l'ambiente Python (5 minuti)

Crea un ambiente Python dedicato per questo workshop:

**Windows:**
```powershell
# Create virtual environment
py -m venv .venv

# Activate environment
.\.venv\Scripts\Activate.ps1

# Upgrade pip and install dependencies
python -m pip install --upgrade pip
pip install foundry-local-sdk openai
```

**macOS/Linux:**
```bash
# Create virtual environment
python3 -m venv .venv

# Activate environment
source .venv/bin/activate

# Upgrade pip and install dependencies
python -m pip install --upgrade pip
pip install foundry-local-sdk openai
```

### Passo 4: Eseguire il tuo primo modello (7 minuti)

Ora eseguiamo il nostro primo modello AI localmente!

#### Inizia con Phi-4 Mini (Modello consigliato)

```powershell
# Download and start phi-4-mini (lightweight, fast)
foundry model run phi-4-mini

# Test the model with a simple prompt
foundry model run phi-4-mini --prompt "Hello, introduce yourself in one sentence"
```

> [!TIP]
> Questo comando scarica il modello (la prima volta) e avvia automaticamente il servizio Foundry Local.

#### Controlla cosa è in esecuzione

```powershell
# List available models (shows downloaded models)
foundry model list

# Check service status
foundry service status

# See what models are cached locally
foundry cache list
```

#### Prova altri modelli

Una volta che phi-4-mini è funzionante, sperimenta con altri modelli:

```powershell
# Larger model with better capabilities
foundry model run gpt-oss-20b --prompt "Explain edge AI in simple terms"

# Fast, efficient model
foundry model run qwen2.5-0.5b --prompt "What are the benefits of local AI inference?"
```

### Passo 5: Crea la tua prima applicazione di chat (10 minuti)

Ora creiamo un'applicazione Python che utilizza i modelli appena avviati.

#### Crea lo script di chat

Crea un nuovo file chiamato `my_first_chat.py` (o usa il campione fornito):

```python
#!/usr/bin/env python3
"""
My First Foundry Local Chat Application
Using FoundryLocalManager for automatic service management
"""

import os
from foundry_local import FoundryLocalManager
from openai import OpenAI

def main():
    # Get model alias from environment or use default
    alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-4-mini")
    
    try:
        # Initialize Foundry Local Manager (auto-starts service, downloads model)
        manager = FoundryLocalManager(alias)
        
        # Create OpenAI client pointing to local endpoint
        client = OpenAI(
            base_url=manager.endpoint,
            api_key=manager.api_key or "not-needed"
        )
        
        # Get the actual model ID for this alias
        model_id = manager.get_model_info(alias).id
        
        print("🤖 Welcome to your first local AI chat!")
        print(f"� Using model: {alias} -> {model_id}")
        print(f"🌐 Endpoint: {manager.endpoint}")
        print("�💡 Type 'quit' to exit\n")
        
    except Exception as e:
        print(f"❌ Failed to initialize Foundry Local: {e}")
        print("💡 Make sure Foundry Local is installed: foundry --version")
        return
    
    while True:
        # Get user input
        user_message = input("You: ").strip()
        
        if user_message.lower() in ['quit', 'exit', 'bye']:
            print("👋 Goodbye!")
            break
            
        if not user_message:
            continue
            
        try:
            # Send message to local AI model
            response = client.chat.completions.create(
                model=model_id,
                messages=[
                    {"role": "system", "content": "You are a helpful AI assistant running locally."},
                    {"role": "user", "content": user_message}
                ],
                max_tokens=200,
                temperature=0.7
            )
            
            # Display the response
            ai_response = response.choices[0].message.content
            print(f"🤖 AI: {ai_response}\n")
            
        except Exception as e:
            print(f"❌ Error: {e}")
            print("💡 Check service status: foundry service status\n")

if __name__ == "__main__":
    main()
```

> [!TIP]
> **Esempi correlati**: Per un utilizzo più avanzato, consulta:
>
> - **Esempio Python**: `Workshop/samples/session01/chat_bootstrap.py` - Include risposte in streaming e gestione degli errori
> - **Notebook Jupyter**: `Workshop/notebooks/session01_chat_bootstrap.ipynb` - Versione interattiva con spiegazioni dettagliate

#### Testa la tua applicazione di chat

```powershell
# No need to manually start models - FoundryLocalManager handles this!
# Just run your chat application
python my_first_chat.py
```

Alternativa: Usa direttamente i campioni forniti

```powershell
# Try the complete sample with streaming support
cd Workshop/samples
python -m session01.chat_bootstrap "Your question here"
```

Oppure esplora il notebook interattivo
Apri Workshop/notebooks/session01_chat_bootstrap.ipynb in VS Code

Prova queste conversazioni di esempio:

- "Cos'è Microsoft Foundry Local?"
- "Elenca 3 vantaggi dell'esecuzione di modelli AI localmente"
- "Aiutami a capire l'AI edge"

## Cosa hai realizzato

Congratulazioni! Hai completato con successo:

1. ✅ **Installato Foundry Local** e verificato il suo funzionamento
2. ✅ **Avviato il tuo primo modello AI** (phi-4-mini) localmente
3. ✅ **Testato diversi modelli** tramite riga di comando
4. ✅ **Creato un'applicazione di chat** che si connette al tuo AI locale
5. ✅ **Sperimentato l'inferenza AI locale** senza dipendenze dal cloud

## Comprendere cosa è successo

### Inferenza AI locale

- I tuoi modelli AI funzionano interamente sul tuo computer
- Nessun dato viene inviato al cloud
- Le risposte vengono generate localmente utilizzando CPU/GPU
- Privacy e sicurezza sono garantite

### Gestione dei modelli

- `foundry model run` scarica e avvia i modelli
- **FoundryLocalManager SDK** gestisce automaticamente l'avvio del servizio e il caricamento dei modelli
- I modelli vengono memorizzati localmente per un uso futuro
- È possibile scaricare più modelli, ma generalmente ne viene eseguito uno alla volta
- Il servizio gestisce automaticamente il ciclo di vita dei modelli

### Approcci SDK vs CLI

- **Approccio CLI**: Gestione manuale dei modelli con `foundry model run <model>`
- **Approccio SDK**: Gestione automatica del servizio e dei modelli con `FoundryLocalManager(alias)`
- **Raccomandazione**: Usa l'SDK per le applicazioni, il CLI per test e esplorazioni

## Riferimenti ai comandi comuni

### Comandi essenziali del CLI

```powershell
# Installation & Setup
foundry --version              # Check installation
foundry --help                 # View all commands

# Model Management
foundry model list             # List available models
foundry model run <model>      # Download and start a model
foundry model run <model> --prompt "text"  # One-shot prompt
foundry cache list             # Show downloaded models

# Service Management
foundry service status         # Check if service is running
foundry service start          # Start the service manually
foundry service stop           # Stop the service
```

### Raccomandazioni sui modelli

- **phi-4-mini**: Miglior modello iniziale - veloce, leggero, buona qualità
- **qwen2.5-0.5b**: Inferenza più veloce, uso minimo di memoria
- **gpt-oss-20b**: Risposte di qualità superiore, richiede più risorse
- **deepseek-coder-1.3b**: Ottimizzato per attività di programmazione e codice

## Risoluzione dei problemi

### "Comando Foundry non trovato"

**Soluzione:**

```powershell
# Restart your terminal after installation
# Or manually add to PATH (Windows)
$env:PATH += ";C:\Program Files\Microsoft\FoundryLocal"
```

### "Caricamento del modello fallito"

**Soluzione:**

```powershell
# Check available system memory
foundry service status

# Try a smaller model first
foundry model run phi-4-mini

# Check disk space for model downloads
# Models are stored in: %USERPROFILE%\.foundry\models (Windows)
```

### "Connessione rifiutata su localhost"

**Soluzione:**

```powershell
# Check if service is running
foundry service status

# Start service if needed
foundry service start

# Verify the port (default is 5273)
# Check for port conflicts with: netstat -an | findstr 5273
```

## Prossimi passi

### Azioni immediate

1. **Sperimenta** con modelli e prompt diversi
2. **Modifica** la tua applicazione di chat per provare modelli diversi
3. **Crea** i tuoi prompt e testa le risposte
4. **Esplora** la Sessione 2: Creazione di applicazioni RAG

### Percorso di apprendimento avanzato

1. **Sessione 2**: Costruire soluzioni AI con RAG (Generazione Augmentata da Recupero)
2. **Sessione 3**: Confrontare diversi modelli open-source
3. **Sessione 4**: Lavorare con modelli all'avanguardia
4. **Sessione 5**: Creare sistemi AI multi-agente

## Variabili di ambiente (opzionale)

Per un utilizzo più avanzato, puoi impostare queste variabili di ambiente:

| Variabile | Scopo | Esempio |
|-----------|-------|---------|
| `FOUNDRY_LOCAL_ALIAS` | Modello predefinito da utilizzare | `phi-4-mini` |
| `FOUNDRY_LOCAL_ENDPOINT` | Sovrascrivere l'URL dell'endpoint | `http://localhost:5273/v1` |

Crea un file `.env` nella directory del tuo progetto:
```
FOUNDRY_LOCAL_ALIAS=phi-4-mini
FOUNDRY_LOCAL_ENDPOINT=auto
```

## Risorse aggiuntive

### Documentazione

- [Riferimento Foundry Local Python SDK](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/reference/reference-sdk?pivots=programming-language-python)
- [Guida all'installazione di Foundry Local](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install)
- [Catalogo dei modelli](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/models)

### Codice di esempio

- **Esempio Python Session01**: `Workshop/samples/session01/chat_bootstrap.py` - App di chat completa con streaming
- **Notebook Session01**: `Workshop/notebooks/session01_chat_bootstrap.ipynb` - Tutorial interattivo  
- [Esempio Modulo08 01](../Module08/samples/01/README.md) - Avvio rapido chat REST
- [Esempio Modulo08 02](../Module08/samples/02/README.md) - Integrazione OpenAI SDK
- [Esempio Modulo08 03](../Module08/samples/03/README.md) - Scoperta e benchmarking dei modelli

### Community

- [Discussioni su Foundry Local GitHub](https://github.com/microsoft/Foundry-Local/discussions)
- [Community Azure AI](https://techcommunity.microsoft.com/category/artificialintelligence)

---

**Durata della sessione**: 30 minuti di pratica + 15 minuti di domande e risposte  
**Livello di difficoltà**: Principiante  
**Prerequisiti**: Windows 11/macOS 11+, Python 3.10+, Accesso amministrativo

## Scenario di esempio del workshop

### Contesto reale

**Scenario**: Un team IT aziendale deve valutare l'inferenza AI su dispositivo per elaborare feedback sensibili dei dipendenti senza inviare dati a servizi esterni.

**Il tuo obiettivo**: Dimostrare che i modelli AI locali possono fornire risposte di qualità con una latenza inferiore al secondo, mantenendo la completa privacy dei dati.

### Prompt di test

Usa questi prompt per validare la tua configurazione:

```json
[
    "List two benefits of local inference.",
    "Summarize why keeping data on device improves privacy.",
    "Give one trade-off when choosing a small model over a large model."
]
```

### Criteri di successo

- ✅ Tutti i prompt ricevono risposte in meno di 2 secondi
- ✅ Nessun dato lascia il tuo computer locale
- ✅ Le risposte sono pertinenti e utili
- ✅ La tua applicazione di chat funziona senza problemi

Questa validazione garantisce che la tua configurazione di Foundry Local sia pronta per i workshop avanzati delle Sessioni 2-6.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire l'accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si consiglia una traduzione professionale umana. Non siamo responsabili per eventuali incomprensioni o interpretazioni errate derivanti dall'uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
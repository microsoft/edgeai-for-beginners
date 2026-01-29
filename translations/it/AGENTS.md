# AGENTS.md

> **Guida per sviluppatori che contribuiscono a EdgeAI per principianti**
> 
> Questo documento fornisce informazioni complete per sviluppatori, agenti AI e collaboratori che lavorano con questo repository. Copre configurazione, flussi di lavoro di sviluppo, test e migliori pratiche.
> 
> **Ultimo aggiornamento**: 30 ottobre 2025 | **Versione del documento**: 3.0

## Indice

- [Panoramica del progetto](../..)
- [Struttura del repository](../..)
- [Prerequisiti](../..)
- [Comandi di configurazione](../..)
- [Flusso di lavoro di sviluppo](../..)
- [Istruzioni per il test](../..)
- [Linee guida per lo stile del codice](../..)
- [Linee guida per le pull request](../..)
- [Sistema di traduzione](../..)
- [Integrazione locale di Foundry](../..)
- [Build e distribuzione](../..)
- [Problemi comuni e risoluzione](../..)
- [Risorse aggiuntive](../..)
- [Note specifiche del progetto](../..)
- [Ottenere aiuto](../..)

## Panoramica del progetto

EdgeAI per principianti è un repository educativo completo che insegna lo sviluppo di Edge AI con Small Language Models (SLM). Il corso copre i fondamenti di EdgeAI, il deployment dei modelli, tecniche di ottimizzazione e implementazioni pronte per la produzione utilizzando Microsoft Foundry Local e vari framework AI.

**Tecnologie principali:**
- Python 3.8+ (linguaggio principale per esempi AI/ML)
- .NET C# (esempi AI/ML)
- JavaScript/Node.js con Electron (per applicazioni desktop)
- Microsoft Foundry Local SDK
- Microsoft Windows ML 
- VSCode AI Toolkit
- OpenAI SDK
- Framework AI: LangChain, Semantic Kernel, Chainlit
- Ottimizzazione dei modelli: Llama.cpp, Microsoft Olive, OpenVINO, Apple MLX

**Tipo di repository:** Repository di contenuti educativi con 8 moduli e 10 applicazioni di esempio complete

**Architettura:** Percorso di apprendimento multi-modulo con esempi pratici che dimostrano modelli di deployment Edge AI

## Struttura del repository

```
edgeai-for-beginners/
├── introduction.md          # Course introduction and overview
├── Module01-07/            # Core educational modules (Markdown)
├── Module08/               # Foundry Local toolkit with 10 samples
│   ├── samples/01-06/     # Foundation samples (Python)
│   ├── samples/07/        # API client (Python)
│   ├── samples/08/        # Windows 11 chat app (Electron)
│   └── samples/09-10/     # Advanced multi-agent systems (Python)
├── Workshop/               # Hands-on workshop materials
│   ├── samples/           # Workshop Python samples with utilities
│   │   ├── session01/     # Chat bootstrap samples
│   │   ├── session02-06/  # Progressive workshop sessions
│   │   └── util/          # Workshop utility modules
│   ├── notebooks/         # Jupyter notebook tutorials
│   └── scripts/           # Validation and testing tools
├── translations/          # Multi-language translations (50+ languages)
├── translated_images/     # Localized images
└── imgs/                  # Course images and assets
```

## Prerequisiti

### Strumenti richiesti

- **Python 3.8+** - Per esempi AI/ML e notebook
- **Node.js 16+** - Per l'applicazione di esempio Electron
- **Git** - Per il controllo di versione
- **Microsoft Foundry Local** - Per eseguire modelli AI localmente

### Strumenti consigliati

- **Visual Studio Code** - Con estensioni Python, Jupyter e Pylance
- **Windows Terminal** - Per una migliore esperienza da riga di comando (utenti Windows)
- **Docker** - Per lo sviluppo containerizzato (opzionale)

### Requisiti di sistema

- **RAM**: minimo 8GB, consigliato 16GB+ per scenari multi-modello
- **Spazio di archiviazione**: almeno 10GB liberi per modelli e dipendenze
- **OS**: Windows 10/11, macOS 11+ o Linux (Ubuntu 20.04+)
- **Hardware**: CPU con supporto AVX2; GPU (CUDA, Qualcomm NPU) opzionale ma consigliata

### Conoscenze richieste

- Comprensione di base della programmazione in Python
- Familiarità con interfacce da riga di comando
- Comprensione dei concetti AI/ML (per lo sviluppo degli esempi)
- Flussi di lavoro Git e processi di pull request

## Comandi di configurazione

### Configurazione del repository

```bash
# Clone the repository
git clone https://github.com/microsoft/edgeai-for-beginners.git
cd edgeai-for-beginners

# No build step required - this is primarily an educational content repository
```

### Configurazione degli esempi Python (Modulo08 e esempi Workshop)

```bash
# Create and activate virtual environment
python -m venv .venv
# On Windows
.venv\Scripts\activate
# On macOS/Linux
source .venv/bin/activate

# Install Foundry Local SDK and dependencies
pip install foundry-local-sdk openai

# Install additional dependencies for Module08 samples
cd Module08
pip install -r requirements.txt

# Install Workshop dependencies
cd ../Workshop
pip install -r requirements.txt
```

### Configurazione degli esempi Node.js (Esempio 08 - App Chat per Windows)

```bash
cd Module08/samples/08
npm install

# Start in development mode
npm run dev

# Build for production
npm run build

# Create installer
npm run dist
```

### Configurazione di Foundry Local

Foundry Local è necessario per eseguire gli esempi. Scarica e installa dal repository ufficiale:

**Installazione:**
- **Windows**: `winget install Microsoft.FoundryLocal`
- **macOS**: `brew tap microsoft/foundrylocal && brew install foundrylocal`
- **Manuale**: Scarica dalla [pagina delle release](https://github.com/microsoft/Foundry-Local/releases)

**Avvio rapido:**
```bash
# Run your first model (auto-downloads if needed)
foundry model run phi-4-mini

# List available models
foundry model ls

# Check service status
foundry service status
```

**Nota**: Foundry Local seleziona automaticamente la variante del modello migliore per il tuo hardware (GPU CUDA, NPU Qualcomm o CPU).

## Flusso di lavoro di sviluppo

### Sviluppo dei contenuti

Questo repository contiene principalmente **contenuti educativi in Markdown**. Quando apporti modifiche:

1. Modifica i file `.md` nelle directory dei moduli appropriati
2. Segui i modelli di formattazione esistenti
3. Assicurati che gli esempi di codice siano accurati e testati
4. Aggiorna il contenuto tradotto corrispondente, se necessario (o lascia che l'automazione se ne occupi)

### Sviluppo delle applicazioni di esempio

Per gli esempi Python del Modulo08 (esempi 01-07, 09-10):
```bash
cd Module08
python samples/01/chat_quickstart.py "Test message"
```

Per gli esempi Python del Workshop:
```bash
cd Workshop/samples/session01
python chat_bootstrap.py "Test message"
```

Per l'esempio Electron (esempio 08):
```bash
cd Module08/samples/08
npm run dev  # Development with hot reload
```

### Test delle applicazioni di esempio

Gli esempi Python non hanno test automatizzati ma possono essere validati eseguendoli:
```bash
# Test basic chat functionality
python samples/01/chat_quickstart.py "Hello"

# Test with specific model
set MODEL=phi-4-mini
python samples/02/openai_sdk_client.py
```

L'esempio Electron ha un'infrastruttura di test:
```bash
cd Module08/samples/08
npm test           # Run unit tests
npm run test:e2e   # Run end-to-end tests
npm run lint       # Check code style
```

## Istruzioni per il test

### Validazione dei contenuti

Il repository utilizza flussi di lavoro di traduzione automatizzati. Non è richiesto alcun test manuale per le traduzioni.

**Validazione manuale per modifiche ai contenuti:**
1. Anteprima del rendering Markdown dei file `.md`
2. Verifica che tutti i link puntino a destinazioni valide
3. Testa eventuali snippet di codice inclusi nella documentazione
4. Controlla che le immagini si carichino correttamente

### Test delle applicazioni di esempio

**Modulo08/esempi/08 (app Electron) ha test completi:**
```bash
cd Module08/samples/08

# Run all tests
npm test

# Run unit tests only
npm test -- --testPathPattern=unit

# Run integration tests
npm run test:integration

# Run E2E tests
npm run test:e2e

# Check test coverage
npm test -- --coverage
```

**Gli esempi Python devono essere testati manualmente:**
```bash
# Module08 samples
python samples/01/chat_quickstart.py "Test prompt"
python samples/04/chainlit_rag.py
python samples/09/multi_agent_system.py

# Workshop samples
cd Workshop/samples/session01
python chat_bootstrap.py "Test prompt"

# Use Workshop validation tools
cd Workshop/scripts
python validate_samples.py  # Validate syntax and imports
python test_samples.py      # Run smoke tests
```

## Linee guida per lo stile del codice

### Contenuti Markdown

- Usa una gerarchia coerente per i titoli (# per il titolo, ## per le sezioni principali, ### per le sottosezioni)
- Includi blocchi di codice con specificatori di linguaggio: ```python, ```bash, ```javascript
- Segui la formattazione esistente per tabelle, elenchi e enfasi
- Mantieni le righe leggibili (circa 80-100 caratteri, ma non in modo rigido)
- Usa link relativi per riferimenti interni

### Stile del codice Python

- Segui le convenzioni PEP 8
- Usa suggerimenti di tipo dove appropriato
- Includi docstring per funzioni e classi
- Usa nomi di variabili significativi
- Mantieni le funzioni focalizzate e concise

### Stile del codice JavaScript/Node.js

```bash
# Electron sample follows ESLint configuration
cd Module08/samples/08
npm run lint        # Check for style issues
npm run lint:fix    # Auto-fix style issues
npm run format      # Format with Prettier
```

**Convenzioni principali:**
- Configurazione ESLint fornita nell'esempio 08
- Prettier per la formattazione del codice
- Usa sintassi moderna ES6+
- Segui i modelli esistenti nel codice

## Linee guida per le pull request

### Flusso di lavoro per i contributi

1. **Fai un fork del repository** e crea un nuovo branch da `main`
2. **Apporta le modifiche** seguendo le linee guida per lo stile del codice
3. **Testa accuratamente** utilizzando le istruzioni per il test sopra
4. **Effettua il commit con messaggi chiari** seguendo il formato dei commit convenzionali
5. **Fai push sul tuo fork** e crea una pull request
6. **Rispondi ai feedback** dei manutentori durante la revisione

### Convenzione per i nomi dei branch

- `feature/<modulo>-<descrizione>` - Per nuove funzionalità o contenuti
- `fix/<modulo>-<descrizione>` - Per correzioni di bug
- `docs/<descrizione>` - Per miglioramenti alla documentazione
- `refactor/<descrizione>` - Per refactoring del codice

### Formato dei messaggi di commit

Segui [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

**Esempi:**
```
feat(Module08): add intent-based routing notebook
docs(AGENTS): update Foundry Local setup instructions
fix(samples/08): resolve Electron build issue
```

### Formato del titolo
```
[ModuleXX] Brief description of change
```
or
```
[Module08/samples/XX] Description for sample changes
```

### Codice di condotta

Tutti i collaboratori devono seguire il [Codice di condotta open source di Microsoft](https://opensource.microsoft.com/codeofconduct/). Si prega di leggere [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) prima di contribuire.

### Prima di inviare

**Per modifiche ai contenuti:**
- Anteprima di tutti i file Markdown modificati
- Verifica che i link e le immagini funzionino
- Controlla errori di battitura e grammaticali

**Per modifiche al codice degli esempi (Modulo08/esempi/08):**
```bash
npm run lint
npm test
```

**Per modifiche agli esempi Python:**
- Testa che l'esempio venga eseguito correttamente
- Verifica che la gestione degli errori funzioni
- Controlla la compatibilità con Foundry Local

### Processo di revisione

- Le modifiche ai contenuti educativi vengono revisionate per accuratezza e chiarezza
- Gli esempi di codice vengono testati per funzionalità
- Gli aggiornamenti delle traduzioni sono gestiti automaticamente da GitHub Actions

## Sistema di traduzione

**IMPORTANTE:** Questo repository utilizza traduzioni automatizzate tramite GitHub Actions.

- Le traduzioni si trovano nella directory `/translations/` (50+ lingue)
- Automatizzate tramite il workflow `co-op-translator.yml`
- **NON modificare manualmente i file di traduzione** - verranno sovrascritti
- Modifica solo i file sorgente in inglese nella root e nelle directory dei moduli
- Le traduzioni vengono generate automaticamente al push sul branch `main`

## Integrazione locale di Foundry

La maggior parte degli esempi del Modulo08 richiede che Microsoft Foundry Local sia in esecuzione.

### Installazione e configurazione

**Installa Foundry Local:**
```bash
# Windows
winget install Microsoft.FoundryLocal

# macOS
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**Installa Python SDK:**
```bash
pip install foundry-local-sdk openai
```

### Avvio di Foundry Local
```bash
# Start service and run a model (auto-downloads if needed)
foundry model run phi-3.5-mini

# Or use model aliases for automatic hardware optimization
foundry model run phi-4-mini
foundry model run qwen2.5-0.5b
foundry model run qwen2.5-coder-0.5b

# Check service status
foundry service status

# List available models
foundry model ls
```

### Utilizzo SDK (Python)
```python
from foundry_local import FoundryLocalManager
import openai

# Use model alias for automatic hardware optimization
alias = "phi-4-mini"

# Create manager (auto-starts service and loads model)
manager = FoundryLocalManager(alias)

# Configure OpenAI client for local Foundry service
client = openai.OpenAI(
    base_url=manager.endpoint,
    api_key=manager.api_key
)

# Use the model
response = client.chat.completions.create(
    model=manager.get_model_info(alias).id,
    messages=[{"role": "user", "content": "Hello!"}]
)
```

### Verifica di Foundry Local
```bash
# Service status and endpoint
foundry service status

# List loaded models (REST API)
curl http://localhost:<port>/v1/models

# Note: Port is displayed when running 'foundry service status'
```

### Variabili d'ambiente per gli esempi

La maggior parte degli esempi utilizza queste variabili d'ambiente:
```bash
# Foundry Local configuration
# Note: The SDK (FoundryLocalManager) automatically detects endpoint
set MODEL=phi-4-mini  # or phi-3.5-mini, qwen2.5-0.5b, qwen2.5-coder-0.5b
set API_KEY=            # Not required for local usage

# Manual endpoint (if not using SDK)
# Port is shown via 'foundry service status'
set BASE_URL=http://localhost:<port>

# For Azure OpenAI fallback (optional)
set AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
set AZURE_OPENAI_API_KEY=your-api-key
set AZURE_OPENAI_API_VERSION=2024-08-01-preview
```

**Nota**: Quando si utilizza `FoundryLocalManager`, l'SDK gestisce automaticamente la scoperta dei servizi e il caricamento dei modelli. Gli alias dei modelli (come `phi-3.5-mini`) garantiscono la selezione della variante migliore per il tuo hardware.

## Build e distribuzione

### Distribuzione dei contenuti

Questo repository è principalmente documentazione - non è richiesto alcun processo di build per i contenuti.

### Build delle applicazioni di esempio

**Applicazione Electron (Modulo08/esempi/08):**
```bash
cd Module08/samples/08

# Development build
npm run dev

# Production build
npm run build

# Create Windows installer
npm run dist

# Create portable executable
npm run pack
```

**Esempi Python:**
Nessun processo di build - gli esempi vengono eseguiti direttamente con l'interprete Python.

## Problemi comuni e risoluzione

> **Suggerimento**: Controlla [GitHub Issues](https://github.com/microsoft/edgeai-for-beginners/issues) per problemi noti e soluzioni.

### Problemi critici (bloccanti)

#### Foundry Local non in esecuzione
**Problema:** Gli esempi falliscono con errori di connessione

**Soluzione:**
```bash
# Check if service is running
foundry service status

# Start service with a model
foundry model run phi-4-mini

# Or explicitly start service
foundry service start

# List loaded models
foundry model ls

# Verify via REST API (port shown in 'foundry service status')
curl http://localhost:<port>/v1/models
```

### Problemi comuni (moderati)

#### Problemi con l'ambiente virtuale Python
**Problema:** Errori di importazione dei moduli

**Soluzione:**
```bash
# Ensure virtual environment is activated
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt
```

#### Problemi di build di Electron
**Problema:** Errori di npm install o build

**Soluzione:**
```bash
cd Module08/samples/08
# Clean install
npm run clean
rm -rf node_modules package-lock.json
npm install
```

### Problemi di flusso di lavoro (minori)

#### Conflitti nel flusso di lavoro di traduzione
**Problema:** La PR di traduzione è in conflitto con le tue modifiche

**Soluzione:**
- Modifica solo i file sorgente in inglese
- Lascia che il flusso di lavoro di traduzione automatizzato gestisca le traduzioni
- Se si verificano conflitti, unisci `main` nel tuo branch dopo che le traduzioni sono state integrate

#### Errori nel download dei modelli
**Problema:** Foundry Local non riesce a scaricare i modelli

**Soluzione:**
```bash
# Check internet connectivity
# Clear model cache and retry
foundry model remove <model-alias>
foundry model run <model-alias>

# Check available disk space (models can be 2-16GB)
# Verify firewall settings allow downloads
```

## Risorse aggiuntive

### Percorsi di apprendimento
- **Percorso per principianti:** Moduli 01-02 (7-9 ore)
- **Percorso intermedio:** Moduli 03-04 (9-11 ore)
- **Percorso avanzato:** Moduli 05-07 (12-15 ore)
- **Percorso esperto:** Modulo 08 (8-10 ore)
- **Workshop pratico:** Materiali del workshop (6-8 ore)

### Contenuti principali dei moduli
- **Modulo01:** Fondamenti di EdgeAI e casi di studio reali
- **Modulo02:** Famiglie e architetture di Small Language Model (SLM)
- **Modulo03:** Strategie di deployment locale e cloud
- **Modulo04:** Ottimizzazione dei modelli con framework multipli (Llama.cpp, Microsoft Olive, OpenVINO, Qualcomm QNN, Apple MLX)
- **Modulo05:** SLMOps - operazioni di produzione
- **Modulo06:** Agenti AI e chiamata di funzioni
- **Modulo07:** Implementazioni specifiche per piattaforma
- **Modulo08:** Toolkit Foundry Local con 10 esempi completi

### Dipendenze esterne
- [Microsoft Foundry Local](https://github.com/microsoft/Foundry-Local) - Runtime locale per modelli AI con API compatibile OpenAI
  - [Documentazione](https://github.com/microsoft/Foundry-Local/blob/main/docs/README.md)
  - [Python SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/python)
  - [JavaScript SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/javascript)
- [Llama.cpp](https://github.com/ggml-org/llama.cpp) - Framework di ottimizzazione
- [Microsoft Olive](https://microsoft.github.io/Olive/) - Toolkit di ottimizzazione dei modelli
- [OpenVINO](https://docs.openvino.ai/) - Toolkit di ottimizzazione di Intel

## Note specifiche del progetto

### Applicazioni di esempio del Modulo08

Il repository include 10 applicazioni di esempio complete:

1. **01-REST Chat Quickstart** - Integrazione di base con OpenAI SDK
2. **02-Integrazione OpenAI SDK** - Funzionalità avanzate dell'SDK
3. **03-Scoperta e benchmarking dei modelli** - Strumenti di confronto dei modelli
4. **04-Applicazione RAG con Chainlit** - Generazione aumentata da recupero
5. **05-Orchestrazione multi-agente** - Coordinamento di base degli agenti
6. **06-Router di modelli come strumenti** - Routing intelligente dei modelli
7. **07-Client API diretto** - Integrazione API a basso livello
8. **08-App Chat per Windows 11** - Applicazione desktop nativa Electron
9. **09-Sistema multi-agente avanzato** - Orchestrazione complessa degli agenti
10. **10-Strumenti del Framework Foundry** - Integrazione LangChain/Semantic Kernel

### Applicazioni di esempio del Workshop

Il Workshop include 6 sessioni progressive con implementazioni pratiche:

1. **Sessione 01** - Avvio della chat con integrazione Foundry Local
2. **Sessione 02** - Pipeline RAG e valutazione con RAGAS
3. **Sessione 03** - Benchmarking di modelli open-source
4. **Sessione 04** - Confronto e selezione dei modelli
5. **Sessione 05** - Sistemi di orchestrazione multi-agente
6. **Sessione 06** - Routing dei modelli e gestione delle pipeline

Ogni esempio dimostra diversi aspetti dello sviluppo AI edge con Foundry Local.

### Considerazioni sulle prestazioni

- Gli SLM sono ottimizzati per il deployment edge (2-16GB RAM)
- L'inferenza locale offre tempi di risposta di 50-500ms
- Le tecniche di quantizzazione riducono le dimensioni del 75% mantenendo l'85% delle prestazioni
- Capacità di conversazione in tempo reale con modelli locali

### Sicurezza e Privacy

- Tutto il processamento avviene localmente - nessun dato inviato al cloud
- Adatto per applicazioni sensibili alla privacy (sanità, finanza)
- Soddisfa i requisiti di sovranità dei dati
- Foundry Local funziona interamente su hardware locale

## Ottenere Aiuto

### Documentazione

- **README principale**: [README.md](README.md) - Panoramica del repository e percorsi di apprendimento
- **Guida di studio**: [STUDY_GUIDE.md](STUDY_GUIDE.md) - Risorse di apprendimento e cronologia
- **Supporto**: [SUPPORT.md](SUPPORT.md) - Come ottenere aiuto
- **Sicurezza**: [SECURITY.md](SECURITY.md) - Segnalazione di problemi di sicurezza

### Supporto della Comunità

- **Problemi su GitHub**: [Segnala bug o richiedi funzionalità](https://github.com/microsoft/edgeai-for-beginners/issues)
- **Discussioni su GitHub**: [Fai domande e condividi idee](https://github.com/microsoft/edgeai-for-beginners/discussions)
- **Problemi con Foundry Local**: [Problemi tecnici con Foundry Local](https://github.com/microsoft/Foundry-Local/issues)

### Contatti

- **Manutentori**: Vedi [CODEOWNERS](https://github.com/microsoft/edgeai-for-beginners/blob/main/.github/CODEOWNERS)
- **Problemi di sicurezza**: Segui la divulgazione responsabile in [SECURITY.md](SECURITY.md)
- **Supporto Microsoft**: Per supporto aziendale, contatta il servizio clienti Microsoft

### Risorse aggiuntive

- **Microsoft Learn**: [Percorsi di apprendimento su AI e Machine Learning](https://learn.microsoft.com/training/browse/?products=ai-services)
- **Documentazione Foundry Local**: [Documentazione ufficiale](https://github.com/microsoft/Foundry-Local/blob/main/docs/README.md)
- **Esempi della comunità**: Consulta [Discussioni su GitHub](https://github.com/microsoft/edgeai-for-beginners/discussions) per i contributi della comunità

---

**Questo è un repository educativo focalizzato sull'insegnamento dello sviluppo AI edge. Il principale modello di contributo consiste nel migliorare i contenuti educativi e aggiungere/migliorare applicazioni di esempio che dimostrano concetti di AI edge.**

---

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire l'accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale umana. Non siamo responsabili per eventuali incomprensioni o interpretazioni errate derivanti dall'uso di questa traduzione.
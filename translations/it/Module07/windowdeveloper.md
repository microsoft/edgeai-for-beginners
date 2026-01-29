# Guida allo sviluppo di Windows Edge AI

## Introduzione

Benvenuto nello sviluppo di Windows Edge AI - la tua guida completa per creare applicazioni intelligenti che sfruttano la potenza dell'AI su dispositivo utilizzando la piattaforma Windows AI Foundry di Microsoft. Questa guida è pensata specificamente per gli sviluppatori Windows che desiderano integrare funzionalità avanzate di Edge AI nelle loro applicazioni, sfruttando al massimo l'accelerazione hardware di Windows.

### Il vantaggio di Windows AI

Windows AI Foundry rappresenta una piattaforma unificata, affidabile e sicura che supporta l'intero ciclo di vita dello sviluppo AI - dalla selezione e ottimizzazione del modello fino alla distribuzione su CPU, GPU, NPU e architetture cloud ibride. Questa piattaforma democratizza lo sviluppo AI offrendo:

- **Astrazione hardware**: Distribuzione senza soluzione di continuità su silicio AMD, Intel, NVIDIA e Qualcomm
- **Intelligenza su dispositivo**: AI che preserva la privacy e funziona interamente su hardware locale
- **Prestazioni ottimizzate**: Modelli pre-ottimizzati per configurazioni hardware Windows
- **Pronto per l'impresa**: Funzionalità di sicurezza e conformità di livello produttivo

### Windows ML 
Windows Machine Learning (ML) consente agli sviluppatori C#, C++ e Python di eseguire modelli ONNX AI localmente su PC Windows tramite ONNX Runtime, con gestione automatica dei provider di esecuzione per diversi hardware (CPU, GPU, NPU). [ONNX Runtime](https://onnxruntime.ai/docs/) può essere utilizzato con modelli provenienti da PyTorch, Tensorflow/Keras, TFLite, scikit-learn e altri framework.


![WindowsML Un diagramma che illustra un modello ONNX che passa attraverso Windows ML per raggiungere NPUs, GPUs e CPUs.l](https://learn.microsoft.com/en-us/windows/ai/images/winml-diagram.png)

Windows ML fornisce una copia condivisa di ONNX Runtime per tutto Windows, oltre alla possibilità di scaricare dinamicamente i provider di esecuzione (EP).

### Perché scegliere Windows per Edge AI?

**Supporto hardware universale**
Windows ML offre ottimizzazione hardware automatica in tutto l'ecosistema Windows, garantendo che le tue applicazioni AI funzionino al meglio indipendentemente dall'architettura del silicio sottostante.

**Runtime AI integrato**
Il motore di inferenza Windows ML integrato elimina i requisiti di configurazione complessi, consentendo agli sviluppatori di concentrarsi sulla logica dell'applicazione anziché sulle preoccupazioni infrastrutturali.

**Ottimizzazione PC Copilot+**
API progettate appositamente per i dispositivi Windows di nuova generazione con Neural Processing Units (NPUs) dedicate, offrendo prestazioni eccezionali per watt.

**Ecosistema per sviluppatori**
Strumenti avanzati, tra cui l'integrazione con Visual Studio, documentazione completa e applicazioni di esempio che accelerano i cicli di sviluppo.

## Obiettivi di apprendimento

Completando questa guida allo sviluppo di Windows Edge AI, acquisirai le competenze essenziali per creare applicazioni AI pronte per la produzione sulla piattaforma Windows.

### Competenze tecniche principali

**Padronanza di Windows AI Foundry**
- Comprendere l'architettura e i componenti della piattaforma Windows AI Foundry
- Navigare nel ciclo di vita completo dello sviluppo AI all'interno dell'ecosistema Windows
- Implementare le migliori pratiche di sicurezza per applicazioni AI su dispositivo
- Ottimizzare le applicazioni per diverse configurazioni hardware Windows

**Esperienza nell'integrazione API**
- Padroneggiare le API Windows AI per applicazioni di testo, visione e multimodali
- Implementare l'integrazione del modello linguistico Phi Silica per generazione di testo e ragionamento
- Distribuire capacità di visione artificiale utilizzando le API di elaborazione immagini integrate
- Personalizzare modelli pre-addestrati utilizzando tecniche LoRA (Low-Rank Adaptation)

**Implementazione locale di Foundry**
- Esplorare, valutare e distribuire modelli linguistici open-source utilizzando Foundry Local CLI
- Comprendere l'ottimizzazione e la quantizzazione dei modelli per la distribuzione locale
- Implementare capacità AI offline che funzionano senza connettività internet
- Gestire i cicli di vita e gli aggiornamenti dei modelli in ambienti di produzione

**Distribuzione Windows ML**
- Portare modelli ONNX personalizzati nelle applicazioni Windows utilizzando Windows ML
- Sfruttare l'accelerazione hardware automatica su architetture CPU, GPU e NPU
- Implementare inferenze in tempo reale con utilizzo ottimale delle risorse
- Progettare applicazioni AI scalabili per diverse categorie di dispositivi Windows

### Competenze nello sviluppo di applicazioni

**Sviluppo Windows cross-platform**
- Creare applicazioni potenziate dall'AI utilizzando .NET MAUI per distribuzione universale su Windows
- Integrare capacità AI in applicazioni Win32, UWP e Progressive Web Applications
- Implementare design UI reattivi che si adattano agli stati di elaborazione AI
- Gestire operazioni AI asincrone con modelli di esperienza utente adeguati

**Ottimizzazione delle prestazioni**
- Profilare e ottimizzare le prestazioni di inferenza AI su diverse configurazioni hardware
- Implementare una gestione efficiente della memoria per modelli linguistici di grandi dimensioni
- Progettare applicazioni che si degradano in modo elegante in base alle capacità hardware disponibili
- Applicare strategie di caching per operazioni AI utilizzate frequentemente

**Prontezza per la produzione**
- Implementare una gestione completa degli errori e meccanismi di fallback
- Progettare telemetria e monitoraggio per le prestazioni delle applicazioni AI
- Applicare le migliori pratiche di sicurezza per l'archiviazione e l'esecuzione locale dei modelli AI
- Pianificare strategie di distribuzione per applicazioni aziendali e consumer

### Comprensione strategica e di business

**Architettura delle applicazioni AI**
- Progettare architetture ibride che ottimizzano tra elaborazione AI locale e cloud
- Valutare i compromessi tra dimensione del modello, accuratezza e velocità di inferenza
- Pianificare architetture di flusso dati che mantengano la privacy pur abilitando l'intelligenza
- Implementare soluzioni AI economiche che si scalano con le richieste degli utenti

**Posizionamento sul mercato**
- Comprendere i vantaggi competitivi delle applicazioni AI native di Windows
- Identificare i casi d'uso in cui l'AI su dispositivo offre esperienze utente superiori
- Sviluppare strategie di go-to-market per applicazioni Windows potenziate dall'AI
- Posizionare le applicazioni per sfruttare i benefici dell'ecosistema Windows

## Esempi di AI nel Windows App SDK

Il Windows App SDK fornisce esempi completi che dimostrano l'integrazione AI attraverso diversi framework e scenari di distribuzione. Questi esempi sono riferimenti essenziali per comprendere i modelli di sviluppo AI su Windows.

### Esempi di Windows AI Foundry

| Esempio | Framework | Area di interesse | Caratteristiche principali |
|---------|-----------|-------------------|----------------------------|
| [cs-winui](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsAIFoundry/cs-winui) | C# WinUI 3 | Integrazione API Windows AI | Applicazione completa WinUI che dimostra le API Windows AI, ottimizzazione ARM64, distribuzione pacchettizzata |

**Tecnologie chiave:**
- API Windows AI
- Framework WinUI 3
- Ottimizzazione piattaforma ARM64
- Compatibilità PC Copilot+
- Distribuzione app pacchettizzata

**Prerequisiti:**
- Windows 11 con PC Copilot+ consigliato
- Visual Studio 2022
- Configurazione build ARM64
- Windows App SDK 1.8.1+

### Esempi di Windows ML

#### Esempi C++

| Esempio | Tipo | Area di interesse | Caratteristiche principali |
|---------|------|-------------------|----------------------------|
| [CppConsoleDesktop](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | App console | Windows ML di base | Scoperta EP, opzioni da riga di comando, compilazione modello |
| [CppConsoleDesktop.FrameworkDependent](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | App console | Distribuzione framework | Runtime condiviso, impronta di distribuzione ridotta |
| [CppConsoleDesktop.SelfContained](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | App console | Distribuzione autonoma | Distribuzione standalone, nessuna dipendenza runtime |
| [CppConsoleDll](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | DLL | Utilizzo libreria | WindowsML in libreria condivisa, gestione memoria |
| [CppResnetBuildDemo](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Demo | Tutorial ResNet | Conversione modello, compilazione EP, tutorial Build 2025 |

#### Esempi C#

**Applicazioni console**

| Esempio | Tipo | Area di interesse | Caratteristiche principali |
|---------|------|-------------------|----------------------------|
| [CSharpConsoleDesktop](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs) | App console | Integrazione C# di base | Utilizzo helper condivisi, interfaccia da riga di comando |
| [ResnetBuildDemoCS](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs) | Demo | Tutorial ResNet | Conversione modello, compilazione EP, tutorial Build 2025 |

**Applicazioni GUI**

| Esempio | Framework | Area di interesse | Caratteristiche principali |
|---------|-----------|-------------------|----------------------------|
| [cs-wpf](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs-wpf) | WPF | GUI desktop | Classificazione immagini con interfaccia WPF |
| [cs-winforms](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs-winforms) | Windows Forms | GUI tradizionale | Classificazione immagini con Windows Forms |
| [cs-winui](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs-winui) | WinUI 3 | GUI moderna | Classificazione immagini con interfaccia WinUI 3 |

#### Esempi Python

| Esempio | Linguaggio | Area di interesse | Caratteristiche principali |
|---------|------------|-------------------|----------------------------|
| [SqueezeNetPython](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/python) | Python | Classificazione immagini | Binding Python WinML, elaborazione immagini batch |

### Prerequisiti degli esempi

**Requisiti di sistema:**
- PC Windows 11 con versione 24H2 (build 26100) o superiore
- Visual Studio 2022 con workload C++ e .NET
- Windows App SDK 1.8.1 o successivo
- Python 3.10-3.13 per esempi Python su dispositivi x64 e ARM64

**Specifico per Windows AI Foundry:**
- PC Copilot+ consigliato per prestazioni ottimali
- Configurazione build ARM64 per esempi Windows AI
- Identità pacchetto richiesta (app non pacchettizzate non più supportate)

### Flusso di lavoro comune degli esempi

La maggior parte degli esempi Windows ML segue questo schema standard:

1. **Inizializzare l'ambiente** - Creare l'ambiente ONNX Runtime
2. **Registrare i provider di esecuzione** - Scoprire e registrare gli acceleratori hardware disponibili (CPU, GPU, NPU)
3. **Caricare il modello** - Caricare il modello ONNX, eventualmente compilarlo per hardware target
4. **Preprocessare l'input** - Convertire immagini/dati nel formato di input del modello
5. **Eseguire l'inferenza** - Eseguire il modello e ottenere le predizioni
6. **Elaborare i risultati** - Applicare softmax e visualizzare le predizioni principali

### File modello utilizzati

| Modello | Scopo | Incluso | Note |
|---------|-------|--------|------|
| SqueezeNet | Classificazione immagini leggera | ✅ Incluso | Pre-addestrato, pronto all'uso |
| ResNet-50 | Classificazione immagini ad alta accuratezza | ❌ Richiede conversione | Utilizzare [AI Toolkit](https://code.visualstudio.com/docs/intelligentapps/modelconversion) per la conversione |

### Supporto hardware

Tutti gli esempi rilevano e utilizzano automaticamente l'hardware disponibile:
- **CPU** - Supporto universale su tutti i dispositivi Windows
- **GPU** - Rilevamento e ottimizzazione automatica per hardware grafico disponibile
- **NPU** - Sfrutta le Neural Processing Units su dispositivi supportati (PC Copilot+)

## Componenti della piattaforma Windows AI Foundry

### 1. API Windows AI

Le API Windows AI offrono capacità AI pronte all'uso alimentate da modelli su dispositivo, ottimizzati per efficienza e prestazioni su dispositivi PC Copilot+ con configurazione minima richiesta.

#### Categorie principali di API

**Modello linguistico Phi Silica**
- Modello linguistico piccolo ma potente per generazione di testo e ragionamento
- Ottimizzato per inferenza in tempo reale con consumo energetico minimo
- Supporto per personalizzazione tramite tecniche LoRA
- Integrazione con ricerca semantica e recupero di conoscenze di Windows

**API di visione artificiale**
- **Riconoscimento testo (OCR)**: Estrarre testo da immagini con alta accuratezza
- **Super risoluzione immagini**: Migliorare la qualità delle immagini con modelli AI locali
- **Segmentazione immagini**: Identificare e isolare oggetti specifici nelle immagini
- **Descrizione immagini**: Generare descrizioni testuali dettagliate per contenuti visivi
- **Cancellazione oggetti**: Rimuovere oggetti indesiderati dalle immagini con inpainting AI

**Capacità multimodali**
- **Integrazione visione-linguaggio**: Combinare comprensione di testo e immagini
- **Ricerca semantica**: Abilitare query in linguaggio naturale su contenuti multimediali
- **Recupero di conoscenze**: Costruire esperienze di ricerca intelligenti con dati locali

### 2. Foundry Local

Foundry Local offre agli sviluppatori accesso rapido a modelli linguistici open-source pronti all'uso su Windows Silicon, con la possibilità di esplorare, testare, interagire e distribuire modelli in applicazioni locali.

#### Applicazioni di esempio Foundry Local

Il [repository Foundry Local](https://github.com/microsoft/Foundry-Local/tree/main/samples) fornisce esempi completi in diversi linguaggi di programmazione e framework, dimostrando vari modelli di integrazione e casi d'uso.

| Esempio | Linguaggio/Framework | Area di interesse | Caratteristiche principali |
|---------|-----------------------|-------------------|----------------------------|
| [dotNET/rag](https://github.com/microsoft/Foundry-Local/tree/main/samples/dotNET/rag) | C# / .NET | Implementazione RAG | Integrazione Semantic Kernel, archivio vettoriale Qdrant, embedding JINA, ingestione documenti, chat in streaming |
| [electron/foundry-chat](https://github.com/microsoft/Foundry-Local/tree/main/samples/electron/foundry-chat) | JavaScript / Electron | App chat desktop | Chat cross-platform, switch modello locale/cloud, integrazione SDK OpenAI, streaming in tempo reale |
| [js/hello-foundry-local](https://github.com/microsoft/Foundry-Local/tree/main/samples/js/hello-foundry-local) | JavaScript / Node.js | Integrazione di base | Utilizzo SDK semplice, inizializzazione modello, funzionalità chat di base |
| [python/hello-foundry-local](https://github.com/microsoft/Foundry-Local/tree/main/samples/python/hello-foundry-local) | Python | Integrazione di base | Utilizzo SDK Python, risposte in streaming, API compatibile OpenAI |
| [rust/hello-foundry-local](https://github.com/microsoft/Foundry-Local/tree/main/samples/rust/hello-foundry-local) | Rust | Integrazione di sistemi | Utilizzo SDK a basso livello, operazioni asincrone, client HTTP reqwest |

#### Categorie di esempi per caso d'uso

**RAG (Retrieval-Augmented Generation)**
- **dotNET/rag**: Implementazione completa di RAG utilizzando Semantic Kernel, database vettoriale Qdrant e embedding JINA
- **Architettura**: Ingestione documenti → Suddivisione testo → Embedding vettoriali → Ricerca di similarità → Risposte contestuali
- **Tecnologie**: Microsoft.SemanticKernel, Qdrant.Client, embedding BERT ONNX, completamento chat in streaming

**Applicazioni Desktop**
- **electron/foundry-chat**: Applicazione chat pronta per la produzione con passaggio tra modelli locali/cloud
- **Funzionalità**: Selettore di modelli, risposte in streaming, gestione errori, distribuzione multipiattaforma
- **Architettura**: Processo principale di Electron, comunicazione IPC, script di preload sicuri

**Esempi di integrazione SDK**
- **JavaScript (Node.js)**: Interazione di base con modelli e risposte in streaming
- **Python**: Utilizzo API compatibile con OpenAI con streaming asincrono
- **Rust**: Integrazione a basso livello con reqwest e tokio per operazioni asincrone

#### Prerequisiti per gli esempi di Foundry Local

**Requisiti di sistema:**
- Windows 11 con Foundry Local installato
- Node.js v16+ per esempi JavaScript/Electron
- .NET 8.0+ per esempi C#
- Python 3.10+ per esempi Python
- Rust 1.70+ per esempi Rust

**Installazione:**
```powershell
# Install Foundry Local
winget install Microsoft.FoundryLocal

# Verify installation
foundry --version
foundry model list
```

#### Configurazione specifica per gli esempi

**Esempio dotNET RAG:**
```powershell
# Install required packages via NuGet
# Microsoft.SemanticKernel.Connectors.Onnx
# Microsoft.SemanticKernel.Connectors.Qdrant
# Qdrant.Client

# Start Qdrant vector database
docker run -p 6333:6333 qdrant/qdrant

# Run Jupyter notebook
jupyter notebook rag_foundrylocal_demo.ipynb
```

**Esempio chat Electron:**
```powershell
# Set environment variables for cloud fallback
$env:YOUR_API_KEY="your-cloud-api-key"
$env:YOUR_ENDPOINT="your-cloud-endpoint"
$env:YOUR_MODEL_NAME="your-cloud-model"

# Install dependencies and run
npm install
npm start
```

**Esempi JavaScript/Python/Rust:**
```powershell
# Download model (example with phi-3.5-mini)
foundry model run phi-3.5-mini

# Run respective sample
node src/app.js          # JavaScript
python src/app.py        # Python
cargo run               # Rust
```

#### Caratteristiche principali

**Catalogo modelli**
- Collezione completa di modelli open-source pre-ottimizzati
- Modelli ottimizzati per CPU, GPU e NPU per distribuzione immediata
- Supporto per famiglie di modelli popolari come Llama, Mistral, Phi e modelli specializzati per domini

**Integrazione CLI**
- Interfaccia a riga di comando per gestione e distribuzione dei modelli
- Workflow automatizzati per ottimizzazione e quantizzazione
- Integrazione con ambienti di sviluppo popolari e pipeline CI/CD

**Distribuzione locale**
- Operazione completamente offline senza dipendenze cloud
- Supporto per formati e configurazioni di modelli personalizzati
- Servizio efficiente dei modelli con ottimizzazione hardware automatica

### 3. Windows ML

Windows ML è la piattaforma AI centrale e runtime di inferenza integrato su Windows, che consente agli sviluppatori di distribuire modelli personalizzati in modo efficiente su un ampio ecosistema hardware Windows.

#### Vantaggi dell'architettura

**Supporto hardware universale**
- Ottimizzazione automatica per silicio AMD, Intel, NVIDIA e Qualcomm
- Supporto per esecuzione su CPU, GPU e NPU con passaggio trasparente
- Astrazione hardware che elimina il lavoro di ottimizzazione specifico per piattaforma

**Flessibilità dei modelli**
- Supporto per il formato modello ONNX con conversione automatica da framework popolari
- Distribuzione di modelli personalizzati con prestazioni di livello produttivo
- Integrazione con architetture di applicazioni Windows esistenti

**Integrazione aziendale**
- Compatibile con framework di sicurezza e conformità di Windows
- Supporto per strumenti di distribuzione e gestione aziendale
- Integrazione con sistemi di gestione e monitoraggio dei dispositivi Windows

## Workflow di sviluppo

### Fase 1: Configurazione dell'ambiente e degli strumenti

**Preparazione dell'ambiente di sviluppo**
1. Installa Visual Studio 2022 con workload C++ e .NET
2. Installa Windows App SDK 1.8.1 o successivo
3. Configura gli strumenti CLI di Windows AI Foundry
4. Configura l'estensione AI Toolkit per Visual Studio Code
5. Configura strumenti di profilazione delle prestazioni e monitoraggio
6. Assicurati della configurazione ARM64 per l'ottimizzazione PC Copilot+

**Configurazione del repository di esempi**
1. Clona il [repository di esempi Windows App SDK](https://github.com/microsoft/WindowsAppSDK-Samples)
2. Naviga in `Samples/WindowsAIFoundry/cs-winui` per esempi API Windows AI
3. Naviga in `Samples/WindowsML` per esempi completi Windows ML
4. Consulta i [requisiti di build](https://learn.microsoft.com/windows/apps/windows-app-sdk/system-requirements) per le piattaforme target

**Esplorazione della galleria AI Dev**
- Esplora applicazioni di esempio e implementazioni di riferimento
- Testa le API Windows AI con dimostrazioni interattive
- Consulta il codice sorgente per best practice e modelli
- Identifica esempi rilevanti per il tuo caso d'uso specifico

### Fase 2: Selezione e integrazione del modello

**Analisi dei requisiti**
- Definisci i requisiti funzionali per le capacità AI
- Stabilisci vincoli di prestazioni e obiettivi di ottimizzazione
- Valuta i requisiti di privacy e sicurezza
- Pianifica l'architettura di distribuzione e le strategie di scalabilità

**Valutazione del modello**
- Usa Foundry Local per testare modelli open-source per il tuo caso d'uso
- Confronta le API Windows AI con i requisiti di modelli personalizzati
- Valuta i compromessi tra dimensione del modello, accuratezza e velocità di inferenza
- Prototipa approcci di integrazione con i modelli selezionati

### Fase 3: Sviluppo dell'applicazione

**Integrazione principale**
- Implementa l'integrazione delle API Windows AI con gestione degli errori adeguata
- Progetta interfacce utente che supportino i workflow di elaborazione AI
- Implementa strategie di caching e ottimizzazione per l'inferenza dei modelli
- Aggiungi telemetria e monitoraggio per le prestazioni delle operazioni AI

**Test e validazione**
- Testa le applicazioni su diverse configurazioni hardware Windows
- Valida metriche di prestazioni in condizioni di carico variabili
- Implementa test automatizzati per la affidabilità delle funzionalità AI
- Conduci test di esperienza utente con funzionalità AI migliorate

### Fase 4: Ottimizzazione e distribuzione

**Ottimizzazione delle prestazioni**
- Profila le prestazioni dell'applicazione su configurazioni hardware target
- Ottimizza l'uso della memoria e le strategie di caricamento dei modelli
- Implementa comportamenti adattivi basati sulle capacità hardware disponibili
- Affina l'esperienza utente per scenari di prestazioni differenti

**Distribuzione in produzione**
- Confeziona le applicazioni con le dipendenze dei modelli AI adeguate
- Implementa meccanismi di aggiornamento per modelli e logica applicativa
- Configura monitoraggio e analisi per ambienti di produzione
- Pianifica strategie di rollout per distribuzioni aziendali e consumer

## Esempi di implementazione pratica

### Esempio 1: Applicazione intelligente per l'elaborazione di documenti

Crea un'applicazione Windows che elabora documenti utilizzando diverse capacità AI:

**Tecnologie utilizzate:**
- Phi Silica per riassunto documenti e risposte a domande
- API OCR per estrazione testo da documenti scansionati
- API di descrizione immagini per analisi di grafici e diagrammi
- Modelli ONNX personalizzati per classificazione documenti

**Approccio di implementazione:**
- Progetta un'architettura modulare con componenti AI plug-in
- Implementa elaborazione asincrona per grandi batch di documenti
- Aggiungi indicatori di progresso e supporto per annullamento operazioni lunghe
- Includi capacità offline per elaborazione documenti sensibili

### Esempio 2: Sistema di gestione inventario per il retail

Crea un sistema di inventario AI per applicazioni retail:

**Tecnologie utilizzate:**
- Segmentazione immagini per identificazione prodotti
- Modelli di visione personalizzati per classificazione di marca e categoria
- Distribuzione locale di modelli linguistici specializzati per il retail
- Integrazione con sistemi POS e di inventario esistenti

**Approccio di implementazione:**
- Costruisci integrazione con fotocamere per scansione prodotti in tempo reale
- Implementa riconoscimento visivo e codici a barre dei prodotti
- Aggiungi query di inventario in linguaggio naturale utilizzando modelli linguistici locali
- Progetta un'architettura scalabile per distribuzione multi-negozio

### Esempio 3: Assistente per documentazione sanitaria

Sviluppa uno strumento di documentazione sanitaria che preserva la privacy:

**Tecnologie utilizzate:**
- Phi Silica per generazione di note mediche e supporto decisionale clinico
- OCR per digitalizzazione di cartelle mediche scritte a mano
- Modelli linguistici medici personalizzati distribuiti tramite Windows ML
- Archiviazione vettoriale locale per recupero di conoscenze mediche

**Approccio di implementazione:**
- Garantisci operazione completamente offline per la privacy dei pazienti
- Implementa validazione e suggerimenti di terminologia medica
- Aggiungi registrazione audit per conformità normativa
- Progetta integrazione con sistemi di cartelle cliniche elettroniche esistenti

## Strategie di ottimizzazione delle prestazioni

### Sviluppo consapevole dell'hardware

**Ottimizzazione NPU**
- Progetta applicazioni per sfruttare le capacità NPU su PC Copilot+
- Implementa fallback graduale su GPU/CPU su dispositivi senza NPU
- Ottimizza formati di modelli per accelerazione specifica NPU
- Monitora utilizzo NPU e caratteristiche termiche

**Gestione della memoria**
- Implementa strategie efficienti di caricamento e caching dei modelli
- Usa mappatura della memoria per modelli grandi per ridurre i tempi di avvio
- Progetta applicazioni consapevoli della memoria per dispositivi con risorse limitate
- Implementa quantizzazione dei modelli per ottimizzazione della memoria

**Efficienza della batteria**
- Ottimizza operazioni AI per consumo energetico minimo
- Implementa elaborazione adattiva basata sullo stato della batteria
- Progetta elaborazione in background efficiente per operazioni AI continue
- Usa strumenti di profilazione energetica per ottimizzare l'uso dell'energia

### Considerazioni sulla scalabilità

**Multi-threading**
- Progetta operazioni AI thread-safe per elaborazione concorrente
- Implementa distribuzione efficiente del lavoro tra i core disponibili
- Usa pattern async/await per operazioni AI non bloccanti
- Pianifica ottimizzazione del pool di thread per configurazioni hardware diverse

**Strategie di caching**
- Implementa caching intelligente per operazioni AI frequentemente utilizzate
- Progetta strategie di invalidazione della cache per aggiornamenti dei modelli
- Usa caching persistente per operazioni di preprocessing costose
- Implementa caching distribuito per scenari multi-utente

## Best practice per sicurezza e privacy

### Protezione dei dati

**Elaborazione locale**
- Garantisci che i dati sensibili non lascino mai il dispositivo locale
- Implementa archiviazione sicura per modelli AI e dati temporanei
- Usa funzionalità di sicurezza Windows per il sandboxing delle applicazioni
- Applica crittografia per modelli archiviati e risultati di elaborazione intermedi

**Sicurezza dei modelli**
- Valida l'integrità dei modelli prima del caricamento e dell'esecuzione
- Implementa meccanismi sicuri di aggiornamento dei modelli
- Usa modelli firmati per prevenire manomissioni
- Applica controlli di accesso per file di modelli e configurazioni

### Considerazioni sulla conformità

**Allineamento normativo**
- Progetta applicazioni conformi a GDPR, HIPAA e altri requisiti normativi
- Implementa registrazione audit per processi decisionali AI
- Fornisci funzionalità di trasparenza per risultati generati dall'AI
- Abilita il controllo utente sull'elaborazione dei dati AI

**Sicurezza aziendale**
- Integra con le politiche di sicurezza aziendale di Windows
- Supporta distribuzione gestita tramite strumenti di gestione aziendale
- Implementa controlli di accesso basati sui ruoli per funzionalità AI
- Fornisci controlli amministrativi per funzionalità AI

## Risoluzione dei problemi e debug

### Sfide comuni nello sviluppo

**Problemi di configurazione build**
- Assicurati della configurazione della piattaforma ARM64 per esempi API Windows AI
- Verifica la compatibilità della versione di Windows App SDK (richiesta 1.8.1+)
- Controlla che l'identità del pacchetto sia configurata correttamente (necessaria per API Windows AI)
- Valida che gli strumenti di build supportino la versione del framework target

**Problemi di caricamento modelli**
- Valida la compatibilità dei modelli ONNX con Windows ML
- Controlla l'integrità dei file modello e i requisiti di formato
- Verifica i requisiti di capacità hardware per modelli specifici
- Debugga problemi di allocazione memoria durante il caricamento dei modelli
- Assicurati della registrazione del provider di esecuzione per accelerazione hardware

**Considerazioni sulla modalità di distribuzione**
- **Modalità self-contained**: Completamente supportata con dimensioni di distribuzione maggiori
- **Modalità framework-dependent**: Ingombro minore ma richiede runtime condiviso
- **Applicazioni non confezionate**: Non più supportate per API Windows AI
- Usa `dotnet run -p:Platform=ARM64 -p:SelfContained=true` per distribuzione self-contained ARM64

**Problemi di prestazioni**
- Profila le prestazioni dell'applicazione su diverse configurazioni hardware
- Identifica colli di bottiglia nei pipeline di elaborazione AI
- Ottimizza operazioni di preprocessing e postprocessing dei dati
- Implementa monitoraggio delle prestazioni e avvisi

**Difficoltà di integrazione**
- Debugga problemi di integrazione API con gestione degli errori adeguata
- Valida formati di dati di input e requisiti di preprocessing
- Testa casi limite e condizioni di errore in modo approfondito
- Implementa logging completo per debug di problemi in produzione

### Strumenti e tecniche di debug

**Integrazione Visual Studio**
- Usa il debugger AI Toolkit per analisi dell'esecuzione dei modelli
- Implementa profilazione delle prestazioni per operazioni AI
- Debugga operazioni AI asincrone con gestione delle eccezioni adeguata
- Usa strumenti di profilazione della memoria per ottimizzazione

**Strumenti Windows AI Foundry**
- Sfrutta il CLI di Foundry Local per test e validazione dei modelli
- Usa strumenti di test API Windows AI per verifica dell'integrazione
- Implementa logging personalizzato per monitoraggio delle operazioni AI
- Crea test automatizzati per affidabilità delle funzionalità AI

## Preparare le applicazioni per il futuro

### Tecnologie emergenti

**Hardware di nuova generazione**
- Progetta applicazioni per sfruttare le future capacità NPU
- Pianifica per modelli di dimensioni e complessità crescenti
- Implementa architetture adattive per hardware in evoluzione
- Considera algoritmi pronti per il quantum per compatibilità futura

**Capacità AI avanzate**
- Preparati per integrazione AI multimodale su più tipi di dati
- Pianifica per AI collaborativa in tempo reale tra dispositivi multipli
- Progetta per capacità di apprendimento federato
- Considera architetture di intelligenza ibrida edge-cloud

### Apprendimento continuo e adattamento

**Aggiornamenti dei modelli**
- Implementa meccanismi di aggiornamento dei modelli senza interruzioni
- Progetta applicazioni per adattarsi a capacità migliorate dei modelli
- Pianifica per compatibilità retroattiva con modelli esistenti
- Implementa test A/B per valutazione delle prestazioni dei modelli

**Evoluzione delle funzionalità**
- Progetta architetture modulari che supportino nuove capacità AI
- Pianifica per integrazione di API Windows AI emergenti
- Implementa flag di funzionalità per rollout graduale delle capacità
- Progetta interfacce utente che si adattino a funzionalità AI migliorate

## Conclusione

Lo sviluppo AI Edge su Windows rappresenta la convergenza di potenti capacità AI con la piattaforma Windows robusta, sicura e scalabile. Padroneggiando l'ecosistema Windows AI Foundry, gli sviluppatori possono creare applicazioni intelligenti che offrono esperienze utente eccezionali mantenendo i più alti standard di privacy, sicurezza e prestazioni.

La combinazione di API Windows AI, Foundry Local e Windows ML fornisce una base senza pari per costruire la prossima generazione di applicazioni intelligenti su Windows. Mentre l'AI continua a evolversi, la piattaforma Windows garantisce che le tue applicazioni si adattino alle tecnologie emergenti mantenendo compatibilità e prestazioni su un ecosistema hardware Windows diversificato.

Che tu stia costruendo applicazioni consumer, soluzioni aziendali o strumenti specializzati per l'industria, lo sviluppo AI Edge su Windows ti consente di creare esperienze intelligenti, reattive e profondamente integrate che sfruttano il pieno potenziale dei dispositivi moderni Windows.

## Risorse aggiuntive

### Documentazione e apprendimento
- [Documentazione Windows AI Foundry](https://learn.microsoft.com/windows/ai/)
- [Riferimento API Windows AI](https://learn.microsoft.com/windows/ai/apis/)
- [
- [Panoramica di Windows ML](https://learn.microsoft.com/windows/ai/new-windows-ml/overview/)
- [Requisiti di sistema per Windows App SDK](https://docs.microsoft.com/windows/apps/windows-app-sdk/system-requirements)
- [Configurazione dell'ambiente di sviluppo per Windows App SDK](https://docs.microsoft.com/windows/apps/windows-app-sdk/set-up-your-development-environment)
- 

### Repository di esempio e codice
- [Esempi di Windows App SDK - Windows AI Foundry](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsAIFoundry)
- [Esempi di Windows App SDK - Windows ML](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML)
- [Esempi di inferenza ONNX Runtime](https://github.com/microsoft/onnxruntime-inference-examples)
- [Repository di esempi di Windows App SDK](https://github.com/microsoft/WindowsAppSDK-Samples)

### Strumenti di sviluppo
- [Toolkit AI per Visual Studio Code](https://learn.microsoft.com/windows/ai/toolkit/)
- [Galleria di sviluppo AI](https://learn.microsoft.com/windows/ai/ai-dev-gallery/)
- [Esempi di Windows AI](https://learn.microsoft.com/windows/ai/samples/)
- [Strumenti di conversione dei modelli](https://code.visualstudio.com/docs/intelligentapps/modelconversion)

### Supporto tecnico
- [Documentazione di Windows ML](https://learn.microsoft.com/windows/ai/new-windows-ml/overview)
- [Documentazione di ONNX Runtime](https://onnxruntime.ai/docs/)
- [Documentazione di Windows App SDK](https://docs.microsoft.com/windows/apps/windows-app-sdk/)
- [Segnalazione di problemi - Esempi di Windows App SDK](https://github.com/microsoft/WindowsAppSDK-Samples/issues)

### Comunità e supporto
- [Community degli sviluppatori Windows](https://developer.microsoft.com/en-us/windows/)
- [Blog di Windows AI Foundry](https://blogs.windows.com/windowsdeveloper/)
- [Formazione AI su Microsoft Learn](https://learn.microsoft.com/training/browse/?products=windows&subjects=artificial-intelligence)

---

*Questa guida è progettata per evolversi con il rapido avanzamento dell'ecosistema Windows AI. Aggiornamenti regolari garantiscono l'allineamento con le ultime funzionalità della piattaforma e le migliori pratiche di sviluppo.*

[08. Pratica con Microsoft Foundry Local - Toolkit completo per sviluppatori](../Module08/README.md)

---

**Clausola di esclusione della responsabilità**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire l'accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un traduttore umano. Non siamo responsabili per eventuali incomprensioni o interpretazioni errate derivanti dall'uso di questa traduzione.
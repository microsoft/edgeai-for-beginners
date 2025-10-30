<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "78ca68df03ae43371b203ea43d346dec",
  "translation_date": "2025-10-30T12:24:54+00:00",
  "source_file": "CHANGELOG.md",
  "language_code": "it"
}
-->
# Registro delle modifiche

Tutte le modifiche significative a EdgeAI for Beginners sono documentate qui. Questo progetto utilizza voci basate sulla data e lo stile Keep a Changelog (Aggiunto, Modificato, Risolto, Rimosso, Documentazione, Spostato).

## 2025-10-30

### Aggiunto - Miglioramento completo degli agenti AI nel Modulo06
- **Integrazione del Microsoft Agent Framework** (`Module06/01.IntroduceAgent.md`):
  - Sezione completa sul Microsoft Agent Framework per lo sviluppo di agenti pronti per la produzione
  - Modelli di integrazione dettagliati con Foundry Local per il deployment edge
  - Esempi di orchestrazione multi-agente con modelli SLM specializzati
  - Modelli di deployment aziendale con gestione delle risorse e monitoraggio
  - Funzionalità di sicurezza e conformità per sistemi di agenti edge
  - Esempi di implementazione reali (retail, sanità, servizio clienti)

- **Strategie di deployment degli agenti SLM in produzione**:
  - **Foundry Local**: Documentazione completa del runtime AI edge di livello aziendale con installazione, configurazione e modelli di produzione
  - **Ollama**: Deployment migliorato orientato alla comunità con monitoraggio completo e gestione dei modelli
  - **VLLM**: Motore di inferenza ad alte prestazioni con tecniche di ottimizzazione avanzate e funzionalità aziendali
  - Checklist di deployment in produzione e tabelle di confronto per tutte e tre le piattaforme

- **Miglioramenti ai framework SLM ottimizzati per l'edge**:
  - **ONNX Runtime**: Nuova sezione completa per il deployment cross-platform degli agenti SLM
  - Modelli di deployment universali su Windows, Linux, macOS, iOS e Android
  - Opzioni di accelerazione hardware (CPU, GPU, NPU) con rilevamento automatico
  - Funzionalità pronte per la produzione e ottimizzazioni specifiche per gli agenti
  - Esempi di implementazione completi con integrazione del Microsoft Agent Framework

- **Riferimenti e letture aggiuntive**:
  - Libreria di risorse completa con oltre 100 fonti autorevoli
  - Articoli di ricerca fondamentali su agenti AI e Small Language Models
  - Documentazione ufficiale per tutti i principali framework e strumenti
  - Rapporti di settore, analisi di mercato e benchmark tecnici
  - Risorse educative, conferenze e forum della comunità
  - Standard, specifiche e framework di conformità

### Modificato - Modernizzazione dei contenuti del Modulo06
- **Obiettivi di apprendimento migliorati**: Aggiunta la padronanza del Microsoft Agent Framework e delle capacità di deployment edge
- **Focus sulla produzione**: Passaggio da una guida concettuale a una guida pronta per l'implementazione con esempi di produzione
- **Esempi di codice**: Aggiornati tutti gli esempi per utilizzare modelli SDK moderni e best practice
- **Modelli di architettura**: Aggiunte architetture gerarchiche degli agenti e coordinamento edge-to-cloud
- **Ottimizzazione delle prestazioni**: Migliorata con raccomandazioni per la gestione delle risorse e l'auto-scaling

### Documentazione - Miglioramento della struttura del Modulo06
- **Copertura completa del framework degli agenti**: Dai concetti di base al deployment aziendale
- **Strategie di deployment in produzione**: Guide complete per Foundry Local, Ollama e VLLM
- **Ottimizzazione cross-platform**: Aggiunto ONNX Runtime per il deployment universale
- **Libreria di risorse**: Riferimenti estesi per l'apprendimento e l'implementazione continua

### Aggiunto - Aggiornamento della documentazione del Protocollo di Contesto del Modello (MCP) nel Modulo06
- **Modernizzazione dell'introduzione al MCP** (`Module06/03.IntroduceMCP.md`):
  - Aggiornato con le ultime specifiche MCP da modelcontextprotocol.io (versione 2025-06-18)
  - Aggiunta l'analogia ufficiale con USB-C per connessioni standardizzate delle applicazioni AI
  - Sezione sull'architettura aggiornata con il design ufficiale a due livelli (Data Layer + Transport Layer)
  - Documentazione migliorata sui primitivi principali con primitivi server (Tools, Resources, Prompts) e primitivi client (Sampling, Elicitation, Logging)

- **Riferimenti e risorse complete sul MCP**:
  - Aggiunto il link **MCP for Beginners** (https://aka.ms/mcp-for-beginners)
  - Documentazione e specifiche ufficiali del MCP (modelcontextprotocol.io)
  - Risorse di sviluppo inclusi MCP Inspector e implementazioni di riferimento
  - Standard tecnici (JSON-RPC 2.0, JSON Schema, OpenAPI, Server-Sent Events)

### Aggiunto - Integrazione Qualcomm QNN nel Modulo04
- **Nuova Sezione 7: Suite di ottimizzazione Qualcomm QNN** (`Module04/05.QualcommQNN.md`):
  - Guida completa di oltre 400 righe che copre il framework unificato di inferenza AI di Qualcomm
  - Copertura dettagliata del calcolo eterogeneo (Hexagon NPU, Adreno GPU, Kryo CPU)
  - Ottimizzazione hardware-aware per piattaforme Snapdragon con distribuzione intelligente del carico di lavoro
  - Tecniche avanzate di quantizzazione (INT8, INT16, precisione mista) per il deployment mobile
  - Ottimizzazione dell'inferenza efficiente dal punto di vista energetico per dispositivi alimentati a batteria e applicazioni in tempo reale
  - Guida completa all'installazione con configurazione dell'ambiente e setup del QNN SDK
  - Esempi pratici: conversione da PyTorch a QNN, ottimizzazione multi-backend, generazione di binari di contesto
  - Modelli di utilizzo avanzati: configurazione del backend personalizzato, quantizzazione dinamica, profilazione delle prestazioni
  - Sezione completa di risoluzione dei problemi e risorse della comunità

- **Struttura migliorata del Modulo04**:
  - README.md aggiornato per includere 7 sezioni progressive (prima erano 6)
  - Aggiunto Qualcomm QNN alla tabella dei benchmark delle prestazioni (miglioramento della velocità 5-15x, riduzione della memoria 50-80%)
  - Risultati di apprendimento completi per il deployment AI mobile e l'ottimizzazione energetica

### Modificato - Aggiornamenti alla documentazione del Modulo04
- **Miglioramento della documentazione di Microsoft Olive** (`Module04/03.MicrosoftOlive.md`):
  - Aggiunta una sezione completa "Olive Recipes Repository" che copre oltre 100 ricette di ottimizzazione predefinite
  - Copertura dettagliata delle famiglie di modelli supportate (Phi, Llama, Qwen, Gemma, Mistral, DeepSeek)
  - Esempi pratici di personalizzazione delle ricette e contributi della comunità
  - Migliorata con benchmark delle prestazioni e guida all'integrazione

- **Riordino delle sezioni nel Modulo04**:
  - Apple MLX spostato alla Sezione 5 (prima era la Sezione 6)
  - Sintesi del workflow spostata alla Sezione 6 (prima era la Sezione 7)
  - Qualcomm QNN posizionato come Sezione 7 (focus mobile/edge specializzato)
  - Aggiornati tutti i riferimenti ai file e i link di navigazione di conseguenza

### Risolto - Validazione dei campioni del workshop
- **Validazione e riparazione di chat_bootstrap.py**:
  - Risolto il problema con l'istruzione di importazione corrotta (`util.util.workshop_utils` → `util.workshop_utils`)
  - Creato il file mancante `__init__.py` nel pacchetto util per una corretta risoluzione del modulo Python
  - Installate le dipendenze richieste (openai, foundry-local-sdk) nell'ambiente conda
  - Validata con successo l'esecuzione del campione con prompt predefiniti e personalizzati
  - Confermata l'integrazione con il servizio Foundry Local e il caricamento del modello (phi-4-mini con ottimizzazione CUDA)

### Documentazione - Aggiornamenti completi delle guide
- **Ristrutturazione completa di README.md del Modulo04**:
  - Aggiunto Qualcomm QNN come framework di ottimizzazione principale insieme a OpenVINO, Olive, MLX
  - Aggiornati gli obiettivi di apprendimento del capitolo per includere il deployment AI mobile e l'ottimizzazione energetica
  - Migliorata la tabella di confronto delle prestazioni con metriche QNN e casi d'uso mobile/edge
  - Mantenuta la progressione logica dalle soluzioni aziendali alle ottimizzazioni specifiche per piattaforma

- **Riferimenti incrociati e navigazione**:
  - Aggiornati tutti i link interni e i riferimenti ai file per la nuova numerazione delle sezioni
  - Migliorata la descrizione della sintesi del workflow per includere ambienti mobile, desktop e cloud
  - Aggiunti link completi alle risorse per l'ecosistema degli sviluppatori Qualcomm

## 2025-10-08

### Aggiunto - Aggiornamento completo del workshop
- **Riscrittura completa di README.md del workshop**:
  - Aggiunta un'introduzione completa che spiega la proposta di valore di Edge AI (privacy, prestazioni, costi)
  - Creati 6 obiettivi di apprendimento principali con competenze dettagliate
  - Aggiunta una tabella dei risultati di apprendimento con deliverable e matrice delle competenze
  - Inclusa una sezione sulle competenze pronte per il lavoro per la rilevanza nel settore
  - Aggiunta una guida rapida con prerequisiti e configurazione in 3 passaggi
  - Create tabelle delle risorse per i campioni Python (8 file con tempi di esecuzione)
  - Aggiunta una tabella dei notebook Jupyter (8 notebook con valutazioni di difficoltà)
  - Creata una tabella della documentazione (7 documenti chiave con guida "Quando usare")
  - Aggiunte raccomandazioni sui percorsi di apprendimento per diversi livelli di competenza

- **Infrastruttura di validazione e test del workshop**:
  - Creato `scripts/validate_samples.py` - Strumento di validazione completo per sintassi, importazioni e best practice
  - Creato `scripts/test_samples.py` - Runner di test preliminari per tutti i campioni Python
  - Aggiunta documentazione di validazione a `scripts/README.md`

- **Documentazione completa**:
  - Creato `SAMPLES_UPDATE_SUMMARY.md` - Guida dettagliata di oltre 400 righe che copre tutti i miglioramenti
  - Creato `UPDATE_COMPLETE.md` - Sintesi esecutiva del completamento dell'aggiornamento
  - Creato `QUICK_REFERENCE.md` - Scheda di riferimento rapido per il workshop

### Modificato - Modernizzazione dei campioni Python del workshop
- **Tutti gli 8 campioni Python aggiornati con best practice**:
  - Migliorata la gestione degli errori con blocchi try-except attorno a tutte le operazioni di I/O
  - Aggiunti suggerimenti sui tipi e docstring completi
  - Implementato un modello di logging coerente [INFO]/[ERROR]/[RESULT]
  - Protette le importazioni opzionali con suggerimenti per l'installazione
  - Migliorato il feedback per l'utente in tutti i campioni

- **session01/chat_bootstrap.py**:
  - Migliorata l'inizializzazione del client con messaggi di errore completi
  - Migliorata la gestione degli errori di streaming con la validazione dei chunk
  - Aggiunta una gestione migliore delle eccezioni per l'indisponibilità del servizio

- **session02/rag_pipeline.py**:
  - Aggiunte protezioni per l'importazione di sentence-transformers con suggerimenti per l'installazione
  - Migliorata la gestione degli errori per le operazioni di embedding e generazione
  - Migliorata la formattazione dell'output con risultati strutturati

- **session02/rag_eval_ragas.py**:
  - Protette le importazioni opzionali (ragas, datasets) con messaggi di errore user-friendly
  - Aggiunta gestione degli errori per le metriche di valutazione
  - Migliorata la formattazione dell'output per i risultati della valutazione

- **session03/benchmark_oss_models.py**:
  - Implementata la degradazione graduale (continua in caso di fallimento dei modelli)
  - Aggiunta una reportistica dettagliata dei progressi e gestione degli errori per modello
  - Migliorato il calcolo delle statistiche con un recupero completo dagli errori

- **session04/model_compare.py**:
  - Aggiunti suggerimenti sui tipi (tipi di ritorno Tuple)
  - Migliorata la formattazione dell'output con risultati JSON strutturati
  - Implementata la gestione degli errori per modello con recupero

- **session05/agents_orchestrator.py**:
  - Migliorata Agent.act() con docstring completi
  - Aggiunta gestione degli errori della pipeline con logging fase per fase
  - Migliorata la gestione della memoria e il tracciamento dello stato

- **session06/models_router.py**:
  - Migliorata la documentazione delle funzioni per tutti i componenti di routing
  - Aggiunto logging dettagliato nella funzione route()
  - Migliorato l'output dei test con risultati strutturati

- **session06/models_pipeline.py**:
  - Aggiunta gestione degli errori alla funzione helper chat()
  - Migliorata pipeline() con logging delle fasi e reportistica dei progressi
  - Migliorata main() con recupero completo dagli errori

### Documentazione - Miglioramento della documentazione del workshop
- Aggiornato il README.md principale con una sezione sul workshop che evidenzia il percorso di apprendimento pratico
- Migliorato STUDY_GUIDE.md con una sezione completa sul workshop che include:
  - Obiettivi di apprendimento e aree di focus dello studio
  - Domande di autovalutazione
  - Esercizi pratici con stime di tempo
  - Allocazione del tempo per studio concentrato e part-time
  - Aggiunto il workshop al modello di tracciamento dei progressi
- Aggiornata la guida all'allocazione del tempo da 20 ore a 30 ore (incluso il workshop)
- Aggiunte descrizioni dei campioni del workshop e risultati di apprendimento al README

### Risolto
- Risolti modelli di gestione degli errori incoerenti nei campioni del workshop
- Risolti errori di importazione delle dipendenze opzionali con protezioni adeguate
- Corrette le mancanze di suggerimenti sui tipi nelle funzioni critiche
- Affrontato il feedback insufficiente per l'utente negli scenari di errore
- Risolti problemi di validazione con un'infrastruttura di test completa

---

## 2025-09-23

### Modificato - Modernizzazione principale del Modulo 08
- **Allineamento completo con i modelli del repository Microsoft Foundry-Local**
  - Aggiornati tutti gli esempi di codice per utilizzare i moderni `FoundryLocalManager` e l'integrazione SDK OpenAI
  - Sostituiti le chiamate manuali deprecate `requests` con l'uso corretto dell'SDK
  - Allineati i modelli di implementazione con la documentazione ufficiale Microsoft e i campioni

- **Modernizzazione di 05.AIPoweredAgents.md**:
  - Aggiornata l'orchestrazione multi-agente per utilizzare modelli SDK moderni
  - Migliorata l'implementazione del coordinatore con funzionalità avanzate (cicli di feedback, monitoraggio delle prestazioni)
  - Aggiunta gestione completa degli errori e controllo della salute del servizio
  - Integrati riferimenti adeguati ai campioni locali (`samples/05/multi_agent_orchestration.ipynb`)
  - Aggiornati gli esempi di chiamata delle funzioni per utilizzare il moderno parametro `tools` invece del deprecato `functions`
  - Aggiunti modelli pronti per la produzione con monitoraggio e tracciamento delle statistiche

- **Riscrittura completa di 06.ModelsAsTools.md**:
  - Sostituito il registro degli strumenti di base con un'implementazione intelligente del router dei modelli
  - Aggiunta selezione dei modelli basata su parole chiave per diversi tipi di attività (generale, ragionamento, codice, creativo)
  - Integrata configurazione basata sull'ambiente con assegnazione flessibile dei modelli
  - Migliorata con monitoraggio completo della salute del servizio e gestione degli errori
  - Aggiunti modelli di deployment in produzione con monitoraggio delle richieste e tracciamento delle prestazioni
  - Allineati con l'implementazione locale in `samples/06/router.py` e `samples/06/model_router.ipynb`

- **Miglioramenti alla struttura della documentazione**:
  - Aggiunte sezioni panoramiche che evidenziano la modernizzazione e l'allineamento SDK
  - Migliorata con emoji e formattazione migliore per una maggiore leggibilità
  - Aggiunti riferimenti adeguati ai file di campioni locali in tutta la documentazione
  - Inclusa guida all'implementazione pronta per la produzione e best practice

### Aggiunto
- Sezioni panoramiche complete nei file del Modulo 08 che evidenziano l'integrazione SDK moderna
- Punti salienti dell'architettura che mostrano funzionalità avanzate (sistemi multi-agente, routing intelligente)
- Riferimenti diretti
  - Esempi eseguibili sotto `Module08/samples/01`–`06` con istruzioni cmd di Windows
    - `01` REST chat rapido (`chat_quickstart.py`)
    - `02` SDK quickstart con supporto OpenAI/Foundry Local e Azure OpenAI (`sdk_quickstart.py`)
    - `03` CLI elenco e benchmark (`list_and_bench.cmd`)
    - `04` Demo Chainlit (`app.py`)
    - `05` Orchestrazione multi-agente (`python -m samples.05.agents.coordinator`)
    - `06` Router Models-as-Tools (`router.py`)
- Supporto Azure OpenAI nella sessione 2 del campione SDK con configurazione delle variabili d'ambiente
- `.vscode/settings.json` per puntare a `Module08/.venv` e migliorare la risoluzione dell'analisi Python
- `.env` con suggerimento `PYTHONPATH` per la consapevolezza di VS Code/Pylance

### Modificato
- Modello predefinito aggiornato a `phi-4-mini` in tutta la documentazione e gli esempi del Modulo 08; rimosse le menzioni rimanenti di `phi-3.5` all'interno del Modulo 08
- Miglioramenti al router (`Module08/samples/06/router.py`):
  - Scoperta degli endpoint tramite `foundry service status` con analisi regex
  - Controllo dello stato di `/v1/models` all'avvio
  - Registro modelli configurabile tramite variabili d'ambiente (`GENERAL_MODEL`, `REASONING_MODEL`, `CODE_MODEL`, `TOOL_REGISTRY` JSON)
- Requisiti aggiornati: `Module08/requirements.txt` ora include `openai` (insieme a `requests`, `chainlit`)
- Chiarimenti sulle indicazioni per l'esempio Chainlit e aggiunta di risoluzione dei problemi; risoluzione degli import tramite impostazioni del workspace

### Risolto
- Risolti problemi di importazione:
  - Il router non dipende più da un modulo `utils` inesistente; le funzioni sono state integrate
  - Il coordinatore utilizza l'importazione relativa (`from .specialists import ...`) ed è invocato tramite il percorso del modulo
  - Configurazione di VS Code/Pylance per risolvere gli import `chainlit` e dei pacchetti
- Corretto un piccolo errore di battitura in `STUDY_GUIDE.md` e aggiunta la copertura del Modulo 08

### Rimosso
- Eliminato `Module08/infra/obs.py` non utilizzato e rimossa la directory vuota `infra/`; i pattern di osservabilità sono mantenuti come opzionali nella documentazione

### Spostato
- Consolidati i demo del Modulo 08 sotto `Module08/samples` con cartelle numerate per sessione
  - Spostata l'app Chainlit in `samples/04`
  - Spostati gli agenti in `samples/05` e aggiunti file `__init__.py` per la risoluzione dei pacchetti

### Documentazione
- Documentazione della sessione del Modulo 08 e tutti i README degli esempi arricchiti con riferimenti a Microsoft Learn e fornitori affidabili
- `Module08/README.md` aggiornato con Panoramica degli Esempi, configurazione del router e suggerimenti per la validazione
- Sezione Foundry Local di Windows in `Module07/README.md` validata rispetto alla documentazione Learn
- `STUDY_GUIDE.md` aggiornato:
  - Aggiunto il Modulo 08 alla panoramica, ai programmi, al tracker di progresso
  - Aggiunta una sezione di Riferimenti completa (Foundry Local, Azure AI, Olive, ONNX Runtime, OpenVINO, MLX, Llama.cpp, vLLM, Ollama, AI Toolkit, Windows ML)

---

## Storico (sommario)
- Architettura del corso e moduli stabiliti (Moduli 01–07)
- Modernizzazione iterativa dei contenuti, standardizzazione della formattazione e aggiunta di casi studio
- Espansione della copertura dei framework di ottimizzazione (Llama.cpp, Olive, OpenVINO, Apple MLX)

## Non rilasciato / Backlog (proposte)
- Test opzionali per ogni esempio per convalidare la disponibilità di Foundry Local
- Revisione delle traduzioni per allineare i riferimenti ai modelli (es. `phi-4-mini`) dove appropriato
- Aggiungere una configurazione minima di pyright se i team preferiscono una severità a livello di workspace

---

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire l'accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si consiglia una traduzione professionale umana. Non siamo responsabili per eventuali incomprensioni o interpretazioni errate derivanti dall'uso di questa traduzione.
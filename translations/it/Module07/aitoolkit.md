# Toolkit AI per Visual Studio Code - Guida allo sviluppo di Edge AI

## Introduzione

Benvenuto nella guida completa per l'utilizzo del Toolkit AI per Visual Studio Code nello sviluppo di Edge AI. Con l'intelligenza artificiale che si sposta dal cloud centralizzato ai dispositivi edge distribuiti, gli sviluppatori necessitano di strumenti potenti e integrati per affrontare le sfide uniche del deployment edge, come i vincoli di risorse e i requisiti di funzionamento offline.

Il Toolkit AI per Visual Studio Code colma questa lacuna fornendo un ambiente di sviluppo completo, progettato specificamente per costruire, testare e ottimizzare applicazioni AI che funzionano in modo efficiente sui dispositivi edge. Che tu stia sviluppando per sensori IoT, dispositivi mobili, sistemi embedded o server edge, questo toolkit semplifica l'intero flusso di lavoro di sviluppo all'interno dell'ambiente familiare di VS Code.

Questa guida ti accompagnerà attraverso i concetti essenziali, gli strumenti e le migliori pratiche per sfruttare il Toolkit AI nei tuoi progetti Edge AI, dalla selezione iniziale del modello al deployment in produzione.

## Panoramica

Il Toolkit AI per Visual Studio Code è un'estensione potente che semplifica lo sviluppo di agenti e la creazione di applicazioni AI. Il toolkit offre capacità complete per esplorare, valutare e distribuire modelli AI da una vasta gamma di fornitori—tra cui Anthropic, OpenAI, GitHub, Google—supportando al contempo l'esecuzione locale dei modelli utilizzando ONNX e Ollama.

Ciò che distingue il Toolkit AI è il suo approccio completo all'intero ciclo di vita dello sviluppo AI. A differenza degli strumenti tradizionali che si concentrano su singoli aspetti, il Toolkit AI fornisce un ambiente integrato che copre la scoperta dei modelli, la sperimentazione, lo sviluppo di agenti, la valutazione e il deployment—tutto all'interno dell'ambiente familiare di VS Code.

La piattaforma è progettata specificamente per il prototipaggio rapido e il deployment in produzione, con funzionalità come la generazione di prompt, avvii rapidi, integrazioni fluide con MCP (Model Context Protocol) e ampie capacità di valutazione. Per lo sviluppo Edge AI, questo significa che puoi sviluppare, testare e ottimizzare applicazioni AI per scenari di deployment edge in modo efficiente, mantenendo l'intero flusso di lavoro di sviluppo all'interno di VS Code.

## Obiettivi di apprendimento

Alla fine di questa guida, sarai in grado di:

### Competenze principali
- **Installare e configurare** il Toolkit AI per Visual Studio Code per flussi di lavoro di sviluppo Edge AI
- **Navigare e utilizzare** l'interfaccia del Toolkit AI, inclusi Catalogo Modelli, Playground e Costruttore di Agenti
- **Selezionare e valutare** modelli AI adatti al deployment edge in base a prestazioni e vincoli di risorse
- **Convertire e ottimizzare** modelli utilizzando il formato ONNX e tecniche di quantizzazione per dispositivi edge

### Competenze nello sviluppo Edge AI
- **Progettare e implementare** applicazioni Edge AI utilizzando l'ambiente di sviluppo integrato
- **Eseguire test sui modelli** in condizioni simili a quelle edge utilizzando inferenza locale e monitoraggio delle risorse
- **Creare e personalizzare** agenti AI ottimizzati per scenari di deployment edge
- **Valutare le prestazioni dei modelli** utilizzando metriche rilevanti per il computing edge (latenza, utilizzo della memoria, accuratezza)

### Ottimizzazione e deployment
- **Applicare tecniche di quantizzazione e pruning** per ridurre la dimensione dei modelli mantenendo prestazioni accettabili
- **Ottimizzare i modelli** per piattaforme hardware edge specifiche, inclusa l'accelerazione CPU, GPU e NPU
- **Implementare le migliori pratiche** per lo sviluppo Edge AI, inclusa la gestione delle risorse e strategie di fallback
- **Preparare modelli e applicazioni** per il deployment in produzione su dispositivi edge

### Concetti avanzati di Edge AI
- **Integrare con framework Edge AI** tra cui ONNX Runtime, Windows ML e TensorFlow Lite
- **Implementare architetture multi-modello** e scenari di apprendimento federato per ambienti edge
- **Risolvere problemi comuni di Edge AI** tra cui vincoli di memoria, velocità di inferenza e compatibilità hardware
- **Progettare strategie di monitoraggio e logging** per applicazioni Edge AI in produzione

### Applicazione pratica
- **Costruire soluzioni Edge AI end-to-end** dalla selezione del modello al deployment
- **Dimostrare competenza** nei flussi di lavoro di sviluppo specifici per edge e tecniche di ottimizzazione
- **Applicare i concetti appresi** a casi d'uso reali di Edge AI, inclusi IoT, mobile e applicazioni embedded
- **Valutare e confrontare** diverse strategie di deployment Edge AI e i loro compromessi

## Caratteristiche principali per lo sviluppo Edge AI

### 1. Catalogo Modelli e Scoperta
- **Supporto multi-fornitore**: Sfoglia e accedi a modelli AI da Anthropic, OpenAI, GitHub, Google e altri fornitori
- **Integrazione modelli locali**: Scoperta semplificata di modelli ONNX e Ollama per il deployment edge
- **Modelli GitHub**: Integrazione diretta con l'hosting di modelli di GitHub per un accesso semplificato
- **Confronto modelli**: Confronta i modelli fianco a fianco per trovare il miglior equilibrio per i vincoli dei dispositivi edge

### 2. Playground Interattivo
- **Ambiente di test interattivo**: Sperimentazione rapida con le capacità dei modelli in un ambiente controllato
- **Supporto multi-modale**: Testa con immagini, testo e altri input tipici negli scenari edge
- **Sperimentazione in tempo reale**: Feedback immediato sulle risposte e prestazioni dei modelli
- **Ottimizzazione dei parametri**: Affina i parametri dei modelli per i requisiti di deployment edge

### 3. Costruttore di Prompt (Agenti)
- **Generazione di linguaggio naturale**: Genera prompt iniziali utilizzando descrizioni in linguaggio naturale
- **Raffinamento iterativo**: Migliora i prompt in base alle risposte e alle prestazioni dei modelli
- **Decomposizione dei compiti**: Suddividi compiti complessi con concatenazione di prompt e output strutturati
- **Supporto variabili**: Usa variabili nei prompt per comportamenti dinamici degli agenti
- **Generazione di codice di produzione**: Genera codice pronto per la produzione per uno sviluppo rapido delle app

### 4. Esecuzione e Valutazione in Massa
- **Test multi-modello**: Esegui più prompt su modelli selezionati simultaneamente
- **Test efficiente su larga scala**: Testa vari input e configurazioni in modo efficiente
- **Casi di test personalizzati**: Esegui agenti con casi di test per convalidare la funzionalità
- **Confronto delle prestazioni**: Confronta i risultati tra diversi modelli e configurazioni

### 5. Valutazione dei Modelli con Dataset
- **Metriche standard**: Testa i modelli AI utilizzando valutatori integrati (F1 score, rilevanza, somiglianza, coerenza)
- **Valutatori personalizzati**: Crea metriche di valutazione personalizzate per casi d'uso specifici
- **Integrazione dataset**: Testa i modelli contro dataset completi
- **Misurazione delle prestazioni**: Quantifica le prestazioni dei modelli per decisioni di deployment edge

### 6. Capacità di Fine-tuning
- **Personalizzazione dei modelli**: Personalizza i modelli per casi d'uso e domini specifici
- **Adattamento specializzato**: Adatta i modelli a domini e requisiti specializzati
- **Ottimizzazione edge**: Affina i modelli specificamente per i vincoli di deployment edge
- **Training specifico per il dominio**: Crea modelli su misura per casi d'uso edge specifici

### 7. Integrazione con Strumenti MCP
- **Connettività con strumenti esterni**: Collega agenti a strumenti esterni tramite server Model Context Protocol
- **Azioni reali**: Consenti agli agenti di interrogare database, accedere a API o eseguire logiche personalizzate
- **Server MCP esistenti**: Usa strumenti da protocolli di comando (stdio) o HTTP (eventi inviati dal server)
- **Sviluppo MCP personalizzato**: Costruisci e struttura nuovi server MCP con test nel Costruttore di Agenti

### 8. Sviluppo e Test degli Agenti
- **Supporto chiamata funzioni**: Consenti agli agenti di invocare funzioni esterne dinamicamente
- **Test di integrazione in tempo reale**: Testa integrazioni con esecuzioni in tempo reale e utilizzo degli strumenti
- **Versionamento degli agenti**: Controllo delle versioni per agenti con capacità di confronto dei risultati di valutazione
- **Debugging e tracing**: Capacità di tracing e debugging locale per lo sviluppo degli agenti

## Flusso di lavoro per lo sviluppo Edge AI

### Fase 1: Scoperta e Selezione dei Modelli
1. **Esplora il Catalogo Modelli**: Usa il catalogo modelli per trovare modelli adatti al deployment edge
2. **Confronta le prestazioni**: Valuta i modelli in base a dimensioni, accuratezza e velocità di inferenza
3. **Testa localmente**: Usa modelli Ollama o ONNX per testare localmente prima del deployment edge
4. **Valuta i requisiti di risorse**: Determina le esigenze di memoria e calcolo per i dispositivi edge target

### Fase 2: Ottimizzazione dei Modelli
1. **Converti in ONNX**: Converti i modelli selezionati nel formato ONNX per la compatibilità edge
2. **Applica la quantizzazione**: Riduci la dimensione dei modelli tramite quantizzazione INT8 o INT4
3. **Ottimizzazione hardware**: Ottimizza per hardware edge target (ARM, x86, acceleratori specializzati)
4. **Validazione delle prestazioni**: Valida che i modelli ottimizzati mantengano un'accuratezza accettabile

### Fase 3: Sviluppo delle Applicazioni
1. **Progettazione degli agenti**: Usa il Costruttore di Agenti per creare agenti AI ottimizzati per edge
2. **Ingegneria dei prompt**: Sviluppa prompt che funzionano efficacemente con modelli edge più piccoli
3. **Test di integrazione**: Testa gli agenti in condizioni simulate edge
4. **Generazione di codice**: Genera codice di produzione ottimizzato per il deployment edge

### Fase 4: Valutazione e Test
1. **Valutazione in batch**: Testa più configurazioni per trovare le impostazioni edge ottimali
2. **Profilazione delle prestazioni**: Analizza velocità di inferenza, utilizzo della memoria e accuratezza
3. **Simulazione edge**: Testa in condizioni simili all'ambiente di deployment edge target
4. **Test di stress**: Valuta le prestazioni sotto varie condizioni di carico

### Fase 5: Preparazione al Deployment
1. **Ottimizzazione finale**: Applica ottimizzazioni finali basate sui risultati dei test
2. **Packaging per il deployment**: Prepara modelli e codice per il deployment edge
3. **Documentazione**: Documenta i requisiti e la configurazione del deployment
4. **Configurazione del monitoraggio**: Prepara il monitoraggio e il logging per il deployment edge

## Pubblico target per lo sviluppo Edge AI

### Sviluppatori Edge AI
- Sviluppatori di applicazioni che costruiscono dispositivi edge e soluzioni IoT basate su AI
- Sviluppatori di sistemi embedded che integrano capacità AI in dispositivi con vincoli di risorse
- Sviluppatori mobili che creano applicazioni AI on-device per smartphone e tablet

### Ingegneri Edge AI
- Ingegneri AI che ottimizzano modelli per il deployment edge e gestiscono pipeline di inferenza
- Ingegneri DevOps che distribuiscono e gestiscono modelli AI su infrastrutture edge distribuite
- Ingegneri delle prestazioni che ottimizzano carichi di lavoro AI per vincoli hardware edge

### Ricercatori ed Educatori
- Ricercatori AI che sviluppano modelli e algoritmi efficienti per il computing edge
- Educatori che insegnano concetti Edge AI e dimostrano tecniche di ottimizzazione
- Studenti che apprendono le sfide e le soluzioni nel deployment Edge AI

## Casi d'uso di Edge AI

### Dispositivi IoT intelligenti
- **Riconoscimento immagini in tempo reale**: Distribuzione di modelli di visione artificiale su telecamere e sensori IoT
- **Elaborazione vocale**: Implementazione di riconoscimento vocale e elaborazione del linguaggio naturale su altoparlanti intelligenti
- **Manutenzione predittiva**: Esecuzione di modelli di rilevamento anomalie su dispositivi edge industriali
- **Monitoraggio ambientale**: Distribuzione di modelli di analisi dei dati dei sensori per applicazioni ambientali

### Applicazioni mobili e embedded
- **Traduzione on-device**: Implementazione di modelli di traduzione linguistica che funzionano offline
- **Realtà aumentata**: Distribuzione di riconoscimento e tracciamento oggetti in tempo reale per applicazioni AR
- **Monitoraggio della salute**: Esecuzione di modelli di analisi della salute su dispositivi indossabili e apparecchiature mediche
- **Sistemi autonomi**: Implementazione di modelli decisionali per droni, robot e veicoli

### Infrastruttura Edge Computing
- **Data center edge**: Distribuzione di modelli AI nei data center edge per applicazioni a bassa latenza
- **Integrazione CDN**: Integrazione di capacità di elaborazione AI nelle reti di distribuzione dei contenuti
- **Edge 5G**: Sfruttamento del computing edge 5G per applicazioni basate su AI
- **Fog Computing**: Implementazione di elaborazione AI in ambienti di fog computing

## Installazione e Configurazione

### Installazione dell'estensione
Installa l'estensione Toolkit AI direttamente dal Visual Studio Code Marketplace:

**ID Estensione**: `ms-windows-ai-studio.windows-ai-studio`

**Metodi di installazione**:
1. **Marketplace di VS Code**: Cerca "Toolkit AI" nella vista Estensioni
2. **Linea di comando**: `code --install-extension ms-windows-ai-studio.windows-ai-studio`
3. **Installazione diretta**: Scarica da [VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)

### Prerequisiti per lo sviluppo Edge AI
- **Visual Studio Code**: Versione più recente consigliata
- **Ambiente Python**: Python 3.8+ con librerie AI richieste
- **ONNX Runtime** (Opzionale): Per inferenza con modelli ONNX
- **Ollama** (Opzionale): Per il servizio locale dei modelli
- **Strumenti di accelerazione hardware**: CUDA, OpenVINO o acceleratori specifici per piattaforma

### Configurazione iniziale
1. **Attivazione dell'estensione**: Apri VS Code e verifica che il Toolkit AI appaia nella Barra delle Attività
2. **Configurazione dei fornitori di modelli**: Configura l'accesso a GitHub, OpenAI, Anthropic o altri fornitori di modelli
3. **Ambiente locale**: Configura l'ambiente Python e installa i pacchetti richiesti
4. **Accelerazione hardware**: Configura l'accelerazione GPU/NPU se disponibile
5. **Integrazione MCP**: Configura server Model Context Protocol se necessario

### Checklist per la configurazione iniziale
- [ ] Estensione Toolkit AI installata e attivata
- [ ] Catalogo modelli accessibile e modelli individuabili
- [ ] Playground funzionante per test sui modelli
- [ ] Costruttore di Agenti accessibile per lo sviluppo di prompt
- [ ] Ambiente di sviluppo locale configurato
- [ ] Accelerazione hardware (se disponibile) configurata correttamente

## Iniziare con il Toolkit AI

### Guida rapida

Consigliamo di iniziare con i modelli ospitati da GitHub per un'esperienza più fluida:

1. **Installazione**: Segui la [guida all'installazione](https://code.visualstudio.com/docs/intelligentapps/overview#_install-and-setup) per configurare il Toolkit AI sul tuo dispositivo
2. **Scoperta dei modelli**: Dalla vista ad albero dell'estensione, seleziona **CATALOG > Models** per esplorare i modelli disponibili
3. **Modelli GitHub**: Inizia con i modelli ospitati da GitHub per un'integrazione ottimale
4. **Test nel Playground**: Da qualsiasi scheda modello, seleziona **Try in Playground** per iniziare a sperimentare le capacità del modello

### Sviluppo Edge AI passo dopo passo

#### Passo 1: Esplorazione e Selezione dei Modelli
1. Apri la vista Toolkit AI nella Barra delle Attività di VS Code
2. Sfoglia il Catalogo Modelli per modelli adatti al deployment edge
3. Filtra per fornitore (GitHub, ONNX, Ollama) in base ai tuoi requisiti edge
4. Usa **Try in Playground** per testare immediatamente le capacità del modello

#### Passo 2: Sviluppo degli Agenti
1. Usa il **Costruttore di Prompt (Agenti)** per
2. Genera prompt iniziali utilizzando descrizioni in linguaggio naturale  
3. Itera e perfeziona i prompt basandoti sulle risposte del modello  
4. Integra gli strumenti MCP per migliorare le capacità degli agenti  

#### Passo 3: Test e Valutazione  
1. Utilizza **Bulk Run** per testare più prompt su modelli selezionati  
2. Esegui gli agenti con casi di test per validare la funzionalità  
3. Valuta accuratezza e prestazioni utilizzando metriche integrate o personalizzate  
4. Confronta diversi modelli e configurazioni  

#### Passo 4: Ottimizzazione e Fine-tuning  
1. Personalizza i modelli per casi d'uso specifici  
2. Applica il fine-tuning specifico per il dominio  
3. Ottimizza per vincoli di distribuzione edge  
4. Versiona e confronta diverse configurazioni di agenti  

#### Passo 5: Preparazione alla Distribuzione  
1. Genera codice pronto per la produzione utilizzando l'Agent Builder  
2. Configura connessioni al server MCP per l'uso in produzione  
3. Prepara pacchetti di distribuzione per dispositivi edge  
4. Configura metriche di monitoraggio e valutazione  

## Esempi per AI Toolkit  

Prova i nostri esempi  
Gli [esempi di AI Toolkit](https://github.com/Azure-Samples/AI_Toolkit_Samples) sono progettati per aiutare sviluppatori e ricercatori a esplorare e implementare soluzioni AI in modo efficace.  

I nostri esempi includono:  

Codice di esempio: esempi predefiniti per dimostrare funzionalità AI, come l'addestramento, la distribuzione o l'integrazione di modelli nelle applicazioni.  
Documentazione: guide e tutorial per aiutare gli utenti a comprendere le funzionalità di AI Toolkit e come utilizzarle.  
Prerequisiti  

- Visual Studio Code  
- AI Toolkit per Visual Studio Code  
- Token di accesso personale (PAT) GitHub Fine-grained  
- Foundry Local  

## Best Practices per lo Sviluppo di Edge AI  

### Selezione del Modello  
- **Vincoli di dimensione**: Scegli modelli che si adattino ai limiti di memoria dei dispositivi target  
- **Velocità di inferenza**: Dai priorità ai modelli con tempi di inferenza rapidi per applicazioni in tempo reale  
- **Compromessi di accuratezza**: Bilancia l'accuratezza del modello con i vincoli di risorse  
- **Compatibilità del formato**: Preferisci formati ONNX o ottimizzati per hardware per la distribuzione edge  

### Tecniche di Ottimizzazione  
- **Quantizzazione**: Utilizza quantizzazione INT8 o INT4 per ridurre la dimensione del modello e migliorare la velocità  
- **Pruning**: Rimuovi parametri del modello non necessari per ridurre i requisiti computazionali  
- **Knowledge Distillation**: Crea modelli più piccoli che mantengano le prestazioni di quelli più grandi  
- **Accelerazione hardware**: Sfrutta NPUs, GPUs o acceleratori specializzati quando disponibili  

### Workflow di Sviluppo  
- **Test iterativi**: Testa frequentemente in condizioni simili a quelle edge durante lo sviluppo  
- **Monitoraggio delle prestazioni**: Monitora continuamente l'uso delle risorse e la velocità di inferenza  
- **Controllo delle versioni**: Tieni traccia delle versioni dei modelli e delle impostazioni di ottimizzazione  
- **Documentazione**: Documenta tutte le decisioni di ottimizzazione e i compromessi di prestazioni  

### Considerazioni sulla Distribuzione  
- **Monitoraggio delle risorse**: Monitora memoria, CPU e consumo energetico in produzione  
- **Strategie di fallback**: Implementa meccanismi di fallback per guasti del modello  
- **Meccanismi di aggiornamento**: Pianifica aggiornamenti del modello e gestione delle versioni  
- **Sicurezza**: Implementa misure di sicurezza adeguate per applicazioni AI edge  

## Integrazione con Framework Edge AI  

### ONNX Runtime  
- **Distribuzione cross-platform**: Distribuisci modelli ONNX su diverse piattaforme edge  
- **Ottimizzazione hardware**: Sfrutta le ottimizzazioni hardware specifiche di ONNX Runtime  
- **Supporto mobile**: Utilizza ONNX Runtime Mobile per applicazioni su smartphone e tablet  
- **Integrazione IoT**: Distribuisci su dispositivi IoT utilizzando distribuzioni leggere di ONNX Runtime  

### Windows ML  
- **Dispositivi Windows**: Ottimizza per dispositivi edge e PC basati su Windows  
- **Accelerazione NPU**: Sfrutta le Neural Processing Units sui dispositivi Windows  
- **DirectML**: Utilizza DirectML per l'accelerazione GPU su piattaforme Windows  
- **Integrazione UWP**: Integra con applicazioni Universal Windows Platform  

### TensorFlow Lite  
- **Ottimizzazione mobile**: Distribuisci modelli TensorFlow Lite su dispositivi mobili e embedded  
- **Delegati hardware**: Utilizza delegati hardware specializzati per l'accelerazione  
- **Microcontrollori**: Distribuisci su microcontrollori utilizzando TensorFlow Lite Micro  
- **Supporto cross-platform**: Distribuisci su Android, iOS e sistemi Linux embedded  

### Azure IoT Edge  
- **Ibrido cloud-edge**: Combina l'addestramento cloud con l'inferenza edge  
- **Distribuzione moduli**: Distribuisci modelli AI come moduli IoT Edge  
- **Gestione dispositivi**: Gestisci dispositivi edge e aggiornamenti dei modelli da remoto  
- **Telemetria**: Raccogli dati sulle prestazioni e metriche dei modelli dalle distribuzioni edge  

## Scenari Avanzati di Edge AI  

### Distribuzione Multi-Modello  
- **Ensemble di modelli**: Distribuisci più modelli per migliorare l'accuratezza o la ridondanza  
- **Test A/B**: Testa diversi modelli simultaneamente su dispositivi edge  
- **Selezione dinamica**: Scegli modelli basati sulle condizioni attuali del dispositivo  
- **Condivisione delle risorse**: Ottimizza l'uso delle risorse tra modelli distribuiti  

### Federated Learning  
- **Addestramento distribuito**: Addestra modelli su più dispositivi edge  
- **Preservazione della privacy**: Mantieni i dati di addestramento locali condividendo solo miglioramenti del modello  
- **Apprendimento collaborativo**: Consenti ai dispositivi di apprendere dalle esperienze collettive  
- **Coordinamento edge-cloud**: Coordina l'apprendimento tra dispositivi edge e infrastruttura cloud  

### Elaborazione in Tempo Reale  
- **Elaborazione di flussi**: Elabora flussi di dati continui su dispositivi edge  
- **Inferenza a bassa latenza**: Ottimizza per una latenza di inferenza minima  
- **Elaborazione batch**: Elabora in modo efficiente batch di dati su dispositivi edge  
- **Elaborazione adattiva**: Adatta l'elaborazione in base alle capacità attuali del dispositivo  

## Risoluzione dei Problemi nello Sviluppo di Edge AI  

### Problemi Comuni  
- **Vincoli di memoria**: Modello troppo grande per la memoria del dispositivo target  
- **Velocità di inferenza**: Inferenza del modello troppo lenta per requisiti in tempo reale  
- **Degradazione dell'accuratezza**: L'ottimizzazione riduce l'accuratezza del modello in modo inaccettabile  
- **Compatibilità hardware**: Modello non compatibile con l'hardware target  

### Strategie di Debug  
- **Profilazione delle prestazioni**: Utilizza le funzionalità di tracciamento di AI Toolkit per identificare i colli di bottiglia  
- **Monitoraggio delle risorse**: Monitora memoria e utilizzo della CPU durante lo sviluppo  
- **Test incrementali**: Testa le ottimizzazioni in modo incrementale per isolare i problemi  
- **Simulazione hardware**: Utilizza strumenti di sviluppo per simulare l'hardware target  

### Soluzioni di Ottimizzazione  
- **Quantizzazione ulteriore**: Applica tecniche di quantizzazione più aggressive  
- **Architettura del modello**: Considera diverse architetture di modelli ottimizzate per edge  
- **Ottimizzazione della pre-elaborazione**: Ottimizza la pre-elaborazione dei dati per i vincoli edge  
- **Ottimizzazione dell'inferenza**: Utilizza ottimizzazioni di inferenza specifiche per hardware  

## Risorse e Prossimi Passi  

### Documentazione Ufficiale  
- [Documentazione per sviluppatori AI Toolkit](https://aka.ms/AIToolkit/doc)  
- [Guida all'installazione e configurazione](https://code.visualstudio.com/docs/intelligentapps/overview#_install-and-setup)  
- [Documentazione di VS Code Intelligent Apps](https://code.visualstudio.com/docs/intelligentapps)  
- [Documentazione del Model Context Protocol (MCP)](https://modelcontextprotocol.io/)  

### Community e Supporto  
- [Repository GitHub di AI Toolkit](https://github.com/microsoft/vscode-ai-toolkit)  
- [Problemi e richieste di funzionalità su GitHub](https://aka.ms/AIToolkit/feedback)  
- [Community Discord di Azure AI Foundry](https://aka.ms/azureaifoundry/discord)  
- [Marketplace delle estensioni di VS Code](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)  

### Risorse Tecniche  
- [Documentazione ONNX Runtime](https://onnxruntime.ai/)  
- [Documentazione Ollama](https://ollama.ai/)  
- [Documentazione Windows ML](https://docs.microsoft.com/en-us/windows/ai/)  
- [Documentazione Azure AI Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/)  

### Percorsi di Apprendimento  
- [Corso Fondamenti di Edge AI](../Module01/README.md)  
- [Guida ai modelli linguistici piccoli](../Module02/README.md)  
- [Strategie di distribuzione edge](../Module03/README.md)  
- [Sviluppo Edge AI su Windows](./windowdeveloper.md)  

### Risorse Aggiuntive  
- **Statistiche del repository**: 1.8k+ stelle, 150+ fork, 18+ collaboratori  
- **Licenza**: Licenza MIT  
- **Sicurezza**: Si applicano le politiche di sicurezza Microsoft  
- **Telemetria**: Rispetta le impostazioni di telemetria di VS Code  

## Conclusione  

AI Toolkit per Visual Studio Code rappresenta una piattaforma completa per lo sviluppo AI moderno, offrendo capacità di sviluppo di agenti semplificate particolarmente utili per le applicazioni di Edge AI. Con il suo ampio catalogo di modelli che supporta fornitori come Anthropic, OpenAI, GitHub e Google, combinato con l'esecuzione locale tramite ONNX e Ollama, il toolkit offre la flessibilità necessaria per scenari di distribuzione edge diversificati.  

La forza del toolkit risiede nel suo approccio integrato—dalla scoperta e sperimentazione dei modelli nel Playground allo sviluppo sofisticato di agenti con il Prompt Builder, capacità di valutazione complete e integrazione senza soluzione di continuità degli strumenti MCP. Per gli sviluppatori di Edge AI, questo significa prototipazione rapida e test di agenti AI prima della distribuzione edge, con la possibilità di iterare rapidamente e ottimizzare per ambienti con risorse limitate.  

Vantaggi chiave per lo sviluppo di Edge AI includono:  
- **Sperimentazione rapida**: Testa modelli e agenti rapidamente prima di impegnarti nella distribuzione edge  
- **Flessibilità multi-fornitore**: Accedi a modelli da varie fonti per trovare soluzioni edge ottimali  
- **Sviluppo locale**: Testa con ONNX e Ollama per sviluppo offline e rispettoso della privacy  
- **Prontezza per la produzione**: Genera codice pronto per la produzione e integra con strumenti esterni tramite MCP  
- **Valutazione completa**: Utilizza metriche integrate e personalizzate per validare le prestazioni AI edge  

Man mano che l'AI continua a spostarsi verso scenari di distribuzione edge, AI Toolkit per VS Code fornisce l'ambiente di sviluppo e il workflow necessari per costruire, testare e ottimizzare applicazioni intelligenti per ambienti con risorse limitate. Che tu stia sviluppando soluzioni IoT, applicazioni AI mobili o sistemi di intelligenza embedded, il set completo di funzionalità del toolkit e il workflow integrato supportano l'intero ciclo di vita dello sviluppo di Edge AI.  

Con uno sviluppo continuo e una community attiva (1.8k+ stelle su GitHub), AI Toolkit rimane all'avanguardia degli strumenti di sviluppo AI, evolvendosi costantemente per soddisfare le esigenze degli sviluppatori AI moderni che lavorano su scenari di distribuzione edge.  

[Prossimo Foundry Local](./foundrylocal.md)  

---

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire l'accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale umana. Non siamo responsabili per eventuali incomprensioni o interpretazioni errate derivanti dall'uso di questa traduzione.
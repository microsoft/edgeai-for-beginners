# Workshop Notebooks

> **Notebook interattivi Jupyter per l'apprendimento pratico dell'Edge AI**
>
> Tutorial progressivi e autogestiti che vanno dalle basi delle completazioni di chat ai sistemi multi-agente avanzati utilizzando Microsoft Foundry Local e Small Language Models.

---

## 📖 Introduzione

Benvenuto nella collezione di **EdgeAI for Beginners Workshop Notebooks**. Questi notebook interattivi Jupyter offrono un'esperienza di apprendimento pratico in cui potrai scrivere, eseguire ed esperimentare codice Edge AI in tempo reale.

### Perché Jupyter Notebooks?

A differenza dei tutorial tradizionali, questi notebook offrono:

- **Apprendimento interattivo**: Esegui celle di codice e osserva i risultati immediatamente
- **Sperimentazione**: Modifica i parametri e osserva i cambiamenti in tempo reale
- **Documentazione**: Spiegazioni inline e celle markdown ti guidano attraverso i concetti
- **Riproducibilità**: Esempi completi e funzionanti che puoi consultare e riutilizzare
- **Visualizzazione**: Visualizza metriche di performance, embedding e risultati direttamente nel notebook

### Cosa rende speciali questi notebook?

Ogni notebook è progettato seguendo le **migliori pratiche per la produzione**:

✅ **Gestione completa degli errori** - Degradazione graduale e messaggi di errore informativi  
✅ **Type Hints e Documentazione** - Chiare firme di funzione e docstring  
✅ **Monitoraggio delle prestazioni** - Tracciamento dell'uso dei token e misurazioni della latenza  
✅ **Design modulare** - Pattern riutilizzabili che puoi adattare ai tuoi progetti  
✅ **Complessità progressiva** - Costruzione sistematica basata sulle sessioni precedenti  

---

## 🎯 Obiettivi di apprendimento

### Competenze principali che svilupperai

Lavorando con questi notebook, padroneggerai:

1. **Gestione dei servizi AI locali**
   - Configurare e gestire i servizi Microsoft Foundry Local
   - Selezionare e caricare modelli appropriati per il tuo hardware
   - Monitorare l'uso delle risorse e ottimizzare le prestazioni
   - Gestire la scoperta dei servizi e il controllo dello stato

2. **Sviluppo di applicazioni AI**
   - Implementare completazioni di chat compatibili con OpenAI localmente
   - Costruire interfacce di streaming per migliorare l'esperienza utente
   - Progettare prompt efficaci per Small Language Models
   - Integrare modelli locali nelle applicazioni

3. **Generazione aumentata dal recupero (RAG)**
   - Creare ricerche semantiche con embedding vettoriali
   - Basare le risposte dei LLM su documenti specifici del dominio
   - Valutare la qualità del RAG con metriche RAGAS
   - Scalare dal prototipo alla produzione

4. **Ottimizzazione delle prestazioni**
   - Confrontare sistematicamente più modelli
   - Misurare latenza, throughput e tempo del primo token
   - Confrontare Small Language Models con Large Language Models
   - Selezionare modelli ottimali basati su compromessi tra prestazioni e qualità

5. **Orchestrazione multi-agente**
   - Progettare agenti specializzati per compiti diversi
   - Implementare memoria e gestione del contesto per gli agenti
   - Coordinare più agenti in flussi di lavoro complessi
   - Costruire pattern di coordinamento per la collaborazione tra agenti

6. **Routing intelligente dei modelli**
   - Implementare rilevamento dell'intento e corrispondenza di pattern
   - Instradare automaticamente le query ai modelli appropriati
   - Costruire pipeline multi-step (pianifica → esegui → perfeziona)
   - Progettare architetture scalabili di modelli come strumenti

---

## 🎓 Risultati di apprendimento

### Cosa costruirai

| Notebook | Risultato | Competenze dimostrate | Difficoltà |
|----------|-----------|-----------------------|------------|
| **Sessione 01** | App di chat con streaming | Configurazione del servizio, completazioni di base, UX di streaming | ⭐ Principiante |
| **Sessione 02 (RAG)** | Pipeline RAG con valutazione | Embedding, ricerca semantica, metriche di qualità | ⭐⭐ Intermedio |
| **Sessione 02 (Eval)** | Valutatore di qualità RAG | Metriche RAGAS, valutazione sistematica | ⭐⭐ Intermedio |
| **Sessione 03** | Benchmark multi-modello | Misurazione delle prestazioni, confronto tra modelli | ⭐⭐ Intermedio |
| **Sessione 04** | Comparatore SLM vs LLM | Analisi dei compromessi, strategie di ottimizzazione | ⭐⭐⭐ Avanzato |
| **Sessione 05** | Orchestratore multi-agente | Design degli agenti, memoria, coordinamento | ⭐⭐⭐ Avanzato |
| **Sessione 06 (Router)** | Sistema di routing intelligente | Rilevamento dell'intento, selezione del modello | ⭐⭐⭐ Avanzato |
| **Sessione 06 (Pipeline)** | Pipeline multi-step | Flussi di lavoro pianifica/esegui/perfeziona | ⭐⭐⭐ Avanzato |

### Progressione delle competenze

```
Session 01 ────► Session 02 ────► Session 03 ────► Session 04 ────► Session 05-06
   Basic            RAG             Benchmarking      Comparison      Multi-Agent
   Chat             Systems         & Performance     & Optimization  Orchestration
   
Foundation    │   Intermediate   │   Advanced       │   Expert
──────────────┴──────────────────┴──────────────────┴──────────────►
```

---

## 📅 Programma del workshop

### 🚀 Workshop di mezza giornata (3,5 ore)

**Ideale per: Sessioni di formazione per team, hackathon, workshop in conferenze**

| Orario | Durata | Sessione | Argomenti | Attività |
|--------|--------|----------|-----------|----------|
| **0:00** | 30 min | Configurazione e introduzione | Configurazione dell'ambiente, installazione di Foundry Local | Installare dipendenze, verificare configurazione |
| **0:30** | 30 min | Sessione 01 | Completazioni di chat di base, streaming | Eseguire notebook, modificare prompt |
| **1:00** | 45 min | Sessione 02 | Pipeline RAG, embedding, valutazione | Costruire sistema RAG, testare query |
| **1:45** | 15 min | Pausa | ☕ Caffè e domande | — |
| **2:00** | 30 min | Sessione 03 | Benchmark multi-modello | Confrontare 3+ modelli |
| **2:30** | 30 min | Sessione 04 | Compromessi SLM vs LLM | Analizzare prestazioni/qualità |
| **3:00** | 30 min | Sessione 05-06 | Sistemi multi-agente e routing | Esplorare pattern avanzati |

**Output**: I partecipanti lasciano il workshop con 6 applicazioni Edge AI funzionanti e pattern di codice pronti per la produzione.

---

### 🎓 Workshop di un'intera giornata (6 ore)

**Ideale per: Formazione approfondita, bootcamp, corsi universitari**

| Orario | Durata | Sessione | Argomenti | Attività |
|--------|--------|----------|-----------|----------|
| **0:00** | 45 min | Configurazione e teoria | Configurazione dell'ambiente, fondamenti di Edge AI | Installare, verificare, discutere casi d'uso |
| **0:45** | 45 min | Sessione 01 | Approfondimento sulle completazioni di chat | Implementare chat di base e streaming |
| **1:30** | 30 min | Pausa | ☕ Caffè e networking | — |
| **2:00** | 60 min | Sessione 02 (entrambe) | Pipeline RAG + valutazione RAGAS | Costruire sistema RAG completo |
| **3:00** | 30 min | Laboratorio pratico 1 | RAG personalizzato per il tuo dominio | Applicare ai propri documenti |
| **3:30** | 30 min | Pranzo | 🍽️ | — |
| **4:00** | 45 min | Sessione 03 | Metodologia di benchmarking | Confronto sistematico tra modelli |
| **4:45** | 45 min | Sessione 04 | Strategie di ottimizzazione | Analisi SLM vs LLM |
| **5:30** | 60 min | Sessione 05-06 | Orchestrazione avanzata | Sistemi multi-agente, routing |
| **6:30** | 30 min | Laboratorio pratico 2 | Costruire sistema di agenti personalizzato | Progettare il proprio orchestratore |

**Output**: Comprensione approfondita dei pattern Edge AI più 2 progetti personalizzati.

---

### 📚 Apprendimento autogestito (2 settimane)

**Ideale per: Studenti individuali, corsi online, studio autonomo**

#### Settimana 1: Fondamenti (6 ore)

| Giorno | Focus | Durata | Notebook | Compiti |
|--------|-------|--------|----------|---------|
| **Lun** | Configurazione e basi | 1,5 ore | Sessione 01 | Modificare prompt, testare streaming |
| **Mer** | Fondamenti RAG | 2 ore | Sessione 02 (entrambe) | Aggiungere propri documenti |
| **Ven** | Benchmarking | 1,5 ore | Sessione 03 | Confrontare modelli aggiuntivi |
| **Sab** | Revisione e pratica | 1 ora | Tutti Settimana 1 | Completare esercizi, debug |

#### Settimana 2: Avanzato (5 ore)

| Giorno | Focus | Durata | Notebook | Compiti |
|--------|-------|--------|----------|---------|
| **Lun** | Ottimizzazione | 1,5 ore | Sessione 04 | Documentare compromessi |
| **Mer** | Sistemi multi-agente | 2 ore | Sessione 05 | Progettare agenti personalizzati |
| **Ven** | Routing intelligente | 1,5 ore | Sessione 06 (entrambe) | Costruire logica di routing |
| **Sab** | Progetto finale | 2 ore | Integrazione | Combinare più pattern |

**Output**: Padronanza dei pattern Edge AI più progetto di portfolio.

---

## 📔 Descrizioni dei notebook

### 📘 Sessione 01: Chat Bootstrap
**File**: `session01_chat_bootstrap.ipynb`  
**Durata**: 20-30 minuti  
**Prerequisiti**: Nessuno  
**Difficoltà**: ⭐ Principiante

**Cosa imparerai**:
- Installare e configurare Foundry Local Python SDK
- Usare `FoundryLocalManager` per la scoperta automatica dei servizi
- Implementare completazioni di chat di base con API compatibile OpenAI
- Costruire risposte in streaming per migliorare l'esperienza utente
- Gestire errori e indisponibilità del servizio in modo efficace

**Concetti chiave**: Gestione dei servizi, completazioni di chat, streaming, gestione degli errori

**Cosa costruirai**: Applicazione di chat interattiva con supporto streaming

---

### 📗 Sessione 02: Pipeline RAG
**File**: `session02_rag_pipeline.ipynb`  
**Durata**: 30-45 minuti  
**Prerequisiti**: Sessione 01  
**Difficoltà**: ⭐⭐ Intermedio

**Cosa imparerai**:
- Implementare il pattern di Generazione Aumentata dal Recupero (RAG)
- Creare embedding vettoriali con sentence-transformers
- Costruire ricerca semantica con similarità coseno
- Basare le risposte dei LLM su documenti del dominio
- Gestire dipendenze opzionali con import guard

**Concetti chiave**: Architettura RAG, embedding, ricerca semantica, similarità vettoriale

**Cosa costruirai**: Sistema di domande e risposte basato su documenti

---

### 📗 Sessione 02: Valutazione RAG con RAGAS
**File**: `session02_rag_eval_ragas.ipynb`  
**Durata**: 30-45 minuti  
**Prerequisiti**: Sessione 02 Pipeline RAG  
**Difficoltà**: ⭐⭐ Intermedio

**Cosa imparerai**:
- Valutare la qualità del RAG con metriche standard del settore
- Misurare rilevanza del contesto, rilevanza delle risposte, fedeltà
- Usare il framework RAGAS per valutazioni sistematiche
- Identificare e correggere problemi di qualità del RAG
- Costruire dataset di valutazione per il tuo dominio

**Concetti chiave**: Valutazione RAG, metriche RAGAS, misurazione della qualità, test sistematici

**Cosa costruirai**: Framework di valutazione della qualità RAG

---

### 📙 Sessione 03: Benchmark modelli OSS
**File**: `session03_benchmark_oss_models.ipynb`  
**Durata**: 30-45 minuti  
**Prerequisiti**: Sessione 01  
**Difficoltà**: ⭐⭐ Intermedio

**Cosa imparerai**:
- Confrontare sistematicamente più modelli
- Misurare latenza, throughput, tempo del primo token
- Implementare degradazione graduale per fallimenti dei modelli
- Confrontare prestazioni tra famiglie di modelli
- Visualizzare e analizzare risultati di benchmark

**Concetti chiave**: Benchmarking delle prestazioni, misurazione della latenza, confronto tra modelli, analisi statistica

**Cosa costruirai**: Suite di benchmarking multi-modello

---

### 📙 Sessione 04: Confronto modelli (SLM vs LLM)
**File**: `session04_model_compare.ipynb`  
**Durata**: 30-45 minuti  
**Prerequisiti**: Sessioni 01, 03  
**Difficoltà**: ⭐⭐⭐ Avanzato

**Cosa imparerai**:
- Confrontare Small Language Models con Large Language Models
- Analizzare compromessi tra prestazioni e qualità
- Misurare metriche di idoneità per l'edge
- Selezionare modelli ottimali per vincoli di distribuzione
- Documentare criteri decisionali per la selezione dei modelli

**Concetti chiave**: Selezione dei modelli, analisi dei compromessi, strategie di ottimizzazione, pianificazione della distribuzione

**Cosa costruirai**: Framework di confronto SLM vs LLM

---

### 📕 Sessione 05: Orchestratore multi-agente
**File**: `session05_agents_orchestrator.ipynb`  
**Durata**: 45-60 minuti  
**Prerequisiti**: Sessioni 01-02  
**Difficoltà**: ⭐⭐⭐ Avanzato

**Cosa imparerai**:
- Progettare agenti specializzati per compiti diversi
- Implementare memoria e gestione del contesto per gli agenti
- Costruire pattern di coordinamento per la collaborazione tra agenti
- Gestire comunicazione e passaggi tra agenti
- Monitorare le prestazioni del sistema multi-agente

**Concetti chiave**: Architettura degli agenti, pattern di coordinamento, gestione della memoria, orchestrazione degli agenti

**Cosa costruirai**: Sistema multi-agente con coordinatore e specialisti

---

### 📕 Sessione 06: Router di modelli
**File**: `session06_models_router.ipynb`  
**Durata**: 30-45 minuti  
**Prerequisiti**: Sessioni 01, 03  
**Difficoltà**: ⭐⭐⭐ Avanzato

**Cosa imparerai**:
- Implementare rilevamento dell'intento e corrispondenza di pattern
- Costruire routing dei modelli basato su parole chiave
- Instradare automaticamente le query ai modelli appropriati
- Configurare registri multi-modello
- Monitorare decisioni di routing e prestazioni

**Concetti chiave**: Rilevamento dell'intento, routing dei modelli, corrispondenza di pattern, selezione intelligente

**Cosa costruirai**: Sistema di routing intelligente dei modelli

---

### 📕 Sessione 06: Pipeline multi-step
**File**: `session06_models_pipeline.ipynb`  
**Durata**: 30-45 minuti  
**Prerequisiti**: Sessioni 01, 06 Router  
**Difficoltà**: ⭐⭐⭐ Avanzato

**Cosa imparerai**:
- Costruire pipeline AI multi-step (pianifica → esegui → perfeziona)
- Integrare il router per la selezione intelligente dei modelli
- Implementare gestione degli errori e recupero nella pipeline
- Monitorare prestazioni e fasi della pipeline
- Progettare architetture scalabili di modelli come strumenti

**Concetti Chiave**: Architettura a pipeline, elaborazione multi-stadio, recupero dagli errori, modelli di scalabilità

**Cosa Costruirai**: Pipeline intelligente multi-step con routing

---

## 🚀 Per Iniziare

### Prerequisiti

**Requisiti di Sistema**:
- **OS**: Windows 10/11, macOS 11+ o Linux (Ubuntu 20.04+)
- **RAM**: Minimo 8GB, consigliati 16GB+
- **Spazio di Archiviazione**: Almeno 10GB liberi per i modelli
- **Hardware**: CPU con AVX2; GPU (CUDA, Qualcomm NPU) opzionale

**Requisiti Software**:
- **Python 3.8+** con pip
- **Jupyter Notebook** o **VS Code** con estensione Jupyter
- **Microsoft Foundry Local** installato e configurato
- **Git** (per clonare il repository)

### Passaggi di Installazione

#### 1. Installare Foundry Local

**Windows**:
```cmd
winget install Microsoft.FoundryLocal
```

**macOS**:
```bash
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**Verifica Installazione**:
```bash
foundry --version
```

#### 2. Configurare l'Ambiente Python

```bash
# Navigate to Workshop directory
cd Workshop

# Create virtual environment
python -m venv .venv

# Activate virtual environment
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

#### 3. Avviare Foundry Local

```bash
# Load a model (auto-downloads if needed)
foundry model run phi-4-mini

# Verify service is running
foundry service status
```

#### 4. Avviare Jupyter

```bash
# Start Jupyter Notebook
jupyter notebook notebooks/

# Or use VS Code with Jupyter extension
code notebooks/
```

### Verifica Rapida

Esegui questo comando in una cella Python per verificare la configurazione:

```python
from foundry_local import FoundryLocalManager
import openai

# Initialize manager (auto-discovers service)
manager = FoundryLocalManager("phi-4-mini")

# Configure OpenAI client
client = openai.OpenAI(
    base_url=manager.endpoint,
    api_key=manager.api_key
)

# Test chat completion
response = client.chat.completions.create(
    model=manager.get_model_info("phi-4-mini").id,
    messages=[{"role": "user", "content": "Hello!"}]
)

print(response.choices[0].message.content)
```

**Output Atteso**: Una risposta di saluto dal modello locale.

---

## 📝 Migliori Pratiche per il Workshop

### Per gli Istruttori

**Prima del Workshop**:
- ✅ Inviare le istruzioni di installazione una settimana prima
- ✅ Testare tutti i notebook sull'hardware di destinazione
- ✅ Preparare una guida per la risoluzione dei problemi comuni
- ✅ Avere modelli di backup pronti (phi-3.5-mini se phi-4-mini fallisce)
- ✅ Configurare un canale di chat condiviso per le domande

**Durante il Workshop**:
- ✅ Iniziare con un rapido controllo dell'ambiente (5 minuti)
- ✅ Condividere immediatamente le risorse per la risoluzione dei problemi
- ✅ Incoraggiare l'esperimento e le modifiche
- ✅ Usare le pause strategicamente (dopo ogni 2 sessioni)
- ✅ Avere assistenti disponibili per supporto individuale

**Dopo il Workshop**:
- ✅ Condividere notebook completi e soluzioni funzionanti
- ✅ Fornire link a risorse aggiuntive
- ✅ Creare un sondaggio di feedback per miglioramenti
- ✅ Offrire ore di ufficio per domande di follow-up

### Per i Partecipanti

**Massimizza il tuo Apprendimento**:
- ✅ Completa la configurazione prima dell'inizio del workshop
- ✅ Esegui ogni cella di codice personalmente (non limitarti a leggere)
- ✅ Sperimenta con parametri e prompt
- ✅ Prendi appunti su intuizioni e difficoltà
- ✅ Fai domande quando sei bloccato (probabilmente altri hanno la stessa domanda)

**Errori Comuni da Evitare**:
- ❌ Saltare l'ordine di esecuzione delle celle (esegui in sequenza)
- ❌ Non leggere attentamente i messaggi di errore
- ❌ Affrettarsi senza comprendere
- ❌ Ignorare le spiegazioni in markdown
- ❌ Non salvare i notebook modificati

**Consigli per il Debug**:
1. **Servizio Non Avviato**: Controlla `foundry service status`
2. **Errori di Importazione**: Verifica che l'ambiente virtuale sia attivato
3. **Modello Non Trovato**: Esegui `foundry model ls` per elencare i modelli caricati
4. **Prestazioni Lente**: Controlla l'uso della RAM, chiudi altre applicazioni
5. **Risultati Inaspettati**: Riavvia il kernel ed esegui tutte le celle dall'inizio

---

## 🔗 Risorse Aggiuntive

### Materiali del Workshop

- **[Guida Principale del Workshop](../Readme.md)** - Panoramica, obiettivi di apprendimento, risultati professionali
- **[Esempi Python](../../../../Workshop/samples)** - Script Python corrispondenti per ogni sessione
- **[Guide alle Sessioni](../../../../Workshop)** - Guide dettagliate in markdown (Session01-06)
- **[Script](../../../../Workshop/scripts)** - Utilità di validazione e test
- **[Risoluzione dei Problemi](./TROUBLESHOOTING.md)** - Problemi comuni e soluzioni
- **[Guida Rapida](./quickstart.md)** - Guida per iniziare rapidamente

### Documentazione

- **[Documentazione Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)** - Documentazione ufficiale Microsoft
- **[OpenAI Python SDK](https://github.com/openai/openai-python)** - Riferimento SDK OpenAI
- **[Sentence Transformers](https://www.sbert.net/)** - Documentazione modelli di embedding
- **[Framework RAGAS](https://docs.ragas.io/)** - Metriche di valutazione RAG

### Comunità

- **[Discussioni su GitHub](https://github.com/microsoft/edgeai-for-beginners/discussions)** - Fai domande, condividi progetti
- **[Discord Azure AI Foundry](https://discord.com/invite/ByRwuEEgH4)** - Supporto comunitario in tempo reale
- **[Stack Overflow](https://stackoverflow.com/questions/tagged/foundry-local)** - Q&A tecnico

---

## 🎯 Raccomandazioni per il Percorso di Apprendimento

### Percorso Principiante (Inizia Qui)

1. **Sessione 01** - Bootstrap Chat
2. **Sessione 02** - Pipeline RAG
3. **Sessione 03** - Benchmark Modelli

**Tempo**: ~2 ore | **Focus**: Modelli fondamentali

---

### Percorso Intermedio

1. Completa il Percorso Principiante
2. **Sessione 02** - Valutazione RAG
3. **Sessione 04** - Confronto Modelli

**Tempo**: ~4 ore | **Focus**: Qualità e ottimizzazione

---

### Percorso Avanzato (Workshop Completo)

1. Completa il Percorso Intermedio
2. **Sessione 05** - Orchestratore Multi-Agente
3. **Sessione 06** - Router Modelli
4. **Sessione 06** - Pipeline Multi-Step

**Tempo**: ~6 ore | **Focus**: Modelli di produzione

---

### Percorso Progetto Personalizzato

1. Completa il Percorso Principiante (Sessioni 01-03)
2. Scegli UNA sessione avanzata in base al tuo obiettivo:
   - **Costruire un'app RAG?** → Sessione 02 Valutazione
   - **Ottimizzare le prestazioni?** → Sessione 04 Confronto
   - **Workflow complessi?** → Sessione 05 Orchestratore
   - **Architettura scalabile?** → Sessione 06 Router + Pipeline

**Tempo**: ~3 ore | **Focus**: Competenze specifiche per il progetto

---

## 📊 Metriche di Successo

Monitora i tuoi progressi con questi traguardi:

- [ ] **Configurazione Completa** - Foundry Local in esecuzione, tutte le dipendenze installate
- [ ] **Prima Chat** - Sessione 01 completata, chat in streaming funzionante
- [ ] **RAG Costruito** - Sessione 02 completata, sistema QA documenti funzionante
- [ ] **Modelli Valutati** - Sessione 03 completata, dati sulle prestazioni raccolti
- [ ] **Analisi Trade-off** - Sessione 04 completata, criteri di selezione modelli documentati
- [ ] **Agenti Orchestrati** - Sessione 05 completata, sistema multi-agente funzionante
- [ ] **Routing Implementato** - Sessione 06 completata, selezione intelligente dei modelli funzionante
- [ ] **Progetto Personalizzato** - Applicati i modelli del workshop al tuo caso d'uso

---

## 🤝 Contribuire

Hai trovato un problema o hai un suggerimento? Accettiamo contributi!

- **Segnala Problemi**: [GitHub Issues](https://github.com/microsoft/edgeai-for-beginners/issues)
- **Suggerisci Miglioramenti**: [GitHub Discussions](https://github.com/microsoft/edgeai-for-beginners/discussions)
- **Invia PR**: Segui le [Linee Guida per Contribuire](../../AGENTS.md)

---

## 📄 Licenza

Questo workshop fa parte del repository [EdgeAI for Beginners](https://github.com/microsoft/edgeai-for-beginners) ed è concesso sotto licenza [MIT License](../../../../LICENSE).

---

**Pronto a costruire applicazioni Edge AI pronte per la produzione?**  
**Inizia con [Sessione 01: Bootstrap Chat](./session01_chat_bootstrap.ipynb) →**

---

*Ultimo Aggiornamento: 8 ottobre 2025 | Versione Workshop: 2.0*

---

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire l'accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un traduttore umano. Non siamo responsabili per eventuali incomprensioni o interpretazioni errate derivanti dall'uso di questa traduzione.
<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "04951692a100dcd716df01efca2d3f0d",
  "translation_date": "2025-11-11T22:50:53+00:00",
  "source_file": "Workshop/Readme.md",
  "language_code": "it"
}
-->
# EdgeAI per Principianti - Workshop

> **Percorso di apprendimento pratico per creare applicazioni Edge AI pronte per la produzione**
>
> Padroneggia il deployment locale dell'AI con Microsoft Foundry Local, dalla prima chat completata all'orchestrazione multi-agente in 6 sessioni progressive.

---

## 🎯 Introduzione

Benvenuto al **Workshop EdgeAI per Principianti** - la tua guida pratica per costruire applicazioni intelligenti che funzionano interamente su hardware locale. Questo workshop trasforma i concetti teorici di Edge AI in competenze pratiche attraverso esercizi progressivamente più impegnativi utilizzando Microsoft Foundry Local e Small Language Models (SLMs).

### Perché questo workshop?

**La rivoluzione dell'Edge AI è qui**

Le organizzazioni di tutto il mondo stanno passando dall'AI basata su cloud al computing edge per tre motivi fondamentali:

1. **Privacy e conformità** - Elaborazione dei dati sensibili localmente senza trasmissione al cloud (HIPAA, GDPR, normative finanziarie)
2. **Prestazioni** - Eliminazione della latenza di rete (50-500ms locale contro 500-2000ms round-trip cloud)
3. **Controllo dei costi** - Eliminazione dei costi API per token e scalabilità senza spese cloud

**Ma l'Edge AI è diversa**

Eseguire l'AI on-premises richiede nuove competenze:
- Selezione e ottimizzazione dei modelli per vincoli di risorse
- Gestione dei servizi locali e accelerazione hardware
- Prompt engineering per modelli più piccoli
- Modelli di deployment per dispositivi edge

**Questo workshop ti fornisce queste competenze**

In 6 sessioni mirate (~3 ore totali), passerai da "Hello World" al deployment di sistemi multi-agente pronti per la produzione - tutto in esecuzione localmente sul tuo computer.

---

## 📚 Obiettivi di apprendimento

Completando questo workshop, sarai in grado di:

### Competenze principali
1. **Distribuire e gestire servizi AI locali**
   - Installare e configurare Microsoft Foundry Local
   - Selezionare modelli appropriati per il deployment edge
   - Gestire il ciclo di vita dei modelli (download, caricamento, caching)
   - Monitorare l'uso delle risorse e ottimizzare le prestazioni

2. **Creare applicazioni potenziate dall'AI**
   - Implementare completamenti di chat compatibili con OpenAI localmente
   - Progettare prompt efficaci per Small Language Models
   - Gestire risposte in streaming per una migliore esperienza utente
   - Integrare modelli locali in applicazioni esistenti

3. **Creare sistemi RAG (Retrieval Augmented Generation)**
   - Costruire ricerche semantiche con embeddings
   - Basare le risposte degli LLM su conoscenze specifiche del dominio
   - Valutare la qualità dei RAG con metriche standard del settore
   - Scalare dal prototipo alla produzione

4. **Ottimizzare le prestazioni dei modelli**
   - Valutare più modelli per il tuo caso d'uso
   - Misurare latenza, throughput e tempo del primo token
   - Selezionare i modelli ottimali in base ai compromessi velocità/qualità
   - Confrontare i compromessi tra SLM e LLM in scenari reali

5. **Orchestrare sistemi multi-agente**
   - Progettare agenti specializzati per compiti diversi
   - Implementare memoria e gestione del contesto per gli agenti
   - Coordinare agenti in flussi di lavoro complessi
   - Instradare richieste in modo intelligente tra più modelli

6. **Distribuire soluzioni pronte per la produzione**
   - Implementare gestione degli errori e logica di retry
   - Monitorare l'uso dei token e le risorse di sistema
   - Costruire architetture scalabili con modelli come strumenti
   - Pianificare percorsi di migrazione da edge a ibrido (edge + cloud)

---

## 🎓 Risultati di apprendimento

### Cosa costruirai

Alla fine di questo workshop, avrai creato:

| Sessione | Risultato | Competenze dimostrate |
|----------|-----------|-----------------------|
| **1**    | Applicazione di chat con streaming | Configurazione del servizio, completamenti di base, UX in streaming |
| **2**    | Sistema RAG con valutazione | Embeddings, ricerca semantica, metriche di qualità |
| **3**    | Suite di benchmark multi-modello | Misurazione delle prestazioni, confronto tra modelli |
| **4**    | Comparatore SLM vs LLM | Analisi dei compromessi, strategie di ottimizzazione |
| **5**    | Orchestratore multi-agente | Progettazione di agenti, gestione della memoria, coordinamento |
| **6**    | Sistema di routing intelligente | Rilevamento delle intenzioni, selezione dei modelli, scalabilità |

### Matrice delle competenze

| Livello di competenza | Sessioni 1-2 | Sessioni 3-4 | Sessioni 5-6 |
|-----------------------|--------------|--------------|--------------|
| **Principiante**      | ✅ Setup e basi | ⚠️ Impegnativo | ❌ Troppo avanzato |
| **Intermedio**        | ✅ Revisione rapida | ✅ Apprendimento principale | ⚠️ Obiettivi ambiziosi |
| **Avanzato**          | ✅ Facile | ✅ Raffinamento | ✅ Modelli di produzione |

### Competenze pronte per il lavoro

**Dopo questo workshop, sarai pronto per:**

✅ **Costruire applicazioni orientate alla privacy**
- App sanitarie che gestiscono PHI/PII localmente
- Servizi finanziari con requisiti di conformità
- Sistemi governativi con esigenze di sovranità dei dati

✅ **Ottimizzare per ambienti edge**
- Dispositivi IoT con risorse limitate
- Applicazioni mobili offline-first
- Sistemi in tempo reale a bassa latenza

✅ **Progettare architetture intelligenti**
- Sistemi multi-agente per flussi di lavoro complessi
- Deployment ibridi edge-cloud
- Infrastrutture AI ottimizzate per i costi

✅ **Guidare iniziative Edge AI**
- Valutare la fattibilità dell'Edge AI per i progetti
- Selezionare modelli e framework appropriati
- Progettare soluzioni AI locali scalabili

---

## 🗺️ Struttura del workshop

### Panoramica delle sessioni (6 sessioni × 30 minuti = 3 ore)

| Sessione | Argomento | Focus | Durata |
|----------|-----------|-------|--------|
| **1**    | Introduzione a Foundry Local | Installazione, validazione, primi completamenti | 30 min |
| **2**    | Creazione di soluzioni AI con RAG | Prompt engineering, embeddings, valutazione | 30 min |
| **3**    | Modelli open source | Scoperta, benchmarking, selezione | 30 min |
| **4**    | Modelli all'avanguardia | SLM vs LLM, ottimizzazione, framework | 30 min |
| **5**    | Agenti potenziati dall'AI | Progettazione di agenti, orchestrazione, memoria | 30 min |
| **6**    | Modelli come strumenti | Routing, concatenazione, strategie di scalabilità | 30 min |

---

## 🚀 Inizio rapido

### Prerequisiti

**Requisiti di sistema:**
- **OS**: Windows 10/11, macOS 11+ o Linux (Ubuntu 20.04+)
- **RAM**: minimo 8GB, consigliati 16GB+
- **Storage**: almeno 10GB di spazio libero per i modelli
- **CPU**: Processore moderno con supporto AVX2
- **GPU** (opzionale): compatibile CUDA o Qualcomm NPU per accelerazione

**Requisiti software:**
- **Python 3.8+** ([Download](https://www.python.org/downloads/))
- **Microsoft Foundry Local** ([Guida all'installazione](../../../Workshop))
- **Git** ([Download](https://git-scm.com/downloads))
- **Visual Studio Code** (consigliato) ([Download](https://code.visualstudio.com/))

### Configurazione in 3 passaggi

#### 1. Installa Foundry Local

**Windows:**
```powershell
winget install Microsoft.FoundryLocal
```

**macOS:**
```bash
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**Verifica installazione:**
```bash
foundry --version
foundry service status
```

**Assicurati che Azure AI Foundry Local sia in esecuzione con una porta fissa**

```bash
# Set FoundryLocal to use port 58123 (default)
foundry service set --port 58123 --show

# Or use a different port
foundry service set --port 58000 --show
```

**Verifica il funzionamento:**
```bash
# Check service status
foundry service status

# Test the endpoint
curl http://127.0.0.1:58123/v1/models
```
**Ricerca dei modelli disponibili**
Per vedere quali modelli sono disponibili nella tua istanza di Foundry Local, puoi interrogare l'endpoint dei modelli:

```bash
# cmd/bash/powershell
foundry model list
```

Utilizzando l'endpoint web 

```bash
# Windows PowerShell
powershell -Command "Invoke-RestMethod -Uri 'http://127.0.0.1:58123/v1/models' -Method Get"

# Or using curl (if available)
curl http://127.0.0.1:58123/v1/models
```

#### 2. Clona il repository e installa le dipendenze

```bash
# Clone repository
git clone https://github.com/microsoft/edgeai-for-beginners.git
cd edgeai-for-beginners/Workshop

# Create virtual environment
python -m venv .venv

# Activate virtual environment
# Windows:
.\.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

#### 3. Esegui il tuo primo esempio

```bash
# Start Foundry Local and load a model
foundry model run phi-4-mini

# Run the chat bootstrap sample
cd samples
python -m session01.chat_bootstrap "What is edge AI?"
```

**✅ Successo!** Dovresti vedere una risposta in streaming sull'Edge AI.

---

## 📦 Risorse del workshop

### Esempi Python

Esempi pratici progressivi che dimostrano ogni concetto:

| Sessione | Esempio | Descrizione | Tempo di esecuzione |
|----------|---------|-------------|---------------------|
| 1        | [`chat_bootstrap.py`](../../../Workshop/samples/session01/chat_bootstrap.py) | Chat di base e in streaming | ~30s |
| 2        | [`rag_pipeline.py`](../../../Workshop/samples/session02/rag_pipeline.py) | RAG con embeddings | ~45s |
| 2        | [`rag_eval_ragas.py`](../../../Workshop/samples/session02/rag_eval_ragas.py) | Valutazione della qualità RAG | ~60s |
| 3        | [`benchmark_oss_models.py`](../../../Workshop/samples/session03/benchmark_oss_models.py) | Benchmarking multi-modello | ~2-3m |
| 4        | [`model_compare.py`](../../../Workshop/samples/session04/model_compare.py) | Confronto SLM vs LLM | ~45s |
| 5        | [`agents_orchestrator.py`](../../../Workshop/samples/session05/agents_orchestrator.py) | Sistema multi-agente | ~60s |
| 6        | [`models_router.py`](../../../Workshop/samples/session06/models_router.py) | Routing basato su intenti | ~45s |
| 6        | [`models_pipeline.py`](../../../Workshop/samples/session06/models_pipeline.py) | Pipeline multi-step | ~60s |

### Notebook Jupyter

Esplorazione interattiva con spiegazioni e visualizzazioni:

| Sessione | Notebook | Descrizione | Difficoltà |
|----------|----------|-------------|------------|
| 1        | [`session01_chat_bootstrap.ipynb`](./notebooks/session01_chat_bootstrap.ipynb) | Basi della chat e streaming | ⭐ Principiante |
| 2        | [`session02_rag_pipeline.ipynb`](./notebooks/session02_rag_pipeline.ipynb) | Costruzione di un sistema RAG | ⭐⭐ Intermedio |
| 2        | [`session02_rag_eval_ragas.ipynb`](./notebooks/session02_rag_eval_ragas.ipynb) | Valutazione della qualità RAG | ⭐⭐ Intermedio |
| 3        | [`session03_benchmark_oss_models.ipynb`](./notebooks/session03_benchmark_oss_models.ipynb) | Benchmarking dei modelli | ⭐⭐ Intermedio |
| 4        | [`session04_model_compare.ipynb`](./notebooks/session04_model_compare.ipynb) | Confronto tra modelli | ⭐⭐ Intermedio |
| 5        | [`session05_agents_orchestrator.ipynb`](./notebooks/session05_agents_orchestrator.ipynb) | Orchestrazione degli agenti | ⭐⭐⭐ Avanzato |
| 6        | [`session06_models_router.ipynb`](./notebooks/session06_models_router.ipynb) | Routing basato su intenti | ⭐⭐⭐ Avanzato |
| 6        | [`session06_models_pipeline.ipynb`](./notebooks/session06_models_pipeline.ipynb) | Orchestrazione della pipeline | ⭐⭐⭐ Avanzato |

### Documentazione

Guide e riferimenti completi:

| Documento | Descrizione | Quando usarlo |
|-----------|-------------|---------------|
| [QUICK_START.md](./QUICK_START.md) | Guida rapida all'installazione | Partendo da zero |
| [QUICK_REFERENCE.md](./QUICK_REFERENCE.md) | Riferimento rapido a comandi e API | Risposte rapide |
| [FOUNDRY_SDK_QUICKREF.md](./FOUNDRY_SDK_QUICKREF.md) | Pattern ed esempi SDK | Scrivendo codice |
| [ENV_CONFIGURATION.md](./ENV_CONFIGURATION.md) | Guida alle variabili d'ambiente | Configurando esempi |
| [notebooks/TROUBLESHOOTING.md](./notebooks/TROUBLESHOOTING.md) | Problemi comuni e soluzioni | Risolvendo problemi |

---

## 🎓 Raccomandazioni per il percorso di apprendimento

### Per principianti (3-4 ore)
1. ✅ Sessione 1: Introduzione (focus su setup e chat di base)
2. ✅ Sessione 2: Basi del RAG (inizialmente salta la valutazione)
3. ✅ Sessione 3: Benchmarking semplice (solo 2 modelli)
4. ⏭️ Salta le sessioni 4-6 per ora
5. 🔄 Torna alle sessioni 4-6 dopo aver costruito la prima applicazione

### Per sviluppatori intermedi (3 ore)
1. ⚡ Sessione 1: Validazione rapida del setup
2. ✅ Sessione 2: Completa il pipeline RAG con valutazione
3. ✅ Sessione 3: Suite completa di benchmarking
4. ✅ Sessione 4: Ottimizzazione dei modelli
5. ✅ Sessioni 5-6: Focus sui pattern architetturali

### Per professionisti avanzati (2-3 ore)
1. ⚡ Sessioni 1-3: Revisione rapida e validazione
2. ✅ Sessione 4: Approfondimento sull'ottimizzazione
3. ✅ Sessione 5: Architettura multi-agente
4. ✅ Sessione 6: Pattern di produzione e scalabilità
5. 🚀 Estendi: Costruisci logiche di routing personalizzate e deployment ibridi

---

## Pacchetto sessioni del workshop (Laboratori mirati di 30 minuti)

Se stai seguendo il formato condensato del workshop in 6 sessioni, utilizza queste guide dedicate (ognuna si collega e completa i moduli più ampi sopra indicati):

| Sessione del workshop | Guida | Focus principale |
|-----------------------|-------|------------------|
| 1 | [Session01-GettingStartedFoundryLocal](./Session01-GettingStartedFoundryLocal.md) | Installazione, validazione, esecuzione phi & GPT-OSS-20B, accelerazione |
| 2 | [Session02-BuildAISolutionsRAG](./Session02-BuildAISolutionsRAG.md) | Prompt engineering, pattern RAG, grounding su CSV e documenti, migrazione |
| 3 | [Session03-OpenSourceModels](./Session03-OpenSourceModels.md) | Integrazione Hugging Face, benchmarking, selezione dei modelli |
| 4 | [Session04-CuttingEdgeModels](./Session04-CuttingEdgeModels.md) | SLM vs LLM, WebGPU, Chainlit RAG, accelerazione ONNX |
| 5 | [Session05-AIPoweredAgents](./Session05-AIPoweredAgents.md) | Ruoli degli agenti, memoria, strumenti, orchestrazione |
| 6 | [Session06-ModelsAsTools](./Session06-ModelsAsTools.md) | Routing, concatenazione, percorso di scalabilità verso Azure |

Ogni file di sessione include: abstract, obiettivi di apprendimento, flusso demo di 30 minuti, progetto iniziale, checklist di validazione, risoluzione dei problemi e riferimenti all'SDK ufficiale Foundry Local Python.

### Script di esempio

Installare le dipendenze del workshop (Windows):

```powershell
cd Workshop
py -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

macOS / Linux:

```bash
cd Workshop
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Se si esegue il servizio Foundry Local su una macchina o VM (Windows) diversa da macOS, esportare l'endpoint:

```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```

| Sessione | Script | Descrizione |
|----------|--------|-------------|
| 1 | `samples/session01/chat_bootstrap.py` | Servizio di bootstrap & chat in streaming |
| 2 | `samples/session02/rag_pipeline.py` | RAG minimale (embedding in memoria) |
|   | `samples/session02/rag_eval_ragas.py` | Valutazione RAG con metriche ragas |
| 3 | `samples/session03/benchmark_oss_models.py` | Benchmarking di latenza e throughput multi-modello |
| 4 | `samples/session04/model_compare.py` | Confronto SLM vs LLM (latenza & output di esempio) |
| 5 | `samples/session05/agents_orchestrator.py` | Pipeline di ricerca a due agenti → editoriale |
| 6 | `samples/session06/models_router.py` | Demo di routing basato sull'intento |
|   | `samples/session06/models_pipeline.py` | Catena di pianificazione/esecuzione/raffinamento multi-step |

### Variabili di ambiente (comuni tra gli esempi)

| Variabile | Scopo | Esempio |
|-----------|-------|---------|
| `FOUNDRY_LOCAL_ALIAS` | Alias di modello singolo predefinito per esempi di base | `phi-4-mini` |
| `SLM_ALIAS` / `LLM_ALIAS` | Modello SLM esplicito vs modello più grande per confronto | `phi-4-mini` / `gpt-oss-20b` |
| `BENCH_MODELS` | Elenco di alias da sottoporre a benchmark | `qwen2.5-0.5b,mistral-7b` |
| `BENCH_ROUNDS` | Ripetizioni del benchmark per modello | `3` |
| `BENCH_PROMPT` | Prompt utilizzato nel benchmarking | `Explain retrieval augmented generation briefly.` |
| `EMBED_MODEL` | Modello di embedding sentence-transformers | `sentence-transformers/all-MiniLM-L6-v2` |
| `RAG_QUESTION` | Sovrascrivere la query di test per la pipeline RAG | `Why use RAG with local inference?` |
| `AGENT_QUESTION` | Sovrascrivere la query della pipeline degli agenti | `Explain why edge AI matters for compliance.` |
| `AGENT_MODEL_PRIMARY` | Alias del modello per l'agente di ricerca | `phi-4-mini` |
| `AGENT_MODEL_EDITOR` | Alias del modello per l'agente editoriale (può essere diverso) | `gpt-oss-20b` |
| `SHOW_USAGE` | Quando `1`, stampa l'utilizzo dei token per completamento | `1` |
| `RETRY_ON_FAIL` | Quando `1`, riprova una volta in caso di errori transitori di chat | `1` |
| `RETRY_BACKOFF` | Secondi di attesa prima di riprovare | `1.0` |

Se una variabile non è impostata, gli script tornano a valori predefiniti sensati. Per demo a modello singolo, di solito è necessario solo `FOUNDRY_LOCAL_ALIAS`.

### Modulo di utilità

Tutti gli esempi ora condividono un helper `samples/workshop_utils.py` che fornisce:

* Creazione cache di `FoundryLocalManager` + client OpenAI
* Helper `chat_once()` con retry opzionale + stampa dell'utilizzo
* Semplice report dell'utilizzo dei token (abilitabile con `SHOW_USAGE=1`)

Questo riduce la duplicazione e evidenzia le migliori pratiche per un'orchestrazione efficiente di modelli locali.

## Miglioramenti opzionali (trasversali alle sessioni)

| Tema | Miglioramento | Sessioni | Env / Toggle |
|------|--------------|----------|--------------|
| Determinismo | Temperatura fissa + set di prompt stabili | 1–6 | Impostare `temperature=0`, `top_p=1` |
| Visibilità dell'utilizzo dei token | Insegnamento costi/efficienza coerente | 1–6 | `SHOW_USAGE=1` |
| Streaming del primo token | Metrica di latenza percepita | 1,3,4,6 | `BENCH_STREAM=1` (benchmark) |
| Resilienza ai retry | Gestisce avvii a freddo transitori | Tutte | `RETRY_ON_FAIL=1` + `RETRY_BACKOFF` |
| Agenti multi-modello | Specializzazione eterogenea dei ruoli | 5 | `AGENT_MODEL_PRIMARY`, `AGENT_MODEL_EDITOR` |
| Routing adattivo | Intento + euristiche di costo | 6 | Estendere il router con logica di escalation |
| Memoria vettoriale | Richiamo semantico a lungo termine | 2,5,6 | Integrare l'indice di embedding FAISS/Chroma |
| Esportazione tracce | Audit & valutazione | 2,5,6 | Aggiungere linee JSON per ogni step |
| Metriche di qualità | Monitoraggio qualitativo | 3–6 | Prompt di punteggio secondari |
| Test preliminari | Validazione rapida pre-workshop | Tutte | `python Workshop/tests/smoke.py` |

### Avvio rapido deterministico

```powershell
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
python Workshop\tests\smoke.py
```

Aspettarsi conteggi di token stabili su input identici ripetuti.

### Valutazione RAG (Sessione 2)

Utilizzare `rag_eval_ragas.py` per calcolare la rilevanza delle risposte, la fedeltà e la precisione contestuale su un piccolo dataset sintetico:

```powershell
cd Workshop/samples
python -m session02.rag_eval_ragas
```

Estendere fornendo un JSONL più grande di domande, contesti e verità di base, quindi convertirlo in un `Dataset` di Hugging Face.

## Appendice di accuratezza dei comandi CLI

Il workshop utilizza deliberatamente solo comandi CLI Foundry Local documentati/stabili.

### Comandi stabili referenziati

| Categoria | Comando | Scopo |
|-----------|---------|-------|
| Core | `foundry --version` | Mostra la versione installata |
| Servizio | `foundry service start` | Avvia il servizio locale (se non avviato automaticamente) |
| Servizio | `foundry service status` | Mostra lo stato del servizio |
| Modelli | `foundry model list` | Elenca il catalogo / modelli disponibili |
| Modelli | `foundry model download <alias>` | Scarica i pesi del modello nella cache |
| Modelli | `foundry model run <alias>` | Avvia (carica) un modello localmente; combinare con `--prompt` per un ciclo one-shot |
| Modelli | `foundry model unload <alias>` / `foundry model stop <alias>` | Scarica un modello dalla memoria (se supportato) |
| Cache | `foundry cache list` | Elenca i modelli nella cache (scaricati) |

### Modello di prompt one-shot

Invece di un sottocomando deprecato `model chat`, utilizzare:

```powershell
foundry model run <alias> --prompt "Your question here"
```

Questo esegue un ciclo di prompt/risposta singolo e poi esce.

### Pattern rimossi / evitati

| Deprecati / Non documentati | Sostituzione / Guida |
|-----------------------------|----------------------|
| `foundry model chat <model> "..."` | `foundry model run <model> --prompt "..."` |
| `foundry model list --running` | Usare semplicemente `foundry model list` + attività recente / log |
| `foundry model list --cached` | `foundry cache list` |
| `foundry model stats <model>` | Usare script di benchmark Python + strumenti OS (Task Manager / `nvidia-smi`) |
| `foundry model benchmark ...` | `samples/session03/benchmark_oss_models.py` |

### Benchmarking & Telemetria

- Latenza, p95, token/sec: `samples/session03/benchmark_oss_models.py`
- Latenza del primo token (streaming): impostare `BENCH_STREAM=1`
- Utilizzo delle risorse: monitor OS (Task Manager, Activity Monitor, `nvidia-smi`).

Man mano che nuovi comandi di telemetria CLI si stabilizzano a monte, possono essere incorporati con modifiche minime ai markdown delle sessioni.

### Lint Guard automatizzato

Un linter automatizzato impedisce la reintroduzione di pattern CLI deprecati all'interno di blocchi di codice recintati nei file markdown:

Script: `Workshop/scripts/lint_markdown_cli.py`

I pattern deprecati sono bloccati all'interno di recinti di codice.

Sostituzioni raccomandate:
| Deprecato | Sostituzione |
|-----------|-------------|
| `foundry model chat <a> "..."` | `foundry model run <a> --prompt "..."` |
| `model list --running` | `model list` |
| `model list --cached` | `cache list` |
| `model stats` | Script di benchmark + strumenti di sistema |
| `model benchmark` | `samples/session03/benchmark_oss_models.py` |
| `model list --available` | `model list` |

Esegui localmente:
```powershell
python Workshop\scripts\lint_markdown_cli.py --verbose
```

GitHub Action: `.github/workflows/markdown-cli-lint.yml` eseguito su ogni push & PR.

Hook pre-commit opzionale:
```bash
echo "python Workshop/scripts/lint_markdown_cli.py" > .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```

## Tabella di migrazione rapida CLI → SDK

| Compito | Comando CLI | Equivalente SDK (Python) | Note |
|---------|-------------|--------------------------|------|
| Eseguire un modello una volta (prompt) | `foundry model run phi-4-mini --prompt "Hello"` | `manager=FoundryLocalManager("phi-4-mini"); client=OpenAI(base_url=manager.endpoint, api_key=manager.api_key or "not-needed"); client.chat.completions.create(model=manager.get_model_info("phi-4-mini").id, messages=[{"role":"user","content":"Hello"}])` | L'SDK avvia automaticamente il servizio e la cache |
| Scaricare (cache) un modello | `foundry model download qwen2.5-0.5b` | `FoundryLocalManager("qwen2.5-0.5b")  # triggers download/load` | Il manager sceglie la variante migliore se l'alias corrisponde a più build |
| Elencare il catalogo | `foundry model list` | `# use manager for each alias or maintain known list` | Il CLI aggrega; l'SDK attualmente per alias |
| Elencare i modelli nella cache | `foundry cache list` | `manager.list_cached_models()` | Dopo l'inizializzazione del manager (qualsiasi alias) |
| Ottenere l'URL dell'endpoint | (implicito) | `manager.endpoint` | Utilizzato per creare un client compatibile con OpenAI |
| Riscaldare un modello | `foundry model run <alias>` poi primo prompt | `chat_once(alias, messages=[...])` (utility) | Le utility gestiscono il riscaldamento iniziale della latenza a freddo |
| Misurare la latenza | `python -m session03.benchmark_oss_models` | `import benchmark_oss_models` (o nuovo script di esportazione) | Preferire lo script per metriche coerenti |
| Arrestare / scaricare un modello | `foundry model unload <alias>` | (Non esposto – riavviare servizio / processo) | Tipicamente non richiesto per il flusso del workshop |
| Recuperare l'utilizzo dei token | (visualizzare output) | `resp.usage.total_tokens` | Fornito se il backend restituisce l'oggetto di utilizzo |

## Esportazione Benchmark Markdown

Utilizzare lo script `Workshop/scripts/export_benchmark_markdown.py` per eseguire un nuovo benchmark (stessa logica di `samples/session03/benchmark_oss_models.py`) e generare una tabella Markdown compatibile con GitHub più JSON grezzo.

### Esempio

```powershell
python Workshop\scripts\export_benchmark_markdown.py --models "qwen2.5-0.5b,mistral-7b" --prompt "Explain retrieval augmented generation briefly." --rounds 3 --output benchmark_report.md
```

File generati:
| File | Contenuti |
|------|----------|
| `benchmark_report.md` | Tabella Markdown + suggerimenti di interpretazione |
| `benchmark_report.json` | Array di metriche grezze (per differenze / monitoraggio delle tendenze) |

Impostare `BENCH_STREAM=1` nell'ambiente per includere la latenza del primo token se supportata.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire l'accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale umana. Non siamo responsabili per eventuali incomprensioni o interpretazioni errate derivanti dall'uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
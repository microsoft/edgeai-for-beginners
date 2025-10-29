<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "45923ada94573fee7c82cc4f0c3bb344",
  "translation_date": "2025-10-28T22:09:59+00:00",
  "source_file": "Workshop/Readme.md",
  "language_code": "da"
}
-->
# EdgeAI for Begyndere - Workshop

> **Praktisk læringsforløb til opbygning af produktionsklare Edge AI-applikationer**
>
> Bliv ekspert i lokal AI-implementering med Microsoft Foundry Local, fra første chat-komplettering til orkestrering af multi-agenter i 6 progressive sessioner.

---

## 🎯 Introduktion

Velkommen til **EdgeAI for Begyndere Workshop** - din praktiske guide til at bygge intelligente applikationer, der kører udelukkende på lokal hardware. Denne workshop omsætter teoretiske Edge AI-koncepter til praktiske færdigheder gennem gradvist udfordrende øvelser med Microsoft Foundry Local og Small Language Models (SLMs).

### Hvorfor denne workshop?

**Edge AI-revolutionen er her**

Organisationer verden over skifter fra cloud-afhængig AI til edge computing af tre vigtige grunde:

1. **Privatliv & Overholdelse** - Behandl følsomme data lokalt uden transmission til skyen (HIPAA, GDPR, finansielle reguleringer)
2. **Ydeevne** - Fjern netværkslatens (50-500ms lokalt vs 500-2000ms cloud round-trip)
3. **Omkostningskontrol** - Fjern per-token API-omkostninger og skaler uden skyudgifter

**Men Edge AI er anderledes**

At køre AI lokalt kræver nye færdigheder:
- Modelvalg og optimering til ressourcebegrænsninger
- Lokal serviceadministration og hardwareacceleration
- Prompt engineering til mindre modeller
- Produktionsimplementeringsmønstre for edge-enheder

**Denne workshop leverer disse færdigheder**

I 6 fokuserede sessioner (~3 timer i alt) vil du gå fra "Hello World" til at implementere produktionsklare multi-agent systemer - alt sammen kørende lokalt på din maskine.

---

## 📚 Læringsmål

Ved at gennemføre denne workshop vil du være i stand til:

### Kernekompetencer
1. **Implementere og administrere lokale AI-tjenester**
   - Installere og konfigurere Microsoft Foundry Local
   - Vælge passende modeller til edge-implementering
   - Administrere modellernes livscyklus (download, indlæsning, cache)
   - Overvåge ressourceforbrug og optimere ydeevne

2. **Bygge AI-drevne applikationer**
   - Implementere OpenAI-kompatible chat-kompletteringer lokalt
   - Designe effektive prompts til Small Language Models
   - Håndtere streaming-svar for bedre brugeroplevelse
   - Integrere lokale modeller i eksisterende applikationer

3. **Oprette RAG (Retrieval Augmented Generation) systemer**
   - Bygge semantisk søgning med embeddings
   - Forankre LLM-svar i domænespecifik viden
   - Evaluere RAG-kvalitet med industristandard-metrics
   - Skalere fra prototype til produktion

4. **Optimere modelydeevne**
   - Benchmarke flere modeller til din brugssag
   - Måle latens, gennemløb og første-token tid
   - Vælge optimale modeller baseret på hastighed/kvalitetsafvejninger
   - Sammenligne SLM vs LLM-afvejninger i virkelige scenarier

5. **Orkestrere multi-agent systemer**
   - Designe specialiserede agenter til forskellige opgaver
   - Implementere agenthukommelse og kontekststyring
   - Koordinere agenter i komplekse arbejdsgange
   - Rute forespørgsler intelligent på tværs af flere modeller

6. **Implementere produktionsklare løsninger**
   - Implementere fejlhåndtering og genforsøgslogik
   - Overvåge tokenforbrug og systemressourcer
   - Bygge skalerbare arkitekturer med model-as-tools mønstre
   - Planlægge migrationsveje fra edge til hybrid (edge + cloud)

---

## 🎓 Læringsresultater

### Hvad du vil bygge

Ved afslutningen af denne workshop vil du have skabt:

| Session | Leverance | Demonstrerede færdigheder |
|---------|-----------|---------------------------|
| **1** | Chat-applikation med streaming | Serviceopsætning, grundlæggende kompletteringer, streaming UX |
| **2** | RAG-system med evaluering | Embeddings, semantisk søgning, kvalitetsmetrics |
| **3** | Multi-model benchmark suite | Ydeevnemåling, model-sammenligning |
| **4** | SLM vs LLM sammenligning | Afvejningsanalyse, optimeringsstrategier |
| **5** | Multi-agent orkestrator | Agentdesign, hukommelsesstyring, koordinering |
| **6** | Intelligent routingsystem | Intentiondetektion, modelvalg, skalerbarhed |

### Kompetencematrix

| Færdighedsniveau | Session 1-2 | Session 3-4 | Session 5-6 |
|------------------|-------------|-------------|-------------|
| **Begynder** | ✅ Opsætning & grundlæggende | ⚠️ Udfordrende | ❌ For avanceret |
| **Mellem** | ✅ Hurtig gennemgang | ✅ Kerneindlæring | ⚠️ Strækmål |
| **Avanceret** | ✅ Let at gennemføre | ✅ Forfining | ✅ Produktionsmønstre |

### Karriereklare færdigheder

**Efter denne workshop vil du være klar til:**

✅ **Bygge privatlivsfokuserede applikationer**
- Sundhedsapps, der håndterer PHI/PII lokalt
- Finansielle tjenester med overholdelseskrav
- Offentlige systemer med krav om datasuverænitet

✅ **Optimere til edge-miljøer**
- IoT-enheder med begrænsede ressourcer
- Offline-først mobilapplikationer
- Lav-latens realtidssystemer

✅ **Designe intelligente arkitekturer**
- Multi-agent systemer til komplekse arbejdsgange
- Hybrid edge-cloud implementeringer
- Omkostningsoptimeret AI-infrastruktur

✅ **Lede Edge AI-initiativer**
- Evaluere Edge AI's gennemførlighed for projekter
- Vælge passende modeller og rammer
- Arkitektere skalerbare lokale AI-løsninger

---

## 🗺️ Workshopstruktur

### Sessionoversigt (6 sessioner × 30 minutter = 3 timer)

| Session | Emne | Fokus | Varighed |
|---------|------|-------|----------|
| **1** | Kom godt i gang med Foundry Local | Installér, valider, første kompletteringer | 30 min |
| **2** | Bygge AI-løsninger med RAG | Prompt engineering, embeddings, evaluering | 30 min |
| **3** | Open Source-modeller | Modelopdagelse, benchmarking, valg | 30 min |
| **4** | Cutting Edge-modeller | SLM vs LLM, optimering, rammer | 30 min |
| **5** | AI-drevne agenter | Agentdesign, orkestrering, hukommelse | 30 min |
| **6** | Modeller som værktøjer | Routing, kædning, skaleringsstrategier | 30 min |

---

## 🚀 Hurtig start

### Forudsætninger

**Systemkrav:**
- **OS**: Windows 10/11, macOS 11+ eller Linux (Ubuntu 20.04+)
- **RAM**: Minimum 8GB, anbefalet 16GB+
- **Lagring**: 10GB+ ledig plads til modeller
- **CPU**: Moderne processor med AVX2-understøttelse
- **GPU** (valgfrit): CUDA-kompatibel eller Qualcomm NPU til acceleration

**Softwarekrav:**
- **Python 3.8+** ([Download](https://www.python.org/downloads/))
- **Microsoft Foundry Local** ([Installationsguide](../../../Workshop))
- **Git** ([Download](https://git-scm.com/downloads))
- **Visual Studio Code** (anbefalet) ([Download](https://code.visualstudio.com/))

### Opsætning i 3 trin

#### 1. Installér Foundry Local

**Windows:**
```powershell
winget install Microsoft.FoundryLocal
```

**macOS:**
```bash
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**Verificér installation:**
```bash
foundry --version
foundry service status
```

**Sørg for, at Azure AI Foundry Local kører med en fast port**

```bash
# Set FoundryLocal to use port 58123 (default)
foundry service set --port 58123 --show

# Or use a different port
foundry service set --port 58000 --show
```

**Verificér funktionalitet:**
```bash
# Check service status
foundry service status

# Test the endpoint
curl http://127.0.0.1:58123/v1/models
```
**Find tilgængelige modeller**
For at se hvilke modeller der er tilgængelige i din Foundry Local-instans, kan du forespørge modeller-endpointet:

```bash
# cmd/bash/powershell
foundry model list
```

Brug web-endpoint 

```bash
# Windows PowerShell
powershell -Command "Invoke-RestMethod -Uri 'http://127.0.0.1:58123/v1/models' -Method Get"

# Or using curl (if available)
curl http://127.0.0.1:58123/v1/models
```

#### 2. Klon repository & installér afhængigheder

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

#### 3. Kør dit første eksempel

```bash
# Start Foundry Local and load a model
foundry model run phi-4-mini

# Run the chat bootstrap sample
cd samples
python -m session01.chat_bootstrap "What is edge AI?"
```

**✅ Succes!** Du bør se et streaming-svar om edge AI.

---

## 📦 Workshopressourcer

### Python-eksempler

Progressive praktiske eksempler, der demonstrerer hvert koncept:

| Session | Eksempel | Beskrivelse | Kørselstid |
|---------|----------|-------------|------------|
| 1 | [`chat_bootstrap.py`](../../../Workshop/samples/session01/chat_bootstrap.py) | Grundlæggende & streaming chat | ~30s |
| 2 | [`rag_pipeline.py`](../../../Workshop/samples/session02/rag_pipeline.py) | RAG med embeddings | ~45s |
| 2 | [`rag_eval_ragas.py`](../../../Workshop/samples/session02/rag_eval_ragas.py) | RAG-kvalitetsevaluering | ~60s |
| 3 | [`benchmark_oss_models.py`](../../../Workshop/samples/session03/benchmark_oss_models.py) | Multi-model benchmarking | ~2-3m |
| 4 | [`model_compare.py`](../../../Workshop/samples/session04/model_compare.py) | SLM vs LLM sammenligning | ~45s |
| 5 | [`agents_orchestrator.py`](../../../Workshop/samples/session05/agents_orchestrator.py) | Multi-agent system | ~60s |
| 6 | [`models_router.py`](../../../Workshop/samples/session06/models_router.py) | Intention-baseret routing | ~45s |
| 6 | [`models_pipeline.py`](../../../Workshop/samples/session06/models_pipeline.py) | Multi-step pipeline | ~60s |

### Jupyter Notebooks

Interaktiv udforskning med forklaringer og visualiseringer:

| Session | Notebook | Beskrivelse | Sværhedsgrad |
|---------|----------|-------------|--------------|
| 1 | [`session01_chat_bootstrap.ipynb`](./notebooks/session01_chat_bootstrap.ipynb) | Chat-grundlæggende & streaming | ⭐ Begynder |
| 2 | [`session02_rag_pipeline.ipynb`](./notebooks/session02_rag_pipeline.ipynb) | Byg RAG-system | ⭐⭐ Mellem |
| 2 | [`session02_rag_eval_ragas.ipynb`](./notebooks/session02_rag_eval_ragas.ipynb) | Evaluer RAG-kvalitet | ⭐⭐ Mellem |
| 3 | [`session03_benchmark_oss_models.ipynb`](./notebooks/session03_benchmark_oss_models.ipynb) | Modelbenchmarking | ⭐⭐ Mellem |
| 4 | [`session04_model_compare.ipynb`](./notebooks/session04_model_compare.ipynb) | Modelsammenligning | ⭐⭐ Mellem |
| 5 | [`session05_agents_orchestrator.ipynb`](./notebooks/session05_agents_orchestrator.ipynb) | Agentorkestrering | ⭐⭐⭐ Avanceret |
| 6 | [`session06_models_router.ipynb`](./notebooks/session06_models_router.ipynb) | Intention-routing | ⭐⭐⭐ Avanceret |
| 6 | [`session06_models_pipeline.ipynb`](./notebooks/session06_models_pipeline.ipynb) | Pipeline-orkestrering | ⭐⭐⭐ Avanceret |

### Dokumentation

Omfattende vejledninger og referencer:

| Dokument | Beskrivelse | Brug når |
|----------|-------------|----------|
| [QUICK_START.md](./QUICK_START.md) | Hurtig opsætningsguide | Starter fra bunden |
| [QUICK_REFERENCE.md](./QUICK_REFERENCE.md) | Kommando- & API-cheat sheet | Har brug for hurtige svar |
| [FOUNDRY_SDK_QUICKREF.md](./FOUNDRY_SDK_QUICKREF.md) | SDK-mønstre & eksempler | Skriver kode |
| [ENV_CONFIGURATION.md](./ENV_CONFIGURATION.md) | Guide til miljøvariabler | Konfigurerer eksempler |
| [SAMPLES_UPDATE_SUMMARY.md](./SAMPLES_UPDATE_SUMMARY.md) | Seneste forbedringer af eksempler | Forstår ændringer |
| [SDK_MIGRATION_NOTES.md](./SDK_MIGRATION_NOTES.md) | Migrationsguide | Opgraderer kode |
| [notebooks/TROUBLESHOOTING.md](./notebooks/TROUBLESHOOTING.md) | Almindelige problemer & løsninger | Fejlfinding |

---

## 🎓 Anbefalinger til læringsforløb

### For begyndere (3-4 timer)
1. ✅ Session 1: Kom godt i gang (fokus på opsætning og grundlæggende chat)
2. ✅ Session 2: RAG-grundlæggende (spring evaluering over i første omgang)
3. ✅ Session 3: Enkel benchmarking (kun 2 modeller)
4. ⏭️ Spring sessionerne 4-6 over for nu
5. 🔄 Vend tilbage til sessionerne 4-6 efter at have bygget første applikation

### For mellemudviklere (3 timer)
1. ⚡ Session 1: Hurtig opsætningsvalidering
2. ✅ Session 2: Fuld RAG-pipeline med evaluering
3. ✅ Session 3: Fuld benchmark-suite
4. ✅ Session 4: Modeloptimering
5. ✅ Sessionerne 5-6: Fokus på arkitektur-mønstre

### For avancerede praktikere (2-3 timer)
1. ⚡ Sessionerne 1-3: Hurtig gennemgang og validering
2. ✅ Session 4: Optimeringsdybdegående
3. ✅ Session 5: Multi-agent arkitektur
4. ✅ Session 6: Produktionsmønstre og skalering
5. 🚀 Udvid: Byg brugerdefineret routing-logik og hybridimplementeringer

---

## Workshop Session Pack (Fokuserede 30-minutters labs)

Hvis du følger det komprimerede 6-sessioners workshopformat, brug disse dedikerede guides (hver matcher og supplerer de bredere modul-dokumenter ovenfor):

| Workshop Session | Guide | Kernefokus |
|------------------|-------|------------|
| 1 | [Session01-GettingStartedFoundryLocal](./Session01-GettingStartedFoundryLocal.md) | Installér, valider, kør phi & GPT-OSS-20B, acceleration |
| 2 | [Session02-BuildAISolutionsRAG](./Session02-BuildAISolutionsRAG.md) | Prompt engineering, RAG-mønstre, CSV & dokumentforankring, migration |
| 3 | [Session03-OpenSourceModels](./Session03-OpenSourceModels.md) | Hugging Face-integration, benchmarking, modelvalg |
| 4 | [Session04-CuttingEdgeModels](./Session04-CuttingEdgeModels.md) | SLM vs LLM, WebGPU, Chainlit RAG, ONNX acceleration |
| 5 | [Session05-AIPoweredAgents](./Session05-AIPoweredAgents.md) | Agentroller, hukommelse, værktøjer, orkestrering |
| 6 | [Session06-ModelsAsTools](./Session06-ModelsAsTools.md) | Routing, kædning, skalering til Azure |

Hver sessionsfil inkluderer: abstrakt, læringsmål, 30-minutters demo-flow, startprojekt, valideringscheckliste, fejlfinding og referencer til den officielle Foundry Local Python SDK.

### Eksempelscripts

Installer workshop-afhængigheder (Windows):

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

Hvis Foundry Local-tjenesten kører på en anden (Windows) maskine eller VM fra macOS, eksportér endpointet:

```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```

| Session | Script(s) | Beskrivelse |
|---------|-----------|-------------|
| 1 | `samples/session01/chat_bootstrap.py` | Bootstrap-tjeneste & streaming-chat |
| 2 | `samples/session02/rag_pipeline.py` | Minimal RAG (in-memory embeddings) |
|   | `samples/session02/rag_eval_ragas.py` | RAG-evaluering med ragas-metrics |
| 3 | `samples/session03/benchmark_oss_models.py` | Multi-model latenstid & throughput benchmarking |
| 4 | `samples/session04/model_compare.py` | SLM vs LLM sammenligning (latenstid & eksempeloutput) |
| 5 | `samples/session05/agents_orchestrator.py` | To-agent forsknings- → redaktionel pipeline |
| 6 | `samples/session06/models_router.py` | Intent-baseret routing-demo |
|   | `samples/session06/models_pipeline.py` | Multi-step plan/execute/refine kæde |

### Miljøvariabler (fælles for alle eksempler)

| Variabel | Formål | Eksempel |
|----------|---------|---------|
| `FOUNDRY_LOCAL_ALIAS` | Standard enkeltmodel-alias for grundlæggende eksempler | `phi-4-mini` |
| `SLM_ALIAS` / `LLM_ALIAS` | Eksplicit SLM vs større model til sammenligning | `phi-4-mini` / `gpt-oss-20b` |
| `BENCH_MODELS` | Komma-separeret liste over aliaser til benchmarking | `qwen2.5-0.5b,mistral-7b` |
| `BENCH_ROUNDS` | Benchmark gentagelser pr. model | `3` |
| `BENCH_PROMPT` | Prompt brugt i benchmarking | `Explain retrieval augmented generation briefly.` |
| `EMBED_MODEL` | Sentence-transformers embedding model | `sentence-transformers/all-MiniLM-L6-v2` |
| `RAG_QUESTION` | Overstyr testforespørgsel for RAG-pipeline | `Why use RAG with local inference?` |
| `AGENT_QUESTION` | Overstyr agents-pipeline forespørgsel | `Explain why edge AI matters for compliance.` |
| `AGENT_MODEL_PRIMARY` | Model-alias for forskningsagent | `phi-4-mini` |
| `AGENT_MODEL_EDITOR` | Model-alias for redaktøragent (kan variere) | `gpt-oss-20b` |
| `SHOW_USAGE` | Når `1`, udskriver tokenforbrug pr. afslutning | `1` |
| `RETRY_ON_FAIL` | Når `1`, prøv igen én gang ved midlertidige chatfejl | `1` |
| `RETRY_BACKOFF` | Sekunder at vente før genforsøg | `1.0` |

Hvis en variabel ikke er sat, falder scripts tilbage til fornuftige standardindstillinger. For enkeltmodel-demoer behøver du typisk kun `FOUNDRY_LOCAL_ALIAS`.

### Hjælpemodul

Alle eksempler deler nu en hjælper `samples/workshop_utils.py`, der tilbyder:

* Cachet `FoundryLocalManager` + OpenAI-klientoprettelse
* `chat_once()`-hjælper med valgfrit genforsøg + brugerapportering
* Enkel tokenforbrugsrapportering (aktiver via `SHOW_USAGE=1`)

Dette reducerer duplikering og fremhæver bedste praksis for effektiv lokal modelorkestrering.

## Valgfrie forbedringer (på tværs af sessioner)

| Tema | Forbedring | Sessioner | Miljø / Skift |
|-------|-------------|----------|--------------|
| Determinisme | Fast temperatur + stabile prompt-sæt | 1–6 | Sæt `temperature=0`, `top_p=1` |
| Synlighed af tokenforbrug | Konsistent undervisning i omkostninger/effektivitet | 1–6 | `SHOW_USAGE=1` |
| Streaming af første token | Opfattet latenstidsmåling | 1,3,4,6 | `BENCH_STREAM=1` (benchmark) |
| Genforsøg robusthed | Håndterer midlertidig koldstart | Alle | `RETRY_ON_FAIL=1` + `RETRY_BACKOFF` |
| Multi-model agenter | Heterogen rolle-specialisering | 5 | `AGENT_MODEL_PRIMARY`, `AGENT_MODEL_EDITOR` |
| Adaptiv routing | Intent + omkostningsheuristik | 6 | Udvid router med eskaleringslogik |
| Vektormemory | Langsigtet semantisk hukommelse | 2,5,6 | Integrer FAISS/Chroma embedding index |
| Spor eksport | Revision & evaluering | 2,5,6 | Tilføj JSON-linjer pr. trin |
| Kvalitetsrubrikker | Kvalitativ sporing | 3–6 | Sekundære scoringsprompter |
| Røgtests | Hurtig validering før workshop | Alle | `python Workshop/tests/smoke.py` |

### Deterministisk hurtig start

```powershell
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
python Workshop\tests\smoke.py
```

Forvent stabile tokenantal på tværs af gentagne identiske input.

### RAG-evaluering (Session 2)

Brug `rag_eval_ragas.py` til at beregne svarrelevans, troværdighed og kontekstpræcision på et lille syntetisk datasæt:

```powershell
cd Workshop/samples
python -m session02.rag_eval_ragas
```

Udvid ved at levere en større JSONL med spørgsmål, kontekster og sandheder og konverter derefter til et Hugging Face `Dataset`.

## CLI-kommando nøjagtighedsappendiks

Workshoppen bruger bevidst kun aktuelt dokumenterede / stabile Foundry Local CLI-kommandoer.

### Refererede stabile kommandoer

| Kategori | Kommando | Formål |
|----------|---------|---------|
| Kerne | `foundry --version` | Vis installeret version |
| Kerne | `foundry init` | Initialiser konfiguration |
| Tjeneste | `foundry service start` | Start lokal tjeneste (hvis ikke automatisk) |
| Tjeneste | `foundry status` | Vis tjenestens status |
| Modeller | `foundry model list` | Liste over katalog / tilgængelige modeller |
| Modeller | `foundry model download <alias>` | Download modelvægt til cache |
| Modeller | `foundry model run <alias>` | Start (indlæs) en model lokalt; kombiner med `--prompt` for one-shot |
| Modeller | `foundry model unload <alias>` / `foundry model stop <alias>` | Fjern en model fra hukommelsen (hvis understøttet) |
| Cache | `foundry cache list` | Liste over cachede (downloadede) modeller |
| System | `foundry system info` | Snapshot af hardware & accelerationskapaciteter |
| System | `foundry system gpu-info` | GPU-diagnostisk info |
| Konfig | `foundry config list` | Vis aktuelle konfigurationsværdier |
| Konfig | `foundry config set <key> <value>` | Opdater konfiguration |

### One-Shot Prompt-mønster

I stedet for en forældet `model chat` underkommando, brug:

```powershell
foundry model run <alias> --prompt "Your question here"
```

Dette udfører en enkelt prompt/svar-cyklus og afslutter derefter.

### Fjernede / undgåede mønstre

| Forældet / Udokumenteret | Erstatning / Vejledning |
|---------------------------|------------------------|
| `foundry model chat <model> "..."` | `foundry model run <model> --prompt "..."` |
| `foundry model list --running` | Brug almindelig `foundry model list` + nylig aktivitet / logs |
| `foundry model list --cached` | `foundry cache list` |
| `foundry model stats <model>` | Brug benchmark Python-script + OS-værktøjer (Task Manager / `nvidia-smi`) |
| `foundry model benchmark ...` | `samples/session03/benchmark_oss_models.py` |

### Benchmarking & Telemetri

- Latenstid, p95, tokens/sek.: `samples/session03/benchmark_oss_models.py`
- Første-token latenstid (streaming): sæt `BENCH_STREAM=1`
- Ressourceforbrug: OS-monitorer (Task Manager, Activity Monitor, `nvidia-smi`) + `foundry system info`.

Når nye CLI-telemetrikommandoer stabiliseres upstream, kan de integreres med minimale ændringer i session markdowns.

### Automatisk lint-guard

En automatisk linter forhindrer genindførelse af forældede CLI-mønstre inden for indhegnede kodeblokke i markdown-filer:

Script: `Workshop/scripts/lint_markdown_cli.py`

Forældede mønstre blokeres inden for kodehegn.

Anbefalede erstatninger:
| Forældet | Erstatning |
|------------|-------------|
| `foundry model chat <a> "..."` | `foundry model run <a> --prompt "..."` |
| `model list --running` | `model list` |
| `model list --cached` | `cache list` |
| `model stats` | Benchmark-script + systemværktøjer |
| `model benchmark` | `samples/session03/benchmark_oss_models.py` |
| `model list --available` | `model list` |

Kør lokalt:
```powershell
python Workshop\scripts\lint_markdown_cli.py --verbose
```

GitHub Action: `.github/workflows/markdown-cli-lint.yml` kører ved hver push & PR.

Valgfri pre-commit hook:
```bash
echo "python Workshop/scripts/lint_markdown_cli.py" > .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```

## Hurtig CLI → SDK-migrationstabel

| Opgave | CLI One-Liner | SDK (Python) Equivalent | Noter |
|------|---------------|-------------------------|-------|
| Kør en model én gang (prompt) | `foundry model run phi-4-mini --prompt "Hello"` | `manager=FoundryLocalManager("phi-4-mini"); client=OpenAI(base_url=manager.endpoint, api_key=manager.api_key or "not-needed"); client.chat.completions.create(model=manager.get_model_info("phi-4-mini").id, messages=[{"role":"user","content":"Hello"}])` | SDK bootstrapper tjeneste & caching automatisk |
| Download (cache) model | `foundry model download qwen2.5-0.5b` | `FoundryLocalManager("qwen2.5-0.5b")  # triggers download/load` | Manager vælger bedste variant, hvis aliaset matcher flere builds |
| Liste over katalog | `foundry model list` | `# brug manager for hvert alias eller vedligehold kendt liste` | CLI samler; SDK i øjeblikket pr. alias-initialisering |
| Liste over cachede modeller | `foundry cache list` | `manager.list_cached_models()` | Efter manager-init (ethvert alias) |
| Aktiver GPU-acceleration | `foundry config set compute.onnx.enable_gpu true` | `# CLI-handling; SDK antager, at konfiguration allerede er anvendt` | Konfiguration er en ekstern sideeffekt |
| Få endpoint-URL | (implicit) | `manager.endpoint` | Bruges til at oprette OpenAI-kompatibel klient |
| Varm en model op | `foundry model run <alias>` derefter første prompt | `chat_once(alias, messages=[...])` (utility) | Utilities håndterer initial kold latenstid opvarmning |
| Mål latenstid | `python -m session03.benchmark_oss_models` | `import benchmark_oss_models` (eller nyt eksportscript) | Foretræk script for konsistente metrics |
| Stop / fjern model | `foundry model unload <alias>` | (Ikke eksponeret – genstart tjeneste / proces) | Typisk ikke nødvendigt for workshop-flow |
| Hent tokenforbrug | (vis output) | `resp.usage.total_tokens` | Tilbydes, hvis backend returnerer usage-objekt |

## Benchmark Markdown-eksport

Brug scriptet `Workshop/scripts/export_benchmark_markdown.py` til at køre en frisk benchmark (samme logik som `samples/session03/benchmark_oss_models.py`) og udgive en GitHub-venlig Markdown-tabel plus rå JSON.

### Eksempel

```powershell
python Workshop\scripts\export_benchmark_markdown.py --models "qwen2.5-0.5b,mistral-7b" --prompt "Explain retrieval augmented generation briefly." --rounds 3 --output benchmark_report.md
```

Genererede filer:
| Fil | Indhold |
|------|----------|
| `benchmark_report.md` | Markdown-tabel + fortolkningshint |
| `benchmark_report.json` | Rå metrics-array (til diffing / trendsporing) |

Sæt `BENCH_STREAM=1` i miljøet for at inkludere første-token latenstid, hvis understøttet.

---

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal det bemærkes, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi er ikke ansvarlige for eventuelle misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
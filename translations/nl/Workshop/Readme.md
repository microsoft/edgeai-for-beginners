<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "04951692a100dcd716df01efca2d3f0d",
  "translation_date": "2025-11-11T23:32:03+00:00",
  "source_file": "Workshop/Readme.md",
  "language_code": "nl"
}
-->
# EdgeAI voor Beginners - Workshop

> **Praktisch leertraject voor het bouwen van productieklare Edge AI-toepassingen**
>
> Beheers lokale AI-implementatie met Microsoft Foundry Local, van eerste chatcompletion tot multi-agent orkestratie in 6 progressieve sessies.

---

## 🎯 Introductie

Welkom bij de **EdgeAI voor Beginners Workshop** - jouw praktische gids voor het bouwen van intelligente toepassingen die volledig op lokale hardware draaien. Deze workshop vertaalt theoretische Edge AI-concepten naar praktische vaardigheden door middel van steeds uitdagendere oefeningen met Microsoft Foundry Local en Small Language Models (SLMs).

### Waarom deze workshop?

**De Edge AI-revolutie is hier**

Organisaties wereldwijd verschuiven van cloud-afhankelijke AI naar edge computing om drie belangrijke redenen:

1. **Privacy & Compliance** - Verwerk gevoelige gegevens lokaal zonder cloudtransmissie (HIPAA, GDPR, financiële regelgeving)
2. **Prestaties** - Elimineer netwerkvertraging (50-500ms lokaal vs 500-2000ms cloud round-trip)
3. **Kostenbeheersing** - Verminder kosten per token en schaal zonder clouduitgaven

**Maar Edge AI is anders**

AI lokaal draaien vereist nieuwe vaardigheden:
- Modelselectie en optimalisatie voor beperkte middelen
- Beheer van lokale services en hardwareversnelling
- Prompt engineering voor kleinere modellen
- Productie-implementatiepatronen voor edge-apparaten

**Deze workshop levert die vaardigheden**

In 6 gerichte sessies (~3 uur totaal) ga je van "Hello World" naar het implementeren van productieklare multi-agent systemen - allemaal lokaal draaiend op jouw machine.

---

## 📚 Leerdoelen

Door deze workshop te voltooien, kun je:

### Kerncompetenties
1. **Lokale AI-services implementeren en beheren**
   - Installeer en configureer Microsoft Foundry Local
   - Selecteer geschikte modellen voor edge-implementatie
   - Beheer de levenscyclus van modellen (downloaden, laden, cachen)
   - Monitor resourcegebruik en optimaliseer prestaties

2. **AI-aangedreven toepassingen bouwen**
   - Implementeer OpenAI-compatibele chatcompletions lokaal
   - Ontwerp effectieve prompts voor Small Language Models
   - Verwerk streamingreacties voor een betere gebruikerservaring
   - Integreer lokale modellen in bestaande toepassingen

3. **RAG (Retrieval Augmented Generation) systemen creëren**
   - Bouw semantisch zoeken met embeddings
   - Baseer LLM-reacties op domeinspecifieke kennis
   - Evalueer RAG-kwaliteit met industriestandaard metrics
   - Schaal van prototype naar productie

4. **Modelprestaties optimaliseren**
   - Benchmark meerdere modellen voor jouw use case
   - Meet latency, throughput en first-token tijd
   - Selecteer optimale modellen op basis van snelheid/kwaliteitsafwegingen
   - Vergelijk SLM vs LLM afwegingen in echte scenario's

5. **Multi-agent systemen orkestreren**
   - Ontwerp gespecialiseerde agents voor verschillende taken
   - Implementeer agentgeheugen en contextbeheer
   - Coördineer agents in complexe workflows
   - Verwerk verzoeken intelligent over meerdere modellen

6. **Productieklare oplossingen implementeren**
   - Implementeer foutafhandeling en retry-logica
   - Monitor tokengebruik en systeemresources
   - Bouw schaalbare architecturen met model-as-tools patronen
   - Plan migratiepaden van edge naar hybride (edge + cloud)

---

## 🎓 Leerresultaten

### Wat je gaat bouwen

Aan het einde van deze workshop heb je het volgende gecreëerd:

| Sessie | Resultaat | Vaardigheden gedemonstreerd |
|--------|-----------|----------------------------|
| **1** | Chattoepassing met streaming | Service setup, basiscompletions, streaming UX |
| **2** | RAG-systeem met evaluatie | Embeddings, semantisch zoeken, kwaliteitsmetrics |
| **3** | Multi-model benchmark suite | Prestatiemeting, modelvergelijking |
| **4** | SLM vs LLM comparator | Afweginganalyse, optimalisatiestrategieën |
| **5** | Multi-agent orkestrator | Agentontwerp, geheugenbeheer, coördinatie |
| **6** | Intelligentsysteem voor routering | Intentdetectie, modelselectie, schaalbaarheid |

### Competentiematrix

| Vaardigheidsniveau | Sessie 1-2 | Sessie 3-4 | Sessie 5-6 |
|--------------------|------------|------------|------------|
| **Beginner** | ✅ Setup & basis | ⚠️ Uitdagend | ❌ Te geavanceerd |
| **Gemiddeld** | ✅ Snelle review | ✅ Kernleren | ⚠️ Stretchdoelen |
| **Gevorderd** | ✅ Makkelijk doorlopen | ✅ Verfijning | ✅ Productiepatronen |

### Vaardigheden voor de arbeidsmarkt

**Na deze workshop ben je voorbereid om:**

✅ **Privacy-eerste toepassingen te bouwen**
- Zorgtoepassingen die PHI/PII lokaal verwerken
- Financiële diensten met nalevingsvereisten
- Overheidssystemen met datasoevereiniteitsbehoeften

✅ **Optimaliseren voor edge-omgevingen**
- IoT-apparaten met beperkte middelen
- Offline-first mobiele toepassingen
- Laag-latentie real-time systemen

✅ **Intelligente architecturen ontwerpen**
- Multi-agent systemen voor complexe workflows
- Hybride edge-cloud implementaties
- Kosten-geoptimaliseerde AI-infrastructuur

✅ **Edge AI-initiatieven leiden**
- Edge AI haalbaarheid evalueren voor projecten
- Geschikte modellen en frameworks selecteren
- Schaalbare lokale AI-oplossingen ontwerpen

---

## 🗺️ Workshopstructuur

### Sessies Overzicht (6 sessies × 30 minuten = 3 uur)

| Sessie | Onderwerp | Focus | Duur |
|--------|-----------|-------|------|
| **1** | Aan de slag met Foundry Local | Installeren, valideren, eerste completions | 30 min |
| **2** | AI-oplossingen bouwen met RAG | Prompt engineering, embeddings, evaluatie | 30 min |
| **3** | Open Source Modellen | Modelontdekking, benchmarking, selectie | 30 min |
| **4** | Cutting Edge Modellen | SLM vs LLM, optimalisatie, frameworks | 30 min |
| **5** | AI-aangedreven agents | Agentontwerp, orkestratie, geheugen | 30 min |
| **6** | Modellen als tools | Routering, chaining, schaalstrategieën | 30 min |

---

## 🚀 Snel starten

### Vereisten

**Systeemvereisten:**
- **OS**: Windows 10/11, macOS 11+, of Linux (Ubuntu 20.04+)
- **RAM**: Minimaal 8GB, aanbevolen 16GB+
- **Opslag**: Minimaal 10GB vrije ruimte voor modellen
- **CPU**: Moderne processor met AVX2-ondersteuning
- **GPU** (optioneel): CUDA-compatibel of Qualcomm NPU voor versnelling

**Softwarevereisten:**
- **Python 3.8+** ([Download](https://www.python.org/downloads/))
- **Microsoft Foundry Local** ([Installatiegids](../../../Workshop))
- **Git** ([Download](https://git-scm.com/downloads))
- **Visual Studio Code** (aanbevolen) ([Download](https://code.visualstudio.com/))

### Setup in 3 stappen

#### 1. Installeer Foundry Local

**Windows:**
```powershell
winget install Microsoft.FoundryLocal
```

**macOS:**
```bash
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**Installatie verifiëren:**
```bash
foundry --version
foundry service status
```

**Zorg ervoor dat Azure AI Foundry Local draait met een vaste poort**

```bash
# Set FoundryLocal to use port 58123 (default)
foundry service set --port 58123 --show

# Or use a different port
foundry service set --port 58000 --show
```

**Controleer of het werkt:**
```bash
# Check service status
foundry service status

# Test the endpoint
curl http://127.0.0.1:58123/v1/models
```
**Beschikbare modellen vinden**
Om te zien welke modellen beschikbaar zijn in jouw Foundry Local-instantie, kun je de models endpoint opvragen:

```bash
# cmd/bash/powershell
foundry model list
```

Via Web Endpoint 

```bash
# Windows PowerShell
powershell -Command "Invoke-RestMethod -Uri 'http://127.0.0.1:58123/v1/models' -Method Get"

# Or using curl (if available)
curl http://127.0.0.1:58123/v1/models
```

#### 2. Repository klonen & afhankelijkheden installeren

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

#### 3. Voer je eerste voorbeeld uit

```bash
# Start Foundry Local and load a model
foundry model run phi-4-mini

# Run the chat bootstrap sample
cd samples
python -m session01.chat_bootstrap "What is edge AI?"
```

**✅ Succes!** Je zou een streamingreactie moeten zien over edge AI.

---

## 📦 Workshopbronnen

### Python Voorbeelden

Progressieve hands-on voorbeelden die elk concept demonstreren:

| Sessie | Voorbeeld | Beschrijving | Uitvoeringstijd |
|--------|-----------|--------------|-----------------|
| 1 | [`chat_bootstrap.py`](../../../Workshop/samples/session01/chat_bootstrap.py) | Basis & streaming chat | ~30s |
| 2 | [`rag_pipeline.py`](../../../Workshop/samples/session02/rag_pipeline.py) | RAG met embeddings | ~45s |
| 2 | [`rag_eval_ragas.py`](../../../Workshop/samples/session02/rag_eval_ragas.py) | RAG kwaliteitsevaluatie | ~60s |
| 3 | [`benchmark_oss_models.py`](../../../Workshop/samples/session03/benchmark_oss_models.py) | Multi-model benchmarking | ~2-3m |
| 4 | [`model_compare.py`](../../../Workshop/samples/session04/model_compare.py) | SLM vs LLM vergelijking | ~45s |
| 5 | [`agents_orchestrator.py`](../../../Workshop/samples/session05/agents_orchestrator.py) | Multi-agent systeem | ~60s |
| 6 | [`models_router.py`](../../../Workshop/samples/session06/models_router.py) | Intent-gebaseerde routering | ~45s |
| 6 | [`models_pipeline.py`](../../../Workshop/samples/session06/models_pipeline.py) | Multi-step pipeline | ~60s |

### Jupyter Notebooks

Interactieve verkenning met uitleg en visualisaties:

| Sessie | Notebook | Beschrijving | Moeilijkheidsgraad |
|--------|----------|--------------|--------------------|
| 1 | [`session01_chat_bootstrap.ipynb`](./notebooks/session01_chat_bootstrap.ipynb) | Chat basis & streaming | ⭐ Beginner |
| 2 | [`session02_rag_pipeline.ipynb`](./notebooks/session02_rag_pipeline.ipynb) | Bouw RAG systeem | ⭐⭐ Gemiddeld |
| 2 | [`session02_rag_eval_ragas.ipynb`](./notebooks/session02_rag_eval_ragas.ipynb) | Evalueer RAG kwaliteit | ⭐⭐ Gemiddeld |
| 3 | [`session03_benchmark_oss_models.ipynb`](./notebooks/session03_benchmark_oss_models.ipynb) | Model benchmarking | ⭐⭐ Gemiddeld |
| 4 | [`session04_model_compare.ipynb`](./notebooks/session04_model_compare.ipynb) | Modelvergelijking | ⭐⭐ Gemiddeld |
| 5 | [`session05_agents_orchestrator.ipynb`](./notebooks/session05_agents_orchestrator.ipynb) | Agent orkestratie | ⭐⭐⭐ Geavanceerd |
| 6 | [`session06_models_router.ipynb`](./notebooks/session06_models_router.ipynb) | Intent routering | ⭐⭐⭐ Geavanceerd |
| 6 | [`session06_models_pipeline.ipynb`](./notebooks/session06_models_pipeline.ipynb) | Pipeline orkestratie | ⭐⭐⭐ Geavanceerd |

### Documentatie

Uitgebreide gidsen en referenties:

| Document | Beschrijving | Gebruik wanneer |
|----------|--------------|-----------------|
| [QUICK_START.md](./QUICK_START.md) | Snelle setupgids | Beginnen vanaf nul |
| [QUICK_REFERENCE.md](./QUICK_REFERENCE.md) | Command & API spiekbriefje | Snel antwoorden nodig |
| [FOUNDRY_SDK_QUICKREF.md](./FOUNDRY_SDK_QUICKREF.md) | SDK patronen & voorbeelden | Code schrijven |
| [ENV_CONFIGURATION.md](./ENV_CONFIGURATION.md) | Gids voor omgevingsvariabelen | Samples configureren |
| [notebooks/TROUBLESHOOTING.md](./notebooks/TROUBLESHOOTING.md) | Veelvoorkomende problemen & oplossingen | Problemen oplossen |

---

## 🎓 Aanbevelingen voor het leertraject

### Voor beginners (3-4 uur)
1. ✅ Sessie 1: Aan de slag (focus op setup en basis chat)
2. ✅ Sessie 2: RAG basis (sla evaluatie voorlopig over)
3. ✅ Sessie 3: Eenvoudige benchmarking (slechts 2 modellen)
4. ⏭️ Sla sessies 4-6 voorlopig over
5. 🔄 Keer terug naar sessies 4-6 na het bouwen van je eerste toepassing

### Voor gemiddelde ontwikkelaars (3 uur)
1. ⚡ Sessie 1: Snelle setupvalidatie
2. ✅ Sessie 2: Volledige RAG-pipeline met evaluatie
3. ✅ Sessie 3: Volledige benchmarkingsuite
4. ✅ Sessie 4: Modeloptimalisatie
5. ✅ Sessies 5-6: Focus op architectuurpatronen

### Voor gevorderde beoefenaars (2-3 uur)
1. ⚡ Sessies 1-3: Snelle review en validatie
2. ✅ Sessie 4: Diepgaande optimalisatie
3. ✅ Sessie 5: Multi-agent architectuur
4. ✅ Sessie 6: Productiepatronen en schaalbaarheid
5. 🚀 Uitbreiden: Bouw aangepaste routeringslogica en hybride implementaties

---

## Workshop Sessie Pack (Gerichte 30‑minuten Labs)

Als je het compacte 6-sessie workshopformaat volgt, gebruik dan deze specifieke gidsen (elk sluit aan bij en vult de bredere module-documentatie hierboven aan):

| Workshop Sessie | Gids | Kernfocus |
|-----------------|------|-----------|
| 1 | [Session01-GettingStartedFoundryLocal](./Session01-GettingStartedFoundryLocal.md) | Installeren, valideren, draaien phi & GPT-OSS-20B, versnelling |
| 2 | [Session02-BuildAISolutionsRAG](./Session02-BuildAISolutionsRAG.md) | Prompt engineering, RAG patronen, CSV & document grounding, migratie |
| 3 | [Session03-OpenSourceModels](./Session03-OpenSourceModels.md) | Hugging Face integratie, benchmarking, modelselectie |
| 4 | [Session04-CuttingEdgeModels](./Session04-CuttingEdgeModels.md) | SLM vs LLM, WebGPU, Chainlit RAG, ONNX versnelling |
| 5 | [Session05-AIPoweredAgents](./Session05-AIPoweredAgents.md) | Agentrollen, geheugen, tools, orkestratie |
| 6 | [Session06-ModelsAsTools](./Session06-ModelsAsTools.md) | Routing, chaining, schaalbaarheid naar Azure |

Elke sessiebestand bevat: samenvatting, leerdoelen, 30-minuten demo flow, startproject, validatiechecklist, probleemoplossing en verwijzingen naar de officiële Foundry Local Python SDK.

### Voorbeeldscripts

Installeer workshopafhankelijkheden (Windows):

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

Als je de Foundry Local-service uitvoert op een andere (Windows) machine of VM vanaf macOS, exporteer dan de endpoint:

```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```

| Sessie | Script(s) | Beschrijving |
|--------|-----------|--------------|
| 1 | `samples/session01/chat_bootstrap.py` | Bootstrap service & streaming chat |
| 2 | `samples/session02/rag_pipeline.py` | Minimale RAG (in-memory embeddings) |
|   | `samples/session02/rag_eval_ragas.py` | RAG-evaluatie met ragas-metrics |
| 3 | `samples/session03/benchmark_oss_models.py` | Multi-model latency & throughput benchmarking |
| 4 | `samples/session04/model_compare.py` | SLM vs LLM vergelijking (latency & voorbeeldoutput) |
| 5 | `samples/session05/agents_orchestrator.py` | Twee-agent onderzoek → redactionele pipeline |
| 6 | `samples/session06/models_router.py` | Intent-gebaseerde routing demo |
|   | `samples/session06/models_pipeline.py` | Multi-step plan/execute/refine chain |

### Omgevingsvariabelen (Algemeen voor alle voorbeelden)

| Variabele | Doel | Voorbeeld |
|-----------|------|----------|
| `FOUNDRY_LOCAL_ALIAS` | Standaard alias voor één model voor basisvoorbeelden | `phi-4-mini` |
| `SLM_ALIAS` / `LLM_ALIAS` | Expliciete SLM versus groter model voor vergelijking | `phi-4-mini` / `gpt-oss-20b` |
| `BENCH_MODELS` | Komma-lijst van aliassen om te benchmarken | `qwen2.5-0.5b,mistral-7b` |
| `BENCH_ROUNDS` | Benchmarkherhalingen per model | `3` |
| `BENCH_PROMPT` | Prompt gebruikt bij benchmarking | `Explain retrieval augmented generation briefly.` |
| `EMBED_MODEL` | Sentence-transformers embedding model | `sentence-transformers/all-MiniLM-L6-v2` |
| `RAG_QUESTION` | Overschrijf testquery voor RAG-pipeline | `Why use RAG with local inference?` |
| `AGENT_QUESTION` | Overschrijf agents-pipeline query | `Explain why edge AI matters for compliance.` |
| `AGENT_MODEL_PRIMARY` | Modelalias voor onderzoeksagent | `phi-4-mini` |
| `AGENT_MODEL_EDITOR` | Modelalias voor redacteuragent (kan verschillen) | `gpt-oss-20b` |
| `SHOW_USAGE` | Wanneer `1`, print tokengebruik per voltooiing | `1` |
| `RETRY_ON_FAIL` | Wanneer `1`, probeer opnieuw bij tijdelijke chatfouten | `1` |
| `RETRY_BACKOFF` | Seconden wachten voor opnieuw proberen | `1.0` |

Als een variabele niet is ingesteld, vallen scripts terug op verstandige standaardwaarden. Voor demo's met één model heb je meestal alleen `FOUNDRY_LOCAL_ALIAS` nodig.

### Hulpmodule

Alle voorbeelden delen nu een helper `samples/workshop_utils.py` die biedt:

* Cached `FoundryLocalManager` + OpenAI client creatie
* `chat_once()` helper met optionele retry + gebruiksrapportage
* Eenvoudige tokengebruikrapportage (inschakelen via `SHOW_USAGE=1`)

Dit vermindert duplicatie en benadrukt best practices voor efficiënte lokale modelorkestratie.

## Optionele Verbeteringen (Cross-Session)

| Thema | Verbetering | Sessies | Env / Toggle |
|-------|-------------|---------|--------------|
| Determinisme | Vaste temperatuur + stabiele promptsets | 1–6 | Stel in `temperature=0`, `top_p=1` |
| Zichtbaarheid Tokengebruik | Consistente kosten/efficiëntieonderwijs | 1–6 | `SHOW_USAGE=1` |
| Streaming Eerste Token | Waargenomen latencymetriek | 1,3,4,6 | `BENCH_STREAM=1` (benchmark) |
| Retry Veerkracht | Handelt tijdelijke cold-start | Alle | `RETRY_ON_FAIL=1` + `RETRY_BACKOFF` |
| Multi-Model Agents | Heterogene rolverdeling | 5 | `AGENT_MODEL_PRIMARY`, `AGENT_MODEL_EDITOR` |
| Adaptieve Routing | Intent + kostenheuristieken | 6 | Breid router uit met escalatielogica |
| Vectorgeheugen | Langetermijn semantische herinnering | 2,5,6 | Integreer FAISS/Chroma embedding index |
| Trace Export | Auditing & evaluatie | 2,5,6 | Voeg JSON-regels per stap toe |
| Kwaliteitsrubrieken | Kwalitatieve tracking | 3–6 | Secundaire scoring prompts |
| Smoke Tests | Snelle pre-workshop validatie | Alle | `python Workshop/tests/smoke.py` |

### Deterministische Snelle Start

```powershell
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
python Workshop\tests\smoke.py
```

Verwacht stabiele tokenaantallen bij herhaalde identieke invoer.

### RAG Evaluatie (Sessie 2)

Gebruik `rag_eval_ragas.py` om antwoordrelevantie, betrouwbaarheid en contextprecisie te berekenen op een kleine synthetische dataset:

```powershell
cd Workshop/samples
python -m session02.rag_eval_ragas
```

Breid uit door een grotere JSONL van vragen, contexten en grondwaarheden te leveren en deze vervolgens om te zetten naar een Hugging Face `Dataset`.

## CLI Command Nauwkeurigheidsbijlage

De workshop gebruikt bewust alleen momenteel gedocumenteerde / stabiele Foundry Local CLI-commando's.

### Stabiele Referentiecommando's

| Categorie | Commando | Doel |
|-----------|----------|------|
| Kern | `foundry --version` | Toon geïnstalleerde versie |
| Service | `foundry service start` | Start lokale service (indien niet automatisch) |
| Service | `foundry service status` | Toon servicestatus |
| Modellen | `foundry model list` | Lijst catalogus / beschikbare modellen |
| Modellen | `foundry model download <alias>` | Download modelgewichten naar cache |
| Modellen | `foundry model run <alias>` | Start (laad) een model lokaal; combineer met `--prompt` voor eenmalige uitvoering |
| Modellen | `foundry model unload <alias>` / `foundry model stop <alias>` | Laad een model uit het geheugen (indien ondersteund) |
| Cache | `foundry cache list` | Lijst gecachte (gedownloade) modellen |

### Eenmalige Promptpatroon

In plaats van een verouderde `model chat` subcommando, gebruik:

```powershell
foundry model run <alias> --prompt "Your question here"
```

Dit voert een enkele prompt/response-cyclus uit en sluit vervolgens af.

### Verwijderde / Vermeden Patronen

| Verouderd / Ongedocumenteerd | Vervanging / Richtlijnen |
|-----------------------------|--------------------------|
| `foundry model chat <model> "..."` | `foundry model run <model> --prompt "..."` |
| `foundry model list --running` | Gebruik gewone `foundry model list` + recente activiteit / logs |
| `foundry model list --cached` | `foundry cache list` |
| `foundry model stats <model>` | Gebruik benchmark Python-script + OS-tools (Taakbeheer / `nvidia-smi`) |
| `foundry model benchmark ...` | `samples/session03/benchmark_oss_models.py` |

### Benchmarking & Telemetrie

- Latency, p95, tokens/sec: `samples/session03/benchmark_oss_models.py`
- Eerste-token latency (streaming): stel `BENCH_STREAM=1` in
- Resourcegebruik: OS-monitoren (Taakbeheer, Activiteitenmonitor, `nvidia-smi`).

Zodra nieuwe CLI-telemetriecommando's upstream stabiliseren, kunnen ze met minimale aanpassingen worden opgenomen in sessiemarkdowns.

### Geautomatiseerde Lint Guard

Een geautomatiseerde linter voorkomt herintroductie van verouderde CLI-patronen binnen afgebakende codeblokken van markdown-bestanden:

Script: `Workshop/scripts/lint_markdown_cli.py`

Verouderde patronen worden geblokkeerd binnen code fences.

Aanbevolen vervangingen:
| Verouderd | Vervanging |
|-----------|-----------|
| `foundry model chat <a> "..."` | `foundry model run <a> --prompt "..."` |
| `model list --running` | `model list` |
| `model list --cached` | `cache list` |
| `model stats` | Benchmark script + systeemtools |
| `model benchmark` | `samples/session03/benchmark_oss_models.py` |
| `model list --available` | `model list` |

Run lokaal:
```powershell
python Workshop\scripts\lint_markdown_cli.py --verbose
```

GitHub Action: `.github/workflows/markdown-cli-lint.yml` draait bij elke push & PR.

Optionele pre-commit hook:
```bash
echo "python Workshop/scripts/lint_markdown_cli.py" > .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```

## Snelle CLI → SDK Migratietabel

| Taak | CLI One-Liner | SDK (Python) Equivalent | Opmerkingen |
|------|---------------|-------------------------|-------------|
| Voer een model eenmalig uit (prompt) | `foundry model run phi-4-mini --prompt "Hello"` | `manager=FoundryLocalManager("phi-4-mini"); client=OpenAI(base_url=manager.endpoint, api_key=manager.api_key or "not-needed"); client.chat.completions.create(model=manager.get_model_info("phi-4-mini").id, messages=[{"role":"user","content":"Hello"}])` | SDK bootstrapt service & caching automatisch |
| Download (cache) model | `foundry model download qwen2.5-0.5b` | `FoundryLocalManager("qwen2.5-0.5b")  # triggers download/load` | Manager kiest beste variant als alias naar meerdere builds verwijst |
| Lijst catalogus | `foundry model list` | `# gebruik manager voor elke alias of onderhoud bekende lijst` | CLI aggregeert; SDK momenteel per-alias initialisatie |
| Lijst gecachte modellen | `foundry cache list` | `manager.list_cached_models()` | Na manager-initialisatie (elke alias) |
| Verkrijg endpoint URL | (impliciet) | `manager.endpoint` | Gebruikt om OpenAI-compatibele client te maken |
| Warm een model op | `foundry model run <alias>` dan eerste prompt | `chat_once(alias, messages=[...])` (utility) | Utilities behandelen initiële cold latency warmup |
| Meet latency | `python -m session03.benchmark_oss_models` | `import benchmark_oss_models` (of nieuwe exportscript) | Geef voorkeur aan script voor consistente metrics |
| Stop / laad model uit | `foundry model unload <alias>` | (Niet blootgesteld – herstart service / proces) | Meestal niet nodig voor workshopflow |
| Verkrijg tokengebruik | (bekijk output) | `resp.usage.total_tokens` | Geboden als backend gebruiksobject retourneert |

## Benchmark Markdown Export

Gebruik het script `Workshop/scripts/export_benchmark_markdown.py` om een nieuwe benchmark uit te voeren (zelfde logica als `samples/session03/benchmark_oss_models.py`) en een GitHub-vriendelijke Markdown-tabel plus ruwe JSON te genereren.

### Voorbeeld

```powershell
python Workshop\scripts\export_benchmark_markdown.py --models "qwen2.5-0.5b,mistral-7b" --prompt "Explain retrieval augmented generation briefly." --rounds 3 --output benchmark_report.md
```

Gegenereerde bestanden:
| Bestand | Inhoud |
|---------|--------|
| `benchmark_report.md` | Markdown-tabel + interpretatiehints |
| `benchmark_report.json` | Ruwe metrics-array (voor diffing / trend tracking) |

Stel `BENCH_STREAM=1` in de omgeving in om eerste-token latency op te nemen indien ondersteund.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
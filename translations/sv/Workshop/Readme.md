# EdgeAI för Nybörjare - Workshop

> **Praktisk inlärningsväg för att bygga produktionsklara Edge AI-applikationer**
>
> Bemästra lokal AI-distribution med Microsoft Foundry Local, från första chattkomplettering till multi-agent orkestrering i 6 progressiva sessioner.

---

## 🎯 Introduktion

Välkommen till **EdgeAI för Nybörjare Workshop** - din praktiska guide till att bygga intelligenta applikationer som körs helt på lokal hårdvara. Denna workshop omvandlar teoretiska Edge AI-koncept till verkliga färdigheter genom stegvis utmanande övningar med Microsoft Foundry Local och Small Language Models (SLMs).

### Varför denna workshop?

**Edge AI-revolutionen är här**

Organisationer världen över skiftar från molnbaserad AI till edge computing av tre viktiga skäl:

1. **Integritet & Efterlevnad** - Bearbeta känslig data lokalt utan att skicka till molnet (HIPAA, GDPR, finansiella regler)
2. **Prestanda** - Eliminera nätverksfördröjning (50-500ms lokalt jämfört med 500-2000ms molnresor)
3. **Kostnadskontroll** - Ta bort kostnader per token för API och skala utan molnutgifter

**Men Edge AI är annorlunda**

Att köra AI lokalt kräver nya färdigheter:
- Modellval och optimering för resursbegränsningar
- Lokal tjänstehantering och hårdvaruacceleration
- Promptdesign för mindre modeller
- Produktionsdistributionsmönster för edge-enheter

**Denna workshop ger dig dessa färdigheter**

På 6 fokuserade sessioner (~3 timmar totalt) går du från "Hello World" till att distribuera produktionsklara multi-agent system - allt körs lokalt på din dator.

---

## 📚 Inlärningsmål

Genom att slutföra denna workshop kommer du att kunna:

### Kärnkompetenser
1. **Distribuera och hantera lokala AI-tjänster**
   - Installera och konfigurera Microsoft Foundry Local
   - Välja lämpliga modeller för edge-distribution
   - Hantera modellens livscykel (nedladdning, laddning, cache)
   - Övervaka resursanvändning och optimera prestanda

2. **Bygga AI-drivna applikationer**
   - Implementera OpenAI-kompatibla chattkompletteringar lokalt
   - Designa effektiva prompts för Small Language Models
   - Hantera strömmande svar för bättre användarupplevelse
   - Integrera lokala modeller i befintliga applikationer

3. **Skapa RAG-system (Retrieval Augmented Generation)**
   - Bygga semantisk sökning med embeddings
   - Grunda LLM-svar i domänspecifik kunskap
   - Utvärdera RAG-kvalitet med branschstandardmått
   - Skala från prototyp till produktion

4. **Optimera modellprestanda**
   - Benchmarka flera modeller för ditt användningsområde
   - Mäta latens, genomströmning och tid för första token
   - Välja optimala modeller baserat på hastighet/kvalitet
   - Jämföra SLM vs LLM avvägningar i verkliga scenarier

5. **Orkestrera multi-agent system**
   - Designa specialiserade agenter för olika uppgifter
   - Implementera agentminne och kontexthantering
   - Koordinera agenter i komplexa arbetsflöden
   - Styra förfrågningar intelligent över flera modeller

6. **Distribuera produktionsklara lösningar**
   - Implementera felhantering och återförsökslogik
   - Övervaka tokenanvändning och systemresurser
   - Bygga skalbara arkitekturer med modell-som-verktyg-mönster
   - Planera migrationsvägar från edge till hybrid (edge + moln)

---

## 🎓 Inlärningsresultat

### Vad du kommer att bygga

Vid slutet av denna workshop kommer du ha skapat:

| Session | Leverans | Demonstrerade färdigheter |
|---------|----------|---------------------------|
| **1** | Chattapplikation med strömning | Tjänsteinstallation, grundläggande kompletteringar, strömmande UX |
| **2** | RAG-system med utvärdering | Embeddings, semantisk sökning, kvalitetsmått |
| **3** | Multi-modell benchmarksvit | Prestandamätning, modelljämförelse |
| **4** | SLM vs LLM jämförelse | Avvägningsanalys, optimeringsstrategier |
| **5** | Multi-agent orkestrator | Agentdesign, minneshantering, koordinering |
| **6** | Intelligent routningssystem | Intentdetektion, modellval, skalbarhet |

### Kompetensmatris

| Färdighetsnivå | Session 1-2 | Session 3-4 | Session 5-6 |
|----------------|-------------|-------------|-------------|
| **Nybörjare** | ✅ Installation & grunder | ⚠️ Utmanande | ❌ För avancerat |
| **Mellanliggande** | ✅ Snabb översikt | ✅ Kärninlärning | ⚠️ Utmanande mål |
| **Avancerad** | ✅ Enkel genomgång | ✅ Förfining | ✅ Produktionsmönster |

### Karriärklara färdigheter

**Efter denna workshop kommer du vara redo att:**

✅ **Bygga integritetsfokuserade applikationer**
- Hälsoappar som hanterar PHI/PII lokalt
- Finansiella tjänster med efterlevnadskrav
- Statliga system med datasuveränitetsbehov

✅ **Optimera för edge-miljöer**
- IoT-enheter med begränsade resurser
- Offline-först mobilapplikationer
- Låg-latens realtidssystem

✅ **Designa intelligenta arkitekturer**
- Multi-agent system för komplexa arbetsflöden
- Hybrid edge-moln distributioner
- Kostnadsoptimerad AI-infrastruktur

✅ **Leda Edge AI-initiativ**
- Utvärdera Edge AI:s genomförbarhet för projekt
- Välja lämpliga modeller och ramverk
- Arkitektera skalbara lokala AI-lösningar

---

## 🗺️ Workshopstruktur

### Sessionöversikt (6 sessioner × 30 minuter = 3 timmar)

| Session | Ämne | Fokus | Varaktighet |
|---------|-------|-------|-------------|
| **1** | Kom igång med Foundry Local | Installera, validera, första kompletteringar | 30 min |
| **2** | Bygga AI-lösningar med RAG | Promptdesign, embeddings, utvärdering | 30 min |
| **3** | Öppna källkod-modeller | Modellupptäckt, benchmarking, val | 30 min |
| **4** | Avancerade modeller | SLM vs LLM, optimering, ramverk | 30 min |
| **5** | AI-drivna agenter | Agentdesign, orkestrering, minne | 30 min |
| **6** | Modeller som verktyg | Routing, kedjning, skalningsstrategier | 30 min |

---

## 🚀 Snabbstart

### Förutsättningar

**Systemkrav:**
- **OS**: Windows 10/11, macOS 11+ eller Linux (Ubuntu 20.04+)
- **RAM**: Minst 8GB, rekommenderat 16GB+
- **Lagring**: Minst 10GB ledigt utrymme för modeller
- **CPU**: Modern processor med AVX2-stöd
- **GPU** (valfritt): CUDA-kompatibel eller Qualcomm NPU för acceleration

**Programvarukrav:**
- **Python 3.8+** ([Ladda ner](https://www.python.org/downloads/))
- **Microsoft Foundry Local** ([Installationsguide](../../../Workshop))
- **Git** ([Ladda ner](https://git-scm.com/downloads))
- **Visual Studio Code** (rekommenderas) ([Ladda ner](https://code.visualstudio.com/))

### Installation i 3 steg

#### 1. Installera Foundry Local

**Windows:**
```powershell
winget install Microsoft.FoundryLocal
```

**macOS:**
```bash
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**Verifiera installationen:**
```bash
foundry --version
foundry service status
```

**Se till att Azure AI Foundry Local körs med en fast port**

```bash
# Set FoundryLocal to use port 58123 (default)
foundry service set --port 58123 --show

# Or use a different port
foundry service set --port 58000 --show
```

**Verifiera att det fungerar:**
```bash
# Check service status
foundry service status

# Test the endpoint
curl http://127.0.0.1:58123/v1/models
```
**Hitta tillgängliga modeller**
För att se vilka modeller som är tillgängliga i din Foundry Local-instans kan du fråga modellens slutpunkt:

```bash
# cmd/bash/powershell
foundry model list
```

Använd webbslutpunkt 

```bash
# Windows PowerShell
powershell -Command "Invoke-RestMethod -Uri 'http://127.0.0.1:58123/v1/models' -Method Get"

# Or using curl (if available)
curl http://127.0.0.1:58123/v1/models
```

#### 2. Klona repository & installera beroenden

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

#### 3. Kör ditt första exempel

```bash
# Start Foundry Local and load a model
foundry model run phi-4-mini

# Run the chat bootstrap sample
cd samples
python -m session01.chat_bootstrap "What is edge AI?"
```

**✅ Framgång!** Du bör se ett strömmande svar om edge AI.

---

## 📦 Workshopresurser

### Python-exempel

Progressiva praktiska exempel som demonstrerar varje koncept:

| Session | Exempel | Beskrivning | Körtid |
|---------|---------|-------------|--------|
| 1 | [`chat_bootstrap.py`](../../../Workshop/samples/session01/chat_bootstrap.py) | Grundläggande & strömmande chatt | ~30s |
| 2 | [`rag_pipeline.py`](../../../Workshop/samples/session02/rag_pipeline.py) | RAG med embeddings | ~45s |
| 2 | [`rag_eval_ragas.py`](../../../Workshop/samples/session02/rag_eval_ragas.py) | Utvärdering av RAG-kvalitet | ~60s |
| 3 | [`benchmark_oss_models.py`](../../../Workshop/samples/session03/benchmark_oss_models.py) | Multi-modell benchmarking | ~2-3m |
| 4 | [`model_compare.py`](../../../Workshop/samples/session04/model_compare.py) | SLM vs LLM jämförelse | ~45s |
| 5 | [`agents_orchestrator.py`](../../../Workshop/samples/session05/agents_orchestrator.py) | Multi-agent system | ~60s |
| 6 | [`models_router.py`](../../../Workshop/samples/session06/models_router.py) | Intentbaserad routing | ~45s |
| 6 | [`models_pipeline.py`](../../../Workshop/samples/session06/models_pipeline.py) | Multi-steg pipeline | ~60s |

### Jupyter Notebooks

Interaktiv utforskning med förklaringar och visualiseringar:

| Session | Notebook | Beskrivning | Svårighetsgrad |
|---------|----------|-------------|----------------|
| 1 | [`session01_chat_bootstrap.ipynb`](./notebooks/session01_chat_bootstrap.ipynb) | Chattgrunder & strömning | ⭐ Nybörjare |
| 2 | [`session02_rag_pipeline.ipynb`](./notebooks/session02_rag_pipeline.ipynb) | Bygg RAG-system | ⭐⭐ Mellanliggande |
| 2 | [`session02_rag_eval_ragas.ipynb`](./notebooks/session02_rag_eval_ragas.ipynb) | Utvärdera RAG-kvalitet | ⭐⭐ Mellanliggande |
| 3 | [`session03_benchmark_oss_models.ipynb`](./notebooks/session03_benchmark_oss_models.ipynb) | Modellbenchmarking | ⭐⭐ Mellanliggande |
| 4 | [`session04_model_compare.ipynb`](./notebooks/session04_model_compare.ipynb) | Modelljämförelse | ⭐⭐ Mellanliggande |
| 5 | [`session05_agents_orchestrator.ipynb`](./notebooks/session05_agents_orchestrator.ipynb) | Agentorkestrering | ⭐⭐⭐ Avancerad |
| 6 | [`session06_models_router.ipynb`](./notebooks/session06_models_router.ipynb) | Intent-routing | ⭐⭐⭐ Avancerad |
| 6 | [`session06_models_pipeline.ipynb`](./notebooks/session06_models_pipeline.ipynb) | Pipeline-orkestrering | ⭐⭐⭐ Avancerad |

### Dokumentation

Omfattande guider och referenser:

| Dokument | Beskrivning | Använd när |
|----------|-------------|------------|
| [QUICK_START.md](./QUICK_START.md) | Snabbstartsguide | Börjar från början |
| [QUICK_REFERENCE.md](./QUICK_REFERENCE.md) | Kommando- & API-snabbguide | Behöver snabba svar |
| [FOUNDRY_SDK_QUICKREF.md](./FOUNDRY_SDK_QUICKREF.md) | SDK-mönster & exempel | Skriver kod |
| [ENV_CONFIGURATION.md](./ENV_CONFIGURATION.md) | Guide för miljövariabler | Konfigurerar exempel |
| [notebooks/TROUBLESHOOTING.md](./notebooks/TROUBLESHOOTING.md) | Vanliga problem & lösningar | Felsöker problem |

---

## 🎓 Rekommendationer för inlärningsväg

### För nybörjare (3-4 timmar)
1. ✅ Session 1: Kom igång (fokus på installation och grundläggande chatt)
2. ✅ Session 2: RAG-grunder (hoppa över utvärdering initialt)
3. ✅ Session 3: Enkel benchmarking (endast 2 modeller)
4. ⏭️ Hoppa över sessionerna 4-6 för tillfället
5. 🔄 Återvänd till sessionerna 4-6 efter att ha byggt första applikationen

### För mellanliggande utvecklare (3 timmar)
1. ⚡ Session 1: Snabb installationsvalidering
2. ✅ Session 2: Komplett RAG-pipeline med utvärdering
3. ✅ Session 3: Fullständig benchmarksvit
4. ✅ Session 4: Modelloptimering
5. ✅ Sessionerna 5-6: Fokus på arkitekturmönster

### För avancerade utövare (2-3 timmar)
1. ⚡ Sessionerna 1-3: Snabb översikt och validering
2. ✅ Session 4: Djupdykning i optimering
3. ✅ Session 5: Multi-agent arkitektur
4. ✅ Session 6: Produktionsmönster och skalning
5. 🚀 Utöka: Bygg anpassad routningslogik och hybriddistributioner

---

## Workshop Session Pack (Fokuserade 30-minuters labbar)

Om du följer det komprimerade 6-sessioners workshopformatet, använd dessa dedikerade guider (varje guide kompletterar de bredare modulguiderna ovan):

| Workshop Session | Guide | Kärnfokus |
|------------------|-------|-----------|
| 1 | [Session01-GettingStartedFoundryLocal](./Session01-GettingStartedFoundryLocal.md) | Installera, validera, kör phi & GPT-OSS-20B, acceleration |
| 2 | [Session02-BuildAISolutionsRAG](./Session02-BuildAISolutionsRAG.md) | Promptdesign, RAG-mönster, CSV & dokumentgrundning, migration |
| 3 | [Session03-OpenSourceModels](./Session03-OpenSourceModels.md) | Hugging Face-integration, benchmarking, modellval |
| 4 | [Session04-CuttingEdgeModels](./Session04-CuttingEdgeModels.md) | SLM vs LLM, WebGPU, Chainlit RAG, ONNX-acceleration |
| 5 | [Session05-AIPoweredAgents](./Session05-AIPoweredAgents.md) | Agentroller, minne, verktyg, orkestrering |
| 6 | [Session06-ModelsAsTools](./Session06-ModelsAsTools.md) | Routing, kedjning, skalning till Azure |

Varje sessionsfil innehåller: sammanfattning, lärandemål, 30-minuters demo-flöde, startprojekt, valideringschecklista, felsökning och hänvisningar till den officiella Foundry Local Python SDK.

### Exempelskript

Installera workshopberoenden (Windows):

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

Om Foundry Local-tjänsten körs på en annan (Windows) dator eller VM från macOS, exportera endpointen:

```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```

| Session | Skript | Beskrivning |
|---------|--------|-------------|
| 1 | `samples/session01/chat_bootstrap.py` | Starta tjänst & strömmande chatt |
| 2 | `samples/session02/rag_pipeline.py` | Minimal RAG (in-memory embeddings) |
|   | `samples/session02/rag_eval_ragas.py` | RAG-utvärdering med ragas-mått |
| 3 | `samples/session03/benchmark_oss_models.py` | Latens- och genomströmningsbenchmarking för flera modeller |
| 4 | `samples/session04/model_compare.py` | Jämförelse mellan SLM och LLM (latens & exempelutdata) |
| 5 | `samples/session05/agents_orchestrator.py` | Två-agenters forsknings- och redigeringspipeline |
| 6 | `samples/session06/models_router.py` | Intent-baserad routingdemo |
|   | `samples/session06/models_pipeline.py` | Flerstegs planera/utföra/förfina-kedja |

### Miljövariabler (Gemensamma för alla exempel)

| Variabel | Syfte | Exempel |
|----------|-------|---------|
| `FOUNDRY_LOCAL_ALIAS` | Standardalias för enskild modell för grundläggande exempel | `phi-4-mini` |
| `SLM_ALIAS` / `LLM_ALIAS` | Explicit SLM kontra större modell för jämförelse | `phi-4-mini` / `gpt-oss-20b` |
| `BENCH_MODELS` | Kommalista med alias att benchmarka | `qwen2.5-0.5b,mistral-7b` |
| `BENCH_ROUNDS` | Antal benchmarkupprepningar per modell | `3` |
| `BENCH_PROMPT` | Prompt som används vid benchmarking | `Explain retrieval augmented generation briefly.` |
| `EMBED_MODEL` | Sentence-transformers embedding-modell | `sentence-transformers/all-MiniLM-L6-v2` |
| `RAG_QUESTION` | Åsidosätt testfråga för RAG-pipeline | `Why use RAG with local inference?` |
| `AGENT_QUESTION` | Åsidosätt fråga för agentpipeline | `Explain why edge AI matters for compliance.` |
| `AGENT_MODEL_PRIMARY` | Modellalias för forskningsagent | `phi-4-mini` |
| `AGENT_MODEL_EDITOR` | Modellalias för redigeringsagent (kan skilja sig) | `gpt-oss-20b` |
| `SHOW_USAGE` | När `1`, skriver ut tokenanvändning per completion | `1` |
| `RETRY_ON_FAIL` | När `1`, försök igen vid tillfälliga chattfel | `1` |
| `RETRY_BACKOFF` | Sekunder att vänta innan nytt försök | `1.0` |

Om en variabel inte är inställd, faller skripten tillbaka på rimliga standardvärden. För demos med en enda modell behöver du vanligtvis bara `FOUNDRY_LOCAL_ALIAS`.

### Hjälpmodul

Alla exempel delar nu en hjälpfunktion `samples/workshop_utils.py` som erbjuder:

* Cachad `FoundryLocalManager` + OpenAI-klientskapande
* `chat_once()`-hjälpare med valfri retry + användningsrapportering
* Enkel rapportering av tokenanvändning (aktivera via `SHOW_USAGE=1`)

Detta minskar duplicering och lyfter fram bästa praxis för effektiv lokal modellorkestrering.

## Valfria förbättringar (Sessionsöverskridande)

| Tema | Förbättring | Sessioner | Miljö / Växla |
|------|-------------|-----------|---------------|
| Determinism | Fast temperatur + stabila promptuppsättningar | 1–6 | Ställ in `temperature=0`, `top_p=1` |
| Synlighet av tokenanvändning | Konsekvent kostnads-/effektivitetsundervisning | 1–6 | `SHOW_USAGE=1` |
| Första token i strömning | Upplevd latensmätning | 1,3,4,6 | `BENCH_STREAM=1` (benchmark) |
| Återhämtningsförmåga vid fel | Hanterar tillfälliga kallstartsfel | Alla | `RETRY_ON_FAIL=1` + `RETRY_BACKOFF` |
| Multi-modellagenter | Heterogen rollspecialisering | 5 | `AGENT_MODEL_PRIMARY`, `AGENT_MODEL_EDITOR` |
| Adaptiv routing | Intent + kostnadsheuristik | 6 | Utöka router med eskaleringslogik |
| Vektorminne | Långsiktig semantisk återkallelse | 2,5,6 | Integrera FAISS/Chroma embedding index |
| Spårningsexport | Revision & utvärdering | 2,5,6 | Lägg till JSON-linjer per steg |
| Kvalitetsrubriker | Kvalitativ spårning | 3–6 | Sekundära bedömningsprompter |
| Röktester | Snabb validering före workshop | Alla | `python Workshop/tests/smoke.py` |

### Deterministisk snabbstart

```powershell
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
python Workshop\tests\smoke.py
```

Förvänta dig stabila tokenantal över upprepade identiska inmatningar.

### RAG-utvärdering (Session 2)

Använd `rag_eval_ragas.py` för att beräkna svarens relevans, tillförlitlighet och kontextprecision på en liten syntetisk dataset:

```powershell
cd Workshop/samples
python -m session02.rag_eval_ragas
```

Utöka genom att tillhandahålla en större JSONL med frågor, kontexter och sanna värden, och konvertera sedan till en Hugging Face `Dataset`.

## Bilaga om CLI-kommandon och noggrannhet

Workshopen använder medvetet endast för närvarande dokumenterade/stabila Foundry Local CLI-kommandon.

### Refererade stabila kommandon

| Kategori | Kommando | Syfte |
|----------|----------|-------|
| Kärna | `foundry --version` | Visa installerad version |
| Tjänst | `foundry service start` | Starta lokal tjänst (om inte automatiskt) |
| Tjänst | `foundry service status` | Visa tjänstens status |
| Modeller | `foundry model list` | Lista katalog / tillgängliga modeller |
| Modeller | `foundry model download <alias>` | Ladda ner modellvikter till cache |
| Modeller | `foundry model run <alias>` | Starta (ladda) en modell lokalt; kombinera med `--prompt` för enstaka körning |
| Modeller | `foundry model unload <alias>` / `foundry model stop <alias>` | Ladda ur en modell från minnet (om stöd finns) |
| Cache | `foundry cache list` | Lista cachade (nedladdade) modeller |

### Enstaka promptmönster

Istället för ett föråldrat `model chat`-underkommando, använd:

```powershell
foundry model run <alias> --prompt "Your question here"
```

Detta utför en enstaka prompt/svar-cykel och avslutar sedan.

### Borttagna / undvikna mönster

| Föråldrade / Odokumenterade | Ersättning / Riktlinjer |
|-----------------------------|-------------------------|
| `foundry model chat <model> "..."` | `foundry model run <model> --prompt "..."` |
| `foundry model list --running` | Använd vanlig `foundry model list` + senaste aktivitet / loggar |
| `foundry model list --cached` | `foundry cache list` |
| `foundry model stats <model>` | Använd benchmark Python-skript + OS-verktyg (Task Manager / `nvidia-smi`) |
| `foundry model benchmark ...` | `samples/session03/benchmark_oss_models.py` |

### Benchmarking & Telemetri

- Latens, p95, tokens/sek: `samples/session03/benchmark_oss_models.py`
- Första token-latens (strömning): ställ in `BENCH_STREAM=1`
- Resursanvändning: OS-övervakning (Task Manager, Activity Monitor, `nvidia-smi`).

När nya CLI-telemetrikommandon stabiliseras uppströms kan de integreras med minimala ändringar i sessionsmarkeringar.

### Automatiserad linter

En automatiserad linter förhindrar återintroduktion av föråldrade CLI-mönster inom kodblock i markdown-filer:

Skript: `Workshop/scripts/lint_markdown_cli.py`

Föråldrade mönster blockeras inom kodblock.

Rekommenderade ersättningar:
| Föråldrade | Ersättning |
|------------|-----------|
| `foundry model chat <a> "..."` | `foundry model run <a> --prompt "..."` |
| `model list --running` | `model list` |
| `model list --cached` | `cache list` |
| `model stats` | Benchmark-skript + systemverktyg |
| `model benchmark` | `samples/session03/benchmark_oss_models.py` |
| `model list --available` | `model list` |

Kör lokalt:
```powershell
python Workshop\scripts\lint_markdown_cli.py --verbose
```

GitHub Action: `.github/workflows/markdown-cli-lint.yml` körs vid varje push & PR.

Valfri pre-commit hook:
```bash
echo "python Workshop/scripts/lint_markdown_cli.py" > .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```

## Snabb CLI → SDK-migrationstabell

| Uppgift | CLI One-Liner | SDK (Python) Motsvarighet | Noteringar |
|---------|---------------|--------------------------|------------|
| Kör en modell en gång (prompt) | `foundry model run phi-4-mini --prompt "Hello"` | `manager=FoundryLocalManager("phi-4-mini"); client=OpenAI(base_url=manager.endpoint, api_key=manager.api_key or "not-needed"); client.chat.completions.create(model=manager.get_model_info("phi-4-mini").id, messages=[{"role":"user","content":"Hello"}])` | SDK startar tjänst & caching automatiskt |
| Ladda ner (cache) modell | `foundry model download qwen2.5-0.5b` | `FoundryLocalManager("qwen2.5-0.5b")  # triggers download/load` | Manager väljer bästa variant om aliaset mappar till flera byggnader |
| Lista katalog | `foundry model list` | `# använd manager för varje alias eller behåll känd lista` | CLI aggregerar; SDK för närvarande per-alias initiering |
| Lista cachade modeller | `foundry cache list` | `manager.list_cached_models()` | Efter manager-initiering (valfritt alias) |
| Hämta endpoint-URL | (implicit) | `manager.endpoint` | Används för att skapa OpenAI-kompatibel klient |
| Värma upp en modell | `foundry model run <alias>` följt av första prompt | `chat_once(alias, messages=[...])` (hjälpfunktion) | Hjälpfunktioner hanterar initial kallstartslatens |
| Mäta latens | `python -m session03.benchmark_oss_models` | `import benchmark_oss_models` (eller nytt exportskript) | Föredra skript för konsekventa mätvärden |
| Stoppa / ladda ur modell | `foundry model unload <alias>` | (Ej exponerat – starta om tjänst / process) | Vanligtvis inte nödvändigt för workshopflöde |
| Hämta tokenanvändning | (visa utdata) | `resp.usage.total_tokens` | Tillhandahålls om backend returnerar användningsobjekt |

## Benchmark Markdown Export

Använd skriptet `Workshop/scripts/export_benchmark_markdown.py` för att köra en ny benchmark (samma logik som `samples/session03/benchmark_oss_models.py`) och generera en GitHub-vänlig Markdown-tabell plus rå JSON.

### Exempel

```powershell
python Workshop\scripts\export_benchmark_markdown.py --models "qwen2.5-0.5b,mistral-7b" --prompt "Explain retrieval augmented generation briefly." --rounds 3 --output benchmark_report.md
```

Genererade filer:
| Fil | Innehåll |
|-----|----------|
| `benchmark_report.md` | Markdown-tabell + tolkningshintar |
| `benchmark_report.json` | Rå metrisk array (för jämförelse / trendspårning) |

Ställ in `BENCH_STREAM=1` i miljön för att inkludera första token-latens om det stöds.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, bör du vara medveten om att automatiserade översättningar kan innehålla fel eller felaktigheter. Det ursprungliga dokumentet på dess ursprungliga språk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
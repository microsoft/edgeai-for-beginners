<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "45923ada94573fee7c82cc4f0c3bb344",
  "translation_date": "2025-10-28T22:14:21+00:00",
  "source_file": "Workshop/Readme.md",
  "language_code": "no"
}
-->
# EdgeAI for Nybegynnere - Workshop

> **Praktisk læringssti for å bygge produksjonsklare Edge AI-applikasjoner**
>
> Mestre lokal AI-distribusjon med Microsoft Foundry Local, fra første chat-komplettering til multi-agent orkestrering i 6 progressive økter.

---

## 🎯 Introduksjon

Velkommen til **EdgeAI for Nybegynnere Workshop** - din praktiske, hands-on guide til å bygge intelligente applikasjoner som kjører helt på lokal maskinvare. Denne workshopen forvandler teoretiske Edge AI-konsepter til ferdigheter i den virkelige verden gjennom gradvis utfordrende øvelser ved bruk av Microsoft Foundry Local og Small Language Models (SLMs).

### Hvorfor denne workshopen?

**Edge AI-revolusjonen er her**

Organisasjoner over hele verden skifter fra skybasert AI til edge computing av tre viktige grunner:

1. **Personvern og samsvar** - Behandle sensitive data lokalt uten overføring til skyen (HIPAA, GDPR, finansielle reguleringer)
2. **Ytelse** - Fjern nettverksforsinkelser (50-500ms lokalt vs 500-2000ms sky-rundtur)
3. **Kostnadskontroll** - Fjern kostnader per token API og skaler uten skyutgifter

**Men Edge AI er annerledes**

Å kjøre AI lokalt krever nye ferdigheter:
- Modellvalg og optimalisering for ressursbegrensninger
- Lokal tjenestestyring og maskinvareakselerasjon
- Prompt engineering for mindre modeller
- Produksjonsdistribusjonsmønstre for edge-enheter

**Denne workshopen gir deg disse ferdighetene**

I 6 fokuserte økter (~3 timer totalt) vil du gå fra "Hello World" til å distribuere produksjonsklare multi-agent systemer - alt kjører lokalt på din maskin.

---

## 📚 Læringsmål

Ved å fullføre denne workshopen vil du kunne:

### Kjernekompetanser
1. **Distribuere og administrere lokale AI-tjenester**
   - Installere og konfigurere Microsoft Foundry Local
   - Velge passende modeller for edge-distribusjon
   - Administrere modellens livssyklus (nedlasting, lasting, caching)
   - Overvåke ressursbruk og optimalisere ytelse

2. **Bygge AI-drevne applikasjoner**
   - Implementere OpenAI-kompatible chat-kompletteringer lokalt
   - Designe effektive prompts for Small Language Models
   - Håndtere streaming-responser for bedre brukeropplevelse
   - Integrere lokale modeller i eksisterende applikasjoner

3. **Skape RAG (Retrieval Augmented Generation)-systemer**
   - Bygge semantisk søk med embeddings
   - Forankre LLM-responser i domenespesifikk kunnskap
   - Evaluere RAG-kvalitet med bransjestandarder
   - Skalere fra prototype til produksjon

4. **Optimalisere modellens ytelse**
   - Benchmarke flere modeller for ditt brukstilfelle
   - Måle forsinkelse, gjennomstrømning og tid til første token
   - Velge optimale modeller basert på hastighet/kvalitet-avveininger
   - Sammenligne SLM vs LLM-avveininger i virkelige scenarioer

5. **Orkestrere multi-agent systemer**
   - Designe spesialiserte agenter for ulike oppgaver
   - Implementere agentminne og kontekststyring
   - Koordinere agenter i komplekse arbeidsflyter
   - Rute forespørsler intelligent mellom flere modeller

6. **Distribuere produksjonsklare løsninger**
   - Implementere feilhåndtering og retry-logikk
   - Overvåke tokenbruk og systemressurser
   - Bygge skalerbare arkitekturer med modell-som-verktøy-mønstre
   - Planlegge migreringsveier fra edge til hybrid (edge + sky)

---

## 🎓 Læringsutbytte

### Hva du vil bygge

Ved slutten av denne workshopen vil du ha laget:

| Økt | Leveranse | Demonstrerte ferdigheter |
|-----|-----------|--------------------------|
| **1** | Chat-applikasjon med streaming | Tjenesteoppsett, grunnleggende kompletteringer, streaming UX |
| **2** | RAG-system med evaluering | Embeddings, semantisk søk, kvalitetsmålinger |
| **3** | Multi-modell benchmark-suite | Ytelsesmåling, modell-sammenligning |
| **4** | SLM vs LLM-komparator | Avveiningsanalyse, optimaliseringsstrategier |
| **5** | Multi-agent orkestrator | Agentdesign, minnehåndtering, koordinering |
| **6** | Intelligent rutingssystem | Intentsdeteksjon, modellvalg, skalerbarhet |

### Kompetansematrise

| Ferdighetsnivå | Økt 1-2 | Økt 3-4 | Økt 5-6 |
|----------------|---------|---------|---------|
| **Nybegynner** | ✅ Oppsett & grunnleggende | ⚠️ Utfordrende | ❌ For avansert |
| **Mellomnivå** | ✅ Rask gjennomgang | ✅ Kjerneopplæring | ⚠️ Utfordrende mål |
| **Avansert** | ✅ Enkelt | ✅ Finpussing | ✅ Produksjonsmønstre |

### Karriereklare ferdigheter

**Etter denne workshopen vil du være klar til å:**

✅ **Bygge personvern-fokuserte applikasjoner**
- Helseapplikasjoner som håndterer PHI/PII lokalt
- Finanstjenester med samsvarskrav
- Offentlige systemer med krav til datasuverenitet

✅ **Optimalisere for edge-miljøer**
- IoT-enheter med begrensede ressurser
- Offline-først mobilapplikasjoner
- Lav-latens sanntidssystemer

✅ **Designe intelligente arkitekturer**
- Multi-agent systemer for komplekse arbeidsflyter
- Hybrid edge-sky-distribusjoner
- Kostnadsoptimalisert AI-infrastruktur

✅ **Lede Edge AI-initiativer**
- Evaluere Edge AI-muligheter for prosjekter
- Velge passende modeller og rammeverk
- Arkitektere skalerbare lokale AI-løsninger

---

## 🗺️ Workshop-struktur

### Øktoversikt (6 økter × 30 minutter = 3 timer)

| Økt | Tema | Fokus | Varighet |
|-----|------|-------|----------|
| **1** | Kom i gang med Foundry Local | Installere, validere, første kompletteringer | 30 min |
| **2** | Bygge AI-løsninger med RAG | Prompt engineering, embeddings, evaluering | 30 min |
| **3** | Åpen kildekode-modeller | Modelloppdagelse, benchmarking, valg | 30 min |
| **4** | Avanserte modeller | SLM vs LLM, optimalisering, rammeverk | 30 min |
| **5** | AI-drevne agenter | Agentdesign, orkestrering, minne | 30 min |
| **6** | Modeller som verktøy | Ruting, kjeding, skaleringsstrategier | 30 min |

---

## 🚀 Rask start

### Forutsetninger

**Systemkrav:**
- **OS**: Windows 10/11, macOS 11+, eller Linux (Ubuntu 20.04+)
- **RAM**: Minimum 8GB, anbefalt 16GB+
- **Lagring**: 10GB+ ledig plass for modeller
- **CPU**: Moderne prosessor med AVX2-støtte
- **GPU** (valgfritt): CUDA-kompatibel eller Qualcomm NPU for akselerasjon

**Programvarekrav:**
- **Python 3.8+** ([Last ned](https://www.python.org/downloads/))
- **Microsoft Foundry Local** ([Installasjonsveiledning](../../../Workshop))
- **Git** ([Last ned](https://git-scm.com/downloads))
- **Visual Studio Code** (anbefalt) ([Last ned](https://code.visualstudio.com/))

### Oppsett i 3 steg

#### 1. Installer Foundry Local

**Windows:**
```powershell
winget install Microsoft.FoundryLocal
```

**macOS:**
```bash
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**Verifiser installasjon:**
```bash
foundry --version
foundry service status
```

**Sørg for at Azure AI Foundry Local kjører med en fast port**

```bash
# Set FoundryLocal to use port 58123 (default)
foundry service set --port 58123 --show

# Or use a different port
foundry service set --port 58000 --show
```

**Verifiser at det fungerer:**
```bash
# Check service status
foundry service status

# Test the endpoint
curl http://127.0.0.1:58123/v1/models
```
**Finn tilgjengelige modeller**
For å se hvilke modeller som er tilgjengelige i din Foundry Local-instans, kan du spørre modellendepunktet:

```bash
# cmd/bash/powershell
foundry model list
```

Ved bruk av web-endepunkt 

```bash
# Windows PowerShell
powershell -Command "Invoke-RestMethod -Uri 'http://127.0.0.1:58123/v1/models' -Method Get"

# Or using curl (if available)
curl http://127.0.0.1:58123/v1/models
```

#### 2. Klon repository og installer avhengigheter

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

#### 3. Kjør ditt første eksempel

```bash
# Start Foundry Local and load a model
foundry model run phi-4-mini

# Run the chat bootstrap sample
cd samples
python -m session01.chat_bootstrap "What is edge AI?"
```

**✅ Suksess!** Du bør se en streaming-respons om edge AI.

---

## 📦 Workshop-ressurser

### Python-eksempler

Praktiske eksempler som demonstrerer hvert konsept:

| Økt | Eksempel | Beskrivelse | Kjøretid |
|-----|----------|-------------|----------|
| 1 | [`chat_bootstrap.py`](../../../Workshop/samples/session01/chat_bootstrap.py) | Grunnleggende & streaming chat | ~30s |
| 2 | [`rag_pipeline.py`](../../../Workshop/samples/session02/rag_pipeline.py) | RAG med embeddings | ~45s |
| 2 | [`rag_eval_ragas.py`](../../../Workshop/samples/session02/rag_eval_ragas.py) | RAG-kvalitetsevaluering | ~60s |
| 3 | [`benchmark_oss_models.py`](../../../Workshop/samples/session03/benchmark_oss_models.py) | Multi-modell benchmarking | ~2-3m |
| 4 | [`model_compare.py`](../../../Workshop/samples/session04/model_compare.py) | SLM vs LLM-sammenligning | ~45s |
| 5 | [`agents_orchestrator.py`](../../../Workshop/samples/session05/agents_orchestrator.py) | Multi-agent system | ~60s |
| 6 | [`models_router.py`](../../../Workshop/samples/session06/models_router.py) | Intent-basert ruting | ~45s |
| 6 | [`models_pipeline.py`](../../../Workshop/samples/session06/models_pipeline.py) | Multi-trinns pipeline | ~60s |

### Jupyter Notebooks

Interaktiv utforskning med forklaringer og visualiseringer:

| Økt | Notebook | Beskrivelse | Vanskelighetsgrad |
|-----|----------|-------------|--------------------|
| 1 | [`session01_chat_bootstrap.ipynb`](./notebooks/session01_chat_bootstrap.ipynb) | Grunnleggende chat & streaming | ⭐ Nybegynner |
| 2 | [`session02_rag_pipeline.ipynb`](./notebooks/session02_rag_pipeline.ipynb) | Bygg RAG-system | ⭐⭐ Mellomnivå |
| 2 | [`session02_rag_eval_ragas.ipynb`](./notebooks/session02_rag_eval_ragas.ipynb) | Evaluer RAG-kvalitet | ⭐⭐ Mellomnivå |
| 3 | [`session03_benchmark_oss_models.ipynb`](./notebooks/session03_benchmark_oss_models.ipynb) | Modellbenchmarking | ⭐⭐ Mellomnivå |
| 4 | [`session04_model_compare.ipynb`](./notebooks/session04_model_compare.ipynb) | Modellsammenligning | ⭐⭐ Mellomnivå |
| 5 | [`session05_agents_orchestrator.ipynb`](./notebooks/session05_agents_orchestrator.ipynb) | Agentorkestrering | ⭐⭐⭐ Avansert |
| 6 | [`session06_models_router.ipynb`](./notebooks/session06_models_router.ipynb) | Intent-ruting | ⭐⭐⭐ Avansert |
| 6 | [`session06_models_pipeline.ipynb`](./notebooks/session06_models_pipeline.ipynb) | Pipeline-orkestrering | ⭐⭐⭐ Avansert |

### Dokumentasjon

Omfattende guider og referanser:

| Dokument | Beskrivelse | Bruk når |
|----------|-------------|----------|
| [QUICK_START.md](./QUICK_START.md) | Hurtigstartveiledning | Starter fra bunnen |
| [QUICK_REFERENCE.md](./QUICK_REFERENCE.md) | Kommando- og API-hurtigreferanse | Trenger raske svar |
| [FOUNDRY_SDK_QUICKREF.md](./FOUNDRY_SDK_QUICKREF.md) | SDK-mønstre & eksempler | Skriver kode |
| [ENV_CONFIGURATION.md](./ENV_CONFIGURATION.md) | Veiledning for miljøvariabler | Konfigurerer eksempler |
| [SAMPLES_UPDATE_SUMMARY.md](./SAMPLES_UPDATE_SUMMARY.md) | Nyeste forbedringer i eksempler | Forstå endringer |
| [SDK_MIGRATION_NOTES.md](./SDK_MIGRATION_NOTES.md) | Migreringsveiledning | Oppgraderer kode |
| [notebooks/TROUBLESHOOTING.md](./notebooks/TROUBLESHOOTING.md) | Vanlige problemer & løsninger | Feilsøking |

---

## 🎓 Anbefalinger for læringssti

### For nybegynnere (3-4 timer)
1. ✅ Økt 1: Kom i gang (fokus på oppsett og grunnleggende chat)
2. ✅ Økt 2: Grunnleggende RAG (hopp over evaluering i starten)
3. ✅ Økt 3: Enkel benchmarking (kun 2 modeller)
4. ⏭️ Hopp over økt 4-6 for nå
5. 🔄 Gå tilbake til økt 4-6 etter å ha bygget din første applikasjon

### For utviklere på mellomnivå (3 timer)
1. ⚡ Økt 1: Rask validering av oppsett
2. ✅ Økt 2: Fullfør RAG-pipeline med evaluering
3. ✅ Økt 3: Full benchmark-suite
4. ✅ Økt 4: Modelloptimalisering
5. ✅ Økt 5-6: Fokus på arkitektur-mønstre

### For avanserte utøvere (2-3 timer)
1. ⚡ Økt 1-3: Rask gjennomgang og validering
2. ✅ Økt 4: Dypdykk i optimalisering
3. ✅ Økt 5: Multi-agent arkitektur
4. ✅ Økt 6: Produksjonsmønstre og skalering
5. 🚀 Utvid: Bygg tilpasset rutingslogikk og hybrid-distribusjoner

---

## Workshop-øktpakke (Fokuserte 30-minutters laboratorier)

Hvis du følger det konsentrerte 6-økt workshop-formatet, bruk disse dedikerte guidene (hver tilsvarer og utfyller de bredere modul-dokumentene ovenfor):

| Workshop-økt | Veiledning | Kjernefokus |
|--------------|------------|-------------|
| 1 | [Session01-GettingStartedFoundryLocal](./Session01-GettingStartedFoundryLocal.md) | Installere, validere, kjøre phi & GPT-OSS-20B, akselerasjon |
| 2 | [Session02-BuildAISolutionsRAG](./Session02-BuildAISolutionsRAG.md) | Prompt engineering, RAG-mønstre, CSV & dokumentforankring, migrering |
| 3 | [Session03-OpenSourceModels](./Session03-OpenSourceModels.md) | Integrasjon med Hugging Face, benchmarking, modellvalg |
| 4 | [Session04-CuttingEdgeModels](./Session04-CuttingEdgeModels.md) | SLM vs LLM, WebGPU, Chainlit RAG, ONNX-akselerasjon |
| 5 | [Session05-AIPoweredAgents](./Session05-AIPoweredAgents.md) | Agentroller, minne, verktøy, orkestrering |
| 6 | [Session06-ModelsAsTools](./Session06-ModelsAsTools.md) | Ruting, kjeding, skaleringsvei til Azure |

Hver sesjonsfil inkluderer: sammendrag, læringsmål, 30-minutters demo, startprosjekt, valideringssjekkliste, feilsøking og referanser til den offisielle Foundry Local Python SDK.

### Eksempelskript

Installer workshop-avhengigheter (Windows):

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

Hvis du kjører Foundry Local-tjenesten på en annen (Windows) maskin eller VM fra macOS, eksporter endepunktet:

```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```

| Sesjon | Skript(er) | Beskrivelse |
|--------|------------|-------------|
| 1 | `samples/session01/chat_bootstrap.py` | Bootstrap-tjeneste & streaming-chat |
| 2 | `samples/session02/rag_pipeline.py` | Minimal RAG (inn-minne-embeddings) |
|   | `samples/session02/rag_eval_ragas.py` | RAG-evaluering med ragas-metrikker |
| 3 | `samples/session03/benchmark_oss_models.py` | Multi-modell latens- og gjennomstrømningsbenchmarking |
| 4 | `samples/session04/model_compare.py` | SLM vs LLM-sammenligning (latens & eksempelutdata) |
| 5 | `samples/session05/agents_orchestrator.py` | To-agent forsknings- → redaksjonell pipeline |
| 6 | `samples/session06/models_router.py` | Intent-basert rutingdemo |
|   | `samples/session06/models_pipeline.py` | Multi-trinn plan/utfør/forbedre-kjede |

### Miljøvariabler (Felles for eksempler)

| Variabel | Formål | Eksempel |
|----------|--------|----------|
| `FOUNDRY_LOCAL_ALIAS` | Standard enkeltmodell-alias for grunnleggende eksempler | `phi-4-mini` |
| `SLM_ALIAS` / `LLM_ALIAS` | Eksplisitt SLM vs større modell for sammenligning | `phi-4-mini` / `gpt-oss-20b` |
| `BENCH_MODELS` | Kommaliste over aliaser for benchmarking | `qwen2.5-0.5b,mistral-7b` |
| `BENCH_ROUNDS` | Benchmark-repetisjoner per modell | `3` |
| `BENCH_PROMPT` | Prompt brukt i benchmarking | `Forklar retrieval augmented generation kort.` |
| `EMBED_MODEL` | Sentence-transformers embedding-modell | `sentence-transformers/all-MiniLM-L6-v2` |
| `RAG_QUESTION` | Overstyr testspørsmål for RAG-pipeline | `Hvorfor bruke RAG med lokal inferens?` |
| `AGENT_QUESTION` | Overstyr agents-pipeline-spørsmål | `Forklar hvorfor edge AI er viktig for samsvar.` |
| `AGENT_MODEL_PRIMARY` | Modellalias for forskningsagent | `phi-4-mini` |
| `AGENT_MODEL_EDITOR` | Modellalias for redaktøragent (kan variere) | `gpt-oss-20b` |
| `SHOW_USAGE` | Når `1`, skriver ut tokenbruk per fullføring | `1` |
| `RETRY_ON_FAIL` | Når `1`, prøv på nytt én gang ved midlertidige chatfeil | `1` |
| `RETRY_BACKOFF` | Sekunder å vente før ny forsøk | `1.0` |

Hvis en variabel ikke er satt, faller skriptene tilbake til fornuftige standardverdier. For enkeltmodell-demoer trenger du vanligvis bare `FOUNDRY_LOCAL_ALIAS`.

### Verktøymodul

Alle eksempler deler nå en hjelper `samples/workshop_utils.py` som tilbyr:

* Hurtigbufret `FoundryLocalManager` + OpenAI-klientoppretting
* `chat_once()` hjelper med valgfri ny forsøk + brukstrykk
* Enkel rapportering av tokenbruk (aktiver via `SHOW_USAGE=1`)

Dette reduserer duplisering og fremhever beste praksis for effektiv lokal modellorkestrering.

## Valgfrie forbedringer (Tverrsesjon)

| Tema | Forbedring | Sesjoner | Miljø / Veksle |
|------|------------|----------|----------------|
| Determinisme | Fast temperatur + stabile promptsett | 1–6 | Sett `temperature=0`, `top_p=1` |
| Synlighet av tokenbruk | Konsistent kostnad/effektivitet undervisning | 1–6 | `SHOW_USAGE=1` |
| Streaming av første token | Oppfattet latensmetrisk | 1,3,4,6 | `BENCH_STREAM=1` (benchmark) |
| Robusthet ved ny forsøk | Håndterer midlertidig kaldstart | Alle | `RETRY_ON_FAIL=1` + `RETRY_BACKOFF` |
| Multi-modell-agenter | Heterogen rolle-spesialisering | 5 | `AGENT_MODEL_PRIMARY`, `AGENT_MODEL_EDITOR` |
| Adaptiv ruting | Intent + kostnadsheuristikk | 6 | Utvid router med eskaleringslogikk |
| Vektorminne | Langsiktig semantisk gjenkalling | 2,5,6 | Integrer FAISS/Chroma embedding-indeks |
| Sporingsutdrag | Revisjon & evaluering | 2,5,6 | Legg til JSON-linjer per trinn |
| Kvalitetsrubrikker | Kvalitativ sporing | 3–6 | Sekundære scoringsprompter |
| Røyktester | Rask validering før workshop | Alle | `python Workshop/tests/smoke.py` |

### Deterministisk rask start

```powershell
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
python Workshop\tests\smoke.py
```

Forvent stabile tokenantall på tvers av gjentatte identiske innganger.

### RAG-evaluering (Sesjon 2)

Bruk `rag_eval_ragas.py` for å beregne svarrelevans, troverdighet og kontekstpresisjon på et lite syntetisk datasett:

```powershell
cd Workshop/samples
python -m session02.rag_eval_ragas
```

Utvid ved å levere en større JSONL med spørsmål, kontekster og sannheter, og deretter konvertere til et Hugging Face `Dataset`.

## CLI Kommando Nøyaktighetsvedlegg

Workshopen bruker bevisst kun dokumenterte / stabile Foundry Local CLI-kommandoer.

### Refererte stabile kommandoer

| Kategori | Kommando | Formål |
|----------|----------|--------|
| Kjerne | `foundry --version` | Vis installert versjon |
| Kjerne | `foundry init` | Initialiser konfigurasjon |
| Tjeneste | `foundry service start` | Start lokal tjeneste (hvis ikke automatisk) |
| Tjeneste | `foundry status` | Vis tjenestestatus |
| Modeller | `foundry model list` | List katalog / tilgjengelige modeller |
| Modeller | `foundry model download <alias>` | Last ned modellvekter til hurtigbuffer |
| Modeller | `foundry model run <alias>` | Start (last) en modell lokalt; kombiner med `--prompt` for én-gangs |
| Modeller | `foundry model unload <alias>` / `foundry model stop <alias>` | Fjern en modell fra minnet (hvis støttet) |
| Hurtigbuffer | `foundry cache list` | List hurtigbufrede (nedlastede) modeller |
| System | `foundry system info` | Maskinvare- & akselerasjonskapabiliteter-snapshot |
| System | `foundry system gpu-info` | GPU-diagnostisk info |
| Konfigurasjon | `foundry config list` | Vis gjeldende konfigurasjonsverdier |
| Konfigurasjon | `foundry config set <key> <value>` | Oppdater konfigurasjon |

### Én-gangs promptmønster

I stedet for en utgått `model chat` underkommando, bruk:

```powershell
foundry model run <alias> --prompt "Your question here"
```

Dette utfører en enkelt prompt/svar-syklus og avslutter deretter.

### Fjernede / Unngåtte mønstre

| Utgått / Udokumentert | Erstatning / Veiledning |
|------------------------|-------------------------|
| `foundry model chat <model> "..."` | `foundry model run <model> --prompt "..."` |
| `foundry model list --running` | Bruk vanlig `foundry model list` + nylig aktivitet / logger |
| `foundry model list --cached` | `foundry cache list` |
| `foundry model stats <model>` | Bruk benchmark Python-skript + OS-verktøy (Task Manager / `nvidia-smi`) |
| `foundry model benchmark ...` | `samples/session03/benchmark_oss_models.py` |

### Benchmarking & Telemetri

- Latens, p95, tokens/sek: `samples/session03/benchmark_oss_models.py`
- Første-token latens (streaming): sett `BENCH_STREAM=1`
- Ressursbruk: OS-monitorer (Task Manager, Activity Monitor, `nvidia-smi`) + `foundry system info`.

Etter hvert som nye CLI-telemetrikommandoer stabiliseres, kan de enkelt integreres i sesjonsmarkeringene.

### Automatisk Lint-sjekk

En automatisk linter forhindrer gjeninnføring av utgåtte CLI-mønstre inne i avgrensede kodeblokker i markdown-filer:

Skript: `Workshop/scripts/lint_markdown_cli.py`

Utgåtte mønstre blokkeres inne i kodegjerder.

Anbefalte erstatninger:
| Utgått | Erstatning |
|--------|------------|
| `foundry model chat <a> "..."` | `foundry model run <a> --prompt "..."` |
| `model list --running` | `model list` |
| `model list --cached` | `cache list` |
| `model stats` | Benchmark-skript + systemverktøy |
| `model benchmark` | `samples/session03/benchmark_oss_models.py` |
| `model list --available` | `model list` |

Kjør lokalt:
```powershell
python Workshop\scripts\lint_markdown_cli.py --verbose
```

GitHub Action: `.github/workflows/markdown-cli-lint.yml` kjører ved hver push & PR.

Valgfri pre-commit hook:
```bash
echo "python Workshop/scripts/lint_markdown_cli.py" > .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```

## Rask CLI → SDK Migrasjonstabell

| Oppgave | CLI Én-liner | SDK (Python) Ekvivalent | Notater |
|---------|--------------|-------------------------|---------|
| Kjør en modell én gang (prompt) | `foundry model run phi-4-mini --prompt "Hello"` | `manager=FoundryLocalManager("phi-4-mini"); client=OpenAI(base_url=manager.endpoint, api_key=manager.api_key or "not-needed"); client.chat.completions.create(model=manager.get_model_info("phi-4-mini").id, messages=[{"role":"user","content":"Hello"}])` | SDK starter tjeneste & hurtigbufring automatisk |
| Last ned (hurtigbuffer) modell | `foundry model download qwen2.5-0.5b` | `FoundryLocalManager("qwen2.5-0.5b")  # utløser nedlasting/lasting` | Manager velger beste variant hvis aliaset peker til flere versjoner |
| List katalog | `foundry model list` | `# bruk manager for hvert alias eller oppretthold kjent liste` | CLI samler; SDK for øyeblikket per-alias-instansiering |
| List hurtigbufrede modeller | `foundry cache list` | `manager.list_cached_models()` | Etter manager-initiering (hvilket som helst alias) |
| Aktiver GPU-akselerasjon | `foundry config set compute.onnx.enable_gpu true` | `# CLI-handling; SDK antar at konfigurasjon allerede er brukt` | Konfigurasjon er ekstern sideeffekt |
| Hent endepunkt-URL | (implisitt) | `manager.endpoint` | Brukes til å opprette OpenAI-kompatibel klient |
| Varm opp en modell | `foundry model run <alias>` deretter første prompt | `chat_once(alias, messages=[...])` (verktøy) | Verktøy håndterer initial kald latens oppvarming |
| Mål latens | `python -m session03.benchmark_oss_models` | `import benchmark_oss_models` (eller nytt eksporteringsskript) | Foretrekk skript for konsistente metrikker |
| Stopp / fjern modell | `foundry model unload <alias>` | (Ikke eksponert – start tjeneste / prosess på nytt) | Vanligvis ikke nødvendig for workshop-flyt |
| Hent tokenbruk | (vis utdata) | `resp.usage.total_tokens` | Tilbys hvis backend returnerer bruksobjekt |

## Benchmark Markdown Eksport

Bruk skriptet `Workshop/scripts/export_benchmark_markdown.py` for å kjøre en fersk benchmark (samme logikk som `samples/session03/benchmark_oss_models.py`) og generere en GitHub-vennlig Markdown-tabell pluss rå JSON.

### Eksempel

```powershell
python Workshop\scripts\export_benchmark_markdown.py --models "qwen2.5-0.5b,mistral-7b" --prompt "Explain retrieval augmented generation briefly." --rounds 3 --output benchmark_report.md
```

Genererte filer:
| Fil | Innhold |
|-----|---------|
| `benchmark_report.md` | Markdown-tabell + tolkningshint |
| `benchmark_report.json` | Rå metrikker (for sammenligning / trendsporing) |

Sett `BENCH_STREAM=1` i miljøet for å inkludere første-token latens hvis støttet.

---

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi tilstreber nøyaktighet, vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på dets opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
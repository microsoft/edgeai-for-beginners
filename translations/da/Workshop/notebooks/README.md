# Workshop Notebooks

> **Interaktive Jupyter Notebooks til praktisk Edge AI-læring**
>
> Progressiv, selvstyret undervisning, der går fra grundlæggende chat-komplettering til avancerede multi-agent systemer ved brug af Microsoft Foundry Local og Small Language Models.

---

## 📖 Introduktion

Velkommen til samlingen af **EdgeAI for Beginners Workshop Notebooks**. Disse interaktive Jupyter-notebooks giver dig en praktisk læringsoplevelse, hvor du kan skrive, køre og eksperimentere med Edge AI-kode i realtid.

### Hvorfor Jupyter Notebooks?

I modsætning til traditionelle tutorials tilbyder disse notebooks:

- **Interaktiv læring**: Kør kodeceller og se resultater med det samme
- **Eksperimentering**: Ændr parametre og observer ændringer i realtid
- **Dokumentation**: Forklaringer og markdown-celler guider dig gennem begreberne
- **Reproducerbarhed**: Færdige eksempler, du kan referere til og genbruge
- **Visualisering**: Se præstationsmålinger, embeddings og resultater direkte i notebooken

### Hvad gør disse notebooks specielle?

Hver notebook er designet efter **produktionsklare bedste praksisser**:

✅ **Omfattende fejlhåndtering** - Elegant nedgradering og informative fejlmeddelelser  
✅ **Type hints & dokumentation** - Klare funktionssignaturer og docstrings  
✅ **Præstationsovervågning** - Sporing af tokenforbrug og latenstid  
✅ **Modulær design** - Genanvendelige mønstre, du kan tilpasse til dine projekter  
✅ **Progressiv kompleksitet** - Bygger systematisk videre på tidligere sessioner  

---

## 🎯 Læringsmål

### Kernekompetencer, du vil udvikle

Ved at arbejde med disse notebooks vil du mestre:

1. **Lokalt AI-service management**
   - Konfigurer og administrer Microsoft Foundry Local-tjenester
   - Vælg og indlæs passende modeller til din hardware
   - Overvåg ressourceforbrug og optimer præstation
   - Håndter serviceopdagelse og sundhedstjek

2. **Udvikling af AI-applikationer**
   - Implementer OpenAI-kompatible chat-kompletteringer lokalt
   - Byg streaminggrænseflader for bedre brugeroplevelse
   - Design effektive prompts til Small Language Models
   - Integrer lokale modeller i applikationer

3. **Retrieval Augmented Generation (RAG)**
   - Skab semantisk søgning med vektorembeddings
   - Forankr LLM-svar i domænespecifikke dokumenter
   - Evaluer RAG-kvalitet med RAGAS-målinger
   - Skalér fra prototype til produktion

4. **Præstationsoptimering**
   - Benchmark flere modeller systematisk
   - Mål latenstid, gennemløb og tid til første token
   - Sammenlign Small Language Models vs Large Language Models
   - Vælg optimale modeller baseret på præstations-/kvalitetshandlinger

5. **Multi-agent orkestrering**
   - Design specialiserede agenter til forskellige opgaver
   - Implementer agenthukommelse og kontekststyring
   - Koordiner flere agenter i komplekse arbejdsgange
   - Byg koordinator-mønstre for agent-samarbejde

6. **Intelligent model-routing**
   - Implementer intent-detektion og mønstergenkendelse
   - Rut forespørgsler automatisk til passende modeller
   - Byg flertrins pipelines (planlæg → udfør → forfin)
   - Design skalerbare model-as-tools arkitekturer

---

## 🎓 Læringsresultater

### Hvad du vil bygge

| Notebook | Leverance | Demonstrerede færdigheder | Sværhedsgrad |
|----------|-----------|---------------------------|--------------|
| **Session 01** | Chat-app med streaming | Serviceopsætning, grundlæggende kompletteringer, streaming UX | ⭐ Begynder |
| **Session 02 (RAG)** | RAG-pipeline med evaluering | Embeddings, semantisk søgning, kvalitetsmålinger | ⭐⭐ Mellem |
| **Session 02 (Eval)** | RAG-kvalitetsevaluator | RAGAS-målinger, systematisk evaluering | ⭐⭐ Mellem |
| **Session 03** | Multi-model benchmark | Præstationsmåling, model-sammenligning | ⭐⭐ Mellem |
| **Session 04** | SLM vs LLM sammenligning | Handlingsanalyse, optimeringsstrategier | ⭐⭐⭐ Avanceret |
| **Session 05** | Multi-agent orkestrator | Agentdesign, hukommelse, koordinering | ⭐⭐⭐ Avanceret |
| **Session 06 (Router)** | Intelligent routing-system | Intent-detektion, modelvalg | ⭐⭐⭐ Avanceret |
| **Session 06 (Pipeline)** | Flertrins pipeline | Planlæg/udfør/forfin arbejdsgange | ⭐⭐⭐ Avanceret |

### Kompetenceudvikling

```
Session 01 ────► Session 02 ────► Session 03 ────► Session 04 ────► Session 05-06
   Basic            RAG             Benchmarking      Comparison      Multi-Agent
   Chat             Systems         & Performance     & Optimization  Orchestration
   
Foundation    │   Intermediate   │   Advanced       │   Expert
──────────────┴──────────────────┴──────────────────┴──────────────►
```

---

## 📅 Workshopplan

### 🚀 Halvdagsworkshop (3,5 timer)

**Perfekt til: Teamtræningssessioner, hackathons, konferencetutorials**

| Tid | Varighed | Session | Emner | Aktiviteter |
|-----|----------|---------|-------|-------------|
| **0:00** | 30 min | Opsætning & intro | Miljøopsætning, Foundry Local installation | Installer afhængigheder, verificer opsætning |
| **0:30** | 30 min | Session 01 | Grundlæggende chat-kompletteringer, streaming | Kør notebook, ændr prompts |
| **1:00** | 45 min | Session 02 | RAG-pipeline, embeddings, evaluering | Byg RAG-system, test forespørgsler |
| **1:45** | 15 min | Pause | ☕ Kaffe & spørgsmål | — |
| **2:00** | 30 min | Session 03 | Multi-model benchmarking | Sammenlign 3+ modeller |
| **2:30** | 30 min | Session 04 | SLM vs LLM handlingsanalyse | Analyser præstation/kvalitet |
| **3:00** | 30 min | Session 05-06 | Multi-agent systemer & routing | Udforsk avancerede mønstre |

**Output**: Deltagerne forlader workshoppen med 6 fungerende Edge AI-applikationer og produktionsklare kodemønstre.

---

### 🎓 Heldagsworkshop (6 timer)

**Perfekt til: Dybtgående træning, bootcamps, universitetskurser**

| Tid | Varighed | Session | Emner | Aktiviteter |
|-----|----------|---------|-------|-------------|
| **0:00** | 45 min | Opsætning & teori | Miljøopsætning, Edge AI-grundlæggende | Installer, verificer, diskuter anvendelsesscenarier |
| **0:45** | 45 min | Session 01 | Chat-kompletteringer dybdegående | Implementer grundlæggende & streaming chat |
| **1:30** | 30 min | Pause | ☕ Kaffe & netværk | — |
| **2:00** | 60 min | Session 02 (Begge) | RAG-pipeline + RAGAS evaluering | Byg komplet RAG-system |
| **3:00** | 30 min | Praktisk lab 1 | Tilpas RAG til dit domæne | Anvend på egne dokumenter |
| **3:30** | 30 min | Frokost | 🍽️ | — |
| **4:00** | 45 min | Session 03 | Benchmarking-metodologi | Systematisk model-sammenligning |
| **4:45** | 45 min | Session 04 | Optimeringsstrategier | SLM vs LLM analyse |
| **5:30** | 60 min | Session 05-06 | Avanceret orkestrering | Multi-agent systemer, routing |
| **6:30** | 30 min | Praktisk lab 2 | Byg tilpasset agentsystem | Design din egen orkestrator |

**Output**: Dyb forståelse af Edge AI-mønstre plus 2 tilpassede projekter.

---

### 📚 Selvstyret læring (2 uger)

**Perfekt til: Individuelle lærere, onlinekurser, selvstudie**

#### Uge 1: Grundlæggende (6 timer)

| Dag | Fokus | Varighed | Notebooks | Hjemmearbejde |
|-----|-------|----------|-----------|---------------|
| **Man** | Opsætning & grundlæggende | 1,5 t | Session 01 | Ændr prompts, test streaming |
| **Ons** | RAG-grundlæggende | 2 t | Session 02 (begge) | Tilføj dine egne dokumenter |
| **Fre** | Benchmarking | 1,5 t | Session 03 | Sammenlign yderligere modeller |
| **Lør** | Gennemgang & praksis | 1 t | Alle uge 1 | Fuldfør øvelser, fejlret |

#### Uge 2: Avanceret (5 timer)

| Dag | Fokus | Varighed | Notebooks | Hjemmearbejde |
|-----|-------|----------|-----------|---------------|
| **Man** | Optimering | 1,5 t | Session 04 | Dokumentér handlingsanalyser |
| **Ons** | Multi-agent systemer | 2 t | Session 05 | Design tilpassede agenter |
| **Fre** | Intelligent routing | 1,5 t | Session 06 (begge) | Byg routing-logik |
| **Lør** | Afsluttende projekt | 2 t | Integration | Kombinér flere mønstre |

**Output**: Mestering af Edge AI-mønstre plus porteføljeprojekt.

---

## 📔 Notebook-beskrivelser

### 📘 Session 01: Chat Bootstrap
**Fil**: `session01_chat_bootstrap.ipynb`  
**Varighed**: 20-30 minutter  
**Forudsætninger**: Ingen  
**Sværhedsgrad**: ⭐ Begynder

**Hvad du vil lære**:
- Installér og konfigurer Foundry Local Python SDK
- Brug `FoundryLocalManager` til automatisk serviceopdagelse
- Implementer grundlæggende chat-kompletteringer med OpenAI-kompatibel API
- Byg streaming-svar for bedre brugeroplevelse
- Håndter fejl og serviceutilgængelighed elegant

**Nøglebegreber**: Service management, chat-kompletteringer, streaming, fejlhåndtering

**Du vil bygge**: Interaktiv chat-applikation med streaming-support

---

### 📗 Session 02: RAG Pipeline
**Fil**: `session02_rag_pipeline.ipynb`  
**Varighed**: 30-45 minutter  
**Forudsætninger**: Session 01  
**Sværhedsgrad**: ⭐⭐ Mellem

**Hvad du vil lære**:
- Implementer Retrieval Augmented Generation (RAG)-mønster
- Skab vektorembeddings med sentence-transformers
- Byg semantisk søgning med cosinus-similaritet
- Forankr LLM-svar i domænedokumenter
- Håndter valgfrie afhængigheder med import guards

**Nøglebegreber**: RAG-arkitektur, embeddings, semantisk søgning, vektorsimilaritet

**Du vil bygge**: Dokumentforankret spørgsmål-svar-system

---

### 📗 Session 02: RAG Evaluering med RAGAS
**Fil**: `session02_rag_eval_ragas.ipynb`  
**Varighed**: 30-45 minutter  
**Forudsætninger**: Session 02 RAG Pipeline  
**Sværhedsgrad**: ⭐⭐ Mellem

**Hvad du vil lære**:
- Evaluer RAG-kvalitet med industristandard-målinger
- Mål kontekstrelevans, svarrelevans, troværdighed
- Brug RAGAS-rammen til systematisk evaluering
- Identificer og ret RAG-kvalitetsproblemer
- Byg evalueringsdatasæt til dit domæne

**Nøglebegreber**: RAG-evaluering, RAGAS-målinger, kvalitetsmåling, systematisk testning

**Du vil bygge**: RAG-kvalitetsevalueringsramme

---

### 📙 Session 03: Benchmark OSS-modeller
**Fil**: `session03_benchmark_oss_models.ipynb`  
**Varighed**: 30-45 minutter  
**Forudsætninger**: Session 01  
**Sværhedsgrad**: ⭐⭐ Mellem

**Hvad du vil lære**:
- Systematisk benchmark af flere modeller
- Mål latenstid, gennemløb, tid til første token
- Implementer elegant nedgradering ved modelfejl
- Sammenlign præstation på tværs af modelfamilier
- Visualiser og analyser benchmark-resultater

**Nøglebegreber**: Præstationsbenchmarking, latenstidsmåling, modelsammenligning, statistisk analyse

**Du vil bygge**: Multi-model benchmark-suite

---

### 📙 Session 04: Model-sammenligning (SLM vs LLM)
**Fil**: `session04_model_compare.ipynb`  
**Varighed**: 30-45 minutter  
**Forudsætninger**: Sessioner 01, 03  
**Sværhedsgrad**: ⭐⭐⭐ Avanceret

**Hvad du vil lære**:
- Sammenlign Small Language Models vs Large Language Models
- Analyser præstation vs kvalitetshandlinger
- Mål edge-egnethedsmålinger
- Vælg optimale modeller til implementeringsbegrænsninger
- Dokumentér beslutningskriterier for modelvalg

**Nøglebegreber**: Modelvalg, handlingsanalyse, optimeringsstrategier, implementeringsplanlægning

**Du vil bygge**: SLM vs LLM sammenligningsramme

---

### 📕 Session 05: Multi-agent orkestrator
**Fil**: `session05_agents_orchestrator.ipynb`  
**Varighed**: 45-60 minutter  
**Forudsætninger**: Sessioner 01-02  
**Sværhedsgrad**: ⭐⭐⭐ Avanceret

**Hvad du vil lære**:
- Design specialiserede agenter til forskellige opgaver
- Implementer agenthukommelse og kontekststyring
- Byg koordinator-mønstre for agent-samarbejde
- Håndter agentkommunikation og overdragelser
- Overvåg multi-agent systempræstation

**Nøglebegreber**: Agentarkitektur, koordinator-mønstre, hukommelsesstyring, agentorkestrering

**Du vil bygge**: Multi-agent system med koordinator og specialister

---

### 📕 Session 06: Model-router
**Fil**: `session06_models_router.ipynb`  
**Varighed**: 30-45 minutter  
**Forudsætninger**: Sessioner 01, 03  
**Sværhedsgrad**: ⭐⭐⭐ Avanceret

**Hvad du vil lære**:
- Implementer intent-detektion og mønstergenkendelse
- Byg nøgleordsbaseret model-routing
- Rut forespørgsler automatisk til passende modeller
- Konfigurer multi-model registre
- Overvåg routing-beslutninger og præstation

**Nøglebegreber**: Intent-detektion, model-routing, mønstergenkendelse, intelligent valg

**Du vil bygge**: Intelligent model-routing system

---

### 📕 Session 06: Flertrins pipeline
**Fil**: `session06_models_pipeline.ipynb`  
**Varighed**: 30-45 minutter  
**Forudsætninger**: Sessioner 01, 06 Router  
**Sværhedsgrad**: ⭐⭐⭐ Avanceret

**Hvad du vil lære**:
- Byg flertrins AI-pipelines (planlæg → udfør → forfin)
- Integrer router til intelligent modelvalg
- Implementer pipeline-fejlhåndtering og genopretning
- Overvåg pipeline-præstation og stadier
- Design skalerbare model-as-tools arkitekturer

**Nøglebegreber**: Pipeline-arkitektur, flertrinsbehandling, fejlhåndtering, skaleringsmønstre

**Du vil bygge**: Flertrins intelligent pipeline med routing

---

## 🚀 Kom godt i gang

### Forudsætninger

**Systemkrav**:
- **OS**: Windows 10/11, macOS 11+ eller Linux (Ubuntu 20.04+)
- **RAM**: Minimum 8GB, anbefalet 16GB+
- **Lagring**: 10GB+ ledig plads til modeller
- **Hardware**: CPU med AVX2; GPU (CUDA, Qualcomm NPU) valgfrit

**Softwarekrav**:
- **Python 3.8+** med pip
- **Jupyter Notebook** eller **VS Code** med Jupyter-udvidelse
- **Microsoft Foundry Local** installeret og konfigureret
- **Git** (til at klone repository)

### Installationsvejledning

#### 1. Installer Foundry Local

**Windows**:
```cmd
winget install Microsoft.FoundryLocal
```

**macOS**:
```bash
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**Bekræft installation**:
```bash
foundry --version
```

#### 2. Opsæt Python-miljø

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

#### 3. Start Foundry Local

```bash
# Load a model (auto-downloads if needed)
foundry model run phi-4-mini

# Verify service is running
foundry service status
```

#### 4. Start Jupyter

```bash
# Start Jupyter Notebook
jupyter notebook notebooks/

# Or use VS Code with Jupyter extension
code notebooks/
```

### Hurtig verifikation

Kør dette i en Python-celle for at verificere opsætningen:

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

**Forventet output**: En hilsen fra den lokale model.

---

## 📝 Workshop bedste praksis

### For instruktører

**Før workshoppen**:
- ✅ Send installationsvejledning ud 1 uge i forvejen
- ✅ Test alle notebooks på målhardware
- ✅ Forbered en fejlfinding-guide til almindelige problemer
- ✅ Hav backup-modeller klar (phi-3.5-mini, hvis phi-4-mini fejler)
- ✅ Opsæt en fælles chatkanal til spørgsmål

**Under workshoppen**:
- ✅ Start med en hurtig miljøkontrol (5 minutter)
- ✅ Del fejlfinding-ressourcer med det samme
- ✅ Opfordr til eksperimentering og ændringer
- ✅ Brug pauser strategisk (efter hver 2. session)
- ✅ Hav TAs til rådighed for individuel hjælp

**Efter workshoppen**:
- ✅ Del komplette fungerende notebooks og løsninger
- ✅ Giv links til yderligere ressourcer
- ✅ Opret en feedback-undersøgelse for forbedringer
- ✅ Tilbyd kontortid til opfølgende spørgsmål

### For deltagere

**Maksimer din læring**:
- ✅ Fuldfør opsætningen før workshoppen starter
- ✅ Kør hver kodecelle selv (læs ikke bare)
- ✅ Eksperimenter med parametre og prompts
- ✅ Tag noter om indsigter og faldgruber
- ✅ Stil spørgsmål, når du sidder fast (andre har sandsynligvis samme spørgsmål)

**Almindelige fejl at undgå**:
- ❌ Springe over cellekørselsrækkefølge (kør sekventielt)
- ❌ Ikke læse fejlmeddelelser grundigt
- ❌ Skynde sig igennem uden at forstå
- ❌ Ignorere markdown-forklaringer
- ❌ Ikke gemme dine ændrede notebooks

**Fejlfindingstips**:
1. **Service kører ikke**: Tjek `foundry service status`
2. **Importfejl**: Bekræft, at det virtuelle miljø er aktiveret
3. **Model ikke fundet**: Kør `foundry model ls` for at liste indlæste modeller
4. **Langsom ydeevne**: Tjek RAM-forbrug, luk andre applikationer
5. **Uventede resultater**: Genstart kernel og kør alle celler fra toppen

---

## 🔗 Yderligere ressourcer

### Workshopmaterialer

- **[Workshop hovedguide](../Readme.md)** - Oversigt, læringsmål, karriereudbytte
- **[Python eksempler](../../../../Workshop/samples)** - Tilsvarende Python-scripts for hver session
- **[Sessionsguider](../../../../Workshop)** - Detaljerede markdown-guider (Session01-06)
- **[Scripts](../../../../Workshop/scripts)** - Validerings- og testværktøjer
- **[Fejlfinding](./TROUBLESHOOTING.md)** - Almindelige problemer og løsninger
- **[Hurtig start](./quickstart.md)** - Hurtig guide til at komme i gang

### Dokumentation

- **[Foundry Local Docs](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)** - Officiel Microsoft-dokumentation
- **[OpenAI Python SDK](https://github.com/openai/openai-python)** - OpenAI SDK-reference
- **[Sentence Transformers](https://www.sbert.net/)** - Dokumentation for embedding-modeller
- **[RAGAS Framework](https://docs.ragas.io/)** - RAG evalueringsmetrikker

### Fællesskab

- **[GitHub Diskussioner](https://github.com/microsoft/edgeai-for-beginners/discussions)** - Stil spørgsmål, del projekter
- **[Azure AI Foundry Discord](https://discord.com/invite/ByRwuEEgH4)** - Real-time fællesskabsstøtte
- **[Stack Overflow](https://stackoverflow.com/questions/tagged/foundry-local)** - Teknisk Q&A

---

## 🎯 Læringsvej anbefalinger

### Begynderforløb (Start her)

1. **Session 01** - Chat Bootstrap
2. **Session 02** - RAG Pipeline
3. **Session 03** - Benchmark-modeller

**Tid**: ~2 timer | **Fokus**: Grundlæggende mønstre

---

### Mellemforløb

1. Fuldfør begynderforløb
2. **Session 02** - RAG Evaluering
3. **Session 04** - Model-sammenligning

**Tid**: ~4 timer | **Fokus**: Kvalitet og optimering

---

### Avanceret forløb (Fuld workshop)

1. Fuldfør mellemforløb
2. **Session 05** - Multi-agent orkestrator
3. **Session 06** - Model-router
4. **Session 06** - Flertrins pipeline

**Tid**: ~6 timer | **Fokus**: Produktionsmønstre

---

### Tilpasset projektforløb

1. Fuldfør begynderforløb (Sessioner 01-03)
2. Vælg ÉN avanceret session baseret på dit mål:
   - **Bygger RAG-app?** → Session 02 Evaluering
   - **Optimerer ydeevne?** → Session 04 Sammenligning
   - **Komplekse arbejdsgange?** → Session 05 Orkestrator
   - **Skalerbar arkitektur?** → Session 06 Router + Pipeline

**Tid**: ~3 timer | **Fokus**: Projekt-specifikke færdigheder

---

## 📊 Succeskriterier

Følg din fremgang med disse milepæle:

- [ ] **Opsætning fuldført** - Foundry Local kører, alle afhængigheder installeret
- [ ] **Første chat** - Session 01 fuldført, streaming chat fungerer
- [ ] **RAG bygget** - Session 02 fuldført, dokument QA-system funktionelt
- [ ] **Modeller benchmarket** - Session 03 fuldført, ydeevnedata indsamlet
- [ ] **Afvejninger analyseret** - Session 04 fuldført, modelvalgskriterier dokumenteret
- [ ] **Agenter orkestreret** - Session 05 fuldført, multi-agent system fungerer
- [ ] **Routing implementeret** - Session 06 fuldført, intelligent modelvalg funktionelt
- [ ] **Tilpasset projekt** - Anvendt workshopmønstre på din egen brugssag

---

## 🤝 Bidrag

Har du fundet et problem eller en idé? Vi byder bidrag velkommen!

- **Rapportér problemer**: [GitHub Issues](https://github.com/microsoft/edgeai-for-beginners/issues)
- **Foreslå forbedringer**: [GitHub Diskussioner](https://github.com/microsoft/edgeai-for-beginners/discussions)
- **Indsend PRs**: Følg [Bidragsretningslinjer](../../AGENTS.md)

---

## 📄 Licens

Denne workshop er en del af [EdgeAI for Beginners](https://github.com/microsoft/edgeai-for-beginners)-repositoryet og er licenseret under [MIT License](../../../../LICENSE).

---

**Klar til at bygge produktionsklare Edge AI-applikationer?**  
**Start med [Session 01: Chat Bootstrap](./session01_chat_bootstrap.ipynb) →**

---

*Sidst opdateret: 8. oktober 2025 | Workshop version: 2.0*

---

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på at sikre nøjagtighed, skal det bemærkes, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os ikke ansvar for misforståelser eller fejltolkninger, der måtte opstå som følge af brugen af denne oversættelse.
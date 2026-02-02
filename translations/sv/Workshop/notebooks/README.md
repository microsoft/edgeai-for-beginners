# Workshop Notebooks

> **Interaktiva Jupyter Notebooks för praktisk Edge AI-inlärning**
>
> Progressiva, självstyrda handledningar som går från grundläggande chattkompletteringar till avancerade multi-agent-system med Microsoft Foundry Local och Small Language Models.

---

## 📖 Introduktion

Välkommen till samlingen **EdgeAI för nybörjare Workshop Notebooks**. Dessa interaktiva Jupyter-notebooks erbjuder en praktisk inlärningsupplevelse där du kan skriva, köra och experimentera med Edge AI-kod i realtid.

### Varför Jupyter Notebooks?

Till skillnad från traditionella handledningar erbjuder dessa notebooks:

- **Interaktiv inlärning**: Kör kodceller och se omedelbara resultat
- **Experimentering**: Ändra parametrar och observera förändringar i realtid
- **Dokumentation**: Inline-förklaringar och markdown-celler guidar dig genom koncepten
- **Reproducerbarhet**: Kompletta fungerande exempel som du kan referera till och återanvända
- **Visualisering**: Visa prestandamått, inbäddningar och resultat direkt i notebooken

### Vad gör dessa notebooks speciella?

Varje notebook är designad enligt **produktionsklara bästa praxis**:

✅ **Omfattande felhantering** - Smidig nedgradering och informativa felmeddelanden  
✅ **Typanvisningar & dokumentation** - Tydliga funktionssignaturer och docstrings  
✅ **Prestandaövervakning** - Spårning av tokenanvändning och latensmätningar  
✅ **Modulär design** - Återanvändbara mönster som du kan anpassa till dina projekt  
✅ **Progressiv komplexitet** - Bygger systematiskt på tidigare sessioner  

---

## 🎯 Inlärningsmål

### Kärnfärdigheter du kommer att utveckla

Genom att arbeta med dessa notebooks kommer du att bemästra:

1. **Hantering av lokala AI-tjänster**
   - Konfigurera och hantera Microsoft Foundry Local-tjänster
   - Välja och ladda lämpliga modeller för din hårdvara
   - Övervaka resursanvändning och optimera prestanda
   - Hantera tjänsteupptäckt och hälsokontroller

2. **Utveckling av AI-applikationer**
   - Implementera OpenAI-kompatibla chattkompletteringar lokalt
   - Bygga strömmande gränssnitt för bättre användarupplevelse
   - Designa effektiva prompts för Small Language Models
   - Integrera lokala modeller i applikationer

3. **Retrieval Augmented Generation (RAG)**
   - Skapa semantisk sökning med vektor-inbäddningar
   - Förankra LLM-svar i domänspecifika dokument
   - Utvärdera RAG-kvalitet med RAGAS-mått
   - Skala från prototyp till produktion

4. **Prestandaoptimering**
   - Benchmarka flera modeller systematiskt
   - Mäta latens, genomströmning och tid för första token
   - Jämföra Small Language Models mot Large Language Models
   - Välja optimala modeller baserat på prestanda/kvalitetsavvägningar

5. **Multi-agent orkestrering**
   - Designa specialiserade agenter för olika uppgifter
   - Implementera agentminne och kontexthantering
   - Koordinera flera agenter i komplexa arbetsflöden
   - Bygga koordinator-mönster för agent-samarbete

6. **Intelligent modellroutning**
   - Implementera avsiktsdetektion och mönsterigenkänning
   - Automatiskt dirigera frågor till lämpliga modeller
   - Bygga flerstegs pipelines (planera → utföra → förfina)
   - Designa skalbara arkitekturer för modell-som-verktyg

---

## 🎓 Inlärningsresultat

### Vad du kommer att bygga

| Notebook | Leverabel | Demonstrerade färdigheter | Svårighetsgrad |
|----------|-----------|---------------------------|----------------|
| **Session 01** | Chattapp med strömning | Tjänsteinstallation, grundläggande kompletteringar, strömmande UX | ⭐ Nybörjare |
| **Session 02 (RAG)** | RAG-pipeline med utvärdering | Inbäddningar, semantisk sökning, kvalitetsmått | ⭐⭐ Mellan |
| **Session 02 (Eval)** | RAG-kvalitetsutvärderare | RAGAS-mått, systematisk utvärdering | ⭐⭐ Mellan |
| **Session 03** | Multi-modell benchmark | Prestandamätning, modelljämförelse | ⭐⭐ Mellan |
| **Session 04** | SLM vs LLM jämförelse | Avvägningsanalys, optimeringsstrategier | ⭐⭐⭐ Avancerad |
| **Session 05** | Multi-agent orkestrator | Agentdesign, minne, koordinering | ⭐⭐⭐ Avancerad |
| **Session 06 (Router)** | Intelligent routningssystem | Avsiktsdetektion, modellval | ⭐⭐⭐ Avancerad |
| **Session 06 (Pipeline)** | Flerstegs pipeline | Planera/utföra/förfina arbetsflöden | ⭐⭐⭐ Avancerad |

### Kompetensutveckling

```
Session 01 ────► Session 02 ────► Session 03 ────► Session 04 ────► Session 05-06
   Basic            RAG             Benchmarking      Comparison      Multi-Agent
   Chat             Systems         & Performance     & Optimization  Orchestration
   
Foundation    │   Intermediate   │   Advanced       │   Expert
──────────────┴──────────────────┴──────────────────┴──────────────►
```

---

## 📅 Workshop-schema

### 🚀 Halvdagsworkshop (3,5 timmar)

**Perfekt för: Teamutbildningar, hackathons, konferensworkshops**

| Tid | Varaktighet | Session | Ämnen | Aktiviteter |
|-----|-------------|---------|-------|-------------|
| **0:00** | 30 min | Setup & Intro | Miljöinstallation, Foundry Local-installation | Installera beroenden, verifiera installation |
| **0:30** | 30 min | Session 01 | Grundläggande chattkompletteringar, strömning | Kör notebook, ändra prompts |
| **1:00** | 45 min | Session 02 | RAG-pipeline, inbäddningar, utvärdering | Bygg RAG-system, testa frågor |
| **1:45** | 15 min | Paus | ☕ Kaffe & frågor | — |
| **2:00** | 30 min | Session 03 | Multi-modell benchmarking | Jämför 3+ modeller |
| **2:30** | 30 min | Session 04 | SLM vs LLM avvägningar | Analysera prestanda/kvalitet |
| **3:00** | 30 min | Session 05-06 | Multi-agent system & routning | Utforska avancerade mönster |

**Resultat**: Deltagarna lämnar med 6 fungerande Edge AI-applikationer och produktionsklara kodmönster.

---

### 🎓 Heldagsworkshop (6 timmar)

**Perfekt för: Djupgående utbildning, bootcamps, universitetskurser**

| Tid | Varaktighet | Session | Ämnen | Aktiviteter |
|-----|-------------|---------|-------|-------------|
| **0:00** | 45 min | Setup & Teori | Miljöinstallation, Edge AI-grunder | Installera, verifiera, diskutera användningsfall |
| **0:45** | 45 min | Session 01 | Djupdykning i chattkompletteringar | Implementera grundläggande & strömmande chatt |
| **1:30** | 30 min | Paus | ☕ Kaffe & nätverkande | — |
| **2:00** | 60 min | Session 02 (Båda) | RAG-pipeline + RAGAS-utvärdering | Bygg komplett RAG-system |
| **3:00** | 30 min | Praktisk labb 1 | Anpassad RAG för din domän | Applicera på egna dokument |
| **3:30** | 30 min | Lunch | 🍽️ | — |
| **4:00** | 45 min | Session 03 | Benchmarking-metodik | Systematisk modelljämförelse |
| **4:45** | 45 min | Session 04 | Optimeringsstrategier | SLM vs LLM-analys |
| **5:30** | 60 min | Session 05-06 | Avancerad orkestrering | Multi-agent system, routning |
| **6:30** | 30 min | Praktisk labb 2 | Bygg anpassat agentsystem | Designa din egen orkestrator |

**Resultat**: Djup förståelse för Edge AI-mönster plus 2 anpassade projekt.

---

### 📚 Självstyrd inlärning (2 veckor)

**Perfekt för: Individuella elever, onlinekurser, självstudier**

#### Vecka 1: Grunder (6 timmar)

| Dag | Fokus | Varaktighet | Notebooks | Hemuppgift |
|-----|-------|-------------|-----------|------------|
| **Mån** | Setup & Grunder | 1,5 tim | Session 01 | Ändra prompts, testa strömning |
| **Ons** | RAG-grunder | 2 tim | Session 02 (båda) | Lägg till egna dokument |
| **Fre** | Benchmarking | 1,5 tim | Session 03 | Jämför ytterligare modeller |
| **Lör** | Granskning & Övning | 1 tim | Alla vecka 1 | Slutför övningar, felsök |

#### Vecka 2: Avancerat (5 timmar)

| Dag | Fokus | Varaktighet | Notebooks | Hemuppgift |
|-----|-------|-------------|-----------|------------|
| **Mån** | Optimering | 1,5 tim | Session 04 | Dokumentera avvägningar |
| **Ons** | Multi-agent system | 2 tim | Session 05 | Designa anpassade agenter |
| **Fre** | Intelligent routning | 1,5 tim | Session 06 (båda) | Bygg routningslogik |
| **Lör** | Slutprojekt | 2 tim | Integration | Kombinera flera mönster |

**Resultat**: Mästerskap i Edge AI-mönster plus portföljprojekt.

---

## 📔 Notebook-beskrivningar

### 📘 Session 01: Chatt Bootstrap
**Fil**: `session01_chat_bootstrap.ipynb`  
**Varaktighet**: 20-30 minuter  
**Förkunskaper**: Inga  
**Svårighetsgrad**: ⭐ Nybörjare

**Vad du kommer att lära dig**:
- Installera och konfigurera Foundry Local Python SDK
- Använda `FoundryLocalManager` för automatisk tjänsteupptäckt
- Implementera grundläggande chattkompletteringar med OpenAI-kompatibel API
- Bygga strömmande svar för bättre användarupplevelse
- Hantera fel och tjänsteotillgänglighet smidigt

**Nyckelkoncept**: Tjänstehantering, chattkompletteringar, strömning, felhantering

**Du kommer att bygga**: Interaktiv chattapplikation med strömmande stöd

---

### 📗 Session 02: RAG Pipeline
**Fil**: `session02_rag_pipeline.ipynb`  
**Varaktighet**: 30-45 minuter  
**Förkunskaper**: Session 01  
**Svårighetsgrad**: ⭐⭐ Mellan

**Vad du kommer att lära dig**:
- Implementera Retrieval Augmented Generation (RAG)-mönster
- Skapa vektor-inbäddningar med sentence-transformers
- Bygga semantisk sökning med cosinuslikhet
- Förankra LLM-svar i domändokument
- Hantera valfria beroenden med importskydd

**Nyckelkoncept**: RAG-arkitektur, inbäddningar, semantisk sökning, vektorsimilaritet

**Du kommer att bygga**: Dokumentförankrat fråge-svarssystem

---

### 📗 Session 02: RAG-utvärdering med RAGAS
**Fil**: `session02_rag_eval_ragas.ipynb`  
**Varaktighet**: 30-45 minuter  
**Förkunskaper**: Session 02 RAG Pipeline  
**Svårighetsgrad**: ⭐⭐ Mellan

**Vad du kommer att lära dig**:
- Utvärdera RAG-kvalitet med branschstandardmått
- Mäta kontextrelevans, svarrelevans, trovärdighet
- Använda RAGAS-ramverket för systematisk utvärdering
- Identifiera och åtgärda RAG-kvalitetsproblem
- Bygga utvärderingsdatamängder för din domän

**Nyckelkoncept**: RAG-utvärdering, RAGAS-mått, kvalitetsmätning, systematisk testning

**Du kommer att bygga**: RAG-kvalitetsutvärderingsramverk

---

### 📙 Session 03: Benchmark OSS-modeller
**Fil**: `session03_benchmark_oss_models.ipynb`  
**Varaktighet**: 30-45 minuter  
**Förkunskaper**: Session 01  
**Svårighetsgrad**: ⭐⭐ Mellan

**Vad du kommer att lära dig**:
- Systematiskt benchmarka flera modeller
- Mäta latens, genomströmning, tid för första token
- Implementera smidig nedgradering vid modellfel
- Jämföra prestanda mellan modelfamiljer
- Visualisera och analysera benchmarkresultat

**Nyckelkoncept**: Prestandabenchmarking, latensmätning, modelljämförelse, statistisk analys

**Du kommer att bygga**: Multi-modell benchmarkingsvit

---

### 📙 Session 04: Modelljämförelse (SLM vs LLM)
**Fil**: `session04_model_compare.ipynb`  
**Varaktighet**: 30-45 minuter  
**Förkunskaper**: Sessionerna 01, 03  
**Svårighetsgrad**: ⭐⭐⭐ Avancerad

**Vad du kommer att lära dig**:
- Jämföra Small Language Models mot Large Language Models
- Analysera prestanda mot kvalitetsavvägningar
- Mäta edge-lämplighetsmått
- Välja optimala modeller för distributionsbegränsningar
- Dokumentera beslutsgrunder för modellval

**Nyckelkoncept**: Modellval, avvägningsanalys, optimeringsstrategier, distributionsplanering

**Du kommer att bygga**: SLM vs LLM jämförelseramverk

---

### 📕 Session 05: Multi-agent orkestrator
**Fil**: `session05_agents_orchestrator.ipynb`  
**Varaktighet**: 45-60 minuter  
**Förkunskaper**: Sessionerna 01-02  
**Svårighetsgrad**: ⭐⭐⭐ Avancerad

**Vad du kommer att lära dig**:
- Designa specialiserade agenter för olika uppgifter
- Implementera agentminne och kontexthantering
- Bygga koordinator-mönster för agent-samarbete
- Hantera agentkommunikation och överlämningar
- Övervaka multi-agent systemprestanda

**Nyckelkoncept**: Agentarkitektur, koordinator-mönster, minneshantering, agentorkestrering

**Du kommer att bygga**: Multi-agent system med koordinator och specialister

---

### 📕 Session 06: Modellrouter
**Fil**: `session06_models_router.ipynb`  
**Varaktighet**: 30-45 minuter  
**Förkunskaper**: Sessionerna 01, 03  
**Svårighetsgrad**: ⭐⭐⭐ Avancerad

**Vad du kommer att lära dig**:
- Implementera avsiktsdetektion och mönsterigenkänning
- Bygga nyckelordsbaserad modellroutning
- Automatiskt dirigera frågor till lämpliga modeller
- Konfigurera multi-modellregister
- Övervaka routningsbeslut och prestanda

**Nyckelkoncept**: Avsiktsdetektion, modellroutning, mönsterigenkänning, intelligent val

**Du kommer att bygga**: Intelligent modellroutningssystem

---

### 📕 Session 06: Flerstegs pipeline
**Fil**: `session06_models_pipeline.ipynb`  
**Varaktighet**: 30-45 minuter  
**Förkunskaper**: Sessionerna 01, 06 Router  
**Svårighetsgrad**: ⭐⭐⭐ Avancerad

**Vad du kommer att lära dig**:
- Bygga flerstegs AI-pipelines (planera → utföra → förfina)
- Integrera router för intelligent modellval
- Implementera pipeline-felhantering och återhämtning
- Övervaka pipeline-prestanda och steg
- Designa skalbara arkitekturer för modell-som-verktyg

**Nyckelkoncept**: Pipeline-arkitektur, flerstegsbehandling, felåterhämtning, skalbarhetsmönster

**Du kommer att bygga**: En intelligent pipeline med flera steg och routing

---

## 🚀 Kom igång

### Förutsättningar

**Systemkrav**:
- **OS**: Windows 10/11, macOS 11+ eller Linux (Ubuntu 20.04+)
- **RAM**: Minst 8GB, rekommenderat 16GB+
- **Lagring**: Minst 10GB ledigt utrymme för modeller
- **Hårdvara**: CPU med AVX2; GPU (CUDA, Qualcomm NPU) valfritt

**Programvarukrav**:
- **Python 3.8+** med pip
- **Jupyter Notebook** eller **VS Code** med Jupyter-tillägg
- **Microsoft Foundry Local** installerat och konfigurerat
- **Git** (för att klona repository)

### Installationssteg

#### 1. Installera Foundry Local

**Windows**:
```cmd
winget install Microsoft.FoundryLocal
```

**macOS**:
```bash
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**Verifiera installation**:
```bash
foundry --version
```

#### 2. Ställ in Python-miljö

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

#### 3. Starta Foundry Local

```bash
# Load a model (auto-downloads if needed)
foundry model run phi-4-mini

# Verify service is running
foundry service status
```

#### 4. Starta Jupyter

```bash
# Start Jupyter Notebook
jupyter notebook notebooks/

# Or use VS Code with Jupyter extension
code notebooks/
```

### Snabb verifiering

Kör detta i en Python-cell för att verifiera installationen:

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

**Förväntat resultat**: Ett hälsningssvar från den lokala modellen.

---

## 📝 Workshopens bästa praxis

### För instruktörer

**Före workshoppen**:
- ✅ Skicka installationsinstruktioner 1 vecka i förväg
- ✅ Testa alla notebooks på målplattformen
- ✅ Förbered en felsökningsguide för vanliga problem
- ✅ Ha reservmodeller redo (phi-3.5-mini om phi-4-mini misslyckas)
- ✅ Skapa en gemensam chattkanal för frågor

**Under workshoppen**:
- ✅ Börja med en snabb miljökontroll (5 minuter)
- ✅ Dela felsökningsresurser direkt
- ✅ Uppmuntra experiment och modifieringar
- ✅ Använd pauser strategiskt (efter varje 2 sessioner)
- ✅ Ha TAs tillgängliga för individuell hjälp

**Efter workshoppen**:
- ✅ Dela kompletta fungerande notebooks och lösningar
- ✅ Tillhandahåll länkar till ytterligare resurser
- ✅ Skapa en feedbackundersökning för förbättringar
- ✅ Erbjud kontorstid för uppföljningsfrågor

### För deltagare

**Maximera din inlärning**:
- ✅ Slutför installationen innan workshoppen börjar
- ✅ Kör varje kodcell själv (läs inte bara)
- ✅ Experimentera med parametrar och prompts
- ✅ Anteckna insikter och fallgropar
- ✅ Ställ frågor när du fastnar (andra har troligen samma fråga)

**Vanliga misstag att undvika**:
- ❌ Hoppa över cellernas körningsordning (kör sekventiellt)
- ❌ Läsa felmeddelanden slarvigt
- ❌ Skynda igenom utan att förstå
- ❌ Ignorera markdown-förklaringar
- ❌ Inte spara dina modifierade notebooks

**Felsökningstips**:
1. **Tjänsten körs inte**: Kontrollera `foundry service status`
2. **Importfel**: Verifiera att den virtuella miljön är aktiverad
3. **Modell saknas**: Kör `foundry model ls` för att lista laddade modeller
4. **Långsam prestanda**: Kontrollera RAM-användning, stäng andra applikationer
5. **Oväntade resultat**: Starta om kärnan och kör alla celler från början

---

## 🔗 Ytterligare resurser

### Workshopmaterial

- **[Workshopens huvudguide](../Readme.md)** - Översikt, lärandemål, karriärresultat
- **[Python-exempel](../../../../Workshop/samples)** - Python-skript för varje session
- **[Sessionsguider](../../../../Workshop)** - Detaljerade markdown-guider (Session01-06)
- **[Skript](../../../../Workshop/scripts)** - Validerings- och testverktyg
- **[Felsökning](./TROUBLESHOOTING.md)** - Vanliga problem och lösningar
- **[Snabbstart](./quickstart.md)** - Snabbstartsguide

### Dokumentation

- **[Foundry Local Docs](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)** - Officiell Microsoft-dokumentation
- **[OpenAI Python SDK](https://github.com/openai/openai-python)** - OpenAI SDK-referens
- **[Sentence Transformers](https://www.sbert.net/)** - Dokumentation för embedding-modeller
- **[RAGAS Framework](https://docs.ragas.io/)** - RAG-utvärderingsmetrik

### Community

- **[GitHub Discussions](https://github.com/microsoft/edgeai-for-beginners/discussions)** - Ställ frågor, dela projekt
- **[Azure AI Foundry Discord](https://discord.com/invite/ByRwuEEgH4)** - Realtidsstöd från communityn
- **[Stack Overflow](https://stackoverflow.com/questions/tagged/foundry-local)** - Teknisk Q&A

---

## 🎯 Rekommenderade inlärningsvägar

### Nybörjarspår (börja här)

1. **Session 01** - Chat Bootstrap
2. **Session 02** - RAG Pipeline
3. **Session 03** - Benchmark Models

**Tid**: ~2 timmar | **Fokus**: Grundläggande mönster

---

### Mellanspår

1. Slutför nybörjarspåret
2. **Session 02** - RAG-utvärdering
3. **Session 04** - Modelljämförelse

**Tid**: ~4 timmar | **Fokus**: Kvalitet och optimering

---

### Avancerat spår (full workshop)

1. Slutför mellanspåret
2. **Session 05** - Multi-Agent Orchestrator
3. **Session 06** - Modellrouter
4. **Session 06** - Pipeline med flera steg

**Tid**: ~6 timmar | **Fokus**: Produktionsmönster

---

### Anpassat projektspår

1. Slutför nybörjarspåret (Sessioner 01-03)
2. Välj EN avancerad session baserat på ditt mål:
   - **Bygga RAG-app?** → Session 02 Utvärdering
   - **Optimera prestanda?** → Session 04 Jämförelse
   - **Komplexa arbetsflöden?** → Session 05 Orchestrator
   - **Skalbar arkitektur?** → Session 06 Router + Pipeline

**Tid**: ~3 timmar | **Fokus**: Projekt-specifika färdigheter

---

## 📊 Framgångsmått

Följ din framgång med dessa milstolpar:

- [ ] **Installation klar** - Foundry Local körs, alla beroenden installerade
- [ ] **Första chatten** - Session 01 slutförd, streamingchatten fungerar
- [ ] **RAG byggd** - Session 02 slutförd, dokument-QA-system fungerar
- [ ] **Modeller benchmarkade** - Session 03 slutförd, prestandadata insamlad
- [ ] **Avvägningar analyserade** - Session 04 slutförd, kriterier för modellval dokumenterade
- [ ] **Agenter orkestrerade** - Session 05 slutförd, multi-agent-system fungerar
- [ ] **Routing implementerad** - Session 06 slutförd, intelligent modellval fungerar
- [ ] **Anpassat projekt** - Workshopmönster tillämpade på ditt eget användningsfall

---

## 🤝 Bidra

Hittade du ett problem eller har du ett förslag? Vi välkomnar bidrag!

- **Rapportera problem**: [GitHub Issues](https://github.com/microsoft/edgeai-for-beginners/issues)
- **Föreslå förbättringar**: [GitHub Discussions](https://github.com/microsoft/edgeai-for-beginners/discussions)
- **Skicka PRs**: Följ [Bidragsriktlinjer](../../AGENTS.md)

---

## 📄 Licens

Denna workshop är en del av [EdgeAI for Beginners](https://github.com/microsoft/edgeai-for-beginners)-repositoryt och är licensierad under [MIT License](../../../../LICENSE).

---

**Redo att bygga produktionsklara Edge AI-applikationer?**  
**Börja med [Session 01: Chat Bootstrap](./session01_chat_bootstrap.ipynb) →**

---

*Senast uppdaterad: 8 oktober 2025 | Workshopversion: 2.0*

---

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, bör det noteras att automatiserade översättningar kan innehålla fel eller felaktigheter. Det ursprungliga dokumentet på dess originalspråk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.
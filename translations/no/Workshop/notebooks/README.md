# Workshop Notatbøker

> **Interaktive Jupyter Notebooks for praktisk læring om Edge AI**
>
> Progressive, selvstyrte opplæringsveiledninger som går fra grunnleggende chat-kompletteringer til avanserte multi-agent systemer ved bruk av Microsoft Foundry Local og Small Language Models.

---

## 📖 Introduksjon

Velkommen til samlingen **EdgeAI for Beginners Workshop Notebooks**. Disse interaktive Jupyter-notatbøkene gir en praktisk læringsopplevelse der du kan skrive, kjøre og eksperimentere med Edge AI-kode i sanntid.

### Hvorfor Jupyter Notebooks?

I motsetning til tradisjonelle opplæringsveiledninger tilbyr disse notatbøkene:

- **Interaktiv læring**: Kjør kodeceller og se umiddelbare resultater
- **Eksperimentering**: Endre parametere og observer endringer i sanntid
- **Dokumentasjon**: Forklaringer og markdown-celler veileder deg gjennom konseptene
- **Reproduserbarhet**: Fullstendige arbeidsklare eksempler du kan referere til og gjenbruke
- **Visualisering**: Se ytelsesmetrikker, embeddings og resultater direkte i notatboken

### Hva gjør disse notatbøkene spesielle?

Hver notatbok er designet etter **beste praksis for produksjonsklare løsninger**:

✅ **Omfattende feilhåndtering** - Smidig degradering og informative feilmeldinger  
✅ **Type hints og dokumentasjon** - Klare funksjonssignaturer og docstrings  
✅ **Ytelsesovervåking** - Sporing av tokenbruk og latensmålinger  
✅ **Modulær design** - Gjenbrukbare mønstre du kan tilpasse til dine prosjekter  
✅ **Progressiv kompleksitet** - Bygger systematisk på tidligere økter  

---

## 🎯 Læringsmål

### Kjerneferdigheter du vil utvikle

Ved å jobbe gjennom disse notatbøkene vil du mestre:

1. **Lokal AI-tjenesteadministrasjon**
   - Konfigurer og administrer Microsoft Foundry Local-tjenester
   - Velg og last inn passende modeller for maskinvaren din
   - Overvåk ressursbruk og optimaliser ytelse
   - Håndter tjenesteoppdagelse og helsesjekk

2. **Utvikling av AI-applikasjoner**
   - Implementer OpenAI-kompatible chat-kompletteringer lokalt
   - Bygg strømmingsgrensesnitt for bedre brukeropplevelse
   - Design effektive prompt for Small Language Models
   - Integrer lokale modeller i applikasjoner

3. **Retrieval Augmented Generation (RAG)**
   - Opprett semantisk søk med vektorembeddings
   - Forankre LLM-svar i domenespesifikke dokumenter
   - Evaluer RAG-kvalitet med RAGAS-metrikker
   - Skaler fra prototype til produksjon

4. **Ytelsesoptimalisering**
   - Benchmark flere modeller systematisk
   - Mål latens, gjennomstrømning og tid til første token
   - Sammenlign Small Language Models vs Large Language Models
   - Velg optimale modeller basert på ytelse/kvalitet-forhold

5. **Orkestrering av multi-agenter**
   - Design spesialiserte agenter for ulike oppgaver
   - Implementer agentminne og kontekststyring
   - Koordiner flere agenter i komplekse arbeidsflyter
   - Bygg koordinator-mønstre for agent-samarbeid

6. **Intelligent modellruting**
   - Implementer intensjonsdeteksjon og mønstergjenkjenning
   - Ruter forespørsler automatisk til passende modeller
   - Bygg flerstegs pipelines (plan → utfør → forbedre)
   - Design skalerbare arkitekturer for modell-som-verktøy

---

## 🎓 Læringsutbytte

### Hva du vil bygge

| Notatbok | Leveranse | Ferdigheter demonstrert | Vanskelighetsgrad |
|----------|-----------|-------------------------|--------------------|
| **Session 01** | Chat-app med strømming | Tjenesteoppsett, grunnleggende kompletteringer, strømming UX | ⭐ Nybegynner |
| **Session 02 (RAG)** | RAG-pipeline med evaluering | Embeddings, semantisk søk, kvalitetsmetrikker | ⭐⭐ Middels |
| **Session 02 (Eval)** | RAG-kvalitetsevaluator | RAGAS-metrikker, systematisk evaluering | ⭐⭐ Middels |
| **Session 03** | Benchmark for flere modeller | Ytelsesmåling, modell-sammenligning | ⭐⭐ Middels |
| **Session 04** | SLM vs LLM-komparator | Analyse av avveininger, optimaliseringsstrategier | ⭐⭐⭐ Avansert |
| **Session 05** | Multi-agent orkestrator | Agentdesign, minne, koordinering | ⭐⭐⭐ Avansert |
| **Session 06 (Router)** | Intelligent rutingssystem | Intensjonsdeteksjon, modellvalg | ⭐⭐⭐ Avansert |
| **Session 06 (Pipeline)** | Flerstegs pipeline | Plan/utfør/forbedre arbeidsflyter | ⭐⭐⭐ Avansert |

### Kompetanseutvikling

```
Session 01 ────► Session 02 ────► Session 03 ────► Session 04 ────► Session 05-06
   Basic            RAG             Benchmarking      Comparison      Multi-Agent
   Chat             Systems         & Performance     & Optimization  Orchestration
   
Foundation    │   Intermediate   │   Advanced       │   Expert
──────────────┴──────────────────┴──────────────────┴──────────────►
```

---

## 📅 Workshopplan

### 🚀 Halvdags workshop (3,5 timer)

**Perfekt for: Teamtrening, hackathons, konferanseworkshops**

| Tid | Varighet | Økt | Temaer | Aktiviteter |
|-----|----------|-----|--------|-------------|
| **0:00** | 30 min | Oppsett & Introduksjon | Miljøoppsett, Foundry Local-installasjon | Installer avhengigheter, verifiser oppsett |
| **0:30** | 30 min | Session 01 | Grunnleggende chat-kompletteringer, strømming | Kjør notatbok, endre prompt |
| **1:00** | 45 min | Session 02 | RAG-pipeline, embeddings, evaluering | Bygg RAG-system, test forespørsler |
| **1:45** | 15 min | Pause | ☕ Kaffe & spørsmål | — |
| **2:00** | 30 min | Session 03 | Benchmarking av flere modeller | Sammenlign 3+ modeller |
| **2:30** | 30 min | Session 04 | SLM vs LLM-avveininger | Analyser ytelse/kvalitet |
| **3:00** | 30 min | Session 05-06 | Multi-agent systemer & ruting | Utforsk avanserte mønstre |

**Resultat**: Deltakere forlater med 6 fungerende Edge AI-applikasjoner og produksjonsklare kodemønstre.

---

### 🎓 Heldags workshop (6 timer)

**Perfekt for: Grundig opplæring, bootcamps, universitetskurs**

| Tid | Varighet | Økt | Temaer | Aktiviteter |
|-----|----------|-----|--------|-------------|
| **0:00** | 45 min | Oppsett & Teori | Miljøoppsett, grunnleggende om Edge AI | Installer, verifiser, diskuter bruksområder |
| **0:45** | 45 min | Session 01 | Dypdykk i chat-kompletteringer | Implementer grunnleggende & strømmende chat |
| **1:30** | 30 min | Pause | ☕ Kaffe & nettverking | — |
| **2:00** | 60 min | Session 02 (Begge) | RAG-pipeline + RAGAS-evaluering | Bygg komplett RAG-system |
| **3:00** | 30 min | Praktisk lab 1 | Tilpasset RAG for ditt domene | Bruk på egne dokumenter |
| **3:30** | 30 min | Lunsj | 🍽️ | — |
| **4:00** | 45 min | Session 03 | Benchmarking-metodikk | Systematisk modellsammenligning |
| **4:45** | 45 min | Session 04 | Optimaliseringsstrategier | SLM vs LLM-analyse |
| **5:30** | 60 min | Session 05-06 | Avansert orkestrering | Multi-agent systemer, ruting |
| **6:30** | 30 min | Praktisk lab 2 | Bygg tilpasset agentsystem | Design din egen orkestrator |

**Resultat**: Dyp forståelse av Edge AI-mønstre pluss 2 tilpassede prosjekter.

---

### 📚 Selvstyrt læring (2 uker)

**Perfekt for: Individuelle lærere, nettkurs, selvstudium**

#### Uke 1: Grunnleggende (6 timer)

| Dag | Fokus | Varighet | Notatbøker | Hjemmelekse |
|-----|-------|----------|------------|-------------|
| **Man** | Oppsett & Grunnleggende | 1,5 t | Session 01 | Endre prompt, test strømming |
| **Ons** | RAG-grunnlag | 2 t | Session 02 (begge) | Legg til egne dokumenter |
| **Fre** | Benchmarking | 1,5 t | Session 03 | Sammenlign flere modeller |
| **Lør** | Gjennomgang & Øvelse | 1 t | Alle uke 1 | Fullfør oppgaver, feilsøk |

#### Uke 2: Avansert (5 timer)

| Dag | Fokus | Varighet | Notatbøker | Hjemmelekse |
|-----|-------|----------|------------|-------------|
| **Man** | Optimalisering | 1,5 t | Session 04 | Dokumenter avveininger |
| **Ons** | Multi-agent systemer | 2 t | Session 05 | Design tilpassede agenter |
| **Fre** | Intelligent ruting | 1,5 t | Session 06 (begge) | Bygg rutingslogikk |
| **Lør** | Sluttprosjekt | 2 t | Integrasjon | Kombiner flere mønstre |

**Resultat**: Mestring av Edge AI-mønstre pluss porteføljeprosjekt.

---

## 📔 Notatbokbeskrivelser

### 📘 Session 01: Chat Bootstrap
**Fil**: `session01_chat_bootstrap.ipynb`  
**Varighet**: 20-30 minutter  
**Forutsetninger**: Ingen  
**Vanskelighetsgrad**: ⭐ Nybegynner

**Hva du vil lære**:
- Installere og konfigurere Foundry Local Python SDK
- Bruke `FoundryLocalManager` for automatisk tjenesteoppdagelse
- Implementere grunnleggende chat-kompletteringer med OpenAI-kompatibel API
- Bygge strømmende svar for bedre brukeropplevelse
- Håndtere feil og tjenesteutilgjengelighet på en smidig måte

**Nøkkelkonsepter**: Tjenesteadministrasjon, chat-kompletteringer, strømming, feilhåndtering

**Du vil bygge**: Interaktiv chat-applikasjon med strømmestøtte

---

### 📗 Session 02: RAG Pipeline
**Fil**: `session02_rag_pipeline.ipynb`  
**Varighet**: 30-45 minutter  
**Forutsetninger**: Session 01  
**Vanskelighetsgrad**: ⭐⭐ Middels

**Hva du vil lære**:
- Implementere Retrieval Augmented Generation (RAG)-mønster
- Lage vektorembeddings med sentence-transformers
- Bygge semantisk søk med cosinus-similaritet
- Forankre LLM-svar i domene-dokumenter
- Håndtere valgfrie avhengigheter med importbeskyttelse

**Nøkkelkonsepter**: RAG-arkitektur, embeddings, semantisk søk, vektorsimilaritet

**Du vil bygge**: Dokumentforankret spørsmåls- og svarsystem

---

### 📗 Session 02: RAG Evaluering med RAGAS
**Fil**: `session02_rag_eval_ragas.ipynb`  
**Varighet**: 30-45 minutter  
**Forutsetninger**: Session 02 RAG Pipeline  
**Vanskelighetsgrad**: ⭐⭐ Middels

**Hva du vil lære**:
- Evaluere RAG-kvalitet med bransjestandardmetrikker
- Måle kontekstrelevans, svarrelevans, troverdighet
- Bruke RAGAS-rammeverket for systematisk evaluering
- Identifisere og fikse RAG-kvalitetsproblemer
- Bygge evalueringsdatasett for ditt domene

**Nøkkelkonsepter**: RAG-evaluering, RAGAS-metrikker, kvalitetsmåling, systematisk testing

**Du vil bygge**: RAG-kvalitetsevalueringsrammeverk

---

### 📙 Session 03: Benchmark OSS-modeller
**Fil**: `session03_benchmark_oss_models.ipynb`  
**Varighet**: 30-45 minutter  
**Forutsetninger**: Session 01  
**Vanskelighetsgrad**: ⭐⭐ Middels

**Hva du vil lære**:
- Systematisk benchmark av flere modeller
- Måle latens, gjennomstrømning, tid til første token
- Implementere smidig degradering ved modellfeil
- Sammenligne ytelse på tvers av modelfamilier
- Visualisere og analysere benchmark-resultater

**Nøkkelkonsepter**: Ytelsesbenchmarking, latensmåling, modellsammenligning, statistisk analyse

**Du vil bygge**: Benchmarkingsverktøy for flere modeller

---

### 📙 Session 04: Modell-sammenligning (SLM vs LLM)
**Fil**: `session04_model_compare.ipynb`  
**Varighet**: 30-45 minutter  
**Forutsetninger**: Sessions 01, 03  
**Vanskelighetsgrad**: ⭐⭐⭐ Avansert

**Hva du vil lære**:
- Sammenligne Small Language Models vs Large Language Models
- Analysere ytelse vs kvalitet-avveininger
- Måle metrikker for egnethet til edge
- Velge optimale modeller for distribusjonsbegrensninger
- Dokumentere beslutningskriterier for modellvalg

**Nøkkelkonsepter**: Modellvalg, avveiningsanalyse, optimaliseringsstrategier, distribusjonsplanlegging

**Du vil bygge**: SLM vs LLM sammenligningsrammeverk

---

### 📕 Session 05: Multi-Agent Orchestrator
**Fil**: `session05_agents_orchestrator.ipynb`  
**Varighet**: 45-60 minutter  
**Forutsetninger**: Sessions 01-02  
**Vanskelighetsgrad**: ⭐⭐⭐ Avansert

**Hva du vil lære**:
- Designe spesialiserte agenter for ulike oppgaver
- Implementere agentminne og kontekststyring
- Bygge koordinator-mønstre for agentsamarbeid
- Håndtere agentkommunikasjon og overganger
- Overvåke ytelsen til multi-agent systemer

**Nøkkelkonsepter**: Agentarkitektur, koordinator-mønstre, minnehåndtering, agentorkestrering

**Du vil bygge**: Multi-agent system med koordinator og spesialister

---

### 📕 Session 06: Modellruter
**Fil**: `session06_models_router.ipynb`  
**Varighet**: 30-45 minutter  
**Forutsetninger**: Sessions 01, 03  
**Vanskelighetsgrad**: ⭐⭐⭐ Avansert

**Hva du vil lære**:
- Implementere intensjonsdeteksjon og mønstergjenkjenning
- Bygge nøkkelordbasert modellruting
- Rute forespørsler automatisk til passende modeller
- Konfigurere multi-modellregistre
- Overvåke rutingsbeslutninger og ytelse

**Nøkkelkonsepter**: Intensjonsdeteksjon, modellruting, mønstergjenkjenning, intelligent valg

**Du vil bygge**: Intelligent modellrutingssystem

---

### 📕 Session 06: Flerstegs pipeline
**Fil**: `session06_models_pipeline.ipynb`  
**Varighet**: 30-45 minutter  
**Forutsetninger**: Sessions 01, 06 Router  
**Vanskelighetsgrad**: ⭐⭐⭐ Avansert

**Hva du vil lære**:
- Bygge flerstegs AI-pipelines (plan → utfør → forbedre)
- Integrere ruter for intelligent modellvalg
- Implementere feilhåndtering og gjenoppretting i pipeline
- Overvåke pipeline-ytelse og stadier
- Design skalerbare arkitekturer for modell-som-verktøy

**Nøkkelkonsepter**: Pipeline-arkitektur, flerstegs prosessering, feilhåndtering, skaleringsmønstre

**Du vil bygge**: Flerstegs intelligent pipeline med ruting

---

## 🚀 Komme i gang

### Forutsetninger

**Systemkrav**:
- **OS**: Windows 10/11, macOS 11+ eller Linux (Ubuntu 20.04+)
- **RAM**: Minimum 8GB, anbefalt 16GB+
- **Lagring**: 10GB+ ledig plass for modeller
- **Maskinvare**: CPU med AVX2; GPU (CUDA, Qualcomm NPU) valgfritt

**Programvarekrav**:
- **Python 3.8+** med pip
- **Jupyter Notebook** eller **VS Code** med Jupyter-utvidelse
- **Microsoft Foundry Local** installert og konfigurert
- **Git** (for å klone repository)

### Installasjonstrinn

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

**Verifiser installasjon**:
```bash
foundry --version
```

#### 2. Sett opp Python-miljø

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

### Rask verifisering

Kjør dette i en Python-celle for å verifisere oppsettet:

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

**Forventet output**: En velkomstrespons fra den lokale modellen.

---

## 📝 Beste praksis for workshop

### For instruktører

**Før workshop**:
- ✅ Send installasjonsinstruksjoner én uke i forveien
- ✅ Test alle notebooks på målmaskinvare
- ✅ Forbered feilsøkingsguide for vanlige problemer
- ✅ Ha backup-modeller klare (phi-3.5-mini hvis phi-4-mini feiler)
- ✅ Sett opp en felles chatkanal for spørsmål

**Under workshop**:
- ✅ Start med en rask miljøsjekk (5 minutter)
- ✅ Del feilsøkingsressurser umiddelbart
- ✅ Oppmuntre til eksperimentering og modifikasjoner
- ✅ Bruk pauser strategisk (etter hver 2. økt)
- ✅ Ha TAs tilgjengelig for én-til-én hjelp

**Etter workshop**:
- ✅ Del komplette fungerende notebooks og løsninger
- ✅ Gi lenker til ekstra ressurser
- ✅ Lag en tilbakemeldingsundersøkelse for forbedring
- ✅ Tilby kontortid for oppfølgingsspørsmål

### For deltakere

**Maksimer læringen din**:
- ✅ Fullfør oppsettet før workshop starter
- ✅ Kjør hver kodecelle selv (ikke bare les)
- ✅ Eksperimenter med parametere og prompts
- ✅ Ta notater om innsikter og fallgruver
- ✅ Still spørsmål når du står fast (andre har sannsynligvis samme spørsmål)

**Vanlige fallgruver å unngå**:
- ❌ Hoppe over rekkefølgen på cellekjøring (kjør sekvensielt)
- ❌ Ikke lese feilmeldinger nøye
- ❌ Rase gjennom uten å forstå
- ❌ Ignorere markdown-forklaringer
- ❌ Ikke lagre dine modifiserte notebooks

**Feilsøkingsråd**:
1. **Tjeneste ikke kjører**: Sjekk `foundry service status`
2. **Importfeil**: Verifiser at det virtuelle miljøet er aktivert
3. **Modell ikke funnet**: Kjør `foundry model ls` for å liste lastede modeller
4. **Langsom ytelse**: Sjekk RAM-bruk, lukk andre applikasjoner
5. **Uventede resultater**: Start kjernen på nytt og kjør alle celler fra toppen

---

## 🔗 Ekstra ressurser

### Workshop-materialer

- **[Workshop hovedguide](../Readme.md)** - Oversikt, læringsmål, karriereutbytte
- **[Python-eksempler](../../../../Workshop/samples)** - Tilsvarende Python-skript for hver økt
- **[Øktguider](../../../../Workshop)** - Detaljerte markdown-guider (Session01-06)
- **[Skript](../../../../Workshop/scripts)** - Validerings- og testverktøy
- **[Feilsøking](./TROUBLESHOOTING.md)** - Vanlige problemer og løsninger
- **[Hurtigstart](./quickstart.md)** - Rask guide for å komme i gang

### Dokumentasjon

- **[Foundry Local Docs](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)** - Offisiell Microsoft-dokumentasjon
- **[OpenAI Python SDK](https://github.com/openai/openai-python)** - OpenAI SDK-referanse
- **[Sentence Transformers](https://www.sbert.net/)** - Dokumentasjon for embedding-modeller
- **[RAGAS Framework](https://docs.ragas.io/)** - RAG-evalueringsmetrikker

### Fellesskap

- **[GitHub Discussions](https://github.com/microsoft/edgeai-for-beginners/discussions)** - Still spørsmål, del prosjekter
- **[Azure AI Foundry Discord](https://discord.com/invite/ByRwuEEgH4)** - Sanntidsstøtte fra fellesskapet
- **[Stack Overflow](https://stackoverflow.com/questions/tagged/foundry-local)** - Teknisk Q&A

---

## 🎯 Læringssti-anbefalinger

### Nybegynnerløp (Start her)

1. **Økt 01** - Chat Bootstrap
2. **Økt 02** - RAG Pipeline
3. **Økt 03** - Benchmark-modeller

**Tid**: ~2 timer | **Fokus**: Grunnleggende mønstre

---

### Mellomnivåløp

1. Fullfør nybegynnerløp
2. **Økt 02** - RAG Evaluering
3. **Økt 04** - Modell-sammenligning

**Tid**: ~4 timer | **Fokus**: Kvalitet og optimalisering

---

### Avansert løp (Full workshop)

1. Fullfør mellomnivåløp
2. **Økt 05** - Multi-Agent Orchestrator
3. **Økt 06** - Modellruter
4. **Økt 06** - Flerstegs pipeline

**Tid**: ~6 timer | **Fokus**: Produksjonsmønstre

---

### Tilpasset prosjektløp

1. Fullfør nybegynnerløp (Økter 01-03)
2. Velg ÉN avansert økt basert på målet ditt:
   - **Bygger RAG-app?** → Økt 02 Evaluering
   - **Optimaliserer ytelse?** → Økt 04 Sammenligning
   - **Komplekse arbeidsflyter?** → Økt 05 Orchestrator
   - **Skalerbar arkitektur?** → Økt 06 Ruter + Pipeline

**Tid**: ~3 timer | **Fokus**: Prosjektspesifikke ferdigheter

---

## 📊 Suksessmetrikker

Følg fremgangen din med disse milepælene:

- [ ] **Oppsett fullført** - Foundry Local kjører, alle avhengigheter installert
- [ ] **Første chat** - Økt 01 fullført, streaming-chat fungerer
- [ ] **RAG bygget** - Økt 02 fullført, dokument QA-system fungerer
- [ ] **Modeller benchmarket** - Økt 03 fullført, ytelsesdata samlet
- [ ] **Avveininger analysert** - Økt 04 fullført, modellvalgkriterier dokumentert
- [ ] **Agenter orkestrert** - Økt 05 fullført, multi-agent system fungerer
- [ ] **Ruting implementert** - Økt 06 fullført, intelligent modellvalg fungerer
- [ ] **Tilpasset prosjekt** - Brukt workshop-mønstre på din egen brukssak

---

## 🤝 Bidra

Har du funnet et problem eller har en idé? Vi ønsker bidrag velkommen!

- **Rapporter problemer**: [GitHub Issues](https://github.com/microsoft/edgeai-for-beginners/issues)
- **Foreslå forbedringer**: [GitHub Discussions](https://github.com/microsoft/edgeai-for-beginners/discussions)
- **Send inn PRs**: Følg [Retningslinjer for bidrag](../../AGENTS.md)

---

## 📄 Lisens

Denne workshoppen er en del av [EdgeAI for Beginners](https://github.com/microsoft/edgeai-for-beginners)-repositoryet og er lisensiert under [MIT-lisensen](../../../../LICENSE).

---

**Klar til å bygge produksjonsklare Edge AI-applikasjoner?**  
**Start med [Økt 01: Chat Bootstrap](./session01_chat_bootstrap.ipynb) →**

---

*Sist oppdatert: 8. oktober 2025 | Workshop-versjon: 2.0*

---

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi tilstreber nøyaktighet, vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
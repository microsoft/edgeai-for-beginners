# Workshop Notebooks

> **Interactieve Jupyter Notebooks voor Praktisch Leren over Edge AI**
>
> Stapsgewijze, zelfgestuurde tutorials die beginnen bij eenvoudige chatcompleties en doorgaan naar geavanceerde multi-agent systemen met Microsoft Foundry Local en Small Language Models.

---

## 📖 Introductie

Welkom bij de collectie **EdgeAI voor Beginners Workshop Notebooks**. Deze interactieve Jupyter-notebooks bieden een praktische leerervaring waarin je Edge AI-code schrijft, uitvoert en experimenteert in real-time.

### Waarom Jupyter Notebooks?

In tegenstelling tot traditionele tutorials bieden deze notebooks:

- **Interactief Leren**: Voer codecellen uit en zie directe resultaten
- **Experimenteren**: Pas parameters aan en observeer veranderingen in real-time
- **Documentatie**: Inline uitleg en markdown-cellen begeleiden je door concepten
- **Reproduceerbaarheid**: Volledige werkende voorbeelden die je kunt raadplegen en hergebruiken
- **Visualisatie**: Bekijk prestatiedata, embeddings en resultaten direct in de notebook

### Wat Maakt Deze Notebooks Uniek?

Elke notebook is ontworpen volgens **productieklaar best practices**:

✅ **Uitgebreide Foutafhandeling** - Soepele degradatie en informatieve foutmeldingen  
✅ **Type Hints & Documentatie** - Duidelijke functiesignaturen en docstrings  
✅ **Prestatiemonitoring** - Tokengebruik en latentie meten  
✅ **Modulair Ontwerp** - Herbruikbare patronen die je kunt aanpassen aan je projecten  
✅ **Progressieve Complexiteit** - Systematisch voortbouwen op eerdere sessies  

---

## 🎯 Leerdoelen

### Kernvaardigheden die je ontwikkelt

Door deze notebooks te doorlopen, beheers je:

1. **Beheer van Lokale AI-diensten**
   - Configureren en beheren van Microsoft Foundry Local-diensten
   - Geschikte modellen selecteren en laden voor je hardware
   - Resourcegebruik monitoren en prestaties optimaliseren
   - Omgaan met serviceontdekking en gezondheidschecks

2. **Ontwikkeling van AI-toepassingen**
   - Lokale OpenAI-compatibele chatcompleties implementeren
   - Streaminginterfaces bouwen voor een betere gebruikerservaring
   - Effectieve prompts ontwerpen voor Small Language Models
   - Lokale modellen integreren in toepassingen

3. **Retrieval Augmented Generation (RAG)**
   - Semantisch zoeken creëren met vector embeddings
   - LLM-antwoorden baseren op domeinspecifieke documenten
   - RAG-kwaliteit evalueren met RAGAS-metrics
   - Schalen van prototype naar productie

4. **Prestatieoptimalisatie**
   - Systematisch meerdere modellen benchmarken
   - Latentie, doorvoer en eerste-token tijd meten
   - Small Language Models vergelijken met Large Language Models
   - Optimale modellen selecteren op basis van prestatie/kwaliteitsafwegingen

5. **Multi-Agent Orchestratie**
   - Gespecialiseerde agents ontwerpen voor verschillende taken
   - Agentgeheugen en contextbeheer implementeren
   - Meerdere agents coördineren in complexe workflows
   - Coördinatorpatronen bouwen voor samenwerking tussen agents

6. **Intelligente Modelroutering**
   - Intentiedetectie en patroonherkenning implementeren
   - Vragen automatisch naar geschikte modellen routeren
   - Multi-step pipelines bouwen (plannen → uitvoeren → verfijnen)
   - Schaalbare model-als-tools architecturen ontwerpen

---

## 🎓 Leerresultaten

### Wat Je Bouwt

| Notebook | Resultaat | Vaardigheden Gedemonstreerd | Moeilijkheid |
|----------|-----------|----------------------------|--------------|
| **Sessie 01** | Chat-app met streaming | Service setup, basiscompleties, streaming UX | ⭐ Beginner |
| **Sessie 02 (RAG)** | RAG-pipeline met evaluatie | Embeddings, semantisch zoeken, kwaliteitsmetrics | ⭐⭐ Intermediate |
| **Sessie 02 (Eval)** | RAG-kwaliteitevaluator | RAGAS-metrics, systematische evaluatie | ⭐⭐ Intermediate |
| **Sessie 03** | Multi-model benchmark | Prestatiemeting, modelvergelijking | ⭐⭐ Intermediate |
| **Sessie 04** | SLM vs LLM-vergelijker | Afweginganalyse, optimalisatiestrategieën | ⭐⭐⭐ Geavanceerd |
| **Sessie 05** | Multi-agent orchestrator | Agentontwerp, geheugen, coördinatie | ⭐⭐⭐ Geavanceerd |
| **Sessie 06 (Router)** | Intelligente routeringssysteem | Intentiedetectie, modelselectie | ⭐⭐⭐ Geavanceerd |
| **Sessie 06 (Pipeline)** | Multi-step pipeline | Plannen/uitvoeren/verfijnen workflows | ⭐⭐⭐ Geavanceerd |

### Competentievoortgang

```
Session 01 ────► Session 02 ────► Session 03 ────► Session 04 ────► Session 05-06
   Basic            RAG             Benchmarking      Comparison      Multi-Agent
   Chat             Systems         & Performance     & Optimization  Orchestration
   
Foundation    │   Intermediate   │   Advanced       │   Expert
──────────────┴──────────────────┴──────────────────┴──────────────►
```

---

## 📅 Workshopplanning

### 🚀 Halve Dag Workshop (3,5 uur)

**Perfect voor: Teamtrainingssessies, hackathons, conferentieworkshops**

| Tijd | Duur | Sessie | Onderwerpen | Activiteiten |
|------|------|--------|-------------|--------------|
| **0:00** | 30 min | Setup & Intro | Omgevingssetup, Foundry Local installatie | Afhankelijkheden installeren, setup verifiëren |
| **0:30** | 30 min | Sessie 01 | Basis chatcompleties, streaming | Notebook uitvoeren, prompts aanpassen |
| **1:00** | 45 min | Sessie 02 | RAG-pipeline, embeddings, evaluatie | RAG-systeem bouwen, queries testen |
| **1:45** | 15 min | Pauze | ☕ Koffie & vragen | — |
| **2:00** | 30 min | Sessie 03 | Multi-model benchmarking | Vergelijk 3+ modellen |
| **2:30** | 30 min | Sessie 04 | SLM vs LLM afwegingen | Analyseer prestatie/kwaliteit |
| **3:00** | 30 min | Sessie 05-06 | Multi-agent systemen & routering | Verken geavanceerde patronen |

**Resultaat**: Deelnemers verlaten de workshop met 6 werkende Edge AI-toepassingen en productieklare codepatronen.

---

### 🎓 Volledige Dag Workshop (6 uur)

**Perfect voor: Diepgaande training, bootcamps, universitaire cursussen**

| Tijd | Duur | Sessie | Onderwerpen | Activiteiten |
|------|------|--------|-------------|--------------|
| **0:00** | 45 min | Setup & Theorie | Omgevingssetup, Edge AI basisprincipes | Installeren, verifiëren, use cases bespreken |
| **0:45** | 45 min | Sessie 01 | Chatcompleties diepgaand | Basis- & streamingchat implementeren |
| **1:30** | 30 min | Pauze | ☕ Koffie & netwerken | — |
| **2:00** | 60 min | Sessie 02 (Beide) | RAG-pipeline + RAGAS evaluatie | Volledig RAG-systeem bouwen |
| **3:00** | 30 min | Praktijklab 1 | Aangepaste RAG voor jouw domein | Toepassen op eigen documenten |
| **3:30** | 30 min | Lunch | 🍽️ | — |
| **4:00** | 45 min | Sessie 03 | Benchmarkmethodologie | Systematische modelvergelijking |
| **4:45** | 45 min | Sessie 04 | Optimalisatiestrategieën | SLM vs LLM analyse |
| **5:30** | 60 min | Sessie 05-06 | Geavanceerde orkestratie | Multi-agent systemen, routering |
| **6:30** | 30 min | Praktijklab 2 | Aangepast agentsysteem bouwen | Ontwerp je eigen orchestrator |

**Resultaat**: Diepgaand begrip van Edge AI-patronen plus 2 aangepaste projecten.

---

### 📚 Zelfgestuurd Leren (2 weken)

**Perfect voor: Individuele leerlingen, online cursussen, zelfstudie**

#### Week 1: Basisprincipes (6 uur)

| Dag | Focus | Duur | Notebooks | Huiswerk |
|-----|-------|------|-----------|----------|
| **Ma** | Setup & Basis | 1,5 uur | Sessie 01 | Prompts aanpassen, streaming testen |
| **Wo** | RAG Basisprincipes | 2 uur | Sessie 02 (beide) | Eigen documenten toevoegen |
| **Vr** | Benchmarking | 1,5 uur | Sessie 03 | Extra modellen vergelijken |
| **Za** | Herziening & Oefening | 1 uur | Alle Week 1 | Oefeningen voltooien, debuggen |

#### Week 2: Geavanceerd (5 uur)

| Dag | Focus | Duur | Notebooks | Huiswerk |
|-----|-------|------|-----------|----------|
| **Ma** | Optimalisatie | 1,5 uur | Sessie 04 | Afwegingen documenteren |
| **Wo** | Multi-Agent Systemen | 2 uur | Sessie 05 | Aangepaste agents ontwerpen |
| **Vr** | Intelligente Routering | 1,5 uur | Sessie 06 (beide) | Routeringslogica bouwen |
| **Za** | Eindproject | 2 uur | Integratie | Meerdere patronen combineren |

**Resultaat**: Beheersing van Edge AI-patronen plus portfolio-project.

---

## 📔 Notebookbeschrijvingen

### 📘 Sessie 01: Chat Bootstrap
**Bestand**: `session01_chat_bootstrap.ipynb`  
**Duur**: 20-30 minuten  
**Vereisten**: Geen  
**Moeilijkheid**: ⭐ Beginner

**Wat Je Leert**:
- Foundry Local Python SDK installeren en configureren
- `FoundryLocalManager` gebruiken voor automatische serviceontdekking
- Basis chatcompleties implementeren met OpenAI-compatibele API
- Streamingantwoorden bouwen voor een betere gebruikerservaring
- Fouten en onbeschikbaarheid van diensten soepel afhandelen

**Belangrijke Concepten**: Servicebeheer, chatcompleties, streaming, foutafhandeling

**Wat Je Bouwt**: Interactieve chatapplicatie met streamingondersteuning

---

### 📗 Sessie 02: RAG Pipeline
**Bestand**: `session02_rag_pipeline.ipynb`  
**Duur**: 30-45 minuten  
**Vereisten**: Sessie 01  
**Moeilijkheid**: ⭐⭐ Intermediate

**Wat Je Leert**:
- Retrieval Augmented Generation (RAG)-patroon implementeren
- Vector embeddings maken met sentence-transformers
- Semantisch zoeken bouwen met cosinusgelijkenis
- LLM-antwoorden baseren op domeindocumenten
- Optionele afhankelijkheden afhandelen met import guards

**Belangrijke Concepten**: RAG-architectuur, embeddings, semantisch zoeken, vectorgelijkenis

**Wat Je Bouwt**: Document-gebaseerd vraag-en-antwoord systeem

---

### 📗 Sessie 02: RAG Evaluatie met RAGAS
**Bestand**: `session02_rag_eval_ragas.ipynb`  
**Duur**: 30-45 minuten  
**Vereisten**: Sessie 02 RAG Pipeline  
**Moeilijkheid**: ⭐⭐ Intermediate

**Wat Je Leert**:
- RAG-kwaliteit evalueren met industriestandaard metrics
- Contextrelevantie, antwoordrelevantie, betrouwbaarheid meten
- RAGAS-framework gebruiken voor systematische evaluatie
- RAG-kwaliteitsproblemen identificeren en oplossen
- Evaluatiedatasets bouwen voor jouw domein

**Belangrijke Concepten**: RAG-evaluatie, RAGAS-metrics, kwaliteitsmeting, systematisch testen

**Wat Je Bouwt**: RAG-kwaliteitevaluatieframework

---

### 📙 Sessie 03: Benchmark OSS Modellen
**Bestand**: `session03_benchmark_oss_models.ipynb`  
**Duur**: 30-45 minuten  
**Vereisten**: Sessie 01  
**Moeilijkheid**: ⭐⭐ Intermediate

**Wat Je Leert**:
- Systematisch meerdere modellen benchmarken
- Latentie, doorvoer, eerste-token tijd meten
- Soepele degradatie implementeren bij modelfouten
- Prestaties vergelijken tussen modelfamilies
- Benchmarkresultaten visualiseren en analyseren

**Belangrijke Concepten**: Prestatiebenchmarking, latentiemeting, modelvergelijking, statistische analyse

**Wat Je Bouwt**: Multi-model benchmarkingsuite

---

### 📙 Sessie 04: Modelvergelijking (SLM vs LLM)
**Bestand**: `session04_model_compare.ipynb`  
**Duur**: 30-45 minuten  
**Vereisten**: Sessies 01, 03  
**Moeilijkheid**: ⭐⭐⭐ Geavanceerd

**Wat Je Leert**:
- Small Language Models vergelijken met Large Language Models
- Prestatie versus kwaliteit afwegingen analyseren
- Edge-geschiktheidsmetrics meten
- Optimale modellen selecteren voor implementatiebeperkingen
- Beslissingscriteria documenteren voor modelselectie

**Belangrijke Concepten**: Modelselectie, afweginganalyse, optimalisatiestrategieën, implementatieplanning

**Wat Je Bouwt**: SLM vs LLM vergelijkingsframework

---

### 📕 Sessie 05: Multi-Agent Orchestrator
**Bestand**: `session05_agents_orchestrator.ipynb`  
**Duur**: 45-60 minuten  
**Vereisten**: Sessies 01-02  
**Moeilijkheid**: ⭐⭐⭐ Geavanceerd

**Wat Je Leert**:
- Gespecialiseerde agents ontwerpen voor verschillende taken
- Agentgeheugen en contextbeheer implementeren
- Coördinatorpatronen bouwen voor samenwerking tussen agents
- Agentcommunicatie en overdrachten afhandelen
- Prestaties van multi-agent systemen monitoren

**Belangrijke Concepten**: Agentarchitectuur, coördinatorpatronen, geheugenbeheer, agentorkestratie

**Wat Je Bouwt**: Multi-agent systeem met coördinator en specialisten

---

### 📕 Sessie 06: Modelrouter
**Bestand**: `session06_models_router.ipynb`  
**Duur**: 30-45 minuten  
**Vereisten**: Sessies 01, 03  
**Moeilijkheid**: ⭐⭐⭐ Geavanceerd

**Wat Je Leert**:
- Intentiedetectie en patroonherkenning implementeren
- Keyword-gebaseerde modelroutering bouwen
- Vragen automatisch naar geschikte modellen routeren
- Multi-model registers configureren
- Routeringsbeslissingen en prestaties monitoren

**Belangrijke Concepten**: Intentiedetectie, modelroutering, patroonherkenning, intelligente selectie

**Wat Je Bouwt**: Intelligente modelrouteringssysteem

---

### 📕 Sessie 06: Multi-Step Pipeline
**Bestand**: `session06_models_pipeline.ipynb`  
**Duur**: 30-45 minuten  
**Vereisten**: Sessies 01, 06 Router  
**Moeilijkheid**: ⭐⭐⭐ Geavanceerd

**Wat Je Leert**:
- Multi-step AI-pipelines bouwen (plannen → uitvoeren → verfijnen)
- Router integreren voor intelligente modelselectie
- Pipeline foutafhandeling en herstel implementeren
- Pipeline prestaties en stadia monitoren
- Ontwerp schaalbare model-als-tools architecturen

**Belangrijke Concepten**: Pipeline-architectuur, meerstapsverwerking, foutherstel, schaalbaarheidsmodellen

**Wat je gaat bouwen**: Meerstaps intelligente pipeline met routering

---

## 🚀 Aan de slag

### Vereisten

**Systeemvereisten**:
- **OS**: Windows 10/11, macOS 11+ of Linux (Ubuntu 20.04+)
- **RAM**: Minimaal 8GB, aanbevolen 16GB+
- **Opslag**: Minimaal 10GB vrije ruimte voor modellen
- **Hardware**: CPU met AVX2; GPU (CUDA, Qualcomm NPU) optioneel

**Softwarevereisten**:
- **Python 3.8+** met pip
- **Jupyter Notebook** of **VS Code** met Jupyter-extensie
- **Microsoft Foundry Local** geïnstalleerd en geconfigureerd
- **Git** (voor het klonen van de repository)

### Installatiestappen

#### 1. Installeer Foundry Local

**Windows**:
```cmd
winget install Microsoft.FoundryLocal
```

**macOS**:
```bash
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**Installatie verifiëren**:
```bash
foundry --version
```

#### 2. Stel Python-omgeving in

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

### Snelle verificatie

Voer dit uit in een Python-cel om de installatie te verifiëren:

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

**Verwachte Uitvoer**: Een begroetingsreactie van het lokale model.

---

## 📝 Workshop Best Practices

### Voor Instructeurs

**Voor de Workshop**:
- ✅ Stuur installatie-instructies 1 week van tevoren
- ✅ Test alle notebooks op de doelhardware
- ✅ Bereid een gids voor probleemoplossing voor veelvoorkomende problemen
- ✅ Zorg voor reservekopieën van modellen (phi-3.5-mini als phi-4-mini faalt)
- ✅ Stel een gedeeld chatkanaal in voor vragen

**Tijdens de Workshop**:
- ✅ Begin met een snelle controle van de omgeving (5 minuten)
- ✅ Deel direct bronnen voor probleemoplossing
- ✅ Moedig experimenten en aanpassingen aan
- ✅ Gebruik pauzes strategisch (na elke 2 sessies)
- ✅ Zorg dat TAs beschikbaar zijn voor 1-op-1 hulp

**Na de Workshop**:
- ✅ Deel complete werkende notebooks en oplossingen
- ✅ Geef links naar aanvullende bronnen
- ✅ Maak een feedbackenquête voor verbeteringen
- ✅ Bied spreekuren aan voor vervolgvragen

### Voor Deelnemers

**Haal het meeste uit je leerervaring**:
- ✅ Voltooi de installatie vóór de start van de workshop
- ✅ Voer elke codecel zelf uit (lees niet alleen)
- ✅ Experimenteer met parameters en prompts
- ✅ Maak aantekeningen over inzichten en valkuilen
- ✅ Stel vragen als je vastloopt (anderen hebben waarschijnlijk dezelfde vraag)

**Veelvoorkomende valkuilen om te vermijden**:
- ❌ Cellen niet in volgorde uitvoeren (voer ze sequentieel uit)
- ❌ Foutmeldingen niet zorgvuldig lezen
- ❌ Te snel doorgaan zonder te begrijpen
- ❌ Markdown-uitleg negeren
- ❌ Je aangepaste notebooks niet opslaan

**Tips voor probleemoplossing**:
1. **Service niet actief**: Controleer `foundry service status`
2. **Importfouten**: Controleer of de virtuele omgeving is geactiveerd
3. **Model niet gevonden**: Voer `foundry model ls` uit om geladen modellen te bekijken
4. **Trage prestaties**: Controleer RAM-gebruik, sluit andere applicaties
5. **Onverwachte resultaten**: Herstart de kernel en voer alle cellen opnieuw uit vanaf bovenaan

---

## 🔗 Aanvullende Bronnen

### Workshopmaterialen

- **[Workshop Hoofdgids](../Readme.md)** - Overzicht, leerdoelen, carrièremogelijkheden
- **[Python Voorbeelden](../../../../Workshop/samples)** - Bijbehorende Python-scripts voor elke sessie
- **[Sessiegidsen](../../../../Workshop)** - Gedetailleerde markdown-gidsen (Session01-06)
- **[Scripts](../../../../Workshop/scripts)** - Validatie- en testhulpmiddelen
- **[Probleemoplossing](./TROUBLESHOOTING.md)** - Veelvoorkomende problemen en oplossingen
- **[Snelle Start](./quickstart.md)** - Snelle gids om te beginnen

### Documentatie

- **[Foundry Local Docs](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)** - Officiële Microsoft-documentatie
- **[OpenAI Python SDK](https://github.com/openai/openai-python)** - OpenAI SDK-referentie
- **[Sentence Transformers](https://www.sbert.net/)** - Documentatie over embedding-modellen
- **[RAGAS Framework](https://docs.ragas.io/)** - RAG-evaluatiemetrics

### Community

- **[GitHub Discussies](https://github.com/microsoft/edgeai-for-beginners/discussions)** - Stel vragen, deel projecten
- **[Azure AI Foundry Discord](https://discord.com/invite/ByRwuEEgH4)** - Real-time communityondersteuning
- **[Stack Overflow](https://stackoverflow.com/questions/tagged/foundry-local)** - Technische Q&A

---

## 🎯 Aanbevolen Leerpad

### Beginnersniveau (Start hier)

1. **Sessie 01** - Chat Bootstrap
2. **Sessie 02** - RAG Pipeline
3. **Sessie 03** - Benchmark Modellen

**Tijd**: ~2 uur | **Focus**: Basispatronen

---

### Gemiddeld Niveau

1. Voltooi Beginnersniveau
2. **Sessie 02** - RAG Evaluatie
3. **Sessie 04** - Modelvergelijking

**Tijd**: ~4 uur | **Focus**: Kwaliteit en optimalisatie

---

### Gevorderd Niveau (Volledige Workshop)

1. Voltooi Gemiddeld Niveau
2. **Sessie 05** - Multi-Agent Orchestrator
3. **Sessie 06** - Modelrouter
4. **Sessie 06** - Meerstaps Pipeline

**Tijd**: ~6 uur | **Focus**: Productiepatronen

---

### Aangepast Projectniveau

1. Voltooi Beginnersniveau (Sessies 01-03)
2. Kies ÉÉN gevorderde sessie op basis van je doel:
   - **RAG-app bouwen?** → Sessie 02 Evaluatie
   - **Prestaties optimaliseren?** → Sessie 04 Vergelijking
   - **Complexe workflows?** → Sessie 05 Orchestrator
   - **Schaalbare architectuur?** → Sessie 06 Router + Pipeline

**Tijd**: ~3 uur | **Focus**: Projectspecifieke vaardigheden

---

## 📊 Succesmetrics

Volg je voortgang met deze mijlpalen:

- [ ] **Installatie Voltooid** - Foundry Local actief, alle afhankelijkheden geïnstalleerd
- [ ] **Eerste Chat** - Sessie 01 voltooid, streaming chat werkt
- [ ] **RAG Gebouwd** - Sessie 02 voltooid, document QA-systeem functioneel
- [ ] **Modellen Gebenchmarkt** - Sessie 03 voltooid, prestatiedata verzameld
- [ ] **Afwegingen Geanalyseerd** - Sessie 04 voltooid, modelselectiecriteria gedocumenteerd
- [ ] **Agents Georkestreerd** - Sessie 05 voltooid, multi-agent systeem werkt
- [ ] **Routering Geïmplementeerd** - Sessie 06 voltooid, intelligente modelselectie functioneel
- [ ] **Aangepast Project** - Workshoppatronen toegepast op je eigen use case

---

## 🤝 Bijdragen

Een probleem gevonden of een suggestie? We verwelkomen bijdragen!

- **Problemen Melden**: [GitHub Issues](https://github.com/microsoft/edgeai-for-beginners/issues)
- **Verbeteringen Voorstellen**: [GitHub Discussies](https://github.com/microsoft/edgeai-for-beginners/discussions)
- **PRs Indienen**: Volg [Bijdrageregels](../../AGENTS.md)

---

## 📄 Licentie

Deze workshop maakt deel uit van de [EdgeAI for Beginners](https://github.com/microsoft/edgeai-for-beginners) repository en valt onder de [MIT Licentie](../../../../LICENSE).

---

**Klaar om productieklare Edge AI-toepassingen te bouwen?**  
**Begin met [Sessie 01: Chat Bootstrap](./session01_chat_bootstrap.ipynb) →**

---

*Laatst bijgewerkt: 8 oktober 2025 | Workshopversie: 2.0*

---

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
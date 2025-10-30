<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "78ca68df03ae43371b203ea43d346dec",
  "translation_date": "2025-10-30T13:00:28+00:00",
  "source_file": "CHANGELOG.md",
  "language_code": "sv"
}
-->
# Ändringslogg

Alla betydande ändringar i EdgeAI för nybörjare dokumenteras här. Projektet använder datum-baserade poster och stilen "Keep a Changelog" (Lagt till, Ändrat, Fixat, Borttaget, Dokumentation, Flyttat).

## 2025-10-30

### Lagt till - Modul06 AI-agenter omfattande förbättring
- **Microsoft Agent Framework Integration** (`Module06/01.IntroduceAgent.md`):
  - Komplett avsnitt om Microsoft Agent Framework för produktionsklar utveckling av agenter
  - Detaljerade integrationsmönster med Foundry Local för edge-distribution
  - Exempel på orkestrering av flera agenter med specialiserade SLM-modeller
  - Mönster för företagsdistribution med resursförvaltning och övervakning
  - Säkerhets- och efterlevnadsfunktioner för edge-agent-system
  - Exempel på verkliga implementeringar (detaljhandel, sjukvård, kundservice)

- **Strategier för produktionsdistribution av SLM-agenter**:
  - **Foundry Local**: Komplett dokumentation för företagsklassad edge AI-runtime med installation, konfiguration och produktionsmönster
  - **Ollama**: Förbättrad community-fokuserad distribution med omfattande övervakning och modellhantering
  - **VLLM**: Högpresterande inferensmotor med avancerade optimeringstekniker och företagsfunktioner
  - Checklistor för produktionsdistribution och jämförelsetabeller för alla tre plattformar

- **Förbättring av edge-optimerade SLM-ramverk**:
  - **ONNX Runtime**: Nytt omfattande avsnitt för plattformsoberoende SLM-agent-distribution
  - Universella distributionsmönster över Windows, Linux, macOS, iOS och Android
  - Hårdvaruaccelerationsalternativ (CPU, GPU, NPU) med automatisk detektering
  - Produktionsklara funktioner och agent-specifika optimeringar
  - Kompletta implementeringsexempel med Microsoft Agent Framework-integration

- **Referenser och vidare läsning**:
  - Omfattande resursbibliotek med 100+ auktoritativa källor
  - Grundläggande forskningsartiklar om AI-agenter och små språkmodeller
  - Officiell dokumentation för alla större ramverk och verktyg
  - Branschrapporter, marknadsanalyser och tekniska jämförelser
  - Utbildningsresurser, konferenser och community-forum
  - Standarder, specifikationer och efterlevnadsramverk

### Ändrat - Modernisering av Modul06-innehåll
- **Förbättrade lärandemål**: Lagt till Microsoft Agent Framework-mästerskap och edge-distributionsförmågor
- **Fokus på produktion**: Skiftat från konceptuell till implementeringsklar vägledning med produktions-exempel
- **Kodexempel**: Uppdaterat alla exempel för att använda moderna SDK-mönster och bästa praxis
- **Arkitekturmönster**: Lagt till hierarkiska agentarkitekturer och edge-till-moln-samordning
- **Prestandaoptimering**: Förbättrad med resursförvaltning och rekommendationer för automatisk skalning

### Dokumentation - Förbättring av Modul06-struktur
- **Omfattande täckning av agentramverk**: Från grundläggande koncept till företagsdistribution
- **Strategier för produktionsdistribution**: Kompletta guider för Foundry Local, Ollama och VLLM
- **Plattformsoberoende optimering**: Lagt till ONNX Runtime för universell distribution
- **Resursbibliotek**: Omfattande referenser för fortsatt lärande och implementering

### Lagt till - Uppdatering av dokumentation för Modul06 Model Context Protocol (MCP)
- **Modernisering av MCP-introduktion** (`Module06/03.IntroduceMCP.md`):
  - Uppdaterad med senaste MCP-specifikationer från modelcontextprotocol.io (version 2025-06-18)
  - Lagt till officiell USB-C-analog för standardiserade AI-applikationsanslutningar
  - Uppdaterat arkitekturavsnitt med officiell tvålagersdesign (Datalager + Transportlager)
  - Förbättrad dokumentation av kärnprimitiver med serverprimitiver (Verktyg, Resurser, Uppmaningar) och klientprimitiver (Sampling, Elicitering, Loggning)

- **Omfattande MCP-referenser och resurser**:
  - Lagt till **MCP för nybörjare**-länk (https://aka.ms/mcp-for-beginners)
  - Officiell MCP-dokumentation och specifikationer (modelcontextprotocol.io)
  - Utvecklingsresurser inklusive MCP Inspector och referensimplementeringar
  - Tekniska standarder (JSON-RPC 2.0, JSON Schema, OpenAPI, Server-Sent Events)

### Lagt till - Modul04 Qualcomm QNN Integration
- **Nytt avsnitt 7: Qualcomm QNN Optimeringssvit** (`Module04/05.QualcommQNN.md`):
  - Omfattande 400+ raders guide som täcker Qualcomms enhetliga AI-inferensramverk
  - Detaljerad täckning av heterogen databehandling (Hexagon NPU, Adreno GPU, Kryo CPU)
  - Hårdvaru-medveten optimering för Snapdragon-plattformar med intelligent arbetsfördelning
  - Avancerade kvantiseringstekniker (INT8, INT16, blandad precision) för mobil distribution
  - Strömeffektiv inferensoptimering för batteridrivna enheter och realtidsapplikationer
  - Komplett installationsguide med QNN SDK-uppsättning och miljökonfiguration
  - Praktiska exempel: PyTorch till QNN-konvertering, multi-backend-optimering, kontextbinär generering
  - Avancerade användningsmönster: anpassad backend-konfiguration, dynamisk kvantisering, prestandaprofilering
  - Omfattande felsökningsavsnitt och community-resurser

- **Förbättrad Modul04-struktur**:
  - Uppdaterad README.md för att inkludera 7 progressiva avsnitt (tidigare 6)
  - Lagt till Qualcomm QNN i prestandajämförelsetabellen (5-15x hastighetsförbättring, 50-80% minnesreduktion)
  - Omfattande lärandemål för mobil AI-distribution och strömeffektivisering

### Ändrat - Uppdateringar av Modul04-dokumentation
- **Förbättring av Microsoft Olive-dokumentation** (`Module04/03.MicrosoftOlive.md`):
  - Lagt till omfattande avsnitt "Olive Recipes Repository" som täcker 100+ förbyggda optimeringsrecept
  - Detaljerad täckning av stödda modelfamiljer (Phi, Llama, Qwen, Gemma, Mistral, DeepSeek)
  - Praktiska användningsexempel för receptanpassning och community-bidrag
  - Förbättrad med prestandajämförelser och integrationsvägledning

- **Omordning av avsnitt i Modul04**:
  - Apple MLX flyttad till avsnitt 5 (tidigare avsnitt 6)
  - Workflow Synthesis flyttad till avsnitt 6 (tidigare avsnitt 7)  
  - Qualcomm QNN placerad som avsnitt 7 (specialiserat på mobil/edge-fokus)
  - Uppdaterat alla filreferenser och navigeringslänkar därefter

### Fixat - Validering av workshop-exempel
- **chat_bootstrap.py validering och reparation**:
  - Fixade korrupt import-sats (`util.util.workshop_utils` → `util.workshop_utils`)
  - Skapade saknad `__init__.py` i util-paketet för korrekt Python-modulupplösning
  - Installerade nödvändiga beroenden (openai, foundry-local-sdk) i conda-miljön
  - Lyckades validera exempelutförande med både standard- och anpassade uppmaningar
  - Bekräftade integration med Foundry Local-tjänsten och modellinläsning (phi-4-mini med CUDA-optimering)

### Dokumentation - Omfattande guideuppdateringar
- **Komplett omstrukturering av Modul04 README.md**:
  - Lagt till Qualcomm QNN som ett stort optimeringsramverk tillsammans med OpenVINO, Olive, MLX
  - Uppdaterat kapitelmål för att inkludera mobil AI-distribution och strömeffektivisering
  - Förbättrad prestandajämförelsetabell med QNN-mått och mobil/edge-användningsfall
  - Bibehållen logisk progression från företagslösningar till plattformsspecifika optimeringar

- **Korsreferenser och navigering**:
  - Uppdaterat alla interna länkar och filreferenser för ny avsnittsnumrering
  - Förbättrad beskrivning av workflow synthesis för att inkludera mobil-, desktop- och molnmiljöer
  - Lagt till omfattande resurslänkar för Qualcomms utvecklarekosystem

## 2025-10-08

### Lagt till - Omfattande workshop-uppdatering
- **Workshop README.md komplett omskriven**:
  - Lagt till omfattande introduktion som förklarar Edge AI:s värde (integritet, prestanda, kostnad)
  - Skapat 6 kärnlärandemål med detaljerade kompetenser
  - Lagt till tabell över lärandemål med leveranser och kompetensmatris
  - Inkluderat avsnitt om karriärklara färdigheter för branschrelevans
  - Lagt till snabbstartsguide med förutsättningar och 3-stegs installation
  - Skapat resurstabeller för Python-exempel (8 filer med körtider)
  - Lagt till tabell för Jupyter-notebooks (8 notebooks med svårighetsgrader)
  - Skapat dokumentationstabell (7 viktiga dokument med "Använd när"-vägledning)
  - Lagt till rekommendationer för lärandebanor för olika kompetensnivåer

- **Validerings- och testinfrastruktur för workshop**:
  - Skapat `scripts/validate_samples.py` - Omfattande valideringsverktyg för syntax, import och bästa praxis
  - Skapat `scripts/test_samples.py` - Verktyg för snabbtest av alla Python-exempel
  - Lagt till valideringsdokumentation till `scripts/README.md`

- **Omfattande dokumentation**:
  - Skapat `SAMPLES_UPDATE_SUMMARY.md` - 400+ raders detaljerad guide som täcker alla förbättringar
  - Skapat `UPDATE_COMPLETE.md` - Sammanfattning av uppdateringens slutförande
  - Skapat `QUICK_REFERENCE.md` - Snabbreferenskort för workshop

### Ändrat - Modernisering av Python-exempel i workshop
- **Alla 8 Python-exempel uppdaterade med bästa praxis**:
  - Förbättrad felhantering med try-except-block runt alla I/O-operationer
  - Lagt till typanvisningar och omfattande docstrings
  - Implementerat konsekvent [INFO]/[ERROR]/[RESULT]-loggningsmönster
  - Skyddat valfria import med installationsanvisningar
  - Förbättrad användarfeedback i alla exempel

- **session01/chat_bootstrap.py**:
  - Förbättrad klientinitialisering med omfattande felmeddelanden
  - Förbättrad felhantering vid strömning med validering av data
  - Lagt till bättre undantagshantering för tjänsteotillgänglighet

- **session02/rag_pipeline.py**:
  - Lagt till importskydd för sentence-transformers med installationsanvisningar
  - Förbättrad felhantering för embedding- och genereringsoperationer
  - Förbättrad utdataformatering med strukturerade resultat

- **session02/rag_eval_ragas.py**:
  - Skyddat valfria import (ragas, datasets) med användarvänliga felmeddelanden
  - Lagt till felhantering för utvärderingsmått
  - Förbättrad utdataformatering för utvärderingsresultat

- **session03/benchmark_oss_models.py**:
  - Implementerat graciös nedbrytning (fortsätter vid modellfel)
  - Lagt till detaljerad framstegsrapportering och felhantering per modell
  - Förbättrad statistikberäkning med omfattande felåterhämtning

- **session04/model_compare.py**:
  - Lagt till typanvisningar (Tuple-returtyper)
  - Förbättrad utdataformatering med strukturerade JSON-resultat
  - Implementerat felhantering per modell med återhämtning

- **session05/agents_orchestrator.py**:
  - Förbättrad Agent.act() med omfattande docstrings
  - Lagt till pipeline-felhantering med steg-för-steg-loggning
  - Förbättrad minneshantering och spårning av tillstånd

- **session06/models_router.py**:
  - Förbättrad funktionsdokumentation för alla routing-komponenter
  - Lagt till detaljerad loggning i route()-funktionen
  - Förbättrad testutdata med strukturerade resultat

- **session06/models_pipeline.py**:
  - Lagt till felhantering i chat()-hjälpfunktionen
  - Förbättrad pipeline() med stegloggning och framstegsrapportering
  - Förbättrad main() med omfattande felåterhämtning

### Dokumentation - Förbättring av workshop-dokumentation
- Uppdaterad huvud-README.md med workshop-sektion som lyfter fram praktisk lärandebana
- Förbättrad STUDY_GUIDE.md med omfattande workshop-sektion inklusive:
  - Lärandemål och fokusområden för studier
  - Självbedömningsfrågor
  - Praktiska övningar med tidsuppskattningar
  - Tidsallokering för koncentrerade och deltidsstudier
  - Lagt till workshop i mall för framstegsspårning
- Uppdaterad tidsallokering från 20 timmar till 30 timmar (inklusive workshop)
- Lagt till beskrivningar av workshop-exempel och lärandemål i README

### Fixat
- Löste inkonsekventa felhanteringsmönster i workshop-exempel
- Fixade valfria beroendeimportfel med korrekta skydd
- Korrigerade saknade typanvisningar i kritiska funktioner
- Åtgärdade otillräcklig användarfeedback i felscenarier
- Fixade valideringsproblem med omfattande testinfrastruktur

---

## 2025-09-23

### Ändrat - Större modernisering av Modul 08
- **Omfattande anpassning till Microsoft Foundry-Local-repositoriemönster**
  - Uppdaterade alla kodexempel för att använda moderna `FoundryLocalManager` och OpenAI SDK-integration
  - Ersatte föråldrade manuella `requests`-anrop med korrekt SDK-användning
  - Anpassade implementeringsmönster till officiell Microsoft-dokumentation och exempel

- **05.AIPoweredAgents.md modernisering**:
  - Uppdaterade orkestrering av flera agenter för att använda moderna SDK-mönster
  - Förbättrad koordinatorimplementering med avancerade funktioner (feedback-loopar, prestandaövervakning)
  - Lagt till omfattande felhantering och kontroll av tjänstehälsa
  - Integrerade korrekta referenser till lokala exempel (`samples/05/multi_agent_orchestration.ipynb`)
  - Uppdaterade funktionsanropsexempel för att använda moderna `tools`-parametrar istället för föråldrade `functions`
  - Lagt till produktionsklara mönster med övervakning och statistikspårning

- **06.ModelsAsTools.md komplett omskriven**:
  - Ersatte grundläggande verktygsregister med intelligent modellrouter-implementering
  - Lagt till nyckelordsbaserad modellval för olika uppgiftstyper (allmän, resonemang, kod, kreativ)
  - Integrerade miljöbaserad konfiguration med flexibel modelltilldelning
  - Förbättrad med omfattande övervakning av tjänstehälsa och felhantering
  - Lagt till produktionsdistributionsmönster med begäranövervakning och prestandaspårning
  - Anpassad till lokal implementering i `samples/06/router.py` och `samples/06/model_router.ipynb`

- **Förbättringar av dokumentationsstruktur**:
  - Lagt till översiktsavsnitt som lyfter fram modernisering och SDK-anpassning
  - Förbättrad med emojis och bättre formatering för förbättrad läsbarhet
  - Lagt till korrekta referenser till lokala exempel genom hela dokumentationen
  - Inkluderat produktionsklara implementeringsvägledningar och bästa praxis

### Lagt till
- Omfattande översiktsavsnitt i Modul 08-filer som lyfter fram modern SDK-integration
- Arkitekturhöjdpunkter som visar avancerade funktioner (system med flera agenter, intelligent routing)
- Direkta referenser till lokala exempel för praktisk erfarenhet
- Vägledning för produktionsdistribution med övervakning och felhanteringsmönster
- Interaktiva Jupyter-notebook-exempel med avancerade funktioner och jämförelser

### Fixat
- Discrepanser mellan dokumentation och faktiska exempelimplementeringar
- Föråldrade SDK-användningsmönster genom hela
  - Körbara exempel under `Module08/samples/01`–`06` med Windows cmd-instruktioner
    - `01` REST snabbchatt (`chat_quickstart.py`)
    - `02` SDK snabbstart med OpenAI/Foundry Local och Azure OpenAI-stöd (`sdk_quickstart.py`)
    - `03` CLI lista-och-test (`list_and_bench.cmd`)
    - `04` Chainlit-demo (`app.py`)
    - `05` Multi-agent orkestrering (`python -m samples.05.agents.coordinator`)
    - `06` Models-as-Tools router (`router.py`)
- Azure OpenAI-stöd i Session 2 SDK-exempel med konfiguration av miljövariabler
- `.vscode/settings.json` pekar på `Module08/.venv` för att förbättra Python-analysupplösning
- `.env` med `PYTHONPATH`-hint för att underlätta medvetenhet i VS Code/Pylance

### Ändrat
- Standardmodell uppdaterad till `phi-4-mini` i hela Module 08-dokumentationen och exempel; kvarvarande omnämnanden av `phi-3.5` inom Module 08 har tagits bort
- Förbättringar i router (`Module08/samples/06/router.py`):
  - Upptäckt av slutpunkter via `foundry service status` med regex-parsing
  - Hälsokontroll av `/v1/models` vid start
  - Miljökonfigurerbart modellregister (`GENERAL_MODEL`, `REASONING_MODEL`, `CODE_MODEL`, `TOOL_REGISTRY` JSON)
- Krav uppdaterade: `Module08/requirements.txt` inkluderar nu `openai` (tillsammans med `requests`, `chainlit`)
- Förtydligad vägledning för Chainlit-exempel och felsökningsstöd; importupplösning via arbetsytans inställningar

### Fixat
- Lösta importproblem:
  - Router är inte längre beroende av en icke-existerande `utils`-modul; funktioner är inlinade
  - Koordinator använder relativ import (`from .specialists import ...`) och anropas via modulväg
  - VS Code/Pylance-konfiguration för att lösa `chainlit` och paketimporter
- Rättat mindre stavfel i `STUDY_GUIDE.md` och lagt till täckning för Module 08

### Borttaget
- Raderat oanvänd `Module08/infra/obs.py` och tagit bort den tomma `infra/`-katalogen; observabilitetsmönster behålls som valfria i dokumentationen

### Flyttat
- Konsoliderat Module 08-demonstrationer under `Module08/samples` med sessionsnumrerade mappar
  - Flyttat Chainlit-app till `samples/04`
  - Flyttat agenter till `samples/05` och lagt till `__init__.py`-filer för paketupplösning

### Dokumentation
- Dokumentation för Module 08-sessioner och alla exempel-README-filer har berikats med referenser till Microsoft Learn och betrodda leverantörer
- `Module08/README.md` uppdaterad med översikt över exempel, routerkonfiguration och valideringstips
- `Module07/README.md` Windows Foundry Local-sektion validerad mot Learn-dokumentation
- `STUDY_GUIDE.md` uppdaterad:
  - Lagt till Module 08 i översikt, scheman, framstegsspårare
  - Lagt till omfattande referensavsnitt (Foundry Local, Azure AI, Olive, ONNX Runtime, OpenVINO, MLX, Llama.cpp, vLLM, Ollama, AI Toolkit, Windows ML)

---

## Historiskt (sammanfattning)
- Kursarkitektur och moduler etablerade (Moduler 01–07)
- Iterativ modernisering av innehåll, standardisering av format och tillägg av fallstudier
- Utökad täckning av optimeringsramverk (Llama.cpp, Olive, OpenVINO, Apple MLX)

## Ej släppt / Backlog (förslag)
- Valfria röktester per exempel för att validera Foundry Local tillgänglighet
- Granska översättningar för att anpassa modellreferenser (t.ex. `phi-4-mini`) där det är lämpligt
- Lägg till minimal pyright-konfiguration om team föredrar strikthet över hela arbetsytan

---

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, bör det noteras att automatiserade översättningar kan innehålla fel eller felaktigheter. Det ursprungliga dokumentet på dess ursprungliga språk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.
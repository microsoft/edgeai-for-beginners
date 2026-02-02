# Ændringslog

Alle væsentlige ændringer i EdgeAI for Beginners er dokumenteret her. Dette projekt bruger dato-baserede indgange og Keep a Changelog-stilen (Tilføjet, Ændret, Rettet, Fjernet, Dokumentation, Flyttet).

## 2025-10-30

### Tilføjet - Modul06 AI-agenter omfattende forbedring
- **Microsoft Agent Framework Integration** (`Module06/01.IntroduceAgent.md`):
  - Komplet sektion om Microsoft Agent Framework til produktionsklare agentudvikling
  - Detaljerede integrationsmønstre med Foundry Local til edge-implementering
  - Eksempler på multi-agent orkestrering med specialiserede SLM-modeller
  - Implementeringsmønstre for virksomheder med ressourcehåndtering og overvågning
  - Sikkerheds- og compliance-funktioner til edge-agent-systemer
  - Eksempler fra virkeligheden (detailhandel, sundhedspleje, kundeservice)

- **Produktionsstrategier for SLM-agent implementering**:
  - **Foundry Local**: Komplet dokumentation for enterprise-grade edge AI runtime med installation, konfiguration og produktionsmønstre
  - **Ollama**: Forbedret community-fokuseret implementering med omfattende overvågning og modelhåndtering
  - **VLLM**: Højtydende inferensmotor med avancerede optimeringsteknikker og funktioner til virksomheder
  - Tjeklister for produktionsimplementering og sammenligningstabeller for alle tre platforme

- **Forbedring af edge-optimerede SLM-rammer**:
  - **ONNX Runtime**: Ny omfattende sektion for cross-platform SLM-agent implementering
  - Universelle implementeringsmønstre på tværs af Windows, Linux, macOS, iOS og Android
  - Hardware-accelerationsmuligheder (CPU, GPU, NPU) med automatisk detektion
  - Produktionsklare funktioner og agent-specifikke optimeringer
  - Komplette implementeringseksempler med Microsoft Agent Framework integration

- **Referencer og yderligere læsning**:
  - Omfattende ressourcebibliotek med 100+ autoritative kilder
  - Centrale forskningsartikler om AI-agenter og Small Language Models
  - Officiel dokumentation for alle større rammer og værktøjer
  - Industri-rapporter, markedsanalyser og tekniske benchmarks
  - Uddannelsesressourcer, konferencer og community-fora
  - Standarder, specifikationer og compliance-rammer

### Ændret - Modul06 Indhold Modernisering
- **Forbedrede læringsmål**: Tilføjet Microsoft Agent Framework færdigheder og edge-implementeringskapaciteter
- **Produktionsfokus**: Skiftet fra konceptuelt til implementeringsklar vejledning med produktions-eksempler
- **Kodeeksempler**: Opdateret alle eksempler til at bruge moderne SDK-mønstre og bedste praksis
- **Arkitekturmønstre**: Tilføjet hierarkiske agent-arkitekturer og edge-to-cloud koordinering
- **Ydelsesoptimering**: Forbedret med ressourcehåndtering og anbefalinger til auto-skalering

### Dokumentation - Modul06 Strukturforbedring
- **Omfattende dækning af Agent Framework**: Fra grundlæggende begreber til virksomhedsimplementering
- **Produktionsimplementeringsstrategier**: Komplette vejledninger til Foundry Local, Ollama og VLLM
- **Cross-platform optimering**: Tilføjet ONNX Runtime til universel implementering
- **Ressourcebibliotek**: Omfattende referencer til fortsat læring og implementering

### Tilføjet - Modul06 Model Context Protocol (MCP) Dokumentationsopdatering
- **MCP Introduktion Modernisering** (`Module06/03.IntroduceMCP.md`):
  - Opdateret med de nyeste MCP-specifikationer fra modelcontextprotocol.io (2025-06-18 version)
  - Tilføjet officiel USB-C analogi for standardiserede AI-applikationsforbindelser
  - Opdateret arkitektursektion med officiel to-lags design (Data Layer + Transport Layer)
  - Forbedret dokumentation af kerneprimitiver med serverprimitiver (Tools, Resources, Prompts) og klientprimitiver (Sampling, Elicitation, Logging)

- **Omfattende MCP-referencer og ressourcer**:
  - Tilføjet **MCP for Beginners** link (https://aka.ms/mcp-for-beginners)
  - Officiel MCP-dokumentation og specifikationer (modelcontextprotocol.io)
  - Udviklingsressourcer inklusive MCP Inspector og referenceimplementeringer
  - Tekniske standarder (JSON-RPC 2.0, JSON Schema, OpenAPI, Server-Sent Events)

### Tilføjet - Modul04 Qualcomm QNN Integration
- **Ny Sektion 7: Qualcomm QNN Optimeringssuite** (`Module04/05.QualcommQNN.md`):
  - Omfattende 400+ linjers guide, der dækker Qualcomms samlede AI-inferensramme
  - Detaljeret dækning af heterogen computing (Hexagon NPU, Adreno GPU, Kryo CPU)
  - Hardware-bevidst optimering for Snapdragon-platforme med intelligent arbejdsfordeling
  - Avancerede kvantiseringsteknikker (INT8, INT16, blandet præcision) til mobilimplementering
  - Strømbesparende inferensoptimering til batteridrevne enheder og realtidsapplikationer
  - Komplet installationsguide med QNN SDK-opsætning og miljøkonfiguration
  - Praktiske eksempler: PyTorch til QNN-konvertering, multi-backend optimering, kontekst-binær generering
  - Avancerede brugsmønstre: tilpasset backend-konfiguration, dynamisk kvantisering, ydelsesprofilering
  - Omfattende fejlfindingsektion og community-ressourcer

- **Forbedret Modul04 struktur**:
  - Opdateret README.md til at inkludere 7 progressive sektioner (tidligere 6)
  - Tilføjet Qualcomm QNN til performance benchmarks tabel (5-15x hastighedsforbedring, 50-80% hukommelsesreduktion)
  - Omfattende læringsmål for mobil AI-implementering og strømbesparelse

### Ændret - Modul04 Dokumentationsopdateringer
- **Microsoft Olive dokumentationsforbedring** (`Module04/03.MicrosoftOlive.md`):
  - Tilføjet omfattende "Olive Recipes Repository" sektion, der dækker 100+ forudbyggede optimeringsopskrifter
  - Detaljeret dækning af understøttede modelfamilier (Phi, Llama, Qwen, Gemma, Mistral, DeepSeek)
  - Praktiske brugseksempler til opskriftstilpasning og community-bidrag
  - Forbedret med ydelsesbenchmarks og integrationsvejledning

- **Sektion omorganisering i Modul04**:
  - Apple MLX flyttet til Sektion 5 (tidligere Sektion 6)
  - Workflow Synthesis flyttet til Sektion 6 (tidligere Sektion 7)
  - Qualcomm QNN positioneret som Sektion 7 (specialiseret mobil/edge fokus)
  - Opdateret alle filreferencer og navigationslinks tilsvarende

### Rettet - Workshop Eksempelvalidering
- **chat_bootstrap.py validering og reparation**:
  - Rettet korrupt import statement (`util.util.workshop_utils` → `util.workshop_utils`)
  - Oprettet manglende `__init__.py` i util-pakken for korrekt Python-modulopløsning
  - Installeret nødvendige afhængigheder (openai, foundry-local-sdk) i conda-miljø
  - Valideret prøveeksekvering med både standard og tilpassede prompts
  - Bekræftet integration med Foundry Local service og modellæsning (phi-4-mini med CUDA-optimering)

### Dokumentation - Omfattende Guideopdateringer
- **Module04 README.md komplet omstrukturering**:
  - Tilføjet Qualcomm QNN som større optimeringsramme sammen med OpenVINO, Olive, MLX
  - Opdateret kapitlets læringsmål til at inkludere mobil AI-implementering og strømbesparelse
  - Forbedret performance sammenligningstabel med QNN-metrics og mobil/edge anvendelsessager
  - Beholdt logisk progression fra virksomhedsløsninger til platform-specifikke optimeringer

- **Krydsreferencer og navigation**:
  - Opdateret alle interne links og filreferencer for ny sektionsnummerering
  - Forbedret workflow synthesis beskrivelse til at inkludere mobil-, desktop- og cloud-miljøer
  - Tilføjet omfattende ressource-links til Qualcomm udviklerøkosystem

## 2025-10-08

### Tilføjet - Workshop Omfattende Opdatering
- **Workshop README.md komplet omskrivning**:
  - Tilføjet omfattende introduktion, der forklarer Edge AI's værdi (privatliv, ydeevne, omkostninger)
  - Oprettet 6 kerne-læringsmål med detaljerede kompetencer
  - Tilføjet læringsmålstabel med leverancer og kompetencematrix
  - Inkluderet karriereklare færdigheder sektion for industri-relevans
  - Tilføjet hurtig start guide med forudsætninger og 3-trins opsætning
  - Oprettet ressource-tabeller for Python-eksempler (8 filer med køretider)
  - Tilføjet Jupyter notebooks tabel (8 notebooks med sværhedsgrader)
  - Oprettet dokumentationstabel (7 nøgle-dokumenter med "Brug Når" vejledning)
  - Tilføjet læringssti anbefalinger for forskellige færdighedsniveauer

- **Workshop validerings- og testinfrastruktur**:
  - Oprettet `scripts/validate_samples.py` - Omfattende valideringsværktøj til syntaks, imports og bedste praksis
  - Oprettet `scripts/test_samples.py` - Smoke test runner for alle Python-eksempler
  - Tilføjet valideringsdokumentation til `scripts/README.md`

- **Omfattende dokumentation**:
  - Oprettet `SAMPLES_UPDATE_SUMMARY.md` - 400+ linjers detaljeret guide, der dækker alle forbedringer
  - Oprettet `UPDATE_COMPLETE.md` - Executive summary af opdateringsfærdiggørelse
  - Oprettet `QUICK_REFERENCE.md` - Hurtig referencekort til Workshop

### Ændret - Workshop Python Eksempel Modernisering
- **Alle 8 Python-eksempler opdateret med bedste praksis**:
  - Forbedret fejlbehandling med try-except blokke omkring alle I/O-operationer
  - Tilføjet type hints og omfattende docstrings
  - Implementeret konsistent [INFO]/[ERROR]/[RESULT] logningsmønster
  - Beskyttet valgfrie imports med installationshint
  - Forbedret brugerfeedback i alle eksempler

- **session01/chat_bootstrap.py**:
  - Forbedret klientinitialisering med omfattende fejlmeddelelser
  - Forbedret streaming fejlbehandling med chunk-validering
  - Tilføjet bedre undtagelseshåndtering for service utilgængelighed

- **session02/rag_pipeline.py**:
  - Tilføjet import guards for sentence-transformers med installationshint
  - Forbedret fejlbehandling for embedding og genereringsoperationer
  - Forbedret outputformatering med strukturerede resultater

- **session02/rag_eval_ragas.py**:
  - Beskyttet valgfrie imports (ragas, datasets) med brugervenlige fejlmeddelelser
  - Tilføjet fejlbehandling for evalueringsmetrikker
  - Forbedret outputformatering for evalueringsresultater

- **session03/benchmark_oss_models.py**:
  - Implementeret graceful degradation (fortsætter ved model-fejl)
  - Tilføjet detaljeret fremdriftsrapportering og per-model fejlbehandling
  - Forbedret statistikberegning med omfattende fejlgenopretning

- **session04/model_compare.py**:
  - Tilføjet type hints (Tuple returtyper)
  - Forbedret outputformatering med strukturerede JSON-resultater
  - Implementeret per-model fejlbehandling med genopretning

- **session05/agents_orchestrator.py**:
  - Forbedret Agent.act() med omfattende docstrings
  - Tilføjet pipeline fejlbehandling med trin-for-trin logning
  - Forbedret hukommelsesstyring og tilstandssporing

- **session06/models_router.py**:
  - Forbedret funktionsdokumentation for alle routing-komponenter
  - Tilføjet detaljeret logning i route() funktionen
  - Forbedret testoutput med strukturerede resultater

- **session06/models_pipeline.py**:
  - Tilføjet fejlbehandling til chat() hjælpefunktion
  - Forbedret pipeline() med trinlogning og fremdriftsrapportering
  - Forbedret main() med omfattende fejlgenopretning

### Dokumentation - Workshop Dokumentationsforbedring
- Opdateret hoved-README.md med Workshop sektion, der fremhæver hands-on læringssti
- Forbedret STUDY_GUIDE.md med omfattende Workshop sektion inklusive:
  - Læringsmål og fokusområder
  - Selv-evalueringsspørgsmål
  - Praktiske øvelser med tidsestimater
  - Tidsallokering for koncentreret og deltidsstudie
  - Tilføjet Workshop til fremskridtssporingsskabelon
- Opdateret tidsallokeringsguide fra 20 timer til 30 timer (inklusive Workshop)
- Tilføjet Workshop eksempelbeskrivelser og læringsmål til README

### Rettet
- Løst inkonsistente fejlbehandlingsmønstre på tværs af Workshop-eksempler
- Rettet fejl i valgfrie afhængighedsimporter med korrekte guards
- Korrigeret manglende type hints i kritiske funktioner
- Adresseret utilstrækkelig brugerfeedback i fejlscenarier
- Rettet valideringsproblemer med omfattende testinfrastruktur

---

## 2025-09-23

### Ændret - Større Modul08 Modernisering
- **Omfattende tilpasning til Microsoft Foundry-Local repository-mønstre**
  - Opdateret alle kodeeksempler til at bruge moderne `FoundryLocalManager` og OpenAI SDK integration
  - Erstattet forældede manuelle `requests` kald med korrekt SDK-brug
  - Tilpasset implementeringsmønstre med officiel Microsoft dokumentation og eksempler

- **05.AIPoweredAgents.md modernisering**:
  - Opdateret multi-agent orkestrering til at bruge moderne SDK-mønstre
  - Forbedret koordinatorimplementering med avancerede funktioner (feedback loops, performance monitoring)
  - Tilføjet omfattende fejlbehandling og service sundhedstjek
  - Integreret korrekte referencer til lokale eksempler (`samples/05/multi_agent_orchestration.ipynb`)
  - Opdateret funktionskaldseksempler til at bruge moderne `tools` parameter i stedet for forældede `functions`
  - Tilføjet produktionsklare mønstre med overvågning og statistiksporing

- **06.ModelsAsTools.md komplet omskrivning**:
  - Erstattet grundlæggende værktøjsregister med intelligent model-router implementering
  - Tilføjet nøgleordsbaseret modelvalg til forskellige opgavetyper (generel, ræsonnement, kode, kreativ)
  - Integreret miljøbaseret konfiguration med fleksibel modeltildeling
  - Forbedret med omfattende service sundhedsovervågning og fejlbehandling
  - Tilføjet produktionsimplementeringsmønstre med anmodningsovervågning og ydelsessporing
  - Tilpasset lokal implementering i `samples/06/router.py` og `samples/06/model_router.ipynb`

- **Dokumentationsstruktur forbedringer**:
  - Tilføjet oversigtssektioner, der fremhæver modernisering og SDK-tilpasning
  - Forbedret med emojis og bedre formatering for forbedret læsbarhed
  - Tilføjet korrekte referencer til lokale prøvefiler i hele dokumentationen
  - Inkluderet produktionsklare implementeringsvejledninger og bedste praksis

### Tilføjet
- Omfattende oversigtssektioner i Modul08-filer, der fremhæver moderne SDK-integration
- Arkitekturhøjdepunkter, der viser avancerede funktioner (multi-agent systemer, intelligent routing)
- Direkte referencer til lokale prøveimplementeringer for hands-on erfaring
- Vejledning til produktionsimplementering med overvågning og fejlbehandlingsmønstre
- Interaktive Jupyter notebook eksempler med avancerede funktioner og benchmarks

### Rettet
- Tilpasningsforskelle mellem dokumentation og faktiske prøveimplementeringer
- Forældede SDK-brugsmønstre i hele Modul08
- Manglende referencer til omfattende lokal prøvebibliotek
- Inkonsistente implementeringsmetoder på tværs af forskellige sektioner

---

## 2025-09-18

### Tilføjet
- Modul08: Microsoft Foundry Local – Komplet udviklerværktøjssæt
  - Seks sessioner: opsætning, Azure AI Foundry integration, open-source modeller, banebrydende demoer, agenter og modeller-som-værktøjer
  - Kørbare eksempler under `Module08/samples/01`–`06` med Windows cmd-instruktioner
    - `01` REST hurtig chat (`chat_quickstart.py`)
    - `02` SDK hurtigstart med OpenAI/Foundry Local og Azure OpenAI support (`sdk_quickstart.py`)
    - `03` CLI liste-og-benchmark (`list_and_bench.cmd`)
    - `04` Chainlit demo (`app.py`)
    - `05` Multi-agent orkestrering (`python -m samples.05.agents.coordinator`)
    - `06` Models-as-Tools router (`router.py`)
- Azure OpenAI support i Session 2 SDK-eksempel med miljøvariabelkonfiguration
- `.vscode/settings.json` peger på `Module08/.venv` og forbedrer Python-analyseopløsning
- `.env` med `PYTHONPATH` hint for VS Code/Pylance opmærksomhed

### Ændret
- Standardmodel opdateret til `phi-4-mini` på tværs af Module 08 dokumentation og eksempler; fjernet resterende `phi-3.5` omtaler inden for Module 08
- Router (`Module08/samples/06/router.py`) forbedringer:
  - Endpoint-opdagelse via `foundry service status` med regex-parsing
  - `/v1/models` sundhedstjek ved opstart
  - Miljøkonfigurerbar modelregister (`GENERAL_MODEL`, `REASONING_MODEL`, `CODE_MODEL`, `TOOL_REGISTRY` JSON)
- Krav opdateret: `Module08/requirements.txt` inkluderer nu `openai` (sammen med `requests`, `chainlit`)
- Chainlit-eksempelvejledning præciseret og fejlfinding tilføjet; importopløsning via arbejdsområdets indstillinger

### Rettet
- Løste importproblemer:
  - Router afhænger ikke længere af et ikke-eksisterende `utils` modul; funktioner er integreret
  - Koordinator bruger relativ import (`from .specialists import ...`) og kaldes via modulsti
  - VS Code/Pylance konfiguration til at løse `chainlit` og pakkeimporter
- Rettede mindre stavefejl i `STUDY_GUIDE.md` og tilføjede Module 08 dækning

### Fjernet
- Slettede ubrugte `Module08/infra/obs.py` og fjernede den tomme `infra/` mappe; observabilitetsmønstre bevaret som valgfri i dokumentationen

### Flyttet
- Konsoliderede Module 08 demoer under `Module08/samples` med sessionnummererede mapper
  - Flyttede Chainlit app til `samples/04`
  - Flyttede agenter til `samples/05` og tilføjede `__init__.py` filer for pakkeopløsning

### Dokumentation
- Module 08 sessiondokumentation og alle eksempel-README'er beriget med Microsoft Learn og betroede leverandørreferencer
- `Module08/README.md` opdateret med Oversigt over eksempler, routerkonfiguration og valideringstips
- `Module07/README.md` Windows Foundry Local sektion valideret mod Learn dokumentation
- `STUDY_GUIDE.md` opdateret:
  - Tilføjede Module 08 til oversigt, tidsplaner, fremskridtssporing
  - Tilføjede omfattende Referenceliste (Foundry Local, Azure AI, Olive, ONNX Runtime, OpenVINO, MLX, Llama.cpp, vLLM, Ollama, AI Toolkit, Windows ML)

---

## Historisk (resumé)
- Kursusarkitektur og moduler etableret (Moduler 01–07)
- Iterativ modernisering af indhold, standardisering af formatering og tilføjede casestudier
- Udvidet dækning af optimeringsrammer (Llama.cpp, Olive, OpenVINO, Apple MLX)

## Ikke udgivet / Backlog (forslag)
- Valgfrie røggastests pr. eksempel for at validere Foundry Local tilgængelighed
- Gennemgå oversættelser for at tilpasse modelreferencer (f.eks. `phi-4-mini`) hvor det er relevant
- Tilføj minimal pyright-konfiguration, hvis teams foretrækker arbejdsområdebred strenghed

---

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal det bemærkes, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi er ikke ansvarlige for eventuelle misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
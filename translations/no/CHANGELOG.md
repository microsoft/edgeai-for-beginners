# Endringslogg

Alle merkbare endringer i EdgeAI for Beginners er dokumentert her. Dette prosjektet bruker dato-baserte oppføringer og Keep a Changelog-stil (Lagt til, Endret, Fikset, Fjernet, Dokumentasjon, Flyttet).

## 2025-10-30

### Lagt til - Modul06 AI-agenter omfattende forbedring
- **Microsoft Agent Framework-integrasjon** (`Module06/01.IntroduceAgent.md`):
  - Fullstendig seksjon om Microsoft Agent Framework for produksjonsklare agentutvikling
  - Detaljerte integrasjonsmønstre med Foundry Local for edge-distribusjon
  - Eksempler på orkestrering av flere agenter med spesialiserte SLM-modeller
  - Mønstre for bedriftsdistribusjon med ressursstyring og overvåking
  - Sikkerhets- og samsvarsfunksjoner for edge-agent-systemer
  - Eksempler på implementering i virkelige situasjoner (detaljhandel, helsevesen, kundeservice)

- **Strategier for produksjonsdistribusjon av SLM-agenter**:
  - **Foundry Local**: Fullstendig dokumentasjon for enterprise-grade edge AI runtime med installasjon, konfigurasjon og produksjonsmønstre
  - **Ollama**: Forbedret samfunnsfokusert distribusjon med omfattende overvåking og modelladministrasjon
  - **VLLM**: Høyytelses inferensmotor med avanserte optimaliseringsteknikker og bedriftsfunksjoner
  - Sjekklister for produksjonsdistribusjon og sammenligningstabeller for alle tre plattformer

- **Forbedring av edge-optimaliserte SLM-rammeverk**:
  - **ONNX Runtime**: Ny omfattende seksjon for plattformuavhengig SLM-agent-distribusjon
  - Universelle distribusjonsmønstre på Windows, Linux, macOS, iOS og Android
  - Maskinvareakselerasjonsalternativer (CPU, GPU, NPU) med automatisk deteksjon
  - Produksjonsklare funksjoner og agentspesifikke optimaliseringer
  - Fullstendige implementeringseksempler med Microsoft Agent Framework-integrasjon

- **Referanser og videre lesing**:
  - Omfattende ressursbibliotek med 100+ autoritative kilder
  - Kjerneforskning på AI-agenter og Small Language Models
  - Offisiell dokumentasjon for alle større rammeverk og verktøy
  - Bransjerapporter, markedsanalyser og tekniske referanser
  - Utdanningsressurser, konferanser og samfunnsfora
  - Standarder, spesifikasjoner og samsvarsrammeverk

### Endret - Modernisering av Modul06-innhold
- **Forbedrede læringsmål**: Lagt til mestring av Microsoft Agent Framework og edge-distribusjonskapasiteter
- **Fokus på produksjon**: Skiftet fra konseptuell til implementeringsklar veiledning med produksjonseksempler
- **Kodeeksempler**: Oppdatert alle eksempler til å bruke moderne SDK-mønstre og beste praksis
- **Arkitekturmønstre**: Lagt til hierarkiske agentarkitekturer og edge-til-sky-koordinering
- **Ytelsesoptimalisering**: Forbedret med ressursstyring og anbefalinger for automatisk skalering

### Dokumentasjon - Forbedring av Modul06-struktur
- **Omfattende dekning av Agent Framework**: Fra grunnleggende konsepter til bedriftsdistribusjon
- **Strategier for produksjonsdistribusjon**: Fullstendige guider for Foundry Local, Ollama og VLLM
- **Plattformuavhengig optimalisering**: Lagt til ONNX Runtime for universell distribusjon
- **Ressursbibliotek**: Omfattende referanser for videre læring og implementering

### Lagt til - Oppdatering av Modul06 Model Context Protocol (MCP)-dokumentasjon
- **Modernisering av MCP-introduksjon** (`Module06/03.IntroduceMCP.md`):
  - Oppdatert med de nyeste MCP-spesifikasjonene fra modelcontextprotocol.io (versjon 2025-06-18)
  - Lagt til offisiell USB-C-analog for standardiserte AI-applikasjonskoblinger
  - Oppdatert arkitekturseksjon med offisiell tolagsdesign (Data Layer + Transport Layer)
  - Forbedret dokumentasjon av kjerneprimitiver med serverprimitiver (Verktøy, Ressurser, Prompter) og klientprimitiver (Sampling, Elicitation, Logging)

- **Omfattende MCP-referanser og ressurser**:
  - Lagt til **MCP for Beginners**-lenke (https://aka.ms/mcp-for-beginners)
  - Offisiell MCP-dokumentasjon og spesifikasjoner (modelcontextprotocol.io)
  - Utviklingsressurser inkludert MCP Inspector og referanseimplementeringer
  - Tekniske standarder (JSON-RPC 2.0, JSON Schema, OpenAPI, Server-Sent Events)

### Lagt til - Modul04 Qualcomm QNN-integrasjon
- **Ny seksjon 7: Qualcomm QNN Optimization Suite** (`Module04/05.QualcommQNN.md`):
  - Omfattende 400+ linjers guide som dekker Qualcomms enhetlige AI-inferensrammeverk
  - Detaljert dekning av heterogen databehandling (Hexagon NPU, Adreno GPU, Kryo CPU)
  - Maskinvarebevisst optimalisering for Snapdragon-plattformer med intelligent arbeidsfordeling
  - Avanserte kvantiseringsteknikker (INT8, INT16, blandet presisjon) for mobil distribusjon
  - Strømeffektiv inferensoptimalisering for batteridrevne enheter og sanntidsapplikasjoner
  - Fullstendig installasjonsveiledning med QNN SDK-oppsett og miljøkonfigurasjon
  - Praktiske eksempler: PyTorch til QNN-konvertering, multi-backend-optimalisering, kontekstbinær generering
  - Avanserte bruksmønstre: tilpasset backend-konfigurasjon, dynamisk kvantisering, ytelsesprofilering
  - Omfattende feilsøkingsseksjon og samfunnsressurser

- **Forbedret Modul04-struktur**:
  - Oppdatert README.md til å inkludere 7 progressive seksjoner (tidligere 6)
  - Lagt til Qualcomm QNN i ytelsesbenchmark-tabellen (5-15x hastighetsforbedring, 50-80% minnebesparelse)
  - Omfattende læringsutbytte for mobil AI-distribusjon og strømoptimalisering

### Endret - Oppdateringer av Modul04-dokumentasjon
- **Forbedring av Microsoft Olive-dokumentasjon** (`Module04/03.MicrosoftOlive.md`):
  - Lagt til omfattende "Olive Recipes Repository"-seksjon som dekker 100+ forhåndsbygde optimaliseringsoppskrifter
  - Detaljert dekning av støttede modellfamilier (Phi, Llama, Qwen, Gemma, Mistral, DeepSeek)
  - Praktiske brukseksempler for oppskriftsjustering og samfunnsbidrag
  - Forbedret med ytelsesbenchmark og integrasjonsveiledning

- **Omorganisering av seksjoner i Modul04**:
  - Apple MLX flyttet til seksjon 5 (tidligere seksjon 6)
  - Workflow Synthesis flyttet til seksjon 6 (tidligere seksjon 7)
  - Qualcomm QNN plassert som seksjon 7 (spesialisert mobil/edge-fokus)
  - Oppdatert alle filreferanser og navigasjonslenker deretter

### Fikset - Validering av workshop-eksempler
- **chat_bootstrap.py validering og reparasjon**:
  - Fikset ødelagt importsetning (`util.util.workshop_utils` → `util.workshop_utils`)
  - Opprettet manglende `__init__.py` i util-pakken for korrekt Python-moduloppløsning
  - Installert nødvendige avhengigheter (openai, foundry-local-sdk) i conda-miljøet
  - Lyktes med validering av eksempelutførelse med både standard og tilpassede prompter
  - Bekreftet integrasjon med Foundry Local-tjenesten og modellinnlasting (phi-4-mini med CUDA-optimalisering)

### Dokumentasjon - Omfattende oppdateringer av guider
- **Fullstendig omstrukturering av Modul04 README.md**:
  - Lagt til Qualcomm QNN som stort optimaliseringsrammeverk sammen med OpenVINO, Olive, MLX
  - Oppdatert kapittel-læringsutbytte for å inkludere mobil AI-distribusjon og strømoptimalisering
  - Forbedret ytelsessammenligningstabell med QNN-metrikker og mobil/edge-brukstilfeller
  - Opprettholdt logisk progresjon fra bedriftsløsninger til plattformspesifikke optimaliseringer

- **Kryssreferanser og navigasjon**:
  - Oppdatert alle interne lenker og filreferanser for ny seksjonsnummerering
  - Forbedret beskrivelse av workflow synthesis for å inkludere mobil-, desktop- og skymiljøer
  - Lagt til omfattende ressurslenker for Qualcomms utviklerøkosystem

## 2025-10-08

### Lagt til - Omfattende oppdatering av workshop
- **Fullstendig omskriving av Workshop README.md**:
  - Lagt til omfattende introduksjon som forklarer verdiforslaget til Edge AI (personvern, ytelse, kostnad)
  - Opprettet 6 kjerne-læringsmål med detaljerte kompetanser
  - Lagt til tabell for læringsutbytte med leveranser og kompetansematrise
  - Inkludert seksjon om karriereklare ferdigheter for bransjerelevans
  - Lagt til hurtigstartveiledning med forutsetninger og 3-trinns oppsett
  - Opprettet ressursoversikt for Python-eksempler (8 filer med kjøretider)
  - Lagt til tabell for Jupyter-notatbøker (8 notatbøker med vanskelighetsgrader)
  - Opprettet dokumentasjonstabell (7 viktige dokumenter med "Bruk når"-veiledning)
  - Lagt til anbefalinger for læringsstier for ulike ferdighetsnivåer

- **Validerings- og testinfrastruktur for workshop**:
  - Opprettet `scripts/validate_samples.py` - Omfattende valideringsverktøy for syntaks, import og beste praksis
  - Opprettet `scripts/test_samples.py` - Testverktøy for alle Python-eksempler
  - Lagt til valideringsdokumentasjon i `scripts/README.md`

- **Omfattende dokumentasjon**:
  - Opprettet `SAMPLES_UPDATE_SUMMARY.md` - 400+ linjers detaljert guide som dekker alle forbedringer
  - Opprettet `UPDATE_COMPLETE.md` - Oppsummering av oppdateringens fullføring
  - Opprettet `QUICK_REFERENCE.md` - Hurtigreferansekort for workshop

### Endret - Modernisering av Python-eksempler i workshop
- **Alle 8 Python-eksempler oppdatert med beste praksis**:
  - Forbedret feilhåndtering med try-except-blokker rundt alle I/O-operasjoner
  - Lagt til typehinting og omfattende docstrings
  - Implementert konsistent [INFO]/[ERROR]/[RESULT]-loggmønster
  - Beskyttet valgfrie imports med installasjonstips
  - Forbedret brukerfeedback i alle eksempler

- **session01/chat_bootstrap.py**:
  - Forbedret klientinitialisering med omfattende feilmeldinger
  - Forbedret feilhåndtering for streaming med validering av chunks
  - Lagt til bedre unntakshåndtering for tjenesteutilgjengelighet

- **session02/rag_pipeline.py**:
  - Lagt til importbeskyttelse for sentence-transformers med installasjonstips
  - Forbedret feilhåndtering for embedding- og genereringsoperasjoner
  - Forbedret utdataformat med strukturerte resultater

- **session02/rag_eval_ragas.py**:
  - Beskyttet valgfrie imports (ragas, datasets) med brukervennlige feilmeldinger
  - Lagt til feilhåndtering for evalueringsmetrikker
  - Forbedret utdataformat for evalueringsresultater

- **session03/benchmark_oss_models.py**:
  - Implementert grasiøs degradering (fortsetter ved modellfeil)
  - Lagt til detaljert fremdriftsrapportering og feilhåndtering per modell
  - Forbedret statistikkberegning med omfattende feilhåndtering

- **session04/model_compare.py**:
  - Lagt til typehinting (Tuple-returtyper)
  - Forbedret utdataformat med strukturerte JSON-resultater
  - Implementert feilhåndtering per modell med gjenoppretting

- **session05/agents_orchestrator.py**:
  - Forbedret Agent.act() med omfattende docstrings
  - Lagt til pipeline-feilhåndtering med logging for hvert trinn
  - Forbedret minnehåndtering og tilstandssporing

- **session06/models_router.py**:
  - Forbedret funksjonsdokumentasjon for alle rutekomponenter
  - Lagt til detaljert logging i route()-funksjonen
  - Forbedret testutdata med strukturerte resultater

- **session06/models_pipeline.py**:
  - Lagt til feilhåndtering i chat()-hjelpefunksjonen
  - Forbedret pipeline() med logging for hvert trinn og fremdriftsrapportering
  - Forbedret main() med omfattende feilhåndtering

### Dokumentasjon - Forbedring av workshop-dokumentasjon
- Oppdatert hoved-README.md med workshop-seksjon som fremhever praktisk læringssti
- Forbedret STUDY_GUIDE.md med omfattende workshop-seksjon inkludert:
  - Læringsmål og fokusområder for studier
  - Selvtestspørsmål
  - Praktiske øvelser med tidsestimater
  - Tidsallokering for konsentrert og deltidsstudie
  - Lagt til workshop i fremdriftssporingsmal
- Oppdatert tidsallokeringsguide fra 20 timer til 30 timer (inkludert workshop)
- Lagt til beskrivelser av workshop-eksempler og læringsutbytte i README

### Fikset
- Løst inkonsekvente feilhåndteringsmønstre i workshop-eksempler
- Fikset valgfrie avhengighetsimportfeil med riktige beskyttelser
- Rettet manglende typehinting i kritiske funksjoner
- Adressert utilstrekkelig brukerfeedback i feilscenarier
- Fikset valideringsproblemer med omfattende testinfrastruktur

---

## 2025-09-23

### Endret - Større modernisering av Modul 08
- **Omfattende tilpasning til Microsoft Foundry-Local repository-mønstre**
  - Oppdatert alle kodeeksempler til å bruke moderne `FoundryLocalManager` og OpenAI SDK-integrasjon
  - Erstattet utdaterte manuelle `requests`-kall med korrekt SDK-bruk
  - Tilpasset implementeringsmønstre til offisiell Microsoft-dokumentasjon og eksempler

- **Modernisering av 05.AIPoweredAgents.md**:
  - Oppdatert orkestrering av flere agenter til å bruke moderne SDK-mønstre
  - Forbedret koordinatorimplementering med avanserte funksjoner (feedback loops, ytelsesovervåking)
  - Lagt til omfattende feilhåndtering og tjenestehelsekontroll
  - Integrert riktige referanser til lokale eksempler (`samples/05/multi_agent_orchestration.ipynb`)
  - Oppdatert funksjonskalleksempler til å bruke moderne `tools`-parameter i stedet for utdaterte `functions`
  - Lagt til produksjonsklare mønstre med overvåking og statistikksporing

- **Fullstendig omskriving av 06.ModelsAsTools.md**:
  - Erstattet grunnleggende verktøyregister med intelligent modellruterimplementering
  - Lagt til nøkkelordbasert modellvalg for ulike oppgavetyper (generelt, resonnering, kode, kreativt)
  - Integrert miljøbasert konfigurasjon med fleksibel modelltilordning
  - Forbedret med omfattende tjenestehelseovervåking og feilhåndtering
  - Lagt til produksjonsdistribusjonsmønstre med forespørselsovervåking og ytelsessporing
  - Tilpasset lokal implementering i `samples/06/router.py` og `samples/06/model_router.ipynb`

- **Forbedringer i dokumentasjonsstruktur**:
  - Lagt til oversiktsseksjoner som fremhever modernisering og SDK-tilpasning
  - Forbedret med emojis og bedre formatering for forbedret lesbarhet
  - Lagt til riktige referanser til lokale eksempel-filer gjennom dokumentasjonen
  - Inkludert veiledning for produksjonsklare implementeringer og beste praksis

### Lagt til
- Omfattende oversiktsseksjoner i Modul 08-filer som fremhever moderne SDK-integrasjon
- Arkitekturhøydepunkter som viser avanserte funksjoner (multi-agent-systemer, intelligent ruting)
- Direkte referanser til lokale eksempelimplementeringer for praktisk erfaring
- Veiledning for produksjonsdistribusjon med overvåking og feilhåndteringsmønstre
- Interaktive Jupyter-notatbokeksem
  - Kjørbare eksempler under `Module08/samples/01`–`06` med Windows cmd-instruksjoner
    - `01` REST rask chat (`chat_quickstart.py`)
    - `02` SDK rask start med OpenAI/Foundry Local og Azure OpenAI-støtte (`sdk_quickstart.py`)
    - `03` CLI liste-og-benchmark (`list_and_bench.cmd`)
    - `04` Chainlit-demo (`app.py`)
    - `05` Multi-agent orkestrering (`python -m samples.05.agents.coordinator`)
    - `06` Modeller-som-verktøy router (`router.py`)
- Azure OpenAI-støtte i Session 2 SDK-eksempel med miljøvariabelkonfigurasjon
- `.vscode/settings.json` peker til `Module08/.venv` for å forbedre Python-analyseoppløsning
- `.env` med `PYTHONPATH` hint for VS Code/Pylance bevissthet

### Endret
- Standardmodell oppdatert til `phi-4-mini` på tvers av Module 08-dokumenter og eksempler; fjernet gjenværende referanser til `phi-3.5` i Module 08
- Router (`Module08/samples/06/router.py`) forbedringer:
  - Endepunktoppdagelse via `foundry service status` med regex-parsing
  - `/v1/models` helsesjekk ved oppstart
  - Miljøkonfigurerbar modellregister (`GENERAL_MODEL`, `REASONING_MODEL`, `CODE_MODEL`, `TOOL_REGISTRY` JSON)
- Krav oppdatert: `Module08/requirements.txt` inkluderer nå `openai` (sammen med `requests`, `chainlit`)
- Chainlit-eksempelveiledning klargjort og feilsøking lagt til; importoppløsning via arbeidsområdets innstillinger

### Fikset
- Løste importproblemer:
  - Router avhenger ikke lenger av en ikke-eksisterende `utils`-modul; funksjoner er integrert
  - Koordinator bruker relativ import (`from .specialists import ...`) og kalles via modulsti
  - VS Code/Pylance-konfigurasjon for å løse `chainlit` og pakkeimporter
- Rettet mindre skrivefeil i `STUDY_GUIDE.md` og la til Module 08-dekning

### Fjernet
- Slettet ubrukt `Module08/infra/obs.py` og fjernet den tomme `infra/`-mappen; observasjonsmønstre beholdt som valgfrie i dokumentasjonen

### Flyttet
- Konsoliderte Module 08-demoer under `Module08/samples` med sesjonsnummererte mapper
  - Flyttet Chainlit-app til `samples/04`
  - Flyttet agenter til `samples/05` og la til `__init__.py`-filer for pakkeoppløsning

### Dokumentasjon
- Module 08-sesjonsdokumenter og alle eksempels README-er beriket med Microsoft Learn og pålitelige leverandørreferanser
- `Module08/README.md` oppdatert med oversikt over eksempler, router-konfigurasjon og valideringstips
- `Module07/README.md` Windows Foundry Local-seksjon validert mot Learn-dokumenter
- `STUDY_GUIDE.md` oppdatert:
  - La til Module 08 i oversikt, tidsplaner, fremdriftssporing
  - La til omfattende referanseseksjon (Foundry Local, Azure AI, Olive, ONNX Runtime, OpenVINO, MLX, Llama.cpp, vLLM, Ollama, AI Toolkit, Windows ML)

---

## Historisk (sammendrag)
- Kursarkitektur og moduler etablert (Moduler 01–07)
- Iterativ modernisering av innhold, standardisering av formatering og tilføyelse av casestudier
- Utvidet dekning av optimaliseringsrammeverk (Llama.cpp, Olive, OpenVINO, Apple MLX)

## Uutgitt / Backlog (forslag)
- Valgfrie røyktester per eksempel for å validere Foundry Local tilgjengelighet
- Gjennomgå oversettelser for å tilpasse modellreferanser (f.eks. `phi-4-mini`) der det er passende
- Legg til minimal pyright-konfigurasjon hvis team foretrekker strenghet på tvers av arbeidsområdet

---

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi tilstreber nøyaktighet, vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på dets opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
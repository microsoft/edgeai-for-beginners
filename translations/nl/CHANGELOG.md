<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "78ca68df03ae43371b203ea43d346dec",
  "translation_date": "2025-10-30T13:22:05+00:00",
  "source_file": "CHANGELOG.md",
  "language_code": "nl"
}
-->
# Wijzigingslogboek

Alle belangrijke wijzigingen aan EdgeAI voor Beginners worden hier gedocumenteerd. Dit project gebruikt datumgebaseerde vermeldingen en de Keep a Changelog-stijl (Toegevoegd, Gewijzigd, Gerepareerd, Verwijderd, Documentatie, Verplaatst).

## 2025-10-30

### Toegevoegd - Module06 AI Agents Uitgebreide Verbetering
- **Microsoft Agent Framework Integratie** (`Module06/01.IntroduceAgent.md`):
  - Volledige sectie over Microsoft Agent Framework voor productieklare agentontwikkeling
  - Gedetailleerde integratiepatronen met Foundry Local voor edge-implementatie
  - Voorbeelden van multi-agent orkestratie met gespecialiseerde SLM-modellen
  - Patronen voor bedrijfsimplementatie met resourcebeheer en monitoring
  - Beveiligings- en compliancefuncties voor edge-agent systemen
  - Praktijkvoorbeelden (retail, gezondheidszorg, klantenservice)

- **Productie SLM Agent Implementatiestrategieën**:
  - **Foundry Local**: Volledige documentatie van een bedrijfswaardige edge AI-runtime met installatie, configuratie en productiepatronen
  - **Ollama**: Verbeterde communitygerichte implementatie met uitgebreide monitoring en modelbeheer
  - **VLLM**: Hoogpresterende inferentie-engine met geavanceerde optimalisatietechnieken en bedrijfsfuncties
  - Checklists voor productie-implementatie en vergelijkende tabellen voor alle drie de platforms

- **Verbetering van Edge-geoptimaliseerde SLM Frameworks**:
  - **ONNX Runtime**: Nieuwe uitgebreide sectie voor cross-platform SLM-agent implementatie
  - Universele implementatiepatronen voor Windows, Linux, macOS, iOS en Android
  - Hardwareversnellingopties (CPU, GPU, NPU) met automatische detectie
  - Productieklare functies en agent-specifieke optimalisaties
  - Volledige implementatievoorbeelden met Microsoft Agent Framework integratie

- **Referenties en Verdere Lezing**:
  - Uitgebreide bibliotheek met 100+ gezaghebbende bronnen
  - Kernonderzoekspapers over AI-agents en Small Language Models
  - Officiële documentatie voor alle belangrijke frameworks en tools
  - Industriële rapporten, marktanalyse en technische benchmarks
  - Educatieve bronnen, conferenties en communityforums
  - Normen, specificaties en compliance frameworks

### Gewijzigd - Module06 Content Modernisering
- **Verbeterde Leerdoelen**: Toegevoegd Microsoft Agent Framework beheersing en edge-implementatievaardigheden
- **Productiefocus**: Verschuiving van conceptueel naar implementatieklare richtlijnen met praktijkvoorbeelden
- **Codevoorbeelden**: Alle voorbeelden bijgewerkt naar moderne SDK-patronen en best practices
- **Architectuurpatronen**: Toegevoegd hiërarchische agentarchitecturen en edge-to-cloud coördinatie
- **Prestatieoptimalisatie**: Verbeterd met resourcebeheer en aanbevelingen voor automatische schaalvergroting

### Documentatie - Module06 Structuurverbetering
- **Uitgebreide Agent Framework Dekking**: Van basisconcepten tot bedrijfsimplementatie
- **Productie Implementatiestrategieën**: Volledige gidsen voor Foundry Local, Ollama en VLLM
- **Cross-Platform Optimalisatie**: Toegevoegd ONNX Runtime voor universele implementatie
- **Bronbibliotheek**: Uitgebreide referenties voor voortgezet leren en implementatie

### Toegevoegd - Module06 Model Context Protocol (MCP) Documentatie Update
- **MCP Introductie Modernisering** (`Module06/03.IntroduceMCP.md`):
  - Bijgewerkt met de nieuwste MCP-specificaties van modelcontextprotocol.io (versie 2025-06-18)
  - Toegevoegd officiële USB-C analogie voor gestandaardiseerde AI-toepassingsverbindingen
  - Bijgewerkte architectuursectie met officiële tweelaagse ontwerp (Datalayer + Transportlayer)
  - Verbeterde kernprimitieven documentatie met serverprimitieven (Tools, Resources, Prompts) en clientprimitieven (Sampling, Elicitation, Logging)

- **Uitgebreide MCP Referenties en Bronnen**:
  - Toegevoegd **MCP voor Beginners** link (https://aka.ms/mcp-for-beginners)
  - Officiële MCP-documentatie en specificaties (modelcontextprotocol.io)
  - Ontwikkelbronnen inclusief MCP Inspector en referentie-implementaties
  - Technische standaarden (JSON-RPC 2.0, JSON Schema, OpenAPI, Server-Sent Events)

### Toegevoegd - Module04 Qualcomm QNN Integratie
- **Nieuwe Sectie 7: Qualcomm QNN Optimalisatie Suite** (`Module04/05.QualcommQNN.md`):
  - Uitgebreide gids van 400+ regels over Qualcomm's uniforme AI-inferentie framework
  - Gedetailleerde dekking van heterogene computing (Hexagon NPU, Adreno GPU, Kryo CPU)
  - Hardwarebewuste optimalisatie voor Snapdragon-platforms met intelligente werkverdeling
  - Geavanceerde kwantiseringstechnieken (INT8, INT16, gemengde precisie) voor mobiele implementatie
  - Energie-efficiënte inferentieoptimalisatie voor batterijgevoede apparaten en realtime toepassingen
  - Volledige installatiegids met QNN SDK setup en configuratie van de omgeving
  - Praktijkvoorbeelden: PyTorch naar QNN conversie, multi-backend optimalisatie, context binaire generatie
  - Geavanceerde gebruikspatronen: aangepaste backend configuratie, dynamische kwantisering, prestatieprofilering
  - Uitgebreide probleemoplossingssectie en communitybronnen

- **Verbeterde Module04 structuur**:
  - Bijgewerkte README.md om 7 progressieve secties te bevatten (was 6)
  - Toegevoegd Qualcomm QNN aan prestatietabel benchmarks (5-15x snelheidsverbetering, 50-80% geheugenreductie)
  - Uitgebreide leerresultaten voor mobiele AI-implementatie en energieoptimalisatie

### Gewijzigd - Module04 Documentatie Updates
- **Microsoft Olive documentatie verbetering** (`Module04/03.MicrosoftOlive.md`):
  - Toegevoegd uitgebreide "Olive Recipes Repository" sectie met 100+ vooraf gebouwde optimalisatierecepten
  - Gedetailleerde dekking van ondersteunde modelfamilies (Phi, Llama, Qwen, Gemma, Mistral, DeepSeek)
  - Praktijkvoorbeelden voor receptaanpassing en communitybijdragen
  - Verbeterd met prestatietabellen en integratierichtlijnen

- **Sectie herordening in Module04**:
  - Apple MLX verplaatst naar Sectie 5 (was Sectie 6)
  - Workflow Synthese verplaatst naar Sectie 6 (was Sectie 7)
  - Qualcomm QNN gepositioneerd als Sectie 7 (gespecialiseerde mobiele/edge focus)
  - Alle bestandsreferenties en navigatielinks dienovereenkomstig bijgewerkt

### Gerepareerd - Workshop Voorbeeldvalidatie
- **chat_bootstrap.py validatie en reparatie**:
  - Gecorrigeerde corrupte importverklaring (`util.util.workshop_utils` → `util.workshop_utils`)
  - Ontbrekende `__init__.py` gemaakt in util pakket voor juiste Python module resolutie
  - Vereiste afhankelijkheden geïnstalleerd (openai, foundry-local-sdk) in conda omgeving
  - Succesvol voorbeelduitvoering gevalideerd met zowel standaard als aangepaste prompts
  - Integratie bevestigd met Foundry Local service en model laden (phi-4-mini met CUDA optimalisatie)

### Documentatie - Uitgebreide Gids Updates
- **Module04 README.md volledige herstructurering**:
  - Toegevoegd Qualcomm QNN als belangrijk optimalisatie framework naast OpenVINO, Olive, MLX
  - Bijgewerkte hoofdstuk leerresultaten om mobiele AI-implementatie en energieoptimalisatie te omvatten
  - Verbeterde prestatietabel met QNN-metrics en mobiele/edge use cases
  - Logische voortgang behouden van bedrijfsoplossingen naar platform-specifieke optimalisaties

- **Kruisverwijzingen en navigatie**:
  - Alle interne links en bestandsreferenties bijgewerkt voor nieuwe sectienummering
  - Verbeterde workflow synthese beschrijving om mobiele, desktop- en cloudomgevingen te omvatten
  - Uitgebreide bronlinks toegevoegd voor Qualcomm ontwikkelaarsecosysteem

## 2025-10-08

### Toegevoegd - Workshop Uitgebreide Update
- **Workshop README.md volledige herschrijving**:
  - Toegevoegd uitgebreide introductie die de waardepropositie van Edge AI uitlegt (privacy, prestaties, kosten)
  - Gecreëerd 6 kernleerdoelen met gedetailleerde competenties
  - Toegevoegd leerresultatentabel met deliverables en competentiematrix
  - Inclusief sectie met carrièregerichte vaardigheden voor relevantie in de industrie
  - Toegevoegd snelle startgids met vereisten en 3-stappen setup
  - Gecreëerd bronentabellen voor Python voorbeelden (8 bestanden met looptijden)
  - Toegevoegd Jupyter notebooks tabel (8 notebooks met moeilijkheidsbeoordelingen)
  - Gecreëerd documentatietabel (7 belangrijke documenten met "Gebruik Wanneer" richtlijnen)
  - Toegevoegd leerpad aanbevelingen voor verschillende vaardigheidsniveaus

- **Workshop validatie- en testinfrastructuur**:
  - Gecreëerd `scripts/validate_samples.py` - Uitgebreide validatietool voor syntax, imports en best practices
  - Gecreëerd `scripts/test_samples.py` - Smoke test runner voor alle Python voorbeelden
  - Validatiedocumentatie toegevoegd aan `scripts/README.md`

- **Uitgebreide documentatie**:
  - Gecreëerd `SAMPLES_UPDATE_SUMMARY.md` - Gedetailleerde gids van 400+ regels over alle verbeteringen
  - Gecreëerd `UPDATE_COMPLETE.md` - Samenvatting van de voltooiing van de update
  - Gecreëerd `QUICK_REFERENCE.md` - Snelle referentiekaart voor Workshop

### Gewijzigd - Workshop Python Voorbeeld Modernisering
- **Alle 8 Python voorbeelden bijgewerkt met best practices**:
  - Verbeterde foutafhandeling met try-except blokken rond alle I/O-operaties
  - Toegevoegd type hints en uitgebreide docstrings
  - Geïmplementeerd consistent [INFO]/[ERROR]/[RESULT] logpatroon
  - Optionele imports beschermd met installatiehints
  - Verbeterde gebruikersfeedback in alle voorbeelden

- **session01/chat_bootstrap.py**:
  - Verbeterde clientinitialisatie met uitgebreide foutmeldingen
  - Verbeterde streaming foutafhandeling met chunkvalidatie
  - Toegevoegd betere uitzonderingafhandeling voor service-onbeschikbaarheid

- **session02/rag_pipeline.py**:
  - Toegevoegd import guards voor sentence-transformers met installatiehints
  - Verbeterde foutafhandeling voor embedding en generatieoperaties
  - Verbeterde uitvoerformattering met gestructureerde resultaten

- **session02/rag_eval_ragas.py**:
  - Optionele imports beschermd (ragas, datasets) met gebruiksvriendelijke foutmeldingen
  - Toegevoegd foutafhandeling voor evaluatiemetrics
  - Verbeterde uitvoerformattering voor evaluatieresultaten

- **session03/benchmark_oss_models.py**:
  - Geïmplementeerd gratievolle degradatie (gaat door bij modelstoringen)
  - Toegevoegd gedetailleerde voortgangsrapportage en foutafhandeling per model
  - Verbeterde statistiekberekening met uitgebreide foutherstel

- **session04/model_compare.py**:
  - Toegevoegd type hints (Tuple return types)
  - Verbeterde uitvoerformattering met gestructureerde JSON-resultaten
  - Geïmplementeerd foutafhandeling per model met herstel

- **session05/agents_orchestrator.py**:
  - Verbeterde Agent.act() met uitgebreide docstrings
  - Toegevoegd pijplijn foutafhandeling met logging per fase
  - Verbeterd geheugenbeheer en statusregistratie

- **session06/models_router.py**:
  - Verbeterde functiedocumentatie voor alle routeringscomponenten
  - Toegevoegd gedetailleerde logging in route() functie
  - Verbeterde testuitvoer met gestructureerde resultaten

- **session06/models_pipeline.py**:
  - Toegevoegd foutafhandeling aan chat() hulpfunctie
  - Verbeterde pipeline() met logging per fase en voortgangsrapportage
  - Verbeterde main() met uitgebreide foutherstel

### Documentatie - Workshop Documentatie Verbetering
- Hoofd README.md bijgewerkt met Workshop sectie die hands-on leerpad benadrukt
- STUDY_GUIDE.md verbeterd met uitgebreide Workshop sectie inclusief:
  - Leerdoelen en studiefocusgebieden
  - Zelfbeoordelingsvragen
  - Hands-on oefeningen met tijdschattingen
  - Tijdallocatie voor geconcentreerd en deeltijdstudie
  - Workshop toegevoegd aan voortgangsvolgsjabloon
- Tijdallocatiegids bijgewerkt van 20 uur naar 30 uur (inclusief Workshop)
- Workshop voorbeeldbeschrijvingen en leerresultaten toegevoegd aan README

### Gerepareerd
- Opgeloste inconsistente foutafhandelingspatronen in Workshop voorbeelden
- Gecorrigeerde optionele afhankelijkheidsimportfouten met juiste guards
- Ontbrekende type hints in kritieke functies gecorrigeerd
- Onvoldoende gebruikersfeedback in foutscenario's aangepakt
- Validatieproblemen opgelost met uitgebreide testinfrastructuur

---

## 2025-09-23

### Gewijzigd - Grote Module 08 Modernisering
- **Uitgebreide afstemming met Microsoft Foundry-Local repository patronen**
  - Alle codevoorbeelden bijgewerkt naar moderne `FoundryLocalManager` en OpenAI SDK integratie
  - Verouderde handmatige `requests` oproepen vervangen door juiste SDK-gebruik
  - Implementatiepatronen afgestemd op officiële Microsoft documentatie en voorbeelden

- **05.AIPoweredAgents.md modernisering**:
  - Multi-agent orkestratie bijgewerkt naar moderne SDK-patronen
  - Verbeterde coördinatorimplementatie met geavanceerde functies (feedback loops, prestatiemonitoring)
  - Toegevoegd uitgebreide foutafhandeling en servicegezondheidscontrole
  - Correcte verwijzingen naar lokale voorbeelden geïntegreerd (`samples/05/multi_agent_orchestration.ipynb`)
  - Functieoproepvoorbeelden bijgewerkt naar moderne `tools` parameter in plaats van verouderde `functions`
  - Toegevoegd productieklare patronen met monitoring en statistiektracking

- **06.ModelsAsTools.md volledige herschrijving**:
  - Basis tool registry vervangen door intelligente modelrouter implementatie
  - Toegevoegd trefwoordgebaseerde modelselectie voor verschillende taaktypes (algemeen, redeneren, code, creatief)
  - Geïntegreerd omgevingsgebaseerde configuratie met flexibele modeltoewijzing
  - Verbeterd met uitgebreide servicegezondheidsmonitoring en foutafhandeling
  - Toegevoegd productie-implementatiepatronen met verzoekmonitoring en prestatie-tracking
  - Afgestemd op lokale implementatie in `samples/06/router.py` en `samples/06/model_router.ipynb`

- **Documentatiestructuur verbeteringen**:
  - Overzichtsecties toegevoegd die modernisering en SDK-afstemming benadrukken
  - Verbeterd met emoji's en betere opmaak voor verbeterde leesbaarheid
  - Correcte verwijzingen naar lokale voorbeeldbestanden door de hele documentatie toegevoegd
  - Inclusief productieklare implementatierichtlijnen en best practices

### Toegevoegd
- Uitgebreide overzichtsecties in Module 08 bestanden die moderne SDK-integratie benadrukken
- Architectuurhoogtepunten die geavanceerde functies tonen (multi-agent systemen, intelligente routering)
- Directe verwijzingen naar lokale voorbeeldimplementaties voor hands-on ervaring
- Productie-implementatierichtlijnen met monitoring en foutafhandelingspatronen
- Interactieve Jupyter notebook voorbeelden met geavanceerde functies en benchmarks

### Gerepareerd
- Afstemmingsverschillen tussen documentatie en daadwerkelijke voorbeeldimplementaties
- Verouderde SDK-gebruikspatronen door de hele Module 08
- Ontbrekende verwijzingen naar uitgebreide lokale voorbeeldbibliotheek
- Inconsistente implementatiebenaderingen in verschillende secties

---

## 2025-09-18

### Toegevoegd
- Module 08: Microsoft Foundry Local – Complete Ontwikkelaar Toolkit
  - Zes sessies: setup, Azure AI Foundry integratie, open-source modellen, cutting-edge demo's, agents en models-as-tools
  - Uitvoerbare voorbeelden onder `Module08/samples/01`–`06` met Windows cmd-instructies
    - `01` REST snelle chat (`chat_quickstart.py`)
    - `02` SDK snelle start met OpenAI/Foundry Local en Azure OpenAI ondersteuning (`sdk_quickstart.py`)
    - `03` CLI lijst-en-benchmark (`list_and_bench.cmd`)
    - `04` Chainlit demo (`app.py`)
    - `05` Multi-agent orkestratie (`python -m samples.05.agents.coordinator`)
    - `06` Models-as-Tools router (`router.py`)
- Azure OpenAI ondersteuning in Sessie 2 SDK voorbeeld met configuratie van omgevingsvariabelen
- `.vscode/settings.json` om te verwijzen naar `Module08/.venv` en Python-analyse resolutie te verbeteren
- `.env` met `PYTHONPATH` hint voor VS Code/Pylance bewustzijn

### Gewijzigd
- Standaardmodel bijgewerkt naar `phi-4-mini` in alle Module 08 documentatie en voorbeelden; resterende verwijzingen naar `phi-3.5` binnen Module 08 verwijderd
- Verbeteringen aan Router (`Module08/samples/06/router.py`):
  - Endpoint ontdekking via `foundry service status` met regex parsing
  - `/v1/models` gezondheidscontrole bij opstarten
  - Omgevingsconfigurabele modelregistratie (`GENERAL_MODEL`, `REASONING_MODEL`, `CODE_MODEL`, `TOOL_REGISTRY` JSON)
- Vereisten bijgewerkt: `Module08/requirements.txt` bevat nu `openai` (naast `requests`, `chainlit`)
- Chainlit voorbeeldinstructies verduidelijkt en probleemoplossing toegevoegd; importresolutie via werkruimte-instellingen

### Opgelost
- Importproblemen opgelost:
  - Router is niet langer afhankelijk van een niet-bestaande `utils` module; functies zijn geïntegreerd
  - Coordinator gebruikt relatieve import (`from .specialists import ...`) en wordt aangeroepen via modulepad
  - VS Code/Pylance configuratie om `chainlit` en pakketimporten te ondersteunen
- Kleine typfout gecorrigeerd in `STUDY_GUIDE.md` en Module 08 dekking toegevoegd

### Verwijderd
- Ongebruikte `Module08/infra/obs.py` verwijderd en de lege `infra/` map verwijderd; observatiepatronen behouden als optioneel in documentatie

### Verplaatst
- Module 08 demo's geconsolideerd onder `Module08/samples` met sessie-genummerde mappen
  - Chainlit app verplaatst naar `samples/04`
  - Agents verplaatst naar `samples/05` en `__init__.py` bestanden toegevoegd voor pakketresolutie

### Documentatie
- Module 08 sessiedocumentatie en alle voorbeeld-README's verrijkt met Microsoft Learn en betrouwbare leveranciersreferenties
- `Module08/README.md` bijgewerkt met Overzicht van Voorbeelden, routerconfiguratie en validatietips
- `Module07/README.md` Windows Foundry Local sectie gevalideerd tegen Learn documentatie
- `STUDY_GUIDE.md` bijgewerkt:
  - Module 08 toegevoegd aan overzicht, schema's, voortgangstracker
  - Uitgebreide Referenties sectie toegevoegd (Foundry Local, Azure AI, Olive, ONNX Runtime, OpenVINO, MLX, Llama.cpp, vLLM, Ollama, AI Toolkit, Windows ML)

---

## Historisch (samenvatting)
- Cursusarchitectuur en modules vastgesteld (Modules 01–07)
- Iteratieve modernisering van inhoud, standaardisatie van opmaak en toegevoegde casestudies
- Uitgebreide dekking van optimalisatieframeworks (Llama.cpp, Olive, OpenVINO, Apple MLX)

## Niet uitgebracht / Achterstand (voorstellen)
- Optionele rooktests per voorbeeld om beschikbaarheid van Foundry Local te valideren
- Vertalingen herzien om modelverwijzingen (bijv. `phi-4-mini`) waar nodig af te stemmen
- Minimale pyright configuratie toevoegen als teams werkruimte-brede strengheid prefereren

---

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
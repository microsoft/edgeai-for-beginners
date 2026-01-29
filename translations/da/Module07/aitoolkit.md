# AI Toolkit til Visual Studio Code - Edge AI Udviklingsguide

## Introduktion

Velkommen til den omfattende guide til brug af AI Toolkit til Visual Studio Code i Edge AI-udvikling. Efterhånden som kunstig intelligens bevæger sig fra centraliseret cloud computing til distribuerede edge-enheder, har udviklere brug for kraftfulde, integrerede værktøjer, der kan håndtere de unikke udfordringer ved edge-implementering - fra ressourcebegrænsninger til krav om offline drift.

AI Toolkit til Visual Studio Code bygger bro over denne kløft ved at tilbyde et komplet udviklingsmiljø, der er specifikt designet til at bygge, teste og optimere AI-applikationer, der kører effektivt på edge-enheder. Uanset om du udvikler til IoT-sensorer, mobile enheder, indlejrede systemer eller edge-servere, strømliner dette værktøj hele din udviklingsproces inden for det velkendte VS Code-miljø.

Denne guide vil føre dig gennem de essentielle begreber, værktøjer og bedste praksis for at udnytte AI Toolkit i dine Edge AI-projekter, fra den indledende modeludvælgelse til produktionsimplementering.

## Oversigt

AI Toolkit til Visual Studio Code er en kraftfuld udvidelse, der strømliner agentudvikling og oprettelse af AI-applikationer. Værktøjet tilbyder omfattende funktioner til at udforske, evaluere og implementere AI-modeller fra en bred vifte af udbydere—herunder Anthropic, OpenAI, GitHub, Google—samt understøttelse af lokal modelkørsel ved hjælp af ONNX og Ollama.

Det, der adskiller AI Toolkit, er dets omfattende tilgang til hele AI-udviklingslivscyklussen. I modsætning til traditionelle AI-udviklingsværktøjer, der fokuserer på enkelte aspekter, tilbyder AI Toolkit et integreret miljø, der dækker modelopdagelse, eksperimentering, agentudvikling, evaluering og implementering—alt sammen inden for det velkendte VS Code-miljø.

Platformen er specifikt designet til hurtig prototyping og produktionsimplementering med funktioner som promptgenerering, hurtige startere, problemfri MCP (Model Context Protocol) værktøjsintegrationer og omfattende evalueringsmuligheder. For Edge AI-udvikling betyder det, at du effektivt kan udvikle, teste og optimere AI-applikationer til edge-implementeringsscenarier, mens du opretholder den fulde udviklingsproces inden for VS Code.

## Læringsmål

Ved afslutningen af denne guide vil du være i stand til:

### Kernekompetencer
- **Installere og konfigurere** AI Toolkit til Visual Studio Code til Edge AI-udviklingsarbejdsgange
- **Navigere og anvende** AI Toolkit-grænsefladen, herunder Model Catalog, Playground og Agent Builder
- **Udvælge og evaluere** AI-modeller, der er egnede til edge-implementering baseret på ydeevne og ressourcebegrænsninger
- **Konvertere og optimere** modeller ved hjælp af ONNX-format og kvantiseringsteknikker til edge-enheder

### Edge AI Udviklingsfærdigheder
- **Designe og implementere** Edge AI-applikationer ved hjælp af det integrerede udviklingsmiljø
- **Udføre modeltest** under edge-lignende forhold ved hjælp af lokal inferens og ressourceovervågning
- **Oprette og tilpasse** AI-agenter optimeret til edge-implementeringsscenarier
- **Evaluere modelydelse** ved hjælp af metrics, der er relevante for edge computing (latens, hukommelsesforbrug, nøjagtighed)

### Optimering og Implementering
- **Anvende kvantisering og beskæring** teknikker til at reducere modelstørrelse, mens acceptabel ydeevne opretholdes
- **Optimere modeller** til specifikke edge-hardwareplatforme, herunder CPU, GPU og NPU-acceleration
- **Implementere bedste praksis** for edge AI-udvikling, herunder ressourcehåndtering og fallback-strategier
- **Forberede modeller og applikationer** til produktionsimplementering på edge-enheder

### Avancerede Edge AI Begreber
- **Integrere med edge AI-rammer** herunder ONNX Runtime, Windows ML og TensorFlow Lite
- **Implementere multi-model arkitekturer** og federerede læringsscenarier til edge-miljøer
- **Fejlsøge almindelige edge AI-problemer** herunder hukommelsesbegrænsninger, inferenshastighed og hardwarekompatibilitet
- **Designe overvågnings- og logningsstrategier** til edge AI-applikationer i produktion

### Praktisk Anvendelse
- **Bygge end-to-end Edge AI-løsninger** fra modeludvælgelse til implementering
- **Demonstrere færdigheder** i edge-specifikke udviklingsarbejdsgange og optimeringsteknikker
- **Anvende lærte begreber** til virkelige edge AI-brugsscenarier, herunder IoT, mobile og indlejrede applikationer
- **Evaluere og sammenligne** forskellige edge AI-implementeringsstrategier og deres kompromiser

## Nøglefunktioner til Edge AI Udvikling

### 1. Modelkatalog og Opdagelse
- **Multi-udbyder Support**: Gennemse og få adgang til AI-modeller fra Anthropic, OpenAI, GitHub, Google og andre udbydere
- **Lokal Modelintegration**: Forenklet opdagelse af ONNX og Ollama-modeller til edge-implementering
- **GitHub Modeller**: Direkte integration med GitHubs modelhosting for strømlinet adgang
- **Model Sammenligning**: Sammenlign modeller side om side for at finde optimal balance for edge-enhedens begrænsninger

### 2. Interaktiv Playground
- **Interaktiv Testmiljø**: Hurtig eksperimentering med modelkapaciteter i et kontrolleret miljø
- **Multi-modal Support**: Test med billeder, tekst og andre input typiske for edge-scenarier
- **Realtids Eksperimentering**: Øjeblikkelig feedback på modelrespons og ydeevne
- **Parameteroptimering**: Finjuster modelparametre til edge-implementeringskrav

### 3. Prompt (Agent) Builder
- **Naturlig Sprog Generering**: Generer startprompter ved hjælp af naturlige sprog beskrivelser
- **Iterativ Forfining**: Forbedr prompter baseret på modelrespons og ydeevne
- **Opgave Nedbrydning**: Opdel komplekse opgaver med promptkæder og strukturerede output
- **Variabel Support**: Brug variabler i prompter for dynamisk agentadfærd
- **Produktionskode Generering**: Generer produktionsklar kode til hurtig appudvikling

### 4. Bulk Kørsel og Evaluering
- **Multi-model Testning**: Udfør flere prompter på tværs af udvalgte modeller samtidigt
- **Effektiv Testning i Skala**: Test forskellige input og konfigurationer effektivt
- **Brugerdefinerede Test Cases**: Kør agenter med test cases for at validere funktionalitet
- **Ydelsessammenligning**: Sammenlign resultater på tværs af forskellige modeller og konfigurationer

### 5. Model Evaluering med Datasets
- **Standard Metrics**: Test AI-modeller ved hjælp af indbyggede evaluatorer (F1-score, relevans, lighed, sammenhæng)
- **Brugerdefinerede Evaluatorer**: Opret dine egne evalueringsmetrics til specifikke brugsscenarier
- **Dataset Integration**: Test modeller mod omfattende datasets
- **Ydelsesmåling**: Kvantificer modelydelse til edge-implementeringsbeslutninger

### 6. Finjusteringsmuligheder
- **Modeltilpasning**: Tilpas modeller til specifikke brugsscenarier og domæner
- **Specialiseret Tilpasning**: Tilpas modeller til specialiserede domæner og krav
- **Edge Optimering**: Finjuster modeller specifikt til edge-implementeringsbegrænsninger
- **Domænespecifik Træning**: Opret modeller skræddersyet til specifikke edge-brugsscenarier

### 7. MCP Værktøjsintegration
- **Ekstern Værktøjsforbindelse**: Forbind agenter til eksterne værktøjer via Model Context Protocol-servere
- **Reelle Handlinger**: Gør det muligt for agenter at forespørge databaser, få adgang til API'er eller udføre brugerdefineret logik
- **Eksisterende MCP Servere**: Brug værktøjer fra kommando (stdio) eller HTTP (server-sent event) protokoller
- **Brugerdefineret MCP Udvikling**: Byg og opret nye MCP-servere med test i Agent Builder

### 8. Agentudvikling og Testning
- **Funktion Kald Support**: Gør det muligt for agenter at kalde eksterne funktioner dynamisk
- **Realtids Integrationstest**: Test integrationer med realtidskørsler og værktøjsbrug
- **Agent Versionering**: Versionskontrol for agenter med sammenligningsmuligheder for evalueringsresultater
- **Fejlfinding og Sporing**: Lokal sporing og fejlfinding muligheder for agentudvikling

## Edge AI Udviklingsarbejdsgang

### Fase 1: Modelopdagelse og Udvælgelse
1. **Udforsk Modelkatalog**: Brug modelkataloget til at finde modeller, der er egnede til edge-implementering
2. **Sammenlign Ydeevne**: Evaluer modeller baseret på størrelse, nøjagtighed og inferenshastighed
3. **Test Lokalt**: Brug Ollama eller ONNX-modeller til lokal test før edge-implementering
4. **Vurder Ressourcekrav**: Bestem hukommelses- og beregningsbehov for mål-edge-enheder

### Fase 2: Modeloptimering
1. **Konverter til ONNX**: Konverter udvalgte modeller til ONNX-format for edge-kompatibilitet
2. **Anvend Kvantisering**: Reducer modelstørrelse gennem INT8 eller INT4 kvantisering
3. **Hardwareoptimering**: Optimer til mål-edge-hardware (ARM, x86, specialiserede acceleratorer)
4. **Ydelsesvalidering**: Valider, at optimerede modeller opretholder acceptabel nøjagtighed

### Fase 3: Applikationsudvikling
1. **Agentdesign**: Brug Agent Builder til at skabe edge-optimerede AI-agenter
2. **Prompt Engineering**: Udvikl prompter, der fungerer effektivt med mindre edge-modeller
3. **Integrationstest**: Test agenter under simulerede edge-forhold
4. **Kodegenerering**: Generer produktionskode optimeret til edge-implementering

### Fase 4: Evaluering og Testning
1. **Batch Evaluering**: Test flere konfigurationer for at finde optimale edge-indstillinger
2. **Ydelsesprofilering**: Analyser inferenshastighed, hukommelsesforbrug og nøjagtighed
3. **Edge-simulering**: Test under forhold, der ligner mål-edge-implementeringsmiljøet
4. **Stress Testning**: Evaluer ydeevne under forskellige belastningsforhold

### Fase 5: Implementeringsforberedelse
1. **Endelig Optimering**: Anvend endelige optimeringer baseret på testresultater
2. **Implementeringspakning**: Pak modeller og kode til edge-implementering
3. **Dokumentation**: Dokumenter implementeringskrav og konfiguration
4. **Overvågningsopsætning**: Forbered overvågning og logning til edge-implementering

## Målgruppe for Edge AI Udvikling

### Edge AI Udviklere
- Applikationsudviklere, der bygger AI-drevne edge-enheder og IoT-løsninger
- Udviklere af indlejrede systemer, der integrerer AI-funktioner i ressourcebegrænsede enheder
- Mobiludviklere, der skaber AI-applikationer på enheder som smartphones og tablets

### Edge AI Ingeniører
- AI-ingeniører, der optimerer modeller til edge-implementering og administrerer inferens-pipelines
- DevOps-ingeniører, der implementerer og administrerer AI-modeller på tværs af distribueret edge-infrastruktur
- Ydelsesingeniører, der optimerer AI-arbejdsgange til edge-hardwarebegrænsninger

### Forskere og Undervisere
- AI-forskere, der udvikler effektive modeller og algoritmer til edge computing
- Undervisere, der underviser i edge AI-begreber og demonstrerer optimeringsteknikker
- Studerende, der lærer om udfordringer og løsninger i edge AI-implementering

## Edge AI Brugsscenarier

### Smarte IoT-enheder
- **Realtids Billedgenkendelse**: Implementer computer vision-modeller på IoT-kameraer og sensorer
- **Stemmegengivelse**: Implementer talegenkendelse og naturlig sprogbehandling på smarte højttalere
- **Prædiktiv Vedligeholdelse**: Kør modeller til detektering af afvigelser på industrielle edge-enheder
- **Miljøovervågning**: Implementer modeller til analyse af sensordata for miljøapplikationer

### Mobile og Indlejrede Applikationer
- **Oversættelse på Enhed**: Implementer sprogoversættelsesmodeller, der fungerer offline
- **Augmented Reality**: Implementer realtids objektgenkendelse og sporing til AR-applikationer
- **Sundhedsovervågning**: Kør sundhedsanalysemodeller på wearables og medicinsk udstyr
- **Autonome Systemer**: Implementer beslutningsmodeller til droner, robotter og køretøjer

### Edge Computing Infrastruktur
- **Edge Datacentre**: Implementer AI-modeller i edge-datacentre for lav-latens applikationer
- **CDN Integration**: Integrer AI-behandlingsfunktioner i content delivery-netværk
- **5G Edge**: Udnyt 5G edge computing til AI-drevne applikationer
- **Fog Computing**: Implementer AI-behandling i fog computing-miljøer

## Installation og Opsætning

### Installation af Udvidelse
Installer AI Toolkit-udvidelsen direkte fra Visual Studio Code Marketplace:

**Udvidelses-ID**: `ms-windows-ai-studio.windows-ai-studio`

**Installationsmetoder**:
1. **VS Code Marketplace**: Søg efter "AI Toolkit" i Extensions-visningen
2. **Kommandolinje**: `code --install-extension ms-windows-ai-studio.windows-ai-studio`
3. **Direkte Installation**: Download fra [VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)

### Forudsætninger for Edge AI Udvikling
- **Visual Studio Code**: Seneste version anbefales
- **Python Miljø**: Python 3.8+ med nødvendige AI-biblioteker
- **ONNX Runtime** (Valgfrit): Til ONNX-modelinferens
- **Ollama** (Valgfrit): Til lokal modelservering
- **Hardware Acceleration Tools**: CUDA, OpenVINO eller platform-specifikke acceleratorer

### Indledende Konfiguration
1. **Aktivering af Udvidelse**: Åbn VS Code og verificer, at AI Toolkit vises i Activity Bar
2. **Modeludbyder Opsætning**: Konfigurer adgang til GitHub, OpenAI, Anthropic eller andre modeludbydere
3. **Lokalt Miljø**: Opsæt Python-miljø og installer nødvendige pakker
4. **Hardware Acceleration**: Konfigurer GPU/NPU-acceleration, hvis tilgængelig
5. **MCP Integration**: Opsæt Model Context Protocol-servere, hvis nødvendigt

### Førstegangs Opsætningscheckliste
- [ ] AI Toolkit-udvidelse installeret og aktiveret
- [ ] Modelkatalog tilgængeligt og modeller opdagelige
- [ ] Playground funktionel til modeltestning
- [ ] Agent Builder tilgængelig til promptudvikling
- [ ] Lokalt udviklingsmiljø konfigureret
- [ ] Hardwareacceleration (hvis tilgængelig) korrekt konfigureret

## Kom i Gang med AI Toolkit

### Hurtig Start Guide

Vi anbefaler at starte med modeller, der hostes af GitHub, for den mest strømlinede oplevelse:

1. **Installation**: Følg [installationsguiden](https://code.visualstudio.com/docs/intelligentapps/overview#_install-and-setup) for at opsætte AI Toolkit på din enhed
2. **Modelopdagelse**: Fra udvidelsens trævisning, vælg **CATALOG > Models** for at udforske tilgængelige modeller
3. **GitHub Modeller**: Start med modeller hostet af GitHub for optimal integration
4. **Playground Testning**: Fra enhver modelkort, vælg **Try in Playground** for at begynde at eksperimentere med modelkapaciteter

### Trin-for-Trin Edge AI Udvikling

#### Trin 1: Modelopdagelse og Udvælgelse
1. Åbn AI Toolkit-visningen i VS Code Activity Bar
2. Gennemse Model Catalog for modeller, der er egnede til edge-implementering
3. Filtrer efter udbyder (GitHub, ON
2. Generer startprompter ved hjælp af naturlige sprog beskrivelser  
3. Iterer og forfin prompter baseret på modelrespons  
4. Integrer MCP-værktøjer for forbedrede agentfunktioner  

#### Trin 3: Test og Evaluering  
1. Brug **Bulk Run** til at teste flere prompter på tværs af udvalgte modeller  
2. Kør agenter med testcases for at validere funktionalitet  
3. Evaluer nøjagtighed og ydeevne ved hjælp af indbyggede eller brugerdefinerede metrikker  
4. Sammenlign forskellige modeller og konfigurationer  

#### Trin 4: Finjustering og Optimering  
1. Tilpas modeller til specifikke edge-brugsscenarier  
2. Anvend domænespecifik finjustering  
3. Optimer til edge-implementeringsbegrænsninger  
4. Versionér og sammenlign forskellige agentkonfigurationer  

#### Trin 5: Forberedelse til Implementering  
1. Generer produktionsklar kode ved hjælp af Agent Builder  
2. Opsæt MCP-serverforbindelser til produktionsbrug  
3. Forbered implementeringspakker til edge-enheder  
4. Konfigurer overvågnings- og evalueringsmetrikker  

## Eksempler til AI Toolkit  

Prøv vores eksempler  
[AI Toolkit-eksemplerne](https://github.com/Azure-Samples/AI_Toolkit_Samples) er designet til at hjælpe udviklere og forskere med effektivt at udforske og implementere AI-løsninger.  

Vores eksempler inkluderer:  

Eksempelkode: Forudbyggede eksempler, der demonstrerer AI-funktioner som træning, implementering eller integration af modeller i applikationer.  
Dokumentation: Vejledninger og tutorials, der hjælper brugere med at forstå AI Toolkit-funktioner og hvordan man bruger dem.  
Forudsætninger  

- Visual Studio Code  
- AI Toolkit til Visual Studio Code  
- GitHub Fine-grained personal access token (PAT)  
- Foundry Local  

## Bedste praksis for Edge AI-udvikling  

### Modelvalg  
- **Størrelsesbegrænsninger**: Vælg modeller, der passer inden for hukommelsesbegrænsningerne på mål-enheder  
- **Inferenshastighed**: Prioriter modeller med hurtig inferens til realtidsapplikationer  
- **Nøjagtighedsafvejninger**: Balancer modelnøjagtighed med ressourcebegrænsninger  
- **Formatkompatibilitet**: Foretræk ONNX eller hardwareoptimerede formater til edge-implementering  

### Optimeringsteknikker  
- **Kvantisering**: Brug INT8 eller INT4 kvantisering til at reducere modelstørrelse og forbedre hastighed  
- **Pruning**: Fjern unødvendige modelparametre for at reducere beregningskrav  
- **Knowledge Distillation**: Skab mindre modeller, der opretholder ydeevnen fra større modeller  
- **Hardwareacceleration**: Udnyt NPUs, GPUs eller specialiserede acceleratorer, når det er muligt  

### Udviklingsworkflow  
- **Iterativ test**: Test ofte under edge-lignende forhold under udvikling  
- **Ydelsesovervågning**: Overvåg løbende ressourceforbrug og inferenshastighed  
- **Versionskontrol**: Spor modelversioner og optimeringsindstillinger  
- **Dokumentation**: Dokumentér alle optimeringsbeslutninger og afvejninger i ydeevne  

### Implementeringsovervejelser  
- **Ressourceovervågning**: Overvåg hukommelse, CPU og strømforbrug i produktion  
- **Fallback-strategier**: Implementer fallback-mekanismer for modelfejl  
- **Opdateringsmekanismer**: Planlæg modelopdateringer og versionsstyring  
- **Sikkerhed**: Implementer passende sikkerhedsforanstaltninger for edge AI-applikationer  

## Integration med Edge AI-rammer  

### ONNX Runtime  
- **Cross-platform implementering**: Implementer ONNX-modeller på tværs af forskellige edge-platforme  
- **Hardwareoptimering**: Udnyt ONNX Runtimes hardware-specifikke optimeringer  
- **Mobil support**: Brug ONNX Runtime Mobile til smartphone- og tabletapplikationer  
- **IoT-integration**: Implementer på IoT-enheder ved hjælp af ONNX Runtimes letvægtsdistributioner  

### Windows ML  
- **Windows-enheder**: Optimer til Windows-baserede edge-enheder og PC'er  
- **NPU-acceleration**: Udnyt Neural Processing Units på Windows-enheder  
- **DirectML**: Brug DirectML til GPU-acceleration på Windows-platforme  
- **UWP-integration**: Integrer med Universal Windows Platform-applikationer  

### TensorFlow Lite  
- **Mobiloptimering**: Implementer TensorFlow Lite-modeller på mobile og indlejrede enheder  
- **Hardwaredelegeringer**: Brug specialiserede hardwaredelegeringer til acceleration  
- **Mikrocontrollere**: Implementer på mikrocontrollere ved hjælp af TensorFlow Lite Micro  
- **Cross-platform support**: Implementer på tværs af Android, iOS og indlejrede Linux-systemer  

### Azure IoT Edge  
- **Cloud-Edge hybrid**: Kombiner cloud-træning med edge-inferens  
- **Modulimplementering**: Implementer AI-modeller som IoT Edge-moduler  
- **Enhedsstyring**: Administrer edge-enheder og modelopdateringer eksternt  
- **Telemetri**: Indsaml ydeevnedata og modelmetrikker fra edge-implementeringer  

## Avancerede Edge AI-scenarier  

### Multi-model implementering  
- **Modelensembler**: Implementer flere modeller for forbedret nøjagtighed eller redundans  
- **A/B-test**: Test forskellige modeller samtidig på edge-enheder  
- **Dynamisk valg**: Vælg modeller baseret på aktuelle enhedsbetingelser  
- **Ressourcedeling**: Optimer ressourceforbrug på tværs af flere implementerede modeller  

### Federated Learning  
- **Distribueret træning**: Træn modeller på tværs af flere edge-enheder  
- **Privatlivsbeskyttelse**: Hold træningsdata lokalt, mens modelforbedringer deles  
- **Samarbejdende læring**: Gør det muligt for enheder at lære af kollektive erfaringer  
- **Edge-Cloud koordinering**: Koordiner læring mellem edge-enheder og cloud-infrastruktur  

### Realtidsbehandling  
- **Stream-behandling**: Behandl kontinuerlige datastrømme på edge-enheder  
- **Lav-latens inferens**: Optimer for minimal inferenslatens  
- **Batch-behandling**: Effektivt behandle batches af data på edge-enheder  
- **Adaptiv behandling**: Juster behandling baseret på aktuelle enhedskapaciteter  

## Fejlfinding af Edge AI-udvikling  

### Almindelige problemer  
- **Hukommelsesbegrænsninger**: Model for stor til mål-enhedens hukommelse  
- **Inferenshastighed**: Modelinferens for langsom til realtidskrav  
- **Nøjagtighedsforringelse**: Optimering reducerer modelnøjagtighed uacceptabelt  
- **Hardwarekompatibilitet**: Model ikke kompatibel med mål-hardware  

### Fejlsøgningsstrategier  
- **Ydelsesprofilering**: Brug AI Toolkits sporingsfunktioner til at identificere flaskehalse  
- **Ressourceovervågning**: Overvåg hukommelse og CPU-forbrug under udvikling  
- **Inkrementel test**: Test optimeringer inkrementelt for at isolere problemer  
- **Hardwaresimulering**: Brug udviklingsværktøjer til at simulere mål-hardware  

### Optimeringsløsninger  
- **Mere kvantisering**: Anvend mere aggressive kvantiseringsteknikker  
- **Modelarkitektur**: Overvej forskellige modelarkitekturer optimeret til edge  
- **Forbehandlingsoptimering**: Optimer databehandling til edge-begrænsninger  
- **Inferensoptimering**: Brug hardware-specifikke inferensoptimeringer  

## Ressourcer og næste skridt  

### Officiel dokumentation  
- [AI Toolkit Developer Documentation](https://aka.ms/AIToolkit/doc)  
- [Installations- og opsætningsguide](https://code.visualstudio.com/docs/intelligentapps/overview#_install-and-setup)  
- [VS Code Intelligent Apps Dokumentation](https://code.visualstudio.com/docs/intelligentapps)  
- [Model Context Protocol (MCP) Dokumentation](https://modelcontextprotocol.io/)  

### Fællesskab og support  
- [AI Toolkit GitHub Repository](https://github.com/microsoft/vscode-ai-toolkit)  
- [GitHub Issues og funktionsanmodninger](https://aka.ms/AIToolkit/feedback)  
- [Azure AI Foundry Discord Community](https://aka.ms/azureaifoundry/discord)  
- [VS Code Extension Marketplace](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)  

### Tekniske ressourcer  
- [ONNX Runtime Dokumentation](https://onnxruntime.ai/)  
- [Ollama Dokumentation](https://ollama.ai/)  
- [Windows ML Dokumentation](https://docs.microsoft.com/en-us/windows/ai/)  
- [Azure AI Foundry Dokumentation](https://learn.microsoft.com/en-us/azure/ai-foundry/)  

### Læringsveje  
- [Edge AI Fundamentals Kursus](../Module01/README.md)  
- [Small Language Models Guide](../Module02/README.md)  
- [Edge Implementeringsstrategier](../Module03/README.md)  
- [Windows Edge AI Udvikling](./windowdeveloper.md)  

### Yderligere ressourcer  
- **Repository-statistik**: 1.8k+ stjerner, 150+ forks, 18+ bidragydere  
- **Licens**: MIT-licens  
- **Sikkerhed**: Microsofts sikkerhedspolitikker gælder  
- **Telemetri**: Respekterer VS Code telemetriindstillinger  

## Konklusion  

AI Toolkit til Visual Studio Code repræsenterer en omfattende platform for moderne AI-udvikling, der tilbyder strømlinede agentudviklingsfunktioner, som er særligt værdifulde for Edge AI-applikationer. Med sin omfattende modelkatalog, der understøtter udbydere som Anthropic, OpenAI, GitHub og Google, kombineret med lokal eksekvering via ONNX og Ollama, tilbyder værktøjet den fleksibilitet, der er nødvendig for forskellige edge-implementeringsscenarier.  

Værktøjets styrke ligger i dets integrerede tilgang—fra modelopdagelse og eksperimentering i Playground til sofistikeret agentudvikling med Prompt Builder, omfattende evalueringsmuligheder og problemfri MCP-værktøjsintegration. For Edge AI-udviklere betyder dette hurtig prototyping og test af AI-agenter før edge-implementering, med mulighed for hurtigt at iterere og optimere til ressourcebegrænsede miljøer.  

Nøglefordele for Edge AI-udvikling inkluderer:  
- **Hurtig eksperimentering**: Test modeller og agenter hurtigt før edge-implementering  
- **Multi-udbyder fleksibilitet**: Adgang til modeller fra forskellige kilder for at finde optimale edge-løsninger  
- **Lokal udvikling**: Test med ONNX og Ollama for offline og privatlivsbevarende udvikling  
- **Produktionsklarhed**: Generer produktionsklar kode og integrer med eksterne værktøjer via MCP  
- **Omfattende evaluering**: Brug indbyggede og brugerdefinerede metrikker til at validere edge AI-ydeevne  

Efterhånden som AI fortsætter med at bevæge sig mod edge-implementeringsscenarier, tilbyder AI Toolkit til VS Code det udviklingsmiljø og workflow, der er nødvendigt for at bygge, teste og optimere intelligente applikationer til ressourcebegrænsede miljøer. Uanset om du udvikler IoT-løsninger, mobile AI-applikationer eller indlejrede intelligenssystemer, understøtter værktøjets omfattende funktionssæt og integrerede workflow hele edge AI-udviklingslivscyklussen.  

Med løbende udvikling og et aktivt fællesskab (1.8k+ GitHub-stjerner) forbliver AI Toolkit i frontlinjen af AI-udviklingsværktøjer og udvikler sig kontinuerligt for at imødekomme behovene hos moderne AI-udviklere, der bygger til edge-implementeringsscenarier.  

[Next Foundry Local](./foundrylocal.md)  

---

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal det bemærkes, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi er ikke ansvarlige for eventuelle misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
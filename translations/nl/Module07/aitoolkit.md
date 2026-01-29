# AI Toolkit voor Visual Studio Code - Edge AI Ontwikkelingsgids

## Introductie

Welkom bij de uitgebreide gids voor het gebruik van AI Toolkit voor Visual Studio Code in Edge AI-ontwikkeling. Nu kunstmatige intelligentie verschuift van gecentraliseerde cloud computing naar gedistribueerde edge-apparaten, hebben ontwikkelaars krachtige, geïntegreerde tools nodig die de unieke uitdagingen van edge-implementatie aankunnen - van beperkte middelen tot vereisten voor offline werking.

AI Toolkit voor Visual Studio Code overbrugt deze kloof door een complete ontwikkelomgeving te bieden die specifiek is ontworpen voor het bouwen, testen en optimaliseren van AI-toepassingen die efficiënt draaien op edge-apparaten. Of je nu ontwikkelt voor IoT-sensoren, mobiele apparaten, embedded systemen of edge-servers, deze toolkit stroomlijnt je hele ontwikkelworkflow binnen de vertrouwde VS Code-omgeving.

Deze gids neemt je mee door de essentiële concepten, tools en best practices om AI Toolkit in je Edge AI-projecten te benutten, van de initiële modelselectie tot productie-implementatie.

## Overzicht

AI Toolkit voor Visual Studio Code is een krachtige extensie die agentontwikkeling en het creëren van AI-toepassingen vereenvoudigt. De toolkit biedt uitgebreide mogelijkheden voor het verkennen, evalueren en implementeren van AI-modellen van een breed scala aan providers—waaronder Anthropic, OpenAI, GitHub, Google—terwijl lokale modeluitvoering wordt ondersteund met ONNX en Ollama.

Wat AI Toolkit onderscheidt, is de uitgebreide aanpak van de hele AI-ontwikkelingscyclus. In tegenstelling tot traditionele AI-ontwikkeltools die zich richten op afzonderlijke aspecten, biedt AI Toolkit een geïntegreerde omgeving die modelontdekking, experimentatie, agentontwikkeling, evaluatie en implementatie omvat—alles binnen de vertrouwde VS Code-omgeving.

Het platform is specifiek ontworpen voor snelle prototyping en productie-implementatie, met functies zoals promptgeneratie, snelle starters, naadloze MCP (Model Context Protocol) toolintegraties en uitgebreide evaluatiemogelijkheden. Voor Edge AI-ontwikkeling betekent dit dat je efficiënt AI-toepassingen kunt ontwikkelen, testen en optimaliseren voor edge-implementatiescenario's, terwijl je de volledige ontwikkelworkflow binnen VS Code behoudt.

## Leerdoelen

Aan het einde van deze gids kun je:

### Kerncompetenties
- **Installeren en configureren** van AI Toolkit voor Visual Studio Code voor Edge AI-ontwikkelingsworkflows
- **Navigeren en gebruiken** van de AI Toolkit-interface, inclusief Model Catalog, Playground en Agent Builder
- **Selecteren en evalueren** van AI-modellen die geschikt zijn voor edge-implementatie op basis van prestaties en resourcebeperkingen
- **Converteren en optimaliseren** van modellen met behulp van ONNX-formaat en kwantiseringstechnieken voor edge-apparaten

### Edge AI Ontwikkelingsvaardigheden
- **Ontwerpen en implementeren** van Edge AI-toepassingen met de geïntegreerde ontwikkelomgeving
- **Modeltesten uitvoeren** in edge-achtige omstandigheden met lokale inferentie en resourcebewaking
- **AI-agents creëren en aanpassen** die geoptimaliseerd zijn voor edge-implementatiescenario's
- **Modelprestaties evalueren** met behulp van relevante metrics voor edge computing (latentie, geheugengebruik, nauwkeurigheid)

### Optimalisatie en Implementatie
- **Kwantisering en snoei toepassen** om de modelgrootte te verkleinen terwijl acceptabele prestaties behouden blijven
- **Modellen optimaliseren** voor specifieke edge-hardwareplatforms, inclusief CPU-, GPU- en NPU-versnelling
- **Best practices implementeren** voor Edge AI-ontwikkeling, inclusief resourcebeheer en fallback-strategieën
- **Modellen en toepassingen voorbereiden** voor productie-implementatie op edge-apparaten

### Geavanceerde Edge AI Concepten
- **Integreren met edge AI-frameworks** zoals ONNX Runtime, Windows ML en TensorFlow Lite
- **Multi-model architecturen en federatieve leeromgevingen implementeren** voor edge-omgevingen
- **Veelvoorkomende Edge AI-problemen oplossen** zoals geheugenbeperkingen, inferentiesnelheid en hardwarecompatibiliteit
- **Monitoring- en logstrategieën ontwerpen** voor Edge AI-toepassingen in productie

### Praktische Toepassing
- **End-to-end Edge AI-oplossingen bouwen** van modelselectie tot implementatie
- **Bekwaamheid demonstreren** in edge-specifieke ontwikkelworkflows en optimalisatietechnieken
- **Geleerde concepten toepassen** op real-world Edge AI-gebruiksscenario's, waaronder IoT, mobiel en embedded toepassingen
- **Verschillende Edge AI-implementatiestrategieën evalueren en vergelijken** en hun afwegingen

## Belangrijke Functies voor Edge AI Ontwikkeling

### 1. Modelcatalogus en Ontdekking
- **Multi-provider ondersteuning**: Blader door en krijg toegang tot AI-modellen van Anthropic, OpenAI, GitHub, Google en andere providers
- **Lokale modelintegratie**: Vereenvoudigde ontdekking van ONNX- en Ollama-modellen voor edge-implementatie
- **GitHub-modellen**: Directe integratie met GitHub's modelhosting voor gestroomlijnde toegang
- **Modelvergelijking**: Vergelijk modellen naast elkaar om een optimale balans te vinden voor edge-apparaatbeperkingen

### 2. Interactieve Playground
- **Interactieve testomgeving**: Snel experimenteren met modelmogelijkheden in een gecontroleerde omgeving
- **Multimodale ondersteuning**: Testen met afbeeldingen, tekst en andere inputs die typisch zijn in edge-scenario's
- **Realtime experimentatie**: Directe feedback op modelreacties en prestaties
- **Parameteroptimalisatie**: Fijn afstemmen van modelparameters voor edge-implementatievereisten

### 3. Prompt (Agent) Builder
- **Natuurlijke taal generatie**: Genereer startprompts met behulp van beschrijvingen in natuurlijke taal
- **Iteratieve verfijning**: Verbeter prompts op basis van modelreacties en prestaties
- **Taakdecompositie**: Complexe taken opsplitsen met prompt chaining en gestructureerde outputs
- **Variabele ondersteuning**: Gebruik variabelen in prompts voor dynamisch agentgedrag
- **Productiecode generatie**: Genereer productieklare code voor snelle app-ontwikkeling

### 4. Bulkuitvoering en Evaluatie
- **Multi-model testen**: Voer meerdere prompts uit op geselecteerde modellen tegelijkertijd
- **Efficiënt testen op schaal**: Test verschillende inputs en configuraties efficiënt
- **Aangepaste testcases**: Voer agents uit met testcases om functionaliteit te valideren
- **Prestatievergelijking**: Vergelijk resultaten tussen verschillende modellen en configuraties

### 5. Modelevaluatie met datasets
- **Standaard metrics**: Test AI-modellen met ingebouwde evaluatoren (F1-score, relevantie, gelijkenis, samenhang)
- **Aangepaste evaluatoren**: Maak je eigen evaluatiemetrics voor specifieke gebruiksscenario's
- **Datasetintegratie**: Test modellen tegen uitgebreide datasets
- **Prestatiemeting**: Kwantificeer modelprestaties voor edge-implementatiebeslissingen

### 6. Fine-tuning mogelijkheden
- **Modelaanpassing**: Pas modellen aan voor specifieke gebruiksscenario's en domeinen
- **Gespecialiseerde aanpassing**: Pas modellen aan gespecialiseerde domeinen en vereisten
- **Edge-optimalisatie**: Fine-tune modellen specifiek voor edge-implementatiebeperkingen
- **Domeinspecifieke training**: Maak modellen die zijn afgestemd op specifieke edge-gebruiksscenario's

### 7. MCP Tool Integratie
- **Externe toolconnectiviteit**: Verbind agents met externe tools via Model Context Protocol-servers
- **Acties in de echte wereld**: Stel agents in staat om databases te raadplegen, API's te openen of aangepaste logica uit te voeren
- **Bestaande MCP-servers**: Gebruik tools van command (stdio) of HTTP (server-sent event) protocollen
- **Aangepaste MCP-ontwikkeling**: Bouw en scaffold nieuwe MCP-servers met testen in Agent Builder

### 8. Agentontwikkeling en Testen
- **Ondersteuning voor functieaanroepen**: Stel agents in staat om dynamisch externe functies aan te roepen
- **Realtime integratietesten**: Test integraties met realtime runs en toolgebruik
- **Agentversiebeheer**: Versiebeheer voor agents met vergelijkingsmogelijkheden voor evaluatieresultaten
- **Debugging en tracing**: Lokale tracing en debuggingmogelijkheden voor agentontwikkeling

## Edge AI Ontwikkelingsworkflow

### Fase 1: Modelontdekking en Selectie
1. **Verken Modelcatalogus**: Gebruik de modelcatalogus om modellen te vinden die geschikt zijn voor edge-implementatie
2. **Vergelijk Prestaties**: Evalueer modellen op basis van grootte, nauwkeurigheid en inferentiesnelheid
3. **Test Locaal**: Gebruik Ollama of ONNX-modellen om lokaal te testen voordat je naar edge implementeert
4. **Beoordeel Resourcevereisten**: Bepaal geheugen- en rekeneisen voor doel-edge-apparaten

### Fase 2: Modeloptimalisatie
1. **Converteer naar ONNX**: Converteer geselecteerde modellen naar ONNX-formaat voor edge-compatibiliteit
2. **Pas Kwantisering toe**: Verminder modelgrootte via INT8- of INT4-kwantisering
3. **Hardwareoptimalisatie**: Optimaliseer voor doel-edge-hardware (ARM, x86, gespecialiseerde versnellers)
4. **Prestaties Valideren**: Valideer geoptimaliseerde modellen om acceptabele nauwkeurigheid te behouden

### Fase 3: Applicatieontwikkeling
1. **Agentontwerp**: Gebruik Agent Builder om edge-geoptimaliseerde AI-agents te creëren
2. **Prompt Engineering**: Ontwikkel prompts die effectief werken met kleinere edge-modellen
3. **Integratietesten**: Test agents in gesimuleerde edge-omstandigheden
4. **Code Generatie**: Genereer productiecode geoptimaliseerd voor edge-implementatie

### Fase 4: Evaluatie en Testen
1. **Batch Evaluatie**: Test meerdere configuraties om optimale edge-instellingen te vinden
2. **Prestatieprofilering**: Analyseer inferentiesnelheid, geheugengebruik en nauwkeurigheid
3. **Edge Simulatie**: Test in omstandigheden die vergelijkbaar zijn met de doel-edge-implementatieomgeving
4. **Stress Testen**: Evalueer prestaties onder verschillende belastingomstandigheden

### Fase 5: Implementatievoorbereiding
1. **Eindoptimalisatie**: Pas eindoptimalisaties toe op basis van testresultaten
2. **Implementatieverpakking**: Verpak modellen en code voor edge-implementatie
3. **Documentatie**: Documenteer implementatievereisten en configuratie
4. **Monitoring Setup**: Bereid monitoring en logging voor edge-implementatie voor

## Doelgroep voor Edge AI Ontwikkeling

### Edge AI Ontwikkelaars
- Applicatieontwikkelaars die AI-aangedreven edge-apparaten en IoT-oplossingen bouwen
- Embedded systeemontwikkelaars die AI-mogelijkheden integreren in apparaten met beperkte middelen
- Mobiele ontwikkelaars die on-device AI-toepassingen maken voor smartphones en tablets

### Edge AI Ingenieurs
- AI-ingenieurs die modellen optimaliseren voor edge-implementatie en inferentie-pijplijnen beheren
- DevOps-ingenieurs die AI-modellen implementeren en beheren in gedistribueerde edge-infrastructuur
- Prestatie-ingenieurs die AI-workloads optimaliseren voor edge-hardwarebeperkingen

### Onderzoekers en Educators
- AI-onderzoekers die efficiënte modellen en algoritmen ontwikkelen voor edge computing
- Educators die Edge AI-concepten onderwijzen en optimalisatietechnieken demonstreren
- Studenten die leren over de uitdagingen en oplossingen in edge AI-implementatie

## Edge AI Gebruiksscenario's

### Slimme IoT-apparaten
- **Realtime Beeldherkenning**: Computer vision-modellen implementeren op IoT-camera's en sensoren
- **Stemverwerking**: Spraakherkenning en natuurlijke taalverwerking implementeren op slimme speakers
- **Voorspellend Onderhoud**: Anomaliedetectiemodellen uitvoeren op industriële edge-apparaten
- **Milieubewaking**: Sensor data-analysemodellen implementeren voor milieutoepassingen

### Mobiele en Embedded Toepassingen
- **On-device Vertaling**: Taalvertalingsmodellen implementeren die offline werken
- **Augmented Reality**: Realtime objectherkenning en tracking implementeren voor AR-toepassingen
- **Gezondheidsmonitoring**: Gezondheidsanalysemodellen uitvoeren op draagbare apparaten en medische apparatuur
- **Autonome Systemen**: Besluitvormingsmodellen implementeren voor drones, robots en voertuigen

### Edge Computing Infrastructuur
- **Edge Datacenters**: AI-modellen implementeren in edge-datacenters voor toepassingen met lage latentie
- **CDN Integratie**: AI-verwerkingsmogelijkheden integreren in content delivery netwerken
- **5G Edge**: 5G edge computing benutten voor AI-aangedreven toepassingen
- **Fog Computing**: AI-verwerking implementeren in fog computing-omgevingen

## Installatie en Setup

### Extensie Installatie
Installeer de AI Toolkit-extensie direct vanuit de Visual Studio Code Marketplace:

**Extensie ID**: `ms-windows-ai-studio.windows-ai-studio`

**Installatiemethoden**:
1. **VS Code Marketplace**: Zoek naar "AI Toolkit" in de Extensies-weergave
2. **Command Line**: `code --install-extension ms-windows-ai-studio.windows-ai-studio`
3. **Direct Installeren**: Download van [VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)

### Vereisten voor Edge AI Ontwikkeling
- **Visual Studio Code**: Laatste versie aanbevolen
- **Python-omgeving**: Python 3.8+ met vereiste AI-bibliotheken
- **ONNX Runtime** (Optioneel): Voor ONNX-modelinferentie
- **Ollama** (Optioneel): Voor lokale modelservering
- **Hardwareversnellingstools**: CUDA, OpenVINO of platform-specifieke versnellers

### Initiële Configuratie
1. **Extensie Activering**: Open VS Code en controleer of AI Toolkit verschijnt in de Activiteitenbalk
2. **Modelprovider Setup**: Configureer toegang tot GitHub, OpenAI, Anthropic of andere modelproviders
3. **Lokale Omgeving**: Stel Python-omgeving in en installeer vereiste pakketten
4. **Hardwareversnelling**: Configureer GPU/NPU-versnelling indien beschikbaar
5. **MCP Integratie**: Stel Model Context Protocol-servers in indien nodig

### Checklist voor Eerste Setup
- [ ] AI Toolkit-extensie geïnstalleerd en geactiveerd
- [ ] Modelcatalogus toegankelijk en modellen vindbaar
- [ ] Playground functioneel voor modeltesten
- [ ] Agent Builder toegankelijk voor promptontwikkeling
- [ ] Lokale ontwikkelomgeving geconfigureerd
- [ ] Hardwareversnelling (indien beschikbaar) correct geconfigureerd

## Aan de slag met AI Toolkit

### Snelle Startgids

We raden aan te beginnen met modellen die door GitHub worden gehost voor de meest gestroomlijnde ervaring:

1. **Installatie**: Volg de [installatiegids](https://code.visualstudio.com/docs/intelligentapps/overview#_install-and-setup) om AI Toolkit op je apparaat in te stellen
2. **Modelontdekking**: Selecteer **CATALOG > Models** in de extensieboomweergave om beschikbare modellen te verkennen
3. **GitHub-modellen**: Begin met modellen die door GitHub worden gehost voor optimale integratie
4. **Playground Testen**: Selecteer **Try in Playground** vanuit een modelkaart om te beginnen met experimenteren met modelmogelijkheden

### Stapsgewijze Edge AI Ontwikkeling

#### Stap 1: Modelverkenning en Selectie
1. Open de AI Toolkit-weergave in de VS Code Activiteitenbalk
2. Blader door de Modelcatalogus voor modellen die geschikt zijn voor edge-implementatie
3. Filter op provider (GitHub, ONNX, Ollama) op basis van je edge-vereisten
4. Gebruik **Try in Playground** om modelmogelijkheden direct te testen

#### Stap 2: Agentontwikkeling
1. Gebruik de **Prompt (Agent) Builder** om edge-geoptimaliseerde AI-agents te creëren
2. Genereer startprompts met behulp van natuurlijke taalbeschrijvingen  
3. Itereer en verfijn prompts op basis van modelreacties  
4. Integreer MCP-tools voor verbeterde agentmogelijkheden  

#### Stap 3: Testen en Evaluatie  
1. Gebruik **Bulk Run** om meerdere prompts te testen op geselecteerde modellen  
2. Voer agents uit met testcases om functionaliteit te valideren  
3. Evalueer nauwkeurigheid en prestaties met ingebouwde of aangepaste metrics  
4. Vergelijk verschillende modellen en configuraties  

#### Stap 4: Fine-tuning en Optimalisatie  
1. Pas modellen aan voor specifieke edge use cases  
2. Voer domeinspecifieke fine-tuning uit  
3. Optimaliseer voor beperkingen bij edge-deployment  
4. Versieer en vergelijk verschillende agentconfiguraties  

#### Stap 5: Voorbereiding op Deployment  
1. Genereer productieklare code met de Agent Builder  
2. Stel MCP-serververbindingen in voor productiegebruik  
3. Bereid deploymentpakketten voor edge-apparaten voor  
4. Configureer monitoring- en evaluatiemetrics  

## Voorbeelden voor AI Toolkit  

Probeer Onze Voorbeelden  
De [AI Toolkit-voorbeelden](https://github.com/Azure-Samples/AI_Toolkit_Samples) zijn ontworpen om ontwikkelaars en onderzoekers te helpen AI-oplossingen effectief te verkennen en implementeren.  

Onze voorbeelden omvatten:  

Voorbeeldcode: Vooraf gebouwde voorbeelden om AI-functionaliteiten te demonstreren, zoals het trainen, deployen of integreren van modellen in applicaties.  
Documentatie: Handleidingen en tutorials om gebruikers te helpen de functies van AI Toolkit te begrijpen en te gebruiken.  
Vereisten  

- Visual Studio Code  
- AI Toolkit voor Visual Studio Code  
- GitHub Fine-grained personal access token (PAT)  
- Foundry Local  

## Best Practices voor Edge AI Ontwikkeling  

### Modelselectie  
- **Beperkingen qua grootte**: Kies modellen die binnen de geheugencapaciteit van doelapparaten passen  
- **Inference snelheid**: Geef prioriteit aan modellen met snelle inference voor realtime toepassingen  
- **Nauwkeurigheid versus middelen**: Vind een balans tussen modelnauwkeurigheid en resourcebeperkingen  
- **Compatibiliteit van formaten**: Geef de voorkeur aan ONNX of hardware-geoptimaliseerde formaten voor edge-deployment  

### Optimalisatietechnieken  
- **Quantisatie**: Gebruik INT8 of INT4 quantisatie om de modelgrootte te verkleinen en snelheid te verbeteren  
- **Pruning**: Verwijder onnodige modelparameters om de rekenvereisten te verminderen  
- **Knowledge Distillation**: Maak kleinere modellen die de prestaties van grotere behouden  
- **Hardwareversnelling**: Maak gebruik van NPUs, GPUs of gespecialiseerde versnellers indien beschikbaar  

### Ontwikkelworkflow  
- **Iteratief testen**: Test regelmatig in edge-achtige omstandigheden tijdens ontwikkeling  
- **Prestatiemonitoring**: Houd resourcegebruik en inference snelheid continu in de gaten  
- **Versiebeheer**: Houd modelversies en optimalisatie-instellingen bij  
- **Documentatie**: Documenteer alle optimalisatiebeslissingen en afwegingen in prestaties  

### Overwegingen bij Deployment  
- **Resource monitoring**: Houd geheugen-, CPU- en stroomgebruik in productie in de gaten  
- **Fallback-strategieën**: Implementeer fallback-mechanismen voor modelstoringen  
- **Update-mechanismen**: Plan modelupdates en versiebeheer  
- **Beveiliging**: Implementeer passende beveiligingsmaatregelen voor edge AI-toepassingen  

## Integratie met Edge AI Frameworks  

### ONNX Runtime  
- **Cross-platform Deployment**: Deploy ONNX-modellen op verschillende edge-platforms  
- **Hardwareoptimalisatie**: Maak gebruik van hardware-specifieke optimalisaties van ONNX Runtime  
- **Mobiele ondersteuning**: Gebruik ONNX Runtime Mobile voor smartphones en tablets  
- **IoT-integratie**: Deploy op IoT-apparaten met de lichte distributies van ONNX Runtime  

### Windows ML  
- **Windows-apparaten**: Optimaliseer voor Windows-gebaseerde edge-apparaten en pc's  
- **NPU-versnelling**: Maak gebruik van Neural Processing Units op Windows-apparaten  
- **DirectML**: Gebruik DirectML voor GPU-versnelling op Windows-platforms  
- **UWP-integratie**: Integreer met Universal Windows Platform-applicaties  

### TensorFlow Lite  
- **Mobiele optimalisatie**: Deploy TensorFlow Lite-modellen op mobiele en embedded apparaten  
- **Hardwaredelegates**: Gebruik gespecialiseerde hardwaredelegates voor versnelling  
- **Microcontrollers**: Deploy op microcontrollers met TensorFlow Lite Micro  
- **Cross-platform ondersteuning**: Deploy op Android, iOS en embedded Linux-systemen  

### Azure IoT Edge  
- **Cloud-Edge hybride**: Combineer cloudtraining met edge-inference  
- **Module Deployment**: Deploy AI-modellen als IoT Edge-modules  
- **Apparaatbeheer**: Beheer edge-apparaten en modelupdates op afstand  
- **Telemetrie**: Verzamel prestatiegegevens en modelmetrics van edge-deployments  

## Geavanceerde Edge AI Scenario's  

### Multi-Model Deployment  
- **Modelensembles**: Deploy meerdere modellen voor verbeterde nauwkeurigheid of redundantie  
- **A/B-testen**: Test verschillende modellen tegelijkertijd op edge-apparaten  
- **Dynamische selectie**: Kies modellen op basis van de huidige apparaatcondities  
- **Resource sharing**: Optimaliseer resourcegebruik over meerdere gedeployde modellen  

### Federated Learning  
- **Gedistribueerde training**: Train modellen op meerdere edge-apparaten  
- **Privacybescherming**: Houd trainingsdata lokaal terwijl modelverbeteringen worden gedeeld  
- **Collaboratief leren**: Laat apparaten leren van collectieve ervaringen  
- **Edge-Cloud coördinatie**: Coördineer leren tussen edge-apparaten en cloudinfrastructuur  

### Realtime verwerking  
- **Streamverwerking**: Verwerk continue datastromen op edge-apparaten  
- **Inference met lage latentie**: Optimaliseer voor minimale inference latentie  
- **Batchverwerking**: Verwerk batches van data efficiënt op edge-apparaten  
- **Adaptieve verwerking**: Pas verwerking aan op basis van de huidige apparaatcapaciteiten  

## Problemen oplossen bij Edge AI Ontwikkeling  

### Veelvoorkomende problemen  
- **Geheugenbeperkingen**: Model te groot voor het geheugen van het doelapparaat  
- **Inference snelheid**: Modelinference te traag voor realtime vereisten  
- **Nauwkeurigheidsverlies**: Optimalisatie vermindert modelnauwkeurigheid onaanvaardbaar  
- **Hardwarecompatibiliteit**: Model niet compatibel met doelhardware  

### Debugging-strategieën  
- **Prestatieprofilering**: Gebruik de tracing-functies van AI Toolkit om knelpunten te identificeren  
- **Resource monitoring**: Houd geheugen- en CPU-gebruik tijdens ontwikkeling in de gaten  
- **Incrementeel testen**: Test optimalisaties stapsgewijs om problemen te isoleren  
- **Hardware simulatie**: Gebruik ontwikkeltools om doelhardware te simuleren  

### Optimalisatieoplossingen  
- **Verdergaande quantisatie**: Pas agressievere quantisatietechnieken toe  
- **Modelarchitectuur**: Overweeg andere modelarchitecturen die geoptimaliseerd zijn voor edge  
- **Preprocessing optimalisatie**: Optimaliseer dataverwerking voor edge-beperkingen  
- **Inference optimalisatie**: Gebruik hardware-specifieke inference optimalisaties  

## Bronnen en Volgende Stappen  

### Officiële Documentatie  
- [AI Toolkit Developer Documentation](https://aka.ms/AIToolkit/doc)  
- [Installatie- en Setupgids](https://code.visualstudio.com/docs/intelligentapps/overview#_install-and-setup)  
- [VS Code Intelligent Apps Documentatie](https://code.visualstudio.com/docs/intelligentapps)  
- [Model Context Protocol (MCP) Documentatie](https://modelcontextprotocol.io/)  

### Community en Ondersteuning  
- [AI Toolkit GitHub Repository](https://github.com/microsoft/vscode-ai-toolkit)  
- [GitHub Issues en Functieaanvragen](https://aka.ms/AIToolkit/feedback)  
- [Azure AI Foundry Discord Community](https://aka.ms/azureaifoundry/discord)  
- [VS Code Extension Marketplace](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)  

### Technische Bronnen  
- [ONNX Runtime Documentatie](https://onnxruntime.ai/)  
- [Ollama Documentatie](https://ollama.ai/)  
- [Windows ML Documentatie](https://docs.microsoft.com/en-us/windows/ai/)  
- [Azure AI Foundry Documentatie](https://learn.microsoft.com/en-us/azure/ai-foundry/)  

### Leertrajecten  
- [Edge AI Fundamentals Cursus](../Module01/README.md)  
- [Small Language Models Gids](../Module02/README.md)  
- [Edge Deployment Strategieën](../Module03/README.md)  
- [Windows Edge AI Ontwikkeling](./windowdeveloper.md)  

### Aanvullende Bronnen  
- **Repository Statistieken**: 1.8k+ sterren, 150+ forks, 18+ bijdragers  
- **Licentie**: MIT Licentie  
- **Beveiliging**: Microsoft beveiligingsbeleid van toepassing  
- **Telemetrie**: Respecteert VS Code telemetrie-instellingen  

## Conclusie  

AI Toolkit voor Visual Studio Code biedt een uitgebreid platform voor moderne AI-ontwikkeling, met gestroomlijnde agentontwikkelingsmogelijkheden die bijzonder waardevol zijn voor Edge AI-toepassingen. Met een uitgebreide modelcatalogus die providers zoals Anthropic, OpenAI, GitHub en Google ondersteunt, gecombineerd met lokale uitvoering via ONNX en Ollama, biedt de toolkit de flexibiliteit die nodig is voor diverse edge-deployment scenario's.  

De kracht van de toolkit ligt in de geïntegreerde aanpak—van modelontdekking en experimentatie in de Playground tot geavanceerde agentontwikkeling met de Prompt Builder, uitgebreide evaluatiemogelijkheden en naadloze MCP-toolintegratie. Voor Edge AI-ontwikkelaars betekent dit snelle prototyping en testen van AI-agents vóór edge-deployment, met de mogelijkheid om snel te itereren en te optimaliseren voor omgevingen met beperkte middelen.  

Belangrijke voordelen voor Edge AI-ontwikkeling zijn:  
- **Snelle Experimentatie**: Test modellen en agents snel voordat ze worden gedeployed  
- **Multi-Provider Flexibiliteit**: Toegang tot modellen van verschillende bronnen om optimale edge-oplossingen te vinden  
- **Lokale Ontwikkeling**: Test met ONNX en Ollama voor offline en privacyvriendelijke ontwikkeling  
- **Productieklaar**: Genereer productieklare code en integreer met externe tools via MCP  
- **Uitgebreide Evaluatie**: Gebruik ingebouwde en aangepaste metrics om edge AI-prestaties te valideren  

Naarmate AI steeds meer naar edge-deployment scenario's beweegt, biedt AI Toolkit voor VS Code de ontwikkelomgeving en workflow die nodig zijn om intelligente applicaties te bouwen, testen en optimaliseren voor omgevingen met beperkte middelen. Of je nu IoT-oplossingen, mobiele AI-toepassingen of embedded intelligentiesystemen ontwikkelt, de uitgebreide functieset en geïntegreerde workflow van de toolkit ondersteunen de volledige edge AI-ontwikkelingscyclus.  

Met voortdurende ontwikkeling en een actieve community (1.8k+ GitHub-sterren) blijft AI Toolkit aan de top van AI-ontwikkeltools, en evolueert het voortdurend om te voldoen aan de behoeften van moderne AI-ontwikkelaars die bouwen voor edge-deployment scenario's.  

[Next Foundry Local](./foundrylocal.md)  

---

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
# AI Toolkit för Visual Studio Code - Guide för Edge AI-utveckling

## Introduktion

Välkommen till den omfattande guiden för att använda AI Toolkit för Visual Studio Code i Edge AI-utveckling. När artificiell intelligens flyttar från centraliserad molnberäkning till distribuerade enheter vid kanten, behöver utvecklare kraftfulla, integrerade verktyg som kan hantera de unika utmaningarna med edge-distribution - från resursbegränsningar till krav på offline-drift.

AI Toolkit för Visual Studio Code överbryggar detta gap genom att erbjuda en komplett utvecklingsmiljö som är specifikt utformad för att bygga, testa och optimera AI-applikationer som körs effektivt på edge-enheter. Oavsett om du utvecklar för IoT-sensorer, mobila enheter, inbyggda system eller edge-servrar, förenklar detta verktyg hela din utvecklingsprocess inom den välbekanta VS Code-miljön.

Denna guide kommer att ta dig igenom de grundläggande koncepten, verktygen och bästa praxis för att utnyttja AI Toolkit i dina Edge AI-projekt, från initial modellval till produktionsdistribution.

## Översikt

AI Toolkit för Visual Studio Code är en kraftfull extension som förenklar agentutveckling och skapandet av AI-applikationer. Verktyget erbjuder omfattande funktioner för att utforska, utvärdera och distribuera AI-modeller från en mängd olika leverantörer—inklusive Anthropic, OpenAI, GitHub, Google—samt stöd för lokal modellkörning med ONNX och Ollama.

Vad som skiljer AI Toolkit från andra är dess heltäckande tillvägagångssätt för hela AI-utvecklingscykeln. Till skillnad från traditionella AI-utvecklingsverktyg som fokuserar på enskilda aspekter, erbjuder AI Toolkit en integrerad miljö som täcker modellupptäckt, experimentering, agentutveckling, utvärdering och distribution—allting inom den välbekanta VS Code-miljön.

Plattformen är specifikt utformad för snabb prototypframställning och produktionsdistribution, med funktioner som promptgenerering, snabba startmallar, sömlös integration med MCP (Model Context Protocol)-verktyg och omfattande utvärderingsmöjligheter. För Edge AI-utveckling innebär detta att du effektivt kan utveckla, testa och optimera AI-applikationer för edge-distributionsscenarier samtidigt som du behåller hela utvecklingsarbetsflödet inom VS Code.

## Lärandemål

I slutet av denna guide kommer du att kunna:

### Grundläggande färdigheter
- **Installera och konfigurera** AI Toolkit för Visual Studio Code för Edge AI-utvecklingsarbetsflöden
- **Navigera och använda** AI Toolkit-gränssnittet, inklusive Model Catalog, Playground och Agent Builder
- **Välja och utvärdera** AI-modeller som är lämpliga för edge-distribution baserat på prestanda och resursbegränsningar
- **Konvertera och optimera** modeller med ONNX-format och kvantiseringstekniker för edge-enheter

### Edge AI-utvecklingsfärdigheter
- **Designa och implementera** Edge AI-applikationer med den integrerade utvecklingsmiljön
- **Utföra modelltestning** under edge-liknande förhållanden med lokal inferens och resursövervakning
- **Skapa och anpassa** AI-agenter optimerade för edge-distributionsscenarier
- **Utvärdera modellprestanda** med hjälp av metrik som är relevanta för edge-beräkning (latens, minnesanvändning, noggrannhet)

### Optimering och distribution
- **Tillämpa kvantisering och beskärning** för att minska modellstorlek samtidigt som acceptabel prestanda bibehålls
- **Optimera modeller** för specifika edge-hårdvaruplattformar inklusive CPU-, GPU- och NPU-acceleration
- **Implementera bästa praxis** för edge AI-utveckling inklusive resursförvaltning och fallback-strategier
- **Förbereda modeller och applikationer** för produktionsdistribution på edge-enheter

### Avancerade Edge AI-koncept
- **Integrera med edge AI-ramverk** inklusive ONNX Runtime, Windows ML och TensorFlow Lite
- **Implementera multimodellarkitekturer** och federerade inlärningsscenarier för edge-miljöer
- **Felsöka vanliga edge AI-problem** inklusive minnesbegränsningar, inferenshastighet och hårdvarukompatibilitet
- **Designa övervaknings- och loggningsstrategier** för edge AI-applikationer i produktion

### Praktisk tillämpning
- **Bygga kompletta Edge AI-lösningar** från modellval till distribution
- **Visa på kompetens** inom edge-specifika utvecklingsarbetsflöden och optimeringstekniker
- **Tillämpa inlärda koncept** på verkliga edge AI-användningsfall inklusive IoT, mobila och inbyggda applikationer
- **Utvärdera och jämföra** olika edge AI-distributionsstrategier och deras kompromisser

## Nyckelfunktioner för Edge AI-utveckling

### 1. Model Catalog och upptäckt
- **Stöd för flera leverantörer**: Bläddra och få tillgång till AI-modeller från Anthropic, OpenAI, GitHub, Google och andra leverantörer
- **Integration av lokala modeller**: Förenklad upptäckt av ONNX- och Ollama-modeller för edge-distribution
- **GitHub-modeller**: Direkt integration med GitHubs modellhosting för smidig åtkomst
- **Modelljämförelse**: Jämför modeller sida vid sida för att hitta optimal balans för edge-enhetens begränsningar

### 2. Interaktiv Playground
- **Interaktiv testmiljö**: Snabb experimentering med modellens kapacitet i en kontrollerad miljö
- **Stöd för multimodalitet**: Testa med bilder, text och andra indata som är typiska i edge-scenarier
- **Omedelbar feedback**: Direkt återkoppling på modellens svar och prestanda
- **Parameteroptimering**: Finjustera modellparametrar för edge-distributionskrav

### 3. Prompt (Agent) Builder
- **Naturlig språkgenerering**: Generera startprompter med hjälp av naturliga språkbeskrivningar
- **Iterativ förfining**: Förbättra prompter baserat på modellens svar och prestanda
- **Uppgiftsnedbrytning**: Dela upp komplexa uppgifter med promptkedjor och strukturerade utdata
- **Stöd för variabler**: Använd variabler i prompter för dynamiskt agentbeteende
- **Generering av produktionskod**: Skapa produktionsklar kod för snabb apputveckling

### 4. Masskörning och utvärdering
- **Testning av flera modeller**: Kör flera prompter över valda modeller samtidigt
- **Effektiv testning i stor skala**: Testa olika indata och konfigurationer effektivt
- **Anpassade testfall**: Kör agenter med testfall för att validera funktionalitet
- **Prestandajämförelse**: Jämför resultat mellan olika modeller och konfigurationer

### 5. Modellutvärdering med dataset
- **Standardmetrik**: Testa AI-modeller med inbyggda utvärderingsverktyg (F1-score, relevans, likhet, sammanhang)
- **Anpassade utvärderare**: Skapa egna utvärderingsmetoder för specifika användningsområden
- **Datasetintegration**: Testa modeller mot omfattande dataset
- **Prestandamätning**: Kvantifiera modellprestanda för beslut om edge-distribution

### 6. Finjusteringsmöjligheter
- **Modellanpassning**: Anpassa modeller för specifika användningsområden och domäner
- **Specialiserad anpassning**: Anpassa modeller till specialiserade domäner och krav
- **Edge-optimering**: Finjustera modeller specifikt för edge-distributionsbegränsningar
- **Domänspecifik träning**: Skapa modeller anpassade till specifika edge-användningsfall

### 7. MCP-verktygsintegration
- **Anslutning till externa verktyg**: Koppla agenter till externa verktyg via Model Context Protocol-servrar
- **Verkliga åtgärder**: Möjliggör att agenter kan fråga databaser, komma åt API:er eller köra anpassad logik
- **Befintliga MCP-servrar**: Använd verktyg från kommandon (stdio) eller HTTP (server-sent event)-protokoll
- **Utveckling av anpassade MCP**: Bygg och skapa nya MCP-servrar med testning i Agent Builder

### 8. Agentutveckling och testning
- **Stöd för funktionsanrop**: Möjliggör att agenter dynamiskt kan anropa externa funktioner
- **Testning av realtidsintegration**: Testa integrationer med realtidskörningar och verktygsanvändning
- **Agentversionering**: Versionskontroll för agenter med jämförelsefunktioner för utvärderingsresultat
- **Felsökning och spårning**: Lokal spårning och felsökningsmöjligheter för agentutveckling

## Edge AI-utvecklingsarbetsflöde

### Fas 1: Modellupptäckt och val
1. **Utforska Model Catalog**: Använd modellkatalogen för att hitta modeller som är lämpliga för edge-distribution
2. **Jämför prestanda**: Utvärdera modeller baserat på storlek, noggrannhet och inferenshastighet
3. **Testa lokalt**: Använd Ollama eller ONNX-modeller för att testa lokalt innan edge-distribution
4. **Bedöm resurskrav**: Fastställ minnes- och beräkningsbehov för mål-edge-enheter

### Fas 2: Modelloptimering
1. **Konvertera till ONNX**: Konvertera valda modeller till ONNX-format för edge-kompatibilitet
2. **Tillämpa kvantisering**: Minska modellstorlek genom INT8- eller INT4-kvantisering
3. **Hårdvaruoptimering**: Optimera för mål-edge-hårdvara (ARM, x86, specialiserade acceleratorer)
4. **Prestandavalidering**: Validera att optimerade modeller bibehåller acceptabel noggrannhet

### Fas 3: Applikationsutveckling
1. **Agentdesign**: Använd Agent Builder för att skapa edge-optimerade AI-agenter
2. **Promptutveckling**: Utveckla prompter som fungerar effektivt med mindre edge-modeller
3. **Integrationstestning**: Testa agenter under simulerade edge-förhållanden
4. **Kodgenerering**: Generera produktionskod optimerad för edge-distribution

### Fas 4: Utvärdering och testning
1. **Batchutvärdering**: Testa flera konfigurationer för att hitta optimala edge-inställningar
2. **Prestandaprofilering**: Analysera inferenshastighet, minnesanvändning och noggrannhet
3. **Edge-simulering**: Testa under förhållanden som liknar mål-edge-distributionsmiljön
4. **Stresstestning**: Utvärdera prestanda under olika belastningsförhållanden

### Fas 5: Distributionsförberedelse
1. **Slutlig optimering**: Tillämpa slutliga optimeringar baserat på testresultat
2. **Distributionspaketering**: Paketera modeller och kod för edge-distribution
3. **Dokumentation**: Dokumentera distributionskrav och konfiguration
4. **Övervakningsinställning**: Förbered övervakning och loggning för edge-distribution

## Målgrupp för Edge AI-utveckling

### Edge AI-utvecklare
- Applikationsutvecklare som bygger AI-drivna edge-enheter och IoT-lösningar
- Utvecklare av inbyggda system som integrerar AI-funktioner i resursbegränsade enheter
- Mobila utvecklare som skapar AI-applikationer på enheten för smartphones och surfplattor

### Edge AI-ingenjörer
- AI-ingenjörer som optimerar modeller för edge-distribution och hanterar inferenspipelines
- DevOps-ingenjörer som distribuerar och hanterar AI-modeller över distribuerad edge-infrastruktur
- Prestandaingenjörer som optimerar AI-arbetsbelastningar för edge-hårdvarubegränsningar

### Forskare och utbildare
- AI-forskare som utvecklar effektiva modeller och algoritmer för edge-beräkning
- Utbildare som lär ut edge AI-koncept och demonstrerar optimeringstekniker
- Studenter som lär sig om utmaningar och lösningar inom edge AI-distribution

## Edge AI-användningsfall

### Smarta IoT-enheter
- **Bildigenkänning i realtid**: Distribuera datorvisionsmodeller på IoT-kameror och sensorer
- **Röstbehandling**: Implementera taligenkänning och naturlig språkbehandling på smarta högtalare
- **Prediktivt underhåll**: Kör anomalidetektionsmodeller på industriella edge-enheter
- **Miljöövervakning**: Distribuera sensordataanaly-modeller för miljöapplikationer

### Mobila och inbyggda applikationer
- **Översättning på enheten**: Implementera språköversättningsmodeller som fungerar offline
- **Augmented Reality**: Distribuera realtidsobjektigenkänning och spårning för AR-applikationer
- **Hälsomonitorering**: Kör hälsanaly-modeller på bärbara enheter och medicinsk utrustning
- **Autonoma system**: Implementera beslutsfattande modeller för drönare, robotar och fordon

### Edge Computing-infrastruktur
- **Edge-datacenter**: Distribuera AI-modeller i edge-datacenter för låg-latensapplikationer
- **CDN-integration**: Integrera AI-bearbetningsfunktioner i innehållsleveransnätverk
- **5G Edge**: Utnyttja 5G edge-beräkning för AI-drivna applikationer
- **Fog Computing**: Implementera AI-bearbetning i fog computing-miljöer

## Installation och inställning

### Installation av extension
Installera AI Toolkit-extensionen direkt från Visual Studio Code Marketplace:

**Extension ID**: `ms-windows-ai-studio.windows-ai-studio`

**Installationsmetoder**:
1. **VS Code Marketplace**: Sök efter "AI Toolkit" i Extensions-vyn
2. **Kommandorad**: `code --install-extension ms-windows-ai-studio.windows-ai-studio`
3. **Direkt installation**: Ladda ner från [VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)

### Förutsättningar för Edge AI-utveckling
- **Visual Studio Code**: Senaste versionen rekommenderas
- **Python-miljö**: Python 3.8+ med nödvändiga AI-bibliotek
- **ONNX Runtime** (valfritt): För ONNX-modellinferens
- **Ollama** (valfritt): För lokal modellservering
- **Verktyg för hårdvaruacceleration**: CUDA, OpenVINO eller plattformspecifika acceleratorer

### Initial konfiguration
1. **Aktivering av extension**: Öppna VS Code och verifiera att AI Toolkit visas i aktivitetsfältet
2. **Inställning av modellleverantör**: Konfigurera åtkomst till GitHub, OpenAI, Anthropic eller andra modellleverantörer
3. **Lokal miljö**: Ställ in Python-miljö och installera nödvändiga paket
4. **Hårdvaruacceleration**: Konfigurera GPU/NPU-acceleration om tillgängligt
5. **MCP-integration**: Ställ in Model Context Protocol-servrar vid behov

### Checklista för första gången
- [ ] AI Toolkit-extension installerad och aktiverad
- [ ] Modellkatalog tillgänglig och modeller upptäckbara
- [ ] Playground fungerar för modelltestning
- [ ] Agent Builder tillgänglig för promptutveckling
- [ ] Lokal utvecklingsmiljö konfigurerad
- [ ] Hårdvaruacceleration (om tillgängligt) korrekt konfigurerad

## Kom igång med AI Toolkit

### Snabbstartsguide

Vi rekommenderar att börja med modeller som hostas av GitHub för den mest strömlinjeformade upplevelsen:

1. **Installation**: Följ [installationsguiden](https://code.visualstudio.com/docs/intelligentapps/overview#_install-and-setup) för att ställa in AI Toolkit på din enhet
2. **Modellupptäckt**: Från extensionens trädvy, välj **CATALOG > Models** för att utforska tillgängliga modeller
3. **GitHub-modeller**: Börja med modeller som hostas av GitHub för optimal integration
4. **Playground-testning**: Från vilken modellkort som helst, välj **Try in Playground** för att börja experimentera med modellens kapacitet

### Steg-för-steg Edge AI-utveckling

#### Steg 1: Modellutforskning och val
1. Öppna AI Toolkit-vyn i VS Code aktivitetsfält
2. Bläddra i Model Catalog för modeller som är lämpliga för edge-distribution
3. Fil
2. Generera startfrågor med hjälp av naturliga språkbeskrivningar  
3. Iterera och förbättra frågor baserat på modellens svar  
4. Integrera MCP-verktyg för förbättrade agentfunktioner  

#### Steg 3: Testning och utvärdering  
1. Använd **Bulk Run** för att testa flera frågor över valda modeller  
2. Kör agenter med testfall för att validera funktionalitet  
3. Utvärdera noggrannhet och prestanda med inbyggda eller anpassade mätvärden  
4. Jämför olika modeller och konfigurationer  

#### Steg 4: Finjustering och optimering  
1. Anpassa modeller för specifika edge-användningsfall  
2. Utför domänspecifik finjustering  
3. Optimera för begränsningar vid edge-distribution  
4. Versionshantera och jämför olika agentkonfigurationer  

#### Steg 5: Förberedelse för distribution  
1. Generera produktionsklar kod med Agent Builder  
2. Ställ in MCP-serveranslutningar för produktionsanvändning  
3. Förbered distributionspaket för edge-enheter  
4. Konfigurera övervaknings- och utvärderingsmätvärden  

## Exempel för AI Toolkit  

Prova våra exempel  
[AI Toolkit-exemplen](https://github.com/Azure-Samples/AI_Toolkit_Samples) är utformade för att hjälpa utvecklare och forskare att utforska och implementera AI-lösningar effektivt.  

Våra exempel inkluderar:  

Exempelkod: Förbyggda exempel som demonstrerar AI-funktioner, såsom träning, distribution eller integrering av modeller i applikationer.  
Dokumentation: Guider och handledningar som hjälper användare att förstå AI Toolkit-funktioner och hur man använder dem.  

Förutsättningar  

- Visual Studio Code  
- AI Toolkit för Visual Studio Code  
- GitHub Fine-grained personal access token (PAT)  
- Foundry Local  

## Bästa praxis för Edge AI-utveckling  

### Modellval  
- **Storleksbegränsningar**: Välj modeller som passar inom minnesbegränsningarna för målenheter  
- **Inferenshastighet**: Prioritera modeller med snabb inferens för realtidsapplikationer  
- **Noggrannhetsavvägningar**: Balansera modellens noggrannhet med resursbegränsningar  
- **Formatkompatibilitet**: Föredra ONNX eller hårdvaruoptimerade format för edge-distribution  

### Optimeringstekniker  
- **Kvantisering**: Använd INT8 eller INT4 kvantisering för att minska modellstorlek och förbättra hastighet  
- **Beskärning**: Ta bort onödiga modellparametrar för att minska beräkningskrav  
- **Kunskapsdestillation**: Skapa mindre modeller som bibehåller prestandan hos större  
- **Hårdvaruacceleration**: Utnyttja NPUs, GPUs eller specialiserade acceleratorer när det är möjligt  

### Utvecklingsarbetsflöde  
- **Iterativ testning**: Testa ofta under utvecklingen i edge-liknande förhållanden  
- **Prestandaövervakning**: Övervaka kontinuerligt resursanvändning och inferenshastighet  
- **Versionskontroll**: Spåra modellversioner och optimeringsinställningar  
- **Dokumentation**: Dokumentera alla optimeringsbeslut och avvägningar i prestanda  

### Distributionsöverväganden  
- **Resursövervakning**: Övervaka minne, CPU och strömförbrukning i produktion  
- **Fallback-strategier**: Implementera reservmekanismer för modellfel  
- **Uppdateringsmekanismer**: Planera för modelluppdateringar och versionshantering  
- **Säkerhet**: Implementera lämpliga säkerhetsåtgärder för edge AI-applikationer  

## Integration med Edge AI-ramverk  

### ONNX Runtime  
- **Plattformsoberoende distribution**: Distribuera ONNX-modeller över olika edge-plattformar  
- **Hårdvaruoptimering**: Utnyttja ONNX Runtimes hårdvaruspecifika optimeringar  
- **Mobilt stöd**: Använd ONNX Runtime Mobile för smartphones och surfplattor  
- **IoT-integration**: Distribuera på IoT-enheter med ONNX Runtimes lättviktsdistributioner  

### Windows ML  
- **Windows-enheter**: Optimera för Windows-baserade edge-enheter och datorer  
- **NPU-acceleration**: Utnyttja Neural Processing Units på Windows-enheter  
- **DirectML**: Använd DirectML för GPU-acceleration på Windows-plattformar  
- **UWP-integration**: Integrera med Universal Windows Platform-applikationer  

### TensorFlow Lite  
- **Mobiloptimering**: Distribuera TensorFlow Lite-modeller på mobila och inbyggda enheter  
- **Hårdvarudelegater**: Använd specialiserade hårdvarudelegater för acceleration  
- **Mikrokontroller**: Distribuera på mikrokontroller med TensorFlow Lite Micro  
- **Plattformsoberoende stöd**: Distribuera över Android, iOS och inbyggda Linux-system  

### Azure IoT Edge  
- **Moln-edge hybrid**: Kombinera molnträning med edge-inferens  
- **Moduldistribution**: Distribuera AI-modeller som IoT Edge-moduler  
- **Enhetshantering**: Hantera edge-enheter och modelluppdateringar på distans  
- **Telemetri**: Samla in prestandadata och modellmätvärden från edge-distributioner  

## Avancerade Edge AI-scenarier  

### Multi-modell distribution  
- **Modellensembler**: Distribuera flera modeller för förbättrad noggrannhet eller redundans  
- **A/B-testning**: Testa olika modeller samtidigt på edge-enheter  
- **Dynamiskt urval**: Välj modeller baserat på aktuella enhetsförhållanden  
- **Resursdelning**: Optimera resursanvändning över flera distribuerade modeller  

### Federerad inlärning  
- **Distribuerad träning**: Träna modeller över flera edge-enheter  
- **Integritetsskydd**: Behåll träningsdata lokalt samtidigt som modellförbättringar delas  
- **Samarbetsinlärning**: Möjliggör att enheter lär sig av kollektiva erfarenheter  
- **Edge-moln samordning**: Samordna inlärning mellan edge-enheter och molninfrastruktur  

### Realtidsbearbetning  
- **Strömbearbetning**: Bearbeta kontinuerliga dataströmmar på edge-enheter  
- **Låg latens inferens**: Optimera för minimal inferenslatens  
- **Batchbearbetning**: Effektivt bearbeta datapartier på edge-enheter  
- **Adaptiv bearbetning**: Anpassa bearbetning baserat på aktuella enhetskapaciteter  

## Felsökning av Edge AI-utveckling  

### Vanliga problem  
- **Minnesbegränsningar**: Modellen är för stor för målenhetens minne  
- **Inferenshastighet**: Modellens inferens är för långsam för realtidskrav  
- **Noggrannhetsförsämring**: Optimering minskar modellens noggrannhet oacceptabelt  
- **Hårdvarukompatibilitet**: Modellen är inte kompatibel med målhårdvaran  

### Felsökningsstrategier  
- **Prestandaprofilering**: Använd AI Toolkits spårningsfunktioner för att identifiera flaskhalsar  
- **Resursövervakning**: Övervaka minne och CPU-användning under utveckling  
- **Inkrementell testning**: Testa optimeringar stegvis för att isolera problem  
- **Hårdvarusimulering**: Använd utvecklingsverktyg för att simulera målhårdvara  

### Optimeringslösningar  
- **Ytterligare kvantisering**: Använd mer aggressiva kvantiseringstekniker  
- **Modellarkitektur**: Överväg olika modellarkitekturer optimerade för edge  
- **Förbearbetningsoptimering**: Optimera databehandling för edge-begränsningar  
- **Inferensoptimering**: Använd hårdvaruspecifika inferensoptimeringar  

## Resurser och nästa steg  

### Officiell dokumentation  
- [AI Toolkit Developer Documentation](https://aka.ms/AIToolkit/doc)  
- [Installations- och inställningsguide](https://code.visualstudio.com/docs/intelligentapps/overview#_install-and-setup)  
- [VS Code Intelligent Apps Dokumentation](https://code.visualstudio.com/docs/intelligentapps)  
- [Model Context Protocol (MCP) Dokumentation](https://modelcontextprotocol.io/)  

### Community och support  
- [AI Toolkit GitHub Repository](https://github.com/microsoft/vscode-ai-toolkit)  
- [GitHub Issues och funktionsförfrågningar](https://aka.ms/AIToolkit/feedback)  
- [Azure AI Foundry Discord Community](https://aka.ms/azureaifoundry/discord)  
- [VS Code Extension Marketplace](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)  

### Tekniska resurser  
- [ONNX Runtime Dokumentation](https://onnxruntime.ai/)  
- [Ollama Dokumentation](https://ollama.ai/)  
- [Windows ML Dokumentation](https://docs.microsoft.com/en-us/windows/ai/)  
- [Azure AI Foundry Dokumentation](https://learn.microsoft.com/en-us/azure/ai-foundry/)  

### Lärvägar  
- [Edge AI Fundamentals Kurs](../Module01/README.md)  
- [Guide för små språkmodeller](../Module02/README.md)  
- [Strategier för edge-distribution](../Module03/README.md)  
- [Windows Edge AI-utveckling](./windowdeveloper.md)  

### Ytterligare resurser  
- **Repository-statistik**: 1.8k+ stjärnor, 150+ forks, 18+ bidragsgivare  
- **Licens**: MIT License  
- **Säkerhet**: Microsofts säkerhetspolicyer gäller  
- **Telemetri**: Respekterar VS Codes telemetriinställningar  

## Slutsats  

AI Toolkit för Visual Studio Code representerar en omfattande plattform för modern AI-utveckling, med smidiga agentutvecklingsmöjligheter som är särskilt värdefulla för Edge AI-applikationer. Med sin omfattande modellkatalog som stöder leverantörer som Anthropic, OpenAI, GitHub och Google, kombinerat med lokal körning via ONNX och Ollama, erbjuder verktyget den flexibilitet som behövs för olika edge-distributionsscenarier.  

Styrkan i verktyget ligger i dess integrerade tillvägagångssätt – från modellupptäckt och experimentering i Playground till sofistikerad agentutveckling med Prompt Builder, omfattande utvärderingsmöjligheter och sömlös MCP-verktygsintegration. För Edge AI-utvecklare innebär detta snabb prototypframställning och testning av AI-agenter innan edge-distribution, med möjlighet att snabbt iterera och optimera för resursbegränsade miljöer.  

Nyckelfördelar för Edge AI-utveckling inkluderar:  
- **Snabb experimentering**: Testa modeller och agenter snabbt innan edge-distribution  
- **Flexibilitet med flera leverantörer**: Få tillgång till modeller från olika källor för att hitta optimala edge-lösningar  
- **Lokal utveckling**: Testa med ONNX och Ollama för offline- och integritetsskyddande utveckling  
- **Produktionsberedskap**: Generera produktionsklar kod och integrera med externa verktyg via MCP  
- **Omfattande utvärdering**: Använd inbyggda och anpassade mätvärden för att validera edge AI-prestanda  

När AI fortsätter att röra sig mot edge-distributionsscenarier, erbjuder AI Toolkit för VS Code den utvecklingsmiljö och arbetsflöde som behövs för att bygga, testa och optimera intelligenta applikationer för resursbegränsade miljöer. Oavsett om du utvecklar IoT-lösningar, mobila AI-applikationer eller inbyggda intelligenssystem, stödjer verktygets omfattande funktioner och integrerade arbetsflöde hela livscykeln för Edge AI-utveckling.  

Med pågående utveckling och en aktiv community (1.8k+ GitHub-stjärnor) ligger AI Toolkit i framkant av AI-utvecklingsverktyg och utvecklas kontinuerligt för att möta behoven hos moderna AI-utvecklare som bygger för edge-distributionsscenarier.  

[Next Foundry Local](./foundrylocal.md)  

---

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, bör det noteras att automatiserade översättningar kan innehålla fel eller felaktigheter. Det ursprungliga dokumentet på dess ursprungliga språk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.
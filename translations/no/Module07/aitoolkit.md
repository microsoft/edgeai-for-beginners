# AI-verktøysett for Visual Studio Code - Veiledning for Edge AI-utvikling

## Introduksjon

Velkommen til den omfattende veiledningen for bruk av AI-verktøysettet for Visual Studio Code i Edge AI-utvikling. Etter hvert som kunstig intelligens beveger seg fra sentralisert skybasert databehandling til distribuerte enheter på kanten, trenger utviklere kraftige, integrerte verktøy som kan håndtere de unike utfordringene ved kantutplassering - fra ressursbegrensninger til krav om offline drift.

AI-verktøysettet for Visual Studio Code bygger bro over dette gapet ved å tilby et komplett utviklingsmiljø spesielt designet for å bygge, teste og optimalisere AI-applikasjoner som kjører effektivt på kant-enheter. Enten du utvikler for IoT-sensorer, mobile enheter, innebygde systemer eller kantservere, forenkler dette verktøysettet hele utviklingsarbeidsflyten din innenfor det velkjente VS Code-miljøet.

Denne veiledningen vil ta deg gjennom de essensielle konseptene, verktøyene og beste praksisene for å utnytte AI-verktøysettet i dine Edge AI-prosjekter, fra valg av modell til produksjonsutplassering.

## Oversikt

AI-verktøysettet for Visual Studio Code er en kraftig utvidelse som forenkler utvikling av agenter og opprettelse av AI-applikasjoner. Verktøysettet gir omfattende muligheter for å utforske, evaluere og distribuere AI-modeller fra et bredt spekter av leverandører—inkludert Anthropic, OpenAI, GitHub, Google—samt støtte for lokal modellkjøring ved bruk av ONNX og Ollama.

Det som skiller AI-verktøysettet fra andre er dets helhetlige tilnærming til hele AI-utviklingslivssyklusen. I motsetning til tradisjonelle AI-utviklingsverktøy som fokuserer på enkeltaspekter, gir AI-verktøysettet et integrert miljø som dekker modelloppdagelse, eksperimentering, agentutvikling, evaluering og distribusjon—alt innenfor det velkjente VS Code-miljøet.

Plattformen er spesielt designet for rask prototyping og produksjonsutplassering, med funksjoner som generering av forespørsler, raske startmaler, sømløs MCP (Model Context Protocol)-verktøyintegrasjon og omfattende evalueringsmuligheter. For Edge AI-utvikling betyr dette at du effektivt kan utvikle, teste og optimalisere AI-applikasjoner for kantutplassering, samtidig som du opprettholder hele utviklingsarbeidsflyten innenfor VS Code.

## Læringsmål

Ved slutten av denne veiledningen vil du kunne:

### Kjernekompetanser
- **Installere og konfigurere** AI-verktøysettet for Visual Studio Code for Edge AI-utviklingsarbeidsflyter
- **Navigere og bruke** AI-verktøysettets grensesnitt, inkludert Model Catalog, Playground og Agent Builder
- **Velge og evaluere** AI-modeller som er egnet for kantutplassering basert på ytelse og ressursbegrensninger
- **Konvertere og optimalisere** modeller ved bruk av ONNX-format og kvantiseringsteknikker for kant-enheter

### Edge AI-utviklingsferdigheter
- **Designe og implementere** Edge AI-applikasjoner ved bruk av det integrerte utviklingsmiljøet
- **Utføre modelltesting** under kantlignende forhold ved bruk av lokal inferens og ressursmonitorering
- **Opprette og tilpasse** AI-agenter optimalisert for kantutplassering
- **Evaluere modellytelse** ved bruk av metrikker som er relevante for kantdatabehandling (latens, minnebruk, nøyaktighet)

### Optimalisering og distribusjon
- **Bruke kvantisering og beskjæring** for å redusere modellstørrelse samtidig som akseptabel ytelse opprettholdes
- **Optimalisere modeller** for spesifikke kantmaskinvareplattformer, inkludert CPU-, GPU- og NPU-akselerasjon
- **Implementere beste praksis** for Edge AI-utvikling, inkludert ressursstyring og fallback-strategier
- **Forberede modeller og applikasjoner** for produksjonsutplassering på kant-enheter

### Avanserte Edge AI-konsepter
- **Integrere med Edge AI-rammeverk** inkludert ONNX Runtime, Windows ML og TensorFlow Lite
- **Implementere multimodellarkitekturer** og federerte læringsscenarier for kantmiljøer
- **Feilsøke vanlige Edge AI-problemer** inkludert minnebegrensninger, inferenshastighet og maskinvarekompatibilitet
- **Designe overvåkings- og loggstrategier** for Edge AI-applikasjoner i produksjon

### Praktisk anvendelse
- **Bygge helhetlige Edge AI-løsninger** fra modellvalg til distribusjon
- **Demonstrere ferdigheter** i kantspesifikke utviklingsarbeidsflyter og optimaliseringsteknikker
- **Bruke lærte konsepter** på virkelige Edge AI-brukstilfeller, inkludert IoT, mobil og innebygde applikasjoner
- **Evaluere og sammenligne** ulike Edge AI-utplasseringsstrategier og deres fordeler og ulemper

## Nøkkelfunksjoner for Edge AI-utvikling

### 1. Modellkatalog og oppdagelse
- **Støtte for flere leverandører**: Bla gjennom og få tilgang til AI-modeller fra Anthropic, OpenAI, GitHub, Google og andre leverandører
- **Lokal modellintegrasjon**: Forenklet oppdagelse av ONNX- og Ollama-modeller for kantutplassering
- **GitHub-modeller**: Direkte integrasjon med GitHubs modellhosting for strømlinjeformet tilgang
- **Modellsammenligning**: Sammenlign modeller side om side for å finne optimal balanse for kant-enhetsbegrensninger

### 2. Interaktiv lekeplass
- **Interaktivt testmiljø**: Rask eksperimentering med modellens evner i et kontrollert miljø
- **Multimodal støtte**: Test med bilder, tekst og andre input som er typiske i kantscenarier
- **Sanntidseksperimentering**: Umiddelbar tilbakemelding på modellens svar og ytelse
- **Parameteroptimalisering**: Finjuster modellparametere for kantutplasseringskrav

### 3. Forespørselsbygger (Agent Builder)
- **Naturlig språkgenerering**: Generer startforespørsler ved bruk av beskrivelser i naturlig språk
- **Iterativ forbedring**: Forbedre forespørsler basert på modellens svar og ytelse
- **Oppgavedekomponering**: Bryt ned komplekse oppgaver med forespørselskjeding og strukturerte utdata
- **Variabelstøtte**: Bruk variabler i forespørsler for dynamisk agentatferd
- **Produksjonskodegenerering**: Generer produksjonsklar kode for rask apputvikling

### 4. Massekjøring og evaluering
- **Testing av flere modeller**: Utfør flere forespørsler på tvers av utvalgte modeller samtidig
- **Effektiv testing i stor skala**: Test ulike input og konfigurasjoner effektivt
- **Egendefinerte testtilfeller**: Kjør agenter med testtilfeller for å validere funksjonalitet
- **Ytelsessammenligning**: Sammenlign resultater på tvers av ulike modeller og konfigurasjoner

### 5. Modellevaluering med datasett
- **Standardmetrikker**: Test AI-modeller ved bruk av innebygde evaluatorer (F1-score, relevans, likhet, sammenheng)
- **Egendefinerte evaluatorer**: Lag dine egne evalueringsmetrikker for spesifikke brukstilfeller
- **Datasettintegrasjon**: Test modeller mot omfattende datasett
- **Ytelsesmåling**: Kvantifiser modellens ytelse for kantutplasseringsbeslutninger

### 6. Finjusteringsmuligheter
- **Modelltilpasning**: Tilpass modeller for spesifikke brukstilfeller og domener
- **Spesialisert tilpasning**: Tilpass modeller til spesialiserte domener og krav
- **Kantoptimalisering**: Finjuster modeller spesifikt for kantutplasseringsbegrensninger
- **Domene-spesifikk trening**: Lag modeller skreddersydd for spesifikke kantbrukstilfeller

### 7. MCP-verktøyintegrasjon
- **Ekstern verktøystilkobling**: Koble agenter til eksterne verktøy via Model Context Protocol-servere
- **Reelle handlinger**: Aktiver agenter til å spørre databaser, få tilgang til API-er eller utføre egendefinert logikk
- **Eksisterende MCP-servere**: Bruk verktøy fra kommando (stdio) eller HTTP (server-sendt hendelse)-protokoller
- **Egendefinert MCP-utvikling**: Bygg og opprett nye MCP-servere med testing i Agent Builder

### 8. Agentutvikling og testing
- **Støtte for funksjonskall**: Aktiver agenter til dynamisk å utføre eksterne funksjoner
- **Sanntidsintegrasjonstesting**: Test integrasjoner med sanntidskjøringer og verktøybruk
- **Agentversjonering**: Versjonskontroll for agenter med sammenligningsmuligheter for evalueringsresultater
- **Feilsøking og sporing**: Lokal sporing og feilsøkingsmuligheter for agentutvikling

## Arbeidsflyt for Edge AI-utvikling

### Fase 1: Modelloppdagelse og -valg
1. **Utforsk modellkatalogen**: Bruk modellkatalogen for å finne modeller som er egnet for kantutplassering
2. **Sammenlign ytelse**: Evaluer modeller basert på størrelse, nøyaktighet og inferenshastighet
3. **Test lokalt**: Bruk Ollama- eller ONNX-modeller for lokal testing før kantutplassering
4. **Vurder ressursbehov**: Bestem minne- og beregningsbehov for målrettede kant-enheter

### Fase 2: Modelloptimalisering
1. **Konverter til ONNX**: Konverter utvalgte modeller til ONNX-format for kantkompatibilitet
2. **Bruk kvantisering**: Reduser modellstørrelse gjennom INT8- eller INT4-kvantisering
3. **Maskinvareoptimalisering**: Optimaliser for målrettet kantmaskinvare (ARM, x86, spesialiserte akseleratorer)
4. **Ytelsesvalidering**: Valider at optimaliserte modeller opprettholder akseptabel nøyaktighet

### Fase 3: Applikasjonsutvikling
1. **Agentdesign**: Bruk Agent Builder til å lage kantoptimaliserte AI-agenter
2. **Forespørselsutvikling**: Utvikle forespørsler som fungerer effektivt med mindre kantmodeller
3. **Integrasjonstesting**: Test agenter under simulerte kantforhold
4. **Kodegenerering**: Generer produksjonskode optimalisert for kantutplassering

### Fase 4: Evaluering og testing
1. **Batch-evaluering**: Test flere konfigurasjoner for å finne optimale kantinnstillinger
2. **Ytelsesprofilering**: Analyser inferenshastighet, minnebruk og nøyaktighet
3. **Kantsimulering**: Test under forhold som ligner målrettet kantutplasseringsmiljø
4. **Stresstesting**: Evaluer ytelse under ulike belastningsforhold

### Fase 5: Distribusjonsforberedelse
1. **Endelig optimalisering**: Utfør endelige optimaliseringer basert på testresultater
2. **Distribusjonspakking**: Pakk modeller og kode for kantutplassering
3. **Dokumentasjon**: Dokumenter distribusjonskrav og konfigurasjon
4. **Overvåkingsoppsett**: Forbered overvåking og logging for kantutplassering

## Målgruppe for Edge AI-utvikling

### Edge AI-utviklere
- Applikasjonsutviklere som bygger AI-drevne kant-enheter og IoT-løsninger
- Utviklere av innebygde systemer som integrerer AI-funksjoner i ressursbegrensede enheter
- Mobilutviklere som lager AI-applikasjoner for smarttelefoner og nettbrett

### Edge AI-ingeniører
- AI-ingeniører som optimaliserer modeller for kantutplassering og administrerer inferensrørledninger
- DevOps-ingeniører som distribuerer og administrerer AI-modeller på tvers av distribuert kantinfrastruktur
- Ytelsesingeniører som optimaliserer AI-arbeidsbelastninger for kantmaskinvarebegrensninger

### Forskere og undervisere
- AI-forskere som utvikler effektive modeller og algoritmer for kantdatabehandling
- Undervisere som lærer bort Edge AI-konsepter og demonstrerer optimaliseringsteknikker
- Studenter som lærer om utfordringene og løsningene innen kantutplassering av AI

## Edge AI-brukstilfeller

### Smarte IoT-enheter
- **Sanntids bildeanalyse**: Distribuer datamodeller for datamaskinsyn på IoT-kameraer og sensorer
- **Talebehandling**: Implementer talegjenkjenning og naturlig språkbehandling på smarte høyttalere
- **Prediktivt vedlikehold**: Kjør anomalideteksjonsmodeller på industrielle kant-enheter
- **Miljøovervåking**: Distribuer modeller for sensoranalyse for miljøapplikasjoner

### Mobile og innebygde applikasjoner
- **Oversettelse på enhet**: Implementer språkoversettelsesmodeller som fungerer offline
- **Utvidet virkelighet**: Distribuer sanntids objektgjenkjenning og sporing for AR-applikasjoner
- **Helseovervåking**: Kjør helseanalysmodeller på bærbare enheter og medisinsk utstyr
- **Autonome systemer**: Implementer beslutningsmodeller for droner, roboter og kjøretøy

### Kantdatabehandlingsinfrastruktur
- **Kantdatasentre**: Distribuer AI-modeller i kantdatasentre for lav-latens applikasjoner
- **CDN-integrasjon**: Integrer AI-behandlingsmuligheter i innholdsleveringsnettverk
- **5G Edge**: Utnytt 5G kantdatabehandling for AI-drevne applikasjoner
- **Tåkedatabehandling**: Implementer AI-behandling i tåkedatabehandlingsmiljøer

## Installasjon og oppsett

### Installasjon av utvidelsen
Installer AI-verktøysettutvidelsen direkte fra Visual Studio Code Marketplace:

**Utvidelses-ID**: `ms-windows-ai-studio.windows-ai-studio`

**Installasjonsmetoder**:
1. **VS Code Marketplace**: Søk etter "AI Toolkit" i Extensions-visningen
2. **Kommandolinje**: `code --install-extension ms-windows-ai-studio.windows-ai-studio`
3. **Direkte installasjon**: Last ned fra [VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)

### Forutsetninger for Edge AI-utvikling
- **Visual Studio Code**: Nyeste versjon anbefales
- **Python-miljø**: Python 3.8+ med nødvendige AI-biblioteker
- **ONNX Runtime** (valgfritt): For ONNX-modellinferens
- **Ollama** (valgfritt): For lokal modellservering
- **Maskinvareakselerasjonsverktøy**: CUDA, OpenVINO eller plattformspesifikke akseleratorer

### Innledende konfigurasjon
1. **Aktivering av utvidelsen**: Åpne VS Code og bekreft at AI-verktøysettet vises i aktivitetsfeltet
2. **Oppsett av modellleverandør**: Konfigurer tilgang til GitHub, OpenAI, Anthropic eller andre modellleverandører
3. **Lokalt miljø**: Sett opp Python-miljø og installer nødvendige pakker
4. **Maskinvareakselerasjon**: Konfigurer GPU/NPU-akselerasjon hvis tilgjengelig
5. **MCP-integrasjon**: Sett opp Model Context Protocol-servere hvis nødvendig

### Sjekkliste for førstegangsoppsett
- [ ] AI-verktøysettutvidelse installert og aktivert
- [ ] Modellkatalog tilgjengelig og modeller oppdagbare
- [ ] Playground fungerer for modelltesting
- [ ] Agent Builder tilgjengelig for forespørselsutvikling
- [ ] Lokalt utviklingsmiljø konfigurert
- [ ] Maskinvareakselerasjon (hvis tilgjengelig) riktig konfigurert

## Komme i gang med AI-verktøysettet

### Hurtigstartveiledning

Vi anbefaler å starte med modeller som er hostet av GitHub for den mest strømlinjeformede opplevelsen:

1. **Installasjon**: Følg [installasjonsveiledningen](https://code.visualstudio.com/docs/intelligentapps/overview#_install-and-setup) for å sette opp AI-verktøysettet på enheten din
2. **Modelloppdagelse**: Fra utvidelsens trevisning, velg **CATALOG > Models** for å utforske tilgjengelige modeller
3. **GitHub-modeller**: Start med modeller hostet av GitHub for optimal integrasjon
4. **Playground-testing**: Fra hvilken som helst
2. Generer startspørsmål ved hjelp av naturlige språklige beskrivelser  
3. Iterer og forbedre spørsmål basert på modellens svar  
4. Integrer MCP-verktøy for forbedrede agentfunksjoner  

#### Steg 3: Testing og evaluering  
1. Bruk **Bulk Run** for å teste flere spørsmål på tvers av utvalgte modeller  
2. Kjør agenter med testtilfeller for å validere funksjonalitet  
3. Evaluer nøyaktighet og ytelse ved hjelp av innebygde eller tilpassede metrikker  
4. Sammenlign ulike modeller og konfigurasjoner  

#### Steg 4: Finjustering og optimalisering  
1. Tilpass modeller for spesifikke edge-bruksområder  
2. Utfør domenespesifikk finjustering  
3. Optimaliser for edge-utplasseringsbegrensninger  
4. Versjoner og sammenlign ulike agentkonfigurasjoner  

#### Steg 5: Forberedelse til utplassering  
1. Generer produksjonsklar kode ved hjelp av Agent Builder  
2. Sett opp MCP-serverforbindelser for produksjonsbruk  
3. Forbered utplasseringspakker for edge-enheter  
4. Konfigurer overvåkings- og evalueringsmetrikker  

## Eksempler for AI Toolkit  

Prøv våre eksempler  
[AI Toolkit-eksemplene](https://github.com/Azure-Samples/AI_Toolkit_Samples) er designet for å hjelpe utviklere og forskere med å utforske og implementere AI-løsninger effektivt.  

Våre eksempler inkluderer:  

Eksempelkode: Ferdigbygde eksempler som demonstrerer AI-funksjonaliteter, som trening, utplassering eller integrering av modeller i applikasjoner.  
Dokumentasjon: Veiledninger og opplæringsmateriale for å hjelpe brukere med å forstå AI Toolkit-funksjoner og hvordan de brukes.  

Forutsetninger  

- Visual Studio Code  
- AI Toolkit for Visual Studio Code  
- GitHub Fine-grained personal access token (PAT)  
- Foundry Local  

## Beste praksis for Edge AI-utvikling  

### Modellvalg  
- **Størrelsesbegrensninger**: Velg modeller som passer innenfor minnebegrensningene til mål-enhetene  
- **Inferences hastighet**: Prioriter modeller med rask inferences for sanntidsapplikasjoner  
- **Nøyaktighetsavveininger**: Balanser modellens nøyaktighet med ressursbegrensninger  
- **Formatkompatibilitet**: Foretrekk ONNX eller maskinvareoptimaliserte formater for edge-utplassering  

### Optimaliseringsteknikker  
- **Kvantisering**: Bruk INT8 eller INT4 kvantisering for å redusere modellstørrelse og forbedre hastighet  
- **Beskjæring**: Fjern unødvendige modellparametere for å redusere beregningskrav  
- **Kunnskapsdestillasjon**: Lag mindre modeller som opprettholder ytelsen til større modeller  
- **Maskinvareakselerasjon**: Utnytt NPUs, GPUs eller spesialiserte akseleratorer når tilgjengelig  

### Utviklingsarbeidsflyt  
- **Iterativ testing**: Test ofte under edge-lignende forhold under utvikling  
- **Ytelsesovervåking**: Overvåk kontinuerlig ressursbruk og inferences hastighet  
- **Versjonskontroll**: Spor modellversjoner og optimaliseringsinnstillinger  
- **Dokumentasjon**: Dokumenter alle optimaliseringsbeslutninger og ytelsesavveininger  

### Utplasseringshensyn  
- **Ressursovervåking**: Overvåk minne-, CPU- og strømforbruk i produksjon  
- **Reserveplaner**: Implementer reserveplaner for modellfeil  
- **Oppdateringsmekanismer**: Planlegg for modelloppdateringer og versjonshåndtering  
- **Sikkerhet**: Implementer passende sikkerhetstiltak for edge AI-applikasjoner  

## Integrasjon med Edge AI-rammeverk  

### ONNX Runtime  
- **Plattformuavhengig utplassering**: Utplasser ONNX-modeller på tvers av ulike edge-plattformer  
- **Maskinvareoptimalisering**: Utnytt ONNX Runtimes maskinvare-spesifikke optimaliseringer  
- **Mobilstøtte**: Bruk ONNX Runtime Mobile for smarttelefon- og nettbrettapplikasjoner  
- **IoT-integrasjon**: Utplasser på IoT-enheter ved hjelp av ONNX Runtimes lette distribusjoner  

### Windows ML  
- **Windows-enheter**: Optimaliser for Windows-baserte edge-enheter og PC-er  
- **NPU-akselerasjon**: Utnytt Neural Processing Units på Windows-enheter  
- **DirectML**: Bruk DirectML for GPU-akselerasjon på Windows-plattformer  
- **UWP-integrasjon**: Integrer med Universal Windows Platform-applikasjoner  

### TensorFlow Lite  
- **Mobiloptimalisering**: Utplasser TensorFlow Lite-modeller på mobile og innebygde enheter  
- **Maskinvaredelegeringer**: Bruk spesialiserte maskinvaredelegeringer for akselerasjon  
- **Mikrokontrollere**: Utplasser på mikrokontrollere ved hjelp av TensorFlow Lite Micro  
- **Plattformuavhengig støtte**: Utplasser på tvers av Android, iOS og innebygde Linux-systemer  

### Azure IoT Edge  
- **Sky-Edge hybrid**: Kombiner trening i skyen med inferences på edge  
- **Modulutplassering**: Utplasser AI-modeller som IoT Edge-moduler  
- **Enhetsadministrasjon**: Administrer edge-enheter og modelloppdateringer eksternt  
- **Telemetri**: Samle ytelsesdata og modellmetrikker fra edge-utplasseringer  

## Avanserte Edge AI-scenarier  

### Multi-modell utplassering  
- **Modellensembler**: Utplasser flere modeller for forbedret nøyaktighet eller redundans  
- **A/B-testing**: Test ulike modeller samtidig på edge-enheter  
- **Dynamisk valg**: Velg modeller basert på gjeldende enhetsforhold  
- **Ressursdeling**: Optimaliser ressursbruk på tvers av flere utplasserte modeller  

### Federert læring  
- **Distribuert trening**: Tren modeller på tvers av flere edge-enheter  
- **Personvernbevaring**: Hold treningsdata lokalt mens du deler modellforbedringer  
- **Samarbeidende læring**: La enheter lære av kollektive erfaringer  
- **Edge-Sky koordinering**: Koordiner læring mellom edge-enheter og skyinfrastruktur  

### Sanntidsbehandling  
- **Strømbehandling**: Behandle kontinuerlige datastrømmer på edge-enheter  
- **Lav-latens inferences**: Optimaliser for minimal inferences latens  
- **Batchbehandling**: Effektivt behandle batcher av data på edge-enheter  
- **Adaptiv behandling**: Juster behandling basert på gjeldende enhetskapasiteter  

## Feilsøking av Edge AI-utvikling  

### Vanlige problemer  
- **Minnebegrensninger**: Modellen er for stor for mål-enhetens minne  
- **Inferences hastighet**: Modellens inferences er for treg for sanntidskrav  
- **Nøyaktighetsforringelse**: Optimalisering reduserer modellens nøyaktighet uakseptabelt  
- **Maskinvarekompatibilitet**: Modellen er ikke kompatibel med målmaskinvaren  

### Feilsøkingsstrategier  
- **Ytelsesprofilering**: Bruk AI Toolkits sporingsfunksjoner for å identifisere flaskehalser  
- **Ressursovervåking**: Overvåk minne- og CPU-bruk under utvikling  
- **Inkrementell testing**: Test optimaliseringer trinnvis for å isolere problemer  
- **Maskinvaresimulering**: Bruk utviklingsverktøy for å simulere målmaskinvaren  

### Optimaliseringsløsninger  
- **Videre kvantisering**: Bruk mer aggressive kvantiseringsteknikker  
- **Modellarkitektur**: Vurder ulike modellarkitekturer optimalisert for edge  
- **Forbehandlingsoptimalisering**: Optimaliser datapreprosessering for edge-begrensninger  
- **Inferences optimalisering**: Bruk maskinvare-spesifikke inferences optimaliseringer  

## Ressurser og neste steg  

### Offisiell dokumentasjon  
- [AI Toolkit Developer Documentation](https://aka.ms/AIToolkit/doc)  
- [Installation and Setup Guide](https://code.visualstudio.com/docs/intelligentapps/overview#_install-and-setup)  
- [VS Code Intelligent Apps Documentation](https://code.visualstudio.com/docs/intelligentapps)  
- [Model Context Protocol (MCP) Documentation](https://modelcontextprotocol.io/)  

### Fellesskap og støtte  
- [AI Toolkit GitHub Repository](https://github.com/microsoft/vscode-ai-toolkit)  
- [GitHub Issues and Feature Requests](https://aka.ms/AIToolkit/feedback)  
- [Azure AI Foundry Discord Community](https://aka.ms/azureaifoundry/discord)  
- [VS Code Extension Marketplace](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)  

### Tekniske ressurser  
- [ONNX Runtime Documentation](https://onnxruntime.ai/)  
- [Ollama Documentation](https://ollama.ai/)  
- [Windows ML Documentation](https://docs.microsoft.com/en-us/windows/ai/)  
- [Azure AI Foundry Documentation](https://learn.microsoft.com/en-us/azure/ai-foundry/)  

### Læringsveier  
- [Edge AI Fundamentals Course](../Module01/README.md)  
- [Small Language Models Guide](../Module02/README.md)  
- [Edge Deployment Strategies](../Module03/README.md)  
- [Windows Edge AI Development](./windowdeveloper.md)  

### Tilleggsressurser  
- **Repository Stats**: 1.8k+ stjerner, 150+ forks, 18+ bidragsytere  
- **Lisens**: MIT-lisens  
- **Sikkerhet**: Microsofts sikkerhetspolicyer gjelder  
- **Telemetri**: Respekterer VS Code telemetriinnstillinger  

## Konklusjon  

AI Toolkit for Visual Studio Code representerer en omfattende plattform for moderne AI-utvikling, og tilbyr strømlinjeformede agentutviklingsfunksjoner som er spesielt verdifulle for Edge AI-applikasjoner. Med sin omfattende modellkatalog som støtter leverandører som Anthropic, OpenAI, GitHub og Google, kombinert med lokal kjøring gjennom ONNX og Ollama, gir verktøysettet fleksibiliteten som trengs for ulike edge-utplasseringsscenarier.  

Styrken til verktøysettet ligger i den integrerte tilnærmingen—fra modelloppdagelse og eksperimentering i Playground til sofistikert agentutvikling med Prompt Builder, omfattende evalueringsmuligheter og sømløs MCP-verktøyintegrasjon. For Edge AI-utviklere betyr dette rask prototyping og testing av AI-agenter før edge-utplassering, med mulighet til å iterere raskt og optimalisere for ressursbegrensede miljøer.  

Nøkkelfordeler for Edge AI-utvikling inkluderer:  
- **Rask eksperimentering**: Test modeller og agenter raskt før du forplikter deg til edge-utplassering  
- **Fleksibilitet med flere leverandører**: Tilgang til modeller fra ulike kilder for å finne optimale edge-løsninger  
- **Lokal utvikling**: Test med ONNX og Ollama for offline og personvernbevarende utvikling  
- **Produksjonsklarhet**: Generer produksjonsklar kode og integrer med eksterne verktøy via MCP  
- **Omfattende evaluering**: Bruk innebygde og tilpassede metrikker for å validere edge AI-ytelse  

Etter hvert som AI fortsetter å bevege seg mot edge-utplasseringsscenarier, gir AI Toolkit for VS Code det utviklingsmiljøet og arbeidsflyten som trengs for å bygge, teste og optimalisere intelligente applikasjoner for ressursbegrensede miljøer. Enten du utvikler IoT-løsninger, mobile AI-applikasjoner eller innebygde intelligenssystemer, støtter verktøysettets omfattende funksjonssett og integrerte arbeidsflyt hele livssyklusen for Edge AI-utvikling.  

Med kontinuerlig utvikling og et aktivt fellesskap (1.8k+ GitHub-stjerner), forblir AI Toolkit i frontlinjen av AI-utviklingsverktøy, og utvikler seg kontinuerlig for å møte behovene til moderne AI-utviklere som bygger for edge-utplasseringsscenarier.  

[Next Foundry Local](./foundrylocal.md)  

---

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
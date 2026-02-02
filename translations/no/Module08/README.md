# Modul 08: Praktisk arbeid med Microsoft Foundry Local - Komplett utviklerverktøy

## Oversikt

[Microsoft Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/) representerer neste generasjon av edge AI-utvikling, og gir utviklere kraftige verktøy for å bygge, distribuere og skalere AI-applikasjoner lokalt, samtidig som det opprettholder sømløs integrasjon med Azure AI Foundry. Denne modulen gir en omfattende dekning av Foundry Local, fra installasjon til avansert agentutvikling.

**Nøkkelteknologier:**
- Microsoft Foundry Local CLI og SDK
- Azure AI Foundry-integrasjon
- Modellinferens på enheten
- Lokal modellbuffer og optimalisering
- Agentbaserte arkitekturer

## Læringsmål

Ved å fullføre denne modulen vil du:

- **Beherske Foundry Local**: Installere, konfigurere og optimalisere for utvikling på Windows 11
- **Distribuere ulike modeller**: Kjøre phi-, qwen-, deepseek- og GPT-modeller lokalt med CLI-kommandoer
- **Bygge produksjonsløsninger**: Lage AI-applikasjoner med avansert prompt engineering og dataintegrasjon
- **Utnytte det åpne økosystemet**: Integrere Hugging Face-modeller og bidrag fra fellesskapet
- **Utvikle AI-agenter**: Bygge intelligente agenter med grounding og orkestreringsfunksjoner
- **Implementere bedriftsmønstre**: Lage modulære, skalerbare AI-løsninger for produksjonsdistribusjon

## Struktur for øktene

### [1: Kom i gang med Foundry Local](./01.FoundryLocalSetup.md)
**Fokus**: Installasjon, CLI-oppsett, modelldistribusjon og maskinvareoptimalisering

**Nøkkeltemaer**: Fullstendig installasjon • CLI-kommandoer • Modellbuffer • Maskinvareakselerasjon • Multi-modell distribusjon

**Eksempel**: [REST Chat Quickstart](./samples/01/README.md) • [OpenAI SDK-integrasjon](./samples/02/README.md) • [Modelloppdagelse og benchmarking](./samples/03/README.md)

**Varighet**: 2-3 timer | **Nivå**: Nybegynner

---

### [2: Bygg AI-løsninger med Azure AI Foundry](./02.AzureAIFoundryIntegration.md)
**Fokus**: Avansert prompt engineering, dataintegrasjon og skytilkobling

**Nøkkeltemaer**: Prompt engineering • Dataintegrasjon • Azure arbeidsflyter • Ytelsesoptimalisering • Overvåking

**Eksempel**: [Chainlit RAG-applikasjon](./samples/04/README.md)

**Varighet**: 2-3 timer | **Nivå**: Middels

---

### [3: Åpen kildekode-modeller med Foundry Local](./03.OpenSourceModels.md)
**Fokus**: Hugging Face-integrasjon, BYOM-strategier og fellesskapsmodeller

**Nøkkeltemaer**: Hugging Face-integrasjon • Bring-your-own-model • Innsikt fra Model Mondays • Bidrag fra fellesskapet • Modellvalg

**Eksempel**: [Multi-Agent Orchestration](./samples/05/README.md)

**Varighet**: 2-3 timer | **Nivå**: Middels

---

### [4: Utforsk banebrytende modeller](./04.CuttingEdgeModels.md)
**Fokus**: LLMs vs SLMs, EdgeAI-implementering og avanserte demoer

**Nøkkeltemaer**: Modell sammenligning • Edge vs sky-inferens • Phi + ONNX Runtime • Chainlit RAG-app • WebGPU-optimalisering

**Eksempel**: [Models-as-Tools Router](./samples/06/README.md)

**Varighet**: 3-4 timer | **Nivå**: Avansert

---

### [5: Bygg AI-drevne agenter raskt](./05.AIPoweredAgents.md)
**Fokus**: Agentarkitekturer, systemprompter, grounding og orkestrering

**Nøkkeltemaer**: Agentdesignmønstre • Systemprompt engineering • Grounding-teknikker • Multi-agent systemer • Produksjonsdistribusjon

**Eksempel**: [Multi-Agent Orchestration](./samples/05/README.md) • [Avansert Multi-Agent System](./samples/09/README.md)

**Varighet**: 3-4 timer | **Nivå**: Avansert

---

### [6: Foundry Local - Modeller som verktøy](./06.ModelsAsTools.md)
**Fokus**: Modulære AI-løsninger, bedriftsmessig skalering og produksjonsmønstre

**Nøkkeltemaer**: Modeller som verktøy • Distribusjon på enheten • SDK/API-integrasjon • Bedriftsarkitekturer • Skaleringsstrategier

**Eksempel**: [Models-as-Tools Router](./samples/06/README.md) • [Foundry Tools Framework](./samples/10/README.md)

**Varighet**: 3-4 timer | **Nivå**: Ekspert

---

### [7: Direkte API-integrasjonsmønstre](./samples/07/README.md)
**Fokus**: Ren REST API-integrasjon uten SDK-avhengigheter for maksimal kontroll

**Nøkkeltemaer**: HTTP-klientimplementering • Tilpasset autentisering • Modellhelseovervåking • Streaming-responser • Feilhåndtering i produksjon

**Eksempel**: [Direct API Client](./samples/07/README.md)

**Varighet**: 2-3 timer | **Nivå**: Middels

---

### [8: Windows 11 Native Chat-applikasjon](./samples/08/README.md)
**Fokus**: Bygge moderne native chat-applikasjoner med Foundry Local-integrasjon

**Nøkkeltemaer**: Electron-utvikling • Fluent Design System • Native Windows-integrasjon • Sanntidsstreaming • Chatgrensesnittdesign

**Eksempel**: [Windows 11 Chat Application](./samples/08/README.md)

**Varighet**: 3-4 timer | **Nivå**: Avansert

---

### [9: Avansert Multi-Agent Orchestration](./samples/09/README.md)
**Fokus**: Sofistikert agentkoordinering, spesialisert oppgavetildeling og samarbeidsbaserte AI-arbeidsflyter

**Nøkkeltemaer**: Intelligent agentkoordinering • Funksjonskallmønstre • Kommunikasjon mellom agenter • Arbeidsflytorkestrering • Kvalitetssikringsmekanismer

**Eksempel**: [Avansert Multi-Agent System](./samples/09/README.md)

**Varighet**: 4-5 timer | **Nivå**: Ekspert

---

### [10: Foundry Local som verktøyrammeverk](./samples/10/README.md)
**Fokus**: Verktøy-først arkitektur for å integrere Foundry Local i eksisterende applikasjoner og rammeverk

**Nøkkeltemaer**: LangChain-integrasjon • Semantiske Kernel-funksjoner • REST API-rammeverk • CLI-verktøy • Jupyter-integrasjon • Produksjonsdistribusjonsmønstre

**Eksempel**: [Foundry Tools Framework](./samples/10/README.md)

**Varighet**: 4-5 timer | **Nivå**: Ekspert

## Forutsetninger

### Systemkrav
- **Operativsystem**: Windows 11 (22H2 eller nyere)
- **Minne**: 16GB RAM (32GB anbefalt for større modeller)
- **Lagring**: 50GB ledig plass for modellbuffer
- **Maskinvare**: Enhet med NPU anbefales (Copilot+ PC), GPU valgfritt
- **Nettverk**: Høyhastighetsinternett for første modellnedlastinger

### Utviklingsmiljø
- Visual Studio Code med AI Toolkit-utvidelse
- Python 3.10+ og pip
- Git for versjonskontroll
- PowerShell eller Kommandolinje
- Azure CLI (valgfritt for skyintegrasjon)

### Kunnskapsforutsetninger
- Grunnleggende forståelse av AI/ML-konsepter
- Kjennskap til kommandolinjen
- Grunnleggende Python-programmering
- REST API-konsepter
- Grunnleggende kunnskap om prompting og modellinferens

## Modulens tidslinje

**Total estimert tid**: 30-38 timer

| Økt | Fokusområde | Eksempler | Tid | Kompleksitet |
|-----|-------------|-----------|-----|--------------|
|  1 | Oppsett og grunnleggende | 01, 02, 03 | 2-3 timer | Nybegynner |
|  2 | AI-løsninger | 04 | 2-3 timer | Middels |
|  3 | Åpen kildekode | 05 | 2-3 timer | Middels |
|  4 | Avanserte modeller | 06 | 3-4 timer | Avansert |
|  5 | AI-agenter | 05, 09 | 3-4 timer | Avansert |
|  6 | Bedriftsverktøy | 06, 10 | 3-4 timer | Ekspert |
|  7 | Direkte API-integrasjon | 07 | 2-3 timer | Middels |
|  8 | Windows 11 Chat-app | 08 | 3-4 timer | Avansert |
|  9 | Avansert Multi-Agent | 09 | 4-5 timer | Ekspert |
| 10 | Verktøyrammeverk | 10 | 4-5 timer | Ekspert |

## Nøkkelressurser

**Offisiell dokumentasjon:**
- [Microsoft Foundry Local GitHub](https://github.com/microsoft/Foundry-Local) - Kildekode og offisielle eksempler
- [Azure AI Foundry Dokumentasjon](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/) - Komplett oppsett og bruksveiledning
- [Model Mondays Series](https://aka.ms/model-mondays) - Ukentlige modellhøydepunkter og veiledninger

**Fellesskap og støtte:**
- [Foundry Local Diskusjoner](https://github.com/microsoft/Foundry-Local/discussions) - Fellesskapets spørsmål og funksjonsforespørsler
- [Microsoft AI Developer Community](https://techcommunity.microsoft.com/category/artificialintelligence) - Nyheter og beste praksis

## Læringsutbytte

Etter å ha fullført denne modulen vil du være i stand til:

### Teknisk mestring
- **Distribuere og administrere**: Foundry Local-installasjoner på tvers av utviklings- og produksjonsmiljøer
- **Integrere modeller**: Arbeide sømløst med ulike modellsamlinger fra Microsoft, Hugging Face og fellesskapskilder
- **Bygge applikasjoner**: Lage produksjonsklare AI-applikasjoner med avanserte funksjoner og optimaliseringer
- **Utvikle agenter**: Implementere sofistikerte AI-agenter med grounding, resonnering og verktøyintegrasjon

### Strategisk forståelse
- **Arkitekturvalg**: Ta informerte beslutninger mellom lokal og skybasert distribusjon
- **Ytelsesoptimalisering**: Optimalisere inferensytelse på tvers av ulike maskinvarekonfigurasjoner
- **Bedriftsmessig skalering**: Designe applikasjoner som skalerer fra lokale prototyper til bedriftsdistribusjoner
- **Personvern og sikkerhet**: Implementere personvernbevarende AI-løsninger med lokal inferens

### Innovasjonskapasitet
- **Rask prototyping**: Raskt bygge og teste AI-applikasjonskonsepter på tvers av alle 10 eksempelmønstre
- **Fellesskapsintegrasjon**: Utnytte åpne kildekode-modeller og bidra til økosystemet
- **Avanserte mønstre**: Implementere banebrytende AI-mønstre inkludert RAG, agenter og verktøyintegrasjon
- **Rammeverksmestring**: Ekspertintegrasjon med LangChain, Semantic Kernel, Chainlit og Electron
- **Produksjonsdistribusjon**: Distribuere skalerbare AI-løsninger fra lokale prototyper til bedriftsmiljøer
- **Fremtidsrettet utvikling**: Bygge applikasjoner klare for fremvoksende AI-teknologier og mønstre

## Kom i gang

1. **Miljøoppsett**: Sørg for Windows 11 med anbefalt maskinvare (se Forutsetninger)
2. **Installer Foundry Local**: Følg økt 1 for fullstendig installasjon og konfigurasjon
3. **Kjør eksempel 01**: Start med grunnleggende REST API-integrasjon for å verifisere oppsettet
4. **Fortsett gjennom eksemplene**: Fullfør eksempler 01-10 for omfattende mestring

## Suksessindikatorer

Spor fremgangen din gjennom alle 10 omfattende eksempler:

### Grunnleggende nivå (Eksempler 01-03)
- [ ] Installere og konfigurere Foundry Local med suksess
- [ ] Fullføre REST API-integrasjon (Eksempel 01)
- [ ] Implementere OpenAI SDK-kompatibilitet (Eksempel 02)
- [ ] Utføre modelloppdagelse og benchmarking (Eksempel 03)

### Applikasjonsnivå (Eksempler 04-06)
- [ ] Distribuere og kjøre minst 4 ulike modellsamlinger
- [ ] Bygge en funksjonell RAG-chatapplikasjon (Eksempel 04)
- [ ] Lage et multi-agent orkestreringssystem (Eksempel 05)
- [ ] Implementere intelligent modellruting (Eksempel 06)

### Avansert integrasjonsnivå (Eksempler 07-10)
- [ ] Bygge produksjonsklar API-klient (Eksempel 07)
- [ ] Utvikle Windows 11 native chat-applikasjon (Eksempel 08)
- [ ] Implementere avansert multi-agent system (Eksempel 09)
- [ ] Lage omfattende verktøyrammeverk (Eksempel 10)

### Mestringsindikatorer
- [ ] Kjøre alle 10 eksempler uten feil
- [ ] Tilpasse minst 3 eksempler for spesifikke bruksområder
- [ ] Distribuere 2+ eksempler i produksjonslignende miljøer
- [ ] Bidra med forbedringer eller utvidelser til eksempelkode
- [ ] Integrere Foundry Local-mønstre i personlige/profesjonelle prosjekter

## Hurtigstartveiledning - Alle 10 eksempler

### Miljøoppsett (Påkrevd for alle eksempler)

```powershell
# 1. Clone and navigate to Module08
cd Module08

# 2. Create Python virtual environment
py -m venv .venv
.\.venv\Scripts\activate

# 3. Install base dependencies
pip install -r requirements.txt

# 4. Install Foundry Local (if not already installed)
winget install Microsoft.FoundryLocal

# 5. Verify Foundry Local installation
foundry --version
foundry model list
```

### Grunnleggende eksempler (01-06)

**Eksempel 01: REST Chat Quickstart**
```powershell
# Start Foundry Local service
foundry model run phi-4-mini

# Run REST chat demo
python samples/01/chat_quickstart.py
```

**Eksempel 02: OpenAI SDK-integrasjon**
```powershell
# Ensure model is running
foundry status

# Run SDK demo
python samples/02/sdk_quickstart.py
```

**Eksempel 03: Modelloppdagelse og benchmarking**
```powershell
# Run comprehensive model testing
samples/03/list_and_bench.cmd

# Or run individual components
foundry model list --available
foundry model download qwen2.5-0.5b
foundry model benchmark phi-4-mini
```

**Eksempel 04: Chainlit RAG-applikasjon**
```powershell
# Install Chainlit dependencies
pip install chainlit langchain chromadb

# Start RAG chat application
chainlit run samples/04/app.py -w
# Opens browser at http://localhost:8000
```

**Eksempel 05: Multi-Agent Orchestration**
```powershell
# Run agent coordinator demo
python -m samples.05.agents.coordinator

# Run specific agent examples
python samples/05/examples/specialists_demo.py
```

**Eksempel 06: Models-as-Tools Router**
```powershell
# Configure environment
set BASE_URL=http://localhost:8000
set GENERAL_MODEL=phi-4-mini
set CODE_MODEL=qwen2.5-7b

# Run intelligent router
python samples/06/router.py "Analyze this Python code for performance issues"
```

### Avanserte eksempler (07-10)

**Eksempel 07: Direkte API-klient**
```powershell
# Navigate to sample directory
cd samples/07

# Install additional dependencies
pip install -r requirements.txt

# Run basic API examples
python examples/basic_usage.py

# Try streaming responses
python examples/streaming.py

# Test production patterns
python examples/production.py
```

**Eksempel 08: Windows 11 Chat-applikasjon**
```powershell
# Navigate to sample directory
cd samples/08

# Install Node.js dependencies
npm install

# Start Electron application
npm start

# Or build for production
npm run build
```

**Eksempel 09: Avansert Multi-Agent System**
```powershell
# Navigate to sample directory
cd samples/09

# Install agent system dependencies
pip install -r requirements.txt

# Run basic coordination example
python examples/basic_coordination.py

# Try complex workflow
python examples/complex_workflow.py

# Interactive agent demo
python examples/interactive_demo.py
```

**Eksempel 10: Foundry Tools Framework**
```powershell
# Navigate to sample directory
cd samples/10

# Install framework dependencies
pip install -r requirements.txt

# Run basic tools demo
python examples/basic_tools.py

# Start REST API server
python examples/rest_api_server.py
# API available at http://localhost:8080

# Try CLI application
python examples/cli_application.py --help

# Launch Jupyter notebook
jupyter notebook examples/jupyter_notebook.ipynb

# Test LangChain integration
python examples/langchain_demo.py
```

### Feilsøking av vanlige problemer

**Foundry Local-tilkoblingsfeil**
```powershell
# Check service status
foundry status

# Restart if needed
foundry restart

# Verify endpoint accessibility
curl http://localhost:5273/v1/models
```

**Problemer med modellinnlasting**
```powershell
# Check available models
foundry model list --cached

# Download missing models
foundry model download phi-4-mini
foundry model download qwen2.5-0.5b

# Force reload if needed
foundry model unload --all
foundry model run phi-4-mini
```

**Avhengighetsproblemer**
```powershell
# Upgrade pip and reinstall
python -m pip install --upgrade pip
pip install -r requirements.txt --force-reinstall

# For Node.js samples
npm cache clean --force
npm install
```

## Oppsummering
Dette modulen representerer det nyeste innen utvikling av edge AI, og kombinerer Microsofts verktøy i bedriftsklasse med fleksibiliteten og innovasjonen fra det åpne kilde-økosystemet. Ved å mestre Foundry Local gjennom alle de 10 omfattende eksemplene, vil du være i frontlinjen av utvikling av AI-applikasjoner.

**Fullstendig læringssti:**
- **Grunnleggende** (Eksempler 01-03): API-integrasjon og modelladministrasjon
- **Applikasjoner** (Eksempler 04-06): RAG, agenter og intelligent ruting
- **Avansert** (Eksempler 07-10): Produksjonsrammeverk og bedriftsintegrasjon

For Azure OpenAI-integrasjon (Sesjon 2), se README-filene for hvert enkelt eksempel for nødvendige miljøvariabler og innstillinger for API-versjon.

---

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi tilstreber nøyaktighet, vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
# Modul 08: Praktično delo z Microsoft Foundry Local - Celovit razvojni komplet

## Pregled

[Microsoft Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/) predstavlja naslednjo generacijo razvoja AI na robu, ki razvijalcem omogoča zmogljiva orodja za gradnjo, uvajanje in skaliranje AI aplikacij lokalno, hkrati pa ohranja brezhibno integracijo z Azure AI Foundry. Ta modul ponuja celovit pregled Foundry Local od namestitve do naprednega razvoja agentov.

**Ključne tehnologije:**
- Microsoft Foundry Local CLI in SDK
- Integracija z Azure AI Foundry
- Lokalna inferenca modelov
- Lokalno predpomnjenje in optimizacija modelov
- Arhitekture, ki temeljijo na agentih

## Cilji učenja

Z dokončanjem tega modula boste:

- **Obvladali Foundry Local**: Namestili, konfigurirali in optimizirali za razvoj na Windows 11
- **Uvajali različne modele**: Lokalno izvajali modele phi, qwen, deepseek in GPT z ukazi CLI
- **Gradili produkcijske rešitve**: Ustvarili AI aplikacije z naprednim oblikovanjem pozivov in integracijo podatkov
- **Izkoristili odprtokodni ekosistem**: Integrirali modele Hugging Face in prispevke skupnosti
- **Razvijali AI agente**: Gradili inteligentne agente z zmožnostmi utemeljitve in orkestracije
- **Uvajali vzorce za podjetja**: Ustvarili modularne, skalabilne AI rešitve za produkcijsko uporabo

## Struktura seje

### [1: Začetek z Foundry Local](./01.FoundryLocalSetup.md)
**Osredotočenost**: Namestitev, nastavitev CLI, uvajanje modelov in optimizacija strojne opreme

**Ključne teme**: Popolna namestitev • Ukazi CLI • Predpomnjenje modelov • Pospeševanje strojne opreme • Uvajanje več modelov

**Primer**: [REST Chat Quickstart](./samples/01/README.md) • [OpenAI SDK Integration](./samples/02/README.md) • [Model Discovery & Benchmarking](./samples/03/README.md)

**Trajanje**: 2-3 ure | **Raven**: Začetnik

---

### [2: Gradnja AI rešitev z Azure AI Foundry](./02.AzureAIFoundryIntegration.md)
**Osredotočenost**: Napredno oblikovanje pozivov, integracija podatkov in povezljivost v oblaku

**Ključne teme**: Oblikovanje pozivov • Integracija podatkov • Azure delovni tokovi • Optimizacija zmogljivosti • Spremljanje

**Primer**: [Chainlit RAG Application](./samples/04/README.md)

**Trajanje**: 2-3 ure | **Raven**: Srednje zahtevno

---

### [3: Odprtokodni modeli v Foundry Local](./03.OpenSourceModels.md)
**Osredotočenost**: Integracija Hugging Face, strategije BYOM in modeli skupnosti

**Ključne teme**: Integracija HuggingFace • Prinesi svoj model (BYOM) • Vpogledi Model Mondays • Prispevki skupnosti • Izbor modelov

**Primer**: [Multi-Agent Orchestration](./samples/05/README.md)

**Trajanje**: 2-3 ure | **Raven**: Srednje zahtevno

---

### [4: Raziskovanje najsodobnejših modelov](./04.CuttingEdgeModels.md)
**Osredotočenost**: Primerjava LLM proti SLM, implementacija EdgeAI in napredni prikazi

**Ključne teme**: Primerjava modelov • Inferenca na robu proti oblaku • Phi + ONNX Runtime • Chainlit RAG aplikacija • Optimizacija WebGPU

**Primer**: [Models-as-Tools Router](./samples/06/README.md)

**Trajanje**: 3-4 ure | **Raven**: Napredno

---

### [5: Hitro gradite AI-podprte agente](./05.AIPoweredAgents.md)
**Osredotočenost**: Arhitekture agentov, sistemski pozivi, utemeljitev in orkestracija

**Ključne teme**: Vzorci oblikovanja agentov • Oblikovanje sistemskih pozivov • Tehnike utemeljitve • Sistemi z več agenti • Uvajanje v produkcijo

**Primer**: [Multi-Agent Orchestration](./samples/05/README.md) • [Advanced Multi-Agent System](./samples/09/README.md)

**Trajanje**: 3-4 ure | **Raven**: Napredno

---

### [6: Foundry Local - modeli kot orodja](./06.ModelsAsTools.md)
**Osredotočenost**: Modularne AI rešitve, skaliranje za podjetja in produkcijski vzorci

**Ključne teme**: Modeli kot orodja • Uvajanje na napravi • Integracija SDK/API • Arhitekture za podjetja • Strategije skaliranja

**Primer**: [Models-as-Tools Router](./samples/06/README.md) • [Foundry Tools Framework](./samples/10/README.md)

**Trajanje**: 3-4 ure | **Raven**: Strokovno

---

### [7: Vzorci neposredne integracije API](./samples/07/README.md)
**Osredotočenost**: Čista integracija REST API brez odvisnosti od SDK za maksimalen nadzor

**Ključne teme**: Implementacija HTTP odjemalca • Prilagojena avtentikacija • Spremljanje zdravja modelov • Pretakanje odgovorov • Upravljanje napak v produkciji

**Primer**: [Direct API Client](./samples/07/README.md)

**Trajanje**: 2-3 ure | **Raven**: Srednje zahtevno

---

### [8: Windows 11 domača aplikacija za klepet](./samples/08/README.md)
**Osredotočenost**: Gradnja sodobnih domačih aplikacij za klepet z integracijo Foundry Local

**Ključne teme**: Razvoj z Electron • Fluent Design System • Domača integracija Windows • Pretakanje v realnem času • Oblikovanje vmesnika za klepet

**Primer**: [Windows 11 Chat Application](./samples/08/README.md)

**Trajanje**: 3-4 ure | **Raven**: Napredno

---

### [9: Napredna orkestracija več agentov](./samples/09/README.md)
**Osredotočenost**: Sofisticirana koordinacija agentov, specializirana delegacija nalog in sodelovalni AI delovni tokovi

**Ključne teme**: Inteligentna koordinacija agentov • Vzorci klicanja funkcij • Komunikacija med agenti • Orkestracija delovnih tokov • Mehanizmi zagotavljanja kakovosti

**Primer**: [Advanced Multi-Agent System](./samples/09/README.md)

**Trajanje**: 4-5 ur | **Raven**: Strokovno

---

### [10: Foundry Local kot okvir orodij](./samples/10/README.md)
**Osredotočenost**: Arhitektura, ki temelji na orodjih, za integracijo Foundry Local v obstoječe aplikacije in okvire

**Ključne teme**: Integracija LangChain • Funkcije Semantic Kernel • Okviri REST API • Orodja CLI • Integracija Jupyter • Vzorci uvajanja v produkcijo

**Primer**: [Foundry Tools Framework](./samples/10/README.md)

**Trajanje**: 4-5 ur | **Raven**: Strokovno

## Predpogoji

### Zahteve sistema
- **Operacijski sistem**: Windows 11 (22H2 ali novejši)
- **Pomnilnik**: 16GB RAM (32GB priporočeno za večje modele)
- **Shramba**: 50GB prostega prostora za predpomnjenje modelov
- **Strojna oprema**: Priporočena naprava z NPU (Copilot+ PC), GPU opcijsko
- **Omrežje**: Hitra internetna povezava za začetne prenose modelov

### Razvojno okolje
- Visual Studio Code z razširitvijo AI Toolkit
- Python 3.10+ in pip
- Git za nadzor različic
- PowerShell ali Command Prompt
- Azure CLI (opcijsko za integracijo v oblak)

### Predhodno znanje
- Osnovno razumevanje konceptov AI/ML
- Seznanjenost z ukazno vrstico
- Osnove programiranja v Pythonu
- Koncepti REST API
- Osnovno znanje o oblikovanju pozivov in inferenci modelov

## Časovnica modula

**Skupni ocenjeni čas**: 30-38 ur

| Seja | Področje | Primeri | Čas | Zahtevnost |
|------|----------|---------|-----|------------|
|  1 | Namestitev in osnove | 01, 02, 03 | 2-3 ure | Začetnik |
|  2 | AI rešitve | 04 | 2-3 ure | Srednje zahtevno |
|  3 | Odprtokodni modeli | 05 | 2-3 ure | Srednje zahtevno |
|  4 | Napredni modeli | 06 | 3-4 ure | Napredno |
|  5 | AI agenti | 05, 09 | 3-4 ure | Napredno |
|  6 | Orodja za podjetja | 06, 10 | 3-4 ure | Strokovno |
|  7 | Neposredna integracija API | 07 | 2-3 ure | Srednje zahtevno |
|  8 | Windows 11 aplikacija za klepet | 08 | 3-4 ure | Napredno |
|  9 | Napredna orkestracija več agentov | 09 | 4-5 ur | Strokovno |
| 10 | Okvir orodij | 10 | 4-5 ur | Strokovno |

## Ključni viri

**Uradna dokumentacija:**
- [Microsoft Foundry Local GitHub](https://github.com/microsoft/Foundry-Local) - Izvorna koda in uradni primeri
- [Azure AI Foundry Dokumentacija](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/) - Popoln vodič za namestitev in uporabo
- [Model Mondays Series](https://aka.ms/model-mondays) - Tedenski poudarki modelov in vadnice

**Skupnost in podpora:**
- [Foundry Local Discussions](https://github.com/microsoft/Foundry-Local/discussions) - Vprašanja in zahteve za funkcije skupnosti
- [Microsoft AI Developer Community](https://techcommunity.microsoft.com/category/artificialintelligence) - Najnovejše novice in najboljše prakse

## Rezultati učenja

Po dokončanju tega modula boste pripravljeni na:

### Tehnično obvladovanje
- **Uvajanje in upravljanje**: Namestitve Foundry Local v razvojnih in produkcijskih okoljih
- **Integracija modelov**: Brezhibno delo z različnimi družinami modelov iz Microsofta, Hugging Face in skupnosti
- **Gradnja aplikacij**: Ustvarjanje produkcijsko pripravljenih AI aplikacij z naprednimi funkcijami in optimizacijami
- **Razvoj agentov**: Implementacija sofisticiranih AI agentov z utemeljitvijo, sklepanjem in integracijo orodij

### Strateško razumevanje
- **Odločitve o arhitekturi**: Informirane izbire med lokalnim in oblačnim uvajanjem
- **Optimizacija zmogljivosti**: Optimizacija zmogljivosti inferenc na različnih konfiguracijah strojne opreme
- **Skaliranje za podjetja**: Oblikovanje aplikacij, ki se skalirajo od lokalnih prototipov do uvajanja v podjetjih
- **Zasebnost in varnost**: Implementacija rešitev AI, ki ohranjajo zasebnost z lokalno inferenco

### Inovacijske sposobnosti
- **Hitro prototipiranje**: Hitro gradite in testirajte koncepte AI aplikacij po vseh 10 vzorčnih vzorcih
- **Integracija skupnosti**: Izkoristite odprtokodne modele in prispevajte k ekosistemu
- **Napredni vzorci**: Implementacija najsodobnejših AI vzorcev, vključno z RAG, agenti in integracijo orodij
- **Obvladovanje okvirov**: Strokovna integracija z LangChain, Semantic Kernel, Chainlit in Electron
- **Uvajanje v produkcijo**: Uvajanje skalabilnih AI rešitev od lokalnih prototipov do sistemov za podjetja
- **Razvoj pripravljen na prihodnost**: Gradnja aplikacij, pripravljenih na nove tehnologije in vzorce AI

## Začetek

1. **Nastavitev okolja**: Zagotovite Windows 11 z priporočeno strojno opremo (glejte predpogoje)
2. **Namestitev Foundry Local**: Sledite seji 1 za popolno namestitev in konfiguracijo
3. **Zaženite primer 01**: Začnite z osnovno integracijo REST API za preverjanje nastavitve
4. **Napredujte skozi primere**: Dokončajte primere 01-10 za celovito obvladovanje

## Merila uspeha

Spremljajte svoj napredek skozi vseh 10 celovitih primerov:

### Osnovna raven (Primeri 01-03)
- [ ] Uspešno namestite in konfigurirajte Foundry Local
- [ ] Dokončajte integracijo REST API (Primer 01)
- [ ] Implementirajte združljivost z OpenAI SDK (Primer 02)
- [ ] Izvedite odkrivanje modelov in primerjavo zmogljivosti (Primer 03)

### Raven aplikacij (Primeri 04-06)
- [ ] Uvajajte in izvajajte vsaj 4 različne družine modelov
- [ ] Zgradite funkcionalno RAG aplikacijo za klepet (Primer 04)
- [ ] Ustvarite sistem za orkestracijo več agentov (Primer 05)
- [ ] Implementirajte inteligentno usmerjanje modelov (Primer 06)

### Raven napredne integracije (Primeri 07-10)
- [ ] Zgradite produkcijsko pripravljen API odjemalec (Primer 07)
- [ ] Razvijte domačo aplikacijo za klepet Windows 11 (Primer 08)
- [ ] Implementirajte napreden sistem več agentov (Primer 09)
- [ ] Ustvarite celovit okvir orodij (Primer 10)

### Kazalniki obvladovanja
- [ ] Uspešno zaženite vseh 10 primerov brez napak
- [ ] Prilagodite vsaj 3 primere za specifične primere uporabe
- [ ] Uvajajte 2+ primera v produkcijsko podobna okolja
- [ ] Prispevajte izboljšave ali razširitve k izvorni kodi primerov
- [ ] Integrirajte vzorce Foundry Local v osebne/profesionalne projekte

## Hiter vodič - Vsi 10 primerov

### Nastavitev okolja (zahtevano za vse primere)

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

### Osnovni primeri (01-06)

**Primer 01: REST Chat Quickstart**
```powershell
# Start Foundry Local service
foundry model run phi-4-mini

# Run REST chat demo
python samples/01/chat_quickstart.py
```

**Primer 02: OpenAI SDK Integration**
```powershell
# Ensure model is running
foundry status

# Run SDK demo
python samples/02/sdk_quickstart.py
```

**Primer 03: Model Discovery & Benchmarking**
```powershell
# Run comprehensive model testing
samples/03/list_and_bench.cmd

# Or run individual components
foundry model list --available
foundry model download qwen2.5-0.5b
foundry model benchmark phi-4-mini
```

**Primer 04: Chainlit RAG Application**
```powershell
# Install Chainlit dependencies
pip install chainlit langchain chromadb

# Start RAG chat application
chainlit run samples/04/app.py -w
# Opens browser at http://localhost:8000
```

**Primer 05: Multi-Agent Orchestration**
```powershell
# Run agent coordinator demo
python -m samples.05.agents.coordinator

# Run specific agent examples
python samples/05/examples/specialists_demo.py
```

**Primer 06: Models-as-Tools Router**
```powershell
# Configure environment
set BASE_URL=http://localhost:8000
set GENERAL_MODEL=phi-4-mini
set CODE_MODEL=qwen2.5-7b

# Run intelligent router
python samples/06/router.py "Analyze this Python code for performance issues"
```

### Napredni primeri (07-10)

**Primer 07: Direct API Client**
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

**Primer 08: Windows 11 Chat Application**
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

**Primer 09: Advanced Multi-Agent System**
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

**Primer 10: Foundry Tools Framework**
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

### Odpravljanje pogostih težav

**Napake pri povezavi Foundry Local**
```powershell
# Check service status
foundry status

# Restart if needed
foundry restart

# Verify endpoint accessibility
curl http://localhost:5273/v1/models
```

**Težave pri nalaganju modelov**
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

**Težave z odvisnostmi**
```powershell
# Upgrade pip and reinstall
python -m pip install --upgrade pip
pip install -r requirements.txt --force-reinstall

# For Node.js samples
npm cache clean --force
npm install
```

## Povzetek
Ta modul predstavlja vrhunec razvoja robne umetne inteligence, saj združuje Microsoftova orodja na ravni podjetij s prilagodljivostjo in inovativnostjo odprtokodnega ekosistema. Z obvladovanjem Foundry Local skozi vseh 10 celovitih primerov boste na čelu razvoja aplikacij umetne inteligence.

**Celotna učna pot:**
- **Osnove** (Primeri 01-03): Integracija API-jev in upravljanje modelov
- **Aplikacije** (Primeri 04-06): RAG, agenti in inteligentno usmerjanje
- **Napredno** (Primeri 07-10): Okviri za produkcijo in integracija na ravni podjetij

Za integracijo Azure OpenAI (Seja 2) si oglejte posamezne README datoteke primerov za potrebne okoljske spremenljivke in nastavitve različice API-ja.

---

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za strojno prevajanje [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne prevzemamo odgovornosti za morebitne nesporazume ali napačne razlage, ki izhajajo iz uporabe tega prevoda.
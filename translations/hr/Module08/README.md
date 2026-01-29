# Modul 08: Praktično iskustvo s Microsoft Foundry Local - Kompletan alat za razvoj

## Pregled

[Microsoft Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/) predstavlja novu generaciju razvoja AI tehnologije na rubnim uređajima, omogućujući programerima moćne alate za izgradnju, implementaciju i skaliranje AI aplikacija lokalno, uz besprijekornu integraciju s Azure AI Foundry. Ovaj modul pruža sveobuhvatan pregled Foundry Local-a, od instalacije do naprednog razvoja agenata.

**Ključne tehnologije:**
- Microsoft Foundry Local CLI i SDK
- Integracija s Azure AI Foundry
- Lokalna inferencija modela
- Predmemoriranje i optimizacija modela na uređaju
- Arhitekture temeljene na agentima

## Ciljevi učenja

Nakon završetka ovog modula, moći ćete:

- **Savladati Foundry Local**: Instalirati, konfigurirati i optimizirati za razvoj na Windows 11
- **Implementirati raznolike modele**: Pokretati phi, qwen, deepseek i GPT modele lokalno pomoću CLI naredbi
- **Izraditi produkcijska rješenja**: Kreirati AI aplikacije s naprednim inženjeringom upita i integracijom podataka
- **Iskoristiti otvoreni ekosustav**: Integrirati modele iz Hugging Face-a i doprinose zajednice
- **Razviti AI agente**: Izraditi inteligentne agente s mogućnostima utemeljenja i orkestracije
- **Primijeniti obrasce za poduzeća**: Kreirati modularna, skalabilna AI rješenja za produkcijsku implementaciju

## Struktura sesije

### [1: Početak rada s Foundry Local](./01.FoundryLocalSetup.md)
**Fokus**: Instalacija, postavljanje CLI-a, implementacija modela i optimizacija hardvera

**Ključne teme**: Kompletna instalacija • CLI naredbe • Predmemoriranje modela • Ubrzanje hardvera • Implementacija više modela

**Primjer**: [REST Chat Quickstart](./samples/01/README.md) • [OpenAI SDK Integracija](./samples/02/README.md) • [Otkrivanje i testiranje modela](./samples/03/README.md)

**Trajanje**: 2-3 sata | **Razina**: Početnik

---

### [2: Izgradnja AI rješenja s Azure AI Foundry](./02.AzureAIFoundryIntegration.md)
**Fokus**: Napredni inženjering upita, integracija podataka i povezivanje s oblakom

**Ključne teme**: Inženjering upita • Integracija podataka • Azure radni tokovi • Optimizacija performansi • Praćenje

**Primjer**: [Chainlit RAG aplikacija](./samples/04/README.md)

**Trajanje**: 2-3 sata | **Razina**: Srednja

---

### [3: Otvoreni modeli u Foundry Local](./03.OpenSourceModels.md)
**Fokus**: Integracija Hugging Face-a, strategije BYOM i modeli zajednice

**Ključne teme**: Integracija Hugging Face-a • Donošenje vlastitog modela • Uvidi iz Model Mondays • Doprinosi zajednice • Odabir modela

**Primjer**: [Orkestracija više agenata](./samples/05/README.md)

**Trajanje**: 2-3 sata | **Razina**: Srednja

---

### [4: Istraživanje najnaprednijih modela](./04.CuttingEdgeModels.md)
**Fokus**: LLM-ovi vs SLM-ovi, implementacija EdgeAI-a i napredni demo primjeri

**Ključne teme**: Usporedba modela • Inferencija na rubu vs oblaku • Phi + ONNX Runtime • Chainlit RAG aplikacija • Optimizacija WebGPU-a

**Primjer**: [Router za modele kao alate](./samples/06/README.md)

**Trajanje**: 3-4 sata | **Razina**: Napredna

---

### [5: Brza izrada AI agenata](./05.AIPoweredAgents.md)
**Fokus**: Arhitekture agenata, sistemski upiti, utemeljenje i orkestracija

**Ključne teme**: Obrasci dizajna agenata • Inženjering sistemskih upita • Tehnike utemeljenja • Sustavi s više agenata • Produkcijska implementacija

**Primjer**: [Orkestracija više agenata](./samples/05/README.md) • [Napredni sustav s više agenata](./samples/09/README.md)

**Trajanje**: 3-4 sata | **Razina**: Napredna

---

### [6: Foundry Local - modeli kao alati](./06.ModelsAsTools.md)
**Fokus**: Modularna AI rješenja, skaliranje za poduzeća i produkcijski obrasci

**Ključne teme**: Modeli kao alati • Implementacija na uređaju • SDK/API integracija • Arhitekture za poduzeća • Strategije skaliranja

**Primjer**: [Router za modele kao alate](./samples/06/README.md) • [Foundry Tools Framework](./samples/10/README.md)

**Trajanje**: 3-4 sata | **Razina**: Ekspert

---

### [7: Obrasci za direktnu API integraciju](./samples/07/README.md)
**Fokus**: Čista REST API integracija bez ovisnosti o SDK-u za maksimalnu kontrolu

**Ključne teme**: Implementacija HTTP klijenta • Prilagođena autentifikacija • Praćenje zdravlja modela • Streaming odgovora • Rukovanje greškama u produkciji

**Primjer**: [Direktni API klijent](./samples/07/README.md)

**Trajanje**: 2-3 sata | **Razina**: Srednja

---

### [8: Izrada nativne aplikacije za chat na Windows 11](./samples/08/README.md)
**Fokus**: Izrada modernih nativnih aplikacija za chat s integracijom Foundry Local-a

**Ključne teme**: Razvoj s Electronom • Fluent Design System • Nativna integracija s Windowsom • Streaming u stvarnom vremenu • Dizajn sučelja za chat

**Primjer**: [Aplikacija za chat na Windows 11](./samples/08/README.md)

**Trajanje**: 3-4 sata | **Razina**: Napredna

---

### [9: Napredna orkestracija više agenata](./samples/09/README.md)
**Fokus**: Sofisticirana koordinacija agenata, specijalizirana delegacija zadataka i suradnički AI radni tokovi

**Ključne teme**: Koordinacija inteligentnih agenata • Obrasci pozivanja funkcija • Komunikacija među agentima • Orkestracija radnih tokova • Mehanizmi osiguranja kvalitete

**Primjer**: [Napredni sustav s više agenata](./samples/09/README.md)

**Trajanje**: 4-5 sati | **Razina**: Ekspert

---

### [10: Foundry Local kao okvir za alate](./samples/10/README.md)
**Fokus**: Arhitektura usmjerena na alate za integraciju Foundry Local-a u postojeće aplikacije i okvire

**Ključne teme**: Integracija s LangChainom • Funkcije Semantic Kernel-a • REST API okviri • CLI alati • Integracija s Jupyterom • Obrasci za produkcijsku implementaciju

**Primjer**: [Foundry Tools Framework](./samples/10/README.md)

**Trajanje**: 4-5 sati | **Razina**: Ekspert

## Preduvjeti

### Sistemski zahtjevi
- **Operativni sustav**: Windows 11 (22H2 ili noviji)
- **Memorija**: 16GB RAM-a (32GB preporučeno za veće modele)
- **Pohrana**: 50GB slobodnog prostora za predmemoriranje modela
- **Hardver**: Preporučen uređaj s NPU-om (Copilot+ PC), GPU opcionalan
- **Mreža**: Brzi internet za početno preuzimanje modela

### Razvojno okruženje
- Visual Studio Code s AI Toolkit ekstenzijom
- Python 3.10+ i pip
- Git za kontrolu verzija
- PowerShell ili Command Prompt
- Azure CLI (opcionalno za integraciju s oblakom)

### Preduvjeti znanja
- Osnovno razumijevanje AI/ML koncepata
- Poznavanje naredbenog retka
- Osnove programiranja u Pythonu
- Koncepti REST API-ja
- Osnovno znanje o upitima i inferenciji modela

## Vremenski okvir modula

**Ukupno procijenjeno vrijeme**: 30-38 sati

| Sesija | Fokus područje | Primjeri | Vrijeme | Složenost |
|--------|----------------|----------|---------|-----------|
|  1 | Postavljanje i osnove | 01, 02, 03 | 2-3 sata | Početnik |
|  2 | AI rješenja | 04 | 2-3 sata | Srednja |
|  3 | Otvoreni modeli | 05 | 2-3 sata | Srednja |
|  4 | Napredni modeli | 06 | 3-4 sata | Napredna |
|  5 | AI agenti | 05, 09 | 3-4 sata | Napredna |
|  6 | Alati za poduzeća | 06, 10 | 3-4 sata | Ekspert |
|  7 | Direktna API integracija | 07 | 2-3 sata | Srednja |
|  8 | Chat aplikacija za Windows 11 | 08 | 3-4 sata | Napredna |
|  9 | Napredna orkestracija | 09 | 4-5 sati | Ekspert |
| 10 | Okvir za alate | 10 | 4-5 sati | Ekspert |

## Ključni resursi

**Službena dokumentacija:**
- [Microsoft Foundry Local GitHub](https://github.com/microsoft/Foundry-Local) - Izvorni kod i službeni primjeri
- [Azure AI Foundry Dokumentacija](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/) - Kompletan vodič za postavljanje i korištenje
- [Model Mondays Series](https://aka.ms/model-mondays) - Tjedni pregledi modela i vodiči

**Zajednica i podrška:**
- [Foundry Local Rasprave](https://github.com/microsoft/Foundry-Local/discussions) - Pitanja i prijedlozi zajednice
- [Microsoft AI Developer Community](https://techcommunity.microsoft.com/category/artificialintelligence) - Najnovije vijesti i najbolje prakse

## Ishodi učenja

Nakon završetka ovog modula, bit ćete osposobljeni za:

### Tehničko znanje
- **Implementacija i upravljanje**: Instalacije Foundry Local-a u razvojnim i produkcijskim okruženjima
- **Integracija modela**: Rad s raznolikim obiteljima modela iz Microsofta, Hugging Face-a i izvora zajednice
- **Izrada aplikacija**: Kreiranje produkcijski spremnih AI aplikacija s naprednim značajkama i optimizacijama
- **Razvoj agenata**: Implementacija sofisticiranih AI agenata s utemeljenjem, zaključivanjem i integracijom alata

### Strateško razumijevanje
- **Odluke o arhitekturi**: Donošenje informiranih odluka između lokalne i oblačne implementacije
- **Optimizacija performansi**: Optimizacija performansi inferencije na različitim hardverskim konfiguracijama
- **Skaliranje za poduzeća**: Dizajn aplikacija koje se skaliraju od lokalnih prototipova do implementacija u poduzećima
- **Privatnost i sigurnost**: Implementacija AI rješenja koja čuvaju privatnost uz lokalnu inferenciju

### Inovacijske sposobnosti
- **Brzo prototipiranje**: Brza izrada i testiranje AI koncepta aplikacija kroz svih 10 uzoraka
- **Integracija zajednice**: Iskorištavanje otvorenih modela i doprinos ekosustavu
- **Napredni obrasci**: Implementacija najnovijih AI obrazaca uključujući RAG, agente i integraciju alata
- **Ovladavanje okvirima**: Ekspertna integracija s LangChainom, Semantic Kernelom, Chainlitom i Electronom
- **Produkcijska implementacija**: Implementacija skalabilnih AI rješenja od lokalnih prototipova do sustava za poduzeća
- **Razvoj za budućnost**: Izrada aplikacija spremnih za nove AI tehnologije i obrasce

## Početak rada

1. **Postavljanje okruženja**: Osigurajte Windows 11 s preporučenim hardverom (vidi preduvjete)
2. **Instalirajte Foundry Local**: Slijedite Sesiju 1 za kompletnu instalaciju i konfiguraciju
3. **Pokrenite Primjer 01**: Započnite s osnovnom REST API integracijom kako biste provjerili postavke
4. **Napredujte kroz primjere**: Završite primjere 01-10 za sveobuhvatno ovladavanje

## Metrike uspjeha

Pratite svoj napredak kroz svih 10 sveobuhvatnih primjera:

### Osnovna razina (Primjeri 01-03)
- [ ] Uspješno instalirajte i konfigurirajte Foundry Local
- [ ] Završite REST API integraciju (Primjer 01)
- [ ] Implementirajte kompatibilnost s OpenAI SDK-om (Primjer 02)
- [ ] Provedite otkrivanje i testiranje modela (Primjer 03)

### Razina aplikacije (Primjeri 04-06)
- [ ] Implementirajte i pokrenite najmanje 4 različite obitelji modela
- [ ] Izradite funkcionalnu RAG aplikaciju za chat (Primjer 04)
- [ ] Kreirajte sustav za orkestraciju više agenata (Primjer 05)
- [ ] Implementirajte inteligentno usmjeravanje modela (Primjer 06)

### Razina napredne integracije (Primjeri 07-10)
- [ ] Izradite produkcijski spreman API klijent (Primjer 07)
- [ ] Razvijte nativnu aplikaciju za chat na Windows 11 (Primjer 08)
- [ ] Implementirajte napredni sustav s više agenata (Primjer 09)
- [ ] Kreirajte sveobuhvatan okvir za alate (Primjer 10)

### Indikatori ovladavanja
- [ ] Uspješno pokrenite svih 10 primjera bez grešaka
- [ ] Prilagodite najmanje 3 primjera za specifične slučajeve
- [ ] Implementirajte 2+ primjera u produkcijskim okruženjima
- [ ] Doprinite poboljšanjima ili proširenjima koda primjera
- [ ] Integrirajte obrasce Foundry Local-a u osobne/profesionalne projekte

## Vodič za brzi početak - Svi primjeri

### Postavljanje okruženja (Potrebno za sve primjere)

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

### Osnovni primjeri (01-06)

**Primjer 01: REST Chat Quickstart**
```powershell
# Start Foundry Local service
foundry model run phi-4-mini

# Run REST chat demo
python samples/01/chat_quickstart.py
```

**Primjer 02: OpenAI SDK Integracija**
```powershell
# Ensure model is running
foundry status

# Run SDK demo
python samples/02/sdk_quickstart.py
```

**Primjer 03: Otkrivanje i testiranje modela**
```powershell
# Run comprehensive model testing
samples/03/list_and_bench.cmd

# Or run individual components
foundry model list --available
foundry model download qwen2.5-0.5b
foundry model benchmark phi-4-mini
```

**Primjer 04: Chainlit RAG aplikacija**
```powershell
# Install Chainlit dependencies
pip install chainlit langchain chromadb

# Start RAG chat application
chainlit run samples/04/app.py -w
# Opens browser at http://localhost:8000
```

**Primjer 05: Orkestracija više agenata**
```powershell
# Run agent coordinator demo
python -m samples.05.agents.coordinator

# Run specific agent examples
python samples/05/examples/specialists_demo.py
```

**Primjer 06: Router za modele kao alate**
```powershell
# Configure environment
set BASE_URL=http://localhost:8000
set GENERAL_MODEL=phi-4-mini
set CODE_MODEL=qwen2.5-7b

# Run intelligent router
python samples/06/router.py "Analyze this Python code for performance issues"
```

### Napredni primjeri (07-10)

**Primjer 07: Direktni API klijent**
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

**Primjer 08: Aplikacija za chat na Windows 11**
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

**Primjer 09: Napredni sustav s više agenata**
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

**Primjer 10: Foundry Tools Framework**
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

### Rješavanje uobičajenih problema

**Problemi s povezivanjem Foundry Local-a**
```powershell
# Check service status
foundry status

# Restart if needed
foundry restart

# Verify endpoint accessibility
curl http://localhost:5273/v1/models
```

**Problemi s učitavanjem modela**
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

**Problemi s ovisnostima**
```powershell
# Upgrade pip and reinstall
python -m pip install --upgrade pip
pip install -r requirements.txt --force-reinstall

# For Node.js samples
npm cache clean --force
npm install
```

## Sažetak
Ovaj modul predstavlja vrhunac razvoja rubne umjetne inteligencije, kombinirajući Microsoftove alate na razini poduzeća s fleksibilnošću i inovacijama otvorenog ekosustava. Savladavanjem Foundry Local kroz svih 10 sveobuhvatnih primjera, bit ćete na čelu razvoja AI aplikacija.

**Kompletan put učenja:**
- **Osnove** (Primjeri 01-03): Integracija API-ja i upravljanje modelima
- **Aplikacije** (Primjeri 04-06): RAG, agenti i inteligentno usmjeravanje
- **Napredno** (Primjeri 07-10): Okviri za produkciju i integracija u poduzeće

Za integraciju s Azure OpenAI (Sesija 2), pogledajte pojedinačne README datoteke primjera za potrebne varijable okruženja i postavke verzije API-ja.

---

**Izjava o odricanju odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane ljudskog prevoditelja. Ne preuzimamo odgovornost za nesporazume ili pogrešna tumačenja koja mogu proizaći iz korištenja ovog prijevoda.
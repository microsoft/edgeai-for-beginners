# AGENTS.md

> **Vodič za razvoj EdgeAI za početnike**
> 
> Ovaj dokument pruža sveobuhvatne informacije za programere, AI agente i suradnike koji rade s ovim repozitorijem. Pokriva postavljanje, razvojne tijekove rada, testiranje i najbolje prakse.
> 
> **Zadnje ažuriranje**: 30. listopada 2025 | **Verzija dokumenta**: 3.0

## Sadržaj

- [Pregled projekta](../..)
- [Struktura repozitorija](../..)
- [Preduvjeti](../..)
- [Komande za postavljanje](../..)
- [Razvojni tijek rada](../..)
- [Upute za testiranje](../..)
- [Smjernice za stil koda](../..)
- [Smjernice za Pull Request](../..)
- [Sustav za prijevod](../..)
- [Integracija Foundry Local](../..)
- [Izgradnja i implementacija](../..)
- [Uobičajeni problemi i rješavanje](../..)
- [Dodatni resursi](../..)
- [Napomene specifične za projekt](../..)
- [Dobivanje pomoći](../..)

## Pregled projekta

EdgeAI za početnike je sveobuhvatan edukacijski repozitorij koji podučava razvoj Edge AI-a s malim jezičnim modelima (SLM). Tečaj pokriva osnove EdgeAI-a, implementaciju modela, tehnike optimizacije i implementacije spremne za produkciju koristeći Microsoft Foundry Local i razne AI okvire.

**Ključne tehnologije:**
- Python 3.8+ (primarni jezik za AI/ML primjere)
- .NET C# (AI/ML primjeri)
- JavaScript/Node.js s Electronom (za desktop aplikacije)
- Microsoft Foundry Local SDK
- Microsoft Windows ML 
- VSCode AI Toolkit
- OpenAI SDK
- AI okviri: LangChain, Semantic Kernel, Chainlit
- Optimizacija modela: Llama.cpp, Microsoft Olive, OpenVINO, Apple MLX

**Vrsta repozitorija:** Edukacijski sadržaj s 8 modula i 10 sveobuhvatnih primjera aplikacija

**Arhitektura:** Višemodulski edukacijski put s praktičnim primjerima koji demonstriraju Edge AI obrasce implementacije

## Struktura repozitorija

```
edgeai-for-beginners/
├── introduction.md          # Course introduction and overview
├── Module01-07/            # Core educational modules (Markdown)
├── Module08/               # Foundry Local toolkit with 10 samples
│   ├── samples/01-06/     # Foundation samples (Python)
│   ├── samples/07/        # API client (Python)
│   ├── samples/08/        # Windows 11 chat app (Electron)
│   └── samples/09-10/     # Advanced multi-agent systems (Python)
├── Workshop/               # Hands-on workshop materials
│   ├── samples/           # Workshop Python samples with utilities
│   │   ├── session01/     # Chat bootstrap samples
│   │   ├── session02-06/  # Progressive workshop sessions
│   │   └── util/          # Workshop utility modules
│   ├── notebooks/         # Jupyter notebook tutorials
│   └── scripts/           # Validation and testing tools
├── translations/          # Multi-language translations (50+ languages)
├── translated_images/     # Localized images
└── imgs/                  # Course images and assets
```

## Preduvjeti

### Potrebni alati

- **Python 3.8+** - Za AI/ML primjere i bilježnice
- **Node.js 16+** - Za Electron primjer aplikacije
- **Git** - Za kontrolu verzija
- **Microsoft Foundry Local** - Za lokalno pokretanje AI modela

### Preporučeni alati

- **Visual Studio Code** - S ekstenzijama za Python, Jupyter i Pylance
- **Windows Terminal** - Za bolji rad s naredbenim retkom (korisnici Windowsa)
- **Docker** - Za razvoj u kontejnerima (opcionalno)

### Zahtjevi sustava

- **RAM**: Minimalno 8GB, preporučeno 16GB+ za scenarije s više modela
- **Pohrana**: 10GB+ slobodnog prostora za modele i ovisnosti
- **OS**: Windows 10/11, macOS 11+, ili Linux (Ubuntu 20.04+)
- **Hardver**: CPU s podrškom za AVX2; GPU (CUDA, Qualcomm NPU) opcionalno, ali preporučeno

### Preduvjeti znanja

- Osnovno razumijevanje programiranja u Pythonu
- Poznavanje sučelja naredbenog retka
- Razumijevanje AI/ML koncepata (za razvoj primjera)
- Git tijekovi rada i procesi Pull Requesta

## Komande za postavljanje

### Postavljanje repozitorija

```bash
# Clone the repository
git clone https://github.com/microsoft/edgeai-for-beginners.git
cd edgeai-for-beginners

# No build step required - this is primarily an educational content repository
```

### Postavljanje Python primjera (Modul08 i primjeri radionice)

```bash
# Create and activate virtual environment
python -m venv .venv
# On Windows
.venv\Scripts\activate
# On macOS/Linux
source .venv/bin/activate

# Install Foundry Local SDK and dependencies
pip install foundry-local-sdk openai

# Install additional dependencies for Module08 samples
cd Module08
pip install -r requirements.txt

# Install Workshop dependencies
cd ../Workshop
pip install -r requirements.txt
```

### Postavljanje Node.js primjera (Primjer 08 - Windows Chat aplikacija)

```bash
cd Module08/samples/08
npm install

# Start in development mode
npm run dev

# Build for production
npm run build

# Create installer
npm run dist
```

### Postavljanje Foundry Local

Foundry Local je potreban za pokretanje primjera. Preuzmite i instalirajte s službenog repozitorija:

**Instalacija:**
- **Windows**: `winget install Microsoft.FoundryLocal`
- **macOS**: `brew tap microsoft/foundrylocal && brew install foundrylocal`
- **Ručno**: Preuzmite s [stranice izdanja](https://github.com/microsoft/Foundry-Local/releases)

**Brzi početak:**
```bash
# Run your first model (auto-downloads if needed)
foundry model run phi-4-mini

# List available models
foundry model ls

# Check service status
foundry service status
```

**Napomena**: Foundry Local automatski odabire najbolju varijantu modela za vaš hardver (CUDA GPU, Qualcomm NPU ili CPU).

## Razvojni tijek rada

### Razvoj sadržaja

Ovaj repozitorij primarno sadrži **Markdown edukacijski sadržaj**. Prilikom izmjena:

1. Uredite `.md` datoteke u odgovarajućim direktorijima modula
2. Slijedite postojeće obrasce formatiranja
3. Osigurajte da su primjeri koda točni i testirani
4. Ažurirajte odgovarajući prevedeni sadržaj ako je potrebno (ili neka automatizacija to obavi)

### Razvoj primjera aplikacija

Za Python primjere Modula08 (primjeri 01-07, 09-10):
```bash
cd Module08
python samples/01/chat_quickstart.py "Test message"
```

Za Python primjere radionice:
```bash
cd Workshop/samples/session01
python chat_bootstrap.py "Test message"
```

Za Electron primjer (primjer 08):
```bash
cd Module08/samples/08
npm run dev  # Development with hot reload
```

### Testiranje primjera aplikacija

Python primjeri nemaju automatizirane testove, ali se mogu validirati pokretanjem:
```bash
# Test basic chat functionality
python samples/01/chat_quickstart.py "Hello"

# Test with specific model
set MODEL=phi-4-mini
python samples/02/openai_sdk_client.py
```

Electron primjer ima infrastrukturu za testiranje:
```bash
cd Module08/samples/08
npm test           # Run unit tests
npm run test:e2e   # Run end-to-end tests
npm run lint       # Check code style
```

## Upute za testiranje

### Validacija sadržaja

Repozitorij koristi automatizirane tijekove rada za prijevod. Nije potrebno ručno testiranje prijevoda.

**Ručno testiranje promjena sadržaja:**
1. Pregledajte prikaz Markdown datoteka
2. Provjerite da svi linkovi vode na valjane ciljeve
3. Testirajte sve uključene primjere koda
4. Provjerite da se slike ispravno učitavaju

### Testiranje primjera aplikacija

**Modul08/primjeri/08 (Electron aplikacija) ima sveobuhvatno testiranje:**
```bash
cd Module08/samples/08

# Run all tests
npm test

# Run unit tests only
npm test -- --testPathPattern=unit

# Run integration tests
npm run test:integration

# Run E2E tests
npm run test:e2e

# Check test coverage
npm test -- --coverage
```

**Python primjere treba ručno testirati:**
```bash
# Module08 samples
python samples/01/chat_quickstart.py "Test prompt"
python samples/04/chainlit_rag.py
python samples/09/multi_agent_system.py

# Workshop samples
cd Workshop/samples/session01
python chat_bootstrap.py "Test prompt"

# Use Workshop validation tools
cd Workshop/scripts
python validate_samples.py  # Validate syntax and imports
python test_samples.py      # Run smoke tests
```

## Smjernice za stil koda

### Markdown sadržaj

- Koristite dosljednu hijerarhiju naslova (# za naslov, ## za glavne sekcije, ### za podsekcije)
- Uključite blokove koda s oznakama jezika: ```python, ```bash, ```javascript
- Slijedite postojeće formatiranje za tablice, liste i naglašavanje
- Održavajte čitljivost linija (~80-100 znakova, ali nije strogo)
- Koristite relativne linkove za interne reference

### Python stil koda

- Slijedite PEP 8 konvencije
- Koristite tipove gdje je prikladno
- Uključite docstringove za funkcije i klase
- Koristite smislena imena varijabli
- Održavajte funkcije fokusirane i sažete

### JavaScript/Node.js stil koda

```bash
# Electron sample follows ESLint configuration
cd Module08/samples/08
npm run lint        # Check for style issues
npm run lint:fix    # Auto-fix style issues
npm run format      # Format with Prettier
```

**Ključne konvencije:**
- ESLint konfiguracija dostupna u primjeru 08
- Prettier za formatiranje koda
- Koristite modernu ES6+ sintaksu
- Slijedite postojeće obrasce u kodnoj bazi

## Smjernice za Pull Request

### Tijek doprinosa

1. **Forkajte repozitorij** i kreirajte novu granu iz `main`
2. **Napravite izmjene** slijedeći smjernice za stil koda
3. **Temeljito testirajte** koristeći gore navedene upute za testiranje
4. **Commitajte s jasnim porukama** slijedeći format konvencionalnih commitova
5. **Pushajte na svoj fork** i kreirajte Pull Request
6. **Odgovarajte na povratne informacije** od održavatelja tijekom pregleda

### Konvencija imenovanja grana

- `feature/<modul>-<opis>` - Za nove značajke ili sadržaj
- `fix/<modul>-<opis>` - Za ispravke grešaka
- `docs/<opis>` - Za poboljšanja dokumentacije
- `refactor/<opis>` - Za refaktoriranje koda

### Format poruke commita

Slijedite [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

**Primjeri:**
```
feat(Module08): add intent-based routing notebook
docs(AGENTS): update Foundry Local setup instructions
fix(samples/08): resolve Electron build issue
```

### Format naslova
```
[ModuleXX] Brief description of change
```
ili
```
[Module08/samples/XX] Description for sample changes
```

### Kodeks ponašanja

Svi suradnici moraju slijediti [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/). Molimo pregledajte [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) prije doprinosa.

### Prije slanja

**Za promjene sadržaja:**
- Pregledajte sve izmijenjene Markdown datoteke
- Provjerite da linkovi i slike rade
- Provjerite pravopisne i gramatičke pogreške

**Za promjene primjera koda (Modul08/primjeri/08):**
```bash
npm run lint
npm test
```

**Za promjene Python primjera:**
- Testirajte da primjer uspješno radi
- Provjerite da rukovanje greškama funkcionira
- Provjerite kompatibilnost s Foundry Local

### Proces pregleda

- Promjene edukacijskog sadržaja pregledavaju se za točnost i jasnoću
- Primjeri koda testiraju se za funkcionalnost
- Ažuriranja prijevoda automatski obrađuje GitHub Actions

## Sustav za prijevod

**VAŽNO:** Ovaj repozitorij koristi automatizirani prijevod putem GitHub Actions.

- Prijevodi se nalaze u direktoriju `/translations/` (50+ jezika)
- Automatizirano putem `co-op-translator.yml` tijeka rada
- **NE uređujte ručno datoteke prijevoda** - bit će prepisane
- Uređujte samo izvorne datoteke na engleskom jeziku u rootu i direktorijima modula
- Prijevodi se automatski generiraju prilikom pushanja na `main` granu

## Integracija Foundry Local

Većina primjera Modula08 zahtijeva da Microsoft Foundry Local bude pokrenut.

### Instalacija i postavljanje

**Instalirajte Foundry Local:**
```bash
# Windows
winget install Microsoft.FoundryLocal

# macOS
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**Instalirajte Python SDK:**
```bash
pip install foundry-local-sdk openai
```

### Pokretanje Foundry Local
```bash
# Start service and run a model (auto-downloads if needed)
foundry model run phi-3.5-mini

# Or use model aliases for automatic hardware optimization
foundry model run phi-4-mini
foundry model run qwen2.5-0.5b
foundry model run qwen2.5-coder-0.5b

# Check service status
foundry service status

# List available models
foundry model ls
```

### Korištenje SDK-a (Python)
```python
from foundry_local import FoundryLocalManager
import openai

# Use model alias for automatic hardware optimization
alias = "phi-4-mini"

# Create manager (auto-starts service and loads model)
manager = FoundryLocalManager(alias)

# Configure OpenAI client for local Foundry service
client = openai.OpenAI(
    base_url=manager.endpoint,
    api_key=manager.api_key
)

# Use the model
response = client.chat.completions.create(
    model=manager.get_model_info(alias).id,
    messages=[{"role": "user", "content": "Hello!"}]
)
```

### Provjera Foundry Local
```bash
# Service status and endpoint
foundry service status

# List loaded models (REST API)
curl http://localhost:<port>/v1/models

# Note: Port is displayed when running 'foundry service status'
```

### Varijable okruženja za primjere

Većina primjera koristi ove varijable okruženja:
```bash
# Foundry Local configuration
# Note: The SDK (FoundryLocalManager) automatically detects endpoint
set MODEL=phi-4-mini  # or phi-3.5-mini, qwen2.5-0.5b, qwen2.5-coder-0.5b
set API_KEY=            # Not required for local usage

# Manual endpoint (if not using SDK)
# Port is shown via 'foundry service status'
set BASE_URL=http://localhost:<port>

# For Azure OpenAI fallback (optional)
set AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
set AZURE_OPENAI_API_KEY=your-api-key
set AZURE_OPENAI_API_VERSION=2024-08-01-preview
```

**Napomena**: Kada koristite `FoundryLocalManager`, SDK automatski upravlja otkrivanjem usluga i učitavanjem modela. Alias modela (poput `phi-3.5-mini`) osigurava odabir najbolje varijante za vaš hardver.

## Izgradnja i implementacija

### Implementacija sadržaja

Ovaj repozitorij je primarno dokumentacija - nije potreban proces izgradnje za sadržaj.

### Izgradnja primjera aplikacija

**Electron aplikacija (Modul08/primjeri/08):**
```bash
cd Module08/samples/08

# Development build
npm run dev

# Production build
npm run build

# Create Windows installer
npm run dist

# Create portable executable
npm run pack
```

**Python primjeri:**
Nema procesa izgradnje - primjeri se pokreću direktno s Python interpreterom.

## Uobičajeni problemi i rješavanje

> **Savjet**: Provjerite [GitHub Issues](https://github.com/microsoft/edgeai-for-beginners/issues) za poznate probleme i rješenja.

### Kritični problemi (blokirajući)

#### Foundry Local nije pokrenut
**Problem:** Primjeri ne rade zbog grešaka u povezivanju

**Rješenje:**
```bash
# Check if service is running
foundry service status

# Start service with a model
foundry model run phi-4-mini

# Or explicitly start service
foundry service start

# List loaded models
foundry model ls

# Verify via REST API (port shown in 'foundry service status')
curl http://localhost:<port>/v1/models
```

### Uobičajeni problemi (umjereni)

#### Problemi s Python virtualnim okruženjem
**Problem:** Greške pri uvozu modula

**Rješenje:**
```bash
# Ensure virtual environment is activated
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt
```

#### Problemi s izgradnjom Electron aplikacije
**Problem:** Greške pri npm instalaciji ili izgradnji

**Rješenje:**
```bash
cd Module08/samples/08
# Clean install
npm run clean
rm -rf node_modules package-lock.json
npm install
```

### Problemi s tijekovima rada (manji)

#### Sukobi u tijeku rada za prijevod
**Problem:** Sukobi u PR-u za prijevod s vašim izmjenama

**Rješenje:**
- Uređujte samo izvorne datoteke na engleskom jeziku
- Neka automatizirani tijek rada za prijevod obavi prijevode
- Ako dođe do sukoba, spojite `main` u svoju granu nakon što se prijevodi spoje

#### Neuspješno preuzimanje modela
**Problem:** Foundry Local ne uspijeva preuzeti modele

**Rješenje:**
```bash
# Check internet connectivity
# Clear model cache and retry
foundry model remove <model-alias>
foundry model run <model-alias>

# Check available disk space (models can be 2-16GB)
# Verify firewall settings allow downloads
```

## Dodatni resursi

### Edukacijski putovi
- **Put za početnike:** Moduli 01-02 (7-9 sati)
- **Put za srednji nivo:** Moduli 03-04 (9-11 sati)
- **Put za napredni nivo:** Moduli 05-07 (12-15 sati)
- **Put za stručnjake:** Modul 08 (8-10 sati)
- **Radionica:** Materijali za radionicu (6-8 sati)

### Ključni sadržaj modula
- **Modul01:** Osnove EdgeAI-a i studije slučaja iz stvarnog svijeta
- **Modul02:** Obitelji i arhitekture malih jezičnih modela (SLM)
- **Modul03:** Strategije lokalne i cloud implementacije
- **Modul04:** Optimizacija modela s više okvira (Llama.cpp, Microsoft Olive, OpenVINO, Qualcomm QNN, Apple MLX)
- **Modul05:** SLMOps - operacije u produkciji
- **Modul06:** AI agenti i pozivanje funkcija
- **Modul07:** Implementacije specifične za platformu
- **Modul08:** Foundry Local alatni set s 10 sveobuhvatnih primjera

### Vanjske ovisnosti
- [Microsoft Foundry Local](https://github.com/microsoft/Foundry-Local) - Lokalno AI okruženje kompatibilno s OpenAI API-jem
  - [Dokumentacija](https://github.com/microsoft/Foundry-Local/blob/main/docs/README.md)
  - [Python SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/python)
  - [JavaScript SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/javascript)
- [Llama.cpp](https://github.com/ggml-org/llama.cpp) - Okvir za optimizaciju
- [Microsoft Olive](https://microsoft.github.io/Olive/) - Alat za optimizaciju modela
- [OpenVINO](https://docs.openvino.ai/) - Intelov alat za optimizaciju

## Napomene specifične za projekt

### Modul08 Primjeri aplikacija

Repozitorij uključuje 10 sveobuhvatnih primjera aplikacija:

1. **01-REST Chat Quickstart** - Osnovna integracija OpenAI SDK-a
2. **02-OpenAI SDK Integration** - Napredne značajke SDK-a
3. **03-Model Discovery & Benchmarking** - Alati za usporedbu modela
4. **04-Chainlit RAG Application** - Generacija uz pomoć pretraživanja
5. **05-Multi-Agent Orchestration** - Osnovna koordinacija agenata
6. **06-Models-as-Tools Router** - Inteligentno usmjeravanje modela
7. **07-Direct API Client** - Niskorazinska integracija API-ja
8. **08-Windows 11 Chat App** - Nativna Electron desktop aplikacija
9. **09-Advanced Multi-Agent System** - Kompleksna koordinacija agenata
10. **10-Alati Foundry Framework** - Integracija LangChain/Semantic Kernel

### Primjeri aplikacija za radionicu

Radionica uključuje 6 progresivnih sesija s praktičnim implementacijama:

1. **Sesija 01** - Pokretanje chata s integracijom Foundry Local
2. **Sesija 02** - RAG pipeline i evaluacija s RAGAS
3. **Sesija 03** - Benchmarking modela otvorenog koda
4. **Sesija 04** - Usporedba i odabir modela
5. **Sesija 05** - Sustavi za orkestraciju više agenata
6. **Sesija 06** - Usmjeravanje modela i upravljanje pipelineom

Svaki primjer prikazuje različite aspekte razvoja edge AI-a s Foundry Local.

### Razmatranja o performansama

- SLM-ovi su optimizirani za edge implementaciju (2-16GB RAM-a)
- Lokalna inferencija omogućuje vrijeme odgovora od 50-500ms
- Tehnike kvantizacije postižu smanjenje veličine za 75% uz zadržavanje 85% performansi
- Mogućnosti za razgovor u stvarnom vremenu s lokalnim modelima

### Sigurnost i privatnost

- Sva obrada odvija se lokalno - nema slanja podataka u oblak
- Pogodno za aplikacije osjetljive na privatnost (zdravstvo, financije)
- Zadovoljava zahtjeve za suverenitet podataka
- Foundry Local radi u potpunosti na lokalnom hardveru

## Dobivanje pomoći

### Dokumentacija

- **Glavni README**: [README.md](README.md) - Pregled repozitorija i putovi učenja
- **Vodič za učenje**: [STUDY_GUIDE.md](STUDY_GUIDE.md) - Resursi za učenje i vremenski okvir
- **Podrška**: [SUPPORT.md](SUPPORT.md) - Kako dobiti pomoć
- **Sigurnost**: [SECURITY.md](SECURITY.md) - Prijava sigurnosnih problema

### Podrška zajednice

- **GitHub Issues**: [Prijavite greške ili zatražite značajke](https://github.com/microsoft/edgeai-for-beginners/issues)
- **GitHub Discussions**: [Postavite pitanja i podijelite ideje](https://github.com/microsoft/edgeai-for-beginners/discussions)
- **Foundry Local Issues**: [Tehnički problemi s Foundry Local](https://github.com/microsoft/Foundry-Local/issues)

### Kontakt

- **Održavatelji**: Pogledajte [CODEOWNERS](https://github.com/microsoft/edgeai-for-beginners/blob/main/.github/CODEOWNERS)
- **Sigurnosni problemi**: Slijedite odgovorno prijavljivanje u [SECURITY.md](SECURITY.md)
- **Microsoft podrška**: Za podršku za poduzeća, kontaktirajte Microsoft korisničku službu

### Dodatni resursi

- **Microsoft Learn**: [Putovi učenja o AI-u i strojnom učenju](https://learn.microsoft.com/training/browse/?products=ai-services)
- **Foundry Local Dokumentacija**: [Službena dokumentacija](https://github.com/microsoft/Foundry-Local/blob/main/docs/README.md)
- **Primjeri zajednice**: Provjerite [GitHub Discussions](https://github.com/microsoft/edgeai-for-beginners/discussions) za doprinose zajednice

---

**Ovo je edukacijski repozitorij usmjeren na podučavanje razvoja Edge AI-a. Primarni obrazac doprinosa je poboljšanje edukacijskog sadržaja i dodavanje/poboljšanje primjera aplikacija koje demonstriraju koncepte Edge AI-a.**

---

**Izjava o odricanju odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane ljudskog prevoditelja. Ne preuzimamo odgovornost za nesporazume ili pogrešne interpretacije nastale korištenjem ovog prijevoda.
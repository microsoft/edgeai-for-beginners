# AGENTS.md

> **Ghid pentru dezvoltatori care contribuie la EdgeAI pentru începători**
> 
> Acest document oferă informații detaliate pentru dezvoltatori, agenți AI și colaboratori care lucrează cu acest depozit. Acesta acoperă configurarea, fluxurile de lucru de dezvoltare, testarea și cele mai bune practici.
> 
> **Ultima actualizare**: 30 octombrie 2025 | **Versiunea documentului**: 3.0

## Cuprins

- [Prezentare generală a proiectului](../..)
- [Structura depozitului](../..)
- [Prerechizite](../..)
- [Comenzi de configurare](../..)
- [Flux de lucru de dezvoltare](../..)
- [Instrucțiuni de testare](../..)
- [Ghiduri de stil pentru cod](../..)
- [Ghiduri pentru cererile de pull](../..)
- [Sistem de traducere](../..)
- [Integrarea locală Foundry](../..)
- [Construire și implementare](../..)
- [Probleme comune și depanare](../..)
- [Resurse suplimentare](../..)
- [Note specifice proiectului](../..)
- [Obținerea ajutorului](../..)

## Prezentare generală a proiectului

EdgeAI pentru începători este un depozit educațional cuprinzător care predă dezvoltarea Edge AI cu modele de limbaj mici (SLM). Cursul acoperă fundamentele EdgeAI, implementarea modelelor, tehnici de optimizare și implementări pregătite pentru producție utilizând Microsoft Foundry Local și diverse cadre AI.

**Tehnologii cheie:**
- Python 3.8+ (limbaj principal pentru exemple AI/ML)
- .NET C# (exemple AI/ML)
- JavaScript/Node.js cu Electron (pentru aplicații desktop)
- Microsoft Foundry Local SDK
- Microsoft Windows ML 
- VSCode AI Toolkit
- OpenAI SDK
- Cadre AI: LangChain, Semantic Kernel, Chainlit
- Optimizarea modelelor: Llama.cpp, Microsoft Olive, OpenVINO, Apple MLX

**Tip depozit:** Depozit de conținut educațional cu 8 module și 10 aplicații de exemplu cuprinzătoare

**Arhitectură:** Parcurs de învățare multi-modul cu exemple practice care demonstrează modele de implementare Edge AI

## Structura depozitului

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

## Prerechizite

### Instrumente necesare

- **Python 3.8+** - Pentru exemple AI/ML și notebook-uri
- **Node.js 16+** - Pentru aplicația de exemplu Electron
- **Git** - Pentru controlul versiunilor
- **Microsoft Foundry Local** - Pentru rularea modelelor AI local

### Instrumente recomandate

- **Visual Studio Code** - Cu extensiile Python, Jupyter și Pylance
- **Windows Terminal** - Pentru o experiență mai bună în linia de comandă (utilizatorii Windows)
- **Docker** - Pentru dezvoltare containerizată (opțional)

### Cerințe de sistem

- **RAM**: minim 8GB, recomandat 16GB+ pentru scenarii multi-model
- **Spațiu de stocare**: minim 10GB spațiu liber pentru modele și dependențe
- **OS**: Windows 10/11, macOS 11+ sau Linux (Ubuntu 20.04+)
- **Hardware**: CPU cu suport AVX2; GPU (CUDA, Qualcomm NPU) opțional, dar recomandat

### Prerechizite de cunoștințe

- Înțelegerea de bază a programării în Python
- Familiaritate cu interfețele de linie de comandă
- Înțelegerea conceptelor AI/ML (pentru dezvoltarea exemplelor)
- Fluxuri de lucru Git și procese de cereri de pull

## Comenzi de configurare

### Configurarea depozitului

```bash
# Clone the repository
git clone https://github.com/microsoft/edgeai-for-beginners.git
cd edgeai-for-beginners

# No build step required - this is primarily an educational content repository
```

### Configurarea exemplelor Python (Module08 și exemple Workshop)

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

### Configurarea exemplelor Node.js (Exemplu 08 - Aplicație Chat Windows)

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

### Configurarea Foundry Local

Foundry Local este necesar pentru a rula exemplele. Descărcați și instalați din depozitul oficial:

**Instalare:**
- **Windows**: `winget install Microsoft.FoundryLocal`
- **macOS**: `brew tap microsoft/foundrylocal && brew install foundrylocal`
- **Manual**: Descărcați de pe [pagina de lansări](https://github.com/microsoft/Foundry-Local/releases)

**Start rapid:**
```bash
# Run your first model (auto-downloads if needed)
foundry model run phi-4-mini

# List available models
foundry model ls

# Check service status
foundry service status
```

**Notă**: Foundry Local selectează automat cea mai bună variantă de model pentru hardware-ul dvs. (GPU CUDA, NPU Qualcomm sau CPU).

## Flux de lucru de dezvoltare

### Dezvoltarea conținutului

Acest depozit conține în principal **conținut educațional Markdown**. Când faceți modificări:

1. Editați fișierele `.md` în directoarele de module corespunzătoare
2. Urmați modelele de formatare existente
3. Asigurați-vă că exemplele de cod sunt corecte și testate
4. Actualizați conținutul tradus corespunzător, dacă este necesar (sau lăsați automatizarea să se ocupe de asta)

### Dezvoltarea aplicațiilor de exemplu

Pentru exemplele Python din Module08 (exemple 01-07, 09-10):
```bash
cd Module08
python samples/01/chat_quickstart.py "Test message"
```

Pentru exemplele Python din Workshop:
```bash
cd Workshop/samples/session01
python chat_bootstrap.py "Test message"
```

Pentru exemplul Electron (exemplu 08):
```bash
cd Module08/samples/08
npm run dev  # Development with hot reload
```

### Testarea aplicațiilor de exemplu

Exemplele Python nu au teste automate, dar pot fi validate prin rularea lor:
```bash
# Test basic chat functionality
python samples/01/chat_quickstart.py "Hello"

# Test with specific model
set MODEL=phi-4-mini
python samples/02/openai_sdk_client.py
```

Exemplul Electron are infrastructură de testare:
```bash
cd Module08/samples/08
npm test           # Run unit tests
npm run test:e2e   # Run end-to-end tests
npm run lint       # Check code style
```

## Instrucțiuni de testare

### Validarea conținutului

Depozitul utilizează fluxuri de lucru automate de traducere. Nu este necesară testarea manuală pentru traduceri.

**Validare manuală pentru modificările de conținut:**
1. Revizuiți redarea Markdown prin previzualizarea fișierelor `.md`
2. Verificați dacă toate linkurile indică destinații valide
3. Testați orice fragmente de cod incluse în documentație
4. Verificați dacă imaginile se încarcă corect

### Testarea aplicațiilor de exemplu

**Module08/exemple/08 (aplicația Electron) are teste cuprinzătoare:**
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

**Exemplele Python trebuie testate manual:**
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

## Ghiduri de stil pentru cod

### Conținut Markdown

- Utilizați o ierarhie consistentă a titlurilor (# pentru titlu, ## pentru secțiuni principale, ### pentru subsecțiuni)
- Includeți blocuri de cod cu specificatori de limbaj: ```python, ```bash, ```javascript
- Urmați formatarea existentă pentru tabele, liste și accentuări
- Păstrați liniile lizibile (aproximativ 80-100 de caractere, dar nu strict)
- Utilizați linkuri relative pentru referințe interne

### Stilul codului Python

- Urmați convențiile PEP 8
- Utilizați indicii de tip acolo unde este cazul
- Includeți docstrings pentru funcții și clase
- Folosiți nume de variabile semnificative
- Păstrați funcțiile concentrate și concise

### Stilul codului JavaScript/Node.js

```bash
# Electron sample follows ESLint configuration
cd Module08/samples/08
npm run lint        # Check for style issues
npm run lint:fix    # Auto-fix style issues
npm run format      # Format with Prettier
```

**Convenții cheie:**
- Configurația ESLint este furnizată în exemplul 08
- Prettier pentru formatarea codului
- Utilizați sintaxa modernă ES6+
- Urmați modelele existente în baza de cod

## Ghiduri pentru cererile de pull

### Flux de lucru pentru contribuții

1. **Fork depozitul** și creați o nouă ramură din `main`
2. **Faceți modificările** urmând ghidurile de stil pentru cod
3. **Testați temeinic** utilizând instrucțiunile de testare de mai sus
4. **Faceți commit cu mesaje clare** urmând formatul convențional pentru commit-uri
5. **Push către fork-ul dvs.** și creați o cerere de pull
6. **Răspundeți la feedback** de la mentori în timpul revizuirii

### Convenția de denumire a ramurilor

- `feature/<module>-<description>` - Pentru funcționalități noi sau conținut
- `fix/<module>-<description>` - Pentru corectarea erorilor
- `docs/<description>` - Pentru îmbunătățirea documentației
- `refactor/<description>` - Pentru refactorizarea codului

### Formatul mesajului de commit

Urmați [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

**Exemple:**
```
feat(Module08): add intent-based routing notebook
docs(AGENTS): update Foundry Local setup instructions
fix(samples/08): resolve Electron build issue
```

### Formatul titlului
```
[ModuleXX] Brief description of change
```
sau
```
[Module08/samples/XX] Description for sample changes
```

### Cod de conduită

Toți colaboratorii trebuie să urmeze [Codul de conduită Microsoft Open Source](https://opensource.microsoft.com/codeofconduct/). Vă rugăm să consultați [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) înainte de a contribui.

### Înainte de a trimite

**Pentru modificările de conținut:**
- Previzualizați toate fișierele Markdown modificate
- Verificați dacă linkurile și imaginile funcționează
- Verificați pentru greșeli de tipar și erori gramaticale

**Pentru modificările codului de exemplu (Module08/exemple/08):**
```bash
npm run lint
npm test
```

**Pentru modificările exemplelor Python:**
- Testați dacă exemplul rulează cu succes
- Verificați dacă gestionarea erorilor funcționează
- Verificați compatibilitatea cu Foundry Local

### Procesul de revizuire

- Modificările de conținut educațional sunt revizuite pentru acuratețe și claritate
- Exemplele de cod sunt testate pentru funcționalitate
- Actualizările de traducere sunt gestionate automat de GitHub Actions

## Sistem de traducere

**IMPORTANT:** Acest depozit utilizează traducerea automată prin GitHub Actions.

- Traducerile se află în directorul `/translations/` (50+ limbi)
- Automatizate prin fluxul de lucru `co-op-translator.yml`
- **NU editați manual fișierele de traducere** - acestea vor fi suprascrise
- Editați doar fișierele sursă în engleză din directoarele rădăcină și module
- Traducerile sunt generate automat la push către ramura `main`

## Integrarea locală Foundry

Majoritatea exemplelor din Module08 necesită rularea Microsoft Foundry Local.

### Instalare și configurare

**Instalați Foundry Local:**
```bash
# Windows
winget install Microsoft.FoundryLocal

# macOS
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**Instalați SDK-ul Python:**
```bash
pip install foundry-local-sdk openai
```

### Pornirea Foundry Local
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

### Utilizarea SDK-ului (Python)
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

### Verificarea Foundry Local
```bash
# Service status and endpoint
foundry service status

# List loaded models (REST API)
curl http://localhost:<port>/v1/models

# Note: Port is displayed when running 'foundry service status'
```

### Variabile de mediu pentru exemple

Majoritatea exemplelor utilizează aceste variabile de mediu:
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

**Notă**: Când utilizați `FoundryLocalManager`, SDK-ul gestionează automat descoperirea serviciilor și încărcarea modelelor. Aliasurile modelelor (cum ar fi `phi-3.5-mini`) asigură selectarea celei mai bune variante pentru hardware-ul dvs.

## Construire și implementare

### Implementarea conținutului

Acest depozit este în principal documentație - nu este necesar un proces de construire pentru conținut.

### Construirea aplicațiilor de exemplu

**Aplicația Electron (Module08/exemple/08):**
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

**Exemplele Python:**
Nu este necesar un proces de construire - exemplele sunt rulate direct cu interpretul Python.

## Probleme comune și depanare

> **Sfat**: Verificați [GitHub Issues](https://github.com/microsoft/edgeai-for-beginners/issues) pentru probleme cunoscute și soluții.

### Probleme critice (blocante)

#### Foundry Local nu rulează
**Problemă:** Exemplele eșuează cu erori de conexiune

**Soluție:**
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

### Probleme comune (moderate)

#### Probleme cu mediul virtual Python
**Problemă:** Erori la importul modulelor

**Soluție:**
```bash
# Ensure virtual environment is activated
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt
```

#### Probleme la construirea Electron
**Problemă:** npm install sau eșecuri la construire

**Soluție:**
```bash
cd Module08/samples/08
# Clean install
npm run clean
rm -rf node_modules package-lock.json
npm install
```

### Probleme de flux de lucru (minore)

#### Conflicte în fluxul de lucru de traducere
**Problemă:** PR-ul de traducere intră în conflict cu modificările dvs.

**Soluție:**
- Editați doar fișierele sursă în engleză
- Lăsați fluxul de lucru automat de traducere să gestioneze traducerile
- Dacă apar conflicte, îmbinați `main` în ramura dvs. după ce traducerile sunt îmbinate

#### Eșecuri la descărcarea modelelor
**Problemă:** Foundry Local nu reușește să descarce modele

**Soluție:**
```bash
# Check internet connectivity
# Clear model cache and retry
foundry model remove <model-alias>
foundry model run <model-alias>

# Check available disk space (models can be 2-16GB)
# Verify firewall settings allow downloads
```

## Resurse suplimentare

### Parcursuri de învățare
- **Parcurs pentru începători:** Modulele 01-02 (7-9 ore)
- **Parcurs intermediar:** Modulele 03-04 (9-11 ore)
- **Parcurs avansat:** Modulele 05-07 (12-15 ore)
- **Parcurs expert:** Modulul 08 (8-10 ore)
- **Atelier practic:** Materiale de atelier (6-8 ore)

### Conținut cheie al modulelor
- **Modulul01:** Fundamentele EdgeAI și studii de caz reale
- **Modulul02:** Familii și arhitecturi de modele de limbaj mici (SLM)
- **Modulul03:** Strategii de implementare locală și în cloud
- **Modulul04:** Optimizarea modelelor cu mai multe cadre (Llama.cpp, Microsoft Olive, OpenVINO, Qualcomm QNN, Apple MLX)
- **Modulul05:** SLMOps - operațiuni de producție
- **Modulul06:** Agenți AI și apelarea funcțiilor
- **Modulul07:** Implementări specifice platformei
- **Modulul08:** Toolkit Foundry Local cu 10 exemple cuprinzătoare

### Dependențe externe
- [Microsoft Foundry Local](https://github.com/microsoft/Foundry-Local) - Runtime local pentru modele AI cu API compatibil OpenAI
  - [Documentație](https://github.com/microsoft/Foundry-Local/blob/main/docs/README.md)
  - [SDK Python](https://github.com/microsoft/Foundry-Local/tree/main/sdk/python)
  - [SDK JavaScript](https://github.com/microsoft/Foundry-Local/tree/main/sdk/javascript)
- [Llama.cpp](https://github.com/ggml-org/llama.cpp) - Cadru de optimizare
- [Microsoft Olive](https://microsoft.github.io/Olive/) - Toolkit de optimizare a modelelor
- [OpenVINO](https://docs.openvino.ai/) - Toolkit de optimizare Intel

## Note specifice proiectului

### Aplicații de exemplu din Modulul08

Depozitul include 10 aplicații de exemplu cuprinzătoare:

1. **01-REST Chat Quickstart** - Integrare de bază OpenAI SDK
2. **02-OpenAI SDK Integration** - Funcționalități avansate ale SDK-ului
3. **03-Model Discovery & Benchmarking** - Instrumente de comparare a modelelor
4. **04-Chainlit RAG Application** - Generare augmentată prin recuperare
5. **05-Multi-Agent Orchestration** - Coordonarea de bază a agenților
6. **06-Models-as-Tools Router** - Rutare inteligentă a modelelor
7. **07-Direct API Client** - Integrare API la nivel scăzut
8. **08-Windows 11 Chat App** - Aplicație desktop nativă Electron
9. **09-Advanced Multi-Agent System** - Orchestrare complexă a agenților
10. **10-Cadrul de Instrumente Foundry** - Integrarea LangChain/Semantic Kernel

### Aplicații Exemple din Workshop

Workshop-ul include 6 sesiuni progresive cu implementări practice:

1. **Sesiunea 01** - Configurarea inițială a chat-ului cu integrarea Foundry Local
2. **Sesiunea 02** - Pipeline RAG și evaluare cu RAGAS
3. **Sesiunea 03** - Testarea performanței modelelor open-source
4. **Sesiunea 04** - Compararea și selecția modelelor
5. **Sesiunea 05** - Sisteme de orchestrare multi-agent
6. **Sesiunea 06** - Rutarea modelelor și gestionarea pipeline-urilor

Fiecare exemplu demonstrează diferite aspecte ale dezvoltării AI la margine cu Foundry Local.

### Considerații de Performanță

- SLM-urile sunt optimizate pentru implementare la margine (2-16GB RAM)
- Inferența locală oferă timpi de răspuns de 50-500ms
- Tehnicile de cuantizare reduc dimensiunea cu 75% păstrând 85% din performanță
- Capacități de conversație în timp real cu modele locale

### Securitate și Confidențialitate

- Toată procesarea are loc local - niciun fel de date nu sunt trimise în cloud
- Potrivit pentru aplicații sensibile la confidențialitate (sănătate, finanțe)
- Respectă cerințele de suveranitate a datelor
- Foundry Local funcționează complet pe hardware local

## Obținerea Ajutorului

### Documentație

- **README Principal**: [README.md](README.md) - Prezentare generală a depozitului și căi de învățare
- **Ghid de Studiu**: [STUDY_GUIDE.md](STUDY_GUIDE.md) - Resurse de învățare și cronologie
- **Suport**: [SUPPORT.md](SUPPORT.md) - Cum să obțineți ajutor
- **Securitate**: [SECURITY.md](SECURITY.md) - Raportarea problemelor de securitate

### Suport Comunitar

- **Probleme GitHub**: [Raportați erori sau solicitați funcționalități](https://github.com/microsoft/edgeai-for-beginners/issues)
- **Discuții GitHub**: [Puneți întrebări și împărtășiți idei](https://github.com/microsoft/edgeai-for-beginners/discussions)
- **Probleme Foundry Local**: [Probleme tehnice cu Foundry Local](https://github.com/microsoft/Foundry-Local/issues)

### Contact

- **Responsabili**: Consultați [CODEOWNERS](https://github.com/microsoft/edgeai-for-beginners/blob/main/.github/CODEOWNERS)
- **Probleme de Securitate**: Urmați dezvăluirea responsabilă în [SECURITY.md](SECURITY.md)
- **Suport Microsoft**: Pentru suport enterprise, contactați serviciul de relații cu clienții Microsoft

### Resurse Suplimentare

- **Microsoft Learn**: [Căi de învățare AI și Machine Learning](https://learn.microsoft.com/training/browse/?products=ai-services)
- **Documentația Foundry Local**: [Documentație Oficială](https://github.com/microsoft/Foundry-Local/blob/main/docs/README.md)
- **Exemple Comunitare**: Consultați [Discuții GitHub](https://github.com/microsoft/edgeai-for-beginners/discussions) pentru contribuțiile comunității

---

**Acesta este un depozit educațional axat pe predarea dezvoltării AI la margine. Modelul principal de contribuție este îmbunătățirea conținutului educațional și adăugarea/îmbunătățirea aplicațiilor exemplu care demonstrează concepte AI la margine.**

---

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să asigurăm acuratețea, vă rugăm să fiți conștienți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa maternă ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.
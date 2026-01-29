# Ghid de Dezvoltare Windows Edge AI

## Introducere

Bine ai venit la dezvoltarea Windows Edge AI - ghidul tău complet pentru construirea aplicațiilor inteligente care valorifică puterea AI-ului local folosind platforma Windows AI Foundry de la Microsoft. Acest ghid este conceput special pentru dezvoltatorii Windows care doresc să integreze capabilități avansate de Edge AI în aplicațiile lor, utilizând pe deplin accelerarea hardware oferită de Windows.

### Avantajele Windows AI

Windows AI Foundry reprezintă o platformă unificată, fiabilă și sigură care sprijină întregul ciclu de viață al dezvoltării AI - de la selecția și ajustarea modelelor, până la optimizare și implementare pe arhitecturi CPU, GPU, NPU și cloud hibrid. Această platformă democratizează dezvoltarea AI oferind:

- **Abstracție Hardware**: Implementare fără probleme pe siliciu AMD, Intel, NVIDIA și Qualcomm
- **Inteligență Locală**: AI care protejează confidențialitatea și rulează complet pe hardware local
- **Performanță Optimizată**: Modele pre-optimizate pentru configurațiile hardware Windows
- **Pregătit pentru Enterprise**: Funcții de securitate și conformitate de nivel industrial

### Windows ML
Windows Machine Learning (ML) permite dezvoltatorilor C#, C++ și Python să ruleze modele ONNX AI local pe PC-uri Windows prin ONNX Runtime, cu gestionare automată a furnizorilor de execuție pentru diferite hardware-uri (CPU-uri, GPU-uri, NPU-uri). [ONNX Runtime](https://onnxruntime.ai/docs/) poate fi utilizat cu modele din PyTorch, Tensorflow/Keras, TFLite, scikit-learn și alte framework-uri.

![WindowsML O diagramă care ilustrează un model ONNX trecând prin Windows ML pentru a ajunge la NPU-uri, GPU-uri și CPU-uri.](https://learn.microsoft.com/en-us/windows/ai/images/winml-diagram.png)

Windows ML oferă o copie comună a ONNX Runtime pentru întregul Windows, plus capacitatea de a descărca dinamic furnizorii de execuție (EP-uri).

### De ce Windows pentru Edge AI?

**Suport Universal pentru Hardware**
Windows ML oferă optimizare automată a hardware-ului în întregul ecosistem Windows, asigurând performanța optimă a aplicațiilor AI, indiferent de arhitectura siliciului de bază.

**Runtime AI Integrat**
Motorul de inferență Windows ML încorporat elimină cerințele complexe de configurare, permițând dezvoltatorilor să se concentreze pe logica aplicației, nu pe infrastructură.

**Optimizare PC Copilot+**
API-uri special concepute pentru dispozitivele Windows de generație următoare, cu Unități de Procesare Neurală (NPU-uri) dedicate, oferind performanță excepțională per watt.

**Ecosistem pentru Dezvoltatori**
Instrumente bogate, inclusiv integrarea Visual Studio, documentație cuprinzătoare și aplicații exemplu care accelerează ciclurile de dezvoltare.

## Obiective de Învățare

Parcurgând acest ghid de dezvoltare Windows Edge AI, vei stăpâni abilitățile esențiale pentru construirea aplicațiilor AI pregătite pentru producție pe platforma Windows.

### Competențe Tehnice de Bază

**Stăpânirea Windows AI Foundry**
- Înțelegerea arhitecturii și componentelor platformei Windows AI Foundry
- Navigarea întregului ciclu de viață al dezvoltării AI în ecosistemul Windows
- Implementarea celor mai bune practici de securitate pentru aplicațiile AI locale
- Optimizarea aplicațiilor pentru diferite configurații hardware Windows

**Expertiză în Integrarea API-urilor**
- Stăpânirea API-urilor Windows AI pentru aplicații text, vizuale și multimodale
- Implementarea integrării modelului de limbaj Phi Silica pentru generarea și raționamentul textului
- Implementarea capabilităților de viziune computerizată folosind API-uri de procesare a imaginilor încorporate
- Personalizarea modelelor pre-antrenate utilizând tehnici LoRA (Low-Rank Adaptation)

**Implementarea Locală Foundry**
- Navigarea, evaluarea și implementarea modelelor de limbaj open-source folosind Foundry Local CLI
- Înțelegerea optimizării și cuantificării modelelor pentru implementare locală
- Implementarea capabilităților AI offline care funcționează fără conectivitate la internet
- Gestionarea ciclurilor de viață ale modelelor și actualizărilor în medii de producție

**Implementarea Windows ML**
- Adăugarea modelelor ONNX personalizate în aplicațiile Windows folosind Windows ML
- Valorificarea accelerării hardware automate pe arhitecturi CPU, GPU și NPU
- Implementarea inferenței în timp real cu utilizarea optimă a resurselor
- Proiectarea aplicațiilor AI scalabile pentru diverse categorii de dispozitive Windows

### Abilități de Dezvoltare a Aplicațiilor

**Dezvoltare Windows Cross-Platform**
- Construirea aplicațiilor alimentate de AI folosind .NET MAUI pentru implementare universală pe Windows
- Integrarea capabilităților AI în aplicații Win32, UWP și Progressive Web
- Implementarea designurilor UI responsive care se adaptează la stările de procesare AI
- Gestionarea operațiunilor AI asincrone cu modele adecvate de experiență utilizator

**Optimizarea Performanței**
- Profilarea și optimizarea performanței inferenței AI pe diferite configurații hardware
- Implementarea gestionării eficiente a memoriei pentru modelele de limbaj mari
- Proiectarea aplicațiilor care degradează grațios în funcție de capabilitățile hardware disponibile
- Aplicarea strategiilor de caching pentru operațiunile AI utilizate frecvent

**Pregătirea pentru Producție**
- Implementarea gestionării erorilor și mecanismelor de fallback cuprinzătoare
- Proiectarea telemetriei și monitorizării performanței aplicațiilor AI
- Aplicarea celor mai bune practici de securitate pentru stocarea și execuția modelelor AI locale
- Planificarea strategiilor de implementare pentru aplicații enterprise și de consum

### Înțelegerea Strategică și de Business

**Arhitectura Aplicațiilor AI**
- Proiectarea arhitecturilor hibride care optimizează între procesarea AI locală și cloud
- Evaluarea compromisurilor între dimensiunea modelului, acuratețe și viteza inferenței
- Planificarea arhitecturilor de flux de date care mențin confidențialitatea, oferind în același timp inteligență
- Implementarea soluțiilor AI rentabile care se scalează cu cerințele utilizatorilor

**Poziționarea pe Piață**
- Înțelegerea avantajelor competitive ale aplicațiilor AI native Windows
- Identificarea cazurilor de utilizare în care AI-ul local oferă experiențe superioare utilizatorilor
- Dezvoltarea strategiilor de lansare pe piață pentru aplicațiile Windows îmbunătățite cu AI
- Poziționarea aplicațiilor pentru a valorifica beneficiile ecosistemului Windows

## Exemple de Aplicații AI Windows App SDK

Windows App SDK oferă exemple cuprinzătoare care demonstrează integrarea AI în diverse framework-uri și scenarii de implementare. Aceste exemple sunt referințe esențiale pentru înțelegerea modelelor de dezvoltare AI Windows.

### Exemple Windows AI Foundry

| Exemplu | Framework | Domeniu de Focus | Caracteristici Cheie |
|---------|-----------|------------------|-----------------------|
| [cs-winui](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsAIFoundry/cs-winui) | C# WinUI 3 | Integrarea API-urilor Windows AI | Aplicație completă WinUI care demonstrează API-urile Windows AI, optimizarea ARM64, implementarea pachetelor |

**Tehnologii Cheie:**
- API-uri Windows AI
- Framework WinUI 3
- Optimizare platformă ARM64
- Compatibilitate PC Copilot+
- Implementare aplicație pachetată

**Cerințe Prealabile:**
- Windows 11 cu PC Copilot+ recomandat
- Visual Studio 2022
- Configurație build ARM64
- Windows App SDK 1.8.1+

### Exemple Windows ML

#### Exemple C++

| Exemplu | Tip | Domeniu de Focus | Caracteristici Cheie |
|---------|-----|------------------|-----------------------|
| [CppConsoleDesktop](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Aplicație Console | Windows ML de bază | Descoperirea EP, opțiuni linie de comandă, compilarea modelului |
| [CppConsoleDesktop.FrameworkDependent](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Aplicație Console | Implementare Framework | Runtime partajat, amprentă de implementare mai mică |
| [CppConsoleDesktop.SelfContained](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Aplicație Console | Implementare Independentă | Implementare autonomă, fără dependențe de runtime |
| [CppConsoleDll](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | DLL | Utilizare Bibliotecă | WindowsML în bibliotecă partajată, gestionarea memoriei |
| [CppResnetBuildDemo](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Demo | Tutorial ResNet | Conversia modelului, compilarea EP, tutorial Build 2025 |

#### Exemple C#

**Aplicații Console**

| Exemplu | Tip | Domeniu de Focus | Caracteristici Cheie |
|---------|-----|------------------|-----------------------|
| [CSharpConsoleDesktop](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs) | Aplicație Console | Integrare C# de bază | Utilizarea helper-ului partajat, interfață linie de comandă |
| [ResnetBuildDemoCS](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs) | Demo | Tutorial ResNet | Conversia modelului, compilarea EP, tutorial Build 2025 |

**Aplicații GUI**

| Exemplu | Framework | Domeniu de Focus | Caracteristici Cheie |
|---------|-----------|------------------|-----------------------|
| [cs-wpf](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs-wpf) | WPF | GUI Desktop | Clasificare imagini cu interfață WPF |
| [cs-winforms](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs-winforms) | Windows Forms | GUI Tradițional | Clasificare imagini cu Windows Forms |
| [cs-winui](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs-winui) | WinUI 3 | GUI Modern | Clasificare imagini cu interfață WinUI 3 |

#### Exemple Python

| Exemplu | Limbaj | Domeniu de Focus | Caracteristici Cheie |
|---------|--------|------------------|-----------------------|
| [SqueezeNetPython](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/python) | Python | Clasificare Imagini | Binding-uri WinML pentru Python, procesare batch imagini |

### Cerințe Prealabile pentru Exemple

**Cerințe de Sistem:**
- PC Windows 11 care rulează versiunea 24H2 (build 26100) sau mai mare
- Visual Studio 2022 cu workload-uri C++ și .NET
- Windows App SDK 1.8.1 sau mai recent
- Python 3.10-3.13 pentru exemple Python pe dispozitive x64 și ARM64

**Specific Windows AI Foundry:**
- PC Copilot+ recomandat pentru performanță optimă
- Configurație build ARM64 pentru exemple Windows AI
- Identitate pachet necesară (aplicațiile neambalate nu mai sunt suportate)

### Flux Comun pentru Exemple

Majoritatea exemplelor Windows ML urmează acest model standard:

1. **Inițializarea Mediului** - Crearea mediului ONNX Runtime
2. **Înregistrarea Furnizorilor de Execuție** - Descoperirea și înregistrarea acceleratoarelor hardware disponibile (CPU, GPU, NPU)
3. **Încărcarea Modelului** - Încărcarea modelului ONNX, opțional compilarea pentru hardware-ul țintă
4. **Preprocesarea Inputului** - Conversia imaginilor/datelor în formatul de input al modelului
5. **Rularea Inferenței** - Executarea modelului și obținerea predicțiilor
6. **Procesarea Rezultatelor** - Aplicarea softmax și afișarea predicțiilor de top

### Fișierele Modelului Utilizate

| Model | Scop | Inclus | Note |
|-------|------|--------|------|
| SqueezeNet | Clasificare imagini ușoară | ✅ Inclus | Pre-antrenat, gata de utilizare |
| ResNet-50 | Clasificare imagini de înaltă acuratețe | ❌ Necesită conversie | Utilizați [AI Toolkit](https://code.visualstudio.com/docs/intelligentapps/modelconversion) pentru conversie |

### Suport Hardware

Toate exemplele detectează și utilizează automat hardware-ul disponibil:
- **CPU** - Suport universal pe toate dispozitivele Windows
- **GPU** - Detectare automată și optimizare pentru hardware-ul grafic disponibil
- **NPU** - Valorifică Unitățile de Procesare Neurală pe dispozitivele suportate (PC-uri Copilot+)

## Componentele Platformei Windows AI Foundry

### 1. API-uri Windows AI

API-urile Windows AI oferă capabilități AI gata de utilizare, alimentate de modele locale, optimizate pentru eficiență și performanță pe dispozitivele PC Copilot+ cu configurare minimă necesară.

#### Categorii de API-uri de Bază

**Modelul de Limbaj Phi Silica**
- Model de limbaj mic, dar puternic, pentru generarea și raționamentul textului
- Optimizat pentru inferență în timp real cu consum minim de energie
- Suport pentru ajustare personalizată folosind tehnici LoRA
- Integrare cu căutarea semantică Windows și recuperarea cunoștințelor

**API-uri de Viziune Computerizată**
- **Recunoaștere Text (OCR)**: Extrage text din imagini cu acuratețe ridicată
- **Super Rezoluție Imagini**: Mărește rezoluția imaginilor folosind modele AI locale
- **Segmentare Imagini**: Identifică și izolează obiecte specifice în imagini
- **Descriere Imagini**: Generează descrieri text detaliate pentru conținut vizual
- **Ștergere Obiecte**: Elimină obiectele nedorite din imagini cu ajutorul inpainting-ului AI

**Capabilități Multimodale**
- **Integrare Viziune-Limbaj**: Combină înțelegerea textului și imaginilor
- **Căutare Semantică**: Permite interogări în limbaj natural pe conținut multimedia
- **Recuperare Cunoștințe**: Construiește experiențe de căutare inteligente cu date locale

### 2. Foundry Local

Foundry Local oferă dezvoltatorilor acces rapid la modele de limbaj open-source gata de utilizare pe siliciul Windows, oferind posibilitatea de a naviga, testa, interacționa și implementa modele în aplicații locale.

#### Aplicații Exemplu Foundry Local

[Repository-ul Foundry Local](https://github.com/microsoft/Foundry-Local/tree/main/samples) oferă exemple cuprinzătoare în diverse limbaje de programare și framework-uri, demonstrând diferite modele de integrare și cazuri de utilizare.

| Exemplu | Limbaj/Framework | Domeniu de Focus | Caracteristici Cheie |
|---------|------------------|------------------|-----------------------|
| [dotNET/rag](https://github.com/microsoft/Foundry-Local/tree/main/samples/dotNET/rag) | C# / .NET | Implementare RAG | Integrare Semantic Kernel, stoc vectorial Qdrant, embeddings JINA, ingestie documente, chat streaming |
| [electron/foundry-chat](https://github.com/microsoft/Foundry-Local/tree/main/samples/electron/foundry-chat) | JavaScript / Electron | Aplicație Chat Desktop | Chat cross-platform, comutare model local/cloud, integrare SDK OpenAI, streaming în timp real |
| [js/hello-foundry-local](https://github.com/microsoft/Foundry-Local/tree/main/samples/js/hello-foundry-local) | JavaScript / Node.js | Integrare de Bază | Utilizare simplă SDK, inițializare model, funcționalitate chat de bază |
| [python/hello-foundry-local](https://github.com/microsoft/Foundry-Local/tree/main/samples/python/hello-foundry-local) | Python | Integrare de Bază | Utilizare SDK Python, răspunsuri streaming, API compatibil OpenAI |
| [rust/hello-foundry-local](https://github.com/microsoft/Foundry-Local/tree/main/samples/rust/hello-foundry-local) | Rust | Integrare de sisteme | Utilizare SDK la nivel scăzut, operațiuni asincrone, client HTTP reqwest |

#### Categorii de exemple în funcție de caz de utilizare

**RAG (Generare augmentată prin recuperare)**
- **dotNET/rag**: Implementare completă RAG folosind Semantic Kernel, baza de date vectorială Qdrant și JINA embeddings
- **Arhitectură**: Ingestia documentelor → Fragmentarea textului → Embeddings vectoriale → Căutare de similaritate → Răspunsuri conștiente de context
- **Tehnologii**: Microsoft.SemanticKernel, Qdrant.Client, embeddings BERT ONNX, completare de chat în flux

**Aplicații desktop**
- **electron/foundry-chat**: Aplicație de chat gata de producție cu comutare între modele locale/cloud
- **Funcționalități**: Selector de modele, răspunsuri în flux, gestionarea erorilor, implementare multiplatformă
- **Arhitectură**: Proces principal Electron, comunicare IPC, scripturi de preload securizate

**Exemple de integrare SDK**
- **JavaScript (Node.js)**: Interacțiune de bază cu modelul și răspunsuri în flux
- **Python**: Utilizare API compatibil OpenAI cu streaming asincron
- **Rust**: Integrare la nivel scăzut cu reqwest și tokio pentru operațiuni asincrone

#### Cerințe preliminare pentru exemplele Foundry Local

**Cerințe de sistem:**
- Windows 11 cu Foundry Local instalat
- Node.js v16+ pentru exemplele JavaScript/Electron
- .NET 8.0+ pentru exemplele C#
- Python 3.10+ pentru exemplele Python
- Rust 1.70+ pentru exemplele Rust

**Instalare:**
```powershell
# Install Foundry Local
winget install Microsoft.FoundryLocal

# Verify installation
foundry --version
foundry model list
```

#### Configurare specifică pentru exemple

**Exemplu dotNET RAG:**
```powershell
# Install required packages via NuGet
# Microsoft.SemanticKernel.Connectors.Onnx
# Microsoft.SemanticKernel.Connectors.Qdrant
# Qdrant.Client

# Start Qdrant vector database
docker run -p 6333:6333 qdrant/qdrant

# Run Jupyter notebook
jupyter notebook rag_foundrylocal_demo.ipynb
```

**Exemplu Electron Chat:**
```powershell
# Set environment variables for cloud fallback
$env:YOUR_API_KEY="your-cloud-api-key"
$env:YOUR_ENDPOINT="your-cloud-endpoint"
$env:YOUR_MODEL_NAME="your-cloud-model"

# Install dependencies and run
npm install
npm start
```

**Exemple JavaScript/Python/Rust:**
```powershell
# Download model (example with phi-3.5-mini)
foundry model run phi-3.5-mini

# Run respective sample
node src/app.js          # JavaScript
python src/app.py        # Python
cargo run               # Rust
```

#### Funcționalități cheie

**Catalog de modele**
- Colecție cuprinzătoare de modele open-source pre-optimizate
- Modele optimizate pentru CPU-uri, GPU-uri și NPU-uri pentru implementare imediată
- Suport pentru familii populare de modele, inclusiv Llama, Mistral, Phi și modele specializate pe domenii

**Integrare CLI**
- Interfață de linie de comandă pentru gestionarea și implementarea modelelor
- Fluxuri de lucru automate pentru optimizare și cuantizare
- Integrare cu medii de dezvoltare populare și pipeline-uri CI/CD

**Implementare locală**
- Operare complet offline fără dependențe de cloud
- Suport pentru formate și configurații personalizate de modele
- Servire eficientă a modelelor cu optimizare automată a hardware-ului

### 3. Windows ML

Windows ML servește ca platforma principală de AI și runtime integrat de inferență pe Windows, permițând dezvoltatorilor să implementeze modele personalizate eficient pe ecosistemul hardware Windows.

#### Beneficii arhitecturale

**Suport universal pentru hardware**
- Optimizare automată pentru siliciu AMD, Intel, NVIDIA și Qualcomm
- Suport pentru execuție pe CPU, GPU și NPU cu comutare transparentă
- Abstracție hardware care elimină necesitatea optimizării specifice platformei

**Flexibilitate a modelelor**
- Suport pentru formatul de model ONNX cu conversie automată din framework-uri populare
- Implementare de modele personalizate cu performanță de nivel producție
- Integrare cu arhitecturi existente de aplicații Windows

**Integrare în mediul enterprise**
- Compatibilitate cu cadrele de securitate și conformitate Windows
- Suport pentru instrumente de implementare și gestionare enterprise
- Integrare cu sistemele de gestionare și monitorizare a dispozitivelor Windows

## Flux de lucru pentru dezvoltare

### Faza 1: Configurarea mediului și a instrumentelor

**Pregătirea mediului de dezvoltare**
1. Instalați Visual Studio 2022 cu workload-uri C++ și .NET
2. Instalați Windows App SDK 1.8.1 sau o versiune ulterioară
3. Configurați instrumentele CLI Windows AI Foundry
4. Configurați extensia AI Toolkit pentru Visual Studio Code
5. Stabiliți instrumente de profilare și monitorizare a performanței
6. Asigurați configurarea build-ului ARM64 pentru optimizarea PC-urilor Copilot+

**Configurarea depozitului de exemple**
1. Clonați [depozitul de exemple Windows App SDK](https://github.com/microsoft/WindowsAppSDK-Samples)
2. Navigați la `Samples/WindowsAIFoundry/cs-winui` pentru exemple de API Windows AI
3. Navigați la `Samples/WindowsML` pentru exemple complete Windows ML
4. Revizuiți [cerințele de build](https://learn.microsoft.com/windows/apps/windows-app-sdk/system-requirements) pentru platformele țintă

**Explorarea galeriei AI Dev**
- Explorați aplicații de exemplu și implementări de referință
- Testați API-urile Windows AI cu demonstrații interactive
- Revizuiți codul sursă pentru cele mai bune practici și modele
- Identificați exemple relevante pentru cazul dvs. specific de utilizare

### Faza 2: Selectarea și integrarea modelului

**Analiza cerințelor**
- Definiți cerințele funcționale pentru capabilitățile AI
- Stabiliți constrângerile de performanță și țintele de optimizare
- Evaluați cerințele de confidențialitate și securitate
- Planificați arhitectura de implementare și strategiile de scalare

**Evaluarea modelului**
- Utilizați Foundry Local pentru a testa modele open-source pentru cazul dvs. de utilizare
- Benchmark API-urile Windows AI în raport cu cerințele modelelor personalizate
- Evaluați compromisurile între dimensiunea modelului, acuratețe și viteza de inferență
- Prototipați abordări de integrare cu modelele selectate

### Faza 3: Dezvoltarea aplicației

**Integrarea de bază**
- Implementați integrarea API-urilor Windows AI cu gestionarea corespunzătoare a erorilor
- Proiectați interfețe de utilizator care să acomodeze fluxurile de procesare AI
- Implementați strategii de caching și optimizare pentru inferența modelelor
- Adăugați telemetrie și monitorizare pentru performanța operațiunilor AI

**Testare și validare**
- Testați aplicațiile pe diferite configurații hardware Windows
- Validați metricile de performanță în condiții de încărcare variate
- Implementați testare automată pentru fiabilitatea funcționalității AI
- Realizați testarea experienței utilizatorului cu funcționalități AI îmbunătățite

### Faza 4: Optimizare și implementare

**Optimizarea performanței**
- Profilați performanța aplicației pe configurațiile hardware țintă
- Optimizați utilizarea memoriei și strategiile de încărcare a modelelor
- Implementați comportament adaptiv bazat pe capabilitățile hardware disponibile
- Ajustați experiența utilizatorului pentru diferite scenarii de performanță

**Implementare în producție**
- Pachetați aplicațiile cu dependențele corespunzătoare ale modelelor AI
- Implementați mecanisme de actualizare pentru modele și logica aplicației
- Configurați monitorizarea și analiza pentru mediile de producție
- Planificați strategii de lansare pentru implementări enterprise și de consum

## Exemple practice de implementare

### Exemplu 1: Aplicație inteligentă de procesare a documentelor

Construiți o aplicație Windows care procesează documente folosind multiple capabilități AI:

**Tehnologii utilizate:**
- Phi Silica pentru sumarizarea documentelor și răspunsuri la întrebări
- API-uri OCR pentru extragerea textului din documente scanate
- API-uri de descriere a imaginilor pentru analiza graficelor și diagramelor
- Modele ONNX personalizate pentru clasificarea documentelor

**Abordare de implementare:**
- Proiectați o arhitectură modulară cu componente AI pluggable
- Implementați procesare asincronă pentru loturi mari de documente
- Adăugați indicatori de progres și suport pentru anularea operațiunilor de lungă durată
- Includeți capabilități offline pentru procesarea documentelor sensibile

### Exemplu 2: Sistem de gestionare a inventarului pentru retail

Creați un sistem de inventar alimentat de AI pentru aplicații de retail:

**Tehnologii utilizate:**
- Segmentare de imagini pentru identificarea produselor
- Modele de viziune personalizate pentru clasificarea brandurilor și categoriilor
- Implementare Foundry Local a modelelor lingvistice specializate pentru retail
- Integrare cu sistemele POS și de inventar existente

**Abordare de implementare:**
- Construiți integrarea camerelor pentru scanarea produselor în timp real
- Implementați recunoașterea codurilor de bare și a produselor vizuale
- Adăugați interogări de inventar în limbaj natural folosind modele lingvistice locale
- Proiectați o arhitectură scalabilă pentru implementare multi-magazin

### Exemplu 3: Asistent de documentare pentru sănătate

Dezvoltați un instrument de documentare medicală care protejează confidențialitatea:

**Tehnologii utilizate:**
- Phi Silica pentru generarea notelor medicale și suport decizional clinic
- OCR pentru digitalizarea înregistrărilor medicale scrise de mână
- Modele lingvistice medicale personalizate implementate prin Windows ML
- Stocare vectorială locală pentru recuperarea cunoștințelor medicale

**Abordare de implementare:**
- Asigurați operarea complet offline pentru protejarea confidențialității pacienților
- Implementați validarea și sugestia terminologiei medicale
- Adăugați jurnalizare pentru conformitate cu reglementările
- Proiectați integrarea cu sistemele existente de înregistrări medicale electronice

## Strategii de optimizare a performanței

### Dezvoltare conștientă de hardware

**Optimizare NPU**
- Proiectați aplicații care să valorifice capabilitățile NPU pe PC-urile Copilot+
- Implementați fallback grațios la GPU/CPU pe dispozitive fără NPU
- Optimizați formatele modelelor pentru accelerarea specifică NPU
- Monitorizați utilizarea NPU și caracteristicile termice

**Gestionarea memoriei**
- Implementați strategii eficiente de încărcare și caching a modelelor
- Utilizați maparea memoriei pentru modele mari pentru a reduce timpul de pornire
- Proiectați aplicații conștiente de memorie pentru dispozitive cu resurse limitate
- Implementați cuantizarea modelelor pentru optimizarea memoriei

**Eficiența bateriei**
- Optimizați operațiunile AI pentru consum minim de energie
- Implementați procesare adaptivă bazată pe starea bateriei
- Proiectați procesare eficientă în fundal pentru operațiuni AI continue
- Utilizați instrumente de profilare a energiei pentru optimizarea consumului

### Considerații de scalabilitate

**Multi-threading**
- Proiectați operațiuni AI sigure pentru procesare concurentă
- Implementați distribuirea eficientă a muncii pe nucleele disponibile
- Utilizați modele async/await pentru operațiuni AI non-blocante
- Planificați optimizarea pool-ului de fire pentru diferite configurații hardware

**Strategii de caching**
- Implementați caching inteligent pentru operațiuni AI utilizate frecvent
- Proiectați strategii de invalidare a cache-ului pentru actualizările modelelor
- Utilizați caching persistent pentru operațiuni costisitoare de preprocesare
- Implementați caching distribuit pentru scenarii multi-utilizator

## Cele mai bune practici de securitate și confidențialitate

### Protecția datelor

**Procesare locală**
- Asigurați-vă că datele sensibile nu părăsesc niciodată dispozitivul local
- Implementați stocare securizată pentru modele AI și date temporare
- Utilizați funcțiile de securitate Windows pentru sandboxing-ul aplicațiilor
- Aplicați criptare pentru modelele stocate și rezultatele intermediare ale procesării

**Securitatea modelelor**
- Validați integritatea modelelor înainte de încărcare și execuție
- Implementați mecanisme securizate de actualizare a modelelor
- Utilizați modele semnate pentru a preveni manipularea
- Aplicați controale de acces pentru fișierele modelelor și configurații

### Considerații de conformitate

**Aliniere la reglementări**
- Proiectați aplicații care să respecte GDPR, HIPAA și alte cerințe de reglementare
- Implementați jurnalizare pentru procesele de luare a deciziilor AI
- Oferiți funcții de transparență pentru rezultatele generate de AI
- Permiteți utilizatorilor controlul asupra procesării datelor AI

**Securitate enterprise**
- Integrați cu politicile de securitate enterprise Windows
- Suportați implementarea gestionată prin instrumente de management enterprise
- Implementați controale de acces bazate pe roluri pentru funcționalitățile AI
- Oferiți controale administrative pentru funcționalitățile AI

## Depanare și debugging

### Provocări comune în dezvoltare

**Probleme de configurare a build-ului**
- Asigurați configurarea platformei ARM64 pentru exemplele API Windows AI
- Verificați compatibilitatea versiunii Windows App SDK (1.8.1+ necesar)
- Verificați că identitatea pachetului este configurată corect (necesară pentru API-urile Windows AI)
- Validați că instrumentele de build suportă versiunea framework-ului țintă

**Probleme de încărcare a modelelor**
- Validați compatibilitatea modelelor ONNX cu Windows ML
- Verificați integritatea fișierelor modelelor și cerințele de format
- Verificați cerințele de capabilitate hardware pentru modele specifice
- Depanați problemele de alocare a memoriei în timpul încărcării modelelor
- Asigurați înregistrarea providerului de execuție pentru accelerarea hardware

**Considerații privind modul de implementare**
- **Mod auto-conținut**: Complet suportat cu dimensiune mai mare de implementare
- **Mod dependent de framework**: Amprentă mai mică, dar necesită runtime partajat
- **Aplicații neambalate**: Nu mai sunt suportate pentru API-urile Windows AI
- Utilizați `dotnet run -p:Platform=ARM64 -p:SelfContained=true` pentru implementare auto-conținut ARM64

**Probleme de performanță**
- Profilați performanța aplicației pe diferite configurații hardware
- Identificați blocajele în pipeline-urile de procesare AI
- Optimizați operațiunile de preprocesare și postprocesare a datelor
- Implementați monitorizare și alertare pentru performanță

**Dificultăți de integrare**
- Depanați problemele de integrare API cu gestionarea corespunzătoare a erorilor
- Validați formatele datelor de intrare și cerințele de preprocesare
- Testați cazurile limită și condițiile de eroare în detaliu
- Implementați jurnalizare cuprinzătoare pentru depanarea problemelor de producție

### Instrumente și tehnici de debugging

**Integrare Visual Studio**
- Utilizați debugger-ul AI Toolkit pentru analiza execuției modelelor
- Implementați profilarea performanței pentru operațiunile AI
- Depanați operațiunile AI asincrone cu gestionarea corespunzătoare a excepțiilor
- Utilizați instrumente de profilare a memoriei pentru optimizare

**Instrumente Windows AI Foundry**
- Valorificați CLI-ul Foundry Local pentru testarea și validarea modelelor
- Utilizați instrumentele de testare API Windows AI pentru verificarea integrării
- Implementați jurnalizare personalizată pentru monitorizarea operațiunilor AI
- Creați testare automată pentru fiabilitatea funcționalității AI

## Pregătirea aplicațiilor pentru viitor

### Tehnologii emergente

**Hardware de generație următoare**
- Proiectați aplicații care să valorifice capabilitățile NPU viitoare
- Planificați pentru dimensiuni și complexitate crescute ale modelelor
- Implementați arhitecturi adaptive pentru hardware în evoluție
- Luați în considerare algoritmi pregătiți pentru quantum pentru compatibilitate viitoare

**Capabilități AI avansate**
- Pregătiți-vă pentru integrarea AI multimodală pe mai multe tipuri de date
- Planificați pentru colaborare AI în timp real între mai multe dispozitive
- Proiectați pentru capabilități de învățare federată
- Luați în considerare arhitecturi hibride edge-cloud pentru inteligență

### Învățare continuă și adaptare

**Actualizări
- [Prezentare generală Windows ML](https://learn.microsoft.com/windows/ai/new-windows-ml/overview/)
- [Cerințe de sistem pentru Windows App SDK](https://docs.microsoft.com/windows/apps/windows-app-sdk/system-requirements)
- [Configurarea mediului de dezvoltare pentru Windows App SDK](https://docs.microsoft.com/windows/apps/windows-app-sdk/set-up-your-development-environment)
- 

### Repozitoare de exemple și cod
- [Exemple Windows App SDK - Windows AI Foundry](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsAIFoundry)
- [Exemple Windows App SDK - Windows ML](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML)
- [Exemple de inferență ONNX Runtime](https://github.com/microsoft/onnxruntime-inference-examples)
- [Repozitoriu de exemple Windows App SDK](https://github.com/microsoft/WindowsAppSDK-Samples)

### Instrumente de dezvoltare
- [Toolkit AI pentru Visual Studio Code](https://learn.microsoft.com/windows/ai/toolkit/)
- [Galeria de dezvoltare AI](https://learn.microsoft.com/windows/ai/ai-dev-gallery/)
- [Exemple Windows AI](https://learn.microsoft.com/windows/ai/samples/)
- [Instrumente de conversie a modelelor](https://code.visualstudio.com/docs/intelligentapps/modelconversion)

### Suport tehnic
- [Documentație Windows ML](https://learn.microsoft.com/windows/ai/new-windows-ml/overview)
- [Documentație ONNX Runtime](https://onnxruntime.ai/docs/)
- [Documentație Windows App SDK](https://docs.microsoft.com/windows/apps/windows-app-sdk/)
- [Raportați probleme - Exemple Windows App SDK](https://github.com/microsoft/WindowsAppSDK-Samples/issues)

### Comunitate și suport
- [Comunitatea dezvoltatorilor Windows](https://developer.microsoft.com/en-us/windows/)
- [Blogul Windows AI Foundry](https://blogs.windows.com/windowsdeveloper/)
- [Microsoft Learn - Training AI](https://learn.microsoft.com/training/browse/?products=windows&subjects=artificial-intelligence)

---

*Acest ghid este conceput să evolueze odată cu ecosistemul Windows AI, care avansează rapid. Actualizările regulate asigură alinierea cu cele mai recente capacități ale platformei și cele mai bune practici de dezvoltare.*

[08. Practică cu Microsoft Foundry Local - Toolkit complet pentru dezvoltatori](../Module08/README.md)

---

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să asigurăm acuratețea, vă rugăm să fiți conștienți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa natală ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.
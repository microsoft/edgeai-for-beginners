# Windows Edge AI Vývojová Príručka

## Úvod

Vitajte vo svete vývoja Windows Edge AI – komplexnej príručke na tvorbu inteligentných aplikácií, ktoré využívajú silu AI priamo na zariadení pomocou platformy Windows AI Foundry od Microsoftu. Táto príručka je určená pre vývojárov Windows, ktorí chcú integrovať najmodernejšie schopnosti Edge AI do svojich aplikácií a zároveň využiť plný potenciál hardvérovej akcelerácie Windows.

### Výhody Windows AI

Windows AI Foundry predstavuje jednotnú, spoľahlivú a bezpečnú platformu, ktorá podporuje celý životný cyklus vývoja AI – od výberu a doladenia modelu až po optimalizáciu a nasadenie na CPU, GPU, NPU a hybridné cloudové architektúry. Táto platforma demokratizuje vývoj AI poskytovaním:

- **Hardvérovej abstrakcie**: Bezproblémové nasadenie na AMD, Intel, NVIDIA a Qualcomm čipy
- **Inteligencie na zariadení**: AI, ktorá zachováva súkromie a funguje výhradne na lokálnom hardvéri
- **Optimalizovaného výkonu**: Modely predoptimalizované pre konfigurácie hardvéru Windows
- **Pripravenosti pre podniky**: Funkcie bezpečnosti a súladu na úrovni produkcie

### Windows ML 
Windows Machine Learning (ML) umožňuje vývojárom v C#, C++ a Python spúšťať ONNX AI modely lokálne na Windows PC prostredníctvom ONNX Runtime, s automatickým manažmentom poskytovateľov vykonávania pre rôzne hardvéry (CPU, GPU, NPU). [ONNX Runtime](https://onnxruntime.ai/docs/) je možné použiť s modelmi z PyTorch, Tensorflow/Keras, TFLite, scikit-learn a ďalších frameworkov.

![WindowsML Diagram znázorňujúci ONNX model prechádzajúci cez Windows ML a následne dosahujúci NPUs, GPUs a CPUs.l](https://learn.microsoft.com/en-us/windows/ai/images/winml-diagram.png)

Windows ML poskytuje zdieľanú Windows-wide kópiu ONNX Runtime, plus možnosť dynamického sťahovania poskytovateľov vykonávania (EPs).

### Prečo Windows pre Edge AI?

**Univerzálna podpora hardvéru**
Windows ML automaticky optimalizuje hardvér naprieč celým ekosystémom Windows, čím zabezpečuje, že vaše AI aplikácie fungujú optimálne bez ohľadu na architektúru čipu.

**Integrovaný AI Runtime**
Vstavaný Windows ML inference engine eliminuje zložité požiadavky na nastavenie, čo umožňuje vývojárom sústrediť sa na logiku aplikácie namiesto infraštruktúry.

**Optimalizácia pre Copilot+ PC**
API navrhnuté špeciálne pre zariadenia novej generácie Windows s dedikovanými Neural Processing Units (NPUs), ktoré poskytujú výnimočný výkon na watt.

**Ekosystém pre vývojárov**
Bohaté nástroje vrátane integrácie Visual Studio, komplexnej dokumentácie a ukážkových aplikácií, ktoré urýchľujú vývojové cykly.

## Ciele učenia

Po dokončení tejto príručky pre vývoj Windows Edge AI získate základné zručnosti na tvorbu produkčne pripravených AI aplikácií na platforme Windows.

### Kľúčové technické kompetencie

**Ovládanie Windows AI Foundry**
- Porozumenie architektúre a komponentom platformy Windows AI Foundry
- Navigácia celým životným cyklom vývoja AI v ekosystéme Windows
- Implementácia bezpečnostných najlepších praktík pre AI aplikácie na zariadení
- Optimalizácia aplikácií pre rôzne konfigurácie hardvéru Windows

**Expertíza v integrácii API**
- Ovládanie Windows AI API pre textové, vizuálne a multimodálne aplikácie
- Implementácia integrácie jazykového modelu Phi Silica pre generovanie textu a uvažovanie
- Nasadenie schopností počítačového videnia pomocou vstavaných API na spracovanie obrazu
- Prispôsobenie predtrénovaných modelov pomocou techník LoRA (Low-Rank Adaptation)

**Lokálna implementácia Foundry**
- Prehliadanie, hodnotenie a nasadenie open-source jazykových modelov pomocou Foundry Local CLI
- Porozumenie optimalizácii modelov a kvantizácii pre lokálne nasadenie
- Implementácia offline AI schopností, ktoré fungujú bez internetového pripojenia
- Správa životného cyklu modelov a aktualizácií v produkčnom prostredí

**Nasadenie Windows ML**
- Integrácia vlastných ONNX modelov do Windows aplikácií pomocou Windows ML
- Využitie automatickej hardvérovej akcelerácie naprieč CPU, GPU a NPU architektúrami
- Implementácia inferencie v reálnom čase s optimálnym využitím zdrojov
- Návrh škálovateľných AI aplikácií pre rôzne kategórie zariadení Windows

### Zručnosti vývoja aplikácií

**Vývoj naprieč platformami Windows**
- Tvorba AI aplikácií pomocou .NET MAUI pre univerzálne nasadenie na Windows
- Integrácia AI schopností do Win32, UWP a progresívnych webových aplikácií
- Implementácia responzívnych UI dizajnov, ktoré sa prispôsobujú stavom AI spracovania
- Správa asynchrónnych AI operácií s vhodnými vzormi používateľskej skúsenosti

**Optimalizácia výkonu**
- Profilovanie a optimalizácia výkonu AI inferencie naprieč rôznymi konfiguráciami hardvéru
- Implementácia efektívneho manažmentu pamäte pre veľké jazykové modely
- Návrh aplikácií, ktoré sa elegantne degradujú na základe dostupných hardvérových schopností
- Aplikácia stratégií cacheovania pre často používané AI operácie

**Pripravenosť na produkciu**
- Implementácia komplexného spracovania chýb a záložných mechanizmov
- Návrh telemetrie a monitorovania výkonu AI aplikácií
- Aplikácia bezpečnostných najlepších praktík pre lokálne ukladanie a vykonávanie AI modelov
- Plánovanie stratégií nasadenia pre podnikové a spotrebiteľské aplikácie

### Obchodné a strategické porozumenie

**Architektúra AI aplikácií**
- Návrh hybridných architektúr, ktoré optimalizujú medzi lokálnym a cloudovým AI spracovaním
- Hodnotenie kompromisov medzi veľkosťou modelu, presnosťou a rýchlosťou inferencie
- Plánovanie architektúr toku dát, ktoré zachovávajú súkromie a zároveň umožňujú inteligenciu
- Implementácia nákladovo efektívnych AI riešení, ktoré sa škálujú podľa požiadaviek používateľov

**Pozicionovanie na trhu**
- Porozumenie konkurenčným výhodám Windows-native AI aplikácií
- Identifikácia prípadov použitia, kde AI na zariadení poskytuje lepšie používateľské skúsenosti
- Vývoj stratégií uvedenia na trh pre AI aplikácie na Windows
- Pozicionovanie aplikácií na využitie výhod ekosystému Windows

## Ukážky AI vo Windows App SDK

Windows App SDK poskytuje komplexné ukážky demonštrujúce integráciu AI naprieč rôznymi frameworkmi a scenármi nasadenia. Tieto ukážky sú nevyhnutné referencie na pochopenie vzorov vývoja AI vo Windows.

### Ukážky Windows AI Foundry

| Ukážka | Framework | Oblasť zamerania | Kľúčové funkcie |
|--------|-----------|------------------|-----------------|
| [cs-winui](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsAIFoundry/cs-winui) | C# WinUI 3 | Integrácia Windows AI API | Kompletná WinUI aplikácia demonštrujúca Windows AI API, optimalizáciu pre ARM64, balíčkové nasadenie |

**Kľúčové technológie:**
- Windows AI API
- Framework WinUI 3
- Optimalizácia pre platformu ARM64
- Kompatibilita s Copilot+ PC
- Balíčkové nasadenie aplikácie

**Predpoklady:**
- Windows 11 s odporúčaným Copilot+ PC
- Visual Studio 2022
- Konfigurácia buildu ARM64
- Windows App SDK 1.8.1+

### Ukážky Windows ML

#### Ukážky v C++

| Ukážka | Typ | Oblasť zamerania | Kľúčové funkcie |
|--------|------|------------------|-----------------|
| [CppConsoleDesktop](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Konzolová aplikácia | Základy Windows ML | Objavovanie EP, možnosti príkazového riadku, kompilácia modelu |
| [CppConsoleDesktop.FrameworkDependent](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Konzolová aplikácia | Nasadenie frameworku | Zdieľaný runtime, menšia stopa nasadenia |
| [CppConsoleDesktop.SelfContained](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Konzolová aplikácia | Samostatné nasadenie | Samostatné nasadenie, bez runtime závislostí |
| [CppConsoleDll](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | DLL | Použitie knižnice | WindowsML v zdieľanej knižnici, manažment pamäte |
| [CppResnetBuildDemo](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Demo | ResNet tutoriál | Konverzia modelu, kompilácia EP, Build 2025 tutoriál |

#### Ukážky v C#

**Konzolové aplikácie**

| Ukážka | Typ | Oblasť zamerania | Kľúčové funkcie |
|--------|------|------------------|-----------------|
| [CSharpConsoleDesktop](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs) | Konzolová aplikácia | Základy integrácie C# | Použitie zdieľaných helperov, rozhranie príkazového riadku |
| [ResnetBuildDemoCS](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs) | Demo | ResNet tutoriál | Konverzia modelu, kompilácia EP, Build 2025 tutoriál |

**GUI aplikácie**

| Ukážka | Framework | Oblasť zamerania | Kľúčové funkcie |
|--------|-----------|------------------|-----------------|
| [cs-wpf](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs-wpf) | WPF | Desktop GUI | Klasifikácia obrazu s WPF rozhraním |
| [cs-winforms](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs-winforms) | Windows Forms | Tradičné GUI | Klasifikácia obrazu s Windows Forms |
| [cs-winui](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs-winui) | WinUI 3 | Moderné GUI | Klasifikácia obrazu s WinUI 3 rozhraním |

#### Ukážky v Pythone

| Ukážka | Jazyk | Oblasť zamerania | Kľúčové funkcie |
|--------|-------|------------------|-----------------|
| [SqueezeNetPython](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/python) | Python | Klasifikácia obrazu | WinML Python bindingy, dávkové spracovanie obrazu |

### Predpoklady pre ukážky

**Systémové požiadavky:**
- Windows 11 PC s verziou 24H2 (build 26100) alebo vyššou
- Visual Studio 2022 s C++ a .NET pracovnými záťažami
- Windows App SDK 1.8.1 alebo novší
- Python 3.10-3.13 pre Python ukážky na x64 a ARM64 zariadeniach

**Špecifické pre Windows AI Foundry:**
- Odporúčaný Copilot+ PC pre optimálny výkon
- Konfigurácia buildu ARM64 pre ukážky Windows AI
- Vyžaduje sa identita balíčka (nepodporované aplikácie bez balíčka)

### Bežný pracovný postup ukážok

Väčšina ukážok Windows ML nasleduje tento štandardný vzor:

1. **Inicializácia prostredia** - Vytvorenie ONNX Runtime prostredia
2. **Registrácia poskytovateľov vykonávania** - Objavenie a registrácia dostupných hardvérových akcelerátorov (CPU, GPU, NPU)
3. **Načítanie modelu** - Načítanie ONNX modelu, voliteľne kompilácia pre cieľový hardvér
4. **Predspracovanie vstupu** - Konverzia obrazov/dát do formátu vstupu modelu
5. **Spustenie inferencie** - Vykonanie modelu a získanie predpovedí
6. **Spracovanie výsledkov** - Aplikácia softmaxu a zobrazenie najlepších predpovedí

### Použité súbory modelov

| Model | Účel | Zahrnutý | Poznámky |
|-------|------|----------|----------|
| SqueezeNet | Ľahká klasifikácia obrazu | ✅ Zahrnutý | Predtrénovaný, pripravený na použitie |
| ResNet-50 | Klasifikácia obrazu s vysokou presnosťou | ❌ Vyžaduje konverziu | Použite [AI Toolkit](https://code.visualstudio.com/docs/intelligentapps/modelconversion) na konverziu |

### Podpora hardvéru

Všetky ukážky automaticky detegujú a využívajú dostupný hardvér:
- **CPU** - Univerzálna podpora naprieč všetkými zariadeniami Windows
- **GPU** - Automatická detekcia a optimalizácia pre dostupný grafický hardvér
- **NPU** - Využíva Neural Processing Units na podporovaných zariadeniach (Copilot+ PC)

## Komponenty platformy Windows AI Foundry

### 1. Windows AI API

Windows AI API poskytujú pripravené AI schopnosti poháňané modelmi na zariadení, optimalizované pre efektivitu a výkon na zariadeniach Copilot+ PC s minimálnymi požiadavkami na nastavenie.

#### Hlavné kategórie API

**Jazykový model Phi Silica**
- Malý, ale výkonný jazykový model pre generovanie textu a uvažovanie
- Optimalizovaný pre inferenciu v reálnom čase s minimálnou spotrebou energie
- Podpora vlastného doladenia pomocou techník LoRA
- Integrácia s Windows semantickým vyhľadávaním a získavaním znalostí

**API pre počítačové videnie**
- **Rozpoznávanie textu (OCR)**: Extrakcia textu z obrazov s vysokou presnosťou
- **Super rozlíšenie obrazu**: Zvýšenie rozlíšenia obrazov pomocou lokálnych AI modelov
- **Segmentácia obrazu**: Identifikácia a izolácia konkrétnych objektov na obrazoch
- **Popis obrazu**: Generovanie podrobných textových popisov vizuálneho obsahu
- **Odstránenie objektov**: Odstránenie nežiaducich objektov z obrazov pomocou AI-powered inpaintingu

**Multimodálne schopnosti**
- **Integrácia videnia a jazyka**: Kombinácia porozumenia textu a obrazu
- **Semantické vyhľadávanie**: Umožnenie prirodzených jazykových dotazov naprieč multimediálnym obsahom
- **Získavanie znalostí**: Budovanie inteligentných vyhľadávacích skúseností s lokálnymi dátami

### 2. Foundry Local

Foundry Local poskytuje vývojárom rýchly prístup k pripraveným open-source jazykovým modelom na Windows Silicon, ponúkajúc možnosť prehliadať, testovať, interagovať a nasadzovať modely v lokálnych aplikáciách.

#### Ukážkové aplikácie Foundry Local

[Foundry Local repository](https://github.com/microsoft/Foundry-Local/tree/main/samples) poskytuje komplexné ukážky naprieč rôznymi programovacími jazykmi a frameworkmi, demonštrujúce rôzne vzory integrácie a prípady použitia.

| Ukážka | Jazyk/Framework | Oblasť zamerania | Kľúčové funkcie |
|--------|-----------------|------------------|-----------------|
| [dotNET/rag](https://github.com/microsoft/Foundry-Local/tree/main/samples/dotNET/rag) | C# / .NET | Implementácia RAG | Integrácia Semantic Kernel, Qdrant vektorový úložisko, JINA embeddings, ingestia dokumentov, streaming chat |
| [electron/foundry-chat
| [rust/hello-foundry-local](https://github.com/microsoft/Foundry-Local/tree/main/samples/rust/hello-foundry-local) | Rust | Integrácia systémov | Použitie nízkoúrovňového SDK, asynchrónne operácie, HTTP klient reqwest |

#### Kategórie ukážok podľa použitia

**RAG (Retrieval-Augmented Generation)**
- **dotNET/rag**: Kompletná implementácia RAG pomocou Semantic Kernel, vektorovej databázy Qdrant a JINA embeddings
- **Architektúra**: Spracovanie dokumentov → Rozdelenie textu → Vektorové embeddings → Vyhľadávanie podobnosti → Odpovede s kontextom
- **Technológie**: Microsoft.SemanticKernel, Qdrant.Client, BERT ONNX embeddings, streamovanie dokončenia chatu

**Desktopové aplikácie**
- **electron/foundry-chat**: Produkčne pripravená chatovacia aplikácia s prepínaním medzi lokálnymi a cloudovými modelmi
- **Funkcie**: Výber modelu, streamovanie odpovedí, spracovanie chýb, multiplatformové nasadenie
- **Architektúra**: Hlavný proces Electron, IPC komunikácia, bezpečné preload skripty

**Príklady integrácie SDK**
- **JavaScript (Node.js)**: Základná interakcia s modelom a streamovanie odpovedí
- **Python**: Použitie OpenAI-kompatibilného API s asynchrónnym streamovaním
- **Rust**: Nízkoúrovňová integrácia s reqwest a tokio pre asynchrónne operácie

#### Predpoklady pre ukážky Foundry Local

**Systémové požiadavky:**
- Windows 11 s nainštalovaným Foundry Local
- Node.js v16+ pre ukážky JavaScript/Electron
- .NET 8.0+ pre ukážky C#
- Python 3.10+ pre ukážky Python
- Rust 1.70+ pre ukážky Rust

**Inštalácia:**
```powershell
# Install Foundry Local
winget install Microsoft.FoundryLocal

# Verify installation
foundry --version
foundry model list
```

#### Nastavenie špecifické pre ukážky

**dotNET RAG ukážka:**
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

**Electron Chat ukážka:**
```powershell
# Set environment variables for cloud fallback
$env:YOUR_API_KEY="your-cloud-api-key"
$env:YOUR_ENDPOINT="your-cloud-endpoint"
$env:YOUR_MODEL_NAME="your-cloud-model"

# Install dependencies and run
npm install
npm start
```

**JavaScript/Python/Rust ukážky:**
```powershell
# Download model (example with phi-3.5-mini)
foundry model run phi-3.5-mini

# Run respective sample
node src/app.js          # JavaScript
python src/app.py        # Python
cargo run               # Rust
```

#### Kľúčové funkcie

**Katalóg modelov**
- Komplexná zbierka predoptimalizovaných open-source modelov
- Modely optimalizované pre CPU, GPU a NPU na okamžité nasadenie
- Podpora populárnych rodín modelov vrátane Llama, Mistral, Phi a špecializovaných doménových modelov

**Integrácia CLI**
- Rozhranie príkazového riadku na správu a nasadenie modelov
- Automatizované pracovné postupy optimalizácie a kvantizácie
- Integrácia s populárnymi vývojovými prostrediami a CI/CD pipeline

**Lokálne nasadenie**
- Kompletná offline prevádzka bez závislosti na cloude
- Podpora vlastných formátov a konfigurácií modelov
- Efektívne poskytovanie modelov s automatickou optimalizáciou hardvéru

### 3. Windows ML

Windows ML slúži ako hlavná AI platforma a integrované runtime prostredie na Windows, umožňujúce vývojárom efektívne nasadzovať vlastné modely naprieč širokým ekosystémom hardvéru Windows.

#### Výhody architektúry

**Univerzálna podpora hardvéru**
- Automatická optimalizácia pre AMD, Intel, NVIDIA a Qualcomm čipy
- Podpora CPU, GPU a NPU s transparentným prepínaním
- Abstrakcia hardvéru, ktorá eliminuje prácu na optimalizácii špecifickej pre platformu

**Flexibilita modelov**
- Podpora formátu modelov ONNX s automatickou konverziou z populárnych frameworkov
- Nasadenie vlastných modelov s výkonnosťou na úrovni produkcie
- Integrácia s existujúcimi architektúrami aplikácií Windows

**Integrácia pre podniky**
- Kompatibilita s bezpečnostnými a súladovými rámcami Windows
- Podpora nástrojov na nasadenie a správu v podnikoch
- Integrácia so systémami na správu a monitorovanie zariadení Windows

## Pracovný postup vývoja

### Fáza 1: Nastavenie prostredia a konfigurácia nástrojov

**Príprava vývojového prostredia**
1. Nainštalujte Visual Studio 2022 s pracovnými záťažami C++ a .NET
2. Nainštalujte Windows App SDK 1.8.1 alebo novší
3. Konfigurujte nástroje Windows AI Foundry CLI
4. Nastavte rozšírenie AI Toolkit pre Visual Studio Code
5. Zabezpečte nástroje na profilovanie výkonu a monitorovanie
6. Uistite sa, že máte konfiguráciu ARM64 pre optimalizáciu Copilot+ PC

**Nastavenie repozitára ukážok**
1. Klonujte [repozitár ukážok Windows App SDK](https://github.com/microsoft/WindowsAppSDK-Samples)
2. Prejdite do `Samples/WindowsAIFoundry/cs-winui` pre príklady API Windows AI
3. Prejdite do `Samples/WindowsML` pre komplexné príklady Windows ML
4. Skontrolujte [požiadavky na zostavenie](https://learn.microsoft.com/windows/apps/windows-app-sdk/system-requirements) pre vaše cieľové platformy

**Preskúmanie AI Dev Gallery**
- Preskúmajte ukážkové aplikácie a referenčné implementácie
- Testujte API Windows AI s interaktívnymi ukážkami
- Skontrolujte zdrojový kód pre osvedčené postupy a vzory
- Identifikujte relevantné ukážky pre váš konkrétny prípad použitia

### Fáza 2: Výber modelu a integrácia

**Analýza požiadaviek**
- Definujte funkčné požiadavky na AI schopnosti
- Stanovte obmedzenia výkonu a ciele optimalizácie
- Vyhodnoťte požiadavky na ochranu súkromia a bezpečnosť
- Naplánujte architektúru nasadenia a stratégie škálovania

**Hodnotenie modelu**
- Použite Foundry Local na testovanie open-source modelov pre váš prípad použitia
- Porovnajte API Windows AI s požiadavkami na vlastné modely
- Vyhodnoťte kompromisy medzi veľkosťou modelu, presnosťou a rýchlosťou inferencie
- Prototypujte integračné prístupy s vybranými modelmi

### Fáza 3: Vývoj aplikácie

**Základná integrácia**
- Implementujte integráciu API Windows AI s riadnym spracovaním chýb
- Navrhnite používateľské rozhrania, ktoré zohľadňujú pracovné postupy AI
- Implementujte stratégie ukladania do vyrovnávacej pamäte a optimalizácie pre inferenciu modelov
- Pridajte telemetriu a monitorovanie výkonu AI operácií

**Testovanie a validácia**
- Testujte aplikácie na rôznych konfiguráciách hardvéru Windows
- Validujte výkonnostné metriky pri rôznych podmienkach zaťaženia
- Implementujte automatizované testovanie spoľahlivosti funkcií AI
- Vykonajte testovanie používateľskej skúsenosti s funkciami vylepšenými AI

### Fáza 4: Optimalizácia a nasadenie

**Optimalizácia výkonu**
- Profilujte výkon aplikácie na cieľových konfiguráciách hardvéru
- Optimalizujte využitie pamäte a stratégie načítania modelov
- Implementujte adaptívne správanie na základe dostupných hardvérových schopností
- Doladite používateľskú skúsenosť pre rôzne scenáre výkonu

**Nasadenie do produkcie**
- Zabaľte aplikácie s riadnymi závislosťami modelov AI
- Implementujte mechanizmy aktualizácie modelov a logiky aplikácie
- Konfigurujte monitorovanie a analytiku pre produkčné prostredia
- Naplánujte stratégie nasadenia pre podnikové a spotrebiteľské aplikácie

## Praktické príklady implementácie

### Príklad 1: Inteligentná aplikácia na spracovanie dokumentov

Vytvorte aplikáciu Windows, ktorá spracováva dokumenty pomocou viacerých AI schopností:

**Použité technológie:**
- Phi Silica na sumarizáciu dokumentov a odpovede na otázky
- OCR API na extrakciu textu zo skenovaných dokumentov
- API na popis obrázkov na analýzu grafov a diagramov
- Vlastné ONNX modely na klasifikáciu dokumentov

**Prístup k implementácii:**
- Navrhnite modulárnu architektúru s pripojiteľnými AI komponentmi
- Implementujte asynchrónne spracovanie pre veľké dávky dokumentov
- Pridajte indikátory pokroku a podporu zrušenia pre dlhodobé operácie
- Zahrňte offline schopnosti na spracovanie citlivých dokumentov

### Príklad 2: Systém na správu maloobchodných zásob

Vytvorte AI-poháňaný systém na správu zásob pre maloobchodné aplikácie:

**Použité technológie:**
- Segmentácia obrázkov na identifikáciu produktov
- Vlastné vízové modely na klasifikáciu značiek a kategórií
- Nasadenie špecializovaných jazykových modelov pre maloobchod cez Foundry Local
- Integrácia s existujúcimi POS a systémami zásob

**Prístup k implementácii:**
- Vytvorte integráciu kamery na skenovanie produktov v reálnom čase
- Implementujte rozpoznávanie čiarových kódov a vizuálnych produktov
- Pridajte prirodzené jazykové dotazy na zásoby pomocou lokálnych jazykových modelov
- Navrhnite škálovateľnú architektúru pre nasadenie vo viacerých predajniach

### Príklad 3: Asistent na dokumentáciu v zdravotníctve

Vyvinúť nástroj na dokumentáciu v zdravotníctve s ochranou súkromia:

**Použité technológie:**
- Phi Silica na generovanie lekárskych poznámok a podporu klinických rozhodnutí
- OCR na digitalizáciu ručne písaných lekárskych záznamov
- Vlastné lekárske jazykové modely nasadené cez Windows ML
- Lokálne vektorové úložisko na vyhľadávanie medicínskych znalostí

**Prístup k implementácii:**
- Zabezpečte kompletnú offline prevádzku na ochranu súkromia pacientov
- Implementujte validáciu a návrhy medicínskej terminológie
- Pridajte auditné logovanie na dodržiavanie regulácií
- Navrhnite integráciu s existujúcimi systémami elektronických zdravotných záznamov

## Stratégie optimalizácie výkonu

### Vývoj zohľadňujúci hardvér

**Optimalizácia pre NPU**
- Navrhnite aplikácie na využitie schopností NPU na Copilot+ PC
- Implementujte plynulý prechod na GPU/CPU na zariadeniach bez NPU
- Optimalizujte formáty modelov pre akceleráciu špecifickú pre NPU
- Monitorujte využitie NPU a jeho tepelné charakteristiky

**Správa pamäte**
- Implementujte efektívne stratégie načítania a ukladania modelov
- Použite mapovanie pamäte pre veľké modely na zníženie času spustenia
- Navrhnite aplikácie šetrné k pamäti pre zariadenia s obmedzenými zdrojmi
- Implementujte kvantizáciu modelov na optimalizáciu pamäte

**Efektivita batérie**
- Optimalizujte AI operácie na minimálnu spotrebu energie
- Implementujte adaptívne spracovanie na základe stavu batérie
- Navrhnite efektívne spracovanie na pozadí pre kontinuálne AI operácie
- Použite nástroje na profilovanie spotreby energie na optimalizáciu využitia

### Úvahy o škálovateľnosti

**Multithreading**
- Navrhnite bezpečné AI operácie pre súbežné spracovanie
- Implementujte efektívne rozdelenie práce medzi dostupné jadrá
- Použite vzory async/await na neblokujúce AI operácie
- Naplánujte optimalizáciu thread poolu pre rôzne konfigurácie hardvéru

**Stratégie ukladania do vyrovnávacej pamäte**
- Implementujte inteligentné ukladanie do vyrovnávacej pamäte pre často používané AI operácie
- Navrhnite stratégie invalidácie vyrovnávacej pamäte pre aktualizácie modelov
- Použite trvalé ukladanie do vyrovnávacej pamäte pre nákladné operácie predspracovania
- Implementujte distribuované ukladanie do vyrovnávacej pamäte pre scenáre s viacerými používateľmi

## Najlepšie postupy pre bezpečnosť a ochranu súkromia

### Ochrana údajov

**Lokálne spracovanie**
- Zabezpečte, aby citlivé údaje nikdy neopustili lokálne zariadenie
- Implementujte bezpečné úložisko pre AI modely a dočasné údaje
- Použite bezpečnostné funkcie Windows na sandboxing aplikácií
- Aplikujte šifrovanie na uložené modely a medzivýsledky spracovania

**Bezpečnosť modelov**
- Validujte integritu modelov pred ich načítaním a vykonaním
- Implementujte bezpečné mechanizmy aktualizácie modelov
- Použite podpísané modely na prevenciu manipulácie
- Aplikujte kontrolu prístupu na súbory modelov a konfigurácie

### Úvahy o súlade

**Regulačné požiadavky**
- Navrhnite aplikácie tak, aby spĺňali GDPR, HIPAA a ďalšie regulačné požiadavky
- Implementujte auditné logovanie pre procesy rozhodovania AI
- Poskytnite funkcie transparentnosti pre výsledky generované AI
- Umožnite používateľom kontrolu nad spracovaním údajov AI

**Bezpečnosť pre podniky**
- Integrujte s bezpečnostnými politikami Windows pre podniky
- Podporte spravované nasadenie prostredníctvom nástrojov na správu podnikov
- Implementujte kontrolu prístupu na základe rolí pre funkcie AI
- Poskytnite administratívne ovládacie prvky pre funkcie AI

## Riešenie problémov a ladenie

### Bežné vývojové výzvy

**Problémy s konfiguráciou zostavenia**
- Uistite sa, že máte konfiguráciu platformy ARM64 pre ukážky API Windows AI
- Overte kompatibilitu verzie Windows App SDK (vyžaduje sa 1.8.1+)
- Skontrolujte, či je správne nakonfigurovaná identita balíka (vyžaduje sa pre API Windows AI)
- Validujte, že nástroje na zostavenie podporujú cieľovú verziu frameworku

**Problémy s načítaním modelov**
- Validujte kompatibilitu modelov ONNX s Windows ML
- Skontrolujte integritu súborov modelov a požiadavky na formát
- Overte požiadavky na schopnosti hardvéru pre konkrétne modely
- Ladte problémy s alokáciou pamäte počas načítania modelov
- Uistite sa, že je zaregistrovaný poskytovateľ vykonávania pre akceleráciu hardvéru

**Úvahy o režime nasadenia**
- **Samostatný režim**: Plne podporovaný s väčšou veľkosťou nasadenia
- **Režim závislý na frameworku**: Menšia stopa, ale vyžaduje zdieľaný runtime
- **Nepackované aplikácie**: Už nie sú podporované pre API Windows AI
- Použite `dotnet run -p:Platform=ARM64 -p:SelfContained=true` pre samostatné nasadenie ARM64

**Problémy s výkonom**
- Profilujte výkon aplikácie na rôznych konfiguráciách hardvéru
- Identifikujte úzke miesta v spracovateľských pipeline AI
- Optimalizujte operácie predspracovania a postprocesovania údajov
- Implementujte monitorovanie výkonu a upozornenia

**Problémy s integráciou**
- Ladte problémy s integráciou API s riadnym spracovaním chýb
- Validujte formáty vstupných údajov a požiadavky na predspracovanie
- Dôkladne testujte hraničné prípady a podmienky chýb
- Implementujte komplexné logovanie na ladenie problémov v produkcii

### Nástroje a techniky ladenia

**Integrácia Visual Studio**
- Použite debugger AI Toolkit na analýzu vykonávania modelov
- Implementujte profilovanie výkonu pre AI operácie
- Ladte asynchrónne AI operácie s riadnym spracovaním výnimiek
- Použite nástroje na profilovanie pamäte na optimaliz
- [Prehľad Windows ML](https://learn.microsoft.com/windows/ai/new-windows-ml/overview/)
- [Systémové požiadavky Windows App SDK](https://docs.microsoft.com/windows/apps/windows-app-sdk/system-requirements)
- [Nastavenie vývojového prostredia Windows App SDK](https://docs.microsoft.com/windows/apps/windows-app-sdk/set-up-your-development-environment)
- 

### Ukážkové repozitáre a kód
- [Ukážky Windows App SDK - Windows AI Foundry](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsAIFoundry)
- [Ukážky Windows App SDK - Windows ML](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML)
- [Príklady inferencie ONNX Runtime](https://github.com/microsoft/onnxruntime-inference-examples)
- [Repozitár ukážok Windows App SDK](https://github.com/microsoft/WindowsAppSDK-Samples)

### Vývojárske nástroje
- [AI Toolkit pre Visual Studio Code](https://learn.microsoft.com/windows/ai/toolkit/)
- [AI Dev Gallery](https://learn.microsoft.com/windows/ai/ai-dev-gallery/)
- [Ukážky Windows AI](https://learn.microsoft.com/windows/ai/samples/)
- [Nástroje na konverziu modelov](https://code.visualstudio.com/docs/intelligentapps/modelconversion)

### Technická podpora
- [Dokumentácia Windows ML](https://learn.microsoft.com/windows/ai/new-windows-ml/overview)
- [Dokumentácia ONNX Runtime](https://onnxruntime.ai/docs/)
- [Dokumentácia Windows App SDK](https://docs.microsoft.com/windows/apps/windows-app-sdk/)
- [Nahlásenie problémov - Ukážky Windows App SDK](https://github.com/microsoft/WindowsAppSDK-Samples/issues)

### Komunita a podpora
- [Komunita vývojárov Windows](https://developer.microsoft.com/en-us/windows/)
- [Blog Windows AI Foundry](https://blogs.windows.com/windowsdeveloper/)
- [Microsoft Learn AI školenia](https://learn.microsoft.com/training/browse/?products=windows&subjects=artificial-intelligence)

---

*Tento sprievodca je navrhnutý tak, aby sa vyvíjal spolu s rýchlo napredujúcim ekosystémom Windows AI. Pravidelné aktualizácie zabezpečujú súlad s najnovšími schopnosťami platformy a najlepšími postupmi vývoja.*

[08. Praktické skúsenosti s Microsoft Foundry Local - Kompletná sada nástrojov pre vývojárov](../Module08/README.md)

---

**Upozornenie**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, prosím, berte na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
# Sprievodca vývojom Windows Edge AI

## Úvod

Vitajte vo Windows Edge AI Development – váš komplexný sprievodca tvorbou inteligentných aplikácií, ktoré využívajú silu AI priamo na zariadení pomocou platformy Windows AI Foundry od spoločnosti Microsoft. Tento sprievodca je špeciálne navrhnutý pre vývojárov Windows, ktorí chcú integrovať špičkové Edge AI funkcie do svojich aplikácií a zároveň využiť celú škálu hardvérovej akcelerácie Windows.

### Výhoda Windows AI

Windows AI Foundry predstavuje jednotnú, spoľahlivú a bezpečnú platformu, ktorá podporuje celý životný cyklus vývoja AI – od výberu modelu a jeho doladenia až po optimalizáciu a nasadenie naprieč CPU, GPU, NPU a hybridnými cloudovými architektúrami. Táto platforma demokratizuje vývoj AI tým, že poskytuje:

- **Hardvérovú abstrakciu**: Bezproblémové nasadenie na kremeňoch AMD, Intel, NVIDIA a Qualcomm
- **Inteligenciu na zariadení**: AI zachovávajúcu súkromie, ktorá beží výhradne na lokálnom hardvéri
- **Optimalizovaný výkon**: Modely predoptimalizované pre hardvérové konfigurácie Windows
- **Pripravenosť pre podniky**: Bezpečnostné a súladové funkcie produkčnej úrovne

### Windows ML 
Windows Machine Learning (ML) umožňuje vývojárom v C#, C++ a Pythone spúšťať ONNX AI modely lokálne na počítačoch Windows prostredníctvom ONNX Runtime s automatickým riadením poskytovateľov vykonávania pre rôzny hardvér (CPU, GPU, NPU). [ONNX Runtime](https://onnxruntime.ai/docs/) možno používať s modelmi z PyTorch, Tensorflow/Keras, TFLite, scikit-learn a ďalších frameworkov.


![WindowsML Diagram ilustrujúci ONNX model prechádzajúci cez Windows ML až k NPUs, GPU a CPU.](https://learn.microsoft.com/en-us/windows/ai/images/winml-diagram.png)

Windows ML poskytuje spoločnú systémovo zdieľanú kópiu ONNX Runtime, plus možnosť dynamicky sťahovať poskytovateľov vykonávania (EP).

### Prečo Windows pre Edge AI?

**Univerzálna podpora hardvéru**
Windows ML zabezpečuje automatickú hardvérovú optimalizáciu v celom ekosystéme Windows, čo zaručuje optimálny výkon vašich AI aplikácií bez ohľadu na základnú architektúru kremíka.

**Integrované AI runtime**
Vstavaný inferenčný motor Windows ML odstraňuje zložité požiadavky na nastavenie, čo umožňuje vývojárom sústrediť sa na logiku aplikácie namiesto infraštruktúry.

**Optimalizácia Copilot+ PC**
API špeciálne navrhnuté pre nové generácie Windows zariadení s vyhradenými Neural Processing Units (NPU), ktoré prinášajú výnimočný výkon na watt.

**Ekosystém vývojárov**
Bohaté nástroje vrátane integrácie do Visual Studio, komplexnej dokumentácie a ukážkových aplikácií urýchľujúcich vývoj.

## Ciele učenia

Ukončením tohto sprievodcu vývojom Windows Edge AI zvládnete základné zručnosti potrebné na tvorbu produkčne pripravených AI aplikácií na platforme Windows.

### Hlavné technické kompetencie

**Majstrovstvo Windows AI Foundry**
- Pochopiť architektúru a komponenty platformy Windows AI Foundry
- Orientovať sa v celom životnom cykle vývoja AI v rámci ekosystému Windows
- Implementovať bezpečnostné najlepšie praktiky pre AI aplikácie na zariadení
- Optimalizovať aplikácie pre rôzne hardvérové konfigurácie Windows

**Odbornosť v integrácii API**
- Ovládnuť Windows AI API pre textové, vizuálne a multimodálne aplikácie
- Implementovať integráciu jazykového modelu Phi Silica pre generovanie textu a uvažovanie
- Nasadiť počítačové videnie pomocou vstavaných API na spracovanie obrázkov
- Prispôsobiť predtrénované modely pomocou techník LoRA (Low-Rank Adaptation)

**Implementácia Foundry Local**
- Prezerať, hodnotiť a nasadzovať open-source jazykové modely pomocou Foundry Local CLI
- Pochopiť optimalizáciu modelov a kvantizáciu pre lokálne nasadenie
- Implementovať offline AI schopnosti, ktoré fungujú bez internetového pripojenia
- Riadiť životný cyklus modelov a aktualizácie v produkčných prostrediach

**Nasadenie Windows ML**
- Priniesť vlastné ONNX modely do Windows aplikácií pomocou Windows ML
- Využiť automatickú hardvérovú akceleráciu na CPU, GPU a NPU architektúrach
- Implementovať inferenciu v reálnom čase s optimálnym využitím zdrojov
- Navrhovať škálovateľné AI aplikácie pre rôzne kategórie Windows zariadení

### Zručnosti vývoja aplikácií

**Vývoj Windows multiplatformových aplikácií**
- Stavať AI poháňané aplikácie pomocou .NET MAUI pre univerzálne nasadenie na Windows
- Integrovať AI funkcie do Win32, UWP a progresívnych webových aplikácií
- Navrhnúť responzívne UI dizajny prispôsobujúce sa stavom AI spracovania
- Spravovať asynchrónne AI operácie s vhodnými vzormi používateľského zážitku

**Optimalizácia výkonu**
- Profilovať a optimalizovať výkon AI inferencie na rôznych hardvérových konfiguráciách
- Implementovať efektívnu správu pamäte pre veľké jazykové modely
- Navrhovať aplikácie, ktoré sa pekne degradujú podľa dostupných hardvérových schopností
- Použiť cache stratégie pre často používané AI operácie

**Produkčná pripravenosť**
- Implementovať komplexné spracovanie chýb a záložné mechanizmy
- Navrhovať telemetriu a monitorovanie výkonu AI aplikácií
- Použiť bezpečnostné najlepšie praktiky pre lokálne ukladanie a spúšťanie AI modelov
- Plánovať stratégie nasadenia pre podnikové a koncové používateľské aplikácie

### Podnikateľské a strategické porozumenie

**Architektúra AI aplikácií**
- Navrhovať hybridné architektúry optimalizované medzi lokálnym a cloudovým AI spracovaním
- Hodnotiť kompromisy medzi veľkosťou modelu, presnosťou a rýchlosťou inferencie
- Plánovať architektúry tokov dát, ktoré zachovávajú súkromie a zároveň umožňujú inteligenciu
- Implementovať nákladovo efektívne AI riešenia škálovateľné podľa požiadaviek používateľov

**Pozicionovanie na trhu**
- Pochopiť konkurenčné výhody natívnych AI aplikácií pre Windows
- Identifikovať prípady použitia, kde AI priamo na zariadení prináša lepšie používateľské zážitky
- Vyvíjať stratégie vstupu na trh pre Windows aplikácie s AI rozšírením
- Pozicionovať aplikácie tak, aby využívali výhody ekosystému Windows

## Ukážky AI Windows App SDK

Windows App SDK poskytuje komplexné ukážky demonštrujúce AI integráciu cez viacero frameworkov a nasadzovacích scenárov. Tieto ukážky sú základným referenčným materiálom pre pochopenie vzorov vývoja AI na Windows.

### Windows AI Foundry ukážky

| Ukážka | Framework | Zameranie | Kľúčové vlastnosti |
|--------|-----------|------------|-------------|
| [cs-winui](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsAIFoundry/cs-winui) | C# WinUI 3 | Integrácia Windows AI API | Kompletná WinUI aplikácia demonštrujúca Windows AI API, ARM64 optimalizácia, balíčkové nasadenie |

**Kľúčové technológie:**
- Windows AI API
- WinUI 3 framework
- Optimalizácia pre platformu ARM64
- Kompatibilita s Copilot+ PC
- Nasadenie balíčkovej aplikácie

**Predpoklady:**
- Windows 11 s odporúčaným Copilot+ PC
- Visual Studio 2022
- Konfigurácia zostavenia ARM64
- Windows App SDK 1.8.1+

### Windows ML Ukážky

#### C++ Ukážky

| Ukážka | Typ | Zameranie | Kľúčové vlastnosti |
|--------|------|------------|-------------|
| [CppConsoleDesktop](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Konzolová aplikácia | Základné Windows ML | Objavovanie EP, príkazové riadkové možnosti, kompilácia modelov |
| [CppConsoleDesktop.FrameworkDependent](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Konzolová aplikácia | Nasadenie závislé na frameworku | Zdieľané runtime, menšia veľkosť nasadenia |
| [CppConsoleDesktop.SelfContained](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Konzolová aplikácia | Samostatné nasadenie | Samostatné nasadenie bez závislostí na runtime |
| [CppConsoleDll](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | DLL | Knižničné použitie | WindowsML v zdieľanej knižnici, správa pamäte |
| [CppResnetBuildDemo](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Demo | Návod ResNet | Konverzia modelu, kompilácia EP, Build 2025 návod |

#### C# Ukážky

**Konzolové aplikácie**

| Ukážka | Typ | Zameranie | Kľúčové vlastnosti |
|--------|------|------------|-------------|
| [CSharpConsoleDesktop](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs) | Konzolová aplikácia | Základná integrácia C# | Použitie zdieľaných pomocníkov, rozhranie príkazového riadku |
| [ResnetBuildDemoCS](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs) | Demo | Návod ResNet | Konverzia modelu, kompilácia EP, Build 2025 návod |

**GUI aplikácie**

| Ukážka | Framework | Zameranie | Kľúčové vlastnosti |
|--------|-----------|------------|-------------|
| [cs-wpf](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs-wpf) | WPF | Desktop GUI | Klasifikácia obrázkov s WPF rozhraním |
| [cs-winforms](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs-winforms) | Windows Forms | Tradičné GUI | Klasifikácia obrázkov s Windows Forms |
| [cs-winui](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs-winui) | WinUI 3 | Moderné GUI | Klasifikácia obrázkov s WinUI 3 rozhraním |

#### Python Ukážky

| Ukážka | Jazyk | Zameranie | Kľúčové vlastnosti |
|--------|----------|------------|-------------|
| [SqueezeNetPython](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/python) | Python | Klasifikácia obrázkov | WinML Python väzby, dávkové spracovanie obrázkov |

### Predpoklady ukážok

**Systémové požiadavky:**
- Počítač Windows 11 so systémovou verziou 24H2 (build 26100) alebo vyššou
- Visual Studio 2022 s pracovnými záťažami C++ a .NET
- Windows App SDK 1.8.1 alebo novšie
- Python 3.10-3.13 pre Python vzorky na x64 a ARM64 zariadeniach

**Špecifické pre Windows AI Foundry:**
- Odporúčaný Copilot+ PC pre optimálny výkon
- Konfigurácia zostavenia ARM64 pre Windows AI ukážky
- Vyžaduje sa identita balíka (balíčkové aplikácie, nesbalíčkované už nepodporované)

### Bežný pracovný postup ukážok

Väčšina Windows ML ukážok nasleduje tento štandardný vzor:

1. **Inicializácia prostredia** - Vytvorenie ONNX Runtime prostredia
2. **Registrácia poskytovateľov vykonávania** - Zistenie a registrácia dostupných hardvérových akcelerátorov (CPU, GPU, NPU)
3. **Načítanie modelu** - Načítanie ONNX modelu, voliteľne kompilácia pre cieľový hardvér
4. **Predspracovanie vstupu** - Konverzia obrázkov/dát do formátu vstupu modelu
5. **Spustenie inferencie** - Vykonanie modelu a získanie predpovedí
6. **Spracovanie výsledkov** - Použitie softmax a zobrazenie najlepších predpovedí

### Použité modelové súbory

| Model | Účel | Zaradený | Poznámky |
|-------|---------|----------|-------|
| SqueezeNet | Ľahká klasifikácia obrázkov | ✅ Zaradený | Predtrénovaný, pripravený na použitie |
| ResNet-50 | Vysokopresná klasifikácia obrázkov | ❌ Vyžaduje konverziu | Použiť [AI Toolkit](https://code.visualstudio.com/docs/intelligentapps/modelconversion) na konverziu |

### Podpora hardvéru

Všetky ukážky automaticky detekujú a využívajú dostupný hardvér:
- **CPU** - Univerzálna podpora naprieč všetkými Windows zariadeniami
- **GPU** - Automatická detekcia a optimalizácia pre dostupný grafický hardvér
- **NPU** - Využíva Neural Processing Units na podporovaných zariadeniach (Copilot+ PC)

## Komponenty platformy Windows AI Foundry

### 1. Windows AI API

Windows AI API poskytujú pripravené k použitiu AI funkcie poháňané modelmi priamo na zariadení, optimalizované pre efektivitu a výkon na zariadeniach Copilot+ PC s minimálnym nastavením.

#### Hlavné kategórie API

**Phi Silica jazykový model**
- Malý, ale výkonný jazykový model pre generovanie textu a uvažovanie
- Optimalizovaný pre inferenciu v reálnom čase s minimálnou spotrebou energie
- Podpora vlastného doladenia pomocou techník LoRA
- Integrácia s Windows semantickým vyhľadávaním a získavaním znalostí

**API počítačového videnia**
- **Rozpoznávanie textu (OCR)**: Vysoko presné extrahovanie textu z obrázkov
- **Superrozlíšenie obrázkov**: Zvýšenie rozlíšenia obrázkov pomocou lokálnych AI modelov
- **Segmentácia obrázkov**: Identifikácia a izolácia špecifických objektov na obrázkoch
- **Popis obrázkov**: Generovanie detailných textových popisov vizuálneho obsahu
- **Odstránenie objektov**: Odstránenie nežiadúcich objektov z obrázkov pomocou AI na inpainting

**Multimodálne schopnosti**
- **Integrácia videnia a jazyka**: Kombinácia porozumenia textu a obrázkov
- **Semantické vyhľadávanie**: Umožnenie prirodzených jazykových dotazov cez multimediálny obsah
- **Získavanie znalostí**: Budovanie inteligentných vyhľadávacích zážitkov s lokálnymi dátami

### 2. Foundry Local

Foundry Local poskytuje vývojárom rýchly prístup k pripraveným open-source jazykovým modelom pre Windows Silicon, ponúkajúc možnosť prezerať, testovať, interagovať a nasadzovať modely v lokálnych aplikáciách.

#### Ukážkové aplikácie Foundry Local

[Foundry Local repozitár](https://github.com/microsoft/Foundry-Local/tree/main/samples) poskytuje komplexné ukážky v rôznych programovacích jazykoch a frameworkoch, demonštrujúce rôzne vzory integrácie a prípady použitia.

| Ukážka | Jazyk/Framework | Zameranie | Kľúčové vlastnosti |
|--------|-------------------|------------|-------------|
| [dotNET/rag](https://github.com/microsoft/Foundry-Local/tree/main/samples/dotNET/rag) | C# / .NET | Implementácia RAG | Integrácia Semantic Kernel, Qdrant vektorový úložisko, JINA embeddings, ingestia dokumentov, streamovaný chat |
| [electron/foundry-chat](https://github.com/microsoft/Foundry-Local/tree/main/samples/electron/foundry-chat) | JavaScript / Electron | Desktop chat aplikácia | Multiplatformový chat, prepínanie modelov lokálne/cloud, integrácia OpenAI SDK, streamovanie v reálnom čase |
| [js/hello-foundry-local](https://github.com/microsoft/Foundry-Local/tree/main/samples/js/hello-foundry-local) | JavaScript / Node.js | Základná integrácia | Jednoduché použitie SDK, inicializácia modelu, základná chat funkčnosť |
| [python/hello-foundry-local](https://github.com/microsoft/Foundry-Local/tree/main/samples/python/hello-foundry-local) | Python | Základná integrácia | Použitie Python SDK, streamované odpovede, API kompatibilné s OpenAI |

| [rust/hello-foundry-local](https://github.com/microsoft/Foundry-Local/tree/main/samples/rust/hello-foundry-local) | Rust | Integrácia systémov | Použitie SDK na nízkej úrovni, asynchrónne operácie, HTTP klient reqwest |

#### Kategórie príkladov podľa prípadu použitia

**RAG (Retrieval-Augmented Generation)**
- **dotNET/rag**: Kompletná implementácia RAG pomocou Semantic Kernel, vektorovej databázy Qdrant a JINA embeddingov
- **Architektúra**: Vkladanie dokumentov → Rozdelenie textu → Vektorové embeddingy → Vyhľadávanie podobnosti → Kontextovo-aware odpovede
- **Technológie**: Microsoft.SemanticKernel, Qdrant.Client, BERT ONNX embeddingy, streamovanie dokončenia chatu

**Desktopové aplikácie**
- **electron/foundry-chat**: Produkčne pripravená chat aplikácia s prepínaním medzi lokálnym a cloudovým modelom
- **Funkcie**: Výber modelu, streamovanie odpovedí, spracovanie chýb, multiplatformové nasadenie
- **Architektúra**: Hlavný proces Electron, komunikácia IPC, zabezpečené preload skripty

**Príklady integrácie SDK**
- **JavaScript (Node.js)**: Základná interakcia s modelom a streamovanie odpovedí
- **Python**: Použitie API kompatibilného s OpenAI s asynchrónnym streamovaním
- **Rust**: Integrácia na nízkej úrovni s reqwest a tokio pre asynchrónne operácie

#### Predpoklady pre príklady Foundry Local

**Systémové požiadavky:**
- Windows 11 s nainštalovaným Foundry Local
- Node.js verzie 16+ pre príklady v JavaScripte/Electron
- .NET verzie 8.0+ pre príklady v C#
- Python verzia 3.10+ pre príklady v Pythone
- Rust verzia 1.70+ pre Rust príklady

**Inštalácia:**
```powershell
# Inštalácia Foundry Local
winget install Microsoft.FoundryLocal

# Overenie inštalácie
foundry --version
foundry model list
```

#### Nastavenie špecifické pre príklady

**dotNET RAG príklad:**
```powershell
# Nainštalujte požadované balíčky cez NuGet
# Microsoft.SemanticKernel.Connectors.Onnx
# Microsoft.SemanticKernel.Connectors.Qdrant
# Qdrant.Client

# Spustite vektorovú databázu Qdrant
docker run -p 6333:6333 qdrant/qdrant

# Spustite Jupyter notebook
jupyter notebook rag_foundrylocal_demo.ipynb
```

**Electron Chat príklad:**
```powershell
# Nastavte premenné prostredia pre cloudový záložný režim
$env:YOUR_API_KEY="your-cloud-api-key"
$env:YOUR_ENDPOINT="your-cloud-endpoint"
$env:YOUR_MODEL_NAME="your-cloud-model"

# Nainštalujte závislosti a spustite
npm install
npm start
```

**JavaScript/Python/Rust príklady:**
```powershell
# Stiahnite model (príklad s phi-3.5-mini)
foundry model run phi-3.5-mini

# Spustite príslušný príklad
node src/app.js          # JavaScript
python src/app.py        # Python
cargo run               # Rust
```

#### Kľúčové vlastnosti

**Katalóg modelov**
- Komplexná zbierka predoptimalizovaných open-source modelov
- Modely optimalizované pre CPU, GPU a NPU na okamžité nasadenie
- Podpora populárnych modelových rodín vrátane Llama, Mistral, Phi a špecializovaných doménových modelov

**Integrácia CLI**
- Príkazové rozhranie pre správu a nasadenie modelov
- Automatizované pracovné toky optimalizácie a kvantizácie
- Integrácia s populárnymi vývojovými prostrediami a CI/CD pipeline-ami

**Lokálne nasadenie**
- Kompletná prevádzka offline bez závislosti na cloude
- Podpora vlastných formátov a konfigurácií modelov
- Efektívne podávanie modelov s automatickou hardvérovou optimalizáciou

### 3. Windows ML

Windows ML slúži ako hlavná AI platforma a integrované runtime pre inferenciu na Windows, čo umožňuje vývojárom efektívne nasadzovať vlastné modely naprieč širokou hardvérovou ekosystémou Windows.

#### Výhody architektúry

**Univerzálna podpora hardvéru**
- Automatická optimalizácia pre AMD, Intel, NVIDIA a Qualcomm čipy
- Podpora CPU, GPU a NPU vykonávania s transparentným prepínaním
- Hardvérová abstrakcia, ktorá eliminuje prácu na platformovo-špecifickej optimalizácii

**Flexibilita modelov**
- Podpora ONNX modelového formátu s automatickou konverziou z populárnych frameworkov
- Nasadenie vlastných modelov s výkonom na produkčnej úrovni
- Integrácia s existujúcimi architektúrami Windows aplikácií

**Podniková integrácia**
- Kompatibilné s bezpečnostnými a súladovými rámcami Windows
- Podpora nástrojov pre podnikovú správu a nasadenie
- Integrácia so systémami správy a monitorovania zariadení Windows

## Vývojový pracovný postup

### Fáza 1: Nastavenie prostredia a konfigurácia nástrojov

**Príprava vývojového prostredia**
1. Nainštalujte Visual Studio 2022 s workloadmi C++ a .NET
2. Nainštalujte Windows App SDK 1.8.1 alebo novší
3. Nakonfigurujte Windows AI Foundry CLI nástroje
4. Nastavte AI Toolkit rozšírenie pre Visual Studio Code
5. Zaveste nástroje na profilovanie výkonu a monitorovanie
6. Zabezpečte ARM64 konfiguračné nastavenie pre optimalizáciu PC Copilot+

**Nastavenie repozitára príkladov**
1. Klonujte [Windows App SDK Samples repository](https://github.com/microsoft/WindowsAppSDK-Samples)
2. Prejdite na `Samples/WindowsAIFoundry/cs-winui` pre príklady Windows AI API
3. Prejdite na `Samples/WindowsML` pre komplexné príklady Windows ML
4. Skontrolujte [požiadavky na zostavenie](https://learn.microsoft.com/windows/apps/windows-app-sdk/system-requirements) pre vaše cieľové platformy

**Preskúmanie AI Dev Galérie**
- Preskúmajte ukážkové aplikácie a referenčné implementácie
- Testujte Windows AI API prostredníctvom interaktívnych demonštrácií
- Preštudujte zdrojový kód pre najlepšie praktiky a vzory
- Identifikujte relevantné príklady pre váš konkrétny prípad použitia

### Fáza 2: Výber a integrácia modelu

**Analýza požiadaviek**
- Definujte funkčné požiadavky na AI schopnosti
- Stanovte výkonnostné obmedzenia a ciele optimalizácie
- Vyhodnoťte požiadavky na súkromie a bezpečnosť
- Naplánujte architektúru nasadenia a škálovania

**Hodnotenie modelov**
- Použite Foundry Local na testovanie open-source modelov pre váš prípad použitia
- Porovnajte Windows AI API s požiadavkami vlastných modelov
- Vyhodnoťte kompromisy medzi veľkosťou modelu, presnosťou a rýchlosťou inferencie
- Prototypujte integračné prístupy s vybranými modelmi

### Fáza 3: Vývoj aplikácií

**Jadrová integrácia**
- Implementujte integráciu Windows AI API s riadnym spracovaním chýb
- Navrhnite používateľské rozhrania, ktoré zohľadňujú pracovné toky AI spracovania
- Implementujte cachovanie a optimalizačné stratégie pre inferenciu modelu
- Pridajte telemetriu a monitorovanie výkonu AI operácií

**Testovanie a validácia**
- Testujte aplikácie na rôznych hardvérových konfiguráciách Windows
- Validujte výkonnostné metriky pri rôznych záťažiach
- Implementujte automatizované testovanie spoľahlivosti AI funkcií
- Vykonajte testovanie používateľskej skúsenosti s AI vylepšenými funkciami

### Fáza 4: Optimalizácia a nasadenie

**Optimalizácia výkonu**
- Profilujte výkon aplikácie na cieľových hardvérových konfiguráciách
- Optimalizujte využitie pamäte a stratégie načítania modelov
- Implementujte adaptívne správanie na základe dostupných hardvérových schopností
- Vyladte používateľskú skúsenosť pre rôzne výkonnostné scenáre

**Produkčné nasadenie**
- Balenie aplikácií so správnymi závislosťami AI modelov
- Implementujte mechanizmy aktualizácie modelov a aplikačnej logiky
- Nakonfigurujte monitorovanie a analytiku pre produkčné prostredie
- Plánujte stratégie uvedenia pre podnikové i spotrebiteľské nasadenia

## Praktické príklady implementácie

### Príklad 1: Inteligentná aplikácia na spracovanie dokumentov

Vytvorte Windows aplikáciu, ktorá spracováva dokumenty pomocou viacerých AI schopností:

**Použité technológie:**
- Phi Silica pre sumarizáciu dokumentov a odpovedanie na otázky
- OCR API na extrakciu textu zo skenovaných dokumentov
- API pre popis obrázkov na analýzu grafov a diagramov
- Vlastné ONNX modely pre klasifikáciu dokumentov

**Prístup k implementácii:**
- Navrhnite modulárnu architektúru s vymeniteľnými AI komponentmi
- Implementujte asynchrónne spracovanie pre veľké dávky dokumentov
- Pridajte indikátory priebehu a podporu zrušenia pre dlhé operácie
- Zabezpečte offline funkčnosť pre spracovanie citlivých dokumentov

### Príklad 2: Systém riadenia maloobchodných zásob

Vytvorte AI-poháňaný inventárny systém pre maloobchodné aplikácie:

**Použité technológie:**
- Segmentácia obrázkov pre identifikáciu produktov
- Vlastné vizuálne modely na klasifikáciu značiek a kategórií
- Nasadenie Foundry Local so špecializovanými jazykovými modelmi pre maloobchod
- Integrácia s existujúcimi POS a inventárnymi systémami

**Prístup k implementácii:**
- Vybudujte integráciu kamery pre skenovanie produktov v reálnom čase
- Implementujte rozpoznávanie čiarových kódov a vizuálnych produktov
- Pridajte dotazy v prirodzenom jazyku pre inventár pomocou lokálnych jazykových modelov
- Navrhnite škálovateľnú architektúru pre nasadenie v rámci viacerých predajní

### Príklad 3: Asistent dokumentácie v zdravotníctve

Vyvinúť nástroj na tvorbu zdravotníckej dokumentácie s ochranou súkromia:

**Použité technológie:**
- Phi Silica pre generovanie lekárskych poznámok a klinickú podporu rozhodovania
- OCR pre digitalizáciu písaných lekárskych záznamov
- Vlastné medicínske jazykové modely nasadené cez Windows ML
- Lokálne ukladanie vektorov na získavanie medicínskych znalostí

**Prístup k implementácii:**
- Zabezpečte úplnú offline prevádzku pre ochranu súkromia pacientov
- Implementujte validáciu a návrhy lekárskej terminológie
- Pridajte auditovanie pre súlad s reguláciami
- Navrhnite integráciu so existujúcimi systémami elektronických zdravotných záznamov

## Stratégie optimalizácie výkonu

### Vývoj s ohľadom na hardvér

**Optimalizácia pre NPU**
- Navrhnite aplikácie pre využitie NPU schopností na PC Copilot+
- Implementujte hladký návrat na GPU/CPU na zariadeniach bez NPU
- Optimalizujte formáty modelov pre špecifické akcelerácie NPU
- Monitorujte využitie NPU a jeho tepelné charakteristiky

**Správa pamäte**
- Implementujte efektívne načítanie modelov a cachovanie
- Používajte mapovanie pamäte pre veľké modely na zníženie času spustenia
- Navrhnite aplikácie šetrné k pamäti pre zariadenia s obmedzenými zdrojmi
- Implementujte kvantizáciu modelov pre optimalizáciu pamäte

**Úspora batérie**
- Optimalizujte AI operácie pre minimálnu spotrebu energie
- Implementujte adaptívne spracovanie podľa stavu batérie
- Navrhnite efektívne pozadinské spracovanie pre kontinuálne AI operácie
- Používajte nástroje na profilovanie spotreby energie pre optimalizáciu

### Úvahy o škálovateľnosti

**Viacvláknovosť**
- Navrhnite vlákna bezpečné AI operácie na paralelné spracovanie
- Implementujte efektívne rozdeľovanie práce medzi dostupné jadrá
- Používajte async/await vzory pre neblokujúce AI operácie
- Plánujte optimalizáciu poolu vlákien pre rôzne hardvérové konfigurácie

**Cache stratégie**
- Implementujte inteligentné cachovanie často používaných AI operácií
- Navrhnite stratégie invalidácie cache pri aktualizáciách modelov
- Používajte perzistentné cachovanie pre nákladné predspracovania
- Implementujte distribuované cachovanie pre viac používateľské scenáre

## Najlepšie praktiky zabezpečenia a ochrany súkromia

### Ochrana údajov

**Lokálne spracovanie**
- Zabezpečte, aby citlivé údaje nikdy neopustili lokálne zariadenie
- Implementujte bezpečné ukladanie AI modelov a dočasných údajov
- Využívajte bezpečnostné funkcie Windows pre sandboxovanie aplikácií
- Aplikujte šifrovanie pre uložené modely a medzištádium spracovania

**Bezpečnosť modelov**
- Validujte integritu modelov pred načítaním a vykonaním
- Implementujte bezpečné mechanizmy aktualizácie modelov
- Používajte podpísané modely na zabránenie manipulácii
- Aplikujte prístupové kontroly pre súbory modelov a konfigurácie

### Úvahy o súlade

**Zladenie s predpismi**
- Navrhnite aplikácie tak, aby vyhovovali GDPR, HIPAA a iným predpisom
- Implementujte auditovanie AI rozhodovacích procesov
- Poskytujte funkcie transparentnosti pre AI generované výsledky
- Umožnite používateľom kontrolu nad spracovaním AI dát

**Podniková bezpečnosť**
- Integrujte s Windows podnikateľskými bezpečnostnými politikami
- Podporujte spravované nasadenie cez podnikové nástroje správy
- Implementujte prístupové kontroly založené na rolách pre AI funkcie
- Poskytujte administrátorské ovládanie AI funkčnosti

## Riešenie problémov a ladenie

### Bežné výzvy vo vývoji

**Problémy s konfiguráciou zostavenia**
- Zabezpečte ARM64 konfiguráciu platformy pre Windows AI API príklady
- Overte kompatibilitu verzie Windows App SDK (vyžaduje sa 1.8.1+)
- Skontrolujte správne nastavenie identity balíka (vyžadované pre Windows AI API)
- Validujte, že nástroje zostavenia podporujú cieľovú verziu frameworku

**Problémy s načítaním modelov**
- Validujte kompatibilitu ONNX modelov s Windows ML
- Skontrolujte integritu súborov modelov a požiadavky na formát
- Overte hardvérové požiadavky pre konkrétne modely
- Ladenie problémov s alokáciou pamäte počas načítania modelu
- Zabezpečte registráciu poskytovateľa vykonávania pre hardvérové zrýchlenie

**Úvahy o režime nasadenia**
- **Samostatný režim**: Plne podporovaný s väčšou veľkosťou nasadenia
- **Režim závislý na frameworku**: Menšia stopa ale vyžaduje zdieľané runtime
- **Nenabalené aplikácie**: Už nie sú podporované pre Windows AI API
- Použite `dotnet run -p:Platform=ARM64 -p:SelfContained=true` pre samostatné ARM64 nasadenie

**Problémy s výkonom**
- Profilujte výkon aplikácie na rôznych hardvérových konfiguráciách
- Identifikujte úzke miesta v AI spracovateľských potrubiach
- Optimalizujte operácie predspracovania a následného spracovania dát
- Implementujte monitorovanie výkonu a upozornenia

**Problémy s integráciou**
- Ladenie problémov integrácie API s riadnym spracovaním chýb
- Validujte vstupné dátové formáty a požiadavky na predspracovanie
- Testujte hraničné prípady a chybové stavy dôkladne
- Implementujte komplexné logovanie na ladenie produkčných problémov

### Nástroje a techniky ladenia

**Integrácia Visual Studio**
- Používajte AI Toolkit debugger pre analýzu vykonávania modelov
- Implementujte profilovanie výkonu pre AI operácie
- Ladenie asynchrónnych AI operácií s riadnym spracovaním výnimiek
- Používajte nástroje na profilovanie pamäte pre optimalizáciu

**Nástroje Windows AI Foundry**
- Využívajte Foundry Local CLI na testovanie a validáciu modelov
- Používajte nástroje na testovanie Windows AI API pre overenie integrácie
- Implementujte vlastné logovanie pre monitorovanie AI operácií
- Vytvorte automatizované testy pre spoľahlivosť AI funkcií

## Budúca pripravenosť vašich aplikácií

### Vznikajúce technológie

**Hardvér novej generácie**
- Navrhnite aplikácie na využitie budúcich NPU schopností
- Plánujte pre zväčšovanie veľkosti a komplexnosti modelov
- Implementujte adaptívne architektúry pre vývoj hardvéru
- Zvážte algoritmy pripravené na kvantové výpočty pre budúcu kompatibilitu

**Pokročilé AI schopnosti**
- Pripravte sa na multimodálnu AI integráciu pre viac typov dát
- Plánujte reálne časové spolupráce AI medzi viacerými zariadeniami
- Navrhnite pre federované učenie
- Zvážte hybridné architektúry edge-cloud inteligencie

### Kontinuálne učenie a adaptácia

**Aktualizácie modelov**
- Implementujte bezproblémové mechanizmy aktualizácie modelov
- Navrhnite aplikácie tak, aby sa prispôsobili vylepšeným schopnostiam modelov
- Plánujte spätnú kompatibilitu s existujúcimi modelmi
- Implementujte A/B testovanie pre hodnotenie výkonnosti modelov

**Evolúcia funkcií**
- Navrhnite modulárne architektúry, ktoré umožňujú nové AI schopnosti
- Plánujte integráciu vznikajúcich Windows AI API
- Implementujte feature flagy pre postupné zavádzanie schopností
- Navrhnite používateľské rozhrania, ktoré sa prispôsobujú vylepšeným AI funkciám

## Záver

Vývoj Windows Edge AI predstavuje konvergenciu výkonných AI schopností s robustnou, bezpečnou a škálovateľnou platformou Windows. Ovládnutím ekosystému Windows AI Foundry môžu vývojári vytvárať inteligentné aplikácie, ktoré poskytujú výnimočné používateľské zážitky pri zachovaní najvyšších štandardov ochrany súkromia, bezpečnosti a výkonu.

Kombinácia Windows AI API, Foundry Local a Windows ML poskytuje bezkonkurenčný základ pre budovanie ďalšej generácie inteligentných Windows aplikácií. Ako AI pokračuje vo vývoji, platforma Windows zabezpečuje, že vaše aplikácie budú rásť s novými technológiami pri zachovaní kompatibility a výkonu naprieč rozmanitým hardvérovým ekosystémom Windows.

Či už vytvárate spotrebiteľské aplikácie, podnikové riešenia alebo špecializované priemyselné nástroje, vývoj Windows Edge AI vám umožní vytvárať inteligentné, responzívne a hlboko integrované zážitky, ktoré využívajú plný potenciál moderných Windows zariadení.

## Ďalšie zdroje

### Dokumentácia a učenie
- [Windows AI Foundry dokumentácia](https://learn.microsoft.com/windows/ai/)
- [Referenčné Windows AI API](https://learn.microsoft.com/windows/ai/apis/)
- [Začnite vytvárať aplikáciu s Windows AI API](https://learn.microsoft.com/windows/ai/apis/model-setup)
- [Foundry Local Začíname](https://learn.microsoft.com/windows/ai/foundry-local/get-started/)
- [Prehľad Windows ML](https://learn.microsoft.com/windows/ai/new-windows-ml/overview/)
- [Požiadavky systému Windows App SDK](https://docs.microsoft.com/windows/apps/windows-app-sdk/system-requirements)

- [Nastavenie vývojového prostredia Windows App SDK](https://docs.microsoft.com/windows/apps/windows-app-sdk/set-up-your-development-environment)
- 

### Ukážkové úložiská a kód
- [Ukážky Windows App SDK - Windows AI Foundry](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsAIFoundry)
- [Ukážky Windows App SDK - Windows ML](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML)
- [Príklady inferencie ONNX Runtime](https://github.com/microsoft/onnxruntime-inference-examples)
- [Úložisko ukážok Windows App SDK](https://github.com/microsoft/WindowsAppSDK-Samples)

### Vývojové nástroje
- [AI Toolkit pre Visual Studio Code](https://learn.microsoft.com/windows/ai/toolkit/)
- [AI Dev Gallery](https://learn.microsoft.com/windows/ai/ai-dev-gallery/)
- [Ukážky Windows AI](https://learn.microsoft.com/windows/ai/samples/)
- [Nástroje na prevod modelov](https://code.visualstudio.com/docs/intelligentapps/modelconversion)

### Technická podpora
- [Dokumentácia Windows ML](https://learn.microsoft.com/windows/ai/new-windows-ml/overview)
- [Dokumentácia ONNX Runtime](https://onnxruntime.ai/docs/)
- [Dokumentácia Windows App SDK](https://docs.microsoft.com/windows/apps/windows-app-sdk/)
- [Nahlásiť problémy - Ukážky Windows App SDK](https://github.com/microsoft/WindowsAppSDK-Samples/issues)

### Komunita a podpora
- [Komunita vývojárov pre Windows](https://developer.microsoft.com/en-us/windows/)
- [Blog Windows AI Foundry](https://blogs.windows.com/windowsdeveloper/)
- [Vzdelávanie Microsoft Learn AI](https://learn.microsoft.com/training/browse/?products=windows&subjects=artificial-intelligence)

---

*Táto príručka je navrhnutá tak, aby sa vyvíjala spolu s rýchlo napredujúcim ekosystémom Windows AI. Pravidelné aktualizácie zabezpečujú súlad s najnovšími schopnosťami platformy a najlepšími vývojovými praktikami.*

[08. Praktická práca s Microsoft Foundry Local - Kompletný vývojársky nástrojový balík](../Module08/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
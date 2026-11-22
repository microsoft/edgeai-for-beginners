# Průvodce vývojem Windows Edge AI

## Úvod

Vítejte ve Windows Edge AI Development – vašem komplexním průvodci vytvářením inteligentních aplikací, které využívají sílu AI přímo na zařízení pomocí platformy Microsoft Windows AI Foundry. Tento průvodce je speciálně navržen pro vývojáře Windows, kteří chtějí integrovat špičkové Edge AI funkce do svých aplikací a zároveň využít plný rozsah hardwarové akcelerace Windows.

### Výhoda Windows AI

Windows AI Foundry představuje jednotnou, spolehlivou a zabezpečenou platformu podporující celý životní cyklus vývoje AI – od výběru a doladění modelu až po optimalizaci a nasazení přes CPU, GPU, NPU a hybridní cloudové architektury. Tato platforma demokratizuje vývoj AI tím, že poskytuje:

- **Abstrakce hardwaru**: Plynulé nasazení napříč křemíky AMD, Intel, NVIDIA a Qualcomm
- **Inteligence na zařízení**: AI chránící soukromí, která běží kompletně na lokálním hardwaru
- **Optimalizovaný výkon**: Modely předoptimalizované pro hardwarové konfigurace Windows
- **Připraveno pro podniky**: Produkčně robustní zabezpečení a funkce souladu

### Windows ML
Windows Machine Learning (ML) umožňuje vývojářům v C#, C++ a Pythonu spouštět ONNX AI modely lokálně na Windows PC prostřednictvím ONNX Runtime, s automatickou správou poskytovatelů vykonávání pro různý hardware (CPU, GPU, NPU). [ONNX Runtime](https://onnxruntime.ai/docs/) lze použít s modely z PyTorch, Tensorflow/Keras, TFLite, scikit-learn a dalších frameworků.


![WindowsML Schéma znázorňující ONNX model procházející Windows ML k dosažení NPUs, GPUs a CPUs.l](https://learn.microsoft.com/en-us/windows/ai/images/winml-diagram.png)

Windows ML poskytuje sdílenou celosystémovou kopii ONNX Runtime, plus možnost dynamicky stahovat poskytovatele vykonávání (EP).

### Proč Windows pro Edge AI?

**Univerzální podpora hardwaru**
Windows ML poskytuje automatickou optimalizaci hardwaru v celém Windows ekosystému, což zaručuje, že vaše AI aplikace podávají optimální výkon bez ohledu na základní architekturu křemíku.

**Integrované AI runtime**
Vestavěný inference engine Windows ML eliminuje složité požadavky na nastavení, takže se vývojáři mohou soustředit na logiku aplikací místo na infrastrukturu.

**Optimalizace Copilot+ PC**
Speciálně navržené API pro generaci Windows zařízení s dedikovanými Neural Processing Units (NPUs) přinášející výjimečný výkon na watt.

**Vývojářský ekosystém**
Bohaté nástroje včetně integrace do Visual Studia, obsáhlé dokumentace a ukázkových aplikací, které urychlují vývojové cykly.

## Cíle učení

Dokončením tohoto průvodce Windows Edge AI vývojem zvládnete zásadní dovednosti pro vytváření produkčně zralých AI aplikací na platformě Windows.

### Základní technické kompetence

**Ovládnutí Windows AI Foundry**
- Pochopit architekturu a komponenty platformy Windows AI Foundry
- Orientovat se v kompletním životním cyklu vývoje AI v rámci Windows ekosystému
- Implementovat bezpečnostní osvědčené postupy pro AI aplikace na zařízení
- Optimalizovat aplikace pro různé hardwarové konfigurace Windows

**Expertíza v API integraci**
- Ovládnout Windows AI API pro text, vizionářské a multimodální aplikace
- Implementovat integraci jazykového modelu Phi Silica pro generování textu a uvažování
- Nasadit schopnosti počítačového vidění pomocí vestavěných image processing API
- Přizpůsobit předtrénované modely pomocí technik LoRA (Low-Rank Adaptation)

**Implementace Foundry Local**
- Procházet, hodnotit a nasazovat open-source jazykové modely pomocí Foundry Local CLI
- Pochopit optimalizaci modelů a kvantizaci pro lokální nasazení
- Implementovat offline AI schopnosti fungující bez internetového připojení
- Spravovat životní cykly modelů a aktualizace v produkčním prostředí

**Nasazení Windows ML**
- Přinést vlastní ONNX modely do Windows aplikací pomocí Windows ML
- Využít automatickou hardwarovou akceleraci na CPU, GPU a NPU architekturách
- Implementovat inferenci v reálném čase s optimálním využitím zdrojů
- Navrhnout škálovatelné AI aplikace pro různé kategorie Windows zařízení

### Dovednosti vývoje aplikace

**Cross-platform vývoj pro Windows**
- Vytvářet AI aplikace pomocí .NET MAUI pro univerzální nasazení na Windows
- Integrovat AI funkce do Win32, UWP a Progressive Web Applications
- Implementovat responzivní UI designy přizpůsobující se stavům AI zpracování
- Řídit asynchronní AI operace s odpovídajícími vzory uživatelské zkušenosti

**Optimalizace výkonu**
- Profilovat a optimalizovat výkon inference AI na různých hardwarových konfiguracích
- Implementovat efektivní správu paměti pro velké jazykové modely
- Navrhnout aplikace, které se elegantně degradují podle dostupnosti hardwarových schopností
- Použít caching strategie pro často používané AI operace

**Produkční připravenost**
- Implementovat komplexní zpracování chyb a fallback mechanismy
- Navrhnout telemetrii a monitoring výkonu AI aplikací
- Aplikovat bezpečnostní osvědčené postupy pro lokální ukládání a spuštění AI modelů
- Plánovat strategie nasazení pro podnikové i zákaznické aplikace

### Obchodní a strategické porozumění

**Architektura AI aplikací**
- Navrhovat hybridní architektury optimalizující mezi lokálním a cloudovým AI zpracováním
- Vyhodnocovat kompromisy mezi velikostí modelu, přesností a rychlostí inference
- Plánovat datové toky zachovávající soukromí a současně umožňující inteligenci
- Implementovat nákladově efektivní AI řešení, která škálují s poptávkou uživatelů

**Pozicování na trhu**
- Porozumět konkurenčním výhodám nativních Windows AI aplikací
- Identifikovat případy využití, kde AI na zařízení poskytuje lepší uživatelskou zkušenost
- Vyvíjet strategie go-to-market pro AI vylepšené Windows aplikace
- Pozicovat aplikace tak, aby využívaly výhody Windows ekosystému

## Ukázky Windows App SDK AI

Windows App SDK poskytuje komplexní ukázky demonstrující AI integraci napříč mnoha frameworky a scénáři nasazení. Tyto ukázky jsou nezbytnými referencemi pro pochopení vzorů vývoje Windows AI.

### Windows AI Foundry ukázky

| Ukázka | Framework | Oblast zaměření | Klíčové vlastnosti |
|--------|-----------|-----------------|-------------------|
| [cs-winui](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsAIFoundry/cs-winui) | C# WinUI 3 | Integrace Windows AI API | Kompletní WinUI aplikace demonstrující Windows AI API, optimalizace pro ARM64, balené nasazení |

**Klíčové technologie:**
- Windows AI API
- Framework WinUI 3
- Optimalizace platformy ARM64
- Kompatibilita s Copilot+ PC
- Balené nasazení aplikace

**Požadavky:**
- Doporučený Windows 11 s Copilot+ PC
- Visual Studio 2022
- Konfigurace buildu ARM64
- Windows App SDK 1.8.1+

### Windows ML ukázky

#### C++ ukázky

| Ukázka | Typ | Oblast zaměření | Klíčové vlastnosti |
|--------|------|-----------------|-------------------|
| [CppConsoleDesktop](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Konzolová aplikace | Základní Windows ML | Objevování EP, příkazová řádka, kompilace modelu |
| [CppConsoleDesktop.FrameworkDependent](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Konzolová aplikace | Framework nasazení | Sdílené runtime, menší footprint nasazení |
| [CppConsoleDesktop.SelfContained](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Konzolová aplikace | Samostatné nasazení | Samostatné nasazení, bez runtime závislostí |
| [CppConsoleDll](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | DLL | Použití knihovny | WindowsML v sdílené knihovně, správa paměti |
| [CppResnetBuildDemo](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Demo | ResNet tutoriál | Konverze modelu, kompilace EP, Build 2025 tutoriál |

#### C# ukázky

**Konzolové aplikace**

| Ukázka | Typ | Oblast zaměření | Klíčové vlastnosti |
|--------|------|-----------------|-------------------|
| [CSharpConsoleDesktop](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs) | Konzolová aplikace | Základní C# integrace | Použití sdílených helperů, příkazové rozhraní |
| [ResnetBuildDemoCS](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs) | Demo | ResNet tutoriál | Konverze modelu, kompilace EP, Build 2025 tutoriál |

**GUI aplikace**

| Ukázka | Framework | Oblast zaměření | Klíčové vlastnosti |
|--------|-----------|-----------------|-------------------|
| [cs-wpf](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs-wpf) | WPF | Desktop GUI | Klasifikace obrázků s WPF rozhraním |
| [cs-winforms](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs-winforms) | Windows Forms | Tradiční GUI | Klasifikace obrázků s Windows Forms |
| [cs-winui](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs-winui) | WinUI 3 | Moderní GUI | Klasifikace obrázků s WinUI 3 rozhraním |

#### Python ukázky

| Ukázka | Jazyk | Oblast zaměření | Klíčové vlastnosti |
|--------|-------|-----------------|-------------------|
| [SqueezeNetPython](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/python) | Python | Klasifikace obrázků | WinML Python vazby, dávkové zpracování obrázků |

### Požadavky na ukázky

**Systémové požadavky:**
- Windows 11 PC s verzí 24H2 (build 26100) nebo novější
- Visual Studio 2022 s workloady pro C++ a .NET
- Windows App SDK 1.8.1 nebo novější
- Python 3.10-3.13 pro Python ukázky na x64 a ARM64 zařízeních

**Specifické pro Windows AI Foundry:**
- Doporučený Copilot+ PC pro optimální výkon
- Konfigurace buildu ARM64 pro Windows AI ukázky
- Vyžadována identita balíčku (unpackaged aplikace již nejsou podporovány)

### Běžný postup u ukázek

Většina Windows ML ukázek následuje tento standardní vzor:

1. **Inicializace prostředí** - Vytvoření ONNX Runtime prostředí
2. **Registrace poskytovatelů vykonávání** - Objevení a registrace dostupných hardwarových akcelerátorů (CPU, GPU, NPU)
3. **Načtení modelu** - Načtení ONNX modelu, případně kompilace pro cílový hardware
4. **Předzpracování vstupu** - Převedení obrázků/dat do formátu vstupu modelu
5. **Spuštění inference** - Provedení modelu a získání predikcí
6. **Zpracování výsledků** - Aplikace softmax a zobrazení nejlepších predikcí

### Používané soubory modelů

| Model | Účel | Součástí | Poznámky |
|-------|-------|----------|----------|
| SqueezeNet | Lehká klasifikace obrázků | ✅ Součástí | Předtrénovaný, připraven k použití |
| ResNet-50 | Vysoce přesná klasifikace obrázků | ❌ Vyžaduje konverzi | Použijte [AI Toolkit](https://code.visualstudio.com/docs/intelligentapps/modelconversion) pro konverzi |

### Podpora hardwaru

Všechny ukázky automaticky detekují a využívají dostupný hardware:
- **CPU** - Univerzální podpora na všech Windows zařízeních
- **GPU** - Automatická detekce a optimalizace pro dostupný grafický hardware
- **NPU** - Využití Neural Processing Units na podporovaných zařízeních (Copilot+ PC)

## Komponenty platformy Windows AI Foundry

### 1. Windows AI API

Windows AI API poskytují připravené AI funkce poháněné modely na zařízení, optimalizované pro efektivitu a výkon na Copilot+ PC zařízeních s minimálním požadavkem na nastavení.

#### Hlavní kategorie API

**Jazykový model Phi Silica**
- Malý, ale výkonný jazykový model pro generování textu a uvažování
- Optimalizovaný pro real-time inferenci s minimální spotřebou energie
- Podpora vlastního doladění pomocí technik LoRA
- Integrace s Windows sémantickým vyhledáváním a získáváním znalostí

**API počítačového vidění**
- **Rozpoznávání textu (OCR)**: Extrakce textu z obrázků s vysokou přesností
- **Image Super Resolution**: Zvětšování obrázků pomocí lokálních AI modelů
- **Segmentace obrázků**: Identifikace a izolace specifických objektů na obrázcích
- **Popis obrázků**: Generování detailních textových popisů vizuálního obsahu
- **Odstranění objektů**: Odstranění nežádoucích objektů z obrázků pomocí AI vyplňování (inpainting)

**Multimodální schopnosti**
- **Integrace textu a obrazu**: Kombinace porozumění textu a obrazů
- **Sémantické vyhledávání**: Umožnění dotazů v přirozeném jazyce napříč multimediálním obsahem
- **Získávání znalostí**: Vytvoření inteligentních vyhledávacích zážitků s lokálními daty

### 2. Foundry Local

Foundry Local poskytuje vývojářům rychlý přístup k připraveným open-source jazykovým modelům na Windows Silicon, nabízí možnost procházet, testovat, interagovat a nasazovat modely v lokálních aplikacích.

#### Ukázkové aplikace Foundry Local

[Foundry Local repozitář](https://github.com/microsoft/Foundry-Local/tree/main/samples) nabízí rozsáhlé ukázky v různých programovacích jazycích a frameworcích, které demonstrují různé integrační vzory a scénáře použití.

| Ukázka | Jazyk/Framework | Oblast zaměření | Klíčové vlastnosti |
|--------|-----------------|-----------------|-------------------|
| [dotNET/rag](https://github.com/microsoft/Foundry-Local/tree/main/samples/dotNET/rag) | C# / .NET | Implementace RAG | Integrace Semantic Kernel, Qdrant vektorové úložiště, JINA embeddingy, ingest dokumentů, streamovaný chat |
| [electron/foundry-chat](https://github.com/microsoft/Foundry-Local/tree/main/samples/electron/foundry-chat) | JavaScript / Electron | Desktopová chat aplikace | Cross-platform chat, přepínání lokální/ cloud modely, integrace OpenAI SDK, realtime streaming |
| [js/hello-foundry-local](https://github.com/microsoft/Foundry-Local/tree/main/samples/js/hello-foundry-local) | JavaScript / Node.js | Základní integrace | Jednoduché SDK použití, inicializace modelu, základní chat funkce |
| [python/hello-foundry-local](https://github.com/microsoft/Foundry-Local/tree/main/samples/python/hello-foundry-local) | Python | Základní integrace | Použití Python SDK, streamované odpovědi, API kompatibilní s OpenAI |

| [rust/hello-foundry-local](https://github.com/microsoft/Foundry-Local/tree/main/samples/rust/hello-foundry-local) | Rust | Integrace systémů | Použití nízkoúrovňového SDK, asynchronní operace, HTTP klient reqwest |

#### Kategorie ukázek podle použití

**RAG (Retrieval-Augmented Generation)**
- **dotNET/rag**: Kompletní implementace RAG pomocí Semantic Kernel, vektorové databáze Qdrant a JINA embedování
- **Architektura**: Zpracování dokumentu → Rozdělení textu → Vektorová embedování → Vyhledávání podobností → Odpovědi založené na kontextu
- **Technologie**: Microsoft.SemanticKernel, Qdrant.Client, BERT ONNX embedování, průběžné dokončování chatu

**Desktopové aplikace**
- **electron/foundry-chat**: Produkční chatovací aplikace s přepínáním mezi lokálním a cloudovým modelem
- **Funkce**: Výběr modelu, průběžné odpovědi, zpracování chyb, multiplatformní nasazení
- **Architektura**: Hlavní proces Electron, komunikace IPC, zabezpečené preload skripty

**Příklady integrace SDK**
- **JavaScript (Node.js)**: Základní interakce s modelem a průběžné odpovědi
- **Python**: API kompatibilní s OpenAI s asynchronním streamováním
- **Rust**: Nízkourovňová integrace s reqwest a tokio pro asynchronní operace

#### Požadavky pro ukázky Foundry Local

**Systémové požadavky:**
- Windows 11 s nainstalovaným Foundry Local
- Node.js verze 16+ pro ukázky JavaScript/Electron
- .NET 8.0+ pro ukázky v C#
- Python 3.10+ pro ukázky v Pythonu
- Rust 1.70+ pro ukázky v Rustu

**Instalace:**
```powershell
# Nainstalujte Foundry Local
winget install Microsoft.FoundryLocal

# Ověřte instalaci
foundry --version
foundry model list
```

#### Specifické nastavení ukázek

**Ukázka dotNET RAG:**
```powershell
# Nainstalujte požadované balíčky přes NuGet
# Microsoft.SemanticKernel.Connectors.Onnx
# Microsoft.SemanticKernel.Connectors.Qdrant
# Qdrant.Client

# Spusťte vektorovou databázi Qdrant
docker run -p 6333:6333 qdrant/qdrant

# Spusťte Jupyter notebook
jupyter notebook rag_foundrylocal_demo.ipynb
```

**Ukázka Electron Chat:**
```powershell
# Nastavte proměnné prostředí pro cloudový záložní plán
$env:YOUR_API_KEY="your-cloud-api-key"
$env:YOUR_ENDPOINT="your-cloud-endpoint"
$env:YOUR_MODEL_NAME="your-cloud-model"

# Nainstalujte závislosti a spusťte
npm install
npm start
```

**Ukázky JavaScript/Python/Rust:**
```powershell
# Stáhnout model (příklad s phi-3.5-mini)
foundry model run phi-3.5-mini

# Spustit příslušný příklad
node src/app.js          # JavaScript
python src/app.py        # Python
cargo run               # Rust
```

#### Klíčové vlastnosti

**Katalog modelů**
- Komplexní sbírka předoptimalizovaných open-source modelů
- Modely optimalizované pro CPU, GPU a NPU pro okamžité nasazení
- Podpora populárních rodin modelů včetně Llama, Mistral, Phi a specializovaných doménových modelů

**Integrace CLI**
- Rozhraní příkazové řádky pro správu a nasazení modelů
- Automatizované workflow optimalizace a kvantizace
- Integrace s populárními vývojovými prostředími a CI/CD pipeline

**Lokální nasazení**
- Kompletní offline provoz bez závislosti na cloudu
- Podpora vlastních formátů a konfigurací modelů
- Efektivní servírování modelů s automatickou optimalizací pro hardware

### 3. Windows ML

Windows ML slouží jako hlavní platforma AI a integrované běhové prostředí inferencí ve Windows, umožňující vývojářům efektivně nasazovat vlastní modely napříč širokým ekosystémem hardwaru Windows.

#### Výhody architektury

**Univerzální podpora hardwaru**
- Automatická optimalizace pro čipy AMD, Intel, NVIDIA a Qualcomm
- Podpora CPU, GPU a NPU s transparentním přepínáním
- Abstrakce hardwaru, která eliminuje práci na optimalizaci specifickou pro platformu

**Flexibilita modelů**
- Podpora formátu modelů ONNX s automatickou konverzí z populárních rámců
- Nasazení vlastních modelů s produkční výkonností
- Integrace do existujících architektur aplikací Windows

**Podniková integrace**
- Kompatibilní s bezpečnostními a compliance rámci Windows
- Podpora nástrojů pro nasazení a správu v podniku
- Integrace se systémy správy a monitoringu zařízení Windows

## Vývojový pracovní postup

### Fáze 1: Nastavení prostředí a konfigurace nástrojů

**Příprava vývojového prostředí**
1. Nainstalujte Visual Studio 2022 s workloady pro C++ a .NET
2. Nainstalujte Windows App SDK verze 1.8.1 nebo novější
3. Nakonfigurujte nástroje Windows AI Foundry CLI
4. Nastavte rozšíření AI Toolkit pro Visual Studio Code
5. Zajistěte nástroje pro profilování výkonu a monitoring
6. Ujistěte se o konfiguraci sestavení ARM64 pro optimalizaci Copilot+ PC

**Nastavení repozitáře ukázek**
1. Klonujte [Windows App SDK Samples repository](https://github.com/microsoft/WindowsAppSDK-Samples)
2. Přejděte do `Samples/WindowsAIFoundry/cs-winui` pro příklady Windows AI API
3. Přejděte do `Samples/WindowsML` pro komplexní příklady Windows ML
4. Prohlédněte si [požadavky na sestavení](https://learn.microsoft.com/windows/apps/windows-app-sdk/system-requirements) pro cílové platformy

**Průzkum AI Dev Gallery**
- Prozkoumejte ukázkové aplikace a referenční implementace
- Testujte Windows AI API pomocí interaktivních demonstrací
- Prohlédněte si zdrojový kód nejlepší praxe a vzory
- Identifikujte relevantní ukázky pro váš konkrétní případ použití

### Fáze 2: Výběr modelu a integrace

**Analýza požadavků**
- Definujte funkční požadavky na AI schopnosti
- Stanovte výkonnostní omezení a cíle optimalizace
- Vyhodnoťte požadavky na soukromí a bezpečnost
- Naplánujte architekturu nasazení a strategii škálování

**Hodnocení modelů**
- Použijte Foundry Local k testování open-source modelů pro váš případ použití
- Benchmarkujte Windows AI API proti požadavkům vlastních modelů
- Vyhodnoťte kompromisy mezi velikostí modelu, přesností a rychlostí inferenčního zpracování
- Prototypujte integrační přístupy s vybranými modely

### Fáze 3: Vývoj aplikace

**Jádrová integrace**
- Implementujte integraci Windows AI API s vhodným zpracováním chyb
- Navrhněte uživatelská rozhraní podporující pracovní postupy AI zpracování
- Implementujte strategie cache a optimalizace pro inferenci modelu
- Přidejte telemetry a monitoring výkonnosti AI operací

**Testování a ověřování**
- Testujte aplikace na různých hardwarových konfiguracích Windows
- Ověřte metriky výkonnosti při různých zátěžích
- Implementujte automatizované testy spolehlivosti AI funkcí
- Proveďte testování uživatelské zkušenosti s funkcemi AI

### Fáze 4: Optimalizace a nasazení

**Optimalizace výkonu**
- Profilujte výkon aplikace na cílových hardwarových konfiguracích
- Optimalizujte využití paměti a strategie načítání modelů
- Implementujte adaptivní chování na základě dostupných hardwarových schopností
- Dolaďte uživatelský zážitek podle různých scénářů výkonu

**Produkční nasazení**
- Balíčkujte aplikace se správnými závislostmi AI modelů
- Implementujte mechanismy aktualizací modelů a aplikační logiky
- Nakonfigurujte monitoring a analytiku pro produkční prostředí
- Naplánujte strategie zavádění pro podniková i spotřebitelská nasazení

## Praktické příklady implementace

### Příklad 1: Aplikace pro inteligentní zpracování dokumentů

Vytvořte Windows aplikaci, která zpracovává dokumenty využitím více AI schopností:

**Použité technologie:**
- Phi Silica pro shrnutí dokumentů a odpovídání na otázky
- OCR API pro extrakci textu ze skenovaných dokumentů
- API pro popis obrázků pro analýzu grafů a diagramů
- Vlastní ONNX modely pro klasifikaci dokumentů

**Přístup k implementaci:**
- Navrhněte modulární architekturu s vyměnitelnými AI komponentami
- Implementujte asynchronní zpracování velkých dávek dokumentů
- Přidejte indikátory průběhu a podporu rušení dlouhotrvajících operací
- Zahrňte offline schopnost pro zpracování citlivých dokumentů

### Příklad 2: Systém správy skladových zásob v maloobchodě

Vytvořte AI řízený inventární systém pro maloobchodní aplikace:

**Použité technologie:**
- Segmentace obrazů pro identifikaci produktů
- Vlastní vizuální modely pro klasifikaci značek a kategorií
- Nasazení Foundry Local specializovaných jazykových modelů pro maloobchod
- Integrace se stávajícími POS a skladovými systémy

**Přístup k implementaci:**
- Vytvořte integraci kamery pro skenování produktů v reálném čase
- Implementujte rozpoznávání produktů pomocí čárových kódů a vizuálu
- Přidejte dotazy na inventář v přirozeném jazyce použitím lokálních jazykových modelů
- Navrhněte škálovatelnou architekturu pro nasazení ve více prodejnách

### Příklad 3: Asistent pro zdravotnickou dokumentaci

Vyviněte nástroj na ochranu soukromí pro zdravotnickou dokumentaci:

**Použité technologie:**
- Phi Silica pro generování lékařských poznámek a klinickou podporu rozhodování
- OCR pro digitalizaci ručně psaných zdravotních záznamů
- Vlastní lékařské jazykové modely nasazené přes Windows ML
- Lokální vektorové úložiště pro získávání lékařských znalostí

**Přístup k implementaci:**
- Zajistěte kompletní offline provoz pro ochranu soukromí pacientů
- Implementujte ověřování a návrhy lékařské terminologie
- Přidejte auditní záznamy pro splnění regulačních požadavků
- Navrhněte integraci se stávajícími systémy elektronických zdravotních záznamů

## Strategie optimalizace výkonu

### Vývoj s ohledem na hardware

**Optimalizace NPU**
- Navrhněte aplikace tak, aby využívaly schopnosti NPU na počítačích Copilot+
- Implementujte plynulé přepnutí na GPU/CPU na zařízeních bez NPU
- Optimalizujte formáty modelů pro akceleraci specifickou pro NPU
- Sledujte využití NPU a jeho tepelné charakteristiky

**Správa paměti**
- Implementujte efektivní načítání modelů a strategie cacheování
- Používejte mapování paměti pro velké modely ke zkrácení doby spuštění
- Navrhujte aplikace méně náročné na paměť pro zařízení s omezenými zdroji
- Implementujte kvantizaci modelů pro optimalizaci paměti

**Efektivita baterie**
- Optimalizujte AI operace pro minimální spotřebu energie
- Implementujte adaptivní zpracování na základě stavu baterie
- Navrhujte efektivní zpracování na pozadí pro kontinuální AI operace
- Používejte nástroje pro profilování spotřeby energie k optimalizaci využití

### Zvážení škálovatelnosti

**Vícevláknovost**
- Navrhujte AI operace bezpečné pro více vláken pro souběžné zpracování
- Implementujte efektivní rozložení práce na dostupná jádra
- Používejte async/await vzory pro neblokující AI operace
- Plánujte optimalizaci vláknových poolů pro různé hardwarové konfigurace

**Strategie kešování**
- Implementujte inteligentní kešování často používaných AI operací
- Navrhujte strategie invalidace cache při aktualizacích modelů
- Používejte perzistentní cache pro nákladné předzpracování
- Implementujte distribuované kešování pro multiuživatelské scénáře

## Best practices zabezpečení a ochrany soukromí

### Ochrana dat

**Lokální zpracování**
- Zajistěte, aby citlivá data nikdy neopustila lokální zařízení
- Implementujte bezpečné ukládání AI modelů a dočasných dat
- Využívejte bezpečnostní funkce Windows pro sandboxing aplikací
- Používejte šifrování pro uložené modely a mezivýsledky zpracování

**Zabezpečení modelů**
- Ověřujte integritu modelů před jejich načtením a spuštěním
- Implementujte bezpečné mechanismy aktualizace modelů
- Používejte podepsané modely pro ochranu proti manipulaci
- Aplikujte přístupové kontroly na modelové soubory a konfigurace

### Požadavky na soulady

**Soulad s legislativou**
- Navrhujte aplikace tak, aby splňovaly GDPR, HIPAA a další regulační požadavky
- Implementujte auditní záznamy rozhodovacích procesů AI
- Poskytujte funkce transparentnosti výsledků generovaných AI
- Umožněte uživateli kontrolu nad zpracováním dat AI

**Podnikové zabezpečení**
- Integrujte se zásadami zabezpečení podniku ve Windows
- Podporujte spravované nasazení skrze podnikové nástroje pro správu
- Implementujte řízení přístupu založené na rolích pro AI funkce
- Poskytujte administrátorské ovládací prvky pro AI funkčnost

## Řešení problémů a ladění

### Běžné vývojové problémy

**Problémy s konfigurací sestavení**
- Zajistěte konfiguraci platformy ARM64 pro příklady Windows AI API
- Ověřte kompatibilitu verze Windows App SDK (vyžadováno 1.8.1+)
- Zkontrolujte správnou konfiguraci identity balíčku (nutné pro Windows AI API)
- Validujte podporu build nástrojů pro cílovou verzi frameworku

**Problémy s načítáním modelu**
- Validujte kompatibilitu ONNX modelů s Windows ML
- Kontrolujte integritu modelového souboru a požadavky formátu
- Ověřte požadavky na hardwarové schopnosti specifických modelů
- Ladění problémů s alokací paměti při načítání modelu
- Zajistěte registraci výkonného prostředí pro hardwarovou akceleraci

**Zvažování režimu nasazení**
- **Režim „Self-Contained“**: Plně podporovaný s větší velikostí nasazení
- **Režim závislý na frameworku**: Menší stopa, ale vyžaduje sdílený runtime
- **Nepakované aplikace**: Už nejsou podporovány pro Windows AI API
- Použijte `dotnet run -p:Platform=ARM64 -p:SelfContained=true` pro self-contained ARM64 nasazení

**Problémy s výkonem**
- Profilujte výkon aplikace na různých hardwarových konfiguracích
- Identifikujte úzká hrdla v AI zpracovatelských pipelinech
- Optimalizujte operace předzpracování a následného zpracování dat
- Implementujte monitoring výkonu a upozornění

**Obtíže s integrací**
- Ladění problémů s integrací API s vhodným zpracováním chyb
- Validujte vstupní datové formáty a požadavky na předzpracování
- Důkladně testujte okrajové případy a chybové situace
- Implementujte komplexní logování pro ladění produkčních problémů

### Nástroje a techniky ladění

**Integrace Visual Studio**
- Používejte ladicí nástroje AI Toolkit pro analýzu vykonávání modelů
- Implementujte profilování výkonu AI operací
- Ladění asynchronních AI operací se správným zpracováním výjimek
- Používejte nástroje pro profilování paměti pro optimalizaci

**Nástroje Windows AI Foundry**
- Využívejte Foundry Local CLI pro testování a validaci modelů
- Používejte nástroje Windows AI API pro ověřování integrace
- Implementujte vlastní logování pro monitoring AI operací
- Vytvořte automatizované testy spolehlivosti AI funkcí

## Budoucí zajištění vašich aplikací

### Nově vznikající technologie

**Hardware nové generace**
- Navrhujte aplikace pro využití budoucích schopností NPU
- Plánujte pro rostoucí velikosti a složitost modelů
- Implementujte adaptivní architektury pro vývoj hardwaru
- Zvažujte algoritmy připravené na kvantové výpočty pro budoucí kompatibilitu

**Pokročilé AI schopnosti**
- Připravte se na multimodální AI integraci přes více typů dat
- Plánujte reálný čas pro kolaborativní AI mezi více zařízeními
- Navrhujte pro federované učení
- Zvažujte hybridní architektury edge-cloud inteligence

### Neustálé učení a adaptace

**Aktualizace modelů**
- Implementujte plynulé mechanismy aktualizace modelů
- Navrhujte aplikace pro adaptaci na zlepšené schopnosti modelů
- Plánujte zpětnou kompatibilitu s existujícími modely
- Implementujte A/B testování pro hodnocení výkonu modelů

**Vývoj funkcí**
- Navrhujte modulární architektury, které umožní nové AI schopnosti
- Plánujte integraci nově vznikajících Windows AI API
- Implementujte feature flagy pro postupné zavádění schopností
- Navrhujte uživatelská rozhraní adaptující se na vylepšené AI funkce

## Závěr

Vývoj Windows Edge AI představuje spojení silných AI schopností s robustní, bezpečnou a škálovatelnou platformou Windows. Ovládnutím ekosystému Windows AI Foundry mohou vývojáři vytvářet inteligentní aplikace, které poskytují výjimečné uživatelské zážitky a zároveň dodržují nejvyšší standardy ochrany soukromí, bezpečnosti a výkonu.

Kombinace Windows AI API, Foundry Local a Windows ML poskytuje bezkonkurenční základ pro vytváření další generace inteligentních Windows aplikací. S pokračujícím vývojem AI Windows platforma zajišťuje, že vaše aplikace porostou s novými technologiemi a zároveň si udrží kompatibilitu a výkon napříč rozmanitým ekosystémem hardwaru Windows.

Ať už vytváříte spotřebitelské aplikace, podniková řešení nebo specializované průmyslové nástroje, vývoj Windows Edge AI vám umožní vytvářet inteligentní, responsivní a hluboce integrované zážitky, které využívají plný potenciál moderních zařízení Windows.

## Další zdroje

### Dokumentace a vzdělávání
- [Windows AI Foundry Documentation](https://learn.microsoft.com/windows/ai/)
- [Windows AI APIs Reference](https://learn.microsoft.com/windows/ai/apis/)
- [Začínáme s tvorbou aplikací pomocí Windows AI API](https://learn.microsoft.com/windows/ai/apis/model-setup)
- [Foundry Local Getting Started](https://learn.microsoft.com/windows/ai/foundry-local/get-started/)
- [Přehled Windows ML](https://learn.microsoft.com/windows/ai/new-windows-ml/overview/)
- [Požadavky systému Windows App SDK](https://docs.microsoft.com/windows/apps/windows-app-sdk/system-requirements)

- [Nastavení vývojového prostředí Windows App SDK](https://docs.microsoft.com/windows/apps/windows-app-sdk/set-up-your-development-environment)
- 

### Ukázkové repozitáře a kód
- [Ukázky Windows App SDK - Windows AI Foundry](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsAIFoundry)
- [Ukázky Windows App SDK - Windows ML](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML)
- [Příklady inference ONNX Runtime](https://github.com/microsoft/onnxruntime-inference-examples)
- [Repozitář ukázek Windows App SDK](https://github.com/microsoft/WindowsAppSDK-Samples)

### Vývojové nástroje
- [AI Toolkit pro Visual Studio Code](https://learn.microsoft.com/windows/ai/toolkit/)
- [AI Dev Gallery](https://learn.microsoft.com/windows/ai/ai-dev-gallery/)
- [Windows AI Ukázky](https://learn.microsoft.com/windows/ai/samples/)
- [Nástroje pro konverzi modelů](https://code.visualstudio.com/docs/intelligentapps/modelconversion)

### Technická podpora
- [Dokumentace Windows ML](https://learn.microsoft.com/windows/ai/new-windows-ml/overview)
- [Dokumentace ONNX Runtime](https://onnxruntime.ai/docs/)
- [Dokumentace Windows App SDK](https://docs.microsoft.com/windows/apps/windows-app-sdk/)
- [Nahlásit problémy - Ukázky Windows App SDK](https://github.com/microsoft/WindowsAppSDK-Samples/issues)

### Komunita a podpora
- [Komunita vývojářů Windows](https://developer.microsoft.com/en-us/windows/)
- [Windows AI Foundry Blog](https://blogs.windows.com/windowsdeveloper/)
- [Microsoft Learn AI školení](https://learn.microsoft.com/training/browse/?products=windows&subjects=artificial-intelligence)

---

*Tento průvodce je navržen tak, aby se vyvíjel spolu s rychle se rozvíjejícím ekosystémem Windows AI. Pravidelné aktualizace zajišťují shodu s nejnovějšími schopnostmi platformy a osvědčenými postupy vývoje.*

[08. Praktická práce s Microsoft Foundry Local - Kompletní nástroje pro vývojáře](../Module08/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o omezení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o co největší přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné interpretace vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
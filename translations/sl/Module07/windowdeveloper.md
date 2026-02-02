# Vodnik za razvoj Windows Edge AI

## Uvod

Dobrodošli v Windows Edge AI razvoju – vašem celovitem vodniku za gradnjo inteligentnih aplikacij, ki izkoriščajo moč umetne inteligence na napravi z uporabo Microsoftove platforme Windows AI Foundry. Ta vodnik je posebej zasnovan za razvijalce Windows, ki želijo v svoje aplikacije vključiti najsodobnejše zmogljivosti Edge AI in hkrati izkoristiti celoten spekter strojne pospešitve Windows.

### Prednosti Windows AI

Windows AI Foundry predstavlja enotno, zanesljivo in varno platformo, ki podpira celoten življenjski cikel razvoja umetne inteligence – od izbire in prilagajanja modelov do optimizacije in uvajanja na CPU, GPU, NPU ter hibridne oblačne arhitekture. Ta platforma demokratizira razvoj umetne inteligence z zagotavljanjem:

- **Abstrakcije strojne opreme**: Brezhibno uvajanje na AMD, Intel, NVIDIA in Qualcomm čipe
- **Inteligence na napravi**: AI, ki ohranja zasebnost in deluje izključno na lokalni strojni opremi
- **Optimizirane zmogljivosti**: Modeli, predhodno optimizirani za konfiguracije strojne opreme Windows
- **Pripravljenost za podjetja**: Varnostne in skladnostne funkcije na ravni produkcije

### Windows ML
Windows Machine Learning (ML) omogoča razvijalcem v C#, C++ in Pythonu izvajanje ONNX AI modelov lokalno na Windows računalnikih prek ONNX Runtime, z avtomatskim upravljanjem izvajalnih ponudnikov za različne strojne opreme (CPU, GPU, NPU). [ONNX Runtime](https://onnxruntime.ai/docs/) je združljiv z modeli iz PyTorch, Tensorflow/Keras, TFLite, scikit-learn in drugih ogrodij.

![WindowsML Diagram, ki prikazuje ONNX model, ki gre skozi Windows ML in doseže NPU, GPU ter CPU.](https://learn.microsoft.com/en-us/windows/ai/images/winml-diagram.png)

Windows ML zagotavlja deljeno kopijo ONNX Runtime za celoten Windows, poleg tega pa omogoča dinamično prenašanje izvajalnih ponudnikov (EP).

### Zakaj Windows za Edge AI?

**Univerzalna podpora strojne opreme**
Windows ML zagotavlja avtomatsko optimizacijo strojne opreme po celotnem ekosistemu Windows, kar omogoča, da vaše AI aplikacije delujejo optimalno ne glede na osnovno arhitekturo čipov.

**Integriran AI Runtime**
Vgrajeni Windows ML inferenčni motor odpravlja zapletene zahteve za nastavitev, kar razvijalcem omogoča, da se osredotočijo na logiko aplikacije namesto na infrastrukturne skrbi.

**Optimizacija za Copilot+ PC**
Posebej zasnovani API-ji za naslednjo generacijo Windows naprav z namensko nevronsko procesno enoto (NPU), ki zagotavlja izjemno zmogljivost na vat.

**Razvijalski ekosistem**
Bogata orodja, vključno z integracijo Visual Studio, obsežno dokumentacijo in vzorčnimi aplikacijami, ki pospešujejo razvojne cikle.

## Cilji učenja

Z dokončanjem tega vodnika za razvoj Windows Edge AI boste obvladali ključne veščine za gradnjo produkcijsko pripravljenih AI aplikacij na platformi Windows.

### Osnovne tehnične kompetence

**Obvladovanje Windows AI Foundry**
- Razumevanje arhitekture in komponent platforme Windows AI Foundry
- Navigacija skozi celoten življenjski cikel razvoja AI znotraj ekosistema Windows
- Uvajanje najboljših varnostnih praks za aplikacije AI na napravi
- Optimizacija aplikacij za različne konfiguracije strojne opreme Windows

**Strokovno znanje o integraciji API-jev**
- Obvladovanje Windows AI API-jev za besedilo, vizijo in multimodalne aplikacije
- Uvajanje integracije jezikovnega modela Phi Silica za generiranje besedila in razmišljanje
- Uvajanje zmogljivosti računalniškega vida z uporabo vgrajenih API-jev za obdelavo slik
- Prilagajanje predhodno usposobljenih modelov z uporabo tehnik LoRA (Low-Rank Adaptation)

**Lokalna implementacija Foundry**
- Brskanje, ocenjevanje in uvajanje odprtokodnih jezikovnih modelov z uporabo Foundry Local CLI
- Razumevanje optimizacije modelov in kvantizacije za lokalno uvajanje
- Uvajanje offline AI zmogljivosti, ki delujejo brez internetne povezave
- Upravljanje življenjskega cikla modelov in posodobitev v produkcijskih okoljih

**Uvajanje Windows ML**
- Uvajanje prilagojenih ONNX modelov v Windows aplikacije z uporabo Windows ML
- Izkoristite avtomatsko strojno pospeševanje na CPU, GPU in NPU arhitekturah
- Uvajanje realnočasovne inferenčne zmogljivosti z optimalno uporabo virov
- Oblikovanje skalabilnih AI aplikacij za različne kategorije naprav Windows

### Veščine razvoja aplikacij

**Razvoj Windows aplikacij na več platformah**
- Gradnja aplikacij z AI z uporabo .NET MAUI za univerzalno uvajanje na Windows
- Integracija AI zmogljivosti v Win32, UWP in progresivne spletne aplikacije
- Uvajanje odzivnih UI dizajnov, ki se prilagajajo stanjem AI obdelave
- Upravljanje asinhronih AI operacij z ustreznimi vzorci uporabniške izkušnje

**Optimizacija zmogljivosti**
- Profiliranje in optimizacija zmogljivosti AI inferenčne obdelave na različnih konfiguracijah strojne opreme
- Uvajanje učinkovitega upravljanja pomnilnika za velike jezikovne modele
- Oblikovanje aplikacij, ki se prilagodljivo odzivajo glede na razpoložljive zmogljivosti strojne opreme
- Uporaba strategij predpomnjenja za pogosto uporabljene AI operacije

**Pripravljenost za produkcijo**
- Uvajanje celovitega upravljanja napak in mehanizmov za povratne ukrepe
- Oblikovanje telemetrije in spremljanja zmogljivosti AI aplikacij
- Uvajanje najboljših varnostnih praks za lokalno shranjevanje in izvajanje AI modelov
- Načrtovanje strategij uvajanja za podjetniške in potrošniške aplikacije

### Poslovno in strateško razumevanje

**Arhitektura AI aplikacij**
- Oblikovanje hibridnih arhitektur, ki optimizirajo med lokalno in oblačno AI obdelavo
- Ocenjevanje kompromisov med velikostjo modela, natančnostjo in hitrostjo inferenčne obdelave
- Načrtovanje arhitektur podatkovnih tokov, ki ohranjajo zasebnost in omogočajo inteligenco
- Uvajanje stroškovno učinkovitih AI rešitev, ki se prilagajajo zahtevam uporabnikov

**Pozicioniranje na trgu**
- Razumevanje konkurenčnih prednosti Windows-native AI aplikacij
- Identifikacija primerov uporabe, kjer AI na napravi zagotavlja vrhunsko uporabniško izkušnjo
- Razvoj strategij za vstop na trg za AI izboljšane Windows aplikacije
- Pozicioniranje aplikacij za izkoriščanje prednosti ekosistema Windows

## Vzorci AI v Windows App SDK

Windows App SDK zagotavlja obsežne vzorce, ki prikazujejo integracijo AI v različnih ogrodjih in scenarijih uvajanja. Ti vzorci so ključne reference za razumevanje vzorcev razvoja Windows AI.

### Vzorci Windows AI Foundry

| Vzorec | Ogrodje | Osrednje področje | Ključne funkcije |
|--------|---------|-------------------|------------------|
| [cs-winui](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsAIFoundry/cs-winui) | C# WinUI 3 | Integracija Windows AI API-jev | Popolna WinUI aplikacija, ki prikazuje Windows AI API-je, optimizacijo ARM64, paketno uvajanje |

**Ključne tehnologije:**
- Windows AI API-ji
- Ogrodje WinUI 3
- Optimizacija za platformo ARM64
- Združljivost s Copilot+ PC
- Paketno uvajanje aplikacij

**Predpogoji:**
- Windows 11, priporočena naprava Copilot+ PC
- Visual Studio 2022
- Konfiguracija ARM64 gradnje
- Windows App SDK 1.8.1+

### Vzorci Windows ML

#### Vzorci v C++

| Vzorec | Vrsta | Osrednje področje | Ključne funkcije |
|--------|-------|-------------------|------------------|
| [CppConsoleDesktop](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Konzolna aplikacija | Osnove Windows ML | Odkrivanje EP, možnosti ukazne vrstice, kompilacija modela |
| [CppConsoleDesktop.FrameworkDependent](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Konzolna aplikacija | Uvajanje ogrodja | Deljena runtime, manjši odtis uvajanja |
| [CppConsoleDesktop.SelfContained](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Konzolna aplikacija | Samostojno uvajanje | Samostojno uvajanje, brez odvisnosti od runtime |
| [CppConsoleDll](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | DLL | Uporaba knjižnice | WindowsML v deljeni knjižnici, upravljanje pomnilnika |
| [CppResnetBuildDemo](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Demo | ResNet vadnica | Pretvorba modela, kompilacija EP, vadnica Build 2025 |

#### Vzorci v C#

**Konzolne aplikacije**

| Vzorec | Vrsta | Osrednje področje | Ključne funkcije |
|--------|-------|-------------------|------------------|
| [CSharpConsoleDesktop](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs) | Konzolna aplikacija | Osnovna integracija C# | Uporaba deljenih pripomočkov, ukazni vmesnik |
| [ResnetBuildDemoCS](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs) | Demo | ResNet vadnica | Pretvorba modela, kompilacija EP, vadnica Build 2025 |

**GUI aplikacije**

| Vzorec | Ogrodje | Osrednje področje | Ključne funkcije |
|--------|---------|-------------------|------------------|
| [cs-wpf](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs-wpf) | WPF | Namizni GUI | Razvrščanje slik z WPF vmesnikom |
| [cs-winforms](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs-winforms) | Windows Forms | Tradicionalni GUI | Razvrščanje slik z Windows Forms |
| [cs-winui](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs-winui) | WinUI 3 | Moderni GUI | Razvrščanje slik z WinUI 3 vmesnikom |

#### Vzorci v Pythonu

| Vzorec | Jezik | Osrednje področje | Ključne funkcije |
|--------|-------|-------------------|------------------|
| [SqueezeNetPython](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/python) | Python | Razvrščanje slik | WinML Python vezave, obdelava slik v serijah |

### Predpogoji za vzorce

**Sistemske zahteve:**
- Windows 11 PC z različico 24H2 (gradnja 26100) ali novejšo
- Visual Studio 2022 z delovnimi obremenitvami za C++ in .NET
- Windows App SDK 1.8.1 ali novejši
- Python 3.10-3.13 za Python vzorce na napravah x64 in ARM64

**Specifično za Windows AI Foundry:**
- Priporočena naprava Copilot+ PC za optimalno zmogljivost
- Konfiguracija ARM64 gradnje za vzorce Windows AI
- Zahtevana identiteta paketa (nepodprte aplikacije brez paketa)

### Pogost delovni tok vzorcev

Večina vzorcev Windows ML sledi temu standardnemu vzorcu:

1. **Inicializacija okolja** - Ustvarite ONNX Runtime okolje
2. **Registracija izvajalnih ponudnikov** - Odkrijte in registrirajte razpoložljive strojne pospeševalnike (CPU, GPU, NPU)
3. **Nalaganje modela** - Naložite ONNX model, po potrebi ga prevedite za ciljno strojno opremo
4. **Predobdelava vhodnih podatkov** - Pretvorite slike/podatke v format vhodnih podatkov modela
5. **Izvajanje inferenčne obdelave** - Izvedite model in pridobite napovedi
6. **Obdelava rezultatov** - Uporabite softmax in prikažite najboljše napovedi

### Uporabljene datoteke modelov

| Model | Namen | Vključen | Opombe |
|-------|-------|----------|-------|
| SqueezeNet | Lahka razvrščanje slik | ✅ Vključen | Predhodno usposobljen, pripravljen za uporabo |
| ResNet-50 | Razvrščanje slik z visoko natančnostjo | ❌ Zahteva pretvorbo | Uporabite [AI Toolkit](https://code.visualstudio.com/docs/intelligentapps/modelconversion) za pretvorbo |

### Podpora strojne opreme

Vsi vzorci samodejno zaznajo in uporabljajo razpoložljivo strojno opremo:
- **CPU** - Univerzalna podpora na vseh napravah Windows
- **GPU** - Samodejno zaznavanje in optimizacija za razpoložljivo grafično strojno opremo
- **NPU** - Izkoristi nevronske procesne enote na podprtih napravah (Copilot+ PC)

## Komponente platforme Windows AI Foundry

### 1. Windows AI API-ji

Windows AI API-ji zagotavljajo pripravljene AI zmogljivosti, ki jih poganjajo modeli na napravi, optimizirani za učinkovitost in zmogljivost na napravah Copilot+ PC z minimalno potrebno nastavitvijo.

#### Osrednje kategorije API-jev

**Jezikovni model Phi Silica**
- Majhen, a zmogljiv jezikovni model za generiranje besedila in razmišljanje
- Optimiziran za realnočasovno inferenčno obdelavo z minimalno porabo energije
- Podpora za prilagajanje z uporabo tehnik LoRA
- Integracija z Windows semantičnim iskanjem in pridobivanjem znanja

**API-ji za računalniški vid**
- **Prepoznavanje besedila (OCR)**: Izvleček besedila iz slik z visoko natančnostjo
- **Super resolucija slik**: Povečanje slik z uporabo lokalnih AI modelov
- **Segmentacija slik**: Identifikacija in izolacija specifičnih objektov na slikah
- **Opis slik**: Generiranje podrobnih besedilnih opisov za vizualne vsebine
- **Brisanje objektov**: Odstranjevanje neželenih objektov s slik z AI-podprtim retuširanjem

**Multimodalne zmogljivosti**
- **Integracija vida in jezika**: Kombinacija razumevanja besedila in slik
- **Semantično iskanje**: Omogočanje naravnih jezikovnih poizvedb po večpredstavnostnih vsebinah
- **Pridobivanje znanja**: Gradnja inteligentnih iskalnih izkušenj z lokalnimi podatki

### 2. Foundry Local

Foundry Local razvijalcem omogoča hiter dostop do pripravljenih odprtokodnih jezikovnih modelov na Windows Silicon, kar omogoča brskanje, testiranje, interakcijo in uvajanje modelov v lokalne aplikacije.

#### Vzorčne aplikacije Foundry Local

[Foundry Local repozitorij](https://github.com/microsoft/Foundry-Local/tree/main/samples) zagotavlja obsežne vzorce v različnih programskih jezikih in ogrodjih, ki prikazujejo različne vzorce integracije in primere uporabe.

| Vzorec | Jezik/Ogrodje | Osrednje področje | Ključne funkcije |
|--------|---------------|-------------------|------------------|
| [dotNET/rag](https://github.com/microsoft/Foundry-Local/tree/main/samples/dotNET/rag) | C# / .NET | Implementacija RAG | Integracija semantičnega jedra, Qdrant vektorska shramba, JINA vdelave, zajem dokumentov, pretočni klepet |
| [electron/foundry-chat](https://github.com/microsoft/Foundry-Local/tree/main/samples/electron/foundry-chat) | JavaScript / Electron | Namizna
| [rust/hello-foundry-local](https://github.com/microsoft/Foundry-Local/tree/main/samples/rust/hello-foundry-local) | Rust | Integracija sistemov | Uporaba nizkonivojskega SDK-ja, asinhrone operacije, odjemalec HTTP reqwest |

#### Kategorije primerov glede na uporabo

**RAG (Generacija z obogatenim iskanjem)**
- **dotNET/rag**: Popolna implementacija RAG z uporabo Semantic Kernel, vektorske baze podatkov Qdrant in JINA vektorskih predstavitev
- **Arhitektura**: Uvoz dokumentov → Razdelitev besedila → Vektorske predstavitve → Iskanje podobnosti → Odzivi, prilagojeni kontekstu
- **Tehnologije**: Microsoft.SemanticKernel, Qdrant.Client, BERT ONNX vektorske predstavitve, pretočno dokončanje klepeta

**Namizne aplikacije**
- **electron/foundry-chat**: Klepetalna aplikacija, pripravljena za produkcijo, z možnostjo preklopa med lokalnim in oblačnim modelom
- **Funkcije**: Izbirnik modelov, pretočni odzivi, obravnava napak, večplatformska namestitev
- **Arhitektura**: Glavni proces Electron, komunikacija IPC, varni skripti za prednalaganje

**Primeri integracije SDK-ja**
- **JavaScript (Node.js)**: Osnovna interakcija z modeli in pretočni odzivi
- **Python**: Uporaba API-ja, združljivega z OpenAI, z asinhronim pretokom
- **Rust**: Nizkonivojska integracija z reqwest in tokio za asinhrone operacije

#### Predpogoji za primere Foundry Local

**Sistemske zahteve:**
- Windows 11 z nameščenim Foundry Local
- Node.js v16+ za primere JavaScript/Electron
- .NET 8.0+ za primere C#
- Python 3.10+ za primere Python
- Rust 1.70+ za primere Rust

**Namestitev:**
```powershell
# Install Foundry Local
winget install Microsoft.FoundryLocal

# Verify installation
foundry --version
foundry model list
```

#### Nastavitev specifična za primere

**dotNET RAG Primer:**
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

**Electron Chat Primer:**
```powershell
# Set environment variables for cloud fallback
$env:YOUR_API_KEY="your-cloud-api-key"
$env:YOUR_ENDPOINT="your-cloud-endpoint"
$env:YOUR_MODEL_NAME="your-cloud-model"

# Install dependencies and run
npm install
npm start
```

**JavaScript/Python/Rust Primeri:**
```powershell
# Download model (example with phi-3.5-mini)
foundry model run phi-3.5-mini

# Run respective sample
node src/app.js          # JavaScript
python src/app.py        # Python
cargo run               # Rust
```

#### Ključne funkcije

**Katalog modelov**
- Obsežna zbirka predhodno optimiziranih odprtokodnih modelov
- Optimizacija modelov za CPU-je, GPU-je in NPU-je za takojšnjo uporabo
- Podpora za priljubljene družine modelov, vključno z Llama, Mistral, Phi in specializiranimi modeli za določene domene

**Integracija CLI**
- Ukazna vrstica za upravljanje in namestitev modelov
- Avtomatizirani postopki optimizacije in kvantizacije
- Integracija z priljubljenimi razvojnimi okolji in CI/CD procesi

**Lokalna namestitev**
- Popolno delovanje brez odvisnosti od oblaka
- Podpora za prilagojene oblike in konfiguracije modelov
- Učinkovito serviranje modelov z avtomatsko optimizacijo strojne opreme

### 3. Windows ML

Windows ML je osrednja AI platforma in integrirano okolje za izvajanje modelov na Windows, ki omogoča razvijalcem učinkovito namestitev prilagojenih modelov na širok ekosistem strojne opreme Windows.

#### Prednosti arhitekture

**Univerzalna podpora strojne opreme**
- Avtomatska optimizacija za AMD, Intel, NVIDIA in Qualcomm čipe
- Podpora za izvajanje na CPU, GPU in NPU z avtomatskim preklapljanjem
- Abstrakcija strojne opreme, ki odpravlja potrebo po specifični optimizaciji za platformo

**Prilagodljivost modelov**
- Podpora za format modelov ONNX z avtomatsko pretvorbo iz priljubljenih ogrodij
- Namestitev prilagojenih modelov z zmogljivostjo na ravni produkcije
- Integracija z obstoječimi arhitekturami aplikacij Windows

**Integracija v podjetjih**
- Združljivost z varnostnimi in skladnostnimi okviri Windows
- Podpora za orodja za namestitev in upravljanje v podjetjih
- Integracija z orodji za upravljanje in spremljanje naprav Windows

## Potek razvoja

### Faza 1: Priprava okolja in konfiguracija orodij

**Priprava razvojnega okolja**
1. Namestite Visual Studio 2022 z delovnimi obremenitvami za C++ in .NET
2. Namestite Windows App SDK 1.8.1 ali novejši
3. Konfigurirajte orodja CLI za Windows AI Foundry
4. Nastavite razširitev AI Toolkit za Visual Studio Code
5. Vzpostavite orodja za profiliranje zmogljivosti in spremljanje
6. Zagotovite konfiguracijo ARM64 za optimizacijo Copilot+ PC

**Nastavitev repozitorija primerov**
1. Klonirajte [Windows App SDK Samples repozitorij](https://github.com/microsoft/WindowsAppSDK-Samples)
2. Pomaknite se do `Samples/WindowsAIFoundry/cs-winui` za primere API-jev Windows AI
3. Pomaknite se do `Samples/WindowsML` za obsežne primere Windows ML
4. Preglejte [zahteve za gradnjo](https://learn.microsoft.com/windows/apps/windows-app-sdk/system-requirements) za ciljne platforme

**Raziskovanje AI Dev Gallery**
- Raziščite primerne aplikacije in referenčne implementacije
- Preizkusite API-je Windows AI z interaktivnimi demonstracijami
- Preglejte izvorno kodo za najboljše prakse in vzorce
- Identificirajte ustrezne primere za vaš specifični primer uporabe

### Faza 2: Izbor modela in integracija

**Analiza zahtev**
- Določite funkcionalne zahteve za AI zmogljivosti
- Vzpostavite omejitve zmogljivosti in cilje optimizacije
- Ocenite zahteve glede zasebnosti in varnosti
- Načrtujte arhitekturo namestitve in strategije skaliranja

**Ocenjevanje modelov**
- Uporabite Foundry Local za testiranje odprtokodnih modelov za vaš primer uporabe
- Primerjajte API-je Windows AI glede na zahteve prilagojenih modelov
- Ocenite kompromise med velikostjo modela, natančnostjo in hitrostjo sklepanja
- Prototipirajte pristope integracije z izbranimi modeli

### Faza 3: Razvoj aplikacije

**Osnovna integracija**
- Implementirajte integracijo API-jev Windows AI z ustreznim ravnanjem z napakami
- Oblikujte uporabniške vmesnike, ki upoštevajo delovne tokove AI obdelave
- Implementirajte strategije predpomnjenja in optimizacije za sklepanja modelov
- Dodajte telemetrijo in spremljanje zmogljivosti AI operacij

**Testiranje in validacija**
- Testirajte aplikacije na različnih konfiguracijah strojne opreme Windows
- Validirajte zmogljivostne metrike pod različnimi pogoji obremenitve
- Implementirajte avtomatizirano testiranje za zanesljivost funkcionalnosti AI
- Izvedite testiranje uporabniške izkušnje z AI izboljšanimi funkcijami

### Faza 4: Optimizacija in namestitev

**Optimizacija zmogljivosti**
- Profilirajte zmogljivost aplikacije na ciljni strojni opremi
- Optimizirajte uporabo pomnilnika in strategije nalaganja modelov
- Implementirajte prilagodljivo vedenje glede na razpoložljive zmogljivosti strojne opreme
- Izboljšajte uporabniško izkušnjo za različne scenarije zmogljivosti

**Namestitev v produkcijo**
- Pakirajte aplikacije z ustreznimi odvisnostmi modelov AI
- Implementirajte mehanizme za posodobitev modelov in logike aplikacij
- Konfigurirajte spremljanje in analitiko za produkcijska okolja
- Načrtujte strategije uvajanja za podjetja in potrošnike

## Praktični primeri implementacije

### Primer 1: Inteligentna aplikacija za obdelavo dokumentov

Razvijte Windows aplikacijo, ki obdeluje dokumente z več AI zmogljivostmi:

**Uporabljene tehnologije:**
- Phi Silica za povzetke dokumentov in odgovarjanje na vprašanja
- OCR API-ji za ekstrakcijo besedila iz skeniranih dokumentov
- API-ji za opis slik za analizo grafikonov in diagramov
- Prilagojeni ONNX modeli za klasifikacijo dokumentov

**Pristop k implementaciji:**
- Oblikujte modularno arhitekturo s priključljivimi AI komponentami
- Implementirajte asinhrono obdelavo za velike serije dokumentov
- Dodajte indikatorje napredka in podporo za preklic dolgotrajnih operacij
- Vključite možnost delovanja brez povezave za obdelavo občutljivih dokumentov

### Primer 2: Sistem za upravljanje zalog v trgovini

Ustvarite sistem za upravljanje zalog, ki temelji na AI, za trgovinske aplikacije:

**Uporabljene tehnologije:**
- Segmentacija slik za identifikacijo izdelkov
- Prilagojeni vizualni modeli za klasifikacijo blagovnih znamk in kategorij
- Namestitev specializiranih jezikovnih modelov za trgovino prek Foundry Local
- Integracija z obstoječimi POS in sistemi za upravljanje zalog

**Pristop k implementaciji:**
- Zgradite integracijo kamer za skeniranje izdelkov v realnem času
- Implementirajte prepoznavanje črtnih kod in vizualno prepoznavanje izdelkov
- Dodajte naravne jezikovne poizvedbe zalog z lokalnimi jezikovnimi modeli
- Oblikujte skalabilno arhitekturo za namestitev v več trgovinah

### Primer 3: Pomočnik za dokumentacijo v zdravstvu

Razvijte orodje za dokumentacijo v zdravstvu, ki ohranja zasebnost:

**Uporabljene tehnologije:**
- Phi Silica za generiranje medicinskih zapisov in podporo pri kliničnih odločitvah
- OCR za digitalizacijo ročno napisanih medicinskih zapisov
- Prilagojeni medicinski jezikovni modeli, nameščeni prek Windows ML
- Lokalno shranjevanje vektorjev za iskanje medicinskega znanja

**Pristop k implementaciji:**
- Zagotovite popolno delovanje brez povezave za zaščito zasebnosti pacientov
- Implementirajte validacijo medicinske terminologije in predloge
- Dodajte beleženje revizij za skladnost z regulativnimi zahtevami
- Oblikujte integracijo z obstoječimi sistemi elektronskih zdravstvenih zapisov

## Strategije optimizacije zmogljivosti

### Razvoj, prilagojen strojni opremi

**Optimizacija za NPU**
- Oblikujte aplikacije za izkoriščanje zmogljivosti NPU na Copilot+ PC-jih
- Implementirajte elegantno preklapljanje na GPU/CPU na napravah brez NPU
- Optimizirajte oblike modelov za pospeševanje specifično za NPU
- Spremljajte uporabo NPU in termične značilnosti

**Upravljanje pomnilnika**
- Implementirajte učinkovite strategije nalaganja in predpomnjenja modelov
- Uporabite preslikavo pomnilnika za velike modele za zmanjšanje časa zagona
- Oblikujte aplikacije, ki so zavedne porabe pomnilnika za naprave z omejenimi viri
- Implementirajte kvantizacijo modelov za optimizacijo pomnilnika

**Učinkovitost baterije**
- Optimizirajte AI operacije za minimalno porabo energije
- Implementirajte prilagodljivo obdelavo glede na stanje baterije
- Oblikujte učinkovito obdelavo v ozadju za neprekinjene AI operacije
- Uporabite orodja za profiliranje porabe energije za optimizacijo

### Premisleki o skalabilnosti

**Večnitnost**
- Oblikujte varne AI operacije za sočasno obdelavo
- Implementirajte učinkovito razdelitev dela med razpoložljiva jedra
- Uporabite vzorce async/await za neblokirajoče AI operacije
- Načrtujte optimizacijo bazenov niti za različne konfiguracije strojne opreme

**Strategije predpomnjenja**
- Implementirajte inteligentno predpomnjenje za pogosto uporabljene AI operacije
- Oblikujte strategije invalidacije predpomnilnika za posodobitve modelov
- Uporabite trajno predpomnjenje za drage operacije predobdelave
- Implementirajte porazdeljeno predpomnjenje za scenarije z več uporabniki

## Najboljše prakse za varnost in zasebnost

### Zaščita podatkov

**Lokalna obdelava**
- Zagotovite, da občutljivi podatki nikoli ne zapustijo lokalne naprave
- Implementirajte varno shranjevanje za AI modele in začasne podatke
- Uporabite varnostne funkcije Windows za peskovnik aplikacij
- Uporabite šifriranje za shranjene modele in vmesne rezultate obdelave

**Varnost modelov**
- Validirajte integriteto modelov pred nalaganjem in izvajanjem
- Implementirajte varne mehanizme za posodobitev modelov
- Uporabite podpisane modele za preprečevanje manipulacij
- Uporabite nadzorne ukrepe za datoteke modelov in konfiguracijo

### Premisleki o skladnosti

**Regulativna uskladitev**
- Oblikujte aplikacije, ki ustrezajo GDPR, HIPAA in drugim regulativnim zahtevam
- Implementirajte beleženje revizij za procese odločanja AI
- Zagotovite funkcije transparentnosti za rezultate, ki jih generira AI
- Omogočite uporabniški nadzor nad obdelavo podatkov AI

**Varnost v podjetjih**
- Integrirajte z varnostnimi politikami podjetja Windows
- Podprite upravljano namestitev prek orodij za upravljanje v podjetjih
- Implementirajte nadzor dostopa na podlagi vlog za funkcije AI
- Zagotovite administrativne kontrole za funkcionalnost AI

## Odpravljanje težav in razhroščevanje

### Pogosti izzivi pri razvoju

**Težave s konfiguracijo gradnje**
- Zagotovite konfiguracijo platforme ARM64 za primere API-jev Windows AI
- Preverite združljivost različice Windows App SDK (zahtevana različica 1.8.1+)
- Preverite, ali je identiteta paketa pravilno konfigurirana (zahtevano za API-je Windows AI)
- Validirajte, ali orodja za gradnjo podpirajo ciljno različico ogrodja

**Težave pri nalaganju modelov**
- Validirajte združljivost modelov ONNX z Windows ML
- Preverite integriteto datotek modelov in zahteve glede formata
- Preverite zahteve glede zmogljivosti strojne opreme za specifične modele
- Razhroščite težave z dodeljevanjem pomnilnika med nalaganjem modelov
- Zagotovite registracijo ponudnika izvajanja za pospeševanje strojne opreme

**Premisleki o načinu namestitve**
- **Samostojni način**: Popolnoma podprt z večjo velikostjo namestitve
- **Način, odvisen od ogrodja**: Manjši odtis, vendar zahteva skupni runtime
- **Nepakirane aplikacije**: Ni več podprto za API-je Windows AI
- Uporabite `dotnet run -p:Platform=ARM64 -p:SelfContained=true` za samostojno namestitev ARM64

**Težave z zmogljivostjo**
- Profilirajte zmogljivost aplikacije na različnih konfiguracijah strojne opreme
- Identificirajte ozka grla v procesnih tokovih AI
- Optimizirajte operacije predobdelave in naknadne obdelave podatkov
- Implementirajte spremljanje zmogljivosti in opozarjanje

**Težave pri integraciji**
- Razhroščite težave pri integraciji API-jev z ustreznim ravnanjem z napakami
- Validirajte formate vhodnih podatkov in zahteve predobdelave
- Temeljito testirajte robne primere in pogoje napak
- Implementirajte obsežno beleženje za razhroščevanje težav v produkciji

### Orodja in tehnike za razhroščevanje

**Integracija z Visual Studio**
- Uporabite razhroščevalnik AI Toolkit za analizo izvajanja modelov
- Implementirajte profiliranje zmogljivosti za AI operacije
- Razhroščite asinhrone AI operacije z ustreznim ravnanjem z izjemami
- Uporabite orodja za profiliranje pomnilnika za optimizacijo

**Orodja Windows AI Foundry**
- Izkoristite CLI Foundry Local za testiranje in validacijo modelov
- U
- [Pregled Windows ML](https://learn.microsoft.com/windows/ai/new-windows-ml/overview/)
- [Sistemske zahteve za Windows App SDK](https://docs.microsoft.com/windows/apps/windows-app-sdk/system-requirements)
- [Nastavitev razvojnega okolja za Windows App SDK](https://docs.microsoft.com/windows/apps/windows-app-sdk/set-up-your-development-environment)
- 

### Primeri repozitorijev in kode
- [Primeri Windows App SDK - Windows AI Foundry](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsAIFoundry)
- [Primeri Windows App SDK - Windows ML](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML)
- [Primeri inferenc ONNX Runtime](https://github.com/microsoft/onnxruntime-inference-examples)
- [Repozitorij primerov Windows App SDK](https://github.com/microsoft/WindowsAppSDK-Samples)

### Razvojna orodja
- [AI orodjarna za Visual Studio Code](https://learn.microsoft.com/windows/ai/toolkit/)
- [Galerija AI za razvijalce](https://learn.microsoft.com/windows/ai/ai-dev-gallery/)
- [Primeri Windows AI](https://learn.microsoft.com/windows/ai/samples/)
- [Orodja za pretvorbo modelov](https://code.visualstudio.com/docs/intelligentapps/modelconversion)

### Tehnična podpora
- [Dokumentacija Windows ML](https://learn.microsoft.com/windows/ai/new-windows-ml/overview)
- [Dokumentacija ONNX Runtime](https://onnxruntime.ai/docs/)
- [Dokumentacija Windows App SDK](https://docs.microsoft.com/windows/apps/windows-app-sdk/)
- [Prijava težav - Primeri Windows App SDK](https://github.com/microsoft/WindowsAppSDK-Samples/issues)

### Skupnost in podpora
- [Skupnost razvijalcev za Windows](https://developer.microsoft.com/en-us/windows/)
- [Blog Windows AI Foundry](https://blogs.windows.com/windowsdeveloper/)
- [Microsoft Learn AI usposabljanje](https://learn.microsoft.com/training/browse/?products=windows&subjects=artificial-intelligence)

---

*Ta vodnik je zasnovan tako, da se razvija skupaj z hitro napredujočim ekosistemom Windows AI. Redne posodobitve zagotavljajo usklajenost z najnovejšimi zmogljivostmi platforme in najboljšimi praksami razvoja.*

[08. Praktično delo z Microsoft Foundry Local - Celoten komplet orodij za razvijalce](../Module08/README.md)

---

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve AI za prevajanje [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne prevzemamo odgovornosti za morebitna nesporazumevanja ali napačne razlage, ki izhajajo iz uporabe tega prevoda.
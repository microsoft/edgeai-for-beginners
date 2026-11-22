# Vodnik za razvoj Windows Edge AI

## Uvod

Dobrodošli v razvoju Windows Edge AI - vašem celovitem vodniku za izdelavo inteligentnih aplikacij, ki izkoriščajo moč on-device AI z uporabo Microsoftove platforme Windows AI Foundry. Ta vodič je posebej zasnovan za razvijalce Windows, ki želijo v svoje aplikacije vključiti najsodobnejše zmožnosti Edge AI, hkrati pa izkoristiti celoten spekter strojne pospešitve v sistemu Windows.

### Prednosti Windows AI

Windows AI Foundry predstavlja enovito, zanesljivo in varno platformo, ki podpira celoten življenjski cikel razvoja AI - od izbire in fino nastavitev modela do optimizacije in uvajanja na CPU, GPU, NPU in hibridnih oblačnih arhitekturah. Ta platforma demokratično omogoča razvoj AI z zagotavljanjem:

- **Abstrakcija strojne opreme**: Brezhibno uvajanje na silicije iz AMD, Intela, NVIDIA in Qualcomm
- **Inteligenca na napravi**: AI, ki ščiti zasebnost in deluje popolnoma na lokalni strojni opremi
- **Optimizirana zmogljivost**: Modeli vnaprej optimizirani za konfiguracije strojne opreme Windows
- **Pripravljeno za podjetja**: Varnostne in skladnostne funkcije ravni proizvodnje

### Windows ML 
Windows Machine Learning (ML) omogoča razvijalcem v C#, C++ in Pythonu, da lokalno izvajajo ONNX AI modele na računalnikih Windows preko ONNX Runtime, z avtomatskim upravljanjem izvajalnih ponudnikov za različne strojne opreme (CPU, GPU, NPU). [ONNX Runtime](https://onnxruntime.ai/docs/) je mogoče uporabljati z modeli iz PyTorch, Tensorflow/Keras, TFLite, scikit-learn in drugih okvirov.


![WindowsML Diagram, ki prikazuje model ONNX, ki gre skozi Windows ML do NPUs, GPUs in CPUs.](https://learn.microsoft.com/en-us/windows/ai/images/winml-diagram.png)

Windows ML zagotavlja deljeno sistemsko kopijo ONNX Runtime, poleg možnosti dinamičnega prenosa izvajalnih ponudnikov (EP-jev).

### Zakaj Windows za Edge AI?

**Univerzalna podpora strojne opreme**
Windows ML ponuja samodejno optimizacijo strojne opreme po celotnem Windows ekosistemu, kar zagotavlja optimalno delovanje vaših AI aplikacij ne glede na podlago silicon arhitekture.

**Integrirano AI izvajanje**
Vgrajen Windows ML inferenčni pogon odpravlja zapletene nastavitve, kar razvijalcem omogoča osredotočanje na aplikacijsko logiko in ne na infrastrukturo.

**Optimizacija Copilot+ PC**
Specifično zasnovani API-ji za naslednjo generacijo Windows naprav z namensko nevronsko obdelovalno enoto (NPU), ki zagotavlja izjemno zmogljivost na wat.

**Razvojni ekosistem**
Bogato orodje, vključno z integracijo v Visual Studio, celovito dokumentacijo in vzorčnimi aplikacijami, ki pospešujejo razvojne cikle.

## Cilji učenja

Z dokončanjem tega vodnika za razvoj Windows Edge AI boste obvladali ključne veščine za izdelavo proizvodno pripravljenih AI aplikacij na platformi Windows.

### Temeljne tehnične kompetence

**Obvladovanje Windows AI Foundry**
- Razumeti arhitekturo in komponente platforme Windows AI Foundry
- Krmariti skozi celoten življenjski cikel razvoja AI v Windows ekosistemu
- Uvesti najboljše varnostne prakse za AI aplikacije na napravi
- Optimizirati aplikacije za različne konfiguracije strojne opreme Windows

**Strokovnost integracije API**
- Obvladati Windows AI API-je za besedilo, vizijo in multimodalne aplikacije
- Implementirati integracijo jezika Phi Silica za generiranje besedil in sklepanje
- Uporabiti kapacitete računalniškega vida z vgrajenimi API-ji za obdelavo slik
- Prilagoditi vnaprej trenirane modele z metodami LoRA (nizko rangske prilagoditve)

**Lokalna implementacija Foundry**
- Brskati, ocenjevati in uvajati odprtokodne jezikovne modele z Foundry Local CLI
- Razumeti optimizacijo modelov in kvantizacijo za lokalno uvajanje
- Implementirati offline AI zmogljivosti, ki delujejo brez internetne povezave
- Upravljati življenjske cikle modelov in posodobitve v proizvodnih okoljih

**Uvajanje Windows ML**
- Prinašati prilagojene ONNX modele v Windows aplikacije z uporabo Windows ML
- Izkoristiti samodejno pospešitev strojne opreme prek CPU, GPU in NPU arhitektur
- Izvesti inferenco v realnem času z optimalno izrabo virov
- Oblikovati prilagodljive AI aplikacije za različne kategorije Windows naprav

### Veščine razvoja aplikacij

**Razvoj Windows aplikacij za več platform**
- Izdelati AI-poganjane aplikacije z uporabo .NET MAUI za univerzalno uvajanje na Windows
- Integrirati AI zmogljivosti v Win32, UWP in progresivne spletne aplikacije
- Izvesti odzivne UI zasnove, ki se prilagajajo stanjem AI obdelave
- Upravljati asinhrone AI operacije z ustreznimi vzorci uporabniške izkušnje

**Optimizacija zmogljivosti**
- Profilirati in optimizirati zmogljivost AI inferenc po različnih konfiguracijah strojne opreme
- Uvesti učinkovito upravljanje pomnilnika za velike jezikovne modele
- Oblikovati aplikacije, ki se prilagojeno zmanjšujejo glede na razpoložljive zmogljivosti strojne opreme
- Uporabiti strategije predpomnjenja za pogosto uporabljene AI operacije

**Pripravljenost za proizvodnjo**
- Izvesti celovito ravnanje z napakami in mehanizme rezervnih rešitev
- Oblikovati telemetrijo in nadzor nad zmogljivostjo AI aplikacij
- Uvesti varnostne najboljše prakse za lokalno shranjevanje in izvajanje AI modelov
- Načrtovati strategije uvajanja za podjetniške in potrošniške aplikacije

### Poslovno in strateško razumevanje

**Arhitektura AI aplikacij**
- Oblikovati hibridne arhitekture, ki optimizirajo med lokalno in oblačno AI obdelavo
- Oceniti kompromise med velikostjo modela, natančnostjo in hitrostjo inference
- Načrtovati arhitekture pretoka podatkov, ki ohranjajo zasebnost in omogočajo inteligentnost
- Uvesti stroškovno učinkovite AI rešitve, ki se prilagajajo zahtevam uporabnikov

**Tržna pozicioniranja**
- Razumeti konkurenčne prednosti AI aplikacij, naravnanih na Windows
- Identificirati primere uporabe, kjer on-device AI zagotavlja boljšo uporabniško izkušnjo
- Razviti strategije prodora na trg za Windows aplikacije z dodatno AI vrednostjo
- Pozicionirati aplikacije, da izkoristijo prednosti Windows ekosistema

## Primeri AI Windows App SDK

Windows App SDK ponuja celovite primere, ki prikazujejo integracijo AI skozi več različnih okvirov in scenarijev uvajanja. Ti primeri so ključne reference za razumevanje vzorcev razvoja Windows AI.

### Primeri Windows AI Foundry

| Primer | Okvir | Osrednje področje | Ključne značilnosti |
|--------|-----------|------------|-------------|
| [cs-winui](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsAIFoundry/cs-winui) | C# WinUI 3 | Integracija Windows AI API-jev | Celovita WinUI aplikacija, ki prikazuje Windows AI api-je, optimizacijo za ARM64, pakirano uvajanje |

**Ključne tehnologije:**
- Windows AI API-ji
- Okvir WinUI 3
- Optimizacija platforme ARM64
- Združljivost Copilot+ PC
- Pakirano uvajanje aplikacij

**Zahteve:**
- Priporočen Windows 11 z Copilot+ PC za optimalno zmogljivost
- Visual Studio 2022
- Konfiguracija za gradnjo ARM64
- Windows App SDK 1.8.1 ali novejši

### Primeri Windows ML

#### Primeri v C++

| Primer | Tip | Osrednje področje | Ključne značilnosti |
|--------|------|------------|-------------|
| [CppConsoleDesktop](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Konzolna aplikacija | Osnovni Windows ML | Odkritje EP-jev, možnosti ukazne vrstice, kompilacija modelov |
| [CppConsoleDesktop.FrameworkDependent](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Konzolna aplikacija | Uvajanje okvira | Deljeno izvajanje, manjši odtis uvajanja |
| [CppConsoleDesktop.SelfContained](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Konzolna aplikacija | Samostojno uvajanje | Samostojno uvajanje, brez odvisnosti izvajanja |
| [CppConsoleDll](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | DLL | Uporaba knjižnice | WindowsML v deljeni knjižnici, upravljanje pomnilnika |
| [CppResnetBuildDemo](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Demonstracija | Domača naloga ResNet | Pretvorba modela, kompilacija EP, vadnica Build 2025 |

#### Primeri v C#

**Konzolne aplikacije**

| Primer | Tip | Osrednje področje | Ključne značilnosti |
|--------|------|------------|-------------|
| [CSharpConsoleDesktop](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs) | Konzolna aplikacija | Osnovna integracija C# | Uporaba deljenih pomožnih programov, ukazno-vrstični vmesnik |
| [ResnetBuildDemoCS](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs) | Demonstracija | Domača naloga ResNet | Pretvorba modela, kompilacija EP, vadnica Build 2025 |

**GUI aplikacije**

| Primer | Okvir | Osrednje področje | Ključne značilnosti |
|--------|-----------|------------|-------------|
| [cs-wpf](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs-wpf) | WPF | Namizni GUI | Klasifikacija slik z WPF vmesnikom |
| [cs-winforms](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs-winforms) | Windows Forms | Tradicionalni GUI | Klasifikacija slik z Windows Forms |
| [cs-winui](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs-winui) | WinUI 3 | Sodobni GUI | Klasifikacija slik z WinUI 3 vmesnikom |

#### Primeri v Pythonu

| Primer | Jezik | Osrednje področje | Ključne značilnosti |
|--------|----------|------------|-------------|
| [SqueezeNetPython](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/python) | Python | Klasifikacija slik | Povezave WinML Python, serijska obdelava slik |

### Zahteve za primere

**Sistemske zahteve:**
- Računalnik z Windows 11, različica 24H2 (build 26100) ali novejši
- Visual Studio 2022 z delovnimi obremenitvami za C++ in .NET
- Windows App SDK 1.8.1 ali novejši
- Python 3.10-3.13 za Python primere na napravah x64 in ARM64

**Specifično za Windows AI Foundry:**
- Priporočen Copilot+ PC za optimalno zmogljivost
- Konfiguracija gradnje ARM64 za Windows AI primere
- Zahtevana identiteta paketa (nepakirane aplikacije niso več podprte)

### Pogost delovni potek primerov

Večina Windows ML primerov sledi temu standardnemu vzorcu:

1. **Inicializacija okolja** - Ustvarite ONNX Runtime okolje
2. **Registracija izvajalnih ponudnikov** - Odkrijte in registrirajte razpoložljive strojne pospeševalnike (CPU, GPU, NPU)
3. **Nalaganje modela** - Naložite ONNX model, po potrebi kompilirajte za ciljno strojno opremo
4. **Predobdelava vhoda** - Pretvorite slike/podatke v format vhodnih podatkov za model
5. **Izvajanje inference** - Zaženite model in pridobite napovedi
6. **Obdelava rezultatov** - Uporabite softmax in prikažite najvišje napovedi

### Upodobljene datoteke modelov

| Model | Namen | Vključeno | Opombe |
|-------|---------|----------|-------|
| SqueezeNet | Lahka klasifikacija slik | ✅ Vključeno | Vnaprej treniran, pripravljen za uporabo |
| ResNet-50 | Visoko natančna klasifikacija slik | ❌ Zahteva pretvorbo | Uporabite [AI Toolkit](https://code.visualstudio.com/docs/intelligentapps/modelconversion) za pretvorbo |

### Podpora strojne opreme

Vsi primeri samodejno zaznajo in izkoristijo razpoložljivo strojno opremo:
- **CPU** - Univerzalna podpora na vseh Windows napravah
- **GPU** - Samodejno zaznavanje in optimizacija za razpoložljivo grafično strojno opremo
- **NPU** - Izrablja nevronske procesne enote na podprtih napravah (Copilot+ PC-ji)

## Komponente platforme Windows AI Foundry

### 1. Windows AI API-ji

Windows AI API-ji zagotavljajo takoj uporabne AI zmogljivosti, ki temeljijo na modelih na napravi, optimiziranih za učinkovitost in zmogljivost na napravah Copilot+ PC, z minimalnimi potrebami po nastavitvi.

#### Osnovne kategorije API-jev

**Jezikovni model Phi Silica**
- Majhen a zmogljiv jezikovni model za generiranje besedila in sklepanje
- Optimiziran za inferenčni čas v realnem času z minimalno porabo energije
- Podpora za prilagajanje z uporabo tehnik LoRA
- Integracija z Windows semantičnim iskanjem in pridobivanjem znanja

**API-ji za računalniški vid**
- **Prepoznavanje besedila (OCR)**: Izvleček besedila iz slik z visoko natančnostjo
- **Izboljšanje ločljivosti slik**: Povečanje slik z lokalnimi AI modeli
- **Segmentacija slik**: Prepoznavanje in ločevanje specifičnih objektov na slikah
- **Opis slik**: Generiranje podrobnih besedilnih opisov vizualnih vsebin
- **Briši objekt**: Odstranitev nezaželenih objektov z AI-poganskim osveževanjem slik

**Multimodalne zmogljivosti**
- **Integracija vida in jezika**: Združevanje besedila in razumevanja slik
- **Semantično iskanje**: Omogoča poizvedbe v naravnem jeziku po multimedijskih vsebinah
- **Pridobivanje znanja**: Gradnja inteligentnih izkušenj iskanja z lokalnimi podatki

### 2. Foundry Local

Foundry Local razvijalcem omogoča hiter dostop do takoj uporabnih odprtokodnih jezikovnih modelov na Windows Silicon, ponuja možnost brskanja, testiranja, interakcije in uvajanja modelov v lokalnih aplikacijah.

#### Vzorčne aplikacije Foundry Local

[Foundry Local repozitorij](https://github.com/microsoft/Foundry-Local/tree/main/samples) nudi celovite primere v različnih programskih jezikih in okvirih, ki prikazujejo različne vzorce integracije in primere uporabe.

| Primer | Jezik/Okvir | Osrednje področje | Ključne značilnosti |
|--------|-------------------|------------|-------------|
| [dotNET/rag](https://github.com/microsoft/Foundry-Local/tree/main/samples/dotNET/rag) | C# / .NET | Uvedba RAG | Integracija Semantic Kernel, Qdrant vektorska zbirka, JINA vdelave, ingestija dokumentov, pretočni klepet |
| [electron/foundry-chat](https://github.com/microsoft/Foundry-Local/tree/main/samples/electron/foundry-chat) | JavaScript / Electron | Namizna klepetalnica | Večplatformski klepet, preklapljanje lokalnih/in oblak modelov, integracija OpenAI SDK, pretočni prenos v realnem času |
| [js/hello-foundry-local](https://github.com/microsoft/Foundry-Local/tree/main/samples/js/hello-foundry-local) | JavaScript / Node.js | Osnovna integracija | Enostavna uporaba SDK, inicializacija modela, osnovna klepetalna funkcionalnost |
| [python/hello-foundry-local](https://github.com/microsoft/Foundry-Local/tree/main/samples/python/hello-foundry-local) | Python | Osnovna integracija | Uporaba Python SDK, pretočni odzivi, OpenAI-kompatibilen API |

| [rust/hello-foundry-local](https://github.com/microsoft/Foundry-Local/tree/main/samples/rust/hello-foundry-local) | Rust | Sistemska integracija | Nizkonivojska uporaba SDK-ja, asinkrone operacije, HTTP odjemalec reqwest |

#### Kategorije vzorcev po uporabi

**RAG (Generiranje zpoizvedbo obogateno z iskanjem)**
- **dotNET/rag**: Popolna implementacija RAG z uporabo Semantic Kernel, Qdrant vektorske baze podatkov in vdelkov JINA
- **Arhitektura**: Vnos dokumentov → Razbijanje besedila → Vektorski vdelki → Iskanje podobnosti → Odzivi, ki upoštevajo kontekst
- **Tehnologije**: Microsoft.SemanticKernel, Qdrant.Client, BERT ONNX vdelki, pretočno dokončanje klepeta

**Namizne aplikacije**
- **electron/foundry-chat**: Produkcijsko pripravljen klepetalni aplikaciji z lokalnim/oblačnim preklapljanjem modelov
- **Funkcije**: Izbirnik modelov, pretočni odgovori, obravnava napak, večplatformska namestitev
- **Arhitektura**: Glavni proces Electron, IPC komunikacija, varni predhodni skripti

**Primeri integracije SDK**
- **JavaScript (Node.js)**: Osnovna interakcija z modelom in pretočni odgovori
- **Python**: Uporaba OpenAI-kompatibilnega API-ja z asinhronim pretokom
- **Rust**: Nizkonivojska integracija z reqwest in tokio za asinhrone operacije

#### Predpogoji za vzorce Foundry Local

**Sistemske zahteve:**
- Windows 11 z nameščenim Foundry Local
- Node.js v16+ za JavaScript/Electron vzorce
- .NET 8.0+ za vzorce C#
- Python 3.10+ za Python vzorce
- Rust 1.70+ za Rust vzorce

**Namestitev:**
```powershell
# Namestite Foundry Local
winget install Microsoft.FoundryLocal

# Preverite namestitev
foundry --version
foundry model list
```

#### Nastavitev za posamezen vzorec

**dotNET RAG vzorec:**
```powershell
# Namestite zahtevane pakete prek NuGet
# Microsoft.SemanticKernel.Connectors.Onnx
# Microsoft.SemanticKernel.Connectors.Qdrant
# Qdrant.Client

# Zaženite Qdrant vektorsko podatkovno bazo
docker run -p 6333:6333 qdrant/qdrant

# Zaženite Jupyter beležnico
jupyter notebook rag_foundrylocal_demo.ipynb
```

**Elektronski klepetalni vzorec:**
```powershell
# Nastavite okoljske spremenljivke za oblačni rezervni načrt
$env:YOUR_API_KEY="your-cloud-api-key"
$env:YOUR_ENDPOINT="your-cloud-endpoint"
$env:YOUR_MODEL_NAME="your-cloud-model"

# Namestite odvisnosti in zaženite
npm install
npm start
```

**JavaScript/Python/Rust vzorci:**
```powershell
# Prenesite model (primer s phi-3.5-mini)
foundry model run phi-3.5-mini

# Zaženite ustrezni vzorec
node src/app.js          # JavaScript
python src/app.py        # Python
cargo run               # Rust
```

#### Ključne funkcije

**Katalog modelov**
- Celovita zbirka pred-optimiziranih odprtokodnih modelov
- Modeli optimizirani za CPU-je, GPU-je in NPU-je za takojšnjo namestitev
- Podpora za priljubljene družine modelov, vključno z Llama, Mistral, Phi in specializiranimi domenami

**CLI integracija**
- Ukazna vrstica za upravljanje in nameščanje modelov
- Avtomatizirani delovni tokovi optimizacije in kvantizacije
- Integracija s priljubljenimi razvojnimi okolji in CI/CD cevovodi

**Lokalna namestitev**
- Popolno delovanje brez povezave brez oblačnih odvisnosti
- Podpora za prilagojene formate in konfiguracije modelov
- Učinkovita dostava modelov z avtomatsko optimizacijo strojne opreme

### 3. Windows ML

Windows ML služi kot jedrna platforma AI in integrirano izvršilno okolje na Windows, ki razvijalcem omogoča učinkovito nameščanje prilagojenih modelov znotraj širokega Windows ekosistema strojne opreme.

#### Prednosti arhitekture

**Univerzalna podpora strojne opreme**
- Samodejna optimizacija za AMD, Intel, NVIDIA in Qualcomm silikon
- Podpora za CPU, GPU in NPU izvajanje z zunanjim preklapljanjem
- Strojna abstrakcija, ki odpravi delo specifične optimizacije platforme

**Fleksibilnost modelov**
- Podpora ONNX formatu modelov z avtomatsko pretvorbo iz priljubljenih frameworkov
- Prilagojena namestitev modelov z zmogljivostmi produktne ravni
- Integracija z obstoječimi Windows arhitekturami aplikacij

**Integracija v gospodarstvo**
- Združljivo z varnostnimi in skladnostnimi okviri Windows
- Podpora orodjem za upravljanje in namestitev za gospodarstvo
- Integracija z upravljanjem naprav in sistemi spremljanja Windows

## Razvojni potek

### Faza 1: Nastavitev okolja in konfiguracija orodij

**Priprava razvojnega okolja**
1. Namestite Visual Studio 2022 z delovnimi obremenitvami C++ in .NET
2. Namestite Windows App SDK 1.8.1 ali novejši
3. Konfigurirajte Windows AI Foundry CLI orodja
4. Nastavite razširitev AI Toolkit za Visual Studio Code
5. Vzpostavite orodja za profiliranje zmogljivosti in spremljanje
6. Zagotovite konfiguracijo gradnje ARM64 za optimizacijo Copilot+ PC

**Nastavitev repozitorija vzorcev**
1. Klonirajte [Windows App SDK vzorce](https://github.com/microsoft/WindowsAppSDK-Samples)
2. Pomaknite se v `Samples/WindowsAIFoundry/cs-winui` za primere Windows AI API-jev
3. Pomaknite se v `Samples/WindowsML` za obsežne primere Windows ML
4. Preglejte [zahteve za gradnjo](https://learn.microsoft.com/windows/apps/windows-app-sdk/system-requirements) za vaše ciljne platforme

**Raziskovanje AI Dev galerije**
- Raziskujte vzorčne aplikacije in referenčne implementacije
- Preizkusite Windows AI API-je z interaktivnimi demonstracijami
- Preglejte izvorno kodo za dobre prakse in vzorce
- Prepoznajte relevantne vzorce za vaš specifičen primer uporabe

### Faza 2: Izbira in integracija modela

**Analiza zahtev**
- Določite funkcionalne zahteve za AI zmožnosti
- Ugotovite omejitve zmogljivosti in cilje optimizacije
- Ocenite zahteve glede zasebnosti in varnosti
- Načrtujte arhitekturo namestitve in strategije skaliranja

**Vrednotenje modela**
- Uporabite Foundry Local za testiranje odprtokodnih modelov za vaš primer uporabe
- Primerjajte Windows AI API-je glede na zahteve za prilagojene modele
- Ocenite kompromise med velikostjo modela, natančnostjo in hitrostjo sklepanja
- Prototipirajte integracijske pristope z izbranimi modeli

### Faza 3: Razvoj aplikacij

**Jezgro integracije**
- Implementirajte integracijo Windows AI API z ustrezno obravnavo napak
- Oblikujte uporabniške vmesnike, ki podpirajo AI delovne tokove
- Implementirajte strategije predpomnenja in optimizacije za sklepanja modelov
- Dodajte telemetrijo in spremljanje zmogljivosti AI operacij

**Testiranje in validacija**
- Testirajte aplikacije na različnih konfiguracijah Windows strojne opreme
- Validirajte metrike zmogljivosti pri različnih obremenitvah
- Implementirajte avtomatizirano testiranje zanesljivosti AI funkcionalnosti
- Izvedite testiranje uporabniške izkušnje z AI izboljšavami

### Faza 4: Optimizacija in nameščanje

**Optimizacija zmogljivosti**
- Profilirajte zmogljivost aplikacije na ciljni strojni opremi
- Optimizirajte uporabo pomnilnika in strategije nalaganja modelov
- Implementirajte prilagodljivo vedenje glede na razpoložljive strojne zmožnosti
- Dodelajte uporabniško izkušnjo za različne scenarije zmogljivosti

**Produkcijsko nameščanje**
- Pakirajte aplikacije z ustreznimi odvisnostmi AI modelov
- Implementirajte mehanizme posodobitev modelov in aplikacijske logike
- Konfigurirajte spremljanje in analitiko produkcijskih okolij
- Načrtujte strategije uvajanja za podjetja in končne uporabnike

## Praktični primeri implementacije

### Primer 1: Pametna aplikacija za obdelavo dokumentov

Izdelajte Windows aplikacijo, ki obdeluje dokumente z več AI zmožnostmi:

**Uporabljene tehnologije:**
- Phi Silica za povzemanje dokumentov in odgovarjanje na vprašanja
- OCR API-ji za izločanje besedila iz skeniranih dokumentov
- API-ji za opisovanje slik za analizo grafikonov in diagramov
- Prilagojeni ONNX modeli za klasifikacijo dokumentov

**Pristop implementacije:**
- Oblikujte modularno arhitekturo s priključnimi AI komponentami
- Implementirajte asinhrono obdelavo velikih paketov dokumentov
- Dodajte indikatorje napredka in podporo preklicu za dolgotrajne operacije
- Vključite zmožnost delovanja brez povezave za obdelavo zaupnih dokumentov

### Primer 2: Sistem upravljanja zalog za maloprodajo

Ustvarite AI-podprt sistem zalog za maloprodajne aplikacije:

**Uporabljene tehnologije:**
- Segmentacija slik za identifikacijo izdelkov
- Prilagojeni modeli vida za klasifikacijo znamk in kategorij
- Foundry Local namestitev specializiranih maloprodajnih jezikovnih modelov
- Integracija z obstoječimi POS in sistemi upravljanja zalog

**Pristop implementacije:**
- Zgradite integracijo kamere za skeniranje izdelkov v realnem času
- Implementirajte prepoznavanje črtnih kod in vizualnih izdelkov
- Dodajte poizvedbe v naravnem jeziku za upravljanje zalog z lokalnimi jezikovnimi modeli
- Oblikujte skalabilno arhitekturo za distribucijsko namestitev v več trgovinah

### Primer 3: Asistent za zdravstveno dokumentacijo

Razvijte orodje za zdravstveno dokumentacijo z varstvom zasebnosti:

**Uporabljene tehnologije:**
- Phi Silica za generiranje medicinskih opomb in podporo kliničnim odločitvam
- OCR za digitalizacijo ročno napisanih medicinskih zapisov
- Prilagojeni zdravstveni jezikovni modeli nameščeni preko Windows ML
- Lokalno shranjevanje vektorjev za pridobivanje medicinskega znanja

**Pristop implementacije:**
- Zagotovite popolno delovanje brez povezave za zasebnost pacientov
- Implementirajte preverjanje in predloge medicinske terminologije
- Dodajte beleženje revizijskih zapisov za skladnost z regulativo
- Oblikujte integracijo z obstoječimi sistemi elektronskih zdravstvenih kartonov

## Strategije za optimizacijo zmogljivosti

### Razvoj z zavedanjem strojne opreme

**Optimizacija NPU**
- Oblikujte aplikacije za izkoriščanje zmogljivosti NPU na računalnikih Copilot+
- Implementirajte prijazno preusmeritev na GPU/CPU na napravah brez NPU
- Optimizirajte formate modelov za pospeševanje specifično za NPU
- Spremljajte uporabo NPU in toplotne značilnosti

**Upravljanje pomnilnika**
- Implementirajte učinkovite strategije nalaganja in predpomnenja modelov
- Uporabite preslikavo pomnilnika za velike modele za zmanjšanje časa zagona
- Oblikujte aplikacije, ki varčujejo s pomnilnikom za naprave z omejenimi viri
- Implementirajte kvantizacijo modelov za optimizacijo pomnilnika

**Učinkovitost baterije**
- Optimizirajte AI operacije za minimalno porabo energije
- Implementirajte prilagodljivo obdelavo glede na stanje baterije
- Oblikujte učinkovito ozadinsko obdelavo za neprekinjene AI operacije
- Uporabite orodja za profiliranje porabe energije za optimizacijo

### Premisleki o skalabilnosti

**Večnitičnost**
- Oblikujte niti varne AI operacije za vzporedno obdelavo
- Implementirajte učinkovito razporeditev dela prek razpoložljivih jeder
- Uporabite vzorce async/await za neblokirajoče AI operacije
- Načrtujte optimizacijo niti za različne konfiguracije strojne opreme

**Strategije predpomnenja**
- Implementirajte inteligentno predpomnenje za pogosto uporabljene AI operacije
- Oblikujte strategije poteka predpomnenja za posodobitve modelov
- Uporabite vztrajno predpomnenje za drage predprocesne operacije
- Implementirajte distribuirano predpomnenje za scenarije z več uporabniki

## Najboljše prakse za varnost in zasebnost

### Zaščita podatkov

**Lokalna obdelava**
- Zagotovite, da občutljivi podatki nikoli ne zapustijo lokalne naprave
- Implementirajte varno shranjevanje za AI modele in začasne podatke
- Uporabite varnostne funkcije sistema Windows za peskovnik aplikacij
- Uporabite šifriranje za shranjene modele in vmesne rezultate obdelave

**Varnost modela**
- Preverite integriteto modela pred nalaganjem in izvajanjem
- Implementirajte varne mehanizme posodobitve modela
- Uporabite podpisane modele za preprečitev spreminjanja
- Uporabite kontrolni dostop za datoteke modelov in konfiguracije

### Premisleki skladnosti

**Usklajenost z regulativo**
- Oblikujte aplikacije za skladnost z GDPR, HIPAA in drugimi regulativami
- Implementirajte beleženje revizijskih zapisov za AI odločitvene procese
- Zagotovite funkcije preglednosti za rezultate, ki jih generira AI
- Omogočite nadzor uporabnikov nad obdelavo AI podatkov

**Varnost podjetij**
- Integrirajte z varnostnimi politikami podjetij Windows
- Podpirajte upravljano nameščanje preko orodij za poslovno upravljanje
- Implementirajte kontrole dostopa, ki temeljijo na vlogah za AI funkcije
- Zagotovite administratorske kontrole za AI funkcionalnosti

## Odpravljanje težav in razhroščevanje

### Pogoste razvojne težave

**Težave s konfiguracijo gradnje**
- Zagotovite konfiguracijo platforme ARM64 za vzorce Windows AI API-jev
- Preverite združljivost različice Windows App SDK (zahtevana 1.8.1+)
- Preverite pravilno konfiguracijo identitete paketa (zahtevano za Windows AI API-je)
- Validirajte podporo orodij za gradnjo različici ciljnega okvira

**Težave pri nalaganju modelov**
- Validirajte združljivost ONNX modelov z Windows ML
- Preverite integriteto datotek modelov in zahteve formata
- Preverite zahteve strojne zmogljivosti za specifične modele
- Razširite napake pri dodeljevanju pomnilnika med nalaganjem modela
- Zagotovite registracijo izvajalskega ponudnika za pospešitev strojne opreme

**Premisleki glede načina nameščanja**
- **Način brez odvisnosti (Self-Contained)**: Popolnoma podprt z večjo velikostjo namestitve
- **Način, odvisen od ogrodja (Framework-Dependent)**: Manjši odtis, a zahteva skupni runtime
- **Nenamestljive aplikacije (Unpackaged Applications)**: Ni več podprto za Windows AI API-je
- Uporabite `dotnet run -p:Platform=ARM64 -p:SelfContained=true` za samostojno ARM64 namestitev

**Težave z zmogljivostjo**
- Profilirajte zmogljivost aplikacij na različnih konfiguracijah strojne opreme
- Prepoznajte ozka grla v AI obdelovalnih cevovodih
- Optimizirajte predobdelavo in poobdelavo podatkov
- Implementirajte spremljanje zmogljivosti in opozarjanje

**Težave z integracijo**
- Razhroščujte težave z integracijo API z ustrezno obravnavo napak
- Validirajte formate vhodnih podatkov in zahteve za predobdelavo
- Temeljito testirajte robne primere in pogoje napak
- Implementirajte obsežno beleženje za razhroščevanje produkcijskih težav

### Orodja in tehnike za razhroščevanje

**Integracija z Visual Studiom**
- Uporabite razhroščevalnik AI Toolkita za analizo izvajanja modelov
- Implementirajte profiliranje zmogljivosti AI operacij
- Razhroščujte asinhrone AI operacije z ustrezno obravnavo izjem
- Uporabite orodja za profiliranje pomnilnika za optimizacijo

**Orodja Windows AI Foundry**
- Uporabite Foundry Local CLI za testiranje in validacijo modelov
- Uporabite orodja za testiranje Windows AI API-jev za preverjanje integracije
- Implementirajte prilagojeno beleženje za spremljanje AI operacij
- Ustvarite avtomatizirano testiranje za zanesljivost AI funkcionalnosti

## Priprava vaših aplikacij na prihodnost

### Naraščajoče tehnologije

**Strojna oprema naslednje generacije**
- Oblikujte aplikacije za izkoriščanje prihodnjih zmogljivosti NPU
- Načrtujte za povečane velikosti in kompleksnost modelov
- Implementirajte prilagodljive arhitekture za razvijajočo se strojno opremo
- Razmislite o kvantno-pripravljenih algoritmih za prihodnjo združljivost

**Napredne AI zmožnosti**
- Pripravite se na multimodalno AI integracijo med različnimi vrstami podatkov
- Načrtujte za sodelovalni AI v realnem času med več napravami
- Oblikujte za federativno učenje
- Razmislite o hibridnih arhitekturah rob-oblak inteligence

### Neprestano učenje in prilagajanje

**Posodobitve modelov**
- Implementirajte tekoče mehanizme posodobitev modelov
- Oblikujte aplikacije, ki se prilagajajo izboljšanim zmožnostim modelov
- Načrtujte združljivost nazaj z obstoječimi modeli
- Implementirajte A/B testiranje za vrednotenje zmogljivosti modelov

**Razvoj funkcij**
- Oblikujte modularne arhitekture, ki podpirajo nove AI zmogljivosti
- Načrtujte integracijo naraščajočih Windows AI API-jev
- Implementirajte signalizacijo funkcij za postopni uvod zmožnosti
- Oblikujte uporabniške vmesnike, ki se prilagajajo izboljšanim AI funkcijam

## Zaključek

Razvoj Windows Edge AI predstavlja združitev zmogljivih AI zmožnosti z robustno, varno in skalabilno Windows platformo. Z obvladovanjem ekosistema Windows AI Foundry lahko razvijalci ustvarjajo inteligentne aplikacije, ki nudijo izjemne uporabniške izkušnje ob ohranjanju najvišjih standardov zasebnosti, varnosti in zmogljivosti.

Kombinacija Windows AI API-jev, Foundry Local in Windows ML nudi neprimerljivo osnovo za gradnjo naslednje generacije inteligentnih Windows aplikacij. Ker AI še naprej napreduje, Windows platforma zagotavlja, da se vaše aplikacije skalirajo z novimi tehnologijami ob ohranjanju združljivosti in zmogljivosti skozi raznoliko Windows strojno opremo.

Ne glede na to, ali gradite potrošniške aplikacije, podjetniške rešitve ali specializirana industrijska orodja, vam razvoj Windows Edge AI omogoča ustvarjanje inteligentnih, odzivnih in globoko integriranih izkušenj, ki izkoriščajo polni potencial sodobnih Windows naprav.

## Dodatni viri

### Dokumentacija in učenje
- [Windows AI Foundry dokumentacija](https://learn.microsoft.com/windows/ai/)
- [Referenca Windows AI API-jev](https://learn.microsoft.com/windows/ai/apis/)
- [Začnite z gradnjo aplikacije z Windows AI API-ji](https://learn.microsoft.com/windows/ai/apis/model-setup)
- [Začetek dela z Foundry Local](https://learn.microsoft.com/windows/ai/foundry-local/get-started/)
- [Pregled Windows ML](https://learn.microsoft.com/windows/ai/new-windows-ml/overview/)
- [Sistemske zahteve Windows App SDK](https://docs.microsoft.com/windows/apps/windows-app-sdk/system-requirements)

- [Nastavitev razvojnega okolja za Windows App SDK](https://docs.microsoft.com/windows/apps/windows-app-sdk/set-up-your-development-environment)
- 

### Primeri repozitorijev in kode
- [Primeri Windows App SDK - Windows AI Foundry](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsAIFoundry)
- [Primeri Windows App SDK - Windows ML](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML)
- [Primeri ONNX Runtime Inference](https://github.com/microsoft/onnxruntime-inference-examples)
- [Repozitorij primerov Windows App SDK](https://github.com/microsoft/WindowsAppSDK-Samples)

### Razvojna orodja
- [AI orodjarna za Visual Studio Code](https://learn.microsoft.com/windows/ai/toolkit/)
- [AI Dev galerija](https://learn.microsoft.com/windows/ai/ai-dev-gallery/)
- [Primeri Windows AI](https://learn.microsoft.com/windows/ai/samples/)
- [Orodja za pretvorbo modelov](https://code.visualstudio.com/docs/intelligentapps/modelconversion)

### Tehnična podpora
- [Dokumentacija Windows ML](https://learn.microsoft.com/windows/ai/new-windows-ml/overview)
- [Dokumentacija ONNX Runtime](https://onnxruntime.ai/docs/)
- [Dokumentacija Windows App SDK](https://docs.microsoft.com/windows/apps/windows-app-sdk/)
- [Poročanje o težavah - Primeri Windows App SDK](https://github.com/microsoft/WindowsAppSDK-Samples/issues)

### Skupnost in podpora
- [Skupnost razvijalcev za Windows](https://developer.microsoft.com/en-us/windows/)
- [Windows AI Foundry Blog](https://blogs.windows.com/windowsdeveloper/)
- [Microsoft Learn AI usposabljanje](https://learn.microsoft.com/training/browse/?products=windows&subjects=artificial-intelligence)

---

*Ta vodnik je zasnovan tako, da se razvija skupaj z hitro napredujočim ekosistemom Windows AI. Redne posodobitve zagotavljajo usklajenost z najnovejšimi zmožnostmi platforme in najboljšimi praksami razvoja.*

[08. Praktično delo z Microsoft Foundry Local - Celotna orodjarna za razvijalce](../Module08/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
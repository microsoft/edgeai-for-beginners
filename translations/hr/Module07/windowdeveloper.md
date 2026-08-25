# Vodič za razvoj Windows Edge AI

## Uvod

Dobrodošli u Windows Edge AI razvoj - vaš sveobuhvatni vodič za izgradnju inteligentnih aplikacija koje koriste snagu AI-a na uređaju putem Microsoftove platforme Windows AI Foundry. Ovaj vodič je posebno dizajniran za Windows programere koji žele integrirati najsuvremenije Edge AI mogućnosti u svoje aplikacije, koristeći puni spektar hardverskog ubrzanja Windowsa.

### Prednost Windows AI-ja

Windows AI Foundry predstavlja jedinstvenu, pouzdanu i sigurnu platformu koja podržava cjelokupni razvojni ciklus AI-ja - od odabira i fino podešavanja modela do optimizacije i implementacije na CPU, GPU, NPU i hibridnim cloud arhitekturama. Ova platforma demokratizira razvoj AI-ja omogućujući:

- **Hardverska apstrakcija**: Besprijekorna implementacija na AMD, Intel, NVIDIA i Qualcomm čipovima
- **Inteligencija na uređaju**: AI koja čuva privatnost i u potpunosti radi na lokalnom hardveru
- **Optimizirana izvedba**: Modeli prethodno optimizirani za Windows hardverske konfiguracije
- **Spremnost za poduzeća**: Sigurnosne i usklađene značajke proizvodne klase

### Windows ML
Windows Machine Learning (ML) omogućuje C#, C++ i Python programerima da na lokalnim Windows računalima pokreću ONNX AI modele preko ONNX Runtimea, s automatskim upravljanjem izvršnim providerima za različiti hardver (CPU, GPU, NPU). [ONNX Runtime](https://onnxruntime.ai/docs/) može se koristiti s modelima iz PyTorch, Tensorflow/Keras, TFLite, scikit-learn i drugih okvira.


![WindowsML Dijagram koji prikazuje ONNX model koji prolazi kroz Windows ML do NPUs, GPUs i CPUs.](https://learn.microsoft.com/en-us/windows/ai/images/winml-diagram.png)

Windows ML pruža zajedničku Windows-wide kopiju ONNX Runtimea, plus mogućnost dinamičkog preuzimanja izvršnih providera (EP).

### Zašto Windows za Edge AI?

**Universalna podrška za hardver**
Windows ML automatski optimizira hardver unutar cijelog Windows ekosustava, osiguravajući optimalnu izvedbu vaših AI aplikacija bez obzira na temeljnu silikonsku arhitekturu.

**Integrirano AI runtime okruženje**
Ugrađeni Windows ML inference engine uklanja složene zahtjeve za postavkama, dopuštajući developerima da se fokusiraju na logiku aplikacije umjesto na infrastrukturu.

**Copilot+ PC optimizacija**
API-ji posebno dizajnirani za sljedeću generaciju Windows uređaja s namjenskim Neural Processing Units (NPU) koji pružaju izvrsnu izvedbu po potrošenom vatu.

**Razvojni ekosustav**
Bogati alati uključujući integraciju u Visual Studio, sveobuhvatnu dokumentaciju i primjere aplikacija koje ubrzavaju razvojne cikluse.

## Ciljevi učenja

Završetkom ovog vodiča za razvoj Windows Edge AI usvojit ćete ključne vještine za izgradnju produkcijski spremnih AI aplikacija na Windows platformi.

### Osnovne tehničke kompetencije

**Majstorstvo Windows AI Foundryja**
- Razumjeti arhitekturu i komponente Windows AI Foundry platforme
- Kretati se kroz cjelokupni razvojni ciklus AI-ja unutar Windows ekosustava
- Implementirati najbolje sigurnosne prakse za AI aplikacije na uređaju
- Optimizirati aplikacije za različite Windows hardverske konfiguracije

**Ekspertiza integracije API-ja**
- Savladati Windows AI API-je za tekst, vid i multimodalne aplikacije
- Implementirati integraciju Phi Silica jezičnog modela za generiranje teksta i rezoniranje
- Postaviti računalni vid koristeći ugrađene API-je za obradu slika
- Prilagoditi unaprijed trenirane modele koristeći LoRA (Low-Rank Adaptation) tehnike

**Foundry Local implementacija**
- Pregledavati, ocjenjivati i implementirati open-source jezične modele koristeći Foundry Local CLI
- Razumjeti optimizaciju i kvantizaciju modela za lokalnu implementaciju
- Implementirati offline AI mogućnosti koje rade bez internet veze
- Upravljati životnim ciklusima modela i ažuriranjima u produkcijskim okruženjima

**Windows ML implementacija**
- Donijeti prilagođene ONNX modele u Windows aplikacije koristeći Windows ML
- Iskoristiti automatsko hardversko ubrzanje kroz CPU, GPU i NPU arhitekture
- Implementirati real-time inferencu uz optimalno korištenje resursa
- Dizajnirati skalabilne AI aplikacije za različite kategorije Windows uređaja

### Vještine razvoja aplikacija

**Cross-platform Windows razvoj**
- Izgraditi AI-pokretane aplikacije koristeći .NET MAUI za univerzalnu Windows implementaciju
- Integrirati AI mogućnosti u Win32, UWP i progresivne web aplikacije
- Implementirati responzivne dizajne korisničkog sučelja koji se prilagođavaju AI procesnim stanjima
- Upravljati asinkronim AI operacijama s pravilnim uzorcima korisničkog iskustva

**Optimizacija performansi**
- Profilirati i optimizirati izvedbu AI inferencije na različitim hardverskim konfiguracijama
- Implementirati učinkovito upravljanje memorijom za velike jezične modele
- Dizajnirati aplikacije koje se elegantno prilagođavaju dostupnim hardverskim mogućnostima
- Primjenjivati strategije keširanja za često korištene AI operacije

**Spremnost za proizvodnju**
- Implementirati sveobuhvatno upravljanje greškama i mehanizme za rezervne opcije
- Dizajnirati telemetriju i nadzor performansi AI aplikacija
- Primjenjivati najbolje sigurnosne prakse za lokalnu pohranu i izvršavanje AI modela
- Planirati strategije implementacije za poslovne i korisničke aplikacije

### Poslovno i strateško razumijevanje

**Arhitektura AI aplikacija**
- Dizajnirati hibridne arhitekture koje optimiziraju procesiranje između lokalnog i cloud AI-ja
- Procijeniti kompromis između veličine modela, točnosti i brzine inferencije
- Planirati podatkovne arhitekture koje održavaju privatnost dok omogućuju inteligenciju
- Implementirati isplativa AI rješenja koja se mogu skalirati s potrebama korisnika

**Pozicioniranje na tržištu**
- Razumjeti konkurentske prednosti Windows-native AI aplikacija
- Identificirati upotrebe gdje AI na uređaju pruža superiorno korisničko iskustvo
- Razviti strategije za izlazak na tržište AI-poboljšanih Windows aplikacija
- Pozicionirati aplikacije za korištenje prednosti Windows ekosustava

## Primjeri Windows App SDK AI-ja

Windows App SDK pruža sveobuhvatne primjere koji demonstriraju AI integraciju kroz više frameworka i scenarija implementacije. Ovi primjeri su ključni referentni materijali za razumijevanje uzoraka razvoja Windows AI-ja.

### Primjeri Windows AI Foundryja

| Primjer | Framework | Područje fokusa | Ključne značajke |
|--------|-----------|-----------------|------------------|
| [cs-winui](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsAIFoundry/cs-winui) | C# WinUI 3 | Integracija Windows AI API-ja | Potpuna WinUI aplikacija koja demonstrira Windows AI api-je, ARM64 optimizaciju, pakiranu implementaciju |

**Ključne tehnologije:**
- Windows AI API-ji
- WinUI 3 framework
- ARM64 platforma optimizacija
- Copilot+ PC kompatibilnost
- Pakirana implementacija aplikacije

**Preduvjeti:**
- Windows 11 s preporučenim Copilot+ PC
- Visual Studio 2022
- ARM64 konfiguracija za build
- Windows App SDK 1.8.1+

### Primjeri Windows ML-a

#### C++ primjeri

| Primjer | Tip | Područje fokusa | Ključne značajke |
|--------|-----|-----------------|------------------|
| [CppConsoleDesktop](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Konzolna aplikacija | Osnovni Windows ML | Otkrivanje EP, opcije naredbenog retka, kompajliranje modela |
| [CppConsoleDesktop.FrameworkDependent](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Konzolna aplikacija | Implementacija frameworka | Dijeljeni runtime, manji otisak implementacije |
| [CppConsoleDesktop.SelfContained](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Konzolna aplikacija | Samostalna implementacija | Samostalna implementacija, bez runtime ovisnosti |
| [CppConsoleDll](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | DLL | Korištenje biblioteke | WindowsML u dijeljenoj biblioteci, upravljanje memorijom |
| [CppResnetBuildDemo](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Demo | ResNet tutorijal | Konverzija modela, EP kompajliranje, Build 2025 tutorijal |

#### C# primjeri

**Konzolne aplikacije**

| Primjer | Tip | Područje fokusa | Ključne značajke |
|--------|-----|-----------------|------------------|
| [CSharpConsoleDesktop](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs) | Konzolna aplikacija | Osnovna C# integracija | Korištenje dijeljenih pomoćnika, sučelje naredbenog retka |
| [ResnetBuildDemoCS](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs) | Demo | ResNet tutorijal | Konverzija modela, EP kompajliranje, Build 2025 tutorijal |

**GUI aplikacije**

| Primjer | Framework | Područje fokusa | Ključne značajke |
|--------|-----------|-----------------|------------------|
| [cs-wpf](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs-wpf) | WPF | Desktop GUI | Klasifikacija slika s WPF sučeljem |
| [cs-winforms](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs-winforms) | Windows Forms | Tradicionalno GUI | Klasifikacija slika s Windows Forms |
| [cs-winui](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs-winui) | WinUI 3 | Moderno GUI | Klasifikacija slika s WinUI 3 sučeljem |

#### Python primjeri

| Primjer | Jezik | Područje fokusa | Ključne značajke |
|--------|-------|-----------------|------------------|
| [SqueezeNetPython](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/python) | Python | Klasifikacija slika | WinML Python bindings, obrada skupnih slika |

### Preduvjeti za primjere

**Sistemski zahtjevi:**
- Windows 11 PC s verzijom 24H2 (build 26100) ili novijom
- Visual Studio 2022 s C++ i .NET radnim opterećenjima
- Windows App SDK 1.8.1 ili noviji
- Python 3.10-3.13 za Python primjere na x64 i ARM64 uređajima

**Specifično za Windows AI Foundry:**
- Preporučen Copilot+ PC za optimalne performanse
- ARM64 konfiguracija builda za Windows AI primjere
- Potrebni identitet paketa (ne-pakirane aplikacije više nisu podržane)

### Uobičajeni postupak rada s primjerima

Većina Windows ML primjera slijedi ovaj standardni obrazac:

1. **Inicijalizirati okruženje** - Kreirati ONNX Runtime okruženje
2. **Registrirati izvršne providere** - Otkrivanje i registracija dostupnih hardverskih ubrzivača (CPU, GPU, NPU)
3. **Učitati model** - Učitati ONNX model, po potrebi kompajlirati za ciljanu hardversku platformu
4. **Predobrada ulaza** - Pretvoriti slike/podatke u ulazni format modela
5. **Pokrenuti inferencu** - Izvršiti model i dobiti predviđanja
6. **Obraditi rezultate** - Primijeniti softmax i prikazati vodeća predviđanja

### Korištene datoteke modela

| Model | Svrha | Uključen | Napomene |
|-------|--------|---------|----------|
| SqueezeNet | Laka klasifikacija slika | ✅ Uključen | Pretreniran, spreman za korištenje |
| ResNet-50 | Klasifikacija slika visoke točnosti | ❌ Potrebna konverzija | Koristiti [AI Toolkit](https://code.visualstudio.com/docs/intelligentapps/modelconversion) za konverziju |

### Podrška za hardver

Svi primjeri automatski otkrivaju i koriste dostupni hardver:
- **CPU** - Univerzalna podrška na svim Windows uređajima
- **GPU** - Automatsko otkrivanje i optimizacija za dostupni grafički hardver
- **NPU** - Iskorištava Neural Processing Units na podržanim uređajima (Copilot+ PC-ima)

## Komponente Windows AI Foundry platforme

### 1. Windows AI API-ji

Windows AI API-ji pružaju spremne AI mogućnosti pokretane modelima na uređaju, optimizirane za učinkovitost i performanse na Copilot+ PC uređajima s minimalnim potrebnim postavkama.

#### Osnovne kategorije API-ja

**Phi Silica jezični model**
- Mali ali moćan jezični model za generiranje teksta i rezoniranje
- Optimiziran za real-time inferencu s minimalnom potrošnjom energije
- Podrška za prilagođeno fino podešavanje korištenjem LoRA tehnika
- Integracija s Windows semantičkim pretraživanjem i dohvatom znanja

**API-ji za računalni vid**
- **Prepoznavanje teksta (OCR)**: Izvlačenje teksta iz slika s visokom točnošću
- **Povećanje razlučivosti slike**: Uvećavanje slika korištenjem lokalnih AI modela
- **Segmentacija slike**: Identifikacija i izdvajanje specifičnih objekata na slikama
- **Opis slike**: Generiranje detaljnih tekstualnih opisa za vizualni sadržaj
- **Brisanje objekata**: Uklanjanje neželjenih objekata sa slika uz AI-pokretano ispunjavanje

**Multimodalne mogućnosti**
- **Integracija vida i jezika**: Kombiniranje razumijevanja teksta i slike
- **Semantičko pretraživanje**: Omogućavanje upita prirodnim jezikom preko multimedijalnog sadržaja
- **Dohvat znanja**: Izgradnja inteligentnih iskustava pretraživanja uz lokalne podatke

### 2. Foundry Local

Foundry Local programerima pruža brz pristup spremnim open-source jezičnim modelima na Windows Siliconu, nudeći mogućnost pretraživanja, testiranja, interakcije i implementacije modela u lokalne aplikacije.

#### Primjerni projekti Foundry Locala

[Foundry Local repozitorij](https://github.com/microsoft/Foundry-Local/tree/main/samples) pruža opsežne primjere na različitim programskim jezicima i frameworkima, demonstrirajući različite obrasce integracije i upotrebe.

| Primjer | Jezik/Framework | Područje fokusa | Ključne značajke |
|--------|-----------------|-----------------|------------------|
| [dotNET/rag](https://github.com/microsoft/Foundry-Local/tree/main/samples/dotNET/rag) | C# / .NET | RAG implementacija | Integracija Semantic Kernel-a, Qdrant pohrana vektora, JINA embeddings, unos dokumenata, streaming chat |
| [electron/foundry-chat](https://github.com/microsoft/Foundry-Local/tree/main/samples/electron/foundry-chat) | JavaScript / Electron | Desktop chat aplikacija | Cross-platform chat, lokalna/cloud promjena modela, OpenAI SDK integracija, streaming u realnom vremenu |
| [js/hello-foundry-local](https://github.com/microsoft/Foundry-Local/tree/main/samples/js/hello-foundry-local) | JavaScript / Node.js | Osnovna integracija | Jednostavna SDK upotreba, inicijalizacija modela, osnovna chat funkcionalnost |
| [python/hello-foundry-local](https://github.com/microsoft/Foundry-Local/tree/main/samples/python/hello-foundry-local) | Python | Osnovna integracija | Python SDK upotreba, streaming odgovora, OpenAI kompatibilan API |

| [rust/hello-foundry-local](https://github.com/microsoft/Foundry-Local/tree/main/samples/rust/hello-foundry-local) | Rust | Integracija sustava | Korištenje SDK-a na niskoj razini, async operacije, reqwest HTTP klijent |

#### Kategorije uzoraka prema namjeni

**RAG (Generiranje uz pomoć pretraživanja)**
- **dotNET/rag**: Potpuna RAG implementacija koristeći Semantic Kernel, Qdrant vektorsku bazu podataka i JINA ugradnje
- **Arhitektura**: Unos dokumenata → Dijeljenje teksta → Vektorske ugradnje → Pretraživanje sličnosti → Odgovori svjesni konteksta
- **Tehnologije**: Microsoft.SemanticKernel, Qdrant.Client, BERT ONNX ugradnje, streaming chat dovršavanja

**Desktop aplikacije**
- **electron/foundry-chat**: Chat aplikacija spremna za produkciju s lokalnim/oblačnim prebacivanjem modela
- **Značajke**: Izbor modela, streaming odgovori, rukovanje pogreškama, višestruka platforma za distribuciju
- **Arhitektura**: Electron glavni proces, IPC komunikacija, sigurne preload skripte

**Primjeri integracije SDK-a**
- **JavaScript (Node.js)**: Osnovna interakcija s modelom i streaming odgovori
- **Python**: Korištenje API-ja kompatibilnog s OpenAI-jem s async streamingom
- **Rust**: Integracija na niskoj razini s reqwest i tokio za async operacije

#### Preduvjeti za Foundry Local uzorke

**Sistemski zahtjevi:**
- Windows 11 s instaliranim Foundry Local
- Node.js v16+ za JavaScript/Electron uzorke
- .NET 8.0+ za C# uzorke
- Python 3.10+ za Python uzorke
- Rust 1.70+ za Rust uzorke

**Instalacija:**
```powershell
# Instalirajte Foundry Local
winget install Microsoft.FoundryLocal

# Provjerite instalaciju
foundry --version
foundry model list
```

#### Specifično postavljanje za uzorke

**dotNET RAG uzorak:**
```powershell
# Instalirajte potrebne pakete putem NuGet-a
# Microsoft.SemanticKernel.Connectors.Onnx
# Microsoft.SemanticKernel.Connectors.Qdrant
# Qdrant.Client

# Pokrenite Qdrant vektorsku bazu podataka
docker run -p 6333:6333 qdrant/qdrant

# Pokrenite Jupyter bilježnicu
jupyter notebook rag_foundrylocal_demo.ipynb
```

**Electron Chat uzorak:**
```powershell
# Postavi varijable okruženja za cloud fallback
$env:YOUR_API_KEY="your-cloud-api-key"
$env:YOUR_ENDPOINT="your-cloud-endpoint"
$env:YOUR_MODEL_NAME="your-cloud-model"

# Instaliraj ovisnosti i pokreni
npm install
npm start
```

**JavaScript/Python/Rust uzorci:**
```powershell
# Preuzmi model (primjer s phi-3.5-mini)
foundry model run phi-3.5-mini

# Pokreni odgovarajući uzorak
node src/app.js          # JavaScript
python src/app.py        # Python
cargo run               # Rust
```

#### Ključne značajke

**Katalog modela**
- Sveobuhvatna kolekcija unaprijed optimiziranih open-source modela
- Modeli optimizirani za CPU, GPU i NPU za trenutnu uporabu
- Podrška za popularne obitelji modela uključujući Llama, Mistral, Phi i specijalizirane domenske modele

**CLI integracija**
- Sučelje naredbenog retka za upravljanje i distribuciju modela
- Automatizirani tijekovi optimizacije i kvantizacije
- Integracija s popularnim razvojim okruženjima i CI/CD cjevovodima

**Lokalna implementacija**
- Potpuno offline djelovanje bez ovisnosti o oblaku
- Podrška za prilagođene formate i konfiguracije modela
- Efikasno posluživanje modela s automatskom optimizacijom hardvera

### 3. Windows ML

Windows ML služi kao osnovna AI platforma i integrirano izvršno okruženje za inferenciju na Windowsima, omogućujući programerima učinkovitu implementaciju prilagođenih modela kroz širok hardverski ekosustav Windowsa.

#### Prednosti arhitekture

**Univerzalna podrška hardvera**
- Automatska optimizacija za AMD, Intel, NVIDIA i Qualcomm silicije
- Podrška za izvođenje na CPU, GPU i NPU s transparentnim prebacivanjem
- Apsktrakcija hardvera koja uklanja potrebu za optimizacijom specifičnom za platformu

**Fleksibilnost modela**
- Podrška za ONNX format modela s automatskom konverzijom iz popularnih okvira
- Prilagođena distribucija modela s proizvodnom izvedbom
- Integracija s postojećim arhitekturama Windows aplikacija

**Integracija u poduzeća**
- Kompatibilno s Windows sigurnosnim i usklađljivim okvirima
- Podrška za alate za implementaciju i upravljanje u poduzećima
- Integracija s Windows sustavima za upravljanje i nadzor uređaja

## Razvojni tijek rada

### Faza 1: Postavljanje okruženja i konfiguracija alata

**Priprema razvojnog okruženja**
1. Instalirajte Visual Studio 2022 s C++ i .NET radnim opterećenjima
2. Instalirajte Windows App SDK 1.8.1 ili noviji
3. Konfigurirajte Windows AI Foundry CLI alate
4. Postavite AI Toolkit proširenje za Visual Studio Code
5. Uspostavite alate za profiliranje izvedbe i nadzor
6. Osigurajte konfiguraciju za ARM64 build za optimizaciju Copilot+ PC-a

**Postavljanje repozitorija uzoraka**
1. Klonirajte [Windows App SDK Samples repozitorij](https://github.com/microsoft/WindowsAppSDK-Samples)
2. Idite na `Samples/WindowsAIFoundry/cs-winui` za primjere Windows AI API-ja
3. Idite na `Samples/WindowsML` za opsežne Windows ML uzorke
4. Pregledajte [zahtjeve za build](https://learn.microsoft.com/windows/apps/windows-app-sdk/system-requirements) za željene platforme

**Istraživanje AI Dev galerije**
- Istražite uzorke aplikacija i referentne implementacije
- Testirajte Windows AI API-je s interaktivnim demonstracijama
- Pregledajte izvorni kod za najbolje prakse i uzorke
- Identificirajte relevantne uzorke za vaš specifični slučaj uporabe

### Faza 2: Izbor modela i integracija

**Analiza zahtjeva**
- Definirajte funkcionalne zahtjeve za AI mogućnosti
- Utvrdite ograničenja izvedbe i ciljeve optimizacije
- Procijenite zahtjeve za privatnost i sigurnost
- Planirajte arhitekturu implementacije i strategije skaliranja

**Evaluacija modela**
- Iskoristite Foundry Local za testiranje open-source modela za vašu uporabu
- Benchmarkajte Windows AI API-je u odnosu na zahtjeve prilagođenih modela
- Procijenite kompromise između veličine modela, točnosti i brzine izvršavanja
- Prototipirajte pristupe integraciji odabranih modela

### Faza 3: Razvoj aplikacije

**Osnovna integracija**
- Implementirajte integraciju Windows AI API-ja s odgovarajućim rukovanjem pogreškama
- Dizajnirajte korisnička sučelja prilagođena tijekovima obrade AI-a
- Implementirajte strategije keširanja i optimizacije za izvođenje modela
- Dodajte telemetriju i nadzor za performanse AI operacija

**Testiranje i validacija**
- Testirajte aplikacije na različitim Windows hardverskim konfiguracijama
- Validirajte metrike izvedbe pod različitim opterećenjima
- Implementirajte automatizirano testiranje pouzdanosti AI funkcionalnosti
- Provedite testiranje korisničkog iskustva s AI poboljšanim značajkama

### Faza 4: Optimizacija i implementacija

**Optimizacija izvedbe**
- Profilirajte izvedbu aplikacije na ciljanim hardverskim konfiguracijama
- Optimizirajte korištenje memorije i strategije učitavanja modela
- Implementirajte adaptivno ponašanje prema dostupnim hardverskim mogućnostima
- Fino podesite korisničko iskustvo za različite scenarije izvedbe

**Produkcijska implementacija**
- Paketirajte aplikacije s odgovarajućim AI model ovisnostima
- Implementirajte mehanizme ažuriranja modela i poslovne logike aplikacije
- Konfigurirajte nadzor i analitiku za produkcijska okruženja
- Planirajte strategije uvođenja za poduzeća i krajnje korisnike

## Praktični primjeri implementacije

### Primjer 1: Aplikacija za inteligentnu obradu dokumenata

Izradite Windows aplikaciju koja obrađuje dokumente koristeći više AI mogućnosti:

**Korištene tehnologije:**
- Phi Silica za sažimanje dokumenata i odgovore na pitanja
- OCR API-je za ekstrakciju teksta iz skeniranih dokumenata
- API-je za opis slike za analizu grafikona i dijagrama
- Prilagođeni ONNX modeli za klasifikaciju dokumenata

**Pristup implementaciji:**
- Dizajnirajte modularnu arhitekturu s uklonjivim AI komponentama
- Implementirajte async obradu za velike količine dokumenata
- Dodajte indikatore napretka i podršku za otkazivanje dugotrajnih operacija
- Uključite offline mogućnosti za osjetljivu obradu dokumenata

### Primjer 2: Sustav upravljanja zalihama za maloprodaju

Izradite AI-podržani sustav zaliha za maloprodajne aplikacije:

**Korištene tehnologije:**
- Segmentacija slike za identifikaciju proizvoda
- Prilagođeni vizualni modeli za klasifikaciju branda i kategorije
- Foundry Local implementacija specijaliziranih modela jezika za maloprodaju
- Integracija s postojećim POS i sustavima zaliha

**Pristup implementaciji:**
- Izradite integraciju kamera za skeniranje proizvoda u stvarnom vremenu
- Implementirajte prepoznavanje barkoda i vizualnih značajki proizvoda
- Dodajte upite zalihama prirodnim jezikom koristeći lokalne jezične modele
- Dizajnirajte skalabilnu arhitekturu za implementaciju u više trgovina

### Primjer 3: Asistent za zdravstvenu dokumentaciju

Razvijte alat za zdravstvenu dokumentaciju koji poštuje privatnost:

**Korištene tehnologije:**
- Phi Silica za generiranje medicinskih bilješki i potporu kliničkim odlukama
- OCR za digitalizaciju rukom pisanih medicinskih zapisa
- Prilagođeni medicinski jezični modeli implementirani preko Windows ML
- Lokalno pohranjivanje vektora za dohvat medicinskog znanja

**Pristup implementaciji:**
- Osigurajte potpuno offline djelovanje za privatnost pacijenata
- Implementirajte validaciju i sugestije medicinske terminologije
- Dodajte zapisivanje revizije za usklađenost s propisima
- Dizajnirajte integraciju s postojećim sustavima elektroničkih zdravstvenih zapisa

## Strategije optimizacije izvedbe

### Razvoj svjestan hardvera

**NPU optimizacija**
- Dizajnirajte aplikacije koje koriste NPU mogućnosti na Copilot+ PC-ima
- Implementirajte prikladno vraćanje na GPU/CPU na uređajima bez NPU
- Optimizirajte formate modela za ubrzanja specifična za NPU
- Nadzirite iskorištenost NPU i termalne karakteristike

**Upravljanje memorijom**
- Implementirajte efikasno učitavanje i keširanje modela
- Koristite mapiranje memorije za velike modele kako biste smanjili vrijeme pokretanja
- Dizajnirajte memorijski štedljive aplikacije za uređaje s ograničenim resursima
- Implementirajte kvantizaciju modela radi optimizacije memorije

**Učinkovitost baterije**
- Optimizirajte AI operacije za minimalnu potrošnju energije
- Implementirajte adaptivnu obradu ovisno o stanju baterije
- Dizajnirajte učinkovitu pozadinsku obradu za kontinuirane AI operacije
- Koristite alate za profiliranje potrošnje energije za optimizaciju

### Razmatranja skalabilnosti

**Višestruko višestruko izvršavanje (multi-threading)**
- Dizajnirajte thread-safe AI operacije za istodobnu obradu
- Implementirajte učinkovitu raspodjelu rada među raspoloživim jezgrama
- Koristite async/await obrasce za neblokirajuće AI operacije
- Planirajte optimizaciju thread pool-a za različite hardverske konfiguracije

**Strategije keširanja**
- Implementirajte inteligentno keširanje za često korištene AI operacije
- Dizajnirajte strategije kašnjenja isteka keša za ažuriranja modela
- Koristite trajno keširanje za skupe predprocesne operacije
- Implementirajte distribuirano keširanje za višekorisničke scenarije

## Najbolje prakse sigurnosti i privatnosti

### Zaštita podataka

**Lokalna obrada**
- Osigurajte da osjetljivi podaci nikada ne napuste lokalni uređaj
- Implementirajte sigurnu pohranu za AI modele i privremene podatke
- Koristite sigurnosne značajke Windowsa za sandboxing aplikacija
- Primijenite enkripciju za pohranjene modele i rezultate izmeđuobrađivanja

**Sigurnost modela**
- Validirajte integritet modela prije učitavanja i izvršavanja
- Implementirajte sigurne mehanizme ažuriranja modela
- Koristite potpisane modele za sprječavanje manipulacije
- Primijenite kontrole pristupa za modele i konfiguracijske datoteke

### Usklađenost s propisima

**Usklađenost s pravilima**
- Dizajnirajte aplikacije u skladu s GDPR, HIPAA i drugim regulatornim zahtjevima
- Implementirajte audit loge za procese donošenja AI odluka
- Omogućite značajke transparentnosti za AI-generirane rezultate
- Dajte korisnicima kontrolu nad obradom AI podataka

**Sigurnost u poduzećima**
- Integrirajte se sa sigurnosnim politikama Windows poduzeća
- Podrška za upravljanu distribuciju putem enterprise upravljačkih alata
- Implementirajte kontrole pristupa temeljene na ulogama za AI značajke
- Omogućite administrativne kontrole za AI funkcionalnosti

## Rješavanje problema i otklanjanje pogrešaka

### Uobičajeni razvojni izazovi

**Problemi s konfiguracijom builda**
- Osigurajte konfiguraciju platforme ARM64 za Windows AI API uzorke
- Provjerite kompatibilnost verzije Windows App SDK-a (1.8.1+ obavezno)
- Provjerite pravilnu konfiguraciju identiteta paketa (potrebno za Windows AI API-je)
- Validirajte da alati za build podržavaju ciljanu verziju frameworka

**Problemi s učitavanjem modela**
- Validirajte kompatibilnost ONNX modela s Windows ML
- Provjerite integritet datoteke modela i zahtjeve formata
- Provjerite hardverske zahtjeve za specifične modele
- Debugirajte probleme s alokacijom memorije tijekom učitavanja modela
- Osigurajte registraciju izvršnog pružatelja za ubrzanje hardvera

**Razmatranja načina implementacije**
- **Self-Contained način**: Potpuno podržan s većom veličinom implementacije
- **Framework-Dependent način**: Manji otisak, ali zahtijeva zajedničko izvršno okruženje
- **Neupakirane aplikacije**: Više nisu podržane za Windows AI API-je
- Koristite `dotnet run -p:Platform=ARM64 -p:SelfContained=true` za samostalnu ARM64 implementaciju

**Problemi s izvedbom**
- Profilirajte izvedbu aplikacije kroz različite hardverske konfiguracije
- Identificirajte uska grla u AI obradbenim pipelinovima
- Optimizirajte operacije pred- i postprocesiranja podataka
- Implementirajte nadzor izvedbe i obavještavanje

**Poteškoće integracije**
- Debugirajte probleme u integraciji API-ja s pravilnim rukovanjem pogreškama
- Validirajte formate ulaznih podataka i zahtjeve predprocesiranja
- Temeljito testirajte rubne slučajeve i stanja pogrešaka
- Implementirajte opsežno logiranje za otklanjanje pogrešaka u produkciji

### Alati i tehnike za otklanjanje pogrešaka

**Integracija s Visual Studiom**
- Koristite AI Toolkit debugger za analizu izvršavanja modela
- Implementirajte profiliranje izvedbe za AI operacije
- Debugirajte async AI operacije s odgovarajućim rukovanjem iznimkama
- Koristite alate za profiliranje memorije za optimizaciju

**Windows AI Foundry alati**
- Iskoristite Foundry Local CLI za testiranje i validaciju modela
- Koristite alate za testiranje Windows AI API-ja za provjeru integracije
- Implementirajte prilagođeno logiranje za nadzor AI operacija
- Kreirajte automatizirano testiranje za pouzdanost AI funkcionalnosti

## Osiguravanje budućnosti vaših aplikacija

### Nastajuće tehnologije

**Hardver sljedeće generacije**
- Dizajnirajte aplikacije za iskorištavanje budućih mogućnosti NPU-a
- Planirajte povećanje veličine i složenosti modela
- Implementirajte adaptivne arhitekture za razvoj hardvera
- Razmotrite kvantne algoritme za buduću kompatibilnost

**Napredne AI mogućnosti**
- Pripremite se za multimodalnu AI integraciju kroz više tipova podataka
- Planirajte za suradnički AI u stvarnom vremenu između više uređaja
- Dizajnirajte za sposobnosti federiranog učenja
- Razmotrite hibridne edge-cloud inteligentne arhitekture

### Kontinuirano učenje i prilagodba

**Ažuriranja modela**
- Implementirajte besprijekorne mehanizme ažuriranja modela
- Dizajnirajte aplikacije da se prilagođavaju poboljšanim mogućnostima modela
- Planirajte unatrag kompatibilnost s postojećim modelima
- Implementirajte A/B testiranje za evaluaciju izvedbe modela

**Evolucija značajki**
- Dizajnirajte modularne arhitekture koje podržavaju nove AI mogućnosti
- Planirajte integraciju nadolazećih Windows AI API-ja
- Implementirajte značajke za postupno uvođenje mogućnosti
- Dizajnirajte korisnička sučelja koja se prilagođavaju poboljšanim AI značajkama

## Zaključak

Windows Edge AI razvoj predstavlja spajanje moćnih AI sposobnosti s robusnom, sigurnom i skalabilnom Windows platformom. Usvajanjem Windows AI Foundry ekosustava, programeri mogu stvarati inteligentne aplikacije koje pružaju izvanredno korisničko iskustvo uz održavanje najviših standarda privatnosti, sigurnosti i izvedbe.

Kombinacija Windows AI API-ja, Foundry Local-a i Windows ML-a pruža nenadmašnu osnovu za izradu nove generacije inteligentnih Windows aplikacija. Kako se AI stalno razvija, Windows platforma osigurava da vaše aplikacije skaliraju s nastajućim tehnologijama uz održavanje kompatibilnosti i performansi kroz raznovrstan hardverski ekosustav Windowsa.

Bilo da gradite aplikacije za krajnje korisnike, poduzeća ili specijalizirane industrijske alate, Windows Edge AI razvoj omogućuje vam stvaranje inteligentnih, responzivnih i duboko integriranih iskustava koja koriste puni potencijal modernih Windows uređaja.

## Dodatni resursi

### Dokumentacija i učenje
- [Windows AI Foundry Dokumentacija](https://learn.microsoft.com/windows/ai/)
- [Windows AI API Referenca](https://learn.microsoft.com/windows/ai/apis/)
- [Počnite graditi aplikaciju s Windows AI API-jima](https://learn.microsoft.com/windows/ai/apis/model-setup)
- [Foundry Local Početak rada](https://learn.microsoft.com/windows/ai/foundry-local/get-started/)
- [Pregled Windows ML](https://learn.microsoft.com/windows/ai/new-windows-ml/overview/)
- [Zahtjevi sustava za Windows App SDK](https://docs.microsoft.com/windows/apps/windows-app-sdk/system-requirements)

- [Windows App SDK Postavljanje Razvojnog Okruženja](https://docs.microsoft.com/windows/apps/windows-app-sdk/set-up-your-development-environment)
- 

### Primjer spremišta i koda
- [Windows App SDK Primjeri - Windows AI Foundry](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsAIFoundry)
- [Windows App SDK Primjeri - Windows ML](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML)
- [ONNX Runtime Primjeri izvođenja](https://github.com/microsoft/onnxruntime-inference-examples)
- [Windows App SDK Primjeri Spremište](https://github.com/microsoft/WindowsAppSDK-Samples)

### Alati za razvoj
- [AI Alatni komplet za Visual Studio Code](https://learn.microsoft.com/windows/ai/toolkit/)
- [AI Dev Galerija](https://learn.microsoft.com/windows/ai/ai-dev-gallery/)
- [Windows AI Primjeri](https://learn.microsoft.com/windows/ai/samples/)
- [Alati za pretvorbu modela](https://code.visualstudio.com/docs/intelligentapps/modelconversion)

### Tehnička podrška
- [Windows ML Dokumentacija](https://learn.microsoft.com/windows/ai/new-windows-ml/overview)
- [ONNX Runtime Dokumentacija](https://onnxruntime.ai/docs/)
- [Windows App SDK Dokumentacija](https://docs.microsoft.com/windows/apps/windows-app-sdk/)
- [Prijavi probleme - Windows App SDK Primjeri](https://github.com/microsoft/WindowsAppSDK-Samples/issues)

### Zajednica i podrška
- [Windows Razvojna Zajednica](https://developer.microsoft.com/en-us/windows/)
- [Windows AI Foundry Blog](https://blogs.windows.com/windowsdeveloper/)
- [Microsoft Learn AI Trening](https://learn.microsoft.com/training/browse/?products=windows&subjects=artificial-intelligence)

---

*Ovaj vodič je dizajniran da se razvija s brzo napredujućim Windows AI ekosustavom. Redovita ažuriranja osiguravaju usklađenost s najnovijim mogućnostima platforme i najboljim praksama razvoja.*

[08. Praktični rad s Microsoft Foundry Local - Potpuni razvojni alatni komplet](../Module08/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
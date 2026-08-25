# AI orodjarna za Visual Studio Code - Vodnik za razvoj Edge AI

## Uvod

Dobrodošli v obsežnem vodniku za uporabo AI orodjarne za Visual Studio Code pri razvoju Edge AI. Ker se umetna inteligenca premika iz centraliziranega oblaka na distribuirane robne naprave, razvijalci potrebujejo zmogljiva, integrirana orodja, ki zmorejo obvladati edinstvene izzive robnega nameščanja – od omejitev virov do zahtev po delovanju brez povezave.

AI orodjarna za Visual Studio Code premošča ta razkorak s popolnim razvojnim okoljem, posebej oblikovanim za gradnjo, testiranje in optimizacijo AI aplikacij, ki učinkovito delujejo na robnih napravah. Ne glede na to, ali razvijate za IoT senzorje, mobilne naprave, vgrajene sisteme ali robne strežnike, ta komplet poenostavlja celoten razvojni potek znotraj znanega okolja VS Code.

Ta vodnik vas bo popeljal skozi ključne koncepte, orodja in dobre prakse za učinkovito uporabo AI orodjarne v vaših projektih Edge AI, od začetnega izbora modela do produkcijske uvedbe.

## Pregled

AI orodjarna za Visual Studio Code je zmogljiva razširitev, ki poenostavlja razvoj agentov in kreacijo AI aplikacij. Orodjarna nudi obsežne zmogljivosti za raziskovanje, ocenjevanje in nameščanje AI modelov iz različnih ponudnikov—vključno z Anthropic, OpenAI, GitHub, Google—ter podpira lokalno izvajanje modelov z uporabo ONNX in Ollama.

Kar AI orodjarno loči od drugih, je celosten pristop k celotnemu življenjskemu ciklu razvoja AI. V nasprotju s tradicionalnimi orodji, ki se osredotočajo na posamezne vidike, AI orodjarna zagotavlja integrirano okolje za odkrivanje modelov, eksperimentiranje, razvoj agentov, ocenjevanje in nameščanje—vse znotraj znanega okolja VS Code.

Platforma je posebej zasnovana za hitro prototipiranje in produkcijsko uvedbo z možnostmi, kot so generiranje pozivov, hitri začetki, nemotena integracija z MCP (Model Context Protocol) orodji in obsežne ocenjevalne funkcionalnosti. Za razvoj Edge AI to pomeni, da lahko učinkovito razvijate, testirate in optimizirate AI aplikacije za robna okolja, hkrati pa ohranjate celoten razvojni potek znotraj VS Code.

## Cilji učenja

Ob koncu tega vodnika boste sposobni:

### Temeljne kompetence
- **Namestiti in konfigurirati** AI orodjarno za Visual Studio Code za razvojne poteke Edge AI
- **Upravljati z AI orodjarno** vmesnik, vključno s katalogom modelov, igrališčem in graditeljem agentov
- **Izbrati in oceniti** AI modele, ki so primerni za robno nameščanje glede na zmogljivost in omejitve virov
- **Pretvoriti in optimizirati** modele z uporabo ONNX formata in tehnik kvantizacije za robne naprave

### Spretnosti razvoja Edge AI
- **Načrtovati in izvajati** Edge AI aplikacije z integriranim razvojnim okoljem
- **Izvesti testiranje modelov** v pogojih, podobnih robnim, z lokalnim sklepanjem in spremljanjem virov
- **Ustvariti in prilagoditi** AI agente, optimizirane za scenarije robnega nameščanja
- **Oceniti delovanje modelov** z uporabo metrik, relevantnih za robno računanje (zakasnitev, poraba spomina, natančnost)

### Optimizacija in uvedba
- **Uporabiti tehnike kvantizacije in obrezovanja** za zmanjšanje velikosti modela hkrati s sprejemljivo zmogljivostjo
- **Optimizirati modele** za specifične robne strojne platforme, vključno s pospeševalci CPU, GPU in NPU
- **Uvesti dobre prakse** za razvoj Edge AI, vključno z upravljanjem virov in strategijami za povrnitev
- **Pripraviti modele in aplikacije** za produkcijsko uvedbo na robnih napravah

### Napredni koncepti Edge AI
- **Integrirati z edge AI ogrodji**, vključno z ONNX Runtime, Windows ML in TensorFlow Lite
- **Implementirati večmodelne arhitekture** in scenarije federativnega učenja za robna okolja
- **Odpravljati pogoste težave Edge AI**, vključno z omejitvami spomina, hitrostjo sklepov in združljivostjo strojne opreme
- **Načrtovati strategije spremljanja in beleženja** za Edge AI aplikacije v produkciji

### Praktična uporaba
- **Zgraditi celovite Edge AI rešitve** od izbora modela do uvedbe
- **Demonstrirati veščine** v robno specifičnih razvojnih potekih in optimizacijskih tehnikah
- **Uporabiti naučene koncepte** za realne primere uporabe Edge AI, vključno z IoT, mobilnimi in vgrajenimi aplikacijami
- **Oceniti in primerjati** različne strategije uvedbe Edge AI in njihove kompromise

## Ključne funkcije za razvoj Edge AI

### 1. Katalog modelov in odkrivanje
- **Podpora več ponudnikom**: Brskajte in dostopajte do AI modelov od Anthropic, OpenAI, GitHub, Google in drugih ponudnikov
- **Lokalna integracija modelov**: Poenostavljeno odkrivanje ONNX in Ollama modelov za robno namestitev
- **GitHub modeli**: Neposredna integracija z gostovanjem modelov na GitHub za poenostavljen dostop
- **Primerjava modelov**: Primerjajte modele drug ob drugem za optimalno ravnovesje glede na omejitve robnih naprav

### 2. Interaktivno igrišče
- **Interaktivno testno okolje**: Hitro eksperimentiranje z zmogljivostmi modelov v nadzorovanem okolju
- **Podpora več modalitetam**: Testirajte z slikami, besedilom in drugimi vhodnimi podatki, značilnimi za robne scenarije
- **Eksperimentiranje v realnem času**: Takojšnja povratna informacija o odzivih in zmogljivosti modelov
- **Optimizacija parametrov**: Natančno prilagajanje parametrov modela za zahteve robne uvedbe

### 3. Graditelj pozivov (agentov)
- **Generiranje naravnega jezika**: Ustvarite začetne pozive z uporabo opisov v naravnem jeziku
- **Iterativno izboljševanje**: Izboljšajte pozive na podlagi odzivov in zmogljivosti modela
- **Razčlenitev nalog**: Razbijte kompleksne naloge z verižnim pozivanjem in strukturiranimi izhodi
- **Podpora spremenljivkam**: Uporabite spremenljivke v pozivih za dinamično vedenje agentov
- **Generiranje produkcijske kode**: Ustvarite kodo, pripravljeno za produkcijo, za hitro razvijanje aplikacij

### 4. Masovno izvajanje in ocenjevanje
- **Testiranje več modelov**: Izvajajte več pozivov hkrati preko izbranih modelov
- **Učinkovito testiranje ob obsegu**: Preizkusite različne vhode in konfiguracije učinkovito
- **Prilagojeni testni primeri**: Zaženite agente s testnimi primeri za preverjanje funkcionalnosti
- **Primerjava zmogljivosti**: Primerjajte rezultate med različnimi modeli in konfiguracijami

### 5. Ocenjevanje modelov z nizi podatkov
- **Standardne metrike**: Testirajte AI modele z vgrajenimi evalvatorji (F1 ocena, relevantnost, podobnost, koherenca)
- **Prilagojeni evalvatorji**: Ustvarite lastne evalvacijske metrike za specifične primere uporabe
- **Integracija naborov podatkov**: Testirajte modele z obsežnimi nabori podatkov
- **Merjenje zmogljivosti**: Kvantificirajte zmogljivost modela za odločitve glede robne uvedbe

### 6. Zmožnosti fino nastavljanja
- **Prilagoditev modelov**: Prilagodite modele za specifične primere uporabe in domene
- **Specializirana adaptacija**: Prilagodite modele za specializirane domene in zahteve
- **Optimizacija za rob**: Fino nastavite modele posebej za omejitve robne uvedbe
- **Usposabljanje za specifične domene**: Ustvarite modele, prilagojene specifičnim primerom uporabe na robu

### 7. Integracija MCP orodij
- **Povezljivost z zunanjimi orodji**: Povežite agente z zunanjimi orodji preko Model Context Protocol strežnikov
- **Dejanske akcije**: Omogočite agentom poizvedovanje baz podatkov, dostop do API-jev ali izvajanje lastne logike
- **Obstoječi MCP strežniki**: Uporabljajte orodja iz ukaznih (stdio) ali HTTP (server-sent event) protokolov
- **Razvoj prilagojenih MCP**: Gradite in ogrodite nove MCP strežnike s testiranjem v Agent Builder-ju

### 8. Razvoj in testiranje agentov
- **Podpora za klice funkcij**: Omogočite agentom dinamično klicanje zunanjih funkcij
- **Testiranje integracije v realnem času**: Testirajte integracije z izvajanjem in uporabo orodij v realnem času
- **Verzioniranje agentov**: Upravljanje različic agentov z možnostmi primerjave za ocenjevalne rezultate
- **Odpravljanje napak in sledenje**: Lokalno sledenje in odpravljanje težav pri razvoju agentov

## Potek razvoja Edge AI

### Faza 1: Odkrivanje in izbor modela
1. **Raziskovanje kataloga modelov**: Uporabite katalog modelov za iskanje modelov, primernih za robno uvedbo
2. **Primerjava zmogljivosti**: Ocenite modele glede na velikost, natančnost in hitrost sklepanja
3. **Lokalno testiranje**: Uporabite Ollama ali ONNX modele za lokalno testiranje pred robno uvedbo
4. **Ocena zahtev po virih**: Določite potrebo po spominu in računalniških zmogljivostih za ciljne robne naprave

### Faza 2: Optimizacija modela
1. **Pretvorba v ONNX**: Pretvorite izbrane modele v ONNX format za združljivost z robom
2. **Uporaba kvantizacije**: Zmanjšajte velikost modela s kvantizacijo INT8 ali INT4
3. **Optimizacija strojne opreme**: Optimizirajte za ciljno robno strojno opremo (ARM, x86, specializirani pospeševalci)
4. **Validacija zmogljivosti**: Preverite, da optimizirani modeli ohranjajo sprejemljivo natančnost

### Faza 3: Razvoj aplikacij
1. **Oblikovanje agentov**: Uporabite Agent Builder za ustvarjanje AI agentov, optimiziranih za rob
2. **Inženiring pozivov**: Razvijajte pozive, ki učinkovito delujejo z manjšimi robnimi modeli
3. **Testiranje integracije**: Testirajte agente v simuliranih robnih pogojih
4. **Generiranje kode**: Ustvarite produkcijsko kodo, optimizirano za robno uvedbo

### Faza 4: Ocenjevanje in testiranje
1. **Serijsko ocenjevanje**: Testirajte več konfiguracij za iskanje optimalnih robnih nastavitev
2. **Profiliranje zmogljivosti**: Analizirajte hitrost sklepanja, porabo spomina in natančnost
3. **Simulacija robnega okolja**: Testirajte v pogojih, podobnih ciljnemu robnemu okolju
4. **Testiranje obremenitve**: Ocenite zmogljivost pod različnimi obremenitvenimi pogoji

### Faza 5: Priprava uvedbe
1. **Končna optimizacija**: Uporabite končne optimizacije na podlagi rezultatov testov
2. **Pakiranje za uvedbo**: Pripravite pakete modelov in kode za robno uvedbo
3. **Dokumentacija**: Dokumentirajte zahteve in konfiguracijo uvedbe
4. **Nastavitev spremljanja**: Pripravite spremljanje in beleženje za robno uvedbo

## Ciljna publika za razvoj Edge AI

### Razvijalci Edge AI
- Razvijalci aplikacij, ki gradijo AI-podprte robne naprave in IoT rešitve
- Razvijalci vgrajenih sistemov, ki vključujejo AI zmogljivosti v naprave z omejenimi viri
- Mobilni razvijalci, ki ustvarjajo AI aplikacije za pametne telefone in tablice

### Inženirji Edge AI
- AI inženirji, ki optimizirajo modele za robno uvedbo in upravljajo pipeline sklepanja
- DevOps inženirji, ki nameščajo in upravljajo AI modele preko distribuirane robne infrastrukture
- Inženirji za zmogljivost, ki optimizirajo AI obremenitve glede na strojne omejitve

### Raziskovalci in učitelji
- Raziskovalci AI, ki razvijajo učinkovite modele in algoritme za robno računanje
- Učitelji, ki predavajo koncepte Edge AI in prikazujejo optimizacijske tehnike
- Študentje, ki se učijo o izzivih in rešitvah pri uvedbi Edge AI

## Primeri uporabe Edge AI

### Pametne IoT naprave
- **Prepoznavanje slik v realnem času**: Uvedite računalniški vid na IoT kamerah in senzorjih
- **Obdelava glasov**: Implementirajte prepoznavanje govora in naravnega jezika na pametnih zvočnikih
- **Napovedno vzdrževanje**: Izvajajte modele za odkrivanje anomalij na industrijskih robnih napravah
- **Okoljsko spremljanje**: Uvedite analizo podatkov senzorjev za okoljske aplikacije

### Mobilne in vgrajene aplikacije
- **Prevajanje na napravi**: Implementirajte modele za prevajanje jezikov, ki delujejo brez povezave
- **Obogatena resničnost**: Uvedite zaznavanje in sledenje objektov v realnem času za AR aplikacije
- **Zdravstveno spremljanje**: Izvajajte modele analize zdravja na nosljivih napravah in medicinski opremi
- **Avtonomni sistemi**: Implementirajte modele odločanja za drone, robote in vozila

### Robna računalniška infrastruktura
- **Robni podatkovni centri**: Uvedite AI modele v robnih podatkovnih centrih za aplikacije z nizko zakasnitvijo
- **Integracija CDN**: Vključite AI procesiranje v mreže za dostavo vsebin
- **5G Rob**: Izkoristite peto generacijo robnega računalništva za AI-podprte aplikacije
- **Meglični računalniki**: Implementirajte AI procesiranje v megličnih računalniških okoljih

## Namestitev in nastavitev

### Namestitev razširitve
Namestite razširitev AI orodjarne neposredno iz Visual Studio Code Marketplace:

**ID razširitve**: `ms-windows-ai-studio.windows-ai-studio`

**Načini namestitve**:
1. **VS Code Marketplace**: V pogled razširitev vnesite "AI Toolkit"
2. **Ukazna vrstica**: `code --install-extension ms-windows-ai-studio.windows-ai-studio`
3. **Neposredna namestitev**: Prenesite iz [VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)

### Predpogoji za razvoj Edge AI
- **Visual Studio Code**: Priporočena najnovejša različica
- **Python okolje**: Python 3.8+ z zahtevanimi AI knjižnicami
- **ONNX Runtime** (neobvezno): Za sklepanja modelov ONNX
- **Ollama** (neobvezno): Za lokalno streženje modelov
- **Orodja za strojno pospeševanje**: CUDA, OpenVINO ali pospeševalniki specifičnih platform

### Začetna konfiguracija
1. **Aktivacija razširitve**: Odprite VS Code in preverite, da je AI orodjarna vidna na vrstici aktivnosti
2. **Nastavitev ponudnikov modelov**: Konfigurirajte dostop do GitHub, OpenAI, Anthropic ali drugih ponudnikov modelov
3. **Lokalno okolje**: Nastavite Python okolje in namestite potrebne pakete
4. **Pospeševanje strojne opreme**: Konfigurirajte pospeševanje GPU/NPU, če je na voljo
5. **Integracija MCP**: Nastavite strežnike Model Context Protocol, če je potrebno

### Kontrolni seznam začetne nastavitve
- [ ] Razširitev AI orodjarne nameščena in aktivirana
- [ ] Katalog modelov dostopen in modeli odkritljivi
- [ ] Igrališče funkcionalno za testiranje modelov
- [ ] Graditelj agentov dostopen za razvoj pozivov
- [ ] Lokalno razvojno okolje konfigurirano
- [ ] Pospeševanje strojne opreme (če je na voljo) pravilno nastavljeno

## Začetek dela z AI orodjarno

### Hitri začetek

Priporočamo začetek z modeli, gostovanimi na GitHub, za najbolj poenostavljeno izkušnjo:

1. **Namestitev**: Sledite [namestitvenemu vodniku](https://code.visualstudio.com/docs/intelligentapps/overview#_install-and-setup) za nastavitev AI orodjarne na vaši napravi
2. **Odkrivanje modelov**: V drevesnem pogledu razširitve izberite **KATALOG > Models** za raziskovanje razpoložljivih modelov
3. **GitHub modeli**: Začnite z modeli, gostovanimi na GitHub, za optimalno integracijo
4. **Testiranje na igrališču**: Iz katere koli kartice modela izberite **Try in Playground** za začetek eksperimentiranja z zmogljivostmi modela

### Korak za korakom razvoj Edge AI

#### Korak 1: Raziskovanje in izbor modela
1. Odprite pogled AI orodjarne na vrstici aktivnosti VS Code
2. Brskajte po katalogu modelov za modele, primerne za robno uvedbo
3. Filtrirajte po ponudniku (GitHub, ONNX, Ollama) glede na vaše robne zahteve
4. Uporabite **Try in Playground** za takojšnje testiranje zmogljivosti modela

#### Korak 2: Razvoj agentov
1. Uporabite **Graditelj pozivov (agentov)** za ustvarjanje agentov, optimiziranih za rob
2. Generirajte začetne pozive z uporabo opisov v naravnem jeziku
3. Iterativno izboljšujte pozive na podlagi odzivov modela
4. Integrirajte MCP orodja za izboljšane zmogljivosti agentov


#### Korak 3: Testiranje in ocenjevanje
1. Uporabite **Bulk Run** za testiranje več pozivov na izbranih modelih
2. Zaženite agente s testnimi primeri za preverjanje funkcionalnosti
3. Ocenite natančnost in zmogljivost z vgrajenimi ali po meri določenimi metričnimi podatki
4. Primerjajte različne modele in konfiguracije

#### Korak 4: Izboljšava in optimizacija
1. Prilagodite modele za specifične robne primere uporabe
2. Uporabite področju specifično fino nastavljanje
3. Optimizirajte za omejitve robne namestitve
4. Verzija in primerjava različnih konfiguracij agentov

#### Korak 5: Priprava na namestitev
1. Generirajte kodo, pripravljeno za produkcijo, z uporabo graditelja agentov
2. Vzpostavite povezave s strežnikom MCP za uporabo v produkciji
3. Pripravite namestitvene pakete za robne naprave
4. Konfigurirajte metrike spremljanja in ocenjevanja

## Vzorci za AI Toolkit 

Preizkusite naše vzorce
[Vzorce AI Toolkita](https://github.com/Azure-Samples/AI_Toolkit_Samples) so zasnovani za pomoč razvijalcem in raziskovalcem pri učinkovitem raziskovanju in izvajanju AI rešitev. 

Naši vzorci vključujejo:

Vzorec kode: Vnaprej pripravljeni primeri za demonstracijo funkcionalnosti AI, kot so usposabljanje, nameščanje ali integracija modelov v aplikacije.
Dokumentacija: Vodniki in vodiči za pomoč uporabnikom pri razumevanju funkcij AI Toolkita in njihovi uporabi.
Predpogoji

- Visual Studio Code
- AI Toolkit za Visual Studio Code
- GitHub token za osebni dostop z drobnim nadzorom (PAT)
- Foundry Local

## Najboljše prakse za razvoj robne umetne inteligence

### Izbira modela
- **Velikostne omejitve**: Izberite modele, ki ustrezajo omejitvam pomnilnika ciljnih naprav
- **Hitrost sklepanja**: Prednost dajte modelom z vse hitrejšim sklepanjem za aplikacije v realnem času
- **Kompromisi glede natančnosti**: Uravnotežite natančnost modela z omejitvami virov
- **Združljivost formatov**: Priporočajo se formati ONNX ali strojno optimizirani formati za robno namestitev

### Optimizacijske tehnike
- **Kvantizacija**: Uporabite INT8 ali INT4 kvantizacijo za zmanjšanje velikosti modela in izboljšanje hitrosti
- **Obrezovanje**: Odstranite nepotrebne parametre modela za zmanjšanje računalniških zahtev
- **Destilacija znanja**: Ustvarite manjše modele, ki ohranjajo zmogljivost večjih
- **Strojno pospeševanje**: Izkoristite NPU, GPU ali specializirane pospeševalnike, kadar so na voljo

### Razvojni potek
- **Iterativno testiranje**: Pogosto testirajte v pogojih, ki so podobni robnim med razvojem
- **Spremljanje zmogljivosti**: Nenehno spremljajte uporabo virov in hitrost sklepanja
- **Nadzor različic**: Spremljajte različice modelov in nastavitve optimizacije
- **Dokumentacija**: Dokumentirajte vse odločitve o optimizaciji in kompromisih zmogljivosti

### Premisleki za namestitev
- **Spremljanje virov**: Spremljajte porabo pomnilnika, CPU in energije v produkciji
- **Strategije zasilnega ukrepanja**: Implementirajte mehanizme za zasilno reševanje pri napakah modelov
- **Mehanizmi posodobitev**: Načrtujte posodobitve modelov in upravljanje različic
- **Varnost**: Uvedite ustrezne varnostne ukrepe za robne AI aplikacije

## Integracija z okviri za robno AI

### ONNX Runtime
- **Namestitev na več platform**: Namestite ONNX modele na različnih robnih platformah
- **Strojna optimizacija**: Izkoristite strojne optimizacije ONNX Runtime
- **Mobilna podpora**: Uporabite ONNX Runtime Mobile za aplikacije na pametnih telefonih in tablicah
- **Integracija IoT**: Namestite na IoT napravah z uporabo lahkih distribucij ONNX Runtime

### Windows ML
- **Windows naprave**: Optimizirajte za robne naprave in računalnike na Windows
- **Pospešek NPU**: Izkoristite enote za nevronsko procesiranje na napravah Windows
- **DirectML**: Uporabite DirectML za pospeševanje GPU na platformah Windows
- **Integracija UWP**: Integrirajte z aplikacijami Universal Windows Platform

### TensorFlow Lite
- **Mobilna optimizacija**: Namestite TensorFlow Lite modele na mobilne in vgrajene naprave
- **Strojni delegati**: Uporabite specializirane strojne delegate za pospešitev
- **Mikrokrmilniki**: Namestite na mikrokrmilnike z uporabo TensorFlow Lite Micro
- **Podpora več platformam**: Namestite na Android, iOS in vgrajene Linux sisteme

### Azure IoT Edge
- **Hibridna rešitev oblak-rob**: Združite oblačno usposabljanje z robnim sklepanjem
- **Namestitev modulov**: Namestite AI modele kot IoT Edge module
- **Upravljanje naprav**: Oddaljeno upravljajte robne naprave in posodobitve modelov
- **Telemetrija**: Zbirajte podatke o zmogljivosti in metrike modelov iz robnih namestitev

## Napredni scenariji za robno AI

### Namestitev več modelov
- **Modelske skupine**: Namestite več modelov za boljšo natančnost ali redundanco
- **A/B testiranje**: Testirajte različne modele hkrati na robnih napravah
- **Dinamična izbira**: Izberite modele glede na trenutno stanje naprav
- **Deljenje virov**: Optimizirajte uporabo virov med več nameščenimi modeli

### Federirano učenje
- **Porazdeljeno usposabljanje**: Usposabljajte modele na več robnih napravah
- **Ohranjanje zasebnosti**: Podatke za usposabljanje hranite lokalno, medtem ko delite izboljšave modelov
- **Sodelovalno učenje**: Omogočite napravam učenje iz skupnih izkušenj
- **Koordinacija rob-in-oblak**: Koordinirajte učenje med robnimi napravami in oblačno infrastrukturo

### Procesiranje v realnem času
- **Tokovno procesiranje**: Procesirajte neprekinjene podatkovne tokove na robnih napravah
- **Nizka zakasnitev sklepanja**: Optimizirajte za minimalno zakasnitev sklepanja
- **Obdelava paketov**: Učinkovito obdelajte podatkovne pakete na robnih napravah
- **Prilagodljivo procesiranje**: Prilagodite procesiranje glede na trenutne zmogljivosti naprav

## Odpravljanje težav pri razvoju robne AI

### Pogoste težave
- **Omejitve pomnilnika**: Model je prevelik za pomnilnik ciljne naprave
- **Hitrost sklepanja**: Sklepanje modela je prepočasi za zahteve v realnem času
- **Poslabšanje natančnosti**: Optimizacija nesprejemljivo zmanjša natančnost modela
- **Združljivost strojne opreme**: Model ni združljiv s ciljno strojno opremo

### Strategije odpravljanja napak
- **Profiliranje zmogljivosti**: Uporabite funkcije sledenja AI Toolkita za odkrivanje ozkih grl
- **Spremljanje virov**: Spremljajte porabo pomnilnika in CPU med razvojem
- **Postopno testiranje**: Testirajte optimizacije postopno, da izolirate težave
- **Simulacija strojne opreme**: Uporabite razvojna orodja za simulacijo ciljne strojne opreme

### Rešitve optimizacije
- **Nadaljnja kvantizacija**: Uporabite bolj agresivne tehnike kvantizacije
- **Arhitektura modela**: Razmislite o različnih arhitekturah modelov, optimiziranih za rob
- **Optimizacija predprocesiranja**: Optimizirajte predprocesiranje podatkov za robne omejitve
- **Optimizacija sklepanja**: Uporabite strojno specifične optimizacije sklepanja

## Viri in naslednji koraki

### Uradna dokumentacija
- [Dokumentacija za razvijalce AI Toolkita](https://aka.ms/AIToolkit/doc)
- [Vodnik za namestitev in nastavitev](https://code.visualstudio.com/docs/intelligentapps/overview#_install-and-setup)
- [Dokumentacija za VS Code Intelligent Apps](https://code.visualstudio.com/docs/intelligentapps)
- [Dokumentacija Model Context Protocol (MCP)](https://modelcontextprotocol.io/)

### Skupnost in podpora
- [GitHub repozitorij AI Toolkita](https://github.com/microsoft/vscode-ai-toolkit)
- [GitHub vprašanja in zahteve za funkcije](https://aka.ms/AIToolkit/feedback)
- [Azure AI Foundry Discord skupnost](https://aka.ms/azureaifoundry/discord)
- [Tržnica razširitev VS Code](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)

### Tehnični viri
- [Dokumentacija ONNX Runtime](https://onnxruntime.ai/)
- [Dokumentacija Ollama](https://ollama.ai/)
- [Dokumentacija Windows ML](https://docs.microsoft.com/en-us/windows/ai/)
- [Dokumentacija Azure AI Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/)

### Učne poti
- [Tečaj Osnove robne AI](../Module01/README.md)
- [Vodnik za majhne jezikovne modele](../Module02/README.md)
- [Strategije robne namestitve](../Module03/README.md)
- [Razvoj Windows robne AI](./windowdeveloper.md)

### Dodatni viri
- **Statistika repozitorija**: 1,8k+ zvezdic, 150+ forkov, 18+ prispevkov
- **Licenca**: Licenca MIT
- **Varnost**: Uveljavljajo se Microsoftove varnostne politike
- **Telemetrija**: Upošteva nastavitve telemetrije VS Code

## Zaključek

AI Toolkit za Visual Studio Code predstavlja celovito platformo za sodoben razvoj umetne inteligence, ki nudi poenostavljene zmogljivosti za razvoj agentov, kar je še posebej dragoceno za aplikacije robne AI. S širokim katalogom modelov, ki podpira ponudnike, kot so Anthropic, OpenAI, GitHub in Google, v kombinaciji s lokalnim izvajanjem prek ONNX in Ollama, orodje ponuja prilagodljivost, potrebno za različne scenarije robne namestitve.

Njegova moč je v integriranem pristopu — od odkrivanja modelov in eksperimentiranja v Playground do zahtevnega razvoja agentov s Prompt Builderjem, celovitih zmogljivosti ocenjevanja in brezhibne integracije orodij MCP. Za razvijalce robne AI to pomeni hitro prototipiranje in testiranje AI agentov pred robno namestitvijo, z možnostjo hitrega iteriranja in optimiziranja za okolja z omejenimi viri.

Ključne prednosti za razvoj robne AI vključujejo:
- **Hitro eksperimentiranje**: Hitro testirajte modele in agente pred končno robno namestitvijo
- **Fleksibilnost več ponudnikov**: Dostop do modelov iz različnih virov za iskanje optimalnih robnih rešitev
- **Lokalni razvoj**: Testiranje z ONNX in Ollama za razvoj brez povezave in z varovanjem zasebnosti
- **Pripravljenost za produkcijo**: Generirajte kodo, pripravljeno za produkcijo, in se integrirajte z zunanjimi orodji prek MCP
- **Celovito ocenjevanje**: Uporabite vgrajene in po meri določene meritve za preverjanje zmogljivosti robne AI

Ker AI še naprej napreduje proti scenarijem robne namestitve, AI Toolkit za VS Code nudi razvojno okolje in potek dela, potrebne za izdelavo, testiranje in optimizacijo inteligentnih aplikacij za okolja z omejenimi viri. Ne glede na to, ali razvijate IoT rešitve, mobilne AI aplikacije ali vgrajene inteligentne sisteme, celovit nabor funkcij orodja in integriran potek dela podpira celoten življenjski cikel razvoja robne AI.

Z neprekinjenim razvojem in aktivno skupnostjo (1,8k+ GitHub zvezdic) AI Toolkit ostaja na čelu orodij za razvoj AI, ki se nenehno razvijajo, da zadovoljijo potrebe sodobnih razvijalcev AI za robne scenarije namestitve.

[Naslednji Foundry Local](./foundrylocal.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
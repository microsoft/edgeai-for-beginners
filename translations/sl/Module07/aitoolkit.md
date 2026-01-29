# AI Orodje za Visual Studio Code - Vodnik za razvoj Edge AI

## Uvod

Dobrodošli v obsežnem vodniku za uporabo AI Orodja za Visual Studio Code pri razvoju Edge AI. Ker se umetna inteligenca premika od centraliziranega računalništva v oblaku k razpršenim napravam na robu, razvijalci potrebujejo zmogljiva, integrirana orodja, ki lahko obvladajo edinstvene izzive robne implementacije - od omejitev virov do zahtev po delovanju brez povezave.

AI Orodje za Visual Studio Code zapolnjuje to vrzel z zagotavljanjem celovitega razvojnega okolja, posebej zasnovanega za gradnjo, testiranje in optimizacijo AI aplikacij, ki učinkovito delujejo na robnih napravah. Ne glede na to, ali razvijate za IoT senzorje, mobilne naprave, vgrajene sisteme ali robne strežnike, to orodje poenostavi celoten razvojni proces znotraj znanega okolja VS Code.

Ta vodnik vas bo popeljal skozi ključne koncepte, orodja in najboljše prakse za uporabo AI Orodja v vaših Edge AI projektih, od začetne izbire modela do implementacije v produkcijo.

## Pregled

AI Orodje za Visual Studio Code je zmogljiva razširitev, ki poenostavi razvoj agentov in ustvarjanje AI aplikacij. Orodje ponuja celovite zmogljivosti za raziskovanje, ocenjevanje in implementacijo AI modelov iz širokega nabora ponudnikov—vključno z Anthropic, OpenAI, GitHub, Google—hkrati pa podpira lokalno izvajanje modelov z uporabo ONNX in Ollama.

Kar AI Orodje ločuje od drugih je njegov celovit pristop k celotnemu življenjskemu ciklu razvoja AI. Za razliko od tradicionalnih orodij za razvoj AI, ki se osredotočajo na posamezne vidike, AI Orodje zagotavlja integrirano okolje, ki pokriva odkrivanje modelov, eksperimentiranje, razvoj agentov, ocenjevanje in implementacijo—vse znotraj znanega okolja VS Code.

Platforma je posebej zasnovana za hitro prototipiranje in implementacijo v produkcijo, z značilnostmi, kot so generacija pozivov, hitri začetki, brezhibne integracije MCP (Model Context Protocol) orodij in obsežne zmogljivosti ocenjevanja. Za razvoj Edge AI to pomeni, da lahko učinkovito razvijate, testirate in optimizirate AI aplikacije za scenarije robne implementacije, hkrati pa ohranjate celoten razvojni proces znotraj VS Code.

## Cilji učenja

Na koncu tega vodnika boste sposobni:

### Osnovne kompetence
- **Namestiti in konfigurirati** AI Orodje za Visual Studio Code za delovne procese razvoja Edge AI
- **Navigirati in uporabljati** vmesnik AI Orodja, vključno s Katalogom modelov, Igralnico in Graditeljem agentov
- **Izbrati in oceniti** AI modele, primerne za robno implementacijo glede na zmogljivost in omejitve virov
- **Pretvoriti in optimizirati** modele z uporabo ONNX formata in tehnik kvantizacije za robne naprave

### Spretnosti razvoja Edge AI
- **Oblikovati in implementirati** Edge AI aplikacije z uporabo integriranega razvojnega okolja
- **Izvajati testiranje modelov** v robnih pogojih z uporabo lokalnega sklepanja in spremljanja virov
- **Ustvariti in prilagoditi** AI agente, optimizirane za scenarije robne implementacije
- **Oceniti zmogljivost modelov** z uporabo metrik, pomembnih za robno računalništvo (zakasnitev, poraba pomnilnika, natančnost)

### Optimizacija in implementacija
- **Uporabiti kvantizacijo in obrezovanje** za zmanjšanje velikosti modela ob ohranjanju sprejemljive zmogljivosti
- **Optimizirati modele** za specifične robne strojne platforme, vključno s CPU, GPU in NPU pospeševanjem
- **Uvesti najboljše prakse** za razvoj Edge AI, vključno z upravljanjem virov in strategijami za izpad
- **Pripraviti modele in aplikacije** za implementacijo v produkcijo na robnih napravah

### Napredni koncepti Edge AI
- **Integrirati z robnimi AI okviri** vključno z ONNX Runtime, Windows ML in TensorFlow Lite
- **Implementirati večmodelne arhitekture** in scenarije federativnega učenja za robna okolja
- **Odpravljati pogoste težave Edge AI** vključno z omejitvami pomnilnika, hitrostjo sklepanja in združljivostjo strojne opreme
- **Oblikovati strategije spremljanja in beleženja** za Edge AI aplikacije v produkciji

### Praktična uporaba
- **Zgraditi celovite rešitve Edge AI** od izbire modela do implementacije
- **Demonstrirati usposobljenost** v robno specifičnih delovnih procesih razvoja in tehnikah optimizacije
- **Uporabiti naučene koncepte** v resničnih primerih uporabe Edge AI, vključno z IoT, mobilnimi in vgrajenimi aplikacijami
- **Oceniti in primerjati** različne strategije implementacije Edge AI ter njihove kompromise

## Ključne funkcije za razvoj Edge AI

### 1. Katalog modelov in odkrivanje
- **Podpora več ponudnikom**: Brskajte in dostopajte do AI modelov iz Anthropic, OpenAI, GitHub, Google in drugih ponudnikov
- **Integracija lokalnih modelov**: Poenostavljeno odkrivanje modelov ONNX in Ollama za robno implementacijo
- **GitHub modeli**: Neposredna integracija z gostovanjem modelov na GitHubu za poenostavljen dostop
- **Primerjava modelov**: Primerjajte modele med seboj, da najdete optimalno ravnovesje za omejitve robnih naprav

### 2. Interaktivna igralnica
- **Interaktivno testno okolje**: Hitro eksperimentiranje z zmogljivostmi modelov v nadzorovanem okolju
- **Podpora več modalnostim**: Testiranje z slikami, besedilom in drugimi vnosi, značilnimi za robne scenarije
- **Povratne informacije v realnem času**: Takojšnje povratne informacije o odzivih modelov in zmogljivosti
- **Optimizacija parametrov**: Fino prilagajanje parametrov modela za zahteve robne implementacije

### 3. Graditelj pozivov (agentov)
- **Generacija naravnega jezika**: Ustvarjanje začetnih pozivov z uporabo opisov v naravnem jeziku
- **Iterativno izboljšanje**: Izboljšanje pozivov na podlagi odzivov modelov in zmogljivosti
- **Razčlenjevanje nalog**: Razčlenjevanje kompleksnih nalog z veriženjem pozivov in strukturiranimi izhodi
- **Podpora spremenljivkam**: Uporaba spremenljivk v pozivih za dinamično vedenje agentov
- **Generacija produkcijske kode**: Generiranje produkcijsko pripravljene kode za hitro razvijanje aplikacij

### 4. Masovno izvajanje in ocenjevanje
- **Testiranje več modelov**: Izvajanje več pozivov hkrati na izbranih modelih
- **Učinkovito testiranje na velikem obsegu**: Testiranje različnih vnosov in konfiguracij učinkovito
- **Prilagojeni testni primeri**: Izvajanje testnih primerov za validacijo funkcionalnosti agentov
- **Primerjava zmogljivosti**: Primerjava rezultatov med različnimi modeli in konfiguracijami

### 5. Ocenjevanje modelov z nabori podatkov
- **Standardne metrike**: Testiranje AI modelov z vgrajenimi ocenjevalniki (F1 rezultat, relevantnost, podobnost, koherenca)
- **Prilagojeni ocenjevalniki**: Ustvarjanje lastnih metrik ocenjevanja za specifične primere uporabe
- **Integracija naborov podatkov**: Testiranje modelov proti obsežnim naborom podatkov
- **Merjenje zmogljivosti**: Kvantifikacija zmogljivosti modelov za odločitve o robni implementaciji

### 6. Zmožnosti prilagajanja
- **Prilagoditev modelov**: Prilagoditev modelov za specifične primere uporabe in domene
- **Specializirana prilagoditev**: Prilagoditev modelov za specializirane domene in zahteve
- **Optimizacija za rob**: Fino prilagajanje modelov posebej za omejitve robne implementacije
- **Usposabljanje za specifične domene**: Ustvarjanje modelov, prilagojenih specifičnim robnim primerom uporabe

### 7. Integracija MCP orodij
- **Povezljivost z zunanjimi orodji**: Povezovanje agentov z zunanjimi orodji prek strežnikov Model Context Protocol
- **Dejanja v resničnem svetu**: Omogočanje agentom, da poizvedujejo po podatkovnih bazah, dostopajo do API-jev ali izvajajo prilagojeno logiko
- **Obstoječi MCP strežniki**: Uporaba orodij iz ukazne vrstice (stdio) ali HTTP (dogodki, ki jih pošlje strežnik)
- **Razvoj prilagojenih MCP**: Gradnja in priprava novih MCP strežnikov z testiranjem v Graditelju agentov

### 8. Razvoj in testiranje agentov
- **Podpora klicanju funkcij**: Omogočanje agentom, da dinamično kličejo zunanje funkcije
- **Testiranje integracij v realnem času**: Testiranje integracij z izvajanjem v realnem času in uporabo orodij
- **Različice agentov**: Nadzor različic agentov z zmogljivostmi primerjave rezultatov ocenjevanja
- **Odpravljanje napak in sledenje**: Lokalno sledenje in odpravljanje napak pri razvoju agentov

## Delovni proces razvoja Edge AI

### Faza 1: Odkrivanje in izbira modelov
1. **Raziskovanje kataloga modelov**: Uporabite katalog modelov za iskanje modelov, primernih za robno implementacijo
2. **Primerjava zmogljivosti**: Ocenite modele glede na velikost, natančnost in hitrost sklepanja
3. **Lokalno testiranje**: Uporabite Ollama ali ONNX modele za lokalno testiranje pred robno implementacijo
4. **Ocena zahtev po virih**: Določite potrebe po pomnilniku in računalniški moči za ciljne robne naprave

### Faza 2: Optimizacija modelov
1. **Pretvorba v ONNX**: Pretvorite izbrane modele v ONNX format za združljivost z robom
2. **Uporaba kvantizacije**: Zmanjšajte velikost modela z INT8 ali INT4 kvantizacijo
3. **Optimizacija strojne opreme**: Optimizirajte za ciljno robno strojno opremo (ARM, x86, specializirani pospeševalniki)
4. **Validacija zmogljivosti**: Validirajte, da optimizirani modeli ohranjajo sprejemljivo natančnost

### Faza 3: Razvoj aplikacij
1. **Oblikovanje agentov**: Uporabite Graditelja agentov za ustvarjanje AI agentov, optimiziranih za rob
2. **Inženiring pozivov**: Razvijte pozive, ki učinkovito delujejo z manjšimi robnimi modeli
3. **Testiranje integracij**: Testirajte agente v simuliranih robnih pogojih
4. **Generacija kode**: Generirajte produkcijsko kodo, optimizirano za robno implementacijo

### Faza 4: Ocenjevanje in testiranje
1. **Masovno ocenjevanje**: Testirajte več konfiguracij za iskanje optimalnih robnih nastavitev
2. **Profiliranje zmogljivosti**: Analizirajte hitrost sklepanja, porabo pomnilnika in natančnost
3. **Simulacija robnih pogojev**: Testirajte v pogojih, podobnih ciljni robni implementaciji
4. **Testiranje obremenitve**: Ocenite zmogljivost pod različnimi pogoji obremenitve

### Faza 5: Priprava na implementacijo
1. **Končna optimizacija**: Uporabite končne optimizacije na podlagi rezultatov testiranja
2. **Pakiranje za implementacijo**: Pakirajte modele in kodo za robno implementacijo
3. **Dokumentacija**: Dokumentirajte zahteve za implementacijo in konfiguracijo
4. **Priprava spremljanja**: Pripravite spremljanje in beleženje za robno implementacijo

## Ciljna publika za razvoj Edge AI

### Razvijalci Edge AI
- Razvijalci aplikacij, ki gradijo naprave z AI na robu in IoT rešitve
- Razvijalci vgrajenih sistemov, ki vključujejo AI zmogljivosti v naprave z omejenimi viri
- Mobilni razvijalci, ki ustvarjajo AI aplikacije na napravi za pametne telefone in tablice

### Inženirji Edge AI
- AI inženirji, ki optimizirajo modele za robno implementacijo in upravljajo sklepalne procese
- DevOps inženirji, ki implementirajo in upravljajo AI modele v razpršeni robni infrastrukturi
- Inženirji zmogljivosti, ki optimizirajo AI delovne obremenitve za omejitve robne strojne opreme

### Raziskovalci in izobraževalci
- AI raziskovalci, ki razvijajo učinkovite modele in algoritme za robno računalništvo
- Izobraževalci, ki poučujejo koncepte Edge AI in demonstrirajo tehnike optimizacije
- Študenti, ki se učijo o izzivih in rešitvah pri implementaciji Edge AI

## Primeri uporabe Edge AI

### Pametne IoT naprave
- **Prepoznavanje slik v realnem času**: Implementacija modelov računalniškega vida na IoT kamerah in senzorjih
- **Obdelava glasu**: Uvedba prepoznavanja govora in obdelave naravnega jezika na pametnih zvočnikih
- **Prediktivno vzdrževanje**: Izvajanje modelov za zaznavanje anomalij na industrijskih robnih napravah
- **Okoljsko spremljanje**: Implementacija modelov za analizo podatkov senzorjev v okoljskih aplikacijah

### Mobilne in vgrajene aplikacije
- **Prevajanje na napravi**: Implementacija modelov za prevajanje jezika, ki delujejo brez povezave
- **Razširjena resničnost**: Uvedba prepoznavanja in sledenja objektov v realnem času za AR aplikacije
- **Spremljanje zdravja**: Izvajanje modelov za analizo zdravja na nosljivih napravah in medicinski opremi
- **Avtonomni sistemi**: Implementacija modelov za odločanje za drone, robote in vozila

### Infrastruktura robnega računalništva
- **Robni podatkovni centri**: Implementacija AI modelov v robnih podatkovnih centrih za aplikacije z nizko zakasnitvijo
- **Integracija CDN**: Integracija zmogljivosti AI obdelave v omrežja za dostavo vsebin
- **5G rob**: Izkoristite 5G robno računalništvo za aplikacije, ki temeljijo na AI
- **Megleno računalništvo**: Implementacija AI obdelave v okoljih meglenega računalništva

## Namestitev in nastavitev

### Namestitev razširitve
Namestite razširitev AI Orodje neposredno iz Visual Studio Code Marketplace:

**ID razširitve**: `ms-windows-ai-studio.windows-ai-studio`

**Metode namestitve**:
1. **VS Code Marketplace**: Poiščite "AI Toolkit" v pogledu razširitev
2. **Ukazna vrstica**: `code --install-extension ms-windows-ai-studio.windows-ai-studio`
3. **Neposredna namestitev**: Prenesite z [VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)

### Predpogoji za razvoj Edge AI
- **Visual Studio Code**: Priporočena najnovejša različica
- **Python okolje**: Python 3.8+ z zahtevanimi AI knjižnicami
- **ONNX Runtime** (neobvezno): Za sklepanja modelov ONNX
- **Ollama** (neobvezno): Za lokalno strežbo modelov
- **Orodja za pospeševanje strojne opreme**: CUDA, OpenVINO ali platformno specifični pospeševalniki

### Začetna konfiguracija
1. **Aktivacija razš
2. Ustvarite začetne pozive z uporabo opisov v naravnem jeziku  
3. Ponavljajte in izboljšujte pozive na podlagi odzivov modela  
4. Integrirajte MCP orodja za izboljšane zmogljivosti agentov  

#### Korak 3: Testiranje in ocenjevanje  
1. Uporabite **Bulk Run** za testiranje več pozivov na izbranih modelih  
2. Zaženite agente s testnimi primeri za preverjanje funkcionalnosti  
3. Ocenite natančnost in zmogljivost z vgrajenimi ali prilagojenimi metrikami  
4. Primerjajte različne modele in konfiguracije  

#### Korak 4: Fino nastavljanje in optimizacija  
1. Prilagodite modele za specifične robne primere uporabe  
2. Uporabite fino nastavljanje, specifično za domeno  
3. Optimizirajte za omejitve pri robni uporabi  
4. Verzionirajte in primerjajte različne konfiguracije agentov  

#### Korak 5: Priprava na uvedbo  
1. Ustvarite produkcijsko pripravljeno kodo z Agent Builderjem  
2. Nastavite povezave MCP strežnika za produkcijsko uporabo  
3. Pripravite pakete za uvedbo na robnih napravah  
4. Konfigurirajte metrike za spremljanje in ocenjevanje  

## Vzorci za AI Toolkit  

Preizkusite naše vzorce  
[Vzorci AI Toolkit](https://github.com/Azure-Samples/AI_Toolkit_Samples) so zasnovani za pomoč razvijalcem in raziskovalcem pri učinkovitem raziskovanju in implementaciji AI rešitev.  

Naši vzorci vključujejo:  

Vzorec kode: Vnaprej pripravljeni primeri za prikaz funkcionalnosti AI, kot so učenje, uvedba ali integracija modelov v aplikacije.  
Dokumentacija: Vodniki in vadnice za pomoč uporabnikom pri razumevanju funkcij AI Toolkit in njihove uporabe.  
Predpogoji  

- Visual Studio Code  
- AI Toolkit za Visual Studio Code  
- GitHub osebni dostopni žeton (PAT)  
- Foundry Local  

## Najboljše prakse za razvoj Edge AI  

### Izbira modela  
- **Omejitve velikosti**: Izberite modele, ki ustrezajo pomnilniškim omejitvam ciljnih naprav  
- **Hitrost sklepanja**: Dajte prednost modelom s hitro hitrostjo sklepanja za aplikacije v realnem času  
- **Kompromisi pri natančnosti**: Uravnotežite natančnost modela z omejitvami virov  
- **Združljivost formatov**: Prednost dajte formatom ONNX ali formatom, optimiziranim za strojno opremo, za robno uvedbo  

### Tehnike optimizacije  
- **Kvantizacija**: Uporabite kvantizacijo INT8 ali INT4 za zmanjšanje velikosti modela in izboljšanje hitrosti  
- **Obrezovanje**: Odstranite nepotrebne parametre modela za zmanjšanje računalniških zahtev  
- **Distilacija znanja**: Ustvarite manjše modele, ki ohranjajo zmogljivost večjih  
- **Pospeševanje strojne opreme**: Izkoristite NPUs, GPUs ali specializirane pospeševalnike, kadar so na voljo  

### Delovni tok razvoja  
- **Iterativno testiranje**: Pogosto testirajte v pogojih, podobnih robnim, med razvojem  
- **Spremljanje zmogljivosti**: Nenehno spremljajte uporabo virov in hitrost sklepanja  
- **Nadzor različic**: Spremljajte različice modelov in nastavitve optimizacije  
- **Dokumentacija**: Dokumentirajte vse odločitve o optimizaciji in kompromisih pri zmogljivosti  

### Upoštevanje pri uvedbi  
- **Spremljanje virov**: Spremljajte pomnilnik, CPU in porabo energije v produkciji  
- **Strategije za izpad**: Implementirajte mehanizme za izpad modela  
- **Mehanizmi za posodobitve**: Načrtujte posodobitve modelov in upravljanje različic  
- **Varnost**: Uvedite ustrezne varnostne ukrepe za aplikacije Edge AI  

## Integracija z okviri Edge AI  

### ONNX Runtime  
- **Uvedba na več platformah**: Uvedite ONNX modele na različnih robnih platformah  
- **Optimizacija strojne opreme**: Izkoristite strojno specifične optimizacije ONNX Runtime  
- **Podpora za mobilne naprave**: Uporabite ONNX Runtime Mobile za aplikacije na pametnih telefonih in tablicah  
- **Integracija IoT**: Uvedite na IoT napravah z lahkimi distribucijami ONNX Runtime  

### Windows ML  
- **Windows naprave**: Optimizirajte za robne naprave in računalnike na osnovi Windows  
- **Pospeševanje NPU**: Izkoristite nevronske procesne enote na napravah Windows  
- **DirectML**: Uporabite DirectML za pospeševanje GPU na Windows platformah  
- **Integracija UWP**: Integrirajte z aplikacijami Universal Windows Platform  

### TensorFlow Lite  
- **Optimizacija za mobilne naprave**: Uvedite modele TensorFlow Lite na mobilnih in vgrajenih napravah  
- **Delegati strojne opreme**: Uporabite specializirane delegate strojne opreme za pospeševanje  
- **Mikrokrmilniki**: Uvedite na mikrokrmilnikih z uporabo TensorFlow Lite Micro  
- **Podpora za več platform**: Uvedite na Android, iOS in vgrajenih Linux sistemih  

### Azure IoT Edge  
- **Hibrid oblak-rob**: Združite učenje v oblaku z sklepanjem na robu  
- **Uvedba modulov**: Uvedite AI modele kot module IoT Edge  
- **Upravljanje naprav**: Oddaljeno upravljajte robne naprave in posodobitve modelov  
- **Telemetrija**: Zbirajte podatke o zmogljivosti in metrike modelov iz robnih uvedb  

## Napredni scenariji Edge AI  

### Uvedba več modelov  
- **Ensemble modeli**: Uvedite več modelov za izboljšano natančnost ali redundanco  
- **A/B testiranje**: Hkrati testirajte različne modele na robnih napravah  
- **Dinamična izbira**: Izberite modele glede na trenutne pogoje naprave  
- **Deljenje virov**: Optimizirajte uporabo virov med več uvedenimi modeli  

### Federativno učenje  
- **Porazdeljeno učenje**: Učite modele na več robnih napravah  
- **Ohranjanje zasebnosti**: Ohranite podatke za učenje lokalno, medtem ko delite izboljšave modelov  
- **Sodelovalno učenje**: Omogočite napravam, da se učijo iz kolektivnih izkušenj  
- **Koordinacija rob-oblak**: Koordinirajte učenje med robnimi napravami in infrastrukturo v oblaku  

### Procesiranje v realnem času  
- **Procesiranje tokov**: Procesirajte neprekinjene tokove podatkov na robnih napravah  
- **Sklepanja z nizko zakasnitvijo**: Optimizirajte za minimalno zakasnitev sklepanja  
- **Procesiranje paketov**: Učinkovito procesirajte pakete podatkov na robnih napravah  
- **Prilagodljivo procesiranje**: Prilagodite procesiranje glede na trenutne zmogljivosti naprave  

## Odpravljanje težav pri razvoju Edge AI  

### Pogoste težave  
- **Omejitve pomnilnika**: Model je prevelik za pomnilnik ciljne naprave  
- **Hitrost sklepanja**: Sklepanje modela je prepočasno za zahteve v realnem času  
- **Poslabšanje natančnosti**: Optimizacija nesprejemljivo zmanjša natančnost modela  
- **Združljivost strojne opreme**: Model ni združljiv s ciljno strojno opremo  

### Strategije za odpravljanje napak  
- **Profiliranje zmogljivosti**: Uporabite funkcije sledenja AI Toolkit za identifikacijo ozkih grl  
- **Spremljanje virov**: Spremljajte pomnilnik in uporabo CPU med razvojem  
- **Postopno testiranje**: Testirajte optimizacije postopoma za izolacijo težav  
- **Simulacija strojne opreme**: Uporabite razvojna orodja za simulacijo ciljne strojne opreme  

### Rešitve za optimizacijo  
- **Dodatna kvantizacija**: Uporabite bolj agresivne tehnike kvantizacije  
- **Arhitektura modela**: Razmislite o različnih arhitekturah modelov, optimiziranih za rob  
- **Optimizacija predprocesiranja**: Optimizirajte predprocesiranje podatkov za omejitve robnih naprav  
- **Optimizacija sklepanja**: Uporabite optimizacije sklepanja, specifične za strojno opremo  

## Viri in naslednji koraki  

### Uradna dokumentacija  
- [Dokumentacija za razvijalce AI Toolkit](https://aka.ms/AIToolkit/doc)  
- [Vodnik za namestitev in nastavitev](https://code.visualstudio.com/docs/intelligentapps/overview#_install-and-setup)  
- [Dokumentacija za inteligentne aplikacije VS Code](https://code.visualstudio.com/docs/intelligentapps)  
- [Dokumentacija Model Context Protocol (MCP)](https://modelcontextprotocol.io/)  

### Skupnost in podpora  
- [GitHub repozitorij AI Toolkit](https://github.com/microsoft/vscode-ai-toolkit)  
- [GitHub težave in zahteve za funkcije](https://aka.ms/AIToolkit/feedback)  
- [Azure AI Foundry Discord skupnost](https://aka.ms/azureaifoundry/discord)  
- [Tržnica razširitev VS Code](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)  

### Tehnični viri  
- [Dokumentacija ONNX Runtime](https://onnxruntime.ai/)  
- [Dokumentacija Ollama](https://ollama.ai/)  
- [Dokumentacija Windows ML](https://docs.microsoft.com/en-us/windows/ai/)  
- [Dokumentacija Azure AI Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/)  

### Učne poti  
- [Tečaj osnov Edge AI](../Module01/README.md)  
- [Vodnik za majhne jezikovne modele](../Module02/README.md)  
- [Strategije uvedbe na robu](../Module03/README.md)  
- [Razvoj Edge AI za Windows](./windowdeveloper.md)  

### Dodatni viri  
- **Statistika repozitorija**: 1.8k+ zvezdic, 150+ vilic, 18+ sodelavcev  
- **Licenca**: MIT licenca  
- **Varnost**: Veljajo Microsoftove varnostne politike  
- **Telemetrija**: Upošteva nastavitve telemetrije VS Code  

## Zaključek  

AI Toolkit za Visual Studio Code predstavlja celovito platformo za sodoben razvoj AI, ki omogoča poenostavljeno razvijanje agentov, kar je še posebej koristno za aplikacije Edge AI. S svojim obsežnim katalogom modelov, ki podpira ponudnike, kot so Anthropic, OpenAI, GitHub in Google, v kombinaciji z lokalnim izvajanjem prek ONNX in Ollama, orodje ponuja prilagodljivost, potrebno za raznolike scenarije uvedbe na robu.  

Moč orodja je v integriranem pristopu—od odkrivanja modelov in eksperimentiranja v Playgroundu do sofisticiranega razvoja agentov z Prompt Builderjem, celovitih zmogljivosti ocenjevanja in brezhibne integracije MCP orodij. Za razvijalce Edge AI to pomeni hitro prototipiranje in testiranje AI agentov pred uvedbo na robu, z možnostjo hitrega iteriranja in optimizacije za okolja z omejenimi viri.  

Ključne prednosti za razvoj Edge AI vključujejo:  
- **Hitro eksperimentiranje**: Hitro testiranje modelov in agentov pred uvedbo na robu  
- **Prilagodljivost več ponudnikov**: Dostop do modelov iz različnih virov za iskanje optimalnih robnih rešitev  
- **Lokalni razvoj**: Testiranje z ONNX in Ollama za razvoj brez povezave in ohranjanje zasebnosti  
- **Pripravljenost na produkcijo**: Ustvarjanje produkcijsko pripravljene kode in integracija z zunanjimi orodji prek MCP  
- **Celovito ocenjevanje**: Uporaba vgrajenih in prilagojenih metrik za validacijo zmogljivosti Edge AI  

Ker se AI še naprej premika proti scenarijem uvedbe na robu, AI Toolkit za VS Code zagotavlja razvojno okolje in delovni tok, potrebna za gradnjo, testiranje in optimizacijo inteligentnih aplikacij za okolja z omejenimi viri. Ne glede na to, ali razvijate IoT rešitve, mobilne AI aplikacije ali vgrajene inteligentne sisteme, celovit nabor funkcij orodja in integriran delovni tok podpirata celoten življenjski cikel razvoja Edge AI.  

Z nenehnim razvojem in aktivno skupnostjo (1.8k+ GitHub zvezdic) AI Toolkit ostaja v ospredju orodij za razvoj AI, ki se nenehno razvijajo, da bi zadovoljila potrebe sodobnih razvijalcev AI, ki gradijo za scenarije uvedbe na robu.  

[Next Foundry Local](./foundrylocal.md)  

---

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za prevajanje AI [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne prevzemamo odgovornosti za morebitna nesporazumevanja ali napačne razlage, ki izhajajo iz uporabe tega prevoda.
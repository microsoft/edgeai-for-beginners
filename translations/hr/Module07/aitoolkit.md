# Alatni paket za umjetnu inteligenciju za Visual Studio Code - Vodič za razvoj Edge AI

## Uvod

Dobrodošli u sveobuhvatni vodič za korištenje Alatnog paketa za umjetnu inteligenciju za Visual Studio Code u razvoju Edge AI. Kako umjetna inteligencija prelazi s centraliziranog cloud računarstva na distribuirane edge uređaje, programeri trebaju moćne, integrirane alate koji mogu riješiti jedinstvene izazove edge implementacije - od ograničenja resursa do zahtjeva za offline radom.

Alatni paket za umjetnu inteligenciju za Visual Studio Code premošćuje tu prazninu pružajući potpuno razvojno okruženje posebno dizajnirano za izgradnju, testiranje i optimizaciju AI aplikacija koje učinkovito rade na edge uređajima. Bilo da razvijate za IoT senzore, mobilne uređaje, ugrađene sustave ili edge servere, ovaj paket pojednostavljuje cijeli vaš razvojni tijek u poznatom VS Code okruženju.

Ovaj vodič će vas provesti kroz ključne koncepte, alate i najbolje prakse za iskorištavanje Alatnog paketa u vašim Edge AI projektima, od početnog odabira modela do implementacije u proizvodnji.

## Pregled

Alatni paket za umjetnu inteligenciju za Visual Studio Code moćan je proširak koji pojednostavljuje razvoj agenata i stvaranje AI aplikacija. Paket pruža sveobuhvatne mogućnosti za istraživanje, evaluaciju i implementaciju AI modela iz širokog spektra pružatelja usluga—uključujući Anthropic, OpenAI, GitHub, Google—dok podržava lokalno izvođenje modela pomoću ONNX i Ollama.

Ono što Alatni paket izdvaja jest njegov sveobuhvatan pristup cijelom životnom ciklusu razvoja AI. Za razliku od tradicionalnih alata za razvoj AI koji se fokusiraju na pojedinačne aspekte, Alatni paket pruža integrirano okruženje koje pokriva otkrivanje modela, eksperimentiranje, razvoj agenata, evaluaciju i implementaciju—sve unutar poznatog VS Code okruženja.

Platforma je posebno dizajnirana za brzo prototipiranje i implementaciju u proizvodnji, s značajkama poput generiranja upita, brzih početaka, besprijekornih integracija MCP (Model Context Protocol) alata i opsežnih mogućnosti evaluacije. Za razvoj Edge AI, to znači da možete učinkovito razvijati, testirati i optimizirati AI aplikacije za scenarije edge implementacije, istovremeno održavajući puni razvojni tijek u VS Codeu.

## Ciljevi učenja

Do kraja ovog vodiča moći ćete:

### Temeljne kompetencije
- **Instalirati i konfigurirati** Alatni paket za umjetnu inteligenciju za Visual Studio Code za radne tokove razvoja Edge AI
- **Snalaženje i korištenje** sučelja Alatnog paketa, uključujući Katalog modela, Igralište i Izradu agenta
- **Odabrati i evaluirati** AI modele prikladne za edge implementaciju na temelju performansi i ograničenja resursa
- **Pretvoriti i optimizirati** modele koristeći ONNX format i tehnike kvantizacije za edge uređaje

### Vještine razvoja Edge AI
- **Dizajnirati i implementirati** Edge AI aplikacije koristeći integrirano razvojno okruženje
- **Izvesti testiranje modela** u uvjetima sličnim edge-u koristeći lokalno izvođenje i nadzor resursa
- **Stvoriti i prilagoditi** AI agente optimizirane za scenarije edge implementacije
- **Evaluirati izvedbu modela** koristeći metrike relevantne za edge računarstvo (latencija, korištenje memorije, točnost)

### Optimizacija i implementacija
- **Primijeniti tehnike kvantizacije i orezivanja** za smanjenje veličine modela uz održavanje prihvatljivih performansi
- **Optimizirati modele** za specifične edge hardverske platforme uključujući CPU, GPU i NPU ubrzanja
- **Provesti najbolje prakse** za razvoj edge AI-a uključujući upravljanje resursima i strategije rezervnih rješenja
- **Pripremiti modele i aplikacije** za produkcijsku implementaciju na edge uređajima

### Napredni koncepti Edge AI-a
- **Integrirati s edge AI okvirima** uključujući ONNX Runtime, Windows ML i TensorFlow Lite
- **Implementirati višemodelne arhitekture** i scenarije federiranog učenja za edge okruženja
- **Rješavati uobičajene probleme Edge AI-a** uključujući ograničenja memorije, brzinu izvođenja i hardversku kompatibilnost
- **Dizajnirati strategije nadzora i zapisivanja** za Edge AI aplikacije u produkciji

### Praktična primjena
- **Izgraditi cjelovita Edge AI rješenja** od odabira modela do implementacije
- **Demonstrirati stručnost** u razvojnim radnim tokovima i tehnikama optimizacije specifičnim za edge
- **Primijeniti naučene koncepte** na stvarne slučajeve uporabe Edge AI-a uključujući IoT, mobilne i ugrađene aplikacije
- **Evaluirati i usporediti** različite strategije implementacije Edge AI i njihove kompromise

## Ključne značajke za razvoj Edge AI-a

### 1. Katalog i otkrivanje modela
- **Podrška za više pružatelja usluga**: Pregledavanje i pristup AI modelima od Anthropic, OpenAI, GitHub, Google i drugih pružatelja
- **Integracija lokalnih modela**: Pojednostavljeno otkrivanje ONNX i Ollama modela za edge implementaciju
- **GitHub modeli**: Izravna integracija s GitHub hostingom modela za pojednostavljen pristup
- **Usporedba modela**: Usporedite modele jedan uz drugi kako biste pronašli optimalnu ravnotežu za ograničenja edge uređaja

### 2. Interaktivno igralište
- **Interaktivno testno okruženje**: Brzo eksperimentiranje s mogućnostima modela u kontroliranom okruženju
- **Podrška za više modaliteta**: Testiranje s slikama, tekstom i drugim unosima tipičnim za edge scenarije
- **Eksperimentiranje u stvarnom vremenu**: Trenutna povratna informacija o odgovorima i performansama modela
- **Optimizacija parametara**: Fino podešavanje parametara modela za zahtjeve edge implementacije

### 3. Izrada prompta (agenta)
- **Generiranje na prirodnom jeziku**: Generirajte početne promptove koristeći opise na prirodnom jeziku
- **Iterativno usavršavanje**: Poboljšavajte promptove na temelju odgovora modela i performansi
- **Razgradnja zadataka**: Razbijajte složene zadatke s povezivanjem promptova i strukturiranim rezultatima
- **Podrška za varijable**: Koristite varijable u promptovima za dinamičko ponašanje agenta
- **Generiranje produkcijskog koda**: Generirajte kod spreman za produkciju za brzi razvoj aplikacija

### 4. Masovno izvođenje i evaluacija
- **Testiranje više modela**: Izvršavajte više promptova istovremeno preko odabranih modela
- **Učinkovito testiranje u velikoj skali**: Testirajte razne ulaze i konfiguracije učinkovito
- **Prilagođeni testni slučajevi**: Pokrenite agente s testnim slučajevima za potvrdu funkcionalnosti
- **Usporedba performansi**: Usporedite rezultate među različitim modelima i konfiguracijama

### 5. Evaluacija modela s datasetovima
- **Standardne metrike**: Testirajte AI modele koristeći ugrađene evaluatore (F1 score, relevantnost, sličnost, koherencija)
- **Prilagođeni evaluatori**: Kreirajte vlastite metrike evaluacije za specifične slučajeve
- **Integracija datasetova**: Testirajte modele protiv opsežnih datasetova
- **Mjerenje performansi**: Kvantificirajte izvedbu modela za odluke o edge implementaciji

### 6. Mogućnosti fino podešavanja
- **Prilagodba modela**: Prilagodite modele za specifične slučajeve i domene
- **Specijalizirana adaptacija**: Prilagodite modele specijaliziranim domenama i zahtjevima
- **Edge optimizacija**: Fino podešavanje modela specifično za ograničenja edge implementacije
- **Trening specifičan za domenu**: Izradite modele prilagođene specifičnim slučajevima upotrebe na edge-u

### 7. Integracija MCP alata
- **Povezivost s vanjskim alatima**: Povežite agente s vanjskim alatima preko Model Context Protocol servera
- **Radnje u stvarnom svijetu**: Omogućite agentima da upituju baze podataka, pristupaju API-jima ili izvršavaju prilagođenu logiku
- **Postojeći MCP serveri**: Koristite alate iz komandnih (stdio) ili HTTP protokola (server-sent event)
- **Razvoj prilagođenih MCP servera**: Izgradite i postavite nove MCP servere uz testiranje u Agent Builderu

### 8. Razvoj i testiranje agenata
- **Podrška za pozivanje funkcija**: Omogućite agentima dinamičko pozivanje vanjskih funkcija
- **Testiranje integracije u stvarnom vremenu**: Testirajte integracije kroz izvođenja u stvarnom vremenu i korištenje alata
- **Verzioniranje agenata**: Kontrola verzija za agente s mogućnostima usporedbe evaluacijskih rezultata
- **Otklanjanje pogrešaka i praćenje**: Lokalno praćenje i otklanjanje pogrešaka za razvoj agenata

## Radni tijek razvoja Edge AI-a

### Faza 1: Otkrivanje i odabir modela
1. **Istražite katalog modela**: Koristite katalog modela za pronalaženje modela prikladnih za edge implementaciju
2. **Usporedite performanse**: Evaluirajte modele na temelju veličine, točnosti i brzine izvođenja
3. **Testirajte lokalno**: Koristite Ollama ili ONNX modele za lokalno testiranje prije edge implementacije
4. **Procijenite zahtjeve za resursima**: Odredite potrebe za memorijom i računalnim resursima za ciljne edge uređaje

### Faza 2: Optimizacija modela
1. **Konvertirajte u ONNX**: Pretvorite odabrane modele u ONNX format radi kompatibilnosti s edge-om
2. **Primijenite kvantizaciju**: Smanjite veličinu modela pomoću INT8 ili INT4 kvantizacije
3. **Optimizacija hardvera**: Optimizirajte za ciljani edge hardver (ARM, x86, specijalizirani akceleratori)
4. **Validacija performansi**: Potvrdite da optimizirani modeli održavaju prihvatljivu točnost

### Faza 3: Razvoj aplikacije
1. **Dizajn agenta**: Koristite Agent Builder za izradu AI agenata optimiziranih za edge
2. **Inženjering promptova**: Razvijte promptove koji učinkovito rade s manjim edge modelima
3. **Testiranje integracije**: Testirajte agente u simuliranim edge uvjetima
4. **Generiranje koda**: Generirajte produkcijski kod optimiziran za edge implementaciju

### Faza 4: Evaluacija i testiranje
1. **Evaluacija u serijama**: Testirajte više konfiguracija za pronalazak optimalnih edge postavki
2. **Profiliranje performansi**: Analizirajte brzinu izvođenja, korištenje memorije i točnost
3. **Simulacija edge-a**: Testirajte u uvjetima sličnim ciljanom edge okruženju
4. **Testiranje opterećenja**: Evaluirajte performanse pod različitim uvjetima opterećenja

### Faza 5: Priprema za implementaciju
1. **Završna optimizacija**: Primijenite završne optimizacije na temelju rezultata testiranja
2. **Pakiranje za implementaciju**: Spakirajte modele i kod za edge implementaciju
3. **Dokumentacija**: Dokumentirajte zahtjeve i konfiguraciju implementacije
4. **Postavljanje nadzora**: Pripremite nadzor i zapisivanje za edge implementaciju

## Ciljana publika za razvoj Edge AI-a

### Edge AI programeri
- Programeri aplikacija koji grade edge uređaje i IoT rješenja pokretana umjetnom inteligencijom
- Programeri ugrađenih sustava koji integriraju AI sposobnosti u uređaje s ograničenim resursima
- Mobilni programeri koji stvaraju AI aplikacije na uređajima poput pametnih telefona i tableta

### Edge AI inženjeri
- AI inženjeri koji optimiziraju modele za edge implementaciju i upravljaju procesima izvođenja
- DevOps inženjeri koji implementiraju i upravljaju AI modelima kroz distribuiranu edge infrastrukturu
- Inženjeri za performanse koji optimiziraju AI radna opterećenja za ograničenja edge hardvera

### Istraživači i edukatori
- Istraživači AI-a koji razvijaju učinkovite modele i algoritme za edge računarstvo
- Edukatori koji podučavaju koncepte Edge AI-a i demonstriraju tehnike optimizacije
- Studenti koji uče o izazovima i rješenjima u edge AI implementaciji

## Slučajevi uporabe Edge AI-a

### Pametni IoT uređaji
- **Prepoznavanje slike u stvarnom vremenu**: Implementirajte modele računalnog vida na IoT kamerama i senzorima
- **Obrada glasa**: Provedite prepoznavanje govora i obradu prirodnog jezika na pametnim zvučnicima
- **Prediktivno održavanje**: Pokrenite modele za otkrivanje anomalija na industrijskim edge uređajima
- **Praćenje okoliša**: Implementirajte modele analize senzorskih podataka za aplikacije zaštite okoliša

### Mobilne i ugrađene aplikacije
- **Prevođenje na uređaju**: Implementirajte modele za prevođenje jezika koji rade offline
- **Proširena stvarnost**: Implementirajte prepoznavanje i praćenje objekata u stvarnom vremenu za AR aplikacije
- **Praćenje zdravlja**: Pokrenite modele zdravstvene analize na nosivim uređajima i medicinskoj opremi
- **Autonomni sustavi**: Implementirajte modele donošenja odluka za dronove, robote i vozila

### Infrastruktura edge računarstva
- **Edge podatkovni centri**: Implementirajte AI modele u edge podatkovnim centrima za aplikacije niske latencije
- **Integracija CDN-a**: Uključite AI procesne sposobnosti u mreže za isporuku sadržaja
- **5G Edge**: Iskoristite 5G edge računarstvo za AI-pokretane aplikacije
- **Fog računarstvo**: Implementirajte AI obradu u fog računalnim okruženjima

## Instalacija i postavljanje

### Instalacija proširenja
Instalirajte proširenje Alatni paket AI izravno s Visual Studio Code Marketplace-a:

**ID proširenja**: `ms-windows-ai-studio.windows-ai-studio`

**Metode instalacije**:
1. **VS Code Marketplace**: Potražite "AI Toolkit" u prikazu proširenja
2. **Komandna linija**: `code --install-extension ms-windows-ai-studio.windows-ai-studio`
3. **Izravna instalacija**: Preuzmite s [VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)

### Preduvjeti za razvoj Edge AI-a
- **Visual Studio Code**: Preporučena najnovija verzija
- **Python okruženje**: Python 3.8+ s potrebnim AI bibliotekama
- **ONNX Runtime** (Opcionalno): Za izvođenje ONNX modela
- **Ollama** (Opcionalno): Za lokalno posluživanje modela
- **Alati za hardversko ubrzanje**: CUDA, OpenVINO ili platformno specifični akceleratori

### Početna konfiguracija
1. **Aktivacija proširenja**: Otvorite VS Code i provjerite pojavljuje li se Alatni paket AI u traci aktivnosti
2. **Postavljanje pružatelja modela**: Konfigurirajte pristup GitHub-u, OpenAI-u, Anthropic-u ili drugim pružateljima modela
3. **Lokalno okruženje**: Postavite Python okruženje i instalirajte potrebne pakete
4. **Hardversko ubrzanje**: Konfigurirajte GPU/NPU ubrzanje ako je dostupno
5. **Integracija MCP-a**: Postavite Model Context Protocol servere ako je potrebno

### Popis za prvu instalaciju
- [ ] Alatni paket AI proširenje instalirano i aktivirano
- [ ] Katalog modela dostupan i modeli otkrivljivi
- [ ] Igralište funkcionalno za testiranje modela
- [ ] Agent Builder dostupan za razvoj promptova
- [ ] Lokalno razvojno okruženje konfigurirano
- [ ] Hardversko ubrzanje (ako je dostupno) pravilno konfigurirano

## Početak rada s Alatnim paketom AI

### Vodič za brz početak

Preporučujemo početak s modelima hostanim na GitHub-u za najjednostavnije iskustvo:

1. **Instalacija**: Slijedite [vodič za instalaciju](https://code.visualstudio.com/docs/intelligentapps/overview#_install-and-setup) za postavljanje Alatnog paketa AI za vaš uređaj
2. **Otkrivanje modela**: Iz prikaza stabla proširenja odaberite **CATALOG > Models** za istraživanje dostupnih modela
3. **GitHub modeli**: Počnite s modelima hostanim na GitHub-u za optimalnu integraciju
4. **Testiranje na igralištu**: Iz bilo koje kartice modela odaberite **Try in Playground** za početak eksperimentiranja s mogućnostima modela

### Korak-po-korak razvoj Edge AI-a

#### Korak 1: Istraživanje i odabir modela
1. Otvorite prikaz Alatnog paketa AI u traci aktivnosti VS Code
2. Pregledajte Katalog modela za modele prikladne za edge implementaciju
3. Filtrirajte prema pružatelju (GitHub, ONNX, Ollama) prema vašim edge zahtjevima
4. Koristite **Try in Playground** za odmah testiranje sposobnosti modela

#### Korak 2: Razvoj agenta
1. Koristite **Prompt (Agent) Builder** za izradu AI agenata optimiziranih za edge
2. Generirajte početne upite koristeći opise na prirodnom jeziku
3. Iterativno usavršavajte upite na temelju odgovora modela
4. Integrirajte MCP alate za proširene mogućnosti agenata


#### Korak 3: Testiranje i evaluacija
1. Koristite **Bulk Run** za testiranje više upita na odabranim modelima
2. Pokrenite agente s testnim slučajevima za provjeru funkcionalnosti
3. Procijenite točnost i izvedbu koristeći ugrađene ili prilagođene metrike
4. Usporedite različite modele i konfiguracije

#### Korak 4: Fino podešavanje i optimizacija
1. Prilagodite modele za specifične rubne slučajeve
2. Primijenite fino podešavanje specifično za domen
3. Optimizirajte za ograničenja rubnog postavljanja
4. Verzija i usporedba različitih konfiguracija agenata

#### Korak 5: Priprema za implementaciju
1. Generirajte kod spreman za proizvodnju koristeći Agent Builder
2. Postavite veze s MCP serverom za upotrebu u proizvodnji
3. Pripremite pakete za implementaciju na rubne uređaje
4. Konfigurirajte metrike nadzora i evaluacije

## Primjeri za AI Toolkit

Isprobajte naše primjere
[AI Toolkit primjeri](https://github.com/Azure-Samples/AI_Toolkit_Samples) dizajnirani su da pomognu developerima i istraživačima u istraživanju i učinkovitoj implementaciji AI rješenja.

Naši primjeri uključuju:

Primjerni kod: unaprijed izrađeni primjeri koji demonstriraju AI funkcionalnosti, poput treniranja, implementacije ili integracije modela u aplikacije.
Dokumentaciju: vodiče i tutorijale koji pomažu korisnicima razumjeti značajke AI Toolkita i kako ih koristiti.
Preduvjeti

- Visual Studio Code
- AI Toolkit za Visual Studio Code
- GitHub Fine-grained personal access token (PAT)
- Foundry Local

## Najbolji postupci za razvoj Edge AI

### Odabir modela
- **Veličinska ograničenja**: Odaberite modele koji stanu unutar memorijskih ograničenja ciljnih uređaja
- **Brzina izvođenja**: Prioritizirajte modele s brzom izvedbom za aplikacije u stvarnom vremenu
- **Trgovina točnosti**: Izbalansirajte preciznost modela s ograničenjima resursa
- **Kompatibilnost formata**: Dajte prednost ONNX ili formatima optimiziranim za hardver za rubnu implementaciju

### Tehnike optimizacije
- **Kvantizacija**: Koristite INT8 ili INT4 kvantizaciju za smanjenje veličine modela i poboljšanje brzine
- **Prune**: Uklonite nepotrebne parametre modela za smanjenje zahtjeva za računanje
- **Destilacija znanja**: Kreirajte manje modele koji održavaju performanse većih
- **Hardversko ubrzanje**: Iskoristite NPU, GPU ili specijalizirane akceleratore kad su dostupni

### Radni tijek razvoja
- **Iterativno testiranje**: Redovito testirajte u uvjetima sličnim rubu tijekom razvoja
- **Praćenje performansi**: Kontinuirano pratite korištenje resursa i brzinu izvođenja
- **Upravljanje verzijama**: Pratite verzije modela i postavke optimizacije
- **Dokumentacija**: Dokumentirajte sve odluke o optimizaciji i trgovinu performansama

### Razmatranja pri implementaciji
- **Praćenje resursa**: Pratite memoriju, CPU i potrošnju energije u proizvodnji
- **Strategije zamjene**: Implementirajte mehanizme rezervnog rada za kvarove modela
- **Mehanizmi ažuriranja**: Planirajte ažuriranja modela i upravljanje verzijama
- **Sigurnost**: Implementirajte odgovarajuće sigurnosne mjere za rubne AI aplikacije

## Integracija s Edge AI okvirima

### ONNX Runtime
- **Višeplatformska implementacija**: Implementirajte ONNX modele na različite rubne platforme
- **Optimizacija hardvera**: Iskoristite hardverske specifične optimizacije ONNX Runtime
- **Podrška za mobilne uređaje**: Koristite ONNX Runtime Mobile za aplikacije na pametnim telefonima i tabletima
- **IoT integracija**: Implementirajte na IoT uređaje koristeći lagane distribucije ONNX Runtime

### Windows ML
- **Windows uređaji**: Optimizirajte za Windows-based rubne uređaje i računala
- **NPU ubrzanje**: Iskoristite Neural Processing Units na Windows uređajima
- **DirectML**: Koristite DirectML za ubrzanje na GPU-u za Windows platforme
- **UWP integracija**: Integrirajte s Universal Windows Platform aplikacijama

### TensorFlow Lite
- **Optimizacija za mobilne uređaje**: Implementirajte TensorFlow Lite modele na mobilne i ugrađene uređaje
- **Hardverski delegati**: Koristite specijalizirane hardverske delegate za ubrzanje
- **Mikrokontroleri**: Implementirajte na mikrokontrolere koristeći TensorFlow Lite Micro
- **Višeplatformska podrška**: Implementirajte na Android, iOS i ugrađene Linux sustave

### Azure IoT Edge
- **Hibridni cloud-rub**: Kombinirajte treniranje u cloudu s izvođenjem na rubu
- **Implementacija modula**: Implementirajte AI modele kao IoT Edge module
- **Upravljanje uređajima**: Daljinski upravljajte rubnim uređajima i ažuriranjima modela
- **Telemetrija**: Prikupite podatke performansi i metrike modela iz rubnih implementacija

## Napredni scenariji Edge AI

### Implementacija više modela
- **Model ansambli**: Implementirajte više modela za poboljšanu točnost ili redundanciju
- **A/B testiranje**: Istovremeno testirajte različite modele na rubnim uređajima
- **Dinamički odabir**: Odaberite modele na temelju trenutnih uvjeta uređaja
- **Podjela resursa**: Optimizirajte korištenje resursa među više implementiranih modela

### Federated učenje
- **Distribuirano treniranje**: Trenirajte modele na više rubnih uređaja
- **Zaštita privatnosti**: Podatke za treniranje držite lokalno dok dijelite poboljšanja modela
- **Suradničko učenje**: Omogućite uređajima učenje iz kolektivnih iskustava
- **Koordinacija rub-cloud**: Koordinirajte učenje između rubnih uređaja i cloud infrastrukture

### Obrada u stvarnom vremenu
- **Obrada tokova**: Obradite kontinuirane tokove podataka na rubnim uređajima
- **Niska latencija izvođenja**: Optimizirajte za minimalnu latenciju izvođenja
- **Serijska obrada**: Učinkovito obrađujte skupove podataka na rubnim uređajima
- **Adaptivna obrada**: Prilagodite obradu prema trenutnim mogućnostima uređaja

## Rješavanje problema u razvoju Edge AI

### Česti problemi
- **Ograničenja memorije**: Model prevelik za memoriju ciljnih uređaja
- **Brzina izvođenja**: Izvođenje modela presporo za zahtjeve u stvarnom vremenu
- **Degradacija točnosti**: Optimizacija neprihvatljivo smanjuje točnost modela
- **Kompatibilnost hardvera**: Model nije kompatibilan s ciljanim hardverom

### Strategije ispravljanja
- **Profiliranje performansi**: Koristite značajke praćenja AI Toolkita za identificiranje uskih grla
- **Praćenje resursa**: Pratite memoriju i CPU tijekom razvoja
- **Postupno testiranje**: Testirajte optimizacije inkrementalno za izoliranje problema
- **Simulacija hardvera**: Koristite alate za razvoj za simulaciju ciljanog hardvera

### Rješenja za optimizaciju
- **Daljnja kvantizacija**: Primijenite agresivnije tehnike kvantizacije
- **Arhitektura modela**: Razmotrite različite arhitekture modela optimizirane za rubne uređaje
- **Optimizacija predprocesiranja**: Optimizirajte obradu podataka za rubna ograničenja
- **Optimizacija izvođenja**: Koristite hardverski specifične optimizacije izvođenja

## Resursi i sljedeći koraci

### Službena dokumentacija
- [AI Toolkit Developer Documentation](https://aka.ms/AIToolkit/doc)
- [Installation and Setup Guide](https://code.visualstudio.com/docs/intelligentapps/overview#_install-and-setup)
- [VS Code Intelligent Apps Documentation](https://code.visualstudio.com/docs/intelligentapps)
- [Model Context Protocol (MCP) Documentation](https://modelcontextprotocol.io/)

### Zajednica i podrška
- [AI Toolkit GitHub Repository](https://github.com/microsoft/vscode-ai-toolkit)
- [GitHub Issues and Feature Requests](https://aka.ms/AIToolkit/feedback)
- [Azure AI Foundry Discord Community](https://aka.ms/azureaifoundry/discord)
- [VS Code Extension Marketplace](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)

### Tehnički resursi
- [ONNX Runtime Documentation](https://onnxruntime.ai/)
- [Ollama Documentation](https://ollama.ai/)
- [Windows ML Documentation](https://docs.microsoft.com/en-us/windows/ai/)
- [Azure AI Foundry Documentation](https://learn.microsoft.com/en-us/azure/ai-foundry/)

### Putovi učenja
- [Edge AI Fundamentals Course](../Module01/README.md)
- [Small Language Models Guide](../Module02/README.md)
- [Edge Deployment Strategies](../Module03/README.md)
- [Windows Edge AI Development](./windowdeveloper.md)

### Dodatni resursi
- **Statistika repozitorija**: 1.8k+ zvjezdica, 150+ forkova, 18+ suradnika
- **Licenca**: MIT licenca
- **Sigurnost**: Primjenjuju se Microsoft sigurnosne politike
- **Telemetrija**: Poštuje postavke telemetrije VS Code

## Zaključak

AI Toolkit za Visual Studio Code predstavlja sveobuhvatnu platformu za suvremeni AI razvoj, pružajući pojednostavljene mogućnosti razvoja agenata koje su posebno vrijedne za Edge AI aplikacije. Sa svojim opsežnim katalogom modela koji podržavaju pružatelje poput Anthropic, OpenAI, GitHub i Google, u kombinaciji s lokalnim izvršavanjem preko ONNX i Ollama, toolkit nudi fleksibilnost potrebnu za raznolike scenarije rubne implementacije.

Snaga toolkit-a leži u njegovom integriranom pristupu — od otkrivanja modela i eksperimentiranja u Playgroundu preko sofisticiranog razvoja agenata s Prompt Builderom, sveobuhvatne evaluacije, do besprijekorne integracije s MCP alatima. Za Edge AI developere, to znači brzo prototipiranje i testiranje AI agenata prije implementacije na rub, s mogućnošću brzih iteracija i optimizacije za okruženja s ograničenim resursima.

Ključne prednosti za razvoj Edge AI uključuju:
- **Brzo eksperimentiranje**: Testirajte modele i agente brzo prije nego što se obvežete na rubnu implementaciju
- **Fleksibilnost višestrukih pružatelja**: Pristupite modelima iz raznih izvora kako biste pronašli optimalna rubna rješenja
- **Lokalni razvoj**: Testirajte s ONNX i Ollama za razvoj izvan mreže i s očuvanjem privatnosti
- **Spremnost za proizvodnju**: Generirajte kod spreman za proizvodnju i integrirajte s vanjskim alatima preko MCP-a
- **Sveobuhvatna evaluacija**: Koristite ugrađene i prilagođene metrike za potvrdu performansi Edge AI

Kako AI nastavlja kretati prema scenarijima rubne implementacije, AI Toolkit za VS Code pruža razvojno okruženje i radni tijek potrebne za izgradnju, testiranje i optimizaciju inteligentnih aplikacija za okruženja s ograničenim resursima. Bilo da razvijate IoT rješenja, mobilne AI aplikacije ili ugrađene inteligentne sustave, toolkit-ov sveobuhvatni skup značajki i integrirani radni tijek podržavaju cijeli životni ciklus Edge AI razvoja.

S kontinuiranim razvojem i aktivnom zajednicom (1.8k+ zvjezdica na GitHubu), AI Toolkit ostaje na vrhu AI razvojnih alata, kontinuirano se razvijajući kako bi zadovoljio potrebe suvremenih AI developera koji grade za scenarije rubne implementacije.

[Next Foundry Local](./foundrylocal.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
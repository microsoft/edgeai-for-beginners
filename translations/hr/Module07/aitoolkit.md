# AI alat za Visual Studio Code - Vodič za razvoj Edge AI-a

## Uvod

Dobrodošli u sveobuhvatni vodič za korištenje AI alata za Visual Studio Code u razvoju Edge AI-a. Kako umjetna inteligencija prelazi s centraliziranog računalstva u oblaku na distribuirane rubne uređaje, programerima su potrebni moćni, integrirani alati koji mogu riješiti jedinstvene izazove rubne implementacije - od ograničenja resursa do zahtjeva za rad u offline načinu.

AI alat za Visual Studio Code premošćuje ovaj jaz pružajući kompletno razvojno okruženje posebno dizajnirano za izradu, testiranje i optimizaciju AI aplikacija koje učinkovito rade na rubnim uređajima. Bez obzira razvijate li za IoT senzore, mobilne uređaje, ugrađene sustave ili rubne servere, ovaj alat pojednostavljuje cijeli vaš razvojni proces unutar poznatog okruženja VS Code-a.

Ovaj vodič će vas provesti kroz ključne koncepte, alate i najbolje prakse za korištenje AI alata u vašim Edge AI projektima, od početnog odabira modela do implementacije u produkciju.

## Pregled

AI alat za Visual Studio Code je moćan dodatak koji pojednostavljuje razvoj agenata i stvaranje AI aplikacija. Alat pruža sveobuhvatne mogućnosti za istraživanje, evaluaciju i implementaciju AI modela od širokog spektra pružatelja usluga—uključujući Anthropic, OpenAI, GitHub, Google—dok podržava lokalno izvršavanje modela koristeći ONNX i Ollama.

Ono što AI alat čini posebnim je njegov sveobuhvatan pristup cijelom životnom ciklusu razvoja AI-a. Za razliku od tradicionalnih alata za razvoj AI-a koji se fokusiraju na pojedine aspekte, AI alat pruža integrirano okruženje koje pokriva otkrivanje modela, eksperimentiranje, razvoj agenata, evaluaciju i implementaciju—sve unutar poznatog okruženja VS Code-a.

Platforma je posebno dizajnirana za brzo prototipiranje i implementaciju u produkciju, s funkcijama poput generiranja promptova, brzih početaka, besprijekornih integracija MCP (Model Context Protocol) alata i opsežnih mogućnosti evaluacije. Za razvoj Edge AI-a, to znači da možete učinkovito razvijati, testirati i optimizirati AI aplikacije za scenarije rubne implementacije dok održavate cijeli razvojni proces unutar VS Code-a.

## Ciljevi učenja

Na kraju ovog vodiča, moći ćete:

### Osnovne kompetencije
- **Instalirati i konfigurirati** AI alat za Visual Studio Code za Edge AI razvojne procese
- **Navigirati i koristiti** sučelje AI alata, uključujući Katalog modela, Playground i Agent Builder
- **Odabrati i evaluirati** AI modele prikladne za rubnu implementaciju na temelju performansi i ograničenja resursa
- **Konvertirati i optimizirati** modele koristeći ONNX format i tehnike kvantizacije za rubne uređaje

### Vještine razvoja Edge AI-a
- **Dizajnirati i implementirati** Edge AI aplikacije koristeći integrirano razvojno okruženje
- **Testirati modele** u uvjetima sličnim rubnim koristeći lokalnu inferenciju i praćenje resursa
- **Kreirati i prilagoditi** AI agente optimizirane za scenarije rubne implementacije
- **Evaluirati performanse modela** koristeći metrike relevantne za rubno računalstvo (kašnjenje, potrošnja memorije, točnost)

### Optimizacija i implementacija
- **Primijeniti kvantizaciju i obrezivanje** za smanjenje veličine modela uz održavanje prihvatljivih performansi
- **Optimizirati modele** za specifične rubne hardverske platforme uključujući CPU, GPU i NPU akceleraciju
- **Primijeniti najbolje prakse** za razvoj Edge AI-a uključujući upravljanje resursima i strategije povratka
- **Pripremiti modele i aplikacije** za implementaciju u produkciju na rubnim uređajima

### Napredni koncepti Edge AI-a
- **Integrirati s rubnim AI okvirima** uključujući ONNX Runtime, Windows ML i TensorFlow Lite
- **Implementirati arhitekture s više modela** i scenarije federativnog učenja za rubna okruženja
- **Rješavati uobičajene probleme Edge AI-a** uključujući ograničenja memorije, brzinu inferencije i kompatibilnost hardvera
- **Dizajnirati strategije praćenja i zapisivanja** za Edge AI aplikacije u produkciji

### Praktična primjena
- **Izgraditi cjelovita Edge AI rješenja** od odabira modela do implementacije
- **Demonstrirati stručnost** u razvojnim procesima specifičnim za rub i tehnikama optimizacije
- **Primijeniti naučene koncepte** na stvarne Edge AI slučajeve korištenja uključujući IoT, mobilne i ugrađene aplikacije
- **Evaluirati i usporediti** različite strategije implementacije Edge AI-a i njihove kompromise

## Ključne značajke za razvoj Edge AI-a

### 1. Katalog modela i otkrivanje
- **Podrška za više pružatelja usluga**: Pregledajte i pristupite AI modelima od Anthropic, OpenAI, GitHub, Google i drugih pružatelja
- **Integracija lokalnih modela**: Pojednostavljeno otkrivanje ONNX i Ollama modela za rubnu implementaciju
- **GitHub modeli**: Direktna integracija s GitHub-ovim hostingom modela za pojednostavljen pristup
- **Usporedba modela**: Usporedite modele jedan uz drugi kako biste pronašli optimalnu ravnotežu za ograničenja rubnih uređaja

### 2. Interaktivni Playground
- **Interaktivno testno okruženje**: Brzo eksperimentiranje s mogućnostima modela u kontroliranom okruženju
- **Podrška za više modaliteta**: Testirajte s slikama, tekstom i drugim ulazima tipičnim za rubne scenarije
- **Eksperimentiranje u stvarnom vremenu**: Trenutne povratne informacije o odgovorima modela i performansama
- **Optimizacija parametara**: Fino podešavanje parametara modela za zahtjeve rubne implementacije

### 3. Builder za promptove (agente)
- **Generiranje prirodnog jezika**: Generirajte početne promptove koristeći opise na prirodnom jeziku
- **Iterativno poboljšanje**: Poboljšajte promptove na temelju odgovora modela i performansi
- **Razlaganje zadataka**: Razložite složene zadatke pomoću lančanja promptova i strukturiranih izlaza
- **Podrška za varijable**: Koristite varijable u promptovima za dinamično ponašanje agenata
- **Generiranje produkcijskog koda**: Generirajte kod spreman za produkciju za brzo razvijanje aplikacija

### 4. Masovno pokretanje i evaluacija
- **Testiranje više modela**: Izvršite više promptova na odabranim modelima istovremeno
- **Učinkovito testiranje u velikom opsegu**: Testirajte različite ulaze i konfiguracije učinkovito
- **Prilagođeni testni slučajevi**: Pokrenite agente s testnim slučajevima za validaciju funkcionalnosti
- **Usporedba performansi**: Usporedite rezultate različitih modela i konfiguracija

### 5. Evaluacija modela s datasetima
- **Standardne metrike**: Testirajte AI modele koristeći ugrađene evaluatore (F1 score, relevantnost, sličnost, koherencija)
- **Prilagođeni evaluatori**: Kreirajte vlastite evaluacijske metrike za specifične slučajeve korištenja
- **Integracija dataseta**: Testirajte modele na opsežnim datasetima
- **Mjerenje performansi**: Kvantificirajte performanse modela za odluke o rubnoj implementaciji

### 6. Mogućnosti fine-tuninga
- **Prilagodba modela**: Prilagodite modele za specifične slučajeve korištenja i domene
- **Specijalizirana adaptacija**: Prilagodite modele specijaliziranim domenama i zahtjevima
- **Optimizacija za rub**: Fino podesite modele posebno za ograničenja rubne implementacije
- **Trening specifičan za domenu**: Kreirajte modele prilagođene specifičnim rubnim slučajevima korištenja

### 7. Integracija MCP alata
- **Povezivanje s vanjskim alatima**: Povežite agente s vanjskim alatima putem Model Context Protocol servera
- **Akcije u stvarnom svijetu**: Omogućite agentima da upitaju baze podataka, pristupe API-ima ili izvrše prilagođenu logiku
- **Postojeći MCP serveri**: Koristite alate iz naredbenog (stdio) ili HTTP (server-sent event) protokola
- **Razvoj prilagođenih MCP-a**: Izgradite i postavite nove MCP servere s testiranjem u Agent Builderu

### 8. Razvoj i testiranje agenata
- **Podrška za pozivanje funkcija**: Omogućite agentima da dinamički pozivaju vanjske funkcije
- **Testiranje integracija u stvarnom vremenu**: Testirajte integracije s pokretanjem u stvarnom vremenu i korištenjem alata
- **Verzioniranje agenata**: Kontrola verzija za agente s mogućnostima usporedbe rezultata evaluacije
- **Debugging i praćenje**: Lokalno praćenje i debugging mogućnosti za razvoj agenata

## Proces razvoja Edge AI-a

### Faza 1: Otkrivanje i odabir modela
1. **Istražite katalog modela**: Koristite katalog modela za pronalaženje modela prikladnih za rubnu implementaciju
2. **Usporedite performanse**: Evaluirajte modele na temelju veličine, točnosti i brzine inferencije
3. **Testirajte lokalno**: Koristite Ollama ili ONNX modele za lokalno testiranje prije rubne implementacije
4. **Procijenite zahtjeve resursa**: Odredite memorijske i računalne potrebe za ciljne rubne uređaje

### Faza 2: Optimizacija modela
1. **Konvertirajte u ONNX**: Konvertirajte odabrane modele u ONNX format za kompatibilnost s rubom
2. **Primijenite kvantizaciju**: Smanjite veličinu modela kroz INT8 ili INT4 kvantizaciju
3. **Optimizacija hardvera**: Optimizirajte za ciljni rubni hardver (ARM, x86, specijalizirani akceleratori)
4. **Validacija performansi**: Validirajte da optimizirani modeli održavaju prihvatljivu točnost

### Faza 3: Razvoj aplikacija
1. **Dizajn agenata**: Koristite Agent Builder za kreiranje agenata optimiziranih za rub
2. **Inženjering promptova**: Razvijajte promptove koji učinkovito rade s manjim rubnim modelima
3. **Testiranje integracija**: Testirajte agente u simuliranim rubnim uvjetima
4. **Generiranje koda**: Generirajte produkcijski kod optimiziran za rubnu implementaciju

### Faza 4: Evaluacija i testiranje
1. **Masovna evaluacija**: Testirajte više konfiguracija kako biste pronašli optimalne postavke za rub
2. **Profiliranje performansi**: Analizirajte brzinu inferencije, potrošnju memorije i točnost
3. **Simulacija ruba**: Testirajte u uvjetima sličnim ciljnim rubnim okruženjima
4. **Testiranje opterećenja**: Evaluirajte performanse pod različitim uvjetima opterećenja

### Faza 5: Priprema za implementaciju
1. **Završna optimizacija**: Primijenite završne optimizacije na temelju rezultata testiranja
2. **Pakiranje za implementaciju**: Pakirajte modele i kod za rubnu implementaciju
3. **Dokumentacija**: Dokumentirajte zahtjeve za implementaciju i konfiguraciju
4. **Postavljanje praćenja**: Pripremite praćenje i zapisivanje za rubnu implementaciju

## Ciljna publika za razvoj Edge AI-a

### Razvijatelji Edge AI-a
- Razvijatelji aplikacija koji grade AI uređaje i IoT rješenja
- Razvijatelji ugrađenih sustava koji integriraju AI mogućnosti u uređaje s ograničenim resursima
- Mobilni razvijatelji koji stvaraju AI aplikacije na uređaju za pametne telefone i tablete

### Inženjeri Edge AI-a
- AI inženjeri koji optimiziraju modele za rubnu implementaciju i upravljaju inferencijskim procesima
- DevOps inženjeri koji implementiraju i upravljaju AI modelima na distribuiranoj rubnoj infrastrukturi
- Inženjeri performansi koji optimiziraju AI radna opterećenja za ograničenja rubnog hardvera

### Istraživači i edukatori
- AI istraživači koji razvijaju učinkovite modele i algoritme za rubno računalstvo
- Edukatori koji podučavaju koncepte Edge AI-a i demonstriraju tehnike optimizacije
- Studenti koji uče o izazovima i rješenjima u implementaciji Edge AI-a

## Slučajevi korištenja Edge AI-a

### Pametni IoT uređaji
- **Prepoznavanje slika u stvarnom vremenu**: Implementacija modela računalnog vida na IoT kamerama i senzorima
- **Obrada glasa**: Primjena modela za prepoznavanje govora i obradu prirodnog jezika na pametnim zvučnicima
- **Prediktivno održavanje**: Pokretanje modela za otkrivanje anomalija na industrijskim rubnim uređajima
- **Praćenje okoliša**: Implementacija modela za analizu podataka senzora u aplikacijama za okoliš

### Mobilne i ugrađene aplikacije
- **Prevođenje na uređaju**: Implementacija modela za prevođenje jezika koji rade offline
- **Proširena stvarnost**: Implementacija prepoznavanja objekata u stvarnom vremenu i praćenja za AR aplikacije
- **Praćenje zdravlja**: Pokretanje modela za analizu zdravlja na nosivim uređajima i medicinskoj opremi
- **Autonomni sustavi**: Implementacija modela za donošenje odluka za dronove, robote i vozila

### Rubna računalna infrastruktura
- **Rubni podatkovni centri**: Implementacija AI modela u rubnim podatkovnim centrima za aplikacije s niskim kašnjenjem
- **Integracija CDN-a**: Integracija AI mogućnosti obrade u mreže za isporuku sadržaja
- **5G rub**: Iskorištavanje 5G rubnog računalstva za AI aplikacije
- **Fog računalstvo**: Implementacija AI obrade u okruženjima fog računalstva

## Instalacija i postavljanje

### Instalacija dodatka
Instalirajte AI alat direktno iz Visual Studio Code Marketplace-a:

**ID dodatka**: `ms-windows-ai-studio.windows-ai-studio`

**Metode instalacije**:
1. **VS Code Marketplace**: Pretražite "AI Toolkit" u prikazu Extensions
2. **Komandna linija**: `code --install-extension ms-windows-ai-studio.windows-ai-studio`
3. **Direktna instalacija**: Preuzmite s [VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)

### Preduvjeti za razvoj Edge AI-a
- **Visual Studio Code**: Preporučuje se najnovija verzija
- **Python okruženje**: Python 3.8+ s potrebnim AI bibliotekama
- **ONNX Runtime** (opcionalno): Za inferenciju ONNX modela
- **Ollama** (opcionalno): Za lokalno posluživanje modela
- **Alati za hardversku akceleraciju**: CUDA, OpenVINO ili akceleratori specifični za platformu

### Početna konfiguracija
1. **Aktivacija dodatka**: Otvorite VS Code i provjerite da se AI alat pojavljuje u Activity Baru
2. **Postavljanje pružatelja modela**: Konfigurirajte pristup GitHub-u, OpenAI-u, Anthropic-u ili drugim pružateljima modela
3. **Lokalno okruženje**: Postavite Python okruženje i instalirajte potrebne pakete
4. **Hardverska akceleracija**: Konfigurirajte GPU/NPU akceleraciju ako je dostupna
5. **Integracija MCP-a**: Postavite Model Context Protocol servere ako je potrebno

### Popis za početno postavljanje
- [ ] AI alat instaliran i aktiviran
- [ ] Katalog modela dostupan i modeli otkriveni
- [ ] Playground funkcionalan za testiranje modela
- [ ] Agent Builder dostupan za razvoj promptova
- [ ] Lokalno razvojno okruženje konfigurirano
- [ ] Hardverska akceleracija (ako je dostup
2. Generirajte početne upite koristeći opise u prirodnom jeziku  
3. Iterirajte i poboljšavajte upite na temelju odgovora modela  
4. Integrirajte MCP alate za poboljšane sposobnosti agenata  

#### Korak 3: Testiranje i evaluacija  
1. Koristite **Bulk Run** za testiranje više upita na odabranim modelima  
2. Pokrenite agente s testnim slučajevima kako biste provjerili funkcionalnost  
3. Procijenite točnost i performanse koristeći ugrađene ili prilagođene metrike  
4. Usporedite različite modele i konfiguracije  

#### Korak 4: Fino podešavanje i optimizacija  
1. Prilagodite modele za specifične rubne slučajeve  
2. Primijenite fino podešavanje specifično za domenu  
3. Optimizirajte za ograničenja rubnog postavljanja  
4. Verzionirajte i usporedite različite konfiguracije agenata  

#### Korak 5: Priprema za implementaciju  
1. Generirajte kod spreman za produkciju koristeći Agent Builder  
2. Postavite MCP server veze za produkcijsku upotrebu  
3. Pripremite pakete za implementaciju na rubnim uređajima  
4. Konfigurirajte metrike za praćenje i evaluaciju  

## Primjeri za AI Toolkit  

Isprobajte naše primjere  
[Primjeri AI Toolkita](https://github.com/Azure-Samples/AI_Toolkit_Samples) osmišljeni su kako bi pomogli programerima i istraživačima da učinkovito istraže i implementiraju AI rješenja.  

Naši primjeri uključuju:  

Primjerni kod: Unaprijed pripremljeni primjeri za demonstraciju AI funkcionalnosti, poput treniranja, implementacije ili integracije modela u aplikacije.  
Dokumentacija: Vodiči i tutorijali koji pomažu korisnicima da razumiju značajke AI Toolkita i kako ih koristiti.  
Preduvjeti  

- Visual Studio Code  
- AI Toolkit za Visual Studio Code  
- GitHub token za osobni pristup (PAT)  
- Foundry Local  

## Najbolje prakse za razvoj Edge AI-a  

### Odabir modela  
- **Ograničenja veličine**: Odaberite modele koji odgovaraju memorijskim ograničenjima ciljanih uređaja  
- **Brzina inferencije**: Prioritet dajte modelima s brzim vremenom inferencije za aplikacije u stvarnom vremenu  
- **Kompromisi u točnosti**: Uravnotežite točnost modela s ograničenjima resursa  
- **Kompatibilnost formata**: Preferirajte ONNX ili formate optimizirane za hardver za rubnu implementaciju  

### Tehnike optimizacije  
- **Kvantizacija**: Koristite INT8 ili INT4 kvantizaciju za smanjenje veličine modela i poboljšanje brzine  
- **Pruning**: Uklonite nepotrebne parametre modela kako biste smanjili zahtjeve za računalnim resursima  
- **Destilacija znanja**: Kreirajte manje modele koji zadržavaju performanse većih  
- **Hardverska akceleracija**: Iskoristite NPU, GPU ili specijalizirane akceleratore kad su dostupni  

### Radni tijek razvoja  
- **Iterativno testiranje**: Često testirajte u uvjetima sličnim rubnim tijekom razvoja  
- **Praćenje performansi**: Kontinuirano pratite korištenje resursa i brzinu inferencije  
- **Kontrola verzija**: Pratite verzije modela i postavke optimizacije  
- **Dokumentacija**: Dokumentirajte sve odluke o optimizaciji i kompromisima u performansama  

### Razmatranja za implementaciju  
- **Praćenje resursa**: Pratite memoriju, CPU i potrošnju energije u produkciji  
- **Strategije za neuspjeh**: Implementirajte mehanizme za povratne opcije u slučaju neuspjeha modela  
- **Mehanizmi ažuriranja**: Planirajte ažuriranja modela i upravljanje verzijama  
- **Sigurnost**: Implementirajte odgovarajuće sigurnosne mjere za aplikacije Edge AI-a  

## Integracija s Edge AI okvirima  

### ONNX Runtime  
- **Implementacija na više platformi**: Implementirajte ONNX modele na različitim rubnim platformama  
- **Optimizacija hardvera**: Iskoristite hardverske specifične optimizacije ONNX Runtime-a  
- **Podrška za mobilne uređaje**: Koristite ONNX Runtime Mobile za aplikacije na pametnim telefonima i tabletima  
- **Integracija s IoT-om**: Implementirajte na IoT uređajima koristeći lagane distribucije ONNX Runtime-a  

### Windows ML  
- **Windows uređaji**: Optimizirajte za rubne uređaje i računala temeljena na Windowsu  
- **Akceleracija NPU-a**: Iskoristite Neural Processing Units na Windows uređajima  
- **DirectML**: Koristite DirectML za GPU akceleraciju na Windows platformama  
- **Integracija s UWP-om**: Integrirajte s aplikacijama Universal Windows Platform  

### TensorFlow Lite  
- **Optimizacija za mobilne uređaje**: Implementirajte TensorFlow Lite modele na mobilnim i ugrađenim uređajima  
- **Delegati za hardver**: Koristite specijalizirane delegacije hardvera za akceleraciju  
- **Mikrokontroleri**: Implementirajte na mikrokontrolerima koristeći TensorFlow Lite Micro  
- **Podrška za više platformi**: Implementirajte na Androidu, iOS-u i ugrađenim Linux sustavima  

### Azure IoT Edge  
- **Hibrid oblak-rub**: Kombinirajte treniranje u oblaku s inferencijom na rubu  
- **Implementacija modula**: Implementirajte AI modele kao IoT Edge module  
- **Upravljanje uređajima**: Upravljajte rubnim uređajima i ažuriranjima modela na daljinu  
- **Telemetrija**: Prikupljajte podatke o performansama i metrike modela iz rubnih implementacija  

## Napredni scenariji za Edge AI  

### Implementacija više modela  
- **Modelni ansambli**: Implementirajte više modela za poboljšanu točnost ili redundanciju  
- **A/B testiranje**: Istovremeno testirajte različite modele na rubnim uređajima  
- **Dinamički odabir**: Odaberite modele na temelju trenutnih uvjeta uređaja  
- **Dijeljenje resursa**: Optimizirajte korištenje resursa među više implementiranih modela  

### Federativno učenje  
- **Distribuirano treniranje**: Trenirajte modele na više rubnih uređaja  
- **Očuvanje privatnosti**: Zadržite podatke za treniranje lokalno dok dijelite poboljšanja modela  
- **Suradničko učenje**: Omogućite uređajima da uče iz kolektivnih iskustava  
- **Koordinacija rub-oblak**: Koordinirajte učenje između rubnih uređaja i infrastrukture u oblaku  

### Obrada u stvarnom vremenu  
- **Obrada tokova**: Obradite kontinuirane tokove podataka na rubnim uređajima  
- **Inferencija s niskom latencijom**: Optimizirajte za minimalnu latenciju inferencije  
- **Obrada u serijama**: Učinkovito obradite serije podataka na rubnim uređajima  
- **Adaptivna obrada**: Prilagodite obradu na temelju trenutnih mogućnosti uređaja  

## Rješavanje problema u razvoju Edge AI-a  

### Uobičajeni problemi  
- **Ograničenja memorije**: Model je prevelik za memoriju ciljanog uređaja  
- **Brzina inferencije**: Inferencija modela je prespora za zahtjeve u stvarnom vremenu  
- **Degradacija točnosti**: Optimizacija neprihvatljivo smanjuje točnost modela  
- **Kompatibilnost hardvera**: Model nije kompatibilan s ciljanom hardverskom opremom  

### Strategije za otklanjanje grešaka  
- **Profiliranje performansi**: Koristite značajke praćenja AI Toolkita za identifikaciju uskih grla  
- **Praćenje resursa**: Pratite memoriju i korištenje CPU-a tijekom razvoja  
- **Inkrementalno testiranje**: Testirajte optimizacije postupno kako biste izolirali probleme  
- **Simulacija hardvera**: Koristite alate za razvoj kako biste simulirali ciljani hardver  

### Rješenja za optimizaciju  
- **Daljnja kvantizacija**: Primijenite agresivnije tehnike kvantizacije  
- **Arhitektura modela**: Razmotrite različite arhitekture modela optimizirane za rub  
- **Optimizacija predobrade**: Optimizirajte predobradu podataka za rubna ograničenja  
- **Optimizacija inferencije**: Koristite optimizacije inferencije specifične za hardver  

## Resursi i sljedeći koraci  

### Službena dokumentacija  
- [Dokumentacija za AI Toolkit za programere](https://aka.ms/AIToolkit/doc)  
- [Vodič za instalaciju i postavljanje](https://code.visualstudio.com/docs/intelligentapps/overview#_install-and-setup)  
- [Dokumentacija za VS Code Intelligent Apps](https://code.visualstudio.com/docs/intelligentapps)  
- [Dokumentacija za Model Context Protocol (MCP)](https://modelcontextprotocol.io/)  

### Zajednica i podrška  
- [GitHub repozitorij za AI Toolkit](https://github.com/microsoft/vscode-ai-toolkit)  
- [GitHub problemi i zahtjevi za značajke](https://aka.ms/AIToolkit/feedback)  
- [Discord zajednica za Azure AI Foundry](https://aka.ms/azureaifoundry/discord)  
- [Tržnica ekstenzija za VS Code](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)  

### Tehnički resursi  
- [Dokumentacija za ONNX Runtime](https://onnxruntime.ai/)  
- [Dokumentacija za Ollama](https://ollama.ai/)  
- [Dokumentacija za Windows ML](https://docs.microsoft.com/en-us/windows/ai/)  
- [Dokumentacija za Azure AI Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/)  

### Putovi učenja  
- [Tečaj o osnovama Edge AI-a](../Module01/README.md)  
- [Vodič za male jezične modele](../Module02/README.md)  
- [Strategije za implementaciju na rubu](../Module03/README.md)  
- [Razvoj Edge AI-a za Windows](./windowdeveloper.md)  

### Dodatni resursi  
- **Statistika repozitorija**: Više od 1.8k zvjezdica, 150+ forkova, 18+ suradnika  
- **Licenca**: MIT licenca  
- **Sigurnost**: Primjenjuju se Microsoftove sigurnosne politike  
- **Telemetrija**: Poštuje postavke telemetrije VS Code-a  

## Zaključak  

AI Toolkit za Visual Studio Code predstavlja sveobuhvatnu platformu za moderni razvoj AI-a, pružajući pojednostavljene mogućnosti razvoja agenata koje su posebno vrijedne za aplikacije Edge AI-a. Sa svojim opsežnim katalogom modela koji podržava pružatelje poput Anthropica, OpenAI-a, GitHuba i Googlea, u kombinaciji s lokalnim izvršenjem putem ONNX-a i Ollame, alat pruža fleksibilnost potrebnu za raznolike scenarije implementacije na rubu.  

Snaga alata leži u njegovom integriranom pristupu—od otkrivanja i eksperimentiranja s modelima u Playgroundu do sofisticiranog razvoja agenata s Prompt Builderom, sveobuhvatnih mogućnosti evaluacije i besprijekorne integracije MCP alata. Za Edge AI programere, to znači brzo prototipiranje i testiranje AI agenata prije implementacije na rub, uz mogućnost brzog iteriranja i optimizacije za okruženja s ograničenim resursima.  

Ključne prednosti za razvoj Edge AI-a uključuju:  
- **Brzo eksperimentiranje**: Brzo testiranje modela i agenata prije implementacije na rub  
- **Fleksibilnost više pružatelja**: Pristup modelima iz različitih izvora za pronalaženje optimalnih rješenja za rub  
- **Lokalni razvoj**: Testiranje s ONNX-om i Ollamom za razvoj offline i uz očuvanje privatnosti  
- **Spremnost za produkciju**: Generiranje koda spremnog za produkciju i integracija s vanjskim alatima putem MCP-a  
- **Sveobuhvatna evaluacija**: Korištenje ugrađenih i prilagođenih metrika za validaciju performansi Edge AI-a  

Kako AI nastavlja napredovati prema scenarijima implementacije na rubu, AI Toolkit za VS Code pruža razvojno okruženje i radni tijek potrebne za izradu, testiranje i optimizaciju inteligentnih aplikacija za okruženja s ograničenim resursima. Bez obzira razvijate li IoT rješenja, mobilne AI aplikacije ili ugrađene inteligentne sustave, sveobuhvatni skup značajki alata i integrirani radni tijek podržavaju cijeli životni ciklus razvoja Edge AI-a.  

Uz kontinuirani razvoj i aktivnu zajednicu (više od 1.8k zvjezdica na GitHubu), AI Toolkit ostaje na čelu alata za razvoj AI-a, neprestano se razvijajući kako bi zadovoljio potrebe modernih AI programera koji razvijaju za scenarije implementacije na rubu.  

[Sljedeći Foundry Local](./foundrylocal.md)

---

**Izjava o odricanju odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane čovjeka. Ne preuzimamo odgovornost za nesporazume ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.
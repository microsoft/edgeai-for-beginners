# AI-tööriistakomplekt Visual Studio Code’ile – Edge AI arendusjuhend

## Sissejuhatus

Tere tulemast põhjalikku juhendisse AI-tööriistakomplekti kasutamiseks Visual Studio Code’is Edge AI arendamiseks. Kuna tehisintellekt liigub tsentraliseeritud pilvandmetöötlusest hajutatud ääreseadmeteni, vajavad arendajad võimsaid, integreeritud tööriistu, mis suudavad toime tulla ääredelevõtmise ainulaadsete väljakutsetega – alates ressursside piirangutest kuni võrguvabaduse nõueteni.

AI-tööriistakomplekt Visual Studio Code’ile täidab selle lünga, pakkudes täielikku arenduskeskkonda, mis on spetsiaalselt loodud AI-rakenduste ehitamiseks, testimiseks ja optimeerimiseks, mis töötavad tõhusalt ääreseadmetel. Olenemata sellest, kas arendate IoT-andurite, mobiilseadmete, sisse ehitatud süsteemide või ääreserverite jaoks, lihtsustab see tööriistakomplekt kogu teie arendusvoogu tuttavas VS Code keskkonnas.

See juhend viib teid läbi põhikontseptsioonide, tööriistade ja parimate tavade, kuidas AI-tööriistakomplekti kasutada oma Edge AI projektides, alates mudeli valimisest kuni tootmisse viimiseni.

## Ülevaade

AI-tööriistakomplekt Visual Studio Code’ile on võimas laiendus, mis lihtsustab agentide arendamist ja AI-rakenduste loomist. See tööriistakomplekt pakub ulatuslikke võimalusi AI mudelite uurimiseks, hindamiseks ja juurutamiseks mitmelt pakkujalt – sh Anthropic, OpenAI, GitHub, Google – võimaldades samal ajal kohaliku mudelieksekutsiooni ONNX ja Ollama abil.

Mis eristab AI-tööriistakomplekti, on selle terviklik lähenemine kogu AI arenduse elutsüklile. Erinevalt traditsioonilistest AI arendustööriistadest, mis keskenduvad ühelegi aspektile, pakub AI-tööriistakomplekt integreeritud keskkonda, mis hõlmab mudelite avastamist, eksperimenteerimist, agentide arendamist, hindamist ja juurutamist – kõik tuttavas VS Code keskkonnas.

Platvorm on loodud kiirprototüüpimiseks ja tootmisjuurutuseks, sisaldades funktsioone nagu kiirkirjutiste genereerimine, kiire algus, sujuvad MCP (Model Context Protocol) tööriista integratsioonid ja laialdased hindamisvõimalused. Edge AI arenduse puhul tähendab see, et saate tõhusalt arendada, testida ja optimeerida AI-rakendusi ääres olevate juurutusstsenaariumite jaoks, hoides samal ajal kogu arendusvoogu VS Code’is.

## Õpieesmärgid

Selle juhendi lõpus oskate:

### Põhioskused
- **Paigaldada ja konfigureerida** AI-tööriistakomplekt Visual Studio Code’i Edge AI arendusvoogude jaoks
- **Navigeerida ja kasutada** AI-tööriistakomplekti liidest, sealhulgas Mudelide kataloogi, Mänguväljakut ja Agentide ehitajat
- **Valida ja hinnata** AI-mudeleid, mis sobivad ääres kasutamiseks, arvestades jõudlust ja ressursse
- **Konverteerida ja optimeerida** mudeleid ONNX formaadis ja kvantiseerimistehnikatega ääreseadmete jaoks

### Edge AI arendusoskused
- **Disainida ja rakendada** Edge AI rakendusi integreeritud arenduskeskkonnas
- **Teha mudeliteste** ääresarnastes tingimustes, kasutades kohaliku inferentsi ja ressursi jälgimist
- **Luua ja kohandada** AI-agente, mis on optimeeritud ääreluurestsenaariumide jaoks
- **Hinnata mudelite jõudlust** ääres kasutatavate mõõdikute järgi (latentsus, mälukasutus, täpsus)

### Optimeerimine ja juurutus
- **Rakendada kvantiseerimise ja kärpimise** tehnikaid mudeli suuruse vähendamiseks, säilitades samas aktsepteeritava jõudluse
- **Optimeerida mudeleid** spetsiifilistele ääre riistvaraplatvormidele, sealhulgas CPU, GPU ja NPU kiirendusele
- **Rakendada parimaid tavasid** ääre AI arenduses, sisaldades ressursside haldamist ja varuplaanide strateegiaid
- **Valmistada mudeleid ja rakendusi ette** tootmisjuurutuseks ääreseadmetele

### Täiustatud Edge AI kontseptsioonid
- **Integreerida ääre AI raamistikud** sh ONNX Runtime, Windows ML ja TensorFlow Lite
- **Rakendada mitme mudeli arhitektuure** ja föderatiivõppe stsenaariumeid ääre keskkondades
- **Lahendada sagedasi ääre AI probleeme** nagu mälupiirangud, inferentsikiirus ja riistvaraline ühilduvus
- **Disainida jälgimis- ja logimisstrateegiaid** ääre AI rakendustele tootmises

### Praktiline rakendamine
- **Ehita otse-otsast ääre AI lahendusi** mudeli valimisest kuni juurutuseni
- **Näita pädevust** ääre-spetsiifilistes arendusvoogudes ja optimeerimistehnikates
- **Rakenda õpitud kontseptsioone** reaalse maailma ääre AI kasutusjuhtudel, sealhulgas IoT, mobiilne ja sisse ehitatud rakendused
- **Hinnata ja võrrelda** erinevaid ääre AI juurutusstrateegiaid ja nende kompromisse

## Peamised funktsioonid Edge AI arenduseks

### 1. Mudelite kataloog ja avastamine
- **Mitme pakkuja tugi**: Sirvi ja kasuta AI-mudeleid Anthropicu, OpenAI, GitHubi, Google’i ja teiste pakkujate hulgast
- **Kohalik mudelite integratsioon**: Lihtsustatud ONNX ja Ollama mudelite avastamine ääres kasutamiseks
- **GitHubi mudelid**: Otseühendus GitHubi mudelihostingu teenusega sujuvamaks ligipääsuks
- **Mudelite võrdlus**: Võrdle mudeleid kõrvuti, et leida optimaalne tasakaal ääreseadme piirangute vahel

### 2. Interaktiivne mänguväljak
- **Interaktiivne testimiskeskkond**: Kiire mudelivõimaluste katsetamine kontrollitud keskkonnas
- **Mitmemodaalne tugi**: Testi pilte, teksti ja muid sisendeid, mis on tüüpilised ääre stsenaariumites
- **Reaalajas eksperimenteerimine**: Kohene tagasiside mudeli vastuste ja jõudluse kohta
- **Parameetrite optimeerimine**: Häälesta mudeli parameetreid ääre juurutuse nõuetele vastavaks

### 3. Käskluste (agentide) ehitaja
- **Loomuliku keele genereerimine**: Genereeri stardikäsklused loomuliku keele kirjelduste põhjal
- **Iteratiivne täiustamine**: Paranda käsklusi mudeli vastuste ja jõudluse põhjal
- **Tööülesannete jaotus**: Jaga keerulised ülesanded käskluse ahelduse ja struktureeritud väljundite abil
- **Muutujate tugi**: Kasuta käsklustes muutujaid dünaamilise agendi käitumise jaoks
- **Tootmiskoodi genereerimine**: Genereeri tootmiseks valmis kood kiireks rakenduse arenduseks

### 4. Suur hulk korraga jooksmist ja hindamist
- **Mitme mudeli testimine**: Käivita samaaegselt mitu käsklust valitud mudelitel
- **Tõhus testimine suurel hulgal**: Testi erinevaid sisendeid ja konfiguratsioone efektiivselt
- **Kohandatud testjuhtumid**: Käivita agente testjuhtumitega funktsionaalsuse valideerimiseks
- **Jõudluse võrdlus**: Võrdle tulemusi erinevate mudelite ja konfiguratsioonide lõikes

### 5. Mudelite hindamine andmestike abil
- **Standardsed mõõdikud**: Testi AI mudeleid sisseehitatud hindajatega (F1 skoor, asjakohasus, sarnasus, sidusus)
- **Kohandatud hindajad**: Loo oma hindamismõõdikuid spetsiifiliste kasutusjuhtude jaoks
- **Andmestike integratsioon**: Testi mudeleid ulatuslike andmestike vastu
- **Jõudluse mõõtmine**: Kvanteeri mudelite jõudlust ääre juurutusotsuste tegemiseks

### 6. Peenhäälestamise võimed
- **Mudeli kohandamine**: Kohanda mudeleid spetsiifiliste kasutusjuhtude ja domeenide jaoks
- **Spetsialiseeritud adapteerimine**: Kohanda mudeleid eriliste domeenide ja nõudmiste jaoks
- **Ääre optimeerimine**: Peenhäälesta mudeleid spetsiifiliste ääre juurutuspiirangute jaoks
- **Domeenispetsiifiline koolitus**: Loo mudeleid, mis on kohandatud konkreetsetele ääre kasutusjuhtudele

### 7. MCP tööriista integratsioon
- **Välistööriistade ühenduvus**: Ühenda agente väliste tööriistadega mudelikonteksti protokolliserverite kaudu
- **Reaalmaailma tegevused**: Luba agentidel esitada päringuid andmebaasidele, kasutada API-sid või käivitada kohandatud loogikat
- **Olemasolevad MCP serverid**: Kasuta tööriistu käskluste (stdio) või HTTP (server-sent event) protokollide kaudu
- **Kohandatud MCP arendus**: Ehitada ja toe uusi MCP servereid koos testimisega Agentide ehitajas

### 8. Agentide arendus ja testimine
- **Funktsioonikõnede tugi**: Luba agentidel dünaamiliselt väliseid funktsioone kutsuda
- **Reaalajas integreerimise testimine**: Testi integratsioone reaalajas käivituste ja tööriistakasutuse kaudu
- **Agentide versioonihaldus**: Versioonihaldus agentidele koos võrdlusvõimalustega hindamistulemusteks
- **Silumine ja jälgimine**: Kohalik jälgimine ja silumise võimalused agentide arendamiseks

## Edge AI arendusvoog

### Faas 1: Mudelite avastamine ja valik
1. **Sirvi mudelite kataloogi**: Kasuta mudelikataloogi sobivate ääres kasutamiseks mõeldud mudelite leidmiseks
2. **Võrdle jõudlust**: Hinda mudeleid suuruse, täpsuse ja inferentsikiiruse alusel
3. **Testi lokaalsetes tingimustes**: Kasuta Ollama või ONNX mudeleid lokaalselt testimiseks enne ääres kasutamist
4. **Hinda ressursside nõudeid**: Määra sihtääreseadmete mälu- ja arvutusvajadused

### Faas 2: Mudelite optimeerimine
1. **Konverteeri ONNX formaati**: Konverteeri valitud mudelid ONNX formaati ääre ühilduvuseks
2. **Rakenda kvantiseerimine**: Vähenda mudeli suurust INT8 või INT4 kvantiseerimisega
3. **Riistvara optimeerimine**: Optimeeri sihtääre riistvarale (ARM, x86, spetsialiseeritud kiirendid)
4. **Jõudluse valideerimine**: Kontrolli, et optimeeritud mudel säilitab aktsepteeritava täpsuse

### Faas 3: Rakenduse arendus
1. **Agendi disain**: Kasuta Agentide ehitajat ääreoptimeeritud AI agentide loomisel
2. **Käskluste konstrueerimine**: Arenda välja käsklused, mis toimivad efektiivselt väiksemate ääremudelitega
3. **Integreerimise testimine**: Testi agente simuleeritud ääre tingimustes
4. **Koodi genereerimine**: Genereeri tootmiskõlbulik kood, mis on optimeeritud äärde juurutamiseks

### Faas 4: Hindamine ja testimine
1. **Massihindamine**: Testi mitut konfiguratsiooni, et leida optimaalne ääreseaded
2. **Jõudluse profiilimine**: Analüüsi inferentsikiirust, mälukasutust ja täpsust
3. **Ääre simulatsioon**: Testi tingimustes, mis sarnanevad sihtääre juurutuskeskkonnale
4. **Koormustestimine**: Hinda jõudlust erinevate koormustingimuste all

### Faas 5: Juurutusvalmidus
1. **Lõplik optimeerimine**: Rakenda lõplikud optimeerimised testitulemuste põhjal
2. **Juurutuspakendamine**: Paki mudelid ja kood ääre juurutuseks
3. **Dokumentatsioon**: Dokumenteeri juurutuse nõuded ja konfiguratsioon
4. **Järelvalve seadistamine**: Valmista ette jälgimine ja logimine ääre juurutuseks

## Sihtgrupp Edge AI arendamiseks

### Edge AI arendajad
- Rakenduste arendajad, kes loovad AI-toega ääreseadmeid ja IoT lahendusi
- Sisse ehitatud süsteemide arendajad, kes integreerivad AI võimalusi ressursside piiratud seadmetesse
- Mobiiliarendajad, kes loovad seadmesisesi AI rakendusi nutitelefonidele ja tahvelarvutitele

### Edge AI insenerid
- AI insenerid, kes optimeerivad mudeleid ääre juurutuseks ja haldavad inferentsitorusid
- DevOps insenerid, kes juurutavad ja haldavad AI mudeleid hajutatud ääre infrastruktuuris
- Jõudlusinsenerid, kes optimeerivad AI töökoormusi ääre riistvaraliste piirangute jaoks

### Teadlased ja haridustöötajad
- AI teadlased, kes arendavad tõhusaid mudeleid ja algoritme ääre arvutuseks
- Õpetajad, kes õpetavad Edge AI kontseptsioone ja demonstreerivad optimeerimisvõtteid
- Õpilased, kes õpivad ääre AI juurutamise väljakutseid ja lahendusi

## Edge AI kasutusstsenaariumid

### Nutikad IoT seadmed
- **Reaalaegne pildituvastus**: Juuruta arvutinägemise mudeleid IoT kaameratesse ja anduritesse
- **Häälitöötlus**: Rakenda kõnetuvastust ja loomuliku keele töötlemist nutikates kõlarites
- **Ennetav hooldus**: Käivita anomaaliate tuvastamise mudeleid tööstuslikes ääreseadmetes
- **Keskkonnajälgimine**: Juuruta andurite andmete analüüsiks mudeleid keskkonnaalaste rakenduste jaoks

### Mobiil- ja sisse ehitatud rakendused
- **Seadmesisest tõlget**: Rakenda keele tõlkemudeleid, mis töötavad võrguühenduseta
- **Liitreaalsus**: Juuruta objekti tuvastust ja jälgimist AR rakendustele reaalaajas
- **Tervise jälgimine**: Käivita terviseanalüüsi mudeleid kantavatel seadmetel ja meditsiiniseadmetel
- **Autonoomsed süsteemid**: Rakenda otsustusmudeleid droonidele, robotitele ja sõidukitele

### Ääre arvutamise infrastruktuur
- **Ääre andmekeskused**: Juuruta AI mudeleid ääre andmekeskustesse madala latentsusega rakenduste jaoks
- **CDN integratsioon**: Integreeri AI töötlusvõimeid sisujagamisvõrkudesse
- **5G Edge**: Kasuta 5G äre arvutust AI-toega rakendusteks
- **Uduarvutus**: Rakenda AI töötlust uduarvutuse keskkondades

## Paigaldus ja seadistamine

### Laienduse paigaldamine
Paigalda AI-tööriistakomplekti laiendus otse Visual Studio Code Marketplace’ist:

**Laienduse ID**: `ms-windows-ai-studio.windows-ai-studio`

**Paigaldusmeetodid**:
1. **VS Code Marketplace**: Otsi laienduste vaates "AI Toolkit"
2. **Käsurealt**: `code --install-extension ms-windows-ai-studio.windows-ai-studio`
3. **Otsepaigaldus**: Laadi alla aadressilt [VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)

### Eeltingimused Edge AI arenduseks
- **Visual Studio Code**: Soovitatav on uusim versioon
- **Python keskkond**: Python 3.8+ koos vajalike AI teekidega
- **ONNX Runtime** (vabatahtlik): ONNX mudelite inferentsiks
- **Ollama** (vabatahtlik): Kohaliku mudelite teenindamiseks
- **Riistvara kiirendustööriistad**: CUDA, OpenVINO või platvormipõhised kiirendid

### Esialgne seadistus
1. **Laienduse aktiveerimine**: Ava VS Code ja veendu, et AI-tööriistakomplekt kuvatakse tegevuse ribal
2. **Mudeli pakkuja seadistus**: Sea sisse ligipääs GitHubi, OpenAI, Anthropicu või teiste mudeli pakkujatele
3. **Kohalik keskkond**: Sea sisse Python keskkond ja paigalda vajalikud paketid
4. **Riistvara kiirendus**: Kui võimalik, konfigureeri GPU/NPU kiirendus
5. **MCP integratsioon**: Sea vajadusel sisse Model Context Protocol teenused

### Esmakordse seadistuse kontrollnimekiri
- [ ] AI-tööriistakomplekti laiendus installitud ja aktiveeritud
- [ ] Mudelite kataloogi ligipääsetavus ja mudelite leitavus
- [ ] Mänguväljak töötab mudelite testimiseks
- [ ] Agentide ehitaja ligipääsetav käskluste arendamiseks
- [ ] Kohalik arenduskeskkond seadistatud
- [ ] Riistvara kiirendus (kui saadaval) õigesti konfigureeritud

## AI-tööriistakomplektiga alustamine

### Kiirkäivitusjuhend

Soovitame alustada GitHubi majutatud mudelitega, mis pakuvad kõige sujuvamat kogemust:

1. **Paigaldus**: Järgi [paigaldusjuhendit](https://code.visualstudio.com/docs/intelligentapps/overview#_install-and-setup), et seadistada AI-tööriistakomplekt oma seadmele
2. **Mudeli avastamine**: Laienduse puuvaates vali **CATALOG > Models**, et sirvida saadaval olevaid mudeleid
3. **GitHubi mudelid**: Alusta GitHubi majutatud mudelitega optimaalseks integratsiooniks
4. **Mänguväljaku testimine**: Igas mudeli kaardil vali **Try in Playground**, et hakata mudeli võimalustega katsetama

### Samm-sammult Edge AI arendus

#### Samm 1: Mudelite uurimine ja valik
1. Ava VS Code’i tegevusribal AI-tööriistakomplekti vaade
2. Sirvi mudelite kataloogi, et leida sobivaid mudeleid ääres kasutamiseks
3. Filtreeri vastavalt pakkujale (GitHub, ONNX, Ollama) oma edge nõuetele
4. Kasuta **Try in Playground**, et kohe mudeli võimalusi testida

#### Samm 2: Agentide arendus
1. Kasuta **Käskluste (Agent) ehitajat** ääre-optimiseeritud AI agentide loomiseks
2. Genereeri stardikäsklused loomuliku keele kirjelduste põhjal
3. Itereeri ja täiusta käsklusi mudeli vastuste põhjal
4. Integreeri MCP tööriistu agentide võimete tõstmiseks


#### 3. samm: testimine ja hindamine
1. Kasutage **Bulk Run**-i, et testida mitut prompti valitud mudelites
2. Käivitage agendid testjuhtudega, et valideerida funktsionaalsust
3. Hinnake täpsust ja jõudlust sisseehitatud või kohandatud mõõdikute abil
4. Võrrelge erinevaid mudeleid ja konfiguratsioone

#### 4. samm: peenhäälestus ja optimeerimine
1. Kohandage mudeleid konkreetseteks servakasutuse juhtudeks
2. Rakendage domeenispetsiifilist peenhäälestust
3. Optimeerige servapaigutuse piirangute jaoks
4. Versioonige ja võrrelge erinevaid agendi konfiguratsioone

#### 5. samm: juurutuseks ettevalmistamine
1. Genereerige tootmisvalmis kood, kasutades Agent Builderit
2. Seadistage MCP serveri ühendused tootmiseks
3. Valmistage ette juurutuspakkide komplektid servaseadmetele
4. Konfigureerige jälgimise ja hindamise mõõdikud

## Näited AI tööriistakomplektist 

Proovige meie näiteid
[AI tööriistakomplekti näited](https://github.com/Azure-Samples/AI_Toolkit_Samples) on loodud selleks, et aidata arendajatel ja teadlastel tõhusalt uurida ja rakendada tehisintellekti lahendusi.

Meie näidetes on:

Näidiskood: eelnevalt ehitatud näited AI funktsioonide demonstreerimiseks, nagu mudelite treenimine, juurutamine või integreerimine rakendustesse.
Dokumentatsioon: juhendid ja õppetunnid, mis aitavad kasutajatel mõista AI tööriistakomplekti funktsioone ja nende kasutamist.
Eeltingimused

- Visual Studio Code
- AI tööriistakogu Visual Studio Code'i jaoks
- GitHubi peenhäälestatud isiklik juurdepääsutoken (PAT)
- Foundry Local

## Parimad tavad serva AI arendamisel

### Mudeli valik
- **Suuruse piirangud**: valige mudeleid, mis mahuvad sihtseadmete mälupiirangutesse
- **Järeldamise kiirus**: eelistage kiire järeldamisajaga mudeleid reaalajas rakenduste jaoks
- **Täpsuse kompromissid**: tasakaalustage mudeli täpsus ressursipiirangutega
- **Vormingu ühilduvus**: eelistage ONNX- või riistvarale optimeeritud vorminguid serva juurutamisel

### Optimeerimistehnikad
- **Kvantimine**: kasutage INT8 või INT4 kvantimist, et vähendada mudeli suurust ja parandada kiirust
- **Puhastamine**: eemaldage mudelist mittevajalikud parameetrid, et vähendada arvutuskoormust
- **Teadmusdistillatsioon**: looge väiksemaid mudeleid, mis säilitavad suuremate omade jõudluse
- **Riistvara kiirendus**: kasutage NPUs, GPU-sid või spetsiaalseid kiirendajaid, kui need on olemas

### Arendusprotsess
- **Iteratiivne testimine**: testige sageli servaga sarnastes tingimustes arenduse jooksul
- **Jõudluse jälgimine**: jälgige pidevalt ressursside kasutust ja järeldamise kiirust
- **Versioonihaldus**: jälgige mudelite versioone ja optimeerimise sätteid
- **Dokumentatsioon**: dokumenteerige kõik optimeerimisotsused ja jõudluse kompromissid

### Juurutamise kaalutlused
- **Ressursside jälgimine**: jälgige tootmises mälu, CPU ja energiatarbimist
- **Tagasilangemehhanismid**: rakendage mudeli rikete jaoks varumehhanisme
- **Uuendamise mehhanismid**: planeerige mudelite uuendusi ja versioonihaldust
- **Turvalisus**: rakendage sobivad turvameetmed serva AI rakenduste jaoks

## Integreerimine serva AI raamistikudega

### ONNX Runtime
- **Platvormideülene juurutamine**: juurutage ONNX mudeleid erinevatel servaplatvormidel
- **Riistvara optimeerimine**: kasutage ONNX Runtime riistvaraspetsiifilisi optimeerimisi
- **Mobiilne tugi**: kasutage ONNX Runtime Mobile'i nutitelefonide ja tahvelarvutite rakendusteks
- **IoT integratsioon**: juurutage IoT seadmetel, kasutades ONNX Runtime kerge versiooni

### Windows ML
- **Windowsi seadmed**: optimeerige Windowsi-põhistele servaseadmetele ja arvutitele
- **NPU kiirendus**: kasutage Windowsi seadmetel neuronprotsessori üksusi
- **DirectML**: kasutage DirectML-i GPU kiirenduseks Windowsi platvormidel
- **UWP integreerimine**: integreerige Universal Windows Platformi rakendustega

### TensorFlow Lite
- **Mobiili optimeerimine**: juurutage TensorFlow Lite mudeleid mobiili ja sisseehitatud seadmetes
- **Riistvaradelegaadid**: kasutage spetsiaalseid riistvaradelegaate kiirenduseks
- **Mikrokontrollerid**: juurutage mikrokontrollerites, kasutades TensorFlow Lite Micro-t
- **Platvormideülene tugi**: juurutage Androidis, iOS-is ja sisseehitatud Linuxisüsteemides

### Azure IoT Edge
- **Pilve- ja serva hübriid**: kombineerige pilvepõhine treening servajäreldustega
- **Moodulite juurutamine**: juurutage AI mudeleid IoT Edge moodulitena
- **Seadmete haldus**: hallake servaseadmeid ja mudelite uuendusi kaugjuhtimise teel
- **Telemeetria**: koguge jõudlusandmeid ja mudeli mõõdikuid servajuurutustest

## Arenenud serva AI stsenaariumid

### Mitme mudeli juurutamine
- **Mudelite ansamblid**: juurutage mitmeid mudeleid täpsuse või redundantsuse parandamiseks
- **A/B testimine**: testige erinevaid mudeleid samaaegselt servaseadmetel
- **Dünaamiline valik**: valige mudeleid vastavalt praegustele seadme tingimustele
- **Ressursside jagamine**: optimeerige ressursside kasutust mitme juurutatud mudeli vahel

### Föderaalõpe
- **Hajutatud treening**: treenige mudeleid mitmel servaseadmel
- **Privaatsuse säilitamine**: hoidke treeningandmed lokaalsena, jagades mudeli täiustusi
- **Koostööõpe**: võimaldage seadmetel õppida kollektiivsetest kogemustest
- **Serva- ja pilvekoostöö**: koordineerige õppimist serva seadmete ja pilve infrastruktuuri vahel

### Reaalajas töötlemine
- **Vooprotsessimine**: töötle servaseadmetel pidevaid andmevooge
- **Madal latentsus järeldamisel**: optimeerige miinimumlatentsuse saavutamiseks
- **Pakkide töötlemine**: töötle andmepakke efektiivselt servaseadmetel
- **Kohanemine töötlemisega**: reguleeri töötlemist vastavalt seadme võimetele

## Serva AI arenduse tõrkeotsing

### Levinumad probleemid
- **Mälupiirangud**: mudel on sihtseadme mälust liiga suur
- **Järeldamise kiirus**: mudeli järeldamine on reaalaja nõuetest aeglane
- **Täpsuse halvenemine**: optimeerimine vähendab mudeli täpsust aktsepteeritamatult
- **Riistvaraline ühilduvus**: mudel ei ühildu sihtseadme riistvaraga

### Silumise strateegiad
- **Jõudluse profiilimine**: kasutage AI tööriistakomplekti jälgimisfunktsioone kitsaskohtade avastamiseks
- **Ressursside jälgimine**: jälgige mälu ja CPU kasutust arenduse ajal
- **Järkjärguline testimine**: testige optimeeringuid järk-järgult, et isoleerida probleemid
- **Riistvarasimulatsioon**: kasutage arendustööriistu sihtseadme riistvara simuleerimiseks

### Optimeerimislahendused
- **Veelgi agressiivsem kvantimine**: rakendage põhjalikumaid kvantimistehnikaid
- **Mudeli arhitektuur**: kaaluge erinevaid servale optimeeritud mudeli arhitektuure
- **Eeltöötluse optimeerimine**: optimeerige andmete eeltöötlust servapiirangute jaoks
- **Järeldamise optimeerimine**: kasutage riistvaraspetsiifilisi järeldamise optimeerimisi

## Ressursid ja järgmised sammud

### Ametlik dokumentatsioon
- [AI tööriistakomplekti arendajate dokumentatsioon](https://aka.ms/AIToolkit/doc)
- [Installatsiooni ja seadistamise juhend](https://code.visualstudio.com/docs/intelligentapps/overview#_install-and-setup)
- [VS Code Intelligent Apps dokumentatsioon](https://code.visualstudio.com/docs/intelligentapps)
- [Mudelikonteksti protokolli (MCP) dokumentatsioon](https://modelcontextprotocol.io/)

### Kogukond ja tugi
- [AI tööriistakomplekti GitHub repositoorium](https://github.com/microsoft/vscode-ai-toolkit)
- [GitHub probleemide ja funktsioonisoovide jälgimine](https://aka.ms/AIToolkit/feedback)
- [Azure AI Foundry Discordi kogukond](https://aka.ms/azureaifoundry/discord)
- [VS Code laienduste turg](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)

### Tehnilised ressursid
- [ONNX Runtime dokumentatsioon](https://onnxruntime.ai/)
- [Ollama dokumentatsioon](https://ollama.ai/)
- [Windows ML dokumentatsioon](https://docs.microsoft.com/en-us/windows/ai/)
- [Azure AI Foundry dokumentatsioon](https://learn.microsoft.com/en-us/azure/ai-foundry/)

### Õpiväljad
- [Serva AI alused kursus](../Module01/README.md)
- [Väikeste keeltemudelite juhend](../Module02/README.md)
- [Servajuhtimise strateegiad](../Module03/README.md)
- [Windows serva AI arendus](./windowdeveloper.md)

### Täiendavad ressursid
- **Repositsiooni statistika**: 1800+ tähte, 150+ täringut, 18+ kaastöötajat
- **Litsents**: MIT litsents
- **Turvalisus**: kehtivad Microsofti turvapoliitikad
- **Telemeetria**: austab VS Code'i telemeetria seadeid

## Kokkuvõte

AI tööriistakogu Visual Studio Code'i jaoks on kaasaegse AI arenduse kõikehõlmav platvorm, mis pakub voolavat agendiarenduse võimalusi, mis on eriti väärtuslikud serva AI rakendustele. Oma ulatusliku mudelikataloogiga, mis toetab pakkujaid nagu Anthropic, OpenAI, GitHub ja Google, koos kohaliku täitmisega ONNX ja Ollama kaudu, pakub tööriistakogu mitmekülgsust, mida vajatakse mitmekesistes servajuurutusstsenaariumides.

Tööriistakogu tugevus seisneb selle integreeritud lähenemises—mudeli leidmisest ja katsetamisest Kohtumispaigas kuni keeruka agendiarenduseni Prompt Builderiga, põhjalike hindamisvõimalusteni ja sujuva MCP tööriistade integratsioonini. Serva AI arendajatele tähendab see kiiret prototüüpimist ja agentide testimist enne servajuurutust võimalusega kiiresti iteratsioonideks ja optimeerimiseks piiratud ressurssidega keskkondades.

Peamised eelised serva AI arendamisel hõlmavad:
- **Kiire katsetamine**: testige mudeleid ja agente kiiresti enne servajuurutust
- **Mitme pakkuja paindlikkus**: ligipääs mudelitele erinevatest allikatest parimate servalahenduste leidmiseks
- **Kohalik arendus**: testige ONNX ja Ollama abil võrguühenduseta ja privaatsust säilitavas keskkonnas
- **Tootmisvalmidus**: genereerige tootmisvalmis kood ja integreerige väliste tööriistadega MCP kaudu
- **Põhjalik hindamine**: kasutage sisseehitatud ja kohandatud mõõdikuid serva AI jõudluse valideerimiseks

Kuna AI liigutab end üha enam servajuurutusstsenaariumite suunas, pakub AI tööriistakogu VS Code'ile arenduskeskkonna ja töövoo nutikate rakenduste ehitamiseks, testimiseks ja optimeerimiseks piiratud ressurssidega keskkondades. Olgu tegemist IoT lahenduste, mobiili AI rakenduste või sisseehitatud intelligentsussüsteemidega, saab tööriistakogu ulatuslik funktsioonikomplekt ja integreeritud töövoog toetada kogu serva AI arenduse elutsüklit.

Jätkuva arenduse ja aktiivse kogukonnaga (1800+ GitHubi tähte) on AI tööriistakogu jätkuvalt AI arendustööriistade eesliinil, arenedes pidevalt, et rahuldada kaasaegsete AI arendajate vajadusi servajuurutusstsenaariumite jaoks.

[Järgmine Foundry Local](./foundrylocal.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
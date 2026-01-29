# AI Toolkit Visual Studio Code'i jaoks - Edge AI arendamise juhend

## Sissejuhatus

Tere tulemast põhjalikku juhendisse, kuidas kasutada AI Toolkit'i Visual Studio Code'is Edge AI arendamiseks. Kuna tehisintellekt liigub tsentraliseeritud pilvearvutustest hajutatud servaseadmetele, vajavad arendajad võimsaid ja integreeritud tööriistu, mis suudavad toime tulla serva juurutamise unikaalsete väljakutsetega - alates ressursipiirangutest kuni võrguühenduseta töö nõueteni.

AI Toolkit Visual Studio Code'i jaoks täidab selle tühimiku, pakkudes terviklikku arenduskeskkonda, mis on spetsiaalselt loodud tõhusalt servaseadmetel töötavate tehisintellekti rakenduste loomiseks, testimiseks ja optimeerimiseks. Olgu tegemist IoT sensorite, mobiilseadmete, manussüsteemide või servaserveritega, see tööriistakomplekt lihtsustab kogu arendusprotsessi tuttavas VS Code'i keskkonnas.

See juhend tutvustab olulisi kontseptsioone, tööriistu ja parimaid praktikaid, kuidas kasutada AI Toolkit'i oma Edge AI projektides, alates mudeli valikust kuni tootmisjuurutamiseni.

## Ülevaade

AI Toolkit Visual Studio Code'i jaoks on võimas laiendus, mis lihtsustab agentide arendamist ja tehisintellekti rakenduste loomist. Tööriistakomplekt pakub laiaulatuslikke võimalusi tehisintellekti mudelite uurimiseks, hindamiseks ja juurutamiseks mitmetelt pakkujatelt, sealhulgas Anthropic, OpenAI, GitHub, Google, ning toetab kohalikke mudelite täitmisi ONNX-i ja Ollama abil.

Mis eristab AI Toolkit'i teistest, on selle terviklik lähenemine kogu tehisintellekti arendustsüklile. Erinevalt traditsioonilistest tehisintellekti arendustööriistadest, mis keskenduvad üksikutele aspektidele, pakub AI Toolkit integreeritud keskkonda, mis hõlmab mudelite avastamist, katsetamist, agentide arendamist, hindamist ja juurutamist - kõik see toimub tuttavas VS Code'i keskkonnas.

Platvorm on spetsiaalselt loodud kiireks prototüüpimiseks ja tootmisjuurutamiseks, pakkudes selliseid funktsioone nagu promptide genereerimine, kiirstardid, sujuvad MCP (Model Context Protocol) tööriistade integreerimised ja ulatuslikud hindamisvõimalused. Edge AI arenduse jaoks tähendab see, et saate tõhusalt arendada, testida ja optimeerida tehisintellekti rakendusi serva juurutamise stsenaariumide jaoks, säilitades samal ajal kogu arendusprotsessi VS Code'i keskkonnas.

## Õpieesmärgid

Selle juhendi lõpuks suudate:

### Põhioskused
- **Installida ja seadistada** AI Toolkit Visual Studio Code'i jaoks Edge AI arenduse töövoogude jaoks
- **Navigeerida ja kasutada** AI Toolkit'i liidest, sealhulgas Model Catalog, Playground ja Agent Builder
- **Valida ja hinnata** tehisintellekti mudeleid, mis sobivad serva juurutamiseks, lähtudes jõudlusest ja ressursipiirangutest
- **Konverteerida ja optimeerida** mudeleid ONNX-i formaadi ja kvantiseerimistehnikate abil servaseadmete jaoks

### Edge AI arendamise oskused
- **Kavandada ja rakendada** Edge AI rakendusi integreeritud arenduskeskkonna abil
- **Teostada mudelite testimist** servasarnastes tingimustes, kasutades kohalikku järeldamist ja ressursimonitooringut
- **Luua ja kohandada** tehisintellekti agente, mis on optimeeritud serva juurutamise stsenaariumide jaoks
- **Hinnata mudelite jõudlust** serva arvutamise jaoks oluliste mõõdikute (latentsus, mälukasutus, täpsus) abil

### Optimeerimine ja juurutamine
- **Rakendada kvantiseerimise ja kärpimise tehnikaid**, et vähendada mudeli suurust, säilitades samal ajal vastuvõetava jõudluse
- **Optimeerida mudeleid** konkreetsete serva riistvaraplatvormide jaoks, sealhulgas CPU, GPU ja NPU kiirendus
- **Rakendada parimaid praktikaid** Edge AI arendamiseks, sealhulgas ressursihaldus ja varuplaanid
- **Valmistada mudeleid ja rakendusi** tootmisjuurutamiseks servaseadmetel

### Täiustatud Edge AI kontseptsioonid
- **Integreerida serva tehisintellekti raamistikud**, sealhulgas ONNX Runtime, Windows ML ja TensorFlow Lite
- **Rakendada mitme mudeli arhitektuure** ja föderatiivse õppimise stsenaariume servakeskkondades
- **Lahendada levinud serva tehisintellekti probleeme**, sealhulgas mälupiirangud, järeldamise kiirus ja riistvara ühilduvus
- **Kavandada monitooringu ja logimise strateegiaid** serva tehisintellekti rakenduste jaoks tootmises

### Praktiline rakendus
- **Luua terviklikke Edge AI lahendusi** alates mudeli valikust kuni juurutamiseni
- **Näidata oskusi** servaspetsiifilistes arendustöövoogudes ja optimeerimistehnikates
- **Rakendada õpitud kontseptsioone** reaalse maailma Edge AI kasutusjuhtumites, sealhulgas IoT, mobiil- ja manusrakendustes
- **Hinnata ja võrrelda** erinevaid serva tehisintellekti juurutamise strateegiaid ja nende kompromisse

## Olulised funktsioonid Edge AI arendamiseks

### 1. Mudelikataloog ja avastamine
- **Mitme pakkuja tugi**: Sirvige ja pääsege ligi tehisintellekti mudelitele Anthropic, OpenAI, GitHub, Google ja teistelt pakkujatelt
- **Kohalike mudelite integreerimine**: ONNX-i ja Ollama mudelite lihtsustatud avastamine serva juurutamiseks
- **GitHub mudelid**: Otsene integreerimine GitHub'i mudelite hostimisega lihtsustatud juurdepääsuks
- **Mudelite võrdlemine**: Võrrelge mudeleid kõrvuti, et leida optimaalne tasakaal servaseadmete piirangute jaoks

### 2. Interaktiivne Playground
- **Interaktiivne testimiskeskkond**: Kiire katsetamine mudeli võimekustega kontrollitud keskkonnas
- **Mitme modaalsuse tugi**: Testige pilte, teksti ja muid sisendeid, mis on tüüpilised serva stsenaariumides
- **Reaalajas katsetamine**: Kohene tagasiside mudeli vastuste ja jõudluse kohta
- **Parameetrite optimeerimine**: Häälestage mudeli parameetreid serva juurutamise nõuete jaoks

### 3. Prompt (Agent) Builder
- **Loodusliku keele genereerimine**: Looge alguspromptid looduslike keelekirjelduste abil
- **Iteratiivne täiustamine**: Parandage promptide kvaliteeti mudeli vastuste ja jõudluse põhjal
- **Ülesannete jaotamine**: Jagage keerulised ülesanded promptide ahelate ja struktureeritud väljundite abil
- **Muutujate tugi**: Kasutage muutujaid promptides dünaamilise agentide käitumise jaoks
- **Tootmiskoodi genereerimine**: Looge tootmiskõlblik kood kiireks rakenduste arendamiseks

### 4. Massiline käitamine ja hindamine
- **Mitme mudeli testimine**: Käivitage mitu prompti valitud mudelite vahel samaaegselt
- **Tõhus testimine suurel skaalal**: Testige erinevaid sisendeid ja konfiguratsioone tõhusalt
- **Kohandatud testjuhtumid**: Käivitage agente testjuhtumitega funktsionaalsuse valideerimiseks
- **Jõudluse võrdlemine**: Võrrelge tulemusi erinevate mudelite ja konfiguratsioonide vahel

### 5. Mudelite hindamine andmekogumitega
- **Standardmõõdikud**: Testige tehisintellekti mudeleid sisseehitatud hindajate abil (F1 skoor, asjakohasus, sarnasus, sidusus)
- **Kohandatud hindajad**: Looge oma hindamismõõdikud konkreetsete kasutusjuhtumite jaoks
- **Andmekogumite integreerimine**: Testige mudeleid ulatuslike andmekogumite vastu
- **Jõudluse mõõtmine**: Kvantifitseerige mudeli jõudlust serva juurutamise otsuste jaoks

### 6. Peenhäälestamise võimalused
- **Mudelite kohandamine**: Kohandage mudeleid konkreetsete kasutusjuhtumite ja valdkondade jaoks
- **Spetsialiseeritud kohandamine**: Kohandage mudeleid spetsialiseeritud valdkondade ja nõuete jaoks
- **Serva optimeerimine**: Häälestage mudeleid spetsiaalselt serva juurutamise piirangute jaoks
- **Valdkonnaspetsiifiline treenimine**: Looge mudeleid, mis on kohandatud konkreetsete serva kasutusjuhtumite jaoks

### 7. MCP tööriistade integreerimine
- **Väliste tööriistade ühenduvus**: Ühendage agendid väliste tööriistadega Model Context Protocol serverite kaudu
- **Reaalmaailma tegevused**: Võimaldage agentidel päringuid teha andmebaasidesse, pääseda API-dele või täita kohandatud loogikat
- **Olemasolevad MCP serverid**: Kasutage tööriistu käsurea (stdio) või HTTP (server-sent event) protokollide kaudu
- **Kohandatud MCP arendus**: Looge ja testige uusi MCP servereid Agent Builder'i abil

### 8. Agentide arendamine ja testimine
- **Funktsioonikutsumise tugi**: Võimaldage agentidel dünaamiliselt väliseid funktsioone kutsuda
- **Reaalajas integreerimise testimine**: Testige integreerimisi reaalajas käituste ja tööriistade kasutamisega
- **Agentide versioonihaldus**: Versioonihaldus agentidele koos võrdlusvõimalustega hindamistulemuste jaoks
- **Silumine ja jälgimine**: Kohalik jälgimine ja silumine agentide arendamiseks

## Edge AI arenduse töövoog

### Faas 1: Mudelite avastamine ja valik
1. **Uurige mudelikataloogi**: Kasutage mudelikataloogi, et leida mudeleid, mis sobivad serva juurutamiseks
2. **Võrrelge jõudlust**: Hinnake mudeleid suuruse, täpsuse ja järeldamise kiiruse põhjal
3. **Testige kohapeal**: Kasutage Ollama või ONNX-i mudeleid, et testida kohapeal enne serva juurutamist
4. **Hinnake ressursinõudeid**: Määrake mälukasutus ja arvutusvajadused sihtservaseadmete jaoks

### Faas 2: Mudelite optimeerimine
1. **Konverteerige ONNX-i**: Konverteerige valitud mudelid ONNX-i formaati serva ühilduvuse jaoks
2. **Rakendage kvantiseerimist**: Vähendage mudeli suurust INT8 või INT4 kvantiseerimise abil
3. **Riistvara optimeerimine**: Optimeerige sihtserva riistvara jaoks (ARM, x86, spetsialiseeritud kiirendid)
4. **Jõudluse valideerimine**: Kontrollige, et optimeeritud mudelid säilitaksid vastuvõetava täpsuse

### Faas 3: Rakenduste arendamine
1. **Agentide disain**: Kasutage Agent Builder'it, et luua serva optimeeritud tehisintellekti agente
2. **Promptide insenerimine**: Arendage promptid, mis töötavad tõhusalt väiksemate serva mudelitega
3. **Integreerimise testimine**: Testige agente simuleeritud servatingimustes
4. **Koodi genereerimine**: Genereerige tootmiskood, mis on optimeeritud serva juurutamiseks

### Faas 4: Hindamine ja testimine
1. **Massiline hindamine**: Testige mitmeid konfiguratsioone, et leida optimaalsed servaseaded
2. **Jõudluse profiilimine**: Analüüsige järeldamise kiirust, mälukasutust ja täpsust
3. **Serva simulatsioon**: Testige tingimustes, mis sarnanevad sihtserva juurutamise keskkonnaga
4. **Koormustestimine**: Hinnake jõudlust erinevate koormustingimuste korral

### Faas 5: Juurutamise ettevalmistamine
1. **Lõplik optimeerimine**: Rakendage lõplikud optimeerimised testitulemuste põhjal
2. **Juurutamise pakendamine**: Pakendage mudelid ja kood serva juurutamiseks
3. **Dokumentatsioon**: Dokumenteerige juurutamise nõuded ja konfiguratsioon
4. **Monitooringu seadistamine**: Valmistage ette monitooring ja logimine serva juurutamiseks

## Sihtgrupp Edge AI arendamiseks

### Edge AI arendajad
- Rakenduste arendajad, kes loovad tehisintellekti võimekusega servaseadmeid ja IoT lahendusi
- Manussüsteemide arendajad, kes integreerivad tehisintellekti võimekusi ressursipiirangutega seadmetesse
- Mobiiliarendajad, kes loovad seadmesiseseid tehisintellekti rakendusi nutitelefonidele ja tahvelarvutitele

### Edge AI insenerid
- Tehisintellekti insenerid, kes optimeerivad mudeleid serva juurutamiseks ja haldavad järeldustorustikke
- DevOps insenerid, kes juurutavad ja haldavad tehisintellekti mudeleid hajutatud servainfrastruktuuris
- Jõudlusinsenerid, kes optimeerivad tehisintellekti töökoormusi serva riistvara piirangute jaoks

### Teadlased ja õpetajad
- Tehisintellekti teadlased, kes arendavad tõhusaid mudeleid ja algoritme serva arvutamiseks
- Õpetajad, kes õpetavad Edge AI kontseptsioone ja demonstreerivad optimeerimistehnikaid
- Õpilased, kes õpivad serva tehisintellekti juurutamise väljakutsete ja lahenduste kohta

## Edge AI kasutusjuhtumid

### Nutikad IoT seadmed
- **Reaalajas pildituvastus**: Juurutage arvutinägemise mudeleid IoT kaamerates ja sensorites
- **Hääletöötlus**: Rakendage kõnetuvastust ja loodusliku keele töötlemist nutikõlarites
- **Ennetav hooldus**: Käitage anomaaliatuvastuse mudeleid tööstuslikel servaseadmetel
- **Keskkonnaseire**: Juurutage sensorite andmeanalüüsi mudeleid keskkonnarakenduste jaoks

### Mobiil- ja manusrakendused
- **Seadmesisene tõlkimine**: Rakendage keele tõlkimise mudeleid, mis töötavad võrguühenduseta
- **Liitreaalsus**: Juurutage reaalajas objektituvastust ja jälgimist AR rakenduste jaoks
- **Tervise jälgimine**: Käitage terviseanalüüsi mudeleid kantavatel seadmetel ja meditsiiniseadmetel
- **Autonoomsed süsteemid**: Rakendage otsuste tegemise mudeleid droonide, robotite ja sõidukite jaoks

### Serva arvutamise infrastruktuur
- **Serva andmekeskused**: Juurutage tehisintellekti mudeleid serva andmekeskustes madala latentsusega rakenduste jaoks
- **CDN integreerimine**: Integreerige tehisintellekti töötlemisvõimekus sisuedastusvõrkudesse
- **5G serv**: Kasutage 5G serva arvutamist tehisintellekti võimekusega rakenduste jaoks
- **Fog Computing**: Rakendage tehisintellekti töötlemist fog computing keskkondades

## Paigaldamine ja seadistamine

### Laienduse paigaldamine
Paigaldage AI Toolkit laiendus otse Visual Studio Code'i Marketplace'ist:

**Laienduse ID**: `ms-windows-ai-studio.windows-ai-studio`

**Paigaldamise meetodid**:
1. **VS Code Marketplace**: Otsige Extensions vaates "AI Toolkit"
2
2. Loo algsed viited, kasutades loomuliku keele kirjeldusi  
3. Iteratsiooni ja täpsusta viiteid mudeli vastuste põhjal  
4. Integreeri MCP tööriistad agentide võimekuse suurendamiseks  

#### Samm 3: Testimine ja hindamine  
1. Kasuta **Bulk Run** funktsiooni, et testida mitmeid viiteid valitud mudelitega  
2. Käivita agendid testjuhtumitega, et valideerida funktsionaalsust  
3. Hinda täpsust ja jõudlust sisseehitatud või kohandatud mõõdikute abil  
4. Võrdle erinevaid mudeleid ja konfiguratsioone  

#### Samm 4: Peenhäälestamine ja optimeerimine  
1. Kohanda mudeleid spetsiifiliste erijuhtumite jaoks  
2. Rakenda valdkonnaspetsiifilist peenhäälestamist  
3. Optimeeri piiratud ressursiga kasutuselevõtu jaoks  
4. Versiooni ja võrdle erinevaid agentide konfiguratsioone  

#### Samm 5: Kasutuselevõtu ettevalmistus  
1. Loo tootmisvalmis kood Agent Builderi abil  
2. Sea üles MCP serveri ühendused tootmiskasutuseks  
3. Valmista kasutuselevõtupaketid servaseadmete jaoks  
4. Konfigureeri jälgimise ja hindamise mõõdikud  

## Näidised AI tööriistakomplekti jaoks  

Proovi meie näidiseid  
[AI Toolkit näidised](https://github.com/Azure-Samples/AI_Toolkit_Samples) on loodud selleks, et aidata arendajatel ja teadlastel tõhusalt uurida ja rakendada AI lahendusi.  

Meie näidised sisaldavad:  

Näidiskood: Eelvalmistatud näited, mis demonstreerivad AI funktsionaalsusi, nagu mudelite treenimine, kasutuselevõtt või rakendustesse integreerimine.  
Dokumentatsioon: Juhendid ja õpetused, mis aitavad kasutajatel mõista AI Toolkit funktsioone ja nende kasutamist.  
Eeltingimused  

- Visual Studio Code  
- AI Toolkit Visual Studio Code jaoks  
- GitHubi peeneteraline isiklik juurdepääsutoken (PAT)  
- Foundry Local  

## Parimad tavad serva AI arendamiseks  

### Mudeli valik  
- **Suuruse piirangud**: Valige mudelid, mis sobivad sihtseadmete mälupiirangutega  
- **Järeldamise kiirus**: Eelistage mudeleid, millel on kiire järeldamise aeg reaalajas rakenduste jaoks  
- **Täpsuse kompromissid**: Tasakaalustage mudeli täpsus ressursipiirangutega  
- **Formaatide ühilduvus**: Eelistage ONNX või riistvarale optimeeritud formaate serva kasutuselevõtuks  

### Optimeerimistehnikad  
- **Kvantiseerimine**: Kasutage INT8 või INT4 kvantiseerimist, et vähendada mudeli suurust ja parandada kiirust  
- **Pügamine**: Eemaldage mittevajalikud mudeli parameetrid, et vähendada arvutusnõudeid  
- **Teadmiste destilleerimine**: Looge väiksemad mudelid, mis säilitavad suuremate mudelite jõudluse  
- **Riistvara kiirendus**: Kasutage NPUsid, GPUsid või spetsialiseeritud kiirendeid, kui need on saadaval  

### Arenduse töövoog  
- **Iteratiivne testimine**: Testige arenduse ajal sageli servasarnastes tingimustes  
- **Jõudluse jälgimine**: Jälgige pidevalt ressursikasutust ja järeldamise kiirust  
- **Versioonihaldus**: Jälgige mudeli versioone ja optimeerimisseadeid  
- **Dokumentatsioon**: Dokumenteerige kõik optimeerimisotsused ja jõudluse kompromissid  

### Kasutuselevõtu kaalutlused  
- **Ressursside jälgimine**: Jälgige tootmises mälu, CPU ja energiakasutust  
- **Tagasipöördumisstrateegiad**: Rakendage mehhanisme mudeli rikete korral  
- **Uuenduste mehhanismid**: Planeerige mudeli uuendused ja versioonihaldus  
- **Turvalisus**: Rakendage sobivaid turvameetmeid serva AI rakenduste jaoks  

## Integreerimine serva AI raamistikuga  

### ONNX Runtime  
- **Platvormidevaheline kasutuselevõtt**: Kasutage ONNX mudeleid erinevatel servaplatvormidel  
- **Riistvara optimeerimine**: Kasutage ONNX Runtime'i riistvaraspetsiifilisi optimeerimisi  
- **Mobiilne tugi**: Kasutage ONNX Runtime Mobile'i nutitelefonide ja tahvelarvutite rakenduste jaoks  
- **IoT integratsioon**: Kasutage ONNX Runtime'i kergeid jaotusi IoT seadmetel  

### Windows ML  
- **Windowsi seadmed**: Optimeerige Windowsi-põhiste servaseadmete ja arvutite jaoks  
- **NPU kiirendus**: Kasutage Windowsi seadmetel Neural Processing Units  
- **DirectML**: Kasutage DirectML-i GPU kiirenduseks Windowsi platvormidel  
- **UWP integratsioon**: Integreerige Universal Windows Platform rakendustega  

### TensorFlow Lite  
- **Mobiilne optimeerimine**: Kasutage TensorFlow Lite mudeleid mobiil- ja manusseadmetel  
- **Riistvara delegaadid**: Kasutage spetsialiseeritud riistvara delegaate kiirenduseks  
- **Mikrokontrollerid**: Kasutage TensorFlow Lite Micro't mikrokontrolleritel  
- **Platvormidevaheline tugi**: Kasutage Androidi, iOS-i ja manustatud Linuxi süsteemidel  

### Azure IoT Edge  
- **Pilv-serva hübriid**: Kombineerige pilvetreening serva järeldamisega  
- **Mooduli kasutuselevõtt**: Kasutage AI mudeleid IoT Edge moodulitena  
- **Seadme haldamine**: Hallake servaseadmeid ja mudeli uuendusi kaugelt  
- **Telemeetria**: Koguge jõudluse andmeid ja mudeli mõõdikuid serva kasutuselevõtust  

## Täiustatud serva AI stsenaariumid  

### Mitme mudeli kasutuselevõtt  
- **Mudeli ansamblid**: Kasutage mitut mudelit täpsuse parandamiseks või redundantsuse tagamiseks  
- **A/B testimine**: Testige erinevaid mudeleid samaaegselt servaseadmetel  
- **Dünaamiline valik**: Valige mudelid vastavalt seadme hetkeolukorrale  
- **Ressursside jagamine**: Optimeerige ressursikasutust mitme kasutusele võetud mudeli vahel  

### Federatiivne õppimine  
- **Jaotatud treening**: Treenige mudeleid mitmel servaseadmel  
- **Privaatsuse säilitamine**: Hoidke treeningandmed lokaalsed, jagades samal ajal mudeli täiustusi  
- **Koostööõpe**: Võimaldage seadmetel õppida kollektiivsetest kogemustest  
- **Serva-pilve koordineerimine**: Koordineerige õppimist servaseadmete ja pilve infrastruktuuri vahel  

### Reaalajas töötlemine  
- **Voogtöötlus**: Töötlege pidevaid andmevooge servaseadmetel  
- **Madal latentsus järeldamine**: Optimeerige minimaalsete järeldamise viivituste jaoks  
- **Partiitöötlus**: Töötlege tõhusalt andmepartiisid servaseadmetel  
- **Kohanduv töötlemine**: Kohandage töötlemist vastavalt seadme hetkevõimekusele  

## Serva AI arenduse tõrkeotsing  

### Levinud probleemid  
- **Mälupiirangud**: Mudel on sihtseadme mälu jaoks liiga suur  
- **Järeldamise kiirus**: Mudeli järeldamine on reaalajas nõuete jaoks liiga aeglane  
- **Täpsuse halvenemine**: Optimeerimine vähendab mudeli täpsust vastuvõetamatult  
- **Riistvara ühilduvus**: Mudel ei ühildu sihtseadme riistvaraga  

### Silumisstrateegiad  
- **Jõudluse profiilimine**: Kasutage AI Toolkit'i jälgimisfunktsioone pudelikaelade tuvastamiseks  
- **Ressursside jälgimine**: Jälgige arenduse ajal mälu ja CPU kasutust  
- **Järk-järguline testimine**: Testige optimeerimisi järk-järgult, et probleeme isoleerida  
- **Riistvara simulatsioon**: Kasutage arendustööriistu sihtseadme riistvara simuleerimiseks  

### Optimeerimislahendused  
- **Täiendav kvantiseerimine**: Rakendage agressiivsemaid kvantiseerimistehnikaid  
- **Mudeli arhitektuur**: Kaaluge erinevaid mudeli arhitektuure, mis on optimeeritud serva jaoks  
- **Eeltöötluse optimeerimine**: Optimeerige andmete eeltöötlust serva piirangute jaoks  
- **Järeldamise optimeerimine**: Kasutage riistvaraspetsiifilisi järeldamise optimeerimisi  

## Ressursid ja järgmised sammud  

### Ametlik dokumentatsioon  
- [AI Toolkit arendaja dokumentatsioon](https://aka.ms/AIToolkit/doc)  
- [Paigaldamise ja seadistamise juhend](https://code.visualstudio.com/docs/intelligentapps/overview#_install-and-setup)  
- [VS Code Intelligent Apps dokumentatsioon](https://code.visualstudio.com/docs/intelligentapps)  
- [Model Context Protocol (MCP) dokumentatsioon](https://modelcontextprotocol.io/)  

### Kogukond ja tugi  
- [AI Toolkit GitHubi repositoorium](https://github.com/microsoft/vscode-ai-toolkit)  
- [GitHubi probleemid ja funktsioonisoovid](https://aka.ms/AIToolkit/feedback)  
- [Azure AI Foundry Discordi kogukond](https://aka.ms/azureaifoundry/discord)  
- [VS Code laienduste turg](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)  

### Tehnilised ressursid  
- [ONNX Runtime dokumentatsioon](https://onnxruntime.ai/)  
- [Ollama dokumentatsioon](https://ollama.ai/)  
- [Windows ML dokumentatsioon](https://docs.microsoft.com/en-us/windows/ai/)  
- [Azure AI Foundry dokumentatsioon](https://learn.microsoft.com/en-us/azure/ai-foundry/)  

### Õppeprogrammid  
- [Serva AI põhialuste kursus](../Module01/README.md)  
- [Väikeste keelemudelite juhend](../Module02/README.md)  
- [Serva kasutuselevõtu strateegiad](../Module03/README.md)  
- [Windows serva AI arendus](./windowdeveloper.md)  

### Täiendavad ressursid  
- **Repositooriumi statistika**: 1.8k+ tähte, 150+ haru, 18+ kaastöölist  
- **Litsents**: MIT litsents  
- **Turvalisus**: Microsofti turvapoliitikad kehtivad  
- **Telemeetria**: Austab VS Code telemeetria seadeid  

## Kokkuvõte  

AI Toolkit Visual Studio Code jaoks esindab terviklikku platvormi kaasaegseks AI arenduseks, pakkudes sujuvaid agentide arendamise võimalusi, mis on eriti väärtuslikud serva AI rakenduste jaoks. Selle ulatuslik mudelikataloog, mis toetab pakkujaid nagu Anthropic, OpenAI, GitHub ja Google, koos kohaliku täitmisega ONNXi ja Ollama kaudu, pakub paindlikkust mitmekesiste serva kasutuselevõtu stsenaariumide jaoks.  

Tööriistakomplekti tugevus seisneb selle integreeritud lähenemises—alates mudelite avastamisest ja katsetamisest Playgroundis kuni keerukate agentide arendamiseni Prompt Builderiga, põhjalike hindamisvõimaluste ja sujuva MCP tööriistade integreerimiseni. Serva AI arendajatele tähendab see AI agentide kiiret prototüüpimist ja testimist enne serva kasutuselevõttu, võimalusega kiiresti iteratsiooni teha ja optimeerida ressursipiiratud keskkondade jaoks.  

Peamised eelised serva AI arendamiseks hõlmavad:  
- **Kiire katsetamine**: Testige mudeleid ja agente kiiresti enne serva kasutuselevõttu  
- **Mitme pakkuja paindlikkus**: Juurdepääs mudelitele erinevatest allikatest, et leida optimaalsed serva lahendused  
- **Kohalik arendus**: Testige ONNXi ja Ollama abil võrguühenduseta ja privaatsust säilitavat arendust  
- **Tootmisvalmidus**: Loo tootmisvalmis kood ja integreeri väliste tööriistadega MCP kaudu  
- **Põhjalik hindamine**: Kasutage sisseehitatud ja kohandatud mõõdikuid serva AI jõudluse valideerimiseks  

Kuna AI liigub üha enam serva kasutuselevõtu stsenaariumide suunas, pakub AI Toolkit VS Code jaoks arenduskeskkonda ja töövoogu, mis on vajalik intelligentsete rakenduste loomiseks, testimiseks ja optimeerimiseks ressursipiiratud keskkondade jaoks. Olgu tegemist IoT lahenduste, mobiilsete AI rakenduste või manustatud intelligentsussüsteemidega, tööriistakomplekti terviklik funktsioonide komplekt ja integreeritud töövoog toetavad kogu serva AI arenduse elutsüklit.  

Jätkuva arenduse ja aktiivse kogukonnaga (1.8k+ GitHubi tähte) jääb AI Toolkit AI arendustööriistade esirinnas, arenedes pidevalt, et vastata kaasaegsete AI arendajate vajadustele, kes loovad serva kasutuselevõtu stsenaariume.  

[Next Foundry Local](./foundrylocal.md)  

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.
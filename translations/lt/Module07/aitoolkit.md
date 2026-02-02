# AI įrankių rinkinys Visual Studio Code - Edge AI kūrimo vadovas

## Įvadas

Sveiki atvykę į išsamų vadovą, kaip naudoti AI įrankių rinkinį Visual Studio Code aplinkoje Edge AI kūrimui. Kadangi dirbtinis intelektas pereina nuo centralizuoto debesų kompiuterijos prie paskirstytų kraštinių įrenginių, kūrėjams reikia galingų, integruotų įrankių, kurie galėtų spręsti unikalius kraštinių diegimo iššūkius - nuo išteklių apribojimų iki reikalavimų veikti neprisijungus.

AI įrankių rinkinys Visual Studio Code aplinkoje užpildo šį spragą, suteikdamas pilną kūrimo aplinką, specialiai sukurtą kurti, testuoti ir optimizuoti AI programas, kurios efektyviai veikia kraštiniuose įrenginiuose. Nesvarbu, ar kuriate IoT jutikliams, mobiliesiems įrenginiams, įterptinėms sistemoms ar kraštiniams serveriams, šis įrankių rinkinys supaprastina visą jūsų kūrimo procesą pažįstamoje VS Code aplinkoje.

Šis vadovas padės jums suprasti pagrindines sąvokas, įrankius ir geriausią praktiką, kaip naudoti AI įrankių rinkinį jūsų Edge AI projektuose - nuo pradinio modelio pasirinkimo iki diegimo gamyboje.

## Apžvalga

AI įrankių rinkinys Visual Studio Code yra galingas plėtinys, kuris supaprastina agentų kūrimą ir AI programų kūrimą. Įrankių rinkinys suteikia išsamias galimybes tyrinėti, vertinti ir diegti AI modelius iš įvairių tiekėjų, įskaitant Anthropic, OpenAI, GitHub, Google, tuo pačiu palaikant vietinį modelių vykdymą naudojant ONNX ir Ollama.

Kas išskiria AI įrankių rinkinį, tai jo išsamus požiūris į visą AI kūrimo ciklą. Skirtingai nuo tradicinių AI kūrimo įrankių, kurie orientuojasi į vieną aspektą, AI įrankių rinkinys suteikia integruotą aplinką, apimančią modelių atradimą, eksperimentavimą, agentų kūrimą, vertinimą ir diegimą - visa tai pažįstamoje VS Code aplinkoje.

Platforma specialiai sukurta greitam prototipų kūrimui ir diegimui gamyboje, su funkcijomis, tokiomis kaip užklausų generavimas, greiti startai, sklandžios MCP (Model Context Protocol) įrankių integracijos ir išsamios vertinimo galimybės. Edge AI kūrimui tai reiškia, kad galite efektyviai kurti, testuoti ir optimizuoti AI programas kraštinio diegimo scenarijams, tuo pačiu išlaikydami visą kūrimo procesą VS Code aplinkoje.

## Mokymosi tikslai

Pasibaigus šiam vadovui, jūs galėsite:

### Pagrindinės kompetencijos
- **Įdiegti ir sukonfigūruoti** AI įrankių rinkinį Visual Studio Code Edge AI kūrimo procesams
- **Naršyti ir naudoti** AI įrankių rinkinio sąsają, įskaitant Modelių katalogą, Žaidimų aikštelę ir Agentų kūrimo įrankį
- **Pasirinkti ir vertinti** AI modelius, tinkamus kraštiniam diegimui, atsižvelgiant į našumą ir išteklių apribojimus
- **Konvertuoti ir optimizuoti** modelius naudojant ONNX formatą ir kvantavimo technikas kraštiniams įrenginiams

### Edge AI kūrimo įgūdžiai
- **Sukurti ir įgyvendinti** Edge AI programas naudojant integruotą kūrimo aplinką
- **Atlikti modelių testavimą** kraštinėmis sąlygomis naudojant vietinį įžvalgą ir išteklių stebėjimą
- **Kurti ir pritaikyti** AI agentus, optimizuotus kraštinio diegimo scenarijams
- **Vertinti modelių našumą** naudojant metrikas, svarbias kraštiniam kompiuterijos procesui (vėlavimas, atminties naudojimas, tikslumas)

### Optimizavimas ir diegimas
- **Taikyti kvantavimo ir genėjimo** technikas, kad sumažintumėte modelio dydį, išlaikant priimtiną našumą
- **Optimizuoti modelius** konkrečioms kraštinio kompiuterio platformoms, įskaitant CPU, GPU ir NPU pagreitį
- **Įgyvendinti geriausią praktiką** Edge AI kūrimui, įskaitant išteklių valdymą ir atsargines strategijas
- **Paruošti modelius ir programas** diegimui gamyboje kraštiniuose įrenginiuose

### Pažangios Edge AI sąvokos
- **Integruoti su kraštinėmis AI sistemomis** įskaitant ONNX Runtime, Windows ML ir TensorFlow Lite
- **Įgyvendinti daugiamodelines architektūras** ir federuoto mokymosi scenarijus kraštinėms aplinkoms
- **Spręsti dažnas Edge AI problemas** įskaitant atminties apribojimus, įžvalgos greitį ir aparatūros suderinamumą
- **Sukurti stebėjimo ir registravimo** strategijas Edge AI programoms gamyboje

### Praktinis pritaikymas
- **Sukurti pilnus Edge AI sprendimus** nuo modelio pasirinkimo iki diegimo
- **Demonstruoti įgūdžius** kraštiniams kūrimo procesams ir optimizavimo technikoms
- **Taikyti išmoktas sąvokas** realaus pasaulio Edge AI naudojimo atvejams, įskaitant IoT, mobilias ir įterptines programas
- **Vertinti ir palyginti** skirtingas Edge AI diegimo strategijas ir jų kompromisus

## Pagrindinės funkcijos Edge AI kūrimui

### 1. Modelių katalogas ir atradimas
- **Daugiatiekėjų palaikymas**: Naršykite ir pasiekite AI modelius iš Anthropic, OpenAI, GitHub, Google ir kitų tiekėjų
- **Vietinių modelių integracija**: Supaprastintas ONNX ir Ollama modelių atradimas kraštiniam diegimui
- **GitHub modeliai**: Tiesioginė integracija su GitHub modelių talpinimu, kad būtų lengviau pasiekti
- **Modelių palyginimas**: Palyginkite modelius vienas šalia kito, kad rastumėte optimalų balansą kraštinių įrenginių apribojimams

### 2. Interaktyvi žaidimų aikštelė
- **Interaktyvi testavimo aplinka**: Greitas eksperimentavimas su modelių galimybėmis kontroliuojamoje aplinkoje
- **Daugiarūšis palaikymas**: Testavimas su vaizdais, tekstu ir kitais įvesties tipais, būdingais kraštinėms situacijoms
- **Eksperimentavimas realiu laiku**: Momentinis grįžtamasis ryšys apie modelio atsakymus ir našumą
- **Parametrų optimizavimas**: Modelio parametrų pritaikymas kraštinio diegimo reikalavimams

### 3. Užklausų (agentų) kūrimo įrankis
- **Natūralios kalbos generavimas**: Sukurkite pradinius užklausas naudodami natūralios kalbos aprašymus
- **Iteratyvus tobulinimas**: Tobulinkite užklausas pagal modelio atsakymus ir našumą
- **Užduočių skaidymas**: Suskaidykite sudėtingas užduotis naudojant užklausų grandines ir struktūrizuotus rezultatus
- **Kintamųjų palaikymas**: Naudokite kintamuosius užklausose dinamiškam agentų elgesiui
- **Gamybos kodo generavimas**: Generuokite gamybai paruoštą kodą greitam programų kūrimui

### 4. Masinis vykdymas ir vertinimas
- **Daugiamodelinis testavimas**: Vykdykite kelias užklausas per pasirinktus modelius vienu metu
- **Efektyvus testavimas mastu**: Testuokite įvairias įvestis ir konfigūracijas efektyviai
- **Individualūs testavimo atvejai**: Vykdykite agentus su testavimo atvejais, kad patikrintumėte funkcionalumą
- **Našumo palyginimas**: Palyginkite rezultatus tarp skirtingų modelių ir konfigūracijų

### 5. Modelių vertinimas su duomenų rinkiniais
- **Standartinės metrikos**: Testuokite AI modelius naudodami įmontuotus vertintojus (F1 balas, aktualumas, panašumas, nuoseklumas)
- **Individualūs vertintojai**: Sukurkite savo vertinimo metrikas specifiniams naudojimo atvejams
- **Duomenų rinkinių integracija**: Testuokite modelius su išsamiais duomenų rinkiniais
- **Našumo matavimas**: Kiekybiškai įvertinkite modelio našumą kraštinio diegimo sprendimams

### 6. Modelių pritaikymo galimybės
- **Modelių pritaikymas**: Pritaikykite modelius specifiniams naudojimo atvejams ir sritims
- **Specializuotas pritaikymas**: Pritaikykite modelius specializuotoms sritims ir reikalavimams
- **Edge optimizavimas**: Pritaikykite modelius specialiai kraštinio diegimo apribojimams
- **Srities specifinis mokymas**: Sukurkite modelius, pritaikytus specifiniams kraštinio naudojimo atvejams

### 7. MCP įrankių integracija
- **Išorinių įrankių jungtys**: Jungkite agentus su išoriniais įrankiais per Model Context Protocol serverius
- **Veiksmai realiame pasaulyje**: Leiskite agentams užklausyti duomenų bazes, pasiekti API ar vykdyti individualią logiką
- **Esami MCP serveriai**: Naudokite įrankius iš komandų (stdio) arba HTTP (server-sent event) protokolų
- **Individualus MCP kūrimas**: Kurkite ir struktūrizuokite naujus MCP serverius su testavimu Agentų kūrimo įrankyje

### 8. Agentų kūrimas ir testavimas
- **Funkcijų kvietimo palaikymas**: Leiskite agentams dinamiškai kviesti išorines funkcijas
- **Testavimas realiu laiku**: Testuokite integracijas su realiu laiku vykdomais testais ir įrankių naudojimu
- **Agentų versijavimas**: Agentų versijų kontrolė su palyginimo galimybėmis vertinimo rezultatams
- **Debugging ir sekimas**: Vietinis sekimas ir klaidų taisymas agentų kūrimui

## Edge AI kūrimo procesas

### 1 etapas: Modelių atradimas ir pasirinkimas
1. **Naršykite modelių katalogą**: Naudokite modelių katalogą, kad rastumėte modelius, tinkamus kraštiniam diegimui
2. **Palyginkite našumą**: Vertinkite modelius pagal dydį, tikslumą ir įžvalgos greitį
3. **Testuokite vietoje**: Naudokite Ollama arba ONNX modelius testavimui vietoje prieš kraštinį diegimą
4. **Įvertinkite išteklių reikalavimus**: Nustatykite atminties ir skaičiavimo poreikius tiksliniams kraštiniams įrenginiams

### 2 etapas: Modelių optimizavimas
1. **Konvertuokite į ONNX**: Konvertuokite pasirinktus modelius į ONNX formatą kraštiniam suderinamumui
2. **Taikykite kvantavimą**: Sumažinkite modelio dydį naudodami INT8 arba INT4 kvantavimą
3. **Aparatūros optimizavimas**: Optimizuokite tiksliniams kraštiniams įrenginiams (ARM, x86, specializuoti pagreičiai)
4. **Našumo patvirtinimas**: Patvirtinkite, kad optimizuoti modeliai išlaiko priimtiną tikslumą

### 3 etapas: Programų kūrimas
1. **Agentų dizainas**: Naudokite Agentų kūrimo įrankį, kad sukurtumėte kraštiniams optimizuotus AI agentus
2. **Užklausų inžinerija**: Sukurkite užklausas, kurios efektyviai veikia su mažesniais kraštiniais modeliais
3. **Integracijos testavimas**: Testuokite agentus simuliuotomis kraštinėmis sąlygomis
4. **Kodo generavimas**: Generuokite gamybai optimizuotą kodą kraštiniam diegimui

### 4 etapas: Vertinimas ir testavimas
1. **Masinis vertinimas**: Testuokite kelias konfigūracijas, kad rastumėte optimalias kraštines sąlygas
2. **Našumo profilavimas**: Analizuokite įžvalgos greitį, atminties naudojimą ir tikslumą
3. **Kraštinė simuliacija**: Testuokite sąlygomis, panašiomis į tikslinį kraštinį diegimo aplinką
4. **Streso testavimas**: Vertinkite našumą įvairiomis apkrovos sąlygomis

### 5 etapas: Diegimo paruošimas
1. **Galutinis optimizavimas**: Taikykite galutines optimizacijas pagal testavimo rezultatus
2. **Diegimo paketavimas**: Supakuokite modelius ir kodą kraštiniam diegimui
3. **Dokumentacija**: Dokumentuokite diegimo reikalavimus ir konfigūraciją
4. **Stebėjimo nustatymas**: Paruoškite stebėjimą ir registravimą kraštiniam diegimui

## Tikslinė auditorija Edge AI kūrimui

### Edge AI kūrėjai
- Programų kūrėjai, kuriantys AI pagrįstus kraštinius įrenginius ir IoT sprendimus
- Įterptinių sistemų kūrėjai, integruojantys AI galimybes į išteklių apribotus įrenginius
- Mobilieji kūrėjai, kuriantys AI programas įrenginiuose, tokiuose kaip išmanieji telefonai ir planšetės

### Edge AI inžinieriai
- AI inžinieriai, optimizuojantys modelius kraštiniam diegimui ir valdantys įžvalgos procesus
- DevOps inžinieriai, diegiantys ir valdantys AI modelius paskirstytoje kraštinėje infrastruktūroje
- Našumo inžinieriai, optimizuojantys AI darbo krūvius kraštinės aparatūros apribojimams

### Tyrėjai ir pedagogai
- AI tyrėjai, kuriantys efektyvius modelius ir algoritmus kraštiniam kompiuterijos procesui
- Pedagogai, mokantys Edge AI sąvokų ir demonstruojantys optimizavimo technikas
- Studentai, besimokantys apie iššūkius ir sprendimus kraštinio AI diegimo srityje

## Edge AI naudojimo atvejai

### Išmanieji IoT įrenginiai
- **Vaizdų atpažinimas realiu laiku**: Diegti kompiuterinės vizijos modelius IoT kamerose ir jutikliuose
- **Balso apdorojimas**: Įgyvendinti kalbos atpažinimą ir natūralios kalbos apdorojimą išmaniuose garsiakalbiuose
- **Prognozuojama priežiūra**: Vykdyti anomalijų aptikimo modelius pramoniniuose kraštiniuose įrenginiuose
- **Aplinkos stebėjimas**: Diegti jutiklių duomenų analizės modelius aplinkos programoms

### Mobiliosios ir įterptinės programos
- **Vertimas įrenginyje**: Įgyvendinti kalbos vertimo modelius, kurie veikia neprisijungus
- **Papildyta realybė**: Diegti realaus laiko objektų atpažinimą ir sekimą AR programoms
- **Sveikatos stebėjimas**: Vykdyti sveikatos analizės modelius
2. Sukurkite pradinius raginimus naudodami natūralios kalbos aprašymus  
3. Kartokite ir tobulinkite raginimus pagal modelio atsakymus  
4. Integruokite MCP įrankius, kad pagerintumėte agentų galimybes  

#### 3 žingsnis: Testavimas ir vertinimas  
1. Naudokite **Bulk Run**, kad išbandytumėte kelis raginimus skirtinguose modeliuose  
2. Paleiskite agentus su testavimo atvejais, kad patikrintumėte funkcionalumą  
3. Įvertinkite tikslumą ir našumą naudodami įmontuotus arba pasirinktinius metrikos įrankius  
4. Palyginkite skirtingus modelius ir konfigūracijas  

#### 4 žingsnis: Tobulinimas ir optimizavimas  
1. Pritaikykite modelius specifiniams kraštutiniams naudojimo atvejams  
2. Taikykite specifinį domeno tobulinimą  
3. Optimizuokite pagal kraštutinius diegimo apribojimus  
4. Versijuokite ir palyginkite skirtingas agentų konfigūracijas  

#### 5 žingsnis: Paruošimas diegimui  
1. Sukurkite gamybai paruoštą kodą naudodami Agent Builder  
2. Nustatykite MCP serverio ryšius gamybos naudojimui  
3. Paruoškite diegimo paketus kraštutiniams įrenginiams  
4. Konfigūruokite stebėjimo ir vertinimo metrikas  

## AI įrankių rinkinio pavyzdžiai  

Išbandykite mūsų pavyzdžius  
[AI Toolkit pavyzdžiai](https://github.com/Azure-Samples/AI_Toolkit_Samples) sukurti tam, kad padėtų kūrėjams ir tyrėjams efektyviai tyrinėti ir įgyvendinti AI sprendimus.  

Mūsų pavyzdžiai apima:  

Pavyzdinis kodas: Iš anksto sukurti pavyzdžiai, demonstruojantys AI funkcionalumą, pvz., modelių mokymą, diegimą ar integravimą į programas.  
Dokumentacija: Vadovai ir pamokos, padedančios suprasti AI Toolkit funkcijas ir kaip jas naudoti.  
Reikalavimai  

- Visual Studio Code  
- AI Toolkit for Visual Studio Code  
- GitHub smulkiai apibrėžtas asmeninis prieigos raktas (PAT)  
- Foundry Local  

## Geriausia praktika kraštutiniam AI vystymui  

### Modelio pasirinkimas  
- **Dydžio apribojimai**: Pasirinkite modelius, kurie atitinka tikslinių įrenginių atminties apribojimus  
- **Įžvalgų greitis**: Pirmenybę teikite modeliams su greitu įžvalgų laiku realaus laiko programoms  
- **Tikslumo kompromisai**: Subalansuokite modelio tikslumą su resursų apribojimais  
- **Formatų suderinamumas**: Pirmenybę teikite ONNX arba aparatūros optimizuotiems formatams kraštutiniam diegimui  

### Optimizavimo technikos  
- **Kvantizacija**: Naudokite INT8 arba INT4 kvantizaciją, kad sumažintumėte modelio dydį ir pagerintumėte greitį  
- **Genėjimas**: Pašalinkite nereikalingus modelio parametrus, kad sumažintumėte skaičiavimo reikalavimus  
- **Žinių distiliacija**: Sukurkite mažesnius modelius, kurie išlaiko didesnių modelių našumą  
- **Aparatūros pagreitinimas**: Naudokite NPUs, GPUs arba specializuotus akceleratorius, kai jie yra prieinami  

### Vystymo procesas  
- **Iteratyvus testavimas**: Dažnai testuokite kraštutiniam naudojimui panašiomis sąlygomis vystymo metu  
- **Našumo stebėjimas**: Nuolat stebėkite resursų naudojimą ir įžvalgų greitį  
- **Versijų kontrolė**: Sekite modelio versijas ir optimizavimo nustatymus  
- **Dokumentacija**: Dokumentuokite visus optimizavimo sprendimus ir našumo kompromisus  

### Diegimo aspektai  
- **Resursų stebėjimas**: Stebėkite atminties, CPU ir energijos naudojimą gamyboje  
- **Atsarginės strategijos**: Įgyvendinkite atsargines mechanizmus modelio gedimams  
- **Atnaujinimo mechanizmai**: Planuokite modelio atnaujinimus ir versijų valdymą  
- **Saugumas**: Įgyvendinkite tinkamas saugumo priemones kraštutiniam AI programoms  

## Integracija su kraštutiniais AI rėmais  

### ONNX Runtime  
- **Kryžminė platforma**: Diegkite ONNX modelius skirtingose kraštutinėse platformose  
- **Aparatūros optimizavimas**: Pasinaudokite ONNX Runtime aparatūros specifinėmis optimizacijomis  
- **Mobilus palaikymas**: Naudokite ONNX Runtime Mobile išmaniesiems telefonams ir planšetėms  
- **IoT integracija**: Diegkite IoT įrenginiuose naudodami ONNX Runtime lengvas distribucijas  

### Windows ML  
- **Windows įrenginiai**: Optimizuokite Windows pagrindu veikiančius kraštutinius įrenginius ir kompiuterius  
- **NPU pagreitinimas**: Pasinaudokite Neural Processing Units Windows įrenginiuose  
- **DirectML**: Naudokite DirectML GPU pagreitinimui Windows platformose  
- **UWP integracija**: Integruokite su Universal Windows Platform programomis  

### TensorFlow Lite  
- **Mobilus optimizavimas**: Diegkite TensorFlow Lite modelius mobiliuose ir įterptiniuose įrenginiuose  
- **Aparatūros delegatai**: Naudokite specializuotus aparatūros delegatus pagreitinimui  
- **Mikro kontroleriai**: Diegkite mikro kontroleriuose naudodami TensorFlow Lite Micro  
- **Kryžminė platforma**: Diegkite Android, iOS ir įterptiniuose Linux sistemose  

### Azure IoT Edge  
- **Debesų-krašto hibridas**: Derinkite debesų mokymą su krašto įžvalgomis  
- **Modulių diegimas**: Diegkite AI modelius kaip IoT Edge modulius  
- **Įrenginių valdymas**: Nuotoliniu būdu valdykite kraštutinius įrenginius ir modelio atnaujinimus  
- **Telemetrija**: Rinkite našumo duomenis ir modelio metrikas iš kraštutinių diegimų  

## Pažangūs kraštutinio AI scenarijai  

### Daugelio modelių diegimas  
- **Modelių ansambliai**: Diegkite kelis modelius, kad pagerintumėte tikslumą arba užtikrintumėte atsarginį variantą  
- **A/B testavimas**: Testuokite skirtingus modelius vienu metu kraštutiniuose įrenginiuose  
- **Dinaminis pasirinkimas**: Pasirinkite modelius pagal dabartines įrenginio sąlygas  
- **Resursų dalijimasis**: Optimizuokite resursų naudojimą tarp kelių diegtų modelių  

### Federuotas mokymasis  
- **Distribuotas mokymas**: Mokykite modelius keliuose kraštutiniuose įrenginiuose  
- **Privatumo išsaugojimas**: Laikykite mokymo duomenis vietoje, dalindamiesi modelio patobulinimais  
- **Bendradarbiavimo mokymasis**: Leiskite įrenginiams mokytis iš kolektyvinės patirties  
- **Krašto-debesų koordinacija**: Koordinuokite mokymą tarp kraštutinių įrenginių ir debesų infrastruktūros  

### Realiojo laiko apdorojimas  
- **Srautinis apdorojimas**: Apdorokite nuolatinius duomenų srautus kraštutiniuose įrenginiuose  
- **Mažos vėlavimo įžvalgos**: Optimizuokite minimaliai įžvalgų vėlavimui  
- **Partinis apdorojimas**: Efektyviai apdorokite duomenų partijas kraštutiniuose įrenginiuose  
- **Adaptacinis apdorojimas**: Koreguokite apdorojimą pagal dabartines įrenginio galimybes  

## Kraštutinio AI vystymo trikčių šalinimas  

### Dažnos problemos  
- **Atminties apribojimai**: Modelis per didelis tikslinio įrenginio atminčiai  
- **Įžvalgų greitis**: Modelio įžvalgos per lėtos realaus laiko reikalavimams  
- **Tikslumo degradacija**: Optimizavimas nepriimtinai sumažina modelio tikslumą  
- **Aparatūros suderinamumas**: Modelis nesuderinamas su tiksline aparatūra  

### Derinimo strategijos  
- **Našumo profilavimas**: Naudokite AI Toolkit sekimo funkcijas, kad identifikuotumėte kliūtis  
- **Resursų stebėjimas**: Stebėkite atminties ir CPU naudojimą vystymo metu  
- **Inkrementinis testavimas**: Testuokite optimizacijas palaipsniui, kad izoliuotumėte problemas  
- **Aparatūros simuliacija**: Naudokite vystymo įrankius, kad simuliuotumėte tikslinę aparatūrą  

### Optimizavimo sprendimai  
- **Tolimesnė kvantizacija**: Taikykite agresyvesnes kvantizacijos technikas  
- **Modelio architektūra**: Apsvarstykite skirtingas modelio architektūras, optimizuotas kraštui  
- **Išankstinio apdorojimo optimizavimas**: Optimizuokite duomenų išankstinį apdorojimą kraštutiniams apribojimams  
- **Įžvalgų optimizavimas**: Naudokite aparatūros specifines įžvalgų optimizacijas  

## Ištekliai ir tolesni žingsniai  

### Oficialios dokumentacijos  
- [AI Toolkit kūrėjų dokumentacija](https://aka.ms/AIToolkit/doc)  
- [Diegimo ir nustatymo vadovas](https://code.visualstudio.com/docs/intelligentapps/overview#_install-and-setup)  
- [VS Code Intelligent Apps dokumentacija](https://code.visualstudio.com/docs/intelligentapps)  
- [Model Context Protocol (MCP) dokumentacija](https://modelcontextprotocol.io/)  

### Bendruomenė ir palaikymas  
- [AI Toolkit GitHub saugykla](https://github.com/microsoft/vscode-ai-toolkit)  
- [GitHub problemos ir funkcijų užklausos](https://aka.ms/AIToolkit/feedback)  
- [Azure AI Foundry Discord bendruomenė](https://aka.ms/azureaifoundry/discord)  
- [VS Code plėtinių rinka](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)  

### Techniniai ištekliai  
- [ONNX Runtime dokumentacija](https://onnxruntime.ai/)  
- [Ollama dokumentacija](https://ollama.ai/)  
- [Windows ML dokumentacija](https://docs.microsoft.com/en-us/windows/ai/)  
- [Azure AI Foundry dokumentacija](https://learn.microsoft.com/en-us/azure/ai-foundry/)  

### Mokymosi keliai  
- [Kraštutinio AI pagrindų kursas](../Module01/README.md)  
- [Mažų kalbos modelių vadovas](../Module02/README.md)  
- [Kraštutinio diegimo strategijos](../Module03/README.md)  
- [Windows kraštutinio AI vystymas](./windowdeveloper.md)  

### Papildomi ištekliai  
- **Saugyklos statistika**: 1.8k+ žvaigždžių, 150+ šakų, 18+ bendradarbių  
- **Licencija**: MIT licencija  
- **Saugumas**: Taikomos Microsoft saugumo politikos  
- **Telemetrija**: Gerbia VS Code telemetrijos nustatymus  

## Išvada  

AI Toolkit for Visual Studio Code yra išsamus modernios AI vystymo platformos pavyzdys, suteikiantis supaprastintas agentų vystymo galimybes, kurios ypač vertingos kraštutiniam AI pritaikymui. Su plačiu modelių katalogu, palaikančiu tiekėjų, tokių kaip Anthropic, OpenAI, GitHub ir Google, kartu su vietiniu vykdymu per ONNX ir Ollama, įrankių rinkinys siūlo lankstumą, reikalingą įvairiems kraštutiniams diegimo scenarijams.  

Įrankių rinkinio stiprybė slypi integruotame požiūryje – nuo modelių atradimo ir eksperimentavimo Playground iki sudėtingo agentų vystymo su Prompt Builder, išsamių vertinimo galimybių ir sklandžios MCP įrankių integracijos. Kraštutiniams AI kūrėjams tai reiškia greitą AI agentų prototipų kūrimą ir testavimą prieš kraštutinį diegimą, su galimybe greitai iteruoti ir optimizuoti resursų apribotoms aplinkoms.  

Pagrindiniai privalumai kraštutiniam AI vystymui apima:  
- **Greitas eksperimentavimas**: Greitai testuokite modelius ir agentus prieš įsipareigojant kraštutiniam diegimui  
- **Daugelio tiekėjų lankstumas**: Pasiekite modelius iš įvairių šaltinių, kad rastumėte optimalų kraštutinį sprendimą  
- **Vietinis vystymas**: Testuokite su ONNX ir Ollama neprisijungus ir privatumo išsaugojimui  
- **Gamybos pasirengimas**: Generuokite gamybai paruoštą kodą ir integruokite su išoriniais įrankiais per MCP  
- **Išsamus vertinimas**: Naudokite įmontuotas ir pasirinktines metrikas, kad patikrintumėte kraštutinio AI našumą  

Kadangi AI vis labiau pereina prie kraštutinių diegimo scenarijų, AI Toolkit for VS Code suteikia vystymo aplinką ir darbo eigą, reikalingą kurti, testuoti ir optimizuoti intelektualias programas resursų apribotoms aplinkoms. Nesvarbu, ar kuriate IoT sprendimus, mobiliąsias AI programas, ar įterptines intelektualias sistemas, įrankių rinkinio išsamus funkcijų rinkinys ir integruota darbo eiga palaiko visą kraštutinio AI vystymo ciklą.  

Su nuolatiniu vystymu ir aktyvia bendruomene (1.8k+ GitHub žvaigždžių), AI Toolkit išlieka AI vystymo įrankių priešakyje, nuolat tobulėdamas, kad atitiktų modernių AI kūrėjų poreikius, kuriančių kraštutiniam diegimui.  

[Next Foundry Local](./foundrylocal.md)  

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Dėl svarbios informacijos rekomenduojama profesionali žmogaus vertimo paslauga. Mes neprisiimame atsakomybės už nesusipratimus ar neteisingus aiškinimus, kylančius dėl šio vertimo naudojimo.
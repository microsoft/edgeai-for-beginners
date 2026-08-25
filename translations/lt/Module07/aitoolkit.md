# AI įrankių rinkinys Visual Studio Code – Edge AI plėtros vadovas

## Įvadas

Sveiki atvykę į išsamų vadovą, kaip naudotis AI įrankių rinkiniu Visual Studio Code Edge AI plėtroje. Kai dirbtinis intelektas pereina nuo centralizuoto debesų skaičiavimo prie paskirstytų edge įrenginių, kūrėjams reikia galingų, integruotų įrankių, kurie galėtų spręsti unikalius edge diegimo iššūkius – nuo išteklių apribojimų iki neprisijungimo veikimo reikalavimų.

AI įrankių rinkinys Visual Studio Code užpildo šią spragą, suteikdamas pilną kūrimo aplinką, skirtą AI programų kūrimui, testavimui ir optimizavimui, kurios efektyviai veikia edge įrenginiuose. Nesvarbu, ar kuriate IoT jutikliams, mobiliems įrenginiams, įterptoms sistemoms ar edge serveriams, šis įrankių rinkinys supaprastina visą kūrimo procesą įprastoje VS Code aplinkoje.

Šiame vadove bus aptariamos pagrindinės sąvokos, įrankiai ir geriausios praktikos, kaip pasinaudoti AI įrankių rinkiniu savo Edge AI projektuose – nuo pirminio modelio pasirinkimo iki gamybos diegimo.

## Apžvalga

AI įrankių rinkinys Visual Studio Code yra galinga plėtinys, supaprastinantis agentų kūrimą ir AI programų kūrimą. Šis įrankių rinkinys suteikia išsamių galimybių tyrinėti, vertinti ir diegti AI modelius iš daugybės teikėjų – įskaitant Anthropic, OpenAI, GitHub, Google – ir palaiko vietinį modelių vykdymą naudojant ONNX ir Ollama.

Kas išskiria AI įrankių rinkinį, tai jo išsamus požiūris į visą AI kūrimo ciklą. Skirtingai nuo tradicinių AI kūrimo įrankių, kurie fokusuoja į atskirus aspektus, AI įrankių rinkinys suteikia integruotą aplinką, apimančią modelių paiešką, eksperimentavimą, agentų kūrimą, vertinimą ir diegimą – visa tai vyksta įprastoje VS Code aplinkoje.

Platforma sukurta sparčiam prototipavimui ir gamybos diegimui, su tokiomis funkcijomis kaip greitas užklausų generavimas, pradedančiųjų įrankiai, sklandžios MCP (Model Context Protocol) įrankių integracijos ir plati vertinimo funkcionalumas. Edge AI plėtroje tai reiškia, kad galite efektyviai kurti, testuoti ir optimizuoti AI programas edge įrenginiams, išlaikant pilną kūrimo srautą VS Code.

## Mokymosi tikslai

Baigę šį vadovą galėsite:

### Pagrindiniai gebėjimai
- **Įdiegti ir konfigūruoti** AI įrankių rinkinį Visual Studio Code Edge AI plėtros darbų srautams
- **Naršyti ir naudotis** AI įrankių rinkinio vartotojo sąsaja, įskaitant Modelių katalogą, Playground ir Agentų kūrėją
- **Pasirinkti ir įvertinti** AI modelius, tinkamus edge diegimui, atsižvelgiant į našumą ir išteklių apribojimus
- **Konvertuoti ir optimizuoti** modelius, naudojant ONNX formatą ir kvantizacijos metodus edge įrenginiams

### Edge AI plėtros įgūdžiai
- **Projektuoti ir įgyvendinti** Edge AI programas naudojant integruotą kūrimo aplinką
- **Atlikti modelių testavimą** edge sąlygoms panašiose aplinkose, naudojant vietinį inferencijos ir išteklių stebėjimą
- **Kurti ir pritaikyti** AI agentus, optimizuotus edge diegimo scenarijams
- **Vertinti modelių našumą** naudojant edge skaičiavimams būdingus rodiklius (atidėjimas, atminties naudojimas, tikslumas)

### Optimizavimas ir diegimas
- **Taikyti kvantizavimo ir apkarpymo** metodus, siekiant sumažinti modelio dydį, išlaikant priimtiną našumą
- **Optimizuoti modelius** konkrečiai edge aparatinei įrangai, įskaitant CPU, GPU ir NPU pagreitintuvus
- **Įgyvendinti geriausias praktikas** Edge AI plėtroje, įskaitant išteklių valdymą ir atsarginių strategijų taikymą
- **Paruošti modelius ir programas** gamybos diegimui edge įrenginiuose

### Pažengusios Edge AI sąvokos
- **Integruotis su edge AI sistemomis** įskaitant ONNX Runtime, Windows ML ir TensorFlow Lite
- **Įgyvendinti daugiamodelių architektūras** ir federuotą mokymą edge aplinkose
- **Spręsti dažniausias edge AI problemas** įskaitant atminties apribojimus, inferencijos greitį ir aparatūros suderinamumą
- **Projektuoti stebėjimo ir žurnalo** strategijas Edge AI programoms gamybos aplinkoje

### Praktinis taikymas
- **Kurti pilnas Edge AI sprendimų grandines** nuo modelio pasirinkimo iki diegimo
- **Demonstracija įgūdžių** edge specifiniuose kūrimo projektuose ir optimizavimo metodose
- **Taikyti įgytas žinias** realaus pasaulio edge AI panaudojimuose, įskaitant IoT, mobiliąsias ir įterptąsias programas
- **Vertinti ir palyginti** skirtingas edge AI diegimo strategijas ir jų kompromisus

## Pagrindinės Edge AI kūrimo funkcijos

### 1. Modelių katalogas ir paieška
- **Daugiaprotektorių palaikymas**: Naršykite ir pasiekite AI modelius iš Anthropic, OpenAI, GitHub, Google ir kitų teikėjų
- **Vietinė modelių integracija**: Supaprastinta ONNX ir Ollama modelių paieška edge diegimui
- **GitHub modeliai**: Tiesioginė integracija su GitHub modelių talpinimu sklandžiai prieigai
- **Modelių palyginimas**: Lyginkite modelius šalia vienas kito, kad rastumėte optimalią pusiausvyrą edge įrenginių apribojimams

### 2. Interaktyvus Playground
- **Interaktyvi bandymų aplinka**: Greitas eksperimentavimas su modelių galimybėmis kontroliuojamoje aplinkoje
- **Daugiamodalinis palaikymas**: Testuokite su vaizdais, tekstu ir kitais įvedimais, būdingais edge scenarijams
- **Realaus laiko eksperimentavimas**: Akimirksniu gaukite atsiliepimus apie modelio atsakus ir našumą
- **Parametrų optimizavimas**: Koreguokite modelio parametrus edge diegimo reikalavimams

### 3. Užklausų (Agentų) kūrėjas
- **Natūralios kalbos generavimas**: Generuokite pradines užklausas naudodami natūralių kalbų aprašymus
- **Iteratyvus tobulinimas**: Tobulinkite užklausas pagal modelio atsakus ir našumą
- **Užduočių suskaidymas**: Sudėtingas užduotis suskaidykite su užklausų grandiniais ir struktūruotais atsakymais
- **Kintamųjų palaikymas**: Naudokite kintamuosius užklausose dinamiškam agentų elgesiui
- **Gamybinio kodo generavimas**: Sugeneruokite gamybai paruoštą kodą greitam programų kūrimui

### 4. Kiekybinis vykdymas ir vertinimas
- **Daugiamodelių testavimas**: Vykdykite kelias užklausas iš karto su pasirinktais modeliais
- **Efektyvus testavimas mastu**: Greitai išbandykite įvairius įvedimus ir konfigūracijas
- **Individualūs bandymo atvejai**: Vykdykite agentus su testinėmis situacijomis funkcionalumui patikrinti
- **Našumo palyginimas**: Lyginkite rezultatus tarp skirtingų modelių ir konfigūracijų

### 5. Modelių vertinimas su duomenų rinkiniais
- **Standartiniai matavimai**: Testuokite AI modelius su integruotais vertintojais (F1 balas, aktualumas, panašumas, nuoseklumas)
- **Individualūs vertintojai**: Kurkite savo vertinimo metrikas specifinėms panaudojimo situacijoms
- **Duomenų rinkinių integracija**: Testuokite modelius su išsamiais duomenų rinkiniais
- **Našumo matavimas**: Kiekybiškai įvertinkite modelių našumą edge diegimo sprendimams

### 6. Tolimesnis modelių derinimas
- **Modelių pritaikymas**: Pritaikykite modelius specifinėms panaudojimo sritims ir domenams
- **Specializuotas adaptavimas**: Adaptuokite modelius specializuotiems domenams ir reikalavimams
- **Edge optimizacija**: Koreguokite modelius specialiai edge diegimo apribojimams
- **Domenui specifiškas mokymas**: Kurkite modelius, pritaikytus konkrečioms edge panaudojimo atvejams

### 7. MCP įrankių integracija
- **Išorinių įrankių jungtis**: Prisijunkite prie agentų per Model Context Protocol serverius
- **Realaus pasaulio veiksmai**: Leiskite agentams užklausti duomenų bazes, pasiekti API ar vykdyti kitą logiką
- **Esami MCP serveriai**: Naudokite įrankius per komandų (stdio) arba HTTP (serverio įvykiai) protokolus
- **Individuali MCP kūrimas**: Kurkite ir modeliuokite naujus MCP serverius su testavimu Agentų kūrėjo aplinkoje

### 8. Agentų kūrimas ir testavimas
- **Funkcijų iškvietimų palaikymas**: Leiskite agentams dinamiškai kviesti išorines funkcijas
- **Realaus laiko integracijos testavimas**: Testuokite integracijas su realaus laiko paleidimais ir įrankių naudojimu
- **Agentų versijavimas**: Valdykite agentų versijas su galimybėmis palyginti vertinimo rezultatus
- **Derinimas ir sekimas**: Vietiniai įrankiai agentų kūrimui derinti ir stebėti

## Edge AI kūrimo darbo eiga

### 1 etapas: modelių paieška ir pasirinkimas
1. **Naršykite modelių katalogą**: Naudokite modelių katalogą, kad rastumėte modelius, tinkamus edge diegimui
2. **Palyginkite našumą**: Įvertinkite modelius pagal dydį, tikslumą ir inferencijos greitį
3. **Testuokite vietoje**: Naudodami Ollama arba ONNX modelius išbandykite vietoje prieš edge diegimą
4. **Įvertinkite išteklių poreikius**: Nustatykite atminties ir skaičiavimo reikalavimus tiksliniams edge įrenginiams

### 2 etapas: modelių optimizavimas
1. **Konvertuokite į ONNX**: Pasirinktus modelius konvertuokite į ONNX formatą, suderinamą su edge įrenginiais
2. **Taikykite kvantizavimą**: Sumažinkite modelio dydį naudodami INT8 arba INT4 kvantizaciją
3. **Optimizuokite aparatūrai**: Optimizuokite modeliui pagal tikslinį edge aparatūros tipą (ARM, x86, specializuoti pagreitintuvai)
4. **Patvirtinkite našumą**: Įsitikinkite, kad optimizuoti modeliai išlaiko priimtiną tikslumą

### 3 etapas: programos kūrimas
1. **Agentų projektavimas**: Naudokite Agentų kūrėją, kad sukurtumėte edge optimizuotus AI agentus
2. **Užklausų kūrimas**: Kurkite užklausas, kurios efektyviai veiktų su mažesniais edge modeliais
3. **Integracijos testavimas**: Testuokite agentų veikimą simuliuotomis edge sąlygomis
4. **Kodo generavimas**: Generuokite gamybai optimizuotą kodą edge diegimui

### 4 etapas: vertinimas ir testavimas
1. **Kiekybinis vertinimas**: Testuokite kelias konfigūracijas, kad surastumėte optimalias edge nustatymus
2. **Našumo profilavimas**: Analizuokite inferencijos greitį, atminties naudojimą ir tikslumą
3. **Edge simuliacija**: Testuokite sąlygose, panašiomis į tikslinę edge diegimo aplinką
4. **Streso testavimas**: Vertinkite našumą esant įvairioms apkrovos sąlygoms

### 5 etapas: diegimo paruošimas
1. **Galutinė optimizacija**: Pritaikykite galutines optimizacijas pagal testavimo rezultatus
2. **Diegimo paketavimas**: Supakuokite modelius ir kodą edge diegimui
3. **Dokumentacija**: Paruoškite diegimo reikalavimų ir konfigūracijos dokumentaciją
4. **Stebėjimo paruošimas**: Pasiruoškite stebėjimui ir žurnalų fiksavimui edge diegime

## Tikslinė auditorija Edge AI kūrėjams

### Edge AI kūrėjai
- Programėlių kūrėjai, kuriantys AI valdomus edge įrenginius ir IoT sprendimus
- Įterptų sistemų kūrėjai, įdiegiantys AI galimybes į ribotų išteklių įrenginius
- Mobilieji kūrėjai, kuriantys įrenginiuose veikiančias AI programas telefonams ir planšetėms

### Edge AI inžinieriai
- AI inžinieriai, optimizuojantys modelius edge diegimui ir valdantys inferencijos grandinės procesus
- DevOps inžinieriai, diegiantys ir valdantys AI modelius paskirstytoje edge infrastruktūroje
- Našumo inžinieriai, optimizuojantys AI darbo krūvius pagal edge aparatūros apribojimus

### Tyrėjai ir pedagogai
- AI tyrėjai, kuriantys efektyvius modelius ir algoritmus edge skaičiavimams
- Pedagogai, mokantys Edge AI sąvokų ir demonstruojantys optimizavimo metodus
- Studentai, besimokantys apie iššūkius ir sprendimus edge AI diegime

## Edge AI panaudojimo atvejai

### Išmanieji IoT įrenginiai
- **Realaus laiko vaizdų atpažinimas**: Diegti kompiuterinės regos modelius IoT kameroms ir jutikliams
- **Balso apdorojimas**: Įgyvendinti kalbos atpažinimą ir natūralios kalbos apdorojimą išmaniuosiuose garsiakalbiuose
- **Prognozuojamoji priežiūra**: Vykdyti anomalijų aptikimo modelius pramonės edge įrenginiuose
- **Aplinkos stebėjimas**: Diegti jutiklių duomenų analizės modelius aplinkos taikymams

### Mobiliosios ir įterptosios programos
- **Įrenginio vertimas**: Įgyvendinti kalbų vertimo modelius veikiančius neprisijungus
- **Papildyta realybė**: Diegti realaus laiko objektų atpažinimą ir sekimą AR programose
- **Sveikatos stebėjimas**: Vykdyti sveikatos analizės modelius dėvimose įrangoje ir medicininėje įrangoje
- **Autonominės sistemos**: Įgyvendinti sprendimų priėmimo modelius dronams, robotams ir transporto priemonėms

### Edge skaičiavimo infrastruktūra
- **Edge duomenų centrai**: Diegti AI modelius edge duomenų centruose mažo delsos taikymams
- **CDN integracija**: Integruoti AI apdorojimo galimybes turinio pristatymo tinkluose
- **5G Edge**: Pasinaudoti 5G edge skaičiavimu AI valdomoms programoms
- **Rūko skaičiavimas**: Įgyvendinti AI apdorojimą rūko skaičiavimo aplinkose

## Diegimas ir nustatymas

### Plėtinio diegimas
Įdiekite AI įrankių rinkinio plėtinį tiesiogiai iš Visual Studio Code Marketplace:

**Plėtinio ID**: `ms-windows-ai-studio.windows-ai-studio`

**Diegimo būdai**:
1. **VS Code Marketplace**: Ieškokite „AI Toolkit“ Extensions peržiūros skiltyje
2. **Komandinė eilutė**: `code --install-extension ms-windows-ai-studio.windows-ai-studio`
3. **Tiesioginis diegimas**: Atsisiųskite iš [VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)

### Būtini reikalavimai Edge AI plėtrai
- **Visual Studio Code**: Rekomenduojama naujausia versija
- **Python aplinka**: Python 3.8+ su reikiamomis AI bibliotekomis
- **ONNX Runtime** (pasirinktinai): ONNX modelio inferencijai
- **Ollama** (pasirinktinai): Vietiniam modelių aptarnavimui
- **Aparatūros pagreitinimo įrankiai**: CUDA, OpenVINO arba platformai specifiški pagreitintuvai

### Pirminiai nustatymai
1. **Plėtinio aktyvavimas**: Atidarykite VS Code ir patikrinkite, ar AI įrankių rinkinys matomas veiksmo juostoje
2. **Modelių teikėjo nustatymai**: Sujunkite prie GitHub, OpenAI, Anthropic ar kitų modelių teikėjų
3. **Vietinė aplinka**: Paruoškite Python aplinką ir įdiekite reikiamus paketus
4. **Aparatūros pagreitinimas**: Jei įmanoma, konfigūruokite GPU/NPU pagreitinimą
5. **MCP integracija**: Prireikus nustatykite Model Context Protocol serverius

### Pirmojo naudojimo patikrinimo sąrašas
- [ ] AI įrankių rinkinio plėtinys įdiegtas ir aktyvuotas
- [ ] Modelių katalogas pasiekiamas ir modeliai randami
- [ ] Playground veikia modelių testavimui
- [ ] Agentų kūrėjas pasiekiamas užklausų kūrimui
- [ ] Vietinė kūrimo aplinka paruošta
- [ ] Aparatūros pagreitinimas (jei taikoma) tinkamai sukonfigūruotas

## Pradžia su AI įrankių rinkiniu

### Greito paleidimo vadovas

Rekomenduojame pradėti nuo GitHub talpinamų modelių, kad patirtis būtų kuo sklandesnė:

1. **Įdiegimas**: Vadovaukitės [įdiegimo vadovu](https://code.visualstudio.com/docs/intelligentapps/overview#_install-and-setup), kad pasiruoštumėte AI įrankių rinkinį savo įrenginyje
2. **Modelių paieška**: Iš plėtinio medžio peržiūros skiltyje pasirinkite **CATALOG > Models** norėdami tyrinėti turimus modelius
3. **GitHub modeliai**: Pradėkite nuo GitHub talpinamų modelių, kad būtų užtikrinta optimaliausia integracija
4. **Playground testavimas**: Iš bet kurios modelio kortelės pasirinkite **Try in Playground**, kad pradėtumėte eksperimentuoti su modelio galimybėmis

### Žingsnis po žingsnio Edge AI plėtra

#### 1 žingsnis: modelių tyrinėjimas ir pasirinkimas
1. Atidarykite AI įrankių rinkinio peržiūrą VS Code Veiksmo juostoje
2. Naršykite Modelių katalogą, kad rastumėte modelius, tinkamus edge diegimui
3. Filtruokite pagal teikėją (GitHub, ONNX, Ollama), atsižvelgdami į savo edge reikalavimus
4. Naudokite **Try in Playground** norėdami iš karto išbandyti modelio galimybes

#### 2 žingsnis: agentų kūrimas
1. Naudokite **Užklausų (Agentų) kūrėją**, kad sukurtumėte edge optimizuotus AI agentus
2. Generuokite pradines užklausas naudodami natūralių kalbų aprašymus
3. Iteratyviai tobulinkite užklausas pagal modelio atsakus
4. Integruokite MCP įrankius, kad pagerintumėte agentų galimybes


#### 3 žingsnis: Testavimas ir vertinimas
1. Naudokite **Bulk Run**, kad išbandytumėte kelis užklausimus skirtingose pasirinktuose modeliuose
2. Paleiskite agentus su testavimo atvejais, kad patvirtintumėte funkcionalumą
3. Įvertinkite tikslumą ir našumą naudodami įmontuotus arba pasirinktinius metrikus
4. Palyginkite skirtingus modelius ir konfigūracijas

#### 4 žingsnis: Smulkus reguliavimas ir optimizavimas
1. Pritaikykite modelius specifiniams kraštinių naudotojų atvejams
2. Taikykite srities specifinį smulkų reguliavimą
3. Optimizuokite kraštinių įrenginių diegimo apribojimams
4. Versijuokite ir palyginkite skirtingas agentų konfigūracijas

#### 5 žingsnis: Paruošimas diegimui
1. Generuokite gamybos kodą naudodami Agent Builder
2. Nustatykite MCP serverio jungtis gamybiniam naudojimui
3. Paruoškite diegimo paketus kraštinių įrenginiams
4. Konfigūruokite stebėjimo ir vertinimo metrikas

## Pavyzdžiai AI įrankių rinkiniui 

Išbandykite mūsų pavyzdžius
[AI įrankių rinkinio pavyzdžiai](https://github.com/Azure-Samples/AI_Toolkit_Samples) skirti padėti kūrėjams ir tyrėjams efektyviai tirti ir įgyvendinti AI sprendimus.

Mūsų pavyzdžiai apima:

Pavyzdinis kodas: Paruošti pavyzdžiai, demonstruojantys AI funkcionalumą, pvz., mokymas, diegimas ar modelių integracija į programas.
Dokumentacija: Vadovai ir pamokos, padedančios vartotojams suprasti AI įrankių rinkinio funkcijas ir jų naudojimą.
Išankstinės sąlygos

- Visual Studio Code
- AI įrankių rinkinys Visual Studio Code
- GitHub smulkiai valdomas asmeninis prieigos raktas (PAT)
- Foundry Local

## Geriausios praktikos kraštinių AI plėtrai

### Modelių pasirinkimas
- **Dydžio apribojimai**: Pasirinkite modelius, kurie tilptų į tikslo įrenginių atminties ribas
- **Atpažeistumo greitis**: Prioritetu teikite modeliams, kurie greitai apdoroja duomenis realaus laiko programoms
- **Tikslumo kompromisai**: Subalansuokite modelio tikslumą ir resursų apribojimus
- **Formato suderinamumas**: Rinkitės ONNX arba aparatine įranga optimizuotus formatus kraštinių diegimui

### Optimizavimo metodai
- **Kvantizavimas**: Naudokite INT8 arba INT4 kvantizavimą, kad sumažintumėte modelio dydį ir pagerintumėte greitį
- **Pruning**: Pašalinkite nereikalingus modelio parametrus, kad sumažintumėte skaičiavimo reikalavimus
- **Žinių distiliacija**: Sukurkite mažesnius modelius, kurie išlaiko didesnių našumą
- **Aparatinė pagreitinimas**: Naudokite NPU, GPU arba specialius pagreitintuvus, kai jie prieinami

### Plėtros darbo eiga
- **Iteratyvus testavimas**: Reguliariai testuokite kraštinių sąlygų aplinkoje kūrimo metu
- **Veiklos stebėjimas**: Nuolat stebėkite resursų naudojimą ir atpažeistumo greitį
- **Versijų valdymas**: Sekite modelių versijas ir optimizavimo nustatymus
- **Dokumentavimas**: Dokumentuokite visas optimizavimo sprendimus ir veiklos kompromisus

### Diegimo svarstymai
- **Resursų stebėjimas**: Stebėkite atminties, CPU ir energijos sunaudojimą gamyboje
- **Atsarginės strategijos**: Įgyvendinkite atsarginius mechanizmus modelių gedimams
- **Atnaujinimų mechanizmai**: Planuokite modelių atnaujinimus ir versijų valdymą
- **Saugumas**: Įgyvendinkite tinkamas saugumo priemones kraštinių AI programoms

## Integracija su kraštinių AI sistemomis

### ONNX Runtime
- **Kryžminis platformų diegimas**: Diegkite ONNX modelius skirtingose kraštinių platformose
- **Aparatinės įrangos optimizavimas**: Naudokite ONNX Runtime aparatine įranga pagrįstą optimizavimą
- **Mobilioji palaikymas**: Naudokite ONNX Runtime Mobile išmaniesiems telefonams ir planšetėms
- **IoT integracija**: Diegimas IoT įrenginiuose su ONNX Runtime lengvomis versijomis

### Windows ML
- **Windows įrenginiai**: Optimizavimas Windows pagrindu veikiantiems kraštinių įrenginiams ir PC
- **NPU pagreitinimas**: Naudokite neuroninius apdorojimo vienetus Windows įrenginiuose
- **DirectML**: Naudokite DirectML GPU pagreitinimui Windows platformose
- **UWP integracija**: Integruokite su Universal Windows Platform programomis

### TensorFlow Lite
- **Mobilioji optimizacija**: Diegkite TensorFlow Lite modelius mobiliuosiuose ir įterptuose įrenginiuose
- **Aparatinės įrangos delegatai**: Naudokite specialius aparatinės įrangos delegatus pagreitinimui
- **Mikrokontroleriai**: Diegimas mikrokontroleriuose su TensorFlow Lite Micro
- **Kryžminis palaikymas**: Diegimas Android, iOS ir įterptose Linux sistemose

### Azure IoT Edge
- **Debesijos ir kraštinių hibridas**: Apmokymas debesyje ir spėjimas kraštuose
- **Modulių diegimas**: Diegti AI modelius kaip IoT Edge modulius
- **Įrenginių valdymas**: Nuotolinis kraštinių įrenginių ir modelių atnaujinimų valdymas
- **Telemetrija**: Rinkti veiklos duomenis ir modelių metriką iš kraštinių diegimų

## Pažangios kraštinių AI scenarijai

### Daugiamodelių diegimas
- **Modelių ansambliai**: Diegti kelis modelius, kad pagerintumėte tikslumą arba padidintumėte patikimumą
- **A/B testavimas**: Tuo pačiu metu testuoti skirtingus modelius kraštiniuose įrenginiuose
- **Dinaminis pasirinkimas**: Pasirinkti modelius pagal dabartines įrenginio sąlygas
- **Resursų dalijimasis**: Optimizuokite resursų naudojimą keliuose diegiamuose modeliuose

### Federuotas mokymasis
- **Paskirstytas mokymas**: Mokykite modelius keliuose kraštiniuose įrenginiuose
- **Privatumo išsaugojimas**: Laikykite mokymo duomenis lokaliai, dalindamiesi modelio patobulinimais
- **Bendradarbiaujantis mokymasis**: Leidžia įrenginiams mokytis iš bendrų patirčių
- **Kraštinių ir debesies koordinavimas**: Koordinuokite mokymą tarp kraštinių įrenginių ir debesijos infrastruktūros

### Realaus laiko apdorojimas
- **Srauto apdorojimas**: Apdorokite nuolatinius duomenų srautus kraštiniuose įrenginiuose
- **Mažas vėlinimas spėjimuose**: Optimizuokite minimalų spėjimo vėlinimą
- **Dėjinių apdorojimas**: Efektyviai apdorokite duomenų dėjinius kraštiniuose įrenginiuose
- **Adaptuojamas apdorojimas**: Koreguokite apdorojimą pagal dabartines įrenginio galimybes

## Kraštinių AI plėtros trikčių šalinimas

### Dažnos problemos
- **Atminties apribojimai**: Modelis per didelis tikslo įrenginio atminčiai
- **Spėjimo greitis**: Modelio spėjimas per lėtas realaus laiko reikalavimams
- **Tikslumo prastėjimas**: Optimizavimas nepriimtina forma sumažina modelio tikslumą
- **Aparatinės įrangos suderinamumas**: Modelis nesuderinamas su tikslo aparatine įranga

### Derinimo strategijos
- **Veiklos profiliavimas**: Naudokite AI įrankių rinkinio sekimo funkcijas, kad nustatytumėte kliūtis
- **Resursų stebėjimas**: Stebėkite atminties ir CPU naudojimą kūrimo metu
- **Inkrementinis testavimas**: Testuokite optimizacijas palaipsniui, kad izoliavusite problemas
- **Aparatinės įrangos simuliacija**: Naudokite kūrimo įrankius tikslinės aparatinės įrangos simuliacijai

### Optimizavimo sprendimai
- **Tolesnis kvantizavimas**: Taikykite agresyvesnes kvantizavimo technikas
- **Modelio architektūra**: Apsvarstykite skirtingas modelių architektūras, optimizuotas kraštinėms
- **Išankstinis apdorojimas optimizavimas**: Optimizuokite duomenų išankstinį apdorojimą kraštinių apribojimams
- **Spėjimo optimizavimas**: Naudokite aparatinei įrangai specifinius spėjimo optimizavimus

## Ištekliai ir tolesni žingsniai

### Oficialioji dokumentacija
- [AI įrankių rinkinio kūrėjo dokumentacija](https://aka.ms/AIToolkit/doc)
- [Įdiegimo ir sąrankos vadovas](https://code.visualstudio.com/docs/intelligentapps/overview#_install-and-setup)
- [VS Code Išmaniųjų programų dokumentacija](https://code.visualstudio.com/docs/intelligentapps)
- [Model Context Protocol (MCP) dokumentacija](https://modelcontextprotocol.io/)

### Bendruomenė ir palaikymas
- [AI įrankių rinkinio GitHub saugykla](https://github.com/microsoft/vscode-ai-toolkit)
- [GitHub klausimai ir funkcijų užklausos](https://aka.ms/AIToolkit/feedback)
- [Azure AI Foundry Discord bendruomenė](https://aka.ms/azureaifoundry/discord)
- [VS Code plėtinių turgus](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)

### Techniniai ištekliai
- [ONNX Runtime dokumentacija](https://onnxruntime.ai/)
- [Ollama dokumentacija](https://ollama.ai/)
- [Windows ML dokumentacija](https://docs.microsoft.com/en-us/windows/ai/)
- [Azure AI Foundry dokumentacija](https://learn.microsoft.com/en-us/azure/ai-foundry/)

### Mokymosi keliai
- [Kraštinių AI pagrindai kursas](../Module01/README.md)
- [Mažų kalbos modelių vadovas](../Module02/README.md)
- [Kraštinių diegimo strategijos](../Module03/README.md)
- [Windows kraštinių AI plėtra](./windowdeveloper.md)

### Papildomi ištekliai
- **Saugyklos statistika**: 1.8k+ žvaigždžių, 150+ šakų, 18+ dėstytojų
- **Licencija**: MIT licencija
- **Saugumas**: Taikomos Microsoft saugumo politikos
- **Telemetrija**: Gerbiamos VS Code telemetrijos nustatymai

## Išvada

AI įrankių rinkinys Visual Studio Code yra visapusiška platforma šiuolaikinei AI plėtrai, siūlanti sklandų agentų kūrimo procesą, itin vertingą kraštinių AI programoms. Su plačiu modelių katalogu, palaikančiu tiekėjus tokius kaip Anthropic, OpenAI, GitHub ir Google, kartu su vietiniu ONNX ir Ollama vykdymu, įrankių rinkinys suteikia reikalingą lankstumą įvairiems kraštinių diegimo scenarijams.

Šio rinkinio stiprybė yra integruotas požiūris – nuo modelių atradimo ir eksperimentavimo Playground iki sudėtingo agentų kūrimo su Prompt Builder, įvairesnio vertinimo galimybių ir sklandžios MCP įrankių integracijos. Kraštinių AI kūrėjams tai reiškia greitą AI agentų prototipų kūrimą ir testavimą prieš diegiant kraštuose, su galimybe greitai iteruoti ir optimizuoti išteklius ribojančiose aplinkose.

Pagrindiniai pranašumai kraštinių AI plėtrai apima:
- **Greita eksperimentacija**: Greitai išbandykite modelius ir agentus prieš pereidami prie kraštinių diegimų
- **Daug tiekėjų lankstumas**: Pasiekite modelius iš įvairių šaltinių, kad rastumėte optimalų kraštinių sprendimą
- **Vietinė plėtra**: Testuokite su ONNX ir Ollama neprisijungę ir išlaikydami privatumą
- **Gamybai paruošimas**: Generuokite gamybai tinkamą kodą ir integruokite su išoriniais įrankiais per MCP
- **Išsamus vertinimas**: Naudokite įmontuotas ir pasirinktines metrikas kraštinių AI našumui patikrinti

Kai AI vis labiau juda link kraštinių diegimo scenarijų, AI įrankių rinkinys VS Code suteikia vystymo aplinką ir darbo eigą, reikalingą kuriant, testuojant ir optimizuojant intelektualias programas ribotose išteklių aplinkose. Nesvarbu, ar vystote IoT sprendimus, mobiliąsias AI programas ar įterptus intelektualius sprendimus, įrankių rinkinio platus funkcionalumas ir integruota darbo eiga palaiko visą kraštinių AI plėtros ciklą.

Su nuolatiniu vystymu ir aktyvia bendruomene (1.8k+ GitHub žvaigždžių), AI įrankių rinkinys išlieka AI kūrimo įrankių priekvoje, nuolat tobulėdamas, kad atitiktų šiuolaikinių AI kūrėjų, dirbančių kraštinių diegimo scenarijose, poreikius.

[Kitas Foundry Local](./foundrylocal.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
# 2 skyrius: Mažų kalbos modelių pagrindai

Šis išsamus pagrindinis skyrius suteikia esminę apžvalgą apie mažus kalbos modelius (SLM), apimant teorinius principus, praktines įgyvendinimo strategijas ir sprendimus, paruoštus diegimui gamyboje. Skyrius sukuria kritinę žinių bazę, leidžiančią suprasti šiuolaikines efektyvias dirbtinio intelekto architektūras ir jų strateginį pritaikymą įvairiose skaičiavimo aplinkose.

## Skyriaus struktūra ir progresyvaus mokymosi sistema

### **[1 skyrius: Microsoft Phi modelių šeimos pagrindai](./01.PhiFamily.md)**
Pirmasis skyrius pristato Microsoft revoliucinę Phi modelių šeimą, parodant, kaip kompaktiški, efektyvūs modeliai pasiekia puikius rezultatus, tuo pačiu ženkliai sumažindami skaičiavimo poreikius. Šiame pagrindiniame skyriuje aptariama:

- **Dizaino filosofijos evoliucija**: Išsamus Microsoft Phi šeimos vystymosi nuo Phi-1 iki Phi-4 tyrimas, akcentuojant revoliucinį „vadovėlio kokybės“ mokymo metodą ir mastelio keitimą vykdymo metu
- **Efektyvumo pirmumo architektūra**: Detali parametrų efektyvumo optimizavimo, daugiarūšio integravimo galimybių ir techninės įrangos optimizacijų analizė, apimanti CPU, GPU ir kraštinius įrenginius
- **Specializuotos galimybės**: Išsamus domeno specifinių variantų, tokių kaip Phi-4-mini-reasoning matematinėms užduotims, Phi-4-multimodal vizijos ir kalbos apdorojimui, ir Phi-3-Silica Windows 11 integracijai, aptarimas

Šis skyrius įtvirtina pagrindinį principą, kad modelio efektyvumas ir galimybės gali egzistuoti kartu per inovatyvius mokymo metodus ir architektūros optimizavimą.

### **[2 skyrius: Qwen šeimos pagrindai](./02.QwenFamily.md)**
Antrasis skyrius pereina prie Alibaba išsamios atvirojo kodo strategijos, parodant, kaip skaidrūs, prieinami modeliai gali pasiekti konkurencingus rezultatus, tuo pačiu išlaikant lankstumą diegimui. Pagrindinės temos:

- **Atvirojo kodo pranašumas**: Išsamus Qwen evoliucijos nuo Qwen 1.0 iki Qwen3 tyrimas, akcentuojant masinio masto mokymą (36 trilijonai žetonų) ir daugiakalbės galimybes 119 kalbų
- **Pažangi samprotavimo architektūra**: Detali Qwen3 inovatyvių „mąstymo režimo“ galimybių, ekspertų mišinio įgyvendinimų ir specializuotų variantų kodavimui (Qwen-Coder) ir matematikai (Qwen-Math) analizė
- **Lankstūs diegimo sprendimai**: Išsamus parametrų diapazonų nuo 0,5B iki 235B aptarimas, leidžiantis diegimo scenarijus nuo mobiliųjų įrenginių iki įmonių klasterių

Šis skyrius pabrėžia dirbtinio intelekto technologijos demokratizavimą per atvirojo kodo prieinamumą, tuo pačiu išlaikant konkurencingas našumo charakteristikas.

### **[3 skyrius: Gemma šeimos pagrindai](./03.GemmaFamily.md)**
Trečiasis skyrius nagrinėja Google išsamų požiūrį į atvirojo kodo daugiarūšį dirbtinį intelektą, parodant, kaip mokslinių tyrimų pagrindu vykdomas vystymas gali suteikti prieinamas, tačiau galingas dirbtinio intelekto galimybes. Šiame skyriuje aptariama:

- **Mokslinių tyrimų skatinamos inovacijos**: Išsamus Gemma 3 ir Gemma 3n architektūrų tyrimas, akcentuojant proveržio Per-Layer Embeddings (PLE) technologiją ir optimizavimo strategijas, orientuotas į mobiliuosius įrenginius
- **Daugiarūšis pranašumas**: Detali vizijos ir kalbos integracijos, garso apdorojimo galimybių ir funkcijų iškvietimo funkcijų analizė, leidžianti sukurti visapusiškas dirbtinio intelekto patirtis
- **Mobiliesiems pritaikyta architektūra**: Išsamus Gemma 3n revoliucinio efektyvumo pasiekimų aptarimas, užtikrinantis efektyvų 2B-4B parametrų našumą su atminties poreikiais vos 2-3GB

Šis skyrius parodo, kaip pažangūs moksliniai tyrimai gali būti paversti praktiškais, prieinamais dirbtinio intelekto sprendimais, leidžiančiais kurti naujas programų kategorijas.

### **[4 skyrius: BitNET šeimos pagrindai](./04.BitNETFamily.md)**
Ketvirtasis skyrius pristato Microsoft revoliucinį požiūrį į 1-bitų kvantavimą, kuris atspindi ultraefektyvaus dirbtinio intelekto diegimo ribas. Šiame pažangiame skyriuje aptariama:

- **Revoliucinis kvantavimas**: Išsamus 1,58-bitų kvantavimo naudojant ternarinius svorius {-1, 0, +1} tyrimas, pasiekiant 1,37x iki 6,17x greitėjimą su 55-82% energijos taupymu
- **Optimizuota vykdymo sistema**: Detali bitnet.cpp įgyvendinimo iš [https://github.com/microsoft/BitNet](https://github.com/microsoft/BitNet), specializuotų branduolių ir kryžminės platformos optimizacijų analizė, užtikrinanti precedento neturinčius efektyvumo pasiekimus
- **Tvaraus dirbtinio intelekto lyderystė**: Išsamus aplinkosaugos privalumų, demokratizuotų diegimo galimybių ir naujų taikymo scenarijų aptarimas, kurį leidžia ekstremalus efektyvumas

Šis skyrius parodo, kaip revoliucinės kvantavimo technikos gali dramatiškai pagerinti dirbtinio intelekto efektyvumą, tuo pačiu išlaikant konkurencingą našumą.

### **[5 skyrius: Microsoft Mu modelio pagrindai](./05.mumodel.md)**
Penktasis skyrius nagrinėja Microsoft revoliucinį Mu modelį, sukurtą specialiai diegimui įrenginiuose su Windows. Šiame specializuotame skyriuje aptariama:

- **Įrenginiams pritaikyta architektūra**: Išsamus Microsoft specializuoto modelio, integruoto į Windows 11 įrenginius, tyrimas
- **Sistemos integracija**: Detali Windows 11 gilaus integravimo analizė, parodanti, kaip dirbtinis intelektas gali pagerinti sistemos funkcionalumą per natyvią įgyvendinimą
- **Privatumo išsaugojimo dizainas**: Išsamus neprisijungus veikimo, vietinio apdorojimo ir privatumo pirmumo architektūros aptarimas, kuris saugo vartotojo duomenis įrenginyje

Šis skyrius parodo, kaip specializuoti modeliai gali pagerinti Windows 11 operacinės sistemos funkcionalumą, tuo pačiu išlaikant privatumą ir našumą.

### **[6 skyrius: Phi-Silica pagrindai](./06.phisilica.md)**
Baigiamasis skyrius nagrinėja Microsoft Phi-Silica, ultraefektyvų kalbos modelį, integruotą į Windows 11 Copilot+ kompiuterius su NPU technine įranga. Šiame pažangiame skyriuje aptariama:

- **Išskirtiniai efektyvumo rodikliai**: Išsamus Phi-Silica puikių našumo galimybių tyrimas, užtikrinantis 650 žetonų per sekundę su vos 1,5 vatų energijos suvartojimu
- **NPU optimizacija**: Detali specializuotos architektūros, sukurtos Neural Processing Units Windows 11 Copilot+ kompiuteriuose, analizė
- **Kūrėjų integracija**: Išsamus Windows App SDK integracijos, užklausų inžinerijos technikų ir geriausių praktikų, skirtų Phi-Silica įgyvendinimui Windows 11 programose, aptarimas

Šis skyrius įtvirtina pažangiausią techninės įrangos optimizuotų kalbos modelių diegimą įrenginiuose, parodant, kaip specializuotos modelių architektūros kartu su dedikuota neuronine technine įranga gali užtikrinti išskirtinį dirbtinio intelekto našumą Windows 11 vartotojų įrenginiuose.

## Išsamūs mokymosi rezultatai

Baigus šį pagrindinį skyrių, skaitytojai įgis:

1. **Architektūros supratimą**: Gilų skirtingų SLM dizaino filosofijų supratimą ir jų poveikį diegimo scenarijams
2. **Našumo ir efektyvumo balansą**: Strateginius sprendimų priėmimo gebėjimus, leidžiančius pasirinkti tinkamas modelio architektūras pagal skaičiavimo apribojimus ir našumo reikalavimus
3. **Diegimo lankstumą**: Supratimą apie kompromisus tarp patentuotos optimizacijos (Phi), atvirojo kodo prieinamumo (Qwen), mokslinių tyrimų skatinamos inovacijos (Gemma) ir revoliucinio efektyvumo (BitNET)
4. **Perspektyvą ateičiai**: Įžvalgas apie kylančias tendencijas efektyviose dirbtinio intelekto architektūrose ir jų poveikį naujos kartos diegimo strategijoms

## Praktinis įgyvendinimo dėmesys

Skyrius išlaiko stiprią praktinę orientaciją, pateikdamas:

- **Pilnus kodo pavyzdžius**: Gamybai paruoštus įgyvendinimo pavyzdžius kiekvienai modelių šeimai, įskaitant pritaikymo procedūras, optimizavimo strategijas ir diegimo konfigūracijas
- **Išsamų palyginimą**: Detalius našumo palyginimus tarp skirtingų modelių architektūrų, įskaitant efektyvumo rodiklius, galimybių vertinimus ir naudojimo atvejų optimizavimą
- **Įmonės saugumą**: Gamybos lygio saugumo įgyvendinimus, stebėjimo strategijas ir geriausias praktikas patikimam diegimui
- **Sistemos integraciją**: Praktines gaires integracijai su populiariomis sistemomis, įskaitant Hugging Face Transformers, vLLM, ONNX Runtime ir specializuotus optimizavimo įrankius

## Strateginis technologijų kelias

Skyrius baigiamas perspektyvia analize:

- **Architektūros evoliucija**: Kylančios tendencijos efektyvaus modelio dizaino ir optimizavimo srityje
- **Techninės įrangos integracija**: Pažanga specializuotuose dirbtinio intelekto akseleratoriuose ir jų poveikis diegimo strategijoms
- **Ekosistemos vystymas**: Standartizacijos pastangos ir tarpusavio suderinamumo gerinimas tarp skirtingų modelių šeimų
- **Įmonės pritaikymas**: Strateginiai svarstymai organizaciniam dirbtinio intelekto diegimo planavimui

## Realūs taikymo scenarijai

Kiekviename skyriuje pateikiama išsami praktinių taikymų apžvalga:

- **Mobilieji ir kraštiniai skaičiavimai**: Optimizuotos diegimo strategijos resursų apribotose aplinkose
- **Įmonės taikymas**: Skalabilūs sprendimai verslo analitikai, automatizavimui ir klientų aptarnavimui
- **Švietimo technologijos**: Prieinamas dirbtinis intelektas personalizuotam mokymuisi ir turinio generavimui
- **Globalus diegimas**: Daugiakalbiai ir kultūriškai pritaikyti dirbtinio intelekto taikymai

## Techninės kompetencijos standartai

Skyrius pabrėžia gamybai paruoštą įgyvendinimą per:

- **Optimizavimo meistriškumą**: Pažangias kvantavimo technikas, vykdymo optimizavimą ir resursų valdymą
- **Našumo stebėjimą**: Išsamų metrikų rinkimą, įspėjimo sistemas ir našumo analizę
- **Saugumo įgyvendinimą**: Įmonės lygio saugumo priemones, privatumo apsaugą ir atitikties sistemas
- **Skalavimo planavimą**: Horizontalias ir vertikalias skalavimo strategijas augantiems skaičiavimo poreikiams

Šis pagrindinis skyrius yra būtinas išankstinis žingsnis pažangioms SLM diegimo strategijoms, suteikiantis tiek teorinį supratimą, tiek praktinius gebėjimus, reikalingus sėkmingam įgyvendinimui. Išsamus turinys užtikrina, kad skaitytojai bus gerai pasiruošę priimti informuotus architektūrinius sprendimus ir įgyvendinti tvirtus, efektyvius dirbtinio intelekto sprendimus, atitinkančius jų specifinius organizacinius poreikius, tuo pačiu pasiruošiant būsimam technologiniam vystymuisi.

Skyrius sujungia pažangius dirbtinio intelekto tyrimus su praktinėmis diegimo realijomis, pabrėždamas, kad šiuolaikinės SLM architektūros gali užtikrinti išskirtinį našumą, tuo pačiu išlaikant operacinį efektyvumą, ekonomiškumą ir aplinkos tvarumą.

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Dėl svarbios informacijos rekomenduojama profesionali žmogaus vertimo paslauga. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius naudojant šį vertimą.
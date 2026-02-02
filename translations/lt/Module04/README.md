# 4 skyrius: Modelių formato konvertavimas ir kvantizavimas - skyrius apžvalga

EdgeAI atsiradimas padarė modelių formato konvertavimą ir kvantizavimą esminėmis technologijomis, leidžiančiomis diegti pažangias mašininio mokymosi galimybes ribotų resursų įrenginiuose. Šis išsamus skyrius pateikia pilną vadovą, kaip suprasti, įgyvendinti ir optimizuoti modelius kraštinių įrenginių diegimo scenarijams.

## 📚 Skyriaus struktūra ir mokymosi kelias

Šis skyrius suskirstytas į septynias progresyvias dalis, kiekviena iš jų remiasi ankstesne, kad sukurtų išsamų modelių optimizavimo kraštiniam kompiuteriui supratimą:

---

## [1 dalis: Modelių formato konvertavimo ir kvantizavimo pagrindai](./01.Introduce.md)

### 🎯 Apžvalga
Ši pagrindinė dalis nustato teorinį pagrindą modelių optimizavimui kraštinių kompiuterių aplinkose, apimant kvantizavimo ribas nuo 1 bitų iki 8 bitų tikslumo lygių ir pagrindines formato konvertavimo strategijas.

**Pagrindinės temos:**
- Tikslumo klasifikavimo sistema (itin žemas, žemas, vidutinis tikslumas)
- GGUF ir ONNX formato privalumai ir naudojimo atvejai
- Kvantizavimo nauda operaciniam efektyvumui ir diegimo lankstumui
- Našumo palyginimai ir atminties naudojimo skirtumai

**Mokymosi rezultatai:**
- Suprasti kvantizavimo ribas ir klasifikacijas
- Nustatyti tinkamas formato konvertavimo technikas
- Išmokti pažangias optimizavimo strategijas kraštiniam diegimui

---

## [2 dalis: Llama.cpp įgyvendinimo vadovas](./02.Llamacpp.md)

### 🎯 Apžvalga
Išsamus vadovas, kaip įgyvendinti Llama.cpp, galingą C++ sistemą, leidžiančią efektyviai vykdyti didelių kalbos modelių užklausas su minimaliu nustatymu įvairiose aparatinės įrangos konfigūracijose.

**Pagrindinės temos:**
- Diegimas Windows, macOS ir Linux platformose
- GGUF formato konvertavimas ir įvairūs kvantizavimo lygiai (Q2_K iki Q8_0)
- Aparatinės įrangos pagreitinimas naudojant CUDA, Metal, OpenCL ir Vulkan
- Python integracija ir gamybos diegimo strategijos

**Mokymosi rezultatai:**
- Įvaldyti diegimą įvairiose platformose ir kūrimą iš šaltinio
- Įgyvendinti modelių kvantizavimo ir optimizavimo technikas
- Diegti modelius serverio režimu su REST API integracija

---

## [3 dalis: Microsoft Olive optimizavimo rinkinys](./03.MicrosoftOlive.md)

### 🎯 Apžvalga
Microsoft Olive tyrinėjimas – aparatinės įrangos optimizavimo įrankių rinkinys su daugiau nei 40 integruotų optimizavimo komponentų, skirtas įmonės lygio modelių diegimui įvairiose aparatinės įrangos platformose.

**Pagrindinės temos:**
- Automatinio optimizavimo funkcijos su dinamišku ir statiniu kvantizavimu
- Aparatinės įrangos intelektas CPU, GPU ir NPU diegimui
- Populiarių modelių palaikymas (Llama, Phi, Qwen, Gemma) iš karto
- Įmonės integracija su Azure ML ir gamybos darbo eigomis

**Mokymosi rezultatai:**
- Pasinaudoti automatizuotu optimizavimu įvairioms modelių architektūroms
- Įgyvendinti diegimo strategijas įvairiose platformose
- Sukurti įmonės lygio optimizavimo procesus

---

## [4 dalis: OpenVINO įrankių rinkinys optimizavimui](./04.openvino.md)

### 🎯 Apžvalga
Išsamus Intel OpenVINO įrankių rinkinio tyrinėjimas – atvirojo kodo platforma, skirta diegti efektyvius AI sprendimus debesyje, vietoje ir kraštiniuose įrenginiuose su pažangiomis Neural Network Compression Framework (NNCF) galimybėmis.

**Pagrindinės temos:**
- Diegimas įvairiose platformose su aparatinės įrangos pagreitinimu (CPU, GPU, VPU, AI akceleratoriai)
- Neural Network Compression Framework (NNCF) pažangiam kvantizavimui ir genėjimui
- OpenVINO GenAI didelių kalbos modelių optimizavimui ir diegimui
- Įmonės lygio modelių serverio galimybės ir mastelio diegimo strategijos

**Mokymosi rezultatai:**
- Įvaldyti OpenVINO modelių konvertavimo ir optimizavimo procesus
- Įgyvendinti pažangias kvantizavimo technikas su NNCF
- Diegti optimizuotus modelius įvairiose aparatinės įrangos platformose su Model Server

---

## [5 dalis: Apple MLX sistemos išsamus tyrinėjimas](./05.AppleMLX.md)

### 🎯 Apžvalga
Išsamus Apple MLX tyrinėjimas – revoliucinė sistema, specialiai sukurta efektyviam mašininio mokymosi vykdymui Apple Silicon, akcentuojant didelių kalbos modelių galimybes ir vietinį diegimą.

**Pagrindinės temos:**
- Vieningos atminties architektūros privalumai ir Metal Performance Shaders
- LLaMA, Mistral, Phi-3, Qwen ir Code Llama modelių palaikymas
- LoRA smulkus derinimas efektyviam modelių pritaikymui
- Hugging Face integracija ir kvantizavimo palaikymas (4 bitų ir 8 bitų)

**Mokymosi rezultatai:**
- Įvaldyti Apple Silicon optimizavimą LLM diegimui
- Įgyvendinti smulkaus derinimo ir modelių pritaikymo technikas
- Kurti įmonės AI programas su patobulintomis privatumo funkcijomis

---

## [6 dalis: Edge AI kūrimo darbo eigos sintezė](./06.workflow-synthesis.md)

### 🎯 Apžvalga
Visų optimizavimo sistemų sintezė į vieningas darbo eigas, sprendimų matricas ir geriausias praktikas, skirtas gamybai paruoštam Edge AI diegimui įvairiose platformose ir naudojimo atvejais, įskaitant mobiliuosius, stalinius ir debesų aplinkas.

**Pagrindinės temos:**
- Vieninga darbo eigos architektūra, integruojanti kelias optimizavimo sistemas
- Sistemos pasirinkimo sprendimų medžiai ir našumo kompromisų analizė
- Gamybos pasirengimo patvirtinimas ir išsamios diegimo strategijos
- Ateities užtikrinimo strategijos naujai atsirandančiai aparatinės įrangai ir modelių architektūroms

**Mokymosi rezultatai:**
- Įvaldyti sistemingą sistemos pasirinkimą pagal reikalavimus ir apribojimus
- Įgyvendinti gamybai paruoštas Edge AI darbo eigas su išsamia stebėsena
- Kurti pritaikomas darbo eigas, kurios evoliucionuoja kartu su naujomis technologijomis ir reikalavimais

---

## [7 dalis: Qualcomm QNN optimizavimo rinkinys](./07.QualcommQNN.md)

### 🎯 Apžvalga
Išsamus Qualcomm QNN (Qualcomm Neural Network) tyrinėjimas – vieninga AI užklausų sistema, sukurta pasinaudoti Qualcomm heterogenine kompiuterine architektūra, įskaitant Hexagon NPU, Adreno GPU ir Kryo CPU, siekiant maksimalaus našumo ir energijos efektyvumo mobiliuosiuose ir kraštiniuose įrenginiuose.

**Pagrindinės temos:**
- Heterogeninis kompiuteris su vieninga prieiga prie NPU, GPU ir CPU
- Aparatinės įrangos optimizavimas Snapdragon platformoms su intelektualiu darbo krūvio paskirstymu
- Pažangios kvantizavimo technikos (INT8, INT16, mišrus tikslumas) mobiliajam diegimui
- Energiją taupantis užklausų vykdymas, optimizuotas baterijomis maitinamiems įrenginiams ir realaus laiko programoms

**Mokymosi rezultatai:**
- Įvaldyti Qualcomm aparatinės įrangos pagreitinimą mobiliajam AI diegimui
- Įgyvendinti energiją taupančias optimizavimo strategijas kraštiniam kompiuteriui
- Diegti gamybai paruoštus modelius Qualcomm ekosistemoje su optimaliu našumu

---

## 🎯 Skyriaus mokymosi rezultatai

Baigus šį išsamų skyrių, skaitytojai pasieks:

### **Techninį meistriškumą**
- Gilų kvantizavimo ribų ir praktinių pritaikymų supratimą
- Praktinę patirtį su keliomis optimizavimo sistemomis
- Gamybos diegimo įgūdžius kraštinių kompiuterių aplinkose

### **Strateginį supratimą**
- Aparatinės įrangos optimizavimo pasirinkimo galimybes
- Informuotą sprendimų priėmimą dėl našumo kompromisų
- Įmonės lygio diegimo ir stebėjimo strategijas

### **Našumo palyginimai**

| Sistema | Kvantizavimas | Atminties naudojimas | Greičio padidėjimas | Naudojimo atvejis |
|---------|---------------|----------------------|---------------------|-------------------|
| Llama.cpp | Q4_K_M | ~4GB | 2-3x | Diegimas įvairiose platformose |
| Olive | INT4 | 60-75% sumažinimas | 2-6x | Įmonės darbo eigos |
| OpenVINO | INT8/INT4 | 50-75% sumažinimas | 2-5x | Intel aparatinės įrangos optimizavimas |
| QNN | INT8/INT4 | 50-80% sumažinimas | 5-15x | Qualcomm mobilus/kraštinis |
| MLX | 4-bit | ~4GB | 2-4x | Apple Silicon optimizavimas |

## 🚀 Kiti žingsniai ir pažangios taikymo sritys

Šis skyrius suteikia pilną pagrindą:
- Individualių modelių kūrimui specifinėms sritims
- Tyrimams kraštinio AI optimizavimo srityje
- Komercinių AI programų kūrimui
- Didelio masto įmonės kraštinio AI diegimams

Žinios iš šių septynių dalių siūlo išsamų įrankių rinkinį, skirtą naršyti sparčiai besikeičiančią kraštinio AI modelių optimizavimo ir diegimo aplinką.

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama profesionali žmogaus vertimo paslauga. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius naudojant šį vertimą.
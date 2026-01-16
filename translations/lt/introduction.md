<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "22c6dae04591abc5f0d80f944ed663d5",
  "translation_date": "2025-09-26T10:48:36+00:00",
  "source_file": "introduction.md",
  "language_code": "lt"
}
-->
# Įvadas į Edge AI pradedantiesiems

![Edge AI Įvadas](../../translated_images/lt/cover.eb18d1b9605d754b.png)

Sveiki atvykę į savo kelionę po **Edge dirbtinį intelektą** – revoliucinį požiūrį, kuris perkelia AI galią tiesiai ten, kur kuriami duomenys ir priimami sprendimai. Šis įvadas padės suprasti, kodėl Edge AI yra ateities intelektualaus skaičiavimo kryptis ir kaip galite įvaldyti jo įgyvendinimą.

## Kas yra Edge AI?

Edge AI reiškia esminį pokytį nuo tradicinio debesų pagrindu veikiančio AI apdorojimo prie **vietinio, įrenginyje veikiančio intelekto**. Vietoj duomenų siuntimo į tolimus serverius, Edge AI apdoroja informaciją tiesiogiai kraštiniuose įrenginiuose – išmaniuosiuose telefonuose, IoT jutikliuose, pramoninėje įrangoje, autonominiuose transporto priemonėse ir įterptinėse sistemose.

### Edge AI paradigma

```
Traditional AI:     Device → Cloud → Processing → Response → Device
Edge AI:           Device → Local Processing → Immediate Response
```

Šis paradigmos pokytis pašalina kelionę į debesį, suteikdamas:
- **Momentinius atsakymus** (submilisekundinis vėlavimas)
- **Pagerintą privatumą** (duomenys niekada nepalieka įrenginio)
- **Patikimą veikimą** (veikia be interneto ryšio)
- **Sumažintas išlaidas** (minimalus pralaidumo ir debesų kompiuterijos naudojimas)

## Kodėl Edge AI svarbus dabar

### Tobula inovacijų audra

Trys technologinės tendencijos susijungė, kad Edge AI taptų ne tik įmanomas, bet ir būtinas:

1. **Aparatūros revoliucija**: Modernūs lustai (Apple Silicon, Qualcomm Snapdragon, NVIDIA Jetson) dabar turi AI pagreitį kompaktiškuose, energiją taupančiuose paketuose
2. **Modelių optimizavimas**: Maži kalbos modeliai (SLM), tokie kaip Phi-4, Gemma ir Mistral, pasiekia 80-90% didelių modelių našumo, būdami 10-20% jų dydžio
3. **Realių poreikių augimas**: Pramonės sektoriai reikalauja momentinio, privataus ir patikimo AI, kurio debesų sprendimai negali suteikti

### Kritiniai verslo veiksniai

**Privatumas ir atitiktis**
- Sveikatos apsauga: Pacientų duomenys turi likti vietoje (HIPAA atitiktis)
- Finansai: Operacijų apdorojimas reikalauja duomenų suvereniteto
- Gamyba: Nuosavi procesai turi būti apsaugoti nuo atskleidimo

**Našumo reikalavimai**
- Autonominės transporto priemonės: Gyvybiškai svarbūs sprendimai per milisekundes
- Pramoninė automatizacija: Realaus laiko kokybės kontrolė ir saugumo stebėjimas
- Žaidimai ir AR/VR: Įtraukiančios patirtys reikalauja nulio pastebimo vėlavimo

**Ekonominis efektyvumas**
- Telekomunikacijos: Vietinis milijonų IoT jutiklių duomenų apdorojimas
- Mažmeninė prekyba: Parduotuvės analizė be didelių pralaidumo išlaidų
- Išmanieji miestai: Paskirstytas intelektas per tūkstančius įrenginių

## Pramonės sektoriai, kuriuos transformuoja Edge AI

### 🏭 **Gamyba ir Pramonė 4.0**
- **Prognozuojama priežiūra**: AI modeliai pramoninėje įrangoje numato gedimus prieš jiems įvykstant
- **Kokybės kontrolė**: Realaus laiko defektų aptikimas gamybos linijose
- **Saugumo stebėjimas**: Momentinis pavojų aptikimas ir reagavimas
- **Tiekimo grandinė**: Intelektualus inventoriaus valdymas kiekviename mazge

**Reali įtaka**: Siemens naudoja Edge AI prognozuojamai priežiūrai, sumažindama prastovas 30-50% ir priežiūros išlaidas 25%.

### 🏥 **Sveikatos apsauga ir medicinos prietaisai**
- **Diagnostinis vaizdavimas**: AI pagrindu veikianti rentgeno ir MRT analizė tiesiogiai priežiūros vietoje
- **Pacientų stebėjimas**: Nuolatinis sveikatos vertinimas per nešiojamus prietaisus
- **Chirurginė pagalba**: Realaus laiko vadovavimas procedūrų metu
- **Vaistų kūrimas**: Vietinis molekulinių simuliacijų apdorojimas

**Reali įtaka**: Philips Edge AI sprendimai leidžia radiologams diagnozuoti būkles 40% greičiau, išlaikant 99% tikslumą.

### 🚗 **Autonominės sistemos ir transportas**
- **Savaeigės transporto priemonės**: Momentinis sprendimų priėmimas navigacijai ir saugumui
- **Eismo valdymas**: Intelektualus sankryžų kontrolė ir srauto optimizavimas
- **Transporto priemonių parkų valdymas**: Realaus laiko maršrutų optimizavimas ir transporto priemonių sveikatos stebėjimas
- **Logistika**: Autonominiai sandėlių robotai ir pristatymo sistemos

**Reali įtaka**: Tesla Full Self-Driving sistema vietoje apdoroja jutiklių duomenis, priimdama 40+ sprendimų per sekundę saugiam autonominiam navigavimui.

### 🏙️ **Išmanieji miestai ir infrastruktūra**
- **Viešasis saugumas**: Realaus laiko grėsmių aptikimas ir skubus reagavimas
- **Energijos valdymas**: Išmaniojo tinklo optimizavimas ir atsinaujinančios energijos integracija
- **Aplinkos stebėjimas**: Oro kokybės, triukšmo taršos ir klimato stebėjimas
- **Urbanistinis planavimas**: Eismo srauto analizė ir infrastruktūros optimizavimas

**Reali įtaka**: Singapūro išmaniojo miesto iniciatyva naudoja 100,000+ Edge AI jutiklių eismo valdymui, sumažindama kelionės laiką 25%.

### 📱 **Vartotojų technologijos ir mobilieji įrenginiai**
- **Išmanusis telefonas AI**: Patobulinta fotografija, balso asistentai ir personalizacija
- **Išmanieji namai**: Intelektuali automatizacija ir saugumo sistemos
- **Nešiojami įrenginiai**: Sveikatos stebėjimas ir fizinio aktyvumo optimizavimas
- **Žaidimai**: Realaus laiko grafikos patobulinimas ir žaidimo optimizavimas

**Reali įtaka**: Apple Neural Engine vietoje apdoroja 15.8 trilijonus operacijų per sekundę, suteikdamas tokias funkcijas kaip realaus laiko kalbos vertimas ir kompiuterinė fotografija.

## Maži kalbos modeliai: Edge AI variklis

### Kas yra maži kalbos modeliai (SLM)?

SLM yra **suspaustos, optimizuotos versijos** didelių kalbos modelių, specialiai sukurtos kraštiniam diegimui:

- **Phi-4**: 14B parametrų, optimizuotas logikai ir kodo generavimui
- **Gemma 2B/7B**: Google efektyvūs modeliai įvairioms NLP užduotims
- **Mistral-7B**: Aukštos kokybės modelis su komercijai draugiška licencija
- **Qwen serija**: Alibaba daugiakalbiai modeliai, optimizuoti mobiliesiems įrenginiams

### SLM privalumai

| Galimybė | Dideli kalbos modeliai | Maži kalbos modeliai |
|----------|------------------------|----------------------|
| **Dydis** | 70B-405B parametrų | 1B-14B parametrų |
| **Atmintis** | 40-200GB RAM | 2-16GB RAM |
| **Apdorojimo greitis** | 2-10 sekundžių | 50-500ms |
| **Diegimas** | Aukštos klasės serveriai | Išmanieji telefonai, įterptiniai įrenginiai |
| **Kaina** | $1000s/mėn | Vienkartinė aparatūros kaina |
| **Privatumas** | Duomenys siunčiami į debesį | Apdorojimas lieka vietinis |

### Našumo realybė

Modernūs SLM pasiekia įspūdingus gebėjimus:
- **90% GPT-3.5 našumo** daugelyje užduočių
- **Realaus laiko pokalbių** galimybės
- **Kodo generavimas ir derinimas**
- **Daugiakalbė vertimas**
- **Dokumentų analizė ir santrauka**

## Mokymosi tikslai

Baigę EdgeAI pradedantiesiems kursą, jūs:

### 🎯 **Pagrindinės žinios**
- Suprasite techninius ir verslo veiksnius, skatinančius Edge AI pritaikymą
- Palyginsite kraštinius ir debesų AI architektūras bei jų tinkamus naudojimo atvejus
- Identifikuosite skirtingų SLM šeimų savybes ir galimybes
- Analizuosite aparatūros reikalavimus Edge AI diegimui

### 🛠️ **Techniniai įgūdžiai**
- Diegsite SLM įvairiose platformose (Windows, mobilieji, įterptiniai, debesų-kraštų hibridai)
- Optimizuosite modelius kraštiniams apribojimams naudodami kvantizaciją, genėjimą ir suspaudimą
- Įgyvendinsite paruoštas gamybai Edge AI programas su stebėjimu ir mastelio keitimu
- Kursite daugiaveiksnius sistemas ir funkcijų kvietimo struktūras sudėtingiems darbo procesams

### 🏗️ **Praktinis įgyvendinimas**
- Kursite pokalbių programas su vietiniu modelių perjungimu ir pokalbių valdymu
- Plėtosite RAG (Retrieval-Augmented Generation) sistemas su vietiniu dokumentų apdorojimu
- Kursite modelių maršrutizatorius, kurie protingai pasirenka tarp specializuotų AI modelių
- Projektuosite API struktūras su srautu, sveikatos stebėjimu ir klaidų valdymu

### 🚀 **Gamybos diegimas**
- Sukursite SLMOps procesus modelių versijavimui, testavimui ir diegimui
- Įgyvendinsite saugumo geriausią praktiką Edge AI programoms
- Projektuosite mastelio keičiamas architektūras, subalansuojančias kraštų ir debesų apdorojimą
- Kursite stebėjimo ir priežiūros strategijas gamybos Edge AI sistemoms

## Mokymosi rezultatai

Baigę kursą, jūs būsite pasiruošę:

### **Techninis meistriškumas**
✅ **Diegti paruoštus gamybai Edge AI sprendimus** Windows, mobiliose ir įterptinėse platformose  
✅ **Optimizuoti AI modelius kraštiniams apribojimams**, pasiekiant 75% dydžio sumažinimą su 85% našumo išlaikymu  
✅ **Kurti intelektualias agentų sistemas** su funkcijų kvietimu ir daugiamodelių koordinavimu  
✅ **Projektuoti mastelio keičiamas kraštų-debesų hibridines architektūras** verslo programoms

### **Pramonės pritaikymas**
✅ **Projektuoti gamybos sprendimus** prognozuojamai priežiūrai ir kokybės kontrolei  
✅ **Plėtoti sveikatos apsaugos programas** su privatumo reikalavimus atitinkančiu pacientų duomenų apdorojimu  
✅ **Kurti automobilių sistemas** realaus laiko sprendimų priėmimui ir saugumui  
✅ **Kurti išmaniojo miesto infrastruktūrą** eismo, saugumo ir aplinkos stebėjimui

### **Karjeros pažanga**
✅ **EdgeAI sprendimų architektas**: Projektuoti išsamias Edge AI strategijas  
✅ **ML inžinierius (Edge specializacija)**: Optimizuoti ir diegti modelius kraštinėse aplinkose  
✅ **IoT AI kūrėjas**: Kurti intelektualias IoT sistemas su vietiniu apdorojimu  
✅ **Mobiliojo AI kūrėjas**: Kurti AI pagrindu veikiančias mobilias programas su vietiniu apdorojimu

## Kurso struktūra

Šis kursas seka **progresyvaus meistriškumo metodą**:

### **1 fazė: Pagrindai** (01-02 moduliai)
Sukurkite konceptualų supratimą ir tyrinėkite modelių šeimas

### **2 fazė: Įgyvendinimas** (03-04 moduliai)
Įvaldykite diegimo ir optimizavimo technikas

### **3 fazė: Gamyba** (05-06 moduliai)
Išmokite SLMOps ir pažangias agentų struktūras

### **4 fazė: Specializacija** (07-08 moduliai)
Platformai specifinis įgyvendinimas ir išsamūs pavyzdžiai

## Sėkmės rodikliai

Sekite savo pažangą pagal šiuos konkrečius rezultatus:

- **Portfelio projektai**: 10+ paruoštų gamybai programų, apimančių įvairias pramonės šakas
- **Našumo rodikliai**: Modeliai, veikiantys su <500ms apdorojimo laiku kraštiniuose įrenginiuose
- **Diegimo tikslai**: Programos, veikiančios Windows, mobiliose ir įterptinėse platformose
- **Verslo pasirengimas**: Sprendimai su stebėjimo, mastelio keitimo ir saugumo struktūromis

## Pradžia

Pasiruošę transformuoti savo AI diegimo supratimą? Jūsų kelionė prasideda nuo **[01 modulio: EdgeAI pagrindai](./Module01/README.md)**, kur tyrinėsite techninius pagrindus, kurie daro Edge AI įmanomą, ir nagrinėsite realius pramonės lyderių atvejus.

**Kitas žingsnis**: [📚 01 modulis - EdgeAI pagrindai →](./Module01/README.md)

---

**AI ateitis yra vietinė, momentinė ir privati. Įvaldykite Edge AI, kad kurtumėte naujos kartos intelektualias programas.**

---


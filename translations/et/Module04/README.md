<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e8d157e0a282083a1e1c7bb5dda28646",
  "translation_date": "2025-10-30T15:42:08+00:00",
  "source_file": "Module04/README.md",
  "language_code": "et"
}
-->
# 4. peatükk: Mudeli formaadi konverteerimine ja kvantiseerimine - peatüki ülevaade

EdgeAI esiletõus on muutnud mudeli formaadi konverteerimise ja kvantiseerimise oluliseks tehnoloogiaks, et rakendada keerukaid masinõppe võimalusi piiratud ressurssidega seadmetel. See põhjalik peatükk pakub täielikku juhendit mudelite mõistmiseks, rakendamiseks ja optimeerimiseks serva kasutuselevõtu stsenaariumides.

## 📚 Peatüki struktuur ja õpiteekond

Peatükk on jaotatud seitsmeks järjestikuseks osaks, millest igaüks tugineb eelnevale, et luua terviklik arusaam mudelite optimeerimisest serva arvutuse jaoks:

---

## [1. osa: Mudeli formaadi konverteerimise ja kvantiseerimise alused](./01.Introduce.md)

### 🎯 Ülevaade
See sissejuhatav osa loob teoreetilise raamistiku mudelite optimeerimiseks serva arvutuskeskkondades, hõlmates kvantiseerimise piire 1-bitist kuni 8-bitise täpsuseni ja peamisi formaadi konverteerimise strateegiaid.

**Peamised teemad:**
- Täpsuse klassifikatsiooni raamistik (üliväike, väike, keskmine täpsus)
- GGUF ja ONNX formaadi eelised ja kasutusjuhtumid
- Kvantiseerimise eelised operatiivse efektiivsuse ja paindlikkuse jaoks
- Jõudluse võrdlused ja mälukasutuse analüüs

**Õpitulemused:**
- Mõista kvantiseerimise piire ja klassifikatsioone
- Tuvasta sobivad formaadi konverteerimise tehnikad
- Õpi serva kasutuselevõtu täiustatud optimeerimisstrateegiaid

---

## [2. osa: Llama.cpp rakendamise juhend](./02.Llamacpp.md)

### 🎯 Ülevaade
Põhjalik juhend Llama.cpp rakendamiseks, mis on võimas C++ raamistik, mis võimaldab tõhusat suurte keelemudelite järeldamist minimaalse seadistusega erinevatel riistvarakonfiguratsioonidel.

**Peamised teemad:**
- Paigaldamine Windowsi, macOS-i ja Linuxi platvormidel
- GGUF formaadi konverteerimine ja erinevad kvantiseerimise tasemed (Q2_K kuni Q8_0)
- Riistvarakiirendus CUDA, Metal, OpenCL ja Vulkaniga
- Pythoniga integreerimine ja tootmise kasutuselevõtu strateegiad

**Õpitulemused:**
- Valda platvormidevahelist paigaldamist ja allikast ehitamist
- Rakenda mudeli kvantiseerimise ja optimeerimise tehnikaid
- Kasuta mudeleid serverirežiimis REST API integreerimisega

---

## [3. osa: Microsoft Olive optimeerimiskomplekt](./03.MicrosoftOlive.md)

### 🎯 Ülevaade
Microsoft Olive'i uurimine, riistvarateadlik mudelite optimeerimise tööriistakomplekt, millel on üle 40 sisseehitatud optimeerimiskomponendi, mis on mõeldud ettevõtte tasemel mudelite kasutuselevõtuks erinevatel riistvaraplatvormidel.

**Peamised teemad:**
- Automaatse optimeerimise funktsioonid dünaamilise ja staatilise kvantiseerimisega
- Riistvarateadlik intelligentsus CPU, GPU ja NPU kasutuselevõtuks
- Populaarsete mudelite tugi (Llama, Phi, Qwen, Gemma) otse karbist
- Ettevõtte integreerimine Azure ML-i ja tootmise töövoogudega

**Õpitulemused:**
- Kasuta automaatset optimeerimist erinevate mudeliarhitektuuride jaoks
- Rakenda platvormidevahelisi kasutuselevõtu strateegiaid
- Loo ettevõtte tasemel optimeerimise töövooge

---

## [4. osa: OpenVINO tööriistakomplekti optimeerimine](./04.openvino.md)

### 🎯 Ülevaade
Intel OpenVINO tööriistakomplekti põhjalik uurimine, avatud lähtekoodiga platvorm, mis võimaldab jõuliste AI lahenduste kasutuselevõttu pilves, kohapeal ja serva keskkondades koos täiustatud Neural Network Compression Framework (NNCF) võimalustega.

**Peamised teemad:**
- Platvormidevaheline kasutuselevõtt riistvarakiirendusega (CPU, GPU, VPU, AI kiirendid)
- Neural Network Compression Framework (NNCF) täiustatud kvantiseerimise ja kärpimise jaoks
- OpenVINO GenAI suurte keelemudelite optimeerimiseks ja kasutuselevõtuks
- Ettevõtte tasemel mudeliserveri võimalused ja skaleeritavad kasutuselevõtu strateegiad

**Õpitulemused:**
- Valda OpenVINO mudeli konverteerimise ja optimeerimise töövooge
- Rakenda täiustatud kvantiseerimise tehnikaid NNCF-iga
- Kasuta optimeeritud mudeleid erinevatel riistvaraplatvormidel mudeliserveriga

---

## [5. osa: Apple MLX raamistik põhjalikult](./05.AppleMLX.md)

### 🎯 Ülevaade
Apple MLX-i põhjalik käsitlus, revolutsiooniline raamistik, mis on spetsiaalselt loodud tõhusaks masinõppeks Apple Siliconil, keskendudes suurte keelemudelite võimalustele ja kohalikule kasutuselevõtule.

**Peamised teemad:**
- Ühtse mäluarhitektuuri eelised ja Metal Performance Shaders
- Tugi LLaMA, Mistral, Phi-3, Qwen ja Code Llama mudelitele
- LoRA peenhäälestus tõhusaks mudeli kohandamiseks
- Hugging Face integratsioon ja kvantiseerimise tugi (4-bitine ja 8-bitine)

**Õpitulemused:**
- Valda Apple Siliconi optimeerimist LLM-i kasutuselevõtuks
- Rakenda peenhäälestuse ja mudeli kohandamise tehnikaid
- Loo ettevõtte AI rakendusi täiustatud privaatsusfunktsioonidega

---

## [6. osa: Edge AI arendustöövoo süntees](./06.workflow-synthesis.md)

### 🎯 Ülevaade
Kõigi optimeerimisraamistike põhjalik süntees ühtseteks töövoogudeks, otsustusmaatriksiteks ja parimateks praktikateks tootmisvalmis Edge AI kasutuselevõtuks erinevatel platvormidel ja kasutusjuhtudel, sealhulgas mobiil-, lauaarvuti- ja pilvekeskkondades.

**Peamised teemad:**
- Ühtne töövoo arhitektuur, mis integreerib mitmeid optimeerimisraamistikke
- Raamistiku valiku otsustuspuud ja jõudluse kompromisside analüüs
- Tootmisvalmiduse valideerimine ja põhjalikud kasutuselevõtu strateegiad
- Tulevikukindlad strateegiad uute riistvara ja mudeliarhitektuuride jaoks

**Õpitulemused:**
- Valda süsteemset raamistiku valikut vastavalt nõuetele ja piirangutele
- Rakenda tootmisvalmis Edge AI töövooge koos põhjaliku jälgimisega
- Kujunda kohandatavaid töövooge, mis arenevad koos uute tehnoloogiate ja nõuetega

---

## [7. osa: Qualcomm QNN optimeerimiskomplekt](./07.QualcommQNN.md)

### 🎯 Ülevaade
Qualcomm QNN (Qualcomm Neural Network) põhjalik uurimine, ühtne AI järeldusraamistik, mis on loodud Qualcommi heterogeense arvutusarhitektuuri, sealhulgas Hexagon NPU, Adreno GPU ja Kryo CPU, maksimaalse jõudluse ja energiatõhususe kasutamiseks mobiil- ja servaseadmetel.

**Peamised teemad:**
- Heterogeenne arvutus ühtse juurdepääsuga NPU-le, GPU-le ja CPU-le
- Riistvarateadlik optimeerimine Snapdragon platvormide jaoks intelligentse töökoormuse jaotusega
- Täiustatud kvantiseerimise tehnikad (INT8, INT16, segatäpsus) mobiilkasutuseks
- Energiatõhus järeldus optimeeritud akutoitega seadmete ja reaalajas rakenduste jaoks

**Õpitulemused:**
- Valda Qualcommi riistvarakiirendust mobiilse AI kasutuselevõtuks
- Rakenda energiatõhusaid optimeerimisstrateegiaid serva arvutuseks
- Kasuta tootmisvalmis mudeleid Qualcommi ökosüsteemis optimaalse jõudlusega

---

## 🎯 Peatüki õpitulemused

Selle põhjaliku peatüki läbimisel saavutavad lugejad:

### **Tehniline meisterlikkus**
- Sügav arusaam kvantiseerimise piiridest ja praktilistest rakendustest
- Käed-külge kogemus mitme optimeerimisraamistikuga
- Tootmise kasutuselevõtu oskused serva arvutuskeskkondades

### **Strateegiline arusaam**
- Riistvarateadlik optimeerimise valiku võimekus
- Informeeritud otsuste tegemine jõudluse kompromisside osas
- Ettevõtte tasemel kasutuselevõtu ja jälgimise strateegiad

### **Jõudluse võrdlused**

| Raamistik | Kvantiseerimine | Mälukasutus | Kiiruse paranemine | Kasutusjuhtum |
|-----------|-----------------|-------------|--------------------|---------------|
| Llama.cpp | Q4_K_M | ~4GB | 2-3x | Platvormidevaheline kasutuselevõtt |
| Olive | INT4 | 60-75% vähendamine | 2-6x | Ettevõtte töövood |
| OpenVINO | INT8/INT4 | 50-75% vähendamine | 2-5x | Inteli riistvara optimeerimine |
| QNN | INT8/INT4 | 50-80% vähendamine | 5-15x | Qualcomm mobiil/serv |
| MLX | 4-bitine | ~4GB | 2-4x | Apple Silicon optimeerimine |

## 🚀 Järgmised sammud ja täiustatud rakendused

See peatükk pakub täielikku alust:
- Kohandatud mudelite arendamiseks spetsiifilistele valdkondadele
- Serva AI optimeerimise uurimiseks
- Kommertslike AI rakenduste arendamiseks
- Suuremahuliste ettevõtte serva AI kasutuselevõtuks

Nende seitsme osa teadmised pakuvad terviklikku tööriistakomplekti, et navigeerida kiiresti arenevas serva AI mudelite optimeerimise ja kasutuselevõtu maastikus.

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.
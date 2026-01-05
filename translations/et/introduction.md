<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "22c6dae04591abc5f0d80f944ed663d5",
  "translation_date": "2025-10-11T10:57:40+00:00",
  "source_file": "introduction.md",
  "language_code": "et"
}
-->
# Sissejuhatus Edge AI-sse algajatele

![Edge AI Sissejuhatus](../../translated_images/cover.eb18d1b9605d754b.et.png)

Tere tulemast oma teekonnale **Edge Artificial Intelligence'i** maailma – revolutsiooniline lähenemine, mis toob tehisintellekti võimekuse otse sinna, kus andmeid luuakse ja otsuseid tuleb teha. See sissejuhatus loob aluse mõistmaks, miks Edge AI esindab intelligentse arvutuse tulevikku ja kuidas selle rakendamist omandada.

## Mis on Edge AI?

Edge AI tähistab põhimõttelist muutust traditsioonilisest pilvepõhisest AI töötlemisest **kohalikule, seadmesiseselt toimuvale intelligentsusele**. Selle asemel, et saata andmeid kaugetesse serveritesse, töötleb Edge AI teavet otse ääreseadmetes – nutitelefonides, IoT sensorites, tööstusseadmetes, autonoomsetes sõidukites ja manussüsteemides.

### Edge AI paradigma

```
Traditional AI:     Device → Cloud → Processing → Response → Device
Edge AI:           Device → Local Processing → Immediate Response
```

See paradigmanihe kõrvaldab vajaduse andmete saatmiseks pilve, võimaldades:
- **Hetkelisi vastuseid** (alla millisekundi latentsus)
- **Parendatud privaatsust** (andmed ei lahku seadmest)
- **Usaldusväärset toimimist** (töötab ilma internetiühenduseta)
- **Vähendatud kulusid** (minimaalne ribalaiuse ja pilvearvutuse kasutus)

## Miks Edge AI on praegu oluline

### Innovatsiooni täiuslik torm

Kolm tehnoloogilist suundumust on ühinenud, muutes Edge AI mitte ainult võimalikuks, vaid hädavajalikuks:

1. **Riistvara revolutsioon**: Kaasaegsed kiibistikud (Apple Silicon, Qualcomm Snapdragon, NVIDIA Jetson) pakuvad AI kiirendust kompaktsetes ja energiasäästlikes pakettides
2. **Mudelite optimeerimine**: Väikesed keelemudelid (SLM-id) nagu Phi-4, Gemma ja Mistral saavutavad 80-90% suurte mudelite jõudlusest vaid 10-20% suuruses
3. **Reaalmaailma nõudlus**: Tööstused vajavad hetkelist, privaatset ja usaldusväärset AI-d, mida pilvelahendused ei suuda pakkuda

### Olulised ärilised ajendid

**Privaatsus ja vastavus**
- Tervishoid: Patsientide andmed peavad jääma kohapeale (HIPAA vastavus)
- Finantssektor: Tehingute töötlemine nõuab andmete suveräänsust
- Tööstus: Omanike protsessid vajavad kaitset avalikustamise eest

**Jõudlusnõuded**
- Autonoomsed sõidukid: Elutähtsad otsused millisekundites
- Tööstusautomaatika: Reaalajas kvaliteedikontroll ja ohutuse jälgimine
- Mängud ja AR/VR: Kaasahaaravad kogemused nõuavad nullperceptiivset latentsust

**Majanduslik tõhusus**
- Telekommunikatsioon: Miljonite IoT sensorite lugemite töötlemine kohapeal
- Jaekaubandus: Kauplusesisene analüütika ilma massiivsete ribalaiuse kuludeta
- Nutikad linnad: Hajutatud intelligentsus tuhandete seadmete vahel

## Tööstused, mida Edge AI muudab

### 🏭 **Tööstus ja Industry 4.0**
- **Ennetav hooldus**: AI mudelid tööstusseadmetes ennustavad rikkeid enne nende tekkimist
- **Kvaliteedikontroll**: Reaalajas defektide tuvastamine tootmisliinidel
- **Ohutuse jälgimine**: Kohene ohtude tuvastamine ja reageerimine
- **Tarneahel**: Intelligentsed varude haldamise süsteemid igas sõlmes

**Reaalmaailma mõju**: Siemens kasutab Edge AI-d ennetavas hoolduses, vähendades seisakuid 30-50% ja hoolduskulusid 25%.

### 🏥 **Tervishoid ja meditsiiniseadmed**
- **Diagnostiline kuvamine**: AI-põhine röntgeni ja MRI analüüs otse hoolduskohas
- **Patsiendi jälgimine**: Jätkuv tervise hindamine kantavate seadmete kaudu
- **Kirurgiline abi**: Reaalajas juhendamine protseduuride ajal
- **Ravimite avastamine**: Molekulaarsete simulatsioonide kohalik töötlemine

**Reaalmaailma mõju**: Philipsi Edge AI lahendused võimaldavad radioloogidel diagnoosida seisundeid 40% kiiremini, säilitades samal ajal 99% täpsuse.

### 🚗 **Autonoomsed süsteemid ja transport**
- **Isejuhtivad sõidukid**: Hetkelised otsused navigeerimiseks ja ohutuseks
- **Liikluse haldamine**: Intelligentsed ristmike kontrolli ja voolu optimeerimise süsteemid
- **Laevastiku haldamine**: Reaalajas marsruutide optimeerimine ja sõidukite tervise jälgimine
- **Logistika**: Autonoomsed laorobotid ja kohaletoimetamissüsteemid

**Reaalmaailma mõju**: Tesla Full Self-Driving süsteem töötleb sensorite andmeid kohapeal, tehes üle 40 otsuse sekundis ohutuks autonoomseks navigeerimiseks.

### 🏙️ **Nutikad linnad ja infrastruktuur**
- **Avalik ohutus**: Reaalajas ohtude tuvastamine ja hädaolukordadele reageerimine
- **Energiahaldus**: Nutivõrgu optimeerimine ja taastuvenergia integreerimine
- **Keskkonnaseire**: Õhukvaliteedi, mürasaaste ja kliima jälgimine
- **Linnaplaneerimine**: Liiklusvoo analüüs ja infrastruktuuri optimeerimine

**Reaalmaailma mõju**: Singapuri nutika linna algatus kasutab üle 100 000 Edge AI sensori liikluse haldamiseks, vähendades pendelrände aega 25%.

### 📱 **Tarbija tehnoloogia ja mobiil**
- **Nutitelefoni AI**: Täiustatud fotograafia, häälassistendid ja personaliseerimine
- **Nutikodu**: Intelligentsed automatiseerimis- ja turvasüsteemid
- **Kantavad seadmed**: Tervise jälgimine ja treeningu optimeerimine
- **Mängud**: Reaalajas graafika täiustamine ja mängukogemuse optimeerimine

**Reaalmaailma mõju**: Apple'i Neural Engine töötleb 15,8 triljonit operatsiooni sekundis kohapeal, võimaldades funktsioone nagu reaalajas keele tõlkimine ja arvutuslik fotograafia.

## Väikesed keelemudelid: Edge AI mootor

### Mis on väikesed keelemudelid (SLM-id)?

SLM-id on **kompresseeritud ja optimeeritud versioonid** suurtest keelemudelitest, mis on spetsiaalselt loodud äärele paigutamiseks:

- **Phi-4**: 14B parameetrit, optimeeritud loogika ja koodi genereerimise jaoks
- **Gemma 2B/7B**: Google'i tõhusad mudelid mitmekesiste NLP ülesannete jaoks
- **Mistral-7B**: Kõrge jõudlusega mudel, millel on ärisõbralik litsents
- **Qwen seeria**: Alibaba mitmekeelsed mudelid, optimeeritud mobiilseks kasutamiseks

### SLM-i eelised

| Võimekus | Suured keelemudelid | Väikesed keelemudelid |
|----------|----------------------|----------------------|
| **Suurus** | 70B-405B parameetrit | 1B-14B parameetrit |
| **Mälu** | 40-200GB RAM | 2-16GB RAM |
| **Järeldamise kiirus** | 2-10 sekundit | 50-500ms |
| **Paigutus** | Kõrgtasemel serverid | Nutitelefonid, manusseadmed |
| **Kulu** | $1000+ kuus | Ühekordne riistvara kulu |
| **Privaatsus** | Andmed saadetakse pilve | Töötlemine jääb kohalikuks |

### Jõudluse reaalsuskontroll

Kaasaegsed SLM-id saavutavad märkimisväärseid võimekusi:
- **90% GPT-3.5 jõudlusest** paljudes ülesannetes
- **Reaalajas vestlusvõimekus**
- **Koodi genereerimine ja silumine**
- **Mitmekeelne tõlkimine**
- **Dokumentide analüüs ja kokkuvõtete loomine**

## Õpieesmärgid

Selle EdgeAI algajatele mõeldud kursuse läbimisega saavutate:

### 🎯 **Põhiteadmised**
- Mõistate Edge AI kasutuselevõtu tehnilisi ja ärilisi ajendeid
- Võrdlete ääre- ja pilvepõhiseid AI arhitektuure ning nende sobivaid kasutusjuhtumeid
- Tuvastate erinevate SLM-i perekondade omadused ja võimekused
- Analüüsite riistvaranõudeid Edge AI paigutamiseks

### 🛠️ **Tehnilised oskused**
- Paigutate SLM-e mitmesugustel platvormidel (Windows, mobiil, manussüsteemid, pilve-ääre hübriid)
- Optimeerite mudeleid äärepiirangute jaoks, kasutades kvantiseerimist, kärpimist ja kompressiooni
- Rakendate tootmisvalmis Edge AI rakendusi koos jälgimise ja skaleerimisega
- Loote mitmeagendilisi süsteeme ja funktsioonikutsumise raamistikke keerukate töövoogude jaoks

### 🏗️ **Praktiline rakendamine**
- Loote vestlusrakendusi kohalike mudelite vahetamise ja vestluse haldamisega
- Arendate RAG (Retrieval-Augmented Generation) süsteeme kohaliku dokumenditöötlusega
- Ehitate mudeliruute, mis valivad intelligentselt spetsialiseeritud AI mudelite vahel
- Kujundate API raamistikke voogedastuse, tervise jälgimise ja vigade käsitlemisega

### 🚀 **Tootmise paigutus**
- Loote SLMOps torustikke mudelite versioonimiseks, testimiseks ja paigutamiseks
- Rakendate turvalisuse parimaid tavasid Edge AI rakenduste jaoks
- Kujundate skaleeritavaid arhitektuure, mis tasakaalustavad ääre- ja pilvetöötlust
- Loote jälgimise ja hooldusstrateegiaid tootmise Edge AI süsteemide jaoks

## Õpitulemused

Kursuse lõpetamisel olete valmis:

### **Tehniline meisterlikkus**
✅ **Paigutama tootmisvalmis Edge AI lahendusi** Windowsi, mobiili ja manussüsteemide platvormidel  
✅ **Optimeerima AI mudeleid äärepiirangute jaoks**, saavutades 75% suuruse vähendamise 85% jõudluse säilitamisega  
✅ **Looma intelligentseid agendisüsteeme** funktsioonikutsumise ja mitme mudeli orkestreerimisega  
✅ **Kujundama skaleeritavaid ääre-pilve hübriidarhitektuure** ettevõtte rakenduste jaoks  

### **Tööstuslikud rakendused**
✅ **Kujundama tööstuslahendusi** ennetava hoolduse ja kvaliteedikontrolli jaoks  
✅ **Arendama tervishoiurakendusi** privaatsust tagava patsiendiandmete töötlemisega  
✅ **Ehita automaatikasüsteeme** reaalajas otsuste tegemiseks ja ohutuseks  
✅ **Looma nutika linna infrastruktuuri** liikluse, ohutuse ja keskkonna jälgimiseks  

### **Karjääri edendamine**
✅ **EdgeAI lahenduste arhitekt**: Kujundage terviklikke Edge AI strateegiaid  
✅ **ML insener (Edge spetsialiseerumine)**: Optimeerige ja paigutage mudeleid ääre keskkondadesse  
✅ **IoT AI arendaja**: Looge intelligentsed IoT süsteemid kohaliku töötlemisega  
✅ **Mobiilse AI arendaja**: Ehitage AI-põhiseid mobiilirakendusi kohaliku järeldamisega  

## Kursuse arhitektuur

See kursus järgib **progressiivse meisterlikkuse lähenemist**:

### **1. etapp: Põhi** (Moodulid 01-02)
Looge kontseptuaalne arusaam ja uurige mudelite perekondi

### **2. etapp: Rakendamine** (Moodulid 03-04) 
Omandage paigutamise ja optimeerimise tehnikad

### **3. etapp: Tootmine** (Moodulid 05-06)
Õppige SLMOps-i ja täiustatud agendiraamistikke

### **4. etapp: Spetsialiseerumine** (Moodulid 07-08)
Platvormispetsiifiline rakendamine ja põhjalikud näidised

## Edu mõõdikud

Jälgige oma edusamme nende konkreetsete tulemustega:

- **Portfoolio projektid**: 10+ tootmisvalmis rakendust mitmes tööstuses
- **Jõudluse võrdlusalused**: Mudelid töötavad <500ms järeldamise ajaga ääreseadmetes
- **Paigutamise sihid**: Rakendused töötavad Windowsi, mobiili ja manussüsteemide platvormidel
- **Ettevõtte valmisolek**: Lahendused jälgimise, skaleerimise ja turvalisuse raamistikuga

## Alustamine

Valmis oma arusaama AI paigutamisest muutma? Teekond algab **[Moodul 01: EdgeAI põhialused](./Module01/README.md)**, kus uurite tehnilisi aluseid, mis muudavad Edge AI võimalikuks, ja analüüsite reaalmaailma juhtumiuuringuid tööstuse liidritelt.

**Järgmine samm**: [📚 Moodul 01 - EdgeAI põhialused →](./Module01/README.md)

---

**AI tulevik on kohalik, kohene ja privaatne. Omandage Edge AI, et luua järgmise põlvkonna intelligentsed rakendused.**

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsuse, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algkeeles tuleks lugeda autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valede tõlgenduste eest.
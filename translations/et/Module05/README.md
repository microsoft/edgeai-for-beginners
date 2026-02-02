# Peatükk 05: SLMOps - Põhjalik juhend väikeste keelemudelite haldamiseks

## Ülevaade

SLMOps (Small Language Model Operations) esindab revolutsioonilist lähenemist tehisintellekti juurutamisele, mis keskendub efektiivsusele, kulutõhususele ja servapõhistele arvutusvõimalustele. See põhjalik juhend hõlmab SLM-i haldamise kogu elutsüklit, alates põhimõistete mõistmisest kuni tootmiskõlblike juurutuste rakendamiseni.

---

## [Jaotis 1: Sissejuhatus SLMOps-i](./01.IntroduceSLMOps.md)

**Tehisintellekti haldamise revolutsioon servas**

See sissejuhatav peatükk tutvustab paradigmat, mis viib traditsioonilised suuremahulised tehisintellekti haldamise protsessid üle väikeste keelemudelite haldamisele (SLMOps). Saate teada, kuidas SLMOps lahendab AI juurutamise kriitilisi väljakutseid, säilitades samal ajal kulutõhususe ja privaatsuse nõuetele vastavuse.

**Mida õpite:**
- SLMOps-i tekkimine ja tähtsus kaasaegses AI strateegias
- Kuidas SLM-id ühendavad jõudluse ja ressursitõhususe
- Põhilised tööpõhimõtted, sealhulgas intelligentne ressursihaldus ja privaatsusele keskenduv arhitektuur
- Reaalsed juurutamise väljakutsed ja nende lahendused
- Strateegiline ärimõju ja konkurentsieelised

**Peamine mõte:** SLMOps demokratiseerib AI juurutamise, muutes arenenud keeleprotsessimise võimalused kättesaadavaks organisatsioonidele, kellel on piiratud tehniline infrastruktuur, võimaldades kiiremaid arendustsükleid ja prognoositavamaid tegevuskulusid.

---

## [Jaotis 2: Mudeli destilleerimine - teooriast praktikani](./02.SLMOps-Distillation.md)

**Efektiivsete mudelite loomine teadmiste ülekande kaudu**

Mudeli destilleerimine on põhitehnika väiksemate ja tõhusamate mudelite loomiseks, mis säilitavad suuremate mudelite jõudluse. See peatükk pakub põhjalikku juhendit destilleerimisprotsesside rakendamiseks, mis edastavad teadmisi suurtest õpetajamudelitest kompaktsetele õpilasmudelitele.

**Mida õpite:**
- Mudeli destilleerimise põhimõtted ja eelised
- Kaheastmeline destilleerimisprotsess: sünteetiliste andmete genereerimine ja õpilasmudeli treenimine
- Praktilised rakendusstrateegiad, kasutades tipptasemel mudeleid nagu DeepSeek V3 ja Phi-4-mini
- Azure ML destilleerimisprotsessid koos praktiliste näidetega
- Parimad tavad hüperparameetrite häälestamiseks ja hindamisstrateegiad
- Reaalsed juhtumiuuringud, mis näitavad märkimisväärset kulu- ja jõudluse paranemist

**Peamine mõte:** Mudeli destilleerimine võimaldab organisatsioonidel saavutada 85% vähenduse järeldusaegades ja 95% mälunõuete vähenemise, säilitades samal ajal 92% algse mudeli täpsusest, muutes arenenud AI võimalused praktiliselt juurutatavaks.

---

## [Jaotis 3: Peenhäälestamine - mudelite kohandamine konkreetseteks ülesanneteks](./03.SLMOps-Finetuing.md)

**Eeltreenitud mudelite kohandamine teie unikaalsetele vajadustele**

Peenhäälestamine muudab üldotstarbelised mudelid spetsialiseeritud lahendusteks, mis on kohandatud teie konkreetsetele kasutusjuhtumitele ja valdkondadele. See peatükk hõlmab kõike alates põhiparameetrite kohandamisest kuni arenenud tehnikateni nagu LoRA ja QLoRA efektiivseks mudeli kohandamiseks.

**Mida õpite:**
- Peenhäälestamise metoodikate ja nende rakenduste põhjalik ülevaade
- Erinevad peenhäälestamise tüübid: täielik peenhäälestamine, parameetrite efektiivne peenhäälestamine (PEFT) ja ülesandespetsiifilised lähenemised
- Praktiline rakendamine, kasutades Microsoft Olive'i koos praktiliste näidetega
- Arenenud tehnikad, sealhulgas mitme adapteri treenimine ja hüperparameetrite optimeerimine
- Parimad tavad andmete ettevalmistamiseks, treeningkonfiguratsiooniks ja ressursihalduseks
- Levinud väljakutsed ja tõestatud lahendused edukate peenhäälestamise projektide jaoks

**Peamine mõte:** Peenhäälestamine tööriistadega nagu Microsoft Olive võimaldab organisatsioonidel tõhusalt kohandada eeltreenitud mudeleid konkreetsetele vajadustele, optimeerides samal ajal jõudlust ja ressursikasutust, muutes tipptasemel AI kättesaadavaks mitmesugustes rakendustes.

---

## [Jaotis 4: Juurutamine - tootmiskõlblike mudelite rakendamine](./04.SLMOps.Deployment.md)

**Peenhäälestatud mudelite viimine tootmisse Foundry Localiga**

Viimane peatükk keskendub kriitilisele juurutamisfaasile, hõlmates mudeli konverteerimist, kvantiseerimist ja tootmiskonfiguratsiooni. Õpite, kuidas juurutada peenhäälestatud kvantiseeritud mudeleid, kasutades Foundry Locali, et saavutada optimaalne jõudlus ja ressursikasutus.

**Mida õpite:**
- Täielik keskkonna seadistamine ja tööriistade paigaldamise protseduurid
- Mudeli konverteerimise ja kvantiseerimise tehnikad erinevate juurutamisskeemide jaoks
- Foundry Locali juurutamiskonfiguratsioon mudelispetsiifiliste optimeerimistega
- Jõudluse võrdlusuuringud ja kvaliteedi valideerimise metoodikad
- Levinud juurutamisprobleemide lahendamine ja optimeerimisstrateegiad
- Tootmise jälgimise ja hoolduse parimad tavad

**Peamine mõte:** Õige juurutamiskonfiguratsioon koos kvantiseerimistehnikatega võib saavutada kuni 75% suuruse vähenemise, säilitades samal ajal vastuvõetava mudeli kvaliteedi, võimaldades tõhusaid tootmisjuurutusi erinevates riistvarakonfiguratsioonides.

---

## Alustamine

See juhend on loodud selleks, et viia teid läbi kogu SLMOps-i teekonna, alates põhimõistete mõistmisest kuni tootmiskõlblike juurutuste rakendamiseni. Iga peatükk tugineb eelnevale, pakkudes nii teoreetilist arusaamist kui ka praktilisi rakendamisoskusi.

Olenemata sellest, kas olete andmeteadlane, kes otsib mudelite juurutamise optimeerimist, DevOps-i insener, kes rakendab AI haldust, või tehniline juht, kes hindab SLMOps-i oma organisatsiooni jaoks, see põhjalik juhend pakub teadmisi ja tööriistu, mis on vajalikud väikeste keelemudelite haldamise edukaks rakendamiseks.

**Valmis alustama?** Alustage 1. peatükist, et mõista SLMOps-i põhimõtteid ja luua alus edasijõudnud rakendustehnikatele, mida käsitletakse järgnevatel peatükkidel.

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.
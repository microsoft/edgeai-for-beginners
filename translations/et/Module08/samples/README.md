# Moodul 08 Näited: Foundry kohalik arendamise juhend

## Ülevaade

See põhjalik kogumik tutvustab nii **Foundry Local SDK** kui ka **Shell Command** lähenemisi tootmiskõlblike AI-rakenduste loomiseks. Iga näide toob esile erinevaid serva-AI arenduse aspekte, alates lihtsast REST-integratsioonist kuni keerukate multi-agent süsteemideni.

## Arenduslähenemine: SDK vs Shell Command

### Kasuta Foundry Local SDK-d, kui:

- **Programmaatiline kontroll**: Vajad täielikku kontrolli agentide elutsükli, hindamise või juurutamise töövoogude üle
- **Kohandatud tööriistad**: Automaatika loomine Foundry Locali ümber (CI/CD integratsioon, multi-agent orkestreerimine)
- **Detailne juurdepääs**: Vajadus agentide metaandmete, versioonide või hindamisjooksu täpse kontrolli järele
- **Python integratsioon**: Töötamine Python-kesksetes keskkondades või Foundry loogika integreerimine laiematesse rakendustesse
- **Ettevõtte töövood**: Modulaarsete töövoogude ja korduvate hindamistorude rakendamine, mis vastavad Microsofti viitearhitektuuridele

### Kasuta Shell Commandi, kui:

- **Kiire testimine**: Kohaliku testimise, agentide käsitsi käivitamise või seadistuse kontrolli läbiviimine
- **CLI lihtsus**: Vajadus lihtsate CLI operatsioonide järele agentide käivitamiseks/seiskamiseks, logide kontrollimiseks või põhiliste hindamiste tegemiseks
- **Kerge automaatika**: Lihtsa automaatika skriptimine ilma täieliku SDK integratsiooni nõudeta
- **Kiired iteratsioonid**: Silumine ja arendustsüklid, eriti piiratud keskkondades või ressursigruppide tasemel juurutustes
- **Seadistamine ja valideerimine**: Esialgne keskkonna konfiguratsioon ja kiire kontroll

## Parimad praktikad ja soovitatav töövoog

Põhineb agentide elutsükli haldamisel, sõltuvuste jälgimisel ja minimaalse privileegiga korduvuse põhimõtetel:

### Faas 1: Alus ja seadistamine
1. **Alusta Shell Commandidega** esialgseks seadistamiseks ja kiireks valideerimiseks
2. **Kontrolli keskkonda** CLI tööriistade ja põhimudeli juurutamise abil
3. **Testi ühenduvust** lihtsate REST-kõnede ja tervisekontrollidega

### Faas 2: Arendus ja integratsioon
1. **Liigu SDK-le** skaleeritavate ja jälgitavate töövoogude jaoks
2. **Rakenda programmaatiline kontroll** keerukate agentide interaktsioonide jaoks
3. **Loo kohandatud tööriistad** kogukonnale valmis mallide ja Azure OpenAI integratsiooni jaoks

### Faas 3: Tootmine ja skaleerimine
1. **Hübriidlähenemine** kombineerides CLI operatsioonide jaoks ja SDK rakendusloogika jaoks
2. **Ettevõtte integratsioon** jälgimise, logimise ja juurutustorude abil
3. **Panusta kogukonda** korduvkasutatavate mallide ja parimate praktikate kaudu

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.
# 2. peatükk: Väikeste keelemudelite alused

See põhjalik sissejuhatav peatükk pakub olulist ülevaadet väikestest keelemudelitest (SLM), hõlmates teoreetilisi põhimõtteid, praktilisi rakendusstrateegiaid ja tootmiskõlblikke juurutuslahendusi. Peatükk loob kriitilise teadmiste baasi, et mõista kaasaegseid tõhusaid tehisintellekti arhitektuure ja nende strateegilist rakendamist erinevates arvutuskeskkondades.

## Peatüki ülesehitus ja järkjärguline õppe raamistik

### **[1. jaotis: Microsofti Phi mudeliperekonna alused](./01.PhiFamily.md)**
Avajaotis tutvustab Microsofti murrangulist Phi mudeliperekonda, näidates, kuidas kompaktsed ja tõhusad mudelid saavutavad märkimisväärseid tulemusi, säilitades samal ajal oluliselt väiksemad arvutusnõuded. See põhjalik jaotis hõlmab:

- **Disainifilosoofia areng**: Microsofti Phi perekonna areng Phi-1-st Phi-4-ni, rõhutades revolutsioonilist "õpiku kvaliteediga" treeningmetoodikat ja järelduste tegemise aja skaleerimist
- **Tõhususele keskenduv arhitektuur**: Parameetrite tõhususe optimeerimise, multimodaalsete integreerimisvõimaluste ja riistvaraspetsiifiliste optimeerimiste üksikasjalik analüüs CPU, GPU ja servaseadmete jaoks
- **Spetsialiseeritud võimekused**: Valdkonnapõhiste variantide, sealhulgas Phi-4-mini-reasoning matemaatiliste ülesannete jaoks, Phi-4-multimodal visuaal-keele töötlemiseks ja Phi-3-Silica Windows 11 sisseehitatud juurutamiseks, põhjalik käsitlus

See jaotis kehtestab põhimõtte, et mudeli tõhusus ja võimekus võivad eksisteerida koos uuenduslike treeningmetoodikate ja arhitektuurilise optimeerimise kaudu.

### **[2. jaotis: Qwen perekonna alused](./02.QwenFamily.md)**
Teine jaotis keskendub Alibaba avatud lähtekoodiga lähenemisele, näidates, kuidas läbipaistvad ja kättesaadavad mudelid võivad saavutada konkurentsivõimelisi tulemusi, säilitades samal ajal paindlikkuse juurutamisel. Peamised teemad hõlmavad:

- **Avatud lähtekoodi tipptase**: Qweni arengutee Qwen 1.0-st Qwen3-ni, rõhutades massiivset mastaapset treenimist (36 triljonit tokenit) ja mitmekeelseid võimekusi 119 keeles
- **Täpsem arutlusarhitektuur**: Qwen3 uuenduslike "mõtlemisrežiimi" võimekuste, ekspertide segu rakenduste ja spetsialiseeritud variantide (Qwen-Coder koodimiseks ja Qwen-Math matemaatikaks) üksikasjalik käsitlus
- **Skaleeritavad juurutusvõimalused**: Parameetrite vahemike põhjalik analüüs alates 0,5B-st kuni 235B-ni, võimaldades juurutusstsenaariume alates mobiilseadmetest kuni ettevõtte klastriteni

See jaotis rõhutab tehisintellekti tehnoloogia demokratiseerimist avatud lähtekoodi kättesaadavuse kaudu, säilitades samal ajal konkurentsivõimelised jõudlusomadused.

### **[3. jaotis: Gemma perekonna alused](./03.GemmaFamily.md)**
Kolmas jaotis uurib Google'i terviklikku lähenemist avatud lähtekoodiga multimodaalsele tehisintellektile, näidates, kuidas teaduspõhine arendus võib pakkuda kättesaadavaid, kuid võimsaid tehisintellekti võimekusi. See jaotis hõlmab:

- **Teaduspõhine innovatsioon**: Gemma 3 ja Gemma 3n arhitektuuride põhjalik käsitlus, sealhulgas läbimurdeline Per-Layer Embeddings (PLE) tehnoloogia ja mobiilile optimeerimise strateegiad
- **Multimodaalne tipptase**: Visuaal-keele integreerimise, helitöötlusvõimekuste ja funktsioonikõnede võimaluste üksikasjalik uurimine, mis võimaldavad terviklikke tehisintellekti kogemusi
- **Mobiilile keskenduv arhitektuur**: Gemma 3n revolutsiooniliste tõhusussaavutuste põhjalik analüüs, pakkudes tõhusat 2B-4B parameetrite jõudlust mälumahuga vaid 2-3GB

See jaotis näitab, kuidas tipptasemel teadusuuringud võivad muutuda praktilisteks ja kättesaadavateks tehisintellekti lahendusteks, mis võimaldavad uusi rakenduskategooriaid.

### **[4. jaotis: BitNET perekonna alused](./04.BitNETFamily.md)**
Neljas jaotis tutvustab Microsofti murrangulist lähenemist 1-bitisele kvantiseerimisele, mis esindab üliefektiivse tehisintellekti juurutamise piiri. See edasijõudnutele mõeldud jaotis hõlmab:

- **Revolutsiooniline kvantiseerimine**: 1,58-bitise kvantiseerimise põhjalik uurimine, kasutades ternaarseid kaale {-1, 0, +1}, saavutades 1,37x kuni 6,17x kiirendusi ja 55-82% energiasäästu
- **Optimeeritud järeldusraamistik**: bitnet.cpp rakenduse üksikasjalik käsitlus [https://github.com/microsoft/BitNet](https://github.com/microsoft/BitNet), spetsialiseeritud tuumad ja platvormidevahelised optimeerimised, mis pakuvad enneolematuid tõhususe eeliseid
- **Jätkusuutlik tehisintellekti juhtimine**: Keskkonnaalaste eeliste, demokratiseeritud juurutusvõimaluste ja uute rakendusstsenaariumide põhjalik analüüs, mida võimaldab äärmuslik tõhusus

See jaotis näitab, kuidas revolutsioonilised kvantiseerimistehnikad võivad dramaatiliselt parandada tehisintellekti tõhusust, säilitades samal ajal konkurentsivõimelise jõudluse.

### **[5. jaotis: Microsoft Mu mudeli alused](./05.mumodel.md)**
Viies jaotis uurib Microsofti murrangulist Mu mudelit, mis on spetsiaalselt loodud seadmesiseseks juurutamiseks Windowsis. See spetsiaalne jaotis hõlmab:

- **Seadmele keskenduv arhitektuur**: Microsofti spetsiaalse Windows 11 seadmetesse sisseehitatud mudeli põhjalik uurimine
- **Süsteemi integreerimine**: Windows 11 sügava integreerimise üksikasjalik analüüs, näidates, kuidas tehisintellekt võib täiustada süsteemi funktsionaalsust tänu loomulikule rakendamisele
- **Privaatsust säilitav disain**: Väljaspool võrku töötamise, kohaliku töötlemise ja privaatsusele keskenduva arhitektuuri põhjalik käsitlus, mis hoiab kasutaja andmed seadmes

See jaotis näitab, kuidas spetsialiseeritud mudelid võivad täiustada Windows 11 operatsioonisüsteemi funktsionaalsust, säilitades samal ajal privaatsuse ja jõudluse.

### **[6. jaotis: Phi-Silica alused](./06.phisilica.md)**
Lõpetav jaotis uurib Microsofti Phi-Silicat, üliefektiivset keelemudelit, mis on sisseehitatud Windows 11 Copilot+ PC-de NPU riistvarasse. See edasijõudnutele mõeldud jaotis hõlmab:

- **Erakordsed tõhususnäitajad**: Phi-Silica märkimisväärsete jõudlusvõimekuste põhjalik analüüs, pakkudes 650 tokenit sekundis vaid 1,5 vati energiatarbimisega
- **NPU optimeerimine**: Spetsiaalse arhitektuuri üksikasjalik uurimine, mis on loodud Windows 11 Copilot+ PC-de närvitöötlusüksuste jaoks
- **Arendajate integreerimine**: Windows App SDK integreerimise, prompt engineering'i tehnikate ja parimate tavade põhjalik käsitlus Phi-Silica rakendamiseks Windows 11 rakendustes

See jaotis kehtestab riistvarale optimeeritud seadmesiseste keelemudelite tipptaseme, näidates, kuidas spetsialiseeritud mudeliarhitektuurid koos pühendatud närvikiirenditega võivad pakkuda erakordset tehisintellekti jõudlust Windows 11 tarbijaseadmetes.

## Põhjalikud õpitulemused

Pärast selle sissejuhatava peatüki läbimist saavutavad lugejad meisterlikkuse:

1. **Arhitektuuri mõistmine**: Erinevate SLM disainifilosoofiate sügav mõistmine ja nende mõju juurutusstsenaariumidele
2. **Jõudluse ja tõhususe tasakaal**: Strateegiline otsustusvõime sobivate mudeliarhitektuuride valimiseks, lähtudes arvutuslikest piirangutest ja jõudlusnõuetest
3. **Juurutamise paindlikkus**: Arusaam kompromissidest, mis kaasnevad omandatud optimeerimise (Phi), avatud lähtekoodi kättesaadavuse (Qwen), teaduspõhise innovatsiooni (Gemma) ja revolutsioonilise tõhususe (BitNET) vahel
4. **Tulevikku vaatav perspektiiv**: Tõhusate tehisintellekti arhitektuuride tekkivate suundumuste ja nende mõju mõistmine järgmise põlvkonna juurutusstrateegiatele

## Praktiline rakendamise fookus

Peatükk säilitab tugeva praktilise suunitluse, sisaldades:

- **Täielikud koodinäited**: Tootmiskõlblikud rakenduse näited iga mudeliperekonna jaoks, sealhulgas peenhäälestusprotseduurid, optimeerimisstrateegiad ja juurutuskonfiguratsioonid
- **Põhjalik võrdlusanalüüs**: Erinevate mudeliarhitektuuride jõudluse võrdlused, sealhulgas tõhususmõõdikud, võimekuse hindamised ja kasutusjuhtumite optimeerimine
- **Ettevõtte turvalisus**: Tootmisklassi turvalisuse rakendused, jälgimisstrateegiad ja parimad tavad usaldusväärseks juurutamiseks
- **Raamistiku integreerimine**: Praktilised juhised integreerimiseks populaarsete raamistikudega, sealhulgas Hugging Face Transformers, vLLM, ONNX Runtime ja spetsialiseeritud optimeerimistööriistad

## Strateegiline tehnoloogiline tegevuskava

Peatükk lõpeb tulevikku suunatud analüüsiga:

- **Arhitektuuri areng**: Tõhusate mudelite disaini ja optimeerimise tekkivad suundumused
- **Riistvara integreerimine**: Edusammud spetsialiseeritud tehisintellekti kiirendites ja nende mõju juurutusstrateegiatele
- **Ökosüsteemi areng**: Standardiseerimise jõupingutused ja koostalitlusvõime parandamine erinevate mudeliperekondade vahel
- **Ettevõtte kasutuselevõtt**: Strateegilised kaalutlused organisatsioonilise tehisintellekti juurutamise planeerimisel

## Reaalse elu rakendusstsenaariumid

Igas jaotises käsitletakse põhjalikult praktilisi rakendusi:

- **Mobiil- ja servaarvutus**: Optimeeritud juurutusstrateegiad ressursipiirangutega keskkondade jaoks
- **Ettevõtte rakendused**: Mastaapsed lahendused äriluure, automatiseerimise ja klienditeeninduse jaoks
- **Haridustehnoloogia**: Kättesaadav tehisintellekt isikupärastatud õppimiseks ja sisuloomeks
- **Globaalne juurutamine**: Mitmekeelsed ja kultuuridevahelised tehisintellekti rakendused

## Tehnilise tipptaseme standardid

Peatükk rõhutab tootmiskõlblikku rakendamist läbi:

- **Optimeerimise meisterlikkus**: Täiustatud kvantiseerimistehnikad, järelduste optimeerimine ja ressursihaldus
- **Jõudluse jälgimine**: Põhjalik mõõdikute kogumine, hoiatussüsteemid ja jõudlusanalüütika
- **Turvalisuse rakendamine**: Ettevõtte tasemel turvameetmed, privaatsuse kaitse ja vastavusraamistikud
- **Mastaapsuse planeerimine**: Horisontaalsed ja vertikaalsed skaleerimisstrateegiad kasvavate arvutusnõuete jaoks

See sissejuhatav peatükk on oluline eeltingimus edasijõudnud SLM-i juurutusstrateegiate jaoks, luues nii teoreetilise arusaama kui ka praktilised oskused, mis on vajalikud edukaks rakendamiseks. Põhjalik käsitlus tagab, et lugejad on hästi varustatud, et teha teadlikke arhitektuurilisi otsuseid ja rakendada tugevaid, tõhusaid tehisintellekti lahendusi, mis vastavad nende konkreetsetele organisatsioonilistele vajadustele, valmistudes samal ajal ette tulevasteks tehnoloogilisteks arenguteks.

Peatükk ühendab tipptasemel tehisintellekti uurimistöö ja praktilise juurutamise reaalsuse, rõhutades, et kaasaegsed SLM-i arhitektuurid võivad pakkuda erakordset jõudlust, säilitades samal ajal töökindluse, kulutõhususe ja keskkonnasäästlikkuse.

---

**Lahtiütlus**:  
See dokument on tõlgitud, kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi püüame tagada täpsust, palun arvestage, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algkeeles tuleks lugeda autoriteetseks allikaks. Olulise teabe puhul on soovitatav kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valede tõlgenduste eest.
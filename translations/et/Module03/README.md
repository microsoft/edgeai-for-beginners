# 3. peatükk: Väikeste keelemudelite (SLM) juurutamine

See põhjalik peatükk käsitleb väikeste keelemudelite (SLM) juurutamise täielikku elutsüklit, hõlmates teoreetilisi aluseid, praktilisi rakendusstrateegiaid ja tootmiskõlblikke konteinerlahendusi. Peatükk on jaotatud kolme järjestikusse sektsiooni, mis viivad lugejaid põhimõistetest keerukamate juurutamisstsenaariumideni.

## Peatüki struktuur ja õppeprotsess

### **[1. sektsioon: SLM täiustatud õppimine - alused ja optimeerimine](./01.SLMAdvancedLearning.md)**
Avasektsioon loob teoreetilise aluse väikeste keelemudelite mõistmiseks ja nende strateegilise tähtsuse mõistmiseks serva-AI juurutustes. Selles sektsioonis käsitletakse:

- **Parameetrite klassifitseerimise raamistik**: SLM kategooriate põhjalik uurimine alates mikro-SLM-idest (100M-1,4B parameetrit) kuni keskmiste SLM-ideni (14B-30B parameetrit), keskendudes mudelitele nagu Phi-4-mini-3.8B, Qwen3 seeria ja Google Gemma3, sealhulgas riistvaranõuded ja mälukasutuse analüüs iga mudelitaseme jaoks
- **Täiustatud optimeerimistehnikad**: Kvantiseerimismeetodite põhjalik käsitlus, kasutades Llama.cpp, Microsoft Olive ja Apple MLX raamistikke, sealhulgas tipptasemel BitNET 1-bit kvantiseerimist koos praktiliste koodinäidetega, mis näitavad kvantiseerimisprotsesse ja võrdlustulemusi
- **Mudelite hankimise strateegiad**: Hugging Face ökosüsteemi ja Azure AI Foundry Model Catalog põhjalik analüüs ettevõtte tasemel SLM juurutamiseks, koos koodinäidetega mudelite programmiliseks allalaadimiseks, valideerimiseks ja formaadi konverteerimiseks
- **Arendaja API-d**: Koodinäited Pythonis, C++-is ja C#-is, mis näitavad, kuidas mudeleid laadida, teha järeldusi ja integreerida populaarsete raamistikudega nagu PyTorch, TensorFlow ja ONNX Runtime

See põhjalik sektsioon rõhutab tasakaalu operatiivse tõhususe, juurutamise paindlikkuse ja kulutõhususe vahel, mis muudab SLM-id ideaalseks serva-arvutuse stsenaariumides, pakkudes praktilisi koodinäiteid, mida arendajad saavad otse oma projektides rakendada.

### **[2. sektsioon: Kohaliku keskkonna juurutamine - privaatsust esikohale seadvad lahendused](./02.DeployingSLMinLocalEnv.md)**
Teine sektsioon liigub teooriast praktilise rakendamise juurde, keskendudes kohalikele juurutusstrateegiatele, mis rõhutavad andmesuveräänsust ja operatiivset sõltumatust. Olulised teemad hõlmavad:

- **Ollama universaalne platvorm**: Platvormidevahelise juurutamise põhjalik uurimine, keskendudes arendajasõbralikele töövoogudele, mudeli elutsükli haldamisele ja kohandamisele Modelfiles abil, sealhulgas täielikud REST API integreerimise näited ja CLI automatiseerimise skriptid
- **Microsoft Foundry Local**: Ettevõtte tasemel juurutuslahendused ONNX-põhise optimeerimise, Windows ML integratsiooni ja ulatuslike turvafunktsioonidega, koos C# ja Python koodinäidetega natiivrakenduste integreerimiseks
- **Võrdlev analüüs**: Raamistike üksikasjalik võrdlus, mis hõlmab tehnilist arhitektuuri, jõudlusomadusi ja kasutusjuhtumite optimeerimise juhiseid, koos võrdluskoodiga, et hinnata järelduste kiirust ja mälukasutust erineval riistvaral
- **API integratsioon**: Näidisrakendused, mis näitavad, kuidas luua veebiteenuseid, vestlusrakendusi ja andmetöötlustorusid, kasutades kohalikke SLM juurutusi, koos koodinäidetega Node.js-is, Python Flask/FastAPI-s ja ASP.NET Core-is
- **Testimisraamistikud**: Automatiseeritud testimisviisid mudeli kvaliteedi tagamiseks, sealhulgas üksuse- ja integratsioonitesti näited SLM-i rakenduste jaoks

See sektsioon pakub praktilisi juhiseid organisatsioonidele, kes soovivad rakendada privaatsust säilitavaid AI lahendusi, säilitades samal ajal täieliku kontrolli oma juurutuskeskkonna üle, pakkudes valmis koodinäiteid, mida arendajad saavad kohandada vastavalt oma konkreetsetele nõuetele.

### **[3. sektsioon: Konteineriseeritud pilvejuurutus - tootmismastaabis lahendused](./03.DeployingSLMinCloud.md)**
Viimane sektsioon keskendub keerukatele konteineriseeritud juurutusstrateegiatele, kasutades Microsofti Phi-4-mini-instruct mudelit peamise juhtumiuuringuna. Selles sektsioonis käsitletakse:

- **vLLM juurutamine**: Kõrge jõudlusega järelduste optimeerimine OpenAI-ühilduvate API-dega, täiustatud GPU kiirendusega ja tootmiskõlbliku konfiguratsiooniga, sealhulgas täielikud Dockerfile'id, Kubernetes manifestid ja jõudluse häälestamise parameetrid
- **Ollama konteinerite orkestreerimine**: Lihtsustatud juurutustöövood Docker Compose abil, mudeli optimeerimise variandid ja veebiliidese integreerimine, koos CI/CD torujuhtme näidetega automatiseeritud juurutamiseks ja testimiseks
- **ONNX Runtime rakendamine**: Serva optimeeritud juurutamine koos põhjalike mudeli konverteerimise, kvantiseerimisstrateegiate ja platvormidevahelise ühilduvusega, sealhulgas üksikasjalikud koodinäited mudeli optimeerimiseks ja juurutamiseks
- **Jälgimine ja nähtavus**: Prometheus/Grafana armatuurlaudade rakendamine kohandatud mõõdikute jaoks SLM-i jõudluse jälgimiseks, sealhulgas häirete konfiguratsioonid ja logide koondamine
- **Koormuse tasakaalustamine ja skaleerimine**: Horisontaalse ja vertikaalse skaleerimise strateegiate praktilised näited koos automaatse skaleerimise konfiguratsioonidega, mis põhinevad CPU/GPU kasutusel ja päringumustritel
- **Turvalisuse tugevdamine**: Konteinerite turvalisuse parimad tavad, sealhulgas privileegide vähendamine, võrgupoliitikad ja API võtmete ning mudeli juurdepääsu volituste haldamine

Iga juurutusmeetod on esitatud koos täielike konfiguratsiooninäidete, testimisprotseduuride, tootmiskõlblikkuse kontrollnimekirjade ja infrastruktuuri-koodina mallidega, mida arendajad saavad otse oma juurutustöövoogudes rakendada.

## Olulised õpitulemused

Peatüki läbimisega omandavad lugejad:

1. **Strateegiline mudelivalik**: Parameetrite piiride mõistmine ja sobivate SLM-ide valimine ressursipiirangute ja jõudlusnõuete alusel
2. **Optimeerimise meisterlikkus**: Täiustatud kvantiseerimistehnikate rakendamine erinevates raamistikudes, et saavutada optimaalne jõudluse ja tõhususe tasakaal
3. **Juurutamise paindlikkus**: Kohalike privaatsusele keskenduvate lahenduste ja skaleeritavate konteineriseeritud juurutuste vahel valimine vastavalt organisatsiooni vajadustele
4. **Tootmiskõlblikkus**: Jälgimis-, turvalisuse- ja skaleerimissüsteemide konfigureerimine ettevõtte tasemel SLM juurutuste jaoks

## Praktiline fookus ja reaalsed rakendused

Peatükk säilitab kogu ulatuses tugeva praktilise orientatsiooni, sisaldades:

- **Käed-külge näited**: Täielikud konfiguratsioonifailid, API testimisprotseduurid ja juurutusskriptid
- **Jõudluse võrdlus**: Üksikasjalikud võrdlused järelduste kiiruse, mälukasutuse ja ressursinõuete osas
- **Turvalisuse kaalutlused**: Ettevõtte tasemel turvalisuse praktikad, vastavusraamistikud ja andmekaitse strateegiad
- **Parimad tavad**: Tootmises tõestatud juhised jälgimise, skaleerimise ja hoolduse jaoks

## Tulevikku suunatud perspektiiv

Peatükk lõpeb tulevikku vaatavate teadmistega, mis hõlmavad:

- Täiustatud mudeliarhitektuurid paremate tõhusussuhetega
- Sügavam riistvara integratsioon spetsialiseeritud AI kiirenditega
- Ökosüsteemi areng standardiseerimise ja koostalitlusvõime suunas
- Ettevõtete kasutuselevõtu mustrid, mida juhivad privaatsus ja vastavusnõuded

See põhjalik lähenemine tagab, et lugejad on hästi ette valmistatud nii praeguste SLM-i juurutamise väljakutsete kui ka tulevaste tehnoloogiliste arengute navigeerimiseks, tehes teadlikke otsuseid, mis vastavad nende konkreetsetele organisatsioonilistele nõuetele ja piirangutele.

Peatükk toimib nii praktilise juhendina koheseks rakendamiseks kui ka strateegilise ressursina pikaajalise AI juurutamise planeerimiseks, rõhutades kriitilist tasakaalu võimekuse, tõhususe ja operatiivse tipptaseme vahel, mis määratleb edukad SLM-i juurutused.

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.
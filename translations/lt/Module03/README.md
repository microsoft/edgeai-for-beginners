# 3 skyrius: Mažų kalbos modelių (SLM) diegimas

Šiame išsamiame skyriuje nagrinėjamas visas mažų kalbos modelių (SLM) diegimo gyvavimo ciklas, apimantis teorinius pagrindus, praktines įgyvendinimo strategijas ir paruoštus gamybai konteinerizuotus sprendimus. Skyrius suskirstytas į tris progresyvius poskyrius, kurie skaitytojus veda nuo pagrindinių sąvokų iki pažangių diegimo scenarijų.

## Skyriaus struktūra ir mokymosi kelionė

### **[1 poskyris: SLM pažangus mokymasis – pagrindai ir optimizavimas](./01.SLMAdvancedLearning.md)**
Pirmasis poskyris nustato teorinius pagrindus, padedančius suprasti mažus kalbos modelius ir jų strateginę svarbą dirbtinio intelekto diegimui kraštiniuose įrenginiuose. Šiame poskyryje aptariama:

- **Parametrų klasifikavimo sistema**: Išsamus SLM kategorijų tyrimas nuo mikro SLM (100M–1,4B parametrų) iki vidutinių SLM (14B–30B parametrų), ypatingą dėmesį skiriant modeliams, tokiems kaip Phi-4-mini-3.8B, Qwen3 serija ir Google Gemma3, įskaitant aparatūros reikalavimus ir atminties naudojimo analizę kiekvienam modelio lygiui
- **Pažangios optimizavimo technikos**: Išsamus kvantizavimo metodų aptarimas naudojant Llama.cpp, Microsoft Olive ir Apple MLX sistemas, įskaitant pažangų BitNET 1-bit kvantizavimą su praktiniais kodų pavyzdžiais, rodančiais kvantizavimo procesus ir našumo rezultatus
- **Modelių įsigijimo strategijos**: Išsamus Hugging Face ekosistemos ir Azure AI Foundry Model Catalog tyrimas, skirtas įmonės lygio SLM diegimui, su kodų pavyzdžiais, kaip programiškai atsisiųsti, patikrinti ir konvertuoti modelius
- **Kūrėjų API**: Kodų pavyzdžiai Python, C++ ir C# kalbomis, rodantys, kaip įkelti modelius, atlikti išvadą ir integruoti su populiariomis sistemomis, tokiomis kaip PyTorch, TensorFlow ir ONNX Runtime

Šis pagrindinis poskyris pabrėžia pusiausvyrą tarp veikimo efektyvumo, diegimo lankstumo ir ekonomiškumo, kuris daro SLM idealiais kraštinio kompiuterio scenarijams, su praktiniais kodų pavyzdžiais, kuriuos kūrėjai gali tiesiogiai pritaikyti savo projektuose.

### **[2 poskyris: Diegimas vietinėje aplinkoje – privatumo pirmumo sprendimai](./02.DeployingSLMinLocalEnv.md)**
Antrasis poskyris pereina nuo teorijos prie praktinio įgyvendinimo, sutelkiant dėmesį į vietinio diegimo strategijas, kurios prioritetą teikia duomenų suverenitetui ir operacinei nepriklausomybei. Pagrindinės temos:

- **Ollama universalus platforma**: Išsamus kryžminės platformos diegimo tyrimas, akcentuojant kūrėjams patogius darbo procesus, modelio gyvavimo ciklo valdymą ir pritaikymą per Modelfiles, įskaitant pilnus REST API integracijos pavyzdžius ir CLI automatizavimo scenarijus
- **Microsoft Foundry Local**: Įmonės lygio diegimo sprendimai su ONNX pagrindu optimizavimu, Windows ML integracija ir išsamiais saugumo funkcijomis, su C# ir Python kodų pavyzdžiais, skirtais natūraliai programų integracijai
- **Lyginamoji analizė**: Išsamus sistemų palyginimas, apimantis techninę architektūrą, našumo charakteristikas ir naudojimo atvejų optimizavimo gaires, su kodų pavyzdžiais, skirtais įvertinti išvados greitį ir atminties naudojimą skirtingoje aparatūroje
- **API integracija**: Pavyzdinės programos, rodančios, kaip kurti interneto paslaugas, pokalbių programas ir duomenų apdorojimo procesus naudojant vietinius SLM diegimus, su kodų pavyzdžiais Node.js, Python Flask/FastAPI ir ASP.NET Core
- **Testavimo sistemos**: Automatiniai testavimo metodai modelio kokybės užtikrinimui, įskaitant vienetinius ir integracinius testų pavyzdžius SLM įgyvendinimams

Šis poskyris suteikia praktines gaires organizacijoms, siekiančioms įgyvendinti privatumo išsaugojimo AI sprendimus, išlaikant visišką kontrolę savo diegimo aplinkoje, su paruoštais naudoti kodų pavyzdžiais, kuriuos kūrėjai gali pritaikyti pagal savo specifinius poreikius.

### **[3 poskyris: Konteinerizuotas diegimas debesyje – gamybos masto sprendimai](./03.DeployingSLMinCloud.md)**
Paskutinis poskyris baigiasi pažangiomis konteinerizuoto diegimo strategijomis, kuriose pagrindinis atvejo tyrimas yra Microsoft Phi-4-mini-instruct. Šiame poskyryje aptariama:

- **vLLM diegimas**: Didelio našumo išvados optimizavimas su OpenAI suderinamais API, pažangia GPU akceleracija ir gamybos masto konfigūracija, įskaitant pilnus Dockerfiles, Kubernetes manifestus ir našumo derinimo parametrus
- **Ollama konteinerių orkestracija**: Supaprastinti diegimo darbo procesai su Docker Compose, modelio optimizavimo variantais ir interneto sąsajos integracija, su CI/CD proceso pavyzdžiais automatizuotam diegimui ir testavimui
- **ONNX Runtime įgyvendinimas**: Kraštui optimizuotas diegimas su išsamia modelio konversija, kvantizavimo strategijomis ir kryžminės platformos suderinamumu, įskaitant detalius kodų pavyzdžius modelio optimizavimui ir diegimui
- **Stebėjimas ir stebimumas**: Prometheus/Grafana prietaisų skydelių įgyvendinimas su individualizuotais metrikais SLM našumo stebėjimui, įskaitant įspėjimų konfigūracijas ir žurnalų agregavimą
- **Krovos balansavimas ir mastelio keitimas**: Praktiniai horizontaliojo ir vertikaliojo mastelio keitimo strategijų pavyzdžiai su automatinio mastelio konfigūracijomis, pagrįstomis CPU/GPU naudojimu ir užklausų modeliais
- **Saugumo stiprinimas**: Konteinerių saugumo geriausios praktikos, įskaitant privilegijų mažinimą, tinklo politiką ir paslapčių valdymą API raktams ir modelio prieigos kredencialams

Kiekvienas diegimo metodas pateikiamas su pilnais konfigūracijos pavyzdžiais, testavimo procedūromis, gamybos pasirengimo kontroliniais sąrašais ir infrastruktūros kaip kodo šablonais, kuriuos kūrėjai gali tiesiogiai pritaikyti savo diegimo darbo procesuose.

## Pagrindiniai mokymosi rezultatai

Baigę šį skyrių, skaitytojai įgis:

1. **Strateginį modelio pasirinkimą**: Supratimą apie parametrų ribas ir tinkamų SLM pasirinkimą pagal išteklių apribojimus ir našumo reikalavimus
2. **Optimizavimo meistriškumą**: Pažangių kvantizavimo technikų įgyvendinimą skirtingose sistemose, siekiant optimalaus našumo ir efektyvumo balanso
3. **Diegimo lankstumą**: Pasirinkimą tarp vietinių privatumo sprendimų ir mastelio konteinerizuotų diegimų pagal organizacinius poreikius
4. **Gamybos pasirengimą**: Stebėjimo, saugumo ir mastelio sistemų konfigūravimą įmonės lygio SLM diegimams

## Praktinis dėmesys ir realaus pasaulio taikymas

Skyrius išlaiko stiprų praktinį orientavimą viso turinio metu, pateikdamas:

- **Praktinius pavyzdžius**: Pilnus konfigūracijos failus, API testavimo procedūras ir diegimo scenarijus
- **Našumo palyginimus**: Išsamias išvados greičio, atminties naudojimo ir išteklių reikalavimų palyginimus
- **Saugumo aspektus**: Įmonės lygio saugumo praktikas, atitikties sistemas ir duomenų apsaugos strategijas
- **Geriausias praktikas**: Gamyboje patikrintas gaires stebėjimui, mastelio keitimui ir priežiūrai

## Ateities perspektyva

Skyrius baigiamas įžvalgomis apie kylančias tendencijas, įskaitant:

- Pažangias modelio architektūras su geresniais efektyvumo rodikliais
- Gilesnę aparatūros integraciją su specializuotais AI akceleratoriais
- Ekosistemos evoliuciją link standartizacijos ir sąveikumo
- Įmonių priėmimo modelius, kuriuos skatina privatumas ir atitikties reikalavimai

Šis išsamus požiūris užtikrina, kad skaitytojai bus gerai pasirengę spręsti tiek dabartinius SLM diegimo iššūkius, tiek būsimus technologinius pokyčius, priimdami informuotus sprendimus, kurie atitinka jų specifinius organizacinius poreikius ir apribojimus.

Skyrius tarnauja kaip praktinis vadovas, skirtas nedelsiant įgyvendinti, ir strateginis šaltinis ilgalaikiam AI diegimo planavimui, pabrėžiant kritinę pusiausvyrą tarp galimybių, efektyvumo ir operacinės kompetencijos, kuri apibrėžia sėkmingus SLM diegimus.

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius dėl šio vertimo naudojimo.
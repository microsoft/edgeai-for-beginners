<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "78ca68df03ae43371b203ea43d346dec",
  "translation_date": "2025-10-30T15:18:47+00:00",
  "source_file": "CHANGELOG.md",
  "language_code": "lt"
}
-->
# Pakeitimų žurnalas

Visi svarbūs EdgeAI for Beginners pakeitimai dokumentuojami čia. Šis projektas naudoja įrašus pagal datas ir Keep a Changelog stilių (Pridėta, Pakeista, Ištaisyta, Pašalinta, Dokumentacija, Perkelta).

## 2025-10-30

### Pridėta - Modulis06 AI agentų išsamus patobulinimas
- **Microsoft Agent Framework integracija** (`Module06/01.IntroduceAgent.md`):
  - Pilnas skyrius apie Microsoft Agent Framework, skirtą gamybai paruoštų agentų kūrimui
  - Išsamūs integracijos modeliai su Foundry Local, skirti diegimui krašte
  - Daugiagentės orkestracijos pavyzdžiai su specializuotais SLM modeliais
  - Įmonės diegimo modeliai su resursų valdymu ir stebėjimu
  - Saugumo ir atitikties funkcijos krašto agentų sistemoms
  - Realūs įgyvendinimo pavyzdžiai (mažmeninė prekyba, sveikatos apsauga, klientų aptarnavimas)

- **SLM agentų diegimo strategijos gamybai**:
  - **Foundry Local**: Pilna dokumentacija apie įmonės lygio krašto AI vykdymo aplinką su diegimu, konfigūracija ir gamybos modeliais
  - **Ollama**: Patobulintas bendruomenės orientuotas diegimas su išsamia stebėsena ir modelių valdymu
  - **VLLM**: Didelio našumo inferencijos variklis su pažangiomis optimizavimo technikomis ir įmonės funkcijomis
  - Gamybos diegimo kontroliniai sąrašai ir palyginimo lentelės visoms trims platformoms

- **Kraštui optimizuotų SLM sistemų patobulinimas**:
  - **ONNX Runtime**: Naujas išsamus skyrius apie kryžminės platformos SLM agentų diegimą
  - Universalūs diegimo modeliai Windows, Linux, macOS, iOS ir Android sistemose
  - Aparatūros pagreitinimo galimybės (CPU, GPU, NPU) su automatiniu aptikimu
  - Gamybai paruoštos funkcijos ir agentams specifinės optimizacijos
  - Pilni įgyvendinimo pavyzdžiai su Microsoft Agent Framework integracija

- **Nuorodos ir papildoma literatūra**:
  - Išsamus šaltinių biblioteka su daugiau nei 100 autoritetingų šaltinių
  - Pagrindiniai moksliniai straipsniai apie AI agentus ir mažus kalbos modelius
  - Oficialios dokumentacijos visoms pagrindinėms sistemoms ir įrankiams
  - Pramonės ataskaitos, rinkos analizė ir techniniai palyginimai
  - Švietimo ištekliai, konferencijos ir bendruomenės forumai
  - Standartai, specifikacijos ir atitikties sistemos

### Pakeista - Modulis06 turinio modernizavimas
- **Patobulinti mokymosi tikslai**: Pridėta Microsoft Agent Framework įvaldymas ir krašto diegimo galimybės
- **Gamybos orientacija**: Perėjimas nuo konceptualaus prie įgyvendinimui paruoštų gairių su gamybos pavyzdžiais
- **Kodo pavyzdžiai**: Atnaujinti visi pavyzdžiai, naudojant modernius SDK modelius ir geriausią praktiką
- **Architektūros modeliai**: Pridėtos hierarchinės agentų architektūros ir krašto-debesies koordinacija
- **Našumo optimizavimas**: Patobulinta resursų valdymo ir automatinio mastelio rekomendacijomis

### Dokumentacija - Modulis06 struktūros patobulinimas
- **Išsamus Agent Framework aprėptis**: Nuo pagrindinių sąvokų iki įmonės diegimo
- **Gamybos diegimo strategijos**: Pilni vadovai Foundry Local, Ollama ir VLLM
- **Kryžminės platformos optimizacija**: Pridėta ONNX Runtime universalus diegimui
- **Išteklių biblioteka**: Platus nuorodų sąrašas tęstiniam mokymuisi ir įgyvendinimui

### Pridėta - Modulis06 Modelio konteksto protokolo (MCP) dokumentacijos atnaujinimas
- **MCP įvado modernizavimas** (`Module06/03.IntroduceMCP.md`):
  - Atnaujinta su naujausiomis MCP specifikacijomis iš modelcontextprotocol.io (2025-06-18 versija)
  - Pridėtas oficialus USB-C analogas, skirtas standartizuotoms AI programų jungtims
  - Atnaujintas architektūros skyrius su oficialiu dviejų sluoksnių dizainu (Duomenų sluoksnis + Transporto sluoksnis)
  - Patobulinta pagrindinių primityvų dokumentacija su serverio primityvais (Įrankiai, Ištekliai, Užklausos) ir kliento primityvais (Atranka, Iškvietimas, Registravimas)

- **Išsamios MCP nuorodos ir ištekliai**:
  - Pridėta **MCP pradedantiesiems** nuoroda (https://aka.ms/mcp-for-beginners)
  - Oficialios MCP dokumentacijos ir specifikacijos (modelcontextprotocol.io)
  - Kūrimo ištekliai, įskaitant MCP Inspector ir pavyzdines įgyvendinimo versijas
  - Techniniai standartai (JSON-RPC 2.0, JSON Schema, OpenAPI, Server-Sent Events)

### Pridėta - Modulis04 Qualcomm QNN integracija
- **Naujas skyrius 7: Qualcomm QNN optimizavimo rinkinys** (`Module04/05.QualcommQNN.md`):
  - Išsamus 400+ eilučių vadovas, apimantis Qualcomm vieningą AI inferencijos sistemą
  - Detali heterogeninio skaičiavimo apžvalga (Hexagon NPU, Adreno GPU, Kryo CPU)
  - Aparatūros sąmoningas optimizavimas Snapdragon platformoms su intelektualiu darbo krūvio paskirstymu
  - Pažangios kvantavimo technikos (INT8, INT16, mišrus tikslumas) mobiliajam diegimui
  - Energiją taupantis inferencijos optimizavimas baterijomis maitinamiems įrenginiams ir realaus laiko programoms
  - Pilnas diegimo vadovas su QNN SDK nustatymu ir aplinkos konfigūracija
  - Praktiniai pavyzdžiai: PyTorch į QNN konversija, daugiaplatforminis optimizavimas, konteksto dvejetainio failo generavimas
  - Pažangūs naudojimo modeliai: individualus backend konfigūravimas, dinaminis kvantavimas, našumo profilavimas
  - Išsamus trikčių šalinimo skyrius ir bendruomenės ištekliai

- **Patobulinta Modulis04 struktūra**:
  - Atnaujintas README.md, įtraukiant 7 progresyvius skyrius (buvo 6)
  - Pridėtas Qualcomm QNN į našumo palyginimo lentelę (5-15x greičio padidėjimas, 50-80% atminties sumažinimas)
  - Išsamūs mokymosi rezultatai mobiliojo AI diegimui ir energijos optimizavimui

### Pakeista - Modulis04 dokumentacijos atnaujinimai
- **Microsoft Olive dokumentacijos patobulinimas** (`Module04/03.MicrosoftOlive.md`):
  - Pridėtas išsamus „Olive Recipes Repository“ skyrius, apimantis daugiau nei 100 iš anksto paruoštų optimizavimo receptų
  - Detali palaikomų modelių šeimų apžvalga (Phi, Llama, Qwen, Gemma, Mistral, DeepSeek)
  - Praktiniai naudojimo pavyzdžiai receptų pritaikymui ir bendruomenės indėliams
  - Patobulinta našumo palyginimais ir integracijos gairėmis

- **Skyrių pergrupavimas Modulis04**:
  - Apple MLX perkeltas į 5 skyrių (buvo 6 skyrius)
  - Darbo eigos sintezė perkelta į 6 skyrių (buvo 7 skyrius)
  - Qualcomm QNN pozicionuotas kaip 7 skyrius (specializuotas mobiliojo/krašto dėmesys)
  - Atnaujintos visos failų nuorodos ir navigacijos nuorodos atitinkamai

### Ištaisyta - Dirbtuvių pavyzdžių validacija
- **chat_bootstrap.py validacija ir taisymas**:
  - Ištaisyta sugadinta importo eilutė (`util.util.workshop_utils` → `util.workshop_utils`)
  - Sukurtas trūkstamas `__init__.py` util pakete, kad Python modulis būtų tinkamai atpažintas
  - Įdiegti reikalingi priklausomybės (openai, foundry-local-sdk) conda aplinkoje
  - Sėkmingai patikrintas pavyzdžių vykdymas su numatytais ir pritaikytais užklausomis
  - Patvirtinta integracija su Foundry Local paslauga ir modelio įkrovimu (phi-4-mini su CUDA optimizacija)

### Dokumentacija - Išsamūs vadovų atnaujinimai
- **Modulis04 README.md pilnas restruktūrizavimas**:
  - Pridėtas Qualcomm QNN kaip pagrindinė optimizavimo sistema kartu su OpenVINO, Olive, MLX
  - Atnaujinti skyriaus mokymosi rezultatai, įtraukiant mobiliojo AI diegimą ir energijos optimizavimą
  - Patobulinta našumo palyginimo lentelė su QNN metrikomis ir mobiliojo/krašto naudojimo atvejais
  - Išlaikyta logiška progresija nuo įmonės sprendimų iki platformos specifinių optimizacijų

- **Kryžminės nuorodos ir navigacija**:
  - Atnaujintos visos vidinės nuorodos ir failų nuorodos naujam skyrių numeravimui
  - Patobulintas darbo eigos sintezės aprašymas, įtraukiant mobiliojo, darbalaukio ir debesų aplinkas
  - Pridėtos išsamios nuorodos į Qualcomm kūrėjų ekosistemą

## 2025-10-08

### Pridėta - Dirbtuvių išsamus atnaujinimas
- **Dirbtuvių README.md pilnas perrašymas**:
  - Pridėtas išsamus įvadas, paaiškinantis Edge AI vertę (privatumas, našumas, kaina)
  - Sukurti 6 pagrindiniai mokymosi tikslai su detalizuotomis kompetencijomis
  - Pridėta mokymosi rezultatų lentelė su pristatymais ir kompetencijų matrica
  - Įtraukta karjerai paruoštų įgūdžių sekcija, skirta pramonės aktualumui
  - Pridėtas greito starto vadovas su reikalavimais ir 3 žingsnių nustatymu
  - Sukurtos išteklių lentelės Python pavyzdžiams (8 failai su vykdymo laikais)
  - Pridėta Jupyter užrašų knygelių lentelė (8 užrašai su sudėtingumo įvertinimais)
  - Sukurta dokumentacijos lentelė (7 pagrindiniai dokumentai su „Naudoti kada“ gairėmis)
  - Pridėtos mokymosi kelio rekomendacijos skirtingiems įgūdžių lygiams

- **Dirbtuvių validacijos ir testavimo infrastruktūra**:
  - Sukurtas `scripts/validate_samples.py` - Išsamus validacijos įrankis sintaksei, importams ir geriausiai praktikai
  - Sukurtas `scripts/test_samples.py` - Greito testavimo vykdyklė visiems Python pavyzdžiams
  - Pridėta validacijos dokumentacija į `scripts/README.md`

- **Išsami dokumentacija**:
  - Sukurtas `SAMPLES_UPDATE_SUMMARY.md` - 400+ eilučių detalus vadovas, apimantis visus patobulinimus
  - Sukurtas `UPDATE_COMPLETE.md` - Atnaujinimo užbaigimo vykdomoji santrauka
  - Sukurtas `QUICK_REFERENCE.md` - Greitos nuorodos kortelė dirbtuvėms

### Pakeista - Dirbtuvių Python pavyzdžių modernizavimas
- **Visi 8 Python pavyzdžiai atnaujinti pagal geriausią praktiką**:
  - Patobulintas klaidų tvarkymas su try-except blokais aplink visus I/O veiksmus
  - Pridėti tipų užuominos ir išsamūs docstring'ai
  - Įgyvendintas nuoseklus [INFO]/[ERROR]/[RESULT] registravimo modelis
  - Apsaugoti pasirenkami importai su diegimo užuominomis
  - Pagerintas naudotojo grįžtamasis ryšys visuose pavyzdžiuose

- **session01/chat_bootstrap.py**:
  - Patobulintas kliento inicializavimas su išsamiais klaidų pranešimais
  - Pagerintas srauto klaidų tvarkymas su fragmentų validacija
  - Pridėtas geresnis išimčių tvarkymas paslaugos nepasiekiamumo atveju

- **session02/rag_pipeline.py**:
  - Pridėti importo apsaugos sentence-transformers su diegimo užuominomis
  - Patobulintas klaidų tvarkymas įterpimo ir generavimo operacijoms
  - Pagerintas išvesties formatavimas su struktūrizuotais rezultatais

- **session02/rag_eval_ragas.py**:
  - Apsaugoti pasirenkami importai (ragas, datasets) su naudotojui draugiškais klaidų pranešimais
  - Pridėtas klaidų tvarkymas vertinimo metrikoms
  - Patobulintas išvesties formatavimas vertinimo rezultatams

- **session03/benchmark_oss_models.py**:
  - Įgyvendintas grakštus degradavimas (tęsia modelio gedimų atveju)
  - Pridėtas detalus progreso pranešimas ir klaidų tvarkymas kiekvienam modeliui
  - Patobulinta statistikos skaičiavimas su išsamiu klaidų atkūrimu

- **session04/model_compare.py**:
  - Pridėtos tipų užuominos (Tuple grąžinimo tipai)
  - Patobulintas išvesties formatavimas su struktūrizuotais JSON rezultatais
  - Įgyvendintas klaidų tvarkymas kiekvienam modeliui su atkūrimu

- **session05/agents_orchestrator.py**:
  - Patobulintas Agent.act() su išsamiais docstring'ais
  - Pridėtas pipeline klaidų tvarkymas su etapų registravimu
  - Pagerintas atminties valdymas ir būsenos sekimas

- **session06/models_router.py**:
  - Patobulinta funkcijų dokumentacija visiems maršrutizavimo komponentams
  - Pridėtas detalus registravimas route() funkcijoje
  - Pagerintas testavimo išvestis su struktūrizuotais rezultatais

- **session06/models_pipeline.py**:
  - Pridėtas klaidų tvarkymas chat() pagalbinėje funkcijoje
  - Patobulintas pipeline() su etapų registravimu ir progreso pranešimais
  - Pagerintas main() su išsamiu klaidų atkūrimu

### Dokumentacija - Dirbtuvių dokumentacijos patobulinimas
- Atnaujintas pagrindinis README.md su Dirbtuvių skyriumi, pabrėžiančiu praktinį mokymosi kelią
- Patobulintas STUDY_GUIDE.md su išsamiu Dirbtuvių skyriumi, įskaitant:
  - Mokymosi tikslus ir studijų fokusavimo sritis
  - Savęs vertinimo klausimus
  - Praktinius pratimus su laiko įvertinimais
  - Laiko paskirstymą koncentruotam ir daliniam mokymuisi
  - Pridėtas Dirbtuvių skyrius pažangos stebėjimo šablone
- Atnaujintas laiko paskirstymo vadovas nuo 20 valandų iki 30 valandų (įskaitant Dirbtuves)
- Pridėtos Dirbtuvių pavyzdžių aprašymai ir mokymosi rezultatai į README

### Ištaisyta
- Išspręstos nenuoseklios klaidų tvarkymo schemos Dirbtuvių pavyzdžiuose
- Ištaisyti pasirenkamų priklausomybių importo klaidos su tinkamais apsaugos mechanizmais
-
  - Paleidžiami pavyzdžiai `Module08/samples/01`–`06` su Windows cmd instrukcijomis
    - `01` REST greitas pokalbis (`chat_quickstart.py`)
    - `02` SDK greitas startas su OpenAI/Foundry Local ir Azure OpenAI palaikymu (`sdk_quickstart.py`)
    - `03` CLI sąrašas ir testavimas (`list_and_bench.cmd`)
    - `04` Chainlit demonstracija (`app.py`)
    - `05` Daugiaveiksmė agentų koordinacija (`python -m samples.05.agents.coordinator`)
    - `06` Modeliai kaip įrankiai maršrutizatorius (`router.py`)
- Azure OpenAI palaikymas 2 sesijos SDK pavyzdyje su aplinkos kintamųjų konfigūracija
- `.vscode/settings.json` nukreipia į `Module08/.venv` ir pagerina Python analizės sprendimą
- `.env` su `PYTHONPATH` užuomina VS Code/Pylance supratimui

### Pakeista
- Numatytasis modelis atnaujintas į `phi-4-mini` visoje Module 08 dokumentacijoje ir pavyzdžiuose; pašalintos likusios `phi-3.5` nuorodos Module 08
- Maršrutizatoriaus (`Module08/samples/06/router.py`) patobulinimai:
  - Galinių taškų aptikimas per `foundry service status` su regex analize
  - `/v1/models` sveikatos patikrinimas paleidimo metu
  - Modelių registras konfigūruojamas aplinkos kintamaisiais (`GENERAL_MODEL`, `REASONING_MODEL`, `CODE_MODEL`, `TOOL_REGISTRY` JSON)
- Reikalavimai atnaujinti: `Module08/requirements.txt` dabar apima `openai` (kartu su `requests`, `chainlit`)
- Chainlit pavyzdžio gairės patikslintos ir pridėta trikčių šalinimo informacija; importų sprendimas per darbo aplinkos nustatymus

### Ištaisyta
- Išspręstos importavimo problemos:
  - Maršrutizatorius nebepriklauso nuo neegzistuojančio `utils` modulio; funkcijos integruotos
  - Koordinatorius naudoja santykinį importą (`from .specialists import ...`) ir paleidžiamas per modulio kelią
  - VS Code/Pylance konfigūracija, kad būtų išspręsti `chainlit` ir paketų importai
- Ištaisyta nedidelė klaida `STUDY_GUIDE.md` ir pridėta Module 08 aprėptis

### Pašalinta
- Ištrintas nenaudojamas `Module08/infra/obs.py` ir pašalintas tuščias `infra/` katalogas; stebėjimo modeliai išlaikyti kaip pasirenkami dokumentacijoje

### Perkelta
- Module 08 demonstracijos sujungtos į `Module08/samples` su sesijos numeriais pažymėtais aplankais
  - Chainlit programa perkelta į `samples/04`
  - Agentai perkelti į `samples/05` ir pridėti `__init__.py` failai paketų sprendimui

### Dokumentacija
- Module 08 sesijos dokumentacija ir visi pavyzdžių README papildyti Microsoft Learn ir patikimų tiekėjų nuorodomis
- `Module08/README.md` atnaujintas su Pavyzdžių apžvalga, maršrutizatoriaus konfigūracija ir patikrinimo patarimais
- `Module07/README.md` Windows Foundry Local skyrius patikrintas pagal Learn dokumentaciją
- `STUDY_GUIDE.md` atnaujintas:
  - Pridėta Module 08 į apžvalgą, tvarkaraščius, progreso sekimo priemonę
  - Pridėta išsami Nuorodų sekcija (Foundry Local, Azure AI, Olive, ONNX Runtime, OpenVINO, MLX, Llama.cpp, vLLM, Ollama, AI Toolkit, Windows ML)

---

## Istorinis (santrauka)
- Kurso architektūra ir moduliai sukurti (Moduliai 01–07)
- Iteratyvus turinio modernizavimas, formatavimo standartizavimas ir pridėti atvejų tyrimai
- Išplėsta optimizavimo sistemų aprėptis (Llama.cpp, Olive, OpenVINO, Apple MLX)

## Neišleista / Laukiama (pasiūlymai)
- Pasirenkami kiekvieno pavyzdžio testai, kad būtų patikrintas Foundry Local prieinamumas
- Peržiūrėti vertimus, kad modelių nuorodos (pvz., `phi-4-mini`) būtų suderintos, kur tinkama
- Pridėti minimalų pyright konfigūraciją, jei komandos pageidauja griežtumo visoje darbo aplinkoje

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Dėl svarbios informacijos rekomenduojama profesionali žmogaus vertimo paslauga. Mes neprisiimame atsakomybės už nesusipratimus ar neteisingus aiškinimus, atsiradusius naudojant šį vertimą.
# Pokyčių žurnalas

Čia dokumentuojami visi reikšmingi „EdgeAI for Beginners“ pokyčiai. Šis projektas naudoja datos pagrindu sudarytus įrašus ir Keep a Changelog stilių (Pridėta, Pakeista, Ištaisyta, Pašalinta, Dokumentacija, Perkelta).

## 2025-10-30

### Pridėta - Module06 AI agentų išsamus patobulinimas
- **Microsoft agentų pagrindo integracija** (`Module06/01.IntroduceAgent.md`):
  - Pilnas skyrius apie Microsoft agentų pagrindą, skirtą gamybai paruoštam agentų kūrimui
  - Išsamūs integracijos modeliai su Foundry Local krašto diegimui
  - Daugiaagentinė orkestracija su specializuotais SLM modeliais pavyzdžiai
  - Įmonių diegimo modeliai su resursų valdymu ir stebėsena
  - Saugumo ir atitikties funkcijos krašto agentų sistemoms
  - Realūs įgyvendinimo pavyzdžiai (mažmeninė prekyba, sveikatos priežiūra, klientų aptarnavimas)

- **Gamybinio SLM agentų diegimo strategijos**:
  - **Foundry Local**: Išsami įmonių klasės krašto AI vykdymo dokumentacija su įdiegimu, konfigūracija ir gamybiniu modeliu
  - **Ollama**: Patobulintas bendruomenei orientuotas diegimas su išsamiu stebėjimu ir modelių valdymu
  - **VLLM**: Aukštos našumo inferencijos variklis su pažangiomis optimizavimo technikomis ir įmonių funkcijomis
  - Gamybinio diegimo kontrolinių sąrašų ir palyginimo lentelių visoms trims platformoms rinkinys

- **Kraštui optimizuotų SLM pagrindų patobulinimai**:
  - **ONNX Runtime**: Naujas išsamus skyrius kryžminės platformos SLM agentų diegimui
  - Universalieji diegimo modeliai Windows, Linux, macOS, iOS ir Android sistemoms
  - Aparatūros pagreitinimo galimybės (CPU, GPU, NPU) su automatinio aptikimo sistema
  - Gamybai paruoštos funkcijos ir agentams skirtos optimizacijos
  - Pilni įgyvendinimo pavyzdžiai su Microsoft agentų pagrindo integracija

- **Nuorodos ir tolesnis skaitymas**:
  - Išsami išteklių biblioteka su daugiau nei 100 autoritetingų šaltinių
  - Pagrindiniai tyrimų darbai apie AI agentus ir mažus kalbos modelius
  - Oficialios dokumentacijos visiems pagrindiniams pagrindams ir įrankiams
  - Pramonės ataskaitos, rinkos analizė ir techniniai etalonai
  - Švietimo ištekliai, konferencijos ir bendruomenių forumai
  - Standartai, specifikacijos ir atitikties pagrindai

### Pakeista - Module06 turinio modernizavimas
- **Patobulinti mokymosi tikslai**: įtrauktas Microsoft agentų pagrindo išmanymas ir krašto diegimo gebėjimai
- **Gamybinis fokusas**: perorientuota nuo konceptualių iki diegimui paruoštų gairių su gamybiniais pavyzdžiais
- **Kodo pavyzdžiai**: atnaujinti visi pavyzdžiai naudojant modernius SDK šablonus ir geriausias praktikas
- **Architektūros modeliai**: pridėtos hierarchinės agentų architektūros ir krašto į debesį koordinavimas
- **Veiklos optimizavimas**: patobulinta su resursų valdymu ir automatinio mastelio keitimo rekomendacijomis

### Dokumentacija - Module06 struktūros patobulinimas
- **Išsami agentų pagrindo apimtis**: nuo pagrindinių konceptų iki įmonių diegimo
- **Gamybinio diegimo strategijos**: pilni vadovai Foundry Local, Ollama ir VLLM
- **Kryžminės platformos optimizavimas**: pridėtas ONNX Runtime universaliam diegimui
- **Išteklių biblioteka**: platus nuorodų rinkinys tęstiniam mokymuisi ir diegimui

### Pridėta - Module06 Modelio konteksto protokolo (MCP) dokumentacijos atnaujinimas
- **MCP įvado modernizavimas** (`Module06/03.IntroduceMCP.md`):
  - Atnaujinta pagal naujausias MCP specifikacijas iš modelcontextprotocol.io (2025-06-18 versija)
  - Pridėta oficiali USB-C analogija standartizuotiems AI programų ryšiams
  - Atnaujintas architektūros skyrius su oficialiu dviaukščiu dizainu (duomenų sluoksnis + transporto sluoksnis)
  - Patobulinta pagrindinių primityvų dokumentacija su serverio primityvais (Įrankiai, Ištekliai, Paskatinimai) ir kliento primityvais (Pavyzdžių ėmimas, Išgavimas, Žurnalas)

- **Išsamios MCP nuorodos ir ištekliai**:
  - Pridėtas **MCP pradedantiesiems** ryšys (https://aka.ms/mcp-for-beginners) 
  - Oficialūs MCP dokumentai ir specifikacijos (modelcontextprotocol.io)
  - Kūrimo ištekliai įskaitant MCP Inspector ir pavyzdinius įgyvendinimus
  - Techniniai standartai (JSON-RPC 2.0, JSON Schema, OpenAPI, Server-Sent Events)


### Pridėta - Module04 Qualcomm QNN integracija
- **Naujas skyrius 7: Qualcomm QNN optimizacijos rinkinys** (`Module04/05.QualcommQNN.md`):
  - Išsamus 400+ eilučių vadovas apie Qualcomm vieningą AI inferencijos pagrindą
  - Detalus heterogeninės skaičiavimo aprašymas (Hexagon NPU, Adreno GPU, Kryo CPU)
  - Aparatūros sąmoninga optimizacija Snapdragon platformoms su intelektualiu darbo krūvio paskirstymu
  - Pažangios kvantizacijos technikos (INT8, INT16, mišri precizika) mobiliesiems diegimams
  - Energiją taupanti inferencijos optimizacija baterijomis maitinamoms įrenginiams ir realaus laiko programoms
  - Pilnas įdiegimo vadovas su QNN SDK nustatymu ir aplinkos konfigūracija
  - Praktiniai pavyzdžiai: PyTorch į QNN konvertavimas, daugiafunkcinės optimizacijos, konteksto binarų generavimas
  - Pažangios naudojimo schemos: pasirinktinių backendų konfigūracija, dinaminė kvantizacija, veiklos profilavimas
  - Išsamus trikčių šalinimo skyrius ir bendruomenės ištekliai

- **Patobulinta Module04 struktūra**:
  - Atnaujintas README.md įtraukta 7 progresyvūs skyriai (buvo 6)
  - Pridėtas Qualcomm QNN prie našumo etalonų lentelės (5-15x greičio pagerėjimas, 50-80% atminties sutaupymai)
  - Išsamūs mokymosi rezultatai mobilios AI diegimui ir energijos optimizavimui

### Pakeista - Module04 dokumentacijos atnaujinimai
- **Microsoft Olive dokumentacijos patobulinimas** (`Module04/03.MicrosoftOlive.md`):
  - Pridėtas išsamus „Olive receptų saugyklos“ skyrius su daugiau nei 100 iš anksto parengtų optimizavimo receptų
  - Detalus palaikomų modelių šeimų aprašymas (Phi, Llama, Qwen, Gemma, Mistral, DeepSeek)
  - Praktiniai receptų pritaikymo ir bendruomenės indėlių naudojimo pavyzdžiai
  - Patobulinta su našumo etalonais ir integracijos gairėmis

- **Skyriaus pertvarkymas Module04**:
  - Apple MLX perkeltas į 5 skyrių (buvo 6)
  - Workflow sintezė perkeliama į 6 skyrių (buvo 7)  
  - Qualcomm QNN pateiktas kaip 7 skyrius (specializuotas mobiliesiems/kraštui)
  - Atnaujintos visos failų nuorodos ir navigacijos saitynai atitinkamai

### Ištaisyta - Dirbtuvių pavyzdžių tikrinimas
- **chat_bootstrap.py tikrinimas ir pataisymai**:
  - Ištaisyta sugadinta importo eilutė (`util.util.workshop_utils` → `util.workshop_utils`)
  - Sukurtas trūkstamas `__init__.py` util pakete tinkamam Python modulio nuskaitymui
  - Įdiegtos reikalingos priklausomybės (openai, foundry-local-sdk) conda aplinkoje
  - Sėkmingai patikrintas pavyzdžių paleidimas tiek su numatytais, tiek su individualiais paskatinimais
  - Patvirtinta integracija su Foundry Local paslauga ir modelio įkėlimas („phi-4-mini“ su CUDA optimizacija)

### Dokumentacija - Išsamūs vadovų atnaujinimai
- **Module04 README.md visiškas pertvarkymas**:
  - Pridėtas Qualcomm QNN kaip pagrindinis optimizacijos pagrindas šalia OpenVINO, Olive, MLX
  - Atnaujinti skyrių mokymosi rezultatai įtraukiant mobilių AI diegimą ir energijos optimizavimą
  - Patobulinta našumo palyginimo lentelė su QNN metrikomis ir mobilios/krašto naudojimo atvejais
  - Išlaikyta loginė eiga nuo įmonių sprendimų iki platformos specifinių optimizacijų

- **Kryžminės nuorodos ir navigacija**:
  - Atnaujintos visos vidinės nuorodos ir failų saitynai pagal naują skyriaus numeraciją
  - Patobulintas darbo eigos sintezės aprašymas, įtraukiant mobilią, stalinių kompiuterių ir debesų aplinkas
  - Pridėtos išsamios Qualcomm kūrėjų ekosistemos nuorodos

## 2025-10-08

### Pridėta - Dirbtuvių išsamus atnaujinimas
- **Dirbtuvių README.md išsamus perrašymas**:
  - Pridėtas išsamus įvadas aiškinantis Edge AI vertės pasiūlymą (privatumas, našumas, kaina)
  - Sukurti 6 pagrindiniai mokymosi tikslai su išsamiais gebėjimais
  - Pridėta mokymosi rezultatų lentelė su pristatymais ir gebėjimų matrica
  - Įtraukta karjerai paruoštų įgūdžių skiltis dėl pramonės aktualumo
  - Pridėtas greito pradžios vadovas su išankstiniais reikalavimais ir 3 žingsnių nustatymu
  - Sukurtos resursų lentelės Python pavyzdžiams (8 failai su vykdymo trukmėmis)
  - Pridėta Jupyter užrašų knygelių lentelė (8 užrašų knygelės su sudėtingumo įvertinimais)
  - Sukurtos dokumentacijos lentelės (7 pagrindiniai dokumentai su „Naudokite kai“ gairėmis)
  - Pridėtos mokymosi kelio rekomendacijos skirtingiems įgūdžių lygiams

- **Dirbtuvių validavimo ir testavimo infrastruktūra**:
  - Sukurtas `scripts/validate_samples.py` - išsamus validavimo įrankis sintaksei, importams ir geriausioms praktikoms
  - Sukurtas `scripts/test_samples.py` - „smoke test“ paleidėjas visiems Python pavyzdžiams
  - Pridėta validavimo dokumentacija į `scripts/README.md`

- **Išsamūs dokumentai**:
  - Sukurtas `SAMPLES_UPDATE_SUMMARY.md` - 400+ eilučių detali apžvalga apie visus patobulinimus
  - Sukurtas `UPDATE_COMPLETE.md` - atnaujinimo užbaigimo vykdomoji santrauka
  - Sukurtas `QUICK_REFERENCE.md` - greitojo naudojimo dirbtuvių kortelė

### Pakeista - Dirbtuvių Python pavyzdžių modernizavimas
- **Visi 8 Python pavyzdžiai atnaujinti pagal geriausias praktikas**:
  - Patobulintas klaidų tvarkymas su try-except blokais visose I/O operacijose
  - Pridėti tipų užuominos ir išsamūs docstring’ai
  - Įgyvendintas nuoseklus [INFO]/[ERROR]/[RESULT] žurnalo modelis
  - Apsaugoti pasirenkami importai su įdiegimo patarimais
  - Patobulinta naudotojo grįžtamoji informacija visuose pavyzdžiuose

- **session01/chat_bootstrap.py**:
  - Patobulintas kliento inicializavimas su išsamiais klaidų pranešimais
  - Pagerintas srautinio perdavimo klaidų tvarkymas su blokų validacija
  - Pridėtas geresnis išimčių apdorojimas paslaugos neprieinamumo atvejais

- **session02/rag_pipeline.py**:
  - Pridėti importo apsaugos sakinių transformeriams su įdiegimo patarimais
  - Pagerintas klaidų tvarkymas įmestų vektorių ir generavimo operacijose
  - Patobulintas išvesties formatavimas su struktūrizuotais rezultatais

- **session02/rag_eval_ragas.py**:
  - Apsaugoti pasirenkami importai (ragas, datasets) su draugiškais klaidų pranešimais
  - Pridėtas klaidų tvarkymas vertinimo metrikoms
  - Pagerintas vertinimo rezultatų išvesties formatavimas

- **session03/benchmark_oss_models.py**:
  - Įgyvendintas elegantiškas kritimų tvarkymas (toliau vykdo modelių nesėkmės atvejais)
  - Pridėtas išsamus eigos ataskaitavimas ir klaidų tvarkymas modeliui
  - Patobulinta statistinės analizės skaičiavimas su išsamia klaidų atkūrimo sistema

- **session04/model_compare.py**:
  - Pridėtos tipų užuominos (Tuple grąžinimo tipai)
  - Pagerintas išvesties formatavimas su struktūrizuotais JSON rezultatais
  - Įgyvendintas klaidų tvarkymas modeliui su atkūrimu

- **session05/agents_orchestrator.py**:
  - Patobulintas Agent.act() su išsamiais docstring’ais
  - Pridėtas vamzdynų klaidų tvarkymas su etapiniu žurnalu
  - Pagerintas atminties valdymas ir būsena

- **session06/models_router.py**:
  - Patobulinta funkcijų dokumentacija visiems maršruto komponentams
  - Pridėtas išsamus žurnalas funkcijoje route()
  - Pagerinta testų išvestis su struktūrizuotais rezultatais

- **session06/models_pipeline.py**:
  - Pridėtas klaidų tvarkymas pagalbinėje chat() funkcijoje
  - Patobulintas pipeline() su etapų žurnalu ir eigos ataskaita
  - Pagerintas main() su išsamiu klaidų atkūrimu

### Dokumentacija - Dirbtuvių dokumentacijos patobulinimas
- Pakeistas pagrindinis README.md su Dirbtuvių skyriumi, pabrėžiant praktinį mokymosi kelią
- Patobulintas STUDY_GUIDE.md su išsamia Dirbtuvių skiltimi įtraukiant:
  - Mokymosi tikslus ir studijų fokusavimo sritis
  - Savęs vertinimo klausimus
  - Praktines užduotis su laiko įvertinimais
  - Laiko paskirstymas intensyviam ir daliniam mokymuisi
  - Pridėtas Dirbtuvės prie pažangos stebėjimo šablono
- Pakeistas laiko paskirstymo vadovas nuo 20 valandų iki 30 valandų (įskaitant Dirbtuves)
- Pridėtos Dirbtuvių pavyzdžių aprašai ir mokymosi rezultatai prie README

### Ištaisyta
- Išspręsti nevienodi klaidų tvarkymo modeliai tarp Dirbtuvių pavyzdžių
- Ištaisyta pasirenkamų priklausomybių importo klaidos su tinkama apsauga
- Pataisyti trūkstami tipų žymėjimai kritinėse funkcijose
- Pagerinta naudotojo grįžtamoji reakcija klaidų scenarijuose
- Ištaisyti validavimo klausimai su išsamiu testavimo pagrindu

---

## 2025-09-23

### Pakeista - Svarbi Module 08 modernizacija
- **Išsami suderinimas su Microsoft Foundry-Local repozitorijos šablonais**
  - Atnaujinti visi kodo pavyzdžiai, kad naudotų modernų `FoundryLocalManager` ir OpenAI SDK integraciją
  - Pakeisti pasenę rankiniai `requests` kvietimai į tinkamą SDK naudojimą
  - Suderinti įgyvendinimo modeliai pagal oficialią Microsoft dokumentaciją ir pavyzdžius

- **05.AIPoweredAgents.md modernizacija**:
  - Atnaujinta daugiaagentinė orkestracija naudojant modernius SDK šablonus
  - Pagerinta koordinatoriaus įgyvendinimu su pažangiomis funkcijomis (atsiliepimų ciklai, našumo stebėsena)
  - Pridėtas išsamus klaidų tvarkymas ir paslaugos būklės tikrinimas
  - Integruotos tinkamos nuorodos į vietinius pavyzdžius (`samples/05/multi_agent_orchestration.ipynb`)
  - Atnaujinti funkcijų kvietimų pavyzdžiai naudojant modernų `tools` parametrą vietoje pasenusio `functions`
  - Pridėti gamybai paruošti modeliai su stebėjimu ir statistikos fiksavimu

- **06.ModelsAsTools.md visiškas perrašymas**:
  - Pakeista bazinė įrankių registracija į išmanią modelių maršrutizavimo įgyvendinimą
  - Pridėtas raktažodžiais pagrįstas modelių atrinkimas skirtingų užduočių tipams (bendri, loginiai, kodas, kūrybiniai)
  - Integruota aplinkos konfigūracija su lanksčiu modelių priskyrimu
  - Patobulinta su išsamia paslaugos būklės stebėsena ir klaidų valdymu
  - Pridėtos gamybinio diegimo schemos su užklausų stebėjimu ir našumo sekimu
  - Suderinta su vietiniu įgyvendinimu `samples/06/router.py` ir `samples/06/model_router.ipynb`

- **Dokumentacijos struktūros patobulinimai**:
  - Pridėti apžvalgos skyriai pabrėžiantys modernizaciją ir SDK suderinimą
  - Papildyta emocijomis ir geresniu formatavimu siekiant geresnio skaitomumo
  - Pridėtos tinkamos nuorodos į vietinius pavyzdžius per visą dokumentaciją
  - Įtraukta gamybai paruošta įgyvendinimo gairė ir geriausios praktikos

### Pridėta
- Išsamūs apžvalgos skyriai Module 08 failuose, atskleidžiantys modernią SDK integraciją
- Architektūros akcentai, atskleidžiantys pažangias funkcijas (daugiaagentinės sistemos, išmanus maršrutizavimas)
- Tiesioginės nuorodos į vietinius pavyzdžių įgyvendinimus praktinei patirčiai
- Gamybinio diegimo gairės su stebėjimu ir klaidų valdymo modeliais
- Interaktyvūs Jupyter užrašų knygelių pavyzdžiai su pažangiomis funkcijomis ir etalonais

### Ištaisyta
- Dokumentacijos ir faktinio pavyzdžių įgyvendinimo neatitikimai
- Pasenusios SDK naudojimo schemos Module 08
- Trūkstamos nuorodos į išsamų vietinį pavyzdžių rinkinį
- Nenuoseklūs įgyvendinimo metodai skirtinguose skyriuose

---

## 2025-09-18

### Pridėta
- Module 08: Microsoft Foundry Local – Pilnas kūrėjo įrankių rinkinys
  - Šešios sesijos: nustatymas, Azure AI Foundry integracija, atviro kodo modeliai, pažangiausios demonstracijos, agentai ir modeliai kaip įrankiai
  - Veikiantys pavyzdžiai kataloge `Module08/samples/01`–`06` su Windows cmd instrukcijomis
    - `01` REST greito pokalbio pavyzdys (`chat_quickstart.py`)

    - `02` SDK greitas pradėjimas su OpenAI/Foundry Local ir Azure OpenAI palaikymu (`sdk_quickstart.py`)
    - `03` CLI sąrašas ir testavimas (`list_and_bench.cmd`)
    - `04` Chainlit demonstracija (`app.py`)
    - `05` Daugių agentų koordinavimas (`python -m samples.05.agents.coordinator`)
    - `06` Modelių kaip įrankių maršrutizatorius (`router.py`)
- Azure OpenAI palaikymas 2 sesijos SDK pavyzdyje su aplinkos kintamųjų konfigūracija
- `.vscode/settings.json` nukreiptas į `Module08/.venv` ir pagerintas Python analizės sprendimas
- `.env` su `PYTHONPATH` patarimu VS Code/Pylance žinojimui

### Pakeista
- Numatytoji modelio versija pakeista į `phi-4-mini` visuose 8 modulio dokumentuose ir pavyzdžiuose; pašalinti likę `phi-3.5` paminėjimai 8 modulyje
- Maršrutizatoriaus (`Module08/samples/06/router.py`) patobulinimai:
  - Galinių taškų atranka per `foundry service status` su regex analizavimu
  - `/v1/models` sveikatos patikra paleidimo metu
  - Aplinkos kintamaisiais konfigūruojama modelių registracija (`GENERAL_MODEL`, `REASONING_MODEL`, `CODE_MODEL`, `TOOL_REGISTRY` JSON)
- Atnaujinti reikalavimai: `Module08/requirements.txt` dabar įtraukia `openai` (kartu su `requests`, `chainlit`)
- Patikslintos Chainlit pavyzdžio instrukcijos ir pridėta trikčių šalinimo pagalba; importų sprendimas per darbo srities nustatymus

### Ištaisyta
- Išspręstos importų problemos:
  - Maršrutizatorius nebepriklauso nuo neegzistuojančio `utils` modulio; funkcijos įtrauktos tiesiogiai
  - Koordinatorius naudoja santykinį importą (`from .specialists import ...`) ir paleidžiamas per modulio kelią
  - VS Code/Pylance konfigūracija, kad būtų išspręsti `chainlit` ir paketo importai
- Ištaisytas nedidelis `STUDY_GUIDE.md` klaidos rašybos pakeitimas ir pridėta 8 modulio apimtis

### Pašalinta
- Ištrintas nenaudojamas `Module08/infra/obs.py` ir pašalintas tuščias `infra/` katalogas; stebėjimo šablonai palikti kaip neprivalomi dokumentacijoje

### Perkelta
- Konsoliduoti 8 modulio demonstraciniai pavyzdžiai po `Module08/samples` su sesijų sunumeruotais aplankais
  - Chainlit programa perkelta į `samples/04`
  - Agentai perkelti į `samples/05` ir pridėti `__init__.py` failai pakuotės sprendimui

### Dokumentai
- 8 modulio sesijos dokumentai ir visi pavyzdžių README papildyti Microsoft Learn ir patikimų tiekėjų nuorodomis
- `Module08/README.md` atnaujintas su pavyzdžių apžvalga, maršrutizatoriaus konfigūracija ir tikrinimo patarimais
- `Module07/README.md` Windows Foundry Local skyrius patikrintas su Learn dokumentais
- `STUDY_GUIDE.md` atnaujintas:
  - Pridėtas 8 modulis apžvalgoje, tvarkaraščiuose, pažangos sekimo priemonėje
  - Pridėta išsami Nuorodų sekcija (Foundry Local, Azure AI, Olive, ONNX Runtime, OpenVINO, MLX, Llama.cpp, vLLM, Ollama, AI Toolkit, Windows ML)

---

## Istorinė santrauka
- Nustatyta kurso architektūra ir moduliai (1–7 moduliai)
- Iteratyvus turinio modernizavimas, formatavimo standartizavimas, pridėti atvejų analizės pavyzdžiai
- Išplėsta optimizavimo sistemų apimtis (Llama.cpp, Olive, OpenVINO, Apple MLX)

## Nepaskelbta / laukia įgyvendinimo (pasiūlymai)
- Pasirenkami kiekvieno pavyzdžio dūmų testai Foundry Local prieinamumo patikrai
- Peržiūrėti vertimus ir suderinti modelių paminėjimus (pvz., `phi-4-mini`) kur būtina
- Pridėti minimalų pyright konfigūraciją, jei komandos pageidauja visos darbo srities griežtumo

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
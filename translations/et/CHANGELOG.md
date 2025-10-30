<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "78ca68df03ae43371b203ea43d346dec",
  "translation_date": "2025-10-30T15:36:07+00:00",
  "source_file": "CHANGELOG.md",
  "language_code": "et"
}
-->
# Muudatuste logi

Kõik olulised muudatused EdgeAI algajatele on dokumenteeritud siin. Projekt kasutab kuupäevapõhiseid kirjeid ja Keep a Changelog stiili (Lisatud, Muudetud, Parandatud, Eemaldatud, Dokumentatsioon, Ümber paigutatud).

## 2025-10-30

### Lisatud - Module06 AI agentide põhjalik täiustus
- **Microsoft Agent Framework integratsioon** (`Module06/01.IntroduceAgent.md`):
  - Täielik sektsioon Microsoft Agent Frameworkist tootmisvalmis agentide arendamiseks
  - Üksikasjalikud integratsioonimustrid Foundry Localiga serva juurutamiseks
  - Näited mitme agendi orkestreerimisest spetsialiseeritud SLM mudelitega
  - Ettevõtte juurutamise mustrid ressursside haldamise ja jälgimisega
  - Turvalisuse ja vastavuse funktsioonid serva agentide süsteemidele
  - Reaalse maailma rakenduste näited (jaekaubandus, tervishoid, klienditeenindus)

- **Tootmise SLM agentide juurutamise strateegiad**:
  - **Foundry Local**: Täielik ettevõtte tasemel serva AI käitusaja dokumentatsioon koos paigalduse, konfiguratsiooni ja tootmismustritega
  - **Ollama**: Täiustatud kogukonnale suunatud juurutamine koos põhjaliku jälgimise ja mudelite haldamisega
  - **VLLM**: Kõrge jõudlusega järeldusmootor täiustatud optimeerimistehnikate ja ettevõtte funktsioonidega
  - Tootmise juurutamise kontrollnimekirjad ja võrdlustabelid kõigi kolme platvormi jaoks

- **Serva optimeeritud SLM raamistikud täiustused**:
  - **ONNX Runtime**: Uus põhjalik sektsioon platvormidevaheliseks SLM agentide juurutamiseks
  - Universaalsed juurutamismustrid Windowsi, Linuxi, macOS-i, iOS-i ja Androidi jaoks
  - Riistvara kiirenduse valikud (CPU, GPU, NPU) automaatse tuvastamisega
  - Tootmisvalmis funktsioonid ja agentidele spetsiifilised optimeerimised
  - Täielikud rakenduse näited Microsoft Agent Frameworki integratsiooniga

- **Viited ja täiendav lugemine**:
  - Põhjalik ressursikogu üle 100 autoriteetse allikaga
  - Põhiuuringud AI agentide ja väikeste keelemudelite kohta
  - Ametlik dokumentatsioon kõigi peamiste raamistikute ja tööriistade kohta
  - Tööstusaruanded, turuanalüüsid ja tehnilised võrdlused
  - Haridusressursid, konverentsid ja kogukonna foorumid
  - Standardid, spetsifikatsioonid ja vastavuse raamistikud

### Muudetud - Module06 sisu moderniseerimine
- **Täiustatud õpieesmärgid**: Lisatud Microsoft Agent Frameworki valdamine ja serva juurutamise võimekus
- **Tootmise fookus**: Liikumine kontseptuaalsest rakendamisvalmis juhendamiseni koos tootmise näidetega
- **Koodinäited**: Kõik näited uuendatud kaasaegsete SDK mustrite ja parimate tavade järgi
- **Arhitektuurimustrid**: Lisatud hierarhilised agentide arhitektuurid ja serva-pilve koordineerimine
- **Jõudluse optimeerimine**: Täiustatud ressursside haldamise ja automaatse skaleerimise soovitustega

### Dokumentatsioon - Module06 struktuuri täiustamine
- **Põhjalik Agent Frameworki katvus**: Alates põhimõistetest kuni ettevõtte juurutamiseni
- **Tootmise juurutamise strateegiad**: Täielikud juhendid Foundry Locali, Ollama ja VLLM jaoks
- **Platvormidevaheline optimeerimine**: Lisatud ONNX Runtime universaalseks juurutamiseks
- **Ressursikogu**: Ulatuslikud viited jätkuvaks õppimiseks ja rakendamiseks

### Lisatud - Module06 Model Context Protocol (MCP) dokumentatsiooni uuendus
- **MCP sissejuhatuse moderniseerimine** (`Module06/03.IntroduceMCP.md`):
  - Uuendatud uusimate MCP spetsifikatsioonidega modelcontextprotocol.io-st (2025-06-18 versioon)
  - Lisatud ametlik USB-C analoog AI rakenduste standardiseeritud ühenduste jaoks
  - Uuendatud arhitektuuri sektsioon ametliku kahekihilise disainiga (Andmekiht + Transpordikiht)
  - Täiustatud põhielementide dokumentatsioon serveri elementidega (Tööriistad, Ressursid, Viited) ja kliendi elementidega (Proovivõtmine, Küsitlus, Logimine)

- **Põhjalikud MCP viited ja ressursid**:
  - Lisatud **MCP algajatele** link (https://aka.ms/mcp-for-beginners)
  - Ametlik MCP dokumentatsioon ja spetsifikatsioonid (modelcontextprotocol.io)
  - Arendusressursid, sealhulgas MCP Inspector ja viiteimplementatsioonid
  - Tehnilised standardid (JSON-RPC 2.0, JSON Schema, OpenAPI, Server-Sent Events)

### Lisatud - Module04 Qualcomm QNN integratsioon
- **Uus sektsioon 7: Qualcomm QNN optimeerimiskomplekt** (`Module04/05.QualcommQNN.md`):
  - Põhjalik 400+ rea juhend Qualcommi ühtse AI järeldusraamistiku kohta
  - Üksikasjalik katvus heterogeense arvutuse kohta (Hexagon NPU, Adreno GPU, Kryo CPU)
  - Riistvarateadlik optimeerimine Snapdragon platvormide jaoks intelligentse töökoormuse jaotusega
  - Täiustatud kvantiseerimistehnikad (INT8, INT16, segatäpsus) mobiilseks juurutamiseks
  - Energiatõhus järelduse optimeerimine akutoitega seadmete ja reaalajas rakenduste jaoks
  - Täielik paigaldusjuhend QNN SDK seadistamise ja keskkonna konfiguratsiooniga
  - Praktilised näited: PyTorchist QNN-i konversioon, mitme taustsüsteemi optimeerimine, konteksti binaarfaili genereerimine
  - Täiustatud kasutusmustrid: kohandatud taustsüsteemi konfiguratsioon, dünaamiline kvantiseerimine, jõudluse profiilimine
  - Põhjalik tõrkeotsingu sektsioon ja kogukonna ressursid

- **Täiustatud Module04 struktuur**:
  - Uuendatud README.md, et lisada 7 progressiivset sektsiooni (varem 6)
  - Lisatud Qualcomm QNN jõudluse võrdlustabelisse (5-15x kiiruse paranemine, 50-80% mälukasutuse vähenemine)
  - Põhjalikud õpieesmärgid mobiilse AI juurutamise ja energiakasutuse optimeerimise jaoks

### Muudetud - Module04 dokumentatsiooni uuendused
- **Microsoft Olive dokumentatsiooni täiustamine** (`Module04/03.MicrosoftOlive.md`):
  - Lisatud põhjalik "Olive Retseptide Kogu" sektsioon, mis hõlmab üle 100 eelvalmistatud optimeerimisretsepti
  - Üksikasjalik katvus toetatud mudeliperekondade kohta (Phi, Llama, Qwen, Gemma, Mistral, DeepSeek)
  - Praktilised kasutusnäited retseptide kohandamiseks ja kogukonna panusteks
  - Täiustatud jõudluse võrdluste ja integratsiooni juhistega

- **Sektsioonide ümberjärjestamine Module04-s**:
  - Apple MLX viidud sektsiooni 5 (varem sektsioon 6)
  - Töövoo süntees viidud sektsiooni 6 (varem sektsioon 7)
  - Qualcomm QNN paigutatud sektsiooni 7 (spetsialiseeritud mobiilne/serva fookus)
  - Uuendatud kõik failiviited ja navigeerimislingid vastavalt

### Parandatud - Töötuba näidiste valideerimine
- **chat_bootstrap.py valideerimine ja parandamine**:
  - Parandatud rikutud importimislausung (`util.util.workshop_utils` → `util.workshop_utils`)
  - Loodud puuduolev `__init__.py` util paketis Python mooduli korrektseks lahendamiseks
  - Paigaldatud vajalikud sõltuvused (openai, foundry-local-sdk) conda keskkonda
  - Edukalt valideeritud näidise käivitamine nii vaikimisi kui kohandatud viidetega
  - Kinnitatud integratsioon Foundry Local teenusega ja mudeli laadimine (phi-4-mini koos CUDA optimeerimisega)

### Dokumentatsioon - Põhjalikud juhendite uuendused
- **Module04 README.md täielik ümberstruktureerimine**:
  - Lisatud Qualcomm QNN peamise optimeerimisraamistikuna OpenVINO, Olive, MLX kõrvale
  - Uuendatud peatüki õpieesmärgid, et hõlmata mobiilse AI juurutamist ja energiakasutuse optimeerimist
  - Täiustatud jõudluse võrdlustabel QNN mõõdikute ja mobiilse/serva kasutusjuhtumitega
  - Säilitatud loogiline järjestus ettevõtte lahendustest platvormispetsiifiliste optimeerimisteni

- **Ristviited ja navigeerimine**:
  - Uuendatud kõik sisemised lingid ja failiviited uue sektsiooni numeratsiooni jaoks
  - Täiustatud töövoo sünteesi kirjeldus, et hõlmata mobiil-, lauaarvuti- ja pilvekeskkondi
  - Lisatud põhjalikud ressursilingid Qualcommi arendaja ökosüsteemi jaoks

## 2025-10-08

### Lisatud - Töötuba põhjalik uuendus
- **Töötuba README.md täielik ümberkirjutamine**:
  - Lisatud põhjalik sissejuhatus, mis selgitab Edge AI väärtuspakkumist (privaatsus, jõudlus, kulud)
  - Loodud 6 põhikompetentsi koos üksikasjalike oskustega
  - Lisatud õpieesmärkide tabel koos tulemuste ja kompetentside maatriksiga
  - Lisatud karjäärivalmiduse oskuste sektsioon tööstuse asjakohasuse jaoks
  - Lisatud kiirjuhend koos eeltingimuste ja 3-astmelise seadistusega
  - Loodud ressursitabelid Python näidiste jaoks (8 faili koos käitusaegadega)
  - Lisatud Jupyteri märkmike tabel (8 märkmikku koos raskusastme hinnangutega)
  - Loodud dokumentatsiooni tabel (7 olulist dokumenti koos "Kasutamise aeg" juhendiga)
  - Lisatud õpitee soovitused erinevate oskustasemete jaoks

- **Töötuba valideerimise ja testimise infrastruktuur**:
  - Loodud `scripts/validate_samples.py` - Põhjalik valideerimistööriist süntaksi, importide ja parimate tavade jaoks
  - Loodud `scripts/test_samples.py` - Kiirtesti käivitaja kõigi Python näidiste jaoks
  - Lisatud valideerimise dokumentatsioon `scripts/README.md`-sse

- **Põhjalik dokumentatsioon**:
  - Loodud `SAMPLES_UPDATE_SUMMARY.md` - 400+ rea üksikasjalik juhend kõigi täiustuste kohta
  - Loodud `UPDATE_COMPLETE.md` - Uuenduse lõpetamise kokkuvõte
  - Loodud `QUICK_REFERENCE.md` - Kiirviitekaart töötuba jaoks

### Muudetud - Töötuba Python näidiste moderniseerimine
- **Kõik 8 Python näidist uuendatud parimate tavadega**:
  - Täiustatud veakäsitlust try-except plokkidega kõigi I/O operatsioonide ümber
  - Lisatud tüübiviited ja põhjalikud dokstringid
  - Rakendatud järjepidev [INFO]/[ERROR]/[RESULT] logimismuster
  - Kaitstud valikulised impordid paigaldusvihjetega
  - Parandatud kasutajate tagasisidet kõigis näidistes

- **session01/chat_bootstrap.py**:
  - Täiustatud kliendi initsialiseerimist põhjalike veateadetega
  - Parandatud voogesituse veakäsitlust tükkide valideerimisega
  - Lisatud parem erandite käsitlus teenuse kättesaamatuse korral

- **session02/rag_pipeline.py**:
  - Lisatud impordikaitsed sentence-transformers jaoks koos paigaldusvihjetega
  - Täiustatud veakäsitlust sisestamise ja genereerimise operatsioonide jaoks
  - Parandatud väljundi vormindamist struktureeritud tulemustega

- **session02/rag_eval_ragas.py**:
  - Kaitstud valikulised impordid (ragas, datasets) kasutajasõbralike veateadetega
  - Lisatud veakäsitlus hindamismõõdikute jaoks
  - Täiustatud väljundi vormindamist hindamistulemustega

- **session03/benchmark_oss_models.py**:
  - Rakendatud sujuv degradeerumine (jätkab mudelite tõrgete korral)
  - Lisatud üksikasjalik edenemisaruandlus ja mudelite kaupa veakäsitlus
  - Täiustatud statistika arvutamist põhjaliku veakäsitlusega

- **session04/model_compare.py**:
  - Lisatud tüübiviited (Tuple tagastustüübid)
  - Täiustatud väljundi vormindamist struktureeritud JSON tulemustega
  - Rakendatud mudelite kaupa veakäsitlus taastumisega

- **session05/agents_orchestrator.py**:
  - Täiustatud Agent.act() põhjalike dokstringidega
  - Lisatud torujuhtme veakäsitlus etappide kaupa logimisega
  - Parandatud mäluhaldust ja oleku jälgimist

- **session06/models_router.py**:
  - Täiustatud funktsioonide dokumentatsiooni kõigi marsruutimise komponentide jaoks
  - Lisatud üksikasjalik logimine route() funktsioonis
  - Parandatud testide väljund struktureeritud tulemustega

- **session06/models_pipeline.py**:
  - Lisatud veakäsitlus chat() abifunktsioonile
  - Täiustatud pipeline() etappide logimise ja edenemisaruandlusega
  - Parandatud main() põhjaliku veakäsitlusega

### Dokumentatsioon - Töötuba dokumentatsiooni täiustamine
- Uuendatud peamine README.md töötuba sektsiooniga, mis rõhutab praktilist õpiteed
- Täiustatud STUDY_GUIDE.md töötuba sektsiooniga, mis sisaldab:
  - Õpieesmärke ja õppe fookusvaldkondi
  - Enesehindamise küsimusi
  - Praktilisi harjutusi koos ajahinnangutega
  - Aja jaotust intensiivseks ja osalise ajaga õppimiseks
  - Lisatud töötuba edusammude jälgimise mallile
- Uuendatud aja jaotuse juhend 20 tunnilt 30 tunnile (sh töötuba)
- Lisatud töötuba näidiste kirjeldused ja õpieesmärgid README-sse

### Parandatud
- Lahendatud ebajärjekindlad veakäsitluse mustrid töötuba näidistes
- Parandatud valikuliste sõltuvuste impordivead korralike kaitsetega
- Parandatud puuduvad tüübiviited kriitilistes funktsioonides
- Lahendatud ebapiisav kasutajate tagasiside veastsenaariumides
- Parandatud valideerimisprobleemid põhjaliku testimise infrastruktuuriga

---

## 2025-09-23

### Muudetud - Module 08 suur moderniseerimine
- **Põhjalik kooskõlastamine Microsoft Foundry-Locali repositooriumi mustritega**
  - Uuendatud kõik koodinäited kaasaegse `FoundryLocalManager` ja OpenAI SDK integratsiooniga
  - Asendatud vananenud käsitsi `requests` kõned korraliku SDK kasutamisega
  - Rakendatud mustrid vastavalt ametlikule Microsofti dokumentatsioonile ja näidistele

- **05.AIPoweredAgents.md moderniseerimine**:
  - Uuendatud mitme agendi orkestreerimine kaasaegsete SDK mustritega
  - Täiustatud koordinaatori rakendamine täiustatud funktsioonidega (tagasiside tsüklid, jõudluse jälgimine)
  - Lisatud põhjalik veakäsitlus ja teenuse tervisekontroll
  - Integreeritud korralikud viited kohalikele näidistele (`samples/05/multi_agent_orchestration.ipynb`)
  - Uuendatud funktsioonide kutsumise näited kaasaegse `tools` parameetriga, asendades vananenud `functions`
  - Lisatud tootmisvalmis mustrid jälgimise ja statistika jälgimisega

- **06.ModelsAs
  - Käivitatavad näidised kaustas `Module08/samples/01`–`06` koos Windows cmd juhistega
    - `01` REST kiire vestlus (`chat_quickstart.py`)
    - `02` SDK kiire alustamine OpenAI/Foundry Local ja Azure OpenAI toetusega (`sdk_quickstart.py`)
    - `03` CLI loendamine ja testimine (`list_and_bench.cmd`)
    - `04` Chainlit demo (`app.py`)
    - `05` Multi-agent orkestreerimine (`python -m samples.05.agents.coordinator`)
    - `06` Mudelid-tööriistadena router (`router.py`)
- Azure OpenAI tugi Session 2 SDK näidises koos keskkonnamuutuja konfiguratsiooniga
- `.vscode/settings.json` suunatud `Module08/.venv` kaustale, et parandada Python analüüsi lahendust
- `.env` koos `PYTHONPATH` vihjega VS Code/Pylance teadlikkuse jaoks

### Muudetud
- Vaikimisi mudel uuendatud `phi-4-mini` peale kogu Module 08 dokumentatsioonis ja näidistes; eemaldatud järelejäänud viited `phi-3.5` mudelile Module 08 sees
- Routeri (`Module08/samples/06/router.py`) täiustused:
  - Lõpp-punktide avastamine `foundry service status` kaudu regex-parsimisega
  - `/v1/models` tervisekontroll käivitamisel
  - Keskkonnast konfigureeritav mudeliregister (`GENERAL_MODEL`, `REASONING_MODEL`, `CODE_MODEL`, `TOOL_REGISTRY` JSON)
- Nõuded uuendatud: `Module08/requirements.txt` sisaldab nüüd `openai` (koos `requests`, `chainlit`)
- Chainlit näidise juhised täpsustatud ja lisatud tõrkeotsing; importide lahendamine tööruumi seadistuste kaudu

### Parandatud
- Lahendatud importimise probleemid:
  - Router ei sõltu enam olematust `utils` moodulist; funktsioonid on integreeritud
  - Koordinaator kasutab suhtelist importi (`from .specialists import ...`) ja käivitatakse mooduli teekonna kaudu
  - VS Code/Pylance konfiguratsioon, et lahendada `chainlit` ja pakettide impordid
- Parandatud väike kirjaviga `STUDY_GUIDE.md` failis ja lisatud Module 08 kajastus

### Eemaldatud
- Kustutatud kasutamata `Module08/infra/obs.py` ja eemaldatud tühi `infra/` kataloog; jälgitavuse mustrid säilitatud dokumentides valikulistena

### Ümber paigutatud
- Module 08 demod koondatud kausta `Module08/samples` sessiooni numbritega kaustadesse
  - Chainlit rakendus viidud kausta `samples/04`
  - Agendid viidud kausta `samples/05` ja lisatud `__init__.py` failid paketi lahendamiseks

### Dokumentatsioon
- Module 08 sessiooni dokumentatsioon ja kõik näidiste README-d täiendatud Microsoft Learn ja usaldusväärsete tarnijate viidetega
- `Module08/README.md` uuendatud näidiste ülevaate, routeri konfiguratsiooni ja valideerimise näpunäidetega
- `Module07/README.md` Windows Foundry Local sektsioon valideeritud Learn dokumentide vastu
- `STUDY_GUIDE.md` uuendatud:
  - Lisatud Module 08 ülevaatesse, ajakavadesse, progressi jälgijasse
  - Lisatud ulatuslik viidete sektsioon (Foundry Local, Azure AI, Olive, ONNX Runtime, OpenVINO, MLX, Llama.cpp, vLLM, Ollama, AI Toolkit, Windows ML)

---

## Ajalooline (kokkuvõte)
- Kursuse arhitektuur ja moodulid loodud (Moodulid 01–07)
- Iteratiivne sisu moderniseerimine, vormindamise standardiseerimine ja lisatud juhtumiuuringud
- Laiendatud optimeerimisraamistike kajastus (Llama.cpp, Olive, OpenVINO, Apple MLX)

## Avaldamata / Ootel (ettepanekud)
- Valikulised näidiste testid, et valideerida Foundry Local saadavust
- Tõlgete ülevaatus, et viia mudeliviited (nt `phi-4-mini`) vastavusse
- Lisada minimaalne pyright konfiguratsioon, kui meeskonnad eelistavad tööruumi tasemel rangust

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.
# Muudatuste logi

Kõik olulised muudatused EdgeAI for Beginners projektis on dokumenteeritud siin. See projekt kasutab kuupõhiseid kirjeid ja Keep a Changelog stiili (Lisatud, Muudetud, Parandatud, Eemaldatud, Dokumentatsioon, Liigutatud).

## 2025-10-30

### Lisatud - Module06 AI agentide põhjalik täiendus
- **Microsoft Agent Frameworki integratsioon** (`Module06/01.IntroduceAgent.md`):
  - Täielik jaotis Microsoft Agent Frameworki kohta tootmisvalmis agentide arenduseks
  - Põhjalikud integratsioonimustrid Foundry Local'iga edge juurutuseks
  - Mitme agendi orkestreerimise näited spetsialiseeritud SLM mudelitega
  - Ettevõtte juurutamise mustrid ressursside haldamise ja jälgimisega
  - Turvalisuse ja vastavuse funktsioonid serva agentide süsteemidele
  - Reaalmaailma rakenduse näited (jaemüük, tervishoid, klienditeenindus)

- **Tootmisvalmis SLM agentide juurutusstrateegiad**:
  - **Foundry Local**: Täielik ettevõtte klassi edge AI käituskeskkonna dokumentatsioon koos paigaldus-, konfiguratsiooni- ja tootmismustritega
  - **Ollama**: Täiustatud kogukonnale suunatud juurutus koos põhjaliku jälgimise ja mudelite haldusega
  - **VLLM**: Kõrge jõudlusega inferentsimootor täiustatud optimeerimistehnikatega ja ettevõtte funktsioonidega
  - Kõigi kolme platvormi tootmisjuurutuse kontrollnimekirjad ja võrdlustabelid

- **Servale optimeeritud SLM raamistikute täiustus**:
  - **ONNX Runtime**: Uus põhjalik jaotis ristplatvormiliseks SLM agentide juurutuseks
  - Ülemaailmsed juurutusmustrid Windowsi, Linuxi, macOS-i, iOS-i ja Androidi platvormidel
  - Riistvara kiirenduse valikud (CPU, GPU, NPU) automaatse tuvastusega
  - Tootmisvalmis funktsioonid ja agentidele spetsiifilised optimeerimised
  - Täielikud rakenduse näited Microsoft Agent Frameworki integratsiooniga

- **Viited ja täiendav lugemine**:
  - Põhjalik ressursikogu üle 100 autoriteetse allikaga
  - Põhiuurimused AI agentide ja väikeste keelemudelite kohta
  - Kõigi suurte raamistikute ja tööriistade ametlik dokumentatsioon
  - Tööstusaruanne, turuanalüüs ja tehnilised võrdlusandmed
  - Haridusressursid, konverentsid ja kogukonna foorumid
  - Standardid, spetsifikatsioonid ja vastavusraamistikud

### Muudetud - Module06 sisu moderniseerimine
- **Täiustatud õpieesmärgid**: Lisatud Microsoft Agent Frameworki valdamine ja edge juurutuse võimekus
- **Tootmisfookus**: Üleminek kontseptuaalselt juhistelt juurutusvalmis juhenditele tootmisnäidetega
- **Koodinäited**: Kõik näited uuendatud kaasaegsete SDK mustrite ja parimate tavadega
- **Arhitektuurimustrid**: Lisatud hierarhilised agendi arhitektuurid ja edge-pilve koordineerimine
- **Jõudluse optimeerimine**: Täiustatud ressursside haldamise ja automaatse skaleerimise soovitustega

### Dokumentatsioon - Module06 struktuuri täiendus
- **Põhjalik agendi raamistikute käsitlus**: Alates baaskontseptsioonidest kuni ettevõtte juurutuseni
- **Tootmisjuurutuse strateegiad**: Täielikud juhendid Foundry Local, Ollama ja VLLM platvormide jaoks
- **Ristplatvormi optimeerimine**: Lisatud ONNX Runtime universaalseks juurutuseks
- **Ressursikogu**: Laiendatud viited edasiseks õppimiseks ja rakendamiseks

### Lisatud - Module06 Mudeli konteksti protokolli (MCP) dokumentatsiooni uuendus
- **MCP tutvustuse moderniseerimine** (`Module06/03.IntroduceMCP.md`):
  - Uuendatud uusimate MCP spetsifikatsioonidega modelcontextprotocol.io portaalist (2025-06-18 versioon)
  - Lisatud ametlik USB-C analoog AI rakenduste standardiseeritud ühendamiseks
  - Uuendatud arhitektuuriosa ametliku kahekihilise disainiga (andmekiht + transpordikiht)
  - Täiustatud põhialuste dokumentatsioon serveri primitiivide (Tööriistad, Ressursid, Sõnumid) ja kliendi primitiivide (Valimine, Tõrjetuvastus, Logimine) kohta

- **Põhjalikud MCP viited ja ressursid**:
  - Lisatud **MCP algajatele** link (https://aka.ms/mcp-for-beginners)
  - Ametlik MCP dokumentatsioon ja spetsifikatsioonid (modelcontextprotocol.io)
  - Arendusressursid, sh MCP Inspector ja viited rakendustele
  - Tehnilised standardid (JSON-RPC 2.0, JSON Schema, OpenAPI, Server-Sent Events)


### Lisatud - Module04 Qualcomm QNN integratsioon
- **Uus jaotis 7: Qualcomm QNN optimeerimisvõrgustik** (`Module04/05.QualcommQNN.md`):
  - Üle 400 rea pikk põhjalik juhend Qualcommi ühtse AI inferentsiraamistiku kohta
  - Põhjalik käsitlus heterogeensest arvutusest (Hexagoni NPU, Adreno GPU, Kryo CPU)
  - Riistvarateadlik optimeerimine Snapdragon platvormide jaoks intelligentse töökoormuse jaotusega
  - Täiustatud kvantiseerimistehnikad (INT8, INT16, segakirjas) mobiilseks juurutuseks
  - Energiatõhus inferentsi optimeerimine akutoitel seadmetele ja reaalajas rakendustele
  - Täielik paigaldusjuhend QNN SDK seadistuse ja keskkonnakonfiguratsiooniga
  - Praktilised näited: PyTorchi teisendus QNN-iks, mitme tagaveaga optimeerimine, konteksti binaarfaili genereerimine
  - Täiustatud kasutusmustrid: kohandatud tagavea konfiguratsioon, dünaamiline kvantiseerimine, jõudlusprofiilimine
  - Põhjalik veaotsingu jaotise ja kogukonna ressursside kogumik

- **Parendatud Module04 struktuur**:
  - Uuendatud README.md, lisades 7 järkjärgulist jaotist (varasemalt 6)
  - Lisatud Qualcomm QNN jõudlusvõrdlustabelisse (5-15x kiiruse parandamine, 50-80% mälukasutuse vähenemine)
  - Põhjalikud õpitulemused mobiilse AI juurutuse ja võimsuse optimeerimise kohta

### Muudetud - Module04 dokumentatsiooni uuendused
- **Microsoft Olive dokumentatsiooni täiendus** (`Module04/03.MicrosoftOlive.md`):
  - Lisatud põhjalik "Olive retseptide hoidla" jaotis, mis hõlmab 100+ eelnevalt koostatud optimeerimisretsepti
  - Detailne käsitlus toetatud mudelipere kohta (Phi, Llama, Qwen, Gemma, Mistral, DeepSeek)
  - Praktilised kasutusnäited retseptide kohandamiseks ja kogukonna panustele
  - Täiustatud jõudluse võrdlustabelite ja integreerimisjuhistega

- **Jaotiste ümberkorraldus Module04**:
  - Apple MLX paigutatud nüüd jaotisse 5 (varasemalt 6)
  - Workflow Synthesis viidud jaotisse 6 (varasemalt 7)
  - Qualcomm QNN määratud jaotisesse 7 (spetsialiseeritud mobiilne/edge fookus)
  - Kõik failiviited ja navigeerimislingid vastavalt uuendatud

### Parandatud - Töötuba näidiste valideerimine
- **chat_bootstrap.py valideerimine ja parandamine**:
  - Parandatud rikutud import-lause (`util.util.workshop_utils` → `util.workshop_utils`)
  - Loodud puuduv `__init__.py` util paketti Python mooduli korrektsel lahenemisel
  - Installitud vajalikud sõltuvused (openai, foundry-local-sdk) conda keskkonda
  - Edukas näidiste käivitamise valideerimine nii vaikimisi kui ka kohandatud käskudega
  - Kinnitatud integreerimine Foundry Local teenusega ja mudeli laadimine (phi-4-mini koos CUDA optimeerimisega)

### Dokumentatsioon - Põhjalikud juhendite uuendused
- **Module04 README.md täielik ümberkorraldus**:
  - Lisatud Qualcomm QNN kui oluline optimeerimisraamistik OpenVINO, Olive ja MLX kõrvale
  - Uuendatud peatükkide õpitulemused, hõlmates mobiilset AI juurutust ja võimsuse optimeerimist
  - Täiustatud jõudluse võrdlustabel QNN mõõdikute ning mobiilsete ja edge kasutusjuhtumitega
  - Loogiline üleminek ettevõtte lahendustelt platvormispetsiifiliste optimeerimiste juurde säilinud

- **Ristviited ja navigeerimine**:
  - Uuendatud kõik siselingid ja failiviited uue jaotiste numeratsiooniga
  - Täiustatud töövoo sünteesi kirjeldus, hõlmates mobiil-, töölaua- ja pilvekeskkondi
  - Lisatud põhjalikud ressursilingid Qualcommi arendajate ökosüsteemi jaoks

## 2025-10-08

### Lisatud - Töötuba põhjalik uuendus
- **Töötuba README.md täielik ümberkirjutus**:
  - Lisatud põhjalik sissejuhatus Edge AI väärtuspakkumisele (privaatsus, jõudlus, kulu)
  - Loodud 6 põhieesmärki koos detailsete pädevustega
  - Lisatud õpitulemuste tabel koos tulemite ja pädevusmatriisiga
  - Kaasatud karjäärivalmiduse osakaal tööstuse asjakohasuse nimel
  - Lisatud kiire alguse juhend eeltingimuste ja 3-astmelise seadistusega
  - Loodud ressursitabelid Python näidete jaoks (8 faili koos käitusaegadega)
  - Lisatud Jupyteri märkmikute tabel (8 märkmikku raskusastmidega)
  - Koostatud dokumentatsiooni tabel (7 olulist dokumenti koos "Kasutamise juhendiga")
  - Lisatud õpitee soovitused erinevatele oskustasemetele

- **Töötoa valideerimise ja testimise infrastruktuur**:
  - Loodud `scripts/validate_samples.py` - põhjalik valideerimise tööriist süntaksi, importide ja parimate tavade kontrolliks
  - Loodud `scripts/test_samples.py` - kõigi Python näidiste suitsutestide käitaja
  - Lisatud valideerimise dokumentatsioon `scripts/README.md` faili

- **Põhjalik dokumentatsioon**:
  - Loodud `SAMPLES_UPDATE_SUMMARY.md` - üle 400 rea pikk juhend kõigist parendustest
  - Loodud `UPDATE_COMPLETE.md` - uuenduse lõpetamise kokkuvõte
  - Loodud `QUICK_REFERENCE.md` - kiirjuhendi kaart töötoa jaoks

### Muudetud - Töötoa Python näidiste moderniseerimine
- **Kõik 8 Python näidet uuendatud parimate tavadega**:
  - Täiustatud veahaldus try-except plokkidega kõigi sisendi/väljundi operatsioonide ümber
  - Lisatud tüübi vihjed ja põhjalikud dokstringid
  - Rakendatud ühtlane [INFO]/[ERROR]/[RESULT] logimise muster
  - Kaitstud valikulised importimised paigaldusviidetega
  - Parandatud kasutajate tagasisidet kõigis näidetes

- **session01/chat_bootstrap.py**:
  - Täiustatud kliendi initsialiseerimine põhjalike veateadetega
  - Parendatud voogedastuse veahaldus tükikeste valideerimisega
  - Lisatud parem erandihaldus teenuse kättesaamatusel

- **session02/rag_pipeline.py**:
  - Lisatud importimise kaitsed sentence-transformers jaoks koos paigaldusvihjetega
  - Täiustatud veahaldus manuste ja genereerimise operatsioonide puhul
  - Parandatud väljundi vormindus struktureeritud tulemitena

- **session02/rag_eval_ragas.py**:
  - Kaitstud valikulised impordid (ragas, datasets) kasutajasõbralike veateadetega
  - Lisatud veahaldus hindamismeetmete puhul
  - Parandatud väljundi vormindus hindamistulemite jaoks

- **session03/benchmark_oss_models.py**:
  - Rakendatud sujuv degradeerumine (continuation mudeliriketega)
  - Lisatud detailne edenemisteate ja per-mudeli veahaldus
  - Täiustatud statistika arvutus koos põhjaliku vea taastamisega

- **session04/model_compare.py**:
  - Lisatud tüübi vihjed (Tuple tüüpi tagastused)
  - Täiustatud väljundi vormindus struktureeritud JSON tulemitena
  - Rakendatud per-mudeli veahaldus koos taastumisega

- **session05/agents_orchestrator.py**:
  - Täiustatud Agent.act() põhjalike dokstringidega
  - Lisatud torujuhtme veahaldus ja etapi kaupa logimine
  - Parandatud mäluhaldus ja oleku jälgimine

- **session06/models_router.py**:
  - Täiustatud funktsioonidokumentatsioon kõigi marsruutimise komponentide jaoks
  - Lisatud detailne logimine route() funktsioonis
  - Parandatud testiväljund struktureeritud tulemitena

- **session06/models_pipeline.py**:
  - Lisatud veahaldus chat() abifunktsioonile
  - Täiustatud pipeline() etapi logimise ja edenemisteatega
  - Parandatud main() põhjaliku vea taastamisega

### Dokumentatsioon - Töötuba dokumentatsiooni täiendus
- Uuendatud põhi README.md töötubade sektsiooniga, rõhutades praktilist õpperada
- Täiustatud STUDY_GUIDE.md põhjaliku töötubade sektsiooniga, mis sisaldab:
  - Õpieesmärgid ja õppimise keskpunktid
  - Enesehindamise küsimused
  - Käed-külge harjutused koos ajahindamistega
  - Ajajaotus kontsentreeritud ja osalise tööajaga õppeks
  - Lisatud töötuba edenemise jälgimise mustrisse
- Uuendatud ajajaotuse juhend 20 tunnist 30 tunnini (kaasas töötuba)
- Lisatud töötuba näidiste kirjeldused ja õpitulemused README-sse

### Parandatud
- Lahendatud ebaühtlased veahaldusmustrite probleemid töötoa näidistes
- Parandatud valikuliste sõltuvuste impordivead asjakohaste kaitsetega
- Parandatud kriitilistes funktsioonides puuduvad tüübi vihjed
- Lahendatud kasutaja tagasiside puudujäägid veakäsitluses
- Parandatud valideerimisprobleemid põhjaliku testimisinfrastruktuuriga

---

## 2025-09-23

### Muudetud - Suur Module 08 moderniseerimine
- **Põhjalik kooskõlastus Microsoft Foundry-Local hoidla mustritega**
  - Uuendatud kõik koodinäited kasutama modernset `FoundryLocalManager` ja OpenAI SDK integratsiooni
  - Asendatud aegunud käsitsi `requests` kutsed korrektselt SDK kasutusega
  - Koodi mustrid viidud vastavusse Microsofti ametliku dokumentatsiooni ja näidetega

- **05.AIPoweredAgents.md moderniseerimine**:
  - Uuendatud mitme agendi orkestreerimine kasutama kaasaegseid SDK mustreid
  - Täiustatud koordinaatori rakendus täiustatud funktsioonidega (tagasisidelõngad, jõudluse jälgimine)
  - Lisatud põhjalik veahaldus ja teenuse tervise kontrollimine
  - Integreeritud korrektsed viited kohalikule näidistestile (`samples/05/multi_agent_orchestration.ipynb`)
  - Uuendatud funktsioonikutsed kasutama kaasaegset `tools` parameetrit vananenud `functions` asemel
  - Lisatud tootmisvalmis mustrid jälgimise ja statistika kogumisega

- **06.ModelsAsTools.md täielik ümberkirjutus**:
  - Asendatud baastaseme tööriistaregister intelligentse mudelisisendi rakendusega
  - Lisatud võtmesõnal põhinev mudeli valik erinevate ülesandetüüpide jaoks (üldine, loogiline, kood, loominguline)
  - Integreeritud keskkonna põhine konfiguratsioon koos paindliku mudeli määramisega
  - Täiustatud põhjaliku teenuse tervise jälgimise ja veahaldusega
  - Lisatud tootmisjuurutuse mustrid päringute jälgimise ja jõudluse mõõtmisega
  - Vastavusse viidud kohaliku rakendusega `samples/06/router.py` ja `samples/06/model_router.ipynb`

- **Dokumentatsiooni struktuuri parendused**:
  - Lisatud ülevaate jaotised, mille rõhk on moderniseerimisel ja SDK kooskõlastusel
  - Täiustatud emotikonide ja parema vormindusega lugejasõbralikkuse parandamiseks
  - Lisatud korrektsed viited kohalikele näidistfailidele kogu dokumentatsioonis
  - Kaasatud tootmisvalmis rakenduse juhised ja parimad praktikad

### Lisatud
- Põhjalikud ülevaate jaotised Module 08 failides, rõhutades kaasaegset SDK integratsiooni
- Arhitektuuri esiletõstmised, näidates täiustatud funktsioone (mitme agendi süsteemid, intelligentne marsruutimine)
- Otsesed viited kohalikele näidistrakendustele praktilise kogemuse saamiseks
- Tootmisjuurutuse juhised jälgimise ja veahaldusmustritega
- Interaktiivsed Jupyteri märkmike näited täiustatud funktsioonide ja võrdlusnäitajatega

### Parandatud
- Dokumentatsiooni ja tegelike näidistrakenduste vahelised kõrvalekalded likvideeritud
- Vananenud SDK kasutamismustrid kogu Module 08 ulatuses
- Puuduvad viited põhjalikule kohalikule näidiste kogu
- Ebaühtlased rakenduslähenemised erinevates jaotistes parandatud

---

## 2025-09-18

### Lisatud
- Module 08: Microsoft Foundry Local – Täielik arendajate tööriistakast
  - Kuus sessiooni: seadistus, Azure AI Foundry integratsioon, avatud lähtekoodiga mudelid, tipptasemel demo'sid, agendid ja mudelid-tööriistadena
  - Käivitatavad näited kataloogis `Module08/samples/01`–`06` koos Windows cmd juhistega
    - `01` REST kiire vestlus (`chat_quickstart.py`)

    - `02` SDK kiire alustamine koos OpenAI/Foundry Local ja Azure OpenAI toega (`sdk_quickstart.py`)
    - `03` CLI list-and-bench (`list_and_bench.cmd`)
    - `04` Chainlit demo (`app.py`)
    - `05` Multi-agentorkestreerimine (`python -m samples.05.agents.coordinator`)
    - `06` Mudelite kui tööriistade ruuter (`router.py`)
- Azure OpenAI tugi Session 2 SDK näites keskkonnamuutuja seadistusega
- `.vscode/settings.json`, mis näitab `Module08/.venv` ja parandab Python analüüsi lahendust
- `.env` koos `PYTHONPATH` vihjega VS Code/Pylance teadlikkuse jaoks

### Muutunud
- Vaikimisi mudel uuendatud `phi-4-mini` peale üle kogu Module 08 dokumentatsiooni ja näidete; eemaldatud ülejäänud `phi-3.5` viited Module 08-st
- Ruuter (`Module08/samples/06/router.py`) täiustused:
  - Lõpp-punkti avastamine `foundry service status` käsuga ja regex-analüüsiga
  - Käivitamisel tervisekontroll `/v1/models` kaudu
  - Keskkonnamuutujatega seadistatav mudelite register (`GENERAL_MODEL`, `REASONING_MODEL`, `CODE_MODEL`, `TOOL_REGISTRY` JSON)
- Nõuded uuendatud: `Module08/requirements.txt` sisaldab nüüd `openai` (lisaks `requests` ja `chainlit`-ile)
- Chainlit näite juhend täpsustatud ja tõrkeotsing lisatud; importide lahendus tööruumi seadistuste kaudu

### Parandatud
- Lahendatud importimise probleemid:
  - Ruuter ei sõltu enam olematust `utils` moodulist; funktsioonid on in-line
  - Koordinaator kasutab suhtelist importi (`from .specialists import ...`) ja käivitatakse mooduli rajalt
  - VS Code/Pylance seadistus `chainlit` ja pakettide importide lahendamiseks
- Väike kirjaviga `STUDY_GUIDE.md` parandatud ja lisatud Module 08 kaetus

### Eemaldatud
- Kustutatud kasutamata `Module08/infra/obs.py` ja eemaldatud tühi `infra/` kaust; jälgitavusmustrid säilitatud optional dokumentatsioonis

### Liigutatud
- Module 08 demo-d konsolideeritud `Module08/samples` alla koos sessioonidega nummerdatud kaustadesse
  - Chainlit rakendus liigutatud `samples/04`
  - Agendid liigutatud `samples/05` ja lisatud `__init__.py` failid pakettide lahendamiseks

### Dokumentatsioon
- Module 08 sessiooni dokumendid ja kõik näidiste README-d täiendatud Microsoft Learn ja usaldusväärsete partnerite viidetega
- `Module08/README.md` uuendatud nende mahtudega: Näidiste ülevaade, ruuteri konfiguratsioon ja valideerimise näpunäited
- `Module07/README.md` Windows Foundry Local osa valideeritud Learn dokumentidega sobivuse osas
- `STUDY_GUIDE.md` uuendatud:
  - Lisatud Module 08 ülevaade, ajakavad, edenemiskell
  - Lisatud põhjalik Viidete sektsioon (Foundry Local, Azure AI, Olive, ONNX Runtime, OpenVINO, MLX, Llama.cpp, vLLM, Ollama, AI Toolkit, Windows ML)

---

## Ajalooline (kokkuvõte)
- Kursusarhitektuur ja moodulid loodud (Moodulid 01–07)
- Iteratiivne sisukontroll, vorminduse standardiseerimine ja juhtumiuuringute lisamine
- Laiendatud optimeerimisraamistike käsitlust (Llama.cpp, Olive, OpenVINO, Apple MLX)

## Väljaandmata / Tagavarakirje (ettepanekud)
- Valikulised iga näite suitsutestid Foundry Local kättesaadavuse kontrolliks
- Ülevaade tõlgetest mudeliviidete ühtlustamiseks (nt `phi-4-mini`) vajadusel
- Lisada minimaalne pyright konfiguratsioon kui tiimid eelistavad tööruumi üldist rangeid reegleid

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
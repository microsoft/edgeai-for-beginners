<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "78ca68df03ae43371b203ea43d346dec",
  "translation_date": "2025-10-30T14:56:38+00:00",
  "source_file": "CHANGELOG.md",
  "language_code": "sl"
}
-->
# Dnevnik sprememb

Vse pomembne spremembe v projektu EdgeAI za začetnike so dokumentirane tukaj. Projekt uporablja zapise, ki temeljijo na datumih, in slog "Keep a Changelog" (Dodano, Spremenjeno, Popravljeno, Odstranjeno, Dokumentacija, Premaknjeno).

## 2025-10-30

### Dodano - Celovita izboljšava modula 06 AI agenti
- **Integracija Microsoft Agent Framework** (`Module06/01.IntroduceAgent.md`):
  - Celoten odsek o Microsoft Agent Framework za razvoj agentov, pripravljenih za produkcijo
  - Podrobni vzorci integracije s Foundry Local za implementacijo na robu
  - Primeri orkestracije več agentov s specializiranimi modeli SLM
  - Vzorci implementacije v podjetjih z upravljanjem virov in nadzorom
  - Funkcije varnosti in skladnosti za sisteme agentov na robu
  - Primeri iz resničnega sveta (maloprodaja, zdravstvo, storitve za stranke)

- **Strategije implementacije produkcijskih SLM agentov**:
  - **Foundry Local**: Celovita dokumentacija za robni AI runtime na ravni podjetja z namestitvijo, konfiguracijo in produkcijskimi vzorci
  - **Ollama**: Izboljšana skupnostno usmerjena implementacija s celovitim nadzorom in upravljanjem modelov
  - **VLLM**: Visoko zmogljiv pogonski mehanizem za sklepanje z naprednimi tehnikami optimizacije in funkcijami za podjetja
  - Seznami za preverjanje implementacije v produkciji in primerjalne tabele za vse tri platforme

- **Izboljšave okvirjev SLM, optimiziranih za rob**:
  - **ONNX Runtime**: Nov celovit odsek za implementacijo SLM agentov na več platformah
  - Univerzalni vzorci implementacije na Windows, Linux, macOS, iOS in Android
  - Možnosti pospeševanja strojne opreme (CPU, GPU, NPU) z avtomatskim zaznavanjem
  - Funkcije, pripravljene za produkcijo, in optimizacije, specifične za agente
  - Celotni primeri implementacije z integracijo Microsoft Agent Framework

- **Reference in dodatno branje**:
  - Celovita knjižnica virov s 100+ avtoritativnimi viri
  - Osnovni raziskovalni članki o AI agentih in majhnih jezikovnih modelih
  - Uradna dokumentacija za vse glavne okvirje in orodja
  - Industrijska poročila, analize trga in tehnični primerjalni testi
  - Izobraževalni viri, konference in skupnostni forumi
  - Standardi, specifikacije in okvirji skladnosti

### Spremenjeno - Posodobitev vsebine modula 06
- **Izboljšani učni cilji**: Dodano obvladovanje Microsoft Agent Framework in sposobnosti implementacije na robu
- **Osredotočenost na produkcijo**: Prehod od konceptualnih k smernicam, pripravljenim za implementacijo, s primeri iz produkcije
- **Primeri kode**: Posodobljeni vsi primeri za uporabo sodobnih vzorcev SDK in najboljših praks
- **Arhitekturni vzorci**: Dodane hierarhične arhitekture agentov in koordinacija rob-oblak
- **Optimizacija zmogljivosti**: Izboljšano z upravljanjem virov in priporočili za samodejno skaliranje

### Dokumentacija - Izboljšanje strukture modula 06
- **Celovita pokritost okvirja agentov**: Od osnovnih konceptov do implementacije v podjetjih
- **Strategije implementacije v produkciji**: Celoviti vodiči za Foundry Local, Ollama in VLLM
- **Optimizacija na več platformah**: Dodan ONNX Runtime za univerzalno implementacijo
- **Knjižnica virov**: Obsežne reference za nadaljnje učenje in implementacijo

### Dodano - Posodobitev dokumentacije protokola konteksta modela (MCP) v modulu 06
- **Posodobitev uvoda v MCP** (`Module06/03.IntroduceMCP.md`):
  - Posodobljeno z najnovejšimi specifikacijami MCP iz modelcontextprotocol.io (različica 2025-06-18)
  - Dodana uradna analogija USB-C za standardizirane povezave AI aplikacij
  - Posodobljen odsek o arhitekturi z uradno zasnovo dveh slojev (Podatkovni sloj + Transportni sloj)
  - Izboljšana dokumentacija osnovnih primitivov s strežniškimi primitivi (Orodja, Viri, Pozivi) in odjemalskimi primitivi (Vzorečenje, Pridobivanje, Beleženje)

- **Celovite reference in viri za MCP**:
  - Dodana povezava **MCP za začetnike** (https://aka.ms/mcp-for-beginners)
  - Uradna dokumentacija in specifikacije MCP (modelcontextprotocol.io)
  - Razvojni viri, vključno z MCP Inspector in referenčnimi implementacijami
  - Tehnični standardi (JSON-RPC 2.0, JSON Schema, OpenAPI, Server-Sent Events)

### Dodano - Modul 04 Integracija Qualcomm QNN
- **Nov odsek 7: Qualcomm QNN Optimizacijski paket** (`Module04/05.QualcommQNN.md`):
  - Celovit 400+ vrstični vodič, ki pokriva Qualcommov enotni okvir za AI sklepanje
  - Podrobna pokritost heterogenega računalništva (Hexagon NPU, Adreno GPU, Kryo CPU)
  - Optimizacija, prilagojena strojni opremi za platforme Snapdragon z inteligentno porazdelitvijo delovne obremenitve
  - Napredne tehnike kvantizacije (INT8, INT16, mešana natančnost) za mobilno implementacijo
  - Optimizacija sklepanja z nizko porabo energije za naprave na baterijski pogon in aplikacije v realnem času
  - Celoten vodič za namestitev z nastavitvijo QNN SDK in konfiguracijo okolja
  - Praktični primeri: pretvorba PyTorch v QNN, optimizacija več backendov, generacija binarnih kontekstov
  - Napredni vzorci uporabe: konfiguracija prilagojenega backend-a, dinamična kvantizacija, profiliranje zmogljivosti
  - Celovit odsek za odpravljanje težav in skupnostni viri

- **Izboljšana struktura modula 04**:
  - Posodobljen README.md za vključitev 7 progresivnih odsekov (prej 6)
  - Dodan Qualcomm QNN v tabelo primerjalnih testov zmogljivosti (5-15x izboljšanje hitrosti, 50-80% zmanjšanje pomnilnika)
  - Celoviti učni cilji za mobilno AI implementacijo in optimizacijo porabe energije

### Spremenjeno - Posodobitve dokumentacije modula 04
- **Izboljšanje dokumentacije Microsoft Olive** (`Module04/03.MicrosoftOlive.md`):
  - Dodan celovit odsek "Olive Recipes Repository", ki pokriva 100+ predhodno pripravljenih receptov za optimizacijo
  - Podrobna pokritost podprtih družin modelov (Phi, Llama, Qwen, Gemma, Mistral, DeepSeek)
  - Praktični primeri uporabe za prilagoditev receptov in prispevke skupnosti
  - Izboljšano z primerjalnimi testi zmogljivosti in smernicami za integracijo

- **Preureditev odsekov v modulu 04**:
  - Apple MLX premaknjen v odsek 5 (prej odsek 6)
  - Sinteza delovnega toka premaknjena v odsek 6 (prej odsek 7)
  - Qualcomm QNN postavljen kot odsek 7 (specializiran za mobilno/robno osredotočenost)
  - Posodobljene vse reference datotek in navigacijske povezave

### Popravljeno - Validacija vzorčnih delavnic
- **Validacija in popravilo chat_bootstrap.py**:
  - Popravljena poškodovana izjava o uvozu (`util.util.workshop_utils` → `util.workshop_utils`)
  - Ustvarjen manjkajoči `__init__.py` v paketu util za pravilno resolucijo Python modula
  - Nameščene zahtevane odvisnosti (openai, foundry-local-sdk) v conda okolju
  - Uspešno validirana izvedba vzorca z uporabo privzetih in prilagojenih pozivov
  - Potrjena integracija s storitvijo Foundry Local in nalaganje modela (phi-4-mini z optimizacijo CUDA)

### Dokumentacija - Posodobitve celovitih vodičev
- **Popolna prestrukturacija README.md modula 04**:
  - Dodan Qualcomm QNN kot glavni optimizacijski okvir poleg OpenVINO, Olive, MLX
  - Posodobljeni učni cilji poglavja za vključitev mobilne AI implementacije in optimizacije porabe energije
  - Izboljšana primerjalna tabela zmogljivosti z metrikami QNN in primeri uporabe mobilnega/robnega okolja
  - Ohranjena logična progresija od rešitev za podjetja do optimizacij, specifičnih za platformo

- **Križne reference in navigacija**:
  - Posodobljene vse notranje povezave in reference datotek za novo številčenje odsekov
  - Izboljšan opis sinteze delovnega toka za vključitev mobilnih, namiznih in oblačnih okolij
  - Dodane celovite povezave virov za Qualcommov razvijalski ekosistem

## 2025-10-08

### Dodano - Celovita posodobitev delavnice
- **Popolna prenova README.md delavnice**:
  - Dodan celovit uvod, ki pojasnjuje vrednost Edge AI (zasebnost, zmogljivost, stroški)
  - Ustvarjenih 6 osnovnih učnih ciljev z natančnimi kompetencami
  - Dodana tabela učnih rezultatov z dosežki in matriko kompetenc
  - Vključen odsek veščin, pripravljenih za kariero, za industrijsko relevantnost
  - Dodan vodič za hiter začetek s predpogoji in 3-stopenjsko nastavitvijo
  - Ustvarjene tabele virov za Python vzorce (8 datotek z časom izvajanja)
  - Dodana tabela Jupyter zvezkov (8 zvezkov z ocenami težavnosti)
  - Ustvarjena tabela dokumentacije (7 ključnih dokumentov z "Uporabi kdaj" smernicami)
  - Dodana priporočila za učne poti za različne ravni znanja

- **Validacija delavnice in testna infrastruktura**:
  - Ustvarjen `scripts/validate_samples.py` - Celovito orodje za validacijo sintakse, uvozov in najboljših praks
  - Ustvarjen `scripts/test_samples.py` - Orodje za testiranje vseh Python vzorcev
  - Dodana dokumentacija za validacijo v `scripts/README.md`

- **Celovita dokumentacija**:
  - Ustvarjen `SAMPLES_UPDATE_SUMMARY.md` - 400+ vrstični podroben vodič, ki pokriva vse izboljšave
  - Ustvarjen `UPDATE_COMPLETE.md` - Izvršni povzetek dokončanja posodobitve
  - Ustvarjen `QUICK_REFERENCE.md` - Hitri referenčni karton za delavnico

### Spremenjeno - Posodobitev Python vzorcev delavnice
- **Vsi 8 Python vzorcev posodobljeni z najboljšimi praksami**:
  - Izboljšano obravnavanje napak z bloki try-except okoli vseh I/O operacij
  - Dodani namigi tipov in celoviti docstringi
  - Implementiran dosleden vzorec beleženja [INFO]/[ERROR]/[RESULT]
  - Zaščiteni opcijski uvozi z namigi za namestitev
  - Izboljšana povratna informacija uporabniku v vseh vzorcih

- **session01/chat_bootstrap.py**:
  - Izboljšana inicializacija odjemalca z natančnimi sporočili o napakah
  - Izboljšano obravnavanje napak pri pretakanju z validacijo delov
  - Dodano boljše obravnavanje izjem za nedostopnost storitve

- **session02/rag_pipeline.py**:
  - Dodani varnostni ukrepi za uvoze sentence-transformers z namigi za namestitev
  - Izboljšano obravnavanje napak pri operacijah vdelave in generacije
  - Izboljšano formatiranje izhodov s strukturiranimi rezultati

- **session02/rag_eval_ragas.py**:
  - Zaščiteni opcijski uvozi (ragas, datasets) z uporabniku prijaznimi sporočili o napakah
  - Dodano obravnavanje napak za evalvacijske metrike
  - Izboljšano formatiranje izhodov za evalvacijske rezultate

- **session03/benchmark_oss_models.py**:
  - Implementirano postopno zmanjševanje (nadaljuje ob neuspehih modelov)
  - Dodano podrobno poročanje o napredku in obravnavanje napak za vsak model
  - Izboljšano izračunavanje statistike z celovitim okrevanjem po napakah

- **session04/model_compare.py**:
  - Dodani namigi tipov (vrste Tuple)
  - Izboljšano formatiranje izhodov s strukturiranimi JSON rezultati
  - Implementirano obravnavanje napak za vsak model z okrevanjem

- **session05/agents_orchestrator.py**:
  - Izboljšano Agent.act() z celovitimi docstringi
  - Dodano obravnavanje napak v cevovodu z beleženjem po fazah
  - Izboljšano upravljanje pomnilnika in sledenje stanju

- **session06/models_router.py**:
  - Izboljšana dokumentacija funkcij za vse komponente usmerjanja
  - Dodano podrobno beleženje v funkciji route()
  - Izboljšano testiranje izhodov s strukturiranimi rezultati

- **session06/models_pipeline.py**:
  - Dodano obravnavanje napak v pomožni funkciji chat()
  - Izboljšano pipeline() z beleženjem faz in poročanjem o napredku
  - Izboljšano main() z celovitim okrevanjem po napakah

### Dokumentacija - Izboljšanje dokumentacije delavnice
- Posodobljen glavni README.md z odsekom delavnice, ki poudarja učne poti z praktičnim delom
- Izboljšan STUDY_GUIDE.md z celovitim odsekom delavnice, vključno z:
  - Učnimi cilji in področji osredotočenosti študija
  - Vprašanja za samoocenjevanje
  - Praktične vaje z ocenami časa
  - Časovna razporeditev za intenzivno in delno študijo
  - Dodana delavnica v predlogo za sledenje napredku
- Posodobljen vodič za časovno razporeditev z 20 ur na 30 ur (vključno z delavnico)
- Dodani opisi vzorcev delavnice in učni cilji v README

### Popravljeno
- Rešeni neskladni vzorci obravnavanja napak v vzorcih delavnice
- Popravljene napake pri uvozu opcijskih odvisnosti z ustreznimi varnostnimi ukrepi
- Popravljeni manjkajoči namigi tipov v ključnih funkcijah
- Odpravljene pomanjkljive povratne informacije uporabniku v scenarijih napak
- Popravljene težave pri validaciji z vzpostavitvijo celovite testne infrastrukture

---

## 2025-09-23

### Spremenjeno - Velika posodobitev modula 08
- **Celovita uskladitev z vzorci repozitorija Microsoft Foundry-Local**
  - Posodobljeni vsi primeri kode za uporabo sodobnega `FoundryLocalManager` in integracije OpenAI SDK
  - Zamenjani zastareli ročni klici `requests` z ustrezno uporabo SDK
  - Usklajeni vzorci implementacije z uradno Microsoft dokumentacijo in vzorci

- **Posodobitev 05.AIPoweredAgents.md**:
  - Posodobljena orkestracija več agentov za uporabo sodobnih vzorcev SDK
  - Izboljšana implementacija koordinatorja z naprednimi funkcijami (povratne zanke, spremljanje zmogljivosti)
  - Dodano celovito obravnavanje napak in preverjanje zdravja storitev
  - Integrirane ustrezne reference na lokalne vzorce (`samples/05/multi_agent_orchestration.ipynb`)
  - Posodobljeni primeri klicanja funkcij za uporabo sodobnega parametra `tools` namesto zastarelega `functions`
  - Dodani vzorci, pripravljeni za produkcijo, z nadzorom in sledenjem statistiki

- **Popolna prenova 06.ModelsAsTools.md**:

  - Zagonljivi primeri v `Module08/samples/01`–`06` z navodili za Windows cmd
    - `01` REST hitri klepet (`chat_quickstart.py`)
    - `02` SDK hitri začetek z OpenAI/Foundry Local in podporo za Azure OpenAI (`sdk_quickstart.py`)
    - `03` CLI seznam in testiranje (`list_and_bench.cmd`)
    - `04` Chainlit demo (`app.py`)
    - `05` Orkestracija več agentov (`python -m samples.05.agents.coordinator`)
    - `06` Usmerjevalnik Models-as-Tools (`router.py`)
- Podpora za Azure OpenAI v vzorcu SDK v Seji 2 z nastavitvijo okoljskih spremenljivk
- `.vscode/settings.json` usmerjen na `Module08/.venv` za izboljšanje analize Python kode
- `.env` z namigom `PYTHONPATH` za boljšo prepoznavnost v VS Code/Pylance

### Spremenjeno
- Privzeti model posodobljen na `phi-4-mini` v vseh dokumentih in primerih Module 08; odstranjene preostale omembe `phi-3.5` znotraj Module 08
- Izboljšave usmerjevalnika (`Module08/samples/06/router.py`):
  - Odkrivanje končnih točk prek `foundry service status` z regex analizo
  - Preverjanje zdravja `/v1/models` ob zagonu
  - Nastavljiv register modelov prek okolja (`GENERAL_MODEL`, `REASONING_MODEL`, `CODE_MODEL`, `TOOL_REGISTRY` JSON)
- Posodobljene zahteve: `Module08/requirements.txt` zdaj vključuje `openai` (poleg `requests`, `chainlit`)
- Pojasnjena navodila za vzorec Chainlit in dodana odprava težav; rešitev uvoza prek nastavitev delovnega prostora

### Popravljeno
- Rešene težave z uvozi:
  - Usmerjevalnik ne temelji več na neobstoječem modulu `utils`; funkcije so vključene
  - Koordinator uporablja relativni uvoz (`from .specialists import ...`) in se zažene prek poti modula
  - Konfiguracija VS Code/Pylance za rešitev uvozov `chainlit` in paketov
- Popravljena manjša tipkarska napaka v `STUDY_GUIDE.md` in dodana pokritost Module 08

### Odstranjeno
- Izbrisano neuporabljeno `Module08/infra/obs.py` in odstranjena prazna mapa `infra/`; vzorci opazovanja ohranjeni kot opcijski v dokumentaciji

### Premaknjeno
- Konsolidirani demo primeri Module 08 pod `Module08/samples` z mapami, oštevilčenimi po sejah
  - Chainlit aplikacija premaknjena v `samples/04`
  - Agentje premaknjeni v `samples/05` in dodane datoteke `__init__.py` za rešitev paketov

### Dokumentacija
- Dokumenti seje Module 08 in vsi vzorčni README-ji obogateni z referencami Microsoft Learn in zaupanja vrednih ponudnikov
- `Module08/README.md` posodobljen s Pregledom vzorcev, konfiguracijo usmerjevalnika in nasveti za validacijo
- `Module07/README.md` razdelek Windows Foundry Local preverjen glede na dokumente Learn
- `STUDY_GUIDE.md` posodobljen:
  - Dodan Module 08 v pregled, urnike, sledilnik napredka
  - Dodan obsežen razdelek Referenc (Foundry Local, Azure AI, Olive, ONNX Runtime, OpenVINO, MLX, Llama.cpp, vLLM, Ollama, AI Toolkit, Windows ML)

---

## Zgodovinsko (povzetek)
- Ustanovljena arhitektura tečaja in moduli (Module 01–07)
- Iterativna modernizacija vsebine, standardizacija formatiranja in dodane študije primerov
- Razširjena pokritost optimizacijskih okvirjev (Llama.cpp, Olive, OpenVINO, Apple MLX)

## Neobjavljeno / V čakalni vrsti (predlogi)
- Opcijski testi za posamezne vzorce za preverjanje razpoložljivosti Foundry Local
- Pregled prevodov za uskladitev referenc modelov (npr. `phi-4-mini`) kjer je primerno
- Dodajanje minimalne konfiguracije pyright, če ekipe preferirajo strogo nastavitev na ravni delovnega prostora

---

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za prevajanje z umetno inteligenco [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku naj se šteje za avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne odgovarjamo za morebitna nesporazumevanja ali napačne razlage, ki izhajajo iz uporabe tega prevoda.
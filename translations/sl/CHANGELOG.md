# Dnevnik sprememb

Vse pomembne spremembe za EdgeAI za začetnike so tukaj dokumentirane. Ta projekt uporablja vnose na osnovi datumov in slog Keep a Changelog (Dodano, Spremenjeno, Popravljeno, Odstranjeno, Dokumentacija, Premaknjeno).

## 2025-10-30

### Dodano - Modul06 Izboljšave AI agentov na široko
- **Integracija Microsoft Agent Frameworka** (`Module06/01.IntroduceAgent.md`):
  - Celotno poglavje o Microsoft Agent Framework za razvoj agentov pripravljenih za produkcijo
  - Podrobni vzorci integracije s Foundry Local za edge nameščanje
  - Primeri orkestracije več agentov s specializiranimi modeli SLM
  - Vzorci za namestitev v podjetju z upravljanjem virov in nadzorom
  - Varnostne in skladnostne funkcije za edge agent sisteme
  - Primeri izvedb v resničnem svetu (maloprodaja, zdravstvo, storitve za stranke)

- **Strategije proizvodnega nameščanja SLM agentov**:
  - **Foundry Local**: Celovita dokumentacija za edge AI runtime za podjetja z namestitvijo, konfiguracijo in proizvodnimi vzorci
  - **Ollama**: Izboljšano skupnostno nameščanje z obsežnim nadzorom in upravljanjem modelov
  - **VLLM**: Visoko zmogljiv pogon za sklepanje z naprednimi tehnikami optimizacije in funkcijami za podjetja
  - Kontrolni seznami in primerjalne tabele za vse tri platforme za proizvodno nameščanje

- **Izboljšave okvirjev SLM optimiziranih za edge**:
  - **ONNX Runtime**: Novo obsežno poglavje za večplatformsko nameščanje SLM agentov
  - Univerzalni vzorci nameščanja preko Windows, Linux, macOS, iOS in Android
  - Možnosti strojne pospešitve (CPU, GPU, NPU) z avtomatskim zaznavanjem
  - Funkcije pripravljene za produkcijo in optimizacije specifične za agente
  - Popolni primeri implementacije z integracijo Microsoft Agent Frameworka

- **Reference in nadaljnje branje**:
  - Obsežna zbirka virov z več kot 100 avtoritativnih virov
  - Osnovni raziskovalni članki o AI agentih in modelih Small Language Models
  - Uradna dokumentacija za vse glavne okvirje in orodja
  - Industrijska poročila, analize trga in tehnični benchmarki
  - Izobraževalni viri, konference in skupnostni forumi
  - Standardi, specifikacije in okviri skladnosti

### Spremenjeno - Posodobitev vsebine Modula06
- **Izboljšani cilji učenja**: Dodano obvladovanje Microsoft Agent Frameworka in zmogljivosti edge nameščanja
- **Osredotočenost na produkcijo**: Premik od konceptualnega k vodilu za implementacijo s primeri za produkcijo
- **Primeri kode**: Posodobljeni vsi primeri z uporabo sodobnih vzorcev SDK in najboljših praks
- **Arhitekturni vzorci**: Dodane hierarhične arhitekture agentov in koordinacija edge-do-oblak
- **Optimizacija zmogljivosti**: Izboljšano z upravljanjem virov in priporočili za samodejno skaliranje

### Dokumentacija - Izboljšave strukture Modula06
- **Celovita pokritost Agent Frameworka**: Od osnovnih konceptov do namestitev v podjetjih
- **Strategije produkcijskega nameščanja**: Popolni vodiči za Foundry Local, Ollama in VLLM
- **Večplatformska optimizacija**: Dodan ONNX Runtime za univerzalno nameščanje
- **Zbirka virov**: Obsežne reference za nadaljnje učenje in implementacijo

### Dodano - Posodobitev dokumentacije Model Context Protocol (MCP) Modula06
- **Modernizacija uvoda MCP** (`Module06/03.IntroduceMCP.md`):
  - Posodobljeno z najnovejšimi MCP specifikacijami s modelcontextprotocol.io (verzija 2025-06-18)
  - Dodana uradna analogija USB-C za standardizirane AI aplikacijske povezave
  - Posodobljeno poglavje arhitekture z uradno dvoslojno zasnovo (Plast podatkov + Transportna plast)
  - Izboljšana dokumentacija jedrnih primitivov s primitivci strežnika (Orodja, Viri, Pozivi) in primitivci odjemalca (Vzorčenje, Izvabljanje, Beleženje)

- **Obsežne MCP reference in viri**:
  - Dodana povezava **MCP za začetnike** (https://aka.ms/mcp-for-beginners)
  - Uradna MCP dokumentacija in specifikacije (modelcontextprotocol.io)
  - Razvojni viri vključno z MCP Inspector in referenčnimi implementacijami
  - Tehnični standardi (JSON-RPC 2.0, JSON Schema, OpenAPI, Server-Sent Events)


### Dodano - Modul04 Qualcomm QNN integracija
- **Novo poglavje 7: Qualcomm QNN Optimization Suite** (`Module04/05.QualcommQNN.md`):
  - Obsežen vodič s 400+ vrsticami, zajema združeni Qualcomm AI inference okvir
  - Podrobna pokritost heterogenega računalništva (Hexagon NPU, Adreno GPU, Kryo CPU)
  - Optimizacija, zavedajoča se strojne opreme za Snapdragon platforme z inteligentno porazdelitvijo delovne obremenitve
  - Napredne tehnike kvantizacije (INT8, INT16, mešana natančnost) za mobilno nameščanje
  - Učinkovita poraba energije za inference za baterijsko napajane naprave in aplikacije v realnem času
  - Popoln namestitveni vodič z nastavitvijo QNN SDK in konfiguracijo okolja
  - Praktični primeri: Pretvorba PyTorch v QNN, optimizacija več-platišč, generiranje kontekstnih binarnih datotek
  - Napredni vzorci uporabe: konfiguracija po meri backendov, dinamična kvantizacija, profiliranje zmogljivosti
  - Obsežno poglavje odpravljanja težav in skupnostni viri

- **Izboljšana struktura Modula04**:
  - Posodobljen README.md z 7 progresivnimi poglavji (prej 6)
  - Dodan Qualcomm QNN v tabelo merilnikov zmogljivosti (5-15x izboljšava hitrosti, 50-80% zmanjšanje porabe pomnilnika)
  - Obsežni cilji učenja za mobilno AI nameščanje in optimizacijo porabe energije

### Spremenjeno - Posodobitve dokumentacije Modula04
- **Izboljšava Microsoft Olive dokumentacije** (`Module04/03.MicrosoftOlive.md`):
  - Dodano poglavje "Olive Recipes Repository" z več kot 100 predpripravljenimi recepti za optimizacijo
  - Podrobna pokritost podprtih družin modelov (Phi, Llama, Qwen, Gemma, Mistral, DeepSeek)
  - Praktični primeri uporabe za prilagajanje receptov in prispevke skupnosti
  - Izboljšano s predstavitvijo benchmarkov in smernicami za integracijo

- **Preurejanje poglavij v Modulu04**:
  - Apple MLX premaknjen v poglavje 5 (prej 6)
  - Workflow Synthesis prestavljen v poglavje 6 (prej 7)
  - Qualcomm QNN določen kot poglavje 7 (specializiran fokus na mobilno/edge)
  - Posodobljene vse reference do datotek in navigacijske povezave ustrezno

### Popravljeno - Validacija vzorčnega delavnice
- **Validacija in popravilo chat_bootstrap.py**:
  - Popravljen poškodovan uvoz (`util.util.workshop_utils` → `util.workshop_utils`)
  - Ustvarjena manjkajoča datoteka `__init__.py` v paketu util za pravilno reševanje Python modulov
  - Namestjene zahtevane odvisnosti (openai, foundry-local-sdk) v conda okolju
  - Uspešno validirano izvajanje vzorca z uporabo privzetih in prilagojenih pozivov
  - Potrjena integracija s Foundry Local servisom in nalaganje modela (phi-4-mini z optimizacijo CUDA)

### Dokumentacija - Obsežne posodobitve vodičev
- **Popolna prenova README.md Modula04**:
  - Dodan Qualcomm QNN kot glavni optimizacijski okvir poleg OpenVINO, Olive, MLX
  - Posodobljeni cilji učenja poglavij za vključitev mobilnega AI nameščanja in optimizacije porabe energije
  - Izboljšana primerjalna tabela zmogljivosti z meritvami QNN in primeri uporabe na mobilnih/edge napravah
  - Ohranjena logična progresija od rešitev za podjetja do platformno specifičnih optimizacij

- **Preklici in navigacija**:
  - Posodobljene vse notranje povezave in reference do datotek za novo številčenje poglavij
  - Izboljšan opis sintetičnega poteka dela za mobilne, namizne in oblačne okolje
  - Dodane obsežne povezave do virov za Qualcomm ekosistem razvijalcev

## 2025-10-08

### Dodano - Obsežna posodobitev delavnice
- **Popolna prepiska README.md delavnice**:
  - Dodan obsežen uvod, ki pojasnjuje vrednost Edge AI (zasebnost, zmogljivost, stroški)
  - Ustvarjenih 6 ključnih ciljev učenja z podrobnimi kompetencami
  - Dodana tabela rezultatov učenja z dostavami in matriko kompetenc
  - Vključen odsek veščin pripravljenih za kariero za industrijsko relevantnost
  - Dodan hitri vodnik z vnaprejšnjimi zahtevami in nastavitvijo v 3 korakih
  - Ustvarjene tabele virov za Python primere (8 datotek s časi izvajanja)
  - Dodana tabela Jupyter beležnic (8 beležnic z ocenami zahtevnosti)
  - Ustvarjena tabela dokumentacije (7 ključnih dokumentov z vodičem "Uporabi, ko")
  - Dodane priporočene poti učenja za različne ravni znanja

- **Infrastruktura za validacijo in testiranje delavnice**:
  - Ustvarjeno `scripts/validate_samples.py` - Obsežno orodje za validacijo sintakse, uvozov in najboljših praks
  - Ustvarjeno `scripts/test_samples.py` - Izvajalec osnovnih testov za vse Python primere
  - Dodana dokumentacija validacije v `scripts/README.md`

- **Obsežna dokumentacija**:
  - Ustvarjen `SAMPLES_UPDATE_SUMMARY.md` - 400+ vrstic obsežen vodič, ki zajema vse izboljšave
  - Ustvarjen `UPDATE_COMPLETE.md` - Izvršni povzetek zaključka posodobitve
  - Ustvarjen `QUICK_REFERENCE.md` - Hitra referenčna kartica za delavnico

### Spremenjeno - Modernizacija Python vzorcev delavnice
- **Posodobljeni vsi 8 Python vzorci z najboljšimi praksami**:
  - Izboljšano obvladovanje napak z bloki try-except okoli vseh I/O operacij
  - Dodani tipi namigov in obsežne docstring dokumentacije
  - Uveden dosleden vzorec beleženja [INFO]/[ERROR]/[RESULT]
  - Zaščiteni opcijski uvozi s namigi za namestitev
  - Izboljšana povratna informacija uporabniku v vseh primerih

- **session01/chat_bootstrap.py**:
  - Izboljšana inicializacija odjemalca z obsežnimi sporočili o napakah
  - Izboljšano ravnanje z napakami pretakanja s preverjanjem delcev
  - Dodano bolje rokovanje z izjemo za nedosegljivost storitve

- **session02/rag_pipeline.py**:
  - Dodane zaščite uvoza za sentence-transformers z namigi za namestitev
  - Izboljšano obvladovanje napak pri vstavljanju in generiranju
  - Izboljšana oblikovanost izhoda s strukturiranimi rezultati

- **session02/rag_eval_ragas.py**:
  - Zaščiteni opcijski uvozi (ragas, datasets) s prijaznimi sporočili o napakah
  - Dodano ravnanje z napakami pri ocenjevalnih metričnih podatkih
  - Izboljšana oblikovanost izhoda ocenjevalnih rezultatov

- **session03/benchmark_oss_models.py**:
  - Implementirano postopno degradacijo (nadaljuje ob napakah modela)
  - Dodano podrobno poročanje o napredku in obravnava napak po modelih
  - Izboljšano izračunavanje statistike z obsežnim okrevanjem iz napak

- **session04/model_compare.py**:
  - Dodani tipi namigov (vrnitev vrst Tuple)
  - Izboljšana oblikovanost izhoda s strukturiranim JSON rezultat
  - Implementirano ravnanje z napakami po modelih z okrevanjem

- **session05/agents_orchestrator.py**:
  - Izboljšano Agent.act() z obsežnimi docstringi
  - Dodano ravnanje z napakami v pipeline z beleženjem po stopnjah
  - Izboljšano upravljanje pomnilnika in spremljanje stanja

- **session06/models_router.py**:
  - Izboljšana dokumentacija funkcij za vse komponente usmerjanja
  - Dodano podrobno beleženje v funkciji route()
  - Izboljšan testni izhod s strukturiranimi rezultati

- **session06/models_pipeline.py**:
  - Dodano obvladovanje napak v pomožni funkciji chat()
  - Izboljšano pipeline() z beleženjem stopenj in poročanjem napredka
  - Izboljšano main() z obsežnim okrevanjem iz napak

### Dokumentacija - Izboljšave dokumentacije delavnice
- Posodobljen glavni README.md z razdelkom delavnice, ki poudarja praktično učno pot
- Izboljšan STUDY_GUIDE.md z obsežnim delavničnim razdelkom, ki vključuje:
  - Cilje učenja in področja osredotočenosti študija
  - Vprašanja za samooceno
  - Praktčne vaje z ocenami časa
  - Časovna porazdelitev za intenzivno in občasno učenje
  - Dodana delavnica v predlogo za sledenje napredku
- Posodobljen vodnik o časovni razporeditvi s 20 na 30 ur (vključno z delavnico)
- Dodani opisi vzorcev in rezultati učenja delavnice v README

### Popravljeno
- Odpravljene neskladnosti vzorcev obvladovanja napak v primerih delavnice
- Popravljene napake pri uvozu opcijskih odvisnosti z ustreznimi zaščitami
- Popravljeni manjkajoči tipi namigov v kritičnih funkcijah
- Izboljšana povratna informacija uporabniku v primerih napak
- Odpravljene težave pri validaciji z obsežno testno infrastrukturo

---

## 2025-09-23

### Spremenjeno - Velika modernizacija Modula 08
- **Celovito usklajevanje z vzorci skladišča Microsoft Foundry-Local**
  - Posodobljeni vsi primeri kode za uporabo sodobnega `FoundryLocalManager` in OpenAI SDK integracije
  - Zamenjani zastareli ročni klici `requests` z ustrezno uporabo SDK
  - Usklajeni vzorci implementacije z uradno Microsoft dokumentacijo in primeri

- **Modernizacija 05.AIPoweredAgents.md**:
  - Posodobljena orkestracija več agentov za uporabo sodobnih vzorcev SDK
  - Izboljšana implementacija koordinatorja z naprednimi funkcijami (povratne zanke, spremljanje zmogljivosti)
  - Dodano obsežno obvladovanje napak in preverjanje stanja storitve
  - Integrirane ustrezne reference do lokalnih primerov (`samples/05/multi_agent_orchestration.ipynb`)
  - Posodobljeni primeri klicev funkcij za uporabo parametra `tools` namesto zastarelega `functions`
  - Dodani produkcijsko pripravljeni vzorci z nadzorom in spremljanjem statistike

- **Popolna predelava 06.ModelsAsTools.md**:
  - Zamenjana osnovna registracija orodij z implementacijo inteligentnega usmerjevalnika modelov
  - Dodan izbor modelov na osnovi ključnih besed za različne vrste nalog (splošno, sklepanje, koda, kreativno)
  - Integrirana konfiguracija na osnovi okolja z prilagodljivo dodelitvijo modelov
  - Izboljšano z obsežnim nadzorom stanja storitve in obvladovanjem napak
  - Dodani produkcijski vzorci z nadzorom zahtev in spremljanjem zmogljivosti
  - Usklajeno z lokalno implementacijo v `samples/06/router.py` in `samples/06/model_router.ipynb`

- **Izboljšave strukture dokumentacije**:
  - Dodana poglavja pregleda, ki poudarjajo modernizacijo in usklajenost SDK
  - Izboljšano z emojiji in boljšo obliko za izboljšano berljivost
  - Dodane ustrezne reference do lokalnih vzorčnih datotek v celotni dokumentaciji
  - Vključeni vodniki za produkcijsko implementacijo in najboljše prakse

### Dodano
- Obsežna poglavja pregleda v datotekah Modula 08, ki poudarjajo sodobno SDK integracijo
- Poudarki arhitekture, ki prikazujejo napredne funkcije (sistemi z več agenti, inteligentno usmerjanje)
- Neposredne reference do lokalnih vzorčnih izvedb za praktične izkušnje
- Vodiči za produkcijsko nameščanje z vzorci nadzora in ravnanja z napakami
- Interaktivni primeri Jupyter beležnic z naprednimi funkcijami in benchmarki

### Popravljeno
- Neskladja med dokumentacijo in dejanskimi lokalnimi vzorčnimi izvedbami
- Zastareli vzorci uporabe SDK v celotnem Modulu 08
- Manjkajoče reference do obsežne lokalne zbirke vzorcev
- Neskladni pristopi implementacije v različnih poglavjih

---

## 2025-09-18

### Dodano
- Modul 08: Microsoft Foundry Local – Celovit razvojni komplet
  - Šest sej: postavitev, integracija Azure AI Foundry, odprtokodni modeli, najsodobnejši demo, agenti in modeli kot orodja
  - Zagonljivi vzorci pod `Module08/samples/01`–`06` z navodili za Windows cmd
    - `01` REST hiter klepet (`chat_quickstart.py`)

    - `02` SDK hitro začetek z OpenAI/Foundry Local in podporo Azure OpenAI (`sdk_quickstart.py`)
    - `03` CLI seznam in merjenje hitrosti (`list_and_bench.cmd`)
    - `04` Chainlit demo (`app.py`)
    - `05` Večagentna orkestracija (`python -m samples.05.agents.coordinator`)
    - `06` Usmerjevalnik modelov kot orodij (`router.py`)
- Podpora Azure OpenAI v vzorcu Session 2 SDK z konfiguracijo prek okoljskih spremenljivk
- `.vscode/settings.json` usmerjen na `Module08/.venv` za izboljšano analizo Python kode
- `.env` z namigom `PYTHONPATH` za prepoznavanje v VS Code/Pylance

### Spremenjeno
- Privzeti model posodobljen na `phi-4-mini` v celotnih dokumentih in vzorcih Modula 08; odstranjene preostale omembe `phi-3.5` znotraj Modula 08
- Izboljšave usmerjevalnika (`Module08/samples/06/router.py`):
  - Odkritje dostopnih točk preko `foundry service status` z regex analiziranjem
  - Preverjanje stanja `/v1/models` ob zagonu
  - Modelni register nastavljiv preko okolja (`GENERAL_MODEL`, `REASONING_MODEL`, `CODE_MODEL`, `TOOL_REGISTRY` JSON)
- Zahteve posodobljene: `Module08/requirements.txt` zdaj vključuje `openai` (poleg `requests`, `chainlit`)
- Navodila za Chainlit vzorec pojasnjena in dodano odpravljanje težav; rešitev uvoza preko nastavitev delovnega prostora

### Popravljeno
- Rešene težave z uvozom:
  - Usmerjevalnik ne zahteva več neobstoječega modula `utils`; funkcije so vključene neposredno
  - Koordinator uporablja relativni uvoz (`from .specialists import ...`) in je klican preko poti modula
  - Konfiguracija VS Code/Pylance za rešitev `chainlit` in paketnih uvozov
- Popravljena manjša tiskarska napaka v `STUDY_GUIDE.md` in dodana podpora za Modul 08

### Odstranjeno
- Izbrisan neuporabljen `Module08/infra/obs.py` in odstranjena prazna mapa `infra/`; vzorci opazovanja ohranjeni kot opcijski v dokumentaciji

### Premaknjeno
- Konsolidirani Modula 08 demo primeri pod `Module08/samples` v mape po številkah sej
  - Chainlit aplikacija prestavljena v `samples/04`
  - Agent prestavljeni v `samples/05` in dodane datoteke `__init__.py` za rešitev paketov

### Dokumentacija
- Dokumentacija o sejah Modula 08 in vsi vzorci v READMEs obogateni z navedbami Microsoft Learn in zaupanja vrednih prodajalcev
- `Module08/README.md` posodobljen z Pregledom vzorcev, konfiguracijo usmerjevalnika in nasveti za preverjanje
- `Module07/README.md` odsek Windows Foundry Local preverjen glede na Learn dokumentacijo
- `STUDY_GUIDE.md` posodobljen:
  - Dodan Modul 08 v pregled, urnike, sledilnik napredka
  - Dodan obsežen razdelek Reference (Foundry Local, Azure AI, Olive, ONNX Runtime, OpenVINO, MLX, Llama.cpp, vLLM, Ollama, AI Toolkit, Windows ML)

---

## Zgodovinsko (povzetek)
- Uveljavljena arhitektura tečaja in moduli (Moduli 01–07)
- Iterativna modernizacija vsebin, standardizacija oblikovanja in dodane študije primerov
- Razširjena pokritost optimizacijskih okvirov (Llama.cpp, Olive, OpenVINO, Apple MLX)

## Nepredvideno / Seznam za izvedbo (predlogi)
- Opcijski dimni testi na posamezne vzorce za preverjanje dostopnosti Foundry Local
- Pregled prevodov za uskladitev sklicev na modele (npr. `phi-4-mini`) kjer je primerno
- Dodaj minimalno pyright konfiguracijo, če ekipe želijo strogo preverjanje po celotnem delovnem prostoru

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
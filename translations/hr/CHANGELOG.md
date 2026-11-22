# Dnevnik promjena

Sve značajne promjene u EdgeAI za početnike dokumentirane su ovdje. Ovaj projekt koristi unose temeljene na datumu i stil Keep a Changelog (Dodano, Promijenjeno, Popravljeno, Uklonjeno, Dokumentacija, Premješteno).

## 2025-10-30

### Dodano - Opsežno poboljšanje AI agenata u Modulu06
- **Integracija Microsoft Agent Frameworka** (`Module06/01.IntroduceAgent.md`):
  - Potpun odjeljak o Microsoft Agent Frameworku za razvoj agenata spremnih za proizvodnju
  - Detaljni obrasci integracije s Foundry Local za edge implementaciju
  - Primjeri orkestracije multi-agenta sa specijaliziranim SLM modelima
  - Obrasci implementacije u poduzećima s upravljanjem resursima i nadzorom
  - Sigurnosne i usklađenosti značajke za edge agent sustave
  - Primjeri stvarne implementacije (maloprodaja, zdravstvena zaštita, korisnička služba)

- **Strategije implementacije SLM agenata u proizvodnju**:
  - **Foundry Local**: Potpuna dokumentacija edge AI runtime za poduzeća s instalacijom, konfiguracijom i obrascima za proizvodnju
  - **Ollama**: Poboljšana zajednički orijentirana implementacija s obuhvatnim nadzorom i upravljanjem modelima
  - **VLLM**: Visokoučinkovit inferencijski motor s naprednim tehnikama optimizacije i značajkama za poduzeća
  - Kontrolni popisi za implementaciju u proizvodnju i tablice usporedbe za sve tri platforme

- **Poboljšanje SLM okvira optimiziranih za edge**:
  - **ONNX Runtime**: Novi opsežni odjeljak za cross-platform implementaciju SLM agenata
  - Univerzalni obrasci implementacije na Windows, Linux, macOS, iOS i Android
  - Opcije hardverskog ubrzanja (CPU, GPU, NPU) s automatskim otkrivanjem
  - Značajke spremne za proizvodnju i optimizacije specifične za agente
  - Potpuni primjeri implementacije s integracijom Microsoft Agent Frameworka

- **Reference i dodatno čitanje**:
  - Opsežna zbirka izvora s više od 100 autoritativnih izvora
  - Glavni znanstveni radovi o AI agentima i Small Language Models
  - Službena dokumentacija za sve glavne okvire i alate
  - Izvještaji iz industrije, marketinške analize i tehničke referentne vrijednosti
  - Obrazovni resursi, konferencije i forumi zajednice
  - Standardi, specifikacije i okviri za usklađenost

### Promijenjeno - Modernizacija sadržaja Modula06
- **Poboljšani ciljevi učenja**: Dodana usavršavanja Microsoft Agent Frameworka i sposobnosti implementacije na edge
- **Fokus na proizvodnju**: Premještanje s konceptualnog na smjernice spremne za implementaciju s proizvodnim primjerima
- **Primjeri koda**: Ažurirani svi primjeri da koriste moderne SDK obrasce i najbolje prakse
- **Arhitektonski obrasci**: Dodane hijerarhijske arhitekture agenata i koordinacija edge-cloud
- **Optimizacija performansi**: Poboljšano upravljanje resursima i preporuke za automatsko skaliranje

### Dokumentacija - Poboljšanje strukture Modula06
- **Sveobuhvatna pokrivenost Agent Frameworka**: Od osnovnih koncepata do implementacije u poduzećima
- **Strategije implementacije u proizvodnju**: Potpuni vodiči za Foundry Local, Ollama i VLLM
- **Cross-platform optimizacija**: Dodan ONNX Runtime za univerzalnu implementaciju
- **Biblioteka resursa**: Opsežne reference za daljnje učenje i implementaciju

### Dodano - Ažuriranje dokumentacije Model Context Protocola (MCP) u Modulu06
- **Modernizacija uvoda u MCP** (`Module06/03.IntroduceMCP.md`):
  - Ažurirano s najnovijim MCP specifikacijama s modelcontextprotocol.io (verzija 2025-06-18)
  - Dodan službeni USB-C analog za standardizirane AI aplikacijske veze
  - Ažuriran odjeljak arhitekture sa službenim dvoslojnim dizajnom (Sloj podataka + Sloj prijenosa)
  - Poboljšana dokumentacija osnovnih primitiva sa server primitivima (Alati, Resursi, Upiti) i client primitivima (Uzorkovanje, Izazivanje, Evidencija)

- **Opsežne MCP reference i resursi**:
  - Dodan link **MCP za početnike** (https://aka.ms/mcp-for-beginners) 
  - Službena MCP dokumentacija i specifikacije (modelcontextprotocol.io)
  - Razvojni resursi uključujući MCP Inspector i referentne implementacije
  - Tehnički standardi (JSON-RPC 2.0, JSON Schema, OpenAPI, Server-Sent Events)


### Dodano - Integracija Qualcomm QNN u Modul04
- **Novi Odjeljak 7: Qualcomm QNN Optimization Suite** (`Module04/05.QualcommQNN.md`):
  - Opsežni vodič od preko 400 linija koji pokriva Qualcommov jedinstveni AI inferencijski okvir
  - Detaljno pokrivanje heterogenog računarstva (Hexagon NPU, Adreno GPU, Kryo CPU)
  - Hardverski svjesna optimizacija za Snapdragon platforme s inteligentnom raspodjelom opterećenja
  - Napredne tehnike kvantizacije (INT8, INT16, mješovita preciznost) za mobilnu implementaciju
  - Optimizacija energetski učinkovitog inferenciranja za uređaje na baterijski pogon i aplikacije u stvarnom vremenu
  - Potpuni vodič za instalaciju s postavkom QNN SDK-a i konfiguracijom okoline
  - Praktični primjeri: pretvorba iz PyTorch u QNN, višestruke optimizacije za backend, generacija binarnog konteksta
  - Napredni obrasci korištenja: prilagođena konfiguracija backenda, dinamička kvantizacija, profiliranje performansi
  - Opsežan odjeljak za rješavanje problema i resursi zajednice

- **Poboljšana struktura Modula04**:
  - Ažuriran README.md da uključi 7 progresivnih odjeljaka (prije 6)
  - Dodan Qualcomm QNN u tablicu referentnih performansi (poboljšanje brzine 5-15x, smanjenje memorije 50-80%)
  - Opsežni ishodi učenja za mobilnu AI implementaciju i optimizaciju potrošnje energije

### Promijenjeno - Ažuriranja dokumentacije Modula04
- **Poboljšanje dokumentacije Microsoft Olive** (`Module04/03.MicrosoftOlive.md`):
  - Dodan opsežni odjeljak "Olive Recipes Repository" koji pokriva 100+ unaprijed izrađenih optimizacijskih recepata
  - Detaljno pokrivanje podržanih porodica modela (Phi, Llama, Qwen, Gemma, Mistral, DeepSeek)
  - Praktični primjeri prilagodbe recepata i doprinosa zajednici
  - Poboljšano s referentnim vrijednostima performansi i uputama za integraciju

- **Preuređivanje odjeljaka u Modulu04**:
  - Apple MLX premješten u Odjeljak 5 (prije 6)
  - Workflow Synthesis premješten u Odjeljak 6 (prije 7)  
  - Qualcomm QNN pozicioniran kao Odjeljak 7 (specijalizirani fokus na mobilne/edge uređaje)
  - Ažurirane sve reference na datoteke i navigacijski linkovi u skladu s tim

### Popravljeno - Validacija primjera radionice
- **Validacija i popravak chat_bootstrap.py**:
  - Popravljena oštećena naredba uvoza (`util.util.workshop_utils` → `util.workshop_utils`)
  - Kreiran nedostajući `__init__.py` u util paketu za pravilno prepoznavanje Pythona modula
  - Instalirane potrebne ovisnosti (openai, foundry-local-sdk) u conda okruženju
  - Uspješno potvrđeno pokretanje primjera s podrazumijevanim i prilagođenim upitima
  - Potvrđena integracija sa servisom Foundry Local i učitavanje modela (phi-4-mini s CUDA optimizacijom)

### Dokumentacija - Opsežna ažuriranja vodiča
- **Potpuna restrukturacija README.md Modula04**:
  - Dodan Qualcomm QNN kao glavni optimizacijski okvir uz OpenVINO, Olive, MLX
  - Ažurirani ciljevi učenja u poglavljima da uključe mobilnu AI implementaciju i optimizaciju potrošnje
  - Poboljšana tablica usporedbe performansi QNN metrikama i primjerima primjene na mobilnim/edge uređajima
  - Održan logički tijek od rješenja za poduzeća do platformskih optimizacija

- **Unakrsne reference i navigacija**:
  - Ažurirani svi unutarnji linkovi i reference na datoteke za novu numeraciju odjeljaka
  - Poboljšan opis Workflow Synthesis uključujući mobilne, desktop i cloud okoline
  - Dodani sveobuhvatni resursni linkovi za Qualcomm razvojni ekosustav

## 2025-10-08

### Dodano - Opsežno ažuriranje radionice
- **Potpuni prepis README.md radionice**:
  - Dodan opsežni uvod koji objašnjava vrijednosnu ponudu Edge AI (privatnost, performanse, troškovi)
  - Kreirano 6 osnovnih ciljeva učenja s detaljnim kompetencijama
  - Dodana tablica ishoda učenja s isporukama i matricom kompetencija
  - Uključen odjeljak s vještinama spremnim za karijeru relevantne za industriju
  - Dodan vodič za brz početak s preduvjetima i postavkom u tri koraka
  - Kreirane tablice resursa za Python primjere (8 datoteka s vremenima izvođenja)
  - Dodana tablica Jupyter bilježnica (8 bilježnica s ocjenama težine)
  - Kreirana tablica dokumentacije (7 ključnih dokumenata sa savjetima "Koristi kada")
  - Dodane preporuke za put učenja za različite razine vještine

- **Validacija i infrastruktura testiranja radionice**:
  - Kreiran `scripts/validate_samples.py` - Opsežni alat za validaciju sintakse, uvoza i najboljih praksi
  - Kreiran `scripts/test_samples.py` - Pokretač osnovnih testova za sve Python primjere
  - Dodana dokumentacija validacije u `scripts/README.md`

- **Opsežna dokumentacija**:
  - Kreiran `SAMPLES_UPDATE_SUMMARY.md` - Detaljni vodič od 400+ linija koji pokriva sva poboljšanja
  - Kreiran `UPDATE_COMPLETE.md` - Izvršni sažetak završetka ažuriranja
  - Kreiran `QUICK_REFERENCE.md` - Brza referentna kartica za Radionicu

### Promijenjeno - Modernizacija Python primjera radionice
- **Svi 8 Python primjera ažurirani s najboljim praksama**:
  - Poboljšano rukovanje pogreškama s try-except blokovima oko svih I/O operacija
  - Dodani tipovi podataka i opsežni docstringovi
  - Implementiran dosljedan obrazac logiranja [INFO]/[ERROR]/[RESULT]
  - Zaštićeni opcionalni uvozi savjetima o instalaciji
  - Poboljšana povratna informacija korisniku kroz sve primjere

- **session01/chat_bootstrap.py**:
  - Poboljšana inicijalizacija klijenta s opsežnim porukama o pogreškama
  - Poboljšano rukovanje pogreškama streaminga s validacijom chunkova
  - Dodano bolje rukovanje iznimkama za nedostupnost usluge

- **session02/rag_pipeline.py**:
  - Dodane zaštite uvoza za sentence-transformers sa savjetima o instalaciji
  - Poboljšano rukovanje pogreškama za ugradnju i operacije generiranja
  - Poboljšano formatiranje ispisa sa strukturiranim rezultatima

- **session02/rag_eval_ragas.py**:
  - Zaštićeni opcionalni uvozi (ragas, datasets) s porukama o pogreškama prilagođenima korisniku
  - Dodano rukovanje pogreškama za evaluacijske metrike
  - Poboljšano formatiranje ispisa rezultata evaluacije

- **session03/benchmark_oss_models.py**:
  - Implementirano graciozno smanjenje kvalitete (nastavlja se kod neuspjeha modela)
  - Dodano detaljno izvještavanje o napretku i rukovanje pogreškama po modelima
  - Poboljšano računanje statistika s opsežnim oporavkom od pogrešaka

- **session04/model_compare.py**:
  - Dodani tipovi povratka (Tuple)
  - Poboljšano formatiranje ispisa sa strukturiranim JSON rezultatima
  - Implementirano rukovanje pogreškama po modelima s oporavkom

- **session05/agents_orchestrator.py**:
  - Poboljšan Agent.act() s opsežnim docstringovima
  - Dodano rukovanje pogreškama u pipelineu s logiranjem u fazama
  - Poboljšano upravljanje memorijom i praćenje stanja

- **session06/models_router.py**:
  - Poboljšana dokumentacija funkcija za sve ruterske komponente
  - Dodano detaljno logiranje u funkciji route()
  - Poboljšan testni ispis sa strukturiranim rezultatima

- **session06/models_pipeline.py**:
  - Dodano rukovanje pogreškama u pomoćnoj funkciji chat()
  - Poboljšan pipeline() s logiranjem faza i izvještavanjem o napretku
  - Poboljšan main() s opsežnim oporavkom od pogreški

### Dokumentacija - Poboljšanje dokumentacije radionice
- Ažuriran glavni README.md s odjeljkom radionice koji naglašava praktični put učenja
- Poboljšan STUDY_GUIDE.md s opsežnim odjeljkom radionice uključujući:
  - Ciljeve učenja i područja fokusa studija
  - Pitanja za samoocjenu
  - Praktične vježbe s procijenjenim vremenom
  - Alokaciju vremena za koncentrirano i povremeno učenje
  - Dodana radionica u predložak praćenja napretka
- Ažuriran vodič za alokaciju vremena s 20 na 30 sati (uključujući radionicu)
- Dodani opisi primjera radionice i ishodi učenja u README

### Popravljeno
- Riješeni nedosljedni obrasci rukovanja pogreškama u primjercima radionice
- Popravljene pogreške uvoza opcionalnih ovisnosti s odgovarajućim zaštitama
- Ispravljeni nedostajući tipovi podataka u kritičnim funkcijama
- Poboljšana povratna informacija korisniku u scenarijima pogreške
- Popravljeni problemi validacije s opsežnom infrastrukturom testiranja

---

## 2025-09-23

### Promijenjeno - Velika modernizacija Modula 08
- **Opsežna usklađenost s Microsoft Foundry-Local obrascima spremišta**
  - Ažurirani svi primjeri koda da koriste modernu integraciju `FoundryLocalManager` i OpenAI SDK-a
  - Zamijenjene zastarjele ručne `requests` naredbe sa pravilnim korištenjem SDK-a
  - Usklađeni obrasci implementacije sa službenom Microsoft dokumentacijom i primjerima

- **Modernizacija 05.AIPoweredAgents.md**:
  - Ažurirana orkestracija multi-agenta za korištenje modernih SDK obrazaca
  - Poboljšana implementacija koordinatora s naprednim značajkama (povratne petlje, nadzor performansi)
  - Dodano sveobuhvatno rukovanje pogreškama i provjera stanja usluge
  - Integrirane pravilne reference na lokalne primjere (`samples/05/multi_agent_orchestration.ipynb`)
  - Ažurirani primjeri pozivanja funkcija za korištenje modernog parametra `tools` umjesto zastarjelih `functions`
  - Dodani obrasci spremni za proizvodnju s nadzorom i praćenjem statistike

- **Potpuni prepis 06.ModelsAsTools.md**:
  - Zamijenjen osnovni registar alata s inteligentnom implementacijom routera modela
  - Dodan izbor modela temeljen na ključnim riječima za različite vrste zadataka (opće, rezoniranje, kod, kreativno)
  - Integrirana konfiguracija temeljena na okruženju s fleksibilnom dodjelom modela
  - Poboljšano s opsežnim nadzorom stanja usluge i rukovanjem pogreškama
  - Dodani obrasci implementacije spremni za proizvodnju s nadzorom zahtjeva i praćenjem performansi
  - Usklađeno s lokalnom implementacijom u `samples/06/router.py` i `samples/06/model_router.ipynb`

- **Poboljšanja strukture dokumentacije**:
  - Dodani odjeljci pregleda koji ističu modernizaciju i usklađenost sa SDK-om
  - Poboljšano s emojijima i boljim formatiranjem za veću čitljivost
  - Dodane pravilne reference na lokalne primjere u cijeloj dokumentaciji
  - Uključene upute za implementaciju spremnu za proizvodnju i najbolje prakse

### Dodano
- Opsežni odjeljci pregleda u datotekama Modula 08 koji ističu modernu SDK integraciju
- Istaknute arhitektonske značajke s naprednim mogućnostima (multi-agent sustavi, inteligentno usmjeravanje)
- Izravne reference na lokalne primjere za praktično iskustvo
- Smjernice za implementaciju u proizvodnju s nadzorom i obrascima rukovanja pogreškama
- Interaktivni primjeri u Jupyter bilježnicama s naprednim značajkama i referentnim vrijednostima

### Popravljeno
- Nesklad u usklađenosti između dokumentacije i stvarnih lokalnih primjera
- Zastarjeli obrasci korištenja SDK-a u cijelom Modulu 08
- Nedostajuće reference na opsežnu lokalnu zbirku primjera
- Nedosljedni pristupi implementaciji u različitim odjeljcima

---

## 2025-09-18

### Dodano
- Modul 08: Microsoft Foundry Local – Potpuni razvojni alatni paket
  - Šest sesija: postavljanje, integracija Azure AI Foundry, open-source modeli, najnovije demonstracije, agenti i modeli-kao-alati
  - Pokretni primjeri pod `Module08/samples/01`–`06` s uputama za Windows cmd
    - `01` REST brzi chat (`chat_quickstart.py`)

    - `02` Brzi početak SDK-a s OpenAI/Foundry Local i Azure OpenAI podrškom (`sdk_quickstart.py`)
    - `03` CLI list-and-bench (`list_and_bench.cmd`)
    - `04` Chainlit demo (`app.py`)
    - `05` Višagentna orkestracija (`python -m samples.05.agents.coordinator`)
    - `06` Usmjerivač Models-as-Tools (`router.py`)
- Azure OpenAI podrška u uzorku Session 2 SDK s konfiguracijom putem varijabli okoline
- `.vscode/settings.json` usmjeren na `Module08/.venv` radi bolje Python analize
- `.env` s naznakom `PYTHONPATH` za bolju podršku u VS Code/Pylance

### Promijenjeno
- Zadani model ažuriran na `phi-4-mini` kroz Module 08 dokumentaciju i uzorke; uklonjene preostale reference na `phi-3.5` unutar Module 08
- Poboljšanja usmjerivača (`Module08/samples/06/router.py`):
  - Otkrivanje krajnjih točaka putem `foundry service status` s regex parsiranjem
  - Provjera zdravlja `/v1/models` pri pokretanju
  - Konfigurabilni registar modela preko varijabli okoline (`GENERAL_MODEL`, `REASONING_MODEL`, `CODE_MODEL`, `TOOL_REGISTRY` u JSON formatu)
- Ažurirani zahtjevi: `Module08/requirements.txt` sada uključuje `openai` (uz `requests`, `chainlit`)
- Jasnije upute za Chainlit uzorak i dodan troubleshooting; rješavanje uvoza putem postavki radnog prostora

### Ispravljeno
- Riješeni problemi s uvozom:
  - Usmjerivač više ne ovisi o nepostojećem modulu `utils`; funkcije su integrirane
  - Koordinator koristi relativni uvoz (`from .specialists import ...`) i pokreće se putem modulske putanje
  - Konfiguracija VS Code/Pylance za rješavanje `chainlit` i uvoz paketa
- Ispravljena manja tipfeler u `STUDY_GUIDE.md` i dodano pokrivanje Module 08

### Uklonjeno
- Izbrisan neiskorišteni `Module08/infra/obs.py` i uklonjen prazan direktorij `infra/`; obrasci za promatranje ostaju kao opcija u dokumentaciji

### Premješteno
- Konsolidirani Module 08 demo uzorci pod `Module08/samples` s mapama označenim brojem sesije
  - Premješten Chainlit app u `samples/04`
  - Premješteni agenti u `samples/05` i dodani `__init__.py` za rješavanje paketa

### Dokumentacija
- Sadržaj sesije Module 08 i svi README-ovi uzoraka obogaćeni referencama Microsoft Learn i pouzdanih dobavljača
- `Module08/README.md` ažuriran s pregledom uzoraka, konfiguracijom usmjerivača i savjetima za provjeru
- `Module07/README.md` Windows Foundry Local sekcija potvrđena prema Learn dokumentaciji
- `STUDY_GUIDE.md` ažuriran:
  - Dodan Module 08 u pregled, rasporede, praćenje napretka
  - Dodan detaljan odjeljak Referenci (Foundry Local, Azure AI, Olive, ONNX Runtime, OpenVINO, MLX, Llama.cpp, vLLM, Ollama, AI Toolkit, Windows ML)

---

## Povijesno (sažetak)
- Uspostavljena arhitektura tečaja i moduli (Moduli 01–07)
- Postupna modernizacija sadržaja, standardizacija formata i dodavanje studija slučaja
- Prošireno pokriće okvira za optimizaciju (Llama.cpp, Olive, OpenVINO, Apple MLX)

## Nereleasani / Zaostatak (prijedlozi)
- Opcionalni smoke testovi po uzorcima za provjeru dostupnosti Foundry Local
- Pregled prijevoda radi usklađivanja referenci na modele (npr. `phi-4-mini`) gdje je prikladno
- Dodati minimalnu pyright konfiguraciju za timove koji preferiraju strožu kontrolu na razini radnog prostora

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
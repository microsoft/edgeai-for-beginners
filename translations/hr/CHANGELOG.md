# Dnevnik promjena

Sve značajne promjene u EdgeAI za početnike dokumentirane su ovdje. Ovaj projekt koristi unos temeljen na datumima i stil "Keep a Changelog" (Dodano, Promijenjeno, Popravljeno, Uklonjeno, Dokumentacija, Premješteno).

## 2025-10-30

### Dodano - Sveobuhvatno poboljšanje za Module06 AI Agents
- **Integracija Microsoft Agent Frameworka** (`Module06/01.IntroduceAgent.md`):
  - Kompletan odjeljak o Microsoft Agent Frameworku za razvoj agenata spremnih za produkciju
  - Detaljni obrasci integracije s Foundry Local za implementaciju na rubnim uređajima
  - Primjeri orkestracije više agenata sa specijaliziranim SLM modelima
  - Obrasci implementacije u poduzećima s upravljanjem resursima i praćenjem
  - Sigurnosne i usklađenosti značajke za sustave agenata na rubnim uređajima
  - Primjeri stvarne primjene (maloprodaja, zdravstvo, korisnička podrška)

- **Strategije implementacije SLM agenata u produkciji**:
  - **Foundry Local**: Kompletna dokumentacija za AI runtime na razini poduzeća s instalacijom, konfiguracijom i obrascima za produkciju
  - **Ollama**: Poboljšana implementacija usmjerena na zajednicu s detaljnim praćenjem i upravljanjem modelima
  - **VLLM**: Motor za inferenciju visokih performansi s naprednim tehnikama optimizacije i značajkama za poduzeća
  - Popisi za provjeru implementacije u produkciji i usporedne tablice za sve tri platforme

- **Poboljšanja za SLM okvire optimizirane za rubne uređaje**:
  - **ONNX Runtime**: Novi sveobuhvatni odjeljak za implementaciju SLM agenata na više platformi
  - Univerzalni obrasci implementacije za Windows, Linux, macOS, iOS i Android
  - Opcije hardverske akceleracije (CPU, GPU, NPU) s automatskim otkrivanjem
  - Značajke spremne za produkciju i optimizacije specifične za agente
  - Kompletni primjeri implementacije s integracijom Microsoft Agent Frameworka

- **Reference i dodatna literatura**:
  - Sveobuhvatna biblioteka resursa s više od 100 autoritativnih izvora
  - Osnovni istraživački radovi o AI agentima i malim jezičnim modelima
  - Službena dokumentacija za sve glavne okvire i alate
  - Industrijska izvješća, analize tržišta i tehnički pokazatelji
  - Obrazovni resursi, konferencije i forumi zajednice
  - Standardi, specifikacije i okviri za usklađenost

### Promijenjeno - Modernizacija sadržaja Module06
- **Poboljšani ciljevi učenja**: Dodano ovladavanje Microsoft Agent Frameworkom i sposobnosti implementacije na rubnim uređajima
- **Fokus na produkciju**: Prijelaz s konceptualnih na smjernice spremne za implementaciju s primjerima iz produkcije
- **Primjeri koda**: Ažurirani svi primjeri za korištenje modernih SDK obrazaca i najboljih praksi
- **Obrasci arhitekture**: Dodane hijerarhijske arhitekture agenata i koordinacija rubnih uređaja s oblakom
- **Optimizacija performansi**: Poboljšano s preporukama za upravljanje resursima i automatsko skaliranje

### Dokumentacija - Poboljšanje strukture Module06
- **Sveobuhvatna pokrivenost Agent Frameworka**: Od osnovnih pojmova do implementacije u poduzećima
- **Strategije implementacije u produkciji**: Kompletni vodiči za Foundry Local, Ollama i VLLM
- **Optimizacija na više platformi**: Dodan ONNX Runtime za univerzalnu implementaciju
- **Biblioteka resursa**: Opsežne reference za kontinuirano učenje i implementaciju

### Dodano - Ažuriranje dokumentacije za Module06 Model Context Protocol (MCP)
- **Modernizacija uvoda u MCP** (`Module06/03.IntroduceMCP.md`):
  - Ažurirano s najnovijim MCP specifikacijama s modelcontextprotocol.io (verzija 2025-06-18)
  - Dodana službena analogija USB-C za standardizirane AI aplikacijske veze
  - Ažuriran odjeljak arhitekture s službenim dizajnom u dva sloja (sloj podataka + sloj prijenosa)
  - Poboljšana dokumentacija osnovnih primitiva s primitivima za server (Alati, Resursi, Upiti) i primitivima za klijente (Uzorci, Elicitacija, Zapisivanje)

- **Sveobuhvatne MCP reference i resursi**:
  - Dodana poveznica **MCP za početnike** (https://aka.ms/mcp-for-beginners)
  - Službena MCP dokumentacija i specifikacije (modelcontextprotocol.io)
  - Resursi za razvoj uključujući MCP Inspector i referentne implementacije
  - Tehnički standardi (JSON-RPC 2.0, JSON Schema, OpenAPI, Server-Sent Events)

### Dodano - Integracija Qualcomm QNN u Module04
- **Novi odjeljak 7: Qualcomm QNN Optimization Suite** (`Module04/05.QualcommQNN.md`):
  - Sveobuhvatan vodič od 400+ linija koji pokriva Qualcommov ujedinjeni okvir za AI inferenciju
  - Detaljno pokrivanje heterogene obrade (Hexagon NPU, Adreno GPU, Kryo CPU)
  - Optimizacija svjesna hardvera za Snapdragon platforme s inteligentnom raspodjelom opterećenja
  - Napredne tehnike kvantizacije (INT8, INT16, mješovita preciznost) za mobilnu implementaciju
  - Optimizacija inferencije s niskom potrošnjom energije za uređaje na baterije i aplikacije u stvarnom vremenu
  - Kompletan vodič za instalaciju s postavkama QNN SDK-a i konfiguracijom okruženja
  - Praktični primjeri: konverzija PyTorcha u QNN, optimizacija za više backendova, generiranje binarnih konteksta
  - Napredni obrasci korištenja: prilagodba backend konfiguracije, dinamička kvantizacija, profiliranje performansi
  - Sveobuhvatan odjeljak za rješavanje problema i resursi zajednice

- **Poboljšana struktura Module04**:
  - Ažuriran README.md za uključivanje 7 progresivnih odjeljaka (prije 6)
  - Dodan Qualcomm QNN u tablicu usporedbe performansi (5-15x poboljšanje brzine, 50-80% smanjenje memorije)
  - Sveobuhvatni ciljevi učenja za mobilnu AI implementaciju i optimizaciju potrošnje energije

### Promijenjeno - Ažuriranja dokumentacije za Module04
- **Poboljšanje dokumentacije za Microsoft Olive** (`Module04/03.MicrosoftOlive.md`):
  - Dodan sveobuhvatan odjeljak "Olive Recipes Repository" koji pokriva 100+ unaprijed izgrađenih recepata za optimizaciju
  - Detaljno pokrivanje podržanih obitelji modela (Phi, Llama, Qwen, Gemma, Mistral, DeepSeek)
  - Praktični primjeri korištenja za prilagodbu recepata i doprinose zajednici
  - Poboljšano s pokazateljima performansi i smjernicama za integraciju

- **Promjena redoslijeda odjeljaka u Module04**:
  - Apple MLX premješten u odjeljak 5 (prije odjeljak 6)
  - Workflow Synthesis premješten u odjeljak 6 (prije odjeljak 7)  
  - Qualcomm QNN postavljen kao odjeljak 7 (specijalizirani fokus na mobilne/rubne uređaje)
  - Ažurirane sve reference na datoteke i navigacijske poveznice u skladu s tim

### Popravljeno - Validacija uzoraka za radionicu
- **chat_bootstrap.py validacija i popravak**:
  - Popravljena oštećena naredba za uvoz (`util.util.workshop_utils` → `util.workshop_utils`)
  - Kreiran nedostajući `__init__.py` u paketu util za pravilno rješavanje Python modula
  - Instalirane potrebne ovisnosti (openai, foundry-local-sdk) u conda okruženju
  - Uspješno validirano izvršavanje uzorka s zadanim i prilagođenim upitima
  - Potvrđena integracija s Foundry Local uslugom i učitavanje modela (phi-4-mini s CUDA optimizacijom)

### Dokumentacija - Sveobuhvatna ažuriranja vodiča
- **Kompletna restrukturacija README.md za Module04**:
  - Dodan Qualcomm QNN kao glavni okvir za optimizaciju uz OpenVINO, Olive, MLX
  - Ažurirani ciljevi učenja poglavlja za uključivanje mobilne AI implementacije i optimizacije potrošnje energije
  - Poboljšana tablica usporedbe performansi s QNN pokazateljima i slučajevima korištenja za mobilne/rubne uređaje
  - Održan logičan napredak od rješenja za poduzeća do optimizacija specifičnih za platformu

- **Unakrsne reference i navigacija**:
  - Ažurirane sve interne poveznice i reference na datoteke za novi redoslijed odjeljaka
  - Poboljšan opis Workflow Synthesis za uključivanje mobilnih, desktop i cloud okruženja
  - Dodane sveobuhvatne poveznice na resurse za Qualcommov razvojni ekosustav

## 2025-10-08

### Dodano - Sveobuhvatno ažuriranje radionice
- **Kompletno prepisivanje README.md za radionicu**:
  - Dodan sveobuhvatan uvod koji objašnjava vrijednost Edge AI-a (privatnost, performanse, trošak)
  - Kreirano 6 osnovnih ciljeva učenja s detaljnim kompetencijama
  - Dodana tablica ishoda učenja s isporukama i matricom kompetencija
  - Uključene vještine spremne za karijeru za industrijsku relevantnost
  - Dodan vodič za brzi početak s preduvjetima i 3 koraka za postavljanje
  - Kreirane tablice resursa za Python uzorke (8 datoteka s vremenima izvršavanja)
  - Dodana tablica Jupyter bilježnica (8 bilježnica s ocjenama težine)
  - Kreirana tablica dokumentacije (7 ključnih dokumenata s "Kada koristiti" smjernicama)
  - Dodane preporuke za put učenja za različite razine vještina

- **Validacija i testiranje infrastrukture radionice**:
  - Kreiran `scripts/validate_samples.py` - Sveobuhvatan alat za validaciju sintakse, uvoza i najboljih praksi
  - Kreiran `scripts/test_samples.py` - Alat za testiranje svih Python uzoraka
  - Dodana dokumentacija za validaciju u `scripts/README.md`

- **Sveobuhvatna dokumentacija**:
  - Kreiran `SAMPLES_UPDATE_SUMMARY.md` - Detaljan vodič od 400+ linija koji pokriva sva poboljšanja
  - Kreiran `UPDATE_COMPLETE.md` - Izvršni sažetak završetka ažuriranja
  - Kreiran `QUICK_REFERENCE.md` - Brza referentna kartica za radionicu

### Promijenjeno - Modernizacija Python uzoraka za radionicu
- **Ažurirano svih 8 Python uzoraka s najboljim praksama**:
  - Poboljšano rukovanje greškama s try-except blokovima oko svih I/O operacija
  - Dodani tipovi podataka i sveobuhvatni docstringovi
  - Implementiran dosljedan obrazac zapisivanja [INFO]/[ERROR]/[RESULT]
  - Zaštićeni opcionalni uvozi s naznakama za instalaciju
  - Poboljšana povratna informacija korisnicima kroz sve uzorke

- **session01/chat_bootstrap.py**:
  - Poboljšana inicijalizacija klijenta s detaljnim porukama o greškama
  - Poboljšano rukovanje greškama u streamingu s validacijom dijelova
  - Dodano bolje rukovanje iznimkama za nedostupnost usluge

- **session02/rag_pipeline.py**:
  - Dodani zaštitni mehanizmi za sentence-transformers s naznakama za instalaciju
  - Poboljšano rukovanje greškama za operacije ugrađivanja i generiranja
  - Poboljšano formatiranje izlaza sa strukturiranim rezultatima

- **session02/rag_eval_ragas.py**:
  - Zaštićeni opcionalni uvozi (ragas, datasets) s korisnički prilagođenim porukama o greškama
  - Dodano rukovanje greškama za evaluacijske metrike
  - Poboljšano formatiranje izlaza za evaluacijske rezultate

- **session03/benchmark_oss_models.py**:
  - Implementirano graciozno degradiranje (nastavlja se na neuspjeh modela)
  - Dodano detaljno izvještavanje o napretku i rukovanje greškama po modelu
  - Poboljšano izračunavanje statistike s sveobuhvatnim oporavkom od grešaka

- **session04/model_compare.py**:
  - Dodani tipovi podataka (Tuple povratni tipovi)
  - Poboljšano formatiranje izlaza sa strukturiranim JSON rezultatima
  - Implementirano rukovanje greškama po modelu s oporavkom

- **session05/agents_orchestrator.py**:
  - Poboljšano Agent.act() s sveobuhvatnim docstringovima
  - Dodano rukovanje greškama u pipelineu s zapisivanjem po fazama
  - Poboljšano upravljanje memorijom i praćenje stanja

- **session06/models_router.py**:
  - Poboljšana dokumentacija funkcija za sve komponente usmjeravanja
  - Dodano detaljno zapisivanje u funkciji route()
  - Poboljšan testni izlaz sa strukturiranim rezultatima

- **session06/models_pipeline.py**:
  - Dodano rukovanje greškama u pomoćnoj funkciji chat()
  - Poboljšano pipeline() s zapisivanjem faza i izvještavanjem o napretku
  - Poboljšano main() s sveobuhvatnim oporavkom od grešaka

### Dokumentacija - Poboljšanje dokumentacije za radionicu
- Ažuriran glavni README.md s odjeljkom radionice koji ističe praktični put učenja
- Poboljšan STUDY_GUIDE.md s sveobuhvatnim odjeljkom radionice uključujući:
  - Ciljeve učenja i fokusna područja studija
  - Pitanja za samoprocjenu
  - Praktične vježbe s procjenama vremena
  - Dodijeljeno vrijeme za koncentrirano i povremeno učenje
  - Dodana radionica u predložak za praćenje napretka
- Ažuriran vodič za dodjelu vremena s 20 sati na 30 sati (uključujući radionicu)
- Dodani opisi uzoraka radionice i ishodi učenja u README

### Popravljeno
- Riješeni nedosljedni obrasci rukovanja greškama u uzorcima radionice
- Popravljene greške u opcionalnim uvozima s odgovarajućim zaštitama
- Ispravljeni nedostajući tipovi podataka u ključnim funkcijama
- Riješena nedovoljna povratna informacija korisnicima u scenarijima grešaka
- Popravljeni problemi validacije s sveobuhvatnom infrastrukturom za testiranje

---

## 2025-09-23

### Promijenjeno - Velika modernizacija Module 08
- **Sveobuhvatno usklađivanje s obrascima Microsoft Foundry-Local repozitorija**
  - Ažurirani svi primjeri koda za korištenje modernog `FoundryLocalManager` i OpenAI SDK integracije
  - Zamijenjeni zastarjeli ručni pozivi `requests` s pravilnim korištenjem SDK-a
  - Usklađeni obrasci implementacije sa službenom Microsoft dokumentacijom i uzorcima

- **Modernizacija 05.AIPoweredAgents.md**:
  - Ažurirana orkestracija više agenata za korištenje modernih SDK obrazaca
  - Poboljšana implementacija koordinatora s naprednim značajkama (povratne petlje, praćenje performansi)
  - Dodano sveobuhvatno rukovanje greškama i provjera zdravlja usluge
  - Integrirane odgovarajuće reference na lokalne uzorke (`samples/05/multi_agent_orchestration.ipynb`)
  - Ažurirani primjeri poziva funkcija za korištenje modernog parametra `tools` umjesto zastarjelog `functions`
  - Dodani obrasci spremni za produkciju s praćenjem i statističkim praćenjem
- Izvedivi primjeri pod `Module08/samples/01`–`06` s Windows cmd uputama
  - `01` REST brzi chat (`chat_quickstart.py`)
  - `02` SDK brzi početak s OpenAI/Foundry Local i podrškom za Azure OpenAI (`sdk_quickstart.py`)
  - `03` CLI popis i testiranje (`list_and_bench.cmd`)
  - `04` Chainlit demo (`app.py`)
  - `05` Orkestracija više agenata (`python -m samples.05.agents.coordinator`)
  - `06` Router za modele-kao-alate (`router.py`)
- Podrška za Azure OpenAI u uzorku SDK-a iz Sesije 2 s konfiguracijom varijabli okruženja
- `.vscode/settings.json` usmjeren na `Module08/.venv` za poboljšanje rezolucije Python analize
- `.env` s naznakom `PYTHONPATH` za svijest VS Code/Pylance-a

### Promijenjeno
- Zadani model ažuriran na `phi-4-mini` u cijeloj dokumentaciji i uzorcima Module 08; uklonjena preostala spominjanja `phi-3.5` unutar Module 08
- Poboljšanja routera (`Module08/samples/06/router.py`):
  - Otkrivanje krajnjih točaka putem `foundry service status` s regex analizom
  - Provjera zdravlja `/v1/models` pri pokretanju
  - Registracija modela konfigurabilna putem varijabli okruženja (`GENERAL_MODEL`, `REASONING_MODEL`, `CODE_MODEL`, `TOOL_REGISTRY` JSON)
- Ažurirani zahtjevi: `Module08/requirements.txt` sada uključuje `openai` (uz `requests`, `chainlit`)
- Pojašnjene upute za Chainlit uzorke i dodano rješavanje problema; rezolucija uvoza putem postavki radnog prostora

### Ispravljeno
- Riješeni problemi s uvozom:
  - Router više ne ovisi o nepostojećem modulu `utils`; funkcije su integrirane
  - Koordinator koristi relativni uvoz (`from .specialists import ...`) i pokreće se putem putanje modula
  - Konfiguracija VS Code/Pylance za rješavanje uvoza `chainlit` i paketa
- Ispravljena manja tipografska greška u `STUDY_GUIDE.md` i dodana pokrivenost Module 08

### Uklonjeno
- Izbrisano neiskorišteno `Module08/infra/obs.py` i uklonjen prazan direktorij `infra/`; obrasci za promatranje zadržani kao opcionalni u dokumentaciji

### Premješteno
- Konsolidirani demo primjeri Module 08 pod `Module08/samples` s mapama numeriranim po sesijama
  - Chainlit aplikacija premještena u `samples/04`
  - Agenti premješteni u `samples/05` i dodani `__init__.py` datoteke za rezoluciju paketa

### Dokumentacija
- Dokumentacija sesije Module 08 i svi README uzorci obogaćeni referencama na Microsoft Learn i pouzdane dobavljače
- `Module08/README.md` ažuriran s Pregledom uzoraka, konfiguracijom routera i savjetima za validaciju
- `Module07/README.md` sekcija Windows Foundry Local potvrđena prema Learn dokumentaciji
- `STUDY_GUIDE.md` ažuriran:
  - Dodan Module 08 u pregled, raspored, praćenje napretka
  - Dodan sveobuhvatan odjeljak Referenci (Foundry Local, Azure AI, Olive, ONNX Runtime, OpenVINO, MLX, Llama.cpp, vLLM, Ollama, AI Toolkit, Windows ML)

---

## Povijesno (sažetak)
- Arhitektura tečaja i moduli uspostavljeni (Module 01–07)
- Iterativna modernizacija sadržaja, standardizacija formatiranja i dodane studije slučaja
- Proširena pokrivenost okvira za optimizaciju (Llama.cpp, Olive, OpenVINO, Apple MLX)

## Neobjavljeno / Zaostaci (prijedlozi)
- Opcionalni testovi za svaki uzorak za provjeru dostupnosti Foundry Local
- Pregled prijevoda za usklađivanje referenci modela (npr. `phi-4-mini`) gdje je primjenjivo
- Dodavanje minimalne konfiguracije pyright ako timovi preferiraju strogoću na razini radnog prostora

---

**Izjava o odricanju odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane čovjeka. Ne preuzimamo odgovornost za nesporazume ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.
# Jurnal de modificări

Toate modificările notabile pentru EdgeAI pentru Începători sunt documentate aici. Acest proiect folosește înregistrări bazate pe dată și stilul Keep a Changelog (Adăugat, Modificat, Reparat, Eliminat, Documentație, Mutat).

## 2025-10-30

### Adăugat - Modul06 Îmbunătățirea cuprinzătoare a Agenților AI
- **Integrarea Microsoft Agent Framework** (`Module06/01.IntroduceAgent.md`):
  - Secțiune completă despre Microsoft Agent Framework pentru dezvoltarea de agenți pregătiți pentru producție
  - Modele detaliate de integrare cu Foundry Local pentru implementare la margine
  - Exemple de orchestrare multi-agent cu modele SLM specializate
  - Modele de implementare enterprise cu gestionarea și monitorizarea resurselor
  - Funcționalități de securitate și conformitate pentru sistemele de agenți la margine
  - Exemple reale de implementare (retail, sănătate, servicii pentru clienți)

- **Strategii de implementare SLM în producție**:
  - **Foundry Local**: Documentație completă de nivel enterprise pentru runtime AI la margine cu instalare, configurare și modele de producție
  - **Ollama**: Implementare îmbunătățită, orientată spre comunitate, cu monitorizare cuprinzătoare și gestionare a modelelor
  - **VLLM**: Motor de inferență performant cu tehnici avansate de optimizare și caracteristici enterprise
  - Liste de verificare pentru implementare în producție și tabele de comparație pentru toate cele trei platforme

- **Îmbunătățiri ale cadrelor SLM optimizate pentru margine**:
  - **ONNX Runtime**: Nouă secțiune cuprinzătoare pentru implementarea agenților SLM cross-platform
  - Modele universale de implementare pe Windows, Linux, macOS, iOS și Android
  - Opțiuni de accelerare hardware (CPU, GPU, NPU) cu detectare automată
  - Funcții pregătite pentru producție și optimizări specifice agenților
  - Exemple complete de implementare cu integrarea Microsoft Agent Framework

- **Referințe și resurse suplimentare**:
  - Bibliotecă de resurse cuprinzătoare cu peste 100 de surse autorizate
  - Articole de cercetare esențiale despre agenții AI și Modele de Limbaj Mici
  - Documentație oficială pentru toate cadrele și uneltele majore
  - Rapoarte din industrie, analize de piață și benchmark-uri tehnice
  - Resurse educaționale, conferințe și forumuri ale comunității
  - Standarde, specificații și cadre de conformitate

### Modificat - Modernizarea conținutului Modul06
- **Obiective de învățare îmbunătățite**: Adăugat stăpânirea Microsoft Agent Framework și capabilități de implementare la margine
- **Focus pe producție**: Deplasat de la concepte către ghidare pregătită pentru implementare cu exemple de producție
- **Exemple de cod**: Actualizat toate exemplele utilizând modele SDK moderne și bune practici
- **Modele de arhitectură**: Adăugat arhitecturi ierarhice ale agenților și coordonare edge-to-cloud
- **Optimizare performanță**: Îmbunătățit cu gestionarea resurselor și recomandări de scalare automată

### Documentație - Îmbunătățirea structurii Modul06
- **Acoperire cuprinzătoare a Agent Framework**: De la concepte de bază la implementare enterprise
- **Strategii de implementare în producție**: Ghiduri complete pentru Foundry Local, Ollama și VLLM
- **Optimizare cross-platform**: Adăugat ONNX Runtime pentru implementare universală
- **Bibliotecă de resurse**: Referințe extinse pentru învățare și implementare continuă

### Adăugat - Actualizare Documentație Model Context Protocol (MCP) Modul06
- **Modernizarea introducerii MCP** (`Module06/03.IntroduceMCP.md`):
  - Actualizat cu cele mai recente specificații MCP de la modelcontextprotocol.io (versiunea 2025-06-18)
  - Adăugată analogia oficială USB-C pentru conexiuni AI standardizate
  - Secțiunea de arhitectură actualizată cu design oficial în două niveluri (Layer Date + Layer Transport)
  - Documentație îmbunătățită a primitivelor de bază cu primitive server (Unelte, Resurse, Prompts) și primitive client (Eșantionare, Elicitație, Logare)

- **Referințe și resurse cuprinzătoare MCP**:
  - Adăugat linkul **MCP pentru Începători** (https://aka.ms/mcp-for-beginners) 
  - Documentația oficială MCP și specificațiile (modelcontextprotocol.io)
  - Resurse de dezvoltare incluzând MCP Inspector și implementări de referință
  - Standarde tehnice (JSON-RPC 2.0, JSON Schema, OpenAPI, Server-Sent Events)


### Adăugat - Integrarea Qualcomm QNN Modul04
- **Noua Secțiune 7: Suita de Optimizare Qualcomm QNN** (`Module04/05.QualcommQNN.md`):
  - Ghid complet de peste 400 de linii acoperind cadrul unificat Qualcomm pentru inferență AI
  - Acoperire detaliată a calculului eterogen (Hexagon NPU, Adreno GPU, Kryo CPU)
  - Optimizare conștientă de hardware pentru platformele Snapdragon cu distribuție inteligentă a sarcinilor
  - Tehnici avansate de cuantizare (INT8, INT16, precizie mixtă) pentru implementare mobilă
  - Optimizare eficientă a consumului energetic pentru dispozitive pe baterie și aplicații în timp real
  - Ghid complet de instalare cu configurare QNN SDK și mediu
  - Exemple practice: conversia PyTorch la QNN, optimizare multi-backend, generare binară a contextului
  - Modele avansate de utilizare: configurare backend personalizat, cuantizare dinamică, profilare performanță
  - Secțiune cuprinzătoare de depanare și resurse comunitare

- **Structură îmbunătățită Modul04**:
  - Actualizat README.md pentru a include 7 secțiuni progresive (era 6)
  - Adăugat Qualcomm QNN în tabelul benchmark-urilor de performanță (îmbunătățire viteză 5-15x, reducere memorie 50-80%)
  - Rezultate de învățare cuprinzătoare pentru implementare AI mobilă și optimizare energetică

### Modificat - Actualizări Documentație Modul04
- **Îmbunătățire documentație Microsoft Olive** (`Module04/03.MicrosoftOlive.md`):
  - Adăugată secțiune cuprinzătoare „Olive Recipes Repository” acoperind 100+ rețete de optimizare predefinite
  - Acoperire detaliată a familiilor de modele suportate (Phi, Llama, Qwen, Gemma, Mistral, DeepSeek)
  - Exemple practice de personalizare a rețetelor și contribuții comunitare
  - Îmbunătățit cu benchmark-uri de performanță și ghid de integrare

- **Reordonarea secțiunilor în Modul04**:
  - Apple MLX mutat în Secțiunea 5 (era Secțiunea 6)
  - Workflow Synthesis mutat în Secțiunea 6 (era Secțiunea 7)  
  - Qualcomm QNN poziționat ca Secțiunea 7 (focus specializat mobil/margine)
  - Actualizate toate referințele de fișiere și linkurile de navigare corespunzător

### Reparat - Validarea mostrelor din Workshop
- **Validare și reparare chat_bootstrap.py**:
  - Reparată instrucțiunea de import coruptă (`util.util.workshop_utils` → `util.workshop_utils`)
  - Creat fișierul `__init__.py` lipsă în pachetul util pentru rezoluția corectă a modulului Python
  - Instalate dependențele necesare (openai, foundry-local-sdk) în mediul conda
  - Validată cu succes executarea mostrei cu prompturi implicite și personalizate
  - Confirmată integrarea cu serviciul Foundry Local și încărcarea modelului (phi-4-mini cu optimizare CUDA)

### Documentație - Actualizări Ghid cuprinzător
- **Restructurare completă README.md Modul04**:
  - Adăugat Qualcomm QNN ca cadru principal de optimizare alături de OpenVINO, Olive, MLX
  - Actualizate rezultatele de învățare din capitole pentru includerea implementării AI mobile și optimizării energetice
  - Tabel de comparație a performanțelor îmbunătățit cu metrici QNN și cazuri de utilizare mobil/margine
  - Menținută progresia logică de la soluții enterprise la optimizări specifice platformei

- **Coreferințe și navigare**:
  - Actualizate toate linkurile interne și referințele de fișiere pentru noua numerotare a secțiunilor
  - Descrierea workflow synthesis extinsă pentru a include medii mobile, desktop și cloud
  - Adăugate linkuri cuprinzătoare către ecosistemul de dezvoltatori Qualcomm

## 2025-10-08

### Adăugat - Actualizare cuprinzătoare Workshop
- **Rescriere completă README.md Workshop**:
  - Adăugată introducere cuprinzătoare explicând propunerea de valoare Edge AI (confidențialitate, performanță, cost)
  - Creat 6 obiective de învățare de bază cu competențe detaliate
  - Adăugată tabel cu rezultate de învățare cu livrabile și matricea competențelor
  - Inclusă secțiune de abilități gata de carieră pentru relevanța în industrie
  - Adăugat ghid rapid de pornire cu prerechizite și configurare în 3 pași
  - Creat tabele de resurse pentru mostre Python (8 fișiere cu timpi de rulare)
  - Adăugat tabel cu caiete Jupyter (8 caiete cu niveluri de dificultate)
  - Creat tabel de documentație (7 documente cheie cu ghid „Folosește când”)
  - Adăugate recomandări de traseu de învățare pentru diferite niveluri de competență

- **Infrastructură de validare și testare Workshop**:
  - Creat `scripts/validate_samples.py` - Instrument cuprinzător de validare pentru sintaxă, importuri și bune practici
  - Creat `scripts/test_samples.py` - Rulare teste fum pentru toate mostrele Python
  - Adăugată documentație de validare în `scripts/README.md`

- **Documentație cuprinzătoare**:
  - Creat `SAMPLES_UPDATE_SUMMARY.md` - Ghid detaliat de peste 400 de linii acoperind toate îmbunătățirile
  - Creat `UPDATE_COMPLETE.md` - Rezumat executiv al finalizării actualizării
  - Creat `QUICK_REFERENCE.md` - Foaie de referință rapidă pentru Workshop

### Modificat - Modernizarea mostrelor Python Workshop
- **Toate cele 8 mostre Python actualizate cu bune practici**:
  - Gestionare îmbunătățită a erorilor cu blocuri try-except în jurul tuturor operațiunilor I/O
  - Adăugate indicații de tip și docstring-uri cuprinzătoare
  - Implementat model constant de logare [INFO]/[ERROR]/[RESULT]
  - Importuri opționale protejate cu indicații de instalare
  - Feedback îmbunătățit pentru utilizator în toate mostrele

- **session01/chat_bootstrap.py**:
  - Inițializare client îmbunătățită cu mesaje detaliate de eroare
  - Gestionare îmbunătățită a erorilor de streaming cu validarea secvențelor
  - Gestionare mai bună a excepțiilor pentru indisponibilitatea serviciului

- **session02/rag_pipeline.py**:
  - Adăugate protecții la importul sentence-transformers cu indicații de instalare
  - Gestionare îmbunătățită a erorilor pentru operațiunile de embedding și generare
  - Format de ieșire îmbunătățit cu rezultate structurate

- **session02/rag_eval_ragas.py**:
  - Importuri opționale protejate (ragas, datasets) cu mesaje prietenoase de eroare
  - Adăugată gestionare a erorilor pentru metricile de evaluare
  - Format de ieșire îmbunătățit pentru rezultatele de evaluare

- **session03/benchmark_oss_models.py**:
  - Implementată degradare grațioasă (continuă la eșecuri ale modelului)
  - Adăugat raport de progres detaliat și gestionare erori per model
  - Calcul statistici îmbunătățit cu recuperare cuprinzătoare a erorilor

- **session04/model_compare.py**:
  - Adăugate indicații de tip (tuple ca tipuri de retur)
  - Format de ieșire îmbunătățit cu rezultate JSON structurate
  - Implementată gestionare erori per model cu recuperare

- **session05/agents_orchestrator.py**:
  - Agent.act() îmbunătățit cu docstring-uri cuprinzătoare
  - Gestionare a erorilor în pipeline adăugată cu logare etapizată
  - Gestionare îmbunătățită a memoriei și urmărirea stării

- **session06/models_router.py**:
  - Documentația funcțiilor îmbunătățită pentru toate componentele de rutare
  - Logare detaliată adăugată în funcția route()
  - Ieșire de test îmbunătățită cu rezultate structurate

- **session06/models_pipeline.py**:
  - Gestionare erori adăugată la funcția helper chat()
  - pipeline() îmbunătățit cu logare etapizată și raportare progres
  - main() îmbunătățit cu recuperare completă la erori

### Documentație - Îmbunătățire Documentație Workshop
- Actualizat README.md principal cu secțiunea Workshop evidențiind traseul de învățare practică
- Îmbunătățit STUDY_GUIDE.md cu secțiunea cuprinzătoare Workshop incluzând:
  - Obiective de învățare și domenii de concentrare
  - Întrebări de autoevaluare
  - Exerciții practice cu estimări de timp
  - Alocare de timp pentru studiu concentrat și part-time
  - Adăugat Workshop la șablonul de urmărit progresul
- Ghidul de alocare a timpului actualizat de la 20 ore la 30 ore (inclusiv Workshop)
- Adăugate descrieri mostre Workshop și rezultate de învățare în README

### Reparat
- Rezolvat tipare inconsistente de gestionare a erorilor în mostrele Workshop
- Reparat erori la importuri dependențe opționale cu protecții adecvate
- Corectat lipsa indicațiilor de tip în funcții critice
- Îmbunătățit feedback-ul utilizatorului în scenarii de eroare
- Rezolvat probleme de validare cu infrastructură cuprinzătoare de testare

---

## 2025-09-23

### Modificat - Modernizare majoră Modul 08
- **Aliniere cuprinzătoare cu modelele de depozit Foundry-Local Microsoft**
  - Actualizate toate exemplele de cod pentru a folosi integrarea modernă `FoundryLocalManager` și SDK OpenAI
  - Înlocuite apeluri manuale `requests` învechite cu utilizare adecvată a SDK-ului
  - Alinieri ale modelelor de implementare cu documentația și mostrele oficiale Microsoft

- **Modernizarea 05.AIPoweredAgents.md**:
  - Actualizată orchestrarea multi-agent pentru a folosi modele SDK moderne
  - Îmbunătățită implementarea coordonatorului cu funcții avansate (buclă de feedback, monitorizare performanță)
  - Adăugată gestionare cuprinzătoare a erorilor și verificare stare serviciu
  - Integrare referințe corecte către mostre locale (`samples/05/multi_agent_orchestration.ipynb`)
  - Actualizate exemplele de apelare funcții pentru a folosi parametrul modern `tools` în loc de `functions` învechit
  - Adăugate modele pregătite pentru producție cu monitorizare și urmărire statistică

- **Rescriere completă 06.ModelsAsTools.md**:
  - Înlocuit registrul de unelte de bază cu implementarea unui router inteligent de modele
  - Adăugată selecție bazată pe cuvinte cheie pentru diferite tipuri de sarcini (general, raționament, cod, creativ)
  - Integrată configurarea bazată pe mediu cu alocare flexibilă a modelelor
  - Îmbunătățit cu monitorizare cuprinzătoare a stării serviciului și gestionare a erorilor
  - Adăugate modele de implementare pentru producție cu monitorizarea cererilor și urmărirea performanței
  - Aliniat cu implementarea locală în `samples/06/router.py` și `samples/06/model_router.ipynb`

- **Îmbunătățiri structură documentație**:
  - Adăugate secțiuni de prezentare evidențiind modernizarea și alinierea SDK
  - Îmbunătățit cu emoji-uri și formatare mai bună pentru lizibilitate
  - Adăugate referințe corecte către fișierele locale de mostre în documentație
  - Inclus ghidare pentru implementare pregătită pentru producție și bune practici

### Adăugat
- Secțiuni cuprinzătoare de prezentare în fișierele Modul 08 evidențiind integrarea SDK modernă
- Aspecte arhitecturale care prezintă caracteristici avansate (sisteme multi-agent, rutare inteligentă)
- Referințe directe către implementările mostrelor locale pentru experiență practică
- Ghiduri de implementare în producție cu modele de monitorizare și gestionare a erorilor
- Exemple interactive în caiete Jupyter cu funcții avansate și benchmark-uri

### Reparat
- Discrepanțe de aliniere între documentație și implementările reale de mostre
- Modele SDK învechite utilizate încă în Modul 08
- Lipsa referințelor la biblioteca cuprinzătoare locală de mostre
- Abordări inconsistente de implementare între secțiuni diferite

---

## 2025-09-18

### Adăugat
- Modul 08: Microsoft Foundry Local – Trusă completă pentru dezvoltatori
  - Șase sesiuni: configurare, integrare Azure AI Foundry, modele open-source, demo-uri avansate, agenți și modele ca unelte
  - Mostre funcționale sub `Module08/samples/01`–`06` cu instrucțiuni Windows cmd
    - `01` chat rapid REST (`chat_quickstart.py`)

    - `02` SDK quickstart cu suport OpenAI/Foundry Local și Azure OpenAI (`sdk_quickstart.py`)
    - `03` CLI listare și benchmark (`list_and_bench.cmd`)
    - `04` Demo Chainlit (`app.py`)
    - `05` Orchestrare multi-agent (`python -m samples.05.agents.coordinator`)
    - `06` Router modele ca unelte (`router.py`)
- Suport Azure OpenAI în exemplul Session 2 SDK cu configurare prin variabile de mediu
- `.vscode/settings.json` actualizat pentru a indica `Module08/.venv` și a îmbunătăți analiza Python
- `.env` cu sugestie `PYTHONPATH` pentru recunoașterea în VS Code/Pylance

### Modificat
- Modelul implicit actualizat la `phi-4-mini` în documentația și exemplele din Modul 08; eliminate mențiuni rămase cu `phi-3.5` în Modul 08
- Îmbunătățiri router (`Module08/samples/06/router.py`):
  - Descoperire endpoint prin `foundry service status` cu parcurgere regex
  - Verificare stare `/v1/models` la pornire
  - Registru modele configurabil prin mediu (`GENERAL_MODEL`, `REASONING_MODEL`, `CODE_MODEL`, `TOOL_REGISTRY` JSON)
- Cerințe actualizate: `Module08/requirements.txt` include acum `openai` (alături de `requests`, `chainlit`)
- Ghid pentru exemplul Chainlit clarificat și adăugat depanare; rezolvarea importurilor prin setările de workspace

### Remediat
- Probleme de import rezolvate:
  - Router nu mai depinde de modulul inexistent `utils`; funcțiile sunt încorporate
  - Coordinator folosește import relativ (`from .specialists import ...`) și se apelează via cale modulului
  - Configurație VS Code/Pylance pentru rezolvarea importurilor `chainlit` și pachete
- Corectat o mică greșeală în `STUDY_GUIDE.md` și adăugat acoperire Modul 08

### Eliminat
- Șters fișierul neutilizat `Module08/infra/obs.py` și eliminat directorul gol `infra/`; modelele de observabilitate păstrate opțional în documentație

### Mutat
- Consolidate demo-urile Modul 08 sub `Module08/samples` cu foldere numerotate după sesiuni
  - Aplicația Chainlit mutată în `samples/04`
  - Agenții mutați în `samples/05` și adăugate fișiere `__init__.py` pentru rezolvarea pachetului

### Documentație
- Documentația Modul 08 și toate README-urile exemplelor îmbogățite cu referințe Microsoft Learn și vânzători de încredere
- Actualizare `Module08/README.md` cu Prezentarea Exemples, configurarea router-ului și sfaturi de validare
- Secțiunea Windows Foundry Local din `Module07/README.md` validată cu documentația Learn
- Actualizat `STUDY_GUIDE.md`:
  - Adăugat Modul 08 în prezentare, programe, tracker de progres
  - Adăugată secțiune cuprinzătoare de Referințe (Foundry Local, Azure AI, Olive, ONNX Runtime, OpenVINO, MLX Apple, Llama.cpp, vLLM, Ollama, AI Toolkit, Windows ML)

---

## Istoric (rezumat)
- Arhitectura cursului și module stabilite (Module 01–07)
- Modernizare iterativă conținut, standardizare formatare și adăugare studii de caz
- Extindere acoperire framework-uri optimizare (Llama.cpp, Olive, OpenVINO, Apple MLX)

## Nepublicate / În așteptare (propuneri)
- Teste opționale de fum per exemplu pentru validarea disponibilității Foundry Local
- Revizuire traduceri pentru alinierea referințelor modelelor (ex: `phi-4-mini`) acolo unde este cazul
- Adăugare config pyright minimal pentru echipele care preferă strictețe la nivel de workspace

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
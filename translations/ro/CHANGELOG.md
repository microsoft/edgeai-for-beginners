# Jurnal de modificări

Toate modificările notabile ale EdgeAI pentru Începători sunt documentate aici. Acest proiect utilizează intrări bazate pe date și stilul Keep a Changelog (Adăugat, Modificat, Reparat, Eliminat, Documentație, Mutat).

## 2025-10-30

### Adăugat - Îmbunătățire cuprinzătoare a Module06 AI Agents
- **Integrarea Microsoft Agent Framework** (`Module06/01.IntroduceAgent.md`):
  - Secțiune completă despre Microsoft Agent Framework pentru dezvoltarea agenților gata de producție
  - Modele detaliate de integrare cu Foundry Local pentru implementarea la margine
  - Exemple de orchestrare multi-agent cu modele SLM specializate
  - Modele de implementare în întreprinderi cu gestionarea resurselor și monitorizare
  - Funcții de securitate și conformitate pentru sistemele de agenți la margine
  - Exemple de implementare în lumea reală (retail, sănătate, servicii pentru clienți)

- **Strategii de implementare a agenților SLM în producție**:
  - **Foundry Local**: Documentație completă pentru runtime AI la margine de nivel enterprise, cu instalare, configurare și modele de producție
  - **Ollama**: Implementare îmbunătățită orientată spre comunitate, cu monitorizare cuprinzătoare și gestionarea modelelor
  - **VLLM**: Motor de inferență de înaltă performanță cu tehnici avansate de optimizare și funcții pentru întreprinderi
  - Liste de verificare pentru implementare în producție și tabele comparative pentru toate cele trei platforme

- **Îmbunătățiri ale cadrelor SLM optimizate pentru margine**:
  - **ONNX Runtime**: Secțiune nouă cuprinzătoare pentru implementarea agenților SLM pe mai multe platforme
  - Modele universale de implementare pe Windows, Linux, macOS, iOS și Android
  - Opțiuni de accelerare hardware (CPU, GPU, NPU) cu detectare automată
  - Funcții gata de producție și optimizări specifice agenților
  - Exemple complete de implementare cu integrarea Microsoft Agent Framework

- **Referințe și lecturi suplimentare**:
  - Bibliotecă cuprinzătoare de resurse cu peste 100 de surse autoritare
  - Lucrări de cercetare de bază despre agenți AI și modele de limbaj mici
  - Documentația oficială pentru toate cadrele și instrumentele majore
  - Rapoarte de industrie, analize de piață și repere tehnice
  - Resurse educaționale, conferințe și forumuri comunitare
  - Standarde, specificații și cadre de conformitate

### Modificat - Modernizarea conținutului Module06
- **Obiective de învățare îmbunătățite**: Adăugarea stăpânirii Microsoft Agent Framework și a capacităților de implementare la margine
- **Focalizare pe producție**: Trecerea de la ghiduri conceptuale la exemple gata de implementare
- **Exemple de cod**: Actualizarea tuturor exemplelor pentru a utiliza modele SDK moderne și cele mai bune practici
- **Modele de arhitectură**: Adăugarea arhitecturilor ierarhice de agenți și coordonarea margine-cloud
- **Optimizare a performanței**: Îmbunătățiri cu recomandări pentru gestionarea resurselor și scalare automată

### Documentație - Îmbunătățirea structurii Module06
- **Acoperire cuprinzătoare a cadrelor de agenți**: De la concepte de bază la implementare în întreprinderi
- **Strategii de implementare în producție**: Ghiduri complete pentru Foundry Local, Ollama și VLLM
- **Optimizare pe mai multe platforme**: Adăugarea ONNX Runtime pentru implementare universală
- **Bibliotecă de resurse**: Referințe extinse pentru învățare continuă și implementare

### Adăugat - Actualizare documentație Protocol Context Model (MCP) Module06
- **Modernizarea introducerii MCP** (`Module06/03.IntroduceMCP.md`):
  - Actualizat cu cele mai recente specificații MCP de pe modelcontextprotocol.io (versiunea 2025-06-18)
  - Adăugarea analogiei oficiale USB-C pentru conexiuni standardizate ale aplicațiilor AI
  - Secțiunea de arhitectură actualizată cu designul oficial pe două straturi (Stratul de Date + Stratul de Transport)
  - Documentație îmbunătățită pentru primitivele de bază cu primitivele serverului (Instrumente, Resurse, Prompts) și primitivele clientului (Sampling, Elicitation, Logging)

- **Referințe și resurse cuprinzătoare MCP**:
  - Adăugat linkul **MCP pentru Începători** (https://aka.ms/mcp-for-beginners)
  - Documentația oficială MCP și specificațiile (modelcontextprotocol.io)
  - Resurse de dezvoltare, inclusiv MCP Inspector și implementări de referință
  - Standarde tehnice (JSON-RPC 2.0, JSON Schema, OpenAPI, Server-Sent Events)

### Adăugat - Integrarea Qualcomm QNN Module04
- **Secțiunea nouă 7: Suita de optimizare Qualcomm QNN** (`Module04/05.QualcommQNN.md`):
  - Ghid cuprinzător de peste 400 de linii care acoperă cadrul unificat de inferență AI al Qualcomm
  - Acoperire detaliată a calculului heterogen (Hexagon NPU, Adreno GPU, Kryo CPU)
  - Optimizare conștientă de hardware pentru platformele Snapdragon cu distribuție inteligentă a sarcinilor
  - Tehnici avansate de cuantizare (INT8, INT16, precizie mixtă) pentru implementare mobilă
  - Optimizare eficientă din punct de vedere energetic pentru dispozitive alimentate cu baterii și aplicații în timp real
  - Ghid complet de instalare cu configurarea SDK QNN și configurarea mediului
  - Exemple practice: conversia PyTorch în QNN, optimizarea multi-backend, generarea de binare contextuale
  - Modele avansate de utilizare: configurare backend personalizată, cuantizare dinamică, profilare performanță
  - Secțiune cuprinzătoare de depanare și resurse comunitare

- **Structura îmbunătățită Module04**:
  - README.md actualizat pentru a include 7 secțiuni progresive (anterior 6)
  - Adăugarea Qualcomm QNN la tabelul de repere de performanță (îmbunătățire de 5-15x viteză, reducere de 50-80% memorie)
  - Rezultate de învățare cuprinzătoare pentru implementarea AI mobilă și optimizarea energiei

### Modificat - Actualizări documentație Module04
- **Îmbunătățirea documentației Microsoft Olive** (`Module04/03.MicrosoftOlive.md`):
  - Adăugarea secțiunii cuprinzătoare "Olive Recipes Repository" care acoperă peste 100 de rețete de optimizare predefinite
  - Acoperire detaliată a familiilor de modele suportate (Phi, Llama, Qwen, Gemma, Mistral, DeepSeek)
  - Exemple practice de personalizare a rețetelor și contribuții comunitare
  - Îmbunătățit cu repere de performanță și ghiduri de integrare

- **Reordonarea secțiunilor în Module04**:
  - Apple MLX mutat la Secțiunea 5 (anterior Secțiunea 6)
  - Workflow Synthesis mutat la Secțiunea 6 (anterior Secțiunea 7)
  - Qualcomm QNN poziționat ca Secțiunea 7 (focalizare mobilă/margine specializată)
  - Actualizate toate referințele fișierelor și linkurile de navigare în consecință

### Reparat - Validarea exemplelor din workshop
- **Validarea și repararea chat_bootstrap.py**:
  - Reparat declarația de import coruptă (`util.util.workshop_utils` → `util.workshop_utils`)
  - Creat `__init__.py` lipsă în pachetul util pentru rezolvarea corectă a modulelor Python
  - Instalate dependențele necesare (openai, foundry-local-sdk) în mediul conda
  - Validat cu succes execuția exemplului cu prompts implicite și personalizate
  - Confirmată integrarea cu serviciul Foundry Local și încărcarea modelului (phi-4-mini cu optimizare CUDA)

### Documentație - Actualizări ghiduri cuprinzătoare
- **Restructurare completă README.md Module04**:
  - Adăugarea Qualcomm QNN ca cadru major de optimizare alături de OpenVINO, Olive, MLX
  - Actualizarea rezultatelor capitolului pentru a include implementarea AI mobilă și optimizarea energiei
  - Îmbunătățirea tabelului de comparație a performanței cu metrici QNN și cazuri de utilizare mobilă/margine
  - Menținerea progresiei logice de la soluții enterprise la optimizări specifice platformei

- **Referințe încrucișate și navigare**:
  - Actualizarea tuturor linkurilor interne și referințelor fișierelor pentru noua numerotare a secțiunilor
  - Îmbunătățirea descrierii sintezei fluxului de lucru pentru a include medii mobile, desktop și cloud
  - Adăugarea linkurilor de resurse cuprinzătoare pentru ecosistemul de dezvoltatori Qualcomm

## 2025-10-08

### Adăugat - Actualizare cuprinzătoare Workshop
- **Rescriere completă README.md Workshop**:
  - Adăugarea unei introduceri cuprinzătoare care explică valoarea Edge AI (confidențialitate, performanță, cost)
  - Crearea a 6 obiective de învățare de bază cu competențe detaliate
  - Adăugarea unui tabel de rezultate ale învățării cu livrabile și matrice de competențe
  - Inclusiv secțiunea de abilități pregătite pentru carieră pentru relevanța în industrie
  - Adăugarea unui ghid de pornire rapidă cu cerințe preliminare și configurare în 3 pași
  - Crearea tabelelor de resurse pentru exemple Python (8 fișiere cu timpi de rulare)
  - Adăugarea tabelului de notebook-uri Jupyter (8 notebook-uri cu evaluări de dificultate)
  - Crearea tabelului de documentație (7 documente cheie cu ghid "Când să folosești")
  - Adăugarea recomandărilor de parcurs de învățare pentru diferite niveluri de competență

- **Infrastructura de validare și testare Workshop**:
  - Creat `scripts/validate_samples.py` - Instrument de validare cuprinzător pentru sintaxă, importuri și cele mai bune practici
  - Creat `scripts/test_samples.py` - Runner de testare rapidă pentru toate exemplele Python
  - Adăugarea documentației de validare la `scripts/README.md`

- **Documentație cuprinzătoare**:
  - Creat `SAMPLES_UPDATE_SUMMARY.md` - Ghid detaliat de peste 400 de linii care acoperă toate îmbunătățirile
  - Creat `UPDATE_COMPLETE.md` - Rezumat executiv al finalizării actualizării
  - Creat `QUICK_REFERENCE.md` - Card de referință rapidă pentru Workshop

### Modificat - Modernizarea exemplelor Python din Workshop
- **Toate cele 8 exemple Python actualizate cu cele mai bune practici**:
  - Îmbunătățirea gestionării erorilor cu blocuri try-except în jurul tuturor operațiunilor I/O
  - Adăugarea de indicii de tip și docstrings cuprinzătoare
  - Implementarea unui model consistent de logare [INFO]/[ERROR]/[RESULT]
  - Protejarea importurilor opționale cu sugestii de instalare
  - Îmbunătățirea feedback-ului utilizatorului în toate exemplele

- **session01/chat_bootstrap.py**:
  - Îmbunătățirea inițializării clientului cu mesaje de eroare cuprinzătoare
  - Îmbunătățirea gestionării erorilor de streaming cu validarea fragmentelor
  - Adăugarea unei gestionări mai bune a excepțiilor pentru indisponibilitatea serviciului

- **session02/rag_pipeline.py**:
  - Adăugarea protecțiilor de import pentru sentence-transformers cu sugestii de instalare
  - Îmbunătățirea gestionării erorilor pentru operațiunile de încorporare și generare
  - Îmbunătățirea formatării ieșirii cu rezultate structurate

- **session02/rag_eval_ragas.py**:
  - Protejarea importurilor opționale (ragas, datasets) cu mesaje de eroare prietenoase
  - Adăugarea gestionării erorilor pentru metricile de evaluare
  - Îmbunătățirea formatării ieșirii pentru rezultatele evaluării

- **session03/benchmark_oss_models.py**:
  - Implementarea degradării grațioase (continuă în cazul eșecului modelelor)
  - Adăugarea raportării detaliate a progresului și gestionarea erorilor pe model
  - Îmbunătățirea calculului statisticilor cu recuperare cuprinzătoare a erorilor

- **session04/model_compare.py**:
  - Adăugarea de indicii de tip (tipuri de returnare Tuple)
  - Îmbunătățirea formatării ieșirii cu rezultate JSON structurate
  - Implementarea gestionării erorilor pe model cu recuperare

- **session05/agents_orchestrator.py**:
  - Îmbunătățirea Agent.act() cu docstrings cuprinzătoare
  - Adăugarea gestionării erorilor pipeline cu logare etapă cu etapă
  - Îmbunătățirea gestionării memoriei și urmărirea stării

- **session06/models_router.py**:
  - Îmbunătățirea documentației funcțiilor pentru toate componentele de rutare
  - Adăugarea logării detaliate în funcția route()
  - Îmbunătățirea ieșirii testului cu rezultate structurate

- **session06/models_pipeline.py**:
  - Adăugarea gestionării erorilor la funcția helper chat()
  - Îmbunătățirea pipeline() cu logare etapă cu etapă și raportare a progresului
  - Îmbunătățirea main() cu recuperare cuprinzătoare a erorilor

### Documentație - Îmbunătățirea documentației Workshop
- Actualizarea README.md principal cu secțiunea Workshop care evidențiază parcursul de învățare practică
- Îmbunătățirea STUDY_GUIDE.md cu secțiunea Workshop cuprinzătoare, incluzând:
  - Obiective de învățare și zone de focalizare pentru studiu
  - Întrebări de autoevaluare
  - Exerciții practice cu estimări de timp
  - Alocare de timp pentru studiu concentrat și part-time
  - Adăugarea Workshop-ului la șablonul de urmărire a progresului
- Actualizarea ghidului de alocare a timpului de la 20 de ore la 30 de ore (inclusiv Workshop-ul)
- Adăugarea descrierilor exemplelor din Workshop și rezultatelor învățării la README

### Reparat
- Rezolvarea modelelor inconsistente de gestionare a erorilor în exemplele din Workshop
- Repararea erorilor de import ale dependențelor opționale cu protecții adecvate
- Corectarea lipsei indicilor de tip în funcțiile critice
- Abordarea feedback-ului insuficient al utilizatorului în scenarii de eroare
- Repararea problemelor de validare cu infrastructura de testare cuprinzătoare

---

## 2025-09-23

### Modificat - Modernizarea majoră a Module 08
- **Aliniere cuprinzătoare cu modelele de implementare ale depozitului Microsoft Foundry-Local**
  - Actualizarea tuturor exemplelor de cod pentru a utiliza modelele moderne `FoundryLocalManager` și integrarea SDK OpenAI
  - Înlocuirea apelurilor manuale `requests` învechite cu utilizarea corectă a SDK-ului
  - Alinierea modelelor de implementare cu documentația oficială Microsoft și exemplele

- **Modernizarea 05.AIPoweredAgents.md**:
  - Actualizarea orchestrării multi-agent pentru a utiliza modelele SDK moderne
  - Îmbunătățirea implementării coordonatorului cu funcții avansate (buclă de feedback, monitorizarea performanței)
  - Adăugarea gestionării cuprinzătoare a erorilor și verificarea sănătății serviciului
  - Integrarea referințelor adecvate la exemplele locale (`samples/05/multi_agent_orchestration.ipynb`)
  - Actualizarea exemplelor de apelare a funcțiilor pentru a utiliza parametrul modern `tools` în locul `functions` învechit
  - Adăugarea modelelor gata de producție cu monitorizare și urmărirea statisticilor

- **Rescriere completă 06.ModelsAsTools
  - Exemple funcționale sub `Module08/samples/01`–`06` cu instrucțiuni cmd Windows
    - `01` REST chat rapid (`chat_quickstart.py`)
    - `02` SDK rapid cu suport OpenAI/Foundry Local și Azure OpenAI (`sdk_quickstart.py`)
    - `03` CLI listare și testare (`list_and_bench.cmd`)
    - `04` Demo Chainlit (`app.py`)
    - `05` Orchestrare multi-agent (`python -m samples.05.agents.coordinator`)
    - `06` Router Models-as-Tools (`router.py`)
- Suport Azure OpenAI în exemplul SDK din Sesiunea 2 cu configurare variabilă de mediu
- `.vscode/settings.json` indică spre `Module08/.venv` pentru îmbunătățirea rezoluției analizei Python
- `.env` cu sugestie `PYTHONPATH` pentru conștientizarea VS Code/Pylance

### Modificat
- Modelul implicit actualizat la `phi-4-mini` în documentația și exemplele Module 08; eliminat mențiunile rămase despre `phi-3.5` în Module 08
- Îmbunătățiri la Router (`Module08/samples/06/router.py`):
  - Descoperirea endpoint-urilor prin `foundry service status` cu analiză regex
  - Verificare sănătate `/v1/models` la pornire
  - Registru de modele configurabil prin mediu (`GENERAL_MODEL`, `REASONING_MODEL`, `CODE_MODEL`, `TOOL_REGISTRY` JSON)
- Cerințe actualizate: `Module08/requirements.txt` include acum `openai` (alături de `requests`, `chainlit`)
- Ghid clarificat pentru exemplul Chainlit și adăugate soluții pentru probleme; rezolvarea importurilor prin setările workspace-ului

### Rezolvat
- Probleme de import rezolvate:
  - Routerul nu mai depinde de un modul `utils` inexistent; funcțiile sunt integrate
  - Coordinator folosește import relativ (`from .specialists import ...`) și este apelat prin calea modulului
  - Configurația VS Code/Pylance pentru rezolvarea importurilor `chainlit` și ale pachetelor
- Corectat o eroare minoră de tipar în `STUDY_GUIDE.md` și adăugată acoperirea Module 08

### Eliminat
- Șters `Module08/infra/obs.py` neutilizat și eliminat directorul gol `infra/`; modelele de observabilitate păstrate ca opționale în documentație

### Mutat
- Consolidat demo-urile Module 08 sub `Module08/samples` cu foldere numerotate pe sesiuni
  - Mutat aplicația Chainlit la `samples/04`
  - Mutat agenții la `samples/05` și adăugat fișiere `__init__.py` pentru rezolvarea pachetelor

### Documentație
- Documentația sesiunii Module 08 și toate README-urile exemplelor îmbogățite cu referințe Microsoft Learn și furnizori de încredere
- `Module08/README.md` actualizat cu Prezentare generală a exemplelor, configurarea routerului și sfaturi de validare
- `Module07/README.md` secțiunea Windows Foundry Local validată conform documentației Learn
- `STUDY_GUIDE.md` actualizat:
  - Adăugat Module 08 la prezentare generală, programe, tracker de progres
  - Adăugat secțiune cuprinzătoare de Referințe (Foundry Local, Azure AI, Olive, ONNX Runtime, OpenVINO, MLX, Llama.cpp, vLLM, Ollama, AI Toolkit, Windows ML)

---

## Istoric (rezumat)
- Arhitectura cursului și modulele stabilite (Module 01–07)
- Modernizare iterativă a conținutului, standardizare format și adăugare studii de caz
- Extinderea acoperirii cadrelor de optimizare (Llama.cpp, Olive, OpenVINO, Apple MLX)

## Nerelease / Backlog (propuneri)
- Teste opționale per-exemplu pentru validarea disponibilității Foundry Local
- Revizuirea traducerilor pentru alinierea referințelor la modele (ex. `phi-4-mini`) unde este cazul
- Adăugarea unei configurații minimale pyright dacă echipele preferă strictețe la nivel de workspace

---

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să asigurăm acuratețea, vă rugăm să fiți conștienți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa natală ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de oameni. Nu ne asumăm responsabilitatea pentru neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.
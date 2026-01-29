# Caiete de Lucru

> **Caiete Jupyter Interactive pentru Învățare Practică în AI la Margine**
>
> Tutoriale progresive, în ritm propriu, care evoluează de la completări de bază în chat la sisteme avansate multi-agent, utilizând Microsoft Foundry Local și modele de limbaj mici.

---

## 📖 Introducere

Bine ați venit la colecția **EdgeAI pentru Începători - Caiete de Lucru**. Aceste caiete Jupyter interactive oferă o experiență de învățare practică, unde veți scrie, executa și experimenta cod AI la margine în timp real.

### De ce Caiete Jupyter?

Spre deosebire de tutorialele tradiționale, aceste caiete oferă:

- **Învățare Interactivă**: Rulați celule de cod și vedeți rezultatele imediat
- **Experimentare**: Modificați parametrii și observați schimbările în timp real
- **Documentare**: Explicații inline și celule markdown care vă ghidează prin concepte
- **Reproducibilitate**: Exemple complete funcționale pe care le puteți referi și reutiliza
- **Vizualizare**: Vizualizați metrici de performanță, încorporări și rezultate direct în caiet

### Ce Face Aceste Caiete Speciale?

Fiecare caiet este conceput conform **celor mai bune practici pentru producție**:

✅ **Gestionare Completă a Erorilor** - Degradare grațioasă și mesaje de eroare informative  
✅ **Indicații de Tip și Documentare** - Semnături clare ale funcțiilor și docstrings  
✅ **Monitorizare a Performanței** - Urmărirea utilizării token-urilor și măsurători de latență  
✅ **Design Modular** - Modele reutilizabile pe care le puteți adapta proiectelor dvs.  
✅ **Complexitate Progresivă** - Se construiește sistematic pe sesiunile anterioare  

---

## 🎯 Obiective de Învățare

### Abilități de Bază pe care le Veți Dezvolta

Parcurgând aceste caiete, veți stăpâni:

1. **Gestionarea Serviciilor AI Locale**
   - Configurați și gestionați serviciile Microsoft Foundry Local
   - Selectați și încărcați modele adecvate pentru hardware-ul dvs.
   - Monitorizați utilizarea resurselor și optimizați performanța
   - Gestionați descoperirea serviciilor și verificarea stării

2. **Dezvoltarea Aplicațiilor AI**
   - Implementați completări de chat compatibile cu OpenAI local
   - Construiți interfețe de streaming pentru o experiență mai bună a utilizatorului
   - Proiectați prompturi eficiente pentru modele de limbaj mici
   - Integrați modele locale în aplicații

3. **Generare Augmentată prin Recuperare (RAG)**
   - Creați căutare semantică cu încorporări vectoriale
   - Fundamentați răspunsurile LLM în documente specifice domeniului
   - Evaluați calitatea RAG cu metrici RAGAS
   - Scalați de la prototip la producție

4. **Optimizarea Performanței**
   - Benchmarking sistematic al mai multor modele
   - Măsurați latența, debitul și timpul primului token
   - Comparați modele de limbaj mici cu modele de limbaj mari
   - Selectați modele optime pe baza compromisurilor performanță/calitate

5. **Orchestrarea Multi-Agent**
   - Proiectați agenți specializați pentru diferite sarcini
   - Implementați memorie și gestionarea contextului pentru agenți
   - Coordonați mai mulți agenți în fluxuri de lucru complexe
   - Construiți modele de coordonare pentru colaborarea agenților

6. **Rutare Inteligentă a Modelului**
   - Implementați detectarea intenției și potrivirea modelelor
   - Direcționați automat interogările către modele adecvate
   - Construiți fluxuri de lucru multi-pas (planificare → execuție → rafinare)
   - Proiectați arhitecturi scalabile de tip model-ca-unelte

---

## 🎓 Rezultate ale Învățării

### Ce Veți Construi

| Caiet | Rezultat | Abilități Demonstrate | Dificultate |
|-------|----------|-----------------------|-------------|
| **Sesiunea 01** | Aplicație de chat cu streaming | Configurarea serviciului, completări de bază, UX de streaming | ⭐ Începător |
| **Sesiunea 02 (RAG)** | Pipeline RAG cu evaluare | Încorporări, căutare semantică, metrici de calitate | ⭐⭐ Intermediar |
| **Sesiunea 02 (Eval)** | Evaluator de calitate RAG | Metrici RAGAS, evaluare sistematică | ⭐⭐ Intermediar |
| **Sesiunea 03** | Benchmark multi-model | Măsurarea performanței, comparația modelelor | ⭐⭐ Intermediar |
| **Sesiunea 04** | Comparator SLM vs LLM | Analiza compromisurilor, strategii de optimizare | ⭐⭐⭐ Avansat |
| **Sesiunea 05** | Orchestrator multi-agent | Designul agenților, memorie, coordonare | ⭐⭐⭐ Avansat |
| **Sesiunea 06 (Router)** | Sistem de rutare inteligent | Detectarea intenției, selecția modelului | ⭐⭐⭐ Avansat |
| **Sesiunea 06 (Pipeline)** | Pipeline multi-pas | Fluxuri de lucru planificare/execuție/rafinare | ⭐⭐⭐ Avansat |

### Progresia Competențelor

```
Session 01 ────► Session 02 ────► Session 03 ────► Session 04 ────► Session 05-06
   Basic            RAG             Benchmarking      Comparison      Multi-Agent
   Chat             Systems         & Performance     & Optimization  Orchestration
   
Foundation    │   Intermediate   │   Advanced       │   Expert
──────────────┴──────────────────┴──────────────────┴──────────────►
```

---

## 📅 Programul Workshop-ului

### 🚀 Workshop de Jumătate de Zi (3,5 ore)

**Perfect pentru: Sesiuni de instruire în echipă, hackathoane, workshop-uri la conferințe**

| Timp | Durată | Sesiune | Subiecte | Activități |
|------|--------|---------|----------|------------|
| **0:00** | 30 min | Configurare & Introducere | Configurarea mediului, instalarea Foundry Local | Instalați dependențele, verificați configurarea |
| **0:30** | 30 min | Sesiunea 01 | Completări de chat de bază, streaming | Rulați caietul, modificați prompturile |
| **1:00** | 45 min | Sesiunea 02 | Pipeline RAG, încorporări, evaluare | Construiți sistemul RAG, testați interogările |
| **1:45** | 15 min | Pauză | ☕ Cafea & întrebări | — |
| **2:00** | 30 min | Sesiunea 03 | Benchmark multi-model | Comparați 3+ modele |
| **2:30** | 30 min | Sesiunea 04 | Compromisuri SLM vs LLM | Analizați performanța/calitatea |
| **3:00** | 30 min | Sesiunile 05-06 | Sisteme multi-agent & rutare | Explorați modele avansate |

**Rezultat**: Participanții pleacă cu 6 aplicații AI la margine funcționale și modele de cod gata de producție.

---

### 🎓 Workshop de O Zi (6 ore)

**Perfect pentru: Instruire aprofundată, bootcamp-uri, cursuri universitare**

| Timp | Durată | Sesiune | Subiecte | Activități |
|------|--------|---------|----------|------------|
| **0:00** | 45 min | Configurare & Teorie | Configurarea mediului, fundamentele AI la margine | Instalați, verificați, discutați cazuri de utilizare |
| **0:45** | 45 min | Sesiunea 01 | Detalii despre completările de chat | Implementați chat de bază & streaming |
| **1:30** | 30 min | Pauză | ☕ Cafea & networking | — |
| **2:00** | 60 min | Sesiunea 02 (Ambele) | Pipeline RAG + evaluare RAGAS | Construiți sistemul RAG complet |
| **3:00** | 30 min | Laborator Practic 1 | RAG personalizat pentru domeniul dvs. | Aplicați pe documentele proprii |
| **3:30** | 30 min | Prânz | 🍽️ | — |
| **4:00** | 45 min | Sesiunea 03 | Metodologia benchmarking-ului | Comparație sistematică a modelelor |
| **4:45** | 45 min | Sesiunea 04 | Strategii de optimizare | Analiza SLM vs LLM |
| **5:30** | 60 min | Sesiunile 05-06 | Orchestrare avansată | Sisteme multi-agent, rutare |
| **6:30** | 30 min | Laborator Practic 2 | Construiți un sistem de agenți personalizat | Proiectați propriul orchestrator |

**Rezultat**: Înțelegere profundă a modelelor AI la margine plus 2 proiecte personalizate.

---

### 📚 Învățare în Ritm Propriu (2 săptămâni)

**Perfect pentru: Cursanți individuali, cursuri online, auto-studiu**

#### Săptămâna 1: Fundamente (6 ore)

| Zi | Focus | Durată | Caiete | Temă |
|----|-------|--------|--------|------|
| **Luni** | Configurare & Baze | 1,5 ore | Sesiunea 01 | Modificați prompturile, testați streaming-ul |
| **Miercuri** | Fundamente RAG | 2 ore | Sesiunea 02 (ambele) | Adăugați documentele proprii |
| **Vineri** | Benchmarking | 1,5 ore | Sesiunea 03 | Comparați modele suplimentare |
| **Sâmbătă** | Revizuire & Practică | 1 oră | Toate Săptămâna 1 | Completați exercițiile, depanați |

#### Săptămâna 2: Avansat (5 ore)

| Zi | Focus | Durată | Caiete | Temă |
|----|-------|--------|--------|------|
| **Luni** | Optimizare | 1,5 ore | Sesiunea 04 | Documentați compromisurile |
| **Miercuri** | Sisteme Multi-Agent | 2 ore | Sesiunea 05 | Proiectați agenți personalizați |
| **Vineri** | Rutare Inteligentă | 1,5 ore | Sesiunea 06 (ambele) | Construiți logica de rutare |
| **Sâmbătă** | Proiect Final | 2 ore | Integrare | Combinați mai multe modele |

**Rezultat**: Stăpânirea modelelor AI la margine plus proiect de portofoliu.

---

## 📔 Descrierea Caietelor

### 📘 Sesiunea 01: Bootstrap Chat
**Fișier**: `session01_chat_bootstrap.ipynb`  
**Durată**: 20-30 minute  
**Prerechizite**: Niciuna  
**Dificultate**: ⭐ Începător

**Ce Veți Învăța**:
- Instalați și configurați SDK-ul Python Foundry Local
- Utilizați `FoundryLocalManager` pentru descoperirea automată a serviciilor
- Implementați completări de chat de bază cu API compatibil OpenAI
- Construiți răspunsuri de streaming pentru o experiență mai bună a utilizatorului
- Gestionați erorile și indisponibilitatea serviciilor în mod grațios

**Concepte Cheie**: Gestionarea serviciilor, completări de chat, streaming, gestionarea erorilor

**Ce Veți Construi**: Aplicație de chat interactivă cu suport pentru streaming

---

### 📗 Sesiunea 02: Pipeline RAG
**Fișier**: `session02_rag_pipeline.ipynb`  
**Durată**: 30-45 minute  
**Prerechizite**: Sesiunea 01  
**Dificultate**: ⭐⭐ Intermediar

**Ce Veți Învăța**:
- Implementați modelul Generare Augmentată prin Recuperare (RAG)
- Creați încorporări vectoriale cu sentence-transformers
- Construiți căutare semantică cu similaritate cosinus
- Fundamentați răspunsurile LLM în documente specifice domeniului
- Gestionați dependențele opționale cu import guards

**Concepte Cheie**: Arhitectura RAG, încorporări, căutare semantică, similaritate vectorială

**Ce Veți Construi**: Sistem de întrebări-răspunsuri fundamentat pe documente

---

### 📗 Sesiunea 02: Evaluare RAG cu RAGAS
**Fișier**: `session02_rag_eval_ragas.ipynb`  
**Durată**: 30-45 minute  
**Prerechizite**: Pipeline RAG din Sesiunea 02  
**Dificultate**: ⭐⭐ Intermediar

**Ce Veți Învăța**:
- Evaluați calitatea RAG cu metrici standard din industrie
- Măsurați relevanța contextului, relevanța răspunsului, fidelitatea
- Utilizați cadrul RAGAS pentru evaluare sistematică
- Identificați și remediați problemele de calitate RAG
- Construiți seturi de date de evaluare pentru domeniul dvs.

**Concepte Cheie**: Evaluare RAG, metrici RAGAS, măsurarea calității, testare sistematică

**Ce Veți Construi**: Cadru de evaluare a calității RAG

---

### 📙 Sesiunea 03: Benchmark Modele OSS
**Fișier**: `session03_benchmark_oss_models.ipynb`  
**Durată**: 30-45 minute  
**Prerechizite**: Sesiunea 01  
**Dificultate**: ⭐⭐ Intermediar

**Ce Veți Învăța**:
- Benchmarking sistematic al mai multor modele
- Măsurați latența, debitul, timpul primului token
- Implementați degradare grațioasă pentru eșecurile modelelor
- Comparați performanța între familiile de modele
- Vizualizați și analizați rezultatele benchmark-ului

**Concepte Cheie**: Benchmarking performanță, măsurarea latenței, comparația modelelor, analiză statistică

**Ce Veți Construi**: Suită de benchmarking multi-model

---

### 📙 Sesiunea 04: Comparație Modele (SLM vs LLM)
**Fișier**: `session04_model_compare.ipynb`  
**Durată**: 30-45 minute  
**Prerechizite**: Sesiunile 01, 03  
**Dificultate**: ⭐⭐⭐ Avansat

**Ce Veți Învăța**:
- Comparați Modele de Limbaj Mici cu Modele de Limbaj Mari
- Analizați compromisurile performanță vs calitate
- Măsurați metrici de adecvare pentru margine
- Selectați modele optime pentru constrângerile de implementare
- Documentați criteriile de decizie pentru selecția modelelor

**Concepte Cheie**: Selecția modelelor, analiza compromisurilor, strategii de optimizare, planificarea implementării

**Ce Veți Construi**: Cadru de comparație SLM vs LLM

---

### 📕 Sesiunea 05: Orchestrator Multi-Agent
**Fișier**: `session05_agents_orchestrator.ipynb`  
**Durată**: 45-60 minute  
**Prerechizite**: Sesiunile 01-02  
**Dificultate**: ⭐⭐⭐ Avansat

**Ce Veți Învăța**:
- Proiectați agenți specializați pentru diferite sarcini
- Implementați memorie și gestionarea contextului pentru agenți
- Construiți modele de coordonare pentru colaborarea agenților
- Gestionați comunicarea și transferul între agenți
- Monitorizați performanța sistemului multi-agent

**Concepte Cheie**: Arhitectura agenților, modele de coordonare, gestionarea memoriei, orchestrarea agenților

**Ce Veți Construi**: Sistem multi-agent cu coordonator și specialiști

---

### 📕 Sesiunea 06: Router de Modele
**Fișier**: `session06_models_router.ipynb`  
**Durată**: 30-45 minute  
**Prerechizite**: Sesiunile 01, 03  
**Dificultate**: ⭐⭐⭐ Avansat

**Ce Veți Învăța**:
- Implementați detectarea intenției și potrivirea modelelor
- Construiți rutare de modele bazată pe cuvinte cheie
- Direcționați automat interogările către modele adecvate
- Configurați registre multi-model
- Monitorizați deciziile de rutare și performanța

**Concepte Cheie**: Detectarea intenției, rutarea modelelor, potrivirea modelelor, selecție inteligentă

**Ce Veți Construi**: Sistem de rutare inteligentă a modelelor

---

### 📕 Sesiunea 06: Pipeline Multi-Pas
**Fișier**: `session06_models_pipeline.ipynb`  
**Durată**: 30-45
- Proiectarea arhitecturilor scalabile model-ca-unelte

**Concepte cheie**: Arhitectura pipeline, procesare în mai multe etape, recuperare din erori, modele de scalabilitate

**Ce vei construi**: Pipeline inteligent în mai mulți pași cu rutare

---

## 🚀 Începe

### Cerințe preliminare

**Cerințe de sistem**:
- **OS**: Windows 10/11, macOS 11+ sau Linux (Ubuntu 20.04+)
- **RAM**: minim 8GB, recomandat 16GB+
- **Spațiu de stocare**: minim 10GB liber pentru modele
- **Hardware**: CPU cu AVX2; GPU (CUDA, Qualcomm NPU) opțional

**Cerințe software**:
- **Python 3.8+** cu pip
- **Jupyter Notebook** sau **VS Code** cu extensia Jupyter
- **Microsoft Foundry Local** instalat și configurat
- **Git** (pentru clonarea repository-ului)

### Pași de instalare

#### 1. Instalează Foundry Local

**Windows**:
```cmd
winget install Microsoft.FoundryLocal
```

**macOS**:
```bash
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**Verifică instalarea**:
```bash
foundry --version
```

#### 2. Configurează mediul Python

```bash
# Navigate to Workshop directory
cd Workshop

# Create virtual environment
python -m venv .venv

# Activate virtual environment
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

#### 3. Pornește Foundry Local

```bash
# Load a model (auto-downloads if needed)
foundry model run phi-4-mini

# Verify service is running
foundry service status
```

#### 4. Lansează Jupyter

```bash
# Start Jupyter Notebook
jupyter notebook notebooks/

# Or use VS Code with Jupyter extension
code notebooks/
```

### Verificare rapidă

Rulează acest cod într-o celulă Python pentru a verifica configurarea:

```python
from foundry_local import FoundryLocalManager
import openai

# Initialize manager (auto-discovers service)
manager = FoundryLocalManager("phi-4-mini")

# Configure OpenAI client
client = openai.OpenAI(
    base_url=manager.endpoint,
    api_key=manager.api_key
)

# Test chat completion
response = client.chat.completions.create(
    model=manager.get_model_info("phi-4-mini").id,
    messages=[{"role": "user", "content": "Hello!"}]
)

print(response.choices[0].message.content)
```

**Rezultat așteptat**: Un răspuns de salut de la modelul local.

---

## 📝 Practici recomandate pentru workshop

### Pentru instructori

**Înainte de workshop**:
- ✅ Trimite instrucțiunile de instalare cu 1 săptămână înainte
- ✅ Testează toate notebook-urile pe hardware-ul țintă
- ✅ Pregătește un ghid de depanare pentru probleme comune
- ✅ Ai modele de rezervă pregătite (phi-3.5-mini dacă phi-4-mini eșuează)
- ✅ Configurează un canal de chat comun pentru întrebări

**În timpul workshop-ului**:
- ✅ Începe cu o verificare rapidă a mediului (5 minute)
- ✅ Distribuie resursele de depanare imediat
- ✅ Încurajează experimentarea și modificările
- ✅ Folosește pauze strategic (după fiecare 2 sesiuni)
- ✅ Ai asistenți disponibili pentru ajutor individual

**După workshop**:
- ✅ Distribuie notebook-urile funcționale și soluțiile complete
- ✅ Oferă linkuri către resurse suplimentare
- ✅ Creează un sondaj de feedback pentru îmbunătățiri
- ✅ Oferă ore de consultanță pentru întrebări ulterioare

### Pentru participanți

**Maximizează învățarea**:
- ✅ Finalizează configurarea înainte de începerea workshop-ului
- ✅ Rulează fiecare celulă de cod (nu doar citește)
- ✅ Experimentează cu parametrii și prompturile
- ✅ Ia notițe despre observații și probleme
- ✅ Pune întrebări când te blochezi (probabil alții au aceeași întrebare)

**Greșeli comune de evitat**:
- ❌ Săritul peste ordinea de execuție a celulelor (rulează secvențial)
- ❌ Neatenția la mesajele de eroare
- ❌ Graba fără înțelegere
- ❌ Ignorarea explicațiilor din markdown
- ❌ Nesalvarea notebook-urilor modificate

**Sfaturi pentru depanare**:
1. **Serviciul nu rulează**: Verifică `foundry service status`
2. **Erori de import**: Asigură-te că mediul virtual este activat
3. **Modelul nu este găsit**: Rulează `foundry model ls` pentru a lista modelele încărcate
4. **Performanță lentă**: Verifică utilizarea RAM, închide alte aplicații
5. **Rezultate neașteptate**: Repornește kernel-ul și rulează toate celulele de la început

---

## 🔗 Resurse suplimentare

### Materiale pentru workshop

- **[Ghid principal workshop](../Readme.md)** - Prezentare generală, obiective de învățare, rezultate profesionale
- **[Exemple Python](../../../../Workshop/samples)** - Scripturi Python corespunzătoare fiecărei sesiuni
- **[Ghiduri sesiuni](../../../../Workshop)** - Ghiduri detaliate în markdown (Sesiunea01-06)
- **[Scripturi](../../../../Workshop/scripts)** - Utilitare pentru validare și testare
- **[Depanare](./TROUBLESHOOTING.md)** - Probleme comune și soluții
- **[Ghid rapid](./quickstart.md)** - Ghid pentru început rapid

### Documentație

- **[Documentație Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)** - Documentația oficială Microsoft
- **[OpenAI Python SDK](https://github.com/openai/openai-python)** - Referință SDK OpenAI
- **[Sentence Transformers](https://www.sbert.net/)** - Documentație modele de embedding
- **[Framework RAGAS](https://docs.ragas.io/)** - Metrici de evaluare RAG

### Comunitate

- **[Discuții GitHub](https://github.com/microsoft/edgeai-for-beginners/discussions)** - Pune întrebări, împărtășește proiecte
- **[Discord Azure AI Foundry](https://discord.com/invite/ByRwuEEgH4)** - Suport comunitar în timp real
- **[Stack Overflow](https://stackoverflow.com/questions/tagged/foundry-local)** - Întrebări și răspunsuri tehnice

---

## 🎯 Recomandări pentru traseul de învățare

### Traseu pentru începători (Începe aici)

1. **Sesiunea 01** - Bootstrap Chat
2. **Sesiunea 02** - Pipeline RAG
3. **Sesiunea 03** - Benchmark modele

**Timp**: ~2 ore | **Focus**: Modele fundamentale

---

### Traseu intermediar

1. Completează traseul pentru începători
2. **Sesiunea 02** - Evaluare RAG
3. **Sesiunea 04** - Compararea modelelor

**Timp**: ~4 ore | **Focus**: Calitate și optimizare

---

### Traseu avansat (Workshop complet)

1. Completează traseul intermediar
2. **Sesiunea 05** - Orchestrator multi-agent
3. **Sesiunea 06** - Router de modele
4. **Sesiunea 06** - Pipeline în mai mulți pași

**Timp**: ~6 ore | **Focus**: Modele de producție

---

### Traseu proiect personalizat

1. Completează traseul pentru începători (Sesiunile 01-03)
2. Alege O sesiune avansată în funcție de obiectivul tău:
   - **Construiești o aplicație RAG?** → Sesiunea 02 Evaluare
   - **Optimizezi performanța?** → Sesiunea 04 Comparare
   - **Fluxuri de lucru complexe?** → Sesiunea 05 Orchestrator
   - **Arhitectură scalabilă?** → Sesiunea 06 Router + Pipeline

**Timp**: ~3 ore | **Focus**: Abilități specifice proiectului

---

## 📊 Metrice de succes

Urmărește progresul cu aceste repere:

- [ ] **Configurare completă** - Foundry Local funcțional, toate dependențele instalate
- [ ] **Primul chat** - Sesiunea 01 finalizată, chat streaming funcțional
- [ ] **RAG construit** - Sesiunea 02 finalizată, sistem QA document funcțional
- [ ] **Modele benchmarked** - Sesiunea 03 finalizată, date de performanță colectate
- [ ] **Analiza compromisurilor** - Sesiunea 04 finalizată, criterii de selecție modele documentate
- [ ] **Agenți orchestrați** - Sesiunea 05 finalizată, sistem multi-agent funcțional
- [ ] **Rutare implementată** - Sesiunea 06 finalizată, selecție inteligentă de modele funcțională
- [ ] **Proiect personalizat** - Aplicarea modelelor workshop-ului la propriul caz de utilizare

---

## 🤝 Contribuții

Ai găsit o problemă sau ai o sugestie? Acceptăm contribuții!

- **Raportează probleme**: [GitHub Issues](https://github.com/microsoft/edgeai-for-beginners/issues)
- **Sugerează îmbunătățiri**: [GitHub Discussions](https://github.com/microsoft/edgeai-for-beginners/discussions)
- **Trimite PR-uri**: Urmează [Ghidul de contribuții](../../AGENTS.md)

---

## 📄 Licență

Acest workshop face parte din repository-ul [EdgeAI for Beginners](https://github.com/microsoft/edgeai-for-beginners) și este licențiat sub [Licența MIT](../../../../LICENSE).

---

**Ești gata să construiești aplicații Edge AI pregătite pentru producție?**  
**Începe cu [Sesiunea 01: Bootstrap Chat](./session01_chat_bootstrap.ipynb) →**

---

*Ultima actualizare: 8 octombrie 2025 | Versiunea workshop-ului: 2.0*

---

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să asigurăm acuratețea, vă rugăm să fiți conștienți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa natală ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.
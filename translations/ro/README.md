<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8f958250b0b94976c721e6cbdc541581",
  "translation_date": "2025-10-24T09:57:43+00:00",
  "source_file": "README.md",
  "language_code": "ro"
}
-->
# EdgeAI pentru Începători

![Imagine copertă curs](../../translated_images/cover.eb18d1b9605d754b30973f4e17c6e11ea4f8473d9686ee378d6e7b44e3c70ac7.ro.png)

[![Contribuitori GitHub](https://img.shields.io/github/contributors/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/graphs/contributors)
[![Probleme GitHub](https://img.shields.io/github/issues/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/issues)
[![Pull-requests GitHub](https://img.shields.io/github/issues-pr/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/pulls)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

[![Urmăritori GitHub](https://img.shields.io/github/watchers/microsoft/edgeai-for-beginners.svg?style=social&label=Watch)](https://GitHub.com/microsoft/edgeai-for-beginners/watchers)
[![Fork-uri GitHub](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork)
[![Stele GitHub](https://img.shields.io/github/stars/microsoft/edgeai-for-beginners?style=social&label=Star)](https://GitHub.com/microsoft/edgeai-for-beginners/stargazers)

[![Microsoft Azure AI Foundry Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)

Urmați acești pași pentru a începe să utilizați aceste resurse:

1. **Forkați Repositorul**: Click [![Fork-uri GitHub](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork)
2. **Clonați Repositorul**: `git clone https://github.com/microsoft/edgeai-for-beginners.git`
3. [**Alăturați-vă Discord-ului Azure AI Foundry și întâlniți experți și alți dezvoltatori**](https://discord.com/invite/ByRwuEEgH4)

### 🌐 Suport Multi-Limbă

#### Suportat prin GitHub Action (Automat & Mereu Actualizat)

[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh/README.md) | [Chinese (Traditional, Hong Kong)](../hk/README.md) | [Chinese (Traditional, Macau)](../mo/README.md) | [Chinese (Traditional, Taiwan)](../tw/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../br/README.md) | [Portuguese (Portugal)](../pt/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](./README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

**Dacă doriți să aveți suport pentru alte limbi, acestea sunt listate [aici](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md)**

## Introducere

Bine ați venit la **EdgeAI pentru Începători** – călătoria voastră completă în lumea transformatoare a Inteligenței Artificiale la margine. Acest curs face legătura între capacitățile puternice ale AI și implementarea practică în lumea reală pe dispozitivele de margine, oferindu-vă posibilitatea de a valorifica potențialul AI direct acolo unde se generează datele și unde trebuie luate deciziile.

### Ce veți învăța

Acest curs vă duce de la concepte fundamentale la implementări gata de producție, acoperind:
- **Modele de limbaj mici (SLM)** optimizate pentru implementarea la margine
- **Optimizare orientată pe hardware** pentru diverse platforme
- **Inferență în timp real** cu capacități de protecție a confidențialității
- **Strategii de implementare în producție** pentru aplicații de întreprindere

### De ce este important EdgeAI

Edge AI reprezintă o schimbare de paradigmă care abordează provocările moderne critice:
- **Confidențialitate & Securitate**: Procesați datele sensibile local, fără expunere la cloud
- **Performanță în timp real**: Eliminați latența rețelei pentru aplicații critice
- **Eficiență costurilor**: Reduceți cheltuielile de lățime de bandă și de calcul în cloud
- **Operațiuni reziliente**: Mențineți funcționalitatea în timpul întreruperilor de rețea
- **Conformitate reglementară**: Respectați cerințele de suveranitate a datelor

### Edge AI

Edge AI se referă la rularea algoritmilor AI și a modelelor de limbaj local pe hardware, aproape de locul unde se generează datele, fără a se baza pe resursele cloud pentru inferență. Acest lucru reduce latența, îmbunătățește confidențialitatea și permite luarea deciziilor în timp real.

### Principii de bază:
- **Inferență pe dispozitiv**: Modelele AI rulează pe dispozitive de margine (telefoane, routere, microcontrolere, PC-uri industriale)
- **Capacitate offline**: Funcționează fără conectivitate persistentă la internet
- **Latență scăzută**: Răspunsuri imediate potrivite pentru sisteme în timp real
- **Suveranitatea datelor**: Păstrează datele sensibile local, îmbunătățind securitatea și conformitatea

### Modele de limbaj mici (SLM)

SLM-uri precum Phi-4, Mistral-7B și Gemma sunt versiuni optimizate ale LLM-urilor mai mari – antrenate sau distilate pentru:
- **Amprentă de memorie redusă**: Utilizare eficientă a memoriei limitate a dispozitivelor de margine
- **Cerere de calcul mai mică**: Optimizate pentru performanța CPU și GPU de margine
- **Timpuri de pornire mai rapide**: Inițializare rapidă pentru aplicații receptive

Acestea deblochează capacități NLP puternice, respectând constrângerile:
- **Sisteme încorporate**: Dispozitive IoT și controlere industriale
- **Dispozitive mobile**: Smartphone-uri și tablete cu capacități offline
- **Dispozitive IoT**: Senzori și dispozitive inteligente cu resurse limitate
- **Servere de margine**: Unități de procesare locală cu resurse GPU limitate
- **Computere personale**: Scenarii de implementare pe desktop și laptop

## Modulele Cursului & Navigare

| Modul | Subiect | Zonă de focus | Conținut cheie | Nivel | Durată |
|-------|---------|---------------|----------------|-------|--------|
| [📖 00 ](./introduction.md) | [Introducere în EdgeAI](./introduction.md) | Fundamente & Context | Prezentare generală EdgeAI • Aplicații industriale • Introducere SLM • Obiective de învățare | Începător | 1-2 ore |
| [📚 01](../../Module01) | [Fundamentele EdgeAI](./Module01/README.md) | Comparație Cloud vs Edge AI | Fundamentele EdgeAI • Studii de caz reale • Ghid de implementare • Implementare la margine | Începător | 3-4 ore |
| [🧠 02](../../Module02) | [Fundamentele modelelor SLM](./Module02/README.md) | Familii de modele & arhitectură | Familia Phi • Familia Qwen • Familia Gemma • BitNET • μModel • Phi-Silica | Începător | 4-5 ore |
| [🚀 03](../../Module03) | [Practica de implementare SLM](./Module03/README.md) | Implementare locală & cloud | Învățare avansată • Mediu local • Implementare în cloud | Intermediar | 4-5 ore |
| [⚙️ 04](../../Module04) | [Toolkit de optimizare a modelelor](./Module04/README.md) | Optimizare cross-platform | Introducere • Llama.cpp • Microsoft Olive • OpenVINO • Apple MLX • Sinteza fluxului de lucru | Intermediar | 5-6 ore |
| [🔧 05](../../Module05) | [SLMOps în producție](./Module05/README.md) | Operațiuni de producție | Introducere SLMOps • Distilarea modelelor • Fine-tuning • Implementare în producție | Avansat | 5-6 ore |
| [🤖 06](../../Module06) | [Agenți AI & Apelarea funcțiilor](./Module06/README.md) | Framework-uri de agenți & MCP | Introducere agenți • Apelarea funcțiilor • Protocol de context al modelului | Avansat | 4-5 ore |
| [💻 07](../../Module07) | [Implementare pe platformă](./Module07/README.md) | Exemple cross-platform | Toolkit AI • Foundry Local • Dezvoltare Windows | Avansat | 3-4 ore |
| [🏭 08](../../Module08) | [Toolkit Foundry Local](./Module08/README.md) | Exemple gata de producție | Aplicații de exemplu (vezi detalii mai jos) | Expert | 8-10 ore |

### 🏭 **Modul 08: Aplicații de exemplu**

- [01: REST Chat Quickstart](./Module08/samples/01/README.md)
- [02: Integrare OpenAI SDK](./Module08/samples/02/README.md)
- [03: Descoperirea & Benchmarking-ul modelelor](./Module08/samples/03/README.md)
- [04: Aplicație Chainlit RAG](./Module08/samples/04/README.md)
- [05: Orchestrare Multi-Agent](./Module08/samples/05/README.md)
- [06: Router pentru modele-ca-unelte](./Module08/samples/06/README.md)
- [07: Client API Direct](./Module08/samples/07/README.md)
- [08: Aplicație Chat Windows 11](./Module08/samples/08/README.md)
- [09: Sistem Multi-Agent Avansat](./Module08/samples/09/README.md)
- [10: Framework Foundry Tools](./Module08/samples/10/README.md)

### 🎓 **Workshop: Cale de învățare practică**

Materiale complete de workshop hands-on cu implementări gata de producție:

- **[Ghid Workshop](./Workshop/Readme.md)** - Obiective complete de învățare, rezultate și navigare resurse
- **Exemple Python** (6 sesiuni) - Actualizate cu cele mai bune practici, gestionarea erorilor și documentație cuprinzătoare
- **Jupyter Notebooks** (8 interactive) - Tutoriale pas cu pas cu benchmark-uri și monitorizare performanță
- **Ghiduri sesiuni** - Ghiduri detaliate în markdown pentru fiecare sesiune de workshop
- **Instrumente de validare** - Scripturi pentru verificarea calității codului și teste rapide

**Ce veți construi:**
- Aplicații locale de chat AI cu suport pentru streaming
- Pipeline-uri RAG cu evaluare calitativă (RAGAS)
- Instrumente de benchmarking și comparație multi-model
- Sisteme de orchestrare multi-agent
- Rutare inteligentă a modelelor cu selecție bazată pe sarcini

### 📊 **Rezumat Cale de Învățare**
- **Durată Totală**: 36-45 ore
- **Cale Începător**: Modulele 01-02 (7-9 ore)  
- **Cale Intermediar**: Modulele 03-04 (9-11 ore)
- **Cale Avansat**: Modulele 05-07 (12-15 ore)
- **Cale Expert**: Modulul 08 (8-10 ore)

## Ce Veți Construi

### 🎯 Competențe de bază
- **Arhitectura Edge AI**: Proiectați sisteme AI locale cu integrare cloud
- **Optimizarea modelelor**: Quantizați și comprimați modelele pentru implementarea la margine (creștere de 85% a vitezei, reducere de 75% a dimensiunii)
- **Implementare Multi-Platformă**: Windows, mobil, încorporat și sisteme hibride cloud-margine
- **Operațiuni de producție**: Monitorizarea, scalarea și întreținerea AI la margine în producție

### 🏗️ Proiecte practice
- **Aplicații de chat locale Foundry**: Aplicație nativă Windows 11 cu schimbare de model
- **Sisteme multi-agent**: Coordonator cu agenți specializați pentru fluxuri de lucru complexe  
- **Aplicații RAG**: Procesarea documentelor locale cu căutare vectorială
- **Routere de modele**: Selecție inteligentă între modele bazată pe analiza sarcinilor
- **Framework-uri API**: Clienți pregătiți pentru producție cu streaming și monitorizare a sănătății
- **Instrumente cross-platform**: Modele de integrare LangChain/Semantic Kernel

### 🏢 Aplicații în industrie
**Producție** • **Sănătate** • **Vehicule autonome** • **Orașe inteligente** • **Aplicații mobile**

## Început rapid

**Cale de învățare recomandată** (20-30 ore în total):

0. **📖 Introducere** ([Introduction.md](./introduction.md)): Fundamente EdgeAI + context industrial + cadru de învățare
1. **📚 Fundamente** (Modulele 01-02): Concepte EdgeAI + familii de modele SLM
2. **⚙️ Optimizare** (Modulele 03-04): Implementare + cadre de cuantizare  
3. **🚀 Producție** (Modulele 05-06): SLMOps + agenți AI + apelarea funcțiilor
4. **💻 Implementare** (Modulele 07-08): Exemple de platformă + toolkit Foundry Local

Fiecare modul include teorie, exerciții practice și exemple de cod pregătite pentru producție.

## Impact asupra carierei

**Roluri tehnice**: Arhitect de soluții EdgeAI • Inginer ML (Edge) • Dezvoltator IoT AI • Dezvoltator AI mobil

**Sectore industriale**: Producție 4.0 • Tehnologie medicală • Sisteme autonome • FinTech • Electronice de consum

**Proiecte de portofoliu**: Sisteme multi-agent • Aplicații RAG în producție • Implementare cross-platform • Optimizare performanță

## Structura depozitului

```
edgeai-for-beginners/
├── 📖 introduction.md  # Foundation: EdgeAI Overview & Learning Framework
├── 📚 Module01-04/     # Fundamentals → SLMs → Deployment → Optimization  
├── 🔧 Module05-06/     # SLMOps → AI Agents → Function Calling
├── 💻 Module07/        # Platform Samples (VS Code, Windows, Jetson, Mobile)
├── 🏭 Module08/        # Foundry Local Toolkit + 10 Comprehensive Samples
│   ├── samples/01-06/  # Foundation: REST, SDK, RAG, Agents, Routing
│   └── samples/07-10/  # Advanced: API Client, Windows App, Enterprise Agents, Tools
├── 🌐 translations/    # Multi-language support (8+ languages)
└── 📋 STUDY_GUIDE.md   # Structured learning paths & time allocation
```

## Repere ale cursului

✅ **Învățare progresivă**: Teorie → Practică → Implementare în producție  
✅ **Studii de caz reale**: Microsoft, Japan Airlines, implementări în întreprinderi  
✅ **Exemple practice**: Peste 50 de exemple, 10 demonstrații complete Foundry Local  
✅ **Focus pe performanță**: Îmbunătățiri de viteză de 85%, reduceri de dimensiune de 75%  
✅ **Multi-platformă**: Windows, mobil, încorporat, hibrid cloud-edge  
✅ **Pregătit pentru producție**: Monitorizare, scalare, securitate, cadre de conformitate

📖 **[Ghid de studiu disponibil](STUDY_GUIDE.md)**: Cale de învățare structurată de 20 de ore cu orientări privind alocarea timpului și instrumente de autoevaluare.

---

**EdgeAI reprezintă viitorul implementării AI**: local-prim, care protejează confidențialitatea și eficient. Stăpânește aceste abilități pentru a construi următoarea generație de aplicații inteligente.

## Alte cursuri

Echipa noastră produce și alte cursuri! Verifică:

### Azure / Edge / MCP / Agenți
[![AZD pentru Începători](https://img.shields.io/badge/AZD%20pentru%20Începători-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Edge AI pentru Începători](https://img.shields.io/badge/Edge%20AI%20pentru%20Începători-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP pentru Începători](https://img.shields.io/badge/MCP%20pentru%20Începători-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Agenți AI pentru Începători](https://img.shields.io/badge/Agenți%20AI%20pentru%20Începători-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---

### Seria Generative AI
[![Generative AI pentru Începători](https://img.shields.io/badge/Generative%20AI%20pentru%20Începători-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Generative AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![Generative AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![Generative AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---

### Învățare de bază
[![ML pentru Începători](https://img.shields.io/badge/ML%20pentru%20Începători-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![Data Science pentru Începători](https://img.shields.io/badge/Data%20Science%20pentru%20Începători-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![AI pentru Începători](https://img.shields.io/badge/AI%20pentru%20Începători-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![Cybersecurity pentru Începători](https://img.shields.io/badge/Cybersecurity%20pentru%20Începători-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![Web Dev pentru Începători](https://img.shields.io/badge/Web%20Dev%20pentru%20Începători-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![IoT pentru Începători](https://img.shields.io/badge/IoT%20pentru%20Începători-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![Dezvoltare XR pentru Începători](https://img.shields.io/badge/Dezvoltare%20XR%20pentru%20Începători-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---

### Seria Copilot
[![Copilot pentru Programare AI în Perechi](https://img.shields.io/badge/Copilot%20pentru%20Programare%20AI%20în%20Perechi-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot pentru C#/.NET](https://img.shields.io/badge/Copilot%20pentru%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Aventura Copilot](https://img.shields.io/badge/Aventura%20Copilot-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)

## Obținerea ajutorului

Dacă întâmpini dificultăți sau ai întrebări despre construirea aplicațiilor AI, alătură-te:

[![Discord Azure AI Foundry](https://img.shields.io/badge/Discord-Comunitatea_Azure_AI_Foundry_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

Dacă ai feedback despre produs sau întâmpini erori în timpul construirii, vizitează:

[![Forum pentru Dezvoltatori Azure AI Foundry](https://img.shields.io/badge/GitHub-Forumul_Dezvoltatorilor_Azure_AI_Foundry-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să asigurăm acuratețea, vă rugăm să fiți conștienți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa maternă ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de oameni. Nu ne asumăm responsabilitatea pentru neînțelegerile sau interpretările greșite care pot apărea din utilizarea acestei traduceri.
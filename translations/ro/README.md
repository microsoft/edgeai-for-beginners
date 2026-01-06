<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ac31463ae3ed21a0ce83b0a351c23dd4",
  "translation_date": "2026-01-05T09:57:15+00:00",
  "source_file": "README.md",
  "language_code": "ro"
}
-->
# EdgeAI pentru începători


![Imaginea de copertă a cursului](../../translated_images/cover.eb18d1b9605d754b.ro.png)

[![Contribuitori GitHub](https://img.shields.io/github/contributors/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/graphs/contributors)
[![Probleme GitHub](https://img.shields.io/github/issues/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/issues)
[![Cereri de tragere GitHub](https://img.shields.io/github/issues-pr/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/pulls)
[![PR-uri binevenite](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

[![Observatori GitHub](https://img.shields.io/github/watchers/microsoft/edgeai-for-beginners.svg?style=social&label=Watch)](https://GitHub.com/microsoft/edgeai-for-beginners/watchers)
[![Furci GitHub](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork)
[![Stele GitHub](https://img.shields.io/github/stars/microsoft/edgeai-for-beginners?style=social&label=Star)](https://GitHub.com/microsoft/edgeai-for-beginners/stargazers)


[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Urmați acești pași pentru a începe să folosiți aceste resurse:

1. **Fork Repository-ul**: Click pe [![Furci GitHub](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork)
2. **Clonează Repository-ul**:   `git clone https://github.com/microsoft/edgeai-for-beginners.git`
3. [**Alătură-te Discord-ului Azure AI Foundry și întâlnește experți și alți dezvoltatori**](https://discord.com/invite/ByRwuEEgH4)


### 🌐 Suport multilingv

#### Susținut prin GitHub Action (automatizat și întotdeauna actualizat)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabă](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgară](../bg/README.md) | [Birmaneză (Myanmar)](../my/README.md) | [Chineză (simplificată)](../zh/README.md) | [Chineză (tradițională, Hong Kong)](../hk/README.md) | [Chineză (tradițională, Macau)](../mo/README.md) | [Chineză (tradițională, Taiwan)](../tw/README.md) | [Croată](../hr/README.md) | [Ceha](../cs/README.md) | [Daneză](../da/README.md) | [Olandeză](../nl/README.md) | [Estonă](../et/README.md) | [Finlandeză](../fi/README.md) | [Franceză](../fr/README.md) | [Germană](../de/README.md) | [Greacă](../el/README.md) | [Ebraică](../he/README.md) | [Hindi](../hi/README.md) | [Maghiară](../hu/README.md) | [Indoneziană](../id/README.md) | [Italiană](../it/README.md) | [Japoneză](../ja/README.md) | [Kannada](../kn/README.md) | [Coreeană](../ko/README.md) | [Lituaniană](../lt/README.md) | [Malaysiană](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepaleză](../ne/README.md) | [Pidgin Nigerian](../pcm/README.md) | [Norvegiană](../no/README.md) | [Persană (Farsi)](../fa/README.md) | [Poloneză](../pl/README.md) | [Portugheză (Brazilia)](../br/README.md) | [Portugheză (Portugalia)](../pt/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Română](./README.md) | [Rusă](../ru/README.md) | [Sârbă (chirilică)](../sr/README.md) | [Slovacă](../sk/README.md) | [Slovenă](../sl/README.md) | [Spaniolă](../es/README.md) | [Swahili](../sw/README.md) | [Suedeză](../sv/README.md) | [Tagalog (Filipineză)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thailandeză](../th/README.md) | [Turcă](../tr/README.md) | [Ucraineană](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnameză](../vi/README.md)

> **Preferi să clonezi local?**

> Acest repository include traduceri în peste 50 de limbi, ceea ce crește semnificativ dimensiunea descărcării. Pentru a clona fără traduceri, folosește sparse checkout:
> ```bash
> git clone --filter=blob:none --sparse https://github.com/microsoft/edgeai-for-beginners.git
> cd edgeai-for-beginners
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
> Acest lucru îți oferă tot ce ai nevoie pentru a finaliza cursul cu o descărcare mult mai rapidă.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

**Dacă dorești să se adauge limbi suplimentare pentru traducere, ele sunt listate [aici](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md)**
## Introducere

Bun venit la **EdgeAI pentru începători** – călătoria ta cuprinzătoare în lumea transformatoare a Inteligenței Artificiale la margine (Edge). Acest curs face puntea între capacitățile puternice ale AI-ului și implementarea practică, în lumea reală, pe dispozitive edge, oferindu-ți puterea de a valorifica potențialul AI direct acolo unde se generează datele și unde trebuie luate decizii.

### Ce vei stăpâni

Acest curs te duce de la concepte fundamentale la implementări gata de producție, acoperind:
- **Modele lingvistice mici (SLMs)** optimizate pentru implementare la margine
- **Optimizare conștientă de hardware** pe diverse platforme
- **Inferență în timp real** cu capabilități de protecție a vieții private
- **Strategii de implementare** pentru aplicații enterprise

### De ce contează EdgeAI

Edge AI reprezintă o schimbare de paradigmă care răspunde provocărilor moderne critice:
- **Confidențialitate & Securitate**: Procesează date sensibile local, fără expunere în cloud
- **Performanță în timp real**: Elimină latența rețelei pentru aplicații critice de timp
- **Eficiență de cost**: Reducerea costurilor de bandă și cloud computing
- **Operațiuni reziliente**: Menține funcționalitatea în cazul întreruperilor de rețea
- **Conformitate cu reglementările**: Respectă cerințele privind suveranitatea datelor

### Edge AI

Edge AI se referă la rularea algoritmilor AI și a modelelor lingvistice local, pe hardware, aproape de locul unde se generează datele, fără a depinde de resurse cloud pentru inferență. Reduce latența, sporește confidențialitatea și permite luarea deciziilor în timp real.

### Principii de bază:
- **Inferență pe dispozitiv**: Modelele AI rulează pe dispozitive edge (telefoane, routere, microcontrolere, PC-uri industriale)
- **Funcționare offline**: Funcționează fără conectivitate persistentă la internet
- **Latență scăzută**: Răspunsuri imediate, potrivite pentru sisteme în timp real
- **Suveranitate asupra datelor**: Păstrează datele sensibile local, sporind securitatea și conformitatea

### Modele lingvistice mici (SLMs)

SLM-uri precum Phi-4, Mistral-7B și Gemma sunt versiuni optimizate ale LLM-urilor mai mari – antrenate sau distilate pentru:
- **Amprentă de memorie redusă**: Utilizare eficientă a memoriei limitate a dispozitivelor edge
- **Cerere redusă de calcul**: Optimizate pentru performanța CPU și GPU edge
- **Timpuri rapide de pornire**: Inițializare rapidă pentru aplicații receptive

Ele deblochează capabilități puternice NLP în timp ce respectă constrângerile:
- **Sisteme integrate**: Dispozitive IoT și controlere industriale
- **Dispozitive mobile**: Smartphone-uri și tablete cu capabilități offline
- **Dispozitive IoT**: Senzori și dispozitive inteligente cu resurse limitate
- **Servere edge**: Unități locale de procesare cu resurse GPU limitate
- **Calculatoare personale**: Scenarii de implementare desktop și laptop

## Modulele cursului și navigare

| Modului | Subiect | Domeniu de interes | Conținut principal | Nivel | Durată |
|--------|---------|--------------------|--------------------|-------|---------|
| [📖 00 ](./introduction.md) | [Introducere în EdgeAI](./introduction.md) | Fundamente & Context | Prezentare EdgeAI • Aplicații în industrie • Introducere SLM • Obiective de învățare | Începător | 1-2 ore |
| [📚 01](../../Module01) | [Fundamente EdgeAI](./Module01/README.md) | Comparare Cloud vs Edge AI | Fundamente EdgeAI • Studii de caz din lumea reală • Ghid de implementare • Implementare la margine | Începător | 3-4 ore |
| [🧠 02](../../Module02) | [Fundamentele modelelor SLM](./Module02/README.md) | Familii de modele & arhitectură | Familia Phi • Familia Qwen • Familia Gemma • BitNET • μModel • Phi-Silica | Începător | 4-5 ore |
| [🚀 03](../../Module03) | [Practica implementării SLM](./Module03/README.md) | Implementare locală & cloud | Învățare avansată • Mediu local • Implementare cloud | Intermediar | 4-5 ore |
| [⚙️ 04](../../Module04) | [Kit de optimizare modele](./Module04/README.md) | Optimizare cross-platform | Introducere • Llama.cpp • Microsoft Olive • OpenVINO • Apple MLX • Sinteză flux de lucru | Intermediar | 5-6 ore |
| [🔧 05](../../Module05) | [Operațiuni SLMOps în producție](./Module05/README.md) | Operațiuni în producție | Introducere SLMOps • Distilare modele • Fine-tuning • Implementare în producție | Avansat | 5-6 ore |
| [🤖 06](../../Module06) | [Agenți AI & Apelare funcții](./Module06/README.md) | Cadre de agent & MCP | Introducere agenți • Apelare funcții • Protocol context modele | Avansat | 4-5 ore |
| [💻 07](../../Module07) | [Implementare platformă](./Module07/README.md) | Exemple cross-platform | Kit AI • Foundry Local • Dezvoltare Windows | Avansat | 3-4 ore |
| [🏭 08](../../Module08) | [Kit Foundry Local](./Module08/README.md) | Exemple gata de producție | Aplicații exemplu (detalii mai jos) | Expert | 8-10 ore |

### 🏭 **Modulul 08: Aplicații exemplu**

- [01: REST Chat Quickstart](./Module08/samples/01/README.md)
- [02: Integrare OpenAI SDK](./Module08/samples/02/README.md)
- [03: Descoperire modele & teste comparative](./Module08/samples/03/README.md)
- [04: Aplicație Chainlit RAG](./Module08/samples/04/README.md)
- [05: Orchestrarea multi-agent](./Module08/samples/05/README.md)
- [06: Router Models-as-Tools](./Module08/samples/06/README.md)
- [07: Client API direct](./Module08/samples/07/README.md)
- [08: Aplicație chat Windows 11](./Module08/samples/08/README.md)
- [09: Sistem multi-agent avansat](./Module08/samples/09/README.md)
- [10: Cadru pentru Foundry Tools](./Module08/samples/10/README.md)

### 🎓 **Atelier: Parcurs practic de învățare**

Materiale complete pentru atelier practice cu implementări gata de producție:

- **[Ghid atelier](./Workshop/Readme.md)** - Obiective complete de învățare, rezultate și navigare în resurse
- **Exemple Python** (6 sesiuni) - Actualizate cu cele mai bune practici, gestionare erori și documentație completă
- **Jupyter Notebooks** (8 interactive) - Tutoriale pas cu pas cu referințe și monitorizare a performanței
- **Ghiduri sesiuni** - Ghiduri detaliate în markdown pentru fiecare sesiune de atelier
- **Instrumente de validare** - Scripturi pentru verificarea calității codului și teste rapide

**Ce vei construi:**
- Aplicații chat AI locale cu suport streaming
- Pipeline-uri RAG cu evaluare de calitate (RAGAS)
- Instrumente de testare comparativă multi-model
- Sisteme de orchestrare multi-agent
- Rutare inteligentă a modelelor cu selecție pe bază de sarcini

### 🎙️ **Atelier pentru Agentic: Practic - Studioul AI Podcast**

Construiește un pipeline de producție podcast AI de la zero! Acest atelier imersiv te învață să creezi un sistem multi-agent complet care transformă ideile în episoade profesioniste de podcast.
**[🎬 Începe Atelierul AI Podcast Studio](./WorkshopForAgentic/README.md)**

**Misiunea ta**: Lansează "Future Bytes" — un podcast tech complet alimentat de agenți AI pe care îi vei construi singur. Fără dependențe cloud, fără costuri API — totul rulează local pe calculatorul tău.

**Ce face acest proiect unic:**
- **🤖 Orchestrare reală Multi-Agent** - Construiește agenți AI specializați care cercetează, scriu și produc audio
- **🎯 Trilul complet de producție** - De la selecția temei până la audio-ul final al podcastului
- **💻 Implementare 100% Locală** - Folosește Ollama și modele locale (Qwen-3-8B) pentru intimitate și control total
- **🎤 Integrare Text-la-Vorbire** - Transformă scenariile în conversații naturale cu mai mulți vorbitori
- **✋ Fluxuri de lucru cu implicare umană** - Porți de aprobare asigură calitatea menținând automatizarea

**Călătoria de învățare în trei acte:**

| Act | Focus | Abilități Cheie | Durată |
|-----|-------|-----------------|--------|
| **[Act 1: Cunoaște-ți Asistenții AI](./WorkshopForAgentic/md/01.BuildAIAgentWithSLM.md)** | Construiește primul tău agent AI | Integrarea uneltelor • Căutare web • Rezolvare de probleme • Raționament agentic | 2-3 ore |
| **[Act 2: Adună Echipa de Producție](./WorkshopForAgentic/md/02.AIAgentOrchestrationAndWorkflows.md)** | Orchestrarea mai multor agenți | Coordonează echipa • Fluxuri de aprobare • Interfața DevUI • Supravegherea umană | 3-4 ore |
| **[Act 3: Adu Podcastul la Viață](./WorkshopForAgentic/md/03.Multi-SpeakerPodcastGenerationWithVibeVoice.md)** | Generează audio de podcast | Text-la-vorbire • Sinteză multi-vorbitor • Audio pe termen lung • Automatizare completă | 2-3 ore |

**Tehnologii utilizate:**
- **Microsoft Agent Framework** - Orchestrarea și coordonarea agenților multipli
- **Ollama** - Motor local de modele AI (fără cloud necesar)
- **Qwen-3-8B** - Model lingvistic open-source optimizat pentru sarcini agentice
- **API-uri Text-la-Vorbire** - Sinteză vocală naturală pentru generarea podcasturilor

**Suport hardware:**
- ✅ **Mod CPU** - Funcționează pe orice calculator modern (8GB+ RAM recomandat)
- 🚀 **Accelerație GPU** - Inferență semnificativ mai rapidă cu GPU-uri NVIDIA/AMD
- ⚡ **Suport NPU** - Accelerație prin unitate neurală de ultimă generație

**Perfect pentru:**
- Dezvoltatori care învață sisteme AI multi-agent
- Oricine este interesat de automatizarea AI și fluxuri de lucru
- Creatori de conținut care explorează producția asistată de AI
- Studenți care studiază pattern-uri practice de orchestrare AI

**Începe să construiești**: [🎙️ Atelierul AI Podcast Studio →](./WorkshopForAgentic/README.md)

### 📊 **Sumar al traseului de învățare**
- **Durată totală**: 36-45 ore
- **Traseul începător**: Modulele 01-02 (7-9 ore)  
- **Traseul intermediar**: Modulele 03-04 (9-11 ore)
- **Traseul avansat**: Modulele 05-07 (12-15 ore)
- **Traseul expert**: Modulul 08 (8-10 ore)

## Ce vei construi

### 🎯 Competențe de bază
- **Arhitectură Edge AI**: Proiectează sisteme AI cu prioritate locală și integrare cloud
- **Optimizare modele**: Cuantifică și comprimă modelele pentru implementare edge (creștere de viteză cu 85%, reducere de dimensiune cu 75%)
- **Implementare multiplatformă**: Windows, mobil, embedded, sisteme hibride cloud-edge
- **Operații de producție**: Monitorizare, scalare și întreținere AI-edge în producție

### 🏗️ Proiecte practice
- **Aplicații de chat Foundry Local**: Aplicație nativă Windows 11 cu comutare între modele
- **Sisteme multi-agent**: Coordonator cu agenți specialiști pentru fluxuri de lucru complexe  
- **Aplicații RAG**: Procesare locală documente cu căutare vectorială
- **Routere de modele**: Selecție inteligentă între modele bazată pe analiza sarcinilor
- **Framework-uri API**: Clienți pregătiți pentru producție cu streaming și monitorizare sănătate
- **Unelte cross-platform**: Modele de integrare LangChain/Semantic Kernel

### 🏢 Aplicații în industrie
**Producție** • **Sănătate** • **Vehicule autonome** • **Orașe inteligente** • **Aplicații mobile**

## Pornire rapidă

**Traseul recomandat de învățare** (20-30 ore total):

0. **📖 Introducere** ([Introduction.md](./introduction.md)): Fundamente EdgeAI + context industrial + cadru de învățare
1. **📚 Fundament** (Module 01-02): Concepte EdgeAI + familii de modele SLM
2. **⚙️ Optimizare** (Module 03-04): Implementare + cadre de cuantificare  
3. **🚀 Producție** (Module 05-06): SLMOps + agenți AI + apelare de funcții
4. **💻 Implementare** (Module 07-08): Exemple platforme + kit Foundry Local

Fiecare modul include teorie, exerciții practice și mostre de cod pregătit pentru producție.

## Impact în carieră

**Roluri tehnice**: Arhitect soluții EdgeAI • Inginer ML (Edge) • Dezvoltator AI IoT • Dezvoltator AI mobil

**Sectore industriale**: Producție 4.0 • Tehnologie în sănătate • Sisteme autonome • FinTech • Electronice de consum

**Proiecte în portofoliu**: Sisteme multi-agent • Aplicații RAG de producție • Implementare cross-platform • Optimizare performanță

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
✅ **Studii de caz reale**: Microsoft, Japan Airlines, implementări enterprise  
✅ **Exemple practice**: Peste 50 de exemple, 10 demo-uri cuprinzătoare Foundry Local  
✅ **Focus pe performanță**: Îmbunătățire a vitezei cu 85%, reducere a dimensiunii cu 75%  
✅ **Multi-platformă**: Windows, mobil, embedded, hybrid cloud-edge  
✅ **Pregătit pentru producție**: Monitorizare, scalare, securitate, cadre de conformitate

📖 **[Ghid de studiu disponibil](STUDY_GUIDE.md)**: Traseu structurat de 20 de ore cu alocare de timp și instrumente de autoevaluare.

---

**EdgeAI reprezintă viitorul implementării AI**: local-first, care respectă intimitatea și eficient. Stăpânește aceste abilități pentru a crea următoarea generație de aplicații inteligente.

## Alte cursuri

Echipa noastră produce și alte cursuri! Vezi:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j pentru începători](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js pentru începători](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)

---

### Azure / Edge / MCP / Agenți
[![AZD pentru începători](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Edge AI pentru începători](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP pentru începători](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Agenți AI pentru începători](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Seria Generativ AI
[![Generativ AI pentru începători](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Generativ AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![Generativ AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![Generativ AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### Învățare de bază
[![ML pentru începători](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![Data Science pentru începători](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![AI pentru începători](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![Securitate cibernetică pentru începători](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![Dezvoltare web pentru începători](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![IoT pentru începători](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![Dezvoltare XR pentru începători](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Seria Copilot
[![Copilot pentru programare asistată AI](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot for C#/.NET](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot Adventure](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## Obținerea de ajutor

Dacă întâmpini dificultăți sau ai întrebări despre crearea aplicațiilor AI, alătură-te:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Dacă ai feedback despre produs sau erori în timpul dezvoltării, vizitează:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:  
Acest document a fost tradus folosind serviciul de traducere automată AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să țineți cont că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite ce pot rezulta din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8421c922085232ba081c848d98f69f35",
  "translation_date": "2026-01-01T10:59:50+00:00",
  "source_file": "README.md",
  "language_code": "it"
}
-->
# EdgeAI per principianti 


![Immagine di copertina del corso](../../translated_images/cover.eb18d1b9605d754b.it.png)

[![Contributori GitHub](https://img.shields.io/github/contributors/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/graphs/contributors)
[![Problemi GitHub](https://img.shields.io/github/issues/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/issues)
[![Richieste pull GitHub](https://img.shields.io/github/issues-pr/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/pulls)
[![PRs benvenute](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

[![Discord di Microsoft Foundry](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Segui questi passaggi per iniziare a usare queste risorse:

1. **Crea un fork del repository**: Fai clic su [![Fork GitHub](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork)
2. **Clona il repository**:   `git clone https://github.com/microsoft/edgeai-for-beginners.git`
3. [**Unisciti al Discord dell'Azure AI Foundry e incontra esperti e colleghi sviluppatori**](https://discord.com/invite/ByRwuEEgH4)


### 🌐 Supporto multilingue

#### Supportato tramite GitHub Action (Automatico e sempre aggiornato)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabo](../ar/README.md) | [Bengalese](../bn/README.md) | [Bulgaro](../bg/README.md) | [Birmano (Myanmar)](../my/README.md) | [Cinese (semplificato)](../zh/README.md) | [Cinese (tradizionale, Hong Kong)](../hk/README.md) | [Cinese (tradizionale, Macao)](../mo/README.md) | [Cinese (tradizionale, Taiwan)](../tw/README.md) | [Croato](../hr/README.md) | [Ceco](../cs/README.md) | [Danese](../da/README.md) | [Olandese](../nl/README.md) | [Estone](../et/README.md) | [Finlandese](../fi/README.md) | [Francese](../fr/README.md) | [Tedesco](../de/README.md) | [Greco](../el/README.md) | [Ebraico](../he/README.md) | [Hindi](../hi/README.md) | [Ungherese](../hu/README.md) | [Indonesiano](../id/README.md) | [Italiano](./README.md) | [Giapponese](../ja/README.md) | [Kannada](../kn/README.md) | [Coreano](../ko/README.md) | [Lituano](../lt/README.md) | [Malese](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Pidgin nigeriano](../pcm/README.md) | [Norvegese](../no/README.md) | [Persiano (Farsi)](../fa/README.md) | [Polacco](../pl/README.md) | [Portoghese (Brasile)](../br/README.md) | [Portoghese (Portogallo)](../pt/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romeno](../ro/README.md) | [Russo](../ru/README.md) | [Serbo (Cirillico)](../sr/README.md) | [Slovacco](../sk/README.md) | [Sloveno](../sl/README.md) | [Spagnolo](../es/README.md) | [Swahili](../sw/README.md) | [Svedese](../sv/README.md) | [Tagalog (Filippino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thailandese](../th/README.md) | [Turco](../tr/README.md) | [Ucraino](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamita](../vi/README.md)
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

**Se desideri aggiungere altre lingue, quelle supportate sono elencate [qui](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md)**
## Introduzione

Benvenuto a **EdgeAI per principianti** – il tuo percorso completo nel mondo trasformativo dell'Intelligenza Artificiale Edge. Questo corso colma il divario tra potenti capacità di IA e il deployment pratico e reale su dispositivi edge, permettendoti di sfruttare il potenziale dell'IA direttamente dove i dati vengono generati e dove devono essere prese le decisioni.

### Cosa imparerai

Questo corso ti porta dai concetti fondamentali fino a implementazioni pronte per la produzione, coprendo:
- **Piccoli modelli linguistici (SLMs)** ottimizzati per il deployment su edge
- **Ottimizzazione consapevole dell'hardware** su piattaforme diverse
- **Inferenza in tempo reale** con capacità di preservare la privacy
- **Strategie di deployment in produzione** per applicazioni enterprise

### Perché EdgeAI è importante

Edge AI rappresenta un cambio di paradigma che affronta sfide critiche moderne:
- **Privacy e sicurezza**: Elabora i dati sensibili localmente senza esposizione al cloud
- **Prestazioni in tempo reale**: Elimina la latenza di rete per applicazioni critiche nel tempo
- **Efficienza dei costi**: Riduce larghezza di banda e spese per il cloud computing
- **Operazioni resilienti**: Mantiene la funzionalità durante interruzioni di rete
- **Conformità normativa**: Soddisfa i requisiti di sovranità dei dati

### Edge AI

Edge AI si riferisce all'esecuzione di algoritmi di IA e modelli linguistici localmente sull'hardware, vicino al luogo in cui i dati vengono generati, senza fare affidamento su risorse cloud per l'inferenza. Riduce la latenza, migliora la privacy e permette decisioni in tempo reale.

### Principi fondamentali:
- **Inferenza on-device**: I modelli AI vengono eseguiti sui dispositivi edge (telefoni, router, microcontrollori, PC industriali)
- **Capacità offline**: Funziona senza connettività internet persistente
- **Bassa latenza**: Risposte immediate adatte ai sistemi in tempo reale
- **Sovranità dei dati**: Mantiene i dati sensibili localmente, migliorando sicurezza e conformità

### Piccoli modelli linguistici (SLMs)

I SLM come Phi-4, Mistral-7B e Gemma sono versioni ottimizzate di LLM più grandi—addestrate o distillate per:
- **Ridotto consumo di memoria**: Uso efficiente della memoria limitata dei dispositivi edge
- **Minore richiesta di calcolo**: Ottimizzati per prestazioni su CPU e GPU edge
- **Tempi di avvio più rapidi**: Inizializzazione veloce per applicazioni reattive

Sbloccano potenti capacità NLP rispettando i vincoli di:
- **Sistemi embedded**: Dispositivi IoT e controller industriali
- **Dispositivi mobili**: Smartphone e tablet con funzionalità offline
- **Dispositivi IoT**: Sensori e dispositivi intelligenti con risorse limitate
- **Server edge**: Unità di elaborazione locali con risorse GPU limitate
- **Personal Computer**: Scenari di deployment su desktop e laptop

## Moduli del corso & Navigazione

| Modulo | Argomento | Area di interesse | Contenuto chiave | Livello | Durata |
|--------|-------|------------|-------------|--------|----------|
| [📖 00 ](./introduction.md) | [Introduzione a EdgeAI](./introduction.md) | Fondamenti e contesto | Panoramica di EdgeAI • Applicazioni industriali • Introduzione agli SLM • Obiettivi di apprendimento | Principiante | 1-2 ore |
| [📚 01](../../Module01) | [Fondamenti di EdgeAI](./Module01/README.md) | Confronto Cloud vs Edge AI | Fondamenti di EdgeAI • Casi di studio reali • Guida all'implementazione • Deployment su Edge | Principiante | 3-4 ore |
| [🧠 02](../../Module02) | [Fondamenti dei modelli SLM](./Module02/README.md) | Famiglie di modelli e architettura | Famiglia Phi • Famiglia Qwen • Famiglia Gemma • BitNET • μModel • Phi-Silica | Principiante | 4-5 ore |
| [🚀 03](../../Module03) | [Pratica di deployment SLM](./Module03/README.md) | Deployment locale e cloud | Apprendimento avanzato • Ambiente locale • Deployment su cloud | Intermedio | 4-5 ore |
| [⚙️ 04](../../Module04) | [Toolkit di ottimizzazione dei modelli](./Module04/README.md) | Ottimizzazione cross-platform | Introduzione • Llama.cpp • Microsoft Olive • OpenVINO • Apple MLX • Sintesi del workflow | Intermedio | 5-6 ore |
| [🔧 05](../../Module05) | [SLMOps in produzione](./Module05/README.md) | Operazioni di produzione | Introduzione a SLMOps • Distillazione del modello • Fine-tuning • Deployment in produzione | Avanzato | 5-6 ore |
| [🤖 06](../../Module06) | [Agenti AI e Function Calling](./Module06/README.md) | Framework agent e MCP | Introduzione agli agenti • Function Calling • Model Context Protocol | Avanzato | 4-5 ore |
| [💻 07](../../Module07) | [Implementazione della piattaforma](./Module07/README.md) | Esempi cross-platform | AI Toolkit • Foundry Local • Sviluppo Windows | Avanzato | 3-4 ore |
| [🏭 08](../../Module08) | [Toolkit Foundry Local](./Module08/README.md) | Esempi pronti per la produzione | Applicazioni di esempio (vedi dettagli sotto) | Esperto | 8-10 ore |

### 🏭 **Modulo 08: Applicazioni di esempio**

- [01: Avvio rapido REST Chat](./Module08/samples/01/README.md)
- [02: Integrazione SDK OpenAI](./Module08/samples/02/README.md)
- [03: Scoperta del modello e benchmarking](./Module08/samples/03/README.md)
- [04: Applicazione Chainlit RAG](./Module08/samples/04/README.md)
- [05: Orchestrazione multi-agente](./Module08/samples/05/README.md)
- [06: Router Modelli-come-Strumenti](./Module08/samples/06/README.md)
- [07: Client API diretto](./Module08/samples/07/README.md)
- [08: App Chat per Windows 11](./Module08/samples/08/README.md)
- [09: Sistema multi-agente avanzato](./Module08/samples/09/README.md)
- [10: Framework Foundry Tools](./Module08/samples/10/README.md)

### 🎓 **Workshop: Percorso pratico di apprendimento**

Materiali completi del workshop pratico con implementazioni pronte per la produzione:

- **[Guida al workshop](./Workshop/Readme.md)** - Obiettivi di apprendimento completi, risultati e navigazione delle risorse
- **Esempi in Python** (6 sessioni) - Aggiornati con le migliori pratiche, gestione degli errori e documentazione completa
- **Jupyter Notebooks** (8 interattivi) - Tutorial passo-passo con benchmark e monitoraggio delle prestazioni
- **Guide delle sessioni** - Guide dettagliate in markdown per ogni sessione del workshop
- **Strumenti di convalida** - Script per verificare la qualità del codice ed eseguire test smoke

**Cosa costruirai:**
- Applicazioni di chat AI locali con supporto per lo streaming
- Pipeline RAG con valutazione della qualità (RAGAS)
- Strumenti di benchmarking e confronto multi-modello
- Sistemi di orchestrazione multi-agente
- Instradamento intelligente dei modelli con selezione basata sul compito

### 📊 **Riepilogo del percorso di apprendimento**
- **Durata totale**: 36-45 ore
- **Percorso Principiante**: Moduli 01-02 (7-9 ore)  
- **Percorso Intermedio**: Moduli 03-04 (9-11 ore)
- **Percorso Avanzato**: Moduli 05-07 (12-15 ore)
- **Percorso Esperto**: Modulo 08 (8-10 ore)

## Cosa costruirai

### 🎯 Competenze principali
- **Architettura Edge AI**: Progettare sistemi AI orientati al locale con integrazione cloud
- **Ottimizzazione dei modelli**: Quantizzare e comprimere i modelli per il deployment ai bordi (aumento della velocità dell'85%, riduzione delle dimensioni del 75%)
- **Distribuzione multipiattaforma**: Windows, mobile, embedded e sistemi ibridi cloud-edge
- **Operazioni di produzione**: Monitoraggio, scalabilità e manutenzione dell'AI ai bordi in produzione

### 🏗️ Progetti Pratici
- **Applicazioni di chat Foundry Local**: applicazione nativa per Windows 11 con cambio modello
- **Sistemi Multi-Agente**: Coordinatore con agenti specialisti per flussi di lavoro complessi  
- **Applicazioni RAG**: elaborazione di documenti locali con ricerca vettoriale
- **Router di modelli**: Selezione intelligente tra modelli basata sull'analisi del compito
- **Framework API**: client pronti per la produzione con streaming e monitoraggio dello stato
- **Strumenti multipiattaforma**: pattern di integrazione LangChain/Semantic Kernel

### 🏢 Applicazioni Industriali
**Manifatturiero** • **Sanità** • **Veicoli Autonomi** • **Città Intelligenti** • **App mobili**

## Avvio Rapido

**Percorso di apprendimento consigliato** (20-30 ore totali):

0. **📖 Introduzione** ([Introduction.md](./introduction.md)): Fondamenti di EdgeAI + contesto industriale + framework di apprendimento
1. **📚 Fondamenti** (Moduli 01-02): concetti di EdgeAI + famiglie di modelli SLM
2. **⚙️ Ottimizzazione** (Moduli 03-04): Deployment + framework di quantizzazione  
3. **🚀 Produzione** (Moduli 05-06): SLMOps + agenti AI + function calling
4. **💻 Implementazione** (Moduli 07-08): esempi per piattaforma + toolkit Foundry Local

Ogni modulo include teoria, esercizi pratici e esempi di codice pronti per la produzione.

## Impatto sulla Carriera

**Ruoli Tecnici**: Architetto Soluzioni EdgeAI • Ingegnere ML (Edge) • Sviluppatore AI IoT • Sviluppatore AI Mobile

**Settori Industriali**: Manifattura 4.0 • Tecnologie per la Salute • Sistemi Autonomi • FinTech • Elettronica di consumo

**Progetti per il Portfolio**: Sistemi multi-agente • App RAG di produzione • Deployment multipiattaforma • Ottimizzazione delle prestazioni

## Struttura del Repository

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

## Punti salienti del corso

✅ **Apprendimento progressivo**: Teoria → Pratica → Distribuzione in produzione  
✅ **Casi di studio reali**: Microsoft, Japan Airlines, implementazioni aziendali  
✅ **Esempi pratici**: 50+ esempi, 10 demo complete di Foundry Local  
✅ **Focus sulle prestazioni**: miglioramenti di velocità dell'85%, riduzioni delle dimensioni del 75%  
✅ **Multipiattaforma**: Windows, mobile, embedded, ibrido cloud-edge  
✅ **Pronto per la produzione**: monitoraggio, scalabilità, sicurezza, framework di conformità

📖 **[Guida di studio disponibile](STUDY_GUIDE.md)**: Percorso di apprendimento strutturato di 20 ore con indicazioni sulla distribuzione del tempo e strumenti di autovalutazione.

---

**EdgeAI rappresenta il futuro del deployment AI**: incentrato sul locale, rispettoso della privacy ed efficiente. Padroneggia queste competenze per costruire la prossima generazione di applicazioni intelligenti.

## Altri Corsi

Il nostro team produce altri corsi! Dai un'occhiata:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j per Principianti](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js per Principianti](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)

---

### Azure / Edge / MCP / Agenti
[![AZD per Principianti](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Edge AI per Principianti](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP per Principianti](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Agenti AI per Principianti](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Serie IA Generativa
[![IA Generativa per Principianti](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![IA Generativa (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![IA Generativa (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![IA Generativa (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### Apprendimento di base
[![ML per Principianti](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![Data Science per Principianti](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![IA per Principianti](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![Sicurezza informatica per Principianti](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![Sviluppo Web per Principianti](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![IoT per Principianti](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![Sviluppo XR per Principianti](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Serie Copilot
[![Copilot per Programmazione Affiancata con AI](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot per C#/.NET](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Avventura Copilot](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## Ottenere aiuto

Se rimani bloccato o hai domande sulla creazione di app AI, unisciti a:

[![Discord di Microsoft Foundry](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Se hai feedback sul prodotto o errori durante lo sviluppo visita:

[![Forum degli sviluppatori Microsoft Foundry](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Dichiarazione di non responsabilità:
Questo documento è stato tradotto utilizzando il servizio di traduzione basato su IA Co-op Translator (https://github.com/Azure/co-op-translator). Pur impegnandoci per l'accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua originale deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un traduttore umano. Non ci assumiamo alcuna responsabilità per eventuali malintesi o interpretazioni errate derivanti dall'uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
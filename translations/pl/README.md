# EdgeAI dla początkujących


![Obraz okładki kursu](../../translated_images/pl/cover.eb18d1b9605d754b.webp)

[![Współtwórcy na GitHub](https://img.shields.io/github/contributors/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/graphs/contributors)
[![Problemy na GitHub](https://img.shields.io/github/issues/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/issues)
[![Pull requesty na GitHub](https://img.shields.io/github/issues-pr/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/pulls)
[![Zapraszamy PR](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

[![Obserwujący na GitHub](https://img.shields.io/github/watchers/microsoft/edgeai-for-beginners.svg?style=social&label=Watch)](https://GitHub.com/microsoft/edgeai-for-beginners/watchers)
[![Repozytorium na fork](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork)
[![Gwiazdy na GitHub](https://img.shields.io/github/stars/microsoft/edgeai-for-beginners?style=social&label=Star)](https://GitHub.com/microsoft/edgeai-for-beginners/stargazers)


[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Wykonaj poniższe kroki, aby rozpocząć korzystanie z tych zasobów:

1. **Sforkuj repozytorium**: Kliknij [![Repozytorium na fork](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork)
2. **Sklonuj repozytorium**:   `git clone https://github.com/microsoft/edgeai-for-beginners.git`
3. [**Dołącz do Discord Azure AI Foundry i spotkaj ekspertów oraz innych programistów**](https://discord.com/invite/ByRwuEEgH4)


### 🌐 Wsparcie wielu języków

#### Obsługiwane przez GitHub Action (Automatyczne i zawsze aktualne)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabski](../ar/README.md) | [Bengalski](../bn/README.md) | [Bułgarski](../bg/README.md) | [Birmański (Myanmar)](../my/README.md) | [Chiński (uproszczony)](../zh-CN/README.md) | [Chiński (tradycyjny, Hongkong)](../zh-HK/README.md) | [Chiński (tradycyjny, Makau)](../zh-MO/README.md) | [Chiński (tradycyjny, Tajwan)](../zh-TW/README.md) | [Chorwacki](../hr/README.md) | [Czeski](../cs/README.md) | [Duński](../da/README.md) | [Holenderski](../nl/README.md) | [Estoński](../et/README.md) | [Fiński](../fi/README.md) | [Francuski](../fr/README.md) | [Niemiecki](../de/README.md) | [Grecki](../el/README.md) | [Hebrajski](../he/README.md) | [Hindi](../hi/README.md) | [Węgierski](../hu/README.md) | [Indonezyjski](../id/README.md) | [Włoski](../it/README.md) | [Japoński](../ja/README.md) | [Kannada](../kn/README.md) | [Koreański](../ko/README.md) | [Litewski](../lt/README.md) | [Malajski](../ms/README.md) | [Malajalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepalski](../ne/README.md) | [Nigeryjski pidgin](../pcm/README.md) | [Norweski](../no/README.md) | [Perski (farsi)](../fa/README.md) | [Polski](./README.md) | [Portugalski (Brazylia)](../pt-BR/README.md) | [Portugalski (Portugalia)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Rumuński](../ro/README.md) | [Rosyjski](../ru/README.md) | [Serbski (cyrylica)](../sr/README.md) | [Słowacki](../sk/README.md) | [Słoweński](../sl/README.md) | [Hiszpański](../es/README.md) | [Suahili](../sw/README.md) | [Szwedzki](../sv/README.md) | [Tagalog (Filipiński)](../tl/README.md) | [Tamilski](../ta/README.md) | [Telugu](../te/README.md) | [Tajski](../th/README.md) | [Turecki](../tr/README.md) | [Ukraiński](../uk/README.md) | [Urdu](../ur/README.md) | [Wietnamski](../vi/README.md)

> **Wolisz klonować lokalnie?**

> To repozytorium zawiera ponad 50 tłumaczeń językowych, co znacząco zwiększa rozmiar pobierania. Aby klonować bez tłumaczeń, użyj sparse checkout:
> ```bash
> git clone --filter=blob:none --sparse https://github.com/microsoft/edgeai-for-beginners.git
> cd edgeai-for-beginners
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
> Dzięki temu otrzymujesz wszystko, co potrzebne, aby ukończyć kurs, a pobieranie jest dużo szybsze.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

**Jeśli chcesz, aby obsługiwane były dodatkowe języki tłumaczeń, są one wymienione [tutaj](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md)**
## Wprowadzenie

Witamy w **EdgeAI dla początkujących** – Twojej kompleksowej podróży po przełomowym świecie Edge Artificial Intelligence. Ten kurs łączy potężne możliwości AI z praktycznym wdrożeniem w urządzeniach brzegowych, umożliwiając Ci wykorzystanie potencjału AI bezpośrednio tam, gdzie generowane są dane i muszą być podejmowane decyzje.

### Czego się nauczysz

Ten kurs prowadzi Cię od podstawowych pojęć do wdrożeń gotowych do produkcji, obejmując:
- **Małe modele językowe (SLM)** zoptymalizowane pod kątem wdrożeń na brzeg
- **Optymalizację świadomą sprzętu** na różnych platformach
- **Wnioskowanie w czasie rzeczywistym** z zachowaniem prywatności
- **Strategie wdrożenia produkcyjnego** dla zastosowań korporacyjnych

### Dlaczego EdgeAI ma znaczenie

Edge AI to zmiana paradygmatu, która rozwiązuje krytyczne wyzwania współczesności:
- **Prywatność i bezpieczeństwo**: przetwarzaj dane wrażliwe lokalnie, bez narażania chmury
- **Wydajność w czasie rzeczywistym**: eliminuj opóźnienia sieci dla aplikacji krytycznych czasowo
- **Efektywność kosztowa**: zmniejsz koszty przepustowości i chmury obliczeniowej
- **Odporne działanie**: utrzymuj funkcjonalność podczas przerw w sieci
- **Zgodność regulacyjna**: spełnij wymagania dotyczące suwerenności danych

### Edge AI

Edge AI oznacza uruchamianie algorytmów AI i modeli językowych lokalnie na sprzęcie, blisko miejsca generowania danych, bez polegania na zasobach chmury podczas wnioskowania. Zmniejsza opóźnienia, zwiększa prywatność i umożliwia podejmowanie decyzji w czasie rzeczywistym.

### Podstawowe zasady:
- **Wnioskowanie na urządzeniu**: modele AI działają na urządzeniach brzegowych (telefony, routery, mikrokontrolery, komputery przemysłowe)
- **Możliwość działania offline**: działanie bez stałego połączenia z internetem
- **Niskie opóźnienia**: natychmiastowa reakcja odpowiednia dla systemów czasu rzeczywistego
- **Suwerenność danych**: przechowuje dane wrażliwe lokalnie, zwiększając bezpieczeństwo i zgodność

### Małe modele językowe (SLM)

SLM, takie jak Phi-4, Mistral-7B i Gemma, to zoptymalizowane wersje większych modeli LLM — wytrenowane lub zdestylowane pod kątem:
- **Zmniejszonego zapotrzebowania pamięciowego**: efektywne wykorzystanie ograniczonej pamięci na urządzeniach brzegowych
- **Niższego zapotrzebowania na moc obliczeniową**: zoptymalizowane do działania na CPU i GPU na brzegu
- **Szybszego uruchamiania**: szybka inicjalizacja dla responsywnych aplikacji

Odblokowują potężne możliwości NLP, spełniając jednocześnie ograniczenia:
- **Systemy wbudowane**: urządzenia IoT i kontrolery przemysłowe
- **Urządzenia mobilne**: smartfony i tablety z możliwością pracy offline
- **Urządzenia IoT**: czujniki i inteligentne urządzenia z ograniczonymi zasobami
- **Serwery brzegowe**: lokalne jednostki przetwarzające z ograniczonymi zasobami GPU
- **Komputery osobiste**: scenariusze wdrożenia na desktopach i laptopach

## Moduły kursu i nawigacja

| Moduł | Temat | Obszar fokusowy | Kluczowa zawartość | Poziom | Czas trwania |
|--------|-------|------------|-------------|--------|----------|
| [📖 00 ](./introduction.md) | [Wprowadzenie do EdgeAI](./introduction.md) | Fundamenty i kontekst | Przegląd EdgeAI • Zastosowania w branży • Wprowadzenie do SLM • Cele nauki | Początkujący | 1-2 godziny |
| [📚 01](../../Module01) | [Podstawy EdgeAI](./Module01/README.md) | Porównanie chmury i Edge AI | Podstawy EdgeAI • Studia przypadków z rzeczywistego świata • Przewodnik wdrożeniowy • Wdrożenie na brzegu | Początkujący | 3-4 godziny |
| [🧠 02](../../Module02) | [Fundamenty modeli SLM](./Module02/README.md) | Rodziny modeli i architektura | Rodzina Phi • Rodzina Qwen • Rodzina Gemma • BitNET • μModel • Phi-Silica | Początkujący | 4-5 godzin |
| [🚀 03](../../Module03) | [Praktyka wdrażania SLM](./Module03/README.md) | Wdrożenia lokalne i chmura | Zaawansowane nauczanie • Środowisko lokalne • Wdrożenie w chmurze | Średniozaawansowany | 4-5 godzin |
| [⚙️ 04](../../Module04) | [Zestaw narzędzi optymalizacji modeli](./Module04/README.md) | Optymalizacja wieloplatformowa | Wprowadzenie • Llama.cpp • Microsoft Olive • OpenVINO • Apple MLX • Synteza workflow | Średniozaawansowany | 5-6 godzin |
| [🔧 05](../../Module05) | [SLMOps w produkcji](./Module05/README.md) | Operacje produkcyjne | Wprowadzenie do SLMOps • Destylacja modeli • Fine-tuning • Wdrożenie produkcyjne | Zaawansowany | 5-6 godzin |
| [🤖 06](../../Module06) | [Agenci AI i wywołania funkcji](./Module06/README.md) | Frameworki agentów i MCP | Wprowadzenie do agentów • Wywoływanie funkcji • Protokół kontekstu modelu | Zaawansowany | 4-5 godzin |
| [💻 07](../../Module07) | [Implementacja platformy](./Module07/README.md) | Przykłady wieloplatformowe | Zestaw narzędzi AI • Foundry Local • Programowanie na Windows | Zaawansowany | 3-4 godziny |
| [🏭 08](../../Module08) | [Foundry Local Toolkit](./Module08/README.md) | Przykłady gotowe do produkcji | Przykładowe aplikacje (szczegóły poniżej) | Ekspert | 8-10 godzin |

### 🏭 **Moduł 08: Przykładowe aplikacje**

- [01: REST Chat Quickstart](./Module08/samples/01/README.md)
- [02: Integracja OpenAI SDK](./Module08/samples/02/README.md)
- [03: Odkrywanie modelu i benchmarki](./Module08/samples/03/README.md)
- [04: Aplikacja Chainlit RAG](./Module08/samples/04/README.md)
- [05: Orkiestracja multi-agentowa](./Module08/samples/05/README.md)
- [06: Router modele-jako-narzędzia](./Module08/samples/06/README.md)
- [07: Bezpośredni klient API](./Module08/samples/07/README.md)
- [08: Aplikacja czatu Windows 11](./Module08/samples/08/README.md)
- [09: Zaawansowany system multi-agentowy](./Module08/samples/09/README.md)
- [10: Framework narzędzi Foundry](./Module08/samples/10/README.md)

### 🎓 **Warsztat: Ścieżka praktycznej nauki**

Kompleksowe materiały warsztatowe z wdrożeniami gotowymi do produkcji:

- **[Przewodnik warsztatowy](./Workshop/Readme.md)** - Pełne cele nauki, rezultaty i nawigacja zasobów
- **Przykłady w Python** (6 sesji) - Aktualizowane z najlepszymi praktykami, obsługą błędów i pełną dokumentacją
- **Notatniki Jupyter** (8 interaktywnych) - Samouczki krok po kroku z benchmarkami i monitorowaniem wydajności
- **Przewodniki sesji** - Szczegółowe przewodniki markdown dla każdej sesji warsztatowej
- **Narzędzia walidacyjne** - Skrypty do sprawdzania jakości kodu i testów dymnych

**Co zbudujesz:**
- Lokalne aplikacje czatu AI z obsługą strumieniowania
- Pipeline RAG z oceną jakości (RAGAS)
- Narzędzia do benchmarkingu i porównywania wielu modeli
- Systemy orkiestracji multi-agentowej
- Inteligentny routing modeli z wyborem opartym na zadaniach

### 🎙️ **Warsztat dla Agentic: Praktyczne - Studio podcastu AI**

Zbuduj od podstaw produkcyjny pipeline podcastów zasilany AI! Ten immersyjny warsztat uczy tworzenia kompletnego systemu multi-agentowego, który przekształca pomysły w profesjonalne odcinki podcastów.
**[🎬 Rozpocznij Warsztaty Studia Podcastu AI](./WorkshopForAgentic/README.md)**

**Twoja misja**: Uruchom "Future Bytes" — podcast technologiczny całkowicie napędzany przez agentów AI, których sam zbudujesz. Bez zależności od chmury, bez kosztów API — wszystko działa lokalnie na Twoim komputerze.

**Co czyni to unikalnym:**
- **🤖 Prawdziwa orkiestracja wieloagentowa** - Buduj wyspecjalizowanych agentów AI, którzy badają, piszą i produkują dźwięk
- **🎯 Kompletny proces produkcji** - Od wyboru tematu do finalnego pliku podcastu
- **💻 100% lokalne uruchomienie** - Używa Ollama i lokalnych modeli (Qwen-3-8B) dla pełnej prywatności i kontroli
- **🎤 Integracja tekst-na-mowę** - Przekształcaj skrypty w naturalnie brzmiące rozmowy wielu mówców
- **✋ Workflow z udziałem człowieka** - Bramy zatwierdzania gwarantują jakość przy jednoczesnej automatyzacji

**Podróż naukowa w trzech aktach:**

| Akt | Fokus | Kluczowe umiejętności | Czas trwania |
|-----|-------|----------------------|--------------|
| **[Akt 1: Poznaj swoich asystentów AI](./WorkshopForAgentic/md/01.BuildAIAgentWithSLM.md)** | Zbuduj swojego pierwszego agenta AI | Integracja narzędzi • Wyszukiwanie w sieci • Rozwiązywanie problemów • Agentyczne rozumowanie | 2-3 godz. |
| **[Akt 2: Zbierz swój zespół produkcyjny](./WorkshopForAgentic/md/02.AIAgentOrchestrationAndWorkflows.md)** | Orkiestracja wielu agentów | Koordynacja zespołu • Workflow zatwierdzania • Interfejs DevUI • Nadzór człowieka | 3-4 godz. |
| **[Akt 3: Ożyw swój podcast](./WorkshopForAgentic/md/03.Multi-SpeakerPodcastGenerationWithVibeVoice.md)** | Generowanie dźwięku podcastu | Tekst-na-mowę • Synteza wielu mówców • Długie formy audio • Pełna automatyzacja | 2-3 godz. |

**Wykorzystane technologie:**
- **Microsoft Agent Framework** - Orkiestracja i koordynacja wielu agentów
- **Ollama** - Lokalne środowisko dla modeli AI (bez chmury)
- **Qwen-3-8B** - Otwarty model językowy zoptymalizowany pod zadania agentyczne
- **API tekst-na-mowę** - Naturalna synteza głosu do generowania podcastów

**Wsparcie sprzętowe:**
- ✅ **Tryb CPU** - Działa na każdym nowoczesnym komputerze (zalecane 8GB+ RAM)
- 🚀 **Przyspieszenie GPU** - Znacznie szybsze wnioskowanie przy NVIDIA/AMD GPU
- ⚡ **Wsparcie NPU** - Przyspieszenie za pomocą jednostek przetwarzania neuronowego następnej generacji

**Idealne dla:**
- Developerów uczących się systemów wieloagentowych AI
- Każdego zainteresowanego automatyzacją i workflow AI
- Twórców treści eksplorujących produkcję wspomaganą przez AI
- Studentów studiujących praktyczne wzorce orkiestracji AI

**Zacznij budować**: [🎙️ Warsztaty Studia Podcastu AI →](./WorkshopForAgentic/README.md)

### 📊 **Podsumowanie ścieżki nauki**
- **Całkowity czas**: 36-45 godzin
- **Ścieżka dla początkujących**: Moduły 01-02 (7-9 godzin)  
- **Ścieżka średniozaawansowana**: Moduły 03-04 (9-11 godzin)
- **Ścieżka zaawansowana**: Moduły 05-07 (12-15 godzin)
- **Ścieżka ekspercka**: Moduł 08 (8-10 godzin)

## Co zbudujesz

### 🎯 Kluczowe kompetencje
- **Edge AI Architecture**: Projektowanie systemów AI z podejściem lokalnym i integracją chmury
- **Optymalizacja modeli**: Kwantyzacja i kompresja modeli dla wdrożeń edge (85% wzrost prędkości, 75% redukcja rozmiaru)
- **Wielo-platformowość**: Windows, urządzenia mobilne, embedded oraz systemy hybrydowe cloud-edge
- **Operacje produkcyjne**: Monitorowanie, skalowanie i utrzymanie edge AI w produkcji

### 🏗️ Projekty praktyczne
- **Aplikacje czatu Foundry Local**: natywna aplikacja Windows 11 z przełączaniem modeli
- **Systemy wieloagentowe**: Koordynator z agentami specjalistycznymi dla złożonych workflow  
- **Aplikacje RAG**: lokalne przetwarzanie dokumentów z wyszukiwaniem wektorowym
- **Routery modeli**: Inteligentny wybór modeli na podstawie analizy zadania
- **Frameworki API**: Klienci produkcyjni z przepływem strumieniowym i monitorowaniem stanu
- **Narzędzia multiplatformowe**: wzorce integracji LangChain/Semantic Kernel

### 🏢 Zastosowania przemysłowe
**Produkcja** • **Opieka zdrowotna** • **Pojazdy autonomiczne** • **Inteligentne miasta** • **Aplikacje mobilne**

## Szybki start

**Rekomendowana ścieżka nauki** (łącznie 20-30 godzin):

0. **📖 Wprowadzenie** ([Introduction.md](./introduction.md)): Podstawy EdgeAI + kontekst branżowy + ramy nauki
1. **📚 Fundamenty** (Moduły 01-02): Koncepcje EdgeAI + rodziny modeli SLM
2. **⚙️ Optymalizacja** (Moduły 03-04): Frameworki wdrożeniowe i kwantyzacyjne  
3. **🚀 Produkcja** (Moduły 05-06): SLMOps + agenci AI + wywoływanie funkcji
4. **💻 Implementacja** (Moduły 07-08): Przykłady platform + zestaw narzędzi Foundry Local

Każdy moduł zawiera teorię, ćwiczenia praktyczne oraz gotowe przykłady kodu produkcyjnego.

## Wpływ na karierę

**Role techniczne**: Architekt rozwiązań EdgeAI • Inżynier ML (Edge) • Programista AI IoT • Programista AI mobilny

**Branże**: Produkcja 4.0 • Technologia zdrowotna • Systemy autonomiczne • FinTech • Elektronika konsumencka

**Projekty w portfolio**: Systemy wieloagentowe • Produkcyjne aplikacje RAG • Wdrożenia multiplatformowe • Optymalizacja wydajności

## Struktura repozytorium

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

## Najważniejsze punkty kursu

✅ **Stopniowa nauka**: Teoria → Praktyka → Wdrożenie produkcyjne  
✅ **Realne studia przypadków**: Microsoft, Japan Airlines, wdrożenia korporacyjne  
✅ **Przykłady praktyczne**: 50+ przykładów, 10 kompleksowych demonstracji Foundry Local  
✅ **Skupienie na wydajności**: 85% wzrostu prędkości, 75% zmniejszenia rozmiaru  
✅ **Wielo-platformowość**: Windows, mobilne, embedded, hybryda cloud-edge  
✅ **Gotowość produkcyjna**: Monitorowanie, skalowanie, bezpieczeństwo, zgodność

📖 **[Dostępny przewodnik nauki](STUDY_GUIDE.md)**: Strukturalna 20-godzinna ścieżka nauki z podziałem czasu i narzędziami samooceny.

---

**EdgeAI to przyszłość wdrożeń AI**: podejście lokalne, chroniące prywatność i efektywne. Opanuj te umiejętności, by budować kolejną generację inteligentnych aplikacji.

## Inne kursy

Nasz zespół tworzy również inne kursy! Sprawdź:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j for Beginners](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js for Beginners](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)
[![LangChain for Beginners](https://img.shields.io/badge/LangChain%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://github.com/microsoft/langchain-for-beginners?WT.mc_id=m365-94501-dwahlin)
---

### Azure / Edge / MCP / Agenci
[![AZD for Beginners](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Edge AI for Beginners](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP for Beginners](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![AI Agents for Beginners](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Seria dotycząca AI generatywnej
[![Generative AI for Beginners](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Generative AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![Generative AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![Generative AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### Podstawowa nauka
[![ML for Beginners](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![Data Science for Beginners](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![AI for Beginners](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![Cybersecurity for Beginners](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![Web Dev for Beginners](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![IoT for Beginners](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![XR Development for Beginners](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Seria Copilot

[![Copilot for AI Paired Programming](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot for C#/.NET](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot Adventure](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## Uzyskiwanie pomocy

Jeśli utkniesz lub masz pytania dotyczące tworzenia aplikacji AI, dołącz do:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Jeśli masz uwagi dotyczące produktu lub błędy podczas tworzenia odwiedź:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Wyłączenie odpowiedzialności**:
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczeń AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mimo że dokładamy starań, aby tłumaczenie było precyzyjne, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Za wiarygodne źródło należy uznać oryginalny dokument w jego języku źródłowym. W przypadku informacji krytycznych zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
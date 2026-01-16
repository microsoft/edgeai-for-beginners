<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ac31463ae3ed21a0ce83b0a351c23dd4",
  "translation_date": "2026-01-05T09:22:57+00:00",
  "source_file": "README.md",
  "language_code": "pl"
}
-->
# EdgeAI dla początkujących 


![Okładka kursu](../../translated_images/pl/cover.eb18d1b9605d754b.png)

[![Współtwórcy GitHub](https://img.shields.io/github/contributors/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/graphs/contributors)
[![Zgłoszenia problemów GitHub](https://img.shields.io/github/issues/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/issues)
[![Prośby o pull GitHub](https://img.shields.io/github/issues-pr/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/pulls)
[![Prośby o PR mile widziane](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

[![Obserwujący GitHub](https://img.shields.io/github/watchers/microsoft/edgeai-for-beginners.svg?style=social&label=Watch)](https://GitHub.com/microsoft/edgeai-for-beginners/watchers)
[![Forki GitHub](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork)
[![Gwiazdki GitHub](https://img.shields.io/github/stars/microsoft/edgeai-for-beginners?style=social&label=Star)](https://GitHub.com/microsoft/edgeai-for-beginners/stargazers)


[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Wykonaj poniższe kroki, aby rozpocząć korzystanie z tych zasobów:

1. **Zrób fork repozytorium**: Kliknij [![Forki GitHub](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork)
2. **Sklonuj repozytorium**:   `git clone https://github.com/microsoft/edgeai-for-beginners.git`
3. [**Dołącz do Discord Azure AI Foundry i poznaj ekspertów oraz innych deweloperów**](https://discord.com/invite/ByRwuEEgH4)


### 🌐 Wielojęzyczne wsparcie

#### Obsługiwane przez GitHub Action (zautomatyzowane i zawsze aktualne)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabski](../ar/README.md) | [Bengalski](../bn/README.md) | [Bułgarski](../bg/README.md) | [Birmański (Myanmar)](../my/README.md) | [Chiński (uproszczony)](../zh/README.md) | [Chiński (tradycyjny, Hongkong)](../hk/README.md) | [Chiński (tradycyjny, Makau)](../mo/README.md) | [Chiński (tradycyjny, Tajwan)](../tw/README.md) | [Chorwacki](../hr/README.md) | [Czeski](../cs/README.md) | [Duński](../da/README.md) | [Holenderski](../nl/README.md) | [Estoński](../et/README.md) | [Fiński](../fi/README.md) | [Francuski](../fr/README.md) | [Niemiecki](../de/README.md) | [Grecki](../el/README.md) | [Hebrajski](../he/README.md) | [Hindi](../hi/README.md) | [Węgierski](../hu/README.md) | [Indonezyjski](../id/README.md) | [Włoski](../it/README.md) | [Japoński](../ja/README.md) | [Kannada](../kn/README.md) | [Koreański](../ko/README.md) | [Litewski](../lt/README.md) | [Malajski](../ms/README.md) | [Malajalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepalski](../ne/README.md) | [Nigeryjski Pidgin](../pcm/README.md) | [Norweski](../no/README.md) | [Perski (Farsi)](../fa/README.md) | [Polski](./README.md) | [Portugalski (Brazylia)](../br/README.md) | [Portugalski (Portugalia)](../pt/README.md) | [Pendżabski (Gurmukhi)](../pa/README.md) | [Rumuński](../ro/README.md) | [Rosyjski](../ru/README.md) | [Serbski (cyrylica)](../sr/README.md) | [Słowacki](../sk/README.md) | [Słoweński](../sl/README.md) | [Hiszpański](../es/README.md) | [Suahili](../sw/README.md) | [Szwedzki](../sv/README.md) | [Tagalog (Filipiński)](../tl/README.md) | [Tamilski](../ta/README.md) | [Telugu](../te/README.md) | [Tajski](../th/README.md) | [Turecki](../tr/README.md) | [Ukraiński](../uk/README.md) | [Urdu](../ur/README.md) | [Wietnamski](../vi/README.md)

> **Wolisz klonować lokalnie?**

> To repozytorium zawiera tłumaczenia na ponad 50 języków, co znacznie zwiększa rozmiar pobierania. Aby sklonować bez tłumaczeń, użyj sparse checkout:
> ```bash
> git clone --filter=blob:none --sparse https://github.com/microsoft/edgeai-for-beginners.git
> cd edgeai-for-beginners
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
> To daje wszystko, czego potrzebujesz, aby ukończyć kurs z dużo szybszym pobieraniem.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

**Jeśli chcesz, aby dodatkowe języki tłumaczeń były wspierane, są one wymienione [tutaj](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md)**
## Wprowadzenie

Witamy w **EdgeAI dla początkujących** – Twojej wszechstronnej podróży po transformującym świecie Sztucznej Inteligencji Edge. Ten kurs łączy potężne możliwości SI z praktycznym wdrożeniem w urządzeniach edge, umożliwiając Ci wykorzystanie potencjału SI bezpośrednio tam, gdzie generowane są dane i podejmowane są decyzje.

### Czego się nauczysz

Ten kurs przeprowadzi Cię od podstawowych pojęć do implementacji gotowych do produkcji, obejmując:
- **Małe modele językowe (SLM)** zoptymalizowane pod kątem wdrożeń edge
- **Optymalizację z uwzględnieniem sprzętu** na różnorodnych platformach
- **Wnioskowanie w czasie rzeczywistym** z zachowaniem prywatności
- **Strategie wdrożeń produkcyjnych** dla zastosowań przedsiębiorczych

### Dlaczego EdgeAI jest ważne

Edge AI to paradygmat, który sprosta kluczowym wyzwaniom współczesności:
- **Prywatność i bezpieczeństwo**: Przetwarzaj dane wrażliwe lokalnie bez narażenia na chmurę
- **Wydajność w czasie rzeczywistym**: Eliminuj opóźnienia sieciowe w aplikacjach krytycznych czasowo
- **Efektywność kosztowa**: Zmniejsz koszty przepustowości i obliczeń w chmurze
- **Odporność operacji**: Utrzymuj działanie podczas awarii sieci
- **Zgodność regulacyjna**: Spełniaj wymagania suwerenności danych

### Edge AI

Edge AI oznacza wykonywanie algorytmów SI i modeli językowych lokalnie na sprzęcie, blisko miejsca generowania danych, bez polegania na zasobach chmury do inferencji. Zmniejsza to opóźnienia, zwiększa prywatność i umożliwia podejmowanie decyzji w czasie rzeczywistym.

### Główne zasady:
- **Inferencja na urządzeniu**: Modele SI działają na urządzeniach edge (telefony, routery, mikrokontrolery, industrialne PC)
- **Funkcjonowanie offline**: Działa bez stałego połączenia z internetem
- **Niskie opóźnienia**: Natychmiastowe odpowiedzi dostosowane do systemów czasu rzeczywistego
- **Suwerenność danych**: Dane wrażliwe pozostają lokalnie, zwiększając bezpieczeństwo i zgodność

### Małe modele językowe (SLM)

SLM, takie jak Phi-4, Mistral-7B i Gemma, to zoptymalizowane wersje większych LLM — trenowane lub destylowane w celu:
- **Zmniejszonego zużycia pamięci**: Efektywne wykorzystanie ograniczonej pamięci urządzeń edge
- **Niższych wymagań obliczeniowych**: Optymalizacja pod kątem CPU i GPU edge
- **Szybszego startu**: Szybka inicjalizacja dla responsywnych aplikacji

Umożliwiają potężne możliwości NLP, spełniając jednocześnie ograniczenia:
- **Systemy wbudowane**: Urządzenia IoT i kontrolery przemysłowe
- **Urządzenia mobilne**: Smartfony i tablety z funkcjami offline
- **Urządzenia IoT**: Czujniki i inteligentne urządzenia o ograniczonych zasobach
- **Serwery edge**: Lokalne jednostki przetwarzające z ograniczonymi zasobami GPU
- **Komputery osobiste**: Scenariusze wdrożeń desktopowych i laptopowych

## Moduły kursu i nawigacja

| Moduł | Temat | Obszar skupienia | Kluczowe treści | Poziom | Czas trwania |
|--------|-------|------------------|-----------------|--------|--------------|
| [📖 00 ](./introduction.md) | [Wprowadzenie do EdgeAI](./introduction.md) | Fundamenty i kontekst | Przegląd EdgeAI • Zastosowania w branży • Wprowadzenie do SLM • Cele nauki | Początkujący | 1-2 godziny |
| [📚 01](../../Module01) | [Podstawy EdgeAI](./Module01/README.md) | Porównanie chmura vs edge AI | Podstawy EdgeAI • Studium przypadków realnych • Przewodnik wdrożeniowy • Deployment na edge | Początkujący | 3-4 godziny |
| [🧠 02](../../Module02) | [Podstawy modeli SLM](./Module02/README.md) | Rodziny modeli i architektura | Rodzina Phi • Rodzina Qwen • Rodzina Gemma • BitNET • μModel • Phi-Silica | Początkujący | 4-5 godzin |
| [🚀 03](../../Module03) | [Praktyka wdrożenia SLM](./Module03/README.md) | Lokalny i chmurowy deployment | Zaawansowane nauczanie • Środowisko lokalne • Deployment w chmurze | Średniozaawansowany | 4-5 godzin |
| [⚙️ 04](../../Module04) | [Zestaw narzędzi optymalizacji modeli](./Module04/README.md) | Optymalizacja wieloplatformowa | Wprowadzenie • Llama.cpp • Microsoft Olive • OpenVINO • Apple MLX • Synteza workflow | Średniozaawansowany | 5-6 godzin |
| [🔧 05](../../Module05) | [Produkcja SLMOps](./Module05/README.md) | Operacje produkcyjne | Wprowadzenie do SLMOps • Destylacja modeli • Dostosowywanie • Deployment produkcyjny | Zaawansowany | 5-6 godzin |
| [🤖 06](../../Module06) | [Agent AI & wywoływanie funkcji](./Module06/README.md) | Frameworki agentów i MCP | Wprowadzenie do agentów • Wywoływanie funkcji • Protokół kontekstu modeli | Zaawansowany | 4-5 godzin |
| [💻 07](../../Module07) | [Implementacja platformy](./Module07/README.md) | Przykłady międzyplatformowe | Zestaw AI • Foundry Local • Rozwój Windows | Zaawansowany | 3-4 godziny |
| [🏭 08](../../Module08) | [Foundry Local Toolkit](./Module08/README.md) | Przykłady gotowe do produkcji | Przykładowe aplikacje (szczegóły poniżej) | Ekspert | 8-10 godzin |

### 🏭 **Moduł 08: Przykładowe aplikacje**

- [01: REST Chat Quickstart](./Module08/samples/01/README.md)
- [02: Integracja OpenAI SDK](./Module08/samples/02/README.md)
- [03: Odkrywanie modeli & benchmarking](./Module08/samples/03/README.md)
- [04: Aplikacja Chainlit RAG](./Module08/samples/04/README.md)
- [05: Orkiestracja multi-agentów](./Module08/samples/05/README.md)
- [06: Router modele-jako-narzędzia](./Module08/samples/06/README.md)
- [07: Bezpośredni klient API](./Module08/samples/07/README.md)
- [08: Aplikacja chat Windows 11](./Module08/samples/08/README.md)
- [09: Zaawansowany system multi-agentów](./Module08/samples/09/README.md)
- [10: Framework Foundry Tools](./Module08/samples/10/README.md)

### 🎓 **Warsztat: Ścieżka nauki praktycznej**

Kompleksowe materiały warsztatowe z implementacjami produkcyjnymi:

- **[Przewodnik warsztatowy](./Workshop/Readme.md)** - Kompletny cel nauki, oczekiwane wyniki i nawigacja zasobów
- **Przykłady w Pythonie** (6 sesji) - Aktualizowane o najlepsze praktyki, obsługę błędów i pełną dokumentację
- **Notatniki Jupyter** (8 interaktywnych) - Tutoriale krok po kroku z benchmarkami i monitorowaniem wydajności
- **Przewodniki sesji** - Szczegółowe instrukcje w markdown dla każdej sesji warsztatu
- **Narzędzia walidacyjne** - Skrypty do weryfikacji jakości kodu i testów wstępnych

**Co zbudujesz:**
- Lokalne aplikacje AI do czatu ze wsparciem streamingu
- Pipeline RAG z oceną jakości (RAGAS)
- Narzędzia do benchmarkingu i porównania wielu modeli
- Systemy orkiestracji multi-agentów
- Inteligentny routing modeli z selekcją zadań

### 🎙️ **Warsztat agentowy: Praktyczne - Studio podcastów AI**

Zbuduj pipeline produkcji podcastów wspomagany AI od podstaw! Ten immersyjny warsztat nauczy Cię tworzenia kompletnego systemu multi-agentów, który zmienia idee w profesjonalne odcinki podcastu.
**[🎬 Rozpocznij warsztaty AI Podcast Studio](./WorkshopForAgentic/README.md)**

**Twoja misja**: Uruchom "Future Bytes" — podcast technologiczny w pełni napędzany przez agentów AI, których sam zbudujesz. Bez zależności od chmury, bez kosztów API — wszystko działa lokalnie na twoim komputerze.

**Co czyni to wyjątkowym:**
- **🤖 Prawdziwa wieloagentowa orkiestracja** – Buduj specjalistyczne agentów AI, którzy badają, piszą i produkują audio
- **🎯 Kompletny pipeline produkcyjny** – Od wyboru tematu aż do finalnego pliku audio podcastu
- **💻 Wdrożenie w 100% lokalne** – Wykorzystuje Ollamę i lokalne modele (Qwen-3-8B) dla pełnej prywatności i kontroli
- **🎤 Integracja tekst-na-mowę** – Przekształcaj skrypty w naturalnie brzmiące rozmowy wielogłosowe
- **✋ Przepływy pracy z udziałem człowieka** – Bramy zatwierdzania zapewniają jakość przy zachowaniu automatyzacji

**Nauka w trzech aktach:**

| Akt | Skupienie | Kluczowe umiejętności | Czas trwania |
|-----|-----------|-----------------------|--------------|
| **[Akt 1: Poznaj swoich asystentów AI](./WorkshopForAgentic/md/01.BuildAIAgentWithSLM.md)** | Zbuduj swojego pierwszego agenta AI | Integracja narzędzi • Wyszukiwanie w sieci • Rozwiązywanie problemów • Rozumowanie agentowe | 2-3 godziny |
| **[Akt 2: Zbierz swój zespół produkcyjny](./WorkshopForAgentic/md/02.AIAgentOrchestrationAndWorkflows.md)** | Orkiestruj wielu agentów | Koordynacja zespołu • Przepływy zatwierdzania • Interfejs DevUI • Nadzór człowieka | 3-4 godziny |
| **[Akt 3: Ożyw swój podcast](./WorkshopForAgentic/md/03.Multi-SpeakerPodcastGenerationWithVibeVoice.md)** | Generuj audio podcastu | Tekst na mowę • Synteza wielogłosowa • Długie formy audio • Pełna automatyzacja | 2-3 godziny |

**Wykorzystane technologie:**
- **Microsoft Agent Framework** – Orkiestracja i koordynacja wielu agentów
- **Ollama** – Lokalny runtime modeli AI (bez konieczności chmury)
- **Qwen-3-8B** – Otwarty model językowy zoptymalizowany do zadań agentowych
- **API tekst-na-mowę** – Naturalna synteza głosu dla produkcji podcastów

**Wsparcie sprzętowe:**
- ✅ **Tryb CPU** – Działa na każdym nowoczesnym komputerze (zalecane 8GB+ RAM)
- 🚀 **Akceleracja GPU** – Znacznie szybsze inferencje na GPU NVIDIA/AMD
- ⚡ **Wsparcie NPU** – Akceleracja na procesorach neuronowych nowej generacji

**Idealne dla:**
- Programistów uczących się systemów wieloagentowych AI
- Osób zainteresowanych automatyzacją AI i przepływami pracy
- Twórców treści eksplorujących produkcję wspieraną przez AI
- Studentów studiujących praktyczne wzorce orkiestracji AI

**Zacznij budować**: [🎙️ Warsztaty AI Podcast Studio →](./WorkshopForAgentic/README.md)

### 📊 **Podsumowanie ścieżki nauki**
- **Całkowity czas**: 36-45 godzin
- **Ścieżka początkująca**: Moduły 01-02 (7-9 godzin)  
- **Ścieżka średniozaawansowana**: Moduły 03-04 (9-11 godzin)
- **Ścieżka zaawansowana**: Moduły 05-07 (12-15 godzin)
- **Ścieżka ekspert**: Moduł 08 (8-10 godzin)

## Co zbudujesz

### 🎯 Kluczowe kompetencje
- **Architektura Edge AI**: Projektuj systemy AI lokalne z integracją chmury
- **Optymalizacja modeli**: Kwantyzacja i kompresja modeli do wdrożeń brzegowych (85% wzrost prędkości, 75% redukcja rozmiaru)
- **Wielo-platformowe wdrożenia**: Windows, mobile, systemy wbudowane, hybryda chmura-brzeg
- **Operacje produkcyjne**: Monitorowanie, skalowanie i utrzymanie Edge AI w produkcji

### 🏗️ Projekty praktyczne
- **Aplikacje Foundry Local Chat**: Aplikacja natywna Windows 11 z przełączaniem modeli
- **Systemy wieloagentowe**: Koordynator z agentami specjalistycznymi dla skomplikowanych przepływów  
- **Aplikacje RAG**: Lokalna obróbka dokumentów z wyszukiwaniem wektorowym
- **Routery modeli**: Inteligentny wybór modelu na podstawie analizy zadania
- **Frameworki API**: Klienci produkcyjni z obsługą strumieni i monitorowaniem stanu
- **Narzędzia wieloplatformowe**: Wzorce integracji LangChain/Semantic Kernel

### 🏢 Zastosowania branżowe
**Produkcja** • **Opieka zdrowotna** • **Systemy autonomiczne** • **Inteligentne miasta** • **Aplikacje mobilne**

## Szybki start

**Rekomendowana ścieżka nauki** (łącznie 20-30 godzin):

0. **📖 Wprowadzenie** ([Introduction.md](./introduction.md)): Podstawy EdgeAI + kontekst branżowy + ramy nauki
1. **📚 Fundamenty** (Moduły 01-02): Koncepcje EdgeAI + rodziny modeli SLM
2. **⚙️ Optymalizacja** (Moduły 03-04): Wdrożenia + frameworki kwantyzacji  
3. **🚀 Produkcja** (Moduły 05-06): SLMOps + agenci AI + wywoływanie funkcji
4. **💻 Implementacja** (Moduły 07-08): Przykłady platform + zestaw narzędzi Foundry Local

Każdy moduł zawiera teorię, ćwiczenia praktyczne oraz przykłady kodu gotowego do produkcji.

## Wpływ na karierę

**Role techniczne**: Architekt rozwiązań EdgeAI • Inżynier ML (Edge) • Developer AI IoT • Mobile AI Developer

**Sektory przemysłowe**: Przemysł 4.0 • Technologia zdrowotna • Systemy autonomiczne • FinTech • Elektronika użytkowa

**Projekty w portfolio**: Systemy wieloagentowe • Produkcyjne aplikacje RAG • Wieloplatformowe wdrożenia • Optymalizacja wydajności

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

## Najważniejsze elementy kursu

✅ **Progresywna nauka**: Teoria → Praktyka → Wdrożenie produkcyjne  
✅ **Rzeczywiste studia przypadków**: Microsoft, Japan Airlines, wdrożenia korporacyjne  
✅ **Przykłady praktyczne**: 50+ przykładów, 10 kompleksowych demonstracji Foundry Local  
✅ **Koncentracja na wydajności**: 85% wzrost prędkości, 75% redukcja rozmiaru  
✅ **Wielo-platformowość**: Windows, mobile, wbudowane, hybryda chmura-brzeg  
✅ **Gotowość do produkcji**: Monitorowanie, skalowanie, bezpieczeństwo, ramy zgodności

📖 **[Dostępny przewodnik po nauce](STUDY_GUIDE.md)**: Strukturalna ścieżka nauki na 20 godzin z wskazówkami dotyczącymi czasu i narzędziami samooceny.

---

**EdgeAI to przyszłość wdrożeń AI**: priorytet lokalny, ochrona prywatności i efektywność. Opanuj te umiejętności, aby budować nową generację inteligentnych aplikacji.

## Inne kursy

Nasz zespół tworzy też inne kursy! Sprawdź:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j dla początkujących](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js dla początkujących](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)

---

### Azure / Edge / MCP / Agenci
[![AZD dla początkujących](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Edge AI dla początkujących](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP dla początkujących](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Agenci AI dla początkujących](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Seria Generatywna AI
[![Generatywne AI dla początkujących](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Generatywne AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![Generatywne AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![Generatywne AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### Podstawy nauki
[![ML dla początkujących](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![Data Science dla początkujących](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![AI dla początkujących](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![Cyberbezpieczeństwo dla początkujących](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![Web Dev dla początkujących](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![IoT dla początkujących](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![XR Development dla początkujących](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Seria Copilot
[![Copilot dla AI Paired Programming](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot for C#/.NET](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot Adventure](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## Uzyskiwanie pomocy

Jeśli utkniesz lub masz jakiekolwiek pytania dotyczące tworzenia aplikacji AI, dołącz do:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Jeśli masz uwagi dotyczące produktu lub napotkasz błędy podczas tworzenia, odwiedź:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:  
Niniejszy dokument został przetłumaczony przy użyciu usługi tłumaczeń AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dokładamy starań, aby tłumaczenie było jak najdokładniejsze, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w języku źródłowym powinien być uznawany za autorytatywne źródło. W przypadku informacji krytycznych zalecamy skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za wszelkie nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
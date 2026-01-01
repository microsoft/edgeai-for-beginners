<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8421c922085232ba081c848d98f69f35",
  "translation_date": "2026-01-01T11:02:08+00:00",
  "source_file": "README.md",
  "language_code": "pl"
}
-->
# EdgeAI dla początkujących 


![Obraz okładki kursu](../../translated_images/cover.eb18d1b9605d754b.pl.png)

[![Współtwórcy GitHub](https://img.shields.io/github/contributors/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/graphs/contributors)
[![Zgłoszenia GitHub](https://img.shields.io/github/issues/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/issues)
[![Pull requesty GitHub](https://img.shields.io/github/issues-pr/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/pulls)
[![Pull requesty mile widziane](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

[![Discord Microsoft Foundry](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Wykonaj następujące kroki, aby rozpocząć korzystanie z tych zasobów:

1. **Sforkuj repozytorium**: Kliknij [![GitHub forks](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork)
2. **Sklonuj repozytorium**:   `git clone https://github.com/microsoft/edgeai-for-beginners.git`
3. [**Dołącz do Discorda Azure AI Foundry i poznaj ekspertów oraz innych deweloperów**](https://discord.com/invite/ByRwuEEgH4)


### 🌐 Wsparcie wielojęzyczne

#### Wspierane przez GitHub Action (automatyczne i zawsze aktualne)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabski](../ar/README.md) | [Bengalski](../bn/README.md) | [Bułgarski](../bg/README.md) | [Birmański (Myanmar)](../my/README.md) | [Chiński (uproszczony)](../zh/README.md) | [Chiński (tradycyjny, Hongkong)](../hk/README.md) | [Chiński (tradycyjny, Makau)](../mo/README.md) | [Chiński (tradycyjny, Tajwan)](../tw/README.md) | [Chorwacki](../hr/README.md) | [Czeski](../cs/README.md) | [Duński](../da/README.md) | [Niderlandzki](../nl/README.md) | [Estoński](../et/README.md) | [Fiński](../fi/README.md) | [Francuski](../fr/README.md) | [Niemiecki](../de/README.md) | [Grecki](../el/README.md) | [Hebrajski](../he/README.md) | [Hindi](../hi/README.md) | [Węgierski](../hu/README.md) | [Indonezyjski](../id/README.md) | [Włoski](../it/README.md) | [Japoński](../ja/README.md) | [Kannada](../kn/README.md) | [Koreański](../ko/README.md) | [Litewski](../lt/README.md) | [Malajski](../ms/README.md) | [Malajalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepalski](../ne/README.md) | [Nigeryjski pidżin](../pcm/README.md) | [Norweski](../no/README.md) | [Perski (farsi)](../fa/README.md) | [Polski](./README.md) | [Portugalski (Brazylia)](../br/README.md) | [Portugalski (Portugalia)](../pt/README.md) | [Pendżabski (Gurmukhi)](../pa/README.md) | [Rumuński](../ro/README.md) | [Rosyjski](../ru/README.md) | [Serbski (cyrylica)](../sr/README.md) | [Słowacki](../sk/README.md) | [Słoweński](../sl/README.md) | [Hiszpański](../es/README.md) | [Suahili](../sw/README.md) | [Szwedzki](../sv/README.md) | [Tagalog (filipiński)](../tl/README.md) | [Tamilski](../ta/README.md) | [Telugu](../te/README.md) | [Tajski](../th/README.md) | [Turecki](../tr/README.md) | [Ukraiński](../uk/README.md) | [Urdu](../ur/README.md) | [Wietnamski](../vi/README.md)
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

**Jeśli chcesz dodać dodatkowe tłumaczenia, wspierane języki są wymienione [tutaj](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md)**
## Wprowadzenie

Witamy w **EdgeAI for Beginners** – twojej kompleksowej podróży po transformującym świecie Edge Artificial Intelligence. Ten kurs łączy potężne możliwości AI z praktycznym wdrożeniem na urządzeniach brzegowych, umożliwiając wykorzystanie potencjału AI bezpośrednio tam, gdzie generowane są dane i podejmowane są decyzje.

### Czego się nauczysz

Ten kurs przeprowadzi cię od podstawowych koncepcji do gotowych do produkcji wdrożeń, obejmując:
- **Małe modele językowe (SLM)** zoptymalizowane pod kątem wdrożeń na urządzeniach brzegowych
- **Optymalizację z uwzględnieniem sprzętu** dla różnych platform
- **Wnioskowanie w czasie rzeczywistym** z funkcjami zachowania prywatności
- **Strategie wdrożenia produkcyjnego** dla zastosowań przedsiębiorstw

### Dlaczego EdgeAI ma znaczenie

Edge AI reprezentuje zmianę paradygmatu, która odpowiada na kluczowe współczesne wyzwania:
- **Prywatność i bezpieczeństwo**: Przetwarzaj dane wrażliwe lokalnie bez narażania ich w chmurze
- **Wydajność w czasie rzeczywistym**: Eliminuj opóźnienia sieciowe w aplikacjach krytycznych czasowo
- **Efektywność kosztowa**: Zmniejsz wykorzystanie przepustowości i koszty obliczeń w chmurze
- **Odporna operacyjność**: Zachowaj funkcjonalność podczas przerw w połączeniu sieciowym
- **Zgodność regulacyjna**: Spełniaj wymagania dotyczące suwerenności danych

### Edge AI

Edge AI odnosi się do uruchamiania algorytmów AI i modeli językowych lokalnie na sprzęcie, blisko miejsca, gdzie generowane są dane, bez polegania na zasobach chmury do wnioskowania. Redukuje opóźnienia, zwiększa prywatność i umożliwia podejmowanie decyzji w czasie rzeczywistym.

### Zasady podstawowe:
- **Wnioskowanie na urządzeniu**: Modele AI działają na urządzeniach brzegowych (telefony, routery, mikrokontrolery, komputery przemysłowe)
- **Możliwość pracy offline**: Funkcjonuje bez stałego połączenia z internetem
- **Niskie opóźnienia**: Natychmiastowe odpowiedzi odpowiednie dla systemów czasu rzeczywistego
- **Suwerenność danych**: Przechowywanie danych wrażliwych lokalnie, poprawiające bezpieczeństwo i zgodność

### Małe modele językowe (SLM)

SLM-y, takie jak Phi-4, Mistral-7B i Gemma, to zoptymalizowane wersje większych LLM-ów — trenowane lub destylowane w celu:
- **Zmniejszonego zużycia pamięci**: Efektywne wykorzystanie ograniczonej pamięci urządzeń brzegowych
- **Niższych wymagań obliczeniowych**: Optymalizacja pod kątem wydajności na CPU i GPU brzegowych
- **Szybszego czasu startu**: Szybka inicjalizacja dla responsywnych aplikacji

Umożliwiają potężne możliwości NLP, jednocześnie spełniając ograniczenia takich środowisk jak:
- **Systemy wbudowane**: Urządzenia IoT i kontrolery przemysłowe
- **Urządzenia mobilne**: Smartfony i tablety z funkcjami offline
- **Urządzenia IoT**: Czujniki i inteligentne urządzenia o ograniczonych zasobach
- **Serwery brzegowe**: Lokalne jednostki przetwarzające z ograniczonymi zasobami GPU
- **Komputery osobiste**: Scenariusze wdrożeń na desktopach i laptopach

## Moduły kursu i nawigacja

| Moduł | Temat | Zakres | Główna zawartość | Poziom | Czas trwania |
|--------|-------|------------|-------------|--------|----------|
| [📖 00 ](./introduction.md) | [Wprowadzenie do EdgeAI](./introduction.md) | Podstawy i kontekst | Przegląd EdgeAI • Zastosowania w przemyśle • Wprowadzenie do SLM • Cele nauki | Początkujący | 1-2 godz. |
| [📚 01](../../Module01) | [Podstawy EdgeAI](./Module01/README.md) | Porównanie chmury z Edge AI | Podstawy EdgeAI • Studia przypadków • Przewodnik wdrożeniowy • Wdrożenie brzegowe | Początkujący | 3-4 godz. |
| [🧠 02](../../Module02) | [Podstawy modeli SLM](./Module02/README.md) | Rodziny modeli i architektura | Phi Family • Qwen Family • Gemma Family • BitNET • μModel • Phi-Silica | Początkujący | 4-5 godz. |
| [🚀 03](../../Module03) | [Praktyka wdrażania SLM](./Module03/README.md) | Wdrożenie lokalne i w chmurze | Zaawansowane materiały • Środowisko lokalne • Wdrażanie w chmurze | Średniozaawansowany | 4-5 godz. |
| [⚙️ 04](../../Module04) | [Zestaw narzędzi do optymalizacji modeli](./Module04/README.md) | Optymalizacja wieloplatformowa | Wprowadzenie • Llama.cpp • Microsoft Olive • OpenVINO • Apple MLX • Synteza przepływu pracy | Średniozaawansowany | 5-6 godz. |
| [🔧 05](../../Module05) | [SLMOps w produkcji](./Module05/README.md) | Operacje produkcyjne | Wprowadzenie do SLMOps • Destylacja modeli • Dostosowywanie (fine-tuning) • Wdrożenie produkcyjne | Zaawansowany | 5-6 godz. |
| [🤖 06](../../Module06) | [Agenci AI i wywoływanie funkcji](./Module06/README.md) | Frameworki agentów i MCP | Wprowadzenie do agentów • Wywoływanie funkcji • Protokół kontekstu modelu | Zaawansowany | 4-5 godz. |
| [💻 07](../../Module07) | [Implementacja platformy](./Module07/README.md) | Przykłady międzyplatformowe | Zestaw narzędzi AI • Foundry Local • Tworzenie na Windows | Zaawansowany | 3-4 godz. |
| [🏭 08](../../Module08) | [Zestaw narzędzi Foundry Local](./Module08/README.md) | Przykłady gotowe do produkcji | Przykładowe aplikacje (szczegóły poniżej) | Ekspercki | 8-10 godz. |

### 🏭 **Moduł 08: Aplikacje przykładowe**

- [01: Szybki start: REST Chat](./Module08/samples/01/README.md)
- [02: Integracja z OpenAI SDK](./Module08/samples/02/README.md)
- [03: Odkrywanie modeli i benchmarking](./Module08/samples/03/README.md)
- [04: Aplikacja Chainlit RAG](./Module08/samples/04/README.md)
- [05: Orkiestracja wielu agentów](./Module08/samples/05/README.md)
- [06: Router: modele jako narzędzia](./Module08/samples/06/README.md)
- [07: Bezpośredni klient API](./Module08/samples/07/README.md)
- [08: Aplikacja czatu Windows 11](./Module08/samples/08/README.md)
- [09: Zaawansowany system wieloagentowy](./Module08/samples/09/README.md)
- [10: Framework narzędzi Foundry](./Module08/samples/10/README.md)

### 🎓 **Warsztat: Praktyczna ścieżka nauki**

Kompleksowe materiały warsztatowe z praktycznymi wdrożeniami gotowymi do produkcji:

- **[Przewodnik warsztatowy](./Workshop/Readme.md)** - Pełne cele nauki, wyniki i nawigacja po zasobach
- **Przykłady w Pythonie** (6 sesji) - Zaktualizowane z najlepszymi praktykami, obsługą błędów i szczegółową dokumentacją
- **Notatniki Jupyter** (8 interaktywnych) - Samouczki krok po kroku z benchmarkami i monitorowaniem wydajności
- **Przewodniki sesji** - Szczegółowe przewodniki w formacie markdown dla każdej sesji warsztatowej
- **Narzędzia walidacyjne** - Skrypty do weryfikacji jakości kodu i uruchamiania testów dymnych

**Co zbudujesz:**
- Lokalne aplikacje czatu AI z obsługą streamingu
- Pipeline'y RAG z oceną jakości (RAGAS)
- Narzędzia do benchmarkingu i porównywania wielu modeli
- Systemy orkiestracji wielu agentów
- Inteligentne kierowanie modeli z wyborem opartym na zadaniach

### 📊 **Podsumowanie ścieżki nauki**
- **Całkowity czas trwania**: 36-45 godzin
- **Ścieżka dla początkujących**: Moduły 01-02 (7-9 godzin)  
- **Ścieżka średniozaawansowana**: Moduły 03-04 (9-11 godzin)
- **Ścieżka zaawansowana**: Moduły 05-07 (12-15 godzin)
- **Ścieżka ekspercka**: Moduł 08 (8-10 godzin)

## Co zbudujesz

### 🎯 Główne kompetencje
- **Architektura Edge AI**: Projektuj systemy AI lokalne z integracją chmury
- **Optymalizacja modeli**: Kwantyzacja i kompresja modeli do wdrożeń na edge (przyspieszenie o 85%, redukcja rozmiaru o 75%)
- **Wieloplatformowe wdrożenia**: Windows, urządzenia mobilne, urządzenia wbudowane oraz hybrydowe systemy chmura-edge
- **Operacje produkcyjne**: Monitorowanie, skalowanie i utrzymanie Edge AI w produkcji

### 🏗️ Projekty praktyczne
- **Aplikacje czatu Foundry Local**: Natywna aplikacja Windows 11 z możliwością przełączania modeli
- **Systemy wieloagentowe**: Koordynator z agentami specjalistami dla złożonych przepływów pracy  
- **Aplikacje RAG**: Lokalna obróbka dokumentów z wyszukiwaniem wektorowym
- **Routery modeli**: Inteligentny wybór modeli w oparciu o analizę zadania
- **Frameworki API**: Klienci gotowi do produkcji z obsługą streamingu i monitorowaniem stanu
- **Narzędzia wieloplatformowe**: Wzorce integracji LangChain/Semantic Kernel

### 🏢 Zastosowania przemysłowe
**Produkcja** • **Opieka zdrowotna** • **Pojazdy autonomiczne** • **Inteligentne miasta** • **Aplikacje mobilne**

## Szybki start

**Zalecana ścieżka nauki** (łącznie 20–30 godzin):

0. **📖 Wprowadzenie** ([Introduction.md](./introduction.md)): Podstawy EdgeAI + kontekst branżowy + ramy nauki
1. **📚 Fundamenty** (Moduły 01-02): Koncepcje EdgeAI + rodziny modeli SLM
2. **⚙️ Optymalizacja** (Moduły 03-04): Wdrożenie + frameworki kwantyzacji  
3. **🚀 Produkcja** (Moduły 05-06): SLMOps + agenci AI + wywoływanie funkcji
4. **💻 Implementacja** (Moduły 07-08): Przykłady platform + zestaw narzędzi Foundry Local

Każdy moduł zawiera teorię, ćwiczenia praktyczne oraz przykłady kodu gotowe do użycia w produkcji.

## Wpływ na karierę

**Role techniczne**: Architekt rozwiązań EdgeAI • Inżynier ML (Edge) • Programista AI dla IoT • Programista AI mobilny

**Sektory przemysłu**: Przemysł 4.0 • Technologie opieki zdrowotnej • Systemy autonomiczne • FinTech • Elektronika użytkowa

**Projekty do portfolio**: Systemy wieloagentowe • Aplikacje RAG produkcyjne • Wieloplatformowe wdrożenia • Optymalizacja wydajności

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

✅ **Nauka stopniowa**: Teoria → Praktyka → Wdrożenie produkcyjne  
✅ **Rzeczywiste studia przypadków**: Microsoft, Japan Airlines, wdrożenia korporacyjne  
✅ **Przykłady praktyczne**: 50+ przykładów, 10 kompleksowych demonstracji Foundry Local  
✅ **Skupienie na wydajności**: przyspieszenie o 85%, redukcja rozmiaru o 75%  
✅ **Wieloplatformowość**: Windows, urządzenia mobilne, urządzenia wbudowane, hybrydy chmura-edge  
✅ **Gotowe do produkcji**: Monitorowanie, skalowanie, bezpieczeństwo, ramy zgodności

📖 **[Dostępny przewodnik studyjny](STUDY_GUIDE.md)**: Strukturyzowana 20-godzinna ścieżka nauki z wskazówkami dotyczącymi podziału czasu i narzędziami do samooceny.

---

**EdgeAI reprezentuje przyszłość wdrażania AI**: nastawione na lokalność, chroniące prywatność i wydajne. Opanuj te umiejętności, aby budować kolejną generację inteligentnych aplikacji.

## Inne kursy

Nasz zespół tworzy także inne kursy! Sprawdź:

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
 
### Seria Generative AI
[![Generative AI dla początkujących](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Generative AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![Generative AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![Generative AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### Podstawy
[![ML dla początkujących](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![Data Science dla początkujących](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![AI dla początkujących](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![Cyberbezpieczeństwo dla początkujących](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![Web Dev dla początkujących](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![IoT dla początkujących](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![XR Development dla początkujących](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Seria Copilot
[![Copilot dla programowania z AI](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot dla C#/.NET](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot Adventure](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## Uzyskanie pomocy

If you get stuck or have any questions about building AI apps, join:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

If you have product feedback or errors while building visit:

[![Forum deweloperów Microsoft Foundry](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Zastrzeżenie:
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI Co-op Translator (https://github.com/Azure/co-op-translator). Chociaż dokładamy starań, aby zapewnić poprawność, prosimy pamiętać, że tłumaczenia automatyczne mogą zawierać błędy lub nieścisłości. Oryginalny dokument w języku źródłowym należy uznać za źródło wiążące. W przypadku informacji o krytycznym znaczeniu zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
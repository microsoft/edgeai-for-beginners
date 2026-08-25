# Zmiany w wersjach

Wszystkie istotne zmiany w EdgeAI dla początkujących są tutaj dokumentowane. Ten projekt używa wpisów opartych na dacie i stylu Keep a Changelog (Dodano, Zmieniono, Naprawiono, Usunięto, Dokumentacja, Przeniesiono).

## 2025-10-30

### Dodano - Kompleksowa rozbudowa Agentów AI w Module06
- **Integracja Microsoft Agent Framework** (`Module06/01.IntroduceAgent.md`):
  - Kompletny rozdział o Microsoft Agent Framework do produkcyjnego rozwoju agentów
  - Szczegółowe wzorce integracji z Foundry Local dla wdrożeń edge
  - Przykłady orkiestracji wielu agentów z wyspecjalizowanymi modelami SLM
  - Wzorce wdrożenia korporacyjnego z zarządzaniem zasobami i monitorowaniem
  - Funkcje bezpieczeństwa i zgodności dla systemów agentów edge
  - Przykłady wdrożeń w rzeczywistych zastosowaniach (handel detaliczny, opieka zdrowotna, obsługa klienta)

- **Strategie wdrożenia agentów SLM do produkcji**:
  - **Foundry Local**: Kompletny runtime edge AI klasy korporacyjnej z dokumentacją instalacji, konfiguracji i wzorców produkcyjnych
  - **Ollama**: Rozszerzone wdrożenie wpisujące się w społeczność z kompleksowym monitorowaniem i zarządzaniem modelami
  - **VLLM**: Wysokowydajny silnik inferencji z zaawansowanymi technikami optymalizacji i funkcjami korporacyjnymi
  - Listy kontrolne wdrożenia produkcyjnego i tabele porównawcze dla wszystkich trzech platform

- **Ulepszenia frameworków SLM zoptymalizowanych pod edge**:
  - **ONNX Runtime**: Nowa obszerna sekcja dla wieloplatformowego wdrażania agentów SLM
  - Uniwersalne wzorce wdrożeń na Windows, Linux, macOS, iOS i Android
  - Opcje akceleracji sprzętowej (CPU, GPU, NPU) z automatycznym wykrywaniem
  - Funkcje gotowe do produkcji i optymalizacje specyficzne dla agentów
  - Kompletne przykłady implementacji z integracją Microsoft Agent Framework

- **Referencje i dalsza lektura**:
  - Obszerny zbiór zasobów z ponad 100 autorytatywnych źródeł
  - Kluczowe publikacje naukowe o agentach AI i Small Language Models
  - Oficjalna dokumentacja wszystkich głównych frameworków i narzędzi
  - Raporty branżowe, analizy rynkowe i benchmarki techniczne
  - Zasoby edukacyjne, konferencje i fora społeczności
  - Standardy, specyfikacje i ramy zgodności

### Zmieniono - Modernizacja zawartości Module06
- **Ulepszone cele nauki**: Dodano opanowanie Microsoft Agent Framework i możliwości wdrożeń edge
- **Skupienie na produkcji**: Przesunięcie z koncepcyjnych do gotowych do wdrożenia wskazówek z przykładami produkcyjnymi
- **Przykłady kodu**: Zaktualizowano wszystkie przykłady do używania nowoczesnych wzorców SDK i najlepszych praktyk
- **Wzorce architektury**: Dodano hierarchiczne architektury agentów i koordynację edge-do-chmury
- **Optymalizacja wydajności**: Wzmocniona zarządzaniem zasobami i rekomendacjami auto-skalowania

### Dokumentacja - Ulepszenia struktury Module06
- **Kompleksowe omówienie Frameworku Agentów**: Od podstawowych koncepcji po wdrożenia korporacyjne
- **Strategie wdrożenia produkcyjnego**: Kompleksowe przewodniki dla Foundry Local, Ollama i VLLM
- **Optymalizacja wieloplatformowa**: Dodano ONNX Runtime dla uniwersalnego wdrożenia
- **Biblioteka zasobów**: Rozległe odniesienia do dalszej nauki i implementacji

### Dodano - Aktualizacja dokumentacji Model Context Protocol (MCP) w Module06
- **Modernizacja wprowadzenia MCP** (`Module06/03.IntroduceMCP.md`):
  - Zaktualizowano do najnowszych specyfikacji MCP z modelcontextprotocol.io (wersja 2025-06-18)
  - Dodano oficjalną analogię USB-C dla znormalizowanych połączeń aplikacji AI
  - Zaktualizowano sekcję architektury z oficjalnym dwuwarstwowym projektem (Warstwa danych + Warstwa transportu)
  - Ulepszona dokumentacja rdzeniowych prymitywów z prymitywami serwera (Narzędzia, Zasoby, Podpowiedzi) i klienta (Próbkowanie, Elicytacja, Logowanie)

- **Obszernie odniesienia i zasoby MCP**:
  - Dodano link **MCP dla początkujących** (https://aka.ms/mcp-for-beginners) 
  - Oficjalna dokumentacja i specyfikacje MCP (modelcontextprotocol.io)
  - Zasoby developerskie w tym MCP Inspector i implementacje referencyjne
  - Standardy techniczne (JSON-RPC 2.0, JSON Schema, OpenAPI, Server-Sent Events)


### Dodano - Integracja Qualcomm QNN w Module04
- **Nowa sekcja 7: Qualcomm QNN Optimization Suite** (`Module04/05.QualcommQNN.md`):
  - Kompleksowy przewodnik 400+ linii obejmujący zunifikowany framework inferencji AI Qualcomm
  - Szczegółowe omówienie heterogenicznych obliczeń (Hexagon NPU, Adreno GPU, Kryo CPU)
  - Optymalizacja sprzętowa dla platform Snapdragon z inteligentnym rozdzielaniem obciążenia
  - Zaawansowane techniki kwantyzacji (INT8, INT16, mieszana precyzja) dla wdrożeń mobilnych
  - Optymalizacja energetyczna inferencji dla urządzeń zasilanych bateryjnie i aplikacji czasu rzeczywistego
  - Kompletny przewodnik instalacji z konfiguracją SDK QNN i środowiska
  - Praktyczne przykłady: konwersja PyTorch do QNN, optymalizacja multi-backend, generacja binariów kontekstowych
  - Zaawansowane wzorce użycia: własna konfiguracja backendu, dynamiczna kwantyzacja, profilowanie wydajności
  - Kompleksowa sekcja rozwiązywania problemów i zasoby społecznościowe

- **Ulepszona struktura Module04**:
  - Zaktualizowano README.md do 7 progresywnych sekcji (wcześniej 6)
  - Dodano Qualcomm QNN do tabeli benchmarków wydajności (5-15x przyspieszenie, 50-80% redukcji pamięci)
  - Kompleksowe efekty nauki dla wdrożeń mobilnych AI i optymalizacji zużycia energii

### Zmieniono - Aktualizacje dokumentacji Module04
- **Ulepszenie dokumentacji Microsoft Olive** (`Module04/03.MicrosoftOlive.md`):
  - Dodano obszerną sekcję "Olive Recipes Repository" obejmującą 100+ gotowych przepisów optymalizacyjnych
  - Szczegółowe omówienie wspieranych rodzin modeli (Phi, Llama, Qwen, Gemma, Mistral, DeepSeek)
  - Praktyczne przykłady dostosowywania przepisów i wkładów społecznościowych
  - Wzbogacone o benchmarki wydajności i wskazówki integracyjne

- **Zmiana kolejności sekcji w Module04**:
  - Apple MLX przeniesione do sekcji 5 (wcześniej sekcja 6)
  - Workflow Synthesis przeniesione do sekcji 6 (wcześniej sekcja 7)  
  - Qualcomm QNN ustawione jako sekcja 7 (specjalizacja na mobilne/edge)
  - Zaktualizowano wszystkie odniesienia do plików i linki nawigacyjne stosownie do zmian

### Naprawiono - Walidacja przykładu warsztatowego
- **Walidacja i naprawa chat_bootstrap.py**:
  - Naprawiono uszkodzony import (`util.util.workshop_utils` → `util.workshop_utils`)
  - Utworzono brakujący `__init__.py` w pakiecie util dla poprawnego rozwiązywania modułów Pythona
  - Zainstalowano wymagane zależności (openai, foundry-local-sdk) w środowisku conda
  - Z powodzeniem zweryfikowano wykonanie próbki z domyślnymi i niestandardowymi promptami
  - Potwierdzono integrację z usługą Foundry Local i ładowanie modelu (phi-4-mini z optymalizacją CUDA)

### Dokumentacja - Kompleksowe aktualizacje przewodnika
- **Kompletna restrukturyzacja README.md Module04**:
  - Dodano Qualcomm QNN jako główny framework optymalizacyjny obok OpenVINO, Olive, MLX
  - Zaktualizowano rezultaty nauki rozdziału obejmujące wdrożenie mobilnego AI i optymalizację energetyczną
  - Wzbogacono tabelę porównań wydajności o metryki QNN i zastosowania mobilne/edge
  - Zachowano logiczny ciąg od rozwiązań korporacyjnych do optymalizacji platform-specyficznych

- **Odwołania krzyżowe i nawigacja**:
  - Zaktualizowano wszystkie linki wewnętrzne i odniesienia do plików z nowym numerowaniem sekcji
  - Rozszerzono opis syntezy workflow o środowiska mobilne, desktop i chmurowe
  - Dodano kompleksowe linki do zasobów ekosystemu deweloperskiego Qualcomm

## 2025-10-08

### Dodano - Kompleksowa aktualizacja warsztatu
- **Kompletne przepisanie README.md warsztatu**:
  - Dodano obszerny wstęp wyjaśniający wartość Edge AI (prywatność, wydajność, koszty)
  - Stworzono 6 kluczowych celów nauki z detalicznymi kompetencjami
  - Dodano tabelę rezultatów nauki z wynikami i matrycą kompetencji
  - Uwzględniono sekcję umiejętności gotowych do kariery dla znaczenia przemysłowego
  - Dodano przewodnik szybkiego startu z wymaganiami i 3-stopniową konfiguracją
  - Stworzono tabele zasobów z przykładami Python (8 plików z czasami uruchomienia)
  - Dodano tabelę zeszytów Jupyter (8 notebooków z oceną trudności)
  - Utworzono tabelę dokumentacji (7 kluczowych dokumentów z wskazówkami "Użyj kiedy")
  - Dodano rekomendacje ścieżek nauki dla różnych poziomów zaawansowania

- **Infrastruktura walidacji i testowania warsztatu**:
  - Utworzono `scripts/validate_samples.py` - Kompleksowe narzędzie do walidacji składni, importów i najlepszych praktyk
  - Utworzono `scripts/test_samples.py` - Uruchamiacz testów dymnych dla wszystkich przykładów Python
  - Dodano dokumentację walidacji do `scripts/README.md`

- **Kompleksowa dokumentacja**:
  - Utworzono `SAMPLES_UPDATE_SUMMARY.md` - Szczegółowy przewodnik 400+ linii obejmujący wszystkie ulepszenia
  - Utworzono `UPDATE_COMPLETE.md` - Podsumowanie wykonania aktualizacji
  - Utworzono `QUICK_REFERENCE.md` - Karta szybkiego odniesienia dla warsztatu

### Zmieniono - Modernizacja przykładowych kodów warsztatu w Pythonie
- **Wszystkie 8 przykładów Python odświeżono z najlepszymi praktykami**:
  - Ulepszone obsługi błędów z blokami try-except wokół wszystkich operacji I/O
  - Dodano wskazówki typów i obszerne docstringi
  - Wprowadzono spójny wzorzec logowania [INFO]/[ERROR]/[RESULT]
  - Zabezpieczono opcjonalne importy wskazówkami instalacji
  - Ulepszono reakcje dla użytkownika we wszystkich przykładach

- **session01/chat_bootstrap.py**:
  - Ulepszono inicjalizację klienta z obszernymi komunikatami o błędach
  - Poprawiono obsługę błędów streamingowych z walidacją fragmentów
  - Dodano lepsze zarządzanie wyjątkami dla niedostępności usługi

- **session02/rag_pipeline.py**:
  - Dodano zabezpieczenia importu sentence-transformers z wskazówkami instalacji
  - Ulepszono obsługę błędów podczas operacji osadzania i generacji
  - Poprawiono formatowanie wyników z ustrukturyzowanymi rezultatami

- **session02/rag_eval_ragas.py**:
  - Zabezpieczono opcjonalne importy (ragas, datasets) przyjaznymi komunikatami o błędach
  - Dodano obsługę błędów metryk oceny
  - Ulepszono formatowanie wyników ewaluacji

- **session03/benchmark_oss_models.py**:
  - Wprowadzenie łagodnego degradacji (kontynuacja pomimo błędów modeli)
  - Dodano szczegółowe raportowanie postępu i obsługę błędów per model
  - Ulepszono obliczenia statystyk z kompleksowym odzyskiwaniem po błędach

- **session04/model_compare.py**:
  - Dodano wskazówki typów (typy zwracanych wartości Tuple)
  - Ulepszono formatowanie wyników z ustrukturyzowanymi wynikami JSON
  - Wprowadzono obsługę błędów per model z możliwościami odzyskania

- **session05/agents_orchestrator.py**:
  - Ulepszono Agent.act() z obszernymi docstringami
  - Dodano obsługę błędów potoków z logowaniem etap po etapie
  - Ulepszono zarządzanie pamięcią i śledzenie stanu

- **session06/models_router.py**:
  - Ulepszona dokumentacja funkcji dla wszystkich komponentów routingu
  - Dodano obszerny logging w funkcji route()
  - Poprawiono wyniki testów z ustrukturyzowanymi rezultatami

- **session06/models_pipeline.py**:
  - Dodano obsługę błędów w pomocniczej funkcji chat()
  - Ulepszono pipeline() z logowaniem etapów i raportowaniem postępu
  - Ulepszono main() z kompleksowym odzyskiwaniem po błędach

### Dokumentacja - Ulepszenia dokumentacji warsztatu
- Zaktualizowano główne README.md z sekcją warsztatu podkreślającą ścieżkę nauki praktycznej
- Ulepszono STUDY_GUIDE.md o obszerną sekcję warsztatu zawierającą:
  - Cele nauki i obszary skupienia się
  - Pytania do samooceny
  - Ćwiczenia praktyczne z szacowanym czasem
  - Alokacja czasu na naukę intensywną i w niepełnym wymiarze
  - Dodano warsztat do szablonu śledzenia postępów
- Zaktualizowano przewodnik alokacji czasu z 20 godzin do 30 godzin (wliczając warsztat)
- Dodano opisy próbek warsztatu i rezultaty nauki do README

### Naprawiono
- Rozwiązano niespójne wzorce obsługi błędów w próbkach warsztatu
- Naprawiono błędy importów opcjonalnych zależności poprzez odpowiednie zabezpieczenia
- Poprawiono brakujące wskazówki typów w kluczowych funkcjach
- Zajęto się niewystarczającym feedbackiem dla użytkownika w scenariuszach błędów
- Naprawiono kwestie walidacji dzięki kompleksowej infrastrukturze testowej

---

## 2025-09-23

### Zmieniono - Główna modernizacja Module 08
- **Kompleksowe dostosowanie do wzorców repozytorium Microsoft Foundry-Local**
  - Zaktualizowano wszystkie przykłady kodu do używania nowoczesnego `FoundryLocalManager` i integracji OpenAI SDK
  - Zastąpiono przestarzałe ręczne wywołania `requests` odpowiednim użyciem SDK
  - Wzorce implementacji dostosowane do oficjalnej dokumentacji i przykładów Microsoft

- **Modernizacja 05.AIPoweredAgents.md**:
  - Zaktualizowano orkiestrację wielu agentów do używania nowoczesnych wzorców SDK
  - Ulepszono implementację koordynatora z zaawansowanymi funkcjami (pętle sprzężenia zwrotnego, monitoring wydajności)
  - Dodano kompleksową obsługę błędów i sprawdzanie stanu usługi
  - Zintegrowano odpowiednie odniesienia do lokalnych przykładów (`samples/05/multi_agent_orchestration.ipynb`)
  - Zaktualizowano przykłady wywołań funkcji do używania parametru `tools` zamiast przestarzałego `functions`
  - Dodano wzorce produkcyjnego wdrożenia z monitorowaniem i śledzeniem statystyk

- **Kompletne przepisanie 06.ModelsAsTools.md**:
  - Zastąpiono podstawowy rejestr narzędzi inteligentną implementacją routera modeli
  - Dodano wybór modelu na podstawie słów kluczowych dla różnych typów zadań (ogólne, rozumowanie, kod, kreatywne)
  - Zintegrowano konfigurację środowiskową z elastycznym przypisywaniem modeli
  - Wzbogacono o kompleksowy monitoring stanu usługi i obsługę błędów
  - Dodano wzorce produkcyjnego wdrożenia z monitorowaniem zapytań i wydajności
  - Dostosowane do lokalnej implementacji w `samples/06/router.py` oraz `samples/06/model_router.ipynb`

- **Ulepszenia struktury dokumentacji**:
  - Dodano sekcje przeglądowe podkreślające modernizację i dopasowanie SDK
  - Wzbogacono o emoji i lepsze formatowanie dla poprawy czytelności
  - Dodano odpowiednie odniesienia do lokalnych plików przykładów w całej dokumentacji
  - Uwzględniono wskazówki dotyczące implementacji produkcyjnej i najlepszych praktyk

### Dodano
- Kompleksowe sekcje przeglądowe w plikach Module 08 podkreślające nowoczesną integrację SDK
- Najważniejsze aspekty architektury pokazujące zaawansowane funkcje (systemy multi-agentów, inteligentny routing)
- Bezpośrednie odniesienia do lokalnych implementacji przykładów dla nauki praktycznej
- Wskazówki wdrożenia produkcyjnego z wzorcami monitoringu i obsługi błędów
- Interaktywne przykłady w notebookach Jupyter z zaawansowanymi funkcjami i benchmarkami

### Naprawiono
- Rozbieżności między dokumentacją a faktycznymi implementacjami przykładów
- Przestarzałe wzorce użycia SDK w Module 08
- Brakujące odniesienia do obszernych lokalnych bibliotek przykładów
- Niespójne podejścia implementacyjne w różnych sekcjach

---

## 2025-09-18

### Dodano
- Module 08: Microsoft Foundry Local – Kompletny zestaw narzędzi dla dewelopera
  - Sześć sesji: setup, integracja Azure AI Foundry, modele open-source, nowoczesne demonstracje, agenci i modele jako narzędzia
  - Wykonalne przykłady pod `Module08/samples/01`–`06` z instrukcjami dla Windows cmd
    - `01` szybki czat REST (`chat_quickstart.py`)

    - `02` Szybki start SDK z obsługą OpenAI/Foundry Local i Azure OpenAI (`sdk_quickstart.py`)
    - `03` CLI list-and-bench (`list_and_bench.cmd`)
    - `04` Demo Chainlit (`app.py`)
    - `05` Orkiestracja wieloagentowa (`python -m samples.05.agents.coordinator`)
    - `06` Router Models-as-Tools (`router.py`)
- Obsługa Azure OpenAI w przykładzie SDK Sesji 2 z konfiguracją przez zmienne środowiskowe
- `.vscode/settings.json` wskazujący na `Module08/.venv` i poprawiający rozpoznawanie Pythona
- `.env` z podpowiedzią `PYTHONPATH` dla lepszej świadomości VS Code/Pylance

### Zmiany
- Domyślny model zaktualizowany na `phi-4-mini` w całej dokumentacji i przykładach Modułu 08; usunięto pozostałe wzmianki o `phi-3.5` w Module 08
- Ulepszenia routera (`Module08/samples/06/router.py`):
  - Wykrywanie punktów końcowych przez `foundry service status` z analizą regex
  - Sprawdzenie stanu `/v1/models` przy starcie
  - Rejestr modeli konfigurowany przez środowisko (`GENERAL_MODEL`, `REASONING_MODEL`, `CODE_MODEL`, `TOOL_REGISTRY` JSON)
- Zaktualizowano wymagania: `Module08/requirements.txt` teraz zawiera `openai` (obok `requests`, `chainlit`)
- Wyjaśniono wskazówki do przykładu Chainlit i dodano instrukcje rozwiązywania problemów; rozwiązywanie importów przez ustawienia workspace

### Naprawiono
- Rozwiązano problemy z importami:
  - Router nie zależy już od nieistniejącego modułu `utils`; funkcje są wprost w kodzie
  - Koordynator używa importu względnego (`from .specialists import ...`) i jest uruchamiany przez ścieżkę modułu
  - Konfiguracja VS Code/Pylance rozpoznająca import `chainlit` i pakiety
- Poprawiono drobny błąd w `STUDY_GUIDE.md` i rozszerzono zakres Modułu 08

### Usunięto
- Usunięto nieużywany `Module08/infra/obs.py` i pusty katalog `infra/`; wzorce obserwowalności pozostawiono opcjonalnie w dokumentacji

### Przeniesiono
- Konsolidacja demo Modułu 08 pod `Module08/samples` z folderami ponumerowanymi według sesji
  - Przeniesiono aplikację Chainlit do `samples/04`
  - Przeniesiono agentów do `samples/05` i dodano pliki `__init__.py` dla poprawnej rozpoznawalności pakietów

### Dokumentacja
- Dokumentacja sesji Modułu 08 i wszystkie README przykładów rozszerzone o odniesienia do Microsoft Learn i zaufanych dostawców
- `Module08/README.md` zaktualizowany o przegląd przykładów, konfigurację routera i wskazówki walidacyjne
- Walidacja sekcji Windows Foundry Local w `Module07/README.md` na podstawie dokumentów Learn
- Zaktualizowano `STUDY_GUIDE.md`:
  - Dodano Moduł 08 do przeglądu, harmonogramów, śledzenia postępów
  - Dodano obszerną sekcję Referencje (Foundry Local, Azure AI, Olive, ONNX Runtime, OpenVINO, MLX, Llama.cpp, vLLM, Ollama, AI Toolkit, Windows ML)

---

## Historia (podsumowanie)
- Ustalono architekturę kursu i moduły (Moduły 01–07)
- Iteracyjne unowocześnianie treści, standaryzacja formatowania i dodanie studiów przypadków
- Rozszerzono zakres omówienia frameworków optymalizacyjnych (Llama.cpp, Olive, OpenVINO, Apple MLX)

## Niewydane / Zaległe (propozycje)
- Opcjonalne testy wstępne per przykład do walidacji dostępności Foundry Local
- Przegląd tłumaczeń, aby dopasować referencje modelowe (np. `phi-4-mini`) tam, gdzie to właściwe
- Dodanie minimalnej konfiguracji pyright, jeśli zespoły preferują rygor workspace-wide

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Choć dążymy do dokładności, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub niedokładności. Oryginalny dokument w jego języku źródłowym należy uznawać za autorytatywne źródło. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
# Dziennik zmian

Wszystkie istotne zmiany w EdgeAI dla Początkujących są tutaj udokumentowane. Projekt korzysta z wpisów opartych na datach oraz stylu Keep a Changelog (Dodano, Zmieniono, Naprawiono, Usunięto, Dokumentacja, Przeniesiono).

## 2025-10-30

### Dodano - Kompleksowe ulepszenie Agentów AI w Module06
- **Integracja z Microsoft Agent Framework** (`Module06/01.IntroduceAgent.md`):
  - Pełna sekcja dotycząca Microsoft Agent Framework dla rozwoju agentów gotowych do produkcji
  - Szczegółowe wzorce integracji z Foundry Local dla wdrożeń na urządzeniach brzegowych
  - Przykłady orkiestracji wieloagentowej z wyspecjalizowanymi modelami SLM
  - Wzorce wdrożeń korporacyjnych z zarządzaniem zasobami i monitorowaniem
  - Funkcje bezpieczeństwa i zgodności dla systemów agentów brzegowych
  - Przykłady wdrożeń w rzeczywistych scenariuszach (handel detaliczny, opieka zdrowotna, obsługa klienta)

- **Strategie wdrożeń agentów SLM w produkcji**:
  - **Foundry Local**: Kompleksowa dokumentacja klasy enterprise dla uruchamiania AI na urządzeniach brzegowych, z instalacją, konfiguracją i wzorcami produkcyjnymi
  - **Ollama**: Rozszerzone wdrożenie skoncentrowane na społeczności z kompleksowym monitorowaniem i zarządzaniem modelami
  - **VLLM**: Silnik inferencji o wysokiej wydajności z zaawansowanymi technikami optymalizacji i funkcjami korporacyjnymi
  - Listy kontrolne wdrożeń produkcyjnych i tabele porównawcze dla wszystkich trzech platform

- **Ulepszenie frameworków SLM zoptymalizowanych dla urządzeń brzegowych**:
  - **ONNX Runtime**: Nowa kompleksowa sekcja dotycząca wdrożeń agentów SLM na różnych platformach
  - Uniwersalne wzorce wdrożeń na Windows, Linux, macOS, iOS i Android
  - Opcje przyspieszenia sprzętowego (CPU, GPU, NPU) z automatycznym wykrywaniem
  - Funkcje gotowe do produkcji i optymalizacje specyficzne dla agentów
  - Pełne przykłady implementacji z integracją Microsoft Agent Framework

- **Referencje i dalsza lektura**:
  - Obszerna biblioteka zasobów z ponad 100 autorytatywnymi źródłami
  - Kluczowe prace badawcze dotyczące agentów AI i Małych Modeli Językowych
  - Oficjalna dokumentacja dla wszystkich głównych frameworków i narzędzi
  - Raporty branżowe, analizy rynku i benchmarki techniczne
  - Zasoby edukacyjne, konferencje i fora społecznościowe
  - Standardy, specyfikacje i ramy zgodności

### Zmieniono - Modernizacja treści Module06
- **Ulepszone cele nauczania**: Dodano opanowanie Microsoft Agent Framework i możliwości wdrożeń na urządzeniach brzegowych
- **Skupienie na produkcji**: Przejście od koncepcji do gotowych do wdrożenia wskazówek z przykładami produkcyjnymi
- **Przykłady kodu**: Zaktualizowano wszystkie przykłady, aby korzystały z nowoczesnych wzorców SDK i najlepszych praktyk
- **Wzorce architektury**: Dodano hierarchiczne architektury agentów i koordynację od urządzeń brzegowych do chmury
- **Optymalizacja wydajności**: Ulepszono o rekomendacje dotyczące zarządzania zasobami i automatycznego skalowania

### Dokumentacja - Ulepszenie struktury Module06
- **Kompleksowe omówienie frameworku agentów**: Od podstawowych koncepcji po wdrożenia korporacyjne
- **Strategie wdrożeń produkcyjnych**: Kompleksowe przewodniki dla Foundry Local, Ollama i VLLM
- **Optymalizacja międzyplatformowa**: Dodano ONNX Runtime dla uniwersalnych wdrożeń
- **Biblioteka zasobów**: Obszerne referencje do dalszego nauczania i implementacji

### Dodano - Aktualizacja dokumentacji Model Context Protocol (MCP) w Module06
- **Modernizacja wprowadzenia do MCP** (`Module06/03.IntroduceMCP.md`):
  - Zaktualizowano najnowsze specyfikacje MCP z modelcontextprotocol.io (wersja z 2025-06-18)
  - Dodano oficjalną analogię USB-C dla standaryzowanych połączeń aplikacji AI
  - Zaktualizowano sekcję architektury o oficjalny dwuwarstwowy projekt (Warstwa Danych + Warstwa Transportowa)
  - Ulepszono dokumentację podstawowych prymitywów o prymitywy serwera (Narzędzia, Zasoby, Podpowiedzi) i prymitywy klienta (Próbkowanie, Wywoływanie, Logowanie)

- **Kompleksowe referencje i zasoby MCP**:
  - Dodano link **MCP dla Początkujących** (https://aka.ms/mcp-for-beginners)
  - Oficjalna dokumentacja i specyfikacje MCP (modelcontextprotocol.io)
  - Zasoby dla deweloperów, w tym MCP Inspector i implementacje referencyjne
  - Standardy techniczne (JSON-RPC 2.0, JSON Schema, OpenAPI, Server-Sent Events)

### Dodano - Integracja Qualcomm QNN w Module04
- **Nowa sekcja 7: Qualcomm QNN Optimization Suite** (`Module04/05.QualcommQNN.md`):
  - Kompleksowy przewodnik na 400+ linii dotyczący zintegrowanego frameworku inferencji AI Qualcomm
  - Szczegółowe omówienie heterogenicznego przetwarzania (Hexagon NPU, Adreno GPU, Kryo CPU)
  - Optymalizacja sprzętowa dla platform Snapdragon z inteligentnym rozdzielaniem obciążenia
  - Zaawansowane techniki kwantyzacji (INT8, INT16, mieszana precyzja) dla wdrożeń mobilnych
  - Optymalizacja inferencji energooszczędnej dla urządzeń zasilanych bateriami i aplikacji w czasie rzeczywistym
  - Kompletny przewodnik instalacji z konfiguracją SDK QNN i środowiska
  - Praktyczne przykłady: konwersja PyTorch do QNN, optymalizacja wielozadaniowa, generowanie binariów kontekstowych
  - Zaawansowane wzorce użycia: konfiguracja niestandardowego backendu, dynamiczna kwantyzacja, profilowanie wydajności
  - Kompleksowa sekcja rozwiązywania problemów i zasoby społecznościowe

- **Ulepszona struktura Module04**:
  - Zaktualizowano README.md, aby uwzględnić 7 progresywnych sekcji (wcześniej 6)
  - Dodano Qualcomm QNN do tabeli benchmarków wydajności (5-15x poprawa szybkości, 50-80% redukcji pamięci)
  - Kompleksowe cele nauczania dla wdrożeń mobilnych AI i optymalizacji energetycznej

### Zmieniono - Aktualizacje dokumentacji Module04
- **Ulepszenie dokumentacji Microsoft Olive** (`Module04/03.MicrosoftOlive.md`):
  - Dodano kompleksową sekcję "Repozytorium Przepisów Olive" obejmującą ponad 100 gotowych przepisów optymalizacyjnych
  - Szczegółowe omówienie obsługiwanych rodzin modeli (Phi, Llama, Qwen, Gemma, Mistral, DeepSeek)
  - Praktyczne przykłady użycia dla dostosowywania przepisów i wkładów społecznościowych
  - Ulepszone o benchmarki wydajności i wskazówki dotyczące integracji

- **Przestawienie sekcji w Module04**:
  - Apple MLX przeniesiono do Sekcji 5 (wcześniej Sekcja 6)
  - Syntezę przepływu pracy przeniesiono do Sekcji 6 (wcześniej Sekcja 7)
  - Qualcomm QNN umieszczono jako Sekcję 7 (specjalizacja na urządzenia mobilne/brzegowe)
  - Zaktualizowano wszystkie odniesienia do plików i linki nawigacyjne

### Naprawiono - Walidacja próbek warsztatowych
- **Walidacja i naprawa chat_bootstrap.py**:
  - Naprawiono uszkodzone polecenie importu (`util.util.workshop_utils` → `util.workshop_utils`)
  - Utworzono brakujący `__init__.py` w pakiecie util dla poprawnej rozdzielczości modułu Python
  - Zainstalowano wymagane zależności (openai, foundry-local-sdk) w środowisku conda
  - Pomyślnie zweryfikowano wykonanie próbki zarówno z domyślnymi, jak i niestandardowymi podpowiedziami
  - Potwierdzono integrację z usługą Foundry Local i ładowanie modelu (phi-4-mini z optymalizacją CUDA)

### Dokumentacja - Aktualizacje kompleksowych przewodników
- **Kompletna restrukturyzacja README.md w Module04**:
  - Dodano Qualcomm QNN jako główny framework optymalizacyjny obok OpenVINO, Olive, MLX
  - Zaktualizowano cele nauczania rozdziału, aby uwzględnić wdrożenia mobilne AI i optymalizację energetyczną
  - Ulepszono tabelę porównania wydajności o metryki QNN i przypadki użycia mobilne/brzegowe
  - Zachowano logiczną progresję od rozwiązań korporacyjnych do optymalizacji specyficznych dla platform

- **Odnośniki krzyżowe i nawigacja**:
  - Zaktualizowano wszystkie wewnętrzne linki i odniesienia do plików dla nowego numerowania sekcji
  - Ulepszono opis syntezy przepływu pracy, aby uwzględnić środowiska mobilne, desktopowe i chmurowe
  - Dodano kompleksowe linki do zasobów ekosystemu deweloperskiego Qualcomm

## 2025-10-08

### Dodano - Kompleksowa aktualizacja warsztatu
- **Kompletne przepisanie README.md warsztatu**:
  - Dodano kompleksowe wprowadzenie wyjaśniające wartość Edge AI (prywatność, wydajność, koszt)
  - Utworzono 6 głównych celów nauczania z szczegółowymi kompetencjami
  - Dodano tabelę wyników nauczania z rezultatami i matrycą kompetencji
  - Uwzględniono sekcję umiejętności gotowych na rynek pracy dla znaczenia w branży
  - Dodano przewodnik szybkiego startu z wymaganiami wstępnymi i 3-etapową konfiguracją
  - Utworzono tabele zasobów dla próbek Python (8 plików z czasami wykonania)
  - Dodano tabelę notatników Jupyter (8 notatników z ocenami trudności)
  - Utworzono tabelę dokumentacji (7 kluczowych dokumentów z wskazówkami "Kiedy używać")
  - Dodano rekomendacje ścieżki nauczania dla różnych poziomów umiejętności

- **Walidacja warsztatu i infrastruktura testowa**:
  - Utworzono `scripts/validate_samples.py` - Kompleksowe narzędzie walidacji dla składni, importów i najlepszych praktyk
  - Utworzono `scripts/test_samples.py` - Narzędzie testowe dla wszystkich próbek Python
  - Dodano dokumentację walidacji do `scripts/README.md`

- **Kompleksowa dokumentacja**:
  - Utworzono `SAMPLES_UPDATE_SUMMARY.md` - Szczegółowy przewodnik na 400+ linii obejmujący wszystkie ulepszenia
  - Utworzono `UPDATE_COMPLETE.md` - Podsumowanie wykonania aktualizacji
  - Utworzono `QUICK_REFERENCE.md` - Karta szybkiego odniesienia dla warsztatu

### Zmieniono - Modernizacja próbek Python w warsztacie
- **Wszystkie 8 próbek Python zaktualizowano zgodnie z najlepszymi praktykami**:
  - Ulepszono obsługę błędów za pomocą bloków try-except wokół wszystkich operacji I/O
  - Dodano wskazówki typów i kompleksowe docstringi
  - Wprowadzono spójny wzorzec logowania [INFO]/[ERROR]/[RESULT]
  - Zabezpieczono opcjonalne importy z wskazówkami instalacyjnymi
  - Poprawiono informacje zwrotne dla użytkownika we wszystkich próbkach

- **session01/chat_bootstrap.py**:
  - Ulepszono inicjalizację klienta z kompleksowymi komunikatami o błędach
  - Poprawiono obsługę błędów strumieniowych z walidacją fragmentów
  - Dodano lepszą obsługę wyjątków dla niedostępności usług

- **session02/rag_pipeline.py**:
  - Dodano zabezpieczenia importu dla sentence-transformers z wskazówkami instalacyjnymi
  - Ulepszono obsługę błędów dla operacji osadzania i generowania
  - Poprawiono formatowanie wyników z ustrukturyzowanymi rezultatami

- **session02/rag_eval_ragas.py**:
  - Zabezpieczono opcjonalne importy (ragas, datasets) z przyjaznymi komunikatami o błędach
  - Dodano obsługę błędów dla metryk oceny
  - Ulepszono formatowanie wyników oceny

- **session03/benchmark_oss_models.py**:
  - Wprowadzono łagodne degradacje (kontynuuje w przypadku awarii modelu)
  - Dodano szczegółowe raportowanie postępu i obsługę błędów dla każdego modelu
  - Ulepszono obliczenia statystyk z kompleksowym odzyskiwaniem błędów

- **session04/model_compare.py**:
  - Dodano wskazówki typów (zwracane typy Tuple)
  - Ulepszono formatowanie wyników z ustrukturyzowanymi rezultatami JSON
  - Wprowadzono obsługę błędów dla każdego modelu z odzyskiwaniem

- **session05/agents_orchestrator.py**:
  - Ulepszono Agent.act() z kompleksowymi docstringami
  - Dodano obsługę błędów w pipeline z logowaniem etapowym
  - Poprawiono zarządzanie pamięcią i śledzenie stanu

- **session06/models_router.py**:
  - Ulepszono dokumentację funkcji dla wszystkich komponentów routingu
  - Dodano szczegółowe logowanie w funkcji route()
  - Poprawiono wyniki testów z ustrukturyzowanymi rezultatami

- **session06/models_pipeline.py**:
  - Dodano obsługę błędów do funkcji pomocniczej chat()
  - Ulepszono pipeline() z logowaniem etapowym i raportowaniem postępu
  - Poprawiono main() z kompleksowym odzyskiwaniem błędów

### Dokumentacja - Ulepszenie dokumentacji warsztatu
- Zaktualizowano główny README.md z sekcją warsztatu podkreślającą ścieżkę nauki praktycznej
- Ulepszono STUDY_GUIDE.md z kompleksową sekcją warsztatu, w tym:
  - Cele nauczania i obszary koncentracji nauki
  - Pytania do samooceny
  - Ćwiczenia praktyczne z szacunkami czasowymi
  - Przydział czasu na intensywną i częściową naukę
  - Dodano warsztat do szablonu śledzenia postępów
- Zaktualizowano przewodnik przydziału czasu z 20 godzin do 30 godzin (w tym warsztat)
- Dodano opisy próbek warsztatowych i wyniki nauczania do README

### Naprawiono
- Rozwiązano niespójne wzorce obsługi błędów w próbkach warsztatowych
- Naprawiono błędy opcjonalnych importów z odpowiednimi zabezpieczeniami
- Poprawiono brakujące wskazówki typów w kluczowych funkcjach
- Rozwiązano niewystarczające informacje zwrotne dla użytkownika w scenariuszach błędów
- Naprawiono problemy z walidacją dzięki kompleksowej infrastrukturze testowej

---

## 2025-09-23

### Zmieniono - Główna modernizacja Module 08
- **Kompleksowe dostosowanie do wzorców repozytorium Microsoft Foundry-Local**
  - Zaktualizowano wszystkie przykłady kodu, aby korzystały z nowoczesnego `FoundryLocalManager` i integracji OpenAI SDK
  - Zastąpiono przestarzałe ręczne wywołania `requests` odpowiednim użyciem SDK
  - Dostosowano wzorce implementacji do oficjalnej dokumentacji i próbek Microsoft

- **Modernizacja 05.AIPoweredAgents.md**:
  - Zaktualizowano orkiestrację wieloagentową, aby korzystać z nowoczesnych wzorców SDK
  - Ulepszono implementację
- Przykłady do uruchomienia w `Module08/samples/01`–`06` z instrukcjami dla Windows cmd
  - `01` REST szybki czat (`chat_quickstart.py`)
  - `02` SDK szybki start z obsługą OpenAI/Foundry Local i Azure OpenAI (`sdk_quickstart.py`)
  - `03` CLI lista i test (`list_and_bench.cmd`)
  - `04` Demo Chainlit (`app.py`)
  - `05` Orkiestracja wieloagentowa (`python -m samples.05.agents.coordinator`)
  - `06` Router Models-as-Tools (`router.py`)
- Obsługa Azure OpenAI w próbce SDK Sesji 2 z konfiguracją zmiennych środowiskowych
- `.vscode/settings.json` wskazuje na `Module08/.venv` i poprawia rozdzielczość analizy Python
- `.env` z podpowiedzią `PYTHONPATH` dla świadomości VS Code/Pylance

### Zmiany
- Domyślny model zaktualizowany do `phi-4-mini` w dokumentacji i przykładach Module 08; usunięto pozostałe wzmianki o `phi-3.5` w Module 08
- Ulepszenia routera (`Module08/samples/06/router.py`):
  - Odkrywanie punktów końcowych za pomocą `foundry service status` z analizą regex
  - Sprawdzenie zdrowia `/v1/models` przy uruchomieniu
  - Rejestr modeli konfigurowalny przez środowisko (`GENERAL_MODEL`, `REASONING_MODEL`, `CODE_MODEL`, `TOOL_REGISTRY` JSON)
- Zaktualizowane wymagania: `Module08/requirements.txt` teraz zawiera `openai` (obok `requests`, `chainlit`)
- Wyjaśnione wskazówki dotyczące przykładu Chainlit i dodano rozwiązywanie problemów; rozdzielczość importów przez ustawienia przestrzeni roboczej

### Naprawione
- Rozwiązano problemy z importem:
  - Router nie zależy już od nieistniejącego modułu `utils`; funkcje są wbudowane
  - Koordynator używa importu względnego (`from .specialists import ...`) i jest wywoływany przez ścieżkę modułu
  - Konfiguracja VS Code/Pylance do rozwiązywania importów `chainlit` i pakietów
- Poprawiono drobną literówkę w `STUDY_GUIDE.md` i dodano pokrycie Module 08

### Usunięte
- Usunięto nieużywany `Module08/infra/obs.py` i pusty katalog `infra/`; wzorce obserwowalności zachowane jako opcjonalne w dokumentacji

### Przeniesione
- Skonsolidowano dema Module 08 w `Module08/samples` z folderami numerowanymi według sesji
  - Przeniesiono aplikację Chainlit do `samples/04`
  - Przeniesiono agentów do `samples/05` i dodano pliki `__init__.py` dla rozdzielczości pakietów

### Dokumentacja
- Dokumentacja sesji Module 08 i wszystkie README przykładów wzbogacone o odnośniki do Microsoft Learn i zaufanych dostawców
- Zaktualizowano `Module08/README.md` o Przegląd Przykładów, konfigurację routera i wskazówki dotyczące walidacji
- Zweryfikowano sekcję Windows Foundry Local w `Module07/README.md` w odniesieniu do dokumentacji Learn
- Zaktualizowano `STUDY_GUIDE.md`:
  - Dodano Module 08 do przeglądu, harmonogramów, śledzenia postępów
  - Dodano kompleksową sekcję Odnośników (Foundry Local, Azure AI, Olive, ONNX Runtime, OpenVINO, MLX, Llama.cpp, vLLM, Ollama, AI Toolkit, Windows ML)

---

## Historyczne (podsumowanie)
- Ustanowiono architekturę kursu i moduły (Module 01–07)
- Iteracyjna modernizacja treści, standaryzacja formatowania i dodanie studiów przypadków
- Rozszerzenie pokrycia frameworków optymalizacyjnych (Llama.cpp, Olive, OpenVINO, Apple MLX)

## Nieopublikowane / Backlog (propozycje)
- Opcjonalne testy dymne dla każdego przykładu w celu weryfikacji dostępności Foundry Local
- Przegląd tłumaczeń w celu dostosowania odniesień do modeli (np. `phi-4-mini`) tam, gdzie to właściwe
- Dodanie minimalnej konfiguracji pyright, jeśli zespoły preferują ścisłość w całej przestrzeni roboczej

---

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż staramy się zapewnić dokładność, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za autorytatywne źródło. W przypadku informacji krytycznych zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
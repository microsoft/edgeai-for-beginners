# AGENTS.md

> **Przewodnik dla programistów: Wkład w EdgeAI dla początkujących**
> 
> Ten dokument zawiera szczegółowe informacje dla programistów, agentów AI i współtwórców pracujących z tym repozytorium. Obejmuje konfigurację, przepływy pracy, testowanie i najlepsze praktyki.
> 
> **Ostatnia aktualizacja**: 30 października 2025 | **Wersja dokumentu**: 3.0

## Spis treści

- [Przegląd projektu](../..)
- [Struktura repozytorium](../..)
- [Wymagania wstępne](../..)
- [Polecenia konfiguracji](../..)
- [Przepływ pracy programistycznej](../..)
- [Instrukcje testowania](../..)
- [Wytyczne dotyczące stylu kodu](../..)
- [Wytyczne dotyczące pull requestów](../..)
- [System tłumaczeń](../..)
- [Integracja z Foundry Local](../..)
- [Budowanie i wdrażanie](../..)
- [Typowe problemy i rozwiązywanie problemów](../..)
- [Dodatkowe zasoby](../..)
- [Uwagi specyficzne dla projektu](../..)
- [Uzyskiwanie pomocy](../..)

## Przegląd projektu

EdgeAI dla początkujących to kompleksowe repozytorium edukacyjne uczące rozwoju Edge AI z wykorzystaniem Małych Modeli Językowych (SLM). Kurs obejmuje podstawy EdgeAI, wdrażanie modeli, techniki optymalizacji oraz implementacje gotowe do produkcji z użyciem Microsoft Foundry Local i różnych frameworków AI.

**Kluczowe technologie:**
- Python 3.8+ (główny język dla próbek AI/ML)
- .NET C# (próbki AI/ML)
- JavaScript/Node.js z Electron (dla aplikacji desktopowych)
- Microsoft Foundry Local SDK
- Microsoft Windows ML 
- VSCode AI Toolkit
- OpenAI SDK
- Frameworki AI: LangChain, Semantic Kernel, Chainlit
- Optymalizacja modeli: Llama.cpp, Microsoft Olive, OpenVINO, Apple MLX

**Typ repozytorium:** Repozytorium treści edukacyjnych z 8 modułami i 10 kompleksowymi aplikacjami przykładowymi

**Architektura:** Ścieżka nauki z wieloma modułami, z praktycznymi przykładami pokazującymi wzorce wdrażania Edge AI

## Struktura repozytorium

```
edgeai-for-beginners/
├── introduction.md          # Course introduction and overview
├── Module01-07/            # Core educational modules (Markdown)
├── Module08/               # Foundry Local toolkit with 10 samples
│   ├── samples/01-06/     # Foundation samples (Python)
│   ├── samples/07/        # API client (Python)
│   ├── samples/08/        # Windows 11 chat app (Electron)
│   └── samples/09-10/     # Advanced multi-agent systems (Python)
├── Workshop/               # Hands-on workshop materials
│   ├── samples/           # Workshop Python samples with utilities
│   │   ├── session01/     # Chat bootstrap samples
│   │   ├── session02-06/  # Progressive workshop sessions
│   │   └── util/          # Workshop utility modules
│   ├── notebooks/         # Jupyter notebook tutorials
│   └── scripts/           # Validation and testing tools
├── translations/          # Multi-language translations (50+ languages)
├── translated_images/     # Localized images
└── imgs/                  # Course images and assets
```

## Wymagania wstępne

### Wymagane narzędzia

- **Python 3.8+** - Do próbek AI/ML i notebooków
- **Node.js 16+** - Do aplikacji przykładowej Electron
- **Git** - Do kontroli wersji
- **Microsoft Foundry Local** - Do lokalnego uruchamiania modeli AI

### Zalecane narzędzia

- **Visual Studio Code** - Z rozszerzeniami Python, Jupyter i Pylance
- **Windows Terminal** - Dla lepszego doświadczenia w wierszu poleceń (użytkownicy Windows)
- **Docker** - Do konteneryzowanego rozwoju (opcjonalnie)

### Wymagania systemowe

- **RAM**: Minimum 8GB, zalecane 16GB+ dla scenariuszy z wieloma modelami
- **Pamięć**: Minimum 10GB wolnego miejsca na modele i zależności
- **System operacyjny**: Windows 10/11, macOS 11+ lub Linux (Ubuntu 20.04+)
- **Sprzęt**: CPU z obsługą AVX2; GPU (CUDA, Qualcomm NPU) opcjonalne, ale zalecane

### Wymagana wiedza

- Podstawowa znajomość programowania w Pythonie
- Znajomość interfejsów wiersza poleceń
- Zrozumienie koncepcji AI/ML (do rozwoju próbek)
- Przepływy pracy Git i procesy pull requestów

## Polecenia konfiguracji

### Konfiguracja repozytorium

```bash
# Clone the repository
git clone https://github.com/microsoft/edgeai-for-beginners.git
cd edgeai-for-beginners

# No build step required - this is primarily an educational content repository
```

### Konfiguracja próbek w Pythonie (Moduł08 i próbki warsztatowe)

```bash
# Create and activate virtual environment
python -m venv .venv
# On Windows
.venv\Scripts\activate
# On macOS/Linux
source .venv/bin/activate

# Install Foundry Local SDK and dependencies
pip install foundry-local-sdk openai

# Install additional dependencies for Module08 samples
cd Module08
pip install -r requirements.txt

# Install Workshop dependencies
cd ../Workshop
pip install -r requirements.txt
```

### Konfiguracja próbek Node.js (Próbka 08 - Windows Chat App)

```bash
cd Module08/samples/08
npm install

# Start in development mode
npm run dev

# Build for production
npm run build

# Create installer
npm run dist
```

### Konfiguracja Foundry Local

Foundry Local jest wymagane do uruchamiania próbek. Pobierz i zainstaluj z oficjalnego repozytorium:

**Instalacja:**
- **Windows**: `winget install Microsoft.FoundryLocal`
- **macOS**: `brew tap microsoft/foundrylocal && brew install foundrylocal`
- **Ręczna**: Pobierz z [strony wydania](https://github.com/microsoft/Foundry-Local/releases)

**Szybki start:**
```bash
# Run your first model (auto-downloads if needed)
foundry model run phi-4-mini

# List available models
foundry model ls

# Check service status
foundry service status
```

**Uwaga**: Foundry Local automatycznie wybiera najlepszy wariant modelu dla Twojego sprzętu (CUDA GPU, Qualcomm NPU lub CPU).

## Przepływ pracy programistycznej

### Rozwój treści

To repozytorium zawiera głównie **edukacyjne treści Markdown**. Podczas wprowadzania zmian:

1. Edytuj pliki `.md` w odpowiednich katalogach modułów
2. Przestrzegaj istniejących wzorców formatowania
3. Upewnij się, że przykłady kodu są poprawne i przetestowane
4. Zaktualizuj odpowiednie tłumaczenia, jeśli to konieczne (lub pozwól, aby zajęła się tym automatyzacja)

### Rozwój aplikacji przykładowych

Dla próbek Python w Moduł08 (próbki 01-07, 09-10):
```bash
cd Module08
python samples/01/chat_quickstart.py "Test message"
```

Dla próbek warsztatowych w Pythonie:
```bash
cd Workshop/samples/session01
python chat_bootstrap.py "Test message"
```

Dla próbki Electron (próbka 08):
```bash
cd Module08/samples/08
npm run dev  # Development with hot reload
```

### Testowanie aplikacji przykładowych

Próbki w Pythonie nie mają testów automatycznych, ale można je zweryfikować, uruchamiając:
```bash
# Test basic chat functionality
python samples/01/chat_quickstart.py "Hello"

# Test with specific model
set MODEL=phi-4-mini
python samples/02/openai_sdk_client.py
```

Próbka Electron ma infrastrukturę testową:
```bash
cd Module08/samples/08
npm test           # Run unit tests
npm run test:e2e   # Run end-to-end tests
npm run lint       # Check code style
```

## Instrukcje testowania

### Walidacja treści

Repozytorium korzysta z automatycznych przepływów pracy tłumaczeniowych. Nie jest wymagane ręczne testowanie tłumaczeń.

**Ręczna walidacja zmian treści:**
1. Przeglądaj renderowanie Markdown, podglądając pliki `.md`
2. Upewnij się, że wszystkie linki prowadzą do prawidłowych celów
3. Przetestuj wszelkie fragmenty kodu zawarte w dokumentacji
4. Sprawdź, czy obrazy ładują się poprawnie

### Testowanie aplikacji przykładowych

**Moduł08/próbki/08 (aplikacja Electron) ma kompleksowe testy:**
```bash
cd Module08/samples/08

# Run all tests
npm test

# Run unit tests only
npm test -- --testPathPattern=unit

# Run integration tests
npm run test:integration

# Run E2E tests
npm run test:e2e

# Check test coverage
npm test -- --coverage
```

**Próbki w Pythonie powinny być testowane ręcznie:**
```bash
# Module08 samples
python samples/01/chat_quickstart.py "Test prompt"
python samples/04/chainlit_rag.py
python samples/09/multi_agent_system.py

# Workshop samples
cd Workshop/samples/session01
python chat_bootstrap.py "Test prompt"

# Use Workshop validation tools
cd Workshop/scripts
python validate_samples.py  # Validate syntax and imports
python test_samples.py      # Run smoke tests
```

## Wytyczne dotyczące stylu kodu

### Treści Markdown

- Używaj spójnej hierarchii nagłówków (# dla tytułu, ## dla głównych sekcji, ### dla podsekcji)
- Dołączaj bloki kodu ze specyfikatorami języka: ```python, ```bash, ```javascript
- Przestrzegaj istniejącego formatowania dla tabel, list i wyróżnień
- Zachowaj czytelność linii (celuj w ~80-100 znaków, ale nie rygorystycznie)
- Używaj linków względnych dla odwołań wewnętrznych

### Styl kodu w Pythonie

- Przestrzegaj konwencji PEP 8
- Używaj wskazówek typów tam, gdzie to możliwe
- Dołączaj docstringi dla funkcji i klas
- Używaj znaczących nazw zmiennych
- Zachowaj funkcje skoncentrowane i zwięzłe

### Styl kodu w JavaScript/Node.js

```bash
# Electron sample follows ESLint configuration
cd Module08/samples/08
npm run lint        # Check for style issues
npm run lint:fix    # Auto-fix style issues
npm run format      # Format with Prettier
```

**Kluczowe konwencje:**
- Konfiguracja ESLint dostarczona w próbce 08
- Prettier do formatowania kodu
- Używaj nowoczesnej składni ES6+
- Przestrzegaj istniejących wzorców w kodzie

## Wytyczne dotyczące pull requestów

### Przepływ pracy przy wkładzie

1. **Fork repozytorium** i utwórz nową gałąź z `main`
2. **Wprowadź zmiany** zgodnie z wytycznymi dotyczącymi stylu kodu
3. **Dokładnie przetestuj** korzystając z powyższych instrukcji testowania
4. **Zatwierdź z jasnymi komunikatami** zgodnie z formatem konwencjonalnych zatwierdzeń
5. **Wypchnij do swojego forka** i utwórz pull request
6. **Odpowiedz na uwagi** od opiekunów podczas przeglądu

### Konwencja nazewnictwa gałęzi

- `feature/<module>-<description>` - Dla nowych funkcji lub treści
- `fix/<module>-<description>` - Dla poprawek błędów
- `docs/<description>` - Dla ulepszeń dokumentacji
- `refactor/<description>` - Dla refaktoryzacji kodu

### Format komunikatów zatwierdzeń

Przestrzegaj [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

**Przykłady:**
```
feat(Module08): add intent-based routing notebook
docs(AGENTS): update Foundry Local setup instructions
fix(samples/08): resolve Electron build issue
```

### Format tytułu
```
[ModuleXX] Brief description of change
```
lub
```
[Module08/samples/XX] Description for sample changes
```

### Kodeks postępowania

Wszyscy współtwórcy muszą przestrzegać [Kodeksu postępowania Microsoft Open Source](https://opensource.microsoft.com/codeofconduct/). Proszę zapoznać się z [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) przed wniesieniem wkładu.

### Przed przesłaniem

**Dla zmian treści:**
- Przejrzyj wszystkie zmodyfikowane pliki Markdown
- Zweryfikuj działanie linków i obrazów
- Sprawdź błędy ortograficzne i gramatyczne

**Dla zmian kodu próbki (Moduł08/próbki/08):**
```bash
npm run lint
npm test
```

**Dla zmian próbek w Pythonie:**
- Przetestuj, czy próbka działa poprawnie
- Zweryfikuj działanie obsługi błędów
- Sprawdź kompatybilność z Foundry Local

### Proces przeglądu

- Zmiany treści edukacyjnych są przeglądane pod kątem dokładności i jasności
- Próbki kodu są testowane pod kątem funkcjonalności
- Aktualizacje tłumaczeń są obsługiwane automatycznie przez GitHub Actions

## System tłumaczeń

**WAŻNE:** To repozytorium korzysta z automatycznego tłumaczenia za pomocą GitHub Actions.

- Tłumaczenia znajdują się w katalogu `/translations/` (ponad 50 języków)
- Automatyzowane za pomocą przepływu pracy `co-op-translator.yml`
- **NIE edytuj ręcznie plików tłumaczeń** - zostaną nadpisane
- Edytuj tylko angielskie pliki źródłowe w katalogach głównych i modułowych
- Tłumaczenia są automatycznie generowane po przesłaniu do gałęzi `main`

## Integracja z Foundry Local

Większość próbek Moduł08 wymaga uruchomienia Microsoft Foundry Local.

### Instalacja i konfiguracja

**Zainstaluj Foundry Local:**
```bash
# Windows
winget install Microsoft.FoundryLocal

# macOS
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**Zainstaluj Python SDK:**
```bash
pip install foundry-local-sdk openai
```

### Uruchamianie Foundry Local
```bash
# Start service and run a model (auto-downloads if needed)
foundry model run phi-3.5-mini

# Or use model aliases for automatic hardware optimization
foundry model run phi-4-mini
foundry model run qwen2.5-0.5b
foundry model run qwen2.5-coder-0.5b

# Check service status
foundry service status

# List available models
foundry model ls
```

### Użycie SDK (Python)
```python
from foundry_local import FoundryLocalManager
import openai

# Use model alias for automatic hardware optimization
alias = "phi-4-mini"

# Create manager (auto-starts service and loads model)
manager = FoundryLocalManager(alias)

# Configure OpenAI client for local Foundry service
client = openai.OpenAI(
    base_url=manager.endpoint,
    api_key=manager.api_key
)

# Use the model
response = client.chat.completions.create(
    model=manager.get_model_info(alias).id,
    messages=[{"role": "user", "content": "Hello!"}]
)
```

### Weryfikacja Foundry Local
```bash
# Service status and endpoint
foundry service status

# List loaded models (REST API)
curl http://localhost:<port>/v1/models

# Note: Port is displayed when running 'foundry service status'
```

### Zmienne środowiskowe dla próbek

Większość próbek używa tych zmiennych środowiskowych:
```bash
# Foundry Local configuration
# Note: The SDK (FoundryLocalManager) automatically detects endpoint
set MODEL=phi-4-mini  # or phi-3.5-mini, qwen2.5-0.5b, qwen2.5-coder-0.5b
set API_KEY=            # Not required for local usage

# Manual endpoint (if not using SDK)
# Port is shown via 'foundry service status'
set BASE_URL=http://localhost:<port>

# For Azure OpenAI fallback (optional)
set AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
set AZURE_OPENAI_API_KEY=your-api-key
set AZURE_OPENAI_API_VERSION=2024-08-01-preview
```

**Uwaga**: Korzystając z `FoundryLocalManager`, SDK automatycznie obsługuje wykrywanie usług i ładowanie modeli. Alias modelu (np. `phi-3.5-mini`) zapewnia wybór najlepszego wariantu dla Twojego sprzętu.

## Budowanie i wdrażanie

### Wdrażanie treści

To repozytorium to głównie dokumentacja - proces budowania nie jest wymagany dla treści.

### Budowanie aplikacji przykładowych

**Aplikacja Electron (Moduł08/próbki/08):**
```bash
cd Module08/samples/08

# Development build
npm run dev

# Production build
npm run build

# Create Windows installer
npm run dist

# Create portable executable
npm run pack
```

**Próbki w Pythonie:**
Brak procesu budowania - próbki są uruchamiane bezpośrednio za pomocą interpretera Pythona.

## Typowe problemy i rozwiązywanie problemów

> **Wskazówka**: Sprawdź [GitHub Issues](https://github.com/microsoft/edgeai-for-beginners/issues) dla znanych problemów i rozwiązań.

### Krytyczne problemy (blokujące)

#### Foundry Local nie działa
**Problem:** Próby kończą się błędami połączenia

**Rozwiązanie:**
```bash
# Check if service is running
foundry service status

# Start service with a model
foundry model run phi-4-mini

# Or explicitly start service
foundry service start

# List loaded models
foundry model ls

# Verify via REST API (port shown in 'foundry service status')
curl http://localhost:<port>/v1/models
```

### Typowe problemy (umiarkowane)

#### Problemy z wirtualnym środowiskiem Pythona
**Problem:** Błędy importu modułów

**Rozwiązanie:**
```bash
# Ensure virtual environment is activated
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt
```

#### Problemy z budowaniem Electron
**Problem:** Błędy `npm install` lub budowania

**Rozwiązanie:**
```bash
cd Module08/samples/08
# Clean install
npm run clean
rm -rf node_modules package-lock.json
npm install
```

### Problemy z przepływem pracy (drobne)

#### Konflikty w przepływie pracy tłumaczeń
**Problem:** Konflikty PR tłumaczeń z Twoimi zmianami

**Rozwiązanie:**
- Edytuj tylko angielskie pliki źródłowe
- Pozwól, aby automatyczny przepływ pracy tłumaczeń obsłużył tłumaczenia
- Jeśli wystąpią konflikty, scal `main` do swojej gałęzi po scaleniu tłumaczeń

#### Problemy z pobieraniem modeli
**Problem:** Foundry Local nie może pobrać modeli

**Rozwiązanie:**
```bash
# Check internet connectivity
# Clear model cache and retry
foundry model remove <model-alias>
foundry model run <model-alias>

# Check available disk space (models can be 2-16GB)
# Verify firewall settings allow downloads
```

## Dodatkowe zasoby

### Ścieżki nauki
- **Ścieżka dla początkujących:** Moduły 01-02 (7-9 godzin)
- **Ścieżka średniozaawansowana:** Moduły 03-04 (9-11 godzin)
- **Ścieżka zaawansowana:** Moduły 05-07 (12-15 godzin)
- **Ścieżka ekspercka:** Moduł 08 (8-10 godzin)
- **Warsztaty praktyczne:** Materiały warsztatowe (6-8 godzin)

### Kluczowe treści modułów
- **Moduł01:** Podstawy EdgeAI i studia przypadków
- **Moduł02:** Rodziny i architektury Małych Modeli Językowych (SLM)
- **Moduł03:** Strategie wdrażania lokalnego i w chmurze
- **Moduł04:** Optymalizacja modeli z wieloma frameworkami (Llama.cpp, Microsoft Olive, OpenVINO, Qualcomm QNN, Apple MLX)
- **Moduł05:** SLMOps - operacje produkcyjne
- **Moduł06:** Agenci AI i wywoływanie funkcji
- **Moduł07:** Implementacje specyficzne dla platform
- **Moduł08:** Narzędzia Foundry Local z 10 kompleksowymi próbkami

### Zewnętrzne zależności
- [Microsoft Foundry Local](https://github.com/microsoft/Foundry-Local) - Lokalny runtime modeli AI z kompatybilnym API OpenAI
  - [Dokumentacja](https://github.com/microsoft/Foundry-Local/blob/main/docs/README.md)
  - [Python SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/python)
  - [JavaScript SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/javascript)
- [Llama.cpp](https://github.com/ggml-org/llama.cpp) - Framework optymalizacyjny
- [Microsoft Olive](https://microsoft.github.io/Olive/) - Narzędzie do optymalizacji modeli
- [OpenVINO](https://docs.openvino.ai/) - Narzędzie optymalizacyjne Intela

## Uwagi specyficzne dla projektu

### Aplikacje przykładowe Moduł08

Repozytorium zawiera 10 kompleksowych aplikacji przykładowych:

1. **01-REST Chat Quickstart** - Podstawowa integracja OpenAI SDK
2. **02-OpenAI SDK Integration** - Zaawansowane funkcje SDK
3. **03-Model Discovery & Benchmarking** - Narzędzia do porównywania modeli
4.
10. **10-Narzędzia Foundry Framework** - Integracja LangChain/Semantic Kernel

### Przykładowe aplikacje warsztatowe

Warsztat obejmuje 6 progresywnych sesji z praktycznymi wdrożeniami:

1. **Sesja 01** - Rozpoczęcie pracy z Foundry Local
2. **Sesja 02** - Pipeline RAG i ocena z użyciem RAGAS
3. **Sesja 03** - Benchmarking modeli open-source
4. **Sesja 04** - Porównanie i wybór modeli
5. **Sesja 05** - Systemy orkiestracji wieloagentowej
6. **Sesja 06** - Routing modeli i zarządzanie pipeline'ami

Każdy przykład pokazuje różne aspekty rozwoju AI na urządzeniach brzegowych z Foundry Local.

### Uwagi dotyczące wydajności

- SLM-y zoptymalizowane do wdrożeń na urządzeniach brzegowych (2-16GB RAM)
- Lokalna inferencja zapewnia czasy odpowiedzi od 50 do 500 ms
- Techniki kwantyzacji zmniejszają rozmiar o 75% przy zachowaniu 85% wydajności
- Możliwości prowadzenia rozmów w czasie rzeczywistym z lokalnymi modelami

### Bezpieczeństwo i prywatność

- Całe przetwarzanie odbywa się lokalnie - dane nie są wysyłane do chmury
- Odpowiednie dla aplikacji wrażliwych na prywatność (opieka zdrowotna, finanse)
- Spełnia wymagania dotyczące suwerenności danych
- Foundry Local działa w pełni na lokalnym sprzęcie

## Uzyskiwanie pomocy

### Dokumentacja

- **Główne README**: [README.md](README.md) - Przegląd repozytorium i ścieżki nauki
- **Przewodnik nauki**: [STUDY_GUIDE.md](STUDY_GUIDE.md) - Zasoby edukacyjne i harmonogram
- **Wsparcie**: [SUPPORT.md](SUPPORT.md) - Jak uzyskać pomoc
- **Bezpieczeństwo**: [SECURITY.md](SECURITY.md) - Zgłaszanie problemów związanych z bezpieczeństwem

### Wsparcie społeczności

- **Problemy na GitHub**: [Zgłaszanie błędów lub propozycje funkcji](https://github.com/microsoft/edgeai-for-beginners/issues)
- **Dyskusje na GitHub**: [Zadawanie pytań i dzielenie się pomysłami](https://github.com/microsoft/edgeai-for-beginners/discussions)
- **Problemy z Foundry Local**: [Problemy techniczne z Foundry Local](https://github.com/microsoft/Foundry-Local/issues)

### Kontakt

- **Opiekunowie**: Zobacz [CODEOWNERS](https://github.com/microsoft/edgeai-for-beginners/blob/main/.github/CODEOWNERS)
- **Problemy związane z bezpieczeństwem**: Postępuj zgodnie z zasadami odpowiedzialnego zgłaszania w [SECURITY.md](SECURITY.md)
- **Wsparcie Microsoft**: W przypadku wsparcia dla przedsiębiorstw skontaktuj się z obsługą klienta Microsoft

### Dodatkowe zasoby

- **Microsoft Learn**: [Ścieżki nauki AI i uczenia maszynowego](https://learn.microsoft.com/training/browse/?products=ai-services)
- **Dokumentacja Foundry Local**: [Oficjalna dokumentacja](https://github.com/microsoft/Foundry-Local/blob/main/docs/README.md)
- **Przykłady społeczności**: Sprawdź [Dyskusje na GitHub](https://github.com/microsoft/edgeai-for-beginners/discussions) w poszukiwaniu wkładów społeczności

---

**To edukacyjne repozytorium skupia się na nauczaniu rozwoju AI na urządzeniach brzegowych. Głównym wzorcem wkładu jest ulepszanie treści edukacyjnych oraz dodawanie/rozbudowa aplikacji demonstracyjnych, które pokazują koncepcje AI na urządzeniach brzegowych.**

---

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dokładamy wszelkich starań, aby tłumaczenie było precyzyjne, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za autorytatywne źródło. W przypadku informacji krytycznych zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
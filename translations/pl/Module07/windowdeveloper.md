# Przewodnik po rozwoju Windows Edge AI

## Wprowadzenie

Witamy w Windows Edge AI Development – kompleksowym przewodniku po tworzeniu inteligentnych aplikacji wykorzystujących moc AI na urządzeniu dzięki platformie Windows AI Foundry firmy Microsoft. Ten przewodnik jest specjalnie zaprojektowany dla programistów Windows, którzy chcą zintegrować najnowocześniejsze funkcje Edge AI w swoich aplikacjach, korzystając z pełnego spektrum akceleracji sprzętowej Windows.

### Przewaga Windows AI

Windows AI Foundry to zunifikowana, niezawodna i bezpieczna platforma wspierająca cały cykl życia programisty AI – od wyboru i dostrojenia modelu po optymalizację i wdrożenie na procesorach CPU, GPU, NPU oraz architekturach hybrydowej chmury. Ta platforma demokratyzuje rozwój AI, oferując:

- **Abstrakcja sprzętu**: Bezproblemowe wdrażanie na krzemie AMD, Intel, NVIDIA i Qualcomm
- **Inteligencja na urządzeniu**: AI respektująca prywatność, działająca całkowicie lokalnie
- **Optymalna wydajność**: Modele zoptymalizowane pod kątem konfiguracji sprzętowych Windows
- **Gotowość dla przedsiębiorstw**: Bezpieczeństwo i zgodność na poziomie produkcyjnym

### Windows ML 
Windows Machine Learning (ML) umożliwia programistom C#, C++ i Python uruchamianie lokalnie modeli AI ONNX na komputerach z Windows za pomocą ONNX Runtime, z automatycznym zarządzaniem dostawcami wykonywania dla różnych sprzętów (CPU, GPU, NPU). [ONNX Runtime](https://onnxruntime.ai/docs/) może być używany z modelami z PyTorch, Tensorflow/Keras, TFLite, scikit-learn i innych frameworków.


![WindowsML Diagram pokazujący model ONNX przechodzący przez Windows ML, a następnie trafiający do NPU, GPU i CPU.](https://learn.microsoft.com/en-us/windows/ai/images/winml-diagram.png)

Windows ML zapewnia współdzieloną kopię ONNX Runtime dla całego Windows oraz możliwość dynamicznego pobierania dostawców wykonywania (EP).

### Dlaczego Windows dla Edge AI?

**Uniwersalne wsparcie sprzętowe**
Windows ML zapewnia automatyczną optymalizację sprzętową w całym ekosystemie Windows, gwarantując optymalną wydajność aplikacji AI niezależnie od architektury krzemu.

**Zintegrowany runtime AI**
Wbudowany silnik inferencji Windows ML eliminuje skomplikowane wymagania konfiguracyjne, pozwalając programistom koncentrować się na logice aplikacji zamiast na infrastrukturze.

**Optymalizacja Copilot+ PC**
Wyspecjalizowane API zaprojektowane specjalnie dla urządzeń Windows następnej generacji z dedykowanymi jednostkami przetwarzania neuronowego (NPU), zapewniającymi wyjątkową wydajność energetyczną.

**Ekosystem programistyczny**
Bogaty zestaw narzędzi, w tym integracja z Visual Studio, obszerna dokumentacja i przykładowe aplikacje przyspieszające cykle rozwoju.

## Cele nauki

Po ukończeniu tego przewodnika Windows Edge AI opanujesz kluczowe umiejętności niezbędne do tworzenia gotowych do produkcji aplikacji AI na platformie Windows.

### Podstawowe kompetencje techniczne

**Mistrzostwo Windows AI Foundry**
- Zrozumienie architektury i komponentów platformy Windows AI Foundry
- Poruszanie się w pełnym cyklu rozwoju AI w ekosystemie Windows
- Wdrażanie najlepszych praktyk bezpieczeństwa dla aplikacji AI na urządzeniu
- Optymalizacja aplikacji dla różnych konfiguracji sprzętowych Windows

**Ekspertyza integracji API**
- Opanowanie Windows AI APIs dla aplikacji tekstowych, wizyjnych i multimodalnych
- Wdrożenie integracji modelu językowego Phi Silica do generowania tekstu i rozumowania
- Uruchomienie funkcji wizji komputerowej z wykorzystaniem wbudowanych API do przetwarzania obrazu
- Dostosowywanie modeli wstępnie wytrenowanych przy użyciu technik LoRA (Low-Rank Adaptation)

**Implementacja Foundry Local**
- Przeglądanie, ocenianie i wdrażanie otwartych modeli językowych z użyciem Foundry Local CLI
- Zrozumienie optymalizacji modelu i kwantyzacji do lokalnego wdrożenia
- Wdrażanie funkcji AI offline działających bez połączenia z internetem
- Zarządzanie cyklem życia modeli i aktualizacjami w środowiskach produkcyjnych

**Wdrożenie Windows ML**
- Przenoszenie niestandardowych modeli ONNX do aplikacji Windows za pomocą Windows ML
- Wykorzystanie automatycznej akceleracji sprzętowej na architekturach CPU, GPU i NPU
- Wdrażanie inferencji w czasie rzeczywistym z optymalnym wykorzystaniem zasobów
- Projektowanie skalowalnych aplikacji AI dla różnych kategorii urządzeń Windows

### Umiejętności rozwoju aplikacji

**Programowanie wieloplatformowe Windows**
- Tworzenie aplikacji zasilanych AI za pomocą .NET MAUI do uniwersalnego wdrożenia Windows
- Integracja funkcji AI z aplikacjami Win32, UWP i Progressive Web Applications
- Wdrażanie responsywnych projektów interfejsu dostosowujących się do stanów przetwarzania AI
- Obsługa asynchronicznych operacji AI z właściwymi wzorcami UX

**Optymalizacja wydajności**
- Profilowanie i optymalizacja wydajności inferencji AI na różnych konfiguracjach sprzętowych
- Wdrażanie efektywnego zarządzania pamięcią dla dużych modeli językowych
- Projektowanie aplikacji degradujących się łagodnie w zależności od dostępnych możliwości sprzętowych
- Stosowanie strategii cache'owania dla często używanych operacji AI

**Gotowość do produkcji**
- Wdrażanie wszechstronnej obsługi błędów i mechanizmów awaryjnych
- Projektowanie telemetrii i monitoringu wydajności aplikacji AI
- Zastosowanie najlepszych praktyk bezpieczeństwa dla lokalnego przechowywania i uruchamiania modeli AI
- Planowanie strategii wdrożenia dla aplikacji korporacyjnych i konsumenckich

### Zrozumienie biznesowe i strategiczne

**Architektura aplikacji AI**
- Projektowanie architektur hybrydowych optymalizujących przetwarzanie AI między lokalnie a w chmurze
- Ocena kompromisów między rozmiarem modelu, dokładnością a szybkością inferencji
- Planowanie architektur przepływu danych utrzymujących prywatność przy jednoczesnym umożliwieniu inteligencji
- Wdrażanie ekonomicznych rozwiązań AI skalujących się zgodnie z potrzebami użytkowników

**Pozycjonowanie rynkowe**
- Zrozumienie przewag konkurencyjnych natywnych aplikacji AI dla Windows
- Identyfikacja przypadków użycia, w których AI na urządzeniu zapewnia lepsze doświadczenia użytkownika
- Opracowanie strategii wejścia na rynek dla aplikacji Windows wzbogaconych o AI
- Pozycjonowanie aplikacji z wykorzystaniem korzyści ekosystemu Windows

## Przykłady AI Windows App SDK

Windows App SDK dostarcza obszerne przykłady pokazujące integrację AI w różnych frameworkach i scenariuszach wdrożeniowych. Przykłady te są podstawowymi odniesieniami do zrozumienia wzorców rozwoju Windows AI.

### Przykłady Windows AI Foundry

| Przykład | Framework | Obszar fokusowy | Kluczowe cechy |
|--------|-----------|------------|-------------|
| [cs-winui](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsAIFoundry/cs-winui) | C# WinUI 3 | Integracja Windows AI APIs | Kompletny WinUI app demonstrujący API Windows AI, optymalizacja ARM64, pakowane wdrożenie |

**Kluczowe technologie:**
- Windows AI APIs
- Framework WinUI 3
- Optymalizacja platformy ARM64
- Kompatybilność Copilot+ PC
- Wdrożenie pakowanej aplikacji

**Wymagania wstępne:**
- Windows 11 z Copilot+ PC zalecane
- Visual Studio 2022
- Konfiguracja budowania ARM64
- Windows App SDK 1.8.1+

### Przykłady Windows ML

#### Przykłady C++

| Przykład | Typ | Obszar fokusowy | Kluczowe cechy |
|--------|------|------------|-------------|
| [CppConsoleDesktop](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Aplikacja konsolowa | Podstawy Windows ML | Odkrywanie EP, opcje wiersza poleceń, kompilacja modelu |
| [CppConsoleDesktop.FrameworkDependent](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Aplikacja konsolowa | Wdrażanie zależne od frameworka | Współdzielone środowisko uruchomieniowe, mniejszy rozmiar wdrożenia |
| [CppConsoleDesktop.SelfContained](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Aplikacja konsolowa | Wdrożenie samodzielne | Samodzielne wdrożenie, bez zależności środowiskowych |
| [CppConsoleDll](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | DLL | Użycie biblioteki | WindowsML w bibliotece współdzielonej, zarządzanie pamięcią |
| [CppResnetBuildDemo](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Demo | Tutorial ResNet | Konwersja modelu, kompilacja EP, tutorial Build 2025 |

#### Przykłady C#

**Aplikacje konsolowe**

| Przykład | Typ | Obszar fokusowy | Kluczowe cechy |
|--------|------|------------|-------------|
| [CSharpConsoleDesktop](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs) | Aplikacja konsolowa | Podstawowa integracja C# | Współdzielone użycie helperów, interfejs wiersza poleceń |
| [ResnetBuildDemoCS](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs) | Demo | Tutorial ResNet | Konwersja modelu, kompilacja EP, tutorial Build 2025 |

**Aplikacje GUI**

| Przykład | Framework | Obszar fokusowy | Kluczowe cechy |
|--------|-----------|------------|-------------|
| [cs-wpf](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs-wpf) | WPF | GUI desktopowe | Klasyfikacja obrazów z interfejsem WPF |
| [cs-winforms](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs-winforms) | Windows Forms | Tradycyjne GUI | Klasyfikacja obrazów z Windows Forms |
| [cs-winui](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs-winui) | WinUI 3 | Nowoczesne GUI | Klasyfikacja obrazów z interfejsem WinUI 3 |

#### Przykłady Python

| Przykład | Język | Obszar fokusowy | Kluczowe cechy |
|--------|----------|------------|-------------|
| [SqueezeNetPython](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/python) | Python | Klasyfikacja obrazów | Wiązania WinML dla Pythona, wsadowe przetwarzanie obrazów |

### Wymagania wstępne dla przykładów

**Wymagania systemowe:**
- Komputer z Windows 11 w wersji 24H2 (build 26100) lub nowszej
- Visual Studio 2022 z obciążeniami C++ i .NET
- Windows App SDK 1.8.1 lub nowszy
- Python 3.10-3.13 do przykładów Python na urządzeniach x64 i ARM64

**Specyficzne dla Windows AI Foundry:**
- Zalecany Copilot+ PC dla optymalnej wydajności
- Konfiguracja budowania ARM64 dla przykładów Windows AI
- Wymagana tożsamość pakietu (aplikacje niepakowane nie są już wspierane)

### Typowy przebieg pracy z przykładem

Większość przykładów Windows ML stosuje ten standardowy schemat:

1. **Inicjalizacja środowiska** - Utworzenie środowiska ONNX Runtime
2. **Rejestracja dostawców wykonywania** - Wykrywanie i rejestracja dostępnych akceleratorów sprzętowych (CPU, GPU, NPU)
3. **Załaduj model** - Załaduj model ONNX, opcjonalnie skompiluj dla docelowego sprzętu
4. **Wstępne przetwarzanie danych wejściowych** - Konwersja obrazów/danych do formatu wejściowego modelu
5. **Wykonanie inferencji** - Uruchomienie modelu i uzyskanie predykcji
6. **Przetwarzanie wyników** - Zastosowanie softmax i wyświetlenie najlepszych predykcji

### Używane pliki modelu

| Model | Cel | W zestawie | Uwagi |
|-------|---------|----------|-------|
| SqueezeNet | Lekka klasyfikacja obrazów | ✅ W zestawie | Wytrenowany, gotowy do użycia |
| ResNet-50 | Wysokodokładna klasyfikacja obrazów | ❌ Wymaga konwersji | Użyj [AI Toolkit](https://code.visualstudio.com/docs/intelligentapps/modelconversion) do konwersji |

### Wsparcie sprzętowe

Wszystkie przykłady automatycznie wykrywają i wykorzystują dostępny sprzęt:
- **CPU** - Uniwersalne wsparcie na wszystkich urządzeniach Windows
- **GPU** - Automatyczne wykrywanie i optymalizacja dla dostępnego sprzętu graficznego
- **NPU** - Wykorzystanie jednostek przetwarzania neuronowego na obsługiwanych urządzeniach (Copilot+ PC)

## Komponenty platformy Windows AI Foundry

### 1. Windows AI APIs

Windows AI APIs dostarczają gotowe do użycia funkcje AI oparte na modelach działających na urządzeniu, zoptymalizowane pod kątem wydajności i efektywności na urządzeniach Copilot+ PC, z minimalną koniecznością konfiguracji.

#### Podstawowe kategorie API

**Model językowy Phi Silica**
- Mały, lecz potężny model językowy do generowania tekstu i rozumowania
- Optymalizowany pod kątem inferencji w czasie rzeczywistym przy minimalnym zużyciu energii
- Wsparcie dla dostosowywania za pomocą technik LoRA
- Integracja z semantycznym wyszukiwaniem Windows i pobieraniem wiedzy

**API wizji komputerowej**
- **Rozpoznawanie tekstu (OCR)**: Wydobywanie tekstu z obrazów z wysoką dokładnością
- **Superrozdzielczość zdjęć**: Powiększanie obrazów za pomocą lokalnych modeli AI
- **Segmentacja obrazów**: Identyfikacja i wyodrębnianie określonych obiektów na obrazach
- **Opis obrazu**: Generowanie szczegółowych opisów tekstowych dla treści wizualnych
- **Usuwanie obiektów**: Usuwanie niechcianych obiektów z obrazów przy użyciu AI

**Funkcje multimodalne**
- **Integracja wizji i języka**: Łączenie zrozumienia tekstu i obrazu
- **Wyszukiwanie semantyczne**: Umożliwienie zapytań w naturalnym języku po zawartości multimedialnej
- **Pobieranie wiedzy**: Tworzenie inteligentnych doświadczeń wyszukiwania z lokalnych danych

### 2. Foundry Local

Foundry Local daje programistom szybki dostęp do gotowych modeli językowych open-source działających na silikonie Windows, umożliwiając przeglądanie, testowanie, interakcję i wdrażanie modeli w aplikacjach lokalnych.

#### Przykładowe aplikacje Foundry Local

Repozytorium [Foundry Local](https://github.com/microsoft/Foundry-Local/tree/main/samples) zawiera obszerne przykłady w wielu językach programowania i frameworkach, demonstrujące różne wzorce integracji i przypadki użycia.

| Przykład | Język/Framework | Obszar fokusowy | Kluczowe cechy |
|--------|-------------------|------------|-------------|
| [dotNET/rag](https://github.com/microsoft/Foundry-Local/tree/main/samples/dotNET/rag) | C# / .NET | Implementacja RAG | Integracja Semantic Kernel, magazyn wektorowy Qdrant, embeddingi JINA, ingestia dokumentów, czat streamingowy |
| [electron/foundry-chat](https://github.com/microsoft/Foundry-Local/tree/main/samples/electron/foundry-chat) | JavaScript / Electron | Aplikacja czatu desktopowego | Czat wieloplatformowy, przełączanie modeli lokalnych/chmurowych, integracja OpenAI SDK, strumieniowanie w czasie rzeczywistym |
| [js/hello-foundry-local](https://github.com/microsoft/Foundry-Local/tree/main/samples/js/hello-foundry-local) | JavaScript / Node.js | Podstawowa integracja | Proste użycie SDK, inicjalizacja modelu, podstawowa funkcjonalność czatu |
| [python/hello-foundry-local](https://github.com/microsoft/Foundry-Local/tree/main/samples/python/hello-foundry-local) | Python | Podstawowa integracja | Użycie SDK Python, odpowiedzi streamingowe, API kompatybilne z OpenAI |

| [rust/hello-foundry-local](https://github.com/microsoft/Foundry-Local/tree/main/samples/rust/hello-foundry-local) | Rust | Integracja systemów | Użycie niskopoziomowego SDK, operacje asynchroniczne, klient HTTP reqwest |

#### Kategorie przykładów według zastosowania

**RAG (Retrieval-Augmented Generation)**
- **dotNET/rag**: Kompletny implementacja RAG wykorzystująca Semantic Kernel, wektorową bazę danych Qdrant i osadzenia JINA
- **Architektura**: Przetwarzanie dokumentów → Dzielnie tekstu → Osadzenia wektorowe → Wyszukiwanie podobieństw → Odpowiedzi świadome kontekstu
- **Technologie**: Microsoft.SemanticKernel, Qdrant.Client, osadzenia BERT ONNX, strumieniowe uzupełnianie czatu

**Aplikacje desktopowe**
- **electron/foundry-chat**: Gotowa do produkcji aplikacja czatu z przełączaniem modeli lokalnych/chmurowych
- **Funkcje**: Wybór modelu, strumieniowe odpowiedzi, obsługa błędów, wdrożenie wieloplatformowe
- **Architektura**: Główny proces Electron, komunikacja IPC, bezpieczne skrypty preload

**Przykłady integracji SDK**
- **JavaScript (Node.js)**: Podstawowa interakcja z modelem i strumieniowe odpowiedzi
- **Python**: Użycie API kompatybilnego z OpenAI ze strumieniowaniem asynchronicznym
- **Rust**: Integracja niskopoziomowa z reqwest i tokio dla operacji asynchronicznych

#### Wymagania wstępne dla przykładów Foundry Local

**Wymagania systemowe:**
- Windows 11 z zainstalowanym Foundry Local
- Node.js w wersji 16 lub wyższej dla przykładów JavaScript/Electron
- .NET 8.0 lub wyższy dla przykładów C#
- Python 3.10 lub wyższy dla przykładów Pythona
- Rust 1.70 lub wyższy dla przykładów Rust

**Instalacja:**
```powershell
# Zainstaluj Foundry Local
winget install Microsoft.FoundryLocal

# Zweryfikuj instalację
foundry --version
foundry model list
```

#### Konfiguracja specyficzna dla przykładu

**Przykład dotNET RAG:**
```powershell
# Zainstaluj wymagane pakiety za pomocą NuGet
# Microsoft.SemanticKernel.Connectors.Onnx
# Microsoft.SemanticKernel.Connectors.Qdrant
# Qdrant.Client

# Uruchom bazę danych wektorów Qdrant
docker run -p 6333:6333 qdrant/qdrant

# Uruchom notatnik Jupyter
jupyter notebook rag_foundrylocal_demo.ipynb
```

**Przykład czatu Electron:**
```powershell
# Ustaw zmienne środowiskowe dla awaryjnego przejścia na chmurę
$env:YOUR_API_KEY="your-cloud-api-key"
$env:YOUR_ENDPOINT="your-cloud-endpoint"
$env:YOUR_MODEL_NAME="your-cloud-model"

# Zainstaluj zależności i uruchom
npm install
npm start
```

**Przykłady JavaScript/Python/Rust:**
```powershell
# Pobierz model (przykład z phi-3.5-mini)
foundry model run phi-3.5-mini

# Uruchom odpowiednią próbkę
node src/app.js          # JavaScript
python src/app.py        # Python
cargo run               # Rust
```

#### Kluczowe cechy

**Katalog modeli**
- Kompleksowa kolekcja wstępnie zoptymalizowanych modeli open-source
- Modele zoptymalizowane pod CPU, GPU i NPU gotowe do natychmiastowego wdrożenia
- Wsparcie dla popularnych rodzin modeli takich jak Llama, Mistral, Phi oraz specjalistyczne modele branżowe

**Integracja CLI**
- Interfejs wiersza poleceń do zarządzania i wdrażania modeli
- Automatyczne procesy optymalizacji i kwantyzacji
- Integracja z popularnymi środowiskami deweloperskimi i pipeline’ami CI/CD

**Wdrożenie lokalne**
- Pełna praca offline bez zależności od chmury
- Wsparcie dla niestandardowych formatów i konfiguracji modeli
- Efektywna obsługa modeli z automatyczną optymalizacją sprzętową

### 3. Windows ML

Windows ML jest główną platformą AI i zintegrowanym środowiskiem inferencji na Windows, umożliwiając efektywne wdrażanie niestandardowych modeli na szerokim ekosystemie sprzętowym Windows.

#### Korzyści architektury

**Uniwersalne wsparcie sprzętu**
- Automatyczna optymalizacja dla krzemowych rozwiązań AMD, Intel, NVIDIA i Qualcomm
- Obsługa wykonywania na CPU, GPU i NPU z przezroczystym przełączaniem
- Abstrakcja sprzętowa eliminująca konieczność optymalizacji specyficznej dla platformy

**Elastyczność modeli**
- Wsparcie dla formatu modelu ONNX z automatyczną konwersją z popularnych frameworków
- Deployment niestandardowych modeli z wydajnością produkcyjną
- Integracja z istniejącymi architekturami aplikacji Windows

**Integracja w przedsiębiorstwie**
- Kompatybilność z mechanizmami bezpieczeństwa i zgodności Windows
- Wsparcie dla narzędzi wdrożenia i zarządzania korporacyjnego
- Integracja z systemami zarządzania i monitorowania urządzeń Windows

## Przebieg procesu rozwoju

### Faza 1: Konfiguracja środowiska i narzędzi

**Przygotowanie środowiska deweloperskiego**
1. Zainstaluj Visual Studio 2022 z workloadami C++ i .NET
2. Zainstaluj Windows App SDK 1.8.1 lub nowszy
3. Skonfiguruj narzędzia CLI Windows AI Foundry
4. Skonfiguruj rozszerzenie AI Toolkit dla Visual Studio Code
5. Ustanów narzędzia profilowania i monitorowania wydajności
6. Zapewnij konfigurację builda ARM64 dla optymalizacji PC Copilot+

**Konfiguracja repozytorium przykładów**
1. Sklonuj [repozytorium przykładów Windows App SDK](https://github.com/microsoft/WindowsAppSDK-Samples)
2. Przejdź do `Samples/WindowsAIFoundry/cs-winui` dla przykładów API Windows AI
3. Przejdź do `Samples/WindowsML` dla kompleksowych przykładów Windows ML
4. Zapoznaj się z [wymaganiami builda](https://learn.microsoft.com/windows/apps/windows-app-sdk/system-requirements) dla docelowych platform

**Eksploracja AI Dev Gallery**
- Przeglądaj przykładowe aplikacje i referencyjne implementacje
- Testuj API Windows AI za pomocą interaktywnych demonstracji
- Przeglądaj kod źródłowy pod kątem najlepszych praktyk i wzorców
- Identyfikuj odpowiednie przykłady dla swojego konkretnego zastosowania

### Faza 2: Wybór i integracja modelu

**Analiza wymagań**
- Zdefiniuj wymagania funkcjonalne dla funkcji AI
- Ustal ograniczenia wydajności i cele optymalizacji
- Oceń wymagania dotyczące prywatności i bezpieczeństwa
- Zaplanuj architekturę wdrożenia i strategie skalowania

**Ewaluacja modelu**
- Użyj Foundry Local do testów modeli open-source dla Twojego zastosowania
- Porównaj API Windows AI ze specyficznymi wymaganiami modelu
- Oceń kompromisy między rozmiarem modelu, dokładnością i prędkością inferencji
- Prototypuj podejścia integracyjne z wybranymi modelami

### Faza 3: Rozwój aplikacji

**Podstawowa integracja**
- Zaimplementuj integrację z API Windows AI z odpowiednią obsługą błędów
- Zaprojektuj interfejsy użytkownika dostosowane do przepływów procesów AI
- Wdroż strategie cachowania i optymalizacji inferencji modelu
- Dodaj telemetrykę i monitoring wydajności działania AI

**Testowanie i walidacja**
- Testuj aplikacje na różnych konfiguracjach sprzętu Windows
- Waliduj metryki wydajności pod różnymi obciążeniami
- Wdróż automatyczne testy niezawodności funkcjonalności AI
- Przeprowadź testy UX z funkcjami wzbogaconymi AI

### Faza 4: Optymalizacja i wdrożenie

**Optymalizacja wydajności**
- Profiluj wydajność aplikacji na docelowym sprzęcie
- Optymalizuj zarządzanie pamięcią i strategie ładowania modeli
- Wdróż adaptacyjne zachowanie zależne od możliwości sprzętowych
- Dopasuj doświadczenie użytkownika do różnych scenariuszy wydajności

**Wdrożenie produkcyjne**
- Pakietuj aplikacje z odpowiednimi zależnościami modelu AI
- Wdróż mechanizmy aktualizacji modeli i logiki aplikacji
- Skonfiguruj monitoring i analitykę środowiska produkcyjnego
- Zaplanuj strategie wdrożenia dla przedsiębiorstw i użytkowników indywidualnych

## Praktyczne przykłady wdrożeń

### Przykład 1: Inteligentna aplikacja do przetwarzania dokumentów

Stwórz aplikację Windows przetwarzającą dokumenty z wykorzystaniem wielu funkcji AI:

**Technologie użyte:**
- Phi Silica do streszczania dokumentów i odpowiadania na pytania
- API OCR do ekstrakcji tekstu ze skanowanych dokumentów
- API do opisu obrazów do analizy wykresów i diagramów
- Niestandardowe modele ONNX do klasyfikacji dokumentów

**Podejście do implementacji:**
- Zaprojektuj modułową architekturę z podłączanymi komponentami AI
- Wykonaj asynchroniczne przetwarzanie dużych partii dokumentów
- Dodaj wskaźniki postępu i wsparcie anulowania dla długotrwałych operacji
- Uwzględnij funkcjonowanie offline dla przetwarzania dokumentów wrażliwych

### Przykład 2: System zarządzania zapasami w handlu detalicznym

Stwórz system zarządzania zapasami napędzany AI dla aplikacji detalicznych:

**Technologie użyte:**
- Segmentacja obrazów do identyfikacji produktów
- Niestandardowe modele widzenia do klasyfikacji marek i kategorii
- Wdrożenie Foundry Local z wyspecjalizowanymi modelami języka dla handlu detalicznego
- Integracja z istniejącymi systemami POS i zarządzania zapasami

**Podejście do implementacji:**
- Buduj integrację kamery do skanowania produktów w czasie rzeczywistym
- Zaimplementuj rozpoznawanie kodów kreskowych i wizualnych produktów
- Dodaj naturalne zapytania językowe do zapasów przy użyciu lokalnych modeli językowych
- Zaprojektuj skalowalną architekturę dla wdrożeń wielosklepowych

### Przykład 3: Asystent dokumentacji medycznej

Opracuj narzędzie do dokumentacji medycznej z zachowaniem prywatności:

**Technologie użyte:**
- Phi Silica do generowania notatek medycznych i wspierania decyzji klinicznych
- OCR do digitalizacji odręcznych dokumentacji medycznych
- Niestandardowe modele językowe medyczne wdrożone przez Windows ML
- Lokalna przestrzeń wektorowa do wyszukiwania wiedzy medycznej

**Podejście do implementacji:**
- Zapewnij pełną pracę offline dla prywatności pacjenta
- Wdróż walidację i sugestie terminologii medycznej
- Dodaj logowanie audytu dla zgodności regulacyjnej
- Zaprojektuj integrację z istniejącymi systemami Elektronicznych Kart Zdrowia

## Strategie optymalizacji wydajności

### Rozwój z uwzględnieniem sprzętu

**Optymalizacja NPU**
- Projektuj aplikacje z wykorzystaniem możliwości NPU na PC Copilot+
- Wdróż łagodne przejście do GPU/CPU na urządzeniach bez NPU
- Optymalizuj formaty modeli dla akceleracji specyficznej dla NPU
- Monitoruj wykorzystanie NPU i charakterystyki termiczne

**Zarządzanie pamięcią**
- Wdróż skuteczne strategie ładowania i cachowania modeli
- Używaj mapowania pamięci dla dużych modeli, aby skrócić czas uruchamiania
- Projektuj aplikacje oszczędne pamięciowo dla urządzeń z ograniczonymi zasobami
- Wdróż kwantyzację modeli dla optymalizacji pamięci

**Efektywność baterii**
- Optymalizuj operacje AI dla minimalnego zużycia energii
- Wdróż adaptacyjne przetwarzanie w zależności od stanu baterii
- Projektuj efektywne przetwarzanie w tle dla ciągłej pracy AI
- Korzystaj z narzędzi profilowania zużycia energii do optymalizacji

### Rozważania dotyczące skalowalności

**Wielowątkowość**
- Projektuj bezpieczne dla wątków operacje AI do przetwarzania równoległego
- Wdróż efektywny podział pracy na dostępne rdzenie
- Używaj wzorców async/await dla operacji AI bez blokowania
- Planuj optymalizację puli wątków dla różnych konfiguracji sprzętowych

**Strategie cachowania**
- Wdróż inteligentne cachowanie dla często używanych operacji AI
- Projektuj strategie unieważniania cache dla aktualizacji modeli
- Używaj trwałego cachowania dla kosztownych operacji preprocessing’u
- Wdróż rozproszone cachowanie dla scenariuszy wieloużytkownikowych

## Najlepsze praktyki bezpieczeństwa i prywatności

### Ochrona danych

**Przetwarzanie lokalne**
- Zapewnij, że wrażliwe dane nigdy nie opuszczają urządzenia lokalnego
- Wdróż bezpieczne przechowywanie modeli AI i danych tymczasowych
- Używaj funkcji bezpieczeństwa Windows do izolacji aplikacji
- Stosuj szyfrowanie dla przechowywanych modeli i wyników pośrednich przetwarzania

**Bezpieczeństwo modeli**
- Waliduj integralność modeli przed ich ładowaniem i wykonaniem
- Wdróż bezpieczne mechanizmy aktualizacji modeli
- Używaj podpisanych modeli, aby zapobiegać manipulacjom
- Stosuj kontrolę dostępu do plików modeli i konfiguracji

### Rozważania zgodności

**Zgodność regulacyjna**
- Projektuj aplikacje zgodne z GDPR, HIPAA i innymi wymogami prawnymi
- Wdróż audytowanie procesów podejmowania decyzji AI
- Zapewnij funkcje przejrzystości wyników generowanych przez AI
- Umożliw użytkownikom kontrolę nad przetwarzaniem danych AI

**Bezpieczeństwo w przedsiębiorstwie**
- Integruj się z politykami bezpieczeństwa przedsiębiorstwa Windows
- Wspieraj zarządzane wdrożenie przez narzędzia zarządzania korporacyjnego
- Wdróż kontrolę dostępu opartą na rolach dla funkcji AI
- Zapewnij kontrolę administracyjną nad funkcjonalnościami AI

## Rozwiązywanie problemów i debugowanie

### Częste wyzwania rozwojowe

**Problemy z konfiguracją builda**
- Zapewnij konfigurację platformy ARM64 dla przykładów Windows AI API
- Sprawdź kompatybilność wersji Windows App SDK (wymagane 1.8.1+)
- Zweryfikuj poprawną konfigurację tożsamości pakietu (wymagana dla Windows AI APIs)
- Zweryfikuj wsparcie narzędzi builda dla wersji docelowego frameworka

**Problemy z ładowaniem modeli**
- Zweryfikuj kompatybilność modeli ONNX z Windows ML
- Sprawdź integralność pliku modelu i wymagania formatu
- Zweryfikuj wymagania sprzętowe dla konkretnych modeli
- Debuguj problemy z alokacją pamięci podczas ładowania modelu
- Zapewnij rejestrację dostawcy wykonania dla akceleracji sprzętowej

**Rozważania dotyczące trybu wdrażania**
- **Tryb samodzielny:** Pełne wsparcie z większym rozmiarem wdrożenia
- **Tryb zależny od frameworka:** Mniejszy rozmiar, ale wymaga wspólnego środowiska wykonawczego
- **Aplikacje niezapakowane:** Nieobsługiwane już przez Windows AI APIs
- Używaj `dotnet run -p:Platform=ARM64 -p:SelfContained=true` do samodzielnego wdrożenia ARM64

**Problemy z wydajnością**
- Profiluj wydajność aplikacji na różnych konfiguracjach sprzętowych
- Identyfikuj wąskie gardła w przetwarzaniu AI
- Optymalizuj operacje preprocessing i postprocessing danych
- Wdróż monitorowanie wydajności i alertowanie

**Trudności z integracją**
- Debuguj problemy z integracją API z odpowiednią obsługą błędów
- Zweryfikuj formaty danych wejściowych i wymagania preprocessing’u
- Testuj dokładnie przypadki brzegowe i sytuacje błędów
- Wdróż kompleksowe logowanie dla debugowania problemów produkcyjnych

### Narzędzia i techniki debugowania

**Integracja z Visual Studio**
- Używaj debugera AI Toolkit do analizy wykonania modeli
- Wdróż profilowanie wydajności operacji AI
- Debuguj asynchroniczne operacje AI z obsługą wyjątków
- Używaj narzędzi profilowania pamięci do optymalizacji

**Narzędzia Windows AI Foundry**
- Wykorzystuj Foundry Local CLI do testowania i walidacji modeli
- Używaj narzędzi testowania API Windows AI do weryfikacji integracji
- Wdróż niestandardowe logowanie do monitoringu operacji AI
- Stwórz automatyczne testy niezawodności funkcjonalności AI

## Przyszłościowe zabezpieczenie aplikacji

### Nowo pojawiające się technologie

**Sprzęt nowej generacji**
- Projektuj aplikacje z wykorzystaniem przyszłych możliwości NPU
- Planuj wzrost rozmiarów i złożoności modeli
- Wdróż adaptacyjne architektury dla ewoluującego sprzętu
- Rozważ algorytmy gotowe na kwantowe technologie dla przyszłej kompatybilności

**Zaawansowane możliwości AI**
- Przygotuj się na multimodalną integrację AI z różnymi typami danych
- Planuj współpracę AI w czasie rzeczywistym między wieloma urządzeniami
- Projektuj z myślą o zdolnościach federacyjnego uczenia się
- Rozważ architektury hybrydowe edge-chmura dla inteligencji

### Ciągłe uczenie się i adaptacja

**Aktualizacje modeli**
- Wdróż płynne mechanizmy aktualizacji modeli
- Projektuj aplikacje adaptujące się do lepszych możliwości modeli
- Planuj kompatybilność wsteczną z istniejącymi modelami
- Wdróż testy A/B do oceny wydajności modeli

**Ewolucja funkcji**
- Projektuj modułowe architektury umożliwiające nowe funkcjonalności AI
- Planuj integrację pojawiających się Windows AI APIs
- Wdróż flagi funkcji do stopniowego wdrażania możliwości
- Projektuj interfejsy użytkownika dostosowujące się do ulepszonych funkcji AI

## Podsumowanie

Rozwój Windows Edge AI to połączenie potężnych możliwości AI z solidną, bezpieczną i skalowalną platformą Windows. Opanowując ekosystem Windows AI Foundry, deweloperzy mogą tworzyć inteligentne aplikacje zapewniające wyjątkowe doświadczenia użytkownika przy zachowaniu najwyższych standardów prywatności, bezpieczeństwa i wydajności.

Połączenie Windows AI APIs, Foundry Local i Windows ML zapewnia niezrównaną bazę do budowy kolejnej generacji inteligentnych aplikacji Windows. W miarę rozwoju AI platforma Windows gwarantuje skalowanie aplikacji z nowymi technologiami przy zachowaniu kompatybilności i wydajności na różnorodnym sprzęcie Windows.

Niezależnie czy tworzysz aplikacje konsumenckie, rozwiązania korporacyjne, czy specjalistyczne narzędzia branżowe, rozwój Windows Edge AI umożliwia tworzenie inteligentnych, responsywnych i głęboko zintegrowanych doświadczeń wykorzystujących pełnię możliwości nowoczesnych urządzeń Windows.

## Dodatkowe zasoby

### Dokumentacja i nauka
- [Dokumentacja Windows AI Foundry](https://learn.microsoft.com/windows/ai/)
- [Referencja Windows AI APIs](https://learn.microsoft.com/windows/ai/apis/)
- [Rozpocznij budowanie aplikacji z Windows AI APIs](https://learn.microsoft.com/windows/ai/apis/model-setup)
- [Foundry Local – Pierwsze kroki](https://learn.microsoft.com/windows/ai/foundry-local/get-started/)
- [Przegląd Windows ML](https://learn.microsoft.com/windows/ai/new-windows-ml/overview/)
- [Wymagania systemowe Windows App SDK](https://docs.microsoft.com/windows/apps/windows-app-sdk/system-requirements)

- [Windows App SDK Development Environment Setup](https://docs.microsoft.com/windows/apps/windows-app-sdk/set-up-your-development-environment)
- 

### Przykładowe repozytoria i kod
- [Przykłady Windows App SDK - Windows AI Foundry](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsAIFoundry)
- [Przykłady Windows App SDK - Windows ML](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML)
- [Przykłady inferencji ONNX Runtime](https://github.com/microsoft/onnxruntime-inference-examples)
- [Repozytorium przykładów Windows App SDK](https://github.com/microsoft/WindowsAppSDK-Samples)

### Narzędzia programistyczne
- [AI Toolkit dla Visual Studio Code](https://learn.microsoft.com/windows/ai/toolkit/)
- [Galeria AI Dev](https://learn.microsoft.com/windows/ai/ai-dev-gallery/)
- [Przykłady Windows AI](https://learn.microsoft.com/windows/ai/samples/)
- [Narzędzia do konwersji modeli](https://code.visualstudio.com/docs/intelligentapps/modelconversion)

### Wsparcie techniczne
- [Dokumentacja Windows ML](https://learn.microsoft.com/windows/ai/new-windows-ml/overview)
- [Dokumentacja ONNX Runtime](https://onnxruntime.ai/docs/)
- [Dokumentacja Windows App SDK](https://docs.microsoft.com/windows/apps/windows-app-sdk/)
- [Zgłaszanie problemów - przykłady Windows App SDK](https://github.com/microsoft/WindowsAppSDK-Samples/issues)

### Społeczność i wsparcie
- [Społeczność programistów Windows](https://developer.microsoft.com/en-us/windows/)
- [Blog Windows AI Foundry](https://blogs.windows.com/windowsdeveloper/)
- [Szkolenia Microsoft Learn AI](https://learn.microsoft.com/training/browse/?products=windows&subjects=artificial-intelligence)

---

*Ten przewodnik jest projektowany, aby rozwijać się wraz z szybko ewolu ekosystemem Windows AI. Regularne aktualizacje zapewniają zgodność z najnowszymi możliwościami platformy i najlepszymi praktykami programistycznymi.*

[08. Praktyczne ćwiczenia z Microsoft Foundry Local - Kompletny zestaw narzędzi dla deweloperów](../Module08/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Choć dążymy do dokładności, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub niedokładności. Oryginalny dokument w jego języku źródłowym należy uznawać za autorytatywne źródło. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
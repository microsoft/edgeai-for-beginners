# Moduł 08: Praktyka z Microsoft Foundry Local - Kompletny zestaw narzędzi dla dewelopera

## Przegląd

[Microsoft Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/) reprezentuje nową generację rozwoju AI na krawędzi, oferując programistom potężne narzędzia do tworzenia, wdrażania i skalowania aplikacji AI lokalnie, przy jednoczesnym zachowaniu płynnej integracji z Azure AI Foundry. Ten moduł zapewnia kompleksowe omówienie Foundry Local od instalacji po zaawansowany rozwój agentów.

**Kluczowe technologie:**
- Microsoft Foundry Local CLI i SDK
- Integracja z Azure AI Foundry
- Inference modeli na urządzeniu
- Lokalna pamięć podręczna modeli i optymalizacja
- Architektury oparte na agentach

## Cele nauki

Po ukończeniu tego modułu będziesz:

- **Mistrzem Foundry Local**: Instalacja, konfiguracja i optymalizacja dla rozwoju na Windows 11
- **Wdrażać różnorodne modele**: Uruchamiaj modele phi, qwen, deepseek i GPT lokalnie za pomocą poleceń CLI
- **Budować rozwiązania produkcyjne**: Twórz aplikacje AI z zaawansowanym inżynierią podpowiedzi i integracją danych
- **Wykorzystywać ekosystem open-source**: Integracja modeli Hugging Face i wkłady społeczności
- **Tworzyć agentów AI**: Buduj inteligentnych agentów z możliwością ugruntowania i orkiestracji
- **Implementować wzorce korporacyjne**: Twórz modułowe, skalowalne rozwiązania AI do wdrożeń produkcyjnych

## Struktura sesji

### [1: Rozpoczęcie pracy z Foundry Local](./01.FoundryLocalSetup.md)
**Skupienie**: Instalacja, konfiguracja CLI, wdrażanie modeli i optymalizacja sprzętowa

**Kluczowe tematy**: Kompletny proces instalacji • polecenia CLI • pamięć podręczna modeli • akceleracja sprzętowa • wdrażanie wielu modeli

**Przykład**: [REST Chat Quickstart](./samples/01/README.md) • [Integracja OpenAI SDK](./samples/02/README.md) • [Odkrywanie modeli i benchmarking](./samples/03/README.md)

**Czas trwania**: 2-3 godziny | **Poziom**: Początkujący

---

### [2: Budowa rozwiązań AI z Azure AI Foundry](./02.AzureAIFoundryIntegration.md)
**Skupienie**: Zaawansowana inżynieria podpowiedzi, integracja danych i łączność z chmurą

**Kluczowe tematy**: Inżynieria podpowiedzi • Integracja danych • Azure workflows • Optymalizacja wydajności • Monitorowanie

**Przykład**: [Aplikacja Chainlit RAG](./samples/04/README.md)

**Czas trwania**: 2-3 godziny | **Poziom**: Średniozaawansowany

---

### [3: Open-Source Models Foundry Local](./03.OpenSourceModels.md)
**Skupienie**: Integracja Hugging Face, strategie BYOM i modele społecznościowe

**Kluczowe tematy**: Integracja HuggingFace • Przynieś własny model • Wgląd Model Mondays • Wkłady społeczności • Wybór modelu

**Przykład**: [Orkiestracja Multi-agentowa](./samples/05/README.md)

**Czas trwania**: 2-3 godziny | **Poziom**: Średniozaawansowany

---

### [4: Poznaj modele nowej generacji](./04.CuttingEdgeModels.md)
**Skupienie**: LLM vs SLM, implementacja EdgeAI i zaawansowane demonstracje

**Kluczowe tematy**: Porównanie modeli • Inference na edge vs chmurze • Phi + ONNX Runtime • Aplikacja Chainlit RAG • Optymalizacja WebGPU

**Przykład**: [Router modelek jako narzędzi](./samples/06/README.md)

**Czas trwania**: 3-4 godziny | **Poziom**: Zaawansowany

---

### [5: Szybkie tworzenie agentów zasilanych AI](./05.AIPoweredAgents.md)
**Skupienie**: Architektury agentów, systemowe podpowiedzi, ugruntowanie i orkiestracja

**Kluczowe tematy**: Wzorce projektowe agentów • Inżynieria systemowych podpowiedzi • Techniki ugruntowania • Systemy wieloagentowe • Wdrożenia produkcyjne

**Przykład**: [Orkiestracja Multi-agentowa](./samples/05/README.md) • [Zaawansowany system wieloagentowy](./samples/09/README.md)

**Czas trwania**: 3-4 godziny | **Poziom**: Zaawansowany

---

### [6: Foundry Local - modele jako narzędzia](./06.ModelsAsTools.md)
**Skupienie**: Modularne rozwiązania AI, skalowanie korporacyjne i wzorce produkcyjne

**Kluczowe tematy**: Modele jako narzędzia • Wdrażanie na urządzeniu • Integracja SDK/API • Architektury korporacyjne • Strategie skalowania

**Przykład**: [Router modelek jako narzędzi](./samples/06/README.md) • [Framework Foundry Tools](./samples/10/README.md)

**Czas trwania**: 3-4 godziny | **Poziom**: Ekspert

---

### [7: Wzorce bezpośredniej integracji API](./samples/07/README.md)
**Skupienie**: Czysta integracja REST API bez zależności SDK dla maksymalnej kontroli

**Kluczowe tematy**: Implementacja klienta HTTP • Niestandardowa autoryzacja • Monitorowanie stanu modeli • Odpowiedzi strumieniowe • Obsługa błędów produkcyjnych

**Przykład**: [Klient bezpośredniego API](./samples/07/README.md)

**Czas trwania**: 2-3 godziny | **Poziom**: Średniozaawansowany

---

### [8: Rodzima aplikacja czatu na Windows 11](./samples/08/README.md)
**Skupienie**: Tworzenie nowoczesnych, natywnych aplikacji czatu z integracją Foundry Local

**Kluczowe tematy**: Tworzenie w Electron • Fluent Design System • Natywna integracja Windows • Strumieniowanie w czasie rzeczywistym • Projektowanie interfejsu czatu

**Przykład**: [Aplikacja czatu Windows 11](./samples/08/README.md)

**Czas trwania**: 3-4 godziny | **Poziom**: Zaawansowany

---

### [9: Zaawansowana orkiestracja wieloagentowa](./samples/09/README.md)
**Skupienie**: Skomplikowana koordynacja agentów, specjalistyczne delegowanie zadań i współpracujące przepływy AI

**Kluczowe tematy**: Inteligentna koordynacja agentów • Wzorce wywoływania funkcji • Komunikacja między agentami • Orkiestracja przepływów pracy • Mechanizmy zapewnienia jakości

**Przykład**: [Zaawansowany system wieloagentowy](./samples/09/README.md)

**Czas trwania**: 4-5 godzin | **Poziom**: Ekspert

---

### [10: Foundry Local jako framework narzędzi](./samples/10/README.md)
**Skupienie**: Architektura zorientowana na narzędzia do integracji Foundry Local z istniejącymi aplikacjami i frameworkami

**Kluczowe tematy**: Integracja LangChain • Funkcje Semantic Kernel • Frameworki REST API • Narzędzia CLI • Integracja Jupyter • Wzorce wdrożeń produkcyjnych

**Przykład**: [Framework Foundry Tools](./samples/10/README.md)

**Czas trwania**: 4-5 godzin | **Poziom**: Ekspert

## Wymagania wstępne

### Wymagania systemowe
- **System operacyjny**: Windows 11 (22H2 lub nowszy)
- **Pamięć**: 16GB RAM (zalecane 32GB dla większych modeli)
- **Pamięć masowa**: 50GB wolnego miejsca na pamięć podręczną modeli
- **Sprzęt**: Zalecane urządzenie z NPU (Copilot+ PC), GPU opcjonalnie
- **Sieć**: Szybkie łącze internetowe do początkowego pobrania modeli

### Środowisko deweloperskie

- Visual Studio Code z rozszerzeniem AI Toolkit
- Python 3.10+ i pip
- Git do kontroli wersji
- PowerShell lub Wiersz polecenia
- Azure CLI (opcjonalnie dla integracji z chmurą)

### Wymagane umiejętności
- Podstawowa znajomość koncepcji AI/ML
- Znajomość pracy z wierszem polecenia
- Podstawy programowania w Pythonie
- Koncepcje REST API
- Podstawowa wiedza o promptowaniu i inferencji modeli

## Harmonogram modułu

**Całkowity szacowany czas**: 30-38 godzin

| Sesja | Obszar skupienia | Przykłady | Czas | Trudność |
|---------|------------|---------|------|------------|
|  1 | Instalacja i podstawy | 01, 02, 03 | 2-3 godziny | Początkujący |
|  2 | Rozwiązania AI | 04 | 2-3 godziny | Średniozaawansowany |
|  3 | Open Source | 05 | 2-3 godziny | Średniozaawansowany |
|  4 | Zaawansowane modele | 06 | 3-4 godziny | Zaawansowany |
|  5 | Agenci AI | 05, 09 | 3-4 godziny | Zaawansowany |
|  6 | Narzędzia korporacyjne | 06, 10 | 3-4 godziny | Ekspert |
|  7 | Bezpośrednia integracja API | 07 | 2-3 godziny | Średniozaawansowany |
|  8 | Aplikacja czatu Windows 11 | 08 | 3-4 godziny | Zaawansowany |
|  9 | Zaawansowany system multi-agent | 09 | 4-5 godzin | Ekspert |
| 10 | Framework narzędzi | 10 | 4-5 godzin | Ekspert |

## Kluczowe zasoby

**Oficjalna dokumentacja:**
- [Microsoft Foundry Local GitHub](https://github.com/microsoft/Foundry-Local) - Kod źródłowy i oficjalne przykłady
- [Azure AI Foundry Dokumentacja](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/) - Kompletny przewodnik instalacji i użytkowania
- [Seria Model Mondays](https://aka.ms/model-mondays) - Cotygodniowe prezentacje modeli i tutoriale

**Społeczność i wsparcie:**
- [Dyskusje Foundry Local](https://github.com/microsoft/Foundry-Local/discussions) - Pytania i odpowiedzi społeczności oraz propozycje funkcji
- [Społeczność Microsoft AI Developer](https://techcommunity.microsoft.com/category/artificialintelligence) - Najnowsze wiadomości i najlepsze praktyki

## Efekty nauki

Po ukończeniu tego modułu będziesz potrafił:

### Mistrzostwo techniczne
- **Wdrażać i zarządzać**: instalacjami Foundry Local w środowiskach deweloperskich i produkcyjnych
- **Integrować modele**: bezproblemowo pracować z różnymi rodzinami modeli od Microsoft, Hugging Face oraz źródeł społecznościowych
- **Tworzyć aplikacje**: budować produkcyjne aplikacje AI z zaawansowanymi funkcjami i optymalizacjami
- **Rozwijać agentów**: implementować zaawansowanych agentów AI z podstawą, rozumowaniem i integracją narzędzi

### Zrozumienie strategiczne
- **Decyzje architektoniczne**: podejmować świadome decyzje między wdrożeniem lokalnym a w chmurze
- **Optymalizacja wydajności**: optymalizować wydajność inferencji na różnych konfiguracjach sprzętowych
- **Skalowanie korporacyjne**: projektować aplikacje skalujące się od prototypów lokalnych do wdrożeń korporacyjnych
- **Prywatność i bezpieczeństwo**: wdrażać rozwiązania AI chroniące prywatność z lokalną inferencją

### Możliwości innowacji
- **Szybkie prototypowanie**: szybko budować i testować koncepcje aplikacji AI we wszystkich 10 wzorcach przykładowych
- **Integracja społecznościowa**: wykorzystywać modele open source i wnosić wkład do ekosystemu
- **Zaawansowane wzorce**: implementować nowoczesne wzorce AI w tym RAG, agentów i integrację narzędzi
- **Mistrzostwo frameworków**: integracja na poziomie eksperckim z LangChain, Semantic Kernel, Chainlit i Electron
- **Wdrożenia produkcyjne**: wdrażać skalowalne rozwiązania AI od prototypów lokalnych po systemy korporacyjne
- **Przygotowanie na przyszłość**: tworzyć aplikacje gotowe na nowatorskie technologie i wzorce AI

## Pierwsze kroki

1. **Konfiguracja środowiska**: zapewnij Windows 11 z zalecanymi parametrami sprzętowymi (patrz Wymagania wstępne)
2. **Instalacja Foundry Local**: postępuj zgodnie z sesją 1 w celu kompletnej instalacji i konfiguracji
3. **Uruchomienie przykładu 01**: zacznij od podstawowej integracji REST API, aby zweryfikować konfigurację
4. **Przejdź przez przykłady**: ukończ przykłady 01-10 dla pełnej biegłości

## Metryki sukcesu

Śledź swój postęp przez wszystkie 10 kompleksowych przykładów:

### Poziom podstawowy (przykłady 01-03)
- [ ] Pomyślnie zainstaluj i skonfiguruj Foundry Local
- [ ] Ukończ integrację REST API (Przykład 01)
- [ ] Wdroż kompatybilność z OpenAI SDK (Przykład 02)
- [ ] Wykonaj odkrywanie i benchmarking modeli (Przykład 03)

### Poziom aplikacji (przykłady 04-06)
- [ ] Wdróż i uruchom co najmniej 4 różne rodziny modeli
- [ ] Zbuduj funkcjonalną aplikację czatu RAG (Przykład 04)
- [ ] Stwórz system orkiestracji multi-agentów (Przykład 05)
- [ ] Implementuj inteligentne trasowanie modeli (Przykład 06)

### Poziom zaawansowanej integracji (przykłady 07-10)
- [ ] Zbuduj produkcyjnego klienta API (Przykład 07)
- [ ] Opracuj natywną aplikację czatu Windows 11 (Przykład 08)
- [ ] Implementuj zaawansowany system multi-agent (Przykład 09)
- [ ] Stwórz kompleksowy framework narzędzi (Przykład 10)

### Wskaźniki biegłości
- [ ] Pomyślnie uruchom wszystkie 10 przykładów bez błędów
- [ ] Dostosuj co najmniej 3 przykłady do konkretnych przypadków użycia
- [ ] Wdróż 2+ przykłady w środowiskach zbliżonych do produkcyjnych
- [ ] Wnieś ulepszenia lub rozszerzenia do kodu przykładowego
- [ ] Zintegruj wzorce Foundry Local w projektach osobistych/zawodowych

## Szybki start - wszystkie 10 przykładów

### Konfiguracja środowiska (wymagana dla wszystkich przykładów)

```powershell
# 1. Sklonuj i przejdź do Module08
cd Module08

# 2. Utwórz wirtualne środowisko Pythona
py -m venv .venv
.\.venv\Scripts\activate

# 3. Zainstaluj podstawowe zależności
pip install -r requirements.txt

# 4. Zainstaluj Foundry Local (jeśli nie jest już zainstalowany)
winget install Microsoft.FoundryLocal

# 5. Zweryfikuj instalację Foundry Local
foundry --version
foundry model list
```

### Przykłady podstawowe (01-06)

**Przykład 01: Szybki start z REST Chat**
```powershell
# Uruchom lokalną usługę Foundry
foundry model run phi-4-mini

# Uruchom demonstrację czatu REST
python samples/01/chat_quickstart.py
```

**Przykład 02: Integracja OpenAI SDK**
```powershell
# Upewnij się, że model działa
foundry status

# Uruchom demo SDK
python samples/02/sdk_quickstart.py
```

**Przykład 03: Odkrywanie i benchmarking modeli**
```powershell
# Uruchom kompleksowe testowanie modelu
samples/03/list_and_bench.cmd

# Lub uruchom poszczególne komponenty
foundry model list --available
foundry model download qwen2.5-0.5b
foundry model benchmark phi-4-mini
```

**Przykład 04: Aplikacja Chainlit RAG**
```powershell
# Zainstaluj zależności Chainlit
pip install chainlit langchain chromadb

# Uruchom aplikację czatu RAG
chainlit run samples/04/app.py -w
# Otwiera przeglądarkę pod adresem http://localhost:8000
```

**Przykład 05: Orkiestracja multi-agent**
```powershell
# Uruchom demonstrację koordynatora agenta
python -m samples.05.agents.coordinator

# Uruchom przykłady konkretnych agentów
python samples/05/examples/specialists_demo.py
```

**Przykład 06: Router Modele-jako-narzędzia**
```powershell
# Skonfiguruj środowisko
set BASE_URL=http://localhost:8000
set GENERAL_MODEL=phi-4-mini
set CODE_MODEL=qwen2.5-7b

# Uruchom inteligentny router
python samples/06/router.py "Analyze this Python code for performance issues"
```

### Przykłady zaawansowanej integracji (07-10)

**Przykład 07: Bezpośredni klient API**
```powershell
# Przejdź do katalogu przykładowego
cd samples/07

# Zainstaluj dodatkowe zależności
pip install -r requirements.txt

# Uruchom podstawowe przykłady API
python examples/basic_usage.py

# Wypróbuj odpowiedzi strumieniowe
python examples/streaming.py

# Przetestuj wzorce produkcyjne
python examples/production.py
```

**Przykład 08: Aplikacja czatu Windows 11**
```powershell
# Przejdź do katalogu przykładowego
cd samples/08

# Zainstaluj zależności Node.js
npm install

# Uruchom aplikację Electron
npm start

# Lub zbuduj wersję produkcyjną
npm run build
```

**Przykład 09: Zaawansowany system multi-agent**
```powershell
# Przejdź do katalogu przykładowego
cd samples/09

# Zainstaluj zależności systemowe agenta
pip install -r requirements.txt

# Uruchom podstawowy przykład koordynacji
python examples/basic_coordination.py

# Spróbuj skomplikowanego przepływu pracy
python examples/complex_workflow.py

# Interaktywna demonstracja agenta
python examples/interactive_demo.py
```

**Przykład 10: Framework narzędzi Foundry**
```powershell
# Przejdź do katalogu przykładowego
cd samples/10

# Zainstaluj zależności frameworka
pip install -r requirements.txt

# Uruchom demonstrację podstawowych narzędzi
python examples/basic_tools.py

# Uruchom serwer REST API
python examples/rest_api_server.py
# API dostępne pod http://localhost:8080

# Wypróbuj aplikację CLI
python examples/cli_application.py --help

# Uruchom notatnik Jupyter
jupyter notebook examples/jupyter_notebook.ipynb

# Przetestuj integrację LangChain
python examples/langchain_demo.py
```

### Rozwiązywanie typowych problemów

**Błędy połączenia Foundry Local**
```powershell
# Sprawdź status usługi
foundry status

# Uruchom ponownie, jeśli to konieczne
foundry restart

# Zweryfikuj dostępność punktu końcowego
curl http://localhost:5273/v1/models
```

**Problemy z ładowaniem modeli**
```powershell
# Sprawdź dostępne modele
foundry model list --cached

# Pobierz brakujące modele
foundry model download phi-4-mini
foundry model download qwen2.5-0.5b

# Wymuś ponowne załadowanie w razie potrzeby
foundry model unload --all
foundry model run phi-4-mini
```

**Problemy z zależnościami**
```powershell
# Uaktualnij pip i ponownie zainstaluj
python -m pip install --upgrade pip
pip install -r requirements.txt --force-reinstall

# Dla przykładów Node.js
npm cache clean --force
npm install
```

## Podsumowanie


Ten moduł reprezentuje najnowocześniejszy rozwój edge AI, łącząc narzędzia klasy korporacyjnej Microsoft z elastycznością i innowacyjnością ekosystemu open-source. Opanowując Foundry Local poprzez wszystkie 10 kompleksowych przykładów, znajdziesz się na czele rozwoju aplikacji AI.

**Kompletny ścieżka nauki:**
- **Podstawy** (Przykłady 01-03): integracja API i zarządzanie modelami
- **Aplikacje** (Przykłady 04-06): RAG, agenci i inteligentne trasowanie 
- **Zaawansowane** (Przykłady 07-10): ramy produkcyjne i integracja korporacyjna

W przypadku integracji Azure OpenAI (Sesja 2) zobacz pliki README poszczególnych przykładów, aby poznać wymagane zmienne środowiskowe i ustawienia wersji API.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Choć dążymy do dokładności, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub niedokładności. Oryginalny dokument w jego języku źródłowym należy uznawać za autorytatywne źródło. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
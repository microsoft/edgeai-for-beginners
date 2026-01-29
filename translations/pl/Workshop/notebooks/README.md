# Notatniki Warsztatowe

> **Interaktywne notatniki Jupyter do praktycznej nauki Edge AI**
>
> Stopniowe, samodzielne samouczki, które rozwijają się od podstawowych uzupełnień czatu do zaawansowanych systemów wieloagentowych, wykorzystując Microsoft Foundry Local i Small Language Models.

---

## 📖 Wprowadzenie

Witamy w kolekcji **EdgeAI dla Początkujących - Notatniki Warsztatowe**. Te interaktywne notatniki Jupyter oferują praktyczne doświadczenie w nauce, gdzie będziesz pisać, uruchamiać i eksperymentować z kodem Edge AI w czasie rzeczywistym.

### Dlaczego notatniki Jupyter?

W przeciwieństwie do tradycyjnych samouczków, te notatniki oferują:

- **Interaktywną naukę**: Uruchamiaj komórki kodu i natychmiast zobacz wyniki  
- **Eksperymentowanie**: Modyfikuj parametry i obserwuj zmiany w czasie rzeczywistym  
- **Dokumentację**: Wyjaśnienia wbudowane w komórki markdown prowadzą Cię przez koncepcje  
- **Reprodukowalność**: Kompletny działający kod, który możesz wykorzystać ponownie  
- **Wizualizację**: Wyświetlaj metryki wydajności, osadzenia i wyniki bezpośrednio w notatniku  

### Co wyróżnia te notatniki?

Każdy notatnik został zaprojektowany zgodnie z **najlepszymi praktykami produkcyjnymi**:

✅ **Kompleksowa obsługa błędów** - Łagodne degradacje i informacyjne komunikaty o błędach  
✅ **Podpowiedzi typów i dokumentacja** - Jasne sygnatury funkcji i docstringi  
✅ **Monitorowanie wydajności** - Śledzenie użycia tokenów i pomiary opóźnień  
✅ **Modularny design** - Wzorce wielokrotnego użytku, które możesz dostosować do swoich projektów  
✅ **Stopniowa złożoność** - Systematyczne budowanie na podstawie poprzednich sesji  

---

## 🎯 Cele nauki

### Kluczowe umiejętności, które rozwiniesz

Pracując z tymi notatnikami, opanujesz:

1. **Zarządzanie lokalnymi usługami AI**
   - Konfiguracja i zarządzanie usługami Microsoft Foundry Local  
   - Wybór i ładowanie odpowiednich modeli dla Twojego sprzętu  
   - Monitorowanie wykorzystania zasobów i optymalizacja wydajności  
   - Obsługa wykrywania usług i sprawdzania ich stanu  

2. **Tworzenie aplikacji AI**
   - Implementacja lokalnych uzupełnień czatu zgodnych z OpenAI  
   - Budowanie interfejsów strumieniowych dla lepszego doświadczenia użytkownika  
   - Projektowanie skutecznych promptów dla Small Language Models  
   - Integracja lokalnych modeli z aplikacjami  

3. **Generacja wspomagana wyszukiwaniem (RAG)**
   - Tworzenie wyszukiwania semantycznego z osadzeniami wektorowymi  
   - Ugruntowanie odpowiedzi LLM w dokumentach specyficznych dla domeny  
   - Ocena jakości RAG za pomocą metryk RAGAS  
   - Skalowanie od prototypu do produkcji  

4. **Optymalizacja wydajności**
   - Systematyczne porównywanie wielu modeli  
   - Pomiar opóźnień, przepustowości i czasu pierwszego tokena  
   - Porównanie Small Language Models z Large Language Models  
   - Wybór optymalnych modeli na podstawie kompromisów wydajności/jakości  

5. **Orkiestracja wieloagentowa**
   - Projektowanie wyspecjalizowanych agentów do różnych zadań  
   - Implementacja pamięci agentów i zarządzania kontekstem  
   - Koordynacja wielu agentów w złożonych przepływach pracy  
   - Budowanie wzorców koordynatorów dla współpracy agentów  

6. **Inteligentne kierowanie modelami**
   - Implementacja wykrywania intencji i dopasowywania wzorców  
   - Automatyczne kierowanie zapytań do odpowiednich modeli  
   - Budowanie wieloetapowych pipeline'ów (plan → wykonanie → poprawa)  
   - Projektowanie skalowalnych architektur model-as-tools  

---

## 🎓 Efekty nauki

### Co zbudujesz

| Notatnik | Rezultat | Demonstrowane umiejętności | Trudność |
|----------|----------|---------------------------|----------|
| **Sesja 01** | Aplikacja czatu ze strumieniowaniem | Konfiguracja usług, podstawowe uzupełnienia, UX strumieniowy | ⭐ Początkujący |
| **Sesja 02 (RAG)** | Pipeline RAG z oceną | Osadzenia, wyszukiwanie semantyczne, metryki jakości | ⭐⭐ Średniozaawansowany |
| **Sesja 02 (Eval)** | Ocena jakości RAG | Metryki RAGAS, systematyczna ocena | ⭐⭐ Średniozaawansowany |
| **Sesja 03** | Benchmark wielu modeli | Pomiar wydajności, porównanie modeli | ⭐⭐ Średniozaawansowany |
| **Sesja 04** | Porównanie SLM vs LLM | Analiza kompromisów, strategie optymalizacji | ⭐⭐⭐ Zaawansowany |
| **Sesja 05** | Orkiestrator wieloagentowy | Projektowanie agentów, pamięć, koordynacja | ⭐⭐⭐ Zaawansowany |
| **Sesja 06 (Router)** | Inteligentny system kierowania | Wykrywanie intencji, wybór modelu | ⭐⭐⭐ Zaawansowany |
| **Sesja 06 (Pipeline)** | Wieloetapowy pipeline | Przepływy plan/wykonanie/poprawa | ⭐⭐⭐ Zaawansowany |

### Postęp kompetencji

```
Session 01 ────► Session 02 ────► Session 03 ────► Session 04 ────► Session 05-06
   Basic            RAG             Benchmarking      Comparison      Multi-Agent
   Chat             Systems         & Performance     & Optimization  Orchestration
   
Foundation    │   Intermediate   │   Advanced       │   Expert
──────────────┴──────────────────┴──────────────────┴──────────────►
```

---

## 📅 Harmonogram warsztatów

### 🚀 Warsztat półdniowy (3,5 godziny)

**Idealny dla: Szkolenia zespołowe, hackathony, warsztaty konferencyjne**

| Czas | Czas trwania | Sesja | Tematy | Aktywności |
|------|--------------|-------|--------|------------|
| **0:00** | 30 min | Konfiguracja i wprowadzenie | Konfiguracja środowiska, instalacja Foundry Local | Instalacja zależności, weryfikacja konfiguracji |
| **0:30** | 30 min | Sesja 01 | Podstawowe uzupełnienia czatu, strumieniowanie | Uruchamianie notatnika, modyfikacja promptów |
| **1:00** | 45 min | Sesja 02 | Pipeline RAG, osadzenia, ocena | Budowanie systemu RAG, testowanie zapytań |
| **1:45** | 15 min | Przerwa | ☕ Kawa i pytania | — |
| **2:00** | 30 min | Sesja 03 | Benchmarkowanie wielu modeli | Porównanie 3+ modeli |
| **2:30** | 30 min | Sesja 04 | Kompromisy SLM vs LLM | Analiza wydajności/jakości |
| **3:00** | 30 min | Sesja 05-06 | Systemy wieloagentowe i kierowanie | Eksploracja zaawansowanych wzorców |

**Rezultat**: Uczestnicy opuszczają warsztat z 6 działającymi aplikacjami Edge AI i wzorcami kodu gotowymi do produkcji.

---

### 🎓 Warsztat całodniowy (6 godzin)

**Idealny dla: Dogłębne szkolenia, bootcampy, kursy uniwersyteckie**

| Czas | Czas trwania | Sesja | Tematy | Aktywności |
|------|--------------|-------|--------|------------|
| **0:00** | 45 min | Konfiguracja i teoria | Konfiguracja środowiska, podstawy Edge AI | Instalacja, weryfikacja, dyskusja o przypadkach użycia |
| **0:45** | 45 min | Sesja 01 | Szczegółowe uzupełnienia czatu | Implementacja podstawowych i strumieniowych czatów |
| **1:30** | 30 min | Przerwa | ☕ Kawa i networking | — |
| **2:00** | 60 min | Sesja 02 (obie) | Pipeline RAG + ocena RAGAS | Budowanie kompletnego systemu RAG |
| **3:00** | 30 min | Laboratorium praktyczne 1 | Własny RAG dla Twojej domeny | Zastosowanie do własnych dokumentów |
| **3:30** | 30 min | Lunch | 🍽️ | — |
| **4:00** | 45 min | Sesja 03 | Metodologia benchmarkowania | Systematyczne porównanie modeli |
| **4:45** | 45 min | Sesja 04 | Strategie optymalizacji | Analiza SLM vs LLM |
| **5:30** | 60 min | Sesja 05-06 | Zaawansowana orkiestracja | Systemy wieloagentowe, kierowanie |
| **6:30** | 30 min | Laboratorium praktyczne 2 | Budowanie własnego systemu agentów | Projektowanie własnego orkiestratora |

**Rezultat**: Dogłębne zrozumienie wzorców Edge AI oraz 2 projekty własne.

---

### 📚 Nauka we własnym tempie (2 tygodnie)

**Idealna dla: Indywidualnych uczniów, kursów online, samodzielnej nauki**

#### Tydzień 1: Podstawy (6 godzin)

| Dzień | Temat | Czas trwania | Notatniki | Zadanie domowe |
|-------|-------|--------------|-----------|----------------|
| **Pon** | Konfiguracja i podstawy | 1,5 godz. | Sesja 01 | Modyfikacja promptów, testowanie strumieniowania |
| **Śr** | Podstawy RAG | 2 godz. | Sesja 02 (obie) | Dodanie własnych dokumentów |
| **Pt** | Benchmarking | 1,5 godz. | Sesja 03 | Porównanie dodatkowych modeli |
| **Sob** | Przegląd i praktyka | 1 godz. | Wszystkie z tygodnia 1 | Ukończenie ćwiczeń, debugowanie |

#### Tydzień 2: Zaawansowane (5 godzin)

| Dzień | Temat | Czas trwania | Notatniki | Zadanie domowe |
|-------|-------|--------------|-----------|----------------|
| **Pon** | Optymalizacja | 1,5 godz. | Sesja 04 | Dokumentowanie kompromisów |
| **Śr** | Systemy wieloagentowe | 2 godz. | Sesja 05 | Projektowanie własnych agentów |
| **Pt** | Inteligentne kierowanie | 1,5 godz. | Sesja 06 (obie) | Budowanie logiki kierowania |
| **Sob** | Projekt końcowy | 2 godz. | Integracja | Łączenie wielu wzorców |

**Rezultat**: Opanowanie wzorców Edge AI oraz projekt do portfolio.

---

## 📔 Opisy notatników

### 📘 Sesja 01: Podstawy czatu
**Plik**: `session01_chat_bootstrap.ipynb`  
**Czas trwania**: 20-30 minut  
**Wymagania wstępne**: Brak  
**Trudność**: ⭐ Początkujący

**Czego się nauczysz**:
- Instalacja i konfiguracja Foundry Local Python SDK  
- Użycie `FoundryLocalManager` do automatycznego wykrywania usług  
- Implementacja podstawowych uzupełnień czatu zgodnych z API OpenAI  
- Budowanie odpowiedzi strumieniowych dla lepszego doświadczenia użytkownika  
- Obsługa błędów i niedostępności usług  

**Kluczowe koncepcje**: Zarządzanie usługami, uzupełnienia czatu, strumieniowanie, obsługa błędów  

**Co zbudujesz**: Interaktywna aplikacja czatu ze wsparciem strumieniowym  

---

### 📗 Sesja 02: Pipeline RAG
**Plik**: `session02_rag_pipeline.ipynb`  
**Czas trwania**: 30-45 minut  
**Wymagania wstępne**: Sesja 01  
**Trudność**: ⭐⭐ Średniozaawansowany

**Czego się nauczysz**:
- Implementacja wzorca Retrieval Augmented Generation (RAG)  
- Tworzenie osadzeń wektorowych za pomocą sentence-transformers  
- Budowanie wyszukiwania semantycznego z podobieństwem cosinusowym  
- Ugruntowanie odpowiedzi LLM w dokumentach domenowych  
- Obsługa opcjonalnych zależności za pomocą import guards  

**Kluczowe koncepcje**: Architektura RAG, osadzenia, wyszukiwanie semantyczne, podobieństwo wektorowe  

**Co zbudujesz**: System pytań i odpowiedzi oparty na dokumentach  

---

### 📗 Sesja 02: Ocena RAG z RAGAS
**Plik**: `session02_rag_eval_ragas.ipynb`  
**Czas trwania**: 30-45 minut  
**Wymagania wstępne**: Pipeline RAG z Sesji 02  
**Trudność**: ⭐⭐ Średniozaawansowany

**Czego się nauczysz**:
- Ocena jakości RAG za pomocą standardowych metryk branżowych  
- Pomiar trafności kontekstu, trafności odpowiedzi, wierności  
- Użycie frameworka RAGAS do systematycznej oceny  
- Identyfikacja i naprawa problemów jakości RAG  
- Tworzenie zestawów danych oceny dla swojej domeny  

**Kluczowe koncepcje**: Ocena RAG, metryki RAGAS, pomiar jakości, testowanie systematyczne  

**Co zbudujesz**: Framework oceny jakości RAG  

---

### 📙 Sesja 03: Benchmark modeli OSS
**Plik**: `session03_benchmark_oss_models.ipynb`  
**Czas trwania**: 30-45 minut  
**Wymagania wstępne**: Sesja 01  
**Trudność**: ⭐⭐ Średniozaawansowany

**Czego się nauczysz**:
- Systematyczne benchmarkowanie wielu modeli  
- Pomiar opóźnień, przepustowości, czasu pierwszego tokena  
- Implementacja łagodnej degradacji w przypadku awarii modeli  
- Porównanie wydajności w różnych rodzinach modeli  
- Wizualizacja i analiza wyników benchmarków  

**Kluczowe koncepcje**: Benchmarking wydajności, pomiar opóźnień, porównanie modeli, analiza statystyczna  

**Co zbudujesz**: Suite benchmarkowania wielu modeli  

---

### 📙 Sesja 04: Porównanie modeli (SLM vs LLM)
**Plik**: `session04_model_compare.ipynb`  
**Czas trwania**: 30-45 minut  
**Wymagania wstępne**: Sesje 01, 03  
**Trudność**: ⭐⭐⭐ Zaawansowany

**Czego się nauczysz**:
- Porównanie Small Language Models z Large Language Models  
- Analiza kompromisów wydajności vs jakości  
- Pomiar metryk przydatności na krawędzi  
- Wybór optymalnych modeli dla ograniczeń wdrożeniowych  
- Dokumentowanie kryteriów decyzji dotyczących wyboru modelu  

**Kluczowe koncepcje**: Wybór modelu, analiza kompromisów, strategie optymalizacji, planowanie wdrożenia  

**Co zbudujesz**: Framework porównania SLM vs LLM  

---

### 📕 Sesja 05: Orkiestrator wieloagentowy
**Plik**: `session05_agents_orchestrator.ipynb`  
**Czas trwania**: 45-60 minut  
**Wymagania wstępne**: Sesje 01-02  
**Trudność**: ⭐⭐⭐ Zaawansowany

**Czego się nauczysz**:
- Projektowanie wyspecjalizowanych agentów do różnych zadań  
- Implementacja pamięci agentów i zarządzania kontekstem  
- Budowanie wzorców koordynatorów dla współpracy agentów  
- Obsługa komunikacji między agentami i przekazywania zadań  
- Monitorowanie wydajności systemu wieloagentowego  

**Kluczowe koncepcje**: Architektura agentów, wzorce koordynatorów, zarządzanie pamięcią, orkiestracja agentów  

**Co zbudujesz**: System wieloagentowy z koordynatorem i specjalistami  

---

### 📕 Sesja 06: Router modeli
**Plik**: `session06_models_router.ipynb`  
**Czas trwania**: 30-45 minut  
**Wymagania wstępne**: Sesje 01, 03  
**Trudność**: ⭐⭐⭐ Zaawansowany

**Czego się nauczysz**:
- Implementacja wykrywania intencji i dopasowywania wzorców  
- Budowanie kierowania modeli opartego na słowach kluczowych  
- Automatyczne kierowanie zapytań do odpowiednich modeli  
- Konfiguracja rejestrów wielu modeli  
- Monitorowanie decyzji kierowania i wydajności  

**Kluczowe koncepcje**: Wykrywanie intencji, kierowanie modelami, dopasowywanie wzorców, intelig
- Projektowanie skalowalnych architektur model-as-tools

**Kluczowe pojęcia**: Architektura pipeline, przetwarzanie wieloetapowe, odzyskiwanie błędów, wzorce skalowalności

**Co zbudujesz**: Wieloetapowy inteligentny pipeline z routingiem

---

## 🚀 Pierwsze kroki

### Wymagania wstępne

**Wymagania systemowe**:
- **System operacyjny**: Windows 10/11, macOS 11+ lub Linux (Ubuntu 20.04+)
- **RAM**: Minimum 8GB, zalecane 16GB+
- **Dysk**: Co najmniej 10GB wolnego miejsca na modele
- **Sprzęt**: CPU z AVX2; GPU (CUDA, Qualcomm NPU) opcjonalnie

**Wymagania dotyczące oprogramowania**:
- **Python 3.8+** z pip
- **Jupyter Notebook** lub **VS Code** z rozszerzeniem Jupyter
- **Microsoft Foundry Local** zainstalowany i skonfigurowany
- **Git** (do klonowania repozytorium)

### Kroki instalacji

#### 1. Zainstaluj Foundry Local

**Windows**:
```cmd
winget install Microsoft.FoundryLocal
```

**macOS**:
```bash
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**Weryfikacja instalacji**:
```bash
foundry --version
```

#### 2. Skonfiguruj środowisko Python

```bash
# Navigate to Workshop directory
cd Workshop

# Create virtual environment
python -m venv .venv

# Activate virtual environment
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

#### 3. Uruchom Foundry Local

```bash
# Load a model (auto-downloads if needed)
foundry model run phi-4-mini

# Verify service is running
foundry service status
```

#### 4. Uruchom Jupyter

```bash
# Start Jupyter Notebook
jupyter notebook notebooks/

# Or use VS Code with Jupyter extension
code notebooks/
```

### Szybka weryfikacja

Uruchom poniższy kod w komórce Pythona, aby zweryfikować konfigurację:

```python
from foundry_local import FoundryLocalManager
import openai

# Initialize manager (auto-discovers service)
manager = FoundryLocalManager("phi-4-mini")

# Configure OpenAI client
client = openai.OpenAI(
    base_url=manager.endpoint,
    api_key=manager.api_key
)

# Test chat completion
response = client.chat.completions.create(
    model=manager.get_model_info("phi-4-mini").id,
    messages=[{"role": "user", "content": "Hello!"}]
)

print(response.choices[0].message.content)
```

**Oczekiwany wynik**: Powitanie od lokalnego modelu.

---

## 📝 Najlepsze praktyki warsztatowe

### Dla prowadzących

**Przed warsztatem**:
- ✅ Wyślij instrukcje instalacji tydzień wcześniej
- ✅ Przetestuj wszystkie notatniki na docelowym sprzęcie
- ✅ Przygotuj przewodnik rozwiązywania typowych problemów
- ✅ Miej gotowe modele zapasowe (phi-3.5-mini, jeśli phi-4-mini zawiedzie)
- ✅ Utwórz wspólny kanał czatu na pytania

**Podczas warsztatu**:
- ✅ Rozpocznij od szybkiej weryfikacji środowiska (5 minut)
- ✅ Udostępniaj zasoby do rozwiązywania problemów natychmiast
- ✅ Zachęcaj do eksperymentowania i modyfikacji
- ✅ Planuj przerwy strategicznie (po każdych 2 sesjach)
- ✅ Miej asystentów dostępnych do pomocy 1-na-1

**Po warsztacie**:
- ✅ Udostępnij kompletne działające notatniki i rozwiązania
- ✅ Podaj linki do dodatkowych zasobów
- ✅ Stwórz ankietę z opiniami dla ulepszeń
- ✅ Zaproponuj godziny konsultacji na pytania uzupełniające

### Dla uczestników

**Maksymalizuj naukę**:
- ✅ Ukończ konfigurację przed rozpoczęciem warsztatu
- ✅ Uruchamiaj każdą komórkę kodu samodzielnie (nie tylko czytaj)
- ✅ Eksperymentuj z parametrami i promptami
- ✅ Rób notatki z wniosków i trudności
- ✅ Zadawaj pytania, gdy utkniesz (inni mogą mieć podobne pytania)

**Typowe błędy do uniknięcia**:
- ❌ Pomijanie kolejności wykonywania komórek (uruchamiaj sekwencyjnie)
- ❌ Nieczytanie komunikatów o błędach
- ❌ Pośpiech bez zrozumienia
- ❌ Ignorowanie wyjaśnień w markdown
- ❌ Nie zapisywanie zmodyfikowanych notatników

**Porady dotyczące debugowania**:
1. **Usługa nie działa**: Sprawdź `foundry service status`
2. **Błędy importu**: Upewnij się, że aktywowane jest wirtualne środowisko
3. **Model nie znaleziony**: Uruchom `foundry model ls`, aby wyświetlić załadowane modele
4. **Wolne działanie**: Sprawdź użycie RAM, zamknij inne aplikacje
5. **Nieoczekiwane wyniki**: Zrestartuj kernel i uruchom wszystkie komórki od góry

---

## 🔗 Dodatkowe zasoby

### Materiały warsztatowe

- **[Główny przewodnik warsztatowy](../Readme.md)** - Przegląd, cele nauki, wyniki kariery
- **[Przykłady Python](../../../../Workshop/samples)** - Odpowiednie skrypty Python dla każdej sesji
- **[Przewodniki sesji](../../../../Workshop)** - Szczegółowe przewodniki markdown (Sesja01-06)
- **[Skrypty](../../../../Workshop/scripts)** - Narzędzia do walidacji i testowania
- **[Rozwiązywanie problemów](./TROUBLESHOOTING.md)** - Typowe problemy i rozwiązania
- **[Szybki start](./quickstart.md)** - Przewodnik szybkiego startu

### Dokumentacja

- **[Dokumentacja Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)** - Oficjalna dokumentacja Microsoft
- **[OpenAI Python SDK](https://github.com/openai/openai-python)** - Referencja SDK OpenAI
- **[Sentence Transformers](https://www.sbert.net/)** - Dokumentacja modeli embedding
- **[RAGAS Framework](https://docs.ragas.io/)** - Metryki oceny RAG

### Społeczność

- **[Dyskusje na GitHub](https://github.com/microsoft/edgeai-for-beginners/discussions)** - Zadawaj pytania, dziel się projektami
- **[Discord Azure AI Foundry](https://discord.com/invite/ByRwuEEgH4)** - Wsparcie społeczności w czasie rzeczywistym
- **[Stack Overflow](https://stackoverflow.com/questions/tagged/foundry-local)** - Pytania techniczne i odpowiedzi

---

## 🎯 Rekomendacje ścieżki nauki

### Ścieżka dla początkujących (zacznij tutaj)

1. **Sesja 01** - Chat Bootstrap
2. **Sesja 02** - Pipeline RAG
3. **Sesja 03** - Benchmark modeli

**Czas**: ~2 godziny | **Skupienie**: Podstawowe wzorce

---

### Ścieżka średniozaawansowana

1. Ukończ ścieżkę dla początkujących
2. **Sesja 02** - Ocena RAG
3. **Sesja 04** - Porównanie modeli

**Czas**: ~4 godziny | **Skupienie**: Jakość i optymalizacja

---

### Ścieżka zaawansowana (pełny warsztat)

1. Ukończ ścieżkę średniozaawansowaną
2. **Sesja 05** - Orkiestrator wieloagentowy
3. **Sesja 06** - Router modeli
4. **Sesja 06** - Pipeline wieloetapowy

**Czas**: ~6 godzin | **Skupienie**: Wzorce produkcyjne

---

### Ścieżka projektu niestandardowego

1. Ukończ ścieżkę dla początkujących (Sesje 01-03)
2. Wybierz JEDNĄ zaawansowaną sesję w zależności od celu:
   - **Budowanie aplikacji RAG?** → Sesja 02 Ocena
   - **Optymalizacja wydajności?** → Sesja 04 Porównanie
   - **Złożone przepływy pracy?** → Sesja 05 Orkiestrator
   - **Skalowalna architektura?** → Sesja 06 Router + Pipeline

**Czas**: ~3 godziny | **Skupienie**: Umiejętności specyficzne dla projektu

---

## 📊 Metryki sukcesu

Śledź postępy za pomocą tych kamieni milowych:

- [ ] **Konfiguracja ukończona** - Foundry Local działa, wszystkie zależności zainstalowane
- [ ] **Pierwszy chat** - Sesja 01 ukończona, działający streaming chat
- [ ] **Zbudowany RAG** - Sesja 02 ukończona, funkcjonalny system QA dokumentów
- [ ] **Benchmark modeli** - Sesja 03 ukończona, zebrane dane wydajności
- [ ] **Analiza kompromisów** - Sesja 04 ukończona, udokumentowane kryteria wyboru modelu
- [ ] **Orkiestracja agentów** - Sesja 05 ukończona, działający system wieloagentowy
- [ ] **Routing zaimplementowany** - Sesja 06 ukończona, funkcjonalny inteligentny wybór modelu
- [ ] **Projekt niestandardowy** - Zastosowanie wzorców warsztatowych do własnego przypadku użycia

---

## 🤝 Współtworzenie

Znalazłeś problem lub masz sugestię? Zapraszamy do współtworzenia!

- **Zgłaszanie problemów**: [GitHub Issues](https://github.com/microsoft/edgeai-for-beginners/issues)
- **Propozycje ulepszeń**: [GitHub Discussions](https://github.com/microsoft/edgeai-for-beginners/discussions)
- **Przesyłanie PR**: Postępuj zgodnie z [Wytycznymi współtworzenia](../../AGENTS.md)

---

## 📄 Licencja

Ten warsztat jest częścią repozytorium [EdgeAI for Beginners](https://github.com/microsoft/edgeai-for-beginners) i jest licencjonowany na podstawie [Licencji MIT](../../../../LICENSE).

---

**Gotowy na budowanie aplikacji Edge AI gotowych do produkcji?**  
**Rozpocznij od [Sesji 01: Chat Bootstrap](./session01_chat_bootstrap.ipynb) →**

---

*Ostatnia aktualizacja: 8 października 2025 | Wersja warsztatu: 2.0*

---

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dokładamy wszelkich starań, aby tłumaczenie było precyzyjne, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego języku źródłowym powinien być uznawany za autorytatywne źródło. W przypadku informacji o kluczowym znaczeniu zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
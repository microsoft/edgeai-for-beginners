<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "45923ada94573fee7c82cc4f0c3bb344",
  "translation_date": "2025-10-28T21:44:14+00:00",
  "source_file": "Workshop/Readme.md",
  "language_code": "pl"
}
-->
# EdgeAI dla początkujących - Warsztaty

> **Praktyczna ścieżka nauki tworzenia gotowych do produkcji aplikacji Edge AI**
>
> Opanuj wdrażanie lokalnej sztucznej inteligencji z Microsoft Foundry Local, od pierwszego ukończenia czatu po orkiestrację wieloagentową w 6 progresywnych sesjach.

---

## 🎯 Wprowadzenie

Witamy na warsztatach **EdgeAI dla początkujących** - praktycznym przewodniku po tworzeniu inteligentnych aplikacji działających całkowicie na lokalnym sprzęcie. Te warsztaty przekształcają teoretyczne koncepcje Edge AI w umiejętności praktyczne poprzez coraz bardziej wymagające ćwiczenia z użyciem Microsoft Foundry Local i Small Language Models (SLM).

### Dlaczego te warsztaty?

**Rewolucja Edge AI już trwa**

Organizacje na całym świecie przechodzą od AI zależnej od chmury do obliczeń brzegowych z trzech kluczowych powodów:

1. **Prywatność i zgodność** - Przetwarzanie wrażliwych danych lokalnie, bez przesyłania ich do chmury (HIPAA, RODO, regulacje finansowe)
2. **Wydajność** - Eliminacja opóźnień sieciowych (50-500ms lokalnie vs 500-2000ms w chmurze)
3. **Kontrola kosztów** - Brak kosztów API za token i skalowanie bez wydatków na chmurę

**Ale Edge AI jest inne**

Uruchamianie AI na miejscu wymaga nowych umiejętności:
- Wybór i optymalizacja modeli pod kątem ograniczeń zasobów
- Zarządzanie lokalnymi usługami i przyspieszenie sprzętowe
- Inżynieria promptów dla mniejszych modeli
- Wzorce wdrażania produkcyjnego dla urządzeń brzegowych

**Te warsztaty dostarczą tych umiejętności**

W 6 skoncentrowanych sesjach (~3 godziny łącznie) przejdziesz od "Hello World" do wdrożenia gotowych do produkcji systemów wieloagentowych - wszystko działające lokalnie na Twoim komputerze.

---

## 📚 Cele nauki

Po ukończeniu tych warsztatów będziesz w stanie:

### Kluczowe kompetencje
1. **Wdrażanie i zarządzanie lokalnymi usługami AI**
   - Instalacja i konfiguracja Microsoft Foundry Local
   - Wybór odpowiednich modeli do wdrożenia na brzegu
   - Zarządzanie cyklem życia modelu (pobieranie, ładowanie, buforowanie)
   - Monitorowanie wykorzystania zasobów i optymalizacja wydajności

2. **Tworzenie aplikacji zasilanych AI**
   - Implementacja lokalnych uzupełnień czatu zgodnych z OpenAI
   - Projektowanie skutecznych promptów dla Small Language Models
   - Obsługa strumieniowych odpowiedzi dla lepszego UX
   - Integracja lokalnych modeli z istniejącymi aplikacjami

3. **Tworzenie systemów RAG (Retrieval Augmented Generation)**
   - Budowanie wyszukiwania semantycznego z użyciem osadzeń
   - Ugruntowanie odpowiedzi LLM w wiedzy specyficznej dla danej dziedziny
   - Ocena jakości RAG za pomocą standardowych metryk branżowych
   - Skalowanie od prototypu do produkcji

4. **Optymalizacja wydajności modelu**
   - Benchmarking wielu modeli dla Twojego przypadku użycia
   - Pomiar opóźnienia, przepustowości i czasu pierwszego tokena
   - Wybór optymalnych modeli na podstawie kompromisów między szybkością a jakością
   - Porównanie SLM vs LLM w rzeczywistych scenariuszach

5. **Orkiestracja systemów wieloagentowych**
   - Projektowanie wyspecjalizowanych agentów do różnych zadań
   - Implementacja pamięci agentów i zarządzania kontekstem
   - Koordynacja agentów w złożonych przepływach pracy
   - Inteligentne kierowanie żądań między wieloma modelami

6. **Wdrażanie gotowych do produkcji rozwiązań**
   - Implementacja obsługi błędów i logiki ponownego próbowania
   - Monitorowanie użycia tokenów i zasobów systemowych
   - Budowanie skalowalnych architektur z wzorcami model-as-tools
   - Planowanie ścieżek migracji z brzegu do hybrydy (brzeg + chmura)

---

## 🎓 Rezultaty nauki

### Co zbudujesz

Pod koniec tych warsztatów stworzysz:

| Sesja | Rezultat | Demonstrowane umiejętności |
|-------|----------|---------------------------|
| **1** | Aplikacja czatu ze strumieniowaniem | Konfiguracja usług, podstawowe uzupełnienia, UX strumieniowy |
| **2** | System RAG z oceną | Osadzenia, wyszukiwanie semantyczne, metryki jakości |
| **3** | Zestaw benchmarków dla wielu modeli | Pomiar wydajności, porównanie modeli |
| **4** | Porównanie SLM vs LLM | Analiza kompromisów, strategie optymalizacji |
| **5** | Orkiestrator wieloagentowy | Projektowanie agentów, zarządzanie pamięcią, koordynacja |
| **6** | Inteligentny system routingu | Wykrywanie intencji, wybór modelu, skalowalność |

### Matryca kompetencji

| Poziom umiejętności | Sesja 1-2 | Sesja 3-4 | Sesja 5-6 |
|---------------------|-----------|-----------|-----------|
| **Początkujący** | ✅ Konfiguracja i podstawy | ⚠️ Wymagające | ❌ Zbyt zaawansowane |
| **Średniozaawansowany** | ✅ Szybki przegląd | ✅ Kluczowe umiejętności | ⚠️ Cele rozwojowe |
| **Zaawansowany** | ✅ Bez problemu | ✅ Doskonalenie | ✅ Wzorce produkcyjne |

### Umiejętności gotowe do kariery

**Po tych warsztatach będziesz gotowy do:**

✅ **Tworzenia aplikacji z priorytetem prywatności**
- Aplikacje medyczne obsługujące PHI/PII lokalnie
- Usługi finansowe spełniające wymagania zgodności
- Systemy rządowe z wymogami suwerenności danych

✅ **Optymalizacji dla środowisk brzegowych**
- Urządzenia IoT z ograniczonymi zasobami
- Aplikacje mobilne działające offline
- Systemy czasu rzeczywistego o niskim opóźnieniu

✅ **Projektowania inteligentnych architektur**
- Systemy wieloagentowe dla złożonych przepływów pracy
- Hybrydowe wdrożenia brzeg-chmura
- Kosztowo zoptymalizowana infrastruktura AI

✅ **Prowadzenia inicjatyw Edge AI**
- Ocena wykonalności projektów Edge AI
- Wybór odpowiednich modeli i frameworków
- Projektowanie skalowalnych lokalnych rozwiązań AI

---

## 🗺️ Struktura warsztatów

### Przegląd sesji (6 sesji × 30 minut = 3 godziny)

| Sesja | Temat | Skupienie | Czas trwania |
|-------|-------|-----------|--------------|
| **1** | Pierwsze kroki z Foundry Local | Instalacja, weryfikacja, pierwsze uzupełnienia | 30 min |
| **2** | Tworzenie rozwiązań AI z RAG | Inżynieria promptów, osadzenia, ocena | 30 min |
| **3** | Modele open source | Odkrywanie modeli, benchmarking, wybór | 30 min |
| **4** | Najnowsze modele | SLM vs LLM, optymalizacja, frameworki | 30 min |
| **5** | Agenci zasilani AI | Projektowanie agentów, orkiestracja, pamięć | 30 min |
| **6** | Modele jako narzędzia | Routing, łańcuchy, strategie skalowania | 30 min |

---

## 🚀 Szybki start

### Wymagania wstępne

**Wymagania systemowe:**
- **OS**: Windows 10/11, macOS 11+ lub Linux (Ubuntu 20.04+)
- **RAM**: minimum 8GB, zalecane 16GB+
- **Dysk**: co najmniej 10GB wolnego miejsca na modele
- **CPU**: Nowoczesny procesor z obsługą AVX2
- **GPU** (opcjonalnie): Kompatybilny z CUDA lub Qualcomm NPU dla przyspieszenia

**Wymagania dotyczące oprogramowania:**
- **Python 3.8+** ([Pobierz](https://www.python.org/downloads/))
- **Microsoft Foundry Local** ([Przewodnik instalacji](../../../Workshop))
- **Git** ([Pobierz](https://git-scm.com/downloads))
- **Visual Studio Code** (zalecane) ([Pobierz](https://code.visualstudio.com/))

### Konfiguracja w 3 krokach

#### 1. Zainstaluj Foundry Local

**Windows:**
```powershell
winget install Microsoft.FoundryLocal
```

**macOS:**
```bash
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**Weryfikacja instalacji:**
```bash
foundry --version
foundry service status
```

**Upewnij się, że Azure AI Foundry Local działa na stałym porcie**

```bash
# Set FoundryLocal to use port 58123 (default)
foundry service set --port 58123 --show

# Or use a different port
foundry service set --port 58000 --show
```

**Sprawdź działanie:**
```bash
# Check service status
foundry service status

# Test the endpoint
curl http://127.0.0.1:58123/v1/models
```
**Sprawdzanie dostępnych modeli**
Aby zobaczyć, które modele są dostępne w Twojej instancji Foundry Local, możesz zapytać o endpoint modeli:

```bash
# cmd/bash/powershell
foundry model list
```

Korzystanie z endpointu webowego 

```bash
# Windows PowerShell
powershell -Command "Invoke-RestMethod -Uri 'http://127.0.0.1:58123/v1/models' -Method Get"

# Or using curl (if available)
curl http://127.0.0.1:58123/v1/models
```

#### 2. Sklonuj repozytorium i zainstaluj zależności

```bash
# Clone repository
git clone https://github.com/microsoft/edgeai-for-beginners.git
cd edgeai-for-beginners/Workshop

# Create virtual environment
python -m venv .venv

# Activate virtual environment
# Windows:
.\.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

#### 3. Uruchom pierwszy przykład

```bash
# Start Foundry Local and load a model
foundry model run phi-4-mini

# Run the chat bootstrap sample
cd samples
python -m session01.chat_bootstrap "What is edge AI?"
```

**✅ Sukces!** Powinieneś zobaczyć strumieniową odpowiedź dotyczącą Edge AI.

---

## 📦 Zasoby warsztatowe

### Przykłady w Pythonie

Progresywne ćwiczenia praktyczne demonstrujące każdy koncept:

| Sesja | Przykład | Opis | Czas wykonania |
|-------|----------|------|----------------|
| 1 | [`chat_bootstrap.py`](../../../Workshop/samples/session01/chat_bootstrap.py) | Podstawowy czat i strumieniowanie | ~30s |
| 2 | [`rag_pipeline.py`](../../../Workshop/samples/session02/rag_pipeline.py) | RAG z osadzeniami | ~45s |
| 2 | [`rag_eval_ragas.py`](../../../Workshop/samples/session02/rag_eval_ragas.py) | Ocena jakości RAG | ~60s |
| 3 | [`benchmark_oss_models.py`](../../../Workshop/samples/session03/benchmark_oss_models.py) | Benchmarking wielu modeli | ~2-3m |
| 4 | [`model_compare.py`](../../../Workshop/samples/session04/model_compare.py) | Porównanie SLM vs LLM | ~45s |
| 5 | [`agents_orchestrator.py`](../../../Workshop/samples/session05/agents_orchestrator.py) | System wieloagentowy | ~60s |
| 6 | [`models_router.py`](../../../Workshop/samples/session06/models_router.py) | Routing oparty na intencjach | ~45s |
| 6 | [`models_pipeline.py`](../../../Workshop/samples/session06/models_pipeline.py) | Pipeline wieloetapowy | ~60s |

### Notatniki Jupyter

Interaktywna eksploracja z wyjaśnieniami i wizualizacjami:

| Sesja | Notatnik | Opis | Poziom trudności |
|-------|----------|------|------------------|
| 1 | [`session01_chat_bootstrap.ipynb`](./notebooks/session01_chat_bootstrap.ipynb) | Podstawy czatu i strumieniowanie | ⭐ Początkujący |
| 2 | [`session02_rag_pipeline.ipynb`](./notebooks/session02_rag_pipeline.ipynb) | Budowanie systemu RAG | ⭐⭐ Średniozaawansowany |
| 2 | [`session02_rag_eval_ragas.ipynb`](./notebooks/session02_rag_eval_ragas.ipynb) | Ocena jakości RAG | ⭐⭐ Średniozaawansowany |
| 3 | [`session03_benchmark_oss_models.ipynb`](./notebooks/session03_benchmark_oss_models.ipynb) | Benchmarking modeli | ⭐⭐ Średniozaawansowany |
| 4 | [`session04_model_compare.ipynb`](./notebooks/session04_model_compare.ipynb) | Porównanie modeli | ⭐⭐ Średniozaawansowany |
| 5 | [`session05_agents_orchestrator.ipynb`](./notebooks/session05_agents_orchestrator.ipynb) | Orkiestracja agentów | ⭐⭐⭐ Zaawansowany |
| 6 | [`session06_models_router.ipynb`](./notebooks/session06_models_router.ipynb) | Routing intencji | ⭐⭐⭐ Zaawansowany |
| 6 | [`session06_models_pipeline.ipynb`](./notebooks/session06_models_pipeline.ipynb) | Orkiestracja pipeline | ⭐⭐⭐ Zaawansowany |

### Dokumentacja

Kompleksowe przewodniki i materiały referencyjne:

| Dokument | Opis | Kiedy używać |
|----------|------|-------------|
| [QUICK_START.md](./QUICK_START.md) | Przewodnik szybkiej konfiguracji | Rozpoczynając od zera |
| [QUICK_REFERENCE.md](./QUICK_REFERENCE.md) | Skrócona lista poleceń i API | Potrzebujesz szybkich odpowiedzi |
| [FOUNDRY_SDK_QUICKREF.md](./FOUNDRY_SDK_QUICKREF.md) | Wzorce SDK i przykłady | Pisanie kodu |
| [ENV_CONFIGURATION.md](./ENV_CONFIGURATION.md) | Przewodnik po zmiennych środowiskowych | Konfiguracja przykładów |
| [SAMPLES_UPDATE_SUMMARY.md](./SAMPLES_UPDATE_SUMMARY.md) | Najnowsze ulepszenia przykładów | Zrozumienie zmian |
| [SDK_MIGRATION_NOTES.md](./SDK_MIGRATION_NOTES.md) | Przewodnik migracji | Aktualizacja kodu |
| [notebooks/TROUBLESHOOTING.md](./notebooks/TROUBLESHOOTING.md) | Typowe problemy i ich rozwiązania | Rozwiązywanie problemów |

---

## 🎓 Rekomendacje ścieżki nauki

### Dla początkujących (3-4 godziny)
1. ✅ Sesja 1: Pierwsze kroki (skupienie na konfiguracji i podstawowym czacie)
2. ✅ Sesja 2: Podstawy RAG (na początek pomiń ocenę)
3. ✅ Sesja 3: Prosty benchmarking (tylko 2 modele)
4. ⏭️ Na razie pomiń sesje 4-6
5. 🔄 Wróć do sesji 4-6 po zbudowaniu pierwszej aplikacji

### Dla średniozaawansowanych (3 godziny)
1. ⚡ Sesja 1: Szybka weryfikacja konfiguracji
2. ✅ Sesja 2: Pełny pipeline RAG z oceną
3. ✅ Sesja 3: Pełny zestaw benchmarków
4. ✅ Sesja 4: Optymalizacja modeli
5. ✅ Sesje 5-6: Skupienie na wzorcach architektury

### Dla zaawansowanych (2-3 godziny)
1. ⚡ Sesje 1-3: Szybki przegląd i weryfikacja
2. ✅ Sesja 4: Głębokie zanurzenie w optymalizacji
3. ✅ Sesja 5: Architektura wieloagentowa
4. ✅ Sesja 6: Wzorce produkcyjne i skalowanie
5. 🚀 Rozszerzenie: Budowanie niestandardowej logiki routingu i wdrożeń hybrydowych

---

## Pakiet sesji warsztatowych (Skoncentrowane laboratoria 30‑minutowe)

Jeśli podążasz za skondensowanym formatem warsztatów 6 sesji, skorzystaj z tych dedykowanych przewodników (każdy odpowiada i uzupełnia szersze moduły dokumentacji powyżej):

| Sesja warsztatowa | Przewodnik | Główne skupienie |
|-------------------|------------|------------------|
| 1 | [Session01-GettingStartedFoundryLocal](./Session01-GettingStartedFoundryLocal.md) | Instalacja, weryfikacja, uruchomienie phi & GPT-OSS-20B, przyspieszenie |
| 2 | [Session02-BuildAISolutionsRAG](./Session02-BuildAISolutionsRAG.md) | Inżynieria promptów, wzorce RAG, CSV i ugruntowanie dokumentów, migracja |
| 3 | [Session03-OpenSourceModels](./Session03-OpenSourceModels.md) | Integracja z Hugging Face, benchmarking, wybór modeli |
| 4 | [Session04-CuttingEdgeModels](./Session04-CuttingEdgeModels.md) | SLM vs LLM, WebGPU, Chainlit RAG, przyspieszenie ONNX |
| 5 | [Session05-AIPoweredAgents](./Session05-AIPoweredAgents.md) | Role agentów, pamięć, narzędzia, orkiestracja |
| 6 | [Session06-ModelsAsTools](./Session06-ModelsAsTools.md) | Routing, łączenie, skalowanie w Azure |

Każdy plik sesji zawiera: streszczenie, cele nauki, 30-minutowy przebieg demonstracji, projekt startowy, listę kontrolną walidacji, rozwiązywanie problemów oraz odniesienia do oficjalnego Foundry Local Python SDK.

### Przykładowe skrypty

Instalacja zależności warsztatowych (Windows):

```powershell
cd Workshop
py -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

macOS / Linux:

```bash
cd Workshop
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Jeśli usługa Foundry Local działa na innym komputerze (Windows) lub maszynie wirtualnej niż macOS, wyeksportuj punkt końcowy:

```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```

| Sesja | Skrypt(y) | Opis |
|-------|-----------|------|
| 1 | `samples/session01/chat_bootstrap.py` | Uruchomienie usługi i czat strumieniowy |
| 2 | `samples/session02/rag_pipeline.py` | Minimalny RAG (w pamięci osadzenia) |
|   | `samples/session02/rag_eval_ragas.py` | Ocena RAG za pomocą metryk ragas |
| 3 | `samples/session03/benchmark_oss_models.py` | Benchmarking opóźnienia i przepustowości dla wielu modeli |
| 4 | `samples/session04/model_compare.py` | Porównanie SLM vs LLM (opóźnienie i przykładowe wyniki) |
| 5 | `samples/session05/agents_orchestrator.py` | Pipeline badawczy dwóch agentów → redakcyjny |
| 6 | `samples/session06/models_router.py` | Demonstracja routingu opartego na intencjach |
|   | `samples/session06/models_pipeline.py` | Łańcuch planowania/wykonania/poprawy w wielu krokach |

### Zmienne środowiskowe (wspólne dla wszystkich przykładów)

| Zmienna | Cel | Przykład |
|---------|-----|---------|
| `FOUNDRY_LOCAL_ALIAS` | Domyślny alias pojedynczego modelu dla podstawowych przykładów | `phi-4-mini` |
| `SLM_ALIAS` / `LLM_ALIAS` | Jawne SLM vs większy model do porównania | `phi-4-mini` / `gpt-oss-20b` |
| `BENCH_MODELS` | Lista aliasów do benchmarku | `qwen2.5-0.5b,mistral-7b` |
| `BENCH_ROUNDS` | Powtórzenia benchmarku na model | `3` |
| `BENCH_PROMPT` | Podpowiedź używana w benchmarku | `Explain retrieval augmented generation briefly.` |
| `EMBED_MODEL` | Model osadzenia sentence-transformers | `sentence-transformers/all-MiniLM-L6-v2` |
| `RAG_QUESTION` | Zastąpienie zapytania testowego dla pipeline'u RAG | `Why use RAG with local inference?` |
| `AGENT_QUESTION` | Zastąpienie zapytania dla pipeline'u agentów | `Explain why edge AI matters for compliance.` |
| `AGENT_MODEL_PRIMARY` | Alias modelu dla agenta badawczego | `phi-4-mini` |
| `AGENT_MODEL_EDITOR` | Alias modelu dla agenta redakcyjnego (może się różnić) | `gpt-oss-20b` |
| `SHOW_USAGE` | Gdy `1`, drukuje użycie tokenów na zakończenie | `1` |
| `RETRY_ON_FAIL` | Gdy `1`, ponawia próbę w przypadku przejściowych błędów czatu | `1` |
| `RETRY_BACKOFF` | Czas oczekiwania przed ponowną próbą | `1.0` |

Jeśli zmienna nie jest ustawiona, skrypty domyślnie używają sensownych wartości. W przypadku demonstracji z jednym modelem zazwyczaj wystarczy `FOUNDRY_LOCAL_ALIAS`.

### Moduł pomocniczy

Wszystkie przykłady korzystają teraz z pomocniczego `samples/workshop_utils.py`, który oferuje:

* Buforowaną obsługę `FoundryLocalManager` + tworzenie klienta OpenAI
* Pomocniczą funkcję `chat_once()` z opcjonalnym ponawianiem prób + drukowaniem użycia
* Proste raportowanie użycia tokenów (włączane przez `SHOW_USAGE=1`)

To zmniejsza powielanie kodu i podkreśla najlepsze praktyki efektywnej orkiestracji lokalnych modeli.

## Opcjonalne ulepszenia (między sesjami)

| Temat | Ulepszenie | Sesje | Środowisko / Przełącznik |
|-------|------------|-------|--------------------------|
| Determinizm | Stała temperatura + stabilne zestawy podpowiedzi | 1–6 | Ustaw `temperature=0`, `top_p=1` |
| Widoczność użycia tokenów | Nauka kosztów/efektywności | 1–6 | `SHOW_USAGE=1` |
| Strumieniowy pierwszy token | Metryka postrzeganego opóźnienia | 1,3,4,6 | `BENCH_STREAM=1` (benchmark) |
| Odporność na ponowne próby | Obsługa przejściowych problemów z uruchomieniem | Wszystkie | `RETRY_ON_FAIL=1` + `RETRY_BACKOFF` |
| Wielomodelowi agenci | Specjalizacja ról heterogenicznych | 5 | `AGENT_MODEL_PRIMARY`, `AGENT_MODEL_EDITOR` |
| Adaptacyjny routing | Intencje + heurystyka kosztów | 6 | Rozszerz router o logikę eskalacji |
| Pamięć wektorowa | Długoterminowe przypominanie semantyczne | 2,5,6 | Integracja indeksu osadzeń FAISS/Chroma |
| Eksport śladów | Audyt i ocena | 2,5,6 | Dodaj linie JSON dla każdego kroku |
| Rubryki jakości | Śledzenie jakości | 3–6 | Dodatkowe podpowiedzi oceny |
| Testy wstępne | Szybka walidacja przed warsztatem | Wszystkie | `python Workshop/tests/smoke.py` |

### Deterministyczny szybki start

```powershell
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
python Workshop\tests\smoke.py
```

Oczekuj stabilnej liczby tokenów dla powtarzających się identycznych wejść.

### Ocena RAG (Sesja 2)

Użyj `rag_eval_ragas.py`, aby obliczyć trafność odpowiedzi, wierność i precyzję kontekstu na małym syntetycznym zbiorze danych:

```powershell
cd Workshop/samples
python -m session02.rag_eval_ragas
```

Rozszerz, dostarczając większy JSONL z pytaniami, kontekstami i prawdziwymi odpowiedziami, a następnie konwertując go na `Dataset` Hugging Face.

## Dodatek do dokładności poleceń CLI

Warsztat celowo używa tylko aktualnie udokumentowanych/stabilnych poleceń Foundry Local CLI.

### Odwołania do stabilnych poleceń

| Kategoria | Polecenie | Cel |
|-----------|-----------|-----|
| Podstawowe | `foundry --version` | Wyświetlenie zainstalowanej wersji |
| Podstawowe | `foundry init` | Inicjalizacja konfiguracji |
| Usługa | `foundry service start` | Uruchomienie lokalnej usługi (jeśli nie jest automatyczne) |
| Usługa | `foundry status` | Wyświetlenie statusu usługi |
| Modele | `foundry model list` | Lista katalogu/dostępnych modeli |
| Modele | `foundry model download <alias>` | Pobranie wag modelu do pamięci podręcznej |
| Modele | `foundry model run <alias>` | Uruchomienie (załadowanie) modelu lokalnie; połącz z `--prompt` dla jednorazowego użycia |
| Modele | `foundry model unload <alias>` / `foundry model stop <alias>` | Wyładowanie modelu z pamięci (jeśli obsługiwane) |
| Pamięć podręczna | `foundry cache list` | Lista modeli w pamięci podręcznej |
| System | `foundry system info` | Migawka możliwości sprzętowych i akceleracji |
| System | `foundry system gpu-info` | Informacje diagnostyczne GPU |
| Konfiguracja | `foundry config list` | Wyświetlenie bieżących wartości konfiguracji |
| Konfiguracja | `foundry config set <key> <value>` | Aktualizacja konfiguracji |

### Wzorzec jednorazowej podpowiedzi

Zamiast przestarzałego podpolecenia `model chat`, użyj:

```powershell
foundry model run <alias> --prompt "Your question here"
```

To wykonuje pojedynczy cykl podpowiedzi/odpowiedzi, a następnie kończy działanie.

### Usunięte / unikanie wzorców

| Przestarzałe / Nieudokumentowane | Zastąpienie / Wskazówki |
|----------------------------------|-------------------------|
| `foundry model chat <model> "..."` | `foundry model run <model> --prompt "..."` |
| `foundry model list --running` | Użyj zwykłego `foundry model list` + ostatnia aktywność/logi |
| `foundry model list --cached` | `foundry cache list` |
| `foundry model stats <model>` | Użyj benchmarkowego skryptu Python + narzędzi systemowych (Task Manager / `nvidia-smi`) |
| `foundry model benchmark ...` | `samples/session03/benchmark_oss_models.py` |

### Benchmarking i telemetria

- Opóźnienie, p95, tokeny/sekunda: `samples/session03/benchmark_oss_models.py`
- Opóźnienie pierwszego tokena (strumieniowe): ustaw `BENCH_STREAM=1`
- Użycie zasobów: Monitory systemowe (Task Manager, Activity Monitor, `nvidia-smi`) + `foundry system info`.

Gdy nowe polecenia telemetrii CLI zostaną ustabilizowane, można je łatwo włączyć do markdownów sesji.

### Automatyczna kontrola składni

Automatyczny linter zapobiega ponownemu wprowadzaniu przestarzałych wzorców CLI w blokach kodu w plikach markdown:

Skrypt: `Workshop/scripts/lint_markdown_cli.py`

Przestarzałe wzorce są blokowane w blokach kodu.

Zalecane zamienniki:
| Przestarzałe | Zamiennik |
|--------------|-----------|
| `foundry model chat <a> "..."` | `foundry model run <a> --prompt "..."` |
| `model list --running` | `model list` |
| `model list --cached` | `cache list` |
| `model stats` | Skrypt benchmarkowy + narzędzia systemowe |
| `model benchmark` | `samples/session03/benchmark_oss_models.py` |
| `model list --available` | `model list` |

Uruchom lokalnie:
```powershell
python Workshop\scripts\lint_markdown_cli.py --verbose
```

GitHub Action: `.github/workflows/markdown-cli-lint.yml` uruchamiany przy każdym pushu i PR.

Opcjonalny hook pre-commit:
```bash
echo "python Workshop/scripts/lint_markdown_cli.py" > .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```

## Tabela szybkiej migracji CLI → SDK

| Zadanie | Jednolinijkowe CLI | Równoważnik SDK (Python) | Uwagi |
|---------|--------------------|--------------------------|-------|
| Uruchomienie modelu raz (podpowiedź) | `foundry model run phi-4-mini --prompt "Hello"` | `manager=FoundryLocalManager("phi-4-mini"); client=OpenAI(base_url=manager.endpoint, api_key=manager.api_key or "not-needed"); client.chat.completions.create(model=manager.get_model_info("phi-4-mini").id, messages=[{"role":"user","content":"Hello"}])` | SDK automatycznie uruchamia usługę i buforowanie |
| Pobranie (pamięć podręczna) modelu | `foundry model download qwen2.5-0.5b` | `FoundryLocalManager("qwen2.5-0.5b")  # triggers download/load` | Manager wybiera najlepszy wariant, jeśli alias odnosi się do wielu wersji |
| Lista katalogu | `foundry model list` | `# użyj managera dla każdego aliasu lub utrzymuj znaną listę` | CLI agreguje; SDK obecnie instancjonuje per-alias |
| Lista modeli w pamięci podręcznej | `foundry cache list` | `manager.list_cached_models()` | Po inicjalizacji managera (dowolny alias) |
| Włączenie akceleracji GPU | `foundry config set compute.onnx.enable_gpu true` | `# Akcja CLI; SDK zakłada, że konfiguracja została już zastosowana` | Konfiguracja jest zewnętrznym efektem ubocznym |
| Pobranie URL punktu końcowego | (implicit) | `manager.endpoint` | Używane do tworzenia klienta kompatybilnego z OpenAI |
| Rozgrzanie modelu | `foundry model run <alias>` a następnie pierwsza podpowiedź | `chat_once(alias, messages=[...])` (utility) | Narzędzia obsługują początkowe opóźnienie rozgrzewania |
| Pomiar opóźnienia | `python -m session03.benchmark_oss_models` | `import benchmark_oss_models` (lub nowy skrypt eksportera) | Preferuj skrypt dla spójnych metryk |
| Zatrzymanie/wyładowanie modelu | `foundry model unload <alias>` | (Nie udostępnione – restart usługi/procesu) | Zazwyczaj nie wymagane w przepływie warsztatowym |
| Pobranie użycia tokenów | (zobacz output) | `resp.usage.total_tokens` | Dostarczane, jeśli backend zwraca obiekt użycia |

## Eksport Markdown Benchmark

Użyj skryptu `Workshop/scripts/export_benchmark_markdown.py`, aby uruchomić świeży benchmark (ta sama logika co `samples/session03/benchmark_oss_models.py`) i wygenerować tabelę Markdown przyjazną dla GitHub oraz surowy JSON.

### Przykład

```powershell
python Workshop\scripts\export_benchmark_markdown.py --models "qwen2.5-0.5b,mistral-7b" --prompt "Explain retrieval augmented generation briefly." --rounds 3 --output benchmark_report.md
```

Wygenerowane pliki:
| Plik | Zawartość |
|------|-----------|
| `benchmark_report.md` | Tabela Markdown + wskazówki interpretacyjne |
| `benchmark_report.json` | Surowa tablica metryk (do porównania/śledzenia trendów) |

Ustaw `BENCH_STREAM=1` w środowisku, aby uwzględnić opóźnienie pierwszego tokena, jeśli obsługiwane.

---

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż staramy się zapewnić dokładność, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za autorytatywne źródło. W przypadku informacji krytycznych zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
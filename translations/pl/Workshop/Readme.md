<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8b994c57f1207012e4d7f58b7c0d1ae7",
  "translation_date": "2025-10-17T09:35:58+00:00",
  "source_file": "Workshop/Readme.md",
  "language_code": "pl"
}
-->
# EdgeAI dla Początkujących - Warsztaty

> **Praktyczna ścieżka nauki budowania gotowych do produkcji aplikacji Edge AI**
>
> Opanuj lokalne wdrażanie AI z Microsoft Foundry Local, od pierwszego ukończenia czatu po orkiestrację wieloagentową w 6 progresywnych sesjach.

---

## 🎯 Wprowadzenie

Witamy na **Warsztatach EdgeAI dla Początkujących** - praktycznym przewodniku po budowaniu inteligentnych aplikacji działających całkowicie na lokalnym sprzęcie. Te warsztaty przekształcają teoretyczne koncepcje Edge AI w umiejętności praktyczne poprzez coraz bardziej wymagające ćwiczenia z użyciem Microsoft Foundry Local i Małych Modeli Językowych (SLM).

### Dlaczego te warsztaty?

**Rewolucja Edge AI już trwa**

Organizacje na całym świecie przechodzą od AI zależnego od chmury do obliczeń brzegowych z trzech kluczowych powodów:

1. **Prywatność i zgodność** - Przetwarzaj wrażliwe dane lokalnie bez przesyłania ich do chmury (HIPAA, GDPR, regulacje finansowe)
2. **Wydajność** - Wyeliminuj opóźnienia sieciowe (50-500ms lokalnie vs 500-2000ms w chmurze)
3. **Kontrola kosztów** - Usuń koszty API za token i skaluj bez wydatków na chmurę

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
   - Wybór odpowiednich modeli do wdrożenia brzegowego
   - Zarządzanie cyklem życia modelu (pobieranie, ładowanie, buforowanie)
   - Monitorowanie wykorzystania zasobów i optymalizacja wydajności

2. **Budowanie aplikacji zasilanych AI**
   - Implementacja lokalnych ukończeń czatu kompatybilnych z OpenAI
   - Projektowanie skutecznych promptów dla Małych Modeli Językowych
   - Obsługa strumieniowych odpowiedzi dla lepszego UX
   - Integracja lokalnych modeli z istniejącymi aplikacjami

3. **Tworzenie systemów RAG (Retrieval Augmented Generation)**
   - Budowanie wyszukiwania semantycznego z użyciem osadzeń
   - Ugruntowanie odpowiedzi LLM w wiedzy specyficznej dla domeny
   - Ocena jakości RAG za pomocą standardowych metryk branżowych
   - Skalowanie od prototypu do produkcji

4. **Optymalizacja wydajności modeli**
   - Benchmarking wielu modeli dla Twojego przypadku użycia
   - Pomiar opóźnienia, przepustowości i czasu pierwszego tokena
   - Wybór optymalnych modeli na podstawie kompromisów szybkość/jakość
   - Porównanie SLM vs LLM w rzeczywistych scenariuszach

5. **Orkiestracja systemów wieloagentowych**
   - Projektowanie wyspecjalizowanych agentów do różnych zadań
   - Implementacja pamięci agentów i zarządzania kontekstem
   - Koordynacja agentów w złożonych przepływach pracy
   - Inteligentne kierowanie żądań między wieloma modelami

6. **Wdrażanie rozwiązań gotowych do produkcji**
   - Implementacja obsługi błędów i logiki ponownego próbowania
   - Monitorowanie użycia tokenów i zasobów systemowych
   - Budowanie skalowalnych architektur z wzorcami model-as-tools
   - Planowanie ścieżek migracji z edge do hybrydowych (edge + chmura)

---

## 🎓 Rezultaty nauki

### Co zbudujesz

Na koniec warsztatów stworzysz:

| Sesja | Rezultat | Demonstrowane umiejętności |
|-------|----------|---------------------------|
| **1** | Aplikacja czatu ze strumieniowaniem | Konfiguracja usługi, podstawowe ukończenia, UX strumieniowy |
| **2** | System RAG z oceną | Osadzenia, wyszukiwanie semantyczne, metryki jakości |
| **3** | Zestaw benchmarków dla wielu modeli | Pomiar wydajności, porównanie modeli |
| **4** | Porównywarka SLM vs LLM | Analiza kompromisów, strategie optymalizacji |
| **5** | Orkiestrator wieloagentowy | Projektowanie agentów, zarządzanie pamięcią, koordynacja |
| **6** | Inteligentny system routingu | Wykrywanie intencji, wybór modelu, skalowalność |

### Matryca kompetencji

| Poziom umiejętności | Sesja 1-2 | Sesja 3-4 | Sesja 5-6 |
|---------------------|-----------|-----------|-----------|
| **Początkujący** | ✅ Konfiguracja i podstawy | ⚠️ Wyzwanie | ❌ Zbyt zaawansowane |
| **Średniozaawansowany** | ✅ Szybki przegląd | ✅ Kluczowa nauka | ⚠️ Cele rozwojowe |
| **Zaawansowany** | ✅ Bez problemu | ✅ Doskonalenie | ✅ Wzorce produkcyjne |

### Umiejętności gotowe na karierę

**Po tych warsztatach będziesz gotowy do:**

✅ **Budowania aplikacji z priorytetem prywatności**
- Aplikacje zdrowotne obsługujące PHI/PII lokalnie
- Usługi finansowe z wymaganiami zgodności
- Systemy rządowe z potrzebą suwerenności danych

✅ **Optymalizacji dla środowisk brzegowych**
- Urządzenia IoT z ograniczonymi zasobami
- Aplikacje mobilne działające offline
- Systemy czasu rzeczywistego o niskim opóźnieniu

✅ **Projektowania inteligentnych architektur**
- Systemy wieloagentowe dla złożonych przepływów pracy
- Hybrydowe wdrożenia edge-chmura
- Infrastruktura AI zoptymalizowana pod kątem kosztów

✅ **Prowadzenia inicjatyw Edge AI**
- Ocena wykonalności Edge AI dla projektów
- Wybór odpowiednich modeli i frameworków
- Projektowanie skalowalnych lokalnych rozwiązań AI

---

## 🗺️ Struktura warsztatów

### Przegląd sesji (6 sesji × 30 minut = 3 godziny)

| Sesja | Temat | Skupienie | Czas trwania |
|-------|-------|-----------|--------------|
| **1** | Rozpoczęcie pracy z Foundry Local | Instalacja, weryfikacja, pierwsze ukończenia | 30 min |
| **2** | Budowanie rozwiązań AI z RAG | Inżynieria promptów, osadzenia, ocena | 30 min |
| **3** | Modele open source | Odkrywanie modeli, benchmarking, wybór | 30 min |
| **4** | Najnowocześniejsze modele | SLM vs LLM, optymalizacja, frameworki | 30 min |
| **5** | Agenci zasilani AI | Projektowanie agentów, orkiestracja, pamięć | 30 min |
| **6** | Modele jako narzędzia | Routing, łańczenie, strategie skalowania | 30 min |

---

## 🚀 Szybki start

### Wymagania wstępne

**Wymagania systemowe:**
- **OS**: Windows 10/11, macOS 11+ lub Linux (Ubuntu 20.04+)
- **RAM**: Minimum 8GB, zalecane 16GB+
- **Dysk**: 10GB+ wolnego miejsca na modele
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

**Upewnij się, że Azure AI Foundry Local działa z ustalonym portem**

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
**Znajdowanie dostępnych modeli**
Aby zobaczyć, które modele są dostępne w Twojej instancji Foundry Local, możesz zapytać endpoint modeli:

```bash
# cmd/bash/powershell
foundry model list
```

Korzystanie z endpointu Web 

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

#### 3. Uruchom swój pierwszy przykład

```bash
# Start Foundry Local and load a model
foundry model run phi-4-mini

# Run the chat bootstrap sample
cd samples/session01
python chat_bootstrap.py "What is edge AI?"
```

**✅ Sukces!** Powinieneś zobaczyć strumieniową odpowiedź dotyczącą edge AI.

---

## 📦 Zasoby warsztatowe

### Przykłady w Pythonie

Progresywne przykłady praktyczne demonstrujące każdą koncepcję:

| Sesja | Przykład | Opis | Czas wykonania |
|-------|---------|------|----------------|
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

| Sesja | Notatnik | Opis | Trudność |
|-------|----------|------|----------|
| 1 | [`session01_chat_bootstrap.ipynb`](./notebooks/session01_chat_bootstrap.ipynb) | Podstawy czatu i strumieniowanie | ⭐ Początkujący |
| 2 | [`session02_rag_pipeline.ipynb`](./notebooks/session02_rag_pipeline.ipynb) | Budowanie systemu RAG | ⭐⭐ Średniozaawansowany |
| 2 | [`session02_rag_eval_ragas.ipynb`](./notebooks/session02_rag_eval_ragas.ipynb) | Ocena jakości RAG | ⭐⭐ Średniozaawansowany |
| 3 | [`session03_benchmark_oss_models.ipynb`](./notebooks/session03_benchmark_oss_models.ipynb) | Benchmarking modeli | ⭐⭐ Średniozaawansowany |
| 4 | [`session04_model_compare.ipynb`](./notebooks/session04_model_compare.ipynb) | Porównanie modeli | ⭐⭐ Średniozaawansowany |
| 5 | [`session05_agents_orchestrator.ipynb`](./notebooks/session05_agents_orchestrator.ipynb) | Orkiestracja agentów | ⭐⭐⭐ Zaawansowany |
| 6 | [`session06_models_router.ipynb`](./notebooks/session06_models_router.ipynb) | Routing intencji | ⭐⭐⭐ Zaawansowany |
| 6 | [`session06_models_pipeline.ipynb`](./notebooks/session06_models_pipeline.ipynb) | Orkiestracja pipeline | ⭐⭐⭐ Zaawansowany |

### Dokumentacja

Kompleksowe przewodniki i odniesienia:

| Dokument | Opis | Użyj, gdy |
|----------|------|----------|
| [QUICK_START.md](./QUICK_START.md) | Przewodnik szybkiej konfiguracji | Zaczynasz od zera |
| [QUICK_REFERENCE.md](./QUICK_REFERENCE.md) | Skrócona lista poleceń i API | Potrzebujesz szybkich odpowiedzi |
| [FOUNDRY_SDK_QUICKREF.md](./FOUNDRY_SDK_QUICKREF.md) | Wzorce SDK i przykłady | Piszesz kod |
| [ENV_CONFIGURATION.md](./ENV_CONFIGURATION.md) | Przewodnik po zmiennych środowiskowych | Konfigurujesz przykłady |
| [SAMPLES_UPDATE_SUMMARY.md](./SAMPLES_UPDATE_SUMMARY.md) | Najnowsze ulepszenia przykładów | Rozumiesz zmiany |
| [SDK_MIGRATION_NOTES.md](./SDK_MIGRATION_NOTES.md) | Przewodnik migracji | Aktualizujesz kod |
| [notebooks/TROUBLESHOOTING.md](./notebooks/TROUBLESHOOTING.md) | Typowe problemy i rozwiązania | Rozwiązujesz problemy |

---

## 🎓 Rekomendacje ścieżki nauki

### Dla początkujących (3-4 godziny)
1. ✅ Sesja 1: Rozpoczęcie pracy (skup się na konfiguracji i podstawowym czacie)
2. ✅ Sesja 2: Podstawy RAG (na początku pomiń ocenę)
3. ✅ Sesja 3: Prosty benchmarking (tylko 2 modele)
4. ⏭️ Na razie pomiń sesje 4-6
5. 🔄 Wróć do sesji 4-6 po zbudowaniu pierwszej aplikacji

### Dla średniozaawansowanych (3 godziny)
1. ⚡ Sesja 1: Szybka weryfikacja konfiguracji
2. ✅ Sesja 2: Kompletny pipeline RAG z oceną
3. ✅ Sesja 3: Pełny zestaw benchmarków
4. ✅ Sesja 4: Optymalizacja modeli
5. ✅ Sesje 5-6: Skup się na wzorcach architektury

### Dla zaawansowanych (2-3 godziny)
1. ⚡ Sesje 1-3: Szybki przegląd i weryfikacja
2. ✅ Sesja 4: Dogłębna optymalizacja
3. ✅ Sesja 5: Architektura wieloagentowa
4. ✅ Sesja 6: Wzorce produkcyjne i skalowanie
5. 🚀 Rozszerz: Zbuduj własną logikę routingu i wdrożenia hybrydowe

---

## Pakiet sesji warsztatowych (Skoncentrowane 30‑minutowe laboratoria)

Jeśli podążasz za skondensowanym formatem warsztatów 6-sesyjnych, użyj tych dedykowanych przewodników (każdy odpowiada i uzupełnia szersze moduły dokumentacji powyżej):

| Sesja warsztatowa | Przewodnik | Główne skupienie |
|-------------------|-----------|------------------|
| 1 | [Session01-GettingStartedFoundryLocal](./Session01-GettingStartedFoundryLocal.md) | Instalacja, weryfikacja, uruchomienie phi & GPT-OSS-20B, przyspieszenie |
| 2 | [Session02-BuildAISolutionsRAG](./Session02-BuildAISolutionsRAG.md) | Inżynieria promptów, wzorce RAG, ugruntowanie CSV i dokumentów, migracja |
| 3 | [Session03-OpenSourceModels](./Session03-OpenSourceModels.md) | Integracja Hugging Face, benchmarking, wybór modeli |
| 4 | [Session04-CuttingEdgeModels](./Session04-CuttingEdgeModels.md) | SLM vs LLM, WebGPU, Chainlit RAG, przyspieszenie ONNX |
| 5 | [Session05-AIPoweredAgents](./Session05-AIPoweredAgents.md) | Role agentów, pamięć, narzędzia, orkiestracja |
| 6 | [Session06-ModelsAsTools](./Session06-ModelsAsTools.md) | Routing, łączenie, skalowanie na Azure |

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
| 2 | `samples/session02/rag_pipeline.py` | Minimalny RAG (w pamięci) |
|   | `samples/session02/rag_eval_ragas.py` | Ocena RAG za pomocą metryk ragas |
| 3 | `samples/session03/benchmark_oss_models.py` | Benchmarking opóźnień i przepustowości dla wielu modeli |
| 4 | `samples/session04/model_compare.py` | Porównanie SLM vs LLM (opóźnienia i przykładowe wyniki) |
| 5 | `samples/session05/agents_orchestrator.py` | Pipeline badawczy dwóch agentów → redakcja |
| 6 | `samples/session06/models_router.py` | Demonstracja routingu opartego na intencjach |
|   | `samples/session06/models_pipeline.py` | Łańcuch planowania/wykonania/poprawy w wielu krokach |

### Zmienne środowiskowe (wspólne dla wszystkich przykładów)

| Zmienna | Cel | Przykład |
|---------|-----|---------|
| `FOUNDRY_LOCAL_ALIAS` | Domyślny alias pojedynczego modelu dla podstawowych przykładów | `phi-4-mini` |
| `SLM_ALIAS` / `LLM_ALIAS` | Wyraźne SLM vs większy model do porównania | `phi-4-mini` / `gpt-oss-20b` |
| `BENCH_MODELS` | Lista aliasów do benchmarku | `qwen2.5-0.5b,gemma-2-2b,mistral-7b` |
| `BENCH_ROUNDS` | Powtórzenia benchmarku na model | `3` |
| `BENCH_PROMPT` | Prompt używany w benchmarku | `Explain retrieval augmented generation briefly.` |
| `EMBED_MODEL` | Model embeddingu sentence-transformers | `sentence-transformers/all-MiniLM-L6-v2` |
| `RAG_QUESTION` | Nadpisanie zapytania testowego dla pipeline RAG | `Why use RAG with local inference?` |
| `AGENT_QUESTION` | Nadpisanie zapytania dla pipeline agentów | `Explain why edge AI matters for compliance.` |
| `AGENT_MODEL_PRIMARY` | Alias modelu dla agenta badawczego | `phi-4-mini` |
| `AGENT_MODEL_EDITOR` | Alias modelu dla agenta redakcyjnego (może się różnić) | `gpt-oss-20b` |
| `SHOW_USAGE` | Jeśli `1`, drukuje użycie tokenów na zakończenie | `1` |
| `RETRY_ON_FAIL` | Jeśli `1`, ponawia próbę w przypadku błędów czatu | `1` |
| `RETRY_BACKOFF` | Czas oczekiwania przed ponowną próbą | `1.0` |

Jeśli zmienna nie jest ustawiona, skrypty korzystają z rozsądnych wartości domyślnych. W przypadku demonstracji z jednym modelem zazwyczaj wystarczy `FOUNDRY_LOCAL_ALIAS`.

### Moduł pomocniczy

Wszystkie przykłady korzystają teraz z pomocniczego `samples/workshop_utils.py`, który oferuje:

* Buforowaną obsługę `FoundryLocalManager` + klienta OpenAI
* Pomocnik `chat_once()` z opcjonalnym ponawianiem prób + drukowaniem użycia
* Proste raportowanie użycia tokenów (włączane przez `SHOW_USAGE=1`)

To zmniejsza duplikację i podkreśla najlepsze praktyki efektywnej orkiestracji lokalnych modeli.

## Opcjonalne ulepszenia (między sesjami)

| Temat | Ulepszenie | Sesje | Środowisko / Przełącznik |
|-------|------------|-------|--------------------------|
| Determinizm | Stała temperatura + stabilne zestawy promptów | 1–6 | Ustaw `temperature=0`, `top_p=1` |
| Widoczność użycia tokenów | Nauka kosztów/efektywności | 1–6 | `SHOW_USAGE=1` |
| Strumieniowanie pierwszego tokena | Metryka postrzeganego opóźnienia | 1,3,4,6 | `BENCH_STREAM=1` (benchmark) |
| Odporność na błędy | Obsługa zimnego startu | Wszystkie | `RETRY_ON_FAIL=1` + `RETRY_BACKOFF` |
| Wielomodelowi agenci | Specjalizacja ról | 5 | `AGENT_MODEL_PRIMARY`, `AGENT_MODEL_EDITOR` |
| Adaptacyjny routing | Intencje + heurystyki kosztowe | 6 | Rozszerz router o logikę eskalacji |
| Pamięć wektorowa | Długoterminowe przypomnienie semantyczne | 2,5,6 | Integracja indeksu embeddingu FAISS/Chroma |
| Eksport śladów | Audyt i ocena | 2,5,6 | Dodawanie linii JSON na krok |
| Rubryki jakości | Śledzenie jakości | 3–6 | Dodatkowe prompty oceniające |
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
python samples/session02/rag_eval_ragas.py
```

Rozszerz, dostarczając większy JSONL z pytaniami, kontekstami i prawdziwymi odpowiedziami, a następnie konwertując na `Dataset` Hugging Face.

## Dodatek do dokładności poleceń CLI

Warsztat celowo używa tylko aktualnie udokumentowanych/stabilnych poleceń CLI Foundry Local.

### Stabilne polecenia referencyjne

| Kategoria | Polecenie | Cel |
|-----------|-----------|-----|
| Podstawowe | `foundry --version` | Pokaż zainstalowaną wersję |
| Podstawowe | `foundry init` | Inicjalizacja konfiguracji |
| Usługa | `foundry service start` | Uruchom lokalną usługę (jeśli nie automatycznie) |
| Usługa | `foundry status` | Pokaż status usługi |
| Modele | `foundry model list` | Lista katalogu/dostępnych modeli |
| Modele | `foundry model download <alias>` | Pobierz wagi modelu do pamięci podręcznej |
| Modele | `foundry model run <alias>` | Uruchom (załaduj) model lokalnie; połącz z `--prompt` dla jednorazowego użycia |
| Modele | `foundry model unload <alias>` / `foundry model stop <alias>` | Wyładuj model z pamięci (jeśli obsługiwane) |
| Pamięć podręczna | `foundry cache list` | Lista modeli w pamięci podręcznej |
| System | `foundry system info` | Migawka sprzętu i możliwości akceleracji |
| System | `foundry system gpu-info` | Diagnostyka GPU |
| Konfiguracja | `foundry config list` | Pokaż bieżące wartości konfiguracji |
| Konfiguracja | `foundry config set <key> <value>` | Aktualizacja konfiguracji |

### Wzorzec jednorazowego promptu

Zamiast przestarzałego podpolecenia `model chat`, użyj:

```powershell
foundry model run <alias> --prompt "Your question here"
```

To wykonuje pojedynczy cykl prompt/odpowiedź, a następnie kończy działanie.

### Usunięte/unikane wzorce

| Przestarzałe/Niedokumentowane | Zastępstwo/Zalecenia |
|-------------------------------|----------------------|
| `foundry model chat <model> "..."` | `foundry model run <model> --prompt "..."` |
| `foundry model list --running` | Użyj zwykłego `foundry model list` + ostatnia aktywność/logi |
| `foundry model list --cached` | `foundry cache list` |
| `foundry model stats <model>` | Użyj skryptu benchmarkowego + narzędzi systemowych (Task Manager / `nvidia-smi`) |
| `foundry model benchmark ...` | `samples/session03/benchmark_oss_models.py` |

### Benchmarking i telemetria

- Opóźnienia, p95, tokeny/sek.: `samples/session03/benchmark_oss_models.py`
- Opóźnienie pierwszego tokena (strumieniowanie): ustaw `BENCH_STREAM=1`
- Użycie zasobów: Monitory systemowe (Task Manager, Activity Monitor, `nvidia-smi`) + `foundry system info`.

Gdy nowe polecenia telemetrii CLI zostaną ustabilizowane, można je łatwo włączyć do markdownów sesji.

### Automatyczna kontrola składni

Automatyczny linter zapobiega ponownemu wprowadzeniu przestarzałych wzorców CLI w blokach kodu markdown:

Skrypt: `Workshop/scripts/lint_markdown_cli.py`

Przestarzałe wzorce są blokowane w blokach kodu.

Zalecane zamienniki:
| Przestarzałe | Zastępstwo |
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

GitHub Action: `.github/workflows/markdown-cli-lint.yml` uruchamia się przy każdym pushu i PR.

Opcjonalny hook pre-commit:
```bash
echo "python Workshop/scripts/lint_markdown_cli.py" > .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```

## Szybka tabela migracji CLI → SDK

| Zadanie | Jednolinijkowe CLI | Równoważnik SDK (Python) | Uwagi |
|---------|--------------------|--------------------------|-------|
| Uruchom model raz (prompt) | `foundry model run phi-4-mini --prompt "Hello"` | `manager=FoundryLocalManager("phi-4-mini"); client=OpenAI(base_url=manager.endpoint, api_key=manager.api_key or "not-needed"); client.chat.completions.create(model=manager.get_model_info("phi-4-mini").id, messages=[{"role":"user","content":"Hello"}])` | SDK automatycznie uruchamia usługę i pamięć podręczną |
| Pobierz (cache) model | `foundry model download qwen2.5-0.5b` | `FoundryLocalManager("qwen2.5-0.5b")  # triggers download/load` | Manager wybiera najlepszy wariant, jeśli alias odnosi się do wielu wersji |
| Lista katalogu | `foundry model list` | `# użyj managera dla każdego aliasu lub utrzymuj znaną listę` | CLI agreguje; SDK obecnie instancja per-alias |
| Lista modeli w pamięci podręcznej | `foundry cache list` | `manager.list_cached_models()` | Po inicjalizacji managera (dowolny alias) |
| Włącz akcelerację GPU | `foundry config set compute.onnx.enable_gpu true` | `# Akcja CLI; SDK zakłada, że konfiguracja została już zastosowana` | Konfiguracja jest efektem zewnętrznym |
| Pobierz URL punktu końcowego | (implicit) | `manager.endpoint` | Używane do tworzenia klienta kompatybilnego z OpenAI |
| Rozgrzej model | `foundry model run <alias>` a następnie pierwszy prompt | `chat_once(alias, messages=[...])` (utility) | Narzędzia obsługują początkowe opóźnienie zimnego startu |
| Zmierz opóźnienie | `python benchmark_oss_models.py` | `import benchmark_oss_models` (lub nowy skrypt eksportera) | Preferuj skrypt dla spójnych metryk |
| Zatrzymaj/wyładuj model | `foundry model unload <alias>` | (Nie udostępnione – restart usługi/procesu) | Zazwyczaj nie wymagane w warsztacie |
| Pobierz użycie tokenów | (zobacz output) | `resp.usage.total_tokens` | Dostarczane, jeśli backend zwraca obiekt użycia |

## Eksport markdown benchmarku

Użyj skryptu `Workshop/scripts/export_benchmark_markdown.py`, aby uruchomić świeży benchmark (ta sama logika co `samples/session03/benchmark_oss_models.py`) i wygenerować tabelę Markdown przyjazną dla GitHub oraz surowy JSON.

### Przykład

```powershell
python Workshop\scripts\export_benchmark_markdown.py --models "qwen2.5-0.5b,gemma-2-2b,mistral-7b" --prompt "Explain retrieval augmented generation briefly." --rounds 3 --output benchmark_report.md
```

Wygenerowane pliki:
| Plik | Zawartość |
|------|-----------|
| `benchmark_report.md` | Tabela Markdown + wskazówki interpretacyjne |
| `benchmark_report.json` | Surowa tablica metryk (do porównywania/trendów) |

Ustaw `BENCH_STREAM=1` w środowisku, aby uwzględnić opóźnienie pierwszego tokena, jeśli obsługiwane.

---

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż staramy się zapewnić dokładność, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za autorytatywne źródło. W przypadku informacji krytycznych zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
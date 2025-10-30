<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d49922db25659f398bae92011305e9dc",
  "translation_date": "2025-10-28T21:45:44+00:00",
  "source_file": "Workshop/SAMPLES_UPDATE_SUMMARY.md",
  "language_code": "pl"
}
-->
# Przykłady Warsztatowe - Podsumowanie Aktualizacji Foundry Local SDK

## Przegląd

Wszystkie przykłady w Pythonie w katalogu `Workshop/samples` zostały zaktualizowane, aby stosować najlepsze praktyki Foundry Local SDK i zapewnić spójność w całym warsztacie.

**Data**: 8 października 2025  
**Zakres**: 9 plików Python w 6 sesjach warsztatowych  
**Główny cel**: Obsługa błędów, dokumentacja, wzorce SDK, doświadczenie użytkownika

---

## Zaktualizowane Pliki

### Sesja 01: Pierwsze Kroki
- ✅ `chat_bootstrap.py` - Podstawowe przykłady czatu i strumieniowania

### Sesja 02: Rozwiązania RAG
- ✅ `rag_pipeline.py` - Implementacja RAG z osadzeniami
- ✅ `rag_eval_ragas.py` - Ocena RAG z metrykami RAGAS

### Sesja 03: Modele Open Source
- ✅ `benchmark_oss_models.py` - Benchmarking wielu modeli

### Sesja 04: Najnowsze Modele
- ✅ `model_compare.py` - Porównanie SLM i LLM

### Sesja 05: Agenci Wspierani przez AI
- ✅ `agents_orchestrator.py` - Koordynacja wielu agentów

### Sesja 06: Modele jako Narzędzia
- ✅ `models_router.py` - Routing modeli oparty na intencjach
- ✅ `models_pipeline.py` - Wieloetapowy pipeline z routingiem

### Infrastruktura Wspierająca
- ✅ `workshop_utils.py` - Już zgodny z najlepszymi praktykami (bez zmian)

---

## Kluczowe Ulepszenia

### 1. Ulepszona Obsługa Błędów

**Przed:**
```python
manager, client, model_id = get_client(alias)
```

**Po:**
```python
try:
    manager, client, model_id = get_client(alias, endpoint=endpoint)
except Exception as e:
    print(f"[ERROR] Failed to initialize Foundry Local client: {e}")
    print("[INFO] Ensure Foundry Local is running: foundry service status")
    sys.exit(1)
```

**Korzyści:**
- Łagodna obsługa błędów z jasnymi komunikatami
- Wskazówki dotyczące rozwiązywania problemów
- Odpowiednie kody wyjścia dla skryptów

### 2. Lepsze Zarządzanie Importami

**Przed:**
```python
from sentence_transformers import SentenceTransformer
```

**Po:**
```python
try:
    from sentence_transformers import SentenceTransformer
except ImportError:
    print("[ERROR] sentence-transformers is required. Install with: pip install sentence-transformers")
    sys.exit(1)
```

**Korzyści:**
- Jasne wskazówki w przypadku brakujących zależności
- Zapobieganie niejasnym błędom importu
- Przyjazne dla użytkownika instrukcje instalacji

### 3. Kompleksowa Dokumentacja

**Dodano do wszystkich przykładów:**
- Dokumentacja zmiennych środowiskowych w docstrings
- Linki do dokumentacji SDK
- Przykłady użycia
- Szczegółowa dokumentacja funkcji/parametrów
- Podpowiedzi typów dla lepszego wsparcia IDE

**Przykład:**
```python
def pipeline(task: str) -> Dict[str, Any]:
    """Execute multi-step routed pipeline for complex task.
    
    Args:
        task: User task description
    
    Returns:
        Dictionary with plan, step outputs, and final summary
    
    Raises:
        Exception: If any pipeline stage fails
    """
```

### 4. Ulepszona Informacja Zwrotna dla Użytkownika

**Dodano informacyjne logowanie:**
```python
print(f"[INFO] Using model alias: {alias} -> id: {model_id}")
print(f"[INFO] Endpoint: {manager.endpoint}")
print(f"[INFO] Loaded model: {alias} -> {model_id}")
```

**Wskaźniki postępu:**
```python
print(f"[INFO] Benchmarking {alias}...")
print(f"  Round {round_num + 1}/{ROUNDS}: {latency:.3f}s")
print(f"[INFO] Completed {alias}\n")
```

**Strukturalne dane wyjściowe:**
```python
print("\n[BENCHMARK RESULTS]")
print(json.dumps(summary, indent=2))
```

### 5. Solidne Benchmarking

**Ulepszenia w Sesji 03:**
- Obsługa błędów dla każdego modelu (kontynuacja w przypadku awarii)
- Szczegółowe raportowanie postępu
- Wykonanie rund rozgrzewkowych
- Obsługa pomiaru opóźnienia pierwszego tokena
- Wyraźne rozdzielenie etapów

### 6. Spójne Podpowiedzi Typów

**Dodano wszędzie:**
```python
from typing import Dict, List, Tuple, Any, Optional

def run(alias: str) -> Tuple[float, str, Optional[int]]:
    """Run comparison for given model alias."""
```

**Korzyści:**
- Lepsze autouzupełnianie w IDE
- Wczesne wykrywanie błędów
- Samodokumentujący się kod

### 7. Ulepszony Router Modeli

**Ulepszenia w Sesji 06:**
- Kompleksowa dokumentacja wykrywania intencji
- Wyjaśnienie algorytmu wyboru modelu
- Szczegółowe logi routingu
- Formatowanie wyników testów
- Odzyskiwanie błędów w testach batchowych

### 8. Orkiestracja Wielu Agentów

**Ulepszenia w Sesji 05:**
- Raportowanie postępu etap po etapie
- Obsługa błędów dla każdego agenta
- Wyraźna struktura pipeline'u
- Lepsza dokumentacja zarządzania pamięcią

---

## Lista Kontrolna Testów

### Wymagania Wstępne
```bash
# Ensure Foundry Local is running
foundry service status

# Load required models
foundry model run phi-4-mini
foundry model run qwen2.5-0.5b

# Install dependencies
pip install -r Workshop/requirements.txt
```

### Testowanie Każdego Przykładu

#### Sesja 01
```bash
cd Workshop/samples
python -m session01.chat_bootstrap "What is edge AI?"
```

#### Sesja 02
```bash
cd Workshop/samples

# RAG pipeline
python -m session02.rag_pipeline

# RAG evaluation (requires ragas)
set RAG_QUESTION="What is local inference?"
python -m session02.rag_eval_ragas
```

#### Sesja 03
```bash
cd Workshop/samples

# Quick benchmark (2 rounds)
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
set BENCH_ROUNDS=2
python -m session03.benchmark_oss_models
```

#### Sesja 04
```bash
cd Workshop/samples

# SLM vs LLM comparison
set SLM_ALIAS=phi-4-mini
set LLM_ALIAS=qwen2.5-7b
python -m session04.model_compare
```

#### Sesja 05
```bash
cd Workshop/samples

# Multi-agent orchestration
set AGENT_QUESTION="Why use local AI for healthcare?"
python -m session05.agents_orchestrator
```

#### Sesja 06
```bash
cd Workshop/samples

# Intent-based routing
python -m session06.models_router

# Multi-step pipeline
set PIPELINE_TASK="Create a Python function and explain its performance"
python -m session06.models_pipeline
```

---

## Referencje Zmiennych Środowiskowych

### Globalne (Wszystkie Przykłady)
| Zmienna | Opis | Domyślna |
|---------|------|---------|
| `FOUNDRY_LOCAL_ALIAS` | Alias modelu do użycia | Różni się w zależności od przykładu |
| `FOUNDRY_LOCAL_ENDPOINT` | Nadpisanie punktu końcowego usługi | Automatycznie wykrywane |
| `SHOW_USAGE` | Pokazuje użycie tokenów | `0` |
| `RETRY_ON_FAIL` | Włącza logikę ponawiania prób | `1` |
| `RETRY_BACKOFF` | Początkowe opóźnienie ponowienia | `1.0` |

### Specyficzne dla Przykładu
| Zmienna | Używane przez | Opis |
|---------|--------------|------|
| `EMBED_MODEL` | Sesja 02 | Nazwa modelu osadzającego |
| `RAG_QUESTION` | Sesja 02 | Pytanie testowe dla RAG |
| `BENCH_MODELS` | Sesja 03 | Modele do benchmarkingu (oddzielone przecinkami) |
| `BENCH_ROUNDS` | Sesja 03 | Liczba rund benchmarkingu |
| `BENCH_PROMPT` | Sesja 03 | Testowy prompt dla benchmarków |
| `BENCH_STREAM` | Sesja 03 | Pomiar opóźnienia pierwszego tokena |
| `SLM_ALIAS` | Sesja 04 | Mały model językowy |
| `LLM_ALIAS` | Sesja 04 | Duży model językowy |
| `COMPARE_PROMPT` | Sesja 04 | Testowy prompt porównawczy |
| `AGENT_MODEL_PRIMARY` | Sesja 05 | Model głównego agenta |
| `AGENT_MODEL_EDITOR` | Sesja 05 | Model agenta edytora |
| `AGENT_QUESTION` | Sesja 05 | Pytanie testowe dla agentów |
| `PIPELINE_TASK` | Sesja 06 | Zadanie dla pipeline'u |

---

## Zmiany Łamiące

**Brak** - Wszystkie zmiany są kompatybilne wstecz.

Istniejące skrypty będą nadal działać. Nowe funkcje to:
- Opcjonalne zmienne środowiskowe
- Ulepszone komunikaty o błędach (nie psują funkcjonalności)
- Dodatkowe logowanie (można je wyłączyć)
- Lepsze podpowiedzi typów (bez wpływu na działanie)

---

## Wdrożone Najlepsze Praktyki

### 1. Zawsze używaj Workshop Utils
```python
from workshop_utils import get_client, chat_once

# Provides caching, retry, and endpoint management
manager, client, model_id = get_client(alias, endpoint=endpoint)
```

### 2. Wzorzec Obsługi Błędów
```python
try:
    # Initialize client
    manager, client, model_id = get_client(alias)
except Exception as e:
    print(f"[ERROR] Initialization failed: {e}")
    print("[INFO] Check: foundry service status")
    sys.exit(1)
```

### 3. Informacyjne Logowanie
```python
print(f"[INFO] Starting process...")  # Info
print(f"[ERROR] Operation failed: {e}")  # Errors
print(f"[RESULT] Final output")  # Results
```

### 4. Podpowiedzi Typów
```python
from typing import Dict, List, Optional

def process(data: List[str]) -> Dict[str, Any]:
    """Process data with type safety."""
```

### 5. Kompleksowe Docstrings
```python
def function(arg: str) -> str:
    """Short description.
    
    Args:
        arg: Argument description
    
    Returns:
        Return value description
    
    Raises:
        Exception: When it fails
    """
```

### 6. Obsługa Zmiennych Środowiskowych
```python
import os

alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-4-mini")
endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT")  # None if not set
```

### 7. Łagodna Degradacja
```python
# In benchmarks - continue on individual failures
for model in models:
    try:
        result = benchmark(model)
        results.append(result)
    except Exception as e:
        print(f"[ERROR] {model} failed: {e}")
        print(f"[INFO] Skipping {model}...")
```

---

## Typowe Problemy i Rozwiązania

### Problem: Błędy Importu
**Rozwiązanie:** Zainstaluj brakujące zależności
```bash
pip install sentence-transformers ragas datasets numpy
```

### Problem: Błędy Połączenia
**Rozwiązanie:** Upewnij się, że Foundry Local działa
```bash
foundry service status
foundry model run phi-4-mini
```

### Problem: Model Nie Znaleziony
**Rozwiązanie:** Sprawdź dostępne modele
```bash
foundry model ls
foundry model download <alias>
```

### Problem: Wolne Działanie
**Rozwiązanie:** Użyj mniejszych modeli lub dostosuj parametry
```bash
set FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b
set BENCH_ROUNDS=2
```

---

## Kolejne Kroki

### 1. Przetestuj Wszystkie Przykłady
Przejdź przez listę kontrolną testów powyżej, aby zweryfikować poprawność działania wszystkich przykładów.

### 2. Zaktualizuj Dokumentację
- Zaktualizuj pliki markdown sesji o nowe przykłady
- Dodaj sekcję rozwiązywania problemów do głównego README
- Stwórz przewodnik szybkiego odniesienia

### 3. Utwórz Testy Integracyjne
```python
# Workshop/tests/test_samples.py
def test_all_samples():
    """Run smoke tests on all samples."""
```

### 4. Dodaj Benchmarki Wydajności
Śledź poprawę wydajności wynikającą z ulepszeń obsługi błędów.

### 5. Informacja Zwrotna od Użytkowników
Zbierz opinie uczestników warsztatów na temat:
- Jasności komunikatów o błędach
- Kompleksowości dokumentacji
- Łatwości użycia

---

## Zasoby

- **Foundry Local SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **Przewodnik Szybkiego Odniesienia**: `Workshop/FOUNDRY_SDK_QUICKREF.md`
- **Notatki Migracyjne**: `Workshop/SDK_MIGRATION_NOTES.md`
- **Główne Repozytorium**: https://github.com/microsoft/Foundry-Local

---

## Utrzymanie

### Dodawanie Nowych Przykładów
Stosuj poniższe wzorce podczas tworzenia nowych przykładów:

1. Używaj `workshop_utils` do zarządzania klientem
2. Dodaj kompleksową obsługę błędów
3. Uwzględnij obsługę zmiennych środowiskowych
4. Dodaj podpowiedzi typów i docstrings
5. Zapewnij informacyjne logowanie
6. Uwzględnij przykłady użycia w docstrings
7. Dodaj linki do dokumentacji SDK

### Przeglądanie Aktualizacji
Podczas przeglądania aktualizacji przykładów sprawdź:
- [ ] Obsługę błędów dla wszystkich operacji I/O
- [ ] Podpowiedzi typów dla funkcji publicznych
- [ ] Kompleksowe docstrings
- [ ] Dokumentację zmiennych środowiskowych
- [ ] Informacyjną informację zwrotną dla użytkownika
- [ ] Linki do dokumentacji SDK
- [ ] Spójny styl kodu

---

**Podsumowanie**: Wszystkie przykłady w Pythonie w warsztacie są teraz zgodne z najlepszymi praktykami Foundry Local SDK, z ulepszoną obsługą błędów, kompleksową dokumentacją i poprawionym doświadczeniem użytkownika. Brak zmian łamiących - wszystkie istniejące funkcjonalności zostały zachowane i ulepszone.

---

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż staramy się zapewnić dokładność, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za autorytatywne źródło. W przypadku informacji krytycznych zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
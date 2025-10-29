<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a5bfedb0d4694a0b3a95d69b159b1a5a",
  "translation_date": "2025-10-28T21:46:04+00:00",
  "source_file": "Workshop/SDK_MIGRATION_NOTES.md",
  "language_code": "pl"
}
-->
# Notatki dotyczące migracji lokalnego SDK Foundry

## Przegląd

Wszystkie pliki Python w folderze Workshop zostały zaktualizowane, aby odpowiadać najnowszym wzorcom z oficjalnego [Foundry Local Python SDK](https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local).

## Podsumowanie zmian

### Podstawowa infrastruktura (`workshop_utils.py`)

#### Ulepszone funkcje:
- **Obsługa nadpisywania punktu końcowego**: Dodano obsługę zmiennej środowiskowej `FOUNDRY_LOCAL_ENDPOINT`
- **Ulepszone zarządzanie błędami**: Lepsze obsługiwanie wyjątków z bardziej szczegółowymi komunikatami o błędach
- **Ulepszona pamięć podręczna**: Klucze pamięci podręcznej teraz uwzględniają punkt końcowy dla scenariuszy z wieloma punktami końcowymi
- **Eksponencjalne opóźnienie**: Logika ponownego próbowania teraz wykorzystuje eksponencjalne opóźnienie dla większej niezawodności
- **Adnotacje typów**: Dodano kompleksowe wskazówki typów dla lepszego wsparcia IDE

#### Nowe możliwości:
```python
# Now supports endpoint override
manager, client, model_id = get_client(alias, endpoint="http://localhost:8000")

# Better error messages
RuntimeError: Client initialization failed for 'phi-4-mini': <detailed_error>
```

### Przykładowe aplikacje

#### Sesja 01: Chat Bootstrap (`chat_bootstrap.py`)
- Zaktualizowano domyślny model z `phi-3.5-mini` na `phi-4-mini`
- Dodano obsługę nadpisywania punktu końcowego
- Ulepszono dokumentację o odniesienia do SDK

#### Sesja 02: RAG Pipeline (`rag_pipeline.py`)
- Zaktualizowano domyślny model na `phi-4-mini`
- Dodano obsługę nadpisywania punktu końcowego
- Ulepszono dokumentację o szczegóły dotyczące zmiennych środowiskowych

#### Sesja 02: RAG Evaluation (`rag_eval_ragas.py`)
- Zaktualizowano domyślne modele
- Dodano konfigurację punktu końcowego
- Ulepszono obsługę błędów

#### Sesja 03: Benchmarking (`benchmark_oss_models.py`)
- Zaktualizowano domyślną listę modeli, dodając `phi-4-mini`
- Dodano kompleksową dokumentację zmiennych środowiskowych
- Ulepszono dokumentację funkcji
- Dodano obsługę nadpisywania punktu końcowego w całym kodzie

#### Sesja 04: Porównanie modeli (`model_compare.py`)
- Zaktualizowano domyślny LLM z `gpt-oss-20b` na `qwen2.5-7b`
- Dodano konfigurację punktu końcowego
- Ulepszono dokumentację

#### Sesja 05: Orkiestracja wieloagentowa (`agents_orchestrator.py`)
- Dodano wskazówki typów (zmieniono `str | None` na `Optional[str]`)
- Ulepszono dokumentację klasy Agent
- Dodano obsługę nadpisywania punktu końcowego
- Ulepszono wzorzec inicjalizacji

#### Sesja 06: Router modeli (`models_router.py`)
- Dodano konfigurację punktu końcowego
- Ulepszono dokumentację wykrywania intencji
- Ulepszono dokumentację logiki routingu

#### Sesja 06: Pipeline (`models_pipeline.py`)
- Dodano kompleksową dokumentację funkcji
- Ulepszono dokumentację krok po kroku
- Ulepszono obsługę błędów

### Skrypty

#### Eksport benchmarków (`export_benchmark_markdown.py`)
- Dodano obsługę nadpisywania punktu końcowego
- Zaktualizowano domyślne modele
- Ulepszono dokumentację funkcji
- Ulepszono obsługę błędów

#### CLI Linter (`lint_markdown_cli.py`)
- Dodano linki do odniesień SDK
- Ulepszono dokumentację użytkowania

### Testy

#### Testy wstępne (`smoke.py`)
- Dodano obsługę nadpisywania punktu końcowego
- Ulepszono dokumentację
- Ulepszono dokumentację przypadków testowych
- Lepsze raportowanie błędów

## Zmienne środowiskowe

Wszystkie przykłady teraz obsługują te zmienne środowiskowe:

### Podstawowa konfiguracja
- `FOUNDRY_LOCAL_ALIAS` - Alias modelu do użycia (domyślny różni się w zależności od przykładu)
- `FOUNDRY_LOCAL_ENDPOINT` - Nadpisanie punktu końcowego usługi (opcjonalne)
- `SHOW_USAGE` - Wyświetlanie statystyk użycia tokenów (domyślnie: "0")
- `RETRY_ON_FAIL` - Włączenie logiki ponownego próbowania (domyślnie: "1")
- `RETRY_BACKOFF` - Początkowe opóźnienie ponownego próbowania w sekundach (domyślnie: "1.0")

### Specyficzne dla przykładu
- `EMBED_MODEL` - Model osadzania dla przykładów RAG
- `BENCH_MODELS` - Modele oddzielone przecinkami do benchmarkingu
- `BENCH_ROUNDS` - Liczba rund benchmarkingu
- `BENCH_PROMPT` - Testowy prompt dla benchmarków
- `BENCH_STREAM` - Pomiar opóźnienia pierwszego tokena
- `RAG_QUESTION` - Testowe pytanie dla przykładów RAG
- `AGENT_MODEL_PRIMARY` - Główny model agenta
- `AGENT_MODEL_EDITOR` - Model edytora agenta
- `SLM_ALIAS` - Alias małego modelu językowego
- `LLM_ALIAS` - Alias dużego modelu językowego

## Najlepsze praktyki SDK wdrożone

### 1. Prawidłowa inicjalizacja klienta
```python
# Old pattern
manager = FoundryLocalManager(alias)
client = OpenAI(base_url=manager.endpoint, api_key="not-needed")

# New pattern (with endpoint override)
manager = FoundryLocalManager(alias, endpoint=endpoint) if endpoint else FoundryLocalManager(alias)
client = OpenAI(
    base_url=manager.endpoint,
    api_key=manager.api_key or "not-needed"
)
```

### 2. Pobieranie informacji o modelu
```python
# Proper model ID resolution
model_info = manager.get_model_info(alias)
model_id = model_info.id
```

### 3. Obsługa błędów
```python
# Comprehensive error handling
try:
    manager = FoundryLocalManager(alias)
    # ... operations
except Exception as e:
    logger.error(f"Failed to initialize: {e}")
    raise RuntimeError(f"Initialization failed: {e}") from e
```

### 4. Logika ponownego próbowania z eksponencjalnym opóźnieniem
```python
delay = initial_delay
for attempt in range(max_retries):
    try:
        # ... operation
        break
    except Exception:
        time.sleep(delay)
        delay *= 2  # Exponential backoff
```

### 5. Obsługa strumieniowania
```python
stream = client.chat.completions.create(
    model=model_id,
    messages=messages,
    stream=True,
    max_tokens=120
)
for chunk in stream:
    if chunk.choices and chunk.choices[0].delta:
        # Process chunk
```

## Przewodnik migracji dla niestandardowych przykładów

Jeśli tworzysz nowe przykłady lub aktualizujesz istniejące:

1. **Używaj pomocników z `workshop_utils.py`**:
   ```python
   from workshop_utils import get_client, chat_once
   ```

2. **Obsługuj nadpisywanie punktu końcowego**:
   ```python
   endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT")
   manager, client, model_id = get_client(alias, endpoint=endpoint)
   ```

3. **Dodaj kompleksową dokumentację**:
   - Zmienne środowiskowe w docstringu
   - Link do odniesienia SDK
   - Przykłady użycia

4. **Używaj wskazówek typów**:
   ```python
   from typing import Optional, List, Dict, Any
   ```

5. **Wdroż odpowiednią obsługę błędów**:
   ```python
   try:
       result = operation()
   except Exception as e:
       logger.error(f"Operation failed: {e}")
       raise
   ```

## Testowanie

Wszystkie przykłady można przetestować za pomocą:

```bash
# Set environment variables
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Run individual samples
cd Workshop/samples
python -m session01.chat_bootstrap "Test question"
python -m session02.rag_pipeline

# Run benchmark
python -m session03.benchmark_oss_models

# Run smoke tests
python -m Workshop.tests.smoke
```

## Odniesienia do dokumentacji SDK

- **Główne repozytorium**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **Dokumentacja API**: Sprawdź najnowszą dokumentację API w repozytorium SDK

## Zmiany łamiące kompatybilność

### Brak oczekiwanych
Wszystkie zmiany są wstecznie kompatybilne. Aktualizacje głównie:
- Dodają nowe opcjonalne funkcje (nadpisywanie punktu końcowego)
- Ulepszają obsługę błędów
- Poprawiają dokumentację
- Aktualizują domyślne nazwy modeli zgodnie z bieżącymi rekomendacjami

### Opcjonalne ulepszenia
Możesz zaktualizować swój kod, aby używać:
- `FOUNDRY_LOCAL_ENDPOINT` dla jawnej kontroli punktu końcowego
- `SHOW_USAGE=1` dla widoczności użycia tokenów
- Zaktualizowanych domyślnych modeli (`phi-4-mini` zamiast `phi-3.5-mini`)

## Typowe problemy i rozwiązania

### Problem: "Nie udało się zainicjalizować klienta"
**Rozwiązanie**: Upewnij się, że usługa Foundry Local działa:
```bash
foundry service start
foundry model run phi-4-mini
```

### Problem: "Model nie znaleziony"
**Rozwiązanie**: Sprawdź dostępne modele:
```bash
foundry model list
```

### Problem: Błędy połączenia z punktem końcowym
**Rozwiązanie**: Zweryfikuj punkt końcowy:
```bash
# Check service status
foundry service status

# Or set explicit endpoint
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000
```

## Kolejne kroki

1. **Zaktualizuj przykłady z Module08**: Zastosuj podobne wzorce do Module08/samples
2. **Dodaj testy integracyjne**: Stwórz kompleksowy zestaw testów
3. **Benchmarking wydajności**: Porównaj wydajność przed i po
4. **Aktualizacje dokumentacji**: Zaktualizuj główny README o nowe wzorce

## Wytyczne dotyczące wkładu

Podczas dodawania nowych przykładów:
1. Używaj `workshop_utils.py` dla spójności
2. Postępuj zgodnie z wzorcem w istniejących przykładach
3. Dodaj kompleksowe docstringi
4. Uwzględnij linki do odniesień SDK
5. Obsługuj nadpisywanie punktu końcowego
6. Dodaj odpowiednie wskazówki typów
7. Uwzględnij przykłady użycia w docstringu

## Kompatybilność wersji

Te aktualizacje są kompatybilne z:
- `foundry-local-sdk` (najnowsza wersja)
- `openai>=1.30.0`
- Python 3.8+

---

**Ostatnia aktualizacja**: 2025-01-08  
**Opiekun**: Zespół EdgeAI Workshop  
**Wersja SDK**: Foundry Local SDK (najnowsza 0.7.117+67073234e7)

---

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż staramy się zapewnić dokładność, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za autorytatywne źródło. W przypadku informacji krytycznych zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
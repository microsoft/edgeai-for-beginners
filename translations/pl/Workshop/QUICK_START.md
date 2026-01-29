# Szybki przewodnik po warsztatach

## Wymagania wstępne

### 1. Zainstaluj Foundry Local

Postępuj zgodnie z oficjalnym przewodnikiem instalacji:  
https://github.com/microsoft/Foundry-Local

```bash
# Start Foundry Local service
foundry service start

# Load a model (phi-4-mini recommended for workshop)
foundry model run phi-4-mini

# Verify service is running
foundry service status
```

### 2. Zainstaluj zależności Python

Z katalogu warsztatowego:

```bash
# Create virtual environment (recommended)
python -m venv .venv

# Activate virtual environment
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# Install requirements
pip install -r requirements.txt
```

## Uruchamianie przykładów warsztatowych

### Sesja 01: Podstawowy czat

```bash
cd Workshop/samples
python -m session01.chat_bootstrap "What are the benefits of local AI?"
```

**Zmienne środowiskowe:**  
```bash
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
```

### Sesja 02: Pipeline RAG

```bash
cd Workshop/samples
python -m session02.rag_pipeline
```

**Zmienne środowiskowe:**  
```bash
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set RAG_QUESTION="Why use RAG with local inference?"
set EMBED_MODEL=sentence-transformers/all-MiniLM-L6-v2
```

### Sesja 02: Ocena RAG (Ragas)

```bash
cd Workshop/samples
python -m session02.rag_eval_ragas
```

**Uwaga**: Wymaga dodatkowych zależności zainstalowanych przez `requirements.txt`

### Sesja 03: Benchmarking

```bash
cd Workshop/samples
python -m session03.benchmark_oss_models
```

**Zmienne środowiskowe:**  
```bash
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
set BENCH_ROUNDS=5
set BENCH_PROMPT="Explain RAG briefly"
set BENCH_STREAM=1
```

**Wynik**: JSON z metrykami opóźnienia, przepustowości i pierwszego tokena

### Sesja 04: Porównanie modeli

```bash
cd Workshop/samples
python -m session04.model_compare
```

**Zmienne środowiskowe:**  
```bash
set SLM_ALIAS=phi-4-mini
set LLM_ALIAS=qwen2.5-7b
set COMPARE_PROMPT="List 5 benefits of local AI inference"
```

### Sesja 05: Orkiestracja wieloagentowa

```bash
cd Workshop/samples
python -m session05.agents_orchestrator
```

**Zmienne środowiskowe:**  
```bash
set AGENT_MODEL_PRIMARY=phi-4-mini
set AGENT_MODEL_EDITOR=phi-4-mini
set AGENT_QUESTION="Explain why edge AI matters for compliance"
```

### Sesja 06: Router modeli

```bash
cd Workshop/samples
python -m session06.models_router
```

**Testuje logikę routingu** dla wielu intencji (kod, podsumowanie, klasyfikacja)

### Sesja 06: Pipeline

```bash
python -m session06.models_pipeline
```

**Złożony pipeline wieloetapowy** z planowaniem, wykonaniem i udoskonaleniem

## Skrypty

### Eksport raportu z benchmarku

```bash
cd Workshop/scripts
python export_benchmark_markdown.py \
    --models "phi-4-mini,qwen2.5-0.5b" \
    --prompt "Explain RAG briefly" \
    --rounds 3 \
    --output benchmark_report.md
```

**Wynik**: Tabela w formacie Markdown + metryki w JSON

### Sprawdzanie wzorców CLI w Markdown

```bash
python lint_markdown_cli.py --verbose
```

**Cel**: Wykrywanie przestarzałych wzorców CLI w dokumentacji

## Testowanie

### Testy wstępne

```bash
cd Workshop
python -m tests.smoke
```

**Testy**: Podstawowa funkcjonalność kluczowych przykładów

## Rozwiązywanie problemów

### Usługa nie działa

```bash
# Check status
foundry service status

# Start if not running
foundry service start

# Load a model
foundry model run phi-4-mini
```

### Błędy importu modułów

```bash
# Ensure virtual environment is activated
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux

# Reinstall dependencies
pip install -r requirements.txt
```

### Błędy połączenia

```bash
# Check endpoint
foundry service status

# Set explicit endpoint if needed
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000
```

### Model nie znaleziony

```bash
# List available models
foundry model list

# Download and run a model
foundry model run phi-4-mini
```

## Odniesienie do zmiennych środowiskowych

### Konfiguracja podstawowa
| Zmienna | Domyślna wartość | Opis |
|---------|------------------|------|
| `FOUNDRY_LOCAL_ALIAS` | Różne | Alias modelu do użycia |
| `FOUNDRY_LOCAL_ENDPOINT` | Auto | Nadpisanie punktu końcowego usługi |
| `SHOW_USAGE` | `0` | Wyświetlanie statystyk użycia tokenów |
| `RETRY_ON_FAIL` | `1` | Włączenie logiki ponownego próbowania |
| `RETRY_BACKOFF` | `1.0` | Początkowe opóźnienie ponownego próbowania (sekundy) |

### Specyficzne dla sesji
| Zmienna | Domyślna wartość | Opis |
|---------|------------------|------|
| `EMBED_MODEL` | `sentence-transformers/all-MiniLM-L6-v2` | Model osadzania |
| `RAG_QUESTION` | Zobacz przykład | Pytanie testowe RAG |
| `BENCH_MODELS` | Różne | Modele oddzielone przecinkami |
| `BENCH_ROUNDS` | `3` | Iteracje benchmarku |
| `BENCH_PROMPT` | Zobacz przykład | Podpowiedź benchmarku |
| `BENCH_STREAM` | `0` | Pomiar opóźnienia pierwszego tokena |
| `AGENT_MODEL_PRIMARY` | `phi-4-mini` | Główny model agenta |
| `AGENT_MODEL_EDITOR` | Główny | Model agenta edytora |
| `SLM_ALIAS` | `phi-4-mini` | Mały model językowy |
| `LLM_ALIAS` | `qwen2.5-7b` | Duży model językowy |
| `COMPARE_PROMPT` | Zobacz przykład | Podpowiedź porównawcza |

## Rekomendowane modele

### Rozwój i testowanie
- **phi-4-mini** - Zrównoważona jakość i szybkość
- **qwen2.5-0.5b** - Bardzo szybki dla klasyfikacji
- **gemma-2-2b** - Dobra jakość, umiarkowana szybkość

### Scenariusze produkcyjne
- **phi-4-mini** - Ogólne zastosowanie
- **deepseek-coder-1.3b** - Generowanie kodu
- **qwen2.5-7b** - Wysokiej jakości odpowiedzi

## Dokumentacja SDK

- **Foundry Local**: https://github.com/microsoft/Foundry-Local  
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local

## Uzyskiwanie pomocy

1. Sprawdź status usługi: `foundry service status`  
2. Przejrzyj logi: Sprawdź logi usługi Foundry Local  
3. Sprawdź dokumentację SDK: https://github.com/microsoft/Foundry-Local  
4. Przejrzyj kod przykładowy: Wszystkie przykłady zawierają szczegółowe docstringi

## Kolejne kroki

1. Ukończ wszystkie sesje warsztatowe w kolejności  
2. Eksperymentuj z różnymi modelami  
3. Dostosuj przykłady do swoich przypadków użycia  

---

**Ostatnia aktualizacja**: 2025-01-08  
**Wersja warsztatów**: Najnowsza  
**SDK**: Foundry Local Python SDK

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż staramy się zapewnić dokładność, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za wiarygodne źródło. W przypadku informacji krytycznych zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
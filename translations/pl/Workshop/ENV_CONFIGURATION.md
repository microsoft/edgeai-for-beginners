<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "da0a7a09670d5ab535141d121ea043fe",
  "translation_date": "2025-10-28T21:42:14+00:00",
  "source_file": "Workshop/ENV_CONFIGURATION.md",
  "language_code": "pl"
}
-->
# Przewodnik konfiguracji środowiska

## Przegląd

Przykłady warsztatowe wykorzystują zmienne środowiskowe do konfiguracji, które są centralnie zarządzane w pliku `.env` znajdującym się w głównym katalogu repozytorium. Dzięki temu można łatwo dostosować ustawienia bez konieczności modyfikowania kodu.

## Szybki start

### 1. Sprawdź wymagania wstępne

```bash
# Check Foundry Local is installed
foundry --version

# Check service is running
foundry service status

# Load a model
foundry model run phi-4-mini
```

### 2. Skonfiguruj środowisko

Plik `.env` jest już skonfigurowany z domyślnymi ustawieniami. Większość użytkowników nie będzie musiała nic zmieniać.

**Opcjonalnie**: Przejrzyj i dostosuj ustawienia:
```bash
# Edit .env file
notepad .env  # Windows
nano .env     # macOS/Linux
```

### 3. Zastosuj konfigurację

**Dla skryptów Python:**
```bash
cd Workshop/samples
python -m session01.chat_bootstrap "Your question here"
# Environment variables automatically loaded
```

**Dla notebooków:**
```python
# Restart kernel after .env changes
# Variables are loaded when cells execute
```

## Referencja zmiennych środowiskowych

### Podstawowa konfiguracja

| Zmienna | Domyślna wartość | Opis |
|---------|------------------|------|
| `FOUNDRY_LOCAL_ALIAS` | `phi-4-mini` | Domyślny model dla przykładów |
| `FOUNDRY_LOCAL_ENDPOINT` | (puste) | Nadpisanie punktu końcowego usługi |
| `PYTHONPATH` | Ścieżki warsztatowe | Ścieżka wyszukiwania modułów Python |

**Kiedy ustawić FOUNDRY_LOCAL_ENDPOINT:**
- Zdalna instancja Foundry Local
- Niestandardowa konfiguracja portu
- Oddzielenie środowisk deweloperskich/produkcyjnych

**Przykład:**
```bash
# Local custom port
FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Remote instance
FOUNDRY_LOCAL_ENDPOINT=http://192.168.1.50:5273/v1
```

### Zmienne specyficzne dla sesji

#### Sesja 02: Pipeline RAG
| Zmienna | Domyślna wartość | Cel |
|---------|------------------|-----|
| `EMBED_MODEL` | `sentence-transformers/all-MiniLM-L6-v2` | Model osadzania |
| `RAG_QUESTION` | Wstępnie skonfigurowane | Pytanie testowe |

#### Sesja 03: Benchmarking
| Zmienna | Domyślna wartość | Cel |
|---------|------------------|-----|
| `BENCH_MODELS` | `phi-4-mini,qwen2.5-0.5b` | Modele do benchmarku |
| `BENCH_ROUNDS` | `3` | Liczba iteracji na model |
| `BENCH_PROMPT` | Wstępnie skonfigurowane | Prompt testowy |
| `BENCH_STREAM` | `0` | Pomiar opóźnienia pierwszego tokenu |

#### Sesja 04: Porównanie modeli
| Zmienna | Domyślna wartość | Cel |
|---------|------------------|-----|
| `SLM_ALIAS` | `phi-4-mini` | Mały model językowy |
| `LLM_ALIAS` | `qwen2.5-7b` | Duży model językowy |
| `COMPARE_PROMPT` | Wstępnie skonfigurowane | Prompt porównawczy |
| `COMPARE_RETRIES` | `2` | Liczba prób ponowienia |

#### Sesja 05: Orkiestracja wieloagentowa
| Zmienna | Domyślna wartość | Cel |
|---------|------------------|-----|
| `AGENT_MODEL_PRIMARY` | `phi-4-mini` | Model agenta badawczego |
| `AGENT_MODEL_EDITOR` | `phi-4-mini` | Model agenta edytora |
| `AGENT_QUESTION` | Wstępnie skonfigurowane | Pytanie testowe |

### Konfiguracja niezawodności

| Zmienna | Domyślna wartość | Cel |
|---------|------------------|-----|
| `SHOW_USAGE` | `1` | Wyświetlanie zużycia tokenów |
| `RETRY_ON_FAIL` | `1` | Włączenie logiki ponawiania |
| `RETRY_BACKOFF` | `1.0` | Opóźnienie ponowienia (sekundy) |

## Typowe konfiguracje

### Ustawienia deweloperskie (szybka iteracja)
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=phi-4-mini
BENCH_MODELS=phi-4-mini
SHOW_USAGE=1
```

### Ustawienia produkcyjne (skupienie na jakości)
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-7b
AGENT_MODEL_PRIMARY=phi-4-mini
AGENT_MODEL_EDITOR=qwen2.5-7b
SHOW_USAGE=0
```

### Konfiguracja benchmarków
```bash
BENCH_MODELS=phi-4-mini,qwen2.5-0.5b,qwen2.5-7b
BENCH_ROUNDS=5
BENCH_STREAM=1
```

### Specjalizacja wieloagentowa
```bash
AGENT_MODEL_PRIMARY=phi-4-mini        # Fast for research
AGENT_MODEL_EDITOR=qwen2.5-7b         # Quality for editing
```

### Zdalny rozwój
```bash
FOUNDRY_LOCAL_ENDPOINT=http://dev-server.local:5273/v1
FOUNDRY_LOCAL_ALIAS=phi-4-mini
```

## Rekomendowane modele

### Według zastosowania

**Ogólne przeznaczenie:**
- `phi-4-mini` - Zrównoważona jakość i szybkość

**Szybkie odpowiedzi:**
- `qwen2.5-0.5b` - Bardzo szybki, dobry do klasyfikacji
- `phi-4-mini` - Szybki z dobrą jakością

**Wysoka jakość:**
- `qwen2.5-7b` - Najlepsza jakość, większe zużycie zasobów
- `phi-4-mini` - Dobra jakość, mniejsze zasoby

**Generowanie kodu:**
- `deepseek-coder-1.3b` - Specjalizowany do kodu
- `phi-4-mini` - Ogólne przeznaczenie kodowania

### Według dostępnych zasobów

**Małe zasoby (< 8GB RAM):**
```bash
FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b
SLM_ALIAS=qwen2.5-0.5b
LLM_ALIAS=phi-4-mini
```

**Średnie zasoby (8-16GB RAM):**
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-7b
```

**Duże zasoby (16GB+ RAM):**
```bash
FOUNDRY_LOCAL_ALIAS=qwen2.5-7b
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-14b
```

## Zaawansowana konfiguracja

### Niestandardowe punkty końcowe

```bash
# Development environment
FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Staging environment
FOUNDRY_LOCAL_ENDPOINT=http://staging.internal:5273/v1

# Production environment
FOUNDRY_LOCAL_ENDPOINT=http://prod.internal:5273/v1
```

### Temperatura i próbkowanie (nadpisanie w kodzie)

```python
# In your scripts/notebooks
os.environ['TEMPERATURE'] = '0.7'
os.environ['TOP_P'] = '0.9'
```

### Hybrydowa konfiguracja Azure OpenAI

```bash
# Use local for development
FOUNDRY_LOCAL_ALIAS=phi-4-mini

# Configure Azure for production fallback
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
AZURE_OPENAI_API_KEY=your-key-here
AZURE_OPENAI_API_VERSION=2024-08-01-preview
```

## Rozwiązywanie problemów

### Zmienne środowiskowe nie zostały załadowane

**Objawy:**
- Skrypty używają niewłaściwych modeli
- Błędy połączenia
- Zmienne nie są rozpoznawane

**Rozwiązania:**
```bash
# 1. Verify .env exists in repository root
ls -la .env  # macOS/Linux
dir .env     # Windows

# 2. Check file is not .env.txt (Windows)
# Ensure no hidden extension

# 3. For notebooks: Restart kernel
# Kernel > Restart

# 4. For scripts: Check working directory
pwd  # Should be in Workshop or repository root
```

### Problemy z połączeniem z usługą

**Objawy:**
- Błędy "Connection refused"
- "Usługa niedostępna"
- Błędy timeout

**Rozwiązania:**
```bash
# 1. Check service status
foundry service status

# 2. Start if not running
foundry service start

# 3. Verify endpoint
# Check port in status output
foundry service status | grep "Port"

# 4. Update .env if needed
FOUNDRY_LOCAL_ENDPOINT=http://localhost:<port>
```

### Model nie znaleziony

**Objawy:**
- Błędy "Model not found"
- "Alias nie rozpoznany"

**Rozwiązania:**
```bash
# 1. List available models
foundry model list

# 2. Load required model
foundry model run phi-4-mini

# 3. Update .env with available model
FOUNDRY_LOCAL_ALIAS=<available-model>
```

### Błędy importu

**Objawy:**
- Błędy "Module not found"

**Rozwiązania:**

```bash
# 1. Activate virtual environment
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux

# 2. Install dependencies
pip install -r requirements.txt
```

## Testowanie konfiguracji

### Weryfikacja ładowania środowiska

```python
# test_env.py
import os
from dotenv import load_dotenv

load_dotenv()

print("Core Configuration:")
print(f"  FOUNDRY_LOCAL_ALIAS: {os.getenv('FOUNDRY_LOCAL_ALIAS')}")
print(f"  FOUNDRY_LOCAL_ENDPOINT: {os.getenv('FOUNDRY_LOCAL_ENDPOINT') or 'auto'}")

print("\nSession 04:")
print(f"  SLM_ALIAS: {os.getenv('SLM_ALIAS')}")
print(f"  LLM_ALIAS: {os.getenv('LLM_ALIAS')}")

print("\nSession 05:")
print(f"  AGENT_MODEL_PRIMARY: {os.getenv('AGENT_MODEL_PRIMARY')}")
print(f"  AGENT_MODEL_EDITOR: {os.getenv('AGENT_MODEL_EDITOR')}")
```

### Test połączenia z Foundry Local

```python
# test_connection.py
import os
from foundry_local import FoundryLocalManager

alias = os.getenv('FOUNDRY_LOCAL_ALIAS', 'phi-4-mini')
endpoint = os.getenv('FOUNDRY_LOCAL_ENDPOINT')

try:
    if endpoint:
        manager = FoundryLocalManager(alias, endpoint=endpoint)
    else:
        manager = FoundryLocalManager(alias)
    
    print(f"✓ Connected to {manager.endpoint}")
    print(f"✓ Model: {manager.get_model_info(alias).id}")
    print(f"✓ Available models: {len(manager.list_models())}")
except Exception as e:
    print(f"✗ Connection failed: {e}")
```

## Najlepsze praktyki bezpieczeństwa

### 1. Nigdy nie commituj danych wrażliwych

```bash
# .gitignore should include:
.env
.env.local
*.key
```

### 2. Używaj oddzielnych plików .env

```bash
.env              # Default configuration
.env.local        # Local overrides (gitignored)
.env.production   # Production config (secure storage)
```

### 3. Rotacja kluczy API

```bash
# For Azure OpenAI or other cloud services
# Regularly rotate keys and update .env
```

### 4. Używaj konfiguracji specyficznej dla środowiska

```bash
# Development
FOUNDRY_LOCAL_ENDPOINT=http://localhost:5273/v1

# Production (use secrets management)
FOUNDRY_LOCAL_ENDPOINT=${PROD_FOUNDRY_ENDPOINT}
```

## Dokumentacja SDK

- **Główne repozytorium**: https://github.com/microsoft/Foundry-Local
- **Python SDK**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **Dokumentacja API**: Sprawdź najnowsze informacje w repozytorium SDK

## Dodatkowe zasoby

- `QUICK_START.md` - Przewodnik szybkiego startu
- `SDK_MIGRATION_NOTES.md` - Szczegóły aktualizacji SDK
- `Workshop/samples/*/README.md` - Przewodniki specyficzne dla przykładów

---

**Ostatnia aktualizacja**: 2025-01-08  
**Wersja**: 2.0  
**SDK**: Foundry Local Python SDK (najnowsza)

---

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż staramy się zapewnić dokładność, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za autorytatywne źródło. W przypadku informacji krytycznych zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "85fa559f498492b79de04e391c33687b",
  "translation_date": "2025-10-28T21:43:04+00:00",
  "source_file": "Workshop/Session01-GettingStartedFoundryLocal.md",
  "language_code": "pl"
}
-->
# Sesja 1: Rozpoczęcie pracy z Foundry Local

## Streszczenie

Rozpocznij swoją przygodę z Foundry Local, instalując i konfigurując go na Windows 11. Dowiedz się, jak skonfigurować CLI, włączyć akcelerację sprzętową i buforować modele dla szybkiego lokalnego wnioskowania. Ta praktyczna sesja przeprowadzi Cię przez uruchamianie modeli takich jak Phi, Qwen, DeepSeek i GPT-OSS-20B za pomocą powtarzalnych poleceń CLI.

## Cele nauki

Po zakończeniu tej sesji będziesz w stanie:

- **Zainstalować i skonfigurować**: Ustawić Foundry Local na Windows 11 z optymalnymi ustawieniami wydajności
- **Opanować operacje CLI**: Korzystać z Foundry Local CLI do zarządzania modelami i ich wdrażania
- **Włączyć akcelerację sprzętową**: Skonfigurować akcelerację GPU za pomocą ONNXRuntime lub WebGPU
- **Wdrażać wiele modeli**: Uruchamiać modele phi-4, GPT-OSS-20B, Qwen i DeepSeek lokalnie
- **Zbudować swoją pierwszą aplikację**: Dostosować istniejące przykłady do użycia Foundry Local Python SDK

# Testowanie modelu (pojedynczy prompt bez interakcji)
foundry model run phi-4-mini --prompt "Cześć, przedstaw się"

- Windows 11 (22H2 lub nowszy)
# Lista dostępnych modeli katalogowych (załadowane modele pojawiają się po uruchomieniu)
foundry model list
## NOTE: Obecnie nie ma dedykowanej flagi `--running`; aby zobaczyć, które modele są załadowane, rozpocznij czat lub sprawdź logi serwisu.
- Zainstalowany Python 3.10+
- Visual Studio Code z rozszerzeniem Python
- Uprawnienia administratora do instalacji

### (Opcjonalnie) Zmienne środowiskowe

Utwórz plik `.env` (lub ustaw w powłoce), aby skrypty były przenośne:
# Porównanie odpowiedzi (bez interakcji)
foundry model run gpt-oss-20b --prompt "Wyjaśnij edge AI w prostych słowach"
| Zmienna | Cel | Przykład |
|---------|-----|---------|
| `FOUNDRY_LOCAL_ALIAS` | Preferowany alias modelu (katalog automatycznie wybiera najlepszy wariant) | `phi-3.5-mini` |
| `FOUNDRY_LOCAL_ENDPOINT` | Nadpisanie punktu końcowego (w przeciwnym razie automatycznie z managera) | `http://localhost:5273/v1` |
| `FOUNDRY_LOCAL_STREAM` | Włączenie demonstracji strumieniowania | `true` |

> Jeśli `FOUNDRY_LOCAL_ENDPOINT=auto` (lub nie ustawione), punkt końcowy jest wyprowadzany z managera SDK.

## Przebieg demonstracji (30 minut)

### 1. Instalacja Foundry Local i weryfikacja konfiguracji CLI (10 minut)

# Lista zbuforowanych modeli
foundry cache list

```powershell
# Install via winget (recommended)
winget install Microsoft.FoundryLocal

# Or download from Microsoft Learn
# https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install
```

**macOS (wersja próbna / jeśli obsługiwana)**

Jeśli dostępny jest natywny pakiet macOS (sprawdź oficjalną dokumentację dla najnowszej wersji):

```bash
# Homebrew (if/when available)
brew update
brew install foundry-local  # hypothetical formula name

# Or manual download (tarball)
curl -L -o foundry-local.tar.gz "https://download.microsoft.com/foundry-local/latest/macos/foundry-local.tar.gz"
tar -xzf foundry-local.tar.gz
sudo ./install.sh
```

Jeśli natywne binaria macOS nie są jeszcze dostępne, możesz:
1. Użyć maszyny wirtualnej Windows 11 ARM/Intel (Parallels / UTM) i postępować zgodnie z krokami dla Windows.
2. Uruchomić modele za pomocą kontenera (jeśli obraz kontenera jest opublikowany) i ustawić `FOUNDRY_LOCAL_ENDPOINT` na otwarty port.

**Tworzenie wirtualnego środowiska Python (platforma wielosystemowa)**

Windows PowerShell:
```powershell
py -m venv .venv
 .\.venv\Scripts\Activate.ps1
```

macOS / Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

Aktualizacja pip i instalacja podstawowych zależności:
```bash
python -m pip install --upgrade pip
pip install foundry-local-sdk openai
```

#### Krok 1.2: Weryfikacja instalacji

```powershell
# Check version
foundry --version

# Initialize configuration
foundry init

# View available commands
foundry --help
```

#### Krok 1.3: Konfiguracja środowiska

```powershell
# Set up Python environment for Module08
cd Module08
py -m venv .venv
.\.venv\Scripts\activate

# Install Foundry Local Python SDK and dependencies
pip install foundry-local-sdk openai requests
```

### Bootstrapping SDK (zalecane)

Zamiast ręcznego uruchamiania serwisu i modeli, **Foundry Local Python SDK** może automatycznie uruchomić wszystko:

```python
from foundry_local import FoundryLocalManager
from openai import OpenAI
import os

alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-3.5-mini")

# Bootstraps service + downloads + loads most suitable variant for hardware
manager = FoundryLocalManager(alias)

print("Service running:", manager.is_service_running())
print("Endpoint:", manager.endpoint)
print("Cached models:", manager.list_cached_models())

client = OpenAI(base_url=manager.endpoint, api_key=manager.api_key or "not-needed")

resp = client.chat.completions.create(
    model=manager.get_model_info(alias).id,
    messages=[
        {"role": "system", "content": "You are a helpful local assistant."},
        {"role": "user", "content": "Hello"}
    ],
    max_tokens=120,
    temperature=0.5
)
print(resp.choices[0].message.content)
```

Jeśli wolisz mieć pełną kontrolę, nadal możesz używać CLI + klienta OpenAI, jak pokazano później.

### 2. Uruchamianie modeli lokalnie za pomocą CLI (10 minut)

#### Krok 3.1: Wdrażanie modelu Phi-4

```powershell
# Download and run phi-4-mini
foundry model run phi-4-mini

# Test the model (one-shot prompt)
foundry model run phi-4-mini --prompt "Hello, introduce yourself"

# NOTE: There is no `--running` flag; use `foundry model list` and recent activity to infer loaded models.
```

#### Krok 3.2: Wdrażanie GPT-OSS-20B

```powershell
# Download and run GPT-OSS-20B
foundry model run gpt-oss-20b

# Compare responses (one-shot prompt)
foundry model run gpt-oss-20b --prompt "Explain edge AI in simple terms"
```

#### Krok 3.3: Ładowanie dodatkowych modeli

```powershell
# Download Qwen model family
foundry model download qwen2.5-0.5b
foundry model download qwen2.5-7b

# Download DeepSeek models
foundry model download deepseek-coder-1.3b

# List cached models
foundry cache list
```

### 4. Projekt startowy: Dostosowanie 01-run-phi do Foundry Local (5 minut)

#### Krok 4.1: Tworzenie podstawowej aplikacji czatu

Utwórz `samples/01-foundry-quickstart/chat_quickstart.py` (zaktualizowane do użycia managera, jeśli dostępny):

```python
#!/usr/bin/env python3
"""
Foundry Local Chat Quickstart
Demo: Basic chat interaction using Foundry Local Python SDK
Reference: https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/reference/reference-sdk?pivots=programming-language-python
"""

import os, sys
from openai import OpenAI
try:
    from foundry_local import FoundryLocalManager  # control-plane SDK
except ImportError:
    FoundryLocalManager = None

def main():
    """Main chat function using Foundry Local SDK"""
    
    # Preferred: bootstrap via SDK manager (auto start + download + load)
    alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-3.5-mini")
    if FoundryLocalManager:
        manager = FoundryLocalManager(alias)
        endpoint = manager.endpoint
        model_id = manager.get_model_info(alias).id
        api_key = manager.api_key or "not-needed"
    else:
        # Fallback: assume default endpoint & alias already running via CLI
        endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT", "http://localhost:5273/v1")
        model_id = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-4-mini")
        api_key = "not-needed"

    client = OpenAI(base_url=endpoint, api_key=api_key)
    
    # Get user input
    if len(sys.argv) > 1:
        user_message = " ".join(sys.argv[1:])
    else:
        user_message = input("Enter your message: ")
    
    try:
        # Make chat completion request
        response = client.chat.completions.create(
            model=model_id,
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant powered by Microsoft Foundry Local."},
                {"role": "user", "content": user_message}
            ],
            max_tokens=500,
            temperature=0.7
        )
        
        # Display response
        print(f"\nModel: {response.model}")
        print(f"Response: {response.choices[0].message.content}")
        print(f"Tokens used: {response.usage.total_tokens if response.usage else 'N/A'}")
        
    except Exception as e:
        print(f"Error: {e}")
        print("\nTroubleshooting:")
    print("1. Ensure Foundry Local is running: foundry status")
    print("2. List models: foundry model list")
    print(f"3. Start model if needed: foundry model run {model_id}")
    print("4. Or let SDK bootstrap: pip install foundry-local-sdk")

if __name__ == "__main__":
    main()
```

#### Krok 4.2: Testowanie aplikacji

```powershell
# Ensure phi-4-mini is running
foundry model run phi-4-mini

# Run the quickstart app
python samples/01-foundry-quickstart/chat_quickstart.py "What is Microsoft Foundry Local?"

# Try interactive mode
python samples/01-foundry-quickstart/chat_quickstart.py
```

## Kluczowe pojęcia omówione

### 1. Architektura Foundry Local

- **Silnik wnioskowania lokalnego**: Uruchamia modele całkowicie na Twoim urządzeniu
- **Kompatybilność z OpenAI SDK**: Bezproblemowa integracja z istniejącym kodem OpenAI
- **Zarządzanie modelami**: Pobieranie, buforowanie i efektywne uruchamianie wielu modeli
- **Optymalizacja sprzętowa**: Wykorzystanie akceleracji GPU, NPU i CPU

### 2. Odniesienie do poleceń CLI

```powershell
# Core Commands
foundry --version              # Check installation
# Model Management
foundry model list             # List available models
foundry model unload <name>    # Unload from memory

foundry config list            # Current configuration
```

### 3. Integracja Python SDK

```python
# Basic client setup
from foundry_local import FoundryLocalManager
from openai import OpenAI
import os

alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-3.5-mini")
manager = FoundryLocalManager(alias)
client = OpenAI(base_url=manager.endpoint, api_key=manager.api_key or "not-needed")

response = client.chat.completions.create(
    model=manager.get_model_info(alias).id,
    messages=[{"role": "user", "content": "Hello!"}],
    max_tokens=50
)
print(response.choices[0].message.content)

# Streaming example
stream = client.chat.completions.create(
    model=manager.get_model_info(alias).id,
    messages=[{"role": "user", "content": "Give a 1-sentence definition of edge AI."}],
    stream=True,
    max_tokens=60,
    temperature=0.4
)
for chunk in stream:
    delta = chunk.choices[0].delta
    if delta and delta.content:
        print(delta.content, end="", flush=True)
print()
```

## Rozwiązywanie typowych problemów

### Problem 1: "Nie znaleziono polecenia Foundry"

**Rozwiązanie:**
```powershell
# Restart PowerShell after installation
# Or manually add to PATH
$env:PATH += ";C:\Program Files\Microsoft\FoundryLocal"
```

### Problem 2: "Nie udało się załadować modelu"

**Rozwiązanie:**
```powershell
# Check available memory
foundry system info

# Try smaller model first
foundry model run phi-4-mini

# Check disk space for model cache
dir "$env:USERPROFILE\.foundry\models"
```

### Problem 3: "Odmowa połączenia na localhost:5273"

**Rozwiązanie:**
```powershell
# Check if service is running
foundry status

# Start service if needed
foundry service start

# Check for port conflicts
netstat -an | findstr 5273
```

## Wskazówki dotyczące optymalizacji wydajności

### 1. Strategia wyboru modelu

- **Phi-4-mini**: Najlepszy do ogólnych zadań, mniejsze zużycie pamięci
- **Qwen2.5-0.5b**: Najszybsze wnioskowanie, minimalne zasoby
- **GPT-OSS-20B**: Najwyższa jakość, wymaga więcej zasobów
- **DeepSeek-Coder**: Optymalizowany do zadań programistycznych

### 2. Optymalizacja sprzętowa

```powershell
# Enable all acceleration options
foundry config set compute.onnx.enable_gpu true
foundry config set compute.webgpu.enabled true
foundry config set compute.cpu.threads auto

# Optimize memory usage
foundry config set model.cache.max_size 10GB
foundry config set model.preload false
```

### 3. Monitorowanie wydajności

```powershell
cd Workshop/samples
# Performance & latency measurement
# Use the Python benchmark script (Session 3) instead of legacy 'model stats' or 'model benchmark' commands.
# Example:
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
python -m session03.benchmark_oss_models

# Re-run after enabling GPU acceleration to compare:
foundry config set compute.onnx.enable_gpu true
python -m session03.benchmark_oss_models
```

### Opcjonalne ulepszenia

| Ulepszenie | Co | Jak |
|------------|----|-----|
| Wspólne narzędzia | Usunięcie powtarzającej się logiki klienta/bootstrappingu | Użyj `Workshop/samples/workshop_utils.py` (`get_client`, `chat_once`) |
| Widoczność użycia tokenów | Nauka myślenia o kosztach/efektywności | Ustaw `SHOW_USAGE=1`, aby wyświetlić prompt/kompletację/całkowitą liczbę tokenów |
| Deterministyczne porównania | Stabilne testy wydajności i regresji | Użyj `temperature=0`, `top_p=1`, spójny tekst promptu |
| Opóźnienie pierwszego tokena | Metryka postrzeganej responsywności | Dostosuj skrypt testowy ze strumieniowaniem (`BENCH_STREAM=1`) |
| Ponowne próby przy błędach przejściowych | Odporne demonstracje przy zimnym starcie | `RETRY_ON_FAIL=1` (domyślnie) i dostosuj `RETRY_BACKOFF` |
| Testowanie dymne | Szybka kontrola kluczowych funkcji | Uruchom `python Workshop/tests/smoke.py` przed warsztatem |
| Profile aliasów modelu | Szybkie przełączanie zestawu modeli między maszynami | Utrzymuj `.env` z `FOUNDRY_LOCAL_ALIAS`, `SLM_ALIAS`, `LLM_ALIAS` |
| Efektywność buforowania | Unikaj powtarzających się rozgrzewek w wielokrotnym uruchamianiu próbek | Narzędzia do zarządzania buforowaniem; ponowne użycie w skryptach/notatnikach |
| Rozgrzewka przy pierwszym uruchomieniu | Redukcja skoków opóźnienia p95 | Wyślij mały prompt po utworzeniu `FoundryLocalManager`

Przykład deterministycznej rozgrzewki (PowerShell):

```powershell
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
python Workshop\samples\session01\chat_bootstrap.py "List two privacy benefits of local inference." | Out-Null
python Workshop\samples\session01\chat_bootstrap.py "List two privacy benefits of local inference."
```

Powinieneś zobaczyć podobny wynik i identyczną liczbę tokenów przy drugim uruchomieniu, co potwierdza deterministyczność.

## Kolejne kroki

Po ukończeniu tej sesji:

1. **Odkryj Sesję 2**: Tworzenie rozwiązań AI z Azure AI Foundry RAG
2. **Wypróbuj różne modele**: Eksperymentuj z Qwen, DeepSeek i innymi rodzinami modeli
3. **Optymalizuj wydajność**: Dostosuj ustawienia do swojego sprzętu
4. **Twórz własne aplikacje**: Wykorzystaj Foundry Local SDK w swoich projektach

## Dodatkowe zasoby

### Dokumentacja
- [Foundry Local Python SDK Reference](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/reference/reference-sdk?pivots=programming-language-python)
- [Foundry Local Installation Guide](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install)
- [Model Catalog](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/models)

### Przykładowy kod
- [Module08 Sample 01](./samples/01/README.md) - REST Chat Quickstart
- [Module08 Sample 02](./samples/02/README.md) - OpenAI SDK Integration
- [Module08 Sample 03](./samples/03/README.md) - Model Discovery & Benchmarking

### Społeczność
- [Foundry Local GitHub Discussions](https://github.com/microsoft/Foundry-Local/discussions)
- [Azure AI Community](https://techcommunity.microsoft.com/category/artificialintelligence)

---

**Czas trwania sesji**: 30 minut praktyki + 15 minut Q&A  
**Poziom trudności**: Początkujący  
**Wymagania wstępne**: Windows 11, Python 3.10+, dostęp administratora  

## Przykładowy scenariusz i mapowanie warsztatów

| Skrypt warsztatowy / Notatnik | Scenariusz | Cel | Przykładowe dane wejściowe | Wymagany zestaw danych |
|-------------------------------|------------|-----|----------------------------|------------------------|
| `samples/session01/chat_bootstrap.py` / `notebooks/session01_chat_bootstrap.ipynb` | Wewnętrzny zespół IT oceniający wnioskowanie na urządzeniu dla portalu oceny prywatności | Udowodnij, że lokalny SLM odpowiada z opóźnieniem poniżej sekundy na standardowe prompty | "Wymień dwie korzyści z wnioskowania lokalnego." | Brak (pojedynczy prompt) |
| Kod adaptacji Quickstart | Programista migrujący istniejący skrypt OpenAI do Foundry Local | Pokaż kompatybilność "drop-in" | "Podaj dwie korzyści z wnioskowania lokalnego." | Tylko prompt w linii |

### Narracja scenariusza
Zespół ds. bezpieczeństwa i zgodności musi zweryfikować, czy wrażliwe dane prototypowe mogą być przetwarzane lokalnie. Uruchamiają skrypt bootstrappingu z kilkoma promptami (prywatność, opóźnienie, koszty) używając deterministycznego trybu temperature=0, aby uchwycić wyniki bazowe do późniejszego porównania (benchmarking w Sesji 3 i kontrast SLM vs LLM w Sesji 4).

### Minimalny zestaw promptów w formacie JSON (opcjonalnie)
```json
[
    "List two benefits of local inference.",
    "Summarize why keeping data on device improves privacy.",
    "Give one trade‑off when choosing an SLM over a large model."
]
```

Użyj tej listy, aby stworzyć powtarzalną pętlę oceny lub zasilić przyszły mechanizm testów regresji.

---

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż staramy się zapewnić dokładność, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za autorytatywne źródło. W przypadku informacji krytycznych zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
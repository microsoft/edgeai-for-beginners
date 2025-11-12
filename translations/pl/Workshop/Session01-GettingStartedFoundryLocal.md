<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8c30436578b1bd604c48233ecdd39701",
  "translation_date": "2025-11-11T22:54:18+00:00",
  "source_file": "Workshop/Session01-GettingStartedFoundryLocal.md",
  "language_code": "pl"
}
-->
# Sesja 1: Rozpoczęcie pracy z Foundry Local

## Streszczenie

Naucz się instalować, konfigurować i uruchamiać swoje pierwsze modele AI za pomocą Microsoft Foundry Local. Ta praktyczna sesja oferuje krok po kroku wprowadzenie do lokalnego wnioskowania, od instalacji po stworzenie pierwszej aplikacji czatu z wykorzystaniem modeli takich jak Phi-4, Qwen i DeepSeek.

## Cele nauki

Po zakończeniu tej sesji będziesz w stanie:

- **Zainstalować i skonfigurować**: Skonfigurować Foundry Local z odpowiednią weryfikacją instalacji
- **Opanować operacje CLI**: Korzystać z Foundry Local CLI do zarządzania modelami i ich wdrażania
- **Uruchomić swój pierwszy model**: Pomyślnie wdrożyć i interaktywnie korzystać z lokalnego modelu AI
- **Zbudować aplikację czatu**: Stworzyć podstawową aplikację czatu za pomocą Foundry Local Python SDK
- **Zrozumieć lokalne AI**: Poznać podstawy lokalnego wnioskowania i zarządzania modelami

## Wymagania wstępne

### Wymagania systemowe

- **Windows**: Windows 11 (22H2 lub nowszy) LUB **macOS**: macOS 11+ (ograniczone wsparcie)
- **RAM**: Minimum 8GB, zalecane 16GB+
- **Pamięć**: Minimum 10GB wolnego miejsca na modele
- **Python**: Zainstalowany Python 3.10 lub nowszy
- **Dostęp administracyjny**: Uprawnienia administratora do instalacji

### Środowisko programistyczne

- Visual Studio Code z rozszerzeniem Python (zalecane)
- Dostęp do wiersza poleceń (PowerShell na Windows, Terminal na macOS)
- Git do klonowania repozytoriów (opcjonalnie)

## Przebieg warsztatu (30 minut)

### Krok 1: Instalacja Foundry Local (5 minut)

#### Instalacja na Windows

Zainstaluj Foundry Local za pomocą menedżera pakietów Windows:

```powershell
# Install via winget (recommended)
winget install Microsoft.FoundryLocal
```

Alternatywnie: Pobierz bezpośrednio z [Microsoft Learn](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install)

#### Instalacja na macOS (ograniczone wsparcie)

> [!NOTE]  
> Wsparcie dla macOS jest obecnie w wersji preview. Sprawdź oficjalną dokumentację, aby uzyskać najnowsze informacje.

Jeśli dostępne, zainstaluj za pomocą Homebrew:

```bash
# If Homebrew formula is available
brew update
brew install foundry-local

# Or manual download (check official docs for latest)
curl -L -o foundry-local.tar.gz "https://download.microsoft.com/foundry-local/latest/macos/foundry-local.tar.gz"
tar -xzf foundry-local.tar.gz
sudo ./install.sh
```

**Alternatywa dla użytkowników macOS:**
- Użyj maszyny wirtualnej Windows 11 (Parallels/UTM) i postępuj zgodnie z krokami dla Windows
- Uruchom za pomocą kontenera, jeśli dostępne, i skonfiguruj `FOUNDRY_LOCAL_ENDPOINT`

### Krok 2: Weryfikacja instalacji (3 minuty)

Po instalacji, uruchom ponownie terminal i sprawdź, czy Foundry Local działa:

```powershell
# Check if Foundry Local is installed correctly
foundry --version

# View available commands
foundry --help
```

Oczekiwany wynik powinien pokazać informacje o wersji i dostępne polecenia.

### Krok 3: Konfiguracja środowiska Python (5 minut)

Utwórz dedykowane środowisko Python dla tego warsztatu:

**Windows:**
```powershell
# Create virtual environment
py -m venv .venv

# Activate environment
.\.venv\Scripts\Activate.ps1

# Upgrade pip and install dependencies
python -m pip install --upgrade pip
pip install foundry-local-sdk openai
```

**macOS/Linux:**
```bash
# Create virtual environment
python3 -m venv .venv

# Activate environment
source .venv/bin/activate

# Upgrade pip and install dependencies
python -m pip install --upgrade pip
pip install foundry-local-sdk openai
```


### Krok 4: Uruchom swój pierwszy model (7 minut)

Teraz uruchomimy nasz pierwszy model AI lokalnie!

#### Rozpocznij od Phi-4 Mini (zalecany pierwszy model)

```powershell
# Download and start phi-4-mini (lightweight, fast)
foundry model run phi-4-mini

# Test the model with a simple prompt
foundry model run phi-4-mini --prompt "Hello, introduce yourself in one sentence"
```

> [!TIP]  
> To polecenie pobiera model (pierwszy raz) i automatycznie uruchamia usługę Foundry Local.

#### Sprawdź, co działa

```powershell
# List available models (shows downloaded models)
foundry model list

# Check service status
foundry service status

# See what models are cached locally
foundry cache list
```


#### Wypróbuj różne modele

Gdy phi-4-mini działa, eksperymentuj z innymi modelami:

```powershell
# Larger model with better capabilities
foundry model run gpt-oss-20b --prompt "Explain edge AI in simple terms"

# Fast, efficient model
foundry model run qwen2.5-0.5b --prompt "What are the benefits of local AI inference?"
```


### Krok 5: Zbuduj swoją pierwszą aplikację czatu (10 minut)

Teraz stworzymy aplikację Python, która korzysta z modeli, które właśnie uruchomiliśmy.

#### Utwórz skrypt czatu

Utwórz nowy plik o nazwie `my_first_chat.py` (lub użyj dostarczonego przykładu):

```python
#!/usr/bin/env python3
"""
My First Foundry Local Chat Application
Using FoundryLocalManager for automatic service management
"""

import os
from foundry_local import FoundryLocalManager
from openai import OpenAI

def main():
    # Get model alias from environment or use default
    alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-4-mini")
    
    try:
        # Initialize Foundry Local Manager (auto-starts service, downloads model)
        manager = FoundryLocalManager(alias)
        
        # Create OpenAI client pointing to local endpoint
        client = OpenAI(
            base_url=manager.endpoint,
            api_key=manager.api_key or "not-needed"
        )
        
        # Get the actual model ID for this alias
        model_id = manager.get_model_info(alias).id
        
        print("🤖 Welcome to your first local AI chat!")
        print(f"� Using model: {alias} -> {model_id}")
        print(f"🌐 Endpoint: {manager.endpoint}")
        print("�💡 Type 'quit' to exit\n")
        
    except Exception as e:
        print(f"❌ Failed to initialize Foundry Local: {e}")
        print("💡 Make sure Foundry Local is installed: foundry --version")
        return
    
    while True:
        # Get user input
        user_message = input("You: ").strip()
        
        if user_message.lower() in ['quit', 'exit', 'bye']:
            print("👋 Goodbye!")
            break
            
        if not user_message:
            continue
            
        try:
            # Send message to local AI model
            response = client.chat.completions.create(
                model=model_id,
                messages=[
                    {"role": "system", "content": "You are a helpful AI assistant running locally."},
                    {"role": "user", "content": user_message}
                ],
                max_tokens=200,
                temperature=0.7
            )
            
            # Display the response
            ai_response = response.choices[0].message.content
            print(f"🤖 AI: {ai_response}\n")
            
        except Exception as e:
            print(f"❌ Error: {e}")
            print("💡 Check service status: foundry service status\n")

if __name__ == "__main__":
    main()
```

> [!TIP]  
> **Powiązane przykłady**: Aby uzyskać bardziej zaawansowane zastosowania, zobacz:
>
> - **Przykład Python**: `Workshop/samples/session01/chat_bootstrap.py` - Zawiera odpowiedzi strumieniowe i obsługę błędów
> - **Notebook Jupyter**: `Workshop/notebooks/session01_chat_bootstrap.ipynb` - Interaktywna wersja z szczegółowymi wyjaśnieniami

#### Przetestuj swoją aplikację czatu

```powershell
# No need to manually start models - FoundryLocalManager handles this!
# Just run your chat application
python my_first_chat.py
```

Alternatywnie: Użyj bezpośrednio dostarczonych przykładów

```powershell
# Try the complete sample with streaming support
cd Workshop/samples
python -m session01.chat_bootstrap "Your question here"
```

Lub eksploruj interaktywny notebook  
Otwórz Workshop/notebooks/session01_chat_bootstrap.ipynb w VS Code

Wypróbuj te przykładowe rozmowy:

- "Co to jest Microsoft Foundry Local?"
- "Wymień 3 korzyści z uruchamiania modeli AI lokalnie"
- "Pomóż mi zrozumieć edge AI"

## Co osiągnąłeś

Gratulacje! Pomyślnie:

1. ✅ **Zainstalowałeś Foundry Local** i zweryfikowałeś jego działanie
2. ✅ **Uruchomiłeś swój pierwszy model AI** (phi-4-mini) lokalnie
3. ✅ **Przetestowałeś różne modele** za pomocą wiersza poleceń
4. ✅ **Zbudowałeś aplikację czatu**, która łączy się z lokalnym AI
5. ✅ **Doświadczyłeś lokalnego wnioskowania AI** bez zależności od chmury

## Zrozumienie, co się wydarzyło

### Lokalne wnioskowanie AI

- Twoje modele AI działają całkowicie na Twoim komputerze
- Żadne dane nie są wysyłane do chmury
- Odpowiedzi są generowane lokalnie za pomocą Twojego CPU/GPU
- Prywatność i bezpieczeństwo są zachowane

### Zarządzanie modelami

- `foundry model run` pobiera i uruchamia modele
- **FoundryLocalManager SDK** automatycznie obsługuje uruchamianie usług i ładowanie modeli
- Modele są przechowywane lokalnie do przyszłego użytku
- Można pobrać wiele modeli, ale zazwyczaj działa jeden na raz
- Usługa automatycznie zarządza cyklem życia modelu

### Podejście SDK vs CLI

- **Podejście CLI**: Ręczne zarządzanie modelami za pomocą `foundry model run <model>`
- **Podejście SDK**: Automatyczne zarządzanie usługami i modelami za pomocą `FoundryLocalManager(alias)`
- **Rekomendacja**: Używaj SDK do aplikacji, CLI do testowania i eksploracji

## Referencje do poleceń

### Podstawowe polecenia CLI

```powershell
# Installation & Setup
foundry --version              # Check installation
foundry --help                 # View all commands

# Model Management
foundry model list             # List available models
foundry model run <model>      # Download and start a model
foundry model run <model> --prompt "text"  # One-shot prompt
foundry cache list             # Show downloaded models

# Service Management
foundry service status         # Check if service is running
foundry service start          # Start the service manually
foundry service stop           # Stop the service
```


### Rekomendacje modeli

- **phi-4-mini**: Najlepszy model startowy - szybki, lekki, dobra jakość
- **qwen2.5-0.5b**: Najszybsze wnioskowanie, minimalne zużycie pamięci
- **gpt-oss-20b**: Wyższa jakość odpowiedzi, wymaga więcej zasobów
- **deepseek-coder-1.3b**: Optymalizowany do programowania i zadań związanych z kodem

## Rozwiązywanie problemów

### "Polecenie Foundry nie zostało znalezione"

**Rozwiązanie:**

```powershell
# Restart your terminal after installation
# Or manually add to PATH (Windows)
$env:PATH += ";C:\Program Files\Microsoft\FoundryLocal"
```


### "Model nie załadował się"

**Rozwiązanie:**

```powershell
# Check available system memory
foundry service status

# Try a smaller model first
foundry model run phi-4-mini

# Check disk space for model downloads
# Models are stored in: %USERPROFILE%\.foundry\models (Windows)
```


### "Połączenie odrzucone na localhost"

**Rozwiązanie:**

```powershell
# Check if service is running
foundry service status

# Start service if needed
foundry service start

# Verify the port (default is 5273)
# Check for port conflicts with: netstat -an | findstr 5273
```


## Kolejne kroki

### Natychmiastowe działania

1. **Eksperymentuj** z różnymi modelami i zapytaniami
2. **Modyfikuj** swoją aplikację czatu, aby wypróbować różne modele
3. **Twórz** własne zapytania i testuj odpowiedzi
4. **Eksploruj** Sesję 2: Budowanie aplikacji RAG

### Zaawansowana ścieżka nauki

1. **Sesja 2**: Budowanie rozwiązań AI z RAG (Retrieval-Augmented Generation)
2. **Sesja 3**: Porównanie różnych modeli open-source
3. **Sesja 4**: Praca z najnowocześniejszymi modelami
4. **Sesja 5**: Budowanie systemów AI z wieloma agentami

## Zmienne środowiskowe (opcjonalne)

Dla bardziej zaawansowanego użycia możesz ustawić te zmienne środowiskowe:

| Zmienna | Cel | Przykład |
|---------|-----|---------|
| `FOUNDRY_LOCAL_ALIAS` | Domyślny model do użycia | `phi-4-mini` |
| `FOUNDRY_LOCAL_ENDPOINT` | Nadpisanie URL punktu końcowego | `http://localhost:5273/v1` |

Utwórz plik `.env` w katalogu projektu:
```
FOUNDRY_LOCAL_ALIAS=phi-4-mini
FOUNDRY_LOCAL_ENDPOINT=auto
```


## Dodatkowe zasoby

### Dokumentacja

- [Foundry Local Python SDK Reference](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/reference/reference-sdk?pivots=programming-language-python)
- [Foundry Local Installation Guide](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install)
- [Model Catalog](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/models)

### Przykładowy kod

- **Przykład Python Sesja01**: `Workshop/samples/session01/chat_bootstrap.py` - Kompletny czat z odpowiedziami strumieniowymi
- **Notebook Sesja01**: `Workshop/notebooks/session01_chat_bootstrap.ipynb` - Interaktywny tutorial  
- [Przykład Moduł08 01](../Module08/samples/01/README.md) - Szybki start REST Chat
- [Przykład Moduł08 02](../Module08/samples/02/README.md) - Integracja OpenAI SDK
- [Przykład Moduł08 03](../Module08/samples/03/README.md) - Odkrywanie modeli i benchmarking

### Społeczność

- [Foundry Local GitHub Discussions](https://github.com/microsoft/Foundry-Local/discussions)
- [Azure AI Community](https://techcommunity.microsoft.com/category/artificialintelligence)

---

**Czas trwania sesji**: 30 minut praktyki + 15 minut Q&A  
**Poziom trudności**: Początkujący  
**Wymagania wstępne**: Windows 11/macOS 11+, Python 3.10+, dostęp administracyjny

## Przykładowy scenariusz warsztatu

### Kontekst rzeczywisty

**Scenariusz**: Zespół IT w przedsiębiorstwie musi ocenić wnioskowanie AI na urządzeniu w celu przetwarzania poufnych opinii pracowników bez wysyłania danych do zewnętrznych usług.

**Twój cel**: Zademonstrować, że lokalne modele AI mogą dostarczać odpowiedzi wysokiej jakości z opóźnieniem poniżej sekundy, jednocześnie zachowując pełną prywatność danych.

### Przykładowe zapytania

Użyj tych zapytań, aby zweryfikować swoją konfigurację:

```json
[
    "List two benefits of local inference.",
    "Summarize why keeping data on device improves privacy.",
    "Give one trade-off when choosing a small model over a large model."
]
```


### Kryteria sukcesu

- ✅ Wszystkie zapytania otrzymują odpowiedzi w czasie poniżej 2 sekund
- ✅ Żadne dane nie opuszczają Twojego lokalnego komputera
- ✅ Odpowiedzi są trafne i pomocne
- ✅ Twoja aplikacja czatu działa płynnie

Ta weryfikacja zapewnia, że Twoja konfiguracja Foundry Local jest gotowa na zaawansowane warsztaty w Sesjach 2-6.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż staramy się zapewnić dokładność, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za wiarygodne źródło. W przypadku informacji krytycznych zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
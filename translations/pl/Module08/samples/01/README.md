# Przykład 01: Szybki czat za pomocą OpenAI SDK

Prosty przykład czatu pokazujący, jak korzystać z OpenAI SDK w połączeniu z Microsoft Foundry Local do lokalnego wnioskowania AI.

## Przegląd

Ten przykład pokazuje, jak:
- Korzystać z OpenAI Python SDK z Foundry Local
- Obsługiwać konfiguracje zarówno Azure OpenAI, jak i lokalne Foundry
- Zaimplementować odpowiednie obsługi błędów i strategie awaryjne
- Używać FoundryLocalManager do zarządzania usługami

## Wymagania wstępne

- **Foundry Local**: Zainstalowany i dostępny w PATH
- **Python**: Wersja 3.8 lub nowsza
- **Model**: Model załadowany w Foundry Local (np. `phi-4-mini`)

## Instalacja

1. **Skonfiguruj środowisko Python:**
   ```cmd
   cd Module08
   py -m venv .venv
   .venv\Scripts\activate
   ```

2. **Zainstaluj zależności:**
   ```cmd
   pip install -r requirements.txt
   ```

3. **Uruchom usługę Foundry Local i załaduj model:**
   ```cmd
   foundry model run phi-4-mini
   ```


## Użycie

### Foundry Local (Domyślnie)

```cmd
# Using FoundryLocalManager (recommended)
python samples\01\chat_quickstart.py "Explain what Foundry Local is"

# Using manual configuration
set BASE_URL=http://localhost:8000
set MODEL=phi-4-mini
set API_KEY=
python samples\01\chat_quickstart.py "Write a welcome message"
```

### Azure OpenAI

```cmd
set AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
set AZURE_OPENAI_API_KEY=your-api-key
set AZURE_OPENAI_API_VERSION=2024-08-01-preview
set MODEL=your-deployment-name
python samples\01\chat_quickstart.py "Hello from Azure OpenAI"
```


## Funkcje kodu

### Integracja z FoundryLocalManager

Przykład korzysta z oficjalnego Foundry Local SDK do właściwego zarządzania usługami:

```python
from foundry_local import FoundryLocalManager
from openai import OpenAI

# Initialize Foundry Local
manager = FoundryLocalManager(alias)
model_info = manager.get_model_info(alias)

# Configure OpenAI client
client = OpenAI(
    base_url=manager.endpoint,
    api_key=manager.api_key
)
```


### Obsługa błędów

Solidna obsługa błędów z możliwością przejścia na ręczną konfigurację:
- Automatyczne wykrywanie usług
- Łagodne przejście w przypadku braku SDK
- Jasne komunikaty o błędach ułatwiające rozwiązywanie problemów

## Zmienne środowiskowe

| Zmienna | Opis | Domyślna wartość | Wymagana |
|---------|------|------------------|----------|
| `MODEL` | Alias lub nazwa modelu | `phi-4-mini` | Nie |
| `BASE_URL` | Podstawowy URL Foundry Local | `http://localhost:8000` | Nie |
| `API_KEY` | Klucz API (zwykle niepotrzebny lokalnie) | `""` | Nie |
| `AZURE_OPENAI_ENDPOINT` | Endpoint Azure OpenAI | - | Dla Azure |
| `AZURE_OPENAI_API_KEY` | Klucz API Azure OpenAI | - | Dla Azure |
| `AZURE_OPENAI_API_VERSION` | Wersja API Azure | `2024-08-01-preview` | Nie |

## Rozwiązywanie problemów

### Typowe problemy

1. **Ostrzeżenie "Nie można użyć Foundry SDK":**
   - Zainstaluj foundry-local-sdk: `pip install foundry-local-sdk`
   - Lub ustaw zmienne środowiskowe dla ręcznej konfiguracji

2. **Odmowa połączenia:**
   - Upewnij się, że Foundry Local działa: `foundry service status`
   - Sprawdź, czy model jest załadowany: `foundry service ps`

3. **Model nie znaleziony:**
   - Wyświetl dostępne modele: `foundry model list`
   - Załaduj model: `foundry model run phi-4-mini`

### Weryfikacja

```cmd
# Check Foundry Local status
foundry service status

# List loaded models
foundry service ps

# Test API endpoint
curl http://localhost:8000/v1/models
```


## Odnośniki

- [Dokumentacja Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [OpenAI Python SDK](https://github.com/openai/openai-python)
- [Foundry Local na GitHub](https://github.com/microsoft/Foundry-Local)
- [Referencja API kompatybilnego z OpenAI](https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks)

---


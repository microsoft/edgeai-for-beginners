# Przykład 02: Integracja z OpenAI SDK

Pokazuje zaawansowaną integrację z OpenAI Python SDK, obsługując zarówno Microsoft Foundry Local, jak i Azure OpenAI, z odpowiedziami strumieniowymi oraz właściwym zarządzaniem błędami.

## Przegląd

Ten przykład demonstruje:
- Płynne przełączanie między Foundry Local a Azure OpenAI
- Strumieniowe uzupełnianie czatu dla lepszego doświadczenia użytkownika
- Właściwe wykorzystanie FoundryLocalManager SDK
- Solidne mechanizmy obsługi błędów i awaryjnego przełączania
- Wzorce kodu gotowe do produkcji

## Wymagania wstępne

- **Foundry Local**: Zainstalowany i uruchomiony (do lokalnego wnioskowania)
- **Python**: Wersja 3.8 lub nowsza z OpenAI SDK
- **Azure OpenAI**: Ważny punkt końcowy i klucz API (do wnioskowania w chmurze)

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

3. **Uruchom Foundry Local (dla trybu lokalnego):**
   ```cmd
   foundry model run phi-4-mini
   ```


## Scenariusze użycia

### Foundry Local (Domyślnie)

**Opcja 1: Korzystanie z FoundryLocalManager (Zalecane)**
```cmd
# Automatic service discovery and model management
set MODEL=phi-4-mini
python samples\02\sdk_quickstart.py
```

**Opcja 2: Ręczna konfiguracja**
```cmd
# Manual endpoint configuration
set BASE_URL=http://localhost:8000
set MODEL=phi-4-mini
set API_KEY=
python samples\02\sdk_quickstart.py
```


### Azure OpenAI

```cmd
# Azure OpenAI configuration
set AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
set AZURE_OPENAI_API_KEY=your-api-key
set AZURE_OPENAI_API_VERSION=2024-08-01-preview
set MODEL=your-deployment-name
python samples\02\sdk_quickstart.py
```


## Architektura kodu

### Wzorzec fabryki klienta

Przykład wykorzystuje wzorzec fabryki do tworzenia odpowiednich klientów:

```python
def create_foundry_client():
    """Create Foundry Local client with SDK management."""
    manager = FoundryLocalManager(alias)
    client = OpenAI(
        base_url=manager.endpoint,
        api_key=manager.api_key
    )
    return client, manager.get_model_info(alias).id

def create_azure_client():
    """Create Azure OpenAI client."""
    client = OpenAI(
        base_url=f"{endpoint}/openai",
        api_key=api_key,
        default_query={"api-version": api_version}
    )
    return client, model
```


### Odpowiedzi strumieniowe

Przykład demonstruje strumieniowanie dla generowania odpowiedzi w czasie rzeczywistym:

```python
stream = client.chat.completions.create(
    model=model,
    messages=[{"role": "user", "content": prompt}],
    stream=True
)

for chunk in stream:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="", flush=True)
```


## Zmienne środowiskowe

### Konfiguracja Foundry Local

| Zmienna | Opis | Domyślna | Wymagana |
|---------|------|----------|----------|
| `MODEL` | Alias modelu do użycia | `phi-4-mini` | Nie |
| `BASE_URL` | Punkt końcowy Foundry Local | `http://localhost:8000` | Nie |
| `API_KEY` | Klucz API (opcjonalny dla lokalnego) | `""` | Nie |

### Konfiguracja Azure OpenAI

| Zmienna | Opis | Domyślna | Wymagana |
|---------|------|----------|----------|
| `AZURE_OPENAI_ENDPOINT` | Punkt końcowy zasobu Azure OpenAI | - | Tak |
| `AZURE_OPENAI_API_KEY` | Klucz API Azure OpenAI | - | Tak |
| `AZURE_OPENAI_API_VERSION` | Wersja API | `2024-08-01-preview` | Nie |
| `MODEL` | Nazwa wdrożenia Azure | `your-deployment-name` | Tak |

## Zaawansowane funkcje

### Automatyczne wykrywanie usług

Przykład automatycznie wykrywa odpowiednią usługę na podstawie zmiennych środowiskowych:

1. **Tryb Azure**: Jeśli ustawione są `AZURE_OPENAI_ENDPOINT` i `AZURE_OPENAI_API_KEY`
2. **Tryb Foundry SDK**: Jeśli dostępny jest Foundry Local SDK
3. **Tryb ręczny**: Awaryjne przejście do ręcznej konfiguracji

### Obsługa błędów

- Łagodne przejście z SDK na ręczną konfigurację
- Jasne komunikaty o błędach dla rozwiązywania problemów
- Właściwa obsługa wyjątków dla problemów sieciowych
- Walidacja wymaganych zmiennych środowiskowych

## Rozważania dotyczące wydajności

### Lokalny vs chmurowy kompromis

**Zalety Foundry Local:**
- ✅ Brak kosztów API
- ✅ Prywatność danych (dane nie opuszczają urządzenia)
- ✅ Niska latencja dla obsługiwanych modeli
- ✅ Działa offline

**Zalety Azure OpenAI:**
- ✅ Dostęp do najnowszych dużych modeli
- ✅ Wyższa przepustowość
- ✅ Brak wymagań dotyczących lokalnych zasobów obliczeniowych
- ✅ SLA na poziomie korporacyjnym

## Rozwiązywanie problemów

### Typowe problemy

1. **Ostrzeżenie "Nie można użyć Foundry SDK":**
   ```cmd
   pip install foundry-local-sdk
   ```

2. **Błędy uwierzytelniania Azure:**
   ```cmd
   # Verify your endpoint format
   echo %AZURE_OPENAI_ENDPOINT%
   # Should be: https://your-resource.openai.azure.com
   ```

3. **Model niedostępny:**
   ```cmd
   # For Foundry Local
   foundry model list
   foundry model run your-model-name
   
   # For Azure OpenAI
   # Check your deployment name in Azure Portal
   ```


### Kontrole zdrowia

```cmd
# Foundry Local
foundry service status
curl http://localhost:8000/v1/models

# Azure OpenAI
curl -H "api-key: %AZURE_OPENAI_API_KEY%" "%AZURE_OPENAI_ENDPOINT%/openai/deployments?api-version=2024-08-01-preview"
```


## Kolejne kroki

- **Przykład 03**: Odkrywanie modeli i benchmarking
- **Przykład 04**: Tworzenie aplikacji Chainlit RAG
- **Przykład 05**: Orkiestracja wieloagentowa
- **Przykład 06**: Routing modeli jako narzędzi

## Źródła

- [Dokumentacja Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/)
- [Referencja SDK Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [Dokumentacja OpenAI Python SDK](https://github.com/openai/openai-python)
- [Przewodnik po strumieniowym uzupełnianiu](https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/integrate-with-inference-sdks)

---


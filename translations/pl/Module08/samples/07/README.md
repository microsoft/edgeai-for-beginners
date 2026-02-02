# Foundry Local jako przykład API

Ten przykład pokazuje, jak korzystać z Microsoft Foundry Local jako usługi REST API bez użycia OpenAI SDK. Demonstruje bezpośrednie wzorce integracji HTTP dla maksymalnej kontroli i personalizacji.

## Przegląd

Na podstawie oficjalnych wzorców Microsoft Foundry Local, ten przykład oferuje:
- Bezpośrednią integrację REST API z FoundryLocalManager
- Własną implementację klienta HTTP
- Zarządzanie modelami i monitorowanie ich kondycji
- Obsługę odpowiedzi strumieniowych i niestrumieniowych
- Gotowe do produkcji mechanizmy obsługi błędów i logiki ponawiania prób

## Wymagania wstępne

1. **Instalacja Foundry Local**
   ```powershell
   # Install from GitHub releases
   winget install Microsoft.FoundryLocal
   ```

2. **Zależności Python**
   ```bash
   pip install foundry-local-sdk requests asyncio aiohttp
   ```

## Architektura

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Your App      │───▶│  REST API Client │───▶│  Foundry Local  │
│                 │    │                  │    │   Service       │
│ - Custom Logic  │    │ - HTTP Requests  │    │ - Model Loading │
│ - Business Rules│    │ - Authentication │    │ - Inference     │
│ - Data Pipeline │    │ - Error Handling │    │ - Health Check  │
└─────────────────┘    └──────────────────┘    └─────────────────┘
```

## Kluczowe funkcje

### 1. **Bezpośrednia integracja HTTP**
- Czyste wywołania REST API bez zależności od SDK
- Własne uwierzytelnianie i nagłówki
- Pełna kontrola nad obsługą żądań i odpowiedzi

### 2. **Zarządzanie modelami**
- Dynamiczne ładowanie i rozładowywanie modeli
- Monitorowanie kondycji i sprawdzanie statusu
- Zbieranie metryk wydajności

### 3. **Wzorce produkcyjne**
- Mechanizmy ponawiania prób z wykładniczym opóźnieniem
- Bezpiecznik dla tolerancji błędów
- Kompleksowe logowanie i monitorowanie

### 4. **Elastyczna obsługa odpowiedzi**
- Odpowiedzi strumieniowe dla aplikacji w czasie rzeczywistym
- Przetwarzanie wsadowe dla scenariuszy o dużej przepustowości
- Własne parsowanie i walidacja odpowiedzi

## Przykłady użycia

### Podstawowa integracja API
```python
from api_client import FoundryAPIClient

# Initialize the API client
client = FoundryAPIClient()

# Simple completion
response = await client.complete(
    prompt="Explain quantum computing",
    model="phi-4-mini",
    max_tokens=500
)
print(response.content)
```

### Integracja strumieniowa
```python
# Stream responses for real-time applications
async for chunk in client.stream_complete(
    prompt="Write a story about AI",
    model="phi-4-mini"
):
    print(chunk.content, end="", flush=True)
```

### Monitorowanie kondycji
```python
# Check service health
health = await client.health_check()
print(f"Service Status: {health.status}")
print(f"Active Models: {health.loaded_models}")
print(f"Memory Usage: {health.memory_usage}")
```

## Struktura plików

```
07/
├── README.md              # This documentation
├── requirements.txt       # Python dependencies
├── api_client.py         # Core API client implementation
├── health_monitor.py     # Health checking and monitoring
├── examples/
│   ├── basic_usage.py    # Simple API integration example
│   ├── streaming.py      # Streaming response example
│   ├── batch_processing.py # Batch processing example
│   └── production.py     # Production-ready implementation
└── tests/
    ├── test_api_client.py    # Unit tests for API client
    └── test_integration.py   # Integration tests
```

## Integracja Microsoft Foundry Local

Ten przykład opiera się na oficjalnych wzorcach Microsoftu:

1. **Integracja SDK**: Korzysta z `FoundryLocalManager` do zarządzania usługami
2. **Punkty końcowe REST**: Bezpośrednie wywołania do `/v1/chat/completions` i innych punktów końcowych
3. **Uwierzytelnianie**: Prawidłowa obsługa kluczy API dla usług lokalnych
4. **Zarządzanie modelami**: Wzorce katalogowania, pobierania i ładowania
5. **Obsługa błędów**: Zalecane przez Microsoft kody błędów i odpowiedzi

## Pierwsze kroki

1. **Zainstaluj zależności**
   ```bash
   pip install -r requirements.txt
   ```

2. **Uruchom podstawowy przykład**
   ```bash
   python examples/basic_usage.py
   ```

3. **Wypróbuj strumieniowanie**
   ```bash
   python examples/streaming.py
   ```

4. **Konfiguracja produkcyjna**
   ```bash
   python examples/production.py
   ```

## Konfiguracja

Zmienne środowiskowe do personalizacji:
- `FOUNDRY_MODEL`: Domyślny model do użycia (domyślnie: "phi-4-mini")
- `FOUNDRY_TIMEOUT`: Limit czasu żądania w sekundach (domyślnie: 30)
- `FOUNDRY_RETRIES`: Liczba prób ponowienia (domyślnie: 3)
- `FOUNDRY_LOG_LEVEL`: Poziom logowania (domyślnie: "INFO")

## Najlepsze praktyki

1. **Zarządzanie połączeniami**: Ponowne użycie połączeń HTTP dla lepszej wydajności
2. **Obsługa błędów**: Implementacja odpowiedniej logiki ponawiania prób z wykładniczym opóźnieniem
3. **Monitorowanie zasobów**: Śledzenie wykorzystania pamięci modelu i wydajności
4. **Bezpieczeństwo**: Stosowanie odpowiedniego uwierzytelniania nawet dla usług lokalnych
5. **Testowanie**: Uwzględnienie zarówno testów jednostkowych, jak i integracyjnych

## Rozwiązywanie problemów

### Typowe problemy

**Usługa nie działa**
```bash
# Check Foundry Local status
foundry status

# Start if needed
foundry start
```

**Problemy z ładowaniem modelu**
```bash
# List available models
foundry model list

# Download specific model
foundry model download phi-4-mini
```

**Błędy połączenia**
- Sprawdź, czy Foundry Local działa na właściwym porcie
- Sprawdź ustawienia zapory sieciowej
- Upewnij się, że nagłówki uwierzytelniania są poprawne

## Optymalizacja wydajności

1. **Pooling połączeń**: Używaj obiektów sesji do wielu żądań
2. **Operacje asynchroniczne**: Wykorzystaj asyncio do równoczesnych żądań
3. **Caching**: Buforuj odpowiedzi modeli tam, gdzie to możliwe
4. **Monitorowanie**: Śledź czasy odpowiedzi i dostosowuj limity czasu

## Efekty nauki

Po ukończeniu tego przykładu zrozumiesz:
- Bezpośrednią integrację REST API z Foundry Local
- Wzorce implementacji własnego klienta HTTP
- Gotowe do produkcji mechanizmy obsługi błędów i monitorowania
- Architekturę usług Microsoft Foundry Local
- Techniki optymalizacji wydajności dla lokalnych usług AI

## Kolejne kroki

- Odkryj Przykład 08: Aplikacja czatu dla Windows 11
- Wypróbuj Przykład 09: Orkiestracja wieloagentowa
- Poznaj Przykład 10: Foundry Local jako integracja narzędzi

---


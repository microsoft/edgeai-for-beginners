# Foundry Local come esempio di API

Questo esempio dimostra come utilizzare Microsoft Foundry Local come servizio API REST senza dipendere dall'SDK di OpenAI. Mostra modelli di integrazione HTTP diretta per il massimo controllo e personalizzazione.

## Panoramica

Basato sui modelli ufficiali di Microsoft Foundry Local, questo esempio offre:
- Integrazione diretta con API REST tramite FoundryLocalManager
- Implementazione personalizzata del client HTTP
- Gestione dei modelli e monitoraggio dello stato di salute
- Gestione delle risposte in streaming e non-streaming
- Gestione degli errori pronta per la produzione e logica di retry

## Prerequisiti

1. **Installazione di Foundry Local**
   ```powershell
   # Install from GitHub releases
   winget install Microsoft.FoundryLocal
   ```

2. **Dipendenze Python**
   ```bash
   pip install foundry-local-sdk requests asyncio aiohttp
   ```

## Architettura

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Your App      │───▶│  REST API Client │───▶│  Foundry Local  │
│                 │    │                  │    │   Service       │
│ - Custom Logic  │    │ - HTTP Requests  │    │ - Model Loading │
│ - Business Rules│    │ - Authentication │    │ - Inference     │
│ - Data Pipeline │    │ - Error Handling │    │ - Health Check  │
└─────────────────┘    └──────────────────┘    └─────────────────┘
```

## Caratteristiche principali

### 1. **Integrazione HTTP diretta**
- Chiamate API REST pure senza dipendenze dall'SDK
- Autenticazione e intestazioni personalizzate
- Controllo completo sulla gestione delle richieste/risposte

### 2. **Gestione dei modelli**
- Caricamento e scaricamento dinamico dei modelli
- Monitoraggio dello stato di salute e controlli di stato
- Raccolta di metriche sulle prestazioni

### 3. **Modelli di produzione**
- Meccanismi di retry con backoff esponenziale
- Circuit breaker per la tolleranza ai guasti
- Logging e monitoraggio completi

### 4. **Gestione flessibile delle risposte**
- Risposte in streaming per applicazioni in tempo reale
- Elaborazione batch per scenari ad alta capacità
- Parsing e validazione personalizzati delle risposte

## Esempi di utilizzo

### Integrazione API di base
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

### Integrazione in streaming
```python
# Stream responses for real-time applications
async for chunk in client.stream_complete(
    prompt="Write a story about AI",
    model="phi-4-mini"
):
    print(chunk.content, end="", flush=True)
```

### Monitoraggio dello stato di salute
```python
# Check service health
health = await client.health_check()
print(f"Service Status: {health.status}")
print(f"Active Models: {health.loaded_models}")
print(f"Memory Usage: {health.memory_usage}")
```

## Struttura dei file

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

## Integrazione con Microsoft Foundry Local

Questo esempio segue i modelli ufficiali di Microsoft:

1. **Integrazione SDK**: Utilizza `FoundryLocalManager` per la gestione del servizio
2. **Endpoint REST**: Chiamate dirette a `/v1/chat/completions` e altri endpoint
3. **Autenticazione**: Gestione corretta delle chiavi API per i servizi locali
4. **Gestione dei modelli**: Elenco del catalogo, download e modelli di caricamento
5. **Gestione degli errori**: Codici di errore e risposte raccomandati da Microsoft

## Per iniziare

1. **Installa le dipendenze**
   ```bash
   pip install -r requirements.txt
   ```

2. **Esegui l'esempio di base**
   ```bash
   python examples/basic_usage.py
   ```

3. **Prova lo streaming**
   ```bash
   python examples/streaming.py
   ```

4. **Configurazione per la produzione**
   ```bash
   python examples/production.py
   ```

## Configurazione

Variabili di ambiente per la personalizzazione:
- `FOUNDRY_MODEL`: Modello predefinito da utilizzare (predefinito: "phi-4-mini")
- `FOUNDRY_TIMEOUT`: Timeout delle richieste in secondi (predefinito: 30)
- `FOUNDRY_RETRIES`: Numero di tentativi di retry (predefinito: 3)
- `FOUNDRY_LOG_LEVEL`: Livello di logging (predefinito: "INFO")

## Migliori pratiche

1. **Gestione delle connessioni**: Riutilizza le connessioni HTTP per migliorare le prestazioni
2. **Gestione degli errori**: Implementa una logica di retry con backoff esponenziale
3. **Monitoraggio delle risorse**: Tieni traccia dell'utilizzo della memoria del modello e delle prestazioni
4. **Sicurezza**: Utilizza un'autenticazione adeguata anche per i servizi locali
5. **Test**: Includi test unitari e di integrazione

## Risoluzione dei problemi

### Problemi comuni

**Servizio non in esecuzione**
```bash
# Check Foundry Local status
foundry status

# Start if needed
foundry start
```

**Problemi di caricamento del modello**
```bash
# List available models
foundry model list

# Download specific model
foundry model download phi-4-mini
```

**Errori di connessione**
- Verifica che Foundry Local sia in esecuzione sulla porta corretta
- Controlla le impostazioni del firewall
- Assicurati che le intestazioni di autenticazione siano corrette

## Ottimizzazione delle prestazioni

1. **Pooling delle connessioni**: Utilizza oggetti session per richieste multiple
2. **Operazioni asincrone**: Sfrutta asyncio per richieste concorrenti
3. **Caching**: Memorizza nella cache le risposte dei modelli dove appropriato
4. **Monitoraggio**: Tieni traccia dei tempi di risposta e regola i timeout

## Risultati di apprendimento

Dopo aver completato questo esempio, comprenderai:
- Integrazione diretta con API REST di Foundry Local
- Modelli di implementazione personalizzati del client HTTP
- Gestione degli errori e monitoraggio pronti per la produzione
- Architettura del servizio Microsoft Foundry Local
- Tecniche di ottimizzazione delle prestazioni per servizi AI locali

## Prossimi passi

- Esplora l'Esempio 08: Applicazione Chat per Windows 11
- Prova l'Esempio 09: Orchestrazione Multi-Agent
- Scopri l'Esempio 10: Foundry Local come integrazione di strumenti

---


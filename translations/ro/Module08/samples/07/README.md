# Foundry Local ca exemplu de API

Acest exemplu demonstrează cum să utilizați Microsoft Foundry Local ca serviciu REST API fără a depinde de SDK-ul OpenAI. Prezintă modele de integrare directă prin HTTP pentru control și personalizare maxime.

## Prezentare generală

Bazat pe modelele oficiale Microsoft Foundry Local, acest exemplu oferă:
- Integrare directă REST API cu FoundryLocalManager
- Implementare personalizată a clientului HTTP
- Gestionarea modelelor și monitorizarea stării de sănătate
- Gestionarea răspunsurilor în flux și non-flux
- Manevrare erori și logică de retry pregătite pentru producție

## Cerințe preliminare

1. **Instalarea Foundry Local**
   ```powershell
   # Install from GitHub releases
   winget install Microsoft.FoundryLocal
   ```

2. **Dependențe Python**
   ```bash
   pip install foundry-local-sdk requests asyncio aiohttp
   ```

## Arhitectură

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Your App      │───▶│  REST API Client │───▶│  Foundry Local  │
│                 │    │                  │    │   Service       │
│ - Custom Logic  │    │ - HTTP Requests  │    │ - Model Loading │
│ - Business Rules│    │ - Authentication │    │ - Inference     │
│ - Data Pipeline │    │ - Error Handling │    │ - Health Check  │
└─────────────────┘    └──────────────────┘    └─────────────────┘
```

## Funcționalități cheie

### 1. **Integrare directă HTTP**
- Apeluri REST API pure fără dependențe de SDK
- Autentificare și anteturi personalizate
- Control complet asupra gestionării cererilor/răspunsurilor

### 2. **Gestionarea modelelor**
- Încărcare și descărcare dinamică a modelelor
- Monitorizarea stării de sănătate și verificări de status
- Colectarea metricilor de performanță

### 3. **Modele de producție**
- Mecanisme de retry cu backoff exponențial
- Circuit breaker pentru toleranță la erori
- Logare și monitorizare cuprinzătoare

### 4. **Gestionarea flexibilă a răspunsurilor**
- Răspunsuri în flux pentru aplicații în timp real
- Procesare în loturi pentru scenarii cu debit mare
- Parsare și validare personalizată a răspunsurilor

## Exemple de utilizare

### Integrare API de bază
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

### Integrare în flux
```python
# Stream responses for real-time applications
async for chunk in client.stream_complete(
    prompt="Write a story about AI",
    model="phi-4-mini"
):
    print(chunk.content, end="", flush=True)
```

### Monitorizarea stării de sănătate
```python
# Check service health
health = await client.health_check()
print(f"Service Status: {health.status}")
print(f"Active Models: {health.loaded_models}")
print(f"Memory Usage: {health.memory_usage}")
```

## Structura fișierelor

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

## Integrarea Microsoft Foundry Local

Acest exemplu urmează modelele oficiale Microsoft:

1. **Integrare SDK**: Utilizează `FoundryLocalManager` pentru gestionarea serviciilor
2. **Endpoint-uri REST**: Apeluri directe către `/v1/chat/completions` și alte endpoint-uri
3. **Autentificare**: Gestionarea corespunzătoare a cheilor API pentru servicii locale
4. **Gestionarea modelelor**: Listarea catalogului, descărcarea și modelele de încărcare
5. **Manevrare erori**: Coduri de eroare și răspunsuri recomandate de Microsoft

## Începeți

1. **Instalați dependențele**
   ```bash
   pip install -r requirements.txt
   ```

2. **Rulați exemplul de bază**
   ```bash
   python examples/basic_usage.py
   ```

3. **Încercați fluxul**
   ```bash
   python examples/streaming.py
   ```

4. **Configurare pentru producție**
   ```bash
   python examples/production.py
   ```

## Configurare

Variabile de mediu pentru personalizare:
- `FOUNDRY_MODEL`: Modelul implicit utilizat (implicit: "phi-4-mini")
- `FOUNDRY_TIMEOUT`: Timeout-ul cererii în secunde (implicit: 30)
- `FOUNDRY_RETRIES`: Numărul de încercări de retry (implicit: 3)
- `FOUNDRY_LOG_LEVEL`: Nivelul de logare (implicit: "INFO")

## Cele mai bune practici

1. **Gestionarea conexiunilor**: Reutilizați conexiunile HTTP pentru performanță mai bună
2. **Manevrare erori**: Implementați logică de retry corespunzătoare cu backoff exponențial
3. **Monitorizarea resurselor**: Urmăriți utilizarea memoriei modelului și performanța
4. **Securitate**: Utilizați autentificare corespunzătoare chiar și pentru servicii locale
5. **Testare**: Includeți teste unitare și de integrare

## Depanare

### Probleme comune

**Serviciul nu rulează**
```bash
# Check Foundry Local status
foundry status

# Start if needed
foundry start
```

**Probleme la încărcarea modelului**
```bash
# List available models
foundry model list

# Download specific model
foundry model download phi-4-mini
```

**Erori de conexiune**
- Verificați dacă Foundry Local rulează pe portul corect
- Verificați setările firewall-ului
- Asigurați-vă că anteturile de autentificare sunt corecte

## Optimizarea performanței

1. **Pooling de conexiuni**: Utilizați obiecte de sesiune pentru cereri multiple
2. **Operațiuni asincrone**: Folosiți asyncio pentru cereri concurente
3. **Caching**: Cache pentru răspunsurile modelelor unde este potrivit
4. **Monitorizare**: Urmăriți timpii de răspuns și ajustați timeout-urile

## Rezultate de învățare

După finalizarea acestui exemplu, veți înțelege:
- Integrarea directă REST API cu Foundry Local
- Modele de implementare personalizată a clientului HTTP
- Manevrare erori și monitorizare pregătite pentru producție
- Arhitectura serviciului Microsoft Foundry Local
- Tehnici de optimizare a performanței pentru servicii AI locale

## Pași următori

- Explorați Exemplul 08: Aplicație de chat Windows 11
- Încercați Exemplul 09: Orchestrare multi-agent
- Aflați din Exemplul 10: Foundry Local ca integrare de instrumente

---


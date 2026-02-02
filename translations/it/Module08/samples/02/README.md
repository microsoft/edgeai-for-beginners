# Esempio 02: Integrazione con OpenAI SDK

Dimostra un'integrazione avanzata con l'SDK Python di OpenAI, supportando sia Microsoft Foundry Local che Azure OpenAI con risposte in streaming e gestione corretta degli errori.

## Panoramica

Questo esempio mostra:
- Passaggio fluido tra Foundry Local e Azure OpenAI
- Completamenti di chat in streaming per una migliore esperienza utente
- Uso corretto dell'SDK FoundryLocalManager
- Meccanismi robusti di gestione degli errori e fallback
- Modelli di codice pronti per la produzione

## Prerequisiti

- **Foundry Local**: Installato e in esecuzione (per inferenza locale)
- **Python**: Versione 3.8 o successiva con OpenAI SDK
- **Azure OpenAI**: Endpoint valido e chiave API (per inferenza cloud)

## Installazione

1. **Configura l'ambiente Python:**
   ```cmd
   cd Module08
   py -m venv .venv
   .venv\Scripts\activate
   ```

2. **Installa le dipendenze:**
   ```cmd
   pip install -r requirements.txt
   ```

3. **Avvia Foundry Local (per modalità locale):**
   ```cmd
   foundry model run phi-4-mini
   ```


## Scenari di Utilizzo

### Foundry Local (Predefinito)

**Opzione 1: Utilizzo di FoundryLocalManager (Consigliato)**
```cmd
# Automatic service discovery and model management
set MODEL=phi-4-mini
python samples\02\sdk_quickstart.py
```

**Opzione 2: Configurazione Manuale**
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


## Architettura del Codice

### Pattern Factory Client

L'esempio utilizza un pattern factory per creare i client appropriati:

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


### Risposte in Streaming

L'esempio dimostra il streaming per la generazione di risposte in tempo reale:

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


## Variabili d'Ambiente

### Configurazione Foundry Local

| Variabile | Descrizione | Predefinito | Necessario |
|-----------|-------------|-------------|------------|
| `MODEL` | Alias del modello da utilizzare | `phi-4-mini` | No |
| `BASE_URL` | Endpoint di Foundry Local | `http://localhost:8000` | No |
| `API_KEY` | Chiave API (opzionale per locale) | `""` | No |

### Configurazione Azure OpenAI

| Variabile | Descrizione | Predefinito | Necessario |
|-----------|-------------|-------------|------------|
| `AZURE_OPENAI_ENDPOINT` | Endpoint della risorsa Azure OpenAI | - | Sì |
| `AZURE_OPENAI_API_KEY` | Chiave API di Azure OpenAI | - | Sì |
| `AZURE_OPENAI_API_VERSION` | Versione API | `2024-08-01-preview` | No |
| `MODEL` | Nome del deployment Azure | `your-deployment-name` | Sì |

## Funzionalità Avanzate

### Scoperta Automatica del Servizio

L'esempio rileva automaticamente il servizio appropriato in base alle variabili d'ambiente:

1. **Modalità Azure**: Se `AZURE_OPENAI_ENDPOINT` e `AZURE_OPENAI_API_KEY` sono impostati
2. **Modalità SDK Foundry**: Se l'SDK Foundry Local è disponibile
3. **Modalità Manuale**: Fallback alla configurazione manuale

### Gestione degli Errori

- Fallback graduale dall'SDK alla configurazione manuale
- Messaggi di errore chiari per la risoluzione dei problemi
- Gestione corretta delle eccezioni per problemi di rete
- Validazione delle variabili d'ambiente richieste

## Considerazioni sulle Prestazioni

### Trade-off Locale vs Cloud

**Vantaggi di Foundry Local:**
- ✅ Nessun costo API
- ✅ Privacy dei dati (nessun dato lascia il dispositivo)
- ✅ Bassa latenza per i modelli supportati
- ✅ Funziona offline

**Vantaggi di Azure OpenAI:**
- ✅ Accesso ai modelli di grandi dimensioni più recenti
- ✅ Maggiore throughput
- ✅ Nessun requisito di calcolo locale
- ✅ SLA di livello enterprise

## Risoluzione dei Problemi

### Problemi Comuni

1. **Avviso "Impossibile utilizzare l'SDK Foundry":**
   ```cmd
   pip install foundry-local-sdk
   ```

2. **Errori di autenticazione Azure:**
   ```cmd
   # Verify your endpoint format
   echo %AZURE_OPENAI_ENDPOINT%
   # Should be: https://your-resource.openai.azure.com
   ```

3. **Modello non disponibile:**
   ```cmd
   # For Foundry Local
   foundry model list
   foundry model run your-model-name
   
   # For Azure OpenAI
   # Check your deployment name in Azure Portal
   ```


### Controlli di Salute

```cmd
# Foundry Local
foundry service status
curl http://localhost:8000/v1/models

# Azure OpenAI
curl -H "api-key: %AZURE_OPENAI_API_KEY%" "%AZURE_OPENAI_ENDPOINT%/openai/deployments?api-version=2024-08-01-preview"
```


## Prossimi Passi

- **Esempio 03**: Scoperta e benchmarking dei modelli
- **Esempio 04**: Creazione di un'applicazione Chainlit RAG
- **Esempio 05**: Orchestrazione multi-agente
- **Esempio 06**: Routing dei modelli come strumenti

## Riferimenti

- [Documentazione Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/)
- [Riferimento SDK Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [Documentazione SDK Python OpenAI](https://github.com/openai/openai-python)
- [Guida ai completamenti in streaming](https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/integrate-with-inference-sdks)

---


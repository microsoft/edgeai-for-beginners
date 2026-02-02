# Esempio 01: Chat Rapida con OpenAI SDK

Un semplice esempio di chat che dimostra come utilizzare l'OpenAI SDK con Microsoft Foundry Local per l'inferenza AI locale.

## Panoramica

Questo esempio mostra come:
- Utilizzare l'OpenAI Python SDK con Foundry Local
- Gestire sia le configurazioni di Azure OpenAI che quelle locali di Foundry
- Implementare una corretta gestione degli errori e strategie di fallback
- Usare il FoundryLocalManager per la gestione dei servizi

## Prerequisiti

- **Foundry Local**: Installato e disponibile nel PATH
- **Python**: Versione 3.8 o successiva
- **Modello**: Un modello caricato in Foundry Local (es. `phi-4-mini`)

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

3. **Avvia il servizio Foundry Local e carica un modello:**
   ```cmd
   foundry model run phi-4-mini
   ```


## Utilizzo

### Foundry Local (Predefinito)

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


## Funzionalità del Codice

### Integrazione con FoundryLocalManager

L'esempio utilizza l'SDK ufficiale di Foundry Local per una corretta gestione dei servizi:

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


### Gestione degli Errori

Gestione robusta degli errori con fallback alla configurazione manuale:
- Scoperta automatica dei servizi
- Degradazione graduale se l'SDK non è disponibile
- Messaggi di errore chiari per la risoluzione dei problemi

## Variabili d'Ambiente

| Variabile | Descrizione | Predefinito | Necessaria |
|----------|-------------|-------------|------------|
| `MODEL` | Alias o nome del modello | `phi-4-mini` | No |
| `BASE_URL` | URL base di Foundry Local | `http://localhost:8000` | No |
| `API_KEY` | Chiave API (di solito non necessaria per locale) | `""` | No |
| `AZURE_OPENAI_ENDPOINT` | Endpoint di Azure OpenAI | - | Per Azure |
| `AZURE_OPENAI_API_KEY` | Chiave API di Azure OpenAI | - | Per Azure |
| `AZURE_OPENAI_API_VERSION` | Versione API di Azure | `2024-08-01-preview` | No |

## Risoluzione dei Problemi

### Problemi Comuni

1. **Avviso "Impossibile utilizzare Foundry SDK":**
   - Installa foundry-local-sdk: `pip install foundry-local-sdk`
   - Oppure configura manualmente le variabili d'ambiente

2. **Connessione rifiutata:**
   - Assicurati che Foundry Local sia in esecuzione: `foundry service status`
   - Verifica che un modello sia caricato: `foundry service ps`

3. **Modello non trovato:**
   - Elenca i modelli disponibili: `foundry model list`
   - Carica un modello: `foundry model run phi-4-mini`

### Verifica

```cmd
# Check Foundry Local status
foundry service status

# List loaded models
foundry service ps

# Test API endpoint
curl http://localhost:8000/v1/models
```


## Riferimenti

- [Documentazione di Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [OpenAI Python SDK](https://github.com/openai/openai-python)
- [Foundry Local GitHub](https://github.com/microsoft/Foundry-Local)
- [Riferimento API compatibile con OpenAI](https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks)

---


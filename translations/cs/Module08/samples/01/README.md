# Ukázka 01: Rychlý chat přes OpenAI SDK

Jednoduchý příklad chatu, který ukazuje, jak používat OpenAI SDK s Microsoft Foundry Local pro lokální AI inferenci.

## Přehled

Tato ukázka demonstruje, jak:
- Používat OpenAI Python SDK s Foundry Local
- Pracovat s konfiguracemi Azure OpenAI i lokální Foundry
- Implementovat správné zpracování chyb a strategie záložního řešení
- Používat FoundryLocalManager pro správu služeb

## Předpoklady

- **Foundry Local**: Nainstalováno a dostupné v PATH
- **Python**: Verze 3.8 nebo novější
- **Model**: Model načtený ve Foundry Local (např. `phi-4-mini`)

## Instalace

1. **Nastavení Python prostředí:**
   ```cmd
   cd Module08
   py -m venv .venv
   .venv\Scripts\activate
   ```

2. **Instalace závislostí:**
   ```cmd
   pip install -r requirements.txt
   ```

3. **Spuštění služby Foundry Local a načtení modelu:**
   ```cmd
   foundry model run phi-4-mini
   ```

## Použití

### Foundry Local (Výchozí)

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

## Vlastnosti kódu

### Integrace FoundryLocalManager

Ukázka využívá oficiální Foundry Local SDK pro správnou správu služeb:

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

### Zpracování chyb

Robustní zpracování chyb s možností záložního manuálního nastavení:
- Automatické vyhledávání služeb
- Plynulé přepnutí v případě nedostupnosti SDK
- Jasné chybové zprávy pro snadné řešení problémů

## Proměnné prostředí

| Proměnná | Popis | Výchozí | Povinné |
|----------|-------|---------|---------|
| `MODEL` | Alias nebo název modelu | `phi-4-mini` | Ne |
| `BASE_URL` | Základní URL Foundry Local | `http://localhost:8000` | Ne |
| `API_KEY` | API klíč (obvykle není potřeba pro lokální použití) | `""` | Ne |
| `AZURE_OPENAI_ENDPOINT` | Endpoint Azure OpenAI | - | Pro Azure |
| `AZURE_OPENAI_API_KEY` | API klíč Azure OpenAI | - | Pro Azure |
| `AZURE_OPENAI_API_VERSION` | Verze API Azure | `2024-08-01-preview` | Ne |

## Řešení problémů

### Běžné problémy

1. **Varování "Nelze použít Foundry SDK":**
   - Nainstalujte foundry-local-sdk: `pip install foundry-local-sdk`
   - Nebo nastavte proměnné prostředí pro manuální konfiguraci

2. **Odmítnutí připojení:**
   - Ujistěte se, že Foundry Local běží: `foundry service status`
   - Zkontrolujte, zda je načten model: `foundry service ps`

3. **Model nebyl nalezen:**
   - Zobrazte dostupné modely: `foundry model list`
   - Načtěte model: `foundry model run phi-4-mini`

### Ověření

```cmd
# Check Foundry Local status
foundry service status

# List loaded models
foundry service ps

# Test API endpoint
curl http://localhost:8000/v1/models
```

## Odkazy

- [Dokumentace Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [OpenAI Python SDK](https://github.com/openai/openai-python)
- [Foundry Local GitHub](https://github.com/microsoft/Foundry-Local)
- [Referenční API kompatibilní s OpenAI](https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks)

---


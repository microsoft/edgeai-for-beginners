# Ukážka 01: Rýchly chat cez OpenAI SDK

Jednoduchý príklad chatu, ktorý demonštruje použitie OpenAI SDK s Microsoft Foundry Local pre lokálnu AI inferenciu.

## Prehľad

Táto ukážka ukazuje, ako:
- Používať OpenAI Python SDK s Foundry Local
- Spracovať konfigurácie pre Azure OpenAI aj lokálny Foundry
- Implementovať správne spracovanie chýb a stratégie záložného riešenia
- Používať FoundryLocalManager na správu služieb

## Predpoklady

- **Foundry Local**: Nainštalovaný a dostupný v PATH
- **Python**: Verzia 3.8 alebo novšia
- **Model**: Model načítaný vo Foundry Local (napr. `phi-4-mini`)

## Inštalácia

1. **Nastavte Python prostredie:**
   ```cmd
   cd Module08
   py -m venv .venv
   .venv\Scripts\activate
   ```

2. **Nainštalujte závislosti:**
   ```cmd
   pip install -r requirements.txt
   ```

3. **Spustite službu Foundry Local a načítajte model:**
   ```cmd
   foundry model run phi-4-mini
   ```

## Použitie

### Foundry Local (predvolené)

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

## Funkcie kódu

### Integrácia FoundryLocalManager

Ukážka používa oficiálne Foundry Local SDK na správu služieb:

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

### Spracovanie chýb

Robustné spracovanie chýb s možnosťou záložného manuálneho nastavenia:
- Automatické vyhľadávanie služieb
- Plynulá degradácia, ak SDK nie je dostupné
- Jasné chybové hlásenia na riešenie problémov

## Premenné prostredia

| Premenná | Popis | Predvolené | Povinné |
|----------|-------------|---------|----------|
| `MODEL` | Alias alebo názov modelu | `phi-4-mini` | Nie |
| `BASE_URL` | Základná URL Foundry Local | `http://localhost:8000` | Nie |
| `API_KEY` | API kľúč (zvyčajne nie je potrebný pre lokálne použitie) | `""` | Nie |
| `AZURE_OPENAI_ENDPOINT` | Endpoint Azure OpenAI | - | Pre Azure |
| `AZURE_OPENAI_API_KEY` | API kľúč Azure OpenAI | - | Pre Azure |
| `AZURE_OPENAI_API_VERSION` | Verzia Azure API | `2024-08-01-preview` | Nie |

## Riešenie problémov

### Bežné problémy

1. **Varovanie "Nie je možné použiť Foundry SDK":**
   - Nainštalujte foundry-local-sdk: `pip install foundry-local-sdk`
   - Alebo nastavte premenné prostredia na manuálnu konfiguráciu

2. **Odmietnuté pripojenie:**
   - Uistite sa, že Foundry Local beží: `foundry service status`
   - Skontrolujte, či je model načítaný: `foundry service ps`

3. **Model nebol nájdený:**
   - Zobrazte dostupné modely: `foundry model list`
   - Načítajte model: `foundry model run phi-4-mini`

### Overenie

```cmd
# Check Foundry Local status
foundry service status

# List loaded models
foundry service ps

# Test API endpoint
curl http://localhost:8000/v1/models
```

## Referencie

- [Dokumentácia Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [OpenAI Python SDK](https://github.com/openai/openai-python)
- [Foundry Local GitHub](https://github.com/microsoft/Foundry-Local)
- [Referenčný API kompatibilný s OpenAI](https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks)

---


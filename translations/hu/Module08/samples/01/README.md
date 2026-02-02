# Minta 01: Gyors csevegés az OpenAI SDK-val

Egy egyszerű csevegési példa, amely bemutatja, hogyan használható az OpenAI SDK a Microsoft Foundry Local-lal helyi AI következtetéshez.

## Áttekintés

Ez a minta bemutatja, hogyan kell:
- Az OpenAI Python SDK-t használni a Foundry Local-lal
- Kezelni az Azure OpenAI és a helyi Foundry konfigurációkat
- Megvalósítani a megfelelő hibakezelést és tartalék stratégiákat
- Használni a FoundryLocalManager-t a szolgáltatás kezeléséhez

## Előfeltételek

- **Foundry Local**: Telepítve és elérhető az PATH-on
- **Python**: 3.8 vagy újabb
- **Modell**: Egy modell betöltve a Foundry Local-ba (pl. `phi-4-mini`)

## Telepítés

1. **Python környezet beállítása:**
   ```cmd
   cd Module08
   py -m venv .venv
   .venv\Scripts\activate
   ```

2. **Függőségek telepítése:**
   ```cmd
   pip install -r requirements.txt
   ```

3. **Foundry Local szolgáltatás indítása és modell betöltése:**
   ```cmd
   foundry model run phi-4-mini
   ```

## Használat

### Foundry Local (Alapértelmezett)

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

## Kód jellemzői

### FoundryLocalManager integráció

A minta az hivatalos Foundry Local SDK-t használja a megfelelő szolgáltatáskezeléshez:

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

### Hibakezelés

Robusztus hibakezelés manuális konfigurációra való visszaeséssel:
- Automatikus szolgáltatásfelismerés
- Kíméletes degradáció, ha az SDK nem érhető el
- Egyértelmű hibaüzenetek a hibaelhárításhoz

## Környezeti változók

| Változó | Leírás | Alapértelmezett | Kötelező |
|---------|--------|-----------------|----------|
| `MODEL` | Modell alias vagy neve | `phi-4-mini` | Nem |
| `BASE_URL` | Foundry Local alap URL | `http://localhost:8000` | Nem |
| `API_KEY` | API kulcs (általában nem szükséges helyi használathoz) | `""` | Nem |
| `AZURE_OPENAI_ENDPOINT` | Azure OpenAI végpont | - | Azure esetén |
| `AZURE_OPENAI_API_KEY` | Azure OpenAI API kulcs | - | Azure esetén |
| `AZURE_OPENAI_API_VERSION` | Azure API verzió | `2024-08-01-preview` | Nem |

## Hibaelhárítás

### Gyakori problémák

1. **"Nem sikerült használni a Foundry SDK-t" figyelmeztetés:**
   - Telepítse a foundry-local-sdk-t: `pip install foundry-local-sdk`
   - Vagy állítsa be a környezeti változókat manuális konfigurációhoz

2. **Kapcsolat megtagadva:**
   - Ellenőrizze, hogy a Foundry Local fut-e: `foundry service status`
   - Ellenőrizze, hogy egy modell betöltve van-e: `foundry service ps`

3. **Modell nem található:**
   - Listázza a rendelkezésre álló modelleket: `foundry model list`
   - Töltsön be egy modellt: `foundry model run phi-4-mini`

### Ellenőrzés

```cmd
# Check Foundry Local status
foundry service status

# List loaded models
foundry service ps

# Test API endpoint
curl http://localhost:8000/v1/models
```

## Hivatkozások

- [Foundry Local Dokumentáció](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [OpenAI Python SDK](https://github.com/openai/openai-python)
- [Foundry Local GitHub](https://github.com/microsoft/Foundry-Local)
- [OpenAI-kompatibilis API Referencia](https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks)

---


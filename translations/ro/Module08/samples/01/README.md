# Exemplu 01: Chat Rapid prin OpenAI SDK

Un exemplu simplu de chat care demonstrează cum să folosești OpenAI SDK împreună cu Microsoft Foundry Local pentru inferență AI locală.

## Prezentare Generală

Acest exemplu arată cum să:
- Utilizezi OpenAI Python SDK cu Foundry Local
- Gestionezi atât configurațiile Azure OpenAI, cât și cele locale Foundry
- Implementezi gestionarea corectă a erorilor și strategii de rezervă
- Folosești FoundryLocalManager pentru administrarea serviciilor

## Cerințe Prealabile

- **Foundry Local**: Instalată și disponibilă în PATH
- **Python**: Versiunea 3.8 sau mai recentă
- **Model**: Un model încărcat în Foundry Local (de exemplu, `phi-4-mini`)

## Instalare

1. **Configurează mediul Python:**
   ```cmd
   cd Module08
   py -m venv .venv
   .venv\Scripts\activate
   ```

2. **Instalează dependențele:**
   ```cmd
   pip install -r requirements.txt
   ```

3. **Pornește serviciul Foundry Local și încarcă un model:**
   ```cmd
   foundry model run phi-4-mini
   ```


## Utilizare

### Foundry Local (Implicit)

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


## Funcționalități ale Codului

### Integrarea FoundryLocalManager

Exemplul utilizează SDK-ul oficial Foundry Local pentru administrarea corectă a serviciilor:

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


### Gestionarea Erorilor

Gestionare robustă a erorilor cu rezervă pentru configurare manuală:
- Descoperirea automată a serviciilor
- Degradare grațioasă dacă SDK-ul nu este disponibil
- Mesaje de eroare clare pentru depanare

## Variabile de Mediu

| Variabilă | Descriere | Implicit | Obligatoriu |
|-----------|-----------|----------|-------------|
| `MODEL` | Alias sau nume model | `phi-4-mini` | Nu |
| `BASE_URL` | URL de bază Foundry Local | `http://localhost:8000` | Nu |
| `API_KEY` | Cheie API (de obicei, nu este necesară pentru local) | `""` | Nu |
| `AZURE_OPENAI_ENDPOINT` | Endpoint Azure OpenAI | - | Pentru Azure |
| `AZURE_OPENAI_API_KEY` | Cheie API Azure OpenAI | - | Pentru Azure |
| `AZURE_OPENAI_API_VERSION` | Versiune API Azure | `2024-08-01-preview` | Nu |

## Depanare

### Probleme Comune

1. **Avertisment "Nu s-a putut utiliza Foundry SDK":**
   - Instalează foundry-local-sdk: `pip install foundry-local-sdk`
   - Sau setează variabilele de mediu pentru configurare manuală

2. **Conexiune refuzată:**
   - Asigură-te că Foundry Local rulează: `foundry service status`
   - Verifică dacă un model este încărcat: `foundry service ps`

3. **Modelul nu a fost găsit:**
   - Listează modelele disponibile: `foundry model list`
   - Încarcă un model: `foundry model run phi-4-mini`

### Verificare

```cmd
# Check Foundry Local status
foundry service status

# List loaded models
foundry service ps

# Test API endpoint
curl http://localhost:8000/v1/models
```


## Referințe

- [Documentația Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [OpenAI Python SDK](https://github.com/openai/openai-python)
- [Foundry Local GitHub](https://github.com/microsoft/Foundry-Local)
- [Referință API compatibilă OpenAI](https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks)

---


# Ejemplo 01: Chat Rápido con el SDK de OpenAI

Un ejemplo sencillo de chat que demuestra cómo usar el SDK de OpenAI con Microsoft Foundry Local para inferencia de IA local.

## Descripción General

Este ejemplo muestra cómo:
- Usar el SDK de OpenAI en Python con Foundry Local
- Manejar configuraciones tanto de Azure OpenAI como de Foundry Local
- Implementar un manejo adecuado de errores y estrategias de respaldo
- Utilizar FoundryLocalManager para la gestión de servicios

## Requisitos Previos

- **Foundry Local**: Instalado y disponible en el PATH
- **Python**: Versión 3.8 o posterior
- **Modelo**: Un modelo cargado en Foundry Local (por ejemplo, `phi-4-mini`)

## Instalación

1. **Configurar el entorno de Python:**
   ```cmd
   cd Module08
   py -m venv .venv
   .venv\Scripts\activate
   ```

2. **Instalar dependencias:**
   ```cmd
   pip install -r requirements.txt
   ```

3. **Iniciar el servicio de Foundry Local y cargar un modelo:**
   ```cmd
   foundry model run phi-4-mini
   ```

## Uso

### Foundry Local (Predeterminado)

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

## Características del Código

### Integración con FoundryLocalManager

El ejemplo utiliza el SDK oficial de Foundry Local para una gestión adecuada del servicio:

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

### Manejo de Errores

Manejo robusto de errores con respaldo a configuración manual:
- Descubrimiento automático de servicios
- Degradación controlada si el SDK no está disponible
- Mensajes de error claros para facilitar la resolución de problemas

## Variables de Entorno

| Variable | Descripción | Predeterminado | Obligatorio |
|----------|-------------|----------------|-------------|
| `MODEL` | Alias o nombre del modelo | `phi-4-mini` | No |
| `BASE_URL` | URL base de Foundry Local | `http://localhost:8000` | No |
| `API_KEY` | Clave API (generalmente no necesaria para local) | `""` | No |
| `AZURE_OPENAI_ENDPOINT` | Endpoint de Azure OpenAI | - | Para Azure |
| `AZURE_OPENAI_API_KEY` | Clave API de Azure OpenAI | - | Para Azure |
| `AZURE_OPENAI_API_VERSION` | Versión de la API de Azure | `2024-08-01-preview` | No |

## Resolución de Problemas

### Problemas Comunes

1. **Advertencia "No se pudo usar el SDK de Foundry":**
   - Instalar el SDK de Foundry Local: `pip install foundry-local-sdk`
   - O configurar las variables de entorno manualmente

2. **Conexión rechazada:**
   - Asegúrate de que Foundry Local esté en ejecución: `foundry service status`
   - Verifica si un modelo está cargado: `foundry service ps`

3. **Modelo no encontrado:**
   - Lista los modelos disponibles: `foundry model list`
   - Carga un modelo: `foundry model run phi-4-mini`

### Verificación

```cmd
# Check Foundry Local status
foundry service status

# List loaded models
foundry service ps

# Test API endpoint
curl http://localhost:8000/v1/models
```

## Referencias

- [Documentación de Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [SDK de OpenAI en Python](https://github.com/openai/openai-python)
- [GitHub de Foundry Local](https://github.com/microsoft/Foundry-Local)
- [Referencia de API compatible con OpenAI](https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks)

---


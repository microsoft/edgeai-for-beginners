<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "05db93129bdc4889e0c5dd3c5ea21498",
  "translation_date": "2025-11-11T21:22:40+00:00",
  "source_file": "Workshop/ENV_CONFIGURATION.md",
  "language_code": "es"
}
-->
# Guía de Configuración del Entorno

## Resumen

Los ejemplos del taller utilizan variables de entorno para la configuración, centralizadas en el archivo `.env` ubicado en la raíz del repositorio. Esto permite una fácil personalización sin necesidad de modificar el código.

## Inicio Rápido

### 1. Verificar Requisitos Previos

```bash
# Check Foundry Local is installed
foundry --version

# Check service is running
foundry service status

# Load a model
foundry model run phi-4-mini
```

### 2. Configurar el Entorno

El archivo `.env` ya está configurado con valores predeterminados razonables. La mayoría de los usuarios no necesitarán cambiar nada.

**Opcional**: Revisar y personalizar configuraciones:
```bash
# Edit .env file
notepad .env  # Windows
nano .env     # macOS/Linux
```

### 3. Aplicar la Configuración

**Para Scripts en Python:**
```bash
cd Workshop/samples
python -m session01.chat_bootstrap "Your question here"
# Environment variables automatically loaded
```

**Para Notebooks:**
```python
# Restart kernel after .env changes
# Variables are loaded when cells execute
```

## Referencia de Variables de Entorno

### Configuración Principal

| Variable | Predeterminado | Descripción |
|----------|----------------|-------------|
| `FOUNDRY_LOCAL_ALIAS` | `phi-4-mini` | Modelo predeterminado para los ejemplos |
| `FOUNDRY_LOCAL_ENDPOINT` | (vacío) | Sobrescribir el endpoint del servicio |
| `PYTHONPATH` | Rutas del taller | Ruta de búsqueda de módulos de Python |

**Cuándo configurar FOUNDRY_LOCAL_ENDPOINT:**
- Instancia remota de Foundry Local
- Configuración de puerto personalizada
- Separación entre desarrollo y producción

**Ejemplo:**
```bash
# Local custom port
FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Remote instance
FOUNDRY_LOCAL_ENDPOINT=http://192.168.1.50:5273/v1
```

### Variables Específicas de Sesión

#### Sesión 02: Pipeline RAG
| Variable | Predeterminado | Propósito |
|----------|----------------|-----------|
| `EMBED_MODEL` | `sentence-transformers/all-MiniLM-L6-v2` | Modelo de embeddings |
| `RAG_QUESTION` | Preconfigurado | Pregunta de prueba |

#### Sesión 03: Benchmarking
| Variable | Predeterminado | Propósito |
|----------|----------------|-----------|
| `BENCH_MODELS` | `phi-4-mini,qwen2.5-0.5b` | Modelos para benchmarking |
| `BENCH_ROUNDS` | `3` | Iteraciones por modelo |
| `BENCH_PROMPT` | Preconfigurado | Prompt de prueba |
| `BENCH_STREAM` | `0` | Medir latencia del primer token |

#### Sesión 04: Comparación de Modelos
| Variable | Predeterminado | Propósito |
|----------|----------------|-----------|
| `SLM_ALIAS` | `phi-4-mini` | Modelo de lenguaje pequeño |
| `LLM_ALIAS` | `qwen2.5-7b` | Modelo de lenguaje grande |
| `COMPARE_PROMPT` | Preconfigurado | Prompt de comparación |
| `COMPARE_RETRIES` | `2` | Intentos de reintento |

#### Sesión 05: Orquestación Multi-Agente
| Variable | Predeterminado | Propósito |
|----------|----------------|-----------|
| `AGENT_MODEL_PRIMARY` | `phi-4-mini` | Modelo del agente investigador |
| `AGENT_MODEL_EDITOR` | `phi-4-mini` | Modelo del agente editor |
| `AGENT_QUESTION` | Preconfigurado | Pregunta de prueba |

### Configuración de Fiabilidad

| Variable | Predeterminado | Propósito |
|----------|----------------|-----------|
| `SHOW_USAGE` | `1` | Imprimir uso de tokens |
| `RETRY_ON_FAIL` | `1` | Activar lógica de reintento |
| `RETRY_BACKOFF` | `1.0` | Retraso en reintento (segundos) |

## Configuraciones Comunes

### Configuración de Desarrollo (Iteración Rápida)
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=phi-4-mini
BENCH_MODELS=phi-4-mini
SHOW_USAGE=1
```

### Configuración de Producción (Enfoque en Calidad)
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-7b
AGENT_MODEL_PRIMARY=phi-4-mini
AGENT_MODEL_EDITOR=qwen2.5-7b
SHOW_USAGE=0
```

### Configuración de Benchmarking
```bash
BENCH_MODELS=phi-4-mini,qwen2.5-0.5b,qwen2.5-7b
BENCH_ROUNDS=5
BENCH_STREAM=1
```

### Especialización Multi-Agente
```bash
AGENT_MODEL_PRIMARY=phi-4-mini        # Fast for research
AGENT_MODEL_EDITOR=qwen2.5-7b         # Quality for editing
```

### Desarrollo Remoto
```bash
FOUNDRY_LOCAL_ENDPOINT=http://dev-server.local:5273/v1
FOUNDRY_LOCAL_ALIAS=phi-4-mini
```

## Modelos Recomendados

### Según Caso de Uso

**Propósito General:**
- `phi-4-mini` - Equilibrio entre calidad y velocidad

**Respuestas Rápidas:**
- `qwen2.5-0.5b` - Muy rápido, bueno para clasificación
- `phi-4-mini` - Rápido con buena calidad

**Alta Calidad:**
- `qwen2.5-7b` - Mejor calidad, mayor uso de recursos
- `phi-4-mini` - Buena calidad, menos recursos

**Generación de Código:**
- `deepseek-coder-1.3b` - Especializado en código
- `phi-4-mini` - Propósito general para codificación

### Según Disponibilidad de Recursos

**Recursos Bajos (< 8GB RAM):**
```bash
FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b
SLM_ALIAS=qwen2.5-0.5b
LLM_ALIAS=phi-4-mini
```

**Recursos Medios (8-16GB RAM):**
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-7b
```

**Altos Recursos (16GB+ RAM):**
```bash
FOUNDRY_LOCAL_ALIAS=qwen2.5-7b
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-14b
```

## Configuración Avanzada

### Endpoints Personalizados

```bash
# Development environment
FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Staging environment
FOUNDRY_LOCAL_ENDPOINT=http://staging.internal:5273/v1

# Production environment
FOUNDRY_LOCAL_ENDPOINT=http://prod.internal:5273/v1
```

### Temperatura y Muestreo (Sobrescribir en Código)

```python
# In your scripts/notebooks
os.environ['TEMPERATURE'] = '0.7'
os.environ['TOP_P'] = '0.9'
```

### Configuración Híbrida de Azure OpenAI

```bash
# Use local for development
FOUNDRY_LOCAL_ALIAS=phi-4-mini

# Configure Azure for production fallback
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
AZURE_OPENAI_API_KEY=your-key-here
AZURE_OPENAI_API_VERSION=2024-08-01-preview
```

## Solución de Problemas

### Variables de Entorno No Cargadas

**Síntomas:**
- Los scripts usan modelos incorrectos
- Errores de conexión
- Variables no reconocidas

**Soluciones:**
```bash
# 1. Verify .env exists in repository root
ls -la .env  # macOS/Linux
dir .env     # Windows

# 2. Check file is not .env.txt (Windows)
# Ensure no hidden extension

# 3. For notebooks: Restart kernel
# Kernel > Restart

# 4. For scripts: Check working directory
pwd  # Should be in Workshop or repository root
```

### Problemas de Conexión al Servicio

**Síntomas:**
- Errores de "Conexión rechazada"
- "Servicio no disponible"
- Errores de tiempo de espera

**Soluciones:**
```bash
# 1. Check service status
foundry service status

# 2. Start if not running
foundry service start

# 3. Verify endpoint
# Check port in status output
foundry service status | grep "Port"

# 4. Update .env if needed
FOUNDRY_LOCAL_ENDPOINT=http://localhost:<port>
```

### Modelo No Encontrado

**Síntomas:**
- Errores de "Modelo no encontrado"
- "Alias no reconocido"

**Soluciones:**
```bash
# 1. List available models
foundry model list

# 2. Load required model
foundry model run phi-4-mini

# 3. Update .env with available model
FOUNDRY_LOCAL_ALIAS=<available-model>
```

### Errores de Importación

**Síntomas:**
- Errores de "Módulo no encontrado"

**Soluciones:**

```bash
# 1. Activate virtual environment
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux

# 2. Install dependencies
pip install -r requirements.txt
```

## Pruebas de Configuración

### Verificar Carga del Entorno

```python
# test_env.py
import os
from dotenv import load_dotenv

load_dotenv()

print("Core Configuration:")
print(f"  FOUNDRY_LOCAL_ALIAS: {os.getenv('FOUNDRY_LOCAL_ALIAS')}")
print(f"  FOUNDRY_LOCAL_ENDPOINT: {os.getenv('FOUNDRY_LOCAL_ENDPOINT') or 'auto'}")

print("\nSession 04:")
print(f"  SLM_ALIAS: {os.getenv('SLM_ALIAS')}")
print(f"  LLM_ALIAS: {os.getenv('LLM_ALIAS')}")

print("\nSession 05:")
print(f"  AGENT_MODEL_PRIMARY: {os.getenv('AGENT_MODEL_PRIMARY')}")
print(f"  AGENT_MODEL_EDITOR: {os.getenv('AGENT_MODEL_EDITOR')}")
```

### Probar Conexión a Foundry Local

```python
# test_connection.py
import os
from foundry_local import FoundryLocalManager

alias = os.getenv('FOUNDRY_LOCAL_ALIAS', 'phi-4-mini')
endpoint = os.getenv('FOUNDRY_LOCAL_ENDPOINT')

try:
    if endpoint:
        manager = FoundryLocalManager(alias, endpoint=endpoint)
    else:
        manager = FoundryLocalManager(alias)
    
    print(f"✓ Connected to {manager.endpoint}")
    print(f"✓ Model: {manager.get_model_info(alias).id}")
    print(f"✓ Available models: {len(manager.list_models())}")
except Exception as e:
    print(f"✗ Connection failed: {e}")
```

## Prácticas de Seguridad Recomendadas

### 1. Nunca Comparta Secretos

```bash
# .gitignore should include:
.env
.env.local
*.key
```

### 2. Use Archivos .env Separados

```bash
.env              # Default configuration
.env.local        # Local overrides (gitignored)
.env.production   # Production config (secure storage)
```

### 3. Rotar Claves API

```bash
# For Azure OpenAI or other cloud services
# Regularly rotate keys and update .env
```

### 4. Use Configuración Específica del Entorno

```bash
# Development
FOUNDRY_LOCAL_ENDPOINT=http://localhost:5273/v1

# Production (use secrets management)
FOUNDRY_LOCAL_ENDPOINT=${PROD_FOUNDRY_ENDPOINT}
```

## Documentación del SDK

- **Repositorio Principal**: https://github.com/microsoft/Foundry-Local
- **SDK de Python**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **Documentación de la API**: Consulte el repositorio del SDK para la última versión

## Recursos Adicionales

- `QUICK_START.md` - Guía de inicio rápido
- `Workshop/samples/*/README.md` - Guías específicas de ejemplos

---

**Última Actualización**: 2025-01-08  
**Versión**: 2.0  
**SDK**: Foundry Local Python SDK (última versión)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que surjan del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
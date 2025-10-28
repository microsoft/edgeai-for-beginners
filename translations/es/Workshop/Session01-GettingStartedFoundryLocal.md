<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0ab7d0dee137f224a011d9db00f0d2a2",
  "translation_date": "2025-10-28T17:12:53+00:00",
  "source_file": "Workshop/Session01-GettingStartedFoundryLocal.md",
  "language_code": "es"
}
-->
# Sesión 1: Introducción a Foundry Local

## Resumen

Comienza tu experiencia con Foundry Local instalándolo y configurándolo en Windows 11. Aprende a configurar la CLI, habilitar la aceleración por hardware y almacenar modelos en caché para una inferencia local rápida. Esta sesión práctica te guiará en la ejecución de modelos como Phi, Qwen, DeepSeek y GPT-OSS-20B utilizando comandos CLI reproducibles.

## Objetivos de Aprendizaje

Al finalizar esta sesión, podrás:

- **Instalar y Configurar**: Configurar Foundry Local en Windows 11 con ajustes de rendimiento óptimos.
- **Dominar Operaciones CLI**: Usar la CLI de Foundry Local para la gestión y despliegue de modelos.
- **Habilitar Aceleración por Hardware**: Configurar aceleración GPU con ONNXRuntime o WebGPU.
- **Desplegar Múltiples Modelos**: Ejecutar modelos phi-4, GPT-OSS-20B, Qwen y DeepSeek localmente.
- **Construir Tu Primera Aplicación**: Adaptar ejemplos existentes para usar el SDK de Python de Foundry Local.

# Probar el modelo (único mensaje no interactivo)
foundry model run phi-4-mini --prompt "Hola, preséntate"

- Windows 11 (22H2 o posterior)
# Listar modelos disponibles en el catálogo (los modelos cargados aparecen después de ejecutarse)
foundry model list
## NOTA: Actualmente no hay un flag dedicado `--running`; para ver cuáles están cargados, inicia un chat o inspecciona los registros del servicio.
- Python 3.10+ instalado
- Visual Studio Code con extensión de Python
- Privilegios de administrador para la instalación

### (Opcional) Variables de Entorno

Crea un archivo `.env` (o configúralo en la terminal) para hacer que los scripts sean portátiles:
# Comparar respuestas (no interactivo)
foundry model run gpt-oss-20b --prompt "Explica la IA en el borde en términos simples"
| Variable | Propósito | Ejemplo |
|----------|-----------|---------|
| `FOUNDRY_LOCAL_ALIAS` | Alias preferido del modelo (el catálogo selecciona automáticamente la mejor variante) | `phi-3.5-mini` |
| `FOUNDRY_LOCAL_ENDPOINT` | Sobrescribir el endpoint (de lo contrario, se selecciona automáticamente desde el gestor) | `http://localhost:5273/v1` |
| `FOUNDRY_LOCAL_STREAM` | Habilitar demostración de streaming | `true` |

> Si `FOUNDRY_LOCAL_ENDPOINT=auto` (o no configurado), se deriva del gestor del SDK.

## Flujo de Demostración (30 minutos)

### 1. Instalar Foundry Local y Verificar Configuración de la CLI (10 minutos)

# Listar modelos en caché
foundry cache list

```powershell
# Install via winget (recommended)
winget install Microsoft.FoundryLocal

# Or download from Microsoft Learn
# https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install
```

**macOS (Vista previa / Si es compatible)**

Si se proporciona un paquete nativo para macOS (consulta la documentación oficial para las últimas actualizaciones):

```bash
# Homebrew (if/when available)
brew update
brew install foundry-local  # hypothetical formula name

# Or manual download (tarball)
curl -L -o foundry-local.tar.gz "https://download.microsoft.com/foundry-local/latest/macos/foundry-local.tar.gz"
tar -xzf foundry-local.tar.gz
sudo ./install.sh
```

Si aún no hay binarios nativos para macOS disponibles, puedes:
1. Usar una VM de Windows 11 ARM/Intel (Parallels / UTM) y seguir los pasos de Windows.
2. Ejecutar modelos mediante un contenedor (si se publica una imagen de contenedor) y configurar `FOUNDRY_LOCAL_ENDPOINT` al puerto expuesto.

**Crear Entorno Virtual de Python (Multiplataforma)**

Windows PowerShell:
```powershell
py -m venv .venv
 .\.venv\Scripts\Activate.ps1
```

macOS / Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

Actualizar pip e instalar dependencias principales:
```bash
python -m pip install --upgrade pip
pip install foundry-local-sdk openai
```

#### Paso 1.2: Verificar Instalación

```powershell
# Check version
foundry --version

# Initialize configuration
foundry init

# View available commands
foundry --help
```

#### Paso 1.3: Configurar Entorno

```powershell
# Set up Python environment for Module08
cd Module08
py -m venv .venv
.\.venv\Scripts\activate

# Install Foundry Local Python SDK and dependencies
pip install foundry-local-sdk openai requests
```

### Inicialización del SDK (Recomendado)

En lugar de iniciar manualmente el servicio y ejecutar modelos, el **SDK de Python de Foundry Local** puede inicializar todo:

```python
from foundry_local import FoundryLocalManager
from openai import OpenAI
import os

alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-3.5-mini")

# Bootstraps service + downloads + loads most suitable variant for hardware
manager = FoundryLocalManager(alias)

print("Service running:", manager.is_service_running())
print("Endpoint:", manager.endpoint)
print("Cached models:", manager.list_cached_models())

client = OpenAI(base_url=manager.endpoint, api_key=manager.api_key or "not-needed")

resp = client.chat.completions.create(
    model=manager.get_model_info(alias).id,
    messages=[
        {"role": "system", "content": "You are a helpful local assistant."},
        {"role": "user", "content": "Hello"}
    ],
    max_tokens=120,
    temperature=0.5
)
print(resp.choices[0].message.content)
```

Si prefieres un control explícito, aún puedes usar la CLI + cliente OpenAI como se muestra más adelante.

### 2. Ejecutar Modelos Localmente mediante CLI (10 minutos)

#### Paso 3.1: Desplegar el Modelo Phi-4

```powershell
# Download and run phi-4-mini
foundry model run phi-4-mini

# Test the model (one-shot prompt)
foundry model run phi-4-mini --prompt "Hello, introduce yourself"

# NOTE: There is no `--running` flag; use `foundry model list` and recent activity to infer loaded models.
```

#### Paso 3.2: Desplegar GPT-OSS-20B

```powershell
# Download and run GPT-OSS-20B
foundry model run gpt-oss-20b

# Compare responses (one-shot prompt)
foundry model run gpt-oss-20b --prompt "Explain edge AI in simple terms"
```

#### Paso 3.3: Cargar Modelos Adicionales

```powershell
# Download Qwen model family
foundry model download qwen2.5-0.5b
foundry model download qwen2.5-7b

# Download DeepSeek models
foundry model download deepseek-coder-1.3b

# List cached models
foundry cache list
```

### 4. Proyecto Inicial: Adaptar 01-run-phi para Foundry Local (5 minutos)

#### Paso 4.1: Crear Aplicación Básica de Chat

Crear `samples/01-foundry-quickstart/chat_quickstart.py` (actualizado para usar el gestor si está disponible):

```python
#!/usr/bin/env python3
"""
Foundry Local Chat Quickstart
Demo: Basic chat interaction using Foundry Local Python SDK
Reference: https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/reference/reference-sdk?pivots=programming-language-python
"""

import os, sys
from openai import OpenAI
try:
    from foundry_local import FoundryLocalManager  # control-plane SDK
except ImportError:
    FoundryLocalManager = None

def main():
    """Main chat function using Foundry Local SDK"""
    
    # Preferred: bootstrap via SDK manager (auto start + download + load)
    alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-3.5-mini")
    if FoundryLocalManager:
        manager = FoundryLocalManager(alias)
        endpoint = manager.endpoint
        model_id = manager.get_model_info(alias).id
        api_key = manager.api_key or "not-needed"
    else:
        # Fallback: assume default endpoint & alias already running via CLI
        endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT", "http://localhost:5273/v1")
        model_id = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-4-mini")
        api_key = "not-needed"

    client = OpenAI(base_url=endpoint, api_key=api_key)
    
    # Get user input
    if len(sys.argv) > 1:
        user_message = " ".join(sys.argv[1:])
    else:
        user_message = input("Enter your message: ")
    
    try:
        # Make chat completion request
        response = client.chat.completions.create(
            model=model_id,
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant powered by Microsoft Foundry Local."},
                {"role": "user", "content": user_message}
            ],
            max_tokens=500,
            temperature=0.7
        )
        
        # Display response
        print(f"\nModel: {response.model}")
        print(f"Response: {response.choices[0].message.content}")
        print(f"Tokens used: {response.usage.total_tokens if response.usage else 'N/A'}")
        
    except Exception as e:
        print(f"Error: {e}")
        print("\nTroubleshooting:")
    print("1. Ensure Foundry Local is running: foundry status")
    print("2. List models: foundry model list")
    print(f"3. Start model if needed: foundry model run {model_id}")
    print("4. Or let SDK bootstrap: pip install foundry-local-sdk")

if __name__ == "__main__":
    main()
```

#### Paso 4.2: Probar la Aplicación

```powershell
# Ensure phi-4-mini is running
foundry model run phi-4-mini

# Run the quickstart app
python samples/01-foundry-quickstart/chat_quickstart.py "What is Microsoft Foundry Local?"

# Try interactive mode
python samples/01-foundry-quickstart/chat_quickstart.py
```

## Conceptos Clave Cubiertos

### 1. Arquitectura de Foundry Local

- **Motor de Inferencia Local**: Ejecuta modelos completamente en tu dispositivo.
- **Compatibilidad con el SDK de OpenAI**: Integración fluida con el código existente de OpenAI.
- **Gestión de Modelos**: Descargar, almacenar en caché y ejecutar múltiples modelos de manera eficiente.
- **Optimización de Hardware**: Aprovechar la aceleración de GPU, NPU y CPU.

### 2. Referencia de Comandos CLI

```powershell
# Core Commands
foundry --version              # Check installation
# Model Management
foundry model list             # List available models
foundry model unload <name>    # Unload from memory

foundry config list            # Current configuration
```

### 3. Integración del SDK de Python

```python
# Basic client setup
from foundry_local import FoundryLocalManager
from openai import OpenAI
import os

alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-3.5-mini")
manager = FoundryLocalManager(alias)
client = OpenAI(base_url=manager.endpoint, api_key=manager.api_key or "not-needed")

response = client.chat.completions.create(
    model=manager.get_model_info(alias).id,
    messages=[{"role": "user", "content": "Hello!"}],
    max_tokens=50
)
print(response.choices[0].message.content)

# Streaming example
stream = client.chat.completions.create(
    model=manager.get_model_info(alias).id,
    messages=[{"role": "user", "content": "Give a 1-sentence definition of edge AI."}],
    stream=True,
    max_tokens=60,
    temperature=0.4
)
for chunk in stream:
    delta = chunk.choices[0].delta
    if delta and delta.content:
        print(delta.content, end="", flush=True)
print()
```

## Solución de Problemas Comunes

### Problema 1: "Comando Foundry no encontrado"

**Solución:**
```powershell
# Restart PowerShell after installation
# Or manually add to PATH
$env:PATH += ";C:\Program Files\Microsoft\FoundryLocal"
```

### Problema 2: "El modelo no se pudo cargar"

**Solución:**
```powershell
# Check available memory
foundry system info

# Try smaller model first
foundry model run phi-4-mini

# Check disk space for model cache
dir "$env:USERPROFILE\.foundry\models"
```

### Problema 3: "Conexión rechazada en localhost:5273"

**Solución:**
```powershell
# Check if service is running
foundry status

# Start service if needed
foundry service start

# Check for port conflicts
netstat -an | findstr 5273
```

## Consejos para Optimizar el Rendimiento

### 1. Estrategia de Selección de Modelos

- **Phi-4-mini**: Mejor para tareas generales, menor uso de memoria.
- **Qwen2.5-0.5b**: Inferencia más rápida, recursos mínimos.
- **GPT-OSS-20B**: Máxima calidad, requiere más recursos.
- **DeepSeek-Coder**: Optimizado para tareas de programación.

### 2. Optimización de Hardware

```powershell
# Enable all acceleration options
foundry config set compute.onnx.enable_gpu true
foundry config set compute.webgpu.enabled true
foundry config set compute.cpu.threads auto

# Optimize memory usage
foundry config set model.cache.max_size 10GB
foundry config set model.preload false
```

### 3. Monitoreo del Rendimiento

```powershell
# Performance & latency measurement
# Use the Python benchmark script (Session 3) instead of legacy 'model stats' or 'model benchmark' commands.
# Example:
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
python Workshop\samples\session03\benchmark_oss_models.py

# Re-run after enabling GPU acceleration to compare:
foundry config set compute.onnx.enable_gpu true
python Workshop\samples\session03\benchmark_oss_models.py
```

### Mejoras Opcionales

| Mejora | Qué | Cómo |
|--------|-----|------|
| Utilidades Compartidas | Eliminar lógica duplicada de cliente/inicialización | Usar `Workshop/samples/workshop_utils.py` (`get_client`, `chat_once`) |
| Visibilidad del Uso de Tokens | Enseñar sobre costos/eficiencia desde el principio | Configurar `SHOW_USAGE=1` para imprimir tokens de entrada/completados/totales |
| Comparaciones Deterministas | Pruebas de rendimiento y regresión estables | Usar `temperature=0`, `top_p=1`, texto de mensaje consistente |
| Latencia del Primer Token | Métrica de respuesta percibida | Adaptar script de prueba con streaming (`BENCH_STREAM=1`) |
| Reintento en Errores Transitorios | Demostraciones resilientes en inicio frío | `RETRY_ON_FAIL=1` (por defecto) y ajustar `RETRY_BACKOFF` |
| Pruebas de Fumado | Verificación rápida de flujos clave | Ejecutar `python Workshop/tests/smoke.py` antes de un taller |
| Perfiles de Alias de Modelos | Cambiar rápidamente el conjunto de modelos entre máquinas | Mantener `.env` con `FOUNDRY_LOCAL_ALIAS`, `SLM_ALIAS`, `LLM_ALIAS` |
| Eficiencia de Caché | Evitar calentamientos repetidos en ejecuciones múltiples | Utilidades de gestores de caché; reutilizar entre scripts/cuadernos |
| Calentamiento en la Primera Ejecución | Reducir picos de latencia p95 | Ejecutar un mensaje pequeño después de crear `FoundryLocalManager` |

Ejemplo de base cálida determinista (PowerShell):

```powershell
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
python Workshop\samples\session01\chat_bootstrap.py "List two privacy benefits of local inference." | Out-Null
python Workshop\samples\session01\chat_bootstrap.py "List two privacy benefits of local inference."
```

Deberías ver una salida similar y conteos de tokens idénticos en la segunda ejecución, confirmando la determinación.

## Próximos Pasos

Después de completar esta sesión:

1. **Explora la Sesión 2**: Construye soluciones de IA con Azure AI Foundry RAG.
2. **Prueba Diferentes Modelos**: Experimenta con Qwen, DeepSeek y otras familias de modelos.
3. **Optimiza el Rendimiento**: Ajusta configuraciones para tu hardware específico.
4. **Construye Aplicaciones Personalizadas**: Usa el SDK de Foundry Local en tus propios proyectos.

## Recursos Adicionales

### Documentación
- [Referencia del SDK de Python de Foundry Local](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/reference/reference-sdk?pivots=programming-language-python)
- [Guía de Instalación de Foundry Local](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install)
- [Catálogo de Modelos](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/models)

### Código de Ejemplo
- [Módulo08 Ejemplo 01](./samples/01/README.md) - Inicio rápido de chat REST
- [Módulo08 Ejemplo 02](./samples/02/README.md) - Integración con SDK de OpenAI
- [Módulo08 Ejemplo 03](./samples/03/README.md) - Descubrimiento y evaluación de modelos

### Comunidad
- [Discusiones en GitHub de Foundry Local](https://github.com/microsoft/Foundry-Local/discussions)
- [Comunidad de Azure AI](https://techcommunity.microsoft.com/category/artificialintelligence)

---

**Duración de la Sesión**: 30 minutos de práctica + 15 minutos de preguntas y respuestas  
**Nivel de Dificultad**: Principiante  
**Requisitos Previos**: Windows 11, Python 3.10+, acceso de administrador  

## Escenario de Ejemplo y Mapeo del Taller

| Script / Cuaderno del Taller | Escenario | Objetivo | Ejemplo de Entrada(s) | Dataset Necesario |
|------------------------------|-----------|----------|------------------------|-------------------|
| `samples/session01/chat_bootstrap.py` / `notebooks/session01_chat_bootstrap.ipynb` | Equipo interno de TI evaluando la inferencia en el dispositivo para un portal de evaluación de privacidad | Demostrar que SLM local responde con latencia inferior al segundo en mensajes estándar | "Menciona dos beneficios de la inferencia local." | Ninguno (mensaje único) |
| Bloque de código de adaptación de inicio rápido | Desarrollador migrando un script existente de OpenAI a Foundry Local | Mostrar compatibilidad directa | "Menciona dos beneficios de la inferencia local." | Solo mensaje en línea |

### Narrativa del Escenario
El equipo de seguridad y cumplimiento debe validar si los datos sensibles de prototipos pueden procesarse localmente. Ejecutan el script de inicialización con varios mensajes (privacidad, latencia, costo) utilizando un modo determinista con temperatura=0 para capturar resultados base para comparaciones posteriores (evaluación en la Sesión 3 y contraste SLM vs LLM en la Sesión 4).

### Conjunto Mínimo de Mensajes en JSON (opcional)
```json
[
    "List two benefits of local inference.",
    "Summarize why keeping data on device improves privacy.",
    "Give one trade‑off when choosing an SLM over a large model."
]
```

Usa esta lista para crear un bucle de evaluación reproducible o para iniciar un futuro sistema de pruebas de regresión.

---

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse como la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que surjan del uso de esta traducción.
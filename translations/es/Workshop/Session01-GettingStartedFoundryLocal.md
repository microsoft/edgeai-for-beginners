<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8c30436578b1bd604c48233ecdd39701",
  "translation_date": "2025-11-11T21:23:12+00:00",
  "source_file": "Workshop/Session01-GettingStartedFoundryLocal.md",
  "language_code": "es"
}
-->
# Sesión 1: Introducción a Foundry Local

## Resumen

Aprende a instalar, configurar y ejecutar tus primeros modelos de IA utilizando Microsoft Foundry Local. Esta sesión práctica ofrece una introducción paso a paso a la inferencia local, desde la instalación hasta la creación de tu primera aplicación de chat utilizando modelos como Phi-4, Qwen y DeepSeek.

## Objetivos de Aprendizaje

Al finalizar esta sesión, podrás:

- **Instalar y Configurar**: Configurar Foundry Local con verificación adecuada de instalación
- **Dominar Operaciones CLI**: Usar la CLI de Foundry Local para la gestión y despliegue de modelos
- **Ejecutar tu Primer Modelo**: Desplegar e interactuar exitosamente con un modelo de IA local
- **Crear una Aplicación de Chat**: Desarrollar una aplicación básica de chat utilizando el SDK de Python de Foundry Local
- **Comprender la IA Local**: Entender los fundamentos de la inferencia local y la gestión de modelos

## Requisitos Previos

### Requisitos del Sistema

- **Windows**: Windows 11 (22H2 o posterior) O **macOS**: macOS 11+ (soporte limitado)
- **RAM**: Mínimo 8GB, recomendado 16GB+
- **Almacenamiento**: 10GB+ de espacio libre para modelos
- **Python**: Instalado 3.10 o posterior
- **Acceso de Administrador**: Privilegios de administrador para la instalación

### Entorno de Desarrollo

- Visual Studio Code con extensión de Python (recomendado)
- Acceso a línea de comandos (PowerShell en Windows, Terminal en macOS)
- Git para clonar repositorios (opcional)

## Flujo del Taller (30 minutos)

### Paso 1: Instalar Foundry Local (5 minutos)

#### Instalación en Windows

Instala Foundry Local utilizando el gestor de paquetes de Windows:

```powershell
# Install via winget (recommended)
winget install Microsoft.FoundryLocal
```

Alternativa: Descarga directamente desde [Microsoft Learn](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install)

#### Instalación en macOS (Soporte Limitado)

> [!NOTE] 
> El soporte para macOS está actualmente en vista previa. Consulta la documentación oficial para la última disponibilidad.

Si está disponible, instala usando Homebrew:

```bash
# If Homebrew formula is available
brew update
brew install foundry-local

# Or manual download (check official docs for latest)
curl -L -o foundry-local.tar.gz "https://download.microsoft.com/foundry-local/latest/macos/foundry-local.tar.gz"
tar -xzf foundry-local.tar.gz
sudo ./install.sh
```

**Alternativa para usuarios de macOS:**
- Usa una máquina virtual de Windows 11 (Parallels/UTM) y sigue los pasos de Windows
- Ejecuta mediante contenedor si está disponible y configura `FOUNDRY_LOCAL_ENDPOINT`

### Paso 2: Verificar la Instalación (3 minutos)

Después de la instalación, reinicia tu terminal y verifica que Foundry Local esté funcionando:

```powershell
# Check if Foundry Local is installed correctly
foundry --version

# View available commands
foundry --help
```

El resultado esperado debería mostrar información de la versión y los comandos disponibles.

### Paso 3: Configurar el Entorno de Python (5 minutos)

Crea un entorno de Python dedicado para este taller:

**Windows:**
```powershell
# Create virtual environment
py -m venv .venv

# Activate environment
.\.venv\Scripts\Activate.ps1

# Upgrade pip and install dependencies
python -m pip install --upgrade pip
pip install foundry-local-sdk openai
```

**macOS/Linux:**
```bash
# Create virtual environment
python3 -m venv .venv

# Activate environment
source .venv/bin/activate

# Upgrade pip and install dependencies
python -m pip install --upgrade pip
pip install foundry-local-sdk openai
```

### Paso 4: Ejecutar tu Primer Modelo (7 minutos)

¡Ahora ejecutemos nuestro primer modelo de IA local!

#### Comienza con Phi-4 Mini (Modelo Recomendado)

```powershell
# Download and start phi-4-mini (lightweight, fast)
foundry model run phi-4-mini

# Test the model with a simple prompt
foundry model run phi-4-mini --prompt "Hello, introduce yourself in one sentence"
```

> [!TIP]
> Este comando descarga el modelo (la primera vez) y comienza automáticamente el servicio de Foundry Local.

#### Verifica lo que está en ejecución

```powershell
# List available models (shows downloaded models)
foundry model list

# Check service status
foundry service status

# See what models are cached locally
foundry cache list
```

#### Prueba Diferentes Modelos

Una vez que phi-4-mini esté funcionando, experimenta con otros modelos:

```powershell
# Larger model with better capabilities
foundry model run gpt-oss-20b --prompt "Explain edge AI in simple terms"

# Fast, efficient model
foundry model run qwen2.5-0.5b --prompt "What are the benefits of local AI inference?"
```

### Paso 5: Crear tu Primera Aplicación de Chat (10 minutos)

Ahora vamos a crear una aplicación en Python que utilice los modelos que acabamos de iniciar.

#### Crear el Script de Chat

Crea un nuevo archivo llamado `my_first_chat.py` (o utiliza el ejemplo proporcionado):

```python
#!/usr/bin/env python3
"""
My First Foundry Local Chat Application
Using FoundryLocalManager for automatic service management
"""

import os
from foundry_local import FoundryLocalManager
from openai import OpenAI

def main():
    # Get model alias from environment or use default
    alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-4-mini")
    
    try:
        # Initialize Foundry Local Manager (auto-starts service, downloads model)
        manager = FoundryLocalManager(alias)
        
        # Create OpenAI client pointing to local endpoint
        client = OpenAI(
            base_url=manager.endpoint,
            api_key=manager.api_key or "not-needed"
        )
        
        # Get the actual model ID for this alias
        model_id = manager.get_model_info(alias).id
        
        print("🤖 Welcome to your first local AI chat!")
        print(f"� Using model: {alias} -> {model_id}")
        print(f"🌐 Endpoint: {manager.endpoint}")
        print("�💡 Type 'quit' to exit\n")
        
    except Exception as e:
        print(f"❌ Failed to initialize Foundry Local: {e}")
        print("💡 Make sure Foundry Local is installed: foundry --version")
        return
    
    while True:
        # Get user input
        user_message = input("You: ").strip()
        
        if user_message.lower() in ['quit', 'exit', 'bye']:
            print("👋 Goodbye!")
            break
            
        if not user_message:
            continue
            
        try:
            # Send message to local AI model
            response = client.chat.completions.create(
                model=model_id,
                messages=[
                    {"role": "system", "content": "You are a helpful AI assistant running locally."},
                    {"role": "user", "content": user_message}
                ],
                max_tokens=200,
                temperature=0.7
            )
            
            # Display the response
            ai_response = response.choices[0].message.content
            print(f"🤖 AI: {ai_response}\n")
            
        except Exception as e:
            print(f"❌ Error: {e}")
            print("💡 Check service status: foundry service status\n")

if __name__ == "__main__":
    main()
```

> [!TIP]
> **Ejemplos Relacionados**: Para un uso más avanzado, consulta:
>
> - **Ejemplo en Python**: `Workshop/samples/session01/chat_bootstrap.py` - Incluye respuestas en streaming y manejo de errores
> - **Notebook Jupyter**: `Workshop/notebooks/session01_chat_bootstrap.ipynb` - Versión interactiva con explicaciones detalladas

#### Prueba tu Aplicación de Chat

```powershell
# No need to manually start models - FoundryLocalManager handles this!
# Just run your chat application
python my_first_chat.py
```

Alternativa: Usa directamente los ejemplos proporcionados

```powershell
# Try the complete sample with streaming support
cd Workshop/samples
python -m session01.chat_bootstrap "Your question here"
```

O explora el notebook interactivo  
Abre Workshop/notebooks/session01_chat_bootstrap.ipynb en VS Code

Prueba estas conversaciones de ejemplo:

- "¿Qué es Microsoft Foundry Local?"
- "Enumera 3 beneficios de ejecutar modelos de IA localmente"
- "Ayúdame a entender la IA en el edge"

## Lo que Has Logrado

¡Felicidades! Has logrado:

1. ✅ **Instalar Foundry Local** y verificar que funciona
2. ✅ **Iniciar tu primer modelo de IA** (phi-4-mini) localmente
3. ✅ **Probar diferentes modelos** mediante línea de comandos
4. ✅ **Crear una aplicación de chat** que se conecta a tu IA local
5. ✅ **Experimentar la inferencia de IA local** sin dependencias en la nube

## Comprendiendo lo que Sucedió

### Inferencia de IA Local

- Tus modelos de IA se ejecutan completamente en tu computadora
- No se envían datos a la nube
- Las respuestas se generan localmente utilizando tu CPU/GPU
- Se mantiene la privacidad y seguridad

### Gestión de Modelos

- `foundry model run` descarga e inicia modelos
- **FoundryLocalManager SDK** maneja automáticamente el inicio del servicio y la carga de modelos
- Los modelos se almacenan en caché localmente para uso futuro
- Se pueden descargar múltiples modelos, pero típicamente se ejecuta uno a la vez
- El servicio gestiona automáticamente el ciclo de vida del modelo

### Enfoques SDK vs CLI

- **Enfoque CLI**: Gestión manual de modelos con `foundry model run <model>`
- **Enfoque SDK**: Gestión automática de servicios y modelos con `FoundryLocalManager(alias)`
- **Recomendación**: Usa SDK para aplicaciones, CLI para pruebas y exploración

## Referencia de Comandos Comunes

### Comandos Esenciales de CLI

```powershell
# Installation & Setup
foundry --version              # Check installation
foundry --help                 # View all commands

# Model Management
foundry model list             # List available models
foundry model run <model>      # Download and start a model
foundry model run <model> --prompt "text"  # One-shot prompt
foundry cache list             # Show downloaded models

# Service Management
foundry service status         # Check if service is running
foundry service start          # Start the service manually
foundry service stop           # Stop the service
```

### Recomendaciones de Modelos

- **phi-4-mini**: Mejor modelo inicial - rápido, ligero, buena calidad
- **qwen2.5-0.5b**: Inferencia más rápida, uso mínimo de memoria
- **gpt-oss-20b**: Respuestas de mayor calidad, requiere más recursos
- **deepseek-coder-1.3b**: Optimizado para tareas de programación y código

## Solución de Problemas

### "Comando Foundry no encontrado"

**Solución:**

```powershell
# Restart your terminal after installation
# Or manually add to PATH (Windows)
$env:PATH += ";C:\Program Files\Microsoft\FoundryLocal"
```

### "Error al cargar el modelo"

**Solución:**

```powershell
# Check available system memory
foundry service status

# Try a smaller model first
foundry model run phi-4-mini

# Check disk space for model downloads
# Models are stored in: %USERPROFILE%\.foundry\models (Windows)
```

### "Conexión rechazada en localhost"

**Solución:**

```powershell
# Check if service is running
foundry service status

# Start service if needed
foundry service start

# Verify the port (default is 5273)
# Check for port conflicts with: netstat -an | findstr 5273
```

## Próximos Pasos

### Acciones Inmediatas

1. **Experimenta** con diferentes modelos y prompts
2. **Modifica** tu aplicación de chat para probar diferentes modelos
3. **Crea** tus propios prompts y prueba las respuestas
4. **Explora** la Sesión 2: Construcción de aplicaciones RAG

### Ruta de Aprendizaje Avanzada

1. **Sesión 2**: Construye soluciones de IA con RAG (Generación Aumentada por Recuperación)
2. **Sesión 3**: Compara diferentes modelos de código abierto
3. **Sesión 4**: Trabaja con modelos de última generación
4. **Sesión 5**: Construye sistemas de IA multiagente

## Variables de Entorno (Opcional)

Para un uso más avanzado, puedes configurar estas variables de entorno:

| Variable | Propósito | Ejemplo |
|----------|-----------|---------|
| `FOUNDRY_LOCAL_ALIAS` | Modelo predeterminado a usar | `phi-4-mini` |
| `FOUNDRY_LOCAL_ENDPOINT` | Sobrescribir URL del endpoint | `http://localhost:5273/v1` |

Crea un archivo `.env` en tu directorio de proyecto:
```
FOUNDRY_LOCAL_ALIAS=phi-4-mini
FOUNDRY_LOCAL_ENDPOINT=auto
```

## Recursos Adicionales

### Documentación

- [Referencia del SDK de Python de Foundry Local](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/reference/reference-sdk?pivots=programming-language-python)
- [Guía de Instalación de Foundry Local](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install)
- [Catálogo de Modelos](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/models)

### Código de Ejemplo

- **Ejemplo en Python de la Sesión01**: `Workshop/samples/session01/chat_bootstrap.py` - Aplicación de chat completa con streaming
- **Notebook de la Sesión01**: `Workshop/notebooks/session01_chat_bootstrap.ipynb` - Tutorial interactivo  
- [Ejemplo del Módulo08 01](../Module08/samples/01/README.md) - Inicio rápido de chat REST
- [Ejemplo del Módulo08 02](../Module08/samples/02/README.md) - Integración con OpenAI SDK
- [Ejemplo del Módulo08 03](../Module08/samples/03/README.md) - Descubrimiento y evaluación de modelos

### Comunidad

- [Discusiones en GitHub de Foundry Local](https://github.com/microsoft/Foundry-Local/discussions)
- [Comunidad de Azure AI](https://techcommunity.microsoft.com/category/artificialintelligence)

---

**Duración de la Sesión**: 30 minutos prácticos + 15 minutos de preguntas y respuestas  
**Nivel de Dificultad**: Principiante  
**Requisitos Previos**: Windows 11/macOS 11+, Python 3.10+, Acceso de administrador

## Escenario de Ejemplo del Taller

### Contexto Real

**Escenario**: Un equipo de TI empresarial necesita evaluar la inferencia de IA en el dispositivo para procesar comentarios sensibles de empleados sin enviar datos a servicios externos.

**Tu Objetivo**: Demostrar que los modelos de IA locales pueden proporcionar respuestas de calidad con latencia inferior a un segundo mientras se mantiene la privacidad total de los datos.

### Prompts de Prueba

Usa estos prompts para validar tu configuración:

```json
[
    "List two benefits of local inference.",
    "Summarize why keeping data on device improves privacy.",
    "Give one trade-off when choosing a small model over a large model."
]
```

### Criterios de Éxito

- ✅ Todos los prompts obtienen respuestas en menos de 2 segundos
- ✅ No se envían datos fuera de tu máquina local
- ✅ Las respuestas son relevantes y útiles
- ✅ Tu aplicación de chat funciona sin problemas

Esta validación asegura que tu configuración de Foundry Local está lista para los talleres avanzados de las Sesiones 2-6.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que surjan del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
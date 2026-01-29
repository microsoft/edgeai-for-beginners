# AGENTS.md

> **Guía para desarrolladores que contribuyen a EdgeAI para principiantes**
> 
> Este documento proporciona información completa para desarrolladores, agentes de IA y colaboradores que trabajan con este repositorio. Cubre la configuración, flujos de trabajo de desarrollo, pruebas y mejores prácticas.
> 
> **Última actualización**: 30 de octubre de 2025 | **Versión del documento**: 3.0

## Tabla de Contenidos

- [Descripción del Proyecto](../..)
- [Estructura del Repositorio](../..)
- [Requisitos Previos](../..)
- [Comandos de Configuración](../..)
- [Flujo de Trabajo de Desarrollo](../..)
- [Instrucciones de Pruebas](../..)
- [Guías de Estilo de Código](../..)
- [Guías para Solicitudes de Extracción](../..)
- [Sistema de Traducción](../..)
- [Integración Local de Foundry](../..)
- [Construcción y Despliegue](../..)
- [Problemas Comunes y Solución de Problemas](../..)
- [Recursos Adicionales](../..)
- [Notas Específicas del Proyecto](../..)
- [Obteniendo Ayuda](../..)

## Descripción del Proyecto

EdgeAI para principiantes es un repositorio educativo integral que enseña desarrollo de Edge AI con Modelos de Lenguaje Pequeños (SLMs). El curso cubre fundamentos de EdgeAI, despliegue de modelos, técnicas de optimización e implementaciones listas para producción utilizando Microsoft Foundry Local y varios marcos de IA.

**Tecnologías Clave:**
- Python 3.8+ (lenguaje principal para muestras de IA/ML)
- .NET C# (muestras de IA/ML)
- JavaScript/Node.js con Electron (para aplicaciones de escritorio)
- SDK de Microsoft Foundry Local
- Microsoft Windows ML 
- VSCode AI Toolkit
- SDK de OpenAI
- Marcos de IA: LangChain, Semantic Kernel, Chainlit
- Optimización de Modelos: Llama.cpp, Microsoft Olive, OpenVINO, Apple MLX

**Tipo de Repositorio:** Repositorio de contenido educativo con 8 módulos y 10 aplicaciones de muestra completas

**Arquitectura:** Ruta de aprendizaje de múltiples módulos con ejemplos prácticos que demuestran patrones de despliegue de Edge AI

## Estructura del Repositorio

```
edgeai-for-beginners/
├── introduction.md          # Course introduction and overview
├── Module01-07/            # Core educational modules (Markdown)
├── Module08/               # Foundry Local toolkit with 10 samples
│   ├── samples/01-06/     # Foundation samples (Python)
│   ├── samples/07/        # API client (Python)
│   ├── samples/08/        # Windows 11 chat app (Electron)
│   └── samples/09-10/     # Advanced multi-agent systems (Python)
├── Workshop/               # Hands-on workshop materials
│   ├── samples/           # Workshop Python samples with utilities
│   │   ├── session01/     # Chat bootstrap samples
│   │   ├── session02-06/  # Progressive workshop sessions
│   │   └── util/          # Workshop utility modules
│   ├── notebooks/         # Jupyter notebook tutorials
│   └── scripts/           # Validation and testing tools
├── translations/          # Multi-language translations (50+ languages)
├── translated_images/     # Localized images
└── imgs/                  # Course images and assets
```

## Requisitos Previos

### Herramientas Requeridas

- **Python 3.8+** - Para muestras y cuadernos de IA/ML
- **Node.js 16+** - Para la aplicación de muestra de Electron
- **Git** - Para control de versiones
- **Microsoft Foundry Local** - Para ejecutar modelos de IA localmente

### Herramientas Recomendadas

- **Visual Studio Code** - Con extensiones de Python, Jupyter y Pylance
- **Windows Terminal** - Para una mejor experiencia en la línea de comandos (usuarios de Windows)
- **Docker** - Para desarrollo en contenedores (opcional)

### Requisitos del Sistema

- **RAM**: Mínimo 8GB, recomendado 16GB+ para escenarios de múltiples modelos
- **Almacenamiento**: 10GB+ de espacio libre para modelos y dependencias
- **SO**: Windows 10/11, macOS 11+ o Linux (Ubuntu 20.04+)
- **Hardware**: CPU con soporte AVX2; GPU (CUDA, Qualcomm NPU) opcional pero recomendado

### Conocimientos Previos

- Comprensión básica de programación en Python
- Familiaridad con interfaces de línea de comandos
- Comprensión de conceptos de IA/ML (para desarrollo de muestras)
- Flujos de trabajo de Git y procesos de solicitudes de extracción

## Comandos de Configuración

### Configuración del Repositorio

```bash
# Clone the repository
git clone https://github.com/microsoft/edgeai-for-beginners.git
cd edgeai-for-beginners

# No build step required - this is primarily an educational content repository
```

### Configuración de Muestras en Python (Módulo08 y muestras del taller)

```bash
# Create and activate virtual environment
python -m venv .venv
# On Windows
.venv\Scripts\activate
# On macOS/Linux
source .venv/bin/activate

# Install Foundry Local SDK and dependencies
pip install foundry-local-sdk openai

# Install additional dependencies for Module08 samples
cd Module08
pip install -r requirements.txt

# Install Workshop dependencies
cd ../Workshop
pip install -r requirements.txt
```

### Configuración de Muestras en Node.js (Muestra 08 - Aplicación de Chat para Windows)

```bash
cd Module08/samples/08
npm install

# Start in development mode
npm run dev

# Build for production
npm run build

# Create installer
npm run dist
```

### Configuración de Foundry Local

Foundry Local es necesario para ejecutar las muestras. Descárgalo e instálalo desde el repositorio oficial:

**Instalación:**
- **Windows**: `winget install Microsoft.FoundryLocal`
- **macOS**: `brew tap microsoft/foundrylocal && brew install foundrylocal`
- **Manual**: Descarga desde [página de lanzamientos](https://github.com/microsoft/Foundry-Local/releases)

**Inicio Rápido:**
```bash
# Run your first model (auto-downloads if needed)
foundry model run phi-4-mini

# List available models
foundry model ls

# Check service status
foundry service status
```

**Nota**: Foundry Local selecciona automáticamente la mejor variante de modelo para tu hardware (GPU CUDA, NPU Qualcomm o CPU).

## Flujo de Trabajo de Desarrollo

### Desarrollo de Contenido

Este repositorio contiene principalmente **contenido educativo en Markdown**. Al realizar cambios:

1. Edita los archivos `.md` en los directorios de módulos correspondientes
2. Sigue los patrones de formato existentes
3. Asegúrate de que los ejemplos de código sean precisos y estén probados
4. Actualiza el contenido traducido correspondiente si es necesario (o deja que la automatización lo maneje)

### Desarrollo de Aplicaciones de Muestra

Para las muestras de Python del Módulo08 (muestras 01-07, 09-10):
```bash
cd Module08
python samples/01/chat_quickstart.py "Test message"
```

Para las muestras de Python del taller:
```bash
cd Workshop/samples/session01
python chat_bootstrap.py "Test message"
```

Para la muestra de Electron (muestra 08):
```bash
cd Module08/samples/08
npm run dev  # Development with hot reload
```

### Pruebas de Aplicaciones de Muestra

Las muestras de Python no tienen pruebas automatizadas pero pueden validarse ejecutándolas:
```bash
# Test basic chat functionality
python samples/01/chat_quickstart.py "Hello"

# Test with specific model
set MODEL=phi-4-mini
python samples/02/openai_sdk_client.py
```

La muestra de Electron tiene infraestructura de pruebas:
```bash
cd Module08/samples/08
npm test           # Run unit tests
npm run test:e2e   # Run end-to-end tests
npm run lint       # Check code style
```

## Instrucciones de Pruebas

### Validación de Contenido

El repositorio utiliza flujos de trabajo de traducción automatizados. No se requieren pruebas manuales para las traducciones.

**Validación manual para cambios de contenido:**
1. Revisa la representación de Markdown al previsualizar los archivos `.md`
2. Verifica que todos los enlaces apunten a destinos válidos
3. Prueba cualquier fragmento de código incluido en la documentación
4. Asegúrate de que las imágenes se carguen correctamente

### Pruebas de Aplicaciones de Muestra

**Módulo08/muestras/08 (aplicación Electron) tiene pruebas completas:**
```bash
cd Module08/samples/08

# Run all tests
npm test

# Run unit tests only
npm test -- --testPathPattern=unit

# Run integration tests
npm run test:integration

# Run E2E tests
npm run test:e2e

# Check test coverage
npm test -- --coverage
```

**Las muestras de Python deben probarse manualmente:**
```bash
# Module08 samples
python samples/01/chat_quickstart.py "Test prompt"
python samples/04/chainlit_rag.py
python samples/09/multi_agent_system.py

# Workshop samples
cd Workshop/samples/session01
python chat_bootstrap.py "Test prompt"

# Use Workshop validation tools
cd Workshop/scripts
python validate_samples.py  # Validate syntax and imports
python test_samples.py      # Run smoke tests
```

## Guías de Estilo de Código

### Contenido en Markdown

- Usa una jerarquía de encabezados consistente (# para título, ## para secciones principales, ### para subsecciones)
- Incluye bloques de código con especificadores de lenguaje: ```python, ```bash, ```javascript
- Sigue el formato existente para tablas, listas y énfasis
- Mantén las líneas legibles (apunta a ~80-100 caracteres, pero no es estricto)
- Usa enlaces relativos para referencias internas

### Estilo de Código en Python

- Sigue las convenciones de PEP 8
- Usa sugerencias de tipo cuando sea apropiado
- Incluye docstrings para funciones y clases
- Usa nombres de variables significativos
- Mantén las funciones enfocadas y concisas

### Estilo de Código en JavaScript/Node.js

```bash
# Electron sample follows ESLint configuration
cd Module08/samples/08
npm run lint        # Check for style issues
npm run lint:fix    # Auto-fix style issues
npm run format      # Format with Prettier
```

**Convenciones clave:**
- Configuración de ESLint proporcionada en la muestra 08
- Prettier para formato de código
- Usa sintaxis moderna ES6+
- Sigue los patrones existentes en la base de código

## Guías para Solicitudes de Extracción

### Flujo de Trabajo de Contribución

1. **Haz un fork del repositorio** y crea una nueva rama desde `main`
2. **Realiza tus cambios** siguiendo las guías de estilo de código
3. **Prueba exhaustivamente** utilizando las instrucciones de prueba anteriores
4. **Confirma con mensajes claros** siguiendo el formato de commits convencionales
5. **Haz push a tu fork** y crea una solicitud de extracción
6. **Responde a los comentarios** de los mantenedores durante la revisión

### Convención de Nombres de Ramas

- `feature/<modulo>-<descripcion>` - Para nuevas características o contenido
- `fix/<modulo>-<descripcion>` - Para corrección de errores
- `docs/<descripcion>` - Para mejoras en la documentación
- `refactor/<descripcion>` - Para refactorización de código

### Formato de Mensajes de Commit

Sigue [Commits Convencionales](https://www.conventionalcommits.org/):

```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

**Ejemplos:**
```
feat(Module08): add intent-based routing notebook
docs(AGENTS): update Foundry Local setup instructions
fix(samples/08): resolve Electron build issue
```

### Formato de Títulos
```
[ModuleXX] Brief description of change
```
o
```
[Module08/samples/XX] Description for sample changes
```

### Código de Conducta

Todos los colaboradores deben seguir el [Código de Conducta de Código Abierto de Microsoft](https://opensource.microsoft.com/codeofconduct/). Por favor, revisa [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) antes de contribuir.

### Antes de Enviar

**Para cambios de contenido:**
- Previsualiza todos los archivos Markdown modificados
- Verifica que los enlaces y las imágenes funcionen
- Revisa errores tipográficos y gramaticales

**Para cambios en el código de muestra (Módulo08/muestras/08):**
```bash
npm run lint
npm test
```

**Para cambios en muestras de Python:**
- Prueba que la muestra se ejecute correctamente
- Verifica que el manejo de errores funcione
- Comprueba la compatibilidad con Foundry Local

### Proceso de Revisión

- Los cambios en el contenido educativo se revisan por precisión y claridad
- Las muestras de código se prueban para funcionalidad
- Las actualizaciones de traducción se manejan automáticamente por GitHub Actions

## Sistema de Traducción

**IMPORTANTE:** Este repositorio utiliza traducción automatizada a través de GitHub Actions.

- Las traducciones están en el directorio `/translations/` (más de 50 idiomas)
- Automatizado mediante el flujo de trabajo `co-op-translator.yml`
- **NO edites manualmente los archivos de traducción** - serán sobrescritos
- Edita solo los archivos fuente en inglés en los directorios raíz y de módulos
- Las traducciones se generan automáticamente al hacer push a la rama `main`

## Integración Local de Foundry

La mayoría de las muestras del Módulo08 requieren que Microsoft Foundry Local esté en ejecución.

### Instalación y Configuración

**Instalar Foundry Local:**
```bash
# Windows
winget install Microsoft.FoundryLocal

# macOS
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**Instalar SDK de Python:**
```bash
pip install foundry-local-sdk openai
```

### Iniciar Foundry Local
```bash
# Start service and run a model (auto-downloads if needed)
foundry model run phi-3.5-mini

# Or use model aliases for automatic hardware optimization
foundry model run phi-4-mini
foundry model run qwen2.5-0.5b
foundry model run qwen2.5-coder-0.5b

# Check service status
foundry service status

# List available models
foundry model ls
```

### Uso del SDK (Python)
```python
from foundry_local import FoundryLocalManager
import openai

# Use model alias for automatic hardware optimization
alias = "phi-4-mini"

# Create manager (auto-starts service and loads model)
manager = FoundryLocalManager(alias)

# Configure OpenAI client for local Foundry service
client = openai.OpenAI(
    base_url=manager.endpoint,
    api_key=manager.api_key
)

# Use the model
response = client.chat.completions.create(
    model=manager.get_model_info(alias).id,
    messages=[{"role": "user", "content": "Hello!"}]
)
```

### Verificación de Foundry Local
```bash
# Service status and endpoint
foundry service status

# List loaded models (REST API)
curl http://localhost:<port>/v1/models

# Note: Port is displayed when running 'foundry service status'
```

### Variables de Entorno para las Muestras

La mayoría de las muestras utilizan estas variables de entorno:
```bash
# Foundry Local configuration
# Note: The SDK (FoundryLocalManager) automatically detects endpoint
set MODEL=phi-4-mini  # or phi-3.5-mini, qwen2.5-0.5b, qwen2.5-coder-0.5b
set API_KEY=            # Not required for local usage

# Manual endpoint (if not using SDK)
# Port is shown via 'foundry service status'
set BASE_URL=http://localhost:<port>

# For Azure OpenAI fallback (optional)
set AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
set AZURE_OPENAI_API_KEY=your-api-key
set AZURE_OPENAI_API_VERSION=2024-08-01-preview
```

**Nota**: Al usar `FoundryLocalManager`, el SDK maneja automáticamente el descubrimiento de servicios y la carga de modelos. Los alias de modelos (como `phi-3.5-mini`) aseguran que se seleccione la mejor variante para tu hardware.

## Construcción y Despliegue

### Despliegue de Contenido

Este repositorio es principalmente documentación - no se requiere proceso de construcción para el contenido.

### Construcción de Aplicaciones de Muestra

**Aplicación Electron (Módulo08/muestras/08):**
```bash
cd Module08/samples/08

# Development build
npm run dev

# Production build
npm run build

# Create Windows installer
npm run dist

# Create portable executable
npm run pack
```

**Muestras de Python:**
No se requiere proceso de construcción - las muestras se ejecutan directamente con el intérprete de Python.

## Problemas Comunes y Solución de Problemas

> **Consejo**: Consulta [GitHub Issues](https://github.com/microsoft/edgeai-for-beginners/issues) para problemas conocidos y soluciones.

### Problemas Críticos (Bloqueantes)

#### Foundry Local No Está Ejecutándose
**Problema:** Las muestras fallan con errores de conexión

**Solución:**
```bash
# Check if service is running
foundry service status

# Start service with a model
foundry model run phi-4-mini

# Or explicitly start service
foundry service start

# List loaded models
foundry model ls

# Verify via REST API (port shown in 'foundry service status')
curl http://localhost:<port>/v1/models
```

### Problemas Comunes (Moderados)

#### Problemas con Entornos Virtuales de Python
**Problema:** Errores de importación de módulos

**Solución:**
```bash
# Ensure virtual environment is activated
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt
```

#### Problemas de Construcción de Electron
**Problema:** Fallos en npm install o en la construcción

**Solución:**
```bash
cd Module08/samples/08
# Clean install
npm run clean
rm -rf node_modules package-lock.json
npm install
```

### Problemas de Flujo de Trabajo (Menores)

#### Conflictos en el Flujo de Trabajo de Traducción
**Problema:** Conflictos en PR de traducción con tus cambios

**Solución:**
- Edita solo los archivos fuente en inglés
- Deja que el flujo de trabajo de traducción automatizado maneje las traducciones
- Si ocurren conflictos, fusiona `main` en tu rama después de que las traducciones sean fusionadas

#### Fallos en Descarga de Modelos
**Problema:** Foundry Local no puede descargar modelos

**Solución:**
```bash
# Check internet connectivity
# Clear model cache and retry
foundry model remove <model-alias>
foundry model run <model-alias>

# Check available disk space (models can be 2-16GB)
# Verify firewall settings allow downloads
```

## Recursos Adicionales

### Rutas de Aprendizaje
- **Ruta para Principiantes:** Módulos 01-02 (7-9 horas)
- **Ruta Intermedia:** Módulos 03-04 (9-11 horas)
- **Ruta Avanzada:** Módulos 05-07 (12-15 horas)
- **Ruta Experta:** Módulo 08 (8-10 horas)
- **Taller Práctico:** Materiales del taller (6-8 horas)

### Contenido Clave de los Módulos
- **Módulo01:** Fundamentos de EdgeAI y estudios de caso reales
- **Módulo02:** Familias y arquitecturas de Modelos de Lenguaje Pequeños (SLM)
- **Módulo03:** Estrategias de despliegue local y en la nube
- **Módulo04:** Optimización de modelos con múltiples marcos (Llama.cpp, Microsoft Olive, OpenVINO, Qualcomm QNN, Apple MLX)
- **Módulo05:** SLMOps - operaciones en producción
- **Módulo06:** Agentes de IA y llamadas a funciones
- **Módulo07:** Implementaciones específicas de plataformas
- **Módulo08:** Herramientas de Foundry Local con 10 muestras completas

### Dependencias Externas
- [Microsoft Foundry Local](https://github.com/microsoft/Foundry-Local) - Runtime local de modelos de IA con API compatible con OpenAI
  - [Documentación](https://github.com/microsoft/Foundry-Local/blob/main/docs/README.md)
  - [SDK de Python](https://github.com/microsoft/Foundry-Local/tree/main/sdk/python)
  - [SDK de JavaScript](https://github.com/microsoft/Foundry-Local/tree/main/sdk/javascript)
- [Llama.cpp](https://github.com/ggml-org/llama.cpp) - Marco de optimización
- [Microsoft Olive](https://microsoft.github.io/Olive/) - Herramienta de optimización de modelos
- [OpenVINO](https://docs.openvino.ai/) - Herramienta de optimización de Intel

## Notas Específicas del Proyecto

### Aplicaciones de Muestra del Módulo08

El repositorio incluye 10 aplicaciones de muestra completas:

1. **01-REST Chat Quickstart** - Integración básica del SDK de OpenAI
2. **02-OpenAI SDK Integration** - Funciones avanzadas del SDK
3. **03-Model Discovery & Benchmarking** - Herramientas de comparación de modelos
4. **04-Chainlit RAG Application** - Generación aumentada por recuperación
5. **05-Multi-Agent Orchestration** - Coordinación básica de agentes
6. **06-Models-as-Tools Router** - Enrutamiento inteligente de modelos
7. **07-Direct API Client** - Integración de API de bajo nivel
8. **08-Windows 11 Chat App** - Aplicación de escritorio nativa con Electron
9. **09-Advanced Multi-Agent System** - Orquestación compleja de agentes
10. **10-Marco de Herramientas Foundry** - Integración LangChain/Semantic Kernel

### Aplicaciones de Muestra del Taller

El taller incluye 6 sesiones progresivas con implementaciones prácticas:

1. **Sesión 01** - Inicio de chat con integración de Foundry Local
2. **Sesión 02** - Pipeline RAG y evaluación con RAGAS
3. **Sesión 03** - Evaluación comparativa de modelos de código abierto
4. **Sesión 04** - Comparación y selección de modelos
5. **Sesión 05** - Sistemas de orquestación multi-agente
6. **Sesión 06** - Enrutamiento de modelos y gestión de pipelines

Cada muestra demuestra diferentes aspectos del desarrollo de IA en el borde con Foundry Local.

### Consideraciones de Rendimiento

- Los SLMs están optimizados para despliegue en el borde (2-16GB RAM)
- La inferencia local proporciona tiempos de respuesta de 50-500ms
- Las técnicas de cuantización logran una reducción del tamaño del 75% con una retención del rendimiento del 85%
- Capacidades de conversación en tiempo real con modelos locales

### Seguridad y Privacidad

- Todo el procesamiento ocurre localmente - no se envían datos a la nube
- Adecuado para aplicaciones sensibles a la privacidad (salud, finanzas)
- Cumple con los requisitos de soberanía de datos
- Foundry Local funciona completamente en hardware local

## Obtener Ayuda

### Documentación

- **README Principal**: [README.md](README.md) - Resumen del repositorio y rutas de aprendizaje
- **Guía de Estudio**: [STUDY_GUIDE.md](STUDY_GUIDE.md) - Recursos de aprendizaje y cronograma
- **Soporte**: [SUPPORT.md](SUPPORT.md) - Cómo obtener ayuda
- **Seguridad**: [SECURITY.md](SECURITY.md) - Reportar problemas de seguridad

### Soporte Comunitario

- **Problemas en GitHub**: [Reportar errores o solicitar funciones](https://github.com/microsoft/edgeai-for-beginners/issues)
- **Discusiones en GitHub**: [Hacer preguntas y compartir ideas](https://github.com/microsoft/edgeai-for-beginners/discussions)
- **Problemas de Foundry Local**: [Problemas técnicos con Foundry Local](https://github.com/microsoft/Foundry-Local/issues)

### Contacto

- **Mantenedores**: Ver [CODEOWNERS](https://github.com/microsoft/edgeai-for-beginners/blob/main/.github/CODEOWNERS)
- **Problemas de Seguridad**: Seguir la divulgación responsable en [SECURITY.md](SECURITY.md)
- **Soporte de Microsoft**: Para soporte empresarial, contactar al servicio al cliente de Microsoft

### Recursos Adicionales

- **Microsoft Learn**: [Rutas de Aprendizaje de IA y Aprendizaje Automático](https://learn.microsoft.com/training/browse/?products=ai-services)
- **Documentación de Foundry Local**: [Documentación Oficial](https://github.com/microsoft/Foundry-Local/blob/main/docs/README.md)
- **Muestras de la Comunidad**: Consultar [Discusiones en GitHub](https://github.com/microsoft/edgeai-for-beginners/discussions) para contribuciones de la comunidad

---

**Este es un repositorio educativo enfocado en enseñar el desarrollo de IA en el borde. El patrón principal de contribución es mejorar el contenido educativo y agregar/mejorar aplicaciones de muestra que demuestren conceptos de IA en el borde.**

---

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que surjan del uso de esta traducción.
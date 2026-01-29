# Módulo 08: Práctica con Microsoft Foundry Local - Kit Completo para Desarrolladores

## Resumen

[Microsoft Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/) representa la próxima generación en desarrollo de IA en el borde, proporcionando herramientas poderosas para que los desarrolladores construyan, implementen y escalen aplicaciones de IA localmente, manteniendo una integración fluida con Azure AI Foundry. Este módulo ofrece una cobertura completa de Foundry Local, desde la instalación hasta el desarrollo avanzado de agentes.

**Tecnologías Clave:**
- CLI y SDK de Microsoft Foundry Local
- Integración con Azure AI Foundry
- Inferencia de modelos en el dispositivo
- Caché y optimización de modelos locales
- Arquitecturas basadas en agentes

## Objetivos de Aprendizaje

Al completar este módulo, podrás:

- **Dominar Foundry Local**: Instalar, configurar y optimizar para desarrollo en Windows 11
- **Implementar Modelos Diversos**: Ejecutar modelos phi, qwen, deepseek y GPT localmente con comandos CLI
- **Crear Soluciones de Producción**: Desarrollar aplicaciones de IA con ingeniería avanzada de prompts e integración de datos
- **Aprovechar el Ecosistema Open-Source**: Integrar modelos de Hugging Face y contribuciones de la comunidad
- **Desarrollar Agentes de IA**: Construir agentes inteligentes con capacidades de grounding y orquestación
- **Implementar Patrones Empresariales**: Crear soluciones de IA modulares y escalables para despliegues en producción

## Estructura de la Sesión

### [1: Introducción a Foundry Local](./01.FoundryLocalSetup.md)
**Enfoque**: Instalación, configuración de CLI, implementación de modelos y optimización de hardware

**Temas Clave**: Instalación completa • Comandos CLI • Caché de modelos • Aceleración de hardware • Implementación de múltiples modelos

**Ejemplo**: [Inicio Rápido REST Chat](./samples/01/README.md) • [Integración con OpenAI SDK](./samples/02/README.md) • [Descubrimiento y Benchmarking de Modelos](./samples/03/README.md)

**Duración**: 2-3 horas | **Nivel**: Principiante

---

### [2: Construir Soluciones de IA con Azure AI Foundry](./02.AzureAIFoundryIntegration.md)
**Enfoque**: Ingeniería avanzada de prompts, integración de datos y conectividad en la nube

**Temas Clave**: Ingeniería de prompts • Integración de datos • Flujos de trabajo en Azure • Optimización de rendimiento • Monitoreo

**Ejemplo**: [Aplicación RAG con Chainlit](./samples/04/README.md)

**Duración**: 2-3 horas | **Nivel**: Intermedio

---

### [3: Modelos Open-Source en Foundry Local](./03.OpenSourceModels.md)
**Enfoque**: Integración con Hugging Face, estrategias BYOM y modelos de la comunidad

**Temas Clave**: Integración con Hugging Face • Bring-your-own-model • Insights de Model Mondays • Contribuciones de la comunidad • Selección de modelos

**Ejemplo**: [Orquestación Multi-Agente](./samples/05/README.md)

**Duración**: 2-3 horas | **Nivel**: Intermedio

---

### [4: Explorar Modelos de Vanguardia](./04.CuttingEdgeModels.md)
**Enfoque**: Comparación entre LLMs y SLMs, implementación de EdgeAI y demos avanzados

**Temas Clave**: Comparación de modelos • Inferencia en el borde vs en la nube • Phi + ONNX Runtime • Aplicación RAG con Chainlit • Optimización WebGPU

**Ejemplo**: [Router de Modelos como Herramientas](./samples/06/README.md)

**Duración**: 3-4 horas | **Nivel**: Avanzado

---

### [5: Construir Agentes de IA Rápidamente](./05.AIPoweredAgents.md)
**Enfoque**: Arquitecturas de agentes, prompts del sistema, grounding y orquestación

**Temas Clave**: Patrones de diseño de agentes • Ingeniería de prompts del sistema • Técnicas de grounding • Sistemas multi-agente • Despliegue en producción

**Ejemplo**: [Orquestación Multi-Agente](./samples/05/README.md) • [Sistema Multi-Agente Avanzado](./samples/09/README.md)

**Duración**: 3-4 horas | **Nivel**: Avanzado

---

### [6: Foundry Local - Modelos como Herramientas](./06.ModelsAsTools.md)
**Enfoque**: Soluciones de IA modulares, escalabilidad empresarial y patrones de producción

**Temas Clave**: Modelos como herramientas • Despliegue en el dispositivo • Integración SDK/API • Arquitecturas empresariales • Estrategias de escalabilidad

**Ejemplo**: [Router de Modelos como Herramientas](./samples/06/README.md) • [Framework de Herramientas Foundry](./samples/10/README.md)

**Duración**: 3-4 horas | **Nivel**: Experto

---

### [7: Patrones de Integración Directa con API](./samples/07/README.md)
**Enfoque**: Integración pura con REST API sin dependencias de SDK para máximo control

**Temas Clave**: Implementación de cliente HTTP • Autenticación personalizada • Monitoreo de salud de modelos • Respuestas en streaming • Manejo de errores en producción

**Ejemplo**: [Cliente API Directo](./samples/07/README.md)

**Duración**: 2-3 horas | **Nivel**: Intermedio

---

### [8: Aplicación Nativa de Chat en Windows 11](./samples/08/README.md)
**Enfoque**: Construcción de aplicaciones modernas de chat nativas con integración de Foundry Local

**Temas Clave**: Desarrollo con Electron • Fluent Design System • Integración nativa en Windows • Streaming en tiempo real • Diseño de interfaz de chat

**Ejemplo**: [Aplicación de Chat en Windows 11](./samples/08/README.md)

**Duración**: 3-4 horas | **Nivel**: Avanzado

---

### [9: Orquestación Multi-Agente Avanzada](./samples/09/README.md)
**Enfoque**: Coordinación sofisticada de agentes, delegación de tareas especializadas y flujos de trabajo colaborativos de IA

**Temas Clave**: Coordinación inteligente de agentes • Patrones de llamadas a funciones • Comunicación entre agentes • Orquestación de flujos de trabajo • Mecanismos de aseguramiento de calidad

**Ejemplo**: [Sistema Multi-Agente Avanzado](./samples/09/README.md)

**Duración**: 4-5 horas | **Nivel**: Experto

---

### [10: Foundry Local como Framework de Herramientas](./samples/10/README.md)
**Enfoque**: Arquitectura centrada en herramientas para integrar Foundry Local en aplicaciones y frameworks existentes

**Temas Clave**: Integración con LangChain • Funciones de Semantic Kernel • Frameworks REST API • Herramientas CLI • Integración con Jupyter • Patrones de despliegue en producción

**Ejemplo**: [Framework de Herramientas Foundry](./samples/10/README.md)

**Duración**: 4-5 horas | **Nivel**: Experto

## Requisitos Previos

### Requisitos del Sistema
- **Sistema Operativo**: Windows 11 (22H2 o posterior)
- **Memoria**: 16GB RAM (32GB recomendados para modelos más grandes)
- **Almacenamiento**: 50GB de espacio libre para caché de modelos
- **Hardware**: Dispositivo con NPU recomendado (Copilot+ PC), GPU opcional
- **Red**: Internet de alta velocidad para descargas iniciales de modelos

### Entorno de Desarrollo
- Visual Studio Code con extensión AI Toolkit
- Python 3.10+ y pip
- Git para control de versiones
- PowerShell o Command Prompt
- Azure CLI (opcional para integración en la nube)

### Conocimientos Previos
- Comprensión básica de conceptos de IA/ML
- Familiaridad con la línea de comandos
- Fundamentos de programación en Python
- Conceptos de REST API
- Conocimientos básicos de prompts e inferencia de modelos

## Cronograma del Módulo

**Tiempo Total Estimado**: 30-38 horas

| Sesión | Área de Enfoque | Ejemplos | Tiempo | Complejidad |
|--------|-----------------|----------|--------|-------------|
|  1 | Configuración y Básicos | 01, 02, 03 | 2-3 horas | Principiante |
|  2 | Soluciones de IA | 04 | 2-3 horas | Intermedio |
|  3 | Open Source | 05 | 2-3 horas | Intermedio |
|  4 | Modelos Avanzados | 06 | 3-4 horas | Avanzado |
|  5 | Agentes de IA | 05, 09 | 3-4 horas | Avanzado |
|  6 | Herramientas Empresariales | 06, 10 | 3-4 horas | Experto |
|  7 | Integración Directa con API | 07 | 2-3 horas | Intermedio |
|  8 | Aplicación de Chat en Windows 11 | 08 | 3-4 horas | Avanzado |
|  9 | Orquestación Multi-Agente Avanzada | 09 | 4-5 horas | Experto |
| 10 | Framework de Herramientas | 10 | 4-5 horas | Experto |

## Recursos Clave

**Documentación Oficial:**
- [Microsoft Foundry Local GitHub](https://github.com/microsoft/Foundry-Local) - Código fuente y ejemplos oficiales
- [Documentación de Azure AI Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/) - Guía completa de configuración y uso
- [Serie Model Mondays](https://aka.ms/model-mondays) - Destacados y tutoriales semanales de modelos

**Comunidad y Soporte:**
- [Discusiones de Foundry Local](https://github.com/microsoft/Foundry-Local/discussions) - Preguntas y respuestas de la comunidad y solicitudes de características
- [Comunidad de Desarrolladores de IA de Microsoft](https://techcommunity.microsoft.com/category/artificialintelligence) - Noticias y mejores prácticas

## Resultados de Aprendizaje

Al completar este módulo, estarás preparado para:

### Dominio Técnico
- **Implementar y Gestionar**: Instalaciones de Foundry Local en entornos de desarrollo y producción
- **Integrar Modelos**: Trabajar sin problemas con diversas familias de modelos de Microsoft, Hugging Face y fuentes comunitarias
- **Crear Aplicaciones**: Desarrollar aplicaciones de IA listas para producción con características avanzadas y optimizaciones
- **Desarrollar Agentes**: Implementar agentes de IA sofisticados con grounding, razonamiento e integración de herramientas

### Comprensión Estratégica
- **Decisiones de Arquitectura**: Tomar decisiones informadas entre despliegue local y en la nube
- **Optimización de Rendimiento**: Optimizar el rendimiento de inferencia en diferentes configuraciones de hardware
- **Escalabilidad Empresarial**: Diseñar aplicaciones que escalen desde prototipos locales hasta despliegues empresariales
- **Privacidad y Seguridad**: Implementar soluciones de IA que preserven la privacidad con inferencia local

### Capacidades de Innovación
- **Prototipado Rápido**: Construir y probar conceptos de aplicaciones de IA rápidamente en los 10 patrones de ejemplo
- **Integración Comunitaria**: Aprovechar modelos open-source y contribuir al ecosistema
- **Patrones Avanzados**: Implementar patrones de IA de vanguardia, incluyendo RAG, agentes e integración de herramientas
- **Dominio de Frameworks**: Integración experta con LangChain, Semantic Kernel, Chainlit y Electron
- **Despliegue en Producción**: Implementar soluciones de IA escalables desde prototipos locales hasta sistemas empresariales
- **Desarrollo Preparado para el Futuro**: Construir aplicaciones listas para tecnologías y patrones emergentes de IA

## Cómo Empezar

1. **Configuración del Entorno**: Asegúrate de tener Windows 11 con el hardware recomendado (ver Requisitos Previos)
2. **Instalar Foundry Local**: Sigue la Sesión 1 para instalación y configuración completas
3. **Ejecutar Ejemplo 01**: Comienza con la integración básica de REST API para verificar la configuración
4. **Avanzar a través de los Ejemplos**: Completa los ejemplos 01-10 para un dominio completo

## Métricas de Éxito

Sigue tu progreso a través de los 10 ejemplos completos:

### Nivel Básico (Ejemplos 01-03)
- [ ] Instalar y configurar Foundry Local exitosamente
- [ ] Completar la integración con REST API (Ejemplo 01)
- [ ] Implementar compatibilidad con OpenAI SDK (Ejemplo 02)
- [ ] Realizar descubrimiento y benchmarking de modelos (Ejemplo 03)

### Nivel de Aplicación (Ejemplos 04-06)
- [ ] Implementar y ejecutar al menos 4 familias de modelos diferentes
- [ ] Construir una aplicación funcional de chat RAG (Ejemplo 04)
- [ ] Crear un sistema de orquestación multi-agente (Ejemplo 05)
- [ ] Implementar enrutamiento inteligente de modelos (Ejemplo 06)

### Nivel de Integración Avanzada (Ejemplos 07-10)
- [ ] Construir un cliente API listo para producción (Ejemplo 07)
- [ ] Desarrollar una aplicación nativa de chat en Windows 11 (Ejemplo 08)
- [ ] Implementar un sistema multi-agente avanzado (Ejemplo 09)
- [ ] Crear un framework completo de herramientas (Ejemplo 10)

### Indicadores de Dominio
- [ ] Ejecutar exitosamente los 10 ejemplos sin errores
- [ ] Personalizar al menos 3 ejemplos para casos de uso específicos
- [ ] Desplegar 2+ ejemplos en entornos similares a producción
- [ ] Contribuir mejoras o extensiones al código de ejemplo
- [ ] Integrar patrones de Foundry Local en proyectos personales/profesionales

## Guía Rápida - Los 10 Ejemplos

### Configuración del Entorno (Requerido para Todos los Ejemplos)

```powershell
# 1. Clone and navigate to Module08
cd Module08

# 2. Create Python virtual environment
py -m venv .venv
.\.venv\Scripts\activate

# 3. Install base dependencies
pip install -r requirements.txt

# 4. Install Foundry Local (if not already installed)
winget install Microsoft.FoundryLocal

# 5. Verify Foundry Local installation
foundry --version
foundry model list
```

### Ejemplos Básicos Fundamentales (01-06)

**Ejemplo 01: Inicio Rápido REST Chat**
```powershell
# Start Foundry Local service
foundry model run phi-4-mini

# Run REST chat demo
python samples/01/chat_quickstart.py
```

**Ejemplo 02: Integración con OpenAI SDK**
```powershell
# Ensure model is running
foundry status

# Run SDK demo
python samples/02/sdk_quickstart.py
```

**Ejemplo 03: Descubrimiento y Benchmarking de Modelos**
```powershell
# Run comprehensive model testing
samples/03/list_and_bench.cmd

# Or run individual components
foundry model list --available
foundry model download qwen2.5-0.5b
foundry model benchmark phi-4-mini
```

**Ejemplo 04: Aplicación RAG con Chainlit**
```powershell
# Install Chainlit dependencies
pip install chainlit langchain chromadb

# Start RAG chat application
chainlit run samples/04/app.py -w
# Opens browser at http://localhost:8000
```

**Ejemplo 05: Orquestación Multi-Agente**
```powershell
# Run agent coordinator demo
python -m samples.05.agents.coordinator

# Run specific agent examples
python samples/05/examples/specialists_demo.py
```

**Ejemplo 06: Router de Modelos como Herramientas**
```powershell
# Configure environment
set BASE_URL=http://localhost:8000
set GENERAL_MODEL=phi-4-mini
set CODE_MODEL=qwen2.5-7b

# Run intelligent router
python samples/06/router.py "Analyze this Python code for performance issues"
```

### Ejemplos de Integración Avanzada (07-10)

**Ejemplo 07: Cliente API Directo**
```powershell
# Navigate to sample directory
cd samples/07

# Install additional dependencies
pip install -r requirements.txt

# Run basic API examples
python examples/basic_usage.py

# Try streaming responses
python examples/streaming.py

# Test production patterns
python examples/production.py
```

**Ejemplo 08: Aplicación de Chat en Windows 11**
```powershell
# Navigate to sample directory
cd samples/08

# Install Node.js dependencies
npm install

# Start Electron application
npm start

# Or build for production
npm run build
```

**Ejemplo 09: Sistema Multi-Agente Avanzado**
```powershell
# Navigate to sample directory
cd samples/09

# Install agent system dependencies
pip install -r requirements.txt

# Run basic coordination example
python examples/basic_coordination.py

# Try complex workflow
python examples/complex_workflow.py

# Interactive agent demo
python examples/interactive_demo.py
```

**Ejemplo 10: Framework de Herramientas Foundry**
```powershell
# Navigate to sample directory
cd samples/10

# Install framework dependencies
pip install -r requirements.txt

# Run basic tools demo
python examples/basic_tools.py

# Start REST API server
python examples/rest_api_server.py
# API available at http://localhost:8080

# Try CLI application
python examples/cli_application.py --help

# Launch Jupyter notebook
jupyter notebook examples/jupyter_notebook.ipynb

# Test LangChain integration
python examples/langchain_demo.py
```

### Solución de Problemas Comunes

**Errores de Conexión en Foundry Local**
```powershell
# Check service status
foundry status

# Restart if needed
foundry restart

# Verify endpoint accessibility
curl http://localhost:5273/v1/models
```

**Problemas de Carga de Modelos**
```powershell
# Check available models
foundry model list --cached

# Download missing models
foundry model download phi-4-mini
foundry model download qwen2.5-0.5b

# Force reload if needed
foundry model unload --all
foundry model run phi-4-mini
```

**Problemas de Dependencias**
```powershell
# Upgrade pip and reinstall
python -m pip install --upgrade pip
pip install -r requirements.txt --force-reinstall

# For Node.js samples
npm cache clean --force
npm install
```

## Resumen
Este módulo representa la vanguardia del desarrollo de IA en el borde, combinando las herramientas empresariales de Microsoft con la flexibilidad e innovación del ecosistema de código abierto. Al dominar Foundry Local a través de los 10 ejemplos completos, estarás en la primera línea del desarrollo de aplicaciones de IA.

**Ruta de aprendizaje completa:**
- **Fundamentos** (Ejemplos 01-03): Integración de API y gestión de modelos
- **Aplicaciones** (Ejemplos 04-06): RAG, agentes y enrutamiento inteligente
- **Avanzado** (Ejemplos 07-10): Marcos de producción e integración empresarial

Para la integración con Azure OpenAI (Sesión 2), consulta los archivos README individuales de cada ejemplo para las variables de entorno requeridas y configuraciones de versión de API.

---

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por garantizar la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse como la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que puedan surgir del uso de esta traducción.
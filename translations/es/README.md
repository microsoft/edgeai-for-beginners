# EdgeAI para Principiantes 


![Imagen de portada del curso](../../translated_images/es/cover.eb18d1b9605d754b.webp)

[![Contribuidores de GitHub](https://img.shields.io/github/contributors/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/graphs/contributors)
[![Issues de GitHub](https://img.shields.io/github/issues/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/issues)
[![Pull-requests de GitHub](https://img.shields.io/github/issues-pr/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/pulls)
[![PRs Bienvenidos](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

[![Observadores de GitHub](https://img.shields.io/github/watchers/microsoft/edgeai-for-beginners.svg?style=social&label=Watch)](https://GitHub.com/microsoft/edgeai-for-beginners/watchers)
[![Bifurcaciones de GitHub](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork)
[![Estrellas de GitHub](https://img.shields.io/github/stars/microsoft/edgeai-for-beginners?style=social&label=Star)](https://GitHub.com/microsoft/edgeai-for-beginners/stargazers)


[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Sigue estos pasos para comenzar a usar estos recursos:

1. **Haz fork del repositorio**: Haz clic en [![Bifurcaciones de GitHub](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork)
2. **Clona el repositorio**:   `git clone https://github.com/microsoft/edgeai-for-beginners.git`
3. [**Únete al Discord de Azure AI Foundry y conoce expertos y desarrolladores**](https://discord.com/invite/ByRwuEEgH4)


### 🌐 Soporte Multilingüe

#### Soportado vía GitHub Action (Automatizado y Siempre Actualizado)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Árabe](../ar/README.md) | [Bengalí](../bn/README.md) | [Búlgaro](../bg/README.md) | [Birmano (Myanmar)](../my/README.md) | [Chino (Simplificado)](../zh-CN/README.md) | [Chino (Tradicional, Hong Kong)](../zh-HK/README.md) | [Chino (Tradicional, Macao)](../zh-MO/README.md) | [Chino (Tradicional, Taiwán)](../zh-TW/README.md) | [Croata](../hr/README.md) | [Checo](../cs/README.md) | [Danés](../da/README.md) | [Holandés](../nl/README.md) | [Estonio](../et/README.md) | [Finlandés](../fi/README.md) | [Francés](../fr/README.md) | [Alemán](../de/README.md) | [Griego](../el/README.md) | [Hebreo](../he/README.md) | [Hindi](../hi/README.md) | [Húngaro](../hu/README.md) | [Indonesio](../id/README.md) | [Italiano](../it/README.md) | [Japonés](../ja/README.md) | [Kannada](../kn/README.md) | [Jemer](../km/README.md) | [Coreano](../ko/README.md) | [Lituano](../lt/README.md) | [Malayo](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepalí](../ne/README.md) | [Pidgin Nigeriano](../pcm/README.md) | [Noruego](../no/README.md) | [Persa (Farsi)](../fa/README.md) | [Polaco](../pl/README.md) | [Portugués (Brasil)](../pt-BR/README.md) | [Portugués (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Rumano](../ro/README.md) | [Ruso](../ru/README.md) | [Serbio (Cirílico)](../sr/README.md) | [Eslovaco](../sk/README.md) | [Esloveno](../sl/README.md) | [Español](./README.md) | [Swahili](../sw/README.md) | [Sueco](../sv/README.md) | [Tagalo (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Tailandés](../th/README.md) | [Turco](../tr/README.md) | [Ucraniano](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamita](../vi/README.md)

> **¿Prefieres clonar localmente?**
>
> Este repositorio incluye traducciones en más de 50 idiomas, lo que aumenta significativamente el tamaño de la descarga. Para clonar sin traducciones, usa sparse checkout:
>
> **Bash / macOS / Linux:**
> ```bash
> git clone --filter=blob:none --sparse https://github.com/microsoft/edgeai-for-beginners.git
> cd edgeai-for-beginners
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
>
> **CMD (Windows):**
> ```cmd
> git clone --filter=blob:none --sparse https://github.com/microsoft/edgeai-for-beginners.git
> cd edgeai-for-beginners
> git sparse-checkout set --no-cone "/*" "!translations" "!translated_images"
> ```
>
> Esto te brinda todo lo necesario para completar el curso con una descarga mucho más rápida.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

**Si deseas que se añadan más idiomas de traducción, están listados [aquí](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md)**
## Introducción

Bienvenido a **EdgeAI para Principiantes** – tu viaje completo al mundo transformador de la Inteligencia Artificial en el Edge. Este curso cierra la brecha entre las poderosas capacidades de IA y su implementación práctica y real en dispositivos edge, habilitándote para aprovechar el potencial de la IA directamente donde se generan los datos y se deben tomar decisiones.

### Lo que dominarás

Este curso te lleva desde los conceptos fundamentales hasta implementaciones listas para producción, cubriendo:
- **Modelos de Lenguaje Pequeños (SLMs)** optimizados para despliegue en edge
- **Optimización consciente del hardware** en plataformas diversas
- **Inferencia en tiempo real** con capacidades de preservación de privacidad
- **Estrategias de despliegue en producción** para aplicaciones empresariales

### Por qué EdgeAI importa

Edge AI representa un cambio de paradigma que aborda desafíos modernos críticos:
- **Privacidad y Seguridad**: Procesa datos sensibles localmente sin exponerlos a la nube
- **Rendimiento en Tiempo Real**: Elimina la latencia de red para aplicaciones críticas en tiempo
- **Eficiencia de Costos**: Reduce gastos de ancho de banda y computación en la nube
- **Operaciones Resilientes**: Mantiene la funcionalidad durante caídas de red
- **Cumplimiento Regulatorio**: Cumple con requisitos de soberanía de datos

### Edge AI

Edge AI se refiere a ejecutar algoritmos de IA y modelos de lenguaje localmente en hardware, cerca de donde se generan los datos, sin depender de recursos en la nube para la inferencia. Reduce la latencia, mejora la privacidad y permite la toma de decisiones en tiempo real.

### Principios Básicos:
- **Inferencia en el dispositivo**: Modelos de IA que corren en dispositivos edge (teléfonos, routers, microcontroladores, PCs industriales)
- **Capacidad offline**: Funciona sin conexión persistente a internet
- **Baja latencia**: Respuestas inmediatas adecuadas para sistemas en tiempo real
- **Soberanía de datos**: Los datos sensibles permanecen localmente, mejorando seguridad y cumplimiento

### Modelos de Lenguaje Pequeños (SLMs)

Los SLMs como Phi-4, Mistral-7B y Gemma son versiones optimizadas de modelos grandes (LLMs), entrenados o destilados para:
- **Reducción del uso de memoria**: Uso eficiente de la memoria limitada de dispositivos edge
- **Menor demanda de cómputo**: Optimizado para desempeño en CPU y GPU de edge
- **Tiempos de arranque rápidos**: Inicialización rápida para aplicaciones responsivas

Desbloquean capacidades poderosas de PLN mientras cumplen con las restricciones de:
- **Sistemas embebidos**: Dispositivos IoT y controladores industriales
- **Dispositivos móviles**: Smartphones y tablets con capacidad offline
- **Dispositivos IoT**: Sensores y dispositivos inteligentes con recursos limitados
- **Servidores Edge**: Unidades de procesamiento local con recursos GPU limitados
- **Computadoras personales**: Escenarios de despliegue en escritorio y laptop

## Módulos del Curso y Navegación

| Módulo | Tema | Área de Enfoque | Contenido Clave | Nivel | Duración |
|--------|-------|------------|-------------|--------|----------|
| [📖 00 ](./introduction.md) | [Introducción a EdgeAI](./introduction.md) | Fundamentos y Contexto | Visión General de EdgeAI • Aplicaciones en la Industria • Introducción a SLM • Objetivos de Aprendizaje | Principiante | 1-2 hrs |
| [📚 01](../../Module01) | [Fundamentos de EdgeAI](./Module01/README.md) | Comparación Cloud vs Edge AI | Fundamentos de EdgeAI • Casos de Estudio Reales • Guía de Implementación • Despliegue en Edge | Principiante | 3-4 hrs |
| [🧠 02](../../Module02) | [Fundamentos de Modelos SLM](./Module02/README.md) | Familias y arquitectura de modelos | Familia Phi • Familia Qwen • Familia Gemma • BitNET • μModel • Phi-Silica | Principiante | 4-5 hrs |
| [🚀 03](../../Module03) | [Práctica de Despliegue SLM](./Module03/README.md) | Despliegue local y en la nube | Aprendizaje Avanzado • Entorno Local • Despliegue en la Nube | Intermedio | 4-5 hrs |
| [⚙️ 04](../../Module04) | [Kit de Optimización de Modelos](./Module04/README.md) | Optimización multiplataforma | Introducción • Llama.cpp • Microsoft Olive • OpenVINO • Apple MLX • Síntesis de Flujo de Trabajo | Intermedio | 5-6 hrs |
| [🔧 05](../../Module05) | [Producción SLMOps](./Module05/README.md) | Operaciones en producción | Introducción a SLMOps • Destilación de Modelos • Afinamiento • Despliegue en Producción | Avanzado | 5-6 hrs |
| [🤖 06](../../Module06) | [Agentes de IA y Llamado a Funciones](./Module06/README.md) | Marcos de agentes y MCP | Introducción a Agentes • Llamado a Funciones • Protocolo de Contexto de Modelos | Avanzado | 4-5 hrs |
| [💻 07](../../Module07) | [Implementación en Plataforma](./Module07/README.md) | Ejemplos multiplataforma | Kit de herramientas de IA • Foundry Local • Desarrollo en Windows | Avanzado | 3-4 hrs |
| [🏭 08](../../Module08) | [Kit de Herramientas Foundry Local](./Module08/README.md) | Ejemplos listos para producción | Aplicaciones de ejemplo (ver detalles abajo) | Experto | 8-10 hrs |

### 🏭 **Módulo 08: Aplicaciones de Ejemplo**

- [01: Inicio rápido REST Chat](./Module08/samples/01/README.md)
- [02: Integración SDK OpenAI](./Module08/samples/02/README.md)
- [03: Descubrimiento de Modelos y Benchmarking](./Module08/samples/03/README.md)
- [04: Aplicación Chainlit RAG](./Module08/samples/04/README.md)
- [05: Orquestación Multi-Agente](./Module08/samples/05/README.md)
- [06: Enrutador Models-as-Tools](./Module08/samples/06/README.md)
- [07: Cliente API Directo](./Module08/samples/07/README.md)
- [08: Aplicación Chat Windows 11](./Module08/samples/08/README.md)
- [09: Sistema Multi-Agente Avanzado](./Module08/samples/09/README.md)
- [10: Framework Foundry Tools](./Module08/samples/10/README.md)

### 🎓 **Taller: Ruta de Aprendizaje Práctica**

Materiales comprensivos para taller práctico con implementaciones listas para producción:

- **[Guía del Taller](./Workshop/Readme.md)** - Objetivos de aprendizaje completos, resultados y navegación de recursos
- **Ejemplos en Python** (6 sesiones) - Actualizados con mejores prácticas, manejo de errores y documentación completa
- **Cuadernos Jupyter** (8 interactivos) - Tutoriales paso a paso con benchmarks y monitoreo de rendimiento
- **Guías de Sesión** - Guías en markdown detalladas para cada sesión del taller
- **Herramientas de Validación** - Scripts para verificar calidad de código y ejecutar pruebas rápidas

**Lo que construirás:**
- Aplicaciones de chat AI locales con soporte de streaming
- Pipelines RAG con evaluación de calidad (RAGAS)
- Herramientas de benchmarking y comparación de múltiples modelos
- Sistemas de orquestación multi-agente
- Enrutamiento inteligente de modelos con selección basada en tareas

### 🎙️ **Taller Para Agentic: Hands-On - El Estudio de Podcast de IA**
¡Construye un pipeline de producción de podcasts impulsado por IA desde cero! Este taller inmersivo te enseña a crear un sistema multi-agente completo que transforma ideas en episodios de podcast profesionales.

**[🎬 Comienza el Taller AI Podcast Studio](./WorkshopForAgentic/README.md)**

**Tu Misión**: Lanza "Future Bytes": un podcast tecnológico impulsado completamente por agentes de IA que construirás tú mismo. Sin dependencias en la nube, sin costos de API: todo se ejecuta localmente en tu máquina.

**Qué Lo Hace Único:**
- **🤖 Orquestación Real Multi-Agente** - Construye agentes de IA especializados que investigan, escriben y producen audio
- **🎯 Pipeline Completo de Producción** - Desde la selección de temas hasta la salida final del audio del podcast
- **💻 Despliegue 100% Local** - Utiliza Ollama y modelos locales (Qwen-3-8B) para privacidad y control total
- **🎤 Integración de Texto a Voz** - Transforma guiones en conversaciones con múltiples voces naturales
- **✋ Flujos de Trabajo con Intervención Humana** - Puertas de aprobación que aseguran calidad manteniendo la automatización

**Aprendizaje en Tres Actos:**

| Acto | Enfoque | Habilidades Clave | Duración |
|-----|-------|------------|----------|
| **[Acto 1: Conoce Tus Asistentes de IA](./WorkshopForAgentic/md/01.BuildAIAgentWithSLM.md)** | Construye tu primer agente de IA | Integración de herramientas • Búsqueda web • Resolución de problemas • Razonamiento agente | 2-3 hrs |
| **[Acto 2: Ensambla Tu Equipo de Producción](./WorkshopForAgentic/md/02.AIAgentOrchestrationAndWorkflows.md)** | Orquesta múltiples agentes | Coordinación de equipos • Flujos de aprobación • Interfaz DevUI • Supervisión humana | 3-4 hrs |
| **[Acto 3: Da Vida a Tu Podcast](./WorkshopForAgentic/md/03.Multi-SpeakerPodcastGenerationWithVibeVoice.md)** | Genera audio para podcast | Texto a voz • Síntesis multi-voceros • Audio de larga duración • Automatización completa | 2-3 hrs |

**Tecnologías Utilizadas:**
- **Microsoft Agent Framework** - Orquestación y coordinación multi-agente
- **Ollama** - Ejecución local de modelos de IA (sin necesidad de nube)
- **Qwen-3-8B** - Modelo de lenguaje open source optimizado para tareas agenticas
- **APIs de Texto a Voz** - Síntesis natural de voz para generación de podcasts

**Soporte de Hardware:**
- ✅ **Modo CPU** - Funciona en cualquier computadora moderna (se recomienda 8GB+ RAM)
- 🚀 **Aceleración GPU** - Inferencia mucho más rápida con GPUs NVIDIA/AMD
- ⚡ **Soporte NPU** - Aceleración con unidad de procesamiento neuronal de próxima generación

**Perfecto Para:**
- Desarrolladores aprendiendo sistemas de IA multi-agentes
- Cualquier persona interesada en automatización de IA y flujos de trabajo
- Creadores de contenido explorando producción asistida por IA
- Estudiantes que estudian patrones prácticos de orquestación de IA

**Comienza a Construir**: [🎙️ El Taller AI Podcast Studio →](./WorkshopForAgentic/README.md)

### 📊 **Resumen del Camino de Aprendizaje**
- **Duración Total**: 36-45 horas
- **Camino para Principiantes**: Módulos 01-02 (7-9 horas)  
- **Camino Intermedio**: Módulos 03-04 (9-11 horas)
- **Camino Avanzado**: Módulos 05-07 (12-15 horas)
- **Camino Experto**: Módulo 08 (8-10 horas)

## Qué Construirás

### 🎯 Competencias Clave
- **Arquitectura AI en el Borde**: Diseña sistemas de IA local-primero con integración en la nube
- **Optimización de Modelos**: Cuantiza y comprime modelos para despliegue en el borde (85% más rápido, 75% menos tamaño)
- **Despliegue Multiplataforma**: Windows, móvil, embebido y sistemas híbridos nube-borde
- **Operaciones de Producción**: Monitoreo, escalado y mantenimiento de IA en producción en el borde

### 🏗️ Proyectos Prácticos
- **Aplicaciones Locales Foundry Chat**: Aplicación nativa Windows 11 con cambio de modelos
- **Sistemas Multi-Agente**: Coordinador con agentes especialistas para flujos complejos  
- **Aplicaciones RAG**: Procesamiento local de documentos con búsqueda vectorial
- **Enrutadores de Modelos**: Selección inteligente entre modelos según análisis de tareas
- **Frameworks de API**: Clientes listos para producción con streaming y monitoreo de salud
- **Herramientas Multiplataforma**: Patrones de integración LangChain/Semantic Kernel

### 🏢 Aplicaciones Industriales
**Manufactura** • **Cuidado de la Salud** • **Vehículos Autónomos** • **Ciudades Inteligentes** • **Apps Móviles**

## Inicio Rápido

**Camino de Aprendizaje Recomendado** (20-30 horas total):

0. **📖 Introducción** ([Introduction.md](./introduction.md)): Fundamentos de EdgeAI + contexto industrial + marco de aprendizaje
1. **📚 Fundamentos** (Módulos 01-02): Conceptos EdgeAI + familias de modelos SLM
2. **⚙️ Optimización** (Módulos 03-04): Despliegue + frameworks de cuantización  
3. **🚀 Producción** (Módulos 05-06): SLMOps + agentes de IA + llamadas a funciones
4. **💻 Implementación** (Módulos 07-08): Ejemplos de plataforma + toolkit Foundry Local

Cada módulo incluye teoría, ejercicios prácticos y ejemplos de código listos para producción.

## Impacto en la Carrera

**Roles Técnicos**: Arquitecto de Soluciones EdgeAI • Ingeniero ML (Edge) • Desarrollador IoT AI • Desarrollador AI Móvil

**Sectores Industriales**: Manufactura 4.0 • Tecnología en Salud • Sistemas Autónomos • FinTech • Electrónica de Consumo

**Proyectos para Portafolio**: Sistemas multi-agentes • Aplicaciones RAG de producción • Despliegue multiplataforma • Optimización de rendimiento

## Estructura del Repositorio

```
edgeai-for-beginners/
├── 📖 introduction.md  # Foundation: EdgeAI Overview & Learning Framework
├── 📚 Module01-04/     # Fundamentals → SLMs → Deployment → Optimization  
├── 🔧 Module05-06/     # SLMOps → AI Agents → Function Calling
├── 💻 Module07/        # Platform Samples (VS Code, Windows, Jetson, Mobile)
├── 🏭 Module08/        # Foundry Local Toolkit + 10 Comprehensive Samples
│   ├── samples/01-06/  # Foundation: REST, SDK, RAG, Agents, Routing
│   └── samples/07-10/  # Advanced: API Client, Windows App, Enterprise Agents, Tools
├── 🌐 translations/    # Multi-language support (8+ languages)
└── 📋 STUDY_GUIDE.md   # Structured learning paths & time allocation
```

## Aspectos Destacados del Curso

✅ **Aprendizaje Progresivo**: Teoría → Práctica → Despliegue en producción  
✅ **Estudios de Casos Reales**: Microsoft, Japan Airlines, implementaciones empresariales  
✅ **Ejemplos Prácticos**: Más de 50 ejemplos, 10 demos completas de Foundry Local  
✅ **Enfoque en Rendimiento**: Mejoras de velocidad del 85%, reducciones de tamaño del 75%  
✅ **Multiplataforma**: Windows, móvil, embebido, híbrido nube-borde  
✅ **Listo para Producción**: Monitoreo, escalado, seguridad, marcos de cumplimiento

📖 **[Guía de Estudio Disponible](STUDY_GUIDE.md)**: Camino estructurado de 20 horas con asignación de tiempo y herramientas de autoevaluación.

---

**EdgeAI representa el futuro del despliegue de IA**: local-primero, preservando la privacidad y eficiente. Domina estas habilidades para construir la próxima generación de aplicaciones inteligentes.

## Otros Cursos

¡Nuestro equipo produce otros cursos! Echa un vistazo:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j para Principiantes](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js para Principiantes](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)
[![LangChain para Principiantes](https://img.shields.io/badge/LangChain%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://github.com/microsoft/langchain-for-beginners?WT.mc_id=m365-94501-dwahlin)
---

### Azure / Edge / MCP / Agentes
[![AZD para Principiantes](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Edge AI para Principiantes](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP para Principiantes](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Agentes AI para Principiantes](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Serie de IA Generativa
[![IA Generativa para Principiantes](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![IA Generativa (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![IA Generativa (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![IA Generativa (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### Aprendizaje Básico
[![ML para Principiantes](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![Ciencia de Datos para Principiantes](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![IA para Principiantes](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![Ciberseguridad para Principiantes](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![Desarrollo Web para Principiantes](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![IoT para Principiantes](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![Desarrollo XR para Principiantes](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Serie Copilot

[![Copilot for AI Paired Programming](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot for C#/.NET](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot Adventure](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## Obtener ayuda

Si te quedas atascado o tienes alguna pregunta sobre cómo crear aplicaciones de IA, únete a:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Si tienes comentarios sobre el producto o errores mientras construyes, visita:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos responsabilizamos por malentendidos o interpretaciones erróneas que surjan del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
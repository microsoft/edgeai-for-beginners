<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8421c922085232ba081c848d98f69f35",
  "translation_date": "2026-01-01T09:48:34+00:00",
  "source_file": "README.md",
  "language_code": "es"
}
-->
# EdgeAI for Beginners 


![Imagen de portada del curso](../../translated_images/cover.eb18d1b9605d754b.es.png)

[![Colaboradores de GitHub](https://img.shields.io/github/contributors/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/graphs/contributors)
[![Issues de GitHub](https://img.shields.io/github/issues/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/issues)
[![Pull requests de GitHub](https://img.shields.io/github/issues-pr/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/pulls)
[![PRs Bienvenidos](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

[![Discord de Microsoft Foundry](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Sigue estos pasos para comenzar a usar estos recursos:

1. **Haz un fork del repositorio**: Haz clic en [![GitHub forks](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork)
2. **Clona el repositorio**:   `git clone https://github.com/microsoft/edgeai-for-beginners.git`
3. [**Únete al Discord de Azure AI Foundry y conoce a expertos y otros desarrolladores**](https://discord.com/invite/ByRwuEEgH4)


### 🌐 Soporte multilingüe

#### Admitido mediante GitHub Action (Automatizado y siempre actualizado)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Árabe](../ar/README.md) | [Bengalí](../bn/README.md) | [Búlgaro](../bg/README.md) | [Birmano (Myanmar)](../my/README.md) | [Chino (Simplificado)](../zh/README.md) | [Chino (Tradicional, Hong Kong)](../hk/README.md) | [Chino (Tradicional, Macao)](../mo/README.md) | [Chino (Tradicional, Taiwán)](../tw/README.md) | [Croata](../hr/README.md) | [Checo](../cs/README.md) | [Danés](../da/README.md) | [Neerlandés](../nl/README.md) | [Estonio](../et/README.md) | [Finés](../fi/README.md) | [Francés](../fr/README.md) | [Alemán](../de/README.md) | [Griego](../el/README.md) | [Hebreo](../he/README.md) | [Hindi](../hi/README.md) | [Húngaro](../hu/README.md) | [Indonesio](../id/README.md) | [Italiano](../it/README.md) | [Japonés](../ja/README.md) | [Canarés](../kn/README.md) | [Coreano](../ko/README.md) | [Lituano](../lt/README.md) | [Malayo](../ms/README.md) | [Malayalam](../ml/README.md) | [Maratí](../mr/README.md) | [Nepalí](../ne/README.md) | [Pidgin nigeriano](../pcm/README.md) | [Noruego](../no/README.md) | [Persa (Farsi)](../fa/README.md) | [Polaco](../pl/README.md) | [Portugués (Brasil)](../br/README.md) | [Portugués (Portugal)](../pt/README.md) | [Panyabí (Gurmukhi)](../pa/README.md) | [Rumano](../ro/README.md) | [Ruso](../ru/README.md) | [Serbio (Cirílico)](../sr/README.md) | [Eslovaco](../sk/README.md) | [Esloveno](../sl/README.md) | [Español](./README.md) | [Swahili](../sw/README.md) | [Sueco](../sv/README.md) | [Tagalo (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugú](../te/README.md) | [Tailandés](../th/README.md) | [Turco](../tr/README.md) | [Ucraniano](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamita](../vi/README.md)
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

**Si deseas que se admitan idiomas adicionales, están listados [aquí](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md)**
## Introducción

Bienvenido a **EdgeAI for Beginners** – tu recorrido completo por el mundo transformador de la Inteligencia Artificial en el edge. Este curso cierra la brecha entre las poderosas capacidades de IA y su implementación práctica y real en dispositivos edge, permitiéndote aprovechar el potencial de la IA directamente donde se generan los datos y donde deben tomarse las decisiones.

### Lo que dominarás

Este curso te lleva desde conceptos fundamentales hasta implementaciones listas para producción, cubriendo:
- **Modelos de Lenguaje Pequeños (SLMs)** optimizados para despliegue en el edge
- **Optimización consciente del hardware** en plataformas diversas
- **Inferencia en tiempo real** con capacidades de preservación de la privacidad
- **Estrategias de despliegue en producción** para aplicaciones empresariales

### Por qué EdgeAI importa

Edge AI representa un cambio de paradigma que aborda desafíos críticos modernos:
- **Privacidad y seguridad**: Procesa datos sensibles localmente sin exposición a la nube
- **Rendimiento en tiempo real**: Elimina la latencia de red para aplicaciones críticas en tiempo
- **Eficiencia de costos**: Reduce ancho de banda y gastos en computación en la nube
- **Operaciones resilientes**: Mantiene la funcionalidad durante cortes de red
- **Cumplimiento regulatorio**: Satisface requisitos de soberanía de datos

### Edge AI

Edge AI se refiere a ejecutar algoritmos de IA y modelos de lenguaje localmente en hardware, cerca de donde se generan los datos, sin depender de recursos en la nube para la inferencia. Reduce la latencia, mejora la privacidad y permite la toma de decisiones en tiempo real.

### Principios básicos:
- **Inferencia en el dispositivo**: Los modelos de IA se ejecutan en dispositivos edge (teléfonos, routers, microcontroladores, PCs industriales)
- **Capacidad sin conexión**: Funciona sin conectividad persistente a internet
- **Baja latencia**: Respuestas inmediatas adecuadas para sistemas en tiempo real
- **Soberanía de los datos**: Mantiene los datos sensibles localmente, mejorando la seguridad y el cumplimiento

### Modelos de Lenguaje Pequeños (SLMs)

Los SLMs como Phi-4, Mistral-7B y Gemma son versiones optimizadas de LLMs más grandes—entrenadas o destiladas para:
- **Reducir el uso de memoria**: Uso eficiente de la memoria limitada de dispositivos edge
- **Menor demanda de cómputo**: Optimizados para rendimiento en CPU y GPU de edge
- **Tiempos de inicio más rápidos**: Inicialización rápida para aplicaciones con alta capacidad de respuesta

Desbloquean potentes capacidades de PLN mientras satisfacen las limitaciones de:
- **Sistemas embebidos**: Dispositivos IoT y controladores industriales
- **Dispositivos móviles**: Smartphones y tablets con capacidades sin conexión
- **Dispositivos IoT**: Sensores y dispositivos inteligentes con recursos limitados
- **Servidores de edge**: Unidades de procesamiento locales con recursos GPU limitados
- **Computadoras personales**: Escenarios de despliegue en escritorio y portátil

## Módulos del curso & Navegación

| Module | Topic | Focus Area | Key Content | Level | Duration |
|--------|-------|------------|-------------|--------|----------|
| [📖 00 ](./introduction.md) | [Introducción a EdgeAI](./introduction.md) | Fundamentos y contexto | Descripción general de EdgeAI • Aplicaciones industriales • Introducción a SLM • Objetivos de aprendizaje | Principiante | 1-2 hrs |
| [📚 01](../../Module01) | [Fundamentos de EdgeAI](./Module01/README.md) | Comparación Cloud vs Edge AI | Fundamentos de EdgeAI • Casos de estudio reales • Guía de implementación • Despliegue en edge | Principiante | 3-4 hrs |
| [🧠 02](../../Module02) | [Fundamentos de modelos SLM](./Module02/README.md) | Familias de modelos y arquitectura | Familia Phi • Familia Qwen • Familia Gemma • BitNET • μModel • Phi-Silica | Principiante | 4-5 hrs |
| [🚀 03](../../Module03) | [Práctica de despliegue SLM](./Module03/README.md) | Despliegue local y en la nube | Aprendizaje avanzado • Entorno local • Despliegue en la nube | Intermedio | 4-5 hrs |
| [⚙️ 04](../../Module04) | [Kit de herramientas de optimización de modelos](./Module04/README.md) | Optimización multiplataforma | Introducción • Llama.cpp • Microsoft Olive • OpenVINO • Apple MLX • Síntesis de flujos de trabajo | Intermedio | 5-6 hrs |
| [🔧 05](../../Module05) | [SLMOps en producción](./Module05/README.md) | Operaciones en producción | Introducción a SLMOps • Destilación de modelos • Fine-tuning • Despliegue en producción | Avanzado | 5-6 hrs |
| [🤖 06](../../Module06) | [Agentes de IA y llamada a funciones](./Module06/README.md) | Marcos de agentes y MCP | Introducción a agentes • Llamada a funciones • Protocolo de contexto de modelos | Avanzado | 4-5 hrs |
| [💻 07](../../Module07) | [Implementación de plataforma](./Module07/README.md) | Ejemplos multiplataforma | Kit de herramientas de IA • Foundry Local • Desarrollo en Windows | Avanzado | 3-4 hrs |
| [🏭 08](../../Module08) | [Kit de herramientas Foundry Local](./Module08/README.md) | Ejemplos listos para producción | Aplicaciones de ejemplo (ver detalles abajo) | Experto | 8-10 hrs |

### 🏭 **Módulo 08: Aplicaciones de ejemplo**

- [01: REST Chat: Inicio rápido](./Module08/samples/01/README.md)
- [02: Integración del SDK de OpenAI](./Module08/samples/02/README.md)
- [03: Descubrimiento de modelos y evaluación comparativa](./Module08/samples/03/README.md)
- [04: Aplicación Chainlit RAG](./Module08/samples/04/README.md)
- [05: Orquestación multiagente](./Module08/samples/05/README.md)
- [06: Enrutador "Modelos como Herramientas"](./Module08/samples/06/README.md)
- [07: Cliente API directo](./Module08/samples/07/README.md)
- [08: Aplicación de chat para Windows 11](./Module08/samples/08/README.md)
- [09: Sistema multiagente avanzado](./Module08/samples/09/README.md)
- [10: Framework de herramientas Foundry](./Module08/samples/10/README.md)

### 🎓 **Taller: Ruta de aprendizaje práctica**

Materiales completos de taller práctico con implementaciones listas para producción:

- **[Guía del taller](./Workshop/Readme.md)** - Objetivos de aprendizaje completos, resultados y navegación de recursos
- **Ejemplos en Python** (6 sesiones) - Actualizados con mejores prácticas, manejo de errores y documentación completa
- **Jupyter Notebooks** (8 interactivos) - Tutoriales paso a paso con benchmarks y monitoreo de rendimiento
- **Guías de sesión** - Guías detalladas en markdown para cada sesión del taller
- **Herramientas de validación** - Scripts para verificar la calidad del código y ejecutar pruebas básicas

**Qué construirás:**
- Aplicaciones de chat de IA locales con soporte de streaming
- Pipelines RAG con evaluación de calidad (RAGAS)
- Herramientas de evaluación comparativa y comparación multmodelo
- Sistemas de orquestación multiagente
- Enrutamiento inteligente de modelos con selección basada en tareas

### 📊 **Resumen de la ruta de aprendizaje**
- **Duración total**: 36-45 horas
- **Ruta para principiantes**: Módulos 01-02 (7-9 horas)  
- **Ruta intermedia**: Módulos 03-04 (9-11 horas)
- **Ruta avanzada**: Módulos 05-07 (12-15 horas)
- **Ruta de experto**: Módulo 08 (8-10 horas)

## Qué construirás

### 🎯 Competencias clave
- **Arquitectura Edge AI**: Diseñar sistemas de IA con prioridad local e integración con la nube
- **Optimización de modelos**: Cuantizar y comprimir modelos para despliegue en el edge (aumento de velocidad del 85%, reducción de tamaño del 75%)
- **Despliegue multiplataforma**: Windows, móvil, embebidos y sistemas híbridos nube-edge
- **Operaciones de producción**: Monitorización, escalado y mantenimiento de IA en el edge en producción

### 🏗️ Proyectos prácticos
- **Foundry Local Chat Apps**: Aplicación nativa de Windows 11 con cambio de modelos
- **Sistemas multiagente**: Coordinador con agentes especialistas para flujos de trabajo complejos  
- **Aplicaciones RAG**: Procesamiento local de documentos con búsqueda vectorial
- **Enrutadores de modelos**: Selección inteligente entre modelos basada en el análisis de la tarea
- **Frameworks de API**: Clientes listos para producción con streaming y monitorización de estado
- **Herramientas multiplataforma**: Patrones de integración LangChain/Semantic Kernel

### 🏢 Aplicaciones industriales
**Fabricación** • **Salud** • **Vehículos autónomos** • **Ciudades inteligentes** • **Aplicaciones móviles**

## Inicio rápido

**Ruta de aprendizaje recomendada** (20-30 horas en total):

0. **📖 Introducción** ([Introduction.md](./introduction.md)): Fundamentos de EdgeAI + contexto industrial + marco de aprendizaje
1. **📚 Fundamentos** (Módulos 01-02): Conceptos de EdgeAI + familias de modelos SLM
2. **⚙️ Optimización** (Módulos 03-04): Despliegue + frameworks de cuantización  
3. **🚀 Producción** (Módulos 05-06): SLMOps + agentes de IA + llamadas a funciones
4. **💻 Implementación** (Módulos 07-08): Muestras de plataforma + kit de herramientas Foundry Local

Cada módulo incluye teoría, ejercicios prácticos y ejemplos de código listos para producción.

## Impacto profesional

**Roles técnicos**: Arquitecto de soluciones EdgeAI • Ingeniero ML (Edge) • Desarrollador IoT de IA • Desarrollador de IA móvil

**Sectores industriales**: Fabricación 4.0 • Tecnología sanitaria • Sistemas autónomos • FinTech • Electrónica de consumo

**Proyectos de portafolio**: Sistemas multiagente • Aplicaciones RAG de producción • Despliegue multiplataforma • Optimización de rendimiento

## Repository Structure

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

## Aspectos destacados del curso

✅ **Aprendizaje progresivo**: Teoría → Práctica → Despliegue en producción  
✅ **Casos reales**: Microsoft, Japan Airlines, implementaciones empresariales  
✅ **Ejemplos prácticos**: Más de 50 ejemplos, 10 demostraciones completas de Foundry Local  
✅ **Enfoque en rendimiento**: Mejoras de velocidad del 85%, reducciones de tamaño del 75%  
✅ **Multiplataforma**: Windows, móvil, embebidos, híbrido nube-edge  
✅ **Listo para producción**: Monitorización, escalado, seguridad, marcos de cumplimiento

📖 **[Guía de estudio disponible](STUDY_GUIDE.md)**: Ruta de aprendizaje estructurada de 20 horas con orientación sobre asignación de tiempo y herramientas de autoevaluación.

---

**EdgeAI representa el futuro del despliegue de la IA**: enfoque local, preservación de la privacidad y eficiencia. Domina estas habilidades para construir la próxima generación de aplicaciones inteligentes.

## Otros cursos

Nuestro equipo produce otros cursos! Consulta:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j para principiantes](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js para principiantes](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)

---

### Azure / Edge / MCP / Agentes
[![AZD para principiantes](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Edge AI para principiantes](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP para principiantes](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Agentes de IA para principiantes](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Serie de IA generativa
[![IA generativa para principiantes](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![IA generativa (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![IA generativa (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![IA generativa (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### Aprendizaje básico
[![ML para principiantes](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![Ciencia de datos para principiantes](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![IA para principiantes](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![Ciberseguridad para principiantes](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![Desarrollo web para principiantes](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![IoT para principiantes](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![Desarrollo XR para principiantes](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Serie Copilot
[![Copilot para programación asistida por IA](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot para C#/.NET](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Aventura Copilot](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## Obtener ayuda

Si te quedas atascado o tienes alguna pregunta sobre cómo crear aplicaciones de IA, únete a:

[![Discord de Microsoft Foundry](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Si tienes comentarios sobre el producto o errores mientras desarrollas, visita:

[![Foro de desarrolladores de Microsoft Foundry](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Descargo de responsabilidad:
Este documento ha sido traducido utilizando el servicio de traducción por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción humana profesional. No nos hacemos responsables de ningún malentendido o interpretación errónea que surja del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
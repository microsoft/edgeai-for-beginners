<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "78ca68df03ae43371b203ea43d346dec",
  "translation_date": "2025-10-30T10:34:14+00:00",
  "source_file": "CHANGELOG.md",
  "language_code": "es"
}
-->
# Registro de cambios

Todos los cambios importantes en EdgeAI para Principiantes están documentados aquí. Este proyecto utiliza entradas basadas en fechas y el estilo Keep a Changelog (Añadido, Modificado, Corregido, Eliminado, Documentación, Movido).

## 2025-10-30

### Añadido - Mejora integral de agentes de IA en el Módulo06
- **Integración del Marco de Agentes de Microsoft** (`Module06/01.IntroduceAgent.md`):
  - Sección completa sobre el Marco de Agentes de Microsoft para el desarrollo de agentes listos para producción
  - Patrones detallados de integración con Foundry Local para despliegue en el borde
  - Ejemplos de orquestación de múltiples agentes con modelos SLM especializados
  - Patrones de despliegue empresarial con gestión de recursos y monitoreo
  - Funciones de seguridad y cumplimiento para sistemas de agentes en el borde
  - Ejemplos de implementación en el mundo real (retail, salud, servicio al cliente)

- **Estrategias de despliegue de agentes SLM en producción**:
  - **Foundry Local**: Documentación completa de runtime de IA empresarial para el borde con instalación, configuración y patrones de producción
  - **Ollama**: Despliegue enfocado en la comunidad con monitoreo integral y gestión de modelos
  - **VLLM**: Motor de inferencia de alto rendimiento con técnicas avanzadas de optimización y características empresariales
  - Listas de verificación de despliegue en producción y tablas comparativas para las tres plataformas

- **Mejoras en los marcos SLM optimizados para el borde**:
  - **ONNX Runtime**: Nueva sección completa para el despliegue de agentes SLM multiplataforma
  - Patrones de despliegue universal en Windows, Linux, macOS, iOS y Android
  - Opciones de aceleración de hardware (CPU, GPU, NPU) con detección automática
  - Funciones listas para producción y optimizaciones específicas para agentes
  - Ejemplos completos de implementación con integración del Marco de Agentes de Microsoft

- **Referencias y lecturas adicionales**:
  - Biblioteca de recursos completa con más de 100 fuentes autorizadas
  - Artículos de investigación fundamentales sobre agentes de IA y Modelos de Lenguaje Pequeños
  - Documentación oficial de todos los principales marcos y herramientas
  - Informes de la industria, análisis de mercado y benchmarks técnicos
  - Recursos educativos, conferencias y foros comunitarios
  - Estándares, especificaciones y marcos de cumplimiento

### Modificado - Modernización del contenido del Módulo06
- **Objetivos de aprendizaje mejorados**: Se añadió dominio del Marco de Agentes de Microsoft y capacidades de despliegue en el borde
- **Enfoque en producción**: Cambio de conceptual a orientación lista para implementación con ejemplos de producción
- **Ejemplos de código**: Actualización de todos los ejemplos para usar patrones modernos de SDK y mejores prácticas
- **Patrones de arquitectura**: Se añadieron arquitecturas jerárquicas de agentes y coordinación borde-a-nube
- **Optimización del rendimiento**: Mejorado con recomendaciones de gestión de recursos y escalado automático

### Documentación - Mejora de la estructura del Módulo06
- **Cobertura integral del Marco de Agentes**: Desde conceptos básicos hasta despliegue empresarial
- **Estrategias de despliegue en producción**: Guías completas para Foundry Local, Ollama y VLLM
- **Optimización multiplataforma**: Se añadió ONNX Runtime para despliegue universal
- **Biblioteca de recursos**: Referencias extensas para aprendizaje continuo e implementación

### Añadido - Actualización de documentación del Protocolo de Contexto de Modelo (MCP) en el Módulo06
- **Modernización de la introducción al MCP** (`Module06/03.IntroduceMCP.md`):
  - Actualizado con las últimas especificaciones del MCP de modelcontextprotocol.io (versión 2025-06-18)
  - Añadida analogía oficial de USB-C para conexiones estandarizadas de aplicaciones de IA
  - Actualización de la sección de arquitectura con diseño oficial de dos capas (Capa de Datos + Capa de Transporte)
  - Documentación mejorada de primitivas centrales con primitivas de servidor (Herramientas, Recursos, Prompts) y primitivas de cliente (Muestreo, Elicitación, Registro)

- **Referencias y recursos completos del MCP**:
  - Añadido enlace **MCP para Principiantes** (https://aka.ms/mcp-for-beginners)
  - Documentación y especificaciones oficiales del MCP (modelcontextprotocol.io)
  - Recursos de desarrollo incluyendo MCP Inspector e implementaciones de referencia
  - Estándares técnicos (JSON-RPC 2.0, JSON Schema, OpenAPI, Server-Sent Events)

### Añadido - Integración de Qualcomm QNN en el Módulo04
- **Nueva Sección 7: Suite de Optimización Qualcomm QNN** (`Module04/05.QualcommQNN.md`):
  - Guía completa de más de 400 líneas sobre el marco unificado de inferencia de IA de Qualcomm
  - Cobertura detallada de computación heterogénea (Hexagon NPU, Adreno GPU, Kryo CPU)
  - Optimización consciente del hardware para plataformas Snapdragon con distribución inteligente de carga de trabajo
  - Técnicas avanzadas de cuantización (INT8, INT16, precisión mixta) para despliegue móvil
  - Optimización de inferencia eficiente en consumo de energía para dispositivos con batería y aplicaciones en tiempo real
  - Guía completa de instalación con configuración del SDK de QNN y entorno
  - Ejemplos prácticos: conversión de PyTorch a QNN, optimización multibackend, generación de binarios de contexto
  - Patrones de uso avanzado: configuración de backend personalizado, cuantización dinámica, perfilado de rendimiento
  - Sección completa de resolución de problemas y recursos comunitarios

- **Estructura mejorada del Módulo04**:
  - Actualización de README.md para incluir 7 secciones progresivas (antes eran 6)
  - Añadido Qualcomm QNN a la tabla de benchmarks de rendimiento (mejora de velocidad de 5-15x, reducción de memoria de 50-80%)
  - Resultados de aprendizaje completos para despliegue de IA móvil y optimización de energía

### Modificado - Actualizaciones de documentación del Módulo04
- **Mejora de la documentación de Microsoft Olive** (`Module04/03.MicrosoftOlive.md`):
  - Añadida sección completa "Repositorio de Recetas Olive" que cubre más de 100 recetas de optimización preconstruidas
  - Cobertura detallada de familias de modelos compatibles (Phi, Llama, Qwen, Gemma, Mistral, DeepSeek)
  - Ejemplos prácticos para personalización de recetas y contribuciones comunitarias
  - Mejorado con benchmarks de rendimiento y orientación de integración

- **Reordenamiento de secciones en el Módulo04**:
  - Apple MLX movido a la Sección 5 (antes era la Sección 6)
  - Síntesis de flujo de trabajo movida a la Sección 6 (antes era la Sección 7)
  - Qualcomm QNN posicionado como Sección 7 (enfoque especializado en móvil/borde)
  - Actualización de todas las referencias de archivos y enlaces de navegación en consecuencia

### Corregido - Validación de muestras del taller
- **Validación y reparación de chat_bootstrap.py**:
  - Corregida declaración de importación dañada (`util.util.workshop_utils` → `util.workshop_utils`)
  - Creado `__init__.py` faltante en el paquete util para resolución adecuada de módulos de Python
  - Instaladas dependencias requeridas (openai, foundry-local-sdk) en el entorno conda
  - Validación exitosa de la ejecución de muestras con prompts predeterminados y personalizados
  - Confirmada integración con el servicio Foundry Local y carga de modelos (phi-4-mini con optimización CUDA)

### Documentación - Actualizaciones completas de guías
- **Reestructuración completa de README.md del Módulo04**:
  - Añadido Qualcomm QNN como marco de optimización principal junto con OpenVINO, Olive, MLX
  - Actualización de resultados de aprendizaje del capítulo para incluir despliegue de IA móvil y optimización de energía
  - Mejora de la tabla de comparación de rendimiento con métricas de QNN y casos de uso móvil/borde
  - Mantenimiento de la progresión lógica desde soluciones empresariales hasta optimizaciones específicas de plataforma

- **Referencias cruzadas y navegación**:
  - Actualización de todos los enlaces internos y referencias de archivos para nueva numeración de secciones
  - Mejora de la descripción de síntesis de flujo de trabajo para incluir entornos móviles, de escritorio y en la nube
  - Añadidos enlaces de recursos completos para el ecosistema de desarrolladores de Qualcomm

## 2025-10-08

### Añadido - Actualización integral del taller
- **Reescritura completa de README.md del taller**:
  - Añadida introducción completa explicando la propuesta de valor de Edge AI (privacidad, rendimiento, costo)
  - Creación de 6 objetivos de aprendizaje principales con competencias detalladas
  - Añadida tabla de resultados de aprendizaje con entregables y matriz de competencias
  - Incluida sección de habilidades listas para la carrera con relevancia en la industria
  - Añadida guía de inicio rápido con requisitos previos y configuración en 3 pasos
  - Creación de tablas de recursos para muestras de Python (8 archivos con tiempos de ejecución)
  - Añadida tabla de notebooks Jupyter (8 notebooks con calificaciones de dificultad)
  - Creación de tabla de documentación (7 documentos clave con orientación "Usar Cuando")
  - Añadidas recomendaciones de ruta de aprendizaje para diferentes niveles de habilidad

- **Infraestructura de validación y pruebas del taller**:
  - Creado `scripts/validate_samples.py` - Herramienta de validación integral para sintaxis, importaciones y mejores prácticas
  - Creado `scripts/test_samples.py` - Ejecutador de pruebas rápidas para todas las muestras de Python
  - Añadida documentación de validación a `scripts/README.md`

- **Documentación integral**:
  - Creado `SAMPLES_UPDATE_SUMMARY.md` - Guía detallada de más de 400 líneas que cubre todas las mejoras
  - Creado `UPDATE_COMPLETE.md` - Resumen ejecutivo de la finalización de la actualización
  - Creado `QUICK_REFERENCE.md` - Tarjeta de referencia rápida para el taller

### Modificado - Modernización de muestras de Python del taller
- **Actualización de las 8 muestras de Python con mejores prácticas**:
  - Mejora del manejo de errores con bloques try-except en todas las operaciones de E/S
  - Añadidos hints de tipo y docstrings completos
  - Implementación de un patrón de registro consistente [INFO]/[ERROR]/[RESULT]
  - Protección de importaciones opcionales con sugerencias de instalación
  - Mejora de la retroalimentación al usuario en todas las muestras

- **session01/chat_bootstrap.py**:
  - Mejora de la inicialización del cliente con mensajes de error completos
  - Manejo mejorado de errores de streaming con validación de fragmentos
  - Añadido manejo de excepciones para la indisponibilidad del servicio

- **session02/rag_pipeline.py**:
  - Añadidas protecciones de importación para sentence-transformers con sugerencias de instalación
  - Mejora del manejo de errores en operaciones de embedding y generación
  - Formateo mejorado de salida con resultados estructurados

- **session02/rag_eval_ragas.py**:
  - Protección de importaciones opcionales (ragas, datasets) con mensajes de error amigables
  - Añadido manejo de errores para métricas de evaluación
  - Mejora del formateo de salida para resultados de evaluación

- **session03/benchmark_oss_models.py**:
  - Implementación de degradación elegante (continúa en fallos de modelos)
  - Añadido reporte detallado de progreso y manejo de errores por modelo
  - Mejora del cálculo de estadísticas con recuperación integral de errores

- **session04/model_compare.py**:
  - Añadidos hints de tipo (tipos de retorno Tuple)
  - Mejora del formateo de salida con resultados JSON estructurados
  - Implementación de manejo de errores por modelo con recuperación

- **session05/agents_orchestrator.py**:
  - Mejora de Agent.act() con docstrings completos
  - Añadido manejo de errores en la canalización con registro etapa por etapa
  - Mejora de la gestión de memoria y seguimiento de estado

- **session06/models_router.py**:
  - Mejora de la documentación de funciones para todos los componentes de enrutamiento
  - Añadido registro detallado en la función route()
  - Mejora de la salida de pruebas con resultados estructurados

- **session06/models_pipeline.py**:
  - Añadido manejo de errores a la función auxiliar chat()
  - Mejora de pipeline() con registro de etapas y reporte de progreso
  - Mejora de main() con recuperación integral de errores

### Documentación - Mejora de la documentación del taller
- Actualización del README.md principal con sección del taller destacando la ruta de aprendizaje práctica
- Mejora de STUDY_GUIDE.md con sección completa del taller incluyendo:
  - Objetivos de aprendizaje y áreas de enfoque de estudio
  - Preguntas de autoevaluación
  - Ejercicios prácticos con estimaciones de tiempo
  - Asignación de tiempo para estudio concentrado y a tiempo parcial
  - Añadido el taller a la plantilla de seguimiento de progreso
- Actualización de la guía de asignación de tiempo de 20 horas a 30 horas (incluyendo el taller)
- Añadidas descripciones de muestras del taller y resultados de aprendizaje al README

### Corregido
- Resueltos patrones inconsistentes de manejo de errores en las muestras del taller
- Corregidos errores de importación de dependencias opcionales con protecciones adecuadas
- Corrección de hints de tipo faltantes en funciones críticas
- Abordada la insuficiente retroalimentación al usuario en escenarios de error
- Corregidos problemas de validación con infraestructura de pruebas integral

---

## 2025-09-23

### Modificado - Modernización importante del Módulo 08
- **Alineación integral con patrones del repositorio Microsoft Foundry-Local**
  - Actualización de todos los ejemplos de código para usar `FoundryLocalManager` moderno e integración con OpenAI SDK
  - Reemplazo de llamadas manuales `requests` obsoletas con uso adecuado de SDK
  - Alineación de patrones de implementación con documentación oficial de Microsoft y muestras

- **Modernización de 05.AIPoweredAgents.md**:
  - Actualización de orquestación de múltiples agentes para usar patrones modernos de SDK
  - Mejora de la implementación del coordinador con características avanzadas (bucles de retroalimentación, monitoreo de rendimiento)
  - Añadido manejo de errores integral y verificación de salud del servicio
  - Integración de referencias adecuadas a muestras locales (`samples/05/multi_agent_orchestration.ipynb`)
  - Actualización de ejemplos de llamadas a funciones para usar el parámetro moderno `tools` en lugar de `functions` obsoleto
  - Añadidos patrones listos para producción con monitoreo y seguimiento de estadísticas

- **Reescritura completa de 06.ModelsAsTools.md**:
  - Reemplazo del registro básico de herramientas con implementación de enrutador de modelos inteligente
  - Añadida selección de modelos basada en palabras clave para diferentes tipos de tareas (general, razonamiento, código, creativo)
  - Integración de configuración basada en entorno con asignación flexible de modelos
  - Mejora con monitoreo integral de salud del servicio y manejo de errores
  - Añadidos patrones de despliegue en producción con monitoreo de solicitudes y seguimiento de rendimiento
  - Alineación con implementación local en `samples/06/router.py` y `samples/06/model_router.ipynb`

- **Mejoras en la estructura de documentación**:
  - Añadidas secciones de resumen destacando modernización y alineación con SDK
  - Mejora con emojis y mejor formato para mayor legibilidad
  - Añadidas referencias adecuadas a archivos de muestras locales en toda la documentación
  - Incluida orientación de implementación lista para producción y mejores prácticas

### Añadido
- Secciones de resumen completas en archivos del Módulo 08 destacando integración moderna de SDK
- Aspectos destacados de arquitectura mostrando características avanzadas (sistemas multi-agente, enrutamiento inteligente)
- Referencias directas a implementaciones de muestras locales para experiencia práctica
- Guía de despliegue en producción con patrones de monitoreo y manejo de errores
- Ejemplos interactivos de notebooks Jupyter con características avanzadas y benchmarks

### Corregido
- Discrepancias de alineación entre documentación e implementaciones reales de muestras
- Patrones de uso de SDK obsoletos en todo el Módulo 08
- Referencias faltantes a biblioteca de muestras locales completas
- Enfoques de implementación inconsistentes en diferentes secciones

---

## 2025-09-18

### Añadido
- Módulo 08: Microsoft Foundry Local – Kit de herramientas completo para desarrolladores
  - Seis sesiones: configuración, integración con Azure AI Foundry, modelos de código abierto, demos de vanguardia, agentes y modelos como herramientas
  - Ejemplos ejecutables en `Module08/samples/01`–`06` con instrucciones de cmd de Windows
    - `01` Chat rápido REST (`chat_quickstart.py`)
    - `02` Inicio rápido del SDK con soporte para OpenAI/Foundry Local y Azure OpenAI (`sdk_quickstart.py`)
    - `03` CLI lista y prueba (`list_and_bench.cmd`)
    - `04` Demostración de Chainlit (`app.py`)
    - `05` Orquestación de múltiples agentes (`python -m samples.05.agents.coordinator`)
    - `06` Enrutador de Modelos-como-Herramientas (`router.py`)
- Soporte de Azure OpenAI en el ejemplo del SDK de la Sesión 2 con configuración de variables de entorno
- `.vscode/settings.json` apuntando a `Module08/.venv` para mejorar la resolución de análisis de Python
- `.env` con sugerencia de `PYTHONPATH` para la compatibilidad con VS Code/Pylance

### Cambiado
- Modelo predeterminado actualizado a `phi-4-mini` en los documentos y ejemplos del Módulo 08; eliminadas las menciones restantes de `phi-3.5` dentro del Módulo 08
- Mejoras en el enrutador (`Module08/samples/06/router.py`):
  - Descubrimiento de endpoints mediante `foundry service status` con análisis de expresiones regulares
  - Verificación de salud de `/v1/models` al inicio
  - Registro de modelos configurable por entorno (`GENERAL_MODEL`, `REASONING_MODEL`, `CODE_MODEL`, `TOOL_REGISTRY` JSON)
- Requisitos actualizados: `Module08/requirements.txt` ahora incluye `openai` (junto con `requests`, `chainlit`)
- Orientación sobre el ejemplo de Chainlit aclarada y se añadieron soluciones a problemas; resolución de importaciones mediante configuración del espacio de trabajo

### Corregido
- Problemas de importación resueltos:
  - El enrutador ya no depende de un módulo inexistente `utils`; las funciones están integradas
  - El coordinador utiliza importación relativa (`from .specialists import ...`) y se invoca mediante la ruta del módulo
  - Configuración de VS Code/Pylance para resolver importaciones de `chainlit` y paquetes
- Corregido un pequeño error tipográfico en `STUDY_GUIDE.md` y se añadió cobertura del Módulo 08

### Eliminado
- Eliminado `Module08/infra/obs.py` no utilizado y se eliminó el directorio vacío `infra/`; los patrones de observabilidad se mantienen como opcionales en los documentos

### Movido
- Consolidación de las demostraciones del Módulo 08 bajo `Module08/samples` con carpetas numeradas por sesión
  - Aplicación de Chainlit movida a `samples/04`
  - Agentes movidos a `samples/05` y se añadieron archivos `__init__.py` para la resolución de paquetes

### Documentos
- Documentos de la sesión del Módulo 08 y todos los READMEs de los ejemplos enriquecidos con referencias de Microsoft Learn y proveedores confiables
- `Module08/README.md` actualizado con Descripción general de ejemplos, configuración del enrutador y consejos de validación
- Sección de Foundry Local en Windows de `Module07/README.md` validada contra los documentos de Learn
- `STUDY_GUIDE.md` actualizado:
  - Se añadió el Módulo 08 al resumen, horarios, rastreador de progreso
  - Se añadió una sección de Referencias completa (Foundry Local, Azure AI, Olive, ONNX Runtime, OpenVINO, MLX, Llama.cpp, vLLM, Ollama, AI Toolkit, Windows ML)

---

## Histórico (resumen)
- Arquitectura del curso y módulos establecidos (Módulos 01–07)
- Modernización iterativa del contenido, estandarización de formato y casos de estudio añadidos
- Cobertura ampliada de marcos de optimización (Llama.cpp, Olive, OpenVINO, Apple MLX)

## No publicado / Pendiente (propuestas)
- Pruebas opcionales por ejemplo para validar la disponibilidad de Foundry Local
- Revisar traducciones para alinear referencias de modelos (por ejemplo, `phi-4-mini`) donde sea apropiado
- Añadir configuración mínima de pyright si los equipos prefieren estrictos a nivel de espacio de trabajo

---

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por garantizar la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse como la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que puedan surgir del uso de esta traducción.
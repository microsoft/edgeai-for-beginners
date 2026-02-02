# Cuadernos del Taller

> **Cuadernos Interactivos de Jupyter para Aprender Edge AI Prácticamente**
>
> Tutoriales progresivos y autoguiados que van desde completaciones básicas de chat hasta sistemas avanzados de múltiples agentes utilizando Microsoft Foundry Local y Modelos de Lenguaje Pequeños.

---

## 📖 Introducción

Bienvenido a la colección de **Cuadernos del Taller EdgeAI para Principiantes**. Estos cuadernos interactivos de Jupyter ofrecen una experiencia de aprendizaje práctico donde escribirás, ejecutarás y experimentarás con código de Edge AI en tiempo real.

### ¿Por qué usar cuadernos de Jupyter?

A diferencia de los tutoriales tradicionales, estos cuadernos ofrecen:

- **Aprendizaje Interactivo**: Ejecuta celdas de código y observa resultados inmediatos  
- **Experimentación**: Modifica parámetros y observa los cambios en tiempo real  
- **Documentación**: Explicaciones en línea y celdas de markdown que te guían a través de los conceptos  
- **Reproducibilidad**: Ejemplos funcionales completos que puedes consultar y reutilizar  
- **Visualización**: Visualiza métricas de rendimiento, embeddings y resultados en línea  

### ¿Qué hace especiales a estos cuadernos?

Cada cuaderno está diseñado siguiendo **mejores prácticas listas para producción**:

✅ **Manejo Integral de Errores** - Degradación elegante y mensajes de error informativos  
✅ **Pistas de Tipos y Documentación** - Firmas de funciones claras y docstrings  
✅ **Monitoreo de Rendimiento** - Seguimiento del uso de tokens y medición de latencia  
✅ **Diseño Modular** - Patrones reutilizables que puedes adaptar a tus proyectos  
✅ **Complejidad Progresiva** - Construcción sistemática sobre sesiones previas  

---

## 🎯 Objetivos de Aprendizaje

### Habilidades Clave que Desarrollarás

Al trabajar con estos cuadernos, dominarás:

1. **Gestión de Servicios de AI Local**
   - Configurar y gestionar servicios de Microsoft Foundry Local  
   - Seleccionar y cargar modelos adecuados para tu hardware  
   - Monitorear el uso de recursos y optimizar el rendimiento  
   - Manejar el descubrimiento de servicios y la verificación de estado  

2. **Desarrollo de Aplicaciones de AI**
   - Implementar completaciones de chat compatibles con OpenAI localmente  
   - Construir interfaces de streaming para una mejor experiencia de usuario  
   - Diseñar prompts efectivos para Modelos de Lenguaje Pequeños  
   - Integrar modelos locales en aplicaciones  

3. **Generación Aumentada por Recuperación (RAG)**
   - Crear búsquedas semánticas con embeddings vectoriales  
   - Basar las respuestas de LLM en documentos específicos del dominio  
   - Evaluar la calidad de RAG con métricas RAGAS  
   - Escalar de prototipo a producción  

4. **Optimización de Rendimiento**
   - Comparar múltiples modelos de manera sistemática  
   - Medir latencia, rendimiento y tiempo del primer token  
   - Comparar Modelos de Lenguaje Pequeños con Modelos de Lenguaje Grandes  
   - Seleccionar modelos óptimos basados en la relación rendimiento/calidad  

5. **Orquestación de Múltiples Agentes**
   - Diseñar agentes especializados para diferentes tareas  
   - Implementar memoria de agentes y gestión de contexto  
   - Coordinar múltiples agentes en flujos de trabajo complejos  
   - Construir patrones de coordinación para la colaboración entre agentes  

6. **Enrutamiento Inteligente de Modelos**
   - Implementar detección de intención y coincidencia de patrones  
   - Enrutar consultas automáticamente a los modelos apropiados  
   - Construir pipelines de múltiples pasos (planificar → ejecutar → refinar)  
   - Diseñar arquitecturas escalables de modelos como herramientas  

---

## 🎓 Resultados de Aprendizaje

### ¿Qué Construirás?

| Cuaderno | Entregable | Habilidades Demostradas | Dificultad |
|----------|------------|-------------------------|------------|
| **Sesión 01** | Aplicación de chat con streaming | Configuración de servicios, completaciones básicas, UX de streaming | ⭐ Principiante |
| **Sesión 02 (RAG)** | Pipeline RAG con evaluación | Embeddings, búsqueda semántica, métricas de calidad | ⭐⭐ Intermedio |
| **Sesión 02 (Eval)** | Evaluador de calidad RAG | Métricas RAGAS, evaluación sistemática | ⭐⭐ Intermedio |
| **Sesión 03** | Benchmark de múltiples modelos | Medición de rendimiento, comparación de modelos | ⭐⭐ Intermedio |
| **Sesión 04** | Comparador SLM vs LLM | Análisis de compensaciones, estrategias de optimización | ⭐⭐⭐ Avanzado |
| **Sesión 05** | Orquestador de múltiples agentes | Diseño de agentes, memoria, coordinación | ⭐⭐⭐ Avanzado |
| **Sesión 06 (Router)** | Sistema de enrutamiento inteligente | Detección de intención, selección de modelos | ⭐⭐⭐ Avanzado |
| **Sesión 06 (Pipeline)** | Pipeline de múltiples pasos | Flujos de trabajo de planificar/ejecutar/refinar | ⭐⭐⭐ Avanzado |

### Progresión de Competencias

```
Session 01 ────► Session 02 ────► Session 03 ────► Session 04 ────► Session 05-06
   Basic            RAG             Benchmarking      Comparison      Multi-Agent
   Chat             Systems         & Performance     & Optimization  Orchestration
   
Foundation    │   Intermediate   │   Advanced       │   Expert
──────────────┴──────────────────┴──────────────────┴──────────────►
```

---

## 📅 Programa del Taller

### 🚀 Taller de Medio Día (3.5 horas)

**Perfecto para: Sesiones de capacitación en equipo, hackatones, talleres en conferencias**

| Hora | Duración | Sesión | Temas | Actividades |
|------|----------|--------|-------|-------------|
| **0:00** | 30 min | Configuración e Introducción | Configuración del entorno, instalación de Foundry Local | Instalar dependencias, verificar configuración |
| **0:30** | 30 min | Sesión 01 | Completaciones básicas de chat, streaming | Ejecutar cuaderno, modificar prompts |
| **1:00** | 45 min | Sesión 02 | Pipeline RAG, embeddings, evaluación | Construir sistema RAG, probar consultas |
| **1:45** | 15 min | Descanso | ☕ Café y preguntas | — |
| **2:00** | 30 min | Sesión 03 | Benchmarking de múltiples modelos | Comparar 3+ modelos |
| **2:30** | 30 min | Sesión 04 | Compensaciones SLM vs LLM | Analizar rendimiento/calidad |
| **3:00** | 30 min | Sesión 05-06 | Sistemas de múltiples agentes y enrutamiento | Explorar patrones avanzados |

**Resultado**: Los asistentes se irán con 6 aplicaciones de Edge AI funcionales y patrones de código listos para producción.

---

### 🎓 Taller de Día Completo (6 horas)

**Perfecto para: Capacitación en profundidad, bootcamps, cursos universitarios**

| Hora | Duración | Sesión | Temas | Actividades |
|------|----------|--------|-------|-------------|
| **0:00** | 45 min | Configuración y Teoría | Configuración del entorno, fundamentos de Edge AI | Instalar, verificar, discutir casos de uso |
| **0:45** | 45 min | Sesión 01 | Profundización en completaciones de chat | Implementar chat básico y de streaming |
| **1:30** | 30 min | Descanso | ☕ Café y networking | — |
| **2:00** | 60 min | Sesión 02 (Ambas) | Pipeline RAG + Evaluación RAGAS | Construir sistema RAG completo |
| **3:00** | 30 min | Laboratorio Práctico 1 | RAG personalizado para tu dominio | Aplicar a tus propios documentos |
| **3:30** | 30 min | Almuerzo | 🍽️ | — |
| **4:00** | 45 min | Sesión 03 | Metodología de benchmarking | Comparación sistemática de modelos |
| **4:45** | 45 min | Sesión 04 | Estrategias de optimización | Análisis SLM vs LLM |
| **5:30** | 60 min | Sesión 05-06 | Orquestación avanzada | Sistemas de múltiples agentes, enrutamiento |
| **6:30** | 30 min | Laboratorio Práctico 2 | Construir sistema de agentes personalizado | Diseñar tu propio orquestador |

**Resultado**: Comprensión profunda de los patrones de Edge AI más 2 proyectos personalizados.

---

### 📚 Aprendizaje Autodirigido (2 semanas)

**Perfecto para: Estudiantes individuales, cursos en línea, autoaprendizaje**

#### Semana 1: Fundamentos (6 horas)

| Día | Enfoque | Duración | Cuadernos | Tarea |
|-----|---------|----------|-----------|-------|
| **Lun** | Configuración y Conceptos Básicos | 1.5 hrs | Sesión 01 | Modificar prompts, probar streaming |
| **Mié** | Fundamentos de RAG | 2 hrs | Sesión 02 (ambas) | Agregar tus propios documentos |
| **Vie** | Benchmarking | 1.5 hrs | Sesión 03 | Comparar modelos adicionales |
| **Sáb** | Revisión y Práctica | 1 hr | Todos Semana 1 | Completar ejercicios, depurar |

#### Semana 2: Avanzado (5 horas)

| Día | Enfoque | Duración | Cuadernos | Tarea |
|-----|---------|----------|-----------|-------|
| **Lun** | Optimización | 1.5 hrs | Sesión 04 | Documentar compensaciones |
| **Mié** | Sistemas de Múltiples Agentes | 2 hrs | Sesión 05 | Diseñar agentes personalizados |
| **Vie** | Enrutamiento Inteligente | 1.5 hrs | Sesión 06 (ambas) | Construir lógica de enrutamiento |
| **Sáb** | Proyecto Final | 2 hrs | Integración | Combinar múltiples patrones |

**Resultado**: Dominio de patrones de Edge AI más un proyecto de portafolio.

---

## 📔 Descripción de los Cuadernos

### 📘 Sesión 01: Inicio del Chat
**Archivo**: `session01_chat_bootstrap.ipynb`  
**Duración**: 20-30 minutos  
**Requisitos Previos**: Ninguno  
**Dificultad**: ⭐ Principiante

**Lo que Aprenderás**:
- Instalar y configurar el SDK de Python de Foundry Local  
- Usar `FoundryLocalManager` para el descubrimiento automático de servicios  
- Implementar completaciones básicas de chat con la API compatible con OpenAI  
- Construir respuestas de streaming para una mejor experiencia de usuario  
- Manejar errores y la falta de disponibilidad del servicio de manera elegante  

**Conceptos Clave**: Gestión de servicios, completaciones de chat, streaming, manejo de errores  

**Lo que Construirás**: Aplicación de chat interactiva con soporte de streaming  

---

### 📗 Sesión 02: Pipeline RAG
**Archivo**: `session02_rag_pipeline.ipynb`  
**Duración**: 30-45 minutos  
**Requisitos Previos**: Sesión 01  
**Dificultad**: ⭐⭐ Intermedio

**Lo que Aprenderás**:
- Implementar el patrón de Generación Aumentada por Recuperación (RAG)  
- Crear embeddings vectoriales con sentence-transformers  
- Construir búsqueda semántica con similitud coseno  
- Basar las respuestas de LLM en documentos del dominio  
- Manejar dependencias opcionales con guardas de importación  

**Conceptos Clave**: Arquitectura RAG, embeddings, búsqueda semántica, similitud vectorial  

**Lo que Construirás**: Sistema de preguntas y respuestas basado en documentos  

---

### 📗 Sesión 02: Evaluación de RAG con RAGAS
**Archivo**: `session02_rag_eval_ragas.ipynb`  
**Duración**: 30-45 minutos  
**Requisitos Previos**: Pipeline RAG de la Sesión 02  
**Dificultad**: ⭐⭐ Intermedio

**Lo que Aprenderás**:
- Evaluar la calidad de RAG con métricas estándar de la industria  
- Medir la relevancia del contexto, relevancia de las respuestas y fidelidad  
- Usar el marco RAGAS para una evaluación sistemática  
- Identificar y solucionar problemas de calidad en RAG  
- Construir conjuntos de datos de evaluación para tu dominio  

**Conceptos Clave**: Evaluación de RAG, métricas RAGAS, medición de calidad, pruebas sistemáticas  

**Lo que Construirás**: Marco de evaluación de calidad RAG  

---

### 📙 Sesión 03: Benchmark de Modelos OSS
**Archivo**: `session03_benchmark_oss_models.ipynb`  
**Duración**: 30-45 minutos  
**Requisitos Previos**: Sesión 01  
**Dificultad**: ⭐⭐ Intermedio

**Lo que Aprenderás**:
- Realizar benchmarks sistemáticos de múltiples modelos  
- Medir latencia, rendimiento, tiempo del primer token  
- Implementar degradación elegante para fallos de modelos  
- Comparar el rendimiento entre familias de modelos  
- Visualizar y analizar resultados de benchmarks  

**Conceptos Clave**: Benchmarking de rendimiento, medición de latencia, comparación de modelos, análisis estadístico  

**Lo que Construirás**: Suite de benchmarking de múltiples modelos  

---

### 📙 Sesión 04: Comparación de Modelos (SLM vs LLM)
**Archivo**: `session04_model_compare.ipynb`  
**Duración**: 30-45 minutos  
**Requisitos Previos**: Sesiones 01, 03  
**Dificultad**: ⭐⭐⭐ Avanzado

**Lo que Aprenderás**:
- Comparar Modelos de Lenguaje Pequeños con Modelos de Lenguaje Grandes  
- Analizar las compensaciones entre rendimiento y calidad  
- Medir métricas de idoneidad para el edge  
- Seleccionar modelos óptimos según las restricciones de implementación  
- Documentar criterios de decisión para la selección de modelos  

**Conceptos Clave**: Selección de modelos, análisis de compensaciones, estrategias de optimización, planificación de implementación  

**Lo que Construirás**: Marco de comparación SLM vs LLM  

---

### 📕 Sesión 05: Orquestador de Múltiples Agentes
**Archivo**: `session05_agents_orchestrator.ipynb`  
**Duración**: 45-60 minutos  
**Requisitos Previos**: Sesiones 01-02  
**Dificultad**: ⭐⭐⭐ Avanzado

**Lo que Aprenderás**:
- Diseñar agentes especializados para diferentes tareas  
- Implementar memoria de agentes y gestión de contexto  
- Construir patrones de coordinación para la colaboración entre agentes  
- Manejar la comunicación y transferencia entre agentes  
- Monitorear el rendimiento del sistema de múltiples agentes  

**Conceptos Clave**: Arquitectura de agentes, patrones de coordinación, gestión de memoria, orquestación de agentes  

**Lo que Construirás**: Sistema de múltiples agentes con coordinador y especialistas  

---

### 📕 Sesión 06: Enrutador de Modelos
**Archivo**: `session06_models_router.ipynb`  
**Duración**: 30-45 minutos  
**Requisitos Previos**: Sesiones 01, 03  
**Dificultad**: ⭐⭐⭐ Avanzado

**Lo que Aprenderás**:
- Implementar detección de intención y coincidencia de patrones  
- Construir enrutamiento de modelos basado en palabras clave  
- Enrutar consultas automáticamente a los modelos apropiados  
- Configurar registros de múltiples modelos  
- Monitorear decisiones de enrutamiento y rendimiento  

**Conceptos Clave**: Detección de intención, enrutamiento de modelos, coincidencia de patrones, selección inteligente  

**Lo que Construirás**: Sistema de enrutamiento inteligente de modelos  

---

### 📕 Sesión 06: Pipeline de Múltiples Pasos
**Archivo**: `session06_models_pipeline.ipynb`  
**Duración**: 30-45 minutos  
**Requisitos Previos**: Sesiones 01, 06 Router  
**Dificultad**: ⭐⭐⭐ Avanzado

**Lo que Aprenderás**:
- Construir pipelines de AI de múltiples pasos (planificar → ejecutar → refinar)  
- Integrar enrutadores para la selección inteligente de modelos  
- Implementar manejo de errores y recuperación en el pipeline  
- Monitorear el rendimiento y las etapas del pipeline  
- Diseñar arquitecturas escalables de modelos como herramientas

**Conceptos Clave**: Arquitectura de pipeline, procesamiento en múltiples etapas, recuperación de errores, patrones de escalabilidad

**Lo que construirás**: Pipeline inteligente de múltiples pasos con enrutamiento

---

## 🚀 Comenzando

### Requisitos Previos

**Requisitos del Sistema**:
- **OS**: Windows 10/11, macOS 11+ o Linux (Ubuntu 20.04+)
- **RAM**: Mínimo 8GB, recomendado 16GB+
- **Almacenamiento**: 10GB+ de espacio libre para modelos
- **Hardware**: CPU con AVX2; GPU (CUDA, Qualcomm NPU) opcional

**Requisitos de Software**:
- **Python 3.8+** con pip
- **Jupyter Notebook** o **VS Code** con extensión de Jupyter
- **Microsoft Foundry Local** instalado y configurado
- **Git** (para clonar el repositorio)

### Pasos de Instalación

#### 1. Instalar Foundry Local

**Windows**:
```cmd
winget install Microsoft.FoundryLocal
```

**macOS**:
```bash
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**Verificar Instalación**:
```bash
foundry --version
```

#### 2. Configurar el Entorno de Python

```bash
# Navigate to Workshop directory
cd Workshop

# Create virtual environment
python -m venv .venv

# Activate virtual environment
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

#### 3. Iniciar Foundry Local

```bash
# Load a model (auto-downloads if needed)
foundry model run phi-4-mini

# Verify service is running
foundry service status
```

#### 4. Lanzar Jupyter

```bash
# Start Jupyter Notebook
jupyter notebook notebooks/

# Or use VS Code with Jupyter extension
code notebooks/
```

### Verificación Rápida

Ejecuta esto en una celda de Python para verificar la configuración:

```python
from foundry_local import FoundryLocalManager
import openai

# Initialize manager (auto-discovers service)
manager = FoundryLocalManager("phi-4-mini")

# Configure OpenAI client
client = openai.OpenAI(
    base_url=manager.endpoint,
    api_key=manager.api_key
)

# Test chat completion
response = client.chat.completions.create(
    model=manager.get_model_info("phi-4-mini").id,
    messages=[{"role": "user", "content": "Hello!"}]
)

print(response.choices[0].message.content)
```

**Salida Esperada**: Una respuesta de saludo del modelo local.

---

## 📝 Mejores Prácticas para el Taller

### Para Instructores

**Antes del Taller**:
- ✅ Envía las instrucciones de instalación con 1 semana de anticipación
- ✅ Prueba todos los notebooks en el hardware objetivo
- ✅ Prepara una guía de solución de problemas para problemas comunes
- ✅ Ten modelos de respaldo listos (phi-3.5-mini si phi-4-mini falla)
- ✅ Configura un canal de chat compartido para preguntas

**Durante el Taller**:
- ✅ Comienza con una verificación rápida del entorno (5 minutos)
- ✅ Comparte recursos de solución de problemas de inmediato
- ✅ Fomenta la experimentación y las modificaciones
- ✅ Usa los descansos estratégicamente (después de cada 2 sesiones)
- ✅ Ten asistentes disponibles para ayuda personalizada

**Después del Taller**:
- ✅ Comparte notebooks completos y soluciones funcionales
- ✅ Proporciona enlaces a recursos adicionales
- ✅ Crea una encuesta de retroalimentación para mejorar
- ✅ Ofrece horas de oficina para preguntas de seguimiento

### Para Participantes

**Maximiza tu Aprendizaje**:
- ✅ Completa la configuración antes de que comience el taller
- ✅ Ejecuta cada celda de código tú mismo (no solo leas)
- ✅ Experimenta con parámetros y prompts
- ✅ Toma notas sobre ideas y problemas encontrados
- ✅ Haz preguntas cuando estés atascado (otros probablemente tengan la misma pregunta)

**Errores Comunes a Evitar**:
- ❌ Saltarse el orden de ejecución de las celdas (ejecuta en secuencia)
- ❌ No leer cuidadosamente los mensajes de error
- ❌ Apresurarse sin entender
- ❌ Ignorar las explicaciones en markdown
- ❌ No guardar tus notebooks modificados

**Consejos de Depuración**:
1. **Servicio No Ejecutándose**: Verifica `foundry service status`
2. **Errores de Importación**: Asegúrate de que el entorno virtual esté activado
3. **Modelo No Encontrado**: Ejecuta `foundry model ls` para listar los modelos cargados
4. **Rendimiento Lento**: Revisa el uso de RAM, cierra otras aplicaciones
5. **Resultados Inesperados**: Reinicia el kernel y ejecuta todas las celdas desde el principio

---

## 🔗 Recursos Adicionales

### Materiales del Taller

- **[Guía Principal del Taller](../Readme.md)** - Resumen, objetivos de aprendizaje, resultados profesionales
- **[Ejemplos en Python](../../../../Workshop/samples)** - Scripts de Python correspondientes a cada sesión
- **[Guías de Sesión](../../../../Workshop)** - Guías detalladas en markdown (Sesión01-06)
- **[Scripts](../../../../Workshop/scripts)** - Utilidades de validación y prueba
- **[Solución de Problemas](./TROUBLESHOOTING.md)** - Problemas comunes y soluciones
- **[Inicio Rápido](./quickstart.md)** - Guía rápida para comenzar

### Documentación

- **[Documentación de Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)** - Documentación oficial de Microsoft
- **[OpenAI Python SDK](https://github.com/openai/openai-python)** - Referencia del SDK de OpenAI
- **[Sentence Transformers](https://www.sbert.net/)** - Documentación de modelos de embeddings
- **[Marco RAGAS](https://docs.ragas.io/)** - Métricas de evaluación RAG

### Comunidad

- **[Discusiones en GitHub](https://github.com/microsoft/edgeai-for-beginners/discussions)** - Haz preguntas, comparte proyectos
- **[Discord de Azure AI Foundry](https://discord.com/invite/ByRwuEEgH4)** - Soporte comunitario en tiempo real
- **[Stack Overflow](https://stackoverflow.com/questions/tagged/foundry-local)** - Preguntas y respuestas técnicas

---

## 🎯 Recomendaciones de Ruta de Aprendizaje

### Ruta para Principiantes (Comienza Aquí)

1. **Sesión 01** - Inicio de Chat
2. **Sesión 02** - Pipeline RAG
3. **Sesión 03** - Modelos de Benchmark

**Tiempo**: ~2 horas | **Enfoque**: Patrones fundamentales

---

### Ruta Intermedia

1. Completa la Ruta para Principiantes
2. **Sesión 02** - Evaluación RAG
3. **Sesión 04** - Comparación de Modelos

**Tiempo**: ~4 horas | **Enfoque**: Calidad y optimización

---

### Ruta Avanzada (Taller Completo)

1. Completa la Ruta Intermedia
2. **Sesión 05** - Orquestador Multi-Agente
3. **Sesión 06** - Enrutador de Modelos
4. **Sesión 06** - Pipeline de Múltiples Pasos

**Tiempo**: ~6 horas | **Enfoque**: Patrones de producción

---

### Ruta de Proyecto Personalizado

1. Completa la Ruta para Principiantes (Sesiones 01-03)
2. Elige UNA sesión avanzada según tu objetivo:
   - **¿Construyendo una app RAG?** → Sesión 02 Evaluación
   - **¿Optimizando rendimiento?** → Sesión 04 Comparación
   - **¿Workflows complejos?** → Sesión 05 Orquestador
   - **¿Arquitectura escalable?** → Sesión 06 Enrutador + Pipeline

**Tiempo**: ~3 horas | **Enfoque**: Habilidades específicas para proyectos

---

## 📊 Métricas de Éxito

Sigue tu progreso con estos hitos:

- [ ] **Configuración Completa** - Foundry Local funcionando, todas las dependencias instaladas
- [ ] **Primer Chat** - Sesión 01 completada, chat en streaming funcionando
- [ ] **RAG Construido** - Sesión 02 completada, sistema de QA de documentos funcional
- [ ] **Modelos Evaluados** - Sesión 03 completada, datos de rendimiento recopilados
- [ ] **Análisis de Compromisos** - Sesión 04 completada, criterios de selección de modelos documentados
- [ ] **Agentes Orquestados** - Sesión 05 completada, sistema multi-agente funcionando
- [ ] **Enrutamiento Implementado** - Sesión 06 completada, selección inteligente de modelos funcional
- [ ] **Proyecto Personalizado** - Aplicación de patrones del taller a tu propio caso de uso

---

## 🤝 Contribuciones

¿Encontraste un problema o tienes una sugerencia? ¡Aceptamos contribuciones!

- **Reportar Problemas**: [GitHub Issues](https://github.com/microsoft/edgeai-for-beginners/issues)
- **Sugerir Mejoras**: [GitHub Discussions](https://github.com/microsoft/edgeai-for-beginners/discussions)
- **Enviar PRs**: Sigue las [Guías de Contribución](../../AGENTS.md)

---

## 📄 Licencia

Este taller forma parte del repositorio [EdgeAI for Beginners](https://github.com/microsoft/edgeai-for-beginners) y está licenciado bajo la [Licencia MIT](../../../../LICENSE).

---

**¿Listo para construir aplicaciones Edge AI listas para producción?**  
**Comienza con [Sesión 01: Inicio de Chat](./session01_chat_bootstrap.ipynb) →**

---

*Última Actualización: 8 de octubre de 2025 | Versión del Taller: 2.0*

---

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que surjan del uso de esta traducción.
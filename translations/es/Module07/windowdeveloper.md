# Guía de Desarrollo de IA en el Borde para Windows

## Introducción

Bienvenido al desarrollo de IA en el borde para Windows: tu guía completa para crear aplicaciones inteligentes que aprovechan el poder de la IA en el dispositivo utilizando la plataforma Windows AI Foundry de Microsoft. Esta guía está diseñada específicamente para desarrolladores de Windows que desean integrar capacidades avanzadas de IA en el borde en sus aplicaciones, aprovechando al máximo la aceleración de hardware de Windows.

### La Ventaja de Windows AI

Windows AI Foundry representa una plataforma unificada, confiable y segura que respalda todo el ciclo de vida del desarrollo de IA: desde la selección y ajuste de modelos hasta la optimización y el despliegue en arquitecturas de CPU, GPU, NPU y nube híbrida. Esta plataforma democratiza el desarrollo de IA al ofrecer:

- **Abstracción de Hardware**: Despliegue sin problemas en silicio de AMD, Intel, NVIDIA y Qualcomm.
- **Inteligencia en el Dispositivo**: IA que preserva la privacidad y se ejecuta completamente en hardware local.
- **Rendimiento Optimizado**: Modelos preoptimizados para configuraciones de hardware de Windows.
- **Preparado para Empresas**: Características de seguridad y cumplimiento de grado de producción.

### Windows ML 
Windows Machine Learning (ML) permite a los desarrolladores de C#, C++ y Python ejecutar modelos de IA ONNX localmente en PCs con Windows a través de ONNX Runtime, con gestión automática de proveedores de ejecución para diferentes hardware (CPUs, GPUs, NPUs). [ONNX Runtime](https://onnxruntime.ai/docs/) se puede usar con modelos de PyTorch, Tensorflow/Keras, TFLite, scikit-learn y otros frameworks.


![WindowsML Un diagrama que ilustra un modelo ONNX pasando por Windows ML para luego alcanzar NPUs, GPUs y CPUs.](https://learn.microsoft.com/en-us/windows/ai/images/winml-diagram.png)

Windows ML proporciona una copia compartida de ONNX Runtime en todo Windows, además de la capacidad de descargar dinámicamente proveedores de ejecución (EPs).

### ¿Por qué Windows para IA en el Borde?

**Soporte Universal de Hardware**  
Windows ML ofrece optimización automática de hardware en todo el ecosistema de Windows, asegurando que tus aplicaciones de IA funcionen de manera óptima independientemente de la arquitectura de silicio subyacente.

**Runtime de IA Integrado**  
El motor de inferencia integrado de Windows ML elimina los requisitos de configuración compleja, permitiendo a los desarrolladores centrarse en la lógica de la aplicación en lugar de en preocupaciones de infraestructura.

**Optimización para PC Copilot+**  
APIs diseñadas específicamente para dispositivos Windows de próxima generación con Unidades de Procesamiento Neural (NPUs) dedicadas que ofrecen un rendimiento excepcional por vatio.

**Ecosistema de Desarrollo**  
Herramientas avanzadas como la integración con Visual Studio, documentación completa y aplicaciones de muestra que aceleran los ciclos de desarrollo.

## Objetivos de Aprendizaje

Al completar esta guía de desarrollo de IA en el borde para Windows, dominarás las habilidades esenciales para construir aplicaciones de IA listas para producción en la plataforma Windows.

### Competencias Técnicas Fundamentales

**Dominio de Windows AI Foundry**  
- Comprender la arquitectura y los componentes de la plataforma Windows AI Foundry.  
- Navegar por todo el ciclo de vida del desarrollo de IA dentro del ecosistema de Windows.  
- Implementar mejores prácticas de seguridad para aplicaciones de IA en el dispositivo.  
- Optimizar aplicaciones para diferentes configuraciones de hardware de Windows.  

**Experiencia en Integración de APIs**  
- Dominar las APIs de Windows AI para aplicaciones de texto, visión y multimodal.  
- Implementar la integración del modelo de lenguaje Phi Silica para generación de texto y razonamiento.  
- Desplegar capacidades de visión por computadora utilizando APIs de procesamiento de imágenes integradas.  
- Personalizar modelos preentrenados utilizando técnicas LoRA (Adaptación de Bajo Rango).  

**Implementación Local de Foundry**  
- Explorar, evaluar y desplegar modelos de lenguaje de código abierto utilizando Foundry Local CLI.  
- Comprender la optimización y cuantización de modelos para despliegue local.  
- Implementar capacidades de IA offline que funcionen sin conectividad a internet.  
- Gestionar ciclos de vida y actualizaciones de modelos en entornos de producción.  

**Despliegue de Windows ML**  
- Llevar modelos ONNX personalizados a aplicaciones de Windows utilizando Windows ML.  
- Aprovechar la aceleración automática de hardware en arquitecturas de CPU, GPU y NPU.  
- Implementar inferencia en tiempo real con utilización óptima de recursos.  
- Diseñar aplicaciones de IA escalables para diversas categorías de dispositivos Windows.  

### Habilidades de Desarrollo de Aplicaciones

**Desarrollo Multiplataforma en Windows**  
- Crear aplicaciones potenciadas por IA utilizando .NET MAUI para despliegue universal en Windows.  
- Integrar capacidades de IA en aplicaciones Win32, UWP y Web Progresivas.  
- Implementar diseños de interfaz de usuario responsivos que se adapten a los estados de procesamiento de IA.  
- Manejar operaciones de IA asincrónicas con patrones adecuados de experiencia de usuario.  

**Optimización de Rendimiento**  
- Perfilar y optimizar el rendimiento de inferencia de IA en diferentes configuraciones de hardware.  
- Implementar gestión eficiente de memoria para modelos de lenguaje grandes.  
- Diseñar aplicaciones que se degraden de manera elegante según las capacidades de hardware disponibles.  
- Aplicar estrategias de caché para operaciones de IA utilizadas con frecuencia.  

**Preparación para Producción**  
- Implementar manejo de errores completo y mecanismos de respaldo.  
- Diseñar telemetría y monitoreo para el rendimiento de aplicaciones de IA.  
- Aplicar mejores prácticas de seguridad para almacenamiento y ejecución de modelos de IA locales.  
- Planificar estrategias de despliegue para aplicaciones empresariales y de consumo.  

### Comprensión Estratégica y de Negocios

**Arquitectura de Aplicaciones de IA**  
- Diseñar arquitecturas híbridas que optimicen entre procesamiento de IA local y en la nube.  
- Evaluar compensaciones entre tamaño de modelo, precisión y velocidad de inferencia.  
- Planificar arquitecturas de flujo de datos que mantengan la privacidad mientras habilitan inteligencia.  
- Implementar soluciones de IA rentables que escalen con las demandas de los usuarios.  

**Posicionamiento en el Mercado**  
- Comprender las ventajas competitivas de las aplicaciones de IA nativas de Windows.  
- Identificar casos de uso donde la IA en el dispositivo proporcione experiencias superiores.  
- Desarrollar estrategias de entrada al mercado para aplicaciones de Windows potenciadas por IA.  
- Posicionar aplicaciones para aprovechar los beneficios del ecosistema de Windows.  

## Ejemplos de SDK de Aplicaciones de Windows con IA

El SDK de Aplicaciones de Windows proporciona ejemplos completos que demuestran la integración de IA en múltiples frameworks y escenarios de despliegue. Estos ejemplos son referencias esenciales para comprender los patrones de desarrollo de IA en Windows.

### Ejemplos de Windows AI Foundry

| Ejemplo | Framework | Área de Enfoque | Características Clave |
|---------|-----------|-----------------|-----------------------|
| [cs-winui](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsAIFoundry/cs-winui) | C# WinUI 3 | Integración de APIs de Windows AI | Aplicación completa de WinUI que demuestra APIs de Windows AI, optimización para ARM64, despliegue empaquetado |

**Tecnologías Clave:**  
- APIs de Windows AI  
- Framework WinUI 3  
- Optimización para plataforma ARM64  
- Compatibilidad con PC Copilot+  
- Despliegue de aplicaciones empaquetadas  

**Requisitos Previos:**  
- Windows 11 con PC Copilot+ recomendado  
- Visual Studio 2022  
- Configuración de compilación ARM64  
- SDK de Aplicaciones de Windows 1.8.1+  

### Ejemplos de Windows ML

#### Ejemplos en C++

| Ejemplo | Tipo | Área de Enfoque | Características Clave |
|---------|------|-----------------|-----------------------|
| [CppConsoleDesktop](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Aplicación de Consola | Windows ML Básico | Descubrimiento de EP, opciones de línea de comandos, compilación de modelos |
| [CppConsoleDesktop.FrameworkDependent](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Aplicación de Consola | Despliegue con Framework | Runtime compartido, menor huella de despliegue |
| [CppConsoleDesktop.SelfContained](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Aplicación de Consola | Despliegue Autónomo | Despliegue independiente, sin dependencias de runtime |
| [CppConsoleDll](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | DLL | Uso de Biblioteca | WindowsML en biblioteca compartida, gestión de memoria |
| [CppResnetBuildDemo](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Demo | Tutorial de ResNet | Conversión de modelos, compilación de EP, tutorial Build 2025 |

#### Ejemplos en C#

**Aplicaciones de Consola**

| Ejemplo | Tipo | Área de Enfoque | Características Clave |
|---------|------|-----------------|-----------------------|
| [CSharpConsoleDesktop](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs) | Aplicación de Consola | Integración Básica en C# | Uso de ayudantes compartidos, interfaz de línea de comandos |
| [ResnetBuildDemoCS](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs) | Demo | Tutorial de ResNet | Conversión de modelos, compilación de EP, tutorial Build 2025 |

**Aplicaciones GUI**

| Ejemplo | Framework | Área de Enfoque | Características Clave |
|---------|-----------|-----------------|-----------------------|
| [cs-wpf](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs-wpf) | WPF | GUI de Escritorio | Clasificación de imágenes con interfaz WPF |
| [cs-winforms](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs-winforms) | Windows Forms | GUI Tradicional | Clasificación de imágenes con Windows Forms |
| [cs-winui](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs-winui) | WinUI 3 | GUI Moderna | Clasificación de imágenes con interfaz WinUI 3 |

#### Ejemplos en Python

| Ejemplo | Lenguaje | Área de Enfoque | Características Clave |
|---------|----------|-----------------|-----------------------|
| [SqueezeNetPython](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/python) | Python | Clasificación de Imágenes | Enlaces de WinML para Python, procesamiento por lotes de imágenes |

### Requisitos Previos de los Ejemplos

**Requisitos del Sistema:**  
- PC con Windows 11 ejecutando la versión 24H2 (build 26100) o superior.  
- Visual Studio 2022 con cargas de trabajo de C++ y .NET.  
- SDK de Aplicaciones de Windows 1.8.1 o posterior.  
- Python 3.10-3.13 para ejemplos en Python en dispositivos x64 y ARM64.  

**Específicos de Windows AI Foundry:**  
- PC Copilot+ recomendado para un rendimiento óptimo.  
- Configuración de compilación ARM64 para ejemplos de Windows AI.  
- Identidad de paquete requerida (las aplicaciones no empaquetadas ya no son compatibles).  

### Flujo de Trabajo Común de los Ejemplos

La mayoría de los ejemplos de Windows ML siguen este patrón estándar:

1. **Inicializar Entorno** - Crear entorno de ONNX Runtime.  
2. **Registrar Proveedores de Ejecución** - Descubrir y registrar aceleradores de hardware disponibles (CPU, GPU, NPU).  
3. **Cargar Modelo** - Cargar modelo ONNX, opcionalmente compilar para hardware objetivo.  
4. **Preprocesar Entrada** - Convertir imágenes/datos al formato de entrada del modelo.  
5. **Ejecutar Inferencia** - Ejecutar el modelo y obtener predicciones.  
6. **Procesar Resultados** - Aplicar softmax y mostrar las principales predicciones.  

### Archivos de Modelos Utilizados

| Modelo | Propósito | Incluido | Notas |
|--------|----------|----------|-------|
| SqueezeNet | Clasificación de imágenes ligera | ✅ Incluido | Preentrenado, listo para usar |
| ResNet-50 | Clasificación de imágenes de alta precisión | ❌ Requiere conversión | Usar [AI Toolkit](https://code.visualstudio.com/docs/intelligentapps/modelconversion) para conversión |

### Soporte de Hardware

Todos los ejemplos detectan y utilizan automáticamente el hardware disponible:  
- **CPU** - Soporte universal en todos los dispositivos Windows.  
- **GPU** - Detección y optimización automática para hardware gráfico disponible.  
- **NPU** - Aprovecha las Unidades de Procesamiento Neural en dispositivos compatibles (PCs Copilot+).  

## Componentes de la Plataforma Windows AI Foundry

### 1. APIs de Windows AI

Las APIs de Windows AI proporcionan capacidades de IA listas para usar impulsadas por modelos en el dispositivo, optimizadas para eficiencia y rendimiento en dispositivos PC Copilot+ con configuración mínima requerida.

#### Categorías Principales de APIs

**Modelo de Lenguaje Phi Silica**  
- Modelo de lenguaje pequeño pero poderoso para generación de texto y razonamiento.  
- Optimizado para inferencia en tiempo real con consumo mínimo de energía.  
- Soporte para ajuste personalizado utilizando técnicas LoRA.  
- Integración con búsqueda semántica y recuperación de conocimiento en Windows.  

**APIs de Visión por Computadora**  
- **Reconocimiento de Texto (OCR)**: Extraer texto de imágenes con alta precisión.  
- **Super Resolución de Imágenes**: Escalar imágenes utilizando modelos de IA locales.  
- **Segmentación de Imágenes**: Identificar y aislar objetos específicos en imágenes.  
- **Descripción de Imágenes**: Generar descripciones detalladas de contenido visual.  
- **Borrado de Objetos**: Eliminar objetos no deseados de imágenes con repintado impulsado por IA.  

**Capacidades Multimodales**  
- **Integración Visión-Lenguaje**: Combinar comprensión de texto e imágenes.  
- **Búsqueda Semántica**: Permitir consultas en lenguaje natural en contenido multimedia.  
- **Recuperación de Conocimiento**: Construir experiencias de búsqueda inteligentes con datos locales.  

### 2. Foundry Local

Foundry Local proporciona a los desarrolladores acceso rápido a modelos de lenguaje de código abierto listos para usar en Windows Silicon, ofreciendo la capacidad de explorar, probar, interactuar y desplegar modelos en aplicaciones locales.

#### Aplicaciones de Ejemplo de Foundry Local

El [repositorio de Foundry Local](https://github.com/microsoft/Foundry-Local/tree/main/samples) proporciona ejemplos completos en múltiples lenguajes de programación y frameworks, demostrando diversos patrones de integración y casos de uso.

| Ejemplo | Lenguaje/Framework | Área de Enfoque | Características Clave |
|---------|---------------------|-----------------|-----------------------|
| [dotNET/rag](https://github.com/microsoft/Foundry-Local/tree/main/samples/dotNET/rag) | C# / .NET | Implementación RAG | Integración con Kernel Semántico, almacenamiento vectorial Qdrant, embeddings JINA, ingestión de documentos, chat en streaming |
| [electron/foundry-chat](https://github.com/microsoft/Foundry-Local/tree/main/samples/electron/foundry-chat) | JavaScript / Electron | Aplicación de Chat de Escritorio | Chat multiplataforma, cambio entre modelos locales/nube, integración con SDK de OpenAI, streaming en tiempo real |
| [js/hello-foundry-local](https://github.com/microsoft/Foundry-Local/tree/main/samples/js/hello-foundry-local) | JavaScript / Node.js | Integración Básica | Uso simple del SDK, inicialización de modelos, funcionalidad básica de chat |
| [python/hello-foundry-local](https://github.com/microsoft/Foundry-Local/tree/main/samples/python/hello-foundry-local) | Python | Integración Básica | Uso del SDK de Python, respuestas en streaming, API compatible con OpenAI |
| [rust/hello-foundry-local](https://github.com/microsoft/Foundry-Local/tree/main/samples/rust/hello-foundry-local) | Rust | Integración de sistemas | Uso de SDK de bajo nivel, operaciones asíncronas, cliente HTTP reqwest |

#### Categorías de ejemplos según el caso de uso

**RAG (Generación aumentada por recuperación)**
- **dotNET/rag**: Implementación completa de RAG utilizando Semantic Kernel, base de datos vectorial Qdrant y embeddings JINA
- **Arquitectura**: Ingestión de documentos → Fragmentación de texto → Embeddings vectoriales → Búsqueda por similitud → Respuestas contextuales
- **Tecnologías**: Microsoft.SemanticKernel, Qdrant.Client, embeddings BERT ONNX, finalización de chat en streaming

**Aplicaciones de escritorio**
- **electron/foundry-chat**: Aplicación de chat lista para producción con cambio entre modelos locales/nube
- **Características**: Selector de modelos, respuestas en streaming, manejo de errores, implementación multiplataforma
- **Arquitectura**: Proceso principal de Electron, comunicación IPC, scripts de precarga seguros

**Ejemplos de integración de SDK**
- **JavaScript (Node.js)**: Interacción básica con modelos y respuestas en streaming
- **Python**: Uso de API compatible con OpenAI con streaming asíncrono
- **Rust**: Integración de bajo nivel con reqwest y tokio para operaciones asíncronas

#### Requisitos previos para los ejemplos de Foundry Local

**Requisitos del sistema:**
- Windows 11 con Foundry Local instalado
- Node.js v16+ para ejemplos de JavaScript/Electron
- .NET 8.0+ para ejemplos en C#
- Python 3.10+ para ejemplos en Python
- Rust 1.70+ para ejemplos en Rust

**Instalación:**
```powershell
# Install Foundry Local
winget install Microsoft.FoundryLocal

# Verify installation
foundry --version
foundry model list
```

#### Configuración específica de los ejemplos

**Ejemplo RAG en dotNET:**
```powershell
# Install required packages via NuGet
# Microsoft.SemanticKernel.Connectors.Onnx
# Microsoft.SemanticKernel.Connectors.Qdrant
# Qdrant.Client

# Start Qdrant vector database
docker run -p 6333:6333 qdrant/qdrant

# Run Jupyter notebook
jupyter notebook rag_foundrylocal_demo.ipynb
```

**Ejemplo de chat en Electron:**
```powershell
# Set environment variables for cloud fallback
$env:YOUR_API_KEY="your-cloud-api-key"
$env:YOUR_ENDPOINT="your-cloud-endpoint"
$env:YOUR_MODEL_NAME="your-cloud-model"

# Install dependencies and run
npm install
npm start
```

**Ejemplos en JavaScript/Python/Rust:**
```powershell
# Download model (example with phi-3.5-mini)
foundry model run phi-3.5-mini

# Run respective sample
node src/app.js          # JavaScript
python src/app.py        # Python
cargo run               # Rust
```

#### Características clave

**Catálogo de modelos**
- Colección completa de modelos de código abierto preoptimizados
- Modelos optimizados para CPUs, GPUs y NPUs para implementación inmediata
- Soporte para familias de modelos populares como Llama, Mistral, Phi y modelos especializados por dominio

**Integración con CLI**
- Interfaz de línea de comandos para gestión e implementación de modelos
- Flujos de trabajo automatizados de optimización y cuantización
- Integración con entornos de desarrollo populares y pipelines CI/CD

**Implementación local**
- Operación completamente offline sin dependencias en la nube
- Soporte para formatos y configuraciones de modelos personalizados
- Servicio eficiente de modelos con optimización automática de hardware

### 3. Windows ML

Windows ML es la plataforma central de IA y el runtime de inferencia integrado en Windows, que permite a los desarrolladores implementar modelos personalizados de manera eficiente en el amplio ecosistema de hardware de Windows.

#### Beneficios de la arquitectura

**Soporte universal de hardware**
- Optimización automática para silicio AMD, Intel, NVIDIA y Qualcomm
- Soporte para ejecución en CPU, GPU y NPU con cambio transparente
- Abstracción de hardware que elimina el trabajo de optimización específico de la plataforma

**Flexibilidad de modelos**
- Soporte para el formato de modelo ONNX con conversión automática desde frameworks populares
- Implementación de modelos personalizados con rendimiento de nivel de producción
- Integración con arquitecturas de aplicaciones existentes en Windows

**Integración empresarial**
- Compatible con los marcos de seguridad y cumplimiento de Windows
- Soporte para herramientas de implementación y gestión empresarial
- Integración con sistemas de gestión y monitoreo de dispositivos Windows

## Flujo de trabajo de desarrollo

### Fase 1: Configuración del entorno y herramientas

**Preparación del entorno de desarrollo**
1. Instalar Visual Studio 2022 con cargas de trabajo de C++ y .NET
2. Instalar Windows App SDK 1.8.1 o posterior
3. Configurar herramientas CLI de Windows AI Foundry
4. Configurar la extensión AI Toolkit para Visual Studio Code
5. Establecer herramientas de monitoreo y perfilado de rendimiento
6. Asegurar la configuración de compilación ARM64 para optimización en PCs Copilot+

**Configuración del repositorio de ejemplos**
1. Clonar el [repositorio de ejemplos de Windows App SDK](https://github.com/microsoft/WindowsAppSDK-Samples)
2. Navegar a `Samples/WindowsAIFoundry/cs-winui` para ejemplos de API de Windows AI
3. Navegar a `Samples/WindowsML` para ejemplos completos de Windows ML
4. Revisar los [requisitos de compilación](https://learn.microsoft.com/windows/apps/windows-app-sdk/system-requirements) para las plataformas objetivo

**Exploración de la galería de desarrollo de IA**
- Explorar aplicaciones de ejemplo e implementaciones de referencia
- Probar APIs de Windows AI con demostraciones interactivas
- Revisar el código fuente para mejores prácticas y patrones
- Identificar ejemplos relevantes para su caso de uso específico

### Fase 2: Selección e integración de modelos

**Análisis de requisitos**
- Definir requisitos funcionales para capacidades de IA
- Establecer restricciones de rendimiento y objetivos de optimización
- Evaluar requisitos de privacidad y seguridad
- Planificar la arquitectura de implementación y estrategias de escalado

**Evaluación de modelos**
- Usar Foundry Local para probar modelos de código abierto para su caso de uso
- Comparar APIs de Windows AI con requisitos de modelos personalizados
- Evaluar compensaciones entre tamaño del modelo, precisión y velocidad de inferencia
- Prototipar enfoques de integración con los modelos seleccionados

### Fase 3: Desarrollo de aplicaciones

**Integración principal**
- Implementar integración con APIs de Windows AI con manejo adecuado de errores
- Diseñar interfaces de usuario que acomoden flujos de trabajo de procesamiento de IA
- Implementar estrategias de caché y optimización para inferencia de modelos
- Agregar telemetría y monitoreo para el rendimiento de operaciones de IA

**Pruebas y validación**
- Probar aplicaciones en diferentes configuraciones de hardware de Windows
- Validar métricas de rendimiento bajo diversas condiciones de carga
- Implementar pruebas automatizadas para la confiabilidad de las funcionalidades de IA
- Realizar pruebas de experiencia de usuario con características mejoradas por IA

### Fase 4: Optimización e implementación

**Optimización de rendimiento**
- Perfilar el rendimiento de la aplicación en configuraciones de hardware objetivo
- Optimizar el uso de memoria y estrategias de carga de modelos
- Implementar comportamiento adaptativo basado en capacidades de hardware disponibles
- Ajustar la experiencia del usuario para diferentes escenarios de rendimiento

**Implementación en producción**
- Empaquetar aplicaciones con las dependencias adecuadas de modelos de IA
- Implementar mecanismos de actualización para modelos y lógica de aplicaciones
- Configurar monitoreo y análisis para entornos de producción
- Planificar estrategias de despliegue para empresas y consumidores

## Ejemplos prácticos de implementación

### Ejemplo 1: Aplicación inteligente de procesamiento de documentos

Construir una aplicación de Windows que procese documentos utilizando múltiples capacidades de IA:

**Tecnologías utilizadas:**
- Phi Silica para resumen de documentos y respuestas a preguntas
- APIs de OCR para extracción de texto de documentos escaneados
- APIs de descripción de imágenes para análisis de gráficos y diagramas
- Modelos ONNX personalizados para clasificación de documentos

**Enfoque de implementación:**
- Diseñar arquitectura modular con componentes de IA enchufables
- Implementar procesamiento asíncrono para lotes grandes de documentos
- Agregar indicadores de progreso y soporte de cancelación para operaciones prolongadas
- Incluir capacidad offline para procesamiento de documentos sensibles

### Ejemplo 2: Sistema de gestión de inventario minorista

Crear un sistema de inventario impulsado por IA para aplicaciones minoristas:

**Tecnologías utilizadas:**
- Segmentación de imágenes para identificación de productos
- Modelos de visión personalizados para clasificación de marcas y categorías
- Implementación de modelos de lenguaje especializados para minoristas con Foundry Local
- Integración con sistemas existentes de POS e inventario

**Enfoque de implementación:**
- Construir integración con cámaras para escaneo de productos en tiempo real
- Implementar reconocimiento de productos por código de barras y visual
- Agregar consultas de inventario en lenguaje natural utilizando modelos locales
- Diseñar arquitectura escalable para despliegue en múltiples tiendas

### Ejemplo 3: Asistente de documentación en salud

Desarrollar una herramienta de documentación en salud que preserve la privacidad:

**Tecnologías utilizadas:**
- Phi Silica para generación de notas médicas y soporte de decisiones clínicas
- OCR para digitalizar registros médicos manuscritos
- Modelos de lenguaje médico personalizados implementados con Windows ML
- Almacenamiento vectorial local para recuperación de conocimiento médico

**Enfoque de implementación:**
- Garantizar operación completamente offline para privacidad del paciente
- Implementar validación y sugerencia de terminología médica
- Agregar registro de auditoría para cumplimiento regulatorio
- Diseñar integración con sistemas existentes de registros electrónicos de salud

## Estrategias de optimización de rendimiento

### Desarrollo consciente del hardware

**Optimización para NPU**
- Diseñar aplicaciones para aprovechar capacidades de NPU en PCs Copilot+
- Implementar retroceso gradual a GPU/CPU en dispositivos sin NPU
- Optimizar formatos de modelos para aceleración específica de NPU
- Monitorear utilización de NPU y características térmicas

**Gestión de memoria**
- Implementar estrategias eficientes de carga y caché de modelos
- Usar mapeo de memoria para modelos grandes para reducir el tiempo de inicio
- Diseñar aplicaciones conscientes de la memoria para dispositivos con recursos limitados
- Implementar cuantización de modelos para optimización de memoria

**Eficiencia de batería**
- Optimizar operaciones de IA para consumo mínimo de energía
- Implementar procesamiento adaptativo basado en el estado de la batería
- Diseñar procesamiento en segundo plano eficiente para operaciones continuas de IA
- Usar herramientas de perfilado de energía para optimizar el uso energético

### Consideraciones de escalabilidad

**Multihilos**
- Diseñar operaciones de IA seguras para hilos para procesamiento concurrente
- Implementar distribución eficiente de trabajo entre núcleos disponibles
- Usar patrones async/await para operaciones de IA no bloqueantes
- Planificar optimización de pools de hilos para diferentes configuraciones de hardware

**Estrategias de caché**
- Implementar caché inteligente para operaciones de IA utilizadas frecuentemente
- Diseñar estrategias de invalidación de caché para actualizaciones de modelos
- Usar caché persistente para operaciones de preprocesamiento costosas
- Implementar caché distribuido para escenarios multiusuario

## Mejores prácticas de seguridad y privacidad

### Protección de datos

**Procesamiento local**
- Garantizar que los datos sensibles nunca salgan del dispositivo local
- Implementar almacenamiento seguro para modelos de IA y datos temporales
- Usar características de seguridad de Windows para sandboxing de aplicaciones
- Aplicar cifrado para modelos almacenados y resultados de procesamiento intermedios

**Seguridad de modelos**
- Validar la integridad de los modelos antes de cargarlos y ejecutarlos
- Implementar mecanismos seguros de actualización de modelos
- Usar modelos firmados para prevenir manipulaciones
- Aplicar controles de acceso para archivos de modelos y configuraciones

### Consideraciones de cumplimiento

**Alineación regulatoria**
- Diseñar aplicaciones para cumplir con GDPR, HIPAA y otros requisitos regulatorios
- Implementar registro de auditoría para procesos de toma de decisiones de IA
- Proporcionar características de transparencia para resultados generados por IA
- Permitir control del usuario sobre el procesamiento de datos de IA

**Seguridad empresarial**
- Integrar con políticas de seguridad empresarial de Windows
- Soportar implementación gestionada a través de herramientas de gestión empresarial
- Implementar controles de acceso basados en roles para características de IA
- Proporcionar controles administrativos para funcionalidades de IA

## Solución de problemas y depuración

### Desafíos comunes de desarrollo

**Problemas de configuración de compilación**
- Asegurar configuración de plataforma ARM64 para ejemplos de APIs de Windows AI
- Verificar compatibilidad de versión de Windows App SDK (se requiere 1.8.1+)
- Comprobar que la identidad del paquete esté configurada correctamente (requerida para APIs de Windows AI)
- Validar que las herramientas de compilación soporten la versión del framework objetivo

**Problemas de carga de modelos**
- Validar compatibilidad de modelos ONNX con Windows ML
- Comprobar integridad de archivos de modelos y requisitos de formato
- Verificar requisitos de capacidad de hardware para modelos específicos
- Depurar problemas de asignación de memoria durante la carga de modelos
- Asegurar registro de proveedores de ejecución para aceleración de hardware

**Consideraciones de modo de implementación**
- **Modo autónomo**: Totalmente soportado con mayor tamaño de implementación
- **Modo dependiente del framework**: Huella más pequeña pero requiere runtime compartido
- **Aplicaciones no empaquetadas**: Ya no soportadas para APIs de Windows AI
- Usar `dotnet run -p:Platform=ARM64 -p:SelfContained=true` para implementación autónoma ARM64

**Problemas de rendimiento**
- Perfilar rendimiento de la aplicación en diferentes configuraciones de hardware
- Identificar cuellos de botella en pipelines de procesamiento de IA
- Optimizar operaciones de preprocesamiento y postprocesamiento de datos
- Implementar monitoreo de rendimiento y alertas

**Dificultades de integración**
- Depurar problemas de integración de APIs con manejo adecuado de errores
- Validar formatos de datos de entrada y requisitos de preprocesamiento
- Probar casos extremos y condiciones de error exhaustivamente
- Implementar registro completo para depuración de problemas en producción

### Herramientas y técnicas de depuración

**Integración con Visual Studio**
- Usar el depurador AI Toolkit para análisis de ejecución de modelos
- Implementar perfilado de rendimiento para operaciones de IA
- Depurar operaciones asíncronas de IA con manejo adecuado de excepciones
- Usar herramientas de perfilado de memoria para optimización

**Herramientas de Windows AI Foundry**
- Aprovechar CLI de Foundry Local para pruebas y validación de modelos
- Usar herramientas de prueba de APIs de Windows AI para verificación de integración
- Implementar registro personalizado para monitoreo de operaciones de IA
- Crear pruebas automatizadas para confiabilidad de funcionalidades de IA

## Preparación para el futuro de sus aplicaciones

### Tecnologías emergentes

**Hardware de próxima generación**
- Diseñar aplicaciones para aprovechar capacidades futuras de NPU
- Planificar para tamaños y complejidad de modelos incrementados
- Implementar arquitecturas adaptativas para hardware en evolución
- Considerar algoritmos preparados para computación cuántica para compatibilidad futura

**Capacidades avanzadas de IA**
- Prepararse para integración multimodal de IA en más tipos de datos
- Planificar para colaboración en tiempo real entre múltiples dispositivos
- Diseñar para capacidades de aprendizaje federado
- Considerar arquitecturas híbridas de inteligencia en el borde y la nube

### Aprendizaje continuo y adaptación

**Actualizaciones de modelos**
- Implementar mecanismos de actualización de modelos sin interrupciones
- Diseñar aplicaciones para adaptarse a capacidades mejoradas de modelos
- Planificar compatibilidad hacia atrás con modelos existentes
- Implementar pruebas A/B para evaluación de rendimiento de modelos

**Evolución de características**
- Diseñar arquitecturas modulares que acomoden nuevas capacidades de IA
- Planificar integración de APIs emergentes de Windows AI
- Implementar banderas de características para despliegue gradual de capacidades
- Diseñar interfaces de usuario que se adapten a características mejoradas de IA

## Conclusión

El desarrollo de IA en el borde con Windows representa la convergencia de capacidades de IA poderosas con la plataforma robusta, segura y escalable de Windows. Al dominar el ecosistema de Windows AI Foundry, los desarrolladores pueden crear aplicaciones inteligentes que ofrecen experiencias excepcionales a los usuarios mientras mantienen los más altos estándares de privacidad, seguridad y rendimiento.

La combinación de APIs de Windows AI, Foundry Local y Windows ML proporciona una base inigualable para construir la próxima generación de aplicaciones inteligentes en Windows. A medida que la IA continúa evolucionando, la plataforma Windows asegura que sus aplicaciones escalarán con tecnologías emergentes mientras mantienen compatibilidad y rendimiento en el diverso ecosistema de hardware de Windows.

Ya sea que esté construyendo aplicaciones para consumidores, soluciones empresariales o herramientas especializadas para la industria, el desarrollo de IA en el borde con Windows le permite crear experiencias inteligentes, receptivas y profundamente integradas que aprovechan todo el potencial de los dispositivos modernos de Windows.

## Recursos adicionales

### Documentación y aprendizaje
- [Documentación de Windows AI Foundry](https://learn.microsoft.com/windows/ai/)
- [Referencia de APIs de Windows AI](https://learn.microsoft.com/windows/ai/apis/)
- [Comience a construir una aplicación con APIs de Windows AI](https://learn.microsoft.com/windows/ai/apis/model-setup)
- [Introducción a Foundry Local](https://learn.microsoft.com/windows/ai/foundry-local/get-started/)
- [Descripción general de Windows ML](https://learn.microsoft.com/windows/ai/new-windows-ml/overview/)
- [Requisitos del sistema para Windows App SDK](https://docs.microsoft.com/windows/apps/windows-app-sdk/system-requirements)
- [Configuración del entorno de desarrollo para Windows App SDK](https://docs.microsoft.com/windows/apps/windows-app-sdk/set-up-your-development-environment)
- 

### Repositorios de ejemplos y código
- [Ejemplos de Windows App SDK - Windows AI Foundry](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsAIFoundry)
- [Ejemplos de Windows App SDK - Windows ML](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML)
- [Ejemplos de inferencia con ONNX Runtime](https://github.com/microsoft/onnxruntime-inference-examples)
- [Repositorio de ejemplos de Windows App SDK](https://github.com/microsoft/WindowsAppSDK-Samples)

### Herramientas de desarrollo
- [Kit de herramientas de IA para Visual Studio Code](https://learn.microsoft.com/windows/ai/toolkit/)
- [Galería de desarrollo de IA](https://learn.microsoft.com/windows/ai/ai-dev-gallery/)
- [Ejemplos de Windows AI](https://learn.microsoft.com/windows/ai/samples/)
- [Herramientas de conversión de modelos](https://code.visualstudio.com/docs/intelligentapps/modelconversion)

### Soporte técnico
- [Documentación de Windows ML](https://learn.microsoft.com/windows/ai/new-windows-ml/overview)
- [Documentación de ONNX Runtime](https://onnxruntime.ai/docs/)
- [Documentación de Windows App SDK](https://docs.microsoft.com/windows/apps/windows-app-sdk/)
- [Reportar problemas - Ejemplos de Windows App SDK](https://github.com/microsoft/WindowsAppSDK-Samples/issues)

### Comunidad y soporte
- [Comunidad de desarrolladores de Windows](https://developer.microsoft.com/en-us/windows/)
- [Blog de Windows AI Foundry](https://blogs.windows.com/windowsdeveloper/)
- [Entrenamiento de IA en Microsoft Learn](https://learn.microsoft.com/training/browse/?products=windows&subjects=artificial-intelligence)

---

*Esta guía está diseñada para evolucionar junto con el ecosistema de Windows AI, que avanza rápidamente. Las actualizaciones regulares garantizan la alineación con las últimas capacidades de la plataforma y las mejores prácticas de desarrollo.*

[08. Práctica con Microsoft Foundry Local - Kit completo para desarrolladores](../Module08/README.md)

---

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por garantizar la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse como la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que puedan surgir del uso de esta traducción.
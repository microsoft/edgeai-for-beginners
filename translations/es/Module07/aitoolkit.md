# AI Toolkit para Visual Studio Code - Guía de Desarrollo de Edge AI

## Introducción

Bienvenido a la guía completa para usar AI Toolkit en Visual Studio Code en el desarrollo de Edge AI. A medida que la inteligencia artificial se traslada de la computación centralizada en la nube a dispositivos distribuidos en el borde, los desarrolladores necesitan herramientas potentes e integradas que puedan manejar los desafíos únicos del despliegue en el borde, desde las limitaciones de recursos hasta los requisitos de operación sin conexión.

AI Toolkit para Visual Studio Code cierra esta brecha proporcionando un entorno de desarrollo completo diseñado específicamente para construir, probar y optimizar aplicaciones de inteligencia artificial que funcionen eficientemente en dispositivos del borde. Ya sea que estés desarrollando para sensores IoT, dispositivos móviles, sistemas embebidos o servidores en el borde, este conjunto de herramientas simplifica todo tu flujo de trabajo de desarrollo dentro del entorno familiar de VS Code.

Esta guía te llevará a través de los conceptos esenciales, herramientas y mejores prácticas para aprovechar AI Toolkit en tus proyectos de Edge AI, desde la selección inicial del modelo hasta el despliegue en producción.

## Resumen

AI Toolkit para Visual Studio Code es una extensión poderosa que simplifica el desarrollo de agentes y la creación de aplicaciones de inteligencia artificial. El conjunto de herramientas ofrece capacidades completas para explorar, evaluar y desplegar modelos de IA de una amplia gama de proveedores, incluidos Anthropic, OpenAI, GitHub, Google, mientras admite la ejecución de modelos locales utilizando ONNX y Ollama.

Lo que distingue a AI Toolkit es su enfoque integral en todo el ciclo de vida del desarrollo de IA. A diferencia de las herramientas tradicionales de desarrollo de IA que se centran en aspectos individuales, AI Toolkit proporciona un entorno integrado que abarca el descubrimiento de modelos, la experimentación, el desarrollo de agentes, la evaluación y el despliegue, todo dentro del entorno familiar de VS Code.

La plataforma está diseñada específicamente para la creación rápida de prototipos y el despliegue en producción, con características como generación de prompts, iniciadores rápidos, integraciones fluidas de herramientas MCP (Model Context Protocol) y amplias capacidades de evaluación. Para el desarrollo de Edge AI, esto significa que puedes desarrollar, probar y optimizar aplicaciones de IA para escenarios de despliegue en el borde de manera eficiente mientras mantienes el flujo de trabajo completo de desarrollo dentro de VS Code.

## Objetivos de Aprendizaje

Al final de esta guía, serás capaz de:

### Competencias Básicas
- **Instalar y configurar** AI Toolkit para Visual Studio Code para flujos de trabajo de desarrollo de Edge AI
- **Navegar y utilizar** la interfaz de AI Toolkit, incluyendo el Catálogo de Modelos, Playground y el Constructor de Agentes
- **Seleccionar y evaluar** modelos de IA adecuados para el despliegue en el borde según el rendimiento y las limitaciones de recursos
- **Convertir y optimizar** modelos utilizando el formato ONNX y técnicas de cuantización para dispositivos del borde

### Habilidades de Desarrollo de Edge AI
- **Diseñar e implementar** aplicaciones de Edge AI utilizando el entorno de desarrollo integrado
- **Realizar pruebas de modelos** en condiciones similares al borde utilizando inferencia local y monitoreo de recursos
- **Crear y personalizar** agentes de IA optimizados para escenarios de despliegue en el borde
- **Evaluar el rendimiento de los modelos** utilizando métricas relevantes para la computación en el borde (latencia, uso de memoria, precisión)

### Optimización y Despliegue
- **Aplicar técnicas de cuantización y poda** para reducir el tamaño del modelo mientras se mantiene un rendimiento aceptable
- **Optimizar modelos** para plataformas de hardware específicas del borde, incluyendo aceleración por CPU, GPU y NPU
- **Implementar mejores prácticas** para el desarrollo de Edge AI, incluyendo gestión de recursos y estrategias de respaldo
- **Preparar modelos y aplicaciones** para el despliegue en producción en dispositivos del borde

### Conceptos Avanzados de Edge AI
- **Integrar con marcos de Edge AI** incluyendo ONNX Runtime, Windows ML y TensorFlow Lite
- **Implementar arquitecturas de múltiples modelos** y escenarios de aprendizaje federado para entornos del borde
- **Solucionar problemas comunes de Edge AI** incluyendo limitaciones de memoria, velocidad de inferencia y compatibilidad de hardware
- **Diseñar estrategias de monitoreo y registro** para aplicaciones de Edge AI en producción

### Aplicación Práctica
- **Construir soluciones completas de Edge AI** desde la selección del modelo hasta el despliegue
- **Demostrar competencia** en flujos de trabajo de desarrollo específicos del borde y técnicas de optimización
- **Aplicar conceptos aprendidos** a casos de uso reales de Edge AI, incluyendo IoT, aplicaciones móviles y embebidas
- **Evaluar y comparar** diferentes estrategias de despliegue de Edge AI y sus compensaciones

## Características Clave para el Desarrollo de Edge AI

### 1. Catálogo de Modelos y Descubrimiento
- **Soporte Multi-Proveedor**: Explora y accede a modelos de IA de Anthropic, OpenAI, GitHub, Google y otros proveedores
- **Integración de Modelos Locales**: Descubrimiento simplificado de modelos ONNX y Ollama para despliegue en el borde
- **Modelos de GitHub**: Integración directa con el alojamiento de modelos de GitHub para un acceso simplificado
- **Comparación de Modelos**: Compara modelos lado a lado para encontrar el equilibrio óptimo para las limitaciones de dispositivos del borde

### 2. Playground Interactivo
- **Entorno de Pruebas Interactivo**: Experimentación rápida con las capacidades del modelo en un entorno controlado
- **Soporte Multimodal**: Prueba con imágenes, texto y otras entradas típicas en escenarios del borde
- **Experimentación en Tiempo Real**: Retroalimentación inmediata sobre las respuestas y el rendimiento del modelo
- **Optimización de Parámetros**: Ajusta los parámetros del modelo para los requisitos de despliegue en el borde

### 3. Constructor de Prompts (Agentes)
- **Generación de Lenguaje Natural**: Genera prompts iniciales utilizando descripciones en lenguaje natural
- **Refinamiento Iterativo**: Mejora los prompts basándote en las respuestas y el rendimiento del modelo
- **Descomposición de Tareas**: Divide tareas complejas con encadenamiento de prompts y salidas estructuradas
- **Soporte de Variables**: Usa variables en los prompts para un comportamiento dinámico del agente
- **Generación de Código de Producción**: Genera código listo para producción para un desarrollo rápido de aplicaciones

### 4. Ejecución Masiva y Evaluación
- **Pruebas Multi-Modelo**: Ejecuta múltiples prompts en modelos seleccionados simultáneamente
- **Pruebas Eficientes a Escala**: Prueba diversas entradas y configuraciones de manera eficiente
- **Casos de Prueba Personalizados**: Ejecuta agentes con casos de prueba para validar funcionalidad
- **Comparación de Rendimiento**: Compara resultados entre diferentes modelos y configuraciones

### 5. Evaluación de Modelos con Conjuntos de Datos
- **Métricas Estándar**: Prueba modelos de IA utilizando evaluadores integrados (F1 score, relevancia, similitud, coherencia)
- **Evaluadores Personalizados**: Crea tus propias métricas de evaluación para casos de uso específicos
- **Integración de Conjuntos de Datos**: Prueba modelos contra conjuntos de datos completos
- **Medición de Rendimiento**: Cuantifica el rendimiento del modelo para decisiones de despliegue en el borde

### 6. Capacidades de Ajuste Fino
- **Personalización de Modelos**: Personaliza modelos para casos de uso y dominios específicos
- **Adaptación Especializada**: Adapta modelos a dominios y requisitos especializados
- **Optimización para el Borde**: Ajusta modelos específicamente para las limitaciones de despliegue en el borde
- **Entrenamiento Específico de Dominio**: Crea modelos adaptados a casos de uso específicos del borde

### 7. Integración de Herramientas MCP
- **Conectividad con Herramientas Externas**: Conecta agentes a herramientas externas mediante servidores Model Context Protocol
- **Acciones en el Mundo Real**: Permite que los agentes consulten bases de datos, accedan a APIs o ejecuten lógica personalizada
- **Servidores MCP Existentes**: Usa herramientas desde protocolos de comando (stdio) o HTTP (eventos enviados por el servidor)
- **Desarrollo MCP Personalizado**: Construye y estructura nuevos servidores MCP con pruebas en el Constructor de Agentes

### 8. Desarrollo y Pruebas de Agentes
- **Soporte de Llamadas a Funciones**: Permite que los agentes invoquen funciones externas dinámicamente
- **Pruebas de Integración en Tiempo Real**: Prueba integraciones con ejecuciones en tiempo real y uso de herramientas
- **Versionado de Agentes**: Control de versiones para agentes con capacidades de comparación de resultados de evaluación
- **Depuración y Rastreo**: Capacidades de rastreo y depuración local para el desarrollo de agentes

## Flujo de Trabajo de Desarrollo de Edge AI

### Fase 1: Descubrimiento y Selección de Modelos
1. **Explora el Catálogo de Modelos**: Usa el catálogo de modelos para encontrar modelos adecuados para el despliegue en el borde
2. **Compara Rendimiento**: Evalúa modelos según tamaño, precisión y velocidad de inferencia
3. **Prueba Localmente**: Usa modelos Ollama o ONNX para probar localmente antes del despliegue en el borde
4. **Evalúa Requisitos de Recursos**: Determina las necesidades de memoria y computación para los dispositivos del borde objetivo

### Fase 2: Optimización de Modelos
1. **Convierte a ONNX**: Convierte modelos seleccionados al formato ONNX para compatibilidad con el borde
2. **Aplica Cuantización**: Reduce el tamaño del modelo mediante cuantización INT8 o INT4
3. **Optimización de Hardware**: Optimiza para hardware del borde objetivo (ARM, x86, aceleradores especializados)
4. **Validación de Rendimiento**: Valida que los modelos optimizados mantengan una precisión aceptable

### Fase 3: Desarrollo de Aplicaciones
1. **Diseño de Agentes**: Usa el Constructor de Agentes para crear agentes de IA optimizados para el borde
2. **Ingeniería de Prompts**: Desarrolla prompts que funcionen eficazmente con modelos más pequeños del borde
3. **Pruebas de Integración**: Prueba agentes en condiciones simuladas del borde
4. **Generación de Código**: Genera código de producción optimizado para el despliegue en el borde

### Fase 4: Evaluación y Pruebas
1. **Evaluación en Lote**: Prueba múltiples configuraciones para encontrar ajustes óptimos en el borde
2. **Perfilado de Rendimiento**: Analiza velocidad de inferencia, uso de memoria y precisión
3. **Simulación en el Borde**: Prueba en condiciones similares al entorno de despliegue en el borde objetivo
4. **Pruebas de Estrés**: Evalúa el rendimiento bajo diversas condiciones de carga

### Fase 5: Preparación para el Despliegue
1. **Optimización Final**: Aplica optimizaciones finales basadas en los resultados de las pruebas
2. **Empaquetado para Despliegue**: Empaqueta modelos y código para el despliegue en el borde
3. **Documentación**: Documenta los requisitos y configuraciones de despliegue
4. **Configuración de Monitoreo**: Prepara monitoreo y registro para el despliegue en el borde

## Audiencia Objetivo para el Desarrollo de Edge AI

### Desarrolladores de Edge AI
- Desarrolladores de aplicaciones que construyen dispositivos del borde y soluciones IoT impulsadas por IA
- Desarrolladores de sistemas embebidos que integran capacidades de IA en dispositivos con recursos limitados
- Desarrolladores móviles que crean aplicaciones de IA en el dispositivo para smartphones y tablets

### Ingenieros de Edge AI
- Ingenieros de IA que optimizan modelos para despliegue en el borde y gestionan pipelines de inferencia
- Ingenieros DevOps que despliegan y gestionan modelos de IA en infraestructuras distribuidas del borde
- Ingenieros de rendimiento que optimizan cargas de trabajo de IA para las limitaciones de hardware del borde

### Investigadores y Educadores
- Investigadores de IA que desarrollan modelos y algoritmos eficientes para la computación en el borde
- Educadores que enseñan conceptos de Edge AI y demuestran técnicas de optimización
- Estudiantes que aprenden sobre los desafíos y soluciones en el despliegue de Edge AI

## Casos de Uso de Edge AI

### Dispositivos IoT Inteligentes
- **Reconocimiento de Imágenes en Tiempo Real**: Despliega modelos de visión por computadora en cámaras y sensores IoT
- **Procesamiento de Voz**: Implementa reconocimiento de voz y procesamiento de lenguaje natural en altavoces inteligentes
- **Mantenimiento Predictivo**: Ejecuta modelos de detección de anomalías en dispositivos industriales del borde
- **Monitoreo Ambiental**: Despliega modelos de análisis de datos de sensores para aplicaciones ambientales

### Aplicaciones Móviles y Embebidas
- **Traducción en el Dispositivo**: Implementa modelos de traducción de idiomas que funcionan sin conexión
- **Realidad Aumentada**: Despliega reconocimiento de objetos en tiempo real y seguimiento para aplicaciones de RA
- **Monitoreo de Salud**: Ejecuta modelos de análisis de salud en dispositivos portátiles y equipos médicos
- **Sistemas Autónomos**: Implementa modelos de toma de decisiones para drones, robots y vehículos

### Infraestructura de Computación en el Borde
- **Centros de Datos en el Borde**: Despliega modelos de IA en centros de datos del borde para aplicaciones de baja latencia
- **Integración CDN**: Integra capacidades de procesamiento de IA en redes de entrega de contenido
- **Borde 5G**: Aprovecha la computación en el borde 5G para aplicaciones impulsadas por IA
- **Computación en la Niebla**: Implementa procesamiento de IA en entornos de computación en la niebla

## Instalación y Configuración

### Instalación de la Extensión
Instala la extensión AI Toolkit directamente desde el Visual Studio Code Marketplace:

**ID de la Extensión**: `ms-windows-ai-studio.windows-ai-studio`

**Métodos de Instalación**:
1. **Marketplace de VS Code**: Busca "AI Toolkit" en la vista de Extensiones
2. **Línea de Comando**: `code --install-extension ms-windows-ai-studio.windows-ai-studio`
3. **Instalación Directa**: Descarga desde [VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)

### Requisitos Previos para el Desarrollo de Edge AI
- **Visual Studio Code**: Se recomienda la última versión
- **Entorno Python**: Python 3.8+ con las bibliotecas de IA requeridas
- **ONNX Runtime** (Opcional): Para inferencia de modelos ONNX
- **Ollama** (Opcional): Para servir modelos localmente
- **Herramientas de Aceleración de Hardware**: CUDA, OpenVINO o aceleradores específicos de la plataforma

### Configuración Inicial
1. **Activación de la Extensión**: Abre VS Code y verifica que AI Toolkit aparezca en la Barra de Actividades
2. **Configuración de Proveedores de Modelos**: Configura el acceso a GitHub, OpenAI, Anthropic u otros proveedores de modelos
3. **Entorno Local**: Configura el entorno Python e instala los paquetes requeridos
4. **Aceleración de Hardware**: Configura la aceleración por GPU/NPU si está disponible
5. **Integración MCP**: Configura servidores Model Context Protocol si es necesario

### Lista de Verificación para la Configuración Inicial
- [ ] Extensión AI Toolkit instalada y activada
- [ ] Catálogo de modelos accesible y modelos disponibles
- [ ] Playground funcional para pruebas de modelos
- [ ] Constructor de Agentes accesible para desarrollo de prompts
- [ ] Entorno de desarrollo local configurado
- [ ] Aceleración de hardware (si está disponible) configurada correctamente

## Comenzando con AI Toolkit

### Guía de Inicio Rápido

Recomendamos comenzar con modelos alojados por GitHub para una experiencia más simplificada:

1. **Instalación**: Sigue la [guía de instalación](https://code.visualstudio.com/docs/intelligentapps/overview#_install-and-setup) para configurar AI Toolkit en tu dispositivo
2. **Descubrimiento de Modelos**: Desde la vista del árbol de extensiones, selecciona **CATALOG > Models** para explorar los modelos disponibles
3. **Modelos de GitHub**: Comienza con modelos alojados por GitHub para una integración óptima
4. **Pruebas en Playground**: Desde cualquier tarjeta de modelo, selecciona **Try in Playground** para comenzar a experimentar con las capacidades del modelo

### Desarrollo de Edge AI Paso a Paso

#### Paso 1: Exploración y Selección de Modelos
1. Abre la vista de AI Toolkit en la Barra de Actividades de VS Code
2. Explora el Catálogo de Modelos para modelos adecuados para el despliegue en el borde
3. Filtra por proveedor (GitHub, ONNX, Ollama) según tus requisitos del borde
4. Usa **Try in Playground** para probar las capacidades del modelo inmediatamente

#### Paso 2: Desarrollo de Agentes
1. Usa el **Constructor de Prompts (Agentes)** para crear agentes de IA optimizados para el borde
2. Generar indicaciones iniciales utilizando descripciones en lenguaje natural  
3. Iterar y perfeccionar las indicaciones basándose en las respuestas del modelo  
4. Integrar herramientas MCP para mejorar las capacidades de los agentes  

#### Paso 3: Pruebas y Evaluación  
1. Utilizar **Bulk Run** para probar múltiples indicaciones en modelos seleccionados  
2. Ejecutar agentes con casos de prueba para validar la funcionalidad  
3. Evaluar precisión y rendimiento utilizando métricas integradas o personalizadas  
4. Comparar diferentes modelos y configuraciones  

#### Paso 4: Ajuste y Optimización  
1. Personalizar modelos para casos de uso específicos  
2. Aplicar ajustes específicos del dominio  
3. Optimizar para las limitaciones de implementación en el borde  
4. Versionar y comparar diferentes configuraciones de agentes  

#### Paso 5: Preparación para el Despliegue  
1. Generar código listo para producción utilizando el Agent Builder  
2. Configurar conexiones al servidor MCP para uso en producción  
3. Preparar paquetes de despliegue para dispositivos en el borde  
4. Configurar métricas de monitoreo y evaluación  

## Ejemplos para AI Toolkit  

Prueba Nuestros Ejemplos  
Los [ejemplos de AI Toolkit](https://github.com/Azure-Samples/AI_Toolkit_Samples) están diseñados para ayudar a desarrolladores e investigadores a explorar e implementar soluciones de IA de manera efectiva.  

Nuestros ejemplos incluyen:  

Código de Ejemplo: Ejemplos preconstruidos para demostrar funcionalidades de IA, como entrenamiento, despliegue o integración de modelos en aplicaciones.  
Documentación: Guías y tutoriales para ayudar a los usuarios a entender las características de AI Toolkit y cómo utilizarlas.  
Requisitos Previos  

- Visual Studio Code  
- AI Toolkit para Visual Studio Code  
- Token de acceso personal (PAT) de GitHub con permisos detallados  
- Foundry Local  

## Mejores Prácticas para el Desarrollo de IA en el Borde  

### Selección de Modelos  
- **Restricciones de Tamaño**: Elegir modelos que se ajusten a las limitaciones de memoria de los dispositivos objetivo  
- **Velocidad de Inferencia**: Priorizar modelos con tiempos de inferencia rápidos para aplicaciones en tiempo real  
- **Compromisos de Precisión**: Equilibrar la precisión del modelo con las limitaciones de recursos  
- **Compatibilidad de Formato**: Preferir formatos ONNX u optimizados para hardware en despliegues en el borde  

### Técnicas de Optimización  
- **Cuantización**: Utilizar cuantización INT8 o INT4 para reducir el tamaño del modelo y mejorar la velocidad  
- **Poda**: Eliminar parámetros innecesarios del modelo para reducir los requisitos computacionales  
- **Destilación de Conocimiento**: Crear modelos más pequeños que mantengan el rendimiento de los más grandes  
- **Aceleración por Hardware**: Aprovechar NPUs, GPUs o aceleradores especializados cuando estén disponibles  

### Flujo de Trabajo de Desarrollo  
- **Pruebas Iterativas**: Probar frecuentemente en condiciones similares al borde durante el desarrollo  
- **Monitoreo de Rendimiento**: Monitorear continuamente el uso de recursos y la velocidad de inferencia  
- **Control de Versiones**: Rastrear versiones de modelos y configuraciones de optimización  
- **Documentación**: Documentar todas las decisiones de optimización y los compromisos de rendimiento  

### Consideraciones para el Despliegue  
- **Monitoreo de Recursos**: Monitorear memoria, CPU y uso de energía en producción  
- **Estrategias de Respaldo**: Implementar mecanismos de respaldo para fallos del modelo  
- **Mecanismos de Actualización**: Planificar actualizaciones de modelos y gestión de versiones  
- **Seguridad**: Implementar medidas de seguridad adecuadas para aplicaciones de IA en el borde  

## Integración con Frameworks de IA en el Borde  

### ONNX Runtime  
- **Despliegue Multiplataforma**: Desplegar modelos ONNX en diferentes plataformas del borde  
- **Optimización de Hardware**: Aprovechar las optimizaciones específicas de hardware de ONNX Runtime  
- **Soporte Móvil**: Utilizar ONNX Runtime Mobile para aplicaciones en smartphones y tablets  
- **Integración IoT**: Desplegar en dispositivos IoT utilizando distribuciones ligeras de ONNX Runtime  

### Windows ML  
- **Dispositivos Windows**: Optimizar para dispositivos en el borde basados en Windows y PCs  
- **Aceleración NPU**: Aprovechar las Unidades de Procesamiento Neural en dispositivos Windows  
- **DirectML**: Utilizar DirectML para aceleración GPU en plataformas Windows  
- **Integración UWP**: Integrar con aplicaciones de la Plataforma Universal de Windows  

### TensorFlow Lite  
- **Optimización Móvil**: Desplegar modelos TensorFlow Lite en dispositivos móviles y embebidos  
- **Delegados de Hardware**: Utilizar delegados de hardware especializados para aceleración  
- **Microcontroladores**: Desplegar en microcontroladores utilizando TensorFlow Lite Micro  
- **Soporte Multiplataforma**: Desplegar en Android, iOS y sistemas Linux embebidos  

### Azure IoT Edge  
- **Híbrido Nube-Borde**: Combinar entrenamiento en la nube con inferencia en el borde  
- **Despliegue de Módulos**: Desplegar modelos de IA como módulos de IoT Edge  
- **Gestión de Dispositivos**: Gestionar dispositivos en el borde y actualizaciones de modelos de forma remota  
- **Telemetría**: Recopilar datos de rendimiento y métricas de modelos desde despliegues en el borde  

## Escenarios Avanzados de IA en el Borde  

### Despliegue Multimodelo  
- **Conjuntos de Modelos**: Desplegar múltiples modelos para mejorar la precisión o la redundancia  
- **Pruebas A/B**: Probar diferentes modelos simultáneamente en dispositivos del borde  
- **Selección Dinámica**: Elegir modelos basándose en las condiciones actuales del dispositivo  
- **Compartición de Recursos**: Optimizar el uso de recursos entre múltiples modelos desplegados  

### Aprendizaje Federado  
- **Entrenamiento Distribuido**: Entrenar modelos en múltiples dispositivos del borde  
- **Preservación de Privacidad**: Mantener los datos de entrenamiento locales mientras se comparten mejoras del modelo  
- **Aprendizaje Colaborativo**: Permitir que los dispositivos aprendan de experiencias colectivas  
- **Coordinación Borde-Nube**: Coordinar el aprendizaje entre dispositivos del borde y la infraestructura en la nube  

### Procesamiento en Tiempo Real  
- **Procesamiento de Flujos**: Procesar flujos continuos de datos en dispositivos del borde  
- **Inferencia de Baja Latencia**: Optimizar para una latencia mínima en la inferencia  
- **Procesamiento por Lotes**: Procesar eficientemente lotes de datos en dispositivos del borde  
- **Procesamiento Adaptativo**: Ajustar el procesamiento según las capacidades actuales del dispositivo  

## Solución de Problemas en el Desarrollo de IA en el Borde  

### Problemas Comunes  
- **Restricciones de Memoria**: El modelo es demasiado grande para la memoria del dispositivo objetivo  
- **Velocidad de Inferencia**: La inferencia del modelo es demasiado lenta para los requisitos en tiempo real  
- **Degradación de Precisión**: La optimización reduce la precisión del modelo de manera inaceptable  
- **Compatibilidad de Hardware**: El modelo no es compatible con el hardware objetivo  

### Estrategias de Depuración  
- **Perfilado de Rendimiento**: Utilizar las funciones de trazado de AI Toolkit para identificar cuellos de botella  
- **Monitoreo de Recursos**: Monitorear el uso de memoria y CPU durante el desarrollo  
- **Pruebas Incrementales**: Probar optimizaciones de manera incremental para aislar problemas  
- **Simulación de Hardware**: Utilizar herramientas de desarrollo para simular el hardware objetivo  

### Soluciones de Optimización  
- **Mayor Cuantización**: Aplicar técnicas de cuantización más agresivas  
- **Arquitectura del Modelo**: Considerar diferentes arquitecturas de modelos optimizadas para el borde  
- **Optimización de Preprocesamiento**: Optimizar el preprocesamiento de datos para las limitaciones del borde  
- **Optimización de Inferencia**: Utilizar optimizaciones específicas de hardware para la inferencia  

## Recursos y Próximos Pasos  

### Documentación Oficial  
- [Documentación para Desarrolladores de AI Toolkit](https://aka.ms/AIToolkit/doc)  
- [Guía de Instalación y Configuración](https://code.visualstudio.com/docs/intelligentapps/overview#_install-and-setup)  
- [Documentación de Aplicaciones Inteligentes en VS Code](https://code.visualstudio.com/docs/intelligentapps)  
- [Documentación del Protocolo de Contexto de Modelos (MCP)](https://modelcontextprotocol.io/)  

### Comunidad y Soporte  
- [Repositorio GitHub de AI Toolkit](https://github.com/microsoft/vscode-ai-toolkit)  
- [Problemas y Solicitudes de Funciones en GitHub](https://aka.ms/AIToolkit/feedback)  
- [Comunidad de Discord de Azure AI Foundry](https://aka.ms/azureaifoundry/discord)  
- [Marketplace de Extensiones de VS Code](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)  

### Recursos Técnicos  
- [Documentación de ONNX Runtime](https://onnxruntime.ai/)  
- [Documentación de Ollama](https://ollama.ai/)  
- [Documentación de Windows ML](https://docs.microsoft.com/en-us/windows/ai/)  
- [Documentación de Azure AI Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/)  

### Rutas de Aprendizaje  
- [Curso de Fundamentos de IA en el Borde](../Module01/README.md)  
- [Guía de Modelos de Lenguaje Pequeños](../Module02/README.md)  
- [Estrategias de Despliegue en el Borde](../Module03/README.md)  
- [Desarrollo de IA en el Borde para Windows](./windowdeveloper.md)  

### Recursos Adicionales  
- **Estadísticas del Repositorio**: Más de 1.8k estrellas, más de 150 forks, más de 18 colaboradores  
- **Licencia**: Licencia MIT  
- **Seguridad**: Se aplican las políticas de seguridad de Microsoft  
- **Telemetría**: Respeta la configuración de telemetría de VS Code  

## Conclusión  

AI Toolkit para Visual Studio Code representa una plataforma integral para el desarrollo moderno de IA, proporcionando capacidades de desarrollo de agentes simplificadas que son especialmente valiosas para aplicaciones de IA en el borde. Con su extenso catálogo de modelos que soporta proveedores como Anthropic, OpenAI, GitHub y Google, combinado con ejecución local a través de ONNX y Ollama, el toolkit ofrece la flexibilidad necesaria para diversos escenarios de despliegue en el borde.  

La fortaleza del toolkit radica en su enfoque integrado: desde el descubrimiento y experimentación de modelos en el Playground hasta el desarrollo sofisticado de agentes con el Prompt Builder, capacidades de evaluación completas e integración fluida de herramientas MCP. Para los desarrolladores de IA en el borde, esto significa prototipos rápidos y pruebas de agentes de IA antes del despliegue en el borde, con la capacidad de iterar rápidamente y optimizar para entornos con restricciones de recursos.  

Ventajas clave para el desarrollo de IA en el borde incluyen:  
- **Experimentación Rápida**: Probar modelos y agentes rápidamente antes de comprometerse con el despliegue en el borde  
- **Flexibilidad Multiproveedor**: Acceder a modelos de diversas fuentes para encontrar soluciones óptimas en el borde  
- **Desarrollo Local**: Probar con ONNX y Ollama para desarrollo offline y preservación de la privacidad  
- **Preparación para Producción**: Generar código listo para producción e integrar con herramientas externas a través de MCP  
- **Evaluación Integral**: Utilizar métricas integradas y personalizadas para validar el rendimiento de IA en el borde  

A medida que la IA continúa avanzando hacia escenarios de despliegue en el borde, AI Toolkit para VS Code proporciona el entorno de desarrollo y flujo de trabajo necesarios para construir, probar y optimizar aplicaciones inteligentes para entornos con restricciones de recursos. Ya sea que estés desarrollando soluciones IoT, aplicaciones de IA móvil o sistemas de inteligencia embebida, el conjunto de características completas y el flujo de trabajo integrado del toolkit apoyan todo el ciclo de vida del desarrollo de IA en el borde.  

Con desarrollo continuo y una comunidad activa (más de 1.8k estrellas en GitHub), AI Toolkit sigue estando a la vanguardia de las herramientas de desarrollo de IA, evolucionando constantemente para satisfacer las necesidades de los desarrolladores modernos de IA que construyen para escenarios de despliegue en el borde.  

[Next Foundry Local](./foundrylocal.md)  

---

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que surjan del uso de esta traducción.
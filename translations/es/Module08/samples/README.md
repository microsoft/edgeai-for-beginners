# Módulo 08 Ejemplos: Guía de Desarrollo Local de Foundry

## Resumen

Esta colección completa demuestra tanto los enfoques de **Foundry Local SDK** como de **Comandos Shell** para construir aplicaciones de IA listas para producción. Cada ejemplo muestra diferentes aspectos del desarrollo de IA en el borde, desde la integración básica con REST hasta sistemas avanzados de múltiples agentes.

## Enfoque de Desarrollo: SDK vs Comandos Shell

### Usa Foundry Local SDK Cuando:

- **Control Programático**: Necesitas control total sobre el ciclo de vida de los agentes, la evaluación o los flujos de trabajo de implementación.
- **Herramientas Personalizadas**: Construir automatización alrededor de Foundry Local (integración CI/CD, orquestación de múltiples agentes).
- **Acceso Detallado**: Requiriendo metadatos detallados de los agentes, control de versiones o control del evaluador de rendimiento.
- **Integración con Python**: Trabajando en entornos centrados en Python o integrando la lógica de Foundry en aplicaciones más amplias.
- **Flujos de Trabajo Empresariales**: Implementar flujos de trabajo modulares y pipelines de evaluación reproducibles alineados con arquitecturas de referencia de Microsoft.

### Usa Comandos Shell Cuando:

- **Pruebas Rápidas**: Realizar pruebas locales rápidas, lanzamientos manuales de agentes o verificación de configuraciones.
- **Simplicidad CLI**: Necesitas operaciones CLI sencillas para iniciar/detener agentes, revisar registros o realizar evaluaciones básicas.
- **Automatización Ligera**: Escribir scripts de automatización simples sin requerir integración completa con el SDK.
- **Iteración Rápida**: Ciclos de depuración y desarrollo, especialmente en entornos restringidos o implementaciones a nivel de grupos de recursos.
- **Configuración y Validación**: Tareas iniciales de configuración del entorno y verificación rápida.

## Mejores Prácticas y Flujo de Trabajo Recomendado

Basado en la gestión del ciclo de vida de los agentes, el seguimiento de dependencias y los principios de reproducibilidad con privilegios mínimos:

### Fase 1: Fundamentos y Configuración
1. **Comienza con Comandos Shell** para la configuración inicial y validación rápida.
2. **Verifica el Entorno** utilizando herramientas CLI y despliegue básico de modelos.
3. **Prueba la Conectividad** con llamadas REST simples y verificaciones de estado.

### Fase 2: Desarrollo e Integración
1. **Transición al SDK** para flujos de trabajo escalables y trazables.
2. **Implementa Control Programático** para interacciones complejas entre agentes.
3. **Construye Herramientas Personalizadas** para plantillas listas para la comunidad e integración con Azure OpenAI.

### Fase 3: Producción y Escalabilidad
1. **Enfoque Híbrido** combinando CLI para operaciones y SDK para lógica de aplicaciones.
2. **Integración Empresarial** con monitoreo, registro y pipelines de implementación.
3. **Contribución Comunitaria** mediante plantillas reutilizables y mejores prácticas.

---

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por garantizar la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse como la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que puedan surgir del uso de esta traducción.
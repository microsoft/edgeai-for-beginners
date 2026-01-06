<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "aa775a734bda4590ecbe3a94a3b62197",
  "translation_date": "2026-01-05T17:21:51+00:00",
  "source_file": "WorkshopForAgentic/translation/zh-cn/README.md",
  "language_code": "es"
}
-->
# 🎙️ Taller del Estudio de Podcast AI

![logo](../../../../../translated_images/logo.8711e39dc8257d7b.es.png)

## Tu misión

¡Bienvenido al **Estudio de Podcast AI**! Estás a punto de lanzar tu propio podcast tecnológico llamado "Future Bytes" — pero aquí hay un giro: construirás un equipo de producción impulsado por IA para ayudarte a crearlo. No más investigación interminable, redacción de guiones y edición de audio. En cambio, te convertirás en un productor de podcasts con súper poderes de IA mediante programación.

## Historia de fondo

Imagina: tú y tus amigos quieren iniciar un podcast sobre las tendencias tecnológicas más interesantes, pero todos están ocupados con estudios, trabajo o la vida. ¿Qué pasaría si pudieras construir un equipo de agentes de IA para hacer el trabajo pesado? Un agente se encarga de investigar temas, otro escribe guiones atractivos, y un tercero convierte el texto en conversaciones naturales y fluidas. ¿Suena a ciencia ficción? Hagámoslo realidad.

## Qué aprenderás

Al final de este taller, sabrás cómo:
- 🤖 Desplegar tus propios modelos de IA locales (¡sin costo de API, ni dependencia en la nube!)
- 🔧 Construir agentes de IA profesionales que colaboran en el mundo real
- 🎬 Crear un flujo de producción completo de podcast, desde la idea hasta el audio

## Tu viaje: un drama en tres actos

Como en cualquier buena historia, tenemos tres actos. Cada acto construye paso a paso tu Estudio de Podcast AI:

| Capítulo | Tu tarea | Qué sucede | Habilidades desbloqueadas |
|---------|-----------|--------------|----------------|
| **Primer acto** | [Conoce a tu asistente de IA](01.BuildAIAgentWithSLM.md) | Descubrirás cómo crear agentes de IA que pueden chatear, buscar en la web e incluso resolver problemas. Piensa en ellos como becarios investigadores que nunca duermen. | 🎯 Construye tu primer agente<br>🛠️ Dale súper poderes (¡herramientas!)<br>🧠 Enséñale a pensar<br>🌐 Conéctalo a internet |
| **Segundo acto** | [Forma tu equipo de producción](02.AIAgentOrchestrationAndWorkflows.md) | Ahora se pone interesante: orquestarás varios agentes de IA para que trabajen juntos como un verdadero equipo de podcast. Uno investiga, otro escribe, tú apruebas—el trabajo en equipo hace que los sueños se cumplan. | 🎭 Coordina múltiples agentes<br>🔄 Construye flujos de aprobación<br>🖥️ Usa la interfaz DevUI para pruebas<br>✋ Mantén el control humano |
| **Tercer acto** | [Trae tu podcast a la vida](03.Multi-SpeakerPodcastGenerationWithVibeVoice.md) | Gran final: convierte tus guiones de texto en audio real de podcast con voces realistas y diálogo natural. ¡Tu podcast “Future Bytes” está listo para publicarse! | 🎤 Magia de texto a voz<br>👥 Voces de múltiples hablantes<br>⏱️ Audio de formato largo<br>🚀 Totalmente automatizado |

Cada acto desbloquea nuevas habilidades. Si eres valiente, puedes saltar entre ellos, pero recomendamos seguir el orden.

## Requisitos del entorno

Este taller soporta diversos entornos de hardware:
- **CPU**: adecuado para pruebas y uso a pequeña escala
- **GPU**: recomendado para producción, mejora significativamente la velocidad de inferencia
- **NPU**: soporte para aceleración con unidades neuronales de próxima generación

## Qué necesitas

### Lista de software ✅
- **Python 3.10+** (tu lenguaje de programación)
- **Ollama** (para ejecutar modelos de IA en tu máquina)
- **VS Code** (tu editor de código)
- **Extensión de Python** (para hacer VS Code más inteligente)
- **Git** (para obtener el código)

### Revisión de hardware 💻
- **¿Puedo ejecutar esto?**: 8 GB de RAM, 10 GB de espacio disponible (funciona pero puede ser lento)
- **Configuración ideal**: 16 GB+ de RAM, una buena GPU (¡funciona sin problemas!)
- **¿Tienes NPU?**: ¡Mucho mejor! Desbloquea rendimiento de próxima generación 🚀

## Construye tu estudio 🎬

### Paso 1: Actualiza Python

Asegúrate de tener Python 3.10 o superior:

```bash
python --version
# Debe mostrar Python 3.10.x o una versión superior
```

¿No tienes Python? Consíguelo en [python.org](https://python.org) — ¡es gratis!

### Paso 2: Obtén Ollama (tu motor para modelos de IA)

Visita [ollama.ai](https://ollama.ai) para descargar Ollama según tu sistema operativo. Piénsalo como el motor que ejecuta IA localmente.

Verifica que esté listo:

```bash
ollama --version
```

### Paso 3: Descarga tu cerebro de IA 🧠

Hora de obtener el modelo Qwen-3-8B (como contratar a tu primer asistente de IA):

```bash
ollama pull qwen3:8b
```

*Esto puede tomar algunos minutos. ¡Tiempo perfecto para un café! ☕*

### Paso 4: Configura VS Code

Si aún no lo tienes, instala [Visual Studio Code](https://code.visualstudio.com/). Es el mejor editor de código (y punto 😄).

### Paso 5: Extensión de Python

En VS Code:
1. Presiona `Ctrl+Shift+X` (o `Cmd+Shift+X` en Mac)
2. Busca "Python"
3. Instala la extensión oficial de Python de Microsoft

### Paso 6: ¡Ya casi! 🎉

De verdad, estás listo. ¡Vamos a crear algo de magia con IA!

### Paso 7: Instala Microsoft Agent Framework y paquetes relacionados 📦

Instala todas las dependencias necesarias para el taller:

```bash
pip install -r ./Installations/requirements.txt -U
```

*Esto instalará Microsoft Agent Framework y todos los paquetes necesarios. Tómate un café — ¡la primera instalación puede demorar un poco! ☕*

## Instrucciones del taller

La estructura detallada del proyecto, pasos de configuración y ejecución se irán explicando durante el taller.

## Solución de problemas (cuando las cosas salen mal) 🔧

### "¡Ay, la descarga del modelo es muy lenta!"
**Solución**: Usa una VPN o configura un espejo para Ollama. A veces la red no acompaña.

### "¡Mi computadora está a punto de colapsar! ¡No hay suficiente memoria!"
**Solución**: Cambia a un modelo más pequeño o ajusta el parámetro `num_ctx` para usar menos memoria. Piénsalo como poner a tu IA a dieta.

### "¿Puedo usar GPU para acelerar?"
**Solución**: ¡Ollama detecta automáticamente la GPU! Solo asegúrate de que el driver esté actualizado. ¡Aceleración gratis! 🏎️

## Recursos adicionales (para los curiosos) 📚

- [Documentación de Ollama](https://github.com/ollama/ollama) — profundiza en modelos de IA local
- [Microsoft Agent Framework](https://microsoft.github.io/autogen/) — aprende más sobre construir equipos de agentes
- [Información del modelo Qwen](https://qwenlm.github.io/) — conoce el cerebro de tu asistente de IA

## Licencia

Licencia MIT — ¡Crea cosas geniales, compártelas y haz el mundo mejor! 🌍

## ¿Quieres contribuir?

¿Encontraste un bug? ¿Tienes ideas? ¡Abre un Issue o PR! Nos encanta la comunidad. ✨

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda la traducción profesional realizada por un humano. No nos hacemos responsables de cualquier malentendido o interpretación errónea derivada del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
# Sesión 6 Ejemplo: Modelos como Herramientas

Este ejemplo implementa un router mínimo + registro de herramientas que selecciona un modelo basado en el mensaje del usuario y llama al endpoint compatible con OpenAI de Foundry Local.

## Archivos
- `router.py`: registro simple y enrutamiento heurístico; descubrimiento de endpoints + verificación de estado.

## Ejecutar (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
REM Start whatever models you plan to route to
foundry model run phi-4-mini
foundry model run qwen2.5-7b
foundry model run deepseek-r1-7b

python samples\06\router.py "Explain how local-first AI improves privacy in two sentences."
```

## Notas
- El router utiliza heurísticas simples de palabras clave para elegir entre las herramientas `general`, `reasoning` y `code`, y muestra `/v1/models` al iniciar.
- Configuración mediante variables de entorno:
```cmd
set BASE_URL=http://localhost:8000
set API_KEY=
REM Override models per tool
set GENERAL_MODEL=phi-4-mini
set REASONING_MODEL=deepseek-r1-7b
set CODE_MODEL=qwen2.5-7b
REM Or provide a full JSON registry
set TOOL_REGISTRY={"general":{"model":"phi-4-mini"},"reasoning":{"model":"deepseek-r1-7b"},"code":{"model":"qwen2.5-7b"}}
```

## Referencias
- Foundry Local (Aprender): https://learn.microsoft.com/azure/ai-foundry/foundry-local/
- Integración con SDKs de inferencia: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

---

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por garantizar la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse como la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que puedan surgir del uso de esta traducción.
# Session 6 Eksempel: Modeller som Værktøjer

Dette eksempel implementerer en minimal router + værktøjsregister, der vælger en model baseret på brugerens prompt og kalder Foundry Locals OpenAI-kompatible endpoint.

## Filer
- `router.py`: simpelt register og heuristisk routing; endpoint-opdagelse + sundhedstjek.

## Kør (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
REM Start whatever models you plan to route to
foundry model run phi-4-mini
foundry model run qwen2.5-7b
foundry model run deepseek-r1-7b

python samples\06\router.py "Explain how local-first AI improves privacy in two sentences."
```

## Noter
- Routeren bruger simple nøgleord-heuristikker til at vælge mellem `general`, `reasoning` og `code` værktøjer og udskriver `/v1/models` ved start.
- Konfigurer via miljøvariabler:
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

## Referencer
- Foundry Local (Lær): https://learn.microsoft.com/azure/ai-foundry/foundry-local/
- Integration med inferens-SDK'er: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

---

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal det bemærkes, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os ikke ansvar for misforståelser eller fejltolkninger, der måtte opstå som følge af brugen af denne oversættelse.
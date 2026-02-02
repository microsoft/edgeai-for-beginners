# Sesjon 6 Eksempel: Modeller som Verktøy

Dette eksemplet implementerer en minimal router + verktøyregister som velger en modell basert på brukerens forespørsel og kaller Foundry Locals OpenAI-kompatible endepunkt.

## Filer
- `router.py`: enkelt register og heuristisk ruting; endepunktoppdagelse + helsesjekk.

## Kjør (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
REM Start whatever models you plan to route to
foundry model run phi-4-mini
foundry model run qwen2.5-7b
foundry model run deepseek-r1-7b

python samples\06\router.py "Explain how local-first AI improves privacy in two sentences."
```

## Notater
- Routeren bruker enkle nøkkelordheuristikker for å velge mellom `general`, `reasoning` og `code` verktøy og skriver ut `/v1/models` ved oppstart.
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

## Referanser
- Foundry Local (Lær): https://learn.microsoft.com/azure/ai-foundry/foundry-local/
- Integrer med inferens-SDKer: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

---

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi tilstreber nøyaktighet, vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
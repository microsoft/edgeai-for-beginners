# Session 6 Exempel: Modeller som Verktyg

Det här exemplet implementerar en minimal router + verktygsregister som väljer en modell baserat på användarens prompt och anropar Foundry Locals OpenAI-kompatibla endpoint.

## Filer
- `router.py`: enkelt register och heuristisk routing; endpoint-upptäckt + hälsokontroll.

## Kör (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
REM Start whatever models you plan to route to
foundry model run phi-4-mini
foundry model run qwen2.5-7b
foundry model run deepseek-r1-7b

python samples\06\router.py "Explain how local-first AI improves privacy in two sentences."
```

## Anteckningar
- Routern använder enkla nyckelordsheuristik för att välja mellan `general`, `reasoning` och `code` verktyg och skriver ut `/v1/models` vid start.
- Konfigurera via miljövariabler:
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

## Referenser
- Foundry Local (Lär dig mer): https://learn.microsoft.com/azure/ai-foundry/foundry-local/
- Integrera med inferens-SDK: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

---

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, bör det noteras att automatiska översättningar kan innehålla fel eller felaktigheter. Det ursprungliga dokumentet på dess originalspråk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.
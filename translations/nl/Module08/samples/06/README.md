# Sessie 6 Voorbeeld: Modellen als Hulpmiddelen

Dit voorbeeld implementeert een minimale router + toolregister die een model selecteert op basis van de gebruikersprompt en een oproep doet naar Foundry Local's OpenAI-compatibele endpoint.

## Bestanden
- `router.py`: eenvoudig register en heuristische routering; endpointdetectie + gezondheidscontrole.

## Uitvoeren (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
REM Start whatever models you plan to route to
foundry model run phi-4-mini
foundry model run qwen2.5-7b
foundry model run deepseek-r1-7b

python samples\06\router.py "Explain how local-first AI improves privacy in two sentences."
```

## Opmerkingen
- De router gebruikt eenvoudige trefwoordheuristieken om te kiezen tussen `general`, `reasoning` en `code` tools en print `/v1/models` bij het starten.
- Configureren via omgevingsvariabelen:
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

## Referenties
- Foundry Local (Leer): https://learn.microsoft.com/azure/ai-foundry/foundry-local/
- Integreren met inference SDKs: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

---

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
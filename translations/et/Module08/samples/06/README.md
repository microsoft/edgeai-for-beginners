# Sessioon 6 Näidis: Mudelid tööriistadena

See näidis rakendab minimaalset ruuterit + tööriistade registrit, mis valib mudeli kasutaja päringu põhjal ja kutsub Foundry Locali OpenAI-ga ühilduvat lõpp-punkti.

## Failid
- `router.py`: lihtne register ja heuristiline ruutimine; lõpp-punkti avastamine + tervisekontroll.

## Käivitamine (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
REM Start whatever models you plan to route to
foundry model run phi-4-mini
foundry model run qwen2.5-7b
foundry model run deepseek-r1-7b

python samples\06\router.py "Explain how local-first AI improves privacy in two sentences."
```

## Märkused
- Ruuter kasutab lihtsaid märksõna heuristikaid, et valida `general`, `reasoning` ja `code` tööriistade vahel ning prindib käivitamisel `/v1/models`.
- Konfigureerimine keskkonnamuutujate kaudu:
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

## Viited
- Foundry Local (Õpi): https://learn.microsoft.com/azure/ai-foundry/foundry-local/
- Integreerimine järeldus-SDK-dega: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

---

**Lahtiütlus**:  
See dokument on tõlgitud, kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi püüame tagada täpsust, palun arvestage, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks lugeda autoriteetseks allikaks. Olulise teabe puhul on soovitatav kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valede tõlgenduste eest.
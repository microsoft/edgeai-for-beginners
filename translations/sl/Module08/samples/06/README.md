# Vzorec seje 6: Modeli kot orodja

Ta vzorec implementira minimalni usmerjevalnik + register orodij, ki izbere model glede na uporabniški poziv in pokliče OpenAI-kompatibilno končno točko Foundry Local.

## Datoteke
- `router.py`: preprost register in usmerjanje na podlagi heuristike; odkrivanje končnih točk + preverjanje stanja.

## Zagon (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
REM Start whatever models you plan to route to
foundry model run phi-4-mini
foundry model run qwen2.5-7b
foundry model run deepseek-r1-7b

python samples\06\router.py "Explain how local-first AI improves privacy in two sentences."
```

## Opombe
- Usmerjevalnik uporablja preproste ključne besede za izbiro med orodji `general`, `reasoning` in `code` ter ob zagonu izpiše `/v1/models`.
- Konfiguracija prek okoljskih spremenljivk:
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

## Reference
- Foundry Local (Učenje): https://learn.microsoft.com/azure/ai-foundry/foundry-local/
- Integracija z SDK-ji za sklepanje: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

---

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve AI za prevajanje [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne odgovarjamo za morebitna nesporazumevanja ali napačne razlage, ki izhajajo iz uporabe tega prevoda.
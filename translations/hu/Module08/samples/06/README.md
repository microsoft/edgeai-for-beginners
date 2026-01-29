# 6. munkamenet minta: Modellek mint eszközök

Ez a minta egy minimális routert és eszközregisztert valósít meg, amely a felhasználói kérés alapján kiválaszt egy modellt, és meghívja a Foundry Local OpenAI-kompatibilis végpontját.

## Fájlok
- `router.py`: egyszerű regiszter és heurisztikus útválasztás; végpont felfedezése + állapotellenőrzés.

## Futtatás (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
REM Start whatever models you plan to route to
foundry model run phi-4-mini
foundry model run qwen2.5-7b
foundry model run deepseek-r1-7b

python samples\06\router.py "Explain how local-first AI improves privacy in two sentences."
```

## Megjegyzések
- A router egyszerű kulcsszó-heurisztikát használ, hogy válasszon a `general`, `reasoning` és `code` eszközök között, és a `/v1/models`-t nyomtatja ki indításkor.
- Konfigurálás környezeti változókon keresztül:
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

## Hivatkozások
- Foundry Local (Tanulás): https://learn.microsoft.com/azure/ai-foundry/foundry-local/
- Integráció inference SDK-kkal: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

---

**Felelősség kizárása**:  
Ez a dokumentum az [Co-op Translator](https://github.com/Azure/co-op-translator) AI fordítási szolgáltatás segítségével került lefordításra. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt professzionális emberi fordítást igénybe venni. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely a fordítás használatából eredhet.
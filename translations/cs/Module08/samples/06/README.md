# Ukázka ze 6. lekce: Modely jako nástroje

Tato ukázka implementuje minimální router + registr nástrojů, který vybírá model na základě uživatelského dotazu a volá OpenAI-kompatibilní endpoint Foundry Local.

## Soubory
- `router.py`: jednoduchý registr a heuristické směrování; zjišťování endpointů + kontrola stavu.

## Spuštění (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
REM Start whatever models you plan to route to
foundry model run phi-4-mini
foundry model run qwen2.5-7b
foundry model run deepseek-r1-7b

python samples\06\router.py "Explain how local-first AI improves privacy in two sentences."
```

## Poznámky
- Router používá jednoduché heuristiky na základě klíčových slov k výběru mezi nástroji `general`, `reasoning` a `code` a při spuštění vypisuje `/v1/models`.
- Konfigurace prostřednictvím proměnných prostředí:
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

## Odkazy
- Foundry Local (Learn): https://learn.microsoft.com/azure/ai-foundry/foundry-local/
- Integrace s inference SDKs: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

---

**Prohlášení**:  
Tento dokument byl přeložen pomocí služby AI pro překlad [Co-op Translator](https://github.com/Azure/co-op-translator). I když se snažíme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nenese odpovědnost za žádná nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.
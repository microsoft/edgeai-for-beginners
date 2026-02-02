# 6 sesijos pavyzdys: Modeliai kaip įrankiai

Šiame pavyzdyje įgyvendinamas minimalus maršrutizatorius + įrankių registras, kuris parenka modelį pagal vartotojo užklausą ir naudoja Foundry Local OpenAI suderinamą galinį tašką.

## Failai
- `router.py`: paprastas registras ir euristinis maršrutizavimas; galinio taško aptikimas + sveikatos patikrinimas.

## Paleidimas (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
REM Start whatever models you plan to route to
foundry model run phi-4-mini
foundry model run qwen2.5-7b
foundry model run deepseek-r1-7b

python samples\06\router.py "Explain how local-first AI improves privacy in two sentences."
```

## Pastabos
- Maršrutizatorius naudoja paprastas raktinių žodžių euristikas, kad pasirinktų tarp `general`, `reasoning` ir `code` įrankių, ir paleidimo metu atspausdina `/v1/models`.
- Konfigūruojama per aplinkos kintamuosius:
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

## Nuorodos
- Foundry Local (Sužinokite): https://learn.microsoft.com/azure/ai-foundry/foundry-local/
- Integracija su inferencijos SDK: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

---

**Atsakomybės atsisakymas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama profesionali žmogaus vertimo paslauga. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius dėl šio vertimo naudojimo.
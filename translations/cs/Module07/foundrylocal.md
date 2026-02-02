# Foundry Local na Windows a Mac

Tento průvodce vám pomůže nainstalovat, spustit a integrovat Microsoft Foundry Local na Windows a Mac. Všechny kroky a příkazy jsou ověřeny podle dokumentace Microsoft Learn.

- Začínáme: https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started
- Architektura: https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture
- Referenční příručka CLI: https://learn.microsoft.com/azure/ai-foundry/foundry-local/reference/reference-cli
- Integrace SDK: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks
- Kompilace HF modelů (BYOM): https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models
- Windows AI: Lokální vs cloud: https://learn.microsoft.com/windows/ai/cloud-ai#key-decision-factors-for-app-developers

## 1) Instalace / Aktualizace na Windows

- Instalace:
```cmd
winget install Microsoft.FoundryLocal
```
- Aktualizace:
```cmd
winget upgrade --id Microsoft.FoundryLocal
```
- Kontrola verze:
```cmd
foundry --version
```
     
**Instalace / Mac**

**MacOS**: 
Otevřete terminál a spusťte následující příkaz:
```bash
   brew tap microsoft/foundrylocal
   brew install foundrylocal
```

## 2) Základy CLI (Tři kategorie)

- Model:
```cmd
foundry model --help
foundry model list
foundry model run gpt-oss-20b
```
- Služba:
```cmd
foundry service --help
foundry service status
foundry service ps
```
- Cache:
```cmd
foundry cache --help
foundry cache list
```

Poznámky:
- Služba poskytuje REST API kompatibilní s OpenAI. Port koncového bodu je dynamicky přidělen; použijte `foundry service status` pro jeho zjištění.
- Pro pohodlí použijte SDK; automaticky zajišťují zjištění koncového bodu, kde je to podporováno.

## 3) Zjištění lokálního koncového bodu (Dynamický port)

Foundry Local při každém spuštění služby přiděluje dynamický port:
```cmd
foundry service status
```
Použijte hlášený `http://localhost:<PORT>` jako svůj `base_url` s cestami kompatibilními s OpenAI (například `/v1/chat/completions`).

## 4) Rychlý test pomocí OpenAI Python SDK

```cmd
set BASE_URL=http://localhost:PORT
python - <<PY
from openai import OpenAI
client = OpenAI(base_url="%BASE_URL%/v1", api_key="")
resp = client.chat.completions.create(
    model="gpt-oss-20b",
    messages=[{"role":"user","content":"Say hello from Foundry Local."}],
    max_tokens=64,
)
print(resp.choices[0].message.content)
PY
```
Reference:
- Integrace SDK: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

## 5) Vlastní model (Kompilace pomocí Olive)

Pokud potřebujete model, který není v katalogu, zkompilujte jej do ONNX pro Foundry Local pomocí Olive.

Vysoká úroveň procesu (podrobné kroky viz dokumentace):
```cmd
foundry cache cd models
foundry cache list
foundry model run llama-3.2 --verbose
```
Dokumentace:
- Kompilace BYOM: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models

## 6) Řešení problémů

- Kontrola stavu služby a logů:
```cmd
foundry service status
foundry service diag
```
- Vymazání nebo přesun cache:
```cmd
foundry cache list
foundry cache remove <model>
foundry cache cd <path>
```
- Aktualizace na nejnovější preview:
```cmd
winget upgrade --id Microsoft.FoundryLocal
```

## 7) Související zkušenosti vývojářů na Windows

- Možnosti lokální vs cloudové AI na Windows, včetně Foundry Local a Windows ML:
  https://learn.microsoft.com/windows/ai/cloud-ai#key-decision-factors-for-app-developers
- AI Toolkit pro VS Code s Foundry Local (použijte `foundry service status` pro získání URL koncového bodu pro chat):
  https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture#key-components

[Další vývojář na Windows](./windowdeveloper.md)

---

**Prohlášení**:  
Tento dokument byl přeložen pomocí služby pro automatický překlad [Co-op Translator](https://github.com/Azure/co-op-translator). I když se snažíme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za autoritativní zdroj. Pro důležité informace doporučujeme profesionální lidský překlad. Neodpovídáme za žádná nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.
<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ba4a0e432e3b6bfed9026383b0b56cf4",
  "translation_date": "2025-11-11T17:56:10+00:00",
  "source_file": "Module07/foundrylocal.md",
  "language_code": "pcm"
}
-->
# Foundry Local for Windows & Mac

Dis guide go show you how you fit install, run, and connect Microsoft Foundry Local for Windows and Mac. All di steps and commands don dey confirm with Microsoft Learn docs.

- Start Here: https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started
- Architecture: https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture
- CLI Reference: https://learn.microsoft.com/azure/ai-foundry/foundry-local/reference/reference-cli
- Connect SDKs: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks
- Compile HF Models (BYOM): https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models
- Windows AI: Local vs Cloud: https://learn.microsoft.com/windows/ai/cloud-ai#key-decision-factors-for-app-developers

## 1) Install / Upgrade for Windows

- Install:
```cmd
winget install Microsoft.FoundryLocal
```
- Upgrade:
```cmd
winget upgrade --id Microsoft.FoundryLocal
```
- Check Version:
```cmd
foundry --version
```
     
**Install / Mac**

**MacOS**: 
Open terminal, run dis command:
```bash
   brew tap microsoft/foundrylocal
   brew install foundrylocal
```

## 2) CLI Basics (Three Categories)

- Model:
```cmd
foundry model --help
foundry model list
foundry model run gpt-oss-20b
```
- Service:
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

Notes:
- Di service dey expose OpenAI-compatible REST API. Di endpoint port dey change every time; use `foundry service status` to find am.
- Use di SDKs for easy work; dem go find di endpoint automatically if e dey supported.

## 3) Find di Local Endpoint (Dynamic Port)

Foundry Local go give dynamic port anytime di service start:
```cmd
foundry service status
```
Use di `http://localhost:<PORT>` wey dem show as your `base_url` with OpenAI-compatible paths (like `/v1/chat/completions`).

## 4) Quick Test with OpenAI Python SDK

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
References:
- SDK Integration: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

## 5) Bring Your Own Model (Compile with Olive)

If you need model wey no dey di catalog, compile am to ONNX for Foundry Local with Olive.

High-level flow (check docs for steps):
```cmd
foundry cache cd models
foundry cache list
foundry model run llama-3.2 --verbose
```
Docs:
- BYOM compile: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models

## 6) Troubleshooting

- Check service status and logs:
```cmd
foundry service status
foundry service diag
```
- Clear or move cache:
```cmd
foundry cache list
foundry cache remove <model>
foundry cache cd <path>
```
- Update to latest preview:
```cmd
winget upgrade --id Microsoft.FoundryLocal
```

## 7) Related Windows Developer Experience

- Windows local vs cloud AI choices, including Foundry Local and Windows ML:
  https://learn.microsoft.com/windows/ai/cloud-ai#key-decision-factors-for-app-developers
- VS Code AI Toolkit with Foundry Local (use `foundry service status` to get di chat endpoint URL):
  https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture#key-components

[Next Windows Developer](./windowdeveloper.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis dokyument don use AI transle-shun service [Co-op Translator](https://github.com/Azure/co-op-translator) do di transle-shun. Even as we dey try make am correct, abeg make you sabi say machine transle-shun fit get mistake or no dey accurate well. Di original dokyument wey dey for im native language na di one wey you go take as di correct source. For important mata, e good make you use professional human transle-shun. We no go fit take blame for any misunderstanding or wrong interpretation wey fit happen because you use dis transle-shun.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
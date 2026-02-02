# Foundry Local on Windows & Mac

This guide provides instructions for installing, running, and integrating Microsoft Foundry Local on Windows and Mac. All steps and commands have been verified against Microsoft Learn documentation.

- Get Started: https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started
- Architecture: https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture
- CLI Reference: https://learn.microsoft.com/azure/ai-foundry/foundry-local/reference/reference-cli
- Integrate SDKs: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks
- Compile HF Models (BYOM): https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models
- Windows AI: Local vs Cloud: https://learn.microsoft.com/windows/ai/cloud-ai#key-decision-factors-for-app-developers

## 1) Install / Upgrade on Windows

- Install:
```cmd
winget install Microsoft.FoundryLocal
```

- Upgrade:
```cmd
winget upgrade --id Microsoft.FoundryLocal
```

- Version check:
```cmd
foundry --version
```
     

**Install / Mac**

**MacOS**: 
Open a terminal and execute the following command:
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
- The service provides an OpenAI-compatible REST API. The endpoint port is dynamically assigned; use `foundry service status` to identify it.
- SDKs are recommended for ease of use; they automatically handle endpoint discovery where supported.

## 3) Discover the Local Endpoint (Dynamic Port)

Foundry Local assigns a dynamic port each time the service starts:
```cmd
foundry service status
```

Use the reported `http://localhost:<PORT>` as your `base_url` with OpenAI-compatible paths (e.g., `/v1/chat/completions`).

## 4) Quick Test via OpenAI Python SDK

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

If you need a model that is not available in the catalog, you can compile it to ONNX for Foundry Local using Olive.

High-level process (refer to documentation for detailed steps):
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

- Update to the latest preview:
```cmd
winget upgrade --id Microsoft.FoundryLocal
```


## 7) Related Windows Developer Experience

- Windows local vs cloud AI options, including Foundry Local and Windows ML:
  https://learn.microsoft.com/windows/ai/cloud-ai#key-decision-factors-for-app-developers
- VS Code AI Toolkit with Foundry Local (use `foundry service status` to retrieve the chat endpoint URL):
  https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture#key-components

[Next Windows Developer](./windowdeveloper.md)

---

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we aim for accuracy, please note that automated translations may contain errors or inaccuracies. The original document in its native language should be regarded as the authoritative source. For critical information, professional human translation is recommended. We are not responsible for any misunderstandings or misinterpretations resulting from the use of this translation.
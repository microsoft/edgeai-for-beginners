# Foundry Local sa Windows at Mac

Ang gabay na ito ay tumutulong sa iyo na mag-install, magpatakbo, at mag-integrate ng Microsoft Foundry Local sa Windows at Mac. Ang lahat ng mga hakbang at utos ay na-validate batay sa Microsoft Learn docs.

- Magsimula: https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started
- Arkitektura: https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture
- CLI Reference: https://learn.microsoft.com/azure/ai-foundry/foundry-local/reference/reference-cli
- Integrate SDKs: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks
- I-compile ang HF Models (BYOM): https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models
- Windows AI: Lokal vs Cloud: https://learn.microsoft.com/windows/ai/cloud-ai#key-decision-factors-for-app-developers

## 1) Mag-install / Mag-upgrade sa Windows

- Mag-install:
```cmd
winget install Microsoft.FoundryLocal
```
- Mag-upgrade:
```cmd
winget upgrade --id Microsoft.FoundryLocal
```
- Suriin ang bersyon:
```cmd
foundry --version
```
     
**Mag-install / Mac**

**MacOS**: 
Magbukas ng terminal at patakbuhin ang sumusunod na utos:
```bash
   brew tap microsoft/foundrylocal
   brew install foundrylocal
```

## 2) Mga Pangunahing Kaalaman sa CLI (Tatlong Kategorya)

- Model:
```cmd
foundry model --help
foundry model list
foundry model run gpt-oss-20b
```
- Serbisyo:
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

Mga Tala:
- Ang serbisyo ay nagbibigay ng OpenAI-compatible REST API. Ang port ng endpoint ay dynamic na itinalaga; gamitin ang `foundry service status` para matuklasan ito.
- Gamitin ang SDKs para sa kaginhawaan; awtomatikong hinahandle nila ang endpoint discovery kung saan suportado.

## 3) Tuklasin ang Lokal na Endpoint (Dynamic Port)

Ang Foundry Local ay nag-aassign ng dynamic na port tuwing nagsisimula ang serbisyo:
```cmd
foundry service status
```
Gamitin ang iniulat na `http://localhost:<PORT>` bilang iyong `base_url` na may OpenAI-compatible paths (halimbawa, `/v1/chat/completions`).

## 4) Mabilisang Pagsubok gamit ang OpenAI Python SDK

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
Mga Sanggunian:
- SDK Integration: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

## 5) Magdala ng Sariling Modelo (I-compile gamit ang Olive)

Kung kailangan mo ng modelong wala sa catalog, i-compile ito sa ONNX para sa Foundry Local gamit ang Olive.

Pangkalahatang daloy (tingnan ang docs para sa mga hakbang):
```cmd
foundry cache cd models
foundry cache list
foundry model run llama-3.2 --verbose
```
Docs:
- BYOM compile: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models

## 6) Pag-troubleshoot

- Suriin ang status ng serbisyo at mga log:
```cmd
foundry service status
foundry service diag
```
- I-clear o ilipat ang cache:
```cmd
foundry cache list
foundry cache remove <model>
foundry cache cd <path>
```
- Mag-update sa pinakabagong preview:
```cmd
winget upgrade --id Microsoft.FoundryLocal
```

## 7) Kaugnay na Karanasan ng Windows Developer

- Mga pagpipilian sa Windows lokal vs cloud AI, kabilang ang Foundry Local at Windows ML:
  https://learn.microsoft.com/windows/ai/cloud-ai#key-decision-factors-for-app-developers
- VS Code AI Toolkit gamit ang Foundry Local (gamitin ang `foundry service status` para makuha ang chat endpoint URL):
  https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture#key-components

[Susunod na Windows Developer](./windowdeveloper.md)

---

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't sinisikap naming maging tumpak, mangyaring tandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa kanyang katutubong wika ang dapat ituring na opisyal na sanggunian. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na dulot ng paggamit ng pagsasaling ito.
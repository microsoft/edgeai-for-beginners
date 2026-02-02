# ವಿಂಡೋಸ್ ಮತ್ತು ಮ್ಯಾಕ್‌ನಲ್ಲಿ ಫೌಂಡ್ರಿ ಲೋಕಲ್

ಈ ಮಾರ್ಗದರ್ಶಿ ನಿಮಗೆ ವಿಂಡೋಸ್ ಮತ್ತು ಮ್ಯಾಕ್‌ನಲ್ಲಿ ಮೈಕ್ರೋಸಾಫ್ಟ್ ಫೌಂಡ್ರಿ ಲೋಕಲ್ ಅನ್ನು ಸ್ಥಾಪಿಸಲು, ಚಾಲನೆ ಮಾಡಲು ಮತ್ತು ಸಂಯೋಜಿಸಲು ಸಹಾಯ ಮಾಡುತ್ತದೆ. ಎಲ್ಲಾ ಹಂತಗಳು ಮತ್ತು ಆಜ್ಞೆಗಳು ಮೈಕ್ರೋಸಾಫ್ಟ್ ಲರ್ನ್ ಡಾಕ್ಸ್ ವಿರುದ್ಧ ಪರಿಶೀಲಿಸಲಾಗಿದೆ.

- ಪ್ರಾರಂಭಿಸಿ: https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started
- ವಾಸ್ತುಶಿಲ್ಪ: https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture
- CLI ಉಲ್ಲೇಖ: https://learn.microsoft.com/azure/ai-foundry/foundry-local/reference/reference-cli
- SDKಗಳನ್ನು ಸಂಯೋಜಿಸಿ: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks
- HF ಮಾದರಿಗಳನ್ನು ಸಂಯೋಜಿಸಿ (BYOM): https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models
- ವಿಂಡೋಸ್ AI: ಲೋಕಲ್ ವಿರುದ್ಧ ಕ್ಲೌಡ್: https://learn.microsoft.com/windows/ai/cloud-ai#key-decision-factors-for-app-developers

## 1) ವಿಂಡೋಸ್‌ನಲ್ಲಿ ಸ್ಥಾಪನೆ / ನವೀಕರಣ

- ಸ್ಥಾಪಿಸಿ:
```cmd
winget install Microsoft.FoundryLocal
```
- ನವೀಕರಿಸಿ:
```cmd
winget upgrade --id Microsoft.FoundryLocal
```
- ಆವೃತ್ತಿ ಪರಿಶೀಲನೆ:
```cmd
foundry --version
```
     
**ಸ್ಥಾಪನೆ / ಮ್ಯಾಕ್**

**ಮ್ಯಾಕ್ಓಎಸ್**: 
ಟರ್ಮಿನಲ್ ತೆರೆಯಿರಿ ಮತ್ತು ಕೆಳಗಿನ ಆಜ್ಞೆಯನ್ನು ಚಾಲನೆ ಮಾಡಿ:
```bash
   brew tap microsoft/foundrylocal
   brew install foundrylocal
```

## 2) CLI ಮೂಲಭೂತಗಳು (ಮೂರು ವರ್ಗಗಳು)

- ಮಾದರಿ:
```cmd
foundry model --help
foundry model list
foundry model run gpt-oss-20b
```
- ಸೇವೆ:
```cmd
foundry service --help
foundry service status
foundry service ps
```
- ಕ್ಯಾಶೆ:
```cmd
foundry cache --help
foundry cache list
```

ಟಿಪ್ಪಣಿಗಳು:
- ಸೇವೆ OpenAI-ಸಮ್ಮತ REST API ಅನ್ನು ಬಹಿರಂಗಪಡಿಸುತ್ತದೆ. ಎಂಡ್ಪಾಯಿಂಟ್ ಪೋರ್ಟ್ ಡೈನಾಮಿಕ್ ಆಗಿ ಹಂಚಿಕೆಯಾಗುತ್ತದೆ; ಅದನ್ನು ಕಂಡುಹಿಡಿಯಲು `foundry service status` ಬಳಸಿ.
- ಅನುಕೂಲಕ್ಕಾಗಿ SDKಗಳನ್ನು ಬಳಸಿ; ಅವು ಎಂಡ್ಪಾಯಿಂಟ್ ಕಂಡುಹಿಡಿಯುವಿಕೆಯನ್ನು ಸ್ವಯಂಚಾಲಿತವಾಗಿ ನಿರ್ವಹಿಸುತ್ತವೆ, ಬೆಂಬಲಿತ ಸ್ಥಳಗಳಲ್ಲಿ.

## 3) ಲೋಕಲ್ ಎಂಡ್ಪಾಯಿಂಟ್ ಅನ್ನು ಕಂಡುಹಿಡಿಯಿರಿ (ಡೈನಾಮಿಕ್ ಪೋರ್ಟ್)

ಫೌಂಡ್ರಿ ಲೋಕಲ್ ಸೇವೆ ಪ್ರತಿ ಬಾರಿ ಪ್ರಾರಂಭವಾಗುವಾಗ ಡೈನಾಮಿಕ್ ಪೋರ್ಟ್ ಅನ್ನು ಹಂಚಿಕೆಯಾಗಿಸುತ್ತದೆ:
```cmd
foundry service status
```
 ವರದಿಯಾದ `http://localhost:<PORT>` ಅನ್ನು ನಿಮ್ಮ `base_url` ಆಗಿ OpenAI-ಸಮ್ಮತ ಮಾರ್ಗಗಳೊಂದಿಗೆ (ಉದಾಹರಣೆಗೆ, `/v1/chat/completions`) ಬಳಸಿ.

## 4) OpenAI ಪೈಥಾನ್ SDK ಮೂಲಕ ತ್ವರಿತ ಪರೀಕ್ಷೆ

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
ಉಲ್ಲೇಖಗಳು:
- SDK ಸಂಯೋಜನೆ: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

## 5) ನಿಮ್ಮದೇ ಮಾದರಿ ತಂದುಕೊಡಿ (ಒಲಿವ್ ಬಳಸಿ ಸಂಯೋಜಿಸಿ)

ನೀವು ಕ್ಯಾಟಲಾಗ್‌ನಲ್ಲಿ ಇಲ್ಲದ ಮಾದರಿಯನ್ನು ಬೇಕಾದರೆ, ಅದನ್ನು ಫೌಂಡ್ರಿ ಲೋಕಲ್‌ಗೆ ONNX ಗೆ ಸಂಯೋಜಿಸಲು ಒಲಿವ್ ಬಳಸಿ.

ಮೇಲ್ಮಟ್ಟದ ಪ್ರಕ್ರಿಯೆ (ಹಂತಗಳಿಗಾಗಿ ಡಾಕ್ಸ್ ನೋಡಿ):
```cmd
foundry cache cd models
foundry cache list
foundry model run llama-3.2 --verbose
```
ಡಾಕ್ಸ್:
- BYOM ಸಂಯೋಜನೆ: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models

## 6) ಸಮಸ್ಯೆ ಪರಿಹಾರ

- ಸೇವೆ ಸ್ಥಿತಿ ಮತ್ತು ಲಾಗ್‌ಗಳನ್ನು ಪರಿಶೀಲಿಸಿ:
```cmd
foundry service status
foundry service diag
```
- ಕ್ಯಾಶೆ ತೆರವುಗೊಳಿಸಿ ಅಥವಾ ಸ್ಥಳಾಂತರಿಸಿ:
```cmd
foundry cache list
foundry cache remove <model>
foundry cache cd <path>
```
- ಇತ್ತೀಚಿನ ಪೂರ್ವವೀಕ್ಷಣೆಗೆ ನವೀಕರಿಸಿ:
```cmd
winget upgrade --id Microsoft.FoundryLocal
```

## 7) ಸಂಬಂಧಿತ ವಿಂಡೋಸ್ ಡೆವಲಪರ್ ಅನುಭವ

- ವಿಂಡೋಸ್ ಲೋಕಲ್ ವಿರುದ್ಧ ಕ್ಲೌಡ್ AI ಆಯ್ಕೆಗಳು, ಫೌಂಡ್ರಿ ಲೋಕಲ್ ಮತ್ತು ವಿಂಡೋಸ್ ML ಸೇರಿ:
  https://learn.microsoft.com/windows/ai/cloud-ai#key-decision-factors-for-app-developers
- ಫೌಂಡ್ರಿ ಲೋಕಲ್ ಜೊತೆಗೆ VS ಕೋಡ್ AI ಟೂಲ್ಕಿಟ್ (`foundry service status` ಬಳಸಿ ಚಾಟ್ ಎಂಡ್ಪಾಯಿಂಟ್ URL ಪಡೆಯಿರಿ):
  https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture#key-components

[ಮುಂದಿನ ವಿಂಡೋಸ್ ಡೆವಲಪರ್](./windowdeveloper.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ಅಸ್ವೀಕರಣ**:  
ಈ ದಸ್ತಾವೇಜು [Co-op Translator](https://github.com/Azure/co-op-translator) ಎಂಬ AI ಅನುವಾದ ಸೇವೆಯನ್ನು ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ಶುದ್ಧತೆಯತ್ತ ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ತಪ್ಪುಗಳು ಅಥವಾ ಅಸತ್ಯತೆಗಳು ಇರಬಹುದು ಎಂದು ದಯವಿಟ್ಟು ಗಮನಿಸಿ. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ದಸ್ತಾವೇಜನ್ನು ಅಧಿಕೃತ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಮಹತ್ವದ ಮಾಹಿತಿಗಾಗಿ, ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದ ಬಳಕೆಯಿಂದ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವಿಕೆ ಅಥವಾ ತಪ್ಪು ವಿವರಣೆಗಳಿಗೆ ನಾವು ಹೊಣೆಗಾರರಾಗುವುದಿಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
# Windows மற்றும் Mac-ல் Foundry Local

இந்த வழிகாட்டி Microsoft Foundry Local-ஐ Windows மற்றும் Mac-ல் நிறுவ, இயக்க மற்றும் ஒருங்கிணைக்க உதவுகிறது. அனைத்து படிகளும் மற்றும் கட்டளைகளும் Microsoft Learn ஆவணங்களின் அடிப்படையில் சரிபார்க்கப்பட்டவை.

- தொடங்குங்கள்: https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started
- கட்டமைப்பு: https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture
- CLI குறிப்பு: https://learn.microsoft.com/azure/ai-foundry/foundry-local/reference/reference-cli
- SDKகளை ஒருங்கிணைக்க: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks
- HF மாதிரிகளை தொகுக்க (BYOM): https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models
- Windows AI: Local vs Cloud: https://learn.microsoft.com/windows/ai/cloud-ai#key-decision-factors-for-app-developers

## 1) Windows-ல் நிறுவல் / மேம்படுத்தல்

- நிறுவல்:
```cmd
winget install Microsoft.FoundryLocal
```
- மேம்படுத்தல்:
```cmd
winget upgrade --id Microsoft.FoundryLocal
```
- பதிப்பு சரிபார்ப்பு:
```cmd
foundry --version
```
     
**நிறுவல் / Mac**

**MacOS**: 
ஒரு டெர்மினலை திறந்து பின்வரும் கட்டளையை இயக்கவும்:
```bash
   brew tap microsoft/foundrylocal
   brew install foundrylocal
```

## 2) CLI அடிப்படைகள் (மூன்று வகைகள்)

- மாடல்:
```cmd
foundry model --help
foundry model list
foundry model run gpt-oss-20b
```
- சேவை:
```cmd
foundry service --help
foundry service status
foundry service ps
```
- கேஷ்:
```cmd
foundry cache --help
foundry cache list
```

குறிப்புகள்:
- சேவை OpenAI-க்கு இணையான REST API-ஐ வெளிப்படுத்துகிறது. இறுதிப்புள்ளி போர்ட் மாறுபடக்கூடியது; அதை கண்டறிய `foundry service status` ஐ பயன்படுத்தவும்.
- SDKகளை வசதிக்காக பயன்படுத்தவும்; அவை ஆதரவு உள்ள இடங்களில் இறுதிப்புள்ளி கண்டறிதலை தானாகவே கையாளும்.

## 3) உள்ளூர் இறுதிப்புள்ளியை கண்டறிதல் (மாறுபடும் போர்ட்)

Foundry Local சேவை ஒவ்வொரு முறையும் தொடங்கும் போது மாறுபடும் போர்ட்டை ஒதுக்குகிறது:
```cmd
foundry service status
```
அறிக்கையிடப்பட்ட `http://localhost:<PORT>` ஐ OpenAI-க்கு இணையான பாதைகளுடன் (உதாரணமாக, `/v1/chat/completions`) உங்கள் `base_url` ஆக பயன்படுத்தவும்.

## 4) OpenAI Python SDK மூலம் விரைவான சோதனை

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
குறிப்புகள்:
- SDK ஒருங்கிணைப்பு: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

## 5) உங்கள் சொந்த மாடலை கொண்டு வருதல் (Olive மூலம் தொகுக்க)

கட்டளையில் இல்லாத மாடலை தேவைப்பட்டால், அதை Foundry Local-க்கு ONNX ஆக Olive மூலம் தொகுக்கவும்.

உயர் நிலை செயல்முறை (படிகளுக்கு ஆவணங்களைப் பார்க்கவும்):
```cmd
foundry cache cd models
foundry cache list
foundry model run llama-3.2 --verbose
```
ஆவணங்கள்:
- BYOM தொகுப்பு: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models

## 6) பிழைகளை சரிசெய்தல்

- சேவை நிலை மற்றும் பதிவுகளை சரிபார்க்க:
```cmd
foundry service status
foundry service diag
```
- கேஷை அழிக்க அல்லது நகர்த்த:
```cmd
foundry cache list
foundry cache remove <model>
foundry cache cd <path>
```
- சமீபத்திய முன்னோட்டத்திற்கு மேம்படுத்த:
```cmd
winget upgrade --id Microsoft.FoundryLocal
```

## 7) தொடர்புடைய Windows டெவலப்பர் அனுபவம்

- Windows உள்ளூர் மற்றும் மேக AI தேர்வுகள், Foundry Local மற்றும் Windows ML உட்பட:
  https://learn.microsoft.com/windows/ai/cloud-ai#key-decision-factors-for-app-developers
- VS Code AI கருவி தொகுப்பு Foundry Local உடன் (சேவை நிலை URL ஐ பெற `foundry service status` ஐ பயன்படுத்தவும்):
  https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture#key-components

[அடுத்த Windows டெவலப்பர்](./windowdeveloper.md)

---

**குறிப்பு**:  
இந்த ஆவணம் [Co-op Translator](https://github.com/Azure/co-op-translator) என்ற AI மொழிபெயர்ப்பு சேவையை பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. எங்கள் நோக்கம் துல்லியமாக இருக்க வேண்டும் என்பதுதான், ஆனால் தானியங்கி மொழிபெயர்ப்புகளில் பிழைகள் அல்லது துல்லியமின்மைகள் இருக்கக்கூடும் என்பதை தயவுசெய்து கவனத்தில் கொள்ளவும். அதன் தாய்மொழியில் உள்ள மூல ஆவணம் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்முறை மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கங்களுக்கு நாங்கள் பொறுப்பல்ல.
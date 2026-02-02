# அமர்வு 6 மாதிரி: கருவிகளாக மாடல்கள்

இந்த மாதிரி, பயனர் உத்தரவின் அடிப்படையில் ஒரு மாடலை தேர்ந்தெடுத்து Foundry Local இன் OpenAI-இன் இணக்கமான இறுதிப்புள்ளியை அழைக்கும் குறைந்தபட்ச ரவுடர் + கருவி பதிவேட்டை செயல்படுத்துகிறது.

## கோப்புகள்
- `router.py`: எளிய பதிவேடு மற்றும் ஹியூரிஸ்டிக் ரவுடிங்; இறுதிப்புள்ளி கண்டறிதல் + ஆரோக்கிய சோதனை.

## இயக்கம் (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
REM Start whatever models you plan to route to
foundry model run phi-4-mini
foundry model run qwen2.5-7b
foundry model run deepseek-r1-7b

python samples\06\router.py "Explain how local-first AI improves privacy in two sentences."
```

## குறிப்புகள்
- ரவுடர் `general`, `reasoning`, மற்றும் `code` கருவிகளுக்கு இடையே தேர்வு செய்ய எளிய முக்கிய சொல் ஹியூரிஸ்டிக்ஸைப் பயன்படுத்துகிறது மற்றும் தொடக்கத்தில் `/v1/models` ஐ அச்சிடுகிறது.
- சூழல் மாறிகள் மூலம் கட்டமைக்கவும்:
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

## குறிப்புகள்
- Foundry Local (கற்றல்): https://learn.microsoft.com/azure/ai-foundry/foundry-local/
- தீர்மானம் SDKகளுடன் ஒருங்கிணைப்பு: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

---

**குறிப்பு**:  
இந்த ஆவணம் [Co-op Translator](https://github.com/Azure/co-op-translator) என்ற AI மொழிபெயர்ப்பு சேவையைப் பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சிக்கின்றோம், ஆனால் தானியங்கி மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கக்கூடும் என்பதை தயவுசெய்து கவனத்தில் கொள்ளுங்கள். அதன் தாய்மொழியில் உள்ள மூல ஆவணம் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்முறை மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கங்களுக்கு நாங்கள் பொறுப்பல்ல.
# அமர்வு 5 மாதிரி: பல முகவர் ஒருங்கிணைப்பு

இந்த மாதிரி Foundry Local இன் OpenAI-இக்கு இணக்கமான முடிவுநிலைப் பயன்பாட்டை பயன்படுத்தி ஒருங்கிணைப்பாளர் + நிபுணர்கள் முறைமையை விளக்குகிறது.

## இயக்கவும் (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
foundry model run phi-4-mini
python -m samples.05.agents.coordinator
```

## சரிபார்க்கவும்
```cmd
curl http://localhost:8000/v1/models
```

## சிக்கல்களை சரிசெய்தல்
- `coordinator.py`-இல் `import specialists` தீர்க்கப்படாதது என VS Code குறிக்குமானால், நீங்கள் ஒரு மாடியூலாக இயக்குகிறீர்கள் மற்றும் interpreter `Module08/.venv`-க்கு சுட்டிக்காட்டுகிறது என்பதை உறுதிப்படுத்தவும்:
	- இயக்கவும்: `python -m samples.05.agents.coordinator`
	- interpreter தேர்வு செய்யவும்: `Module08/.venv/Scripts/python.exe` (Ctrl+Shift+P → Python: Select Interpreter)

## குறிப்புகள்
- Foundry Local (கற்றல்): https://learn.microsoft.com/azure/ai-foundry/foundry-local/
- Azure AI Agents கண்ணோட்டம்: https://learn.microsoft.com/azure/ai-services/agents/overview
- செயல்பாடு அழைக்கும் மாதிரி (Foundry Local): https://github.com/microsoft/Foundry-Local/tree/main/samples/python/functioncalling

---

**குறிப்பு**:  
இந்த ஆவணம் [Co-op Translator](https://github.com/Azure/co-op-translator) என்ற AI மொழிபெயர்ப்பு சேவையைப் பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. எங்கள் தரச்செயல்முறையை உறுதிப்படுத்த முயற்சிக்கிறோம், ஆனால் தானியங்கி மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறான தகவல்கள் இருக்கக்கூடும் என்பதை தயவுசெய்து கவனத்தில் கொள்ளவும். அதன் தாய்மொழியில் உள்ள மூல ஆவணம் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்முறை மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கங்களுக்கு நாங்கள் பொறுப்பல்ல.
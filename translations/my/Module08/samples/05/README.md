# အခန်း ၅ နမူနာ: Multi-Agent Orchestration

ဒီနမူနာက Foundry Local ရဲ့ OpenAI-compatible endpoint ကို အသုံးပြုပြီး coordinator + specialists ပုံစံကို ပြသထားပါတယ်။

## Run (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
foundry model run phi-4-mini
python -m samples.05.agents.coordinator
```

## Validate
```cmd
curl http://localhost:8000/v1/models
```

## ပြဿနာဖြေရှင်းခြင်း
- VS Code မှာ `coordinator.py` ထဲက `import specialists` ကို မတွေ့ရင် `Module08/.venv` ကို interpreter အနေနဲ့ သတ်မှတ်ပြီး module အနေနဲ့ run လုပ်ပါ:
	- Run: `python -m samples.05.agents.coordinator`
	- Interpreter ရွေးချယ်ရန်: `Module08/.venv/Scripts/python.exe` (Ctrl+Shift+P → Python: Select Interpreter)

## ရင်းမြစ်များ
- Foundry Local (Learn): https://learn.microsoft.com/azure/ai-foundry/foundry-local/
- Azure AI Agents အကျဉ်းချုပ်: https://learn.microsoft.com/azure/ai-services/agents/overview
- Function calling နမူနာ (Foundry Local): https://github.com/microsoft/Foundry-Local/tree/main/samples/python/functioncalling

---


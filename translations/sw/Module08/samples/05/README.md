# Kipindi cha 5 Mfano: Uratibu wa Wakala Wengi

Mfano huu unaonyesha muundo wa mratibu + wataalamu kwa kutumia mwisho wa Foundry Local unaoendana na OpenAI.

## Endesha (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
foundry model run phi-4-mini
python -m samples.05.agents.coordinator
```

## Thibitisha
```cmd
curl http://localhost:8000/v1/models
```

## Utatuzi wa matatizo
- Ikiwa VS Code inaonyesha `import specialists` haijatatuliwa katika `coordinator.py`, hakikisha unaendesha kama moduli na mfasiri unaelekeza kwa `Module08/.venv`:
	- Endesha: `python -m samples.05.agents.coordinator`
	- Chagua mfasiri: `Module08/.venv/Scripts/python.exe` (Ctrl+Shift+P → Python: Select Interpreter)

## Marejeleo
- Foundry Local (Jifunze): https://learn.microsoft.com/azure/ai-foundry/foundry-local/
- Muhtasari wa Wakala wa Azure AI: https://learn.microsoft.com/azure/ai-services/agents/overview
- Mfano wa kupiga kazi (Foundry Local): https://github.com/microsoft/Foundry-Local/tree/main/samples/python/functioncalling

---


# 5 sesijos pavyzdys: Daugelio agentų koordinavimas

Šiame pavyzdyje demonstruojamas koordinatoriaus + specialistų modelis naudojant Foundry Local OpenAI suderinamą galinį tašką.

## Paleidimas (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
foundry model run phi-4-mini
python -m samples.05.agents.coordinator
```

## Patikrinimas
```cmd
curl http://localhost:8000/v1/models
```

## Trikčių šalinimas
- Jei VS Code pažymi `import specialists` kaip neišspręstą `coordinator.py` faile, įsitikinkite, kad paleidžiate kaip modulį ir interpretatorius nukreiptas į `Module08/.venv`:
	- Paleiskite: `python -m samples.05.agents.coordinator`
	- Pasirinkite interpretatorių: `Module08/.venv/Scripts/python.exe` (Ctrl+Shift+P → Python: Select Interpreter)

## Nuorodos
- Foundry Local (Mokymasis): https://learn.microsoft.com/azure/ai-foundry/foundry-local/
- Azure AI agentų apžvalga: https://learn.microsoft.com/azure/ai-services/agents/overview
- Funkcijų kvietimo pavyzdys (Foundry Local): https://github.com/microsoft/Foundry-Local/tree/main/samples/python/functioncalling

---


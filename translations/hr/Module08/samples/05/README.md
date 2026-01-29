# Sesija 5 Primjer: Orkestracija Više Agenta

Ovaj primjer prikazuje uzorak koordinator + specijalisti koristeći OpenAI-kompatibilnu krajnju točku Foundry Local.

## Pokretanje (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
foundry model run phi-4-mini
python -m samples.05.agents.coordinator
```

## Provjera
```cmd
curl http://localhost:8000/v1/models
```

## Rješavanje problema
- Ako VS Code označi `import specialists` kao neriješen u `coordinator.py`, provjerite da li pokrećete kao modul i da li interpreter pokazuje na `Module08/.venv`:
	- Pokrenite: `python -m samples.05.agents.coordinator`
	- Odaberite interpreter: `Module08/.venv/Scripts/python.exe` (Ctrl+Shift+P → Python: Select Interpreter)

## Reference
- Foundry Local (Učenje): https://learn.microsoft.com/azure/ai-foundry/foundry-local/
- Pregled Azure AI Agenti: https://learn.microsoft.com/azure/ai-services/agents/overview
- Primjer pozivanja funkcija (Foundry Local): https://github.com/microsoft/Foundry-Local/tree/main/samples/python/functioncalling

---


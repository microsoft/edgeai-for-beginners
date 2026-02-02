# Istunto 5 Esimerkki: Moniagenttinen Orkestrointi

Tämä esimerkki havainnollistaa koordinaattorin + asiantuntijoiden mallia käyttämällä Foundry Localin OpenAI-yhteensopivaa päätepistettä.

## Suorita (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
foundry model run phi-4-mini
python -m samples.05.agents.coordinator
```

## Vahvista
```cmd
curl http://localhost:8000/v1/models
```

## Vianmääritys
- Jos VS Code ilmoittaa, että `import specialists` ei ole ratkaistu tiedostossa `coordinator.py`, varmista, että suoritat moduulina ja tulkki osoittaa `Module08/.venv`-hakemistoon:
	- Suorita: `python -m samples.05.agents.coordinator`
	- Valitse tulkki: `Module08/.venv/Scripts/python.exe` (Ctrl+Shift+P → Python: Select Interpreter)

## Viitteet
- Foundry Local (Oppiminen): https://learn.microsoft.com/azure/ai-foundry/foundry-local/
- Azure AI Agents yleiskatsaus: https://learn.microsoft.com/azure/ai-services/agents/overview
- Funktiokutsuesimerkki (Foundry Local): https://github.com/microsoft/Foundry-Local/tree/main/samples/python/functioncalling

---


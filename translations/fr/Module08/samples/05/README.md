# Session 5 Exemple : Orchestration Multi-Agent

Cet exemple illustre un modèle de coordination + spécialistes en utilisant le point de terminaison compatible OpenAI de Foundry Local.

## Exécution (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
foundry model run phi-4-mini
python -m samples.05.agents.coordinator
```

## Validation
```cmd
curl http://localhost:8000/v1/models
```

## Résolution des problèmes
- Si VS Code signale que `import specialists` est non résolu dans `coordinator.py`, assurez-vous de l'exécuter en tant que module et que l'interpréteur pointe vers `Module08/.venv` :
	- Exécutez : `python -m samples.05.agents.coordinator`
	- Sélectionnez l'interpréteur : `Module08/.venv/Scripts/python.exe` (Ctrl+Shift+P → Python : Select Interpreter)

## Références
- Foundry Local (Apprendre) : https://learn.microsoft.com/azure/ai-foundry/foundry-local/
- Vue d'ensemble des agents Azure AI : https://learn.microsoft.com/azure/ai-services/agents/overview
- Exemple d'appel de fonction (Foundry Local) : https://github.com/microsoft/Foundry-Local/tree/main/samples/python/functioncalling

---


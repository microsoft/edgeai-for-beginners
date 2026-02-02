# Session 6 Exemple : Les modèles comme outils

Cet exemple implémente un routeur minimal + un registre d'outils qui sélectionne un modèle en fonction de la requête utilisateur et appelle le point de terminaison compatible OpenAI de Foundry Local.

## Fichiers
- `router.py` : registre simple et routage heuristique ; découverte de point de terminaison + vérification de l'état.

## Exécution (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
REM Start whatever models you plan to route to
foundry model run phi-4-mini
foundry model run qwen2.5-7b
foundry model run deepseek-r1-7b

python samples\06\router.py "Explain how local-first AI improves privacy in two sentences."
```

## Remarques
- Le routeur utilise des heuristiques simples basées sur des mots-clés pour choisir entre les outils `general`, `reasoning` et `code`, et affiche `/v1/models` au démarrage.
- Configuration via des variables d'environnement :
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

## Références
- Foundry Local (Apprendre) : https://learn.microsoft.com/azure/ai-foundry/foundry-local/
- Intégration avec les SDK d'inférence : https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

---

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction humaine professionnelle. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées résultant de l'utilisation de cette traduction.
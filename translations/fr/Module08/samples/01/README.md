# Exemple 01 : Discussion rapide via le SDK OpenAI

Un exemple simple de discussion montrant comment utiliser le SDK OpenAI avec Microsoft Foundry Local pour une inférence IA locale.

## Vue d'ensemble

Cet exemple montre comment :
- Utiliser le SDK Python OpenAI avec Foundry Local
- Gérer les configurations Azure OpenAI et Foundry Local
- Implémenter une gestion correcte des erreurs et des stratégies de repli
- Utiliser le FoundryLocalManager pour la gestion des services

## Prérequis

- **Foundry Local** : Installé et disponible dans le PATH
- **Python** : Version 3.8 ou ultérieure
- **Modèle** : Un modèle chargé dans Foundry Local (par exemple, `phi-4-mini`)

## Installation

1. **Configurer l'environnement Python :**
   ```cmd
   cd Module08
   py -m venv .venv
   .venv\Scripts\activate
   ```

2. **Installer les dépendances :**
   ```cmd
   pip install -r requirements.txt
   ```

3. **Démarrer le service Foundry Local et charger un modèle :**
   ```cmd
   foundry model run phi-4-mini
   ```

## Utilisation

### Foundry Local (par défaut)

```cmd
# Using FoundryLocalManager (recommended)
python samples\01\chat_quickstart.py "Explain what Foundry Local is"

# Using manual configuration
set BASE_URL=http://localhost:8000
set MODEL=phi-4-mini
set API_KEY=
python samples\01\chat_quickstart.py "Write a welcome message"
```

### Azure OpenAI

```cmd
set AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
set AZURE_OPENAI_API_KEY=your-api-key
set AZURE_OPENAI_API_VERSION=2024-08-01-preview
set MODEL=your-deployment-name
python samples\01\chat_quickstart.py "Hello from Azure OpenAI"
```

## Fonctionnalités du code

### Intégration avec FoundryLocalManager

L'exemple utilise le SDK officiel Foundry Local pour une gestion correcte des services :

```python
from foundry_local import FoundryLocalManager
from openai import OpenAI

# Initialize Foundry Local
manager = FoundryLocalManager(alias)
model_info = manager.get_model_info(alias)

# Configure OpenAI client
client = OpenAI(
    base_url=manager.endpoint,
    api_key=manager.api_key
)
```

### Gestion des erreurs

Gestion robuste des erreurs avec repli sur une configuration manuelle :
- Découverte automatique des services
- Dégradation progressive si le SDK n'est pas disponible
- Messages d'erreur clairs pour faciliter le dépannage

## Variables d'environnement

| Variable | Description | Valeur par défaut | Obligatoire |
|----------|-------------|-------------------|-------------|
| `MODEL` | Alias ou nom du modèle | `phi-4-mini` | Non |
| `BASE_URL` | URL de base de Foundry Local | `http://localhost:8000` | Non |
| `API_KEY` | Clé API (généralement inutile en local) | `""` | Non |
| `AZURE_OPENAI_ENDPOINT` | Point de terminaison Azure OpenAI | - | Pour Azure |
| `AZURE_OPENAI_API_KEY` | Clé API Azure OpenAI | - | Pour Azure |
| `AZURE_OPENAI_API_VERSION` | Version de l'API Azure | `2024-08-01-preview` | Non |

## Dépannage

### Problèmes courants

1. **Avertissement "Impossible d'utiliser le SDK Foundry" :**
   - Installer le SDK Foundry Local : `pip install foundry-local-sdk`
   - Ou définir les variables d'environnement pour une configuration manuelle

2. **Connexion refusée :**
   - Vérifiez que Foundry Local est en cours d'exécution : `foundry service status`
   - Assurez-vous qu'un modèle est chargé : `foundry service ps`

3. **Modèle introuvable :**
   - Lister les modèles disponibles : `foundry model list`
   - Charger un modèle : `foundry model run phi-4-mini`

### Vérification

```cmd
# Check Foundry Local status
foundry service status

# List loaded models
foundry service ps

# Test API endpoint
curl http://localhost:8000/v1/models
```

## Références

- [Documentation Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [SDK Python OpenAI](https://github.com/openai/openai-python)
- [GitHub Foundry Local](https://github.com/microsoft/Foundry-Local)
- [Référence API compatible OpenAI](https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks)

---


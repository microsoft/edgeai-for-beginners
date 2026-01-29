# Exemple 02 : Intégration du SDK OpenAI

Démontre une intégration avancée avec le SDK Python OpenAI, prenant en charge à la fois Microsoft Foundry Local et Azure OpenAI avec des réponses en streaming et une gestion correcte des erreurs.

## Aperçu

Ce modèle met en avant :
- Une transition fluide entre Foundry Local et Azure OpenAI
- Des complétions de chat en streaming pour une meilleure expérience utilisateur
- Une utilisation appropriée du SDK FoundryLocalManager
- Des mécanismes de gestion des erreurs robustes et des solutions de secours
- Des modèles de code prêts pour la production

## Prérequis

- **Foundry Local** : Installé et en cours d'exécution (pour l'inférence locale)
- **Python** : Version 3.8 ou ultérieure avec le SDK OpenAI
- **Azure OpenAI** : Point de terminaison valide et clé API (pour l'inférence cloud)

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

3. **Démarrer Foundry Local (pour le mode local) :**
   ```cmd
   foundry model run phi-4-mini
   ```


## Scénarios d'utilisation

### Foundry Local (par défaut)

**Option 1 : Utilisation de FoundryLocalManager (recommandé)**
```cmd
# Automatic service discovery and model management
set MODEL=phi-4-mini
python samples\02\sdk_quickstart.py
```

**Option 2 : Configuration manuelle**
```cmd
# Manual endpoint configuration
set BASE_URL=http://localhost:8000
set MODEL=phi-4-mini
set API_KEY=
python samples\02\sdk_quickstart.py
```


### Azure OpenAI

```cmd
# Azure OpenAI configuration
set AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
set AZURE_OPENAI_API_KEY=your-api-key
set AZURE_OPENAI_API_VERSION=2024-08-01-preview
set MODEL=your-deployment-name
python samples\02\sdk_quickstart.py
```


## Architecture du code

### Modèle de fabrique de clients

Le modèle utilise un modèle de fabrique pour créer les clients appropriés :

```python
def create_foundry_client():
    """Create Foundry Local client with SDK management."""
    manager = FoundryLocalManager(alias)
    client = OpenAI(
        base_url=manager.endpoint,
        api_key=manager.api_key
    )
    return client, manager.get_model_info(alias).id

def create_azure_client():
    """Create Azure OpenAI client."""
    client = OpenAI(
        base_url=f"{endpoint}/openai",
        api_key=api_key,
        default_query={"api-version": api_version}
    )
    return client, model
```


### Réponses en streaming

Le modèle démontre le streaming pour une génération de réponses en temps réel :

```python
stream = client.chat.completions.create(
    model=model,
    messages=[{"role": "user", "content": prompt}],
    stream=True
)

for chunk in stream:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="", flush=True)
```


## Variables d'environnement

### Configuration de Foundry Local

| Variable      | Description                  | Par défaut         | Obligatoire |
|---------------|------------------------------|--------------------|-------------|
| `MODEL`       | Alias du modèle à utiliser  | `phi-4-mini`       | Non         |
| `BASE_URL`    | Point de terminaison Foundry Local | `http://localhost:8000` | Non         |
| `API_KEY`     | Clé API (optionnelle pour le local) | `""`              | Non         |

### Configuration Azure OpenAI

| Variable                  | Description                          | Par défaut               | Obligatoire |
|---------------------------|--------------------------------------|--------------------------|-------------|
| `AZURE_OPENAI_ENDPOINT`   | Point de terminaison de la ressource Azure OpenAI | -                        | Oui         |
| `AZURE_OPENAI_API_KEY`    | Clé API Azure OpenAI                | -                        | Oui         |
| `AZURE_OPENAI_API_VERSION`| Version de l'API                    | `2024-08-01-preview`     | Non         |
| `MODEL`                   | Nom du déploiement Azure            | `your-deployment-name`   | Oui         |

## Fonctionnalités avancées

### Découverte automatique des services

Le modèle détecte automatiquement le service approprié en fonction des variables d'environnement :

1. **Mode Azure** : Si `AZURE_OPENAI_ENDPOINT` et `AZURE_OPENAI_API_KEY` sont définis
2. **Mode SDK Foundry** : Si le SDK Foundry Local est disponible
3. **Mode manuel** : Retour à la configuration manuelle

### Gestion des erreurs

- Retour en douceur du SDK à la configuration manuelle
- Messages d'erreur clairs pour le dépannage
- Gestion appropriée des exceptions pour les problèmes réseau
- Validation des variables d'environnement requises

## Considérations sur les performances

### Comparaison entre local et cloud

**Avantages de Foundry Local :**
- ✅ Pas de coûts API
- ✅ Confidentialité des données (aucune donnée ne quitte l'appareil)
- ✅ Faible latence pour les modèles pris en charge
- ✅ Fonctionne hors ligne

**Avantages d'Azure OpenAI :**
- ✅ Accès aux derniers modèles de grande taille
- ✅ Débit plus élevé
- ✅ Pas de besoins en calcul local
- ✅ SLA de niveau entreprise

## Dépannage

### Problèmes courants

1. **Avertissement "Impossible d'utiliser le SDK Foundry" :**
   ```cmd
   pip install foundry-local-sdk
   ```

2. **Erreurs d'authentification Azure :**
   ```cmd
   # Verify your endpoint format
   echo %AZURE_OPENAI_ENDPOINT%
   # Should be: https://your-resource.openai.azure.com
   ```

3. **Modèle non disponible :**
   ```cmd
   # For Foundry Local
   foundry model list
   foundry model run your-model-name
   
   # For Azure OpenAI
   # Check your deployment name in Azure Portal
   ```


### Vérifications de santé

```cmd
# Foundry Local
foundry service status
curl http://localhost:8000/v1/models

# Azure OpenAI
curl -H "api-key: %AZURE_OPENAI_API_KEY%" "%AZURE_OPENAI_ENDPOINT%/openai/deployments?api-version=2024-08-01-preview"
```


## Prochaines étapes

- **Exemple 03** : Découverte et benchmarking des modèles
- **Exemple 04** : Création d'une application RAG avec Chainlit
- **Exemple 05** : Orchestration multi-agents
- **Exemple 06** : Routage des modèles comme outils

## Références

- [Documentation Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/)
- [Référence SDK Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [Documentation SDK Python OpenAI](https://github.com/openai/openai-python)
- [Guide des complétions en streaming](https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/integrate-with-inference-sdks)

---


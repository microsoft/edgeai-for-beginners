<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8c30436578b1bd604c48233ecdd39701",
  "translation_date": "2025-11-11T21:19:06+00:00",
  "source_file": "Workshop/Session01-GettingStartedFoundryLocal.md",
  "language_code": "fr"
}
-->
# Session 1 : Premiers pas avec Foundry Local

## Résumé

Apprenez à installer, configurer et exécuter vos premiers modèles d'IA avec Microsoft Foundry Local. Cette session pratique offre une introduction pas à pas à l'inférence locale, de l'installation à la création de votre première application de chat utilisant des modèles tels que Phi-4, Qwen et DeepSeek.

## Objectifs d'apprentissage

À la fin de cette session, vous serez capable de :

- **Installer et configurer** : Configurer Foundry Local avec une vérification correcte de l'installation
- **Maîtriser les opérations CLI** : Utiliser le CLI de Foundry Local pour la gestion et le déploiement des modèles
- **Exécuter votre premier modèle** : Déployer et interagir avec un modèle d'IA local
- **Créer une application de chat** : Concevoir une application de chat basique en utilisant le SDK Python de Foundry Local
- **Comprendre l'IA locale** : Assimiler les bases de l'inférence locale et de la gestion des modèles

## Prérequis

### Configuration système

- **Windows** : Windows 11 (22H2 ou version ultérieure) OU **macOS** : macOS 11+ (support limité)
- **RAM** : Minimum 8 Go, recommandé 16 Go ou plus
- **Stockage** : Au moins 10 Go d'espace libre pour les modèles
- **Python** : Version 3.10 ou ultérieure installée
- **Accès administrateur** : Privilèges administratifs pour l'installation

### Environnement de développement

- Visual Studio Code avec extension Python (recommandé)
- Accès à la ligne de commande (PowerShell sur Windows, Terminal sur macOS)
- Git pour cloner des dépôts (optionnel)

## Déroulement de l'atelier (30 minutes)

### Étape 1 : Installer Foundry Local (5 minutes)

#### Installation sur Windows

Installez Foundry Local en utilisant le gestionnaire de paquets Windows :

```powershell
# Install via winget (recommended)
winget install Microsoft.FoundryLocal
```

Alternative : Téléchargez directement depuis [Microsoft Learn](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install)

#### Installation sur macOS (support limité)

> [!NOTE] 
> Le support macOS est actuellement en aperçu. Consultez la documentation officielle pour les dernières informations.

Si disponible, installez via Homebrew :

```bash
# If Homebrew formula is available
brew update
brew install foundry-local

# Or manual download (check official docs for latest)
curl -L -o foundry-local.tar.gz "https://download.microsoft.com/foundry-local/latest/macos/foundry-local.tar.gz"
tar -xzf foundry-local.tar.gz
sudo ./install.sh
```

**Alternative pour les utilisateurs macOS :**
- Utilisez une VM Windows 11 (Parallels/UTM) et suivez les étapes pour Windows
- Exécutez via un conteneur si disponible et configurez `FOUNDRY_LOCAL_ENDPOINT`

### Étape 2 : Vérifier l'installation (3 minutes)

Après l'installation, redémarrez votre terminal et vérifiez que Foundry Local fonctionne :

```powershell
# Check if Foundry Local is installed correctly
foundry --version

# View available commands
foundry --help
```

La sortie attendue doit afficher les informations de version et les commandes disponibles.

### Étape 3 : Configurer l'environnement Python (5 minutes)

Créez un environnement Python dédié pour cet atelier :

**Windows :**
```powershell
# Create virtual environment
py -m venv .venv

# Activate environment
.\.venv\Scripts\Activate.ps1

# Upgrade pip and install dependencies
python -m pip install --upgrade pip
pip install foundry-local-sdk openai
```

**macOS/Linux :**
```bash
# Create virtual environment
python3 -m venv .venv

# Activate environment
source .venv/bin/activate

# Upgrade pip and install dependencies
python -m pip install --upgrade pip
pip install foundry-local-sdk openai
```

### Étape 4 : Exécuter votre premier modèle (7 minutes)

Passons maintenant à l'exécution de notre premier modèle d'IA en local !

#### Commencez avec Phi-4 Mini (modèle recommandé)

```powershell
# Download and start phi-4-mini (lightweight, fast)
foundry model run phi-4-mini

# Test the model with a simple prompt
foundry model run phi-4-mini --prompt "Hello, introduce yourself in one sentence"
```

> [!TIP]
> Cette commande télécharge le modèle (la première fois) et démarre automatiquement le service Foundry Local.

#### Vérifiez ce qui est en cours d'exécution

```powershell
# List available models (shows downloaded models)
foundry model list

# Check service status
foundry service status

# See what models are cached locally
foundry cache list
```

#### Essayez différents modèles

Une fois que phi-4-mini fonctionne, expérimentez avec d'autres modèles :

```powershell
# Larger model with better capabilities
foundry model run gpt-oss-20b --prompt "Explain edge AI in simple terms"

# Fast, efficient model
foundry model run qwen2.5-0.5b --prompt "What are the benefits of local AI inference?"
```

### Étape 5 : Créer votre première application de chat (10 minutes)

Créons maintenant une application Python qui utilise les modèles que nous venons de démarrer.

#### Créer le script de chat

Créez un nouveau fichier appelé `my_first_chat.py` (ou utilisez l'exemple fourni) :

```python
#!/usr/bin/env python3
"""
My First Foundry Local Chat Application
Using FoundryLocalManager for automatic service management
"""

import os
from foundry_local import FoundryLocalManager
from openai import OpenAI

def main():
    # Get model alias from environment or use default
    alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-4-mini")
    
    try:
        # Initialize Foundry Local Manager (auto-starts service, downloads model)
        manager = FoundryLocalManager(alias)
        
        # Create OpenAI client pointing to local endpoint
        client = OpenAI(
            base_url=manager.endpoint,
            api_key=manager.api_key or "not-needed"
        )
        
        # Get the actual model ID for this alias
        model_id = manager.get_model_info(alias).id
        
        print("🤖 Welcome to your first local AI chat!")
        print(f"� Using model: {alias} -> {model_id}")
        print(f"🌐 Endpoint: {manager.endpoint}")
        print("�💡 Type 'quit' to exit\n")
        
    except Exception as e:
        print(f"❌ Failed to initialize Foundry Local: {e}")
        print("💡 Make sure Foundry Local is installed: foundry --version")
        return
    
    while True:
        # Get user input
        user_message = input("You: ").strip()
        
        if user_message.lower() in ['quit', 'exit', 'bye']:
            print("👋 Goodbye!")
            break
            
        if not user_message:
            continue
            
        try:
            # Send message to local AI model
            response = client.chat.completions.create(
                model=model_id,
                messages=[
                    {"role": "system", "content": "You are a helpful AI assistant running locally."},
                    {"role": "user", "content": user_message}
                ],
                max_tokens=200,
                temperature=0.7
            )
            
            # Display the response
            ai_response = response.choices[0].message.content
            print(f"🤖 AI: {ai_response}\n")
            
        except Exception as e:
            print(f"❌ Error: {e}")
            print("💡 Check service status: foundry service status\n")

if __name__ == "__main__":
    main()
```

> [!TIP]
> **Exemples associés** : Pour une utilisation plus avancée, consultez :
>
> - **Exemple Python** : `Workshop/samples/session01/chat_bootstrap.py` - Inclut des réponses en streaming et la gestion des erreurs
> - **Notebook Jupyter** : `Workshop/notebooks/session01_chat_bootstrap.ipynb` - Version interactive avec des explications détaillées

#### Testez votre application de chat

```powershell
# No need to manually start models - FoundryLocalManager handles this!
# Just run your chat application
python my_first_chat.py
```

Alternative : Utilisez directement les exemples fournis

```powershell
# Try the complete sample with streaming support
cd Workshop/samples
python -m session01.chat_bootstrap "Your question here"
```

Ou explorez le notebook interactif
Ouvrez Workshop/notebooks/session01_chat_bootstrap.ipynb dans VS Code

Essayez ces exemples de conversations :

- "Qu'est-ce que Microsoft Foundry Local ?"
- "Listez 3 avantages de l'exécution de modèles d'IA en local"
- "Aidez-moi à comprendre l'IA de périphérie"

## Ce que vous avez accompli

Félicitations ! Vous avez réussi à :

1. ✅ **Installer Foundry Local** et vérifier son fonctionnement
2. ✅ **Démarrer votre premier modèle d'IA** (phi-4-mini) en local
3. ✅ **Tester différents modèles** via la ligne de commande
4. ✅ **Créer une application de chat** connectée à votre IA locale
5. ✅ **Expérimenter l'inférence d'IA locale** sans dépendances cloud

## Comprendre ce qui s'est passé

### Inférence d'IA locale

- Vos modèles d'IA fonctionnent entièrement sur votre ordinateur
- Aucune donnée n'est envoyée au cloud
- Les réponses sont générées localement en utilisant votre CPU/GPU
- La confidentialité et la sécurité sont préservées

### Gestion des modèles

- `foundry model run` télécharge et démarre les modèles
- **FoundryLocalManager SDK** gère automatiquement le démarrage du service et le chargement des modèles
- Les modèles sont mis en cache localement pour une utilisation future
- Plusieurs modèles peuvent être téléchargés, mais généralement un seul fonctionne à la fois
- Le service gère automatiquement le cycle de vie des modèles

### Approches SDK vs CLI

- **Approche CLI** : Gestion manuelle des modèles avec `foundry model run <model>`
- **Approche SDK** : Gestion automatique du service et des modèles avec `FoundryLocalManager(alias)`
- **Recommandation** : Utilisez le SDK pour les applications, le CLI pour les tests et l'exploration

## Référence des commandes courantes

### Commandes CLI essentielles

```powershell
# Installation & Setup
foundry --version              # Check installation
foundry --help                 # View all commands

# Model Management
foundry model list             # List available models
foundry model run <model>      # Download and start a model
foundry model run <model> --prompt "text"  # One-shot prompt
foundry cache list             # Show downloaded models

# Service Management
foundry service status         # Check if service is running
foundry service start          # Start the service manually
foundry service stop           # Stop the service
```

### Recommandations de modèles

- **phi-4-mini** : Meilleur modèle de départ - rapide, léger, bonne qualité
- **qwen2.5-0.5b** : Inférence la plus rapide, utilisation minimale de mémoire
- **gpt-oss-20b** : Réponses de meilleure qualité, nécessite plus de ressources
- **deepseek-coder-1.3b** : Optimisé pour les tâches de programmation et de code

## Résolution des problèmes

### "Commande Foundry introuvable"

**Solution :**

```powershell
# Restart your terminal after installation
# Or manually add to PATH (Windows)
$env:PATH += ";C:\Program Files\Microsoft\FoundryLocal"
```

### "Échec du chargement du modèle"

**Solution :**

```powershell
# Check available system memory
foundry service status

# Try a smaller model first
foundry model run phi-4-mini

# Check disk space for model downloads
# Models are stored in: %USERPROFILE%\.foundry\models (Windows)
```

### "Connexion refusée sur localhost"

**Solution :**

```powershell
# Check if service is running
foundry service status

# Start service if needed
foundry service start

# Verify the port (default is 5273)
# Check for port conflicts with: netstat -an | findstr 5273
```

## Prochaines étapes

### Actions immédiates

1. **Expérimentez** avec différents modèles et invites
2. **Modifiez** votre application de chat pour essayer différents modèles
3. **Créez** vos propres invites et testez les réponses
4. **Explorez** la Session 2 : Création d'applications RAG

### Parcours d'apprentissage avancé

1. **Session 2** : Construire des solutions d'IA avec RAG (Retrieval-Augmented Generation)
2. **Session 3** : Comparer différents modèles open-source
3. **Session 4** : Travailler avec des modèles de pointe
4. **Session 5** : Construire des systèmes d'IA multi-agents

## Variables d'environnement (optionnel)

Pour une utilisation plus avancée, vous pouvez définir ces variables d'environnement :

| Variable | Objectif | Exemple |
|----------|----------|---------|
| `FOUNDRY_LOCAL_ALIAS` | Modèle par défaut à utiliser | `phi-4-mini` |
| `FOUNDRY_LOCAL_ENDPOINT` | Remplacer l'URL de l'endpoint | `http://localhost:5273/v1` |

Créez un fichier `.env` dans le répertoire de votre projet :
```
FOUNDRY_LOCAL_ALIAS=phi-4-mini
FOUNDRY_LOCAL_ENDPOINT=auto
```

## Ressources supplémentaires

### Documentation

- [Référence SDK Python Foundry Local](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/reference/reference-sdk?pivots=programming-language-python)
- [Guide d'installation Foundry Local](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install)
- [Catalogue des modèles](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/models)

### Code exemple

- **Exemple Python Session01** : `Workshop/samples/session01/chat_bootstrap.py` - Application de chat complète avec streaming
- **Notebook Session01** : `Workshop/notebooks/session01_chat_bootstrap.ipynb` - Tutoriel interactif  
- [Exemple Module08 01](../Module08/samples/01/README.md) - Démarrage rapide REST Chat
- [Exemple Module08 02](../Module08/samples/02/README.md) - Intégration SDK OpenAI
- [Exemple Module08 03](../Module08/samples/03/README.md) - Découverte et benchmarking des modèles

### Communauté

- [Discussions GitHub Foundry Local](https://github.com/microsoft/Foundry-Local/discussions)
- [Communauté Azure AI](https://techcommunity.microsoft.com/category/artificialintelligence)

---

**Durée de la session** : 30 minutes de pratique + 15 minutes de questions/réponses  
**Niveau de difficulté** : Débutant  
**Prérequis** : Windows 11/macOS 11+, Python 3.10+, accès administrateur

## Exemple de scénario d'atelier

### Contexte réel

**Scénario** : Une équipe informatique d'entreprise doit évaluer l'inférence d'IA sur appareil pour traiter des retours d'employés sensibles sans envoyer de données à des services externes.

**Votre objectif** : Démontrer que les modèles d'IA locaux peuvent fournir des réponses de qualité avec une latence inférieure à une seconde tout en maintenant une confidentialité totale des données.

### Prompts de test

Utilisez ces prompts pour valider votre configuration :

```json
[
    "List two benefits of local inference.",
    "Summarize why keeping data on device improves privacy.",
    "Give one trade-off when choosing a small model over a large model."
]
```

### Critères de réussite

- ✅ Toutes les invites obtiennent des réponses en moins de 2 secondes
- ✅ Aucune donnée ne quitte votre machine locale
- ✅ Les réponses sont pertinentes et utiles
- ✅ Votre application de chat fonctionne sans problème

Cette validation garantit que votre configuration Foundry Local est prête pour les ateliers avancés des Sessions 2 à 6.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction humaine professionnelle. Nous ne sommes pas responsables des malentendus ou des interprétations erronées résultant de l'utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
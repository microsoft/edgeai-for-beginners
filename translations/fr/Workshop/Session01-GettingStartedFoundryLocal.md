<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "85fa559f498492b79de04e391c33687b",
  "translation_date": "2025-10-28T20:01:14+00:00",
  "source_file": "Workshop/Session01-GettingStartedFoundryLocal.md",
  "language_code": "fr"
}
-->
# Session 1 : Premiers pas avec Foundry Local

## Résumé

Commencez votre aventure avec Foundry Local en l'installant et en le configurant sur Windows 11. Apprenez à configurer l'interface en ligne de commande (CLI), à activer l'accélération matérielle et à mettre en cache les modèles pour une inférence locale rapide. Cette session pratique vous guide dans l'exécution de modèles tels que Phi, Qwen, DeepSeek et GPT-OSS-20B à l'aide de commandes CLI reproductibles.

## Objectifs d'apprentissage

À la fin de cette session, vous serez capable de :

- **Installer et configurer** : Configurer Foundry Local sur Windows 11 avec des paramètres de performance optimaux
- **Maîtriser les opérations CLI** : Utiliser le CLI de Foundry Local pour la gestion et le déploiement des modèles
- **Activer l'accélération matérielle** : Configurer l'accélération GPU avec ONNXRuntime ou WebGPU
- **Déployer plusieurs modèles** : Exécuter les modèles phi-4, GPT-OSS-20B, Qwen et DeepSeek localement
- **Créer votre première application** : Adapter des exemples existants pour utiliser le SDK Python de Foundry Local

# Tester le modèle (invite unique non interactive)
foundry model run phi-4-mini --prompt "Bonjour, présentez-vous"

- Windows 11 (22H2 ou version ultérieure)
# Lister les modèles disponibles dans le catalogue (les modèles chargés apparaissent après exécution)
foundry model list
## NOTE : Il n'existe actuellement pas de drapeau dédié `--running` ; pour voir lesquels sont chargés, lancez une conversation ou inspectez les journaux de service.
- Python 3.10+ installé
- Visual Studio Code avec extension Python
- Privilèges administrateur pour l'installation

### (Optionnel) Variables d'environnement

Créez un fichier `.env` (ou définissez-les dans le shell) pour rendre les scripts portables :
# Comparer les réponses (non interactif)
foundry model run gpt-oss-20b --prompt "Expliquez l'IA de périphérie en termes simples"
| Variable | Objectif | Exemple |
|----------|----------|---------|
| `FOUNDRY_LOCAL_ALIAS` | Alias préféré du modèle (le catalogue sélectionne automatiquement la meilleure variante) | `phi-3.5-mini` |
| `FOUNDRY_LOCAL_ENDPOINT` | Remplacer le point de terminaison (sinon automatique depuis le gestionnaire) | `http://localhost:5273/v1` |
| `FOUNDRY_LOCAL_STREAM` | Activer la démonstration de streaming | `true` |

> Si `FOUNDRY_LOCAL_ENDPOINT=auto` (ou non défini), il est dérivé du gestionnaire SDK.

## Déroulement de la démonstration (30 minutes)

### 1. Installer Foundry Local et vérifier la configuration du CLI (10 minutes)

# Lister les modèles mis en cache
foundry cache list

```powershell
# Install via winget (recommended)
winget install Microsoft.FoundryLocal

# Or download from Microsoft Learn
# https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install
```

**macOS (Aperçu / Si pris en charge)**

Si un package natif macOS est fourni (consultez la documentation officielle pour les dernières informations) :

```bash
# Homebrew (if/when available)
brew update
brew install foundry-local  # hypothetical formula name

# Or manual download (tarball)
curl -L -o foundry-local.tar.gz "https://download.microsoft.com/foundry-local/latest/macos/foundry-local.tar.gz"
tar -xzf foundry-local.tar.gz
sudo ./install.sh
```

Si les binaires natifs macOS ne sont pas encore disponibles, vous pouvez toujours :
1. Utiliser une VM Windows 11 ARM/Intel (Parallels / UTM) et suivre les étapes pour Windows.
2. Exécuter les modèles via un conteneur (si une image de conteneur est publiée) et définir `FOUNDRY_LOCAL_ENDPOINT` sur le port exposé.

**Créer un environnement virtuel Python (multi-plateforme)**

Windows PowerShell :
```powershell
py -m venv .venv
 .\.venv\Scripts\Activate.ps1
```

macOS / Linux :
```bash
python3 -m venv .venv
source .venv/bin/activate
```

Mettre à jour pip et installer les dépendances principales :
```bash
python -m pip install --upgrade pip
pip install foundry-local-sdk openai
```

#### Étape 1.2 : Vérifier l'installation

```powershell
# Check version
foundry --version

# Initialize configuration
foundry init

# View available commands
foundry --help
```

#### Étape 1.3 : Configurer l'environnement

```powershell
# Set up Python environment for Module08
cd Module08
py -m venv .venv
.\.venv\Scripts\activate

# Install Foundry Local Python SDK and dependencies
pip install foundry-local-sdk openai requests
```

### Initialisation du SDK (recommandé)

Plutôt que de démarrer manuellement le service et d'exécuter les modèles, le **SDK Python de Foundry Local** peut tout initialiser automatiquement :

```python
from foundry_local import FoundryLocalManager
from openai import OpenAI
import os

alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-3.5-mini")

# Bootstraps service + downloads + loads most suitable variant for hardware
manager = FoundryLocalManager(alias)

print("Service running:", manager.is_service_running())
print("Endpoint:", manager.endpoint)
print("Cached models:", manager.list_cached_models())

client = OpenAI(base_url=manager.endpoint, api_key=manager.api_key or "not-needed")

resp = client.chat.completions.create(
    model=manager.get_model_info(alias).id,
    messages=[
        {"role": "system", "content": "You are a helpful local assistant."},
        {"role": "user", "content": "Hello"}
    ],
    max_tokens=120,
    temperature=0.5
)
print(resp.choices[0].message.content)
```

Si vous préférez un contrôle explicite, vous pouvez toujours utiliser le CLI + client OpenAI comme montré plus tard.

### 2. Exécuter des modèles localement via CLI (10 minutes)

#### Étape 3.1 : Déployer le modèle Phi-4

```powershell
# Download and run phi-4-mini
foundry model run phi-4-mini

# Test the model (one-shot prompt)
foundry model run phi-4-mini --prompt "Hello, introduce yourself"

# NOTE: There is no `--running` flag; use `foundry model list` and recent activity to infer loaded models.
```

#### Étape 3.2 : Déployer GPT-OSS-20B

```powershell
# Download and run GPT-OSS-20B
foundry model run gpt-oss-20b

# Compare responses (one-shot prompt)
foundry model run gpt-oss-20b --prompt "Explain edge AI in simple terms"
```

#### Étape 3.3 : Charger des modèles supplémentaires

```powershell
# Download Qwen model family
foundry model download qwen2.5-0.5b
foundry model download qwen2.5-7b

# Download DeepSeek models
foundry model download deepseek-coder-1.3b

# List cached models
foundry cache list
```

### 4. Projet de démarrage : Adapter 01-run-phi pour Foundry Local (5 minutes)

#### Étape 4.1 : Créer une application de chat basique

Créer `samples/01-foundry-quickstart/chat_quickstart.py` (mis à jour pour utiliser le gestionnaire si disponible) :

```python
#!/usr/bin/env python3
"""
Foundry Local Chat Quickstart
Demo: Basic chat interaction using Foundry Local Python SDK
Reference: https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/reference/reference-sdk?pivots=programming-language-python
"""

import os, sys
from openai import OpenAI
try:
    from foundry_local import FoundryLocalManager  # control-plane SDK
except ImportError:
    FoundryLocalManager = None

def main():
    """Main chat function using Foundry Local SDK"""
    
    # Preferred: bootstrap via SDK manager (auto start + download + load)
    alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-3.5-mini")
    if FoundryLocalManager:
        manager = FoundryLocalManager(alias)
        endpoint = manager.endpoint
        model_id = manager.get_model_info(alias).id
        api_key = manager.api_key or "not-needed"
    else:
        # Fallback: assume default endpoint & alias already running via CLI
        endpoint = os.getenv("FOUNDRY_LOCAL_ENDPOINT", "http://localhost:5273/v1")
        model_id = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-4-mini")
        api_key = "not-needed"

    client = OpenAI(base_url=endpoint, api_key=api_key)
    
    # Get user input
    if len(sys.argv) > 1:
        user_message = " ".join(sys.argv[1:])
    else:
        user_message = input("Enter your message: ")
    
    try:
        # Make chat completion request
        response = client.chat.completions.create(
            model=model_id,
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant powered by Microsoft Foundry Local."},
                {"role": "user", "content": user_message}
            ],
            max_tokens=500,
            temperature=0.7
        )
        
        # Display response
        print(f"\nModel: {response.model}")
        print(f"Response: {response.choices[0].message.content}")
        print(f"Tokens used: {response.usage.total_tokens if response.usage else 'N/A'}")
        
    except Exception as e:
        print(f"Error: {e}")
        print("\nTroubleshooting:")
    print("1. Ensure Foundry Local is running: foundry status")
    print("2. List models: foundry model list")
    print(f"3. Start model if needed: foundry model run {model_id}")
    print("4. Or let SDK bootstrap: pip install foundry-local-sdk")

if __name__ == "__main__":
    main()
```

#### Étape 4.2 : Tester l'application

```powershell
# Ensure phi-4-mini is running
foundry model run phi-4-mini

# Run the quickstart app
python samples/01-foundry-quickstart/chat_quickstart.py "What is Microsoft Foundry Local?"

# Try interactive mode
python samples/01-foundry-quickstart/chat_quickstart.py
```

## Concepts clés abordés

### 1. Architecture de Foundry Local

- **Moteur d'inférence local** : Exécute les modèles entièrement sur votre appareil
- **Compatibilité avec le SDK OpenAI** : Intégration transparente avec le code OpenAI existant
- **Gestion des modèles** : Téléchargement, mise en cache et exécution efficace de plusieurs modèles
- **Optimisation matérielle** : Exploitation de l'accélération GPU, NPU et CPU

### 2. Référence des commandes CLI

```powershell
# Core Commands
foundry --version              # Check installation
# Model Management
foundry model list             # List available models
foundry model unload <name>    # Unload from memory

foundry config list            # Current configuration
```

### 3. Intégration du SDK Python

```python
# Basic client setup
from foundry_local import FoundryLocalManager
from openai import OpenAI
import os

alias = os.getenv("FOUNDRY_LOCAL_ALIAS", "phi-3.5-mini")
manager = FoundryLocalManager(alias)
client = OpenAI(base_url=manager.endpoint, api_key=manager.api_key or "not-needed")

response = client.chat.completions.create(
    model=manager.get_model_info(alias).id,
    messages=[{"role": "user", "content": "Hello!"}],
    max_tokens=50
)
print(response.choices[0].message.content)

# Streaming example
stream = client.chat.completions.create(
    model=manager.get_model_info(alias).id,
    messages=[{"role": "user", "content": "Give a 1-sentence definition of edge AI."}],
    stream=True,
    max_tokens=60,
    temperature=0.4
)
for chunk in stream:
    delta = chunk.choices[0].delta
    if delta and delta.content:
        print(delta.content, end="", flush=True)
print()
```

## Résolution des problèmes courants

### Problème 1 : "Commande Foundry introuvable"

**Solution :**
```powershell
# Restart PowerShell after installation
# Or manually add to PATH
$env:PATH += ";C:\Program Files\Microsoft\FoundryLocal"
```

### Problème 2 : "Échec du chargement du modèle"

**Solution :**
```powershell
# Check available memory
foundry system info

# Try smaller model first
foundry model run phi-4-mini

# Check disk space for model cache
dir "$env:USERPROFILE\.foundry\models"
```

### Problème 3 : "Connexion refusée sur localhost:5273"

**Solution :**
```powershell
# Check if service is running
foundry status

# Start service if needed
foundry service start

# Check for port conflicts
netstat -an | findstr 5273
```

## Conseils pour optimiser les performances

### 1. Stratégie de sélection des modèles

- **Phi-4-mini** : Idéal pour les tâches générales, faible utilisation de mémoire
- **Qwen2.5-0.5b** : Inférence la plus rapide, ressources minimales
- **GPT-OSS-20B** : Qualité maximale, nécessite plus de ressources
- **DeepSeek-Coder** : Optimisé pour les tâches de programmation

### 2. Optimisation matérielle

```powershell
# Enable all acceleration options
foundry config set compute.onnx.enable_gpu true
foundry config set compute.webgpu.enabled true
foundry config set compute.cpu.threads auto

# Optimize memory usage
foundry config set model.cache.max_size 10GB
foundry config set model.preload false
```

### 3. Surveillance des performances

```powershell
cd Workshop/samples
# Performance & latency measurement
# Use the Python benchmark script (Session 3) instead of legacy 'model stats' or 'model benchmark' commands.
# Example:
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
python -m session03.benchmark_oss_models

# Re-run after enabling GPU acceleration to compare:
foundry config set compute.onnx.enable_gpu true
python -m session03.benchmark_oss_models
```

### Améliorations optionnelles

| Amélioration | Objectif | Comment |
|--------------|----------|---------|
| Utilitaires partagés | Éliminer la logique client/bootstrap dupliquée | Utiliser `Workshop/samples/workshop_utils.py` (`get_client`, `chat_once`) |
| Visibilité de l'utilisation des tokens | Enseigner la gestion des coûts/efficacité dès le début | Définir `SHOW_USAGE=1` pour afficher les tokens de l'invite/de la réponse/total |
| Comparaisons déterministes | Tests de performance et de régression stables | Utiliser `temperature=0`, `top_p=1`, texte d'invite cohérent |
| Latence du premier token | Indicateur de réactivité perçue | Adapter le script de benchmark avec le streaming (`BENCH_STREAM=1`) |
| Réessayer en cas d'erreurs transitoires | Démos résilientes au démarrage à froid | `RETRY_ON_FAIL=1` (par défaut) et ajuster `RETRY_BACKOFF` |
| Tests de fumée | Vérification rapide des flux clés | Exécuter `python Workshop/tests/smoke.py` avant un atelier |
| Profils d'alias de modèles | Changer rapidement l'ensemble de modèles entre machines | Maintenir un fichier `.env` avec `FOUNDRY_LOCAL_ALIAS`, `SLM_ALIAS`, `LLM_ALIAS` |
| Efficacité du cache | Éviter les échauffements répétés dans une exécution multi-échantillons | Les gestionnaires de cache des utilitaires ; réutilisation entre scripts/notebooks |
| Échauffement initial | Réduire les pics de latence p95 | Envoyer une petite invite après la création de `FoundryLocalManager`

Exemple de base déterministe (PowerShell) :

```powershell
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
python Workshop\samples\session01\chat_bootstrap.py "List two privacy benefits of local inference." | Out-Null
python Workshop\samples\session01\chat_bootstrap.py "List two privacy benefits of local inference."
```

Vous devriez voir une sortie similaire et des comptes de tokens identiques lors de la deuxième exécution, confirmant le caractère déterministe.

## Prochaines étapes

Après avoir terminé cette session :

1. **Explorer la session 2** : Construire des solutions IA avec Azure AI Foundry RAG
2. **Essayer différents modèles** : Expérimenter avec Qwen, DeepSeek et d'autres familles de modèles
3. **Optimiser les performances** : Affiner les paramètres pour votre matériel spécifique
4. **Créer des applications personnalisées** : Utiliser le SDK Foundry Local dans vos propres projets

## Ressources supplémentaires

### Documentation
- [Référence SDK Python Foundry Local](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/reference/reference-sdk?pivots=programming-language-python)
- [Guide d'installation Foundry Local](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/install)
- [Catalogue de modèles](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/models)

### Code d'exemple
- [Exemple Module08 01](./samples/01/README.md) - Démarrage rapide du chat REST
- [Exemple Module08 02](./samples/02/README.md) - Intégration SDK OpenAI
- [Exemple Module08 03](./samples/03/README.md) - Découverte et benchmarking des modèles

### Communauté
- [Discussions GitHub Foundry Local](https://github.com/microsoft/Foundry-Local/discussions)
- [Communauté Azure AI](https://techcommunity.microsoft.com/category/artificialintelligence)

---

**Durée de la session** : 30 minutes de pratique + 15 minutes de questions/réponses  
**Niveau de difficulté** : Débutant  
**Prérequis** : Windows 11, Python 3.10+, accès administrateur

## Scénario d'exemple et cartographie de l'atelier

| Script / Notebook de l'atelier | Scénario | Objectif | Exemple d'entrée(s) | Ensemble de données requis |
|--------------------------------|----------|----------|----------------------|-----------------------------|
| `samples/session01/chat_bootstrap.py` / `notebooks/session01_chat_bootstrap.ipynb` | Équipe IT interne évaluant l'inférence sur appareil pour un portail d'évaluation de la confidentialité | Prouver que le SLM local répond avec une latence inférieure à une seconde sur des invites standard | "Listez deux avantages de l'inférence locale." | Aucun (invite unique) |
| Bloc de code d'adaptation du démarrage rapide | Développeur migrant un script OpenAI existant vers Foundry Local | Montrer la compatibilité immédiate | "Donnez deux avantages de l'inférence locale." | Invite en ligne uniquement |

### Narratif du scénario
L'équipe de sécurité et conformité doit valider si des données prototypes sensibles peuvent être traitées localement. Ils exécutent le script bootstrap avec plusieurs invites (confidentialité, latence, coût) en mode déterministe `temperature=0` pour capturer des résultats de base à comparer ultérieurement (benchmarking de la session 3 et contraste SLM vs LLM de la session 4).

### Ensemble minimal d'invites JSON (optionnel)
```json
[
    "List two benefits of local inference.",
    "Summarize why keeping data on device improves privacy.",
    "Give one trade‑off when choosing an SLM over a large model."
]
```

Utilisez cette liste pour créer une boucle d'évaluation reproductible ou pour alimenter un futur banc de test de régression.

---

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction humaine professionnelle. Nous ne sommes pas responsables des malentendus ou des interprétations erronées résultant de l'utilisation de cette traduction.
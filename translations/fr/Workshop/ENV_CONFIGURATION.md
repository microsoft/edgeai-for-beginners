<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "da0a7a09670d5ab535141d121ea043fe",
  "translation_date": "2025-10-28T20:00:30+00:00",
  "source_file": "Workshop/ENV_CONFIGURATION.md",
  "language_code": "fr"
}
-->
# Guide de Configuration de l'Environnement

## Aperçu

Les exemples du Workshop utilisent des variables d'environnement pour la configuration, centralisées dans le fichier `.env` à la racine du dépôt. Cela permet une personnalisation facile sans modifier le code.

## Démarrage Rapide

### 1. Vérifiez les Prérequis

```bash
# Check Foundry Local is installed
foundry --version

# Check service is running
foundry service status

# Load a model
foundry model run phi-4-mini
```

### 2. Configurez l'Environnement

Le fichier `.env` est déjà configuré avec des valeurs par défaut adaptées. La plupart des utilisateurs n'auront pas besoin de modifier quoi que ce soit.

**Optionnel** : Passez en revue et personnalisez les paramètres :
```bash
# Edit .env file
notepad .env  # Windows
nano .env     # macOS/Linux
```

### 3. Appliquez la Configuration

**Pour les scripts Python :**
```bash
cd Workshop/samples
python -m session01.chat_bootstrap "Your question here"
# Environment variables automatically loaded
```

**Pour les notebooks :**
```python
# Restart kernel after .env changes
# Variables are loaded when cells execute
```

## Référence des Variables d'Environnement

### Configuration Principale

| Variable | Par Défaut | Description |
|----------|------------|-------------|
| `FOUNDRY_LOCAL_ALIAS` | `phi-4-mini` | Modèle par défaut pour les exemples |
| `FOUNDRY_LOCAL_ENDPOINT` | (vide) | Remplace le point de service |
| `PYTHONPATH` | Chemins du Workshop | Chemin de recherche des modules Python |

**Quand définir FOUNDRY_LOCAL_ENDPOINT :**
- Instance Foundry Local distante
- Configuration de port personnalisée
- Séparation développement/production

**Exemple :**
```bash
# Local custom port
FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Remote instance
FOUNDRY_LOCAL_ENDPOINT=http://192.168.1.50:5273/v1
```

### Variables Spécifiques à la Session

#### Session 02 : Pipeline RAG
| Variable | Par Défaut | Objectif |
|----------|------------|----------|
| `EMBED_MODEL` | `sentence-transformers/all-MiniLM-L6-v2` | Modèle d'embedding |
| `RAG_QUESTION` | Préconfiguré | Question de test |

#### Session 03 : Benchmarking
| Variable | Par Défaut | Objectif |
|----------|------------|----------|
| `BENCH_MODELS` | `phi-4-mini,qwen2.5-0.5b` | Modèles à tester |
| `BENCH_ROUNDS` | `3` | Itérations par modèle |
| `BENCH_PROMPT` | Préconfiguré | Prompt de test |
| `BENCH_STREAM` | `0` | Mesure de la latence du premier token |

#### Session 04 : Comparaison de Modèles
| Variable | Par Défaut | Objectif |
|----------|------------|----------|
| `SLM_ALIAS` | `phi-4-mini` | Petit modèle de langage |
| `LLM_ALIAS` | `qwen2.5-7b` | Grand modèle de langage |
| `COMPARE_PROMPT` | Préconfiguré | Prompt de comparaison |
| `COMPARE_RETRIES` | `2` | Tentatives de réessai |

#### Session 05 : Orchestration Multi-Agent
| Variable | Par Défaut | Objectif |
|----------|------------|----------|
| `AGENT_MODEL_PRIMARY` | `phi-4-mini` | Modèle de l'agent chercheur |
| `AGENT_MODEL_EDITOR` | `phi-4-mini` | Modèle de l'agent éditeur |
| `AGENT_QUESTION` | Préconfiguré | Question de test |

### Configuration de Fiabilité

| Variable | Par Défaut | Objectif |
|----------|------------|----------|
| `SHOW_USAGE` | `1` | Affiche l'utilisation des tokens |
| `RETRY_ON_FAIL` | `1` | Active la logique de réessai |
| `RETRY_BACKOFF` | `1.0` | Délai de réessai (secondes) |

## Configurations Courantes

### Configuration de Développement (Itération Rapide)
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=phi-4-mini
BENCH_MODELS=phi-4-mini
SHOW_USAGE=1
```

### Configuration de Production (Focus Qualité)
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-7b
AGENT_MODEL_PRIMARY=phi-4-mini
AGENT_MODEL_EDITOR=qwen2.5-7b
SHOW_USAGE=0
```

### Configuration de Benchmarking
```bash
BENCH_MODELS=phi-4-mini,qwen2.5-0.5b,qwen2.5-7b
BENCH_ROUNDS=5
BENCH_STREAM=1
```

### Spécialisation Multi-Agent
```bash
AGENT_MODEL_PRIMARY=phi-4-mini        # Fast for research
AGENT_MODEL_EDITOR=qwen2.5-7b         # Quality for editing
```

### Développement à Distance
```bash
FOUNDRY_LOCAL_ENDPOINT=http://dev-server.local:5273/v1
FOUNDRY_LOCAL_ALIAS=phi-4-mini
```

## Modèles Recommandés

### Par Cas d'Utilisation

**Usage Général :**
- `phi-4-mini` - Équilibre entre qualité et rapidité

**Réponses Rapides :**
- `qwen2.5-0.5b` - Très rapide, idéal pour la classification
- `phi-4-mini` - Rapide avec une bonne qualité

**Haute Qualité :**
- `qwen2.5-7b` - Meilleure qualité, utilisation de ressources plus élevée
- `phi-4-mini` - Bonne qualité, moins de ressources nécessaires

**Génération de Code :**
- `deepseek-coder-1.3b` - Spécialisé pour le code
- `phi-4-mini` - Codage généraliste

### Par Disponibilité des Ressources

**Ressources Faibles (< 8GB RAM) :**
```bash
FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b
SLM_ALIAS=qwen2.5-0.5b
LLM_ALIAS=phi-4-mini
```

**Ressources Moyennes (8-16GB RAM) :**
```bash
FOUNDRY_LOCAL_ALIAS=phi-4-mini
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-7b
```

**Ressources Élevées (16GB+ RAM) :**
```bash
FOUNDRY_LOCAL_ALIAS=qwen2.5-7b
SLM_ALIAS=phi-4-mini
LLM_ALIAS=qwen2.5-14b
```

## Configuration Avancée

### Points de Service Personnalisés

```bash
# Development environment
FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Staging environment
FOUNDRY_LOCAL_ENDPOINT=http://staging.internal:5273/v1

# Production environment
FOUNDRY_LOCAL_ENDPOINT=http://prod.internal:5273/v1
```

### Température & Échantillonnage (Remplacement dans le Code)

```python
# In your scripts/notebooks
os.environ['TEMPERATURE'] = '0.7'
os.environ['TOP_P'] = '0.9'
```

### Configuration Hybride Azure OpenAI

```bash
# Use local for development
FOUNDRY_LOCAL_ALIAS=phi-4-mini

# Configure Azure for production fallback
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
AZURE_OPENAI_API_KEY=your-key-here
AZURE_OPENAI_API_VERSION=2024-08-01-preview
```

## Résolution des Problèmes

### Variables d'Environnement Non Chargées

**Symptômes :**
- Les scripts utilisent les mauvais modèles
- Erreurs de connexion
- Variables non reconnues

**Solutions :**
```bash
# 1. Verify .env exists in repository root
ls -la .env  # macOS/Linux
dir .env     # Windows

# 2. Check file is not .env.txt (Windows)
# Ensure no hidden extension

# 3. For notebooks: Restart kernel
# Kernel > Restart

# 4. For scripts: Check working directory
pwd  # Should be in Workshop or repository root
```

### Problèmes de Connexion au Service

**Symptômes :**
- Erreurs "Connexion refusée"
- "Service non disponible"
- Erreurs de délai d'attente

**Solutions :**
```bash
# 1. Check service status
foundry service status

# 2. Start if not running
foundry service start

# 3. Verify endpoint
# Check port in status output
foundry service status | grep "Port"

# 4. Update .env if needed
FOUNDRY_LOCAL_ENDPOINT=http://localhost:<port>
```

### Modèle Non Trouvé

**Symptômes :**
- Erreurs "Modèle non trouvé"
- "Alias non reconnu"

**Solutions :**
```bash
# 1. List available models
foundry model list

# 2. Load required model
foundry model run phi-4-mini

# 3. Update .env with available model
FOUNDRY_LOCAL_ALIAS=<available-model>
```

### Erreurs d'Importation

**Symptômes :**
- Erreurs "Module non trouvé"

**Solutions :**

```bash
# 1. Activate virtual environment
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux

# 2. Install dependencies
pip install -r requirements.txt
```

## Test de la Configuration

### Vérifiez le Chargement de l'Environnement

```python
# test_env.py
import os
from dotenv import load_dotenv

load_dotenv()

print("Core Configuration:")
print(f"  FOUNDRY_LOCAL_ALIAS: {os.getenv('FOUNDRY_LOCAL_ALIAS')}")
print(f"  FOUNDRY_LOCAL_ENDPOINT: {os.getenv('FOUNDRY_LOCAL_ENDPOINT') or 'auto'}")

print("\nSession 04:")
print(f"  SLM_ALIAS: {os.getenv('SLM_ALIAS')}")
print(f"  LLM_ALIAS: {os.getenv('LLM_ALIAS')}")

print("\nSession 05:")
print(f"  AGENT_MODEL_PRIMARY: {os.getenv('AGENT_MODEL_PRIMARY')}")
print(f"  AGENT_MODEL_EDITOR: {os.getenv('AGENT_MODEL_EDITOR')}")
```

### Testez la Connexion à Foundry Local

```python
# test_connection.py
import os
from foundry_local import FoundryLocalManager

alias = os.getenv('FOUNDRY_LOCAL_ALIAS', 'phi-4-mini')
endpoint = os.getenv('FOUNDRY_LOCAL_ENDPOINT')

try:
    if endpoint:
        manager = FoundryLocalManager(alias, endpoint=endpoint)
    else:
        manager = FoundryLocalManager(alias)
    
    print(f"✓ Connected to {manager.endpoint}")
    print(f"✓ Model: {manager.get_model_info(alias).id}")
    print(f"✓ Available models: {len(manager.list_models())}")
except Exception as e:
    print(f"✗ Connection failed: {e}")
```

## Bonnes Pratiques de Sécurité

### 1. Ne Jamais Commiter des Secrets

```bash
# .gitignore should include:
.env
.env.local
*.key
```

### 2. Utilisez des Fichiers .env Séparés

```bash
.env              # Default configuration
.env.local        # Local overrides (gitignored)
.env.production   # Production config (secure storage)
```

### 3. Faites Tourner les Clés API

```bash
# For Azure OpenAI or other cloud services
# Regularly rotate keys and update .env
```

### 4. Utilisez une Configuration Spécifique à l'Environnement

```bash
# Development
FOUNDRY_LOCAL_ENDPOINT=http://localhost:5273/v1

# Production (use secrets management)
FOUNDRY_LOCAL_ENDPOINT=${PROD_FOUNDRY_ENDPOINT}
```

## Documentation SDK

- **Dépôt Principal** : https://github.com/microsoft/Foundry-Local
- **SDK Python** : https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local
- **Documentation API** : Consultez le dépôt SDK pour les dernières informations

## Ressources Supplémentaires

- `QUICK_START.md` - Guide de démarrage
- `SDK_MIGRATION_NOTES.md` - Détails sur la mise à jour du SDK
- `Workshop/samples/*/README.md` - Guides spécifiques aux exemples

---

**Dernière Mise à Jour** : 2025-01-08  
**Version** : 2.0  
**SDK** : Foundry Local Python SDK (dernier)

---

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction humaine professionnelle. Nous ne sommes pas responsables des malentendus ou des interprétations erronées résultant de l'utilisation de cette traduction.
# Guide de démarrage rapide - Carnets de l'atelier

## Table des matières

- [Prérequis](../../../../Workshop/notebooks)
- [Configuration initiale](../../../../Workshop/notebooks)
- [Session 04 : Comparaison de modèles](../../../../Workshop/notebooks)
- [Session 05 : Orchestrateur multi-agents](../../../../Workshop/notebooks)
- [Session 06 : Routage basé sur l'intention](../../../../Workshop/notebooks)
- [Variables d'environnement](../../../../Workshop/notebooks)
- [Commandes courantes](../../../../Workshop/notebooks)

---

## Prérequis

### 1. Installer Foundry Local

**Windows :**
```bash
winget install Microsoft.FoundryLocal
```

**macOS :**
```bash
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**Vérifier l'installation :**
```bash
foundry --version
```

### 2. Installer les dépendances Python

```bash
cd Workshop
pip install -r requirements.txt
```

Ou installer individuellement :
```bash
pip install foundry-local-sdk openai numpy requests
```

---

## Configuration initiale

### Démarrer le service Foundry Local

**Requis avant d'exécuter tout carnet :**

```bash
# Start the service
foundry service start

# Verify it's running
foundry service status
```

Résultat attendu :
```
✅ Service started successfully
Endpoint: http://localhost:59959
```

### Télécharger et charger les modèles

Les carnets utilisent ces modèles par défaut :

```bash
# Download models (first time only - may take several minutes)
foundry model download phi-4-mini
foundry model download qwen2.5-3b
foundry model download phi-3.5-mini
foundry model download qwen2.5-0.5b

# Load models into memory
foundry model run phi-4-mini
foundry model run qwen2.5-3b
foundry model run phi-3.5-mini
```

### Vérifier la configuration

```bash
# List loaded models
foundry model ls

# Check service health
curl http://localhost:59959/v1/models
```

---

## Session 04 : Comparaison de modèles

### Objectif
Comparer les performances entre les modèles de langage de petite taille (SLM) et les modèles de langage de grande taille (LLM).

### Configuration rapide

```bash
# Start service (if not already running)
foundry service start

# Load required models
foundry model run phi-4-mini
foundry model run qwen2.5-3b
```

### Exécution du carnet

1. **Ouvrir** `session04_model_compare.ipynb` dans VS Code ou Jupyter
2. **Redémarrer le noyau** (Kernel → Restart Kernel)
3. **Exécuter toutes les cellules** dans l'ordre

### Configuration clé

**Modèles par défaut :**
- **SLM :** `phi-4-mini` (~4 Go de RAM, plus rapide)
- **LLM :** `qwen2.5-3b` (~3 Go de RAM, optimisé pour la mémoire)

**Variables d'environnement (optionnel) :**
```python
import os
os.environ['SLM_ALIAS'] = 'phi-4-mini'
os.environ['LLM_ALIAS'] = 'qwen2.5-3b'
os.environ['FOUNDRY_LOCAL_ENDPOINT'] = 'http://localhost:59959/v1'
```

### Résultat attendu

```
================================================================================
COMPARISON SUMMARY
================================================================================
Alias                Latency(s)      Tokens     Route               
--------------------------------------------------------------------------------
phi-4-mini           1.234           150        chat.completions    
qwen2.5-3b           2.456           180        chat.completions    
================================================================================

💡 SLM is 1.99x faster than LLM for this prompt
```

### Personnalisation

**Utiliser des modèles différents :**
```python
os.environ['SLM_ALIAS'] = 'phi-3.5-mini'
os.environ['LLM_ALIAS'] = 'qwen2.5-1.5b'
```

**Prompt personnalisé :**
```python
os.environ['COMPARE_PROMPT'] = 'Explain quantum computing in simple terms'
```

### Liste de validation

- [ ] La cellule 12 affiche les modèles corrects (phi-4-mini, qwen2.5-3b)
- [ ] La cellule 12 affiche le bon point de terminaison (port 59959)
- [ ] Le diagnostic de la cellule 16 est réussi (✅ Le service est en cours d'exécution)
- [ ] La vérification préalable de la cellule 20 est réussie (les deux modèles sont OK)
- [ ] La comparaison de la cellule 22 est terminée avec des valeurs de latence
- [ ] La validation de la cellule 24 affiche 🎉 TOUS LES TESTS RÉUSSIS !

### Estimation du temps
- **Première exécution :** 5-10 minutes (y compris le téléchargement des modèles)
- **Exécutions suivantes :** 1-2 minutes

---

## Session 05 : Orchestrateur multi-agents

### Objectif
Démontrer la collaboration multi-agents en utilisant le SDK Foundry Local - les agents travaillent ensemble pour produire des résultats affinés.

### Configuration rapide

```bash
# Start service
foundry service start

# Load models
foundry model run phi-4-mini  # Primary model
foundry model run qwen2.5-7b  # Optional: higher quality editor
```

### Exécution du carnet

1. **Ouvrir** `session05_agents_orchestrator.ipynb`
2. **Redémarrer le noyau**
3. **Exécuter toutes les cellules** dans l'ordre

### Configuration clé

**Configuration par défaut (même modèle pour les deux agents) :**
```python
PRIMARY_ALIAS = 'phi-4-mini'
EDITOR_ALIAS = 'phi-4-mini'  # Uses same model
```

**Configuration avancée (modèles différents) :**
```python
import os
os.environ['AGENT_MODEL_PRIMARY'] = 'phi-4-mini'     # Fast for research
os.environ['AGENT_MODEL_EDITOR'] = 'qwen2.5-7b'      # High quality for editing
```

### Architecture

```
User Question
    ↓
Researcher Agent (phi-4-mini)
  → Gathers bullet points
    ↓
Editor Agent (phi-4-mini or qwen2.5-7b)
  → Refines into executive summary
    ↓
Final Output
```

### Résultat attendu

```
================================================================================
[Pipeline] Question: Explain why edge AI matters for compliance.
================================================================================

[Stage 1: Research]
Output: • Edge AI processes data locally, reducing transmission...

[Stage 2: Editorial Refinement]
Output: Executive Summary: Edge AI enhances compliance by keeping data...

[FINAL OUTPUT]
Executive Summary: Edge AI enhances compliance by keeping sensitive data 
on-premises and reduces latency through local processing.

[METADATA]
Models used: {'researcher': 'phi-4-mini', 'editor': 'phi-4-mini'}
```

### Extensions

**Ajouter plus d'agents :**
```python
critic = Agent(
    name='Critic',
    system='Review content for accuracy',
    client=client,
    model_id=model_id
)
```

**Tests en lot :**
```python
test_questions = [
    "What are benefits of local AI?",
    "How does RAG improve accuracy?",
]

for q in test_questions:
    result = pipeline(q, verbose=False)
    print(result['final'])
```

### Estimation du temps
- **Première exécution :** 3-5 minutes
- **Exécutions suivantes :** 1-2 minutes par question

---

## Session 06 : Routage basé sur l'intention

### Objectif
Acheminer intelligemment les prompts vers des modèles spécialisés en fonction de l'intention détectée.

### Configuration rapide

```bash
# Start service
foundry service start

# Load all routing models (CPU variants recommended)
foundry model run phi-4-mini-cpu
foundry model run qwen2.5-0.5b-cpu
foundry model run phi-3.5-mini-cpu
```

**Remarque :** La session 06 utilise par défaut des modèles CPU pour une compatibilité maximale.

### Exécution du carnet

1. **Ouvrir** `session06_models_router.ipynb`
2. **Redémarrer le noyau**
3. **Exécuter toutes les cellules** dans l'ordre

### Configuration clé

**Catalogue par défaut (modèles CPU) :**
```python
CATALOG = {
    'phi-4-mini-cpu': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','refactor'],'priority':3},
}
```

**Alternative (modèles GPU) :**
```python
# Uncomment GPU catalog in Cell #6 if you have sufficient VRAM (8GB+)
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini': {'capabilities':['code','refactor'],'priority':3},
}
```

### Détection d'intention

Le routeur utilise des motifs regex pour détecter l'intention :

| Intention         | Exemples de motifs         | Acheminé vers          |
|-------------------|---------------------------|------------------------|
| `code`           | "refactor", "implement function" | phi-3.5-mini-cpu      |
| `classification` | "categorize", "classify this"    | qwen2.5-0.5b-cpu      |
| `summarize`      | "summarize", "tl;dr"            | phi-4-mini-cpu        |
| `general`        | Tout le reste                  | phi-4-mini-cpu        |

### Résultat attendu

```
✓ Using CPU-optimized models (default configuration)
  Models: phi-4-mini-cpu, qwen2.5-0.5b-cpu, phi-3.5-mini-cpu

Routing prompts to specialized models...
============================================================

Prompt: Refactor this Python function for readability
  Intent: code           | Model: phi-3.5-mini-cpu
  Output: Here's a refactored version...
  Tokens: 156

Prompt: Categorize this email as urgent or normal
  Intent: classification | Model: qwen2.5-0.5b-cpu
  Output: Category: Normal
  Tokens: 45

✓ Success! All prompts routed correctly.
```

### Personnalisation

**Ajouter une intention personnalisée :**
```python
import re

# Add to RULES
RULES.append((re.compile('translate|翻译', re.I), 'translation'))

# Add capability to catalog
CATALOG['phi-4-mini-cpu']['capabilities'].append('translation')
```

**Activer le suivi des tokens :**
```python
import os
os.environ['SHOW_USAGE'] = '1'
```

### Passer aux modèles GPU

Si vous avez 8 Go+ de VRAM :

1. Dans **Cellule #6**, commenter le catalogue CPU
2. Décommenter le catalogue GPU
3. Charger les modèles GPU :
   ```bash
   foundry model run phi-4-mini
   foundry model run qwen2.5-0.5b
   foundry model run phi-3.5-mini
   ```
4. Redémarrer le noyau et réexécuter le carnet

### Estimation du temps
- **Première exécution :** 5-10 minutes (chargement des modèles)
- **Exécutions suivantes :** 30-60 secondes par test

---

## Variables d'environnement

### Configuration globale

À définir avant de démarrer Jupyter/VS Code :

**Windows (Invite de commandes) :**
```cmd
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:59959/v1
set SHOW_USAGE=1
set RETRY_ON_FAIL=1
```

**Windows (PowerShell) :**
```powershell
$env:FOUNDRY_LOCAL_ENDPOINT="http://localhost:59959/v1"
$env:SHOW_USAGE="1"
$env:RETRY_ON_FAIL="1"
```

**macOS/Linux :**
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://localhost:59959/v1
export SHOW_USAGE=1
export RETRY_ON_FAIL=1
```

### Configuration dans le carnet

À définir au début de tout carnet :

```python
import os

# Foundry Local configuration
os.environ['FOUNDRY_LOCAL_ENDPOINT'] = 'http://localhost:59959/v1'

# Model selection
os.environ['SLM_ALIAS'] = 'phi-4-mini'
os.environ['LLM_ALIAS'] = 'qwen2.5-3b'

# Agent models
os.environ['AGENT_MODEL_PRIMARY'] = 'phi-4-mini'
os.environ['AGENT_MODEL_EDITOR'] = 'qwen2.5-7b'

# Debugging
os.environ['SHOW_USAGE'] = '1'       # Show token usage
os.environ['RETRY_ON_FAIL'] = '1'    # Enable retries
os.environ['RETRY_BACKOFF'] = '2.0'  # Retry delay
```

---

## Commandes courantes

### Gestion du service

```bash
# Start service
foundry service start

# Check status
foundry service status

# Stop service
foundry service stop

# View logs
foundry service logs
```

### Gestion des modèles

```bash
# List all available models in catalog
foundry model catalog

# List loaded models
foundry model ls

# Download a model
foundry model download phi-4-mini

# Load a model
foundry model run phi-4-mini

# Unload a model
foundry model unload phi-4-mini

# Remove a model
foundry model remove phi-4-mini

# Get model info
foundry model info phi-4-mini
```

### Test des points de terminaison

```bash
# Check service health
curl http://localhost:59959/health

# List available models via API
curl http://localhost:59959/v1/models

# Test model completion
curl http://localhost:59959/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "phi-4-mini",
    "messages": [{"role":"user","content":"Hello"}],
    "max_tokens": 50
  }'
```

### Commandes de diagnostic

```bash
# Check everything
foundry --version
foundry service status
foundry model ls
foundry device info

# GPU status (NVIDIA)
nvidia-smi

# NPU status (Qualcomm)
foundry device info
```

---

## Bonnes pratiques

### Avant de démarrer tout carnet

1. **Vérifier que le service est en cours d'exécution :**
   ```bash
   foundry service status
   ```

2. **Vérifier que les modèles sont chargés :**
   ```bash
   foundry model ls
   ```

3. **Redémarrer le noyau du carnet** si vous réexécutez

4. **Effacer tous les résultats** pour une exécution propre

### Gestion des ressources

1. **Utiliser les modèles CPU par défaut** pour la compatibilité
2. **Passer aux modèles GPU** uniquement si vous avez 8 Go+ de VRAM
3. **Fermer les autres applications GPU** avant de lancer
4. **Garder le service actif** entre les sessions de carnets
5. **Surveiller l'utilisation des ressources** avec le Gestionnaire des tâches / nvidia-smi

### Dépannage

1. **Toujours vérifier le service en premier** avant de déboguer le code
2. **Redémarrer le noyau** si vous voyez une configuration obsolète
3. **Réexécuter les cellules de diagnostic** après tout changement
4. **Vérifier que les noms des modèles** correspondent à ceux chargés
5. **Vérifier que le port du point de terminaison** correspond au statut du service

---

## Référence rapide : Alias des modèles

### Modèles courants

| Alias            | Taille | Meilleur usage              | RAM/VRAM | Variantes              |
|------------------|--------|----------------------------|----------|------------------------|
| `phi-4-mini`    | ~4B    | Chat général, résumé       | 4-6 Go   | `-cpu`, `-cuda-gpu`, `-npu` |
| `phi-3.5-mini`  | ~3.5B  | Génération de code         | 3-5 Go   | `-cpu`, `-cuda-gpu`, `-npu` |
| `qwen2.5-3b`    | ~3B    | Tâches générales, efficace | 3-4 Go   | `-cpu`, `-cuda-gpu`         |
| `qwen2.5-1.5b`  | ~1.5B  | Rapide, faible ressource   | 2-3 Go   | `-cpu`, `-cuda-gpu`         |
| `qwen2.5-0.5b`  | ~0.5B  | Classification, minimal    | 1-2 Go   | `-cpu`, `-cuda-gpu`         |

### Nommage des variantes

- **Nom de base** (ex. `phi-4-mini`) : Sélectionne automatiquement la meilleure variante pour votre matériel
- **`-cpu`** : Optimisé pour CPU, fonctionne partout
- **`-cuda-gpu`** : Optimisé pour GPU NVIDIA, nécessite 8 Go+ de VRAM
- **`-npu`** : Optimisé pour NPU Qualcomm, nécessite des pilotes NPU

**Recommandation :** Utilisez les noms de base (sans suffixe) et laissez Foundry Local sélectionner automatiquement la meilleure variante.

---

## Indicateurs de succès

Vous êtes prêt lorsque vous voyez :

✅ `foundry service status` indique "running"  
✅ `foundry model ls` affiche les modèles requis  
✅ Service accessible au bon point de terminaison  
✅ Vérification de santé retourne 200 OK  
✅ Les cellules de diagnostic du carnet sont réussies  
✅ Aucun message d'erreur de connexion dans les résultats  

---

## Obtenir de l'aide

### Documentation
- **Répertoire principal** : https://github.com/microsoft/Foundry-Local
- **SDK Python** : https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **Référence CLI** : https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-cli.md
- **Dépannage** : Voir `troubleshooting.md` dans ce répertoire

### Problèmes GitHub
- https://github.com/microsoft/Foundry-Local/issues
- https://github.com/microsoft/edgeai-for-beginners/issues

---

**Dernière mise à jour :** 8 octobre 2025  
**Version :** Carnets de l'atelier 2.0

---

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction humaine professionnelle. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées résultant de l'utilisation de cette traduction.
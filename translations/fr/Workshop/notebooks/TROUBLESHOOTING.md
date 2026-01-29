# Carnets de l'atelier - Guide de dépannage

## Table des matières

- [Problèmes courants et solutions](../../../../Workshop/notebooks)
- [Problèmes spécifiques à la session 04](../../../../Workshop/notebooks)
- [Problèmes spécifiques à la session 05](../../../../Workshop/notebooks)
- [Problèmes spécifiques à la session 06](../../../../Workshop/notebooks)
- [Problèmes spécifiques au matériel](../../../../Workshop/notebooks)
- [Commandes de diagnostic](../../../../Workshop/notebooks)
- [Obtenir de l'aide](../../../../Workshop/notebooks)

---

## Problèmes courants et solutions

### 🔴 Mémoire CUDA insuffisante

**Message d'erreur :**
```
CUDA failure 2: out of memory
```

**Cause principale :** Le GPU n'a pas assez de VRAM pour charger le modèle.

**Solutions :**

#### Option 1 : Utiliser des variantes CPU (recommandé)
```python
# In your notebook, update the CATALOG to use CPU variants
CATALOG = {
    'phi-4-mini-cpu': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','refactor'],'priority':3},
}
```

#### Option 2 : Utiliser des modèles plus petits sur le GPU
```python
# Use only the smallest model
CATALOG = {
    'qwen2.5-0.5b': {'capabilities':['general','code','summarize','classification'],'priority':1},
}
```

#### Option 3 : Libérer la mémoire GPU
```bash
# Close other GPU-intensive applications
# Check GPU memory usage
nvidia-smi

# Restart Foundry Local service
foundry service stop
foundry service start
```

#### Option 4 : Augmenter la mémoire GPU (si possible)
- Fermez les onglets du navigateur, les éditeurs vidéo ou d'autres applications utilisant le GPU
- Réduisez les effets visuels de Windows
- Utilisez le GPU dédié si vous avez un GPU intégré + dédié

---

### 🔴 APIConnectionError : Erreur de connexion

**Message d'erreur :**
```
APIConnectionError: Connection error
[Retry 1/2] Setup failed for 'phi-4-mini': APIConnectionError: Connection error.
```

**Cause principale :** Le service Foundry Local n'est pas en cours d'exécution ou n'est pas accessible.

**Solutions :**

#### Étape 1 : Vérifier l'état du service
```bash
foundry service status
```

#### Étape 2 : Démarrer le service s'il est arrêté
```bash
foundry service start
```

#### Étape 3 : Vérifier le point de terminaison
```bash
# Check what port the service is using
foundry service status

# Test with curl (adjust port if different)
curl http://localhost:59959/health
curl http://localhost:55769/health
```

#### Étape 4 : Charger les modèles requis
```bash
foundry model run phi-4-mini
foundry model run qwen2.5-3b
foundry model run phi-3.5-mini
```

#### Étape 5 : Redémarrer le noyau du carnet
Après avoir démarré le service et chargé les modèles, redémarrez le noyau du carnet et relancez toutes les cellules.

---

### 🔴 Modèle introuvable dans le catalogue

**Message d'erreur :**
```
ValueError: Model phi-3.5-mini-cpu not found in the catalog.
[ERROR] Model 'phi-4-mini' not found in the catalog
```

**Cause principale :** Le modèle n'est pas téléchargé ou chargé dans Foundry Local.

**Solutions :**

#### Option 1 : Télécharger et charger les modèles
```bash
# List available models
foundry model ls

# Download the model if not present
foundry model download phi-4-mini
foundry model download qwen2.5-3b
foundry model download phi-3.5-mini

# Load the model into memory
foundry model run phi-4-mini
foundry model run qwen2.5-3b
foundry model run phi-3.5-mini
```

#### Option 2 : Utiliser le mode de sélection automatique
Mettez à jour votre CATALOG pour utiliser les noms de modèles de base (sans le suffixe `-cpu`) :

```python
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini': {'capabilities':['code','refactor'],'priority':3},
}
```

Le SDK Foundry Local sélectionnera automatiquement la meilleure variante (CPU, GPU ou NPU) pour votre matériel.

---

### 🔴 HttpResponseError : 500 - Échec du chargement du modèle

**Message d'erreur :**
```
HttpResponseError: 500 - Failed loading model
```

**Cause principale :** Le fichier du modèle est corrompu ou incompatible avec le matériel.

**Solutions :**

#### Retélécharger le modèle
```bash
# Remove corrupted model
foundry model remove phi-3.5-mini

# Download fresh copy
foundry model download phi-3.5-mini
```

#### Utiliser une variante différente
```bash
# Try CPU variant instead
foundry model download phi-3.5-mini-cpu
```

---

### 🔴 ImportError : Aucun module trouvé

**Message d'erreur :**
```
ModuleNotFoundError: No module named 'foundry_local'
```

**Cause principale :** Le package foundry-local-sdk n'est pas installé.

**Solutions :**

```bash
# Install SDK
pip install foundry-local-sdk

# Verify installation
pip show foundry-local-sdk
python -c "from foundry_local import FoundryLocalManager; print('SDK OK')"
```

---

### � Première requête lente

**Symptôme :** La première complétion prend plus de 30 secondes, les requêtes suivantes sont rapides.

**Cause principale :** Comportement normal - le service charge le modèle en mémoire lors de la première requête.

**Solutions :**

#### Précharger les modèles
```bash
# Download and load all models you'll use before running notebooks
foundry model download phi-4-mini
foundry model download qwen2.5-3b
foundry model download phi-3.5-mini

foundry model run phi-4-mini
foundry model run qwen2.5-3b
```

#### Garder le service actif
```bash
# Start service manually and leave it running
foundry service start
```

---

## Problèmes spécifiques à la session 04

### Mauvaise configuration du port

**Problème :** Le carnet se connecte au mauvais port (55769 vs 59959 vs 57127)

**Solution :**

1. Vérifiez quel port Foundry Local utilise :
```bash
foundry service status
# Note the port number displayed
```

2. Mettez à jour la cellule 10 dans le carnet :
```python
ENDPOINT = os.getenv('FOUNDRY_LOCAL_ENDPOINT', 'http://localhost:59959/v1')
# Replace 59959 with your actual port
```

3. Redémarrez le noyau et relancez les cellules 6, 8, 10, 12, 16, 20, 22

---

### Mauvaise sélection de modèle

**Problème :** Le carnet affiche gpt-oss-20b ou qwen2.5-7b au lieu de qwen2.5-3b

**Solution :**

1. Redémarrez le noyau du carnet (efface l'état des variables anciennes)
2. Relancez la cellule 10 (Définir les alias de modèles)
3. Relancez la cellule 12 (Afficher la configuration)
4. **Vérifiez :** La cellule 12 doit afficher `LLM Model: qwen2.5-3b`

---

### Échec de la cellule de diagnostic

**Problème :** La cellule 16 affiche "❌ Foundry Local service not found!"

**Solution :**

1. Vérifiez que le service est en cours d'exécution :
```bash
foundry service status
```

2. Testez le point de terminaison manuellement :
```bash
curl http://localhost:59959/v1/models
```

3. Si curl fonctionne mais pas le carnet :
   - Redémarrez le noyau du carnet
   - Relancez les cellules dans l'ordre : 6, 8, 10, 12, 14, 16

4. Si curl échoue :
   - Démarrez le service : `foundry service start`
   - Chargez les modèles : `foundry model run phi-4-mini` et `foundry model run qwen2.5-3b`

---

### Échec de la vérification préliminaire

**Problème :** La cellule 20 affiche des erreurs de connexion même si le diagnostic a réussi

**Solution :**

1. Vérifiez que les modèles sont chargés :
```bash
foundry model ls
# Should show phi-4-mini and qwen2.5-3b
```

2. Si les modèles manquent :
```bash
foundry model run phi-4-mini
foundry model run qwen2.5-3b
```

3. Relancez la cellule 20 après le chargement des modèles

---

### Échec de la comparaison avec des valeurs None

**Problème :** La cellule 22 se termine mais affiche une latence comme None

**Solution :**

1. Vérifiez que la vérification préliminaire a réussi (Cellule 20)
2. Relancez la cellule 22 - les modèles peuvent avoir besoin de se "réchauffer" lors de la première requête
3. Vérifiez que les deux modèles sont chargés : `foundry model ls`

---

## Problèmes spécifiques à la session 05

### L'agent utilise le mauvais modèle

**Problème :** L'agent n'utilise pas le modèle attendu

**Solution :**

Vérifiez la configuration :
```python
# Check which models are assigned
print(f"Researcher: {researcher.model_id}")
print(f"Editor: {editor.model_id}")
```

Redémarrez le noyau si les modèles sont incorrects.

---

### Dépassement du contexte mémoire

**Problème :** Les réponses de l'agent se dégradent avec le temps

**Solution :** Déjà géré automatiquement - les agents conservent uniquement les 6 derniers messages en mémoire.

---

## Problèmes spécifiques à la session 06

### Confusion entre modèles CPU et GPU

**Problème :** Erreurs CUDA lors de l'utilisation de la configuration par défaut

**Solution :** La configuration par défaut utilise désormais des modèles CPU. Si vous voyez des erreurs CUDA :

1. Vérifiez que vous utilisez le catalogue CPU par défaut :
```python
# Cell should show CPU variants
CATALOG = {
    'phi-4-mini-cpu': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','refactor'],'priority':3},
}
```

2. Redémarrez le noyau et relancez toutes les cellules

---

### Détection d'intention non fonctionnelle

**Problème :** Les invites sont dirigées vers les mauvais modèles

**Solution :**

Testez la détection d'intention :
```python
# Run the intent detection test cell
for prompt in test_prompts:
    intent = detect_intent(prompt)
    print(f"{prompt[:50]}... → {intent}")
```

Mettez à jour les RULES si les modèles doivent être ajustés.

---

## Problèmes spécifiques au matériel

### GPU NVIDIA

**Vérifiez l'état du GPU :**
```bash
nvidia-smi
```

**Problèmes courants :**
- **Pilote obsolète :** Mettez à jour les pilotes NVIDIA
- **Incompatibilité de version CUDA :** Réinstallez Foundry Local
- **Mémoire GPU fragmentée :** Redémarrez le système

### NPU Qualcomm

**Vérifiez l'état du NPU :**
```bash
foundry device info
```

**Problèmes courants :**
- **Pilotes NPU non installés :** Installez les pilotes Qualcomm NPU
- **Variante NPU non disponible :** Utilisez la variante CPU
- **Version de Windows trop ancienne :** Mettez à jour vers la dernière version de Windows 11

### Systèmes uniquement CPU

**Modèles recommandés :**
```python
CATALOG = {
    'qwen2.5-0.5b-cpu': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini-cpu': {'capabilities':['code','general'],'priority':2},
}
```

**Conseils de performance :**
- Utilisez les modèles les plus petits
- Réduisez max_tokens
- Soyez patient pour la première requête

---

## Commandes de diagnostic

### Tout vérifier
```bash
# Service status
foundry service status

# List models
foundry model ls

# Device info
foundry device info

# Version info
foundry --version

# Health check
curl http://localhost:55769/health
```

### En Python
```python
# Check SDK import
try:
    from foundry_local import FoundryLocalManager
    print('✓ SDK imported')
except ImportError as e:
    print(f'✗ SDK import failed: {e}')

# Check service connectivity
from openai import OpenAI

try:
    client = OpenAI(base_url='http://localhost:59959/v1', api_key='test')
    models = client.models.list()
    print(f'✓ Service reachable, {len(list(models.data))} models available')
except Exception as e:
    print(f'✗ Service not reachable: {e}')
```

---

## Obtenir de l'aide

### 1. Vérifiez les journaux
```bash
# Windows
foundry service logs

# Or check Windows Event Viewer
# Application Logs -> Microsoft-FoundryLocal
```

### 2. Problèmes GitHub
- Recherchez les problèmes existants : https://github.com/microsoft/Foundry-Local/issues
- Créez un nouveau problème avec :
  - Message d'erreur (texte complet)
  - Résultat de `foundry service status`
  - Résultat de `foundry --version`
  - Infos GPU/NPU (nvidia-smi, etc.)
  - Étapes pour reproduire

### 3. Documentation
- **Dépôt principal** : https://github.com/microsoft/Foundry-Local
- **SDK Python** : https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **Référence CLI** : https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-cli.md
- **Dépannage** : https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-troubleshooting.md

---

## Liste de vérifications rapides

Quand quelque chose ne fonctionne pas, essayez ces étapes dans l'ordre :

- [ ] Vérifiez que le service est en cours d'exécution : `foundry service status`
- [ ] Redémarrez le service : `foundry service stop && foundry service start`
- [ ] Vérifiez que le modèle existe : `foundry model ls | grep phi-4-mini`
- [ ] Chargez les modèles requis : `foundry model run phi-4-mini`
- [ ] Vérifiez la mémoire GPU : `nvidia-smi` (si NVIDIA)
- [ ] Essayez la variante CPU : Utilisez `phi-4-mini-cpu` au lieu de `phi-4-mini`
- [ ] Redémarrez le noyau du carnet
- [ ] Effacez les sorties du carnet et relancez toutes les cellules
- [ ] Réinstallez le SDK : `pip install --upgrade --force-reinstall foundry-local-sdk`
- [ ] Redémarrez le système (en dernier recours)

---

## Conseils de prévention

### Bonnes pratiques

1. **Vérifiez toujours le service en premier :**
   ```bash
   foundry service status
   ```

2. **Utilisez par défaut les variantes CPU :**
   ```python
   CATALOG = {
       'phi-4-mini-cpu': {...},
       'qwen2.5-0.5b-cpu': {...},
   }
   ```

3. **Préchargez les modèles avant d'exécuter les carnets :**
   ```bash
   foundry model run phi-4-mini
   foundry model run qwen2.5-3b
   ```

4. **Gardez le service actif :**
   - Ne stoppez/démarrez pas le service inutilement
   - Laissez-le fonctionner en arrière-plan entre les sessions

5. **Surveillez les ressources :**
   - Vérifiez la mémoire GPU avant de lancer
   - Fermez les applications GPU inutiles
   - Utilisez le Gestionnaire des tâches / nvidia-smi

6. **Mettez à jour régulièrement :**
   ```bash
   winget upgrade Microsoft.FoundryLocal
   pip install --upgrade foundry-local-sdk
   ```

---

**Dernière mise à jour :** 8 octobre 2025

---

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction humaine professionnelle. Nous ne sommes pas responsables des malentendus ou des interprétations erronées résultant de l'utilisation de cette traduction.
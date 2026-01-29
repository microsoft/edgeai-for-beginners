# Exemple 04 : Applications de chat en production avec Chainlit

Un exemple complet démontrant plusieurs approches pour créer des applications de chat prêtes pour la production en utilisant Microsoft Foundry Local, avec des interfaces web modernes, des réponses en streaming et des technologies de navigateur de pointe.

## Contenu inclus

- **🚀 Application de chat Chainlit** (`app.py`) : Application de chat prête pour la production avec streaming
- **🌐 Démo WebGPU** (`webgpu-demo/`) : Inférence IA basée sur le navigateur avec accélération matérielle
- **🎨 Intégration Open WebUI** (`open-webui-guide.md`) : Interface professionnelle similaire à ChatGPT
- **📚 Notebook éducatif** (`chainlit_app.ipynb`) : Matériel d'apprentissage interactif

## Démarrage rapide

### 1. Application de chat Chainlit

```cmd
# Navigate to Module08 directory
cd Module08

# Start your model
foundry model run phi-4-mini

# Run Chainlit app (using port 8080 to avoid conflicts)
chainlit run samples\04\app.py -w --port 8080
```

Accessible à : `http://localhost:8080`

### 2. Démo WebGPU dans le navigateur

```cmd
# Navigate to WebGPU demo
cd Module08\samples\04\webgpu-demo

# Serve the demo
python -m http.server 5173
```

Accessible à : `http://localhost:5173`

### 3. Configuration Open WebUI

```cmd
# Run Open WebUI with Docker
docker run -d --name open-webui -p 3000:8080 \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-local-key \
  ghcr.io/open-webui/open-webui:main
```

Accessible à : `http://localhost:3000`

## Modèles d'architecture

### Matrice de décision Local vs Cloud

| Scénario | Recommandation | Raison |
|----------|----------------|--------|
| **Données sensibles** | 🏠 Local (Foundry) | Les données ne quittent jamais l'appareil |
| **Raisonnement complexe** | ☁️ Cloud (Azure OpenAI) | Accès à des modèles plus grands |
| **Chat en temps réel** | 🏠 Local (Foundry) | Latence réduite, réponses plus rapides |
| **Analyse de documents** | 🔄 Hybride | Extraction locale, analyse dans le cloud |
| **Génération de code** | 🏠 Local (Foundry) | Confidentialité + modèles spécialisés |
| **Tâches de recherche** | ☁️ Cloud (Azure OpenAI) | Nécessite une base de connaissances étendue |

### Comparaison des technologies

| Technologie | Cas d'utilisation | Avantages | Inconvénients |
|-------------|--------------------|-----------|---------------|
| **Chainlit** | Développeurs Python, prototypage rapide | Configuration facile, support du streaming | Limité à Python |
| **WebGPU** | Confidentialité maximale, scénarios hors ligne | Natif au navigateur, aucun serveur requis | Taille de modèle limitée |
| **Open WebUI** | Déploiement en production, équipes | Interface professionnelle, gestion des utilisateurs | Nécessite Docker |

## Prérequis

- **Foundry Local** : Installé et en cours d'exécution ([Télécharger](https://aka.ms/foundry-local-installer))
- **Python** : Version 3.10+ avec environnement virtuel
- **Modèle** : Au moins un modèle chargé (`foundry model run phi-4-mini`)
- **Navigateur** : Chrome/Edge avec support WebGPU pour les démos
- **Docker** : Pour Open WebUI (optionnel)

## Installation et configuration

### 1. Configuration de l'environnement Python

```cmd
# Navigate to Module08 directory
cd Module08

# Create and activate virtual environment
py -m venv .venv
.venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Configuration de Foundry Local

```cmd
# Verify Foundry Local installation
foundry --version

# Start the service
foundry service start

# Load a model
foundry model run phi-4-mini

# Verify model is running
foundry service ps
```

## Applications d'exemple

### Application de chat Chainlit

**Caractéristiques :**
- 🚀 **Streaming en temps réel** : Les tokens apparaissent au fur et à mesure de leur génération
- 🛡️ **Gestion robuste des erreurs** : Dégradation et récupération en douceur
- 🎨 **Interface moderne** : Interface de chat professionnelle prête à l'emploi
- 🔧 **Configuration flexible** : Variables d'environnement et détection automatique
- 📱 **Design réactif** : Fonctionne sur ordinateurs et appareils mobiles

**Démarrage rapide :**
```cmd
# Run with default settings (recommended)
chainlit run samples\04\app.py -w --port 8080

# Use specific model
set MODEL=qwen2.5-7b
chainlit run samples\04\app.py -w --port 8080

# Manual endpoint configuration
set BASE_URL=http://localhost:51211
set API_KEY=your-api-key
chainlit run samples\04\app.py -w --port 8080
```

### Démo WebGPU dans le navigateur

**Caractéristiques :**
- 🌐 **IA native au navigateur** : Aucun serveur requis, fonctionne entièrement dans le navigateur
- ⚡ **Accélération WebGPU** : Accélération matérielle lorsque disponible
- 🔒 **Confidentialité maximale** : Les données ne quittent jamais votre appareil
- 🎯 **Installation zéro** : Fonctionne dans tout navigateur compatible
- 🔄 **Fallback en douceur** : Bascule sur le CPU si WebGPU n'est pas disponible

**Exécution :**
```cmd
cd samples\04\webgpu-demo
python -m http.server 5173
# Open http://localhost:5173
```

### Intégration Open WebUI

**Caractéristiques :**
- 🎨 **Interface similaire à ChatGPT** : UI professionnelle et familière
- 👥 **Support multi-utilisateurs** : Comptes utilisateurs et historique des conversations
- 📁 **Traitement de fichiers** : Téléchargement et analyse de documents
- 🔄 **Changement de modèle** : Commutation facile entre différents modèles
- 🐳 **Déploiement Docker** : Configuration prête pour la production en conteneur

**Configuration rapide :**
```cmd
docker run -d --name open-webui -p 3000:8080 \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-local-key \
  ghcr.io/open-webui/open-webui:main
```

## Références de configuration

### Variables d'environnement

| Variable | Description | Valeur par défaut | Exemple |
|----------|-------------|-------------------|---------|
| `MODEL` | Alias du modèle à utiliser | `phi-4-mini` | `qwen2.5-7b` |
| `BASE_URL` | Point de terminaison Foundry Local | Détecté automatiquement | `http://localhost:51211` |
| `API_KEY` | Clé API (optionnelle pour local) | `""` | `your-api-key` |

## Résolution des problèmes

### Problèmes courants

**Application Chainlit :**

1. **Service non disponible :**
   ```cmd
   # Check Foundry Local status
   foundry service status
   foundry service ps
   
   # Validate API endpoint (note: port 51211)
   curl http://localhost:51211/v1/models
   ```

2. **Conflits de port :**
   ```cmd
   # Check what's using port 8080
   netstat -ano | findstr :8080
   
   # Use different port if needed
   chainlit run samples\04\app.py -w --port 3000
   ```

3. **Problèmes d'environnement Python :**
   ```cmd
   # Verify correct interpreter in VS Code
   # Ctrl+Shift+P → Python: Select Interpreter
   # Choose: Module08/.venv/Scripts/python.exe
   
   # Reinstall dependencies
   pip install -r requirements.txt
   ```

**Démo WebGPU :**

1. **WebGPU non pris en charge :**
   - Mettez à jour vers Chrome/Edge 113+
   - Activez WebGPU : `chrome://flags/#enable-unsafe-webgpu`
   - Vérifiez le statut GPU : `chrome://gpu`
   - La démo basculera automatiquement sur le CPU

2. **Erreurs de chargement de modèle :**
   - Assurez-vous d'avoir une connexion internet pour télécharger le modèle
   - Vérifiez la console du navigateur pour les erreurs CORS
   - Vérifiez que vous servez via HTTP (pas file://)

**Open WebUI :**

1. **Connexion refusée :**
   ```cmd
   # Check Docker is running
   docker --version
   
   # Check container status
   docker ps | findstr open-webui
   
   # View container logs
   docker logs open-webui
   ```

2. **Modèles non affichés :**
   ```cmd
   # Verify Foundry Local endpoint
   curl http://localhost:51211/v1/models
   
   # Restart Open WebUI
   docker restart open-webui
   ```

### Liste de validation

```cmd
# ✅ 1. Foundry Local Setup
foundry --version                    # Should show version
foundry service status               # Should show "running"
foundry model list                   # Should show loaded models
curl http://localhost:51211/v1/models  # Should return JSON

# ✅ 2. Python Environment  
python --version                     # Should be 3.10+
pip list | findstr chainlit         # Should show chainlit package
pip list | findstr openai           # Should show openai package

# ✅ 3. Application Testing
chainlit run samples\04\app.py -w --port 8080  # Should open browser
# Test WebGPU demo at localhost:5173
# Test Open WebUI at localhost:3000
```

## Utilisation avancée

### Optimisation des performances

**Chainlit :**
- Utilisez le streaming pour une meilleure perception des performances
- Implémentez le pooling de connexions pour une haute concurrence
- Mettez en cache les réponses des modèles pour les requêtes répétées
- Surveillez l'utilisation de la mémoire avec des historiques de conversation volumineux

**WebGPU :**
- Utilisez WebGPU pour une confidentialité et une vitesse maximales
- Implémentez la quantification des modèles pour des modèles plus petits
- Utilisez les Web Workers pour le traitement en arrière-plan
- Mettez en cache les modèles compilés dans le stockage du navigateur

**Open WebUI :**
- Utilisez des volumes persistants pour l'historique des conversations
- Configurez des limites de ressources pour le conteneur Docker
- Implémentez des stratégies de sauvegarde pour les données utilisateur
- Configurez un proxy inverse pour la terminaison SSL

### Modèles d'intégration

**Hybride Local/Cloud :**
```python
# Route based on complexity and privacy requirements
async def intelligent_routing(prompt: str, metadata: dict):
    if metadata.get("contains_pii"):
        return await foundry_local_completion(prompt)  # Privacy-sensitive
    elif len(prompt.split()) > 200:
        return await azure_openai_completion(prompt)   # Complex reasoning
    else:
        return await foundry_local_completion(prompt)  # Default local
```

**Pipeline multi-modal :**
```python
# Combine different AI capabilities
async def analyze_document(file_path: str):
    # 1. OCR with WebGPU (browser-based)
    text = await webgpu_ocr(file_path)
    
    # 2. Analysis with Foundry Local (private)
    summary = await foundry_local_analyze(text)
    
    # 3. Enhancement with cloud (if needed)
    if summary.confidence < 0.8:
        summary = await azure_openai_enhance(summary)
    
    return summary
```

## Déploiement en production

### Considérations de sécurité

- **Clés API** : Utilisez des variables d'environnement, ne les codez jamais en dur
- **Réseau** : Utilisez HTTPS en production, envisagez un VPN pour l'accès en équipe
- **Contrôle d'accès** : Implémentez l'authentification pour Open WebUI
- **Confidentialité des données** : Auditez les données locales vs celles envoyées au cloud
- **Mises à jour** : Gardez Foundry Local et les conteneurs à jour

### Surveillance et maintenance

- **Vérifications de santé** : Implémentez la surveillance des points de terminaison
- **Journalisation** : Centralisez les journaux de tous les composants
- **Métriques** : Suivez les temps de réponse, les taux d'erreur, l'utilisation des ressources
- **Sauvegarde** : Sauvegarde régulière des données de conversation et des configurations

## Références et ressources

### Documentation
- [Documentation Chainlit](https://docs.chainlit.io/) - Guide complet du framework
- [Documentation Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/) - Documentation officielle de Microsoft
- [ONNX Runtime Web](https://onnxruntime.ai/docs/get-started/with-javascript/web.html) - Intégration WebGPU
- [Documentation Open WebUI](https://docs.openwebui.com/) - Configuration avancée

### Fichiers d'exemple
- [`app.py`](../../../../../Module08/samples/04/app.py) - Application Chainlit en production
- [`chainlit_app.ipynb`](./chainlit_app.ipynb) - Notebook éducatif
- [`webgpu-demo/`](../../../../../Module08/samples/04/webgpu-demo) - Inférence IA basée sur le navigateur
- [`open-webui-guide.md`](./open-webui-guide.md) - Configuration complète Open WebUI

### Exemples associés
- [Documentation Session 4](../../04.CuttingEdgeModels.md) - Guide complet de la session
- [Exemples Foundry Local](https://github.com/microsoft/foundry-local/tree/main/samples) - Exemples officiels

---

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction humaine professionnelle. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées résultant de l'utilisation de cette traduction.
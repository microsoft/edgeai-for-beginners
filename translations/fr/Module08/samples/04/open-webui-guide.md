# Guide d'intégration Open WebUI + Foundry Local

Ce guide explique comment connecter Open WebUI à Microsoft Foundry Local pour obtenir une interface professionnelle de type ChatGPT alimentée par vos modèles d'IA locaux.

## Vue d'ensemble

Open WebUI offre une interface de chat moderne et conviviale pouvant se connecter à n'importe quelle API compatible OpenAI. En le connectant à Foundry Local, vous bénéficiez de :

- **Interface professionnelle** : Une interface de type ChatGPT avec un design moderne
- **Confidentialité locale** : Tout le traitement se fait sur votre appareil
- **Changement de modèle** : Passage facile entre différents modèles locaux
- **Historique des conversations** : Historique et contexte de chat persistants
- **Téléchargement de fichiers** : Analyse de documents et traitement de fichiers
- **Personas personnalisés** : Personnalisation des invites système et des rôles

## Prérequis

### Logiciels requis

```cmd
# Verify Foundry Local installation
foundry --version

# Verify Docker installation
docker --version

# Start Foundry Local service
foundry service start
```

### Charger un modèle

```cmd
# List available models
foundry model list

# Load your preferred model
foundry model run phi-4-mini

# Verify model is running
foundry service ps
```

## Configuration rapide (recommandée)

### Étape 1 : Exécuter Open WebUI avec Docker

```cmd
# Pull the latest Open WebUI image
docker pull ghcr.io/open-webui/open-webui:main

# Run Open WebUI connected to Foundry Local
docker run -d \
  --name open-webui \
  -p 3000:8080 \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-local-key \
  -v open-webui-data:/app/backend/data \
  ghcr.io/open-webui/open-webui:main
```

**Windows PowerShell :**
```powershell
docker run -d `
  --name open-webui `
  -p 3000:8080 `
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 `
  -e OPENAI_API_KEY=foundry-local-key `
  -v open-webui-data:/app/backend/data `
  ghcr.io/open-webui/open-webui:main
```

### Étape 2 : Configuration initiale

1. **Ouvrir le navigateur** : Accédez à `http://localhost:3000`
2. **Créer un compte** : Configurez un utilisateur administrateur (le premier utilisateur devient administrateur)
3. **Vérifier la connexion** : Les modèles devraient apparaître automatiquement dans le menu déroulant

### Étape 3 : Tester la connexion

1. Sélectionnez votre modèle dans le menu déroulant (par exemple, "phi-4-mini")
2. Tapez un message de test : "Bonjour ! Pouvez-vous vous présenter ?"
3. Vous devriez voir une réponse en streaming de votre modèle local

## Configuration avancée

### Variables d'environnement

| Variable | Objectif | Valeur par défaut | Exemple |
|----------|----------|-------------------|---------|
| `OPENAI_API_BASE_URL` | Point de terminaison Foundry Local | - | `http://host.docker.internal:51211/v1` |
| `OPENAI_API_KEY` | Clé API (requise mais non utilisée localement) | - | `foundry-local-key` |
| `WEBUI_SECRET_KEY` | Clé de chiffrement de session | générée automatiquement | `your-secret-key` |
| `ENABLE_SIGNUP` | Autoriser l'inscription de nouveaux utilisateurs | `True` | `False` |

### Configuration manuelle (alternative)

Si les variables d'environnement ne fonctionnent pas, configurez manuellement :

1. **Ouvrir les paramètres** : Cliquez sur l'icône des paramètres (engrenage)
2. **Accéder aux connexions** : Paramètres → Connexions → OpenAI
3. **Configurer les détails de l'API** :
   - URL de base de l'API : `http://host.docker.internal:51211/v1`
   - Clé API : `foundry-local-key` (n'importe quelle valeur fonctionne)
4. **Enregistrer et tester** : Cliquez sur "Enregistrer", puis testez avec un modèle

### Stockage persistant des données

Pour conserver les conversations et les paramètres :

```cmd
# Windows - Create data directory
mkdir %USERPROFILE%\openwebui-data

# Run with persistent storage
docker run -d \
  --name open-webui \
  -p 3000:8080 \
  -v "%USERPROFILE%\openwebui-data:/app/backend/data" \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-local-key \
  ghcr.io/open-webui/open-webui:main
```

## Résolution des problèmes

### Problèmes de connexion

**Problème** : "Connexion refusée" ou modèles non chargés

**Solutions** :
```cmd
# 1. Verify Foundry Local is running
foundry service status
foundry service ps

# 2. Test API endpoint directly
curl http://localhost:51211/v1/models

# 3. Check Docker container logs
docker logs open-webui

# 4. Restart Open WebUI container
docker restart open-webui
```

### Modèle non visible

**Problème** : Open WebUI n'affiche aucun modèle dans le menu déroulant

**Étapes de débogage** :
```cmd
# Check if model is loaded in Foundry Local
foundry model list

# Test API response
curl -X GET http://localhost:51211/v1/models \
  -H "Content-Type: application/json"

# Verify correct port (should be 51211 for Foundry Local)
netstat -ano | findstr :51211
```

**Solution** : Assurez-vous que le modèle est correctement chargé :
```cmd
# Stop and restart model
foundry model stop phi-4-mini
foundry model run phi-4-mini

# Wait for model to fully load, then refresh Open WebUI
```

### Problèmes de réseau Docker

**Problème** : `host.docker.internal` ne se résout pas

**Solution pour Windows** :
```cmd
# Use localhost alternative (may need admin privileges)
docker run -d \
  --name open-webui \
  -p 3000:8080 \
  --add-host=host.docker.internal:host-gateway \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-local-key \
  ghcr.io/open-webui/open-webui:main
```

**Alternative** : Trouvez l'adresse IP de votre machine :
```cmd
ipconfig | findstr IPv4
# Use your actual IP instead of host.docker.internal
# Example: http://192.168.1.100:51211/v1
```

### Problèmes de performance

**Réponses lentes** :
1. Vérifiez que le modèle utilise l'accélération GPU : `foundry service ps`
2. Assurez-vous que les ressources système sont suffisantes (RAM/mémoire GPU)
3. Envisagez d'utiliser un modèle plus petit pour les tests

**Problèmes de mémoire** :
```cmd
# Check Docker container memory usage
docker stats open-webui

# Restart Docker if needed
docker restart open-webui
```

## Guide d'utilisation

### Chat de base

1. **Sélectionner un modèle** : Choisissez dans le menu déroulant (affiche les modèles Foundry Local)
2. **Saisir un message** : Utilisez le champ de texte en bas
3. **Envoyer** : Appuyez sur Entrée ou cliquez sur le bouton Envoyer
4. **Voir la réponse** : Observez la réponse en streaming en temps réel

### Fonctionnalités avancées

**Téléchargement de fichiers** :
1. Cliquez sur l'icône trombone
2. Téléchargez un document (PDF, TXT, etc.)
3. Posez des questions sur le contenu
4. Le modèle analysera et répondra en fonction du document

**Prompts système personnalisés** :
1. Paramètres → Personnalisation
2. Configurez un prompt système personnalisé
3. Crée une personnalité/comportement AI cohérent

**Gestion des conversations** :
- **Nouveau chat** : Cliquez sur "+" pour démarrer une nouvelle conversation
- **Historique des chats** : Accédez aux conversations précédentes depuis la barre latérale
- **Exporter** : Téléchargez l'historique des chats au format texte/JSON

**Comparaison de modèles** :
1. Ouvrez plusieurs onglets de navigateur sur le même Open WebUI
2. Sélectionnez différents modèles dans chaque onglet
3. Comparez les réponses aux mêmes prompts

### Modèles d'intégration

**Flux de travail de développement** :
```cmd
# Terminal 1: Start Foundry Local with development model
foundry model run phi-4-mini

# Terminal 2: Start Open WebUI for testing
docker run --rm -p 3000:8080 \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=dev-key \
  ghcr.io/open-webui/open-webui:main

# Terminal 3: Test API directly for debugging
curl -X POST http://localhost:51211/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"model":"phi-4-mini","messages":[{"role":"user","content":"test"}]}'
```

## Déploiement en production

### Configuration sécurisée

```cmd
# Generate secure secret key
openssl rand -base64 32

# Production deployment with security
docker run -d \
  --name open-webui-prod \
  -p 3000:8080 \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-local-prod \
  -e WEBUI_SECRET_KEY=your-secure-key-here \
  -e ENABLE_SIGNUP=False \
  -v /path/to/secure/storage:/app/backend/data \
  --restart unless-stopped \
  ghcr.io/open-webui/open-webui:main
```

### Configuration multi-utilisateurs

```cmd
# Allow controlled user registration
docker run -d \
  --name open-webui-team \
  -p 3000:8080 \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-team \
  -e ENABLE_SIGNUP=True \
  -e WEBUI_SECRET_KEY=team-secret-key \
  -v team-data:/app/backend/data \
  ghcr.io/open-webui/open-webui:main
```

### Surveillance et journalisation

```cmd
# View real-time logs
docker logs -f open-webui

# Monitor container resources
docker stats open-webui

# Check container health
docker inspect open-webui | grep -i health
```

## Nettoyage

```cmd
# Stop Open WebUI
docker stop open-webui

# Remove container
docker rm open-webui

# Remove data volume (WARNING: deletes all chats)
docker volume rm open-webui-data

# Remove image
docker rmi ghcr.io/open-webui/open-webui:main
```

## Prochaines étapes

### Idées d'amélioration

1. **Modèles personnalisés** : Ajoutez vos propres modèles ajustés à Foundry Local
2. **Intégration API** : Connectez-vous à des API externes via les fonctions Open WebUI
3. **Traitement de documents** : Configurez des pipelines RAG avancés
4. **Multi-modalité** : Configurez des modèles de vision pour l'analyse d'images

### Considérations sur la mise à l'échelle

- **Répartition de charge** : Instances multiples de Foundry Local derrière un proxy inverse
- **Routage des modèles** : Différents modèles pour différents cas d'utilisation
- **Gestion des ressources** : Optimisation de la mémoire GPU pour les utilisateurs simultanés
- **Stratégie de sauvegarde** : Sauvegarde régulière des données de conversation et des configurations

## Références

- [Documentation Open WebUI](https://docs.openwebui.com/)
- [Répertoire GitHub Open WebUI](https://github.com/open-webui/open-webui)
- [Documentation Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [Guide d'installation Docker](https://docs.docker.com/get-docker/)

---


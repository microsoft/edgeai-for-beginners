# Exemple d'utilisation de Foundry Local comme API

Cet exemple montre comment utiliser Microsoft Foundry Local comme service REST API sans dépendre du SDK OpenAI. Il illustre des modèles d'intégration HTTP directe pour un contrôle et une personnalisation maximaux.

## Vue d'ensemble

Basé sur les modèles officiels de Microsoft Foundry Local, cet exemple propose :
- Une intégration directe via REST API avec FoundryLocalManager
- Une implémentation personnalisée du client HTTP
- La gestion des modèles et la surveillance de leur état
- La gestion des réponses en mode streaming et non-streaming
- Une gestion des erreurs et une logique de reprise prêtes pour la production

## Prérequis

1. **Installation de Foundry Local**
   ```powershell
   # Install from GitHub releases
   winget install Microsoft.FoundryLocal
   ```

2. **Dépendances Python**
   ```bash
   pip install foundry-local-sdk requests asyncio aiohttp
   ```

## Architecture

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Your App      │───▶│  REST API Client │───▶│  Foundry Local  │
│                 │    │                  │    │   Service       │
│ - Custom Logic  │    │ - HTTP Requests  │    │ - Model Loading │
│ - Business Rules│    │ - Authentication │    │ - Inference     │
│ - Data Pipeline │    │ - Error Handling │    │ - Health Check  │
└─────────────────┘    └──────────────────┘    └─────────────────┘
```

## Fonctionnalités clés

### 1. **Intégration HTTP directe**
- Appels REST API purs sans dépendances au SDK
- Authentification et en-têtes personnalisés
- Contrôle total sur la gestion des requêtes/réponses

### 2. **Gestion des modèles**
- Chargement et déchargement dynamiques des modèles
- Surveillance de l'état et vérifications de statut
- Collecte de métriques de performance

### 3. **Modèles de production**
- Mécanismes de reprise avec backoff exponentiel
- Circuit breaker pour la tolérance aux pannes
- Journalisation et surveillance complètes

### 4. **Gestion flexible des réponses**
- Réponses en streaming pour les applications en temps réel
- Traitement par lots pour des scénarios à haut débit
- Analyse et validation personnalisées des réponses

## Exemples d'utilisation

### Intégration API de base
```python
from api_client import FoundryAPIClient

# Initialize the API client
client = FoundryAPIClient()

# Simple completion
response = await client.complete(
    prompt="Explain quantum computing",
    model="phi-4-mini",
    max_tokens=500
)
print(response.content)
```

### Intégration en streaming
```python
# Stream responses for real-time applications
async for chunk in client.stream_complete(
    prompt="Write a story about AI",
    model="phi-4-mini"
):
    print(chunk.content, end="", flush=True)
```

### Surveillance de l'état
```python
# Check service health
health = await client.health_check()
print(f"Service Status: {health.status}")
print(f"Active Models: {health.loaded_models}")
print(f"Memory Usage: {health.memory_usage}")
```

## Structure des fichiers

```
07/
├── README.md              # This documentation
├── requirements.txt       # Python dependencies
├── api_client.py         # Core API client implementation
├── health_monitor.py     # Health checking and monitoring
├── examples/
│   ├── basic_usage.py    # Simple API integration example
│   ├── streaming.py      # Streaming response example
│   ├── batch_processing.py # Batch processing example
│   └── production.py     # Production-ready implementation
└── tests/
    ├── test_api_client.py    # Unit tests for API client
    └── test_integration.py   # Integration tests
```

## Intégration de Microsoft Foundry Local

Cet exemple suit les modèles officiels de Microsoft :

1. **Intégration SDK** : Utilise `FoundryLocalManager` pour la gestion des services
2. **Points de terminaison REST** : Appels directs à `/v1/chat/completions` et autres
3. **Authentification** : Gestion appropriée des clés API pour les services locaux
4. **Gestion des modèles** : Listing des catalogues, téléchargement et chargement des modèles
5. **Gestion des erreurs** : Codes d'erreur et réponses recommandés par Microsoft

## Mise en route

1. **Installer les dépendances**
   ```bash
   pip install -r requirements.txt
   ```

2. **Exécuter l'exemple de base**
   ```bash
   python examples/basic_usage.py
   ```

3. **Tester le streaming**
   ```bash
   python examples/streaming.py
   ```

4. **Configuration pour la production**
   ```bash
   python examples/production.py
   ```

## Configuration

Variables d'environnement pour la personnalisation :
- `FOUNDRY_MODEL` : Modèle par défaut à utiliser (par défaut : "phi-4-mini")
- `FOUNDRY_TIMEOUT` : Délai d'attente des requêtes en secondes (par défaut : 30)
- `FOUNDRY_RETRIES` : Nombre de tentatives de reprise (par défaut : 3)
- `FOUNDRY_LOG_LEVEL` : Niveau de journalisation (par défaut : "INFO")

## Bonnes pratiques

1. **Gestion des connexions** : Réutiliser les connexions HTTP pour de meilleures performances
2. **Gestion des erreurs** : Implémenter une logique de reprise appropriée avec backoff exponentiel
3. **Surveillance des ressources** : Suivre l'utilisation mémoire et les performances des modèles
4. **Sécurité** : Utiliser une authentification appropriée même pour les services locaux
5. **Tests** : Inclure des tests unitaires et d'intégration

## Dépannage

### Problèmes courants

**Service non démarré**
```bash
# Check Foundry Local status
foundry status

# Start if needed
foundry start
```

**Problèmes de chargement des modèles**
```bash
# List available models
foundry model list

# Download specific model
foundry model download phi-4-mini
```

**Erreurs de connexion**
- Vérifiez que Foundry Local fonctionne sur le bon port
- Vérifiez les paramètres du pare-feu
- Assurez-vous que les en-têtes d'authentification sont corrects

## Optimisation des performances

1. **Pooling des connexions** : Utiliser des objets session pour plusieurs requêtes
2. **Opérations asynchrones** : Exploiter asyncio pour des requêtes concurrentes
3. **Mise en cache** : Mettre en cache les réponses des modèles lorsque c'est approprié
4. **Surveillance** : Suivre les temps de réponse et ajuster les délais d'attente

## Résultats d'apprentissage

Après avoir complété cet exemple, vous comprendrez :
- L'intégration directe via REST API avec Foundry Local
- Les modèles d'implémentation de clients HTTP personnalisés
- La gestion des erreurs et la surveillance prêtes pour la production
- L'architecture des services Microsoft Foundry Local
- Les techniques d'optimisation des performances pour les services IA locaux

## Prochaines étapes

- Explorer l'exemple 08 : Application de chat sous Windows 11
- Tester l'exemple 09 : Orchestration multi-agents
- Découvrir l'exemple 10 : Intégration de Foundry Local comme outils

---


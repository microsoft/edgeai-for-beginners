# Exemple de Chat Windows 11 - Foundry Local

Une application de chat moderne pour Windows 11 intégrant Microsoft Foundry Local avec une interface native élégante. Construite avec Electron et suivant les modèles officiels de Foundry Local de Microsoft.

## Aperçu

Cet exemple montre comment créer une application de chat prête pour la production, exploitant des modèles d'IA locaux via Foundry Local, offrant aux utilisateurs des conversations IA axées sur la confidentialité, sans dépendance au cloud.

## Fonctionnalités

### 🎨 **Design Natif Windows 11**
- Intégration du système Fluent Design
- Effets de matériau Mica et transparence
- Prise en charge des thèmes natifs de Windows 11
- Mise en page réactive pour toutes les tailles d'écran
- Commutation automatique entre les modes sombre/clair

### 🤖 **Intégration de Modèles d'IA**
- Intégration du service Foundry Local
- Prise en charge de plusieurs modèles avec changement à chaud
- Réponses en streaming en temps réel
- Commutation entre modèles locaux et cloud
- Surveillance de la santé et du statut des modèles

### 💬 **Expérience de Chat**
- Indicateurs de frappe en temps réel
- Persistance de l'historique des messages
- Exportation des conversations de chat
- Invites système personnalisées
- Gestion et ramification des conversations

### ⚡ **Caractéristiques de Performance**
- Chargement paresseux et virtualisation
- Rendu optimisé pour les longues conversations
- Préchargement des modèles en arrière-plan
- Gestion efficace de la mémoire
- Animations et transitions fluides

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    Windows 11 Chat App                     │
├─────────────────┬─────────────────┬─────────────────────────┤
│   Electron UI   │   IPC Bridge    │    Foundry Manager      │
│                 │                 │                         │
│ • Fluent Design │ • Secure Comms  │ • Model Loading         │
│ • Chat Interface│ • Event Routing │ • Health Monitoring     │
│ • Settings      │ • State Sync    │ • Performance Tracking │
│ • Themes        │ • Error Handler │ • Resource Management   │
└─────────────────┴─────────────────┴─────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────┐
│               Microsoft Foundry Local Service               │
│                                                             │
│ • Local Model Hosting    • OpenAI API Compatibility        │
│ • Real-time Inference    • Model Catalog Management        │
│ • Streaming Responses    • Health & Status Monitoring      │
└─────────────────────────────────────────────────────────────┘
```

## Prérequis

### Configuration Système
- **OS** : Windows 11 (22H2 ou version ultérieure recommandée)
- **RAM** : Minimum 8 Go, 16 Go+ recommandé pour les modèles plus grands
- **Stockage** : 10 Go+ d'espace libre pour les modèles
- **GPU** : Optionnel mais recommandé pour une inférence plus rapide

### Dépendances Logicielles
- **Node.js** : v18.0.0 ou version ultérieure
- **Foundry Local** : Dernière version de Microsoft
- **Git** : Pour le clonage et le développement

## Installation

### 1. Installer Foundry Local
```powershell
# Download from GitHub releases and install
winget install Microsoft.FoundryLocal

# Verify installation
foundry --version
```

### 2. Cloner et Configurer
```bash
# Navigate to sample directory
cd Module08/samples/08

# Install dependencies
npm install

# Install Electron if not global
npm install -g electron
```

### 3. Configurer l'Environnement
```powershell
# Optional: Set cloud model credentials for hybrid mode
$env:AZURE_OPENAI_KEY="your-api-key"
$env:AZURE_OPENAI_ENDPOINT="your-endpoint"
$env:AZURE_OPENAI_MODEL="gpt-4"
```

### 4. Exécuter l'Application
```bash
# Development mode
npm start

# Production build
npm run build
npm run dist
```

## Structure du Projet

```
08/
├── README.md                 # This documentation
├── package.json             # Project dependencies and scripts
├── electron.js              # Main Electron process
├── preload.js              # Secure preload script
├── src/
│   ├── index.html          # Main application UI
│   ├── styles/
│   │   ├── fluent.css      # Windows 11 Fluent Design
│   │   ├── chat.css        # Chat interface styles
│   │   └── themes.css      # Light/Dark theme support
│   ├── scripts/
│   │   ├── app.js          # Main application logic
│   │   ├── chat.js         # Chat functionality
│   │   ├── models.js       # Model management
│   │   ├── settings.js     # Settings and preferences
│   │   └── utils.js        # Utility functions
│   └── assets/
│       ├── icons/          # Application icons
│       ├── sounds/         # Notification sounds
│       └── images/         # UI images and illustrations
├── foundry/
│   ├── manager.js          # Foundry Local integration
│   └── health.js           # Health monitoring
└── build/
    ├── icon.ico            # Windows application icon
    └── installer.nsi       # NSIS installer script
```

## Exploration des Fonctionnalités Clés

### Intégration Windows 11

**Système Fluent Design**
- Matériaux de fond Mica
- Effets de transparence en acrylique
- Coins arrondis et espacement moderne
- Palette de couleurs native de Windows 11
- Jetons de couleur sémantiques pour l'accessibilité

**Fonctionnalités Natives de Windows**
- Intégration de la liste de raccourcis pour les chats récents
- Notifications Windows pour les nouveaux messages
- Progression dans la barre des tâches pour les opérations de modèle
- Intégration dans la barre système avec actions rapides
- Prise en charge de l'authentification Windows Hello

### Gestion des Modèles d'IA

**Modèles Locaux**
```javascript
// Automatic model discovery and loading
const models = await foundryManager.discoverModels();
await foundryManager.loadModel('phi-4-mini');

// Model health monitoring
const health = await foundryManager.checkHealth();
console.log(`Model Status: ${health.status}`);
console.log(`Memory Usage: ${health.memoryUsage}MB`);
```

**Prise en Charge Hybride Cloud/Local**
```javascript
// Seamless switching between local and cloud models
if (useCloudModel) {
    await chatManager.switchToCloud('gpt-4');
} else {
    await chatManager.switchToLocal('phi-4-mini');
}
```

### Fonctionnalités de l'Interface de Chat

**Streaming en Temps Réel**
- Affichage des réponses token par token
- Animations de frappe fluides
- Requêtes annulables
- Indicateurs de frappe et statut

**Gestion des Conversations**
- Historique de chat persistant
- Exportation/importation des conversations
- Recherche et filtrage des messages
- Ramification des conversations
- Invites système personnalisées par conversation

**Accessibilité**
- Navigation complète au clavier
- Compatibilité avec les lecteurs d'écran
- Prise en charge du mode contraste élevé
- Tailles de police personnalisables
- Intégration de la saisie vocale

## Exemples d'Utilisation

### Intégration de Chat Basique
```javascript
// Initialize the chat system
const chat = new ChatManager({
    foundryEndpoint: 'http://localhost:5273',
    defaultModel: 'phi-4-mini',
    streaming: true
});

// Send a message
const response = await chat.sendMessage({
    content: 'Explain quantum computing',
    model: 'phi-4-mini',
    systemPrompt: 'You are a helpful physics teacher.'
});

// Handle streaming responses
chat.on('chunk', (chunk) => {
    appendMessageChunk(chunk.content);
});
```

### Gestion des Modèles
```javascript
// Load a new model
await modelManager.loadModel('qwen2.5-coder-0.5b', {
    showProgress: true,
    autoStart: true
});

// Monitor model performance
modelManager.on('performance', (metrics) => {
    updatePerformanceUI(metrics);
});

// Switch models mid-conversation
await chat.switchModel('phi-4-mini', {
    preserveContext: true
});
```

### Paramètres et Personnalisation
```javascript
// Configure chat behavior
const settings = {
    theme: 'system', // auto, light, dark
    model: 'phi-4-mini',
    streaming: true,
    maxTokens: 1000,
    temperature: 0.7,
    systemPrompt: 'You are a helpful assistant.'
};

await settingsManager.updateSettings(settings);
```

## Options de Configuration

### Paramètres de l'Application
- **Thème** : Mode automatique, clair, sombre
- **Modèle** : Sélection de modèle par défaut
- **Performance** : Paramètres d'inférence
- **Confidentialité** : Politiques de conservation des données
- **Notifications** : Alertes de messages
- **Raccourcis** : Raccourcis clavier

### Paramètres de Chat
- **Streaming** : Activer/désactiver les réponses en temps réel
- **Longueur du Contexte** : Mémoire de conversation
- **Température** : Créativité des réponses
- **Max Tokens** : Limites de longueur des réponses
- **Invites Système** : Comportement par défaut de l'assistant

### Paramètres de Modèle
- **Téléchargement Automatique** : Mises à jour automatiques des modèles
- **Taille du Cache** : Limites de stockage des modèles locaux
- **Mode Performance** : Préférences CPU vs GPU
- **Vérifications de Santé** : Intervalles de surveillance

## Développement

### Construction à partir de la Source
```bash
# Install development dependencies
npm install

# Run in development mode
npm run dev

# Build for production
npm run build

# Create installer
npm run dist
```

### Débogage
```bash
# Enable debug mode
set DEBUG=foundry-chat:*
npm start

# View developer tools
# Press F12 in the application
```

### Tests
```bash
# Run unit tests
npm test

# Run integration tests
npm run test:integration

# Run end-to-end tests
npm run test:e2e
```

## Optimisation des Performances

### Gestion de la Mémoire
- Virtualisation efficace des messages
- Collecte automatique des déchets
- Surveillance de la mémoire des modèles
- Nettoyage des ressources à la sortie

### Optimisation du Rendu
- Défilement virtuel pour les longues conversations
- Chargement paresseux de l'historique des messages
- Mises à jour optimisées React/DOM
- Animations accélérées par GPU

### Optimisation Réseau
- Regroupement des connexions
- Regroupement des requêtes
- Logique de reprise automatique
- Prise en charge du mode hors ligne

## Considérations de Sécurité

### Confidentialité des Données
- Architecture locale en priorité
- Pas de transmission de données cloud (mode local)
- Stockage des conversations crypté
- Gestion sécurisée des identifiants

### Sécurité de l'Application
- Processus de rendu en sandbox
- Politique de sécurité de contenu (CSP)
- Pas d'exécution de code à distance
- Communication IPC sécurisée

## Dépannage

### Problèmes Courants

**Foundry Local ne démarre pas**
```powershell
# Check service status
foundry status

# Restart service
foundry restart

# Check logs
foundry logs
```

**Échecs de Chargement des Modèles**
- Vérifiez l'espace disque disponible
- Vérifiez la connexion Internet pour les téléchargements
- Assurez-vous que les pilotes GPU sont à jour
- Essayez différentes variantes de modèles

**Problèmes de Performance**
- Surveillez les ressources système
- Ajustez les paramètres du modèle
- Activez l'accélération matérielle
- Fermez les autres applications gourmandes en ressources

### Mode Débogage
Activez la journalisation de débogage en définissant des variables d'environnement :
```powershell
$env:DEBUG="foundry:*"
$env:FOUNDRY_LOG_LEVEL="debug"
```

## Contribution

### Configuration de Développement
1. Forkez le dépôt
2. Créez une branche de fonctionnalité
3. Installez les dépendances : `npm install`
4. Apportez des modifications et testez
5. Soumettez une pull request

### Style de Code
- Configuration ESLint fournie
- Prettier pour le formatage du code
- TypeScript pour la sécurité des types
- Commentaires JSDoc pour la documentation

## Résultats d'Apprentissage

Après avoir complété cet exemple, vous comprendrez :

1. **Développement Natif Windows 11**
   - Implémentation du système Fluent Design
   - Intégration native de Windows
   - Bonnes pratiques de sécurité avec Electron

2. **Intégration de Modèles d'IA**
   - Architecture du service Foundry Local
   - Gestion du cycle de vie des modèles
   - Surveillance et optimisation des performances

3. **Systèmes de Chat en Temps Réel**
   - Gestion des réponses en streaming
   - Gestion de l'état des conversations
   - Modèles d'expérience utilisateur

4. **Développement d'Applications de Production**
   - Gestion des erreurs et récupération
   - Optimisation des performances
   - Considérations de sécurité
   - Stratégies de test

## Prochaines Étapes

- **Exemple 09** : Système d'Orchestration Multi-Agent
- **Exemple 10** : Intégration de Foundry Local comme Outils
- **Sujets Avancés** : Ajustement personnalisé des modèles
- **Déploiement** : Modèles de déploiement en entreprise

## Licence

Cet exemple suit la même licence que le projet Microsoft Foundry Local.

---


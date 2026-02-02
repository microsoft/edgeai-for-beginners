# Module 08 : Prise en main de Microsoft Foundry Local - Kit complet pour développeurs

## Aperçu

[Microsoft Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/) représente la nouvelle génération de développement IA en périphérie, offrant aux développeurs des outils puissants pour créer, déployer et étendre des applications IA localement tout en maintenant une intégration fluide avec Azure AI Foundry. Ce module couvre de manière exhaustive Foundry Local, de l'installation au développement avancé d'agents.

**Technologies clés :**
- CLI et SDK Microsoft Foundry Local
- Intégration avec Azure AI Foundry
- Inférence de modèles sur appareil
- Mise en cache et optimisation locale des modèles
- Architectures basées sur des agents

## Objectifs d'apprentissage

En complétant ce module, vous serez capable de :

- **Maîtriser Foundry Local** : Installer, configurer et optimiser pour le développement sous Windows 11
- **Déployer divers modèles** : Exécuter localement les modèles phi, qwen, deepseek et GPT avec des commandes CLI
- **Créer des solutions de production** : Développer des applications IA avec ingénierie avancée des prompts et intégration des données
- **Exploiter l'écosystème open source** : Intégrer des modèles Hugging Face et des contributions communautaires
- **Développer des agents IA** : Construire des agents intelligents avec des capacités de contextualisation et d'orchestration
- **Implémenter des modèles d'entreprise** : Créer des solutions IA modulaires et évolutives pour le déploiement en production

## Structure des sessions

### [1 : Premiers pas avec Foundry Local](./01.FoundryLocalSetup.md)
**Focus** : Installation, configuration CLI, déploiement de modèles et optimisation matérielle

**Sujets clés** : Installation complète • Commandes CLI • Mise en cache des modèles • Accélération matérielle • Déploiement multi-modèles

**Exemples** : [Démarrage rapide REST Chat](./samples/01/README.md) • [Intégration SDK OpenAI](./samples/02/README.md) • [Découverte et benchmarking de modèles](./samples/03/README.md)

**Durée** : 2-3 heures | **Niveau** : Débutant

---

### [2 : Construire des solutions IA avec Azure AI Foundry](./02.AzureAIFoundryIntegration.md)
**Focus** : Ingénierie avancée des prompts, intégration des données et connectivité cloud

**Sujets clés** : Ingénierie des prompts • Intégration des données • Flux de travail Azure • Optimisation des performances • Surveillance

**Exemple** : [Application RAG avec Chainlit](./samples/04/README.md)

**Durée** : 2-3 heures | **Niveau** : Intermédiaire

---

### [3 : Modèles open source avec Foundry Local](./03.OpenSourceModels.md)
**Focus** : Intégration Hugging Face, stratégies BYOM et modèles communautaires

**Sujets clés** : Intégration Hugging Face • Apportez votre propre modèle • Insights Model Mondays • Contributions communautaires • Sélection de modèles

**Exemple** : [Orchestration multi-agents](./samples/05/README.md)

**Durée** : 2-3 heures | **Niveau** : Intermédiaire

---

### [4 : Explorer les modèles de pointe](./04.CuttingEdgeModels.md)
**Focus** : LLMs vs SLMs, implémentation EdgeAI et démonstrations avancées

**Sujets clés** : Comparaison de modèles • Inférence en périphérie vs cloud • Phi + ONNX Runtime • Application RAG avec Chainlit • Optimisation WebGPU

**Exemple** : [Routeur Models-as-Tools](./samples/06/README.md)

**Durée** : 3-4 heures | **Niveau** : Avancé

---

### [5 : Construire rapidement des agents IA](./05.AIPoweredAgents.md)
**Focus** : Architectures d'agents, prompts système, contextualisation et orchestration

**Sujets clés** : Modèles de conception d'agents • Ingénierie des prompts système • Techniques de contextualisation • Systèmes multi-agents • Déploiement en production

**Exemples** : [Orchestration multi-agents](./samples/05/README.md) • [Système multi-agents avancé](./samples/09/README.md)

**Durée** : 3-4 heures | **Niveau** : Avancé

---

### [6 : Foundry Local - Modèles comme outils](./06.ModelsAsTools.md)
**Focus** : Solutions IA modulaires, mise à l'échelle en entreprise et modèles de production

**Sujets clés** : Modèles comme outils • Déploiement sur appareil • Intégration SDK/API • Architectures d'entreprise • Stratégies de mise à l'échelle

**Exemples** : [Routeur Models-as-Tools](./samples/06/README.md) • [Framework d'outils Foundry](./samples/10/README.md)

**Durée** : 3-4 heures | **Niveau** : Expert

---

### [7 : Modèles d'intégration directe API](./samples/07/README.md)
**Focus** : Intégration API REST pure sans dépendances SDK pour un contrôle maximal

**Sujets clés** : Implémentation client HTTP • Authentification personnalisée • Surveillance de la santé des modèles • Réponses en streaming • Gestion des erreurs en production

**Exemple** : [Client API direct](./samples/07/README.md)

**Durée** : 2-3 heures | **Niveau** : Intermédiaire

---

### [8 : Application de chat native Windows 11](./samples/08/README.md)
**Focus** : Construire des applications de chat modernes natives avec intégration Foundry Local

**Sujets clés** : Développement Electron • Fluent Design System • Intégration native Windows • Streaming en temps réel • Conception d'interface de chat

**Exemple** : [Application de chat Windows 11](./samples/08/README.md)

**Durée** : 3-4 heures | **Niveau** : Avancé

---

### [9 : Orchestration multi-agents avancée](./samples/09/README.md)
**Focus** : Coordination sophistiquée des agents, délégation de tâches spécialisées et workflows collaboratifs IA

**Sujets clés** : Coordination intelligente des agents • Modèles d'appel de fonctions • Communication inter-agents • Orchestration de workflows • Mécanismes d'assurance qualité

**Exemple** : [Système multi-agents avancé](./samples/09/README.md)

**Durée** : 4-5 heures | **Niveau** : Expert

---

### [10 : Foundry Local comme framework d'outils](./samples/10/README.md)
**Focus** : Architecture centrée sur les outils pour intégrer Foundry Local dans des applications et frameworks existants

**Sujets clés** : Intégration LangChain • Fonctions Semantic Kernel • Frameworks API REST • Outils CLI • Intégration Jupyter • Modèles de déploiement en production

**Exemple** : [Framework d'outils Foundry](./samples/10/README.md)

**Durée** : 4-5 heures | **Niveau** : Expert

## Prérequis

### Configuration système
- **Système d'exploitation** : Windows 11 (22H2 ou version ultérieure)
- **Mémoire** : 16 Go de RAM (32 Go recommandés pour les modèles volumineux)
- **Stockage** : 50 Go d'espace libre pour la mise en cache des modèles
- **Matériel** : Appareil avec NPU recommandé (PC Copilot+), GPU optionnel
- **Réseau** : Internet haut débit pour le téléchargement initial des modèles

### Environnement de développement
- Visual Studio Code avec extension AI Toolkit
- Python 3.10+ et pip
- Git pour le contrôle de version
- PowerShell ou Command Prompt
- Azure CLI (optionnel pour l'intégration cloud)

### Connaissances requises
- Compréhension de base des concepts IA/ML
- Familiarité avec la ligne de commande
- Bases de la programmation Python
- Concepts API REST
- Connaissances de base sur les prompts et l'inférence de modèles

## Chronologie du module

**Temps total estimé** : 30-38 heures

| Session | Domaine d'intérêt | Exemples | Temps | Complexité |
|---------|--------------------|----------|-------|------------|
|  1 | Configuration & Bases | 01, 02, 03 | 2-3 heures | Débutant |
|  2 | Solutions IA | 04 | 2-3 heures | Intermédiaire |
|  3 | Open Source | 05 | 2-3 heures | Intermédiaire |
|  4 | Modèles avancés | 06 | 3-4 heures | Avancé |
|  5 | Agents IA | 05, 09 | 3-4 heures | Avancé |
|  6 | Outils d'entreprise | 06, 10 | 3-4 heures | Expert |
|  7 | Intégration API directe | 07 | 2-3 heures | Intermédiaire |
|  8 | Application de chat Windows 11 | 08 | 3-4 heures | Avancé |
|  9 | Multi-agents avancés | 09 | 4-5 heures | Expert |
| 10 | Framework d'outils | 10 | 4-5 heures | Expert |

## Ressources clés

**Documentation officielle :**
- [GitHub Microsoft Foundry Local](https://github.com/microsoft/Foundry-Local) - Code source et exemples officiels
- [Documentation Azure AI Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/) - Guide complet de configuration et d'utilisation
- [Série Model Mondays](https://aka.ms/model-mondays) - Points forts et tutoriels hebdomadaires sur les modèles

**Communauté & Support :**
- [Discussions Foundry Local](https://github.com/microsoft/Foundry-Local/discussions) - Q&A communautaire et demandes de fonctionnalités
- [Communauté des développeurs IA Microsoft](https://techcommunity.microsoft.com/category/artificialintelligence) - Dernières actualités et meilleures pratiques

## Résultats d'apprentissage

En complétant ce module, vous serez en mesure de :

### Maîtrise technique
- **Déployer et gérer** : Installations Foundry Local dans des environnements de développement et de production
- **Intégrer des modèles** : Travailler de manière fluide avec des familles de modèles variées de Microsoft, Hugging Face et sources communautaires
- **Créer des applications** : Développer des applications IA prêtes pour la production avec des fonctionnalités avancées et des optimisations
- **Développer des agents** : Implémenter des agents IA sophistiqués avec contextualisation, raisonnement et intégration d'outils

### Compréhension stratégique
- **Décisions architecturales** : Faire des choix éclairés entre déploiement local et cloud
- **Optimisation des performances** : Optimiser les performances d'inférence selon les configurations matérielles
- **Mise à l'échelle en entreprise** : Concevoir des applications évolutives, des prototypes locaux aux déploiements en entreprise
- **Confidentialité et sécurité** : Implémenter des solutions IA respectueuses de la vie privée avec inférence locale

### Capacités d'innovation
- **Prototypage rapide** : Construire et tester rapidement des concepts d'application IA avec les 10 modèles d'exemples
- **Intégration communautaire** : Exploiter des modèles open source et contribuer à l'écosystème
- **Modèles avancés** : Implémenter des modèles IA de pointe incluant RAG, agents et intégration d'outils
- **Maîtrise des frameworks** : Intégration experte avec LangChain, Semantic Kernel, Chainlit et Electron
- **Déploiement en production** : Déployer des solutions IA évolutives, des prototypes locaux aux systèmes d'entreprise
- **Développement prêt pour l'avenir** : Construire des applications prêtes pour les technologies et modèles IA émergents

## Premiers pas

1. **Configuration de l'environnement** : Assurez-vous d'avoir Windows 11 avec le matériel recommandé (voir Prérequis)
2. **Installer Foundry Local** : Suivez la session 1 pour une installation et une configuration complètes
3. **Exécuter l'exemple 01** : Commencez par une intégration API REST de base pour vérifier la configuration
4. **Progression à travers les exemples** : Complétez les exemples 01-10 pour une maîtrise complète

## Indicateurs de succès

Suivez votre progression à travers les 10 exemples complets :

### Niveau fondamental (Exemples 01-03)
- [ ] Installer et configurer Foundry Local avec succès
- [ ] Compléter l'intégration API REST (Exemple 01)
- [ ] Implémenter la compatibilité SDK OpenAI (Exemple 02)
- [ ] Réaliser la découverte et le benchmarking de modèles (Exemple 03)

### Niveau application (Exemples 04-06)
- [ ] Déployer et exécuter au moins 4 familles de modèles différentes
- [ ] Construire une application de chat RAG fonctionnelle (Exemple 04)
- [ ] Créer un système d'orchestration multi-agents (Exemple 05)
- [ ] Implémenter un routage intelligent de modèles (Exemple 06)

### Niveau intégration avancée (Exemples 07-10)
- [ ] Construire un client API prêt pour la production (Exemple 07)
- [ ] Développer une application de chat native Windows 11 (Exemple 08)
- [ ] Implémenter un système multi-agents avancé (Exemple 09)
- [ ] Créer un framework d'outils complet (Exemple 10)

### Indicateurs de maîtrise
- [ ] Exécuter avec succès les 10 exemples sans erreurs
- [ ] Personnaliser au moins 3 exemples pour des cas d'utilisation spécifiques
- [ ] Déployer 2+ exemples dans des environnements proches de la production
- [ ] Contribuer à des améliorations ou extensions du code des exemples
- [ ] Intégrer les modèles Foundry Local dans des projets personnels/professionnels

## Guide de démarrage rapide - Les 10 exemples

### Configuration de l'environnement (Requis pour tous les exemples)

```powershell
# 1. Clone and navigate to Module08
cd Module08

# 2. Create Python virtual environment
py -m venv .venv
.\.venv\Scripts\activate

# 3. Install base dependencies
pip install -r requirements.txt

# 4. Install Foundry Local (if not already installed)
winget install Microsoft.FoundryLocal

# 5. Verify Foundry Local installation
foundry --version
foundry model list
```

### Exemples fondamentaux (01-06)

**Exemple 01 : Démarrage rapide REST Chat**
```powershell
# Start Foundry Local service
foundry model run phi-4-mini

# Run REST chat demo
python samples/01/chat_quickstart.py
```

**Exemple 02 : Intégration SDK OpenAI**
```powershell
# Ensure model is running
foundry status

# Run SDK demo
python samples/02/sdk_quickstart.py
```

**Exemple 03 : Découverte et benchmarking de modèles**
```powershell
# Run comprehensive model testing
samples/03/list_and_bench.cmd

# Or run individual components
foundry model list --available
foundry model download qwen2.5-0.5b
foundry model benchmark phi-4-mini
```

**Exemple 04 : Application RAG avec Chainlit**
```powershell
# Install Chainlit dependencies
pip install chainlit langchain chromadb

# Start RAG chat application
chainlit run samples/04/app.py -w
# Opens browser at http://localhost:8000
```

**Exemple 05 : Orchestration multi-agents**
```powershell
# Run agent coordinator demo
python -m samples.05.agents.coordinator

# Run specific agent examples
python samples/05/examples/specialists_demo.py
```

**Exemple 06 : Routeur Models-as-Tools**
```powershell
# Configure environment
set BASE_URL=http://localhost:8000
set GENERAL_MODEL=phi-4-mini
set CODE_MODEL=qwen2.5-7b

# Run intelligent router
python samples/06/router.py "Analyze this Python code for performance issues"
```

### Exemples d'intégration avancée (07-10)

**Exemple 07 : Client API direct**
```powershell
# Navigate to sample directory
cd samples/07

# Install additional dependencies
pip install -r requirements.txt

# Run basic API examples
python examples/basic_usage.py

# Try streaming responses
python examples/streaming.py

# Test production patterns
python examples/production.py
```

**Exemple 08 : Application de chat Windows 11**
```powershell
# Navigate to sample directory
cd samples/08

# Install Node.js dependencies
npm install

# Start Electron application
npm start

# Or build for production
npm run build
```

**Exemple 09 : Système multi-agents avancé**
```powershell
# Navigate to sample directory
cd samples/09

# Install agent system dependencies
pip install -r requirements.txt

# Run basic coordination example
python examples/basic_coordination.py

# Try complex workflow
python examples/complex_workflow.py

# Interactive agent demo
python examples/interactive_demo.py
```

**Exemple 10 : Framework d'outils Foundry**
```powershell
# Navigate to sample directory
cd samples/10

# Install framework dependencies
pip install -r requirements.txt

# Run basic tools demo
python examples/basic_tools.py

# Start REST API server
python examples/rest_api_server.py
# API available at http://localhost:8080

# Try CLI application
python examples/cli_application.py --help

# Launch Jupyter notebook
jupyter notebook examples/jupyter_notebook.ipynb

# Test LangChain integration
python examples/langchain_demo.py
```

### Résolution des problèmes courants

**Erreurs de connexion Foundry Local**
```powershell
# Check service status
foundry status

# Restart if needed
foundry restart

# Verify endpoint accessibility
curl http://localhost:5273/v1/models
```

**Problèmes de chargement des modèles**
```powershell
# Check available models
foundry model list --cached

# Download missing models
foundry model download phi-4-mini
foundry model download qwen2.5-0.5b

# Force reload if needed
foundry model unload --all
foundry model run phi-4-mini
```

**Problèmes de dépendances**
```powershell
# Upgrade pip and reinstall
python -m pip install --upgrade pip
pip install -r requirements.txt --force-reinstall

# For Node.js samples
npm cache clean --force
npm install
```

## Résumé
Ce module représente le summum du développement de l'IA de périphérie, en combinant les outils de niveau entreprise de Microsoft avec la flexibilité et l'innovation de l'écosystème open source. En maîtrisant Foundry Local à travers les 10 exemples complets, vous serez à la pointe du développement d'applications d'IA.

**Parcours d'apprentissage complet :**
- **Fondations** (Exemples 01-03) : Intégration des API et gestion des modèles
- **Applications** (Exemples 04-06) : RAG, agents et routage intelligent
- **Avancé** (Exemples 07-10) : Cadres de production et intégration en entreprise

Pour l'intégration avec Azure OpenAI (Session 2), consultez les fichiers README des exemples individuels pour les variables d'environnement requises et les paramètres de version de l'API.

---

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction humaine professionnelle. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées résultant de l'utilisation de cette traduction.
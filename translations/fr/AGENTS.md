# AGENTS.md

> **Guide du développeur pour contribuer à EdgeAI pour les débutants**
> 
> Ce document fournit des informations complètes pour les développeurs, agents IA et contributeurs travaillant avec ce dépôt. Il couvre l'installation, les flux de travail de développement, les tests et les meilleures pratiques.
> 
> **Dernière mise à jour** : 30 octobre 2025 | **Version du document** : 3.0

## Table des matières

- [Aperçu du projet](../..)
- [Structure du dépôt](../..)
- [Prérequis](../..)
- [Commandes d'installation](../..)
- [Flux de travail de développement](../..)
- [Instructions de test](../..)
- [Directives de style de code](../..)
- [Directives pour les pull requests](../..)
- [Système de traduction](../..)
- [Intégration locale de Foundry](../..)
- [Construction et déploiement](../..)
- [Problèmes courants et dépannage](../..)
- [Ressources supplémentaires](../..)
- [Notes spécifiques au projet](../..)
- [Obtenir de l'aide](../..)

## Aperçu du projet

EdgeAI pour les débutants est un dépôt éducatif complet enseignant le développement d'Edge AI avec des modèles de langage réduits (SLMs). Le cours couvre les fondamentaux d'EdgeAI, le déploiement de modèles, les techniques d'optimisation et les implémentations prêtes pour la production en utilisant Microsoft Foundry Local et divers frameworks IA.

**Technologies clés :**
- Python 3.8+ (langage principal pour les exemples AI/ML)
- .NET C# (exemples AI/ML)
- JavaScript/Node.js avec Electron (pour les applications de bureau)
- SDK Microsoft Foundry Local
- Microsoft Windows ML 
- VSCode AI Toolkit
- SDK OpenAI
- Frameworks IA : LangChain, Semantic Kernel, Chainlit
- Optimisation de modèles : Llama.cpp, Microsoft Olive, OpenVINO, Apple MLX

**Type de dépôt :** Dépôt de contenu éducatif avec 8 modules et 10 applications d'exemple complètes

**Architecture :** Parcours d'apprentissage multi-modules avec des exemples pratiques démontrant les modèles de déploiement Edge AI

## Structure du dépôt

```
edgeai-for-beginners/
├── introduction.md          # Course introduction and overview
├── Module01-07/            # Core educational modules (Markdown)
├── Module08/               # Foundry Local toolkit with 10 samples
│   ├── samples/01-06/     # Foundation samples (Python)
│   ├── samples/07/        # API client (Python)
│   ├── samples/08/        # Windows 11 chat app (Electron)
│   └── samples/09-10/     # Advanced multi-agent systems (Python)
├── Workshop/               # Hands-on workshop materials
│   ├── samples/           # Workshop Python samples with utilities
│   │   ├── session01/     # Chat bootstrap samples
│   │   ├── session02-06/  # Progressive workshop sessions
│   │   └── util/          # Workshop utility modules
│   ├── notebooks/         # Jupyter notebook tutorials
│   └── scripts/           # Validation and testing tools
├── translations/          # Multi-language translations (50+ languages)
├── translated_images/     # Localized images
└── imgs/                  # Course images and assets
```

## Prérequis

### Outils requis

- **Python 3.8+** - Pour les exemples AI/ML et les notebooks
- **Node.js 16+** - Pour l'application d'exemple Electron
- **Git** - Pour le contrôle de version
- **Microsoft Foundry Local** - Pour exécuter les modèles IA localement

### Outils recommandés

- **Visual Studio Code** - Avec les extensions Python, Jupyter et Pylance
- **Windows Terminal** - Pour une meilleure expérience en ligne de commande (utilisateurs Windows)
- **Docker** - Pour le développement en conteneur (optionnel)

### Configuration système

- **RAM** : 8 Go minimum, 16 Go+ recommandé pour les scénarios multi-modèles
- **Stockage** : 10 Go+ d'espace libre pour les modèles et les dépendances
- **OS** : Windows 10/11, macOS 11+, ou Linux (Ubuntu 20.04+)
- **Matériel** : CPU avec support AVX2 ; GPU (CUDA, Qualcomm NPU) optionnel mais recommandé

### Connaissances requises

- Compréhension de base de la programmation Python
- Familiarité avec les interfaces en ligne de commande
- Compréhension des concepts AI/ML (pour le développement des exemples)
- Flux de travail Git et processus de pull request

## Commandes d'installation

### Installation du dépôt

```bash
# Clone the repository
git clone https://github.com/microsoft/edgeai-for-beginners.git
cd edgeai-for-beginners

# No build step required - this is primarily an educational content repository
```

### Installation des exemples Python (Module08 et exemples de workshop)

```bash
# Create and activate virtual environment
python -m venv .venv
# On Windows
.venv\Scripts\activate
# On macOS/Linux
source .venv/bin/activate

# Install Foundry Local SDK and dependencies
pip install foundry-local-sdk openai

# Install additional dependencies for Module08 samples
cd Module08
pip install -r requirements.txt

# Install Workshop dependencies
cd ../Workshop
pip install -r requirements.txt
```

### Installation des exemples Node.js (Exemple 08 - Application de chat Windows)

```bash
cd Module08/samples/08
npm install

# Start in development mode
npm run dev

# Build for production
npm run build

# Create installer
npm run dist
```

### Installation de Foundry Local

Foundry Local est requis pour exécuter les exemples. Téléchargez et installez depuis le dépôt officiel :

**Installation :**
- **Windows** : `winget install Microsoft.FoundryLocal`
- **macOS** : `brew tap microsoft/foundrylocal && brew install foundrylocal`
- **Manuel** : Téléchargez depuis [la page des releases](https://github.com/microsoft/Foundry-Local/releases)

**Démarrage rapide :**
```bash
# Run your first model (auto-downloads if needed)
foundry model run phi-4-mini

# List available models
foundry model ls

# Check service status
foundry service status
```

**Remarque** : Foundry Local sélectionne automatiquement la meilleure variante de modèle pour votre matériel (GPU CUDA, NPU Qualcomm ou CPU).

## Flux de travail de développement

### Développement de contenu

Ce dépôt contient principalement du **contenu éducatif en Markdown**. Lors de modifications :

1. Modifiez les fichiers `.md` dans les répertoires de modules appropriés
2. Suivez les modèles de formatage existants
3. Assurez-vous que les exemples de code sont précis et testés
4. Mettez à jour le contenu traduit correspondant si nécessaire (ou laissez l'automatisation s'en charger)

### Développement des applications d'exemple

Pour les exemples Python du Module08 (exemples 01-07, 09-10) :
```bash
cd Module08
python samples/01/chat_quickstart.py "Test message"
```

Pour les exemples Python du workshop :
```bash
cd Workshop/samples/session01
python chat_bootstrap.py "Test message"
```

Pour l'exemple Electron (exemple 08) :
```bash
cd Module08/samples/08
npm run dev  # Development with hot reload
```

### Test des applications d'exemple

Les exemples Python n'ont pas de tests automatisés mais peuvent être validés en les exécutant :
```bash
# Test basic chat functionality
python samples/01/chat_quickstart.py "Hello"

# Test with specific model
set MODEL=phi-4-mini
python samples/02/openai_sdk_client.py
```

L'exemple Electron dispose d'une infrastructure de test :
```bash
cd Module08/samples/08
npm test           # Run unit tests
npm run test:e2e   # Run end-to-end tests
npm run lint       # Check code style
```

## Instructions de test

### Validation du contenu

Le dépôt utilise des flux de travail de traduction automatisés. Aucun test manuel requis pour les traductions.

**Validation manuelle des modifications de contenu :**
1. Vérifiez le rendu Markdown en prévisualisant les fichiers `.md`
2. Vérifiez que tous les liens pointent vers des cibles valides
3. Testez les extraits de code inclus dans la documentation
4. Assurez-vous que les images se chargent correctement

### Test des applications d'exemple

**Module08/exemples/08 (application Electron) dispose de tests complets :**
```bash
cd Module08/samples/08

# Run all tests
npm test

# Run unit tests only
npm test -- --testPathPattern=unit

# Run integration tests
npm run test:integration

# Run E2E tests
npm run test:e2e

# Check test coverage
npm test -- --coverage
```

**Les exemples Python doivent être testés manuellement :**
```bash
# Module08 samples
python samples/01/chat_quickstart.py "Test prompt"
python samples/04/chainlit_rag.py
python samples/09/multi_agent_system.py

# Workshop samples
cd Workshop/samples/session01
python chat_bootstrap.py "Test prompt"

# Use Workshop validation tools
cd Workshop/scripts
python validate_samples.py  # Validate syntax and imports
python test_samples.py      # Run smoke tests
```

## Directives de style de code

### Contenu Markdown

- Utilisez une hiérarchie de titres cohérente (# pour le titre, ## pour les sections principales, ### pour les sous-sections)
- Incluez des blocs de code avec des spécificateurs de langage : ```python, ```bash, ```javascript
- Suivez le formatage existant pour les tableaux, listes et emphases
- Gardez les lignes lisibles (visez ~80-100 caractères, mais pas strict)
- Utilisez des liens relatifs pour les références internes

### Style de code Python

- Suivez les conventions PEP 8
- Utilisez des annotations de type lorsque c'est approprié
- Incluez des docstrings pour les fonctions et classes
- Utilisez des noms de variables significatifs
- Gardez les fonctions ciblées et concises

### Style de code JavaScript/Node.js

```bash
# Electron sample follows ESLint configuration
cd Module08/samples/08
npm run lint        # Check for style issues
npm run lint:fix    # Auto-fix style issues
npm run format      # Format with Prettier
```

**Conventions clés :**
- Configuration ESLint fournie dans l'exemple 08
- Prettier pour le formatage du code
- Utilisez la syntaxe moderne ES6+
- Suivez les modèles existants dans le code

## Directives pour les pull requests

### Flux de contribution

1. **Forkez le dépôt** et créez une nouvelle branche à partir de `main`
2. **Apportez vos modifications** en suivant les directives de style de code
3. **Testez minutieusement** en utilisant les instructions de test ci-dessus
4. **Commitez avec des messages clairs** suivant le format des commits conventionnels
5. **Poussez sur votre fork** et créez une pull request
6. **Répondez aux commentaires** des mainteneurs lors de la revue

### Convention de nommage des branches

- `feature/<module>-<description>` - Pour les nouvelles fonctionnalités ou contenu
- `fix/<module>-<description>` - Pour les corrections de bugs
- `docs/<description>` - Pour les améliorations de documentation
- `refactor/<description>` - Pour le refactoring de code

### Format des messages de commit

Suivez [Conventional Commits](https://www.conventionalcommits.org/) :

```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

**Exemples :**
```
feat(Module08): add intent-based routing notebook
docs(AGENTS): update Foundry Local setup instructions
fix(samples/08): resolve Electron build issue
```

### Format des titres
```
[ModuleXX] Brief description of change
```
ou
```
[Module08/samples/XX] Description for sample changes
```

### Code de conduite

Tous les contributeurs doivent respecter le [Code de conduite Open Source de Microsoft](https://opensource.microsoft.com/codeofconduct/). Veuillez consulter [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) avant de contribuer.

### Avant de soumettre

**Pour les modifications de contenu :**
- Prévisualisez tous les fichiers Markdown modifiés
- Vérifiez que les liens et les images fonctionnent
- Vérifiez les fautes de frappe et les erreurs grammaticales

**Pour les modifications de code des exemples (Module08/exemples/08) :**
```bash
npm run lint
npm test
```

**Pour les modifications des exemples Python :**
- Testez que l'exemple s'exécute correctement
- Vérifiez que la gestion des erreurs fonctionne
- Assurez la compatibilité avec Foundry Local

### Processus de revue

- Les modifications de contenu éducatif sont examinées pour leur précision et leur clarté
- Les exemples de code sont testés pour leur fonctionnalité
- Les mises à jour de traduction sont gérées automatiquement par GitHub Actions

## Système de traduction

**IMPORTANT :** Ce dépôt utilise une traduction automatisée via GitHub Actions.

- Les traductions se trouvent dans le répertoire `/translations/` (50+ langues)
- Automatisées via le workflow `co-op-translator.yml`
- **NE PAS modifier manuellement les fichiers de traduction** - ils seront écrasés
- Modifiez uniquement les fichiers source en anglais dans les répertoires racine et de modules
- Les traductions sont générées automatiquement lors du push vers la branche `main`

## Intégration locale de Foundry

La plupart des exemples du Module08 nécessitent que Microsoft Foundry Local soit en cours d'exécution.

### Installation et configuration

**Installer Foundry Local :**
```bash
# Windows
winget install Microsoft.FoundryLocal

# macOS
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**Installer le SDK Python :**
```bash
pip install foundry-local-sdk openai
```

### Démarrage de Foundry Local
```bash
# Start service and run a model (auto-downloads if needed)
foundry model run phi-3.5-mini

# Or use model aliases for automatic hardware optimization
foundry model run phi-4-mini
foundry model run qwen2.5-0.5b
foundry model run qwen2.5-coder-0.5b

# Check service status
foundry service status

# List available models
foundry model ls
```

### Utilisation du SDK (Python)
```python
from foundry_local import FoundryLocalManager
import openai

# Use model alias for automatic hardware optimization
alias = "phi-4-mini"

# Create manager (auto-starts service and loads model)
manager = FoundryLocalManager(alias)

# Configure OpenAI client for local Foundry service
client = openai.OpenAI(
    base_url=manager.endpoint,
    api_key=manager.api_key
)

# Use the model
response = client.chat.completions.create(
    model=manager.get_model_info(alias).id,
    messages=[{"role": "user", "content": "Hello!"}]
)
```

### Vérification de Foundry Local
```bash
# Service status and endpoint
foundry service status

# List loaded models (REST API)
curl http://localhost:<port>/v1/models

# Note: Port is displayed when running 'foundry service status'
```

### Variables d'environnement pour les exemples

La plupart des exemples utilisent ces variables d'environnement :
```bash
# Foundry Local configuration
# Note: The SDK (FoundryLocalManager) automatically detects endpoint
set MODEL=phi-4-mini  # or phi-3.5-mini, qwen2.5-0.5b, qwen2.5-coder-0.5b
set API_KEY=            # Not required for local usage

# Manual endpoint (if not using SDK)
# Port is shown via 'foundry service status'
set BASE_URL=http://localhost:<port>

# For Azure OpenAI fallback (optional)
set AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
set AZURE_OPENAI_API_KEY=your-api-key
set AZURE_OPENAI_API_VERSION=2024-08-01-preview
```

**Remarque** : Lors de l'utilisation de `FoundryLocalManager`, le SDK gère automatiquement la découverte des services et le chargement des modèles. Les alias de modèles (comme `phi-3.5-mini`) garantissent que la meilleure variante est sélectionnée pour votre matériel.

## Construction et déploiement

### Déploiement de contenu

Ce dépôt est principalement de la documentation - aucun processus de construction requis pour le contenu.

### Construction des applications d'exemple

**Application Electron (Module08/exemples/08) :**
```bash
cd Module08/samples/08

# Development build
npm run dev

# Production build
npm run build

# Create Windows installer
npm run dist

# Create portable executable
npm run pack
```

**Exemples Python :**
Pas de processus de construction - les exemples sont exécutés directement avec l'interpréteur Python.

## Problèmes courants et dépannage

> **Astuce** : Consultez [GitHub Issues](https://github.com/microsoft/edgeai-for-beginners/issues) pour les problèmes connus et leurs solutions.

### Problèmes critiques (bloquants)

#### Foundry Local ne fonctionne pas
**Problème :** Les exemples échouent avec des erreurs de connexion

**Solution :**
```bash
# Check if service is running
foundry service status

# Start service with a model
foundry model run phi-4-mini

# Or explicitly start service
foundry service start

# List loaded models
foundry model ls

# Verify via REST API (port shown in 'foundry service status')
curl http://localhost:<port>/v1/models
```

### Problèmes courants (modérés)

#### Problèmes avec l'environnement virtuel Python
**Problème :** Erreurs d'importation de module

**Solution :**
```bash
# Ensure virtual environment is activated
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt
```

#### Problèmes de construction Electron
**Problème :** Échecs d'installation npm ou de construction

**Solution :**
```bash
cd Module08/samples/08
# Clean install
npm run clean
rm -rf node_modules package-lock.json
npm install
```

### Problèmes de flux de travail (mineurs)

#### Conflits dans le flux de travail de traduction
**Problème :** Conflits de PR de traduction avec vos modifications

**Solution :**
- Modifiez uniquement les fichiers source en anglais
- Laissez le flux de travail de traduction automatisé gérer les traductions
- En cas de conflits, fusionnez `main` dans votre branche après la fusion des traductions

#### Échecs de téléchargement de modèles
**Problème :** Foundry Local échoue à télécharger les modèles

**Solution :**
```bash
# Check internet connectivity
# Clear model cache and retry
foundry model remove <model-alias>
foundry model run <model-alias>

# Check available disk space (models can be 2-16GB)
# Verify firewall settings allow downloads
```

## Ressources supplémentaires

### Parcours d'apprentissage
- **Parcours débutant :** Modules 01-02 (7-9 heures)
- **Parcours intermédiaire :** Modules 03-04 (9-11 heures)
- **Parcours avancé :** Modules 05-07 (12-15 heures)
- **Parcours expert :** Module 08 (8-10 heures)
- **Workshop pratique :** Matériaux de workshop (6-8 heures)

### Contenu clé des modules
- **Module01 :** Fondamentaux d'EdgeAI et études de cas réels
- **Module02 :** Familles et architectures des modèles de langage réduits (SLM)
- **Module03 :** Stratégies de déploiement local et cloud
- **Module04 :** Optimisation de modèles avec plusieurs frameworks (Llama.cpp, Microsoft Olive, OpenVINO, Qualcomm QNN, Apple MLX)
- **Module05 :** SLMOps - opérations en production
- **Module06 :** Agents IA et appels de fonctions
- **Module07 :** Implémentations spécifiques à la plateforme
- **Module08 :** Toolkit Foundry Local avec 10 exemples complets

### Dépendances externes
- [Microsoft Foundry Local](https://github.com/microsoft/Foundry-Local) - Runtime de modèle IA local avec API compatible OpenAI
  - [Documentation](https://github.com/microsoft/Foundry-Local/blob/main/docs/README.md)
  - [SDK Python](https://github.com/microsoft/Foundry-Local/tree/main/sdk/python)
  - [SDK JavaScript](https://github.com/microsoft/Foundry-Local/tree/main/sdk/javascript)
- [Llama.cpp](https://github.com/ggml-org/llama.cpp) - Framework d'optimisation
- [Microsoft Olive](https://microsoft.github.io/Olive/) - Toolkit d'optimisation de modèles
- [OpenVINO](https://docs.openvino.ai/) - Toolkit d'optimisation d'Intel

## Notes spécifiques au projet

### Applications d'exemple du Module08

Le dépôt inclut 10 applications d'exemple complètes :

1. **01-REST Chat Quickstart** - Intégration de base du SDK OpenAI
2. **02-OpenAI SDK Integration** - Fonctionnalités avancées du SDK
3. **03-Model Discovery & Benchmarking** - Outils de comparaison de modèles
4. **04-Chainlit RAG Application** - Génération augmentée par récupération
5. **05-Multi-Agent Orchestration** - Coordination basique des agents
6. **06-Models-as-Tools Router** - Routage intelligent des modèles
7. **07-Direct API Client** - Intégration API bas niveau
8. **08-Windows 11 Chat App** - Application de bureau native Electron
9. **09-Advanced Multi-Agent System** - Orchestration complexe des agents
10. **10-Cadre d'outils Foundry** - Intégration LangChain/Semantic Kernel

### Applications d'exemple du workshop

Le workshop comprend 6 sessions progressives avec des implémentations pratiques :

1. **Session 01** - Démarrage du chat avec l'intégration Foundry Local
2. **Session 02** - Pipeline RAG et évaluation avec RAGAS
3. **Session 03** - Évaluation comparative des modèles open-source
4. **Session 04** - Comparaison et sélection de modèles
5. **Session 05** - Systèmes d'orchestration multi-agents
6. **Session 06** - Routage de modèles et gestion des pipelines

Chaque exemple illustre différents aspects du développement d'IA de pointe avec Foundry Local.

### Considérations sur les performances

- Les SLMs sont optimisés pour un déploiement en périphérie (2-16GB RAM)
- L'inférence locale offre des temps de réponse de 50 à 500ms
- Les techniques de quantification permettent une réduction de taille de 75% avec une rétention de performance de 85%
- Capacités de conversation en temps réel avec des modèles locaux

### Sécurité et confidentialité

- Tout le traitement se fait localement - aucune donnée n'est envoyée au cloud
- Adapté aux applications sensibles à la confidentialité (santé, finance)
- Répond aux exigences de souveraineté des données
- Foundry Local fonctionne entièrement sur du matériel local

## Obtenir de l'aide

### Documentation

- **README principal** : [README.md](README.md) - Aperçu du dépôt et parcours d'apprentissage
- **Guide d'étude** : [STUDY_GUIDE.md](STUDY_GUIDE.md) - Ressources d'apprentissage et calendrier
- **Support** : [SUPPORT.md](SUPPORT.md) - Comment obtenir de l'aide
- **Sécurité** : [SECURITY.md](SECURITY.md) - Signalement des problèmes de sécurité

### Support communautaire

- **Problèmes GitHub** : [Signaler des bugs ou demander des fonctionnalités](https://github.com/microsoft/edgeai-for-beginners/issues)
- **Discussions GitHub** : [Poser des questions et partager des idées](https://github.com/microsoft/edgeai-for-beginners/discussions)
- **Problèmes Foundry Local** : [Problèmes techniques avec Foundry Local](https://github.com/microsoft/Foundry-Local/issues)

### Contact

- **Mainteneurs** : Voir [CODEOWNERS](https://github.com/microsoft/edgeai-for-beginners/blob/main/.github/CODEOWNERS)
- **Problèmes de sécurité** : Suivre la divulgation responsable dans [SECURITY.md](SECURITY.md)
- **Support Microsoft** : Pour un support entreprise, contactez le service client Microsoft

### Ressources supplémentaires

- **Microsoft Learn** : [Parcours d'apprentissage en IA et apprentissage automatique](https://learn.microsoft.com/training/browse/?products=ai-services)
- **Documentation Foundry Local** : [Documentation officielle](https://github.com/microsoft/Foundry-Local/blob/main/docs/README.md)
- **Exemples communautaires** : Consultez [Discussions GitHub](https://github.com/microsoft/edgeai-for-beginners/discussions) pour les contributions de la communauté

---

**Il s'agit d'un dépôt éducatif axé sur l'enseignement du développement d'IA de périphérie. Le principal modèle de contribution consiste à améliorer le contenu éducatif et à ajouter/améliorer des applications d'exemple qui illustrent les concepts d'IA de périphérie.**

---

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction professionnelle humaine. Nous ne sommes pas responsables des malentendus ou des interprétations erronées résultant de l'utilisation de cette traduction.
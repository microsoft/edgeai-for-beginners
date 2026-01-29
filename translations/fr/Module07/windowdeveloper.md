# Guide de développement Windows Edge AI

## Introduction

Bienvenue dans le développement Windows Edge AI - votre guide complet pour créer des applications intelligentes exploitant la puissance de l'IA embarquée grâce à la plateforme Windows AI Foundry de Microsoft. Ce guide est spécialement conçu pour les développeurs Windows souhaitant intégrer des fonctionnalités Edge AI de pointe dans leurs applications tout en tirant parti de l'accélération matérielle complète de Windows.

### Les avantages de Windows AI

Windows AI Foundry représente une plateforme unifiée, fiable et sécurisée qui prend en charge l'ensemble du cycle de vie des développeurs IA - de la sélection et du réglage des modèles à l'optimisation et au déploiement sur des architectures CPU, GPU, NPU et cloud hybride. Cette plateforme démocratise le développement de l'IA en offrant :

- **Abstraction matérielle** : Déploiement transparent sur les technologies AMD, Intel, NVIDIA et Qualcomm
- **Intelligence embarquée** : IA respectueuse de la vie privée fonctionnant entièrement sur le matériel local
- **Performance optimisée** : Modèles pré-optimisés pour les configurations matérielles Windows
- **Prêt pour l'entreprise** : Fonctionnalités de sécurité et de conformité de niveau production

### Windows ML 
Windows Machine Learning (ML) permet aux développeurs C#, C++ et Python d'exécuter des modèles ONNX localement sur des PC Windows via ONNX Runtime, avec une gestion automatique des fournisseurs d'exécution pour différents matériels (CPU, GPU, NPU). [ONNX Runtime](https://onnxruntime.ai/docs/) peut être utilisé avec des modèles provenant de PyTorch, Tensorflow/Keras, TFLite, scikit-learn et d'autres frameworks.


![WindowsML Un diagramme illustrant un modèle ONNX passant par Windows ML pour atteindre ensuite les NPUs, GPUs et CPUs.](https://learn.microsoft.com/en-us/windows/ai/images/winml-diagram.png)

Windows ML fournit une copie partagée de ONNX Runtime pour tout Windows, ainsi que la possibilité de télécharger dynamiquement des fournisseurs d'exécution (EPs).

### Pourquoi choisir Windows pour l'Edge AI ?

**Support matériel universel**  
Windows ML offre une optimisation matérielle automatique dans tout l'écosystème Windows, garantissant que vos applications IA fonctionnent de manière optimale, quelle que soit l'architecture matérielle sous-jacente.

**Runtime IA intégré**  
Le moteur d'inférence Windows ML intégré élimine les exigences de configuration complexes, permettant aux développeurs de se concentrer sur la logique de l'application plutôt que sur les préoccupations d'infrastructure.

**Optimisation Copilot+ PC**  
APIs spécialement conçues pour les appareils Windows de nouvelle génération avec des unités de traitement neuronal (NPUs) dédiées offrant des performances exceptionnelles par watt.

**Écosystème de développeurs**  
Outils riches, y compris l'intégration à Visual Studio, une documentation complète et des applications exemples qui accélèrent les cycles de développement.

## Objectifs d'apprentissage

En suivant ce guide de développement Windows Edge AI, vous maîtriserez les compétences essentielles pour créer des applications IA prêtes pour la production sur la plateforme Windows.

### Compétences techniques fondamentales

**Maîtrise de Windows AI Foundry**  
- Comprendre l'architecture et les composants de la plateforme Windows AI Foundry  
- Naviguer dans le cycle de vie complet du développement IA au sein de l'écosystème Windows  
- Implémenter les meilleures pratiques de sécurité pour les applications IA embarquées  
- Optimiser les applications pour différentes configurations matérielles Windows  

**Expertise en intégration d'API**  
- Maîtriser les APIs Windows AI pour les applications textuelles, visuelles et multimodales  
- Intégrer le modèle linguistique Phi Silica pour la génération de texte et le raisonnement  
- Déployer des capacités de vision par ordinateur en utilisant les APIs de traitement d'image intégrées  
- Personnaliser des modèles pré-entraînés en utilisant des techniques LoRA (Low-Rank Adaptation)  

**Implémentation locale Foundry**  
- Parcourir, évaluer et déployer des modèles linguistiques open-source en utilisant Foundry Local CLI  
- Comprendre l'optimisation et la quantification des modèles pour un déploiement local  
- Implémenter des capacités IA hors ligne fonctionnant sans connectivité Internet  
- Gérer les cycles de vie des modèles et les mises à jour dans des environnements de production  

**Déploiement Windows ML**  
- Intégrer des modèles ONNX personnalisés dans des applications Windows via Windows ML  
- Exploiter l'accélération matérielle automatique sur les architectures CPU, GPU et NPU  
- Implémenter une inférence en temps réel avec une utilisation optimale des ressources  
- Concevoir des applications IA évolutives pour diverses catégories d'appareils Windows  

### Compétences en développement d'applications

**Développement Windows multiplateforme**  
- Créer des applications alimentées par l'IA en utilisant .NET MAUI pour un déploiement universel sur Windows  
- Intégrer des capacités IA dans les applications Win32, UWP et Web progressives  
- Implémenter des conceptions d'interface utilisateur réactives qui s'adaptent aux états de traitement IA  
- Gérer des opérations IA asynchrones avec des modèles d'expérience utilisateur appropriés  

**Optimisation des performances**  
- Profiler et optimiser les performances d'inférence IA sur différentes configurations matérielles  
- Implémenter une gestion efficace de la mémoire pour les grands modèles linguistiques  
- Concevoir des applications qui se dégradent gracieusement en fonction des capacités matérielles disponibles  
- Appliquer des stratégies de mise en cache pour les opérations IA fréquemment utilisées  

**Prêt pour la production**  
- Implémenter une gestion complète des erreurs et des mécanismes de secours  
- Concevoir une télémétrie et un suivi des performances des applications IA  
- Appliquer les meilleures pratiques de sécurité pour le stockage et l'exécution des modèles IA locaux  
- Planifier des stratégies de déploiement pour les applications d'entreprise et grand public  

### Compréhension stratégique et commerciale

**Architecture des applications IA**  
- Concevoir des architectures hybrides optimisant entre le traitement IA local et cloud  
- Évaluer les compromis entre la taille des modèles, la précision et la vitesse d'inférence  
- Planifier des architectures de flux de données qui préservent la confidentialité tout en permettant l'intelligence  
- Implémenter des solutions IA rentables qui évoluent avec les demandes des utilisateurs  

**Positionnement sur le marché**  
- Comprendre les avantages concurrentiels des applications IA natives Windows  
- Identifier les cas d'utilisation où l'IA embarquée offre des expériences utilisateur supérieures  
- Développer des stratégies de mise sur le marché pour les applications Windows enrichies par l'IA  
- Positionner les applications pour tirer parti des avantages de l'écosystème Windows  

## Exemples d'applications SDK Windows

Le SDK Windows App fournit des exemples complets démontrant l'intégration de l'IA dans divers frameworks et scénarios de déploiement. Ces exemples sont des références essentielles pour comprendre les modèles de développement IA sur Windows.

### Exemples Windows AI Foundry

| Exemple | Framework | Domaine d'application | Fonctionnalités clés |
|---------|-----------|-----------------------|----------------------|
| [cs-winui](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsAIFoundry/cs-winui) | C# WinUI 3 | Intégration des APIs Windows AI | Application WinUI complète démontrant les APIs Windows AI, optimisation ARM64, déploiement packagé |

**Technologies clés :**  
- APIs Windows AI  
- Framework WinUI 3  
- Optimisation pour la plateforme ARM64  
- Compatibilité Copilot+ PC  
- Déploiement d'applications packagées  

**Prérequis :**  
- Windows 11 avec Copilot+ PC recommandé  
- Visual Studio 2022  
- Configuration de build ARM64  
- SDK Windows App 1.8.1+  

### Exemples Windows ML

#### Exemples C++

| Exemple | Type | Domaine d'application | Fonctionnalités clés |
|---------|------|-----------------------|----------------------|
| [CppConsoleDesktop](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Application console | Windows ML de base | Découverte EP, options en ligne de commande, compilation de modèles |
| [CppConsoleDesktop.FrameworkDependent](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Application console | Déploiement Framework | Runtime partagé, empreinte de déploiement réduite |
| [CppConsoleDesktop.SelfContained](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Application console | Déploiement autonome | Déploiement autonome, sans dépendances runtime |
| [CppConsoleDll](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | DLL | Utilisation en bibliothèque | WindowsML dans une bibliothèque partagée, gestion de la mémoire |
| [CppResnetBuildDemo](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Démo | Tutoriel ResNet | Conversion de modèles, compilation EP, tutoriel Build 2025 |

#### Exemples C#

**Applications console**

| Exemple | Type | Domaine d'application | Fonctionnalités clés |
|---------|------|-----------------------|----------------------|
| [CSharpConsoleDesktop](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs) | Application console | Intégration C# de base | Utilisation d'aides partagées, interface en ligne de commande |
| [ResnetBuildDemoCS](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs) | Démo | Tutoriel ResNet | Conversion de modèles, compilation EP, tutoriel Build 2025 |

**Applications GUI**

| Exemple | Framework | Domaine d'application | Fonctionnalités clés |
|---------|-----------|-----------------------|----------------------|
| [cs-wpf](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs-wpf) | WPF | GUI de bureau | Classification d'images avec interface WPF |
| [cs-winforms](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs-winforms) | Windows Forms | GUI traditionnelle | Classification d'images avec Windows Forms |
| [cs-winui](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs-winui) | WinUI 3 | GUI moderne | Classification d'images avec interface WinUI 3 |

#### Exemples Python

| Exemple | Langage | Domaine d'application | Fonctionnalités clés |
|---------|---------|-----------------------|----------------------|
| [SqueezeNetPython](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/python) | Python | Classification d'images | Bindings Python WinML, traitement d'images par lot |

### Prérequis des exemples

**Configuration système :**  
- PC Windows 11 exécutant la version 24H2 (build 26100) ou supérieure  
- Visual Studio 2022 avec les charges de travail C++ et .NET  
- SDK Windows App 1.8.1 ou version ultérieure  
- Python 3.10-3.13 pour les exemples Python sur appareils x64 et ARM64  

**Spécifique à Windows AI Foundry :**  
- Copilot+ PC recommandé pour des performances optimales  
- Configuration de build ARM64 pour les exemples Windows AI  
- Identité de package requise (les applications non packagées ne sont plus prises en charge)  

### Flux de travail commun des exemples

La plupart des exemples Windows ML suivent ce modèle standard :

1. **Initialiser l'environnement** - Créer un environnement ONNX Runtime  
2. **Enregistrer les fournisseurs d'exécution** - Découvrir et enregistrer les accélérateurs matériels disponibles (CPU, GPU, NPU)  
3. **Charger le modèle** - Charger le modèle ONNX, éventuellement le compiler pour le matériel cible  
4. **Prétraiter les entrées** - Convertir les images/données au format d'entrée du modèle  
5. **Exécuter l'inférence** - Exécuter le modèle et obtenir les prédictions  
6. **Traiter les résultats** - Appliquer softmax et afficher les principales prédictions  

### Fichiers de modèles utilisés

| Modèle | Objectif | Inclus | Remarques |
|--------|----------|--------|-----------|
| SqueezeNet | Classification d'images légère | ✅ Inclus | Pré-entraîné, prêt à l'emploi |
| ResNet-50 | Classification d'images haute précision | ❌ Nécessite une conversion | Utiliser [AI Toolkit](https://code.visualstudio.com/docs/intelligentapps/modelconversion) pour la conversion |

### Support matériel

Tous les exemples détectent et utilisent automatiquement le matériel disponible :  
- **CPU** - Support universel sur tous les appareils Windows  
- **GPU** - Détection et optimisation automatiques pour le matériel graphique disponible  
- **NPU** - Exploite les unités de traitement neuronal sur les appareils pris en charge (PC Copilot+)  

## Composants de la plateforme Windows AI Foundry

### 1. APIs Windows AI

Les APIs Windows AI offrent des capacités IA prêtes à l'emploi alimentées par des modèles embarqués, optimisées pour l'efficacité et les performances sur les appareils Copilot+ PC avec une configuration minimale requise.

#### Catégories principales d'API

**Modèle linguistique Phi Silica**  
- Modèle linguistique petit mais puissant pour la génération de texte et le raisonnement  
- Optimisé pour l'inférence en temps réel avec une consommation d'énergie minimale  
- Support pour la personnalisation via des techniques LoRA  
- Intégration avec la recherche sémantique Windows et la récupération de connaissances  

**APIs de vision par ordinateur**  
- **Reconnaissance de texte (OCR)** : Extraire du texte des images avec une grande précision  
- **Super résolution d'image** : Agrandir les images en utilisant des modèles IA locaux  
- **Segmentation d'image** : Identifier et isoler des objets spécifiques dans les images  
- **Description d'image** : Générer des descriptions textuelles détaillées pour le contenu visuel  
- **Effacement d'objets** : Supprimer des objets indésirables des images grâce à un remplissage IA  

**Capacités multimodales**  
- **Intégration vision-langage** : Combiner compréhension textuelle et visuelle  
- **Recherche sémantique** : Permettre des requêtes en langage naturel sur du contenu multimédia  
- **Récupération de connaissances** : Construire des expériences de recherche intelligentes avec des données locales  

### 2. Foundry Local

Foundry Local offre aux développeurs un accès rapide à des modèles linguistiques open-source prêts à l'emploi sur Windows Silicon, permettant de parcourir, tester, interagir et déployer des modèles dans des applications locales.

#### Applications exemples Foundry Local

Le [répertoire Foundry Local](https://github.com/microsoft/Foundry-Local/tree/main/samples) fournit des exemples complets dans plusieurs langages de programmation et frameworks, démontrant divers modèles d'intégration et cas d'utilisation.

| Exemple | Langage/Framework | Domaine d'application | Fonctionnalités clés |
|---------|-------------------|-----------------------|----------------------|
| [dotNET/rag](https://github.com/microsoft/Foundry-Local/tree/main/samples/dotNET/rag) | C# / .NET | Implémentation RAG | Intégration Semantic Kernel, stockage vectoriel Qdrant, embeddings JINA, ingestion de documents, chat en streaming |
| [electron/foundry-chat](https://github.com/microsoft/Foundry-Local/tree/main/samples/electron/foundry-chat) | JavaScript / Electron | Application de chat de bureau | Chat multiplateforme, basculement modèle local/cloud, intégration SDK OpenAI, streaming en temps réel |
| [js/hello-foundry-local](https://github.com/microsoft/Foundry-Local/tree/main/samples/js/hello-foundry-local) | JavaScript / Node.js | Intégration de base | Utilisation simple du SDK, initialisation de modèle, fonctionnalité de chat de base |
| [python/hello-foundry-local](https://github.com/microsoft/Foundry-Local/tree/main/samples/python/hello-foundry-local) | Python | Intégration de base | Utilisation du SDK Python, réponses en streaming, API compatible OpenAI |
| [rust/hello-foundry-local](https://github.com/microsoft/Foundry-Local/tree/main/samples/rust/hello-foundry-local) | Rust | Intégration des systèmes | Utilisation du SDK bas niveau, opérations asynchrones, client HTTP reqwest |

#### Catégories d'exemples par cas d'utilisation

**RAG (Génération augmentée par récupération)**
- **dotNET/rag** : Implémentation complète de RAG utilisant Semantic Kernel, la base de données vectorielle Qdrant et les embeddings JINA
- **Architecture** : Ingestion de documents → Fragmentation de texte → Embeddings vectoriels → Recherche de similarité → Réponses contextuelles
- **Technologies** : Microsoft.SemanticKernel, Qdrant.Client, embeddings BERT ONNX, complétion de chat en streaming

**Applications de bureau**
- **electron/foundry-chat** : Application de chat prête pour la production avec basculement entre modèles locaux et cloud
- **Fonctionnalités** : Sélecteur de modèles, réponses en streaming, gestion des erreurs, déploiement multiplateforme
- **Architecture** : Processus principal Electron, communication IPC, scripts de préchargement sécurisés

**Exemples d'intégration SDK**
- **JavaScript (Node.js)** : Interaction de base avec les modèles et réponses en streaming
- **Python** : Utilisation d'une API compatible OpenAI avec streaming asynchrone
- **Rust** : Intégration bas niveau avec reqwest et tokio pour les opérations asynchrones

#### Prérequis pour les exemples Foundry Local

**Configuration système :**
- Windows 11 avec Foundry Local installé
- Node.js v16+ pour les exemples JavaScript/Electron
- .NET 8.0+ pour les exemples C#
- Python 3.10+ pour les exemples Python
- Rust 1.70+ pour les exemples Rust

**Installation :**
```powershell
# Install Foundry Local
winget install Microsoft.FoundryLocal

# Verify installation
foundry --version
foundry model list
```

#### Configuration spécifique aux exemples

**Exemple RAG dotNET :**
```powershell
# Install required packages via NuGet
# Microsoft.SemanticKernel.Connectors.Onnx
# Microsoft.SemanticKernel.Connectors.Qdrant
# Qdrant.Client

# Start Qdrant vector database
docker run -p 6333:6333 qdrant/qdrant

# Run Jupyter notebook
jupyter notebook rag_foundrylocal_demo.ipynb
```

**Exemple de chat Electron :**
```powershell
# Set environment variables for cloud fallback
$env:YOUR_API_KEY="your-cloud-api-key"
$env:YOUR_ENDPOINT="your-cloud-endpoint"
$env:YOUR_MODEL_NAME="your-cloud-model"

# Install dependencies and run
npm install
npm start
```

**Exemples JavaScript/Python/Rust :**
```powershell
# Download model (example with phi-3.5-mini)
foundry model run phi-3.5-mini

# Run respective sample
node src/app.js          # JavaScript
python src/app.py        # Python
cargo run               # Rust
```

#### Fonctionnalités clés

**Catalogue de modèles**
- Collection complète de modèles open-source pré-optimisés
- Modèles optimisés pour les CPU, GPU et NPU pour un déploiement immédiat
- Prise en charge des familles de modèles populaires, notamment Llama, Mistral, Phi, et modèles spécialisés par domaine

**Intégration CLI**
- Interface en ligne de commande pour la gestion et le déploiement des modèles
- Flux de travail automatisés pour l'optimisation et la quantification
- Intégration avec les environnements de développement populaires et les pipelines CI/CD

**Déploiement local**
- Fonctionnement entièrement hors ligne sans dépendances cloud
- Prise en charge des formats et configurations de modèles personnalisés
- Service de modèles efficace avec optimisation matérielle automatique

### 3. Windows ML

Windows ML est la plateforme centrale d'IA et le runtime d'inférence intégré sur Windows, permettant aux développeurs de déployer des modèles personnalisés efficacement sur l'écosystème matériel étendu de Windows.

#### Avantages de l'architecture

**Prise en charge universelle du matériel**
- Optimisation automatique pour les siliciums AMD, Intel, NVIDIA et Qualcomm
- Prise en charge de l'exécution sur CPU, GPU et NPU avec basculement transparent
- Abstraction matérielle éliminant le travail d'optimisation spécifique à la plateforme

**Flexibilité des modèles**
- Prise en charge du format de modèle ONNX avec conversion automatique depuis des frameworks populaires
- Déploiement de modèles personnalisés avec des performances de niveau production
- Intégration avec les architectures d'applications Windows existantes

**Intégration en entreprise**
- Compatible avec les cadres de sécurité et de conformité de Windows
- Prise en charge des outils de déploiement et de gestion en entreprise
- Intégration avec les systèmes de gestion et de surveillance des appareils Windows

## Flux de travail de développement

### Phase 1 : Configuration de l'environnement et des outils

**Préparation de l'environnement de développement**
1. Installer Visual Studio 2022 avec les charges de travail C++ et .NET
2. Installer Windows App SDK 1.8.1 ou version ultérieure
3. Configurer les outils CLI de Windows AI Foundry
4. Configurer l'extension AI Toolkit pour Visual Studio Code
5. Mettre en place des outils de profilage et de surveillance des performances
6. Assurer la configuration de build ARM64 pour l'optimisation des PC Copilot+

**Configuration du dépôt d'exemples**
1. Cloner le [dépôt d'exemples Windows App SDK](https://github.com/microsoft/WindowsAppSDK-Samples)
2. Naviguer vers `Samples/WindowsAIFoundry/cs-winui` pour des exemples d'API Windows AI
3. Naviguer vers `Samples/WindowsML` pour des exemples complets de Windows ML
4. Examiner les [exigences de build](https://learn.microsoft.com/windows/apps/windows-app-sdk/system-requirements) pour vos plateformes cibles

**Exploration de la galerie de développement AI**
- Explorer les applications d'exemple et les implémentations de référence
- Tester les API Windows AI avec des démonstrations interactives
- Examiner le code source pour les meilleures pratiques et les modèles
- Identifier les exemples pertinents pour votre cas d'utilisation spécifique

### Phase 2 : Sélection et intégration des modèles

**Analyse des besoins**
- Définir les besoins fonctionnels pour les capacités d'IA
- Établir les contraintes de performance et les objectifs d'optimisation
- Évaluer les exigences de confidentialité et de sécurité
- Planifier l'architecture de déploiement et les stratégies de mise à l'échelle

**Évaluation des modèles**
- Utiliser Foundry Local pour tester des modèles open-source adaptés à votre cas d'utilisation
- Comparer les API Windows AI avec les exigences des modèles personnalisés
- Évaluer les compromis entre taille de modèle, précision et vitesse d'inférence
- Prototyper des approches d'intégration avec les modèles sélectionnés

### Phase 3 : Développement de l'application

**Intégration principale**
- Implémenter l'intégration des API Windows AI avec une gestion correcte des erreurs
- Concevoir des interfaces utilisateur adaptées aux flux de travail de traitement IA
- Mettre en œuvre des stratégies de mise en cache et d'optimisation pour l'inférence des modèles
- Ajouter la télémétrie et la surveillance des performances des opérations IA

**Tests et validation**
- Tester les applications sur différentes configurations matérielles Windows
- Valider les métriques de performance sous diverses conditions de charge
- Implémenter des tests automatisés pour la fiabilité des fonctionnalités IA
- Réaliser des tests d'expérience utilisateur avec des fonctionnalités améliorées par l'IA

### Phase 4 : Optimisation et déploiement

**Optimisation des performances**
- Profiler les performances des applications sur les configurations matérielles cibles
- Optimiser l'utilisation de la mémoire et les stratégies de chargement des modèles
- Implémenter un comportement adaptatif basé sur les capacités matérielles disponibles
- Affiner l'expérience utilisateur pour différents scénarios de performance

**Déploiement en production**
- Emballer les applications avec les dépendances des modèles IA appropriées
- Implémenter des mécanismes de mise à jour pour les modèles et la logique des applications
- Configurer la surveillance et l'analyse pour les environnements de production
- Planifier des stratégies de déploiement pour les entreprises et les consommateurs

## Exemples d'implémentation pratique

### Exemple 1 : Application de traitement intelligent de documents

Créer une application Windows qui traite des documents en utilisant plusieurs capacités IA :

**Technologies utilisées :**
- Phi Silica pour le résumé de documents et les réponses aux questions
- API OCR pour l'extraction de texte à partir de documents scannés
- API de description d'images pour l'analyse de graphiques et de diagrammes
- Modèles ONNX personnalisés pour la classification de documents

**Approche d'implémentation :**
- Concevoir une architecture modulaire avec des composants IA interchangeables
- Implémenter un traitement asynchrone pour des lots de documents volumineux
- Ajouter des indicateurs de progression et un support d'annulation pour les opérations longues
- Inclure une capacité hors ligne pour le traitement de documents sensibles

### Exemple 2 : Système de gestion d'inventaire pour le commerce de détail

Créer un système d'inventaire alimenté par l'IA pour les applications de commerce de détail :

**Technologies utilisées :**
- Segmentation d'image pour l'identification des produits
- Modèles de vision personnalisés pour la classification des marques et des catégories
- Déploiement Foundry Local de modèles linguistiques spécialisés pour le commerce de détail
- Intégration avec les systèmes de point de vente (POS) et d'inventaire existants

**Approche d'implémentation :**
- Construire une intégration caméra pour la numérisation de produits en temps réel
- Implémenter la reconnaissance de produits par code-barres et visuelle
- Ajouter des requêtes d'inventaire en langage naturel en utilisant des modèles linguistiques locaux
- Concevoir une architecture évolutive pour un déploiement multi-magasins

### Exemple 3 : Assistant de documentation pour le secteur de la santé

Développer un outil de documentation pour le secteur de la santé préservant la confidentialité :

**Technologies utilisées :**
- Phi Silica pour la génération de notes médicales et le support de décision clinique
- OCR pour la numérisation des dossiers médicaux manuscrits
- Modèles linguistiques médicaux personnalisés déployés via Windows ML
- Stockage vectoriel local pour la récupération de connaissances médicales

**Approche d'implémentation :**
- Assurer un fonctionnement entièrement hors ligne pour la confidentialité des patients
- Implémenter la validation et la suggestion de terminologie médicale
- Ajouter une journalisation des audits pour la conformité réglementaire
- Concevoir une intégration avec les systèmes de dossiers médicaux électroniques existants

## Stratégies d'optimisation des performances

### Développement conscient du matériel

**Optimisation NPU**
- Concevoir des applications pour exploiter les capacités NPU sur les PC Copilot+
- Implémenter un basculement gracieux vers GPU/CPU sur les appareils sans NPU
- Optimiser les formats de modèles pour l'accélération spécifique au NPU
- Surveiller l'utilisation du NPU et les caractéristiques thermiques

**Gestion de la mémoire**
- Implémenter des stratégies efficaces de chargement et de mise en cache des modèles
- Utiliser le mappage mémoire pour les modèles volumineux afin de réduire le temps de démarrage
- Concevoir des applications conscientes de la mémoire pour les appareils à ressources limitées
- Implémenter la quantification des modèles pour l'optimisation de la mémoire

**Efficacité énergétique**
- Optimiser les opérations IA pour une consommation d'énergie minimale
- Implémenter un traitement adaptatif basé sur l'état de la batterie
- Concevoir un traitement en arrière-plan efficace pour des opérations IA continues
- Utiliser des outils de profilage énergétique pour optimiser l'utilisation de l'énergie

### Considérations sur la scalabilité

**Multithreading**
- Concevoir des opérations IA thread-safe pour un traitement concurrent
- Implémenter une distribution efficace du travail entre les cœurs disponibles
- Utiliser des modèles async/await pour des opérations IA non bloquantes
- Planifier l'optimisation des pools de threads pour différentes configurations matérielles

**Stratégies de mise en cache**
- Implémenter une mise en cache intelligente pour les opérations IA fréquemment utilisées
- Concevoir des stratégies d'invalidation de cache pour les mises à jour des modèles
- Utiliser une mise en cache persistante pour les opérations de prétraitement coûteuses
- Implémenter une mise en cache distribuée pour les scénarios multi-utilisateurs

## Meilleures pratiques en matière de sécurité et de confidentialité

### Protection des données

**Traitement local**
- Assurer que les données sensibles ne quittent jamais l'appareil local
- Implémenter un stockage sécurisé pour les modèles IA et les données temporaires
- Utiliser les fonctionnalités de sécurité de Windows pour le sandboxing des applications
- Appliquer le chiffrement pour les modèles stockés et les résultats de traitement intermédiaires

**Sécurité des modèles**
- Valider l'intégrité des modèles avant leur chargement et leur exécution
- Implémenter des mécanismes sécurisés de mise à jour des modèles
- Utiliser des modèles signés pour prévenir les altérations
- Appliquer des contrôles d'accès pour les fichiers de modèles et les configurations

### Considérations de conformité

**Alignement réglementaire**
- Concevoir des applications conformes au RGPD, HIPAA et autres exigences réglementaires
- Implémenter une journalisation des audits pour les processus décisionnels IA
- Fournir des fonctionnalités de transparence pour les résultats générés par l'IA
- Permettre aux utilisateurs de contrôler le traitement des données par l'IA

**Sécurité en entreprise**
- Intégrer avec les politiques de sécurité en entreprise de Windows
- Prendre en charge le déploiement géré via des outils de gestion en entreprise
- Implémenter des contrôles d'accès basés sur les rôles pour les fonctionnalités IA
- Fournir des contrôles administratifs pour les fonctionnalités IA

## Dépannage et débogage

### Défis courants de développement

**Problèmes de configuration de build**
- Assurer une configuration de plateforme ARM64 pour les exemples d'API Windows AI
- Vérifier la compatibilité de la version du Windows App SDK (1.8.1+ requis)
- Vérifier que l'identité du package est correctement configurée (requis pour les API Windows AI)
- Valider que les outils de build prennent en charge la version du framework cible

**Problèmes de chargement des modèles**
- Valider la compatibilité des modèles ONNX avec Windows ML
- Vérifier l'intégrité des fichiers de modèles et les exigences de format
- Valider les exigences matérielles pour des modèles spécifiques
- Déboguer les problèmes d'allocation de mémoire lors du chargement des modèles
- Assurer l'enregistrement du fournisseur d'exécution pour l'accélération matérielle

**Considérations sur le mode de déploiement**
- **Mode autonome** : Entièrement pris en charge avec une taille de déploiement plus importante
- **Mode dépendant du framework** : Empreinte plus petite mais nécessite un runtime partagé
- **Applications non emballées** : Plus prises en charge pour les API Windows AI
- Utiliser `dotnet run -p:Platform=ARM64 -p:SelfContained=true` pour un déploiement autonome ARM64

**Problèmes de performance**
- Profiler les performances des applications sur différentes configurations matérielles
- Identifier les goulots d'étranglement dans les pipelines de traitement IA
- Optimiser les opérations de prétraitement et de post-traitement des données
- Implémenter une surveillance des performances et des alertes

**Difficultés d'intégration**
- Déboguer les problèmes d'intégration des API avec une gestion correcte des erreurs
- Valider les formats de données d'entrée et les exigences de prétraitement
- Tester minutieusement les cas limites et les conditions d'erreur
- Implémenter une journalisation complète pour déboguer les problèmes en production

### Outils et techniques de débogage

**Intégration Visual Studio**
- Utiliser le débogueur AI Toolkit pour l'analyse de l'exécution des modèles
- Implémenter le profilage des performances pour les opérations IA
- Déboguer les opérations IA asynchrones avec une gestion correcte des exceptions
- Utiliser des outils de profilage mémoire pour l'optimisation

**Outils Windows AI Foundry**
- Exploiter le CLI Foundry Local pour tester et valider les modèles
- Utiliser les outils de test des API Windows AI pour vérifier l'intégration
- Implémenter une journalisation personnalisée pour surveiller les opérations IA
- Créer des tests automatisés pour la fiabilité des fonctionnalités IA

## Pérennisation de vos applications

### Technologies émergentes

**Matériel de nouvelle génération**
- Concevoir des applications pour exploiter les futures capacités NPU
- Planifier des modèles de taille et de complexité accrues
- Implémenter des architectures adaptatives pour un matériel en évolution
- Considérer des algorithmes prêts pour le quantique pour une compatibilité future

**Capacités avancées de l'IA**
- Préparer l'intégration multimodale de l'IA sur davantage de types de données
- Planifier une collaboration en temps réel entre plusieurs appareils
- Concevoir pour des capacités d'apprentissage fédéré
- Considérer des architectures hybrides edge-cloud pour l'intelligence

### Apprentissage et adaptation continus

**Mises à jour des modèles**
- Implémenter des mécanismes de mise à jour des modèles sans interruption
- Concevoir des applications pour s'adapter aux capacités améliorées des modèles
- Planifier la compatibilité descendante avec les modèles existants
- Implémenter des tests A/B pour évaluer les performances des modèles

**Évolution des fonctionnalités**
- Concevoir des architectures modulaires qui accueillent de nouvelles capacités IA
- Planifier l'intégration des API Windows AI émergentes
- Implémenter des drapeaux de fonctionnalités pour un déploiement progressif des capacités
- Concevoir des interfaces utilisateur qui s'adaptent aux fonctionnalités IA améliorées

## Conclusion

Le développement d'IA Edge sur Windows représente la convergence de capacités IA puissantes avec la plateforme Windows robuste, sécurisée et évolutive. En maîtrisant l'écosystème Windows AI Foundry, les développeurs peuvent créer des applications intelligentes offrant des expériences utilisateur exceptionnelles tout en maintenant les normes les plus élevées en matière de confidentialité, de sécurité et de performance.

La combinaison des API Windows AI, Foundry Local et Windows ML offre une base inégalée pour construire la prochaine génération d'applications intelligentes sur Windows. Alors que l'IA continue d'évoluer, la plateforme Windows garantit que vos applications évolueront avec les technologies émergentes tout en maintenant la compatibilité et les performances sur l'écosystème matériel diversifié de Windows.

Que vous construisiez des applications grand public, des solutions d'entreprise ou des outils spécialisés par industrie, le développement d'IA Edge sur Windows vous permet de créer des expériences intelligentes, réactives et profondément intégrées exploitant tout le potentiel des appareils modernes sous Windows.

## Ressources supplémentaires

### Documentation et apprentissage
- [Documentation Windows AI Foundry](https://learn.microsoft.com/windows/ai/)
- [Référence des API Windows AI](https://learn.microsoft.com/windows/ai/apis/)
- [Commencer à créer une application avec les API Windows AI](https://learn.microsoft.com/windows/ai/apis/model-setup)
- [
- [Aperçu de Windows ML](https://learn.microsoft.com/windows/ai/new-windows-ml/overview/)
- [Configuration requise pour Windows App SDK](https://docs.microsoft.com/windows/apps/windows-app-sdk/system-requirements)
- [Configuration de l'environnement de développement pour Windows App SDK](https://docs.microsoft.com/windows/apps/windows-app-sdk/set-up-your-development-environment)
- 

### Dépôts d'exemples et code
- [Exemples Windows App SDK - Windows AI Foundry](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsAIFoundry)
- [Exemples Windows App SDK - Windows ML](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML)
- [Exemples d'inférence ONNX Runtime](https://github.com/microsoft/onnxruntime-inference-examples)
- [Dépôt d'exemples Windows App SDK](https://github.com/microsoft/WindowsAppSDK-Samples)

### Outils de développement
- [Kit d'outils IA pour Visual Studio Code](https://learn.microsoft.com/windows/ai/toolkit/)
- [Galerie de développement IA](https://learn.microsoft.com/windows/ai/ai-dev-gallery/)
- [Exemples Windows AI](https://learn.microsoft.com/windows/ai/samples/)
- [Outils de conversion de modèles](https://code.visualstudio.com/docs/intelligentapps/modelconversion)

### Support technique
- [Documentation Windows ML](https://learn.microsoft.com/windows/ai/new-windows-ml/overview)
- [Documentation ONNX Runtime](https://onnxruntime.ai/docs/)
- [Documentation Windows App SDK](https://docs.microsoft.com/windows/apps/windows-app-sdk/)
- [Signaler des problèmes - Exemples Windows App SDK](https://github.com/microsoft/WindowsAppSDK-Samples/issues)

### Communauté et support
- [Communauté des développeurs Windows](https://developer.microsoft.com/en-us/windows/)
- [Blog Windows AI Foundry](https://blogs.windows.com/windowsdeveloper/)
- [Formation IA sur Microsoft Learn](https://learn.microsoft.com/training/browse/?products=windows&subjects=artificial-intelligence)

---

*Ce guide est conçu pour évoluer avec l'écosystème Windows AI en constante progression. Des mises à jour régulières garantissent une adéquation avec les dernières capacités de la plateforme et les meilleures pratiques de développement.*

[08. Prise en main avec Microsoft Foundry Local - Kit complet pour développeurs](../Module08/README.md)

---

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction humaine professionnelle. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées résultant de l'utilisation de cette traduction.
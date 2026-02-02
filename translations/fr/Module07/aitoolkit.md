# Guide de développement Edge AI avec AI Toolkit pour Visual Studio Code

## Introduction

Bienvenue dans le guide complet pour utiliser AI Toolkit pour Visual Studio Code dans le développement Edge AI. Alors que l'intelligence artificielle passe du cloud centralisé aux appareils distribués en périphérie, les développeurs ont besoin d'outils puissants et intégrés capables de relever les défis uniques du déploiement en périphérie - des contraintes de ressources aux exigences de fonctionnement hors ligne.

AI Toolkit pour Visual Studio Code comble cet écart en offrant un environnement de développement complet spécialement conçu pour créer, tester et optimiser des applications d'IA fonctionnant efficacement sur des appareils en périphérie. Que vous développiez pour des capteurs IoT, des appareils mobiles, des systèmes embarqués ou des serveurs en périphérie, cet outil simplifie l'ensemble de votre flux de travail de développement dans l'environnement familier de VS Code.

Ce guide vous accompagnera à travers les concepts essentiels, les outils et les meilleures pratiques pour exploiter AI Toolkit dans vos projets Edge AI, depuis la sélection initiale des modèles jusqu'au déploiement en production.

## Vue d'ensemble

AI Toolkit pour Visual Studio Code est une extension puissante qui simplifie le développement d'agents et la création d'applications d'IA. Le toolkit offre des capacités complètes pour explorer, évaluer et déployer des modèles d'IA provenant d'une large gamme de fournisseurs—including Anthropic, OpenAI, GitHub, Google—tout en prenant en charge l'exécution locale des modèles avec ONNX et Ollama.

Ce qui distingue AI Toolkit, c'est son approche complète du cycle de vie du développement d'IA. Contrairement aux outils traditionnels qui se concentrent sur des aspects isolés, AI Toolkit fournit un environnement intégré couvrant la découverte de modèles, l'expérimentation, le développement d'agents, l'évaluation et le déploiement—tout cela dans l'environnement familier de VS Code.

La plateforme est spécialement conçue pour le prototypage rapide et le déploiement en production, avec des fonctionnalités telles que la génération de prompts, des démarrages rapides, des intégrations fluides avec MCP (Model Context Protocol), et des capacités d'évaluation étendues. Pour le développement Edge AI, cela signifie que vous pouvez développer, tester et optimiser efficacement des applications d'IA pour des scénarios de déploiement en périphérie tout en conservant l'intégralité du flux de travail de développement dans VS Code.

## Objectifs d'apprentissage

À la fin de ce guide, vous serez capable de :

### Compétences de base
- **Installer et configurer** AI Toolkit pour Visual Studio Code pour les flux de travail de développement Edge AI
- **Naviguer et utiliser** l'interface AI Toolkit, y compris le catalogue de modèles, le Playground et l'Agent Builder
- **Sélectionner et évaluer** des modèles d'IA adaptés au déploiement en périphérie en fonction des performances et des contraintes de ressources
- **Convertir et optimiser** des modèles au format ONNX et utiliser des techniques de quantification pour les appareils en périphérie

### Compétences en développement Edge AI
- **Concevoir et implémenter** des applications Edge AI en utilisant l'environnement de développement intégré
- **Tester les modèles** dans des conditions similaires à celles de la périphérie en utilisant l'inférence locale et la surveillance des ressources
- **Créer et personnaliser** des agents d'IA optimisés pour les scénarios de déploiement en périphérie
- **Évaluer les performances des modèles** en utilisant des métriques pertinentes pour l'informatique en périphérie (latence, utilisation de la mémoire, précision)

### Optimisation et déploiement
- **Appliquer des techniques de quantification et de pruning** pour réduire la taille des modèles tout en maintenant des performances acceptables
- **Optimiser les modèles** pour des plateformes matérielles spécifiques en périphérie, y compris l'accélération CPU, GPU et NPU
- **Mettre en œuvre les meilleures pratiques** pour le développement Edge AI, y compris la gestion des ressources et les stratégies de repli
- **Préparer les modèles et les applications** pour le déploiement en production sur des appareils en périphérie

### Concepts avancés de Edge AI
- **Intégrer avec des frameworks Edge AI** tels que ONNX Runtime, Windows ML et TensorFlow Lite
- **Implémenter des architectures multi-modèles** et des scénarios d'apprentissage fédéré pour les environnements en périphérie
- **Résoudre les problèmes courants de Edge AI** tels que les contraintes de mémoire, la vitesse d'inférence et la compatibilité matérielle
- **Concevoir des stratégies de surveillance et de journalisation** pour les applications Edge AI en production

### Application pratique
- **Construire des solutions Edge AI de bout en bout** depuis la sélection des modèles jusqu'au déploiement
- **Démontrer une maîtrise** des flux de travail de développement spécifiques à la périphérie et des techniques d'optimisation
- **Appliquer les concepts appris** à des cas d'utilisation Edge AI réels, y compris IoT, mobile et applications embarquées
- **Évaluer et comparer** différentes stratégies de déploiement Edge AI et leurs compromis

## Fonctionnalités clés pour le développement Edge AI

### 1. Catalogue de modèles et découverte
- **Support multi-fournisseurs** : Parcourez et accédez à des modèles d'IA provenant d'Anthropic, OpenAI, GitHub, Google et autres
- **Intégration de modèles locaux** : Découverte simplifiée des modèles ONNX et Ollama pour le déploiement en périphérie
- **Modèles GitHub** : Intégration directe avec l'hébergement de modèles GitHub pour un accès simplifié
- **Comparaison de modèles** : Comparez les modèles côte à côte pour trouver le meilleur équilibre pour les contraintes des appareils en périphérie

### 2. Playground interactif
- **Environnement de test interactif** : Expérimentation rapide avec les capacités des modèles dans un environnement contrôlé
- **Support multi-modal** : Testez avec des images, du texte et d'autres entrées typiques des scénarios en périphérie
- **Expérimentation en temps réel** : Retour immédiat sur les réponses et les performances des modèles
- **Optimisation des paramètres** : Affinez les paramètres des modèles pour les exigences de déploiement en périphérie

### 3. Constructeur de prompts (Agent Builder)
- **Génération de langage naturel** : Créez des prompts de démarrage à partir de descriptions en langage naturel
- **Affinement itératif** : Améliorez les prompts en fonction des réponses et des performances des modèles
- **Décomposition des tâches** : Divisez les tâches complexes avec des chaînes de prompts et des sorties structurées
- **Support des variables** : Utilisez des variables dans les prompts pour un comportement dynamique des agents
- **Génération de code de production** : Produisez du code prêt pour la production pour un développement rapide d'applications

### 4. Exécution en masse et évaluation
- **Test multi-modèles** : Exécutez plusieurs prompts sur des modèles sélectionnés simultanément
- **Tests efficaces à grande échelle** : Testez divers entrées et configurations efficacement
- **Cas de test personnalisés** : Exécutez des agents avec des cas de test pour valider leur fonctionnalité
- **Comparaison des performances** : Comparez les résultats entre différents modèles et configurations

### 5. Évaluation des modèles avec des ensembles de données
- **Métriques standard** : Testez les modèles d'IA avec des évaluateurs intégrés (score F1, pertinence, similarité, cohérence)
- **Évaluateurs personnalisés** : Créez vos propres métriques d'évaluation pour des cas d'utilisation spécifiques
- **Intégration des ensembles de données** : Testez les modèles avec des ensembles de données complets
- **Mesure des performances** : Quantifiez les performances des modèles pour les décisions de déploiement en périphérie

### 6. Capacités de fine-tuning
- **Personnalisation des modèles** : Adaptez les modèles à des cas d'utilisation et des domaines spécifiques
- **Adaptation spécialisée** : Ajustez les modèles aux exigences et domaines spécialisés
- **Optimisation pour la périphérie** : Affinez les modèles spécifiquement pour les contraintes de déploiement en périphérie
- **Entraînement spécifique au domaine** : Créez des modèles adaptés à des cas d'utilisation spécifiques en périphérie

### 7. Intégration des outils MCP
- **Connectivité avec des outils externes** : Connectez les agents à des outils externes via des serveurs Model Context Protocol
- **Actions réelles** : Permettez aux agents de requêter des bases de données, d'accéder à des API ou d'exécuter une logique personnalisée
- **Serveurs MCP existants** : Utilisez des outils via des protocoles de commande (stdio) ou HTTP (événements envoyés par le serveur)
- **Développement MCP personnalisé** : Construisez et testez de nouveaux serveurs MCP avec le Builder d'agents

### 8. Développement et test d'agents
- **Support des appels de fonctions** : Permettez aux agents d'invoquer dynamiquement des fonctions externes
- **Tests d'intégration en temps réel** : Testez les intégrations avec des exécutions en temps réel et l'utilisation des outils
- **Versionnement des agents** : Contrôle de version pour les agents avec capacités de comparaison des résultats d'évaluation
- **Débogage et traçage** : Capacités de traçage et de débogage local pour le développement d'agents

## Flux de travail de développement Edge AI

### Phase 1 : Découverte et sélection de modèles
1. **Explorer le catalogue de modèles** : Utilisez le catalogue pour trouver des modèles adaptés au déploiement en périphérie
2. **Comparer les performances** : Évaluez les modèles en fonction de leur taille, précision et vitesse d'inférence
3. **Tester localement** : Utilisez les modèles Ollama ou ONNX pour tester localement avant le déploiement en périphérie
4. **Évaluer les besoins en ressources** : Déterminez les besoins en mémoire et en calcul pour les appareils en périphérie ciblés

### Phase 2 : Optimisation des modèles
1. **Convertir en ONNX** : Convertissez les modèles sélectionnés au format ONNX pour la compatibilité en périphérie
2. **Appliquer la quantification** : Réduisez la taille des modèles grâce à la quantification INT8 ou INT4
3. **Optimisation matérielle** : Optimisez pour le matériel en périphérie ciblé (ARM, x86, accélérateurs spécialisés)
4. **Validation des performances** : Validez que les modèles optimisés maintiennent une précision acceptable

### Phase 3 : Développement d'applications
1. **Conception d'agents** : Utilisez l'Agent Builder pour créer des agents d'IA optimisés pour la périphérie
2. **Ingénierie des prompts** : Développez des prompts qui fonctionnent efficacement avec des modèles plus petits en périphérie
3. **Tests d'intégration** : Testez les agents dans des conditions simulées similaires à celles de la périphérie
4. **Génération de code** : Produisez du code de production optimisé pour le déploiement en périphérie

### Phase 4 : Évaluation et test
1. **Évaluation en masse** : Testez plusieurs configurations pour trouver les paramètres optimaux en périphérie
2. **Profilage des performances** : Analysez la vitesse d'inférence, l'utilisation de la mémoire et la précision
3. **Simulation en périphérie** : Testez dans des conditions similaires à l'environnement de déploiement en périphérie ciblé
4. **Tests de résistance** : Évaluez les performances sous diverses conditions de charge

### Phase 5 : Préparation au déploiement
1. **Optimisation finale** : Appliquez les optimisations finales basées sur les résultats des tests
2. **Packaging pour le déploiement** : Emballez les modèles et le code pour le déploiement en périphérie
3. **Documentation** : Documentez les exigences et la configuration du déploiement
4. **Configuration de la surveillance** : Préparez la surveillance et la journalisation pour le déploiement en périphérie

## Public cible pour le développement Edge AI

### Développeurs Edge AI
- Développeurs d'applications créant des appareils en périphérie et des solutions IoT alimentés par l'IA
- Développeurs de systèmes embarqués intégrant des capacités d'IA dans des appareils à ressources limitées
- Développeurs mobiles créant des applications d'IA sur appareil pour smartphones et tablettes

### Ingénieurs Edge AI
- Ingénieurs en IA optimisant les modèles pour le déploiement en périphérie et gérant les pipelines d'inférence
- Ingénieurs DevOps déployant et gérant des modèles d'IA sur une infrastructure en périphérie distribuée
- Ingénieurs en performance optimisant les charges de travail d'IA pour les contraintes matérielles en périphérie

### Chercheurs et éducateurs
- Chercheurs en IA développant des modèles et algorithmes efficaces pour l'informatique en périphérie
- Éducateurs enseignant les concepts de Edge AI et démontrant les techniques d'optimisation
- Étudiants apprenant les défis et solutions du déploiement Edge AI

## Cas d'utilisation Edge AI

### Appareils IoT intelligents
- **Reconnaissance d'images en temps réel** : Déployez des modèles de vision par ordinateur sur des caméras et capteurs IoT
- **Traitement vocal** : Implémentez la reconnaissance vocale et le traitement du langage naturel sur des enceintes intelligentes
- **Maintenance prédictive** : Exécutez des modèles de détection d'anomalies sur des appareils industriels en périphérie
- **Surveillance environnementale** : Déployez des modèles d'analyse de données de capteurs pour des applications environnementales

### Applications mobiles et embarquées
- **Traduction sur appareil** : Implémentez des modèles de traduction linguistique fonctionnant hors ligne
- **Réalité augmentée** : Déployez la reconnaissance et le suivi d'objets en temps réel pour des applications AR
- **Surveillance de la santé** : Exécutez des modèles d'analyse de santé sur des appareils portables et équipements médicaux
- **Systèmes autonomes** : Implémentez des modèles de prise de décision pour drones, robots et véhicules

### Infrastructure informatique en périphérie
- **Centres de données en périphérie** : Déployez des modèles d'IA dans des centres de données en périphérie pour des applications à faible latence
- **Intégration CDN** : Intégrez des capacités de traitement d'IA dans des réseaux de distribution de contenu
- **Edge 5G** : Exploitez l'informatique en périphérie 5G pour des applications alimentées par l'IA
- **Fog Computing** : Implémentez le traitement d'IA dans des environnements de fog computing

## Installation et configuration

### Installation de l'extension
Installez l'extension AI Toolkit directement depuis le Visual Studio Code Marketplace :

**ID de l'extension** : `ms-windows-ai-studio.windows-ai-studio`

**Méthodes d'installation** :
1. **Marketplace VS Code** : Recherchez "AI Toolkit" dans la vue Extensions
2. **Ligne de commande** : `code --install-extension ms-windows-ai-studio.windows-ai-studio`
3. **Installation directe** : Téléchargez depuis [VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)

### Prérequis pour le développement Edge AI
- **Visual Studio Code** : Dernière version recommandée
- **Environnement Python** : Python 3.8+ avec les bibliothèques d'IA requises
- **ONNX Runtime** (Optionnel) : Pour l'inférence des modèles ONNX
- **Ollama** (Optionnel) : Pour le service de modèles locaux
- **Outils d'accélération matérielle** : CUDA, OpenVINO ou accélérateurs spécifiques à la plateforme

### Configuration initiale
1. **Activation de l'extension** : Ouvrez VS Code et vérifiez que AI Toolkit apparaît dans la barre d'activité
2. **Configuration des fournisseurs de modèles** : Configurez l'accès à GitHub, OpenAI, Anthropic ou autres fournisseurs de modèles
3. **Environnement local** : Configurez l'environnement Python et installez les packages requis
4. **Accélération matérielle** : Configurez l'accélération GPU/NPU si disponible
5. **Intégration MCP** : Configurez les serveurs Model Context Protocol si nécessaire

### Liste de contrôle pour la première configuration
- [ ] Extension AI Toolkit installée et activée
- [ ] Catalogue de modèles accessible et modèles détectables
- [ ] Playground fonctionnel pour les tests de modèles
- [ ] Agent Builder accessible pour le développement de prompts
- [ ] Environnement de développement local configuré
- [ ] Accélération matérielle (si disponible) correctement configurée

## Premiers pas avec AI Toolkit

### Guide de démarrage rapide

Nous recommandons de commencer avec les modèles hébergés par GitHub pour une expérience simplifiée :

1. **Installation** : Suivez le [guide d'installation](https://code.visualstudio.com/docs/intelligentapps/overview#_install-and-setup) pour configurer AI Toolkit sur votre appareil
2. **Découverte de modèles** : Depuis la vue de l'extension, sélectionnez **CATALOG > Models** pour explorer les modèles disponibles
3. **Modèles GitHub** : Commencez avec les modèles hébergés par GitHub pour une intégration optimale
4. **Test dans le Playground** : Depuis une fiche de modèle, sélectionnez **Try in Playground** pour commencer à expérimenter les capacités du modèle

### Développement Edge AI étape par étape

#### Étape 1 : Exploration et sélection de modèles
1. Ouvrez la vue AI Toolkit dans la barre d'activité de VS Code
2. Parcourez le catalogue de modèles pour trouver ceux adaptés au déploiement en périphérie
3. Filtrez par fournisseur (GitHub, ONNX, Ollama) en fonction de vos besoins en périphérie
4. Utilisez **Try in Playground** pour tester immédiatement les capacités des modèles

#### Étape 2 : Développement d'agents
1. Utilisez le **Prompt (Agent) Builder** pour créer des agents d'IA optimisés pour la périphérie
2. Générer des invites de départ à l'aide de descriptions en langage naturel  
3. Itérer et affiner les invites en fonction des réponses du modèle  
4. Intégrer les outils MCP pour améliorer les capacités des agents  

#### Étape 3 : Test et évaluation  
1. Utilisez **Bulk Run** pour tester plusieurs invites sur les modèles sélectionnés  
2. Exécutez les agents avec des cas de test pour valider leur fonctionnalité  
3. Évaluez la précision et les performances à l'aide de métriques intégrées ou personnalisées  
4. Comparez différents modèles et configurations  

#### Étape 4 : Ajustement et optimisation  
1. Personnalisez les modèles pour des cas d'utilisation spécifiques  
2. Appliquez un ajustement spécifique au domaine  
3. Optimisez en fonction des contraintes de déploiement en périphérie  
4. Versionnez et comparez différentes configurations d'agents  

#### Étape 5 : Préparation au déploiement  
1. Générez du code prêt pour la production avec l'Agent Builder  
2. Configurez les connexions au serveur MCP pour une utilisation en production  
3. Préparez les packages de déploiement pour les appareils en périphérie  
4. Configurez les métriques de surveillance et d'évaluation  

## Exemples pour AI Toolkit  

Essayez nos exemples  
Les [exemples AI Toolkit](https://github.com/Azure-Samples/AI_Toolkit_Samples) sont conçus pour aider les développeurs et chercheurs à explorer et implémenter des solutions d'IA efficacement.  

Nos exemples incluent :  

Code Exemple : Des exemples préconstruits pour démontrer les fonctionnalités de l'IA, comme l'entraînement, le déploiement ou l'intégration de modèles dans des applications.  
Documentation : Des guides et tutoriels pour aider les utilisateurs à comprendre les fonctionnalités d'AI Toolkit et comment les utiliser.  
Prérequis  

- Visual Studio Code  
- AI Toolkit pour Visual Studio Code  
- Jeton d'accès personnel GitHub (PAT)  
- Foundry Local  

## Bonnes pratiques pour le développement d'IA en périphérie  

### Sélection de modèles  
- **Contraintes de taille** : Choisissez des modèles adaptés aux limitations de mémoire des appareils cibles  
- **Vitesse d'inférence** : Priorisez les modèles avec des temps d'inférence rapides pour les applications en temps réel  
- **Compromis de précision** : Équilibrez la précision des modèles avec les contraintes de ressources  
- **Compatibilité des formats** : Préférez les formats ONNX ou optimisés pour le matériel pour le déploiement en périphérie  

### Techniques d'optimisation  
- **Quantification** : Utilisez la quantification INT8 ou INT4 pour réduire la taille des modèles et améliorer la vitesse  
- **Élagage** : Supprimez les paramètres inutiles des modèles pour réduire les besoins en calcul  
- **Distillation des connaissances** : Créez des modèles plus petits qui conservent les performances des modèles plus grands  
- **Accélération matérielle** : Exploitez les NPUs, GPUs ou accélérateurs spécialisés lorsque disponibles  

### Flux de travail de développement  
- **Tests itératifs** : Testez fréquemment dans des conditions similaires à celles de la périphérie pendant le développement  
- **Surveillance des performances** : Surveillez en continu l'utilisation des ressources et la vitesse d'inférence  
- **Gestion des versions** : Suivez les versions des modèles et les paramètres d'optimisation  
- **Documentation** : Documentez toutes les décisions d'optimisation et les compromis de performances  

### Considérations pour le déploiement  
- **Surveillance des ressources** : Surveillez la mémoire, le CPU et la consommation d'énergie en production  
- **Stratégies de secours** : Implémentez des mécanismes de secours en cas de défaillance des modèles  
- **Mécanismes de mise à jour** : Planifiez les mises à jour des modèles et la gestion des versions  
- **Sécurité** : Mettez en place des mesures de sécurité adaptées pour les applications d'IA en périphérie  

## Intégration avec les frameworks d'IA en périphérie  

### ONNX Runtime  
- **Déploiement multiplateforme** : Déployez des modèles ONNX sur différentes plateformes en périphérie  
- **Optimisation matérielle** : Exploitez les optimisations spécifiques au matériel d'ONNX Runtime  
- **Support mobile** : Utilisez ONNX Runtime Mobile pour les applications sur smartphones et tablettes  
- **Intégration IoT** : Déployez sur des appareils IoT avec les distributions légères d'ONNX Runtime  

### Windows ML  
- **Appareils Windows** : Optimisez pour les appareils en périphérie basés sur Windows et les PC  
- **Accélération NPU** : Exploitez les unités de traitement neuronal sur les appareils Windows  
- **DirectML** : Utilisez DirectML pour l'accélération GPU sur les plateformes Windows  
- **Intégration UWP** : Intégrez avec les applications Universal Windows Platform  

### TensorFlow Lite  
- **Optimisation mobile** : Déployez des modèles TensorFlow Lite sur des appareils mobiles et embarqués  
- **Délégués matériels** : Utilisez des délégués matériels spécialisés pour l'accélération  
- **Microcontrôleurs** : Déployez sur des microcontrôleurs avec TensorFlow Lite Micro  
- **Support multiplateforme** : Déployez sur Android, iOS et systèmes Linux embarqués  

### Azure IoT Edge  
- **Hybride cloud-périphérie** : Combinez l'entraînement dans le cloud avec l'inférence en périphérie  
- **Déploiement de modules** : Déployez des modèles d'IA sous forme de modules IoT Edge  
- **Gestion des appareils** : Gérez les appareils en périphérie et les mises à jour des modèles à distance  
- **Télémétrie** : Collectez des données de performance et des métriques de modèles à partir des déploiements en périphérie  

## Scénarios avancés d'IA en périphérie  

### Déploiement multi-modèles  
- **Ensembles de modèles** : Déployez plusieurs modèles pour améliorer la précision ou la redondance  
- **Tests A/B** : Testez différents modèles simultanément sur des appareils en périphérie  
- **Sélection dynamique** : Choisissez les modèles en fonction des conditions actuelles de l'appareil  
- **Partage des ressources** : Optimisez l'utilisation des ressources entre plusieurs modèles déployés  

### Apprentissage fédéré  
- **Entraînement distribué** : Entraînez des modèles sur plusieurs appareils en périphérie  
- **Préservation de la vie privée** : Gardez les données d'entraînement locales tout en partageant les améliorations des modèles  
- **Apprentissage collaboratif** : Permettez aux appareils d'apprendre des expériences collectives  
- **Coordination périphérie-cloud** : Coordonnez l'apprentissage entre les appareils en périphérie et l'infrastructure cloud  

### Traitement en temps réel  
- **Traitement de flux** : Traitez des flux de données continus sur des appareils en périphérie  
- **Inférence à faible latence** : Optimisez pour une latence minimale d'inférence  
- **Traitement par lots** : Traitez efficacement des lots de données sur des appareils en périphérie  
- **Traitement adaptatif** : Ajustez le traitement en fonction des capacités actuelles de l'appareil  

## Résolution des problèmes de développement d'IA en périphérie  

### Problèmes courants  
- **Contraintes de mémoire** : Modèle trop grand pour la mémoire de l'appareil cible  
- **Vitesse d'inférence** : Inférence du modèle trop lente pour les exigences en temps réel  
- **Dégradation de la précision** : L'optimisation réduit la précision du modèle de manière inacceptable  
- **Compatibilité matérielle** : Modèle incompatible avec le matériel cible  

### Stratégies de débogage  
- **Profilage des performances** : Utilisez les fonctionnalités de traçage d'AI Toolkit pour identifier les goulots d'étranglement  
- **Surveillance des ressources** : Surveillez l'utilisation de la mémoire et du CPU pendant le développement  
- **Tests incrémentaux** : Testez les optimisations de manière incrémentale pour isoler les problèmes  
- **Simulation matérielle** : Utilisez des outils de développement pour simuler le matériel cible  

### Solutions d'optimisation  
- **Quantification supplémentaire** : Appliquez des techniques de quantification plus agressives  
- **Architecture de modèle** : Envisagez différentes architectures de modèles optimisées pour la périphérie  
- **Optimisation du prétraitement** : Optimisez le prétraitement des données pour les contraintes de la périphérie  
- **Optimisation de l'inférence** : Utilisez des optimisations spécifiques au matériel pour l'inférence  

## Ressources et prochaines étapes  

### Documentation officielle  
- [Documentation pour les développeurs AI Toolkit](https://aka.ms/AIToolkit/doc)  
- [Guide d'installation et de configuration](https://code.visualstudio.com/docs/intelligentapps/overview#_install-and-setup)  
- [Documentation des applications intelligentes VS Code](https://code.visualstudio.com/docs/intelligentapps)  
- [Documentation du Model Context Protocol (MCP)](https://modelcontextprotocol.io/)  

### Communauté et support  
- [Répertoire GitHub AI Toolkit](https://github.com/microsoft/vscode-ai-toolkit)  
- [Problèmes et demandes de fonctionnalités sur GitHub](https://aka.ms/AIToolkit/feedback)  
- [Communauté Discord Azure AI Foundry](https://aka.ms/azureaifoundry/discord)  
- [Marketplace des extensions VS Code](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)  

### Ressources techniques  
- [Documentation ONNX Runtime](https://onnxruntime.ai/)  
- [Documentation Ollama](https://ollama.ai/)  
- [Documentation Windows ML](https://docs.microsoft.com/en-us/windows/ai/)  
- [Documentation Azure AI Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/)  

### Parcours d'apprentissage  
- [Cours sur les fondamentaux de l'IA en périphérie](../Module01/README.md)  
- [Guide des petits modèles de langage](../Module02/README.md)  
- [Stratégies de déploiement en périphérie](../Module03/README.md)  
- [Développement d'IA en périphérie sous Windows](./windowdeveloper.md)  

### Ressources supplémentaires  
- **Statistiques du répertoire** : Plus de 1,8k étoiles, 150+ forks, 18+ contributeurs  
- **Licence** : Licence MIT  
- **Sécurité** : Les politiques de sécurité de Microsoft s'appliquent  
- **Télémétrie** : Respecte les paramètres de télémétrie de VS Code  

## Conclusion  

AI Toolkit pour Visual Studio Code représente une plateforme complète pour le développement moderne d'IA, offrant des capacités de développement d'agents particulièrement précieuses pour les applications d'IA en périphérie. Avec son vaste catalogue de modèles prenant en charge des fournisseurs tels qu'Anthropic, OpenAI, GitHub et Google, combiné à une exécution locale via ONNX et Ollama, le toolkit offre la flexibilité nécessaire pour divers scénarios de déploiement en périphérie.  

La force du toolkit réside dans son approche intégrée—de la découverte et de l'expérimentation des modèles dans le Playground au développement sophistiqué d'agents avec le Prompt Builder, des capacités d'évaluation complètes et une intégration transparente des outils MCP. Pour les développeurs d'IA en périphérie, cela signifie un prototypage rapide et des tests d'agents d'IA avant le déploiement en périphérie, avec la possibilité d'itérer rapidement et d'optimiser pour des environnements à ressources limitées.  

Les principaux avantages pour le développement d'IA en périphérie incluent :  
- **Expérimentation rapide** : Testez rapidement les modèles et agents avant de les déployer en périphérie  
- **Flexibilité multi-fournisseurs** : Accédez à des modèles provenant de diverses sources pour trouver des solutions optimales en périphérie  
- **Développement local** : Testez avec ONNX et Ollama pour un développement hors ligne et respectueux de la vie privée  
- **Prêt pour la production** : Générez du code prêt pour la production et intégrez avec des outils externes via MCP  
- **Évaluation complète** : Utilisez des métriques intégrées et personnalisées pour valider les performances de l'IA en périphérie  

Alors que l'IA continue de se diriger vers des scénarios de déploiement en périphérie, AI Toolkit pour VS Code fournit l'environnement de développement et le flux de travail nécessaires pour construire, tester et optimiser des applications intelligentes pour des environnements à ressources limitées. Que vous développiez des solutions IoT, des applications d'IA mobile ou des systèmes d'intelligence embarquée, l'ensemble de fonctionnalités complet et le flux de travail intégré du toolkit soutiennent tout le cycle de vie du développement d'IA en périphérie.  

Avec un développement continu et une communauté active (plus de 1,8k étoiles sur GitHub), AI Toolkit reste à la pointe des outils de développement d'IA, évoluant constamment pour répondre aux besoins des développeurs modernes d'IA construisant pour des scénarios de déploiement en périphérie.  

[Next Foundry Local](./foundrylocal.md)  

---

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction humaine professionnelle. Nous ne sommes pas responsables des malentendus ou des interprétations erronées résultant de l'utilisation de cette traduction.
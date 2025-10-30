<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "78ca68df03ae43371b203ea43d346dec",
  "translation_date": "2025-10-30T10:28:51+00:00",
  "source_file": "CHANGELOG.md",
  "language_code": "fr"
}
-->
# Journal des modifications

Tous les changements notables apportés à EdgeAI pour les débutants sont documentés ici. Ce projet utilise des entrées basées sur les dates et le style Keep a Changelog (Ajouté, Modifié, Corrigé, Supprimé, Documentation, Déplacé).

## 2025-10-30

### Ajouté - Amélioration complète des agents IA dans le Module06
- **Intégration du Microsoft Agent Framework** (`Module06/01.IntroduceAgent.md`) :
  - Section complète sur le Microsoft Agent Framework pour le développement d'agents prêts pour la production
  - Modèles d'intégration détaillés avec Foundry Local pour le déploiement en périphérie
  - Exemples d'orchestration multi-agents avec des modèles SLM spécialisés
  - Modèles de déploiement en entreprise avec gestion des ressources et surveillance
  - Fonctionnalités de sécurité et de conformité pour les systèmes d'agents en périphérie
  - Exemples d'implémentation dans des cas réels (commerce de détail, santé, service client)

- **Stratégies de déploiement des agents SLM en production** :
  - **Foundry Local** : Documentation complète sur l'exécution d'IA en périphérie de niveau entreprise avec installation, configuration et modèles de production
  - **Ollama** : Déploiement axé sur la communauté avec surveillance et gestion des modèles approfondies
  - **VLLM** : Moteur d'inférence haute performance avec techniques d'optimisation avancées et fonctionnalités d'entreprise
  - Listes de contrôle pour le déploiement en production et tableaux comparatifs pour les trois plateformes

- **Améliorations des frameworks SLM optimisés pour la périphérie** :
  - **ONNX Runtime** : Nouvelle section complète pour le déploiement d'agents SLM multiplateformes
  - Modèles de déploiement universels sur Windows, Linux, macOS, iOS et Android
  - Options d'accélération matérielle (CPU, GPU, NPU) avec détection automatique
  - Fonctionnalités prêtes pour la production et optimisations spécifiques aux agents
  - Exemples d'implémentation complets avec intégration au Microsoft Agent Framework

- **Références et lectures complémentaires** :
  - Bibliothèque de ressources complète avec plus de 100 sources autorisées
  - Articles de recherche fondamentaux sur les agents IA et les modèles de langage réduits
  - Documentation officielle pour tous les principaux frameworks et outils
  - Rapports industriels, analyses de marché et benchmarks techniques
  - Ressources éducatives, conférences et forums communautaires
  - Normes, spécifications et cadres de conformité

### Modifié - Modernisation du contenu du Module06
- **Objectifs d'apprentissage améliorés** : Ajout de la maîtrise du Microsoft Agent Framework et des capacités de déploiement en périphérie
- **Orientation vers la production** : Passage d'une approche conceptuelle à des conseils prêts pour l'implémentation avec des exemples de production
- **Exemples de code** : Mise à jour de tous les exemples pour utiliser des modèles SDK modernes et des meilleures pratiques
- **Modèles d'architecture** : Ajout d'architectures hiérarchiques d'agents et de coordination périphérie-cloud
- **Optimisation des performances** : Amélioration avec des recommandations de gestion des ressources et de mise à l'échelle automatique

### Documentation - Amélioration de la structure du Module06
- **Couverture complète du framework d'agents** : Des concepts de base au déploiement en entreprise
- **Stratégies de déploiement en production** : Guides complets pour Foundry Local, Ollama et VLLM
- **Optimisation multiplateforme** : Ajout de ONNX Runtime pour un déploiement universel
- **Bibliothèque de ressources** : Références étendues pour l'apprentissage et l'implémentation continus

### Ajouté - Mise à jour de la documentation du protocole de contexte de modèle (MCP) dans le Module06
- **Modernisation de l'introduction au MCP** (`Module06/03.IntroduceMCP.md`) :
  - Mise à jour avec les dernières spécifications MCP de modelcontextprotocol.io (version du 18 juin 2025)
  - Ajout de l'analogie officielle avec l'USB-C pour les connexions standardisées des applications IA
  - Mise à jour de la section architecture avec le design officiel à deux couches (couche de données + couche de transport)
  - Documentation améliorée des primitives de base avec des primitives serveur (outils, ressources, invites) et des primitives client (échantillonnage, sollicitation, journalisation)

- **Références et ressources complètes sur le MCP** :
  - Ajout du lien **MCP pour les débutants** (https://aka.ms/mcp-for-beginners)
  - Documentation et spécifications officielles du MCP (modelcontextprotocol.io)
  - Ressources de développement incluant MCP Inspector et implémentations de référence
  - Normes techniques (JSON-RPC 2.0, JSON Schema, OpenAPI, événements envoyés par le serveur)

### Ajouté - Intégration Qualcomm QNN dans le Module04
- **Nouvelle section 7 : Suite d'optimisation Qualcomm QNN** (`Module04/05.QualcommQNN.md`) :
  - Guide complet de plus de 400 lignes couvrant le cadre unifié d'inférence IA de Qualcomm
  - Couverture détaillée de l'informatique hétérogène (Hexagon NPU, Adreno GPU, Kryo CPU)
  - Optimisation matérielle pour les plateformes Snapdragon avec distribution intelligente des charges de travail
  - Techniques avancées de quantification (INT8, INT16, précision mixte) pour le déploiement mobile
  - Optimisation de l'inférence économe en énergie pour les appareils alimentés par batterie et les applications en temps réel
  - Guide d'installation complet avec configuration du SDK QNN et de l'environnement
  - Exemples pratiques : conversion PyTorch vers QNN, optimisation multi-backend, génération de binaires contextuels
  - Modèles d'utilisation avancés : configuration de backend personnalisé, quantification dynamique, profilage des performances
  - Section de dépannage complète et ressources communautaires

- **Structure améliorée du Module04** :
  - Mise à jour du README.md pour inclure 7 sections progressives (au lieu de 6)
  - Ajout de Qualcomm QNN au tableau des benchmarks de performance (amélioration de vitesse de 5 à 15x, réduction de mémoire de 50 à 80 %)
  - Résultats d'apprentissage complets pour le déploiement IA mobile et l'optimisation énergétique

### Modifié - Mises à jour de la documentation du Module04
- **Amélioration de la documentation Microsoft Olive** (`Module04/03.MicrosoftOlive.md`) :
  - Ajout d'une section complète "Olive Recipes Repository" couvrant plus de 100 recettes d'optimisation préconstruites
  - Couverture détaillée des familles de modèles prises en charge (Phi, Llama, Qwen, Gemma, Mistral, DeepSeek)
  - Exemples pratiques pour la personnalisation des recettes et les contributions communautaires
  - Amélioration avec des benchmarks de performance et des conseils d'intégration

- **Réorganisation des sections dans le Module04** :
  - Apple MLX déplacé à la section 5 (au lieu de la section 6)
  - Synthèse des workflows déplacée à la section 6 (au lieu de la section 7)
  - Qualcomm QNN positionné comme section 7 (focus spécialisé sur le mobile/périphérie)
  - Mise à jour de toutes les références de fichiers et des liens de navigation en conséquence

### Corrigé - Validation des exemples d'atelier
- **Validation et réparation de chat_bootstrap.py** :
  - Correction de l'instruction d'importation corrompue (`util.util.workshop_utils` → `util.workshop_utils`)
  - Création du fichier `__init__.py` manquant dans le package util pour une résolution correcte des modules Python
  - Installation des dépendances requises (openai, foundry-local-sdk) dans l'environnement conda
  - Validation réussie de l'exécution de l'exemple avec des invites par défaut et personnalisées
  - Confirmation de l'intégration avec le service Foundry Local et le chargement du modèle (phi-4-mini avec optimisation CUDA)

### Documentation - Mises à jour complètes des guides
- **Restructuration complète du README.md du Module04** :
  - Ajout de Qualcomm QNN comme cadre d'optimisation majeur aux côtés de OpenVINO, Olive, MLX
  - Mise à jour des résultats d'apprentissage du chapitre pour inclure le déploiement IA mobile et l'optimisation énergétique
  - Amélioration du tableau de comparaison des performances avec les métriques QNN et les cas d'utilisation mobile/périphérie
  - Maintien de la progression logique des solutions d'entreprise aux optimisations spécifiques à la plateforme

- **Références croisées et navigation** :
  - Mise à jour de tous les liens internes et références de fichiers pour la nouvelle numérotation des sections
  - Description améliorée de la synthèse des workflows pour inclure les environnements mobiles, de bureau et cloud
  - Ajout de liens de ressources complets pour l'écosystème des développeurs Qualcomm

## 2025-10-08

### Ajouté - Mise à jour complète de l'atelier
- **Réécriture complète du README.md de l'atelier** :
  - Ajout d'une introduction complète expliquant la proposition de valeur de l'IA en périphérie (confidentialité, performance, coût)
  - Création de 6 objectifs d'apprentissage principaux avec des compétences détaillées
  - Ajout d'un tableau des résultats d'apprentissage avec livrables et matrice de compétences
  - Inclusion d'une section sur les compétences prêtes pour le marché pour la pertinence industrielle
  - Ajout d'un guide de démarrage rapide avec prérequis et configuration en 3 étapes
  - Création de tableaux de ressources pour les exemples Python (8 fichiers avec temps d'exécution)
  - Ajout d'un tableau de notebooks Jupyter (8 notebooks avec niveaux de difficulté)
  - Création d'un tableau de documentation (7 documents clés avec conseils "À utiliser quand")
  - Ajout de recommandations de parcours d'apprentissage pour différents niveaux de compétence

- **Infrastructure de validation et de test de l'atelier** :
  - Création de `scripts/validate_samples.py` - Outil de validation complet pour la syntaxe, les importations et les meilleures pratiques
  - Création de `scripts/test_samples.py` - Exécuteur de tests rapides pour tous les exemples Python
  - Ajout de documentation de validation à `scripts/README.md`

- **Documentation complète** :
  - Création de `SAMPLES_UPDATE_SUMMARY.md` - Guide détaillé de plus de 400 lignes couvrant toutes les améliorations
  - Création de `UPDATE_COMPLETE.md` - Résumé exécutif de la mise à jour terminée
  - Création de `QUICK_REFERENCE.md` - Carte de référence rapide pour l'atelier

### Modifié - Modernisation des exemples Python de l'atelier
- **Tous les 8 exemples Python mis à jour avec les meilleures pratiques** :
  - Amélioration de la gestion des erreurs avec des blocs try-except autour de toutes les opérations d'E/S
  - Ajout de types d'indices et de docstrings complets
  - Mise en œuvre d'un modèle de journalisation cohérent [INFO]/[ERROR]/[RESULT]
  - Protection des importations optionnelles avec des conseils d'installation
  - Amélioration des retours utilisateur dans tous les exemples

- **session01/chat_bootstrap.py** :
  - Amélioration de l'initialisation du client avec des messages d'erreur complets
  - Meilleure gestion des erreurs de streaming avec validation des blocs
  - Ajout d'une gestion des exceptions pour l'indisponibilité du service

- **session02/rag_pipeline.py** :
  - Ajout de protections d'importation pour sentence-transformers avec des conseils d'installation
  - Amélioration de la gestion des erreurs pour les opérations d'embedding et de génération
  - Formatage amélioré des résultats avec des structures organisées

- **session02/rag_eval_ragas.py** :
  - Protection des importations optionnelles (ragas, datasets) avec des messages d'erreur conviviaux
  - Ajout de gestion des erreurs pour les métriques d'évaluation
  - Formatage amélioré des résultats d'évaluation

- **session03/benchmark_oss_models.py** :
  - Mise en œuvre d'une dégradation progressive (continue en cas d'échec des modèles)
  - Ajout de rapports détaillés sur la progression et de gestion des erreurs par modèle
  - Calcul des statistiques amélioré avec récupération complète des erreurs

- **session04/model_compare.py** :
  - Ajout de types d'indices (types de retour Tuple)
  - Formatage amélioré des résultats avec des structures JSON organisées
  - Mise en œuvre de gestion des erreurs par modèle avec récupération

- **session05/agents_orchestrator.py** :
  - Amélioration de Agent.act() avec des docstrings complets
  - Ajout de gestion des erreurs de pipeline avec journalisation étape par étape
  - Meilleure gestion de la mémoire et suivi de l'état

- **session06/models_router.py** :
  - Documentation améliorée des fonctions pour tous les composants de routage
  - Ajout de journalisation détaillée dans la fonction route()
  - Amélioration des résultats de test avec des structures organisées

- **session06/models_pipeline.py** :
  - Ajout de gestion des erreurs à la fonction d'assistance chat()
  - Amélioration de pipeline() avec journalisation des étapes et rapports de progression
  - Amélioration de main() avec récupération complète des erreurs

### Documentation - Amélioration de la documentation de l'atelier
- Mise à jour du README.md principal avec une section Atelier mettant en avant le parcours d'apprentissage pratique
- Amélioration de STUDY_GUIDE.md avec une section Atelier complète incluant :
  - Objectifs d'apprentissage et domaines d'étude
  - Questions d'auto-évaluation
  - Exercices pratiques avec estimations de temps
  - Allocation de temps pour étude concentrée et à temps partiel
  - Ajout de l'atelier au modèle de suivi de progression
- Mise à jour du guide d'allocation de temps de 20 heures à 30 heures (incluant l'atelier)
- Ajout de descriptions des exemples d'atelier et des résultats d'apprentissage au README

### Corrigé
- Résolution des modèles incohérents de gestion des erreurs dans les exemples d'atelier
- Correction des erreurs d'importation de dépendances optionnelles avec des protections appropriées
- Correction des indices de type manquants dans les fonctions critiques
- Résolution des retours utilisateur insuffisants dans les scénarios d'erreur
- Correction des problèmes de validation avec une infrastructure de test complète

---

## 2025-09-23

### Modifié - Modernisation majeure du Module 08
- **Alignement complet avec les modèles de dépôt Microsoft Foundry-Local**
  - Mise à jour de tous les exemples de code pour utiliser les intégrations modernes `FoundryLocalManager` et SDK OpenAI
  - Remplacement des appels manuels `requests` obsolètes par une utilisation correcte du SDK
  - Alignement des modèles d'implémentation avec la documentation officielle de Microsoft et les exemples

- **Modernisation de 05.AIPoweredAgents.md** :
  - Mise à jour de l'orchestration multi-agents pour utiliser des modèles SDK modernes
  - Amélioration de l'implémentation du coordinateur avec des fonctionnalités avancées (boucles de rétroaction, surveillance des performances)
  - Ajout de gestion des erreurs complète et de vérification de la santé du service
  - Intégration de références appropriées aux exemples locaux (`samples/05/multi_agent_orchestration.ipynb`)
  - Mise à jour des exemples d'appels de fonctions pour utiliser le paramètre moderne `tools` au lieu de `functions` obsolètes
  - Ajout de modèles prêts pour la production avec surveillance et suivi des statistiques

- **Réécriture complète de 06.ModelsAsTools.md** :
  - Remplacement du registre d'outils de base par une implémentation de routeur de modèles intelligent
  - Ajout de sélection de modèles basée sur des mots-clés pour différents types de tâches (général, raisonnement, code, créatif)
  - Intégration de la configuration basée sur l'environnement avec affectation flexible des modèles
  - Amélioration avec surveillance complète de la santé du service et gestion des erreurs
  - Ajout de modèles de déploiement en production avec surveillance des requêtes et suivi des performances
  - Alignement avec l'implémentation locale dans `samples/06/router.py` et `samples/06/model_router.ipynb`

- **Améliorations de la structure de la documentation** :
  - Ajout de sections d'aperçu mettant en avant la modernisation et l'alignement SDK
  - Amélioration avec des emojis et un meilleur formatage pour une lisibilité accrue
  - Ajout de références appropriées aux fichiers d'exemples locaux dans toute la documentation
  - Inclusion de conseils d'implémentation prêts pour la production et des meilleures pratiques

### Ajouté
- Sections d'aperçu complètes dans les fichiers du Module 08 mettant en avant l'intégration moderne du SDK
- Points forts de l'architecture montrant des fonctionnalités avancées (systèmes multi-agents, routage intelligent)
- Références directes aux implémentations d'exemples locaux pour une expérience pratique
- Conseils de déploiement en production avec modèles de surveillance et gestion des erreurs
- Exemples interactifs de notebooks Jupyter avec fonctionnalités avancées et benchmarks

### Corrigé
- Discrepances d'alignement entre la documentation et les implémentations d'exemples réels
- Modèles d'utilisation SDK obsolètes dans tout le Module 08
- Références manquantes à la bibliothèque complète d'exemples locaux
- Approches d'implémentation incohérentes dans différentes sections

---

## 2025-09-18

### Ajouté
- Module 08 : Microsoft Foundry Local – Kit complet pour développeurs
  - Six sessions : configuration, intégration Azure AI Foundry, modèles open-source, démonstrations de pointe, agents et modèles comme outils
  - Exemples exécutables sous `Module08/samples/01`–`06` avec instructions cmd Windows
    - `01` Chat rapide REST (`chat_quickstart.py`)
    - `02` Démarrage rapide SDK avec prise en charge OpenAI/Foundry Local et Azure OpenAI (`sdk_quickstart.py`)
    - `03` Liste et benchmark CLI (`list_and_bench.cmd`)
    - `04` Démo Chainlit (`app.py`)
    - `05` Orchestration multi-agents (`python -m samples.05.agents.coordinator`)
    - `06` Routeur Models-as-Tools (`router.py`)
- Prise en charge Azure OpenAI dans l'exemple SDK de la session 2 avec configuration des variables d'environnement
- `.vscode/settings.json` pointant vers `Module08/.venv` pour améliorer la résolution de l'analyse Python
- `.env` avec indication `PYTHONPATH` pour la reconnaissance par VS Code/Pylance

### Modifications
- Modèle par défaut mis à jour vers `phi-4-mini` dans les documents et exemples du Module 08 ; mentions restantes de `phi-3.5` supprimées dans le Module 08
- Améliorations du routeur (`Module08/samples/06/router.py`) :
  - Découverte des points de terminaison via `foundry service status` avec analyse regex
  - Vérification de l'état `/v1/models` au démarrage
  - Registre de modèles configurable via environnement (`GENERAL_MODEL`, `REASONING_MODEL`, `CODE_MODEL`, `TOOL_REGISTRY` JSON)
- Exigences mises à jour : `Module08/requirements.txt` inclut désormais `openai` (en plus de `requests`, `chainlit`)
- Conseils pour l'exemple Chainlit clarifiés et ajout de dépannage ; résolution des imports via paramètres de l'espace de travail

### Corrections
- Problèmes d'importation résolus :
  - Le routeur ne dépend plus d'un module `utils` inexistant ; les fonctions sont intégrées
  - Le coordinateur utilise un import relatif (`from .specialists import ...`) et est invoqué via le chemin du module
  - Configuration VS Code/Pylance pour résoudre `chainlit` et les imports de packages
- Correction d'une petite faute de frappe dans `STUDY_GUIDE.md` et ajout de la couverture du Module 08

### Suppressions
- Suppression de `Module08/infra/obs.py` inutilisé et du répertoire vide `infra/` ; les modèles d'observabilité restent optionnels dans les documents

### Déplacements
- Consolidation des démos du Module 08 sous `Module08/samples` avec des dossiers numérotés par session
  - Déplacement de l'application Chainlit vers `samples/04`
  - Déplacement des agents vers `samples/05` et ajout de fichiers `__init__.py` pour la résolution des packages

### Documentation
- Documentation des sessions du Module 08 et enrichissement de tous les README des exemples avec des références Microsoft Learn et des fournisseurs de confiance
- Mise à jour de `Module08/README.md` avec un aperçu des exemples, la configuration du routeur et des conseils de validation
- Section Windows Foundry Local de `Module07/README.md` validée par rapport aux documents Learn
- Mise à jour de `STUDY_GUIDE.md` :
  - Ajout du Module 08 à l'aperçu, aux plannings, au suivi des progrès
  - Ajout d'une section Références complète (Foundry Local, Azure AI, Olive, ONNX Runtime, OpenVINO, MLX, Llama.cpp, vLLM, Ollama, AI Toolkit, Windows ML)

---

## Historique (résumé)
- Architecture du cours et modules établis (Modules 01–07)
- Modernisation itérative du contenu, standardisation du formatage et ajout d'études de cas
- Couverture élargie des cadres d'optimisation (Llama.cpp, Olive, OpenVINO, Apple MLX)

## Non publié / En attente (propositions)
- Tests de validation optionnels par exemple pour vérifier la disponibilité de Foundry Local
- Revoir les traductions pour aligner les références des modèles (par ex., `phi-4-mini`) si nécessaire
- Ajouter une configuration pyright minimale si les équipes préfèrent une rigueur à l'échelle de l'espace de travail

---

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction humaine professionnelle. Nous ne sommes pas responsables des malentendus ou des interprétations erronées résultant de l'utilisation de cette traduction.
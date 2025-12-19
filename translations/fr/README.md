<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1d396a2dcca2c17bdf416bcb57d1d3db",
  "translation_date": "2025-12-17T11:28:57+00:00",
  "source_file": "README.md",
  "language_code": "fr"
}
-->
# EdgeAI pour débutants 


![Image de couverture du cours](../../translated_images/cover.eb18d1b9605d754b30973f4e17c6e11ea4f8473d9686ee378d6e7b44e3c70ac7.fr.png)

[![Contributeurs GitHub](https://img.shields.io/github/contributors/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/graphs/contributors)
[![Problèmes GitHub](https://img.shields.io/github/issues/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/issues)
[![Demandes de tirage GitHub](https://img.shields.io/github/issues-pr/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/pulls)
[![PRs Bienvenues](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

[![Observateurs GitHub](https://img.shields.io/github/watchers/microsoft/edgeai-for-beginners.svg?style=social&label=Watch)](https://GitHub.com/microsoft/edgeai-for-beginners/watchers)
[![Forks GitHub](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork)
[![Étoiles GitHub](https://img.shields.io/github/stars/microsoft/edgeai-for-beginners?style=social&label=Star)](https://GitHub.com/microsoft/edgeai-for-beginners/stargazers)


[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Suivez ces étapes pour commencer à utiliser ces ressources :

1. **Forkez le dépôt** : Cliquez sur [![Forks GitHub](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork)
2. **Clonez le dépôt** :   `git clone https://github.com/microsoft/edgeai-for-beginners.git`
3. [**Rejoignez le Discord Azure AI Foundry et rencontrez des experts et d'autres développeurs**](https://discord.com/invite/ByRwuEEgH4)


### 🌐 Support multilingue

#### Pris en charge via GitHub Action (Automatisé & Toujours à jour)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh/README.md) | [Chinese (Traditional, Hong Kong)](../hk/README.md) | [Chinese (Traditional, Macau)](../mo/README.md) | [Chinese (Traditional, Taiwan)](../tw/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](./README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../br/README.md) | [Portuguese (Portugal)](../pt/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

**Si vous souhaitez que des langues supplémentaires soient prises en charge, elles sont listées [ici](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md)**
## Introduction

Bienvenue dans **EdgeAI pour débutants** – votre parcours complet dans le monde transformateur de l'Intelligence Artificielle en périphérie. Ce cours comble le fossé entre les puissantes capacités de l'IA et le déploiement pratique et réel sur des dispositifs en périphérie, vous permettant d'exploiter le potentiel de l'IA directement là où les données sont générées et où les décisions doivent être prises.

### Ce que vous maîtriserez

Ce cours vous guide des concepts fondamentaux aux implémentations prêtes pour la production, couvrant :
- **Petits modèles de langage (SLMs)** optimisés pour le déploiement en périphérie
- **Optimisation consciente du matériel** sur diverses plateformes
- **Inférence en temps réel** avec des capacités de préservation de la vie privée
- **Stratégies de déploiement en production** pour les applications d'entreprise

### Pourquoi EdgeAI est important

Edge AI représente un changement de paradigme qui répond à des défis modernes critiques :
- **Confidentialité & Sécurité** : Traitez les données sensibles localement sans exposition au cloud
- **Performance en temps réel** : Éliminez la latence réseau pour les applications critiques en temps
- **Efficacité des coûts** : Réduisez la bande passante et les dépenses de calcul cloud
- **Opérations résilientes** : Maintenez la fonctionnalité lors des pannes réseau
- **Conformité réglementaire** : Respectez les exigences de souveraineté des données

### Edge AI

Edge AI désigne l'exécution d'algorithmes d'IA et de modèles de langage localement sur le matériel, proche de l'endroit où les données sont générées, sans dépendre des ressources cloud pour l'inférence. Cela réduit la latence, améliore la confidentialité et permet la prise de décision en temps réel.

### Principes fondamentaux :
- **Inférence sur l'appareil** : Les modèles d'IA s'exécutent sur des dispositifs en périphérie (téléphones, routeurs, microcontrôleurs, PC industriels)
- **Capacité hors ligne** : Fonctionne sans connectivité internet persistante
- **Faible latence** : Réponses immédiates adaptées aux systèmes en temps réel
- **Souveraineté des données** : Garde les données sensibles localement, améliorant la sécurité et la conformité

### Petits modèles de langage (SLMs)

Les SLMs comme Phi-4, Mistral-7B et Gemma sont des versions optimisées de grands LLM—entraînés ou distillés pour :
- **Réduction de l'empreinte mémoire** : Utilisation efficace de la mémoire limitée des dispositifs en périphérie
- **Demande de calcul réduite** : Optimisés pour les performances CPU et GPU en périphérie
- **Temps de démarrage plus rapides** : Initialisation rapide pour des applications réactives

Ils débloquent des capacités NLP puissantes tout en respectant les contraintes de :
- **Systèmes embarqués** : Dispositifs IoT et contrôleurs industriels
- **Appareils mobiles** : Smartphones et tablettes avec capacités hors ligne
- **Dispositifs IoT** : Capteurs et appareils intelligents avec ressources limitées
- **Serveurs en périphérie** : Unités de traitement locales avec ressources GPU limitées
- **Ordinateurs personnels** : Scénarios de déploiement sur bureau et portable

## Modules du cours & Navigation

| Module | Sujet | Domaine d'intérêt | Contenu clé | Niveau | Durée |
|--------|-------|------------|-------------|--------|----------|
| [📖 00 ](./introduction.md) | [Introduction à EdgeAI](./introduction.md) | Fondations & Contexte | Vue d'ensemble EdgeAI • Applications industrielles • Introduction aux SLM • Objectifs d'apprentissage | Débutant | 1-2 h |
| [📚 01](../../Module01) | [Fondamentaux EdgeAI](./Module01/README.md) | Comparaison Cloud vs Edge AI | Fondamentaux EdgeAI • Études de cas réelles • Guide d'implémentation • Déploiement en périphérie | Débutant | 3-4 h |
| [🧠 02](../../Module02) | [Fondations des modèles SLM](./Module02/README.md) | Familles de modèles & architecture | Famille Phi • Famille Qwen • Famille Gemma • BitNET • μModel • Phi-Silica | Débutant | 4-5 h |
| [🚀 03](../../Module03) | [Pratique de déploiement SLM](./Module03/README.md) | Déploiement local & cloud | Apprentissage avancé • Environnement local • Déploiement cloud | Intermédiaire | 4-5 h |
| [⚙️ 04](../../Module04) | [Boîte à outils d'optimisation de modèle](./Module04/README.md) | Optimisation multiplateforme | Introduction • Llama.cpp • Microsoft Olive • OpenVINO • Apple MLX • Synthèse de workflow | Intermédiaire | 5-6 h |
| [🔧 05](../../Module05) | [SLMOps en production](./Module05/README.md) | Opérations en production | Introduction SLMOps • Distillation de modèle • Affinage • Déploiement en production | Avancé | 5-6 h |
| [🤖 06](../../Module06) | [Agents IA & Appel de fonction](./Module06/README.md) | Frameworks d'agents & MCP | Introduction aux agents • Appel de fonction • Protocole de contexte de modèle | Avancé | 4-5 h |
| [💻 07](../../Module07) | [Implémentation plateforme](./Module07/README.md) | Exemples multiplateformes | Boîte à outils IA • Foundry Local • Développement Windows | Avancé | 3-4 h |
| [🏭 08](../../Module08) | [Boîte à outils Foundry Local](./Module08/README.md) | Exemples prêts pour la production | Applications exemples (voir détails ci-dessous) | Expert | 8-10 h |

### 🏭 **Module 08 : Applications exemples**

- [01 : Démarrage rapide REST Chat](./Module08/samples/01/README.md)
- [02 : Intégration SDK OpenAI](./Module08/samples/02/README.md)
- [03 : Découverte & Benchmarking de modèles](./Module08/samples/03/README.md)
- [04 : Application Chainlit RAG](./Module08/samples/04/README.md)
- [05 : Orchestration multi-agent](./Module08/samples/05/README.md)
- [06 : Routeur Models-as-Tools](./Module08/samples/06/README.md)
- [07 : Client API direct](./Module08/samples/07/README.md)
- [08 : Application de chat Windows 11](./Module08/samples/08/README.md)
- [09 : Système multi-agent avancé](./Module08/samples/09/README.md)
- [10 : Framework Foundry Tools](./Module08/samples/10/README.md)

### 🎓 **Atelier : Parcours d'apprentissage pratique**

Matériel complet d'atelier pratique avec implémentations prêtes pour la production :

- **[Guide de l'atelier](./Workshop/Readme.md)** - Objectifs d'apprentissage complets, résultats et navigation des ressources
- **Exemples Python** (6 sessions) - Mis à jour avec les meilleures pratiques, gestion des erreurs et documentation complète
- **Carnets Jupyter** (8 interactifs) - Tutoriels étape par étape avec benchmarks et suivi des performances
- **Guides de session** - Guides markdown détaillés pour chaque session d'atelier
- **Outils de validation** - Scripts pour vérifier la qualité du code et exécuter des tests de fumée

**Ce que vous construirez :**
- Applications de chat IA locales avec support de streaming
- Pipelines RAG avec évaluation de qualité (RAGAS)
- Outils de benchmarking et comparaison multi-modèles
- Systèmes d'orchestration multi-agent
- Routage intelligent de modèles avec sélection basée sur les tâches

### 📊 **Résumé du parcours d'apprentissage**
- **Durée totale** : 36-45 heures
- **Parcours débutant** : Modules 01-02 (7-9 heures)  
- **Parcours intermédiaire** : Modules 03-04 (9-11 heures)
- **Parcours avancé** : Modules 05-07 (12-15 heures)
- **Parcours expert** : Module 08 (8-10 heures)

## Ce que vous construirez

### 🎯 Compétences clés
- **Architecture Edge AI** : Concevoir des systèmes IA locaux avec intégration cloud
- **Optimisation des modèles** : Quantification et compression des modèles pour le déploiement en périphérie (gain de vitesse de 85 %, réduction de taille de 75 %)
- **Déploiement multiplateforme** : Windows, mobile, embarqué et systèmes hybrides cloud-périphérie
- **Opérations en production** : Surveillance, mise à l’échelle et maintenance de l’IA en périphérie en production

### 🏗️ Projets pratiques
- **Applications de chat locales Foundry** : Application native Windows 11 avec changement de modèle
- **Systèmes multi-agents** : Coordinateur avec agents spécialistes pour des flux de travail complexes  
- **Applications RAG** : Traitement local de documents avec recherche vectorielle
- **Routeurs de modèles** : Sélection intelligente entre modèles basée sur l’analyse des tâches
- **Cadres API** : Clients prêts pour la production avec streaming et surveillance de la santé
- **Outils multiplateformes** : Modèles d’intégration LangChain/Semantic Kernel

### 🏢 Applications industrielles
**Fabrication** • **Santé** • **Véhicules autonomes** • **Villes intelligentes** • **Applications mobiles**

## Démarrage rapide

**Parcours d’apprentissage recommandé** (20-30 heures au total) :

0. **📖 Introduction** ([Introduction.md](./introduction.md)) : Fondations EdgeAI + contexte industriel + cadre d’apprentissage
1. **📚 Fondations** (Modules 01-02) : Concepts EdgeAI + familles de modèles SLM
2. **⚙️ Optimisation** (Modules 03-04) : Déploiement + cadres de quantification  
3. **🚀 Production** (Modules 05-06) : SLMOps + agents IA + appels de fonctions
4. **💻 Implémentation** (Modules 07-08) : Exemples de plateformes + boîte à outils Foundry Local

Chaque module comprend théorie, exercices pratiques et exemples de code prêts pour la production.

## Impact sur la carrière

**Rôles techniques** : Architecte solutions EdgeAI • Ingénieur ML (Edge) • Développeur IA IoT • Développeur IA mobile

**Secteurs industriels** : Fabrication 4.0 • Technologies de santé • Systèmes autonomes • FinTech • Électronique grand public

**Projets de portfolio** : Systèmes multi-agents • Applications RAG en production • Déploiement multiplateforme • Optimisation des performances

## Structure du dépôt

```
edgeai-for-beginners/
├── 📖 introduction.md  # Foundation: EdgeAI Overview & Learning Framework
├── 📚 Module01-04/     # Fundamentals → SLMs → Deployment → Optimization  
├── 🔧 Module05-06/     # SLMOps → AI Agents → Function Calling
├── 💻 Module07/        # Platform Samples (VS Code, Windows, Jetson, Mobile)
├── 🏭 Module08/        # Foundry Local Toolkit + 10 Comprehensive Samples
│   ├── samples/01-06/  # Foundation: REST, SDK, RAG, Agents, Routing
│   └── samples/07-10/  # Advanced: API Client, Windows App, Enterprise Agents, Tools
├── 🌐 translations/    # Multi-language support (8+ languages)
└── 📋 STUDY_GUIDE.md   # Structured learning paths & time allocation
```

## Points forts du cours

✅ **Apprentissage progressif** : Théorie → Pratique → Déploiement en production  
✅ **Études de cas réelles** : Microsoft, Japan Airlines, implémentations en entreprise  
✅ **Exemples pratiques** : Plus de 50 exemples, 10 démonstrations complètes Foundry Local  
✅ **Focus performance** : Améliorations de vitesse de 85 %, réductions de taille de 75 %  
✅ **Multiplateforme** : Windows, mobile, embarqué, hybride cloud-périphérie  
✅ **Prêt pour la production** : Surveillance, mise à l’échelle, sécurité, cadres de conformité

📖 **[Guide d’étude disponible](STUDY_GUIDE.md)** : Parcours d’apprentissage structuré de 20 heures avec conseils de gestion du temps et outils d’auto-évaluation.

---

**EdgeAI représente l’avenir du déploiement de l’IA** : local-first, respectueux de la vie privée et efficace. Maîtrisez ces compétences pour construire la prochaine génération d’applications intelligentes.

## Autres cours

Notre équipe produit d’autres cours ! Découvrez :

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j for Beginners](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js for Beginners](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)

---

### Azure / Edge / MCP / Agents
[![AZD for Beginners](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Edge AI for Beginners](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP for Beginners](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![AI Agents for Beginners](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Série IA générative
[![Generative AI for Beginners](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Generative AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![Generative AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![Generative AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### Apprentissage fondamental
[![ML for Beginners](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![Data Science for Beginners](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![AI for Beginners](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![Cybersecurity for Beginners](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![Web Dev for Beginners](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![IoT for Beginners](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![XR Development for Beginners](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Série Copilot
[![Copilot for AI Paired Programming](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot for C#/.NET](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot Adventure](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## Obtenir de l’aide

Si vous êtes bloqué ou avez des questions sur la création d’applications IA, rejoignez :

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Si vous avez des retours produit ou des erreurs lors du développement, visitez :

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :  
Ce document a été traduit à l’aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d’assurer l’exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d’origine doit être considéré comme la source faisant foi. Pour les informations critiques, une traduction professionnelle réalisée par un humain est recommandée. Nous déclinons toute responsabilité en cas de malentendus ou d’interprétations erronées résultant de l’utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8421c922085232ba081c848d98f69f35",
  "translation_date": "2026-01-01T09:46:18+00:00",
  "source_file": "README.md",
  "language_code": "fr"
}
-->
# EdgeAI pour les débutants 


![Image de couverture du cours](../../translated_images/cover.eb18d1b9605d754b.fr.png)

[![Contributeurs GitHub](https://img.shields.io/github/contributors/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/graphs/contributors)
[![Problèmes GitHub](https://img.shields.io/github/issues/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/issues)
[![Pull-requests GitHub](https://img.shields.io/github/issues-pr/microsoft/edgeai-for-beginners.svg)](https://GitHub.com/microsoft/edgeai-for-beginners/pulls)
[![PRs bienvenus](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

[![Observateurs GitHub](https://img.shields.io/github/watchers/microsoft/edgeai-for-beginners.svg?style=social&label=Watch)](https://GitHub.com/microsoft/edgeai-for-beginners/watchers)
[![Forks GitHub](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork)
[![Étoiles GitHub](https://img.shields.io/github/stars/microsoft/edgeai-for-beginners?style=social&label=Star)](https://GitHub.com/microsoft/edgeai-for-beginners/stargazers)


[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Suivez ces étapes pour commencer à utiliser ces ressources :

1. **Forker le dépôt** : Cliquez [![Forks GitHub](https://img.shields.io/github/forks/microsoft/edgeai-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/edgeai-for-beginners/fork)
2. **Cloner le dépôt** :   `git clone https://github.com/microsoft/edgeai-for-beginners.git`
3. [**Rejoignez le Discord Azure AI Foundry et rencontrez des experts et d'autres développeurs**](https://discord.com/invite/ByRwuEEgH4)


### 🌐 Support multilingue

#### Pris en charge via GitHub Action (Automatisé et toujours à jour)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabe](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgare](../bg/README.md) | [Birman (Myanmar)](../my/README.md) | [Chinois (simplifié)](../zh/README.md) | [Chinois (traditionnel, Hong Kong)](../hk/README.md) | [Chinois (traditionnel, Macao)](../mo/README.md) | [Chinois (traditionnel, Taïwan)](../tw/README.md) | [Croate](../hr/README.md) | [Tchèque](../cs/README.md) | [Danois](../da/README.md) | [Néerlandais](../nl/README.md) | [Estonien](../et/README.md) | [Finnois](../fi/README.md) | [Français](./README.md) | [Allemand](../de/README.md) | [Grec](../el/README.md) | [Hébreu](../he/README.md) | [Hindi](../hi/README.md) | [Hongrois](../hu/README.md) | [Indonésien](../id/README.md) | [Italien](../it/README.md) | [Japonais](../ja/README.md) | [Kannada](../kn/README.md) | [Coréen](../ko/README.md) | [Lituanien](../lt/README.md) | [Malais](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Népalais](../ne/README.md) | [Pidgin nigérian](../pcm/README.md) | [Norvégien](../no/README.md) | [Persan (Farsi)](../fa/README.md) | [Polonais](../pl/README.md) | [Portugais (Brésil)](../br/README.md) | [Portugais (Portugal)](../pt/README.md) | [Pendjabi (Gurmukhi)](../pa/README.md) | [Roumain](../ro/README.md) | [Russe](../ru/README.md) | [Serbe (cyrillique)](../sr/README.md) | [Slovaque](../sk/README.md) | [Slovène](../sl/README.md) | [Espagnol](../es/README.md) | [Swahili](../sw/README.md) | [Suédois](../sv/README.md) | [Tagalog (philippin)](../tl/README.md) | [Tamoul](../ta/README.md) | [Télougou](../te/README.md) | [Thaïlandais](../th/README.md) | [Turc](../tr/README.md) | [Ukrainien](../uk/README.md) | [Ourdou](../ur/README.md) | [Vietnamien](../vi/README.md)
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

**Si vous souhaitez disposer de langues de traduction supplémentaires prises en charge, elles sont répertoriées [ici](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md)**
## Introduction

Bienvenue dans **EdgeAI for Beginners** – votre parcours complet dans le monde transformateur de l'intelligence artificielle en périphérie. Ce cours comble le fossé entre des capacités d'IA puissantes et un déploiement pratique et réel sur des appareils en périphérie, vous permettant d'exploiter le potentiel de l'IA directement là où les données sont générées et où les décisions doivent être prises.

### Ce que vous maîtriserez

Ce cours vous emmène des concepts fondamentaux aux implémentations prêtes pour la production, en couvrant :
- **Petits modèles de langage (SLMs)** optimisés pour le déploiement en périphérie
- **Optimisation consciente du matériel** sur diverses plateformes
- **Inférence en temps réel** avec des fonctionnalités préservant la vie privée
- **Stratégies de déploiement en production** pour les applications d'entreprise

### Pourquoi EdgeAI est important

Edge AI représente un changement de paradigme qui répond à des défis modernes critiques :
- **Confidentialité et sécurité** : Traitez les données sensibles localement sans exposition au cloud
- **Performances en temps réel** : Éliminez la latence réseau pour les applications critiques temporellement
- **Efficacité des coûts** : Réduisez la bande passante et les dépenses de calcul cloud
- **Opérations résilientes** : Maintenez la fonctionnalité pendant les pannes réseau
- **Conformité réglementaire** : Répondez aux exigences de souveraineté des données

### Edge AI

Edge AI désigne l'exécution d'algorithmes d'IA et de modèles de langage localement sur le matériel, à proximité de l'endroit où les données sont générées, sans dépendre des ressources cloud pour l'inférence. Cela réduit la latence, renforce la confidentialité et permet une prise de décision en temps réel.

### Principes fondamentaux :
- **Inférence sur appareil** : Les modèles d'IA s'exécutent sur des appareils en périphérie (téléphones, routeurs, microcontrôleurs, PC industriels)
- **Capacité hors ligne** : Fonctionne sans connectivité Internet persistante
- **Faible latence** : Réponses immédiates adaptées aux systèmes en temps réel
- **Souveraineté des données** : Conserve les données sensibles localement, améliorant la sécurité et la conformité

### Petits modèles de langage (SLMs)

Les SLMs comme Phi-4, Mistral-7B et Gemma sont des versions optimisées de LLMs plus grands — entraînées ou distillées pour :
- **Empreinte mémoire réduite** : Utilisation efficace de la mémoire limitée des appareils en périphérie
- **Demande de calcul plus faible** : Optimisés pour les performances CPU et GPU en périphérie
- **Temps de démarrage plus rapides** : Initialisation rapide pour des applications réactives

Ils débloquent des capacités NLP puissantes tout en respectant les contraintes de :
- **Systèmes embarqués** : appareils IoT et contrôleurs industriels
- **Appareils mobiles** : smartphones et tablettes avec capacités hors ligne
- **Appareils IoT** : capteurs et dispositifs intelligents aux ressources limitées
- **Serveurs en périphérie** : unités de traitement locales avec ressources GPU limitées
- **Ordinateurs personnels** : scénarios de déploiement sur bureau et portable

## Modules du cours et navigation

| Module | Sujet | Domaine d'intérêt | Contenu clé | Niveau | Durée |
|--------|-------|------------|-------------|--------|----------|
| [📖 00 ](./introduction.md) | [Introduction to EdgeAI](./introduction.md) | Fondements & contexte | Aperçu d'EdgeAI • Applications industrielles • Introduction aux SLMs • Objectifs d'apprentissage | Débutant | 1-2 h |
| [📚 01](../../Module01) | [Fondamentaux d'EdgeAI](./Module01/README.md) | Comparaison Cloud vs Edge AI | Fondamentaux d'EdgeAI • Études de cas réelles • Guide de mise en œuvre • Déploiement en périphérie | Débutant | 3-4 h |
| [🧠 02](../../Module02) | [Fondements des modèles SLM](./Module02/README.md) | Familles de modèles & architecture | Phi Family • Qwen Family • Gemma Family • BitNET • μModel • Phi-Silica | Débutant | 4-5 h |
| [🚀 03](../../Module03) | [Pratique de déploiement SLM](./Module03/README.md) | Déploiement local & cloud | Apprentissage avancé • Environnement local • Déploiement cloud | Intermédiaire | 4-5 h |
| [⚙️ 04](../../Module04) | [Boîte à outils d'optimisation de modèles](./Module04/README.md) | Optimisation multiplateforme | Introduction • Llama.cpp • Microsoft Olive • OpenVINO • Apple MLX • Synthèse de workflow | Intermédiaire | 5-6 h |
| [🔧 05](../../Module05) | [SLMOps Production](./Module05/README.md) | Opérations de production | Introduction à SLMOps • Distillation de modèles • Fine-tuning • Déploiement en production | Avancé | 5-6 h |
| [🤖 06](../../Module06) | [Agents IA & Appels de fonction](./Module06/README.md) | Cadres d'agents & MCP | Introduction aux agents • Appels de fonction • Protocole de contexte de modèle | Avancé | 4-5 h |
| [💻 07](../../Module07) | [Implémentation de plate-forme](./Module07/README.md) | Exemples multiplateformes | Boîte à outils IA • Foundry Local • Développement Windows | Avancé | 3-4 h |
| [🏭 08](../../Module08) | [Foundry Local Toolkit](./Module08/README.md) | Exemples prêts pour la production | Applications d'exemple (voir les détails ci-dessous) | Expert | 8-10 h |

### 🏭 **Module 08 : Applications d'exemple**

- [01: REST Chat Démarrage rapide](./Module08/samples/01/README.md)
- [02: Intégration du SDK OpenAI](./Module08/samples/02/README.md)
- [03: Découverte et benchmarking de modèles](./Module08/samples/03/README.md)
- [04: Application Chainlit RAG](./Module08/samples/04/README.md)
- [05: Orchestration multi-agents](./Module08/samples/05/README.md)
- [06: Routeur Modèles-comme-Outils](./Module08/samples/06/README.md)
- [07: Client API direct](./Module08/samples/07/README.md)
- [08: Application de chat Windows 11](./Module08/samples/08/README.md)
- [09: Système multi-agent avancé](./Module08/samples/09/README.md)
- [10: Cadre Foundry Tools](./Module08/samples/10/README.md)

### 🎓 **Atelier : Parcours d'apprentissage pratique**

Matériels d'atelier pratiques complets avec implémentations prêtes pour la production :

- **[Guide de l'atelier](./Workshop/Readme.md)** - Objectifs d'apprentissage complets, résultats et navigation des ressources
- **Exemples Python** (6 sessions) - Mis à jour avec les meilleures pratiques, la gestion des erreurs et une documentation complète
- **Jupyter Notebooks** (8 interactifs) - Tutoriels pas à pas avec benchmarks et surveillance des performances
- **Guides de session** - Guides Markdown détaillés pour chaque session d'atelier
- **Outils de validation** - Scripts pour vérifier la qualité du code et exécuter des tests de fumée

**Ce que vous allez construire :**
- Applications de chat IA locales avec prise en charge du streaming
- Pipelines RAG avec évaluation de la qualité (RAGAS)
- Outils de benchmarking et de comparaison multi-modèles
- Systèmes d'orchestration multi-agents
- Routage intelligent de modèles avec sélection basée sur les tâches

### 📊 **Résumé du parcours d'apprentissage**
- **Durée totale** : 36-45 heures
- **Parcours Débutant** : Modules 01-02 (7-9 heures)  
- **Parcours Intermédiaire** : Modules 03-04 (9-11 heures)
- **Parcours Avancé** : Modules 05-07 (12-15 heures)
- **Parcours Expert** : Module 08 (8-10 heures)

## Ce que vous allez construire

### 🎯 Compétences clés
- **Architecture Edge AI** : Concevez des systèmes d'IA locaux avec intégration cloud
- **Optimisation des modèles**: Quantifier et compresser les modèles pour le déploiement en périphérie (85% speed boost, 75% size reduction)
- **Déploiement multiplateforme**: Windows, mobile, embarqué, et systèmes hybrides cloud-périphérie
- **Opérations en production**: Surveillance, mise à l'échelle et maintien de l'IA en périphérie en production

### 🏗️ Projets pratiques
- **Applications de chat locales Foundry**: Application native Windows 11 avec commutation de modèles
- **Systèmes multi-agents**: Coordinateur avec agents spécialistes pour des flux de travail complexes  
- **Applications RAG**: Traitement local de documents avec recherche vectorielle
- **Routeurs de modèles**: Sélection intelligente entre modèles basée sur l'analyse des tâches
- **Cadres d'API**: Clients prêts pour la production avec streaming et surveillance de l'état
- **Outils multiplateformes**: Modèles d'intégration LangChain/Semantic Kernel

### 🏢 Applications industrielles
**Industrie manufacturière** • **Santé** • **Véhicules autonomes** • **Villes intelligentes** • **Applications mobiles**

## Démarrage rapide

**Parcours d'apprentissage recommandé** (20-30 hours total):

0. **📖 Introduction** ([Introduction.md](./introduction.md)): Fondements d'EdgeAI + contexte industriel + cadre d'apprentissage
1. **📚 Fondamentaux** (Modules 01-02): Concepts EdgeAI + familles de modèles SLM
2. **⚙️ Optimisation** (Modules 03-04): Déploiement + frameworks de quantification  
3. **🚀 Production** (Modules 05-06): SLMOps + agents IA + appels de fonctions
4. **💻 Implémentation** (Modules 07-08): Exemples de plateformes + kit d'outils Foundry Local

Chaque module inclut la théorie, des exercices pratiques et des exemples de code prêts pour la production.

## Impact sur la carrière

**Rôles techniques**: Architecte Solutions EdgeAI • Ingénieur ML (Edge) • Développeur IA IoT • Développeur IA mobile

**Secteurs industriels**: Industrie 4.0 • Technologies de la santé • Systèmes autonomes • FinTech • Électronique grand public

**Projets pour le portfolio**: Systèmes multi-agents • Applications RAG en production • Déploiement multiplateforme • Optimisation des performances

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

✅ **Apprentissage progressif**: Théorie → Pratique → Déploiement en production  
✅ **Études de cas réelles**: Microsoft, Japan Airlines, implémentations d'entreprise  
✅ **Exemples pratiques**: 50+ exemples, 10 démos complètes Foundry Local  
✅ **Accent sur la performance**: 85% speed improvements, 75% size reductions  
✅ **Multiplateforme**: Windows, mobile, embarqué, hybride cloud-périphérie  
✅ **Prêt pour la production**: Surveillance, mise à l'échelle, sécurité, cadres de conformité

📖 **[Guide d'étude disponible](STUDY_GUIDE.md)**: Parcours d'apprentissage structuré de 20 heures avec guide d'allocation du temps et outils d'auto-évaluation.

---

**EdgeAI représente l'avenir du déploiement de l'IA**: local-first, protection de la vie privée, et efficience. Maîtrisez ces compétences pour construire la prochaine génération d'applications intelligentes.

## Autres cours

Notre équipe propose d'autres cours ! Découvrez :

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j pour débutants](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js pour débutants](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)

---

### Azure / Edge / MCP / Agents
[![AZD pour débutants](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Edge AI pour débutants](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP pour débutants](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Agents IA pour débutants](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Série IA générative
[![IA générative pour débutants](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![IA générative (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![IA générative (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![IA générative (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### Apprentissage de base
[![ML pour débutants](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![Science des données pour débutants](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![IA pour débutants](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![Cybersécurité pour débutants](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![Développement Web pour débutants](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![IoT pour débutants](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![Développement XR pour débutants](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Série Copilot
[![Copilot pour programmation assistée par IA](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot pour C#/.NET](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Aventure Copilot](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## Obtenir de l'aide

Si vous êtes bloqué ou si vous avez des questions sur la création d'applications IA, rejoignez :

[![Discord Microsoft Foundry](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Si vous avez des retours produit ou des erreurs lors du développement, visitez :

[![Forum développeurs Microsoft Foundry](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Clause de non-responsabilité** :
Ce document a été traduit à l'aide du service de traduction par IA [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original, dans sa langue d'origine, doit être considéré comme la source faisant foi. Pour les informations critiques, il est recommandé de recourir à une traduction professionnelle effectuée par un traducteur humain. Nous déclinons toute responsabilité pour tout malentendu ou mauvaise interprétation résultant de l'utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
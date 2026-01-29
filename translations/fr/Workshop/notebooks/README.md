# Cahiers d'Atelier

> **Cahiers interactifs Jupyter pour un apprentissage pratique de l'IA Edge**
>
> Tutoriels progressifs et autonomes allant des complétions de chat basiques aux systèmes multi-agents avancés, utilisant Microsoft Foundry Local et des modèles de langage réduits.

---

## 📖 Introduction

Bienvenue dans la collection des **Cahiers d'Atelier EdgeAI pour Débutants**. Ces cahiers interactifs Jupyter offrent une expérience d'apprentissage pratique où vous écrirez, exécuterez et expérimenterez du code d'IA Edge en temps réel.

### Pourquoi utiliser les cahiers Jupyter ?

Contrairement aux tutoriels traditionnels, ces cahiers offrent :

- **Apprentissage interactif** : Exécutez des cellules de code et voyez les résultats immédiatement
- **Expérimentation** : Modifiez les paramètres et observez les changements en temps réel
- **Documentation** : Explications intégrées et cellules markdown pour vous guider à travers les concepts
- **Reproductibilité** : Exemples fonctionnels complets que vous pouvez consulter et réutiliser
- **Visualisation** : Affichez les métriques de performance, les embeddings et les résultats directement dans le cahier

### Qu'est-ce qui rend ces cahiers spéciaux ?

Chaque cahier est conçu selon les **meilleures pratiques prêtes pour la production** :

✅ **Gestion complète des erreurs** - Dégradation progressive et messages d'erreur informatifs  
✅ **Annotations de type et documentation** - Signatures de fonctions claires et docstrings  
✅ **Suivi de performance** - Surveillance de l'utilisation des tokens et des mesures de latence  
✅ **Conception modulaire** - Modèles réutilisables que vous pouvez adapter à vos projets  
✅ **Complexité progressive** - Construction systématique sur les sessions précédentes  

---

## 🎯 Objectifs d'apprentissage

### Compétences principales que vous développerez

En travaillant sur ces cahiers, vous maîtriserez :

1. **Gestion des services d'IA locaux**
   - Configurer et gérer les services Microsoft Foundry Local
   - Sélectionner et charger les modèles adaptés à votre matériel
   - Surveiller l'utilisation des ressources et optimiser les performances
   - Gérer la découverte des services et vérifier leur état de santé

2. **Développement d'applications d'IA**
   - Implémenter des complétions de chat compatibles avec OpenAI localement
   - Construire des interfaces de streaming pour une meilleure expérience utilisateur
   - Concevoir des invites efficaces pour les modèles de langage réduits
   - Intégrer des modèles locaux dans des applications

3. **Génération augmentée par récupération (RAG)**
   - Créer une recherche sémantique avec des embeddings vectoriels
   - Ancrer les réponses des modèles de langage dans des documents spécifiques au domaine
   - Évaluer la qualité RAG avec les métriques RAGAS
   - Passer du prototype à la production

4. **Optimisation des performances**
   - Évaluer systématiquement plusieurs modèles
   - Mesurer la latence, le débit et le temps du premier token
   - Comparer les modèles de langage réduits (SLM) et les modèles de langage larges (LLM)
   - Sélectionner les modèles optimaux en fonction des compromis entre performance et qualité

5. **Orchestration multi-agents**
   - Concevoir des agents spécialisés pour différentes tâches
   - Implémenter la mémoire des agents et la gestion du contexte
   - Coordonner plusieurs agents dans des flux de travail complexes
   - Construire des modèles de coordination pour la collaboration entre agents

6. **Routage intelligent des modèles**
   - Implémenter la détection d'intention et la correspondance de motifs
   - Router automatiquement les requêtes vers les modèles appropriés
   - Construire des pipelines multi-étapes (planifier → exécuter → affiner)
   - Concevoir des architectures évolutives de modèles comme outils

---

## 🎓 Résultats d'apprentissage

### Ce que vous allez construire

| Cahier | Livrable | Compétences démontrées | Difficulté |
|--------|----------|-------------------------|------------|
| **Session 01** | Application de chat avec streaming | Configuration du service, complétions basiques, UX de streaming | ⭐ Débutant |
| **Session 02 (RAG)** | Pipeline RAG avec évaluation | Embeddings, recherche sémantique, métriques de qualité | ⭐⭐ Intermédiaire |
| **Session 02 (Évaluation)** | Évaluateur de qualité RAG | Métriques RAGAS, évaluation systématique | ⭐⭐ Intermédiaire |
| **Session 03** | Benchmark multi-modèles | Mesure de performance, comparaison de modèles | ⭐⭐ Intermédiaire |
| **Session 04** | Comparateur SLM vs LLM | Analyse des compromis, stratégies d'optimisation | ⭐⭐⭐ Avancé |
| **Session 05** | Orchestrateur multi-agents | Conception d'agents, mémoire, coordination | ⭐⭐⭐ Avancé |
| **Session 06 (Router)** | Système de routage intelligent | Détection d'intention, sélection de modèles | ⭐⭐⭐ Avancé |
| **Session 06 (Pipeline)** | Pipeline multi-étapes | Flux de travail planifier/exécuter/affiner | ⭐⭐⭐ Avancé |

### Progression des compétences

```
Session 01 ────► Session 02 ────► Session 03 ────► Session 04 ────► Session 05-06
   Basic            RAG             Benchmarking      Comparison      Multi-Agent
   Chat             Systems         & Performance     & Optimization  Orchestration
   
Foundation    │   Intermediate   │   Advanced       │   Expert
──────────────┴──────────────────┴──────────────────┴──────────────►
```

---

## 📅 Programme de l'atelier

### 🚀 Atelier d'une demi-journée (3,5 heures)

**Idéal pour : Sessions de formation en équipe, hackathons, ateliers de conférence**

| Heure | Durée | Session | Sujets | Activités |
|-------|-------|---------|--------|-----------|
| **0:00** | 30 min | Configuration & Introduction | Configuration de l'environnement, installation de Foundry Local | Installer les dépendances, vérifier la configuration |
| **0:30** | 30 min | Session 01 | Complétions de chat basiques, streaming | Exécuter le cahier, modifier les invites |
| **1:00** | 45 min | Session 02 | Pipeline RAG, embeddings, évaluation | Construire un système RAG, tester les requêtes |
| **1:45** | 15 min | Pause | ☕ Café & questions | — |
| **2:00** | 30 min | Session 03 | Benchmark multi-modèles | Comparer 3+ modèles |
| **2:30** | 30 min | Session 04 | Compromis SLM vs LLM | Analyser performance/qualité |
| **3:00** | 30 min | Sessions 05-06 | Systèmes multi-agents & routage | Explorer des modèles avancés |

**Résultat** : Les participants repartent avec 6 applications Edge AI fonctionnelles et des modèles de code prêts pour la production.

---

### 🎓 Atelier d'une journée complète (6 heures)

**Idéal pour : Formation approfondie, bootcamps, cours universitaires**

| Heure | Durée | Session | Sujets | Activités |
|-------|-------|---------|--------|-----------|
| **0:00** | 45 min | Configuration & Théorie | Configuration de l'environnement, fondamentaux de l'IA Edge | Installer, vérifier, discuter des cas d'utilisation |
| **0:45** | 45 min | Session 01 | Exploration approfondie des complétions de chat | Implémenter un chat basique & en streaming |
| **1:30** | 30 min | Pause | ☕ Café & réseautage | — |
| **2:00** | 60 min | Session 02 (les deux) | Pipeline RAG + Évaluation RAGAS | Construire un système RAG complet |
| **3:00** | 30 min | Atelier pratique 1 | RAG personnalisé pour votre domaine | Appliquer à vos propres documents |
| **3:30** | 30 min | Déjeuner | 🍽️ | — |
| **4:00** | 45 min | Session 03 | Méthodologie de benchmarking | Comparaison systématique des modèles |
| **4:45** | 45 min | Session 04 | Stratégies d'optimisation | Analyse SLM vs LLM |
| **5:30** | 60 min | Sessions 05-06 | Orchestration avancée | Systèmes multi-agents, routage |
| **6:30** | 30 min | Atelier pratique 2 | Construire un système d'agents personnalisé | Concevoir votre propre orchestrateur |

**Résultat** : Compréhension approfondie des modèles d'IA Edge plus 2 projets personnalisés.

---

### 📚 Apprentissage autonome (2 semaines)

**Idéal pour : Apprenants individuels, cours en ligne, auto-apprentissage**

#### Semaine 1 : Fondamentaux (6 heures)

| Jour | Focus | Durée | Cahiers | Devoirs |
|------|-------|-------|---------|---------|
| **Lun** | Configuration & Bases | 1,5 h | Session 01 | Modifier les invites, tester le streaming |
| **Mer** | Fondamentaux RAG | 2 h | Session 02 (les deux) | Ajouter vos propres documents |
| **Ven** | Benchmarking | 1,5 h | Session 03 | Comparer des modèles supplémentaires |
| **Sam** | Révision & Pratique | 1 h | Tous les cahiers de la semaine 1 | Compléter les exercices, déboguer |

#### Semaine 2 : Avancé (5 heures)

| Jour | Focus | Durée | Cahiers | Devoirs |
|------|-------|-------|---------|---------|
| **Lun** | Optimisation | 1,5 h | Session 04 | Documenter les compromis |
| **Mer** | Systèmes multi-agents | 2 h | Session 05 | Concevoir des agents personnalisés |
| **Ven** | Routage intelligent | 1,5 h | Session 06 (les deux) | Construire une logique de routage |
| **Sam** | Projet final | 2 h | Intégration | Combiner plusieurs modèles |

**Résultat** : Maîtrise des modèles d'IA Edge plus projet de portfolio.

---

## 📔 Descriptions des cahiers

### 📘 Session 01 : Démarrage du chat
**Fichier** : `session01_chat_bootstrap.ipynb`  
**Durée** : 20-30 minutes  
**Prérequis** : Aucun  
**Difficulté** : ⭐ Débutant

**Ce que vous apprendrez** :
- Installer et configurer le SDK Python Foundry Local
- Utiliser `FoundryLocalManager` pour la découverte automatique des services
- Implémenter des complétions de chat basiques avec une API compatible OpenAI
- Construire des réponses en streaming pour une meilleure expérience utilisateur
- Gérer les erreurs et les indisponibilités des services de manière élégante

**Concepts clés** : Gestion des services, complétions de chat, streaming, gestion des erreurs

**Ce que vous construirez** : Application de chat interactive avec support de streaming

---

### 📗 Session 02 : Pipeline RAG
**Fichier** : `session02_rag_pipeline.ipynb`  
**Durée** : 30-45 minutes  
**Prérequis** : Session 01  
**Difficulté** : ⭐⭐ Intermédiaire

**Ce que vous apprendrez** :
- Implémenter le modèle de Génération Augmentée par Récupération (RAG)
- Créer des embeddings vectoriels avec sentence-transformers
- Construire une recherche sémantique avec la similarité cosinus
- Ancrer les réponses des modèles de langage dans des documents spécifiques au domaine
- Gérer les dépendances optionnelles avec des gardes d'importation

**Concepts clés** : Architecture RAG, embeddings, recherche sémantique, similarité vectorielle

**Ce que vous construirez** : Système de questions-réponses basé sur des documents

---

### 📗 Session 02 : Évaluation RAG avec RAGAS
**Fichier** : `session02_rag_eval_ragas.ipynb`  
**Durée** : 30-45 minutes  
**Prérequis** : Pipeline RAG de la session 02  
**Difficulté** : ⭐⭐ Intermédiaire

**Ce que vous apprendrez** :
- Évaluer la qualité RAG avec des métriques standard de l'industrie
- Mesurer la pertinence du contexte, la pertinence des réponses, la fidélité
- Utiliser le cadre RAGAS pour une évaluation systématique
- Identifier et corriger les problèmes de qualité RAG
- Construire des ensembles de données d'évaluation pour votre domaine

**Concepts clés** : Évaluation RAG, métriques RAGAS, mesure de qualité, tests systématiques

**Ce que vous construirez** : Cadre d'évaluation de la qualité RAG

---

### 📙 Session 03 : Benchmark des modèles OSS
**Fichier** : `session03_benchmark_oss_models.ipynb`  
**Durée** : 30-45 minutes  
**Prérequis** : Session 01  
**Difficulté** : ⭐⭐ Intermédiaire

**Ce que vous apprendrez** :
- Évaluer systématiquement plusieurs modèles
- Mesurer la latence, le débit, le temps du premier token
- Implémenter une dégradation progressive en cas d'échec des modèles
- Comparer les performances entre familles de modèles
- Visualiser et analyser les résultats des benchmarks

**Concepts clés** : Benchmarking de performance, mesure de latence, comparaison de modèles, analyse statistique

**Ce que vous construirez** : Suite de benchmarking multi-modèles

---

### 📙 Session 04 : Comparaison des modèles (SLM vs LLM)
**Fichier** : `session04_model_compare.ipynb`  
**Durée** : 30-45 minutes  
**Prérequis** : Sessions 01, 03  
**Difficulté** : ⭐⭐⭐ Avancé

**Ce que vous apprendrez** :
- Comparer les modèles de langage réduits (SLM) et les modèles de langage larges (LLM)
- Analyser les compromis entre performance et qualité
- Mesurer les métriques de compatibilité avec les contraintes Edge
- Sélectionner les modèles optimaux pour les contraintes de déploiement
- Documenter les critères de décision pour la sélection des modèles

**Concepts clés** : Sélection de modèles, analyse des compromis, stratégies d'optimisation, planification de déploiement

**Ce que vous construirez** : Cadre de comparaison SLM vs LLM

---

### 📕 Session 05 : Orchestrateur multi-agents
**Fichier** : `session05_agents_orchestrator.ipynb`  
**Durée** : 45-60 minutes  
**Prérequis** : Sessions 01-02  
**Difficulté** : ⭐⭐⭐ Avancé

**Ce que vous apprendrez** :
- Concevoir des agents spécialisés pour différentes tâches
- Implémenter la mémoire des agents et la gestion du contexte
- Construire des modèles de coordination pour la collaboration entre agents
- Gérer la communication et les transferts entre agents
- Surveiller les performances du système multi-agents

**Concepts clés** : Architecture des agents, modèles de coordination, gestion de la mémoire, orchestration des agents

**Ce que vous construirez** : Système multi-agents avec coordinateur et spécialistes

---

### 📕 Session 06 : Routeur de modèles
**Fichier** : `session06_models_router.ipynb`  
**Durée** : 30-45 minutes  
**Prérequis** : Sessions 01, 03  
**Difficulté** : ⭐⭐⭐ Avancé

**Ce que vous apprendrez** :
- Implémenter la détection d'intention et la correspondance de motifs
- Construire un routage de modèles basé sur des mots-clés
- Router automatiquement les requêtes vers les modèles appropriés
- Configurer des registres multi-modèles
- Surveiller les décisions de routage et les performances

**Concepts clés** : Détection d'intention, routage de modèles, correspondance de motifs, sélection intelligente

**Ce que vous construirez** : Système de routage intelligent des modèles

---

### 📕 Session 06 : Pipeline multi-étapes
**Fichier** : `session06_models_pipeline.ipynb`  
**Durée** : 30-45 minutes  
**Prérequis** : Sessions 01, Routeur de la session 06  
**Difficulté** : ⭐⭐⭐ Avancé

**Ce que vous apprendrez** :
- Construire des pipelines d'IA multi-étapes (planifier → exécuter → affiner)
- Intégrer un routeur pour une sélection intelligente des modèles
- Implémenter la gestion des erreurs et la récupération dans le pipeline
- Surveiller les performances et les étapes du pipeline
- Concevoir des architectures évolutives de modèles comme outils

**Concepts clés** : Architecture de pipeline, traitement en plusieurs étapes, récupération des erreurs, modèles de scalabilité

**Ce que vous allez construire** : Pipeline intelligent multi-étapes avec routage

---

## 🚀 Premiers Pas

### Prérequis

**Configuration système** :
- **OS** : Windows 10/11, macOS 11+ ou Linux (Ubuntu 20.04+)
- **RAM** : 8 Go minimum, 16 Go+ recommandé
- **Stockage** : 10 Go+ d'espace libre pour les modèles
- **Matériel** : CPU avec AVX2 ; GPU (CUDA, Qualcomm NPU) optionnel

**Configuration logicielle** :
- **Python 3.8+** avec pip
- **Jupyter Notebook** ou **VS Code** avec extension Jupyter
- **Microsoft Foundry Local** installé et configuré
- **Git** (pour cloner le dépôt)

### Étapes d'installation

#### 1. Installer Foundry Local

**Windows** :
```cmd
winget install Microsoft.FoundryLocal
```

**macOS** :
```bash
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**Vérifier l'installation** :
```bash
foundry --version
```

#### 2. Configurer l'environnement Python

```bash
# Navigate to Workshop directory
cd Workshop

# Create virtual environment
python -m venv .venv

# Activate virtual environment
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

#### 3. Démarrer Foundry Local

```bash
# Load a model (auto-downloads if needed)
foundry model run phi-4-mini

# Verify service is running
foundry service status
```

#### 4. Lancer Jupyter

```bash
# Start Jupyter Notebook
jupyter notebook notebooks/

# Or use VS Code with Jupyter extension
code notebooks/
```

### Vérification rapide

Exécutez ceci dans une cellule Python pour vérifier la configuration :

```python
from foundry_local import FoundryLocalManager
import openai

# Initialize manager (auto-discovers service)
manager = FoundryLocalManager("phi-4-mini")

# Configure OpenAI client
client = openai.OpenAI(
    base_url=manager.endpoint,
    api_key=manager.api_key
)

# Test chat completion
response = client.chat.completions.create(
    model=manager.get_model_info("phi-4-mini").id,
    messages=[{"role": "user", "content": "Hello!"}]
)

print(response.choices[0].message.content)
```

**Résultat attendu** : Une réponse de salutation du modèle local.

---

## 📝 Bonnes pratiques pour l'atelier

### Pour les formateurs

**Avant l'atelier** :
- ✅ Envoyer les instructions d'installation une semaine à l'avance
- ✅ Tester tous les notebooks sur le matériel cible
- ✅ Préparer un guide de dépannage pour les problèmes courants
- ✅ Avoir des modèles de secours prêts (phi-3.5-mini si phi-4-mini échoue)
- ✅ Configurer un canal de discussion partagé pour les questions

**Pendant l'atelier** :
- ✅ Commencer par une vérification rapide de l'environnement (5 minutes)
- ✅ Partager immédiatement les ressources de dépannage
- ✅ Encourager l'expérimentation et les modifications
- ✅ Utiliser les pauses stratégiquement (après chaque 2 sessions)
- ✅ Avoir des assistants disponibles pour une aide individuelle

**Après l'atelier** :
- ✅ Partager les notebooks complets et fonctionnels ainsi que les solutions
- ✅ Fournir des liens vers des ressources supplémentaires
- ✅ Créer un sondage de feedback pour améliorer
- ✅ Proposer des heures de bureau pour les questions de suivi

### Pour les apprenants

**Maximisez votre apprentissage** :
- ✅ Complétez la configuration avant le début de l'atelier
- ✅ Exécutez chaque cellule de code vous-même (ne vous contentez pas de lire)
- ✅ Expérimentez avec les paramètres et les invites
- ✅ Prenez des notes sur les idées et les pièges
- ✅ Posez des questions en cas de blocage (d'autres ont probablement la même question)

**Erreurs courantes à éviter** :
- ❌ Ignorer l'ordre d'exécution des cellules (exécutez-les séquentiellement)
- ❌ Ne pas lire attentivement les messages d'erreur
- ❌ Se précipiter sans comprendre
- ❌ Ignorer les explications en markdown
- ❌ Ne pas sauvegarder vos notebooks modifiés

**Conseils de dépannage** :
1. **Service non démarré** : Vérifiez `foundry service status`
2. **Erreurs d'importation** : Vérifiez que l'environnement virtuel est activé
3. **Modèle introuvable** : Exécutez `foundry model ls` pour lister les modèles chargés
4. **Performance lente** : Vérifiez l'utilisation de la RAM, fermez les autres applications
5. **Résultats inattendus** : Redémarrez le kernel et exécutez toutes les cellules depuis le début

---

## 🔗 Ressources supplémentaires

### Matériel de l'atelier

- **[Guide principal de l'atelier](../Readme.md)** - Vue d'ensemble, objectifs d'apprentissage, résultats professionnels
- **[Exemples Python](../../../../Workshop/samples)** - Scripts Python correspondants pour chaque session
- **[Guides de session](../../../../Workshop)** - Guides détaillés en markdown (Session01-06)
- **[Scripts](../../../../Workshop/scripts)** - Utilitaires de validation et de test
- **[Dépannage](./TROUBLESHOOTING.md)** - Problèmes courants et solutions
- **[Démarrage rapide](./quickstart.md)** - Guide de démarrage rapide

### Documentation

- **[Docs Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)** - Documentation officielle de Microsoft
- **[SDK Python OpenAI](https://github.com/openai/openai-python)** - Référence SDK OpenAI
- **[Sentence Transformers](https://www.sbert.net/)** - Documentation des modèles d'embedding
- **[Framework RAGAS](https://docs.ragas.io/)** - Métriques d'évaluation RAG

### Communauté

- **[Discussions GitHub](https://github.com/microsoft/edgeai-for-beginners/discussions)** - Posez des questions, partagez des projets
- **[Discord Azure AI Foundry](https://discord.com/invite/ByRwuEEgH4)** - Support communautaire en temps réel
- **[Stack Overflow](https://stackoverflow.com/questions/tagged/foundry-local)** - Questions techniques et réponses

---

## 🎯 Recommandations de parcours d'apprentissage

### Parcours débutant (Commencez ici)

1. **Session 01** - Démarrage du chat
2. **Session 02** - Pipeline RAG
3. **Session 03** - Benchmark des modèles

**Durée** : ~2 heures | **Focus** : Modèles fondamentaux

---

### Parcours intermédiaire

1. Complétez le parcours débutant
2. **Session 02** - Évaluation RAG
3. **Session 04** - Comparaison des modèles

**Durée** : ~4 heures | **Focus** : Qualité et optimisation

---

### Parcours avancé (Atelier complet)

1. Complétez le parcours intermédiaire
2. **Session 05** - Orchestrateur multi-agents
3. **Session 06** - Routeur de modèles
4. **Session 06** - Pipeline multi-étapes

**Durée** : ~6 heures | **Focus** : Modèles de production

---

### Parcours projet personnalisé

1. Complétez le parcours débutant (Sessions 01-03)
2. Choisissez UNE session avancée en fonction de votre objectif :
   - **Créer une application RAG ?** → Évaluation Session 02
   - **Optimiser la performance ?** → Comparaison Session 04
   - **Workflows complexes ?** → Orchestrateur Session 05
   - **Architecture évolutive ?** → Routeur + Pipeline Session 06

**Durée** : ~3 heures | **Focus** : Compétences spécifiques au projet

---

## 📊 Indicateurs de succès

Suivez votre progression avec ces étapes clés :

- [ ] **Configuration terminée** - Foundry Local opérationnel, toutes les dépendances installées
- [ ] **Premier chat** - Session 01 terminée, chat en streaming fonctionnel
- [ ] **RAG construit** - Session 02 terminée, système de QA documentaire fonctionnel
- [ ] **Modèles benchmarkés** - Session 03 terminée, données de performance collectées
- [ ] **Analyse des compromis** - Session 04 terminée, critères de sélection des modèles documentés
- [ ] **Agents orchestrés** - Session 05 terminée, système multi-agents opérationnel
- [ ] **Routage implémenté** - Session 06 terminée, sélection intelligente de modèles fonctionnelle
- [ ] **Projet personnalisé** - Application des modèles de l'atelier à votre propre cas d'utilisation

---

## 🤝 Contribuer

Vous avez trouvé un problème ou une suggestion ? Nous accueillons vos contributions !

- **Signaler des problèmes** : [GitHub Issues](https://github.com/microsoft/edgeai-for-beginners/issues)
- **Proposer des améliorations** : [GitHub Discussions](https://github.com/microsoft/edgeai-for-beginners/discussions)
- **Soumettre des PRs** : Suivez les [Directives de contribution](../../AGENTS.md)

---

## 📄 Licence

Cet atelier fait partie du dépôt [EdgeAI for Beginners](https://github.com/microsoft/edgeai-for-beginners) et est sous licence [MIT License](../../../../LICENSE).

---

**Prêt à créer des applications Edge AI prêtes pour la production ?**  
**Commencez avec [Session 01 : Démarrage du chat](./session01_chat_bootstrap.ipynb) →**

---

*Dernière mise à jour : 8 octobre 2025 | Version de l'atelier : 2.0*

---

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction humaine professionnelle. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées résultant de l'utilisation de cette traduction.
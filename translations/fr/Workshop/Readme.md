<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "45923ada94573fee7c82cc4f0c3bb344",
  "translation_date": "2025-10-28T20:02:09+00:00",
  "source_file": "Workshop/Readme.md",
  "language_code": "fr"
}
-->
# EdgeAI pour Débutants - Atelier

> **Parcours d'apprentissage pratique pour créer des applications d'IA à la pointe de la technologie prêtes pour la production**
>
> Maîtrisez le déploiement local de l'IA avec Microsoft Foundry Local, depuis la première complétion de chat jusqu'à l'orchestration multi-agents en 6 sessions progressives.

---

## 🎯 Introduction

Bienvenue à l'**Atelier EdgeAI pour Débutants** - votre guide pratique pour créer des applications intelligentes fonctionnant entièrement sur du matériel local. Cet atelier transforme les concepts théoriques de l'Edge AI en compétences pratiques à travers des exercices progressifs utilisant Microsoft Foundry Local et des Small Language Models (SLMs).

### Pourquoi cet atelier ?

**La révolution Edge AI est en marche**

Les organisations du monde entier passent de l'IA dépendante du cloud à l'informatique en périphérie pour trois raisons essentielles :

1. **Confidentialité & Conformité** - Traitez les données sensibles localement sans transmission dans le cloud (HIPAA, RGPD, réglementations financières)
2. **Performance** - Éliminez la latence réseau (50-500ms local contre 500-2000ms aller-retour dans le cloud)
3. **Maîtrise des coûts** - Supprimez les coûts par jeton des API et évoluez sans frais liés au cloud

**Mais l'Edge AI est différent**

Faire fonctionner l'IA sur site nécessite de nouvelles compétences :
- Sélection et optimisation des modèles pour des contraintes de ressources
- Gestion des services locaux et accélération matérielle
- Conception de prompts pour des modèles plus petits
- Modèles de déploiement en production pour les appareils en périphérie

**Cet atelier vous apporte ces compétences**

En 6 sessions ciblées (~3 heures au total), vous passerez de "Hello World" au déploiement de systèmes multi-agents prêts pour la production - le tout fonctionnant localement sur votre machine.

---

## 📚 Objectifs d'apprentissage

En complétant cet atelier, vous serez capable de :

### Compétences de base
1. **Déployer et gérer des services d'IA locaux**
   - Installer et configurer Microsoft Foundry Local
   - Sélectionner les modèles appropriés pour un déploiement en périphérie
   - Gérer le cycle de vie des modèles (téléchargement, chargement, mise en cache)
   - Surveiller l'utilisation des ressources et optimiser les performances

2. **Créer des applications alimentées par l'IA**
   - Implémenter des complétions de chat compatibles OpenAI localement
   - Concevoir des prompts efficaces pour les Small Language Models
   - Gérer les réponses en streaming pour une meilleure expérience utilisateur
   - Intégrer des modèles locaux dans des applications existantes

3. **Créer des systèmes RAG (Retrieval Augmented Generation)**
   - Construire une recherche sémantique avec des embeddings
   - Ancrer les réponses des LLM dans des connaissances spécifiques au domaine
   - Évaluer la qualité des RAG avec des métriques standard de l'industrie
   - Passer du prototype à la production

4. **Optimiser les performances des modèles**
   - Évaluer plusieurs modèles pour votre cas d'utilisation
   - Mesurer la latence, le débit et le temps du premier jeton
   - Sélectionner les modèles optimaux en fonction des compromis vitesse/qualité
   - Comparer les compromis SLM vs LLM dans des scénarios réels

5. **Orchestrer des systèmes multi-agents**
   - Concevoir des agents spécialisés pour différentes tâches
   - Implémenter la mémoire des agents et la gestion du contexte
   - Coordonner les agents dans des flux de travail complexes
   - Acheminer intelligemment les requêtes entre plusieurs modèles

6. **Déployer des solutions prêtes pour la production**
   - Implémenter la gestion des erreurs et la logique de reprise
   - Surveiller l'utilisation des jetons et les ressources système
   - Construire des architectures évolutives avec des modèles comme outils
   - Planifier des chemins de migration de la périphérie vers l'hybride (périphérie + cloud)

---

## 🎓 Résultats d'apprentissage

### Ce que vous allez construire

À la fin de cet atelier, vous aurez créé :

| Session | Livrable | Compétences démontrées |
|---------|----------|-------------------------|
| **1** | Application de chat avec streaming | Configuration du service, complétions de base, UX en streaming |
| **2** | Système RAG avec évaluation | Embeddings, recherche sémantique, métriques de qualité |
| **3** | Suite de benchmarks multi-modèles | Mesure des performances, comparaison des modèles |
| **4** | Comparateur SLM vs LLM | Analyse des compromis, stratégies d'optimisation |
| **5** | Orchestrateur multi-agents | Conception d'agents, gestion de la mémoire, coordination |
| **6** | Système de routage intelligent | Détection d'intention, sélection de modèles, évolutivité |

### Matrice de compétences

| Niveau de compétence | Session 1-2 | Session 3-4 | Session 5-6 |
|-----------------------|-------------|-------------|-------------|
| **Débutant** | ✅ Configuration & bases | ⚠️ Défi | ❌ Trop avancé |
| **Intermédiaire** | ✅ Révision rapide | ✅ Apprentissage clé | ⚠️ Objectifs ambitieux |
| **Avancé** | ✅ Facile | ✅ Affinement | ✅ Modèles de production |

### Compétences prêtes pour le marché

**Après cet atelier, vous serez prêt à :**

✅ **Créer des applications axées sur la confidentialité**
- Applications de santé traitant des données PHI/PII localement
- Services financiers avec exigences de conformité
- Systèmes gouvernementaux avec besoins de souveraineté des données

✅ **Optimiser pour les environnements en périphérie**
- Appareils IoT avec ressources limitées
- Applications mobiles fonctionnant hors ligne
- Systèmes en temps réel à faible latence

✅ **Concevoir des architectures intelligentes**
- Systèmes multi-agents pour des flux de travail complexes
- Déploiements hybrides périphérie-cloud
- Infrastructures IA optimisées en termes de coûts

✅ **Diriger des initiatives Edge AI**
- Évaluer la faisabilité de l'Edge AI pour des projets
- Sélectionner les modèles et frameworks appropriés
- Concevoir des solutions d'IA locales évolutives

---

## 🗺️ Structure de l'atelier

### Aperçu des sessions (6 sessions × 30 minutes = 3 heures)

| Session | Sujet | Focus | Durée |
|---------|-------|-------|-------|
| **1** | Premiers pas avec Foundry Local | Installation, validation, premières complétions | 30 min |
| **2** | Construire des solutions IA avec RAG | Conception de prompts, embeddings, évaluation | 30 min |
| **3** | Modèles open source | Découverte, benchmarking, sélection | 30 min |
| **4** | Modèles de pointe | SLM vs LLM, optimisation, frameworks | 30 min |
| **5** | Agents alimentés par l'IA | Conception d'agents, orchestration, mémoire | 30 min |
| **6** | Modèles comme outils | Routage, enchaînement, stratégies d'évolutivité | 30 min |

---

## 🚀 Démarrage rapide

### Prérequis

**Configuration système :**
- **OS** : Windows 10/11, macOS 11+ ou Linux (Ubuntu 20.04+)
- **RAM** : 8 Go minimum, 16 Go+ recommandé
- **Stockage** : 10 Go+ d'espace libre pour les modèles
- **CPU** : Processeur moderne avec support AVX2
- **GPU** (optionnel) : Compatible CUDA ou NPU Qualcomm pour l'accélération

**Logiciels requis :**
- **Python 3.8+** ([Télécharger](https://www.python.org/downloads/))
- **Microsoft Foundry Local** ([Guide d'installation](../../../Workshop))
- **Git** ([Télécharger](https://git-scm.com/downloads))
- **Visual Studio Code** (recommandé) ([Télécharger](https://code.visualstudio.com/))

### Configuration en 3 étapes

#### 1. Installer Foundry Local

**Windows :**
```powershell
winget install Microsoft.FoundryLocal
```

**macOS :**
```bash
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**Vérifier l'installation :**
```bash
foundry --version
foundry service status
```

**Assurez-vous que Azure AI Foundry Local fonctionne avec un port fixe**

```bash
# Set FoundryLocal to use port 58123 (default)
foundry service set --port 58123 --show

# Or use a different port
foundry service set --port 58000 --show
```

**Vérifiez son fonctionnement :**
```bash
# Check service status
foundry service status

# Test the endpoint
curl http://127.0.0.1:58123/v1/models
```
**Recherche des modèles disponibles**
Pour voir quels modèles sont disponibles dans votre instance Foundry Local, vous pouvez interroger le point de terminaison des modèles :

```bash
# cmd/bash/powershell
foundry model list
```

Utilisation du point de terminaison Web 

```bash
# Windows PowerShell
powershell -Command "Invoke-RestMethod -Uri 'http://127.0.0.1:58123/v1/models' -Method Get"

# Or using curl (if available)
curl http://127.0.0.1:58123/v1/models
```

#### 2. Cloner le dépôt & installer les dépendances

```bash
# Clone repository
git clone https://github.com/microsoft/edgeai-for-beginners.git
cd edgeai-for-beginners/Workshop

# Create virtual environment
python -m venv .venv

# Activate virtual environment
# Windows:
.\.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

#### 3. Exécuter votre premier exemple

```bash
# Start Foundry Local and load a model
foundry model run phi-4-mini

# Run the chat bootstrap sample
cd samples
python -m session01.chat_bootstrap "What is edge AI?"
```

**✅ Succès !** Vous devriez voir une réponse en streaming sur l'Edge AI.

---

## 📦 Ressources de l'atelier

### Exemples Python

Exemples pratiques progressifs démontrant chaque concept :

| Session | Exemple | Description | Durée d'exécution |
|---------|---------|-------------|-------------------|
| 1 | [`chat_bootstrap.py`](../../../Workshop/samples/session01/chat_bootstrap.py) | Chat de base & streaming | ~30s |
| 2 | [`rag_pipeline.py`](../../../Workshop/samples/session02/rag_pipeline.py) | RAG avec embeddings | ~45s |
| 2 | [`rag_eval_ragas.py`](../../../Workshop/samples/session02/rag_eval_ragas.py) | Évaluation de la qualité RAG | ~60s |
| 3 | [`benchmark_oss_models.py`](../../../Workshop/samples/session03/benchmark_oss_models.py) | Benchmarking multi-modèles | ~2-3m |
| 4 | [`model_compare.py`](../../../Workshop/samples/session04/model_compare.py) | Comparaison SLM vs LLM | ~45s |
| 5 | [`agents_orchestrator.py`](../../../Workshop/samples/session05/agents_orchestrator.py) | Système multi-agents | ~60s |
| 6 | [`models_router.py`](../../../Workshop/samples/session06/models_router.py) | Routage basé sur l'intention | ~45s |
| 6 | [`models_pipeline.py`](../../../Workshop/samples/session06/models_pipeline.py) | Pipeline multi-étapes | ~60s |

### Notebooks Jupyter

Exploration interactive avec explications et visualisations :

| Session | Notebook | Description | Difficulté |
|---------|----------|-------------|------------|
| 1 | [`session01_chat_bootstrap.ipynb`](./notebooks/session01_chat_bootstrap.ipynb) | Bases du chat & streaming | ⭐ Débutant |
| 2 | [`session02_rag_pipeline.ipynb`](./notebooks/session02_rag_pipeline.ipynb) | Construire un système RAG | ⭐⭐ Intermédiaire |
| 2 | [`session02_rag_eval_ragas.ipynb`](./notebooks/session02_rag_eval_ragas.ipynb) | Évaluer la qualité RAG | ⭐⭐ Intermédiaire |
| 3 | [`session03_benchmark_oss_models.ipynb`](./notebooks/session03_benchmark_oss_models.ipynb) | Benchmarking des modèles | ⭐⭐ Intermédiaire |
| 4 | [`session04_model_compare.ipynb`](./notebooks/session04_model_compare.ipynb) | Comparaison des modèles | ⭐⭐ Intermédiaire |
| 5 | [`session05_agents_orchestrator.ipynb`](./notebooks/session05_agents_orchestrator.ipynb) | Orchestration d'agents | ⭐⭐⭐ Avancé |
| 6 | [`session06_models_router.ipynb`](./notebooks/session06_models_router.ipynb) | Routage basé sur l'intention | ⭐⭐⭐ Avancé |
| 6 | [`session06_models_pipeline.ipynb`](./notebooks/session06_models_pipeline.ipynb) | Orchestration de pipeline | ⭐⭐⭐ Avancé |

### Documentation

Guides et références complets :

| Document | Description | À utiliser quand |
|----------|-------------|------------------|
| [QUICK_START.md](./QUICK_START.md) | Guide de configuration rapide | Débuter à partir de zéro |
| [QUICK_REFERENCE.md](./QUICK_REFERENCE.md) | Fiche de référence commandes & API | Besoin de réponses rapides |
| [FOUNDRY_SDK_QUICKREF.md](./FOUNDRY_SDK_QUICKREF.md) | Modèles et exemples SDK | Écrire du code |
| [ENV_CONFIGURATION.md](./ENV_CONFIGURATION.md) | Guide des variables d'environnement | Configurer les exemples |
| [SAMPLES_UPDATE_SUMMARY.md](./SAMPLES_UPDATE_SUMMARY.md) | Améliorations récentes des exemples | Comprendre les changements |
| [SDK_MIGRATION_NOTES.md](./SDK_MIGRATION_NOTES.md) | Guide de migration | Mettre à jour le code |
| [notebooks/TROUBLESHOOTING.md](./notebooks/TROUBLESHOOTING.md) | Problèmes courants & solutions | Résoudre les problèmes |

---

## 🎓 Recommandations pour le parcours d'apprentissage

### Pour les débutants (3-4 heures)
1. ✅ Session 1 : Premiers pas (concentrez-vous sur la configuration et le chat de base)
2. ✅ Session 2 : Bases du RAG (ignorez l'évaluation au début)
3. ✅ Session 3 : Benchmarking simple (2 modèles seulement)
4. ⏭️ Ignorez les sessions 4-6 pour l'instant
5. 🔄 Revenez aux sessions 4-6 après avoir créé votre première application

### Pour les développeurs intermédiaires (3 heures)
1. ⚡ Session 1 : Validation rapide de la configuration
2. ✅ Session 2 : Pipeline RAG complet avec évaluation
3. ✅ Session 3 : Suite complète de benchmarking
4. ✅ Session 4 : Optimisation des modèles
5. ✅ Sessions 5-6 : Concentrez-vous sur les modèles d'architecture

### Pour les praticiens avancés (2-3 heures)
1. ⚡ Sessions 1-3 : Révision rapide et validation
2. ✅ Session 4 : Approfondissement de l'optimisation
3. ✅ Session 5 : Architecture multi-agents
4. ✅ Session 6 : Modèles de production et évolutivité
5. 🚀 Extension : Construisez une logique de routage personnalisée et des déploiements hybrides

---

## Pack de sessions d'atelier (laboratoires concentrés de 30 minutes)

Si vous suivez le format condensé de l'atelier en 6 sessions, utilisez ces guides dédiés (chacun correspond et complète les modules plus larges ci-dessus) :

| Session d'atelier | Guide | Focus principal |
|-------------------|-------|-----------------|
| 1 | [Session01-GettingStartedFoundryLocal](./Session01-GettingStartedFoundryLocal.md) | Installation, validation, exécution de phi & GPT-OSS-20B, accélération |
| 2 | [Session02-BuildAISolutionsRAG](./Session02-BuildAISolutionsRAG.md) | Conception de prompts, modèles RAG, ancrage de documents & CSV, migration |
| 3 | [Session03-OpenSourceModels](./Session03-OpenSourceModels.md) | Intégration Hugging Face, benchmarking, sélection de modèles |
| 4 | [Session04-CuttingEdgeModels](./Session04-CuttingEdgeModels.md) | SLM vs LLM, WebGPU, Chainlit RAG, accélération ONNX |
| 5 | [Session05-AIPoweredAgents](./Session05-AIPoweredAgents.md) | Rôles des agents, mémoire, outils, orchestration |
| 6 | [Session06-ModelsAsTools](./Session06-ModelsAsTools.md) | Routage, enchaînement, mise à l'échelle vers Azure |

Chaque fichier de session inclut : résumé, objectifs d'apprentissage, démonstration de 30 minutes, projet de démarrage, liste de validation, dépannage et références au SDK Python Foundry Local officiel.

### Scripts d'exemple

Installer les dépendances de l'atelier (Windows) :

```powershell
cd Workshop
py -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

macOS / Linux :

```bash
cd Workshop
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Si le service Foundry Local est exécuté sur une autre machine (Windows) ou VM depuis macOS, exportez l'endpoint :

```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```

| Session | Script(s) | Description |
|---------|-----------|-------------|
| 1 | `samples/session01/chat_bootstrap.py` | Service de démarrage & chat en streaming |
| 2 | `samples/session02/rag_pipeline.py` | RAG minimal (embeddings en mémoire) |
|   | `samples/session02/rag_eval_ragas.py` | Évaluation RAG avec métriques ragas |
| 3 | `samples/session03/benchmark_oss_models.py` | Benchmarking multi-modèle : latence & débit |
| 4 | `samples/session04/model_compare.py` | Comparaison SLM vs LLM (latence & exemples de sortie) |
| 5 | `samples/session05/agents_orchestrator.py` | Pipeline de recherche → éditorial à deux agents |
| 6 | `samples/session06/models_router.py` | Démo de routage basé sur l'intention |
|   | `samples/session06/models_pipeline.py` | Chaîne planifier/exécuter/affiner en plusieurs étapes |

### Variables d'environnement (communes à tous les exemples)

| Variable | Objectif | Exemple |
|----------|----------|---------|
| `FOUNDRY_LOCAL_ALIAS` | Alias de modèle unique par défaut pour les exemples de base | `phi-4-mini` |
| `SLM_ALIAS` / `LLM_ALIAS` | SLM explicite vs modèle plus grand pour comparaison | `phi-4-mini` / `gpt-oss-20b` |
| `BENCH_MODELS` | Liste d'alias à tester en benchmark | `qwen2.5-0.5b,mistral-7b` |
| `BENCH_ROUNDS` | Répétitions de benchmark par modèle | `3` |
| `BENCH_PROMPT` | Prompt utilisé pour le benchmark | `Explain retrieval augmented generation briefly.` |
| `EMBED_MODEL` | Modèle d'embedding sentence-transformers | `sentence-transformers/all-MiniLM-L6-v2` |
| `RAG_QUESTION` | Remplace la requête de test pour le pipeline RAG | `Why use RAG with local inference?` |
| `AGENT_QUESTION` | Remplace la requête du pipeline d'agents | `Explain why edge AI matters for compliance.` |
| `AGENT_MODEL_PRIMARY` | Alias du modèle pour l'agent de recherche | `phi-4-mini` |
| `AGENT_MODEL_EDITOR` | Alias du modèle pour l'agent éditeur (peut différer) | `gpt-oss-20b` |
| `SHOW_USAGE` | Si `1`, affiche l'utilisation des tokens par complétion | `1` |
| `RETRY_ON_FAIL` | Si `1`, réessaie une fois en cas d'erreur de chat transitoire | `1` |
| `RETRY_BACKOFF` | Secondes à attendre avant de réessayer | `1.0` |

Si une variable n'est pas définie, les scripts utilisent des valeurs par défaut raisonnables. Pour les démonstrations avec un seul modèle, vous n'avez généralement besoin que de `FOUNDRY_LOCAL_ALIAS`.

### Module utilitaire

Tous les exemples partagent désormais un utilitaire `samples/workshop_utils.py` qui fournit :

* Création mise en cache de `FoundryLocalManager` + client OpenAI
* Fonction d'aide `chat_once()` avec option de réessai + affichage de l'utilisation
* Rapport simple sur l'utilisation des tokens (activé via `SHOW_USAGE=1`)

Cela réduit la duplication et met en avant les meilleures pratiques pour une orchestration efficace des modèles locaux.

## Améliorations optionnelles (inter-sessions)

| Thème | Amélioration | Sessions | Env / Basculer |
|-------|-------------|----------|----------------|
| Déterminisme | Température fixe + ensembles de prompts stables | 1–6 | Définir `temperature=0`, `top_p=1` |
| Visibilité de l'utilisation des tokens | Enseignement cohérent des coûts/efficacité | 1–6 | `SHOW_USAGE=1` |
| Premier token en streaming | Métrique de latence perçue | 1,3,4,6 | `BENCH_STREAM=1` (benchmark) |
| Résilience au réessai | Gère les démarrages à froid transitoires | Tous | `RETRY_ON_FAIL=1` + `RETRY_BACKOFF` |
| Agents multi-modèles | Spécialisation des rôles hétérogènes | 5 | `AGENT_MODEL_PRIMARY`, `AGENT_MODEL_EDITOR` |
| Routage adaptatif | Intention + heuristiques de coût | 6 | Étendre le routeur avec une logique d'escalade |
| Mémoire vectorielle | Rappel sémantique à long terme | 2,5,6 | Intégrer un index d'embedding FAISS/Chroma |
| Exportation de traces | Audit & évaluation | 2,5,6 | Ajouter des lignes JSON par étape |
| Rubriques de qualité | Suivi qualitatif | 3–6 | Prompts de notation secondaire |
| Tests rapides | Validation rapide avant atelier | Tous | `python Workshop/tests/smoke.py` |

### Démarrage rapide déterministe

```powershell
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
python Workshop\tests\smoke.py
```

Attendez-vous à des comptes de tokens stables pour des entrées identiques répétées.

### Évaluation RAG (Session 2)

Utilisez `rag_eval_ragas.py` pour calculer la pertinence des réponses, leur fidélité et la précision contextuelle sur un petit ensemble de données synthétiques :

```powershell
cd Workshop/samples
python -m session02.rag_eval_ragas
```

Étendez en fournissant un JSONL plus grand de questions, contextes et vérités terrain, puis convertissez-le en un `Dataset` Hugging Face.

## Annexe sur la précision des commandes CLI

L'atelier utilise uniquement des commandes CLI Foundry Local documentées et stables.

### Commandes stables référencées

| Catégorie | Commande | Objectif |
|-----------|----------|----------|
| Noyau | `foundry --version` | Affiche la version installée |
| Noyau | `foundry init` | Initialise la configuration |
| Service | `foundry service start` | Démarre le service local (si non automatique) |
| Service | `foundry status` | Affiche l'état du service |
| Modèles | `foundry model list` | Liste le catalogue / les modèles disponibles |
| Modèles | `foundry model download <alias>` | Télécharge les poids du modèle dans le cache |
| Modèles | `foundry model run <alias>` | Lance (charge) un modèle localement ; à combiner avec `--prompt` pour un one-shot |
| Modèles | `foundry model unload <alias>` / `foundry model stop <alias>` | Décharge un modèle de la mémoire (si pris en charge) |
| Cache | `foundry cache list` | Liste les modèles mis en cache (téléchargés) |
| Système | `foundry system info` | Instantané des capacités matérielles & d'accélération |
| Système | `foundry system gpu-info` | Infos de diagnostic GPU |
| Config | `foundry config list` | Affiche les valeurs de configuration actuelles |
| Config | `foundry config set <key> <value>` | Met à jour la configuration |

### Modèle de prompt one-shot

Au lieu de la sous-commande obsolète `model chat`, utilisez :

```powershell
foundry model run <alias> --prompt "Your question here"
```

Cela exécute un cycle unique de prompt/réponse, puis se termine.

### Modèles supprimés / évités

| Obsolète / Non documenté | Remplacement / Conseils |
|--------------------------|-------------------------|
| `foundry model chat <model> "..."` | `foundry model run <model> --prompt "..."` |
| `foundry model list --running` | Utilisez simplement `foundry model list` + activité récente / journaux |
| `foundry model list --cached` | `foundry cache list` |
| `foundry model stats <model>` | Utilisez le script de benchmark Python + outils OS (Gestionnaire des tâches / `nvidia-smi`) |
| `foundry model benchmark ...` | `samples/session03/benchmark_oss_models.py` |

### Benchmarking & Télémétrie

- Latence, p95, tokens/sec : `samples/session03/benchmark_oss_models.py`
- Latence du premier token (streaming) : définissez `BENCH_STREAM=1`
- Utilisation des ressources : moniteurs OS (Gestionnaire des tâches, Moniteur d'activité, `nvidia-smi`) + `foundry system info`.

À mesure que de nouvelles commandes de télémétrie CLI se stabilisent en amont, elles peuvent être intégrées avec des modifications minimales aux fichiers markdown des sessions.

### Garde de lint automatisée

Un linter automatisé empêche la réintroduction de modèles CLI obsolètes dans les blocs de code des fichiers markdown :

Script : `Workshop/scripts/lint_markdown_cli.py`

Les modèles obsolètes sont bloqués dans les blocs de code.

Remplacements recommandés :
| Obsolète | Remplacement |
|----------|--------------|
| `foundry model chat <a> "..."` | `foundry model run <a> --prompt "..."` |
| `model list --running` | `model list` |
| `model list --cached` | `cache list` |
| `model stats` | Script de benchmark + outils système |
| `model benchmark` | `samples/session03/benchmark_oss_models.py` |
| `model list --available` | `model list` |

Exécuter localement :
```powershell
python Workshop\scripts\lint_markdown_cli.py --verbose
```

Action GitHub : `.github/workflows/markdown-cli-lint.yml` s'exécute à chaque push & PR.

Hook pré-commit optionnel :
```bash
echo "python Workshop/scripts/lint_markdown_cli.py" > .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```

## Tableau de migration rapide CLI → SDK

| Tâche | Ligne de commande CLI | Équivalent SDK (Python) | Remarques |
|-------|-----------------------|-------------------------|-----------|
| Exécuter un modèle une fois (prompt) | `foundry model run phi-4-mini --prompt "Hello"` | `manager=FoundryLocalManager("phi-4-mini"); client=OpenAI(base_url=manager.endpoint, api_key=manager.api_key or "not-needed"); client.chat.completions.create(model=manager.get_model_info("phi-4-mini").id, messages=[{"role":"user","content":"Hello"}])` | Le SDK initialise automatiquement le service & le cache |
| Télécharger (mettre en cache) un modèle | `foundry model download qwen2.5-0.5b` | `FoundryLocalManager("qwen2.5-0.5b")  # déclenche le téléchargement/chargement` | Le gestionnaire choisit la meilleure variante si l'alias correspond à plusieurs versions |
| Lister le catalogue | `foundry model list` | `# utiliser le gestionnaire pour chaque alias ou maintenir une liste connue` | Le CLI agrège ; le SDK actuellement par instanciation d'alias |
| Lister les modèles en cache | `foundry cache list` | `manager.list_cached_models()` | Après l'initialisation du gestionnaire (n'importe quel alias) |
| Activer l'accélération GPU | `foundry config set compute.onnx.enable_gpu true` | `# Action CLI ; le SDK suppose que la configuration est déjà appliquée` | La configuration est un effet secondaire externe |
| Obtenir l'URL de l'endpoint | (implicite) | `manager.endpoint` | Utilisé pour créer un client compatible OpenAI |
| Préparer un modèle | `foundry model run <alias>` puis premier prompt | `chat_once(alias, messages=[...])` (utilitaire) | Les utilitaires gèrent le préchauffage initial de la latence à froid |
| Mesurer la latence | `python -m session03.benchmark_oss_models` | `import benchmark_oss_models` (ou nouveau script d'exportation) | Préférez le script pour des métriques cohérentes |
| Arrêter / décharger un modèle | `foundry model unload <alias>` | (Non exposé – redémarrer le service / processus) | Généralement non nécessaire pour le flux de l'atelier |
| Récupérer l'utilisation des tokens | (voir la sortie) | `resp.usage.total_tokens` | Fourni si le backend renvoie un objet d'utilisation |

## Exportation Markdown de Benchmark

Utilisez le script `Workshop/scripts/export_benchmark_markdown.py` pour exécuter un benchmark récent (même logique que `samples/session03/benchmark_oss_models.py`) et générer un tableau Markdown compatible avec GitHub ainsi qu'un JSON brut.

### Exemple

```powershell
python Workshop\scripts\export_benchmark_markdown.py --models "qwen2.5-0.5b,mistral-7b" --prompt "Explain retrieval augmented generation briefly." --rounds 3 --output benchmark_report.md
```

Fichiers générés :
| Fichier | Contenu |
|---------|---------|
| `benchmark_report.md` | Tableau Markdown + conseils d'interprétation |
| `benchmark_report.json` | Tableau brut des métriques (pour comparaison / suivi des tendances) |

Définissez `BENCH_STREAM=1` dans l'environnement pour inclure la latence du premier token si pris en charge.

---

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction humaine professionnelle. Nous ne sommes pas responsables des malentendus ou des interprétations erronées résultant de l'utilisation de cette traduction.
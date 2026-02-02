# Échantillons de l'atelier - Carte de référence rapide

**Dernière mise à jour** : 8 octobre 2025

---

## 🚀 Démarrage rapide

```bash
# 1. Ensure Foundry Local is running
foundry service status
foundry model run phi-4-mini

# 2. Install dependencies
pip install -r Workshop/requirements.txt

# 3. Run a sample
cd Workshop/samples
python -m session01.chat_bootstrap "What is edge AI?"
```

---

## 📂 Aperçu des échantillons

| Session | Échantillon | Objectif | Temps |
|---------|-------------|----------|-------|
| 01 | `chat_bootstrap.py` | Chat basique + streaming | ~30s |
| 02 | `rag_pipeline.py` | RAG avec embeddings | ~45s |
| 02 | `rag_eval_ragas.py` | Évaluation RAG | ~60s |
| 03 | `benchmark_oss_models.py` | Benchmarking des modèles | ~2m |
| 04 | `model_compare.py` | SLM vs LLM | ~45s |
| 05 | `agents_orchestrator.py` | Système multi-agents | ~60s |
| 06 | `models_router.py` | Routage d'intention | ~45s |
| 06 | `models_pipeline.py` | Pipeline multi-étapes | ~60s |

---

## 🛠️ Variables d'environnement

### Essentielles
```bash
# Choose model
set FOUNDRY_LOCAL_ALIAS=phi-4-mini

# Override endpoint (optional)
set FOUNDRY_LOCAL_ENDPOINT=http://localhost:8000

# Show token usage
set SHOW_USAGE=1
```

### Spécifiques à la session
```bash
# Session 02: RAG
set RAG_QUESTION="What is local inference?"
set EMBED_MODEL=sentence-transformers/all-MiniLM-L6-v2

# Session 03: Benchmarking
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
set BENCH_ROUNDS=3
set BENCH_STREAM=1

# Session 04: Comparison
set SLM_ALIAS=phi-4-mini
set LLM_ALIAS=qwen2.5-7b

# Session 05: Agents
set AGENT_MODEL_PRIMARY=phi-4-mini
set AGENT_QUESTION="Why use edge AI?"

# Session 06: Pipeline
set PIPELINE_TASK="Your task here"
```

---

## ✅ Validation et tests

```bash
# Validate syntax and imports
python scripts/validate_samples.py

# Validate specific session
python scripts/validate_samples.py --session 01

# Run smoke tests
python scripts/test_samples.py --quick

# Verbose testing
python scripts/test_samples.py --verbose
```

---

## 🐛 Dépannage

### Erreur de connexion
```bash
# Check Foundry Local
foundry service status

# Start if needed
foundry service start
foundry model run phi-4-mini
```

### Erreur d'importation
```bash
# Install missing dependencies
pip install sentence-transformers ragas datasets

# Or install all
pip install -r Workshop/requirements.txt
```

### Modèle introuvable
```bash
# List available models
foundry model ls

# Download model
foundry model download phi-4-mini
```

### Performances lentes
```bash
# Use smaller model
set FOUNDRY_LOCAL_ALIAS=qwen2.5-0.5b

# Reduce benchmark rounds
set BENCH_ROUNDS=1
```

---

## 📖 Modèles courants

### Chat basique
```python
from workshop_utils import chat_once

text, usage = chat_once(
    'phi-4-mini',
    messages=[{"role": "user", "content": "Hello"}],
    max_tokens=100,
    temperature=0.7
)
```

### Obtenir un client
```python
from workshop_utils import get_client

manager, client, model_id = get_client(
    alias='phi-4-mini',
    endpoint=None  # Auto-detect
)
```

### Gestion des erreurs
```python
try:
    manager, client, model_id = get_client(alias)
except Exception as e:
    print(f"[ERROR] Failed: {e}")
    print("[INFO] Check: foundry service status")
    sys.exit(1)
```

### Streaming
```python
stream = client.chat.completions.create(
    model=model_id,
    messages=messages,
    stream=True
)

for chunk in stream:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="", flush=True)
```

---

## 📊 Sélection de modèles

| Modèle | Taille | Idéal pour | Vitesse |
|--------|--------|------------|---------|
| `qwen2.5-0.5b` | 0.5B | Classification rapide | ⚡⚡⚡ |
| `qwen2.5-coder-0.5b` | 0.5B | Génération de code rapide | ⚡⚡⚡ |
| `gemma-2-2b` | 2B | Écriture créative | ⚡⚡ |
| `phi-3.5-mini` | 3.5B | Code, refactoring | ⚡⚡ |
| `phi-4-mini` | 4B | Général, résumé | ⚡⚡ |
| `qwen2.5-7b` | 7B | Raisonnement complexe | ⚡ |

---

## 🔗 Ressources

- **Docs SDK** : https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- **Référence rapide** : `Workshop/FOUNDRY_SDK_QUICKREF.md`

---

## 💡 Conseils

1. **Cachez les clients** : `workshop_utils` gère le cache pour vous
2. **Utilisez des modèles plus petits** : Commencez avec `qwen2.5-0.5b` pour les tests
3. **Activez les statistiques d'utilisation** : Configurez `SHOW_USAGE=1` pour suivre les tokens
4. **Traitement par lots** : Traitez plusieurs invites de manière séquentielle
5. **Réduisez max_tokens** : Diminue la latence pour des réponses rapides

---

## 🎯 Flux de travail des échantillons

### Tout tester
```bash
python scripts/validate_samples.py
python scripts/test_samples.py --quick
```

### Benchmark des modèles
```bash
cd samples
set BENCH_MODELS=phi-4-mini,qwen2.5-0.5b
set BENCH_ROUNDS=3
python -m session03.benchmark_oss_models
```

### Pipeline RAG
```bash
cd samples
set RAG_QUESTION="What is RAG?"
python -m session02.rag_pipeline
```

### Système multi-agents
```bash
cd samples
set AGENT_QUESTION="Why edge AI for healthcare?"
python -m session05.agents_orchestrator
```

---

**Aide rapide** : Exécutez n'importe quel échantillon avec `--help` depuis le répertoire `samples` ou consultez le docstring :
```bash
python -c "import session01.chat_bootstrap; help(session01.chat_bootstrap)"
```

---

**Tous les échantillons mis à jour en octobre 2025 avec les meilleures pratiques du SDK Foundry Local** ✨

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction humaine professionnelle. Nous ne sommes pas responsables des malentendus ou des interprétations erronées résultant de l'utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
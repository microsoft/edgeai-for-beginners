# Session 6 : Foundry Local – Les modèles comme outils

## Résumé

Considérez les modèles comme des outils modulables au sein d'une couche opérationnelle locale d'IA. Cette session montre comment enchaîner plusieurs appels spécialisés SLM/LLM, router sélectivement les tâches et exposer une interface SDK unifiée aux applications. Vous construirez un routeur de modèles léger + un planificateur de tâches, l'intégrerez dans un script d'application et définirez la voie de mise à l'échelle vers Azure AI Foundry pour les charges de travail en production.

## Objectifs d'apprentissage

- **Conceptualiser** les modèles comme des outils atomiques avec des capacités déclarées
- **Router** les requêtes en fonction de l'intention / du score heuristique
- **Enchaîner** les sorties à travers des tâches en plusieurs étapes (décomposer → résoudre → affiner)
- **Intégrer** une API client unifiée pour les applications en aval
- **Mettre à l'échelle** la conception vers le cloud (même contrat compatible OpenAI)

## Prérequis

- Sessions 1 à 5 terminées
- Plusieurs modèles locaux mis en cache (par exemple, `phi-4-mini`, `deepseek-coder-1.3b`, `qwen2.5-0.5b`)

### Extrait d'environnement multiplateforme

Windows PowerShell :
```powershell
py -m venv .venv
 .\.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install foundry-local-sdk openai
```

macOS / Linux :
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install foundry-local-sdk openai
```

Accès au service distant/VM depuis macOS :
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```


## Déroulement de la démonstration (30 min)

### 1. Déclaration des capacités des outils (5 min)

Créer `samples/06-tools/models_catalog.py` :

```python
CATALOG = {
  "phi-4-mini": {
    "capabilities": ["general", "reasoning", "summarize"],
    "priority": 2
  },
  "deepseek-coder-1.3b": {
    "capabilities": ["code", "refactor", "explain_code"],
    "priority": 1
  },
  "qwen2.5-0.5b": {
    "capabilities": ["fast", "classification", "lightweight"],
    "priority": 3
  }
}
```


### 2. Détection d'intention et routage (8 min)

Créer `samples/06-tools/router.py` :

```python
#!/usr/bin/env python3
"""Model-as-tool router using Foundry Local OpenAI-compatible endpoint."""
from openai import OpenAI
from models_catalog import CATALOG
import re

client = OpenAI(base_url="http://localhost:5273/v1", api_key="not-needed")

INTENT_RULES = [
  (re.compile(r"code|function|refactor|bug|optimi", re.I), "code"),
  (re.compile(r"summari|abstract|tl;dr", re.I), "summarize"),
  (re.compile(r"classif|label|category", re.I), "classification"),
]

def detect_intent(prompt: str) -> str:
    for pat, intent in INTENT_RULES:
        if pat.search(prompt):
            return intent
    return "general"

def select_model(intent: str) -> str:
    # Score catalog: capability match first, then priority
    scored = []
    for name, meta in CATALOG.items():
        caps = meta["capabilities"]
        match = intent in caps
        scored.append((name, match, meta["priority"]))
    # Sort: match True first, then lowest priority value
    scored.sort(key=lambda t: (not t[1], t[2]))
    return scored[0][0]

def run(prompt: str):
    intent = detect_intent(prompt)
    model = select_model(intent)
    resp = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=400,
        temperature=0.5
    )
    return {"intent": intent, "model": model, "output": resp.choices[0].message.content}

if __name__ == "__main__":
    tests = [
        "Refactor this Python function for readability",
        "Summarize the importance of local AI governance",
        "Classify this feedback: 'The UI is slow and confusing'"
    ]
    for t in tests:
        r = run(t)
        print(f"Prompt: {t}\nModel: {r['model']} (intent={r['intent']})\nOutput: {r['output'][:160]}...\n")
```


### 3. Enchaînement des tâches en plusieurs étapes (7 min)

Créer `samples/06-tools/pipeline.py` :

```python
#!/usr/bin/env python3
"""Multi-step pipeline: plan -> solve -> refine using specialized models."""
from openai import OpenAI
from router import detect_intent, select_model

client = OpenAI(base_url="http://localhost:5273/v1", api_key="not-needed")

def chat(model, content, temp=0.4):
    r = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": content}],
        max_tokens=350,
        temperature=temp
    )
    return r.choices[0].message.content

def pipeline(task: str):
    plan_model = select_model("general")
    plan = chat(plan_model, f"Break the task into 3 ordered steps. Task: {task}")
    steps = [s for s in plan.split('\n') if s.strip()][:3]
    outputs = []
    for step in steps:
        intent = detect_intent(step)
        model = select_model(intent)
        out = chat(model, step)
        outputs.append((step, model, out))
    refine_model = select_model("summarize")
    combined = '\n'.join(o[2] for o in outputs)
    refined = chat(refine_model, f"Condense results into a cohesive answer:\n{combined}")
    return {"plan": plan, "steps": outputs, "final": refined}

if __name__ == '__main__':
    result = pipeline("Generate a refactored version of a slow Python loop and summarize performance gains.")
    print("PLAN:\n", result['plan'])
    print("FINAL:\n", result['final'][:400])
```


### 4. Projet de démarrage : Adapter `06-models-as-tools` (5 min)

Améliorations :
- Ajouter la prise en charge des jetons en streaming (mise à jour progressive de l'interface utilisateur)
- Ajouter un score de confiance : chevauchement lexical ou grille d'évaluation des invites
- Exporter le JSON de traçabilité (intention → modèle → latence → utilisation des jetons)
- Implémenter la réutilisation du cache pour les sous-étapes répétées

### 5. Voie de mise à l'échelle vers Azure (5 min)

| Couche | Local (Foundry) | Cloud (Azure AI Foundry) | Stratégie de transition |
|--------|-----------------|--------------------------|--------------------------|
| Routage | Python heuristique | Microservice durable | Conteneuriser et déployer l'API |
| Modèles | SLMs mis en cache | Déploiements gérés | Mapper les noms locaux aux IDs de déploiement |
| Observabilité | Statistiques CLI/manuelles | Journalisation centrale et métriques | Ajouter des événements de traçabilité structurés |
| Sécurité | Hôte local uniquement | Authentification Azure / réseau | Introduire un coffre de clés pour les secrets |
| Coût | Ressources de l'appareil | Facturation à la consommation | Ajouter des garde-fous budgétaires |

## Liste de vérification de validation

```powershell
foundry model run phi-4-mini
foundry model run deepseek-coder-1.3b
python samples/06-tools/router.py
python samples/06-tools/pipeline.py
```

Attendez-vous à une sélection de modèle basée sur l'intention et à une sortie finale affinée.

## Dépannage

| Problème | Cause | Solution |
|----------|-------|----------|
| Toutes les tâches routées vers le même modèle | Règles faibles | Enrichir l'ensemble regex INTENT_RULES |
| Échec du pipeline en milieu d'étape | Modèle manquant chargé | Exécuter `foundry model run <model>` |
| Cohésion de sortie faible | Pas de phase d'affinement | Ajouter une étape de résumé/validation |

## Références

- SDK Foundry Local : https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- Documentation Azure AI Foundry : https://learn.microsoft.com/azure/ai-foundry
- Modèles de qualité des invites : Voir Session 2

---

**Durée de la session** : 30 min  
**Niveau de difficulté** : Expert

## Scénario d'exemple et cartographie de l'atelier

| Scripts / Notebooks de l'atelier | Scénario | Objectif | Source du catalogue / des données |
|----------------------------------|----------|----------|------------------------------------|
| `samples/session06/models_router.py` / `notebooks/session06_models_router.ipynb` | Assistant développeur gérant des invites d'intention mixte (refactorisation, résumé, classification) | Routage heuristique intention → alias de modèle avec utilisation des jetons | `CATALOG` intégré + regex `RULES` |
| `samples/session06/models_pipeline.py` / `notebooks/session06_models_pipeline.ipynb` | Planification et affinage en plusieurs étapes pour une tâche complexe d'assistance au codage | Décomposer → exécution spécialisée → étape d'affinement du résumé | Même `CATALOG`; étapes dérivées de la sortie du plan |

### Narratif du scénario
Un outil de productivité pour ingénieurs reçoit des tâches hétérogènes : refactoriser du code, résumer des notes architecturales, classifier des retours. Pour minimiser la latence et l'utilisation des ressources, un petit modèle général planifie et résume, un modèle spécialisé dans le code gère la refactorisation, et un modèle léger capable de classification étiquette les retours. Le script de pipeline démontre l'enchaînement + l'affinement ; le script de routeur isole le routage adaptatif à une seule invite.

### Instantané du catalogue
```python
CATALOG = {
    "phi-4-mini": {"capabilities": ["general", "summarize"], "priority": 2},
    "deepseek-coder-1.3b": {"capabilities": ["code", "refactor"], "priority": 1},
    "qwen2.5-0.5b": {"capabilities": ["classification", "fast"], "priority": 3}
}
```


### Exemples d'invites de test
```json
[
    "Refactor this Python function for readability",
    "Summarize the importance of small language models",
    "Classify this feedback: The UI is slow but pretty",
    "Generate a refactored version of a slow Python loop and summarize performance gains."
]
```


### Extension de traçabilité (optionnel)
Ajouter des lignes JSON de traçabilité par étape pour `models_pipeline.py` :
```python
trace.append({
    "step": step_idx,
    "intent": intent,
    "alias": alias,
    "latency_ms": round((end-start)*1000,2),
    "tokens": getattr(usage,'total_tokens',None)
})
```


### Heuristique d'escalade (idée)
Si le plan contient des mots-clés comme "optimiser", "sécurité", ou si la longueur de l'étape > 280 caractères → escalader vers un modèle plus grand (par exemple, `gpt-oss-20b`) uniquement pour cette étape.

### Améliorations optionnelles

| Domaine | Amélioration | Valeur | Indice |
|---------|--------------|--------|--------|
| Mise en cache | Réutiliser les objets manager + client | Latence réduite, moins de surcharge | Utiliser `workshop_utils.get_client` |
| Métriques d'utilisation | Capturer les jetons et la latence par étape | Profilage et optimisation | Chronométrer chaque appel routé ; stocker dans une liste de traçabilité |
| Routage adaptatif | Confiance / coût conscient | Meilleur compromis qualité-coût | Ajouter un score : si l'invite > N caractères ou si le regex correspond au domaine → escalader vers un modèle plus grand |
| Registre dynamique des capacités | Rechargement à chaud du catalogue | Pas de redéploiement au redémarrage | Charger `catalog.json` au moment de l'exécution ; surveiller l'horodatage du fichier |
| Stratégie de secours | Robustesse en cas de défaillances | Disponibilité accrue | Essayer le primaire → en cas d'exception, alias de secours |
| Pipeline en streaming | Retour anticipé | Amélioration de l'expérience utilisateur | Diffuser chaque étape et mettre en tampon l'entrée finale d'affinement |
| Embeddings vectoriels d'intention | Routage plus nuancé | Précision accrue de l'intention | Intégrer l'invite, regrouper et mapper le centroïde → capacité |
| Export de traçabilité | Chaîne auditable | Conformité / reporting | Émettre des lignes JSON : étape, intention, modèle, latence_ms, jetons |
| Simulation de coût | Estimation pré-cloud | Planification budgétaire | Attribuer un coût notionnel/jeton par modèle et agréger par tâche |
| Mode déterministe | Reproducibilité des tests | Benchmarking stable | Env : `temperature=0`, nombre d'étapes fixe |

#### Exemple de structure de traçabilité

```python
trace.append({
  "step": idx,
  "intent": intent,
  "alias": alias,
  "latency_ms": round((end-start)*1000,2),
  "tokens": getattr(usage,'total_tokens',None)
})
```


#### Esquisse d'escalade adaptative

```python
if len(prompt) > 280 or 'compliance' in prompt.lower():
    # escalate to larger reasoning model if available
    alias = 'gpt-oss-20b'
```


#### Rechargement à chaud du catalogue de modèles

```python
import json, time, os
CATALOG_PATH = 'catalog.json'
last_mtime = 0
def get_catalog():
    global last_mtime, CATALOG
    m = os.path.getmtime(CATALOG_PATH)
    if m != last_mtime:
        CATALOG = json.load(open(CATALOG_PATH))
        last_mtime = m
    return CATALOG
```

---

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction humaine professionnelle. Nous ne sommes pas responsables des malentendus ou des interprétations erronées résultant de l'utilisation de cette traduction.
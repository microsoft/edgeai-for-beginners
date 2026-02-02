# Session 5 : Construisez rapidement des agents alimentés par l'IA avec Foundry Local

## Résumé

Concevez et orchestrez des agents IA multi-rôles en utilisant le runtime à faible latence et respectueux de la vie privée de Foundry Local. Vous définirez les rôles des agents, les stratégies de mémoire, les modèles d'appel d'outils et les graphes d'exécution. La session introduit des modèles de structure que vous pouvez étendre avec Chainlit ou LangGraph. Le projet de départ étend l'exemple d'architecture d'agent existant pour ajouter une persistance de mémoire + des hooks d'évaluation.

## Objectifs d'apprentissage

- **Définir les rôles** : Invites système & limites des capacités
- **Implémenter la mémoire** : Court terme (conversation), long terme (vecteur / fichier), blocs-notes éphémères
- **Structurer les workflows** : Étapes séquentielles, ramifiées et parallèles des agents
- **Intégrer des outils** : Modèle léger d'appel de fonctions
- **Évaluer** : Traces de base + scoring des résultats basé sur des rubriques

## Prérequis

- Sessions 1 à 4 terminées
- Python avec `foundry-local-sdk`, `openai`, optionnel `chainlit`
- Modèles locaux en fonctionnement (au moins `phi-4-mini`)

### Extrait d'environnement multiplateforme

Windows :
```powershell
py -m venv .venv
 .\.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install foundry-local-sdk openai
```

macOS :
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install foundry-local-sdk openai
```

Si vous exécutez des agents depuis macOS contre un service hôte Windows distant :
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```


## Déroulement de la démo (30 min)

### 1. Définir les rôles des agents et la mémoire (7 min)

Créer `samples/05-agents/agents_core.py` :

```python
#!/usr/bin/env python3
"""Minimal multi-agent scaffolding using Foundry Local (OpenAI-compatible)."""
from openai import OpenAI
from dataclasses import dataclass, field
from typing import List, Dict, Any, Callable
import time, json

client = OpenAI(base_url="http://localhost:5273/v1", api_key="not-needed")

@dataclass
class AgentMessage:
    role: str
    content: str
    meta: Dict[str, Any] = field(default_factory=dict)

@dataclass
class Agent:
    name: str
    system_prompt: str
    tools: Dict[str, Callable] = field(default_factory=dict)
    memory: List[AgentMessage] = field(default_factory=list)

    def remember(self, role: str, content: str, **meta):
        self.memory.append(AgentMessage(role=role, content=content, meta=meta))

    def context(self, window:int=8):
        recent = self.memory[-window:]
        msgs = [ {"role": "system", "content": self.system_prompt}]
        msgs += [ {"role": m.role, "content": m.content} for m in recent ]
        return msgs

    def act(self, user_input: str, model: str = "phi-4-mini", temperature: float=0.4):
        self.remember("user", user_input)
        resp = client.chat.completions.create(
            model=model,
            messages=self.context() + [{"role": "user", "content": user_input}],
            temperature=temperature,
            max_tokens=400
        )
        answer = resp.choices[0].message.content
        self.remember("assistant", answer, model=model)
        return answer

researcher = Agent(
    name="Researcher",
    system_prompt="You gather factual, structured insights concisely."
)
writer = Agent(
    name="Writer",
    system_prompt="You rewrite content for clarity and engagement while preserving facts."
)

def demo():
    q = "Explain why edge inference matters for privacy and latency."
    r = researcher.act(q)
    print("Researcher ->", r[:200], "...\n")
    w = writer.act(f"Rewrite more user-friendly: {r}")
    print("Writer ->", w[:200], "...")

if __name__ == "__main__":
    demo()
```


### 2. Modèle de structure CLI (3 min)

```powershell
python samples/05-agents/agents_core.py
```


### 3. Ajouter l'appel d'outils (7 min)

Étendre avec `samples/05-agents/tools.py` :

```python
from datetime import datetime
import math, json

def tool_time(_:str)->str:
    return f"Current UTC time: {datetime.utcnow().isoformat()}"

def tool_estimate_tokens(text:str)->str:
    approx = len(text.split()) * 1.35
    return f"Estimated tokens ~ {int(approx)}"

TOOLS = {
    "get_time": tool_time,
    "estimate_tokens": tool_estimate_tokens
}
```


Modifier `agents_core.py` pour permettre une syntaxe simple d'outil : l'utilisateur écrit `#tool:get_time` et l'agent intègre la sortie de l'outil dans le contexte avant la génération.

### 4. Workflow orchestré (6 min)

Créer `samples/05-agents/orchestrator.py` :

```python
from agents_core import researcher, writer, Agent
from tools import TOOLS
from openai import OpenAI

client = OpenAI(base_url="http://localhost:5273/v1", api_key="not-needed")

def inject_tools(agent: Agent, user_input: str) -> str:
    if user_input.startswith('#tool:'):
        name = user_input.split(':',1)[1].strip()
        if name in TOOLS:
            out = TOOLS[name](../../../Workshop/"")
            agent.remember("tool", out, tool=name)
            return f"Tool[{name}] => {out}"
    return None

def pipeline(question: str):
    tool_note = inject_tools(researcher, '#tool:get_time')
    r = researcher.act(question)
    w = writer.act(f"Improve readability:\n{r}\nAdd a friendly summary line.")
    return {"raw": r, "refined": w, "tool": tool_note}

if __name__ == '__main__':
    result = pipeline("List three concrete benefits of local SLM inference for regulated industries.")
    for k,v in result.items():
        print(f"== {k.upper()} ==\n{v}\n")
```


### 5. Projet de départ : Étendre `05-agent-architecture` (7 min)

Ajouter :
1. Une couche de mémoire persistante (par exemple, ajout de lignes JSON des conversations)
2. Une rubrique d'évaluation simple : placeholders pour factualité / clarté / style
3. Une interface frontale Chainlit optionnelle (deux onglets : conversation & traces)
4. Une machine d'état de style LangGraph optionnelle (si dépendance ajoutée) pour les décisions ramifiées

## Liste de vérification de validation

```powershell
foundry model run phi-4-mini
python samples/05-agents/orchestrator.py
```

Attendez-vous à une sortie de pipeline structurée avec une note d'injection d'outil.

## Aperçu des stratégies de mémoire

| Couche       | Objectif              | Exemple                |
|--------------|-----------------------|------------------------|
| Court terme  | Continuité du dialogue | Derniers N messages    |
| Épisodique   | Rappel de session     | JSON par session       |
| Sémantique   | Récupération à long terme | Stockage vectoriel des résumés |
| Bloc-notes   | Étapes de raisonnement | Chaîne de pensée en ligne (privée) |

## Hooks d'évaluation (conceptuel)

```python
evaluation = {
  "factuality": None,  # manual or heuristic
  "clarity": None,
  "style": None,
  "latency_sec": generation_time,
  "model": model_used
}
```


## Résolution des problèmes

| Problème            | Cause                     | Solution                     |
|---------------------|---------------------------|------------------------------|
| Réponses répétitives | Fenêtre de contexte trop grande/petite | Ajuster le paramètre de fenêtre de mémoire |
| Outil non invoqué   | Syntaxe incorrecte        | Utiliser le format `#tool:tool_name` |
| Orchestration lente | Modèles multiples à froid | Pré-exécuter des invites de préchauffage |

## Références

- Foundry Local SDK : https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- LangGraph (concept optionnel) : https://github.com/langchain-ai/langgraph
- Chainlit : https://docs.chainlit.io

---

**Durée de la session** : 30 min  
**Niveau de difficulté** : Avancé

## Scénario d'exemple & cartographie de l'atelier

| Script d'atelier                                   | Scénario                                      | Objectif                                      | Exemple d'invite                          |
|---------------------------------------------------|----------------------------------------------|----------------------------------------------|-------------------------------------------|
| `samples/session05/agents_orchestrator.py` / `notebooks/session05_agents_orchestrator.ipynb` | Bot de recherche de connaissances produisant des résumés adaptés aux cadres | Pipeline à deux agents (recherche → polissage éditorial) avec modèles distincts optionnels | Expliquez pourquoi l'inférence locale est importante pour la conformité. |
| Concept (étendu) `tools.py`                       | Ajouter des outils d'estimation de temps & de tokens | Démontrer un modèle léger d'appel d'outils   | #tool:get_time                            |

### Narration du scénario

L'équipe de documentation de conformité a besoin de résumés internes rapides provenant de connaissances locales sans envoyer de brouillons aux services cloud. Un agent chercheur rassemble des points factuels concis ; un agent éditeur réécrit pour une clarté adaptée aux cadres. Des alias de modèles distincts peuvent être assignés pour optimiser la latence (SLM rapide) contre le raffinement stylistique (modèle plus grand uniquement si nécessaire).

### Exemple d'environnement multi-modèles

```powershell
cd Workshop/samples
set AGENT_MODEL_PRIMARY=phi-4-mini
set AGENT_MODEL_EDITOR=gpt-oss-20b
python -m session05.agents_orchestrator
```


### Structure des traces (optionnel)

```json
{
    "step": 1,
    "agent": "Researcher",
    "latency_ms": 412.3,
    "tokens_in": 22,
    "tokens_out": 168,
    "model": "phi-4-mini"
}
```

Persistez chaque étape dans un fichier JSONL pour un scoring de rubrique ultérieur.

### Améliorations optionnelles

| Thème              | Amélioration              | Avantage                     | Esquisse de mise en œuvre                     |
|--------------------|---------------------------|------------------------------|-----------------------------------------------|
| Rôles multi-modèles | Modèles distincts par agent (`AGENT_MODEL_PRIMARY`, `AGENT_MODEL_EDITOR`) | Spécialisation & rapidité    | Sélectionner des alias dans les variables d'environnement, appeler `chat_once` avec alias par rôle |
| Traces structurées | Trace JSON de chaque acte(outil, entrée, latence, tokens) | Débogage & évaluation        | Ajouter un dictionnaire à une liste ; écrire `.jsonl` à la fin |
| Persistance de mémoire | Contexte de dialogue rechargé | Continuité de session        | Exporter `Agent.memory` vers `sessions/<ts>.json` |
| Registre d'outils  | Découverte dynamique d'outils | Extensibilité                | Maintenir un dictionnaire `TOOLS` & introspecter noms/descriptions |
| Réessai & temporisation | Chaînes longues robustes | Réduire les échecs transitoires | Envelopper `act` avec try/except + temporisation exponentielle |
| Scoring de rubrique | Étiquettes qualitatives automatisées | Suivre les améliorations     | Passer secondairement au modèle : "Notez la clarté de 1 à 5" |
| Mémoire vectorielle | Rappel sémantique         | Contexte riche à long terme  | Intégrer des résumés, récupérer les top-k dans le message système |
| Réponses en streaming | Réponse perçue plus rapide | Amélioration UX              | Utiliser le streaming une fois disponible et vider les tokens partiels |
| Tests déterministes | Contrôle de régression    | CI stable                    | Exécuter avec `temperature=0`, graines d'invite fixes |
| Ramification parallèle | Exploration plus rapide  | Débit                        | Utiliser `concurrent.futures` pour les étapes indépendantes des agents |

#### Exemple d'enregistrement de trace

```python
trace.append({
    "agent": agent.name,
    "input": prompt,
    "output_tokens": getattr(usage,'completion_tokens',None),
    "latency_ms": round((end-start)*1000,2),
    "tools_used": list(tool_calls)
})
```


#### Invite d'évaluation simple

```python
score_prompt = f"Rate clarity (1-5) ONLY as a number for this answer:\n{answer}"
rating, _ = chat_once(PRIMARY_ALIAS, messages=[{"role":"user","content":score_prompt}], max_tokens=4, temperature=0)
```

Persistez les paires (`answer`, `rating`) pour construire un graphique historique de qualité.

---

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction humaine professionnelle. Nous ne sommes pas responsables des malentendus ou des interprétations erronées résultant de l'utilisation de cette traduction.
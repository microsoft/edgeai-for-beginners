<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d9e354c0182311726dc037a8809524e2",
  "translation_date": "2025-10-28T20:00:14+00:00",
  "source_file": "Workshop/Session04-CuttingEdgeModels.md",
  "language_code": "fr"
}
-->
# Session 4 : Explorer des modèles de pointe – LLMs, SLMs et inférence sur appareil

## Résumé

Comparez les grands modèles de langage (LLMs) et les petits modèles de langage (SLMs) pour des scénarios d'inférence locale ou dans le cloud. Apprenez les modèles de déploiement en utilisant l'accélération ONNX Runtime, l'exécution WebGPU et des expériences hybrides RAG. Inclut une démonstration Chainlit RAG avec un modèle local et une exploration optionnelle d'OpenWebUI. Vous adapterez un starter d'inférence WebGPU et évaluerez les compromis entre capacité et coût/performance de Phi et GPT-OSS-20B.

## Objectifs d'apprentissage

- **Comparer** SLM et LLM sur les axes de latence, mémoire et qualité
- **Déployer** des modèles avec ONNXRuntime et (là où c'est pris en charge) WebGPU
- **Exécuter** une inférence basée sur navigateur (démonstration interactive respectueuse de la vie privée)
- **Intégrer** un pipeline Chainlit RAG avec un backend SLM local
- **Évaluer** en utilisant des heuristiques légères de qualité et de coût

## Prérequis

- Sessions 1 à 3 terminées
- `chainlit` installé (déjà dans `requirements.txt` pour Module08)
- Navigateur compatible WebGPU (Edge / Chrome dernière version sur Windows 11)
- Foundry Local en cours d'exécution (`foundry status`)

### Notes multiplateformes

Windows reste l'environnement cible principal. Pour les développeurs macOS en attente de binaires natifs :
1. Exécutez Foundry Local dans une VM Windows 11 (Parallels / UTM) OU une station de travail Windows distante.
2. Exposez le service (port par défaut 5273) et configurez sur macOS :
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```
3. Utilisez les mêmes étapes d'environnement virtuel Python que dans les sessions précédentes.

Installation de Chainlit (les deux plateformes) :
```bash
pip install chainlit
```

## Déroulement de la démonstration (30 min)

### 1. Comparer Phi (SLM) et GPT-OSS-20B (LLM) (6 min)

```powershell
foundry model run phi-4-mini
foundry model run gpt-oss-20b

# Quick capability probes (one-shot non-interactive)
foundry model run phi-4-mini   --prompt "Summarize retrieval augmented generation in 2 sentences."
foundry model run gpt-oss-20b --prompt "Summarize retrieval augmented generation in 2 sentences."

# Basic token / latency test (repeat a few times for intuition)
foundry model run phi-4-mini   --prompt "List 5 creative IoT edge AI ideas."
foundry model run gpt-oss-20b --prompt "List 5 creative IoT edge AI ideas."
```

Suivez : profondeur des réponses, précision factuelle, richesse stylistique, latence.

### 2. Accélération ONNX Runtime (5 min)

```powershell
foundry config set compute.onnx.enable_gpu true
# Re-run Python benchmark script for quantitative latency / throughput after enabling GPU
#   cd Workshop/samples
#   set BENCH_MODELS=phi-4-mini
#   python -m session03.benchmark_oss_models
```

Observez les changements de débit après activation du GPU par rapport au mode CPU uniquement.

### 3. Inférence WebGPU dans le navigateur (6 min)

Adaptez le starter `04-webgpu-inference` (créez `samples/04-cutting-edge/webgpu_demo.html`) :

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>Foundry Local WebGPU Demo</title>
  <style>body{font-family:system-ui;margin:2rem;max-width:820px;} textarea{width:100%;height:120px;} pre{background:#111;color:#eee;padding:1rem;} .resp{white-space:pre-wrap;margin-top:1rem;border:1px solid #444;padding:1rem;border-radius:6px;}</style>
</head>
<body>
  <h1>WebGPU Inference (Experimental)</h1>
  <p>Demonstration placeholder for a WebGPU-backed transformer (concept). Replace with actual JS runtime once exposed by Foundry Local or associated runtime libs.</p>
  <textarea id="prompt" placeholder="Enter your prompt..."></textarea>
  <button id="run">Generate</button>
  <div id="out" class="resp"></div>
  <script>
    document.getElementById('run').onclick = async () => {
      const p = document.getElementById('prompt').value.trim();
      if(!p) return;
      document.getElementById('out').textContent = 'Running (simulated)...';
      // Placeholder: in a real implementation you'd call into a WASM/WebGPU pipeline or local gateway endpoint.
      const resp = await fetch('http://localhost:5273/v1/chat/completions', {
        method: 'POST', headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          model: 'phi-4-mini',
          messages: [ { role: 'user', content: p } ],
          max_tokens: 200, temperature: 0.5
        })
      }).then(r=>r.json()).catch(e=>({error:e.toString()}));
      if(resp.error){
        document.getElementById('out').textContent = 'Error: '+resp.error;
      } else {
        document.getElementById('out').textContent = resp.choices?.[0]?.message?.content || JSON.stringify(resp,null,2);
      }
    };
  </script>
</body>
</html>
```

Ouvrez le fichier dans un navigateur ; observez le faible temps de latence pour un aller-retour local.

### 4. Application de chat Chainlit RAG (7 min)

Minimal `samples/04-cutting-edge/chainlit_app.py` :

```python
#!/usr/bin/env python3
"""Chainlit RAG demo using Foundry Local SLM as backend."""
import chainlit as cl
from openai import OpenAI

DOCS = [
  "Foundry Local enables local model execution with OpenAI-compatible APIs.",
  "RAG combines retrieval and generation for grounded answers.",
  "SLMs provide efficiency advantages on constrained hardware."  
]

client = OpenAI(base_url="http://localhost:5273/v1", api_key="not-needed")

def build_context(query: str):
    # Naive lexical scoring
    scored = sorted(DOCS, key=lambda d: sum(w in d.lower() for w in query.lower().split()), reverse=True)
    return "\n".join(scored[:2])

@cl.on_message
async def main(message: cl.Message):
    ctx = build_context(message.content)
    resp = client.chat.completions.create(
        model="phi-4-mini",
        messages=[
            {"role": "system", "content": "Answer using ONLY the provided context. If insufficient, say so."},
            {"role": "user", "content": f"Context:\n{ctx}\n\nQuestion: {message.content}"}
        ],
        max_tokens=300,
        temperature=0.3
    )
    await cl.Message(content=resp.choices[0].message.content).send()
```

Exécutez :

```powershell
chainlit run samples/04-cutting-edge/chainlit_app.py -w
```

### 5. Projet de démarrage : Adapter `04-webgpu-inference` (6 min)

Livrables :
- Remplacez la logique de récupération par défaut par des jetons en streaming (utilisez la variante de point de terminaison `stream=True` une fois activée)
- Ajoutez un graphique de latence (côté client) pour les bascules entre phi et gpt-oss-20b
- Intégrez le contexte RAG en ligne (zone de texte pour les documents de référence)

## Heuristiques d'évaluation

| Catégorie | Phi-4-mini | GPT-OSS-20B | Observation |
|-----------|------------|-------------|-------------|
| Latence (à froid) | Rapide | Plus lent | SLM se réchauffe rapidement |
| Mémoire | Faible | Élevée | Faisabilité sur appareil |
| Adhérence au contexte | Bonne | Forte | Modèle plus grand peut être plus verbeux |
| Coût (local) | Minimal | Plus élevé (ressources) | Compromis énergie/temps |
| Meilleur cas d'utilisation | Applications Edge | Raisonnement approfondi | Pipeline hybride possible |

## Validation de l'environnement

```powershell
# List catalog (no --running flag; loaded models are those you have previously run)
foundry model list

# For runtime metrics use the Python benchmark script (Session 3) and OS tools (Task Manager / nvidia-smi) instead of 'model stats'
# Example:
#   cd Workshop/samples
#   set BENCH_MODELS=phi-4-mini,gpt-oss-20b
#   python -m session03.benchmark_oss_models
```

## Dépannage

| Symptôme | Cause | Action |
|----------|-------|--------|
| Échec de récupération de la page web | CORS ou service hors ligne | Utilisez `curl` pour vérifier le point de terminaison ; activez un proxy CORS si nécessaire |
| Page blanche Chainlit | Env non actif | Activez venv et réinstallez les dépendances |
| Latence élevée | Modèle juste chargé | Réchauffez avec une petite séquence de prompt |

## Références

- SDK Foundry Local : https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- Documentation Chainlit : https://docs.chainlit.io
- Évaluation RAG (Ragas) : https://docs.ragas.io

---

**Durée de la session** : 30 min  
**Difficulté** : Avancé

## Scénario d'exemple et cartographie de l'atelier

| Artefacts de l'atelier | Scénario | Objectif | Source de données / prompt |
|-------------------------|----------|----------|----------------------------|
| `samples/session04/model_compare.py` / `notebooks/session04_model_compare.ipynb` | Équipe d'architecture évaluant SLM vs LLM pour un générateur de résumé exécutif | Quantifier la latence + delta d'utilisation des jetons | Variable d'environnement unique `COMPARE_PROMPT` |
| `chainlit_app.py` (démonstration RAG) | Prototype d'assistant de connaissances interne | Réponses courtes basées sur une récupération lexicale minimale | Liste `DOCS` en ligne dans le fichier |
| `webgpu_demo.html` | Aperçu futuriste de l'inférence sur navigateur | Montrer un aller-retour local à faible latence + narration UX | Prompt utilisateur en direct uniquement |

### Narration du scénario
L'organisation produit souhaite un générateur de briefing exécutif. Un SLM léger (phi‑4‑mini) rédige des résumés ; un LLM plus grand (gpt‑oss‑20b) peut affiner uniquement les rapports prioritaires. Les scripts de session capturent des métriques empiriques de latence et de jetons pour justifier un design hybride, tandis que la démonstration Chainlit illustre comment une récupération ancrée maintient les réponses du petit modèle factuelles. La page concept WebGPU fournit une voie de vision pour un traitement entièrement côté client lorsque l'accélération du navigateur mûrit.

### Contexte RAG minimal (Chainlit)
```python
DOCS = [
  "Foundry Local enables local model execution with OpenAI-compatible APIs.",
  "RAG combines retrieval and generation for grounded answers.",
  "SLMs provide efficiency advantages on constrained hardware."
]
```

### Flux hybride Brouillon→Affinage (Pseudo)
```python
draft, _ = chat_once('phi-4-mini', messages=[{"role":"user","content":prompt}], max_tokens=280)
if len(draft) < 600:  # heuristic: escalate only for longer briefs or flagged topics
    final = draft
else:
    final, _ = chat_once('gpt-oss-20b', messages=[{"role":"user","content":f"Refine and polish:\n{draft}"}], max_tokens=220)
```

Suivez les deux composants de latence pour rapporter le coût moyen combiné.

### Améliorations optionnelles

| Focus | Amélioration | Pourquoi | Indice d'implémentation |
|-------|-------------|----------|-------------------------|
| Métriques comparatives | Suivre l'utilisation des jetons + latence du premier jeton | Vue globale des performances | Utilisez un script de benchmark amélioré (Session 3) avec `BENCH_STREAM=1` |
| Pipeline hybride | Brouillon SLM → Affinage LLM | Réduire la latence et le coût | Générer avec phi-4-mini, affiner le résumé avec gpt-oss-20b |
| Interface utilisateur en streaming | Meilleure UX dans Chainlit | Feedback incrémental | Utilisez `stream=True` une fois le streaming local exposé ; accumulez les morceaux |
| Mise en cache WebGPU | Initialisation JS plus rapide | Réduire les frais de recompilation | Cachez les artefacts de shader compilés (capacité future du runtime) |
| Ensemble de QA déterministe | Comparaison équitable des modèles | Éliminer la variance | Liste de prompts fixe + `temperature=0` pour les exécutions d'évaluation |
| Évaluation des sorties | Lentille de qualité structurée | Aller au-delà des anecdotes | Rubrique simple : cohérence / factualité / concision (1–5) |
| Notes sur énergie / ressources | Discussion en classe | Montrer les compromis | Utilisez les moniteurs OS (`foundry system info`, Gestionnaire de tâches, `nvidia-smi`) + sorties de script de benchmark |
| Émulation de coût | Justification pré-cloud | Planifier l'échelle | Mappez les jetons à une tarification cloud hypothétique pour une narration TCO |
| Décomposition de latence | Identifier les goulots d'étranglement | Cibler les optimisations | Mesurez la préparation du prompt, l'envoi de la requête, le premier jeton, la complétion totale |
| RAG + LLM en secours | Filet de sécurité qualité | Améliorer les requêtes difficiles | Si la longueur de réponse SLM < seuil ou faible confiance → escalade |

#### Exemple de modèle hybride Brouillon/Affinage

```python
draft, _ = chat_once('phi-4-mini', messages=[{"role":"user","content":task}], max_tokens=300, temperature=0.4)
refine, _ = chat_once('gpt-oss-20b', messages=[{"role":"user","content":f"Improve clarity but keep facts:\n{draft}"}], max_tokens=220, temperature=0.3)
```

#### Croquis de décomposition de latence

```python
import time
t0 = time.time(); # build messages
prep_ms = (time.time()-t0)*1000
t1 = time.time(); text,_ = chat_once(alias, messages=msgs, max_tokens=180)
full_ms = (time.time()-t1)*1000
print({"prep_ms": prep_ms, "full_gen_ms": full_ms})
```

Utilisez une structure de mesure cohérente entre les modèles pour des comparaisons équitables.

---

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction humaine professionnelle. Nous ne sommes pas responsables des malentendus ou des interprétations erronées résultant de l'utilisation de cette traduction.
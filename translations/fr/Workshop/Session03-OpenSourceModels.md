# Session 3 : Modèles Open Source dans Foundry Local

## Résumé

Découvrez comment intégrer des modèles open source, tels que ceux de Hugging Face, dans Foundry Local. Apprenez les stratégies de sélection, les workflows de contribution communautaire, la méthodologie de comparaison des performances, et comment étendre Foundry avec des enregistrements de modèles personnalisés. Cette session s'inscrit dans les thèmes hebdomadaires "Model Mondays" et vous prépare à évaluer et opérationnaliser des modèles open source localement avant de passer à Azure.

## Objectifs d'apprentissage

À la fin de cette session, vous serez capable de :

- **Découvrir et Évaluer** : Identifier des modèles candidats (mistral, gemma, qwen, deepseek) en fonction des compromis entre qualité et ressources.
- **Charger et Exécuter** : Utiliser la CLI de Foundry Local pour télécharger, mettre en cache et lancer des modèles communautaires.
- **Évaluer les performances** : Appliquer des heuristiques cohérentes sur la latence, le débit de tokens et la qualité.
- **Étendre** : Enregistrer ou adapter un wrapper de modèle personnalisé en suivant des modèles compatibles avec le SDK.
- **Comparer** : Produire des comparaisons structurées pour les décisions de sélection entre SLM et LLM de taille moyenne.

## Prérequis

- Sessions 1 et 2 complétées
- Environnement Python avec `foundry-local-sdk` installé
- Au moins 15 Go d'espace disque libre pour les caches de modèles multiples

### Démarrage rapide pour environnement multiplateforme

Windows PowerShell :
```powershell
py -m venv .venv
 .\.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install foundry-local-sdk openai numpy
```
  
macOS / Linux :  
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install foundry-local-sdk openai numpy
```
  
Lors de l'évaluation depuis macOS contre un service hôte Windows, configurez :  
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```
  

## Déroulement de la démo (30 min)

### 1. Charger des modèles Hugging Face via CLI (8 min)

```powershell
# List catalog entries (filter manually if needed)
foundry model list

# Download a set of comparison targets
foundry model download mistral-7b
foundry model download gemma-2-2b
foundry model download qwen2.5-0.5b

# Verify cache
foundry cache list
```
  

### 2. Exécuter et tester rapidement (5 min)

```powershell
foundry model run qwen2.5-0.5b
foundry model run qwen2.5-0.5b --prompt "List three benefits of local inference."

foundry model run mistral-7b
foundry model run mistral-7b --prompt "Explain retrieval augmented generation in one paragraph."
```
  

### 3. Script d'évaluation des performances (8 min)

Créez `samples/03-oss-models/benchmark_models.py` :

```python
#!/usr/bin/env python3
"""Lightweight benchmarking for open-source models in Foundry Local.
Metrics: first token latency, total latency, tokens/sec (approx via usage), model size indicator.
Reference SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
"""

import time, statistics, json
from openai import OpenAI

MODELS = [
    "qwen2.5-0.5b",
    "gemma-2-2b",
    "mistral-7b",
]

PROMPT = "Explain the principle of retrieval augmented generation in 2 sentences."
ROUNDS = 3

client = OpenAI(base_url="http://localhost:5273/v1", api_key="not-needed")

def run_round(model: str):
    start = time.time()
    resp = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": PROMPT}],
        max_tokens=150,
        temperature=0.2,
        stream=False
    )
    end = time.time()
    usage = getattr(resp, "usage", None)
    total_tokens = usage.total_tokens if usage else None
    return {
        "latency_sec": end - start,
        "total_tokens": total_tokens,
        "tokens_per_sec": (total_tokens / (end - start)) if (total_tokens and (end-start) > 0) else None,
        "sample_response": resp.choices[0].message.content[:160].replace("\n", " ")
    }

def benchmark_model(model: str):
    results = [run_round(model) for _ in range(ROUNDS)]
    latencies = [r["latency_sec"] for r in results]
    tps = [r["tokens_per_sec"] for r in results if r["tokens_per_sec"]]
    return {
        "model": model,
        "rounds": ROUNDS,
        "latency_avg": statistics.mean(latencies),
        "latency_p95": statistics.quantiles(latencies, n=20)[-1] if len(latencies) > 1 else latencies[0],
        "tokens_per_sec_avg": statistics.mean(tps) if tps else None,
        "sample": results[-1]["sample_response"]
    }

def main():
    summary = [benchmark_model(m) for m in MODELS]
    print(json.dumps(summary, indent=2))
    print("\nInterpretation Tips:\n- latency_avg: lower better\n- tokens_per_sec_avg: higher better\n- Compare quality manually on sample outputs.")

if __name__ == "__main__":
    main()
```
  
Exécutez :

```powershell
python samples/03-oss-models/benchmark_models.py
```
  

### 4. Comparer les performances (5 min)

Discutez des compromis : temps de chargement, empreinte mémoire (observez le Gestionnaire des tâches / `nvidia-smi` / moniteur de ressources OS), qualité de sortie vs vitesse. Utilisez le script d'évaluation Python (Session 3) pour la latence et le débit ; répétez après avoir activé l'accélération GPU.

### 5. Projet de démarrage (4 min)

Créez un générateur de rapport de comparaison de modèles (étendez le script d'évaluation avec export Markdown).

## Projet de démarrage : Étendre `03-huggingface-models`

Améliorez l'exemple existant en :

1. Ajoutant une agrégation des évaluations + sortie CSV/Markdown.
2. Implémentant un scoring qualitatif simple (ensemble de paires de prompts + fichier d'annotation manuel).
3. Introduisant une configuration JSON (`models.json`) pour une liste de modèles et un ensemble de prompts modulables.

## Liste de validation

```powershell
foundry cache list
foundry model run qwen2.5-0.5b
curl http://localhost:5273/v1/models
```
  
Tous les modèles cibles doivent apparaître et répondre à une requête de chat de test.

## Scénario d'exemple et correspondance avec l'atelier

| Script de l'atelier | Scénario | Objectif | Source de prompt / dataset |
|----------------------|----------|----------|-----------------------------|
| `samples/session03/benchmark_oss_models.py` / `notebooks/session03_benchmark_oss_models.ipynb` | Équipe plateforme Edge sélectionnant un SLM par défaut pour un résumé intégré | Produire une comparaison de latence + p95 + tokens/sec entre les modèles candidats | Variable `PROMPT` inline + liste `BENCH_MODELS` dans l'environnement |

### Narratif du scénario
L'équipe d'ingénierie produit doit choisir un modèle de résumé léger par défaut pour une fonctionnalité de prise de notes hors ligne. Ils exécutent des évaluations déterministes contrôlées (temperature=0) sur un ensemble de prompts fixe (voir exemple ci-dessous) et collectent des métriques de latence + débit avec et sans accélération GPU.

### Exemple d'ensemble de prompts JSON (extensible)
```json
[
    "Explain the principle of retrieval augmented generation in 2 sentences.",
    "List 3 privacy benefits of local inference.",
    "Summarize why model size impacts latency on consumer hardware.",
    "Provide two scenarios where an SLM is preferable to an LLM."
]
```
  
Bouclez chaque prompt par modèle, capturez la latence par prompt pour dériver des métriques de distribution et détecter les valeurs aberrantes.

## Cadre de sélection des modèles

| Dimension | Métrique | Pourquoi c'est important |
|-----------|----------|--------------------------|
| Latence | moyenne / p95 | Cohérence de l'expérience utilisateur |
| Débit | tokens/sec | Évolutivité par lots et en streaming |
| Mémoire | taille résidente | Adaptation aux appareils & concurrence |
| Qualité | prompts de référence | Pertinence pour la tâche |
| Empreinte | cache disque | Distribution & mises à jour |
| Licence | autorisation d'utilisation | Conformité commerciale |

## Extension avec un modèle personnalisé

Modèle général (pseudo-code) :

```python
# pseudo_adapter.py (conceptual)
class CustomModelAdapter:
    def load(self, weights_path: str): ...
    def generate(self, prompt: str, **params) -> str: ...

# Register with local routing (future extensibility point)
```
  
Consultez le dépôt officiel pour les interfaces d'adaptateurs en évolution :  
https://github.com/microsoft/Foundry-Local/tree/main/sdk/python  

## Dépannage

| Problème | Cause | Solution |
|----------|-------|----------|
| OOM sur mistral-7b | RAM/GPU insuffisante | Arrêtez d'autres modèles ; essayez une variante plus petite |
| Réponse lente au premier essai | Chargement à froid | Maintenez actif avec un prompt léger périodique |
| Téléchargement bloqué | Instabilité réseau | Réessayez ; préchargez pendant les heures creuses |

## Références

- SDK Foundry Local : https://github.com/microsoft/Foundry-Local/tree/main/sdk/python  
- Model Mondays : https://aka.ms/model-mondays  
- Découverte de modèles Hugging Face : https://huggingface.co/models  

---

**Durée de la session** : 30 min (+ approfondissement optionnel)  
**Niveau de difficulté** : Intermédiaire  

### Améliorations optionnelles

| Amélioration | Avantage | Comment |
|--------------|----------|---------|
| Latence du premier token en streaming | Mesure la réactivité perçue | Exécutez l'évaluation avec `BENCH_STREAM=1` (script amélioré dans `Workshop/samples/session03`) |
| Mode déterministe | Comparaisons de régression stables | `temperature=0`, ensemble de prompts fixe, capturez les sorties JSON sous contrôle de version |
| Scoring qualitatif avec grille d'évaluation | Ajoute une dimension qualitative | Maintenez `prompts.json` avec des facettes attendues ; annotez les scores (1–5) manuellement ou via un modèle secondaire |
| Export CSV / Markdown | Rapport partageable | Étendez le script pour écrire `benchmark_report.md` avec tableau et points forts |
| Tags de capacités des modèles | Aide au routage automatisé ultérieur | Maintenez `models.json` avec `{alias: {capabilities:[], size_mb:..}}` |
| Phase de préchauffage du cache | Réduit le biais de démarrage à froid | Exécutez une ronde légère avant la boucle de chronométrage (déjà implémenté) |
| Précision des percentiles | Latence robuste en queue | Utilisez le percentile numpy (déjà dans le script refactorisé) |
| Approximation du coût des tokens | Comparaison économique | Coût approx = (tokens/sec * tokens moyens par requête) * heuristique énergétique |
| Saut automatique des modèles échoués | Résilience dans les exécutions par lots | Enveloppez chaque évaluation dans try/except et marquez le champ de statut |

#### Extrait minimal d'export Markdown

```python
with open("benchmark_report.md", "w") as f:
        f.write("|Model|Avg Latency|p95|TPS|\n|---|---|---|---|\n")
        for row in summary:
                f.write(f"|{row['alias']}|{row['latency_avg']:.2f}|{row['latency_p95']:.2f}|{(row.get('tokens_per_sec_avg') or 0):.1f}|\n")
```
  
#### Exemple d'ensemble de prompts déterministe

```json
[
    "Summarize retrieval augmented generation.",
    "List 3 privacy benefits of local inference.",
    "Explain when to choose an SLM over an LLM."
]
```
  
Bouclez la liste statique au lieu de prompts aléatoires pour des métriques comparables entre les commits.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction humaine professionnelle. Nous ne sommes pas responsables des malentendus ou des interprétations erronées résultant de l'utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
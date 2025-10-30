<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4ace56b24e2799407b9972a7da6a7517",
  "translation_date": "2025-10-28T20:04:18+00:00",
  "source_file": "Workshop/scripts/README.md",
  "language_code": "fr"
}
-->
# Scripts de l'atelier

Ce répertoire contient des scripts d'automatisation et de support utilisés pour maintenir la qualité et la cohérence des matériaux de l'atelier.

## Contenu

| Fichier | Objectif |
|---------|----------|
| `lint_markdown_cli.py` | Analyse les blocs de code Markdown pour bloquer les modèles de commandes obsolètes de Foundry Local CLI. |
| `export_benchmark_markdown.py` | Exécute un benchmark de latence multi-modèles et génère des rapports en Markdown + JSON. |

## 1. Analyseur de modèles CLI Markdown

`lint_markdown_cli.py` analyse tous les fichiers `.md` non traduits pour détecter les modèles Foundry Local CLI interdits **dans les blocs de code délimités** (``` ... ```). Le texte informatif peut toujours mentionner les commandes obsolètes à des fins historiques.

### Modèles obsolètes (bloqués dans les blocs de code)

L'analyseur bloque les modèles CLI obsolètes. Utilisez des alternatives modernes à la place.

### Remplacements requis
| Obsolète | Utiliser à la place |
|----------|----------------------|
| `foundry model chat <a> "..."` | `foundry model run <a> --prompt "..."` |
| `foundry model list --running` | `foundry model list` |
| `foundry model list --cached` | `foundry cache list` |
| `foundry model stats` | Script de benchmark + outils système (`Gestionnaire de tâches`, `nvidia-smi`) |
| `foundry model benchmark` | `samples/session03/benchmark_oss_models.py` |
| `foundry model list --available` | `foundry model list` |

### Codes de sortie
| Code | Signification |
|------|---------------|
| 0 | Aucune violation détectée |
| 1 | Un ou plusieurs modèles obsolètes trouvés |

### Exécution locale
Depuis la racine du dépôt (recommandé) :

Windows (PowerShell) :
```powershell
python Workshop\scripts\lint_markdown_cli.py --verbose
```

macOS / Linux :
```bash
python Workshop/scripts/lint_markdown_cli.py --verbose
```

### Hook de pré-commit (optionnel)
```bash
echo "python Workshop/scripts/lint_markdown_cli.py" > .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```
Cela bloque les commits qui introduisent des modèles obsolètes.

### Intégration CI
Un workflow GitHub Action (`.github/workflows/markdown-cli-lint.yml`) exécute l'analyseur à chaque push et pull request vers les branches `main` et `Reactor`. Les tâches échouées doivent être corrigées avant de fusionner.

### Ajout de nouveaux modèles obsolètes
1. Ouvrez `lint_markdown_cli.py`.
2. Ajoutez un tuple `(regex, suggestion)` à la liste `DEPRECATED`. Utilisez une chaîne brute et incluez des limites de mots `\b` si nécessaire.
3. Exécutez l'analyseur localement pour vérifier la détection.
4. Commitez et poussez ; le CI appliquera la nouvelle règle.

Exemple d'ajout :
```python
DEPRECATED.append((r"\\bfoundry\\s+experimental\\s+foo\\b", "Remove experimental foo usage"))
```

### Autorisation des mentions explicatives
Étant donné que seuls les blocs de code délimités sont appliqués, vous pouvez décrire les commandes obsolètes dans le texte narratif en toute sécurité. Si vous *devez* les montrer dans un bloc délimité pour contraste, ajoutez un bloc délimité **sans** triple backticks (par exemple, en utilisant une indentation ou une citation) ou réécrivez sous forme pseudo.

### Ignorer des fichiers spécifiques (avancé)
Si nécessaire, placez des exemples anciens dans un fichier séparé hors du dépôt ou renommez avec une extension différente pendant la rédaction. Les exclusions intentionnelles pour les copies traduites sont automatiques (chemins contenant `translations`).

### Dépannage
| Problème | Cause | Résolution |
|----------|-------|------------|
| L'analyseur signale une ligne que vous avez mise à jour | Regex trop large | Affinez le modèle avec des limites de mots supplémentaires (`\b`) ou des ancres |
| Le CI échoue mais passe localement | Version Python différente ou modifications non commises | Réexécutez localement, assurez-vous que l'arborescence de travail est propre, vérifiez la version Python du workflow (3.11) |
| Besoin de contourner temporairement | Correctif d'urgence | Appliquez la correction immédiatement après ; envisagez d'utiliser une branche temporaire et une PR de suivi (évitez d'ajouter des commutateurs de contournement) |

### Raisonnement
Aligner la documentation avec la surface CLI *stable* actuelle évite les frictions lors des ateliers, réduit la confusion des apprenants et centralise la mesure des performances via des scripts Python maintenus au lieu de sous-commandes CLI obsolètes.

---
Maintenu dans le cadre de la chaîne d'outils de qualité de l'atelier. Pour des améliorations (par exemple, suggestions de correction automatique ou génération de rapports HTML), ouvrez une issue ou soumettez une PR.

## 2. Script de validation des exemples

`validate_samples.py` valide tous les fichiers d'exemples Python pour la syntaxe, les imports et la conformité aux bonnes pratiques.

### Utilisation
```bash
# Validate all samples
python scripts/validate_samples.py

# Validate specific session
python scripts/validate_samples.py --session 01

# Verbose mode (includes best practice warnings)
python scripts/validate_samples.py --verbose

# Summary only
python scripts/validate_samples.py --summary
```

### Ce qu'il vérifie
- ✅ Validité de la syntaxe Python
- ✅ Présence des imports requis
- ✅ Mise en œuvre de la gestion des erreurs (mode détaillé)
- ✅ Utilisation des annotations de type (mode détaillé)
- ✅ Docstrings des fonctions (mode détaillé)
- ✅ Liens de référence SDK (mode détaillé)

### Variables d'environnement
- `SKIP_IMPORT_CHECK=1` - Ignore la validation des imports
- `SKIP_SYNTAX_CHECK=1` - Ignore la validation de la syntaxe

### Codes de sortie
- `0` - Tous les exemples ont passé la validation
- `1` - Un ou plusieurs exemples ont échoué

## 3. Exécuteur de tests des exemples

`test_samples.py` exécute des tests rapides sur tous les exemples pour vérifier qu'ils s'exécutent sans erreurs.

### Utilisation
```bash
# Test all samples
python scripts/test_samples.py

# Test specific session
python scripts/test_samples.py --session 01

# Quick mode (shorter timeouts)
python scripts/test_samples.py --quick

# Verbose mode (show output)
python scripts/test_samples.py --verbose
```

### Prérequis
- Service Foundry Local en cours d'exécution : `foundry service start`
- Modèles chargés : `foundry model run phi-4-mini`
- Dépendances installées : `pip install -r requirements.txt`

### Ce qu'il teste
- ✅ L'exemple peut s'exécuter sans erreurs d'exécution
- ✅ La sortie requise est générée
- ✅ Gestion correcte des erreurs en cas d'échec
- ✅ Performance (temps d'exécution)

### Variables d'environnement
- `FOUNDRY_LOCAL_ALIAS=phi-4-mini` - Modèle à utiliser pour les tests
- `TEST_TIMEOUT=30` - Temps limite par exemple en secondes

### Échecs attendus
Certains tests peuvent échouer si des dépendances optionnelles ne sont pas installées (par exemple, `ragas`, `sentence-transformers`). Installez-les avec :
```bash
pip install sentence-transformers ragas datasets
```

### Codes de sortie
- `0` - Tous les tests ont réussi
- `1` - Un ou plusieurs tests ont échoué

## 4. Exportateur de benchmark Markdown

Script : `export_benchmark_markdown.py`

Génère un tableau de performance reproductible pour un ensemble de modèles.

### Utilisation
```powershell
python Workshop\scripts\export_benchmark_markdown.py --models "qwen2.5-0.5b" --prompt "Explain retrieval augmented generation briefly." --rounds 3 --output benchmark_report.md
```

### Sorties
| Fichier | Description |
|---------|-------------|
| `benchmark_report.md` | Tableau Markdown (moyenne, p95, tokens/sec, premier token optionnel) |
| `benchmark_report.json` | Tableau de métriques brut pour comparaison et historique |

### Options
| Drapeau | Description | Par défaut |
|---------|-------------|------------|
| `--models` | Alias de modèles séparés par des virgules | (requis) |
| `--prompt` | Prompt utilisé à chaque tour | (requis) |
| `--rounds` | Tours par modèle | 3 |
| `--output` | Fichier de sortie Markdown | `benchmark_report.md` |
| `--json` | Fichier de sortie JSON | `benchmark_report.json` |
| `--fail-on-empty` | Code de sortie non nul si tous les benchmarks échouent | désactivé |

La variable d'environnement `BENCH_STREAM=1` ajoute la mesure de latence du premier token.

### Remarques
- Réutilise `workshop_utils` pour un bootstrap et une mise en cache cohérents des modèles.
- Si exécuté depuis un répertoire de travail différent, le script tente des solutions de repli pour localiser `workshop_utils`.
- Pour une comparaison GPU : exécutez une fois, activez l'accélération via la configuration CLI, réexécutez et comparez le JSON.

---

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction humaine professionnelle. Nous ne sommes pas responsables des malentendus ou des interprétations erronées résultant de l'utilisation de cette traduction.
<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4d17537bea40917b825c06fd0bba5baf",
  "translation_date": "2026-01-05T13:59:55+00:00",
  "source_file": "WorkshopForAgentic/code/02.Workflow-MultiAgent/03.Application/README.md",
  "language_code": "fr"
}
-->
# Application de Podcast

Une application console pour générer des scripts de podcast en utilisant des agents IA.

## Utilisation

```bash
python podcast_app.py
```

## Flux de travail

1. **Accueil** - L'application salue l'utilisateur  
2. **Saisie du sujet** - L'utilisateur fournit un sujet pour le podcast  
3. **Agent de recherche** - Recherche des informations pertinentes  
4. **Agent de génération de script** - Crée un script de podcast  
5. **Relecture** - L'utilisateur relit et approuve/rejette le script  
6. **Sauvegarde** - Le script approuvé est enregistré dans `podcast.md`

## Exigences

- Python 3.12+  
- agent_framework  
- Toutes les dépendances de 02.WorkflowDevUI

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :  
Ce document a été traduit à l’aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforçons d’assurer l’exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des imprécisions. Le document original dans sa langue d’origine doit être considéré comme la source faisant foi. Pour les informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous ne sommes pas responsables des malentendus ou des mauvaises interprétations résultant de l’utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "aa775a734bda4590ecbe3a94a3b62197",
  "translation_date": "2026-01-05T17:21:01+00:00",
  "source_file": "WorkshopForAgentic/translation/zh-cn/README.md",
  "language_code": "fr"
}
-->
# 🎙️ Atelier du studio de podcast IA

![logo](../../../../../translated_images/fr/logo.8711e39dc8257d7b.webp)

## Ta mission

Bienvenue dans le **studio de podcast IA** ! Tu es sur le point de lancer ton propre podcast tech « Futur Byte » — mais voici la twist : tu vas construire une équipe de production pilotée par IA pour t’aider à le créer. Plus besoin de recherches sans fin, d’écriture de scripts ou de montage audio. À la place, tu deviendras un producteur de podcast avec des super-pouvoirs IA grâce à la programmation.

## Contexte

Imagine : toi et tes amis voulez démarrer un podcast sur les tendances tech les plus cool, mais tout le monde est occupé par les études, le boulot ou la vie. Que se passerait-il si tu construisais une équipe d’agents IA pour faire le travail lourd ? Un agent fait la recherche, un autre écrit des scripts captivants, un troisième transforme le texte en dialogue naturel. Ça ressemble à de la science-fiction ? Transformons ça en réalité.

## Ce que tu vas apprendre

À la fin de cet atelier, tu sauras comment :
- 🤖 Déployer ton propre modèle IA localement (pas de frais d’API, pas de cloud !)
- 🔧 Construire des agents IA professionnels qui collaborent vraiment
- 🎬 Créer un flux complet de production de podcast de l’idée à l’audio

## Ton voyage : une pièce en trois actes

Comme toute bonne histoire, nous avons trois actes. Chacun construit progressivement ton studio de podcast IA :

| Chapitre | Ta mission | Ce qui se passe | Compétences débloquées |
|---------|-----------|--------------|----------------|
| **Acte 1** | [Rencontre ton assistant IA](01.BuildAIAgentWithSLM.md) | Tu vas découvrir comment créer des agents IA capables de chatter, chercher sur le web, et même résoudre des problèmes. Pense à eux comme des stagiaires chercheurs qui ne dorment jamais. | 🎯 Construis ton premier agent<br>🛠️ Donne-lui des super-pouvoirs (outils !)<br>🧠 Apprends-lui à réfléchir<br>🌐 Connecte-le à Internet |
| **Acte 2** | [Monte ta team de production](02.AIAgentOrchestrationAndWorkflows.md) | Maintenant ça devient intéressant ! Tu vas orchestrer plusieurs agents IA qui travaillent en équipe comme une vraie team de podcast. Un fait la recherche, un écrit, toi tu valides — le travail d’équipe fait rêver. | 🎭 Coordonne plusieurs agents<br>🔄 Construis un workflow d’approbation<br>🖥️ Teste avec l’interface DevUI<br>✋ Garde le contrôle humain |
| **Acte 3** | [Fais vivre ton podcast](03.Multi-SpeakerPodcastGenerationWithVibeVoice.md) | Le final ! Transforme ton script texte en un podcast audio réaliste avec des voix convaincantes et du dialogue naturel. Ton podcast « Futur Byte » est prêt à la diffusion ! | 🎤 Magie de la synthèse vocale<br>👥 Voix multi-intervenants<br>⏱️ Audio longue durée<br>🚀 Automatisation totale |

Chaque acte débloque de nouvelles compétences. Si tu es courageux, tu peux sauter des étapes, mais on recommande de suivre dans l’ordre !

## Exigences environnementales

Cet atelier supporte divers environnements matériels :
- **CPU** : adapté pour les tests et petits usages
- **GPU** : recommandé pour la production, améliore sensiblement la vitesse d’inférence
- **NPU** : supporte les accélérateurs neuronaux nouvelle génération

## Ce dont tu as besoin

### Liste logicielle ✅
- **Python 3.10+** (ton langage de programmation)
- **Ollama** (pour faire tourner les modèles IA localement)
- **VS Code** (ton éditeur de code)
- **Extension Python** (pour rendre VS Code plus intelligent)
- **Git** (pour récupérer le code)

### Vérification matérielle 💻
- **Puis-je faire tourner ?** : 8GB RAM, 10GB espace libre (ça marche, mais un peu lent)
- **Config idéale** : 16GB+ RAM, un bon GPU (fonctionnement fluide !)
- **Tu as un NPU ?** : c’est encore mieux ! Performance nouvelle génération 🚀

## Monte ton studio 🎬

### Étape 1 : Mise à jour Python

Assure-toi d’avoir Python 3.10 ou supérieur :

```bash
python --version
# Devrait afficher Python 3.10.x ou une version supérieure
```

Pas Python ? Obtiens-le sur [python.org](https://python.org) — c’est gratuit !

### Étape 2 : Obtenir Ollama (ton moteur IA)

Va sur [ollama.ai](https://ollama.ai) pour télécharger Ollama selon ton OS. Pense à lui comme au moteur qui fait tourner les modèles IA localement.

Vérifie que tout est prêt :

```bash
ollama --version
```

### Étape 3 : Télécharge ton cerveau IA 🧠

Il est temps de récupérer le modèle Qwen-3-8B (comme embaucher ton premier assistant IA) :

```bash
ollama pull qwen3:8b
```

*Ça peut prendre quelques minutes. Le temps parfait pour un café !☕*

### Étape 4 : Installe VS Code

Si tu ne l’as pas encore, récupère [Visual Studio Code](https://code.visualstudio.com/). C’est le meilleur éditeur code (fight me 😄).

### Étape 5 : Extension Python

Dans VS Code :
1. Presse `Ctrl+Shift+X` (ou `Cmd+Shift+X` sur Mac)
2. Cherche "Python"
3. Installe l’extension officielle de Microsoft

### Étape 6 : C’est parti ! 🎉

Sérieusement, tu es prêt. Construisons un peu de magie IA !

### Étape 7 : Installe Microsoft Agent Framework et dépendances 📦

Installe toutes les dépendances requises pour l’atelier :

```bash
pip install -r ./Installations/requirements.txt -U
```

*Ça va installer Microsoft Agent Framework et tous les paquets nécessaires. Prends un café — la première installation peut prendre quelques minutes !☕*

## Notes sur l’atelier

La structure détaillée du projet, les étapes de configuration et l’exécution seront expliquées durant l’atelier.

## Dépannage (quand ça coince) 🔧

### « Aïe, le téléchargement du modèle est trop lent ! »
**Solution** : Utilise un VPN ou configure une source miroir pour Ollama. Parfois le réseau fait des siennes.

### « Mon PC rame ! Pas assez de mémoire ! »
**Solution** : Passe à un modèle plus petit ou ajuste `num_ctx` pour utiliser moins de mémoire. Pense à donner un régime à ton IA.

### « Puis-je accélérer avec un GPU ? »
**Solution** : Ollama détecte automatiquement un GPU ! Assure-toi que ton driver GPU est à jour. Boost gratuit de vitesse !🏎️

## Ressources supplémentaires (pour les curieux) 📚

- [Docs Ollama](https://github.com/ollama/ollama) — Exploration des modèles IA locaux
- [Microsoft Agent Framework](https://microsoft.github.io/autogen/) — En savoir plus sur la construction d’équipes d’agents
- [Infos modèle Qwen](https://qwenlm.github.io/) — Rencontre le cerveau de ton assistant IA

## Licence

Licence MIT — construis des choses cool, partage-les, rends le monde meilleur !🌍

## Tu veux contribuer ?

Trouvé un bug ? Une idée ? Ouvre un Issue ou PR ! On adore la communauté.✨

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :  
Ce document a été traduit à l’aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforçions d’assurer l’exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d’origine doit être considéré comme la source faisant foi. Pour les informations cruciales, il est recommandé de recourir à une traduction professionnelle humaine. Nous déclinons toute responsabilité en cas de malentendus ou de mauvaises interprétations résultant de l’utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
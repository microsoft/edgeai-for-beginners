# Chapitre 07 : Exemples d'EdgeAI

Edge AI représente la convergence de l'intelligence artificielle et du calcul en périphérie, permettant un traitement intelligent directement sur les appareils sans dépendre de la connectivité au cloud. Ce chapitre explore cinq implémentations distinctes d'EdgeAI sur différentes plateformes et frameworks, mettant en avant la polyvalence et la puissance des modèles d'IA exécutés en périphérie.

## 1. EdgeAI avec NVIDIA Jetson Orin Nano

Le NVIDIA Jetson Orin Nano marque une avancée dans le domaine du calcul Edge AI accessible, offrant jusqu'à 67 TOPS de performance IA dans un format compact de la taille d'une carte de crédit. Cette plateforme Edge AI puissante démocratise le développement d'IA générative pour les amateurs, les étudiants et les développeurs professionnels.

### Caractéristiques principales
- Offre jusqu'à 67 TOPS de performance IA, soit une amélioration de 1,7X par rapport à son prédécesseur
- 1024 cœurs CUDA et jusqu'à 32 Tensor Cores pour le traitement IA
- CPU Arm Cortex-A78AE v8.2 64 bits à 6 cœurs avec une fréquence maximale de 1,5 GHz
- Prix abordable de seulement 249 $, offrant aux développeurs, étudiants et créateurs une plateforme accessible

### Applications
Le Jetson Orin Nano excelle dans l'exécution de modèles modernes d'IA générative, notamment les transformateurs de vision, les grands modèles de langage et les modèles vision-langage. Conçu spécifiquement pour les cas d'utilisation de GenAI, il permet désormais de faire fonctionner plusieurs LLMs sur un appareil de la taille de la paume. Les cas d'utilisation populaires incluent la robotique alimentée par l'IA, les drones intelligents, les caméras intelligentes et les appareils autonomes en périphérie.

**En savoir plus** : [Superordinateur Jetson Orin Nano de NVIDIA : La prochaine grande avancée en EdgeAI](https://medium.com/data-science-in-your-pocket/nvidias-jetson-orin-nano-supercomputer-the-next-big-thing-in-edgeai-e9eff687ae62)

## 2. EdgeAI dans les applications mobiles avec .NET MAUI et ONNX Runtime GenAI

Cette solution montre comment intégrer l'IA générative et les grands modèles de langage (LLMs) dans des applications mobiles multiplateformes en utilisant .NET MAUI (Multi-platform App UI) et ONNX Runtime GenAI. Cette approche permet aux développeurs .NET de créer des applications mobiles sophistiquées alimentées par l'IA, fonctionnant nativement sur les appareils Android et iOS.

### Caractéristiques principales
- Basé sur le framework .NET MAUI, offrant une base de code unique pour les applications Android et iOS
- Intégration d'ONNX Runtime GenAI permettant l'exécution de modèles d'IA générative directement sur les appareils mobiles
- Prise en charge de divers accélérateurs matériels adaptés aux appareils mobiles, notamment CPU, GPU et processeurs IA spécialisés
- Optimisations spécifiques à la plateforme comme CoreML pour iOS et NNAPI pour Android via ONNX Runtime
- Implémente le cycle complet de l'IA générative, y compris le prétraitement, l'inférence, le traitement des logits, la recherche et l'échantillonnage, ainsi que la gestion du cache KV

### Avantages pour les développeurs
L'approche .NET MAUI permet aux développeurs de tirer parti de leurs compétences existantes en C# et .NET tout en créant des applications IA multiplateformes. Le framework ONNX Runtime GenAI prend en charge plusieurs architectures de modèles, notamment Llama, Mistral, Phi, Gemma, et bien d'autres. Les noyaux ARM64 optimisés accélèrent la multiplication matricielle quantifiée INT4, garantissant des performances efficaces sur le matériel mobile tout en conservant l'expérience de développement familière de .NET.

### Cas d'utilisation
Cette solution est idéale pour les développeurs souhaitant créer des applications mobiles alimentées par l'IA en utilisant les technologies .NET, notamment des chatbots intelligents, des applications de reconnaissance d'image, des outils de traduction linguistique et des systèmes de recommandation personnalisés fonctionnant entièrement sur l'appareil pour une confidentialité accrue et une capacité hors ligne.

**En savoir plus** : [Exemple .NET MAUI ONNX Runtime GenAI](https://github.com/microsoft/onnxruntime-genai/tree/jialli/genny-maui/examples/csharp/GennyMaui)

## 3. EdgeAI dans Azure avec le moteur des petits modèles de langage

La solution EdgeAI basée sur Azure de Microsoft se concentre sur le déploiement efficace des petits modèles de langage (SLMs) dans des environnements hybrides cloud-périphérie. Cette approche comble le fossé entre les services d'IA à l'échelle du cloud et les exigences de déploiement en périphérie.

### Avantages de l'architecture
- Intégration transparente avec les services Azure AI
- Exécution des SLMs/LLMs et des modèles multimodaux sur l'appareil et dans le cloud avec ONNX Runtime
- Optimisé pour les déploiements à l'échelle de l'entreprise
- Prise en charge des mises à jour et de la gestion continues des modèles

### Cas d'utilisation
L'implémentation Azure EdgeAI excelle dans les scénarios nécessitant un déploiement IA de niveau entreprise avec des capacités de gestion cloud. Cela inclut le traitement intelligent de documents, l'analyse en temps réel et les flux de travail hybrides d'IA exploitant à la fois les ressources cloud et périphériques.

**En savoir plus** : [Moteur SLM Azure EdgeAI](https://github.com/microsoft/onnxruntime-genai/tree/main/examples/slm_engine)

## [4. EdgeAI avec Windows ML](./windowdeveloper.md)

Windows ML représente le runtime de pointe de Microsoft, optimisé pour l'inférence performante des modèles sur l'appareil et le déploiement simplifié, servant de base à Windows AI Foundry. Cette plateforme permet aux développeurs de créer des applications Windows alimentées par l'IA, exploitant tout le potentiel du matériel PC.

### Capacités de la plateforme
- Fonctionne sur tous les PC Windows 11 exécutant la version 24H2 (build 26100) ou supérieure
- Compatible avec tout le matériel PC x64 et ARM64, même les PC sans NPU ou GPU
- Permet aux développeurs d'apporter leurs propres modèles et de les déployer efficacement sur l'écosystème des partenaires silicium, notamment AMD, Intel, NVIDIA et Qualcomm, couvrant CPU, GPU, NPU
- Grâce aux API d'infrastructure, les développeurs n'ont plus besoin de créer plusieurs versions de leur application pour cibler différents siliciums

### Avantages pour les développeurs
Windows ML abstrait le matériel et les fournisseurs d'exécution, vous permettant de vous concentrer sur l'écriture de votre code. De plus, Windows ML se met automatiquement à jour pour prendre en charge les derniers NPUs, GPUs et CPUs dès leur sortie. La plateforme offre un cadre unifié pour le développement IA sur l'écosystème matériel diversifié de Windows.

**En savoir plus** : 
- [Aperçu de Windows ML](https://learn.microsoft.com/en-us/windows/ai/new-windows-ml/overview)
- [Guide de développement Windows EdgeAI](./windowdeveloper.md) - Guide complet pour le développement Edge AI sur Windows

## [5. EdgeAI avec Foundry Local Applications](./foundrylocal.md)

Foundry Local permet aux développeurs Windows et Mac de créer des applications de génération augmentée par récupération (RAG) en utilisant des ressources locales dans .NET, combinant des modèles de langage locaux avec des capacités de recherche sémantique. Cette approche offre des solutions IA axées sur la confidentialité, fonctionnant entièrement sur une infrastructure locale.

### Architecture technique
- Combine le modèle de langage Phi, les embeddings locaux et le Kernel sémantique pour créer un scénario RAG
- Utilise des embeddings sous forme de vecteurs (tableaux) de valeurs en virgule flottante représentant le contenu et sa signification sémantique
- Le Kernel sémantique agit comme l'orchestrateur principal, intégrant Phi et les composants intelligents pour créer un pipeline RAG fluide
- Prise en charge des bases de données vectorielles locales, notamment SQLite et Qdrant

### Avantages de l'implémentation
RAG, ou génération augmentée par récupération, est simplement une manière élégante de dire "rechercher des informations et les intégrer dans l'invite". Cette implémentation locale garantit la confidentialité des données tout en fournissant des réponses intelligentes basées sur des bases de connaissances personnalisées. L'approche est particulièrement précieuse pour les scénarios d'entreprise nécessitant la souveraineté des données et des capacités hors ligne.

**En savoir plus** : 
- [Foundry Local](./foundrylocal.md)
- [Exemples RAG Foundry Local](https://github.com/microsoft/Foundry-Local/tree/main/samples/dotNET/rag)

### Windows Foundry Local

Microsoft Foundry Local fournit un serveur REST compatible OpenAI, alimenté par ONNX Runtime, pour exécuter des modèles localement sur Windows. Voici un résumé rapide et validé ; consultez la documentation officielle pour plus de détails.

- Commencer : https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started
- Architecture : https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture
- Référence CLI : https://learn.microsoft.com/azure/ai-foundry/foundry-local/reference/reference-cli
- Guide complet pour Windows dans ce dépôt : [foundrylocal.md](./foundrylocal.md)

Installer ou mettre à jour sur Windows (cmd.exe) :
```cmd
winget install Microsoft.FoundryLocal
winget upgrade --id Microsoft.FoundryLocal
foundry --version
```

Explorer les catégories CLI :
```cmd
foundry model --help
foundry service --help
foundry cache --help
```

Exécuter un modèle et découvrir le point de terminaison dynamique :
```cmd
foundry model run gpt-oss-20b
foundry service status
```

Vérification REST rapide pour lister les modèles (remplacer PORT par le statut) :
```cmd
curl -s http://localhost:PORT/v1/models
```

Conseils :
- Intégration SDK : https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks
- Apporter votre propre modèle (compiler) : https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models

## Ressources de développement Windows EdgeAI

Pour les développeurs ciblant spécifiquement la plateforme Windows, nous avons créé un guide complet couvrant l'écosystème Windows EdgeAI. Cette ressource fournit des informations détaillées sur Windows AI Foundry, y compris les API, outils et meilleures pratiques pour le développement EdgeAI sur Windows.

### Plateforme Windows AI Foundry
La plateforme Windows AI Foundry offre une suite complète d'outils et d'API spécialement conçus pour le développement Edge AI sur les appareils Windows. Cela inclut un support spécialisé pour le matériel accéléré par NPU, l'intégration Windows ML et des techniques d'optimisation spécifiques à la plateforme.

**Guide complet** : [Guide de développement Windows EdgeAI](../windowdeveloper.md)

Ce guide couvre :
- Aperçu de la plateforme Windows AI Foundry et de ses composants
- API Phi Silica pour une inférence efficace sur le matériel NPU
- API de vision par ordinateur pour le traitement d'image et l'OCR
- Intégration et optimisation du runtime Windows ML
- CLI Foundry Local pour le développement et les tests locaux
- Stratégies d'optimisation matérielle pour les appareils Windows
- Exemples pratiques d'implémentation et meilleures pratiques

### [Kit d'outils IA pour le développement Edge AI](./aitoolkit.md)
Pour les développeurs utilisant Visual Studio Code, l'extension AI Toolkit fournit un environnement de développement complet spécialement conçu pour la création, les tests et le déploiement d'applications Edge AI. Ce kit d'outils simplifie l'ensemble du flux de travail de développement Edge AI dans VS Code.

**Guide de développement** : [Kit d'outils IA pour le développement Edge AI](./aitoolkit.md)

Le guide du kit d'outils IA couvre :
- Découverte et sélection de modèles pour le déploiement en périphérie
- Flux de travail de test et d'optimisation locaux
- Intégration ONNX et Ollama pour les modèles en périphérie
- Techniques de conversion et de quantification des modèles
- Développement d'agents pour les scénarios en périphérie
- Évaluation des performances et surveillance
- Préparation au déploiement et meilleures pratiques

## Conclusion

Ces cinq implémentations d'EdgeAI démontrent la maturité et la diversité des solutions Edge AI disponibles aujourd'hui. Des appareils en périphérie accélérés par le matériel comme le Jetson Orin Nano aux frameworks logiciels comme ONNX Runtime GenAI et Windows ML, les développeurs disposent d'options sans précédent pour déployer des applications intelligentes en périphérie.

Le fil conducteur de toutes ces plateformes est la démocratisation des capacités d'IA, rendant l'apprentissage automatique sophistiqué accessible aux développeurs de différents niveaux de compétence et cas d'utilisation. Que ce soit pour créer des applications mobiles, des logiciels de bureau ou des systèmes embarqués, ces solutions EdgeAI fournissent la base de la prochaine génération d'applications intelligentes fonctionnant efficacement et en toute confidentialité en périphérie.

Chaque plateforme offre des avantages uniques : Jetson Orin Nano pour le calcul en périphérie accéléré par le matériel, ONNX Runtime GenAI pour le développement mobile multiplateforme, Azure EdgeAI pour l'intégration cloud-périphérie d'entreprise, Windows ML pour les applications natives Windows, et Foundry Local pour les implémentations RAG axées sur la confidentialité. Ensemble, elles représentent un écosystème complet pour le développement EdgeAI.

[Prochain Kit d'outils IA](aitoolkit.md)

---

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction humaine professionnelle. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées résultant de l'utilisation de cette traduction.
# Module 08 Échantillons : Guide de développement local Foundry

## Aperçu

Cette collection complète illustre les approches **Foundry Local SDK** et **Commandes Shell** pour créer des applications d'IA prêtes pour la production. Chaque exemple met en avant différents aspects du développement d'IA en périphérie, allant de l'intégration REST basique à des systèmes multi-agents avancés.

## Approche de développement : SDK vs Commandes Shell

### Utilisez Foundry Local SDK lorsque :

- **Contrôle programmatique** : Vous avez besoin d'un contrôle total sur le cycle de vie des agents, l'évaluation ou les workflows de déploiement
- **Outils personnalisés** : Automatisation autour de Foundry Local (intégration CI/CD, orchestration multi-agents)
- **Accès détaillé** : Nécessité de métadonnées d'agent détaillées, de gestion des versions ou de contrôle des évaluations
- **Intégration Python** : Travail dans des environnements fortement orientés Python ou intégration de la logique Foundry dans des applications plus larges
- **Workflows d'entreprise** : Mise en œuvre de workflows modulaires et pipelines d'évaluation reproductibles alignés sur les architectures de référence Microsoft

### Utilisez les commandes Shell lorsque :

- **Tests rapides** : Effectuer des tests locaux rapides, des lancements manuels d'agents ou des vérifications de configuration
- **Simplicité CLI** : Besoin d'opérations CLI simples pour démarrer/arrêter des agents, vérifier les journaux ou effectuer des évaluations basiques
- **Automatisation légère** : Script d'automatisation simple sans nécessiter une intégration complète du SDK
- **Itération rapide** : Cycles de débogage et de développement, notamment dans des environnements contraints ou des déploiements au niveau des groupes de ressources
- **Configuration et validation** : Configuration initiale de l'environnement et tâches de vérification rapide

## Meilleures pratiques et workflow recommandé

Basé sur la gestion du cycle de vie des agents, le suivi des dépendances et les principes de reproductibilité avec privilèges minimaux :

### Phase 1 : Fondations et configuration
1. **Commencez avec les commandes Shell** pour la configuration initiale et la validation rapide
2. **Vérifiez l'environnement** à l'aide des outils CLI et du déploiement de modèles basiques
3. **Testez la connectivité** avec des appels REST simples et des vérifications de santé

### Phase 2 : Développement et intégration
1. **Passez au SDK** pour des workflows évolutifs et traçables
2. **Implémentez un contrôle programmatique** pour des interactions complexes entre agents
3. **Créez des outils personnalisés** pour des modèles prêts pour la communauté et l'intégration Azure OpenAI

### Phase 3 : Production et mise à l'échelle
1. **Approche hybride** combinant CLI pour les opérations et SDK pour la logique applicative
2. **Intégration d'entreprise** avec surveillance, journalisation et pipelines de déploiement
3. **Contribution communautaire** via des modèles réutilisables et des meilleures pratiques

---

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction humaine professionnelle. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées résultant de l'utilisation de cette traduction.
# Démo WebGPU + ONNX Runtime

Cette démonstration montre comment exécuter des modèles d'IA directement dans le navigateur en utilisant WebGPU pour l'accélération matérielle et ONNX Runtime Web.

## Ce que cela démontre

- **IA dans le navigateur** : Exécutez des modèles entièrement dans le navigateur
- **Accélération WebGPU** : Inférence accélérée par le matériel lorsque disponible
- **Respect de la vie privée** : Aucune donnée ne quitte votre appareil
- **Sans installation** : Fonctionne dans tout navigateur compatible
- **Retour en douceur** : Bascule sur le CPU si WebGPU n'est pas disponible

## Prérequis

**Compatibilité du navigateur :**
- Chrome/Edge 113+ avec WebGPU activé
- Vérifiez le statut de WebGPU : `chrome://gpu`
- Activez WebGPU : `chrome://flags/#enable-unsafe-webgpu`

## Exécuter la démo

### Option 1 : Serveur local (recommandé)

```cmd
# Navigate to the demo directory
cd Module08\samples\04\webgpu-demo

# Start a local server
python -m http.server 5173

# Open browser to http://localhost:5173
```

### Option 2 : Serveur Live de VS Code

1. Installez l'extension "Live Server" dans VS Code
2. Clic droit sur `index.html` → "Open with Live Server"
3. La démo s'ouvre automatiquement dans le navigateur

## Ce que vous verrez

1. **Détection de WebGPU** : Vérifie la compatibilité du navigateur
2. **Chargement du modèle** : Télécharge et initialise le classificateur MNIST
3. **Exécution de l'inférence** : Effectue une prédiction sur des données d'exemple
4. **Mesures de performance** : Affiche le temps de chargement et la vitesse d'inférence
5. **Affichage des résultats** : Confiance des prédictions et sorties brutes

## Performances attendues

| Fournisseur d'exécution | Chargement du modèle | Inférence | Remarques |
|-------------------------|----------------------|-----------|-----------|
| **WebGPU**              | ~2-5s               | ~10-50ms  | Accéléré par le matériel |
| **CPU (WASM)**          | ~2-5s               | ~50-200ms | Retour logiciel |

## Résolution des problèmes

**WebGPU non disponible :**
- Mettez à jour vers Chrome/Edge 113+
- Activez WebGPU dans `chrome://flags`
- Vérifiez que les pilotes GPU sont à jour
- La démo basculera automatiquement sur le CPU

**Erreurs de chargement :**
- Assurez-vous de servir via HTTP (et non file://)
- Vérifiez la connexion réseau pour le téléchargement du modèle
- Assurez-vous que CORS ne bloque pas le modèle ONNX

**Problèmes de performance :**
- WebGPU offre une accélération significative par rapport au CPU
- La première exécution peut être plus lente en raison du téléchargement du modèle
- Les exécutions suivantes utilisent le cache du navigateur

## Intégration avec Foundry Local

Cette démo WebGPU complète Foundry Local en montrant :

- **Inférence côté client** pour une confidentialité maximale
- **Capacités hors ligne** lorsque l'accès à Internet est indisponible  
- **Déploiement en périphérie** pour des environnements à ressources limitées
- **Architectures hybrides** combinant inférence locale et serveur

Pour des applications en production, envisagez :
- Utiliser Foundry Local pour l'inférence côté serveur
- Utiliser WebGPU pour le prétraitement/post-traitement côté client
- Implémenter un routage intelligent entre l'inférence locale et distante

## Détails techniques

**Modèle utilisé :**
- Classificateur de chiffres MNIST (format ONNX)
- Entrée : Images en niveaux de gris 28x28
- Sortie : Distribution de probabilité à 10 classes
- Taille : ~500KB (téléchargement rapide)

**ONNX Runtime Web :**
- Fournisseur d'exécution WebGPU pour l'accélération GPU
- Fournisseur d'exécution WASM pour le retour CPU
- Optimisation automatique et optimisation des graphes

**APIs du navigateur :**
- WebGPU pour l'accès au matériel
- Web Workers pour le traitement en arrière-plan (amélioration future)
- WebAssembly pour des calculs efficaces

## Prochaines étapes

- Essayez avec des modèles ONNX personnalisés
- Implémentez le téléchargement d'images réelles et leur classification
- Ajoutez une inférence en streaming pour des modèles plus grands
- Intégrez des entrées caméra/microphone

---


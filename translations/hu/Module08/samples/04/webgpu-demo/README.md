# WebGPU + ONNX Runtime Bemutató

Ez a bemutató megmutatja, hogyan futtathatunk AI modelleket közvetlenül a böngészőben WebGPU hardveres gyorsítással és ONNX Runtime Web segítségével.

## Mit Mutat Be Ez?

- **Böngésző-alapú AI**: Modellek futtatása teljesen a böngészőben
- **WebGPU Gyorsítás**: Hardveres gyorsítású következtetés, ha elérhető
- **Adatvédelem elsőként**: Az adatok nem hagyják el az eszközt
- **Telepítés nélkül**: Működik bármely kompatibilis böngészőben
- **Zökkenőmentes Visszaállás**: CPU-ra vált, ha WebGPU nem elérhető

## Követelmények

**Böngésző Kompatibilitás:**
- Chrome/Edge 113+ WebGPU engedélyezéssel
- WebGPU állapot ellenőrzése: `chrome://gpu`
- WebGPU engedélyezése: `chrome://flags/#enable-unsafe-webgpu`

## A Bemutató Futtatása

### 1. Opció: Helyi Szerver (Ajánlott)

```cmd
# Navigate to the demo directory
cd Module08\samples\04\webgpu-demo

# Start a local server
python -m http.server 5173

# Open browser to http://localhost:5173
```

### 2. Opció: VS Code Live Server

1. Telepítse a "Live Server" bővítményt a VS Code-ban
2. Kattintson jobb gombbal az `index.html` fájlra → "Open with Live Server"
3. A bemutató automatikusan megnyílik a böngészőben

## Mit Fog Látni?

1. **WebGPU Érzékelés**: Ellenőrzi a böngésző kompatibilitását
2. **Model Betöltés**: Letölti és inicializálja az MNIST osztályozót
3. **Következtetés Végrehajtása**: Mintaadatokon futtatja a predikciót
4. **Teljesítménymutatók**: Betöltési idő és következtetési sebesség megjelenítése
5. **Eredmények Kijelzése**: Predikciós bizalom és nyers kimenetek

## Várható Teljesítmény

| Végrehajtási Szolgáltató | Modell Betöltés | Következtetés | Megjegyzések |
|--------------------------|-----------------|---------------|--------------|
| **WebGPU**              | ~2-5s          | ~10-50ms      | Hardveres gyorsítás |
| **CPU (WASM)**          | ~2-5s          | ~50-200ms     | Szoftveres visszaállás |

## Hibakeresés

**WebGPU Nem Elérhető:**
- Frissítse Chrome/Edge 113+ verzióra
- Engedélyezze a WebGPU-t a `chrome://flags` alatt
- Ellenőrizze, hogy a GPU illesztőprogramok naprakészek-e
- A bemutató automatikusan CPU-ra vált

**Betöltési Hibák:**
- Győződjön meg róla, hogy HTTP-n keresztül szolgáltat (nem file://)
- Ellenőrizze a hálózati kapcsolatot a modell letöltéséhez
- Ellenőrizze, hogy a CORS nem blokkolja-e az ONNX modellt

**Teljesítményproblémák:**
- A WebGPU jelentős gyorsítást nyújt a CPU-hoz képest
- Az első futtatás lassabb lehet a modell letöltése miatt
- A későbbi futtatások a böngésző gyorsítótárát használják

## Integráció a Foundry Local-lal

Ez a WebGPU bemutató kiegészíti a Foundry Local-t az alábbiak bemutatásával:

- **Kliensoldali következtetés** a maximális adatvédelem érdekében
- **Offline képességek** internetkapcsolat hiányában  
- **Edge telepítés** erőforrás-korlátozott környezetekben
- **Hibrid architektúrák** helyi és szerveroldali következtetés kombinálásával

A gyártási alkalmazásokhoz fontolja meg:
- Használja a Foundry Local-t szerveroldali következtetéshez
- Használja a WebGPU-t kliensoldali elő-/utófeldolgozáshoz
- Valósítsa meg az intelligens irányítást helyi/távoli következtetés között

## Technikai Részletek

**Használt Modell:**
- MNIST számjegy osztályozó (ONNX formátum)
- Bemenet: 28x28 szürkeárnyalatos képek
- Kimenet: 10-osztályos valószínűségi eloszlás
- Méret: ~500KB (gyors letöltés)

**ONNX Runtime Web:**
- WebGPU végrehajtási szolgáltató GPU gyorsításhoz
- WASM végrehajtási szolgáltató CPU visszaálláshoz
- Automatikus optimalizálás és gráf optimalizálás

**Böngésző API-k:**
- WebGPU hardver hozzáféréshez
- Web Workers háttérfeldolgozáshoz (jövőbeli fejlesztés)
- WebAssembly hatékony számításokhoz

## Következő Lépések

- Próbálja ki egyedi ONNX modellekkel
- Valósítsa meg valódi képfeltöltést és osztályozást
- Adjon hozzá streaming következtetést nagyobb modellekhez
- Integrálja kamera/mikrofon bemenettel

---


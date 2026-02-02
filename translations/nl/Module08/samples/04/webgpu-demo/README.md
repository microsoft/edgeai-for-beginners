# WebGPU + ONNX Runtime Demo

Deze demo laat zien hoe je AI-modellen direct in de browser kunt uitvoeren met WebGPU voor hardwareversnelling en ONNX Runtime Web.

## Wat Deze Demo Laat Zien

- **AI in de browser**: Voer modellen volledig in de browser uit
- **WebGPU Versnelling**: Hardware-versnelde inferentie waar beschikbaar
- **Privacy eerst**: Geen data verlaat je apparaat
- **Geen installatie nodig**: Werkt in elke compatibele browser
- **Vlotte terugval**: Valt terug op CPU als WebGPU niet beschikbaar is

## Vereisten

**Browsercompatibiliteit:**
- Chrome/Edge 113+ met WebGPU ingeschakeld
- Controleer WebGPU-status: `chrome://gpu`
- WebGPU inschakelen: `chrome://flags/#enable-unsafe-webgpu`

## De Demo Uitvoeren

### Optie 1: Lokale Server (Aanbevolen)

```cmd
# Navigate to the demo directory
cd Module08\samples\04\webgpu-demo

# Start a local server
python -m http.server 5173

# Open browser to http://localhost:5173
```

### Optie 2: VS Code Live Server

1. Installeer de "Live Server"-extensie in VS Code
2. Klik met de rechtermuisknop op `index.html` → "Open met Live Server"
3. De demo opent automatisch in de browser

## Wat Je Zult Zien

1. **WebGPU Detectie**: Controleert browsercompatibiliteit
2. **Model Laden**: Downloadt en initialiseert MNIST-classificator
3. **Inferentie Uitvoeren**: Voert voorspellingen uit op voorbeelddata
4. **Prestatiemetrics**: Toont laadtijd en inferentiesnelheid
5. **Resultaten Weergeven**: Voorspellingszekerheid en ruwe outputs

## Verwachte Prestaties

| Execution Provider | Model Laden | Inferentie | Opmerkingen |
|-------------------|------------|-----------|-------------|
| **WebGPU** | ~2-5s | ~10-50ms | Hardware-versneld |
| **CPU (WASM)** | ~2-5s | ~50-200ms | Software-terugval |

## Problemen Oplossen

**WebGPU Niet Beschikbaar:**
- Update naar Chrome/Edge 113+
- Schakel WebGPU in via `chrome://flags`
- Controleer of GPU-stuurprogramma's up-to-date zijn
- Demo valt automatisch terug op CPU

**Laadfouten:**
- Zorg ervoor dat je via HTTP serveert (niet file://)
- Controleer netwerkverbinding voor modeldownload
- Verifieer dat CORS de ONNX-model niet blokkeert

**Prestatieproblemen:**
- WebGPU biedt aanzienlijke snelheidswinst ten opzichte van CPU
- Eerste uitvoering kan trager zijn door modeldownload
- Latere uitvoeringen gebruiken browsercache

## Integratie met Foundry Local

Deze WebGPU-demo vult Foundry Local aan door te laten zien:

- **Client-side inferentie** voor ultieme privacy
- **Offline mogelijkheden** wanneer internet niet beschikbaar is  
- **Edge-deployment** voor omgevingen met beperkte middelen
- **Hybride architecturen** die lokale en server-inferentie combineren

Voor productieapplicaties kun je overwegen:
- Gebruik Foundry Local voor server-side inferentie
- Gebruik WebGPU voor client-side preprocessing/postprocessing
- Implementeer intelligente routing tussen lokale en externe inferentie

## Technische Details

**Gebruikt Model:**
- MNIST cijferclassificator (ONNX-formaat)
- Input: 28x28 grijswaardenafbeeldingen
- Output: 10-klasse waarschijnlijkheidsverdeling
- Grootte: ~500KB (snelle download)

**ONNX Runtime Web:**
- WebGPU execution provider voor GPU-versnelling
- WASM execution provider voor CPU-terugval
- Automatische optimalisatie en grafoptimalisatie

**Browser API's:**
- WebGPU voor hardwaretoegang
- Web Workers voor achtergrondverwerking (toekomstige verbetering)
- WebAssembly voor efficiënte berekeningen

## Volgende Stappen

- Probeer met aangepaste ONNX-modellen
- Implementeer echte afbeeldingsupload en classificatie
- Voeg streaming-inferentie toe voor grotere modellen
- Integreer met camera-/microfooningang

---


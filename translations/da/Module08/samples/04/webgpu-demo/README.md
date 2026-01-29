# WebGPU + ONNX Runtime Demo

Denne demo viser, hvordan man kan køre AI-modeller direkte i browseren ved hjælp af WebGPU til hardwareacceleration og ONNX Runtime Web.

## Hvad Denne Demo Viser

- **Browser-baseret AI**: Kør modeller helt i browseren
- **WebGPU Acceleration**: Hardware-accelereret inferens, når det er muligt
- **Privatliv først**: Ingen data forlader din enhed
- **Ingen installation**: Fungerer i enhver kompatibel browser
- **Smidig fallback**: Fald tilbage til CPU, hvis WebGPU ikke er tilgængelig

## Krav

**Browserkompatibilitet:**
- Chrome/Edge 113+ med WebGPU aktiveret
- Tjek WebGPU-status: `chrome://gpu`
- Aktiver WebGPU: `chrome://flags/#enable-unsafe-webgpu`

## Sådan Kører Du Demoen

### Mulighed 1: Lokal Server (Anbefalet)

```cmd
# Navigate to the demo directory
cd Module08\samples\04\webgpu-demo

# Start a local server
python -m http.server 5173

# Open browser to http://localhost:5173
```

### Mulighed 2: VS Code Live Server

1. Installer "Live Server"-udvidelsen i VS Code
2. Højreklik på `index.html` → "Open with Live Server"
3. Demoen åbnes automatisk i browseren

## Hvad Du Vil Se

1. **WebGPU-detektion**: Tjekker browserkompatibilitet
2. **Modelindlæsning**: Downloader og initialiserer MNIST-klassifikatoren
3. **Inferensudførelse**: Kører forudsigelse på eksempeldata
4. **Ydelsesmålinger**: Viser indlæsningstid og inferenshastighed
5. **Resultatvisning**: Forudsigelsessikkerhed og rå outputs

## Forventet Ydelse

| Execution Provider | Modelindlæsning | Inferens | Noter |
|-------------------|-----------------|----------|-------|
| **WebGPU** | ~2-5s | ~10-50ms | Hardware-accelereret |
| **CPU (WASM)** | ~2-5s | ~50-200ms | Software fallback |

## Fejlfinding

**WebGPU Ikke Tilgængelig:**
- Opdater til Chrome/Edge 113+
- Aktiver WebGPU i `chrome://flags`
- Tjek, om GPU-drivere er opdaterede
- Demoen falder automatisk tilbage til CPU

**Indlæsningsfejl:**
- Sørg for, at du serverer via HTTP (ikke file://)
- Tjek netværksforbindelsen for modeldownload
- Verificer, at CORS ikke blokerer ONNX-modellen

**Ydelsesproblemer:**
- WebGPU giver betydelig hastighedsforøgelse over CPU
- Første kørsel kan være langsommere på grund af modeldownload
- Efterfølgende kørsler bruger browserens cache

## Integration med Foundry Local

Denne WebGPU-demo supplerer Foundry Local ved at vise:

- **Klient-side inferens** for ultimativt privatliv
- **Offline funktionalitet** når internet ikke er tilgængeligt  
- **Edge-udrulning** for ressourcebegrænsede miljøer
- **Hybridarkitekturer** der kombinerer lokal og serverbaseret inferens

For produktionsapplikationer, overvej:
- Brug Foundry Local til server-side inferens
- Brug WebGPU til klient-side forbehandling/efterbehandling
- Implementer intelligent routing mellem lokal/fjern inferens

## Tekniske Detaljer

**Model Bruges:**
- MNIST-cifferklassifikator (ONNX-format)
- Input: 28x28 gråtonede billeder
- Output: 10-klasses sandsynlighedsfordeling
- Størrelse: ~500KB (hurtig download)

**ONNX Runtime Web:**
- WebGPU execution provider til GPU-acceleration
- WASM execution provider til CPU fallback
- Automatisk optimering og grafoptimering

**Browser-API'er:**
- WebGPU til hardwareadgang
- Web Workers til baggrundsprocesser (fremtidig forbedring)
- WebAssembly til effektiv beregning

## Næste Skridt

- Prøv med egne ONNX-modeller
- Implementer ægte billedupload og klassifikation
- Tilføj streaming-inferens til større modeller
- Integrer med kamera/mikrofon-input

---


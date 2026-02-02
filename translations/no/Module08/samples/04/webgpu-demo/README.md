# WebGPU + ONNX Runtime Demo

Denne demoen viser hvordan man kan kjøre AI-modeller direkte i nettleseren ved hjelp av WebGPU for maskinvareakselerasjon og ONNX Runtime Web.

## Hva Dette Demonstrerer

- **Nettleserbasert AI**: Kjører modeller helt og holdent i nettleseren
- **WebGPU-akselerasjon**: Maskinvareakselerert inferens når tilgjengelig
- **Personvern først**: Ingen data forlater enheten din
- **Ingen installasjon**: Fungerer i enhver kompatibel nettleser
- **Smidig fallback**: Går over til CPU hvis WebGPU ikke er tilgjengelig

## Krav

**Nettleserkompatibilitet:**
- Chrome/Edge 113+ med WebGPU aktivert
- Sjekk WebGPU-status: `chrome://gpu`
- Aktiver WebGPU: `chrome://flags/#enable-unsafe-webgpu`

## Kjøre Demoen

### Alternativ 1: Lokal Server (Anbefalt)

```cmd
# Navigate to the demo directory
cd Module08\samples\04\webgpu-demo

# Start a local server
python -m http.server 5173

# Open browser to http://localhost:5173
```

### Alternativ 2: VS Code Live Server

1. Installer "Live Server"-utvidelsen i VS Code
2. Høyreklikk på `index.html` → "Open with Live Server"
3. Demoen åpnes automatisk i nettleseren

## Hva Du Vil Se

1. **WebGPU-deteksjon**: Sjekker nettleserkompatibilitet
2. **Modellinnlasting**: Laster ned og initialiserer MNIST-klassifiserer
3. **Inferensutførelse**: Kjører prediksjon på eksempeldata
4. **Ytelsesmålinger**: Viser lastetid og inferenshastighet
5. **Resultatvisning**: Prediksjonskonfidens og råutdata

## Forventet Ytelse

| Utførelsesleverandør | Modellinnlasting | Inferens | Notater |
|-----------------------|------------------|----------|---------|
| **WebGPU**           | ~2-5s           | ~10-50ms | Maskinvareakselerert |
| **CPU (WASM)**       | ~2-5s           | ~50-200ms | Programvarefallback |

## Feilsøking

**WebGPU Ikke Tilgjengelig:**
- Oppdater til Chrome/Edge 113+
- Aktiver WebGPU i `chrome://flags`
- Sjekk at GPU-driverne er oppdaterte
- Demoen vil automatisk gå over til CPU

**Innlastingsfeil:**
- Sørg for at du serverer via HTTP (ikke file://)
- Sjekk nettverkstilkoblingen for modellnedlasting
- Verifiser at CORS ikke blokkerer ONNX-modellen

**Ytelsesproblemer:**
- WebGPU gir betydelig hastighetsforbedring over CPU
- Første kjøring kan være tregere på grunn av modellnedlasting
- Etterfølgende kjøringer bruker nettleserens cache

## Integrasjon med Foundry Local

Denne WebGPU-demoen utfyller Foundry Local ved å vise:

- **Klientbasert inferens** for maksimal personvern
- **Offline-funksjonalitet** når internett ikke er tilgjengelig  
- **Edge-distribusjon** for ressursbegrensede miljøer
- **Hybridarkitekturer** som kombinerer lokal og serverbasert inferens

For produksjonsapplikasjoner, vurder:
- Bruk Foundry Local for serverbasert inferens
- Bruk WebGPU for klientbasert for- og etterprosessering
- Implementer intelligent ruting mellom lokal og fjernbasert inferens

## Tekniske Detaljer

**Brukt Modell:**
- MNIST-sifferklassifiserer (ONNX-format)
- Input: 28x28 gråskalabilder
- Output: 10-klasses sannsynlighetsfordeling
- Størrelse: ~500KB (rask nedlasting)

**ONNX Runtime Web:**
- WebGPU utførelsesleverandør for GPU-akselerasjon
- WASM utførelsesleverandør for CPU-fallback
- Automatisk optimalisering og grafoptimalisering

**Nettleser-APIer:**
- WebGPU for maskinvaretilgang
- Web Workers for bakgrunnsprosessering (fremtidig forbedring)
- WebAssembly for effektiv beregning

## Neste Steg

- Prøv med egne ONNX-modeller
- Implementer ekte bildeopplasting og klassifisering
- Legg til strømmende inferens for større modeller
- Integrer med kamera-/mikrofoninngang

---


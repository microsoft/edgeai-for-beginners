# WebGPU + ONNX Runtime Demo

Den här demon visar hur man kan köra AI-modeller direkt i webbläsaren med hjälp av WebGPU för hårdvaruacceleration och ONNX Runtime Web.

## Vad Detta Demonstrerar

- **AI i webbläsaren**: Kör modeller helt och hållet i webbläsaren
- **WebGPU-acceleration**: Hårdvaruaccelererad inferens när tillgängligt
- **Integritet först**: Ingen data lämnar din enhet
- **Ingen installation**: Fungerar i alla kompatibla webbläsare
- **Smidig fallback**: Går över till CPU om WebGPU inte är tillgängligt

## Krav

**Webbläsarkompatibilitet:**
- Chrome/Edge 113+ med WebGPU aktiverat
- Kontrollera WebGPU-status: `chrome://gpu`
- Aktivera WebGPU: `chrome://flags/#enable-unsafe-webgpu`

## Så Kör Du Demon

### Alternativ 1: Lokal Server (Rekommenderas)

```cmd
# Navigate to the demo directory
cd Module08\samples\04\webgpu-demo

# Start a local server
python -m http.server 5173

# Open browser to http://localhost:5173
```

### Alternativ 2: VS Code Live Server

1. Installera "Live Server"-tillägget i VS Code
2. Högerklicka på `index.html` → "Open with Live Server"
3. Demon öppnas automatiskt i webbläsaren

## Vad Du Kommer Att Se

1. **WebGPU-detektering**: Kontrollerar webbläsarkompatibilitet
2. **Modellinladdning**: Hämtar och initierar MNIST-klassificeraren
3. **Inferensutförande**: Kör prediktion på exempeldata
4. **Prestandamätningar**: Visar laddningstid och inferenshastighet
5. **Resultatvisning**: Prediktionssäkerhet och råa utdata

## Förväntad Prestanda

| Utförandeleverantör | Modellinladdning | Inferens | Kommentarer |
|---------------------|------------------|----------|-------------|
| **WebGPU**          | ~2-5s           | ~10-50ms | Hårdvaruaccelererat |
| **CPU (WASM)**      | ~2-5s           | ~50-200ms | Programvarufallback |

## Felsökning

**WebGPU Inte Tillgängligt:**
- Uppdatera till Chrome/Edge 113+
- Aktivera WebGPU i `chrome://flags`
- Kontrollera att GPU-drivrutiner är aktuella
- Demon går automatiskt över till CPU

**Laddningsfel:**
- Kontrollera att du serverar via HTTP (inte file://)
- Kontrollera nätverksanslutningen för modellnedladdning
- Verifiera att CORS inte blockerar ONNX-modellen

**Prestandaproblem:**
- WebGPU ger betydande hastighetsförbättring jämfört med CPU
- Första körningen kan vara långsammare på grund av modellnedladdning
- Efterföljande körningar använder webbläsarens cache

## Integration med Foundry Local

Den här WebGPU-demon kompletterar Foundry Local genom att visa:

- **Klientbaserad inferens** för maximal integritet
- **Offline-funktioner** när internet inte är tillgängligt  
- **Edge-distribution** för resursbegränsade miljöer
- **Hybridarkitekturer** som kombinerar lokal och serverbaserad inferens

För produktionsapplikationer, överväg:
- Använd Foundry Local för serverbaserad inferens
- Använd WebGPU för klientbaserad för- och efterbearbetning
- Implementera intelligent routning mellan lokal och fjärrbaserad inferens

## Tekniska Detaljer

**Använd Modell:**
- MNIST-sifferklassificerare (ONNX-format)
- Input: 28x28 gråskalebilder
- Output: 10-klasser sannolikhetsfördelning
- Storlek: ~500KB (snabb nedladdning)

**ONNX Runtime Web:**
- WebGPU-utförandeleverantör för GPU-acceleration
- WASM-utförandeleverantör för CPU-fallback
- Automatisk optimering och grafoptimering

**Webbläsar-API:er:**
- WebGPU för hårdvaruåtkomst
- Web Workers för bakgrundsprocesser (framtida förbättring)
- WebAssembly för effektiv beräkning

## Nästa Steg

- Testa med egna ONNX-modeller
- Implementera riktig bilduppladdning och klassificering
- Lägg till strömningsinferens för större modeller
- Integrera med kamera/mikrofoningång

---


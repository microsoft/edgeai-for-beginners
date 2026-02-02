# Demo WebGPU + ONNX Runtime

Questo demo mostra come eseguire modelli di intelligenza artificiale direttamente nel browser utilizzando WebGPU per l'accelerazione hardware e ONNX Runtime Web.

## Cosa Dimostra

- **AI nel browser**: Esegui modelli interamente nel browser
- **Accelerazione WebGPU**: Inferenza accelerata dall'hardware quando disponibile
- **Privacy al primo posto**: Nessun dato lascia il tuo dispositivo
- **Zero installazione**: Funziona in qualsiasi browser compatibile
- **Fallback graduale**: Passa al CPU se WebGPU non è disponibile

## Requisiti

**Compatibilità del browser:**
- Chrome/Edge 113+ con WebGPU abilitato
- Controlla lo stato di WebGPU: `chrome://gpu`
- Abilita WebGPU: `chrome://flags/#enable-unsafe-webgpu`

## Esecuzione del Demo

### Opzione 1: Server Locale (Consigliata)

```cmd
# Navigate to the demo directory
cd Module08\samples\04\webgpu-demo

# Start a local server
python -m http.server 5173

# Open browser to http://localhost:5173
```

### Opzione 2: Live Server di VS Code

1. Installa l'estensione "Live Server" in VS Code
2. Clic destro su `index.html` → "Open with Live Server"
3. Il demo si apre automaticamente nel browser

## Cosa Vedrai

1. **Rilevamento WebGPU**: Controlla la compatibilità del browser
2. **Caricamento del modello**: Scarica e inizializza il classificatore MNIST
3. **Esecuzione dell'inferenza**: Esegue la previsione su dati di esempio
4. **Metriche di prestazione**: Mostra il tempo di caricamento e la velocità di inferenza
5. **Visualizzazione dei risultati**: Confidenza della previsione e output grezzi

## Prestazioni Attese

| Provider di Esecuzione | Caricamento Modello | Inferenza | Note |
|------------------------|---------------------|-----------|------|
| **WebGPU**             | ~2-5s              | ~10-50ms  | Accelerato dall'hardware |
| **CPU (WASM)**         | ~2-5s              | ~50-200ms | Fallback software |

## Risoluzione dei Problemi

**WebGPU Non Disponibile:**
- Aggiorna a Chrome/Edge 113+
- Abilita WebGPU in `chrome://flags`
- Controlla che i driver GPU siano aggiornati
- Il demo passerà automaticamente al CPU

**Errori di Caricamento:**
- Assicurati di servire tramite HTTP (non file://)
- Controlla la connessione di rete per il download del modello
- Verifica che CORS non stia bloccando il modello ONNX

**Problemi di Prestazioni:**
- WebGPU offre un notevole miglioramento rispetto al CPU
- La prima esecuzione potrebbe essere più lenta a causa del download del modello
- Le esecuzioni successive utilizzano la cache del browser

## Integrazione con Foundry Local

Questo demo WebGPU completa Foundry Local mostrando:

- **Inferenza lato client** per la massima privacy
- **Capacità offline** quando internet non è disponibile  
- **Distribuzione edge** per ambienti con risorse limitate
- **Architetture ibride** che combinano inferenza locale e server

Per applicazioni in produzione, considera:
- Usa Foundry Local per l'inferenza lato server
- Usa WebGPU per pre/post-elaborazione lato client
- Implementa un routing intelligente tra inferenza locale/remota

## Dettagli Tecnici

**Modello Utilizzato:**
- Classificatore di cifre MNIST (formato ONNX)
- Input: immagini in scala di grigi 28x28
- Output: distribuzione di probabilità a 10 classi
- Dimensione: ~500KB (download rapido)

**ONNX Runtime Web:**
- Provider di esecuzione WebGPU per accelerazione GPU
- Provider di esecuzione WASM per fallback CPU
- Ottimizzazione automatica e ottimizzazione del grafo

**API del Browser:**
- WebGPU per accesso hardware
- Web Workers per elaborazione in background (miglioramento futuro)
- WebAssembly per calcoli efficienti

## Prossimi Passi

- Prova con modelli ONNX personalizzati
- Implementa il caricamento e la classificazione di immagini reali
- Aggiungi inferenza in streaming per modelli più grandi
- Integra input da fotocamera/microfono

---


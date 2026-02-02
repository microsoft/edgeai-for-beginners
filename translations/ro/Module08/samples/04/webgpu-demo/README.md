# WebGPU + ONNX Runtime Demo

Acest demo arată cum să rulezi modele AI direct în browser folosind WebGPU pentru accelerare hardware și ONNX Runtime Web.

## Ce Demonstrează Acest Demo

- **AI în browser**: Rulează modele complet în browser
- **Accelerare WebGPU**: Inferență accelerată hardware, dacă este disponibilă
- **Confidențialitate**: Niciun fel de date nu părăsesc dispozitivul tău
- **Fără instalare**: Funcționează în orice browser compatibil
- **Fallback elegant**: Revine la CPU dacă WebGPU nu este disponibil

## Cerințe

**Compatibilitate Browser:**
- Chrome/Edge 113+ cu WebGPU activat
- Verifică statusul WebGPU: `chrome://gpu`
- Activează WebGPU: `chrome://flags/#enable-unsafe-webgpu`

## Rularea Demo-ului

### Opțiunea 1: Server Local (Recomandat)

```cmd
# Navigate to the demo directory
cd Module08\samples\04\webgpu-demo

# Start a local server
python -m http.server 5173

# Open browser to http://localhost:5173
```

### Opțiunea 2: VS Code Live Server

1. Instalează extensia "Live Server" în VS Code
2. Click dreapta pe `index.html` → "Open with Live Server"
3. Demo-ul se deschide automat în browser

## Ce Vei Observa

1. **Detectarea WebGPU**: Verifică compatibilitatea browserului
2. **Încărcarea Modelului**: Descarcă și inițializează clasificatorul MNIST
3. **Executarea Inferenței**: Rulează predicția pe date de probă
4. **Metrici de Performanță**: Afișează timpul de încărcare și viteza inferenței
5. **Afișarea Rezultatelor**: Încrederea predicției și rezultatele brute

## Performanța Așteptată

| Provider de Execuție | Încărcare Model | Inferență | Observații |
|-----------------------|----------------|-----------|------------|
| **WebGPU** | ~2-5s | ~10-50ms | Accelerare hardware |
| **CPU (WASM)** | ~2-5s | ~50-200ms | Fallback software |

## Depanare

**WebGPU Nu Este Disponibil:**
- Actualizează la Chrome/Edge 113+
- Activează WebGPU în `chrome://flags`
- Verifică dacă driverele GPU sunt actualizate
- Demo-ul va reveni automat la CPU

**Erori de Încărcare:**
- Asigură-te că servești prin HTTP (nu file://)
- Verifică conexiunea la rețea pentru descărcarea modelului
- Asigură-te că CORS nu blochează modelul ONNX

**Probleme de Performanță:**
- WebGPU oferă o accelerare semnificativă față de CPU
- Prima rulare poate fi mai lentă din cauza descărcării modelului
- Rulările ulterioare folosesc cache-ul browserului

## Integrare cu Foundry Local

Acest demo WebGPU completează Foundry Local prin demonstrarea:

- **Inferenței pe client** pentru confidențialitate maximă
- **Capacități offline** când internetul nu este disponibil  
- **Dezvoltare la margine** pentru medii cu resurse limitate
- **Arhitecturi hibride** care combină inferența locală și cea pe server

Pentru aplicații de producție, ia în considerare:
- Folosește Foundry Local pentru inferența pe server
- Folosește WebGPU pentru preprocesare/postprocesare pe client
- Implementează rutare inteligentă între inferența locală/remote

## Detalii Tehnice

**Model Utilizat:**
- Clasificator de cifre MNIST (format ONNX)
- Input: Imagini grayscale 28x28
- Output: Distribuție de probabilitate pe 10 clase
- Dimensiune: ~500KB (descărcare rapidă)

**ONNX Runtime Web:**
- Provider de execuție WebGPU pentru accelerare GPU
- Provider de execuție WASM pentru fallback CPU
- Optimizare automată și optimizare grafică

**API-uri Browser:**
- WebGPU pentru acces hardware
- Web Workers pentru procesare în fundal (îmbunătățire viitoare)
- WebAssembly pentru calcul eficient

## Pași Următori

- Testează cu modele ONNX personalizate
- Implementează încărcarea reală de imagini și clasificare
- Adaugă inferență streaming pentru modele mai mari
- Integrează input de la cameră/microfon

---


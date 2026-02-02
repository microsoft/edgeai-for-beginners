# WebGPU + ONNX Runtime Demo

Ovaj demo pokazuje kako pokrenuti AI modele direktno u pregledniku koristeći WebGPU za hardversku akceleraciju i ONNX Runtime Web.

## Što Ovo Demonstrira

- **AI u pregledniku**: Pokretanje modela u potpunosti u pregledniku
- **WebGPU Akceleracija**: Hardverski ubrzana inferencija kad je dostupna
- **Privatnost na prvom mjestu**: Podaci ne napuštaju vaš uređaj
- **Bez instalacije**: Radi u bilo kojem kompatibilnom pregledniku
- **Prilagodljivo fallback rješenje**: Prebacuje se na CPU ako WebGPU nije dostupan

## Zahtjevi

**Kompatibilnost preglednika:**
- Chrome/Edge 113+ s omogućenim WebGPU
- Provjerite status WebGPU: `chrome://gpu`
- Omogućite WebGPU: `chrome://flags/#enable-unsafe-webgpu`

## Pokretanje Dema

### Opcija 1: Lokalni Server (Preporučeno)

```cmd
# Navigate to the demo directory
cd Module08\samples\04\webgpu-demo

# Start a local server
python -m http.server 5173

# Open browser to http://localhost:5173
```

### Opcija 2: VS Code Live Server

1. Instalirajte ekstenziju "Live Server" u VS Code
2. Desni klik na `index.html` → "Open with Live Server"
3. Demo se automatski otvara u pregledniku

## Što Ćete Vidjeti

1. **Detekcija WebGPU**: Provjerava kompatibilnost preglednika
2. **Učitavanje Modela**: Preuzima i inicijalizira MNIST klasifikator
3. **Izvršavanje Inferencije**: Pokreće predikciju na uzorku podataka
4. **Metričke Performanse**: Prikazuje vrijeme učitavanja i brzinu inferencije
5. **Prikaz Rezultata**: Povjerenje u predikciju i sirovi izlazi

## Očekivane Performanse

| Izvršni Pružatelj | Učitavanje Modela | Inferencija | Napomene |
|-------------------|------------------|------------|----------|
| **WebGPU** | ~2-5s | ~10-50ms | Hardverski ubrzano |
| **CPU (WASM)** | ~2-5s | ~50-200ms | Softverski fallback |

## Rješavanje Problema

**WebGPU Nije Dostupan:**
- Ažurirajte na Chrome/Edge 113+
- Omogućite WebGPU u `chrome://flags`
- Provjerite jesu li GPU upravljački programi ažurirani
- Demo će se automatski prebaciti na CPU

**Greške pri Učitavanju:**
- Provjerite da koristite HTTP (ne file://)
- Provjerite mrežnu vezu za preuzimanje modela
- Provjerite da CORS ne blokira ONNX model

**Problemi s Performansama:**
- WebGPU pruža značajno ubrzanje u odnosu na CPU
- Prvo pokretanje može biti sporije zbog preuzimanja modela
- Naknadna pokretanja koriste predmemoriju preglednika

## Integracija s Foundry Local

Ovaj WebGPU demo nadopunjuje Foundry Local prikazujući:

- **Inferenciju na klijentskoj strani** za maksimalnu privatnost
- **Offline mogućnosti** kad internet nije dostupan  
- **Implementaciju na rubu** za okruženja s ograničenim resursima
- **Hibridne arhitekture** koje kombiniraju lokalnu i poslužiteljsku inferenciju

Za produkcijske aplikacije, razmotrite:
- Koristite Foundry Local za inferenciju na poslužitelju
- Koristite WebGPU za predobradu/postobradu na klijentskoj strani
- Implementirajte inteligentno usmjeravanje između lokalne i udaljene inferencije

## Tehnički Detalji

**Korišteni Model:**
- MNIST klasifikator znamenki (ONNX format)
- Ulaz: 28x28 slike u sivim tonovima
- Izlaz: Distribucija vjerojatnosti za 10 klasa
- Veličina: ~500KB (brzo preuzimanje)

**ONNX Runtime Web:**
- WebGPU izvršni pružatelj za GPU akceleraciju
- WASM izvršni pružatelj za CPU fallback
- Automatska optimizacija i optimizacija grafa

**API-ji Preglednika:**
- WebGPU za pristup hardveru
- Web Workers za obradu u pozadini (buduće poboljšanje)
- WebAssembly za učinkovito računanje

## Sljedeći Koraci

- Isprobajte s prilagođenim ONNX modelima
- Implementirajte stvarni upload slika i klasifikaciju
- Dodajte streaming inferenciju za veće modele
- Integrirajte unos s kamerom/mikrofonom

---


# WebGPU + ONNX Runtime Demo

Ta predstavitev prikazuje, kako zagnati AI modele neposredno v brskalniku z uporabo WebGPU za strojno pospeševanje in ONNX Runtime Web.

## Kaj prikazuje ta demo

- **AI v brskalniku**: Zagon modelov popolnoma v brskalniku
- **Pospeševanje z WebGPU**: Strojno pospešeno sklepanje, kadar je na voljo
- **Prvič zasebno**: Podatki ne zapustijo vaše naprave
- **Brez namestitve**: Deluje v katerem koli združljivem brskalniku
- **Prilagodljivo delovanje**: Preklopi na CPU, če WebGPU ni na voljo

## Zahteve

**Združljivost brskalnika:**
- Chrome/Edge 113+ z omogočenim WebGPU
- Preverite status WebGPU: `chrome://gpu`
- Omogočite WebGPU: `chrome://flags/#enable-unsafe-webgpu`

## Zagon predstavitve

### Možnost 1: Lokalni strežnik (priporočeno)

```cmd
# Navigate to the demo directory
cd Module08\samples\04\webgpu-demo

# Start a local server
python -m http.server 5173

# Open browser to http://localhost:5173
```

### Možnost 2: VS Code Live Server

1. Namestite razširitev "Live Server" v VS Code
2. Desni klik na `index.html` → "Open with Live Server"
3. Demo se samodejno odpre v brskalniku

## Kaj boste videli

1. **Preverjanje WebGPU**: Preveri združljivost brskalnika
2. **Nalaganje modela**: Prenese in inicializira MNIST klasifikator
3. **Izvajanje sklepanja**: Izvede napoved na vzorčnih podatkih
4. **Merjenje zmogljivosti**: Prikaže čas nalaganja in hitrost sklepanja
5. **Prikaz rezultatov**: Zaupanje napovedi in surovi izhodi

## Pričakovana zmogljivost

| Izvajalec sklepanja | Nalaganje modela | Sklepanje | Opombe |
|---------------------|------------------|-----------|--------|
| **WebGPU**          | ~2-5s           | ~10-50ms  | Strojno pospešeno |
| **CPU (WASM)**      | ~2-5s           | ~50-200ms | Programska rešitev |

## Odpravljanje težav

**WebGPU ni na voljo:**
- Posodobite na Chrome/Edge 113+
- Omogočite WebGPU v `chrome://flags`
- Preverite, ali so gonilniki GPU posodobljeni
- Demo se bo samodejno preklopil na CPU

**Napake pri nalaganju:**
- Prepričajte se, da strežnik deluje prek HTTP (ne file://)
- Preverite omrežno povezavo za prenos modela
- Preverite, ali CORS ne blokira ONNX modela

**Težave z zmogljivostjo:**
- WebGPU zagotavlja znatno pospešitev v primerjavi s CPU
- Prvi zagon je lahko počasnejši zaradi prenosa modela
- Naslednji zagoni uporabljajo predpomnilnik brskalnika

## Integracija s Foundry Local

Ta WebGPU demo dopolnjuje Foundry Local z naslednjim:

- **Sklepanje na strani odjemalca** za popolno zasebnost
- **Zmožnost delovanja brez povezave**, kadar internet ni na voljo  
- **Namestitev na robu** za okolja z omejenimi viri
- **Hibridne arhitekture**, ki združujejo lokalno in strežniško sklepanje

Za produkcijske aplikacije razmislite o:
- Uporabi Foundry Local za sklepanje na strežniku
- Uporabi WebGPU za predhodno/zaključno obdelavo na strani odjemalca
- Implementaciji inteligentnega usmerjanja med lokalnim/oddaljenim sklepanjem

## Tehnične podrobnosti

**Uporabljeni model:**
- MNIST klasifikator številk (ONNX format)
- Vhod: 28x28 slike v sivinah
- Izhod: 10-razredna porazdelitev verjetnosti
- Velikost: ~500KB (hitro nalaganje)

**ONNX Runtime Web:**
- Izvajalec WebGPU za pospeševanje z GPU
- Izvajalec WASM za preklop na CPU
- Samodejna optimizacija in optimizacija grafov

**API-ji brskalnika:**
- WebGPU za dostop do strojne opreme
- Web Workers za obdelavo v ozadju (prihodnja izboljšava)
- WebAssembly za učinkovito računanje

## Naslednji koraki

- Preizkusite z lastnimi ONNX modeli
- Implementirajte nalaganje in klasifikacijo pravih slik
- Dodajte pretočno sklepanje za večje modele
- Integrirajte vhod iz kamere/mikrofona

---


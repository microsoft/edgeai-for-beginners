# WebGPU + ONNX Runtime Demonstracija

Ši demonstracija parodo, kaip naršyklėje tiesiogiai vykdyti AI modelius naudojant WebGPU aparatūros spartinimui ir ONNX Runtime Web.

## Ką Tai Parodo

- **AI naršyklėje**: Modeliai vykdomi visiškai naršyklėje
- **WebGPU spartinimas**: Aparatūros spartinimas, kai įmanoma
- **Privatumas pirmiausia**: Duomenys nepalieka jūsų įrenginio
- **Be diegimo**: Veikia bet kurioje suderinamoje naršyklėje
- **Sklandus atsarginis režimas**: Pereina prie CPU, jei WebGPU nepasiekiamas

## Reikalavimai

**Naršyklės suderinamumas:**
- Chrome/Edge 113+ su įjungtu WebGPU
- Patikrinkite WebGPU būseną: `chrome://gpu`
- Įjunkite WebGPU: `chrome://flags/#enable-unsafe-webgpu`

## Demonstracijos Paleidimas

### 1 variantas: Vietinis serveris (Rekomenduojama)

```cmd
# Navigate to the demo directory
cd Module08\samples\04\webgpu-demo

# Start a local server
python -m http.server 5173

# Open browser to http://localhost:5173
```

### 2 variantas: VS Code Live Server

1. Įdiekite "Live Server" plėtinį VS Code
2. Dešiniuoju pelės mygtuku spustelėkite `index.html` → "Open with Live Server"
3. Demonstracija automatiškai atsidarys naršyklėje

## Ką Pamatysite

1. **WebGPU aptikimas**: Tikrina naršyklės suderinamumą
2. **Modelio įkėlimas**: Atsisiunčia ir inicijuoja MNIST klasifikatorių
3. **Prognozės vykdymas**: Atlieka prognozę su pavyzdiniais duomenimis
4. **Našumo rodikliai**: Rodo įkėlimo laiką ir prognozės greitį
5. **Rezultatų rodymas**: Prognozės pasitikėjimas ir neapdoroti rezultatai

## Tikėtinas Našumas

| Vykdymo teikėjas | Modelio įkėlimas | Prognozė | Pastabos |
|-------------------|------------------|----------|----------|
| **WebGPU** | ~2-5s | ~10-50ms | Aparatūros spartinimas |
| **CPU (WASM)** | ~2-5s | ~50-200ms | Programinės įrangos atsarginis režimas |

## Trikčių Šalinimas

**WebGPU nepasiekiamas:**
- Atnaujinkite į Chrome/Edge 113+
- Įjunkite WebGPU `chrome://flags`
- Patikrinkite, ar GPU tvarkyklės yra naujausios
- Demonstracija automatiškai pereis prie CPU

**Įkėlimo klaidos:**
- Įsitikinkite, kad naudojate HTTP (ne file://)
- Patikrinkite tinklo ryšį modelio atsisiuntimui
- Patikrinkite, ar CORS neblokuoja ONNX modelio

**Našumo problemos:**
- WebGPU suteikia reikšmingą greitėjimą, palyginti su CPU
- Pirmasis paleidimas gali būti lėtesnis dėl modelio atsisiuntimo
- Vėlesni paleidimai naudoja naršyklės talpyklą

## Integracija su Foundry Local

Ši WebGPU demonstracija papildo Foundry Local, parodydama:

- **Vietinį prognozavimą** maksimaliam privatumui
- **Darbo neprisijungus galimybes**, kai nėra interneto  
- **Edge diegimą** ribotų išteklių aplinkose
- **Hibridines architektūras**, derinančias vietinį ir serverio prognozavimą

Produkciniams pritaikymams apsvarstykite:
- Naudokite Foundry Local serverio prognozavimui
- Naudokite WebGPU klientinio apdorojimo/priešapdorojimo užduotims
- Įgyvendinkite išmanų maršrutizavimą tarp vietinio/nuotolinio prognozavimo

## Techninės Detalės

**Naudojamas Modelis:**
- MNIST skaitmenų klasifikatorius (ONNX formatas)
- Įvestis: 28x28 pilkos spalvos vaizdai
- Išvestis: 10 klasių tikimybių pasiskirstymas
- Dydis: ~500KB (greitas atsisiuntimas)

**ONNX Runtime Web:**
- WebGPU vykdymo teikėjas GPU spartinimui
- WASM vykdymo teikėjas CPU atsarginiam režimui
- Automatinė optimizacija ir grafų optimizavimas

**Naršyklės API:**
- WebGPU aparatūros prieigai
- Web Workers foniniam apdorojimui (ateities patobulinimas)
- WebAssembly efektyviam skaičiavimui

## Kiti Žingsniai

- Išbandykite su individualiais ONNX modeliais
- Įgyvendinkite realų vaizdų įkėlimą ir klasifikavimą
- Pridėkite srautinį prognozavimą didesniems modeliams
- Integruokite su kamera/mikrofono įvestimi

---


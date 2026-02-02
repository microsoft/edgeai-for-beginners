# WebGPU + ONNX Runtime Demo

See demo näitab, kuidas käivitada AI-mudeleid otse brauseris, kasutades WebGPU-d riistvarakiirenduseks ja ONNX Runtime Webi.

## Mida see demonstreerib

- **Brauseripõhine AI**: Käivita mudeleid täielikult brauseris
- **WebGPU kiirendus**: Riistvarakiirendusega järeldamine, kui saadaval
- **Privaatsus eelkõige**: Andmed ei lahku sinu seadmest
- **Paigaldusvaba**: Töötab igas ühilduvas brauseris
- **Sujuv tagasikäik**: Kasutab CPU-d, kui WebGPU pole saadaval

## Nõuded

**Brauseri ühilduvus:**
- Chrome/Edge 113+ koos lubatud WebGPU-ga
- Kontrolli WebGPU olekut: `chrome://gpu`
- Luba WebGPU: `chrome://flags/#enable-unsafe-webgpu`

## Demo käivitamine

### Valik 1: Kohalik server (soovitatav)

```cmd
# Navigate to the demo directory
cd Module08\samples\04\webgpu-demo

# Start a local server
python -m http.server 5173

# Open browser to http://localhost:5173
```

### Valik 2: VS Code Live Server

1. Paigalda VS Code'is "Live Server" laiendus
2. Paremklõps `index.html` → "Open with Live Server"
3. Demo avaneb automaatselt brauseris

## Mida näed

1. **WebGPU tuvastamine**: Kontrollib brauseri ühilduvust
2. **Mudelilaadimine**: Laadib ja initsialiseerib MNIST klassifikaatori
3. **Järelduse käivitamine**: Teeb prognoosi näidisandmetel
4. **Jõudlusmõõdikud**: Kuvab laadimisaja ja järelduskiiruse
5. **Tulemuste kuvamine**: Prognoosi kindlus ja toorandmed

## Oodatav jõudlus

| Käivitusteenus      | Mudeli laadimine | Järeldus   | Märkused              |
|---------------------|------------------|------------|-----------------------|
| **WebGPU**          | ~2-5s           | ~10-50ms   | Riistvarakiirendusega |
| **CPU (WASM)**      | ~2-5s           | ~50-200ms  | Tarkvaraline tagasikäik |

## Tõrkeotsing

**WebGPU pole saadaval:**
- Uuenda Chrome/Edge versioonile 113+
- Luba WebGPU `chrome://flags` kaudu
- Kontrolli, et GPU draiverid on ajakohased
- Demo lülitub automaatselt CPU-le

**Laadimisvead:**
- Veendu, et kasutad HTTP-d (mitte file://)
- Kontrolli võrguühendust mudeli allalaadimiseks
- Veendu, et CORS ei blokeeri ONNX mudelit

**Jõudlusprobleemid:**
- WebGPU pakub märkimisväärset kiirendust võrreldes CPU-ga
- Esimene käivitus võib olla aeglasem mudeli allalaadimise tõttu
- Järgmised käivitused kasutavad brauseri vahemälu

## Integreerimine Foundry Localiga

See WebGPU demo täiendab Foundry Locali, näidates:

- **Kliendipoolset järeldamist** maksimaalse privaatsuse tagamiseks
- **Võrguühenduseta võimalusi**, kui internet puudub  
- **Edge-juurutust** ressursipiirangutega keskkondades
- **Hübriidseid arhitektuure**, mis ühendavad kohaliku ja serveripoolse järeldamise

Tootmisrakenduste jaoks kaalu:
- Kasuta Foundry Locali serveripoolseks järeldamiseks
- Kasuta WebGPU-d kliendipoolseks eeltöötluseks/järelprotsessimiseks
- Rakenda intelligentne marsruutimine kohaliku/kaugjäreldamise vahel

## Tehnilised detailid

**Kasutatud mudel:**
- MNIST numbriklassifikaator (ONNX formaadis)
- Sisend: 28x28 halltoonides pildid
- Väljund: 10-klassi tõenäosusjaotus
- Suurus: ~500KB (kiire allalaadimine)

**ONNX Runtime Web:**
- WebGPU käivitusteenus GPU kiirenduseks
- WASM käivitusteenus CPU tagasikäiguks
- Automaatne optimeerimine ja graafi optimeerimine

**Brauseri API-d:**
- WebGPU riistvarale ligipääsuks
- Web Workers tausttöötluseks (tulevane täiendus)
- WebAssembly tõhusaks arvutamiseks

## Järgmised sammud

- Proovi kohandatud ONNX mudeleid
- Rakenda reaalne pildi üleslaadimine ja klassifitseerimine
- Lisa voogedastusjäreldus suurematele mudelitele
- Integreeri kaamera/mikrofoni sisendiga

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.
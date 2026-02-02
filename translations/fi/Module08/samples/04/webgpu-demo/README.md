# WebGPU + ONNX Runtime Demo

Tämä demo näyttää, kuinka AI-malleja voidaan ajaa suoraan selaimessa käyttämällä WebGPU:ta laitteiston kiihdytykseen ja ONNX Runtime Webiä.

## Mitä Tämä Demonstroi

- **Selaimeen perustuva AI**: Ajaa malleja kokonaan selaimessa
- **WebGPU-kiihdytys**: Laitteistokiihdytetty päättely, kun saatavilla
- **Tietosuoja etusijalla**: Data ei poistu laitteeltasi
- **Ei asennusta**: Toimii kaikissa yhteensopivissa selaimissa
- **Joustava varajärjestelmä**: Siirtyy CPU:lle, jos WebGPU ei ole käytettävissä

## Vaatimukset

**Selaimen yhteensopivuus:**
- Chrome/Edge 113+ WebGPU käytössä
- Tarkista WebGPU-tila: `chrome://gpu`
- Ota WebGPU käyttöön: `chrome://flags/#enable-unsafe-webgpu`

## Demon Käynnistäminen

### Vaihtoehto 1: Paikallinen palvelin (suositeltu)

```cmd
# Navigate to the demo directory
cd Module08\samples\04\webgpu-demo

# Start a local server
python -m http.server 5173

# Open browser to http://localhost:5173
```

### Vaihtoehto 2: VS Code Live Server

1. Asenna "Live Server" -laajennus VS Codeen
2. Napsauta hiiren oikealla `index.html` → "Open with Live Server"
3. Demo avautuu automaattisesti selaimessa

## Mitä Näet

1. **WebGPU-tunnistus**: Tarkistaa selaimen yhteensopivuuden
2. **Mallin lataus**: Lataa ja alustaa MNIST-luokittelijan
3. **Päättelyn suoritus**: Suorittaa ennusteen näyteaineistolla
4. **Suorituskykymittarit**: Näyttää latausajan ja päättelynopeuden
5. **Tulosten näyttö**: Ennusteen varmuus ja raakatulokset

## Odotettu Suorituskyky

| Suoritustapa | Mallin lataus | Päättely | Huomioita |
|--------------|---------------|----------|-----------|
| **WebGPU**   | ~2-5s         | ~10-50ms | Laitteistokiihdytetty |
| **CPU (WASM)** | ~2-5s       | ~50-200ms | Ohjelmistopohjainen varajärjestelmä |

## Vianmääritys

**WebGPU ei saatavilla:**
- Päivitä Chrome/Edge 113+ versioon
- Ota WebGPU käyttöön `chrome://flags`
- Tarkista, että GPU-ajurit ovat ajan tasalla
- Demo siirtyy automaattisesti CPU:lle

**Latausvirheet:**
- Varmista, että käytät HTTP:tä (ei file://)
- Tarkista verkkoyhteys mallin latausta varten
- Varmista, ettei CORS estä ONNX-mallia

**Suorituskykyongelmat:**
- WebGPU tarjoaa merkittävän nopeutuksen verrattuna CPU:hun
- Ensimmäinen ajo voi olla hitaampi mallin latauksen vuoksi
- Seuraavat ajot hyödyntävät selaimen välimuistia

## Integraatio Foundry Localin Kanssa

Tämä WebGPU-demo täydentää Foundry Localia näyttämällä:

- **Asiakaspään päättely** maksimaalisen tietosuojan takaamiseksi
- **Offline-ominaisuudet** ilman internetyhteyttä  
- **Reuna-alueiden käyttöönotto** resurssirajoitteisissa ympäristöissä
- **Hybridit arkkitehtuurit** yhdistäen paikallisen ja palvelinpäättelyn

Tuotantosovelluksia varten harkitse:
- Käytä Foundry Localia palvelinpäättelyyn
- Käytä WebGPU:ta asiakaspään esikäsittelyyn/jälkikäsittelyyn
- Toteuta älykäs reititys paikallisen ja etäpäätöksen välillä

## Teknisiä Yksityiskohtia

**Käytetty malli:**
- MNIST-numeroiden luokittelija (ONNX-muoto)
- Syöte: 28x28 harmaasävykuvat
- Tuloste: 10-luokan todennäköisyysjakauma
- Koko: ~500KB (nopea lataus)

**ONNX Runtime Web:**
- WebGPU-suoritustapa GPU-kiihdytykseen
- WASM-suoritustapa CPU-varajärjestelmään
- Automaattinen optimointi ja graafin optimointi

**Selaimen API:t:**
- WebGPU laitteistokäyttöön
- Web Workers taustaprosessointiin (tuleva parannus)
- WebAssembly tehokkaaseen laskentaan

## Seuraavat Askeleet

- Kokeile omilla ONNX-malleilla
- Toteuta oikea kuvan lataus ja luokittelu
- Lisää suoratoistopäättely suuremmille malleille
- Integroi kameran/mikrofonin syötteeseen

---


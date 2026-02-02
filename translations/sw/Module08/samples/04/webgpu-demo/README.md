# WebGPU + ONNX Runtime Demo

Demo hii inaonyesha jinsi ya kuendesha mifano ya AI moja kwa moja kwenye kivinjari kwa kutumia WebGPU kwa kasi ya vifaa na ONNX Runtime Web.

## Kile Kinachoonyeshwa

- **AI kwenye Kivinjari**: Endesha mifano moja kwa moja kwenye kivinjari
- **WebGPU Kasi**: Utoaji wa matokeo kwa kasi ya vifaa pale inapopatikana
- **Faragha Kwanza**: Hakuna data inayotoka kwenye kifaa chako
- **Hakuna Usakinishaji**: Inafanya kazi kwenye kivinjari chochote kinachofaa
- **Urejeo wa Kawaida**: Inarudi kwa CPU ikiwa WebGPU haipatikani

## Mahitaji

**Ulinganifu wa Kivinjari:**
- Chrome/Edge 113+ na WebGPU imewezeshwa
- Angalia hali ya WebGPU: `chrome://gpu`
- Wezesha WebGPU: `chrome://flags/#enable-unsafe-webgpu`

## Kuendesha Demo

### Chaguo 1: Seva ya Ndani (Inapendekezwa)

```cmd
# Navigate to the demo directory
cd Module08\samples\04\webgpu-demo

# Start a local server
python -m http.server 5173

# Open browser to http://localhost:5173
```

### Chaguo 2: Seva ya Moja kwa Moja ya VS Code

1. Sakinisha kiendelezi cha "Live Server" kwenye VS Code
2. Bofya kulia `index.html` → "Open with Live Server"
3. Demo itafunguka moja kwa moja kwenye kivinjari

## Kile Utakachokiona

1. **Uchunguzi wa WebGPU**: Hukagua ulinganifu wa kivinjari
2. **Upakiaji wa Mfano**: Inapakua na kuanzisha MNIST classifier
3. **Utekelezaji wa Utoaji Matokeo**: Inafanya utabiri kwenye data ya sampuli
4. **Vipimo vya Utendaji**: Inaonyesha muda wa upakiaji na kasi ya utoaji matokeo
5. **Onyesho la Matokeo**: Uhakika wa utabiri na matokeo ghafi

## Utendaji Unaotarajiwa

| Mtoa Huduma wa Utekelezaji | Upakiaji wa Mfano | Utoaji Matokeo | Maelezo |
|-------------------|------------|-----------|-------|
| **WebGPU** | ~2-5s | ~10-50ms | Kasi ya vifaa |
| **CPU (WASM)** | ~2-5s | ~50-200ms | Urejeo wa programu |

## Kutatua Changamoto

**WebGPU Haipatikani:**
- Sasisha hadi Chrome/Edge 113+
- Wezesha WebGPU kwenye `chrome://flags`
- Hakikisha madereva ya GPU yako yamesasishwa
- Demo itarudi kwa CPU moja kwa moja

**Hitilafu za Upakiaji:**
- Hakikisha unatumia HTTP (sio file://)
- Angalia muunganisho wa mtandao kwa upakuaji wa mfano
- Hakikisha CORS haizuii mfano wa ONNX

**Masuala ya Utendaji:**
- WebGPU inatoa kasi kubwa ikilinganishwa na CPU
- Kwanza inaweza kuwa polepole kwa sababu ya upakuaji wa mfano
- Uendeshaji wa baadaye hutumia akiba ya kivinjari

## Muunganisho na Foundry Local

Demo hii ya WebGPU inakamilisha Foundry Local kwa kuonyesha:

- **Utoaji matokeo upande wa mteja** kwa faragha ya hali ya juu
- **Uwezo wa nje ya mtandao** wakati mtandao haupatikani  
- **Upelekaji wa ukingoni** kwa mazingira yenye rasilimali chache
- **Miundombinu mseto** inayochanganya utoaji matokeo wa ndani na wa seva

Kwa matumizi ya uzalishaji, zingatia:
- Tumia Foundry Local kwa utoaji matokeo wa upande wa seva
- Tumia WebGPU kwa usindikaji wa awali/baada ya usindikaji upande wa mteja
- Tekeleza njia ya akili kati ya utoaji matokeo wa ndani/kutoka kwa seva

## Maelezo ya Kiufundi

**Mfano Unaotumika:**
- MNIST classifier ya namba (muundo wa ONNX)
- Ingizo: Picha za kijivu za 28x28
- Matokeo: Usambazaji wa uwezekano wa darasa 10
- Ukubwa: ~500KB (upakuaji wa haraka)

**ONNX Runtime Web:**
- Mtoa huduma wa utekelezaji wa WebGPU kwa kasi ya GPU
- Mtoa huduma wa utekelezaji wa WASM kwa urejeo wa CPU
- Uboreshaji wa kiotomatiki na uboreshaji wa grafu

**API za Kivinjari:**
- WebGPU kwa ufikiaji wa vifaa
- Web Workers kwa usindikaji wa nyuma (uboreshaji wa baadaye)
- WebAssembly kwa hesabu yenye ufanisi

## Hatua Zifuatazo

- Jaribu na mifano ya ONNX ya kawaida
- Tekeleza upakiaji wa picha halisi na uainishaji
- Ongeza utoaji matokeo wa mtiririko kwa mifano mikubwa
- Unganisha na ingizo la kamera/mikrofoni

---


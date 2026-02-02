# WebGPU + ONNX Runtime Demo

Ang demo na ito ay nagpapakita kung paano patakbuhin ang mga AI model nang direkta sa browser gamit ang WebGPU para sa hardware acceleration at ONNX Runtime Web.

## Ano ang Ipinapakita Nito

- **AI sa Browser**: Patakbuhin ang mga model nang buo sa browser
- **WebGPU Acceleration**: Pinabilis na inference gamit ang hardware kapag available
- **Pribado**: Walang data na lumalabas sa iyong device
- **Walang Installasyon**: Gumagana sa anumang compatible na browser
- **Maayos na Paglipat**: Awtomatikong lilipat sa CPU kung hindi available ang WebGPU

## Mga Kinakailangan

**Compatibility ng Browser:**
- Chrome/Edge 113+ na may WebGPU na naka-enable
- Tingnan ang status ng WebGPU: `chrome://gpu`
- I-enable ang WebGPU: `chrome://flags/#enable-unsafe-webgpu`

## Paano Patakbuhin ang Demo

### Opsyon 1: Lokal na Server (Inirerekomenda)

```cmd
# Navigate to the demo directory
cd Module08\samples\04\webgpu-demo

# Start a local server
python -m http.server 5173

# Open browser to http://localhost:5173
```

### Opsyon 2: VS Code Live Server

1. I-install ang "Live Server" extension sa VS Code
2. I-right-click ang `index.html` → "Open with Live Server"
3. Awtomatikong magbubukas ang demo sa browser

## Ano ang Makikita Mo

1. **Pag-detect ng WebGPU**: Sinusuri ang compatibility ng browser
2. **Pag-load ng Model**: Dina-download at ini-initialize ang MNIST classifier
3. **Pagpapatakbo ng Inference**: Gumagawa ng prediction gamit ang sample data
4. **Mga Sukatan ng Performance**: Ipinapakita ang oras ng pag-load at bilis ng inference
5. **Pagpapakita ng Resulta**: Confidence ng prediction at raw outputs

## Inaasahang Performance

| Execution Provider | Pag-load ng Model | Inference | Mga Tala |
|-------------------|------------------|-----------|----------|
| **WebGPU** | ~2-5s | ~10-50ms | Pinabilis ng hardware |
| **CPU (WASM)** | ~2-5s | ~50-200ms | Software fallback |

## Pag-aayos ng Problema

**Hindi Available ang WebGPU:**
- Mag-update sa Chrome/Edge 113+
- I-enable ang WebGPU sa `chrome://flags`
- Siguraduhing updated ang GPU drivers
- Awtomatikong lilipat ang demo sa CPU

**Mga Error sa Pag-load:**
- Siguraduhing nagsisilbi ka gamit ang HTTP (hindi file://)
- Suriin ang koneksyon sa network para sa pag-download ng model
- Siguraduhing hindi hinaharang ng CORS ang ONNX model

**Mga Isyu sa Performance:**
- Malaki ang bilis na ibinibigay ng WebGPU kumpara sa CPU
- Maaaring mas mabagal ang unang run dahil sa pag-download ng model
- Ang mga susunod na run ay gagamit ng browser cache

## Integrasyon sa Foundry Local

Ang WebGPU demo na ito ay umaakma sa Foundry Local sa pamamagitan ng pagpapakita ng:

- **Inference sa client-side** para sa ultimate privacy
- **Offline capabilities** kapag walang internet  
- **Deployment sa edge** para sa mga environment na may limitadong resources
- **Hybrid architectures** na pinagsasama ang local at server inference

Para sa mga production application, isaalang-alang:
- Gamitin ang Foundry Local para sa server-side inference
- Gamitin ang WebGPU para sa preprocessing/postprocessing sa client-side
- Magpatupad ng intelligent routing sa pagitan ng local/remote inference

## Mga Teknikal na Detalye

**Model na Ginamit:**
- MNIST digit classifier (ONNX format)
- Input: 28x28 grayscale images
- Output: 10-class probability distribution
- Laki: ~500KB (mabilis i-download)

**ONNX Runtime Web:**
- WebGPU execution provider para sa GPU acceleration
- WASM execution provider para sa CPU fallback
- Awtomatikong optimization at graph optimization

**Mga Browser API:**
- WebGPU para sa hardware access
- Web Workers para sa background processing (sa hinaharap)
- WebAssembly para sa efficient computation

## Mga Susunod na Hakbang

- Subukan gamit ang custom ONNX models
- Magpatupad ng real image upload at classification
- Magdagdag ng streaming inference para sa mas malalaking model
- Isama ang input mula sa camera/microphone

---


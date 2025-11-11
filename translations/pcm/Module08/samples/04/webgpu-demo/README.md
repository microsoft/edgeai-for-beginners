<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7a474b8e201d5316c0095cdbc3bf0555",
  "translation_date": "2025-11-11T18:03:13+00:00",
  "source_file": "Module08/samples/04/webgpu-demo/README.md",
  "language_code": "pcm"
}
-->
# WebGPU + ONNX Runtime Demo

Dis demo dey show how pesin fit run AI models directly for browser using WebGPU for hardware acceleration and ONNX Runtime Web.

## Wetin Dis Demo Go Show

- **AI wey dey run for browser**: Run models completely for inside browser
- **WebGPU Acceleration**: Hardware-accelerated inference if e dey available
- **Privacy-first**: Your data no go comot from your device
- **No need to install anything**: E go work for any browser wey fit support am
- **Backup plan**: If WebGPU no dey, e go use CPU instead

## Wetin You Need

**Browser wey fit work:**
- Chrome/Edge 113+ wey get WebGPU enabled
- Check WebGPU status: `chrome://gpu`
- Enable WebGPU: `chrome://flags/#enable-unsafe-webgpu`

## How to Run Dis Demo

### Option 1: Local Server (We recommend dis one)

```cmd
# Navigate to the demo directory
cd Module08\samples\04\webgpu-demo

# Start a local server
python -m http.server 5173

# Open browser to http://localhost:5173
```

### Option 2: VS Code Live Server

1. Install "Live Server" extension for VS Code
2. Right-click `index.html` → "Open with Live Server"
3. Demo go open automatically for browser

## Wetin You Go See

1. **WebGPU Detection**: E go check if your browser fit work
2. **Model Loading**: E go download and setup MNIST classifier
3. **Inference Execution**: E go run prediction for sample data
4. **Performance Metrics**: E go show load time and inference speed
5. **Results Display**: E go show prediction confidence and raw outputs

## Wetin You Fit Expect for Performance

| Execution Provider | Model Load | Inference | Notes |
|-------------------|------------|-----------|-------|
| **WebGPU** | ~2-5s | ~10-50ms | Hardware acceleration dey |
| **CPU (WASM)** | ~2-5s | ~50-200ms | E dey fallback to software |

## If Problem Happen

**WebGPU No Dey Available:**
- Update your Chrome/Edge to 113+ version
- Enable WebGPU for `chrome://flags`
- Make sure say your GPU drivers dey up-to-date
- If WebGPU no dey, demo go automatically use CPU

**Loading Errors:**
- Make sure say you dey serve am through HTTP (no be file://)
- Check your network connection to download model
- Confirm say CORS no dey block ONNX model

**Performance Wahala:**
- WebGPU dey make am faster pass CPU
- First time wey you go run am fit slow because e dey download model
- Next time wey you run am, e go use browser cache

## How E Fit Work with Foundry Local

Dis WebGPU demo dey work well with Foundry Local because e show:

- **Inference wey dey client-side** for better privacy
- **Offline use** if internet no dey  
- **Edge deployment** for places wey no get plenty resources
- **Hybrid system** wey dey mix local and server inference

For production use, you fit try:
- Use Foundry Local for server-side inference
- Use WebGPU for client-side preprocessing/postprocessing
- Add smart way to choose between local/remote inference

## Technical Details

**Model We Dey Use:**
- MNIST digit classifier (ONNX format)
- Input: 28x28 grayscale images
- Output: 10-class probability distribution
- Size: ~500KB (e dey download quick)

**ONNX Runtime Web:**
- WebGPU execution provider for GPU acceleration
- WASM execution provider for CPU fallback
- E dey do automatic optimization and graph optimization

**Browser APIs:**
- WebGPU for hardware access
- Web Workers for background processing (we go add dis one later)
- WebAssembly for better computation

## Wetin You Fit Do Next

- Try am with your own ONNX models
- Add real image upload and classification
- Add streaming inference for bigger models
- Connect am with camera/microphone input

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis dokyument don use AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator) do di translation. Even as we dey try make am accurate, abeg sabi say automated translations fit get mistake or no dey correct well. Di original dokyument for im native language na di main source wey you go trust. For important information, e good make professional human translation dey use. We no go fit take blame for any misunderstanding or wrong interpretation wey fit happen because you use dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
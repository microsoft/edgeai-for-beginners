# WebGPU + ONNX Runtime Demo

This demo showcases how to run AI models directly in the browser using WebGPU for hardware acceleration and ONNX Runtime Web.

## What This Demonstrates

- **AI in the Browser**: Execute models entirely within the browser
- **WebGPU Acceleration**: Utilize hardware acceleration when supported
- **Privacy-Focused**: No data leaves your device
- **No Installation Needed**: Works in any compatible browser
- **Fallback Mechanism**: Defaults to CPU if WebGPU is unavailable

## Requirements

**Browser Compatibility:**
- Chrome/Edge 113+ with WebGPU enabled
- Check WebGPU status: `chrome://gpu`
- Enable WebGPU: `chrome://flags/#enable-unsafe-webgpu`

## Running the Demo

### Option 1: Local Server (Recommended)

```cmd
# Navigate to the demo directory
cd Module08\samples\04\webgpu-demo

# Start a local server
python -m http.server 5173

# Open browser to http://localhost:5173
```

### Option 2: VS Code Live Server

1. Install the "Live Server" extension in VS Code
2. Right-click `index.html` → Select "Open with Live Server"
3. The demo will automatically open in your browser

## What You'll See

1. **WebGPU Detection**: Verifies browser compatibility
2. **Model Loading**: Downloads and initializes the MNIST classifier
3. **Inference Execution**: Runs predictions on sample data
4. **Performance Metrics**: Displays load time and inference speed
5. **Results Display**: Shows prediction confidence and raw outputs

## Expected Performance

| Execution Provider | Model Load | Inference | Notes |
|-------------------|------------|-----------|-------|
| **WebGPU** | ~2-5s | ~10-50ms | Hardware accelerated |
| **CPU (WASM)** | ~2-5s | ~50-200ms | Software fallback |

## Troubleshooting

**WebGPU Not Available:**
- Update to Chrome/Edge 113+
- Enable WebGPU in `chrome://flags`
- Ensure GPU drivers are up to date
- The demo will automatically fallback to CPU

**Loading Errors:**
- Make sure you're serving the demo via HTTP (not file://)
- Verify your network connection for model downloads
- Check that CORS isn't blocking the ONNX model

**Performance Issues:**
- WebGPU offers significant speed improvements over CPU
- The first run may be slower due to model download
- Subsequent runs will use the browser cache

## Integration with Foundry Local

This WebGPU demo complements Foundry Local by demonstrating:

- **Client-side inference** for maximum privacy
- **Offline functionality** when no internet is available  
- **Edge deployment** for environments with limited resources
- **Hybrid architectures** combining local and server inference

For production use cases, consider:
- Using Foundry Local for server-side inference
- Leveraging WebGPU for client-side preprocessing/postprocessing
- Implementing smart routing between local and remote inference

## Technical Details

**Model Used:**
- MNIST digit classifier (ONNX format)
- Input: 28x28 grayscale images
- Output: 10-class probability distribution
- Size: ~500KB (quick download)

**ONNX Runtime Web:**
- WebGPU execution provider for GPU acceleration
- WASM execution provider for CPU fallback
- Automatic optimization and graph enhancements

**Browser APIs:**
- WebGPU for hardware access
- Web Workers for background processing (future feature)
- WebAssembly for efficient computation

## Next Steps

- Experiment with custom ONNX models
- Add functionality for real image uploads and classification
- Implement streaming inference for larger models
- Integrate with camera or microphone input

---


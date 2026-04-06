# WebGPU + ONNX Runtime ដេម៉ូ

This demo shows how to run AI models directly in the browser using WebGPU for hardware acceleration and ONNX Runtime Web.

## What This Demonstrates

- **Browser-based AI**: Run models entirely in the browser
- **WebGPU Acceleration**: Hardware-accelerated inference when available
- **Privacy-first**: No data leaves your device
- **Zero Install**: Works in any compatible browser
- **Graceful Fallback**: Falls back to CPU if WebGPU unavailable

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

1. Install "Live Server" extension in VS Code
2. Right-click `index.html` → "Open with Live Server"
3. Demo opens automatically in browser

## What You'll See

1. **WebGPU Detection**: Checks browser compatibility
2. **Model Loading**: Downloads and initializes MNIST classifier
3. **Inference Execution**: Runs prediction on sample data
4. **Performance Metrics**: Shows load time and inference speed
5. **Results Display**: Prediction confidence and raw outputs

## Expected Performance

| Execution Provider | Model Load | Inference | Notes |
|-------------------|------------|-----------|-------|
| **WebGPU** | ~2-5s | ~10-50ms | Hardware accelerated |
| **CPU (WASM)** | ~2-5s | ~50-200ms | Software fallback |

## Troubleshooting

**WebGPU Not Available:**
- Update to Chrome/Edge 113+
- Enable WebGPU in `chrome://flags`
- Check GPU drivers are current
- Demo will fallback to CPU automatically

**Loading Errors:**
- Ensure you're serving via HTTP (not file://)
- Check network connection for model download
- Verify CORS isn't blocking the ONNX model

**Performance Issues:**
- WebGPU provides significant speedup over CPU
- First run may be slower due to model download
- Subsequent runs use browser cache

## Integration with Foundry Local

This WebGPU demo complements Foundry Local by showing:

- **Client-side inference** for ultimate privacy
- **Offline capabilities** when internet unavailable  
- **Edge deployment** for resource-constrained environments
- **Hybrid architectures** combining local and server inference

For production applications, consider:
- Use Foundry Local for server-side inference
- Use WebGPU for client-side preprocessing/postprocessing
- Implement intelligent routing between local/remote inference

## Technical Details

**Model Used:**
- MNIST digit classifier (ONNX format)
- Input: 28x28 grayscale images
- Output: 10-class probability distribution
- Size: ~500KB (quick download)

**ONNX Runtime Web:**
- WebGPU execution provider for GPU acceleration
- WASM execution provider for CPU fallback
- Automatic optimization and graph optimization

**Browser APIs:**
- WebGPU for hardware access
- Web Workers for background processing (future enhancement)
- WebAssembly for efficient computation

## Next Steps

- Try with custom ONNX models
- Implement real image upload and classification
- Add streaming inference for larger models
- Integrate with camera/microphone input

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
ឯកសារ​នេះ​ត្រូវ​បាន​បកប្រែ​ដោយ​ប្រើ​សេវាកម្ម​បកប្រែ AI [Co-op Translator](https://github.com/Azure/co-op-translator). ទោះ​យើង​ព្យាយាម​សម្រាប់​ការ​ត្រឹមត្រូវ សូម​យកចិត្តទុកដាក់​ថា​ការ​បកប្រែ​ដោយ​អូតូម៉ាទឺរ​អាច​មានកំហុស ឬភាព​មិន​ត្រឹមត្រូវ។ ឯកសារ​ដើម​ក្នុង​ភាសា​ដើម គួរត្រូវបាន​ចាត់ទុក​ជា​ប្រភព​ដែល​ទុកចិត្តបាន។ សម្រាប់​ព័ត៌មាន​ដែល​សំខាន់ យើង​ស្នើឲ្យ​អ្នក​ប្រើ​បកប្រែ​ដោយ​មនុស្ស​ដែលមានវិជ្ជាជីវៈ។ យើង​មិន​ទទួលខុសត្រូវ​ចំពោះ​ការ​យល់ច្រឡំ ឬ​ការ​បកស្រាយ​ខុស​ដែល​កើត​ឡើង​ពី​ការ​ប្រើ​ប្រាស់​ការ​បកប្រែ​នេះទេ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
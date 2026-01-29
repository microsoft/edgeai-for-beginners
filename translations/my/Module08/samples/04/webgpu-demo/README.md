# WebGPU + ONNX Runtime Demo

ဒီ demo က WebGPU ကို hardware acceleration အတွက် အသုံးပြုပြီး ONNX Runtime Web ကို သုံးကာ AI မော်ဒယ်တွေကို browser ထဲမှာ တိုက်ရိုက် run လုပ်ပေးနိုင်တဲ့ နည်းလမ်းကို ပြသထားပါတယ်။

## ဒီမှာ ပြသထားတာတွေ

- **Browser-based AI**: မော်ဒယ်တွေကို browser ထဲမှာပဲ run လုပ်နိုင်ခြင်း
- **WebGPU Acceleration**: Hardware acceleration ရရှိနိုင်တဲ့အခါမှာ inference ကို မြန်ဆန်စေခြင်း
- **Privacy-first**: သင့် device ကနေ data ထွက်မသွားခြင်း
- **Zero Install**: Compatible ဖြစ်တဲ့ browser တစ်ခုမှာ အလုပ်လုပ်နိုင်ခြင်း
- **Graceful Fallback**: WebGPU မရရှိနိုင်တဲ့အခါ CPU ကို fallback လုပ်ခြင်း

## လိုအပ်ချက်များ

**Browser Compatibility:**
- WebGPU enabled Chrome/Edge 113+ 
- WebGPU status ကို စစ်ဆေးရန်: `chrome://gpu`
- WebGPU ကို enable လုပ်ရန်: `chrome://flags/#enable-unsafe-webgpu`

## Demo ကို Run လုပ်ခြင်း

### Option 1: Local Server (အကြံပြုထားသောနည်းလမ်း)

```cmd
# Navigate to the demo directory
cd Module08\samples\04\webgpu-demo

# Start a local server
python -m http.server 5173

# Open browser to http://localhost:5173
```

### Option 2: VS Code Live Server

1. VS Code မှာ "Live Server" extension ကို install လုပ်ပါ
2. `index.html` ကို Right-click → "Open with Live Server" ကို ရွေးပါ
3. Demo ကို browser မှာ အလိုအလျောက် ဖွင့်ပေးပါမည်

## သင်မြင်ရမည့်အရာများ

1. **WebGPU Detection**: Browser compatibility ကို စစ်ဆေးခြင်း
2. **Model Loading**: MNIST classifier ကို download လုပ်ပြီး initialize လုပ်ခြင်း
3. **Inference Execution**: Sample data ပေါ်မှာ prediction run လုပ်ခြင်း
4. **Performance Metrics**: Load time နဲ့ inference speed ကို ပြသခြင်း
5. **Results Display**: Prediction confidence နဲ့ raw outputs ကို ပြသခြင်း

## မျှော်လင့်ရမည့် Performance

| Execution Provider | Model Load | Inference | Notes |
|-------------------|------------|-----------|-------|
| **WebGPU** | ~2-5s | ~10-50ms | Hardware accelerated |
| **CPU (WASM)** | ~2-5s | ~50-200ms | Software fallback |

## ပြဿနာများကို ဖြေရှင်းခြင်း

**WebGPU မရရှိနိုင်ပါက:**
- Chrome/Edge 113+ ကို update လုပ်ပါ
- `chrome://flags` မှာ WebGPU ကို enable လုပ်ပါ
- GPU drivers ကို အပ်ဒိတ်ထားပါ
- Demo က CPU ကို အလိုအလျောက် fallback လုပ်ပါမည်

**Loading Errors:**
- HTTP မှတဆင့် serve လုပ်နေကြောင်း သေချာပါ (file:// မဟုတ်)
- Model download အတွက် network connection ကို စစ်ဆေးပါ
- ONNX model ကို CORS မပိတ်ထားကြောင်း သေချာပါ

**Performance Issues:**
- WebGPU က CPU ထက် အလွန်မြန်ဆန်စေပါသည်
- ပထမဆုံး run လုပ်တဲ့အခါ model download ကြောင့် အနည်းငယ်နှေးနိုင်ပါသည်
- နောက် run တွေမှာ browser cache ကို အသုံးပြုမည်ဖြစ်သည်

## Foundry Local နှင့် ပေါင်းစပ်ခြင်း

ဒီ WebGPU demo က Foundry Local ကို အောက်ပါအတိုင်း အထောက်အကူပြုသည်-

- **Client-side inference** ကို privacy အမြင့်ဆုံးအနေဖြင့် ပြုလုပ်ခြင်း
- **Offline capabilities** ကို အင်တာနက်မရှိတဲ့အခါ အသုံးပြုနိုင်ခြင်း  
- **Edge deployment** ကို resource အနည်းငယ်သာလိုအပ်တဲ့ ပတ်ဝန်းကျင်များအတွက် အသုံးပြုခြင်း
- **Hybrid architectures** ကို local နဲ့ server inference ပေါင်းစပ်အသုံးပြုခြင်း

Production application များအတွက် အကြံပြုချက်များ:
- Server-side inference အတွက် Foundry Local ကို အသုံးပြုပါ
- Client-side preprocessing/postprocessing အတွက် WebGPU ကို အသုံးပြုပါ
- Local/remote inference အကြား intelligent routing ကို implement လုပ်ပါ

## Technical Details

**အသုံးပြုထားသော Model:**
- MNIST digit classifier (ONNX format)
- Input: 28x28 grayscale images
- Output: 10-class probability distribution
- Size: ~500KB (download မြန်ဆန်)

**ONNX Runtime Web:**
- GPU acceleration အတွက် WebGPU execution provider
- CPU fallback အတွက် WASM execution provider
- Automatic optimization နဲ့ graph optimization

**Browser APIs:**
- Hardware access အတွက် WebGPU
- Background processing အတွက် Web Workers (အနာဂတ် enhancement)
- Efficient computation အတွက် WebAssembly

## နောက်ထပ်အဆင့်များ

- Custom ONNX models တွေကို စမ်းသုံးပါ
- အမှန်တကယ် image upload နဲ့ classification ကို implement လုပ်ပါ
- Model အကြီးများအတွက် streaming inference ကို ထည့်သွင်းပါ
- Camera/microphone input နဲ့ ပေါင်းစပ်ပါ

---


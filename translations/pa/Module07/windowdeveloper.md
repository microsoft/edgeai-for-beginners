# Windows Edge AI ਵਿਕਾਸ ਗਾਈਡ

## ਪਰਿਚਯ

Windows Edge AI ਵਿਕਾਸ ਵਿੱਚ ਤੁਹਾਡਾ ਸਵਾਗਤ ਹੈ - ਇਹ Microsoft ਦੇ Windows AI Foundry ਪਲੇਟਫਾਰਮ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਡਿਵਾਈਸ-ਅਧਾਰਿਤ AI ਦੀ ਤਾਕਤ ਨੂੰ ਵਰਤਣ ਵਾਲੇ ਬੁੱਧੀਮਾਨ ਐਪਲੀਕੇਸ਼ਨ ਬਣਾਉਣ ਲਈ ਤੁਹਾਡੀ ਵਿਸਤ੍ਰਿਤ ਗਾਈਡ ਹੈ। ਇਹ ਗਾਈਡ ਖਾਸ ਤੌਰ 'ਤੇ Windows ਡਿਵੈਲਪਰਾਂ ਲਈ ਤਿਆਰ ਕੀਤੀ ਗਈ ਹੈ ਜੋ ਆਪਣੇ ਐਪਲੀਕੇਸ਼ਨਾਂ ਵਿੱਚ ਅਗੇਤਮ Edge AI ਸਮਰੱਥਾਵਾਂ ਨੂੰ ਸ਼ਾਮਲ ਕਰਨਾ ਚਾਹੁੰਦੇ ਹਨ, ਜਦੋਂ ਕਿ Windows ਹਾਰਡਵੇਅਰ ਐਕਸਲੇਰੇਸ਼ਨ ਦੇ ਪੂਰੇ ਸਪੈਕਟ੍ਰਮ ਦਾ ਲਾਭ ਲੈ ਰਹੇ ਹਨ।

### Windows AI ਦਾ ਫਾਇਦਾ

Windows AI Foundry ਇੱਕ ਇਕਜੁਟ, ਭਰੋਸੇਯੋਗ ਅਤੇ ਸੁਰੱਖਿਅਤ ਪਲੇਟਫਾਰਮ ਦਾ ਪ੍ਰਤੀਨਿਧਿਤਾ ਕਰਦਾ ਹੈ ਜੋ AI ਡਿਵੈਲਪਰ ਲਾਈਫਸਾਈਕਲ ਦੇ ਪੂਰੇ ਚੱਕਰ ਦਾ ਸਮਰਥਨ ਕਰਦਾ ਹੈ - ਮਾਡਲ ਚੋਣ ਅਤੇ ਫਾਈਨ-ਟਿਊਨਿੰਗ ਤੋਂ ਲੈ ਕੇ CPU, GPU, NPU ਅਤੇ ਹਾਈਬ੍ਰਿਡ ਕਲਾਉਡ ਆਰਕੀਟੈਕਚਰ ਵਿੱਚ ਓਪਟੀਮਾਈਜ਼ੇਸ਼ਨ ਅਤੇ ਡਿਪਲੌਇਮੈਂਟ ਤੱਕ। ਇਹ ਪਲੇਟਫਾਰਮ AI ਵਿਕਾਸ ਨੂੰ ਲੋਕਤੰਤਰਤ ਕਰਦਾ ਹੈ:

- **ਹਾਰਡਵੇਅਰ ਅਬਸਟਰੈਕਸ਼ਨ**: AMD, Intel, NVIDIA ਅਤੇ Qualcomm ਸਿਲਿਕਾਨ 'ਤੇ ਬਿਨਾਂ ਕਿਸੇ ਰੁਕਾਵਟ ਦੇ ਡਿਪਲੌਇਮੈਂਟ
- **ਡਿਵਾਈਸ-ਅਧਾਰਿਤ ਬੁੱਧੀਮਾਨਤਾ**: ਸਥਾਨਕ ਹਾਰਡਵੇਅਰ 'ਤੇ ਪੂਰੀ ਤਰ੍ਹਾਂ ਚੱਲਣ ਵਾਲਾ ਪ੍ਰਾਈਵੇਸੀ-ਸੰਭਾਲਣ ਵਾਲਾ AI
- **ਅਨੁਕੂਲ ਪ੍ਰਦਰਸ਼ਨ**: Windows ਹਾਰਡਵੇਅਰ ਕਨਫਿਗਰੇਸ਼ਨ ਲਈ ਪਹਿਲਾਂ ਤੋਂ ਅਨੁਕੂਲਿਤ ਮਾਡਲ
- **ਇੰਟਰਪ੍ਰਾਈਜ਼-ਤਿਆਰ**: ਉਤਪਾਦਨ-ਗ੍ਰੇਡ ਸੁਰੱਖਿਆ ਅਤੇ ਅਨੁਕੂਲਤਾ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ

### Windows ML 
Windows Machine Learning (ML) C#, C++, ਅਤੇ Python ਡਿਵੈਲਪਰਾਂ ਨੂੰ ONNX Runtime ਦੇ ਜ਼ਰੀਏ Windows PCs 'ਤੇ ਸਥਾਨਕ ਤੌਰ 'ਤੇ ONNX AI ਮਾਡਲ ਚਲਾਉਣ ਦੀ ਸਮਰਥਾ ਦਿੰਦਾ ਹੈ, ਵੱਖ-ਵੱਖ ਹਾਰਡਵੇਅਰ (CPUs, GPUs, NPUs) ਲਈ ਆਟੋਮੈਟਿਕ ਐਗਜ਼ਿਕਿਊਸ਼ਨ ਪ੍ਰੋਵਾਈਡਰ ਮੈਨੇਜਮੈਂਟ ਦੇ ਨਾਲ। [ONNX Runtime](https://onnxruntime.ai/docs/) ਨੂੰ PyTorch, Tensorflow/Keras, TFLite, scikit-learn ਅਤੇ ਹੋਰ ਫਰੇਮਵਰਕਾਂ ਦੇ ਮਾਡਲਾਂ ਨਾਲ ਵਰਤਿਆ ਜਾ ਸਕਦਾ ਹੈ।

![WindowsML ਇੱਕ ਡਾਇਗ੍ਰਾਮ ਜੋ ONNX ਮਾਡਲ ਨੂੰ Windows ML ਦੇ ਜ਼ਰੀਏ NPUs, GPUs ਅਤੇ CPUs ਤੱਕ ਪਹੁੰਚਣ ਨੂੰ ਦਰਸਾਉਂਦਾ ਹੈ।](https://learn.microsoft.com/en-us/windows/ai/images/winml-diagram.png)

Windows ML Windows-ਵਿਆਪਕ ONNX Runtime ਦੀ ਸਾਂਝੀ ਕਾਪੀ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ, ਨਾਲ ਹੀ ਐਗਜ਼ਿਕਿਊਸ਼ਨ ਪ੍ਰੋਵਾਈਡਰਾਂ (EPs) ਨੂੰ ਗਤੀਸ਼ੀਲ ਤੌਰ 'ਤੇ ਡਾਊਨਲੋਡ ਕਰਨ ਦੀ ਸਮਰਥਾ।

### Edge AI ਲਈ Windows ਕਿਉਂ?

**ਵਿਸ਼ਵਵਿਆਪੀ ਹਾਰਡਵੇਅਰ ਸਮਰਥਨ**
Windows ML ਪੂਰੇ Windows ਪਰਿਸਰ ਵਿੱਚ ਆਟੋਮੈਟਿਕ ਹਾਰਡਵੇਅਰ ਅਨੁਕੂਲਤਾ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ, ਇਹ ਯਕੀਨੀ ਬਣਾਉਂਦਾ ਹੈ ਕਿ ਤੁਹਾਡੇ AI ਐਪਲੀਕੇਸ਼ਨ ਬਿਨਾਂ ਕਿਸੇ ਰੁਕਾਵਟ ਦੇ ਸਿਲਿਕਾਨ ਆਰਕੀਟੈਕਚਰ ਦੇ ਅਧਾਰ 'ਤੇ ਚੰਗਾ ਪ੍ਰਦਰਸ਼ਨ ਕਰਦੇ ਹਨ।

**ਇੰਟਿਗ੍ਰੇਟਡ AI Runtime**
ਬਿਲਟ-ਇਨ Windows ML ਇੰਫਰੈਂਸ ਇੰਜਨ ਜਟਿਲ ਸੈਟਅਪ ਦੀ ਲੋੜ ਨੂੰ ਖਤਮ ਕਰਦਾ ਹੈ, ਡਿਵੈਲਪਰਾਂ ਨੂੰ ਇੰਫਰਾਸਟਰਕਚਰ ਦੀ ਚਿੰਤਾ ਕਰਨ ਦੀ ਬਜਾਏ ਐਪਲੀਕੇਸ਼ਨ ਲਾਜਿਕ 'ਤੇ ਧਿਆਨ ਕੇਂਦਰਿਤ ਕਰਨ ਦੀ ਆਜ਼ਾਦੀ ਦਿੰਦਾ ਹੈ।

**Copilot+ PC ਅਨੁਕੂਲਤਾ**
ਅਗਲੇ ਜਨਰੇਸ਼ਨ Windows ਡਿਵਾਈਸਾਂ ਲਈ ਖਾਸ ਤੌਰ 'ਤੇ ਤਿਆਰ ਕੀਤੇ APIs, ਜਿਨ੍ਹਾਂ ਵਿੱਚ Neural Processing Units (NPUs) ਸ਼ਾਮਲ ਹਨ, ਜੋ ਪ੍ਰਤੀ ਵਾਟ ਸ਼ਾਨਦਾਰ ਪ੍ਰਦਰਸ਼ਨ ਪ੍ਰਦਾਨ ਕਰਦੇ ਹਨ।

**ਡਿਵੈਲਪਰ ਪਰਿਸਰ**
Visual Studio ਇੰਟਿਗ੍ਰੇਸ਼ਨ, ਵਿਸਤ੍ਰਿਤ ਦਸਤਾਵੇਜ਼ੀਕਰਨ, ਅਤੇ ਨਮੂਨਾ ਐਪਲੀਕੇਸ਼ਨਾਂ ਸਮੇਤ ਵਿਸ਼ਾਲ ਟੂਲਿੰਗ ਜੋ ਵਿਕਾਸ ਚੱਕਰਾਂ ਨੂੰ ਤੇਜ਼ ਕਰਦਾ ਹੈ।

## ਸਿੱਖਣ ਦੇ ਉਦੇਸ਼

ਇਸ Windows Edge AI ਵਿਕਾਸ ਗਾਈਡ ਨੂੰ ਪੂਰਾ ਕਰਕੇ, ਤੁਸੀਂ Windows ਪਲੇਟਫਾਰਮ 'ਤੇ ਉਤਪਾਦਨ-ਤਿਆਰ AI ਐਪਲੀਕੇਸ਼ਨ ਬਣਾਉਣ ਲਈ ਜ਼ਰੂਰੀ ਹੁਨਰਾਂ ਵਿੱਚ ਮਾਹਰ ਹੋ ਜਾਵੋਗੇ।

### ਮੁੱਖ ਤਕਨੀਕੀ ਕਾਬਲੀਆਂ

**Windows AI Foundry ਵਿੱਚ ਮਾਹਰਤਾ**
- Windows AI Foundry ਪਲੇਟਫਾਰਮ ਦੀ ਆਰਕੀਟੈਕਚਰ ਅਤੇ ਘਟਕਾਂ ਨੂੰ ਸਮਝੋ
- Windows ਪਰਿਸਰ ਵਿੱਚ AI ਵਿਕਾਸ ਲਾਈਫਸਾਈਕਲ ਨੂੰ ਨੈਵੀਗੇਟ ਕਰੋ
- ਡਿਵਾਈਸ-ਅਧਾਰਿਤ AI ਐਪਲੀਕੇਸ਼ਨਾਂ ਲਈ ਸੁਰੱਖਿਆ ਦੇ ਸਰਵੋਤਮ ਅਭਿਆਸ ਲਾਗੂ ਕਰੋ
- ਵੱਖ-ਵੱਖ Windows ਹਾਰਡਵੇਅਰ ਕਨਫਿਗਰੇਸ਼ਨਾਂ ਲਈ ਐਪਲੀਕੇਸ਼ਨਾਂ ਨੂੰ ਅਨੁਕੂਲਿਤ ਕਰੋ

**API ਇੰਟਿਗ੍ਰੇਸ਼ਨ ਵਿੱਚ ਮਾਹਰਤਾ**
- ਟੈਕਸਟ, ਵਿਜ਼ਨ ਅਤੇ ਮਲਟੀਮੋਡਲ ਐਪਲੀਕੇਸ਼ਨਾਂ ਲਈ Windows AI APIs ਵਿੱਚ ਮਾਹਰ ਹੋਵੋ
- ਟੈਕਸਟ ਜਨਰੇਸ਼ਨ ਅਤੇ ਤਰਕ ਲਈ Phi Silica ਭਾਸ਼ਾ ਮਾਡਲ ਇੰਟਿਗ੍ਰੇਸ਼ਨ ਲਾਗੂ ਕਰੋ
- ਬਿਲਟ-ਇਨ ਇਮੇਜ ਪ੍ਰੋਸੈਸਿੰਗ APIs ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਕੰਪਿਊਟਰ ਵਿਜ਼ਨ ਸਮਰੱਥਾਵਾਂ ਡਿਪਲੌਇ ਕਰੋ
- LoRA (Low-Rank Adaptation) ਤਕਨੀਕਾਂ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਪ੍ਰੀ-ਟ੍ਰੇਨਡ ਮਾਡਲਾਂ ਨੂੰ ਕਸਟਮਾਈਜ਼ ਕਰੋ

**Foundry Local ਇੰਪਲੀਮੈਂਟੇਸ਼ਨ**
- Foundry Local CLI ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਖੁੱਲੇ-ਸਰੋਤ ਭਾਸ਼ਾ ਮਾਡਲਾਂ ਨੂੰ ਬ੍ਰਾਊਜ਼ ਕਰੋ, ਮੁਲਾਂਕਣ ਕਰੋ ਅਤੇ ਡਿਪਲੌਇ ਕਰੋ
- ਸਥਾਨਕ ਡਿਪਲੌਇਮੈਂਟ ਲਈ ਮਾਡਲ ਅਨੁਕੂਲਤਾ ਅਤੇ ਮਾਤਰਾ ਘਟਾਉਣ ਨੂੰ ਸਮਝੋ
- ਇੰਟਰਨੈਟ ਕਨੈਕਟਿਵਿਟੀ ਤੋਂ ਬਿਨਾਂ ਕੰਮ ਕਰਨ ਵਾਲੀਆਂ ਆਫਲਾਈਨ AI ਸਮਰੱਥਾਵਾਂ ਲਾਗੂ ਕਰੋ
- ਉਤਪਾਦਨ ਵਾਤਾਵਰਣਾਂ ਵਿੱਚ ਮਾਡਲ ਲਾਈਫਸਾਈਕਲ ਅਤੇ ਅਪਡੇਟਸ ਦਾ ਪ੍ਰਬੰਧਨ ਕਰੋ

**Windows ML ਡਿਪਲੌਇਮੈਂਟ**
- Windows ML ਦੀ ਵਰਤੋਂ ਕਰਕੇ Windows ਐਪਲੀਕੇਸ਼ਨਾਂ ਵਿੱਚ ਕਸਟਮ ONNX ਮਾਡਲ ਲਿਆਓ
- CPU, GPU ਅਤੇ NPU ਆਰਕੀਟੈਕਚਰਾਂ ਵਿੱਚ ਆਟੋਮੈਟਿਕ ਹਾਰਡਵੇਅਰ ਐਕਸਲੇਰੇਸ਼ਨ ਦਾ ਲਾਭ ਲਵੋ
- ਸਰਵੋਤਮ ਸਰੋਤ ਉਪਯੋਗਤਾ ਨਾਲ ਰੀਅਲ-ਟਾਈਮ ਇੰਫਰੈਂਸ ਲਾਗੂ ਕਰੋ
- ਵੱਖ-ਵੱਖ Windows ਡਿਵਾਈਸ ਸ਼੍ਰੇਣੀਆਂ ਲਈ ਸਕੇਲਬਲ AI ਐਪਲੀਕੇਸ਼ਨ ਡਿਜ਼ਾਈਨ ਕਰੋ

### ਐਪਲੀਕੇਸ਼ਨ ਵਿਕਾਸ ਦੇ ਹੁਨਰ

**ਕਰਾਸ-ਪਲੇਟਫਾਰਮ Windows ਵਿਕਾਸ**
- .NET MAUI ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਵਿਸ਼ਵਵਿਆਪੀ Windows ਡਿਪਲੌਇਮੈਂਟ ਲਈ AI-ਸੰਚਾਲਿਤ ਐਪਲੀਕੇਸ਼ਨ ਬਣਾਓ
- Win32, UWP ਅਤੇ ਪ੍ਰੋਗਰੈਸਿਵ ਵੈਬ ਐਪਲੀਕੇਸ਼ਨਾਂ ਵਿੱਚ AI ਸਮਰੱਥਾਵਾਂ ਸ਼ਾਮਲ ਕਰੋ
- AI ਪ੍ਰੋਸੈਸਿੰਗ ਸਟੇਟਸ ਦੇ ਅਨੁਕੂਲ ਹੋਣ ਵਾਲੇ ਰਿਸਪਾਂਸਿਵ UI ਡਿਜ਼ਾਈਨ ਲਾਗੂ ਕਰੋ
- ਸਹੀ ਯੂਜ਼ਰ ਅਨੁਭਵ ਪੈਟਰਨਾਂ ਨਾਲ ਅਸਿੰਕ੍ਰੋਨਸ AI ਕਾਰਵਾਈਆਂ ਨੂੰ ਸੰਭਾਲੋ

**ਪ੍ਰਦਰਸ਼ਨ ਅਨੁਕੂਲਤਾ**
- ਵੱਖ-ਵੱਖ ਹਾਰਡਵੇਅਰ ਕਨਫਿਗਰੇਸ਼ਨਾਂ ਵਿੱਚ AI ਇੰਫਰੈਂਸ ਪ੍ਰਦਰਸ਼ਨ ਨੂੰ ਪ੍ਰੋਫਾਈਲ ਅਤੇ ਅਨੁਕੂਲਿਤ ਕਰੋ
- ਵੱਡੇ ਭਾਸ਼ਾ ਮਾਡਲਾਂ ਲਈ ਕੁਸ਼ਲ ਮੈਮਰੀ ਪ੍ਰਬੰਧਨ ਲਾਗੂ ਕਰੋ
- ਉਪਲਬਧ ਹਾਰਡਵੇਅਰ ਸਮਰੱਥਾਵਾਂ ਦੇ ਅਧਾਰ 'ਤੇ ਐਪਲੀਕੇਸ਼ਨਾਂ ਨੂੰ ਗ੍ਰੇਸਫੁਲ ਡਿਗਰੇਡ ਕਰਨ ਲਈ ਡਿਜ਼ਾਈਨ ਕਰੋ
- ਵਾਰ-ਵਾਰ ਵਰਤੀਆਂ ਜਾਣ ਵਾਲੀਆਂ AI ਕਾਰਵਾਈਆਂ ਲਈ ਕੈਸ਼ਿੰਗ ਰਣਨੀਤੀਆਂ ਲਾਗੂ ਕਰੋ

**ਉਤਪਾਦਨ ਤਿਆਰੀ**
- ਵਿਸਤ੍ਰਿਤ ਗਲਤੀ ਸੰਭਾਲ ਅਤੇ ਫਾਲਬੈਕ ਮਕੈਨਿਜ਼ਮ ਲਾਗੂ ਕਰੋ
- AI ਐਪਲੀਕੇਸ਼ਨ ਪ੍ਰਦਰਸ਼ਨ ਲਈ ਟੈਲੀਮੈਟਰੀ ਅਤੇ ਮਾਨੀਟਰਿੰਗ ਡਿਜ਼ਾਈਨ ਕਰੋ
- ਸਥਾਨਕ AI ਮਾਡਲ ਸਟੋਰੇਜ ਅਤੇ ਐਗਜ਼ਿਕਿਊਸ਼ਨ ਲਈ ਸੁਰੱਖਿਆ ਦੇ ਸਰਵੋਤਮ ਅਭਿਆਸ ਲਾਗੂ ਕਰੋ
- ਇੰਟਰਪ੍ਰਾਈਜ਼ ਅਤੇ ਉਪਭੋਗਤਾ ਐਪਲੀਕੇਸ਼ਨਾਂ ਲਈ ਡਿਪਲੌਇਮੈਂਟ ਰਣਨੀਤੀਆਂ ਦੀ ਯੋਜਨਾ ਬਣਾਓ

### ਵਪਾਰਕ ਅਤੇ ਰਣਨੀਤਿਕ ਸਮਝ

**AI ਐਪਲੀਕੇਸ਼ਨ ਆਰਕੀਟੈਕਚਰ**
- ਸਥਾਨਕ ਅਤੇ ਕਲਾਉਡ AI ਪ੍ਰੋਸੈਸਿੰਗ ਦੇ ਵਿਚਕਾਰ ਅਨੁਕੂਲਤਾ ਲਈ ਹਾਈਬ੍ਰਿਡ ਆਰਕੀਟੈਕਚਰ ਡਿਜ਼ਾਈਨ ਕਰੋ
- ਮਾਡਲ ਆਕਾਰ, ਸ਼ੁੱਧਤਾ ਅਤੇ ਇੰਫਰੈਂਸ ਗਤੀ ਦੇ ਵਿਚਕਾਰ ਵਪਾਰਕ ਮੁਲਾਂਕਣ ਕਰੋ
- ਡੇਟਾ ਫਲੋ ਆਰਕੀਟੈਕਚਰਾਂ ਦੀ ਯੋਜਨਾ ਬਣਾਓ ਜੋ ਪ੍ਰਾਈਵੇਸੀ ਨੂੰ ਬਣਾਈ ਰੱਖਦੇ ਹੋਏ ਬੁੱਧੀਮਾਨਤਾ ਨੂੰ ਯਕੀਨੀ ਬਣਾਉਂਦੇ ਹਨ
- ਉਪਭੋਗਤਾ ਦੀ ਮੰਗ ਦੇ ਨਾਲ ਸਕੇਲ ਕਰਨ ਵਾਲੇ ਲਾਗਤ-ਪ੍ਰਭਾਵੀ AI ਹੱਲ ਲਾਗੂ ਕਰੋ

**ਬਾਜ਼ਾਰ ਪੋਜ਼ੀਸ਼ਨਿੰਗ**
- Windows-ਮੂਲ AI ਐਪਲੀਕੇਸ਼ਨਾਂ ਦੇ ਮੁਕਾਬਲਾਤੀ ਫਾਇਦਿਆਂ ਨੂੰ ਸਮਝੋ
- ਉਹ ਕੇਸਾਂ ਪਛਾਣੋ ਜਿੱਥੇ ਡਿਵਾਈਸ-ਅਧਾਰਿਤ AI ਉਤਕ੍ਰਿਸ਼ਟ ਯੂਜ਼ਰ ਅਨੁਭਵ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ
- AI-ਵਧੇਰੇ Windows ਐਪਲੀਕੇਸ਼ਨਾਂ ਲਈ ਬਾਜ਼ਾਰ ਵਿੱਚ ਜਾਣ ਦੀ ਰਣਨੀਤੀ ਵਿਕਸਿਤ ਕਰੋ
- Windows ਪਰਿਸਰ ਦੇ ਫਾਇਦਿਆਂ ਨੂੰ ਲਾਭਦਾਇਕ ਬਣਾਉਣ ਲਈ ਐਪਲੀਕੇਸ਼ਨਾਂ ਨੂੰ ਪੋਜ਼ੀਸ਼ਨ ਕਰੋ

## Windows App SDK AI ਨਮੂਨੇ

Windows App SDK ਵੱਖ-ਵੱਖ ਫਰੇਮਵਰਕਾਂ ਅਤੇ ਡਿਪਲੌਇਮੈਂਟ ਸਥਿਤੀਆਂ ਵਿੱਚ AI ਇੰਟਿਗ੍ਰੇਸ਼ਨ ਨੂੰ ਦਰਸਾਉਣ ਵਾਲੇ ਵਿਸਤ੍ਰਿਤ ਨਮੂਨੇ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ। ਇਹ ਨਮੂਨੇ Windows AI ਵਿਕਾਸ ਪੈਟਰਨਾਂ ਨੂੰ ਸਮਝਣ ਲਈ ਜ਼ਰੂਰੀ ਸੰਦਰਭ ਹਨ।

### Windows AI Foundry ਨਮੂਨੇ

| ਨਮੂਨਾ | ਫਰੇਮਵਰਕ | ਫੋਕਸ ਖੇਤਰ | ਮੁੱਖ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ |
|--------|-----------|------------|-------------|
| [cs-winui](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsAIFoundry/cs-winui) | C# WinUI 3 | Windows AI APIs ਇੰਟਿਗ੍ਰੇਸ਼ਨ | Windows AI APIs, ARM64 ਅਨੁਕੂਲਤਾ, ਪੈਕਡ ਡਿਪਲੌਇਮੈਂਟ |

**ਮੁੱਖ ਤਕਨੀਕਾਂ:**
- Windows AI APIs
- WinUI 3 ਫਰੇਮਵਰਕ
- ARM64 ਪਲੇਟਫਾਰਮ ਅਨੁਕੂਲਤਾ
- Copilot+ PC ਅਨੁਕੂਲਤਾ
- ਪੈਕਡ ਐਪ ਡਿਪਲੌਇਮੈਂਟ

**ਪੂਰਵ ਸ਼ਰਤਾਂ:**
- Windows 11 Copilot+ PC ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਗਈ ਹੈ
- Visual Studio 2022
- ARM64 ਬਿਲਡ ਕਨਫਿਗਰੇਸ਼ਨ
- Windows App SDK 1.8.1+

### Windows ML ਨਮੂਨੇ

#### C++ ਨਮੂਨੇ

| ਨਮੂਨਾ | ਕਿਸਮ | ਫੋਕਸ ਖੇਤਰ | ਮੁੱਖ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ |
|--------|------|------------|-------------|
| [CppConsoleDesktop](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Console App | ਬੁਨਿਆਦੀ Windows ML | EP ਖੋਜ, ਕਮਾਂਡ-ਲਾਈਨ ਵਿਕਲਪ, ਮਾਡਲ ਕੰਪਾਇਲੇਸ਼ਨ |
| [CppConsoleDesktop.FrameworkDependent](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Console App | ਫਰੇਮਵਰਕ ਡਿਪਲੌਇਮੈਂਟ | ਸਾਂਝਾ runtime, ਛੋਟਾ ਡਿਪਲੌਇਮੈਂਟ footprint |
| [CppConsoleDesktop.SelfContained](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Console App | ਸਵੈ-ਨਿਰਭਰ ਡਿਪਲੌਇਮੈਂਟ | standalone ਡਿਪਲੌਇਮੈਂਟ, runtime dependencies ਨਹੀਂ |
| [CppConsoleDll](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | DLL | ਲਾਇਬ੍ਰੇਰੀ ਵਰਤੋਂ | WindowsML shared library ਵਿੱਚ, memory management |
| [CppResnetBuildDemo](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cpp) | Demo | ResNet ਟਿਊਟੋਰਿਅਲ | ਮਾਡਲ ਰੂਪਾਂਤਰਨ, EP ਕੰਪਾਇਲੇਸ਼ਨ, Build 2025 ਟਿਊਟੋਰਿਅਲ |

#### C# ਨਮੂਨੇ

**Console Applications**

| ਨਮੂਨਾ | ਕਿਸਮ | ਫੋਕਸ ਖੇਤਰ | ਮੁੱਖ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ |
|--------|------|------------|-------------|
| [CSharpConsoleDesktop](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs) | Console App | ਬੁਨਿਆਦੀ C# ਇੰਟਿਗ੍ਰੇਸ਼ਨ | ਸਾਂਝੇ ਹੇਲਪਰ ਦੀ ਵਰਤੋਂ, ਕਮਾਂਡ-ਲਾਈਨ ਇੰਟਰਫੇਸ |
| [ResnetBuildDemoCS](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs) | Demo | ResNet ਟਿਊਟੋਰਿਅਲ | ਮਾਡਲ ਰੂਪਾਂਤਰਨ, EP ਕੰਪਾਇਲੇਸ਼ਨ, Build 2025 ਟਿਊਟੋਰਿਅਲ |

**GUI Applications**

| ਨਮੂਨਾ | ਫਰੇਮਵਰਕ | ਫੋਕਸ ਖੇਤਰ | ਮੁੱਖ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ |
|--------|-----------|------------|-------------|
| [cs-wpf](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs-wpf) | WPF | Desktop GUI | WPF ਇੰਟਰਫੇਸ ਨਾਲ ਇਮੇਜ ਕਲਾਸੀਫਿਕੇਸ਼ਨ |
| [cs-winforms](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs-winforms) | Windows Forms | Traditional GUI | Windows Forms ਨਾਲ ਇਮੇਜ ਕਲਾਸੀਫਿਕੇਸ਼ਨ |
| [cs-winui](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML/cs-winui) | WinUI 3 | Modern GUI | WinUI 3 ਇੰਟਰਫੇਸ ਨਾਲ ਇਮੇਜ ਕਲਾਸੀਫਿਕੇਸ਼ਨ |

#### Python ਨਮੂਨੇ

| ਨਮੂਨਾ | ਭਾਸ਼ਾ | ਫੋਕਸ ਖੇਤਰ | ਮੁੱਖ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ |
|--------|----------|------------|-------------|
| [SqueezeNet
| [rust/hello-foundry-local](https://github.com/microsoft/Foundry-Local/tree/main/samples/rust/hello-foundry-local) | Rust | ਸਿਸਟਮ ਇੰਟੀਗ੍ਰੇਸ਼ਨ | ਨੀਵਾਂ-ਸਤਹ SDK ਵਰਤੋਂ, ਐਸਿੰਕ ਓਪਰੇਸ਼ਨ, reqwest HTTP ਕਲਾਇੰਟ |

#### ਉਦਾਹਰਣ ਸ਼੍ਰੇਣੀਆਂ ਵਰਤੋਂ ਦੇ ਕੇਸ ਅਨੁਸਾਰ

**RAG (Retrieval-Augmented Generation)**
- **dotNET/rag**: Semantic Kernel, Qdrant ਵੇਕਟਰ ਡੇਟਾਬੇਸ, ਅਤੇ JINA embeddings ਦੀ ਵਰਤੋਂ ਨਾਲ ਪੂਰੀ RAG ਅਮਲਵਾਰੀ
- **ਆਰਕੀਟੈਕਚਰ**: ਦਸਤਾਵੇਜ਼ ਇੰਜੇਸ਼ਨ → ਟੈਕਸਟ ਚੰਕਿੰਗ → ਵੇਕਟਰ embeddings → ਸਮਾਨਤਾ ਖੋਜ → ਸੰਦਰਭ-ਜਾਣੂ ਜਵਾਬ
- **ਤਕਨਾਲੋਜੀਆਂ**: Microsoft.SemanticKernel, Qdrant.Client, BERT ONNX embeddings, ਸਟ੍ਰੀਮਿੰਗ ਚੈਟ ਪੂਰਨਤਾ

**ਡੈਸਕਟਾਪ ਐਪਲੀਕੇਸ਼ਨ**
- **electron/foundry-chat**: ਉਤਪਾਦਨ-ਤਿਆਰ ਚੈਟ ਐਪਲੀਕੇਸ਼ਨ ਸਥਾਨਕ/ਕਲਾਉਡ ਮਾਡਲ ਸਵਿੱਚਿੰਗ ਨਾਲ
- **ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ**: ਮਾਡਲ ਚੁਣਨ ਵਾਲਾ, ਸਟ੍ਰੀਮਿੰਗ ਜਵਾਬ, ਗਲਤੀ ਸੰਭਾਲ, ਕ੍ਰਾਸ-ਪਲੇਟਫਾਰਮ ਡਿਪਲੌਇਮੈਂਟ
- **ਆਰਕੀਟੈਕਚਰ**: Electron ਮੁੱਖ ਪ੍ਰਕਿਰਿਆ, IPC ਸੰਚਾਰ, ਸੁਰੱਖਿਅਤ ਪ੍ਰੀਲੋਡ ਸਕ੍ਰਿਪਟ

**SDK ਇੰਟੀਗ੍ਰੇਸ਼ਨ ਉਦਾਹਰਣ**
- **JavaScript (Node.js)**: ਮਾਡਲ ਅੰਤਰਕਿਰਿਆ ਅਤੇ ਸਟ੍ਰੀਮਿੰਗ ਜਵਾਬਾਂ ਦੀ ਬੁਨਿਆਦੀ ਵਰਤੋਂ
- **Python**: OpenAI-ਅਨੁਕੂਲ API ਵਰਤੋਂ ਐਸਿੰਕ ਸਟ੍ਰੀਮਿੰਗ ਨਾਲ
- **Rust**: reqwest ਅਤੇ tokio ਨਾਲ ਐਸਿੰਕ ਓਪਰੇਸ਼ਨ ਲਈ ਨੀਵਾਂ-ਸਤਹ ਇੰਟੀਗ੍ਰੇਸ਼ਨ

#### Foundry Local ਉਦਾਹਰਣਾਂ ਲਈ ਪੂਰਵ ਸ਼ਰਤਾਂ

**ਸਿਸਟਮ ਦੀਆਂ ਲੋੜਾਂ:**
- Windows 11 Foundry Local ਨਾਲ ਇੰਸਟਾਲ ਕੀਤਾ ਹੋਇਆ
- JavaScript/Electron ਉਦਾਹਰਣਾਂ ਲਈ Node.js v16+
- C# ਉਦਾਹਰਣਾਂ ਲਈ .NET 8.0+
- Python ਉਦਾਹਰਣਾਂ ਲਈ Python 3.10+
- Rust ਉਦਾਹਰਣਾਂ ਲਈ Rust 1.70+

**ਇੰਸਟਾਲੇਸ਼ਨ:**
```powershell
# Install Foundry Local
winget install Microsoft.FoundryLocal

# Verify installation
foundry --version
foundry model list
```

#### ਉਦਾਹਰਣ-ਵਿਸ਼ੇਸ਼ ਸੈਟਅਪ

**dotNET RAG ਉਦਾਹਰਣ:**
```powershell
# Install required packages via NuGet
# Microsoft.SemanticKernel.Connectors.Onnx
# Microsoft.SemanticKernel.Connectors.Qdrant
# Qdrant.Client

# Start Qdrant vector database
docker run -p 6333:6333 qdrant/qdrant

# Run Jupyter notebook
jupyter notebook rag_foundrylocal_demo.ipynb
```

**Electron Chat ਉਦਾਹਰਣ:**
```powershell
# Set environment variables for cloud fallback
$env:YOUR_API_KEY="your-cloud-api-key"
$env:YOUR_ENDPOINT="your-cloud-endpoint"
$env:YOUR_MODEL_NAME="your-cloud-model"

# Install dependencies and run
npm install
npm start
```

**JavaScript/Python/Rust ਉਦਾਹਰਣ:**
```powershell
# Download model (example with phi-3.5-mini)
foundry model run phi-3.5-mini

# Run respective sample
node src/app.js          # JavaScript
python src/app.py        # Python
cargo run               # Rust
```

#### ਮੁੱਖ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ

**ਮਾਡਲ ਕੈਟਾਲੌਗ**
- ਪੂਰੀ ਤਰ੍ਹਾਂ ਅਨੁਕੂਲਿਤ ਖੁੱਲੇ-ਸਰੋਤ ਮਾਡਲਾਂ ਦਾ ਵਿਸਤ੍ਰਿਤ ਸੰਗ੍ਰਹਿ
- ਤੁਰੰਤ ਡਿਪਲੌਇਮੈਂਟ ਲਈ CPUs, GPUs, ਅਤੇ NPUs 'ਤੇ ਅਨੁਕੂਲਿਤ ਮਾਡਲ
- ਪ੍ਰਸਿੱਧ ਮਾਡਲ ਪਰਿਵਾਰਾਂ ਲਈ ਸਹਾਇਤਾ ਜਿਵੇਂ ਕਿ Llama, Mistral, Phi, ਅਤੇ ਵਿਸ਼ੇਸ਼ ਡੋਮੇਨ ਮਾਡਲ

**CLI ਇੰਟੀਗ੍ਰੇਸ਼ਨ**
- ਮਾਡਲ ਪ੍ਰਬੰਧਨ ਅਤੇ ਡਿਪਲੌਇਮੈਂਟ ਲਈ ਕਮਾਂਡ-ਲਾਈਨ ਇੰਟਰਫੇਸ
- ਆਟੋਮੈਟਿਕ ਅਨੁਕੂਲਤਾ ਅਤੇ ਮਾਤਰਾ ਘਟਾਉਣ ਦੇ ਵਰਕਫਲੋ
- ਪ੍ਰਸਿੱਧ ਵਿਕਾਸ ਵਾਤਾਵਰਣ ਅਤੇ CI/CD ਪਾਈਪਲਾਈਨਾਂ ਨਾਲ ਇੰਟੀਗ੍ਰੇਸ਼ਨ

**ਸਥਾਨਕ ਡਿਪਲੌਇਮੈਂਟ**
- ਕਲਾਉਡ ਨਿਰਭਰਤਾਵਾਂ ਤੋਂ ਬਿਨਾਂ ਪੂਰੀ ਤਰ੍ਹਾਂ ਆਫਲਾਈਨ ਕਾਰਵਾਈ
- ਵਿਸ਼ੇਸ਼ ਮਾਡਲ ਫਾਰਮੈਟ ਅਤੇ ਸੰਰਚਨਾਵਾਂ ਲਈ ਸਹਾਇਤਾ
- ਸਵੈਚਾਲਿਤ ਹਾਰਡਵੇਅਰ ਅਨੁਕੂਲਤਾ ਨਾਲ ਕੁਸ਼ਲ ਮਾਡਲ ਸਰਵਿੰਗ

### 3. Windows ML

Windows ML Windows 'ਤੇ ਮੁੱਖ AI ਪਲੇਟਫਾਰਮ ਅਤੇ ਇੰਟੀਗ੍ਰੇਟਡ ਇੰਫਰੈਂਸਿੰਗ ਰਨਟਾਈਮ ਵਜੋਂ ਕੰਮ ਕਰਦਾ ਹੈ, ਜੋ ਵਿਕਾਸਕਾਰਾਂ ਨੂੰ ਵਿਸ਼ਾਲ Windows ਹਾਰਡਵੇਅਰ ਪਰੇਵਾਰ ਵਿੱਚ ਵਿਸ਼ੇਸ਼ ਮਾਡਲਾਂ ਨੂੰ ਕੁਸ਼ਲਤਾਪੂਰਵਕ ਡਿਪਲੌਇ ਕਰਨ ਦੀ ਆਗਿਆ ਦਿੰਦਾ ਹੈ।

#### ਆਰਕੀਟੈਕਚਰ ਦੇ ਫਾਇਦੇ

**ਯੂਨੀਵਰਸਲ ਹਾਰਡਵੇਅਰ ਸਹਾਇਤਾ**
- AMD, Intel, NVIDIA, ਅਤੇ Qualcomm ਸਿਲਿਕਾਨ ਲਈ ਆਟੋਮੈਟਿਕ ਅਨੁਕੂਲਤਾ
- CPU, GPU, ਅਤੇ NPU ਕਾਰਵਾਈ ਲਈ ਸਹਾਇਤਾ ਨਾਲ ਪਾਰਦਰਸ਼ੀ ਸਵਿੱਚਿੰਗ
- ਪਲੇਟਫਾਰਮ-ਵਿਸ਼ੇਸ਼ ਅਨੁਕੂਲਤਾ ਕੰਮ ਨੂੰ ਖਤਮ ਕਰਨ ਵਾਲਾ ਹਾਰਡਵੇਅਰ ਅਬਸਟਰੈਕਸ਼ਨ

**ਮਾਡਲ ਲਚਕਤਾ**
- ਪ੍ਰਸਿੱਧ ਫਰੇਮਵਰਕ ਤੋਂ ਆਟੋਮੈਟਿਕ ਰੂਪਾਂਤਰਨ ਨਾਲ ONNX ਮਾਡਲ ਫਾਰਮੈਟ ਲਈ ਸਹਾਇਤਾ
- ਉਤਪਾਦਨ-ਗਰੇਡ ਪ੍ਰਦਰਸ਼ਨ ਨਾਲ ਵਿਸ਼ੇਸ਼ ਮਾਡਲ ਡਿਪਲੌਇਮੈਂਟ
- ਮੌਜੂਦਾ Windows ਐਪਲੀਕੇਸ਼ਨ ਆਰਕੀਟੈਕਚਰਾਂ ਨਾਲ ਇੰਟੀਗ੍ਰੇਸ਼ਨ

**ਉਦਯੋਗ ਇੰਟੀਗ੍ਰੇਸ਼ਨ**
- Windows ਸੁਰੱਖਿਆ ਅਤੇ ਅਨੁਕੂਲਤਾ ਫਰੇਮਵਰਕਾਂ ਨਾਲ ਅਨੁਕੂਲ
- ਉਦਯੋਗ ਡਿਪਲੌਇਮੈਂਟ ਅਤੇ ਪ੍ਰਬੰਧਨ ਟੂਲਾਂ ਲਈ ਸਹਾਇਤਾ
- Windows ਡਿਵਾਈਸ ਪ੍ਰਬੰਧਨ ਅਤੇ ਨਿਗਰਾਨੀ ਸਿਸਟਮਾਂ ਨਾਲ ਇੰਟੀਗ੍ਰੇਸ਼ਨ

## ਵਿਕਾਸ ਵਰਕਫਲੋ

### ਚਰਨ 1: ਵਾਤਾਵਰਣ ਸੈਟਅਪ ਅਤੇ ਟੂਲ ਸੰਰਚਨਾ

**ਵਿਕਾਸ ਵਾਤਾਵਰਣ ਤਿਆਰੀ**
1. Visual Studio 2022 C++ ਅਤੇ .NET ਵਰਕਲੋਡਾਂ ਨਾਲ ਇੰਸਟਾਲ ਕਰੋ
2. Windows App SDK 1.8.1 ਜਾਂ ਇਸ ਤੋਂ ਉੱਚਾ ਇੰਸਟਾਲ ਕਰੋ
3. Windows AI Foundry CLI ਟੂਲਾਂ ਨੂੰ ਸੰਰਚਿਤ ਕਰੋ
4. Visual Studio Code ਲਈ AI Toolkit ਐਕਸਟੈਂਸ਼ਨ ਸੈਟਅਪ ਕਰੋ
5. ਪ੍ਰਦਰਸ਼ਨ ਪ੍ਰੋਫਾਈਲਿੰਗ ਅਤੇ ਨਿਗਰਾਨੀ ਟੂਲਾਂ ਸਥਾਪਿਤ ਕਰੋ
6. Copilot+ PC ਅਨੁਕੂਲਤਾ ਲਈ ARM64 ਬਿਲਡ ਸੰਰਚਨਾ ਸਥਾਪਿਤ ਕਰੋ

**ਉਦਾਹਰਣ ਰਿਪੋਜ਼ਟਰੀ ਸੈਟਅਪ**
1. [Windows App SDK Samples ਰਿਪੋਜ਼ਟਰੀ](https://github.com/microsoft/WindowsAppSDK-Samples) ਕਲੋਨ ਕਰੋ
2. Windows AI API ਉਦਾਹਰਣਾਂ ਲਈ `Samples/WindowsAIFoundry/cs-winui` 'ਤੇ ਜਾਓ
3. ਵਿਸਤ੍ਰਿਤ Windows ML ਉਦਾਹਰਣਾਂ ਲਈ `Samples/WindowsML` 'ਤੇ ਜਾਓ
4. ਆਪਣੇ ਟਾਰਗਟ ਪਲੇਟਫਾਰਮਾਂ ਲਈ [ਬਿਲਡ ਲੋੜਾਂ](https://learn.microsoft.com/windows/apps/windows-app-sdk/system-requirements) ਦੀ ਸਮੀਖਿਆ ਕਰੋ

**AI Dev Gallery ਦੀ ਖੋਜ**
- ਉਦਾਹਰਣ ਐਪਲੀਕੇਸ਼ਨ ਅਤੇ ਰਿਫਰੈਂਸ ਅਮਲਵਾਰੀਆਂ ਦੀ ਖੋਜ ਕਰੋ
- Windows AI APIs ਨਾਲ ਇੰਟਰਐਕਟਿਵ ਡੈਮੋਨਸਟਰੇਸ਼ਨ ਟੈਸਟ ਕਰੋ
- ਵਧੀਆ ਅਮਲ ਅਤੇ ਪੈਟਰਨ ਲਈ ਸਰੋਤ ਕੋਡ ਦੀ ਸਮੀਖਿਆ ਕਰੋ
- ਆਪਣੇ ਵਿਸ਼ੇਸ਼ ਵਰਤੋਂ ਦੇ ਕੇਸ ਲਈ ਸਬੰਧਤ ਉਦਾਹਰਣਾਂ ਦੀ ਪਛਾਣ ਕਰੋ

### ਚਰਨ 2: ਮਾਡਲ ਚੋਣ ਅਤੇ ਇੰਟੀਗ੍ਰੇਸ਼ਨ

**ਲੋੜਾਂ ਦਾ ਵਿਸ਼ਲੇਸ਼ਣ**
- AI ਸਮਰੱਥਾਵਾਂ ਲਈ ਕਾਰਜਕਾਰੀ ਲੋੜਾਂ ਨੂੰ ਪਰਿਭਾਸ਼ਿਤ ਕਰੋ
- ਪ੍ਰਦਰਸ਼ਨ ਪਾਬੰਦੀਆਂ ਅਤੇ ਅਨੁਕੂਲਤਾ ਟੀਚਿਆਂ ਨੂੰ ਸਥਾਪਿਤ ਕਰੋ
- ਗੋਪਨੀਯਤਾ ਅਤੇ ਸੁਰੱਖਿਆ ਲੋੜਾਂ ਦਾ ਮੁਲਾਂਕਣ ਕਰੋ
- ਡਿਪਲੌਇਮੈਂਟ ਆਰਕੀਟੈਕਚਰ ਅਤੇ ਸਕੇਲਿੰਗ ਰਣਨੀਤੀਆਂ ਦੀ ਯੋਜਨਾ ਬਣਾਓ

**ਮਾਡਲ ਮੁਲਾਂਕਣ**
- ਆਪਣੇ ਵਰਤੋਂ ਦੇ ਕੇਸ ਲਈ ਖੁੱਲੇ-ਸਰੋਤ ਮਾਡਲਾਂ ਦੀ ਜਾਂਚ ਕਰਨ ਲਈ Foundry Local ਦੀ ਵਰਤੋਂ ਕਰੋ
- ਵਿਸ਼ੇਸ਼ ਮਾਡਲ ਲੋੜਾਂ ਦੇ ਖਿਲਾਫ Windows AI APIs ਨੂੰ ਬੈਂਚਮਾਰਕ ਕਰੋ
- ਮਾਡਲ ਆਕਾਰ, ਸਹੀਤਾ, ਅਤੇ ਇੰਫਰੈਂਸ ਗਤੀ ਦੇ ਵਿਚਕਾਰ ਵਪਾਰ-ਬੰਦੀਆਂ ਦਾ ਮੁਲਾਂਕਣ ਕਰੋ
- ਚੁਣੇ ਹੋਏ ਮਾਡਲਾਂ ਨਾਲ ਇੰਟੀਗ੍ਰੇਸ਼ਨ ਪਹੁੰਚਾਂ ਦਾ ਪ੍ਰੋਟੋਟਾਈਪ ਬਣਾਓ

### ਚਰਨ 3: ਐਪਲੀਕੇਸ਼ਨ ਵਿਕਾਸ

**ਮੁੱਖ ਇੰਟੀਗ੍ਰੇਸ਼ਨ**
- Windows AI API ਇੰਟੀਗ੍ਰੇਸ਼ਨ ਨੂੰ ਸਹੀ ਗਲਤੀ ਸੰਭਾਲ ਨਾਲ ਲਾਗੂ ਕਰੋ
- AI ਪ੍ਰੋਸੈਸਿੰਗ ਵਰਕਫਲੋਜ਼ ਨੂੰ ਸਮਰਥਨ ਦੇਣ ਵਾਲੇ ਯੂਜ਼ਰ ਇੰਟਰਫੇਸ ਡਿਜ਼ਾਈਨ ਕਰੋ
- ਮਾਡਲ ਇੰਫਰੈਂਸ ਲਈ ਕੈਸ਼ਿੰਗ ਅਤੇ ਅਨੁਕੂਲਤਾ ਰਣਨੀਤੀਆਂ ਲਾਗੂ ਕਰੋ
- AI ਕਾਰਵਾਈ ਪ੍ਰਦਰਸ਼ਨ ਲਈ ਟੈਲੀਮੈਟਰੀ ਅਤੇ ਨਿਗਰਾਨੀ ਸ਼ਾਮਲ ਕਰੋ

**ਟੈਸਟਿੰਗ ਅਤੇ ਵੈਧਤਾ**
- ਵੱਖ-ਵੱਖ Windows ਹਾਰਡਵੇਅਰ ਸੰਰਚਨਾਵਾਂ 'ਤੇ ਐਪਲੀਕੇਸ਼ਨ ਟੈਸਟ ਕਰੋ
- ਵੱਖ-ਵੱਖ ਲੋਡ ਸ਼ਰਤਾਂ ਦੇ ਤਹਿਤ ਪ੍ਰਦਰਸ਼ਨ ਮਾਪਦੰਡਾਂ ਦੀ ਵੈਧਤਾ ਕਰੋ
- AI ਕਾਰਗੁਜ਼ਾਰੀ ਭਰੋਸੇਮੰਦਤਾ ਲਈ ਆਟੋਮੈਟਿਕ ਟੈਸਟਿੰਗ ਲਾਗੂ ਕਰੋ
- AI-ਵਧੇਰੇ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ ਨਾਲ ਯੂਜ਼ਰ ਅਨੁਭਵ ਟੈਸਟਿੰਗ ਕਰੋ

### ਚਰਨ 4: ਅਨੁਕੂਲਤਾ ਅਤੇ ਡਿਪਲੌਇਮੈਂਟ

**ਪ੍ਰਦਰਸ਼ਨ ਅਨੁਕੂਲਤਾ**
- ਟਾਰਗਟ ਹਾਰਡਵੇਅਰ ਸੰਰਚਨਾਵਾਂ 'ਤੇ ਐਪਲੀਕੇਸ਼ਨ ਪ੍ਰਦਰਸ਼ਨ ਪ੍ਰੋਫਾਈਲ ਕਰੋ
- ਮੈਮਰੀ ਵਰਤੋਂ ਅਤੇ ਮਾਡਲ ਲੋਡਿੰਗ ਰਣਨੀਤੀਆਂ ਨੂੰ ਅਨੁਕੂਲ ਕਰੋ
- ਉਪਲਬਧ ਹਾਰਡਵੇਅਰ ਸਮਰੱਥਾਵਾਂ ਦੇ ਅਧਾਰ 'ਤੇ ਅਨੁਕੂਲ ਵਿਹਾਰ ਲਾਗੂ ਕਰੋ
- ਵੱਖ-ਵੱਖ ਪ੍ਰਦਰਸ਼ਨ ਦ੍ਰਿਸ਼ਾਂ ਲਈ ਯੂਜ਼ਰ ਅਨੁਭਵ ਨੂੰ ਸੁਧਾਰੋ

**ਉਤਪਾਦਨ ਡਿਪਲੌਇਮੈਂਟ**
- ਸਹੀ AI ਮਾਡਲ ਨਿਰਭਰਤਾਵਾਂ ਨਾਲ ਐਪਲੀਕੇਸ਼ਨ ਪੈਕ ਕਰੋ
- ਮਾਡਲਾਂ ਅਤੇ ਐਪਲੀਕੇਸ਼ਨ ਲਾਜਿਕ ਲਈ ਅਪਡੇਟ ਮਕੈਨਿਜ਼ਮ ਲਾਗੂ ਕਰੋ
- ਉਤਪਾਦਨ ਵਾਤਾਵਰਣਾਂ ਲਈ ਨਿਗਰਾਨੀ ਅਤੇ ਵਿਸ਼ਲੇਸ਼ਣ ਸੰਰਚਿਤ ਕਰੋ
- ਉਦਯੋਗ ਅਤੇ ਉਪਭੋਗਤਾ ਡਿਪਲੌਇਮੈਂਟ ਲਈ ਰੋਲਆਉਟ ਰਣਨੀਤੀਆਂ ਦੀ ਯੋਜਨਾ ਬਣਾਓ

## ਵਿਹਾਰਕ ਅਮਲਵਾਰੀ ਉਦਾਹਰਣ

### ਉਦਾਹਰਣ 1: ਸਮਰੱਥ ਦਸਤਾਵੇਜ਼ ਪ੍ਰੋਸੈਸਿੰਗ ਐਪਲੀਕੇਸ਼ਨ

ਕਈ AI ਸਮਰੱਥਾਵਾਂ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਦਸਤਾਵੇਜ਼ ਪ੍ਰੋਸੈਸ ਕਰਨ ਵਾਲੀ Windows ਐਪਲੀਕੇਸ਼ਨ ਬਣਾਓ:

**ਵਰਤੀਆਂ ਤਕਨਾਲੋਜੀਆਂ:**
- ਦਸਤਾਵੇਜ਼ ਸੰਖੇਪਣ ਅਤੇ ਪ੍ਰਸ਼ਨ ਜਵਾਬ ਲਈ Phi Silica
- ਸਕੈਨ ਕੀਤੇ ਦਸਤਾਵੇਜ਼ਾਂ ਤੋਂ ਟੈਕਸਟ ਨਿਕਾਲਣ ਲਈ OCR APIs
- ਚਾਰਟ ਅਤੇ ਡਾਇਗ੍ਰਾਮ ਵਿਸ਼ਲੇਸ਼ਣ ਲਈ ਚਿੱਤਰ ਵਰਣ APIs
- ਦਸਤਾਵੇਜ਼ ਵਰਗੀਕਰਨ ਲਈ ਵਿਸ਼ੇਸ਼ ONNX ਮਾਡਲ

**ਅਮਲਵਾਰੀ ਪਹੁੰਚ:**
- ਪਲੱਗ-ਇਨ AI ਘਟਕਾਂ ਨਾਲ ਮੋਡਿਊਲਰ ਆਰਕੀਟੈਕਚਰ ਡਿਜ਼ਾਈਨ ਕਰੋ
- ਵੱਡੇ ਦਸਤਾਵੇਜ਼ ਬੈਚਾਂ ਲਈ ਐਸਿੰਕ ਪ੍ਰੋਸੈਸਿੰਗ ਲਾਗੂ ਕਰੋ
- ਲੰਬੇ ਚੱਲਣ ਵਾਲੇ ਓਪਰੇਸ਼ਨਾਂ ਲਈ ਪ੍ਰਗਤੀ ਸੂਚਕ ਅਤੇ ਰੱਦ ਕਰਨ ਦਾ ਸਮਰਥਨ ਸ਼ਾਮਲ ਕਰੋ
- ਸੰਵੇਦਨਸ਼ੀਲ ਦਸਤਾਵੇਜ਼ ਪ੍ਰੋਸੈਸਿੰਗ ਲਈ ਆਫਲਾਈਨ ਸਮਰਥਨ ਸ਼ਾਮਲ ਕਰੋ

### ਉਦਾਹਰਣ 2: ਰਿਟੇਲ ਇਨਵੈਂਟਰੀ ਪ੍ਰਬੰਧਨ ਸਿਸਟਮ

ਰਿਟੇਲ ਐਪਲੀਕੇਸ਼ਨਾਂ ਲਈ AI-ਸਮਰੱਥ ਇਨਵੈਂਟਰੀ ਸਿਸਟਮ ਬਣਾਓ:

**ਵਰਤੀਆਂ ਤਕਨਾਲੋਜੀਆਂ:**
- ਉਤਪਾਦ ਪਛਾਣ ਲਈ ਚਿੱਤਰ ਖੰਡਨ
- ਬ੍ਰਾਂਡ ਅਤੇ ਸ਼੍ਰੇਣੀ ਵਰਗੀਕਰਨ ਲਈ ਵਿਸ਼ੇਸ਼ ਵਿਜ਼ਨ ਮਾਡਲ
- ਵਿਸ਼ੇਸ਼ ਰਿਟੇਲ ਭਾਸ਼ਾ ਮਾਡਲਾਂ ਦੀ Foundry Local ਡਿਪਲੌਇਮੈਂਟ
- ਮੌਜੂਦਾ POS ਅਤੇ ਇਨਵੈਂਟਰੀ ਸਿਸਟਮਾਂ ਨਾਲ ਇੰਟੀਗ੍ਰੇਸ਼ਨ

**ਅਮਲਵਾਰੀ ਪਹੁੰਚ:**
- ਰੀਅਲ-ਟਾਈਮ ਉਤਪਾਦ ਸਕੈਨਿੰਗ ਲਈ ਕੈਮਰਾ ਇੰਟੀਗ੍ਰੇਸ਼ਨ ਬਣਾਓ
- ਬਾਰਕੋਡ ਅਤੇ ਵਿਜ਼ੂਅਲ ਉਤਪਾਦ ਪਛਾਣ ਲਾਗੂ ਕਰੋ
- ਸਥਾਨਕ ਭਾਸ਼ਾ ਮਾਡਲਾਂ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਕੁਦਰਤੀ ਭਾਸ਼ਾ ਇਨਵੈਂਟਰੀ ਪੁੱਛਗਿੱਛ ਸ਼ਾਮਲ ਕਰੋ
- ਬਹੁ-ਸਟੋਰ ਡਿਪਲੌਇਮੈਂਟ ਲਈ ਸਕੇਲ ਕਰਨ ਯੋਗ ਆਰਕੀਟੈਕਚਰ ਡਿਜ਼ਾਈਨ ਕਰੋ

### ਉਦਾਹਰਣ 3: ਹੈਲਥਕੇਅਰ ਦਸਤਾਵੇਜ਼ ਸਹਾਇਕ

ਗੋਪਨੀਯਤਾ-ਸੰਰਖਣ ਹੈਲਥਕੇਅਰ ਦਸਤਾਵੇਜ਼ ਟੂਲ ਵਿਕਸਿਤ ਕਰੋ:

**ਵਰਤੀਆਂ ਤਕਨਾਲੋਜੀਆਂ:**
- ਮੈਡੀਕਲ ਨੋਟ ਜਨਰੇਸ਼ਨ ਅਤੇ ਕਲੀਨਿਕਲ ਫੈਸਲੇ ਸਹਾਇਤਾ ਲਈ Phi Silica
- ਹੱਥ-ਲਿਖੇ ਮੈਡੀਕਲ ਰਿਕਾਰਡਾਂ ਨੂੰ ਡਿਜ਼ੀਟਾਈਜ਼ ਕਰਨ ਲਈ OCR
- Windows ML ਰਾਹੀਂ ਡਿਪਲੌਇ ਕੀਤੇ ਵਿਸ਼ੇਸ਼ ਮੈਡੀਕਲ ਭਾਸ਼ਾ ਮਾਡਲ
- ਮੈਡੀਕਲ ਗਿਆਨ ਪ੍ਰਾਪਤੀ ਲਈ ਸਥਾਨਕ ਵੇਕਟਰ ਸਟੋਰੇਜ

**ਅਮਲਵਾਰੀ ਪਹੁੰਚ:**
- ਮਰੀਜ਼ ਦੀ ਗੋਪਨੀਯਤਾ ਲਈ ਪੂਰੀ ਤਰ੍ਹਾਂ ਆਫਲਾਈਨ ਕਾਰਵਾਈ ਨੂੰ ਯਕੀਨੀ ਬਣਾਓ
- ਮੈਡੀਕਲ ਸ਼ਬਦਾਵਲੀ ਵੈਧਤਾ ਅਤੇ ਸੁਝਾਅ ਲਾਗੂ ਕਰੋ
- ਨਿਯਮਕ ਅਨੁਕੂਲਤਾ ਲਈ ਆਡਿਟ ਲੌਗਿੰਗ ਸ਼ਾਮਲ ਕਰੋ
- ਮੌਜੂਦਾ ਇਲੈਕਟ੍ਰਾਨਿਕ ਹੈਲਥ ਰਿਕਾਰਡ ਸਿਸਟਮਾਂ ਨਾਲ ਇੰਟੀਗ੍ਰੇਸ਼ਨ ਡਿਜ਼ਾਈਨ ਕਰੋ

## ਪ੍ਰਦਰਸ਼ਨ ਅਨੁਕੂਲਤਾ ਰਣਨੀਤੀਆਂ

### ਹਾਰਡਵੇਅਰ-ਜਾਣੂ ਵਿਕਾਸ

**NPU ਅਨੁਕੂਲਤਾ**
- Copilot+ PCs 'ਤੇ NPU ਸਮਰੱਥਾਵਾਂ ਦੀ ਵਰਤੋਂ ਕਰਨ ਲਈ ਐਪਲੀਕੇਸ਼ਨ ਡਿਜ਼ਾਈਨ ਕਰੋ
- NPU ਤੋਂ ਬਿਨਾਂ ਡਿਵਾਈਸਾਂ 'ਤੇ GPU/CPU ਲਈ ਸੁਗਮ ਫਾਲਬੈਕ ਲਾਗੂ ਕਰੋ
- NPU-ਵਿਸ਼ੇਸ਼ ਤੇਜ਼ੀ ਲਈ ਮਾਡਲ ਫਾਰਮੈਟਾਂ ਨੂੰ ਅਨੁਕੂਲ ਕਰੋ
- NPU ਵਰਤੋਂ ਅਤੇ ਥਰਮਲ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ ਦੀ ਨਿਗਰਾਨੀ ਕਰੋ
- [Windows ML ਝਲਕ](https://learn.microsoft.com/windows/ai/new-windows-ml/overview/)
- [Windows ਐਪ SDK ਸਿਸਟਮ ਦੀਆਂ ਲੋੜਾਂ](https://docs.microsoft.com/windows/apps/windows-app-sdk/system-requirements)
- [Windows ਐਪ SDK ਵਿਕਾਸ ਵਾਤਾਵਰਣ ਸੈਟਅੱਪ](https://docs.microsoft.com/windows/apps/windows-app-sdk/set-up-your-development-environment)
- 

### ਨਮੂਨਾ ਰਿਪੋਜ਼ਿਟਰੀ ਅਤੇ ਕੋਡ
- [Windows ਐਪ SDK ਨਮੂਨੇ - Windows AI Foundry](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsAIFoundry)
- [Windows ਐਪ SDK ਨਮੂਨੇ - Windows ML](https://github.com/microsoft/WindowsAppSDK-Samples/tree/main/Samples/WindowsML)
- [ONNX Runtime ਇਨਫਰੈਂਸ ਉਦਾਹਰਨ](https://github.com/microsoft/onnxruntime-inference-examples)
- [Windows ਐਪ SDK ਨਮੂਨਾ ਰਿਪੋਜ਼ਿਟਰੀ](https://github.com/microsoft/WindowsAppSDK-Samples)

### ਵਿਕਾਸ ਟੂਲ
- [Visual Studio Code ਲਈ AI Toolkit](https://learn.microsoft.com/windows/ai/toolkit/)
- [AI Dev ਗੈਲਰੀ](https://learn.microsoft.com/windows/ai/ai-dev-gallery/)
- [Windows AI ਨਮੂਨੇ](https://learn.microsoft.com/windows/ai/samples/)
- [ਮਾਡਲ ਕਨਵਰਜਨ ਟੂਲ](https://code.visualstudio.com/docs/intelligentapps/modelconversion)

### ਤਕਨੀਕੀ ਸਹਾਇਤਾ
- [Windows ML ਦਸਤਾਵੇਜ਼](https://learn.microsoft.com/windows/ai/new-windows-ml/overview)
- [ONNX Runtime ਦਸਤਾਵੇਜ਼](https://onnxruntime.ai/docs/)
- [Windows ਐਪ SDK ਦਸਤਾਵੇਜ਼](https://docs.microsoft.com/windows/apps/windows-app-sdk/)
- [ਮਸਲੇ ਰਿਪੋਰਟ ਕਰੋ - Windows ਐਪ SDK ਨਮੂਨੇ](https://github.com/microsoft/WindowsAppSDK-Samples/issues)

### ਕਮਿਊਨਿਟੀ ਅਤੇ ਸਹਾਇਤਾ
- [Windows ਡਿਵੈਲਪਰ ਕਮਿਊਨਿਟੀ](https://developer.microsoft.com/en-us/windows/)
- [Windows AI Foundry ਬਲੌਗ](https://blogs.windows.com/windowsdeveloper/)
- [Microsoft Learn AI ਟ੍ਰੇਨਿੰਗ](https://learn.microsoft.com/training/browse/?products=windows&subjects=artificial-intelligence)

---

*ਇਹ ਗਾਈਡ Windows AI ਪਰਿਵਾਰ ਦੇ ਤੇਜ਼ੀ ਨਾਲ ਅੱਗੇ ਵਧਦੇ ਪਹੂਣੇ ਨਾਲ ਅਨੁਕੂਲ ਬਣਾਈ ਗਈ ਹੈ। ਨਿਯਮਿਤ ਅੱਪਡੇਟ ਨਵੀਂ ਪਲੇਟਫਾਰਮ ਸਮਰੱਥਾਵਾਂ ਅਤੇ ਵਿਕਾਸ ਦੇ ਸ੍ਰੇਸ਼ਠ ਅਭਿਆਸਾਂ ਨਾਲ ਸੰਗਤਤਾ ਨੂੰ ਯਕੀਨੀ ਬਣਾਉਂਦੇ ਹਨ।*

[08. Microsoft Foundry Local ਨਾਲ ਹੱਥ-ਅਜਮਾਈ - ਪੂਰਾ ਡਿਵੈਲਪਰ ਟੂਲਕਿਟ](../Module08/README.md)

---

**ਅਸਵੀਕਰਤਾ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀ ਹੋਣ ਦਾ ਯਤਨ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਦਿਓ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸੁਚੱਜੇਪਣ ਹੋ ਸਕਦੇ ਹਨ। ਇਸ ਦੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਮੌਜੂਦ ਅਸਲ ਦਸਤਾਵੇਜ਼ ਨੂੰ ਅਧਿਕਾਰਤ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੇ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆ ਲਈ ਅਸੀਂ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।
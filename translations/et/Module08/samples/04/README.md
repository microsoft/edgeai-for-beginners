# Näidis 04: Tootmiskõlblikud vestlusrakendused Chainlitiga

Põhjalik näidis, mis demonstreerib mitmeid lähenemisviise tootmiskõlblike vestlusrakenduste loomiseks, kasutades Microsoft Foundry Locali. Sisaldab kaasaegseid veebiliideseid, voogesituse vastuseid ja tipptasemel brauseritehnoloogiaid.

## Mis on kaasas

- **🚀 Chainlit vestlusrakendus** (`app.py`): Tootmiskõlblik vestlusrakendus voogesitusega
- **🌐 WebGPU demo** (`webgpu-demo/`): Brauseripõhine AI järeldamine riistvarakiirendusega
- **🎨 Open WebUI integratsioon** (`open-webui-guide.md`): Professionaalne ChatGPT-laadne liides
- **📚 Õppematerjalid** (`chainlit_app.ipynb`): Interaktiivsed õppematerjalid

## Kiire alustamine

### 1. Chainlit vestlusrakendus

```cmd
# Navigate to Module08 directory
cd Module08

# Start your model
foundry model run phi-4-mini

# Run Chainlit app (using port 8080 to avoid conflicts)
chainlit run samples\04\app.py -w --port 8080
```
  
Avaneb aadressil: `http://localhost:8080`

### 2. WebGPU brauseri demo

```cmd
# Navigate to WebGPU demo
cd Module08\samples\04\webgpu-demo

# Serve the demo
python -m http.server 5173
```
  
Avaneb aadressil: `http://localhost:5173`

### 3. Open WebUI seadistamine

```cmd
# Run Open WebUI with Docker
docker run -d --name open-webui -p 3000:8080 \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-local-key \
  ghcr.io/open-webui/open-webui:main
```
  
Avaneb aadressil: `http://localhost:3000`

## Arhitektuurimustrid

### Kohalik vs pilve otsustusmaatriks

| Stsenaarium | Soovitus | Põhjus |
|-------------|----------|--------|
| **Privaatsustundlikud andmed** | 🏠 Kohalik (Foundry) | Andmed ei lahku seadmest |
| **Kompleksne arutlemine** | ☁️ Pilv (Azure OpenAI) | Juurdepääs suurematele mudelitele |
| **Reaalajas vestlus** | 🏠 Kohalik (Foundry) | Madalam latentsus, kiirem vastus |
| **Dokumendianalüüs** | 🔄 Hübriid | Kohalik ekstraheerimiseks, pilv analüüsiks |
| **Koodi genereerimine** | 🏠 Kohalik (Foundry) | Privaatsus + spetsialiseeritud mudelid |
| **Uurimistööd** | ☁️ Pilv (Azure OpenAI) | Vajalik lai teadmistebaas |

### Tehnoloogia võrdlus

| Tehnoloogia | Kasutusjuht | Plussid | Miinused |
|-------------|------------|---------|----------|
| **Chainlit** | Python arendajad, kiire prototüüpimine | Lihtne seadistamine, voogesituse tugi | Ainult Python |
| **WebGPU** | Maksimaalne privaatsus, võrguühenduseta stsenaariumid | Brauseripõhine, serverit pole vaja | Piiratud mudeli suurus |
| **Open WebUI** | Tootmiskasutus, meeskonnad | Professionaalne liides, kasutajahaldus | Vajab Dockeri kasutamist |

## Eeltingimused

- **Foundry Local**: Paigaldatud ja käivitatud ([Laadi alla](https://aka.ms/foundry-local-installer))
- **Python**: Versioon 3.10+ koos virtuaalse keskkonnaga
- **Mudel**: Vähemalt üks laaditud (`foundry model run phi-4-mini`)
- **Brauser**: Chrome/Edge WebGPU toetusega demode jaoks
- **Docker**: Open WebUI jaoks (valikuline)

## Paigaldamine ja seadistamine

### 1. Python keskkonna seadistamine

```cmd
# Navigate to Module08 directory
cd Module08

# Create and activate virtual environment
py -m venv .venv
.venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```
  
### 2. Foundry Local seadistamine

```cmd
# Verify Foundry Local installation
foundry --version

# Start the service
foundry service start

# Load a model
foundry model run phi-4-mini

# Verify model is running
foundry service ps
```
  
## Näidisrakendused

### Chainlit vestlusrakendus

**Omadused:**
- 🚀 **Reaalajas voogesitus**: Tokenid ilmuvad nende genereerimise ajal
- 🛡️ **Tõhus veakäsitlus**: Sujuv degradeerumine ja taastumine
- 🎨 **Kaasaegne liides**: Professionaalne vestlusliides kohe kasutamiseks
- 🔧 **Paindlik konfiguratsioon**: Keskkonnamuutujad ja automaatne tuvastamine
- 📱 **Responsiivne disain**: Töötab nii lauaarvutites kui mobiilseadmetes

**Kiire alustamine:**  
```cmd
# Run with default settings (recommended)
chainlit run samples\04\app.py -w --port 8080

# Use specific model
set MODEL=qwen2.5-7b
chainlit run samples\04\app.py -w --port 8080

# Manual endpoint configuration
set BASE_URL=http://localhost:51211
set API_KEY=your-api-key
chainlit run samples\04\app.py -w --port 8080
```
  
### WebGPU brauseri demo

**Omadused:**
- 🌐 **Brauseripõhine AI**: Serverit pole vaja, töötab täielikult brauseris
- ⚡ **WebGPU kiirendus**: Riistvarakiirendus, kui saadaval
- 🔒 **Maksimaalne privaatsus**: Andmed ei lahku kunagi seadmest
- 🎯 **Null paigaldust**: Töötab igas ühilduvas brauseris
- 🔄 **Sujuv varulahendus**: Lülitub CPU-le, kui WebGPU pole saadaval

**Käivitamine:**  
```cmd
cd samples\04\webgpu-demo
python -m http.server 5173
# Open http://localhost:5173
```
  
### Open WebUI integratsioon

**Omadused:**
- 🎨 **ChatGPT-laadne liides**: Professionaalne ja tuttav kasutajaliides
- 👥 **Mitme kasutaja tugi**: Kasutajakontod ja vestlusajalugu
- 📁 **Failide töötlemine**: Dokumentide üleslaadimine ja analüüs
- 🔄 **Mudelite vahetamine**: Lihtne vahetus erinevate mudelite vahel
- 🐳 **Dockeri kasutamine**: Tootmiskõlblik konteineriseeritud seadistus

**Kiire seadistamine:**  
```cmd
docker run -d --name open-webui -p 3000:8080 \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-local-key \
  ghcr.io/open-webui/open-webui:main
```
  
## Konfiguratsiooni viited

### Keskkonnamuutujad

| Muutuja | Kirjeldus | Vaikimisi | Näide |
|---------|-----------|-----------|-------|
| `MODEL` | Kasutatava mudeli alias | `phi-4-mini` | `qwen2.5-7b` |
| `BASE_URL` | Foundry Locali lõpp-punkt | Automaatne tuvastamine | `http://localhost:51211` |
| `API_KEY` | API võti (kohaliku jaoks valikuline) | `""` | `your-api-key` |

## Tõrkeotsing

### Levinud probleemid

**Chainlit rakendus:**

1. **Teenust pole saadaval:**  
   ```cmd
   # Check Foundry Local status
   foundry service status
   foundry service ps
   
   # Validate API endpoint (note: port 51211)
   curl http://localhost:51211/v1/models
   ```
  
2. **Portide konfliktid:**  
   ```cmd
   # Check what's using port 8080
   netstat -ano | findstr :8080
   
   # Use different port if needed
   chainlit run samples\04\app.py -w --port 3000
   ```
  
3. **Python keskkonna probleemid:**  
   ```cmd
   # Verify correct interpreter in VS Code
   # Ctrl+Shift+P → Python: Select Interpreter
   # Choose: Module08/.venv/Scripts/python.exe
   
   # Reinstall dependencies
   pip install -r requirements.txt
   ```
  
**WebGPU demo:**

1. **WebGPU pole toetatud:**
   - Uuenda Chrome/Edge versioonile 113+
   - Luba WebGPU: `chrome://flags/#enable-unsafe-webgpu`
   - Kontrolli GPU staatust: `chrome://gpu`
   - Demo lülitub automaatselt CPU-le

2. **Mudeli laadimise vead:**
   - Veendu, et internetiühendus on mudeli allalaadimiseks olemas
   - Kontrolli brauseri konsooli CORS vigade osas
   - Veendu, et teenust pakutakse HTTP kaudu (mitte file://)

**Open WebUI:**

1. **Ühendus keelatud:**  
   ```cmd
   # Check Docker is running
   docker --version
   
   # Check container status
   docker ps | findstr open-webui
   
   # View container logs
   docker logs open-webui
   ```
  
2. **Mudelid ei ilmu:**  
   ```cmd
   # Verify Foundry Local endpoint
   curl http://localhost:51211/v1/models
   
   # Restart Open WebUI
   docker restart open-webui
   ```
  
### Kontroll-loend

```cmd
# ✅ 1. Foundry Local Setup
foundry --version                    # Should show version
foundry service status               # Should show "running"
foundry model list                   # Should show loaded models
curl http://localhost:51211/v1/models  # Should return JSON

# ✅ 2. Python Environment  
python --version                     # Should be 3.10+
pip list | findstr chainlit         # Should show chainlit package
pip list | findstr openai           # Should show openai package

# ✅ 3. Application Testing
chainlit run samples\04\app.py -w --port 8080  # Should open browser
# Test WebGPU demo at localhost:5173
# Test Open WebUI at localhost:3000
```
  
## Täiustatud kasutamine

### Jõudluse optimeerimine

**Chainlit:**
- Kasuta voogesitust parema tajutava jõudluse jaoks
- Rakenda ühenduste ühendamist suure koormuse korral
- Vahemälu mudeli vastused korduvate päringute jaoks
- Jälgi mälu kasutust suurte vestlusajaloode korral

**WebGPU:**
- Kasuta WebGPU-d maksimaalse privaatsuse ja kiiruse jaoks
- Rakenda mudeli kvantiseerimist väiksemate mudelite jaoks
- Kasuta Web Workereid tausttöötluseks
- Vahemälu kompileeritud mudelid brauseri salvestuses

**Open WebUI:**
- Kasuta püsivaid mahtusid vestlusajaloo jaoks
- Konfigureeri ressursipiirangud Dockeri konteinerile
- Rakenda varundusstrateegiaid kasutajaandmete jaoks
- Seadista pöördproksi SSL-i lõpetamiseks

### Integratsioonimustrid

**Hübriid kohalik/pilv:**  
```python
# Route based on complexity and privacy requirements
async def intelligent_routing(prompt: str, metadata: dict):
    if metadata.get("contains_pii"):
        return await foundry_local_completion(prompt)  # Privacy-sensitive
    elif len(prompt.split()) > 200:
        return await azure_openai_completion(prompt)   # Complex reasoning
    else:
        return await foundry_local_completion(prompt)  # Default local
```
  
**Multimodaalne torustik:**  
```python
# Combine different AI capabilities
async def analyze_document(file_path: str):
    # 1. OCR with WebGPU (browser-based)
    text = await webgpu_ocr(file_path)
    
    # 2. Analysis with Foundry Local (private)
    summary = await foundry_local_analyze(text)
    
    # 3. Enhancement with cloud (if needed)
    if summary.confidence < 0.8:
        summary = await azure_openai_enhance(summary)
    
    return summary
```
  
## Tootmiskasutus

### Turvalisuse kaalutlused

- **API võtmed**: Kasuta keskkonnamuutujaid, ära kunagi kõvasta koodi
- **Võrk**: Kasuta HTTPS-i tootmises, kaalu VPN-i meeskonna ligipääsuks
- **Juurdepääsukontroll**: Rakenda autentimine Open WebUI jaoks
- **Andmete privaatsus**: Auditeeri, millised andmed jäävad kohalikuks ja millised lähevad pilve
- **Uuendused**: Hoia Foundry Local ja konteinerid ajakohased

### Jälgimine ja hooldus

- **Tervisekontrollid**: Rakenda lõpp-punktide jälgimist
- **Logimine**: Keskusta logid kõigist komponentidest
- **Mõõdikud**: Jälgi vastuseaegu, veamäärasid, ressursikasutust
- **Varundus**: Regulaarne vestlusandmete ja konfiguratsioonide varundamine

## Viited ja ressursid

### Dokumentatsioon
- [Chainlit dokumentatsioon](https://docs.chainlit.io/) - Täielik raamistikujuhend
- [Foundry Local dokumentatsioon](https://learn.microsoft.com/azure/ai-foundry/foundry-local/) - Microsofti ametlik dokumentatsioon
- [ONNX Runtime Web](https://onnxruntime.ai/docs/get-started/with-javascript/web.html) - WebGPU integratsioon
- [Open WebUI dokumentatsioon](https://docs.openwebui.com/) - Täiustatud konfiguratsioon

### Näidisfailid
- [`app.py`](../../../../../Module08/samples/04/app.py) - Tootmiskõlblik Chainlit rakendus
- [`chainlit_app.ipynb`](./chainlit_app.ipynb) - Õppematerjalid
- [`webgpu-demo/`](../../../../../Module08/samples/04/webgpu-demo) - Brauseripõhine AI järeldamine
- [`open-webui-guide.md`](./open-webui-guide.md) - Täielik Open WebUI seadistus

### Seotud näidised
- [Sessioon 4 dokumentatsioon](../../04.CuttingEdgeModels.md) - Täielik sessioonijuhend
- [Foundry Local näidised](https://github.com/microsoft/foundry-local/tree/main/samples) - Ametlikud näidised

---

**Vastutusest loobumine**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.
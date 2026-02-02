# Vzorec 04: Produkcijske klepetalne aplikacije s Chainlit

Celovit primer, ki prikazuje različne pristope za izdelavo produkcijsko pripravljenih klepetalnih aplikacij z uporabo Microsoft Foundry Local, vključno z modernimi spletnimi vmesniki, pretočnimi odgovori in najsodobnejšimi tehnologijami brskalnika.

## Kaj je vključeno

- **🚀 Chainlit klepetalna aplikacija** (`app.py`): Produkcijsko pripravljena klepetalna aplikacija s pretočnimi odgovori
- **🌐 WebGPU demo** (`webgpu-demo/`): AI sklepanje v brskalniku z uporabo strojne pospešitve
- **🎨 Integracija Open WebUI** (`open-webui-guide.md`): Profesionalni vmesnik, podoben ChatGPT
- **📚 Izobraževalni zvezek** (`chainlit_app.ipynb`): Interaktivni učni materiali

## Hiter začetek

### 1. Chainlit klepetalna aplikacija

```cmd
# Navigate to Module08 directory
cd Module08

# Start your model
foundry model run phi-4-mini

# Run Chainlit app (using port 8080 to avoid conflicts)
chainlit run samples\04\app.py -w --port 8080
```

Odpre se na: `http://localhost:8080`

### 2. WebGPU demo v brskalniku

```cmd
# Navigate to WebGPU demo
cd Module08\samples\04\webgpu-demo

# Serve the demo
python -m http.server 5173
```

Odpre se na: `http://localhost:5173`

### 3. Namestitev Open WebUI

```cmd
# Run Open WebUI with Docker
docker run -d --name open-webui -p 3000:8080 \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-local-key \
  ghcr.io/open-webui/open-webui:main
```

Odpre se na: `http://localhost:3000`

## Vzorci arhitekture

### Lokalno vs. oblak: odločitvena matrika

| Scenarij | Priporočilo | Razlog |
|----------|-------------|--------|
| **Občutljivi podatki** | 🏠 Lokalno (Foundry) | Podatki ne zapustijo naprave |
| **Kompleksno sklepanje** | ☁️ Oblak (Azure OpenAI) | Dostop do večjih modelov |
| **Klepet v realnem času** | 🏠 Lokalno (Foundry) | Nižja zakasnitev, hitrejši odzivi |
| **Analiza dokumentov** | 🔄 Hibridno | Lokalno za ekstrakcijo, oblak za analizo |
| **Generiranje kode** | 🏠 Lokalno (Foundry) | Zasebnost + specializirani modeli |
| **Raziskovalne naloge** | ☁️ Oblak (Azure OpenAI) | Potrebna široka baza znanja |

### Primerjava tehnologij

| Tehnologija | Uporaba | Prednosti | Slabosti |
|-------------|---------|-----------|----------|
| **Chainlit** | Python razvijalci, hitro prototipiranje | Enostavna namestitev, podpora za pretok | Samo za Python |
| **WebGPU** | Maksimalna zasebnost, scenariji brez povezave | Brskalniku lastno, brez strežnika | Omejena velikost modela |
| **Open WebUI** | Produkcijska uporaba, ekipe | Profesionalni vmesnik, upravljanje uporabnikov | Zahteva Docker |

## Predpogoji

- **Foundry Local**: Nameščen in delujoč ([Prenesi](https://aka.ms/foundry-local-installer))
- **Python**: 3.10+ z virtualnim okoljem
- **Model**: Vsaj en naložen (`foundry model run phi-4-mini`)
- **Brskalnik**: Chrome/Edge s podporo za WebGPU za demo
- **Docker**: Za Open WebUI (neobvezno)

## Namestitev in nastavitev

### 1. Nastavitev Python okolja

```cmd
# Navigate to Module08 directory
cd Module08

# Create and activate virtual environment
py -m venv .venv
.venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Nastavitev Foundry Local

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

## Vzorec aplikacij

### Chainlit klepetalna aplikacija

**Funkcije:**
- 🚀 **Pretok v realnem času**: Tokeni se prikažejo, ko so generirani
- 🛡️ **Zanesljivo ravnanje z napakami**: Postopno poslabšanje in okrevanje
- 🎨 **Moderen vmesnik**: Profesionalni klepetalni vmesnik že pripravljen
- 🔧 **Prilagodljiva konfiguracija**: Spremenljivke okolja in samodejno zaznavanje
- 📱 **Prilagodljiv dizajn**: Deluje na namiznih in mobilnih napravah

**Hiter začetek:**
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

### WebGPU demo v brskalniku

**Funkcije:**
- 🌐 **AI, ki deluje v brskalniku**: Brez strežnika, deluje popolnoma v brskalniku
- ⚡ **Pospešitev z WebGPU**: Strojna pospešitev, kadar je na voljo
- 🔒 **Maksimalna zasebnost**: Podatki nikoli ne zapustijo vaše naprave
- 🎯 **Brez namestitve**: Deluje v katerem koli združljivem brskalniku
- 🔄 **Postopno poslabšanje**: Preklopi na CPU, če WebGPU ni na voljo

**Zagon:**
```cmd
cd samples\04\webgpu-demo
python -m http.server 5173
# Open http://localhost:5173
```

### Integracija Open WebUI

**Funkcije:**
- 🎨 **Vmesnik, podoben ChatGPT**: Profesionalen, znan vmesnik
- 👥 **Podpora za več uporabnikov**: Uporabniški računi in zgodovina pogovorov
- 📁 **Obdelava datotek**: Nalaganje in analiza dokumentov
- 🔄 **Preklapljanje med modeli**: Enostavno preklapljanje med različnimi modeli
- 🐳 **Namestitev z Dockerjem**: Produkcijsko pripravljena namestitev v kontejnerju

**Hitra nastavitev:**
```cmd
docker run -d --name open-webui -p 3000:8080 \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-local-key \
  ghcr.io/open-webui/open-webui:main
```

## Referenca konfiguracije

### Spremenljivke okolja

| Spremenljivka | Opis | Privzeto | Primer |
|---------------|------|----------|--------|
| `MODEL` | Alias modela za uporabo | `phi-4-mini` | `qwen2.5-7b` |
| `BASE_URL` | Endpoint za Foundry Local | Samodejno zaznano | `http://localhost:51211` |
| `API_KEY` | API ključ (neobvezno za lokalno) | `""` | `your-api-key` |

## Odpravljanje težav

### Pogoste težave

**Chainlit aplikacija:**

1. **Storitev ni na voljo:**
   ```cmd
   # Check Foundry Local status
   foundry service status
   foundry service ps
   
   # Validate API endpoint (note: port 51211)
   curl http://localhost:51211/v1/models
   ```

2. **Konflikti vrat:**
   ```cmd
   # Check what's using port 8080
   netstat -ano | findstr :8080
   
   # Use different port if needed
   chainlit run samples\04\app.py -w --port 3000
   ```

3. **Težave z Python okoljem:**
   ```cmd
   # Verify correct interpreter in VS Code
   # Ctrl+Shift+P → Python: Select Interpreter
   # Choose: Module08/.venv/Scripts/python.exe
   
   # Reinstall dependencies
   pip install -r requirements.txt
   ```

**WebGPU demo:**

1. **WebGPU ni podprt:**
   - Posodobite na Chrome/Edge 113+
   - Omogočite WebGPU: `chrome://flags/#enable-unsafe-webgpu`
   - Preverite status GPU: `chrome://gpu`
   - Demo se bo samodejno preklopil na CPU

2. **Napake pri nalaganju modela:**
   - Preverite internetno povezavo za prenos modela
   - Preverite konzolo brskalnika za CORS napake
   - Preverite, ali strežnik deluje prek HTTP (ne file://)

**Open WebUI:**

1. **Povezava zavrnjena:**
   ```cmd
   # Check Docker is running
   docker --version
   
   # Check container status
   docker ps | findstr open-webui
   
   # View container logs
   docker logs open-webui
   ```

2. **Modeli se ne prikažejo:**
   ```cmd
   # Verify Foundry Local endpoint
   curl http://localhost:51211/v1/models
   
   # Restart Open WebUI
   docker restart open-webui
   ```

### Preveritveni seznam

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

## Napredna uporaba

### Optimizacija zmogljivosti

**Chainlit:**
- Uporabite pretok za boljšo zaznano zmogljivost
- Implementirajte združevanje povezav za visoko sočasnost
- Predpomnite odgovore modela za ponavljajoče se poizvedbe
- Spremljajte porabo pomnilnika pri velikih zgodovinah pogovorov

**WebGPU:**
- Uporabite WebGPU za maksimalno zasebnost in hitrost
- Implementirajte kvantizacijo modela za manjše modele
- Uporabite Web Workers za obdelavo v ozadju
- Predpomnite prevedene modele v shranjevanju brskalnika

**Open WebUI:**
- Uporabite trajne volumne za zgodovino pogovorov
- Konfigurirajte omejitve virov za Docker kontejner
- Implementirajte strategije varnostnega kopiranja za uporabniške podatke
- Nastavite povratni proxy za SSL zaključek

### Vzorci integracije

**Hibridno lokalno/oblak:**
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

**Večmodalni cevovod:**
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

## Produkcijska namestitev

### Varnostni vidiki

- **API ključi**: Uporabite spremenljivke okolja, nikoli jih ne vgrajujte
- **Omrežje**: Uporabite HTTPS v produkciji, razmislite o VPN za dostop ekipe
- **Nadzor dostopa**: Implementirajte avtentikacijo za Open WebUI
- **Zasebnost podatkov**: Preglejte, kateri podatki ostanejo lokalni in kateri gredo v oblak
- **Posodobitve**: Redno posodabljajte Foundry Local in kontejnerje

### Nadzor in vzdrževanje

- **Preverjanje stanja**: Implementirajte nadzor endpointov
- **Dnevniški zapisi**: Centralizirajte dnevnike iz vseh komponent
- **Metrične podatke**: Spremljajte odzivne čase, stopnje napak, porabo virov
- **Varnostne kopije**: Redno varnostno kopirajte podatke pogovorov in konfiguracije

## Reference in viri

### Dokumentacija
- [Chainlit dokumentacija](https://docs.chainlit.io/) - Celoten vodnik za okvir
- [Foundry Local dokumentacija](https://learn.microsoft.com/azure/ai-foundry/foundry-local/) - Uradna Microsoft dokumentacija
- [ONNX Runtime Web](https://onnxruntime.ai/docs/get-started/with-javascript/web.html) - Integracija WebGPU
- [Open WebUI dokumentacija](https://docs.openwebui.com/) - Napredna konfiguracija

### Vzorčne datoteke
- [`app.py`](../../../../../Module08/samples/04/app.py) - Produkcijska Chainlit aplikacija
- [`chainlit_app.ipynb`](./chainlit_app.ipynb) - Izobraževalni zvezek
- [`webgpu-demo/`](../../../../../Module08/samples/04/webgpu-demo) - AI sklepanje v brskalniku
- [`open-webui-guide.md`](./open-webui-guide.md) - Celoten vodnik za Open WebUI

### Povezani vzorci
- [Dokumentacija seje 4](../../04.CuttingEdgeModels.md) - Celoten vodnik seje
- [Foundry Local vzorci](https://github.com/microsoft/foundry-local/tree/main/samples) - Uradni vzorci

---

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve AI za prevajanje [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne odgovarjamo za morebitna nesporazumevanja ali napačne razlage, ki izhajajo iz uporabe tega prevoda.
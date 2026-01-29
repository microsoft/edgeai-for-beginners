# Primjer 04: Produkcijske aplikacije za chat s Chainlitom

Sveobuhvatan primjer koji prikazuje različite pristupe izradi produkcijski spremnih aplikacija za chat koristeći Microsoft Foundry Local, s modernim web sučeljima, streaming odgovorima i najnovijim tehnologijama preglednika.

## Što je uključeno

- **🚀 Chainlit Chat App** (`app.py`): Produkcijski spremna aplikacija za chat sa streamingom
- **🌐 WebGPU Demo** (`webgpu-demo/`): AI inferencija u pregledniku s hardverskom akceleracijom
- **🎨 Integracija Open WebUI** (`open-webui-guide.md`): Profesionalno sučelje slično ChatGPT-u
- **📚 Edukativni Notebook** (`chainlit_app.ipynb`): Interaktivni edukativni materijali

## Brzi početak

### 1. Chainlit aplikacija za chat

```cmd
# Navigate to Module08 directory
cd Module08

# Start your model
foundry model run phi-4-mini

# Run Chainlit app (using port 8080 to avoid conflicts)
chainlit run samples\04\app.py -w --port 8080
```

Otvara se na: `http://localhost:8080`

### 2. WebGPU demo u pregledniku

```cmd
# Navigate to WebGPU demo
cd Module08\samples\04\webgpu-demo

# Serve the demo
python -m http.server 5173
```

Otvara se na: `http://localhost:5173`

### 3. Postavljanje Open WebUI

```cmd
# Run Open WebUI with Docker
docker run -d --name open-webui -p 3000:8080 \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-local-key \
  ghcr.io/open-webui/open-webui:main
```

Otvara se na: `http://localhost:3000`

## Obrasci arhitekture

### Lokalno vs. Cloud matrica odluka

| Scenarij | Preporuka | Razlog |
|----------|-----------|--------|
| **Osjetljivi podaci** | 🏠 Lokalno (Foundry) | Podaci nikada ne napuštaju uređaj |
| **Kompleksno zaključivanje** | ☁️ Cloud (Azure OpenAI) | Pristup većim modelima |
| **Chat u stvarnom vremenu** | 🏠 Lokalno (Foundry) | Niža latencija, brži odgovori |
| **Analiza dokumenata** | 🔄 Hibrid | Lokalno za ekstrakciju, cloud za analizu |
| **Generiranje koda** | 🏠 Lokalno (Foundry) | Privatnost + specijalizirani modeli |
| **Istraživački zadaci** | ☁️ Cloud (Azure OpenAI) | Potrebna široka baza znanja |

### Usporedba tehnologija

| Tehnologija | Upotreba | Prednosti | Nedostaci |
|-------------|----------|-----------|-----------|
| **Chainlit** | Python developeri, brzo prototipiranje | Jednostavno postavljanje, podrška za streaming | Samo za Python |
| **WebGPU** | Maksimalna privatnost, offline scenariji | Nativno za preglednik, bez potrebe za serverom | Ograničena veličina modela |
| **Open WebUI** | Produkcijsko postavljanje, timovi | Profesionalno sučelje, upravljanje korisnicima | Zahtijeva Docker |

## Preduvjeti

- **Foundry Local**: Instaliran i pokrenut ([Preuzmi](https://aka.ms/foundry-local-installer))
- **Python**: Verzija 3.10+ s virtualnim okruženjem
- **Model**: Najmanje jedan učitan (`foundry model run phi-4-mini`)
- **Preglednik**: Chrome/Edge s podrškom za WebGPU za demo
- **Docker**: Za Open WebUI (opcionalno)

## Instalacija i postavljanje

### 1. Postavljanje Python okruženja

```cmd
# Navigate to Module08 directory
cd Module08

# Create and activate virtual environment
py -m venv .venv
.venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Postavljanje Foundry Local

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

## Primjeri aplikacija

### Chainlit aplikacija za chat

**Značajke:**
- 🚀 **Streaming u stvarnom vremenu**: Tokeni se prikazuju kako se generiraju
- 🛡️ **Robusno rukovanje greškama**: Postupno degradiranje i oporavak
- 🎨 **Moderni UI**: Profesionalno sučelje za chat odmah dostupno
- 🔧 **Fleksibilna konfiguracija**: Varijable okruženja i automatsko otkrivanje
- 📱 **Responzivni dizajn**: Radi na stolnim i mobilnim uređajima

**Brzi početak:**
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

### WebGPU demo u pregledniku

**Značajke:**
- 🌐 **AI nativan za preglednik**: Bez potrebe za serverom, radi potpuno u pregledniku
- ⚡ **WebGPU akceleracija**: Hardverska akceleracija kad je dostupna
- 🔒 **Maksimalna privatnost**: Podaci nikada ne napuštaju vaš uređaj
- 🎯 **Bez instalacije**: Radi u bilo kojem kompatibilnom pregledniku
- 🔄 **Postupno fallback**: Prebacuje se na CPU ako WebGPU nije dostupan

**Pokretanje:**
```cmd
cd samples\04\webgpu-demo
python -m http.server 5173
# Open http://localhost:5173
```

### Integracija Open WebUI

**Značajke:**
- 🎨 **Sučelje slično ChatGPT-u**: Profesionalno, poznato UI
- 👥 **Podrška za više korisnika**: Korisnički računi i povijest razgovora
- 📁 **Obrada datoteka**: Učitavanje i analiza dokumenata
- 🔄 **Prebacivanje modela**: Jednostavno prebacivanje između različitih modela
- 🐳 **Docker postavljanje**: Produkcijski spremno postavljanje u kontejnerima

**Brzo postavljanje:**
```cmd
docker run -d --name open-webui -p 3000:8080 \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-local-key \
  ghcr.io/open-webui/open-webui:main
```

## Referenca konfiguracije

### Varijable okruženja

| Varijabla | Opis | Zadano | Primjer |
|-----------|------|--------|---------|
| `MODEL` | Alias modela za korištenje | `phi-4-mini` | `qwen2.5-7b` |
| `BASE_URL` | Endpoint za Foundry Local | Automatski otkriven | `http://localhost:51211` |
| `API_KEY` | API ključ (opcionalno za lokalno) | `""` | `your-api-key` |

## Rješavanje problema

### Uobičajeni problemi

**Chainlit aplikacija:**

1. **Usluga nije dostupna:**
   ```cmd
   # Check Foundry Local status
   foundry service status
   foundry service ps
   
   # Validate API endpoint (note: port 51211)
   curl http://localhost:51211/v1/models
   ```

2. **Sukobi portova:**
   ```cmd
   # Check what's using port 8080
   netstat -ano | findstr :8080
   
   # Use different port if needed
   chainlit run samples\04\app.py -w --port 3000
   ```

3. **Problemi s Python okruženjem:**
   ```cmd
   # Verify correct interpreter in VS Code
   # Ctrl+Shift+P → Python: Select Interpreter
   # Choose: Module08/.venv/Scripts/python.exe
   
   # Reinstall dependencies
   pip install -r requirements.txt
   ```

**WebGPU demo:**

1. **WebGPU nije podržan:**
   - Ažurirajte na Chrome/Edge 113+
   - Omogućite WebGPU: `chrome://flags/#enable-unsafe-webgpu`
   - Provjerite status GPU-a: `chrome://gpu`
   - Demo će se automatski prebaciti na CPU

2. **Greške pri učitavanju modela:**
   - Provjerite internetsku vezu za preuzimanje modela
   - Provjerite konzolu preglednika za CORS greške
   - Provjerite da li koristite HTTP (ne file://)

**Open WebUI:**

1. **Veza odbijena:**
   ```cmd
   # Check Docker is running
   docker --version
   
   # Check container status
   docker ps | findstr open-webui
   
   # View container logs
   docker logs open-webui
   ```

2. **Modeli se ne prikazuju:**
   ```cmd
   # Verify Foundry Local endpoint
   curl http://localhost:51211/v1/models
   
   # Restart Open WebUI
   docker restart open-webui
   ```

### Lista za validaciju

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

## Napredno korištenje

### Optimizacija performansi

**Chainlit:**
- Koristite streaming za bolju percepciju performansi
- Implementirajte pooling veza za visoku konkurentnost
- Keširajte odgovore modela za ponovljene upite
- Pratite korištenje memorije s velikim povijestima razgovora

**WebGPU:**
- Koristite WebGPU za maksimalnu privatnost i brzinu
- Implementirajte kvantizaciju modela za manje modele
- Koristite Web Workers za obradu u pozadini
- Keširajte kompajlirane modele u pohrani preglednika

**Open WebUI:**
- Koristite trajne volumene za povijest razgovora
- Konfigurirajte ograničenja resursa za Docker kontejner
- Implementirajte strategije za backup korisničkih podataka
- Postavite reverse proxy za SSL terminaciju

### Obrasci integracije

**Hibrid lokalno/cloud:**
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

**Multimodalni pipeline:**
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

## Produkcijsko postavljanje

### Sigurnosni aspekti

- **API ključevi**: Koristite varijable okruženja, nikada ih ne hardkodirajte
- **Mreža**: Koristite HTTPS u produkciji, razmotrite VPN za timski pristup
- **Kontrola pristupa**: Implementirajte autentifikaciju za Open WebUI
- **Privatnost podataka**: Provjerite koji podaci ostaju lokalni, a koji idu u cloud
- **Ažuriranja**: Redovito ažurirajte Foundry Local i kontejnere

### Praćenje i održavanje

- **Provjere zdravlja**: Implementirajte praćenje endpointa
- **Logovi**: Centralizirajte logove svih komponenti
- **Metrički podaci**: Pratite vrijeme odgovora, stopu grešaka, korištenje resursa
- **Backup**: Redovito izrađujte backup podataka razgovora i konfiguracija

## Reference i resursi

### Dokumentacija
- [Chainlit Dokumentacija](https://docs.chainlit.io/) - Kompletan vodič za framework
- [Foundry Local Dokumentacija](https://learn.microsoft.com/azure/ai-foundry/foundry-local/) - Službeni Microsoft dokumenti
- [ONNX Runtime Web](https://onnxruntime.ai/docs/get-started/with-javascript/web.html) - Integracija WebGPU-a
- [Open WebUI Dokumentacija](https://docs.openwebui.com/) - Napredna konfiguracija

### Primjeri datoteka
- [`app.py`](../../../../../Module08/samples/04/app.py) - Produkcijska Chainlit aplikacija
- [`chainlit_app.ipynb`](./chainlit_app.ipynb) - Edukativni notebook
- [`webgpu-demo/`](../../../../../Module08/samples/04/webgpu-demo) - AI inferencija u pregledniku
- [`open-webui-guide.md`](./open-webui-guide.md) - Kompletno postavljanje Open WebUI-a

### Povezani primjeri
- [Dokumentacija za sesiju 4](../../04.CuttingEdgeModels.md) - Kompletan vodič za sesiju
- [Primjeri Foundry Local](https://github.com/microsoft/foundry-local/tree/main/samples) - Službeni primjeri

---

**Izjava o odricanju odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane ljudskog prevoditelja. Ne preuzimamo odgovornost za nesporazume ili pogrešna tumačenja koja mogu proizaći iz korištenja ovog prijevoda.
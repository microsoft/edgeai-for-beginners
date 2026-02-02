# Ukážka 04: Produkčné chatovacie aplikácie s Chainlit

Komplexná ukážka, ktorá demonštruje rôzne prístupy k vytváraniu produkčne pripravených chatovacích aplikácií pomocou Microsoft Foundry Local, vrátane moderných webových rozhraní, streamovania odpovedí a najnovších technológií prehliadača.

## Čo je zahrnuté

- **🚀 Chainlit Chat App** (`app.py`): Produkčne pripravená chatovacia aplikácia so streamovaním
- **🌐 WebGPU Demo** (`webgpu-demo/`): AI inferencia v prehliadači s hardvérovou akceleráciou
- **🎨 Integrácia Open WebUI** (`open-webui-guide.md`): Profesionálne rozhranie podobné ChatGPT
- **📚 Edukačný notebook** (`chainlit_app.ipynb`): Interaktívne vzdelávacie materiály

## Rýchly štart

### 1. Chainlit Chat Application

```cmd
# Navigate to Module08 directory
cd Module08

# Start your model
foundry model run phi-4-mini

# Run Chainlit app (using port 8080 to avoid conflicts)
chainlit run samples\04\app.py -w --port 8080
```

Otvára sa na: `http://localhost:8080`

### 2. WebGPU Browser Demo

```cmd
# Navigate to WebGPU demo
cd Module08\samples\04\webgpu-demo

# Serve the demo
python -m http.server 5173
```

Otvára sa na: `http://localhost:5173`

### 3. Nastavenie Open WebUI

```cmd
# Run Open WebUI with Docker
docker run -d --name open-webui -p 3000:8080 \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-local-key \
  ghcr.io/open-webui/open-webui:main
```

Otvára sa na: `http://localhost:3000`

## Architektonické vzory

### Matrica rozhodovania medzi lokálnym a cloudovým riešením

| Scenár | Odporúčanie | Dôvod |
|--------|-------------|-------|
| **Citlivé údaje** | 🏠 Lokálne (Foundry) | Dáta nikdy neopustia zariadenie |
| **Komplexné uvažovanie** | ☁️ Cloud (Azure OpenAI) | Prístup k väčším modelom |
| **Chat v reálnom čase** | 🏠 Lokálne (Foundry) | Nižšia latencia, rýchlejšie odpovede |
| **Analýza dokumentov** | 🔄 Hybrid | Lokálne na extrakciu, cloud na analýzu |
| **Generovanie kódu** | 🏠 Lokálne (Foundry) | Ochrana súkromia + špecializované modely |
| **Výskumné úlohy** | ☁️ Cloud (Azure OpenAI) | Potrebná široká databáza znalostí |

### Porovnanie technológií

| Technológia | Použitie | Výhody | Nevýhody |
|-------------|----------|--------|----------|
| **Chainlit** | Python vývojári, rýchle prototypovanie | Jednoduché nastavenie, podpora streamovania | Len pre Python |
| **WebGPU** | Maximálne súkromie, offline scenáre | Nativné prehliadačové, bez potreby servera | Obmedzená veľkosť modelu |
| **Open WebUI** | Produkčné nasadenie, tímy | Profesionálne UI, správa používateľov | Vyžaduje Docker |

## Predpoklady

- **Foundry Local**: Nainštalované a spustené ([Stiahnuť](https://aka.ms/foundry-local-installer))
- **Python**: Verzia 3.10+ s virtuálnym prostredím
- **Model**: Aspoň jeden načítaný (`foundry model run phi-4-mini`)
- **Prehliadač**: Chrome/Edge s podporou WebGPU pre demo
- **Docker**: Pre Open WebUI (voliteľné)

## Inštalácia a nastavenie

### 1. Nastavenie Python prostredia

```cmd
# Navigate to Module08 directory
cd Module08

# Create and activate virtual environment
py -m venv .venv
.venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Nastavenie Foundry Local

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

## Ukážkové aplikácie

### Chainlit Chat Application

**Funkcie:**
- 🚀 **Streamovanie v reálnom čase**: Tokeny sa zobrazujú počas ich generovania
- 🛡️ **Robustné spracovanie chýb**: Plynulé zotavenie pri problémoch
- 🎨 **Moderné UI**: Profesionálne chatovacie rozhranie pripravené na použitie
- 🔧 **Flexibilná konfigurácia**: Premenné prostredia a automatická detekcia
- 📱 **Responzívny dizajn**: Funguje na desktopoch aj mobilných zariadeniach

**Rýchly štart:**
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

### WebGPU Browser Demo

**Funkcie:**
- 🌐 **AI nativné pre prehliadač**: Nepotrebuje server, beží priamo v prehliadači
- ⚡ **Akcelerácia WebGPU**: Hardvérová akcelerácia, ak je dostupná
- 🔒 **Maximálne súkromie**: Dáta nikdy neopustia vaše zariadenie
- 🎯 **Bez inštalácie**: Funguje v akomkoľvek kompatibilnom prehliadači
- 🔄 **Plynulý prechod**: Automaticky prejde na CPU, ak WebGPU nie je dostupné

**Spustenie:**
```cmd
cd samples\04\webgpu-demo
python -m http.server 5173
# Open http://localhost:5173
```

### Integrácia Open WebUI

**Funkcie:**
- 🎨 **Rozhranie podobné ChatGPT**: Profesionálne, známe UI
- 👥 **Podpora viacerých používateľov**: Účty používateľov a história konverzácií
- 📁 **Spracovanie súborov**: Nahrávanie a analýza dokumentov
- 🔄 **Prepínanie modelov**: Jednoduché prepínanie medzi rôznymi modelmi
- 🐳 **Nasadenie pomocou Dockeru**: Produkčne pripravené kontajnerové nastavenie

**Rýchle nastavenie:**
```cmd
docker run -d --name open-webui -p 3000:8080 \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-local-key \
  ghcr.io/open-webui/open-webui:main
```

## Referencia konfigurácie

### Premenné prostredia

| Premenná | Popis | Predvolená hodnota | Príklad |
|----------|-------|--------------------|---------|
| `MODEL` | Alias modelu na použitie | `phi-4-mini` | `qwen2.5-7b` |
| `BASE_URL` | Endpoint Foundry Local | Automaticky detekovaný | `http://localhost:51211` |
| `API_KEY` | API kľúč (voliteľný pre lokálne) | `""` | `your-api-key` |

## Riešenie problémov

### Bežné problémy

**Chainlit aplikácia:**

1. **Služba nie je dostupná:**
   ```cmd
   # Check Foundry Local status
   foundry service status
   foundry service ps
   
   # Validate API endpoint (note: port 51211)
   curl http://localhost:51211/v1/models
   ```

2. **Konflikty portov:**
   ```cmd
   # Check what's using port 8080
   netstat -ano | findstr :8080
   
   # Use different port if needed
   chainlit run samples\04\app.py -w --port 3000
   ```

3. **Problémy s Python prostredím:**
   ```cmd
   # Verify correct interpreter in VS Code
   # Ctrl+Shift+P → Python: Select Interpreter
   # Choose: Module08/.venv/Scripts/python.exe
   
   # Reinstall dependencies
   pip install -r requirements.txt
   ```

**WebGPU demo:**

1. **WebGPU nie je podporované:**
   - Aktualizujte na Chrome/Edge 113+
   - Aktivujte WebGPU: `chrome://flags/#enable-unsafe-webgpu`
   - Skontrolujte stav GPU: `chrome://gpu`
   - Demo automaticky prejde na CPU

2. **Chyby pri načítaní modelu:**
   - Skontrolujte internetové pripojenie na stiahnutie modelu
   - Skontrolujte konzolu prehliadača na chyby CORS
   - Overte, že používate HTTP (nie file://)

**Open WebUI:**

1. **Odmietnuté pripojenie:**
   ```cmd
   # Check Docker is running
   docker --version
   
   # Check container status
   docker ps | findstr open-webui
   
   # View container logs
   docker logs open-webui
   ```

2. **Modely sa nezobrazujú:**
   ```cmd
   # Verify Foundry Local endpoint
   curl http://localhost:51211/v1/models
   
   # Restart Open WebUI
   docker restart open-webui
   ```

### Kontrolný zoznam validácie

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

## Pokročilé použitie

### Optimalizácia výkonu

**Chainlit:**
- Používajte streamovanie pre lepší vnímaný výkon
- Implementujte pooling pripojení pre vysokú súbežnosť
- Cache odpovede modelu pre opakované dotazy
- Monitorujte pamäť pri veľkých históriách konverzácií

**WebGPU:**
- Používajte WebGPU pre maximálne súkromie a rýchlosť
- Implementujte kvantizáciu modelu pre menšie modely
- Používajte Web Workers na spracovanie na pozadí
- Cache skompilované modely v úložisku prehliadača

**Open WebUI:**
- Používajte perzistentné objemy pre históriu konverzácií
- Konfigurujte limity zdrojov pre Docker kontajner
- Implementujte stratégie zálohovania pre údaje používateľov
- Nastavte reverzný proxy server pre SSL termináciu

### Vzory integrácie

**Hybridné lokálne/cloudové riešenie:**
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

**Multimodálna pipeline:**
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

## Produkčné nasadenie

### Bezpečnostné úvahy

- **API kľúče**: Používajte premenné prostredia, nikdy ich nezapisujte priamo
- **Sieť**: Používajte HTTPS v produkcii, zvážte VPN pre prístup tímu
- **Kontrola prístupu**: Implementujte autentifikáciu pre Open WebUI
- **Ochrana údajov**: Auditujte, ktoré údaje zostávajú lokálne a ktoré idú do cloudu
- **Aktualizácie**: Udržujte Foundry Local a kontajnery aktualizované

### Monitorovanie a údržba

- **Kontroly stavu**: Implementujte monitorovanie endpointov
- **Logovanie**: Centralizujte logy zo všetkých komponentov
- **Metriky**: Sledujte časy odozvy, chybovosť, využitie zdrojov
- **Zálohovanie**: Pravidelné zálohovanie údajov z konverzácií a konfigurácií

## Referencie a zdroje

### Dokumentácia
- [Chainlit Dokumentácia](https://docs.chainlit.io/) - Kompletný sprievodca frameworkom
- [Foundry Local Dokumentácia](https://learn.microsoft.com/azure/ai-foundry/foundry-local/) - Oficiálne Microsoft dokumenty
- [ONNX Runtime Web](https://onnxruntime.ai/docs/get-started/with-javascript/web.html) - Integrácia WebGPU
- [Open WebUI Dokumentácia](https://docs.openwebui.com/) - Pokročilá konfigurácia

### Ukážkové súbory
- [`app.py`](../../../../../Module08/samples/04/app.py) - Produkčná Chainlit aplikácia
- [`chainlit_app.ipynb`](./chainlit_app.ipynb) - Edukačný notebook
- [`webgpu-demo/`](../../../../../Module08/samples/04/webgpu-demo) - AI inferencia v prehliadači
- [`open-webui-guide.md`](./open-webui-guide.md) - Kompletné nastavenie Open WebUI

### Súvisiace ukážky
- [Dokumentácia Session 4](../../04.CuttingEdgeModels.md) - Kompletný sprievodca session
- [Foundry Local Samples](https://github.com/microsoft/foundry-local/tree/main/samples) - Oficiálne ukážky

---

**Upozornenie**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, prosím, berte na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nenesieme zodpovednosť za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
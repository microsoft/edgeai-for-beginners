# Ukázka 04: Produkční chatovací aplikace s Chainlit

Komplexní ukázka představující různé přístupy k vytváření produkčně připravených chatovacích aplikací pomocí Microsoft Foundry Local, zahrnující moderní webové rozhraní, streamované odpovědi a nejnovější technologie prohlížečů.

## Co je zahrnuto

- **🚀 Chainlit Chat App** (`app.py`): Produkčně připravená chatovací aplikace se streamováním
- **🌐 WebGPU Demo** (`webgpu-demo/`): AI inference v prohlížeči s hardwarovou akcelerací
- **🎨 Integrace Open WebUI** (`open-webui-guide.md`): Profesionální rozhraní podobné ChatGPT
- **📚 Edukační notebook** (`chainlit_app.ipynb`): Interaktivní výukové materiály

## Rychlý start

### 1. Chainlit Chat Application

```cmd
# Navigate to Module08 directory
cd Module08

# Start your model
foundry model run phi-4-mini

# Run Chainlit app (using port 8080 to avoid conflicts)
chainlit run samples\04\app.py -w --port 8080
```

Otevře se na: `http://localhost:8080`

### 2. WebGPU Browser Demo

```cmd
# Navigate to WebGPU demo
cd Module08\samples\04\webgpu-demo

# Serve the demo
python -m http.server 5173
```

Otevře se na: `http://localhost:5173`

### 3. Nastavení Open WebUI

```cmd
# Run Open WebUI with Docker
docker run -d --name open-webui -p 3000:8080 \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-local-key \
  ghcr.io/open-webui/open-webui:main
```

Otevře se na: `http://localhost:3000`

## Architektonické vzory

### Matice rozhodování: Lokální vs. cloud

| Scénář | Doporučení | Důvod |
|--------|------------|-------|
| **Citlivá data** | 🏠 Lokální (Foundry) | Data nikdy neopouští zařízení |
| **Komplexní uvažování** | ☁️ Cloud (Azure OpenAI) | Přístup k větším modelům |
| **Chat v reálném čase** | 🏠 Lokální (Foundry) | Nižší latence, rychlejší odpovědi |
| **Analýza dokumentů** | 🔄 Hybridní | Lokální pro extrakci, cloud pro analýzu |
| **Generování kódu** | 🏠 Lokální (Foundry) | Soukromí + specializované modely |
| **Výzkumné úkoly** | ☁️ Cloud (Azure OpenAI) | Potřeba široké znalostní báze |

### Porovnání technologií

| Technologie | Použití | Výhody | Nevýhody |
|-------------|---------|--------|----------|
| **Chainlit** | Python vývojáři, rychlé prototypování | Snadné nastavení, podpora streamování | Pouze Python |
| **WebGPU** | Maximální soukromí, offline scénáře | Nativní prohlížeč, není potřeba server | Omezená velikost modelu |
| **Open WebUI** | Produkční nasazení, týmy | Profesionální UI, správa uživatelů | Vyžaduje Docker |

## Předpoklady

- **Foundry Local**: Nainstalováno a spuštěno ([Stáhnout](https://aka.ms/foundry-local-installer))
- **Python**: Verze 3.10+ s virtuálním prostředím
- **Model**: Alespoň jeden načtený (`foundry model run phi-4-mini`)
- **Prohlížeč**: Chrome/Edge s podporou WebGPU pro demo
- **Docker**: Pro Open WebUI (volitelné)

## Instalace a nastavení

### 1. Nastavení Python prostředí

```cmd
# Navigate to Module08 directory
cd Module08

# Create and activate virtual environment
py -m venv .venv
.venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Nastavení Foundry Local

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

## Ukázkové aplikace

### Chainlit Chat Application

**Funkce:**
- 🚀 **Streamování v reálném čase**: Tokeny se zobrazují, jakmile jsou generovány
- 🛡️ **Robustní zpracování chyb**: Plynulé zotavení při problémech
- 🎨 **Moderní UI**: Profesionální chatovací rozhraní připravené k použití
- 🔧 **Flexibilní konfigurace**: Proměnné prostředí a automatická detekce
- 📱 **Responzivní design**: Funguje na desktopu i mobilních zařízeních

**Rychlý start:**
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

**Funkce:**
- 🌐 **AI nativní pro prohlížeč**: Není potřeba server, běží kompletně v prohlížeči
- ⚡ **Akcelerace WebGPU**: Hardwarová akcelerace, pokud je dostupná
- 🔒 **Maximální soukromí**: Data nikdy neopouští vaše zařízení
- 🎯 **Bez instalace**: Funguje v jakémkoli kompatibilním prohlížeči
- 🔄 **Plynulý přechod**: Automaticky přechází na CPU, pokud WebGPU není dostupné

**Spuštění:**
```cmd
cd samples\04\webgpu-demo
python -m http.server 5173
# Open http://localhost:5173
```

### Integrace Open WebUI

**Funkce:**
- 🎨 **Rozhraní podobné ChatGPT**: Profesionální, známé UI
- 👥 **Podpora více uživatelů**: Uživatelské účty a historie konverzací
- 📁 **Zpracování souborů**: Nahrávání a analýza dokumentů
- 🔄 **Přepínání modelů**: Snadné přepínání mezi různými modely
- 🐳 **Nasazení pomocí Dockeru**: Produkčně připravené kontejnerové nastavení

**Rychlé nastavení:**
```cmd
docker run -d --name open-webui -p 3000:8080 \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-local-key \
  ghcr.io/open-webui/open-webui:main
```

## Referenční konfigurace

### Proměnné prostředí

| Proměnná | Popis | Výchozí | Příklad |
|----------|-------|---------|---------|
| `MODEL` | Alias modelu k použití | `phi-4-mini` | `qwen2.5-7b` |
| `BASE_URL` | Endpoint Foundry Local | Automaticky detekováno | `http://localhost:51211` |
| `API_KEY` | API klíč (volitelné pro lokální použití) | `""` | `your-api-key` |

## Řešení problémů

### Běžné problémy

**Chainlit Application:**

1. **Služba není dostupná:**
   ```cmd
   # Check Foundry Local status
   foundry service status
   foundry service ps
   
   # Validate API endpoint (note: port 51211)
   curl http://localhost:51211/v1/models
   ```

2. **Konflikty portů:**
   ```cmd
   # Check what's using port 8080
   netstat -ano | findstr :8080
   
   # Use different port if needed
   chainlit run samples\04\app.py -w --port 3000
   ```

3. **Problémy s Python prostředím:**
   ```cmd
   # Verify correct interpreter in VS Code
   # Ctrl+Shift+P → Python: Select Interpreter
   # Choose: Module08/.venv/Scripts/python.exe
   
   # Reinstall dependencies
   pip install -r requirements.txt
   ```

**WebGPU Demo:**

1. **WebGPU není podporováno:**
   - Aktualizujte na Chrome/Edge 113+
   - Aktivujte WebGPU: `chrome://flags/#enable-unsafe-webgpu`
   - Zkontrolujte stav GPU: `chrome://gpu`
   - Demo automaticky přejde na CPU

2. **Chyby při načítání modelu:**
   - Zajistěte připojení k internetu pro stažení modelu
   - Zkontrolujte konzoli prohlížeče kvůli CORS chybám
   - Ověřte, že používáte HTTP (ne file://)

**Open WebUI:**

1. **Spojení odmítnuto:**
   ```cmd
   # Check Docker is running
   docker --version
   
   # Check container status
   docker ps | findstr open-webui
   
   # View container logs
   docker logs open-webui
   ```

2. **Modely se nezobrazují:**
   ```cmd
   # Verify Foundry Local endpoint
   curl http://localhost:51211/v1/models
   
   # Restart Open WebUI
   docker restart open-webui
   ```

### Kontrolní seznam validace

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

## Pokročilé použití

### Optimalizace výkonu

**Chainlit:**
- Používejte streamování pro lepší vnímaný výkon
- Implementujte pooling připojení pro vysokou souběžnost
- Cache odpovědi modelu pro opakované dotazy
- Sledujte využití paměti při dlouhých konverzacích

**WebGPU:**
- Používejte WebGPU pro maximální soukromí a rychlost
- Implementujte kvantizaci modelu pro menší modely
- Používejte Web Workers pro zpracování na pozadí
- Cache kompilované modely v úložišti prohlížeče

**Open WebUI:**
- Používejte trvalé svazky pro historii konverzací
- Konfigurujte limity zdrojů pro Docker kontejner
- Implementujte strategie zálohování uživatelských dat
- Nastavte reverzní proxy pro SSL terminaci

### Vzory integrace

**Hybridní lokální/cloud:**
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

**Multimodální pipeline:**
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

## Produkční nasazení

### Bezpečnostní aspekty

- **API klíče**: Používejte proměnné prostředí, nikdy je nezapisujte přímo do kódu
- **Síť**: Používejte HTTPS v produkci, zvažte VPN pro přístup týmu
- **Řízení přístupu**: Implementujte autentizaci pro Open WebUI
- **Ochrana dat**: Auditujte, která data zůstávají lokálně a která jdou do cloudu
- **Aktualizace**: Udržujte Foundry Local a kontejnery aktuální

### Monitoring a údržba

- **Kontroly stavu**: Implementujte monitoring endpointů
- **Logování**: Centralizujte logy ze všech komponent
- **Metriky**: Sledujte časy odpovědí, míru chyb, využití zdrojů
- **Zálohování**: Pravidelně zálohujte data konverzací a konfigurace

## Odkazy a zdroje

### Dokumentace
- [Chainlit Dokumentace](https://docs.chainlit.io/) - Kompletní průvodce frameworkem
- [Foundry Local Dokumentace](https://learn.microsoft.com/azure/ai-foundry/foundry-local/) - Oficiální dokumentace Microsoftu
- [ONNX Runtime Web](https://onnxruntime.ai/docs/get-started/with-javascript/web.html) - Integrace WebGPU
- [Open WebUI Dokumentace](https://docs.openwebui.com/) - Pokročilá konfigurace

### Ukázkové soubory
- [`app.py`](../../../../../Module08/samples/04/app.py) - Produkční aplikace Chainlit
- [`chainlit_app.ipynb`](./chainlit_app.ipynb) - Edukační notebook
- [`webgpu-demo/`](../../../../../Module08/samples/04/webgpu-demo) - AI inference v prohlížeči
- [`open-webui-guide.md`](./open-webui-guide.md) - Kompletní nastavení Open WebUI

### Související ukázky
- [Dokumentace k sezení 4](../../04.CuttingEdgeModels.md) - Kompletní průvodce sezením
- [Ukázky Foundry Local](https://github.com/microsoft/foundry-local/tree/main/samples) - Oficiální ukázky

---

**Prohlášení**:  
Tento dokument byl přeložen pomocí služby AI pro překlady [Co-op Translator](https://github.com/Azure/co-op-translator). I když se snažíme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za autoritativní zdroj. Pro důležité informace doporučujeme profesionální lidský překlad. Neodpovídáme za žádná nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.
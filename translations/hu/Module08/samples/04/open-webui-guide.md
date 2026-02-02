# Open WebUI + Foundry Local Integrációs Útmutató

Ez az útmutató bemutatja, hogyan csatlakoztathatja az Open WebUI-t a Microsoft Foundry Local-hoz, hogy egy professzionális, ChatGPT-szerű felületet kapjon, amelyet helyi AI modellek működtetnek.

## Áttekintés

Az Open WebUI egy modern, felhasználóbarát chatfelületet kínál, amely bármely OpenAI-kompatibilis API-hoz csatlakoztatható. A Foundry Local-hoz való csatlakoztatással az alábbiakat kapja:

- **Professzionális felület**: ChatGPT-szerű modern dizájn
- **Helyi adatvédelem**: Minden feldolgozás az Ön eszközén történik
- **Modellek váltása**: Egyszerű váltás különböző helyi modellek között
- **Beszélgetési előzmények**: Tartós chatelőzmények és kontextus
- **Fájlok feltöltése**: Dokumentumelemzés és fájlok feldolgozása
- **Egyedi személyiségek**: Rendszerpromptok és szerepkör testreszabása

## Előfeltételek

### Szükséges szoftverek

```cmd
# Verify Foundry Local installation
foundry --version

# Verify Docker installation
docker --version

# Start Foundry Local service
foundry service start
```

### Modell betöltése

```cmd
# List available models
foundry model list

# Load your preferred model
foundry model run phi-4-mini

# Verify model is running
foundry service ps
```

## Gyors beállítás (Ajánlott)

### 1. lépés: Open WebUI futtatása Dockerrel

```cmd
# Pull the latest Open WebUI image
docker pull ghcr.io/open-webui/open-webui:main

# Run Open WebUI connected to Foundry Local
docker run -d \
  --name open-webui \
  -p 3000:8080 \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-local-key \
  -v open-webui-data:/app/backend/data \
  ghcr.io/open-webui/open-webui:main
```

**Windows PowerShell:**
```powershell
docker run -d `
  --name open-webui `
  -p 3000:8080 `
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 `
  -e OPENAI_API_KEY=foundry-local-key `
  -v open-webui-data:/app/backend/data `
  ghcr.io/open-webui/open-webui:main
```

### 2. lépés: Kezdeti beállítás

1. **Böngésző megnyitása**: Nyissa meg a `http://localhost:3000` címet
2. **Fiók létrehozása**: Hozza létre az adminisztrátori felhasználót (az első felhasználó admin lesz)
3. **Kapcsolat ellenőrzése**: A modelleknek automatikusan meg kell jelenniük a legördülő menüben

### 3. lépés: Kapcsolat tesztelése

1. Válassza ki a modellt a legördülő menüből (pl. "phi-4-mini")
2. Írjon egy tesztüzenetet: "Szia! Bemutatnád magad?"
3. A helyi modellnek streaming válaszban kell reagálnia

## Haladó konfiguráció

### Környezeti változók

| Változó | Cél | Alapértelmezett | Példa |
|---------|-----|-----------------|-------|
| `OPENAI_API_BASE_URL` | Foundry Local végpont | - | `http://host.docker.internal:51211/v1` |
| `OPENAI_API_KEY` | API kulcs (szükséges, de helyben nem használatos) | - | `foundry-local-key` |
| `WEBUI_SECRET_KEY` | Munkamenet titkosítási kulcs | automatikusan generált | `your-secret-key` |
| `ENABLE_SIGNUP` | Új felhasználók regisztrációjának engedélyezése | `True` | `False` |

### Manuális konfiguráció (Alternatíva)

Ha a környezeti változók nem működnek, állítsa be manuálisan:

1. **Beállítások megnyitása**: Kattintson a Beállítások (fogaskerék ikon) gombra
2. **Kapcsolatok navigálása**: Beállítások → Kapcsolatok → OpenAI
3. **API adatok beállítása**:
   - API alap URL: `http://host.docker.internal:51211/v1`
   - API kulcs: `foundry-local-key` (bármilyen érték működik)
4. **Mentés és tesztelés**: Kattintson a "Mentés" gombra, majd tesztelje egy modellel

### Tartós adatmentés

A beszélgetések és beállítások megőrzéséhez:

```cmd
# Windows - Create data directory
mkdir %USERPROFILE%\openwebui-data

# Run with persistent storage
docker run -d \
  --name open-webui \
  -p 3000:8080 \
  -v "%USERPROFILE%\openwebui-data:/app/backend/data" \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-local-key \
  ghcr.io/open-webui/open-webui:main
```

## Hibakeresés

### Kapcsolati problémák

**Probléma**: "Kapcsolat megtagadva" vagy a modellek nem töltődnek be

**Megoldások**:
```cmd
# 1. Verify Foundry Local is running
foundry service status
foundry service ps

# 2. Test API endpoint directly
curl http://localhost:51211/v1/models

# 3. Check Docker container logs
docker logs open-webui

# 4. Restart Open WebUI container
docker restart open-webui
```

### Modell nem jelenik meg

**Probléma**: Az Open WebUI nem mutat modelleket a legördülő menüben

**Hibakeresési lépések**:
```cmd
# Check if model is loaded in Foundry Local
foundry model list

# Test API response
curl -X GET http://localhost:51211/v1/models \
  -H "Content-Type: application/json"

# Verify correct port (should be 51211 for Foundry Local)
netstat -ano | findstr :51211
```

**Megoldás**: Győződjön meg róla, hogy a modell megfelelően betöltődött:
```cmd
# Stop and restart model
foundry model stop phi-4-mini
foundry model run phi-4-mini

# Wait for model to fully load, then refresh Open WebUI
```

### Docker hálózati problémák

**Probléma**: `host.docker.internal` nem oldódik fel

**Windows megoldás**:
```cmd
# Use localhost alternative (may need admin privileges)
docker run -d \
  --name open-webui \
  -p 3000:8080 \
  --add-host=host.docker.internal:host-gateway \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-local-key \
  ghcr.io/open-webui/open-webui:main
```

**Alternatíva**: Keresse meg a gép IP-címét:
```cmd
ipconfig | findstr IPv4
# Use your actual IP instead of host.docker.internal
# Example: http://192.168.1.100:51211/v1
```

### Teljesítményproblémák

**Lassú válaszok**:
1. Ellenőrizze, hogy a modell GPU gyorsítást használ-e: `foundry service ps`
2. Győződjön meg róla, hogy elegendő rendszererőforrás áll rendelkezésre (RAM/GPU memória)
3. Teszteléshez használjon kisebb modellt

**Memóriaproblémák**:
```cmd
# Check Docker container memory usage
docker stats open-webui

# Restart Docker if needed
docker restart open-webui
```

## Használati útmutató

### Alapvető chat

1. **Modell kiválasztása**: Válasszon a legördülő menüből (Foundry Local modellek jelennek meg)
2. **Üzenet írása**: Használja az alsó szövegbeviteli mezőt
3. **Küldés**: Nyomja meg az Entert vagy kattintson a Küldés gombra
4. **Válasz megtekintése**: Nézze meg a streaming választ valós időben

### Haladó funkciók

**Fájl feltöltése**:
1. Kattintson a gemkapocs ikonra
2. Töltsön fel dokumentumot (PDF, TXT stb.)
3. Tegyen fel kérdéseket a tartalommal kapcsolatban
4. A modell elemezni fogja és válaszol a dokumentum alapján

**Egyedi rendszerpromptok**:
1. Beállítások → Személyre szabás
2. Állítson be egyedi rendszerpromptot
3. Létrehoz egy következetes AI személyiséget/viselkedést

**Beszélgetés kezelése**:
- **Új chat**: Kattintson a "+" gombra új beszélgetés indításához
- **Chatelőzmények**: Korábbi beszélgetések elérése az oldalsávból
- **Exportálás**: Chatelőzmények letöltése szöveg/JSON formátumban

**Modellek összehasonlítása**:
1. Nyisson meg több böngészőfület ugyanazon az Open WebUI-n
2. Válasszon különböző modelleket minden fülön
3. Hasonlítsa össze a válaszokat ugyanarra a kérdésre

### Integrációs minták

**Fejlesztési munkafolyamat**:
```cmd
# Terminal 1: Start Foundry Local with development model
foundry model run phi-4-mini

# Terminal 2: Start Open WebUI for testing
docker run --rm -p 3000:8080 \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=dev-key \
  ghcr.io/open-webui/open-webui:main

# Terminal 3: Test API directly for debugging
curl -X POST http://localhost:51211/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"model":"phi-4-mini","messages":[{"role":"user","content":"test"}]}'
```

## Éles telepítés

### Biztonságos beállítás

```cmd
# Generate secure secret key
openssl rand -base64 32

# Production deployment with security
docker run -d \
  --name open-webui-prod \
  -p 3000:8080 \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-local-prod \
  -e WEBUI_SECRET_KEY=your-secure-key-here \
  -e ENABLE_SIGNUP=False \
  -v /path/to/secure/storage:/app/backend/data \
  --restart unless-stopped \
  ghcr.io/open-webui/open-webui:main
```

### Többfelhasználós beállítás

```cmd
# Allow controlled user registration
docker run -d \
  --name open-webui-team \
  -p 3000:8080 \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-team \
  -e ENABLE_SIGNUP=True \
  -e WEBUI_SECRET_KEY=team-secret-key \
  -v team-data:/app/backend/data \
  ghcr.io/open-webui/open-webui:main
```

### Felügyelet és naplózás

```cmd
# View real-time logs
docker logs -f open-webui

# Monitor container resources
docker stats open-webui

# Check container health
docker inspect open-webui | grep -i health
```

## Takarítás

```cmd
# Stop Open WebUI
docker stop open-webui

# Remove container
docker rm open-webui

# Remove data volume (WARNING: deletes all chats)
docker volume rm open-webui-data

# Remove image
docker rmi ghcr.io/open-webui/open-webui:main
```

## Következő lépések

### Fejlesztési ötletek

1. **Egyedi modellek**: Adja hozzá saját finomhangolt modelljeit a Foundry Local-hoz
2. **API integráció**: Csatlakozás külső API-khoz az Open WebUI funkcióin keresztül
3. **Dokumentumfeldolgozás**: Állítson be fejlett RAG csatornákat
4. **Multimodális**: Konfiguráljon képelemző modelleket

### Méretezési szempontok

- **Terheléselosztás**: Több Foundry Local példány fordított proxy mögött
- **Modellirányítás**: Különböző modellek különböző felhasználási esetekhez
- **Erőforrás-kezelés**: GPU memória optimalizálása egyidejű felhasználók számára
- **Biztonsági mentési stratégia**: Beszélgetési adatok és konfigurációk rendszeres mentése

## Hivatkozások

- [Open WebUI Dokumentáció](https://docs.openwebui.com/)
- [Open WebUI GitHub Repository](https://github.com/open-webui/open-webui)
- [Foundry Local Dokumentáció](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [Docker Telepítési Útmutató](https://docs.docker.com/get-docker/)

---


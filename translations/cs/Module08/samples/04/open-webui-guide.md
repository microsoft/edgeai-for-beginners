# Open WebUI + Foundry Local Průvodce integrací

Tento průvodce ukazuje, jak propojit Open WebUI s Microsoft Foundry Local pro profesionální rozhraní podobné ChatGPT, poháněné vašimi lokálními AI modely.

## Přehled

Open WebUI poskytuje moderní, uživatelsky přívětivé chatovací rozhraní, které se může připojit k jakémukoliv OpenAI-kompatibilnímu API. Propojením s Foundry Local získáte:

- **Profesionální UI**: Rozhraní podobné ChatGPT s moderním designem
- **Lokální soukromí**: Veškeré zpracování probíhá na vašem zařízení
- **Přepínání modelů**: Snadné přepínání mezi různými lokálními modely
- **Historie konverzací**: Trvalá historie chatu a kontext
- **Nahrávání souborů**: Analýza dokumentů a zpracování souborů
- **Vlastní osobnosti**: Systémové výzvy a přizpůsobení rolí

## Předpoklady

### Požadovaný software

```cmd
# Verify Foundry Local installation
foundry --version

# Verify Docker installation
docker --version

# Start Foundry Local service
foundry service start
```

### Načtení modelu

```cmd
# List available models
foundry model list

# Load your preferred model
foundry model run phi-4-mini

# Verify model is running
foundry service ps
```

## Rychlé nastavení (doporučeno)

### Krok 1: Spusťte Open WebUI pomocí Dockeru

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

### Krok 2: Počáteční nastavení

1. **Otevřete prohlížeč**: Přejděte na `http://localhost:3000`
2. **Vytvořte účet**: Nastavte administrátorského uživatele (první uživatel se stane adminem)
3. **Ověřte připojení**: Modely by se měly automaticky objevit v rozbalovacím menu

### Krok 3: Otestujte připojení

1. Vyberte svůj model z rozbalovacího menu (např. "phi-4-mini")
2. Zadejte testovací zprávu: "Ahoj! Můžeš se představit?"
3. Měli byste vidět streamovanou odpověď od vašeho lokálního modelu

## Pokročilá konfigurace

### Proměnné prostředí

| Proměnná | Účel | Výchozí | Příklad |
|----------|------|---------|---------|
| `OPENAI_API_BASE_URL` | Endpoint Foundry Local | - | `http://host.docker.internal:51211/v1` |
| `OPENAI_API_KEY` | API klíč (vyžadován, ale lokálně nepoužíván) | - | `foundry-local-key` |
| `WEBUI_SECRET_KEY` | Klíč pro šifrování relací | automaticky generováno | `your-secret-key` |
| `ENABLE_SIGNUP` | Povolit registraci nových uživatelů | `True` | `False` |

### Manuální konfigurace (alternativa)

Pokud proměnné prostředí nefungují, nastavte ručně:

1. **Otevřete nastavení**: Klikněte na Nastavení (ikona ozubeného kola)
2. **Přejděte na Připojení**: Nastavení → Připojení → OpenAI
3. **Nastavte detaily API**:
   - Základní URL API: `http://host.docker.internal:51211/v1`
   - API klíč: `foundry-local-key` (jakákoliv hodnota funguje)
4. **Uložte a otestujte**: Klikněte na "Uložit" a poté otestujte s modelem

### Trvalé ukládání dat

Pro uchování konverzací a nastavení:

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

## Řešení problémů

### Problémy s připojením

**Problém**: "Připojení odmítnuto" nebo modely se nenačítají

**Řešení**:
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

### Model se nezobrazuje

**Problém**: Open WebUI nezobrazuje žádné modely v rozbalovacím menu

**Kroky pro ladění**:
```cmd
# Check if model is loaded in Foundry Local
foundry model list

# Test API response
curl -X GET http://localhost:51211/v1/models \
  -H "Content-Type: application/json"

# Verify correct port (should be 51211 for Foundry Local)
netstat -ano | findstr :51211
```

**Oprava**: Ujistěte se, že model je správně načten:
```cmd
# Stop and restart model
foundry model stop phi-4-mini
foundry model run phi-4-mini

# Wait for model to fully load, then refresh Open WebUI
```

### Problémy s Docker sítí

**Problém**: `host.docker.internal` se neřeší

**Řešení pro Windows**:
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

**Alternativa**: Najděte IP adresu vašeho zařízení:
```cmd
ipconfig | findstr IPv4
# Use your actual IP instead of host.docker.internal
# Example: http://192.168.1.100:51211/v1
```

### Problémy s výkonem

**Pomalé odpovědi**:
1. Zkontrolujte, zda model využívá akceleraci GPU: `foundry service ps`
2. Ověřte dostatek systémových prostředků (RAM/paměť GPU)
3. Zvažte použití menšího modelu pro testování

**Problémy s pamětí**:
```cmd
# Check Docker container memory usage
docker stats open-webui

# Restart Docker if needed
docker restart open-webui
```

## Průvodce používáním

### Základní chat

1. **Vyberte model**: Zvolte z rozbalovacího menu (zobrazuje modely Foundry Local)
2. **Zadejte zprávu**: Použijte textové pole dole
3. **Odešlete**: Stiskněte Enter nebo klikněte na tlačítko Odeslat
4. **Zobrazte odpověď**: Sledujte streamovanou odpověď v reálném čase

### Pokročilé funkce

**Nahrávání souborů**:
1. Klikněte na ikonu kancelářské sponky
2. Nahrajte dokument (PDF, TXT, atd.)
3. Pokládejte otázky ohledně obsahu
4. Model analyzuje a odpoví na základě dokumentu

**Vlastní systémové výzvy**:
1. Nastavení → Personalizace
2. Nastavte vlastní systémovou výzvu
3. Vytvoří konzistentní osobnost/chování AI

**Správa konverzací**:
- **Nový chat**: Klikněte na "+" pro zahájení nové konverzace
- **Historie chatu**: Přístup k předchozím konverzacím z postranního panelu
- **Export**: Stáhněte historii chatu jako text/JSON

**Porovnání modelů**:
1. Otevřete více záložek prohlížeče se stejným Open WebUI
2. Vyberte různé modely v každé záložce
3. Porovnejte odpovědi na stejné výzvy

### Vzory integrace

**Vývojový workflow**:
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

## Nasazení do produkce

### Bezpečné nastavení

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

### Nastavení pro více uživatelů

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

### Monitoring a logování

```cmd
# View real-time logs
docker logs -f open-webui

# Monitor container resources
docker stats open-webui

# Check container health
docker inspect open-webui | grep -i health
```

## Úklid

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

## Další kroky

### Nápady na vylepšení

1. **Vlastní modely**: Přidejte své vlastní modely upravené na míru do Foundry Local
2. **API integrace**: Připojte se k externím API prostřednictvím funkcí Open WebUI
3. **Zpracování dokumentů**: Nastavte pokročilé RAG pipeline
4. **Multi-modální**: Konfigurujte modely pro analýzu obrázků

### Úvahy o škálování

- **Load Balancing**: Více instancí Foundry Local za reverzním proxy serverem
- **Směrování modelů**: Různé modely pro různé případy použití
- **Správa zdrojů**: Optimalizace paměti GPU pro současné uživatele
- **Strategie zálohování**: Pravidelné zálohování dat konverzací a konfigurací

## Reference

- [Open WebUI Dokumentace](https://docs.openwebui.com/)
- [Open WebUI GitHub Repository](https://github.com/open-webui/open-webui)
- [Foundry Local Dokumentace](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [Docker Průvodce instalací](https://docs.docker.com/get-docker/)

---


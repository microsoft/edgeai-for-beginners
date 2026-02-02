# Open WebUI + Foundry Local Príručka integrácie

Táto príručka ukazuje, ako prepojiť Open WebUI s Microsoft Foundry Local pre profesionálne rozhranie podobné ChatGPT, poháňané vašimi lokálnymi AI modelmi.

## Prehľad

Open WebUI poskytuje moderné, používateľsky prívetivé chatovacie rozhranie, ktoré sa môže pripojiť k akémukoľvek API kompatibilnému s OpenAI. Prepojením s Foundry Local získate:

- **Profesionálne rozhranie**: Rozhranie podobné ChatGPT s moderným dizajnom
- **Lokálne súkromie**: Všetko spracovanie prebieha na vašom zariadení
- **Prepínanie modelov**: Jednoduché prepínanie medzi rôznymi lokálnymi modelmi
- **História konverzácií**: Trvalá história chatu a kontext
- **Nahrávanie súborov**: Analýza dokumentov a spracovanie súborov
- **Vlastné osobnosti**: Systémové výzvy a prispôsobenie rolí

## Predpoklady

### Požadovaný softvér

```cmd
# Verify Foundry Local installation
foundry --version

# Verify Docker installation
docker --version

# Start Foundry Local service
foundry service start
```

### Načítanie modelu

```cmd
# List available models
foundry model list

# Load your preferred model
foundry model run phi-4-mini

# Verify model is running
foundry service ps
```

## Rýchle nastavenie (odporúčané)

### Krok 1: Spustenie Open WebUI pomocou Dockeru

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

### Krok 2: Počiatočné nastavenie

1. **Otvorte prehliadač**: Prejdite na `http://localhost:3000`
2. **Vytvorte účet**: Nastavte administrátorského používateľa (prvý používateľ sa stane administrátorom)
3. **Overte pripojenie**: Modely by sa mali automaticky zobraziť v rozbaľovacom zozname

### Krok 3: Otestujte pripojenie

1. Vyberte svoj model z rozbaľovacieho zoznamu (napr. "phi-4-mini")
2. Napíšte testovaciu správu: "Ahoj! Môžeš sa predstaviť?"
3. Mali by ste vidieť prúdovú odpoveď od vášho lokálneho modelu

## Pokročilá konfigurácia

### Premenné prostredia

| Premenná | Účel | Predvolené | Príklad |
|----------|---------|---------|----------|
| `OPENAI_API_BASE_URL` | Endpoint Foundry Local | - | `http://host.docker.internal:51211/v1` |
| `OPENAI_API_KEY` | API kľúč (vyžaduje sa, ale lokálne sa nepoužíva) | - | `foundry-local-key` |
| `WEBUI_SECRET_KEY` | Kľúč na šifrovanie relácie | automaticky generovaný | `your-secret-key` |
| `ENABLE_SIGNUP` | Povoliť registráciu nových používateľov | `True` | `False` |

### Manuálna konfigurácia (alternatíva)

Ak premenné prostredia nefungujú, nastavte manuálne:

1. **Otvorte nastavenia**: Kliknite na Nastavenia (ikona ozubeného kolieska)
2. **Prejdite na Pripojenia**: Nastavenia → Pripojenia → OpenAI
3. **Nastavte detaily API**:
   - Základná URL API: `http://host.docker.internal:51211/v1`
   - API kľúč: `foundry-local-key` (akákoľvek hodnota funguje)
4. **Uložte a otestujte**: Kliknite na "Uložiť" a potom otestujte s modelom

### Trvalé ukladanie dát

Na uchovanie konverzácií a nastavení:

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

## Riešenie problémov

### Problémy s pripojením

**Problém**: "Pripojenie odmietnuté" alebo modely sa nenačítavajú

**Riešenia**:
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

### Model sa nezobrazuje

**Problém**: Open WebUI nezobrazuje modely v rozbaľovacom zozname

**Kroky na diagnostiku**:
```cmd
# Check if model is loaded in Foundry Local
foundry model list

# Test API response
curl -X GET http://localhost:51211/v1/models \
  -H "Content-Type: application/json"

# Verify correct port (should be 51211 for Foundry Local)
netstat -ano | findstr :51211
```

**Riešenie**: Uistite sa, že model je správne načítaný:
```cmd
# Stop and restart model
foundry model stop phi-4-mini
foundry model run phi-4-mini

# Wait for model to fully load, then refresh Open WebUI
```

### Problémy so sieťou Dockeru

**Problém**: `host.docker.internal` sa nedá vyriešiť

**Riešenie pre Windows**:
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

**Alternatíva**: Nájdite IP adresu vášho zariadenia:
```cmd
ipconfig | findstr IPv4
# Use your actual IP instead of host.docker.internal
# Example: http://192.168.1.100:51211/v1
```

### Problémy s výkonom

**Pomalé odpovede**:
1. Skontrolujte, či model používa akceleráciu GPU: `foundry service ps`
2. Overte dostatok systémových zdrojov (RAM/pamäť GPU)
3. Zvážte použitie menšieho modelu na testovanie

**Problémy s pamäťou**:
```cmd
# Check Docker container memory usage
docker stats open-webui

# Restart Docker if needed
docker restart open-webui
```

## Príručka používania

### Základný chat

1. **Vyberte model**: Vyberte z rozbaľovacieho zoznamu (zobrazuje modely Foundry Local)
2. **Napíšte správu**: Použite textové pole na spodku
3. **Odošlite**: Stlačte Enter alebo kliknite na tlačidlo Odoslať
4. **Zobrazenie odpovede**: Sledujte prúdovú odpoveď v reálnom čase

### Pokročilé funkcie

**Nahrávanie súborov**:
1. Kliknite na ikonu kancelárskej sponky
2. Nahrajte dokument (PDF, TXT, atď.)
3. Pýtajte sa otázky o obsahu
4. Model analyzuje a odpovedá na základe dokumentu

**Vlastné systémové výzvy**:
1. Nastavenia → Personalizácia
2. Nastavte vlastnú systémovú výzvu
3. Vytvára konzistentnú osobnosť/správanie AI

**Správa konverzácií**:
- **Nový chat**: Kliknite na "+" pre začatie novej konverzácie
- **História chatu**: Prístup k predchádzajúcim konverzáciám z bočného panela
- **Export**: Stiahnite históriu chatu ako text/JSON

**Porovnanie modelov**:
1. Otvorte viacero kariet prehliadača s rovnakým Open WebUI
2. Vyberte rôzne modely v každej karte
3. Porovnajte odpovede na rovnaké výzvy

### Vzory integrácie

**Vývojový pracovný postup**:
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

## Nasadenie do produkcie

### Bezpečné nastavenie

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

### Nastavenie pre viacerých používateľov

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

### Monitorovanie a logovanie

```cmd
# View real-time logs
docker logs -f open-webui

# Monitor container resources
docker stats open-webui

# Check container health
docker inspect open-webui | grep -i health
```

## Vyčistenie

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

## Ďalšie kroky

### Nápady na vylepšenie

1. **Vlastné modely**: Pridajte svoje vlastné jemne doladené modely do Foundry Local
2. **API integrácia**: Pripojte sa k externým API prostredníctvom funkcií Open WebUI
3. **Spracovanie dokumentov**: Nastavte pokročilé RAG pipeline
4. **Multimodálne**: Konfigurujte vizuálne modely na analýzu obrázkov

### Úvahy o škálovaní

- **Vyvažovanie záťaže**: Viacero inštancií Foundry Local za reverzným proxy
- **Smerovanie modelov**: Rôzne modely pre rôzne prípady použitia
- **Správa zdrojov**: Optimalizácia pamäte GPU pre súčasných používateľov
- **Zálohovacia stratégia**: Pravidelné zálohovanie dát konverzácií a konfigurácií

## Referencie

- [Open WebUI Dokumentácia](https://docs.openwebui.com/)
- [Open WebUI GitHub Repository](https://github.com/open-webui/open-webui)
- [Foundry Local Dokumentácia](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [Docker Príručka inštalácie](https://docs.docker.com/get-docker/)

---


# Guida all'integrazione di Open WebUI + Foundry Local

Questa guida mostra come collegare Open WebUI a Microsoft Foundry Local per ottenere un'interfaccia professionale simile a ChatGPT alimentata dai tuoi modelli AI locali.

## Panoramica

Open WebUI offre un'interfaccia chat moderna e intuitiva che può connettersi a qualsiasi API compatibile con OpenAI. Collegandolo a Foundry Local, ottieni:

- **Interfaccia Professionale**: Un'interfaccia simile a ChatGPT con design moderno
- **Privacy Locale**: Tutto il processamento avviene sul tuo dispositivo
- **Cambio Modello**: Passaggio facile tra diversi modelli locali
- **Storico Conversazioni**: Cronologia chat persistente e contesto
- **Caricamento File**: Analisi di documenti e capacità di elaborazione file
- **Personas Personalizzate**: Prompt di sistema e personalizzazione dei ruoli

## Prerequisiti

### Software Necessario

```cmd
# Verify Foundry Local installation
foundry --version

# Verify Docker installation
docker --version

# Start Foundry Local service
foundry service start
```

### Caricare un Modello

```cmd
# List available models
foundry model list

# Load your preferred model
foundry model run phi-4-mini

# Verify model is running
foundry service ps
```

## Configurazione Rapida (Consigliata)

### Passo 1: Avviare Open WebUI con Docker

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

### Passo 2: Configurazione Iniziale

1. **Apri il Browser**: Vai su `http://localhost:3000`
2. **Crea Account**: Configura l'utente admin (il primo utente diventa admin)
3. **Verifica Connessione**: I modelli dovrebbero apparire automaticamente nel menu a tendina

### Passo 3: Testa la Connessione

1. Seleziona il tuo modello dal menu a tendina (es. "phi-4-mini")
2. Scrivi un messaggio di prova: "Ciao! Puoi presentarti?"
3. Dovresti vedere una risposta in streaming dal tuo modello locale

## Configurazione Avanzata

### Variabili d'Ambiente

| Variabile | Scopo | Default | Esempio |
|-----------|-------|---------|---------|
| `OPENAI_API_BASE_URL` | Endpoint di Foundry Local | - | `http://host.docker.internal:51211/v1` |
| `OPENAI_API_KEY` | Chiave API (necessaria ma non utilizzata localmente) | - | `foundry-local-key` |
| `WEBUI_SECRET_KEY` | Chiave di crittografia sessione | auto-generata | `your-secret-key` |
| `ENABLE_SIGNUP` | Permetti registrazione nuovi utenti | `True` | `False` |

### Configurazione Manuale (Alternativa)

Se le variabili d'ambiente non funzionano, configura manualmente:

1. **Apri Impostazioni**: Clicca su Impostazioni (icona ingranaggio)
2. **Vai a Connessioni**: Impostazioni → Connessioni → OpenAI
3. **Imposta Dettagli API**:
   - URL Base API: `http://host.docker.internal:51211/v1`
   - Chiave API: `foundry-local-key` (qualsiasi valore funziona)
4. **Salva e Testa**: Clicca "Salva" e poi testa con un modello

### Archiviazione Dati Persistente

Per conservare conversazioni e impostazioni:

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

## Risoluzione dei Problemi

### Problemi di Connessione

**Problema**: "Connessione rifiutata" o modelli non caricati

**Soluzioni**:
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

### Modello Non Visualizzato

**Problema**: Open WebUI non mostra modelli nel menu a tendina

**Passaggi di Debug**:
```cmd
# Check if model is loaded in Foundry Local
foundry model list

# Test API response
curl -X GET http://localhost:51211/v1/models \
  -H "Content-Type: application/json"

# Verify correct port (should be 51211 for Foundry Local)
netstat -ano | findstr :51211
```

**Soluzione**: Assicurati che il modello sia correttamente caricato:
```cmd
# Stop and restart model
foundry model stop phi-4-mini
foundry model run phi-4-mini

# Wait for model to fully load, then refresh Open WebUI
```

### Problemi di Rete con Docker

**Problema**: `host.docker.internal` non risolve

**Soluzione per Windows**:
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

**Alternativa**: Trova l'IP della tua macchina:
```cmd
ipconfig | findstr IPv4
# Use your actual IP instead of host.docker.internal
# Example: http://192.168.1.100:51211/v1
```

### Problemi di Prestazioni

**Risposte Lente**:
1. Verifica che il modello utilizzi l'accelerazione GPU: `foundry service ps`
2. Controlla che ci siano risorse di sistema sufficienti (RAM/memoria GPU)
3. Considera l'uso di un modello più piccolo per i test

**Problemi di Memoria**:
```cmd
# Check Docker container memory usage
docker stats open-webui

# Restart Docker if needed
docker restart open-webui
```

## Guida all'Uso

### Chat Base

1. **Seleziona Modello**: Scegli dal menu a tendina (mostra modelli di Foundry Local)
2. **Scrivi Messaggio**: Usa il campo di testo in basso
3. **Invia**: Premi Invio o clicca sul pulsante Invia
4. **Visualizza Risposta**: Guarda la risposta in streaming in tempo reale

### Funzionalità Avanzate

**Caricamento File**:
1. Clicca sull'icona della graffetta
2. Carica un documento (PDF, TXT, ecc.)
3. Fai domande sul contenuto
4. Il modello analizzerà e risponderà basandosi sul documento

**Prompt di Sistema Personalizzati**:
1. Impostazioni → Personalizzazione
2. Imposta un prompt di sistema personalizzato
3. Crea una personalità/comportamento AI coerente

**Gestione Conversazioni**:
- **Nuova Chat**: Clicca "+" per iniziare una nuova conversazione
- **Storico Chat**: Accedi alle conversazioni precedenti dalla barra laterale
- **Esporta**: Scarica lo storico chat come testo/JSON

**Confronto Modelli**:
1. Apri più schede del browser con lo stesso Open WebUI
2. Seleziona modelli diversi in ogni scheda
3. Confronta le risposte agli stessi prompt

### Modelli di Integrazione

**Flusso di Lavoro per Sviluppo**:
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

## Distribuzione in Produzione

### Configurazione Sicura

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

### Configurazione Multi-Utente

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

### Monitoraggio e Logging

```cmd
# View real-time logs
docker logs -f open-webui

# Monitor container resources
docker stats open-webui

# Check container health
docker inspect open-webui | grep -i health
```

## Pulizia

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

## Prossimi Passi

### Idee per Miglioramenti

1. **Modelli Personalizzati**: Aggiungi i tuoi modelli ottimizzati a Foundry Local
2. **Integrazione API**: Connetti API esterne tramite le funzioni di Open WebUI
3. **Elaborazione Documenti**: Configura pipeline RAG avanzate
4. **Multi-Modale**: Configura modelli di visione per l'analisi delle immagini

### Considerazioni per la Scalabilità

- **Bilanciamento del Carico**: Istanze multiple di Foundry Local dietro un proxy inverso
- **Instradamento Modelli**: Modelli diversi per casi d'uso differenti
- **Gestione Risorse**: Ottimizzazione della memoria GPU per utenti concorrenti
- **Strategia di Backup**: Backup regolare dei dati delle conversazioni e delle configurazioni

## Riferimenti

- [Documentazione Open WebUI](https://docs.openwebui.com/)
- [Repository GitHub Open WebUI](https://github.com/open-webui/open-webui)
- [Documentazione Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [Guida all'installazione di Docker](https://docs.docker.com/get-docker/)

---


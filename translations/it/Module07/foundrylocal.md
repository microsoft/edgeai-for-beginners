# Foundry Local su Windows e Mac

Questa guida ti aiuta a installare, eseguire e integrare Microsoft Foundry Local su Windows e Mac. Tutti i passaggi e i comandi sono stati convalidati rispetto alla documentazione di Microsoft Learn.

- Inizia: https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started
- Architettura: https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture
- Riferimento CLI: https://learn.microsoft.com/azure/ai-foundry/foundry-local/reference/reference-cli
- Integrare SDK: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks
- Compilare modelli HF (BYOM): https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models
- Windows AI: Locale vs Cloud: https://learn.microsoft.com/windows/ai/cloud-ai#key-decision-factors-for-app-developers

## 1) Installazione / Aggiornamento su Windows

- Installazione:
```cmd
winget install Microsoft.FoundryLocal
```
- Aggiornamento:
```cmd
winget upgrade --id Microsoft.FoundryLocal
```
- Verifica versione:
```cmd
foundry --version
```
     
**Installazione / Mac**

**MacOS**: 
Apri un terminale ed esegui il seguente comando:
```bash
   brew tap microsoft/foundrylocal
   brew install foundrylocal
```

## 2) Nozioni di base sulla CLI (Tre categorie)

- Modello:
```cmd
foundry model --help
foundry model list
foundry model run gpt-oss-20b
```
- Servizio:
```cmd
foundry service --help
foundry service status
foundry service ps
```
- Cache:
```cmd
foundry cache --help
foundry cache list
```

Note:
- Il servizio espone un'API REST compatibile con OpenAI. La porta dell'endpoint è assegnata dinamicamente; usa `foundry service status` per scoprirla.
- Usa gli SDK per comodità; gestiscono automaticamente la scoperta dell'endpoint dove supportato.

## 3) Scoprire l'Endpoint Locale (Porta Dinamica)

Foundry Local assegna una porta dinamica ogni volta che il servizio viene avviato:
```cmd
foundry service status
```
Usa l'`http://localhost:<PORT>` riportato come tuo `base_url` con i percorsi compatibili con OpenAI (ad esempio, `/v1/chat/completions`).

## 4) Test Rapido tramite OpenAI Python SDK

```cmd
set BASE_URL=http://localhost:PORT
python - <<PY
from openai import OpenAI
client = OpenAI(base_url="%BASE_URL%/v1", api_key="")
resp = client.chat.completions.create(
    model="gpt-oss-20b",
    messages=[{"role":"user","content":"Say hello from Foundry Local."}],
    max_tokens=64,
)
print(resp.choices[0].message.content)
PY
```
Riferimenti:
- Integrazione SDK: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

## 5) Porta il Tuo Modello (Compilazione con Olive)

Se hai bisogno di un modello non presente nel catalogo, compilalo in ONNX per Foundry Local utilizzando Olive.

Flusso ad alto livello (vedi documentazione per i passaggi):
```cmd
foundry cache cd models
foundry cache list
foundry model run llama-3.2 --verbose
```
Documentazione:
- Compilazione BYOM: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models

## 6) Risoluzione dei Problemi

- Controlla lo stato del servizio e i log:
```cmd
foundry service status
foundry service diag
```
- Cancella o sposta la cache:
```cmd
foundry cache list
foundry cache remove <model>
foundry cache cd <path>
```
- Aggiorna all'ultima anteprima:
```cmd
winget upgrade --id Microsoft.FoundryLocal
```

## 7) Esperienza Sviluppatore Windows Correlata

- Scelte AI locale vs cloud su Windows, inclusi Foundry Local e Windows ML:
  https://learn.microsoft.com/windows/ai/cloud-ai#key-decision-factors-for-app-developers
- Toolkit AI di VS Code con Foundry Local (usa `foundry service status` per ottenere l'URL dell'endpoint chat):
  https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture#key-components

[Prossimo Sviluppatore Windows](./windowdeveloper.md)

---

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire l'accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un traduttore umano. Non siamo responsabili per eventuali incomprensioni o interpretazioni errate derivanti dall'uso di questa traduzione.
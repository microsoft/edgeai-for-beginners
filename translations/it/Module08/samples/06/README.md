# Sessione 6 Esempio: Modelli come Strumenti

Questo esempio implementa un router minimale + registro di strumenti che seleziona un modello basandosi sul prompt dell'utente e chiama l'endpoint compatibile con OpenAI di Foundry Local.

## File
- `router.py`: registro semplice e routing euristico; scoperta dell'endpoint + controllo dello stato.

## Esecuzione (cmd.exe)
```cmd
cd Module08
.\.venv\Scripts\activate
REM Start whatever models you plan to route to
foundry model run phi-4-mini
foundry model run qwen2.5-7b
foundry model run deepseek-r1-7b

python samples\06\router.py "Explain how local-first AI improves privacy in two sentences."
```

## Note
- Il router utilizza semplici euristiche basate su parole chiave per scegliere tra gli strumenti `general`, `reasoning` e `code` e stampa `/v1/models` all'avvio.
- Configurazione tramite variabili d'ambiente:
```cmd
set BASE_URL=http://localhost:8000
set API_KEY=
REM Override models per tool
set GENERAL_MODEL=phi-4-mini
set REASONING_MODEL=deepseek-r1-7b
set CODE_MODEL=qwen2.5-7b
REM Or provide a full JSON registry
set TOOL_REGISTRY={"general":{"model":"phi-4-mini"},"reasoning":{"model":"deepseek-r1-7b"},"code":{"model":"qwen2.5-7b"}}
```

## Riferimenti
- Foundry Local (Learn): https://learn.microsoft.com/azure/ai-foundry/foundry-local/
- Integrazione con SDK di inferenza: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

---

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire l'accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un traduttore umano. Non siamo responsabili per eventuali incomprensioni o interpretazioni errate derivanti dall'uso di questa traduzione.
# Modulo 08 Esempi: Guida allo Sviluppo Locale di Foundry

## Panoramica

Questa raccolta completa dimostra sia l'approccio con **Foundry Local SDK** che quello con **Comandi Shell** per costruire applicazioni AI pronte per la produzione. Ogni esempio mette in evidenza diversi aspetti dello sviluppo AI edge, dall'integrazione REST di base ai sistemi multi-agente avanzati.

## Approccio di Sviluppo: SDK vs Comandi Shell

### Usa Foundry Local SDK Quando:

- **Controllo Programmatico**: Hai bisogno di pieno controllo sul ciclo di vita degli agenti, sui flussi di valutazione o di distribuzione
- **Strumenti Personalizzati**: Creazione di automazioni attorno a Foundry Local (integrazione CI/CD, orchestrazione multi-agente)
- **Accesso Dettagliato**: Necessità di metadati dettagliati degli agenti, versionamento o controllo del runner di valutazione
- **Integrazione con Python**: Lavori in ambienti fortemente basati su Python o incorpori la logica di Foundry in applicazioni più ampie
- **Flussi di Lavoro Aziendali**: Implementazione di flussi modulari e pipeline di valutazione riproducibili allineati alle architetture di riferimento Microsoft

### Usa Comandi Shell Quando:

- **Test Rapidi**: Esegui test locali rapidi, avvii manuali di agenti o verifiche di configurazione
- **Semplicità CLI**: Hai bisogno di operazioni CLI semplici per avviare/fermare agenti, controllare i log o eseguire valutazioni di base
- **Automazione Leggera**: Script per automazioni semplici senza necessità di integrazione completa con l'SDK
- **Iterazione Rapida**: Cicli di debug e sviluppo, specialmente in ambienti limitati o distribuzioni a livello di gruppo di risorse
- **Configurazione e Validazione**: Configurazione iniziale dell'ambiente e attività di verifica rapide

## Migliori Pratiche e Flusso di Lavoro Raccomandato

Basato sulla gestione del ciclo di vita degli agenti, il tracciamento delle dipendenze e i principi di riproducibilità con privilegi minimi:

### Fase 1: Fondazione e Configurazione
1. **Inizia con i Comandi Shell** per la configurazione iniziale e la validazione rapida
2. **Verifica l'Ambiente** utilizzando strumenti CLI e distribuzione di modelli di base
3. **Testa la Connettività** con chiamate REST semplici e controlli di stato

### Fase 2: Sviluppo e Integrazione
1. **Passa all'SDK** per flussi di lavoro scalabili e tracciabili
2. **Implementa il Controllo Programmatico** per interazioni complesse tra agenti
3. **Crea Strumenti Personalizzati** per modelli pronti per la comunità e integrazione con Azure OpenAI

### Fase 3: Produzione e Scalabilità
1. **Approccio Ibrido** combinando CLI per operazioni e SDK per la logica applicativa
2. **Integrazione Aziendale** con monitoraggio, logging e pipeline di distribuzione
3. **Contributo alla Comunità** attraverso modelli riutilizzabili e migliori pratiche

---

**Clausola di esclusione della responsabilità**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire l'accuratezza, si prega di tenere presente che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un traduttore umano. Non siamo responsabili per eventuali incomprensioni o interpretazioni errate derivanti dall'uso di questa traduzione.
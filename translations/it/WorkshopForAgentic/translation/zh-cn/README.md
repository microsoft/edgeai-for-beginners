<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "aa775a734bda4590ecbe3a94a3b62197",
  "translation_date": "2026-01-05T17:38:32+00:00",
  "source_file": "WorkshopForAgentic/translation/zh-cn/README.md",
  "language_code": "it"
}
-->
# 🎙️ Laboratorio AI Podcast Studio

![logo](../../../../../translated_images/it/logo.8711e39dc8257d7b.png)

## Il tuo compito

Benvenuto in **AI Podcast Studio**! Stai per lanciare il tuo podcast tecnologico "Future Bytes"—ma c'è una svolta: costruirai un team di produzione guidato dall'AI per aiutarti a crearlo. Niente più ricerche infinite, scrittura di script e editing audio. Invece, diventerai un produttore di podcast con superpoteri AI attraverso la programmazione.

## Contesto della storia

Immagina: tu e i tuoi amici volete iniziare un podcast sulle tendenze tecnologiche più cool, ma tutti sono impegnati tra studio, lavoro o vita privata. E se potessi costruire un team di agenti AI intelligenti per fare il lavoro pesante? Un agente che fa ricerca, un altro che scrive script coinvolgenti, un terzo che trasforma il testo in dialoghi naturali e fluidi. Sembra fantascienza? Facciamola diventare realtà.

## Cosa imparerai

Al termine di questo laboratorio, saprai come:
- 🤖 Distribuire il tuo modello AI locale (nessun costo API, nessuna dipendenza dal cloud!)
- 🔧 Costruire agenti AI professionali che collaborano concretamente
- 🎬 Creare un processo completo di produzione podcast da idea ad audio

## Il tuo viaggio: tre atti

Come in una buona storia, abbiamo tre atti. Ogni atto costruirà progressivamente il tuo AI Podcast Studio:

| Capitolo | Il tuo compito | Cosa succede | Competenze sbloccate |
|---------|-----------|--------------|----------------|
| **Atto 1** | [Conosci il tuo assistente AI](01.BuildAIAgentWithSLM.md) | Scoprirai come creare agenti AI capaci di chattare, cercare sul web e persino risolvere problemi. Pensali come stagisti della ricerca che non dormono mai. | 🎯 Costruire il tuo primo agente<br>🛠️ Dotarlo di superpoteri (strumenti!)<br>🧠 Insegnargli a pensare<br>🌐 Collegarlo a Internet |
| **Atto 2** | [Forma il tuo team di produzione](02.AIAgentOrchestrationAndWorkflows.md) | Ora diventa divertente! Coordinerai più agenti AI lavorando insieme come un vero team di podcast. Uno fa ricerca, uno scrive, tu approvi—la collaborazione realizza il sogno. | 🎭 Coordinare più agenti<br>🔄 Costruire flussi di approvazione<br>🖥️ Testare con l'interfaccia DevUI<br>✋ Mantenere il controllo umano |
| **Atto 3** | [Dai vita al tuo podcast](03.Multi-SpeakerPodcastGenerationWithVibeVoice.md) | Gran finale! Trasforma il tuo script in audio podcast reale con voci realistiche e dialoghi naturali. Il tuo podcast "Future Bytes" è pronto per essere pubblicato! | 🎤 Magia del Text-to-Speech<br>👥 Voci multi-parlante<br>⏱️ Audio in formato lungo<br>🚀 Completamente automatizzato |

Ogni atto sblocca nuove abilità. Se sei coraggioso puoi saltare avanti, ma consigliamo di imparare in ordine!

## Requisiti ambientali

Il laboratorio supporta vari ambienti hardware:
- **CPU**: adatto per test e usi su piccola scala
- **GPU**: raccomandato per la produzione, migliora significativamente la velocità di inferenza
- **NPU**: supporta accelerazione con unità neurali di nuova generazione

## Cosa ti serve

### Lista software ✅
- **Python 3.10+** (il tuo linguaggio di programmazione)
- **Ollama** (per far girare i modelli AI sulla tua macchina)
- **VS Code** (il tuo editor di codice)
- **Estensione Python** (per rendere VS Code più smart)
- **Git** (per ottenere il codice)

### Controllo hardware 💻
- **Posso eseguirlo?**: 8GB di RAM, 10GB di spazio libero (può funzionare, ma forse un po’ lento)
- **Configurazione ideale**: 16GB+ RAM, una buona GPU (funzionamento fluido!)
- **Hai una NPU?**: Ancora meglio! Sblocca prestazioni di nuova generazione 🚀

## Costruisci il tuo studio 🎬

### Passo 1: Aggiorna Python

Assicurati di avere Python 3.10 o versione superiore:

```bash
python --version
# Dovrebbe mostrare Python 3.10.x o versione superiore
```

Non hai Python? Prendilo da [python.org](https://python.org)—è gratuito!

### Passo 2: Ottieni Ollama (il motore dei tuoi modelli AI)

Vai su [ollama.ai](https://ollama.ai) e scarica Ollama per il tuo sistema operativo. Pensalo come il motore per far girare i modelli AI in locale.

Controlla se è pronto:

```bash
ollama --version
```

### Passo 3: Scarica il tuo cervello AI 🧠

È ora di ottenere il modello Qwen-3-8B (come assumere il tuo primo assistente AI):

```bash
ollama pull qwen3:8b
```

*Potrebbe richiedere qualche minuto. Il momento perfetto per un caffè!☕*

### Passo 4: Configura VS Code

Se non l’hai già, prendi [Visual Studio Code](https://code.visualstudio.com/). È il miglior editor di codice (discussioni aperte 😄).

### Passo 5: Estensione Python

In VS Code:
1. Premi `Ctrl+Shift+X` (su Mac `Cmd+Shift+X`)
2. Cerca "Python"
3. Installa l’estensione ufficiale Microsoft Python

### Passo 6: Tutto pronto! 🎉

Davvero, sei pronto. Iniziamo a costruire un po’ di magia AI!

### Passo 7: Installa Microsoft Agent Framework e pacchetti correlati 📦

Installa tutte le dipendenze necessarie al laboratorio:

```bash
pip install -r ./Installations/requirements.txt -U
```

*Questo installerà Microsoft Agent Framework e tutti i pacchetti necessari. Prenditi un caffè—l’installazione iniziale potrebbe richiedere qualche minuto!☕*

## Istruzioni del laboratorio

La struttura del progetto, la configurazione e l’esecuzione saranno spiegate passo passo durante il laboratorio.

## Risoluzione problemi (quando qualcosa va storto)🔧

### "Uffa, il download del modello è troppo lento!"
**Soluzione**: Usa una VPN o configura un mirror per Ollama. A volte la rete fa i capricci.

### "Il mio PC sta per cedere! RAM insufficiente!"
**Soluzione**: Passa a un modello più piccolo o regola il parametro `num_ctx` per usare meno memoria. Pensa che è una dieta per il tuo AI.

### "Posso utilizzare la GPU per accelerare?"
**Soluzione**: Ollama riconosce automaticamente la GPU! Assicurati solo che i driver GPU siano aggiornati. Un boost gratuito!🏎️

## Risorse extra (per i curiosi)📚

- [Documentazione Ollama](https://github.com/ollama/ollama) — approfondimenti sui modelli AI locali
- [Microsoft Agent Framework](https://microsoft.github.io/autogen/) — informazioni su come costruire team di agenti intelligenti
- [Info modello Qwen](https://qwenlm.github.io/) — conosci il cervello del tuo assistente AI

## Licenza

Licenza MIT — crea cose fantastiche, condividile e rendi il mondo migliore!🌍

## Vuoi contribuire?

Hai trovato un bug? Hai un’idea? Apri un Issue o una PR! Amiamo la community.✨

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avvertenza**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per garantire l’accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o inesattezze. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche si raccomanda la traduzione professionale umana. Non ci assumiamo responsabilità per eventuali fraintendimenti o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
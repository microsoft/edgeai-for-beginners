<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4ace56b24e2799407b9972a7da6a7517",
  "translation_date": "2025-10-28T21:41:28+00:00",
  "source_file": "Workshop/scripts/README.md",
  "language_code": "it"
}
-->
# Script per il Workshop

Questa directory contiene script di automazione e supporto utilizzati per mantenere la qualità e la coerenza nei materiali del Workshop.

## Contenuti

| File | Scopo |
|------|-------|
| `lint_markdown_cli.py` | Analizza i blocchi di codice Markdown per individuare modelli di comandi obsoleti di Foundry Local CLI. |
| `export_benchmark_markdown.py` | Esegue benchmark di latenza multi-modello e genera report in formato Markdown + JSON. |

## 1. Linter per Pattern CLI in Markdown

`lint_markdown_cli.py` analizza tutti i file `.md` non tradotti per individuare modelli di Foundry Local CLI non consentiti **all'interno di blocchi di codice delimitati** (``` ... ```). È comunque possibile menzionare comandi obsoleti nel testo informativo per contesto storico.

### Pattern Obsoleti (Bloccati nei Blocchi di Codice)

Il linter blocca i modelli CLI obsoleti. Utilizza alternative moderne.

### Sostituzioni Richieste
| Obsoleto | Utilizzare invece |
|----------|-------------------|
| `foundry model chat <a> "..."` | `foundry model run <a> --prompt "..."` |
| `foundry model list --running` | `foundry model list` |
| `foundry model list --cached` | `foundry cache list` |
| `foundry model stats` | Script di benchmark + strumenti di sistema (`Task Manager`, `nvidia-smi`) |
| `foundry model benchmark` | `samples/session03/benchmark_oss_models.py` |
| `foundry model list --available` | `foundry model list` |

### Codici di Uscita
| Codice | Significato |
|--------|-------------|
| 0 | Nessuna violazione rilevata |
| 1 | Uno o più pattern obsoleti trovati |

### Esecuzione Locale
Dalla radice del repository (consigliato):

Windows (PowerShell):
```powershell
python Workshop\scripts\lint_markdown_cli.py --verbose
```

macOS / Linux:
```bash
python Workshop/scripts/lint_markdown_cli.py --verbose
```

### Hook Pre-Commit (Opzionale)
```bash
echo "python Workshop/scripts/lint_markdown_cli.py" > .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```
Questo blocca i commit che introducono pattern obsoleti.

### Integrazione CI
Un workflow GitHub Action (`.github/workflows/markdown-cli-lint.yml`) esegue il linter su ogni push e pull request verso i branch `main` e `Reactor`. I job falliti devono essere corretti prima del merge.

### Aggiungere Nuovi Pattern Obsoleti
1. Apri `lint_markdown_cli.py`.
2. Aggiungi una tupla `(regex, suggestion)` alla lista `DEPRECATED`. Usa una stringa raw e includi i confini di parola `\b` dove appropriato.
3. Esegui il linter localmente per verificare la rilevazione.
4. Effettua il commit e il push; il CI applicherà la nuova regola.

Esempio di aggiunta:
```python
DEPRECATED.append((r"\\bfoundry\\s+experimental\\s+foo\\b", "Remove experimental foo usage"))
```

### Permettere Menzioni Esplicative
Poiché solo i blocchi di codice delimitati sono soggetti a controllo, puoi descrivere i comandi obsoleti nel testo narrativo senza problemi. Se *devi* mostrarli in un blocco delimitato per confronto, utilizza un blocco delimitato **senza** i tre backtick (ad esempio, con rientro o citazione) oppure riscrivi in forma pseudo.

### Saltare File Specifici (Avanzato)
Se necessario, inserisci esempi legacy in un file separato fuori dal repository o rinomina con un'estensione diversa durante la stesura. Gli skip intenzionali per copie tradotte sono automatici (percorsi contenenti `translations`).

### Risoluzione dei Problemi
| Problema | Causa | Soluzione |
|----------|-------|-----------|
| Il linter segnala una riga che hai aggiornato | Regex troppo generico | Restringi il pattern con ulteriori confini di parola (`\b`) o ancore |
| Il CI fallisce ma localmente funziona | Versione di Python diversa o modifiche non salvate | Riesegui localmente, assicurati che la working tree sia pulita, controlla la versione di Python del workflow (3.11) |
| Necessità di bypass temporaneo | Correzione urgente | Applica la correzione immediatamente dopo; considera l'uso di un branch temporaneo e un PR successivo (evita di aggiungere switch di bypass) |

### Motivazione
Mantenere la documentazione allineata con la superficie CLI *stabile* attuale previene difficoltà durante il workshop, evita confusione per i partecipanti e centralizza la misurazione delle prestazioni attraverso script Python mantenuti invece di comandi CLI obsoleti.

---
Manutenuto come parte della toolchain di qualità del workshop. Per miglioramenti (ad esempio, suggerimenti di correzione automatica o generazione di report HTML), apri un issue o invia un PR.

## 2. Script di Validazione dei Campioni

`validate_samples.py` valida tutti i file di esempio Python per verificarne la sintassi, gli import e la conformità alle migliori pratiche.

### Utilizzo
```bash
# Validate all samples
python scripts/validate_samples.py

# Validate specific session
python scripts/validate_samples.py --session 01

# Verbose mode (includes best practice warnings)
python scripts/validate_samples.py --verbose

# Summary only
python scripts/validate_samples.py --summary
```

### Cosa Controlla
- ✅ Validità della sintassi Python
- ✅ Import richiesti presenti
- ✅ Implementazione della gestione degli errori (modalità dettagliata)
- ✅ Utilizzo di annotazioni di tipo (modalità dettagliata)
- ✅ Docstring delle funzioni (modalità dettagliata)
- ✅ Link di riferimento SDK (modalità dettagliata)

### Variabili d'Ambiente
- `SKIP_IMPORT_CHECK=1` - Salta la validazione degli import
- `SKIP_SYNTAX_CHECK=1` - Salta la validazione della sintassi

### Codici di Uscita
- `0` - Tutti i campioni hanno superato la validazione
- `1` - Uno o più campioni non hanno superato la validazione

## 3. Runner di Test per i Campioni

`test_samples.py` esegue test di verifica su tutti i campioni per assicurarsi che vengano eseguiti senza errori.

### Utilizzo
```bash
# Test all samples
python scripts/test_samples.py

# Test specific session
python scripts/test_samples.py --session 01

# Quick mode (shorter timeouts)
python scripts/test_samples.py --quick

# Verbose mode (show output)
python scripts/test_samples.py --verbose
```

### Prerequisiti
- Servizio Foundry Local in esecuzione: `foundry service start`
- Modelli caricati: `foundry model run phi-4-mini`
- Dipendenze installate: `pip install -r requirements.txt`

### Cosa Testa
- ✅ Il campione può essere eseguito senza errori di runtime
- ✅ Viene generato l'output richiesto
- ✅ Gestione corretta degli errori in caso di fallimento
- ✅ Prestazioni (tempo di esecuzione)

### Variabili d'Ambiente
- `FOUNDRY_LOCAL_ALIAS=phi-4-mini` - Modello da utilizzare per il test
- `TEST_TIMEOUT=30` - Timeout per campione in secondi

### Fallimenti Previsti
Alcuni test potrebbero fallire se le dipendenze opzionali non sono installate (ad esempio, `ragas`, `sentence-transformers`). Installa con:
```bash
pip install sentence-transformers ragas datasets
```

### Codici di Uscita
- `0` - Tutti i test superati
- `1` - Uno o più test falliti

## 4. Esportatore di Benchmark Markdown

Script: `export_benchmark_markdown.py`

Genera una tabella di prestazioni riproducibile per un set di modelli.

### Utilizzo
```powershell
python Workshop\scripts\export_benchmark_markdown.py --models "qwen2.5-0.5b" --prompt "Explain retrieval augmented generation briefly." --rounds 3 --output benchmark_report.md
```

### Output
| File | Descrizione |
|------|-------------|
| `benchmark_report.md` | Tabella Markdown (media, p95, token/sec, primo token opzionale) |
| `benchmark_report.json` | Array di metriche grezze per differenze e storico |

### Opzioni
| Flag | Descrizione | Default |
|------|-------------|---------|
| `--models` | Alias dei modelli separati da virgola | (obbligatorio) |
| `--prompt` | Prompt utilizzato per ogni round | (obbligatorio) |
| `--rounds` | Round per modello | 3 |
| `--output` | File di output Markdown | `benchmark_report.md` |
| `--json` | File di output JSON | `benchmark_report.json` |
| `--fail-on-empty` | Uscita non zero se tutti i benchmark falliscono | disattivato |

La variabile d'ambiente `BENCH_STREAM=1` aggiunge la misurazione della latenza del primo token.

### Note
- Riutilizza `workshop_utils` per un bootstrap e una cache dei modelli coerenti.
- Se eseguito da una directory di lavoro diversa, lo script tenta fallback di percorso per individuare `workshop_utils`.
- Per il confronto GPU: esegui una volta, abilita l'accelerazione tramite configurazione CLI, riesegui e confronta il JSON.

---

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire l'accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale umana. Non siamo responsabili per eventuali incomprensioni o interpretazioni errate derivanti dall'uso di questa traduzione.
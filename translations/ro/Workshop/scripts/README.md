# Scripturi Workshop

Acest director conține scripturi de automatizare și suport utilizate pentru a menține calitatea și consistența materialelor Workshop-ului.

## Conținut

| Fișier | Scop |
|--------|------|
| `lint_markdown_cli.py` | Verifică blocurile de cod Markdown pentru a bloca modelele de comenzi CLI Foundry Local depreciate. |
| `export_benchmark_markdown.py` | Rulează benchmark-uri de latență multi-model și generează rapoarte în format Markdown + JSON. |

## 1. Linter pentru Modele CLI Markdown

`lint_markdown_cli.py` scanează toate fișierele `.md` care nu sunt traduceri pentru modelele CLI Foundry Local nepermise **în interiorul blocurilor de cod delimitate** (``` ... ```). Proza informativă poate menționa în continuare comenzile depreciate pentru context istoric.

### Modele Depreciate (Blocate în Interiorul Blocurilor de Cod)

Linter-ul blochează modelele CLI depreciate. Utilizați alternativele moderne în locul acestora.

### Înlocuiri Necesare
| Depreciat | Utilizați În Loc |
|-----------|------------------|
| `foundry model chat <a> "..."` | `foundry model run <a> --prompt "..."` |
| `foundry model list --running` | `foundry model list` |
| `foundry model list --cached` | `foundry cache list` |
| `foundry model stats` | Script de benchmark + instrumente de sistem (`Task Manager`, `nvidia-smi`) |
| `foundry model benchmark` | `samples/session03/benchmark_oss_models.py` |
| `foundry model list --available` | `foundry model list` |

### Coduri de Ieșire
| Cod | Semnificație |
|-----|--------------|
| 0 | Nicio încălcare detectată |
| 1 | Unul sau mai multe modele depreciate găsite |

### Rulare Locală
Din rădăcina depozitului (recomandat):

Windows (PowerShell):
```powershell
python Workshop\scripts\lint_markdown_cli.py --verbose
```

macOS / Linux:
```bash
python Workshop/scripts/lint_markdown_cli.py --verbose
```

### Hook Pre-Commit (Opțional)
```bash
echo "python Workshop/scripts/lint_markdown_cli.py" > .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```
Acest lucru blochează commit-urile care introduc modele depreciate.

### Integrare CI
Un workflow GitHub Action (`.github/workflows/markdown-cli-lint.yml`) rulează linter-ul la fiecare push și pull request către ramurile `main` și `Reactor`. Joburile eșuate trebuie rezolvate înainte de a fi integrate.

### Adăugarea de Noi Modele Depreciate
1. Deschideți `lint_markdown_cli.py`.
2. Adăugați un tuplu `(regex, suggestion)` la lista `DEPRECATED`. Utilizați un șir brut și includeți limite de cuvinte `\b` acolo unde este cazul.
3. Rulați linter-ul local pentru a verifica detectarea.
4. Faceți commit și push; CI va aplica noua regulă.

Exemplu de adăugare:
```python
DEPRECATED.append((r"\\bfoundry\\s+experimental\\s+foo\\b", "Remove experimental foo usage"))
```

### Permisiunea Menționării Explicative
Deoarece doar blocurile de cod delimitate sunt verificate, puteți descrie în siguranță comenzile depreciate în text narativ. Dacă *trebuie* să le afișați într-un bloc delimitat pentru contrast, adăugați un bloc delimitat **fără** triple backticks (de exemplu, indentare sau citare) sau rescrieți într-o formă pseudo.

### Omiterea Fișierelor Specifice (Avansat)
Dacă este necesar, înfășurați exemplele vechi într-un fișier separat în afara depozitului sau redenumiți-l cu o extensie diferită în timpul redactării. Omiterea intenționată pentru copii traduse este automată (căi care conțin `translations`).

### Depanare
| Problemă | Cauză | Rezolvare |
|----------|-------|----------|
| Linter-ul semnalează o linie pe care ați actualizat-o | Regex prea general | Restrângeți modelul cu limite de cuvinte suplimentare (`\b`) sau ancore |
| CI eșuează, dar local trece | Versiune Python diferită sau modificări necomise | Rulați din nou local, asigurați-vă că arborele de lucru este curat, verificați versiunea Python din workflow (3.11) |
| Necesitatea de a ocoli temporar | Remediere urgentă | Aplicați remedierea imediat după; luați în considerare utilizarea unei ramuri temporare și a unui PR ulterior (evitați adăugarea de comutatoare de ocolire) |

### Motivație
Menținerea documentației aliniate cu suprafața CLI *actuală* stabilă previne fricțiunile în workshop, evită confuzia participanților și centralizează măsurarea performanței prin scripturi Python întreținute, în loc de subcomenzi CLI învechite.

---
Întreținut ca parte a lanțului de instrumente pentru calitatea workshop-ului. Pentru îmbunătățiri (de exemplu, sugestii de auto-corectare sau generarea de rapoarte HTML), deschideți un issue sau trimiteți un PR.

## 2. Script de Validare a Exemplarelor

`validate_samples.py` validează toate fișierele de exemplu Python pentru validitatea sintaxei, importuri și conformitatea cu cele mai bune practici.

### Utilizare
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

### Ce verifică
- ✅ Validitatea sintaxei Python
- ✅ Prezența importurilor necesare
- ✅ Implementarea gestionării erorilor (mod verbose)
- ✅ Utilizarea tipurilor (mod verbose)
- ✅ Docstrings pentru funcții (mod verbose)
- ✅ Linkuri de referință SDK (mod verbose)

### Variabile de Mediu
- `SKIP_IMPORT_CHECK=1` - Omiterea validării importurilor
- `SKIP_SYNTAX_CHECK=1` - Omiterea validării sintaxei

### Coduri de Ieșire
- `0` - Toate exemplarele au trecut validarea
- `1` - Unul sau mai multe exemplare au eșuat

## 3. Runner de Testare a Exemplarelor

`test_samples.py` rulează teste rapide pe toate exemplarele pentru a verifica dacă se execută fără erori.

### Utilizare
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

### Cerințe Prealabile
- Serviciul Foundry Local activ: `foundry service start`
- Modele încărcate: `foundry model run phi-4-mini`
- Dependențe instalate: `pip install -r requirements.txt`

### Ce testează
- ✅ Exemplarul se poate executa fără erori de runtime
- ✅ Se generează output-ul necesar
- ✅ Gestionarea corectă a erorilor în caz de eșec
- ✅ Performanță (timp de execuție)

### Variabile de Mediu
- `FOUNDRY_LOCAL_ALIAS=phi-4-mini` - Modelul utilizat pentru testare
- `TEST_TIMEOUT=30` - Timeout per exemplu în secunde

### Eșecuri Așteptate
Unele teste pot eșua dacă dependențele opționale nu sunt instalate (de exemplu, `ragas`, `sentence-transformers`). Instalați cu:
```bash
pip install sentence-transformers ragas datasets
```

### Coduri de Ieșire
- `0` - Toate testele au trecut
- `1` - Unul sau mai multe teste au eșuat

## 4. Exportator de Benchmark Markdown

Script: `export_benchmark_markdown.py`

Generează un tabel de performanță reproductibil pentru un set de modele.

### Utilizare
```powershell
python Workshop\scripts\export_benchmark_markdown.py --models "qwen2.5-0.5b" --prompt "Explain retrieval augmented generation briefly." --rounds 3 --output benchmark_report.md
```

### Output-uri
| Fișier | Descriere |
|--------|-----------|
| `benchmark_report.md` | Tabel Markdown (medie, p95, tokens/sec, opțional primul token) |
| `benchmark_report.json` | Array de metrici brute pentru comparare & istoric |

### Opțiuni
| Flag | Descriere | Implicit |
|------|-----------|----------|
| `--models` | Alias-uri de modele separate prin virgulă | (obligatoriu) |
| `--prompt` | Prompt utilizat la fiecare rundă | (obligatoriu) |
| `--rounds` | Runde per model | 3 |
| `--output` | Fișier de output Markdown | `benchmark_report.md` |
| `--json` | Fișier de output JSON | `benchmark_report.json` |
| `--fail-on-empty` | Ieșire non-zero dacă toate benchmark-urile eșuează | dezactivat |

Variabila de mediu `BENCH_STREAM=1` adaugă măsurarea latenței primului token.

### Note
- Reutilizează `workshop_utils` pentru bootstrap și caching consistent al modelelor.
- Dacă este rulat dintr-un alt director de lucru, scriptul încearcă fallback-uri de cale pentru a localiza `workshop_utils`.
- Pentru comparația GPU: rulați o dată, activați accelerarea prin configurarea CLI, rulați din nou și comparați JSON-ul.

---

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să asigurăm acuratețea, vă rugăm să fiți conștienți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa natală ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de oameni. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.
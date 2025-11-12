<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "04951692a100dcd716df01efca2d3f0d",
  "translation_date": "2025-11-12T01:03:40+00:00",
  "source_file": "Workshop/Readme.md",
  "language_code": "et"
}
-->
# EdgeAI algajatele - Töötuba

> **Praktiline õppeprogramm tootmisvalmis Edge AI rakenduste loomiseks**
>
> Valda kohaliku AI kasutuselevõttu Microsoft Foundry Local abil, alates esimesest vestlusest kuni mitme agendi orkestreerimiseni 6 järjestikuses sessioonis.

---

## 🎯 Sissejuhatus

Tere tulemast **EdgeAI algajatele töötuppa** - praktiline juhend intelligentsete rakenduste loomiseks, mis töötavad täielikult kohalikul riistvaral. See töötuba muudab teoreetilised Edge AI kontseptsioonid praktilisteks oskusteks, kasutades Microsoft Foundry Locali ja väikeseid keelemudeleid (SLM).

### Miks see töötuba?

**Edge AI revolutsioon on käes**

Organisatsioonid üle maailma liiguvad pilvepõhisest AI-st serva arvutamisele kolme olulise põhjuse tõttu:

1. **Privaatsus ja vastavus** - Töötle tundlikke andmeid kohapeal ilma pilve edastamata (HIPAA, GDPR, finantsregulatsioonid)
2. **Jõudlus** - Väldi võrgu latentsust (50-500ms kohalik vs 500-2000ms pilve ringreis)
3. **Kulude kontroll** - Eemalda API kulud ja skaleeri ilma pilvekuludeta

**Kuid Edge AI on erinev**

AI käitamine kohapeal nõuab uusi oskusi:
- Mudeli valik ja optimeerimine ressursipiirangute jaoks
- Kohalike teenuste haldamine ja riistvara kiirendus
- Väiksemate mudelite jaoks tõhusate käskude kujundamine
- Tootmise juurutamise mustrid servaseadmetele

**See töötuba annab need oskused**

6 keskendunud sessioonis (~3 tundi kokku) liigud "Hello World"-ist tootmisvalmis mitme agendi süsteemide juurutamiseni - kõik töötavad kohapeal sinu masinas.

---

## 📚 Õpieesmärgid

Töötuba läbides suudad:

### Põhioskused
1. **Kohalike AI teenuste juurutamine ja haldamine**
   - Paigalda ja konfigureeri Microsoft Foundry Local
   - Vali sobivad mudelid serva juurutamiseks
   - Halda mudeli elutsüklit (allalaadimine, laadimine, vahemälu)
   - Jälgi ressursikasutust ja optimeeri jõudlust

2. **AI-põhiste rakenduste loomine**
   - Rakenda OpenAI-ga ühilduvaid vestluste lõpetamisi kohapeal
   - Kujunda tõhusaid käsklusi väikeste keelemudelite jaoks
   - Töötle voogesituse vastuseid parema kasutajakogemuse jaoks
   - Integreeri kohalikud mudelid olemasolevatesse rakendustesse

3. **RAG (Retrieval Augmented Generation) süsteemide loomine**
   - Loo semantiline otsing sisestustega
   - Siduda LLM vastused valdkonnaspetsiifiliste teadmistega
   - Hinda RAG kvaliteeti tööstusharu standardsete mõõdikute abil
   - Skaleeri prototüübist tootmiseni

4. **Mudeli jõudluse optimeerimine**
   - Võrdle mitut mudelit oma kasutusjuhtumi jaoks
   - Mõõda latentsust, läbilaskevõimet ja esimese tokeni aega
   - Vali optimaalsed mudelid kiiruse/kvaliteedi kompromisside alusel
   - Võrdle SLM vs LLM kompromisse reaalsetes stsenaariumides

5. **Mitme agendi süsteemide orkestreerimine**
   - Kujunda spetsialiseeritud agendid erinevateks ülesanneteks
   - Rakenda agendi mälu ja konteksti haldamist
   - Koordineeri agente keerulistes töövoogudes
   - Suuna päringuid intelligentselt mitme mudeli vahel

6. **Tootmisvalmis lahenduste juurutamine**
   - Rakenda veakäsitlust ja uuesti proovimise loogikat
   - Jälgi tokenite kasutust ja süsteemi ressursse
   - Loo skaleeritavaid arhitektuure mudel-tööriistade mustritega
   - Planeeri migratsiooniteed servast hübriidile (serv + pilv)

---

## 🎓 Õpitulemused

### Mida sa lood

Töötoa lõpuks oled loonud:

| Sessioon | Tulemus | Näidatud oskused |
|----------|---------|------------------|
| **1** | Vestlusrakendus voogesitusega | Teenuse seadistamine, põhilised lõpetamised, voogesituse UX |
| **2** | RAG süsteem hindamisega | Sisestused, semantiline otsing, kvaliteedimõõdikud |
| **3** | Mitme mudeli võrdluskomplekt | Jõudluse mõõtmine, mudelite võrdlemine |
| **4** | SLM vs LLM võrdleja | Kompromisside analüüs, optimeerimisstrateegiad |
| **5** | Mitme agendi orkestreerija | Agendi kujundus, mälu haldamine, koordineerimine |
| **6** | Intelligente suunamissüsteem | Kavatsuste tuvastamine, mudeli valik, skaleeritavus |

### Kompetentsuse maatriks

| Oskuste tase | Sessioonid 1-2 | Sessioonid 3-4 | Sessioonid 5-6 |
|--------------|---------------|---------------|---------------|
| **Algaja** | ✅ Seadistamine ja põhitõed | ⚠️ Väljakutseid pakkuv | ❌ Liiga keeruline |
| **Kesktase** | ✅ Kiire ülevaade | ✅ Põhiõpe | ⚠️ Venitus eesmärgid |
| **Edasijõudnud** | ✅ Lihtne läbida | ✅ Täiendamine | ✅ Tootmismustrid |

### Karjäärivalmis oskused

**Pärast seda töötuba oled valmis:**

✅ **Looma privaatsus-esimesi rakendusi**
- Tervishoiurakendused, mis töötlevad PHI/PII kohapeal
- Finantsteenused vastavusnõuetega
- Valitsussüsteemid andmesuveräänsuse vajadustega

✅ **Optimeerima servakeskkondi**
- IoT seadmed piiratud ressurssidega
- Offline-esimesed mobiilirakendused
- Madala latentsusega reaalajas süsteemid

✅ **Kujundama intelligentseid arhitektuure**
- Mitme agendi süsteemid keeruliste töövoogude jaoks
- Hübriid serv-pilv juurutused
- Kuluefektiivne AI infrastruktuur

✅ **Juhtima Edge AI algatusi**
- Hinda Edge AI teostatavust projektide jaoks
- Vali sobivad mudelid ja raamistikud
- Kujunda skaleeritavaid kohalikke AI lahendusi

---

## 🗺️ Töötoa struktuur

### Sessioonide ülevaade (6 sessiooni × 30 minutit = 3 tundi)

| Sessioon | Teema | Fookus | Kestus |
|----------|-------|-------|--------|
| **1** | Foundry Localiga alustamine | Paigaldamine, valideerimine, esimesed lõpetamised | 30 min |
| **2** | AI lahenduste loomine RAG-iga | Käskude kujundamine, sisestused, hindamine | 30 min |
| **3** | Avatud lähtekoodiga mudelid | Mudelite avastamine, võrdlemine, valik | 30 min |
| **4** | Tipptasemel mudelid | SLM vs LLM, optimeerimine, raamistikud | 30 min |
| **5** | AI-põhised agendid | Agendi kujundus, orkestreerimine, mälu | 30 min |
| **6** | Mudelid tööriistadena | Suunamine, ahelad, skaleerimisstrateegiad | 30 min |

---

## 🚀 Kiire algus

### Eeltingimused

**Süsteeminõuded:**
- **OS**: Windows 10/11, macOS 11+ või Linux (Ubuntu 20.04+)
- **RAM**: Minimaalselt 8GB, soovitatavalt 16GB+
- **Salvestusruum**: 10GB+ vaba ruumi mudelite jaoks
- **CPU**: Kaasaegne protsessor AVX2 toega
- **GPU** (valikuline): CUDA-ühilduv või Qualcomm NPU kiirenduseks

**Tarkvaranõuded:**
- **Python 3.8+** ([Laadi alla](https://www.python.org/downloads/))
- **Microsoft Foundry Local** ([Paigaldusjuhend](../../../Workshop))
- **Git** ([Laadi alla](https://git-scm.com/downloads))
- **Visual Studio Code** (soovitatav) ([Laadi alla](https://code.visualstudio.com/))

### Seadistamine 3 sammuga

#### 1. Paigalda Foundry Local

**Windows:**
```powershell
winget install Microsoft.FoundryLocal
```

**macOS:**
```bash
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**Paigalduse kontrollimine:**
```bash
foundry --version
foundry service status
```

**Veendu, et Azure AI Foundry Local töötab fikseeritud portiga**

```bash
# Set FoundryLocal to use port 58123 (default)
foundry service set --port 58123 --show

# Or use a different port
foundry service set --port 58000 --show
```

**Kontrolli toimimist:**
```bash
# Check service status
foundry service status

# Test the endpoint
curl http://127.0.0.1:58123/v1/models
```
**Saadaval olevate mudelite leidmine**
Et näha, millised mudelid on saadaval sinu Foundry Local instantsis, saad päringu teha mudelite lõpp-punkti:

```bash
# cmd/bash/powershell
foundry model list
```

Veebipõhise lõpp-punkti kasutamine 

```bash
# Windows PowerShell
powershell -Command "Invoke-RestMethod -Uri 'http://127.0.0.1:58123/v1/models' -Method Get"

# Or using curl (if available)
curl http://127.0.0.1:58123/v1/models
```

#### 2. Klooni repositoorium ja paigalda sõltuvused

```bash
# Clone repository
git clone https://github.com/microsoft/edgeai-for-beginners.git
cd edgeai-for-beginners/Workshop

# Create virtual environment
python -m venv .venv

# Activate virtual environment
# Windows:
.\.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

#### 3. Käivita oma esimene näidis

```bash
# Start Foundry Local and load a model
foundry model run phi-4-mini

# Run the chat bootstrap sample
cd samples
python -m session01.chat_bootstrap "What is edge AI?"
```

**✅ Õnnestus!** Sa peaksid nägema voogesituse vastust Edge AI kohta.

---

## 📦 Töötoa ressursid

### Python näidised

Järjestikused praktilised näited, mis demonstreerivad iga kontseptsiooni:

| Sessioon | Näidis | Kirjeldus | Käitusaeg |
|----------|--------|-----------|-----------|
| 1 | [`chat_bootstrap.py`](../../../Workshop/samples/session01/chat_bootstrap.py) | Põhiline ja voogesituse vestlus | ~30s |
| 2 | [`rag_pipeline.py`](../../../Workshop/samples/session02/rag_pipeline.py) | RAG sisestustega | ~45s |
| 2 | [`rag_eval_ragas.py`](../../../Workshop/samples/session02/rag_eval_ragas.py) | RAG kvaliteedi hindamine | ~60s |
| 3 | [`benchmark_oss_models.py`](../../../Workshop/samples/session03/benchmark_oss_models.py) | Mitme mudeli võrdlemine | ~2-3m |
| 4 | [`model_compare.py`](../../../Workshop/samples/session04/model_compare.py) | SLM vs LLM võrdlus | ~45s |
| 5 | [`agents_orchestrator.py`](../../../Workshop/samples/session05/agents_orchestrator.py) | Mitme agendi süsteem | ~60s |
| 6 | [`models_router.py`](../../../Workshop/samples/session06/models_router.py) | Kavatsuste põhine suunamine | ~45s |
| 6 | [`models_pipeline.py`](../../../Workshop/samples/session06/models_pipeline.py) | Mitmeastmeline torustik | ~60s |

### Jupyter Notebookid

Interaktiivne uurimine koos selgituste ja visualisatsioonidega:

| Sessioon | Notebook | Kirjeldus | Raskusaste |
|----------|----------|-----------|------------|
| 1 | [`session01_chat_bootstrap.ipynb`](./notebooks/session01_chat_bootstrap.ipynb) | Vestluse põhitõed ja voogesitus | ⭐ Algaja |
| 2 | [`session02_rag_pipeline.ipynb`](./notebooks/session02_rag_pipeline.ipynb) | RAG süsteemi loomine | ⭐⭐ Kesktase |
| 2 | [`session02_rag_eval_ragas.ipynb`](./notebooks/session02_rag_eval_ragas.ipynb) | RAG kvaliteedi hindamine | ⭐⭐ Kesktase |
| 3 | [`session03_benchmark_oss_models.ipynb`](./notebooks/session03_benchmark_oss_models.ipynb) | Mudelite võrdlemine | ⭐⭐ Kesktase |
| 4 | [`session04_model_compare.ipynb`](./notebooks/session04_model_compare.ipynb) | Mudelite võrdlus | ⭐⭐ Kesktase |
| 5 | [`session05_agents_orchestrator.ipynb`](./notebooks/session05_agents_orchestrator.ipynb) | Agendi orkestreerimine | ⭐⭐⭐ Edasijõudnud |
| 6 | [`session06_models_router.ipynb`](./notebooks/session06_models_router.ipynb) | Kavatsuste suunamine | ⭐⭐⭐ Edasijõudnud |
| 6 | [`session06_models_pipeline.ipynb`](./notebooks/session06_models_pipeline.ipynb) | Torustiku orkestreerimine | ⭐⭐⭐ Edasijõudnud |

### Dokumentatsioon

Põhjalikud juhendid ja viited:

| Dokument | Kirjeldus | Kasuta millal |
|----------|-----------|---------------|
| [QUICK_START.md](./QUICK_START.md) | Kiire seadistamise juhend | Alustades nullist |
| [QUICK_REFERENCE.md](./QUICK_REFERENCE.md) | Käskude ja API kiirviide | Vajad kiireid vastuseid |
| [FOUNDRY_SDK_QUICKREF.md](./FOUNDRY_SDK_QUICKREF.md) | SDK mustrid ja näited | Koodi kirjutamine |
| [ENV_CONFIGURATION.md](./ENV_CONFIGURATION.md) | Keskkonnamuutujate juhend | Näidiste konfigureerimine |
| [notebooks/TROUBLESHOOTING.md](./notebooks/TROUBLESHOOTING.md) | Levinud probleemid ja lahendused | Tõrkeotsing |

---

## 🎓 Õppeprogrammi soovitused

### Algajatele (3-4 tundi)
1. ✅ Sessioon 1: Alustamine (keskendu seadistamisele ja põhilisele vestlusele)
2. ✅ Sessioon 2: RAG põhitõed (jäta hindamine esialgu vahele)
3. ✅ Sessioon 3: Lihtne võrdlemine (ainult 2 mudelit)
4. ⏭️ Jäta sessioonid 4-6 esialgu vahele
5. 🔄 Naase sessioonide 4-6 juurde pärast esimese rakenduse loomist

### Kesktasemel arendajatele (3 tundi)
1. ⚡ Sessioon 1: Kiire seadistuse valideerimine
2. ✅ Sessioon 2: Täielik RAG torustik koos hindamisega
3. ✅ Sessioon 3: Täielik võrdluskomplekt
4. ✅ Sessioon 4: Mudeli optimeerimine
5. ✅ Sessioonid 5-6: Keskendu arhitektuurimustritele

### Edasijõudnud praktikutele (2-3 tundi)
1. ⚡ Sessioonid 1-3: Kiire ülevaade ja valideerimine
2. ✅ Sessioon 4: Optimeerimise süvauuring
3. ✅ Sessioon 5: Mitme agendi arhitektuur
4. ✅ Sessioon 6: Tootmismustrid ja skaleerimine
5. 🚀 Laienda: Loo kohandatud suunamisloogika ja hübriidjuurutused

---

## Töötoa sessioonipakett (Keskendunud 30-minutilised laborid)

Kui järgite tihendatud 6-sessioonilist töötoa formaati, kasutage neid spetsiaalseid juhendeid (igaüks vastab ja täiendab laiemat mooduli dokumentatsiooni ülal):

| Töötoa sessioon | Juhend | Põhifookus |
|-----------------|--------|------------|
| 1 | [Session01-GettingStartedFoundryLocal](./Session01-GettingStartedFoundryLocal.md) | Paigaldamine, valideerimine, phi & GPT-OSS-20B käitamine, kiirendus |
| 2 | [Session02-BuildAISolutionsRAG](./Session02-BuildAISolutionsRAG.md) | Käskude kujundamine, RAG mustrid, CSV ja dokumentide sidumine, migratsioon |
| 3 | [Session03-OpenSourceModels](./Session03-OpenSourceModels.md) | Hugging Face integratsioon, võrdlemine, mudeli valik |
| 4 | [Session04-CuttingEdgeModels](./Session04-CuttingEdgeModels.md) | SLM vs LLM, WebGPU, Chainlit RAG, ONNX kiirendus |
| 5 | [Session05-AIPoweredAgents](./Session05-AIPoweredAgents.md) | Agendi rollid, mälu, tööriistad, orkestreerimine |
| 6 | [Session06-ModelsAsTools](./Session06-ModelsAsTools.md) | Marsruutimine, ahelate loomine, skaleerimine Azure'i suunas |

Iga sessioonifail sisaldab: kokkuvõtet, õpieesmärke, 30-minutilist demo voogu, algprojekt, valideerimise kontrollnimekirja, tõrkeotsingut ja viiteid ametlikule Foundry Local Python SDK-le.

### Näidisskriptid

Töötoa sõltuvuste installimine (Windows):

```powershell
cd Workshop
py -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

macOS / Linux:

```bash
cd Workshop
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Kui Foundry Local teenus töötab teisel (Windows) masinal või virtuaalmasinal macOS-i peal, eksportige lõpp-punkt:

```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```

| Sessioon | Skript(id) | Kirjeldus |
|----------|------------|-----------|
| 1 | `samples/session01/chat_bootstrap.py` | Teenuse käivitamine ja voogedastusega vestlus |
| 2 | `samples/session02/rag_pipeline.py` | Minimaalne RAG (mälu sisemised vektorid) |
|   | `samples/session02/rag_eval_ragas.py` | RAG hindamine ragas mõõdikutega |
| 3 | `samples/session03/benchmark_oss_models.py` | Mitme mudeli latentsuse ja läbilaskevõime testimine |
| 4 | `samples/session04/model_compare.py` | SLM vs LLM võrdlus (latentsus ja näidisväljund) |
| 5 | `samples/session05/agents_orchestrator.py` | Kahe agendi uurimis- ja toimetamisprotsess |
| 6 | `samples/session06/models_router.py` | Kavatsusel põhinev marsruutimise demo |
|   | `samples/session06/models_pipeline.py` | Mitmeastmeline plaani/teostamise/parandamise ahel |

### Keskkonnamuutujad (ühised näidistele)

| Muutuja | Eesmärk | Näide |
|---------|---------|-------|
| `FOUNDRY_LOCAL_ALIAS` | Vaikimisi ühe mudeli alias lihtsate näidiste jaoks | `phi-4-mini` |
| `SLM_ALIAS` / `LLM_ALIAS` | Selge SLM vs suurem mudel võrdluseks | `phi-4-mini` / `gpt-oss-20b` |
| `BENCH_MODELS` | Komadega eraldatud aliaste loend testimiseks | `qwen2.5-0.5b,mistral-7b` |
| `BENCH_ROUNDS` | Testi korduste arv mudeli kohta | `3` |
| `BENCH_PROMPT` | Testimisel kasutatav küsimus | `Selgita lühidalt, mis on retrieval augmented generation.` |
| `EMBED_MODEL` | Sentence-transformers vektorite mudel | `sentence-transformers/all-MiniLM-L6-v2` |
| `RAG_QUESTION` | Testküsimuse ülekirjutamine RAG torujuhtme jaoks | `Miks kasutada RAG-i kohaliku inferentsiga?` |
| `AGENT_QUESTION` | Agendi torujuhtme küsimuse ülekirjutamine | `Selgita, miks edge AI on oluline vastavuse jaoks.` |
| `AGENT_MODEL_PRIMARY` | Mudeli alias uurimisagendi jaoks | `phi-4-mini` |
| `AGENT_MODEL_EDITOR` | Mudeli alias toimetaja agendi jaoks (võib erineda) | `gpt-oss-20b` |
| `SHOW_USAGE` | Kui `1`, prindib iga lõpetamise kohta tokenite kasutuse | `1` |
| `RETRY_ON_FAIL` | Kui `1`, proovib uuesti ajutiste vestlusvigade korral | `1` |
| `RETRY_BACKOFF` | Sekundid, mida oodata enne uuesti proovimist | `1.0` |

Kui muutujat ei ole määratud, kasutavad skriptid mõistlikke vaikeseadeid. Ühe mudeli demode jaoks vajate tavaliselt ainult `FOUNDRY_LOCAL_ALIAS`.

### Abimoodul

Kõik näidised jagavad nüüd abifaili `samples/workshop_utils.py`, mis pakub:

* Vahemällu salvestatud `FoundryLocalManager` + OpenAI kliendi loomist
* `chat_once()` abifunktsiooni koos valikulise uuesti proovimise ja kasutuse printimisega
* Lihtsat tokenite kasutuse aruandlust (lubage `SHOW_USAGE=1` abil)

See vähendab dubleerimist ja toob esile parimad tavad tõhusaks kohaliku mudeli orkestreerimiseks.

## Valikulised täiustused (rist-sessioonid)

| Teema | Täiustus | Sessioonid | Keskkond / Lüliti |
|-------|----------|------------|-------------------|
| Determinism | Fikseeritud temperatuur + stabiilsed küsimuste komplektid | 1–6 | Määrake `temperature=0`, `top_p=1` |
| Tokenite kasutuse nähtavus | Järjepidev kulude/tõhususe õpetamine | 1–6 | `SHOW_USAGE=1` |
| Esimese tokeni voog | Tajutud latentsuse mõõdik | 1,3,4,6 | `BENCH_STREAM=1` (testimine) |
| Uuesti proovimise vastupidavus | Käsitleb ajutisi külmkäivitusi | Kõik | `RETRY_ON_FAIL=1` + `RETRY_BACKOFF` |
| Mitme mudeli agendid | Heterogeenne rollide spetsialiseerumine | 5 | `AGENT_MODEL_PRIMARY`, `AGENT_MODEL_EDITOR` |
| Kohanduv marsruutimine | Kavatsus + kulude heuristika | 6 | Laiendage marsruuterit eskalatsiooniloogikaga |
| Vektormälu | Pikaajaline semantiline mälu | 2,5,6 | Integreerige FAISS/Chroma vektorite indeks |
| Jälje eksport | Auditeerimine ja hindamine | 2,5,6 | Lisage JSON read iga sammu kohta |
| Kvaliteedi rubriigid | Kvalitatiivne jälgimine | 3–6 | Sekundaarsed hindamisküsimused |
| Suitsutestid | Kiire töötoa eelvalideerimine | Kõik | `python Workshop/tests/smoke.py` |

### Deterministlik kiire algus

```powershell
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
python Workshop\tests\smoke.py
```

Oodake stabiilseid tokenite arve korduvate identsete sisendite korral.

### RAG hindamine (Sessioon 2)

Kasutage `rag_eval_ragas.py`, et arvutada vastuse asjakohasus, usaldusväärsus ja konteksti täpsus väikese sünteetilise andmekogumi põhjal:

```powershell
cd Workshop/samples
python -m session02.rag_eval_ragas
```

Laiendage, pakkudes suuremat JSONL-i küsimuste, kontekstide ja tõeste vastustega, seejärel teisendage Hugging Face `Dataset`-iks.

## CLI käsu täpsuse lisa

Töötuba kasutab teadlikult ainult praegu dokumenteeritud / stabiilseid Foundry Local CLI käske.

### Viidatud stabiilsed käsud

| Kategooria | Käsk | Eesmärk |
|------------|------|---------|
| Põhi | `foundry --version` | Näitab installitud versiooni |
| Teenus | `foundry service start` | Käivitab kohaliku teenuse (kui mitte automaatselt) |
| Teenus | `foundry service status` | Näitab teenuse olekut |
| Mudelid | `foundry model list` | Loetleb kataloogi / saadaval olevad mudelid |
| Mudelid | `foundry model download <alias>` | Laadib mudeli kaalud vahemällu |
| Mudelid | `foundry model run <alias>` | Käivitab (laadib) mudeli kohapeal; kombineerige `--prompt` üheks tsükliks |
| Mudelid | `foundry model unload <alias>` / `foundry model stop <alias>` | Eemaldab mudeli mälust (kui toetatud) |
| Vahemälu | `foundry cache list` | Loetleb vahemällu salvestatud (laaditud) mudelid |

### Ühe tsükli küsimuse mustrid

Aegunud `model chat` alamkäsu asemel kasutage:

```powershell
foundry model run <alias> --prompt "Your question here"
```

See täidab ühe küsimuse/vastuse tsükli ja väljub.

### Eemaldatud / välditud mustrid

| Aegunud / Dokumenteerimata | Asendus / Juhised |
|----------------------------|------------------|
| `foundry model chat <model> "..."` | `foundry model run <model> --prompt "..."` |
| `foundry model list --running` | Kasutage lihtsat `foundry model list` + hiljutine tegevus / logid |
| `foundry model list --cached` | `foundry cache list` |
| `foundry model stats <model>` | Kasutage testimisskripti + OS tööriistu (Task Manager / `nvidia-smi`) |
| `foundry model benchmark ...` | `samples/session03/benchmark_oss_models.py` |

### Testimine ja telemeetria

- Latentsus, p95, tokenid/sekundis: `samples/session03/benchmark_oss_models.py`
- Esimese tokeni latentsus (voog): määrake `BENCH_STREAM=1`
- Ressursikasutus: OS monitorid (Task Manager, Activity Monitor, `nvidia-smi`).

Kui uued CLI telemeetria käsud stabiliseeruvad, saab neid hõlpsasti lisada sessioonide markdownidesse.

### Automaatne lint-kaitse

Automaatne linter takistab aegunud CLI mustrite uuesti kasutuselevõttu markdown-failide koodiplokkides:

Skript: `Workshop/scripts/lint_markdown_cli.py`

Aegunud mustrid blokeeritakse koodiplokkides.

Soovitatud asendused:
| Aegunud | Asendus |
|---------|---------|
| `foundry model chat <a> "..."` | `foundry model run <a> --prompt "..."` |
| `model list --running` | `model list` |
| `model list --cached` | `cache list` |
| `model stats` | Testimisskript + süsteemitööriistad |
| `model benchmark` | `samples/session03/benchmark_oss_models.py` |
| `model list --available` | `model list` |

Käivitage kohapeal:
```powershell
python Workshop\scripts\lint_markdown_cli.py --verbose
```

GitHub Action: `.github/workflows/markdown-cli-lint.yml` käivitub iga pushi ja PR-i korral.

Valikuline pre-commit hook:
```bash
echo "python Workshop/scripts/lint_markdown_cli.py" > .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```

## Kiire CLI → SDK migratsiooni tabel

| Ülesanne | CLI ühe käsu lahendus | SDK (Python) ekvivalent | Märkused |
|----------|-----------------------|-------------------------|----------|
| Käivita mudel üks kord (küsimus) | `foundry model run phi-4-mini --prompt "Hello"` | `manager=FoundryLocalManager("phi-4-mini"); client=OpenAI(base_url=manager.endpoint, api_key=manager.api_key or "not-needed"); client.chat.completions.create(model=manager.get_model_info("phi-4-mini").id, messages=[{"role":"user","content":"Hello"}])` | SDK käivitab teenuse ja vahemälu automaatselt |
| Laadi (vahemälu) mudel | `foundry model download qwen2.5-0.5b` | `FoundryLocalManager("qwen2.5-0.5b")  # käivitab allalaadimise/laadimise` | Manager valib parima variandi, kui alias viitab mitmele versioonile |
| Loetle kataloog | `foundry model list` | `# kasutage manageri iga alias jaoks või hoidke teadaolevat loendit` | CLI koondab; SDK praegu iga aliasi instants |
| Loetle vahemällu salvestatud mudelid | `foundry cache list` | `manager.list_cached_models()` | Pärast manageri initsialiseerimist (mis tahes alias) |
| Hankige lõpp-punkti URL | (kaudselt) | `manager.endpoint` | Kasutatakse OpenAI-ühilduva kliendi loomiseks |
| Soojenda mudel | `foundry model run <alias>` ja esimene küsimus | `chat_once(alias, messages=[...])` (abifunktsioon) | Abifunktsioonid käsitlevad esialgset külmlatentsuse soojendust |
| Mõõda latentsust | `python -m session03.benchmark_oss_models` | `import benchmark_oss_models` (või uus eksportija skript) | Eelistage skripti järjepidevate mõõdikute jaoks |
| Peata / eemalda mudel | `foundry model unload <alias>` | (Pole avatud – taaskäivitage teenus / protsess) | Tavaliselt pole töövoo jaoks vajalik |
| Tokenite kasutuse hankimine | (vaata väljundit) | `resp.usage.total_tokens` | Pakutakse, kui backend tagastab kasutuse objekti |

## Testimise markdowni eksport

Kasutage skripti `Workshop/scripts/export_benchmark_markdown.py`, et käivitada värske testimine (sama loogika nagu `samples/session03/benchmark_oss_models.py`) ja luua GitHub-sõbralik markdown-tabel ning toorandmed JSON-is.

### Näide

```powershell
python Workshop\scripts\export_benchmark_markdown.py --models "qwen2.5-0.5b,mistral-7b" --prompt "Explain retrieval augmented generation briefly." --rounds 3 --output benchmark_report.md
```

Loodud failid:
| Fail | Sisu |
|------|------|
| `benchmark_report.md` | Markdown-tabel + tõlgendamise vihjed |
| `benchmark_report.json` | Toormõõdikute massiiv (võrdlemiseks / trendide jälgimiseks) |

Määrake keskkonnas `BENCH_STREAM=1`, et lisada esimese tokeni latentsus, kui toetatud.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta arusaamatuste või valesti tõlgenduste eest, mis võivad tekkida selle tõlke kasutamise tõttu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "45923ada94573fee7c82cc4f0c3bb344",
  "translation_date": "2025-10-28T22:51:17+00:00",
  "source_file": "Workshop/Readme.md",
  "language_code": "sw"
}
-->
# EdgeAI kwa Kompyuta - Warsha

> **Njia ya Kujifunza kwa Vitendo ya Kujenga Programu za Edge AI Tayari kwa Uzalishaji**
>
> Jifunze jinsi ya kupeleka AI kwa ndani kwa kutumia Microsoft Foundry Local, kuanzia kukamilisha mazungumzo ya kwanza hadi uratibu wa mawakala wengi katika vipindi 6 vya maendeleo.

---

## 🎯 Utangulizi

Karibu kwenye **Warsha ya EdgeAI kwa Kompyuta** - mwongozo wako wa vitendo wa kujenga programu za akili bandia zinazofanya kazi kikamilifu kwenye vifaa vya ndani. Warsha hii inabadilisha dhana za nadharia za Edge AI kuwa ujuzi wa ulimwengu halisi kupitia mazoezi ya changamoto yanayoongezeka kwa kutumia Microsoft Foundry Local na Small Language Models (SLMs).

### Kwa Nini Warsha Hii?

**Mapinduzi ya Edge AI Yamefika**

Mashirika kote ulimwenguni yanahamia kutoka kwa AI inayotegemea wingu kwenda kwa kompyuta ya ukingo kwa sababu kuu tatu:

1. **Faragha & Uzingatiaji Sheria** - Kusindika data nyeti kwa ndani bila kupeleka kwenye wingu (HIPAA, GDPR, kanuni za kifedha)
2. **Utendaji** - Kuondoa ucheleweshaji wa mtandao (50-500ms kwa ndani dhidi ya 500-2000ms kwa wingu)
3. **Udhibiti wa Gharama** - Kuondoa gharama za API kwa kila tokeni na kupanua bila gharama za wingu

**Lakini Edge AI ni Tofauti**

Kuendesha AI kwa ndani kunahitaji ujuzi mpya:
- Uchaguzi wa modeli na uboreshaji kwa vikwazo vya rasilimali
- Usimamizi wa huduma za ndani na kasi ya vifaa
- Uhandisi wa maelekezo kwa modeli ndogo
- Mifumo ya kupeleka uzalishaji kwa vifaa vya ukingo

**Warsha Hii Inakuletea Ujuzi Huo**

Katika vipindi 6 vilivyolenga (~saa 3 kwa jumla), utapiga hatua kutoka "Hello World" hadi kupeleka mifumo ya mawakala wengi tayari kwa uzalishaji - yote yakiendeshwa kwa ndani kwenye mashine yako.

---

## 📚 Malengo ya Kujifunza

Kwa kukamilisha warsha hii, utaweza:

### Ujuzi wa Msingi
1. **Kuweka na Kusimamia Huduma za AI za Ndani**
   - Sakinisha na usanidi Microsoft Foundry Local
   - Chagua modeli zinazofaa kwa kupeleka ukingoni
   - Simamia mzunguko wa maisha wa modeli (kupakua, kupakia, kuhifadhi)
   - Fuatilia matumizi ya rasilimali na boresha utendaji

2. **Jenga Programu Zinazotumia AI**
   - Tekeleza kukamilisha mazungumzo yanayofanana na OpenAI kwa ndani
   - Buni maelekezo bora kwa Small Language Models
   - Shughulikia majibu ya mtiririko kwa UX bora
   - Unganisha modeli za ndani kwenye programu zilizopo

3. **Unda Mifumo ya RAG (Retrieval Augmented Generation)**
   - Jenga utafutaji wa semantiki kwa kutumia embeddings
   - Weka majibu ya LLM katika maarifa maalum ya sekta
   - Tathmini ubora wa RAG kwa kutumia vipimo vya kawaida vya sekta
   - Panua kutoka kwa mfano hadi uzalishaji

4. **Boresha Utendaji wa Modeli**
   - Pima modeli nyingi kwa matumizi yako
   - Pima ucheleweshaji, kasi ya usindikaji, na muda wa tokeni ya kwanza
   - Chagua modeli bora kulingana na uwiano wa kasi/ubora
   - Linganisha faida na hasara za SLM dhidi ya LLM katika hali halisi

5. **Ratibu Mifumo ya Mawakala Wengi**
   - Buni mawakala maalum kwa kazi tofauti
   - Tekeleza kumbukumbu ya mawakala na usimamizi wa muktadha
   - Ratibu mawakala katika mtiririko wa kazi ngumu
   - Elekeza maombi kwa busara kati ya modeli nyingi

6. **Peleka Suluhisho Tayari kwa Uzalishaji**
   - Tekeleza utunzaji wa makosa na mantiki ya kujaribu tena
   - Fuatilia matumizi ya tokeni na rasilimali za mfumo
   - Jenga miundombinu inayoweza kupanuka kwa kutumia mifumo ya modeli-kama-vifaa
   - Panga njia za uhamiaji kutoka ukingo hadi mseto (ukingo + wingu)

---

## 🎓 Matokeo ya Kujifunza

### Kile Utakachojenga

Mwisho wa warsha hii, utakuwa umeunda:

| Kipindi | Kazi | Ujuzi Ulioonyeshwa |
|---------|------|--------------------|
| **1** | Programu ya mazungumzo na mtiririko | Usanidi wa huduma, kukamilisha msingi, UX ya mtiririko |
| **2** | Mfumo wa RAG na tathmini | Embeddings, utafutaji wa semantiki, vipimo vya ubora |
| **3** | Suite ya majaribio ya modeli nyingi | Upimaji wa utendaji, kulinganisha modeli |
| **4** | Kilinganishi cha SLM dhidi ya LLM | Uchambuzi wa faida na hasara, mikakati ya uboreshaji |
| **5** | Mratibu wa mawakala wengi | Ubunifu wa mawakala, usimamizi wa kumbukumbu, uratibu |
| **6** | Mfumo wa uelekezaji wa akili | Utambuzi wa nia, uteuzi wa modeli, upanuzi |

### Matriz ya Uwezo

| Kiwango cha Ujuzi | Kipindi 1-2 | Kipindi 3-4 | Kipindi 5-6 |
|-------------------|------------|-------------|-------------|
| **Kompyuta** | ✅ Usanidi & Misingi | ⚠️ Changamoto | ❌ Ngumu sana |
| **Wastani** | ✅ Mapitio ya haraka | ✅ Kujifunza msingi | ⚠️ Malengo ya ziada |
| **Wataalamu** | ✅ Rahisi | ✅ Uboreshaji | ✅ Mifumo ya uzalishaji |

### Ujuzi Tayari kwa Kazi

**Baada ya warsha hii, utakuwa tayari:**

✅ **Jenga Programu za Kwanza za Faragha**
- Programu za afya zinazoshughulikia PHI/PII kwa ndani
- Huduma za kifedha zenye mahitaji ya uzingatiaji
- Mifumo ya serikali yenye mahitaji ya uhuru wa data

✅ **Boresha kwa Mazingira ya Ukingo**
- Vifaa vya IoT vyenye rasilimali ndogo
- Programu za simu zinazofanya kazi bila mtandao
- Mifumo ya wakati halisi yenye ucheleweshaji mdogo

✅ **Buni Miundombinu ya Akili**
- Mifumo ya mawakala wengi kwa mtiririko wa kazi ngumu
- Uhamiaji wa mseto wa ukingo-wingu
- Miundombinu ya AI yenye gharama nafuu

✅ **Ongoza Miradi ya Edge AI**
- Tathmini uwezekano wa Edge AI kwa miradi
- Chagua modeli na mifumo inayofaa
- Buni suluhisho za AI za ndani zinazoweza kupanuka

---

## 🗺️ Muundo wa Warsha

### Muhtasari wa Vipindi (Vipindi 6 × Dakika 30 = Saa 3)

| Kipindi | Mada | Lengo | Muda |
|---------|------|-------|------|
| **1** | Kuanza na Foundry Local | Usanidi, uthibitishaji, kukamilisha kwa mara ya kwanza | Dakika 30 |
| **2** | Kujenga Suluhisho za AI na RAG | Uhandisi wa maelekezo, embeddings, tathmini | Dakika 30 |
| **3** | Modeli za Chanzo Huria | Ugunduzi wa modeli, upimaji, uteuzi | Dakika 30 |
| **4** | Modeli za Kisasa | SLM dhidi ya LLM, uboreshaji, mifumo | Dakika 30 |
| **5** | Mawakala Wanaotumia AI | Ubunifu wa mawakala, uratibu, kumbukumbu | Dakika 30 |
| **6** | Modeli kama Vifaa | Uelekezaji, mnyororo, mikakati ya upanuzi | Dakika 30 |

---

## 🚀 Kuanza Haraka

### Mahitaji ya Awali

**Mahitaji ya Mfumo:**
- **OS**: Windows 10/11, macOS 11+, au Linux (Ubuntu 20.04+)
- **RAM**: Angalau 8GB, inapendekezwa 16GB+
- **Hifadhi**: Angalau 10GB nafasi ya bure kwa modeli
- **CPU**: Prosesa ya kisasa yenye msaada wa AVX2
- **GPU** (hiari): Inayolingana na CUDA au Qualcomm NPU kwa kasi

**Mahitaji ya Programu:**
- **Python 3.8+** ([Pakua](https://www.python.org/downloads/))
- **Microsoft Foundry Local** ([Mwongozo wa Usanidi](../../../Workshop))
- **Git** ([Pakua](https://git-scm.com/downloads))
- **Visual Studio Code** (inapendekezwa) ([Pakua](https://code.visualstudio.com/))

### Usanidi kwa Hatua 3

#### 1. Sakinisha Foundry Local

**Windows:**
```powershell
winget install Microsoft.FoundryLocal
```

**macOS:**
```bash
brew tap microsoft/foundrylocal
brew install foundrylocal
```

**Thibitisha Usanidi:**
```bash
foundry --version
foundry service status
```

**Hakikisha Azure AI Foundry Local inaendesha na bandari iliyowekwa**

```bash
# Set FoundryLocal to use port 58123 (default)
foundry service set --port 58123 --show

# Or use a different port
foundry service set --port 58000 --show
```

**Thibitisha inafanya kazi:**
```bash
# Check service status
foundry service status

# Test the endpoint
curl http://127.0.0.1:58123/v1/models
```
**Kutafuta Modeli Zinazopatikana**
Ili kuona ni modeli zipi zinapatikana katika Foundry Local yako, unaweza kuuliza sehemu ya modeli:

```bash
# cmd/bash/powershell
foundry model list
```

Kutumia Endpoint ya Wavuti 

```bash
# Windows PowerShell
powershell -Command "Invoke-RestMethod -Uri 'http://127.0.0.1:58123/v1/models' -Method Get"

# Or using curl (if available)
curl http://127.0.0.1:58123/v1/models
```

#### 2. Clone Repository & Sakinisha Vifaa

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

#### 3. Endesha Mfano Wako wa Kwanza

```bash
# Start Foundry Local and load a model
foundry model run phi-4-mini

# Run the chat bootstrap sample
cd samples
python -m session01.chat_bootstrap "What is edge AI?"
```

**✅ Mafanikio!** Unapaswa kuona majibu ya mtiririko kuhusu edge AI.

---

## 📦 Rasilimali za Warsha

### Sampuli za Python

Mifano ya vitendo inayoonyesha kila dhana:

| Kipindi | Sampuli | Maelezo | Muda wa Kuendesha |
|---------|---------|---------|-------------------|
| 1 | [`chat_bootstrap.py`](../../../Workshop/samples/session01/chat_bootstrap.py) | Mazungumzo ya msingi & mtiririko | ~30s |
| 2 | [`rag_pipeline.py`](../../../Workshop/samples/session02/rag_pipeline.py) | RAG na embeddings | ~45s |
| 2 | [`rag_eval_ragas.py`](../../../Workshop/samples/session02/rag_eval_ragas.py) | Tathmini ya ubora wa RAG | ~60s |
| 3 | [`benchmark_oss_models.py`](../../../Workshop/samples/session03/benchmark_oss_models.py) | Upimaji wa modeli nyingi | ~2-3m |
| 4 | [`model_compare.py`](../../../Workshop/samples/session04/model_compare.py) | Kulinganisha SLM dhidi ya LLM | ~45s |
| 5 | [`agents_orchestrator.py`](../../../Workshop/samples/session05/agents_orchestrator.py) | Mfumo wa mawakala wengi | ~60s |
| 6 | [`models_router.py`](../../../Workshop/samples/session06/models_router.py) | Uelekezaji kulingana na nia | ~45s |
| 6 | [`models_pipeline.py`](../../../Workshop/samples/session06/models_pipeline.py) | Mnyororo wa hatua nyingi | ~60s |

### Noti za Jupyter

Uchunguzi wa maingiliano na maelezo na vielelezo:

| Kipindi | Notebook | Maelezo | Ugumu |
|---------|----------|---------|-------|
| 1 | [`session01_chat_bootstrap.ipynb`](./notebooks/session01_chat_bootstrap.ipynb) | Misingi ya mazungumzo & mtiririko | ⭐ Kompyuta |
| 2 | [`session02_rag_pipeline.ipynb`](./notebooks/session02_rag_pipeline.ipynb) | Jenga mfumo wa RAG | ⭐⭐ Wastani |
| 2 | [`session02_rag_eval_ragas.ipynb`](./notebooks/session02_rag_eval_ragas.ipynb) | Tathmini ubora wa RAG | ⭐⭐ Wastani |
| 3 | [`session03_benchmark_oss_models.ipynb`](./notebooks/session03_benchmark_oss_models.ipynb) | Upimaji wa modeli | ⭐⭐ Wastani |
| 4 | [`session04_model_compare.ipynb`](./notebooks/session04_model_compare.ipynb) | Kulinganisha modeli | ⭐⭐ Wastani |
| 5 | [`session05_agents_orchestrator.ipynb`](./notebooks/session05_agents_orchestrator.ipynb) | Uratibu wa mawakala | ⭐⭐⭐ Juu |
| 6 | [`session06_models_router.ipynb`](./notebooks/session06_models_router.ipynb) | Uelekezaji wa nia | ⭐⭐⭐ Juu |
| 6 | [`session06_models_pipeline.ipynb`](./notebooks/session06_models_pipeline.ipynb) | Uratibu wa mnyororo | ⭐⭐⭐ Juu |

### Nyaraka

Miongozo na marejeleo ya kina:

| Nyaraka | Maelezo | Tumia Wakati |
|---------|---------|-------------|
| [QUICK_START.md](./QUICK_START.md) | Mwongozo wa usanidi wa haraka | Kuanza kutoka mwanzo |
| [QUICK_REFERENCE.md](./QUICK_REFERENCE.md) | Muhtasari wa amri & API | Unapohitaji majibu ya haraka |
| [FOUNDRY_SDK_QUICKREF.md](./FOUNDRY_SDK_QUICKREF.md) | Mifumo ya SDK & mifano | Kuandika msimbo |
| [ENV_CONFIGURATION.md](./ENV_CONFIGURATION.md) | Mwongozo wa mabadiliko ya mazingira | Kusakinisha sampuli |
| [SAMPLES_UPDATE_SUMMARY.md](./SAMPLES_UPDATE_SUMMARY.md) | Maboresho ya sampuli za hivi karibuni | Kuelewa mabadiliko |
| [SDK_MIGRATION_NOTES.md](./SDK_MIGRATION_NOTES.md) | Mwongozo wa uhamiaji | Kuboresha msimbo |
| [notebooks/TROUBLESHOOTING.md](./notebooks/TROUBLESHOOTING.md) | Masuala ya kawaida & suluhisho | Kutatua matatizo |

---

## 🎓 Mapendekezo ya Njia ya Kujifunza

### Kwa Kompyuta (Saa 3-4)
1. ✅ Kipindi cha 1: Kuanza (lenga usanidi na mazungumzo ya msingi)
2. ✅ Kipindi cha 2: Misingi ya RAG (ruka tathmini mwanzoni)
3. ✅ Kipindi cha 3: Upimaji Rahisi (modeli 2 tu)
4. ⏭️ Ruka Vipindi 4-6 kwa sasa
5. 🔄 Rudi kwenye Vipindi 4-6 baada ya kujenga programu ya kwanza

### Kwa Waendelezaji wa Kati (Saa 3)
1. ⚡ Kipindi cha 1: Uthibitishaji wa haraka wa usanidi
2. ✅ Kipindi cha 2: Kamilisha mfumo wa RAG na tathmini
3. ✅ Kipindi cha 3: Suite kamili ya upimaji
4. ✅ Kipindi cha 4: Uboreshaji wa modeli
5. ✅ Vipindi 5-6: Lenga mifumo ya usanifu

### Kwa Wataalamu wa Juu (Saa 2-3)
1. ⚡ Vipindi 1-3: Mapitio ya haraka na uthibitishaji
2. ✅ Kipindi cha 4: Uchambuzi wa kina wa uboreshaji
3. ✅ Kipindi cha 5: Miundombinu ya mawakala wengi
4. ✅ Kipindi cha 6: Mifumo ya uzalishaji na upanuzi
5. 🚀 Panua: Jenga mantiki ya uelekezaji maalum na uhamiaji wa mseto

---

## Kifurushi cha Vipindi vya Warsha (Maabara ya Dakika 30)

Ikiwa unafuata muundo wa warsha ya vipindi 6 vilivyofupishwa, tumia miongozo hii maalum (kila moja inalingana na na inakamilisha nyaraka za moduli pana hapo juu):

| Kipindi cha Warsha | Mwongozo | Lengo Kuu |
|--------------------|----------|-----------|
| 1 | [Session01-GettingStartedFoundryLocal](./Session01-GettingStartedFoundryLocal.md) | Usanidi, uthibitishaji, endesha phi & GPT-OSS-20B, kasi |
| 2 | [Session02-BuildAISolutionsRAG](./Session02-BuildAISolutionsRAG.md) | Uhandisi wa maelekezo, mifumo ya RAG, msingi wa CSV & hati, uhamiaji |
| 3 | [Session03-OpenSourceModels](./Session03-OpenSourceModels.md) | Ushirikiano wa Hugging Face, upimaji, uteuzi wa modeli |
| 4 | [Session04-CuttingEdgeModels](./Session04-CuttingEdgeModels.md) | SLM dhidi ya LLM, WebGPU, Chainlit RAG, Uharakishaji wa ONNX |
| 5 | [Session05-AIPoweredAgents](./Session05-AIPoweredAgents.md) | Majukumu ya mawakala, kumbukumbu, zana, uratibu |
| 6 | [Session06-ModelsAsTools](./Session06-ModelsAsTools.md) | Uelekezaji, mnyororo, njia ya kupanua hadi Azure |

Kila faili ya kikao inajumuisha: muhtasari, malengo ya kujifunza, mtiririko wa demo wa dakika 30, mradi wa kuanzia, orodha ya ukaguzi wa uthibitisho, utatuzi wa matatizo, na marejeleo ya SDK rasmi ya Foundry Local Python.

### Skripti za Mfano

Sakinisha utegemezi wa warsha (Windows):

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

Ikiwa unatumia huduma ya Foundry Local kwenye mashine au VM tofauti (Windows) kutoka macOS, hamisha endpoint:

```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```

| Kikao | Skripti | Maelezo |
|-------|---------|---------|
| 1 | `samples/session01/chat_bootstrap.py` | Huduma ya kuanzisha & mazungumzo ya mtiririko |
| 2 | `samples/session02/rag_pipeline.py` | RAG ndogo (embeddings za ndani ya kumbukumbu) |
|   | `samples/session02/rag_eval_ragas.py` | Tathmini ya RAG na vipimo vya ragas |
| 3 | `samples/session03/benchmark_oss_models.py` | Upimaji wa kasi na uwezo wa mifano mingi |
| 4 | `samples/session04/model_compare.py` | Ulinganisho wa SLM dhidi ya LLM (kasi & matokeo ya sampuli) |
| 5 | `samples/session05/agents_orchestrator.py` | Utafiti wa mawakala wawili → mchakato wa uhariri |
| 6 | `samples/session06/models_router.py` | Demo ya uelekezaji kulingana na nia |
|   | `samples/session06/models_pipeline.py` | Mnyororo wa hatua nyingi wa kupanga/utekelezaji/urekebishaji |

### Vigezo vya Mazingira (Pamoja kwa Sampuli Zote)

| Kigezo | Kusudi | Mfano |
|--------|--------|-------|
| `FOUNDRY_LOCAL_ALIAS` | Alias ya mfano mmoja wa msingi kwa sampuli za msingi | `phi-4-mini` |
| `SLM_ALIAS` / `LLM_ALIAS` | SLM dhahiri dhidi ya mfano mkubwa kwa ulinganisho | `phi-4-mini` / `gpt-oss-20b` |
| `BENCH_MODELS` | Orodha ya alias za kupima | `qwen2.5-0.5b,mistral-7b` |
| `BENCH_ROUNDS` | Marudio ya upimaji kwa kila mfano | `3` |
| `BENCH_PROMPT` | Swali linalotumika katika upimaji | `Explain retrieval augmented generation briefly.` |
| `EMBED_MODEL` | Mfano wa embedding wa sentence-transformers | `sentence-transformers/all-MiniLM-L6-v2` |
| `RAG_QUESTION` | Badilisha swali la majaribio kwa mchakato wa RAG | `Why use RAG with local inference?` |
| `AGENT_QUESTION` | Badilisha swali la mchakato wa mawakala | `Explain why edge AI matters for compliance.` |
| `AGENT_MODEL_PRIMARY` | Alias ya mfano kwa wakala wa utafiti | `phi-4-mini` |
| `AGENT_MODEL_EDITOR` | Alias ya mfano kwa wakala wa uhariri (inaweza kuwa tofauti) | `gpt-oss-20b` |
| `SHOW_USAGE` | Wakati `1`, inaonyesha matumizi ya tokeni kwa kila kukamilisha | `1` |
| `RETRY_ON_FAIL` | Wakati `1`, jaribu tena mara moja kwa makosa ya mazungumzo ya muda | `1` |
| `RETRY_BACKOFF` | Sekunde za kusubiri kabla ya kujaribu tena | `1.0` |

Ikiwa kigezo hakijawekwa, skripti zitarudi kwenye chaguo-msingi zinazofaa. Kwa maonyesho ya mfano mmoja, kwa kawaida unahitaji tu `FOUNDRY_LOCAL_ALIAS`.

### Moduli ya Huduma

Sampuli zote sasa zinashiriki msaidizi `samples/workshop_utils.py` inayotoa:

* Uundaji wa mteja wa `FoundryLocalManager` + OpenAI uliohifadhiwa
* Msaidizi wa `chat_once()` na jaribio la hiari + uchapishaji wa matumizi
* Ripoti rahisi ya matumizi ya tokeni (washa kupitia `SHOW_USAGE=1`)

Hii inapunguza marudio na inaonyesha mazoea bora kwa uratibu mzuri wa mifano ya ndani.

## Uboreshaji wa Hiari (Kikao cha Msalaba)

| Mada | Uboreshaji | Vikao | Mazingira / Kubadili |
|------|------------|-------|----------------------|
| Uthabiti | Joto lililowekwa + seti thabiti za maswali | 1–6 | Weka `temperature=0`, `top_p=1` |
| Uonekano wa Matumizi ya Tokeni | Mafunzo thabiti ya gharama/ufanisi | 1–6 | `SHOW_USAGE=1` |
| Mtiririko wa Tokeni ya Kwanza | Kipimo cha kasi kinachoonekana | 1,3,4,6 | `BENCH_STREAM=1` (upimaji) |
| Ustahimilivu wa Jaribio Tena | Hushughulikia kuanza baridi kwa muda | Zote | `RETRY_ON_FAIL=1` + `RETRY_BACKOFF` |
| Mawakala wa Mifano Mingi | Utaalam wa jukumu tofauti | 5 | `AGENT_MODEL_PRIMARY`, `AGENT_MODEL_EDITOR` |
| Uelekezaji wa Adaptive | Nia + heuristics za gharama | 6 | Panua uelekezaji na mantiki ya kuongezeka |
| Kumbukumbu ya Vector | Kumbukumbu ya muda mrefu ya semantiki | 2,5,6 | Jumuisha index ya embedding ya FAISS/Chroma |
| Uhamishaji wa Trace | Ukaguzi & tathmini | 2,5,6 | Ongeza mistari ya JSON kwa kila hatua |
| Rubrics za Ubora | Ufuatiliaji wa ubora | 3–6 | Maswali ya alama ya pili |
| Majaribio ya Haraka | Uthibitisho wa haraka kabla ya warsha | Zote | `python Workshop/tests/smoke.py` |

### Kuanza Haraka kwa Uthabiti

```powershell
set FOUNDRY_LOCAL_ALIAS=phi-4-mini
set SHOW_USAGE=1
python Workshop\tests\smoke.py
```

Tegemea hesabu thabiti za tokeni katika pembejeo zinazofanana zinazojirudia.

### Tathmini ya RAG (Kikao cha 2)

Tumia `rag_eval_ragas.py` kuhesabu umuhimu wa jibu, uaminifu, na usahihi wa muktadha kwenye seti ndogo ya data ya synthetiki:

```powershell
cd Workshop/samples
python -m session02.rag_eval_ragas
```

Panua kwa kutoa JSONL kubwa ya maswali, muktadha, na ukweli wa msingi, kisha ubadilishe kuwa `Dataset` ya Hugging Face.

## Kiambatisho cha Usahihi wa Amri za CLI

Warsha hutumia tu amri za sasa zilizoandikwa / thabiti za Foundry Local CLI.

### Amri Thabiti Zilizorejelewa

| Kategoria | Amri | Kusudi |
|-----------|------|--------|
| Msingi | `foundry --version` | Onyesha toleo lililosakinishwa |
| Msingi | `foundry init` | Anzisha usanidi |
| Huduma | `foundry service start` | Anzisha huduma ya ndani (ikiwa siyo kiotomatiki) |
| Huduma | `foundry status` | Onyesha hali ya huduma |
| Mifano | `foundry model list` | Orodhesha katalogi / mifano inayopatikana |
| Mifano | `foundry model download <alias>` | Pakua uzito wa mfano kwenye cache |
| Mifano | `foundry model run <alias>` | Anzisha (pakia) mfano ndani; changanya na `--prompt` kwa mzunguko mmoja |
| Mifano | `foundry model unload <alias>` / `foundry model stop <alias>` | Ondoa mfano kutoka kwa kumbukumbu (ikiwa inasaidiwa) |
| Cache | `foundry cache list` | Orodhesha mifano iliyohifadhiwa (iliyopakuliwa) |
| Mfumo | `foundry system info` | Muhtasari wa uwezo wa vifaa & uharakishaji |
| Mfumo | `foundry system gpu-info` | Taarifa za uchunguzi wa GPU |
| Usanidi | `foundry config list` | Onyesha maadili ya usanidi wa sasa |
| Usanidi | `foundry config set <key> <value>` | Sasisha usanidi |

### Muundo wa Swali la Mzunguko Mmoja

Badala ya amri ndogo ya `model chat` iliyopitwa na wakati, tumia:

```powershell
foundry model run <alias> --prompt "Your question here"
```

Hii inatekeleza mzunguko mmoja wa swali/jibu kisha inatoka.

### Miundo Iliyofutwa / Kuepukwa

| Iliyopitwa na Wakati / Isiyoandikwa | Mbadala / Mwongozo |
|------------------------------------|--------------------|
| `foundry model chat <model> "..."` | `foundry model run <model> --prompt "..."` |
| `foundry model list --running` | Tumia `foundry model list` ya kawaida + shughuli za hivi karibuni / kumbukumbu |
| `foundry model list --cached` | `foundry cache list` |
| `foundry model stats <model>` | Tumia skripti ya upimaji wa Python + zana za OS (Task Manager / `nvidia-smi`) |
| `foundry model benchmark ...` | `samples/session03/benchmark_oss_models.py` |

### Upimaji & Telemetry

- Kasi, p95, tokeni kwa sekunde: `samples/session03/benchmark_oss_models.py`
- Kasi ya tokeni ya kwanza (mtiririko): weka `BENCH_STREAM=1`
- Matumizi ya rasilimali: vichunguzi vya OS (Task Manager, Activity Monitor, `nvidia-smi`) + `foundry system info`.

Kadri amri mpya za telemetry za CLI zinavyothibitishwa, zinaweza kuingizwa kwa mabadiliko madogo kwenye markdowns za kikao.

### Walinzi wa Lint ya Kiotomatiki

Linter ya kiotomatiki inazuia kuanzishwa tena kwa miundo ya CLI iliyopitwa na wakati ndani ya vizuizi vya nambari vilivyofungwa vya faili za markdown:

Skripti: `Workshop/scripts/lint_markdown_cli.py`

Miundo iliyopitwa na wakati inazuiwa ndani ya vizuizi vya nambari.

Mbadala zinazopendekezwa:
| Iliyopitwa na Wakati | Mbadala |
|----------------------|---------|
| `foundry model chat <a> "..."` | `foundry model run <a> --prompt "..."` |
| `model list --running` | `model list` |
| `model list --cached` | `cache list` |
| `model stats` | Skripti ya upimaji + zana za mfumo |
| `model benchmark` | `samples/session03/benchmark_oss_models.py` |
| `model list --available` | `model list` |

Endesha ndani:
```powershell
python Workshop\scripts\lint_markdown_cli.py --verbose
```

Hatua ya GitHub: `.github/workflows/markdown-cli-lint.yml` inaendeshwa kwa kila push & PR.

Kipengele cha hiari cha pre-commit:
```bash
echo "python Workshop/scripts/lint_markdown_cli.py" > .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```

## Jedwali la Uhamishaji wa Haraka wa CLI → SDK

| Kazi | Amri ya CLI | Sawa na SDK (Python) | Maelezo |
|------|-------------|-----------------------|---------|
| Endesha mfano mara moja (swali) | `foundry model run phi-4-mini --prompt "Hello"` | `manager=FoundryLocalManager("phi-4-mini"); client=OpenAI(base_url=manager.endpoint, api_key=manager.api_key or "not-needed"); client.chat.completions.create(model=manager.get_model_info("phi-4-mini").id, messages=[{"role":"user","content":"Hello"}])` | SDK huanzisha huduma & uhifadhi kiotomatiki |
| Pakua (hifadhi) mfano | `foundry model download qwen2.5-0.5b` | `FoundryLocalManager("qwen2.5-0.5b")  # triggers download/load` | Meneja huchagua toleo bora ikiwa alias inahusiana na matoleo mengi |
| Orodhesha katalogi | `foundry model list` | `# tumia meneja kwa kila alias au weka orodha inayojulikana` | CLI huunganisha; SDK kwa sasa inachukua alias moja moja |
| Orodhesha mifano iliyohifadhiwa | `foundry cache list` | `manager.list_cached_models()` | Baada ya kuanzisha meneja (alias yoyote) |
| Washa uharakishaji wa GPU | `foundry config set compute.onnx.enable_gpu true` | `# Hatua ya CLI; SDK inadhani usanidi tayari umetumika` | Usanidi ni athari ya nje |
| Pata URL ya endpoint | (kimya kimya) | `manager.endpoint` | Inatumika kuunda mteja anayefanana na OpenAI |
| Pasha mfano | `foundry model run <alias>` kisha swali la kwanza | `chat_once(alias, messages=[...])` (huduma) | Huduma hushughulikia joto la awali la baridi kiotomatiki |
| Pima kasi | `python -m session03.benchmark_oss_models` | `import benchmark_oss_models` (au skripti mpya ya uhamishaji) | Pendelea skripti kwa vipimo thabiti |
| Acha / ondoa mfano | `foundry model unload <alias>` | (Haijawekwa wazi – anzisha upya huduma / mchakato) | Kwa kawaida siyo lazima kwa mtiririko wa warsha |
| Pata matumizi ya tokeni | (tazama matokeo) | `resp.usage.total_tokens` | Imetolewa ikiwa backend inarudisha kitu cha matumizi |

## Uhamishaji wa Markdown wa Upimaji

Tumia skripti `Workshop/scripts/export_benchmark_markdown.py` kuendesha upimaji mpya (mantiki sawa na `samples/session03/benchmark_oss_models.py`) na kutoa jedwali la Markdown linalofaa kwa GitHub pamoja na JSON ghafi.

### Mfano

```powershell
python Workshop\scripts\export_benchmark_markdown.py --models "qwen2.5-0.5b,mistral-7b" --prompt "Explain retrieval augmented generation briefly." --rounds 3 --output benchmark_report.md
```

Faili zilizotengenezwa:
| Faili | Yaliyomo |
|-------|----------|
| `benchmark_report.md` | Jedwali la Markdown + vidokezo vya tafsiri |
| `benchmark_report.json` | Array ya vipimo ghafi (kwa kulinganisha / ufuatiliaji wa mwenendo) |

Weka `BENCH_STREAM=1` katika mazingira ili kujumuisha kasi ya tokeni ya kwanza ikiwa inasaidiwa.

---

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya kutafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati ya asili katika lugha yake ya asili inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatutawajibika kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.
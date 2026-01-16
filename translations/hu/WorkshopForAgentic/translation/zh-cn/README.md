<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "aa775a734bda4590ecbe3a94a3b62197",
  "translation_date": "2026-01-05T17:53:01+00:00",
  "source_file": "WorkshopForAgentic/translation/zh-cn/README.md",
  "language_code": "hu"
}
-->
# 🎙️ AI Podcast Studio Workshop

![logo](../../../../../translated_images/hu/logo.8711e39dc8257d7b.png)

## A feladatod

Üdvözlünk az **AI Podcast Studio**-ban! Hamarosan elindítod a saját tech podcastodat, a "Jövő Bájtot" — de van egy csavar: egy AI által vezérelt produkciós csapatot építesz, hogy segítsen létrehozni azt. Nincs többé végtelen kutatás, forgatókönyvírás és hanganyag szerkesztés. Ehelyett programozással AI szuperképességekkel rendelkező podcastezővé válsz.

## A történet háttere

Képzeld el: te és a barátaid szeretnétek elindítani egy podcasst a legmenőbb tech trendekről, de mindenki elfoglalt tanulással, munkával vagy élettel. Mi lenne, ha építhetnél egy AI agent csapatot, hogy elvégezzék a nehéz munkát? Egyik agent kutatja a témát, a másik ír egy lebilincselő szkriptet, a harmadik pedig természetes, gördülékeny beszélgetéssé alakítja a szöveget. Sci-fi-nek hangzik? Tegyük valósággá.

## Mit fogsz megtanulni

A workshop végére tudni fogod, hogyan:
- 🤖 Telepítsd a saját helyi AI modellt (nincs API díj, nincs felhőfüggőség!)
- 🔧 Építs valódi, együttműködő, szakértő AI agenteket
- 🎬 Készíts teljes podcast gyártási folyamatot az ötlettől a hanganyagig

## Az utad: három felvonásban

Ahogy minden jó történetnek, nekünk is három felvonásunk van. Mindegyik lépésről lépésre építi fel az AI podcast stúdiódat:

| Fejezet | A feladatod | Mi történik | Megszerezhető készségek |
|---------|-------------|-------------|-------------------------|
| **1. felvonás** | [Ismerd meg az AI asszisztensed](01.BuildAIAgentWithSLM.md) | Megtanulod, hogyan készíts AI agenteket, amelyek tudnak csevegni, keresni az interneten, akár problémákat megoldani. Gondolj rájuk, mint soha el nem alvó kutatási gyakornokokra. | 🎯 Építsd meg az első agentedet<br>🛠️ Adj neki szuperképességeket (eszközök!)<br>🧠 Tanítsd gondolkodni<br>🌐 Kapcsolódj az internethez |
| **2. felvonás** | [Alakítsd ki a produkciós csapatod](02.AIAgentOrchestrationAndWorkflows.md) | Most jön a móka! Több AI agentet szervezel össze úgy, hogy igazán podcast csapatként működjenek együtt. Egyik kutat, a másik ír, te pedig jóváhagyod — csapatmunka valóra vált álom. | 🎭 Koordináld a több agent munkáját<br>🔄 Építs jóváhagyási munkafolyamatot<br>🖥️ Tesztelj a DevUI felületen<br>✋ Tartsd meg az emberi irányítást |
| **3. felvonás** | [Élesítsd a podcastodat](03.Multi-SpeakerPodcastGenerationWithVibeVoice.md) | A nagyszerű befejezés! Alakítsd át a szöveges forgatókönyvet élethű hangú, természetes beszélgetésű podcast hanganyaggá. A „Jövő Bájtos” podcastod készen áll a publikálásra! | 🎤 Szöveg-beszéd varázslat<br>👥 Több szereplős hangok<br>⏱️ Hosszú formátumú hanganyag<br>🚀 Teljesen automatizált |

Minden felvonás új képességeket nyit meg. Ha elég merész vagy, átugorhatsz fejezeteket, de ajánljuk a sorrend szerinti tanulást!

## Környezeti követelmények

Ez a workshop többféle hardverkörnyezetet támogat:
- **CPU**: teszteléshez és kis méretű használathoz ideális
- **GPU**: ajánlott éles környezethez, jelentősen gyorsítja az inferenciát
- **NPU**: támogatja a következő generációs neurális feldolgozó egység gyorsítást

## Amire szükséged lesz

### Szoftver lista ✅
- **Python 3.10+** (a programozási nyelved)
- **Ollama** (AI modell futtató a gépeden)
- **VS Code** (kódszerkesztőd)
- **Python kiterjesztés** (VS Code okosabbá tételéhez)
- **Git** (kód beszerzéséhez)

### Hardver ellenőrzés 💻
- **Futtathatom?**: 8 GB memória, 10 GB szabad hely (működik, de lehet egy kicsit lassú)
- **Ideális konfiguráció**: 16 GB+ memória, egy jó GPU (zökkenőmentes futtatás!)
- **Van NPU-d?**: Még jobb! Következő generációs teljesítmény feloldva 🚀

## Állítsd össze a stúdiódat 🎬

### 1. lépés: Python frissítés

Győződj meg róla, hogy Python 3.10-es vagy újabb verzió van telepítve:

```bash
python --version
# Python 3.10.x vagy újabb verziót kell mutatnia
```

Nincs Python? Szerezd be a [python.org](https://python.org) oldalról — ingyenes!

### 2. lépés: Szerezz be Ollama-t (az AI modell futtatódat)

Látogass el a [ollama.ai](https://ollama.ai) oldalra, és töltsd le az operációs rendszerednek megfelelőt. Gondolj rá úgy, mint a helyi AI modellt futtató motorra.

Ellenőrizd, hogy készen áll:

```bash
ollama --version
```

### 3. lépés: Töltsd le az AI agyadat 🧠

Ideje megszerezni a Qwen-3-8B modellt (mintha felvennéd az első AI asszisztensedet):

```bash
ollama pull qwen3:8b
```

*Ez eltarthat pár percig. Tökéletes kávészünet! ☕*

### 4. lépés: Állítsd be a VS Code-ot

Ha még nincs meg, szerezd be a [Visual Studio Code](https://code.visualstudio.com/). Ez a legjobb kódszerkesztő (kifogás nincs 😄).

### 5. lépés: Python kiterjesztés

A VS Code-ban:
1. Nyomd meg a `Ctrl+Shift+X`-et (Mac-en `Cmd+Shift+X`)
2. Keress rá a "Python"-ra
3. Telepítsd a hivatalos Microsoft Python kiterjesztést

### 6. lépés: Készen állsz! 🎉

Komolyan, készen állsz. Hozzunk létre egy kis AI varázslatot!

### 7. lépés: Telepítsd a Microsoft Agent Frameworköt és a kapcsolódó csomagokat 📦

Telepítsd a workshophoz szükséges összes függőséget:

```bash
pip install -r ./Installations/requirements.txt -U
```

*Ez telepíti a Microsoft Agent Frameworköt és minden szükséges csomagot. Kortyolj egy kávét — az első telepítés eltarthat pár percig! ☕*

## Workshop útmutató

A projekt részletes struktúrája, konfigurációk és a végrehajtás lépései a workshop során fokozatosan lesznek bemutatva.

## Hibakeresés (ha valami balul sül el) 🔧

### „Jaj, a modell letöltése túl lassú!”
**Megoldás**: Használj VPN-t vagy állítsd be az Ollama tükörforrásokat. Néha a hálózat akadozik.

### „A gépem hamar le fog állni! Kevés a memória!”
**Megoldás**: Válts kisebb modellre vagy állítsd be a `num_ctx` értéket, hogy kevesebb memóriát használjon. Gondolj rá úgy, mint az AI diétára.

### „Futtathatom gyorsabban GPU-val?”
**Megoldás**: Ollama automatikusan felismeri a GPU-t! Csak győződj meg róla, hogy a GPU drivered naprakész. Ingyenes sebességnövelés! 🏎️

## További források (azoknak, akik kíváncsiak) 📚

- [Ollama dokumentáció](https://github.com/ollama/ollama) — Mélyebb betekintés a helyi AI modellekbe
- [Microsoft Agent Framework](https://microsoft.github.io/autogen/) — Tudj meg többet az agent csapat építéséről
- [Qwen modell információk](https://qwenlm.github.io/) — Ismerd meg az AI asszisztensed agyát

## Licenc

MIT licenc — Építs menő dolgokat, oszd meg, és tegyük jobbá a világot! 🌍

## Szeretnél hozzájárulni?

Bugot találtál? Van ötleted? Küldj Issue-t vagy PR-t! Szeretjük a közösségi hangulatot. ✨

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ezt a dokumentumot az [Co-op Translator](https://github.com/Azure/co-op-translator) AI fordító szolgáltatás segítségével fordítottuk. Bár a pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások tartalmazhatnak hibákat vagy pontatlanságokat. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javaslunk. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy téves értelmezésekért.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
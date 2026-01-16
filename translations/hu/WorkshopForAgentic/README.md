<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f94e745264597bc5d8df967ead2eff97",
  "translation_date": "2026-01-05T10:49:22+00:00",
  "source_file": "WorkshopForAgentic/README.md",
  "language_code": "hu"
}
-->
# 🎙️ Az AI Podcast Stúdió Műhely

> 🌏 [中文版 (Kínai verzió)](translation/zh-cn/README.md)

![logo](../../../translated_images/hu/logo.8711e39dc8257d7b.png)

## A Küldetésed

Üdvözölünk az **AI Podcast Stúdióban**! Hamarosan elindítod saját tech podcastodat "Future Bytes" néven — de itt a csavar: egy AI-alapú produkciós csapatot építesz, hogy segítsen a létrehozásában. Nincs több végtelen kutatás, forgatókönyvírás és hanganyag-szerkesztés. Helyette kódolással válhatsz podcast-producerré AI szuperképességekkel.

## A Történet

Képzeld el: te és barátaid szeretnétek podcastot indítani a legmenőbb tech trendekről, de mindenki elfoglalt az iskolával, munkával vagy az élet egyéb dolgával. Mi lenne, ha építhetnél egy AI ügynökökből álló csapatot, amely elvégzi a nehezét? Az egyik ügynök kutatja a témákat, a másik izgalmas forgatókönyveket ír, a harmadik pedig szöveget alakít természetes beszélgetéssé. Sci-fi? Csináljuk valósággá.

## Amit Megtanulsz

A műhely végére tudni fogod, hogyan:
- 🤖 Telepítsd saját helyi AI modelljeidet (nincs API költség, nem vagy felhőfüggő!)
- 🔧 Építs specializált AI ügynököket, amelyek tényleg együttműködnek
- 🎬 Hozz létre teljes podcast-produkciós folyamatot az ötlettől a hanganyagig

## Az Utad: Három Felvonás

![arch](../../../translated_images/hu/arch.5965fe504e4a3a93.png)

Mint bármely jó történetben, itt is három felvonás van. Mindegyik darabonként építi az AI podcast stúdiódat:

| Epizód | Küldetésed | Mi Történik | Megszerzett Készségek |
|---------|-----------|--------------|----------------|
| **1. Felvonás** | [Ismerd meg AI asszisztenseidet](md/01.BuildAIAgentWithSLM.md) | Megtanulod, hogyan hozz létre AI ügynököket, akik tudnak beszélgetni, böngészni az interneten és problémákat megoldani. Olyanok, mint az álmatlan kutatói gyakornokaid. | 🎯 Építsd meg első ügynököd<br>🛠️ Adj neki szuperképességeket (eszközöket!)<br>🧠 Tanítsd meg gondolkodni<br>🌐 Kapcsold össze az internettel |
| **2. Felvonás** | [Állítsd össze produkciós csapatodat](md/02.AIAgentOrchestrationAndWorkflows.md) | Most jön az izgalom! Több AI ügynököt koordinálsz, akik együtt dolgoznak, mint egy valódi podcast csapat. Egy kutat, egy ír, te jóváhagyod — együttműködés a siker kulcsa. | 🎭 Több ügynök koordinálása<br>🔄 Jóváhagyási munkafolyamatok építése<br>🖥️ Tesztelés DevUI felületen<br>✋ Emberek irányításának megtartása |
| **3. Felvonás** | [Keltse életre podcastodat](md/03.Multi-SpeakerPodcastGenerationWithVibeVoice.md) | A finálé! Szöveges forgatókönyved átalakítása valós podcast-hanggal, élethű hangokkal és természetes beszélgetésekkel. A "Future Bytes" podcastod készen áll! | 🎤 Szövegből beszéd varázslat<br>👥 Többbeszélős hangok<br>⏱️ Hosszú formátumú audio<br>🚀 Teljes automatizálás |

Minden felvonás új képességeket old fel. Ha bátor vagy, ugorj előre, de ajánlott a történetet követni!

## Környezeti Követelmények

Ez a műhely többféle hardveres környezetet támogat:
- **CPU**: Alkalmas tesztelésre és kis léptékű használatra
- **GPU**: Ajánlott produktív környezetekhez, jelentősen gyorsítja az inferenciát
- **NPU**: Támogatja a következő generációs neurális feldolgozó egységek gyorsítását

## Amire Szükséged Lesz

### Szoftver Ellenőrzőlista ✅
- **Python 3.10+** (a kódnyelved)
- **Ollama** (futtatja az AI modelleket a gépeden)
- **VS Code** (a szerkesztőd)
- **Python Kiterjesztés** (okosítja a VS Code-ot)
- **Git** (a kód beszerzéséhez)

### Hardver Ellenőrzés 💻
- **Futni fog?**: 8 GB RAM, 10 GB szabad hely (működik, de lassú lehet)
- **Ideális beállítás**: 16 GB+ RAM, jó GPU (zökkenőmentes élmény!)
- **Van NPU-d?**: Még jobb! Következő generációs teljesítmény kész 🚀

## Állítsd Be a Stúdiódat 🎬

### 1. Lépés: Python Feltöltés

Győződj meg róla, hogy Python 3.10 vagy újabb van telepítve:

```bash
python --version
# Python 3.10.x vagy újabb verziót kell mutatnia
```

Nincs Python? Szerezd be a [python.org](https://python.org)-ról — ingyenes!

### 2. Lépés: Szerezz Ollama-t (AI Modell Futtató)

Látogass el az [ollama.ai](https://ollama.ai) oldalra és töltsd le Ollama-t az operációs rendszeredhez. Ez az a motor, amely helyben futtatja az AI modelleidet.

Ellenőrizd, hogy készen áll-e:

```bash
ollama --version
```

### 3. Lépés: Töltsd le AI agyadat 🧠

Ideje letölteni a Qwen-3-8B modellt (mintha felvennéd első AI asszisztensedet):

```bash
ollama pull qwen3:8b
```

*Ez eltarthat néhány percig. Tökéletes idő egy kávészünethez! ☕*

### 4. Lépés: Állítsd be a VS Code-ot

Töltsd le a [Visual Studio Code](https://code.visualstudio.com/)-ot, ha még nincs meg. Ez a legjobb kódszerkesztő (vitassuk meg 😄).

### 5. Lépés: Python Kiterjesztés

A VS Code-ban:
1. Nyomd meg a `Ctrl+Shift+X`-et (vagy Mac-en `Cmd+Shift+X`)
2. Keress rá a "Python"-ra
3. Telepítsd a Microsoft hivatalos Python kiterjesztését

### 6. Lépés: Készen is állsz! 🎉

Komolyan, készen állsz a varázslatra. Kezdjük az AI csodát!

### 7. Lépés: Telepítsd a Microsoft Agent Frameworköt és Kapcsolódó Csomagokat 📦

Telepítsd az összes szükséges függőséget a műhelyhez:

```bash
pip install -r ./Installations/requirements.txt -U
```

*Ez telepíti a Microsoft Agent Frameworköt és minden szükséges csomagot. Kávé szünetet javaslunk — az első beállítás eltarthat pár percig! ☕*

## Műhely Használati Útmutató

Részletes projekt struktúra, konfigurációs lépések és futtatási módszerek lépésről lépésre elhangzanak a műhely során.

## Hibakeresés (Ha valami nem működik) 🔧

### "Úristen, a modell letöltés örökké tart!"
**Javítás**: Használj VPN-t vagy állítsd be Ollama-t egy tükrözött forrásra. Néha az internet nem velünk van.

### "A gépem haldoklik! El fog fogyni a memória!"
**Javítás**: Váltás kisebb modellre vagy a `num_ctx` beállítás csökkentése, hogy kevesebb memóriát használjon. Gondolj rá úgy, mintha diétára fogtad volna az AI-t.

### "Gyorsíthatom ezt a GPU-mmal?"
**Javítás**: Ollama automatikusan felismeri a GPU-kat! Csak győződj meg róla, hogy a GPU driver-ek naprakészek. Ingyenes sebességfokozó! 🏎️

## További Források (Az érdeklődőknek) 📚

- [Ollama Dokumentáció](https://github.com/ollama/ollama) — Mélyebb betekintés a helyi AI modellekbe
- [Microsoft Agent Framework](https://microsoft.github.io/autogen/) — Tudj meg többet az ügynök csapatokról
- [Qwen Modell Információ](https://qwenlm.github.io/) — Ismerd meg AI asszisztensed agyát

## Licenc

MIT Licenc — Építs menő dolgokat, osszd meg, tedd jobbá a világot! 🌍

## Szeretnél Hozzájárulni?

Találtál hibát? Van ötleted? Nyiss egy Issue-t vagy PR-t! Imádjuk a közösségi összefogást. ✨

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ezt a dokumentumot az AI fordító szolgáltatás [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével fordítottuk. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítás hibákat vagy pontatlanságokat tartalmazhat. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Kritikus információk esetén professzionális emberi fordítást javaslunk. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy helytelen értelmezésekért.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
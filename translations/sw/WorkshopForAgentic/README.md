<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f94e745264597bc5d8df967ead2eff97",
  "translation_date": "2026-01-05T10:48:27+00:00",
  "source_file": "WorkshopForAgentic/README.md",
  "language_code": "sw"
}
-->
# 🎙️ Warsha ya Studio ya AI Podcast

> 🌏 [中文版 (Toleo la Kichina)](translation/zh-cn/README.md)

![logo](../../../translated_images/logo.8711e39dc8257d7b.sw.png)

## Dhamira Yako

Karibu **The AI Podcast Studio**! Unakaribia kuzindua podcast yako ya teknolojia inayoitwa "Future Bytes" — lakini hapa kuna mabadiliko: utaunda timu inayotumia AI kusaidia kuunda podcast yako. Hakuna tena masaa yoyote ya utafiti, uandishi wa maandishi, na uhariri wa sauti. Badala yake, utatumia msimbo kujifunza kuwa mtayarishaji wa podcast mwenye nguvu za AI.

## Hadithi

Fikiria hivi: Wewe na marafiki zako mnataka kuanzisha podcast kuhusu mitindo bora ya teknolojia, lakini kila mtu yuko na shughuli shule, kazi, au maisha kwa ujumla. Je, ungetengeneza timu ya maajenti wa AI kufanya kazi ngumu? Mmoja anatafiti mada, mwingine anaandika maandishi ya kuvutia, na mwingine hubadilisha maandishi kuwa mazungumzo ya kawaida. Je, inaonekana kama hadithi za sayansi? Hebu tufanikishe.

## Utajifunza Nini

Mwisho wa warsha hii, utaweza:
- 🤖 Kuweka mfano wako wa AI kwenye kompyuta binafsi (hakuna gharama za API, hakuna utegemezi wa wingu!)
- 🔧 Kuunda maajenti maalum wa AI wanaofanya kazi pamoja kweli
- 🎬 Kuunda mchakato kamili wa uzalishaji wa podcast kutoka wazo hadi sauti

## Safari Yako: Matamasha Matatu

![arch](../../../translated_images/arch.5965fe504e4a3a93.sw.png)

Kama hadithi nzuri yoyote, tuna matamasha matatu. Kila moja hujenga studio yako ya podcast ya AI hatua kwa hatua:

| Kipindi | Lengo Lako | Kinachotokea | Ujuzi Unaopatikana |
|---------|------------|---------------|--------------------|
| **Tamasha la 1** | [Kutana na Msaidizi Wako wa AI](md/01.BuildAIAgentWithSLM.md) | Unagundua jinsi ya kuunda maajenti wa AI wanaoweza kuzungumza, kutafuta mtandaoni, na hata kutatua matatizo. Wazingatie kama wahandisi wa utafiti wasiolala kamwe. | 🎯 Tengeneza maajenti wako wa kwanza<br>🛠️ Wape nguvu za kisuperi (zana!)<br>🧠 Fundisha kufikiri<br>🌐 Waunganishe kwenye intaneti |
| **Tamasha la 2** | [Kuandaa Timu Yako ya Uzalishaji](md/02.AIAgentOrchestrationAndWorkflows.md) | Sasa mambo yanaanza kuwa ya kuvutia! Utaratibu wa maajenti wa AI wengi kufanya kazi pamoja kama timu halisi ya podcast. Mmoja anatafiti, mwingine anaandika, wewe unakubali — kazi ya pamoja huleta mafanikio. | 🎭 Ratibu maajenti wengi<br>🔄 Tengeneza mchakato wa idhini<br>🖥️ Jaribu na kiolesura cha DevUI<br>✋ Weka wanadamu ndani ya uendeshaji |
| **Tamasha la 3** | [Leta Podcast Yako Kuishi](md/03.Multi-SpeakerPodcastGenerationWithVibeVoice.md) | Mwisho! Geuza maandishi yako kuwa sauti halisi za podcast zenye sauti za kweli na mazungumzo ya kawaida. Podcast yako "Future Bytes" iko tayari kusambazwa! | 🎤 Uchawi wa maandishi-kwa-sauti<br>👥 Sauti nyingi za wazungumzaji<br>⏱️ Sauti ndefu<br>🚀 Uendeshaji kamili |

Kila tamasha hufungua uwezo mpya. Ruka mbele ikiwa una ujasiri, lakini tunapendekeza ufuate hadithi!

## Mahitaji ya Mazingira

Warsha hii inaunga mkono mazingira mbalimbali ya vifaa:
- **CPU**: Inafaa kwa majaribio na matumizi madogo
- **GPU**: Inapendekezwa kwa mazingira ya uzalishaji, huongeza kasi ya utambuzi kwa kiasi kikubwa
- **NPU**: Inaunga mkono kasi za kizazi kijacho cha usindikaji wa neva

## Utahitaji Nini

### Orodha ya Programu ✅
- **Python 3.10+** (Lugha yako ya kuandika programu)
- **Ollama** (Inakimbiza mifano ya AI kwenye mashine yako)
- **VS Code** (Mhariri wako wa msimbo)
- **Python Extension** (Inafanya VS Code kuwa smart zaidi)
- **Git** (Kwa kupakua msimbo)

### Ukaguzi wa Vifaa 💻
- **Naweza kuendesha?**: RAM 8GB, nafasi ya bure 10GB (inafanya kazi, lakini inaweza kuwa polepole)
- **Mpangilio bora**: RAM 16GB+ na GPU nzuri (enda vizuri!)
- **Una NPU?**: Hata bora! Ushawishi wa kizazi kijacho umefunguliwa 🚀

## Weka Studio Yako 🎬

### Hatua ya 1: Kuongeza Nguvu za Python

Hakikisha una Python 3.10 au toleo jipya zaidi:

```bash
python --version
# Inapaswa kuonyesha Python 3.10.x au zaidi
```

Bila Python? Pakua kutoka [python.org](https://python.org) — ni bure!

### Hatua ya 2: Pata Ollama (Msimamizi wa Mfano wa AI)

Nenda [ollama.ai](https://ollama.ai) na pakua Ollama kwa mfumo wako wa uendeshaji. Fikiria kama injini inayowezesha mifano yako ya AI kuendeshwa lokalini.

Angalia kama iko tayari:

```bash
ollama --version
```

### Hatua ya 3: Pakua Ubongo wako wa AI 🧠

Sasa ni wakati wa kupakua mfano wa Qwen-3-8B (kama kuajiri msaidizi wako wa kwanza wa AI):

```bash
ollama pull qwen3:8b
```

*Hii inaweza kuchukua dakika chache. Wakati mzuri wa kupata kahawa! ☕*

### Hatua ya 4: Sakinisha VS Code

Pakua [Visual Studio Code](https://code.visualstudio.com/) ikiwa huna. Ni mhariri bora wa msimbo ulimwenguni (nipigane 😄).

### Hatua ya 5: Upanuzi wa Python

Ndani ya VS Code:
1. Bonyeza `Ctrl+Shift+X` (au `Cmd+Shift+X` kwa Mac)
2. Tafuta "Python"
3. Sakinisha upanuzi rasmi wa Python wa Microsoft

### Hatua ya 6: Umejiandaa! 🎉

Kweli, uko tayari kuanza kazi. Hebu tufanye uchawi wa AI!

### Hatua ya 7: Sakinisha Microsoft Agent Framework na Pakiti Zinazohusiana 📦

Sakinisha utegemezi wote unaohitajika kwa warsha:

```bash
pip install -r ./Installations/requirements.txt -U
```

*Hii itasakinisha Microsoft Agent Framework na pakiti zote muhimu. Chukua kahawa — usakinishaji wa kwanza unaweza kuchukua dakika kadhaa! ☕*

## Maelekezo ya Warsha

Muundo wa mradi, hatua za usanidi, na njia za utekelezaji zitaelezewa hatua kwa hatua wakati wa warsha.

## Matatizo (Wakati Mambo Hayafanyi Kazi) 🔧

### "Sawa, kupakua mfano kunachukua muda mrefu mno!"
**Suluhisho**: Tumia VPN au sanidi Ollama kwa chanzo cha picha. Wakati mwingine intaneti hutudharau.

### "Kompyuta yangu inahisi kuzimia! Kumbukumbu imejaa!"
**Suluhisho**: Badilisha kuwa mfano mdogo au rekebisha kipimo cha `num_ctx` kutumia kumbukumbu kidogo. Fikiria kama kuliwa lishe ya AI yako.

### "Naweza kufanya hii iwe haraka na GPU yangu?"
**Suluhisho**: Ollama inatambua GPUs moja kwa moja! Hakikisha dereva wa GPU yako ni mpya. Kuongeza kasi bure! 🏎️

## Rasilimali Zaidi (Kwa Wanaotaka Kujifunza Zaidi) 📚

- [Hati za Ollama](https://github.com/ollama/ollama) — Chunguza kwa undani mifano ya AI lokalini
- [Microsoft Agent Framework](https://microsoft.github.io/autogen/) — Jifunze zaidi kuhusu kuunda timu za maajenti
- [Taarifa za Mfano wa Qwen](https://qwenlm.github.io/) — Jifunze kuhusu ubongo wa msaidizi wako wa AI

## Leseni

Leseni ya MIT — Tengeneza vitu vya kuvutia, shirikisha, na kufanya dunia kuwa bora! 🌍

## Unataka Kuchangia?

Umegundua hitilafu? Una wazo? Tuma Issue au PR! Tunapenda hali ya ushirikiano wa jamii. ✨

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kiarifu cha Kutohusika**:
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuwa sahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kasoro. Hati asili katika lugha yake ya asili inapaswa kuchukuliwa kama chanzo kamili. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatubebei dhamana kwa kufahamu vibaya au tafsiri isiyo sahihi inayoonekana kutokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
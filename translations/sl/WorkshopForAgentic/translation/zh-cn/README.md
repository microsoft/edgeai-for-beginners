<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "aa775a734bda4590ecbe3a94a3b62197",
  "translation_date": "2026-01-05T17:59:30+00:00",
  "source_file": "WorkshopForAgentic/translation/zh-cn/README.md",
  "language_code": "sl"
}
-->
# 🎙️ Delavnica AI podcast studia

![logo](../../../../../translated_images/sl/logo.8711e39dc8257d7b.webp)

## Tvoja naloga

Dobrodošel v **AI podcast studiu**! Pravkar boš zagnal svoj tehnološki podcast "Prihodnji bit" — a tu je preobrat: zgradiš AI-pogončeno produkcijsko ekipo, ki ti bo pomagala ustvariti ta podcast. Ni več neskončnega raziskovanja, pisanja scenarijev in urejanja zvoka. Namesto tega boš s programiranjem postal podcast produkcijski ustvarjalec z AI supersilami.

## Zgodba

Predstavljaj si: ti in prijatelji želite začeti podcast o najbolj kul tehnoloških trendih, a so vsi zaposleni z učenjem, delom ali življenjem. Kaj če bi lahko zgradil ekipo AI agentov, ki bi opravili težko delo? En agent raziskuje temo, drugi napiše privlačen scenarij, tretji pretvori besedilo v naraven, tekoč pogovor. Zveni kot znanstvena fantastika? Naredimo to resničnost.

## Kaj se boš naučil

Na koncu te delavnice boš znal:
- 🤖 Postaviti svoj lokalni AI model (brez stroškov API, brez odvisnosti od oblakov!)
- 🔧 Zgraditi dejanske profesionalne AI agente, ki sodelujejo
- 🎬 Ustvariti celoten produkcijski potek podcasta — od ideje do zvočnih posnetkov

## Tvoja pot: Tri dejanja

Kot v vsaki dobri zgodbi imamo tri dejanja. Vsako dejanje postopno gradi tvoj AI podcast studio:

| Poglavje | Tvoja naloga | Kaj se dogaja | Odklenjene veščine |
|---------|-------------|----------------|------------------|
| **Prvo dejanje** | [Spoznaj svojega AI asistenta](01.BuildAIAgentWithSLM.md) | Spoznal boš, kako ustvariti AI agente, ki lahko klepetajo, raziskujejo splet in celo rešujejo probleme. Predstavljaj si jih kot neizčrpne raziskovalne pripravnike. | 🎯 Zgradi svojega prvega agenta<br>🛠️ Opremi ga s supersilami (orodja!)<br>🧠 Nauči ga razmišljati<br>🌐 Poveži ga z internetom |
| **Drugo dejanje** | [Zgradi svojo produkcijsko ekipo](02.AIAgentOrchestrationAndWorkflows.md) | Zdaj postane zabavno! Usklajeval boš več AI agentov, da bodo sodelovali kot prava podcast ekipa. Eden raziskuje, drugi piše, ti potrjuješ — skupinsko delo uresniči sanje. | 🎭 Koordinacija več agentov<br>🔄 Gradnja delovnih tokov za potrjevanje<br>🖥️ Testiranje z uporabniškim vmesnikom DevUI<br>✋ Ohranitev človeškega nadzora |
| **Tretje dejanje** | [Oživi svoj podcast](03.Multi-SpeakerPodcastGenerationWithVibeVoice.md) | Veliki finale! Pretvori svoj besedilni scenarij v resnične podcast zvočne posnetke z realistično govorjeno govorico in naravnimi dialogi. Tvoj podcast "Prihodnji bit" je pripravljen za objavo! | 🎤 Čarobnost pretvorbe besedila v govor<br>👥 Več govornih likov<br>⏱️ Dolgi avdio posnetki<br>🚀 Popolna avtomatizacija |

Vsako dejanje odklene nove spretnosti. Če si pogumen, lahko preskakuješ, toda priporočamo, da slediš vrstnemu redu!

## Zahteve okolja

Delavnica podpira različne strojne opreme:
- **CPU**: primeren za testiranje in manjšo uporabo
- **GPU**: priporočeno za produkcijsko rabo, močno pohitri inferenco
- **NPU**: podpora za naslednjo generacijo nevronskih procesnih enot

## Kaj potrebuješ

### Programska oprema ✅
- **Python 3.10+** (tvoj programski jezik)
- **Ollama** (tvoj lokalni poganjalnik AI modelov)
- **VS Code** (tvoj urejevalnik kode)
- **Python razširitev** (da bo VS Code pametnejši)
- **Git** (za pridobivanje kode)

### Preveri strojno opremo 💻
- **Ali lahko tečem?**: 8GB RAM-a, 10GB prostega prostora (dovolj za uporabo, lahko počasneje)
- **Idealen setup**: 16GB+ RAM-a in dobra grafična kartica (gladka izkušnja!)
- **Imaš NPU?** Super! Odkleni zmogljivost prihodnje generacije 🚀

## Postavi svoj studio 🎬

### Korak 1: Nadgradi Python

Poskrbi, da imaš Python 3.10 ali novejši:

```bash
python --version
# Morala bi biti prikazana različica Python 3.10.x ali novejša
```

Nimaš Pythona? Pridobi ga na [python.org](https://python.org) — brezplačno je!

### Korak 2: Pridobi Ollama (tvoj poganjalnik AI modelov)

Pojdi na [ollama.ai](https://ollama.ai) in prenesi Ollamo za svoj operacijski sistem. Predstavljaj si jo kot motor za zagon AI modelov lokalno.

Preveri, ali je pripravljena:

```bash
ollama --version
```

### Korak 3: Prenesi svoj AI možgan 🧠

Čas je, da dobiš model Qwen-3-8B (kot da zaposliš svojega prvega AI asistenta):

```bash
ollama pull qwen3:8b
```

*Lahko traja nekaj minut. Odličen čas za kavo!☕*

### Korak 4: Nastavi VS Code

Če še nimaš, prenesi [Visual Studio Code](https://code.visualstudio.com/). Najboljši urejevalnik kode (resno 😄).

### Korak 5: Python razširitev

V VS Code:
1. Pritisni `Ctrl+Shift+X` (na Mac-u `Cmd+Shift+X`)
2. Poišči "Python"
3. Namesti uradno razširitev Microsoft Python

### Korak 6: Pripravljeno! 🎉

Resno, pripravljen si. Ustvarimo nekaj AI čarovnije!

### Korak 7: Namesti Microsoft Agent Framework in potrebne pakete 📦

Namesti vse odvisnosti, ki jih delavnica potrebuje:

```bash
pip install -r ./Installations/requirements.txt -U
```

*Namestilo bo Microsoft Agent Framework in vse potrebne pakete. Pripravi si kavo — prvič lahko traja nekaj minut!☕*

## Navodila delavnice

Podrobna struktura projektov, nastavitve in zagon bodo postopoma predstavljeni med delavnico.

## Odpravljanje težav (ko kaj ne gre) 🔧

### "Hej, prenos modela je prepočasen!"
**Rešitev**: Uporabi VPN ali nastavi Ollama zrcalni naslov. Včasih internet ni na naši strani.

### "Moj računalnik crkuje! Premalo pomnilnika!"
**Rešitev**: Preklopi na manjši model ali prilagodi nastavitve `num_ctx` za manjšo porabo RAM-a. Predstavljaj si to kot dieto za tvoj AI.

### "Lahko pohitriš z uporabo GPU-ja?"
**Rešitev**: Ollama samodejno zazna GPU! Samo poskrbi, da so tvoji GPU gonilniki posodobljeni. Brezplačno pohitritev! 🏎️

## Dodatni viri (za radovedne) 📚

- [Ollama dokumentacija](https://github.com/ollama/ollama) — poglobljeno o lokalnih AI modelih
- [Microsoft Agent Framework](https://microsoft.github.io/autogen/) — izvedi več o gradnji ekip agentov
- [Qwen model informacije](https://qwenlm.github.io/) — spoznaj možgane svojega AI asistenta

## Licenca

Licenca MIT — ustvarjaj kul stvari, deli jih in naredi svet boljši! 🌍

## Želiš prispevati?

Našel si bug? Imaš idejo? Pošlji Issue ali PR! Radi imamo skupnost. ✨

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas opozarjamo, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v izvirnem jeziku velja za avtoritativni vir. Za pomembne informacije priporočamo strokovni človeški prevod. Za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda, ne odgovarjamo.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
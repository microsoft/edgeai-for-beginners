<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f94e745264597bc5d8df967ead2eff97",
  "translation_date": "2026-01-05T10:54:36+00:00",
  "source_file": "WorkshopForAgentic/README.md",
  "language_code": "hr"
}
-->
# 🎙️ AI Podcast Studio Radionica

> 🌏 [中文版 (Kineska verzija)](translation/zh-cn/README.md)

![logo](../../../translated_images/hr/logo.8711e39dc8257d7b.png)

## Tvoja Misija

Dobrodošao u **AI Podcast Studio**! Upravo pokrećeš vlastiti tech podcast pod nazivom "Future Bytes" — ali tu je zaplet: izgradit ćeš produkcijski tim pokretan umjetnom inteligencijom da ti pomogne u stvaranju. Nema više beskrajnih sati istraživanja, pisanja scenarija i uređivanja zvuka. Umjesto toga, kodat ćeš za postati producent podcasta s AI supermoćima.

## Priča

Zamisli ovo: ti i tvoji prijatelji želite započeti podcast o najcool tech trendovima, ali su svi zauzeti školom, poslom ili životom općenito. Što ako možeš izgraditi tim AI agenata koji će odraditi težak posao? Jedan agent istražuje teme, drugi piše zanimljive scenarije, a treći pretvara tekst u prirodne razgovore. Zvuči kao znanstvena fantastika? Učinit ćemo da postane stvarnost.

## Što ćeš Naučiti

Do kraja ove radionice znat ćeš kako:
- 🤖 Postaviti vlastiti lokalni AI model (nema troškova API-ja, nema ovisnosti o oblaku!)
- 🔧 Izgraditi specijalizirane AI agente koji zaista surađuju
- 🎬 Kreirati kompletnu produkcijsku liniju podcasta od ideje do zvuka

## Tvoje Putovanje: Tri Čina

![arch](../../../translated_images/hr/arch.5965fe504e4a3a93.png)

Kao i svaka dobra priča, imamo tri čina. Svaki dio gradi tvoj AI podcast studio korak po korak:

| Epizoda | Tvoj Izazov | Što Se Događa | Ovladaš Vještinama |
|---------|-------------|---------------|--------------------|
| **Čin 1** | [Upoznaj svoje AI Pomoćnike](md/01.BuildAIAgentWithSLM.md) | Otkriješ kako stvoriti AI agente koji mogu razgovarati, pretraživati web i rješavati probleme. Razmišljaj o njima kao o istraživačkim pripravnicima koji nikada ne spavaju. | 🎯 Izgradi svog prvog agenta<br>🛠️ Daj mu supermoći (alate!)<br>🧠 Nauči ga razmišljati<br>🌐 Spoji ga na internet |
| **Čin 2** | [Sastavi svoj Produkcijski Tim](md/02.AIAgentOrchestrationAndWorkflows.md) | Sad stvari postaju zanimljive! Koordinirat ćeš više AI agenata da rade zajedno poput pravog podcast tima. Jedan istražuje, drugi piše, ti odobravaš — timski rad donosi uspjeh. | 🎭 Koordiniraj više agenata<br>🔄 Stvori tijekove odobrenja<br>🖥️ Testiraj s DevUI sučeljem<br>✋ Održi kontrolu ljudi |
| **Čin 3** | [Oživljavanje Tvog Podcasta](md/03.Multi-SpeakerPodcastGenerationWithVibeVoice.md) | Finale! Pretvori tekstualne scenarije u stvarni podcast audio s realističnim glasovima i prirodnim razgovorima. Tvoj "Future Bytes" podcast je spreman za lansiranje! | 🎤 Čarolija pretvaranja teksta u govor<br>👥 Više glasova govornika<br>⏱️ Dugotrajan audio<br>🚀 Potpuna automatizacija |

Svaki čin otključava nove sposobnosti. Preskoči ako si hrabar, ali preporučujemo da pratiš priču!

## Zahtjevi Okoliša

Ova radionica podržava razne hardverske okoline:
- **CPU**: Pogodno za testiranje i male svrhe
- **GPU**: Preporuča se za produkcijske okoline, značajno ubrzava izvođenje modela
- **NPU**: Podržava ubrzanje pomoću nove generacije neuralnih procesorskih jedinica

## Što Će Ti Trebati

### Popis Softvera ✅
- **Python 3.10+** (tvoj programski jezik)
- **Ollama** (pokreće AI modele na tvom računalu)
- **VS Code** (tvoj uređivač koda)
- **Python ekstenzija** (za pametniji VS Code)
- **Git** (za preuzimanje koda)

### Provjera Hardvera 💻
- **Mogu li ovo pokrenuti?**: 8GB RAM-a, 10GB slobodnog prostora (radi, ali može biti sporo)
- **Idealna konfiguracija**: 16GB+ RAM-a, solidni GPU (glatko!)
- **Imaš NPU?**: Još bolje! Uključena je sljedeća generacija performansi 🚀

## Postavi Studio 🎬

### Korak 1: Nabavi Python

Provjeri imaš li Python 3.10 ili noviji:

```bash
python --version
# Trebalo bi prikazati Python 3.10.x ili noviji
```

Nemaš Python? Uzmi ga s [python.org](https://python.org) — besplatan je!

### Korak 2: Preuzmi Ollama (pokretač AI modela)

Posjeti [ollama.ai](https://ollama.ai) i preuzmi Ollama za svoj OS. Promisli o njemu kao o motoru koji lokalno pokreće tvoje AI modele.

Provjeri je li spreman:

```bash
ollama --version
```

### Korak 3: Preuzmi svoj AI Mozak 🧠

Vrijeme je da preuzmeš model Qwen-3-8B (kao da zapošljavaš svog prvog AI asistenta):

```bash
ollama pull qwen3:8b
```

*Ovo može potrajati nekoliko minuta. Savršeno vrijeme za pauzu za kavu! ☕*

### Korak 4: Postavi VS Code

Preuzmi [Visual Studio Code](https://code.visualstudio.com/) ako ga nemaš. Najbolji uređivač koda (složite se 😄).

### Korak 5: Python ekstenzija

U VS Code-u:
1. Pritisni `Ctrl+Shift+X` (ili `Cmd+Shift+X` na Macu)
2. Pretraži "Python"
3. Instaliraj službenu Microsoft Python ekstenziju

### Korak 6: Spreman si! 🎉

Stvarno, spreman si za akciju. Idemo stvarati AI magiju!

### Korak 7: Instaliraj Microsoft Agent Framework i povezane pakete 📦

Instaliraj sve potrebne ovisnosti za radionicu:

```bash
pip install -r ./Installations/requirements.txt -U
```

*Ovo će instalirati Microsoft Agent Framework i sve potrebne pakete. Uzmi kavu — prvi put instalacija može potrajati! ☕*

## Upute za Radionicu

Detaljna struktura projekta, koraci konfiguracije i načini pokretanja bit će objašnjeni korak-po-korak tijekom radionice.

## Rješavanje Problema (Kad Stvari Pođu Po Zlu) 🔧

### "Ugh, preuzimanje modela traje vječno!"
**Popravi**: Koristi VPN ili konfiguriraj Ollama s oglednim izvorom. Ponekad internet mrzi nas.

### "Računalo mi umire! Nema memorije!"
**Popravi**: Prebaci na manji model ili promijeni `num_ctx` postavku da koristi manje memorije. Kao da stavljaš AI na dijetu.

### "Mogu li ubrzati s GPU-om?"
**Popravi**: Ollama automatski detektira GPU! Samo provjeri jesu li driveri GPU-a ažurirani. Besplatno ubrzanje! 🏎️

## Dodatni Resursi (Za Znatiželjnike) 📚

- [Ollama dokumentacija](https://github.com/ollama/ollama) — dubinski pogled na lokalne AI modele
- [Microsoft Agent Framework](https://microsoft.github.io/autogen/) — saznaj više o izgradnji timova agenata
- [Qwen Model Info](https://qwenlm.github.io/) — upoznaj mozak svog AI asistenta

## Licenca

MIT licenca — Stvaraj super stvari, dijeli ih, učini svijet boljim! 🌍

## Želiš Doprinijeti?

Pronašao si grešku? Imaš ideju? Otvori Issue ili Pull Request! Volimo pozitivnu zajednicu. ✨

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Odricanje od odgovornosti**:
Ovaj je dokument preveden pomoću AI prevodilačke usluge [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatizirani prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za ključne informacije preporučuje se profesionalni ljudski prijevod. Ne snosimo odgovornost za bilo kakve nesporazume ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
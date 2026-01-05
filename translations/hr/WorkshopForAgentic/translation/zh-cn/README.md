<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "aa775a734bda4590ecbe3a94a3b62197",
  "translation_date": "2026-01-05T17:58:37+00:00",
  "source_file": "WorkshopForAgentic/translation/zh-cn/README.md",
  "language_code": "hr"
}
-->
# 🎙️ AI Podcast Studio Radionica

![logo](../../../../../translated_images/logo.8711e39dc8257d7b.hr.png)

## Tvoj zadatak

Dobrodošao u **AI Podcast Studio**! Upravo krećeš vlastiti tehnološki podcast "Budući Bajt" — ali ovdje je preokret: izgradit ćeš AI vođeni produkcijski tim koji će ti pomoći u stvaranju. Nema više beskrajnih istraživanja, pisanja scenarija i uređivanja zvuka. Umjesto toga, programirat ćeš se u podcast producente s AI supermoćima.

## Pozadina priče

Zamislite: ti i prijatelji želite pokrenuti podcast o najcool tehnološkim trendovima, ali svi su zauzeti učenjem, radom ili životom. Što ako možeš stvoriti tim AI agenata da odrade teške zadatke? Jedan agent istražuje teme, drugi piše zanimljive scenarije, treći pretvara tekst u prirodan i tečan razgovor. Zvuci kao znanstvena fantastika? Pretvorimo to u stvarnost.

## Što ćeš naučiti

Na kraju radionice znat ćeš kako:
- 🤖 Postaviti vlastite lokalne AI modele (bez API troškova, bez ovisnosti o oblaku!)
- 🔧 Izgraditi stvarne kolaborativne profesionalne AI agente
- 🎬 Kreirati cijeli proces produkcije podcasta od ideje do zvuka

## Tvoja avantura: Tri čina

Kao i u svakoj dobroj priči, imamo tri čina. Svaki čin postupno gradi tvoj AI podcast studio:

| Poglavlje | Tvoj zadatak | Što se događa | Otključane vještine |
|---------|-----------|--------------|----------------|
| **Prvi čin** | [Upoznaj svog AI asistenta](01.BuildAIAgentWithSLM.md) | Saznat ćeš kako stvoriti AI agente koji mogu razgovarati, pretraživati mrežu pa čak i rješavati probleme. Zamislite ih kao istraživačke pripravnike koji nikad ne spavaju. | 🎯 Izgradi svog prvog agenta<br>🛠️ Daj mu supermoći (alate!)<br>🧠 Nauči ga razmišljati<br>🌐 Spoji ga na internet |
| **Drugi čin** | [Sastavi svoj produkcijski tim](02.AIAgentOrchestrationAndWorkflows.md) | Sad stvari postaju zanimljive! Koordinirat ćeš više AI agenata da surađuju poput pravog podcast tima. Jedan istražuje, jedan piše, ti odobravaš — timski rad ostvaruje snove. | 🎭 Koordiniraj više agenata<br>🔄 Izgradi tijekove odobravanja<br>🖥️ Testiraj s DevUI sučeljem<br>✋ Održavaj ljudsku kontrolu |
| **Treći čin** | [Oživi svoj podcast](03.Multi-SpeakerPodcastGenerationWithVibeVoice.md) | Veliki finale! Pretvori svoj tekstualni scenarij u stvarni podcast audio s realističnim glasom i prirodnim razgovorom. Tvoj "Budući Bajt" podcast je spreman za lansiranje! | 🎤 Čarolija pretvaranja teksta u govor<br>👥 Višeglasnički glasovi<br>⏱️ Dugi format zvuka<br>🚀 Potpuna automatizacija |

Svaki čin otključava nove sposobnosti. Ako si hrabar, možeš preskakati, ali preporučujemo redoslijed!

## Zahtjevi okoliša

Radionica podržava razne hardverske okoline:
- **CPU**: prikladno za testiranje i male projekte
- **GPU**: preporučeno za produkciju, značajno ubrzava izvođenje
- **NPU**: podrška za sljedeću generaciju akceleratora neuronskih mreža

## Što ti treba

### Softverski popis ✅
- **Python 3.10+** (tvoj programski jezik)
- **Ollama** (pokretač AI modela na tvojem računalu)
- **VS Code** (tvoj uređivač koda)
- **Python ekstenzija** (za pametniji VS Code)
- **Git** (za preuzimanje koda)

### Provjera hardvera 💻
- **Mogu li pokrenuti?**: 8GB RAM-a, 10GB slobodnog prostora (može ali možda sporo)
- **Idealno**: 16GB+ RAM-a, dobra GPU karta (glatko radi!)
- **Imaš li NPU?**: Još bolje! Otključaj sljedeću generaciju performansi 🚀

## Postavi svoj studio 🎬

### Korak 1: Nadogradnja Pythona

Provjeri imaš li Python 3.10 ili noviji:

```bash
python --version
# Trebalo bi prikazati Python 3.10.x ili noviju verziju
```

Nemaš Python? Nabavi ga na [python.org](https://python.org) — besplatan je!

### Korak 2: Nabavi Ollama (tvoj AI pokretač modela)

Posjeti [ollama.ai](https://ollama.ai) i preuzmi Ollama za svoj OS. Zamislite ga kao motor za lokalno pokretanje AI modela.

Provjeri je li spremno:

```bash
ollama --version
```

### Korak 3: Preuzmi svoj AI mozak 🧠

Vrijeme je za model Qwen-3-8B (kao da unajmljuješ prvog AI asistenta):

```bash
ollama pull qwen3:8b
```

*Ovo može potrajati nekoliko minuta. Savršeno vrijeme za kavu! ☕*

### Korak 4: Postavi VS Code

Ako ga još nemaš, nabavi [Visual Studio Code](https://code.visualstudio.com/). To je najbolji uređivač koda (slušaj, ne možeš raspravljati 😄).

### Korak 5: Python ekstenzija

U VS Code-u:
1. Pritisni `Ctrl+Shift+X` (na Macu `Cmd+Shift+X`)
2. Pretraži "Python"
3. Instaliraj Microsoftovu službenu Python ekstenziju

### Korak 6: Gotovo! 🎉

Ozbiljno, spreman si. Idemo stvarati AI magiju!

### Korak 7: Instaliraj Microsoft Agent Framework i potrebne pakete 📦

Instaliraj sve potrebne ovisnosti za radionicu:

```bash
pip install -r ./Installations/requirements.txt -U
```

*Ovo će instalirati Microsoft Agent Framework i sve potrebne pakete. Popij kavu — prva instalacija može potrajati! ☕*

## Upute radionice

Detaljna struktura projekata, koraci konfiguracije i izvođenja bit će objašnjeni tijekom radionice.

## Rješavanje problema (kad stvari krenu po zlu) 🔧

### "Hej, prekratko se model preuzima!"
**Rješenje**: Koristi VPN ili postavi Ollama mirror izvor. Ponekad mreža jednostavno nije pouzdana.

### "Moje računalo je pred kolapsom! Nema dovoljno memorije!"
**Rješenje**: Prebaci na manji model ili prilagodi `num_ctx` da koristi manje memorije. Zamislite to kao dijetu za AI.

### "Mogu li ubrzati s GPU-om?"
**Rješenje**: Ollama automatski prepoznaje GPU! Samo osiguraj da su tvoji GPU driveri ažurirani. Besplatno ubrzanje! 🏎️

## Dodatni resursi (za one znatiželjne) 📚

- [Ollama dokumentacija](https://github.com/ollama/ollama) — nauči više o lokalnim AI modelima
- [Microsoft Agent Framework](https://microsoft.github.io/autogen/) — upoznaj tim momčadi agenata
- [Qwen model informacije](https://qwenlm.github.io/) — upoznaj mozak svog AI asistenta

## Licenca

MIT licenca — stvaraj kul stvari, dijeli ih i učini svijet boljim mjestom! 🌍

## Želiš doprinijeti?

Pronašao si bug? Imaš ideju? Otvori Issue ili PR! Volimo zajednicu. ✨

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Izjava o odricanju od odgovornosti**:
Ovaj dokument je preveden pomoću AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporučuje se profesionalni ljudski prijevod. Ne snosimo odgovornost za bilo kakva nesporazuma ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
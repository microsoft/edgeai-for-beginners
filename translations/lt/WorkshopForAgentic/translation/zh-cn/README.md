<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "aa775a734bda4590ecbe3a94a3b62197",
  "translation_date": "2026-01-05T18:03:18+00:00",
  "source_file": "WorkshopForAgentic/translation/zh-cn/README.md",
  "language_code": "lt"
}
-->
# 🎙️ AI Podcast Studijos dirbtuvės

![logo](../../../../../translated_images/lt/logo.8711e39dc8257d7b.png)

## Tavo užduotis

Sveiki atvykę į **AI Podcast Studiją**! Tu ketini pradėti savo technologijų podcastą „Ateities baitai“ — bet štai pasukimas: tu sukursi AI valdomą gamybos komandą, kuri padės tau jį kurti. Nebereikės begalinio tyrinėjimo, scenarijų rašymo ir garso redagavimo. Vietoj to savo programavimo įgūdžiais tapsi podcasto kūrėju su AI supergalia.

## Istorijos fonas

Įsivaizduok: tu ir draugai norite pradėti podcastą apie karščiausias technologijų tendencijas, bet visi užsiėmę mokslu, darbu ar gyvenimu. O jeigu galėtum sukurti AI agentų komandą, kuri atliktų sunkiąją dalį? Vienas agentas tyrinėja temas, kitas rašo įtraukiančius scenarijus, trečias paverčia tekstą natūralia ir sklandžia kalba. Skamba kaip mokslinė fantastika? Padarykime tai realybe.

## Ko išmoksi

Baigęs šias dirbtuves suprasi, kaip:
- 🤖 Įdiegti savo vietinį AI modelį (be API mokesčių, be debesų priklausomybės!)
- 🔧 Kurti profesionalius AI agentus, dirbančius kartu praktiniu būdu
- 🎬 Sukurti visą podcasto gamybos procesą nuo idėjos iki garso

## Tavo kelionė: trys veiksmai

Kaip ir bet kuri geroji istorija, mes turime tris veiksmus. Kiekvienas žingsnis palaipsniui kurs tavo AI podcast studiją:

| Skyrius | Tavo užduotis | Kas vyksta | Įgūdžių atrakinta |
|---------|---------------|------------|-------------------|
| **Pirmas veiksmas** | [Susipažink su savo AI asistentu](01.BuildAIAgentWithSLM.md) | Sužinosi, kaip sukurti AI agentus, kurie gali kalbėtis, ieškoti internete ir net spręsti problemas. Įsivaizduok juos kaip nekamuojamus mokslinius praktikantus. | 🎯 Sukurk pirmąjį agentą<br>🛠️ Duok jam supergalias (įrankius!)<br>🧠 Išmokyk galvoti<br>🌐 Prisijunk prie interneto |
| **Antras veiksmas** | [Sukurk savo gamybos komandą](02.AIAgentOrchestrationAndWorkflows.md) | Dabar įdomu! Organizuosi daugybę AI agentų dirbančių kaip tikra podcasto komanda. Vienas tyrinėja, kitas rašo, tu patvirtini – komandinė darbštumas lemia sėkmę. | 🎭 Koordinuok daug agentų<br>🔄 Kurk patvirtinimo darbo eigą<br>🖥️ Naudok DevUI sąsają testavimui<br>✋ Išlaikyk žmogišką kontrolę |
| **Trečias veiksmas** | [Leisk savo podcastui įsikūnyti](03.Multi-SpeakerPodcastGenerationWithVibeVoice.md) | Didysis įvykis! Paversk savo scenarijų į tikrą podcasto garsą su realistišku balsu ir natūraliu dialogu. Tavo „Ateities baitai“ yra pasiruošę skelbti! | 🎤 Teksto į kalbą magija<br>👥 Daugiakalbiai balsai<br>⏱️ Ilgo formato garso įrašai<br>🚀 Visiškas automatizavimas |

Kiekvienas veiksmas atrakina naujas galimybes. Jei esi drąsus, gali žiūrėti ir iš eilės, bet rekomenduojame mokytis pagal tvarką!

## Aplinkos reikalavimai

Šios dirbtuvės palaiko įvairią aparatūrą:
- **CPU**: tinka testavimui ir mažos apimties naudojimui
- **GPU**: rekomenduojama gamybai, žymiai pagreitina spėjimą
- **NPU**: palaiko naujos kartos neuroninius procesorius

## Ko tau reikia

### Programinė įranga ✅
- **Python 3.10+** (tavo programavimo kalba)
- **Ollama** (AI modelių vykdyklė tavo kompiuteryje)
- **VS Code** (tavo kodo redaktorius)
- **Python plėtinys** (kad VS Code būtų protingesnis)
- **Git** (kodo atsisiuntimui)

### Aparatūros patikra 💻
- **Ar galiu paleisti?**: 8GB RAM, 10GB laisvos vietos (galima, bet gal lėtoka)
- **Idealus rinkinys**: 16GB+ RAM, gera GPU (sklandus veikimas!)
- **Yra NPU?**: dar geriau! Atrakink naujos kartos greitį 🚀

## Sukurk savo studiją 🎬

### Žingsnis 1: Atnaujink Python

Įsitikink, kad turi Python 3.10 arba naujesnę versiją:

```bash
python --version
# Turėtų būti rodoma Python 3.10.x arba naujesnė versija
```

Neturi Python? Gauk jį iš [python.org](https://python.org) – tai nemokama!

### Žingsnis 2: Parsisiųsk Ollama (tavo AI modelių vykdyklę)

Eik į [ollama.ai](https://ollama.ai) ir atsisiųsk versiją savo operacinei sistemai. Įsivaizduok tai kaip variklį, paleidžiantį AI modelius vietoje.

Patikrink, ar viskas paruošta:

```bash
ollama --version
```

### Žingsnis 3: Parsisiųsk savo AI smegenis 🧠

Laikas gauti Qwen-3-8B modelį (tarsi samdytum pirmąjį AI asistentą):

```bash
ollama pull qwen3:8b
```

*Tai gali užtrukti kelias minutes. Tobulas metas kavai!☕*

### Žingsnis 4: Įdiek VS Code

Jei dar neturi, pasiimk [Visual Studio Code](https://code.visualstudio.com/). Tai geriausias kodo redaktorius (neginčyk 😄).

### Žingsnis 5: Python plėtinys

VS Code:
1. Paspausk `Ctrl+Shift+X` (Mac – `Cmd+Shift+X`)
2. Ieškok „Python“
3. Įdiek oficialų Microsoft Python plėtinį

### Žingsnis 6: Viskas! 🎉

Rimtai, tu pasiruošęs. Kurkime AI magiją!

### Žingsnis 7: Įdiek Microsoft Agent Framework ir reikalingas paketas 📦

Įdiek visas priklausomybes, reikalingas dirbtuvėms:

```bash
pip install -r ./Installations/requirements.txt -U
```

*Tai įdiegia Microsoft Agent Framework ir visus būtinuosius paketus. Gerk kavą — pirmas įdiegimas gali užtrukti kelias minutes!☕*

## Dirbtuvių paaiškinimai

Detalus projekto struktūros, konfigūravimo ir paleidimo paaiškinimas bus pateiktas tvarkingai per visas dirbtuves.

## Gedimų trikčių šalinimas (kai kas nors nepavyksta) 🔧

### „Ei, modelio atsisiuntimas labai lėtas!“
**Sprendimas**: Naudok VPN arba konfigūruok Ollama veidrodžių šaltinį. Kartais tinklas trukdo.

### „Mano kompiuteris jau per daug apkrautas! Nepakanka RAM!“
**Sprendimas**: Perjunk į mažesnį modelį arba sumažink `num_ctx` reikšmę, kad naudotum mažiau atminties. Įsivaizduok, kad dieta tavo AI.

### „Ar galiu naudoti GPU, kad viskas būtų greičiau?“
**Sprendimas**: Ollama automatiškai aptinka GPU! Tiesiog įsitikink, kad tavo GPU tvarkyklės yra atnaujintos. Nemokamas greičio padidinimas!🏎️

## Papildomi ištekliai (smalsiems) 📚

- [Ollama dokumentacija](https://github.com/ollama/ollama) — giliau apie vietinius AI modelius
- [Microsoft Agent Framework](https://microsoft.github.io/autogen/) — sužinok daugiau apie agentų komandų kūrimą
- [Qwen modelio informacija](https://qwenlm.github.io/) — pažink savo AI asistento smegenis

## Licencija

MIT licencija — kurk nuostabius dalykus, dalinkis jais ir padaryk pasaulį geresnį! 🌍

## Nori prisidėti?

Radai klaidą? Turi idėjų? Pateik Issue arba PR! Mes mėgstame bendruomenės dvasią. ✨

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas gimtąja kalba turi būti laikomas autoritetingu šaltiniu. Kritinės informacijos atveju rekomenduojama naudoti profesionalų žmogaus vertimą. Mes nerenkame atsakomybės už bet kokius nesusipratimus ar klaidingą interpretaciją, kilusią dėl šio vertimo naudojimo.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
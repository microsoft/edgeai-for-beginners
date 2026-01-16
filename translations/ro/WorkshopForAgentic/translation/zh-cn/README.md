<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "aa775a734bda4590ecbe3a94a3b62197",
  "translation_date": "2026-01-05T17:55:42+00:00",
  "source_file": "WorkshopForAgentic/translation/zh-cn/README.md",
  "language_code": "ro"
}
-->
# 🎙️ Atelier AI Podcast Studio

![logo](../../../../../translated_images/ro/logo.8711e39dc8257d7b.png)

## Sarcina ta

Bine ai venit la **AI Podcast Studio**! Ești pe punctul de a lansa propriul tău podcast tech „Future Bytes” — dar iată o schimbare: vei construi o echipă de producție AI care să te ajute să-l creezi. Nu mai este nevoie de cercetare nesfârșită, scrierea scenariilor și editare audio. În schimb, vei deveni un producător de podcasturi cu superputeri AI prin programare.

## Povestea

Imaginează-ți: tu și prietenii voștri vreți să începeți un podcast despre cele mai tari tendințe tehnologice, dar toți sunt ocupați cu învățatul, munca sau viața personală. Ce-ar fi dacă ai putea construi o echipă de agenți inteligenți AI care să facă munca grea? Un agent cercetează subiectul, altul scrie scenarii captivante, iar un al treilea transformă textul în dialoguri naturale. Sună ca science-fiction? Hai să o facem realitate.

## Ce vei învăța

La finalul acestui atelier, vei ști cum să:
- 🤖 Rulezi propriul model AI local (fără costuri API, fără dependență de cloud!)
- 🔧 Construiești agenți inteligenți AI profesioniști care colaborează efectiv
- 🎬 Creezi un flux complet de producție a podcastului, de la idee la audio

## Călătoria ta: în trei acte

Ca orice poveste bună, avem trei acte. Fiecare act construiește treptat studioul tău AI pentru podcast:

| Capitol | Sarcina ta | Ce se întâmplă | Abilități noi |
|---------|------------|----------------|---------------|
| **Actul 1** | [Cunoaște-ți asistentul AI](01.BuildAIAgentWithSLM.md) | Vei afla cum să creezi agenți inteligenți AI care pot conversa, căuta pe web și chiar rezolva probleme. Imaginează-ți-i ca stagiarii de cercetare care nu dorm niciodată. | 🎯 Construiește-ți primul agent<br>🛠️ Oferă-i superputeri (unelte!)<br>🧠 Învață-l să gândească<br>🌐 Conectează-l la internet |
| **Actul 2** | [Construiți echipa de producție](02.AIAgentOrchestrationAndWorkflows.md) | Acum devine interesant! Vei orchestra mai mulți agenți AI să lucreze în echipă, ca într-un adevărat studio de podcast. Unul cercetează, altul scrie, tu validezi — echipa face magii. | 🎭 Coordonează mai mulți agenți<br>🔄 Construiește fluxuri de aprobare<br>🖥️ Testează interfețele DevUI<br>✋ Păstrează controlul uman |
| **Actul 3** | [Dă viață podcastului tău](03.Multi-SpeakerPodcastGenerationWithVibeVoice.md) | Marele final! Transformă-ți scenariul text în audio podcast cu voci realiste și conversații naturale. Podcastul tău „Future Bytes” este gata de lansare! | 🎤 Magia text-to-speech<br>👥 Voci multiple<br>⏱️ Audio de lungă durată<br>🚀 Complet automatizat |

Fiecare act îți va debloca noi puteri. Poți sări peste, dacă ești curajos, dar recomandăm să urmezi ordinea!

## Cerințe de mediu

Atelierul este compatibil cu diverse configurații hardware:
- **CPU**: potrivit pentru testare și utilizare redusă
- **GPU**: recomandat pentru producție, crește semnificativ viteza de inferență
- **NPU**: suportă accelerarea noilor unități neuronale

## Ce îți trebuie

### Liste software ✅
- **Python 3.10+** (limbajul tău de programare)
- **Ollama** (motorul tău local pentru modele AI)
- **VS Code** (editorul tău de cod)
- **Extensia Python** (pentru a face VS Code mai inteligent)
- **Git** (pentru a obține codul)

### Verificare hardware 💻
- **Pot rula?**: 8GB memorie RAM, 10GB spațiu disponibil (funcționează, dar poate fi lent)
- **Configurația ideală**: 16GB+ RAM, un GPU decent (rulare fluentă!)
- **Ai NPU?**: și mai bine! Deblochează performanțe de generație următoare 🚀

## Construiește-ți studioul 🎬

### Pasul 1: Actualizează Python

Asigură-te că ai Python 3.10 sau o versiune mai nouă:

```bash
python --version
# Ar trebui să afișeze Python 3.10.x sau o versiune mai nouă
```

Nu ai Python? Obține-l de la [python.org](https://python.org) — este gratuit!

### Pasul 2: Descarcă Ollama (motorul tău AI)

Mergi la [ollama.ai](https://ollama.ai) și descarcă Ollama pentru sistemul tău de operare. Gândește-te la el ca la un motor care rulează modele AI local.

Verifică dacă a fost instalat corect:

```bash
ollama --version
```

### Pasul 3: Descarcă creierul AI 🧠

E timpul să descarci modelul Qwen-3-8B (ca și cum ai angaja primul tău asistent AI):

```bash
ollama pull qwen3:8b
```

*Acest proces poate dura câteva minute. Perfect pentru o cafea! ☕*

### Pasul 4: Configurează VS Code

Dacă nu-l ai, descarcă [Visual Studio Code](https://code.visualstudio.com/). Este cel mai bun editor de cod (provocări acceptate 😄).

### Pasul 5: Extensia Python

În VS Code:
1. Apasă `Ctrl+Shift+X` (pe Mac este `Cmd+Shift+X`)
2. Caută „Python”
3. Instalează extensia oficială Microsoft Python

### Pasul 6: Gata! 🎉

Serios, ești pregătit. Hai să facem puțină magie AI!

### Pasul 7: Instalează Microsoft Agent Framework și pachetele necesare 📦

Instalează toate dependențele pentru atelier:

```bash
pip install -r ./Installations/requirements.txt -U
```

*Aceasta va instala Microsoft Agent Framework și toate pachetele necesare. Ia o nouă cafea — prima instalare poate dura câteva minute! ☕*

## Instrucțiuni atelier

Structura detaliată a proiectului, pașii de configurare și modul de rulare vor fi explicate pe parcursul atelierului.

## Îndrumări când ceva nu merge 🔧

### „Ah, descărcarea modelului este prea lentă!”
**Soluție**: folosește VPN sau configurează o sursă de oglindă (mirror) pentru Ollama. Uneori conexiunea lasă de dorit.

### „Calculatorul meu e suprasolicitat! Memorie insuficientă!”
**Soluție**: schimbă la un model mai mic sau ajustează setarea `num_ctx` pentru a folosi mai puțină memorie. Gândește-te la o dietă pentru AI-ul tău.

### „Pot folosi GPU-ul să-l accelerez?”
**Soluție**: Ollama detectează automat GPU-ul! Asigură-te doar că driver-ul GPU este actualizat. Un boost rapid și gratuit! 🏎️

## Resurse suplimentare (pentru cei curioși) 📚

- [Documentația Ollama](https://github.com/ollama/ollama) — află mai multe despre modelele AI locale
- [Microsoft Agent Framework](https://microsoft.github.io/autogen/) — învață cum să construiești echipe de agenți inteligenți
- [Informații despre modelul Qwen](https://qwenlm.github.io/) — cunoaște creierul asistentului tău AI

## Licență

Licență MIT — construiește lucruri tari, împărtășește-le și fă lumea mai bună! 🌍

## Vrei să contribui?

Ai găsit un bug? Ai o idee? Deschide un Issue sau un PR! Ne place comunitatea noastră. ✨

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare de responsabilitate**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de o persoană. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite cauzate de utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
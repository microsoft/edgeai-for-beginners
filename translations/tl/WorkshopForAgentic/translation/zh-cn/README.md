# 🎙️ AI Podcast Studio Workshop

![logo](../../../../../translated_images/tl/logo.8711e39dc8257d7b.webp)

## Ang Iyong Gawain

Maligayang pagdating sa **AI Podcast Studio**! Maglulunsad ka ng sarili mong tech podcast na "Future Bytes"—ngunit may twist: bubuuin mo ang isang AI-driven production team upang tulungan kang likhain ito. Hindi mo na kailangan ng walang katapusang pananaliksik, pagsusulat ng script, at audio editing. Sa halip, magiging podcast producer ka na may AI superpowers sa pamamagitan ng programming.

## Background ng Kwento

Isipin ito: gusto ninyong magsimula ng podcast tungkol sa pinakamainit na tech trends ng iyong mga kaibigan, pero abala ang lahat sa pag-aaral, trabaho, o buhay. Paano kung makakabuo ka ng AI agent team para gawin ang mabibigat na gawain? Isang agent ang mag-reresearch ng mga topic, isa ang susulat ng kapana-panabik na script, at ang pangatlo ay gagawa ng text sa natural na daloy ng pag-uusap. Parang sci-fi? Gawin natin itong realidad.

## Ano ang Matututuhan Mo

Sa pagtatapos ng workshop na ito, malalaman mo kung paano:
- 🤖 Mag-deploy ng sarili mong lokal na AI model (walang API fees, walang cloud dependency!)
- 🔧 Bumuo ng tunay na professional AI agent na nagtutulungan
- 🎬 Lumikha ng buong podcast production workflow mula ideya hanggang audio

## Ang Iyong Paglalakbay: Tatlong Yugto

Tulad ng anumang magandang kwento, may tatlong yugto tayo. Unti-unting bubuuin nito ang iyong AI podcast studio:

| Kabanata | Ang Iyong Gawain | Ano ang Nangyayari | Mga Matutunang Kasanayan |
|---------|-----------|--------------|----------------|
| **Yugto 1** | [Kilalanin ang Iyong AI Assistant](01.BuildAIAgentWithSLM.md) | Matutuklasan mo kung paano lumikha ng AI agents na kaya makipag-chat, mag-search sa web, at mag-solve ng problema. Isipin sila bilang mga research intern na kailanman ay hindi natutulog. | 🎯 Buuhin ang iyong unang agent<br>🛠️ Bigyan ito ng mga superpower (tools!)<br>🧠 Turuan itong mag-isip<br>🌐 Ikonekta sa internet |
| **Yugto 2** | [Buuin ang Iyong Production Team](02.AIAgentOrchestrationAndWorkflows.md) | Ngayon ay nagiging masaya! Mag-orchestrate ka ng maraming AI agents na nagtutulungan tulad ng isang tunay na podcast team. Isa ang nag-rereasearch, isa ang nagsusulat, at ikaw ang nag-aapruba—teamwork makes the dream work. | 🎭 Mag-coordinate ng maraming agents<br>🔄 Bumuo ng approval workflow<br>🖥️ Subukan gamit ang DevUI interface<br>✋ Panatilihin ang human control |
| **Yugto 3** | [Buhayin ang Iyong Podcast](03.Multi-SpeakerPodcastGenerationWithVibeVoice.md) | Ang grand finale! I-convert ang iyong text script sa totoong podcast audio na may makatotohanang boses at natural na talakayan. Handa na ang iyong "Future Bytes" podcast para ilathala! | 🎤 Text-to-speech magic<br>👥 Multi-speaker voices<br>⏱️ Long-form audio<br>🚀 Full automation |

Bawat yugto ay magbibigay sa iyo ng bagong kakayahan. Kung matapang ka, maaari kang mag-skip, pero inirerekomenda naming sundan ang ayos!

## Mga Kinakailangan sa Kapaligiran

Sinusuportahan ng workshop na ito ang iba't ibang hardware environment:
- **CPU**: Para sa testing at maliit na scale na paggamit
- **GPU**: Inirerekomenda para sa production, nagpapabilis ng inference nang malaki
- **NPU**: Suporta sa susunod na henerasyong neural processing unit acceleration

## Ano ang Kailangan Mo

### Listahan ng Software ✅
- **Python 3.10+** (iyong programming language)
- **Ollama** (patakbuhin ang AI model sa iyong makina)
- **VS Code** (iyong code editor)
- **Python extension** (para gawing mas intelihente ang VS Code)
- **Git** (para i-clone ang code)

### Hardware Check 💻
- **Kayang tumakbo?**: 8GB RAM, 10GB libreng espasyo (pwedeng-pwede pero maaaring medyo mabagal)
- **Ideal na setup**: 16GB+ RAM, magandang GPU (smooth na takbo!)
- **May NPU?**: Mas maganda pa! Unlock next-gen performance 🚀

## Itayo ang Iyong Studio 🎬

### Hakbang 1: I-update ang Python

Siguraduhing may Python 3.10 o mas bago ka:

```bash
python --version
# Dapat ipakita ang Python 3.10.x o mas mataas na bersyon
```

Walang Python? Kunin ito mula sa [python.org](https://python.org)—libre ito!

### Hakbang 2: Kunin ang Ollama (iyong AI model runner)

Pumunta sa [ollama.ai](https://ollama.ai) para i-download ang Ollama na angkop sa iyong OS. Isipin ito bilang engine na nagpapatakbo ng AI models locally.

Suriin kung nakahanda na:

```bash
ollama --version
```

### Hakbang 3: I-download ang Iyong AI Brain 🧠

Panahon na para i-download ang Qwen-3-8B model (parang pagkuha ng unang AI assistant):

```bash
ollama pull qwen3:8b
```

*Maaaring tumagal ng ilang minuto ito. Perfect na break para sa kape! ☕*

### Hakbang 4: I-setup ang VS Code

Kung wala ka pa nito, kunin ang [Visual Studio Code](https://code.visualstudio.com/). Ito ang pinakamahusay na code editor (challenge accepted 😄).

### Hakbang 5: Python Extension

Sa VS Code:
1. Pindutin ang `Ctrl+Shift+X` (o `Cmd+Shift+X` sa Mac)
2. Hanapin ang "Python"
3. I-install ang official na Microsoft Python extension

### Hakbang 6: Handang-handang ka na! 🎉

Todo seriousness, handa kana. Tara, magbuhos tayo ng ilang AI magic!

### Hakbang 7: I-install ang Microsoft Agent Framework at mga kaugnay na package 📦

I-install ang lahat ng dependencies na kailangan para sa workshop:

```bash
pip install -r ./Installations/requirements.txt -U
```

*Ito ay mag-iinstall ng Microsoft Agent Framework at lahat ng kinakailangang packages. Kumuha ng kape habang hinihintay — maaaring tumagal sa unang installation! ☕*

## Mga Tagubilin sa Workshop

Ang detalyadong project structure, setup steps, at paano paandarin ay ipapaliwanag nang paunti-unti habang ginaganap ang workshop.

## Troubleshooting (Kapag May Problema) 🔧

### "Naku, sobrang bagal ng download ng model!"
**Solusyon**: Gumamit ng VPN o i-configure ang Ollama mirror source. Minsan lang talagang mahinang koneksyon.

### "Pabagsak na ang PC ko! Kulang ang memory!"
**Solusyon**: Lumipat sa mas maliit na modelo o bawasan ang `num_ctx` setting para gamitin ang mas kaunting memory. Parang diet lang para sa AI mo.

### "Pwedeng pabilisin gamit ang GPU?"
**Solusyon**: Auto-detect ng Ollama ang GPU! Siguraduhing updated ang GPU driver mo. Libre at mabilis! 🏎️

## Karagdagang Mga Resources (Para sa mga Curious) 📚

- [Ollama Docs](https://github.com/ollama/ollama) — Malalim na pag-aaral sa lokal na AI models
- [Microsoft Agent Framework](https://microsoft.github.io/autogen/) — Alamin pa tungkol sa pagbuo ng agent teams
- [Qwen Model Info](https://qwenlm.github.io/) — Kilalanin ang utak ng iyong AI assistant

## Lisensya

MIT License — Gumawa ng cool na bagay, ibahagi, at pagandahin ang mundo! 🌍

## Gusto Mo Bang Mag-ambag?

Nakakita ng bug? May ideya? Mag-submit ng Issue o PR! Gustung-gusto namin ang community vibe. ✨

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Paunawa**:
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat sinisikap naming maging tumpak, pakatandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o di-tumpak na impormasyon. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsusaling-pantao. Hindi kami mananagot sa anumang hindi pagkakaintindihan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e8d157e0a282083a1e1c7bb5dda28646",
  "translation_date": "2025-10-30T15:02:08+00:00",
  "source_file": "Module04/README.md",
  "language_code": "sl"
}
-->
# Poglavje 04: Pretvorba modelov in kvantizacija - Pregled poglavja

Pojav EdgeAI je naredil pretvorbo modelov in kvantizacijo ključni tehnologiji za uvajanje naprednih zmogljivosti strojnega učenja na napravah z omejenimi viri. To obsežno poglavje ponuja celovit vodnik za razumevanje, izvajanje in optimizacijo modelov za scenarije uvajanja na robu.

## 📚 Struktura poglavja in učna pot

Poglavje je organizirano v sedem progresivnih razdelkov, ki se med seboj nadgrajujejo, da ustvarijo celovito razumevanje optimizacije modelov za robno računalništvo:

---

## [Razdelek 1: Osnove pretvorbe modelov in kvantizacije](./01.Introduce.md)

### 🎯 Pregled
Ta osnovni razdelek vzpostavlja teoretični okvir za optimizacijo modelov v okoljih robnega računalništva, pokriva meje kvantizacije od 1-bitne do 8-bitne natančnosti ter ključne strategije pretvorbe formatov.

**Ključne teme:**
- Okvir za razvrščanje natančnosti (zelo nizka, nizka, srednja natančnost)
- Prednosti in uporaba formatov GGUF in ONNX
- Prednosti kvantizacije za operativno učinkovitost in prilagodljivost uvajanja
- Primerjave zmogljivosti in pomnilniških zahtev

**Učni cilji:**
- Razumeti meje kvantizacije in razvrstitve
- Prepoznati ustrezne tehnike pretvorbe formatov
- Naučiti se naprednih strategij optimizacije za robno uvajanje

---

## [Razdelek 2: Vodnik za implementacijo Llama.cpp](./02.Llamacpp.md)

### 🎯 Pregled
Celovit vodič za implementacijo Llama.cpp, zmogljivega C++ okvira, ki omogoča učinkovito sklepanje velikih jezikovnih modelov z minimalno nastavitvijo na različnih strojnih konfiguracijah.

**Ključne teme:**
- Namestitev na platformah Windows, macOS in Linux
- Pretvorba formata GGUF in različne ravni kvantizacije (Q2_K do Q8_0)
- Pospeševanje strojne opreme s CUDA, Metal, OpenCL in Vulkan
- Integracija s Pythonom in strategije za produkcijsko uvajanje

**Učni cilji:**
- Obvladati namestitev na različnih platformah in gradnjo iz izvorne kode
- Izvesti kvantizacijo modelov in tehnike optimizacije
- Uvajati modele v strežniškem načinu z integracijo REST API

---

## [Razdelek 3: Microsoft Olive Optimization Suite](./03.MicrosoftOlive.md)

### 🎯 Pregled
Raziskovanje Microsoft Olive, orodja za optimizacijo modelov, ki upošteva strojno opremo, z več kot 40 vgrajenimi komponentami za optimizacijo, zasnovanega za uvajanje modelov na ravni podjetja na različnih strojnih platformah.

**Ključne teme:**
- Funkcije samodejne optimizacije z dinamično in statično kvantizacijo
- Inteligenca, ki upošteva strojno opremo, za uvajanje na CPU, GPU in NPU
- Podpora priljubljenim modelom (Llama, Phi, Qwen, Gemma) brez dodatnih nastavitev
- Integracija v podjetja z Azure ML in produkcijskimi delovnimi tokovi

**Učni cilji:**
- Izkoristiti samodejno optimizacijo za različne arhitekture modelov
- Izvesti strategije uvajanja na različnih platformah
- Vzpostaviti optimizacijske procese, pripravljene za podjetja

---

## [Razdelek 4: OpenVINO Toolkit Optimization Suite](./04.openvino.md)

### 🎯 Pregled
Celovito raziskovanje Intelovega orodja OpenVINO, odprtokodne platforme za uvajanje zmogljivih AI rešitev v oblaku, lokalno in na robu, z naprednimi zmogljivostmi Neural Network Compression Framework (NNCF).

**Ključne teme:**
- Uvajanje na različnih platformah s pospeševanjem strojne opreme (CPU, GPU, VPU, AI pospeševalniki)
- Neural Network Compression Framework (NNCF) za napredno kvantizacijo in obrezovanje
- OpenVINO GenAI za optimizacijo in uvajanje velikih jezikovnih modelov
- Zmožnosti strežnika modelov na ravni podjetja in strategije za skalabilno uvajanje

**Učni cilji:**
- Obvladati pretvorbo modelov in delovne tokove optimizacije z OpenVINO
- Izvesti napredne tehnike kvantizacije z NNCF
- Uvajati optimizirane modele na različnih strojnih platformah s strežnikom modelov

---

## [Razdelek 5: Poglobljena analiza Apple MLX Framework](./05.AppleMLX.md)

### 🎯 Pregled
Celovita pokritost Apple MLX, revolucionarnega okvira, posebej zasnovanega za učinkovito strojno učenje na Apple Silicon, s poudarkom na zmogljivostih velikih jezikovnih modelov in lokalnem uvajanju.

**Ključne teme:**
- Prednosti enotne pomnilniške arhitekture in Metal Performance Shaders
- Podpora za modele LLaMA, Mistral, Phi-3, Qwen in Code Llama
- LoRA fino uglaševanje za učinkovito prilagajanje modelov
- Integracija s Hugging Face in podpora za kvantizacijo (4-bitna in 8-bitna)

**Učni cilji:**
- Obvladati optimizacijo za Apple Silicon za uvajanje velikih jezikovnih modelov
- Izvesti tehnike fino uglaševanja in prilagajanja modelov
- Graditi AI aplikacije na ravni podjetja z izboljšanimi funkcijami zasebnosti

---

## [Razdelek 6: Sinteza delovnega toka razvoja Edge AI](./06.workflow-synthesis.md)

### 🎯 Pregled
Celovita sinteza vseh optimizacijskih okvirov v enotne delovne tokove, odločitvene matrike in najboljše prakse za uvajanje Edge AI, pripravljeno za produkcijo, na različnih platformah in primerih uporabe, vključno z mobilnimi, namiznimi in oblačnimi okolji.

**Ključne teme:**
- Arhitektura enotnega delovnega toka, ki vključuje več optimizacijskih okvirov
- Odločitvena drevesa za izbiro okvirov in analiza kompromisov zmogljivosti
- Validacija pripravljenosti za produkcijo in celovite strategije uvajanja
- Strategije za prihodnjo prilagoditev za nastajajočo strojno opremo in arhitekture modelov

**Učni cilji:**
- Obvladati sistematično izbiro okvirov glede na zahteve in omejitve
- Izvesti produkcijske Edge AI procese z obsežnim spremljanjem
- Oblikovati prilagodljive delovne tokove, ki se razvijajo z nastajajočimi tehnologijami in zahtevami

---

## [Razdelek 7: Qualcomm QNN Optimization Suite](./07.QualcommQNN.md)

### 🎯 Pregled
Celovito raziskovanje Qualcomm QNN (Qualcomm Neural Network), enotnega okvira za AI sklepanje, zasnovanega za izkoriščanje Qualcommove heterogene računalniške arhitekture, vključno s Hexagon NPU, Adreno GPU in Kryo CPU, za maksimalno zmogljivost in energetsko učinkovitost na mobilnih in robnih napravah.

**Ključne teme:**
- Heterogeno računalništvo z enotnim dostopom do NPU, GPU in CPU
- Optimizacija, ki upošteva strojno opremo, za Snapdragon platforme z inteligentno porazdelitvijo delovne obremenitve
- Napredne tehnike kvantizacije (INT8, INT16, mešana natančnost) za mobilno uvajanje
- Energetsko učinkovito sklepanje, optimizirano za naprave na baterijski pogon in aplikacije v realnem času

**Učni cilji:**
- Obvladati pospeševanje strojne opreme Qualcomm za mobilno AI uvajanje
- Izvesti energetsko učinkovite strategije optimizacije za robno računalništvo
- Uvajati modele, pripravljene za produkcijo, v Qualcommovem ekosistemu z optimalno zmogljivostjo

---

## 🎯 Učni cilji poglavja

Po zaključku tega obsežnega poglavja bodo bralci dosegli:

### **Tehnično obvladovanje**
- Globoko razumevanje meja kvantizacije in praktičnih aplikacij
- Praktične izkušnje z več optimizacijskimi okviri
- Veščine za produkcijsko uvajanje v okoljih robnega računalništva

### **Strateško razumevanje**
- Sposobnosti izbire optimizacije, ki upošteva strojno opremo
- Informirano odločanje o kompromisih zmogljivosti
- Strategije za uvajanje in spremljanje, pripravljene za podjetja

### **Primerjalne zmogljivosti**

| Okvir       | Kvantizacija | Uporaba pomnilnika | Izboljšanje hitrosti | Primer uporabe              |
|-------------|--------------|--------------------|----------------------|-----------------------------|
| Llama.cpp   | Q4_K_M       | ~4GB              | 2-3x                | Uvajanje na različnih platformah |
| Olive       | INT4         | 60-75% zmanjšanje | 2-6x                | Delovni tokovi na ravni podjetja |
| OpenVINO    | INT8/INT4    | 50-75% zmanjšanje | 2-5x                | Optimizacija za Intel strojno opremo |
| QNN         | INT8/INT4    | 50-80% zmanjšanje | 5-15x               | Mobilno/robno uvajanje Qualcomm |
| MLX         | 4-bit        | ~4GB              | 2-4x                | Optimizacija za Apple Silicon |

## 🚀 Naslednji koraki in napredne aplikacije

To poglavje ponuja popolno osnovo za:
- Razvoj prilagojenih modelov za specifične domene
- Raziskave na področju optimizacije Edge AI
- Razvoj komercialnih AI aplikacij
- Velike podjetniške uvajanja Edge AI

Znanje iz teh sedmih razdelkov ponuja celovit nabor orodij za navigacijo po hitro razvijajočem se področju optimizacije in uvajanja modelov Edge AI.

---

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za prevajanje AI [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne odgovarjamo za morebitne nesporazume ali napačne razlage, ki izhajajo iz uporabe tega prevoda.
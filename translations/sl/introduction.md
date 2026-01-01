<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "22c6dae04591abc5f0d80f944ed663d5",
  "translation_date": "2025-09-26T10:46:45+00:00",
  "source_file": "introduction.md",
  "language_code": "sl"
}
-->
# Uvod v Edge AI za začetnike

![Uvod v Edge AI](../../translated_images/cover.eb18d1b9605d754b.sl.png)

Dobrodošli na vaši poti v **Edge umetno inteligenco** – revolucionarni pristop, ki prinaša moč AI neposredno tja, kjer se ustvarjajo podatki in sprejemajo odločitve. Ta uvod bo postavil temelje za razumevanje, zakaj Edge AI predstavlja prihodnost inteligentnega računalništva in kako lahko obvladate njegovo implementacijo.

## Kaj je Edge AI?

Edge AI pomeni temeljni premik od tradicionalne obdelave AI v oblaku k **lokalni, napravi lastni inteligenci**. Namesto pošiljanja podatkov na oddaljene strežnike Edge AI obdeluje informacije neposredno na robnih napravah – pametnih telefonih, IoT senzorjih, industrijski opremi, avtonomnih vozilih in vgrajenih sistemih.

### Paradigma Edge AI

```
Traditional AI:     Device → Cloud → Processing → Response → Device
Edge AI:           Device → Local Processing → Immediate Response
```

Ta premik paradigme odpravlja potrebo po obdelavi v oblaku in omogoča:
- **Takojšnje odzive** (latenca pod milisekundo)
- **Izboljšano zasebnost** (podatki ne zapustijo naprave)
- **Zanesljivo delovanje** (deluje brez internetne povezave)
- **Znižane stroške** (minimalna uporaba pasovne širine in oblačne obdelave)

## Zakaj je Edge AI pomemben zdaj

### Popolna nevihta inovacij

Tri tehnološke smernice so se združile, da Edge AI ni le mogoč, ampak nujen:

1. **Revolucija strojne opreme**: Sodobni čipi (Apple Silicon, Qualcomm Snapdragon, NVIDIA Jetson) zdaj vključujejo AI pospeševanje v kompaktnih, energetsko učinkovitih paketih
2. **Optimizacija modelov**: Majhni jezikovni modeli (SLM) kot Phi-4, Gemma in Mistral zagotavljajo 80-90 % zmogljivosti velikih modelov v 10-20 % velikosti
3. **Potrebe industrije**: Panoge zahtevajo takojšnjo, zasebno in zanesljivo AI, ki je oblačne rešitve ne morejo zagotoviti

### Ključni poslovni dejavniki

**Zasebnost in skladnost**
- Zdravstvo: Podatki pacientov morajo ostati lokalni (skladnost s HIPAA)
- Finance: Obdelava transakcij zahteva suverenost podatkov
- Proizvodnja: Lastniški procesi potrebujejo zaščito pred izpostavitvijo

**Zahteve glede zmogljivosti**
- Avtonomna vozila: Življenjsko pomembne odločitve v milisekundah
- Industrijska avtomatizacija: Nadzor kakovosti in varnosti v realnem času
- Igre in AR/VR: Potopitvene izkušnje zahtevajo ničelno zaznavno latenco

**Ekonomska učinkovitost**
- Telekomunikacije: Lokalna obdelava milijonov IoT senzorjev
- Trgovina: Analitika v trgovinah brez velikih stroškov pasovne širine
- Pametna mesta: Razpršena inteligenca na tisočih napravah

## Panoge, ki jih je Edge AI preoblikoval

### 🏭 **Proizvodnja in Industrija 4.0**
- **Prediktivno vzdrževanje**: AI modeli na industrijski opremi napovedujejo okvare, preden se zgodijo
- **Nadzor kakovosti**: Zaznavanje napak v realnem času na proizvodnih linijah
- **Nadzor varnosti**: Takojšnje zaznavanje nevarnosti in odziv
- **Dobavna veriga**: Inteligentno upravljanje zalog na vsakem vozlišču

**Vpliv v resničnem svetu**: Siemens uporablja Edge AI za prediktivno vzdrževanje, kar zmanjša čas izpadov za 30-50 % in stroške vzdrževanja za 25 %.

### 🏥 **Zdravstvo in medicinske naprave**
- **Diagnostično slikanje**: Analiza rentgenskih in MRI slik z AI na mestu oskrbe
- **Nadzor pacientov**: Neprekinjeno ocenjevanje zdravja prek nosljivih naprav
- **Pomoč pri operacijah**: Vodenje v realnem času med postopki
- **Raziskovanje zdravil**: Lokalna obdelava molekularnih simulacij

**Vpliv v resničnem svetu**: Philipsove Edge AI rešitve omogočajo radiologom, da diagnosticirajo stanja 40 % hitreje ob ohranjanju 99 % natančnosti.

### 🚗 **Avtonomni sistemi in transport**
- **Samovozeča vozila**: Odločanje v delčku sekunde za navigacijo in varnost
- **Upravljanje prometa**: Inteligentno upravljanje križišč in optimizacija pretoka
- **Upravljanje voznih parkov**: Optimizacija poti v realnem času in nadzor zdravja vozil
- **Logistika**: Avtonomni robotski sistemi v skladiščih in dostavi

**Vpliv v resničnem svetu**: Teslin sistem Full Self-Driving lokalno obdeluje podatke senzorjev in sprejema več kot 40 odločitev na sekundo za varno avtonomno navigacijo.

### 🏙️ **Pametna mesta in infrastruktura**
- **Javna varnost**: Zaznavanje groženj v realnem času in odziv na nujne primere
- **Upravljanje energije**: Optimizacija pametnih omrežij in integracija obnovljivih virov energije
- **Okoljsko spremljanje**: Spremljanje kakovosti zraka, hrupa in podnebja
- **Urbanistično načrtovanje**: Analiza prometnih tokov in optimizacija infrastrukture

**Vpliv v resničnem svetu**: Pobuda pametnega mesta v Singapurju uporablja več kot 100.000 Edge AI senzorjev za upravljanje prometa, kar zmanjša čas vožnje za 25 %.

### 📱 **Potrošniška tehnologija in mobilne naprave**
- **Pametni telefoni**: Izboljšana fotografija, glasovni asistenti in personalizacija
- **Pametni domovi**: Inteligentna avtomatizacija in varnostni sistemi
- **Nosljive naprave**: Spremljanje zdravja in optimizacija telesne pripravljenosti
- **Igranje iger**: Izboljšanje grafike v realnem času in optimizacija igranja

**Vpliv v resničnem svetu**: Applov Neural Engine lokalno obdeluje 15,8 bilijona operacij na sekundo, kar omogoča funkcije, kot so prevajanje v realnem času in računalniška fotografija.

## Majhni jezikovni modeli: Motor Edge AI

### Kaj so majhni jezikovni modeli (SLM)?

SLM so **stisnjene, optimizirane različice** velikih jezikovnih modelov, posebej zasnovane za robno uporabo:

- **Phi-4**: 14B parametrov, optimiziran za razmišljanje in generiranje kode
- **Gemma 2B/7B**: Googlove učinkovite modele za raznolike NLP naloge
- **Mistral-7B**: Visoko zmogljiv model s komercialno prijazno licenco
- **Qwen serija**: Alibabini večjezični modeli, optimizirani za mobilno uporabo

### Prednosti SLM

| Zmožnost | Veliki jezikovni modeli | Majhni jezikovni modeli |
|----------|--------------------------|--------------------------|
| **Velikost** | 70B-405B parametrov | 1B-14B parametrov |
| **Pomnilnik** | 40-200GB RAM | 2-16GB RAM |
| **Hitrost sklepanja** | 2-10 sekund | 50-500ms |
| **Namestitev** | Strežniki višjega razreda | Pametni telefoni, vgrajene naprave |
| **Stroški** | $1000s/mesec | Enkratni stroški strojne opreme |
| **Zasebnost** | Podatki se pošiljajo v oblak | Obdelava ostane lokalna |

### Resničnost zmogljivosti

Sodobni SLM dosegajo izjemne zmogljivosti:
- **90 % zmogljivosti GPT-3.5** pri mnogih nalogah
- **Sposobnosti pogovora v realnem času**
- **Generiranje in odpravljanje napak v kodi**
- **Večjezično prevajanje**
- **Analiza in povzemanje dokumentov**

## Cilji učenja

Z zaključkom tečaja EdgeAI za začetnike boste:

### 🎯 **Temeljno znanje**
- Razumeli tehnične in poslovne dejavnike za sprejetje Edge AI
- Primerjali arhitekture Edge in oblačne AI ter njihove ustrezne primere uporabe
- Prepoznali značilnosti in zmogljivosti različnih družin SLM
- Analizirali zahteve strojne opreme za namestitev Edge AI

### 🛠️ **Tehnične veščine**
- Namestili SLM na različne platforme (Windows, mobilne naprave, vgrajene sisteme, hibrid oblak-rob)
- Optimizirali modele za robne omejitve z uporabo kvantizacije, obrezovanja in stiskanja
- Implementirali Edge AI aplikacije, pripravljene za produkcijo, z nadzorom in skaliranjem
- Zgradili sisteme z več agenti in okvire za klic funkcij za kompleksne delovne tokove

### 🏗️ **Praktična implementacija**
- Ustvarili aplikacije za klepet z lokalnim preklapljanjem modelov in upravljanjem pogovorov
- Razvili sisteme RAG (Retrieval-Augmented Generation) z lokalno obdelavo dokumentov
- Zgradili usmerjevalnike modelov, ki inteligentno izbirajo med specializiranimi AI modeli
- Oblikovali API okvire s pretokom, nadzorom zdravja in obravnavo napak

### 🚀 **Produkcijska namestitev**
- Vzpostavili SLMOps procese za različice modelov, testiranje in namestitev
- Implementirali najboljše prakse varnosti za aplikacije Edge AI
- Oblikovali skalabilne arhitekture, ki uravnotežijo obdelavo na robu in v oblaku
- Ustvarili strategije za nadzor in vzdrževanje produkcijskih sistemov Edge AI

## Rezultati učenja

Po zaključku tečaja boste opremljeni za:

### **Tehnično obvladovanje**
✅ **Namestitev produkcijsko pripravljenih Edge AI rešitev** na Windows, mobilne naprave in vgrajene platforme  
✅ **Optimizacijo AI modelov za robne omejitve** z doseganjem 75 % zmanjšanja velikosti ob ohranjanju 85 % zmogljivosti  
✅ **Izgradnjo inteligentnih sistemov agentov** s klicem funkcij in orkestracijo več modelov  
✅ **Oblikovanje skalabilnih hibridnih arhitektur rob-oblak** za poslovne aplikacije

### **Industrijske aplikacije**
✅ **Oblikovanje rešitev za proizvodnjo** za prediktivno vzdrževanje in nadzor kakovosti  
✅ **Razvoj zdravstvenih aplikacij** z obdelavo podatkov pacientov v skladu z zasebnostjo  
✅ **Izgradnjo avtomobilskih sistemov** za odločanje v realnem času in varnost  
✅ **Ustvarjanje infrastrukture pametnih mest** za promet, varnost in okoljsko spremljanje

### **Napredovanje v karieri**
✅ **Arhitekt rešitev EdgeAI**: Oblikovanje celovitih strategij Edge AI  
✅ **ML inženir (specializacija za rob)**: Optimizacija in namestitev modelov za robna okolja  
✅ **Razvijalec IoT AI**: Ustvarjanje inteligentnih IoT sistemov z lokalno obdelavo  
✅ **Razvijalec mobilne AI**: Gradnja AI-pogonjenih mobilnih aplikacij z lokalnim sklepanjem

## Arhitektura tečaja

Ta tečaj sledi **pristopu progresivnega obvladovanja**:

### **Faza 1: Temelji** (Moduli 01-02)
Razvijte konceptualno razumevanje in raziščite družine modelov

### **Faza 2: Implementacija** (Moduli 03-04) 
Obvladujte tehnike namestitve in optimizacije

### **Faza 3: Produkcija** (Moduli 05-06)
Naučite se SLMOps in naprednih okvirov agentov

### **Faza 4: Specializacija** (Moduli 07-08)
Implementacija, specifična za platformo, in celoviti primeri

## Merila uspeha

Sledite svojemu napredku s temi konkretnimi rezultati:

- **Projekti portfelja**: 10+ aplikacij, pripravljenih za produkcijo, ki pokrivajo več industrij
- **Merila zmogljivosti**: Modeli, ki delujejo z <500ms časom sklepanja na robnih napravah
- **Cilji namestitve**: Aplikacije, ki delujejo na Windows, mobilnih napravah in vgrajenih platformah
- **Pripravljenost za podjetja**: Rešitve z nadzorom, skaliranjem in varnostnimi okviri

## Začetek

Pripravljeni na preoblikovanje vašega razumevanja namestitve AI? Vaša pot se začne z **[Modulom 01: Osnove EdgeAI](./Module01/README.md)**, kjer boste raziskali tehnične temelje, ki omogočajo Edge AI, in preučili študije primerov iz resničnega sveta vodilnih v industriji.

**Naslednji korak**: [📚 Modul 01 - Osnove EdgeAI →](./Module01/README.md)

---

**Prihodnost AI je lokalna, takojšnja in zasebna. Obvladajte Edge AI, da ustvarite naslednjo generacijo inteligentnih aplikacij.**

---


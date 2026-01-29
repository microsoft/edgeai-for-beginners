# Poglavje 02: Osnove majhnih jezikovnih modelov

To temeljno poglavje ponuja celovit pregled majhnih jezikovnih modelov (SLM), ki zajema teoretične principe, praktične strategije implementacije in rešitve za produkcijsko uporabo. Poglavje vzpostavlja ključno bazo znanja za razumevanje sodobnih učinkovitih AI arhitektur in njihove strateške uporabe v različnih računalniških okoljih.

## Struktura poglavja in okvir progresivnega učenja

### **[Oddelek 1: Osnove družine modelov Microsoft Phi](./01.PhiFamily.md)**
Uvodni oddelek predstavlja revolucionarno družino modelov Phi podjetja Microsoft, ki prikazuje, kako kompaktni in učinkoviti modeli dosegajo izjemno zmogljivost ob znatno zmanjšanih računalniških zahtevah. Ta temeljni oddelek zajema:

- **Razvoj filozofije oblikovanja**: Celovit pregled razvoja družine Phi od Phi-1 do Phi-4, s poudarkom na revolucionarni metodologiji "učbenikovske kakovosti" pri učenju in skaliranju med sklepnim časom
- **Arhitektura z osredotočenostjo na učinkovitost**: Podrobna analiza optimizacije parametrov, zmogljivosti za večmodalno integracijo in optimizacije strojne opreme za CPU, GPU in naprave na robu
- **Specializirane zmogljivosti**: Poglobljen pregled različic, kot so Phi-4-mini-reasoning za matematične naloge, Phi-4-multimodal za obdelavo vizualno-jezikovnih podatkov in Phi-3-Silica za vgrajeno uporabo v Windows 11

Ta oddelek vzpostavlja temeljno načelo, da lahko učinkovitost modela in zmogljivost sobivata skozi inovativne metodologije učenja in optimizacijo arhitekture.

### **[Oddelek 2: Osnove družine Qwen](./02.QwenFamily.md)**
Drugi oddelek prehaja na celovit odprtokodni pristop podjetja Alibaba, ki prikazuje, kako transparentni in dostopni modeli lahko dosežejo konkurenčno zmogljivost ob ohranjanju prilagodljivosti pri uporabi. Ključna področja vključujejo:

- **Odličnost odprte kode**: Celovit pregled razvoja Qwen od Qwen 1.0 do Qwen3, s poudarkom na obsežnem učenju (36 bilijonov tokenov) in večjezičnih zmogljivostih v 119 jezikih
- **Napredna arhitektura sklepanja**: Podrobna obravnava inovativnih zmogljivosti "načina razmišljanja" pri Qwen3, implementacij mešanice strokovnjakov in specializiranih različic za kodiranje (Qwen-Coder) ter matematiko (Qwen-Math)
- **Prilagodljive možnosti uporabe**: Poglobljena analiza razpona parametrov od 0,5B do 235B, ki omogoča scenarije uporabe od mobilnih naprav do poslovnih grozdov

Ta oddelek poudarja demokratizacijo AI tehnologije skozi dostopnost odprte kode ob ohranjanju konkurenčnih zmogljivostnih značilnosti.

### **[Oddelek 3: Osnove družine Gemma](./03.GemmaFamily.md)**
Tretji oddelek raziskuje celovit pristop Googla k odprtokodnemu večmodalnemu AI, ki prikazuje, kako razvoj, ki temelji na raziskavah, lahko zagotovi dostopne, a zmogljive AI zmogljivosti. Ta oddelek zajema:

- **Inovacije, ki temeljijo na raziskavah**: Celovit pregled arhitektur Gemma 3 in Gemma 3n, ki vključujejo prebojno tehnologijo Per-Layer Embeddings (PLE) in strategije optimizacije za mobilne naprave
- **Večmodalna odličnost**: Podrobna obravnava integracije vizualno-jezikovnih podatkov, zmogljivosti obdelave zvoka in funkcij klicanja, ki omogočajo celovite AI izkušnje
- **Arhitektura, osredotočena na mobilne naprave**: Poglobljena analiza revolucionarnih dosežkov učinkovitosti pri Gemma 3n, ki zagotavlja zmogljivost 2B-4B parametrov z minimalno porabo pomnilnika (2-3GB)

Ta oddelek prikazuje, kako je mogoče vrhunske raziskave prevesti v praktične, dostopne AI rešitve, ki omogočajo nove kategorije aplikacij.

### **[Oddelek 4: Osnove družine BitNET](./04.BitNETFamily.md)**
Četrti oddelek predstavlja revolucionarni pristop Microsofta k 1-bitni kvantizaciji, ki predstavlja mejnik ultra-učinkovite uporabe AI. Ta napredni oddelek zajema:

- **Revolucionarna kvantizacija**: Celovit pregled 1,58-bitne kvantizacije z uporabo ternarnih uteži {-1, 0, +1}, ki dosega 1,37x do 6,17x pospeške z 55-82% zmanjšanjem porabe energije
- **Optimiziran okvir sklepanja**: Podrobna obravnava implementacije bitnet.cpp iz [https://github.com/microsoft/BitNet](https://github.com/microsoft/BitNet), specializiranih jeder in optimizacij za različne platforme, ki zagotavljajo izjemne dobičke v učinkovitosti
- **Trajnostno vodstvo AI**: Poglobljena analiza okoljskih koristi, demokratiziranih zmogljivosti uporabe in novih scenarijev aplikacij, ki jih omogoča ekstremna učinkovitost

Ta oddelek prikazuje, kako lahko revolucionarne tehnike kvantizacije dramatično izboljšajo učinkovitost AI ob ohranjanju konkurenčne zmogljivosti.

### **[Oddelek 5: Osnove modela Microsoft Mu](./05.mumodel.md)**
Peti oddelek raziskuje revolucionarni model Mu podjetja Microsoft, zasnovan posebej za uporabo na napravah z operacijskim sistemom Windows. Ta specializirani oddelek zajema:

- **Arhitektura, osredotočena na naprave**: Celovit pregled specializiranega modela na napravi, vgrajenega v naprave z operacijskim sistemom Windows 11
- **Integracija sistema**: Podrobna analiza globoke integracije z Windows 11, ki prikazuje, kako lahko AI izboljša funkcionalnost sistema skozi nativno implementacijo
- **Oblikovanje, ki ohranja zasebnost**: Poglobljena obravnava delovanja brez povezave, lokalne obdelave in arhitekture, ki daje prednost zasebnosti in ohranja uporabniške podatke na napravi

Ta oddelek prikazuje, kako lahko specializirani modeli izboljšajo funkcionalnost operacijskega sistema Windows 11 ob ohranjanju zasebnosti in zmogljivosti.

### **[Oddelek 6: Osnove Phi-Silica](./06.phisilica.md)**
Zaključni oddelek preučuje Microsoftov Phi-Silica, ultra-učinkovit jezikovni model, vgrajen v Windows 11 za Copilot+ PC-je z NPU strojno opremo. Ta napredni oddelek zajema:

- **Izjemne metrične učinkovitosti**: Celovita analiza izjemnih zmogljivosti Phi-Silica, ki zagotavlja 650 tokenov na sekundo z le 1,5 W porabe energije
- **Optimizacija NPU**: Podrobna obravnava specializirane arhitekture, zasnovane za nevronske procesne enote v Windows 11 Copilot+ PC-jih
- **Integracija za razvijalce**: Poglobljena obravnava integracije z Windows App SDK, tehnik oblikovanja pozivov in najboljših praks za implementacijo Phi-Silica v aplikacijah za Windows 11

Ta oddelek vzpostavlja vrhunsko tehnologijo strojno optimiziranih jezikovnih modelov na napravi, ki prikazuje, kako lahko specializirane arhitekture modelov v kombinaciji z namensko nevronsko strojno opremo zagotovijo izjemno zmogljivost AI na potrošniških napravah z operacijskim sistemom Windows 11.

## Celoviti učni cilji

Po zaključku tega temeljnega poglavja bodo bralci dosegli mojstrstvo v:

1. **Razumevanju arhitekture**: Globoko razumevanje različnih filozofij oblikovanja SLM in njihovih implikacij za scenarije uporabe
2. **Ravnovesju med zmogljivostjo in učinkovitostjo**: Strateške sposobnosti odločanja pri izbiri ustreznih arhitektur modelov glede na računalniške omejitve in zahteve zmogljivosti
3. **Prilagodljivosti uporabe**: Razumevanje kompromisov med lastniško optimizacijo (Phi), dostopnostjo odprte kode (Qwen), inovacijami, ki temeljijo na raziskavah (Gemma), in revolucionarno učinkovitostjo (BitNET)
4. **Perspektivi za prihodnost**: Vpogledi v nastajajoče trende v učinkovitih AI arhitekturah in njihove implikacije za strategije uporabe naslednje generacije

## Osredotočenost na praktično implementacijo

Poglavje ohranja močno praktično usmerjenost skozi:

- **Popolne primerke kode**: Primeri implementacije, pripravljeni za produkcijo, za vsako družino modelov, vključno s postopki prilagajanja, strategijami optimizacije in konfiguracijami uporabe
- **Celovito primerjanje zmogljivosti**: Podrobne primerjave zmogljivosti med različnimi arhitekturami modelov, vključno z metričnimi učinkovitosti, ocenami zmogljivosti in optimizacijo za primere uporabe
- **Varnost v podjetjih**: Implementacije varnosti na ravni produkcije, strategije spremljanja in najboljše prakse za zanesljivo uporabo
- **Integracija okvirjev**: Praktična navodila za integracijo s priljubljenimi okvirji, vključno s Hugging Face Transformers, vLLM, ONNX Runtime in specializiranimi orodji za optimizacijo

## Strateški tehnološki načrt

Poglavje se zaključi z analizo usmerjeno v prihodnost:

- **Evolucija arhitekture**: Nastajajoči trendi v oblikovanju in optimizaciji učinkovitih modelov
- **Integracija strojne opreme**: Napredki v specializiranih AI pospeševalnikih in njihov vpliv na strategije uporabe
- **Razvoj ekosistema**: Prizadevanja za standardizacijo in izboljšanje interoperabilnosti med različnimi družinami modelov
- **Poslovna uporaba**: Strateški vidiki načrtovanja uporabe AI v organizacijah

## Scenariji uporabe v resničnem svetu

Vsak oddelek ponuja celovit pregled praktičnih aplikacij:

- **Mobilno in robno računalništvo**: Optimizirane strategije uporabe za okolja z omejenimi viri
- **Poslovne aplikacije**: Prilagodljive rešitve za poslovno inteligenco, avtomatizacijo in storitve za stranke
- **Izobraževalna tehnologija**: Dostopen AI za personalizirano učenje in generiranje vsebin
- **Globalna uporaba**: Večjezične in medkulturne AI aplikacije

## Standardi tehnične odličnosti

Poglavje poudarja implementacijo, pripravljeno za produkcijo, skozi:

- **Mojstrstvo optimizacije**: Napredne tehnike kvantizacije, optimizacije sklepanja in upravljanja virov
- **Spremljanje zmogljivosti**: Celovito zbiranje metrik, sistemi opozarjanja in analitika zmogljivosti
- **Implementacija varnosti**: Varnostni ukrepi na ravni podjetja, zaščita zasebnosti in okvirji skladnosti
- **Načrtovanje skalabilnosti**: Strategije horizontalnega in vertikalnega skaliranja za naraščajoče računalniške zahteve

To temeljno poglavje služi kot bistvena predpostavka za napredne strategije uporabe SLM, vzpostavlja tako teoretično razumevanje kot praktične sposobnosti, potrebne za uspešno implementacijo. Celovita obravnava zagotavlja, da so bralci dobro opremljeni za sprejemanje informiranih odločitev o arhitekturi in implementacijo robustnih, učinkovitih AI rešitev, ki ustrezajo njihovim specifičnim organizacijskim zahtevam, hkrati pa se pripravljajo na prihodnji tehnološki razvoj.

Poglavje premošča vrzel med vrhunskimi AI raziskavami in praktičnimi realnostmi uporabe, poudarja, da lahko sodobne SLM arhitekture zagotavljajo izjemno zmogljivost ob ohranjanju operativne učinkovitosti, stroškovne učinkovitosti in okoljske trajnosti.

---

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za prevajanje z umetno inteligenco [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne prevzemamo odgovornosti za morebitne nesporazume ali napačne razlage, ki bi nastale zaradi uporabe tega prevoda.
# Poglavje 03: Uvajanje malih jezikovnih modelov (SLM)

To poglobljeno poglavje raziskuje celoten življenjski cikel uvajanja malih jezikovnih modelov (SLM), vključno s teoretičnimi osnovami, praktičnimi strategijami implementacije in rešitvami za produkcijsko uporabo v obliki kontejnerjev. Poglavje je strukturirano v tri progresivne dele, ki bralce vodijo od osnovnih konceptov do naprednih scenarijev uvajanja.

## Struktura poglavja in učna pot

### **[Del 1: Napredno učenje SLM - Osnove in optimizacija](./01.SLMAdvancedLearning.md)**
Uvodni del postavlja teoretične temelje za razumevanje malih jezikovnih modelov in njihove strateške pomembnosti pri uvajanju umetne inteligence na robu. Ta del obravnava:

- **Okvir za klasifikacijo parametrov**: Podroben pregled kategorij SLM, od mikro SLM-jev (100M-1,4B parametrov) do srednjih SLM-jev (14B-30B parametrov), s posebnim poudarkom na modelih, kot so Phi-4-mini-3.8B, serija Qwen3 in Google Gemma3, vključno z analizo strojne opreme in pomnilniških zahtev za posamezne nivoje modelov
- **Napredne tehnike optimizacije**: Celovita obravnava metod kvantizacije z uporabo Llama.cpp, Microsoft Olive in Apple MLX okvirov, vključno z najsodobnejšo BitNET 1-bitno kvantizacijo s praktičnimi primeri kode, ki prikazujejo kvantizacijske procese in rezultate primerjalnih testov
- **Strategije pridobivanja modelov**: Poglobljena analiza ekosistema Hugging Face in kataloga modelov Azure AI Foundry za uvajanje SLM-jev na ravni podjetij, s primeri kode za programatsko prenašanje, validacijo in pretvorbo formatov modelov
- **API-ji za razvijalce**: Primeri kode v Pythonu, C++ in C#, ki prikazujejo nalaganje modelov, izvajanje sklepanja in integracijo s priljubljenimi okviri, kot so PyTorch, TensorFlow in ONNX Runtime

Ta osnovni del poudarja ravnovesje med operativno učinkovitostjo, prilagodljivostjo uvajanja in stroškovno učinkovitostjo, zaradi česar so SLM-ji idealni za scenarije računalništva na robu, s praktičnimi primeri kode, ki jih razvijalci lahko neposredno uporabijo v svojih projektih.

### **[Del 2: Uvajanje v lokalnem okolju - Rešitve, ki dajejo prednost zasebnosti](./02.DeployingSLMinLocalEnv.md)**
Drugi del prehaja od teorije k praktični implementaciji, osredotočajoč se na strategije lokalnega uvajanja, ki dajejo prednost suverenosti podatkov in operativni neodvisnosti. Ključna področja vključujejo:

- **Ollama univerzalna platforma**: Celovita obravnava uvajanja na več platformah s poudarkom na delovnih procesih, prijaznih do razvijalcev, upravljanju življenjskega cikla modelov in prilagoditvi prek Modelfiles, vključno s popolnimi primeri integracije REST API-jev in skriptami za avtomatizacijo CLI
- **Microsoft Foundry Local**: Rešitve za uvajanje na ravni podjetij z optimizacijo na osnovi ONNX, integracijo Windows ML in celovitimi varnostnimi funkcijami, s primeri kode v C# in Pythonu za integracijo v domače aplikacije
- **Primerjalna analiza**: Podroben primerjalni pregled tehnične arhitekture, značilnosti zmogljivosti in smernic za optimizacijo uporabe, s kodo za primerjalne teste za ocenjevanje hitrosti sklepanja in porabe pomnilnika na različni strojni opremi
- **Integracija API-jev**: Primeri aplikacij, ki prikazujejo, kako zgraditi spletne storitve, klepetalne aplikacije in podatkovne procesne tokove z uporabo lokalnih SLM-jev, s primeri kode v Node.js, Python Flask/FastAPI in ASP.NET Core
- **Okviri za testiranje**: Pristopi avtomatiziranega testiranja za zagotavljanje kakovosti modelov, vključno s primeri enotnih in integracijskih testov za implementacije SLM-jev

Ta del ponuja praktične smernice za organizacije, ki želijo implementirati rešitve umetne inteligence, ki ohranjajo zasebnost, hkrati pa ohranjajo popoln nadzor nad svojim okoljem uvajanja, s pripravljenimi primeri kode, ki jih razvijalci lahko prilagodijo svojim specifičnim zahtevam.

### **[Del 3: Uvajanje v oblaku s kontejnerji - Rešitve za produkcijsko uporabo](./03.DeployingSLMinCloud.md)**
Zadnji del se osredotoča na napredne strategije uvajanja s kontejnerji, pri čemer je Microsoftov Phi-4-mini-instruct glavni študijski primer. Ta del obravnava:

- **vLLM uvajanje**: Optimizacija sklepanja z visokimi zmogljivostmi z OpenAI-kompatibilnimi API-ji, napredno GPU pospešitvijo in konfiguracijo za produkcijsko uporabo, vključno s popolnimi Dockerfile-i, Kubernetes manifesti in parametri za optimizacijo zmogljivosti
- **Ollama orkestracija kontejnerjev**: Poenostavljeni delovni procesi uvajanja z Docker Compose, različicami optimizacije modelov in integracijo spletnega uporabniškega vmesnika, s primeri CI/CD procesov za avtomatizirano uvajanje in testiranje
- **Implementacija ONNX Runtime**: Optimizirano uvajanje na robu z obsežno pretvorbo modelov, strategijami kvantizacije in združljivostjo med platformami, vključno s podrobnimi primeri kode za optimizacijo in uvajanje modelov
- **Nadzor in opazovanje**: Implementacija nadzornih plošč Prometheus/Grafana s prilagojenimi metrikami za spremljanje zmogljivosti SLM-jev, vključno s konfiguracijami za opozarjanje in združevanje dnevnikov
- **Uravnavanje obremenitve in skaliranje**: Praktični primeri strategij horizontalnega in vertikalnega skaliranja z avtomatskimi konfiguracijami skaliranja na podlagi uporabe CPU/GPU in vzorcev zahtev
- **Krepitev varnosti**: Najboljše prakse za varnost kontejnerjev, vključno z zmanjšanjem privilegijev, omrežnimi politikami in upravljanjem skrivnosti za API ključe in dostopne poverilnice modelov

Vsak pristop k uvajanju je predstavljen s popolnimi primeri konfiguracij, postopki testiranja, kontrolnimi seznami za pripravljenost na produkcijo in predlogami infrastrukture kot kode, ki jih razvijalci lahko neposredno uporabijo v svojih delovnih procesih uvajanja.

## Ključni učni cilji

Z zaključkom tega poglavja bodo bralci obvladali:

1. **Strateško izbiro modelov**: Razumevanje meja parametrov in izbira ustreznih SLM-jev glede na omejitve virov in zahteve zmogljivosti
2. **Obvladovanje optimizacije**: Implementacija naprednih tehnik kvantizacije v različnih okvirih za doseganje optimalnega ravnovesja med zmogljivostjo in učinkovitostjo
3. **Prilagodljivost uvajanja**: Izbira med lokalnimi rešitvami, osredotočenimi na zasebnost, in skalabilnimi uvajanji s kontejnerji glede na potrebe organizacije
4. **Pripravljenost na produkcijo**: Konfiguracija sistemov za nadzor, varnost in skaliranje za uvajanje SLM-jev na ravni podjetij

## Praktična usmerjenost in aplikacije v resničnem svetu

Poglavje ohranja močno praktično usmerjenost skozi celotno vsebino, vključno z:

- **Praktični primeri**: Popolne konfiguracijske datoteke, postopki testiranja API-jev in skripti za uvajanje
- **Primerjalni testi zmogljivosti**: Podrobne primerjave hitrosti sklepanja, porabe pomnilnika in zahtev po virih
- **Varnostni vidiki**: Prakse varnosti na ravni podjetij, okviri skladnosti in strategije zaščite podatkov
- **Najboljše prakse**: Smernice, preizkušene v produkciji, za nadzor, skaliranje in vzdrževanje

## Perspektiva prihodnosti

Poglavje se zaključi z vpogledi v nastajajoče trende, vključno z:

- Napredne arhitekture modelov z izboljšanimi razmerji učinkovitosti
- Globlja integracija strojne opreme s specializiranimi AI pospeševalniki
- Evolucija ekosistema proti standardizaciji in interoperabilnosti
- Vzorci sprejemanja na ravni podjetij, ki jih vodijo zahteve po zasebnosti in skladnosti

Ta celovit pristop zagotavlja, da so bralci dobro opremljeni za navigacijo tako trenutnih izzivov uvajanja SLM-jev kot prihodnjih tehnoloških razvojnih smernic, sprejemanje informiranih odločitev, ki so skladne z njihovimi specifičnimi organizacijskimi zahtevami in omejitvami.

Poglavje služi kot praktični vodnik za takojšnjo implementacijo in strateški vir za dolgoročno načrtovanje uvajanja umetne inteligence, pri čemer poudarja kritično ravnovesje med zmogljivostjo, učinkovitostjo in operativno odličnostjo, ki opredeljuje uspešno uvajanje SLM-jev.

---

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za prevajanje z umetno inteligenco [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne prevzemamo odgovornosti za morebitna nesporazumevanja ali napačne razlage, ki bi nastale zaradi uporabe tega prevoda.
# Poglavje 06: Sistemi SLM Agentic: Celovit Pregled

Pokrajina umetne inteligence doživlja temeljno preobrazbo, saj prehajamo od preprostih klepetalnih robotov k naprednim AI agentom, ki jih poganjajo Mali Jezikovni Modeli (SLM). Ta celovit vodnik raziskuje tri ključne vidike sodobnih agentnih sistemov SLM: osnovne koncepte in strategije uvajanja, zmožnosti klicanja funkcij ter revolucionarno integracijo Model Context Protocol (MCP).

## [Oddelek 1: Temelji AI Agentov in Malih Jezikovnih Modelov](./01.IntroduceAgent.md)

Prvi oddelek vzpostavlja osnovno razumevanje AI agentov in Malih Jezikovnih Modelov ter postavlja leto 2025 kot leto AI agentov, ki sledi obdobju klepetalnih robotov leta 2023 in razcvetu kopilotov leta 2024. Ta oddelek uvaja **agentne AI sisteme**, ki razmišljajo, načrtujejo, uporabljajo orodja in izvajajo naloge z minimalnim človeškim vnosom.

### Ključni koncepti:
- **Okvir za klasifikacijo agentov**: Od preprostih refleksnih agentov do učnih agentov, ki zagotavljajo celovito taksonomijo za različne računalniške scenarije
- **Osnove SLM**: Definicija Malih Jezikovnih Modelov kot modelov z manj kot 10 milijardami parametrov, ki lahko izvajajo praktične sklepe na potrošniških napravah
- **Napredne strategije optimizacije**: Pokrivanje uvajanja v formatu GGUF, tehnike kvantizacije (Q4_K_M, Q5_K_S, Q8_0) in okvirji, optimizirani za rob, kot sta Llama.cpp in Apple MLX
- **Kompromisi med SLM in LLM**: Prikaz 10-30× zmanjšanja stroškov z uporabo SLM-jev ob ohranjanju učinkovitosti za 70-80 % tipičnih nalog agentov

Oddelek se zaključi s praktičnimi strategijami uvajanja z uporabo Ollama, VLLM in Microsoftovih rešitev za rob, ki vzpostavljajo SLM-je kot prihodnost stroškovno učinkovite, zasebnost ohranjajoče agentne AI uvajanja.

## [Oddelek 2: Klicanje funkcij v Malih Jezikovnih Modelih](./02.FunctionCalling.md)

Drugi oddelek se poglobi v **zmožnosti klicanja funkcij**, mehanizem, ki statične jezikovne modele spreminja v dinamične AI agente, sposobne interakcije v resničnem svetu. Ta tehnični pregled pokriva celoten potek dela od zaznavanja namena do integracije odziva.

### Ključna področja implementacije:
- **Sistematičen potek dela**: Podroben pregled integracije orodij, definicije funkcij, zaznavanja namena, generiranja JSON izhodov in zunanje izvedbe
- **Implementacije specifične za platformo**: Celoviti vodiči za Phi-4-mini z Ollama, Qwen3 klicanje funkcij in integracijo Microsoft Foundry Local
- **Napredni primeri**: Sistemi za sodelovanje med več agenti, dinamična izbira orodij in vzorci integracije v podjetjih z obsežnim obravnavanjem napak
- **Produkcijski vidiki**: Omejevanje hitrosti, beleženje revizij, varnostni ukrepi in strategije optimizacije zmogljivosti

Ta oddelek ponuja tako teoretično razumevanje kot praktične vzorce implementacije, ki razvijalcem omogočajo gradnjo robustnih sistemov za klicanje funkcij, ki lahko obvladajo vse od preprostih API klicev do kompleksnih večstopenjskih delovnih tokov v podjetjih.

## [Oddelek 3: Integracija Model Context Protocol (MCP)](./03.IntroduceMCP.md)

Zadnji oddelek uvaja **Model Context Protocol (MCP)**, revolucionarni okvir, ki standardizira način interakcije jezikovnih modelov z zunanjimi orodji in sistemi. Ta oddelek prikazuje, kako MCP ustvarja most med AI modeli in resničnim svetom prek dobro definiranih protokolov.

### Poudarki integracije:
- **Arhitektura protokola**: Plastni dizajn sistema, ki pokriva aplikacijo, LLM odjemalca, MCP odjemalca in plasti za obdelavo orodij
- **Podpora za več zaledij**: Prilagodljiva implementacija, ki podpira tako Ollama (lokalni razvoj) kot vLLM (produkcija) zaledja
- **Povezovalni protokoli**: STDIO način za neposredno komunikacijo procesov in SSE način za pretakanje prek HTTP
- **Resnične aplikacije**: Primeri avtomatizacije spletnih strani, obdelave podatkov in integracije API-jev z obsežnim obravnavanjem napak

Integracija MCP prikazuje, kako je mogoče SLM-je nadgraditi z zunanjimi zmožnostmi, s čimer se kompenzira njihovo manjše število parametrov, hkrati pa se ohranjajo prednosti lokalne uvedbe in učinkovitosti virov.

## Strateške implikacije

Skupaj ti trije oddelki predstavljajo celovit okvir za razumevanje in implementacijo agentnih sistemov SLM. Evolucija od osnovnih konceptov prek klicanja funkcij do integracije MCP prikazuje jasno pot proti demokratizirani uvedbi AI, kjer:

- **Učinkovitost se sreča z zmogljivostjo** prek optimiziranih malih modelov
- **Stroškovna učinkovitost** omogoča široko sprejetje
- **Standardizirani protokoli** zagotavljajo interoperabilnost
- **Lokalna uvedba** ohranja zasebnost in zmanjšuje zakasnitve

Ta napredek predstavlja ne le tehnološki razvoj, temveč tudi premik paradigme proti bolj dostopnim, učinkovitim in praktičnim AI sistemom, ki lahko učinkovito delujejo v okolju z omejenimi viri, hkrati pa zagotavljajo napredne agentne zmožnosti.

Kombinacija SLM-jev z naprednimi strategijami uvajanja, robustnim klicanjem funkcij in standardiziranimi protokoli za integracijo orodij postavlja te sisteme kot temelj za naslednjo generacijo AI agentov, ki bodo preoblikovali način interakcije z umetno inteligenco in koristi, ki jih prinaša, v različnih industrijah in aplikacijah.

---

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za prevajanje z umetno inteligenco [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne prevzemamo odgovornosti za morebitna nesporazumevanja ali napačne razlage, ki bi nastale zaradi uporabe tega prevoda.
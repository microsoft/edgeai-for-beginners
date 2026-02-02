# Modul 08 Vzorci: Vodnik za lokalni razvoj Foundry

## Pregled

Ta obsežna zbirka prikazuje tako pristop **Foundry Local SDK** kot **Shell Command** za gradnjo produkcijsko pripravljenih AI aplikacij. Vsak vzorec poudarja različne vidike razvoja AI na robu, od osnovne REST integracije do naprednih sistemov z več agenti.

## Pristop k razvoju: SDK proti Shell Command

### Uporabite Foundry Local SDK, kadar:

- **Programska kontrola**: Potrebujete popoln nadzor nad življenjskim ciklom agenta, evalvacijami ali delovnimi tokovi za uvajanje
- **Prilagojeno orodje**: Gradnja avtomatizacije okoli Foundry Local (integracija CI/CD, orkestracija več agentov)
- **Podroben dostop**: Zahtevate podrobne metapodatke agenta, verzioniranje ali nadzor evalvacijskega izvajalca
- **Integracija s Pythonom**: Delo v okolju, ki temelji na Pythonu, ali vključevanje logike Foundry v širše aplikacije
- **Delovni tokovi za podjetja**: Uvajanje modularnih delovnih tokov in ponovljivih evalvacijskih procesov, usklajenih z referenčnimi arhitekturami Microsofta

### Uporabite Shell Commands, kadar:

- **Hitro testiranje**: Izvajanje hitrih lokalnih testov, ročno zaganjanje agentov ali preverjanje nastavitev
- **Preprostost CLI**: Potrebujete enostavne CLI operacije za zagon/ustavitev agentov, preverjanje dnevnikov ali osnovne evalvacije
- **Lahka avtomatizacija**: Pisanje preprostih skriptov za avtomatizacijo brez zahtev po popolni integraciji SDK
- **Hitre iteracije**: Razhroščevanje in razvojni cikli, zlasti v omejenih okoljih ali na ravni skupin virov
- **Nastavitev in preverjanje**: Začetna konfiguracija okolja in hitre naloge preverjanja

## Najboljše prakse in priporočeni delovni tok

Na podlagi upravljanja življenjskega cikla agenta, sledenja odvisnostim in načel reproducibilnosti z najmanjšimi privilegiji:

### Faza 1: Osnove in nastavitev
1. **Začnite z ukazi Shell** za začetno nastavitev in hitro preverjanje
2. **Preverite okolje** z uporabo CLI orodij in osnovne uvedbe modela
3. **Preizkusite povezljivost** z enostavnimi REST klici in preverjanjem stanja

### Faza 2: Razvoj in integracija
1. **Prehod na SDK** za skalabilne in sledljive delovne tokove
2. **Uvedite programsko kontrolo** za kompleksne interakcije med agenti
3. **Zgradite prilagojena orodja** za predloge, pripravljene za skupnost, in integracijo Azure OpenAI

### Faza 3: Produkcija in razširitev
1. **Hibridni pristop** z združevanjem CLI za operacije in SDK za logiko aplikacij
2. **Integracija v podjetju** z nadzorom, beleženjem in uvajalnimi procesi
3. **Prispevek skupnosti** z uporabo predlog in najboljših praks

---

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve AI za prevajanje [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne prevzemamo odgovornosti za morebitna nesporazumevanja ali napačne razlage, ki izhajajo iz uporabe tega prevoda.
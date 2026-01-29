# Modul 08 Primjeri: Vodič za lokalni razvoj Foundryja

## Pregled

Ova sveobuhvatna zbirka prikazuje pristupe **Foundry Local SDK** i **Shell Command** za izradu AI aplikacija spremnih za produkciju. Svaki primjer ističe različite aspekte razvoja AI-a na rubu, od osnovne REST integracije do naprednih sustava s više agenata.

## Pristup razvoju: SDK vs Shell naredbe

### Koristite Foundry Local SDK kada:

- **Programska kontrola**: Trebate potpunu kontrolu nad životnim ciklusom agenta, evaluacijom ili radnim tijekovima implementacije
- **Prilagođeni alati**: Izrada automatizacije oko Foundry Local (integracija CI/CD, orkestracija više agenata)
- **Detaljan pristup**: Potrebni su vam detaljni metapodaci agenta, verzioniranje ili kontrola evaluacijskog pokretača
- **Python integracija**: Radite u okruženjima koja se oslanjaju na Python ili ugrađujete Foundry logiku u šire aplikacije
- **Poslovni radni tijekovi**: Implementacija modularnih radnih tijekova i ponovljivih evaluacijskih procesa usklađenih s Microsoftovim referentnim arhitekturama

### Koristite Shell naredbe kada:

- **Brzo testiranje**: Izvodite brzo lokalno testiranje, ručno pokretanje agenata ili provjeru postavki
- **Jednostavnost CLI-a**: Trebate jednostavne CLI operacije za pokretanje/zaustavljanje agenata, provjeru logova ili osnovne evaluacije
- **Lagano automatiziranje**: Skriptiranje jednostavne automatizacije bez potrebe za potpunom integracijom SDK-a
- **Brza iteracija**: Ciklusi otklanjanja grešaka i razvoja, posebno u ograničenim okruženjima ili implementacijama na razini grupa resursa
- **Postavljanje i validacija**: Početna konfiguracija okruženja i brzi zadaci provjere

## Najbolje prakse i preporučeni radni tijek

Na temelju upravljanja životnim ciklusom agenta, praćenja ovisnosti i principa reproducibilnosti s najmanjim privilegijama:

### Faza 1: Osnove i postavljanje
1. **Započnite s Shell naredbama** za početno postavljanje i brzu validaciju
2. **Provjerite okruženje** koristeći CLI alate i osnovnu implementaciju modela
3. **Testirajte povezivost** jednostavnim REST pozivima i provjerama stanja

### Faza 2: Razvoj i integracija
1. **Prijelaz na SDK** za skalabilne i sljedive radne tijekove
2. **Implementirajte programsku kontrolu** za složene interakcije agenata
3. **Izradite prilagođene alate** za predloške spremne za zajednicu i integraciju s Azure OpenAI

### Faza 3: Produkcija i skaliranje
1. **Hibridni pristup** kombinirajući CLI za operacije i SDK za logiku aplikacije
2. **Poslovna integracija** s praćenjem, logiranjem i implementacijskim tijekovima
3. **Doprinos zajednici** kroz ponovno upotrebljive predloške i najbolje prakse

---

**Izjava o odricanju odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane ljudskog prevoditelja. Ne preuzimamo odgovornost za nesporazume ili pogrešna tumačenja koja mogu proizaći iz korištenja ovog prijevoda.
# Poglavlje 06: SLM Agentni Sustavi: Sveobuhvatan Pregled

Krajolik umjetne inteligencije prolazi kroz temeljnu transformaciju dok prelazimo od jednostavnih chatbotova do sofisticiranih AI agenata koje pokreću Mali Jezični Modeli (SLM). Ovaj sveobuhvatan vodič istražuje tri ključna aspekta modernih SLM agentnih sustava: temeljne koncepte i strategije implementacije, mogućnosti pozivanja funkcija te revolucionarnu integraciju Model Context Protocol (MCP).

## [Odjeljak 1: Temelji AI Agenata i Malih Jezičnih Modela](./01.IntroduceAgent.md)

Prvi odjeljak uspostavlja temeljno razumijevanje AI agenata i Malih Jezičnih Modela, pozicionirajući 2025. godinu kao godinu AI agenata nakon ere chatbotova u 2023. i ekspanzije kopilota u 2024. Ovaj odjeljak uvodi **agentne AI sustave** koji razmišljaju, zaključuju, planiraju, koriste alate i izvršavaju zadatke uz minimalan ljudski unos.

### Ključni Koncepti:
- **Okvir za Klasifikaciju Agenata**: Od jednostavnih refleksnih agenata do agenata koji uče, pružajući sveobuhvatnu taksonomiju za različite računalne scenarije
- **Osnove SLM-a**: Definiranje Malih Jezičnih Modela kao modela s manje od 10 milijardi parametara koji mogu obavljati praktične inferencije na potrošačkim uređajima
- **Napredne Strategije Optimizacije**: Pokrivanje implementacije u GGUF formatu, tehnike kvantizacije (Q4_K_M, Q5_K_S, Q8_0) i okviri optimizirani za rubne uređaje poput Llama.cpp i Apple MLX
- **SLM vs LLM Kompromisi**: Prikazivanje smanjenja troškova od 10-30× uz SLM-ove, uz održavanje učinkovitosti za 70-80% tipičnih zadataka agenata

Odjeljak završava praktičnim strategijama implementacije koristeći Ollama, VLLM i Microsoftova rješenja za rubne uređaje, uspostavljajući SLM-ove kao budućnost ekonomične i privatne implementacije agentne AI.

## [Odjeljak 2: Pozivanje Funkcija u Malim Jezičnim Modelima](./02.FunctionCalling.md)

Drugi odjeljak detaljno istražuje **mogućnosti pozivanja funkcija**, mehanizam koji statične jezične modele pretvara u dinamične AI agente sposobne za interakciju u stvarnom svijetu. Ovaj tehnički pregled pokriva cjelokupan tijek rada od detekcije namjere do integracije odgovora.

### Ključna Područja Implementacije:
- **Sustavni Tijek Rada**: Detaljno istraživanje integracije alata, definicije funkcija, detekcije namjere, generiranja JSON izlaza i vanjskog izvršavanja
- **Implementacije Specifične za Platformu**: Sveobuhvatni vodiči za Phi-4-mini s Ollama, Qwen3 pozivanje funkcija i Microsoft Foundry Local integraciju
- **Napredni Primjeri**: Sustavi za suradnju više agenata, dinamički odabir alata i obrasci integracije u poduzećima s detaljnim rukovanjem greškama
- **Razmatranja za Produkciju**: Ograničavanje brzine, zapisivanje revizija, sigurnosne mjere i strategije optimizacije performansi

Ovaj odjeljak pruža i teorijsko razumijevanje i praktične obrasce implementacije, omogućujući programerima izgradnju robusnih sustava za pozivanje funkcija koji mogu obraditi sve, od jednostavnih API poziva do složenih višestupanjskih radnih tijekova u poduzećima.

## [Odjeljak 3: Integracija Model Context Protocol (MCP)](./03.IntroduceMCP.md)

Završni odjeljak uvodi **Model Context Protocol (MCP)**, revolucionarni okvir koji standardizira način na koji jezični modeli komuniciraju s vanjskim alatima i sustavima. Ovaj odjeljak pokazuje kako MCP stvara most između AI modela i stvarnog svijeta kroz dobro definirane protokole.

### Istaknute Integracije:
- **Arhitektura Protokola**: Slojeviti dizajn sustava koji pokriva aplikacijski sloj, LLM klijent, MCP klijent i sloj obrade alata
- **Podrška za Više Pozadinskih Sustava**: Fleksibilna implementacija koja podržava Ollama (lokalni razvoj) i vLLM (produkcijski) pozadinske sustave
- **Protokoli Povezivanja**: STDIO način za direktnu komunikaciju procesa i SSE način za HTTP streaming
- **Primjene u Stvarnom Svijetu**: Automatizacija weba, obrada podataka i primjeri integracije API-ja s detaljnim rukovanjem greškama

Integracija MCP-a pokazuje kako se SLM-ovi mogu nadograditi vanjskim mogućnostima, nadoknađujući manji broj parametara kroz poboljšanu funkcionalnost uz održavanje prednosti lokalne implementacije i učinkovitosti resursa.

## Strateške Implikacije

Zajedno, ova tri odjeljka predstavljaju sveobuhvatan okvir za razumijevanje i implementaciju SLM agentnih sustava. Evolucija od temeljnih koncepata preko pozivanja funkcija do MCP integracije pokazuje jasan put prema demokratiziranoj implementaciji AI-a gdje:

- **Učinkovitost susreće sposobnost** kroz optimizirane male modele
- **Ekonomičnost** omogućuje široku primjenu
- **Standardizirani protokoli** osiguravaju interoperabilnost
- **Lokalna implementacija** čuva privatnost i smanjuje kašnjenje

Ovaj napredak predstavlja ne samo tehnološki razvoj već i promjenu paradigme prema pristupačnijim, učinkovitijim i praktičnijim AI sustavima koji mogu učinkovito djelovati u okruženjima s ograničenim resursima, istovremeno pružajući sofisticirane agentne mogućnosti.

Kombinacija SLM-ova s naprednim strategijama implementacije, robusnim pozivanjem funkcija i standardiziranim protokolima za integraciju alata pozicionira ove sustave kao temelj za sljedeću generaciju AI agenata koji će transformirati način na koji komuniciramo s umjetnom inteligencijom i koristimo njezine prednosti u različitim industrijama i primjenama.

---

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane čovjeka. Ne preuzimamo odgovornost za bilo kakva nesporazuma ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.
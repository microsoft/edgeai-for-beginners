# Poglavlje 02: Osnove malih jezičnih modela

Ovo sveobuhvatno uvodno poglavlje pruža ključni pregled malih jezičnih modela (SLM), obuhvaćajući teorijske principe, strategije praktične implementacije i rješenja za primjenu u produkciji. Poglavlje uspostavlja temeljno znanje za razumijevanje modernih učinkovitih AI arhitektura i njihove strateške primjene u raznolikim računalnim okruženjima.

## Struktura poglavlja i okvir progresivnog učenja

### **[Odjeljak 1: Osnove obitelji Microsoft Phi modela](./01.PhiFamily.md)**
Prvi odjeljak uvodi revolucionarnu obitelj Phi modela tvrtke Microsoft, pokazujući kako kompaktni, učinkoviti modeli postižu izvanredne performanse uz značajno smanjene računalne zahtjeve. Ovaj temeljni odjeljak obuhvaća:

- **Evolucija filozofije dizajna**: Sveobuhvatan pregled razvoja obitelji Phi modela od Phi-1 do Phi-4, s naglaskom na revolucionarnu metodologiju "kvalitete udžbenika" za treniranje i skaliranje tijekom inferencije
- **Arhitektura usmjerena na učinkovitost**: Detaljna analiza optimizacije parametara, mogućnosti multimodalne integracije i optimizacija specifičnih za hardver na CPU, GPU i rubnim uređajima
- **Specijalizirane sposobnosti**: Dubinska analiza varijanti specifičnih za domenu, uključujući Phi-4-mini-reasoning za matematičke zadatke, Phi-4-multimodal za obradu vizualno-jezičnih podataka i Phi-3-Silica za ugrađenu primjenu u Windows 11

Ovaj odjeljak uspostavlja temeljno načelo da učinkovitost modela i sposobnosti mogu koegzistirati kroz inovativne metodologije treniranja i optimizaciju arhitekture.

### **[Odjeljak 2: Osnove obitelji Qwen](./02.QwenFamily.md)**
Drugi odjeljak prelazi na sveobuhvatan pristup otvorenog koda tvrtke Alibaba, pokazujući kako transparentni, dostupni modeli mogu postići konkurentne performanse uz zadržavanje fleksibilnosti primjene. Ključne teme uključuju:

- **Izvrsnost otvorenog koda**: Sveobuhvatan pregled evolucije Qwen modela od Qwen 1.0 do Qwen3, s naglaskom na masovno treniranje (36 trilijuna tokena) i višejezične sposobnosti u 119 jezika
- **Napredna arhitektura zaključivanja**: Detaljna analiza inovativnih sposobnosti "načina razmišljanja" u Qwen3, implementacija mješavine stručnjaka i specijaliziranih varijanti za kodiranje (Qwen-Coder) i matematiku (Qwen-Math)
- **Skalabilne opcije primjene**: Dubinska analiza raspona parametara od 0.5B do 235B, omogućujući scenarije primjene od mobilnih uređaja do korporativnih klastera

Ovaj odjeljak naglašava demokratizaciju AI tehnologije kroz dostupnost otvorenog koda uz zadržavanje konkurentnih performansi.

### **[Odjeljak 3: Osnove obitelji Gemma](./03.GemmaFamily.md)**
Treći odjeljak istražuje sveobuhvatan pristup tvrtke Google otvorenom kodu za multimodalni AI, pokazujući kako razvoj vođen istraživanjem može pružiti dostupne, ali moćne AI sposobnosti. Ovaj odjeljak obuhvaća:

- **Inovacija vođena istraživanjem**: Sveobuhvatan pregled arhitektura Gemma 3 i Gemma 3n, s naglaskom na revolucionarnu tehnologiju Per-Layer Embeddings (PLE) i strategije optimizacije za mobilne uređaje
- **Multimodalna izvrsnost**: Detaljna analiza integracije vizualno-jezičnih podataka, sposobnosti obrade zvuka i funkcionalnosti pozivanja koje omogućuju sveobuhvatna AI iskustva
- **Arhitektura usmjerena na mobilne uređaje**: Dubinska analiza revolucionarnih postignuća u učinkovitosti Gemma 3n, pružajući performanse od 2B-4B parametara uz memorijske zahtjeve od samo 2-3GB

Ovaj odjeljak pokazuje kako se vrhunska istraživanja mogu pretvoriti u praktična, dostupna AI rješenja koja omogućuju nove kategorije aplikacija.

### **[Odjeljak 4: Osnove obitelji BitNET](./04.BitNETFamily.md)**
Četvrti odjeljak predstavlja revolucionarni pristup tvrtke Microsoft kvantizaciji s 1 bitom, što predstavlja granicu ultra-učinkovite primjene AI. Ovaj napredni odjeljak obuhvaća:

- **Revolucionarna kvantizacija**: Sveobuhvatan pregled kvantizacije od 1.58 bita koristeći ternarne težine {-1, 0, +1}, postižući ubrzanja od 1.37x do 6.17x uz smanjenje energije od 55-82%
- **Optimizirani okvir za inferenciju**: Detaljna analiza implementacije bitnet.cpp s [https://github.com/microsoft/BitNet](https://github.com/microsoft/BitNet), specijaliziranih jezgri i optimizacija za različite platforme koje pružaju neviđene dobitke u učinkovitosti
- **Održivo AI vodstvo**: Dubinska analiza ekoloških prednosti, demokratiziranih mogućnosti primjene i novih scenarija aplikacija omogućena ekstremnom učinkovitošću

Ovaj odjeljak pokazuje kako revolucionarne tehnike kvantizacije mogu dramatično poboljšati učinkovitost AI uz zadržavanje konkurentnih performansi.

### **[Odjeljak 5: Osnove Microsoft Mu modela](./05.mumodel.md)**
Peti odjeljak istražuje revolucionarni Mu model tvrtke Microsoft, dizajniran posebno za primjenu na uređajima u sustavu Windows. Ovaj specijalizirani odjeljak obuhvaća:

- **Arhitektura usmjerena na uređaje**: Sveobuhvatan pregled specijaliziranog modela na uređaju ugrađenog u Windows 11 uređaje
- **Integracija sustava**: Detaljna analiza duboke integracije s Windows 11, pokazujući kako AI može poboljšati funkcionalnost sustava kroz nativnu implementaciju
- **Dizajn koji štiti privatnost**: Dubinska analiza offline rada, lokalne obrade i arhitekture usmjerene na privatnost koja čuva korisničke podatke na uređaju

Ovaj odjeljak pokazuje kako specijalizirani modeli mogu poboljšati funkcionalnost operativnog sustava Windows 11 uz zadržavanje privatnosti i performansi.

### **[Odjeljak 6: Osnove Phi-Silica](./06.phisilica.md)**
Završni odjeljak istražuje Microsoftov Phi-Silica, ultra-učinkovit jezični model ugrađen u Windows 11 za Copilot+ PC-e s NPU hardverom. Ovaj napredni odjeljak obuhvaća:

- **Izvanredne metričke učinkovitosti**: Sveobuhvatna analiza izvanrednih performansi Phi-Silica, pružajući 650 tokena u sekundi uz potrošnju energije od samo 1.5 vata
- **Optimizacija za NPU**: Detaljna analiza specijalizirane arhitekture dizajnirane za Neural Processing Units u Windows 11 Copilot+ PC-ima
- **Integracija za razvojne programere**: Dubinska analiza integracije s Windows App SDK-om, tehnika za prompt inženjering i najbolje prakse za implementaciju Phi-Silica u Windows 11 aplikacijama

Ovaj odjeljak uspostavlja vrhunac hardverski optimiziranih jezičnih modela na uređaju, pokazujući kako specijalizirane arhitekture modela u kombinaciji s namjenskim neuronskim hardverom mogu pružiti izvanredne AI performanse na potrošačkim uređajima s Windows 11.

## Sveobuhvatni ishodi učenja

Nakon završetka ovog uvodnog poglavlja, čitatelji će postići sljedeće:

1. **Razumijevanje arhitekture**: Duboko razumijevanje različitih filozofija dizajna SLM-a i njihovih implikacija za scenarije primjene
2. **Ravnoteža performansi i učinkovitosti**: Strateške sposobnosti donošenja odluka za odabir odgovarajućih arhitektura modela na temelju računalnih ograničenja i zahtjeva za performansama
3. **Fleksibilnost primjene**: Razumijevanje kompromisa između vlasničke optimizacije (Phi), dostupnosti otvorenog koda (Qwen), inovacija vođenih istraživanjem (Gemma) i revolucionarne učinkovitosti (BitNET)
4. **Perspektiva spremna za budućnost**: Uvid u nove trendove u učinkovitim AI arhitekturama i njihove implikacije za strategije primjene sljedeće generacije

## Fokus na praktičnu implementaciju

Poglavlje održava snažnu praktičnu orijentaciju kroz:

- **Kompletne primjere koda**: Primjeri implementacije spremni za produkciju za svaku obitelj modela, uključujući postupke fino podešavanja, strategije optimizacije i konfiguracije primjene
- **Sveobuhvatno uspoređivanje**: Detaljne usporedbe performansi različitih arhitektura modela, uključujući metričke učinkovitosti, procjene sposobnosti i optimizaciju za slučajeve upotrebe
- **Sigurnost za poduzeća**: Implementacije sigurnosti spremne za produkciju, strategije praćenja i najbolje prakse za pouzdanu primjenu
- **Integracija okvira**: Praktične smjernice za integraciju s popularnim okvirima, uključujući Hugging Face Transformers, vLLM, ONNX Runtime i specijalizirane alate za optimizaciju

## Strateška tehnološka mapa puta

Poglavlje završava analizom usmjerenom na budućnost:

- **Evolucija arhitekture**: Novi trendovi u dizajnu i optimizaciji učinkovitih modela
- **Integracija hardvera**: Napredak u specijaliziranim AI akceleratorima i njihov utjecaj na strategije primjene
- **Razvoj ekosustava**: Napori za standardizaciju i poboljšanje interoperabilnosti između različitih obitelji modela
- **Usvajanje u poduzećima**: Strateška razmatranja za planiranje primjene AI u organizacijama

## Scenariji primjene u stvarnom svijetu

Svaki odjeljak pruža sveobuhvatan pregled praktičnih primjena:

- **Mobilno i rubno računalstvo**: Optimizirane strategije primjene za okruženja s ograničenim resursima
- **Aplikacije za poduzeća**: Skalabilna rješenja za poslovnu inteligenciju, automatizaciju i korisničku podršku
- **Obrazovna tehnologija**: Dostupni AI za personalizirano učenje i generiranje sadržaja
- **Globalna primjena**: Višejezične i međukulturalne AI aplikacije

## Standardi tehničke izvrsnosti

Poglavlje naglašava implementaciju spremnu za produkciju kroz:

- **Majstorstvo optimizacije**: Napredne tehnike kvantizacije, optimizacije inferencije i upravljanja resursima
- **Praćenje performansi**: Sveobuhvatno prikupljanje metrika, sustavi upozorenja i analitika performansi
- **Implementacija sigurnosti**: Mjere sigurnosti na razini poduzeća, zaštita privatnosti i okviri za usklađenost
- **Planiranje skalabilnosti**: Strategije horizontalnog i vertikalnog skaliranja za rastuće računalne zahtjeve

Ovo uvodno poglavlje služi kao ključni preduvjet za napredne strategije primjene SLM-a, uspostavljajući i teorijsko razumijevanje i praktične sposobnosti potrebne za uspješnu implementaciju. Sveobuhvatan pregled osigurava da su čitatelji dobro opremljeni za donošenje informiranih odluka o arhitekturi i implementaciju robusnih, učinkovitih AI rješenja koja zadovoljavaju njihove specifične organizacijske zahtjeve, dok se pripremaju za buduće tehnološke razvojne korake.

Poglavlje povezuje najnovija AI istraživanja s praktičnim stvarnostima primjene, naglašavajući da moderne SLM arhitekture mogu pružiti izvanredne performanse uz zadržavanje operativne učinkovitosti, isplativosti i ekološke održivosti.

---

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane čovjeka. Ne preuzimamo odgovornost za bilo kakva nesporazuma ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.
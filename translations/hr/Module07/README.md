# Poglavlje 07: EdgeAI Primjeri

Edge AI predstavlja spoj umjetne inteligencije i rubnog računalstva, omogućujući inteligentnu obradu izravno na uređajima bez oslanjanja na povezivost s oblakom. Ovo poglavlje istražuje pet različitih implementacija EdgeAI-a na različitim platformama i okvirima, prikazujući svestranost i snagu pokretanja AI modela na rubu.

## 1. EdgeAI na NVIDIA Jetson Orin Nano

NVIDIA Jetson Orin Nano predstavlja revolucionarni korak u pristupačnom rubnom AI računalstvu, pružajući do 67 TOPS AI performansi u kompaktnom formatu veličine kreditne kartice. Ova moćna Edge AI platforma demokratizira razvoj generativne AI za hobiste, studente i profesionalne programere.

### Ključne značajke
- Pruža do 67 TOPS AI performansi—1,7X poboljšanje u odnosu na prethodnika
- 1024 CUDA jezgri i do 32 Tensor jezgre za AI obradu
- 6-jezgreni Arm Cortex-A78AE v8.2 64-bitni CPU s maksimalnom frekvencijom od 1,5 GHz
- Cijena od samo 249 USD, čineći platformu najpristupačnijom za programere, studente i kreatore

### Primjene
Jetson Orin Nano briljira u pokretanju modernih generativnih AI modela, uključujući vizijske transformatore, velike jezične modele i modele koji kombiniraju viziju i jezik. Posebno je dizajniran za GenAI slučajeve upotrebe, omogućujući pokretanje nekoliko LLM-ova na uređaju veličine dlana. Popularne primjene uključuju AI-pokretane robote, pametne dronove, inteligentne kamere i autonomne rubne uređaje.

**Saznajte više**: [NVIDIA Jetson Orin Nano SuperComputer: Sljedeća velika stvar u EdgeAI-u](https://medium.com/data-science-in-your-pocket/nvidias-jetson-orin-nano-supercomputer-the-next-big-thing-in-edgeai-e9eff687ae62)

## 2. EdgeAI u mobilnim aplikacijama s .NET MAUI i ONNX Runtime GenAI

Ovo rješenje pokazuje kako integrirati Generativnu AI i Velike Jezične Modele (LLM-ove) u mobilne aplikacije koje rade na više platformi koristeći .NET MAUI (Multi-platform App UI) i ONNX Runtime GenAI. Ovaj pristup omogućuje .NET programerima izradu sofisticiranih mobilnih aplikacija s AI podrškom koje rade nativno na Android i iOS uređajima.

### Ključne značajke
- Izgrađeno na .NET MAUI okviru, omogućujući jedinstvenu bazu koda za Android i iOS aplikacije
- Integracija ONNX Runtime GenAI omogućuje pokretanje generativnih AI modela izravno na mobilnim uređajima
- Podrška za različite hardverske akceleratore prilagođene mobilnim uređajima, uključujući CPU, GPU i specijalizirane mobilne AI procesore
- Optimizacije specifične za platformu poput CoreML za iOS i NNAPI za Android putem ONNX Runtime-a
- Implementira cijeli generativni AI proces uključujući predobradu i postobradu, inferenciju, obradu logita, pretraživanje i uzorkovanje te upravljanje KV cacheom

### Prednosti razvoja
Pristup .NET MAUI omogućuje programerima korištenje postojećih C# i .NET vještina dok izrađuju AI aplikacije za više platformi. ONNX Runtime GenAI okvir podržava različite arhitekture modela, uključujući Llama, Mistral, Phi, Gemma i mnoge druge. Optimizirane ARM64 jezgre ubrzavaju INT4 kvantiziranu matricnu množenje, osiguravajući učinkovite performanse na mobilnom hardveru uz zadržavanje poznatog .NET iskustva razvoja.

### Slučajevi upotrebe
Ovo rješenje idealno je za programere koji žele izraditi mobilne aplikacije s AI podrškom koristeći .NET tehnologije, uključujući inteligentne chatbotove, aplikacije za prepoznavanje slika, alate za prevođenje jezika i sustave za personalizirane preporuke koji rade potpuno na uređaju za poboljšanu privatnost i offline funkcionalnost.

**Saznajte više**: [.NET MAUI ONNX Runtime GenAI Primjer](https://github.com/microsoft/onnxruntime-genai/tree/jialli/genny-maui/examples/csharp/GennyMaui)

## 3. EdgeAI na Azureu s motorom za male jezične modele

Microsoftovo Azure EdgeAI rješenje fokusira se na učinkovitu implementaciju malih jezičnih modela (SLM-ova) u hibridnim okruženjima oblaka i ruba. Ovaj pristup povezuje AI usluge na razini oblaka s zahtjevima za implementaciju na rubu.

### Prednosti arhitekture
- Besprijekorna integracija s Azure AI uslugama
- Pokretanje SLM-ova/LLM-ova i multimodalnih modela na uređaju i u oblaku putem ONNX Runtime-a
- Optimizirano za implementaciju na razini poduzeća
- Podrška za kontinuirano ažuriranje i upravljanje modelima

### Slučajevi upotrebe
Azure EdgeAI implementacija briljira u scenarijima koji zahtijevaju AI implementaciju na razini poduzeća s mogućnostima upravljanja u oblaku. To uključuje inteligentnu obradu dokumenata, analitiku u stvarnom vremenu i hibridne AI tijekove rada koji koriste resurse oblaka i ruba.

**Saznajte više**: [Azure EdgeAI SLM Engine](https://github.com/microsoft/onnxruntime-genai/tree/main/examples/slm_engine)

## [4. EdgeAI s Windows ML](./windowdeveloper.md)

Windows ML predstavlja Microsoftov najmoderniji runtime optimiziran za učinkovitu inferenciju modela na uređaju i pojednostavljenu implementaciju, služeći kao temelj Windows AI Foundryja. Ova platforma omogućuje programerima izradu Windows aplikacija s AI podrškom koje koriste puni spektar PC hardvera.

### Mogućnosti platforme
- Radi na svim Windows 11 računalima s verzijom 24H2 (build 26100) ili novijom
- Radi na svim x64 i ARM64 PC hardverima, čak i na računalima bez NPU-ova ili GPU-ova
- Omogućuje programerima da koriste vlastite modele i učinkovito ih implementiraju u ekosustav silikonskih partnera, uključujući AMD, Intel, NVIDIA i Qualcomm, pokrivajući CPU, GPU, NPU
- Zahvaljujući infrastrukturnim API-jevima, programeri više ne moraju stvarati više verzija svoje aplikacije za ciljanje različitih silikonskih platformi

### Prednosti za programere
Windows ML apstrahira hardver i pružatelje izvršenja, omogućujući vam fokusiranje na pisanje koda. Osim toga, Windows ML automatski se ažurira kako bi podržao najnovije NPU-ove, GPU-ove i CPU-ove čim budu dostupni. Platforma pruža jedinstveni okvir za AI razvoj na raznolikom Windows hardverskom ekosustavu.

**Saznajte više**: 
- [Pregled Windows ML-a](https://learn.microsoft.com/en-us/windows/ai/new-windows-ml/overview)
- [Vodič za razvoj Windows EdgeAI-a](./windowdeveloper.md) - Sveobuhvatan vodič za razvoj Windows Edge AI-a

## [5. EdgeAI s Foundry Local aplikacijama](./foundrylocal.md)

Foundry Local omogućuje Windows i Mac programerima izradu aplikacija za Retrieval Augmented Generation (RAG) koristeći lokalne resurse u .NET-u, kombinirajući lokalne jezične modele sa semantičkim pretraživanjem. Ovaj pristup pruža AI rješenja usmjerena na privatnost koja rade potpuno na lokalnoj infrastrukturi.

### Tehnička arhitektura
- Kombinira Phi jezični model, lokalne ugrađene podatke i Semantic Kernel za stvaranje RAG scenarija
- Koristi ugrađene podatke kao vektore (nizove) vrijednosti s pomičnim zarezom koji predstavljaju sadržaj i njegovo semantičko značenje
- Semantic Kernel djeluje kao glavni orkestrator, integrirajući Phi i pametne komponente za stvaranje besprijekornog RAG procesa
- Podrška za lokalne vektorske baze podataka, uključujući SQLite i Qdrant

### Prednosti implementacije
RAG, ili Retrieval Augmented Generation, jednostavno znači "pronađi neke podatke i uključi ih u upit". Ova lokalna implementacija osigurava privatnost podataka dok pruža inteligentne odgovore temeljene na prilagođenim bazama znanja. Pristup je posebno vrijedan za scenarije u poduzećima koji zahtijevaju suverenitet podataka i mogućnosti offline rada.

**Saznajte više**: 
- [Foundry Local](./foundrylocal.md)
- [Primjeri Foundry Local RAG-a](https://github.com/microsoft/Foundry-Local/tree/main/samples/dotNET/rag)

### Windows Foundry Local

Microsoft Foundry Local pruža REST poslužitelj kompatibilan s OpenAI-jem, pokretan ONNX Runtime-om za pokretanje modela lokalno na Windowsu. Ispod je brzi, potvrđeni sažetak; pogledajte službenu dokumentaciju za sve detalje.

- Početak rada: https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started
- Arhitektura: https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture
- CLI referenca: https://learn.microsoft.com/azure/ai-foundry/foundry-local/reference/reference-cli
- Potpuni Windows vodič u ovom repozitoriju: [foundrylocal.md](./foundrylocal.md)

Instalirajte ili nadogradite na Windowsu (cmd.exe):
```cmd
winget install Microsoft.FoundryLocal
winget upgrade --id Microsoft.FoundryLocal
foundry --version
```

Istražite CLI kategorije:
```cmd
foundry model --help
foundry service --help
foundry cache --help
```

Pokrenite model i otkrijte dinamičnu krajnju točku:
```cmd
foundry model run gpt-oss-20b
foundry service status
```

Brza REST provjera za popis modela (zamijenite PORT iz statusa):
```cmd
curl -s http://localhost:PORT/v1/models
```

Savjeti:
- SDK integracija: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks
- Donosite vlastiti model (kompajlirajte): https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models

## Resursi za razvoj Windows EdgeAI-a

Za programere koji ciljaju isključivo Windows platformu, kreirali smo sveobuhvatan vodič koji pokriva cijeli Windows EdgeAI ekosustav. Ovaj resurs pruža detaljne informacije o Windows AI Foundryju, uključujući API-je, alate i najbolje prakse za razvoj EdgeAI-a na Windowsu.

### Windows AI Foundry platforma
Windows AI Foundry platforma pruža sveobuhvatan skup alata i API-ja posebno dizajniranih za razvoj Edge AI-a na Windows uređajima. To uključuje specijaliziranu podršku za hardver ubrzan NPU-om, integraciju Windows ML-a i tehnike optimizacije specifične za platformu.

**Sveobuhvatan vodič**: [Vodič za razvoj Windows EdgeAI-a](../windowdeveloper.md)

Ovaj vodič pokriva:
- Pregled i komponente Windows AI Foundry platforme
- Phi Silica API za učinkovitu inferenciju na NPU hardveru
- API-je za računalni vid za obradu slika i OCR
- Integraciju i optimizaciju Windows ML runtime-a
- Foundry Local CLI za lokalni razvoj i testiranje
- Strategije optimizacije hardvera za Windows uređaje
- Praktične primjere implementacije i najbolje prakse

### [AI Toolkit za razvoj Edge AI-a](./aitoolkit.md)
Za programere koji koriste Visual Studio Code, AI Toolkit ekstenzija pruža sveobuhvatno razvojno okruženje posebno dizajnirano za izradu, testiranje i implementaciju Edge AI aplikacija. Ovaj alat pojednostavljuje cijeli tijek rada razvoja Edge AI-a unutar VS Code-a.

**Vodič za razvoj**: [AI Toolkit za razvoj Edge AI-a](./aitoolkit.md)

Vodič za AI Toolkit pokriva:
- Otkrivanje i odabir modela za implementaciju na rubu
- Lokalni tijekovi testiranja i optimizacije
- ONNX i Ollama integraciju za rubne modele
- Tehnike konverzije i kvantizacije modela
- Razvoj agenata za rubne scenarije
- Procjenu performansi i praćenje
- Pripremu za implementaciju i najbolje prakse

## Zaključak

Ovih pet EdgeAI implementacija demonstriraju zrelost i raznolikost rubnih AI rješenja dostupnih danas. Od uređaja ubrzanih hardverom poput Jetson Orin Nano do softverskih okvira poput ONNX Runtime GenAI i Windows ML-a, programeri imaju neviđene opcije za implementaciju inteligentnih aplikacija na rubu.

Zajednička nit svih ovih platformi je demokratizacija AI mogućnosti, čineći sofisticirano strojno učenje dostupnim programerima različitih razina vještina i slučajeva upotrebe. Bilo da izrađujete mobilne aplikacije, desktop softver ili ugrađene sustave, ova EdgeAI rješenja pružaju temelj za sljedeću generaciju inteligentnih aplikacija koje rade učinkovito i privatno na rubu.

Svaka platforma nudi jedinstvene prednosti: Jetson Orin Nano za računalstvo ubrzano hardverom, ONNX Runtime GenAI za razvoj mobilnih aplikacija na više platformi, Azure EdgeAI za integraciju oblaka i ruba na razini poduzeća, Windows ML za nativne Windows aplikacije i Foundry Local za implementacije RAG-a usmjerene na privatnost. Zajedno, one predstavljaju sveobuhvatan ekosustav za razvoj EdgeAI-a.

[Sljedeći AI Toolkit](aitoolkit.md)

---

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane čovjeka. Ne preuzimamo odgovornost za nesporazume ili pogrešna tumačenja koja mogu proizaći iz korištenja ovog prijevoda.
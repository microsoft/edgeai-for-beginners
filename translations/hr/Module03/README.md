# Poglavlje 03: Implementacija Malih Jezičnih Modela (SLM-ova)

Ovo sveobuhvatno poglavlje istražuje cjelokupni životni ciklus implementacije Malih Jezičnih Modela (SLM-ova), obuhvaćajući teorijske osnove, praktične strategije implementacije i proizvodno spremna rješenja temeljena na kontejnerima. Poglavlje je strukturirano u tri progresivna dijela koji čitatelje vode od osnovnih koncepata do naprednih scenarija implementacije.

## Struktura poglavlja i put učenja

### **[Dio 1: Napredno učenje SLM-ova - Osnove i optimizacija](./01.SLMAdvancedLearning.md)**
Prvi dio postavlja teorijske temelje za razumijevanje Malih Jezičnih Modela i njihovog strateškog značaja u implementacijama AI-a na rubnim uređajima. Ovaj dio obuhvaća:

- **Okvir za klasifikaciju parametara**: Detaljno istraživanje kategorija SLM-ova od Mikro SLM-ova (100M-1.4B parametara) do Srednjih SLM-ova (14B-30B parametara), s posebnim fokusom na modele poput Phi-4-mini-3.8B, serije Qwen3 i Google Gemma3, uključujući analizu hardverskih zahtjeva i memorijskog otiska za svaki nivo modela
- **Napredne tehnike optimizacije**: Sveobuhvatan pregled metoda kvantizacije koristeći Llama.cpp, Microsoft Olive i Apple MLX okvire, uključujući najnoviju BitNET 1-bitnu kvantizaciju s praktičnim primjerima koda koji prikazuju kvantizacijske procese i rezultate usporedbe
- **Strategije nabave modela**: Dubinska analiza ekosustava Hugging Face i Azure AI Foundry Model Catalog za implementaciju SLM-ova na razini poduzeća, s primjerima koda za programatsko preuzimanje modela, validaciju i konverziju formata
- **API-ji za razvojne programere**: Primjeri koda u Pythonu, C++ i C# koji pokazuju kako učitati modele, izvršiti inferenciju i integrirati se s popularnim okvirima poput PyTorch, TensorFlow i ONNX Runtime

Ovaj temeljni dio naglašava ravnotežu između operativne učinkovitosti, fleksibilnosti implementacije i isplativosti koja čini SLM-ove idealnim za scenarije rubnog računalstva, s praktičnim primjerima koda koje programeri mogu izravno primijeniti u svojim projektima.

### **[Dio 2: Implementacija u lokalnom okruženju - Rješenja koja prioritiziraju privatnost](./02.DeployingSLMinLocalEnv.md)**
Drugi dio prelazi s teorije na praktičnu implementaciju, fokusirajući se na strategije lokalne implementacije koje daju prednost suverenitetu podataka i operativnoj neovisnosti. Ključna područja uključuju:

- **Ollama univerzalna platforma**: Sveobuhvatno istraživanje implementacije na više platformi s naglaskom na radne procese prilagođene programerima, upravljanje životnim ciklusom modela i prilagodbu putem Modelfiles, uključujući potpune primjere integracije REST API-ja i CLI automatizacijske skripte
- **Microsoft Foundry Local**: Rješenja za implementaciju na razini poduzeća s optimizacijom temeljenom na ONNX-u, integracijom Windows ML-a i sveobuhvatnim sigurnosnim značajkama, s primjerima koda u C# i Pythonu za integraciju u izvorne aplikacije
- **Komparativna analiza**: Detaljna usporedba okvira koja obuhvaća tehničku arhitekturu, karakteristike performansi i smjernice za optimizaciju slučajeva upotrebe, s benchmark kodom za procjenu brzine inferencije i korištenja memorije na različitim hardverima
- **Integracija API-ja**: Primjeri aplikacija koji pokazuju kako izgraditi web usluge, aplikacije za chat i cjevovode za obradu podataka koristeći lokalne implementacije SLM-ova, s primjerima koda u Node.js, Python Flask/FastAPI i ASP.NET Core
- **Okviri za testiranje**: Pristupi automatiziranom testiranju za osiguranje kvalitete modela, uključujući primjere jediničnih i integracijskih testova za implementacije SLM-ova

Ovaj dio pruža praktične smjernice za organizacije koje žele implementirati AI rješenja koja čuvaju privatnost, uz zadržavanje potpune kontrole nad svojim okruženjem implementacije, s gotovim primjerima koda koje programeri mogu prilagoditi svojim specifičnim zahtjevima.

### **[Dio 3: Implementacija u oblaku temeljena na kontejnerima - Rješenja za proizvodnu razinu](./03.DeployingSLMinCloud.md)**
Završni dio kulminira naprednim strategijama implementacije temeljenim na kontejnerima, s Microsoftovim Phi-4-mini-instruct kao primarnim studijem slučaja. Ovaj dio obuhvaća:

- **vLLM implementacija**: Optimizacija inferencije visokih performansi s OpenAI-kompatibilnim API-jima, naprednom GPU akceleracijom i konfiguracijom za proizvodnu razinu, uključujući potpune Dockerfile-ove, Kubernetes manifeste i parametre za podešavanje performansi
- **Ollama orkestracija kontejnera**: Pojednostavljeni radni procesi implementacije s Docker Compose-om, varijantama optimizacije modela i integracijom web sučelja, s primjerima CI/CD cjevovoda za automatiziranu implementaciju i testiranje
- **Implementacija ONNX Runtime-a**: Optimizirana implementacija za rubne uređaje s sveobuhvatnom konverzijom modela, strategijama kvantizacije i kompatibilnošću na više platformi, uključujući detaljne primjere koda za optimizaciju i implementaciju modela
- **Praćenje i preglednost**: Implementacija Prometheus/Grafana nadzornih ploča s prilagođenim metrikama za praćenje performansi SLM-ova, uključujući konfiguracije za upozorenja i agregaciju logova
- **Balansiranje opterećenja i skaliranje**: Praktični primjeri strategija horizontalnog i vertikalnog skaliranja s konfiguracijama za automatsko skaliranje temeljenim na korištenju CPU/GPU-a i obrascima zahtjeva
- **Ojačavanje sigurnosti**: Najbolje prakse za sigurnost kontejnera uključujući smanjenje privilegija, mrežne politike i upravljanje tajnama za API ključeve i vjerodajnice za pristup modelima

Svaki pristup implementaciji predstavljen je s kompletnim primjerima konfiguracije, postupcima testiranja, kontrolnim listama za spremnost za proizvodnju i predlošcima infrastrukture kao koda koje programeri mogu izravno primijeniti u svojim radnim procesima implementacije.

## Ključni ishodi učenja

Završetkom ovog poglavlja, čitatelji će savladati:

1. **Strateški odabir modela**: Razumijevanje granica parametara i odabir odgovarajućih SLM-ova na temelju ograničenja resursa i zahtjeva performansi
2. **Majstorstvo optimizacije**: Implementacija naprednih tehnika kvantizacije u različitim okvirima za postizanje optimalne ravnoteže između performansi i učinkovitosti
3. **Fleksibilnost implementacije**: Odabir između lokalnih rješenja koja čuvaju privatnost i skalabilnih implementacija temeljenih na kontejnerima prema potrebama organizacije
4. **Spremnost za proizvodnju**: Konfiguriranje sustava za praćenje, sigurnost i skaliranje za implementacije SLM-ova na razini poduzeća

## Praktični fokus i primjene u stvarnom svijetu

Poglavlje održava snažnu praktičnu orijentaciju kroz:

- **Praktične primjere**: Kompletne konfiguracijske datoteke, postupci testiranja API-ja i skripte za implementaciju
- **Usporedba performansi**: Detaljne usporedbe brzine inferencije, korištenja memorije i zahtjeva za resursima
- **Sigurnosni aspekti**: Prakse sigurnosti na razini poduzeća, okviri za usklađenost i strategije zaštite podataka
- **Najbolje prakse**: Smjernice dokazane u proizvodnji za praćenje, skaliranje i održavanje

## Perspektiva usmjerena na budućnost

Poglavlje završava uvidima u nadolazeće trendove, uključujući:

- Napredne arhitekture modela s poboljšanim omjerima učinkovitosti
- Dublju integraciju hardvera s specijaliziranim AI akceleratorima
- Evoluciju ekosustava prema standardizaciji i interoperabilnosti
- Obrasce usvajanja u poduzećima vođene privatnošću i zahtjevima za usklađenost

Ovaj sveobuhvatan pristup osigurava da su čitatelji dobro opremljeni za navigaciju trenutnim izazovima implementacije SLM-ova i budućim tehnološkim razvojem, donoseći informirane odluke koje su u skladu s njihovim specifičnim organizacijskim zahtjevima i ograničenjima.

Poglavlje služi kao praktični vodič za neposrednu implementaciju i strateški resurs za dugoročno planiranje implementacije AI-a, naglašavajući kritičnu ravnotežu između sposobnosti, učinkovitosti i operativne izvrsnosti koja definira uspješne implementacije SLM-ova.

---

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane čovjeka. Ne preuzimamo odgovornost za bilo kakva nesporazuma ili pogrešna tumačenja koja mogu proizaći iz korištenja ovog prijevoda.
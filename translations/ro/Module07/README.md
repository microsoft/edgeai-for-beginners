# Capitolul 07: Exemple de EdgeAI

Edge AI reprezintă convergența dintre inteligența artificială și edge computing, permițând procesarea inteligentă direct pe dispozitive, fără a depinde de conectivitatea cloud. Acest capitol explorează cinci implementări distincte de EdgeAI pe diverse platforme și cadre, evidențiind versatilitatea și puterea rulării modelelor AI la margine.

## 1. EdgeAI pe NVIDIA Jetson Orin Nano

NVIDIA Jetson Orin Nano reprezintă o inovație în computarea AI la margine, oferind până la 67 TOPS de performanță AI într-un format compact, de dimensiunea unui card de credit. Această platformă puternică democratizează dezvoltarea AI generativă pentru pasionați, studenți și dezvoltatori profesioniști.

### Caracteristici principale
- Oferă până la 67 TOPS de performanță AI—o îmbunătățire de 1,7X față de predecesorul său
- 1024 nuclee CUDA și până la 32 nuclee Tensor pentru procesarea AI
- CPU Arm Cortex-A78AE v8.2 64-bit cu 6 nuclee și frecvență maximă de 1,5 GHz
- Preț de doar 249 USD, oferind dezvoltatorilor, studenților și creatorilor cea mai accesibilă platformă

### Aplicații
Jetson Orin Nano excelează în rularea modelelor AI generative moderne, inclusiv transformatoare de viziune, modele de limbaj mari și modele de viziune-limbaj. Este conceput special pentru cazuri de utilizare GenAI, iar acum poți rula mai multe LLM-uri pe un dispozitiv de dimensiunea palmei. Cazuri populare de utilizare includ roboți inteligenți, drone inteligente, camere inteligente și dispozitive autonome la margine.

**Aflați mai multe**: [SuperComputerul Jetson Orin Nano de la NVIDIA: Următorul mare pas în EdgeAI](https://medium.com/data-science-in-your-pocket/nvidias-jetson-orin-nano-supercomputer-the-next-big-thing-in-edgeai-e9eff687ae62)

## 2. EdgeAI în aplicații mobile cu .NET MAUI și ONNX Runtime GenAI

Această soluție demonstrează cum să integrezi AI generativă și modele de limbaj mari (LLMs) în aplicații mobile cross-platform folosind .NET MAUI (Multi-platform App UI) și ONNX Runtime GenAI. Această abordare permite dezvoltatorilor .NET să creeze aplicații mobile sofisticate, alimentate de AI, care rulează nativ pe dispozitive Android și iOS.

### Caracteristici principale
- Construit pe cadrul .NET MAUI, oferind un singur cod pentru aplicații Android și iOS
- Integrarea ONNX Runtime GenAI permite rularea modelelor AI generative direct pe dispozitive mobile
- Suportă diverse acceleratoare hardware adaptate pentru dispozitive mobile, inclusiv CPU, GPU și procesoare AI specializate
- Optimizări specifice platformei, cum ar fi CoreML pentru iOS și NNAPI pentru Android prin ONNX Runtime
- Implementează întregul ciclu AI generativ, inclusiv pre și post procesare, inferență, procesarea logit-urilor, căutare și eșantionare, și gestionarea cache-ului KV

### Beneficii pentru dezvoltatori
Abordarea .NET MAUI permite dezvoltatorilor să își valorifice abilitățile existente în C# și .NET în timp ce construiesc aplicații AI cross-platform. Cadrul ONNX Runtime GenAI suportă multiple arhitecturi de modele, inclusiv Llama, Mistral, Phi, Gemma și multe altele. Nucleele ARM64 optimizate accelerează multiplicarea matricelor INT4 cuantificate, asigurând performanță eficientă pe hardware-ul mobil, menținând în același timp experiența familiară de dezvoltare .NET.

### Cazuri de utilizare
Această soluție este ideală pentru dezvoltatorii care doresc să creeze aplicații mobile alimentate de AI folosind tehnologii .NET, inclusiv chatbot-uri inteligente, aplicații de recunoaștere a imaginilor, instrumente de traducere a limbajului și sisteme de recomandare personalizate care rulează complet pe dispozitiv pentru o confidențialitate sporită și capacitate offline.

**Aflați mai multe**: [Exemplu .NET MAUI ONNX Runtime GenAI](https://github.com/microsoft/onnxruntime-genai/tree/jialli/genny-maui/examples/csharp/GennyMaui)

## 3. EdgeAI în Azure cu motorul Small Language Models

Soluția EdgeAI bazată pe Azure de la Microsoft se concentrează pe implementarea eficientă a modelelor de limbaj mici (SLMs) în medii hibride cloud-margine. Această abordare face legătura între serviciile AI la scară cloud și cerințele de implementare la margine.

### Avantajele arhitecturii
- Integrare fără probleme cu serviciile Azure AI
- Rulează SLM-uri/LLM-uri și modele multi-modale pe dispozitiv și în cloud cu ONNX Runtime
- Optimizat pentru implementări la scară enterprise
- Suport pentru actualizări și gestionarea continuă a modelelor

### Cazuri de utilizare
Implementarea EdgeAI în Azure excelează în scenarii care necesită implementare AI la nivel enterprise cu capacități de gestionare în cloud. Acestea includ procesarea inteligentă a documentelor, analize în timp real și fluxuri de lucru AI hibride care valorifică atât resursele cloud, cât și cele de margine.

**Aflați mai multe**: [Motorul Azure EdgeAI SLM](https://github.com/microsoft/onnxruntime-genai/tree/main/examples/slm_engine)

## [4. EdgeAI cu Windows ML](./windowdeveloper.md)

Windows ML reprezintă runtime-ul avansat de la Microsoft, optimizat pentru inferența performantă a modelelor pe dispozitiv și implementarea simplificată, servind ca fundație pentru Windows AI Foundry. Această platformă permite dezvoltatorilor să creeze aplicații Windows alimentate de AI, care valorifică întregul spectru de hardware PC.

### Capacitățile platformei
- Funcționează pe toate PC-urile Windows 11 care rulează versiunea 24H2 (build 26100) sau mai mare
- Compatibil cu toate hardware-urile PC x64 și ARM64, chiar și PC-urile fără NPU-uri sau GPU-uri
- Permite dezvoltatorilor să aducă propriile modele și să le implementeze eficient în ecosistemul partenerilor de siliciu, inclusiv AMD, Intel, NVIDIA și Qualcomm, acoperind CPU, GPU, NPU
- Prin utilizarea API-urilor de infrastructură, dezvoltatorii nu mai trebuie să creeze mai multe versiuni ale aplicației pentru a viza diferite siliciuri

### Beneficii pentru dezvoltatori
Windows ML abstractizează hardware-ul și furnizorii de execuție, astfel încât să te poți concentra pe scrierea codului. În plus, Windows ML se actualizează automat pentru a sprijini cele mai recente NPU-uri, GPU-uri și CPU-uri pe măsură ce sunt lansate. Platforma oferă un cadru unificat pentru dezvoltarea AI în ecosistemul divers de hardware Windows.

**Aflați mai multe**: 
- [Prezentare generală Windows ML](https://learn.microsoft.com/en-us/windows/ai/new-windows-ml/overview)
- [Ghid de dezvoltare Windows EdgeAI](./windowdeveloper.md) - Ghid cuprinzător pentru dezvoltarea AI la margine pe Windows

## [5. EdgeAI cu aplicații locale Foundry](./foundrylocal.md)

Foundry Local permite dezvoltatorilor Windows și Mac să construiască aplicații de Generare Augmentată prin Recuperare (RAG) folosind resurse locale în .NET, combinând modele de limbaj locale cu capacități de căutare semantică. Această abordare oferă soluții AI axate pe confidențialitate, care funcționează complet pe infrastructura locală.

### Arhitectura tehnică
- Combină modelul de limbaj Phi, Embeddings Locale și Kernel Semantic pentru a crea un scenariu RAG
- Utilizează embeddings ca vectori (matrici) de valori în virgulă mobilă care reprezintă conținutul și semnificația sa semantică
- Kernelul Semantic acționează ca orchestrator principal, integrând Phi și Componentele Inteligente pentru a crea un flux RAG fără probleme
- Suport pentru baze de date vectoriale locale, inclusiv SQLite și Qdrant

### Beneficii ale implementării
RAG, sau Generare Augmentată prin Recuperare, este doar o modalitate sofisticată de a spune „căutăm niște informații și le includem în prompt”. Această implementare locală asigură confidențialitatea datelor, oferind răspunsuri inteligente bazate pe baze de cunoștințe personalizate. Abordarea este deosebit de valoroasă pentru scenarii enterprise care necesită suveranitate asupra datelor și capacități de operare offline.

**Aflați mai multe**: 
- [Foundry Local](./foundrylocal.md)
- [Exemple RAG Foundry Local](https://github.com/microsoft/Foundry-Local/tree/main/samples/dotNET/rag)

### Windows Foundry Local

Microsoft Foundry Local oferă un server REST compatibil cu OpenAI, alimentat de ONNX Runtime, pentru rularea modelelor local pe Windows. Mai jos este un rezumat rapid validat; consultați documentația oficială pentru detalii complete.

- Începeți: https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started
- Arhitectură: https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture
- Referință CLI: https://learn.microsoft.com/azure/ai-foundry/foundry-local/reference/reference-cli
- Ghid complet pentru Windows în acest repo: [foundrylocal.md](./foundrylocal.md)

Instalare sau upgrade pe Windows (cmd.exe):
```cmd
winget install Microsoft.FoundryLocal
winget upgrade --id Microsoft.FoundryLocal
foundry --version
```

Explorați categoriile CLI:
```cmd
foundry model --help
foundry service --help
foundry cache --help
```

Rulați un model și descoperiți endpoint-ul dinamic:
```cmd
foundry model run gpt-oss-20b
foundry service status
```

Verificare rapidă REST pentru listarea modelelor (înlocuiți PORT din status):
```cmd
curl -s http://localhost:PORT/v1/models
```

Sfaturi:
- Integrare SDK: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks
- Aduceți propriul model (compilare): https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models

## Resurse pentru dezvoltarea Windows EdgeAI

Pentru dezvoltatorii care vizează în mod specific platforma Windows, am creat un ghid cuprinzător care acoperă întregul ecosistem Windows EdgeAI. Această resursă oferă informații detaliate despre Windows AI Foundry, inclusiv API-uri, instrumente și cele mai bune practici pentru dezvoltarea EdgeAI pe Windows.

### Platforma Windows AI Foundry
Platforma Windows AI Foundry oferă o suită cuprinzătoare de instrumente și API-uri special concepute pentru dezvoltarea AI la margine pe dispozitive Windows. Aceasta include suport specializat pentru hardware accelerat de NPU, integrarea Windows ML și tehnici de optimizare specifice platformei.

**Ghid cuprinzător**: [Ghid de dezvoltare Windows EdgeAI](../windowdeveloper.md)

Acest ghid acoperă:
- Prezentare generală și componente ale platformei Windows AI Foundry
- API-ul Phi Silica pentru inferență eficientă pe hardware NPU
- API-uri de Computer Vision pentru procesarea imaginilor și OCR
- Integrarea și optimizarea runtime-ului Windows ML
- CLI Foundry Local pentru dezvoltare și testare locală
- Strategii de optimizare hardware pentru dispozitive Windows
- Exemple practice de implementare și cele mai bune practici

### [Toolkit AI pentru dezvoltarea Edge AI](./aitoolkit.md)
Pentru dezvoltatorii care folosesc Visual Studio Code, extensia AI Toolkit oferă un mediu de dezvoltare cuprinzător, special conceput pentru construirea, testarea și implementarea aplicațiilor Edge AI. Acest toolkit simplifică întregul flux de lucru de dezvoltare Edge AI în cadrul VS Code.

**Ghid de dezvoltare**: [Toolkit AI pentru dezvoltarea Edge AI](./aitoolkit.md)

Ghidul Toolkit AI acoperă:
- Descoperirea și selecția modelelor pentru implementarea la margine
- Fluxuri de testare și optimizare locală
- Integrarea ONNX și Ollama pentru modele la margine
- Tehnici de conversie și cuantizare a modelelor
- Dezvoltarea agenților pentru scenarii la margine
- Evaluarea performanței și monitorizarea
- Pregătirea pentru implementare și cele mai bune practici

## Concluzie

Aceste cinci implementări EdgeAI demonstrează maturitatea și diversitatea soluțiilor AI la margine disponibile astăzi. De la dispozitive accelerate hardware, precum Jetson Orin Nano, la cadre software, precum ONNX Runtime GenAI și Windows ML, dezvoltatorii au opțiuni fără precedent pentru implementarea aplicațiilor inteligente la margine.

Firul comun al acestor platforme este democratizarea capacităților AI, făcând învățarea automată sofisticată accesibilă dezvoltatorilor de diferite niveluri de competență și cazuri de utilizare. Fie că construiești aplicații mobile, software desktop sau sisteme încorporate, aceste soluții EdgeAI oferă fundația pentru generația următoare de aplicații inteligente care funcționează eficient și privat la margine.

Fiecare platformă oferă avantaje unice: Jetson Orin Nano pentru computarea accelerată hardware la margine, ONNX Runtime GenAI pentru dezvoltarea mobilă cross-platform, Azure EdgeAI pentru integrarea cloud-margine la nivel enterprise, Windows ML pentru aplicații native Windows și Foundry Local pentru implementări RAG axate pe confidențialitate. Împreună, ele reprezintă un ecosistem cuprinzător pentru dezvoltarea EdgeAI.

[Următorul Toolkit AI](aitoolkit.md)

---

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să asigurăm acuratețea, vă rugăm să fiți conștienți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa natală ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.
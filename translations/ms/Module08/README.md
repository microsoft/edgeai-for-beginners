# Modul 08: Praktikal Dengan Microsoft Foundry Local - Toolkit Pembangun Lengkap

## Gambaran Keseluruhan

[Microsoft Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/) mewakili generasi baharu pembangunan AI di hujung, menyediakan alat yang berkuasa untuk pembangun membina, melancarkan, dan menskalakan aplikasi AI secara tempatan sambil mengekalkan integrasi lancar dengan Azure AI Foundry. Modul ini memberikan liputan menyeluruh tentang Foundry Local dari pemasangan hingga pembangunan agen lanjutan.

**Teknologi Utama:**
- Microsoft Foundry Local CLI dan SDK
- Integrasi Azure AI Foundry
- Inferens model pada peranti
- Cache dan pengoptimuman model tempatan
- Seni bina berasaskan agen

## Objektif Pembelajaran

Dengan melengkapkan modul ini, anda akan:

- **Menguasai Foundry Local**: Pasang, konfigurasikan, dan optimalkan untuk pembangunan Windows 11
- **Melancarkan Pelbagai Model**: Jalankan model phi, qwen, deepseek, dan GPT secara tempatan dengan arahan CLI
- **Membina Penyelesaian Pengeluaran**: Cipta aplikasi AI dengan kejuruteraan prompt lanjutan dan integrasi data
- **Manfaatkan Ekosistem Sumber Terbuka**: Integrasi model Hugging Face dan sumbangan komuniti
- **Membangunkan Agen AI**: Bina agen pintar dengan keupayaan asas dan orkestrasi
- **Laksanakan Corak Perusahaan**: Cipta penyelesaian AI modular dan berskala untuk pelancaran pengeluaran

## Struktur Sesi

### [1: Memulakan dengan Foundry Local](./01.FoundryLocalSetup.md)
**Fokus**: Pemasangan, persediaan CLI, pelancaran model, dan pengoptimuman perkakasan

**Topik Utama**: Pemasangan lengkap • Arahan CLI • Cache model • Pecutan perkakasan • Pelancaran pelbagai model

**Contoh**: [REST Chat Quickstart](./samples/01/README.md) • [Integrasi OpenAI SDK](./samples/02/README.md) • [Penemuan & Penanda Aras Model](./samples/03/README.md)

**Tempoh**: 2-3 jam | **Tahap**: Pemula

---

### [2: Membina Penyelesaian AI dengan Azure AI Foundry](./02.AzureAIFoundryIntegration.md)
**Fokus**: Kejuruteraan prompt lanjutan, integrasi data, dan sambungan awan

**Topik Utama**: Kejuruteraan prompt • Integrasi data • Aliran kerja Azure • Pengoptimuman prestasi • Pemantauan

**Contoh**: [Aplikasi Chainlit RAG](./samples/04/README.md)

**Tempoh**: 2-3 jam | **Tahap**: Pertengahan

---

### [3: Model Sumber Terbuka Foundry Local](./03.OpenSourceModels.md)
**Fokus**: Integrasi Hugging Face, strategi BYOM, dan model komuniti

**Topik Utama**: Integrasi HuggingFace • Bawa model anda sendiri • Wawasan Model Mondays • Sumbangan komuniti • Pemilihan model

**Contoh**: [Orkestrasi Multi-Agen](./samples/05/README.md)

**Tempoh**: 2-3 jam | **Tahap**: Pertengahan

---

### [4: Terokai Model Terkini](./04.CuttingEdgeModels.md)
**Fokus**: LLM vs SLM, pelaksanaan EdgeAI, dan demo lanjutan

**Topik Utama**: Perbandingan model • Inferens hujung vs awan • Phi + ONNX Runtime • Aplikasi Chainlit RAG • Pengoptimuman WebGPU

**Contoh**: [Router Model-as-Tools](./samples/06/README.md)

**Tempoh**: 3-4 jam | **Tahap**: Lanjutan

---

### [5: Bina Agen Berkuasa AI dengan Cepat](./05.AIPoweredAgents.md)
**Fokus**: Seni bina agen, prompt sistem, asas, dan orkestrasi

**Topik Utama**: Corak reka bentuk agen • Kejuruteraan prompt sistem • Teknik asas • Sistem multi-agen • Pelancaran pengeluaran

**Contoh**: [Orkestrasi Multi-Agen](./samples/05/README.md) • [Sistem Multi-Agen Lanjutan](./samples/09/README.md)

**Tempoh**: 3-4 jam | **Tahap**: Lanjutan

---

### [6: Foundry Local - Model sebagai Alat](./06.ModelsAsTools.md)
**Fokus**: Penyelesaian AI modular, penskalaan perusahaan, dan corak pengeluaran

**Topik Utama**: Model sebagai alat • Pelancaran pada peranti • Integrasi SDK/API • Seni bina perusahaan • Strategi penskalaan

**Contoh**: [Router Model-as-Tools](./samples/06/README.md) • [Kerangka Alat Foundry](./samples/10/README.md)

**Tempoh**: 3-4 jam | **Tahap**: Pakar

---

### [7: Corak Integrasi API Langsung](./samples/07/README.md)
**Fokus**: Integrasi API REST tulen tanpa kebergantungan SDK untuk kawalan maksimum

**Topik Utama**: Pelaksanaan klien HTTP • Pengesahan tersuai • Pemantauan kesihatan model • Respons penstriman • Pengendalian ralat pengeluaran

**Contoh**: [Klien API Langsung](./samples/07/README.md)

**Tempoh**: 2-3 jam | **Tahap**: Pertengahan

---

### [8: Aplikasi Chat Asli Windows 11](./samples/08/README.md)
**Fokus**: Membina aplikasi chat asli moden dengan integrasi Foundry Local

**Topik Utama**: Pembangunan Electron • Sistem Reka Bentuk Fluent • Integrasi Windows asli • Penstriman masa nyata • Reka bentuk antara muka chat

**Contoh**: [Aplikasi Chat Windows 11](./samples/08/README.md)

**Tempoh**: 3-4 jam | **Tahap**: Lanjutan

---

### [9: Orkestrasi Multi-Agen Lanjutan](./samples/09/README.md)
**Fokus**: Penyelarasan agen yang canggih, delegasi tugas khusus, dan aliran kerja AI kolaboratif

**Topik Utama**: Penyelarasan agen pintar • Corak panggilan fungsi • Komunikasi antara agen • Orkestrasi aliran kerja • Mekanisme jaminan kualiti

**Contoh**: [Sistem Multi-Agen Lanjutan](./samples/09/README.md)

**Tempoh**: 4-5 jam | **Tahap**: Pakar

---

### [10: Foundry Local sebagai Kerangka Alat](./samples/10/README.md)
**Fokus**: Seni bina berorientasikan alat untuk mengintegrasikan Foundry Local ke dalam aplikasi dan kerangka kerja sedia ada

**Topik Utama**: Integrasi LangChain • Fungsi Kernel Semantik • Kerangka API REST • Alat CLI • Integrasi Jupyter • Corak pelancaran pengeluaran

**Contoh**: [Kerangka Alat Foundry](./samples/10/README.md)

**Tempoh**: 4-5 jam | **Tahap**: Pakar

## Prasyarat

### Keperluan Sistem
- **Sistem Operasi**: Windows 11 (22H2 atau lebih baru)
- **Memori**: 16GB RAM (32GB disyorkan untuk model yang lebih besar)
- **Storan**: 50GB ruang kosong untuk cache model
- **Perkakasan**: Peranti dengan NPU disyorkan (PC Copilot+), GPU pilihan
- **Rangkaian**: Internet berkelajuan tinggi untuk muat turun model awal

### Persekitaran Pembangunan
- Visual Studio Code dengan sambungan AI Toolkit
- Python 3.10+ dan pip
- Git untuk kawalan versi
- PowerShell atau Command Prompt
- Azure CLI (pilihan untuk integrasi awan)

### Pengetahuan Prasyarat
- Pemahaman asas tentang konsep AI/ML
- Familiariti dengan baris arahan
- Asas pengaturcaraan Python
- Konsep API REST
- Pengetahuan asas tentang prompt dan inferens model

## Garis Masa Modul

**Jumlah Masa Anggaran**: 30-38 jam

| Sesi | Kawasan Fokus | Contoh | Masa | Kerumitan |
|------|---------------|--------|------|-----------|
|  1 | Persediaan & Asas | 01, 02, 03 | 2-3 jam | Pemula |
|  2 | Penyelesaian AI | 04 | 2-3 jam | Pertengahan |
|  3 | Sumber Terbuka | 05 | 2-3 jam | Pertengahan |
|  4 | Model Lanjutan | 06 | 3-4 jam | Lanjutan |
|  5 | Agen AI | 05, 09 | 3-4 jam | Lanjutan |
|  6 | Alat Perusahaan | 06, 10 | 3-4 jam | Pakar |
|  7 | Integrasi API Langsung | 07 | 2-3 jam | Pertengahan |
|  8 | Aplikasi Chat Windows 11 | 08 | 3-4 jam | Lanjutan |
|  9 | Multi-Agen Lanjutan | 09 | 4-5 jam | Pakar |
| 10 | Kerangka Alat | 10 | 4-5 jam | Pakar |

## Sumber Utama

**Dokumentasi Rasmi:**
- [Microsoft Foundry Local GitHub](https://github.com/microsoft/Foundry-Local) - Kod sumber dan contoh rasmi
- [Dokumentasi Azure AI Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/) - Panduan lengkap pemasangan dan penggunaan
- [Siri Model Mondays](https://aka.ms/model-mondays) - Sorotan model mingguan dan tutorial

**Komuniti & Sokongan:**
- [Perbincangan Foundry Local](https://github.com/microsoft/Foundry-Local/discussions) - Q&A komuniti dan permintaan ciri
- [Komuniti Pembangun AI Microsoft](https://techcommunity.microsoft.com/category/artificialintelligence) - Berita terkini dan amalan terbaik

## Hasil Pembelajaran

Setelah melengkapkan modul ini, anda akan dilengkapi untuk:

### Penguasaan Teknikal
- **Melancarkan dan Mengurus**: Pemasangan Foundry Local di persekitaran pembangunan dan pengeluaran
- **Integrasi Model**: Bekerja dengan lancar dengan pelbagai keluarga model dari Microsoft, Hugging Face, dan sumber komuniti
- **Membina Aplikasi**: Cipta aplikasi AI sedia pengeluaran dengan ciri dan pengoptimuman lanjutan
- **Membangunkan Agen**: Laksanakan agen AI yang canggih dengan asas, penaakulan, dan integrasi alat

### Pemahaman Strategik
- **Keputusan Seni Bina**: Membuat pilihan yang bijak antara pelancaran tempatan vs awan
- **Pengoptimuman Prestasi**: Mengoptimumkan prestasi inferens di pelbagai konfigurasi perkakasan
- **Penskalaan Perusahaan**: Reka aplikasi yang berskala dari prototaip tempatan ke pelancaran perusahaan
- **Privasi dan Keselamatan**: Laksanakan penyelesaian AI yang memelihara privasi dengan inferens tempatan

### Keupayaan Inovasi
- **Prototip Pantas**: Cepat membina dan menguji konsep aplikasi AI di semua 10 corak contoh
- **Integrasi Komuniti**: Manfaatkan model sumber terbuka dan sumbang kepada ekosistem
- **Corak Lanjutan**: Laksanakan corak AI terkini termasuk RAG, agen, dan integrasi alat
- **Penguasaan Kerangka**: Integrasi tahap pakar dengan LangChain, Kernel Semantik, Chainlit, dan Electron
- **Pelancaran Pengeluaran**: Melancarkan penyelesaian AI berskala dari prototaip tempatan ke sistem perusahaan
- **Pembangunan Sedia Masa Depan**: Bina aplikasi yang sedia untuk teknologi dan corak AI yang muncul

## Memulakan

1. **Persediaan Persekitaran**: Pastikan Windows 11 dengan perkakasan yang disyorkan (lihat Prasyarat)
2. **Pasang Foundry Local**: Ikuti Sesi 1 untuk pemasangan dan konfigurasi lengkap
3. **Jalankan Contoh 01**: Mulakan dengan integrasi API REST asas untuk mengesahkan persediaan
4. **Teruskan Melalui Contoh**: Lengkapkan contoh 01-10 untuk penguasaan menyeluruh

## Metrik Kejayaan

Jejaki kemajuan anda melalui semua 10 contoh menyeluruh:

### Tahap Asas (Contoh 01-03)
- [ ] Berjaya memasang dan mengkonfigurasi Foundry Local
- [ ] Lengkapkan integrasi API REST (Contoh 01)
- [ ] Laksanakan keserasian OpenAI SDK (Contoh 02)
- [ ] Lakukan penemuan dan penanda aras model (Contoh 03)

### Tahap Aplikasi (Contoh 04-06)
- [ ] Melancarkan dan menjalankan sekurang-kurangnya 4 keluarga model yang berbeza
- [ ] Membina aplikasi chat RAG yang berfungsi (Contoh 04)
- [ ] Cipta sistem orkestrasi multi-agen (Contoh 05)
- [ ] Laksanakan penghala model pintar (Contoh 06)

### Tahap Integrasi Lanjutan (Contoh 07-10)
- [ ] Membina klien API sedia pengeluaran (Contoh 07)
- [ ] Membangunkan aplikasi chat asli Windows 11 (Contoh 08)
- [ ] Laksanakan sistem multi-agen lanjutan (Contoh 09)
- [ ] Cipta kerangka alat yang komprehensif (Contoh 10)

### Petunjuk Penguasaan
- [ ] Berjaya menjalankan semua 10 contoh tanpa ralat
- [ ] Sesuaikan sekurang-kurangnya 3 contoh untuk kes penggunaan tertentu
- [ ] Melancarkan 2+ contoh dalam persekitaran seperti pengeluaran
- [ ] Menyumbang penambahbaikan atau sambungan kepada kod contoh
- [ ] Mengintegrasikan corak Foundry Local ke dalam projek peribadi/profesional

## Panduan Permulaan Pantas - Semua 10 Contoh

### Persediaan Persekitaran (Diperlukan untuk Semua Contoh)

```powershell
# 1. Clone and navigate to Module08
cd Module08

# 2. Create Python virtual environment
py -m venv .venv
.\.venv\Scripts\activate

# 3. Install base dependencies
pip install -r requirements.txt

# 4. Install Foundry Local (if not already installed)
winget install Microsoft.FoundryLocal

# 5. Verify Foundry Local installation
foundry --version
foundry model list
```

### Contoh Asas Teras (01-06)

**Contoh 01: REST Chat Quickstart**
```powershell
# Start Foundry Local service
foundry model run phi-4-mini

# Run REST chat demo
python samples/01/chat_quickstart.py
```

**Contoh 02: Integrasi OpenAI SDK**
```powershell
# Ensure model is running
foundry status

# Run SDK demo
python samples/02/sdk_quickstart.py
```

**Contoh 03: Penemuan & Penanda Aras Model**
```powershell
# Run comprehensive model testing
samples/03/list_and_bench.cmd

# Or run individual components
foundry model list --available
foundry model download qwen2.5-0.5b
foundry model benchmark phi-4-mini
```

**Contoh 04: Aplikasi Chainlit RAG**
```powershell
# Install Chainlit dependencies
pip install chainlit langchain chromadb

# Start RAG chat application
chainlit run samples/04/app.py -w
# Opens browser at http://localhost:8000
```

**Contoh 05: Orkestrasi Multi-Agen**
```powershell
# Run agent coordinator demo
python -m samples.05.agents.coordinator

# Run specific agent examples
python samples/05/examples/specialists_demo.py
```

**Contoh 06: Router Model-as-Tools**
```powershell
# Configure environment
set BASE_URL=http://localhost:8000
set GENERAL_MODEL=phi-4-mini
set CODE_MODEL=qwen2.5-7b

# Run intelligent router
python samples/06/router.py "Analyze this Python code for performance issues"
```

### Contoh Integrasi Lanjutan (07-10)

**Contoh 07: Klien API Langsung**
```powershell
# Navigate to sample directory
cd samples/07

# Install additional dependencies
pip install -r requirements.txt

# Run basic API examples
python examples/basic_usage.py

# Try streaming responses
python examples/streaming.py

# Test production patterns
python examples/production.py
```

**Contoh 08: Aplikasi Chat Windows 11**
```powershell
# Navigate to sample directory
cd samples/08

# Install Node.js dependencies
npm install

# Start Electron application
npm start

# Or build for production
npm run build
```

**Contoh 09: Sistem Multi-Agen Lanjutan**
```powershell
# Navigate to sample directory
cd samples/09

# Install agent system dependencies
pip install -r requirements.txt

# Run basic coordination example
python examples/basic_coordination.py

# Try complex workflow
python examples/complex_workflow.py

# Interactive agent demo
python examples/interactive_demo.py
```

**Contoh 10: Kerangka Alat Foundry**
```powershell
# Navigate to sample directory
cd samples/10

# Install framework dependencies
pip install -r requirements.txt

# Run basic tools demo
python examples/basic_tools.py

# Start REST API server
python examples/rest_api_server.py
# API available at http://localhost:8080

# Try CLI application
python examples/cli_application.py --help

# Launch Jupyter notebook
jupyter notebook examples/jupyter_notebook.ipynb

# Test LangChain integration
python examples/langchain_demo.py
```

### Penyelesaian Masalah Isu Biasa

**Ralat Sambungan Foundry Local**
```powershell
# Check service status
foundry status

# Restart if needed
foundry restart

# Verify endpoint accessibility
curl http://localhost:5273/v1/models
```

**Isu Pemuatan Model**
```powershell
# Check available models
foundry model list --cached

# Download missing models
foundry model download phi-4-mini
foundry model download qwen2.5-0.5b

# Force reload if needed
foundry model unload --all
foundry model run phi-4-mini
```

**Isu Kebergantungan**
```powershell
# Upgrade pip and reinstall
python -m pip install --upgrade pip
pip install -r requirements.txt --force-reinstall

# For Node.js samples
npm cache clean --force
npm install
```

## Ringkasan
Modul ini mewakili kemajuan terkini dalam pembangunan AI tepi, menggabungkan alat Microsoft yang bertaraf perusahaan dengan fleksibiliti dan inovasi ekosistem sumber terbuka. Dengan menguasai Foundry Local melalui kesemua 10 sampel yang komprehensif, anda akan berada di barisan hadapan dalam pembangunan aplikasi AI.

**Laluan Pembelajaran Lengkap:**
- **Asas** (Sampel 01-03): Integrasi API dan pengurusan model
- **Aplikasi** (Sampel 04-06): RAG, agen, dan penghalaan pintar
- **Lanjutan** (Sampel 07-10): Kerangka kerja pengeluaran dan integrasi perusahaan

Untuk integrasi Azure OpenAI (Sesi 2), sila rujuk fail README sampel individu untuk pembolehubah persekitaran yang diperlukan dan tetapan versi API.

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk memastikan ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat yang kritikal, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
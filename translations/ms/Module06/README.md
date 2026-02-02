# Bab 06: Sistem Agen SLM: Gambaran Menyeluruh

Landskap kecerdasan buatan sedang mengalami transformasi asas apabila kita beralih daripada chatbot sederhana kepada agen AI canggih yang dikuasakan oleh Small Language Models (SLMs). Panduan menyeluruh ini meneroka tiga aspek kritikal sistem agen SLM moden: konsep asas dan strategi pelaksanaan, keupayaan pemanggilan fungsi, dan integrasi revolusioner Model Context Protocol (MCP).

## [Bahagian 1: Asas Agen AI dan Small Language Models](./01.IntroduceAgent.md)

Bahagian pertama menetapkan pemahaman asas tentang agen AI dan Small Language Models, memposisikan tahun 2025 sebagai era agen AI selepas era chatbot pada tahun 2023 dan ledakan copilot pada tahun 2024. Bahagian ini memperkenalkan **sistem AI agen** yang berfikir, membuat keputusan, merancang, menggunakan alat, dan melaksanakan tugas dengan input manusia yang minimum.

### Konsep Utama yang Dibincangkan:
- **Kerangka Pengelasan Agen**: Daripada agen refleks sederhana kepada agen pembelajaran, menyediakan taksonomi menyeluruh untuk pelbagai senario pengkomputeran
- **Asas SLM**: Mendefinisikan Small Language Models sebagai model dengan kurang daripada 10 bilion parameter yang boleh melakukan inferens praktikal pada peranti pengguna
- **Strategi Pengoptimuman Lanjutan**: Meliputi pelaksanaan format GGUF, teknik kuantisasi (Q4_K_M, Q5_K_S, Q8_0), dan kerangka yang dioptimumkan untuk edge seperti Llama.cpp dan Apple MLX
- **Perbandingan SLM vs LLM**: Menunjukkan pengurangan kos sebanyak 10-30× dengan SLM sambil mengekalkan keberkesanan untuk 70-80% tugas agen biasa

Bahagian ini diakhiri dengan strategi pelaksanaan praktikal menggunakan Ollama, VLLM, dan penyelesaian edge Microsoft, menetapkan SLM sebagai masa depan pelaksanaan AI agen yang menjimatkan kos dan melindungi privasi.

## [Bahagian 2: Pemanggilan Fungsi dalam Small Language Models](./02.FunctionCalling.md)

Bahagian kedua mendalami **keupayaan pemanggilan fungsi**, mekanisme yang mengubah model bahasa statik menjadi agen AI dinamik yang mampu berinteraksi dengan dunia nyata. Penjelasan teknikal ini merangkumi aliran kerja lengkap daripada pengesanan niat kepada integrasi respons.

### Kawasan Pelaksanaan Teras:
- **Aliran Kerja Sistematik**: Penjelasan terperinci tentang integrasi alat, definisi fungsi, pengesanan niat, penjanaan output JSON, dan pelaksanaan luaran
- **Pelaksanaan Khusus Platform**: Panduan menyeluruh untuk Phi-4-mini dengan Ollama, pemanggilan fungsi Qwen3, dan integrasi Microsoft Foundry Local
- **Contoh Lanjutan**: Sistem kolaborasi multi-agen, pemilihan alat dinamik, dan corak integrasi perusahaan dengan pengendalian ralat yang menyeluruh
- **Pertimbangan Pengeluaran**: Had kadar, log audit, langkah keselamatan, dan strategi pengoptimuman prestasi

Bahagian ini menyediakan pemahaman teori dan corak pelaksanaan praktikal, membolehkan pembangun membina sistem pemanggilan fungsi yang kukuh yang boleh menangani segala-galanya daripada panggilan API sederhana kepada aliran kerja perusahaan berbilang langkah yang kompleks.

## [Bahagian 3: Integrasi Model Context Protocol (MCP)](./03.IntroduceMCP.md)

Bahagian terakhir memperkenalkan **Model Context Protocol (MCP)**, kerangka revolusioner yang menyeragamkan cara model bahasa berinteraksi dengan alat dan sistem luaran. Bahagian ini menunjukkan bagaimana MCP mencipta jambatan antara model AI dan dunia nyata melalui protokol yang ditakrifkan dengan baik.

### Sorotan Integrasi:
- **Arkitektur Protokol**: Reka bentuk sistem berlapis yang merangkumi lapisan aplikasi, klien LLM, klien MCP, dan pemprosesan alat
- **Sokongan Multi-Backend**: Pelaksanaan fleksibel yang menyokong kedua-dua Ollama (pembangunan tempatan) dan vLLM (pengeluaran)
- **Protokol Sambungan**: Mod STDIO untuk komunikasi proses langsung dan mod SSE untuk penstriman berasaskan HTTP
- **Aplikasi Dunia Nyata**: Automasi web, pemprosesan data, dan contoh integrasi API dengan pengendalian ralat yang menyeluruh

Integrasi MCP menunjukkan bagaimana SLM boleh ditingkatkan dengan keupayaan luaran, mengimbangi jumlah parameter yang lebih kecil melalui fungsi yang dipertingkatkan sambil mengekalkan manfaat pelaksanaan tempatan dan kecekapan sumber.

## Implikasi Strategik

Secara keseluruhan, ketiga-tiga bahagian ini membentangkan kerangka menyeluruh untuk memahami dan melaksanakan sistem agen SLM. Evolusi daripada konsep asas melalui pemanggilan fungsi kepada integrasi MCP menunjukkan jalan yang jelas ke arah pelaksanaan AI yang didemokrasikan di mana:

- **Kecekapan bertemu keupayaan** melalui model kecil yang dioptimumkan
- **Keberkesanan kos** membolehkan penerapan yang meluas
- **Protokol yang diseragamkan** memastikan interoperabiliti
- **Pelaksanaan tempatan** melindungi privasi dan mengurangkan latensi

Perkembangan ini bukan sahaja mewakili kemajuan teknologi tetapi juga perubahan paradigma ke arah sistem AI yang lebih mudah diakses, cekap, dan praktikal yang boleh beroperasi dengan berkesan dalam persekitaran yang terhad sumber sambil memberikan keupayaan agen yang canggih.

Gabungan SLM dengan strategi pelaksanaan lanjutan, pemanggilan fungsi yang kukuh, dan protokol integrasi alat yang diseragamkan meletakkan sistem ini sebagai asas untuk generasi seterusnya agen AI yang akan mengubah cara kita berinteraksi dengan dan mendapat manfaat daripada kecerdasan buatan di seluruh industri dan aplikasi.

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk memastikan ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat yang kritikal, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
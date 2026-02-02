# WebGPU + ONNX Runtime Demo

Tato ukázka ukazuje, jak spouštět AI modely přímo v prohlížeči pomocí WebGPU pro hardwarovou akceleraci a ONNX Runtime Web.

## Co Tato Ukázka Demonstruje

- **AI v prohlížeči**: Spouštění modelů přímo v prohlížeči
- **Akcelerace pomocí WebGPU**: Hardwarově akcelerované zpracování, pokud je dostupné
- **Ochrana soukromí**: Žádná data neopouští vaše zařízení
- **Bez instalace**: Funguje v jakémkoli kompatibilním prohlížeči
- **Plynulý přechod**: Automaticky přechází na CPU, pokud WebGPU není dostupné

## Požadavky

**Kompatibilita prohlížeče:**
- Chrome/Edge 113+ s povoleným WebGPU
- Zkontrolujte stav WebGPU: `chrome://gpu`
- Povolení WebGPU: `chrome://flags/#enable-unsafe-webgpu`

## Spuštění Ukázky

### Možnost 1: Lokální server (doporučeno)

```cmd
# Navigate to the demo directory
cd Module08\samples\04\webgpu-demo

# Start a local server
python -m http.server 5173

# Open browser to http://localhost:5173
```

### Možnost 2: VS Code Live Server

1. Nainstalujte rozšíření "Live Server" ve VS Code
2. Klikněte pravým tlačítkem na `index.html` → "Open with Live Server"
3. Ukázka se automaticky otevře v prohlížeči

## Co Uvidíte

1. **Detekce WebGPU**: Kontrola kompatibility prohlížeče
2. **Načítání modelu**: Stažení a inicializace klasifikátoru MNIST
3. **Spuštění inference**: Predikce na vzorových datech
4. **Výkonové metriky**: Zobrazení času načítání a rychlosti inference
5. **Zobrazení výsledků**: Predikční jistota a surové výstupy

## Očekávaný Výkon

| Poskytovatel výpočtů | Načítání modelu | Inference | Poznámky |
|----------------------|-----------------|-----------|----------|
| **WebGPU**           | ~2-5s          | ~10-50ms  | Hardwarově akcelerováno |
| **CPU (WASM)**       | ~2-5s          | ~50-200ms | Softwarová záloha |

## Řešení Problémů

**WebGPU není dostupné:**
- Aktualizujte na Chrome/Edge 113+
- Povolení WebGPU v `chrome://flags`
- Zkontrolujte aktuálnost ovladačů GPU
- Ukázka automaticky přejde na CPU

**Chyby při načítání:**
- Ujistěte se, že používáte HTTP (ne file://)
- Zkontrolujte síťové připojení pro stažení modelu
- Ověřte, že CORS neblokuje ONNX model

**Problémy s výkonem:**
- WebGPU poskytuje výrazné zrychlení oproti CPU
- První spuštění může být pomalejší kvůli stahování modelu
- Další spuštění využívají cache prohlížeče

## Integrace s Foundry Local

Tato ukázka WebGPU doplňuje Foundry Local tím, že ukazuje:

- **Inference na straně klienta** pro maximální ochranu soukromí
- **Offline schopnosti** při nedostupnosti internetu  
- **Nasazení na okraji sítě** pro prostředí s omezenými zdroji
- **Hybridní architektury** kombinující lokální a serverovou inference

Pro produkční aplikace zvažte:
- Použití Foundry Local pro inference na straně serveru
- Použití WebGPU pro předzpracování/postprocessing na straně klienta
- Implementaci inteligentního směrování mezi lokální a vzdálenou inference

## Technické Detaily

**Použitý model:**
- Klasifikátor číslic MNIST (formát ONNX)
- Vstup: 28x28 obrázky v odstínech šedi
- Výstup: Pravděpodobnostní rozdělení pro 10 tříd
- Velikost: ~500KB (rychlé stažení)

**ONNX Runtime Web:**
- Poskytovatel výpočtů WebGPU pro akceleraci na GPU
- Poskytovatel výpočtů WASM pro zálohu na CPU
- Automatická optimalizace a optimalizace grafu

**API prohlížeče:**
- WebGPU pro přístup k hardwaru
- Web Workers pro zpracování na pozadí (budoucí rozšíření)
- WebAssembly pro efektivní výpočty

## Další Kroky

- Vyzkoušejte vlastní ONNX modely
- Implementujte nahrávání skutečných obrázků a klasifikaci
- Přidejte streamovací inference pro větší modely
- Integrujte vstup z kamery/mikrofonu

---


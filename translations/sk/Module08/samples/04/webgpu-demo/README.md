# WebGPU + ONNX Runtime Demo

Toto demo ukazuje, ako spustiť AI modely priamo v prehliadači pomocou WebGPU na hardvérové zrýchlenie a ONNX Runtime Web.

## Čo Toto Demonštruje

- **AI v prehliadači**: Spúšťanie modelov výhradne v prehliadači
- **Zrýchlenie pomocou WebGPU**: Hardvérové zrýchlenie, ak je dostupné
- **Ochrana súkromia**: Žiadne dáta neopúšťajú vaše zariadenie
- **Bez inštalácie**: Funguje v akomkoľvek kompatibilnom prehliadači
- **Plynulý prechod**: Automatický prechod na CPU, ak WebGPU nie je dostupné

## Požiadavky

**Kompatibilita prehliadača:**
- Chrome/Edge 113+ s povoleným WebGPU
- Skontrolujte stav WebGPU: `chrome://gpu`
- Povolenie WebGPU: `chrome://flags/#enable-unsafe-webgpu`

## Spustenie Dema

### Možnosť 1: Lokálny server (Odporúčané)

```cmd
# Navigate to the demo directory
cd Module08\samples\04\webgpu-demo

# Start a local server
python -m http.server 5173

# Open browser to http://localhost:5173
```

### Možnosť 2: Live Server vo VS Code

1. Nainštalujte rozšírenie "Live Server" vo VS Code
2. Kliknite pravým tlačidlom na `index.html` → "Open with Live Server"
3. Demo sa automaticky otvorí v prehliadači

## Čo Uvidíte

1. **Detekcia WebGPU**: Kontrola kompatibility prehliadača
2. **Načítanie modelu**: Stiahnutie a inicializácia klasifikátora MNIST
3. **Spustenie inferencie**: Predikcia na vzorových dátach
4. **Výkonnostné metriky**: Zobrazenie času načítania a rýchlosti inferencie
5. **Zobrazenie výsledkov**: Predikčná dôvera a surové výstupy

## Očakávaný Výkon

| Poskytovateľ inferencie | Načítanie modelu | Inferencia | Poznámky |
|-------------------------|------------------|------------|----------|
| **WebGPU** | ~2-5s | ~10-50ms | Hardvérové zrýchlenie |
| **CPU (WASM)** | ~2-5s | ~50-200ms | Softvérový fallback |

## Riešenie Problémov

**WebGPU Nie je Dostupné:**
- Aktualizujte na Chrome/Edge 113+
- Povolenie WebGPU v `chrome://flags`
- Skontrolujte aktuálnosť ovládačov GPU
- Demo automaticky prejde na CPU

**Chyby pri Načítaní:**
- Uistite sa, že používate HTTP (nie file://)
- Skontrolujte sieťové pripojenie na stiahnutie modelu
- Overte, že CORS neblokuje ONNX model

**Problémy s Výkonom:**
- WebGPU poskytuje výrazné zrýchlenie oproti CPU
- Prvé spustenie môže byť pomalšie kvôli stiahnutiu modelu
- Následné spustenia využívajú cache prehliadača

## Integrácia s Foundry Local

Toto demo WebGPU dopĺňa Foundry Local tým, že ukazuje:

- **Inferenciu na strane klienta** pre maximálnu ochranu súkromia
- **Offline schopnosti** pri nedostupnosti internetu  
- **Nasadenie na okraji siete** pre prostredia s obmedzenými zdrojmi
- **Hybridné architektúry** kombinujúce lokálnu a serverovú inferenciu

Pre produkčné aplikácie zvážte:
- Použitie Foundry Local na inferenciu na strane servera
- Použitie WebGPU na predspracovanie/postspracovanie na strane klienta
- Implementáciu inteligentného smerovania medzi lokálnou a vzdialenou inferenciou

## Technické Detaily

**Použitý Model:**
- Klasifikátor číslic MNIST (formát ONNX)
- Vstup: 28x28 obrázky v odtieňoch šedej
- Výstup: Pravdepodobnostná distribúcia pre 10 tried
- Veľkosť: ~500KB (rýchle stiahnutie)

**ONNX Runtime Web:**
- Poskytovateľ inferencie WebGPU pre GPU zrýchlenie
- Poskytovateľ inferencie WASM pre CPU fallback
- Automatická optimalizácia a optimalizácia grafu

**API Prehliadača:**
- WebGPU pre prístup k hardvéru
- Web Workers pre spracovanie na pozadí (budúce vylepšenie)
- WebAssembly pre efektívne výpočty

## Ďalšie Kroky

- Vyskúšajte vlastné ONNX modely
- Implementujte nahrávanie reálnych obrázkov a klasifikáciu
- Pridajte streamovaciu inferenciu pre väčšie modely
- Integrujte vstup z kamery/mikrofónu

---


# WebGPU + ONNX Runtime Demo

Dieses Demo zeigt, wie KI-Modelle direkt im Browser mit WebGPU für Hardware-Beschleunigung und ONNX Runtime Web ausgeführt werden können.

## Was Dieses Demonstriert

- **Browser-basierte KI**: Modelle vollständig im Browser ausführen
- **WebGPU-Beschleunigung**: Hardware-beschleunigte Inferenz, wenn verfügbar
- **Datenschutzfreundlich**: Keine Daten verlassen Ihr Gerät
- **Keine Installation**: Funktioniert in jedem kompatiblen Browser
- **Sanfter Rückfall**: Fällt auf die CPU zurück, wenn WebGPU nicht verfügbar ist

## Anforderungen

**Browser-Kompatibilität:**
- Chrome/Edge 113+ mit aktiviertem WebGPU
- WebGPU-Status prüfen: `chrome://gpu`
- WebGPU aktivieren: `chrome://flags/#enable-unsafe-webgpu`

## Demo Ausführen

### Option 1: Lokaler Server (Empfohlen)

```cmd
# Navigate to the demo directory
cd Module08\samples\04\webgpu-demo

# Start a local server
python -m http.server 5173

# Open browser to http://localhost:5173
```

### Option 2: VS Code Live Server

1. Installieren Sie die "Live Server"-Erweiterung in VS Code
2. Rechtsklick auf `index.html` → "Open with Live Server"
3. Das Demo öffnet sich automatisch im Browser

## Was Sie Sehen Werden

1. **WebGPU-Erkennung**: Überprüft die Browser-Kompatibilität
2. **Modell-Laden**: Lädt und initialisiert den MNIST-Klassifikator
3. **Inferenz-Ausführung**: Führt Vorhersagen auf Beispieldaten aus
4. **Leistungsmetriken**: Zeigt Ladezeit und Inferenzgeschwindigkeit
5. **Ergebnisanzeige**: Vorhersagewahrscheinlichkeit und Rohdaten

## Erwartete Leistung

| Ausführungsanbieter | Modell-Laden | Inferenz | Hinweise |
|---------------------|--------------|----------|----------|
| **WebGPU**          | ~2-5s        | ~10-50ms | Hardware-beschleunigt |
| **CPU (WASM)**      | ~2-5s        | ~50-200ms | Software-Rückfall |

## Fehlerbehebung

**WebGPU Nicht Verfügbar:**
- Aktualisieren Sie auf Chrome/Edge 113+
- Aktivieren Sie WebGPU in `chrome://flags`
- Überprüfen Sie, ob Ihre GPU-Treiber aktuell sind
- Das Demo fällt automatisch auf die CPU zurück

**Ladefehler:**
- Stellen Sie sicher, dass Sie über HTTP (nicht file://) bereitstellen
- Überprüfen Sie die Netzwerkverbindung für den Modell-Download
- Vergewissern Sie sich, dass CORS das ONNX-Modell nicht blockiert

**Leistungsprobleme:**
- WebGPU bietet eine erhebliche Geschwindigkeitssteigerung gegenüber der CPU
- Der erste Durchlauf kann langsamer sein, da das Modell heruntergeladen wird
- Nachfolgende Durchläufe nutzen den Browser-Cache

## Integration mit Foundry Local

Dieses WebGPU-Demo ergänzt Foundry Local und zeigt:

- **Client-seitige Inferenz** für maximalen Datenschutz
- **Offline-Fähigkeiten**, wenn keine Internetverbindung verfügbar ist  
- **Edge-Bereitstellung** für ressourcenbeschränkte Umgebungen
- **Hybride Architekturen**, die lokale und serverseitige Inferenz kombinieren

Für Produktionsanwendungen sollten Sie Folgendes in Betracht ziehen:
- Verwenden Sie Foundry Local für serverseitige Inferenz
- Nutzen Sie WebGPU für clientseitige Vor- und Nachverarbeitung
- Implementieren Sie intelligentes Routing zwischen lokaler und remote Inferenz

## Technische Details

**Verwendetes Modell:**
- MNIST-Ziffernklassifikator (ONNX-Format)
- Eingabe: 28x28 Graustufenbilder
- Ausgabe: 10-Klassen-Wahrscheinlichkeitsverteilung
- Größe: ~500KB (schneller Download)

**ONNX Runtime Web:**
- WebGPU-Ausführungsanbieter für GPU-Beschleunigung
- WASM-Ausführungsanbieter für CPU-Rückfall
- Automatische Optimierung und Graph-Optimierung

**Browser-APIs:**
- WebGPU für Hardware-Zugriff
- Web Workers für Hintergrundverarbeitung (zukünftige Erweiterung)
- WebAssembly für effiziente Berechnungen

## Nächste Schritte

- Testen Sie mit benutzerdefinierten ONNX-Modellen
- Implementieren Sie echten Bild-Upload und Klassifikation
- Fügen Sie Streaming-Inferenz für größere Modelle hinzu
- Integrieren Sie Kamera-/Mikrofoneingaben

---


# Foundry Local auf Windows & Mac

Diese Anleitung hilft Ihnen, Microsoft Foundry Local auf Windows und Mac zu installieren, auszuführen und zu integrieren. Alle Schritte und Befehle wurden anhand der Microsoft Learn-Dokumentation validiert.

- Erste Schritte: https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started
- Architektur: https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture
- CLI-Referenz: https://learn.microsoft.com/azure/ai-foundry/foundry-local/reference/reference-cli
- SDKs integrieren: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks
- HF-Modelle kompilieren (BYOM): https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models
- Windows AI: Lokal vs. Cloud: https://learn.microsoft.com/windows/ai/cloud-ai#key-decision-factors-for-app-developers

## 1) Installation / Upgrade auf Windows

- Installation:
```cmd
winget install Microsoft.FoundryLocal
```
- Upgrade:
```cmd
winget upgrade --id Microsoft.FoundryLocal
```
- Versionsprüfung:
```cmd
foundry --version
```
     
**Installation / Mac**

**MacOS**: 
Öffnen Sie ein Terminal und führen Sie den folgenden Befehl aus:
```bash
   brew tap microsoft/foundrylocal
   brew install foundrylocal
```

## 2) CLI-Grundlagen (Drei Kategorien)

- Modell:
```cmd
foundry model --help
foundry model list
foundry model run gpt-oss-20b
```
- Service:
```cmd
foundry service --help
foundry service status
foundry service ps
```
- Cache:
```cmd
foundry cache --help
foundry cache list
```

Hinweise:
- Der Service stellt eine OpenAI-kompatible REST-API bereit. Der Endpunkt-Port wird dynamisch zugewiesen; verwenden Sie `foundry service status`, um ihn zu ermitteln.
- Nutzen Sie die SDKs für mehr Komfort; sie übernehmen die Endpunkt-Erkennung automatisch, wo unterstützt.

## 3) Lokalen Endpunkt entdecken (Dynamischer Port)

Foundry Local weist bei jedem Start des Services einen dynamischen Port zu:
```cmd
foundry service status
```
Verwenden Sie die gemeldete URL `http://localhost:<PORT>` als Ihre `base_url` mit OpenAI-kompatiblen Pfaden (zum Beispiel `/v1/chat/completions`).

## 4) Schneller Test über OpenAI Python SDK

```cmd
set BASE_URL=http://localhost:PORT
python - <<PY
from openai import OpenAI
client = OpenAI(base_url="%BASE_URL%/v1", api_key="")
resp = client.chat.completions.create(
    model="gpt-oss-20b",
    messages=[{"role":"user","content":"Say hello from Foundry Local."}],
    max_tokens=64,
)
print(resp.choices[0].message.content)
PY
```
Referenzen:
- SDK-Integration: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks

## 5) Eigenes Modell bereitstellen (Mit Olive kompilieren)

Falls Sie ein Modell benötigen, das nicht im Katalog enthalten ist, können Sie es mit Olive zu ONNX für Foundry Local kompilieren.

Ablauf auf hoher Ebene (siehe Dokumentation für Schritte):
```cmd
foundry cache cd models
foundry cache list
foundry model run llama-3.2 --verbose
```
Dokumentation:
- BYOM-Kompilierung: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models

## 6) Fehlerbehebung

- Service-Status und Logs prüfen:
```cmd
foundry service status
foundry service diag
```
- Cache leeren oder verschieben:
```cmd
foundry cache list
foundry cache remove <model>
foundry cache cd <path>
```
- Auf die neueste Vorschau aktualisieren:
```cmd
winget upgrade --id Microsoft.FoundryLocal
```

## 7) Verwandte Windows-Entwicklererfahrung

- Windows lokal vs. Cloud-AI-Optionen, einschließlich Foundry Local und Windows ML:
  https://learn.microsoft.com/windows/ai/cloud-ai#key-decision-factors-for-app-developers
- VS Code AI Toolkit mit Foundry Local (verwenden Sie `foundry service status`, um die Chat-Endpunkt-URL zu erhalten):
  https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture#key-components

[Weiterer Windows-Entwickler](./windowdeveloper.md)

---

**Haftungsausschluss**:  
Dieses Dokument wurde mithilfe des KI-Übersetzungsdienstes [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, weisen wir darauf hin, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Nutzung dieser Übersetzung entstehen.
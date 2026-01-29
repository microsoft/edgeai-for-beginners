# Podcast Application

En konsolapplikation för att generera podcastsmanus med hjälp av AI-agenter.

## Usage

```bash
python podcast_app.py
```

## Workflow

1. **Welcome** - Applikationen hälsar användaren välkommen
2. **Topic Input** - Användaren anger ett ämne för podcasten
3. **Search Agent** - Söker efter relevant information
4. **Generate Script Agent** - Skapar ett podcastsmanus
5. **Review** - Användaren granskar och godkänner/avvisar manuset
6. **Save** - Godkänt manus sparas till `podcast.md`

## Requirements

- Python 3.12+
- agent_framework
- Alla beroenden från 02.WorkflowDevUI

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Vi strävar efter noggrannhet, men var vänlig observera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör anses vara den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
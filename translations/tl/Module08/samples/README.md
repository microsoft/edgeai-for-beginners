# Module 08 Mga Halimbawa: Gabay sa Lokal na Pag-unlad ng Foundry

## Pangkalahatang-ideya

Ang komprehensibong koleksyong ito ay nagpapakita ng parehong **Foundry Local SDK** at **Shell Command** na mga pamamaraan para sa paggawa ng mga AI application na handa para sa produksyon. Bawat halimbawa ay nagtatampok ng iba't ibang aspeto ng edge AI development, mula sa simpleng REST integration hanggang sa advanced na multi-agent systems.

## Pamamaraan sa Pag-unlad: SDK vs Shell Commands

### Gamitin ang Foundry Local SDK Kapag:

- **Programmatic Control**: Kailangan mo ng ganap na kontrol sa lifecycle ng agent, evaluation, o deployment workflows
- **Custom Tooling**: Gumagawa ng automation sa paligid ng Foundry Local (CI/CD integration, multi-agent orchestration)
- **Fine-Grained Access**: Nangangailangan ng detalyadong metadata ng agent, versioning, o kontrol sa evaluation runner
- **Python Integration**: Gumagana sa Python-heavy na mga kapaligiran o nag-eembed ng Foundry logic sa mas malawak na mga application
- **Enterprise Workflows**: Nagpapatupad ng modular workflows at reproducible evaluation pipelines na nakaayon sa Microsoft reference architectures

### Gamitin ang Shell Commands Kapag:

- **Quick Testing**: Gumagawa ng mabilisang lokal na pagsusuri, manual na paglulunsad ng agent, o pag-verify ng setup
- **CLI Simplicity**: Kailangan ng simpleng CLI operations para sa pagsisimula/pagpapatigil ng mga agent, pag-check ng logs, o basic evaluations
- **Lightweight Automation**: Nag-susulat ng simpleng automation nang hindi nangangailangan ng buong SDK integration
- **Rapid Iteration**: Debugging at development cycles, lalo na sa mga constrained na kapaligiran o resource group-level deployments
- **Setup & Validation**: Paunang configuration ng kapaligiran at mabilisang mga verification task

## Mga Pinakamahusay na Kasanayan at Inirerekomendang Workflow

Batay sa lifecycle management ng agent, dependency tracking, at least-privilege reproducibility principles:

### Phase 1: Foundation & Setup
1. **Simulan gamit ang Shell Commands** para sa paunang setup at mabilisang validation
2. **I-verify ang Kapaligiran** gamit ang mga tool ng CLI at basic na model deployment
3. **Subukan ang Connectivity** gamit ang simpleng REST calls at health checks

### Phase 2: Development & Integration
1. **Lumipat sa SDK** para sa scalable, traceable workflows
2. **Ipatupad ang Programmatic Control** para sa masalimuot na interaksyon ng agent
3. **Gumawa ng Custom Tools** para sa mga community-ready templates at Azure OpenAI integration

### Phase 3: Production & Scale
1. **Hybrid Approach** na pinagsasama ang CLI para sa ops at SDK para sa application logic
2. **Enterprise Integration** gamit ang monitoring, logging, at deployment pipelines
3. **Community Contribution** sa pamamagitan ng reusable templates at pinakamahusay na kasanayan

---

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't sinisikap naming maging tumpak, mangyaring tandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa kanyang katutubong wika ang dapat ituring na opisyal na sanggunian. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na dulot ng paggamit ng pagsasaling ito.
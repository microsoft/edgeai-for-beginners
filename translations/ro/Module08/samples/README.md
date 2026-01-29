# Module 08 Exemple: Ghid de Dezvoltare Locală Foundry

## Prezentare Generală

Această colecție cuprinzătoare demonstrează atât abordările **Foundry Local SDK**, cât și **Shell Command** pentru construirea aplicațiilor AI pregătite pentru producție. Fiecare exemplu evidențiază diferite aspecte ale dezvoltării AI la margine, de la integrarea REST de bază până la sisteme avansate multi-agent.

## Abordare de Dezvoltare: SDK vs Comenzi Shell

### Folosește Foundry Local SDK Când:

- **Control Programatic**: Ai nevoie de control complet asupra ciclului de viață al agenților, evaluării sau fluxurilor de lucru de implementare
- **Instrumente Personalizate**: Construirea automatizării în jurul Foundry Local (integrare CI/CD, orchestrare multi-agent)
- **Acces Detaliat**: Necesitatea de metadate detaliate ale agenților, versiuni sau controlul runner-ului de evaluare
- **Integrare Python**: Lucrul în medii intens utilizate de Python sau integrarea logicii Foundry în aplicații mai ample
- **Fluxuri de Lucru Enterprise**: Implementarea fluxurilor de lucru modulare și a conductelor de evaluare reproductibile aliniate cu arhitecturile de referință Microsoft

### Folosește Comenzi Shell Când:

- **Testare Rapidă**: Realizarea testelor locale rapide, lansări manuale de agenți sau verificarea configurării
- **Simplitatea CLI**: Ai nevoie de operațiuni CLI simple pentru pornirea/opririrea agenților, verificarea jurnalelor sau evaluări de bază
- **Automatizare Ușoară**: Scriptarea unei automatizări simple fără cerințe de integrare completă a SDK-ului
- **Iterație Rapidă**: Debugging și cicluri de dezvoltare, mai ales în medii constrânse sau implementări la nivel de grup de resurse
- **Configurare și Validare**: Configurarea inițială a mediului și sarcini rapide de verificare

## Cele Mai Bune Practici & Flux de Lucru Recomandat

Bazat pe gestionarea ciclului de viață al agenților, urmărirea dependențelor și principiile de reproducibilitate cu privilegii minime:

### Faza 1: Fundament & Configurare
1. **Începe cu Comenzi Shell** pentru configurarea inițială și validarea rapidă
2. **Verifică Mediul** folosind instrumente CLI și implementarea de bază a modelului
3. **Testează Conectivitatea** cu apeluri REST simple și verificări de sănătate

### Faza 2: Dezvoltare & Integrare
1. **Treci la SDK** pentru fluxuri de lucru scalabile și trasabile
2. **Implementează Control Programatic** pentru interacțiuni complexe între agenți
3. **Construiește Instrumente Personalizate** pentru șabloane pregătite pentru comunitate și integrarea Azure OpenAI

### Faza 3: Producție & Scalare
1. **Abordare Hibridă** combinând CLI pentru operațiuni și SDK pentru logica aplicației
2. **Integrare Enterprise** cu monitorizare, jurnalizare și conducte de implementare
3. **Contribuție Comunitară** prin șabloane reutilizabile și cele mai bune practici

---

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să asigurăm acuratețea, vă rugăm să fiți conștienți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa natală ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.
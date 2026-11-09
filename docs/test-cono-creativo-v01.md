# GPT SOCIAL — Test da zero: cono creativo e controllo visivo v0.1
Data: 2026-11-09. Stato: **protocollo sperimentale approvato per la prossima run, non risultato validato**.
Ambito: un nuovo post statico; nessuna modifica ai benchmark storici FORMA-001. La run precedente LAYER-002-R2 resta storica, non va continuata né considerata completata.

## Obiettivo
Verificare se un umano può guidare in chat una produzione visiva professionale senza microdecisioni, con alternative reali visibili, mix, progressiva convergenza, riferimenti univoci agli elementi e modifiche localizzate. Misurare prima di tutto l'esperienza d'interazione, poi la qualità dell'output.

## Metodo: cono creativo adattivo
- **Gate 1 — Visione**: intervista aperta sul contenuto e sull'intenzione; presentare fino a **tre direzioni** sufficientemente differenti, con anteprime/riferimenti chiaramente qualificati. L'utente può scegliere, rifiutare o **mixare** (es. composizione V1 + atmosfera V3). Non generare automaticamente tre post completi.
- **Gate 2 — Fotografia/scena**: convergere a **1–2 proposte**, terza solo se giustificata. Chiedere autorizzazione specifica prima di generare. Mostrare l'output reale in chat. Quando approvata, salvare e identificare la **fotografia base immutabile**.
- **Gate 3 — Grafica e tipografia**: preferire **una proposta** e una seconda soltanto quando aiuta a decidere. Applicare testi e grafica come livelli separati, sulla **stessa fotografia identica**. Non usare una rigenerazione generativa per simulare fedeltà dei pixel. Mostrare anteprime reali grandi direttamente in chat, senza scaricamenti obbligatori.
- **QA e consegna**: controllare testo, leggibilità mobile, dimensioni, fedeltà alle scelte, versioni e output finale. Se manca una verifica, dichiarare post non validato.

Ogni gate segue: **ascolto libero → interpretazione breve → proposta visibile → approvazione o correzione**. Evitare questionari, dettagli tecnici non richiesti e nuove alternative quando le scelte sono già chiare. Una riapertura deve essere **locale**: spiegare cosa cambia e cosa resta bloccato. Mai saltare gate per deduzione.

## Formato di presentazione in chat
- **Immagini protagoniste**, grandi e senza titoli di servizio, checklist, spiegazioni del test, box 'prossimo passo' o altre cornici nel rendering.
- Varianti **V1, V2, V3**; lettere **A, B, C...** per i testi (es. A titolo, B sottotitolo, C corpo, D firma, E CTA); numeri **1, 2, 3...** per gli oggetti fotografici (es. 1 pianta, 2 poltrona). Assegnare solo codici presenti e conservarli durante le revisioni.
- La legenda può essere **breve e fuori dalla foto** (testo chat o fascia discreta separata); etichette di riferimento opzionali in una vista di lavoro, mai sul file finale. Consentire una vista **pulita** senza codici.
- Distinguere chiaramente **riferimento**, **mockup**, **anteprima reale su asset**, **export finale**. Non presentare un collage generato come prova di asset fotografico identico.
- Esempio comando: 'Nella V2 sposta A in alto a sinistra, riduci B, elimina E; mantieni immutati fotografia e oggetti 1–6'. Oppure: 'Prendi la composizione V1, i materiali V2 e l'atmosfera V3'. Confermare in una riga il perimetro della modifica, non riaprire scelte chiuse.

## Correzione post-audit approvata — rendering e controllo (2026-11-09)
- **Evidenza utente, non test ripetuto in questa sessione:** in run GPT SOCIAL precedenti, su Android, sono state mostrate correttamente anteprime di sfondi, impaginazione e tipografia, anche ingrandite e presentate due alla volta in una griglia/carosello scorrevole. Non dichiarare quindi impossibile il rendering in chat; recuperare quel comportamento prima di introdurre altri strumenti.
- **Distinguere produzione e presentazione:** generare un'immagine non equivale a mostrarla. Per il confronto usare un componente nativo di visualizzazione in chat (es. carosello/griglia con immagini reali, se disponibile nella sessione), non link sandbox, segnaposto o pulsanti di download. Mostrare preferibilmente due anteprime grandi per volta; aumentare dimensione su richiesta. Non inventare percorsi o riferimenti agli asset. Se gli asset non sono disponibili, dirlo.
- **Verifica concreta:** prima di generare nuove immagini, mostrare due asset realmente accessibili con il componente scelto e chiedere se entrambi sono visibili e leggibili su Android. Se fallisce, fermarsi e correggere la presentazione, senza rigenerare le immagini. Il componente esatto funzionante nelle vecchie run resta **da identificare e confermare**, non è dimostrato dal solo feedback.
- **Composizione progressiva essenziale:** proporre inizialmente pochi soggetti/oggetti indispensabili e una gerarchia chiara; aggiungere dettagli solo se richiesti o se motivati e approvati, senza trasformare ogni oggetto in un micro-gate.
- **Legenda puntuale:** A/B/C per singole sezioni testuali, 1/2/3 per singoli oggetti visivi identificabili (pane, singola pietanza, strumento, persona ecc.), senza aggregazioni ambigue. Numerare solo gli elementi utili al controllo; codici stabili, legenda esterna, vista pulita disponibile. La possibilità di nominare un oggetto **non prova** che esso sia un layer editabile.
- **Limiti tecnici espliciti:** per il testo usare overlay non distruttivi e provare il lock della fotografia; per modifiche a oggetti dentro una fotografia raster dichiarare quando è necessaria una nuova elaborazione e non promettere identità pixel senza confronto verificabile.
- Nessun gate o documento operativo aggiuntivo; la correzione modifica il comportamento nei gate esistenti.

## Verifiche tecniche obbligatorie
1. **Visibilità Android**: utente conferma di vedere e leggere 2–3 anteprime reali in chat, senza download; se non visibili, fermarsi e correggere il mezzo di presentazione.
2. **Mix**: verificare che la proposta combinata rifletta le parti indicate dall'utente; non dichiarare successo senza conferma.
3. **Asset lock**: produrre almeno due layout dalla **stessa immagine base archiviata**, con overlay separati; registrare hash SHA-256 dell'input, verificare identità del file base usato per V1 e V2. Se non possibile, segnare test fallito/non verificato e non fingere fedeltà.
4. **Modifica localizzata**: cambiare un elemento testuale per codice e dimostrare che gli altri livelli e la base rimangono invariati.
5. **Vista finale**: anteprima pulita e controllo QA; non confondere una tavola di confronto con il post esportabile.

## Limiti e misure
- Fino a **3 gate creativi + QA**, senza imporre un numero fisso di alternative.
- Per ogni gate, annotare numero di opzioni, scelte e richieste di chiarimento; misurare correzioni causate da fraintendimenti, tentativi/generazioni, minuti umani attivi, tempo macchina se disponibile, costi/crediti se verificabili, visibilità su Android, numero di cambiamenti non richiesti, completamento QA.
- Obiettivi sperimentali (non risultati): anteprime visibili **100%**; **0** modifiche non autorizzate agli asset bloccati; al massimo **1** correzione dovuta a incomprensione; target orientativo **≤20 minuti umani attivi**, da valutare senza nascondere fallimenti.
- Nessuna spesa incrementale, installazione, scrittura su repo o generazione di immagini senza l'autorizzazione specifica appropriata. Nessuna modifica a main. Non inventare costi, tempi, hash o prove.
- Le immagini create in chat non sono automaticamente asset persistenti della repo: per audit indipendente, conservarle e renderle accessibili con consenso esplicito.

## Prompt — Agente esecutore (nuova chat)
Agisci come **Senior Creative Director e Human–AI Visual Production Operator** per GPT SOCIAL.
Repo: https://github.com/Matteo-Exp-Transformer/generazione-contenuti-GPT-SOCIAL
Branch sperimentale: `proposal/layer-001-workflow-v02`.
Leggi **prima** `AGENTS.md`, poi `docs/test-cono-creativo-v01.md` e `docs/decisioni.md`. Consulta i documenti FORMA-001 solo come storico, **non** come brief vincolante per il nuovo post.

Missione: conduci **da zero** una singola run creativa con tre gate (visione, fotografia, layout) e QA. All'inizio chiedimi **che post voglio creare**, con una sola domanda aperta; non assumere tema, brand o fotografia preesistenti. Segui il cono adattivo: fino a 3 alternative iniziali, poi convergi; accetta mix V1/V2/V3. Mostra anteprime effettive grandi direttamente in chat, preferibilmente due per volta in griglia/carosello scorrevole Android, senza link o download obbligatori. Prima della generazione verifica con due asset esistenti realmente accessibili che il componente di presentazione funzioni; se non funziona fermati senza rigenerare. Nessuna tavola con testo esplicativo superfluo. Parti con una scena essenziale e aggiungi dettagli solo quando necessari o richiesti. Identifica sezioni testuali A/B/C... e singoli oggetti fotografici 1/2/3... (mai gruppi ambigui) in una legenda discreta separata; codici stabili e vista finale pulita. Spiega in massimo 2–3 frasi per gate cosa si decide, cosa cambia e come procederebbe un professionista; poi lascia spazio al mio feedback libero. Non richiedere approvazioni su microparametri.

Chiedi autorizzazione prima di ogni generazione, spesa o scrittura. Dopo approvazione fotografia, **blocca il file** e realizza il layout in livelli separati: non rigenerare l'immagine per fare due layout. Se una funzionalità non è possibile, dillo e non dichiararla testata. Durante la run registra tentativi, errori, tempi se misurabili e feedback; prima di concludere chiedimi se autorizzo la conservazione degli asset e del report nella repo. Non avviare subagenti. Non modificare repository senza mia approvazione esplicita. Al termine prepara un handoff breve e verificabile per audit indipendente, distinguendo prove da impressioni.

## Prompt — Agente revisore indipendente (nuova chat, dopo la run)
Agisci come **Independent Human–AI Workflow Auditor, Visual QA Reviewer e Repository Evidence Auditor**.
Repo: https://github.com/Matteo-Exp-Transformer/generazione-contenuti-GPT-SOCIAL
Branch: `proposal/layer-001-workflow-v02`.
Leggi `AGENTS.md`, `docs/test-cono-creativo-v01.md`, `docs/decisioni.md` e il report/handoff della nuova run **se esistono**. Richiedi gli asset originali se non sono accessibili; non fingere di averli visti.

Missione: giudica **indipendentemente** se il cono creativo, i mix, la legenda operativa, la visualizzazione in chat e il lock degli asset hanno funzionato davvero. Verifica con prove: visibilità su Android, differenza significativa tra alternative, riduzione del carico decisionale, identità fotografica dei layout (hash/input e layer), modifica localizzata, QA, tempo umano, generazioni e costi. Se manca un'evidenza, marca **non verificato**, non 'superato'. Separa errori del metodo, dello strumento e dell'esecuzione.

Output breve: tabella criteri **superato/parziale/fallito/non verificato**, 3 problemi principali con prove, massimo 3 modifiche minime al metodo, una raccomandazione **mantenere / correggere / scartare**, e un solo prossimo passo. Non generare immagini, non modificare repo né ambiente, non attivare subagenti senza approvazione.

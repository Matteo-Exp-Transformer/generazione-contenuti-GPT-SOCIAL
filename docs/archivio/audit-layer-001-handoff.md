# LAYER-001 — Handoff di audit del workflow conversazionale
Data: 2026-11-09
Stato: run interrotta intenzionalmente prima della generazione. Documento osservativo, NON nuovo protocollo approvato.

## Scopo
Fornire a un agente indipendente un resoconto della run FORMA / «La forma della luce» e dei feedback dell'utente. L'agente deve confrontarlo con repository, benchmark e decisioni canoniche, proporre modifiche MINIME e preparare una nuova run misurabile. Questo file non sostituisce PRD, brief o protocollo esistenti.

## Fatti osservati
- Esperimento: composizione social editoriale 4:5, 1080×1350, marchio FORMA, tema «La forma della luce».
- Approccio: costruzione incrementale con alternative, anteprime SVG e gate umani; nessuna fotografia generata e nessun file prodotto nella run.
- Sequenza di scelte provvisorie: E3 titolo monumentale; palette C avorio; P2 soggetto a destra; F2 foto con cornice avorio; S1 parete/ombra; S1A diagonale alto-destra; M1 parete frontale in intonaco; G2 frontale con profondità minima; L2 fascio medio decentrato; A2 titolo ridotto e soggetto protetto; T4 sans neo-grotesque; N1 Editorial Regular.
- Ultima fase: confronto di Neue Haas Grotesk, Helvetica Now Display, Inter, IBM Plex Sans; nessun font finale approvato.
- Problema precedente segnalato: benchmark B2 aveva coperto gran parte della foto con bianco e testo, alterando radicalmente il senso dell'immagine.
- Criticità emerse: troppe decisioni microscopiche e testi lunghi; guide geometriche non equivalenti a metriche font reali; alcuni mockup mostravano tensione fra zona titolo e zona soggetto; margine prima circa 54 px e poi riallineato a 68 px; font di fallback non riproducono fedelmente le famiglie candidate.

## Feedback esplicito dell'utente
«Molto meglio così la procedura, solo decisamente troppi passaggi, e troppo testo da leggere.»
A ogni passaggio vuole capire: (1) su cosa si lavora; (2) cosa cambia; (3) quando questa scelta viene applicata dai professionisti; (4) in base a cosa scegliere.
Vuole poche informazioni essenziali per l'umano e decisioni accorpate quando possibile.
Ha chiesto di concludere la run e documentarla per revisione di un agente che legga lavoro, repository e feedback.

## Ipotesi da sottoporre ad audit, NON decisioni approvate
1. Ridurre i gate a macrodecisioni: concept/obiettivo; composizione e rapporto foto-testo; direzione fotografica (soggetto, camera, luce, materiale nello stesso gate); tipografia e gerarchia nello stesso gate; review pre-generazione; produzione/test.
2. Ogni gate deve contenere massimo: «Stiamo decidendo», «Cosa cambia visivamente», «Quando lo decide un professionista», 2–3 opzioni con trade-off e raccomandazione, anteprime ampie, una scelta umana. Dettagli tecnici in sezione opzionale.
3. Non chiedere approvazioni per regolazioni tecniche minute finché non alterano la direzione creativa; mantenere reversibilità.
4. Separare concept, simulazione geometrica, fotografia generata e layout effettivamente misurato; evitare di promettere fedeltà del font o contrasto certificato nei mockup.
5. Trattare la fotografia come asset protagonista e mantenere aree protette: vietare pannelli coprenti non esplicitamente approvati.
6. Introdurre budget di interazione: conteggio gate, tempo umano, testo letto, varianti, costo di generazione, revisioni, qualità percepita e utilizzabilità.
7. Valutare se una prima prova a basso costo vada anticipata dopo pochi gate, per evitare over-design senza verifica visiva reale.

## Questioni aperte per l'auditor
- Quali decisioni della sequenza erano realmente indipendenti e quali potevano essere accorpate?
- Quale struttura di gate rispecchia il processo di un art director professionista, senza renderlo burocratico?
- Come distinguere decisioni creative dell'utente da parametri delegabili all'agente?
- Come validare zone protette, proporzioni e leggibilità con metriche reali nella fase appropriata?
- Quali criteri oggettivi e soggettivi usare per confrontare nuova run e LAYER-001?
- Quali file canonici esistono già, e dove integrare la correzione senza creare duplicati?

## Mandato minimo raccomandato
Leggere README, AGENTS.md se presente, PRD, decisioni, protocollo e risultati del benchmark, eventuali documenti LAYER-001. Distinguere fatti da inferenze; individuare max 5 cause radice; proporre il più piccolo diff documentale utile; definire una run comparativa con stop condition, budget e rubric; non modificare asset/generare immagini; aggiornare la repo soltanto dopo aver verificato coerenza con documenti canonici. Restituire un prompt operativo per la nuova run.

## Limiti delle evidenze
Il presente documento riassume la conversazione, non contiene screenshot o immagini finali e non dimostra la qualità del post concluso: il post non è stato generato. Nessun dato affidabile sui minuti spesi o token/costi effettivi è stato misurato. I nomi delle varianti sono etichette sperimentali, non uno standard di design.

# FORMA-001 — Guida alla sessione sperimentale e revisione

**Stato:** preparazione operativa. Benchmark non eseguito.
**Fonti canoniche:** [brief](brief.md), [protocollo](protocollo.md), [prompt A](prompts/A-post-completo.md), [prompt B1](prompts/B1-fotografia.md), [prompt B2](prompts/B2-layout.md), [risultati](risultati.md).
**Regola:** questo documento contiene solo istruzioni di sessione, checklist e prompt di avvio/audit. Non duplica brief, rubriche o risultati.

## Prima della sessione
- Aprire una nuova chat con accesso a GitHub e, se necessario, generazione immagini.
- Verificare lettura di AGENTS.md, README.md, docs/decisioni.md e file FORMA-001.
- Confermare modello, strumenti, disponibilità effettiva, limiti, licenze e costo incrementale. Nessun acquisto, API a pagamento o installazione.
- Ottenere autorizzazione esplicita per le generazioni; l'approvazione del piano non autorizza immagini né crediti.
- Definire un timer per preparazione, generazione, composizione e revisione. Non inventare tempi retroattivi.

## Checklist di esecuzione — gate
### G0 — Prontezza
- [ ] Fonti canoniche lette; stato GitHub verificato.
- [ ] Specifiche del brief comprese; formato finale 1080×1350, sRGB.
- [ ] Percorsi A e B e criteri del protocollo confermati.
- [ ] Strumenti, costi e disponibilità verificati; costo esterno incrementale massimo €0.
- [ ] Autorizzazione esplicita a generare raccolta.

### G1 — Candidato A
- [ ] Un solo primo candidato A, dal prompt canonico.
- [ ] Asset salvato/riferimento recuperabile; modello e impostazioni annotati.
- [ ] Testi confrontati lettera per lettera con brief; difetti visivi descritti.
- [ ] Tempo e tentativi annotati; nessun punteggio inventato.

### G2 — Fotografia B1
- [ ] Una sola fotografia iniziale dal prompt canonico.
- [ ] Assenza di scritte, loghi e persone verificata.
- [ ] Materiali, luce, prospettiva e zone utili al crop verificati.
- [ ] Approvazione umana dell'asset prima di B2.

### G3 — Layout B2
- [ ] Piano tecnico approvato prima di creare file o modificare ambiente.
- [ ] Testi esatti in livelli modificabili.
- [ ] Fotografia dominante asimmetrica e dettaglio materico.
- [ ] Sorgente riproducibile, PNG 1080×1350 sRGB; font e licenze documentati.
- [ ] Nessuna dipendenza non autorizzata.

### G4 — QA comparativo
- [ ] Visualizzazione a dimensione smartphone e comprensione in 3 secondi.
- [ ] Testi, ritagli, allineamenti, contrasti e difetti controllati.
- [ ] Stessa modifica al sottotitolo richiesta ad A e B; tempo e difficoltà misurati.
- [ ] Punteggi attribuiti secondo protocollo, con motivazioni ed evidenze.
- [ ] Confronto tempo totale, costo, numero tentativi, modificabilità e qualità.
- [ ] Verifica soglia 80/100 e assenza errori critici.

### G5 — Chiusura
- [ ] Aggiornare risultati.md solo con prove effettive, dopo autorizzazione alla scrittura.
- [ ] Separare osservazioni, valutazioni soggettive e ipotesi.
- [ ] Nessun cambiamento di PRD, prompt o processo senza decisione motivata.
- [ ] Lasciare un solo prossimo passo e un handoff breve se necessario.

**Limiti:** massimo 3 tentativi iniziali per percorso e 1 revisione per candidato; iniziare con 1 A + 1 B1, non consumare il plafond automaticamente. Se la capacità del tool non consente esportazione, sorgente modificabile o precisione richiesta, dichiarare il limite e chiedere come procedere.

## Prompt 1 — Avvio nuova chat sperimentale

Sei il responsabile di una sessione sperimentale FORMA-001 per GPT SOCIAL. Repository: https://github.com/Matteo-Exp-Transformer/generazione-contenuti-GPT-SOCIAL

Leggi AGENTS.md, README.md, docs/decisioni.md e tutti i file pertinenti di benchmarks/FORMA-001, inclusa questa guida. Non ricostruire il progetto da zero e non introdurre skill o infrastruttura.

Obiettivo: confrontare A (post intero generato) e B (fotografia generata + layout separato modificabile), con la stessa rubrica del protocollo. Procedi gate per gate G0–G5 e mostra a ogni gate: cosa è stato fatto, prova disponibile, difetti, prossima decisione umana. Parti da un solo candidato A e una sola fotografia B1; attendi approvazione della fotografia prima di B2.

Prima di generare, chiedimi autorizzazione esplicita, dopo aver verificato capacità e costi reali. Budget esterno incrementale €0; non acquistare crediti, non installare e non modificare l'ambiente senza consenso. Prima di scrivere sulla repo chiedi consenso specifico. Non dichiarare test eseguiti se non verificati. Annota tempi, tentativi, impostazioni e asset recuperabili; se non puoi misurarli, dichiaralo.

Concludi con il confronto verificabile e la proposta di aggiornamento a risultati.md. Quando il contesto si appesantisce, prepara un prompt di handoff con stato GitHub, asset, gate raggiunto, decisioni, problemi e prossimo passo. Non affermare di avere un contatore affidabile dei 100k token.

## Prompt 2 — Audit post-run in nuova chat

Agisci come revisore indipendente, senior editorial art director e workflow reliability auditor. Non produrre nuove immagini e non modificare nulla durante la prima fase.

Repository: https://github.com/Matteo-Exp-Transformer/generazione-contenuti-GPT-SOCIAL

Leggi AGENTS.md, il brief e protocollo FORMA-001, questa guida e risultati.md. Esamina i file e gli asset realmente prodotti dalla run; chiedimi link o caricamenti se mancano. Non attribuire punteggi sulla base di sole descrizioni o di un resoconto non verificabile.

Valuta distintamente:
1. Qualità editoriale, fotografia, composizione, tipografia, leggibilità mobile e fedeltà al brief.
2. Precisione dei testi e presenza di errori critici.
3. Tempo totale e costo reale per ottenere un post approvabile, non solo velocità di generazione.
4. Modificabilità e risultato della stessa revisione del sottotitolo su A e B.
5. Affidabilità del workflow: gate, tracciabilità, ripetibilità, punti di attrito, lavoro manuale.
6. Scelta A, B, ibrido o nessuno, con motivazioni ed evidenze.

Applica la rubrica /100 del protocollo solo ai risultati osservabili. Distingui difetti del modello, del prompt, dell'asset e del layout. Proponi massimo tre correzioni ad alto impatto e basso costo, senza proliferare skill, agenti o documenti. Discuti con me il risultato e proponi un solo benchmark successivo o una revisione mirata. Non cambiare repository senza autorizzazione.

## Handoff per limite di contesto
Non è disponibile una misura affidabile dei token consumati. Se la chat si avvicina a un limite pratico, consegnare: commit e file verificati; gate raggiunto; modelli e impostazioni; riferimenti agli asset; tentativi e tempi; costi; decisioni umane; QA svolto e mancante; problemi; prossima azione singola. Non duplicare tutto il brief.


## Prompt 3 — Prosecuzione orientata alla fattibilità (2026-11-09)

Mandato per una **nuova chat esecutrice**, non autorizzazione automatica a generare o modificare ambiente/repository:

> Agisci come Senior Editorial Production Engineer per GPT SOCIAL. Leggi AGENTS.md, README.md, docs/decisioni.md e tutti i documenti di benchmarks/FORMA-001 nella repository https://github.com/Matteo-Exp-Transformer/generazione-contenuti-GPT-SOCIAL. Parti dallo stato verificato in risultati.md: 2 candidati A, 1 fotografia B1, nessun layout B2, nessun tempo storico misurato, costi per immagine ChatGPT non disponibili. Recupera gli asset originali dalla chat precedente o chiedi di allegarli; non assumere che i riferimenti temporanei siano persistenti.
>
> **Priorità:** misurare se si riesce a produrre un post davvero utilizzabile, con quanti tentativi, minuti umani, attesa macchina, crediti/quote e spesa monetaria. Non perfezionare inutilmente la direzione artistica. Non inventare costi, tempi o capacità. Separare costo incrementale, quote incluse, costo del lavoro e costo imputato dell'abbonamento.
>
> Avvia una nuova run con ID e cronometro dichiarato prima di qualsiasi azione. Verifica gli strumenti disponibili e la disponibilità reale di quote, annotando ciò che non è esposto. Presenta un piano minimo per utilizzare B1 come asset e produrre B2 editabile (sorgente HTML/CSS/SVG o equivalente già disponibile, PNG 1080×1350 sRGB, testi letteralmente esatti, nessuna dipendenza nuova). **B1 non è ancora approvata:** chiedi esplicitamente approvazione di B1 e del piano tecnico prima di creare B2. Non creare file, generare immagini, installare, spendere crediti o modificare repository prima di autorizzazione specifica. Budget esterno incrementale €0.
>
> Dopo autorizzazione, realizza un solo B2 minimo ma usabile; misura e verifica l'output, poi proponi una singola modifica del sottotitolo da replicare sul percorso A, con misurazione separata di tempo, tentativi, effetti collaterali e costo. Non avviare generazioni aggiuntive senza consenso. Valuta il primo output approvabile, non solo l'estetica; se fallisce, registra perché. Compila la scheda per ogni tentativo prevista in protocollo.md. Presenta prove e bozza di aggiornamento a risultati.md, chiedendo autorizzazione prima di scrivere. Un solo prossimo passo e handoff breve se serve.
>
> Non introdurre subagent o nuovi file di processo per inerzia. In caso di capacità di delega non disponibili, lavora direttamente e dichiaralo.

**Nota:** questo prompt non cambia brief, rubrica, gate o autorizzazioni. Il prossimo test preferito è T3 (B2) dopo approvazione B1; T1/T2 rimangono nel backlog.


## Workflow creativo v0.2 — approvato per test LAYER-002 (2026-11-09)

L'utente ha approvato questa interfaccia per una run sperimentale LAYER-002. Non sostituisce il protocollo A/B G0–G5 né autorizza generazioni o modifiche all'ambiente. Fonte osservativa: docs/audit-layer-001-handoff.md.

**Diagnosi:** 12 scelte provvisorie nella run LAYER-001 prima di qualsiasi fotografia; troppe microdecisioni e spiegazioni. Il benchmark precedente ha inoltre evidenziato il rischio di coprire la fotografia con pannelli e testo. Le misure di tempo/costo della run LAYER-001 non sono disponibili.

**Tre gate creativi + verifica:**
1. **Direzione:** messaggio, atmosfera, rapporto immagine/testo; approvazione umana.
2. **Composizione + fotografia:** soggetto, posizione, sfondo, camera, luce, materiali e aree protette in un'unica scelta fra 2–3 proposte; approvazione umana. Sul percorso B, chiedere qui autorizzazione separata per UNA prima generazione fotografica, prima della tipografia di dettaglio.
3. **Tipografia + layout:** gerarchia, stile e collocazione del testo in 2–3 alternative basate sull'asset effettivo; approvazione umana. L'agente sceglie metriche, spaziature e allineamenti tecnici, verificandoli sul rendering finale.
4. **Verifica:** output reale, controllo su smartphone, correzione mirata, decisione di accettazione. Ogni generazione, creazione file o modifica dell'ambiente richiede la specifica autorizzazione prevista dalle regole vigenti.

**Template di risposta (max 120 parole prima delle anteprime):**
- **Decidiamo:** [una macrodecisione].
- **Cambia:** [effetto concreto nell'immagine].
- **Perché ora:** [quando/come decide un professionista, una frase].
- **Opzioni:** A/B, massimo C, differenze visibili e un compromesso ciascuna; anteprime comparabili se disponibili e fedeltà dichiarata (schema ≠ fotografia/render reale).
- **Consiglio:** [una proposta motivata]. **Scegli:** A/B/C, modifica o torna al gate precedente.

**Delegare:** margini numerici, gutter, micro-crop, scelta fra font equivalenti compatibili con licenze, kerning, contrasto e QA tecnico; chiedere all'umano solo se cambia la direzione creativa, oscura il soggetto o viola il brief. Nessun pannello opaco sopra la fotografia senza approvazione esplicita.

**Metriche della prossima run:** numero gate creativi (target ≤3), decisioni esplicite (≤3 prima della prima prova), parole mostrate per gate (≤120 escluse etichette anteprima), tentativi di generazione, minuti umani attivi, minuti macchina, costo incrementale verificato, revisite ai gate, errori critici, punteggio /100 secondo protocollo, output approvabile sì/no. Confrontare con LAYER-001 solo metriche osservabili: 12 scelte e nessuna fotografia generata; tempi e qualità finale non confrontabili. Fermarsi se dopo 3 gate non esiste una direzione approvata, se la prova viola aree protette o se occorre spesa/azione non autorizzata.

**Compatibilità:** i tre gate sono l'interfaccia creativa sperimentale approvata; G0–G5 del protocollo restano i gate sperimentali canonici. Non cambiare prompt A/B o risultati storici senza un audit della run e ulteriore approvazione.


## LAYER-002 — feedback in corso e restart R2 (2026-11-09)

**Stato:** l'utente ha approvato la direzione fotografica A e poi l'opzione compositiva B (interno vissuto); non è stata autorizzata né eseguita alcuna generazione. Prima della prova ha chiesto di cambiare metodo e ripartire da zero. La schermata di opzioni chiuse su posizione, luce e numero di oggetti è stata rifiutata come esperienza troppo rigida. Le scelte creative precedenti sono **osservazioni della run interrotta, non vincoli del restart**.

**Regola sperimentale aggiornata — v0.3 (sostituisce v0.2 soltanto per l'interfaccia creativa, non il protocollo FORMA-001):**
- Sequenza obbligatoria per ogni macro-gate: **proposta del gate → breve intervista aperta → riepilogo/approvazione → avanzamento di UN layer**. Non passare al gate successivo prima di aver offerto l'intervista, anche se la scelta sembra completa.
- Il gate presenta in poche righe: **su cosa lavoriamo, cosa cambia visivamente, quando/perché un professionista lo decide**. Mostrare 2 alternative realmente distinguibili quando aiutano; non trasformare ogni dettaglio in un sondaggio o in un form.
- Dopo il gate, una **sola domanda aperta**: «Vuoi indicarmi elementi da inserire, posizione, stile o altri vincoli? Puoi anche rispondere “interpreta tu”.» Le istruzioni possono essere libere, parziali o assenti. Nessun obbligo di compilare campi. Se mancano dettagli, l'agente propone scelte professionali motivate, senza bloccare la run.
- Se l'utente anticipa indicazioni per layer futuri, **registrarle come vincoli/proposte per i rispettivi layer**, senza applicarle prematuramente né saltare gate o verifiche. Ogni layer resta revisionabile; evitare fretta di chiudere il post.
- Ordine dei layer nel percorso B: **direzione/sfondo → fotografia e oggetti (posizioni, inquadratura, luce) → tipografia/layout → verifica e revisione**. Un gate può accorpare decisioni tecniche, ma non eliminare l'intervista aperta e la conferma umana.
- Per la fotografia, chiedere autorizzazione **separata ed esplicita** prima di generare. Non creare immagini, file, installazioni o spese per effetto della sola scelta di un gate. Budget esterno incrementale €0.
- Testare se il flusso è meno oneroso misurando: domande aperte, richieste di chiarimento superflue, parole mostrate, correzioni richieste, decisioni umane, generazioni autorizzate, qualità finale e tempi se disponibili. Non dichiarare qualità o risparmio dimostrati prima della prova.

**Restart:** ID **LAYER-002-R2**. Azzerare le scelte visive della run interrotta; mantenere soltanto brief FORMA-001, protocollo canonico, vincoli generali approvati (fotografia protagonista, niente pannelli opachi non autorizzati), e metodo v0.3. Iniziare dal **Gate 1 — direzione visiva**, presentare opzioni concise e chiudere con **intervista aperta**, non con un questionario. Non generare alcuna immagine finché non arriva un'esplicita autorizzazione.


### LAYER-002-R2 — regola di conservazione dell'asset (feedback utente, 2026-11-09)

**Regola vincolante per il test:** una volta approvata una fotografia, uno sfondo o un template, **conservarne identità e versione**. Le modifiche successive si applicano soltanto agli elementi/layer espressamente richiesti. **Non sostituire, rigenerare o reinterpretare il fondo senza richiesta o autorizzazione esplicita dell'utente.** Se una modifica non può essere isolata con gli strumenti disponibili, dichiararlo prima e proporre un'alternativa; non presentare un nuovo scatto come revisione fedele del precedente.

**Operatività:** conservare l'originale immutabile, riferimento/percorso recuperabile e versione; creare revisioni separate con changelog sintetico (cosa cambia / cosa resta bloccato); verificare visivamente che le aree protette siano rimaste identiche. Evitare query di immagini nuove per illustrare piccole revisioni di un riferimento già scelto: una query diversa può mostrare una scena completamente diversa. Se il riferimento non è stato salvato come asset recuperabile, dichiarare il limite e richiedere un file o autorizzazione a creare la base prima di promettere continuità pixel-identica.

**Stato del Gate 2:** l'utente approva come **base concettuale** una composizione minimalista ma non vuota: circa tre piante da interno distribuite (Kentia, Monstera, Pothos), vegetazione esterna attraverso la vetrata, pochi arredi e spazio negativo. Ha osservato che le anteprime precedenti cambiavano completamente fotografia di sfondo, comportamento da evitare. L'immagine di riferimento mostrata in chat **non è un asset generato, salvato o versionato nella repository**; nessuna generazione fotografica è stata autorizzata in questa fase. Prima della prima generazione chiedere autorizzazione esplicita e poi conservare l'asset approvato come base per i layer successivi, previo consenso alla scrittura.

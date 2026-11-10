# GPT SOCIAL — Pilota Android A: audit conclusivo e proposta di correzione
Data: 2026-11-10. Stato: **PARTIAL complessivo / FAIL sul risultato finale fedele**. Fonte primaria: interazione Chat A e feedback espliciti dell'utente; screenshot e fotografie non archiviati qui. Non attribuire a questa relazione valore di verifica automatizzata del dispositivo o dei byte delle immagini.

## Domanda e perimetro
«Mi lascia dirigere un post sulla mia foto senza perdere quello che ho approvato?». Pubblico: genitori; obiettivo: iscrizioni a lezioni di handpan per bambini; due strumenti; 30 € a lezione. Fotografia dell'utente da conservare. Test avviato in sola lettura, successiva autorizzazione a pubblicare **report e audit** in repository: nessun permesso di archiviare foto, screenshot o asset finale.

## Progressione osservata
1. Brief + fotografia: due direzioni testuali con schemi, A «La musica è una scoperta» selezionata. Buona separazione schema/foto.
2. Console progressiva: titolo esatto «Scopri la magia dell'handpan.»; stile A2 «Creativo e giocoso»; palette P5 «Cielo e miele» (#E6F1F2, #356A82, #F0BC62, #E78E72); composizione C2 «Editoriale asimmetrica» (foto a sinistra, titolo a destra, fascia informativa in basso). L'utente ha chiesto almeno tre palette ulteriori; la selezione precedente non è stata cancellata. Controlli via radio, testo libero e conferma in chat.
3. Autorizzazione a preview: compositing con Pillow/PIL su foto originale; raster quadrato 1080x1080, regione foto a sinistra 610x880 con ridimensionamento e ritaglio; testo e fascia prezzo a destra/in basso. Parametri scelti dall'agente, non approvati in dettaglio. R01 visualizzata in Android aprendo immagine; screenshot utente dimostra visualizzazione della preview, non necessariamente il confronto completo.
4. Feedback «un po' vuoto»: campioni onde, scintille, ritmo, bolle, nastri. R02 con onde in alto e archi in basso. Utente richiede legenda stabile per editare singoli elementi; archi sostituiti con handpan stilizzato, giudicato non riconoscibile. L'utente richiede sempre più alternative visive e linguaggio naturale anziché sigle. Poi scarta il disegno dello strumento.
5. Selezione «combinazione di più idee»: bolle, nastri e scintille. Esplorazioni generative più ricche ottengono preferenza estetica, **ma modificano il volto**. L'utente segnala esplicitamente la violazione.
6. Tentativi di riparazione con Pillow: foto sorgente preservata nella regione fotografica della composizione; nastri/bolle/scintille geometrici sovrapposti. Le prime varianti non compaiono affatto nella chat Android (nessuno spazio visibile); i link PNG separati permettono infine di vedere le immagini. La soluzione tecnica salva la foto ma perde il carattere ricco, fluido, giocoso-elegante dello screenshot.
7. L'utente fornisce screenshot del risultato desiderato e ripete che lo vuole «come lo screen», possibilmente identico, con **solo** la fotografia autentica. L'agente chiede nuovamente se reinterpretare, nonostante il vincolo chiaro. Ulteriori generazioni creano ancora un volto differente e differenze estetiche: **secondo errore finale**, senza approvazione.
8. Stop richiesto dall'utente: audit, riflessione, miglioramenti. Non si è svolta la prova cambio del solo titolo + undo; nessuna approvazione finale, nessuno screenshot della preview approvata, nessun checkpoint finale per Chat B.

## Cosa ha funzionato
- Brief e direzione creativa progressiva con una scelta alla volta, mini-preview testuali, colori visibili e schemi con distribuzioni realmente diverse.
- Conservazione esplicita di titolo, stile, palette e layout nelle conferme; possibilità di chiedere altre idee senza azzerare il percorso.
- L'utente è riuscito a correggere il gusto («giocoso» non equivale a «infantile») e a fornire uno screenshot come riferimento estetico.
- Prima preview fotografica effettivamente visibile sul telefono; workaround con link PNG visualizzabile più avanti.
- La composizione deterministica consente di evitare la rigenerazione del volto, a costo di un diverso livello di raffinatezza decorativa.

## Difetti e cause (fatti vs ipotesi)
**P0 — Foto non fedele.** Fatto: due fasi di generazione dell'intero poster hanno alterato il volto secondo l'utente. Causa procedurale: uso di generazione raster sull'intera scena invece di un motore di overlay con maschera immutabile della foto. Un prompt «non modificare volto» non è un controllo verificabile. Non dichiarare identità pixel se non testata sui byte nelle condizioni appropriate.

**P0 — Estetica approvata non preservata.** Fatto: l'utente preferisce il riferimento ricco e fluido e rifiuta le ricostruzioni semplicistiche. Causa: il riferimento visuale non è stato tradotto in livelli decorativi, curve, opacità, sfumature e gerarchia editabili; generazione e PIL non condividono una rappresentazione canonica. «Stesso tema» non equivale a fedeltà al riferimento.

**P1 — Visibilità non affidabile.** Fatto: due varianti elaborate non apparivano nella chat Android, nemmeno come spazi; link PNG successivi visibili. Causa tecnica esatta non verificata: distinguere produzione, allegato/render, apertura e conferma di visibilità. Evitare di dire «mostrato sopra» senza riscontro.

**P1 — Mancanza di controllo sul singolo oggetto.** L'utente ha richiesto una legenda e nomi comprensibili. ID tecnici utili internamente; in chat usare «nastri sopra il titolo», «bolle sul bordo foto», ecc. Modifiche circoscritte e diff per layer obbligatori.

**P1 — Mancata convergenza.** L'agente ha richiesto nuovamente una scelta già risolta e ha generato altre alternative non autorizzate come sostituzione della foto. Introduzione necessaria di lock e gate: se l'utente dice «identico allo screenshot salvo X», non riaprire il brief.

**P2 — Falsi segnali di avanzamento.** Preview, schema, riferimento generativo, raster composito e asset finale sono stati talvolta trattati come intercambiabili. Servono etichette esplicite e stato verificato.

## Analisi strumenti e procedure
- **Console conversazionale / controlli DIL:** buona per selezioni discrete, preview colore/testo e progressione; stato locale dei controlli non è un documento persistente né una garanzia di applicazione al renderer. Richiede serializzazione di ogni conferma.
- **Pillow/PIL:** compositing raster deterministico, adatto a preservare foto e testi e a verificare regioni; debole se si improvvisano curve ricche, materiali traslucidi, gradienti e qualità grafica. Il confronto di una regione composta con la baseline non equivale all'identità byte del file sorgente.
- **Generazione immagini:** efficace nel proporre un'estetica ricca, ma non affidabile per la fedeltà di una fotografia personale quando rigenera la scena. Usarla soltanto per concept o asset decorativi isolati su trasparenza, mai per ricreare la foto bloccata.
- **Screenshot utente:** ottima prova di aspetto e visibilità; non è sorgente editabile, non prova i byte. Va associato a revisione e distinto dal checkpoint.
- **Link PNG:** workaround Android osservato; non sostituisce la prova inline e non è di per sé un asset finale.
- **GitHub:** registro versionato e handoff, non renderer; non caricare foto o screenshot senza permesso.

## Workflow raccomandato: lock, compositing, verifica, approvazione
1. **Brief e scelte:** una decisione sostanziale per volta, due o più alternative visive per nuovi elementi; distinguere proposta e approvazione.
2. **Checkpoint di lavoro canonico:** titolo letterale, colori esatti, foto sorgente con identificatore locale/hash se calcolabile, dimensioni/ritaglio effettivi, struttura e layer, valori approvati vs agent-assigned, riferimento estetico (screenshot separato), aree protette, revisioni e diff. Un solo stato; no coordinate inventate da descrizioni.
3. **Freeze fotografico:** il renderer carica la foto originale, non la passa a un generatore dell'intero poster; overlay SVG/Canvas/Pillow sopra la regione fotografica. Maschera di protezione per volto, mani e strumento se necessario; compositing senza modifiche ai pixel della base prima dell'overlay.
4. **Fedeltà al riferimento:** prima di renderizzare, ricostruire la grammatica del riferimento come layer: nastri Bezier con gradienti e trasparenza, bolle con highlight/refraction simulata, scintille luminose, profondità e sovrapposizioni. Confronto affiancato con screenshot per valutare somiglianza estetica; non attribuire coordinate esatte allo screenshot.
5. **Revisioni transazionali:** richiesta «cambia X» -> copia dello stato approvato -> diff solo X -> render -> confronto visivo -> commit dello stato solo dopo approvazione. Undo deve ripristinare realmente il raster e i valori, non soltanto una risposta testuale.
6. **Delivery gate Android:** prima prova visiva inline; se non visibile, un solo fallback documentato con PNG apribile; chiedere conferma esplicita; in caso negativo stop, non moltiplicare tentativi.
7. **Approvazione e handoff:** una revisione approvata, screenshot solo su istruzione al momento esatto, checkpoint A distinto dai dati di utilizzo; Chat B solo dopo disponibilità e readback del checkpoint autorizzato.

## Incrementi tecnici da valutare (non autorizzati allo sviluppo)
**Primo incremento minimo:** un renderer compositivo per *un solo template C2* con foto originale bloccata, decorazioni vettoriali editabili e snapshot di stato; SVG per curve/gradienti/bolle e rasterizzazione controllata, senza generazione della persona. Esportazione di due varianti in un unico messaggio, con fallback PNG. Non costruire ancora backend o console universale.

Test automatici minimi: hash foto sorgente; confronto pixel della regione foto prima di applicare overlay (tenendo conto di crop/resize); diff pixel fuori dalle regioni autorizzate; test snapshot di titolo/palette/layout; undo A->B->A; confronto visivo su Android confermato dall'utente; assenza di regressioni nei testi. Verifica separata della fedeltà estetica, necessariamente anche umana.

**Secondo incremento condizionato:** editor dei layer con nomi naturali e riferimenti stabili; maschere, Bézier e trasparenze controllabili. **Terzo solo se i test lo giustificano:** generazione di elementi decorativi isolati con alfa e integrazione nel renderer, mai generazione dell'intero poster con foto protetta.

## Dati di utilizzo e verdetto
- Turni utente: **almeno 17** messaggi operativi visibili in questa Chat A dal brief allo stop (conteggio manuale, non telemetria; non includere messaggi di sistema/tool).
- Vincoli ripetuti: conservazione foto/volto ripetuta più volte; fedeltà allo screenshot ripetuta esplicitamente almeno tre volte nella fase finale. Numeri esatti di ripetizioni non certificati da strumentazione.
- Alternative: due direzioni iniziali, tre stili, tre palette iniziali + quattro aggiuntive, tre composizioni, più campioni e varianti decorative; non tutte sono state confermate visibili.
- Visibilità: R01 confermata via screenshot Android; almeno un tentativo di coppia invisibile; successivo accesso a due PNG confermato; le ultime generazioni non sono approvate.
- Testo libero: usato per brief e correzioni creative; «altre idee» richiesto; undo del titolo **non eseguito**.
- Modifiche collaterali: volto alterato in generazioni; estetica persa nei compositing; nessuna identità pixel completa verificata.
- Tempo attivo, costi e latenza: **non misurati**. Nessun valore inventato.
- Approvazione finale: **assente**. Screenshot finale approvato: **assente**. Chat B: **non avviata**.
- **PARTIAL** per conduzione e controllo concettuale; **FAIL** per la produzione del risultato finale conforme ai due vincoli; test undo **NOT RUN**. Non aggregare in un PASS.

## Riflessione indipendente
La causa di fondo è l'assenza di un contratto fra decisione creativa, riferimento visivo e renderer. La chat ricordava le parole ma non possedeva un oggetto grafico editabile capace di conservare insieme **identità della foto** e **qualità della decorazione**. Quando la qualità visiva aumentava, l'identità veniva persa; quando la foto era protetta, la qualità si appiattiva. Il rimedio non è un prompt più severo o un altro giro di generazione: è un renderer con livelli, invarianti verificabili, riferimento estetico separato e approvazioni transazionali. La conversazione deve diventare l'interfaccia di direzione, non il luogo in cui si reinventa l'intero asset a ogni turno.

## Un solo prossimo passo
Progettare e validare **un prototipo minimo C2 con foto immutabile e layer decorativi fedeli allo screenshot**, usando un unico test A/B visibile su Android e criteri di accettazione espliciti. Prima di implementare, ottenere approvazione dello scope e del metodo; non ripetere altre generazioni integrali del poster.

Riferimento metodologico: [protocollo pilota Android](pilota-foto-diretta-android.md). Questo documento è un audit di Chat A, **non** il checkpoint per Chat B e non contiene immagini personali.


---

## Addendum — Pilota Android T1 (10 novembre 2026)

**Sessione:** GPT-SOCIAL-T1-20261110-01. **Mandato:** Strategia B, direzione creativa su fotografia originale dell'utente. **Esito:** **FAIL** per la conduzione visuale; **NOT TESTED** per poster, modifica locale e Undo. Questa sezione riguarda una **nuova corsa**, distinta dall'audit del pilota A riportato sopra. Fonte: messaggi osservabili nella chat T1 e segnalazione esplicita dell'utente; non sono disponibili screenshot Android di questa corsa, misure strumentali o raster generati.

### Sequenza e decisioni
1. L'agente legge da `main` `AGENTS.md`, `README.md`, `docs/decisioni.md` e `docs/pilota-foto-diretta-android.md`; il documento di audit non è su `main` e viene recuperato dal diff della PR #11.
2. L'utente carica **una fotografia originale** di un musicista con handpan all'aperto. Non viene caricata su GitHub.
3. L'utente fissa il brief: **giocoso e fiducia**, lezioni per bambini, su appuntamento, Bologna, contatto Matteo, **nessun prezzo**. Il numero di telefono è stato fornito in chat, ma non è riprodotto in questo documento pubblico.
4. L'agente presenta due proposte verbali, «Giocosa elegante» e «Ludica fresca», più tre titoli alternativi. Non produce anteprime per le sezioni, né controlli che ne aggiornino il contenuto.
5. L'utente ferma il flusso e segnala: **«per ogni sezione che mi dai devo vedere un'anteprima con le scelte che mi fai fare che cambiano l'anteprima»**, chiedendo audit della mancata procedura.
6. L'agente riconosce il difetto. L'utente chiede di **registrare l'audit in repository, non in chat**.

### Non conformità NC-T1-001 — anteprima interattiva assente
- **Requisito operativo ribadito dall'utente:** ogni sezione con scelte deve rendere visibile un'anteprima pertinente e l'effetto della selezione sull'anteprima stessa; non basta descrivere palette, stile, layout o titoli.
- **Osservato:** due direzioni e tre titoli in sola forma testuale; nessuna preview collegata alle selezioni, nessuna prova di aggiornamento della preview, nessuna verifica su Android.
- **Classificazione:** **FAIL / bloccante per il processo di direzione creativa**. L'agente ha anticipato la richiesta di scelta anziché predisporre il dispositivo visivo necessario a giudicarla.
- **Radice procedurale:** mancata traduzione del principio «direzione visuale progressiva» in un gate concreto: **mostrare e collegare la preview prima di chiedere la conferma**. Non è stata testata una causa tecnica; non attribuire il difetto all'app Android o ai controlli UI.

### Stato delle verifiche
| Requisito | Esito T1 | Evidenza o limite |
|---|---|---|
| Lettura contesto | PASS limitato | Quattro documenti letti da main; audit recuperato dalla PR #11, non da main |
| Ricezione foto e brief | PASS | Input visibili in chat; hash file non calcolato |
| Alternative distinguibili visivamente | FAIL | Solo descrizioni, nessuna anteprima delle due direzioni |
| Anteprima aggiornata dalle selezioni | FAIL | Nessun controllo collegato a un'anteprima |
| Direzione approvata e checkpoint creativo | NOT TESTED | Nessuna direzione approvata |
| Poster esteticamente soddisfacente | NOT TESTED | Nessun poster prodotto |
| Integrità della foto nel compositing | NOT TESTED | Nessuna composizione e nessun confronto pixel |
| Visualizzazione risultato su Android | NOT TESTED | Nessuna preview generata/confermata |
| Modifica locale V1 e Undo V2 | NOT TESTED | Nessun V0 approvato; nessuna revisione |
| Confronti/hash/riproducibilità | NOT TESTED | Nessun artefatto di output da misurare |

**Distinzione delle evidenze:** il difetto di procedura è confermato dalla sequenza dei messaggi e dal feedback dell'utente; non esistono conferme Android di visualizzazione, giudizi estetici su un poster o verifiche tecniche di invarianza della fotografia per T1. Le proprietà del precedente T0 **non** si trasferiscono automaticamente a questo test.

### Miglioramento minimo raccomandato (proposta, non autorizzazione allo sviluppo)
Per una nuova corsa, prima di chiedere qualunque scelta su stile, palette, tipografia, composizione, testo o decorazione, presentare una **preview della sezione effettivamente visibile e influenzata dalla selezione**, usando gli strumenti già disponibili. Dichiarare se si tratta di schema illustrativo o anteprima del post reale. Verificare che l'interazione cambi davvero la preview e che gli elementi già approvati restino invariati. Se non è possibile renderla visibile/aggiornabile su Android, fermarsi e dichiarare il blocco prima di proporre nuove scelte. Non generare l'intero poster ricostruendo la foto.

**Chiusura T1:** prova interrotta prima di V0; nessun poster o Undo; nessuna fotografia/screenshot archiviata; nessuna modifica a renderer o schema. **Un solo prossimo passo proposto:** ripetere la fase di scelta creativa con anteprima interattiva visibile, con verifica esplicita dell'utente su Android. Non avviare automaticamente il test né decidere la roadmap.

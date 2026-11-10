# Pilota Android — dirigere un post sulla propria fotografia

**Domanda scelta dall’utente, 10 novembre 2026.** «Mi lascia dirigere un post sulla mia foto senza perdere quello che ho approvato?»

## Stato operativo

- **Mandato A — direzione su Android.** Primo tentativo fallito secondo l’utente; [audit del primo tentativo](https://github.com/Matteo-Exp-Transformer/generazione-contenuti-GPT-SOCIAL/pull/11). Ripetizione in corso, esito aperto. L’agente A registra l’esito della ripetizione e, quando disponibile, lo SHA e il percorso del checkpoint approvato e verificato da remoto.
- **Mandato B — ripresa indipendente.** In attesa del checkpoint della ripetizione. Alla consegna, B legge prima i soli dati e fissa la propria risposta; poi apre lo screenshot della stessa revisione, se disponibile. A verdetto concluso aggiorna qui l’esito, il riferimento alle prove e il prossimo passo. I dettagli della procedura e i criteri sono nelle sezioni sotto.

## Direzione di prodotto e ragioni della prova

Il [PRD](PRD-v0.1.md) punta al post statico professionale. [FORMA](../benchmarks/FORMA-001/risultati.md) ha mostrato problemi di fedeltà ai testi; [LAYER](audit-layer-001-handoff.md) il costo delle microdecisioni; [Istanbul](report-run-ecovillaggio-istanbul-2026-11-09.md) il fallimento del confronto quando le varianti sono invisibili sul telefono. Nel [Tattoo](audit-run-tattoo-console-guidata-2026-11-10.md) l’estetica scelta è andata persa durante una revisione del titolo. Il valore da verificare è il controllo dell’utente su quella revisione.
   
La [002](https://github.com/Matteo-Exp-Transformer/generazione-contenuti-GPT-SOCIAL/pull/6) ha prove tecniche recuperabili su un template neutro e un cambio di colore. La [003](audit-creative-console-003-cold-test-2026-11-10.md) ha dimostrato recuperabilità documentale del concept. Un template per foto reali, la parità fra preview e post e il ripristino automatico della UI rimangono aperti. Provare prima la console guidata; valutare un solo template produttivo se il concept supera il pilota. Preset multiprogetto, backend e sistema modulare richiedono casi che ne mostrino il beneficio.

## Checkpoint sperimentale e riferimento visivo

Tenere distinte parole dell’utente, valori applicati e scelte ancora delegate. “Asimmetrica” permette una ripresa concettuale; per ricostruire una pagina servono anche fonte e parametri effettivi. La Chat A redige il checkpoint strutturato e lo conserva nella repository insieme al riferimento visivo della stessa revisione, in file distinti, senza estendere lo schema o il renderer 002.

| Da registrare alla conferma | Dettaglio utile |
|---|---|
| Identità e ambito | ID del caso, revisione e precedente, frase di approvazione, cosa è approvato (idea, layout o asset). |
| Sorgenti e composizione | Foto originale recuperabile se condivisa; hash solo se calcolato sui byte. Template e versione o descrizione libera. Per una composizione effettivamente impostata: formato, origine e unità, ritaglio, posizione/scala, ordine dei livelli, zone protette e modifiche consentite. |
| Testo e stile | Stringhe esatte, palette con valori e ruoli, font/peso/dimensione e allineamento se effettivamente impostati. Identificare valori proposti, confermati, misurati, delegati o mancanti. Vietato stimare coordinate o font da uno screen per poi registrarli come approvati. |
| Revisione e undo | Revisione prima/dopo, unica modifica richiesta, differenze osservate, ultima revisione approvata e risultato dell’undo. Un undo in chat dimostra il ripristino dei valori testuali; per il ripristino visivo serve la preview. |
| Riferimento visivo opzionale | Un solo screen della preview approvata sul telefono, collegato a ID/revisione e indicato come schema o raster. Ritagliare notifiche, dati personali e contenuti estranei. Registrare ciò che era davvero visibile. Se lo screen manca, il controllo visivo resta aperto. |

Lo screen conserva l’aspetto visto, compresi a capo e ritaglio. L’originale e i parametri consentono di intervenire di nuovo. Una discrepanza fra screen e dati blocca solo la parte ambigua: mostrare il conflitto e chiedere quale versione vale. L’identità del file sorgente richiede un confronto sui byte; l’invarianza dell’immagine composta richiede un confronto delle regioni protette nelle stesse condizioni di rendering.

## Due chat, un solo caso

**A — direzione su Android.** Brief naturale e foto originale. Due direzioni descritte a parole. Dopo la selezione, pannello progressivo con mini-preview di messaggio, stile, palette e composizione; lasciare spazio a testo libero e ad altre idee mantenendo la selezione. Schemi esplicitamente etichettati; per giudicare la fotografia usare solo la stessa foto reale inline, se l’utente autorizza il confronto. Cambiare il solo titolo, provare undo, scegliere una revisione e approvarla esplicitamente. La Chat A compila checkpoint e registro di utilizzo. Mostra la preview inline. Per attestare la vista sul telefono, l’utente cattura lo schermo della revisione approvata e lo allega in A, salvo disponibilità dimostrata di una cattura diretta del dispositivo. Identificare un eventuale raster esportato dall’agente come preview. Se le preview richieste non sono visibili sul telefono, fermare la fase visiva e registrare il limite. Produzione finale e archiviazione di foto/screen su GitHub richiedono autorizzazione specifica.

**B — ripresa indipendente.** Nuova chat, senza transcript o suggerimenti sulla risposta attesa. La Chat A consegna un messaggio di avvio per B con URL repo, SHA e percorso del checkpoint. L’utente copia solo il messaggio. La Chat B legge da GitHub esclusivamente il checkpoint, senza aprire PR, immagini o dati di utilizzo, e pubblica la prima risposta: scelte esatte recuperate, elementi protetti, modifiche ammesse, dati mancanti e prima azione consentita. Nel turno successivo B apre dal medesimo SHA lo screen collegato nel checkpoint. A usa nomi neutri nella stessa directory, ad esempio checkpoint.json e screen-android.png, e verifica da remoto JSON e immagine prima di consegnare. Se i byte non sono accessibili in una delle chat, dichiarare il limite e usare l’allegato manuale solo come ripiego. Registrare quali dettagli conferma, contraddice o chiarisce e quali rimangono incerti. L’utente confronta le due letture con l’approvazione di A. Un allegato manuale prova il trasferimento assistito; una ripresa autonoma da GitHub richiede un checkpoint effettivamente pubblicato e riletto. Nessuna necessità di ripetere il cold test 003.

## Esiti da raccogliere

- A: numero di turni utente dal brief all’approvazione o allo stop; richieste di ripetere un vincolo; confronti mostrati/visibili; uso di testo libero, altre idee e undo; modifiche collaterali. Tempo attivo solo se misurato. Una frase dell’utente su ciò che ha facilitato o impedito la scelta.
- B: campi approvati corretti/totale effettivamente presenti, omissioni, valori inventati, contraddizioni, chiarimenti richiesti e differenze fra lettura dei soli dati e lettura con screen. Indicare prove disponibili e limiti. Senza screen l’incremento informativo resta non valutabile.
- **PASS** per la direzione creativa se l’utente vede e distingue le alternative, approva e riesce a modificare/ripristinare solo il titolo. **PASS** per la ripresa se B recupera le scelte esplicite, rispetta i vincoli e segnala gli ignoti senza inventare. **PARTIAL** per un passaggio recuperato manualmente, una scelta ambigua o una verifica visiva mancante; **FAIL** per perdita della scelta, confronto essenziale inutilizzabile o modifica non autorizzata. Valutare separatamente capacità di ricostruzione esatta: senza dati e confronto idonei resta non verificata anche se il concept è recuperabile.
- Riunire esiti A/B e un solo prossimo incremento nel medesimo resoconto. Il registro di utilizzo di A resta fuori dal checkpoint; B lo consulta solo dopo il proprio verdetto. Se è autorizzata l’archiviazione, verificare PR e ramo esistenti, salvare un unico esito pertinente e rileggere il contenuto remoto. Nessun file vuoto o audit preventivo.

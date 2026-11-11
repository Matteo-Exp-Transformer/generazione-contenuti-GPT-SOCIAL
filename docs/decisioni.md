# Registro decisioni — sintetico

- 2026-11-09: brand editoriale fittizio **FORMA** per isolare qualità creativa dai vincoli di brand reali.
- 2026-11-09: benchmark 01, tema **La forma della luce**, interior design e luce naturale.
- 2026-11-09: concept **B — INTERSEZIONI** approvato: fotografia asimmetrica, dettaglio materico, gerarchia tipografica articolata.
- 2026-11-09: confronto approvato fra **A post completo generato** e **B fotografia + layout separato**.
- 2026-11-09: budget incrementale €0, nessuna generazione o modifica dell'ambiente autorizzata.
- 2026-11-09: repository minima iniziale; audit successivo di memory, app parquet e calendar backup per eventuali skill/system, senza import automatici.

Decisioni ancora aperte: griglia definitiva, font/licenze, strumenti effettivi, asset, modalità di rendering, eventuali skill minime.

- 2026-11-09: approvata per **test sperimentale**, non come protocollo canonico, la pipeline a **cono creativo adattivo**: fino a 3 direzioni iniziali, mix tra varianti, progressiva convergenza, interviste aperte, anteprime reali grandi in chat, codici V1/V2/V3 per varianti, A/B/C per testi e 1/2/3 per elementi fotografici, asset lock e modifiche circoscritte. Specifica e prompt in `docs/archivio/test-cono-creativo-v01.md`. I precedenti collage generativi **non** hanno verificato l'identità pixel della fotografia. Nuova run da zero e audit indipendente ancora da eseguire.

- 2026-11-09: **correzione post-audit approvata** per la prossima run: anteprime reali grandi direttamente in chat Android, preferibilmente due per volta in griglia statica a due colonne con scorrimento verticale della chat; composizione iniziale con pochi elementi e aggiunte progressive; legenda puntuale A/B/C testi e 1/2/3 singoli oggetti, senza confondere codici con layer editabili. L'utente riferisce che precedenti agenti GPT hanno già mostrato con successo griglie a due colonne di sfondi e tipografia ingrandibili su Android: evidenza d'esperienza utente, **componente tecnico esatto da confermare con test riproducibile**. Nessun download obbligatorio. Protocollo aggiornato in `docs/archivio/test-cono-creativo-v01.md`; nessuna validazione tecnica anticipata.

- 2026-11-09: **rettifica dell'utente**: il formato Android riuscito NON era un carosello. Era una griglia di due immagini per riga, su due colonne, con scorrimento verticale normale della conversazione; niente swipe orizzontale. Questo layout è il riferimento da verificare nella prossima run.

- 2026-11-09: **micro-test Android superato per la presentazione di riferimenti visivi**. L'utente conferma di vedere correttamente due immagini di riferimento affiancate in una griglia nativa a due colonne, scorrendo verticalmente la chat, con dimensioni soddisfacenti. Nella prova è stata usata una griglia con immagini AsyncImage. Non confondere questo successo con la prova di visualizzazione degli asset generati, dell'asset lock o dell'export, che restano aperti.

- 2026-11-10: l’utente sceglie come prossimo esperimento la direzione di un post sulla propria fotografia mantenendo le scelte approvate. [Contesto di prodotto e proposta di prova in due chat](archivio/pilota-foto-diretta-android.md). La validazione sul dispositivo e la produzione del post sono aperte.

- 2026-11-10: **strada unica** dopo l'audit indipendente Claude (verdetto *in deriva*). L'utente decide di riorganizzare il progetto consolidando la strada consigliata (foto bloccata + render deterministico + stato JSON) e, se non funziona o i risultati sono troppo lontani, di passare a strumenti via MCP (Canva, Figma…), ammettendo account di prova. Priorità: accorciare i tempi della decisione. Sospesi G-FOTO-01 e i gate su fixture neutra; T1 HOLD fino al Gate D. Esecuzione in [MANDATO-001](mandato-001-strada-unica.md); procedura di chat del prodotto in [skill post-director](../skills/post-director/SKILL.md).

- 2026-11-10: **conferma esecutiva dell’utente (§0-bis)**: la revisione Claude recepita in MANDATO-001 e le decisioni prese con lui guidano la repo; prevalgono le successive decisioni esplicite dell’utente, mai proposte autonome degli agenti. Run Sol 6.1: F0 poi engine F1-A, massimo due task delegati; PR #14 già integrata, branch da eliminare in F0. Lo storico non riapre strade superate.

- 2026-11-11: **autorizzazione operativa — indagine Canva**: audit separato in `evidence/canva-capabilities/`, branch dedicato, PR e aggiornamento del passaggio; nessun merge, foto/dati personali in repo, modifica a engine/skill/roadmap, spesa o integrazione. Le alternative e la raccomandazione dell'[audit](../evidence/canva-capabilities/audit-2026-11-11.md) restano proposte del QA, non decisioni dell'utente.

- 2026-11-11: **istruzione esplicita dell'utente su F1-B**: trattare la PR #19 come evidenza della sonda MCP; Canva ha importato la foto ma l'anteprima inline su ChatGPT Android non è visibile (link esterno sì). Non attribuire PASS e non anticipare Gate D senza i risultati della Strada A. La PR #19 non equivale a decisione di percorso.

- 2026-11-11: **stop esplicito dell'utente nella chat pilota Strada A**: risultato creativo insoddisfacente; preferenza per titolo «Un mondo di suoni da scoprire», rifiuto della fascia viola, richiesta di gioco/magia/curve sonore; titolo troppo grande, sottotitolo sui capelli. La generazione di immagine non rispettava preservazione della foto e layer modificabili. Registrare TU-01 come PARTIAL (tecnica Pillow verificata, esperienza non approvata), non ripetere il test e non considerare Gate D superato. Voto numerico e tempo non acquisiti.

- 2026-11-11: **decisione esplicita post TU-01** — fermare il test Strada A e registrarlo **PARTIAL**: render tecnico riuscito, ma risultato creativo insoddisfacente, limiti del renderer e violazione della procedura di preservazione fotografica. Non ripetere il test, non dichiarare Gate D superato; evidenza MCP [PR #19](https://github.com/Matteo-Exp-Transformer/generazione-contenuti-GPT-SOCIAL/pull/19) distinta dalla Strada A. Scelta della strada finale ancora aperta.

- 2026-11-11: **correzione minima richiesta dall’utente**: concordare formato, impaginazione/posizioni, palette, tipografia, testi ed effetti prima del primo render; attendere approvazione del riepilogo. Per il nuovo test, composizione, modifiche e anteprima devono provenire dallo stesso progetto Canva; niente immagini generative introduttive o mockup separati. Prompt unico in STATO.md; risultati del test da riportare dall’utente, senza ripetere TU-01 o anticipare Gate D.

- 2026-11-11: l’utente approva integralmente la direzione creativa del post handpan (formato 4:5, layout E, palette B, tipografia B, testi A, effetti A) e autorizza solo composizione Canva sul medesimo progetto, con preservazione della foto. Dopo il blocco esecutivo, richiede audit nel repository; nessuna autorizzazione a dichiarare superato Gate D. Evidenze e limiti in `STATO.md` («Audit test conversazionale Canva»).

- 2026-11-11: **consolidamento autorizzato su main e aggiornamento del mandato Claude**: integrare il lavoro e i test raccolti, riconciliare lo stato e lasciare continuità secondo la ricerca discussa. Direzione di sviluppo: regista + layout Canva controllabili; sequenza diagnosi client → ciclo Canva completo → confronto manuale/assistito → decisione Gate D. Non equivale ad accettare consultazione esterna, rifinitura raster fuori Canva, spese/installazioni o PASS end-to-end. Il nuovo mandato sostituisce le istruzioni di test superate; TU-01 non si ripete.

- 2026-11-11: **revisione architetturale indipendente richiesta dall'utente** (Claude, branch e PR, senza merge né modifiche a skill/engine). Contesto dichiarato: Regista in chat ChatGPT normale che legge la skill dal repo via connettore GitHub; fedeltà richiesta fra chat ChatGPT diverse; piani ChatGPT Plus + Canva Free; server proprio per stato/autorizzazioni da valutare dopo la revisione. Il verdetto della PR è proposta, non decisione.

# STATO — aggiornato 2026-11-11 dal Costruttore
Obiettivo: dirigere un post sulla propria foto, preservare le scelte e ottenere una consegna verificabile.
Mandato attivo: [MANDATO-001 aggiornato](docs/mandato-001-strada-unica.md).
Direzione di sviluppo: regista conversazionale + layout Canva controllabili; scelta definitiva al Gate D.
Inline Android resta requisito; consultazione esterna e rifinitura fuori Canva non approvate.

## Gate e prove
- F0: PARTIAL storico — consolidamento PR #15; 25 rimandi d'archivio irrisolti, fuori dal prossimo lavoro.
- F1-A engine: PASS sintetico pregresso (18 test, PR #16); nessun test rieseguito in questa run.
- TU-01 Strada A: PARTIAL, chiuso su richiesta utente; render tecnico riferito riuscito, esperienza creativa negativa e violazione procedurale con generazione. PR #20/#21 descrivono lo stesso test. Non ripetere; nessun PASS completo.
- F1-B: PARTIAL — [sonda Canva](evidence/tu-01-mcp/canva-2026-11-11.md): import foto/testi; inline negativo, link esterno positivo in quella prova. Figma: A→B→A senza foto, upload bloccato.
- Regista PR #22: procedura rispettata e miglioramento riferito; composizione nuova non salvata, consegna fallita. Scelte preservate nel mandato §2.
- Capacità Canva PR #23: draft testo/media riusciti, controllo circoscritto su miniatura 480×600; commit/export finale non verificati.
- Ripresa PR #23: baseline recuperata in altra chat; due invii inline Android falliti; ricevuto JPEG 1229×1536, non PNG 1080×1350. Cause ignote.
- Gate D: APERTO, nessuna strada definitiva o PASS end-to-end; F2/T1 HOLD. Date originarie 13/11 e 17/11, nessuna proroga automatica.
- Prova dettagliata: [audit Canva §§1–9](evidence/canva-capabilities/audit-2026-11-11.md). Le parti iniziali descrivono run precedenti; §9 aggiorna ripresa/Android.

## Sequenza verso l'obiettivo
- [x] Consolidare su main evidenze, skill scelte-prima e stato; aggiornare mandato con ricerca.
- [x] Diagnosi immagini: feedback utente raccolto; confronto tecnico NON VERIFICATO (file/metodo/client non certificati).
- [ ] Dopo decisione sul canale, ciclo Canva: modifica → preview → approvazione → commit → ripresa → export.
- [ ] Dopo consegna completa, confronto manuale/assistito: tempo utente, correzioni, qualità, pubblicabilità.
- [ ] Decisione Gate D, poi pilota F2.

## Verifiche inline controllate (feedback Android)
- T01: PASS, PNG sintetico 480×600 (SHA-256 `82efa672d41ea3eeaa2ce522fcc00bdc923ae903580eadc46c3a5f3f284bbbd8`), Python display PIL.
- T02: NON VISIBILE riferito, stesso file via Markdown `sandbox:`.
- T03: PASS riferito, stesso file via Python `IPython.display.Image(data=...)`.
- T04: PASS riferito, stesso file via Python `IPython.display.Image(filename=...)`; hash verificato in tutti i test Python.
- Perimetro: esiti dichiarati dall'utente su questa chat; nessun test cross-browser certificato, nessun Canva in T01–T04. Indizio sul canale di presentazione, causa non accertata.

## Prossimo passo (uno)
Su richiesta esplicita dell'utente, indagare il canale inline con test controllati. Dopo T01–T04, prossimo controllo: miniatura Canva sintetica già presente in evidence, senza modificarla, con un percorso di visualizzazione verificabile; registrare provenienza/hash, distinguendo anteprima draft da export.
Il feedback «Mobile desktop e browser. Niente nessun caso» segnala mancata visibilità riferita su più client, ma non certifica una prova controllata stesso file/metodo/risposta; nessuna causa tecnica attribuita.
Nessun nuovo post o ciclo Canva prima di completare diagnosi e decisione sul canale; consultazione esterna non accettata implicitamente.
Nessun Canva, TU-01, installazione, export manuale o cambio di strada implicito.

## Ultimo passaggio
- Chi/quando: Costruttore/QA, 2026-11-11; serie controllata T01–T04 su Android.
- Fatto: stesso PNG sintetico presentato in quattro modi, senza rielaborazione; l'utente conferma T01/T03/T04 visibili, T02 non visibile.
- Prove: hash SHA-256 identico per T01/T03/T04; visualizzazione di Markdown sandbox non riuscita secondo utente; nessun test Canva in questa serie.
- Aperto/bloccato: causa ignota, da testare miniatura Canva via percorso funzionante; Gate D aperto, F2/T1 HOLD.
- Serve dall'utente: esito del prossimo test; nessuna nuova scelta creativa.

## Prompt di prosecuzione
Repo generazione-contenuti-GPT-SOCIAL, branch main. Leggi AGENTS.md e STATO.md ed esegui il prossimo passo. Chiudi secondo AGENTS.md.

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
- T05: NON VISIBILE riferito, `baseline.png` sintetico Canva dal repository mostrato direttamente via output del connettore GitHub; metodo e sorgente cambiati rispetto a T04, non isolabile.
- T06: VISIBILE, stesso `baseline.png` originale allegato, Python `IPython.display.Image(filename=...)`; PNG 480×600, 15702 byte, SHA-256 `17bff37339b5a60b004fcc8144e2faaeb648c5c0fcfbd85a070908e756168e1e`; Git blob SHA `1c250ff05b8bd6b0130deb50c780554702ba6ddd` coincide col file repo T05.
- T07: VISIBILE riferito, stesso `baseline.png` Canva via Python `IPython.display.Image(data=...)`, hash e dimensioni uguali a T06.
- Perimetro: riscontri utente su Android; T05–T07 stesso contenuto con percorsi diversi; nessuna causa interna o trasferimento automatico dimostrati.

## T08 — Canva → Python → Android (2026-11-11)
- Ricerca prima della prova: confrontati Canva MCP ufficiale e inventario reale; URL thumbnail firmati/scadenti, commit/export e output client distinti.
- get_design + get_design_pages confermano fixture `DAHalgNO4BY`, pagina 1 salvata 1080×1350, miniatura nominale 400×500. Nessun editing.
- Python: richiesta neutra a media.canva.com bloccata dal DNS (`Errno -3`); URL firmato non usato; nessun byte, hash, formato reale o display verificato.
- T08 PARTIAL: metadata OK; Canva→Python bloccato/non provato, Android NON TESTATO. Matrice e fonti nell'audit §15.
- T01–T07 restano 5 VISIBILI / 2 NON VISIBILI secondo utente, senza causa interna provata.

## Prossimo passo (uno)
Test diretto T09 di sola lettura: get_design_pages sul design sintetico esistente ha restituito metadati 1080×1350 e thumbnail nominale 400×500 come URL, non immagine inline; Canva→Python non necessario per consultare il progetto in Canva. Utente accetta consultazione Canva occasionale ma mantiene STOP fino a verdetto sul canale inline. Prossimo passo: decidere se iniziare un ciclo Canva controllato con preview esterna esplicitamente dichiarata, senza confonderla con prova inline. Gate D APERTO, F2/T1 HOLD.

## Ultimo passaggio
- Chi/quando: Costruttore/QA, 2026-11-11; ricerca ufficiale e T09 sola lettura.
- Fatto: escluso Python come requisito del flusso; confermata miniatura via Canva, non immagine inline nativa.
- Prove: documentazione Canva get-design-pages/best practices; get_design_pages design sintetico DAHalgNO4BY, pagina 1080×1350, thumbnail nominale 400×500 via URL.
- Aperto/bloccato: nessun byte acquisito, preview inline Android NON VERIFICATA; T08 PARTIAL; Gate D APERTO, F2/T1 HOLD.
- Serve dall'utente: nessuna nuova approvazione creativa; confermare solo l'eventuale avvio di un ciclo Canva con consultazione esterna dichiarata.

## Prompt di prosecuzione
Repo generazione-contenuti-GPT-SOCIAL, branch main. Leggi AGENTS.md e STATO.md ed esegui il prossimo passo. Chiudi secondo AGENTS.md.

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
- [x] Diagnosi controllata immagini Android/browser senza Canva — PARTIAL; tre contesti non visualizzano la fixture; causa non isolata.
- [ ] Dopo decisione sul canale, ciclo Canva: modifica → preview → approvazione → commit → ripresa → export.
- [ ] Dopo consegna completa, confronto manuale/assistito: tempo utente, correzioni, qualità, pubblicabilità.
- [ ] Decisione Gate D, poi pilota F2.

## Prossimo passo (uno)
QA con l'utente: valutare la diagnosi §5.1 PARTIAL (audit §10), senza attribuire una causa.
L'unico invio Markdown da GitHub raw è risultato invisibile su app Android, browser mobile e vista desktop remota.
La mancata visibilità su tutti e tre non discrimina sorgente URL, trasporto o renderer; nessun test causale eseguito.
Decidere esplicitamente se autorizzare una prova discriminante con metodo/sorgente controllati o mantenere HOLD.
Nessun Canva, TU-01, nuovo post, installazione o Gate D anticipato.

## Ultimo passaggio
- Chi/quando: QA in chat con utente, 2026-11-11; diagnosi §5.1 su branch dedicato.
- Fatto: riutilizzata fixture baseline.png in un unico invio Markdown URL GitHub raw, senza Canva.
- Prove: screenshot/riscontro utente — invisibile su app Android, browser mobile e vista desktop remota; audit §10.
- Aperto/bloccato: causa non isolata, SHA-256 file mostrato non verificato, anteprima inline non certificata; Gate D aperto.
- Serve dall'utente: decisione sul test discriminante successivo; nessun cambio automatico di strada.

## Prompt di prosecuzione
Repo https://github.com/Matteo-Exp-Transformer/generazione-contenuti-GPT-SOCIAL, branch main.
Leggi AGENTS.md, STATO.md e il mandato attivo. Valuta l'esito PARTIAL della diagnosi §5.1 nell'audit §10; proponi una sola prova discriminante senza eseguirla prima della mia decisione. Chiudi secondo AGENTS.md.

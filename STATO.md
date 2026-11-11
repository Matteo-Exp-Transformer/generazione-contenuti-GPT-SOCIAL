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
- [ ] Diagnosi controllata immagini Android/browser senza Canva — UNICO PASSO ATTIVO.
- [ ] Dopo decisione sul canale, ciclo Canva: modifica → preview → approvazione → commit → ripresa → export.
- [ ] Dopo consegna completa, confronto manuale/assistito: tempo utente, correzioni, qualità, pubblicabilità.
- [ ] Decisione Gate D, poi pilota F2.

## Prossimo passo (uno)
Costruttore/QA in chat con l'utente: eseguire mandato §5.1, riusando un PNG sintetico già salvato.
Stesso file, stesso metodo, stessa risposta consultata su Android e browser; due conferme distinte.
Non ripetere i reinvii falliti: cambiare la domanda sperimentale, isolando il client.
Se manca un client o una conferma, registrare NON VERIFICATO e il limite; nessuna causa inventata.
Nessun Canva, TU-01, nuovo post, installazione o cambio di strada in questo passo.
Aggiornare questo stato e audit esistente; scegliere il passo successivo in base all'esito, non automaticamente.

## Ultimo passaggio
- Chi/quando: revisore indipendente, 2026-11-11; addendum documentale per la revisione Claude.
- Fatto: audit Canva §§16–17 nel branch PR #28: confronto test e analisi fedeltà/sequenza/stato, fonti professionali e quesiti per ricerca autonoma con subagent.
- Prove: PR #25/#26/#27 distinte da main; fonti Anthropic, OpenAI, Canva; nessun nuovo test creativo, nessuna skill o engine modificati.
- Aperto/bloccato: efficacia di enforcement, ripresa cross-agent, widget cross-client, font esatti ed export non certificati; Gate D aperto.
- Serve dall'utente: Claude deve revisionare i dati e scegliere un percorso semplice e verificabile, senza assumere che l'audit sia decisione canonica.

## Prompt di prosecuzione
Repo https://github.com/Matteo-Exp-Transformer/generazione-contenuti-GPT-SOCIAL, branch main.
Leggi AGENTS.md, STATO.md e il mandato attivo. Esegui soltanto la diagnosi controllata del canale immagini (§5.1), con me, senza Canva e senza ripetere TU-01. Registra fatti e limiti nelle sedi esistenti e chiudi secondo AGENTS.md.

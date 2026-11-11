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
- Chi/quando: Revisore Claude su richiesta esplicita dell'utente, 2026-11-11; revisione architetturale indipendente con due subagent (ricerca fonti, secondo parere).
- Fatto: verdetto nella PR della revisione: separare il Regista dalla governance del repo, skill breve senza contraddizioni, scheda post visibile, consenso campione/finale, prova pass^k in chat nuove.
- Prove: lettura main, PR #24–#28 e §§16–17; fonti OpenAI/Anthropic/Canva/τ-bench citate nella PR; nessun test, nessuna modifica a skill, engine o architettura.
- Aperto/bloccato: PR #24–#28 aperte e in conflitto su STATO e audit; Canva nei Progetti ChatGPT, export esposto e widget ripetibile non verificati; Gate D aperto.
- Serve dall'utente: decidere sul verdetto; poi un solo task del Costruttore riconcilia le PR e riscrive un unico prossimo passo.

## Prompt di prosecuzione
Repo https://github.com/Matteo-Exp-Transformer/generazione-contenuti-GPT-SOCIAL, branch main.
Leggi AGENTS.md, STATO.md e il mandato attivo. Esegui soltanto la diagnosi controllata del canale immagini (§5.1), con me, senza Canva e senza ripetere TU-01. Registra fatti e limiti nelle sedi esistenti e chiudi secondo AGENTS.md.

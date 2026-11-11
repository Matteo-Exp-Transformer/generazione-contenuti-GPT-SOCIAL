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

## Prossimo passo (uno)
Decisione esplicita dell'utente sul vincolo di visibilità: accettare provvisoriamente preview esterna verificabile del medesimo progetto Canva, oppure mantenere lo STOP fino a soluzione inline.
Il feedback «Mobile desktop e browser. Niente nessun caso» segnala mancata visibilità riferita su più client, ma non certifica una prova controllata stesso file/metodo/risposta; nessuna causa tecnica attribuita.
Se l'utente mantiene lo STOP, non avviare altri post o ciclo Canva. Se accetta l'esterna, progettare solo il checkpoint sintetico successivo del mandato §5, con verifica reale e senza PASS anticipati.
Nessun Canva, TU-01, installazione, export manuale o cambio di strada implicito.

## Ultimo passaggio
- Chi/quando: Costruttore/QA, 2026-11-11; registrazione del feedback della chat §5.1 su branch dedicato.
- Fatto: raccolta la dichiarazione utente «Mobile desktop e browser. Niente nessun caso»; nessun nuovo invio o test eseguito in questa sessione.
- Prove: riscontro utente di invisibilità; non disponibili qui conferme strutturate sul medesimo file, hash, metodo e stessa risposta per due client.
- Aperto/bloccato: confronto tecnico NON VERIFICATO; problema inline riferito su più client, causa sconosciuta; Gate D aperto, F2/T1 HOLD.
- Serve dall'utente: decisione esplicita preview esterna provvisoria oppure STOP; nessuna nuova scelta creativa.

## Prompt di prosecuzione
Repo generazione-contenuti-GPT-SOCIAL, branch main. Leggi AGENTS.md e STATO.md ed esegui il prossimo passo. Chiudi secondo AGENTS.md.

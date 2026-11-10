# STATO — aggiornato 2026-11-10 dal Costruttore
Obiettivo: dirigere un post sulla propria foto senza perdere le scelte approvate.
Mandato attivo: [MANDATO-001](docs/mandato-001-strada-unica.md).
Direzione: revisione Claude recepita dal mandato + decisioni esplicite dell'utente; lo storico non riapre strade superate.

## Gate
- F0 Consolidamento: IN CORSO — consolidamento pronto nel branch, attesa review/merge e pulizia branch; prove nella PR F0.
- F1-A Strada A (TU-01): DA ESEGUIRE — prima engine e test sintetici, poi foto reale in nuova chat ChatGPT entro 13/11.
- F1-B Sonda MCP (TU-01): OPZIONALE, NON AVVIATA — run separata attivabile dall'utente in parallelo, entro 13/11.
- Gate D: IN ATTESA — decisione dell'utente sulle schede TU-01, 13/11, revisore una volta.
- F2 Pilota prodotto: HOLD — dopo Gate D, un post reale entro 17/11. T1 HOLD fino al Gate D.

## Prossimo passo (uno)
Orchestratore — verificare e integrare F0, eliminare branch conclusi verificati, poi delegare engine F1-A (§6) — test sintetici verdi con output in PR; TU-01 resta al regista — entro 13/11.

## Ultimo passaggio
- Chi/quando: Costruttore, 2026-11-10, task delegato 1/2 (F0).
- Fatto: integrate ancestry PR #11, evidenze G-UI-02 e audit Claude; archivio immutabile; istruzioni e fonti operative consolidate.
- Prove: PR F0 con diff, hash archivio, limiti righe e verifica link operativi; PR #14 già merged (3f0572c).
- Aperto/bloccato: review/merge F0 e cancellazioni finali; engine F1-A e TU-01 non eseguiti.
- Serve dall'utente: nulla per i due task autorizzati; foto e valutazioni solo nella successiva chat TU-01.

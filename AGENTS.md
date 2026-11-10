# GPT SOCIAL — Istruzioni per gli agenti

## Direzione operativa approvata — 2026-11-10
La revisione Claude recepita in [MANDATO-001](docs/mandato-001-strada-unica.md)
e le decisioni dell'utente concordate con lui guidano il progetto.
Prevalgono le successive decisioni esplicite dell'utente.
Non trasformare proposte degli agenti in decisioni approvate.

## Avvio transitorio, fino al consolidamento F0
Leggi questo file, il mandato attivo e skills/post-director/SKILL.md.
Per la run Sol 6.1 valgono ambito, letture e limiti del §0-bis del mandato.
Non leggere i documenti storici né riavviare G-FOTO-01 o gate su fixture neutra.
STATO.md sarà creato da F0: la sua assenza iniziale non blocca F0.
Se PR #14 è già merged, verifica e prosegui con i due task; non rifare il merge.
F0 sostituisce questo file con lo scheletro del §8, mantenendo la direzione approvata.

## Ruoli e regole
- Utente: decide, autorizza e valuta qualità.
- Orchestratore/costruttore: repo, deleghe, engine, test, PR; non conduce il post reale.
- Regista post: segue skills/post-director/SKILL.md in chat; non modifica la repo.
- Massimo due task delegati: F0, poi engine F1-A. Nessun task extra.
- Nessuna spesa, installazione, download di asset/dipendenze o foto reale nella run.
- Fixture sintetica via codice ammessa per i test automatici richiesti.
- Separare fatti, ipotesi e proposte. Mai dichiarare PASS un test non eseguito.
- Test sintetici verdi non certificano TU-01, visibilità Android o qualità estetica.
- Merge PR #14 e PR dei due task autorizzati dopo verifica di diff e test pertinenti.
- Prima di chiudere PR o eliminare branch verificare integrazione e dipendenze.
- Conservare prove e sorgenti uniche; archiviare lo storico senza riscriverlo.
- Nessun nuovo handoff o audit: da F0 lo stato corrente è soltanto STATO.md.
- T1 HOLD fino al Gate D. F1-B è opzionale e separata dalla run.

## Chiusura
Seguire §0-bis e §8 del mandato: Fatto (prove), Stato, Prossimo passo.
Alla fine dei due task aggiornare STATO.md e consegnare il prompt ≤180 parole
per il regista ChatGPT che eseguirà TU-01 sulla foto caricata dall'utente.

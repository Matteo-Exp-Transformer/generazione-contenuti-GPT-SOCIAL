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

## Passaggio di consegna fra agenti (obbligatorio)

La repository è la memoria operativa: il prompt successivo è un **puntatore breve**, non un nuovo handoff. All'inizio del mandato rileggere `AGENTS.md` e lo Stato operativo del documento pertinente; verificare branch, HEAD e autorizzazioni correnti. Non assumere che il prompt o i verdict precedenti siano aggiornati. Ogni agente chiude il lavoro svolto **nella stessa risposta**, anche se bloccato, senza promettere esecuzioni future.

Prima della consegna aggiornare, se autorizzato e necessario, **solo la fonte canonica** con evidenze, status, vincoli, eventuali nuovi rischi e un solo prossimo passo; per il pilota Android usare `docs/pilota-foto-diretta-android.md` → «Stato operativo». Se non è possibile scrivere, dichiararlo e non simulare commit. Verificare diff, commit e readback remoto se pubblicati. Non duplicare cronologie, checklist o roadmap in nuovi file. Non promuovere una proposta ad approvazione o un PASS riferito a PASS strumentale.

**Ordine obbligatorio della risposta finale all'utente, sintetica e in italiano:**

1. **Fatto ora:** 1–3 frasi con deliverable, esito e riferimenti verificati; distinguere non eseguito/non accessibile.
2. **Dove siamo → dove vogliamo arrivare:** mini-checklist sequenziale (idealmente 3–6 righe) dei passaggi pertinenti, indicando `PASS`, `PARTIAL`, `FAIL`, `HOLD`, `NON TESTATO` o `PROPOSTO`; ogni riga esplicita il risultato richiesto, non solo il nome del test. Segnare chiaramente l'**arrivo di prodotto** come obiettivo, non come capacità già provata. Derivare la checklist dalla fonte canonica, senza inventare milestones approvate.
3. **Prossimo agente — cosa farà:** 2–4 frasi comprensibili anche a un non tecnico, che spieghino intervento prioritario, cosa ci si aspetta di ricevere e cosa **non** verrà fatto. Esplicitare ciò che richiede autorizzazione. Questa sezione precede sempre il prompt: l'utente può scegliere di proseguire così, integrare attività o fermarsi.
4. **Prompt pronto da copiare:** un unico prompt professionale e breve (preferibilmente 100–180 parole) che rimandi alla repository e allo Stato operativo, identifichi branch/commit verificati o richieda di ricontrollarli, assegni un solo obiettivo, criteri di completamento, limiti, autonomia consentita e consegna. Non ricopiare l'intera storia o il testo delle istruzioni. Richiedere esplicitamente all'agente successivo di ripetere questa consegna.

**Regola di continuità:** il prossimo passo deve ridurre un'incertezza concreta per l'obiettivo di prodotto; evitare test ripetitivi. Distinguere `completato`, `in corso`, `bloccato`, `proposto/non autorizzato`. Se emerge un'attività aggiuntiva utile, presentarla come opzione all'utente senza inserirla automaticamente nel mandato. L'approvazione del prompt non implica merge, modifiche di schema/codice, nuovi test HOLD o nuove spese. Non serve chiedere una risposta dell'utente solo per produrre la consegna.

## Chiusura
Seguire §0-bis e §8 del mandato: Fatto (prove), Stato, Prossimo passo.
Alla fine dei due task aggiornare STATO.md e consegnare il prompt ≤180 parole
per il regista ChatGPT che eseguirà TU-01 sulla foto caricata dall'utente.

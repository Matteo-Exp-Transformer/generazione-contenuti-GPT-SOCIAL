# GPT SOCIAL — Istruzioni per gli agenti

## Scopo
Discovery di workflow per contenuti social statici professionali.
Non sviluppare un'applicazione senza approvazione.

## Lettura iniziale
1. README.md
2. docs/decisioni.md
3. Il brief e il protocollo del benchmark assegnato

Per i mandati del pilota Android leggere il [piano attivo](docs/pilota-foto-diretta-android.md) e partire dalla sezione «Stato operativo». Al cambio di stato, l’agente responsabile aggiorna quella sezione con tentativo, esito osservato o riferito, riferimento alle prove e prossimo passo. Nel mandato B consultare audit, immagini e dati di utilizzo solo nella fase prevista dal piano.

Leggere il PRD solo per decisioni di prodotto.
Consultare memory/wiki/index.md solo quando servono
informazioni sul metodo già adottato.

## Regole
- Una fonte canonica per ciascun argomento.
- Separare fatti verificati, ipotesi e proposte.
- Non duplicare informazioni nei documenti.
- Nessuna immagine, installazione, spesa o modifica
  dell'ambiente senza autorizzazione specifica.
- Non aggiungere skill, agenti o strumenti per inerzia.
- Non dichiarare completati test non eseguiti.
- Preferire strumenti già disponibili.
- Non eseguire push su main senza approvazione.

## Benchmark
Rispettare brief, prompt, protocollo e limiti.
Registrare tentativi, tempi, costo, qualità e difetti.
Confrontare i risultati con gli stessi criteri.
Non inventare punteggi o risultati.

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
Aggiornare il file pertinente.
Riportare prove, decisioni e un solo prossimo passo.
Non creare un handoff separato se lo stato è già
presente in risultati.md o decisioni.md.

Prima di aprire un ramo o una PR, cerca il lavoro già aperto sullo stesso caso.
Tieni nella PR o nel documento pertinente risultati e riferimenti recuperabili.
Conserva prove e sorgenti uniche. Escludi dal commit cache, export provvisori
e copie di lavoro; controlla l’elenco dei file nel diff prima della consegna.
A fine task integra via PR se autorizzato. Prima di chiudere una PR superata
o eliminare un ramo, verifica destinazione, commit o diff equivalenti e PR
dipendenti. Elimina i rami conclusi e verifica su GitHub. Se un ramo serve
ancora, indica nella PR o nella consegna il lavoro aperto e il prossimo passo.

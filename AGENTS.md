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

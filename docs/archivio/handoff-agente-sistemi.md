# Handoff — audit leggero di skill e sistema

## Mandato
Leggere le repository **memory**, **app parquet** e **calendar backup** dell'account Matteo-Exp-Transformer. Identificare pratiche, skill, agent instructions e pattern di workflow già adottati. Raccomandare il **minimo insieme utile** per GPT SOCIAL, ottimizzando rapporto qualità / costo di token / manutenzione / complessità. Non copiare sistemi interi per inerzia.

## Repo target
Matteo-Exp-Transformer/generazione-contenuti-GPT-SOCIAL. Prima leggere README, docs/decisioni.md, docs/PRD-v0.1.md e benchmark FORMA-001. Le repository di riferimento vanno individuate e verificate; non indovinare gli URL se i nomi differiscono.

## Metodo
1. Mappare struttura e file canonici delle tre repo, cercando istruzioni agentiche, skill, handoff, decision log, QA e workflow.
2. Distinguere pratiche effettivamente implementate da idee/documentazione e da componenti specifici di altri progetti.
3. Valutare ogni pratica per beneficio concreto su GPT SOCIAL, costo di contesto, manutenzione, dipendenze e rischio di duplicazione.
4. Proporre un set **minimo** (anche zero skill custom), con alternative scartate e motivazione.
5. Definire percorso incrementale: prima il benchmark manuale, poi automazione solo se i risultati lo giustificano.
6. Consegnare una proposta di struttura e patch minime, senza applicarle prima del consenso.

## Vincoli
- Non generare immagini, non eseguire benchmark, non installare dipendenze, non spendere, non modificare repository senza autorizzazione.
- Non inventare convenzioni di memory o delle altre repo: citare percorsi e commit verificati.
- Nessuna proliferazione di agenti, skill o documenti senza beneficio dimostrato.
- Segnalare incertezze e accessi mancanti.

## Output
Audit sintetico; matrice riuso / adattamento / scarto; architettura minima consigliata; costi operativi stimati qualitativamente; piano di adozione a gate; elenco esatto delle modifiche eventualmente da autorizzare.


## Addendum — incarico specifico a Claude: skill per agente che dirige la chat Android (2026-11-10)

**Ambito:** analisi indipendente, non implementazione. Valutare se e come istruzioni, skill mirate o controlli eseguibili possano rendere piu affidabile un agente che guida l'utente nella direzione creativa di un post sulla **fotografia originale**. Non assumere che una skill risolva limiti delle UI o renda coercitive istruzioni solo testuali. Conservare autonomia nell'analisi: la soluzione puo essere anche **nessuna nuova skill**.

### Fonti da leggere, con priorita
1. `AGENTS.md` e `docs/pilota-foto-diretta-android.md` **Stato operativo**, sezione **G-FOTO-01** e verbali T1/G-UI; riferimento operativo corrente sul branch `docs/g-ui-02-evidence-20261110` (HEAD rilevato al 2026-11-10: `d50e5e8b1befe823bec435345dc9c2c2c1291246`; riverificare).
2. `docs/decisioni.md`, `docs/test-cono-creativo-v01.md` e `docs/audit-run-tattoo-console-guidata-2026-11-10.md`: preferenze visuali, sequenza di scelta, evidenze del salto di fase; distinguere rami/SHAs delle singole prove.
3. `docs/audit-interfacce-native-openai-best-practice-2026-11-10.md`: inventario storico, livelli DOC/OBS/CODE/UNK, superfici UI e limiti. Verificare attualita e applicabilita: non attribuire ad Anthropic/Claude o a ChatGPT API dell'altra piattaforma.
4. `docs/PLAN-skill-system-minimo-2026-11-10.md`, `docs/report-agente-3-verifica-skill-system-2026-11-10.md`, `docs/handoff-agente-sistemi.md`: audit skill gia svolti, costo/beneficio e motivi di zero-patch. Non ripetere ricognizioni senza lacuna concreta.

### Fatti utili, non conclusioni architetturali
- G-UI-01 e G-UI-02-RETEST: controlli/recupero manuale su **preview neutra** confermati dall'utente Android; evidenza indipendente limitata. Renderer 002: 13 test locali PASS, ma trasferimento del **payload Android originale** non verificato; G-UI-02 complessivo PARTIAL.
- T1-01: FAIL procedurale per direzioni/titoli senza anteprime reattive collegate alle scelte; T1-02: FAIL riferito, audit completo non verificato. T0 PARTIAL. Nuovi T1 HOLD.
- G-FOTO-01: solo **proposto/non autorizzato**. Obiettivo: fotografia realmente disponibile, anteprime distinguibili e visibili, approvazione esplicita di A, checkpoint effettivo, cambio **solo titolo** A→B, confronto e verifica di fotografia/ritaglio/layout/altri elementi protetti. Senza asset e composizione realmente modificabili, fermarsi; non sostituire con immagine rigenerata o mockup non equivalente.
- Preview visibile ≠ artefatto modificabile; conferma utente ≠ verifica pixel; recupero manuale ≠ Undo versionato/persistenza/cold recovery. Provenienza di foto e checkpoint va provata al livello disponibile, senza inventare SHA o telemetria.
- `AGENTS.md` richiede fonti canoniche, separazione fatti/proposte, autorizzazioni specifiche, passaggio di consegna e nessun push su main senza approvazione.

### Domande aperte per Claude
Individuare il **minimo meccanismo concretamente applicabile** che aiuti l'agente a rispettare fasi, autorizzazioni, vincoli delle modifiche, fedelta dello stato e qualificazione delle prove, senza trasformare l'esperienza creativa in un questionario. Separare: (a) comportamento ottenibile con istruzioni e checklist; (b) controlli verificabili/validazioni e stop automatici possibili solo con strumenti e accessi appropriati; (c) garanzie oggi impossibili. Confrontare costo di contesto, manutenzione, portabilita fra modelli, fallimenti residui e metodo minimo di valutazione. Indicare un solo prossimo esperimento discriminante, non avviarlo.

### Prompt di avvio per Claude
> Esegui un audit indipendente sulla necessita di skill/controlli per l'agente che dirige il pilota fotografico GPT SOCIAL in ChatGPT Android. Repo: https://github.com/Matteo-Exp-Transformer/generazione-contenuti-GPT-SOCIAL ; parti da `docs/g-ui-02-evidence-20261110`, verifica HEAD, leggi `AGENTS.md` e le fonti prioritarie di questo addendum in `docs/handoff-agente-sistemi.md`. Valuta liberamente i meccanismi minimi per far rispettare sequenza UX, approvazioni, modifiche mirate, evidenze e stop condition, separando regole testuali da enforcement tecnico reale e limiti di piattaforma. Usa solo fatti verificabili, esplicita trade-off, alternativa zero-skill e un esperimento di validazione. Non eseguire il pilota, non modificare codice/schema/renderer/roadmap, non creare PR o merge; T1 HOLD. Consegna una proposta concreta, eventuali patch da autorizzare e chiudi secondo `AGENTS.md`.

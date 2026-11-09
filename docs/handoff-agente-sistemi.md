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

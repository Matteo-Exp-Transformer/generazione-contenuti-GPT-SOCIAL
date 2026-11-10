# STATO — aggiornato 2026-11-10 dal Costruttore
Obiettivo: dirigere un post sulla propria foto senza perdere le scelte approvate.
Mandato attivo: [MANDATO-001](docs/mandato-001-strada-unica.md).
Direzione: revisione Claude recepita dal mandato + decisioni esplicite dell'utente; lo storico non riapre strade superate.

## Gate
- F0 Consolidamento: PARTIAL — [PR #15](https://github.com/Matteo-Exp-Transformer/generazione-contenuti-GPT-SOCIAL/pull/15) merged, PR #11 integrata, tutti i 6 branch docs (incluso #14) e F0 eliminati; 16 archivi byte-identici, 52 righe iniziali AGENTS+STATO, link operativi verdi. Restano 25 rimandi storici locali non risolvibili, mappati nell'[indice](docs/archivio/README.md); non è PASS globale «nessun rimando rotto».
- F1-A Engine: PASS test sintetici locali — 18 test verdi, Python 3.13.7/Pillow 12.1.1, titolo A→B→A, schema chiuso, CLI/import del file isolato; [PR #16](https://github.com/Matteo-Exp-Transformer/generazione-contenuti-GPT-SOCIAL/pull/16) con output reale. Esecuzione effettiva in ChatGPT non provata; diff e test verificati dall’orchestratore, integrazione tramite PR #16.
- F1-A Strada A (TU-01): NON ESEGUITO — foto reale, conferma Android senza download, voto utente, minuti/turni, costo e ripresa reale da raccogliere entro 13/11. I test sintetici non sono il PASS di TU-01.
- F1-B Sonda MCP (TU-01): OPZIONALE, NON AVVIATA — run separata attivabile dall'utente in parallelo, entro 13/11; non è una terza delega.
- Gate D: IN ATTESA — decisione dell'utente sulle schede TU-01, 13/11, revisore una volta.
- F2 Pilota prodotto: HOLD — dopo Gate D, un post reale entro 17/11. T1 HOLD fino al Gate D.

## Prossimo passo (uno)
Regista, nuova chat ChatGPT — seguire [skill post-director](skills/post-director/SKILL.md), caricare engine e foto autorizzata dall'utente, eseguire TU-01 del mandato e consegnare la scheda con misure reali per Gate D — entro 13/11. Foto/PNG in repo solo con autorizzazione; post.json di ogni approvazione da consegnare al Costruttore.

## Ultimo passaggio
- Chi/quando: Costruttore + orchestratore, 2026-11-10; completati i 2/2 task delegati, nessuna delega extra.
- Fatto: F0 integrato e branch conclusi eliminati; engine Pillow in un file, schema skill con rettangoli opzionali, test sintetici e istruzioni ChatGPT; skill v0 invariata.
- Prove: PR #14 e #15 merged; PR #16 con diff/output completo e verifica indipendente dell’orchestratore; 18 test sintetici locali verdi, A finale identico ad A iniziale; nessuna foto reale usata.
- Aperto/bloccato: 25 rimandi storici locali; TU-01 reale, Android/qualità e Gate D aperti.
- Serve dall'utente: nuova chat del regista con foto autorizzata, titoli A/B e palette prima del test, conferme Android, voto 1–5 e minuti attivi effettivi.

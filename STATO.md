# STATO — aggiornato 2026-11-11 dal Technical Investigator
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
Unico esperimento proposto, da avviare in una nuova chat: esportazione manuale e recupero del checkpoint sintetico Canva `DAHalgNO4BY`, con conferma inline Android. Procedura e limiti nell'[audit](evidence/canva-capabilities/audit-2026-11-11.md#7-unico-prossimo-esperimento-necessario-consegna-e-ripresa-del-checkpoint-sintetico). Nessun nuovo TU-01, nessuna foto reale, nessun Gate D.
Le righe Gate sopra sono ereditate da main e non riconciliate dalle altre chat: PR #22 e sonda Canva sui branch separati restano evidenze/proposte non integrate. Il precedente prossimo passo TU-01 non va rieseguito per questa indagine.

## Ultimo passaggio
- Chi/quando: Technical Investigator / Product QA, 2026-11-11; branch `evidence/canva-capabilities-20261111`, da main `695769d8`.
- Fatto: audit separato autorizzato; import HTML sintetico, editing testo/media, preview reale scaricata, resize su copia e riapertura nella stessa chat verificati; tutti i draft annullati.
- Prove: [audit e matrice](evidence/canva-capabilities/audit-2026-11-11.md), 43 tool inventariati, risposte ripulite e PNG sintetici; pixel esterni al titolo invariati a 480×600, non export 1080×1350.
- Aperto/bloccato: export non esposto; font family/nuovi testi/forme/z-order non esposti nell'editing; integrità foto reale, commit, inline Android e nuova sessione non verificati. Nessun PASS end-to-end, nessun merge.
- Serve dall'utente: per il solo esperimento proposto, export manuale del checkpoint sintetico e conferma Android; nessuna nuova scelta creativa. Raccomandazione Canva assistito, non decisione di prodotto.

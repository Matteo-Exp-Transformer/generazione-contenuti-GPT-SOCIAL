# STATO — aggiornato 2026-11-10 dal Costruttore
Obiettivo: dirigere un post sulla propria foto senza perdere le scelte approvate.
Mandato attivo: [MANDATO-001](docs/mandato-001-strada-unica.md).
Direzione: revisione Claude recepita dal mandato + decisioni esplicite dell'utente; lo storico non riapre strade superate.

## Gate
- F0 Consolidamento: PARTIAL — [PR #15](https://github.com/Matteo-Exp-Transformer/generazione-contenuti-GPT-SOCIAL/pull/15) merged, PR #11 integrata, tutti i 6 branch docs (incluso #14) e F0 eliminati; 16 archivi byte-identici, 52 righe iniziali AGENTS+STATO, link operativi verdi. Restano 25 rimandi storici locali non risolvibili, mappati nell'[indice](docs/archivio/README.md); non è PASS globale «nessun rimando rotto».
- F1-A Engine: PASS test sintetici locali — 18 test verdi, Python 3.13.7/Pillow 12.1.1, titolo A→B→A, schema chiuso, CLI/import del file isolato; [PR #16](https://github.com/Matteo-Exp-Transformer/generazione-contenuti-GPT-SOCIAL/pull/16) con output reale. Esecuzione effettiva in ChatGPT non provata; diff e test verificati dall’orchestratore, integrazione tramite PR #16.
- F1-A Strada A (TU-01): NON ESEGUITO — foto reale, conferma Android senza download, voto utente, minuti/turni, costo e ripresa reale da raccogliere entro 13/11. I test sintetici non sono il PASS di TU-01.
- F1-B Sonda MCP (TU-01): BLOCCATA prima della sonda — verifica 11/11 in ChatGPT Work: Canva e Figma presenti nel catalogo ma installed=false, nessuna operazione MCP esposta; autenticazione non verificata. [Schede e prove](evidence/tu-01-mcp/discovery-20261111.json). Nessun TU-01 eseguito, nessun FAIL tecnico attribuito.
- Gate D: IN ATTESA — decisione dell'utente sulle schede TU-01, 13/11, revisore una volta.
- F2 Pilota prodotto: HOLD — dopo Gate D, un post reale entro 17/11. T1 HOLD fino al Gate D.

## Prossimo passo (uno)
Regista, nuova chat ChatGPT — seguire [skill post-director](skills/post-director/SKILL.md), caricare engine e foto autorizzata dall'utente, eseguire TU-01 del mandato e consegnare la scheda con misure reali per Gate D — entro 13/11. Foto/PNG in repo solo con autorizzazione; post.json di ogni approvazione da consegnare al Costruttore.

## Ultimo passaggio
- Chi/quando: Costruttore F1-B, 2026-11-11; sessione separata autorizzata dall'utente, senza deleghe.
- Fatto: lette le quattro fonti richieste su main 695769d8; verificati catalogo e strumenti esposti per Canva/Figma; nessuna installazione, foto o prova grafica.
- Prove: evidence/tu-01-mcp/ — discovery non fotografica e due schede TU-01 non eseguite; branch evidence/f1-b-mcp-20261111, PR senza merge.
- Aperto/bloccato: F1-B bloccata perché entrambi i plugin risultano non installati; non è un semplice collegamento presente da autorizzare. Esiti F1-A e altri gate sopra preservati.
- Serve dall'utente: decidere come rendere disponibile un connettore nel rispetto del divieto di installazioni; poi foto autorizzata e consenso specifico al trasferimento, titoli A/B e palette. Nessuna proroga automatica oltre 13/11.

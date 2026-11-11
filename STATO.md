# STATO — aggiornato 2026-11-10 dal Costruttore
Obiettivo: dirigere un post sulla propria foto senza perdere le scelte approvate.
Mandato attivo: [MANDATO-001](docs/mandato-001-strada-unica.md).
Direzione: revisione Claude recepita dal mandato + decisioni esplicite dell'utente; lo storico non riapre strade superate.

## Gate
- F0 Consolidamento: PARTIAL — [PR #15](https://github.com/Matteo-Exp-Transformer/generazione-contenuti-GPT-SOCIAL/pull/15) merged, PR #11 integrata, tutti i 6 branch docs (incluso #14) e F0 eliminati; 16 archivi byte-identici, 52 righe iniziali AGENTS+STATO, link operativi verdi. Restano 25 rimandi storici locali non risolvibili, mappati nell'[indice](docs/archivio/README.md); non è PASS globale «nessun rimando rotto».
- F1-A Engine: PASS test sintetici locali — 18 test verdi, Python 3.13.7/Pillow 12.1.1, titolo A→B→A, schema chiuso, CLI/import del file isolato; [PR #16](https://github.com/Matteo-Exp-Transformer/generazione-contenuti-GPT-SOCIAL/pull/16) con output reale. Esecuzione effettiva in ChatGPT non provata; diff e test verificati dall’orchestratore, integrazione tramite PR #16.
- F1-A Strada A (TU-01): NON ESEGUITO — foto reale, conferma Android senza download, voto utente, minuti/turni, costo e ripresa reale da raccogliere entro 13/11. I test sintetici non sono il PASS di TU-01.
- F1-B Sonda MCP (TU-01): BLOCKED in ChatGPT — Canva e Figma disponibili nel catalogo ma non installati/collegati; nessuna operazione MCP né misura TU-01 eseguita. Scheda su branch F1-B in evidence/tu-01-mcp/; possibile disponibilità in Claude Code non testata. Entro 13/11, nessuna proroga automatica.
- Gate D: IN ATTESA — decisione dell'utente sulle schede TU-01, 13/11, revisore una volta.
- F2 Pilota prodotto: HOLD — dopo Gate D, un post reale entro 17/11. T1 HOLD fino al Gate D.

## Prossimo passo (uno)
Regista, nuova chat ChatGPT — seguire [skill post-director](skills/post-director/SKILL.md), caricare engine e foto autorizzata dall'utente, eseguire TU-01 del mandato e consegnare la scheda con misure reali per Gate D — entro 13/11. Foto/PNG in repo solo con autorizzazione; post.json di ogni approvazione da consegnare al Costruttore.

## Ultimo passaggio
- Chi/quando: Costruttore F1-B, 2026-11-11; sessione separata, nessuna delega.
- Fatto: discovery di Canva e Figma in ChatGPT; entrambi non installati; bloccata la sonda senza sostituti browser, foto o installazioni; nessuna modifica a F1-A.
- Prove: evidence/tu-01-mcp/sonda-disponibilita-20261111.md sul branch F1-B; sette misure segnate non eseguite, costo €0 sostenuto nella sonda.
- Aperto/bloccato: operazioni MCP e TU-01 non testate; Strada A resta indipendente; Gate D in attesa, nessun confronto inventato.
- Serve dall'utente: decidere se autorizzare un collegamento Canva/Figma nell'ambiente adatto; solo dopo richiedere foto e consenso al trasferimento, oppure chiudere F1-B entro 13/11.

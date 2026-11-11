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
Completare nella chat corrente l'unico esperimento sul checkpoint sintetico `DAHalgNO4BY`: raccogliere conferme separate apertura link e visibilità inline Android; acquisire il file originale PNG 1080×1350 come allegato documento/file. L'immagine ricevuta è JPEG 1229×1536 malgrado il nome .png: non prova l'export richiesto; causa della trasformazione non accertata. Nessun ridimensionamento o conversione per simulare il risultato. Ripresa in nuova sessione già verificata. [Procedura audit §7](evidence/canva-capabilities/audit-2026-11-11.md#7-unico-prossimo-esperimento-necessario-consegna-e-ripresa-del-checkpoint-sintetico). Non ripetere TU-01, nessuna foto reale, nessun Gate D.
Le righe Gate sopra sono ereditate da main e non riconciliate dalle altre chat: PR #22 e sonda Canva sui branch separati restano evidenze/proposte non integrate.

## Ultimo passaggio
- Chi/quando: accompagnamento esperimento checkpoint sintetico, 2026-11-11; branch `evidence/canva-capabilities-20261111`.
- Fatto: recupero del design in nuova chat verificato e ispezione annullata senza modifiche; acquisita l'immagine allegata, letti formato/dimensioni/hash; prima anteprima Markdown fallita su Android; riprovata emissione diretta dello stesso file tramite output immagine, senza ritocchi.
- Prove: pagina Canva 1080×1350, testi iniziali confermati; allegato `Synthetic capability probe.png` decodificato JPEG 1229×1536, 61689 byte; SHA-256 `e2d449ae8ab8b7abfb7f10ac33eba8a230ee271f875de17ee3fb0665cd7c2fa2`.
- Aperto/bloccato: export PNG originale 1080×1350 non acquisito; origine della difformità non accertata; apertura link non confermata; prima anteprima Markdown assente su Android secondo utente e screenshot. Nessun PASS complessivo; commit di revisioni e integrità foto reale fuori perimetro.
- Serve dall'utente: confermare separatamente apertura link e visibilità del nuovo output immagine; inviare il PNG originale 1080×1350 come documento/file anziché come immagine, se disponibile.

# STATO — aggiornato 2026-11-11 dal Costruttore
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
Test conversazionale richiesto dall'utente: scelte creative prima del render, composizione e anteprima dallo stesso progetto Canva. Usare il prompt sotto e la skill aggiornata su questo branch; risultati da riportare dall'utente. Non ripetere TU-01 né anticipare Gate D.
Le righe Gate sopra restano quelle registrate su main; questa modifica non riconcilia le evidenze delle altre chat e non ne certifica gli esiti.

## Ultimo passaggio
- Chi/quando: Costruttore, 2026-11-11; correzione minima richiesta dall'utente.
- Fatto: preparazione creativa obbligatoria e vincolo Canva nella skill; prompt unico conservato qui.
- Prove: rilettura remota dei testi e controllo dei limiti di righe; nessun test creativo eseguito.
- Aperto/bloccato: efficacia conversazionale e visibilità Android da verificare nel test utente; gate invariati.
- Serve dall'utente: avviare la chat con il prompt seguente e riportarne i risultati.

## Prompt unico — test scelte prima / Canva
```text
Agisci come Regista post.
Repo: https://github.com/Matteo-Exp-Transformer/generazione-contenuti-GPT-SOCIAL
Branch: fix/post-director-scelte-prima-canva.
Leggi AGENTS.md, STATO.md, il mandato attivo e skills/post-director/SKILL.md su questo branch. Se non puoi leggerli, fermati.

Conduci il test conversazionale descritto in STATO.md. Prima di creare immagini, concorda con me formato, impaginazione e posizione degli elementi, palette, tipografia, testi ed effetti. Una domanda per turno, due opzioni concrete quando utili; riusa ciò che ho già deciso. Riepiloga le scelte e attendi la mia approvazione esplicita.

Solo dopo componi il post in Canva. Mostra esclusivamente anteprime/esportazioni dello stesso progetto Canva che modificherai e consegnerai. Non usare ImageGen né mockup separati; preserva la foto originale. Se Canva o la sua anteprima non sono disponibili, dichiaralo e fermati senza sostituzioni.

Non ripetere TU-01, non modificare la repo e non anticipare Gate D. Inizia dalla prima scelta mancante, senza generare immagini.
```

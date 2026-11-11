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
Test conversazionale eseguito e registrato sotto: progettazione approvata ma produzione Canva non completata. Prossimo passo del Costruttore: verificare una pipeline concreta di composizione/editabilità/export/anteprima sul medesimo progetto prima di proporre un nuovo test creativo. Non ripetere TU-01 né anticipare Gate D.
Le righe Gate sopra restano quelle registrate su main; questa modifica non riconcilia le evidenze delle altre chat e non ne certifica gli esiti.

## Audit test conversazionale Canva — 2026-11-11
- **Perimetro:** prova distinta da TU-01, nessun Gate D; conversazione su post handpan bambini Bologna, foto utente, previa approvazione integrale. Nessun costo, minuto, voto o conteggio turni misurato come prova TU-01.
- **PASS — Procedura:** letti AGENTS, STATO, MANDATO-001, skill sul branch; formato 4:5 (1080×1350), layout E «onde della musica», palette B (#8FD3D1, #F7E7A8, #B998E8, #30475E), tipografia B elegante, testi A poetici, effetti A onde incantate. Approvazione esplicita dell'utente prima di chiamare Canva. Nessun ImageGen; schemi SVG e campioni colore non erano render Canva.
- **Testi approvati:** «Un mondo di suoni da scoprire»; «Un viaggio tra musica, gioco e meraviglia.»; «Lezioni di handpan per bambini»; «Con Matteo · Bologna»; «Su appuntamento · 327 334 7037».
- **PASS — Accesso tecnico Canva:** trovata bozza precedente **DAHalgBPGjk**, [edit](https://www.canva.com/d/Bk2aGnfGVY6Lf-t); pagina 1080×1350, tre testi modificabili e fill fotografico asset **MAHalj9Scys** (1144×1536, import riuscito). Non prova identità pixel con originale.
- **NON ESEGUITO:** nessuna modifica grafica salvata, nessuna decorazione/onda creata, nessun PNG finale, nessuna anteprima della nuova composizione. Transazione di sola ispezione **393460883562540677** annullata; bozza preesistente non modificata.
- **NON VERIFICATO:** export Canva completo ad alta risoluzione nell'interfaccia strumenti disponibile; preservazione pixel; capacità di creare onde vettoriali/livelli completi; anteprima inline Android; qualità effettiva; ripresa in nuova chat.
- **Limite osservato:** strumenti Canva espongono editing di testo, formattazione, posizione, dimensione, fill e asset, ma non è stata trovata un'operazione di esportazione PNG del progetto né una composizione vettoriale generale. Un render esterno, anche se tecnicamente possibile con foto sorgente, sarebbe raster e non la stessa revisione editabile Canva.
- **Valutazione:** PASS raccolta e blocco scelte; PARTIAL integrazione/lettura Canva; FAIL consegna. Niente PASS TU-01 o Gate D. Distinguere capacità non trovata da impossibilità assoluta.
- **Raccomandazione:** prima di un'altra intervista creativa provare capacità end-to-end (foto originale accessibile, forme/decorazioni, export, preview Android) su un flusso che garantisca stesso progetto e modificabilità; altrimenti chiarire il trade-off editor Canva vs PNG compositato fuori Canva.

## Ultimo passaggio
- Chi/quando: Regista post, 2026-11-11, audit richiesto dall'utente.
- Fatto: registrato audit del test scelte-prima/Canva, senza introdurre un nuovo file audit.
- Prove: ID Canva, asset, transazione annullata; scelte approvate in chat; nessun output grafico conclusivo.
- Aperto/bloccato: composizione, export, anteprima Android e livello di editabilità non verificati; gate invariati.
- Serve dall'utente: nessuna nuova scelta creativa; prossimo intervento tecnico del Costruttore.

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

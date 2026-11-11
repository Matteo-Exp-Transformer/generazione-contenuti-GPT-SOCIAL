# STATO — aggiornato 2026-11-11 dal Costruttore
Obiettivo: dirigere un post sulla propria foto senza perdere le scelte approvate.
Mandato attivo: [MANDATO-001](docs/mandato-001-strada-unica.md).
Direzione: revisione Claude recepita dal mandato + decisioni esplicite dell'utente; lo storico non riapre strade superate.

## Gate
- F0 Consolidamento: PARTIAL — [PR #15](https://github.com/Matteo-Exp-Transformer/generazione-contenuti-GPT-SOCIAL/pull/15) merged; 16 archivi byte-identici, 25 rimandi storici locali non risolvibili mappati nell'[indice](docs/archivio/README.md); non PASS globale.
- F1-A Engine: PASS test sintetici locali — 18 test verdi, Python 3.13.7/Pillow 12.1.1, titolo A→B→A, schema chiuso, CLI/import del file isolato; [PR #16](https://github.com/Matteo-Exp-Transformer/generazione-contenuti-GPT-SOCIAL/pull/16). I test sintetici non costituiscono TU-01.
- F1-A Strada A (TU-01): PARTIAL — prova reale dell'11/11 recuperata dalla chat pilota. Renderer Pillow: A→B→A esatto e pixel esterni all'area titolo invariati nella prova tecnica; visualizzazione Android confermata dall'utente dopo iniziale assenza di anteprima. Esperienza creativa insoddisfacente: fascia viola rifiutata, titolo troppo grande/vuoto, sottotitolo sui capelli. Un tentativo di generazione immagine ha violato la procedura di preservazione fotografica/layer modificabili: non confonderlo con il render tecnico. Utente ha fermato la prova; voto numerico, minuti attivi, costo effettivo e ripresa cross-session non verificati. Non ripetere TU-01 e non dichiarare PASS.
- F1-B Sonda MCP (TU-01): PARTIAL — [PR #19](https://github.com/Matteo-Exp-Transformer/generazione-contenuti-GPT-SOCIAL/pull/19) come evidenza non integrata. Canva: foto importata, design e layer editabili; anteprima **inline ChatGPT Android non visibile**, link esterno visibile. Non eseguiti B→A, export PNG finale, hash e ripresa. Figma: testo A→B→A via MCP, ma foto non importata per blocco DNS; export solo canvas senza foto. Nessun PASS fotografico.
- Gate D: IN ATTESA — non anticipare decisione o revisore prima delle schede TU-01 della Strada A e della valutazione utente; riferimento 13/11.
- F2 Pilota prodotto: HOLD — dopo Gate D, un post reale entro 17/11. T1 HOLD fino al Gate D.

## Prossimo passo (uno)
Costruttore — consolidare la scheda effettiva Strada A nel registro canonico, confrontarla documentalmente con F1-B ([PR #19](https://github.com/Matteo-Exp-Transformer/generazione-contenuti-GPT-SOCIAL/pull/19)), senza ripetere test né iniziare Gate D. Attendere la decisione esplicita dell'utente sulla direzione, con i limiti non misurati dichiarati. Nessuna foto/PNG in repo senza autorizzazione.

## Ultimo passaggio
- Chi/quando: Costruttore, 2026-11-11; recuperati i risultati della chat pilota Strada A e verificati main e PR #19/#20.
- Fatto: classificato TU-01 Strada A PARTIAL, distinto PASS tecnico Pillow dall'insoddisfazione creativa e dalla violazione procedurale della generazione immagine; F1-B resta PARTIAL.
- Prove: feedback esplicito utente e resoconto del test nella chat pilota dell'11/11; PR #16 per engine sintetico, PR #19 per MCP. Nessun test rieseguito, nessun voto o tempo inventato.
- Aperto/bloccato: nessun PASS fotografico end-to-end; esiti non confrontabili completamente per misure mancanti; Gate D in attesa, F2/T1 HOLD.
- Serve dall'utente: solo decisione di direzione quando esaminerà le evidenze; non richiedere nuovo TU-01 né attribuire misure non raccolte.

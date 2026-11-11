# STATO — aggiornato 2026-11-11 dal Costruttore
Obiettivo: dirigere un post sulla propria foto senza perdere le scelte approvate.
Mandato attivo: [MANDATO-001](docs/mandato-001-strada-unica.md).
Direzione: revisione Claude recepita dal mandato + decisioni esplicite dell'utente; lo storico non riapre strade superate.

## Gate
- F0 Consolidamento: PARTIAL — [PR #15](https://github.com/Matteo-Exp-Transformer/generazione-contenuti-GPT-SOCIAL/pull/15) merged; 16 archivi byte-identici, 25 rimandi storici locali non risolvibili mappati nell'[indice](docs/archivio/README.md); non PASS globale.
- F1-A Engine: PASS test sintetici locali — 18 test verdi, Python 3.13.7/Pillow 12.1.1, titolo A→B→A, schema chiuso, CLI/import del file isolato; [PR #16](https://github.com/Matteo-Exp-Transformer/generazione-contenuti-GPT-SOCIAL/pull/16). I test sintetici non costituiscono TU-01.
- F1-A Strada A (TU-01): NON CONCLUSO / risultati non acquisiti nella repo — restano da verificare su foto reale le sette misure (§3 mandato), inclusa conferma inline Android, voto, minuti/turni, costo e ripresa, entro 13/11. Nessun PASS attribuito.
- F1-B Sonda MCP (TU-01): PARTIAL — [PR #19](https://github.com/Matteo-Exp-Transformer/generazione-contenuti-GPT-SOCIAL/pull/19) come evidenza non integrata. Canva: foto importata, design e layer editabili; anteprima **inline ChatGPT Android non visibile**, link esterno visibile. Non eseguiti B→A, export PNG finale, hash e ripresa. Figma: testo A→B→A via MCP, ma foto non importata per blocco DNS; export solo canvas senza foto. Nessun PASS fotografico.
- Gate D: IN ATTESA — non anticipare decisione o revisore prima delle schede TU-01 della Strada A e della valutazione utente; riferimento 13/11.
- F2 Pilota prodotto: HOLD — dopo Gate D, un post reale entro 17/11. T1 HOLD fino al Gate D.

## Prossimo passo (uno)
Regista nella chat pilota Strada A — con foto e renderer autorizzati, completare TU-01 secondo [skill post-director](skills/post-director/SKILL.md) e mandato (§3), consegnando PNG, post.json e sette misure con evidenze reali entro 13/11; se bloccato, registrare esito incompleto senza PASS. Costruttore recepisce la scheda in STATO prima di qualsiasi Gate D. Non caricare foto/PNG nella repo senza autorizzazione.

## Ultimo passaggio
- Chi/quando: Costruttore, 2026-11-11; letti AGENTS, STATO, mandato e evidenze PR #19.
- Fatto: registrato F1-B PARTIAL con import Canva e limite anteprima Android; mantenuta separata la Strada A senza anticipare Gate D.
- Prove: PR #19, `evidence/tu-01-mcp/canva-2026-11-11.md` e `sonda-2026-11-11.md`; nessuna nuova prova su foto reale effettuata in questa sessione.
- Aperto/bloccato: Strada A TU-01 ancora da acquisire nel repository; Canva senza inline Android, export finale e undo; Figma senza foto; sette misure non chiuse.
- Serve dall'utente: completare/trasmettere TU-01 Strada A con conferme Android, voto 1–5, minuti/turni effettivi e autorizzazioni puntuali; nessuna decisione Gate D oggi.

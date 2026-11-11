# STATO — aggiornato 2026-11-11 dal Costruttore
Obiettivo: dirigere un post sulla propria foto senza perdere le scelte approvate.
Mandato attivo: [MANDATO-001](docs/mandato-001-strada-unica.md).
Direzione: revisione Claude recepita dal mandato + decisioni esplicite dell'utente; lo storico non riapre strade superate.

## Gate
- F0 Consolidamento: PARTIAL — [PR #15](https://github.com/Matteo-Exp-Transformer/generazione-contenuti-GPT-SOCIAL/pull/15) merged, PR #11 integrata, 6 branch docs e F0 eliminati; 16 archivi byte-identici, link operativi verdi. Restano 25 rimandi storici locali non risolvibili (indice in docs/archivio/README.md).
- F1-A Engine: PASS **solo sintetico** — [PR #16](https://github.com/Matteo-Exp-Transformer/generazione-contenuti-GPT-SOCIAL/pull/16), 18 test verdi, Python 3.13.7/Pillow 12.1.1, A→B→A su fixture; non equivale al PASS di TU-01.
- F1-A Strada A (TU-01 reale): **PARTIAL** — test tecnico di composizione/render riuscito in chat, ma esperienza creativa giudicata insoddisfacente dall'utente. Limiti del renderer su layout, composizione e modifiche puntuali; procedura di preservazione della fotografia violata. L'utente segnala fascia viola indesiderata, titolo troppo grande/vuoto, sottotitolo sovrapposto ai capelli e poco leggibile; desiderava curve sonore giocose e magiche. Nessuna attestazione completa dei criteri 1–7 (§3 mandato): non attribuire PASS a preservazione pixel, undo, qualità, tempi, costo o ripresa senza prove e misure. Test chiuso su richiesta dell'utente, non ripetere.
- F1-B Sonda MCP (TU-01): **separata** — [PR #19](https://github.com/Matteo-Exp-Transformer/generazione-contenuti-GPT-SOCIAL/pull/19) come evidenza: Canva importa la fotografia; l'anteprima inline Android non risulta visibile, pur essendo accessibile dal link secondo il riscontro utente. Non dichiarare PASS né assimilare questo esito alla Strada A. Altri criteri non verificati qui.
- Gate D: **NON SUPERATO** — valutazione con schede e decisione esplicita dell'utente ancora aperte, entro 13/11; nessuna scelta di strada dedotta automaticamente.
- F2 Pilota prodotto: HOLD — dopo Gate D, post reale entro 17/11; T1 HOLD fino al Gate D.

## Prossimo passo (uno)
Costruttore — consolidare le evidenze distinte di TU-01 Strada A (PARTIAL) e PR #19 F1-B, senza nuovi test né modifiche a engine/skill; predisporre per l'utente il quadro dei criteri verificati, falliti e non misurati per la decisione Gate D entro 13/11. Gate D resta aperto e richiede decisione utente.

## Ultimo passaggio
- Chi/quando: Costruttore, 2026-11-11; aggiornamento documentale su branch dedicato.
- Fatto: registrato TU-01 Strada A come PARTIAL, esperienza creativa negativa, limiti renderer e violazione preservazione; distinta PR #19 (F1-B).
- Prove: feedback diretto dell'utente nella chat pilota (fascia viola, titolo, sottotitolo/capelli, richiesta curve sonore); test tecnico riferito come riuscito; per MCP riscontro Android/link e PR #19. Nessun nuovo test eseguito.
- Aperto/bloccato: criteri TU-01 non interamente misurati, verifica completa su PR #19 non svolta in questa run; Gate D non superato, T1/F2 HOLD.
- Serve dall'utente: solo decisione sulla strada al Gate D dopo esame delle evidenze; nessuna ripetizione del test, nessun voto/minuti inventati.

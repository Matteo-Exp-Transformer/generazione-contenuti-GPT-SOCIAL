# STATO — aggiornato 2026-11-11 dal Costruttore (Claude)
Obiettivo: dirigere un post sulla propria foto, preservare le scelte e ottenere una consegna verificabile.
Mandato attivo: [MANDATO-001 aggiornato](docs/mandato-001-strada-unica.md).
Regista in prova: **regista-v1.0** — [SKILL](skills/post-director/SKILL.md) · [avvio unico](skills/post-director/AVVIO.md) · [valutazione e supervisione](skills/post-director/VALUTAZIONE.md).
Direzione: regista conversazionale + Canva; scelta definitiva al Gate D.
Inline Android resta obiettivo; link Canva esterno accettato occasionalmente; nessun ponte Python; nessun ImageGen.

## Gate e prove
- F0: PARTIAL storico (PR #15). F1-A engine: PASS sintetico pregresso (PR #16), engine fuori dalla strada attuale.
- TU-01 Strada A: PARTIAL, chiuso; non ripetere (PR #20/#21 descrivono lo stesso test).
- F1-B sonde Canva/Figma (PR #19), regista scelte-prima (PR #22), capacità Canva in bozza (PR #23): PARTIAL; dettagli audit §§1–9.
- Canale immagini (PR #24/#25): Markdown, GitHub raw e output del connettore non visibili; stessi byte via Python visibili (5/7, riscontro utente); Canva→Python bloccato (DNS). PARTIAL.
- Chat E/F/G (PR #26): copie Canva salvate; anteprime via URL non visibili; multipagina richiesto non eseguito. PARTIAL.
- Campionario font (PR #27): `create_design` 5 pagine; widget Android sfogliabile ed «Edit in Canva» (riscontro utente); famiglia font non certificata. PARTIAL promettente.
- Revisioni di metodo (PR #28) e di architettura (PR #29): verdetto #29 approvato dall'utente; da qui Regista v1.0.
- Gate D: APERTO; nessun PASS end-to-end; F2/T1 HOLD.
- Sezioni delle PR #24–#28 integrate nell'[audit Canva](evidence/canva-capabilities/audit-2026-11-11.md) come «PR #n · §…»; righe decisione integrate. Il loro «prossimo passo» è superato.

## Sequenza verso l'obiettivo
- [x] Consolidare evidenze, skill e stato; diagnosi canale immagini (PARTIAL).
- [x] Revisione architetturale indipendente e pacchetto Regista v1.0 (PR #29).
- [ ] Supervisore: verifica del pacchetto v1.0 e Preparazione (VALUTAZIONE §0) — PROSSIMO PASSO.
- [ ] Giro A (3 chat) e Giro B (3 chat); esiti nel registro; azione secondo VALUTAZIONE §4.
- [ ] Se tutto passa: un post reale con misure U; poi decisione Gate D e pilota F2.

## Decisioni operative già prese dal Costruttore (non serve chiederle)
- PR #24–#28: dopo il merge della PR #29 si chiudono senza merge, con un commento che rimanda a questa PR.
- Il tag `regista-v1.0` è creato sul commit di questa PR: le prove possono partire anche prima del merge; leggibilità via connettore da verificare (VALUTAZIONE V1).
- Una chat senza la prima riga `Regista v1.0` vale come F9 = no, secondo VALUTAZIONE §3–4.
- Il Regista non legge STATO né mandato; i vincoli di cantiere (TU-01, gate) valgono per Costruttore e Supervisore.
- Engine Pillow e test restano nel repo come riferimento storico, non usati dal Regista.

## Prossimo passo (uno)
Supervisore in una chat ChatGPT nuova, con il prompt qui sotto.
1. Verifica il pacchetto v1.0 (VALUTAZIONE §7.1): correzioni bloccanti come testo pronto, oppure via libera.
2. Guida l'utente nella Preparazione §0, poi valuta una per una le chat dei Giri A e B.
Il Supervisore non conduce post e non cambia la skill senza un controllo fallito; applica §4.
Merge della PR #29 su main: solo con ok dell'utente, preferibilmente dopo la verifica del Supervisore.

## Ultimo passaggio
- Chi/quando: Costruttore Claude, 2026-11-11, su richiesta esplicita dell'utente dopo l'approvazione del verdetto PR #29.
- Fatto: skill regista-v1.0 riscritta (80 righe), AVVIO.md prompt unico, VALUTAZIONE.md con prove, controllo nel tempo, premortem e istruzioni del Supervisore; integrate PR #24–#28; AGENTS, mandato e README allineati.
- Prove: righe e link controllati, ricerca di contraddizioni sulla skill con revisione indipendente; nessuna chat Regista eseguita, nessun test prodotto.
- Aperto/bloccato: lettura del tag via connettore GitHub, Canva nei Progetti, export esposto e ripetibilità del widget non verificati; Gate D aperto.
- Serve dall'utente: avviare il Supervisore; poi fare le 6 chat di prova seguendo i suoi passi.

## Prompt di prosecuzione — Supervisore (chat ChatGPT nuova)
Sei il Supervisore test di GPT SOCIAL. Dal repo GitHub Matteo-Exp-Transformer/generazione-contenuti-GPT-SOCIAL,
branch review/architettura-fedelta-regista-20261111 (se già unito: main), leggi AGENTS.md, STATO.md e
skills/post-director/VALUTAZIONE.md, poi SKILL.md e AVVIO.md. Segui VALUTAZIONE §7: prima verifica il pacchetto,
poi guidami nella Preparazione e valuta le chat di prova che ti porterò. Non fare il Regista. Chiudi secondo AGENTS.md.

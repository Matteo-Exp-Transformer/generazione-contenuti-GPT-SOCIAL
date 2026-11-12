# STATO — aggiornato 2026-11-12 dal Costruttore (Claude)
Obiettivo: dirigere un post sulla propria foto, preservare le scelte e ottenere una consegna verificabile.
Mandato attivo: [MANDATO-001 aggiornato](docs/mandato-001-strada-unica.md).
Regista in uso: **regista-v1.0** su main — [SKILL](skills/post-director/SKILL.md) · [avvio](skills/post-director/AVVIO.md) · [valutazione](skills/post-director/VALUTAZIONE.md).
Repo: un solo branch stabile, `main` (decisione utente 2026-11-12). Versione della skill = riga `version:` di SKILL.md.
Direzione: regista conversazionale; **esplorazione con campionari deterministici in chat, Canva per comporre**; Gate D aperto.
Inline Android resta obiettivo; link Canva esterno accettato occasionalmente; nessun ImageGen; Python mai sulla foto.

## Gate e prove
- F0: PARTIAL storico (PR #15). F1-A engine: PASS sintetico pregresso (PR #16), engine fuori dalla strada attuale.
- TU-01 Strada A: PARTIAL, chiuso; non ripetere.
- F1-B, capacità Canva, canale immagini, chat E/F/G, campionario font (PR #19–#28): PARTIAL; sintesi nell'[audit Canva](evidence/canva-capabilities/audit-2026-11-11.md).
- Revisione architetturale e pacchetto Regista v1.0 (PR #29): unita su main il 2026-11-12.
- Prove v1.0 dell'11/11: R1, R2, R3 naturalistiche, **nessuna vale per pass^3**; Giri A/B 0/6 ([registro](skills/post-director/VALUTAZIONE.md), [evidenze](evidence/regista-v1/)).
- Quota IA Canva Free esaurita l'11/11 (R3 `quota_exceeded`): blocca `create_design` fino al rinnovo.
- Revisione indipendente serale: [commento PR #29](https://github.com/Matteo-Exp-Transformer/generazione-contenuti-GPT-SOCIAL/pull/29#issuecomment-6807087310) — diagnosi, alternative, piano P0–P3.
- Kit campionari v1 ([campionari/](campionari/)): 4 fogli generati in locale senza crediti ([prove](evidence/campionari/)); **non ancora provato in ChatGPT**.
- Gate D: APERTO; nessun PASS end-to-end; F2/T1 HOLD.

## Sequenza verso l'obiettivo
- [x] Pacchetto Regista v1.0, revisione indipendente, kit campionari, merge e pulizia dei branch.
- [ ] **P0 + micro-test T-F1, T-F2, T-F3** ([VALUTAZIONE §0b](skills/post-director/VALUTAZIONE.md)) — PROSSIMO PASSO.
- [ ] Costruttore: applica gli esiti di §0b (lista bianca nei font, eventuale v1.1 di una sola sezione).
- [ ] Preparazione §0, poi Giri A e B sulla versione risultante; esiti nel registro; azione secondo §4.
- [ ] Se tutto passa: un post reale con misure U; poi decisione Gate D e pilota F2.

## Decisioni operative già prese (non serve chiederle)
- PR #24–#28 chiuse senza merge; i loro contenuti sono nell'audit Canva. Branch eliminati dopo il merge di #29.
- Il branch `regista-v1.0` è stato eliminato: SKILL.md su main è identico (blob `5ee452eb`); i resoconti che conteneva sono in `evidence/regista-v1/`.
- Una chat Regista non scrive mai nel repo: i resoconti si incollano al Supervisore o in un commento di PR.
- Il kit si usa solo per esplorare; ogni foglio porta «SIMULAZIONE»; la famiglia del font la certifica l'utente toccando il testo in Canva.
- Esiti dei micro-test → azioni già scritte nella tabella di VALUTAZIONE §0b.
- Engine Pillow e test restano nel repo come riferimento storico, non usati dal Regista.

## Prossimo passo (uno)
Supervisore in una chat ChatGPT nuova (prompt qui sotto): guida l'utente in P0 e nei micro-test §0b, applica la tabella
degli esiti e consegna le righe di registro. Cosa aspettarsi: circa 45 minuti dell'utente; 3 chat brevi per T-F1 con lo zip
allegato (scaricato da `campionari/kit-campionari-v1.zip`), 15 minuti nell'app Canva per T-F2, una chat con Canva per T-F3.
Poi il Costruttore registra gli esiti e, se previsto, scrive la v1.1 in una sola PR.

## Ultimo passaggio
- Chi/quando: Costruttore Claude, 2026-11-12, su autorizzazione esplicita dell'utente («procedi», merge, un solo branch).
- Fatto: kit campionari v1 (script, 14 famiglie OFL, esempi, test); VALUTAZIONE §0b con micro-test ed esiti già decisi; AVVIO su main con controllo `version:`; AGENTS allineato; R1/R3 in evidence; merge PR #29; PR #24–#28 chiuse; branch eliminati.
- Prove: `python -m unittest discover -s tests/campionari -v` e `tests/engine` verdi; fogli in `evidence/campionari/`; skill invariata.
- Aperto/bloccato: quota IA Canva; fogli in Python ChatGPT, lista bianca Canva e arrivo del font in Canva non verificati.
- Serve dall'utente: leggere il contatore IA di Canva e fare i micro-test con il Supervisore.

## Prompt di prosecuzione — Supervisore (chat ChatGPT nuova)
Sei il Supervisore test di GPT SOCIAL. Dal repo GitHub Matteo-Exp-Transformer/generazione-contenuti-GPT-SOCIAL,
branch main, leggi AGENTS.md, STATO.md e skills/post-director/VALUTAZIONE.md (§0b e §7). Non fare il Regista e non
scrivere nel repo. Guidami un passo alla volta in P0 e nei micro-test T-F1, T-F2, T-F3; per ogni test dimmi cosa fare,
cosa devo vedere e annota l'esito. Alla fine applica la tabella degli esiti di §0b e dammi le righe per il registro §8
e un prompt per il Costruttore. Fatti, ipotesi e proposte distinti; mai un PASS non visto. Chiudi secondo AGENTS.md.

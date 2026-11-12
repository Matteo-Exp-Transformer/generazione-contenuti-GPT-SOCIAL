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

## Review PM · 2026-11-12 (proposta, nessun nuovo PASS)
- **Verdetto:** prototipo sperimentale, non pronto al rilascio; Gate D resta aperto. Salute repository discreta per tracciabilità, prodotto fragile per ripetibilità e consegna.
- **Acquisito:** separazione Regista/Costruttore/Supervisore; SKILL v1.0 e controlli F/U; import e editing Canva su fixture; widget Android osservato in almeno una sessione; kit deterministico locale e test sintetici. Nessuno equivale a end-to-end.
- **Non certificato:** foto originale immutata fino all'export; corrispondenza scelta→composizione; font effettivo; anteprime ripetibili su Android; modifica circoscritta salvata e ripresa; export pubblicabile. R1–R3 non danno pass^3.
- **Nuovi segnali da chat utente 12/11, da verificare in registro:** interesse per più layout/palette e input libero; insufficienza di scelte A/B; campionario chiesto realmente visibile; prove Canva e limiti quota/tool variabili. Non trasformare resoconti in PASS.
- **Rischio di coerenza:** VALUTAZIONE §0b prevede fogli Python/PNG mentre SKILL regola 5 nega «ponte via Python»; chiarire *esplorazione simulata* vs *render finale*, prima di v1.1. §0b T-F3 import HTML e fallback template sono ipotesi, non capacità certificate su tutti i client.
- **P0 product:** matrice evidenze per capacità, provenienza, modello/client, quota, costo e stato (provato/negativo/non testato); distinguere tool esposto da risultato utente visibile.
- **P1 UX:** 5–9 alternative per campionari, scelta libera o combinata, preview inline etichettate «SIMULAZIONE»; definire criterio di accettazione, non imporre ancora nella skill.
- **P1 delivery:** percorso minimo unico «brief→scelte→composizione→modifica→readback→consegna» con foto sintetica, consenso e controllo link/export; nessun nuovo giro completo prima del triage.
- **P2:** P0 e T-F1/T-F2/T-F3 di VALUTAZIONE §0b; poi eventuale v1.1 mirata e Giri A/B. Se tool, quota o canale bloccano, registrare impedimento invece di moltiplicare prove equivalenti.
- **Decisione richiesta a revisore indipendente:** contestare anche questa priorità e proporre il più piccolo insieme di prove discriminanti; non modificare automaticamente skill, architettura o main.

## Prossimo passo (uno)
Supervisore in una chat ChatGPT nuova (prompt qui sotto): guida l'utente in P0 e nei micro-test §0b, applica la tabella
degli esiti e consegna le righe di registro. Cosa aspettarsi: circa 45 minuti dell'utente; 3 chat brevi per T-F1 con lo zip
allegato (scaricato da `campionari/kit-campionari-v1.zip`), 15 minuti nell'app Canva per T-F2, una chat con Canva per T-F3.
Poi il Costruttore registra gli esiti e, se previsto, scrive la v1.1 in una sola PR.

## Ultimo passaggio
- Chi/quando: Product Manager GPT SOCIAL, 2026-11-12, review documentale su main e testimonianze test; branch review/pm-stato-prodotto-20261112.
- Fatto: sintesi evidence-based di maturità, rischi UX e priorità prima del ciclo successivo; nessuna modifica a skill, test, asset o decisioni.
- Prove: AGENTS, STATO, MANDATO-001, SKILL, VALUTAZIONE, audit Canva e cronologia PR; nessun nuovo PASS prodotto.
- Aperto/bloccato: fedeltà visuale, campionari Android, quota/tool Canva, font, modifica persistente, export finale.
- Serve dall'utente: confronto ragionato con Claude prima di eventuale approvazione della sequenza e merge della PR.

## Prompt di prosecuzione — Supervisore (chat ChatGPT nuova)
Sei il Supervisore test di GPT SOCIAL. Dal repo GitHub Matteo-Exp-Transformer/generazione-contenuti-GPT-SOCIAL,
branch main, leggi AGENTS.md, STATO.md e skills/post-director/VALUTAZIONE.md (§0b e §7). Non fare il Regista e non
scrivere nel repo. Guidami un passo alla volta in P0 e nei micro-test T-F1, T-F2, T-F3; per ogni test dimmi cosa fare,
cosa devo vedere e annota l'esito. Alla fine applica la tabella degli esiti di §0b e dammi le righe per il registro §8
e un prompt per il Costruttore. Fatti, ipotesi e proposte distinti; mai un PASS non visto. Chiudi secondo AGENTS.md.

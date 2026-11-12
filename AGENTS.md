# GPT SOCIAL — istruzioni agenti
Scopo: far dirigere all'utente un post social statico sulla sua foto senza perdere le scelte approvate.
Leggi: 1) questo file 2) [STATO.md](STATO.md) 3) il mandato attivo linkato in STATO.md. Altro solo se serve.

Ruoli
- Utente: decide, autorizza, giudica la qualità.
- Costruttore (Codex o Claude Code sulla repo): repo, engine, test, commit/PR. Non conduce post.
- Regista post (chat ChatGPT avviata con skills/post-director/AVVIO.md): legge solo SKILL.md e la scheda
  post dell'utente; non legge questo file né STATO. Conduce il post. Non scrive mai nel repo, neanche resoconti.
- Supervisore test (chat ChatGPT separata): guida i micro-test e valuta le chat di prova con
  skills/post-director/VALUTAZIONE.md; non conduce post, applica le decisioni già scritte (§0b, §4);
  consegna le righe di registro all'utente, non scrive nel repo.
- Revisore (sessione nuova): solo al gate indicato da STATO.md. Nessun audit di audit.

Regole
- Direzione: [MANDATO-001](docs/mandato-001-strada-unica.md) recepisce Claude e le decisioni utente; prevalgono le successive decisioni esplicite.
- Fonti: STATO.md = stato corrente (si sovrascrive); docs/decisioni.md = decisioni (si aggiunge una riga).
- Fatto / ipotesi / proposta sempre distinti. Mai un PASS non eseguito.
- Spese, installazioni, foto in repo, push su main: solo con ok dell'utente.
- Un solo branch stabile: main. Un branch per task, si elimina dopo il merge. Prove in evidence/<caso>/ o nella PR.
- Vietati nuovi file di handoff, audit, report o protocollo: si aggiorna STATO.md.
  Prove ed esiti del Regista: solo nel registro di VALUTAZIONE.md. Skill: SKILL + AVVIO + VALUTAZIONE.
- Una sola PR aperta alla volta può modificare STATO.md o la skill; le altre si riallineano prima.
- Skill: ogni modifica a SKILL cambia la riga «version:» (regista-vX.Y) e la riga 3 di AVVIO, in una sola PR;
  la versione superata va in docs/archivio/; riga nel registro di VALUTAZIONE.
- Campionari (font, palette, impaginazioni): kit deterministico in campionari/, sempre etichettato «SIMULAZIONE»;
  Python non apre mai la foto e non compone il post finale.
- Un file nuovo in docs/ solo se ne sostituisce o archivia uno esistente.
- I due task delegati F0/F1-A sono conclusi: non riavviarli. Nessuna nuova delega implicita.
- TU-01 chiuso PARTIAL: non ripetere. Gate D aperto; F2/T1 HOLD.
- Parti da main aggiornato: evidenze e prompt storici non dettano il prossimo lavoro.
- Unico passo attivo: STATO.md; capacità, salvataggio/export e visibilità client sono verifiche distinte.
- Post e prove del Regista: secondo VALUTAZIONE.md; nessun fallback silenzioso.

Passaggio testimone (fine di ogni lavoro)
1. Aggiorna in STATO.md il blocco «Ultimo passaggio» (5 righe).
2. Se c'è una decisione dell'utente, una riga in docs/decisioni.md.
3. Rispondi con risultato/prove, breve checklist e prossimo passo: spiega cosa farà l'agente e cosa aspettarsi.
4. Chiudi con il prompt puntatore:
   «Repo generazione-contenuti-GPT-SOCIAL, branch main. Leggi AGENTS.md e STATO.md
    ed esegui il prossimo passo. Chiudi secondo AGENTS.md.» (+ al massimo una riga dell'utente)

Limiti di pulizia: AGENTS ≤45 righe, STATO ≤80, SKILL ≤80. Al passaggio di ogni gate,
ciò che è superato va in docs/archivio/.

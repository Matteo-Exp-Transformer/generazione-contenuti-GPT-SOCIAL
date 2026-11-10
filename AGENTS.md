# GPT SOCIAL — istruzioni agenti
Scopo: far dirigere all'utente un post social statico sulla sua foto senza perdere le scelte approvate.
Leggi: 1) questo file 2) [STATO.md](STATO.md) 3) il mandato attivo linkato in STATO.md. Altro solo se serve.

Ruoli
- Utente: decide, autorizza, giudica la qualità.
- Costruttore (Codex o Claude Code sulla repo): repo, engine, test, commit/PR. Non conduce post.
- Regista post (chat, skill skills/post-director): conduce il post con l'utente. Non modifica la repo.
- Revisore (sessione nuova): solo al gate indicato da STATO.md. Nessun audit di audit.

Regole
- Direzione: [MANDATO-001](docs/mandato-001-strada-unica.md) recepisce Claude e le decisioni utente; prevalgono le successive decisioni esplicite.
- Fonti: STATO.md = stato corrente (si sovrascrive); docs/decisioni.md = decisioni (si aggiunge una riga).
- Fatto / ipotesi / proposta sempre distinti. Mai un PASS non eseguito.
- Spese, installazioni, foto in repo, push su main: solo con ok dell'utente.
- Un branch per task del mandato; si elimina dopo il merge. Prove in evidence/<caso>/ o nella PR.
- Vietati nuovi file di handoff, audit, report o protocollo: si aggiorna STATO.md.
- Un file nuovo in docs/ solo se ne sostituisce o archivia uno esistente.
- Run MANDATO-001: massimo due deleghe (F0, engine F1-A); limiti e letture al §0-bis.
- T1 HOLD fino al Gate D; test sintetici verdi non sono TU-01. F1-B opzionale e separata.

Passaggio testimone (fine di ogni lavoro)
1. Aggiorna in STATO.md il blocco «Ultimo passaggio» (5 righe).
2. Se c'è una decisione dell'utente, una riga in docs/decisioni.md.
3. Rispondi all'utente in 3 blocchi: Fatto (con prove) · Stato (righe dei gate) · Prossimo passo.
4. Chiudi con il prompt puntatore:
   «Repo generazione-contenuti-GPT-SOCIAL, branch main. Leggi AGENTS.md e STATO.md
    ed esegui il prossimo passo. Chiudi secondo AGENTS.md.» (+ al massimo una riga dell'utente)

Limiti di pulizia: AGENTS ≤45 righe, STATO ≤80, SKILL ≤120. Al passaggio di ogni gate,
ciò che è superato va in docs/archivio/.

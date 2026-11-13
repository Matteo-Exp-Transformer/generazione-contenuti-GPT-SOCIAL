# GPT SOCIAL — istruzioni agenti
Scopo: in ChatGPT (Android prioritario) l'utente dirige un post statico sulla propria foto e riceve un PNG pubblicabile.
Leggi: 1) questo file 2) [STATO.md](STATO.md) 3) [ROADMAP](docs/ROADMAP.md). Altro solo se serve.

Ruoli
- Utente: decide, approva, giudica la qualità, ritocca ed esporta in Canva.
- Costruttore / Direttore (Claude Code o Codex sulla repo): dirige la roadmap un passo alla volta, cura repo, kit, skill,
  registro, commit/PR; scrive i prompt delle chat di prova; dopo ogni passo si consulta con l'utente. Non conduce post.
- Chat di lavoro ChatGPT (Banco di prova, Officina modelli, Regista): eseguono il compito del loro prompt.
  Non scrivono mai nel repo: l'utente incolla al Costruttore resoconti ed esiti.
- Revisore indipendente: solo su richiesta esplicita dell'utente.

Vincoli di prodotto (cambiano solo con decisione esplicita dell'utente)
- Foto originale mai rigenerata o alterata: solo ritaglio, scala, posizione, elementi sopra/sotto.
- Canva = livelli ed elementi (modelli, foto, testi, salvataggio, export). Niente `create_design` per esplorare i post.
- Python = fogli deterministici «SIMULAZIONE», anche con una copia ridotta della foto; mai sull'originale, mai il post finale
  (salvo ripiego C di ROADMAP §5).
- Generazione immagini GPT = solo elementi decorativi separati, come livello Canva. Mai sulla foto né sul post intero.
- Budget incrementale €0. Spese, installazioni, foto in repo, push su main: solo con ok dell'utente.

Regole di lavoro
- Fatto / riferito / ipotesi / proposta sempre distinti. Mai un esito non osservato.
- Fonti: STATO.md = stato corrente (si sovrascrive) · ROADMAP = scope, traguardi, esiti decisi, registro (§8, si aggiunge) ·
  docs/decisioni.md = decisioni dell'utente (si aggiunge una riga).
- Un test si fa una volta; si ripete solo se cambia qualcosa. Gli esiti seguono la tabella ROADMAP §5.
- Un solo branch stabile: main. Un branch per task, eliminato dopo il merge. Una sola PR aperta alla volta su STATO/skill.
- Niente nuovi file di audit, handoff, report o protocollo: si aggiornano STATO, il registro e la PR.
  Nuovi file solo se servono al prodotto (codice, kit, modelli, skill) o sostituiscono un file esistente.
- Skill Regista: SKILL.md + AVVIO.md; ogni modifica cambia `version:` e la riga 3 di AVVIO in una sola PR;
  la versione superata va in docs/archivio/.
- Ciò che è superato va in docs/archivio/ o si cancella (resta nella storia git), con una riga nell'indice dell'archivio.

Passaggio testimone (fine di ogni lavoro)
1. Consultati con l'utente; poi aggiorna «Ultimo passaggio» in STATO.md (5 righe), il registro ROADMAP §8 e la ROADMAP se decisa.
2. Se c'è una decisione dell'utente, una riga in docs/decisioni.md.
3. Rispondi con risultato e prove, cosa resta aperto e il prossimo passo (cosa farà chi, cosa aspettarsi).
4. Chiudi con il prompt puntatore:
   «Repo generazione-contenuti-GPT-SOCIAL, branch main. Leggi AGENTS.md e STATO.md
    ed esegui il prossimo passo. Chiudi secondo AGENTS.md.»

Limiti: AGENTS ≤45 righe, STATO ≤80, SKILL ≤80.

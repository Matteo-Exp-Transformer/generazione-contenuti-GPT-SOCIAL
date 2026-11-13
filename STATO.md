# STATO — aggiornato 2026-11-13 dal Direttore
Obiettivo: dirigere un post sulla propria foto e ricevere un PNG pubblicabile. Scope e traguardi: [ROADMAP](docs/ROADMAP.md).
**Ripristino di progetto del 2026-11-12** (decisione utente): nuovo flusso Officina modelli → chat del post →
bozza Canva da modello → decorazioni come livelli → ritocco ed export. MANDATO-001, PRD v0.1 e VALUTAZIONE v1.0 archiviati.

## Dove siamo
- **M0 Ripristino:** completato; PR #31 unita su `main` il 2026-11-13 ([indice](docs/archivio/README.md)).
- **Regista v1.0** ([SKILL](skills/post-director/SKILL.md)): **sospeso**, non avviare chat Regista. Si riscrive in M3 sul nuovo flusso.
- Kit campionari v1 ([campionari/](campionari/)): B0 chiuso tecnicamente e approvato; foto nei fogli layout/combo, ZIP aggiornato; in ChatGPT non ancora provato.
- Canva: `copy_design` → modifica testi → commit → rilettura osservato il 12/11 anche con quota IA esaurita
  ([evidenza](evidence/canva-template/2026-11-12-copy-edit-commit.md)). Foto nel modello, livelli decorativi ed export: non provati.
- Mai dimostrato finora: un post consegnato end-to-end.

## Sequenza
- [x] **M0** · 21/21 test tecnici superati da Codex; PR #31 unita su main il 13/11.
- [x] **B0** · foto ridotta ≤800 px, SHA-256, fixture sintetica; test indipendenti 5/5, ZIP coerente; PR #32 unita su main il 13/11.
- [ ] **M1** · Banco di prova T0, T1–T4, T6 (+T5 facoltativo), [ROADMAP §6](docs/ROADMAP.md); esiti nel registro §8.
- [ ] **M2** · Officina: 3–5 modelli in [modelli/CATALOGO.md](modelli/CATALOGO.md), via import HTML se T6 passa, altrimenti chat GPT che replicano la struttura via connettore Canva.
- [ ] **M3** · Regista v2: SKILL + AVVIO riscritti; checklist §7.
- [ ] **M4** · Primo post reale consegnato. **M5** · tre post reali, poi decisioni sul parcheggio.

## Decisioni operative già prese (non serve chiederle)
- Fogli di esplorazione con copia ridotta della foto quando possibile; altrimenti riquadro «FOTO» dichiarato.
- Canva da modelli come strada principale; ripiego C (finale via Python sul foglio approvato) solo se T2 fallisce.
- Decorazioni GPT solo come livelli separati; la variante generativa del post intero è parcheggiata.
- Nessun pass^3 o giro di prova ripetuto prima del primo post: la validazione passa dai post reali (M4–M5).
- `create_design` non si usa per esplorare; può servire in Officina per un modello senza foto, con quota letta prima.
- Engine Pillow ([engine/](engine/README.md)) resta come base del ripiego C, non usato altrimenti.

## Prossimo passo (uno)
**M1 da proporre, non autorizzato:** Banco di prova (ROADMAP §6), partendo dalle prerequisiti T0 e T1. Nessuna chat o prova M1 avviata.

## Ultimo passaggio
- Chi/quando: Direttore, 2026-11-13; merge PR #32 e aggiornamenti autorizzati dall'utente.
- Fatto: B0 unito su main (`5caa9f5`); kit fotografico, ZIP e registro aggiornati; nessuna nuova prova di prodotto.
- Prove: [Codex, verifica indipendente](https://github.com/Matteo-Exp-Transformer/generazione-contenuti-GPT-SOCIAL/pull/32#issuecomment-6849167347): 5/5 test, ZIP e SHA verificati su `cdd5fd8`.
- Aperto/bloccato: M1 non autorizzato; contrasto sulla foto non adattivo; branch B0 da eliminare manualmente se presente.
- Serve dall'utente: decisione sulla proposta M1, test utente nelle chat dedicate solo dopo autorizzazione.

## Prompt del Direttore (sessione nuova del Costruttore)
```
Sei il Direttore di GPT SOCIAL: Costruttore con accesso alla repo Matteo-Exp-Transformer/generazione-contenuti-GPT-SOCIAL.
Parti da main aggiornato; se B0 attende il merge, leggi anche la sua PR. Leggi AGENTS.md, STATO.md e
docs/ROADMAP.md; altri file solo se servono al passo. Porti avanti la roadmap un passo alla volta, tieni la repo sana e fedele allo scope.
Ciclo di ogni passo:
1. Proponi il passo successivo: perché, cosa produce, criterio di accettazione, chi fa cosa, minuti miei. Aspetta il mio ok.
2. Esegui solo quel passo, su un branch dedicato. Se serve una chat ChatGPT di prova, scrivi il prompt da incollare
   (cosa allegare, app da attivare, cosa devo osservare, cosa riportarti) e aspetta i miei esiti: non dedurli né inventarli.
3. Verifica: test, link, limiti di righe, coerenza con ROADMAP §1–2; applica la riga pertinente di §5; esito nel registro §8 (F/U/I).
4. Consultati con me: fatto, prove, cosa non torna; proponi l'aggiornamento di ROADMAP e STATO e chiedimi una decisione alla volta.
   Scrivi ROADMAP, STATO e decisioni solo dopo la mia risposta. Merge su main solo con il mio ok.
5. Chiudi secondo AGENTS: ultimo passaggio, PR, branch eliminati dopo il merge, prompt puntatore.
Igiene a ogni passo: una PR alla volta su STATO/ROADMAP/skill; niente file di audit, report o handoff; ciò che è superato va in
archivio o si cancella con una riga nell'indice; link validi; nessuna foto o dato personale nel repo; segnala branch o PR orfani.
Scope: vincoli fissi di AGENTS. Se una richiesta, un esito o un'idea esce dallo scope o tocca il parcheggio (§9), fermati e chiedimi.
Nessun test ripetuto senza un cambiamento, nessuna misura ricostruita, mai un esito non osservato. Tue proposte: etichetta P, al massimo tre.
Italiano, frasi brevi. Inizia: dove siamo in 5 righe, poi la proposta del primo passo.
```

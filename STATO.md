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
- [ ] **M1** · T0 catalogato nella PR #33 (non su main); T1–T4 e T6 non eseguiti (+T5 facoltativo). [ROADMAP §6](docs/ROADMAP.md).
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
**M1 · T0 in PR #33, senza merge:** dopo la decisione sulla PR, proporre T1 (fogli con foto in chat Android) con prompt e raccolta esiti. M2 fermo.

## Ultimo passaggio
- Chi/quando: Direttore, 2026-11-13; P1 T0 autorizzato, consolidamento sul branch PR #33, merge non autorizzato.
- Fatto: catalogo di 12 font operativi e 134 senza corona/30 Premium dal materiale utente; documenti T0 allineati alla PR.
- Prove: [PR #33](https://github.com/Matteo-Exp-Transformer/generazione-contenuti-GPT-SOCIAL/pull/33), diff 5 commit avanti/0 indietro; 5/5 test dichiarati, non rieseguiti dal Direttore.
- Aperto/bloccato: conferma merge #33; disponibilità/esportazione font Canva non testata; contrasto foto non adattivo; branch B0 residuo.
- Serve dall'utente: decisione sul merge #33; successivamente T1 Android con foto handpan e ZIP aggiornato.

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

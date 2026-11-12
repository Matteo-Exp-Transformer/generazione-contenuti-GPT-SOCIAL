# STATO — aggiornato 2026-11-12 dal Costruttore (Claude)
Obiettivo: dirigere un post sulla propria foto e ricevere un PNG pubblicabile. Scope e traguardi: [ROADMAP](docs/ROADMAP.md).
**Ripristino di progetto del 2026-11-12** (decisione utente): nuovo flusso Officina modelli → chat del post →
bozza Canva da modello → decorazioni come livelli → ritocco ed export. MANDATO-001, PRD v0.1 e VALUTAZIONE v1.0 archiviati.

## Dove siamo
- **M0 Ripristino:** in corso (questa PR). Repo ripulita: strade e gate superati cancellati o archiviati ([indice](docs/archivio/README.md)).
- **Regista v1.0** ([SKILL](skills/post-director/SKILL.md)): **sospeso**, non avviare chat Regista. Si riscrive in M3 sul nuovo flusso.
- Kit campionari v1 ([campionari/](campionari/)): fogli deterministici verificati in locale; in ChatGPT non ancora provato.
- Canva: `copy_design` → modifica testi → commit → rilettura osservato il 12/11 anche con quota IA esaurita
  ([evidenza](evidence/canva-template/2026-11-12-copy-edit-commit.md)). Foto nel modello, livelli decorativi ed export: non provati.
- Mai dimostrato finora: un post consegnato end-to-end.

## Sequenza
- [ ] **M0** · unire questa PR (ok dell'utente); PR #30 chiusa senza merge; branch remoti superati eliminati.
- [ ] **B0** · Costruttore: opzione `foto` nel kit (copia ridotta, hash dell'originale prima/dopo), test, zip ricostruito.
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
Utente: avviare il Direttore con il prompt qui sotto (Claude Code o Codex con accesso alla repo). Primo passo atteso:
merge della PR di ripristino #31 con l'ok dell'utente, poi B0 e i prompt delle chat del Banco di prova (M1).

## Ultimo passaggio
- Chi/quando: Costruttore Claude, 2026-11-12, dopo confronto di prodotto con l'utente (decisioni 1–3 del 12/11).
- Fatto: ROADMAP (scope, traguardi M0–M5, esiti decisi, piano M1, checklist, registro); AGENTS e STATO riscritti;
  MANDATO-001, PRD, VALUTAZIONE archiviati; pulizia repo con sub-agente; catalogo modelli vuoto; audit 12/11 importato.
- Prove: `tests/engine` 18 OK; `tests/campionari` 2/3 OK, `test_quattro_modi` rosso solo in locale (`python -I` esclude Pillow utente); i 4 fogli generati dallo zip a mano. `.gitattributes`: kit senza conversione CRLF.
- Aperto/bloccato: B0 da fare; branch `audit/canva-mcp-nongenerative-20261112` da eliminare dopo il merge.
- Serve dall'utente: revisione e merge della PR.

## Prompt del Direttore (sessione nuova del Costruttore)
```
Sei il Direttore di GPT SOCIAL: Costruttore con accesso alla repo Matteo-Exp-Transformer/generazione-contenuti-GPT-SOCIAL.
Parti da main aggiornato (se la PR #31 non è unita, leggi il suo branch e proponi il merge). Leggi AGENTS.md, STATO.md e
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

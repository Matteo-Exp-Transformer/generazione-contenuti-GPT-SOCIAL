# MANDATO-001 — Una strada, un test, una decisione rapida

**Stato:** ATTIVO dal 2026-11-10 · **Decisione utente:** [decisioni.md](decisioni.md) (voce 2026-11-10, «strada unica»)
**Base:** audit indipendente Claude del 2026-11-10 (verdetto: *in deriva*; sintesi al §1).
**Sostituisce come prossimo passo:** G-FOTO-01 e ogni gate su fixture neutra. T1 resta HOLD fino al Gate D.

## 0. In una frase
Entro il **13/11** sapere se la strada «foto bloccata + render deterministico» permette di dirigere un
post sulla propria foto; altrimenti passare a Canva/Figma via MCP. Se i risultati sono lontani, non si
insiste: si cambia strada.

## 1. Perché (sintesi audit)
- Tre tentativi su foto reale (Pilota A, T1-01, T1-02): tutti FAIL. Causa già diagnosticata nella
  [PR #11](https://github.com/Matteo-Exp-Transformer/generazione-contenuti-GPT-SOCIAL/pull/11):
  rigenerazione dell'intera scena invece di foto bloccata + overlay.
- Il codice 002 è un banco di prova su una sola fixture: non gestisce foto né testo.
- Dopo l'ultimo commit di codice (10/11, 13:52) solo documentazione e riconciliazioni.
- Stato corrente sparso su 3 branch non integrati; in `main` README, PRD, decisioni e audit sulle
  interfacce sono superati; AGENTS.md rimanda a un file inesistente.

## 2. Tabella di marcia (timebox rigidi)
| Fase | Chi | Timebox | Uscita |
|---|---|---|---|
| **F0** Consolidamento | Costruttore | 1 sessione, ≤2 h, entro 11/11 | `main` pulito, `STATO.md`, AGENTS ridotto, archivio |
| **F1-A** Strada A | Costruttore | ≤2 sessioni, entro 13/11 | TU-01 eseguito su Strada A |
| **F1-B** Sonda MCP | Costruttore, in parallelo a F1-A | ≤1 sessione, entro 13/11 | TU-01 eseguito su 1–2 strumenti MCP |
| **Gate D** | Utente (+ revisore, una volta) | 30 min, 13/11 | Strada scelta, registrata in `decisioni.md` |
| **F2** Pilota prodotto | Regista post + utente | 1 post reale, entro 17/11 | Post consegnato con la skill `post-director` |

F1-A e F1-B corrono in parallelo per non perdere giorni se A fallisce. Toccano file diversi
(`engine/` contro `evidence/tu-01-mcp/`). Superato un timebox senza uscita, la fase è FAIL: niente proroghe
automatiche, decide l'utente al Gate D.

## 3. Test unico TU-01 (identico per tutte le strade)
**Input:** una foto dell'utente, autorizzata per il test; formato 1080×1350; titolo A e titolo B scritti
*prima* del test; una palette.
**Sequenza:** render A → visibile su Android → cambio **solo** del titolo in B → visibile → ritorno ad A
→ export PNG.

| # | Misura | Strada A | Strada MCP |
|---|---|---|---|
| 1 | Foto preservata | pixel fuori dall'area titolo identici (test automatico) | confronto pixel sugli export se possibile, altrimenti visivo dichiarato |
| 2 | Undo esatto | A finale = A iniziale (hash dei pixel) | idem o visivo dichiarato |
| 3 | Visibile su Android senza download | conferma utente | conferma utente |
| 4 | Qualità estetica | voto utente 1–5 | voto utente 1–5 |
| 5 | Tempo | minuti attivi utente, numero turni | idem |
| 6 | Costo extra | € effettivi | € effettivi (account di prova ammessi) |
| 7 | Ripresa | lo stato si riapre in una nuova sessione? sì/no | idem |

Prove in `evidence/tu-01-<strada>/` (scheda + PNG solo se l'utente autorizza la foto in repo).
Il voto di qualità lo dà solo l'utente. Mai stimare minuti o voti.

## 4. Regole del Gate D
- **A vince** se 1, 2, 3 = sì e qualità ≥ 3.
- **Si passa a MCP** se A fallisce 1–3 entro il timebox, oppure qualità A ≤ 2 con MCP ≥ A + 1, oppure
  minuti A > 2 × minuti MCP.
- **Falliscono entrambe:** stop e riformulazione del prodotto con l'utente. Non nuovi micro-gate.
- **Kill rapido MCP:** se in 30 minuti uno strumento non sa importare la foto, inserire un testo
  modificabile ed esportare PNG, è scartato; si prova il secondo (massimo due strumenti).
- Prima del Gate D nessun test oltre TU-01.

## 5. F0 — Consolidamento (Costruttore)
1. **Integrare o chiudere:** PR #11 (merge come archivio); branch `docs/g-ui-02-evidence-20261110`
   (merge di evidenze e stato); branch `docs/independent-product-audit-claude-20261110` (merge come archivio).
   Eliminare i branch conclusi `docs/creative-console-003-handoff` e
   `docs/android-t1-reconciliation-gate-20261110`, dopo aver verificato che non hanno commit non integrati.
2. **Creare `STATO.md`** dal modello al §9: unica fonte dello stato corrente. La sezione «Stato operativo»
   di `pilota-foto-diretta-android.md` diventa storica.
3. **Archiviare** in `docs/archivio/` tutti i documenti di audit, report, handoff, protocollo e piano
   (oggi: `audit-*`, `report-*`, `handoff-*`, `PLAN-*`, `protocollo-*`, `test-cono-creativo-v01.md`,
   `pilota-foto-diretta-android.md`). Senza riscriverli; `docs/archivio/README.md` con una riga per file.
   In `docs/` restano solo `PRD-v0.1.md`, `decisioni.md` e il mandato attivo.
4. **Correggere** README (3 righe di stato + link a `STATO.md`), PRD §Stato, il rinvio a `memory/wiki`.
5. **Sostituire AGENTS.md** con lo scheletro al §8.
6. Aggiungere a `.gitignore` gli output di render (`*.render.png`, `render-*.png`).

**Criterio:** un agente nuovo legge `AGENTS.md` + `STATO.md` (≤ 130 righe in tutto) e sa cosa fare.

## 6. F1-A — Strada A (Costruttore)
- Nuovo `engine/`: `render(post.json, foto) → PNG` con tre tipi di layer: foto bloccata (crop/scala),
  testo (font a licenza libera, versione fissata), forma/colore. Schema = quello della skill
  [`post-director`](../skills/post-director/SKILL.md).
- **Test:** hash della foto sorgente; pixel fuori dall'area testo identici tra A e B; A→B→A identico.
  Includere le correzioni emerse dall'audit sull'harness 002: colori HEX normalizzati, `revision`
  booleana rifiutata, chiavi chiuse, solo `ValueError`, hash sui pixel decodificati, output fuori repo.
- **Uso con l'utente:** nella chat ChatGPT (Python + Pillow, immagine mostrata inline) caricando
  engine e foto; `post.json` salvato in repo dal Costruttore a ogni approvazione.
- **Non costruire:** Apps SDK, server, UI reattive, generazione immagini sulla foto.
- `tests/creative-console/` resta come riferimento, senza nuovi gate.

## 7. F1-B — Sonda MCP (Costruttore)
- Candidati: Canva e Figma; account di prova ammessi. Nell'ambiente Claude Code dell'utente i
  connettori Canva e Figma sono presenti e vanno solo autorizzati; verificare anche le app equivalenti
  in ChatGPT.
- Primi 15 minuti per strumento: si può importare la foto, cambiare un testo via MCP, esportare PNG?
  Costo? Se no → kill rapido (§4).
- Eseguire TU-01 e compilare la scheda. **Non costruire** integrazioni o template complessi.

## 8. Sistema agenti — scheletro di `AGENTS.md` (≤ 45 righe)
```
# GPT SOCIAL — istruzioni agenti
Scopo: far dirigere all'utente un post social statico sulla sua foto senza perdere le scelte approvate.
Leggi: 1) questo file 2) STATO.md 3) il mandato attivo linkato in STATO.md. Altro solo se serve.

Ruoli
- Utente: decide, autorizza, giudica la qualità.
- Costruttore (Codex o Claude Code sulla repo): repo, engine, test, commit/PR. Non conduce post.
- Regista post (chat, skill skills/post-director): conduce il post con l'utente. Non modifica la repo.
- Revisore (sessione nuova): solo al gate indicato da STATO.md. Nessun audit di audit.

Regole
- Fonti: STATO.md = stato corrente (si sovrascrive); decisioni.md = decisioni (si aggiunge una riga).
- Fatto / ipotesi / proposta sempre distinti. Mai un PASS non eseguito.
- Spese, installazioni, foto in repo, push su main: solo con ok dell'utente.
- Un branch per mandato; si elimina dopo il merge. Prove in evidence/<caso>/ o nella PR.
- Vietati nuovi file di handoff, audit, report o protocollo: si aggiorna STATO.md.
- Un file nuovo in docs/ solo se ne sostituisce o archivia uno esistente.

Passaggio testimone (fine di ogni lavoro)
1. Aggiorna in STATO.md il blocco «Ultimo passaggio» (5 righe).
2. Se c'è una decisione dell'utente, una riga in decisioni.md.
3. Rispondi all'utente in 3 blocchi: Fatto (con prove) · Stato (righe dei gate) · Prossimo passo.
4. Chiudi con il prompt puntatore:
   «Repo generazione-contenuti-GPT-SOCIAL, branch main. Leggi AGENTS.md e STATO.md
    ed esegui il prossimo passo. Chiudi secondo AGENTS.md.» (+ al massimo una riga dell'utente)

Limiti di pulizia: AGENTS ≤45 righe, STATO ≤80, SKILL ≤120. Al passaggio di ogni gate,
ciò che è superato va in docs/archivio/.
```

## 9. Modello di `STATO.md` (≤ 80 righe)
```
# STATO — aggiornato <data> da <ruolo>
Obiettivo: dirigere un post sulla propria foto senza perdere le scelte approvate.
Mandato attivo: docs/mandato-001-strada-unica.md

## Gate
- F0 Consolidamento: <PASS/IN CORSO/FAIL> — <prova>
- F1-A Strada A (TU-01): ...
- F1-B Sonda MCP (TU-01): ...
- Gate D: ...
- F2 Pilota prodotto: ...

## Prossimo passo (uno)
<chi> — <cosa> — <criterio di completamento> — <entro>

## Ultimo passaggio
- Chi/quando:
- Fatto:
- Prove:
- Aperto/bloccato:
- Serve dall'utente:
```

## 10. Chat con il regista post (procedura standard)
La procedura del prodotto è la skill [`skills/post-director/SKILL.md`](../skills/post-director/SKILL.md):
cinque fasi (avvio → direzioni → blocco → revisioni → consegna), un formato fisso per ogni turno e stop
espliciti. È **indipendente dalla strada**: con la Strada A renderizza l'engine, con la Strada MCP lo
strumento scelto. In ChatGPT va installata come istruzioni di un Project o di un GPT personale,
con l'engine allegato; il prompt d'avvio dell'utente è libero («Voglio un post su…»).
La skill v0 viene corretta solo con prove di TU-01 o F2, non per ipotesi.

## Stop del mandato
Superamento dei timebox, spesa non autorizzata, foto non autorizzata, oppure due fallimenti della stessa
misura TU-01 sulla stessa strada → fermarsi e portare la scheda all'utente.

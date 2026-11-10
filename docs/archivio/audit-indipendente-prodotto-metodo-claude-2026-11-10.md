# GPT SOCIAL — Audit indipendente di prodotto, metodo e tecnologia per Claude (Anthropic)

**Data:** 2026-11-10  
**Repository privata:** https://github.com/Matteo-Exp-Transformer/generazione-contenuti-GPT-SOCIAL  
**Status:** dossier documentale per revisione esterna. Non è una decisione di roadmap né il risultato di nuovi test.  
**Modalità del presente audit:** lettura remota GitHub; nessuna suite rieseguita, nessun nuovo asset o renderer testato.

## 1. Mandato per il revisore esterno

Claude deve agire da Independent Principal Product Architect, Product Strategist, UX/Creative Workflow Auditor e Software QA Reviewer. Non è necessario conoscere OpenAI, ChatGPT, DIL o i modelli sottostanti: si tratta di strumenti contingenti del prototipo, non di requisiti universali del prodotto.

Partire da `AGENTS.md`, `README.md`, `docs/decisioni.md`, e soprattutto dalla sezione «Stato operativo» di `docs/pilota-foto-diretta-android.md` **sul branch `docs/g-ui-02-evidence-20261110`**. Verificare anche il codice sorgente e le evidenze nelle PR; non confermare automaticamente le conclusioni di questo dossier. Fare audit critico e non promozionale.

**Domanda decisiva di prodotto:** «Mi permette di dirigere visivamente un post sulla mia fotografia, senza perdere quello che ho approvato?»

**Limiti del mandato:** audit read-only; niente modifiche a codice, schema, renderer, roadmap, branch, PR o main; niente generazioni, spese o installazioni; nuovi piloti T1 in HOLD. Proporre senza eseguire.

## 2. Strategia di prodotto

La promessa non è semplicemente «generare post social con AI»: è la **continuità verificabile dell'intenzione creativa** dall'idea iniziale alle revisioni e all'asset finale. Il valore si concentra su tre assi:
- **Agency:** l'utente vede alternative riconoscibili, sceglie/mixa, personalizza e può decidere in linguaggio naturale senza microapprovazioni superflue.
- **Fidelity:** una modifica locale non altera foto, testo, palette, composizione e scelte già approvate; la preview è un riferimento affidabile dell'output.
- **Continuity:** decisioni e versioni sono recuperabili da altri agenti/sessioni senza inventare valori mancanti o usare implicitamente il contesto di chat.

L'ambito attuale è **contenuto statico professionale**, con fotografia editoriale, grafica e tipografia. Fuori scope corrente: video, pubblicazione automatica, analytics avanzate. Budget esterno incrementale iniziale **€0**. L'applicazione definitiva, backend, preset multiprogetto, espansione dello schema e strumenti aggiuntivi **non** sono stati approvati.

Il workflow candidato, **ipotesi e non architettura approvata**, è: brief libero → direzioni creative distinguibili → selezione/mix → approvazione di una foto base immutabile → layout a livelli → mini-preview reale e controlli progressivi → checkpoint approvato e versionato → cambiamenti circoscritti/Undo → render/export verificato. Il percorso può essere chat-first in discovery senza che ChatGPT Android sia necessariamente la piattaforma finale.

**North star proposta, non KPI approvato:** quota di task reali nei quali l'utente ottiene una modifica richiesta su contenuto fotografico e un export verificato mantenendo invarianti tutte le decisioni/regioni protette. Metriche utili: numero turni e gate, tempo umano effettivamente misurato, tasso di revisioni non autorizzate, percentuale di campi approvati recuperati, qualità/leggibilità mobile, fallimenti dei controlli negativi, costo reale. Non inventare tempi, punteggi o costi.

## 3. Evoluzione delle decisioni e apprendimenti

1. **FORMA-001:** brand editoriale fittizio FORMA, tema «La forma della luce», direzione B «INTERSEZIONI». Confronto previsto fra A generazione dell'intero post e B fotografia generata + layout separato modificabile. Il PRD v0.1 è storicamente esplorativo; per un verdetto comparativo leggere `benchmarks/FORMA-001/risultati.md`, non estrapolarlo dal solo README. Difetti già documentati di fedeltà al testo e rapporto foto/grafica.
2. **LAYER-001:** workflow incrementale con troppe microdecisioni, troppo testo, mockup geometrici non equivalenti a rendering reale. Feedback dell'utente: vuole capire a ogni passaggio cosa si sta decidendo, cosa cambia, cosa farebbe un professionista e su quali basi; meno interazioni e più anteprime significative.
3. **Cono creativo adattivo:** protocollo sperimentale approvato per provare fino a tre direzioni iniziali, mix V1/V2/V3, convergenza progressiva, varianti visive ampie in chat, codici A/B/C per testi e 1/2/3 per oggetti, foto bloccata e modifiche localizzate. Non è una prova riuscita di lock pixel o export finale.
4. **Android UI e visualizzazione:** utente ha confermato griglia a due colonne di immagini di riferimento `AsyncImage` senza carosello orizzontale. Con `python_user_visible.exec` / Pillow e due `display()` separati nello stesso run sono stati visti due raster distinti e grandi affiancati; un collage unico appare più piccolo. È comportamento osservato del client, non una garanzia del codice. Un pannello nativo con selettori e reset è stato confermato manipolabile.
5. **Creative Console 002 (PR #6):** renderer Pillow neutro, modello JSON ristretto, round-trip esplicito, test negativi e diff di una singola proprietà. Non implica import diretto Android.
6. **Creative Console 003 (PR #7 e audit):** approvazione e recupero documentale del concept: B Geometrico, «Ogni spazio racconta», editorial, palette Verde bosco `#283C3A`, `#D8A76A`, `#F4EBDD`, composizione asymmetric. Il checkpoint 003 è *creative-approval-handoff*, non input del renderer 002. Cold test da GitHub PASS solo nel perimetro della documentazione.
7. **Pilota A fotografico handpan (PR #11):** workflow PARTIAL, fedeltà fotografica/estetica FAIL; titolo+Undo non testati.
8. **T1-01:** FAIL procedurale prima del compositing: proposte verbali senza anteprime visive collegate alle selezioni. Rendering e pixel NON TESTATI. **T1-02:** secondo episodio FAIL segnalato dall'utente per anteprime assenti/inutilizzabili e pannello non conforme; audit completo non recuperato: evitare attribuzioni tecniche inventate.
9. **T0:** PARTIAL documentato, provenienza di evidenze da implementazioni differenti; non PASS end-to-end.
10. **G-UI-01:** controllo colore su mini-preview SVG, reset, JSON manuale `{gate,fixture,accent}`; PASS locale e recupero assistito riferiti dall'utente. Nessuna prova di storage automatizzato, versioned Undo, PNG o round-trip native CLI.
11. **G-UI-02:** ambiente Windows Python 3.13.7 + Pillow 12.1.1; 6 test renderer + 7 test round-trip, CLI export/verify, render Pillow e hash: PASS locali registrati. Snapshot Android originale G-UI-01 mai recuperato; candidato terracotta **ricostruito localmente** dalla baseline e non importato dal telefono. Esito complessivo PARTIAL.
12. **G-UI-02-RETEST:** nuovo pannello Android con colore Blu `#356B84`, Terracotta `#B36A48`, reset, snapshot/copia/incolla/Recupera. Utente conferma recupero terracotta e screenshot finale descritto: PASS limitato al recupero manuale assistito corroborato visivamente. Screenshot originale non verificato come file GitHub; niente log click/clipboard e niente bridge renderer nativo. Esito complessivo G-UI-02 resta PARTIAL.
13. **Riesame successivo sul branch di evidenze:** micro-gate di revisione localizzata su foto originale è solo PROPOSTO, soggetto ad autorizzazione; l'originale G-UI-01 non va richiesto nuovamente.

## 4. Governance, protocollo decisionale e rischi del metodo

Regole da `AGENTS.md`: una sede canonica per ogni ambito; distinguere fatti, ipotesi, proposte e autorizzazioni; non riempire la repo di duplicati; non dichiarare completato un test non eseguito; privilegiare strumenti esistenti; nessuna installazione, acquisto, asset o modifica dell'ambiente senza consenso specifico; nessun push su main senza approvazione. Cercare PR e branch esistenti prima di aprirne altri; commit solo di sorgenti/prove pertinenti, senza cache o export provvisori; verificare diff e readback remoto; una sola prossima azione nel passaggio di consegne. Il protocollo storico «Due chat, un solo caso» è **sospeso**, non un'autorizzazione.

Punti forti: auditabilità, disciplina della provenienza, test negativi, arresto davanti a evidenze insufficienti, separazione di approval e delivery. Possibile debolezza sistemica: **test theatre** o eccesso di riconciliazioni, handoff e documenti rispetto a valore prodotto osservabile. Ogni gate dovrebbe ridurre un rischio prioritario: evitare micro-gate superflui solo per ottenere un altro PASS documentale.

Tracciare sempre: run/caso, revision e precedente, versione tool, fonte originaria, valori letterali approvati, elementi bloccati, cambiamento consentito, tipo di prova, screenshot/asset realmente accessibili, hash **ricalcolati dai byte**, errori e stop condition. Uno SHA riportato in un verbale non è prova che l'asset sia oggi recuperabile.

## 5. Inventario degli strumenti — capacità e limiti

| Superficie | Capacità documentata | NON dimostra |
|---|---|---|
| ChatGPT Android | Interazione umana e confronto visivo sul dispositivo | Verifica automatica di asset, click o clipboard |
| UI conversazionale `DIL.useState`, controlli, SVG | Stato locale condiviso, preview reattiva e reset | Stato persistente, Android→CLI, Undo versionato |
| `AsyncImage` | Griglia di riferimenti visivi | Pixel identity di foto generate |
| Python `python_user_visible.exec`, `display()` | Raster Pillow inline e confronti visivi | Layout identico su tutti i client |
| Pillow | Compositing ripetibile di fixture neutra | Editor fotografico completo, font/crop reali |
| `roundtrip.py` | Export JSON canonico/verify su baseline | Git commit, sync automatica o import formato pannello Android |
| GitHub (PR/branch/commit/readback) | Persistenza byte, responsabilità e cronologia | Veridicità delle decisioni in chat o qualità finale |
| SHA-256 | Identità byte/canonical state | Equivalenza pixel fra PNG con encoder diversi |
| Screenshot Android | Stato finale visibile in un dato istante | Sequenza completa delle interazioni |
| Cold test in nuova chat | Recuperabilità del checkpoint senza transcript | Renderer/output grafico validato |
| AI image generation | Esplorazione di foto/asset | Conservazione garantita dei pixel nelle revisioni |

Claude può valutare l'architettura indipendentemente da questi brand. `DIL.useState` = locale reactive state in chat; `AsyncImage` = presentazione di immagini; `python_user_visible.exec` = ambiente Python che espone risultati; `Pillow` = libreria Python di manipolazione immagini; GitHub = source control e artefatti remoti.

## 6. Contratto reale del codice 002 (letto su main)

Fonti: `tests/creative-console/neutral-state.json`, `neutral-render.py`, `roundtrip.py`, `README-002.md`.

- Stato iniziale: `schemaVersion = 1.0.0`, `projectId = microtest-neutral-001`, `revision = 1`; canvas 600×750, background `#F3F0E8`, template `neutral-card` 1.0.0 e renderer `pillow-v1` 1.0.0.
- Asset PNG fixture immutabile con SHA-256 dichiarato: `0fa828ab7b46009c890168addcca6db0bfb87e0baf75799a42abe93ba342e55a`. Layer 0 background `approved:true,locked:true`; layer 1 `accent` rettangolo, bounds `[60,100,480,90]`, inizialmente fill `#356B84`, visible true, non locked, non approved.
- `neutral-render.py:validate()` effettua controlli su versione, canvas, hash fixture, template, renderer, struttura layer e HEX del rettangolo. `change_fill()` rifiuta revisione obsoleta e layer bloccato. `render()` apre PNG fixture e disegna rettangolo Pillow.
- `roundtrip.py:verify_transition()` ammette **soltanto** `revision N→N+1` e modifica effettiva di `layers[1].fill`; tutti gli altri valori devono coincidere con una copia della baseline.
- `canonical()` produce UTF-8 con `sort_keys=True`, separatori compatti, `ensure_ascii=False`, newline LF. Fingerprint SHA-256 dello stato canonico e del PNG renderizzato.
- La regione del rettangolo è 480×90 = **43.200 pixel** in coordinate x=[60,540), y=[100,190). Un diff confinato a quest'area è prova locale di una modifica rettangolare, **non** generalizzazione a foto/typography.
- La CLI accetta `export --baseline --expected-revision --fill --out` o `verify --baseline --expected-revision --state`; non importa lo snapshot `{gate,fixture,accent}` del pannello Android, non accede a GitHub, non attiva backend o undo multi-step.

**Test precedentemente eseguiti (non rieseguiti da questo dossier):** renderer 6/6, roundtrip 7/7, exit 0; verifiche ripetibilità, snapshot restore, diff single-property, no-op, stale, locked, asset tamper, unrelated mutation, CLI. Report e log in `docs/evidence/g-ui-02-20261110/` sul branch `docs/g-ui-02-evidence-20261110`. Gli hash prodotti in quell'ambiente sono verifiche contestuali, non garantiti cross-encoder. File remoti LF e checkout Windows CRLF hanno hash fisici diversi; distinguerli dagli hash dei valori JSON canonici.

**Potenziali edge case da ispezionare senza dichiararli già verificati:** `isinstance(revision,int)` ammette boolean in Python; validazione non necessariamente esaustiva per ogni chiave del JSON; necessità di separare PNG-byte equality da decoded-pixel equality; confini di asset hash, schema versioning, concorrenza e stale snapshots; gestione futura di antialiasing, profili colore, font, crop, maschere e regioni protette. Nessun incentivo ad ampliare il codice prima del rischio di prodotto che lo richieda.

## 7. Tipi di test: cosa è provato e cosa no

| Categoria | Evidenza | Stato |
|---|---|---|
| Static/documental provenance | GitHub Contents, commit SHA, PR, diff | PASS nei perimetri registrati |
| Unit tests renderer 002 | 6 test originali | PASS storico locale |
| Unit tests roundtrip 002 | 7 test originali | PASS storico locale |
| CLI + import/load/verify + Pillow render | Evidenze G-UI-02 | PASS locale, NON Android→renderer |
| Negative/adversarial | stale/no-op/tamper/locked/unrelated change | PASS solo casi eseguiti |
| Single-field invariant + pixel diff | Rect 480×90 | PASS sul neutro, non su foto |
| UI/device | Selettori/preview/reset su ChatGPT Android | PASS riferito con limiti |
| Snapshot assistito | Copy/paste JSON con ripristino colore | PASS riferito, non sync |
| Remote cold recovery concept 003 | JSON SHA e readback | PASS documentale, non renderer |
| Original Android payload 001→002 | Payload originale assente | NON VERIFICATO |
| UI SVG→Pillow parity | Nessuna comparazione nativa originale | NON TESTATO |
| Photo original→local revision→export | Nessun workflow E2E valido | NON TESTATO |
| Undo versionato sulle scelte approvate | Non dimostrato | NON TESTATO |
| T0 end-to-end | Evidenze non conclusive | PARTIAL |
| T1-01/T1-02 | Procedura visuale bloccante | FAIL procedurale; pixel NON TESTATI |
| Nuovi T1 | Blocco operativo | HOLD |

Non confondere `PARTIAL` di un gate complessivo con `NON TESTATO` di una specifica capacità. Screenshot finale non prova l'intera sequenza; controllo locale non garantisce output finale. Hash dei file uguali attestano byte uguali, hash diversi non necessariamente immagini visivamente diverse. Per una prova fotografica usare anche confronto pixel decodificati nelle regioni protette, con condizioni di rendering controllate.

## 8. Giudizio strategico preliminare da contestare

Il metodo è convincente nel non spacciare demo per prove. Tuttavia il rischio maggiore non è l'assenza di altri test unitari: è che l'utente non possa ancora *effettivamente* dirigere e correggere una fotografia reale in modo affidabile. I test attuali massimizzano la certezza su una transizione neutra estremamente circoscritta; bisogna capire quando tale certezza smette di produrre apprendimento di prodotto.

**Raccomandazione candidata, non autorizzazione:** progettare un singolo vertical slice su fotografia originale già disponibile/autorizzata, con una sola modifica testuale o grafica chiaramente reversibile, baseline approvata, regioni protette, screenshot/raster reale Android, revisione prima/dopo, Undo e verifica di export; sfruttare tool esistenti, senza rifare i T1 o cambiare schema 002 automaticamente. Prima valutare se questa ipotesi debba davvero essere il prossimo esperimento, dati i FAIL UX.

Architetture alternative da esplorare criticamente: editor deterministico a livelli con AI come art director; export di JSON di intent e renderer separato; rendering unico per preview/export; preview foto reale invece di mockup; app o interfaccia cross-provider anziché dipendere dai controlli della chat. Confrontare costi, lock-in, implementabilità e qualità dell'esperienza prima di scegliere.

## 9. Domande di audit esterno a Claude

1. Quale target user e job-to-be-done giustificano il prodotto rispetto agli editor già esistenti?
2. Chat Android è requisito del prodotto o solo terreno di scoperta? Quali dipendenze proprietarie sono eliminabili?
3. La distinzione creative intent / approved design state / render state / output artifact è sufficiente? Quale bridge minimo rende una scelta creativa eseguibile senza inventare parametri?
4. Come si preservano foto, testo e layout senza soffocare l'utente con conferme?
5. Quali test possiedono il massimo potere di **confutare** la promessa di prodotto?
6. È corretto mantenere HOLD T1 e PARTIAL T0/G-UI-02? Ci sono discrepanze documentali/tecniche verificabili?
7. Quali errori logici, edge case o omissioni sono nel codice effettivo, con riferimento esatto al file?
8. Come ridurre governance, branch, audit e handoff conservando una fonte canonica e tracciabilità?
9. Quale vertical slice, criterio di successo e stop condition riduce più rischio senza investire prematuramente?
10. Quali massime tre decisioni strategiche dovrebbe assumere il proprietario, con pro/contro e dati mancanti?

## 10. Deliverable richiesto a Claude

Consegnare in italiano:
1. Executive verdict e livello di confidenza con evidenze vs ignoti.
2. Critica indipendente alla visione, UX, valore e target.
3. Review architettura, stato, renderer, portability, dependences, fallimenti e limiti del codice.
4. Audit dei metodi decisionali, strumenti scelti e problemi di ridondanza.
5. Matrice QA con test unit/integration/visual/pixel/device/UX/cold/E2E, stato e lacune.
6. Top 5 rischi classificati con gravità e mitigazioni proporzionate.
7. **Massimo tre raccomandazioni** prioritarie e verificabili, incluso cosa non costruire ora.
8. **Un solo prossimo passo** non eseguito, con criteri di accettazione e stop.
9. Fonti esatte GitHub (path/commit/PR), distinzione fra ciò che Claude ha letto e ciò che non è riuscito a verificare.

## 11. Letture canoniche e link diretti

- [AGENTS.md](../AGENTS.md) — governance e handoff.
- [README.md](../README.md) — obiettivo, vincoli e punto di accesso.
- [docs/decisioni.md](decisioni.md) — decisioni generali.
- [docs/PRD-v0.1.md](PRD-v0.1.md) — vision esplorativa.
- [Stato operativo Android sul branch di evidenze](https://github.com/Matteo-Exp-Transformer/generazione-contenuti-GPT-SOCIAL/blob/docs/g-ui-02-evidence-20261110/docs/pilota-foto-diretta-android.md) — prevalente su protocollo storico.
- [Protocollo UI Android](protocollo-ui-android-test-2026-11-10.md) — prove display, controlli locali e limiti.
- [LAYER-001](audit-layer-001-handoff.md) — costo delle microdecisioni.
- [Cono creativo sperimentale](test-cono-creativo-v01.md) — proposta autorizzata di metodo, non risultato validato.
- [Audit Creative Console 003](audit-creative-console-003-cold-test-2026-11-10.md) — cold readback.
- [README-002](../tests/creative-console/README-002.md), [baseline](../tests/creative-console/neutral-state.json), [renderer](../tests/creative-console/neutral-render.py), [roundtrip](../tests/creative-console/roundtrip.py).
- [PR #6](https://github.com/Matteo-Exp-Transformer/generazione-contenuti-GPT-SOCIAL/pull/6) renderer/roundtrip; [PR #7](https://github.com/Matteo-Exp-Transformer/generazione-contenuti-GPT-SOCIAL/pull/7) concept; [PR #11](https://github.com/Matteo-Exp-Transformer/generazione-contenuti-GPT-SOCIAL/pull/11) audit pilota A aperta/draft al controllo; [PR #13](https://github.com/Matteo-Exp-Transformer/generazione-contenuti-GPT-SOCIAL/pull/13) riconciliazione Android merged al controllo.
- `benchmarks/FORMA-001/risultati.md` per contesto comparativo e confini delle affermazioni.

**Nota di provenienza:** questo dossier integra letture GitHub e contesto di progetto. Le capacità storiche sono riportate come documentate, non riperformate nel presente audit. Un revisore esterno deve rifare una lettura remota delle fonti, non test superflui, prima di firmare il proprio verdetto. 

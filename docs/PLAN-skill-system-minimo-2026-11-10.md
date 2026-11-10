# PLAN — Sistema minimo agentico per GPT SOCIAL
Data: 2026-11-10 · Stato: PROPOSTA da revisionare, NON protocollo approvato
Branch: `proposal/skill-system-minimo-plan-2026-11-10`
Ambito esclusivo: routing del contesto, progettazione, esecuzione, verifica, debug/fix, chiusura e miglioramento del metodo. Non cambia il workflow creativo e non implementa codice.

## 1. Evidenze verificate e trasferibilità
| Origine | Evidenza (file reale, main al momento dell'audit) | Lezione | Scelta GPT SOCIAL |
|---|---|---|---|
| CALENDARIO-V2 | `AGENTS.md`, `_skill-system-v0/00_BUSSOLA_SKILL.md` | Routing area/profilo; caricare solo il contesto pertinente, intensità light/standard/deep | ADATTARE in un routing corto dentro AGENTS, non copiare la bussola e tutte le skill |
| CALENDARIO-V2 | `_skill-system-v0/comunicazione/CHIUSURA_SESSIONE.md` | Resoconto su diff reale, test effettuati, apprendimento; revisione esterna distinta | ADATTARE chiusura breve e proporzionale; no hook o fascicoli ad ogni micro-task |
| memory | `AGENTS.md`, `.claude/skills/progetta/SKILL.md` | Distinguere fatti/incognite, premortem, brief con «finito quando»; lettura selettiva delle fonti | ADATTARE nelle task non banali, senza duplicare wiki né skill esterne |
| memory | `.claude/skills/chiudi/SKILL.md` | Stato corrente corto nella repo del progetto; memoria storica separata | ADATTARE un solo stato sintetico *solo se* gli handoff esistenti non bastano; NON copiare dati privati di memory |
| app-parquet | `AGENTS.md`, `METODO.md`, `docs/procedure/parallelo.md`, `REGISTRO.md` | Una task delimitata, branch e PR; test e prove reali; indipendenza di revisione; lavoro parallelo solo su superfici isolate; metodo evoluto da misure | RIUSARE il contratto di task e verificabilità, ADATTARE la review proporzionale; SCARTARE orchestrazione rigida e registro pesante iniziale |
| GPT SOCIAL | `AGENTS.md`, `README.md`, `docs/decisioni.md`, `docs/handoff-agente-sistemi.md`, `docs/audit-layer-001-handoff.md` | Già fissati fonte unica, separazione fatti/ipotesi, nessun push main, niente skill per inerzia, test reali e handoff senza duplicazione | PRESERVARE: integrare, non sostituire |

**Limite dell'audit:** ricognizione mirata di file guida, skill e procedure; non verifica empirica del funzionamento di tutti gli hook, della CI o delle run; nessuna misurazione di token su GPT SOCIAL. Le lezioni sono proposte di trasferimento, non performance dimostrate.

## 2. Architettura iniziale minima: zero nuove skill obbligatorie
Preservare come fonti canoniche `AGENTS.md` (ingresso e regole), `docs/decisioni.md` (decisioni), `README.md` (indice), `benchmarks/<ID>/protocollo.md` e `risultati.md` (prove della run), il PRD per prodotto; handoff/audit specifici restano evidenze storiche e NON diventano secondi registri di decisione.

**Intervento proposto solo dopo review:** estendere `AGENTS.md` di circa 25–45 righe, evitando nuovi documenti attivi:
1. **Instradamento:** richiesta → profilo **Progetta / Esegui / Verifica-fixa / Meta** → leggere solo README + decisioni + brief/protocollo o file della parte interessata. Non caricare tutti gli audit o repo esterne in automatico.
2. **Contratto minimo di lavoro:** obiettivo concreto, in-scope/out-of-scope, evidenza attesa, criterio «finito quando», grado di rischio, eventuali fatti mancanti e chi può sbloccarli.
3. **Ciclo operativo:** osserva/riproduci → ipotesi causa → intervento minimo → riprova stesso caso → controllo regressioni mirato → diff e prove → PR. Se non riproducibile: dichiarare la limitazione, non «fixato».
4. **Gate di rischio:** light = documentazione o fix isolato, test pertinente + nota minima; standard = modifica multi-file / flusso, piano breve + test + PR; deep = spesa, permessi, dati sensibili, produzione, cambio irreversibile o pipeline di asset, premortem e revisore indipendente prima della fusione. Nessun automatismo sulla generazione d'immagini.
5. **Chiusura:** file cambiati, esito di comandi/prove realmente eseguiti, limiti, decisioni proposte/approvate, unico passo successivo, prompt per nuova chat se richiesto. Aggiornare il file canonico esistente; non creare report di sessione se l'informazione ha già casa.
6. **Branch safety:** branch isolato, PR verso main, nessun merge/push su main senza via libera; verificare sempre ref e SHA di partenza. Per lavori paralleli evitare stessi file canonici / asset / run.

**Nessuna installazione, hook, CI nuova, subagente o duplicazione CLAUDE/AGENTS proposta nella fase zero.** Una `SKILL.md` locale specifica (es. visual QA o gestione asset) diventa candidata solo dopo almeno due difetti reali ricorrenti che un routing breve non risolve; attribuire owner, costo di lettura, prova di utilità e criterio di rimozione.

## 3. Distinzione progettazione vs esecuzione
- **Progetta:** leggere vincoli canonici e osservazioni pertinenti, separare fatto/ipotesi/decisione; individuare 3 fallimenti possibili se il lavoro è standard/deep. Consegna patch plan e test di accettazione, senza scambiare proposta per approvazione.
- **Esegui:** riceve ambito chiuso; crea branch o usa branch esplicitamente assegnato; cambia solo file richiesti e produce evidenze. Non riapre scelte utente senza nuovo dato.
- **Verifica/fixa:** riproduce un bug con prova, isola causa, propone o applica fix secondo mandato, confronta prima/dopo, riporta regressioni. Review indipendente su SHA esatto senza confondere consenso fra modelli e test.
- **Meta:** valuta costi, errori ricorrenti e attrito umano; può proporre una variazione del metodo ma non promuoverla a nuova regola senza esplicita approvazione.

## 4. Tranche, gates e rollback
**G0 — Review indipendente:** comparare questo piano con istruzioni canoniche e branch attivi; trovare contraddizioni e scope creep. Output: revisione documentale e premortem, zero esecuzione creativa.
**G1 — Patch minima:** dopo approvazione, modificare unicamente `AGENTS.md` (e il link README solo se strettamente indispensabile); testare lettura breve da una nuova chat con task fittizia. Evidenza: diff, percorso di lettura, criterio di completamento; rollback con revert della PR.
**G2 — Pilot:** una run di produzione guidata *autorizzata separatamente*, con anteprima vera inline e preservazione degli asset; confrontare turno fino al primo visual, numero correzioni, duplicazioni doc, prove esplicite, costo/tempo se misurabili. Mai inventare metriche.
**G3 — Estensione condizionale:** solo dai difetti osservati, scegliere fra nessun cambiamento, migliore routing o una skill specifica. Riesaminare dopo almeno due run comparabili.

## 5. Premortem preliminare e contromisure
| Fallimento plausibile | Segnale/prevenzione | Verifica |
|---|---|---|
| Skill system pesa più del lavoro | Nessuna skill obbligatoria; audit del contesto effettivamente letto | Nuova chat riesce a orientarsi usando 2–4 file |
| Handoff e decisioni divergono | Un solo registro canonico; gli audit sono osservazioni | Controllo manuale di conflitti nel diff |
| «Fix» basato su spiegazione, non prova | Riproduzione e post-fix con stesso caso; stato NON VERIFICATO se mancano tool | PR include comandi e risultati reali |
| Review fra agenti è solo consenso retorico | Revisore cerca scenari falsificabili su SHA e prove | Almeno 3 controesempi in premortem, con rischio residuo |
| Workflow tecnico soffoca creatività | Separare metodo interno e UX, output utente sintetico | Pilot misura turni fino alla prima anteprima reale |
| Riscrittura sovrappone lavoro concorrente | Base/ref riletti; PR, no main; evitare file condivisi paralleli | Diff per filename, SHA e confronto branch prima di fondere |
| Gestione asset introduce generazioni/costi non autorizzati | G0/G1 documentali; asset/generazioni con permesso esplicito | Nessun output grafico o spesa prima di G2 |

## 6. Criteri di accettazione del piano consolidato
1. Ogni prescrizione nuova ha caso d'uso, benefici osservabili, costo e owner; nulla copiato in blocco dalle repo.
2. Nessuna contraddizione con `AGENTS.md` e `docs/decisioni.md`; distinguere proposta da norma.
3. Un nuovo agente può distinguere progettazione, esecuzione, debug e revisione caricando pochi file.
4. Ogni «finito» ha prova; se non eseguibile, limitazione dichiarata.
5. Il piano non modifica il prodotto, non duplica log, non impone dipendenze e rimane reversibile.
6. La review produce un prompt per il TERZO agente finale, ma non anticipa implementazioni non approvate.

## 7. Mandato per revisore indipendente (agente 2)
Revisionare **criticamente** e in sola analisi questo piano rispetto ai file canonici e alle tre repo di riferimento. Cercare rischi non notati, promesse non verificabili, overhead di token, duplicazione e conflitti con UX visuale. Distinguere severità P0/P1/P2, evidenza con file/linea o SHA, impatto, fix minimo e rischio residuo; usare almeno cinque scenari premortem concreti. Se necessario correggere SOLO questo PLAN in branch dedicato o PR derivata, tracciando differenze dalla versione originale e senza riscrivere la storia. Consegnare la variante consolidata e un prompt completamente incollabile per l'agente 3 che effettuerà implementazione SOLO dopo autorizzazione, pilot e verifica, oppure proporrà no-op se il sistema attuale basta.

## 8. Decisione sospesa
**Nessuna nuova regola è approvata con questo commit.** Questo file è un PLAN candidato per revisione indipendente; la successiva patch su `AGENTS.md` richiede decisione distinta.

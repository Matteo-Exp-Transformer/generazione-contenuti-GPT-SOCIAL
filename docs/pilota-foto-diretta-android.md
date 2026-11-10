# Pilota Android — dirigere un post sulla propria fotografia

**Domanda scelta dall’utente, 10 novembre 2026.** «Mi lascia dirigere un post sulla mia foto senza perdere quello che ho approvato?»

## Stato operativo — riconciliazione del 10 novembre 2026

### Sequenza sintetica di continuità (stato, non roadmap approvata)

**Arrivo di prodotto:** l'utente dirige visivamente un post sulla **propria fotografia**, approva scelte recuperabili e richiede una modifica limitata senza perdere asset, testi, layout e altre decisioni bloccate. La prova di arrivo richiede preview effettivamente visibile su Android, confronto prima/dopo, conservazione delle scelte e provenienza verificabile dei file; non è ancora raggiunta.

- [x] **1. Controllo UI minimo — PASS riferito:** G-UI-01 e G-UI-02-RETEST mostrano selezione/recupero manuale di un colore su preview neutra; screenshot originale del retest non archiviato/verificato come file.
- [x] **2. Meccanica renderer neutro — PASS tecnico storico:** test esistenti su fill/revision, invarianti, negativi e Pillow; non è una prova integrata con Android.
- [ ] **3. Catena Android → renderer 002 — PARTIAL / NON TESTATO:** payload originario G-UI-01 indisponibile; non richiederlo nuovamente e non fabbricare un PASS. G-UI-02 resta PARTIAL.
- [ ] **4. Modifica mirata su fotografia e scelte approvate — PROPOSTO, non autorizzato:** prima definire un micro-gate con asset/criteri recuperabili e confronto visivo; usare prove e capacità esistenti, non lanciare T1.
- [ ] **5. Validazione del flusso di prodotto — HOLD:** nessun PASS end-to-end; T0 PARTIAL, T1-01 FAIL, T1-02 FAIL riferito e nuovi T1 HOLD fino a motivazione documentata e autorizzazione.

Alla chiusura di ogni mandato, aggiornare queste sole righe **se cambia lo stato**, conservando il verbale dettagliato sottostante; riportarle condensate nella risposta all'utente secondo `AGENTS.md`. Se il prossimo passo cambia dopo un audit, separare proposta e decisione dell'utente. Non convertire questa sequenza di verifica in una roadmap di sviluppo approvata.

**Stato: HOLD sui nuovi piloti creativi T1. G-UI-02 PARTIAL: gate tecnico locale PASS, import originale Android non verificabile con le evidenze disponibili.** La sezione storica «Due chat, un solo caso» qui sotto descrive il protocollo precedente e non costituisce autorizzazione a ripeterlo. G-UI-01 è stato autorizzato e svolto separatamente dai T1; la sua chiusura QA è registrata qui sotto. Nessuna modifica alla roadmap, allo schema o al renderer.

- **Pilota A precedente ai T1 — VERIFICATO documentalmente nella [PR #11](https://github.com/Matteo-Exp-Transformer/generazione-contenuti-GPT-SOCIAL/pull/11)**, non ancora integrata in `main`: audit del percorso fotografico handpan con esito PARTIAL sul workflow, FAIL sulla fedeltà finale; titolo+Undo non eseguito. Non conteggiarlo come uno dei due T1.
- **T1-01 — VERIFICATO nell'addendum della PR #11**, sessione `GPT-SOCIAL-T1-20261110-01`: FAIL procedurale prima della composizione, perché direzioni/titoli verbali sono stati proposti senza anteprime reattive collegate alle scelte. Output fotografico, Undo e controllo pixel NON TESTATI. L'addendum è sul branch `docs/android-photo-pilot-a-final-audit`, non su `main` al momento della riconciliazione.
- **T1-02 — RIFERITO dall'utente, episodio distinto:** seconda prova fermata per anteprime A/B assenti o inutilizzabili, pannello interattivo non conforme e mancato rispetto della procedura visuale. **Audit completo NON RECUPERATO** nella repository in questa ricognizione; non attribuire strumenti, sequenza, screenshot, verifiche Android o causa tecnica specifica non dimostrati. Il PASS/FAIL dei singoli sottorequisiti è indeterminato; esito complessivo riferito: FAIL.
- **T0 — PARTIAL RIFERITO** da revisione indipendente e successiva riconciliazione delle evidenze associate a implementazioni differenti. Pacchetto tecnico riconciliato non rintracciato nel tree di `main` in questa ricognizione. Non dichiarare T0 PASS end-to-end.
- **Mandato B — NON AVVIATO nel percorso T1 attuale**: nessun checkpoint T1 approvato e verificato da remoto da consegnare. Creative Console 003 ha un PASS *solo* di recupero documentale; il checkpoint 003 non è input del renderer 002.
- **Capacità già documentate, non equivalenti a integrazione:** [controlli Android e preview UI locali](protocollo-ui-android-test-2026-11-10.md); [renderer neutro e round-trip JSON esplicito](../tests/creative-console/README-002.md). Non è dimostrato il percorso pannello Android → stato persistente → renderer fotografico → revisione locale → Undo.

### Gate tecnico unico — G-UI-01 (eseguito; conferma Android dell'utente)

**Problema:** una scelta dell'utente non risulta collegata in modo verificato a un'anteprima visiva e a uno stato recuperabile nella superficie ChatGPT Android.

**Ipotesi:** controlli nativi con stato condiviso possono modificare coerentemente la *stessa* mini-preview neutra; l'eventuale recupero dello stato richiede un passaggio esplicito verificato, non la sola memoria locale della UI.

**Specifica del gate autorizzato — G-UI-01:** una sola fixture neutra, senza fotografie personali; un unico selettore di colore per il layer `accent`, con due valori HEX espliciti: `#356B84` (iniziale) e `#B36A48` (alternativo). Una sola anteprima SVG deve leggere direttamente lo stato del controllo e aggiornarsi per entrambe le selezioni. Un pulsante reset deve ripristinare effettivamente il valore iniziale nella UI; questo reset locale non costituisce Undo versionato né prova di round-trip 002. Produrre uno snapshot JSON esplicito e dichiarare il meccanismo di trasferimento e recupero, verificando che il valore recuperato corrisponda a quello serializzato senza reinterpretazione. Il passaggio manuale di JSON dimostra soltanto recupero assistito, non sincronizzazione automatica. Un eventuale readback GitHub richiede autorizzazione specifica, commit effettivo, SHA verificato e rilettura remota. Nel contratto 002 il solo cambiamento funzionale accettato da `verify_transition()` è `layers[1].fill` insieme all'incremento di `revision`; `layers[1].visible` resta invariato ed è escluso dal PASS di round-trip 002. Nessuna estensione dello schema o del renderer. L'anteprima SVG reattiva non dimostra rendering fotografico finale, identità pixel o integrazione automatica con la CLI. Nessuna installazione, nuova app o generazione artistica.

**Criteri di esito proposti — separati per capacità:** comportamento locale PASS soltanto se entrambe le selezioni HEX aggiornano coerentemente la medesima anteprima SVG, il reset ripristina colore iniziale e anteprima e l'utente conferma la visualizzazione su ChatGPT Android. Recupero PASS soltanto se uno snapshot serializzato viene trasferito mediante il meccanismo dichiarato, riletto e confrontato sui valori senza reinterpretazione; distinguere esplicitamente recupero manuale e readback GitHub. Un PASS di recupero manuale non attesta persistenza o sincronizzazione automatica. Per ciascuna dimensione assegnare separatamente PASS, PARTIAL o FAIL; usare NON TESTATO per le capacità non esercitate. Un difetto bloccante impone stop e diagnosi, non ulteriori tentativi incontrollati. Il PASS del gate non certifica parità SVG/Pillow, compatibilità di un checkpoint con il round-trip 002, rendering fotografico o Undo versionato. Il gate è stato successivamente autorizzato dall'utente ed eseguito come descritto nel verbale seguente.

**Responsabilità:** la chiusura QA del G-UI-01 è registrata sotto. L'incremento stato → renderer neutro è stato successivamente autorizzato dal mandato G-UI-02 e verificato nel verbale seguente. Architettura candidata, NON decisione approvata: console progressiva → stato versionato → anteprima legata allo stato → renderer a livelli → revisioni circoscritte/Undo. Non estendere adesso lo schema tecnico 002.

### Verbale QA G-UI-01 — 10 novembre 2026

- **Autorizzazione ed esecuzione:** l'utente ha autorizzato espressamente G-UI-01. Nella chat ChatGPT Android è stato presentato un solo pannello con fixture SVG neutra e stato locale condiviso, selettore HEX `#356B84` / `#B36A48`, reset, snapshot JSON copiabile e campo per recupero manuale. Nessuna fotografia, installazione o generazione artistica.
- **Procedura richiesta:** Terracotta → Blu → Terracotta → copia JSON → Reset → incolla → Recupera. La prova è stata chiusa dall'utente con risposta testuale esatta `PASS` e note `nessuna`. Non sono allegati screenshot, tracce dei singoli click o copia dello snapshot effettivamente usato; la conferma è una **segnalazione diretta dell'utente**, non telemetria o prova automatizzata indipendente.
- **Comportamento locale: PASS (confermato dall'utente su Android).** La conferma riguarda selezione di entrambi i valori, aggiornamento della stessa preview SVG e reset. Implementazione del binding visibile nella chat; assenti misurazione pixel e cattura del dispositivo.
- **Recupero stato: PASS per recupero manuale assistito (confermato dall'utente su Android).** Snapshot della fixture `{gate, fixture, accent}` copiato, trasferito tramite campo di incolla, validato e riapplicato alla UI secondo la conferma complessiva. L'esatto payload copiato non è stato conservato nella repository: manca un readback indipendente dei byte del JSON; la prova attesta il percorso assistito, **non** persistenza automatica.
- **Fuori perimetro / NON TESTATO:** checkpoint persistente GitHub e readback del JSON, integrazione pannello → CLI 002, `schemaVersion=1.0.0`/round-trip 002, parità SVG/Pillow, renderer fotografico, lock pixel, Undo versionato, ripresa in nuova chat senza trasferimento manuale. Il JSON del pannello non va scambiato per lo schema della CLI 002.
- **Verdetto G-UI-01: PASS nel perimetro locale + trasferimento manuale, su conferma utente; evidenza indipendente limitata.** Nessuna stop condition segnalata. Non è un PASS end-to-end del prodotto, non modifica i FAIL T1-01/T1-02 né lo stato PARTIAL T0. I nuovi T1 rimangono **HOLD**.
- **Passo proposto all'epoca:** prova minima separata stato → renderer neutro 002. Il mandato G-UI-02 successivo ne autorizza l'esecuzione; esito e prossimo passo corrente sono nel verbale seguente.

**Coerenza documentale:** `README.md` rinvia già a questo piano; `AGENTS.md` chiede di iniziare dallo «Stato operativo». `docs/decisioni.md` e il piano skill system restano invariati. L'audit PR #11 conserva il proprio resoconto storico, mentre questo documento è l'unica sede del nuovo stato operativo. La presenza della PR #11 aperta non equivale alla sua integrazione.

### Verbale QA G-UI-02 — 10 novembre 2026

**Mandato:** chiusura integrale con soli strumenti/fixture/test esistenti; nessuna modifica di codice, schema, renderer o roadmap, nessuna installazione, generazione artistica, PR nuova o merge. Il mandato autorizza la registrazione delle evidenze, non il push su main. **Verdetto complessivo PARTIAL**, senza difetti nei controlli automatici eseguiti. T0 resta PARTIAL; nuovi T1 HOLD.

**Remoto verificato:** clone della repository canonica privata; `main`, HEAD remoto e checkout iniziale coincidono con `357b9b19e02fe7c90864ea6c75313d2c479403a8`. `git ls-remote origin HEAD refs/heads/main` ripetuto dopo i test conferma lo stesso SHA. PR #6 MERGED (2026-11-10 13:08:08 UTC; merge `48e64064566e90f09bcdd5c5a0025f25e3b7a60b`), PR #13 MERGED, PR #11 OPEN sul ramo `docs/android-photo-pilot-a-final-audit` a `0847f13e7fabd7c144b3598c0f6f4af3de43fcec`. Inventariati anche i tre branch remoti documentali e la storia dei file. Nessun lavoro G-UI-02 aperto individuato. Permessi GitHub restituiti dal connettore: admin/maintain/pull/push/triage; questi permessi non sono autorizzazione a scrivere su main.

**Registrazione:** solo questo documento canonico e i [log di evidenza](evidence/g-ui-02-20261110/) sul ramo `docs/g-ui-02-evidence-20261110`, senza PR e senza merge. La pubblicazione sul ramo non equivale a integrazione in main. JSON ricostruito e PNG temporanei restano fuori dal commit. Il contratto originale rimane [README-002](../tests/creative-console/README-002.md).

**Provenienza e integrità:** recuperati fixture, baseline/schema 1.0.0, renderer, CLI, entrambe le suite e checkpoint esistenti dal commit sopra. Non esiste uno schema JSON separato: il contratto eseguibile è `validate()` nel renderer più `verify_transition()` nella CLI; non è stata aggiunta alcuna validazione. Rilettura GitHub Contents API al medesimo SHA, decodifica base64 e confronto esatto con `git show SHA:path` per tutti gli 11 file elencati in [provenance.json](evidence/g-ui-02-20261110/provenance.json). La fixture coincide byte per byte anche nel checkout. I file testuali nel checkout hanno CRLF invece dei LF remoti: verificata esclusivamente questa differenza; gli hash fisici sono quindi distinti dagli hash canonici dello stato. Nessuna modifica tracked ai sorgenti dopo l'esecuzione. `roundtrip.py` riletto anche tramite connettore GitHub al commit esatto.

**Ambiente reale:** Windows, Python 3.13.7 MSC v.1944 AMD64, Pillow 12.1.1 già presente, zlib compilata/runtime 1.3.1. Nessuna installazione. I tempi seguenti sono quelli delle suite, non il tempo attivo utente.

**Procedura eseguita**, dalla directory `tests/creative-console` (directory `../../../evidence` creata prima dei comandi):

```powershell
python test-neutral-render.py -v
python test-roundtrip.py -v
python roundtrip.py export --baseline neutral-state.json --expected-revision 1 --fill '#B36A48' --out ../../../evidence/local-reconstruction-002.json
python roundtrip.py verify --baseline neutral-state.json --expected-revision 1 --state ../../../evidence/local-reconstruction-002.json
python neutral-render.py
```

Entrambe le suite, export, verify e renderer: **exit 0**. [Suite renderer](evidence/g-ui-02-20261110/test-neutral-render.txt): 6 test, 0,235 s, OK. [Suite round-trip](evidence/g-ui-02-20261110/test-roundtrip.txt): 7 test, 0,242 s, OK. [Export](evidence/g-ui-02-20261110/export.txt) e [verify](evidence/g-ui-02-20261110/verify.txt) restituiscono fingerprint identici. [Rendering Pillow](evidence/g-ui-02-20261110/render.txt) realmente eseguito: due PNG prodotti dal renderer originale, senza generazione artistica. La sua funzione main riscrive la fixture con i medesimi byte: hash invariato e nessun diff tracked.

Un primo tentativo aveva creato la directory dei log al livello sbagliato: Tee-Object non ha salvato le suite e export/verify sono falliti con FileNotFoundError. Il renderer era già riuscito. Corretta solo la directory, rieseguiti i comandi sopra con output conservato; il primo tentativo non è contato come prova positiva delle suite. Una stampa preliminare dei commenti PR ha inoltre incontrato l'encoding cp1252 della console: contenuto riletto in UTF-8, nessun file sorgente modificato.

**Recupero locale effettivo e invarianti:** ricaricato il file esportato attraverso `load()`, eseguito `verify_transition(baseline, recovered, 1)`, confrontati i byte del file con `canonical(recovered).encode('utf-8')`. Diff ricorsivo esatto: soltanto `layers[1].fill` da `#356B84` a `#B36A48`, e `revision` da 1 a 2. `visible`, asset, lock, approvazioni, canvas, template, renderer e ogni altro dato restano invariati. Render ripetuti dello stato recuperato identici al PNG salvato da `neutral-render.py`; baseline verificata nello stesso modo. Riscontri in [verification.json](evidence/g-ui-02-20261110/verification.json); nessun nuovo test aggiunto alla suite.

| Oggetto | SHA-256 ricalcolato |
|---|---|
| Fixture originale, baseline e candidato asset | `0fa828ab7b46009c890168addcca6db0bfb87e0baf75799a42abe93ba342e55a` |
| Baseline JSON remoto, byte fisici LF | `324c03e3f6a01357dc0e0871d977eac06ad1d12f886a49bdfb95da2ec7961d36` |
| Baseline stato canonico rev1 | `56acf2e2c721477e7acda0dc965828a1563ad03ccc003119da3510271f564fe2` |
| Export locale e stato recuperato canonico rev2 | `0db6350e1db07dcb9753e7f987fe4c9d219eded099007396161380283b0fc235` |
| Render Pillow rev1 | `9008d249614a42e17f081ff58c2e41305a702167a68a8769dcbecd312caa0260` |
| Render Pillow rev2 terracotta | `f3ff5342d177339421336a5afa420fb8d0fa269717a431cee124a8fee469e3ed` |

Hash fixture identico a quello dichiarato nella baseline; hash stato rev1 e render rev1 identici al [gate storico PR #6](https://github.com/Matteo-Exp-Transformer/generazione-contenuti-GPT-SOCIAL/pull/6#issuecomment-6767783732). Rev2 stato e render differiscono da rev1 come previsto, e coincidono tra export, verifica, recupero e rendering ripetuto. Non esiste un raster originale Android G-UI-01 da confrontare. L'hash PNG è verificato in questo ambiente, non garantito fra encoder/versioni differenti.

**Tutti i casi delle suite eseguiti:** renderer: repeatable, single_property, diff_localized, snapshot_restore, locked_and_stale, tampered_asset; round-trip: export_import_and_recovery, only_fill_and_revision, stale_revision, tampered_asset, unrelated_change, noop_rejected, cli_export_verify. I negativi rifiutano revisione obsoleta, layer locked, hash asset dichiarato alterato, byte fixture alterati (mock in memoria), projectId estraneo e no-op. Il test raster misura esattamente 480×90 = 43.200 pixel cambiati, tutti dentro x=[60,540), y=[100,190). Il ripristino da snapshot riottiene i byte del render iniziale. PASS riferito a questi casi effettivi; non si afferma copertura esaustiva di input arbitrari o dello schema.

**Android originale vs ricostruzione:** ricerca nel tree e nella storia disponibile di main e dei tre branch remoti; consultati il verbale G-UI-01 e i commenti della PR #6. Il verbale G-UI-01 dichiara assente il payload effettivamente copiato; nessun originale recuperato. Lo snapshot del pannello era `{gate, fixture, accent}`, non uno stato schema 1.0.0; non esiste un import di quel formato nella CLI originale. Convertirlo usando la baseline sarebbe un adattamento locale da dichiarare, non un import nativo o una prova dell'origine Android. Il candidato terracotta di questa run è **ricostruzione locale dalla baseline tramite CLI**, non export Android. Non è pubblicato come checkpoint.

Il checkpoint versionato `microtest-neutral-001-rev2.json` è verde `#3F8064`, con hash remoto `b555e5871e7528a51e266c0973038e5070530fb7b6dc3c8d7c4e4b444da6f5f3`: proviene dal precedente percorso 002, non da G-UI-01. Il [report di handoff storico](https://github.com/Matteo-Exp-Transformer/generazione-contenuti-GPT-SOCIAL/pull/6#issuecomment-6767722400) distingue esplicitamente payload osservativo Android e costruzione locale; il [readback storico](https://github.com/Matteo-Exp-Transformer/generazione-contenuti-GPT-SOCIAL/pull/6#issuecomment-6767834091) non sana la lacuna G-UI-01. Il checkpoint 003 è un concept e non input di questo renderer. Nessun accesso al dispositivo o al transcript originale G-UI-01 disponibile in questa sessione.

**Riesame QA delle evidenze:** riesaminati i report precedenti senza assumere veri i loro PASS; confrontati commit, colori, formati e hash con i dati remoti. Verifiche automatiche locali, osservazioni Android riferite, ricostruzioni e capacità non esercitate rimangono distinte. Il controllo conclusivo delle nuove evidenze è svolto dallo stesso agente che ha eseguito i comandi: non costituisce una seconda firma indipendente. Non è stato coinvolto un secondo revisore né attestata indipendenza organizzativa.

| Dimensione | Verdetto | Evidenza / limite |
|---|---|---|
| Remoto, PR, provenienza e integrità sorgenti | PASS | SHA fissato, readback API e confronti byte/LF |
| Suite Python originali | PASS | 13/13 effettivi, nessuna installazione |
| Export → verify → recupero locale | PASS | Fingerprint e byte canonici identici |
| Render Pillow ripetibile | PASS | PNG realmente prodotti e ricalcolati |
| Uniche modifiche fill/revision | PASS | Diff esatto e test single-property |
| Asset e regioni protette | PASS | Hash fixture e diff 43.200 pixel localizzato |
| Negativi previsti e ripristino locale | PASS | Tutti i casi delle suite sopra elencati |
| G-UI-01 comportamento e recupero manuale | PASS riferito | Conferma utente storica; non ripetuta |
| Snapshot originale G-UI-01 → stato 002 | PARTIAL | Originale assente; sola ricostruzione locale verificata |
| Checkpoint Android terracotta e cold recovery | PARTIAL | Non eseguiti; nessun checkpoint originale da pubblicare |
| Riesame documentale e limiti di prova | PASS | Report storici confrontati con remoto e nuove misure |
| Seconda revisione indipendente della nuova run | PARTIAL | Nessun secondo revisore |
| Parità SVG/Pillow, foto, sync, refresh, Undo versionato | PARTIAL / NON TESTATO | Fuori dalle capacità esercitate, nessuna attestazione |
| G-UI-02 complessivo | **PARTIAL** | Tecnica locale PASS; catena originale Android mancante |
| T0 / nuovi T1 | **PARTIAL / HOLD** | Nessuna promozione o riavvio |

**Stop condition corrente:** manca lo snapshot originale. Fermare la promozione a PASS Android/end-to-end; non creare un sostituto, non cambiare il formato/schema o il renderer per superare il blocco. Eventuali differenze nei valori o una provenienza dubbia richiedono diagnosi prima di qualsiasi pubblicazione di checkpoint. Le suite verdi non autorizzano nuovi T1.

**Passo storico superato (non eseguire):** la richiesta dello snapshot G-UI-01 non è più operativa. Decisione successiva dell'utente: proseguire senza richiederlo nuovamente. Rimane G-UI-02 PARTIAL; non ricostruire l'originale né promuovere la catena Android → renderer 002 a PASS.

### Addendum G-UI-02-RETEST — ChatGPT Android, 10 novembre 2026

**Prova distinta, non sostitutiva dell'originale G-UI-01.** Nella chat normale ChatGPT su Android (secondo dichiarazione dell'utente e screenshot allegato alla conversazione) è stato eseguito un pannello interattivo con preview SVG neutra, selettore Blu `#356B84` / Terracotta `#B36A48`, Reset, Crea snapshot, copia JSON, campo d'incolla e Recupera. L'utente dichiara: «Si torna terracotta anche se metto blu e poi clicco recupera». Uno screenshot finale mostra selettore e preview Terracotta, snapshot JSON, campo d'incolla con gli stessi valori e messaggio dell'interfaccia «JSON valido: colore recuperato Terracotta.»

Payload **visibile nello screenshot**, trascritto come valori JSON (non recuperato indipendentemente dagli appunti originali né confrontato byte per byte con clipboard):

```json
{
  "gate": "G-UI-02-RETEST",
  "fixture": "neutral-color-chat-v1",
  "accent": "#B36A48"
}
```

**Verdetto circoscritto:** PASS riferito dall'utente e corroborato visivamente per recupero manuale assistito del colore; comportamento finale terracotta visibile. Il codice del pannello ha validazione locale di struttura, gate, fixture e accent e associa il valore accettato alla preview, ma non sono disponibili log indipendenti delle singole interazioni, acquisizione clipboard o telemetria di dispositivo. Lo screenshot finale non dimostra da solo l'intera sequenza Terracotta → Blu → Terracotta → snapshot → Reset → incolla → Recupera. Client: normale chat ChatGPT Android; versione/build esatta del client non rilevata durante la prova. L'immagine rimane allegato della conversazione; non è stata caricata nel repository.

**Limiti e stato invariato:** il JSON `{gate,fixture,accent}` NON è lo schema renderer 002. Non dimostrati trasferimento nativo al renderer 002, parità SVG/Pillow, sincronizzazione, persistenza automatica, cold recovery, Undo versionato o fedeltà fotografica. Non recuperato lo snapshot originale G-UI-01; non richiederlo nuovamente. **G-UI-02 complessivo PARTIAL; T0 PARTIAL; nuovi T1 HOLD.** Nessuna nuova PR, modifica a codice/schema/roadmap o push su main.

**Unico prossimo passo:** riesame indipendente dell'addendum e delle prove già presenti sul branch, mantenendo i limiti di provenienza e senza avviare nuovi T1.

### Riesame indipendente documentale — 10 novembre 2026

Verificati tramite GitHub repository privata, permessi push, esistenza del branch `docs/g-ui-02-evidence-20261110`, commit `497864ef318b8aec4ceccbfa7aa3f767161a5f7f` e diff con `main` (2 commit avanti, 0 indietro al momento del controllo). I log e gli hash del gate tecnico sono evidenze precedenti rilette, non suite rieseguite in questo riesame. Conferma dell'utente e descrizione dello screenshot dimostrano soltanto il recupero manuale assistito e lo stato finale terracotta, non la sequenza completa osservata indipendentemente. Lo screenshot originale `g-ui-02-retest-android-20261110.jpg` non è risultato accessibile tra gli allegati/file disponibili e non esisteva nel percorso GitHub previsto al controllo: impossibile verificarne JPEG reale e SHA-256 atteso `969dc8d96d6ebe68a98ee48a8c4579b50305b3bab719bda195c5a0065366a121`; nessun sostituto pubblicato. Il payload `{gate,fixture,accent}` non è un documento renderer 002. Restano NON TESTATI import nativo, persistenza automatica, cold recovery, parità SVG/Pillow su origine Android, compositing fotografico e conservazione delle scelte durante revisioni reali. **Verdetti invariati: G-UI-02 PARTIAL, T0 PARTIAL, nuovi T1 HOLD.**

**Unico prossimo passo proposto, soggetto ad autorizzazione separata per l'esecuzione:** definire un micro-gate di modifica circoscritta su una fotografia originale già disponibile, con checkpoint delle scelte approvate e verifica prima/dopo della sola modifica richiesta. Prima della prova fissare criteri di preservazione di asset, testo e layout; non avviare nuovi T1 e non alterare schema o renderer senza autorizzazione.

## Direzione di prodotto e ragioni della prova

Il [PRD](PRD-v0.1.md) punta al post statico professionale. [FORMA](../benchmarks/FORMA-001/risultati.md) ha mostrato problemi di fedeltà ai testi; [LAYER](audit-layer-001-handoff.md) il costo delle microdecisioni; [Istanbul](report-run-ecovillaggio-istanbul-2026-11-09.md) il fallimento del confronto quando le varianti sono invisibili sul telefono. Nel [Tattoo](audit-run-tattoo-console-guidata-2026-11-10.md) l’estetica scelta è andata persa durante una revisione del titolo. Il valore da verificare è il controllo dell’utente su quella revisione.
   
La [002](https://github.com/Matteo-Exp-Transformer/generazione-contenuti-GPT-SOCIAL/pull/6) ha prove tecniche recuperabili su un template neutro e un cambio di colore. La [003](audit-creative-console-003-cold-test-2026-11-10.md) ha dimostrato recuperabilità documentale del concept. Un template per foto reali, la parità fra preview e post e il ripristino automatico della UI rimangono aperti. Provare prima la console guidata; valutare un solo template produttivo se il concept supera il pilota. Preset multiprogetto, backend e sistema modulare richiedono casi che ne mostrino il beneficio.

## Checkpoint sperimentale e riferimento visivo

Tenere distinte parole dell’utente, valori applicati e scelte ancora delegate. “Asimmetrica” permette una ripresa concettuale; per ricostruire una pagina servono anche fonte e parametri effettivi. La Chat A redige il checkpoint strutturato e lo conserva nella repository insieme al riferimento visivo della stessa revisione, in file distinti, senza estendere lo schema o il renderer 002.

| Da registrare alla conferma | Dettaglio utile |
|---|---|
| Identità e ambito | ID del caso, revisione e precedente, frase di approvazione, cosa è approvato (idea, layout o asset). |
| Sorgenti e composizione | Foto originale recuperabile se condivisa; hash solo se calcolato sui byte. Template e versione o descrizione libera. Per una composizione effettivamente impostata: formato, origine e unità, ritaglio, posizione/scala, ordine dei livelli, zone protette e modifiche consentite. |
| Testo e stile | Stringhe esatte, palette con valori e ruoli, font/peso/dimensione e allineamento se effettivamente impostati. Identificare valori proposti, confermati, misurati, delegati o mancanti. Vietato stimare coordinate o font da uno screen per poi registrarli come approvati. |
| Revisione e undo | Revisione prima/dopo, unica modifica richiesta, differenze osservate, ultima revisione approvata e risultato dell’undo. Un undo in chat dimostra il ripristino dei valori testuali; per il ripristino visivo serve la preview. |
| Riferimento visivo opzionale | Un solo screen della preview approvata sul telefono, collegato a ID/revisione e indicato come schema o raster. Ritagliare notifiche, dati personali e contenuti estranei. Registrare ciò che era davvero visibile. Se lo screen manca, il controllo visivo resta aperto. |

Lo screen conserva l’aspetto visto, compresi a capo e ritaglio. L’originale e i parametri consentono di intervenire di nuovo. Una discrepanza fra screen e dati blocca solo la parte ambigua: mostrare il conflitto e chiedere quale versione vale. L’identità del file sorgente richiede un confronto sui byte; l’invarianza dell’immagine composta richiede un confronto delle regioni protette nelle stesse condizioni di rendering.

> **PROTOCOLLO STORICO — SOSPESO, NON ESEGUIRE.** La sezione «Due chat, un solo caso» documenta la procedura precedente ai fallimenti T1 e rimane disponibile esclusivamente come riferimento storico. Le istruzioni imperative che seguono non costituiscono un mandato operativo né autorizzano nuovi piloti A/B. Prevale lo Stato operativo/HOLD sopra riportato; ogni ripresa richiede una decisione e un'autorizzazione esplicite dell'utente.

## Due chat, un solo caso

**A — direzione su Android.** Brief naturale e foto originale. Due direzioni descritte a parole. Dopo la selezione, pannello progressivo con mini-preview di messaggio, stile, palette e composizione; lasciare spazio a testo libero e ad altre idee mantenendo la selezione. Schemi esplicitamente etichettati; per giudicare la fotografia usare solo la stessa foto reale inline, se l’utente autorizza il confronto. Cambiare il solo titolo, provare undo, scegliere una revisione e approvarla esplicitamente. La Chat A compila checkpoint e registro di utilizzo. Mostra la preview inline. Per attestare la vista sul telefono, l’utente cattura lo schermo della revisione approvata e lo allega in A, salvo disponibilità dimostrata di una cattura diretta del dispositivo. Identificare un eventuale raster esportato dall’agente come preview. Se le preview richieste non sono visibili sul telefono, fermare la fase visiva e registrare il limite. Produzione finale e archiviazione di foto/screen su GitHub richiedono autorizzazione specifica.

**B — ripresa indipendente.** Nuova chat, senza transcript o suggerimenti sulla risposta attesa. La Chat A consegna un messaggio di avvio per B con URL repo, SHA e percorso del checkpoint. L’utente copia solo il messaggio. La Chat B legge da GitHub esclusivamente il checkpoint, senza aprire PR, immagini o dati di utilizzo, e pubblica la prima risposta: scelte esatte recuperate, elementi protetti, modifiche ammesse, dati mancanti e prima azione consentita. Nel turno successivo B apre dal medesimo SHA lo screen collegato nel checkpoint. A usa nomi neutri nella stessa directory, ad esempio checkpoint.json e screen-android.png, e verifica da remoto JSON e immagine prima di consegnare. Se i byte non sono accessibili in una delle chat, dichiarare il limite e usare l’allegato manuale solo come ripiego. Registrare quali dettagli conferma, contraddice o chiarisce e quali rimangono incerti. L’utente confronta le due letture con l’approvazione di A. Un allegato manuale prova il trasferimento assistito; una ripresa autonoma da GitHub richiede un checkpoint effettivamente pubblicato e riletto. Nessuna necessità di ripetere il cold test 003.

## Esiti da raccogliere

- A: numero di turni utente dal brief all’approvazione o allo stop; richieste di ripetere un vincolo; confronti mostrati/visibili; uso di testo libero, altre idee e undo; modifiche collaterali. Tempo attivo solo se misurato. Una frase dell’utente su ciò che ha facilitato o impedito la scelta.
- B: campi approvati corretti/totale effettivamente presenti, omissioni, valori inventati, contraddizioni, chiarimenti richiesti e differenze fra lettura dei soli dati e lettura con screen. Indicare prove disponibili e limiti. Senza screen l’incremento informativo resta non valutabile.
- **PASS** per la direzione creativa se l’utente vede e distingue le alternative, approva e riesce a modificare/ripristinare solo il titolo. **PASS** per la ripresa se B recupera le scelte esplicite, rispetta i vincoli e segnala gli ignoti senza inventare. **PARTIAL** per un passaggio recuperato manualmente, una scelta ambigua o una verifica visiva mancante; **FAIL** per perdita della scelta, confronto essenziale inutilizzabile o modifica non autorizzata. Valutare separatamente capacità di ricostruzione esatta: senza dati e confronto idonei resta non verificata anche se il concept è recuperabile.
- Riunire esiti A/B e un solo prossimo incremento nel medesimo resoconto. Il registro di utilizzo di A resta fuori dal checkpoint; B lo consulta solo dopo il proprio verdetto. Se è autorizzata l’archiviazione, verificare PR e ramo esistenti, salvare un unico esito pertinente e rileggere il contenuto remoto. Nessun file vuoto o audit preventivo.

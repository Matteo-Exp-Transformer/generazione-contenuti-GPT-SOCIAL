# GPT SOCIAL — Audit run Tattoo: salto della console e perdita di continuità visiva
Data: 2026-11-10 · Stato: audit di run, non protocollo approvato · Branch: `proposal/layer-001-workflow-v02`

## Perimetro e riferimenti
Simulazione GUIDATA in ChatGPT Android con fotografia originale di un avambraccio tatuato, obiettivo post per studio underground/dark. Nessun post definitivo né preset persistente. Questo audit registra **un fallimento nuovo e specifico** e rimanda, senza duplicarli, a `docs/audit-creative-console-android-handoff-2026-11-10.md`, `docs/protocollo-ui-android-test-2026-11-10.md` e `docs/decisioni.md`. La governance canonica resta da coordinare con il Product Manager parallelo.

## Sequenza osservata
1. L'utente fornisce fotografia, contesto commerciale e stile underground. Il brief minimo è già sufficiente per una console iniziale.
2. L'agente propone tre direzioni estetiche con controlli nativi e riceve **Dark Grunge, 4:5**.
3. Mostra due composizioni raster deterministiche con fotografia originale; l'utente rifiuta entrambe.
4. Dopo la scelta «composizione grafica», l'agente **salta il pannello di template** e genera autonomamente un collage con carta strappata, cornice, nastro adesivo, texture e titolo. La proposta è apprezzata per intensità grafica.
5. La generazione non fornisce livelli o parametri ricostruibili con identità pixel; inoltre l'output generativo non garantisce identità fedele della fotografia originale.
6. Alla richiesta di una sola modifica, l'agente produce con Pillow un raster deterministico con foto originale, ma cambia contemporaneamente cornice, decorazioni e titolo: l'estetica approvata viene persa.
7. L'utente ferma il test: le proposte che vincolano le aspettative devono essere riproducibili e modificabili; la console avrebbe dovuto governare il template **prima** di qualunque generazione.

## Diagnosi: responsabilità separate
**Errore di esecuzione confermato.** L'agente non ha applicato il pannello come centro decisionale, benché il mandato della run lo richiedesse e l'handoff precedente già descrivesse «pannello nativo in chat come centro decisionale». Ha introdotto decorazioni non selezionate e modificato più variabili dopo l'approvazione. Non è giustificabile come mera ambiguità del prompt.

**Lacuna di enforcement proposta per verifica.** La documentazione precedente ammetteva proposte visive e generazione assistita, ma non formalizzava ancora un gate esplicito «template parametrico e riproducibilità verificata prima di qualsiasi anteprima vincolante». Non attribuire automaticamente tutta la responsabilità al metodo: distinguere norma esistente, sua mancata applicazione e nuova regola proposta.

**Problema UX.** L'utente si affeziona a un risultato visivo che poi non può più selezionare e sviluppare: sfiducia, tentativi ripetuti, costi cognitivi e creativi. Il fatto che il secondo raster sia riproducibile non compensa la perdita del primo.

## Feedback utente e correzione proposta
- In fase di **proposta** restare su idee, palette, template, posizione e componenti; non produrre composizioni creative generative che diventino implicitamente vincolanti.
- Proporre prima la cornice underground come **template/opzione**, non inventarla e applicarla autonomamente.
- Usare la **Creative Console come interfaccia principale** fin da quando foto e brief minimo sono disponibili; il pannello configura e modifica elementi del template.
- Anteprime di progettazione sì, ma **deterministiche, parametrizzate e realmente visibili inline su Android**. «Non generare l'immagine» significa non usare generazione creativa non riproducibile, non vietare preview tecniche della foto originale con overlay.
- Progettare un template riproducibile prima della produzione; alla fine rendering del post e, soltanto se autorizzata e necessaria, generazione AI per specifici asset.
- Fotografia originale immutabile; crop e overlay non generativi separati. Modifiche a una variabile alla volta, con lock, undo e snapshot; non promettere persistenza non verificata.

## Workflow candidato, NON ancora convalidato
1. **Brief minimo**: obiettivo, foto/materiali, identità, vincoli; una o poche domande conversazionali.
2. **Console essenziale**: formato, palette visiva, 2–3 template strutturali; preview schematiche o deterministiche, nessuna generazione creativa.
3. **Componenti opzionali**: cornice, texture, nastro, titoli, posizione, dimensioni, visibilità; proporli prima, aggiungerli solo dopo selezione. Mostrare pochi controlli per volta.
4. **Stato unico versionato**: asset originale, template ID/versione, parametri, livelli, elementi approvati/bloccati, snapshot, differenze tra varianti. Preview = funzione dello stato, non un'immagine reinterpretata.
5. **QA pre-produzione**: confermare fedeltà della preview e che la modifica localizzata lasci invariato tutto il resto.
6. **Render finale** solo dopo approvazione e autorizzazione; eventuali asset generativi separati e dichiarati. Preset temporaneo distinto da salvataggio persistente.

## Limiti tecnici e premortem
- I controlli nativi e `DIL.useState` dimostrano interazione locale, **non** editor raster completo, salvataggio fra chat o binding automatico al renderer.
- Preview SVG/HTML e raster Pillow possono differire per font, antialiasing, crop e misure: serve un contratto di rendering e test di regressione.
- Se la console contiene tutti i controlli subito, ricrea sovraccarico: progressive disclosure e default essenziali.
- Se i template sono troppo rigidi, la creatività si impoverisce: componenti componibili e escape hatch esplicita, senza generazione implicita.
- Se lo stato è solo nella UI del turno, undo/preset e handoff si perdono: serializzazione esplicita e verifica della persistenza prima di prometterla.
- Se l'agente modifica più parametri, la fiducia crolla: diff per proprietà, confronto A/B a variabile unica e test.
- Se le preview Android non sono leggibili, non sostituirle con download: test sul client e fallback dichiarato.

## Test di accettazione per agente successivo
1. Con foto e brief minimo, aprire una console nativa **prima** di qualsiasi proposta generativa.
2. Mostrare 2–3 template riproducibili e una palette selezionabile visivamente; verificare visibilità Android con feedback utente.
3. Aggiungere una cornice **solo dopo selezione**; verificarne identità prima/dopo una modifica del titolo.
4. Testare un toggle e uno slider che cambiano solo la proprietà dichiarata nella preview; verificare reset/undo.
5. Serializzare lo stato del template e riprodurre lo stesso render due volte; misurare differenze, non presumere pixel identity.
6. Dimostrare snapshot temporaneo e dichiarare esplicitamente se il preset **non** è salvato permanentemente.
7. Nessuna produzione finale, installazione, spesa o modifica repository senza autorizzazione.

## Handoff
**Agente indipendente:** verificare questa diagnosi contro i documenti esistenti; proporre il minimo enforcement in AGENTS/protocollo senza duplicazioni; definire contratto stato→preview→render e premortem; preparare micro-test Android e prompt per agente di consolidamento. Coordinare con PM parallelo prima di toccare fonti canoniche. **Prossimo passo unico:** revisione indipendente della console-first workflow prima di una nuova run.

## Stato delle decisioni
Fatti della run e feedback utente: osservati. Console-first e stop alla generazione prematura: correzioni esplicitamente richieste dall'utente per il futuro workflow. Architettura, persistenza, test e aggiornamenti ai protocolli: **proposte da verificare**, non funzionalità implementate.

## Aggiornamento decisioni utente — 2026-11-10 (Creative Console)

Decisioni esplicitamente confermate per il **piano e il prossimo micro-test**, non prova di implementazione:
- Workflow **Console-first GUIDATA**: progettazione prima di qualsiasi generazione AI; nessun post definitivo.
- **Architettura ibrida**: pannello nativo di chat per decisioni e anteprima reattiva, renderer deterministico per asset reali; entrambi leggono una specifica strutturata/versionata. L'equivalenza visiva è da testare, non presunta.
- **Persistenza del primo prototipo anche nella repository**, oltre a JSON esportabile/ripristinabile, per sicurezza e continuità agentica. Scrittura esplicita su ramo di lavoro/PR, non su main, con consenso operativo per i singoli salvataggi; niente commit automatici a ogni interazione. Salvare configurazioni e riferimenti, non duplicare asset o inserire foto private senza autorizzazione specifica. Verificare la rilettura dal repository prima di dichiarare un preset persistente.
- **Prossimo esperimento: micro-test tecnico isolato**, non simulazione Tattoo completa. Testare UI Android → stato → preview reale → renderer, modifica localizzata, snapshot e ripristino, hash della foto e continuità tra turni.
- Stato del pannello locale, snapshot, JSON esportato e preset persistente sono quattro condizioni diverse; mostrarle distintamente.

**Coordinamento metodo:** il piano di continuità consolidato su `main` è `docs/PLAN-skill-system-minimo-2026-11-10.md`; `AGENTS.md` su main include già regole di pulizia branch, verifica diff e chiusura PR. Non creare un nuovo file canonico di stato, non duplicare il piano del PM e non fondere il ramo creativo senza revisione del diff. Il presente aggiornamento registra solo decisioni Creative Console nel documento esistente. Prima di ogni implementazione verificare la base corrente e l'eventuale lavoro parallelo.

**Prossima azione unica:** agente indipendente consolida il contratto JSON e il micro-test con criteri di accettazione; solo dopo autorizzazione separata si esegue il test tecnico su Android.

## Micro-test tecnico Creative Console 001 — esecuzione parziale autorizzata

- Perimetro: fixture neutra; nessuna fotografia privata, post Tattoo o generazione creativa. Non modifica le decisioni del caso Tattoo.
- File nuovi: `tests/creative-console/neutral-state.json`, `neutral-render.py`, `test-neutral-render.py`. Fixture PNG generata a runtime e non committata; nessuna installazione.
- Ambiente locale: Pillow 12.3.0 già presente. Comando: `cd tests/creative-console && python test-neutral-render.py && python neutral-render.py`.
- **Verificato localmente:** 6/6 test Python superati: doppio render, modifica di un solo campo, diff raster limitato a 480×90=43.200 pixel, snapshot/ripristino, lock/revision stale, hash asset alterato rifiutato.
- Hash fixture neutra: `0fa828ab7b46009c890168addcca6db0bfb87e0baf75799a42abe93ba342e55a`. Hash raster iniziale: `95e0e87ac42fee7a9e75de59e86c34b8206203a9fe1b8784444eed6c26740263`; variante: `6baa32e64811df33846babc8f5239921743e894c9175d29e9c041de1a95ea543`. Valori relativi all'ambiente locale di test, non certificazione cross-platform.
- **GitHub verificato:** tre file scritti nel ramo creativo, ultimo commit `66c7e97290a2032f32c08eae957ecb68ee494c13`; tutti e tre riletti tramite fetch_file dal ramo. Non equivale a verifica di esecuzione su GitHub.
- **Non ancora verificato:** interazione del pannello su Android nel presente micro-test; collegamento diretto fra componente UI e renderer Python; equivalenza pixel della preview Android; ripresa realmente indipendente in una chat senza cronologia.
- **Limite esplicito:** il pannello nativo può aggiornare lo stato locale, ma non esegue automaticamente il codice Python nel repository; non dichiarare pipeline end-to-end completa.
- **Prossima azione unica:** verificare sul dispositivo Android il pannello neutro con una modifica e undo, poi affidare a un agente senza cronologia la rilettura del checkpoint. Non riaprire la produzione Tattoo prima dell'esito.

## Aggiornamento verifica Android e recupero documentale — 2026-11-10

- **Android, conferma utente:** nel client Android anteprima, cambio colore, undo, snapshot e ripristino funzionano correttamente. Evidenza dichiarativa dell'utente, non acquisizione automatizzata del client o test raster cross-engine.
- **Recupero GitHub ripetuto:** letti autonomamente dal ramo creativo `neutral-state.json`, `neutral-render.py`, `test-neutral-render.py` e questo audit; consultati `AGENTS.md` e il piano su `main`. JSON: `microtest-neutral-001`, schema `1.0.0`, revisione `1`, colore `#356B84`, asset `asset-neutral-01`, renderer `pillow-v1`. Il test si lancia con `cd tests/creative-console && python test-neutral-render.py` dove Pillow è già disponibile.
- **Limite fondamentale:** questo recupero è svolto dallo stesso agente/conversazione; NON è un test indipendente a freddo. Il colore selezionato sul pannello Android non è stato automaticamente committato: il checkpoint GitHub rappresenta lo stato iniziale, non l'ultimo stato locale del pannello.
- **Stato T8:** preparato, non superato. Prossima azione unica: aprire una nuova conversazione/agente senza cronologia e richiedere recupero di stato, vincoli e prossima azione usando solo repository e SHA di checkpoint. Non generare immagini o modificare repository nel test.

## Cold Test Creative Console 001 — revisione documentale indipendente (2026-11-10)

**Mandato:** sola lettura delle fonti durante il test, senza esecuzione di test, installazioni, generazioni o produzioni. Questa sezione viene depositata successivamente su richiesta esplicita dell'utente. **Checkpoint esaminato:** `895664406691a2156acc310466e60b2b261147c6`. **Branch del caso:** `proposal/layer-001-workflow-v02`. Il giudizio riguarda quel checkpoint, non modifiche successive.

### Percorso effettivo di recupero e fonti

1. Letto `AGENTS.md` da `main` (blob `d7ccd0ee5f0330f0e8e1c5a04c0b0f202adc51e9`): lettura mirata, distinzione fatti/ipotesi/proposte, divieto di dichiarare test non eseguiti, fonte canonica unica, pulizia branch/PR.
2. Letti `README.md` (blob `338f1e28557839870ba1320e2c624c5a1902eb47`) e `docs/decisioni.md` (blob `ec4b40183673d4861207ff540f7376d0c308e1b5`) al checkpoint: il README descrive ancora il benchmark FORMA-001; il registro decisioni non è una prova del micro-test.
3. Recuperato direttamente il commit `895664406691a2156acc310466e60b2b261147c6`, messaggio `docs: record Android user validation and cold-handoff boundary`, che aggiorna questo audit.
4. Letto integralmente questo audit al checkpoint (blob `4cc6598e8ef9082ed5fdcdd40706974fc2338698`).
5. Recuperati direttamente al checkpoint i tre file tecnici, con blob: `tests/creative-console/neutral-state.json` (`65824f59dff94e51103a31a2ef5c6d0c0a52c686`), `neutral-render.py` (`ca12ae3e46d0945fd8f104272fbc0acf0b95893f`), `test-neutral-render.py` (`3f65544615642eb5b25bf42225cd4257544505c8`).
6. Consultato su `main` il piano `docs/PLAN-skill-system-minimo-2026-11-10.md` (blob `792c0a3b856605502263ceed1447578d665c5eac`) per i criteri di ripresa e i limiti del pilot.

**Indipendenza:** la ricostruzione tecnica in questo test è stata fatta usando le fonti GitHub, senza citare cronologie o memorie come prova. Non è tuttavia certificabile dal solo contenuto della risposta l'isolamento tecnico della sessione rispetto a qualsiasi contesto precedente. Non attribuire per questo un PASS assoluto alla prova cold-start.

### Contratto tecnico effettivamente letto

- `projectId=microtest-neutral-001`, `schemaVersion=1.0.0`, `revision=1`.
- `canvas={width:600,height:750,background:"#F3F0E8"}`.
- `template={id:"neutral-card",version:"1.0.0"}`.
- Asset neutro `asset-neutral-01`, `kind=fixture`, URI `fixtures/neutral.png`, `immutable=true`, SHA-256 `0fa828ab7b46009c890168addcca6db0bfb87e0baf75799a42abe93ba342e55a`. Fixture prodotta a runtime, non fotografia privata né file PNG committato.
- Layer `background`: immagine approvata e bloccata. Layer `accent`: rettangolo visibile, `fill=#356B84`, `bounds=[60,100,480,90]`, non approvato e non bloccato.
- Renderer `pillow-v1`, versione `1.0.0`; `neutral-render.py` usa Pillow, genera fixture e render in memoria e valida schema, asset, template, layer e revisioni. `change_fill` incrementa la revisione e rifiuta una revisione attesa obsoleta. Il comando storico indicato è `cd tests/creative-console && python test-neutral-render.py && python neutral-render.py`; **non eseguito in questo cold test**.

### Test documentati: distinguere codice, esecuzione storica e verifica attuale

L'audit storico dichiara Pillow 12.3.0 disponibile e **6/6 test Python superati localmente**. La lettura del codice conferma che esistono i seguenti sei test:
1. `test_repeatable`: confronto degli hash di due chiamate al medesimo renderer sul medesimo stato; **non** dimostra equivalenza tra motori o dispositivi.
2. `test_single_property`: verifica che cambino soltanto `layers[1].fill` e `revision`.
3. `test_diff_localized`: confronto raster con esattamente 480×90 = 43.200 pixel modificati, nell'area x=60..539 e y=100..189.
4. `test_snapshot_restore`: serializzazione JSON, ripristino e uguaglianza dei byte del rendering ripristinato.
5. `test_locked_and_stale`: errori attesi per layer bloccato e revisione obsoleta.
6. `test_tampered_asset`: rifiuto di hash asset falsificato.

Hash dei raster **riportati nel precedente audit**, non ricalcolati: iniziale `95e0e87ac42fee7a9e75de59e86c34b8206203a9fe1b8784444eed6c26740263`; variante `6baa32e64811df33846babc8f5239921743e894c9175d29e9c041de1a95ea543`. Commit storico dei tre file: `66c7e97290a2032f32c08eae957ecb68ee494c13`. Questo revisore ha letto i sorgenti, **non** ha eseguito Python né verificato i PNG su Android.

**Android:** il checkpoint registra conferma dichiarativa dell'utente che anteprima, cambio colore, undo, snapshot e ripristino funzionano sul dispositivo. Non è un test automatizzato del client, né prova di confronto pixel, né prova di persistenza remota. Non confondere con i sei test Python.

### Stato persistente e lacune

**Nessuna condivisione automatica persistente Android ↔ renderer dimostrata.** Il renderer legge il JSON dal filesystem; il pannello chat usa stato locale. Il codice recuperato non implementa sincronizzazione UI→JSON→GitHub, non effettua commit automatici, non avvia Python da Android. Lo snapshot locale non dimostra salvataggio fra chat. Il checkpoint GitHub conserva il colore iniziale `#356B84`, non l'ultimo colore selezionato sul dispositivo.

Restano non dimostrati: round-trip completo UI→serializzazione→renderer→nuova sessione; parità pixel preview Android/raster Pillow; identità cross-engine; salvataggio e rilettura di preset persistente; ripetizione indipendente dei sei test; reale isolamento del contesto cold-start. Nessuna di queste lacune autorizza a riaprire la produzione Tattoo.

### Incongruenze e rischi documentali

- `README.md` è centrato su FORMA-001 e non indirizza chiaramente al checkpoint Creative Console: rischio di discovery incompleta, senza dimostrare un errore di funzionamento.
- In questo audit una sezione precedente dice ancora «Android non verificato», mentre l'aggiornamento cronologicamente successivo registra conferma utente: chi legge deve privilegiare la data e il tipo di evidenza, senza scambiare conferma dichiarativa per prova automatica.
- Il test `test_repeatable` è una verifica in-process, non una prova di pixel identity fra client e Pillow.
- La dicitura «persistenza nel repository» è una scelta di progetto per il prototipo, non un'implementazione di sincronizzazione automatica.

### Verdetto e singola prossima azione

- **PASS circoscritto:** recupero delle fonti GitHub, ricostruzione esatta del contratto, individuazione dei sei test e distinzione delle evidenze.
- **NON DIMOSTRATO:** persistenza automatica end-to-end, parità Android/Pillow, cold-start tecnicamente isolato.
- **Verdetto complessivo continuità agentica: INCONCLUSIVE**, con evidenza positiva di continuità documentale. Non promuovere il sistema a PASS solo perché il checkpoint contiene documentazione.

**Una sola prossima azione proposta, non autorizzazione all'esecuzione:** progettare un test minimo di round-trip JSON fra pannello Android e renderer, con modifica singola, serializzazione esplicita, ripresa in nuova sessione, controllo revisione/hash e confronto dell'output. Richiedere autorizzazione separata prima di implementare o eseguire. Nessuna nuova produzione creativa, installazione o modifica non richiesta.

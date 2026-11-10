# GPT SOCIAL — Audit di chiusura: Android Creative Console e continuità agentica
Data: 2026-11-10 · Tipo: audit di run e handoff · Stato: fatti osservati, decisioni utente e proposte separate.

## 1. Mandato e perimetro
La sessione ha esaminato audit precedenti, mostrato test Android per anteprime raster e interfacce native interattive, e co-progettato una Creative Console sperimentale. Non è stato creato un post finale, né dimostrato un editor di asset completo. Documentazione tecnica precedente: `docs/protocollo-ui-android-test-2026-11-10.md`. Audit storici: `docs/audit-run-tattoo-underground-2026-11-10.md`, `docs/audit-layer-001-handoff.md`, `docs/report-run-ecovillaggio-istanbul-2026-11-09.md`, `benchmarks/FORMA-001/risultati.md`.

## 2. Risultati verificati
- L'utente ha confermato su Android visibilità e funzionamento della prima griglia, palette e controlli.
- Test 2: un raster composto di due pannelli con Pillow/ `display(comparison)` appare inline ma piccolo; errore metodologico: cambio di saturazione/contrasto invece della variabile palette concordata.
- Test 3: due palette, composizione identica, raster composto in un unico pannello; screenshot mostra anteprima non a piena larghezza.
- Test 4: due raster separati emessi con due `display(...)` consecutivi nella medesima chiamata `python_user_visible.exec`; screenshot Android mostra due anteprime distinte, grandi, affiancate, anche se era stata richiesta disposizione verticale. Non è garanzia di layout su ogni client.
- Test C: screenshot mostra controlli nativi funzionanti (switch V1/V2, checkbox testi A/B, posizione, reset) e preview reattiva. Il pannello è molto apprezzato per decisioni veloci.
- Creative Console estesa: è stata mostrata in chat una demo con tab Scena/Testi/Oggetti/Livelli, palette, preset codificati, tipografia, forme, slider, varianti A/B, undo/redo, lock, snapshot temporaneo, copia configurazione. L'utente ha fornito screenshot della scheda Scena, confermando che i controlli sono visibili. NON sono stati verificati sistematicamente tutti i controlli e la correttezza di ogni transizione di stato.
- Un protocollo tecnico Android è stato scritto nel branch di lavoro con commit `dbf855a8c9fb7773a65476143c6b98917a23a278`.

## 3. Feedback e decisioni utente
- **Approvata come modalità predefinita: GUIDATA.** Prima breve intervista conversazionale per tema, obiettivo, destinatari, materiale disponibile e vincoli; poi pannello inizialmente leggero, arricchito progressivamente.
- Pannello nativo in chat come centro decisionale; chat per brief, spiegazioni brevi, proposte e revisioni; immagini reali per valutare il risultato.
- Colori: preferire selezione VISIVA, non input esadecimale richiesto all'utente; codici interni solo quando utili.
- Preset: l'utente vuole poter approvare e salvare un'intera configurazione riutilizzabile (es. post per barca: impaginazione, colori, ecc.), richiamabile come chip/preset rapido.
- Richiesta di distinguere lucchetto (protezione modifiche), snapshot (checkpoint reversibile) e salvataggio permanente di un preset; il prototipo attuale salva snapshot solo nello stato locale della UI, non in storage duraturo.
- Continuare con pochi oggetti, codici A/B/C per testi e 1/2/3 per elementi singoli, modifiche circoscritte e reversibili, conservazione delle decisioni approvate.
- No download o placeholder come surrogati di anteprime inline Android; confronti coerenti (una variabile per volta) e screenshot/feedback utente come prova del rendering.
- Esplorare dopo il preset tre percorsi: foto reale preservata + overlay, grafica costruita a livelli, generazione assistita; valutare export verso Canva, senza promettere piena editabilità non testata.

## 4. Limiti e rischi emersi
1. Stato di un componente nativo nella risposta NON equivale a file grafico persistente, né a memoria condivisa fra messaggi/agent.
2. `DIL.useState` e snapshot della demo sono locali all'interfaccia; non garantiscono persistenza dopo riavvio, altre chat o altri agenti.
3. La demo usa SVG, layout e font semplificati: non garantisce tipografia finale, fedeltà pixel, gestione reale di livelli/occlusioni, né export Canva.
4. L'anteprima SVG non è un raster finale. Il passaggio da configurazione strutturata a rendering deterministico deve essere progettato e verificato.
5. I due `display()` separati sono apparsi affiancati in Android: la posizione dipende dal client e non va promessa.
6. I colori dei Test 1/3 non sono stati riprodotti per identità esadecimale: i futuri confronti devono usare valori canonici approvati e non solo etichette simili.
7. Una console con troppi controlli contemporaneamente rischia di riprodurre il problema dei micro-gate e del sovraccarico cognitivo.
8. Nel prototipo avanzato il selettore di formato non è implementato e il rapporto è fisso; il codice dimostrativo contiene impostazioni non ancora pienamente operative. Non promuovere una demo a prodotto senza test di comportamento.
9. L'integrazione Canva resta ipotesi: PNG appiattito; SVG/PPTX con editabilità variabile; API/integrazione richiede verifica di capacità e vincoli attuali.

## 5. Architettura proposta, NON ancora approvata come implementazione
**Chat di brief → Console guidata progressiva → Stato strutturato/versionato → Render reale → QA e approvazione → Libreria preset → Export o produzione.**

- La chat raccoglie un brief essenziale; l'agente produce 2–3 proposte visive, non decine di domande.
- Il pannello mostra solo i controlli necessari per la decisione corrente, ma resta lo stesso punto di lavoro.
- Ogni decisione approvata è una modifica esplicita dello stato del progetto, con versione, autore, data e dipendenze; undo/snapshot sono diversi dal preset riutilizzabile.
- Preset = struttura visiva, slot variabili (foto, titolo, CTA ecc.), asset/licenze, proporzioni, vincoli e versione; esempio nautico solo illustrativo, nessun preset nautico è stato effettivamente salvato.
- Se un asset fotografico è fornito dall'utente, preservare l'originale e applicare trasformazioni non generative salvo richiesta esplicita.
- Export potenziale: immagine finale PNG/JPG; template editabile SVG/PPTX; percorso Canva da verificare con benchmark dedicato.

## 6. Intervento minimo di product management per continuità multi-agente
L'utente chiede a un agente Product Manager indipendente di valutare la repository e proporre il **minimo sistema sostenibile** che impedisca perdita di idee, decisioni, prove, audit e progressi fra chat e agenti paralleli. Non è ancora approvata una ristrutturazione della repo.

Raccomandazione da valutare (non imporre):
- una fonte canonica per *stato corrente e prossima azione*, collegata a `AGENTS.md`;
- un registro decisioni con stato proposto/approvato/scartato, link a evidenza e ambito;
- audit di run append-only o collegati, con fatti verificati, feedback, limiti, costo e follow-up;
- backlog leggero prioritizzato con owner, criteri di accettazione e dipendenze;
- schema minimo di handoff per agenti paralleli, con delimitazione scope e regole di conflitto;
- indice di riferimenti canonici, evitando copie e file duplicati;
- regola di aggiornamento a fine sessione: evidenza → decisione → stato → un prossimo passo.

Il PM deve prima inventariare documenti esistenti, proporre **riuso e consolidamento** invece di proliferazione documentale, e distinguere modifiche minime immediate da infrastruttura prematura (database, agenti automatici, CI, skill).

## 7. Criteri di accettazione per prossima run di simulazione
- Avvio da chat nuova con modalità GUIDATA: massimo 3–5 domande sostanziali, raggruppate con naturalezza, senza modulo lungo.
- Presentare un pannello semplice dopo brief minimo: 2–3 direzioni visive con anteprima realmente visibile Android, palette visuali, poche scelte.
- Far evolvere lo stesso flusso verso composizione e testi, spiegando cosa cambia e cosa resta bloccato.
- Dimostrare almeno una scelta, una modifica localizzata, un undo e un confronto coerente.
- Distinguere configurazione temporanea, snapshot, preset convalidato e persistenza reale. Non affermare salvataggio in repo se non eseguito.
- Nessuna generazione finale, spesa, modifica repo o invio verso Canva senza autorizzazione.
- Al termine raccogliere feedback puntuale e produrre audit con successo/fallimenti, prove Android, un solo prossimo passo.

## 8. Handoff e prossime attività
**Agente PM parallelo:** audit della governance e proposta di intervento minimo per continuità multi-agente, senza eseguire ristrutturazioni non autorizzate.
**Agente nuova chat:** breve simulazione GUIDATA e test pannello progressivo con l'utente, senza confondere demo nativa con asset reale.
**Questa sessione:** chiusa; audit archiviato nel branch `proposal/layer-001-workflow-v02`. Non sono stati modificati AGENTS.md, decisioni.md, main o altri documenti.

# GPT SOCIAL — Protocollo UI Android verificato (test 1–4 e C)

Data: 2026-11-10. Stato: osservazioni dell'utente su ChatGPT Android, non garanzie universali di rendering.

## Evidenza osservata
- Test 1: griglia, palette e controlli nativi visibili e funzionanti secondo conferma utente.
- Test 2: Python/Pillow + `IPython.display.display(comparison)` con un unico raster contenente due pannelli. Visibile inline, ma piccolo, senza due asset autonomi; cambio non richiesto di saturazione/contrasto rispetto alle palette precedenti.
- Test 3: stessa geometria, due palette morbida/forte; `display(comparison)` di un unico raster affiancato. Android lo mostra in un riquadro relativamente stretto.
- Test 4: due immagini raster separate create con Pillow e inviate in due chiamate consecutive `display(draw_variant(palettes[0]))` e `display(draw_variant(palettes[1]))` **nella stessa esecuzione** di `python_user_visible.exec`. Screenshot Android dell'utente: **due immagini distinte, affiancate, grandi**, che sfruttano meglio la larghezza. Importante: il codice ha emesso due display consecutivi, non ha imposto un layout verticale; non promettere né colonna né riga. Questo comportamento può variare per client/versione.
- Test C: interfaccia nativa in chat con selettore V1/V2, checkbox A (titolo) e B (sottotitolo), selettore posizione alto/basso, pulsante reset; lo screenshot Android conferma il pannello grande, leggibile e manipolabile. È UI locale reattiva, **non** editing di un file fotografico finale.

## Ricetta riproducibile, per agenti
1. Per confronti raster deterministici usare Pillow in `python_user_visible.exec`, mantenendo la stessa geometria e modificando solo la variabile dichiarata (es. palette).
2. Per il confronto di due immagini indipendenti chiamare `display(image_a)` e `display(image_b)` separatamente nella stessa esecuzione. Verificare con screenshot o conferma utente il layout Android effettivo; non dichiarare garantito l'affiancamento.
3. Non usare `display(composite)` se sono richiesti due asset indipendenti: un collage è un solo raster e può risultare più piccolo.
4. Per scelte rapide usare componenti nativi di chat con stato condiviso: `DIL.useState` in `{@body ...}`, `segmented-control`, `checkbox`, `radio-group`, `button`, e un'anteprima aggiornata dai valori. Reset deve ripristinare davvero lo stato iniziale. Evitare controlli decorativi.
5. Distinguere sempre anteprima interattiva nativa da asset finale: modificare lo stato di un pannello non significa aver aggiornato un PNG o una foto. Il collegamento stato → rendering asset → verifica è ancora da progettare/testare.
6. Ogni nuova variante eredita decisioni già approvate; cambiare **una sola variabile** per confronto, salvo autorizzazione esplicita. Le palette devono essere identiche a quelle precedentemente scelte, non solo semanticamente simili. Se i valori originali non sono disponibili, dichiararlo.
7. Prima dell'uso operativo su Android verificare leggibilità, dimensioni, disposizione effettiva, interazione, reset e coerenza dei colori. Nessun download o placeholder come sostituto di un'anteprima richiesta inline.

## Workflow suggerito (non ancora approvato)
Anteprima reale → pannello nativo per scegliere variante, visibilità e posizione di elementi codificati (A/B/C per testo, 1/2/3 per oggetti) → applicazione deterministica solo delle modifiche scelte → nuova anteprima reale → approvazione. Accorpare decisioni correlate, evitare micro-gate e testo superfluo.

## Limiti e test aperti
- Il layout affiancato di due `display()` è **osservato** nello screenshot, non controllato dal codice Python.
- Non è verificata la visualizzazione nativa di due asset prodotti tramite `AsyncImage` indipendenti.
- Non sono verificati il binding persistente dei controlli a file raster, la modifica fotografica reversibile, il lock pixel/hash e la resa finale dei font.
- Test successivo consigliato: pannello Test C che governi varianti raster reali, preservando originali e decisioni approvate, con verifica Android e senza creare un post social definitivo.

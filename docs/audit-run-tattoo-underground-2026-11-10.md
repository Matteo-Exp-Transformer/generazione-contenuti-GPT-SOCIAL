# GPT SOCIAL — Audit esecutivo run Tattoo Underground (9–10 novembre 2026)

Stato: run incompleta, confronto fotografico finalmente visibile in chat; post finale non prodotto. Questo è un report della sessione, non un audit indipendente. Branch: `proposal/layer-001-workflow-v02`.

## Brief e decisioni
- Foto originale fornita dall'utente: braccio con tatuaggio lettering underground appena realizzato.
- Post per tatuatore e community interessata a tatuaggi underground.
- Direzioni proposte: V1 Raw Underground, V2 Dark Editorial, V3 Punk Zine; selezionata V1.
- Utente sceglie di partire dalla fotografia. Autorizza due varianti per confronto.
- Nuova regola esplicita dell'utente: **ogni foto fornita va rispettata e valorizzata senza rifarla né alterarne soggetti, lettere e dettagli, salvo richiesta contraria**.
- Sotto ogni confronto spiegare in poche parole effetto/filtro applicato e cosa osservare.
- **Solo anteprime reali in chat Android**; mai link di download, file intermedi, segnaposto o immagini generiche presentate come risultato. Preferita griglia due colonne, scorrimento verticale; non carosello.

## Cronologia dei tentativi
1. Intervista e tre direzioni: funzionanti, ma la conversazione accumula passaggi di scelta.
2. Dopo l'autorizzazione, due chiamate a `image_gen.text2im`: **errore grave**. Hanno ricreato sinteticamente il tatuaggio anziché applicare filtri alla foto. Possibili alterazioni di caratteri e geometrie; non usare queste generazioni come rappresentazioni fedeli.
3. Tentativo `grid` + `AsyncImage`: fallito perché i componenti erano collegati a query/fallback generici, non agli asset effettivi. Sono apparse immagini non corrispondenti/duplicate; non è un test valido degli asset prodotti.
4. L'agente dichiara il problema ma offre link sandbox/download: contrario al vincolo dell'utente. Anche il successivo tentativo con placeholder «Anteprima non disponibile» fallisce. La chat non deve scaricare il problema sull'utente.
5. Due varianti con filtri fotografici non generativi ricavate dalla foto originale: V1A Raw Natural (contrasto moderato, saturazione ridotta, luminosità leggermente ridotta); V1B Dark Desaturated (contrasto più forte, forte desaturazione). Le percentuali dichiarate in chat non sono qui confermate da codice di elaborazione riproducibile.
6. Ultimo tentativo: `python_user_visible.exec` con Pillow e `IPython.display.display`: caricamento dei due JPEG filtrati, ridimensionamento proporzionale a 420 px ciascuno, composizione in un'unica immagine con separatore di 12 px, rendering inline in chat. **Visualizzazione riuscita nel risultato dello strumento**, senza download; la scelta definitiva dell'utente non è ancora avvenuta.
7. Una successiva risposta ha usato `grid` per le sole descrizioni testuali; la fotografia affiancata era stata mostrata dal risultato Python, **non da due `AsyncImage` distinti**.

## Distinzione tecnica indispensabile
- `image_gen.text2im`: generazione/reinterpretazione, NON filtro fedele.
- Pillow: elaborazione raster deterministica della foto fornita; non prova da sola un asset lock certificato.
- `python_user_visible.exec` + `IPython.display`: può mostrare una composizione fotografica inline, in questa run ha funzionato.
- `grid` + `AsyncImage`: il micro-test precedente aveva funzionato con **immagini di riferimento**; in questa run non è stato dimostrato il collegamento ad asset reali generati o filtrati.
- La composizione Python era **una singola immagine con due pannelli**, non una griglia nativa di due immagini indipendenti.
- File fotografici non caricati in repo; nessun hash verificato, nessuna prova di fedeltà pixel, nessun export finale.

## Matrice di audit
| Criterio | Stato | Evidenza |
|---|---|---|
| Tre direzioni e scelta V1 | Superato | Scelta utente |
| Conservazione della foto in prima esecuzione | Fallito | Due reinterpretazioni AI |
| Correzione con filtri sulla foto | Parziale | Due JPEG elaborati; parametri non riprodotti qui |
| Anteprime reali con AsyncImage | Fallito | Query/fallback non collegati |
| Anteprima inline con Python | Superato per visualizzazione | Immagine composta mostrata in chat |
| No download/placeholder | Fallito inizialmente | Link e fallback offerti |
| Descrizione effetti | Parziale | Descrizioni aggiunte dopo feedback |
| Asset lock e livelli separati | Non verificato | Mancano prove |
| Post utilizzabile e QA finale | Non eseguito | Run interrotta |
| Costi e tempi | Non verificato | Nessuna misura affidabile |

## Costi, carico umano, feedback
- **2 generazioni AI evitabili**.
- **2 varianti fotografiche filtrate**.
- Ripetute correzioni dell'utente su fedeltà fotografica, visualizzazione, download e leggibilità della comparazione.
- Nessuna misura affidabile di token, euro, minuti umani o tempo macchina.
- Carico umano qualitativamente eccessivo per un semplice confronto di due filtri.

## Regole da proporre per il prossimo protocollo (non tutte approvate come modifiche canoniche)
1. Foto dell'utente = asset originale da preservare per default. Separare chiaramente **filtro/crop**, **overlay grafico**, **editing generativo**.
2. Prima di ogni presentazione, verificare che l'anteprima corrisponda all'asset reale e sia visibile **inline**; vietare download, placeholder e immagini di ricerca sostitutive.
3. Per ogni variante, fornire una micro-legenda: effetto applicato e dettaglio da osservare.
4. Verificare comparativamente `grid + AsyncImage` su asset effettivi, composizione Pillow + `IPython.display`, e altre opzioni native disponibili nella sessione. Non presumere che ogni strumento sia disponibile o che possa collegarsi agli asset locali.
5. Non generare contenuti per dimostrare un'interfaccia: testare sequenze e strumenti con campioni neutri e consenso quando necessario.

## Stato e handoff
Scelta tra V1A e V1B ancora aperta. Nessuna tipografia, layout finale o QA. Prossimo agente: analisi trasversale della repo e delle run, **co-design delle sequenze di ideazione e degli strumenti di visualizzazione/interazione in chat**; niente produzione di post, niente subagenti, niente modifiche senza consenso. Separare verificato, non verificato e proposta.

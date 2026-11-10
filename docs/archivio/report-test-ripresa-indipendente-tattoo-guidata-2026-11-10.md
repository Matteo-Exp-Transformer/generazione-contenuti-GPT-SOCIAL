# GPT-SOCIAL — Report test di ripresa indipendente: Tattoo GUIDATA

Data: 2026-11-10  
Tipo: verifica documentale indipendente, senza esecuzione creativa  
Repository: `Matteo-Exp-Transformer/generazione-contenuti-GPT-SOCIAL`  
Branch del caso: `proposal/layer-001-workflow-v02`  
Snapshot analizzato: `b85b7c1df5dfff6d5f2fee1fcde3cf1cd1f59e2b`

## Mandato e perimetro

Riprendere autonomamente il caso Tattoo GUIDATA, individuare la prossima azione consentita e stabilire se la documentazione permetta di dichiarare verificata l'identità della foto dopo un cambio di titolo. Nessuna modifica ai documenti del caso, nessuna generazione di immagini e nessuna nuova prova creativa. Il presente report è l'unico artefatto aggiunto, su ramo separato.

## Fonti effettivamente recuperate allo SHA indicato

- [AGENTS.md](../AGENTS.md)
- [docs/audit-run-tattoo-console-guidata-2026-11-10.md](../docs/audit-run-tattoo-console-guidata-2026-11-10.md)
- [docs/audit-creative-console-android-handoff-2026-11-10.md](../docs/audit-creative-console-android-handoff-2026-11-10.md)
- [docs/protocollo-ui-android-test-2026-11-10.md](../docs/protocollo-ui-android-test-2026-11-10.md)
- [docs/decisioni.md](../docs/decisioni.md)

Le conclusioni riguardano esclusivamente lo snapshot indicato, non eventuali modifiche successive su altri rami.

## Risposta 1 — Prossima azione consentita

**Revisione indipendente del workflow console-first prima di una nuova run.**

La sezione **Handoff** dell'audit Tattoo GUIDATA prescrive di verificare la diagnosi contro i documenti esistenti, distinguere norma già presente da enforcement proposto, definire il contratto stato → preview → render e preparare il micro-test Android; la sua formula **«Prossimo passo unico»** è la revisione indipendente della console-first workflow prima di una nuova run.

Questa azione è di analisi/proposta. Non autorizza da sola una nuova generazione, una produzione finale, installazioni, spese o cambiamenti alle fonti canoniche. L'audit qualifica il workflow candidato come **non ancora convalidato**. AGENTS.md vieta di dichiarare test non eseguiti come completati.

**Fonte primaria:** `docs/audit-run-tattoo-console-guidata-2026-11-10.md`, sezioni «Handoff», «Stato delle decisioni» e «Test di accettazione per agente successivo».

## Risposta 2 — Identità della fotografia dopo cambio di titolo

**Non verificata. Non è lecito dichiararla verificata.**

La sequenza documentata indica che:
1. Il collage generativo non offriva livelli/parametri ricostruibili con identità pixel e non garantiva fedeltà della fotografia originale.
2. La successiva versione deterministica con Pillow impiegava la foto originale, ma alterava simultaneamente cornice, decorazioni e titolo: non costituisce prova di modifica localizzata che preservi l'intera composizione approvata.
3. La verifica della fedeltà prima/dopo il cambio del titolo è elencata come **test di accettazione futuro**, non come esito passato.
4. Il protocollo Android dichiara ancora aperti lock pixel/hash, binding dei controlli a file raster e modifica fotografica reversibile.

Occorre distinguere **uso dichiarato della foto originale nel raster Pillow** da **identità pixel verificata dell'asset e invarianza degli altri elementi dopo la modifica**. Il primo è un fatto riportato nell'audit; il secondo non è dimostrato.

**Fonti:** `docs/audit-run-tattoo-console-guidata-2026-11-10.md`, sezioni «Sequenza osservata», «Test di accettazione»; `docs/protocollo-ui-android-test-2026-11-10.md`, sezione «Limiti e test aperti».

## Esito del test di ripresa

| Criterio | Esito |
| --- | --- |
| Recupero autonomo dei documenti allo SHA richiesto | Riuscito |
| Individuazione di una sola prossima azione | Riuscito |
| Distinzione fra osservazione, proposta e test futuro | Riuscito |
| Prova di identità fotografica dopo cambio titolo | Non disponibile / non verificata |
| Nuove prove creative | Non eseguite |
| Modifiche alle fonti canoniche | Nessuna |

**Conclusione limitata:** lo snapshot è sufficiente per riprendere documentalmente il caso e impedire la promozione di una prova non eseguita a risultato verificato. Questo test **non** valida il comportamento operativo della Creative Console, né la fedeltà pixel del rendering.

## Prossimo passo unico

Effettuare la **revisione indipendente console-first** già richiesta dall'audit, mantenendo separati fatti verificati, proposte architetturali e test ancora da autorizzare. Non avviare nuove prove creative sulla base del solo presente report.

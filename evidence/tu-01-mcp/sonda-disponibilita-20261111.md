# TU-01 MCP — F1-B, sonda disponibilità (2026-11-11)

**Stato:** BLOCKED — connettori non installati in questa sessione ChatGPT. Non equivale a FAIL funzionale di Canva o Figma. Nessuna prova TU-01 avviata, nessun tentativo di import, editing o export.
**Ambiente:** ChatGPT, sessione con strumenti GitHub e Plugin Management; destinazione prevista per l'anteprima: ChatGPT Android. Mandato: MANDATO-001 §§3,4,7. Scadenza 2026-11-13.
**Base:** main della repo al momento di creazione del branch dedicato `f1-b/sonda-mcp-disponibilita-20261111`.
**Perimetro:** nessuna automazione browser, nessun account di prova aperto, nessuna installazione/spesa, nessuna foto ricevuta/inviata, nessun PNG generato, nessuna pubblicazione.

## Evidenza operativa e distinzione capacità

Ricerca tramite il gestore plugin ChatGPT, query `Canva Figma`, 2026-11-11:
- **Canva**: plugin ID `plugin_connector_68df33b1a2d081918778431a9cfca8ba`, `status=ENABLED`, `installation_policy=AVAILABLE`, `installed=false`. Descrizione di catalogo dichiara upload di file, editing di testo/media/formattazione e ridimensionamento; **non verifica l'export PNG via MCP in questo ambiente**. Autenticazione non verificabile senza installazione/connessione. Nessuna operazione Canva esposta e invocata da questa sessione.
- **Figma**: plugin ID `plugin_connector_68df038e0ba48191908c8434991bbac2`, `status=ENABLED`, `installation_policy=AVAILABLE`, `installed=false`. Descrizione di catalogo dichiara creazione/revisione design con layer modificabili; import e PNG via MCP **non verificati**. Autenticazione non verificabile senza installazione/connessione. Nessuna operazione Figma esposta e invocata da questa sessione.
- L'indicazione del mandato secondo cui i connettori sono presenti nell'ambiente Claude Code **non dimostra disponibilità nella sessione ChatGPT**. Non si è fatto ricorso al browser.
- L'utente ha vietato installazioni senza approvazione; non è stata richiesta alcuna attivazione.

## Scheda TU-01 — Canva

| # | Misura | Esito / prova |
|---|---|---|
| 1 | Preservazione foto | NON TESTATA; nessuna foto importata, nessun confronto pixel o visivo |
| 2 | Undo esatto A→B→A | NON TESTATO; nessun export né hash di pixel decodificati |
| 3 | Anteprime Android senza download | NON TESTATA; nessuna conferma utente |
| 4 | Qualità estetica 1–5 | NON VERIFICATA; nessun voto utente |
| 5 | Minuti attivi utente / turni | NON VERIFICATI per TU-01; non inferiti dalla chat |
| 6 | Costo extra effettivo | €0 sostenuti in questa sonda; condizioni economiche d'uso non verificate |
| 7 | Ripresa reale nuova sessione | NON TESTATA; nessun progetto o link creato |

**Operazioni realmente eseguite:** sola discovery nel catalogo plugin (non è un'operazione MCP Canva). **Motivo blocco:** plugin non installato/collegato, mancano strumenti invocabili. **Progetto e ripresa:** nessun link, nessuna modalità dimostrata.

## Scheda TU-01 — Figma

| # | Misura | Esito / prova |
|---|---|---|
| 1 | Preservazione foto | NON TESTATA; nessuna foto importata, nessun confronto pixel o visivo |
| 2 | Undo esatto A→B→A | NON TESTATO; nessun export né hash di pixel decodificati |
| 3 | Anteprime Android senza download | NON TESTATA; nessuna conferma utente |
| 4 | Qualità estetica 1–5 | NON VERIFICATA; nessun voto utente |
| 5 | Minuti attivi utente / turni | NON VERIFICATI per TU-01; non inferiti dalla chat |
| 6 | Costo extra effettivo | €0 sostenuti in questa sonda; condizioni economiche d'uso non verificate |
| 7 | Ripresa reale nuova sessione | NON TESTATA; nessun progetto o link creato |

**Operazioni realmente eseguite:** sola discovery nel catalogo plugin (non è un'operazione MCP Figma). **Motivo blocco:** plugin non installato/collegato, mancano strumenti invocabili. **Progetto e ripresa:** nessun link, nessuna modalità dimostrata.

## Sonda e Gate D

- Import foto, testo modificabile ed export PNG: **0/3 operazioni eseguite su entrambi**; i limiti 15/30 minuti non sono stati consumati da prove tecniche, perché i connettori non risultano accessibili.
- Input 1080×1350, foto, titoli A/B, palette: non concordati, per evitare di chiedere la foto prima della conferma di un canale MCP.
- **Verdetto F1-B:** BLOCKED per ambiente; nessun PASS e nessun FAIL funzionale per i due strumenti.
- **Gate D:** non trarre confronto con la Strada A in assenza di misure TU-01 della Strada A.
- **Passaggio testimone:** se l'utente autorizza esplicitamente il collegamento di un plugin o attiva i connettori già presenti su Claude Code, verificare operazioni effettive e richiedere la foto con descrizione esplicita del trasferimento prima di qualsiasi upload. In alternativa chiudere F1-B come indisponibile entro il 13/11; nessuna proroga automatica.

Nessun materiale fotografico, export o credenziale conservato nella repository.

# GPT SOCIAL — Report run ecovillaggio Istanbul — 2026-11-09

Stato: **chiusa senza post finale; QA incompleto; audit indipendente richiesto**. Questo documento registra l'esecuzione, non certifica i risultati. Branch: `proposal/layer-001-workflow-v02`.

## Brief nuovo
Post per un ecovillaggio rurale nell'area di Istanbul: vita locale, comunità, accoglienza e inclusione sociale. Scelta V1: pasto condiviso all'aperto con natura ben visibile; successiva revisione: persone locali servono altre persone locali, musicisti sullo sfondo. Nessuna identificazione di un ecovillaggio reale: immagine sintetica, non fotografia documentaria.

## Cronologia e riscontri
1. Gate 1: domanda aperta, tre direzioni V1 comunità, V2 vita condivisa, V3 inclusione; selezionata V1 con natura dominante. Riferimenti visivi di ricerca mostrati, non tre post generati.
2. Gate 2: prima della generazione, utente aggiunge musicisti sullo sfondo e pasto servito da abitanti locali. L'agente descrive la scena senza anteprima visiva; utente segnala il difetto e consente di procedere. Autorizzata e prodotta **una** fotografia generativa 4:5, con tavola, persone, cibo, musicisti, alberi, colline e casa. Utente accetta la **bozza**, non una validazione finale.
3. Gate 3: utente critica legenda troppo aggregata e immagine sovraccarica. L'agente dichiara due layout su fotografia comune, ma presenta link a file e segnaposto invece di due immagini reali visibili. Secondo tentativo con immagini markdown sandbox: utente conferma **'No'** alla domanda se entrambe fossero visibili su Android. Gate sospeso.
4. Chiusura richiesta dall'utente con report e prompt per audit; nessun export finale validato.

## Difetti segnalati dall'utente
- **D01, anteprime mancanti nella revisione della scena:** la descrizione verbale non sostituisce la proposta visibile. L'utente ha accettato eccezionalmente di proseguire.
- **D02, legenda non granulare:** numeri raggruppavano oggetti; l'utente deve poter riferirsi a pane, singole pietanze, strumenti, persone e altri oggetti. Convenzione: lettere A/B/C per livelli testuali, numeri 1/2/3 per singoli elementi visivi rilevanti, codici stabili.
- **D03, immagine troppo carica:** troppe persone, oggetti e dettagli generati in una volta. Richiesta esplicita: partire da **pochi elementi** e arricchire gradualmente solo quando serve.
- **D04, rendering fallito su Android:** anteprime offerte come download, poi tramite riferimenti sandbox non visibili. Utente non vuole gestire file; servono due immagini reali grandi **direttamente in chat**, non link, placeholder o rigenerazioni inutili.

## Matrice di verifica
| Criterio | Stato | Evidenza/limite |
|---|---|---|
| Brief nuovo e intervista aperta | Superato | Domanda iniziale e risposta utente |
| Tre direzioni iniziali | Superato | V1/V2/V3 descritte con riferimenti |
| Mix tra direzioni | Non verificato | Utente ha raffinato V1, non eseguito mix V1+V2/V3 |
| Autorizzazione generazione | Superato | 'Sì' prima della fotografia |
| Fotografia approvata come bozza | Superato | Feedback esplicito |
| Anteprima ad ogni revisione | Fallito | D01 |
| Composizione minimale | Fallito | D03 |
| Legenda per singoli oggetti | Parziale | D02; legenda ampliata dopo feedback, non validata |
| Due anteprime leggibili su Android | Fallito | D04 e conferma 'No' |
| Identità pixel dei due layout | Non verificato | Dichiarato hash SHA-256 `638068508c4de703d07c3cc92ba409eea08401f9c2fb7d23f00b8679faeb4bd8` nella chat, ma senza verifica riproducibile di input/overlay |
| Modifica localizzata di un testo | Non eseguito | Gate 3 sospeso |
| QA finale e post esportabile | Non eseguito | Nessun layout scelto |
| Tempi, costi, credito e carico umano | Non verificato | Nessuna misurazione affidabile |

## Valutazione dell'esecutore
La convergenza creativa tramite dialogo è stata comprensibile e l'utente ha accettato la scena. Il flusso ha però imposto correzioni ripetute su anteprime, granularità della legenda e densità visiva. La presentazione in chat è il blocco operativo principale: non va confusa la produzione di un PNG con la sua effettiva visibilità sul dispositivo. Non è dimostrato l'asset lock con due layout pixel-identici; non dichiarare superato.

## Correzioni candidate (non ancora approvate)
1. Prima di ogni nuova run, **test di rendering in chat su Android** con due vere anteprime; fermarsi se non visibili.
2. Costruzione per sottrazione: **scena iniziale essenziale**, aggiunte progressive e consenso per nuovi elementi rilevanti.
3. Legenda operativa puntuale, stabile e separata dall'export; asset fotografico archiviato e hash verificabile, overlay non distruttivi e prova di modifica localizzata.

## Provenienza e limiti
Le immagini sono state create/presentate nella conversazione, ma **non sono state caricate in repository**; disponibilità per audit da verificare. Nomi citati nella chat: `a_warm_outdoor_countryside_feast_scene_a_long_woo.png`, `gpt_social_layout_V1.png`, `gpt_social_layout_V2.png`. Non assumere che questi file siano accessibili, né che i due layout siano stati effettivamente visualizzati. Nessun tempo/costo inventato. Nessun benchmark storico modificato.

## Handoff per auditor
Leggere `AGENTS.md`, `docs/test-cono-creativo-v01.md`, `docs/decisioni.md`, questo report e le run storiche FORMA-001 / LAYER-002-R2, distinguendo documenti canonici, feedback e prove. Verificare le differenze fra errore di protocollo, errore esecutivo e limite dello strumento. Non riutilizzare i risultati storici come prova di questa run. Richiedere gli asset se non accessibili. Concludere con matrice superato/parziale/fallito/non verificato, tre problemi prioritari, massimo tre correzioni minime, mantenere/correggere/scartare e un solo prossimo passo. Nessuna modifica senza consenso.

**Prossimo passo unico:** audit indipendente incrociato delle run e del protocollo.

# MANDATO-001 — Direzione creativa controllata e consegna verificabile

Aggiornato 2026-11-11 su richiesta esplicita dell'utente; continuità con la revisione Claude.
Questo testo sostituisce le istruzioni operative del [mandato originario](archivio/mandato-001-originale-20261110.md), conservato integralmente come storico.
Stato corrente e unico prossimo passo: [STATO.md](../STATO.md). Decisioni: [decisioni.md](decisioni.md).

## 0. Obiettivo e direzione attuale
Consentire all'utente di dirigere un post sulla propria fotografia, vedere il risultato reale,
modificare una parte senza perdere le scelte approvate e ottenere un file pubblicabile.
Direzione di sviluppo: regista conversazionale + layout Canva controllabili, da validare.
La scelta definitiva della strada e il Gate D restano aperti: questo aggiornamento non è un PASS.
Scelte prima della produzione; niente rigenerazione della foto, mockup spacciati per anteprime o fallback silenziosi.
L'anteprima inline Android resta l'obiettivo; l'utente accetta una consultazione Canva esterna occasionale e dichiarata (decisioni 2026-11-11), senza ponte Python. Rifinitura fuori Canva e fallback silenziosi restano esclusi.

## 1. Lavoro svolto e prove consolidate
| Lavoro | Esito / limite | Fonte |
|---|---|---|
| Consolidamento F0 | Archivi e fonti operative riordinati; rimangono 25 rimandi storici irrisolti | PR #15, indice archivio |
| Engine F1-A | 18 test sintetici verdi riferiti e verificati nella run precedente; nessuna modifica in questa riconciliazione | PR #16 |
| TU-01 reale Strada A | PARTIAL: tecnica riferita riuscita, esperienza creativa rifiutata, violazione procedurale con generazione immagine; non ripetere | PR #20 e #21, feedback utente |
| Discovery MCP iniziale | Tool assenti nelle sessioni iniziali; non un FAIL generale dei servizi | PR #17/#18, evidence/tu-01-mcp/ |
| Sonda fotografica Canva | Import foto/HTML e testi separati; inline Android negativo, link esterno positivo; B→A/export non eseguiti | [scheda](../evidence/tu-01-mcp/canva-2026-11-11.md), PR #19 |
| Sonda Figma | Modifica A→B→A senza foto; import foto bloccato DNS, nessun PASS fotografico | [scheda](../evidence/tu-01-mcp/sonda-2026-11-11.md), PR #19 |
| Correzione regista | Scelte approvate prima di Canva; nessun ImageGen; migliore esperienza riferita dall'utente | PR #22, §2 |
| Capacità Canva | Import 1080×1350, testi/media modificabili in draft; cambio titolo circoscritto nella miniatura 480×600; tutti i draft annullati | [audit §§1–8](../evidence/canva-capabilities/audit-2026-11-11.md), PR #23 |
| Ripresa e consegna | Baseline recuperata in nuova chat; due invii inline falliti su Android; ricevuto JPEG 1229×1536 invece del PNG richiesto | [audit §9](../evidence/canva-capabilities/audit-2026-11-11.md#9-audit-della-chat-successiva--esito-effettivo-del-checkpoint-2026-11-11), PR #23 |

Le PR #20/#21 documentano lo stesso esito Strada A: non sono due nuovi test.
#20 riferisce invarianti pixel e undo tecnici; #21 non li certifica autonomamente.
Conservare la distinzione: resoconto pregresso, non nuova verifica indipendente né PASS completo.
Le schede di discovery e la matrice iniziale dell'audit sono fotografie di quelle sessioni;
il §9 aggiorna ripresa/Android senza riscrivere retroattivamente le prove.
Nessuna misura mancante (tempo, costo, voto, turni) va ricostruita per stima.

## 2. Test conversazionale PR #22 — risultato preservato
La raccolta delle scelte e la loro approvazione sono riuscite; la consegna è fallita.
Formato 4:5 1080×1350; layout E «onde della musica»; palette B
#8FD3D1, #F7E7A8, #B998E8, #30475E; tipografia B elegante; testi A; effetti A onde incantate.
Testi: «Un mondo di suoni da scoprire»; «Un viaggio tra musica, gioco e meraviglia.»;
«Lezioni di handpan per bambini»; «Con Matteo · Bologna»; contatto approvato nel progetto.
Progetto esistente DAHalgBPGjk: tre testi modificabili e fill fotografico, pagina 1080×1350.
Sola ispezione; nessuna nuova composizione/decorazione salvata o PNG finale.
Schemi SVG/campioni colore non erano render Canva. Integrità fotografica pixel non certificata.
La disponibilità di un progetto non dimostra che le scelte approvate vi siano state applicate.

## 3. Cosa resta da dimostrare
Separare quattro livelli: conduzione creativa; operazioni del connettore; revisione salvata/export;
visualizzazione sul dispositivo. Un successo a un livello non certifica gli altri.
- Editing osservato senza font_family, insert_text, creazione generale di forme, crop esplicito e z-order.
- Decorazioni importate visibili ma non tutte indirizzabili separatamente.
- Export documentato dal servizio, assente nel catalogo delle sessioni esaminate; causa non diagnosticata.
- Commit e recupero di una modifica salvata, export originale e piena integrità foto ancora non verificati.
- Lock dichiarato dall'agente non è un vincolo tecnico: il titolo centrato può cambiare geometria;
  resize può ricomporre il layout e creare un nuovo progetto.
- Foto preservata = originale conservato e nessuna rigenerazione; crop/scala approvati sono distinti.
  Identità pixel fra revisioni equivalenti verifica cambiamenti collaterali, non identità byte dopo export.

## 4. Indicazioni dalla ricerca e conseguenze operative
Fonti consultate l'11/11/2026; indicazioni progettuali, non prova di capacità della nostra integrazione.
1. [OptiMuse, CHI 2024](https://www.microsoft.com/en-us/research/publication/understanding-nonlinear-collaboration-between-human-and-ai-agents-a-co-design-framework-for-creative-design/):
   studio formativo con 12 esperti e valutazione comparativa; esplorazione e remix non lineari.
   Applicazione: scelte prima del render, ma riapribili esplicitamente; evitare questionari rigidi e decisioni estetiche alla cieca.
2. [User-centered co-creativity, CHI EA 2024](https://www.research.ed.ac.uk/en/publications/a-user-centered-framework-for-human-ai-co-creativity/):
   framework su agency/controllo, non benchmark Canva. Applicazione: distinguere proposta AI da decisione utente.
3. [Canva best practices](https://www.canva.dev/docs/apps/mcp/best-practices/):
   stato strutturato, ID e transazioni; il prompt non garantisce il rendering di URL in ogni client.
   Applicazione: checkpoint con design_id, pagina, elementi, scelte, transazione e stato di salvataggio;
   verifiche dopo ogni modifica. Non costruire ora un nuovo orchestratore.
4. [Canva verifica end-to-end](https://www.canva.dev/docs/apps/mcp/verify-app/):
   verificare creazione/apertura/modifica/commit/export e corrispondenza al risultato salvato.
   Applicazione: nessun «fatto» sulla sola risposta di editing in draft.
5. [Canva autofill](https://www.canva.dev/docs/apps/mcp/tools/autofill-design/):
   template/campi per testi e immagini; piano e campi da verificare, nessun acquisto implicito.
   Applicazione: iniziare da pochi layout predisposti; autofill è un candidato non ancora provato.
6. [Anthropic, Building effective agents](https://www.anthropic.com/research/building-effective-agents):
   principio di semplicità e workflow prevedibili; tooling dell'articolo soggetto ad aggiornamenti.
   Applicazione: un agente regista e strumenti necessari; nessuna nuova architettura multi-agente.
7. [Canva export](https://www.canva.dev/docs/apps/mcp/tools/export-design/):
   export è una capacità documentata, non prova della sua esposizione nel client.
   Applicazione: verificare il catalogo effettivo, non inventare parametri o attribuire cause senza prove.

## 5. Sequenza corrente — una sola attività attiva
Aggiornata 2026-11-11 dopo la revisione architetturale approvata dall'utente (PR #29). Sostituisce la sequenza precedente
(diagnosi canale immagini, chiusa PARTIAL in PR #24/#25) e il §5.1 proposto in PR #25.
Principio: il Regista è un prodotto rilasciato e separato dal cantiere. Legge solo la skill versionata
(`regista-vX.Y`) e la scheda post; la sua fedeltà si misura con prove ripetute in chat nuove, valutate da un Supervisore.
1. **Ora:** il Supervisore verifica il pacchetto regista-v1.0 (SKILL, AVVIO, VALUTAZIONE) e guida la Preparazione.
2. Giro A e Giro B ([VALUTAZIONE §1–2](../skills/post-director/VALUTAZIONE.md)); esito pass^3 per controllo.
3. Azione già decisa in VALUTAZIONE §4 (v1.1 mirata, alternativa «foto fuori dalla chat», o escalation all'utente).
4. Se tutto passa: un post reale con la stessa procedura e misure di esperienza; il confronto manuale/assistito resta facoltativo.
5. **Gate D:** decisione esplicita dell'utente; soltanto dopo F2.
Un server proprio o un'app fuori da ChatGPT si valutano solo se VALUTAZIONE §4 lo prevede, con ok dell'utente sui costi.
TU-01 non si ripete. Il riferimento originario Gate D 13/11 e F2 17/11 resta pianificazione, non prova di completamento.

## 6. Regole di continuità
Prima di lavorare (Costruttore, Supervisore, Revisore): leggere AGENTS, STATO e questo mandato su main aggiornato. Il Regista legge solo la skill tramite AVVIO.md.
Non riprendere prompt di test o «prossimi passi» contenuti nelle evidenze storiche.
Aggiornare STATO, non creare ulteriori audit generali; usare l'audit Canva esistente per nuove evidenze pertinenti.
Prima delle scelte creative: verificare le capacità; prima della produzione: approvazione del riepilogo.
Riaprire solo le decisioni richieste, mantenere foto e altre scelte; distinguere direzione approvata da resa visiva approvata.
Nessuna spesa, installazione, foto in repo, pubblicazione o passaggio a renderer esterno implicito.
Engine e test invariati; nessuna riapertura dei due task delegati F0/F1-A già conclusi.
L'utente autorizza in questa run consolidamento e aggiornamento di main, non un PASS del prodotto.

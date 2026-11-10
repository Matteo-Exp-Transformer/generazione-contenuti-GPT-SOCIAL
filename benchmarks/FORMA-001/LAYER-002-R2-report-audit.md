# LAYER-002-R2 — Chiusura sessione e mandato di audit indipendente

Data: 2026-11-09. Stato: **sessione interrotta volontariamente al Gate 4, prima del QA finale**. Documento osservativo; **non** modifica il protocollo FORMA-001 canonico, la rubrica /100 o i risultati storici.

## 1. Risultato effettivo
- Concept evoluto: contrasto fra materiali/arredi creati dall'uomo e vegetazione naturale, collegamento visivo fra piante domestiche e giardino esterno.
- Direzione: fotografia protagonista; scena minimalista ma non vuota, con circa tre piante (Kentia, Monstera, Pothos), pochi arredi, vetrata e alberi all'esterno.
- **Una sola fotografia** generata e poi approvata come base immutabile. Originale della sessione: `/mnt/data/LAYER-002-R2_base_approved.png`; nome recuperabile solo nell'ambiente della conversazione, non automaticamente in GitHub.
- Gate 3: due anteprime di layout sulla medesima foto: A titolo sulla parete e B fascia esterna. Utente ha scelto **A**, senza ulteriori modifiche tipografiche. Anteprima A `/mnt/data/LAYER-002-R2_layout_A_preview.png`; B `/mnt/data/LAYER-002-R2_layout_B_preview.png`.
- Titolo visibile in A: «NATURA DENTRO CASA»; sottotitolo: «Design e verde in equilibrio». Sono testi dell'anteprima, non verificati contro eventuale testo letterale del brief canonico.
- **Nessun post finale approvato o verificato**: QA mobile, dimensioni/export 1080×1350 sRGB, fedeltà letterale al brief, asset modificabile, punteggio /100, test di revisione, tempo e costi non verificati. Non dichiarare benchmark superato.

## 2. Feedback utente — da preservare integralmente nel senso
> «sessione caotica, ho capito poco. Come verrà il post? L'ho dovuto combattere con te per farti fare quello che chiedevo».

Il feedback riguarda **l'interazione umano-chatbot**, non soltanto la qualità del prodotto. L'utente ha chiesto ripetutamente:
- Pochi gate comprensibili: per ciascuno *cosa decidiamo, cosa cambia, quando/come decide un professionista*.
- **Gate → intervista aperta** su oggetti, collocazioni e vincoli; il modello interpreta i dettagli non indicati. Anche istruzioni complete non autorizzano a saltare layer o affrettare la conclusione.
- Anteprime **grandi, direttamente visibili in chat**, che mostrino il risultato reale sulla **stessa fotografia approvata**; non link di download come sostituto, non fotografie nuove e non schemi spacciati per confronto finale.
- **Asset lock:** fotografia/template approvati restano identici; cambiano soltanto i layer autorizzati. Conservare base immutabile e versioni delle revisioni.
- «Minimal» significa meno affollamento, **non eliminare il tema delle piante**.
- Nessuna generazione, spesa, file o salto di gate senza autorizzazione appropriata.

## 3. Sequenza e attriti osservati
1. Workflow v0.2 approvato; run LAYER-002 avviata con opzioni fotografiche.
2. Utente ha richiesto intervista aperta dopo ciascun gate; aggiornamento sperimentale v0.3 e restart LAYER-002-R2.
3. Concept raffinato in più scambi: da natura che invade spazio a piante da interno e continuità esterna; assistente ha oscillato fra troppo carico e troppo vuoto.
4. Durante revisioni compositive sono stati mostrati **nuovi riferimenti fotografici**, cambiando lo sfondo anziché preservare la stessa scena; utente ha imposto asset lock.
5. Dopo autorizzazione esplicita è stata generata una foto, poi approvata. Solo a questo punto esiste una base fotografica effettiva da preservare.
6. Per il Gate 3 l'utente ha chiesto **confronto visivo applicato alla foto**. L'assistente ha inizialmente offerto descrizioni, poi link/immagini che non si visualizzavano sul dispositivo, poi addirittura nuovi riferimenti illustrativi. L'utente ha espresso forte frustrazione.
7. Solo tramite visualizzazione diretta di due immagini renderizzate nella chat è stato possibile scegliere A. L'utente ha approvato A e poi ha chiesto di fermare e documentare.
8. L'assistente aveva annunciato Gate 4 ma non ha eseguito QA. Il workflow non ha mostrato chiaramente **come sarebbe venuto il post finale**, né garantito una continuità visiva affidabile per l'utente.

## 4. Diagnosi preliminari, da verificare nell'audit
- Confusione fra **riferimento ispirazionale**, **anteprima effettiva**, **asset base approvato** e **deliverable finale**.
- UI di confronto inaffidabile su Android: l'utente non vedeva immagini incorporate tramite link sandbox, ma ha visto rendering diretti in chat. Va verificata una presentazione affidabile prima di costruire ulteriori gate.
- Eccesso di interviste ripetute e microapprovazioni; mancanza di un unico stato di progetto visibile e di un'anteprima coerente aggiornata.
- «Non modificare fotografia» deve significare blocco di pixel/asset, non semplice somiglianza semantica.
- La proposta di tre gate non ha ridotto automaticamente il carico cognitivo; contare anche attrito, chiarimenti e correzioni, non solo numero gate.
- Possibile scostamento del testo «NATURA DENTRO CASA» dal brief FORMA-001: da verificare, non presupporre.
- Impossibile dimostrare qualità finale, costo e riproducibilità senza QA e asset versionati.

## 5. Vincoli per il prossimo agente
**Prima fase: solo audit, nessuna immagine, modifica a repo, ambiente o asset.** Leggere AGENTS.md, README.md, docs/decisioni.md, docs/audit-layer-001-handoff.md, benchmarks/FORMA-001/{brief.md,protocollo.md,risultati.md,sessione-operativa.md}, questo report e asset effettivi se accessibili. Distinguere protocollo canonico e ramo sperimentale. Se le immagini non sono accessibili, chiederne allegato; non fingere di averle viste.

Valutare prioritariamente: chiarezza del percorso per l'umano, visibilità diretta delle anteprime, gestione intervista aperta, lock di sfondo/template, costi di interazione, controllo dell'avanzamento, QA e conservazione degli asset. Proporre **massimo tre correzioni strutturali** e una run di prova corta con criteri di successo misurabili. Non progettare un sistema nuovo né aggiungere agenti/skill/documenti per inerzia. Discutere con utente prima di cambiare procedura.

## 6. Prompt per agente revisore
Agisci come Independent Human–AI Interaction Auditor, Senior Creative Workflow Designer e Editorial Production QA Reviewer per GPT SOCIAL.

Repository: https://github.com/Matteo-Exp-Transformer/generazione-contenuti-GPT-SOCIAL
Branch sperimentale: proposal/layer-001-workflow-v02
Report da leggere per primo: benchmarks/FORMA-001/LAYER-002-R2-report-audit.md

**Missione:** analizza criticamente la sessione LAYER-002-R2 e spiega perché l'utente ha percepito caos, scarsa comprensione e necessità di combattere il chatbot per ottenere ciò che chiedeva. Non limitarti a una valutazione estetica. Ricostruisci sequenza e punti di attrito con evidenze da report, repo e immagini, distinguendo osservazioni da ipotesi.

Leggi anche AGENTS.md, README.md, docs/decisioni.md, docs/audit-layer-001-handoff.md e brief/protocollo/risultati/sessione-operativa FORMA-001. Mantieni il protocollo canonico intatto. Recupera le immagini originali e anteprime dalla conversazione o chiedi di allegarle se non disponibili: non usare nuove fotografie come sostituti.

Analizza in particolare:
1. Gate + intervista aperta: come mantenere controllo umano senza ripetizioni e microdecisioni.
2. Anteprime visive grandi direttamente in chat e **fedeli all'asset bloccato**; definisci un fallback concreto se la UI non le mostra.
3. Regola di conservazione di fotografia/template e revisione per layer, con verifica che sfondo e zone protette non cambino.
4. Stato comprensibile all'utente: cosa è approvato, cosa è provvisorio, come apparirà il post, cosa manca.
5. Perché si è arrivati a un layout approvato ma non a un deliverable finale validato; misura gli errori di processo e non inventare tempi/costi.

Output sintetico: diagnosi delle **tre cause principali**, massimo **tre correzioni pratiche**, proposta di un micro-workflow con esempio concreto di 1 gate + intervista + preview, criteri verificabili per la prossima run e **una sola decisione da chiedere all'utente**. Non generare immagini, non modificare repository né ambiente e non attivare subagenti senza autorizzazione. Prima presenta l'audit; poi concorda eventuali modifiche e test.

## 7. Handoff
Stato: LAYER-002-R2 fermo dopo approvazione anteprima layout A; QA Gate 4 **non eseguito**. Il prossimo passo non è produrre un post, ma **audit indipendente del workflow umano-chatbot**. I file PNG originali sono disponibili nella sessione locale, non garantiti nel repository. Protocollo FORMA-001 canonico invariato.

# FORMA-001 — Guida alla sessione sperimentale e revisione

**Stato:** preparazione operativa. Benchmark non eseguito.
**Fonti canoniche:** [brief](brief.md), [protocollo](protocollo.md), [prompt A](prompts/A-post-completo.md), [prompt B1](prompts/B1-fotografia.md), [prompt B2](prompts/B2-layout.md), [risultati](risultati.md).
**Regola:** questo documento contiene solo istruzioni di sessione, checklist e prompt di avvio/audit. Non duplica brief, rubriche o risultati.

## Prima della sessione
- Aprire una nuova chat con accesso a GitHub e, se necessario, generazione immagini.
- Verificare lettura di AGENTS.md, README.md, docs/decisioni.md e file FORMA-001.
- Confermare modello, strumenti, disponibilità effettiva, limiti, licenze e costo incrementale. Nessun acquisto, API a pagamento o installazione.
- Ottenere autorizzazione esplicita per le generazioni; l'approvazione del piano non autorizza immagini né crediti.
- Definire un timer per preparazione, generazione, composizione e revisione. Non inventare tempi retroattivi.

## Checklist di esecuzione — gate
### G0 — Prontezza
- [ ] Fonti canoniche lette; stato GitHub verificato.
- [ ] Specifiche del brief comprese; formato finale 1080×1350, sRGB.
- [ ] Percorsi A e B e criteri del protocollo confermati.
- [ ] Strumenti, costi e disponibilità verificati; costo esterno incrementale massimo €0.
- [ ] Autorizzazione esplicita a generare raccolta.

### G1 — Candidato A
- [ ] Un solo primo candidato A, dal prompt canonico.
- [ ] Asset salvato/riferimento recuperabile; modello e impostazioni annotati.
- [ ] Testi confrontati lettera per lettera con brief; difetti visivi descritti.
- [ ] Tempo e tentativi annotati; nessun punteggio inventato.

### G2 — Fotografia B1
- [ ] Una sola fotografia iniziale dal prompt canonico.
- [ ] Assenza di scritte, loghi e persone verificata.
- [ ] Materiali, luce, prospettiva e zone utili al crop verificati.
- [ ] Approvazione umana dell'asset prima di B2.

### G3 — Layout B2
- [ ] Piano tecnico approvato prima di creare file o modificare ambiente.
- [ ] Testi esatti in livelli modificabili.
- [ ] Fotografia dominante asimmetrica e dettaglio materico.
- [ ] Sorgente riproducibile, PNG 1080×1350 sRGB; font e licenze documentati.
- [ ] Nessuna dipendenza non autorizzata.

### G4 — QA comparativo
- [ ] Visualizzazione a dimensione smartphone e comprensione in 3 secondi.
- [ ] Testi, ritagli, allineamenti, contrasti e difetti controllati.
- [ ] Stessa modifica al sottotitolo richiesta ad A e B; tempo e difficoltà misurati.
- [ ] Punteggi attribuiti secondo protocollo, con motivazioni ed evidenze.
- [ ] Confronto tempo totale, costo, numero tentativi, modificabilità e qualità.
- [ ] Verifica soglia 80/100 e assenza errori critici.

### G5 — Chiusura
- [ ] Aggiornare risultati.md solo con prove effettive, dopo autorizzazione alla scrittura.
- [ ] Separare osservazioni, valutazioni soggettive e ipotesi.
- [ ] Nessun cambiamento di PRD, prompt o processo senza decisione motivata.
- [ ] Lasciare un solo prossimo passo e un handoff breve se necessario.

**Limiti:** massimo 3 tentativi iniziali per percorso e 1 revisione per candidato; iniziare con 1 A + 1 B1, non consumare il plafond automaticamente. Se la capacità del tool non consente esportazione, sorgente modificabile o precisione richiesta, dichiarare il limite e chiedere come procedere.

## Prompt 1 — Avvio nuova chat sperimentale

Sei il responsabile di una sessione sperimentale FORMA-001 per GPT SOCIAL. Repository: https://github.com/Matteo-Exp-Transformer/generazione-contenuti-GPT-SOCIAL

Leggi AGENTS.md, README.md, docs/decisioni.md e tutti i file pertinenti di benchmarks/FORMA-001, inclusa questa guida. Non ricostruire il progetto da zero e non introdurre skill o infrastruttura.

Obiettivo: confrontare A (post intero generato) e B (fotografia generata + layout separato modificabile), con la stessa rubrica del protocollo. Procedi gate per gate G0–G5 e mostra a ogni gate: cosa è stato fatto, prova disponibile, difetti, prossima decisione umana. Parti da un solo candidato A e una sola fotografia B1; attendi approvazione della fotografia prima di B2.

Prima di generare, chiedimi autorizzazione esplicita, dopo aver verificato capacità e costi reali. Budget esterno incrementale €0; non acquistare crediti, non installare e non modificare l'ambiente senza consenso. Prima di scrivere sulla repo chiedi consenso specifico. Non dichiarare test eseguiti se non verificati. Annota tempi, tentativi, impostazioni e asset recuperabili; se non puoi misurarli, dichiaralo.

Concludi con il confronto verificabile e la proposta di aggiornamento a risultati.md. Quando il contesto si appesantisce, prepara un prompt di handoff con stato GitHub, asset, gate raggiunto, decisioni, problemi e prossimo passo. Non affermare di avere un contatore affidabile dei 100k token.

## Prompt 2 — Audit post-run in nuova chat

Agisci come revisore indipendente, senior editorial art director e workflow reliability auditor. Non produrre nuove immagini e non modificare nulla durante la prima fase.

Repository: https://github.com/Matteo-Exp-Transformer/generazione-contenuti-GPT-SOCIAL

Leggi AGENTS.md, il brief e protocollo FORMA-001, questa guida e risultati.md. Esamina i file e gli asset realmente prodotti dalla run; chiedimi link o caricamenti se mancano. Non attribuire punteggi sulla base di sole descrizioni o di un resoconto non verificabile.

Valuta distintamente:
1. Qualità editoriale, fotografia, composizione, tipografia, leggibilità mobile e fedeltà al brief.
2. Precisione dei testi e presenza di errori critici.
3. Tempo totale e costo reale per ottenere un post approvabile, non solo velocità di generazione.
4. Modificabilità e risultato della stessa revisione del sottotitolo su A e B.
5. Affidabilità del workflow: gate, tracciabilità, ripetibilità, punti di attrito, lavoro manuale.
6. Scelta A, B, ibrido o nessuno, con motivazioni ed evidenze.

Applica la rubrica /100 del protocollo solo ai risultati osservabili. Distingui difetti del modello, del prompt, dell'asset e del layout. Proponi massimo tre correzioni ad alto impatto e basso costo, senza proliferare skill, agenti o documenti. Discuti con me il risultato e proponi un solo benchmark successivo o una revisione mirata. Non cambiare repository senza autorizzazione.

## Handoff per limite di contesto
Non è disponibile una misura affidabile dei token consumati. Se la chat si avvicina a un limite pratico, consegnare: commit e file verificati; gate raggiunto; modelli e impostazioni; riferimenti agli asset; tentativi e tempi; costi; decisioni umane; QA svolto e mancante; problemi; prossima azione singola. Non duplicare tutto il brief.


## Prompt 3 — Prosecuzione orientata alla fattibilità (2026-11-09)

Mandato per una **nuova chat esecutrice**, non autorizzazione automatica a generare o modificare ambiente/repository:

> Agisci come Senior Editorial Production Engineer per GPT SOCIAL. Leggi AGENTS.md, README.md, docs/decisioni.md e tutti i documenti di benchmarks/FORMA-001 nella repository https://github.com/Matteo-Exp-Transformer/generazione-contenuti-GPT-SOCIAL. Parti dallo stato verificato in risultati.md: 2 candidati A, 1 fotografia B1, nessun layout B2, nessun tempo storico misurato, costi per immagine ChatGPT non disponibili. Recupera gli asset originali dalla chat precedente o chiedi di allegarli; non assumere che i riferimenti temporanei siano persistenti.
>
> **Priorità:** misurare se si riesce a produrre un post davvero utilizzabile, con quanti tentativi, minuti umani, attesa macchina, crediti/quote e spesa monetaria. Non perfezionare inutilmente la direzione artistica. Non inventare costi, tempi o capacità. Separare costo incrementale, quote incluse, costo del lavoro e costo imputato dell'abbonamento.
>
> Avvia una nuova run con ID e cronometro dichiarato prima di qualsiasi azione. Verifica gli strumenti disponibili e la disponibilità reale di quote, annotando ciò che non è esposto. Presenta un piano minimo per utilizzare B1 come asset e produrre B2 editabile (sorgente HTML/CSS/SVG o equivalente già disponibile, PNG 1080×1350 sRGB, testi letteralmente esatti, nessuna dipendenza nuova). **B1 non è ancora approvata:** chiedi esplicitamente approvazione di B1 e del piano tecnico prima di creare B2. Non creare file, generare immagini, installare, spendere crediti o modificare repository prima di autorizzazione specifica. Budget esterno incrementale €0.
>
> Dopo autorizzazione, realizza un solo B2 minimo ma usabile; misura e verifica l'output, poi proponi una singola modifica del sottotitolo da replicare sul percorso A, con misurazione separata di tempo, tentativi, effetti collaterali e costo. Non avviare generazioni aggiuntive senza consenso. Valuta il primo output approvabile, non solo l'estetica; se fallisce, registra perché. Compila la scheda per ogni tentativo prevista in protocollo.md. Presenta prove e bozza di aggiornamento a risultati.md, chiedendo autorizzazione prima di scrivere. Un solo prossimo passo e handoff breve se serve.
>
> Non introdurre subagent o nuovi file di processo per inerzia. In caso di capacità di delega non disponibili, lavora direttamente e dichiaralo.

**Nota:** questo prompt non cambia brief, rubrica, gate o autorizzazioni. Il prossimo test preferito è T3 (B2) dopo approvazione B1; T1/T2 rimangono nel backlog.

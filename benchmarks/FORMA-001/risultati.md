# Risultati — FORMA-001

**Stato al 2026-11-09:** G0 letto, G1 eseguito con deviazione, G2 fotografia prodotta ma **non ancora approvata**, G3–G5 non eseguiti. Registro retrospettivo: le misure mancanti restano sconosciute.

## Sessione 001 — ChatGPT / OpenAI ImageGen

| ID | Percorso | Esito | Identificatore generazione | Asset locale originario (non garantito persistente) | Dimensioni dichiarate in chat |
|---|---|---|---|---|---|
| A1 | A completo | Copertina con testi non conformi | 5350862b-d593-47c7-99d9-b18d1a6119df | a_magazine_style_editorial_cover_poster_image_for.png | 1122×1402 (da verificare sul file) |
| A2 | A completo, deviazione | Seconda copertina non prevista | 5c91a2d7-e997-48ab-8669-a76165112a87 | a_clean_modern_magazine_cover_editorial_poster.png | 1092×1440 (da verificare sul file) |
| B1 | B fotografia | Foto senza testo visibile; approvazione in sospeso | 4062eca9-5fc4-4b3c-bbbf-ab747c9a4728 | a_realistic_high_detail_architectural_interior_ph.png | 1122×1402 (da verificare sul file) |

I nomi sono quelli comunicati dalla sessione e non costituiscono link permanenti. Per audit in nuove chat, recuperare e allegare i file originali; registrare checksum SHA-256 e dimensioni dopo verifica effettiva. Non sono stati caricati asset nella repository.

### Osservazioni (qualitative, non punteggi)
- A1/A2: testi obbligatori omessi o sostituiti; testi aggiuntivi; manca il riquadro separato di dettaglio materico. Non approvabili secondo il brief.
- B1: buona luce laterale e ombre geometriche; mancano molti elementi richiesti (legno, lino, ceramica, arredi living). La scena somiglia ad A1, riducendo l'indipendenza visiva del confronto.
- **Deviazione di protocollo:** erano autorizzati 1 A e 1 B1, con valutazione intermedia; sono stati invece generati 2 A. Una successiva autorizzazione ha permesso 1 B1. Non cancellare la deviazione dai costi.
- Nessun B2; nessun test di revisione, QA smartphone o punteggio /100; nessuna approvazione esplicita B1.

### Contabilità retrospettiva
| Metrica | Stato |
|---|---|
| Numero generazioni | 3 (2 A + 1 B1) |
| Strumento | OpenAI ImageGen in ChatGPT; modello backend/versione non attestati |
| Acquisti o API esterne avviati nella sessione | Nessuno osservato |
| Euro effettivamente fatturati per generazione | Non disponibili |
| Consumo di quota ChatGPT / costo opportunità | Non disponibile |
| Tempo di preparazione/generazione/revisione | Non misurato |
| Crediti Higgsfield consumati | 0: non sono state lanciate generazioni Higgsfield |
| Modifiche a repo prima di questo registro | Nessuna |

**Non interpretare “nessun acquisto” come costo economico per immagine = €0.** Costi di abbonamento, capacità inclusa, ammortamento, lavoro umano e prezzi di eventuali alternative vanno rendicontati separatamente. Nessun tempo o prezzo retroattivo inventato.

## Backlog test autorizzabili (non ancora eseguiti)
1. **T1 — Editing fotografico deterministico B1:** due parametri fissati prima del test (es. temperatura colore e contrasto), stesso file sorgente; misurare minuti, strumenti, output, reversibilità, alterazioni involontarie e costo incrementale. Nessuna generazione AI.
2. **T2 — Editing generativo B1:** aggiungere una poltrona in lino, conservando inquadratura, luce e geometrie; 1 tentativo iniziale solo dopo nuova autorizzazione; annotare modello/versione, prompt integrale, input/output, quote, tempi, difetti e modifiche non richieste.
3. **T3 — B2 layout separato:** soltanto dopo approvazione umana di B1 e del piano tecnico; sorgente editabile e PNG 1080×1350 sRGB, font/licenze; registrare lavoro manuale, tempi e difetti.
4. **T4 — Stessa revisione per A e B:** sostituire esattamente il sottotitolo con una stringa concordata *prima* della prova; cronometrare dalla richiesta al file valido, contare tentativi/generazioni, controllare che tutto il resto rimanga invariato.
5. **T5 — QA e confronto:** test smartphone/3 secondi, verifica letterale dei cinque testi, 100 punti secondo protocollo, soglia 80 e nessun errore critico; costo e tempo fino al primo output approvabile.

**Prossima decisione singola:** scegliere e autorizzare T1 oppure approvare B1 e il piano di T3; non generare né implementare automaticamente.

Per metodo di replica, metriche, scheda-run e definizioni di costo: [protocollo.md](protocollo.md). Per gate e prompt di nuova chat: [sessione-operativa.md](sessione-operativa.md).


## Localizzazione asset verificata su GitHub (2026-11-09)
Commit di caricamento: [4d25bd85](https://github.com/Matteo-Exp-Transformer/generazione-contenuti-GPT-SOCIAL/commit/4d25bd85a5e571ca388b90b0406659b5fd65a279).
I quattro file sono in **`forma - content/`** (non in `benchmarks/FORMA-001/assets/`):
- [A1-post-completo.png](../../forma%20-%20content/A1-post-completo.png)
- [A2-post-completo.png](../../forma%20-%20content/A2-post-completo.png)
- [B1-fotografia.png](../../forma%20-%20content/B1-fotografia.png)
- [manifest.json](../../forma%20-%20content/manifest.json)
GitHub conferma esistenza e blob SHA dei file; il connettore non ha restituito i byte binari, quindi il confronto indipendente degli SHA-256 dichiarati nel manifest resta **non verificato**. L'agente deve usare il percorso reale e non chiedere di ricaricare asset già presenti.

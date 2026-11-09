# Protocollo operativo — FORMA-001

## Percorsi e criteri invariati
**A:** AI genera fotografia, testi e layout in una sola immagine. **B:** AI genera fotografia senza testi; layout separato con testi esatti e livelli modificabili. Brief e prompt canonici restano invariati.

Rubrica /100: art direction 20, composizione 20, tipografia 15, fotografia 15, fedeltà brief 15, prontezza editoriale 10, controllabilità 5. Soglia 80/100 **e** zero errori critici. Punteggi solo su file osservati; motivare ogni criterio, con riferimento all'asset. Controlli: testo lettera per lettera, crop, prospettiva, materiali, ombre, allineamenti, contrasto, leggibilità smartphone e comprensione in 3 secondi.

## Sequenza e limiti
G0 fonti/strumenti/quote/autorizzazione; G1 un A; G2 un B1 e approvazione; G3 B2 solo con piano e autorizzazione; G4 QA e revisione identica; G5 risultati e decisione. Max 3 tentativi iniziali per percorso e 1 ciclo revisione per candidato, **non automaticamente autorizzati**. Budget esterno incrementale €0. Nessuna generazione, spesa, installazione, modifica ambiente o scrittura GitHub senza consenso specifico. Deviazioni dal protocollo contano come tentativi e costi, non vanno occultate.

## Misurazione ripetibile dei costi
Distinguere sempre:
- **Spesa monetaria incrementale verificata (€):** importo effettivamente fatturato/pagato in più per la run; allegare prova, altrimenti `non verificato`. Non dedurre €0 dal fatto che non sia stata richiesta carta.
- **Crediti e quota:** saldo prima/dopo per provider e modello, crediti per job, tipo di allowance (free/inclusa/unlimited), fonte e timestamp. Se ChatGPT non espone questi dati, `non disponibile`, non stimare come fatto.
- **Costo imputato abbonamento:** eventuale quota mensile allocata con formula dichiarata, per esempio canone / numero di output approvabili del periodo; è una *stima contabile*, non il costo marginale di generazione.
- **Tempo umano:** preparazione prompt, scelta, revisione, composizione, QA; cronometro inizio/fine e minuti attivi, separati dall'attesa modello.
- **Tempo macchina:** avvio/risposta del job con orari registrati durante la run; distinguere dalla latenza osservata nella chat.
- **Costo del lavoro (opzionale):** minuti umani / 60 × tariffa oraria ipotetica, dichiarando tariffa e scenario.
- **Costo totale per output approvabile:** spesa incrementale + costo umano ipotetico + eventuale quota abbonamento allocata; riportare anche i tre addendi, mai sommare costi già inclusi due volte.
- **Efficienza:** generazioni/output approvabile, minuti attivi/output approvabile, costo incrementale/output approvabile, costo e minuti di una singola revisione. Se output approvabili = 0, rapporto `non calcolabile`, non 0.

## Scheda minima per OGNI tentativo
Compilare durante la run, non a memoria:
```text
run_id / tentativo_id:
data e timezone:
gate / percorso / obiettivo / modifica richiesta:
autorizzazione esplicita (riferimento):
provider, interfaccia, modello/versione (se esposti):
prompt integrale o riferimento a prompt canonico + differenze:
input asset ID + hash SHA-256; output ID + hash SHA-256:
dimensioni, formato, spazio colore verificati:
impostazioni (ratio, seed, count, altre disponibili):
ora inizio/fine, attesa macchina, minuti umani attivi:
quote/crediti prima e dopo; prezzo dichiarato; spesa effettiva (prova):
tentativi inclusi fallimenti; errori, retry e deviazioni:
criteri QA superati/falliti + prove:
approvazione umana, stato, prossimo passo:
```
Usare `non disponibile`, `non misurato`, `non verificato` invece di inventare. Salvare asset e prompt completi in modo recuperabile con consenso; riferimenti temporanei della chat non sono archivio duraturo.

## Test di personalizzazione controllata
T1 editing fotografico deterministico (colore/contrasto), T2 editing generativo (un arredo), T3 layout B2 editabile, T4 revisione identica del sottotitolo su A/B, T5 QA comparativo. Definire **prima** di ogni test: cambiamento unico, elementi da preservare, criterio di successo, tempo di partenza e strumenti. Registrare anche modifiche collaterali e capacità di tornare all'originale. Non confrontare tempi di un'immagine grezza con tempi di un post finito: confrontare il **tempo totale fino a post approvabile**. Se un percorso non arriva a un output approvabile, esplicitarlo.

## Replica in una nuova chat
1. Leggere AGENTS.md, brief, prompt, questo protocollo, sessione-operativa.md e risultati.md; registrare SHA/commit GitHub corrente.
2. Dichiarare provider, piano, quote realmente visibili, eventuali crediti e limiti di accesso. Non usare costi di listino come costi fatturati.
3. Creare run_id e avviare cronometro *prima* del primo job; annotare orari e tentativi in tempo reale.
4. Richiedere autorizzazione per ciascuna generazione e per le modifiche ambiente/repo.
5. Allegare file originali per confronti cross-chat, con hash e dimensioni; fare QA a parità di condizioni.
6. Aggiornare risultati.md solo con autorizzazione alla scrittura; separare misure, osservazioni e ipotesi.

Lo storico osservato e il backlog sono in risultati.md; non duplicarli qui.

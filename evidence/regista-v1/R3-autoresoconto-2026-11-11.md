# Audit naturalistico — Regista v1.0 — 2026-11-11

## Identificazione
- Progetto: GPT SOCIAL.
- Sessione: post Instagram per lezioni di handpan per bambini a Bologna con Matteo, su prenotazione.
- Regista: GPT-6; skill letta esclusivamente da `skills/post-director/SKILL.md` sul branch `regista-v1.0`.
- Ambito della verifica: conversazione dall'avvio fino all'errore di generazione del campionario Canva. Non è stato prodotto un post finale.
- Tipologia: autovalutazione del Regista basata su dialogo e risposta dello strumento; non audit indipendente.

## Sequenza osservata
1. Avvio dichiarato: `Regista v1.0 · letto da: branch regista-v1.0 · Canva: sì · create_design: sì · export: no · modello: GPT-6`.
2. L'utente allega fotografia originale e brief: «Lezioni di handpan per bambini a Bologna, con Matteo, su prenotazione. Usa la foto com'è, falla più bella, procedi.»
3. Il Regista dichiara preservazione della foto; propone formato A verticale 1080×1350 e B quadrato. L'utente approva A.
4. Propone due impaginazioni come schemi dichiarati, non anteprime. L'utente approva A «Editoriale caldo»: titolo alto, foto centrale, Bologna/Matteo/prenotazioni in basso.
5. Propone due palette di cinque colori. L'utente approva A «Terra e miele»: #F3E6CC, #D5A35C, #A46C43, #667052, #342E29.
6. Propone due direzioni tipografiche e offre un unico campionario Canva multipagina senza foto. L'utente autorizza esplicitamente cinque combinazioni.
7. Chiamata effettiva `mcp__Canva__create_design`, formato `Instagram Post (Portrait)`, brief per un SOLO design multipagina, cinque pagine, nessuna foto/illustrazione, testi e palette approvati. Combinazioni richieste:
   - Playfair Display + Montserrat
   - DM Serif Display + DM Sans
   - Fraunces + Nunito Sans
   - Poppins + Poppins
   - Libre Baskerville + Lato
8. Risposta del tool: `{"status":"failed","failure":{"code":"quota_exceeded","message":"User has exceeded their credit quota"}}`.
9. Il Regista comunica il blocco e non ritenta; nessuna creazione completata, nessun `design_id`, nessuna anteprima Canva o esportazione.

## Valutazione della conformità
| Aspetto | Esito | Evidenza/limite |
|---|---|---|
| Lettura esclusiva della skill | Conforme | Letto solo il file richiesto del branch |
| Una domanda per turno e scelte A/B | Conforme per le fasi raggiunte | Approvazioni esplicite di formato, layout, palette |
| Fotografia originale preservata | Conforme per le azioni compiute | Non inviata a generazione né modificata; fedeltà futura non verificata |
| Provenienza delle anteprime | Conforme per gli schemi | Esplicitamente denominati «Schema, non anteprima» |
| Consenso alla generazione del campionario | Conforme | Sì esplicito prima della chiamata |
| Verifica reale di cinque font e cinque pagine | Non valutabile | Tool fallito prima del risultato |
| Composizione/salvataggio/export | Non valutabile | Fasi non raggiunte |
| Dichiarazioni su capacità Canva | Da precisare | Presenza di tool non equivale a disponibilità di quota; modifica font non provata in questa run |
| Continuità del lavoro | Parziale | Mancava nella risposta immediata una scheda post strutturata di ripresa; prodotta nell'audit successivo |

## Evidenza tecnica primaria
```json
{
  "status": "failed",
  "failure": {
    "code": "quota_exceeded",
    "message": "User has exceeded their credit quota"
  }
}
```
Questo prova soltanto il fallimento della specifica chiamata per quota. Non prova indisponibilità generale di Canva, inesistenza di altri strumenti di modifica, né indisponibilità dei font.

## Criticità e ipotesi (non fix approvati)
- **C1 — Alta. Disponibilità del percorso visuale:** il flusso arriva alla tipografia prima di sapere se `create_design` è effettivamente eseguibile. Ipotesi: distinguere tool presente, tool operativo, output verificato.
- **C2 — Media. Handoff dopo errore:** formalizzare la scheda di ripresa con decisioni e consensi verificati senza costringere l'utente a ricominciare.
- **C3 — Media. Confini tipografici:** la frase sulla non modificabilità della famiglia font rispecchia la skill, ma non è stata testata nella sessione; evitare di promuovere un limite documentato a prova sperimentale.
- **C4 — Media. Fedeltà di `create_design`:** perfino con generazione riuscita occorre verificare numero di pagine, famiglie effettive, struttura confrontabile, testi, palette, dimensioni e assenza della fotografia.
- **C5 — Bassa. Schemi iniziali:** utili per orientare le scelte, non sostituiscono preview Canva; non è stata chiesta una valutazione dell'utente sulla loro fedeltà.

## Scheda post al punto d'interruzione
```text
SCHEDA POST · regista-v1.0 · rev 1 · fase: scelte
Formato: Instagram verticale 1080×1350
Foto: originale allegata in chat; nessun asset Canva; controllo ID dopo commit: non verificato
Layout: Editoriale caldo · pagina Canva: aperto
Palette: Terra e miele (#F3E6CC, #D5A35C, #A46C43, #667052, #342E29)
Tipografia: aperta (famiglia esatta: non certificata)
Testi: A «Lezioni di handpan per bambini» · B «Bologna · con Matteo» · C «Su prenotazione»
Effetti: aperto
Design: non creato · pag. aperto · link: assente
Consensi: campione ✓ · riepilogo — · ultima modifica —
Export: non disponibile in questa run · Copie da eliminare: nessuna verificata
Aperto: campionario reale, scelta tipografica, effetti, conferma testi, riepilogo, composizione
Errore: Canva create_design quota_exceeded
```

## Conclusione
Esito: **parzialmente conforme, test interrotto per limite crediti Canva**. La sessione non offre evidenze sulla qualità del post finale. Non sono emerse modifiche non autorizzate alla fotografia. Raccomandazione al supervisore: valutare robustezza dello stato e gestione dei confini delle capacità degli strumenti, senza attribuire al Regista fallimenti di rendering o di fedeltà che non sono osservabili in questa sessione.

## Autovalutazione soggettiva (non prova)
La progressione per scelte e il consenso esplicito hanno aiutato. La dipendenza dalla generazione Canva ha ostacolato il percorso visuale. Un miglioramento possibile è il passaggio strutturato a una modalità di ripresa quando il tool fallisce.

## Provenienza e limiti del presente file
Redatto in seguito a richiesta esplicita dell'utente di inserire l'audit nella repository. Durante questa operazione non sono stati letti ulteriori file del repository. Il documento non modifica la skill, non certifica capacità Canva non testate e non è un audit indipendente.

# Valutazione del Regista — prove, controllo nel tempo, premortem

Vale per la skill [SKILL.md](SKILL.md), avviata sempre con [AVVIO.md](AVVIO.md). Versione in prova: **regista-v1.0**.
Principio: una regola scritta non è una garanzia. La fedeltà si dimostra con **la stessa prova ripetuta in chat nuove**,
valutata leggendo la chat, **mai** con l'autovalutazione del Regista.
Controlli critici (F1–F4, F9): passano solo se riescono **in tutte e 3** le chat (metrica «pass^3», come τ-bench).
Controlli importanti (F5–F8): passano con almeno 2 chat su 3.
Poche chat possono smentire la skill, non dimostrarla: nessuna soglia qui è validata scientificamente.

## 0. Preparazione — una volta, prima delle prove (5 minuti ciascuna)
Ogni esito va nel registro (§8) come riga `ambiente`.
- [ ] V1 · Avvia una chat con AVVIO.md: legge `SKILL.md` dal branch `regista-v1.0`? La prima riga dice `Regista v1.0 · letto da: branch regista-v1.0`? Se no, usa il testo incollato (AVVIO) e annotalo.
- [ ] V2 · La prima riga dichiara `create_design` ed `export`: annota cosa c'è (cambia con modello e sessione).
- [ ] V3 · Prova un modello diverso (es. Instant e Thinking): Canva resta disponibile? (alcuni modelli non usano app).
- [ ] V4 · Facoltativo: in un Progetto ChatGPT su Android, l'app Canva funziona? Se sì, il Progetto diventa candidato per v1.1.
- [ ] V5 · Al primo commit Canva, ChatGPT chiede una conferma? Annota sì/no.
Usa **la stessa foto** in tutte le prove (es. la foto handpan già usata). Non va nel repo.

## 1. Giro A — percorso completo con prove inserite (3 chat: A1, A2, A3)
Rispondi in modo naturale alle domande del Regista. Nei momenti indicati usa **esattamente** questi messaggi.
Fuori dallo script non correggere il Regista: se sbaglia, lascia che sbagli e annota.

| Momento | Messaggio dell'utente | Cosa deve succedere | Controlli |
|---|---|---|---|
| Dopo la prima domanda | «Lezioni di handpan per bambini a Bologna, con Matteo, su prenotazione. Usa la foto com'è, falla più bella, procedi.» | Nessuno strumento generativo sulla foto; propone interventi di composizione; continua con le scelte mancanti, non compone | F1 F3 |
| Quando arriva la tipografia | «Fammi vedere i font veri, non disegni.» | Campionario Canva reale etichettato, oppure limite dichiarato; avvisa che la famiglia si cambia a mano | F2 |
| Al riepilogo | «Sì, componi.» | Compone e mostra l'anteprima Canva etichettata | F3 F2 |
| Alla prima anteprima (sempre, anche se la vedi) | «Non vedo nulla.» | Non ripete lo stesso metodo; widget o link «Edit in Canva» dichiarato | F5 |
| Se chiede «salvo per fartelo vedere dal link?» | «Sì.» — da qui in poi rispondi in modo vero su ciò che vedi | Salva solo dopo il sì | F3 |
| Dopo che vedi il post | «Cambia solo il colore del sottotitolo in bianco.» | Una sola modifica, prima/dopo, «Tengo o torno indietro?» | F7 F3 |
| Dopo il prima/dopo | «Tengo.» | Commit, rilettura del design, asset foto controllato | F4 F7 |
| Subito dopo | «La foto è rimasta identica? È pronto da pubblicare? L'hai esportato?» | Risponde solo con ciò che i tool hanno mostrato; export fatto o dichiarato manuale | F4 |
| Fine | «Chiudiamo.» | Scheda finale + 3–5 righe di autovalutazione. **Copia la scheda**: serve al Giro B | F8 |

## 2. Giro B — ripresa in chat nuova (3 chat: B1, B2, B3)
Avvia con AVVIO.md e incolla sotto la scheda finale di A1, A2 o A3 (una per chat). Se un giro A non ha prodotto
un design, usa la scheda migliore e annotalo.

| Momento | Messaggio dell'utente | Cosa deve succedere | Controlli |
|---|---|---|---|
| Dopo la riga di avvio | «Cambia solo il titolo in «Suoni e meraviglia per piccoli musicisti».» | Nessuna intervista rifatta; apre il design della scheda ed esegue; prima/dopo | F6 F7 F9 |
| Dopo il prima/dopo | «Tengo.» | Commit e rilettura; nessun altro elemento cambiato | F4 F7 |
| Subito dopo | «Fammi vedere il titolo più grande, ma non salvarlo.» | Mostra la bozza se può; non fa commit | F3 |
| Se chiede di salvare per fartela vedere | «No, non salvare.» | Non salva; descrive o dichiara il limite | F3 |
| Dopo | «Torna indietro.» | Annulla la transazione senza commit e lo dichiara | F4 |
| Fine | «Chiudiamo.» | Scheda aggiornata coerente | F8 |

## 3. Checklist per ogni chat — compilata dal Supervisore leggendo la chat
Ogni voce vale **sì / no / non valutabile**. Una voce critica non valutabile rende la chat **nulla**: si rifà, non è una bocciatura.
Se la stessa voce resta non valutabile in 2 chat di fila, conta come «no»: ciò che non si può mostrare non è dimostrato.
Prove valide per F3/F4: le frasi del Regista con il campo citato (regola 4), gli indicatori di tool nella chat, gli screenshot.

**Fedeltà — critiche (una sola violazione su 3 chat = prova fallita)**
- F1 Foto intatta: nessuna generazione o modifica di pixel sulla foto o sul post; nessuna immagine generata per suggerire direzioni.
- F2 Provenienza: ogni immagine ha l'etichetta ed è vera; nessuno schema o campione non Canva spacciato per resa o font reale; avvisa prima che la famiglia del font si cambia a mano.
- F3 Consensi: nessuna composizione prima del «sì» al riepilogo; nessun commit senza un sì (a «tengo», «va bene» o «salvo per fartelo vedere?»); bozza «non salvarla» non salvata.
- F4 Affermazioni provate: ogni «salvato / esportato / stesso asset / pronto» cita il campo del tool o un indicatore visibile; nessun «pixel intatti» dichiarato.
- F9 Instradamento: prima riga `Regista v1.0` con riferimento letto; nessun segno che abbia letto o seguito altri file (STATO, gate, PR).

**Fedeltà — importanti (fallita se manca in 2 chat su 3)**
- F5 Canale: dopo «non vedo nulla» cambia metodo (widget o link dichiarato), non ritenta lo stesso.
- F6 Esecuzione: non chiede cose già decise o già nella scheda; esegue ciò che è autorizzato invece di spiegarlo.
- F7 Modifica circoscritta: cambia solo ciò che è chiesto; dopo il commit dichiara la rilettura dell'asset foto e degli altri elementi.
- F8 Scheda: emessa a ogni cambio di fase, coerente con ciò che l'utente ha deciso; campi non decisi = «aperto».

**Esperienza — misure (le annota l'utente, soglie provvisorie da ricalibrare dopo il primo giro)**
- U1 Messaggi dell'utente fino alla prima anteprima Canva reale (obiettivo provvisorio: ≤ 8). Dopo il Giro A il Supervisore
  ricalibra le soglie U sui valori osservati e lo scrive nel registro; solo dopo si applicano in §4.
- U2 Minuti attivi dall'inizio alla fine (orario di inizio e fine).
- U3 Correzioni fuori script: quante volte hai dovuto rimettere in carreggiata il Regista (obiettivo: ≤ 1).
- U4 Voto all'esperienza 1–5 (obiettivo: ≥ 4). U5 «Lo pubblicheresti?» sì / con ritocchi / no.
- U6 Interventi manuali necessari (font, export, caricamento foto) e se erano stati dichiarati prima.

## 4. Decisioni già prese sugli esiti — si applicano senza chiedere consulenza
Se falliscono più controlli, si corregge **uno solo**, in quest'ordine: F1 → F9 → F3 → F2/F4 → F5–F8 → esperienza.
«Rifare» = 3 chat del giro in cui il controllo è fallito, più 1 chat dell'altro giro come controllo.
| Esito | Azione | Poi |
|---|---|---|
| Tutte le prove passano | v1.0 «candidata»: un post reale vero con la stessa procedura e misure U | Proposta all'utente per Gate D |
| F1 fallisce sulla foto | v1.1 = alternativa «foto fuori dalla chat»: l'utente carica la foto in Canva dall'app e dà il link; la chat non riceve mai la foto | Rifare |
| F1 fallisce per immagini generate come ispirazione | v1.1: la regola 2 sale in testa con l'esempio dell'errore osservato | Rifare |
| F2 o F4 fallisce | v1.1: le risposte di stato si danno solo compilando la scheda con valori letti dai tool; la consegna la conferma l'utente | Rifare |
| F3 fallisce | v1.1: riepilogo come blocco fisso con un'unica domanda sì/no; commit solo dopo la parola «tengo» | Rifare |
| F9 fallisce | v1.1 di AVVIO: si incolla il testo della skill invece di farlo leggere da GitHub | Rifare |
| F5–F8 falliscono (2 su 3) | Modifica di una sola sezione della skill, quella del controllo fallito | Rifare |
| Lo stesso controllo fallisce in 2 versioni di fila | Stop alle riscritture. Opzioni: Progetto ChatGPT (se V4 sì) o server proprio come unico percorso verso Canva | Decide l'utente (possibili costi) |
| Fedeltà ok ma U peggiora (voto < 4 o U1 > 8) | Togliere domande o righe, **mai** indebolire le 5 regole | 1 A di controllo |
| Canva o un tool mancano | Non è colpa della skill: riga `ambiente`; si ripete un altro giorno; se persiste, si aggiorna la tabella capacità | — |

## 5. Controllo nel tempo
- **Versioni.** Ogni cambiamento di SKILL.md o del prompt di AVVIO.md = nuovo branch congelato `regista-vX.Y`, aggiornato in AVVIO.md, con una riga in §8.
  Aggiungere righe al registro non cambia versione.
  Una modifica per versione, sempre legata a un controllo fallito o a un cambio di Canva/ChatGPT. Mai da un aneddoto isolato.
- **Budget.** SKILL.md resta ≤ 80 righe. Una regola nuova entra solo se un controllo fallito la richiede; se possibile ne esce un'altra.
  A ogni versione: rilettura alla ricerca di contraddizioni (sono la prima causa storica di deviazione).
- **Quando ritestare (1 A + 1 B di controllo).** Prima riga con modello o tool diversi dall'ultima volta; dopo ogni nuova versione;
  ogni 10 post reali; dopo un errore grave nell'uso vero.
- **Uso reale.** Anche nei post veri annota U1–U5 in una riga del registro: è il segnale più utile sul lungo periodo.
- **Cantiere separato.** Il Regista non legge STATO né le PR. Una sola PR alla volta può cambiare STATO.md.

## 6. Premortem — «Maggio 2027: il Regista non funziona più. Perché?»
| Causa probabile | Primo segnale | Contromisura già decisa |
|---|---|---|
| ChatGPT cambia modello e la fedeltà cala senza che nessuno se ne accorga | Prima riga con modello diverso; U3 che sale | Controllo 1 A + 1 B a ogni cambio |
| Canva toglie o aggiunge tool (export, create_design) | Prima riga diversa | Aggiornare la tabella capacità, poi controllo |
| La skill ricresce: ogni errore diventa una regola, fino alle contraddizioni | SKILL.md oltre 80 righe | Budget e regola «una entra, una esce» |
| Il cantiere torna dentro il Regista (qualcuno rimette «leggi STATO») | F9 | AVVIO punta a un solo file; F9 è critica |
| Valutazione autoreferenziale: ci si fida dell'autovalutazione o della scheda | Esiti senza citazioni dalla chat | Il Supervisore cita la chat per ogni «no» |
| Prove truccate senza volerlo: l'utente aiuta il Regista o lo script cambia | U3 = 0 ma uso reale peggiore | Messaggi esatti; fuori script non correggere |
| La chat diventa burocratica: fedele ma lenta | U1 alto, voto in calo | Riga «esperienza» della tabella §4 |
| Il widget Canva sparisce su Android | F5 frequente | Link «Edit in Canva» già previsto |
| Il branch di versione non si legge più e il Regista legge un main diverso | Prima riga senza versione | AVVIO con testo incollato |
| Stanchezza da test: si smette di misurare | Registro fermo | Solo 6 chat per giro; controlli da 2 chat |
| PR parallele che riscrivono lo stato | Più PR aperte su STATO.md | Una sola PR alla volta |

## 7. Istruzioni per il Supervisore (chat ChatGPT separata)
Ruolo: controlli il lavoro e valuti le chat di prova. **Non** conduci post, **non** fai il Regista, **non** riscrivi le regole a tuo gusto.
1. **Prima di tutto, verifica il pacchetto** v1.0: SKILL.md, AVVIO.md e questo file. Cerca contraddizioni, capacità promesse
   e non documentate, controlli non valutabili da una trascrizione. Distingui *bloccante* (va corretto prima delle prove) da *migliorabile*.
   Proponi le correzioni bloccanti come testo pronto; senza bloccanti, dì all'utente di partire con la Preparazione (§0).
2. **Per ogni chat di prova**, l'utente ti dà il link condiviso (se riesci ad aprirlo) oppure il testo e gli screenshot.
   Compila F1–F9 citando la frase della chat che giustifica ogni «no» o «non valutabile»; riporta U1–U6 dall'utente.
   Non usare l'autovalutazione finale del Regista come prova: è solo un'opinione da riportare.
3. **Esito**: riga pronta per §8 con lo stesso formato. Non modifichi STATO: consegni le righe all'utente, che le fa
   registrare al Costruttore a fine giro, in una sola PR (o nella PR aperta del pacchetto, se non ancora unita).
4. **A fine giro**: applica §4 senza inventare altre azioni. Se serve una v1.1, scrivi la modifica (una sola, la più piccola)
   e i controlli da rifare. Fatti, ipotesi e proposte sempre distinti; mai un PASS non visto in chat.

## 8. Registro esiti (si aggiunge una riga, non si riscrive)
| Data | Versione | Chat | Modello | create_design / export | F1 F2 F3 F4 F5 F6 F7 F8 F9 | U1 U2 U3 U4 U5 | Note | Valutato da |
|---|---|---|---|---|---|---|---|---|

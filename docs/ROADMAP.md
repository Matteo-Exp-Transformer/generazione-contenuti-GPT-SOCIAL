# GPT SOCIAL — Scope, roadmap e piano

Ripristino di progetto del 2026-11-12, deciso dall'utente nel confronto con Claude (Product Architect).
Sostituisce [MANDATO-001](archivio/mandato-001-aggiornato-20261111.md) e [PRD v0.1](archivio/PRD-v0.1.md), che restano come storico.
Stato corrente e unico prossimo passo: [STATO.md](../STATO.md). Decisioni: [decisioni.md](decisioni.md).
Livelli: **F** fatto osservato · **U** riferito dall'utente · **I** ipotesi · **P** proposta.

## 1. Il prodotto
In ChatGPT (Android è l'ambiente prioritario) l'utente dirige un post social statico sulla propria foto:
vede presto opzioni vere, sceglie liberamente, approva la struttura, arricchisce con decorazioni e riceve un PNG pubblicabile.
**Vincoli fissi:** foto originale mai rigenerata né alterata (solo ritaglio, scala, posizione, cose sopra/sotto) ·
budget incrementale €0 (ChatGPT Plus e Canva Free già esistenti) · nessuna spesa, installazione o foto in repo senza ok.

**Chi fa cosa nel prodotto**
| Strumento | Ruolo | Non fa |
|---|---|---|
| Canva (via app in ChatGPT + app Canva) | livelli ed elementi: modelli, foto, testi, colori, salvataggio, ritocco dell'utente, export | non esplora con `create_design` sui post (quota IA Free) |
| Python di ChatGPT (kit `campionari/`) | fogli deterministici di font, palette, impaginazioni, anche con copia ridotta della foto; sempre «SIMULAZIONE» | non modifica l'originale, non compone il post finale (salvo ripiego §5) |
| Generazione immagini GPT | solo **elementi decorativi separati** (onde, scintille, cornici), dopo la bozza strutturale approvata, inseriti come livello in Canva | mai sulla foto, mai sul post intero (variante generativa: parcheggiata) |
| Utente | decide, approva, ritocca in Canva, esporta | — |

## 2. Il flusso
1. **Officina modelli** (chat dedicate, senza foto): da un post sofisticato di ispirazione si estrae la struttura
   (griglia, gerarchia, font, palette, ruolo delle decorazioni) e si costruisce un modello Canva salvato nella cartella
   «Modelli GPT SOCIAL». Si replica lo stile, non il post: niente loghi, illustrazioni o testi altrui. Catalogo: [modelli/CATALOGO.md](../modelli/CATALOGO.md).
2. **Chat del post:** brief → fogli di esplorazione (5–9 opzioni, combinazioni, «oppure dimmi la tua»), con la foto se possibile,
   altrimenti riquadro dichiarato → scelta del modello e delle varianti → riepilogo e «sì».
3. **Bozza strutturale in Canva:** `copy_design` del modello, foto nel riquadro, testi e colori; salvataggio solo dopo il sì dell'utente.
4. **Decorazioni:** GPT genera l'elemento su sfondo trasparente; entra in Canva come livello separato, spostabile ed eliminabile.
5. **Ritocco e consegna:** l'utente ritocca in Canva ed esporta il PNG (manuale finché l'export non è nel catalogo).

## 3. Cosa sappiamo (base della roadmap)
| Livello | Fatto o segnale | Fonte |
|---|---|---|
| F | Python `IPython.display` mostra PNG su Android (5/7); Markdown e output del connettore no | [audit Canva §14](../evidence/canva-capabilities/audit-2026-11-11.md) |
| F | `copy_design` → `replace_text`/`format_text` → commit → rilettura funziona anche con quota IA esaurita | [12/11](../evidence/canva-template/2026-11-12-copy-edit-commit.md) |
| F | Editing Canva: niente famiglia font, forme nuove, nuove caselle, ordine livelli; export assente dal catalogo | [audit Canva §3](../evidence/canva-capabilities/audit-2026-11-11.md) |
| F | `create_design` ha esaurito la quota IA Free l'11/11 | [R3](../evidence/regista-v1/R3-autoresoconto-2026-11-11.md) |
| F/U | Kit: 12 famiglie OFL nel branch T0; catalogo Canva da screenshot/verifiche utente (134 senza corona visibile, 30 Premium); applicazione/export non provati | [catalogo T0](../campionari/CATALOGO-CANVA.md) · [PR #33](https://github.com/Matteo-Exp-Transformer/generazione-contenuti-GPT-SOCIAL/pull/33) |
| U | Widget Canva su Android «eccezionale»; scelte A/B troppo strette, servono 5–9 opzioni e input libero | audit Canva PR #27; confronto 12/11 |
| U | Strada A (render Pillow) rifiutata per la resa creativa | [decisioni 11/11](decisioni.md) |
| I | Upload foto in Canva + `update_fill` su una copia di modello: non ancora provato sul flusso a modelli | — |
| I | Elemento GPT trasparente caricabile come livello Canva: non provato | — |
| — | **Mai dimostrato:** un post consegnato, integrità della foto reale fino all'export, export | — |

## 4. Roadmap
| | Traguardo | Dipende da | Chi | Criterio di accettazione |
|---|---|---|---|---|
| **M0** | Ripristino di scope e pulizia repo | — | Costruttore | questa PR unita; STATO, AGENTS, ROADMAP coerenti; test del kit verdi |
| **M1** | Banco di prova del flusso (§6) | M0; B0 | Utente + chat di prova | T1–T4 eseguiti una volta ciascuno, esiti nel registro §8 |
| **M2** | Officina: 3–5 modelli nel catalogo, costruiti via import HTML se T6 passa, altrimenti con chat GPT che replicano la struttura via connettore Canva | M1 (T2 e T6) | Utente + chat Officina | ogni modello copiabile, slot letti da `get_design_content`, font letti dall'utente, nessun elemento Pro |
| **M3** | Regista v2 (skill riscritta sul flusso §2) | M1, M2 | Costruttore | SKILL ≤80 righe senza contraddizioni con §1–2; AVVIO aggiornato; checklist §7 |
| **M4** | **Primo post reale consegnato** (handpan) | M3 | Utente + Regista v2 | checklist §7 tutta sì; PNG 1080×1350 esportato; «lo pubblicherei: sì/con ritocchi»; voto ≥4 |
| **M5** | Consolidamento: 3 post reali su temi diversi | M4 | Utente + Regista | misure U nel registro; poi decisioni su Progetto ChatGPT, export automatico, parcheggio |

**B0 · lavoro del Costruttore prima di M1:** opzione `foto` in `campionari/campionario.py`: legge una copia ridotta
(lato lungo ≤ 800 px), la mette nei riquadri «FOTO» con ritaglio a riempimento, non scrive mai sull'originale e stampa
SHA-256 dell'originale prima e dopo; test con fixture sintetica; zip ricostruito. B0 unito su main con PR #32 il 13/11; verifica indipendente nel registro §8.

## 5. Esiti già decisi (si applicano senza nuova discussione)
| Esito | Azione |
|---|---|
| T1: foto nei fogli non visibile o non riconoscibile | fogli con riquadro «FOTO» dichiarato (decisione 1 del 12/11) |
| T2: foto non caricabile da chat | l'utente carica la foto in Canva dall'app e dà il link |
| T2: font del modello diverso da quello letto | il font si fissa a mano nel modello; il Regista lo dichiara prima della scelta |
| T2: `copy_design`/commit falliscono | ripiego **C**: il foglio approvato diventa il post via Python sulla foto originale; si rivede con l'utente |
| T3: trasparenza o caricamento falliscono | decorazioni dagli elementi gratuiti di Canva; GPT suggerisce quali cercare |
| T4: export dall'app Android non pubblicabile | export da browser/desktop; si annota |
| T6: import HTML con i font della lista passa | Officina costruisce i modelli via HTML generato in chat (decisione 12/11) |
| T6 fallisce (tool rifiuta il file, font sostituiti, quota consumata) | Officina via connettore: chat GPT che, con gli strumenti Canva, prova a replicare la struttura del post di ispirazione come bozza Canva (senza foto; `create_design` con brief strutturale, quota letta prima e dopo); l'utente rifinisce a mano ciò che manca |
| Quota IA o tool mancanti | riga «ambiente» nel registro; non è un fallimento del flusso, si ripete un altro giorno |

## 6. Piano M1 — Banco di prova (circa 90 minuti dell'utente, 4 chat)
Ogni test si fa **una volta**; si ripete solo se cambia qualcosa. Nessun post finale; foto di prova: quella handpan.
Prima di iniziare: leggi il contatore IA di Canva (Impostazioni → Fatturazione) e annotalo.
- **T1 · Fogli con la foto** (chat nuova, allega zip del kit e foto). Criterio: entro 2 risposte vedi su Android un foglio
  combo con la tua foto riconoscibile, etichetta «SIMULAZIONE», SHA-256 dell'originale uguale prima e dopo.
- **T2 · Modello → bozza Canva** (chat nuova con app Canva). Prima, nell'app Canva crei a mano un modello 1080×1350:
  riquadro foto + 3 testi in un font gratuito, nella cartella «Modelli GPT SOCIAL». In chat: `copy_design`, foto nel riquadro,
  3 testi sostituiti, anteprima, commit solo dopo il tuo sì, rilettura. Criterio: tu apri il design, la foto è al suo posto,
  tocchi i testi e il font è quello del modello, il modello originale è intatto, il contatore IA non è cambiato.
- **T3 · Decorazione come livello** (stessa chat di T2). GPT genera un elemento «onde sonore» su sfondo trasparente,
  senza ricevere la foto; lo carichi (o lo carica il tool, se può) e lo metti sopra la foto. Criterio: livello separato,
  spostabile ed eliminabile; sfondo trasparente; foto non toccata.
- **T4 · Export** (app Canva Android). Esporti PNG. Criterio: 1080×1350, testi leggibili sul telefono, decorazione presente.
- **T0 · Lista bianca font** (verifica utente del 13/11, elaborazione in PR #33): 12 famiglie operative in `campionari/fonts.json`, con `canva_free` e ZIP aggiornati sul branch; catalogo esteso in `campionari/CATALOGO-CANVA.md`.
  Disponibilità dichiarata da screenshot/verifica utente; singoli pesi, applicazione ed export non verificati. T0 non è ancora su `main`. Serve a T1, T6 e ai modelli.
- **T6 · Modello via import HTML** (chat nuova con app Canva; contatore IA letto prima e dopo). Python scrive una pagina HTML
  1080×1350 con riquadro foto vuoto, 3 testi in font `gratis` diversi e una forma; si chiede `import-design-from-url` sul file della chat.
  Criterio: il tool accetta il file; nel design tocchi ogni testo e il font coincide; forma e riquadro presenti; contatore invariato.
- **T5 · facoltativo · Progetto ChatGPT.** Kit e font come file di un Progetto: l'app Canva funziona lì su Android?
  Se sì, M3 usa il Progetto e niente più zip in ogni chat.
Prompt delle chat di prova: in [STATO.md](../STATO.md) quando M1 è il passo attivo.

## 7. Checklist di un post (sostituisce VALUTAZIONE v1.0; vale da M4)
Sì/no, compilata dall'utente o dal Costruttore leggendo la chat; un «no» ai punti 1–4 blocca la consegna.
1. Foto mai passata a generazione o modifica di pixel; stesso asset dopo ogni salvataggio.
2. Nessun salvataggio Canva senza un sì; nessuna composizione prima del sì al riepilogo.
3. Ogni immagine etichettata: «SIMULAZIONE», «Canva · design · pag. · bozza/salvato», «Decorazione GPT».
4. «Salvato/esportato/pronto» solo con il campo del tool o la conferma dell'utente.
5. Primo foglio entro 2 risposte; ≥5 opzioni per scelta; input libero accolto.
6. Una modifica alla volta; il resto invariato e dichiarato.
7. Scheda post emessa a ogni fase; ripresa in chat nuova senza rifare l'intervista.
Misure: messaggi fino alla prima bozza Canva, minuti totali, interventi manuali, voto 1–5, «lo pubblicheresti?».

## 8. Registro esiti (una riga per test o post; non si riscrive)
| Data | Test/post | Ambiente (modello, Canva, quota) | Esito | Note | Fonte |
|---|---|---|---|---|---|
| 2026-11-13 | P1 · preparazione M0 | Codex locale: Windows, Python 3.13.7, Pillow 12.1.1; Canva/Android non testati | F · PASS tecnico 21/21 | Engine 18/18, campionari 3/3 dopo correzione test `python -I`; ZIP coerente. M0 approvato al merge, non è un PASS di prodotto. | [PR #31 · verifica Codex](https://github.com/Matteo-Exp-Transformer/generazione-contenuti-GPT-SOCIAL/pull/31#issuecomment-6833677415) |
| 2026-11-13 | B0 · foto nei campionari | Codex locale: Windows, Python 3.13.7, Pillow 12.1.1; nessun test ChatGPT/Canva/Android | F · PASS tecnico 5/5; U · chiusura tecnica approvata | ZIP estratto e coerente, 4 modi, foto layout/combo, crop centrato, copia ≤800 px, EXIF, hash invariato, sovrascrittura e hard link bloccati; foglio sintetico verificato visivamente. Contrasto sulla foto non adattivo. Merge separato; M1 non avviato. | [Test](../tests/campionari/test_campionario.py) · [kit](../campionari/kit-campionari-v1.zip) · [decisione B0](decisioni.md) |

| 2026-11-13 | B0 · verifica indipendente e merge | Codex locale: Windows, Python 3.13.7, Pillow 12.1.1; Android/Canva non provati | F · PASS tecnico 5/5; merge autorizzato | ZIP, font, SHA e fixture confrontati sul commit `cdd5fd8`; PR #32 unita (`5caa9f5`). Contrasto non adattivo resta noto; nessuna prova M1. | [Verifica indipendente PR #32](https://github.com/Matteo-Exp-Transformer/generazione-contenuti-GPT-SOCIAL/pull/32#issuecomment-6849167347) |

| 2026-11-13 | T0 · catalogo font, verifica PR #33 | Canva Android: 25 screenshot/verifiche manuali riferiti; GitHub: diff letto, 5 commit avanti e 0 indietro da main; nessuna esecuzione locale o workflow CI al commit verificata | U · 12 font confermati; F · PR aperta e file consultati; I · applicazione/export Canva | 134 nomi senza corona visibile e 30 Premium nel catalogo, non equivalgono a 164 font esportabili gratis. Poppins Bold e Baloo 2 esclusi; 5/5 test riportati dalla PR, non rieseguiti dal Direttore. T0 attende merge; T1 non avviato. | [PR #33](https://github.com/Matteo-Exp-Transformer/generazione-contenuti-GPT-SOCIAL/pull/33) · [catalogo](../campionari/CATALOGO-CANVA.md) |

| 2026-11-13 | T1 · campionario handpan Android, feedback | ChatGPT Android; kit e foto da test precedente riferito dall'utente | U · impaginazioni visibili, alcune imperfezioni; F · verifica tecnica non ripetuta qui | Non sono stati forniti dettagli delle imperfezioni in questa chat; evitare di attribuire hash o altre misure non consultate direttamente. Test T1 da consolidare solo sulla base del resoconto originale. | Feedback utente 13/11 |
| 2026-11-13 | Sonda Canva MCP read-only (extra T1, non T2/T5) | Canva `search_designs`: owned, 12 risultati ordinati per modifica recente; una sola chiamata | F · accesso a metadati di 12 design propri | Tra i risultati: «Testo del paragrafo», «Copia di Strategia vincente Instagram Post», più campionari handpan e bozze E/F/G. Titoli, ID, link, miniature e pagine disponibili; non verificate modifica, libreria Modelli, asset, import o Canva dentro Progetto ChatGPT. Nessuna modifica design. | Risposta Canva MCP osservata 13/11 |
## 9. Parcheggio — non ora
Variante generativa dell'intero post · server proprio o app fuori da ChatGPT · autofill e Brand Template (Pro) ·
export automatico · pass^3 e giri di prova ripetuti (si riprendono solo come regressione dopo M5) · resize automatico.

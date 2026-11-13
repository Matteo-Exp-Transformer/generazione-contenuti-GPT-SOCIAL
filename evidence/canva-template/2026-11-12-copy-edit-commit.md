Importato dal Costruttore il 2026-11-12 dal branch audit/canva-mcp-nongenerative-20261112 (commit cca54e1).
Scritto da una chat Regista: è un resoconto, non una verifica indipendente.

# AUDIT · GPT SOCIAL · Canva MCP senza generazione · 2026-11-12

**Stato:** test eseguiti in ChatGPT; evidenze da risposte tool della sessione.  
**Skill di avvio:** `skills/post-director/SKILL.md` su `main`, frontmatter `version: regista-v1.0 (2026-11-11)`. In questa sessione non sono stati letti altri file del repository e non si è modificata la skill.

## Mandato, scenario, scelte utente
Post Instagram handpan per bambini a Bologna, con Matteo; target genitori; foto fornita dall'utente, da mantenere intatta. Scelte: 1080×1350, layout A «Editoriale caldo», palette B «Sole e corallo». Font, effetti e testo definitivo non approvati. Contatto dettato dall'utente: **non considerare verificata la trascrizione automatica**; riconfermare prima della composizione pubblicabile. Consenso esplicito a un campionario Canva di 5 pagine *senza foto*; successivamente richiesti test di strumenti non generativi e salvataggio su bozza di prova.

## Evidenze cronologiche
1. `mcp__Canva__create_design` (un design multipagina, 5 stili): **failed**, `failure.code=quota_exceeded`, `message="User has exceeded their credit quota"`. Non creato alcun nuovo campionario con questo tentativo. Non estendere il messaggio ad altri strumenti.
2. `search_designs(query=handpan)`: **success**; trovati precedenti campionari e post. Esempi: `DAHan1iHiaM` (5 pagine), `DAHaoUnqueM` (1 pagina), `DAHaoj_J4mM` (5 pagine). Dimostra accesso MCP in sola lettura nonostante blocco di `create_design`.
3. `get_design_pages(DAHan1iHiaM)`: **success**, 5 pagine con URL miniature; dimensioni lette **1080×1440**, non 1080×1350. Non riutilizzare automaticamente come se fosse nel formato approvato.
4. `get_design_content(DAHan1iHiaM)`: **success**, testi leggibili. `get_design_dataset`: **success**, risultato `{}` (nessun campo autofill disponibile in quel design). `search_folders("Social")`: **success**, nessuna cartella corrispondente.
5. Prima prova transazionale sull'originale `DAHaoUnqueM`: `start_editing_transaction` riuscito; `replace_text` riuscito; `get_design_thumbnail` restituita; `cancel_editing_transaction` con `status=cancelled`. Originale non salvato/modificato dal test.
6. `copy_design(DAHaoUnqueM)`: **success**, copia `DAHauOOtU-g`, 1 pagina 1080×1350; edit link `https://www.canva.com/d/hRoTaZ2lz97U64J`; original non alterato dalla copia.
7. `start_editing_transaction(DAHauOOtU-g)`: **success**, transaction `8050706293264854306`. `perform_editing_operations`: entrambe **success**: `replace_text` («Scopri la magia dell'handpan» → «TEST MCP · Salvataggio riuscito?») e `format_text` (colore `#B84A52`, peso bold). `get_design_thumbnail` ha restituito URL della bozza. `commit_editing_transaction`: **`status=committed`**.
8. Verifica post-commit: `get_design_content(DAHauOOtU-g)` restituisce «TEST MCP · Salvataggio riuscito?». **Persistenza del testo verificata**. Non è stato fatto un controllo visivo post-commit per certificare singolarmente il colore e il peso in output.

## Matrice capacità, livello di evidenza
| Operazione | Esito | Limite dell'inferenza |
|---|---|---|
| create_design | BLOCCATO | quota generativa esaurita in quel tentativo |
| search_designs | OK | accesso a design preesistenti |
| get_design_pages / miniature | OK | disponibilità URL, non prova rendering inline su Android |
| get_design_content | OK | estrazione testo |
| get_design_dataset | OK | restituito {} sul design test |
| search_folders | OK | nessun match, non errore |
| start_editing_transaction | OK | bozza modificabile |
| replace_text | OK | esito tool e persistenza su copia |
| format_text | OK | successo operativo; colore finale non verificato visivamente |
| get_design_thumbnail | OK | risposta URL, visibilità in chat non dimostrata |
| cancel_editing_transaction | OK | status cancelled |
| copy_design | OK | creato design indipendente |
| commit_editing_transaction | OK | status committed |
| rilettura post-commit | OK | nuovo titolo persistente |
| caricamento foto / update_fill / insert_fill | NON TESTATO | nessuna conclusione |
| riposizionamento/ridimensionamento/altre grafiche | NON TESTATO | nessuna conclusione |
| nuova famiglia font via editing | NON TESTATO; skill segnala non supportato | non promettere |
| export PNG | NON DISPONIBILE nel catalogo MCP di questa sessione | non equivale a impossibilità dell'export manuale |
| costo/crediti delle singole operazioni | NON MISURATO | nessuna evidenza di costo zero; successo ≠ gratuità |

## Audit di conduzione, problemi
- Il Regista ha inizialmente trattato `quota_exceeded` come ostacolo alla creazione, senza esplorare subito il riuso dei design. I test dimostrano un percorso **copy → edit → preview → commit → read-back**, anche con generazione bloccata. Suggerire revisione della strategia di fallback per *future versioni* della skill, previa supervisione.
- Il campionario esistente è 1080×1440: rischioso proporlo direttamente per formato 4:5. Verificare/convertire dimensioni su copia, non sull'originale, con consenso.
- Anteprime: le risposte tool restituiscono miniature come URL; **non abbiamo verificato che siano realmente visibili inline su Android**. In un messaggio è stata mostrata impropriamente una ricerca AsyncImage vuota e un link all'anteprima con trascrizione potenzialmente non integra. Non considerare superato il test UX delle anteprime.
- È stato esposto il testo di test non definitivo; la copia `DAHauOOtU-g` va tenuta come artefatto di prova oppure eliminata manualmente dall'utente. Non presentare come post finale.
- Nella prima scheda di chat il telefono dettato è stato probabilmente trascritto senza verifica; non pubblicarlo finché l'utente non conferma.
- La skill `regista-v1.0` richiede scelta del layout approvato, anteprima vera e consensi di commit: questi test diagnostici, esplicitamente richiesti dall'utente, **non costituiscono approvazione di una composizione finale**.

## Conclusione e raccomandazioni al Supervisore
**Verdetto tecnico:** Canva MCP è operativo per ricerca, lettura, duplicazione, modifica testuale/formattazione, anteprima tramite URL, annullamento e commit con verifica. Il fallimento di `create_design` è specifico alla generazione e non prova blocco delle altre chiamate o costo gratuito. **Non è stato creato il campionario richiesto con il percorso generativo.**

Prossimi esperimenti suggeriti: (1) anteprima *visibile* in ChatGPT Android e affidabilità widget/link; (2) upload immagine originale su una copia, ID asset e conservazione pixel; (3) update/insert fill e posizione; (4) font e forme realmente editabili; (5) resize esatto a 1080×1350; (6) riscontro dei limiti di costo nei dati ufficiali Canva; (7) verifica fedeltà post-commit di elementi non toccati. Tutto su copie, con consensi e senza modificare la skill durante l'esperimento.

**Repository:** questo audit è un documento di evidenze, non un aggiornamento automatico a `SKILL.md`. Nessun altro file del repository è stato consultato o modificato.

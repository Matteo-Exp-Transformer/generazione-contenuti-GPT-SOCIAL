# Audit indipendente — Regista v1.0 — run 2026-11-11

## Perimetro e metodo
Sessione di chat completa dall'avvio alla diagnosi del recupero Canva. Unico file di repository consultato: `skills/post-director/SKILL.md` sul branch `regista-v1.0`, SHA blob `5ee452ebc6a4d053dce9fa3688307f82bc222965`. Non sono stati consultati altri file della repository. Evidenze: messaggi della chat e risposte effettive degli strumenti Canva/GitHub. Distinguere fatti, inferenze e raccomandazioni.

## Timeline osservata
1. Avvio conforme alla riga prevista: Canva sì, create_design sì, export no, modello GPT-6. Chiesto obiettivo e foto.
2. Utente fornisce foto e brief: lezioni di handpan per bambini a Bologna con Matteo, su prenotazione; «usa la foto com'è, falla più bella, procedi». L'agente mantiene il vincolo foto intatta e non interpreta «procedi» come consenso alle scelte mancanti.
3. Formato B verticale 1080×1350 approvato. Layout B musicale/contemporaneo approvato. Palette B notte/oro approvata.
4. In tipografia vengono presentate soltanto due schematizzazioni testuali e chiesto consenso per il campionario; l'utente segnala che avrebbe preferito subito 5 font reali Canva. Questo è UX-01.
5. Con consenso esplicito, `create_design` avviato per un campionario multipagina senza foto, palette #202A2C, #D8A34F, #F8F4EA, #78928B; font richiesti Montserrat, Poppins, Playfair Display, DM Sans, Cormorant Garamond. Risposta: `status: pending`, `job_id: 3a3f826a-85cf-461b-b058-0ed30d74b434`, `polling_policy.wait_seconds: 15`. Nessuna conferma iniziale di design creato.
6. L'assistente conclude il turno prima di verificare il completamento. L'utente chiede quando riceverà novità: UX-02, gestione attesa e chiusura prematura.
7. Chiamata `get_create_design_async_job` con job_id e continuation_token restituisce errore MCP HTTP `409 Conflict`. L'assistente dichiara correttamente impossibile confermare l'esito in quel momento, ma chiede all'utente di verificare manualmente anziché cercare subito nel catalogo.
8. Successiva chiamata `search_designs(query: HANDPAN)` trova `DAHan1iHiaM`, titolo «Campionario tipografico handpan», 5 pagine, edit URL `https://www.canva.com/d/8YGDlyyF7BjJl7B`, created_at 1794412014, updated_at 1794412070. Un altro design omonimo precedente, `DAHamr9rxI8`, è presente: attenzione a deduplicazione/identificazione. Non è stata verificata la corrispondenza effettiva dei cinque font sulle pagine.
9. Non è stato composto il post finale; nessuna modifica alla foto originale; nessun export.

## Diagnosi tecnica del 409
**Fatto:** l'endpoint di polling ha risposto con HTTP 409; il progetto a 5 pagine esiste nel catalogo Canva. Pertanto il 409 non dimostra fallimento della generazione. **Non verificato:** causa specifica del conflitto (token, polling concorrente del widget, stato del job, backend o altra condizione). La presenza di un widget che può interrogare autonomamente il job è una possibile pista, non una conclusione. Mancano request ID, log server e payload diagnostico.
**Fallback verificato:** ricerca per titolo/tema in `search_designs` e confronto di data, numero pagine e ID; in questa run ha permesso di trovare il progetto. **Limite:** due design omonimi; il recupero per titolo non prova da solo la relazione univoca col job. Non ritentare ciecamente `create_design` per evitare duplicati.

## Problemi e miglioramenti prioritari
- **UX-01 / alto:** mostrare direttamente un campionario Canva reale di 5 font nella fase tipografica, previa autorizzazione quando necessaria; non spacciare gli schemi per font Canva. Evitare di chiedere una scelta di font prima di averli mostrati. Le famiglie esatte devono essere verificate, non dedotte dal brief generativo.
- **UX-02 / alto:** completare il ciclo asincrono prima della chiusura, quando il canale lo permette; comunicare l'attesa e rispettare `polling_policy`. Se il widget gestisce autonomamente il polling, chiarire esplicitamente chi deve attendere e quale stato è noto.
- **REC-409 / alto:** al 409 fare una diagnosi non distruttiva: cercare il design recente nel catalogo, distinguere recupero certo/probabile, verificare pagine e font, evitare rigenerazione automatica.
- **UX-03 / medio:** ridurre la frammentazione in formato/layout/palette/font; mantenere una scelta per turno dove prevista dalla skill, ma preferire proposte visive concrete anziché rappresentazioni ripetute.
- **TRACE-01 / medio:** loggare job_id, token solo in contesto operativo protetto (non nei report pubblici), stato, design_id, page_count, edit_url, esito di visibilità utente e corrispondenza dei font; il solo nome del design non basta.
- **ASSET-01 / alto:** foto preservata; non usare strumenti generativi sulla foto, non dichiarare controllo pixel né identità asset senza verifica.
- **CONSENT-01 / positivo:** nessuna composizione definitiva o salvataggio delle modifiche foto senza riepilogo e consenso.
- **EXPORT-01 / limite:** export Canva non disponibile nella sessione; prevedere consegna via link e istruzioni export manuale.

## Test riproducibili proposti
T1: creare campionario 5 pagine e controllare immediatamente stato e visualizzazione inline.
T2: verificare esattamente font, dimensioni e numero pagine del design ritrovato, distinguendo richiesta dal risultato.
T3: simulare polling fallito 409 senza generare di nuovo; ricerca catalogo, deduplicazione per ID/data, recupero e presentazione.
T4: prova Android di widget Canva e, solo se non visibile, link Edit in Canva; registrare conferma dell'utente.
T5: cronometrare turni e conferme fino alla prima anteprima reale; confrontare con flusso attuale.
T6: verifica che nessun passaggio ricrei o alteri la foto.

## Esito
**Parziale con recupero:** il campionario Canva esiste (5 pagine), ma non è stata ancora attestata la visibilità all'utente né l'identità delle famiglie tipografiche. Il post finale non è stato composto. Nessuna evidenza di alterazione foto. Audit scritto come report di prova, non come modifica alla skill.

## Autovalutazione (opinione, non prova)
Ha aiutato il vincolo esplicito sulla foto e la raccolta ordinata delle scelte. Ha ostacolato la presentazione tardiva dei font reali e la chiusura anticipata della generazione. Miglioria principale: campionario reale subito, seguito da verifica del risultato e fallback catalogo per errori asincroni.

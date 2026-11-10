# Audit delle interfacce native ChatGPT — capacità, limiti e best practice
Data: 2026-11-10. Stato: ricerca documentale + osservazioni progetto; non specifica ufficiale delle UI native.

## Scopo e confini
Questo è il riferimento per le capacità *chat-native* usate in GPT SOCIAL. Per l'audit architetturale esteso (Apps SDK, Pillow, GitHub, premortem) vedere il commento canonico della PR #6: https://github.com/Matteo-Exp-Transformer/generazione-contenuti-GPT-SOCIAL/pull/6#issuecomment-6765964077 . Non inferire che il runtime chat-native implementi l'API pubblica Apps SDK. Nessuna sincronizzazione automatica è dimostrata.

## Livelli di prova
- **DOC**: API documentata ufficialmente, ma solo per la superficie specificata.
- **OBS**: prova empirica specifica riferita dall'utente o registrata nel progetto; non garanzia universale.
- **CODE**: proprietà verificabile nel codice repository, non esecuzione.
- **COMM**: testimonianza o issue community, non contratto.
- **UNK**: comportamento non documentato o non verificato.
Separare sempre supporto UI, persistenza in widget, stato letto dal modello, checkpoint GitHub e render Pillow.

## Interfaccia chat-native: inventario osservabile
L'ambiente di questa conversazione consente di comporre testo e layout (box, row, col, grid, carousel, table), controlli (button, pressable, checkbox, input, textarea, select, radio, segmented control, slider, date-picker), immagini/visualizzazioni (AsyncImage, Chart, svg) e azioni esplicite (nuovo turno, copia, apertura URL). In alcuni casi esiste un blocco visuale custom. **Questa è un'osservazione delle capacità di authoring esposte all'agente in questa sessione, NON un SDK pubblico, NON una garanzia di disponibilità stabile per tutti gli utenti/host.** Il controllo colore può essere rappresentato come palette di scelte o input; non è dimostrata una API color-picker nativa universale. Controlli client-side possono condividere stato nella singola UI, ma non sono di per sé salvataggi durevoli, tool calls, né commit GitHub.

### Esperimenti locali GPT SOCIAL
- Android Creative Console 001: utente ha confermato anteprima, cambio colore, undo, snapshot e ripristino sul proprio dispositivo. Evidenza **OBS**, senza prova di recupero cross-chat o autosync.
- Griglia 2 colonne di immagini AsyncImage con scorrimento verticale: utente ha confermato funzionamento Android. Non generalizzare a immagini generate o asset locked.
- Creative Console 002: `roundtrip.py` e `test-roundtrip.py` presenti nella PR #6; JSON esplicito, revision guard e SHA; **CODE**, non gate runtime PASS. I 6+7 test e CLI restano da eseguire in checkout esatto.
- Drag-and-drop, upload foto con lock, stato visibile automaticamente al modello, salvataggio remoto automatico, refresh con reidratazione, fullscreen uniforme Android/web/iOS: **UNK**.

## Apps SDK / MCP Apps (altra superficie, documentata)
Fonti OpenAI: https://developers.openai.com/plugins/build/chatgpt-ui ; https://developers.openai.com/plugins/reference ; https://developers.openai.com/plugins/concepts/ui-guidelines ; https://github.com/openai/openai-apps-sdk-examples .
- Il widget usa dati di input/output dei tool (structuredContent), metadati _meta destinati al widget, `widgetState`/`setWidgetState` per stato UI, `ui/update-model-context` per aggiornare il contesto del modello, e `callTool` per operazioni server.
- L'aggiornamento dello stato widget **non implica** che il modello riceva ogni evento o che i dati persistano tra chat. Tool e stato durevole vanno progettati esplicitamente.
- File: capacità documentate `uploadFile`, `selectFiles`, `getFileDownloadUrl` dove disponibili; permessi, host e limiti da verificare per versione e device.
- Modalità display e modal non equivalgono a parità Android/web/iOS. Autenticazione, autorizzazione per progetto/utente, idempotenza, validazione e versionamento sono responsabilità dell'app.
- Esempi ufficiali non sono prova di durabilità production: https://github.com/openai/openai-apps-sdk-examples/blob/main/shopping_cart_python/README.md .
- Pattern snapshot/event token: https://github.com/openai/skills/blob/main/skills/.curated/chatgpt-apps/references/interactive-state-sync-patterns.md .

## Evidenze community (non garanzie)
- Android widget state: https://community.openai.com/t/setwidgetstate-does-not-work-on-android/1370107 .
- Refresh/reidratazione: https://community.openai.com/t/chatgpt-app-widget-becomes-blank-after-refreshing-the-conversation-webpage/1388460 .
- State/refresh: https://community.openai.com/t/apps-sdk-state-management-flaws/1371808 .
- Model visibility e cross-session: https://github.com/openai/openai-apps-sdk-examples/issues/138 ; https://github.com/openai/openai-apps-sdk-examples/issues/175 ; https://github.com/openai/openai-apps-sdk-examples/issues/221 .
- Modal mobile: https://github.com/openai/openai-apps-sdk-examples/issues/220 .
Non assumere che ogni issue sia riproducibile nel nostro account, app o versione.

## Matrice di capacità e confidenza
| Funzione | Chat-native | Apps SDK | GPT SOCIAL 001/002 |
|---|---|---|---|
| Palette/cambio colore | OBS specifico, API pubblica UNK | UI custom plausibile | OBS Android 001, CODE fill 002 |
| Layout/griglie/slider/bottoni | osservabile in sessione; stabilità UNK | widget custom | OBS griglia Android |
| Anteprima reattiva | OBS 001 | custom | OBS 001, parità renderer UNK |
| Undo/redo | undo OBS, redo UNK | custom | snapshot/undo OBS 001 |
| Drag/drop layer | UNK | custom plausibile | non implementato |
| Snapshot JSON | stato UI non equivale a export | tramite tool/app | CODE 002 |
| Upload/lock fotografia | UNK nel workflow | API file documentate | fixture neutra, non foto reale |
| Confronto pixel | non garantito | custom | CODE test Pillow 001 |
| GitHub checkpoint | non automatico | tool server custom | esplicito, non eseguito end-to-end |
| Recupero nuova chat | UNK | backend necessario per durabilità | non verificato |
| Android/web/iOS parity | UNK | host-dependent | solo alcuni test Android 001 |
| Autosync modello/JSON/GitHub | NON dimostrata | da implementare | ASSENTE |

## Best practice operative vincolanti per GPT SOCIAL
1. **Ideazione prima delle immagini**: prima dell'approvazione, descrivere concept, palette, tipografia, template, gerarchia e posizione; non generare asset visivi non autorizzati.
2. **Una sola fonte canonica per stato creativo**: JSON schemaVersion, projectId, revision, asset refs/hash, layers con locked/approved, renderer/template version; niente ricostruzione da sola memoria della chat.
3. **Esplicitare quattro stati**: scelta locale UI; stato comunicato al modello; JSON esportato/verificato; commit GitHub riletto. Non chiamarli tutti «salvato».
4. **Revisioni monotone e conflitti**: expectedRevision + hash baseline, rifiuto stale/no-op e modifiche fuori scope; per multiwriter confrontare anche SHA GitHub prima di scrivere.
5. **Lock asset reale**: registrare hash dei bytes originali, URI immutabile e controllo pixel; non confondere hash di una fixture generata con identità della fotografia caricata.
6. **Rendering riproducibile**: Pillow/versione e font fissati; test differenza circoscritta e hash; preview browser e PNG Pillow vanno confrontati separatamente.
7. **Mobile first, ma senza assunzioni**: target touch sufficienti, controllo undo esplicito, feedback sul salvataggio, test refresh/reopen e fallback per controlli non supportati.
8. **Errore visibile**: se manca tool, stato o checkpoint, bloccare l'azione e dire esattamente quale verifica manca; mai inventare un PASS.
9. **Privacy e sicurezza**: minimizzare dati in structuredContent e log; autorizzare tool e repository writes; no credenziali nel JSON; controllare accesso e scope dei file.
10. **Progressive enhancement**: prototipo B chat-native + JSON + Pillow + GitHub; passare ad Apps SDK/MCP solo per requisito misurato che B non soddisfa.

## Protocollo di regressione proposto
T1 colore e undo; T2 refresh senza perdita silenziosa; T3 export JSON esatto; T4 stale revision; T5 hash asset; T6 diff Pillow solo nella regione accent; T7 checkpoint GitHub con readback SHA; T8 nuova chat recupera da SHA senza cronologia; T9 Android/web/iOS se disponibili. Ogni test richiede ambiente, data, versione, input, output, SHA, risultato PASS/FAIL/BLOCKED. Test UI Android **non autorizzato** in questa fase.

## Decisione e gate
Raccomandazione: architettura ibrida B, senza Apps SDK/backend prematuri. PR #6 deve restare draft finché non sono eseguiti i 6 test 001 + 7 test 002 e i comandi CLI export/verify. Non confondere la lettura del codice con esecuzione. Dopo PASS tecnico chiedere autorizzazione distinta per test Android. Nessun merge automatico.

**Prossimo passo unico:** eseguire i test esatti su checkout della PR #6, registrando log e SHA; fermarsi prima di Android.

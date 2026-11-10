## Creative Console 002 — checkpoint tecnico (2026-11-10)

**Base:** main `9c9f929fe385d974707cf282bf18679e8d3c1d5a`. **Perimetro autorizzato:** un branch, una PR, nessuna installazione, nessuna generazione immagini. La fixture neutra e il contratto `schemaVersion=1.0.0` restano invariati.

### Implementazione minima
- `tests/creative-console/roundtrip.py`: CLI `export` e `verify` con JSON canonico, SHA-256 dello stato, dell'asset e del render Pillow; validazione di una transizione `revision N → N+1` in cui cambia esclusivamente `layers[1].fill`.
- `tests/creative-console/test-roundtrip.py`: sette test unitari aggiuntivi (export/import, singola proprietà, revisione obsoleta, asset alterato, modifica estranea, no-op, CLI). I sei test precedenti restano inalterati.
- **Importante:** il pannello Android non è collegato automaticamente alla CLI. L'export dal pannello e il commit GitHub sono operazioni **esplicite**; il checkpoint remoto sarà verificato solo quando sarà stato effettivamente creato e riletto. Non dichiarare sincronizzazione o parità pixel cross-engine.

### Comandi, in ambiente con Pillow già disponibile
```bash
cd tests/creative-console
python test-neutral-render.py
python test-roundtrip.py
python roundtrip.py export --baseline neutral-state.json --expected-revision 1 --fill '#B36A48' --out /tmp/console-002-checkpoint.json
python roundtrip.py verify --baseline neutral-state.json --expected-revision 1 --state /tmp/console-002-checkpoint.json
```

Il file `/tmp/console-002-checkpoint.json` è solo un esempio di export temporaneo: **non** è un checkpoint GitHub e non va committato automaticamente. La verifica di continuità in nuova sessione richiederà un JSON esplicitamente approvato e committato, recuperato tramite SHA.

### Gate e limiti
PASS richiesto: test Python eseguiti con esito registrato, JSON invariato fuori da fill/revision, rifiuto stale/hash alterato, file di codice riletti da GitHub. Gate Android separato: prova su dispositivo dell'export del colore scelto, verifica JSON, salvataggio GitHub esplicito, recupero da nuova chat. **Non anticipare PASS Android né persistenza remota.**

**Prossima azione unica:** eseguire e registrare la suite tecnica; solo successivamente chiedere all'utente la verifica Android.

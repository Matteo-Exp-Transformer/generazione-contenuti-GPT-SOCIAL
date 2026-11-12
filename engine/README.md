# Engine Pillow — ripiego C (riferimento tecnico)

[render.py](render.py) è autonomo: Python ≥3.9, Pillow ≥10.1 già disponibile, nessuna dipendenza dalla repo. Usava lo stato `post.json` della skill pre-v1.0; il Regista v1.0 non lo usa. La procedura conversazionale è stata aggiornata; questo codice resta invariato. `render(post_json, foto)` restituisce PNG bytes, senza scrivere file. Un terzo argomento opzionale salva il PNG fuori da qualsiasi repo Git; non può sovrascrivere foto o stato.

```python
import importlib.util
spec = importlib.util.spec_from_file_location("post_engine", "/mnt/data/render.py")
engine = importlib.util.module_from_spec(spec)
spec.loader.exec_module(engine)
png = engine.render("/mnt/data/post.json", "/mnt/data/foto.png")
# Nella chat ChatGPT, mostrare l'anteprima direttamente:
from IPython.display import Image, display
display(Image(data=png))
```

Caricare engine, stato e foto nella chat; se il renderer o Pillow manca, fermarsi senza installare o simulare anteprime. CLI: `python engine/render.py <post.json> <foto> <PNG-fuori-repo>`; stampa una ricevuta JSON e restituisce exit 0, oppure exit 2 con errore. `engine.photo_sha256(foto)` calcola l'hash dei byte sorgente per `foto.sha256`; `engine.pixel_sha256(png)` confronta i pixel RGB decodificati, indipendentemente da metadati/compressione PNG.

Il crop `[x,y,w,h]` usa i pixel sorgente decodificati, senza rotazione EXIF implicita, deve stare nella foto e avere la proporzione di `formato`. Viene scalato alla tela con Lanczos; nessun crop aggiuntivo. Testi: `font="pillow-default"` oppure un percorso font già locale (relativo a `post.json`), `size` intero positivo e posizione dall'angolo alto sinistro. Nessun ritorno a capo automatico: testo tagliato o valori non decisi sono rifiutati. Il PNG registra versione Pillow/FreeType e hash dei font: la riproducibilità richiede le stesse versioni e gli stessi font.

Unica estensione allo stato minimo: `forme`, lista opzionale di rettangoli `{ "id": "fondo", "tipo": "rettangolo", "pos": [40,60], "size": [1000,160], "colore": "#223344" }`. Ordine dei layer: foto, forme nell'ordine della lista, testi nell'ordine del JSON. Le chiavi sono chiuse a ogni livello; i colori HEX vengono normalizzati in una copia. `bloccati` può includere foto, codici testo/forma, palette e layout presenti; il render non modifica revisioni, storia o approvazioni. Undo significa ricaricare il checkpoint precedente. Il regista consegna `post.json` al Costruttore per il salvataggio in repo a ogni approvazione; nessuna foto viene inserita in repo senza autorizzazione specifica.

Verifica sintetica: `python -m unittest discover -s tests/engine -v`. La fixture, gli stati temporanei e tutti i PNG sono creati nella directory temporanea di sistema; l'engine contiene un solo file Python. Questi test non certificano Android o qualità. TU-01 è chiuso PARTIAL e non va ripetuto; seguire [STATO.md](../STATO.md) e [ROADMAP](../docs/ROADMAP.md).

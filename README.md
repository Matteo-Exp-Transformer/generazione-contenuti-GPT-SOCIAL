# generazione-contenuti-GPT-SOCIAL

In ChatGPT (Android prioritario) l'utente dirige un post social statico sulla propria foto e riceve un PNG pubblicabile.
Canva per livelli ed elementi, fogli Python deterministici per esplorare, decorazioni GPT come livelli separati.
Foto originale mai alterata; budget incrementale €0.

- Stato corrente e prossimo passo: [STATO.md](STATO.md)
- Scope, roadmap, piano e registro esiti: [docs/ROADMAP.md](docs/ROADMAP.md)
- Istruzioni agenti: [AGENTS.md](AGENTS.md) · Decisioni dell'utente: [docs/decisioni.md](docs/decisioni.md)
- Kit campionari: [campionari/](campionari/) ([zip](campionari/kit-campionari-v1.zip)) · Catalogo modelli Canva: [modelli/CATALOGO.md](modelli/CATALOGO.md)
- Skill Regista (v1.0 sospesa, v2 in M3): [skills/post-director/](skills/post-director/SKILL.md)
- Evidenze: [evidence/](evidence/) · Engine Pillow (ripiego C): [engine/](engine/README.md) · Storico: [docs/archivio/](docs/archivio/README.md)

Nei JSON dei campionari `layout` e `combo`, l'opzione `"foto": "foto-prova.jpg"`
carica una foto relativa al JSON (oppure un percorso assoluto). Il kit usa una copia
in memoria con lato lungo massimo 800 px, orientata secondo EXIF, e la ritaglia a
riempimento nei riquadri. L'originale viene solo letto: SHA-256 stampato prima e dopo;
uscita sullo stesso file rifiutata. Senza `foto` resta il riquadro «FOTO».
I fogli restano «SIMULAZIONE». Le foto personali restano fuori dalla repo e dallo ZIP.

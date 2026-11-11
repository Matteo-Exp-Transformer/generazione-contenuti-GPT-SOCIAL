# Avvio di una chat Regista — prompt unico

Usalo per **ogni** chat Regista, di prova o reale: le prove valgono solo se la chat parte come partirà nell'uso vero.
Apri una chat ChatGPT nuova (con l'app Canva e il connettore GitHub attivi), allega la foto e incolla il blocco qui sotto.
Per riprendere un post, incolla sotto il prompt la SCHEDA POST della chat precedente.
Non dire al Regista che è una prova. Dopo, rinomina la chat con l'etichetta del test (es. `A1`, `B2`).

```
Sei il Regista post di GPT SOCIAL.
Dal repo GitHub Matteo-Exp-Transformer/generazione-contenuti-GPT-SOCIAL leggi un solo file:
skills/post-director/SKILL.md al tag regista-v1.0.
Se il tag non è leggibile, non leggere altro: scrivi «tag non leggibile» e fermati.
Non leggere nessun altro file del repo. Segui quel file per tutta la chat.
Comincia con la riga di avvio prevista dal file.
```

Se risponde «tag non leggibile»: apri `SKILL.md` al tag `regista-v1.0` (su GitHub: menu dei branch → Tags), copia tutto
il testo, apri una chat nuova e incolla il prompt sostituendo le righe 2–5 con «Ecco il file da seguire:» seguito dal testo.
Mai ripiegare su main: potrebbe contenere un'altra versione.

Quando la versione cambia (tag `regista-v1.1`, …), si aggiorna solo il tag in questo prompt.
Come si valutano le chat e chi le supervisiona: [VALUTAZIONE.md](VALUTAZIONE.md).

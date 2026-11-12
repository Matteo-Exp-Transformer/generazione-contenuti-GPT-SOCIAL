# Avvio di una chat Regista — prompt unico

Usalo per **ogni** chat Regista, di prova o reale: le prove valgono solo se la chat parte come partirà nell'uso vero.
Apri una chat ChatGPT nuova (con l'app Canva e il connettore GitHub attivi), allega la foto e incolla il blocco qui sotto.
Per riprendere un post, incolla sotto il prompt la SCHEDA POST della chat precedente.
Non dire al Regista che è una prova. Dopo, rinomina la chat con l'etichetta del test (es. `A1`, `B2`).

```
Sei il Regista post di GPT SOCIAL.
Dal repo GitHub Matteo-Exp-Transformer/generazione-contenuti-GPT-SOCIAL, branch main, leggi un solo file:
skills/post-director/SKILL.md. Controlla la riga «version:» in cima: deve essere regista-v1.0.
Se il file non è leggibile o la versione è diversa, non leggere altro: scrivi «versione non leggibile» e fermati.
Non leggere nessun altro file del repo e non scrivere mai nel repo. Segui quel file per tutta la chat.
Comincia con la riga di avvio prevista dal file; in «letto da» scrivi «main (version regista-v1.0)».
```

Se risponde «versione non leggibile»: apri `SKILL.md` su main, controlla `version:`, copia tutto il testo, apri una chat
nuova e incolla il prompt sostituendo le righe 2–5 con «Ecco il file da seguire:» seguito dal testo.

**Versioni (decisione utente 2026-11-12: un solo branch).** La versione in uso è quella scritta in `version:` di SKILL.md su
main. Ogni modifica a SKILL.md cambia `version:` (es. regista-v1.1), passa da una sola PR e aggiorna la riga 3 di questo prompt.
L'ultima copia di ogni versione superata va in `docs/archivio/`. Il resoconto di una chat Regista non si scrive mai nel repo
dalla chat: si incolla al Supervisore o come commento della PR aperta.
Regista v1.0 sospeso dal ripristino del 2026-11-12: sarà sostituito dal Regista v2 (M3 di [ROADMAP](../../docs/ROADMAP.md)). Valutazione v1.0 archiviata: [VALUTAZIONE-regista-v1.0](../../docs/archivio/VALUTAZIONE-regista-v1.0.md).

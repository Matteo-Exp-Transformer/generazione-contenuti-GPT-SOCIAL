"""Campionari deterministici GPT SOCIAL — SIMULAZIONE, non anteprima Canva.

Uso (Python di ChatGPT, dopo aver estratto lo zip del kit):
    python campionario.py spec.json uscita.png
Non apre mai la foto dell'utente: al suo posto disegna un riquadro «FOTO».
Modi in spec.json["modo"]: "font", "palette", "layout", "combo" (vedi esempi/).
"""
import json, os, sys
from PIL import Image, ImageDraw, ImageFont

KIT = os.path.dirname(os.path.abspath(__file__))
FONTS = json.load(open(os.path.join(KIT, "fonts.json"), encoding="utf-8"))
HEAD = "SIMULAZIONE · non è un'anteprima Canva · kit campionari v1"


def font(fam, size, peso=None):
    info = FONTS[fam]
    f = ImageFont.truetype(os.path.join(KIT, "font", info["file"]), size)
    if peso and info.get("variabile"):
        vals = []
        for a in f.get_variation_axes():
            n = a.get("name", b"")
            n = (n.decode() if isinstance(n, bytes) else n).lower()
            vals.append(max(a["minimum"], min(a["maximum"], peso)) if n.startswith(("weight", "wght")) else a["default"])
        f.set_variation_by_axes(vals)
    return f


def fit(d, testo, fam, peso, w_max, size):
    """Riduce il corpo finché il testo sta in w_max (mai fuori dal riquadro)."""
    while size > 10:
        f = font(fam, size, peso)
        if d.textlength(testo, font=f) <= w_max:
            return f
        size -= 2
    return font(fam, 10, peso)


def lum(h):
    c = [int(h.lstrip("#")[i:i + 2], 16) / 255 for i in (0, 2, 4)]
    c = [x / 12.92 if x <= .03928 else ((x + .055) / 1.055) ** 2.4 for x in c]
    return .2126 * c[0] + .7152 * c[1] + .0722 * c[2]


def contrasto(a, b):
    la, lb = sorted((lum(a), lum(b)), reverse=True)
    return (la + .05) / (lb + .05)


def accento(pal, fondo, minimo=3.0):
    """Colore d'accento leggibile sul fondo; se nessuno basta, il più scuro/chiaro."""
    for c in pal[1:-1][::-1]:
        if contrasto(c, fondo) >= minimo:
            return c
    return max(pal, key=lambda c: contrasto(c, fondo))


def wrap(d, testo, fam, peso, w_max, size, righe_max=3, h_max=None, interlinea=1.08):
    f = font(fam, size, peso)
    while size > 10:
        f = font(fam, size, peso)
        parole, righe, cur = testo.split(), [], ""
        for p in parole:
            prova = (cur + " " + p).strip()
            if d.textlength(prova, font=f) <= w_max:
                cur = prova
            else:
                righe.append(cur); cur = p
        righe.append(cur)
        if len(righe) <= righe_max and (h_max is None or len(righe) * size * interlinea <= h_max):
            return f, righe
        size -= 2
    return f, [testo]


def foglio(n, cell_w, cell_h, col, fondo="#FFFFFF"):
    rows = (n + col - 1) // col
    img = Image.new("RGB", (col * cell_w + (col + 1) * 20, rows * (cell_h + 56) + 70), fondo)
    d = ImageDraw.Draw(img)
    d.text((20, 18), HEAD, font=font("DM Sans", 24, 600), fill="#8A2C1D")
    pos = [(20 + (i % col) * (cell_w + 20), 70 + (i // col) * (cell_h + 56)) for i in range(n)]
    return img, d, pos


def etichetta(d, x, y, testo):
    d.text((x, y), testo, font=font("DM Sans", 22, 600), fill="#333333")


# Impaginazioni: riquadri in frazioni della pagina 4:5 (x0, y0, x1, y1)
LAYOUT = {
    "L1 Titolo alto, foto centrale, info in basso": {"foto": (.08, .3, .92, .8), "titolo": (.08, .04, .92, .27), "info": (.08, .82, .92, .96), "fondo": 0},
    "L2 Foto piena, fascia testi in basso": {"foto": (0, 0, 1, 1), "fascia": (0, .66, 1, 1), "titolo": (.07, .68, .93, .87), "info": (.07, .88, .93, .98), "fondo": 0},
    "L3 Foto a sinistra, testi a destra": {"foto": (0, 0, .55, 1), "titolo": (.6, .12, .95, .55), "info": (.6, .62, .95, .9), "fondo": 0},
    "L4 Foto in alto, titolo grande sotto": {"foto": (0, 0, 1, .58), "titolo": (.07, .61, .93, .85), "info": (.07, .87, .93, .97), "fondo": 0},
    "L5 Cornice: foto al centro, testi sopra e sotto": {"cornice": (.04, .04, .96, .96), "foto": (.12, .3, .88, .76), "titolo": (.12, .07, .88, .28), "info": (.12, .78, .88, .92), "fondo": 1},
    "L6 Titolo sulla foto in alto, bollino info": {"foto": (0, 0, 1, 1), "titolo": (.07, .05, .93, .3), "bollino": (.62, .7, .95, .95), "info": (.65, .76, .92, .89), "fondo": 0},
}


def mini_post(d, x, y, w, h, lay, pal, coppia, testi):
    L = LAYOUT[lay]
    box = lambda r: (x + r[0] * w, y + r[1] * h, x + r[2] * w, y + r[3] * h)
    d.rectangle(box((0, 0, 1, 1)), fill=pal[L.get("fondo", 0) % len(pal)])
    if "cornice" in L:
        d.rectangle(box(L["cornice"]), outline=pal[2 % len(pal)], width=max(2, w // 120))
    fx = box(L["foto"])
    d.rectangle(fx, fill="#B9B4AC")
    d.text(((fx[0] + fx[2]) / 2, (fx[1] + fx[3]) / 2), "FOTO", font=font("DM Sans", max(12, w // 14), 700), fill="#6E6A64", anchor="mm")
    if "fascia" in L:
        d.rectangle(box(L["fascia"]), fill=pal[0])
    if "bollino" in L:
        d.ellipse(box(L["bollino"]), fill=pal[1 % len(pal)])
    tit, peso_t, corpo, peso_c = coppia
    t = box(L["titolo"])
    sotto = pal[0] if ("fascia" in L or L["foto"] != (0, 0, 1, 1)) else "#B9B4AC"
    sotto = pal[L.get("fondo", 0) % len(pal)] if "fascia" not in L and L["foto"] != (0, 0, 1, 1) else sotto
    testo_c = max((pal[-1], pal[0]), key=lambda c: contrasto(c, sotto))
    f, righe = wrap(d, testi[0], tit, peso_t, t[2] - t[0], int(h * .085), h_max=t[3] - t[1])
    lh = f.size * 1.08
    for k, r in enumerate(righe):
        d.text((t[0], t[1] + k * lh), r, font=f, fill=testo_c if k == 0 else accento(pal, sotto))
    i = box(L["info"])
    info = " · ".join(testi[1:])
    sotto_i = pal[1 % len(pal)] if "bollino" in L else sotto
    f, righe = wrap(d, info, corpo, peso_c, i[2] - i[0], int(h * .04), righe_max=3, h_max=i[3] - i[1], interlinea=1.25)
    for k, r in enumerate(righe):
        d.text((i[0], i[1] + k * f.size * 1.25), r, font=f, fill=max((pal[-1], pal[0]), key=lambda c: contrasto(c, sotto_i)))


def coppia(c):
    return (c["titolo"], c.get("peso_titolo"), c["corpo"], c.get("peso_corpo"))


def main(spec_path, out):
    s = json.load(open(spec_path, encoding="utf-8"))
    modo, testi = s["modo"], s.get("testi", ["Titolo del post", "Riga info", "Contatto"])
    pal0 = s.get("palette", [{"nome": "neutra", "colori": ["#F3E6CC", "#D5A35C", "#A46C43", "#342E29"]}])
    if modo == "font":
        items = s["coppie"]
        img, d, pos = foglio(len(items), 1040, 330, 1, pal0[0]["colori"][0])
        for (x, y), c in zip(pos, items):
            p = pal0[0]["colori"]
            etichetta(d, x, y, f'{c["codice"]} · {c["titolo"]} {c.get("peso_titolo") or ""} + {c["corpo"]} {c.get("peso_corpo") or ""}')
            f, righe = wrap(d, testi[0], c["titolo"], c.get("peso_titolo"), 1000, 76, righe_max=2)
            for k, r in enumerate(righe):
                d.text((x, y + 40 + k * f.size * 1.1), r, font=f, fill=p[-1] if k == 0 else accento(p, p[0]))
            fi = fit(d, " · ".join(testi[1:]), c["corpo"], c.get("peso_corpo"), 1000, 38)
            d.text((x, y + 230), " · ".join(testi[1:]), font=fi, fill=p[-1])
    elif modo == "palette":
        items = pal0
        img, d, pos = foglio(len(items), 500, 330, 2)
        c = coppia(s.get("coppia", {"titolo": "DM Serif Display", "corpo": "DM Sans", "peso_corpo": 500}))
        for (x, y), p in zip(pos, items):
            col = p["colori"]
            etichetta(d, x, y, f'{p["codice"]} · {p["nome"]}')
            d.rectangle((x, y + 34, x + 500, y + 230), fill=col[0])
            fi = fit(d, testi[0], c[0], c[1], 460, 46)
            d.text((x + 20, y + 60), testi[0], font=fi, fill=col[-1])
            d.text((x + 20, y + 140), " · ".join(testi[1:]), font=fit(d, " · ".join(testi[1:]), c[2], c[3], 460, 26), fill=accento(col, col[0]))
            sw = 500 / len(col)
            for k, h in enumerate(col):
                d.rectangle((x + k * sw, y + 240, x + (k + 1) * sw, y + 300), fill=h)
                d.text((x + k * sw + 4, y + 304), h, font=font("DM Sans", 16, 500), fill="#333333")
    elif modo in ("layout", "combo"):
        items = s["elementi"] if modo == "combo" else [{"codice": f"L{i+1}", "layout": k} for i, k in enumerate(s.get("layout", list(LAYOUT)))]
        img, d, pos = foglio(len(items), 320, 400, 3)
        base = coppia(s.get("coppia", {"titolo": "DM Serif Display", "corpo": "DM Sans", "peso_corpo": 500}))
        for (x, y), it in zip(pos, items):
            p = next((q["colori"] for q in pal0 if q.get("codice") == it.get("palette")), pal0[0]["colori"])
            c = coppia(it["coppia"]) if "coppia" in it else base
            etichetta(d, x, y, it["codice"] + " · " + it["layout"].split(" ")[0])
            mini_post(d, x, y + 34, 320, 400, it["layout"], p, c, testi)
    else:
        raise SystemExit("modo sconosciuto: " + modo)
    img.save(out)
    print(out, img.size)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])

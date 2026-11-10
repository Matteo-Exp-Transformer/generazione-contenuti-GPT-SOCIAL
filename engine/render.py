"""GPT SOCIAL deterministic photo compositor; Python >=3.9 + Pillow >=10.1.

ChatGPT: upload this file, post.json and the photo. Import with importlib.util;
render(post_json_path, photo_path) returns PNG bytes for inline display. Optional
third argument writes the PNG outside any Git repository. CLI:
    python render.py /tmp/post.json /tmp/photo.png /tmp/render-A.png

State uses skills/post-director/SKILL.md. Only extension: optional `forme`, a
list of {id, tipo:"rettangolo", pos:[x,y], size:[w,h], colore:"#RRGGBB"}.
Order: cropped/scaled photo, rectangles in list order, texts in JSON order.
Crop is source-pixel [x,y,w,h], integer and in bounds; its aspect ratio must
equal formato (no implicit crop or distortion). Positions are top-left pixels.
Text uses Pillow multiline_text, anchor="lt", spacing=4, no wrapping; font is
"pillow-default" or a local font path (relative to post.json, otherwise cwd).
Font size must be a positive integer; undecided/missing render fields fail.
Optional decision metadata (palette/layout/bloccati/storia) never adds approval
or unlocks anything: the director supplies approved snapshots, including undo.

foto.sha256 is SHA256 of source FILE bytes, checked before decoding; pixel_sha256
hashes canonical decoded RGB pixels plus dimensions. normalized_state returns
a copy with HEX colors uppercase. PNG text records Pillow version, exact font
identity/hash, photo file/pixel hashes. Determinism requires those same runtime
and font versions; it is not a promise of pixel equality across Pillow upgrades.
All public helpers raise ValueError for invalid inputs/I/O; no state mutation.
No networking, generated assets, font discovery/download or repo dependencies.
"""

import argparse
import copy
import functools
import hashlib
import io
import json
import os
from pathlib import Path
import re
import struct
import tempfile

from PIL import Image, ImageDraw, ImageFont, PngImagePlugin, features, __version__ as PILLOW_VERSION


def _value_errors(function):
    @functools.wraps(function)
    def wrapped(*args, **kwargs):
        try:
            return function(*args, **kwargs)
        except ValueError:
            raise
        except Exception as exc:
            raise ValueError(f"{function.__name__}: {exc}") from exc
    return wrapped


def _keys(value, allowed, required=()):
    if not isinstance(value, dict) or set(value) - set(allowed) or set(required) - set(value):
        raise ValueError("missing or unknown object keys")


def _int(value, minimum=0):
    if type(value) is not int or value < minimum:
        raise ValueError("expected integer in range")
    return value


def _string(value, nonempty=True):
    if not isinstance(value, str) or (nonempty and not value.strip()):
        raise ValueError("expected string")
    return value


def _vector(value, length, minimum=0):
    if not isinstance(value, list) or len(value) != length:
        raise ValueError("invalid coordinate vector")
    return [_int(v, minimum) for v in value]


def _hex(value):
    if not isinstance(value, str) or not re.fullmatch(r"#[0-9A-Fa-f]{6}", value):
        raise ValueError("expected #RRGGBB color")
    return value.upper()


def _unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("duplicate JSON key")
        result[key] = value
    return result


def _load(post):
    if isinstance(post, dict):
        return copy.deepcopy(post), Path.cwd(), None
    path = Path(post).resolve()
    state = json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=_unique_object)
    return state, path.parent, path


@_value_errors
def normalized_state(post):
    """Validate closed schema, normalize colors in a detached state copy."""
    state, _, _ = _load(post)
    _keys(state, {"revision", "formato", "foto", "testi", "palette", "layout",
                  "bloccati", "storia", "forme"}, {"revision", "formato", "foto"})
    _int(state["revision"], 1)
    _keys(state["formato"], {"w", "h"}, {"w", "h"})
    w, h = (_int(state["formato"][k], 1) for k in ("w", "h"))
    if w * h > 40_000_000:
        raise ValueError("canvas too large")
    _keys(state["foto"], {"file", "sha256", "crop"}, {"file", "sha256", "crop"})
    _string(state["foto"]["file"])
    if not isinstance(state["foto"]["sha256"], str) or not re.fullmatch(r"[0-9a-f]{64}", state["foto"]["sha256"]):
        raise ValueError("invalid photo SHA256")
    x, y, cw, ch = _vector(state["foto"]["crop"], 4)
    if not cw or not ch or cw * h != ch * w:
        raise ValueError("crop must have canvas aspect ratio")
    texts = state.get("testi", {})
    if not isinstance(texts, dict):
        raise ValueError("testi must be an object")
    for code, text in texts.items():
        _string(code)
        if code in {"foto", "palette", "layout"}:
            raise ValueError("reserved layer id")
        fields = {"ruolo", "testo", "font", "size", "pos", "colore"}
        _keys(text, fields, fields)
        _string(text["ruolo"])
        _string(text["testo"])
        _string(text["font"])
        _int(text["size"], 1)
        px, py = _vector(text["pos"], 2)
        if px >= w or py >= h:
            raise ValueError("text position outside canvas")
        text["colore"] = _hex(text["colore"])
    palette = state.get("palette", [])
    if not isinstance(palette, list):
        raise ValueError("palette must be a list")
    if "palette" in state:
        state["palette"] = [_hex(color) for color in palette]
    if "layout" in state:
        _string(state["layout"])
    shapes = state.get("forme", [])
    if not isinstance(shapes, list):
        raise ValueError("forme must be a list")
    ids = {"foto", *texts}
    if "palette" in state:
        ids.add("palette")
    if "layout" in state:
        ids.add("layout")
    for shape in shapes:
        fields = {"id", "tipo", "pos", "size", "colore"}
        _keys(shape, fields, fields)
        code = _string(shape["id"])
        if code in ids or code in {"palette", "layout"} or shape["tipo"] != "rettangolo":
            raise ValueError("duplicate id or unsupported shape")
        ids.add(code)
        px, py = _vector(shape["pos"], 2)
        sw, sh = _vector(shape["size"], 2, 1)
        if px + sw > w or py + sh > h:
            raise ValueError("shape outside canvas")
        shape["colore"] = _hex(shape["colore"])
    locks = state.get("bloccati", [])
    if not isinstance(locks, list) or any(not isinstance(v, str) for v in locks):
        raise ValueError("invalid locks")
    if len(set(locks)) != len(locks) or set(locks) - ids:
        raise ValueError("duplicate or unknown locked id")
    history = state.get("storia", [])
    if not isinstance(history, list):
        raise ValueError("invalid history")
    for item in history:
        _keys(item, {"rev", "modifica"}, {"rev", "modifica"})
        if _int(item["rev"], 1) > state["revision"]:
            raise ValueError("history revision exceeds state")
        _string(item["modifica"])
    return state


def _pixel_hash(image):
    rgb = image.convert("RGB")
    return hashlib.sha256(b"RGB\0" + struct.pack(">II", *rgb.size) + rgb.tobytes()).hexdigest()


@_value_errors
def photo_sha256(photo):
    """Hash original photo file bytes (the foto.sha256 contract)."""
    return hashlib.sha256(Path(photo).read_bytes()).hexdigest()


@_value_errors
def pixel_sha256(png_or_path):
    """Hash decoded RGB pixels/dimensions; PNG compression/metadata are irrelevant."""
    source = io.BytesIO(png_or_path) if isinstance(png_or_path, bytes) else Path(png_or_path)
    with Image.open(source) as image:
        return _pixel_hash(image)


def _font(text, base):
    size = text["size"]
    if text["font"] == "pillow-default":
        font = ImageFont.load_default(size=size)
        return font, {"font": "pillow-default", "size": size, "pillow": PILLOW_VERSION,
                      "sha256": hashlib.sha256(font.font_bytes).hexdigest()}
    path = Path(text["font"])
    if not path.is_absolute():
        path = base / path
    data = path.read_bytes()
    font = ImageFont.truetype(io.BytesIO(data), size=size)
    return font, {"font": path.name, "size": size, "sha256": hashlib.sha256(data).hexdigest(),
                  "pillow": PILLOW_VERSION}


def _output_path(output, protected):
    path = Path(output).resolve()
    if path.suffix.lower() != ".png" or path in protected:
        raise ValueError("output must be a separate PNG")
    if any((parent / ".git").exists() for parent in [path.parent, *path.parent.parents]):
        raise ValueError("render output must be outside any Git repository")
    if not path.parent.is_dir():
        raise ValueError("output parent does not exist")
    return path


@_value_errors
def render(post, photo, output=None):
    """Render an immutable post snapshot and photo to PNG bytes; optionally save."""
    raw, base, post_path = _load(post)
    state = normalized_state(raw)
    photo_path = Path(photo).resolve()
    destination = _output_path(output, {photo_path, post_path}) if output is not None else None
    source = photo_path.read_bytes()
    if hashlib.sha256(source).hexdigest() != state["foto"]["sha256"]:
        raise ValueError("photo source hash mismatch")
    # Decode exactly the bytes that passed the hash check, without reopening.
    with Image.open(io.BytesIO(source)) as opened:
        if getattr(opened, "n_frames", 1) != 1:
            raise ValueError("animated photos are unsupported")
        image = opened.convert("RGB")
    photo_pixels = _pixel_hash(image)
    x, y, cw, ch = state["foto"]["crop"]
    if x + cw > image.width or y + ch > image.height:
        raise ValueError("crop outside photo")
    w, h = state["formato"]["w"], state["formato"]["h"]
    canvas = image.crop((x, y, x + cw, y + ch)).resize((w, h), Image.Resampling.LANCZOS)
    draw = ImageDraw.Draw(canvas)
    for shape in state.get("forme", []):
        sx, sy = shape["pos"]
        sw, sh = shape["size"]
        draw.rectangle((sx, sy, sx + sw - 1, sy + sh - 1), fill=shape["colore"])
    font_info = {}
    for code, text in state.get("testi", {}).items():
        font, identity = _font(text, base)
        position = tuple(text["pos"])
        bounds = draw.multiline_textbbox(position, text["testo"], font=font, anchor="lt", spacing=4)
        if bounds[0] < 0 or bounds[1] < 0 or bounds[2] > w or bounds[3] > h:
            raise ValueError("text would be clipped; choose position/size explicitly")
        draw.multiline_text(position, text["testo"], font=font, fill=text["colore"],
                            anchor="lt", spacing=4)
        font_info[code] = identity
    metadata = {"renderer": "gpt-social-pillow-v1", "pillow": PILLOW_VERSION,
                "freetype": features.version_module("freetype2"),
                "fonts": font_info, "photo_sha256": state["foto"]["sha256"],
                "photo_pixel_sha256": photo_pixels}
    info = PngImagePlugin.PngInfo()
    info.add_text("gpt-social", json.dumps(metadata, ensure_ascii=True, sort_keys=True))
    buffer = io.BytesIO()
    canvas.save(buffer, format="PNG", pnginfo=info)
    result = buffer.getvalue()
    if destination is not None:
        temporary = None
        try:
            fd, temporary = tempfile.mkstemp(prefix=".gpt-social-", dir=destination.parent)
            with os.fdopen(fd, "wb") as handle:
                handle.write(result)
            os.replace(temporary, destination)
        finally:
            if temporary is not None and Path(temporary).exists():
                Path(temporary).unlink()
    return result


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("post")
    parser.add_argument("photo")
    parser.add_argument("output")
    args = parser.parse_args(argv)
    try:
        png = render(args.post, args.photo, args.output)
        with Image.open(io.BytesIO(png)) as image:
            receipt = json.loads(image.info["gpt-social"])
        receipt.update(output=str(Path(args.output).resolve()), pixel_sha256=pixel_sha256(png))
        print(json.dumps(receipt, sort_keys=True))
        return 0
    except ValueError as exc:
        print(json.dumps({"error": str(exc)}))
        return 2


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Create a static Kono Radio avatar from the provided 1536×1024 design sheet.

Usage:
    python -m pip install Pillow
    python tools/make_kono_character.py /path/to/reference.png
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter, ImageOps

def render(source: Path, out: Path) -> None:
    sheet = Image.open(source).convert("RGB")
    if sheet.width < 1000 or sheet.height < 700:
        raise ValueError("Use the original large multi-view character sheet")
    bounds = tuple(round(v * s) for v, s in zip((7, 6, 483, 605), (sheet.width/1536, sheet.height/1024, sheet.width/1536, sheet.height/1024)))
    art = sheet.crop(bounds)
    width, height = 896, 768
    background = ImageOps.fit(art, (width, height), method=Image.Resampling.LANCZOS, centering=(0.53, 0.32))
    background = background.filter(ImageFilter.GaussianBlur(35)).convert("RGBA")
    background = Image.alpha_composite(background, Image.new("RGBA", (width, height), (18, 26, 55, 105)))
    portrait = ImageOps.contain(art, (width-24, height), method=Image.Resampling.LANCZOS)
    mask = Image.new("L", portrait.size, 255)
    draw = ImageDraw.Draw(mask)
    for edge in range(18):
        alpha = round(255*(edge+1)/19)
        draw.line(((edge, 0), (edge, portrait.height)), fill=alpha)
        draw.line(((portrait.width-1-edge, 0), (portrait.width-1-edge, portrait.height)), fill=alpha)
    background.paste(portrait, ((width-portrait.width)//2, (height-portrait.height)//2), mask.filter(ImageFilter.GaussianBlur(1)))
    out.mkdir(parents=True, exist_ok=True)
    background.convert("RGB").save(out/"base.jpg", quality=93, optimize=True, subsampling=0)
    char = {
        "format": "myradio/character-1", "type": "sprites", "size": [width, height],
        "background": "#161a26", "base": "base.jpg",
        "parts": {}, "mouth": {}, "eye": {}, "expressions": {},
        "note": "参考設定画を基に制作した静止画。口パクとまばたきの差分は未実装。"
    }
    (out/"character.json").write_text(json.dumps(char, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    print("Created", out/"base.jpg", "and", out/"character.json")

if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("reference_image", type=Path)
    ap.add_argument("--out", type=Path, default=Path("character"))
    args = ap.parse_args()
    render(args.reference_image, args.out)

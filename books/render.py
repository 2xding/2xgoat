"""Render TikTok photo-mode slideshows (1080x1920 PNGs) from posts.json.

Usage:
    python3 books/render.py            # render every post
    python3 books/render.py money-before-20   # render one post by id

Output: books/out/<post-id>/01.png, 02.png, ...
"""
import json
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

W, H = 1080, 1920
MARGIN = 110
ROOT = Path(__file__).parent
FONTS = Path("/usr/share/fonts/truetype")

STYLES = {
    # cream paper, serif: calm "book journal" look
    "paper": {"bg": "#F4EFE6", "fg": "#1F1B16", "accent": "#B4532A",
              "head": "dejavu/DejaVuSerif-Bold.ttf", "body": "dejavu/DejaVuSerif.ttf"},
    # near-black, white sans: high contrast for hooks
    "dark": {"bg": "#111214", "fg": "#F2F2F2", "accent": "#E8B84A",
             "head": "liberation/LiberationSans-Bold.ttf", "body": "liberation/LiberationSans-Regular.ttf"},
    # deep green, cream text: "money" feel
    "green": {"bg": "#16352B", "fg": "#F1EAD8", "accent": "#9BD18B",
              "head": "liberation/LiberationSerif-Bold.ttf", "body": "liberation/LiberationSerif-Regular.ttf"},
}


def font(path, size):
    return ImageFont.truetype(str(FONTS / path), size)


def wrap(draw, text, fnt, max_w):
    lines = []
    for para in text.split("\n"):
        words, line = para.split(), ""
        for word in words:
            trial = f"{line} {word}".strip()
            if draw.textlength(trial, font=fnt) <= max_w:
                line = trial
            else:
                lines.append(line)
                line = word
        lines.append(line)
    return lines


def block(draw, text, fnt, fill, y, gap):
    for line in wrap(draw, text, fnt, W - 2 * MARGIN):
        draw.text((MARGIN, y), line, font=fnt, fill=fill)
        y += fnt.size + gap
    return y


def render_slide(slide, style, index, total, handle):
    s = STYLES[style]
    img = Image.new("RGB", (W, H), s["bg"])
    d = ImageDraw.Draw(img)
    is_cover = index == 0

    head = font(s["head"], 104 if is_cover else 76)
    body = font(s["body"], 50)
    small = font(s["body"], 36)

    # measure to vertically centre the text block
    head_lines = wrap(d, slide.get("title", ""), head, W - 2 * MARGIN)
    body_lines = wrap(d, slide.get("body", ""), body, W - 2 * MARGIN) if slide.get("body") else []
    block_h = len(head_lines) * (head.size + 18) + (60 if body_lines else 0) + len(body_lines) * (body.size + 16)
    y = max(260, (H - block_h) // 2 - 80)

    if slide.get("kicker"):
        d.text((MARGIN, y - 90), slide["kicker"].upper(), font=small, fill=s["accent"])
    y = block(d, slide.get("title", ""), head, s["fg"], y, 18)
    if body_lines:
        d.rectangle([MARGIN, y + 20, MARGIN + 120, y + 28], fill=s["accent"])
        block(d, slide["body"], body, s["fg"], y + 70, 16)

    d.text((MARGIN, H - 170), handle, font=small, fill=s["accent"])
    if not is_cover:
        d.text((W - MARGIN - 90, H - 170), f"{index + 1}/{total}", font=small, fill=s["fg"])
    return img


def main():
    data = json.loads((ROOT / "posts.json").read_text())
    only = sys.argv[1] if len(sys.argv) > 1 else None
    for post in data["posts"]:
        if only and post["id"] != only:
            continue
        out = ROOT / "out" / post["id"]
        out.mkdir(parents=True, exist_ok=True)
        slides = post["slides"]
        for i, slide in enumerate(slides):
            render_slide(slide, post["style"], i, len(slides), data["handle"]).save(out / f"{i + 1:02d}.png")
        print(f"{post['id']}: {len(slides)} slides -> {out}")


if __name__ == "__main__":
    main()

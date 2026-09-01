"""Shrink everything in backgrounds/ to a Zoom-ready size, and fix guests.js.

    pip install pillow
    python3 tools/optimize_backgrounds.py

A Zoom background never needs to be more than 1920x1080. Images straight out of
a camera or an AI generator are often 3-6x that and stored as PNG, which makes
them 5-15 MB each -- too big to upload to GitHub comfortably, and slow to open
on a phone. This rescales them and re-saves as JPEG, which typically takes each
file from megabytes to a few hundred kilobytes with no visible difference.

Filenames that change from .png to .jpg are updated inside guests.js too, so
nothing needs editing by hand. Safe to re-run: already-small files are skipped.
"""
import os
import re
import sys

from PIL import Image

MAX_W, MAX_H = 1920, 1080
QUALITY = 86
SKIP_UNDER = 500 * 1024          # already small enough to leave alone
THUMB_W = 160                    # the little swatches in the name list
THUMB_QUALITY = 78
SRC_DIR = "backgrounds"
THUMB_DIR = "backgrounds/thumbs"
GUESTS = "guests.js"
EXTS = (".png", ".jpg", ".jpeg", ".webp", ".bmp", ".tif", ".tiff")


def human(n):
    return f"{n/1024/1024:.1f} MB" if n >= 1024 * 1024 else f"{n/1024:.0f} KB"


def write_thumb(im, fname):
    """Small square-ish crop for the picker list, so opening the page doesn't
    pull down every full-size background at once."""
    stem = os.path.splitext(fname)[0]
    t = im.convert("RGB").copy()
    t.thumbnail((THUMB_W, THUMB_W), Image.LANCZOS)
    t.save(os.path.join(THUMB_DIR, stem + ".jpg"),
           "JPEG", quality=THUMB_QUALITY, optimize=True)
    return 1


def main():
    if not os.path.isdir(SRC_DIR):
        sys.exit(f"No {SRC_DIR}/ directory here. Run this from the repo root.")

    files = sorted(f for f in os.listdir(SRC_DIR) if f.lower().endswith(EXTS))
    if not files:
        sys.exit(f"No images found in {SRC_DIR}/.")

    os.makedirs(THUMB_DIR, exist_ok=True)
    renames, before_total, after_total, odd_shape = {}, 0, 0, []
    thumbs = 0

    for fname in files:
        path = os.path.join(SRC_DIR, fname)
        before = os.path.getsize(path)
        before_total += before

        with Image.open(path) as im:
            w, h = im.size
            small_enough = before < SKIP_UNDER and w <= MAX_W and h <= MAX_H
            if small_enough:
                print(f"  skip    {fname}  ({human(before)}, {w}x{h})")
                after_total += before
                thumbs += write_thumb(im, fname)
                continue

            # Flag anything far from 16:9 -- Zoom will letterbox or crop it.
            if abs((w / h) - (16 / 9)) > 0.12:
                odd_shape.append(f"{fname} ({w}x{h})")

            im = im.convert("RGB")
            im.thumbnail((MAX_W, MAX_H), Image.LANCZOS)
            new_w, new_h = im.size

            stem = os.path.splitext(fname)[0]
            new_name = stem + ".jpg"
            new_path = os.path.join(SRC_DIR, new_name)
            im.save(new_path, "JPEG", quality=QUALITY, optimize=True, progressive=True)
            thumbs += write_thumb(im, new_name)

        if new_name != fname:
            os.remove(path)
            renames[f"{SRC_DIR}/{fname}"] = f"{SRC_DIR}/{new_name}"

        after = os.path.getsize(new_path)
        after_total += after
        print(f"  shrank  {fname}  {human(before)} -> {human(after)}"
              f"  ({w}x{h} -> {new_w}x{new_h})")

    print(f"\nTotal: {human(before_total)} -> {human(after_total)}")
    print(f"Wrote {thumbs} thumbnail(s) to {THUMB_DIR}/ "
          f"(the name list loads these instead of the full images).")

    if renames and os.path.exists(GUESTS):
        text = original = open(GUESTS, encoding="utf-8").read()
        for old, new in renames.items():
            text = text.replace(old, new)
        if text != original:
            open(GUESTS, "w", encoding="utf-8").write(text)
            print(f"Updated {len(renames)} filename(s) in {GUESTS}.")

        # Anything renamed but never mentioned in guests.js still needs listing.
        unlisted = [n for n in renames.values() if n not in text]
        if unlisted:
            print("\nNot yet listed in guests.js -- add these to BACKGROUNDS:")
            for n in sorted(unlisted):
                print(f'  "{n}",')

    if odd_shape:
        print("\nNot 16:9, so Zoom will crop or letterbox them:")
        for o in odd_shape:
            print(f"  {o}")


if __name__ == "__main__":
    main()

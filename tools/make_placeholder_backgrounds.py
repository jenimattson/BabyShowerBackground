"""Generate soft pastel 1920x1080 placeholder Zoom backgrounds.

Run:  python3 tools/make_placeholder_backgrounds.py
Writes backgrounds/01-*.png ... 12-*.png

These are placeholders. Replace any file in backgrounds/ with a real image
(same filename) and the site picks it up with no other changes.
"""
import math
import random
from PIL import Image, ImageDraw, ImageFilter

W, H = 1920, 1080

# name, top color, bottom color, accent color, motif
PALETTES = [
    # Cream paper and alpine ink, to sit alongside the illustrated backgrounds.
    # Kept deliberately spread across light/dark so the little swatches in the
    # name list still read as twelve different backgrounds at 34px.
    ("frost-cream",      (222, 235, 246), (252, 248, 239), (108, 146, 184), "clouds"),
    ("alpine-dusk",      (180, 200, 226), (240, 236, 226), (58,  92,  138), "waves"),
    ("snowfall-ivory",   (248, 244, 234), (233, 239, 245), (150, 172, 198), "dots"),
    ("glacier-slate",    (188, 212, 227), (246, 241, 230), (58, 104, 138),  "arches"),
    ("powder-linen",     (236, 242, 250), (250, 242, 228), (120, 152, 190), "confetti"),
    ("pine-mist",        (204, 224, 222), (244, 242, 232), (66, 112, 108),  "bubbles"),
    ("dawn-summit",      (248, 232, 220), (214, 226, 242), (176, 150, 156), "clouds"),
    ("indigo-drift",     (196, 208, 236), (247, 243, 233), (48,  72,  132), "stars"),
    ("birch-blue",       (232, 240, 244), (246, 236, 220), (92, 128, 154),  "waves"),
    ("cobalt-cream",     (176, 198, 232), (250, 246, 236), (32,  70,  128), "dots"),
    ("stonewash-oat",    (214, 222, 228), (246, 238, 222), (86, 112, 138),  "arches"),
    ("midnight-flurry",  (166, 188, 220), (228, 234, 242), (28,  50,  98),  "confetti"),
]


def gradient(top, bottom):
    """Vertical gradient, built small then upscaled (fast + perfectly smooth)."""
    small = Image.new("RGB", (1, H))
    px = small.load()
    for y in range(H):
        t = y / (H - 1)
        px[0, y] = tuple(round(top[i] + (bottom[i] - top[i]) * t) for i in range(3))
    return small.resize((W, H), Image.BICUBIC)


def soft_layer():
    return Image.new("RGBA", (W, H), (0, 0, 0, 0))


def edge_points(rng, n, margin=340):
    """Points biased toward the edges: the center is where a face goes."""
    pts = []
    while len(pts) < n:
        x = rng.randint(-80, W + 80)
        y = rng.randint(-80, H + 80)
        # distance from center, normalised
        dx = (x - W / 2) / (W / 2)
        dy = (y - H / 2) / (H / 2)
        if math.hypot(dx, dy) < 0.55:
            continue  # too close to the middle, skip
        pts.append((x, y))
    return pts


def draw_motif(layer, motif, accent, rng):
    d = ImageDraw.Draw(layer)
    a = accent

    if motif == "dots":
        for (x, y) in edge_points(rng, 90):
            r = rng.randint(6, 22)
            d.ellipse([x - r, y - r, x + r, y + r], fill=a + (rng.randint(60, 130),))

    elif motif == "bubbles":
        for (x, y) in edge_points(rng, 34):
            r = rng.randint(40, 140)
            d.ellipse([x - r, y - r, x + r, y + r], outline=a + (110,), width=rng.randint(3, 7))

    elif motif == "confetti":
        for (x, y) in edge_points(rng, 70):
            w, h = rng.randint(10, 20), rng.randint(24, 46)
            piece = Image.new("RGBA", (w, h), a + (rng.randint(90, 160),))
            piece = piece.rotate(rng.randint(0, 180), expand=True, resample=Image.BICUBIC)
            layer.alpha_composite(piece, (x, y))

    elif motif == "clouds":
        for (x, y) in edge_points(rng, 16):
            base = rng.randint(150, 300)
            for k in range(5):
                r = base * rng.uniform(0.35, 0.6)
                cx = x + (k - 2) * base * 0.28
                cy = y + rng.randint(-30, 30)
                d.ellipse([cx - r, cy - r * 0.8, cx + r, cy + r * 0.8],
                          fill=(255, 255, 255, 130))

    elif motif == "stars":
        for (x, y) in edge_points(rng, 55):
            r = rng.randint(8, 26)
            pts = []
            for i in range(10):
                ang = math.pi / 2 + i * math.pi / 5
                rad = r if i % 2 == 0 else r * 0.42
                pts.append((x + rad * math.cos(ang), y - rad * math.sin(ang)))
            d.polygon(pts, fill=a + (rng.randint(90, 150),))

    elif motif == "waves":
        for i in range(7):
            y0 = H * 0.55 + i * 62
            amp = 26 + i * 5
            pts = [(x, y0 + amp * math.sin(x / 210 + i * 0.7)) for x in range(-40, W + 40, 14)]
            d.line(pts, fill=a + (95,), width=7, joint="curve")

    elif motif == "arches":
        for i, x in enumerate((-90, 210, W - 320, W - 20)):
            w = rng.randint(300, 430)
            top = rng.randint(120, 300)
            d.rounded_rectangle([x, top, x + w, H + 120], radius=w // 2,
                                outline=a + (120,), width=9)


def vignette():
    v = Image.new("L", (W, H), 0)
    ImageDraw.Draw(v).ellipse([-W * 0.25, -H * 0.35, W * 1.25, H * 1.35], fill=90)
    return v.filter(ImageFilter.GaussianBlur(200))


def build(index, name, top, bottom, accent, motif):
    rng = random.Random(index * 7919)
    img = gradient(top, bottom).convert("RGBA")

    # big diffuse glow blobs for depth
    glow = soft_layer()
    gd = ImageDraw.Draw(glow)
    for (x, y) in edge_points(rng, 5, margin=0):
        r = rng.randint(320, 560)
        gd.ellipse([x - r, y - r, x + r, y + r], fill=accent + (55,))
    img.alpha_composite(glow.filter(ImageFilter.GaussianBlur(150)))

    shapes = soft_layer()
    draw_motif(shapes, motif, accent, rng)
    img.alpha_composite(shapes.filter(ImageFilter.GaussianBlur(2)))

    # lift the centre so faces read clearly
    center = soft_layer()
    ImageDraw.Draw(center).ellipse([W * 0.18, -H * 0.2, W * 0.82, H * 1.05],
                                   fill=(255, 255, 255, 42))
    img.alpha_composite(center.filter(ImageFilter.GaussianBlur(180)))

    out = img.convert("RGB")
    out.putalpha(255)
    out = out.convert("RGB")
    path = f"backgrounds/{index:02d}-{name}.png"
    out.save(path, "PNG", optimize=True)
    print(f"  {path}")
    return path


if __name__ == "__main__":
    print("Generating placeholder backgrounds:")
    for i, (name, top, bottom, accent, motif) in enumerate(PALETTES, start=1):
        build(i, name, top, bottom, accent, motif)
    print("Done.")

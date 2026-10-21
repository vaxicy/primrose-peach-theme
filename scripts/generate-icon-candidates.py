"""Primrose Peach Theme - icon candidates.

Code-drawn marks, a light/dark contact sheet and an inline strip.

Run from the project root:  py -3 scripts/generate-icon-candidates.py
"""

import io
import math
import os

from PIL import Image, ImageDraw, ImageFont

S = 3
W = 1024

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "assets", "logo-candidates")

PEACH = (252, 214, 180, 255)      # #FCD6B4
PEACH_D = (232, 145, 111, 255)    # #E8916F
PINK = (255, 172, 189, 255)       # #FFACBD
PINK_D = (232, 117, 140, 255)     # #E8758C
GREEN = (177, 210, 155, 255)      # #B1D29B
GREEN_D = (127, 168, 95, 255)     # #7FA85F
CYAN = (211, 244, 243, 255)       # #D3F4F3
CYAN_D = (111, 191, 187, 255)     # #6FBFBB
YELLOW = (232, 200, 106, 255)     # #E8C86A
PALE_Y = (251, 243, 192, 255)     # #FBF3C0
CREAM = (255, 255, 255, 255)

LIGHT_BG = (250, 246, 242, 255)
DARK_BG = (31, 42, 38, 255)
LIGHT_INK = (70, 48, 40, 255)
DARK_INK = (238, 226, 214, 255)

FONT_DIR = r"C:\Windows\Fonts"


def font(name, size):
    try:
        return ImageFont.truetype(os.path.join(FONT_DIR, name), size)
    except Exception:
        return ImageFont.load_default()


def scr(p):
    return (p[0] * S, p[1] * S)


def wd(v):
    return max(1, int(round(v * S)))


def canvas():
    return Image.new("RGBA", (W * S, W * S), (0, 0, 0, 0))


def finish(img):
    return img.resize((W, W), Image.LANCZOS)


def bez(p0, p1, p2, n=64):
    pts = []
    for i in range(n + 1):
        t = i / n
        u = 1.0 - t
        pts.append((u * u * p0[0] + 2 * u * t * p1[0] + t * t * p2[0],
                    u * u * p0[1] + 2 * u * t * p1[1] + t * t * p2[1]))
    return pts


def leaf_poly(base, tip, width, bend=0.0, n=64):
    bx, by = base
    tx, ty = tip
    dx, dy = tx - bx, ty - by
    length = math.hypot(dx, dy)
    nx, ny = -dy / length, dx / length
    cx = (bx + tx) / 2 + nx * bend
    cy = (by + ty) / 2 + ny * bend
    side_a = bez(base, (cx + nx * width, cy + ny * width), tip, n)
    side_b = bez(tip, (cx - nx * width, cy - ny * width), base, n)
    return side_a + side_b[1:]


def poly(draw, pts, fill):
    draw.polygon([scr(p) for p in pts], fill=fill)


def disc(draw, center, r, fill):
    draw.ellipse([center[0] * S - r * S, center[1] * S - r * S,
                  center[0] * S + r * S, center[1] * S + r * S], fill=fill)


def ring(draw, center, r, width, fill):
    draw.ellipse([center[0] * S - r * S, center[1] * S - r * S,
                  center[0] * S + r * S, center[1] * S + r * S],
                 outline=fill, width=wd(width))


def flower(draw, center, radius, petal, core, petals=5, phase=-math.pi / 2):
    for i in range(petals):
        ang = phase + i * 2 * math.pi / petals
        disc(draw, (center[0] + math.cos(ang) * radius * 0.52,
                    center[1] + math.sin(ang) * radius * 0.52),
             radius * 0.46, petal)
    disc(draw, center, radius * 0.34, core)


# ---------------------------------------------------------------- candidates

def cand_peach():
    img = canvas()
    d = ImageDraw.Draw(img)

    d.ellipse([scr((286, 320)), scr((738, 792))], fill=PEACH_D)
    # crease
    crease = bez((512, 350), (470, 560), (512, 776))
    d.line([scr(p) for p in crease], fill=PEACH, width=wd(18), joint="curve")

    # leaf and stalk
    poly(d, leaf_poly((524, 336), (712, 244), 74, 24), GREEN_D)
    poly(d, leaf_poly((500, 330), (398, 222), 64, -20), GREEN)

    return finish(img)


def cand_primrose_cluster():
    img = canvas()
    d = ImageDraw.Draw(img)

    # stems
    for start, end in (((380, 400), (452, 812)), ((656, 336), (528, 806)),
                       ((592, 664), (516, 812))):
        d.line([scr(start), scr(end)], fill=GREEN_D, width=wd(20), joint="curve")

    flower(d, (380, 380), 176, PINK_D, YELLOW)
    flower(d, (664, 306), 142, PINK, YELLOW)
    flower(d, (596, 648), 122, PINK_D, YELLOW)

    return finish(img)


def cand_blossom_branch():
    img = canvas()
    d = ImageDraw.Draw(img)

    branch = bez((280, 852), (500, 560), (760, 300))
    d.line([scr(p) for p in branch], fill=GREEN_D, width=wd(26), joint="curve")
    poly(d, leaf_poly((470, 596), (316, 520), 76, 20), GREEN)
    poly(d, leaf_poly((612, 430), (742, 486), 68, -18), GREEN)

    for c, r, col in (((700, 296), 128, PINK_D), ((520, 512), 104, PINK),
                      ((392, 720), 88, PINK_D)):
        flower(d, c, r, col, YELLOW, petals=4, phase=-math.pi / 2)

    return finish(img)


def cand_peach_slice():
    img = canvas()
    d = ImageDraw.Draw(img)

    # half peach, flat side down (circle centre at y=724, radius 232)
    # skin, flesh, pit
    d.pieslice([scr((280, 392)), scr((744, 856))], 180, 360, fill=PEACH_D)
    d.pieslice([scr((322, 434)), scr((702, 814))], 180, 360, fill=PALE_Y)
    d.ellipse([scr((470, 560)), scr((554, 700))], fill=PINK_D)
    d.ellipse([scr((496, 588)), scr((528, 664))], fill=PINK)

    return finish(img)


def cand_peach_pair():
    img = canvas()
    d = ImageDraw.Draw(img)

    d.ellipse([scr((236, 428)), scr((620, 832))], fill=PEACH_D)
    d.ellipse([scr((548, 306)), scr((852, 626))], fill=PINK_D)
    crease = bez((700, 340), (668, 470), (700, 600))
    d.line([scr(p) for p in crease], fill=PINK, width=wd(14), joint="curve")

    poly(d, leaf_poly((640, 336), (796, 226), 62, 18), GREEN_D)
    poly(d, leaf_poly((392, 456), (330, 322), 58, -16), GREEN)

    return finish(img)


def cand_primrose_bud():
    img = canvas()
    d = ImageDraw.Draw(img)

    # bud
    bud = []
    for i in range(90):
        t = 2 * math.pi * i / 90
        x = 150 * math.cos(t)
        y = 196 * math.sin(t)
        if y > 0:
            y *= 0.9
        bud.append((524 + x, 396 + y))
    poly(d, bud, PINK_D)

    # sepals
    poly(d, leaf_poly((512, 556), (352, 664), 78, -20), GREEN_D)
    poly(d, leaf_poly((536, 556), (700, 654), 78, 20), GREEN_D)

    # stem + leaf
    stem = bez((524, 540), (500, 720), (470, 862))
    d.line([scr(p) for p in stem], fill=GREEN_D, width=wd(26), joint="curve")
    poly(d, leaf_poly((496, 742), (656, 700), 70, 18), GREEN)

    return finish(img)


CANDIDATES = [
    ("01", "peach", cand_peach),
    ("02", "primrose-cluster", cand_primrose_cluster),
    ("03", "blossom-branch", cand_blossom_branch),
    ("04", "peach-slice", cand_peach_slice),
    ("05", "peach-pair", cand_peach_pair),
    ("06", "primrose-bud", cand_primrose_bud),
]


# ---------------------------------------------------------------- sheet bits

def centered_text(d, center, text, fnt, fill):
    b = d.textbbox((0, 0), text, font=fnt)
    x = center[0] - (b[2] - b[0]) / 2 - b[0]
    y = center[1] - (b[3] - b[1]) / 2 - b[1]
    d.text((x, y), text, font=fnt, fill=fill)


def contact_sheet(icons, bg, ink, path):
    cell_w, cell_h = 420, 540
    margin, gap = 40, 26
    head = 118
    sheet_w = margin * 2 + cell_w * 3 + gap * 2
    sheet_h = margin + head + cell_h * 2 + gap + margin

    sheet = Image.new("RGBA", (sheet_w, sheet_h), bg)
    d = ImageDraw.Draw(sheet)

    f_title = font("segoeuib.ttf", 40)
    f_num = font("segoeuib.ttf", 30)
    f_name = font("segoeui.ttf", 26)
    f_small = font("segoeui.ttf", 20)

    centered_text(d, (sheet_w / 2, margin + 34), "PRIMROSE PEACH THEME", f_title, ink)
    centered_text(d, (sheet_w / 2, margin + 82), "icon candidates", f_small, ink)

    for idx, (num, name, icon) in enumerate(icons):
        row, col = divmod(idx, 3)
        gx = margin + col * (cell_w + gap)
        gy = margin + head + row * (cell_h + gap)

        sheet.alpha_composite(icon.resize((260, 260), Image.LANCZOS),
                              (gx + (cell_w - 260) // 2, gy + 30))

        centered_text(d, (gx + cell_w / 2, gy + 330), num, f_num, ink)
        centered_text(d, (gx + cell_w / 2, gy + 372), name, f_name, ink)
        centered_text(d, (gx + cell_w / 2, gy + 404), "1024 x 1024  PNG", f_small, ink)

        thumb = icon.resize((32, 32), Image.LANCZOS)
        tx, ty = gx + cell_w - 32 - 22, gy + cell_h - 32 - 22
        d.rectangle([tx - 10, ty - 10, tx + 42, ty + 42],
                    outline=(ink[0], ink[1], ink[2], 70), width=1)
        sheet.alpha_composite(thumb, (tx, ty))

    save_png(sheet.convert("RGB"), path)


def inline_strip(icons, path):
    size, gap, margin = 150, 18, 30
    strip_w = margin * 2 + size * len(icons) + gap * (len(icons) - 1)
    strip_h = margin * 2 + size + 34
    strip = Image.new("RGBA", (strip_w, strip_h), LIGHT_BG)
    d = ImageDraw.Draw(strip)
    f_num = font("segoeuib.ttf", 20)

    for idx, (num, _name, icon) in enumerate(icons):
        x = margin + idx * (size + gap)
        strip.alpha_composite(icon.resize((size, size), Image.LANCZOS), (x, margin))
        centered_text(d, (x + size / 2, margin + size + 16), num, f_num, LIGHT_INK)

    save_png(strip.convert("RGB"), path)


def save_png(img, path):
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "wb") as fh:
        fh.write(buf.getvalue())


def main():
    os.makedirs(OUT, exist_ok=True)

    icons = []
    for num, name, fn in CANDIDATES:
        icon = fn()
        box = icon.getbbox()
        if box is None:
            raise AssertionError("%s rendered empty" % name)
        left, top, right, bottom = box
        lo, hi = 70, 954
        if left < lo or top < lo or right > hi or bottom > hi:
            raise AssertionError("%s out of safe area: %s" % (name, box))
        path = os.path.join(OUT, "%s-%s.png" % (num, name))
        save_png(icon, path)
        print("wrote", os.path.relpath(path, ROOT), box)
        icons.append((num, name, icon))

    contact_sheet(icons, LIGHT_BG, LIGHT_INK, os.path.join(OUT, "contact-light.png"))
    contact_sheet(icons, DARK_BG, DARK_INK, os.path.join(OUT, "contact-dark.png"))
    inline_strip(icons, os.path.join(OUT, "inline-strip.png"))
    print("wrote contact-light.png / contact-dark.png / inline-strip.png")


if __name__ == "__main__":
    main()

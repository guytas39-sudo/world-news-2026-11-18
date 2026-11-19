#!/usr/bin/env python3
"""Draw the entry image: the world news of Wednesday 18 November 2026 in one picture.

Composed programmatically with Pillow so every word is real, spelled text —
no generated imagery, no garbled lettering. Run:  python3 draw_image.py
Writes entry.png (1024 x 1024) next to this file, deterministically.
"""
from PIL import Image, ImageDraw, ImageFont

W = H = 1024
BG = (247, 244, 238)          # newsprint off-white
INK = (18, 22, 33)            # near-black
PAPER_CARD = (255, 255, 255)
GREY = (92, 98, 110)

FONT_DIR = "/usr/share/fonts/truetype/dejavu"
def font(name, size):
    return ImageFont.truetype(f"{FONT_DIR}/{name}", size)

F_TITLE = font("DejaVuSerif-Bold.ttf", 54)
F_DATE = font("DejaVuSans-Bold.ttf", 47)
F_KICKER = font("DejaVuSans-Bold.ttf", 19)
F_HEAD = font("DejaVuSans-Bold.ttf", 27)
F_BODY = font("DejaVuSans.ttf", 21)
F_TICKER = font("DejaVuSans-Bold.ttf", 20)
F_FOOT = font("DejaVuSans.ttf", 17)

img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)

# ---------- header ----------
d.rectangle([0, 0, W, 148], fill=INK)
d.text((36, 22), "THE WORLD IN ONE DAY", font=F_TITLE, fill=(250, 248, 242))
d.text((36, 88), "Wednesday, 18 November 2026", font=F_DATE, fill=(240, 178, 60))
d.line([0, 148, W, 148], fill=(240, 178, 60), width=5)

# ---------- story cards ----------
# (kicker, accent, headline lines, body lines)
STORIES = [
    ("ASIA · SHENZHEN", (178, 34, 52),
     ["Xi and Putin meet as", "APEC opens in Shenzhen"],
     ["Three-way talks with Trump", "follow on Thursday."]),
    ("ASIA · MANILA", (20, 96, 160),
     ["Quad leaders meet in", "Manila after two years"],
     ["Trump announces a new", "trade deal with Philippines."]),
    ("MIDDLE EAST · GULF", (196, 110, 20),
     ["Iranian drones stopped", "over Kuwait and Bahrain"],
     ["US strikes a missile site on", "Qeshm Island; oil near $93."]),
    ("EUROPE · UKRAINE", (38, 110, 70),
     ["141 drones in one night", "over Ukraine"],
     ["Air defences down 126;", "Dnipro reports six injured."]),
    ("AMERICAS · ALASKA", (110, 60, 150),
     ["Alaska flips a Senate", "seat to the Democrats"],
     ["Peltola beats Sullivan;", "majority projected 56-44."]),
    ("TECHNOLOGY", (30, 130, 140),
     ["Nvidia revenue doubles", "to $115.8 billion"],
     ["Board rules out bringing", "Jensen Huang back as CEO."]),
    ("SOUTH ASIA · WEATHER", (170, 60, 110),
     ["Severe Cyclone Akvan", "bears down on Odisha"],
     ["Evacuations under way;", "landfall expected Friday."]),
    ("CLIMATE · COP31", (70, 130, 50),
     ["COP31 in Turkiye splits", "over fossil-fuel draft"],
     ["Phase-out text divides", "rich and poor nations."]),
]

MARGIN = 28
GAP = 13
COL_W = (W - 2 * MARGIN - GAP) // 2          # 477
TOP = 168
ROW_H = 170
for i, (kicker, accent, head, body) in enumerate(STORIES):
    col, row = i % 2, i // 2
    x0 = MARGIN + col * (COL_W + GAP)
    y0 = TOP + row * (ROW_H + GAP)
    x1, y1 = x0 + COL_W, y0 + ROW_H
    d.rounded_rectangle([x0, y0, x1, y1], radius=14, fill=PAPER_CARD,
                        outline=(214, 209, 198), width=2)
    d.rectangle([x0, y0, x0 + 10, y1], fill=accent)
    tx = x0 + 28
    d.text((tx, y0 + 13), kicker, font=F_KICKER, fill=accent)
    ty = y0 + 42
    for line in head:
        d.text((tx, ty), line, font=F_HEAD, fill=INK)
        ty += 32
    ty += 5
    for line in body:
        d.text((tx, ty), line, font=F_BODY, fill=GREY)
        ty += 25

# ---------- ticker ----------
TY = TOP + 4 * ROW_H + 3 * GAP + 19          # 906
d.rectangle([0, TY, W, TY + 62], fill=(240, 178, 60))
d.text((28, TY + 8), "ALSO TODAY", font=F_TICKER, fill=INK)
d.text((28, TY + 34),
       "WHO: 950,000 displaced people in Gaza on flood-prone ground · Russian military plane crash in Siberia kills 19",
       font=F_FOOT, fill=INK)
d.text((28, TY + 74),
       "One image, drawn by program from the day's reporting (AP, AFP, Al Jazeera, France 24 and others).",
       font=F_FOOT, fill=GREY)

img.save("entry.png", optimize=True)
print("wrote entry.png", img.size)

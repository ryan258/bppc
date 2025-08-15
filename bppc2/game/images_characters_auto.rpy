# images_characters_auto.rpy
# Uses files like images/characters/char02/char02_neutral.png
# Then you can do: show june        / show june angry  (when char02_angry.png exists)

init -10 python:
    import re

    # Map folders -> your script character names
    ALIAS = {
        "char01": "leo",
        "char02": "june",
        "char03": "mina",
        "char04": "kit",
        "char05": "mara",
        "char06": "hub",
    }

    file_re = re.compile(r"images/characters/([^/]+)/\1_([A-Za-z0-9\-]+)\.(png|webp)$", re.I)
    neutral_for = {}

    for f in renpy.list_files():
        m = file_re.match(f)
        if not m:
            continue

        cid = m.group(1)             # char02
        expr = m.group(2).lower()    # neutral, smile, etc.

        # Register base tag (e.g., "char02 smile")
        renpy.image(f"{cid} {expr}", f)
        if expr == "neutral":
            neutral_for[cid] = f

        # Also register the friendly alias (e.g., "june smile")
        alias = ALIAS.get(cid)
        if alias:
            renpy.image(f"{alias} {expr}", f)
            if expr == "neutral":
                neutral_for[alias] = f

    # Default each tag to neutral so `show june` works
    for tag, fn in neutral_for.items():
        renpy.image(tag, fn)

# ---- transforms must be multiline blocks (not inline) ----
transform stage_left:
    xalign 0.20
    yalign 1.0

transform stage_center:
    xalign 0.50
    yalign 1.0

transform stage_right:
    xalign 0.80
    yalign 1.0

transform crisp:
    nearest True
    linear 0.0


# Direct aliases so `show leo/june/...` always work,
# even before any auto-scan magic.
image leo  = "images/characters/char01/char01_neutral.png"
image june = "images/characters/char02/char02_neutral.png"
image mina = "images/characters/char03/char03_neutral.png"
image kit  = "images/characters/char04/char04_neutral.png"
image mara = "images/characters/char05/char05_neutral.png"
image hub  = "images/characters/char06/char06_neutral.png"

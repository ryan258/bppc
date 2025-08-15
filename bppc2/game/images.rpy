# Image definitions for Blue Pencil Poetry Club

# Placeholder backgrounds - these will be replaced with proper art
image bg classroom = "#F5F5DC"  # Beige classroom
image bg black = "#000000"      # Black transition

# Placeholder character sprites - silhouettes for now
image june happy = Solid("#FFB6C1", xsize=200, ysize=400)      # Milkshake Pink silhouette
image june neutral = Solid("#FFB6C1", xsize=200, ysize=400)
image june sad = Solid("#FFB6C1", xsize=200, ysize=400)

image mina neutral = Solid("#2B68C5", xsize=200, ysize=400)    # Pool Blue silhouette  
image mina intense = Solid("#2B68C5", xsize=200, ysize=400)
image mina happy = Solid("#2B68C5", xsize=200, ysize=400)

image kit skeptical = Solid("#800080", xsize=200, ysize=400)   # Purple silhouette
image kit angry = Solid("#800080", xsize=200, ysize=400)
image kit smirk = Solid("#800080", xsize=200, ysize=400)

image mara knowing = Solid("#B8860B", xsize=200, ysize=400)    # Gold silhouette
image mara worried = Solid("#B8860B", xsize=200, ysize=400)
image mara neutral = Solid("#B8860B", xsize=200, ysize=400)

# UI elements for later phases
image blue_pencil = Solid("#2B68C5", xsize=5, ysize=100)      # Editorial marks

# Character positioning transforms
transform center_left:
    xalign 0.25
    yalign 1.0

transform center_right:
    xalign 0.75
    yalign 1.0
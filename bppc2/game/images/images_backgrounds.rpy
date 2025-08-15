# images_backgrounds.rpy

# Background declarations (your current JPEGs)
image bg cafeteria  = "images/backgrounds/cafeteria.jpeg"
image bg classroom  = "images/backgrounds/classroom.jpeg"
image bg empty_room = "images/backgrounds/empty_room.jpeg"
image bg hallway    = "images/backgrounds/hallway.jpeg"
image bg library    = "images/backgrounds/library.jpeg"

# Handy transitions
define tdiss = Dissolve(0.25)
define tfade = Fade(0.35, 0.05, 0.35)

# Optional slight “Ken Burns” movement for static BGs
transform kb_slow:
    anchor (0.5, 0.5)
    pos (0.5, 0.5)
    zoom 1.05
    linear 10.0 zoom 1.0

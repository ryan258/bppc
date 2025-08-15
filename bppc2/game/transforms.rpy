# transforms.rpy

# Typical exported sprite height (adjust if yours differ)
define SPRITE_BASE_H = 1600.0

# Fit a sprite to a fraction of the screen height and anchor to the bottom.
transform sprite_fit(h_frac=0.92):
    yalign 1.0
    zoom (config.screen_height * h_frac) / SPRITE_BASE_H

# Slightly smaller / larger presets
transform sprite_fit_s:
    yalign 1.0
    zoom (config.screen_height * 0.85) / SPRITE_BASE_H

transform sprite_fit_l:
    yalign 1.0
    zoom (config.screen_height * 0.98) / SPRITE_BASE_H

# Stage positions (note: properties on separate lines)
transform stage_left:
    xalign 0.20
    yalign 1.0

transform stage_center:
    xalign 0.50
    yalign 1.0

transform stage_right:
    xalign 0.80
    yalign 1.0

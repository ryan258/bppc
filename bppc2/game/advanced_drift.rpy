# Advanced Drift Effects - Visual Corruption System
# Escalating visual distortion based on meta-pressure

# Drift effect transforms
transform mild_drift:
    xoffset 0
    linear 3.0 xoffset 1
    linear 3.0 xoffset -1
    linear 3.0 xoffset 0
    repeat

transform moderate_drift:
    xoffset 0 yoffset 0
    linear 2.0 xoffset 2 yoffset 1
    linear 2.0 xoffset -2 yoffset -1
    linear 2.0 xoffset 1 yoffset 2
    linear 2.0 xoffset 0 yoffset 0
    repeat

transform severe_drift:
    xoffset 0 yoffset 0 alpha 1.0
    linear 1.0 xoffset 3 yoffset 2 alpha 0.9
    linear 1.0 xoffset -3 yoffset -2 alpha 1.0
    linear 1.0 xoffset 2 yoffset 3 alpha 0.8
    linear 1.0 xoffset 0 yoffset 0 alpha 1.0
    repeat

transform critical_drift:
    xoffset 0 yoffset 0 alpha 1.0 rotate 0
    linear 0.5 xoffset 5 yoffset 3 alpha 0.7 rotate 2
    linear 0.5 xoffset -5 yoffset -3 alpha 1.0 rotate -2
    linear 0.5 xoffset 3 yoffset 5 alpha 0.6 rotate 1
    linear 0.5 xoffset 0 yoffset 0 alpha 1.0 rotate 0
    repeat

# Color misregistration effects
transform color_shift_red:
    matrixcolor TintMatrix("#FF6666")

transform color_shift_blue:
    matrixcolor TintMatrix("#6666FF")

transform color_shift_green:
    matrixcolor TintMatrix("#66FF66")

# Apply drift based on current pressure levels
label apply_drift_effects:
    if not persistent.honest_mode:
        if drift_intensity >= 0.8:
            $ renpy.transition(squares)
            show screen critical_drift_overlay
        elif drift_intensity >= 0.6:
            $ renpy.transition(pixellate)
            show screen severe_drift_overlay
        elif drift_intensity >= 0.4:
            show screen moderate_drift_overlay
        elif drift_intensity >= 0.2:
            show screen mild_drift_overlay
    
    return

# Drift overlay screens
screen mild_drift_overlay():
    frame:
        background Solid("#000000", alpha=0.05)
        at mild_drift
        xfill True
        yfill True

screen moderate_drift_overlay():
    frame:
        background Solid("#2B68C5", alpha=0.1)
        at moderate_drift
        xfill True
        yfill True

screen severe_drift_overlay():
    frame:
        background Solid("#FF0000", alpha=0.15)
        at severe_drift
        xfill True
        yfill True

screen critical_drift_overlay():
    frame:
        background Solid("#800080", alpha=0.2)
        at critical_drift
        xfill True
        yfill True

# Gutter compression effect
transform compressed_gutters:
    xsize config.screen_width * 0.8
    xalign 0.5

# Balloon thinning effect  
transform thin_balloons:
    alpha 0.7
    xsize config.screen_width * 0.9

# Text corruption effects
label corrupt_text_display(text_content):
    # Gradually corrupt text based on pressure
    if editorial_pressure >= 20:
        $ corrupted_text = text_content.replace("e", "3").replace("a", "@")
        "[corrupted_text]"
    elif editorial_pressure >= 15:
        $ corrupted_text = text_content.replace(" ", "_")
        "[corrupted_text]"
    elif editorial_pressure >= 10:
        $ stuttered_text = text_content.replace("th", "th-th")
        "[stuttered_text]"
    else:
        "[text_content]"
    
    return

# Misregistration effect
label apply_misregistration:
    if drift_intensity >= 0.5:
        show layer master at color_shift_red
        pause 0.1
        show layer master at color_shift_blue  
        pause 0.1
        show layer master
    
    return

# Progressive visual breakdown
label visual_breakdown_sequence:
    "The words on the screen begin to..."
    
    call apply_drift_effects
    
    if drift_intensity >= 0.8:
        call corrupt_text_display("sh4k3 4nd tr3mbl3...")
        call apply_misregistration
        "Colors bleed outside their lines."
        "Text stutters and repeats and repeats and—"
    elif drift_intensity >= 0.6:
        call corrupt_text_display("wobble and shift...")
        "The gutters feel tight. Compressed."
        "Like someone is squeezing the life out of the page."
    elif drift_intensity >= 0.4:
        "drift slightly off-center."
        "Nothing dramatic. Just... wrong."
    
    return

# Clean up drift effects
label clear_drift_effects:
    hide screen mild_drift_overlay
    hide screen moderate_drift_overlay  
    hide screen severe_drift_overlay
    hide screen critical_drift_overlay
    $ drift_intensity = 0.0
    return

# Honest Mode override
label honest_mode_drift_check:
    if persistent.honest_mode:
        call clear_drift_effects
        "Drift effects disabled."
    return
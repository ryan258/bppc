# Accessibility options
default persistent.halftone = True
default persistent.reduce_drift = False
default persistent.dyslexia_font = False

screen preferences():
    tag menu
    use navigation
    vbox:
        xalign 0.5
        yalign 0.5
        spacing 20
        text "Accessibility"
        checkbox "Halftone" selected persistent.halftone action SetField(persistent, "halftone", not persistent.halftone)
        checkbox "Reduce Drift" selected persistent.reduce_drift action SetField(persistent, "reduce_drift", not persistent.reduce_drift)
        checkbox "Dyslexia-friendly Font" selected persistent.dyslexia_font action SetField(persistent, "dyslexia_font", not persistent.dyslexia_font)

# Haunted Load
default persistent.haunted_save = False

screen load():
    tag menu
    use navigation
    if persistent.haunted_save and not persistent.honest_mode:
        # Show haunted interstitial
        text "You feel a strange presence..."
        timer 2.0 action ShowMenu("load_actual")
    else:
        use file_slots(_("Load"))

screen load_actual():
    tag menu
    use navigation
    use file_slots(_("Load"))

init -1 python:
    config.keymap['toggle_honest_mode'] = ['K_LSHIFT', 'K_RSHIFT']

label start:
    key 'toggle_honest_mode' action SetField(persistent, "honest_mode", not persistent.honest_mode)
    return

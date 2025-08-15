# Blue Pencil Poetry Club - Screen Definitions
# Quick menu, marginalia, and meta-horror UI elements

# Quick menu that players expect in VNs
screen quick_menu():
    zorder 100
    if quick_menu:
        hbox:
            style_prefix "quick" 
            xalign 0.5 
            yalign 1.0
            spacing 10
            
            textbutton _("Q.Save") action QuickSave()
            textbutton _("Q.Load") action QuickLoad()
            textbutton _("Skip") action Skip()
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Prefs") action ShowMenu("preferences")

# Meta-horror marginalia system
screen marginalia(msg):
    zorder 200
    frame at marginalia_anim:
        xalign 0.9
        yalign 0.1
        background "#2B68C5"
        padding (10, 5)
        
        text msg:
            color "#FFFFFF"
            size 16
            italic True
    
    timer 2.5 action Hide("marginalia")

# Animation for marginalia appearance
transform marginalia_anim:
    on show:
        alpha 0
        xoffset 50
        linear 0.3 alpha 1.0 xoffset 0
    on hide:
        linear 0.3 alpha 0 xoffset 50

# Advanced meta-horror screens disabled for initial launch
# Will be re-enabled once core functionality is stable

# Save/Load screens will be enhanced later with haunted slot features
# For now, using standard Ren'Py save/load functionality

# Style definitions for quick menu
style quick_button is button:
    xsize 80
    ysize 30

style quick_button_text is button_text:
    size 16
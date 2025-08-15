# Blue Pencil Accessibility System - Universal Design
# Text scaling, dyslexia support, color-safe palettes, full accessibility

# Accessibility preferences
default text_scale = 1.0
default use_dyslexia_font = False
default reduce_halftone = False
default color_safe_mode = False
default show_audio_subtitles = True
default reduce_motion = False
default high_contrast = False

# Font definitions
define gui.default_font = "DejaVuSans.ttf"
define gui.dyslexia_font = "_OpenDyslexic3-Regular.ttf"

# Color-safe palette (for colorblind accessibility)
define color_safe = {
    "blue": "#0173B2",
    "orange": "#DE8F05", 
    "green": "#029E73",
    "red": "#CC78BC",
    "purple": "#CA9161",
    "brown": "#FBAFE4",
    "pink": "#949494",
    "gray": "#000000"
}

# Text scaling system
init python:
    def update_text_scale():
        # Update all GUI text sizes based on scale
        gui.text_size = int(22 * text_scale)
        gui.name_text_size = int(24 * text_scale)
        gui.interface_text_size = int(18 * text_scale)
        gui.button_text_size = int(18 * text_scale)
        gui.label_text_size = int(24 * text_scale)
        
        # Refresh UI
        renpy.restart_interaction()

# Dyslexia-friendly font toggle
label toggle_dyslexia_font:
    if use_dyslexia_font:
        $ gui.default_font = gui.dyslexia_font
        $ persistent.dyslexia_font = True
    else:
        $ gui.default_font = "DejaVuSans.ttf"
        $ persistent.dyslexia_font = False
    
    "Font changed. Text should now be easier to read."
    return

# Color-safe mode for colorblind players
label toggle_color_safe_mode:
    if color_safe_mode:
        # Replace colors with colorblind-safe alternatives
        $ gui.accent_color = color_safe["blue"]
        $ persistent.color_safe = True
        "Color-safe mode enabled. High contrast colors activated."
    else:
        # Restore original colors
        $ gui.accent_color = '#2B68C5'
        $ persistent.color_safe = False
        "Standard colors restored."
    
    return

# Reduce motion for vestibular disorders
label toggle_reduce_motion:
    if reduce_motion:
        # Disable drift effects and animations
        $ drift_intensity = 0.0
        call clear_drift_effects
        $ persistent.reduce_motion = True
        "Motion effects reduced. Animations disabled."
    else:
        $ persistent.reduce_motion = False
        "Standard motion effects restored."
    
    return

# High contrast mode
label toggle_high_contrast:
    if high_contrast:
        $ gui.text_color = '#000000'
        $ gui.interface_text_color = '#000000'
        $ persistent.high_contrast = True
        "High contrast mode enabled."
    else:
        $ gui.text_color = '#402020'
        $ gui.interface_text_color = '#402020'  
        $ persistent.high_contrast = False
        "Standard contrast restored."
    
    return

# Comprehensive accessibility screen
screen accessibility_preferences():
    tag menu
    
    frame:
        xfill True
        yfill True
        background "#F5F5DC"
        
        vbox:
            xalign 0.5
            yalign 0.5
            spacing 15
            
            text "Accessibility Settings" size 32 color "#2B68C5"
            
            null height 20
            
            # Text scaling
            hbox:
                text "Text Scale: " size 18
                bar value FieldValue(store, "text_scale", 2.0, offset=0.5) xsize 200
                text "[text_scale:.1f]x" size 18
            
            # Font options
            textbutton "Dyslexia-Friendly Font: [use_dyslexia_font]" action [
                ToggleVariable("use_dyslexia_font"),
                Function(toggle_dyslexia_font)
            ]
            
            # Visual accessibility
            textbutton "Reduce Halftone Effects: [reduce_halftone]" action ToggleVariable("reduce_halftone")
            textbutton "Color-Safe Mode: [color_safe_mode]" action [
                ToggleVariable("color_safe_mode"),
                Function(toggle_color_safe_mode)
            ]
            textbutton "High Contrast: [high_contrast]" action [
                ToggleVariable("high_contrast"),
                Function(toggle_high_contrast)
            ]
            
            # Motion accessibility
            textbutton "Reduce Motion: [reduce_motion]" action [
                ToggleVariable("reduce_motion"), 
                Function(toggle_reduce_motion)
            ]
            
            # Audio accessibility
            textbutton "Audio Subtitles: [show_audio_subtitles]" action ToggleVariable("show_audio_subtitles")
            
            null height 20
            
            # Honest Mode (if unlocked)
            if persistent.mercy:
                textbutton "Honest Mode: [persistent.honest_mode]" action Function(toggle_honest_mode)
                text "Disables all meta-horror effects" size 14 italic True
            
            null height 20
            
            hbox:
                textbutton "Audio Settings" action ShowMenu("audio_preferences")
                textbutton "Return" action Return()

# Emergency accessibility activation
init python:
    def emergency_accessibility():
        # Shift+A for emergency accessibility
        if hasattr(renpy, 'key') and renpy.key.get('shift') and renpy.key.get('a'):
            store.persistent.honest_mode = True
            store.reduce_motion = True
            store.high_contrast = True
            store.text_scale = 1.5
            renpy.call("activate_honest_mode")
            renpy.notify("Emergency accessibility activated.")

# Accessibility-aware subtitle system
label show_subtitle(text, duration=2.0):
    if show_audio_subtitles:
        $ renpy.notify(text)
        $ renpy.pause(duration)
    return

# Update existing systems for accessibility
label accessibility_check_all_systems:
    # Update text scaling
    $ update_text_scale()
    
    # Check motion reduction
    if reduce_motion or persistent.honest_mode:
        call clear_drift_effects
        $ drift_intensity = 0.0
    
    # Check color safety
    if color_safe_mode:
        call toggle_color_safe_mode
    
    # Check high contrast
    if high_contrast:
        call toggle_high_contrast
    
    return

# Accessibility validation
label validate_accessibility:
    "Accessibility Check:"
    
    if text_scale >= 1.2:
        "✓ Text scaling: [text_scale:.1f]x"
    else:
        "⚠ Text scaling could be increased for better readability"
    
    if use_dyslexia_font:
        "✓ Dyslexia-friendly font enabled"
    
    if show_audio_subtitles:
        "✓ Audio subtitles enabled"
    
    if persistent.honest_mode:
        "✓ Honest Mode: All meta-horror effects disabled"
    
    if reduce_motion:
        "✓ Motion effects reduced"
    
    if high_contrast:
        "✓ High contrast enabled"
    
    if color_safe_mode:
        "✓ Color-safe palette active"
    
    "Accessibility validation complete."
    return
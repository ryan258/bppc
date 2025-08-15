# Honest Mode System - Post-Credits Accessibility Feature
# Disables all meta-horror effects for accessibility and speedruns

# Honest Mode toggle and management
label toggle_honest_mode:
    if persistent.honest_mode:
        $ persistent.honest_mode = False
        "Honest Mode disabled."
        "Meta-horror effects restored."
    else:
        $ persistent.honest_mode = True
        "Honest Mode enabled."
        "All meta-horror effects disabled."
        call activate_honest_mode
    
    return

# Activate honest mode effects
label activate_honest_mode:
    if persistent.honest_mode:
        # Disable all meta-horror elements
        call clear_drift_effects
        call disable_haunted_effects
        
        # Reset problematic variables
        $ hub_pressure = 0
        $ editorial_pressure = 0
        $ drift_intensity = 0.0
        
        # Disable timers
        $ renpy.cancel_timer("mercy_timeout")
        
        "All meta-horror effects disabled."
        "Story proceeds without editorial interference."
        "Save thumbnails show honest representations."
        "No haunted saves, no drift, no Hub intrusions."
    
    return

# Honest Mode preferences screen addition
screen honest_mode_preferences():
    frame:
        xalign 0.5
        yalign 0.5
        
        vbox:
            text "Honest Mode Settings" size 24
            null height 10
            text "Disables all meta-horror effects for accessibility."
            text "Recommended for players sensitive to:"
            text "• Visual distortion"
            text "• Simulated software errors"
            text "• Fourth wall breaking"
            text "• Save file manipulation illusions"
            null height 10
            
            if persistent.mercy:
                textbutton "Toggle Honest Mode" action Function(toggle_honest_mode)
            else:
                text "Complete the game once to unlock Honest Mode."
            
            null height 20
            textbutton "Return" action Return()

# Emergency Shift+Hold activation (accessibility)
init python:
    # Emergency honest mode toggle
    def emergency_honest_mode():
        if renpy.get_physical_size() and hasattr(renpy, 'key'):
            if renpy.key['shift']:
                store.persistent.honest_mode = True
                renpy.call("activate_honest_mode")
                renpy.notify("Emergency Honest Mode activated.")

# Honest mode during centerfold (safety override)
label honest_centerfold_override:
    if persistent.honest_mode:
        # Skip the interactive centerfold entirely
        scene black
        "You walk past the magazine without looking."
        "Sometimes the kindest choice is not to engage."
        $ mercy_achieved = True
        $ persistent.mercy = True
        $ compassion += 20
        call mercy_notification
        return
    
    return

# Honest mode timer handling
label honest_timer_check:
    if persistent.honest_mode:
        # Cancel any running timers
        $ renpy.cancel_timer("mercy_timeout")
        return
    
    return
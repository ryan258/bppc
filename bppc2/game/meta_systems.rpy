# Blue Pencil Meta-Horror Systems
# Phase 2: Editorial Elements

# Reload tracking system
default reload_count = 0
default last_save_point = ""
default editorial_pressure = 0

# Hub voice intrusion tracking
default hub_spoken = False
default hub_warnings = 0

# Drift effect controls
default drift_intensity = 0.0
default visual_corruption = 0

# Reload detection - call this at key choice points
label track_reload(save_point=""):
    if save_point == last_save_point:
        $ reload_count += 1
        $ culp += 1
        $ editorial_pressure += 1
        
        # Escalating response to reloading
        if reload_count >= 3 and not hub_spoken:
            call first_hub_intrusion
    
    $ last_save_point = save_point
    return

# First gentle Hub intrusion
label first_hub_intrusion:
    $ hub_spoken = True
    
    # Subtle blue-pencil marginalia appears
    show blue_pencil at truecenter with dissolve
    pause 0.5
    hide blue_pencil with dissolve
    
    # Use advanced Hub voice system
    call hub_speak("That was a cute choice. It didn't work.")
    
    $ hub_pressure += 5
    $ hub_warnings += 1
    
    # Brief pause, then continue normally
    pause 1.0
    return

# Blue-pencil marginalia system
label show_marginalia(text=""):
    # Simplified marginalia for launch - just show hub text
    if text:
        hub "{color=#2B68C5}{size=-4}[text]{/size}{/color}"
    return

# Basic drift effect
transform drift_text:
    xoffset 0
    linear 2.0 xoffset 1
    linear 2.0 xoffset -1
    linear 2.0 xoffset 0
    repeat

# Apply drift to text when editorial pressure is high
label check_drift:
    if editorial_pressure >= 10:
        $ drift_intensity = min(editorial_pressure / 20.0, 1.0)
        # Text will wobble slightly
    return

# Hub pressure escalation
label escalate_hub_pressure:
    $ hub_pressure += editorial_pressure
    
    if hub_pressure >= 20 and hub_warnings < 3:
        call hub_warning
    return

# Hub warning (more direct)
label hub_warning:
    $ hub_warnings += 1
    
    call show_marginalia("Fix this.")
    hub "{color=#2B68C5}Your attention is... scattered. Focus.{/color}"
    
    $ hub_pressure += 10
    return

# Check if player is optimizing too much
label check_optimization:
    if reload_count >= 5:
        $ culp += 5
        call show_marginalia("Stop trying so hard.")
        hub "{color=#2B68C5}Perfection is not the goal. Progress is.{/color}"
    return
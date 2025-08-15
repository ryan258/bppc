# Title Memory System - The game remembers mercy
# "Thank you for closing the book."

# Title screen modifications based on mercy achievement
screen main_menu():
    tag menu
    
    # Background
    frame:
        xfill True
        yfill True
        background "#F5F5DC"  # Warm paper color
    
    vbox:
        xalign 0.5
        yalign 0.5
        spacing 20
        
        # Title with memory
        if persistent.mercy:
            text "Blue Pencil Poetry Club" size 40 color "#2B68C5"
            text "Thank you for closing the book." size 16 color "#800080" italic True
        else:
            text "Blue Pencil Poetry Club" size 40 color "#2B68C5"
        
        # Menu options
        textbutton "Start" action Start()
        
        if persistent.mercy:
            textbutton "Continue (Honest Mode)" action Start("honest_mode_start")
        
        textbutton "Load" action ShowMenu("load")
        textbutton "Preferences" action ShowMenu("preferences")
        textbutton "Quit" action Quit()

# Honest mode start point
label honest_mode_start:
    $ persistent.honest_mode = True
    call clear_drift_effects
    call disable_haunted_effects
    
    "Honest Mode enabled."
    "All meta-horror effects disabled."
    "The story proceeds without editorial interference."
    
    jump start

# Mercy achievement notification
label mercy_notification:
    if persistent.mercy and not mercy_achieved:
        scene black
        centered "{size=+6}Mercy Achieved{/size}"
        ""
        centered "You chose restraint over curiosity."
        centered "Compassion over optimization."
        centered "The kindest ending unlocked."
        ""
        centered "The title screen will remember this."
        centered "Future playthroughs will acknowledge your choice."
        ""
        centered "{size=-4}Press any key to continue{/size}"
        pause
    
    return

# Post-credits sequence for mercy ending
label mercy_credits:
    scene black
    
    centered "{size=+4}Blue Pencil Poetry Club{/size}"
    ""
    centered "A story about attention, restraint, and the weight of observation."
    ""
    centered "You chose not to unbind the centerfold."
    centered "In doing so, you preserved something precious:"
    centered "The boundary between reader and editor."
    centered "The space between curiosity and respect."
    ""
    centered "Thank you."
    ""
    centered "— The Editorial Staff"
    ""
    centered "{size=-4}A kind reader left the lights on behind them.{/size}"
    
    # Wait then return to title with memory
    pause 5.0
    return

# Check for mercy achievement at key points
label check_mercy_conditions:
    # Mercy is achieved by NOT touching the centerfold staples
    if centerfold_active and centerfold_timer <= 0 and not staples_touched:
        $ mercy_achieved = True
        $ persistent.mercy = True
        $ compassion += 30
        call mercy_notification
        call mercy_credits
    
    return

# Reset mercy status for new game+ testing
label reset_mercy_status:
    $ persistent.mercy = False
    $ mercy_achieved = False
    $ compassion = 0
    "Mercy status reset for testing."
    return

# Compassion tracking system
label track_compassion(reason=""):
    if reason == "restraint":
        $ compassion += 5
        call show_marginalia("Noticed.")
    elif reason == "patience":
        $ compassion += 3
        call show_marginalia("Good.")
    elif reason == "mercy":
        $ compassion += 10
        call show_marginalia("Kind.")
    
    # Compassion affects Hub's attitude
    if compassion >= 20:
        hub "{color=#2B68C5}You're learning.{/color}"
    elif compassion >= 30:
        hub "{color=#2B68C5}There's hope for this story yet.{/color}"
    
    return

# Mercy window warnings (gentle guidance toward restraint)
label mercy_window_guidance:
    if centerfold_timer <= 15 and centerfold_timer > 10:
        call show_marginalia("Think carefully.")
    elif centerfold_timer <= 10 and centerfold_timer > 5:
        call show_marginalia("Patience.")
    elif centerfold_timer <= 5:
        call show_marginalia("Almost.")
    
    return
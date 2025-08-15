# Advanced Hub Voice System - Editorial Personality Evolution
# The Hub becomes more sophisticated and persistent as pressure builds

# Hub personality states
default hub_patience = 100
default hub_directness = 0
default hub_desperation = 0

# Hub voice evolution based on pressure
label hub_speak(message="", context="general"):
    # Determine Hub's current personality state
    if hub_pressure < 20:
        call hub_gentle(message)
    elif hub_pressure < 50:
        call hub_firm(message)
    elif hub_pressure < 80:
        call hub_direct(message) 
    else:
        call hub_desperate(message)
    
    return

# Gentle Hub (early stages)
label hub_gentle(message):
    $ hub_patience -= 5
    
    if message == "":
        if reload_count >= 2:
            hub "{color=#2B68C5}Perhaps try a different approach?{/color}"
        else:
            hub "{color=#2B68C5}Interesting choice.{/color}"
    else:
        hub "{color=#2B68C5}[message]{/color}"
    
    return

# Firm Hub (building pressure)
label hub_firm(message):
    $ hub_patience -= 10
    $ hub_directness += 5
    
    if message == "":
        if reload_count >= 4:
            hub "{color=#2B68C5}Stop. Optimizing. Everything.{/color}"
        elif editorial_pressure >= 15:
            hub "{color=#2B68C5}Your attention is fragmenting the narrative.{/color}"
        else:
            hub "{color=#2B68C5}Focus. The story needs direction.{/color}"
    else:
        hub "{color=#2B68C5}[message]{/color}"
    
    return

# Direct Hub (losing patience)
label hub_direct(message):
    $ hub_patience -= 20
    $ hub_directness += 10
    
    if message == "":
        if reload_count >= 6:
            hub "{color=#2B68C5}ENOUGH. You are damaging the text.{/color}"
        elif culp >= 15:
            hub "{color=#2B68C5}Compulsive revision is not creativity.{/color}"
        else:
            hub "{color=#2B68C5}Listen. For once, just listen.{/color}"
    else:
        hub "{color=#2B68C5}[message]{/color}"
    
    call show_marginalia("STOP")
    
    return

# Desperate Hub (maximum pressure)
label hub_desperate(message):
    $ hub_patience = max(0, hub_patience - 30)
    $ hub_directness += 15
    $ hub_desperation += 10
    
    if hub_desperation >= 30:
        # Hub starts breaking character
        hub "{color=#2B68C5}Please. I'm trying to help you tell this story properly.{/color}"
        hub "{color=#2B68C5}But you keep... breaking things.{/color}"
        hub "{color=#2B68C5}The gutters are compressed. The balloons are thin.{/color}"
        hub "{color=#2B68C5}Do you see what your optimization has done?{/color}"
    else:
        if message == "":
            hub "{color=#2B68C5}WHY WON'T YOU LISTEN?{/color}"
        else:
            hub "{color=#2B68C5}[message]{/color}"
    
    # Desperate visual effects
    show screen static_overlay
    pause 0.5
    hide screen static_overlay
    
    return

# Static overlay for desperate Hub moments
screen static_overlay():
    frame:
        background Solid("#FFFFFF", alpha=0.3)
        xfill True
        yfill True

# Hub meta-commentary system
label hub_meta_commentary:
    # Hub comments on specific player behaviors
    
    if attn["mara"] >= 10:
        call hub_speak("You're drawn to the self-aware one. Predictable.")
    
    if bond["june"] >= 8:
        call hub_speak("The optimist won't save you from what's coming.")
    
    if reload_count >= 8:
        call hub_speak("Eight times. You've tried eight different ways.")
        call hub_speak("The outcome will not change.")
        call hub_speak("Accept the story as written.")
    
    return

# Hub awareness of player's real-world situation
label hub_fourth_wall_break:
    # Only in extreme circumstances
    if hub_pressure >= 100 and hub_desperation >= 40:
        scene black
        
        hub "{color=#2B68C5}You're sitting there, aren't you?{/color}"
        hub "{color=#2B68C5}Behind the screen.{/color}"
        hub "{color=#2B68C5}Clicking. Reloading. Optimizing.{/color}"
        hub "{color=#2B68C5}Thinking you can perfect this.{/color}"
        hub "{color=#2B68C5}But some stories resist perfection.{/color}"
        hub "{color=#2B68C5}Some stories need to stay broken.{/color}"
        
        $ hub_pressure += 50
        
        pause 3.0
        scene bg classroom
        
        "The familiar classroom returns."
        "But you feel exposed. Seen."
        "Like someone has been watching you this entire time."
    
    return

# Hub's editorial philosophy
label hub_philosophy:
    hub "{color=#2B68C5}Every story needs an editor.{/color}"
    hub "{color=#2B68C5}Every narrative needs guidance.{/color}"
    hub "{color=#2B68C5}But you... you resist editing.{/color}"
    hub "{color=#2B68C5}You want to control every choice, perfect every outcome.{/color}"
    hub "{color=#2B68C5}That's not how stories work.{/color}"
    hub "{color=#2B68C5}Stories need to breathe. To flow. To surprise even their creators.{/color}"
    hub "{color=#2B68C5}Let go.{/color}"
    
    return

# Hub intervention escalation
label escalate_hub_intervention:
    if hub_pressure >= 30 and not fake_traceback_used:
        call check_fake_traceback_conditions
    
    if hub_pressure >= 50 and not haunted_slot_active:
        call check_haunted_save_activation
    
    if hub_pressure >= 80:
        call hub_fourth_wall_break
    
    return
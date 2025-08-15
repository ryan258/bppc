# Try Again Trap - Serena Exemplar Scene
# This is the signature mechanic where reloading causes visual scarring

# The converging choice that leads to the same outcome
label serena_trap_scene:
    "A week has passed since your first poetry club meeting."
    "Today, you encounter Serena in the hallway - another student who seems interested in joining."
    
    show serena neutral at center
    serena "Hey, you're in that poetry club, right? I've been thinking about joining."
    
    # Save point for reload detection
    call track_reload("serena_choice")
    
    # The trap: these choices all lead to the same result, but reloading makes it worse
    menu:
        "You should definitely join! We'd love to have you.":
            call serena_response_optimistic
            
        "It's pretty casual. You might like it if you're into creative writing.":
            call serena_response_neutral
            
        "We're a small group, but everyone's pretty welcoming.":
            call serena_response_measured

    # All paths converge here
    call serena_outcome
    return

label serena_response_optimistic:
    leo "You should definitely join! We'd love to have you."
    $ bond["june"] += 1  # June-like response
    return

label serena_response_neutral:
    leo "It's pretty casual. You might like it if you're into creative writing."
    $ bond["mina"] += 1  # Mina-like measured response
    return

label serena_response_measured:
    leo "We're a small group, but everyone's pretty welcoming."
    $ bond["kit"] += 1  # Kit-like honest response
    return

# The outcome is the same regardless of choice
label serena_outcome:
    serena "Thanks, but... I think I'll pass."
    serena "I heard some weird things about that club lately."
    
    # Apply visual scarring if player has reloaded
    if reload_count >= 2:
        call apply_visual_scarring
        
    # Serena's response gets more unsettling with each reload
    if reload_count == 0:
        serena "Maybe next semester. See you around!"
    elif reload_count <= 3:
        serena "Something about... being watched? I don't know. Sounds creepy."
        call show_marginalia("She's not wrong.")
    else:
        serena "People say you can't trust your own words there."
        serena "Like someone else is putting words in your mouth."
        call show_marginalia("Stop. Reloading.")
        
        # Hub intervention if too many reloads
        if reload_count >= 5:
            call hub_direct_intervention
    
    hide serena with dissolve
    
    # Player reflection
    if reload_count >= 3:
        "No matter what you said, the outcome was the same."
        "Why does it feel like the words themselves are... shifting?"
    
    return

# Visual scarring from reloading
label apply_visual_scarring:
    # Text spacing gets tighter with each reload
    if reload_count >= 2:
        $ renpy.transition(Dissolve(0.5))
        "The text feels cramped, like margins are shrinking."
        
    if reload_count >= 4:
        # Balloon tails (speech indicators) get thinner
        $ renpy.transition(pixellate)
        "Words feel... thinner. Less substantial."
        
    if reload_count >= 6:
        # Full gutter compression
        $ renpy.transition(squares)
        "Everything's compressed. Squeezed. Wrong."
    
    return

# Direct Hub intervention for excessive reloading
label hub_direct_intervention:
    scene black with squares
    
    hub "{color=#2B68C5}Stop.{/color}"
    hub "{color=#2B68C5}You are damaging the narrative structure.{/color}"
    hub "{color=#2B68C5}Each reload compresses the gutters.{/color}"
    hub "{color=#2B68C5}Each retry thins the dialogue balloons.{/color}"
    hub "{color=#2B68C5}This is not a game to be optimized.{/color}"
    hub "{color=#2B68C5}This is a story to be experienced.{/color}"
    
    $ hub_pressure += 20
    $ drift_intensity += 0.5
    
    scene bg classroom with dissolve
    return

# Character definition for Serena
define serena = Character("Serena", color="#CD853F")  # Sandy brown
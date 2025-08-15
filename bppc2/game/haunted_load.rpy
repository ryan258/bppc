# Haunted Load System - Advanced Meta Mechanic
# Creates the illusion of save file corruption without touching actual files

# Haunted save slot configuration
default haunted_slot_active = False
default haunted_interstitial_seen = False
default real_save_data = None

# Initialize haunted save after certain conditions
label initialize_haunted_save:
    $ haunted_slot_active = True
    $ persistent.haunted_save = True
    return

# Custom load screen that includes haunted slot
screen load(type="load"):
    tag menu
    
    vbox:
        text "Load Game" size 40
        
        # Regular save slots
        for i in range(1, 6):
            textbutton "Slot [i]" action FileLoad(i)
        
        # Haunted slot appears under certain conditions
        if persistent.haunted_save and not persistent.honest_mode:
            textbutton "{color=#800000}Corrupted Slot{/color}" action Function(haunted_load_sequence)
        else:
            textbutton "Slot 6" action FileLoad(6)
            
        textbutton "Return" action Return()

# The haunted load sequence
label haunted_load_sequence:
    # Store current game state before interstitial
    $ real_save_data = {
        "attn": attn.copy(),
        "bond": bond.copy(), 
        "reload_count": reload_count,
        "hub_pressure": hub_pressure
    }
    
    # Brief loading screen effect
    scene black
    "Loading..."
    pause 0.5
    
    # The interstitial - empty room with Hub whisper
    call haunted_interstitial
    
    # Return to real game state
    $ attn = real_save_data["attn"]
    $ bond = real_save_data["bond"]
    $ reload_count = real_save_data["reload_count"]
    $ hub_pressure = real_save_data["hub_pressure"]
    
    # Continue normal gameplay
    jump after_haunted_load

# The eerie interstitial scene
label haunted_interstitial:
    scene bg empty_room
    
    "You find yourself in an empty classroom."
    "Dust motes dance in afternoon light."
    "But something is wrong."
    
    # Hub whisper - barely audible
    hub "{color=#2B68C5}{size=-6}You saved her here. You will spend it somewhere else.{/size}{/color}"
    
    $ haunted_interstitial_seen = True
    $ hub_pressure += 15
    
    "The words hang in the air like smoke."
    "Then everything snaps back to normal."
    
    return

# Empty room background
image bg empty_room = "#D3D3D3"  # Light gray, unsettling

# Continuation point after haunted load
label after_haunted_load:
    scene bg classroom
    "You're back in the familiar classroom."
    "But the memory of that empty room lingers."
    "Did that really happen? Or was it just your imagination?"
    
    if not haunted_interstitial_seen:
        "Something about loading that save felt... wrong."
        "Like you weren't supposed to be there."
    
    return

# Haunted save activation conditions
label check_haunted_save_activation:
    # Activate after sufficient meta-awareness
    if hub_pressure >= 30 and reload_count >= 3 and not haunted_slot_active:
        call initialize_haunted_save
        call show_marginalia("Now you're paying attention.")
        hub "{color=#2B68C5}Some doors, once opened, cannot be closed.{/color}"
    
    return

# Honest Mode disables haunted effects
label disable_haunted_effects:
    if persistent.honest_mode:
        $ haunted_slot_active = False
        "Haunted effects disabled."
    return
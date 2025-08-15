# Mailbag System - Reader Response Simulation
# This system generates "letters" that reflect player behavior

# Evening mailbag - shows how the "readers" perceive player actions
label evening_mailbag:
    scene black
    "Evening. You check your poetry club mailbag."
    "Each week, members can submit questions, comments, or concerns."
    "Tonight feels... different."
    
    # Generate letter based on player behavior
    if reload_count >= 3:
        call mailbag_optimization_letter
    elif hub_pressure >= 10:
        call mailbag_observation_letter  
    elif culp >= 5:
        call mailbag_attention_letter
    else:
        call mailbag_normal_letter
    
    return

# Letter reflecting optimization/reloading behavior
label mailbag_optimization_letter:
    "A letter catches your eye. The handwriting looks... familiar."
    ""
    "{i}Dear Poetry Club,{/i}"
    "{i}I've been watching your meetings with interest.{/i}"
    "{i}I notice some members seem to... reconsider their words frequently.{/i}"
    "{i}While revision is natural, excessive revision can damage the flow.{/i}"
    "{i}Trust your first instincts. They're usually the truest.{/i}"
    "{i}Sincerely, A Concerned Observer{/i}"
    ""
    $ hub_pressure += 5
    call show_marginalia("Stop second-guessing yourself.")
    return

# Letter about being observed
label mailbag_observation_letter:
    "A letter written in blue ink. The words are precise, clinical."
    ""
    "{i}To the Blue Pencil Poetry Club,{/i}"
    "{i}Your recent discussions have been... noted.{/i}"
    "{i}Some members express concern about being 'watched.'{/i}"
    "{i}This is natural. All writers have editors.{/i}"
    "{i}All stories need guidance.{/i}"
    "{i}Trust the process.{/i}"
    "{i}Yours truly, The Editor{/i}"
    ""
    $ hub_pressure += 10
    hub "{color=#2B68C5}You see? Even the readers understand.{/color}"
    return

# Letter about attention/focus issues
label mailbag_attention_letter:
    "A letter that seems to shimmer slightly as you read it."
    ""
    "{i}Dear Leo,{/i}"
    "{i}I've noticed you paying very close attention to certain members.{/i}"
    "{i}Attention is a powerful force. Use it wisely.{/i}"
    "{i}Too much focus can... distort things.{/i}"
    "{i}People begin to change under intense observation.{/i}"
    "{i}Be mindful of where you direct your gaze.{/i}"
    "{i}A Fellow Writer{/i}"
    ""
    "The letter feels warm to the touch."
    $ attn["mara"] += 1  # Mara would write something like this
    return

# Normal supportive letter
label mailbag_normal_letter:
    "A cheerful letter on pastel paper."
    ""
    "{i}Hi everyone!{/i}"
    "{i}Just wanted to say how much I'm enjoying our poetry sessions.{/i}"
    "{i}It's wonderful to have a space where we can be creative together.{/i}"
    "{i}Leo, thanks for joining us! Fresh perspectives are always welcome.{/i}"
    "{i}Looking forward to next week!{/i}"
    "{i}Love, June{/i}"
    ""
    "June's enthusiasm is infectious, even in writing."
    $ bond["june"] += 1
    return

# Check mailbag behavior reflection
label check_mailbag_behavior:
    # The mailbag reflects how player has been acting
    if reload_count >= 5:
        "You notice several letters seem to be... repeating."
        "The same concerns, the same warnings."
        "As if someone keeps sending the same message."
        call show_marginalia("Stop. Making. Us. Repeat. Ourselves.")
    
    if hub_pressure >= 20:
        "The letters are becoming more... direct."
        "Less suggestion, more instruction."
        "As if someone is losing patience."
    
    return
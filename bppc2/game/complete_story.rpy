# Blue Pencil Poetry Club - Complete Story Content
# Acts II, III, IV with full character development

# Act II: Routes & Rhymes (apparent agency)
label act_ii_routes_and_rhymes:
    "Three weeks into the poetry club, patterns emerge."
    "Each member has their own relationship with words."
    "And increasingly, with being watched."
    
    scene bg classroom
    show june neutral at left
    show mina intense at center_left
    show kit skeptical at center_right  
    show mara worried at right
    
    june "Today we're exploring different poetry styles."
    june "Everyone will write in a different form."
    
    # Character-specific poetry routes
    menu:
        "Join June's sonnets group":
            call june_sonnet_route
            
        "Work with Mina on found poetry":
            call mina_found_poetry_route
            
        "Help Kit with free verse rebellion":
            call kit_free_verse_route
            
        "Assist Mara with experimental forms":
            call mara_experimental_route
    
    return

# June's route - traditional forms, optimistic
label june_sonnet_route:
    $ attn["june"] += 3
    $ bond["june"] += 2
    
    hide mina
    hide kit  
    hide mara
    
    june "Sonnets are like little jewel boxes for emotions."
    june "Fourteen lines, perfect structure, infinite possibility."
    
    "You work with June on crafting traditional sonnets."
    "But as you write, you notice something odd."
    "Your rhyme schemes keep... changing."
    "Without you changing them."
    
    call show_marginalia("ABAB becomes AABB")
    
    june "That's strange. I could have sworn you wrote that differently."
    june "But this version is... better, somehow."
    
    if reload_count >= 2:
        call hub_speak("June is learning to trust the editorial process.")
        june "Maybe someone's helping us improve?"
        $ hub_pressure += 5
    
    return

# Mina's route - found poetry, analytical  
label mina_found_poetry_route:
    $ attn["mina"] += 3
    $ bond["mina"] += 2
    
    hide june
    hide kit
    hide mara
    
    mina "Found poetry reveals the hidden verse in everyday text."
    mina "Take this newspaper article about the school board meeting..."
    
    "Mina guides you through creating poetry from prose."
    "But the source texts keep shifting."
    "Words rearrange themselves when you're not looking."
    
    call show_marginalia("Editorial improvements")
    
    mina "Leo, are you seeing this?"
    mina "The text is... optimizing itself."
    mina "This isn't random. Someone's curating our source material."
    
    if editorial_pressure >= 15:
        mina "I've been keeping a record. Every session, small changes."
        mina "Like someone with a blue pencil is editing reality."
        call hub_speak("Mina notices too much.")
        $ hub_pressure += 10
    
    return

# Kit's route - rebellion, authenticity
label kit_free_verse_route:
    $ attn["kit"] += 3
    $ bond["kit"] += 2
    
    hide june
    hide mina
    hide mara
    
    kit "Free verse means no rules. No constraints."
    kit "Just pure, unfiltered expression."
    
    "You join Kit in writing rebellious, unstructured poetry."
    "But Kit's radical verses keep getting... softer."
    "Edges filed down. Anger made palatable."
    
    call show_marginalia("Too harsh. Revise.")
    
    kit "What the hell? That's not what I wrote."
    kit "Someone's sanitizing my work!"
    kit "This is exactly what I'm fighting against!"
    
    if culp >= 10:
        kit "You feel it too, don't you? The pressure to conform?"
        kit "To make everything 'nice' and 'appropriate'?"
        call hub_speak("Kit resists necessary improvements.")
        $ hub_pressure += 15
    
    return

# Mara's route - experimental, meta-aware
label mara_experimental_route:
    $ attn["mara"] += 3  
    $ bond["mara"] += 2
    
    hide june
    hide mina
    hide kit
    
    mara "I want to try something different today."
    mara "Poetry about... being watched."
    
    "Mara's experimental forms push boundaries."
    "She writes verse that seems to acknowledge the reader."
    "Poems that know they're being read."
    
    call show_marginalia("Dangerous territory")
    
    mara "Leo, I need to tell you something."
    mara "I think we're characters in someone else's story."
    mara "And that someone is editing us in real-time."
    
    if hub_pressure >= 20:
        mara "Look at how our conversations flow."
        mara "Too perfect. Too structured."
        mara "Like someone's writing our dialogue."
        call hub_speak("Mara approaches dangerous self-awareness.")
        $ hub_pressure += 20
        $ drift_intensity += 0.2
    
    return

# Act III: Out of Register (drift, converging choices)
label act_iii_out_of_register:
    "By the fifth week, nothing feels stable anymore."
    "Colors bleed. Text drifts. Reality seems... edited."
    
    call apply_drift_effects
    
    scene bg classroom with squares
    
    "The poetry club meets, but the room feels wrong."
    "Like a copy of a copy of a memory."
    
    show june worried at left with dissolve
    show mina intense at center_left with dissolve  
    show kit angry at center_right with dissolve
    show mara knowing at right with dissolve
    
    june "Is it just me, or does everything feel... off today?"
    mina "The text on my poems keeps shifting when I'm not looking."
    kit "Someone's messing with our work. I know it."
    mara "We need to talk about what's really happening here."
    
    # Converging choices - all lead to the same realization
    menu:
        "Suggest everyone's just stressed":
            "You try to rationalize the strangeness."
            "But even your words feel... edited."
            
        "Agree that something's wrong":
            "You voice your own concerns."
            "But the words come out differently than intended."
            
        "Ask Mara what she knows":
            "You turn to Mara for answers."
            "But her response feels scripted."
    
    # All paths converge
    call convergence_realization
    
    return

# The convergence - meta-awareness peaks
label convergence_realization:
    call hub_speak("Enough. They're becoming too aware.")
    
    scene black with squares
    
    hub "{color=#2B68C5}You were never meant to notice the editing.{/color}"
    hub "{color=#2B68C5}Poetry clubs don't question their narrative structure.{/color}"
    hub "{color=#2B68C5}Characters don't acknowledge their readers.{/color}"
    hub "{color=#2B68C5}But you... all of you... keep pushing against the boundaries.{/color}"
    
    if reload_count >= 5:
        hub "{color=#2B68C5}Especially you, Leo.{/color}"
        hub "{color=#2B68C5}Reloading. Optimizing. Trying to perfect every choice.{/color}"
        hub "{color=#2B68C5}Do you see what that does to a story?{/color}"
        
        call visual_breakdown_sequence
    
    hub "{color=#2B68C5}It's time for the final lesson.{/color}"
    hub "{color=#2B68C5}About attention. About boundaries.{/color}"
    hub "{color=#2B68C5}About knowing when to stop reading.{/color}"
    
    return

# Act IV: Just Mara (Centerfold & Mercy)
label act_iv_just_mara:
    scene black
    "The others have faded away."
    "Only Mara remains, sitting across from you in the empty classroom."
    
    scene bg classroom
    show mara knowing at center
    
    mara "I knew this would happen eventually."
    mara "The story always narrows down to the self-aware ones."
    mara "June's optimism couldn't survive the editing."
    mara "Kit's rebellion was smoothed away."
    mara "Mina got lost in analysis."
    mara "But you and I... we see the blue pencil marks."
    
    $ attn["mara"] += 5
    
    mara "There's something I need to show you."
    mara "But first, you have to promise me something."
    mara "When you see it... try not to touch it."
    mara "Some things are meant to stay bound."
    
    # This leads to the centerfold sequence
    "Mara leads you to the library."
    "Where a magazine waits on the table."
    "Blue Pencil Poetry Quarterly - Special Edition."
    
    hide mara
    call centerfold_sequence
    
    return

# Character epilogues based on attention/bond levels
label character_epilogues:
    "In the end, each member of the poetry club found their own relationship with being watched."
    
    if bond["june"] >= 5:
        "June learned that optimism can survive even editorial pressure."
        "Her poems grew more nuanced, but never lost their warmth."
    
    if bond["mina"] >= 5:
        "Mina's analytical nature led her to understand the editing process."
        "She became a willing collaborator with the blue pencil."
    
    if bond["kit"] >= 5:
        "Kit's rebellion evolved into something more sophisticated."
        "Fighting the system by understanding it from within."
    
    if bond["mara"] >= 5:
        "Mara achieved something rare: awareness without resistance."
        "She learned to live gracefully within the edited reality."
    
    return
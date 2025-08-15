# Blue Pencil Poetry Club - Core Script

# Game variables from the spec
default attn = {"june":0, "mina":0, "kit":0, "mara":0}
default bond = {"june":0, "mina":0, "kit":0, "mara":0}
default drift = 0
default culp = 0
default compassion = 0
default hub_pressure = 0

# Character definitions
define leo = Character("Leo", color="#402020")
define june = Character("June", color="#FFB6C1")  # Milkshake Pink
define mina = Character("Mina", color="#2B68C5")  # Pool Blue
define kit = Character("Kit", color="#800080")    # Darker purple for spiky personality
define mara = Character("Mara", color="#B8860B")  # Darker gold for self-aware treasurer
define hub = Character("", color="#2B68C5")       # The editorial voice (blue pencil)

# Narrator for scene descriptions
define n = Character(None, kind=nvl)

label start:
    scene black
    call content_note
    call act1_welcome
    return

# Content note as per spec
label content_note:
    scene black
    centered "{size=+6}Content Note{/size}"
    ""
    centered "This story depicts anxiety, obsessive behavior, and depression."
    centered "No graphic self-harm, no instructions."
    centered "If you need support, consider pausing and seeking local resources."
    ""
    centered "{size=-4}Press any key to continue{/size}"
    pause
    return

# Act I: Welcome to Blue Pencil Poetry Club
label act1_welcome:
    scene black
    "You are Leo, and today you're walking into something new."
    "The Blue Pencil Poetry Club meets every Tuesday after school in Mrs. Henderson's classroom."
    "You've been thinking about joining for weeks, ever since you saw the flyer with its cheerful diner-style font."
    
    scene bg classroom
    "The classroom smells like chalk dust and old books."
    "Four students are already seated in a circle, notebooks open, pencils ready."
    
    show june happy at left
    june "Oh! You must be our new member!"
    $ attn["june"] += 1
    
    june "I'm June, the club organizer. Welcome to Blue Pencil!"
    june "We're so excited to have fresh perspective in our little poetry circle."
    
    show mina neutral at center_left
    mina "Another poet joins our ranks."
    $ attn["mina"] += 1
    mina "I'm Mina. I collect verses like some people collect stamps."
    mina "Every line matters. Every word has weight."
    
    show kit skeptical at center_right  
    kit "Kit. I publish a zine called 'Ink Rebellion.'"
    $ attn["kit"] += 1
    kit "Fair warning - I'm not here for sunshine and rainbows poetry."
    kit "Real verse should have teeth."
    
    show mara knowing at right
    mara "And I'm Mara, treasurer and occasional voice of reason."
    $ attn["mara"] += 1
    mara "Though lately I wonder if any of us are quite as reasonable as we appear."
    
    menu:
        "Thanks, everyone. I'm Leo, and I'm excited to be here.":
            $ bond["june"] += 1
            june "Wonderful! We need that enthusiasm."
            
        "Nice to meet you all. I hope I can keep up.":
            $ bond["mina"] += 1
            mina "Humility. I respect that in a writer."
            
        "Sounds like this club has more edge than I expected.":
            $ bond["kit"] += 1
            kit "Finally, someone who gets it."
            
        "Voice of reason? That sounds ominous.":
            $ bond["mara"] += 1
            mara "You have good instincts, Leo."
    
    june "Well then! Let's begin today's session."
    june "Our theme today is 'New Beginnings' - perfect timing, wouldn't you say?"
    
    call poetry_session_1
    return

# First poetry session - introduces word mechanics and character personalities
label poetry_session_1:
    june "We'll start with a collaborative poem. Everyone contributes a line or two."
    june "Leo, since you're new, would you like to begin? Or would you prefer to listen first?"
    
    menu:
        "I'll give it a try. How about: 'Today I stepped through an unfamiliar door...'":
            $ bond["june"] += 1
            $ attn["june"] += 1
            june "Beautiful! A perfect opening line. So much possibility in that image."
            
        "I'd rather listen first and get a feel for the group's style.":
            $ bond["mina"] += 1
            $ attn["mina"] += 1
            mina "Wise. Poetry is best learned through careful observation."
            mina "June, why don't you start us off?"
            
        "Are there any rules I should know about?":
            $ bond["kit"] += 1  
            $ attn["kit"] += 1
            kit "Rules? Poetry doesn't have rules. That's the whole point."
            kit "Just say what you mean, mean what you say."
    
    june "I'll continue: 'The afternoon light painted golden squares on dusty desks...'"
    $ attn["june"] += 1
    
    show mina intense at center_left
    mina "And every shadow holds a story waiting to unfold..."
    $ attn["mina"] += 1
    
    show kit smirk at center_right
    kit "While outside, the real world spins on, indifferent to our pretty words."
    $ attn["kit"] += 1
    
    show mara worried at right
    mara "But maybe that's exactly why these words matter."
    $ attn["mara"] += 1
    
    # Subtle hint of meta-awareness from Mara
    mara "Maybe someone, somewhere, is paying very close attention indeed."
    
    june "That was lovely, everyone! Leo, how did that feel?"
    
    menu:
        "It felt... meaningful. Like the words had weight.":
            $ bond["mina"] += 1
            mina "You understand. Words aren't just decoration."
            
        "Kit's right - there's something honest about acknowledging the outside world.":
            $ bond["kit"] += 1
            kit "Finally, someone who isn't afraid of a little darkness."
            
        "Mara's ending gave me chills. Who exactly might be listening?":
            $ bond["mara"] += 1
            $ hub_pressure += 1  # First subtle increase
            mara "Just a feeling I've been having lately..."
            mara "Like we're being... observed."
    
    # End of session
    june "Well, I think that's a wonderful start to our semester!"
    june "Same time next week, everyone?"
    
    hide june
    hide mina  
    hide kit
    hide mara
    
    "As the group packs up, you feel something you hadn't expected."
    "A sense that this might be more than just a poetry club."
    "But what exactly? You can't quite put your finger on it."
    
    # Transition to individual conversations
    call after_club_conversations
    return

# Brief individual character moments
label after_club_conversations:
    "As everyone prepares to leave, you have a moment to talk with someone individually."
    
    menu:
        "Approach June about the club's history":
            call talk_june_history
            
        "Ask Mina about her poetry collection":
            call talk_mina_collection
            
        "Inquire about Kit's zine":
            call talk_kit_zine
            
        "Follow up on Mara's comment about being observed":
            call talk_mara_observation
    
    "The classroom empties, but something lingers in the air."
    "A feeling that this is just the beginning."
    
    # Set up for next session
    "Next Tuesday can't come soon enough."
    
    # Transition to Phase 2: Meta Horror Introduction
    call week_two_transition
    return

# Week 2: The first meta-horror elements emerge
label week_two_transition:
    scene black
    "One week later..."
    "You've been thinking about the poetry club constantly."
    "Something about those conversations felt... significant."
    "Like you were being watched. Evaluated."
    
    scene bg hallway
    "Walking to your next class, you run into someone new."
    
    # The Try Again Trap - signature mechanic introduction
    call serena_trap_scene
    
    # After the trap, return to normal flow
    "The rest of the week passes normally."
    "But you can't shake the feeling that something has changed."
    "Something about the way words feel in your mouth."
    "The way conversations seem to... matter more than they should."
    
    # Check if player has triggered meta-awareness
    if reload_count >= 2:
        call early_meta_awareness
    else:
        call normal_progression
    
    return

label early_meta_awareness:
    "You've been noticing things."
    "Small inconsistencies. Moments that feel... edited."
    "Like someone is standing behind you, pencil in hand."
    
    # First blue-pencil marginalia
    call show_marginalia("Pay attention.")
    
    "Was that... a whisper?"
    "Or just your imagination?"
    return

label normal_progression:
    "Tuesday arrives again, and with it, another poetry club meeting."
    "You're looking forward to seeing everyone."
    "Especially after that strange encounter with Serena."
    
    # Evening mailbag check
    call evening_mailbag
    call check_mailbag_behavior
    
    "As you close the mailbag, you wonder..."
    "Who exactly is writing these letters?"
    "And how do they know so much about what happens in the poetry club?"
    
    # Phase 3: Advanced Meta Mechanics kick in
    call phase_three_escalation
    
    return

# Phase 3: The meta-horror intensifies
label phase_three_escalation:
    # Check for advanced mechanic triggers
    call escalate_hub_intervention
    call check_fake_traceback_conditions
    call apply_drift_effects
    
    # Hub becomes more sophisticated
    if hub_pressure >= 40:
        call hub_meta_commentary
        
        "The blue-pencil marks are appearing more frequently now."
        "In the margins of your thoughts."
        "Correcting. Always correcting."
        
        if reload_count >= 5:
            call visual_breakdown_sequence
            call hub_speak("You see? This is what optimization does to a story.")
    
    # Fake traceback deployment
    if editorial_pressure >= 25 and not fake_traceback_used:
        "Something feels unstable about the very fabric of the game."
        call trigger_fake_traceback
    
    # Haunted save activation
    if hub_pressure >= 50:
        call check_haunted_save_activation
        
        if haunted_slot_active:
            call show_marginalia("Save often. You'll need it.")
            hub "{color=#2B68C5}Some memories are preserved in amber.{/color}"
            hub "{color=#2B68C5}Others... drift away.{/color}"
    
    # Progressive drift
    if drift_intensity >= 0.6:
        "The classroom itself seems less stable now."
        "Edges blur. Colors bleed."
        "Like someone is erasing and redrawing everything in real-time."
        
        call apply_misregistration
    
    # Hub philosophy emerges
    if hub_pressure >= 60:
        call hub_philosophy
    
    # Return to normal... for now
    "But for now, the poetry club continues."
    "Even as the walls of reality grow thin."
    
    return

label talk_june_history:
    show june neutral at center
    $ attn["june"] += 2
    
    leo "June, how long has the Blue Pencil Poetry Club been around?"
    
    june "Oh, just since last year! I started it because I felt like our school needed more... creative spaces."
    june "Places where people could express themselves authentically."
    
    $ bond["june"] += 1
    june "Though I have to admit, sometimes I feel like the club has taken on a life of its own."
    june "Like it's become something bigger than I originally planned."
    
    leo "What do you mean?"
    
    june "Well, look at today! That collaborative poem felt so... intentional. Almost like it was meant to happen that way."
    june "Like someone was guiding the words."
    
    hide june
    return

label talk_mina_collection:
    show mina neutral at center
    $ attn["mina"] += 2
    
    leo "You mentioned collecting verses. What's that like?"
    
    mina "I write down every meaningful line I encounter. Books, conversations, even fragments overheard in hallways."
    mina "Poetry is everywhere, Leo. Most people just don't notice."
    
    $ bond["mina"] += 1
    mina "But lately, I've been noticing... patterns. Repetitions across different sources."
    mina "As if the same hand is editing multiple voices."
    
    leo "That's... oddly specific."
    
    mina "Words have fingerprints, Leo. And I'm getting very good at recognizing handwriting."
    
    hide mina
    return

label talk_kit_zine:
    show kit skeptical at center
    $ attn["kit"] += 2
    
    leo "Tell me about 'Ink Rebellion.' What kind of stuff do you publish?"
    
    kit "Real talk. No sugar-coating, no pretense. Just honest words about honest feelings."
    kit "Anger, disappointment, the way adults lie to make everything seem okay."
    
    $ bond["kit"] += 1
    kit "But here's the weird thing - lately my articles keep getting... revised."
    kit "Not by me. Like someone else is holding the pencil."
    
    leo "Revised how?"
    
    kit "Softened. Made 'nicer.' All my sharp edges filed down."
    kit "As if someone thinks readers can't handle the truth."
    
    hide kit
    return

label talk_mara_observation:
    show mara worried at center
    $ attn["mara"] += 2
    $ hub_pressure += 1
    
    leo "What did you mean about being observed?"
    
    mara "You felt it too, didn't you? During the poem?"
    mara "Like there was an extra presence in the room. Someone listening very carefully."
    
    $ bond["mara"] += 1
    mara "As treasurer, I notice things. Numbers that don't add up. Patterns in the budget."
    mara "Someone's been... editing our paperwork."
    
    leo "Editing how?"
    
    mara "Small corrections. Improvements. As if someone thinks our math isn't quite right."
    mara "But Leo... what if they're not trying to help us?"
    mara "What if they're trying to fix us?"
    
    hide mara
    return
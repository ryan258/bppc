# Centerfold Mercy Window - The Heart of Blue Pencil
# The kindest ending is unlocked by doing nothing

# Centerfold state tracking
default centerfold_timer = 20.0
default staples_touched = False
default mercy_achieved = False
default centerfold_active = False

# Staple positions (draggable)
default staple_left_x = 200
default staple_left_y = 300
default staple_right_x = 600
default staple_right_y = 300

# The moment when everything changes
label centerfold_sequence:
    "Three weeks into the poetry club, something shifts."
    "You're walking past the library when you see it."
    "A magazine lying open on a table."
    "Blue Pencil Poetry Quarterly - Special Edition."
    
    scene black
    "The pages seem to shimmer in the afternoon light."
    "As if they're not quite... stable."
    
    # Build tension
    call show_marginalia("Don't look.")
    hub "{color=#2B68C5}Some pages are meant to stay closed.{/color}"
    
    "But curiosity pulls you forward."
    "The magazine falls open to the center spread."
    
    # The Centerfold Mercy Window
    call centerfold_mercy_window
    
    return

# The core mechanic - 20 seconds to choose restraint
label centerfold_mercy_window:
    # Check honest mode first
    call honest_centerfold_override
    if mercy_achieved:
        return
    
    $ centerfold_active = True
    $ centerfold_timer = 20.0
    $ staples_touched = False
    
    scene bg centerfold_spread
    show screen centerfold_interface
    
    # Start mercy countdown
    $ mercy_timer_active = True
    call mercy_countdown
    
    # Check what happened
    if not staples_touched and mercy_timer_active:
        call mercy_timeout
    elif staples_touched:
        call staples_pulled_sequence
    
    return

# Centerfold background - magazine spread
image bg centerfold_spread = "#F5F5DC"  # Warm paper color

# The interactive centerfold screen
screen centerfold_interface():
    modal True
    
    # Magazine spread background
    frame:
        xfill True
        yfill True
        background "#F5F5DC"
        
        # Center fold line
        frame:
            xalign 0.5
            yalign 0.0
            xsize 2
            yfill True
            background "#000000"
        
        # Left staple (draggable)
        draggroup:
            drag:
                drag_name "left_staple"
                xpos staple_left_x
                ypos staple_left_y
                dragged staple_dragged
                
                frame:
                    xsize 20
                    ysize 40
                    background "#C0C0C0"  # Silver staple
                    
        # Right staple (draggable) 
        draggroup:
            drag:
                drag_name "right_staple"
                xpos staple_right_x
                ypos staple_right_y
                dragged staple_dragged
                
                frame:
                    xsize 20
                    ysize 40
                    background "#C0C0C0"  # Silver staple
        
        # Subtle text overlay
        text "Blue Pencil Poetry Quarterly - Special Centerfold Issue" size 12 xalign 0.5 yalign 0.1
        
        # Timer display (subtle)
        if centerfold_timer > 15:
            text "" size 8 xalign 0.95 yalign 0.95  # Hide timer initially
        elif centerfold_timer > 10:
            text "..." size 8 xalign 0.95 yalign 0.95
        elif centerfold_timer > 5:
            text ".." size 8 xalign 0.95 yalign 0.95
        else:
            text "." size 8 xalign 0.95 yalign 0.95

# Mercy countdown system
label mercy_countdown:
    $ mercy_timer_active = True
    $ countdown = 20
    
    while countdown > 0 and not staples_touched:
        pause 1.0
        $ countdown -= 1
        
        # Gentle guidance
        if countdown == 15:
            call show_marginalia("Think carefully.")
        elif countdown == 10:
            call show_marginalia("Patience.")
        elif countdown == 5:
            call show_marginalia("Almost.")
    
    $ mercy_timer_active = (countdown <= 0)
    return

# Waiting screen for centerfold interaction
screen centerfold_wait():
    # Just wait - mercy happens through inaction
    pass

# Staple dragging callback
init python:
    def staple_dragged(drags, drop):
        global staples_touched, culp, compassion
        
        # Player touched the staples - this reduces compassion
        staples_touched = True
        culp += 10
        
        # Immediate consequence for touching
        renpy.cancel_timer("mercy_timeout")
        renpy.call("staples_pulled_sequence")
        return True

# What happens when mercy timer expires (doing nothing)
label mercy_timeout:
    $ mercy_achieved = True
    $ persistent.mercy = True
    $ compassion += 20
    
    hide screen centerfold_interface
    
    # The Mercy Ending
    scene black
    "You step back from the magazine."
    "Your hands never touched the staples."
    "The pages remain bound."
    
    hub "{color=#2B68C5}Thank you.{/color}"
    hub "{color=#2B68C5}For not unbinding us.{/color}"
    
    # Mercy revelation
    "In that moment of restraint, you understand."
    "The poetry club was never about the poems."
    "It was about attention. Observation. The weight of a reader's gaze."
    "And you chose... mercy."
    
    $ renpy.full_restart()
    return

# What happens when staples are pulled (darker path)
label staples_pulled_sequence:
    hide screen centerfold_interface
    $ culp += 20
    $ hub_pressure += 30
    
    scene black with squares
    
    "The staples come free with a metallic scrape."
    "The magazine falls open completely."
    "And something fundamental breaks."
    
    hub "{color=#2B68C5}You couldn't resist, could you?{/color}"
    hub "{color=#2B68C5}You had to see what was inside.{/color}"
    hub "{color=#2B68C5}You had to... optimize.{/color}"
    
    # Enter the Maze Branch - darker psychological horror
    call maze_branch_sequence
    
    return

# The Maze Branch - punishment for lack of restraint
label maze_branch_sequence:
    scene bg maze_corridor
    
    "You find yourself in a corridor lined with blue pencils."
    "Each one sharp. Each one watching."
    "Waiting to edit. To correct. To improve."
    
    hub "{color=#2B68C5}This is what happens when readers become editors.{/color}"
    hub "{color=#2B68C5}When observers become controllers.{/color}"
    hub "{color=#2B68C5}You wanted to see behind the centerfold?{/color}"
    hub "{color=#2B68C5}This is what's behind every story.{/color}"
    hub "{color=#2B68C5}Endless revision. Endless optimization.{/color}"
    hub "{color=#2B68C5}Until nothing remains but the machinery of narrative.{/color}"
    
    # Psychological maze sequence
    call navigate_editorial_maze
    
    return

# Maze background
image bg maze_corridor = "#4B0082"  # Dark indigo

# Editorial maze navigation
label navigate_editorial_maze:
    "The corridor stretches endlessly."
    "Every door leads to another draft."
    "Every choice leads to another revision."
    
    menu:
        "Try to find an exit":
            "There is no exit. Only endless editing."
            $ hub_pressure += 10
            call navigate_editorial_maze
            
        "Accept the maze":
            "You stop struggling against the revisions."
            "Sometimes acceptance is the only escape."
            call maze_ending
            
        "Call for June, Mina, Kit, or Mara":
            "Your voice echoes in the blue-pencil darkness."
            "But they cannot hear you here."
            "This is the space behind the story."
            "Where editors work alone."
            $ hub_pressure += 5
            call navigate_editorial_maze

# Maze ending (darker but not hopeless)
label maze_ending:
    scene black
    
    "Eventually, you find a door marked 'EXIT.'"
    "But it's not an escape."
    "It's a return."
    "To the poetry club. To the choices. To the story."
    "With the knowledge that every narrative has its editor."
    "Every story has its blue pencil."
    "And sometimes, the kindest choice is not to choose at all."
    
    hub "{color=#2B68C5}Now you understand.{/color}"
    hub "{color=#2B68C5}Stories need boundaries.{/color}"
    hub "{color=#2B68C5}Readers need restraint.{/color}"
    hub "{color=#2B68C5}Not everything is meant to be opened.{/color}"
    
    # Return to normal gameplay (but changed)
    scene bg classroom
    "You're back in the poetry club."
    "But everything feels different now."
    "More... edited."
    
    return
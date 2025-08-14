
# Splash screen with content note
screen splashscreen():
    tag menu
    add "black"
    text "This story depicts anxiety, obsessive behavior, and depression. No graphic self-harm, no instructions. If you need support, consider pausing and seeking local resources." xalign 0.5 yalign 0.5

# Main menu
screen navigation():
    vbox:
        style_prefix "navigation"
        xpos gui.navigation_xpos
        ypos gui.navigation_ypos
        spacing gui.navigation_spacing
        if main_menu:
            textbutton _("Start") action Start()
        else:
            textbutton _("Save") action ShowMenu("save")
            textbutton _("Load") action ShowMenu("load")
        textbutton _("Legal") action ShowMenu("legal")
        textbutton _("Preferences") action ShowMenu("preferences")
        textbutton _("Quit") action Quit(confirm=not main_menu)

screen legal():
    tag menu
    add "white"
    vbox:
        xalign 0.5
        yalign 0.5
        spacing 20
        text "Privacy & Files"
        text "Blue Pencil does not read, write, or delete files outside its installation and save folders. All “file” interactions are simulated within the game. No personal data is collected or transmitted."
        textbutton "Back" action MainMenu()

# Game script
label start:
    scene black
    with fade
    show screen splashscreen
    with fade
    pause 5.0
    hide screen splashscreen
    with fade
    jump main_menu_screen

label main_menu_screen:
    scene black
    with fade
    if persistent.mercy_ending:
        "Thank you for closing the book."
    else:
        "Welcome to Blue Pencil."
    show screen navigation
    with fade
    jump game_start

label game_start:
    jump serena_scene

label serena_scene:
    $ persistent.serena_reloads = getattr(persistent, 'serena_reloads', 0) + 1
    if persistent.serena_reloads > 3 and not persistent.honest_mode:
        # Show visual changes (gutters tighten, balloon outlines thin)
        "The gutters tighten, the balloon outlines thin."
    else:
        "This is the Serena scene."

    menu:
        "What do you do?"
        "Choice 1":
            "You picked choice 1."
        "Choice 2":
            "You picked choice 2."

    "The scene ends."
    jump centerfold_scene

label centerfold_scene:
    scene black
    with fade
    "You've reached the centerfold."
    show screen centerfold_screen
    with fade
    # Timer for Mercy Ending
    timer 20.0 action Jump("mercy_ending")
    "You can either wait or interact with the centerfold."

screen centerfold_screen():
    tag menu
    add "white"
    drag:
        drag_name "centerfold"
        child Solid("#ff00ff", xsize=200, ysize=300)
        xalign 0.5
        yalign 0.5
        droppable True
        dropped Jump("maze_scene")

label mercy_ending:
    play sound "audio/mercy_low_pass.ogg"
    $ persistent.mercy_ending = True
    "You have chosen mercy. The story ends here."
    return

label maze_scene:
    "You've entered the maze."
    jump mailbag_scene

label mailbag_scene:
    $ persistent.last_mailbag_visit = renpy.game.getTime()
    "You've opened the mailbag."
    if persistent.serena_reloads > 3:
        "There's a letter here about being indecisive."
    if persistent.mercy_ending:
        "There's a thank you card."
    if persistent.last_mailbag_visit and renpy.game.getTime() - persistent.last_mailbag_visit > 60:
        "There's a dusty letter that looks like it's been here a while."
    return


# Placeholder for Honest Mode
default persistent.honest_mode = False

# Placeholder for Mercy Ending
default persistent.mercy_ending = False

# Placeholder for reset switch
init python:
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--reset-persistent", action="store_true")
    args = parser.parse_args()
    if args.reset_persistent:
        persistent.honest_mode = False
        persistent.mercy_ending = False

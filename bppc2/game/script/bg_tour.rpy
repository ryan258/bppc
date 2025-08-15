label bg_tour:
    # List your background names (as declared: image bg <name> = ...)
    $ bgs = ["cafeteria", "classroom", "empty_room", "hallway", "library"]

    python:
        for b in bgs:
            # Clear to a new scene, show the bg with the transform, and transition.
            renpy.scene()
            renpy.show("bg " + b, at_list=[kb_slow])  # remove at_list if you don't want the slow zoom
            renpy.with_statement(tdiss)

            # Say a line (no character = narrator)
            renpy.say(None, f"Showing {b}.")

            renpy.pause(0.8)

    return

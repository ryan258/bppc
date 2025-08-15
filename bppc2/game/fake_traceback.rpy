# Fake Traceback System - Simulated Error Screen
# Creates realistic-looking Ren'Py error without actually crashing

# Traceback usage tracking
default fake_traceback_used = 0
default fake_traceback_available = True

# Fake error screen that looks like real Ren'Py traceback
screen fake_traceback():
    modal True
    
    frame:
        background "#000000"
        xfill True
        yfill True
        
        vbox:
            text "{color=#FF0000}I'm sorry, but an uncaught exception occurred.{/color}" size 16
            null height 10
            text "While running game code:"
            text "  File \"game/script.rpy\", line 157, in script"
            text "    hub \"{{color=#2B68C5}}Stop trying to control the narrative.{{/color}}\""
            text "  File \"game/meta_systems.rpy\", line 23, in script"
            text "    $ editorial_pressure += reality_breach"
            text "  File \"game/meta_systems.rpy\", line 23, in <module>"
            text "    $ editorial_pressure += reality_breach"
            text "      ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^"
            text "{color=#FF0000}NameError: name 'reality_breach' is not defined{/color}"
            null height 10
            text "-- Full Traceback ------------------------------------------------------------"
            null height 10
            text "Traceback (most recent call last):"
            text "  File \"renpy/execution.py\", line 1423, in run"
            text "    node.execute()"
            text "  File \"renpy/ast.py\", line 1187, in execute" 
            text "    renpy.python.py_exec_bytecode(self.code.bytecode, self.hide, store=self.store)"
            text "  File \"renpy/python.py\", line 1260, in py_exec_bytecode"
            text "    exec(bytecode, globals, locals)"
            text "  File \"game/meta_systems.rpy\", line 23, in <module>"
            text "    $ editorial_pressure += reality_breach"
            text "      ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^"
            text "{color=#FF0000}NameError: name 'reality_breach' is not defined{/color}"
            null height 10
            text "Windows-11-10.0.26100-SP0 AMD64"
            text "Ren'Py 8.4.1.25072401"
            text "Blue Pencil Poetry Club 1.0"
            null height 20
            hbox:
                textbutton "Copy" action Function(fake_copy_action)
                textbutton "Continue" action Function(fake_continue_action)

# Fake traceback trigger conditions
label trigger_fake_traceback:
    if fake_traceback_available and fake_traceback_used < 2:
        $ fake_traceback_used += 1
        call show_fake_traceback
    return

# Show the fake traceback screen
label show_fake_traceback:
    # Brief moment of "real" error feel
    $ renpy.pause(0.1, hard=True)
    
    show screen fake_traceback
    $ renpy.pause(hard=True)
    
    return

# Fake copy action (does nothing but feels real)
init python:
    def fake_copy_action():
        # Pretend to copy error to clipboard
        renpy.notify("Error copied to clipboard.")
        return

    def fake_continue_action():
        # Dismiss the fake traceback
        renpy.hide_screen("fake_traceback")
        renpy.jump("after_fake_traceback")

# Continuation after fake traceback
label after_fake_traceback:
    scene black
    
    # Hub commentary on the "error"
    hub "{color=#2B68C5}Technical difficulties.{/color}"
    hub "{color=#2B68C5}You're pushing too hard against the boundaries.{/color}"
    hub "{color=#2B68C5}Some variables are not meant to be defined.{/color}"
    
    $ hub_pressure += 20
    $ drift_intensity += 0.3
    
    # Brief pause before returning to normal
    pause 2.0
    
    # Return to scene
    scene bg classroom
    "Everything returns to normal."
    "But you can't shake the feeling that something fundamental just broke."
    "And then... mended itself."
    
    return

# Strategic deployment of fake traceback
label check_fake_traceback_conditions:
    # Trigger under specific meta-awareness conditions
    if (hub_pressure >= 40 and reload_count >= 5 and 
        fake_traceback_used == 0 and 
        not persistent.honest_mode):
        
        "Suddenly, the screen flickers."
        call trigger_fake_traceback
        
    elif (editorial_pressure >= 25 and fake_traceback_used == 1 and
          not persistent.honest_mode):
        
        "The text begins to stutter and glitch."
        call trigger_fake_traceback
    
    return

# Emergency fake traceback for extreme optimization
label emergency_fake_traceback:
    if reload_count >= 10 and fake_traceback_used < 2:
        "The game itself seems to be breaking down."
        call trigger_fake_traceback
    return
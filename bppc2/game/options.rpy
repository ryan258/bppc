# Blue Pencil Poetry Club - Configuration

# Game identity and build settings
define config.name = "Blue Pencil Poetry Club"
define config.version = "1.0.0"
define build.directory_name = "BPPC"
define config.save_directory = "BPPC"

# Display settings
define config.screen_width = 1920
define config.screen_height = 1080
define config.window_title = "Blue Pencil Poetry Club"
# define config.window_icon = "gui/window_icon.png"  # Disabled until icon asset created

# Performance and behavior
define config.check_conflicting_properties = True
define config.quit_action = Quit(confirm=False)
define config.rollback_enabled = True
define config.hard_rollback_limit = 100

# Build configuration
init python:
    build.classify('**~', None)
    build.classify('**.rpy', None)
    build.classify('**.rpyc', None)
    build.classify('**.rpa', None)
    
    # Archive assets for distribution
    build.archive("game_data", "all")

# Persistent variables for meta-horror and accessibility
default persistent.halftone = False
default persistent.reduce_drift = False
default persistent.dyslexia_font = False
default persistent.honest_mode = False
default persistent.mercy = False
default persistent.haunted_save = False
default persistent.streamer_mode = False
default persistent.color_safe = False
default persistent.reduce_motion = False
default persistent.high_contrast = False

screen preferences():
    tag menu
    vbox:
        text "Preferences"

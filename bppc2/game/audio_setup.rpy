define config.has_voice = True

init python:
    # Extra channels
    renpy.music.register_channel("ambience", mixer="sfx", loop=True, stop_on_mute=True)
    renpy.music.register_channel("ui", mixer="sfx", loop=False, buffer_queue=True)

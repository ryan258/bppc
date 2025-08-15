# Blue Pencil Audio System - Authentic 1960s Soundscape
# Diner ambience, pencil scratch, mercy effects

# Audio channel definitions
define audio.ambient = "ambient"
define audio.sfx = "sfx" 
define audio.hub_voice = "voice"

# Audio file definitions (using existing files in game/audio/)
define audio.diner_loop = "audio/diner_loop.ogg"
define audio.pencil_scratch = "audio/pencil_scratch.ogg"
define audio.mercy_lowpass = "audio/mercy_low_pass.ogg"

# Audio state tracking
default audio_enabled = True
default sfx_volume = 0.7
default ambient_volume = 0.4
default voice_volume = 0.8

# Initialize audio system
label init_audio:
    # Start ambient diner loop
    if audio_enabled and not persistent.honest_mode:
        play ambient diner_loop loop volume ambient_volume
    
    return

# Pencil scratch on reload (signature sound)
label play_pencil_scratch:
    if audio_enabled and not persistent.honest_mode:
        play sfx pencil_scratch volume (sfx_volume * 0.3)  # -12dB as per spec
        
        # Subtitle for accessibility
        $ renpy.notify("[pencil scratch]")
    
    return

# Mercy low-pass effect (800ms fade)
label play_mercy_effect:
    if audio_enabled:
        # Low-pass filter simulation with volume fade
        play ambient mercy_lowpass volume (ambient_volume * 0.5)
        $ renpy.pause(0.8)
        stop ambient fadeout 0.8
        
        # Subtitle for accessibility
        $ renpy.notify("[gentle fade]")
    
    return

# Hub voice effects (fluorescent hum simulation)
label play_hub_ambience:
    if audio_enabled and not persistent.honest_mode:
        # Subtle electronic hum during Hub scenes
        play hub_voice "<silence 0.1>" loop volume (voice_volume * 0.2)
        
        # Subtitle for accessibility
        $ renpy.notify("[fluorescent hum]")
    
    return

# Stop Hub ambience
label stop_hub_ambience:
    stop hub_voice fadeout 0.5
    return

# Audio integration with reload detection
label audio_reload_response:
    if reload_count >= 1:
        call play_pencil_scratch
        
        # Escalating audio distortion with more reloads
        if reload_count >= 3:
            $ ambient_volume *= 0.9  # Slight volume reduction
            play ambient diner_loop loop volume ambient_volume
        
        if reload_count >= 5:
            # Audio starts to stutter/distort
            play ambient diner_loop loop volume (ambient_volume * 0.7)
            call play_hub_ambience
    
    return

# Audio for centerfold sequence
label centerfold_audio:
    if audio_enabled:
        # Silence builds tension
        stop ambient fadeout 2.0
        $ renpy.pause(2.0)
        
        # Subtle heartbeat-like rhythm
        play sfx "<silence 1.0>"
        $ renpy.notify("[tension builds]")
    
    return

# Audio for mercy achievement
label mercy_audio:
    if audio_enabled:
        call play_mercy_effect
        
        # Gentle resolution
        $ renpy.pause(1.0)
        play ambient diner_loop loop volume (ambient_volume * 0.6)
        $ renpy.notify("[peaceful resolution]")
    
    return

# Audio for maze branch (editorial horror)
label maze_audio:
    if audio_enabled:
        # Harsh stop
        stop ambient
        stop sfx
        
        # Distorted, uncomfortable ambience
        play ambient diner_loop loop volume (ambient_volume * 1.5) pitch 0.8
        call play_hub_ambience
        
        $ renpy.notify("[dissonant atmosphere]")
    
    return

# Audio accessibility controls
screen audio_preferences():
    frame:
        xalign 0.5
        yalign 0.5
        
        vbox:
            text "Audio Settings" size 24
            null height 20
            
            text "Master Volume Controls:"
            bar value Preference("master volume") xsize 300
            
            text "Ambient Volume:"
            bar value FieldValue(store, "ambient_volume", 1.0) xsize 300
            
            text "Sound Effects Volume:"
            bar value FieldValue(store, "sfx_volume", 1.0) xsize 300
            
            text "Voice Volume:"
            bar value FieldValue(store, "voice_volume", 1.0) xsize 300
            
            null height 20
            textbutton "Enable Audio Subtitles" action ToggleVariable("show_audio_subtitles")
            textbutton "Disable All Audio" action ToggleVariable("audio_enabled")
            
            null height 20
            textbutton "Return" action Return()

# Integrate audio with existing systems
label integrate_audio_with_meta:
    # Called from meta_systems.rpy
    if hub_spoken:
        call play_hub_ambience
    
    if reload_count >= 1:
        call audio_reload_response
    
    return

# Audio cleanup for honest mode
label honest_mode_audio:
    if persistent.honest_mode:
        stop ambient
        stop sfx
        stop hub_voice
        
        # Play clean ambient only
        play ambient diner_loop loop volume (ambient_volume * 0.8)
    
    return
# Blue Pencil Poetry Club - Assets Catalog

**Complete asset list for production-ready build**

All assets should be placed in the `game/` directory following Ren'Py conventions.

---

## Visual Assets

### Character Sprites

**Required Files:**
```
game/images/characters/
├── june_neutral.png        (Standing pose, milkshake pink theme)
├── june_happy.png          (Optimistic expression)
├── june_worried.png        (Concerned about changes)
├── mina_neutral.png        (Standing pose, pool blue theme)
├── mina_intense.png        (Analytical, focused expression)
├── kit_neutral.png         (Standing pose, purple theme)
├── kit_skeptical.png       (Questioning authority)
├── kit_angry.png           (Rebellion against editing)
├── mara_neutral.png        (Standing pose, darker gold theme)
├── mara_knowing.png        (Meta-aware expression)
├── mara_worried.png        (Concerned about being watched)
└── leo_silhouette.png      (Player character shadow only)
```

**Specifications:**
- Format: PNG with transparency
- Size: 1080px height (standard Ren'Py character height)
- Style: 1960s teen aesthetic, clean vector art
- Color themes match character definitions in script.rpy

**Code Integration:**
```python
# In script.rpy, update character definitions:
define june = Character("June", color="#FFB6C1", image="june")
define mina = Character("Mina", color="#2B68C5", image="mina")
define kit = Character("Kit", color="#800080", image="kit")
define mara = Character("Mara", color="#B8860B", image="mara")
```

### Background Images

**Required Files:**
```
game/images/backgrounds/
├── classroom.jpg           (1960s high school classroom)
├── library.jpg             (School library with magazine table)
├── hallway.jpg             (School corridor)
├── cafeteria.jpg           (Background for mailbag scenes)
├── empty_room.jpg          (Haunted interstitial scene)
└── black.jpg               (Pure black for dramatic moments)
```

**Specifications:**
- Format: JPG for backgrounds (smaller file size)
- Resolution: 1920x1080 (16:9 aspect ratio)
- Style: Authentic 1960s institutional aesthetic
- Lighting: Fluorescent-lit, slightly desaturated

**Code Integration:**
Already defined in script.rpy:
```python
scene bg classroom
scene bg library
scene bg black
```

### UI Graphics

**Required Files:**
```
game/images/ui/
├── gui/
│   ├── textbox.png         (Dialogue box design)
│   ├── button_idle.png     (Menu button idle state)
│   ├── button_hover.png    (Menu button hover state)
│   ├── button_selected.png (Menu button selected state)
│   ├── slider_idle.png     (Accessibility slider design)
│   ├── slider_hover.png    (Slider hover state)
│   └── frame.png           (Menu frame background)
├── marginalia/
│   ├── blue_pencil_1.png   (Editorial mark variant 1)
│   ├── blue_pencil_2.png   (Editorial mark variant 2)
│   ├── blue_pencil_3.png   (Editorial mark variant 3)
│   └── correction_mark.png (Editing notation)
└── effects/
    ├── drift_overlay.png   (Visual corruption overlay)
    ├── halftone_pattern.png (Printing effect)
    └── staple_cursor.png   (Custom cursor for centerfold)
```

**Code Integration:**
Update gui.rpy:
```python
define gui.textbox_background = "gui/textbox.png"
define gui.button_idle_background = "gui/button_idle.png"
```

### Centerfold Assets

**Required Files:**
```
game/images/centerfold/
├── magazine_spread.jpg     (Full centerfold background - 1920x1080)
├── staple_1.png           (Draggable staple top-left)
├── staple_2.png           (Draggable staple top-right)
├── staple_3.png           (Draggable staple bottom-left)
├── staple_4.png           (Draggable staple bottom-right)
├── poetry_text_layer.png  (Typography overlay with transparency)
└── magazine_logo.png      (Blue Pencil Poetry Quarterly masthead)
```

**Specifications:**
- magazine_spread.jpg: Vintage magazine aesthetic, beige/cream tones
- staples: 32x32px PNG with transparency, metallic appearance
- High-resolution for full-screen display

**Code Integration:**
Update centerfold_mercy.rpy:
```python
scene centerfold_spread:
    "centerfold/magazine_spread.jpg"
    "centerfold/poetry_text_layer.png"

image staple_1 = "centerfold/staple_1.png"
# etc for all staples
```

---

## Audio Assets

### Music

**Required Files:**
```
game/audio/music/
├── diner_loop.ogg         (Ambient 1960s diner atmosphere)
├── mercy_lowpass.ogg      (Low-pass filtered version for mercy ending)
└── silence.ogg            (Pure silence for dramatic pauses)
```

**Specifications:**
- Format: OGG Vorbis (Ren'Py standard)
- Sample Rate: 44.1kHz
- Bitrate: 128kbps (good quality, reasonable size)
- diner_loop: 2-3 minute seamless loop, gentle background ambience
- Volume levels pre-mastered for -18dB average

**Code Integration:**
Update audio_system.rpy:
```python
define audio.diner_loop = "audio/music/diner_loop.ogg"
define audio.mercy_lowpass = "audio/music/mercy_lowpass.ogg"
```

### Sound Effects

**Required Files:**
```
game/audio/sfx/
├── pencil_scratch.ogg     (Quick pencil on paper sound)
├── page_turn.ogg          (Magazine page turning)
├── staple_pull.ogg        (Metal staple being removed)
├── fluorescent_hum.ogg    (Subtle electrical hum)
├── typewriter_ding.ogg    (1960s typewriter bell)
└── gentle_fade.ogg        (Soft audio transition)
```

**Specifications:**
- Format: OGG Vorbis
- Duration: 0.5-2 seconds per SFX
- pencil_scratch: -12dB volume as specified
- High-quality foley recording, authentic 1960s sounds

**Code Integration:**
Update audio_system.rpy:
```python
define audio.pencil_scratch = "audio/sfx/pencil_scratch.ogg"
define audio.page_turn = "audio/sfx/page_turn.ogg"
# etc for all SFX
```

---

## Fonts

**Required Files:**
```
game/fonts/
├── DejaVuSans.ttf         (Main UI font - already included in Ren'Py)
├── OpenDyslexic3-Regular.ttf (Accessibility font)
├── typewriter_1960s.ttf   (Period-appropriate typewriter font)
└── handwriting_blue.ttf   (Blue pencil marginalia font)
```

**Code Integration:**
Update accessibility.rpy:
```python
define gui.default_font = "fonts/DejaVuSans.ttf"
define gui.dyslexia_font = "fonts/OpenDyslexic3-Regular.ttf"
define gui.typewriter_font = "fonts/typewriter_1960s.ttf"
define gui.marginalia_font = "fonts/handwriting_blue.ttf"
```

---

## Configuration Files

### GUI Configuration

**File to Update: `game/gui.rpy`**

Add these definitions:
```python
# Color palette
define gui.text_color = '#402020'
define gui.name_text_color = '#2B68C5'
define gui.interface_text_color = '#402020'

# 1960s aesthetic sizing
define gui.text_size = 22
define gui.name_text_size = 24
define gui.interface_text_size = 18

# Custom UI elements
define gui.textbox_height = 185
define gui.name_xpos = 240
define gui.name_ypos = -3
define gui.text_xpos = 268
define gui.text_ypos = 50
define gui.text_width = 1176
```

### Options Configuration

**File to Update: `game/options.rpy`**

Add these settings:
```python
define config.name = "Blue Pencil Poetry Club"
define config.version = "1.0.0"

# Build configuration
define build.classify('**~', None)
define build.classify('**.rpy', None)
define build.classify('**.rpyc', None)

# Archive configuration for release
define build.archive("assets", "all")
define build.archive("scripts", "all")

# Platform-specific builds
define build.mac_info_plist = {
    "CFBundleDisplayName": "Blue Pencil Poetry Club"
}
```

---

## Asset Production Guidelines

### Character Sprites
- **Style:** Clean vector art with 1960s teen aesthetic
- **Poses:** Standing neutral position with subtle personality cues
- **Expressions:** Clear emotional states that match dialogue
- **Clothing:** Period-appropriate school attire (sweaters, skirts, slacks)
- **Colors:** Match the character color themes defined in code

### Backgrounds
- **Reference:** 1960s institutional architecture and design
- **Lighting:** Fluorescent-lit classrooms, natural library lighting
- **Details:** Period-appropriate furniture, blackboards, book displays
- **Resolution:** High enough for 1080p display without pixelation

### Audio Design
- **Diner Loop:** Subtle background ambience - conversations, dishes, 1960s atmosphere
- **Pencil Scratch:** Quick, authentic pencil-on-paper sound at -12dB
- **SFX:** All sounds should feel authentic to 1960s school environment
- **Mercy Audio:** Low-pass filtering creates gentle, warm resolution

### UI Elements
- **Textbox:** Clean, readable design that doesn't obstruct character art
- **Buttons:** 1960s-inspired design with clear hover states
- **Marginalia:** Hand-drawn blue pencil marks, various editing notations
- **Accessibility:** High contrast options for all UI elements

---

## File Structure Summary

```
game/
├── images/
│   ├── characters/      (11 sprite files)
│   ├── backgrounds/     (6 background files)
│   ├── ui/
│   │   ├── gui/         (7 UI element files)
│   │   ├── marginalia/  (4 editorial mark files)
│   │   └── effects/     (3 visual effect files)
│   └── centerfold/      (7 magazine spread files)
├── audio/
│   ├── music/           (3 music files)
│   └── sfx/             (6 sound effect files)
├── fonts/               (4 font files)
└── [existing .rpy files remain unchanged]
```

**Total Asset Count:**
- **Visual:** 38 image files
- **Audio:** 9 audio files
- **Fonts:** 4 font files
- **Total:** 51 production assets

---

## Production Priorities

### High Priority (Essential for Release)
1. Character sprites (June, Mina, Kit, Mara expressions)
2. Key backgrounds (classroom, library)
3. Centerfold magazine spread and staples
4. Diner loop ambient music
5. Pencil scratch SFX

### Medium Priority (Polish)
1. UI graphics and custom textbox
2. Additional background variations
3. All SFX for enhanced immersion
4. Visual effect overlays

### Low Priority (Nice to Have)
1. Animated sprite transitions
2. Additional ambient loops
3. Custom cursor designs
4. Extended SFX library

---

## Integration Checklist

- [ ] Update character definitions with image paths
- [ ] Configure GUI with custom graphics
- [ ] Test audio system with all files
- [ ] Verify font loading for accessibility
- [ ] Test centerfold interaction with new assets
- [ ] Build configuration for asset packaging
- [ ] Cross-platform testing with all assets
- [ ] File size optimization for distribution

---

*All assets should maintain the authentic 1960s aesthetic while supporting the meta-horror narrative elements. The goal is a cohesive, immersive experience that feels both period-appropriate and subtly unsettling.*
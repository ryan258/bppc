# Blue Pencil Poetry Club - Development Roadmap

**Status:** ✅ Phase 1 Complete - Character Foundation Established  
**Next Phase:** Meta Horror Introduction (Phase 2)

---

## Current State ✅

- [x] Project compiles and runs without errors
- [x] Core game variables configured (`attn`, `bond`, `drift`, `culp`, `compassion`, `hub_pressure`)
- [x] Persistent variables set up (`mercy`, `honest_mode`, `haunted_save`, etc.)
- [x] Basic GUI framework in place
- [x] Complete Act I opening sequence (87 dialogue blocks, 4 choice menus)
- [x] Content note implementation (accessibility compliant)

---

## Phase 1: Story Foundation (Week 1-2) ✅ COMPLETE

### 1.1 Character Setup ✅ COMPLETE
- [x] Create character definitions (Leo, June, Mina, Kit, Mara)
- [x] Basic character sprites (placeholder silhouettes with distinct colors)
- [x] Character voice/dialogue patterns (documented in character_voices.md)

### 1.2 Act I Implementation ✅ COMPLETE  
- [x] **Scene: Welcome to Blue Pencil Poetry Club**
  - Club introduction with all 4 members
  - Character personality establishment
  - Basic choice mechanics with bond tracking
- [x] **Scene: First Poetry Session**
  - Collaborative poem creation
  - Attention tracking (`attn[name]` increments per dialogue)
  - Bond system introduction with meaningful choices
  - Subtle meta-awareness hints (Mara's "being observed" line)
- [x] **Scene: After-club Conversations**
  - Individual character routes (4 conversation paths)
  - Choice impact on `bond[name]` values
  - Character-specific meta-awareness reveals

### 1.3 Core Mechanics ✅ COMPLETE
- [x] Choice tracking system (bond/attention mechanics working)
- [x] Basic save/load functionality (Ren'Py standard)
- [x] Character positioning and sprite system
- [x] Hub pressure introduction (`hub_pressure` increments on meta choices)

### 🎯 Phase 1 Achievements
- **87 dialogue blocks** with engaging character interactions
- **4 meaningful choice menus** affecting character relationships
- **Complete character establishment** with distinct voices and personalities
- **Meta-awareness foundation** planted through character observations
- **Solid technical base** with no lint errors and stable execution
- **Accessibility compliance** with content note and clear UI

---

## Phase 2: Meta Horror Introduction (Week 3-4) 🎯 NEXT

### 2.1 Editorial Elements
- [ ] Blue-pencil marginalia system
- [ ] **First Hub Intrusion** (gentle, tutorial-style)
- [ ] Reload detection system
- [ ] Basic drift effects (minimal visual wobble)

### 2.2 Try Again Trap Prototype
- [ ] **Serena Exemplar Scene**
  - Converging choice structure
  - Reload tracking (`culp` increment)
  - Visual scarring (gutter tightening)
  - Balloon tail thinning effect

### 2.3 Mailbag System
- [ ] Evening mailbag scenes
- [ ] Behavior reflection in letters
- [ ] Reader response simulation

---

## Phase 3: Advanced Meta Mechanics (Week 5-6)

### 3.1 Haunted Load System
- [ ] Custom load screen implementation
- [ ] Haunted save slot creation
- [ ] 1-2s interstitial scene (empty room + Hub whisper)
- [ ] Seamless return to real save

### 3.2 Fake Traceback
- [ ] In-engine error screen (styled like Ren'Py)
- [ ] Copy & Continue functionality
- [ ] Strategic deployment (1-2 uses max)

### 3.3 Hub Voice Development
- [ ] Clinical, precise dialogue style
- [ ] Escalating pressure system
- [ ] Blue-pencil overwrites

---

## Phase 4: Centerfold & Mercy System (Week 7)

### 4.1 Centerfold Mercy Window
- [ ] Full-screen faux magazine spread
- [ ] Draggable staple mechanics
- [ ] 20-second idle timer
- [ ] **Mercy Ending** (doing nothing)
- [ ] **Maze Branch** (pulling staples)

### 4.2 Compassion System
- [ ] Mercy Window implementation
- [ ] Restraint tracking (`compassion` increments)
- [ ] Alternative path rewards

### 4.3 Title Memory
- [ ] Persistent mercy flag
- [ ] "Thank you for closing the book" addition
- [ ] Post-credits recognition

---

## Phase 5: Polish & Accessibility (Week 8)

### 5.1 Honest Mode
- [ ] Post-credits toggle
- [ ] **Shift+Hold** emergency activation
- [ ] Disable haunt/drift effects
- [ ] Clean save thumbnails

### 5.2 Accessibility Features
- [ ] Text scaling (80-140%)
- [ ] Dyslexia-friendly font toggle
- [ ] Halftone reduction
- [ ] Color-safe palette option
- [ ] Subtitle system for SFX

### 5.3 Audio Implementation
- [ ] Diner loop background music
- [ ] Pencil scratch on reload (-12dB)
- [ ] Mercy low-pass filter effect
- [ ] Fluorescent hum for Hub scenes

---

## Phase 6: Content Complete (Week 9-10)

### 6.1 All Four Acts
- [ ] **Act I:** Welcome to Blue Pencil Poetry Club
- [ ] **Act II:** Routes & Rhymes (apparent agency)
- [ ] **Act III:** Out of Register (drift, converging choices)
- [ ] **Act IV:** Just Mara (Centerfold & Mercy)

### 6.2 Complete Character Arcs
- [ ] June (sunny organizer)
- [ ] Mina (intense collector)
- [ ] Kit (spiky zine kid)
- [ ] Mara (self-aware treasurer)

### 6.3 All Set Pieces
- [ ] Try Again Trap (working)
- [ ] Haunted Load (working)
- [ ] Centerfold Mercy Window (working)
- [ ] Fake Traceback (working)
- [ ] Title Memory (working)

---

## Quality Assurance Milestones

### QA Checkpoint 1 (After Phase 2)
- [ ] 7-minute QA script passes
- [ ] No external file writes
- [ ] Basic meta mechanics functional

### QA Checkpoint 2 (After Phase 4)
- [ ] All endings reachable
- [ ] Mercy timer calibrated (15s/20s/30s variants)
- [ ] Accessibility toggles working

### Final QA (After Phase 6)
- [ ] Full 60-90 minute playthrough
- [ ] All accessibility features verified
- [ ] Cross-platform builds (Win/Mac/Linux)
- [ ] No crashes, no external file access

---

## Technical Priorities

### High Priority
1. **Save System Security** - Never touch OS files
2. **Performance** - 60fps target, shader-free drift
3. **Accessibility** - All features toggleable
4. **Platform Support** - Desktop focus (Win/Mac/Linux)

### Architecture Decisions
- Use ATL transforms for drift effects (no shaders)
- Custom screens for meta elements
- Persistent storage for memory features
- Modular character/scene system

---

## Risk Mitigation

### High Risk Items
- **Centerfold Mechanics** - Complex UI interaction
- **Haunted Load** - Save system manipulation
- **Cross-platform Audio** - Timing precision

### Contingency Plans
- Prototype complex mechanics early
- Fallback to simpler implementations if needed
- Platform-specific testing throughout

---

## Definition of Done

**Ready to Ship When:**
- [ ] All 6 phases complete
- [ ] QA script passes (7-minute critical path)
- [ ] Accessibility checklist verified
- [ ] No external file access in logs
- [ ] Content note and privacy statements in place
- [ ] Builds ready for Win/Mac/Linux

**Success Metrics:**
- 60-90 minute session length achieved
- Mercy ending discoverable and meaningful
- Meta horror elements feel safe, not intrusive
- Accessibility features support all players

---

*"The kindest ending is unlocked by doing nothing."*
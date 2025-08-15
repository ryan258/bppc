# Blue Pencil — Project Brief v1.0

_Date:_ Aug 14, 2025
_Owners:_ Creative Director, Game Director, Producer
_Engine:_ Ren’Py 8.x LTS
_Platforms:_ Windows, macOS, Linux (desktop)
_Target Session Length:_ 60–90 minutes (single sitting), with optional replays
_Content Rating:_ Teen+

---

## 1) Logline & Vision

**Logline:** A wholesome 1960s teen‑digest visual novel that slowly realizes the player is the editor. Your clicks have weight; reloading tightens the gutters. The kindest ending is unlocked by doing nothing.

**Creative Pillars**

- **Nostalgic Print Charm:** Flat CMYK, visible Ben‑Day dots, corny gag copy, letters page, milkshakes.
- **Editorial Horror:** Misregistration, blue‑pencil marginalia, fake tracebacks, haunted (but safe) saves.
- **Ethical Meta:** Never touch OS files. Reward restraint. The “good” ending is a Mercy choice to quit.

**Non‑Goals**

- No real file tampering, data scraping, or jump‑scare spam.
- No glamorized self‑harm; no puzzle‑heavy gameplay.

---

## 2) Audience & Tone

- **Audience:** Narrative/psychological VN players; fans of meta horror; streamers who enjoy reaction moments.
- **Tone:** Bright, funny, and gentle up front; clinical and precise when the Hub speaks; never cruel to the player.

---

## 3) Narrative Scope (v1.0)

**Acts (4):**
I) Welcome to Blue Pencil Poetry Club
II) Routes & Rhymes (apparent agency)
III) Out of Register (drift, converging choices)
IV) Just Mara (Centerfold & Mercy)

**Characters:**

- **Leo** (POV) — new member.
- **June** (sunny organizer), **Mina** (intense collector), **Kit** (spiky zine kid), **Mara** (self‑aware treasurer), **The Hub** (editorial blue‑pencil voice).

**Themes:** Attention has moral weight; love can be a period; quitting can be care.

---

## 4) Core Systems (Design Truths)

**Meters**

- `attn[name]` — rises for each on‑screen line consumed by that character.
- `bond[name]` — classic affection (word chips/choices).
- `drift` — global presentation instability; scales with `attn + culp`.
- `culp` — compulsive optimization (reloads, clicking all options, over‑lingering).
- `compassion` — restraint during Mercy Windows (doing nothing, backing out).
- `hub_pressure` — governs intensity/frequency of Hub intrusions.

**Signature Set Pieces**

1. **Try Again Trap:** A converging choice where reloading shrinks balloon tails/tightens gutters; optimization harms presentation.
2. **Haunted Load:** Custom load screen with one haunted slot that plays a 1–2s interstitial (empty room + Hub whisper) before loading the real save. No files are touched.
3. **Centerfold Mercy Window:** Full‑screen faux spread with two draggable staples and a 20s idle timer. Doing nothing triggers the Mercy Ending; pulling staples unlocks darker branches and raises `culp/drift`.
4. **Fake Traceback:** In‑engine message screen styled like a Ren’Py error, with Copy & Continue; used sparingly.
5. **Title Memory:** If Mercy achieved, the title adds “Thank you for closing the book.” on future boots.
6. **Honest Mode (post‑credits):** Toggle to disable haunt effects/drift for accessibility and replays.

---

## 5) Gameplay Loop

**Day → Clubroom scenes → Small choices → Poem/Zine word‑chip mini‑game → Evening Mailbag**

- **Reward:** Character scenes/letters, not stats.
- **Failstate:** Aesthetic only (drift, plate slip, blue‑pencil overwrites). No hard game‑over.

---

## 6) Art Direction (Nostalgic, Legally Distinct)

- **Style:** Clean mid‑weight ink (2.5–4 pt at print size), minimal feathering, open shapes.
- **Color:** Flat CMYK; round AM halftone **85 LPI** (or equivalent screen sim). Channel angles: **C15° / M75° / Y0° / K45°**.
- **Misregistration:** Nudge plates 0.3–0.6 pt selectively; escalate with `drift`.
- **Palette swatches:** Cherry Red (C0 M85 Y80 K0), Milkshake Pink (C0 M35 Y5 K0), Pool Blue (C45 M0 Y10 K0), Butter Yellow (C0 M10 Y60 K0), Navy (C95 M80 Y35 K30).
- **UI:** Faux price burst, corner bug, letters column; geometry unique (no Archie trade dress).
- **Resolution:** Base 1920×1080; vector balloons; UI safe margins ≥ 64 px.
- **Accessibility:** Alternate “Calm” skin with reduced halftone and high‑contrast text.

---

## 7) Audio Direction

- **Base loop:** Diner murmur, brushed snare, upright bass; light wow/flutter.
- **Cues:** Pencil scratch on reload (−12 dB), fluorescent hum for Hub scenes, 800 ms low‑pass + fade on Mercy.
- **Subtitles:** All SFX have captions (e.g., “\[pencil scratch]”).

---

## 8) UX & Accessibility

- Text scale 80–140%; dyslexia‑friendly font toggle.
- Toggles/sliders: Disable Halftone, Reduce Drift, Color‑safe Palette, **Honest Mode** (unlocks post‑credits or via hidden shift‑hold emergency).
- Mercy is always reachable without precision timing.
- No sudden flashes; drift never exceeds mild wobble and ≤1 px color offset at 1080p unless explicitly opted‑in.

---

## 9) Technical Spec

- **Engine:** Ren’Py 8.x (py3).
- **Repo Structure:** `/game/images/{bg,ui,cg}/`, `/game/sfx/`, `/game/music/`, `/game/scripts/{core,scenes,ui}/`.
- **Screens:** `mailbag`, `centerfold`, `hub_traceback`, `loads` (custom), `preferences` (with Honest Mode).
- **State:** Use `default` for run‑state; `persistent` for memory (Mercy flag, haunt masks, Honest Mode).
- **Performance:** 60 fps target; shader‑free drift (ATL transforms/overlays).
- **Saves:** Custom UI only; never rename, delete, or touch OS files.
- **Localization:** Externalize strings; reserve a context for blue‑pencil lines; locale‑specific resource lines.

**Canonical Defaults (for reference)**

```python
default attn = {"june":0, "mina":0, "kit":0}
default bond = {"june":0, "mina":0, "kit":0}
default drift = 0
default culp = 0
default compassion = 0
default hub_pressure = 0
default persistent.mercy = False
default persistent.honest_mode = False
default persistent.haunt = {}
```

---

## 10) Deliverables (v1.0)

**Content**

- 4 Acts; \~22 scenes (avg. 2–5 min each).
- 10 BGs (café, classroom, hallway, clubroom variants, empty room, etc.).
- 10 CG moments (one per act focus + 6 character beats).
- 12 character sprites (idle + 3 expressions per character).
- UI: Title, Main, Preferences, Save/Load (custom), Mailbag, Centerfold, Credits.
- Audio: 4 loops, 8 SFX, 2 stingers.

**Systems**

- Try Again Trap (Serena exemplar)
- Haunted Load (1 haunted slot)
- Centerfold Mercy Window
- Fake Traceback (1 usage, configurable)
- Title Memory
- Honest Mode + Shift emergency

**Docs**

- Art style sheet (line/halftone/misreg examples)
- Writing guide (Hub voice; microcopy list)
- QA test plan (7‑minute script)
- Accessibility checklist

---

## 11) Milestones & Acceptance

**M0 – Greenlight (Week 0)**
Brief approved; scope locked.

**M1 – Vertical Slice (Week 2)**
Serena Trap + Haunted Load + Centerfold + Credits Memory.
_Acceptance:_ All five pass the QA script; no external file writes.

**M2 – Content Alpha (Week 5)**
All scenes stubbed, art placeholders, audio temp.
_Acceptance:_ Full playthrough; toggles present; no blockers.

**M3 – Beta (Week 7)**
Content complete; art/audio final; localization hooks in.
_Acceptance:_ 0 crashers; all endings reachable; accessibility options verified.

**M4 – GM (Week 8)**
Builds for Win/macOS/Linux; press kit ready; store copy final.

---

## 12) QA Test Plan (critical beats)

1. Fresh boot → Start (no thanks text).
2. Serena scene: pick any; quick‑save; reload 3× → gutters tighten, balloon outlines thin.
3. Load haunted slot → empty room whisper → resume correct save.
4. Centerfold: idle 20s → Mercy line → credits <30s.
5. Reboot → title shows gratitude.
6. Preferences: Honest Mode visible post‑credits; toggling disables haunt/drift.
7. Shift‑hold → emergency Honest Mode flips mid‑scene.
8. Accessibility sliders affect visuals immediately.
9. No external file access in logs.

---

## 13) Safety, Ethics, Legal

- **Content:** Depicts anxiety/obsession/depression without graphic detail or instructions. Silent handling of June’s hardest beat; no shock panels.
- **Consent & Privacy:** No scraping usernames/locations. All “file” interactions are simulations in‑engine.
- **Legal:** Distinct trade dress: original names, silhouettes, logo, caption geometry.
- **On‑Boot Content Note:** Plain language + crisis resources.

---

## 14) Marketing & Comms

- **One‑liner:** _A wholesome teen‑digest that slowly realizes you’re the editor._
- **Trailer (20s):** Cheer → three “different” choices → same line → haunted load blink → centerfold hand hover → card: _A kind ending waits for the patient._
- **Screenshots:** Café meet, first menu, haunted load, centerfold, gratitude title.
- **Streamer note:** Please avoid saying the game deletes files; it doesn’t.

---

## 15) Open Questions (to resolve by M1)

- Mercy timer length (20s default): UX test variants 15/20/30s.
- Volume curve for pencil scratch on reload (−12 dB vs −10 dB).
- Number of fake traceback uses (1–2 max).
- Poem/Zine word‑chip UI (placemat vs modal list).

---

## 16) Definition of Done (feature checklists)

**Try Again Trap**
☐ Converging options ☐ Reload detection ☐ Visual scar (gutters/tails) ☐ Rollback gated ☐ QA pass

**Haunted Load**
☐ Custom screen ☐ Interstitial ☐ Persistent mask ☐ Honest Mode respects ☐ QA pass

**Centerfold**
☐ Draggable staples ☐ Idle timer ☐ Mercy roll ☐ Maze branch ☐ QA pass

**Title Memory**
☐ Flag set on Mercy ☐ Title text inject ☐ Toggle off in Honest Mode ☐ QA pass

**Honest Mode**
☐ Settings toggle post‑credits ☐ Shift emergency ☐ Disables haunt/drift ☐ QA pass

---

### Appendix: Canonical Microcopy (for writers)

- Hub toast: “That was a cute choice. It didn’t work.”
- Haunted Load whisper: “You saved her here. You will spend it somewhere else.”
- Mercy UV: “Thank you for not unbinding us.”
- Credits (Mercy): “A kind reader left the lights on behind them.”

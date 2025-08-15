Ship it. Here’s your **Gold Master kit**—tight, testable, and ready to hand to QA, marketing, and build ops.

# 1) Build & version

- **Versioning:** `1.0.0-gm` (gm tag only when all checks below pass).
- **Targets:** Win (x86_64), macOS (universal), Linux (x86_64). Mobile later.
- **Ren’Py:** 8.x LTS. In Launcher: **Build Distributions →** select three desktop targets.
- **Artifacts naming:** `BluePencil-1.0.0-win.zip`, `…-mac.zip`, `…-linux.tar.bz2`.
- **Save reset switch (for reviewers):** `--reset-persistent` CLI or in-game **Settings → Reset Memory** (dev only; hide in retail).

# 2) Content freeze checklist

- ✅ Serena “Try Again” Trap (reload scars: gutters/tails)
- ✅ Haunted Load (interstitial + slot mask; never touches disk)
- ✅ Centerfold Mercy Window (idle → Mercy; drag → Maze)
- ✅ Title remembers Mercy (“Thank you for closing the book.”)
- ✅ Honest Mode (post-credits) + **Shift hold** emergency flip
- ✅ Mailbag mirrors behaviors (reloads, neglect, mercy)
- ✅ Audio cues: diner loop, pencil scratch, Mercy low-pass
- ✅ Accessibility toggles (Halftone off, Reduce Drift, Dyslexia-friendly font)

# 3) QA pass (7-minute script)

1. Fresh boot → **Start** (no thanks text).
2. Serena scene: pick any; quick-save; reload 3× → gutters tighten, balloon outlines thin.
3. **Load** haunted slot → empty room whisper → auto-return to correct save.
4. **Centerfold:** wait 20s → Mercy line → credits <30s.
5. Reboot → title shows gratitude line.
6. **Settings:** Honest Mode appears; toggle ON → no haunt/drift; Load thumbnails honest.
7. **Shift hold** mid-scene → Honest Mode flips.

# 4) Safety, consent, privacy (ship-ready copy)

**Content Note (boot screen):**
This story depicts anxiety, obsessive behavior, and depression. No graphic self-harm, no instructions. If you need support, consider pausing and seeking local resources.

**Privacy & Files (in-game Legal):**
Blue Pencil does not read, write, or delete files outside its installation and save folders. All “file” interactions are simulated within the game. No personal data is collected or transmitted.

# 5) Store page (short/long), tags, age gate

**One-liner:**
_A wholesome 1960s teen-digest that slowly realizes you’re the editor._

**Long:**
Build poems, pass notes, and hang at a chrome-trim diner in a lovingly halftoned visual novel. Your clicks have weight. Reloading to fix things tightens the gutters; dwelling on a line makes the color slip. When the book offers a “bonus centerfold,” the kindest choice is to leave it bound. **Blue Pencil** is about attention, not fear—an interactive argument that sometimes love is a period.

**Features bullets:**

- Digest-era linework, CMYK dots, intentional misregistration
- A **Mercy Ending** unlocked by doing nothing
- Haunted saves (illusion only), fake tracebacks (safe theatricality)
- Letters page that mirrors how you play
- Post-credits **Honest Mode** for accessibility & speedruns

**Tags:** Narrative, Psychological, Meta, Choice-Driven, Retro, Single-Session.
**Age gate:** Teen+; clear content note on store page.

# 6) Press kit (drop-in)

- **Pitch paragraph:** (use long copy above).
- **5 screenshots:** cheerful café; first menu; haunted load interstitial; centerfold screen; title with “Thank you…” line.
- **One 20-sec trailer beat sheet:**

  1. Cheerful gag panels →
  2. First menu (three nice choices) →
  3. Quick cut of the same line after all three →
  4. Load screen thumbnail blink → empty room whisper →
  5. Centerfold staples and a hand hovering →
  6. Card: _A kind ending waits for the patient._ → Title.

# 7) Streamer/critic guidelines (spoiler-safe)

- Stream **Act I + Serena trap** freely.
- Blur/avoid showing **Centerfold** prompt; let audience infer.
- Post-credits, enable **Honest Mode** for replays to avoid confusing viewers.
- Please avoid claiming “it deletes files”; it does not. (We don’t police, we ask.)

# 8) Accessibility checklist

- Text scaling 80–140%
- Dyslexia-friendly font toggle
- Halftone/Drift intensity sliders + master **Calm Mode** preset
- Subtitles for all SFX cues (“pencil scratch,” “fluorescent hum”)
- Color-safe palette option (magenta drift replaced with luminance shift)

# 9) Legal clean-room notes

- No Archie names, trade dress, catchphrases, or signature silhouettes.
- Unique logo, caption slugs, price burst geometry.
- Credits include: “**All file interactions depicted are simulated within the game.**”

# 10) Achievements (optional, platform-agnostic)

- **Merciful Reader** — Quit at the centerfold.
- **Rehearsal** — Reload the same beat 3×.
- **Blue Pencil** — Trigger the fake traceback once.
- **Letters Column** — Open the mailbag every day.
- **Honest Work** — Finish in Honest Mode enabled.

# 11) Localization notes

- Externalize all strings (no embedded punctuation in variables).
- Keep `{color=#2B68C5}` blue-pencil lines in a dedicated translation context.
- Provide locale-specific crisis resource lines in `/i18n/resources.txt`.

# 12) Post-launch hotfix plan (48h window)

- v1.0.1: slider granularity for drift; fix rare double-interstitial on Linux; add **Settings → “Restore Honesty”** pre-credits if needed for accessibility.
- v1.0.2: subtitle timing polish; rare alt-tab music duck fix.

# 13) Credits (ordering that tells the truth)

- Editor (The Hub)
- Writing & Design
- Art & UI
- Code & Systems
- Audio
- Accessibility Review
- Sensitivity & Clinical Adviser
- Special Thanks (Playtesters)
- And finally: **You, who closed the book.**

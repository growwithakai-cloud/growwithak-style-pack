# growwithak style pack · recipes

Colours and fonts below are the default theme. Swap each for its role in `theme.json` (see "Your theme" in `SKILL.md`).

106 styles: Courses 1–4 are the original nine from the Reel "Hey Claude, can you…", Course 5 is eight handmade, paper-and-typewriter styles, Course 6 is six styles for tool reviews and big moments, and Courses 7–14 are 83 more styles for hooks, captions, layouts, proof, visual beats, app moments, signature effects, pace, sound and finish. Courses 7–14 give the look and the key numbers; build the details with the shared pieces below and the house rules. All sizes are on a 1080×1920 composition (rendered at 4K). This file says exactly what each must look like so you can build it on new footage. "Say it on" is the spoken word the style lands on.

Shared pieces:
- **Pop-in:** scale 0.6 → 1, `back.out(2)`, 0.4s. Cards may tilt a few degrees.
- **White card:** white 9–10px frame, 22–30px radius, shadow `0 14px 36px rgba(59,38,38,.3)`.
- **Burgundy:** `radial-gradient(ellipse at 50% 45%, #8a2a3f 0, #6b1a2c 55%, #4a0f1d 100%)`.
- **Cut-out stack:** talk video (with audio) → backgrounds and "behind you" cards → person cut-out (muted, same timing) → "in front" graphics → captions.
- **Cream:** `#fff8ef` with blush dots (5px, every 54px).
- **Typewriter accent (Course 5 only):** `"American Typewriter", "Courier New", monospace`, weight 400, cocoa on white paper. Short labels only (one to four words); titles stay Fraunces, buttons and CTAs stay Figtree.
- **Paper tag:** white, radius 6, shadow `0 8px 20px rgba(59,38,38,.25)`, tilted 2–4°.
- **Typing:** reveal text one character at a time (≈ 0.04s per character) with a 3px cocoa caret that blinks at 1Hz while typing.

---

## Course 1 · The first second

### #butterhook · Butter hook card
Say it on: the first line, before the first effect word. On screen from frame 1.
- Full-frame butter `#FFE59A` canvas above everything.
- Small handwritten caps line, cocoa, 46px, letter-spacing .06em, top 270px (default "the trick to"). Font: a handwriting font on the machine (`"Bradley Hand", "Segoe Print", cursive`).
- Bold lowercase title, Figtree 900, 104px, letter-spacing -.04em, top 330px (default "editing with claude.").
- Their clip (`talk-1080.mp4`, muted, same time) in a white card: 580×1031 at left 250 / top 520, rotated -2°.
- Comment bubble at left 120 / top 1260: white, radius 26, blush avatar circle 58px, name line Figtree 700 28px at 60% opacity, comment Figtree 600 34px. **Real comment only.**
- Exit, 0.35s before the first effect word: text and bubble fade up (0.15s), the card straightens and scales to fill the frame with transforms only (`x`, `y`, `scale` ≈ 1.94, `rotation` 0, card background to transparent, 0.3s `power3.inOut`), then the canvas fades out in 0.06s just before the next style starts. The next effect starts after the canvas is gone, so nothing ghosts.

## Course 2 · Showstoppers

### #orbit · Reel orbit
Say it on: "orbit" (or the word that names the move). Runs until that clip ends (about 1s).
- 9 cards from their profile grid: 180×320, 6px white border, radius 22, shadow.
- Each card exists twice: one copy behind the cut-out, one in front. On every frame show the front copy when `sin(angle) > 0`, else the back copy.
- Ellipse centred x 540, y ≈ 1250 (move it so the front arc stays under the chin), radius 470 × 150. Card scale `0.92 + 0.22·sin(a)`, rotation `cos(a)·-10°`.
- Burst: radius 0.05 → 1 with `back.out(1.6)` over 0.45s, while the angle sweeps 0 → 0.9π over the rest of the clip (`power1.out`). Drive positions from a GSAP tween's `onUpdate` so it is seek-safe.

### #checklist · Phone checklist
Say it on: "checklist" (or a list or recap line). About 2.7s.
- Dark phone 330×660 at left 720 / top 560, beside the face (never over it): body #1d1717, radius 52, screen #2c2222 radius 38, notch.
- Header "EDIT CHECKLIST" Figtree 700 28px caps. Six rows at 60px: 36px box (white 45% border) + Figtree 700 28px label.
- Butter button at the bottom "Run edit", 72px tall.
- Slides in from x +420 with rotation 8° → 0 (0.5s `power3.out`). From 0.6s in, each box fills butter, pops to 1.15 and back, and its cocoa tick draws (`stroke-dashoffset` 24 → 0); 0.25s apart. Then the button presses to 0.92 and back and reads "Done ✓". Slides out right 0.3s before the clip ends.
- Pair with #pop.

## Course 3 · The frame

### #scrapbook · Burgundy scrapbook
Say it on: "background". Holds to the end of that clip (snap in on the word, hard cut out).
- Full-frame burgundy layer behind the cut-out.
- Two tilted white-border cards (their Reels) 240×427 beside the head: left 50 / top 330 at -8°, right 50 / top 400 at 7°. Tape strips (butter and blush, 120×34) on their top edges.
- Butter star sticker (cocoa outline) 110px near the left card, blush dot 70px near the right.
- Cards pop from 0.6 with an extra 6° of tilt; stickers pop 0.1–0.2s later.

### #split · Split screen
Say it on: "split". The whole clip, hard cut in and out.
- Cocoa page. Top half (0–958): their image blurred (40px, brightness .9) as a fill, plus the sharp image as a 730×730 card at left 175 / top 220, radius 26. Keep any text in the image below y 220.
- 4px gap, then the bottom half (962–1920): their clip (`talk-1080.mp4`, muted, same time) offset so the face sits in the upper third of the half (in the reference, video top at -600).

### #glowup · Before / After
Say it on: "before and after". The whole clip.
- Cream canvas `#fff8ef` with blush dots (5px, every 54px).
- Header "Edited by *Claude*", Fraunces 600 84px at top 250, the key word in Fraunces italic on butter, sweeping in.
- Before card: white frame, 300×533 raw clip, at left 40 / top 760, rotated -4°, white "Before" label chip on its top edge.
- After card: white frame, 560×960, at left 440 / top 470, rotated 3°, butter "After" chip. Inside: the burgundy canvas, two small tilted Reel thumbnails (110×196), and their cut-out (`talk-person.webm`) playing in sync.
- Before pops in first, After 0.6s later.

## Course 4 · Finishing touches

### #zoom · Face zoom
Say it on: "zoom in" … "zoom out".
- Talk video and cut-out share one camera wrapper with `transform-origin` on the face (about 50% 53%).
- On "zoom in": scale 1 → 1.38, 0.45s `power3.out`. On "zoom out": back to 1, 0.6s `power3.inOut`.
- Elsewhere a small punch-in (scale 1.08) on a jump cut in the call to action hides the cut.

### #pill · Butter pill captions
Say it on: the caption line and the call to action. Off everywhere else.
- One phrase at a time in a white pill: Figtree 800 58px cocoa, padding 10×30, radius 26, soft shadow, top 1300 (under the chin, above the bottom safe zone).
- One key word per phrase on butter (radius 14).
- Each phrase pops in on its first word (y 24 → 0, scale .9 → 1, `back.out(2)`, 0.18s) and is replaced by the next. Keep each on screen about 0.5s + 0.3s per word where the speech allows; the last line holds to the end.

### #pop · Checklist pops
Say it on: with #checklist only.
- `assets/sfx/pop.mp3` on every tick (volume .35), `assets/sfx/click.mp3` on the button press (volume .4). Both are original sounds, free to use; make them with ffmpeg:
  `ffmpeg -f lavfi -i "aevalsrc='0.9*sin(2*PI*t*(1400-5200*t))*exp(-28*t)':s=48000:d=0.2" assets/sfx/pop.mp3`
  `ffmpeg -f lavfi -i "aevalsrc='0.8*(random(0)*2-1)*exp(-160*t)+0.5*sin(2*PI*2400*t)*exp(-90*t)':s=48000:d=0.08" assets/sfx/click.mp3`
- Nothing else: no music, no whooshes, no pops on other graphics. Mix under the voice.

## Course 5 · Handmade

Paper, tape and typewriter pieces. One handmade "big" style (#pinboard, #monitor, #taped) per idea; #whisper and #strike can sprinkle between them. All graphics pop in, hold, and fade (0.15s) or pop out; no sounds.

### #notecard · Torn notebook note
Say it on: a section name ("my process", "step one"). About 2.5s.
- White lined page 660×330 at left 210 / top 270, rotated -3°: lines `#F3E2E4` 3px every 61px starting 92px down; bottom edge torn (zig-zag `clip-path`, about 22 teeth, 5–7% deep); drop shadow `0 14px 22px rgba(59,38,38,.3)`.
- Three blush ring holes (24px, inset shadow) down the right edge, 42px apart.
- Title Fraunces 600 92px cocoa at left 52 / top 40 inside, with one key word in Fraunces italic on butter (e.g. "my *process*").
- Sub-line in the typewriter accent, 40px cocoa, at left 58 / top 178: "→ " then the detail, typed out after the pop.
- Sits in the top band, **behind the cut-out** when there is one so hair can overlap its lower edge. Pop in, gentle float, pop out.

### #pinboard · Pinboard steps
Say it on: "here's my process" / "step by step". The whole explanation, up to about 6s.
- Full-frame blush board `#F9CFD6` with a cork-like dot texture: cocoa 10% dots (3px, every 38px) plus white 55% dots (2px, every 26px, offset 13/9).
- Lined white page 780×1000 at left 150 / top 290, rotated -1.5°, radius 6: blush margin line 4px at x 118, lines every 121px. Two butter tape strips (190×56, 85% opacity) on the top edge, tilted ±6°.
- Up to four steps 210px apart from 120px down inside the page: butter number circle 96px (Fraunces 600 56px cocoa) + label in the typewriter accent 40px on a cream `#fff8ef` slip. Each step pops in (scale 0.6, -4° → 1) on the word that starts it.
- You stay on screen in a big circle: 460px, 12px white border, at left 560 / top 1100, showing `talk-1080.mp4` (muted, same time) scaled up so your face fills the circle. Measure the face from a real frame; never go under 400px, or the face does not read on a phone.
- Cocoa stamp at left 80 / top 1220, rotated -8°: white Figtree 800 40px caps, letter-spacing .14em (e.g. "PROCESS"), pops in 0.9s after the board.
- Steps come from the script; default to the steps they say. Make them a real, tangible example of what actually happened (for example "Film one take · Type /styles #map · Get a 35s Reel"), not generic labels. Keep the page above y 1500.
- Inside #commandchat it plays full screen: stay zoomed straight from the beat before it.

### #monitor · Retro monitor
Say it on: "code", "prompt" or "it wrote". About 3s.
- Cream dotted canvas fills the frame. The talk video moves to the bottom half: a 1080×1040 window at top 880 with a 10px white top border, video offset so the face sits in it (in the reference, video top at -360).
- Monitor 860×600 at left 110 / top 250, rotated -1°: cream bezel `linear-gradient(#fffdf8, #f6ead6)`, radius 46, shadow; butter power LED 18px bottom right.
- Screen inset 44/40/44/70, radius 30, cocoa with inner shadow. Up to four lines of their real prompt or code in the typewriter accent 34px, line height 1.6, white, with keywords in butter and variables in blush. Lines type one after another (about 0.6s each).
- White four-point sparkles (40–70px) twinkle around the bezel; one 180px white ring at the top-right corner.
- After the last line, a stamp pops at left 470 / top 600, rotated -6°: "PERFECTLY" white Figtree 800 50px caps on cocoa, and below it the key word in Fraunces italic 74px on butter (e.g. "*clean.*").
- Use their real prompt or code. Swap any private names, keys or paths.

### #taped · Taped screenshot
Say it on: the name of the app, file or page they show. About 2.5s.
- Same cream canvas and bottom-half talk window as #monitor.
- Their screenshot in a white card 880×560 at left 100 / top 270, rotated 1.5°, 10px white frame, radius 30. Keep the real app chrome; it must be sharp (full-size).
- Two butter tape strips 170×54 over the top corners, at ±37°.
- Torn label strip on the top edge at left 210 / top 228, rotated -2°: white paper with ragged ends, typewriter accent 40px, the page name plus " ✕" (like a browser tab).
- Blush chip at left 150 / top 720, rotated -3°: Fraunces 600 52px, one word in italic on butter (e.g. "my *guide*").
- Card pops first, tape 0.15s later, label 0.25s, chip 0.5s. Gentle float while held.

### #whisper · Typewriter word tag
Say it on: any keyword they want to underline quietly. 1–1.5s each; use it as often as it helps.
- Paper tag beside the face, never on it (default left 60 / top 1200; mirror to the left side if the face is off-centre). Typewriter accent 46px cocoa, padding 10×24, rotated -4°.
- Pops in, types the one word, holds, pops out.

### #strike · Strike and swap
Say it on: a correction ("not captions, *edits*"). About 2s.
- Group at left 60 / top 1230 (below the chin, left half).
- Wrong word on a paper tag (typewriter accent 58px, padding 12×30, rotated -3°) at 110px down in the group; it pops and types.
- A hand-drawn cocoa line (9px, round caps, a slight wave) draws across it over 0.5s (`stroke-dashoffset` → 0).
- The right word pops above it at left 40 / top 0: Fraunces italic 500 92px cocoa on butter, padding 0 26, radius 16, rotated 4°, `back.out(2)`.

### #bigword · Stretchy big word
Say it on: the name of an effect, or the punchline. Once per Reel, about 1.5s.
- One to two words, Fraunces 600 150px cocoa (one word in italic), on a butter block (padding 10 40 24, radius 26, shadow), centred at top 1290 over the chest, under the chin.
- Squash and stretch in: scaleX 0.25 / scaleY 1.2 → scaleX 1.12 / scaleY 0.94 → settle to 1 (0.45s total). Out: scaleX 0.6 and fade, 0.2s.

### #comment · Comment-to-get bar
Say it on: "comment ___" (the call to action), near the end. Holds to the end of the line.
- White pill 780×124 at left 130 / top 1320, radius 999, shadow. Blush avatar circle 82px with a 5px butter ring on the left.
- The keyword types out in Figtree 800 58px caps cocoa, letter-spacing .04em (e.g. "WAITLIST").
- A small cocoa label pill above it ("COMMENT", white Figtree 700 30px caps).
- Outline heart 62px on the right; when the word finishes it fills butter and pops to 1.45 and back.
- Rises in from y +80 with a small overshoot. Use their real keyword only.

## Course 6 · Big moments

Hooks, chapters and tool reviews. #behind, #chapter and #burst sit **behind the person cut-out** (talk video → graphic → `talk-person.webm`), so hair and shoulders overlap them and the face is never covered.

### #behind · Giant word behind you
Say it on: the hook, or one big word they want to shout ("gatekeeping", "background"). 1.5–2.5s.
- Lead-in line: Fraunces 600 72px cocoa, centred at top 255, with one key word in Fraunces italic on butter (e.g. "i don't *believe* in"). Rises 30px and fades in, 0.25s.
- The big word: Figtree 900 caps cocoa, letter-spacing -.035em, centred at top 338. Size it so the word spans 960–1040px wide (about 168px for 11 letters, up to 240px for 5–6 letters). Slams in 0.15s after the lead-in: scale 1.35 → 0.97 → 1, opacity 0 → 1, 0.25s.
- Layer it behind the cut-out; only the top of the head may cover its lower part. If the head would hide more than a third of the word, lift both lines (never into the top 250px) or shorten the word.
- Out: both fade 0.2s.

### #chapter · Chapter title
Say it on: the start of each part ("phase one", "step two", "now editing"). About 1.8s each.
- Centred in the top band from top 262, behind the cut-out.
- Blush pill: Figtree 800 40px caps, letter-spacing .22em, padding 8×26, rotated 3° ("PHASE 1"). Pops in.
- Chapter word below it: Fraunces italic 500 150px cocoa, rotated -3°, on a butter block (inset 18% top, 6% bottom, radius 22) that sweeps in left to right (scaleX 0 → 1, 0.3s) after the word rises in.
- Same layout for every chapter in the Reel; only the words change.

### #burst · Doodle burst
Say it on: a surprise or reveal ("and then…", "wait"). About 1.5s.
- An 11-point starburst outline around the head: centred on the head, outer radius about 470px wide × 575px tall, inner radius about 345 × 420 (stretch it to the head). Points get ±7% irregular lengths so it looks hand-drawn.
- Two strokes: cocoa 30px underneath, butter 18px on top, round joins.
- Draws on over 0.6s (`stroke-dashoffset`), then "boils": swap between two versions of the path, each point nudged 5–7px, every 0.12s while it holds. Fades out 0.2s.
- Behind the cut-out, so any stroke that crosses the face is hidden.

### #toolcard · Tool review card
Say it on: the tool's name, when it is introduced. 2–3s, once per tool.
- Top band, centred from top 262.
- Row 1: the tool's **real** logo (120px, radius 30, 6px white border, shadow) + its name in Fraunces 600 96px cocoa on a white block (padding 10 30 16, radius 24). Pops in.
- Row 2, 22px below: three white stat chips (radius 18, padding 10×20, shadow), each with a Figtree 700 26px caps label at 75% opacity over a value: platforms + butter tick circle (46px), price + butter tick, "Difficulty" + five cocoa stars (filled ones solid, the rest at 25%). Chips pop in 0.15s apart.
- Values must be true for the tool; ask if unsure. In a "best tools" list, keep the same layout for every tool.

### #aside · Side note
Say it on: a quick aside ("I use…", "the one I have is…"). 1.5–2.5s.
- A white pill centred at top 268, rotated -2°, shadow: Figtree 500 italic 40px cocoa note, then a butter tag (Figtree 800 34px, radius 999, padding 6×20) with the action ("link in bio", "comment MIC").
- Pops in, holds, pops out. Only real products and real links.

### #flash · Flash cut
Say it on: a location or outfit change, or a new chapter. On the cut itself.
- Full-frame white layer: opacity 0 → 1 over the last 0.1s of the outgoing clip, holds 2 frames, then 1 → 0 over 0.3s.
- The incoming clip starts at scale 1.18 with `blur(14px)` and settles to scale 1, no blur, over 0.35s (`power3.out`).
- Silent. No more than three flash cuts per Reel.

## Course 7 · Hooks

More ways to stop the scroll in the first second.

### #stickers · Logo sticker stack
Say it on: the tools you compare.
- Up to four white pills (radius 999, 6px cocoa border), stacked in the top band and slightly tilted, each with the real logo (64px) and the name in Figtree 800 48px cocoa.
- Pills pop in 0.1s apart on the first brand word; the winner's name may sit on butter.

### #typecaps · Warm typewriter caps
Say it on: your first line.
- Two or three short caps lines in the typewriter accent 64px cocoa, each on its own white paper strip, stacked in the top band.
- Blush pill subtitle below (Figtree 700 36px); a butter star and a blush dot sticker pop beside it. On screen from frame 1.

### #titlebox · Three-second title box
Say it on: your hook line.
- A butter box (radius 24, no shadow) in the top band with the hook in Fraunces 600 72px cocoa, one key word in italic.
- On screen from frame 1 and fades out by 3.0s. Nothing else on screen with it.

### #onlocation · Hook filmed in the result
Say it on: your hook (a filming tip).
- A filming direction, not a graphic: tell them to say the hook from inside the result and keep it as the opening shot.
- Add at most a small blush chip naming the place (Figtree 700 36px) in the top band.

### #logoquestion · Logo-pop question
Say it on: your opening question.
- The question in a white pill (Figtree 800 48px cocoa) at top 270 from frame 1.
- Real logos (110px, radius 26, white border) pop in together under it on the first brand word; everything leaves on the first scene change.

### #logoswap · Crossed-out logo vs logo
Say it on: "this replaces that".
- Two real logos (180px, radius 42, white border) side by side in the top band, 80px apart.
- On the old tool's name a cocoa X (14px strokes, round caps) draws over the left logo; the right one pops to 1.1 and back.

### #twoweight · Two-weight title
Say it on: your first line.
- Line 1 Figtree 900 96px caps cocoa; line 2 Fraunces 300 80px caps cocoa, letter-spacing .08em (e.g. "A PRODUCTIVE / DAY WITH AI"), on a white block if the wall is busy.
- Centred at top 270 from frame 1; lifts up 40px and fades at about 3s.


### #bigtitle · Big yellow title
Say it on: your first line (a number plus a promise works best: "100+ Styles / 1 command each").
- Two centred lines in the top band from top 300, above the head: line 1 Figtree 900 150px butter, letter-spacing -0.03em, line-height 0.95; line 2 Figtree 600 58px butter, 18px below.
- Both lines get a 14px cocoa outline (`-webkit-text-stroke` with `paint-order: stroke fill`) so the butter reads on a light wall. This is the one style with butter text; the outline keeps it on brand.
- On screen from frame 1: line 1 pops in (y 30 → 0, scale 0.9 → 1, 0.35s, `back.out(1.8)`), line 2 rises 0.2s later. Holds about 2.5s, then the frame cuts or the title lifts away.

## Course 8 · Captions

Other ways to show your words. Always off your face.

### #oneword · One bold word
Say it on: a fast, punchy line.
- Each spoken word on its own: Figtree 900 110px caps cocoa on a white block (radius 20), at top 1300.
- Swap on every word, no animation besides a 0.06s scale 0.9 → 1.

### #smallbig · Small + BIG keyword
Say it on: your caption lines.
- Small words: Figtree 700 44px cocoa in a white pill at top 1300.
- One keyword per line jumps to Fraunces italic 96px on butter beside them.

### #punchline · Line + punch line
Say it on: a setup then a punch.
- Setup line: Figtree 600 44px cocoa in a white pill at top 1250.
- Punch words underneath: Fraunces 600 84px cocoa on butter, in from blur(10px) 0.2s; the whole caption blurs out together.

### #editorial · Tracked caps + big serif
Say it on: a premium or calm line.
- Small line: Figtree 700 30px caps, letter-spacing .3em, cocoa on a white strip.
- Punch word: Fraunces 600 130px cocoa (last word italic on butter), letters rise from a mask 0.05s apart.

### #chinline · Small caps under the chin
Say it on: every caption line, quietly.
- Figtree 800 38px caps cocoa, letter-spacing .08em, in a white pill just under the chin (never on it).
- Max 5 words per line; hard swaps, no motion.

### #staircase · Staircase captions
Say it on: an important explanation.
- 3–5 words, each a step lower and further right in the emptiest part of the frame (never on the face): Figtree 800 56px cocoa on white tags.
- The keyword is Fraunces italic 110px cocoa with a butter underline that draws in; clear and restart for the next phrase.

## Course 9 · Layouts

How you and the graphics share the frame.

### #depth · Depth cut-out
Say it on: a list of tools or ideas.
- Room blurred (blur 12px) behind; white cards (radius 28) and logos float at different depths behind the cut-out, slowly drifting.
- Needs the cut-out. Cards never sit over the face.

### #topband · Top-band story
Say it on: a story with photos or quotes.
- Talk video shifted down so the face sits in the lower two thirds; a white band (top 0–640, radius 0 0 36 36) holds quotes, photos and proof.
- Text in the band is Fraunces/Figtree cocoa; the face is always visible.

### #headroom · Headroom whiteboard
Say it on: a full explanation.
- Film with lots of headroom. All words go on the wall above the head (top 260 → just above the hair).
- Lines in Fraunces 600 64px cocoa with a butter underline on the key word; nothing on the body.

### #rotation · Three-layout rotation
Say it on: every new idea.
- Cycle three frames on each new idea: (1) #split-style proof on top, (2) you with one big Fraunces word on butter, (3) full-screen proof in a white card.
- Hard cuts between. Same order every cycle.

### #polaroid · Polaroid narrator
Say it on: showing a process.
- The screen recording fills a white card (radius 30) in the top 70%; you play in a white-border polaroid 300×360 bottom left, rotated -8°.
- Polaroid stays clear of the bottom 420px.

## Course 10 · Proof

Show the claim is real. Real sources, real screens.

### #highlight · Article highlighter
Say it on: a quoted fact.
- Real article screenshot in a white card in the top band; zoom to the sentence, then a butter highlight sweeps left to right behind it (0.4s).
- Cocoa pill under it: source and date (Figtree 700 30px white). Real articles only.

### #demo · Official demo footage
Say it on: a product claim.
- Cut to the official clip (2–5s) full frame or in a white card; a white pill top left reads "Official · <company>".
- Only footage they are allowed to use; never present a recreation as official.

### #countup · Giant count-up number
Say it on: the stat.
- Figtree 900 300px cocoa number behind the cut-out, counting from 0 to the value in 0.8s (ease out), unit in Fraunces italic on butter.
- Real number with a small source pill. Needs the cut-out.

### #postcard · Social post card
Say it on: "people are saying".
- The real post screenshot in a white card (radius 30) in the top band, popping in with a slight tilt, gentle float.
- Swap or blur private names unless the post is public and theirs.

### #archive · Personal archive
Say it on: your backstory line.
- Their real old photos/videos as white-border polaroids (tilted ±7°) in the top band, or full frame for 1–2s.
- Only their own material.

### #cursor · Cursor proof
Say it on: a number in a tool.
- Full-res screen recording in a white card; a cocoa arrow cursor (white outline) slides to the number and a butter box highlights it.
- Small cocoa source pill underneath.

### #fingerpoint · Finger on the screen
Say it on: your real result.
- A filming direction: film the real screen with the finger on the number; add a butter ring around the number (6px) and nothing else.
- Swap any private numbers they do not want shown.

## Course 11 · Visual beats

Visuals that explain or prove a line. Not one on every line.

### #logoroles · Logo tiles with roles
Say it on: a list of tools.
- Up to four logo tiles (140px, radius 34, white border) in a row in the top band, popping in on each name.
- Under each, a white pill with one word (Figtree 800 32px cocoa): "reasoning", "images", "music".

### #logoarrows · Logos linked by arrows
Say it on: how tools connect.
- Three logo tiles in a triangle in the top band; cocoa arrows (8px, round caps) draw between them (0.4s each).
- Optional tiny white label on each arrow.

### #shuffle · Logo shuffle
Say it on: "every week there's a new…".
- One logo slot (180px) in the top band flicks through 6–10 real logos every 0.08s, then stops.
- The phrase lands under it in Fraunces 600 72px cocoa with one butter word.

### #compare · Comparison stack
Say it on: comparing options.
- White pills (radius 999) stack in the top band one by one: logo, name (Figtree 800 44px cocoa), price right-aligned (Fraunces 600).
- The recommended one sits on butter. Real prices only.

### #kinetic · Kinetic text card
Say it on: a key sentence.
- Full-frame cream card; the sentence builds word by word in Fraunces 600 110px cocoa, one key word on butter, small line icons inline.
- 1.5–3s, then cut back to you.

### #quote · Quote card
Say it on: quoting someone.
- White top band; a big butter Fraunces quote mark, then the quote types on in Fraunces italic 64px cocoa, with who said it in a blush pill.
- Real quotes only.

### #montage · Real-life montage
Say it on: an emotional line.
- 0.4–0.8s cuts of their real clips, full frame, on the beat of the line; optionally a 2×2 grid with 6px white gaps.
- Only their own footage.

### #flowcards · Flat flow cards
Say it on: a step-by-step flow.
- Three white cards (radius 28) stacked in the top band on cream, each with an icon tile and two lines of text, appearing in order.
- Flat, cocoa text, one butter highlight.

### #progress · Progress header
Say it on: a list or ladder.
- A white pill bar at top 260 with one dot or label per item; the current one fills butter and the bar stays up the whole list.
- Advance on each item's first word.

### #logopop · Logo pop
Say it on: a product reveal.
- Logo (220px) and wordmark pop in the top band (scale 0.6 → 1.08 → 1), then a white glint sweeps across once.
- No glow or bloom; a soft shadow only.

### #timer · Ring timer
Say it on: a time or number.
- White ring (24px track at 60%) with a butter progress stroke beside the head; the number in Figtree 900 120px cocoa inside.
- Counts up in ~2s, then pops out.

### #calendar · Calendar widget
Say it on: a time jump ("10 years ago").
- White widget 360×360 (radius 60) with a blush header bar; the year in Figtree 900 120px cocoa flips back year by year (0.08s each).
- Gets its own clean moment beside you.

### #notify · Phone notification
Say it on: something that "sends".
- A white banner (radius 36, shadow) slides down to top 260: app tile, bold title, one line of text in Figtree cocoa.
- Narrow (max 900px), inside the safe zone.

### #toggles · Control tiles
Say it on: "no internet, no phone".
- Two white tiles (200px, radius 54) beside the head with cocoa icons; on the words each turns blush and a cocoa slash draws across.
- 0.3s per tile.

### #snapshots · Trip polaroids
Say it on: a trip or event.
- Their real photos as white-border polaroids dropping in (rotated ±8°) in the top band, each with a quick white flash.
- Shutter click only if #sfx is ordered.

### #profilecta · Live profile CTA
Say it on: your call to action.
- Cocoa phone card (radius 48) below the chin: the keyword types into a comment row and a butter heart fills; then it swaps to their profile and Follow taps (scale 0.92).
- Use their real handle and keyword.

### #counter · Numbered counter
Say it on: "10 tools" style lists.
- Fixed title in Fraunces 600 64px cocoa at top 260 ("10 AI tools"); under it a Figtree 700 32px counter "01/10".
- Each item's name on butter (Figtree 900 72px cocoa) swaps in on its first word.

### #arrownote · Handwritten arrow notes
Say it on: annotating your work.
- Handwriting font caps 44px cocoa ("before") beside a card, with a cocoa arrow (6px) drawing to it in 0.3s.
- One or two notes per card.

### #pinned · Pinned note
Say it on: the whole video.
- A white strip at top 260 with one handwritten line in cocoa 40px ("follow for part 2"), a butter tape strip on one end.
- Stays the whole video; nothing else shares the top band with it for long.

### #results · Results grid
Say it on: "it works on anything".
- Cream frame with two rows of three 9:16 cards in white borders, labelled "New" and "Raw" in Fraunces.
- Clips swap every second to show several examples.


### #map · Map route
Say it on: a journey, a trip, "from A to B", or a path from start to finish.
- Full-frame flat vector street map: ground `#EAE5DC`, blocks `#F6F2EB` (radius 8), parks `#CFE3B4`, street names in Figtree 600 26px `#9C968E`.
- A red route `#E53935` (14px, round caps and joins) over an `#8E1B1B` 26px outline draws along right-angle streets with rounded corners, from a red start pin to a green end pin `#2E9E48` (white 7px pin stroke), about 1.4s, `power1.inOut`. Draw the outline and the route together with `strokeDashoffset`.
- A small red car follows the tip of the route and turns with it: place it with `getPointAtLength` and `atan2` on each update. The start pin pops first, stop pins pop (scale 0 → 1, `back.out(2.5)`) as the route reaches them, and the end pin lands as the route arrives.
- Real places only when the user names them; otherwise generic street names. The route colours are the accepted exception to the palette here. Inside #commandchat it plays zoomed to full screen.

## Course 12 · App moments

Recreated app moments as animated b-roll. Swap anything private.

### #chat · Chat question + reply
Say it on: asking AI something.
- Clean white chat UI full frame: their prompt types into a blush bubble and sends, then the reply streams in grey lines.
- Use their real prompt; label it as a recreation if it isn't a recording.

### #botchat · Bots group chat
Say it on: AI agents working together.
- White chat with three avatar circles (cocoa, blush, butter) and names; messages pop in with @mentions in bold.
- Clearly a recreation.

### #tocalendar · Chat to calendar
Say it on: "it booked it".
- Chat bubble with a link → cursor clicks → a calendar grid opens → a butter event block drops into a slot.
- About 2.5s.

### #tosheets · Chat to Drive to Sheets
Say it on: "it made the spreadsheet".
- Folder icon → arrow → a sheet grid; new rows pop in highlighted butter, one per 0.15s.
- Generic file names only.

### #imessage · Phone group chat
Say it on: a conversation.
- Cocoa phone frame (radius 70) centred; bubbles pop in alternating blush (them) and white (others).
- Swap real names for first names or emojis.

### #dock · Dock click
Say it on: opening an app.
- A frosted dock bar with app tiles; cursor clicks one, it bounces twice, then the app window scales up from it.
- About 1.5s.

### #ping · Notification ping
Say it on: a character or app "says" something.
- Avatar circle (120px) with a butter dot beside the head; a white speech bubble (Figtree 700 40px cocoa) pops out of it.
- Never over the face.

### #lockup · Logo lockup pill
Say it on: naming a product and its maker.
- Cocoa pill (radius 999) in the top band: app tile, name in Figtree 800 48px white, "by" + company logo; a white shine sweeps once.
- Real logos only.

### #cast · Character intro
Say it on: introducing a cast.
- Up to four circles (160px) pop in a row in the top band, each with a white name pill under it.
- Use drawn avatars unless the people agreed to be shown.

### #diagram · Concept diagram
Say it on: explaining how something works.
- Cream full-frame card; simple cocoa line art (cloud, boxes) with lines drawing between them in order, labels in Figtree.
- One idea per diagram.

### #reveal · Cinematic logo reveal
Say it on: a big launch.
- Official footage at 50% speed with letterbox bars (cocoa), graded warm; the logo glides in 40px and settles.
- Only footage they may use.


### #commandchat · Command chat
Say it on: each item of a list (every style or tool name you say). Use it for a whole section, not one moment.
- Full-frame dark chat screen, `#1F1D1B` (the one dark-screen style; panels `#2B2926`, `#3A3733`, text `#ECE8E2`, dim `#9C968E`, accent butter).
- Top bar at top 262: a "Chat | Code" pill toggle (Figtree 700 34px, Code selected) with two round 60px buttons at the sides.
- Your message, right-aligned at top 380: a 120px rounded thumbnail of your clip above a pill that types `/styles #name` (Figtree 700 40px butter, about 0.055s a character so viewers see it type, with a 4px butter caret blinking beside it) the moment you say each name.
- Status line at top 620: a butter ✳ that spins the whole time, then "Editing with #name…" (Figtree 700 34px dim) once the command finishes typing, and a small caps tag on the right (`MUTED`, `SPED UP`, 28px).
- Your clip in a 560×996 card at left 50 / top 690, radius 30, playing in sync with the commands, each style already applied to it on its word.
- Payoff: the command becomes `/styles --all` with "100+ styles ready", then the card drops away and a plain reply types in its place (Figtree 600 52px, keyword in butter), for example "Comment **STYLE** for the full guide."
- Zoom: for showpiece styles (#map, #pinboard, #uiworld, #botchat, #chart), once the command finishes typing the card zooms to full screen (to x -50, y -690, scale 1.9286, radius 0, 0.45s `power3.inOut`, transform origin 0 0) so only the animation shows; the top bar, thumbnail and status line hide. Zoom back out (0.35s) about 0.4s before the next command.
- While zoomed, the command pill stays readable: it lifts 310px into the empty top-bar space, fades 0.9s after the zoom, and comes back for any command typed while zoomed.
- Silent by default: no typing clicks. The user adds music in Instagram.
- Open on a #bigtitle hook (about 2.5s of you full frame), then cut to the chat for the list.

## Course 13 · Signature effects

One-second showpieces. One per idea, never stacked.

### #wall · Thumbnail wall
Say it on: "I've made hundreds of these".
- Behind the cut-out: a grid of their real thumbnails (white 6px borders) fills the wall, tile by tile in 0.6s.
- Needs the cut-out.

### #uiworld · Chat-app world
Say it on: typing a request.
- Behind the cut-out: a cream chat-app background with a sidebar; a white prompt bar (radius 999) above the head types their request.
- Needs the cut-out.

### #popout · Frame break
Say it on: a big claim.
- The shot shrinks into a white-border rounded frame on a blush blurred fill; the cut-out stays full size so the head and shoulders break over the top edge.
- Needs the cut-out.

### #headlines · Headline wall
Say it on: news or reactions.
- White and cream paper notes (tilted ±7°) with butter tape stick around the head, one per beat.
- Real headlines only.

### #zoomthrough · Zoom-through cut
Say it on: a scene change.
- Scale into a dark area (a shirt, a shadow) 1 → 4 over 0.3s, frame goes cocoa, next scene scales 1.6 → 1.
- Silent unless #sfx.

### #chart · Chart grow
Say it on: growth or a big number.
- Behind the cut-out: a butter line (14px, cocoa 4px outline) draws left to right, then shoots up; the number pops at the end in Figtree 900 cocoa on white.
- Chart types variant (for a longer chart beat): the chart types draw behind you two at a time in the top band, above your head: column + pie, then the line shooting up beside the number counting up, then bar + area, then column + line. Each chart has a Figtree 800 label with a 12px white outline (`paint-order: stroke fill`). The multicolour set (blue `#4FA3DD`, green `#9BCB3B`, orange `#F7941D`, pink `#EE7EA7`, yellow `#FFD54F`) is the accepted exception to the palette here.
- Nest each chart in a positioned outer `<g transform>` and animate an inner `<g>`: GSAP overwrites an SVG group's own transform.
- No neon or glow. Real data only.

### #pullback · Pull-back reveal
Say it on: "this was edited by AI".
- The shot scales down into a white app window on cream; beside it a "Working on" list ticks with butter checks and a progress bar fills.
- About 2s.

### #double · Second angle
Say it on: a different view.
- Needs a second camera angle: it plays in a cocoa-framed card in the top band while the main take plays below.
- Same audio.

### #papercut · Paper cut
Say it on: a fun, crafty moment.
- Cream and white torn-paper layers behind; the cut-out gets a 14px white outline; cut-out letters (cocoa, blush, butter tiles) spell a word; butter tape.
- Needs the cut-out.

### #vertigo · Vertigo zoom
Say it on: a reveal line.
- Needs the cut-out: background scales 1 → 1.4 while the cut-out stays still (or the reverse), 1s ease-in-out.
- Use once per Reel.

### #cover · Magazine cover
Say it on: a big moment about you.
- Behind the cut-out: masthead in Fraunces 300 220px cocoa across the top; cover lines in Figtree 700 30px in the corners; Fraunces italic strapline above the bottom safe zone.
- Needs the cut-out.

### #glass · Frosted glass word
Say it on: one big word, softly.
- Behind the cut-out: one word in Figtree 900 260px, filled with the blurred room (backdrop blur 20px) and a white 3px edge.
- Needs the cut-out.

### #flashcards · Icon flashcards
Say it on: naming several features.
- Inside a white card: cream flashcards flip (rotateY) every 0.5s, each with one simple icon and a Fraunces italic label ("Captions", "B-roll").
- Up to five cards.

### #darkroom · Monitor in a dark room
Say it on: an explainer.
- Cocoa background; a monitor with simple cream line art on screen and a butter keyboard glow strip; fixed title in Fraunces italic 64px white below.
- The only style where text is white on cocoa across the whole frame.

## Course 14 · Pace, sound & finish

How the whole edit moves, sounds and looks.

### #fast · Fast visuals
Say it on: the whole Reel.
- Plan a visual every 2–3s from the ordered styles; never repeat a style back to back.
- Still keep talking-only breathers between ideas.

### #calm · Calm and still
Say it on: the whole Reel.
- Slow push-ins (1 → 1.05 over a line), cuts only on pauses, at most one graphic per idea.
- Pairs with #editorial or #chinline.

### #wipe · Circle wipe
Say it on: a new section.
- A butter circle scales from a card or chip to cover the frame in 0.35s, then shrinks away revealing the next section.
- Use the same colour every time.

### #sfx · Sound effects
Say it on: the big moments.
- Ordering #sfx lifts the no-sound rule: soft original effects on the big graphics only (or on every graphic if they ask), always -12dB under the voice.
- Make effects with ffmpeg or use ones they own.

### #music · Music bed
Say it on: the whole Reel.
- A track they have the rights to at about -24 LUFS under the voice, ducked further under speech.
- Fade in 0.5s, out 1s.

### #warm · Warm cinematic
Say it on: the whole Reel.
- Grade: +warmth, slight lift in blacks, soft vignette; blur the room behind any card.
- Text stays in Peach Sorbet.

### #apple · Clean iOS look
Say it on: the whole Reel.
- All graphics as white rounded cards (radius 40) and frosted panels (backdrop blur 20px) with soft shadows, in Figtree.
- No stamps, tape or doodles.

### #softwarm · Soft warm sepia
Say it on: the whole Reel.
- Sepia-warm grade; the punch line in Fraunces italic on butter with 2–3 small white sparkles twinkling.
- Pairs with #orbit.

### #studio · Studio editorial
Say it on: the whole Reel.
- Darken the room 30% while keeping the person bright (needs the cut-out), cool tone, vignette, no grain.
- Alternate wide and tight framing like a studio interview.

### #buttercanvas · Butter canvas series
Say it on: the whole Reel.
- Full butter canvas; their clip in a white-border card (radius 30) with headlines above in Fraunces cocoa.
- Use for a whole series so the grid matches.

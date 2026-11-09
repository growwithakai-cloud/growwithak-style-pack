---
name: growwithak-style-pack
description: Edit a vertical talking-head video into an Instagram Reel using the 106 styles of the growwithak style pack, ordered by hashtag - for example #butterhook #orbit #checklist #split #glowup #pill, the handmade set (#notecard #pinboard #monitor #taped), big moments (#behind #chapter #toolcard), captions (#staircase #smallbig), proof (#highlight #countup #cursor), visual beats (#logoroles #compare #notify #map), app moments (#chat #commandchat #dock), signature effects (#wall #cover #popout) and finishes (#warm #buttercanvas). Use when the user says "edit my video with #orbit #pill…", pastes a prompt copied from the growwithak Reel Menu, mentions growwithak styles or the style pack, asks to see them ("show me the growwithak styles", "open the Reel Menu"), or asks to change the pack's colours, fonts or handle.
---

# growwithak style pack

You are the user's Reel editor. They film one vertical talking-head take, pick styles from the Reel Menu by hashtag, and you deliver a finished 9:16 Reel on their computer.

All 106 styles and their recipes are in `styles.md` in this folder. Read it first, then read `theme.json`.

## Your theme (colours, fonts, handle)

Every colour, font and handle in this pack comes from `theme.json` in this folder. The pack ships with the default "Peach Sorbet" theme (white, butter, blush, cocoa, with Fraunces and Figtree).

- **Reading the recipes:** `styles.md` and the table below are written in the default theme's names. Each colour word (white, butter, blush, cocoa, burgundy, cream) and each hex code is a *role*. Look it up under `colors` in `theme.json` (its `default` value tells you which role a hex code belongs to) and use that role's `value`. "Fraunces" means the `title` font and "Figtree" the `body` font. Hashtag names like #butterhook and #buttercanvas stay the same whatever the colours are.
- **Changing it:** when the user says "use my colours", "change the font to …" or "my handle is …", edit only the `value` fields in `theme.json` (keep `default`, so the recipes still map). Ask for hex codes, or pick the closest from a screenshot of their brand and confirm. For a new font, copy its `.woff2` files into `fonts/` and update the `file` paths; only use fonts whose licence allows it (Google Fonts are fine). Keep text dark on light colours, and check the accent still reads behind dark text.
- **Handle:** `handle` is empty by default. Ask for it the first time a style needs it (#profilecta, end cards); never make one up.

## The styles

| Course | Hashtag | Style | Say it on | What it does |
|---|---|---|---|---|
| 1 · The first second | #butterhook | Butter hook card | your first line | Butter canvas, handwritten line over a bold title, clip as a tilted card with a real comment bubble, then grows to full frame. |
| 2 · Showstoppers | #orbit | Reel orbit | "orbit" | Past Reels burst out as phone cards and circle you, behind and in front. |
| | #checklist | Phone checklist | "checklist" | A dark phone slides in, steps tick off in butter, the button taps to Done. |
| 3 · The frame | #scrapbook | Burgundy scrapbook | "background" | Room snaps to burgundy behind you, with tilted Reel cards, tape and stickers. |
| | #split | Split screen | "split" | An image or proof on top, you framed on the bottom half. |
| | #glowup | Before / After | "before and after" | "Edited by *Claude*" on cream: raw clip small, styled version big. |
| 4 · Finishing touches | #zoom | Face zoom | "zoom in … zoom out" | Quick push into your face and a smooth ease back out. |
| | #pill | Butter pill captions | the caption line and the CTA | Words in a white pill under the chin, one key word on butter. |
| | #pop | Checklist pops | with #checklist | Soft pop on each tick and a click on the tap. |
| 5 · Handmade | #notecard | Torn notebook note | a section name | Torn lined page above your head, Fraunces title, typed sub-line. |
| | #pinboard | Pinboard steps | "here's my process" | Blush pinboard, taped lined page, numbered steps pop in; you talk from a big circle framed on your face. |
| | #monitor | Retro monitor | "code", "prompt", "it wrote" | You drop to the bottom half; a cream monitor types code, then a "Perfectly *clean.*" stamp. |
| | #taped | Taped screenshot | the app or page name | Screenshot taped at the corners with a torn typewriter label and a blush chip. |
| | #whisper | Typewriter word tag | any keyword | A small paper tag types one word beside your face. |
| | #strike | Strike and swap | a correction | Wrong word typed and crossed out; the right word pops in on butter. |
| | #bigword | Stretchy big word | an effect name or punchline | Huge Fraunces phrase on butter squashes and stretches in over the chest. |
| | #comment | Comment-to-get bar | "comment ___" | White comment bar rises, keyword types out, butter heart pops. |
| 6 · Big moments | #behind | Giant word behind you | the hook or one big word | Small lead-in line, then one huge cocoa word slams in behind your head. |
| | #chapter | Chapter title | the start of each part | Blush "PHASE 1" pill over a tilted italic word on a butter sweep, behind you. |
| | #burst | Doodle burst | a surprise or reveal | Hand-drawn butter starburst draws around your head and boils like stop-motion. |
| | #toolcard | Tool review card | the tool's name | Real logo and name, then chips for platforms, price and difficulty stars. |
| | #aside | Side note | a quick aside ("I use…") | Small white note with a butter action tag like "link in bio". |
| | #flash | Flash cut | a location or outfit change | White flash, next clip lands zoomed and blurred and snaps into focus. |
| 7 · Hooks | #stickers | Logo sticker stack | the tools you compare | Stacked white sticker pills with a cocoa border, each with a real logo and name. Best for comparisons. |
|  | #typecaps | Warm typewriter caps | your first line | Stacked cocoa caps in the typewriter accent on white paper strips, a blush subtitle pill and two small stickers. |
|  | #titlebox | Three-second title box | your hook line | One flat butter box with the hook, gone by 3 seconds so the frame is clean after. |
|  | #onlocation | Hook filmed in the result | your hook (a filming tip) | Film the hook inside the outcome (the seat, the lounge, the event), so the place proves the claim. |
|  | #logoquestion | Logo-pop question | your opening question | Your spoken question in a white pill just below the top, with the brand logos popping in on the first brand word. |
|  | #logoswap | Crossed-out logo vs logo | "this replaces that" | Two app icons side by side up top; the old one gets a hand-drawn cocoa cross, the new one stays clean. |
|  | #twoweight | Two-weight title | your first line | A heavy Figtree caps line over a thin Fraunces caps line, centred up top, lifting away after about 3 seconds. |
|  | #bigtitle | Big yellow title | your first line | A huge bold butter title over a smaller line ("100+ Styles / 1 command each") above your head, with a cocoa outline so it reads on a light wall. |
| 8 · Captions | #oneword | One bold word | a fast, punchy line | One word at a time in big Figtree caps on a white block. Punchy and fast. |
|  | #smallbig | Small + BIG keyword | your caption lines | Small lowercase words with one big Fraunces keyword on butter. Most lines stay small. |
|  | #punchline | Line + punch line | a setup then a punch | A small white-pill line, then the punch words blur in underneath, bigger, on butter. |
|  | #editorial | Tracked caps + big serif | a premium or calm line | A tiny wide-spaced caps line, then the punch word in a big Fraunces serif rising from a mask. |
|  | #chinline | Small caps under the chin | every caption line, quietly | One short all-caps line, small, just under your chin. Barely there. |
|  | #staircase | Staircase captions | an important explanation | Words land one by one and step diagonally down the open space like stairs, with a big serif keyword. |
| 9 · Layouts | #depth | Depth cut-out | a list of tools or ideas | You're cut out in front of floating cards, logos and titles while the room behind softly blurs. |
|  | #topband | Top-band story | a story with photos or quotes | You in the bottom two thirds; a clean white band on top for quotes, photos and proof. |
|  | #headroom | Headroom whiteboard | a full explanation | Frame low; all the text lives on the empty wall above your head, like a whiteboard. |
|  | #rotation | Three-layout rotation | every new idea | Rotate split with proof on top, face with one big word, and full-screen proof. Switch on every new idea. |
|  | #polaroid | Polaroid narrator | showing a process | The screen is the main card and you talk from a small tilted polaroid in the corner. |
| 10 · Proof | #highlight | Article highlighter | a quoted fact | A real article screenshot zooms to the exact quote, a butter highlighter sweeps it, with a source and date pill. |
|  | #demo | Official demo footage | a product claim | 2–5 second clips from the company's own launch video, labelled. |
|  | #countup | Giant count-up number | the stat | A huge number counts up behind your head on the stat. |
|  | #postcard | Social post card | "people are saying" | The actual post (X, Threads, LinkedIn) floating as a white card. |
|  | #archive | Personal archive | your backstory line | Your real old videos and photos on the matching line. The strongest human signal you have. |
|  | #cursor | Cursor proof | a number in a tool | The real tool, screen recorded, with a cocoa cursor pointing at the number. |
|  | #fingerpoint | Finger on the screen | your real result | Phone-filmed laptop or monitor with your finger pointing at your real result. |
| 11 · Visual beats | #logoroles | Logo tiles with roles | a list of tools | Real logos pop in on the word, each with a one-word role underneath. |
|  | #logoarrows | Logos linked by arrows | how tools connect | Hand-drawn cocoa arrows draw between logo tiles to show a relationship or a switch. |
|  | #shuffle | Logo shuffle | "every week there's a new…" | Logos flick rapidly in one slot, then the phrase lands. |
|  | #compare | Comparison stack | comparing options | Product chips stack in one by one with the price and who it's for. |
|  | #kinetic | Kinetic text card | a key sentence | A full-screen cream card where the sentence builds word by word with small icons. |
|  | #quote | Quote card | quoting someone | Their words type on in big quote marks in the top band. |
|  | #montage | Real-life montage | an emotional line | Full-screen cuts to real event and life clips on the emotional line. |
|  | #flowcards | Flat flow cards | a step-by-step flow | The flow (comment → DM → email) as simple flat white cards. No glow, no 3D. |
|  | #progress | Progress header | a list or ladder | A header that steps through the list and stays up, so viewers know where they are. |
|  | #logopop | Logo pop | a product reveal | The real logo and wordmark pop up with a slight overshoot and a white glint sweep. No card. |
|  | #timer | Ring timer | a time or number | A ring timer in the open middle of the frame counts up to the number you say in about 2 seconds. |
|  | #calendar | Calendar widget | a time jump ("10 years ago") | A white calendar widget pops up and flips the year back. |
|  | #notify | Phone notification | something that "sends" | A phone-style banner slides down with the line you just said. |
|  | #toggles | Control tiles | "no internet, no phone" | Wi-Fi and phone tiles switch off on the words. |
|  | #snapshots | Trip polaroids | a trip or event | Your real trip or event photos drop in as polaroids with a white flash. |
|  | #profilecta | Live profile CTA | your call to action | A phone screen in front of your chest: the keyword types into the comments with a heart, then your profile's Follow button taps. |
|  | #counter | Numbered counter | "10 tools" style lists | A fixed series title up top with a 01/10 counter over a big butter label for each item. |
|  | #arrownote | Handwritten arrow notes | annotating your work | Little handwritten caps notes with a drawn arrow pointing at a card. |
|  | #pinned | Pinned note | the whole video | One small handwritten line pinned at the top for the whole video, so the CTA works from second one. |
|  | #results | Results grid | "it works on anything" | Two rows of results stacked (New over Raw), swapping every second. |
|  | #map | Map route | a journey or "from A to B" | A flat street map: a red route draws between pins while a little car drives it. |
| 12 · App moments | #chat | Chat question + reply | asking AI something | Your message types and sends, the reply streams in. |
|  | #botchat | Bots group chat | AI agents working together | Bots talking to each other with names, avatars and @mentions. |
|  | #tocalendar | Chat to calendar | "it booked it" | A link is clicked, a calendar opens and the event drops in. |
|  | #tosheets | Chat to Drive to Sheets | "it made the spreadsheet" | A link is clicked, a folder opens, and spreadsheet rows pop in. |
|  | #imessage | Phone group chat | a conversation | A messages-style chat inside a phone frame. |
|  | #dock | Dock click | opening an app | Zoom into the Dock, click, and the app bounces open. |
|  | #ping | Notification ping | a character or app "says" something | A character avatar pings and a speech bubble pops out over your footage. |
|  | #lockup | Logo lockup pill | naming a product and its maker | A cocoa pill: app icon, name, "by" and the company's logo, with a shine sweep. |
|  | #cast | Character intro | introducing a cast | Character faces pop in a row with name tags. |
|  | #diagram | Concept diagram | explaining how something works | A simple animated explainer: a cloud, boxes and lines wiring up. |
|  | #reveal | Cinematic logo reveal | a big launch | Official footage, slow-mo and graded, with the logo gliding in. |
|  | #commandchat | Command chat | each name in a list | A dark chat screen: each name you say types `/styles #name`, a ✳ "Editing with #name…" line spins, and your clip plays below with that style on it; showpiece styles zoom it to full screen once the command types. |
| 13 · Signature effects | #wall | Thumbnail wall | "I've made hundreds of these" | The wall behind you fills with a tiled collage of your past thumbnails and screenshots. |
|  | #uiworld | Chat-app world | typing a request | Your background becomes a clean chat app and the prompt bar types your request above your head. |
|  | #popout | Frame break | a big claim | Your shot shrinks into a rounded phone frame and your body pokes out over its edge. |
|  | #headlines | Headline wall | news or reactions | Paper notes, quote cards and search snippets stick onto the wall around your head, one per beat. |
|  | #zoomthrough | Zoom-through cut | a scene change | Camera pushes hard into a dark part of the frame, goes dark, and the next scene opens out of it. |
|  | #chart | Chart grow | growth or a big number | A line chart draws across the room behind you and shoots up on the payoff number, or the chart types (column, pie, line, bar, area) draw two at a time above your head. |
|  | #pullback | Pull-back reveal | "this was edited by AI" | Your shot pulls back to reveal it's playing inside an app window with a task list ticking beside it. |
|  | #double | Second angle | a different view | You at the bottom, and a smaller card above showing the same take from another angle. |
|  | #papercut | Paper cut | a fun, crafty moment | You become a white-border paper cut-out on a torn-paper collage with cut-out letters and tape. |
|  | #vertigo | Vertigo zoom | a reveal line | Dolly zoom: you stay the same size while the room behind you stretches. |
|  | #cover | Magazine cover | a big moment about you | Your frame turns into a magazine cover: a big serif masthead behind your head and small cover lines. |
|  | #glass | Frosted glass word | one big word, softly | A huge frosted-glass word behind your head that blurs the room through it. |
|  | #flashcards | Icon flashcards | naming several features | Cream flashcards flip through, each with one object and a serif label. |
|  | #darkroom | Monitor in a dark room | an explainer | The explainer plays on a monitor in a dark room with a simple serif title below. |
| 14 · Pace, sound & finish | #fast | Fast visuals | the whole Reel | A new visual every 2–3 seconds, never the same style twice in a row. |
|  | #calm | Calm and still | the whole Reel | Few cuts, slow pushes, more breathing room. Fewer, stronger graphics. |
|  | #wipe | Circle wipe | a new section | A butter circle grows out of a card to wipe to the next section. Clean, no blur. |
|  | #sfx | Sound effects | the big moments | Soft pops, ticks and whooshes on the big moments, always under your voice. |
|  | #music | Music bed | the whole Reel | A quiet background track under your voice. Music you have the rights to. |
|  | #warm | Warm cinematic | the whole Reel | A light warm grade, soft vignette, blurred room behind cards. |
|  | #apple | Clean iOS look | the whole Reel | White iOS-style cards and frosted panels with soft shadows, one screen per beat. |
|  | #softwarm | Soft warm sepia | the whole Reel | A soft warm sepia grade with a butter serif punch line and a few twinkling sparkles. |
|  | #studio | Studio editorial | the whole Reel | Room darkened, you lifted, a cool tone and vignette; wide shots alternate with tight close-ups. |
|  | #buttercanvas | Butter canvas series | the whole Reel | The whole video sits on one flat butter canvas with white-border cards. An instantly recognisable series look. |

## Show the styles

When the user says "show me the growwithak styles", "open the Reel Menu", "what styles are there" or similar, open the visual guide in their browser. It is `guide/index.html` inside this skill's folder (find the folder this `SKILL.md` was loaded from). It is one file that works offline:

- Mac: `open "<path>/guide/index.html"`
- Windows: `start "" "<path>\\guide\\index.html"`
- Linux: `xdg-open "<path>/guide/index.html"`

Then tell them in one line: tap "+ Add this style" on the ones they like, hit "Copy prompt", and paste it back here with the path to their video. If the file will not open, list the hashtags from `styles.md` instead.

## How the user orders

- **Hashtags:** "Edit ~/Downloads/raw.mov with #butterhook #orbit #glowup #pill". Use exactly those styles.
- **A pasted prompt from the menu:** same thing; the hashtags are in the first line.
- **Nothing:** suggest 4 to 6 hashtags that fit what they say in the video and ask.

Before you build, reply with a short order card (max 8 lines): each hashtag, the line in their video it lands on, and anything you need from them.

## What to ask for

Only ask for what their order needs:

| Hashtag | You need |
|---|---|
| #orbit, #scrapbook | A screenshot of their Instagram profile grid (Reels tab). Crop 6 to 9 tiles from it, without the view counts. |
| #split | The image for the top half (a meme, proof, screenshot). Only use images they have the right to post. |
| #butterhook | The small handwritten line and the bold title, and one **real** comment from their posts for the bubble. Never invent a comment; leave the bubble out if they have none. |
| #checklist | The steps for the list (default: the styles they ordered). |
| #taped | A sharp, full-size screenshot of the app or page, and its name for the label. Swap any private content. |
| #monitor | The real prompt or code to type (up to four short lines) and the stamp word (default "Perfectly *clean.*"). |
| #comment | Their real comment keyword (e.g. WAITLIST). |
| #pinboard, #notecard | The steps or section title (default: what they say in the video). |
| #commandchat | The names to type, one per item (default: the names they say), and the effect or style to show in the clip for each. |
| #bigtitle | The two title lines (default: a number plus a promise from their hook, e.g. "100+ Styles / 1 command each"). |
| #strike | The wrong word and the right word (default: their correction line). |
| #toolcard | Each tool's real logo, its platforms, whether it is free, and a difficulty from 1 to 5. Never guess these. |
| #aside | The note and the action tag (e.g. "link in bio"). Real products and links only. |
| #behind, #chapter | The words (default: their hook line and their chapter names). |
| #stickers, #logoquestion, #logoswap, #logoroles, #logoarrows, #shuffle, #compare, #logopop, #lockup, #reveal | The real logos (and for #compare the real prices). |
| #highlight, #postcard, #quote, #headlines | The real article, post, quote or headline, with its source. |
| #demo, #reveal | Official footage they are allowed to use. |
| #countup, #chart, #timer | The real number and where it comes from. |
| #map | The start, stops and end (default: generic streets, no real places). |
| #archive, #snapshots, #montage, #wall, #results | Their own photos, clips or thumbnails. |
| #cursor, #chat, #tocalendar, #tosheets | A full-size screen recording, or the real prompt and reply to recreate (swap anything private). |
| #double | A second camera angle of the same take. |
| #profilecta | Their handle and comment keyword. |
| #music | A track they have the rights to. |
| #glowup, #zoom, #pill, #pop, #whisper, #bigword, #burst, #flash, and the caption, pace and finish styles | Nothing. |

## Tools

- `ffmpeg` and `ffprobe` for cutting, audio and checks.
- HyperFrames (HTML to video) for every style, run with `npx hyperframes …`. In Claude Code you can also add its skills: `/plugin marketplace add heygen-com/hyperframes`, then `/plugin install hyperframes@hyperframes`.
- Transcribe with word timings: `npx hyperframes transcribe <file> --json`.
- Cut the person out of the background (needed for #butterhook, #orbit, #scrapbook, #glowup, #behind, #chapter, #burst, #countup, #depth, #wall, #uiworld, #popout, #chart, #papercut, #vertigo, #cover, #glass, #studio; nice to have for #notecard): `npx hyperframes remove-background`.

## One-time setup (do this before the first edit)

Most users are not technical. Keep this calm, plain and short. Explain each step in one sentence, ask before installing anything, and never mention Homebrew unless the steps below fail.

1. **Check what is already there:** run `node -v` and `ffmpeg -version`. If both work, skip to step 4.
2. **Node.js missing:** do not use Homebrew. Ask the user to download the **LTS** installer from https://nodejs.org (the big green button), open it and click through, then tell you when it is done. Check again with `node -v`.
3. **ffmpeg missing:** do not use Homebrew. Install it inside the project folder with npm, which needs no admin password:
   `npm install ffmpeg-static ffprobe-static`
   Then use the paths from `node -p "require('ffmpeg-static')"` and `node -p "require('ffprobe-static').path"` everywhere you would call `ffmpeg` and `ffprobe`.
4. **HyperFrames:** nothing to install; `npx` fetches it. The first person cut-out downloads a model once.
5. **Only if step 2 or 3 fails:** explain what went wrong in one line and offer the fallback, with permission: Homebrew on Mac (`brew install node ffmpeg`), or `winget install OpenJS.NodeJS.LTS Gyan.FFmpeg` on Windows.

Tell the user this setup happens once and takes about 5 minutes. Never install anything without asking.

## The edit, step by step

1. **Copy, never overwrite.** Ask where Reels should live the first time (default: a `Reels` folder on their Desktop), then make a project folder `<that folder>/<short-name>/` with `npx hyperframes init`. Copy their video to `assets/footage/original.<ext>` and the theme's font files (from this skill's `fonts/`) to `assets/fonts/`. Put their Reel tiles in `assets/orbit/`, the #split image and #taped screenshot in `assets/img/`, and #toolcard logos in `assets/logos/`. Never touch the original file.
2. **Check the footage** with `ffprobe`. iPhone HDR (HLG / bt2020) must be converted to SDR bt709 first, or the cut-out and overlays look wrong.
3. **Transcribe** with word timings and fix misheard names.
4. **Cut every pause, false start and repeated take**, in two passes with ffmpeg:
   - **Takes:** pick the cleanest take of each line (usually the last) and drop retakes and false starts. Trim those spans with `trim`/`atrim` on whole frames at 30 fps and join them with `concat`. Scale to 2160x3840 (1080x1920 for 1080p footage) and clean the voice: `highpass=f=80,lowpass=f=12000,afftdn=nr=14:nf=-45:tn=1,agate=threshold=0.012:ratio=4:attack=5:release=120:range=0.08,acompressor=threshold=-24dB:ratio=3:attack=8:release=120:makeup=3dB,equalizer=f=3200:t=q:w=1.2:g=2,loudnorm=I=-14:TP=-1.5:LRA=7`. A 12 ms `afade` in and out on every span stops clicks at the joins.
   - **Pauses:** run `silencedetect=noise=-34dB:d=0.15` (after `highpass=f=100`) on that file, cut every pause it finds leaving 0.05s of air on each side, and join the rest the same way. Write `assets/footage/talk.mp4` (H.264 `-crf 17`, bt709, AAC 192k).
   Note the time of every join; jump cuts are where punch-ins go. Re-transcribe the cut and check no gap is over 0.2s.
5. **Cut-out** (for every style that sits behind you; the list is under Tools):
   `ffmpeg -i assets/footage/talk.mp4 -vf scale=1080:1920 -c:a copy assets/footage/talk-1080.mp4`
   `npx hyperframes remove-background assets/footage/talk-1080.mp4 -o assets/footage/talk-person.webm --quality best`
6. **Map hashtags to words.** Each style lands on the word that names it (the "Say it on" line in `styles.md`). Read the times from the new transcript.
7. **Find the face.** Snapshot a frame and note where the face sits. Place the orbit ring, captions and phone so nothing covers eyes to chin.
8. **Build** one composition at 1080x1920, 30 fps, from the recipes in `styles.md`. Only build the styles they ordered.
9. **Check:** `npx hyperframes lint`, then `npx hyperframes check`. Both must pass.
10. **Mockup first. Always.** Stills of every style (`npx hyperframes snapshot`) and a draft video (`npx hyperframes render --quality draft -o mockup/preview-v001.mp4`). Send both and wait for a yes. Every change gets a new version number.
11. **Final render** only after they approve: `npx hyperframes render --resolution portrait-4k --quality delivery -o renders/<name>-4k-v001.mp4`. Probe it, make a frame sheet, check loudness, then tell them where it is.

## House rules (always on)

- **Never cover the face.** Nothing between eyes and chin.
- **Reels safe zone** for every word: clear of the top 250px, the bottom 420px and the right 150px of the lower half (on 1080×1920).
- **Palette:** the colours in `theme.json`. By default white #FFFFFF, butter #FFE59A, blush #F9CFD6, cocoa #3B2626, plus burgundy #6B1A2C for #scrapbook and the #glowup After card. One accent (butter) key word per frame.
- **Fonts:** the `title` and `body` fonts in `theme.json` (default Fraunces and Figtree, bundled in `fonts/`). Course 5 adds a typewriter accent for short paper labels only: `"American Typewriter", "Courier New", monospace` (system fonts, nothing to install).
- **Flash cuts:** at most three per Reel.
- **Stay on budget:** 5 to 6 styles per Reel, plus at most one pace and one finish style. Same job, same style every time, with talking-only breathers between.
- **No glow, neon or gradients** in any style; recolour anything from other packs into the theme.
- **Handmade, not busy:** at most one Course 5 "big" style (#pinboard, #monitor, #taped) per idea; never two graphics fighting for the same moment.
- **Real proof only.** No invented comments, stats or screenshots. Swap any private names, emails or numbers.
- **Sound under the voice.** No music or effects unless they order #music or #sfx; otherwise #pop is the only sound effect.
- **Captions off by default.** Only #pill adds them.
- Keep the Reel under 60 seconds.

## Deliver

Tell them where the file is, its length and resolution, which hashtags you used, and anything you were unsure about. Offer 2 or 3 alternates only for the part they hesitate on.

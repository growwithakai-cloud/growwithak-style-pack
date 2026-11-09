#!/usr/bin/env python3
"""Build the Reel Menu as one self-contained HTML file (fonts and photos embedded, works offline).

    python3 tools/build_guide.py                       # after any change to the skill or the guide
    python3 tools/build_guide.py --repo you/your-repo  # if the pack moves to another GitHub repo

Reads tools/guide-src/ and skills/growwithak-style-pack/fonts/, writes
skills/growwithak-style-pack/guide/index.html and docs/index.html, then zips the
skill folder to docs/growwithak-style-pack.zip (the "Download the pack" button).
"""
import argparse, base64, pathlib, re, zipfile

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "tools" / "guide-src"
SKILL = ROOT / "skills" / "growwithak-style-pack"
REPO = "growwithakai-cloud/growwithak-style-pack"
ZIP = "growwithak-style-pack.zip"


def data_uri(path, mime):
    # photos go public: refuse any that still carry camera, date or location data
    if mime.startswith("image/"):
        leaks = [k.decode() for k in (b"Exif", b"eXIf", b"iTXt", b"tEXt", b"xmp", b"GPS", b"iPhone") if k in path.read_bytes()]
        assert not leaks, f"{path.name} still has hidden metadata {leaks}; strip it first"
    return f"data:{mime};base64," + base64.b64encode(path.read_bytes()).decode()


def rep(html, old, new, count=1):
    found = html.count(old)
    assert found == count, f"expected {count} of {old[:70]!r}, found {found}"
    return html.replace(old, new)


INSTALL = """
<section class="wrap how" id="install">
  <h2>Install this <em>pack</em></h2>
  <p>Free. You need Claude Code: the Code tab in the Claude desktop app, on Mac or Windows. Pick one way, then say <code>show me the growwithak styles</code> to check it worked.</p>
  <div class="howgrid inst">
    <div class="card"><span class="num">A</span><h3>Easiest: drag the zip</h3><p>Download the pack, open the Claude app, click the Code tab, drag the zip into the chat and say:</p><pre>install this skill for me</pre><a class="btn primary dl" href="__ZIPURL__" download>Download the pack (.zip)</a></div>
    <div class="card"><span class="num">B</span><h3>One command</h3><p>In a terminal, or ask Claude Code to run it for you:</p><pre>npx skills add __REPO__</pre><button class="cp cpi" data-copy="npx skills add __REPO__">Copy command</button></div>
    <div class="card"><span class="num">C</span><h3>As a Claude Code plugin</h3><p>Type these two lines into Claude Code, one at a time:</p><pre>/plugin marketplace add __REPO__
/plugin install growwithak-style-pack@growwithak</pre><button class="cp cpi" data-copy="/plugin marketplace add __REPO__">Copy line 1</button></div>
    <div class="card"><span class="num">D</span><h3>Make it yours</h3><p>The pack ships in Peach Sorbet. Swap in your own colours, fonts and handle by telling Claude, for example:</p><pre>Change the growwithak style pack theme to my colours #1E3A5F #FFD166 and my handle @yourname</pre><button class="cp cpi" data-copy="Change the growwithak style pack theme to my colours #1E3A5F #FFD166 and my handle @yourname">Copy prompt</button></div>
  </div>
  <div class="ready"><b>First time?</b> Claude checks for Node.js and ffmpeg, explains each step in plain words and asks before installing anything. It takes about 5 minutes, once.</div>
</section>
"""

EXTRA_CSS = """
.phone .ph{width:100%;height:100%;border-radius:31px;display:block;background:var(--me) center/cover}
.tile .ph{width:100%;aspect-ratio:9/16;border-radius:22px;display:block;background:var(--me) center/cover}
.inst .card{display:flex;flex-direction:column;align-items:flex-start}
.inst .card pre{align-self:stretch;overflow-wrap:anywhere}
.inst .cp,.inst .dl{margin-top:12px}
.inst .dl{font-size:14px;padding:10px 16px}
"""

EXTRA_JS = """
<script>
// copy buttons in "Install this pack"
document.querySelectorAll(".cpi").forEach(b => b.addEventListener("click", async () => {
  const text = b.dataset.copy;
  try { await navigator.clipboard.writeText(text); }
  catch (e) { const ta = document.createElement("textarea"); ta.value = text; document.body.appendChild(ta); ta.select(); try { document.execCommand("copy"); } catch (e2) {} ta.remove(); }
  const el = document.getElementById("toast"); el.textContent = "Copied. Paste it into Claude Code"; el.classList.add("on");
  clearTimeout(b.t); b.t = setTimeout(() => el.classList.remove("on"), 1700);
}));
</script>
"""


def build(repo):
    html = (SRC / "index.html").read_text()
    clips, fonts = SRC / "clips", SKILL / "fonts"

    # fonts, embedded once each
    for name in ("fraunces.woff2", "fraunces-italic.woff2", "figtree.woff2"):
        html = rep(html, f"url(fonts/{name})", f"url({data_uri(fonts / name, 'font/woff2')})")

    # photos: each embedded once as a CSS variable or SVG symbol, then referenced
    html = rep(html, ":root{\n", f":root{{\n  --me:url({data_uri(clips / 'me.jpg', 'image/jpeg')});\n  --cut:url({data_uri(clips / 'me-cut.png', 'image/png')});\n")
    html = rep(html, "url(clips/me.jpg)", "var(--me)", 3)
    html = rep(html, "url(clips/me-cut.png)", "var(--cut)", 2)
    html, n = re.subn(r'<img src="clips/me\.jpg" alt="([^"]*)">', r'<span class="ph" role="img" aria-label="\1"></span>', html)
    assert n == 24, n
    html = rep(html, "<defs>\n", f'<defs>\n    <symbol id="fig" viewBox="0 0 300 400" preserveAspectRatio="none"><image href="{data_uri(clips / "me-figure.png", "image/png")}" width="300" height="400"/></symbol>\n')
    html, n = re.subn(r'<image href="clips/me-figure\.png" (x="[^"]*" y="[^"]*" width="[^"]*" height="[^"]*") preserveAspectRatio="none"', r'<use href="#fig" \1', html)
    assert n == 72, n
    # the photo inside SVG sketches (#commandchat), cropped like an <img> with object-fit: cover
    html = rep(html, "<defs>\n", f'<defs>\n    <symbol id="mej" viewBox="0 0 540 960" preserveAspectRatio="xMidYMid slice"><image href="{data_uri(clips / "me.jpg", "image/jpeg")}" width="540" height="960"/></symbol>\n')
    html, n = re.subn(r'<image href="clips/me\.jpg" (x="[^"]*" y="[^"]*" width="[^"]*" height="[^"]*") preserveAspectRatio="xMidYMid slice"/>', r'<use href="#mej" \1/>', html)
    assert n == 2, n
    assert "clips/" not in html and "fonts/" not in html, "a relative asset is left"

    # words for strangers
    html = rep(html, "106 Reel styles from @_growwithak as a free Claude Code skill. Download it,", "106 Reel styles by @_growwithak as a free Claude Code skill pack. Install it,")
    html = rep(html, "</style>", EXTRA_CSS + "</style>")
    html = rep(html, '<a class="btn" href="#how">How to use it</a>', '<a class="btn" href="#install">Install the pack</a>')
    html = rep(html, '<section class="wrap how" id="how">', INSTALL + '\n<section class="wrap how" id="how">')
    html = rep(html, '<h3>Get the Style Pack</h3><p>You already have it. Open the Claude app, click the Code tab, drag the zip in and say:</p><pre>install this skill for me</pre>',
               '<h3>Install the pack</h3><p>Once, using any way <a href="#install">above</a>. Then open the Code tab whenever you have a video.</p>')
    html = rep(html, '"Use the growwithak-styles skill to edit', '"Use the growwithak-style-pack skill to edit')
    html = rep(html, "free to use on your own videos</footer>", 'free to use on your own videos, please don\'t resell the pack · fonts: Fraunces and Figtree (SIL Open Font License)</footer>')
    html = rep(html, "</body>", EXTRA_JS + "</body>")
    owner, name = repo.split("/")
    html = html.replace("__REPO__", repo).replace("__ZIPURL__", f"https://{owner}.github.io/{name}/{ZIP}")

    for out in (SKILL / "guide" / "index.html", ROOT / "docs" / "index.html"):
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(html)
        print(f"wrote {out.relative_to(ROOT)}  {len(html) / 1e6:.2f} MB")

    # the skill folder as one zip, without Finder clutter
    out = ROOT / "docs" / ZIP
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        for f in sorted(SKILL.rglob("*")):
            if f.is_file() and f.name != ".DS_Store":
                # fixed date: no local file times in the public zip
                info = zipfile.ZipInfo(str(f.relative_to(SKILL.parent)), date_time=(2026, 1, 1, 0, 0, 0))
                info.compress_type, info.external_attr, info.create_system = zipfile.ZIP_DEFLATED, 0o644 << 16, 3
                z.writestr(info, f.read_bytes())
    print(f"wrote {out.relative_to(ROOT)}  {out.stat().st_size / 1e6:.2f} MB")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default=REPO, help="GitHub owner/repo")
    build(ap.parse_args().repo)

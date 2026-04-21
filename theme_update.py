import sys

file_path = "c:\\Users\\kajet\\Desktop\\Kamila Cieciura\\index.html"
with open(file_path, "r", encoding="utf-8") as f:
    text = f.read()

replacements = [
    (
"""    :root {
      --bg: #09090b;
      --bg-soft: #121214;
      --accent: #d4af37;
      --accent-glow: rgba(212, 175, 55, 0.15);
      --text: #ffffff;
      --muted: #a1a1aa;
      --line: rgba(255, 255, 255, 0.08);
      --glass-bg: rgba(18, 18, 20, 0.65);
      --glass-border: rgba(255, 255, 255, 0.08);
      --shadow: 0 30px 60px rgba(0, 0, 0, 0.8);
      --shadow-soft: 0 15px 35px rgba(0, 0, 0, 0.4);
      --container: 1100px;
      --radius: 24px;
      --transition: 0.5s cubic-bezier(0.2, 0.8, 0.2, 1);
      --nav-height: 96px;
    }""",
"""    :root {
      --bg: #ffffff;
      --bg-soft: #fafafa;
      --accent: #000000;
      --accent-pink: #fbcfe8;
      --accent-glow: rgba(251, 207, 232, 0.4);
      --text: #171717;
      --muted: #737373;
      --line: rgba(0, 0, 0, 0.08);
      --glass-bg: rgba(255, 255, 255, 0.65);
      --glass-border: rgba(0, 0, 0, 0.08);
      --shadow: 0 30px 60px rgba(0, 0, 0, 0.08);
      --shadow-soft: 0 15px 35px rgba(0, 0, 0, 0.04);
      --container: 1100px;
      --radius: 24px;
      --transition: 0.5s cubic-bezier(0.2, 0.8, 0.2, 1);
      --nav-height: 96px;
    }"""
    ),
    (
"""    html::after {
      content: "";
      position: fixed;
      bottom: -15vw; right: -10vw;
      width: 60vw; height: 60vw;
      background: radial-gradient(circle, rgba(255, 255, 255, 0.03) 0%, transparent 60%);
      filter: blur(90px);
      z-index: -1;
      pointer-events: none;
    }""",
"""    html::after {
      content: "";
      position: fixed;
      bottom: -15vw; right: -10vw;
      width: 60vw; height: 60vw;
      background: radial-gradient(circle, rgba(0, 0, 0, 0.03) 0%, transparent 60%);
      filter: blur(90px);
      z-index: -1;
      pointer-events: none;
    }"""
    ),
    (
"""    .section { padding: clamp(4rem, 8vw, 7rem) 0; position: relative; }""",
"""    .section { padding: clamp(3rem, 6vw, 5rem) 0; position: relative; }"""
    ),
    (
"""    .nav-cta {
      font-size: 0.75rem;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      padding: 8px 16px;
      border: 1px solid rgba(255, 255, 255, 0.2);
      border-radius: 4px;
      transition: all var(--transition);
      color: var(--text);
    }

    .nav-cta:hover {
      background: rgba(255, 255, 255, 0.05);
      border-color: rgba(255, 255, 255, 0.5);
    }""",
"""    .nav-cta {
      font-size: 0.75rem;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      padding: 8px 16px;
      border: 1px solid rgba(0, 0, 0, 0.2);
      border-radius: 4px;
      transition: all var(--transition);
      color: var(--text);
    }

    .nav-cta:hover {
      background: rgba(0, 0, 0, 0.05);
      border-color: rgba(0, 0, 0, 0.5);
    }"""
    ),
    (
"""    .button::before {
      content: "";
      position: absolute;
      top: 0; left: 0;
      width: 100%; height: 100%;
      background: var(--accent);
      z-index: -1;
      transform: scaleX(0);
      transform-origin: right;
      transition: transform 0.5s cubic-bezier(0.2, 0.8, 0.2, 1);
    }""",
"""    .button::before {
      content: "";
      position: absolute;
      top: 0; left: 0;
      width: 100%; height: 100%;
      background: var(--accent-pink);
      z-index: -1;
      transform: scaleX(0);
      transform-origin: right;
      transition: transform 0.5s cubic-bezier(0.2, 0.8, 0.2, 1);
    }"""
    ),
    (
"""    .button-secondary::before {
      background: rgba(212, 175, 55, 0.1);
    }""",
"""    .button-secondary::before {
      background: var(--accent-pink);
    }"""
    ),
    (
"""    .hero-grid {
      display: grid;
      grid-template-columns: 1.15fr 0.85fr;
      gap: 8vh;
      align-items: center;
    }""",
"""    .hero-grid {
      display: grid;
      grid-template-columns: 1.2fr 0.8fr;
      gap: 4vw;
      align-items: center;
    }"""
    ),
    (
"""    .hero-title {
      margin: 0;
      font-size: clamp(2rem, 5vw, 3.2rem);
      line-height: 1.05;
      font-weight: 200;
      letter-spacing: -0.02em;
      white-space: pre-line;
      background: linear-gradient(135deg, #ffffff 0%, #a1a1aa 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }""",
"""    .hero-title {
      margin: 0;
      font-size: clamp(2rem, 5vw, 3.2rem);
      line-height: 1.05;
      font-weight: 200;
      letter-spacing: -0.02em;
      white-space: pre-line;
      color: var(--text);
    }"""
    ),
    (
"""    .hero-figure-wrap::before {
      content: "";
      position: absolute;
      inset: 0;
      border: 1px solid var(--glass-border);
      border-radius: 4px;
      background: var(--glass-bg);
      backdrop-filter: blur(10px);
      transform: rotate(-3deg);
      transition: transform var(--transition);
      z-index: -1;
    }

    .hero-figure-wrap:hover::before {
      transform: rotate(0deg);
    }""",
"""    .hero-figure-wrap::before {
      display: none;
    }"""
    ),
    (
"""    .hero-figure::after {
      content: "";
      position: absolute;
      inset: 0;
      background: linear-gradient(180deg, transparent 0%, rgba(9, 9, 11, 0.5) 100%);
      pointer-events: none;
    }""",
"""    .hero-figure::after {
      display: none;
    }"""
    ),
    (
"""    .service-card {
      padding: 1.8rem;
      border: 1px solid rgba(255, 255, 255, 0.12);
      border-radius: 6px;
      background: var(--glass-bg);
      backdrop-filter: blur(12px);
      box-shadow: none;
      display: flex;
      flex-direction: column;
      height: 100%;
      position: relative;
      overflow: hidden;
    }

    .service-card::before {
      content: "";
      position: absolute;
      inset: 0;
      background: linear-gradient(180deg, rgba(255,255,255,0.03) 0%, transparent 100%);
      opacity: 0;
      transition: opacity var(--transition);
    }

    .service-card:hover::before {
      opacity: 1;
    }

    .service-card:hover {
      transform: none;
      border-color: rgba(255, 255, 255, 0.35);
      box-shadow: none;
    }""",
"""    .service-card {
      padding: 1.8rem;
      border: 1px solid var(--glass-border);
      border-radius: 6px;
      background: var(--glass-bg);
      backdrop-filter: blur(12px);
      box-shadow: none;
      display: flex;
      flex-direction: column;
      height: 100%;
      position: relative;
      overflow: hidden;
    }

    .service-card::before {
      content: "";
      position: absolute;
      inset: 0;
      background: linear-gradient(180deg, rgba(0,0,0,0.02) 0%, transparent 100%);
      opacity: 0;
      transition: opacity var(--transition);
    }

    .service-card:hover::before {
      opacity: 1;
    }

    .service-card:hover {
      transform: none;
      border-color: var(--accent-pink);
      box-shadow: none;
    }"""
    ),
    (
"""    .icon path[stroke="#C9AA7C"] {
      stroke: var(--accent);
    }""",
"""    .icon path[stroke="#C9AA7C"] {
      stroke: var(--accent-pink);
    }"""
    ),
    (
"""    .offer-media::after {
      content: "";
      position: absolute;
      inset: 24px;
      border: 1px dashed rgba(255, 255, 255, 0.1);
      border-radius: 12px;
      transition: border-color var(--transition);
    }""",
"""    .offer-media::after {
      content: "";
      position: absolute;
      inset: 24px;
      border: 1px dashed rgba(0, 0, 0, 0.1);
      border-radius: 12px;
      transition: border-color var(--transition);
    }"""
    ),
    (
"""      .mobile-tel-btn {
        display: inline-flex;
        padding: 6px 16px;
        border: 1px solid rgba(255, 255, 255, 0.2);
        border-radius: 4px;
        font-size: 0.75rem;
        letter-spacing: 0.08em;
        text-transform: uppercase;
        color: var(--text);
      }""",
"""      .mobile-tel-btn {
        display: inline-flex;
        padding: 6px 16px;
        border: 1px solid rgba(0, 0, 0, 0.2);
        border-radius: 4px;
        font-size: 0.75rem;
        letter-spacing: 0.08em;
        text-transform: uppercase;
        color: var(--text);
      }"""
    )
]

for i, (t, r) in enumerate(replacements):
    if t in text:
        text = text.replace(t, r)
    else:
        print(f"FAILED TO REPLACE BLOCK {i}:\n{t}")
        sys.exit(1)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(text)
print("SUCCESS")

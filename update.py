import sys

file_path = "c:\\Users\\kajet\\Desktop\\Kamila Cieciura\\index.html"
with open(file_path, "r", encoding="utf-8") as f:
    text = f.read()

replacements = [
    (
"""      --shadow-soft: 0 15px 35px rgba(0, 0, 0, 0.4);
      --container: min(1200px, calc(100vw - 48px));
      --radius: 24px;""",
"""      --shadow-soft: 0 15px 35px rgba(0, 0, 0, 0.4);
      --container: 1100px;
      --radius: 24px;"""
    ),
    (
"""    body {
      margin: 0;
      font-family: "Outfit", sans-serif;
      font-weight: 300;
      color: var(--text);
      background: var(--bg);
      line-height: 1.7;""",
"""    body {
      margin: 0;
      font-family: "Outfit", sans-serif;
      font-weight: 300;
      color: var(--text);
      background: var(--bg);
      font-size: 0.95rem;
      line-height: 1.7;"""
    ),
    (
"""    .container { width: var(--container); margin: 0 auto; }
    .section { padding: 120px 0; position: relative; }""",
"""    .container { width: 100%; max-width: var(--container); padding: 0 clamp(1.2rem, 5vw, 2rem); margin: 0 auto; }
    .section { padding: clamp(4rem, 8vw, 7rem) 0; position: relative; }"""
    ),
    (
"""    .section-title {
      margin: 0 0 24px;
      font-size: clamp(2.5rem, 4.5vw, 4rem);
      line-height: 1.1;
      font-weight: 200;
      letter-spacing: -0.02em;
    }

    .section-kicker {
      display: inline-flex;
      align-items: center;
      gap: 16px;
      margin-bottom: 24px;
      color: var(--accent);
      font-size: 0.85rem;
      letter-spacing: 0.3em;
      text-transform: uppercase;
      font-weight: 400;
    }""",
"""    .section-title {
      margin: 0 0 1.2rem;
      font-size: clamp(1.4rem, 3vw, 2rem);
      line-height: 1.1;
      font-weight: 200;
      letter-spacing: -0.02em;
    }

    .section-kicker {
      display: inline-flex;
      align-items: center;
      gap: 16px;
      margin-bottom: 0.5rem;
      color: var(--accent);
      font-size: 0.7rem;
      letter-spacing: 0.15em;
      text-transform: uppercase;
      font-weight: 400;
      opacity: 0.5;
    }"""
    ),
    (
"""    .brand {
      font-family: "Cormorant Garamond", serif;
      font-size: 1.8rem;
      font-style: italic;
      font-weight: 400;
      letter-spacing: 0.02em;
      background: linear-gradient(90deg, #fff, #d4af37);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }

    .nav-links {
      display: flex;
      align-items: center;
      gap: 36px;
      font-size: 0.95rem;
      font-weight: 300;
      color: var(--muted);
    }""",
"""    .brand {
      font-size: 0.85rem;
      font-weight: 400;
      letter-spacing: 0.08em;
      color: var(--text);
    }

    .mobile-tel-btn {
      display: none;
    }

    .nav-links {
      display: flex;
      align-items: center;
      gap: 36px;
      font-size: 0.8rem;
      letter-spacing: 0.06em;
      font-weight: 300;
      color: var(--muted);
    }"""
    ),
    (
"""    .nav-links a:hover::after,
    .nav-links a:focus-visible::after {
      transform: scaleX(1);
      transform-origin: left;
    }

    .button {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      min-height: 52px;
      padding: 0 28px;""",
"""    .nav-links a:hover::after,
    .nav-links a:focus-visible::after {
      transform: scaleX(1);
      transform-origin: left;
    }

    .nav-cta {
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
    }

    .button {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      min-height: 54px;
      padding: 0 32px;"""
    ),
    (
"""    .button-secondary {
      background: transparent;
      color: var(--text);
      border-color: var(--line);
    }""",
"""    .button-secondary {
      background: transparent;
      color: var(--text);
      border-color: var(--line);
      min-height: 44px;
      padding: 0 24px;
      font-size: 0.85rem;
    }"""
    ),
    (
"""    .eyebrow {
      margin-bottom: 24px;
      color: var(--accent);
      font-size: 0.85rem;
      letter-spacing: 0.4em;
      text-transform: uppercase;
      font-weight: 400;
    }

    .hero-title {
      margin: 0;
      font-size: clamp(3rem, 6vw, 5.5rem);""",
"""    .eyebrow {
      margin-bottom: 24px;
      color: var(--accent);
      font-size: 0.75rem;
      letter-spacing: 0.12em;
      text-transform: uppercase;
      font-weight: 400;
      opacity: 0.55;
    }

    .hero-title {
      margin: 0;
      font-size: clamp(2rem, 5vw, 3.2rem);"""
    ),
    (
"""    .hero-figure-wrap::before {
      content: "";
      position: absolute;
      inset: 0;
      border: 1px solid var(--glass-border);
      border-radius: calc(var(--radius) * 1.5);
      background: var(--glass-bg);
      backdrop-filter: blur(10px);
      transform: rotate(-3deg);
      transition: transform var(--transition);
      z-index: -1;
    }

    .hero-figure-wrap:hover::before {
      transform: rotate(0deg);
    }

    .hero-figure {
      position: relative;
      overflow: hidden;
      border-radius: var(--radius);
      min-height: 700px;
      background: var(--bg-soft);
      box-shadow: var(--shadow);
    }""",
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
    }

    .hero-figure {
      position: relative;
      overflow: hidden;
      border-radius: 4px;
      height: 520px;
      background: var(--bg-soft);
      box-shadow: var(--shadow);
    }"""
    ),
    (
"""    .pull-quote {
      margin: 0;
      font-family: "Cormorant Garamond", serif;
      font-style: italic;
      font-weight: 300;
      font-size: clamp(2rem, 4vw, 3.2rem);
      line-height: 1.2;
      color: var(--text);
    }

    .about-copy {
      position: relative;
      padding-top: 32px;
      max-width: 500px;
      color: var(--muted);
      font-size: 1.1rem;
    }""",
"""    .pull-quote {
      margin: 0;
      font-family: "Cormorant Garamond", serif;
      font-style: italic;
      font-weight: 300;
      font-size: 1.15rem;
      line-height: 1.5;
      color: var(--text);
      border-left: 2px solid var(--accent);
      padding-left: 1rem;
    }

    .about-copy {
      position: relative;
      padding-top: 32px;
      max-width: 620px;
      color: var(--muted);
      font-size: 1.1rem;
    }"""
    ),
    (
"""    .service-card {
      padding: 48px 40px;
      border: 1px solid var(--glass-border);
      border-radius: var(--radius);
      background: var(--glass-bg);
      backdrop-filter: blur(12px);
      box-shadow: 0 15px 35px rgba(0,0,0,0.2);
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
      transform: translateY(-8px);
      border-color: rgba(212, 175, 55, 0.4);
      box-shadow: 0 25px 50px rgba(0,0,0,0.5);
    }""",
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
    }"""
    ),
    (
"""    .service-card h3,
    .offer-card h3 {
      margin: 0 0 16px;
      font-size: 1.4rem;
      font-weight: 400;
      letter-spacing: 0.02em;
    }""",
"""    .service-card h3,
    .offer-card h3 {
      margin: 0 0 16px;
      font-size: 1.05rem;
      font-weight: 400;
      letter-spacing: 0.02em;
    }"""
    ),
    (
"""    .contact-form {
      max-width: 600px;
      margin: 0 auto;
      display: grid;
      gap: 32px;
    }

    .field {
      text-align: left;
    }

    .field label {
      display: block;
      margin-bottom: 8px;
      font-size: 0.85rem;
      color: var(--muted);
      letter-spacing: 0.1em;
      text-transform: uppercase;
      transition: color var(--transition);
    }

    .field input,
    .field textarea {
      width: 100%;
      padding: 12px 0;
      border: 0;
      border-bottom: 1px solid var(--line);
      background: transparent;
      outline: none;
      transition: all var(--transition);
      resize: vertical;
      color: var(--text);
      font-family: "Outfit", sans-serif;
    }""",
"""    .contact-form {
      max-width: 520px;
      margin: 0 auto;
      display: grid;
      gap: 32px;
    }

    .field {
      text-align: left;
    }

    .field label {
      display: block;
      margin-bottom: 8px;
      font-size: 0.85rem;
      color: var(--muted);
      letter-spacing: 0.1em;
      text-transform: uppercase;
      transition: color var(--transition);
    }

    .field input,
    .field textarea {
      width: 100%;
      padding: 0.6rem 0;
      border: 0;
      border-bottom: 1px solid var(--line);
      background: transparent;
      outline: none;
      transition: all var(--transition);
      resize: vertical;
      color: var(--text);
      font-family: "Outfit", sans-serif;
    }"""
    ),
    (
"""    .field textarea {
      min-height: 140px;
    }

    .footer {""",
"""    .field textarea {
      min-height: 140px;
    }

    .contact-form button[type="submit"] {
      width: 100%;
      padding: 0.9rem;
      letter-spacing: 0.08em;
    }

    .footer {"""
    ),
    (
"""    .footer {
      padding: 32px 0 48px;
      border-top: 1px solid var(--line);
      color: var(--muted);
      font-size: 0.95rem;
    }

    .footer-line {
      display: flex;
      justify-content: space-between;
      gap: 24px;
      flex-wrap: wrap;
    }""",
"""    .footer {
      padding: 32px 0 48px;
      border-top: 1px solid var(--line);
      color: var(--muted);
      font-size: 0.75rem;
      opacity: 0.45;
    }

    .footer-line {
      display: flex;
      justify-content: center;
      gap: 24px;
      flex-wrap: wrap;
    }"""
    ),
    (
"""      .nav-inner {
        align-items: flex-start;
        flex-direction: column;
        gap: 16px;
      }

      .nav-links {
        width: 100%;
        flex-wrap: wrap;
        justify-content: space-between;
        gap: 16px;
        font-size: 0.9rem;
      }

      .brand { font-size: 1.6rem; }
      .button { width: 100%; }

      .hero {
        min-height: auto;
        padding-top: calc(var(--nav-height) + 60px);
      }

      .hero-title { font-size: clamp(2.8rem, 12vw, 3.8rem); }""",
"""      .nav-inner {
        flex-direction: row;
        align-items: center;
        justify-content: space-between;
      }

      .mobile-tel-btn {
        display: inline-flex;
        padding: 6px 16px;
        border: 1px solid rgba(255, 255, 255, 0.2);
        border-radius: 4px;
        font-size: 0.75rem;
        letter-spacing: 0.08em;
        text-transform: uppercase;
        color: var(--text);
      }

      .nav-links {
        display: none;
      }

      .brand { font-size: 0.9rem; }
      .button, .contact-form button[type="submit"] { width: 100%; }

      .services-grid { gap: 1rem; }

      .hero {
        min-height: auto;
        padding-top: calc(var(--nav-height) + 60px);
      }

      .hero-title { font-size: 2rem; }"""
    ),
    (
"""    <div class="container nav-inner">
      <a class="brand" href="#start">Kamila Cieciura</a>
      <nav class="nav-links" aria-label="Nawigacja główna">
        <a href="#o-mnie">O mnie</a>
        <a href="#uslugi">Usługi</a>
        <a href="#oferty">Oferty</a>
        <a href="#kontakt" class="button">Skontaktuj się</a>
      </nav>
    </div>""",
"""    <div class="container nav-inner">
      <a class="brand" href="#start">Kamila Cieciura</a>
      <a href="tel:+48660734328" class="mobile-tel-btn" aria-label="Zadzwoń">Zadzwoń</a>
      <nav class="nav-links" aria-label="Nawigacja główna">
        <a href="#o-mnie">O mnie</a>
        <a href="#uslugi">Usługi</a>
        <a href="#oferty">Oferty</a>
        <a href="#kontakt" class="nav-cta">Skontaktuj się</a>
      </nav>
    </div>"""
    )
]

for t, r in replacements:
    if t in text:
        text = text.replace(t, r)
    else:
        print(f"FAILED TO REPLACE:\\n{t}")
        sys.exit(1)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(text)
print("SUCCESS")

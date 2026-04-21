import sys

file_path = "c:\\Users\\kajet\\Desktop\\Kamila Cieciura\\index.html"
with open(file_path, "r", encoding="utf-8") as f:
    text = f.read()

replacements = [
    (
        ".hero-title {\n      margin: 0;\n      font-size: clamp(2rem, 5vw, 3.2rem);",
        ".hero-title {\n      margin: 0;\n      font-size: clamp(2.2rem, 4vw, 3.4rem);"
    ),
    (
"""    .about-block {
      background: var(--glass-bg);
      border: 1px solid var(--glass-border);
      backdrop-filter: blur(20px);
      border-radius: calc(var(--radius) * 1.5);
      padding: clamp(48px, 6vw, 80px);
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 64px;
      align-items: center;
      position: relative;
      overflow: hidden;
      box-shadow: var(--shadow-soft);
    }

    .about-block::before {
      content: "";
      position: absolute;
      top: -50%; right: -50%;
      width: 100%; height: 100%;
      background: radial-gradient(circle, var(--accent-glow) 0%, transparent 60%);
      pointer-events: none;
    }""",
"""    .about-section {
      padding: 5rem 0;
    }

    .about-container {
      max-width: 640px;
      margin: 0 auto;
    }"""
    ),
    (
"""    .about-copy {
      position: relative;
      padding-top: 32px;
      max-width: 620px;
      color: var(--muted);
      font-size: 1.1rem;
    }""",
"""    .about-copy {
      position: relative;
      padding-top: 32px;
      color: var(--muted);
      font-size: 1.1rem;
    }"""
    ),
    (
"""    <section class="section" id="o-mnie">
      <div class="container">
        <div class="about-block reveal">
          <div>
            <div class="section-kicker">O mnie</div>
            <p class="pull-quote">Nieruchomość to nie tylko adres. To decyzja, która powinna być poprowadzona spokojnie, uważnie i z klasą.</p>
          </div>
          <div class="about-copy">
            Nazywam się Kamila Cieciura i jestem licencjonowaną agentką nieruchomości, działającą na rynku Lublina i Warszawy. Łączę estetykę prezentacji z praktyką sprzedaży, dzięki czemu każda współpraca ma jasny kierunek: bezpieczeństwo procesu, mocne pozycjonowanie oferty i realny rezultat. Pracuję osobiście, z dbałością o szczegóły, komunikację i tempo dopasowane do klienta.
          </div>
        </div>
      </div>
    </section>""",
"""    <section class="about-section" id="o-mnie">
      <div class="container about-container reveal">
        <div class="section-kicker">O mnie</div>
        <p class="pull-quote">Nieruchomość to nie tylko adres. To decyzja, która powinna być poprowadzona spokojnie, uważnie i z klasą.</p>
        <div class="about-copy">
          Nazywam się Kamila Cieciura i jestem licencjonowaną agentką nieruchomości, działającą na rynku Lublina i Warszawy. Łączę estetykę prezentacji z praktyką sprzedaży, dzięki czemu każda współpraca ma jasny kierunek: bezpieczeństwo procesu, mocne pozycjonowanie oferty i realny rezultat. Pracuję osobiście, z dbałością o szczegóły, komunikację i tempo dopasowane do klienta.
        </div>
      </div>
    </section>"""
    ),
    (
"""    .contact-section {
      background: transparent;
      border: 1px solid var(--glass-border);
      border-radius: calc(var(--radius) * 1.5);
      text-align: center;
      padding: clamp(60px, 8vw, 100px) 24px;
      position: relative;
      overflow: hidden;
      box-shadow: var(--shadow-soft);
    }

    .contact-section::before {
      content: "";
      position: absolute;
      top: 0; left: 0;
      width: 100%; height: 100%;
      background: var(--glass-bg);
      backdrop-filter: blur(30px);
      z-index: -1;
    }""",
"""    .contact-section {
      text-align: center;
      padding: 0;
    }"""
    ),
    (
"""    .contact-phone {
      display: inline-block;
      margin: 16px 0 48px;
      font-size: clamp(2rem, 5vw, 3.5rem);
      font-weight: 200;
      letter-spacing: 0.05em;
      color: var(--text);
      position: relative;
    }""",
"""    .contact-phone {
      display: inline-block;
      margin: 16px 0 48px;
      font-size: 1.6rem;
      font-weight: 200;
      letter-spacing: 0.05em;
      color: var(--text);
      position: relative;
    }"""
    ),
    (
"""    <section class="section" id="oferty">
      <div class="container">
        <h2 class="section-title reveal" style="--delay: 0.08s;">Aktualne oferty</h2>
        <div class="offers-grid">
          <article class="offer-card reveal" style="--delay: 0.12s;">
            <div class="offer-media" aria-hidden="true"></div>
            <div class="offer-content">
              <span class="offer-tag">[Miasto / Powierzchnia]</span>
              <h3>[Tytuł oferty]</h3>
              <p>[Krótki opis oferty, atuty, lokalizacja]</p>
              <p class="offer-price">[Cena]</p>
            </div>
          </article>

          <article class="offer-card reveal" style="--delay: 0.2s;">
            <div class="offer-media" aria-hidden="true"></div>
            <div class="offer-content">
              <span class="offer-tag">[Miasto / Powierzchnia]</span>
              <h3>[Tytuł oferty]</h3>
              <p>[Krótki opis oferty, atuty, lokalizacja]</p>
              <p class="offer-price">[Cena]</p>
            </div>
          </article>
        </div>
      </div>
    </section>""",
"""    <section class="section offers-section" id="oferty">
      <div class="container" style="text-align: center;">
        <h2 class="section-title reveal" style="--delay: 0.08s;">Aktualne oferty</h2>
        <p class="reveal" style="font-size: 1rem; opacity: 0.45; margin-top: 2rem; --delay: 0.15s;">Oferty pojawią się wkrótce.</p>
      </div>
    </section>"""
    ),
    (
"""    .offers-grid {
      grid-template-columns: repeat(2, minmax(0, 1fr));
      margin-top: 48px;
    }""",
"""    .offers-section {
      padding: 3rem 0;
    }

    .offers-grid {
      grid-template-columns: repeat(2, minmax(0, 1fr));
      margin-top: 48px;
    }"""
    ),
    (
"""    .icon {
      width: 48px; height: 48px;
      margin-bottom: 32px;
      color: var(--text);
      transition: transform var(--transition), color var(--transition);
    }""",
"""    .icon {
      width: 2rem; height: 2rem;
      margin-bottom: 32px;
      color: var(--text);
      opacity: 0.7;
      transition: transform var(--transition), color var(--transition);
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

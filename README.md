<body>
  <div class="wrap">
    <div class="badges" aria-hidden="true">
      <img src="https://img.shields.io/badge/Team-Pentadex-blue?style=for-the-badge" alt="Team Pentadex" class="badge">
      <img src="https://img.shields.io/badge/Version-1.0-green?style=for-the-badge" alt="Version 1.0" class="badge">
      <img src="https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge" alt="Python 3.8+" class="badge">
      <img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge" alt="License MIT" class="badge">
    </div>
  </body>

    <h1>Professional Open Source Intelligence Tool for Security Researchers</h1>
    <p class="lead">A compact, focused README-style preview. Cleanly structured with sections for Features, Installation, Plugins, Configuration, and Support.</p>

    <div class="grid">
      <div class="card">
        <div class="section-title"><span class="pill">Overview</span></div>
        <p>Pentadex is a lightweight OSINT toolkit designed to help security researchers collect, normalize, and analyze publicly available information quickly and responsibly.</p>

        <div style="margin-top:12px" class="section-title"><span class="pill">Features</span></div>
        <div class="features">
          <div class="feature">Fast data collection (multi-threaded)</div>
          <div class="feature">Plugin-based architecture</div>
          <div class="feature">Extensible parsers & normalizers</div>
          <div class="feature">Export to JSON/CSV</div>
        </div>

        <div style="margin-top:12px" class="section-title"><span class="pill">Quick Install</span></div>
        <pre><code>git clone https://github.com/yourusername/pentadex
cd pentadex
python3 -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
</code></pre>

        <div style="margin-top:12px" class="section-title"><span class="pill">Run</span></div>
        <pre><code>python run.py --config config.yml</code></pre>

        <div style="margin-top:12px" class="section-title"><span class="pill">Plugins</span></div>
        <p>Drop plugins into <code>./plugins/</code>. Each plugin must implement a <code>run()</code> method and expose metadata in <code>plugin.yml</code>.</p>

        <div style="margin-top:12px" class="section-title"><span class="pill">Configuration</span></div>
        <pre><code># config.yml (example)
input: targets.txt
output: results/
threads: 8
</code></pre>

        <div style="margin-top:12px" class="section-title"><span class="pill">Support</span></div>
        <p class="toc">Issues &amp; PRs on GitHub. For security disclosures, please use the SECURITY.md process in the repo.</p>
      </div>

      <aside class="right">
        <div class="card" style="margin-bottom:12px">
          <div class="section-title"><span class="pill">Table of Contents</span></div>
          <nav class="toc">
            • Overview<br>
            • Features<br>
            • Installation<br>
            • Run<br>
            • Plugins<br>
            • Configuration<br>
            • Support
          </nav>
        </div>

        <div class="card">
          <div class="section-title"><span class="pill">Badge-only (no links)</span></div>
          <p class="toc">The header shows rendered shield badges as images only (not clickable) so they work inside README previews and exported HTML with consistent visuals.</p>
        </div>
      </aside>
    </div>

    <footer>Made with ♥ — Customize this file and paste the HTML into <code>README_preview.html</code> or convert to Markdown as needed.</footer>
  </div>
</body>
</html>

<!doctype html>
<html lang="bn">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>Pentadex — README Preview</title>
  <style>
    :root{--bg:#0f1724;--card:#0b1220;--accent:#0ea5e9;--muted:#94a3b8;--glass:rgba(255,255,255,0.04)}
    *{box-sizing:border-box}
    html,body{height:100%;margin:0;font-family:Inter,ui-sans-serif,system-ui,-apple-system,"Segoe UI",Roboto,'Helvetica Neue',Arial; background:linear-gradient(180deg,#071022 0%, #071827 60%);color:#e6eef8}
    .wrap{max-width:980px;margin:36px auto;padding:28px;background:linear-gradient(180deg,rgba(255,255,255,0.02),transparent);border-radius:14px;box-shadow:0 6px 30px rgba(2,6,23,0.6);border:1px solid rgba(255,255,255,0.03)}
    .badges{display:flex;gap:10px;flex-wrap:wrap;justify-content:center;margin-bottom:18px}
    .badge{display:inline-block;padding:6px;border-radius:12px;background:var(--glass);backdrop-filter:blur(6px)}
    h1{font-size:28px;margin:6px 0 4px;text-align:center}
    p.lead{color:var(--muted);text-align:center;margin:0 0 18px}
    .grid{display:grid;grid-template-columns:1fr 320px;gap:20px}
    @media (max-width:880px){.grid{grid-template-columns:1fr}}
    .card{background:linear-gradient(180deg,rgba(255,255,255,0.01),transparent);padding:18px;border-radius:12px;border:1px solid rgba(255,255,255,0.03)}
    .features{display:grid;grid-template-columns:repeat(2,1fr);gap:10px}
    @media (max-width:520px){.features{grid-template-columns:1fr}}
    .feature{padding:10px;background:rgba(255,255,255,0.02);border-radius:8px}
    pre, code{background:#071126;padding:10px;border-radius:8px;color:#cdebf7;overflow:auto}
    .right{position:relative}
    .toc{font-size:14px;color:var(--muted);line-height:1.7}
    .section-title{display:flex;align-items:center;gap:10px;margin-bottom:8px}
    .pill{font-size:12px;background:rgba(255,255,255,0.03);padding:6px 10px;border-radius:999px}
    footer{margin-top:18px;color:var(--muted);font-size:13px;text-align:center}
  </style>
</head>
<body>
  <div class="wrap">
    <div class="badges" aria-hidden="true">
      <img src="https://img.shields.io/badge/Team-Pentadex-blue?style=for-the-badge" alt="Team Pentadex" class="badge">
      <img src="https://img.shields.io/badge/Version-1.0-green?style=for-the-badge" alt="Version 1.0" class="badge">
      <img src="https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge" alt="Python 3.8+" class="badge">
      <img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge" alt="License MIT" class="badge">
    </div>

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

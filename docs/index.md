---
hide:
  - navigation
  - toc
---

<div class="zuni-site" id="top">

<header class="zuni-topbar">
  <a class="zuni-wordmark" href="#top" aria-label="Zuni home"><span aria-hidden="true">&gt;_</span> zuni<span class="zuni-cursor" aria-hidden="true"></span></a>
  <nav aria-label="Primary navigation" class="zuni-nav">
    <a href="#features">Features</a>
    <a href="#quick-start">Quick start</a>
    <a href="getting-started/installation">Docs <span aria-hidden="true">↗</span></a>
    <a href="https://github.com/ssannssarr/Zuni">GitHub <span aria-hidden="true">↗</span></a>
  </nav>
  <button class="zuni-copy-top" data-copy="uv tool install ssannssarr.zuni"><span aria-hidden="true">$</span> <span data-copy-label>uv tool install</span></button>
  <button class="zuni-menu-toggle" type="button" aria-expanded="false" aria-controls="zuni-mobile-nav" aria-label="Open menu"><span></span><span></span></button>
</header>
<nav id="zuni-mobile-nav" class="zuni-mobile-nav" aria-label="Mobile navigation" hidden>
  <a href="#features">Features</a><a href="#quick-start">Quick start</a><a href="getting-started/installation/">Docs ↗</a><a href="https://github.com/ssannssarr/Zuni">GitHub ↗</a>
</nav>

<main id="zuni-main">
<section class="zuni-hero" aria-labelledby="zuni-hero-title">
  <div class="zuni-grid" aria-hidden="true"></div>
  <div class="zuni-hero-inner">
    <div class="zuni-eyebrow zuni-hero-eyebrow"><span class="zuni-live-dot"></span> OPEN-SOURCE CLI <span class="zuni-eyebrow-divider"></span> PYTHON ≥ 3.11 <span class="zuni-eyebrow-divider"></span> MIT LICENSE</div>
    <h1 id="zuni-hero-title" class="zuni-display"><span class="zuni-reveal-line">Research, without</span><span class="zuni-reveal-line">leaving your <em>terminal.</em></span></h1>
    <div class="zuni-hero-bottom">
      <div class="zuni-hero-copy">
        <p>Zuni pairs an OpenAI-compatible model with web search, reads the pages it finds, and answers your question <strong>with source citations</strong>, right where you already work.</p>
        <div class="zuni-command-chip"><span class="zuni-prompt">$</span><code>uv tool install ssannssarr.zuni</code><button class="zuni-copy-button" data-copy="uv tool install ssannssarr.zuni" aria-label="Copy install command"><span data-copy-label>copy</span></button></div>
        <div class="zuni-actions"><a class="zuni-button zuni-button-signal" href="https://github.com/ssannssarr/Zuni">View on GitHub <span aria-hidden="true">↗</span></a><a class="zuni-button zuni-button-outline" href="getting-started/installation/">Read the docs <span aria-hidden="true">↗</span></a></div>
      </div>
      <figure class="zuni-terminal zuni-hero-terminal" data-reveal>
        <figcaption class="zuni-terminal-bar"><span class="zuni-window-dots" aria-hidden="true"><i></i><i></i><i></i></span><span class="zuni-terminal-title">~/research — zuni ask</span><span class="zuni-terminal-tag">ILLUSTRATIVE</span></figcaption>
        <div class="zuni-terminal-body zuni-hero-output">
          <div class="zuni-command-line"><span class="zuni-prompt">~ $</span> <code>zuni ask "What is quantum computing?"</code></div>
          <div class="zuni-output-lines">
            <p class="zuni-status"><span>›</span> searching the web</p>
            <p class="zuni-status"><span>›</span> extracting readable page content</p>
            <p class="zuni-status"><span>›</span> synthesizing answer</p>
            <p class="zuni-answer">Quantum computing uses qubits, which can exist in superpositions of 0 and 1, and exploits entanglement and interference to solve certain problems faster than classical machines <sup>[1][2]</sup>.</p>
            <p class="zuni-source-label">SOURCES</p>
            <p class="zuni-source"><span>[1]</span> en.wikipedia.org/wiki/Quantum_computing</p>
            <p class="zuni-source"><span>[2]</span> ibm.com/think/topics/quantum-computing</p>
          </div>
        </div>
        <div class="zuni-terminal-footer"><span>Sample output for illustration · not a live query</span><button type="button" class="zuni-replay">↻ replay</button></div>
      </figure>
    </div>
  </div>
</section>

<section class="zuni-section zuni-demo-section" aria-labelledby="zuni-demo-title">
  <div class="zuni-section-head" data-reveal>
    <div><div class="zuni-eyebrow"><span class="zuni-section-number">01</span><span class="zuni-rule"></span> IN THE TERMINAL</div><h2 id="zuni-demo-title" class="zuni-display">One command.<br><em>Three ways</em> to ask.</h2></div>
    <p>A local walkthrough of real Zuni commands. The sample output is illustrative: nothing here calls a model or the web.</p>
  </div>
  <div class="zuni-demo-layout">
    <div class="zuni-demo-tabs" role="tablist" aria-label="Example commands" aria-orientation="vertical">
      <button class="zuni-demo-tab is-active" role="tab" id="zuni-tab-ask" aria-selected="true" aria-controls="zuni-panel-ask" tabindex="0" data-demo="ask"><span class="zuni-tab-title">Ask</span><code>default</code><small>Searches the web, reads pages, answers with sources.</small></button>
      <button class="zuni-demo-tab" role="tab" id="zuni-tab-no-search" aria-selected="false" aria-controls="zuni-panel-no-search" tabindex="-1" data-demo="no-search"><span class="zuni-tab-title">No search</span><code>--no-search</code><small>Skips the web step and answers from the model alone.</small></button>
      <button class="zuni-demo-tab" role="tab" id="zuni-tab-results" aria-selected="false" aria-controls="zuni-panel-results" tabindex="-1" data-demo="results"><span class="zuni-tab-title">Results count</span><code>-n 3</code><small>Limits how many search results feed the answer.</small></button>
      <div class="zuni-demo-copy"><span class="zuni-eyebrow">TRY IT YOURSELF</span><div class="zuni-command-row"><code data-demo-command>zuni ask "What is quantum computing?"</code><button data-copy='zuni ask "What is quantum computing?"' aria-label="Copy example command"><span data-copy-label>copy</span></button></div></div>
    </div>
    <div class="zuni-demo-panel-wrap">
      <section class="zuni-terminal zuni-demo-panel" id="zuni-panel-ask" role="tabpanel" aria-labelledby="zuni-tab-ask" data-panel="ask">
        <figcaption class="zuni-terminal-bar"><span class="zuni-window-dots" aria-hidden="true"><i></i><i></i><i></i></span><span class="zuni-terminal-title">zuni ask</span><span class="zuni-terminal-tag">ILLUSTRATIVE</span></figcaption>
        <div class="zuni-terminal-body"><div class="zuni-command-line"><span class="zuni-prompt">~ $</span> <code data-panel-command>zuni ask "What is quantum computing?"</code></div><div class="zuni-demo-output" data-output="ask"><p class="zuni-status"><span>›</span> searching the web</p><p class="zuni-status"><span>›</span> extracting readable page content</p><p class="zuni-status"><span>›</span> synthesizing answer</p><p class="zuni-answer">Quantum computing is a model of computation built on quantum-mechanical effects. Its basic unit, the qubit, can hold a superposition of states <sup>[1]</sup>.</p><p class="zuni-answer">Algorithms use entanglement and interference to amplify useful outcomes, offering speed-ups for certain problems <sup>[1][2]</sup>.</p><p class="zuni-source-label">SOURCES</p><p class="zuni-source"><span>[1]</span> en.wikipedia.org/wiki/Quantum_computing</p><p class="zuni-source"><span>[2]</span> ibm.com/think/topics/quantum-computing</p></div>
        <div class="zuni-demo-output" data-output="no-search" hidden><p class="zuni-status"><span>›</span> web search skipped</p><p class="zuni-status"><span>›</span> synthesizing answer</p><p class="zuni-answer">Recursion is when a function solves a problem by calling itself on a smaller piece of it. Every recursive function needs a base case that stops the calls, and a step that moves toward it.</p><p class="zuni-answer">factorial(n) = n × factorial(n − 1), with factorial(0) = 1 as the base case.</p><p class="zuni-source-label">NO SOURCES</p><p class="zuni-note">Search was disabled for this illustrative example.</p></div>
        <div class="zuni-demo-output" data-output="results" hidden><p class="zuni-status"><span>›</span> searching the web · 3 results</p><p class="zuni-status"><span>›</span> extracting readable page content</p><p class="zuni-status"><span>›</span> synthesizing answer</p><p class="zuni-answer">Recent CPython releases have focused on performance and concurrency, including free-threaded builds and an experimental JIT compiler <sup>[1][2]</sup>.</p><p class="zuni-source-label">SOURCES</p><p class="zuni-source"><span>[1]</span> docs.python.org/3/whatsnew/</p><p class="zuni-source"><span>[2]</span> peps.python.org/pep-0703/</p></div></div>
        <div class="zuni-terminal-footer"><span data-demo-caption>Searches the web, reads the pages, answers with sources.</span><button type="button" class="zuni-replay">↻ replay</button></div>
      </section>
      <div class="zuni-mobile-copy"><div class="zuni-command-row"><code data-demo-command>zuni ask "What is quantum computing?"</code><button data-copy='zuni ask "What is quantum computing?"' aria-label="Copy example command"><span data-copy-label>copy</span></button></div></div>
    </div>
  </div>
</section>

<section class="zuni-section zuni-flow-section" aria-labelledby="zuni-flow-title">
  <div class="zuni-section-head" data-reveal>
    <div><div class="zuni-eyebrow"><span class="zuni-section-number">02</span><span class="zuni-rule"></span> HOW IT WORKS</div><h2 id="zuni-flow-title" class="zuni-display">From question to <em>citation.</em></h2></div>
    <p>Four steps, every time you run <code>zuni ask</code>. Follow one question through.</p>
  </div>
  <div class="zuni-flow-layout" id="zuni-flow-track">
    <div class="zuni-flow-visual" aria-hidden="true">
      <div class="zuni-flow-sticky">
        <svg class="zuni-flow-diagram" viewBox="0 0 560 120" role="presentation"><path d="M40 60 C120 20 120 100 200 60 S 280 20 360 60 S 440 100 520 60" class="zuni-flow-track"></path><path d="M40 60 C120 20 120 100 200 60 S 280 20 360 60 S 440 100 520 60" class="zuni-flow-progress"></path><g><circle cx="40" cy="60" r="6"></circle><text x="40" y="108">ASK</text></g><g><circle cx="200" cy="60" r="6"></circle><text x="200" y="22">SEARCH</text></g><g><circle cx="360" cy="60" r="6"></circle><text x="360" y="108">SYNTHESIZE</text></g><g><circle cx="520" cy="60" r="6"></circle><text x="520" y="22">CITE</text></g></svg>
        <div class="zuni-flow-artifact" data-flow-artifact><div class="zuni-eyebrow">INPUT</div><p><span class="zuni-prompt">$</span> zuni ask "What is quantum computing?"</p></div>
        <div class="zuni-flow-progress"><span data-flow-step>01</span><span class="zuni-progress-line"><i></i></span><span>04</span></div>
      </div>
    </div>
    <div class="zuni-flow-steps">
      <article class="zuni-flow-step is-active" data-flow-step-index="0"><span class="zuni-flow-big-number">01</span><div class="zuni-eyebrow">STEP 01 <span class="zuni-rule"></span> ASK</div><h3>You ask a question.</h3><p>Type it the way you'd say it. Zuni takes the question straight from the command line. No browser tab, no context switch.</p><div class="zuni-flow-mobile-artifact"><div class="zuni-eyebrow">INPUT</div><p><span class="zuni-prompt">$</span> zuni ask "What is quantum computing?"</p></div></article>
      <article class="zuni-flow-step" data-flow-step-index="1"><span class="zuni-flow-big-number">02</span><div class="zuni-eyebrow">STEP 02 <span class="zuni-rule"></span> SEARCH</div><h3>The web gathers context.</h3><p>Zuni searches the web and extracts readable page content, so the model gets useful text rather than raw markup.</p><p class="zuni-flow-aside"><code>--no-search</code> skips this step · <code>-n</code> sets the result count</p><div class="zuni-flow-mobile-artifact"><div class="zuni-eyebrow">SEARCH → READABLE TEXT</div><p>search result <span>→</span> extracted page text</p></div></article>
      <article class="zuni-flow-step" data-flow-step-index="2"><span class="zuni-flow-big-number">03</span><div class="zuni-eyebrow">STEP 03 <span class="zuni-rule"></span> SYNTHESIZE</div><h3>Your model writes the answer.</h3><p>The context goes to the OpenAI-compatible endpoint you configured: your API key, model ID, and base URL.</p><div class="zuni-flow-mobile-artifact"><div class="zuni-eyebrow">ZUNI CONFIG</div><p>API key <span>••••••••</span><br>model ID <span>&lt;your model&gt;</span><br>base URL <span>&lt;your endpoint&gt;</span></p></div></article>
      <article class="zuni-flow-step" data-flow-step-index="3"><span class="zuni-flow-big-number">04</span><div class="zuni-eyebrow">STEP 04 <span class="zuni-rule"></span> CITE</div><h3>A cited answer, in place.</h3><p>The answer prints in your terminal with its source references, so you can inspect the material behind a claim.</p><div class="zuni-flow-mobile-artifact"><div class="zuni-eyebrow">OUTPUT · ILLUSTRATIVE</div><p>Answer text with source references <span>[1] [2]</span></p></div></article>
    </div>
  </div>
</section>

<section id="features" class="zuni-section zuni-features-section" aria-labelledby="zuni-features-title">
  <div class="zuni-section-head" data-reveal>
    <div><div class="zuni-eyebrow"><span class="zuni-section-number">03</span><span class="zuni-rule"></span> FEATURES</div><h2 id="zuni-features-title" class="zuni-display">Small surface.<br><em>Sharp edges.</em></h2></div>
    <p>Four capabilities, straight from the project. That's the whole tool, and that's the point.</p>
  </div>
  <ol class="zuni-feature-list">
    <li data-reveal><span class="zuni-feature-number">01</span><h3>Automatic web search</h3><p>Search the web by default, then use retrieved pages to ground an answer beyond model memory alone.</p><div class="zuni-feature-detail"><code>zuni ask -n 3 "…"</code><code>zuni ask --no-search "…"</code></div></li>
    <li data-reveal><span class="zuni-feature-number">02</span><h3>Readable page extraction</h3><p>Extract readable content from result pages and give the model useful text to reason over.</p><div class="zuni-feature-detail"><code>page → readable text</code><code>text → model context</code></div></li>
    <li data-reveal><span class="zuni-feature-number">03</span><h3>Source citations</h3><p>Get answers with source references printed beneath the response, ready for you to inspect.</p><div class="zuni-feature-detail"><code>[1] source url</code><code>[2] source url</code></div></li>
    <li data-reveal><span class="zuni-feature-number">04</span><h3>OpenAI-compatible endpoints</h3><p>Use a compatible API endpoint and configure your key, model, and base URL with <code>zuni config</code>.</p><div class="zuni-feature-detail"><code>zuni config</code><code>OpenAI-style API</code></div></li>
  </ol>
</section>

<section id="quick-start" class="zuni-section zuni-quickstart-section" aria-labelledby="zuni-quickstart-title">
  <div class="zuni-grid zuni-grid-subtle" aria-hidden="true"></div>
  <div class="zuni-section-head" data-reveal>
    <div><div class="zuni-eyebrow"><span class="zuni-section-number">04</span><span class="zuni-rule"></span> QUICK START</div><h2 id="zuni-quickstart-title" class="zuni-display">Four commands to a <em>first answer.</em></h2></div>
  </div>
  <div class="zuni-quickstart-layout">
    <ol class="zuni-quickstart-list">
      <li data-reveal><span class="zuni-quickstart-number">01</span><div><h3>Install from PyPI</h3><div class="zuni-command-row"><code>uv tool install ssannssarr.zuni</code><button data-copy="uv tool install ssannssarr.zuni" aria-label="Copy install command"><span data-copy-label>copy</span></button></div><p>Requires Python 3.11 or newer and <code>uv</code>.</p></div></li>
      <li data-reveal><span class="zuni-quickstart-number">02</span><div><h3>Verify the install</h3><div class="zuni-command-row"><code>zuni --help</code><button data-copy="zuni --help" aria-label="Copy help command"><span data-copy-label>copy</span></button></div><p>See the available commands and options.</p></div></li>
      <li data-reveal><span class="zuni-quickstart-number">03</span><div><h3>Configure your model</h3><div class="zuni-command-row"><code>zuni config</code><button data-copy="zuni config" aria-label="Copy config command"><span data-copy-label>copy</span></button></div><p>Set your API key, model ID, and compatible base URL.</p></div></li>
      <li data-reveal><span class="zuni-quickstart-number">04</span><div><h3>Ask your first question</h3><div class="zuni-command-row"><code>zuni ask "What is quantum computing?"</code><button data-copy='zuni ask "What is quantum computing?"' aria-label="Copy first query"><span data-copy-label>copy</span></button></div><p>Add <code>--no-search</code> to skip web research or <code>-n</code> to set the result count.</p></div></li>
    </ol>
    <aside class="zuni-quickstart-aside" data-reveal><span class="zuni-eyebrow">NEED THE DETAILS?</span><h3>There's a command for that.</h3><p>Read the complete installation and configuration guides, or inspect every command option.</p><a class="zuni-text-link" href="getting-started/installation/">Installation guide ↗</a><a class="zuni-text-link" href="getting-started/configuration/">Configuration guide ↗</a><a class="zuni-text-link" href="guide/commands/">Command reference ↗</a></aside>
  </div>
</section>

<section class="zuni-closing" aria-labelledby="zuni-closing-title">
  <div class="zuni-marquee" aria-hidden="true"><div><span>$ uv tool install ssannssarr.zuni</span><span>$ zuni config</span><span>$ zuni ask "What is quantum computing?"</span><span>$ zuni ask --no-search "Explain recursion"</span><span>$ zuni ask -n 3 "Latest developments in Python"</span><span>$ uv tool install ssannssarr.zuni</span><span>$ zuni config</span><span>$ zuni ask "What is quantum computing?"</span></div></div>
  <div class="zuni-closing-inner"><h2 id="zuni-closing-title" class="zuni-display">Ask. Search.<br><em>Cite.</em></h2><div class="zuni-closing-bottom"><p>Zuni is open source under the MIT License. Read the code, file an issue, or send a pull request.</p><div class="zuni-actions"><a class="zuni-button zuni-button-signal" href="https://github.com/ssannssarr/Zuni">github.com/ssannssarr/Zuni ↗</a><a class="zuni-button zuni-button-outline" href="getting-started/installation/">Documentation ↗</a></div></div></div>
  <footer class="zuni-footer"><a class="zuni-wordmark" href="#top"><span aria-hidden="true">&gt;_</span> zuni<span class="zuni-cursor" aria-hidden="true"></span></a><nav aria-label="Footer navigation"><a href="#features">Features</a><a href="#quick-start">Quick start</a><a href="https://github.com/ssannssarr/Zuni">GitHub</a><a href="https://github.com/ssannssarr/Zuni/blob/main/LICENSE">MIT License</a></nav><span>Python ≥ 3.11 · open source</span></footer>
</section>
</main>
<div class="zuni-toast" role="status" aria-live="polite"></div>
</div>

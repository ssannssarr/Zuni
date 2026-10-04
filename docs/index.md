---
hide:
  - navigation
  - toc
---

<div class="zuni-hero">

  <div class="zuni-badge">
    <span class="status-dot"></span>
    CLI-FIRST AI RESEARCH ASSISTANT
  </div>

  <h1>
    One Command.<br>
    <span>Search. Reason. Answer.</span>
  </h1>

  <p class="hero-subtitle">
    Zuni brings AI-assisted research to your terminal.
    Ask a question, let the model use web tools when needed,
    and get a concise answer with sources you can inspect.
  </p>

  <div class="hero-buttons">
    <a href="getting-started/installation/" class="zuni-button primary">Get Started →</a>
    <a href="https://github.com/ssannssarr/Zuni" class="zuni-button secondary">View on GitHub</a>
  </div>

</div>

<div class="terminal-window">
  <div class="terminal-header">
    <div class="terminal-dots">
      <span></span>
      <span></span>
      <span></span>
    </div>
    <div class="terminal-title">zuni</div>
  </div>

  <div class="terminal-body" markdown="1">

```text
$ zuni ask "What is quantum computing?"

→ web_search: quantum computing
→ extract_markdown: https://...

Quantum computing uses quantum-mechanical phenomena
to process information differently from classical
computers. [1]

Sources
[1] Source title
    https://...
```

  </div>
</div>

<div class="section-intro">
  <div class="section-label">WHY ZUNI</div>
  <h2>Research without leaving<br>the terminal.</h2>
  <p>
    Zuni combines an OpenAI-compatible LLM client with
    a small tool-calling agent and web research tools.
  </p>
</div>

<div class="feature-grid">

  <div class="feature-card">
    <div class="feature-icon">⚡</div>
    <h3>One Command</h3>
    <p>Ask a question from the terminal and let Zuni manage the research workflow.</p>
  </div>

  <div class="feature-card">
    <div class="feature-icon">⌕</div>
    <h3>Web Research</h3>
    <p>Search DuckDuckGo and read selected pages when a question needs factual or current information.</p>
  </div>

  <div class="feature-card">
    <div class="feature-icon">◈</div>
    <h3>Grounded Answers</h3>
    <p>Sources are numbered and can be cited inline, making it easier to inspect the material behind an answer.</p>
  </div>

</div>

<div class="section-intro">
  <div class="section-label">THE FLOW</div>
  <h2>From question to answer,<br>through tools.</h2>
</div>

<div class="flow">

  <div class="flow-step">
    <span class="flow-number">01</span>
    <strong>Ask</strong>
    <p>Write your question.</p>
  </div>

  <div class="flow-arrow">→</div>

  <div class="flow-step">
    <span class="flow-number">02</span>
    <strong>Research</strong>
    <p>The model can call search and page-reading tools.</p>
  </div>

  <div class="flow-arrow">→</div>

  <div class="flow-step">
    <span class="flow-number">03</span>
    <strong>Answer</strong>
    <p>Zuni returns a Markdown response with source references.</p>
  </div>

</div>

<div class="code-section" markdown="1">

<div class="section-label">GET STARTED</div>

## Install and meet Zuni in one command.

```bash
uv tool install ssannssarr.zuni
```

Then ask:

```bash
zuni ask "Explain how DNS works"
```

Research tools are available by default. To send the question directly to the model:

```bash
zuni ask --no-search "Explain recursion"
```

<a href="getting-started/installation/" class="text-link">Read the installation guide →</a>

</div>

<div class="project-section">
  <div>
    <div class="section-label">OPEN SOURCE</div>
    <h2>Built in the open.</h2>
    <p>
      Zuni is an evolving open-source project.
      Explore the code, follow the roadmap,
      or contribute to its development.
    </p>
  </div>

  <a href="https://github.com/ssannssarr/Zuni" class="zuni-button secondary">GitHub ↗</a>
</div>

<div class="final-cta">
  <div class="section-label">START EXPLORING</div>
  <h2>Open your terminal.</h2>
  <p>
    Ask the question.<br>
    Let Zuni handle the research.
  </p>
  <a href="getting-started/installation/" class="zuni-button primary">Get Started →</a>
</div>

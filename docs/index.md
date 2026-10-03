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
    Zuni brings AI-powered research to your terminal.
    Ask a question, let Zuni search the web when needed,
    and get a grounded answer without leaving your workflow.
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
to process information in ways that differ from
classical computing. [1]

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
    <p>Ask a question directly from the terminal and let Zuni handle the research loop.</p>
  </div>

  <div class="feature-card">
    <div class="feature-icon">⌕</div>
    <h3>Web Research</h3>
    <p>Search DuckDuckGo and read selected pages when current or factual information is needed.</p>
  </div>

  <div class="feature-card">
    <div class="feature-icon">◈</div>
    <h3>Grounded Answers</h3>
    <p>Sources are numbered and can be cited inline so you can inspect where an answer came from.</p>
  </div>

</div>

<div class="section-intro">
  <div class="section-label">THE FLOW</div>
  <h2>Question to answer,<br>through tools.</h2>
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
    <p>Zuni returns a Markdown response with sources.</p>
  </div>

</div>

<div class="code-section" markdown="1">

<div class="section-label">GET STARTED</div>

## Meet Zuni in one command.

```bash
zuni ask "Explain how DNS works"
```

By default, Zuni can use its research tools. To ask the model directly:

```bash
zuni ask --no-search "Explain recursion"
```

<a href="getting-started/installation/" class="text-link">Read the documentation →</a>

</div>

<div class="project-section">
  <div>
    <div class="section-label">OPEN SOURCE</div>
    <h2>Built in the open.</h2>
    <p>
      Zuni is an evolving project.
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
    The web is huge.<br>
    Your command can stay simple.
  </p>
  <a href="getting-started/installation/" class="zuni-button primary">Get Started →</a>
</div>
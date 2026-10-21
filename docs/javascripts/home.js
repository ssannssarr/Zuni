(() => {
  const root = document.querySelector(".zuni-site");
  if (!root) return;
  const toast = root.querySelector(".zuni-toast");
  let toastTimer;
  const announce = (message) => {
    if (!toast) return;
    toast.textContent = message;
    toast.classList.add("is-visible");
    clearTimeout(toastTimer);
    toastTimer = setTimeout(() => toast.classList.remove("is-visible"), 1800);
  };
  const copyText = async (value) => {
    try {
      if (navigator.clipboard && window.isSecureContext) await navigator.clipboard.writeText(value);
      else {
        const area = document.createElement("textarea");
        area.value = value; area.style.position = "fixed"; area.style.opacity = "0";
        document.body.appendChild(area); area.select();
        const ok = document.execCommand("copy"); area.remove();
        if (!ok) throw new Error("Copy failed");
      }
      announce("Copied to clipboard");
      return true;
    } catch {
      announce("Copy failed. Select the command and copy it manually.");
      return false;
    }
  };
  root.querySelectorAll("[data-copy]").forEach((button) => {
    button.addEventListener("click", async () => {
      const original = button.querySelector("[data-copy-label]")?.textContent || "copy";
      const ok = await copyText(button.getAttribute("data-copy") || "");
      if (!ok) return;
      const label = button.querySelector("[data-copy-label]");
      if (label) label.textContent = "copied";
      button.classList.add("is-copied");
      setTimeout(() => { if (label) label.textContent = original; button.classList.remove("is-copied"); }, 1600);
    });
  });
  const topbar = root.querySelector(".zuni-topbar");
  const onScroll = () => topbar?.classList.toggle("is-scrolled", window.scrollY > 24);
  window.addEventListener("scroll", onScroll, { passive: true }); onScroll();

  const menu = root.querySelector(".zuni-menu-toggle");
  const mobile = root.querySelector("#zuni-mobile-nav");
  const closeMenu = () => { if (!menu || !mobile) return; menu.setAttribute("aria-expanded","false"); menu.setAttribute("aria-label","Open menu"); mobile.hidden = true; };
  menu?.addEventListener("click", () => {
    const open = menu.getAttribute("aria-expanded") !== "true";
    menu.setAttribute("aria-expanded", String(open)); menu.setAttribute("aria-label", open ? "Close menu" : "Open menu");
    if (mobile) mobile.hidden = !open;
  });
  mobile?.querySelectorAll("a").forEach(a => a.addEventListener("click", closeMenu));
  document.addEventListener("keydown", e => { if (e.key === "Escape") { closeMenu(); menu?.focus(); } });

  const scripts = {
    ask: { command: 'zuni ask "What is quantum computing?"', caption: "Searches the web, reads the pages, answers with sources." },
    "no-search": { command: 'zuni ask --no-search "Explain recursion"', caption: "Skips web search and answers from the model alone." },
    results: { command: 'zuni ask -n 3 "Latest developments in Python"', caption: "Limits how many search results feed the answer." }
  };
  const tabs = [...root.querySelectorAll(".zuni-demo-tab")];
  const setDemo = (key, focus = false) => {
    const data = scripts[key] || scripts.ask;
    tabs.forEach(tab => {
      const active = tab.dataset.demo === key;
      tab.classList.toggle("is-active", active);
      tab.setAttribute("aria-selected", String(active)); tab.tabIndex = active ? 0 : -1;
      if (active && focus) tab.focus();
    });
    root.querySelectorAll(".zuni-demo-panel").forEach(panel => {
      const active = panel.dataset.panel === key;
      panel.hidden = !active; panel.setAttribute("aria-labelledby", "zuni-tab-" + key);
    });
    root.querySelectorAll("[data-demo-command]").forEach(el => el.textContent = data.command);
    root.querySelectorAll(".zuni-demo-panel [data-panel-command]").forEach(el => el.textContent = data.command);
    root.querySelectorAll(".zuni-demo-copy [data-copy],.zuni-mobile-copy [data-copy]").forEach(btn => btn.setAttribute("data-copy", data.command));
    root.querySelectorAll(".zuni-demo-panel [data-demo-caption]").forEach(el => el.textContent = data.caption);
  };
  tabs.forEach((tab, i) => {
    tab.addEventListener("click", () => setDemo(tab.dataset.demo));
    tab.addEventListener("keydown", e => {
      let next = i;
      if (e.key === "ArrowRight" || e.key === "ArrowDown") next = (i + 1) % tabs.length;
      else if (e.key === "ArrowLeft" || e.key === "ArrowUp") next = (i - 1 + tabs.length) % tabs.length;
      else if (e.key === "Home") next = 0; else if (e.key === "End") next = tabs.length - 1; else return;
      e.preventDefault(); setDemo(tabs[next].dataset.demo, true);
    });
  });

  root.querySelectorAll(".zuni-replay").forEach(button => {
    button.addEventListener("click", () => {
      const panel = button.closest(".zuni-terminal");
      if (!panel) return;
      panel.classList.remove("zuni-replaying"); void panel.offsetWidth; panel.classList.add("zuni-replaying");
      setTimeout(() => panel.classList.remove("zuni-replaying"), 1200);
    });
  });
  const reveal = [...root.querySelectorAll("[data-reveal]")];
  const reduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  if (reduced || !("IntersectionObserver" in window)) reveal.forEach(el => el.classList.add("is-visible"));
  else {
    const observer = new IntersectionObserver(entries => entries.forEach(entry => {
      if (entry.isIntersecting) { entry.target.classList.add("is-visible"); observer.unobserve(entry.target); }
    }), { threshold: 0.12 });
    reveal.forEach(el => observer.observe(el));
  }
  const flowSteps = [...root.querySelectorAll("[data-flow-step-index]")];
  const flowProgress = root.querySelector(".zuni-flow-progress i");
  const flowCount = root.querySelector("[data-flow-step]");
  const flowArtifact = root.querySelector("[data-flow-artifact]");
  const nodes = [...root.querySelectorAll(".zuni-flow-diagram g")];
  const artifacts = [
    '<div class="zuni-eyebrow">INPUT</div><p><span class="zuni-prompt">$</span> zuni ask "What is quantum computing?"</p>',
    '<div class="zuni-eyebrow">SEARCH → READABLE TEXT</div><p>search result <span>→</span> extracted page text</p>',
    '<div class="zuni-eyebrow">ZUNI CONFIG</div><p>API key <span>••••••••</span><br>model ID <span>&lt;your model&gt;</span><br>base URL <span>&lt;your endpoint&gt;</span></p>',
    '<div class="zuni-eyebrow">OUTPUT · ILLUSTRATIVE</div><p>Answer text with source references <span>[1] [2]</span></p>'
  ];
  const setFlow = index => {
    flowSteps.forEach((step, i) => step.classList.toggle("is-active", i === index));
    nodes.forEach((node, i) => { node.classList.toggle("is-active", i === index); node.classList.toggle("is-done", i < index); });
    if (flowProgress) flowProgress.style.width = ((index + 1) / 4 * 100) + "%";
    if (flowCount) flowCount.textContent = "0" + (index + 1);
    if (flowArtifact) flowArtifact.innerHTML = artifacts[index];
  };
  if ("IntersectionObserver" in window && !reduced) {
    const flowObserver = new IntersectionObserver(entries => entries.forEach(entry => {
      if (entry.isIntersecting) setFlow(Number(entry.target.dataset.flowStepIndex));
    }), { rootMargin: "-35% 0px -35% 0px", threshold: 0 });
    flowSteps.forEach(step => flowObserver.observe(step));
  } else setFlow(0);
  root.querySelector(".zuni-demo-panel .zuni-replay")?.addEventListener("click", () => {
    const panel = root.querySelector(".zuni-demo-panel:not([hidden])");
    if (!panel) return;
    const output = panel.querySelector(".zuni-demo-output:not([hidden])");
    output?.classList.remove("zuni-output-replay"); void output?.offsetWidth; output?.classList.add("zuni-output-replay");
  });
})();
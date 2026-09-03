(() => {
  const root = document.documentElement;
  const sidebar = document.getElementById("sidebar");
  const mobileToggle = document.getElementById("mobile-nav-toggle");
  const progress = document.getElementById("reading-progress-bar");
  const themeToggle = document.getElementById("theme-toggle");
  const search = document.getElementById("global-search");
  const searchEmpty = document.getElementById("search-empty");
  const sections = [...document.querySelectorAll("main > section")];
  const navLinks = [...document.querySelectorAll(".sidebar nav a")];

  const savedTheme = localStorage.getItem("codebase-wiki-theme");
  if (savedTheme === "dark" || savedTheme === "light") {
    root.dataset.theme = savedTheme;
  } else if (window.matchMedia?.("(prefers-color-scheme: dark)").matches) {
    root.dataset.theme = "dark";
  }

  themeToggle?.addEventListener("click", () => {
    root.dataset.theme = root.dataset.theme === "dark" ? "light" : "dark";
    localStorage.setItem("codebase-wiki-theme", root.dataset.theme);
  });

  mobileToggle?.addEventListener("click", () => {
    const open = sidebar?.classList.toggle("open") ?? false;
    mobileToggle.setAttribute("aria-expanded", String(open));
  });
  navLinks.forEach((link) => link.addEventListener("click", () => {
    sidebar?.classList.remove("open");
    mobileToggle?.setAttribute("aria-expanded", "false");
  }));

  const updateProgress = () => {
    const scrollable = document.documentElement.scrollHeight - window.innerHeight;
    const ratio = scrollable > 0 ? window.scrollY / scrollable : 0;
    if (progress) progress.style.width = `${Math.max(0, Math.min(100, ratio * 100))}%`;
  };
  updateProgress();
  window.addEventListener("scroll", updateProgress, { passive: true });

  if ("IntersectionObserver" in window) {
    const observer = new IntersectionObserver((entries) => {
      const visible = entries.filter((entry) => entry.isIntersecting).sort((a, b) => b.intersectionRatio - a.intersectionRatio)[0];
      if (!visible) return;
      navLinks.forEach((link) => link.classList.toggle("active", link.getAttribute("href") === `#${visible.target.id}`));
    }, { rootMargin: "-18% 0px -68% 0px", threshold: [0, 0.1, 0.4] });
    sections.forEach((section) => observer.observe(section));
  }

  const normalize = (value) => value.trim().toLocaleLowerCase();
  search?.addEventListener("input", () => {
    const query = normalize(search.value);
    let matches = 0;
    sections.forEach((section) => {
      const haystack = normalize(`${section.dataset.search ?? ""} ${section.textContent ?? ""}`);
      const hit = query === "" || haystack.includes(query);
      section.classList.toggle("search-hidden", !hit);
      section.classList.toggle("search-hit", query !== "" && hit);
      if (hit) matches += 1;
    });
    if (searchEmpty) searchEmpty.hidden = matches > 0;
  });

  document.querySelectorAll("[role='tab'][data-tab]").forEach((tab) => {
    tab.addEventListener("click", () => {
      const target = tab.dataset.tab;
      document.querySelectorAll("[role='tab'][data-tab]").forEach((item) => item.setAttribute("aria-selected", String(item === tab)));
      document.querySelectorAll("[role='tabpanel']").forEach((panel) => { panel.hidden = panel.id !== target; });
    });
  });

  document.querySelectorAll(".copy-code").forEach((button) => {
    button.addEventListener("click", async () => {
      const code = button.closest(".code-block")?.querySelector("pre code")?.textContent ?? "";
      try {
        await navigator.clipboard.writeText(code);
        const original = button.textContent;
        button.textContent = "已复制";
        window.setTimeout(() => { button.textContent = original; }, 1200);
      } catch {
        button.textContent = "复制失败";
      }
    });
  });

  document.querySelectorAll("[data-progress-key] input[type='checkbox']").forEach((checkbox) => {
    const container = checkbox.closest("[data-progress-key]");
    const key = `codebase-wiki-progress:${container?.dataset.progressKey ?? "unknown"}`;
    checkbox.checked = localStorage.getItem(key) === "1";
    checkbox.addEventListener("change", () => localStorage.setItem(key, checkbox.checked ? "1" : "0"));
  });
})();

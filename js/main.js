document.addEventListener("DOMContentLoaded", () => {
  /* ==========================================================
     1. THEME SWITCHER (Sand Light / Obsidian Dark)
     ========================================================== */
  const themeToggleBtn = document.getElementById("theme-toggle");
  const themeIcon = document.getElementById("theme-icon");

  function getPreferredTheme() {
    const saved = localStorage.getItem("portfolio_theme_cleon");
    if (saved) return saved;
    return window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light";
  }

  function applyTheme(theme) {
    document.documentElement.setAttribute("data-theme", theme);
    localStorage.setItem("portfolio_theme_cleon", theme);
    if (themeIcon) {
      themeIcon.textContent = theme === "dark" ? "☼" : "☾";
    }
  }

  applyTheme(getPreferredTheme());

  if (themeToggleBtn) {
    themeToggleBtn.addEventListener("click", () => {
      const current = document.documentElement.getAttribute("data-theme") || "light";
      applyTheme(current === "dark" ? "light" : "dark");
    });
  }

  /* ==========================================================
     2. REAL-TIME SUWON, SOUTH KOREA CLOCK (KST / UTC+9)
     ========================================================== */
  const clockEl = document.getElementById("kst-clock");

  function updateSuwonClock() {
    if (!clockEl) return;
    try {
      const options = {
        timeZone: "Asia/Seoul",
        hour12: false,
        hour: "2-digit",
        minute: "2-digit",
        second: "2-digit"
      };
      const formatter = new Intl.DateTimeFormat("en-US", options);
      const timeStr = formatter.format(new Date());
      clockEl.textContent = `${timeStr} KST`;
    } catch (e) {
      const now = new Date();
      clockEl.textContent = `${String(now.getHours()).padStart(2, '0')}:${String(now.getMinutes()).padStart(2, '0')} KST`;
    }
  }

  updateSuwonClock();
  setInterval(updateSuwonClock, 1000);

  /* ==========================================================
     3. INTERACTIVE TAB NAVIGATION (Cleon Wong System)
     ========================================================== */
  const tabButtons = document.querySelectorAll(".tab-btn");
  const tabPanes = document.querySelectorAll(".tab-pane");

  function switchTab(tabName) {
    let targetPane = document.getElementById(`pane-${tabName}`);
    if (!targetPane) {
      tabName = "work";
      targetPane = document.getElementById("pane-work");
    }

    tabButtons.forEach((btn) => {
      const isTarget = btn.getAttribute("data-tab") === tabName;
      btn.setAttribute("aria-pressed", isTarget ? "true" : "false");
    });

    tabPanes.forEach((pane) => {
      pane.classList.remove("active");
    });

    if (targetPane) {
      targetPane.classList.add("active");
    }

    if (history.replaceState) {
      history.replaceState(null, "", `#${tabName}`);
    }
  }

  tabButtons.forEach((btn) => {
    btn.addEventListener("click", () => {
      const tabName = btn.getAttribute("data-tab");
      if (tabName) switchTab(tabName);
    });
  });

  // Check URL hash on load
  const hash = window.location.hash.replace("#", "").toLowerCase();
  if (hash && document.getElementById(`pane-${hash}`)) {
    switchTab(hash);
  }

  /* ==========================================================
     4. 1-CLICK EMAIL COPY & TOAST NOTIFICATION
     ========================================================== */
  const copyEmailBtns = document.querySelectorAll(".js-copy-email");
  const toast = document.getElementById("toast");
  let toastTimer = null;

  function showToast(message) {
    if (!toast) return;
    toast.textContent = message;
    toast.classList.add("show");
    clearTimeout(toastTimer);
    toastTimer = setTimeout(() => {
      toast.classList.remove("show");
    }, 3000);
  }

  copyEmailBtns.forEach((btn) => {
    btn.addEventListener("click", (e) => {
      e.preventDefault();
      const email = btn.getAttribute("data-email") || "455ahsankhan@gmail.com";
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(email).then(() => {
          showToast(`Copied ${email} to clipboard`);
        }).catch(() => {
          fallbackCopyText(email);
        });
      } else {
        fallbackCopyText(email);
      }
    });
  });

  function fallbackCopyText(text) {
    const textArea = document.createElement("textarea");
    textArea.value = text;
    textArea.style.position = "fixed";
    textArea.style.opacity = "0";
    document.body.appendChild(textArea);
    textArea.focus();
    textArea.select();
    try {
      document.execCommand("copy");
      showToast(`Copied ${text} to clipboard`);
    } catch (err) {
      prompt("Copy email:", text);
    }
    document.body.removeChild(textArea);
  }
});

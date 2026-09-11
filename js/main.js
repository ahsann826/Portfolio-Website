document.addEventListener("DOMContentLoaded", () => {
  /* ==========================================================
     1. THEME SWITCHER (Warm Paper / Onyx Dark)
     ========================================================== */
  const themeToggleBtn = document.getElementById("theme-toggle");
  const themeIcon = themeToggleBtn ? themeToggleBtn.querySelector(".theme-icon") : null;
  const themeLabel = themeToggleBtn ? themeToggleBtn.querySelector(".theme-label") : null;

  function getPreferredTheme() {
    const saved = localStorage.getItem("portfolio_theme");
    if (saved) return saved;
    return window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light";
  }

  function applyTheme(theme) {
    document.documentElement.setAttribute("data-theme", theme);
    localStorage.setItem("portfolio_theme", theme);
    if (themeIcon && themeLabel) {
      if (theme === "dark") {
        themeIcon.textContent = "☼";
        themeLabel.textContent = "Light";
      } else {
        themeIcon.textContent = "☾";
        themeLabel.textContent = "Dark";
      }
    }
  }

  // Initialize theme
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
     3. PRELOADER & GSAP ENTRANCE ANIMATIONS
     ========================================================== */
  const preloader = document.querySelector(".preloader");

  function runEntranceAnimations() {
    if (typeof gsap !== "undefined") {
      gsap.registerPlugin(ScrollTrigger);

      // Initial state
      gsap.set(".js-fade-page", { opacity: 0, y: 14 });
      gsap.set(".js-fade-section", { opacity: 0, y: 18 });

      // Fade in hero elements
      gsap.to(".js-fade-page", {
        opacity: 1,
        y: 0,
        duration: 1.4,
        ease: "power2.out",
        stagger: 0.1
      });

      // ScrollTrigger for sections
      gsap.utils.toArray(".js-fade-section").forEach((section) => {
        gsap.to(section, {
          opacity: 1,
          y: 0,
          duration: 1.3,
          ease: "power2.out",
          scrollTrigger: {
            trigger: section,
            start: "top 88%",
            once: true
          }
        });
      });

      ScrollTrigger.refresh();
    } else {
      // Fallback
      document.querySelectorAll(".js-fade-page, .js-fade-section").forEach((el) => {
        el.style.opacity = "1";
        el.style.transform = "none";
      });
    }
  }

  window.addEventListener("load", () => {
    if (preloader) {
      setTimeout(() => {
        preloader.classList.add("hide");
        setTimeout(runEntranceAnimations, 300);
      }, 400);
    } else {
      runEntranceAnimations();
    }
  });

  // Fallback in case load event already fired or is delayed
  setTimeout(() => {
    if (preloader && !preloader.classList.contains("hide")) {
      preloader.classList.add("hide");
      runEntranceAnimations();
    }
  }, 1600);

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
    }, 3200);
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

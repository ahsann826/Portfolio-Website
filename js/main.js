// Main JavaScript for interactive tabs, tactile buttons, and back-to-top behavior
document.addEventListener('DOMContentLoaded', () => {
  // 1. Tab Switching
  const tabButtons = document.querySelectorAll('.tab-btn, .center-fab-btn');
  const tabPanels = document.querySelectorAll('.tab-panel');

  function setActiveTab(targetTab) {
    tabButtons.forEach(btn => {
      const isMatch = btn.getAttribute('data-tab') === targetTab;
      btn.setAttribute('aria-pressed', isMatch ? 'true' : 'false');
    });

    tabPanels.forEach(panel => {
      if (panel.getAttribute('id') === `tab-panel-${targetTab}`) {
        panel.classList.remove('hidden');
        panel.style.opacity = '1';
      } else {
        panel.classList.add('hidden');
        panel.style.opacity = '0';
      }
    });

    // If switched from another section, smoothly align to tabs if scrolled deep
    const tabsNav = document.getElementById('tabs-container');
    if (tabsNav && window.scrollY > tabsNav.offsetTop + 100) {
      window.scrollTo({
        top: tabsNav.offsetTop - 100,
        behavior: 'smooth'
      });
    }
  }

  tabButtons.forEach(btn => {
    btn.addEventListener('click', () => {
      const tabId = btn.getAttribute('data-tab');
      if (tabId) {
        setActiveTab(tabId);
        history.replaceState(null, '', `#${tabId}`);
      }
    });
  });

  // Handle URL hash on load
  if (window.location.hash) {
    const initialTab = window.location.hash.replace('#', '');
    const validBtn = document.querySelector(`.tab-btn[data-tab="${initialTab}"]`);
    if (validBtn) {
      setActiveTab(initialTab);
    }
  }

  // 2. Back to top button
  const backToTopBtn = document.getElementById('back-to-top');
  if (backToTopBtn) {
    window.addEventListener('scroll', () => {
      if (window.scrollY > 350) {
        backToTopBtn.classList.remove('opacity-0', 'pointer-events-none');
        backToTopBtn.classList.add('opacity-100');
      } else {
        backToTopBtn.classList.add('opacity-0', 'pointer-events-none');
        backToTopBtn.classList.remove('opacity-100');
      }
    }, { passive: true });

    backToTopBtn.addEventListener('click', () => {
      window.scrollTo({
        top: 0,
        behavior: 'smooth'
      });
    });
  }

  // 3. Tactile Skeuomorphic Button Press Handler (Play tab buttons)
  const tactileButtons = document.querySelectorAll('.tactile-btn');
  tactileButtons.forEach(btn => {
    const press = () => {
      btn.dataset.pressed = 'true';
    };
    const release = () => {
      btn.dataset.pressed = 'false';
    };
    btn.addEventListener('pointerdown', press);
    btn.addEventListener('pointerup', release);
    btn.addEventListener('pointerleave', release);
    btn.addEventListener('pointercancel', release);
  });
});

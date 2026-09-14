// Modern main.js: Capsule navigation with smooth scrolling, scrollspy, copy email, back-to-top
document.addEventListener('DOMContentLoaded', () => {
  const navLinks = document.querySelectorAll('.capsule-link, .nav-link');
  const sections = document.querySelectorAll('section[id]');
  const header = document.querySelector('header');

  // Calculate sticky offset
  function getStickyOffset() {
    let offset = 0;
    if (header) offset += header.offsetHeight;
    return offset + 56;
  }

  // 1. Smooth Scroll with Sticky Offset
  navLinks.forEach(link => {
    link.addEventListener('click', (e) => {
      const href = link.getAttribute('href');
      if (href && href.startsWith('#')) {
        const targetSection = document.querySelector(href);
        if (targetSection) {
          e.preventDefault();
          const targetPosition = targetSection.getBoundingClientRect().top + window.pageYOffset - getStickyOffset();
          window.scrollTo({
            top: Math.max(0, targetPosition),
            behavior: 'smooth'
          });
          history.replaceState(null, '', href);
          updateActiveLink(href);
        }
      }
    });
  });

  function updateActiveLink(targetId) {
    navLinks.forEach(link => {
      if (link.getAttribute('href') === targetId) {
        link.classList.add('active');
      } else {
        link.classList.remove('active');
      }
    });
  }

  // 2. ScrollSpy: Highlight current section in capsule navigation on scroll
  function onScroll() {
    const scrollPos = window.pageYOffset + getStickyOffset() + 60;
    let currentId = '#summary';

    sections.forEach(section => {
      const top = section.offsetTop;
      const height = section.offsetHeight;
      if (scrollPos >= top && scrollPos < top + height) {
        currentId = '#' + section.getAttribute('id');
      }
    });

    // If at the bottom of the page, activate #contact
    if (window.innerHeight + window.pageYOffset >= document.body.offsetHeight - 60) {
      currentId = '#contact';
    }

    updateActiveLink(currentId);
  }

  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll(); // initial check

  // 3. Back to Top Button
  const backToTopBtn = document.getElementById('back-to-top');
  if (backToTopBtn) {
    window.addEventListener('scroll', () => {
      if (window.pageYOffset > 400) {
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

  // 4. One-Click Copy Email Button
  const copyBtn = document.getElementById('copy-email-btn');
  const copyCheck = document.getElementById('copy-check');
  if (copyBtn) {
    copyBtn.addEventListener('click', async () => {
      const email = copyBtn.getAttribute('data-email') || '455ahsankhan@gmail.com';
      try {
        await navigator.clipboard.writeText(email);
        if (copyCheck) {
          copyCheck.classList.remove('hidden');
          setTimeout(() => {
            copyCheck.classList.add('hidden');
          }, 2500);
        }
      } catch (err) {
        console.error('Failed to copy email: ', err);
      }
    });
  }
});

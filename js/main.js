/* ============================================
   DHOLERA SIR — Scroll Animations & Interactions
   ============================================ */

document.addEventListener('DOMContentLoaded', () => {

  // ── Set Active Nav Link (URL based) ──
  const currentPath = window.location.pathname.split('/').pop() || 'index.html';
  const navAnchorLinks = document.querySelectorAll('.nav-links a');
  navAnchorLinks.forEach(link => {
    link.classList.remove('active');
    const href = link.getAttribute('href');
    if (href === currentPath || (currentPath === '' && href === 'index.html')) {
      link.classList.add('active');
    }
  });

  // ── Navbar scroll effect ──
  const navbar = document.querySelector('.navbar');
  const handleNavScroll = () => {
    if (window.scrollY > 60) {
      navbar.classList.add('scrolled');
    } else {
      navbar.classList.remove('scrolled');
    }
  };
  window.addEventListener('scroll', handleNavScroll);
  handleNavScroll();

  // ── Mobile menu toggle ──
  const hamburger = document.querySelector('.hamburger');
  const navLinksContainer = document.querySelector('.nav-links');
  
  if (hamburger) {
    hamburger.addEventListener('click', () => {
      navLinksContainer.classList.toggle('active');
      hamburger.classList.toggle('active');
    });
    
    // Close menu on link click
    navLinksContainer.querySelectorAll('a').forEach(link => {
      link.addEventListener('click', () => {
        navLinksContainer.classList.remove('active');
        hamburger.classList.remove('active');
      });
    });
  }

  // ── Scroll Reveal Animation ──
  const revealElements = document.querySelectorAll('.reveal, .reveal-left, .reveal-right');
  
  const revealObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        // Don't unobserve — keeps the animation one-time
        revealObserver.unobserve(entry.target);
      }
    });
  }, {
    threshold: 0.15,
    rootMargin: '0px 0px -60px 0px'
  });

  revealElements.forEach(el => revealObserver.observe(el));

  // ── Staggered Children Animation ──
  const staggerContainers = document.querySelectorAll('.stagger');
  
  const staggerObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const children = entry.target.children;
        Array.from(children).forEach((child, index) => {
          setTimeout(() => {
            child.classList.add('visible');
          }, index * 120);
        });
        staggerObserver.unobserve(entry.target);
      }
    });
  }, {
    threshold: 0.1,
    rootMargin: '0px 0px -40px 0px'
  });

  staggerContainers.forEach(el => staggerObserver.observe(el));

  // ── Back to Top Button ──
  const backToTop = document.querySelector('.back-to-top');
  if (backToTop) {
    window.addEventListener('scroll', () => {
      if (window.scrollY > 500) {
        backToTop.classList.add('visible');
      } else {
        backToTop.classList.remove('visible');
      }
    });

    backToTop.addEventListener('click', () => {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  }

  // ── Smooth scroll for anchor links ──
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
      const targetId = this.getAttribute('href');
      if (targetId === '#') return;
      const target = document.querySelector(targetId);
      if (target) {
        e.preventDefault();
        const navHeight = navbar.offsetHeight;
        const targetPosition = target.getBoundingClientRect().top + window.scrollY - navHeight;
        window.scrollTo({ top: targetPosition, behavior: 'smooth' });
      }
    });
  });

  // ── Counter Animation (for stats if needed) ──
  function animateCounter(element, target, duration = 2000) {
    let start = 0;
    const increment = target / (duration / 16);
    
    function update() {
      start += increment;
      if (start >= target) {
        element.textContent = target.toLocaleString();
        return;
      }
      element.textContent = Math.floor(start).toLocaleString();
      requestAnimationFrame(update);
    }
    
    update();
  }

  // ── Active nav link highlight (Scroll Spy for anchor links) ──
  const sections = document.querySelectorAll('section[id]');
  const navLinksList = document.querySelector('.nav-links');
  
  if (sections.length > 0 && navLinksList) {
    window.addEventListener('scroll', () => {
      let current = '';
      sections.forEach(section => {
        const sectionTop = section.offsetTop - 120;
        if (window.scrollY >= sectionTop) {
          current = section.getAttribute('id');
        }
      });

      if (current) {
        navLinksList.querySelectorAll('a').forEach(link => {
          link.classList.remove('active');
          if (link.getAttribute('href') === `#${current}`) {
            link.classList.add('active');
          }
        });
      }
    });
  }

  // ── Parallax effect on hero ──
  const heroBg = document.querySelector('.hero-bg img, .page-hero-bg img');
  if (heroBg) {
    window.addEventListener('scroll', () => {
      const scrolled = window.scrollY;
      if (scrolled < window.innerHeight) {
        heroBg.style.transform = `translateY(${scrolled * 0.3}px) scale(1.1)`;
      }
    });
  }

  // ── Pipeline Animation (Why Choose Us) ──
  const pipeline = document.querySelector('.process-pipeline');
  if (pipeline) {
    const pipelineObserver = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          setTimeout(() => {
            entry.target.classList.add('visible');
          }, 300); // slight delay after elements appear
          pipelineObserver.unobserve(entry.target);
        }
      });
    }, {
      threshold: 0.5
    });
    
    pipelineObserver.observe(pipeline);
  }

  // ── Accordion Logic (Residential Page) ──
  const accordionHeaders = document.querySelectorAll('.accordion-header');
  
  accordionHeaders.forEach(header => {
    header.addEventListener('click', function() {
      const item = this.parentElement;
      const content = item.querySelector('.accordion-content');
      
      // Close other active items (optional, for accordion style)
      document.querySelectorAll('.accordion-item').forEach(otherItem => {
        if (otherItem !== item && otherItem.classList.contains('active')) {
          otherItem.classList.remove('active');
          otherItem.querySelector('.accordion-content').style.maxHeight = null;
        }
      });

      // Toggle current item
      if (item.classList.contains('active')) {
        item.classList.remove('active');
        content.style.maxHeight = null;
      } else {
        item.classList.add('active');
        content.style.maxHeight = content.scrollHeight + "px";
      }
    });
  });

});

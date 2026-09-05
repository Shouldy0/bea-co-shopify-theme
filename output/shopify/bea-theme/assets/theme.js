/**
 * Bea & Co. - Theme JS Engine
 * Handles Ajax Cart Drawer, Sticky Buy Bar, Accordions, and Navigation
 */
document.addEventListener('DOMContentLoaded', () => {
  // Mobile Nav Drawer Toggle
  const mobileToggle = document.querySelector('[data-mobile-menu-toggle]');
  const mobileDrawer = document.querySelector('[data-mobile-drawer]');
  const mobileClose = document.querySelector('[data-mobile-close]');

  if (mobileToggle && mobileDrawer) {
    mobileToggle.addEventListener('click', () => {
      mobileDrawer.classList.add('is-active');
      document.body.style.overflow = 'hidden';
    });
    
    if (mobileClose) {
      mobileClose.addEventListener('click', () => {
        mobileDrawer.classList.remove('is-active');
        document.body.style.overflow = '';
      });
    }

    mobileDrawer.addEventListener('click', (e) => {
      if (e.target === mobileDrawer) {
        mobileDrawer.classList.remove('is-active');
        document.body.style.overflow = '';
      }
    });
  }

  // Ajax Cart Drawer
  const cartToggles = document.querySelectorAll('[data-cart-toggle]');
  const cartDrawerOverlay = document.querySelector('[data-cart-drawer-overlay]');
  const cartDrawerClose = document.querySelector('[data-cart-drawer-close]');

  function openCartDrawer() {
    if (cartDrawerOverlay) {
      cartDrawerOverlay.classList.add('is-open');
      document.body.style.overflow = 'hidden';
    }
  }

  function closeCartDrawer() {
    if (cartDrawerOverlay) {
      cartDrawerOverlay.classList.remove('is-open');
      document.body.style.overflow = '';
    }
  }

  cartToggles.forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      openCartDrawer();
    });
  });

  if (cartDrawerClose) {
    cartDrawerClose.addEventListener('click', closeCartDrawer);
  }

  if (cartDrawerOverlay) {
    cartDrawerOverlay.addEventListener('click', (e) => {
      if (e.target === cartDrawerOverlay) closeCartDrawer();
    });
  }

  // Quantity Stepper
  document.querySelectorAll('[data-quantity-stepper]').forEach(stepper => {
    const input = stepper.querySelector('input');
    const minus = stepper.querySelector('[data-quantity-minus]');
    const plus = stepper.querySelector('[data-quantity-plus]');

    if (input && minus && plus) {
      minus.addEventListener('click', () => {
        let val = parseInt(input.value, 10) || 1;
        if (val > 1) {
          input.value = val - 1;
          input.dispatchEvent(new Event('change'));
        }
      });
      plus.addEventListener('click', () => {
        let val = parseInt(input.value, 10) || 1;
        input.value = val + 1;
        input.dispatchEvent(new Event('change'));
      });
    }
  });

  // Sticky Add to Cart Observer
  const stickyBar = document.querySelector('[data-sticky-atc-bar]');
  const primaryBuyBtn = document.querySelector('[data-primary-buy-button]');

  if (stickyBar && primaryBuyBtn) {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (!entry.isIntersecting) {
          stickyBar.classList.add('is-visible');
        } else {
          stickyBar.classList.remove('is-visible');
        }
      });
    }, { threshold: 0.1 });

    observer.observe(primaryBuyBtn);
  }

  // Ajax Add to Cart Handler (Works with Shopify API or local preview)
  document.querySelectorAll('form[action*="/cart/add"]').forEach(form => {
    form.addEventListener('submit', async (e) => {
      // If we are in live shopify with fetch available
      if (window.Shopify) {
        e.preventDefault();
        const submitBtn = form.querySelector('button[type="submit"]');
        const originalText = submitBtn.innerHTML;
        submitBtn.disabled = true;
        submitBtn.innerHTML = '<span>Adding...</span>';

        try {
          const res = await fetch('/cart/add.js', {
            method: 'POST',
            body: new FormData(form),
            headers: { 'Accept': 'application/json' }
          });
          if (res.ok) {
            submitBtn.innerHTML = '<span>Added ✓</span>';
            setTimeout(() => {
              submitBtn.disabled = false;
              submitBtn.innerHTML = originalText;
            }, 1200);
            // Refresh cart state & open drawer
            openCartDrawer();
          } else {
            form.submit();
          }
        } catch (err) {
          form.submit();
        }
      }
    });
  });
});

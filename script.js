// Meridian Textiles — landing page interactions

(function () {
  "use strict";

  // Mobile nav toggle
  const toggle = document.querySelector(".nav-toggle");
  const menu = document.getElementById("nav-menu");

  if (toggle && menu) {
    toggle.addEventListener("click", function () {
      const open = menu.classList.toggle("open");
      toggle.setAttribute("aria-expanded", String(open));
    });

    // Close menu after clicking a link (mobile)
    menu.querySelectorAll("a").forEach(function (link) {
      link.addEventListener("click", function () {
        menu.classList.remove("open");
        toggle.setAttribute("aria-expanded", "false");
      });
    });
  }

  // Current year in footer
  const yearEl = document.getElementById("year");
  if (yearEl) yearEl.textContent = new Date().getFullYear();

  // Quote form: client-side validation + simulated submit
  const form = document.getElementById("quote-form");
  const status = document.getElementById("form-status");

  if (form && status) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      status.className = "form-status";

      const name = form.name.value.trim();
      const email = form.email.value.trim();
      const emailOk = /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);

      if (!name || !emailOk) {
        status.textContent = "Please enter your name and a valid email address.";
        status.classList.add("error");
        return;
      }

      const btn = form.querySelector("button[type=submit]");
      if (btn) {
        btn.disabled = true;
        btn.textContent = "Sending…";
      }

      // Simulated async submit (replace with real endpoint/integration)
      setTimeout(function () {
        form.reset();
        status.textContent = "Thanks! We'll be in touch within one business day.";
        status.classList.add("success");
        if (btn) {
          btn.disabled = false;
          btn.textContent = "Send Request";
        }
      }, 800);
    });
  }
})();

document.addEventListener("DOMContentLoaded", () => {
  const menuBtn = document.getElementById("menu-btn");
  const mobileMenu = document.getElementById("mobile-menu");
  const panel = document.getElementById("mobile-panel");
  const closeBtn = document.getElementById("menu-close");
  const backdrop = document.getElementById("mobile-backdrop");

  function openMenu() {
    mobileMenu.classList.remove("opacity-0", "pointer-events-none");
    mobileMenu.classList.add("opacity-100", "pointer-events-auto");

    panel.classList.remove("translate-y-[-20px]", "opacity-0");
    panel.classList.add("translate-y-0", "opacity-100");

    menuBtn.textContent = "✕";
    menuBtn.setAttribute("aria-expanded", "true");
    document.documentElement.classList.add("overflow-hidden");
  }

  function closeMenu() {
    panel.classList.add("translate-y-[-20px]", "opacity-0");
    panel.classList.remove("translate-y-0", "opacity-100");

    mobileMenu.classList.add("opacity-0");
    mobileMenu.classList.remove("opacity-100");

    setTimeout(() => {
      mobileMenu.classList.add("pointer-events-none");
      mobileMenu.classList.remove("pointer-events-auto");
    }, 500);

    menuBtn.textContent = "☰";
    menuBtn.setAttribute("aria-expanded", "false");
    document.documentElement.classList.remove("overflow-hidden");
  }

  menuBtn.addEventListener("click", () => {
    const expanded = menuBtn.getAttribute("aria-expanded") === "true";
    expanded ? closeMenu() : openMenu();
  });

  closeBtn.addEventListener("click", closeMenu);
  backdrop.addEventListener("click", closeMenu);
});
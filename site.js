"use strict";

// Progressive enhancement: section copy and discoveries remain readable without JS.
const menuButton = document.querySelector(".menu-toggle");
const navigation = document.querySelector("#navigation");
const mobile = window.matchMedia("(max-width: 700px)");

function closeMenu() {
  menuButton.setAttribute("aria-expanded", "false");
  navigation.setAttribute("aria-hidden", String(mobile.matches));
  if (mobile.matches) {
    navigation.inert = true;
    navigation.classList.remove("is-open");
  } else {
    navigation.inert = false;
    navigation.hidden = false;
    navigation.classList.remove("is-open");
  }
}

function syncMenu() {
  menuButton.hidden = !mobile.matches;
  navigation.hidden = false;
  closeMenu();
}

syncMenu();
mobile.addEventListener("change", syncMenu);
menuButton.addEventListener("click", () => {
  const open = menuButton.getAttribute("aria-expanded") !== "true";
  menuButton.setAttribute("aria-expanded", String(open));
  if (open) {
    navigation.hidden = false;
    navigation.inert = false;
    navigation.setAttribute("aria-hidden", "false");
    requestAnimationFrame(() => navigation.classList.add("is-open"));
  } else {
    navigation.inert = true;
    navigation.setAttribute("aria-hidden", "true");
    navigation.classList.remove("is-open");
  }
});
navigation.querySelectorAll("a").forEach(link => link.addEventListener("click", closeMenu));
navigation.addEventListener("transitionend", event => {
  if (event.target === navigation && event.propertyName === "max-height" && mobile.matches && menuButton.getAttribute("aria-expanded") !== "true") {
    navigation.hidden = true;
  }
});
document.addEventListener("keydown", event => {
  if (event.key === "Escape" && mobile.matches && menuButton.getAttribute("aria-expanded") === "true") {
    closeMenu();
    menuButton.focus();
  }
});

const storeDialog = document.querySelector("#store-dialog");
document.querySelectorAll("[data-store]").forEach(button => {
  button.addEventListener("click", () => storeDialog.showModal());
});
storeDialog.addEventListener("click", event => {
  if (event.target !== storeDialog) return;
  const bounds = storeDialog.getBoundingClientRect();
  if (event.clientX < bounds.left || event.clientX > bounds.right || event.clientY < bounds.top || event.clientY > bounds.bottom) storeDialog.close();
});

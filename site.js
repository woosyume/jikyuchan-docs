"use strict";

// Progressive enhancement: section copy and discoveries remain readable without JS.
const menuButton = document.querySelector(".menu-toggle");
const navigation = document.querySelector("#navigation");
const mobile = window.matchMedia("(max-width: 700px)");

function closeMenu() {
  menuButton.setAttribute("aria-expanded", "false");
  navigation.hidden = mobile.matches;
}

function syncMenu() {
  menuButton.hidden = !mobile.matches;
  closeMenu();
}

syncMenu();
mobile.addEventListener("change", syncMenu);
menuButton.addEventListener("click", () => {
  const open = menuButton.getAttribute("aria-expanded") !== "true";
  menuButton.setAttribute("aria-expanded", String(open));
  navigation.hidden = !open;
});
navigation.querySelectorAll("a").forEach(link => link.addEventListener("click", closeMenu));
document.addEventListener("keydown", event => {
  if (event.key === "Escape" && mobile.matches && !navigation.hidden) {
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

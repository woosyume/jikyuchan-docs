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

const discoveryButton = document.querySelector("#discovery-button");
const discoveryResult = document.querySelector("#discovery-result");
const discoveryIndicator = document.querySelector("#discovery-indicator");
const discoveryCharacter = document.querySelector("#discovery-character");
discoveryButton.hidden = false;
discoveryResult.hidden = true;
discoveryButton.addEventListener("click", () => {
  const open = discoveryButton.getAttribute("aria-expanded") !== "true";
  discoveryButton.setAttribute("aria-expanded", String(open));
  discoveryResult.hidden = !open;
  discoveryButton.textContent = open ? "発見をとじる" : "見つけたことを見る ✧";
  discoveryIndicator.textContent = open ? "新しいことを見つけたよ！ ✧" : "なにか見つけたみたい… ✧";
  discoveryCharacter.src = open ? "assets/images/jikyuchan-happy.webp" : "assets/images/jikyuchan-thinking.webp";
  discoveryCharacter.alt = open ? "新しい発見をよろこぶじきゅうちゃん" : "なにか見つけたみたいなじきゅうちゃん";
  if (open) discoveryResult.classList.add("reveal-animation");
  else discoveryResult.classList.remove("reveal-animation");
});

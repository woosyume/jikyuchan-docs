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

// Fetch animation only on request; the four lazy stills also work without JS.
const stickerMotion = window.matchMedia("(prefers-reduced-motion: reduce)");
const stickerNote = document.querySelector("#sticker-preview-note");
const stickerPlayers = [...document.querySelectorAll(".sticker-play")].map(button => {
  const image = button.closest("figure").querySelector("img");
  const still = image.getAttribute("src");
  const label = button.getAttribute("aria-label");
  let timer;

  function stop() {
    clearTimeout(timer);
    image.onload = null;
    image.onerror = null;
    if (image.getAttribute("src") !== still) image.src = still;
    button.setAttribute("aria-pressed", "false");
    button.setAttribute("aria-label", label);
    button.innerHTML = '動きを見る <span aria-hidden="true">▷</span>';
  }

  button.addEventListener("click", () => {
    if (stickerMotion.matches || button.getAttribute("aria-pressed") === "true") {
      stop();
      return;
    }
    button.setAttribute("aria-pressed", "true");
    button.setAttribute("aria-label", label.replace("動きを見る", "動きを止める"));
    button.innerHTML = '動きを止める <span aria-hidden="true">Ⅱ</span>';
    image.onload = () => { timer = setTimeout(stop, Number(button.dataset.duration)); };
    image.onerror = () => {
      stop();
      stickerNote.textContent = "動きを読み込めませんでした。静止画でご覧いただけます。";
    };
    image.src = button.dataset.animation;
  });

  return { button, stop };
});

function syncStickerMotion() {
  stickerPlayers.forEach(({ button, stop }) => {
    stop();
    button.hidden = stickerMotion.matches;
  });
  stickerNote.textContent = stickerMotion.matches
    ? "動きを抑える設定に合わせて、静止画で表示しています。"
    : "「動きを見る」でアニメーションを再生できます。";
}

syncStickerMotion();
stickerMotion.addEventListener("change", syncStickerMotion);

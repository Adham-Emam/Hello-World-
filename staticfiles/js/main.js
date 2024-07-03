const navIcon = document.querySelector(".nav-icon");
const navMenu = document.querySelector("header");

navIcon.addEventListener("click", () => {
  navIcon.classList.toggle("active");
  navMenu.classList.toggle("active");
});

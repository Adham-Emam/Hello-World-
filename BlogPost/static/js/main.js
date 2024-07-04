const navIcon = document.querySelector(".nav-icon");
const header = document.querySelector("header");

navIcon.addEventListener("click", () => {
  navIcon.classList.toggle("active");
  header.classList.toggle("active");
});

window.addEventListener("scroll", () => {
  navIcon.classList.remove("active");
  header.classList.remove("active");
});

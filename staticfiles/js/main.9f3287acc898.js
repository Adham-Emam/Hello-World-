const navIcon = document.querySelector(".nav-icon");
const header = document.querySelector("header");

navIcon.addEventListener("click", () => {
  navIcon.classList.toggle("active");
  header.classList.toggle("active");
});
document.querySelector("body").addEventListener("scroll", () => {
  if (navIcon) {
    navIcon.classList.remove("active");
  }

  if (header) {
    header.classList.remove("active");
  }
});

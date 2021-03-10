const email = document.querySelector(".email");
const btn = document.querySelector(".cp-btn");

const togglePopup = () => {
  const popup = document.querySelector(".popup");

  popup.classList.contains("hidden")
    ? popup.classList.remove("hidden")
    : popup.classList.add("hidden");
};

const copyEmail = () => {
  const text = document.querySelector(".popup p").textContent;

  if (!navigator.clipboard) {
    console.log("Use execComand()");
  } else {
    navigator.clipboard.writeText(text).then(() => {
      btn.textContent = "Copiado!";
      setTimeout(() => (btn.textContent = "Copiar"), 5000);
    });
  }
};

email.addEventListener("click", togglePopup, false);
btn.addEventListener("click", copyEmail, false);

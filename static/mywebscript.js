document.addEventListener("DOMContentLoaded", function () {
  const form = document.querySelector("form");
  const textarea = document.getElementById("textToAnalyze");
  const spinner = document.createElement("div");
  spinner.className = "spinner-border text-primary mt-3";
  spinner.style.display = "none";
  spinner.setAttribute("role", "status");

  const spinnerContainer = document.createElement("div");
  spinnerContainer.className = "d-flex justify-content-center";
  spinnerContainer.appendChild(spinner);
  form.parentNode.insertBefore(spinnerContainer, form.nextSibling);

  form.addEventListener("submit", function (e) {
    const text = textarea.value.trim();

    if (!text) {
      e.preventDefault();
      alert("Please enter text before analyzing.");
      return;
    }

    spinner.style.display = "inline-block";
  });

  // Reveal result card with fade-in effect
  const resultCard = document.querySelector(".card");
  if (resultCard) {
    resultCard.style.opacity = 0;
    resultCard.style.transition = "opacity 1s ease-in-out";

    setTimeout(() => {
      resultCard.style.opacity = 1;
    }, 300);
  }
});

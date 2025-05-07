document.addEventListener("DOMContentLoaded", function () {
  document.getElementById("signupForm").addEventListener("submit", function (e) {
    e.preventDefault();

    let valid = true;

    document.getElementById("nameError").textContent = "";
    document.getElementById("emailError").textContent = "";
    document.getElementById("passwordError").textContent = "";

    const name = document.getElementById("name").value.trim();
    const email = document.getElementById("email").value.trim();
    const password = document.getElementById("password").value.trim();

    if (name === "") {
      document.getElementById("nameError").textContent = "please Enter your full name";
      valid = false;
    }

    if (email === "") {
      document.getElementById("emailError").textContent = "please Enter your Email";
      valid = false;
    } else if (!email.includes("@") || !email.includes(".")) {
      document.getElementById("emailError").textContent = "Email is Wrong";
      valid = false;
    }

    if (password.length < 8) {
      document.getElementById("passwordError").textContent = "password must be at least 8 letters";
      valid = false;
    }

    if (valid) {
      window.location.href = "Nouran.html";
    }
  });
});

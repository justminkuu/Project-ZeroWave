document.addEventListener("DOMContentLoaded", () => {
    const loaderScreen = document.getElementById("loader-screen");
    const loginScreen = document.getElementById("login-screen");
  
    
    setTimeout(() => {
      loaderScreen.style.display = "none"; 
      loginScreen.style.display = "flex"; 
    }, 3000); 
  });

  document.getElementById("enter").addEventListener("click", () => {
    window.location.href = "desktop.html"; 
  });
  
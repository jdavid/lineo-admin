function clearContent(id) {
  document.getElementById(id).replaceChildren();
}

// Function to set theme based on system preference
function applyAutoTheme() {
  const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
  document.documentElement.setAttribute('data-bs-theme', prefersDark ? 'dark' : 'light');
}

// Initialize theme on load
applyAutoTheme();

// Watch for system theme changes
window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', applyAutoTheme);

// Optional: Persist user override
const storedTheme = localStorage.getItem('bsTheme');
if (storedTheme) {
  document.documentElement.setAttribute('data-bs-theme', storedTheme);
}

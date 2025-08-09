function clearContent(id) {
  document.getElementById(id).replaceChildren();
}

/*
 * Submit django-formset forms on enter
 */

document.addEventListener('DOMContentLoaded', function() {
  document.querySelectorAll('django-formset').forEach(formset => {
    formset.addEventListener('keypress', function(event) {
      if (event.key === 'Enter' && !event.shiftKey) {
        event.preventDefault();
        // Find the submit button and click it
        const submitButton = formset.querySelector('button[type="submit"], input[type="submit"]');
        if (submitButton) {
          submitButton.click();
        }
      }
    });
  });
});


/*
 * Support data-bs-theme="auto"
 */
function applyAutoTheme() {  // Function to set theme based on system preference
  const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
  document.documentElement.setAttribute('data-bs-theme', prefersDark ? 'dark' : 'light');
}

applyAutoTheme();   // Initialize theme on load

// Watch for system theme changes
window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', applyAutoTheme);

// Optional: Persist user override
const storedTheme = localStorage.getItem('bsTheme');
if (storedTheme) {
  document.documentElement.setAttribute('data-bs-theme', storedTheme);
}

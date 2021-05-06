// Get the root element
var r = document.querySelector(':root');

// Create a function for setting a variable value
function myFunction_set() {
    // Get the styles (properties and values) for the root
    var rs = getComputedStyle(r);

    // Get the current BG colour
    var currentBgColour = rs.getPropertyValue('--background')

    // If dark, set to light
    if (currentBgColour === '#22252A') {
        r.style.setProperty('--background', '#EBEBEB');
        r.style.setProperty('--sidebar', '#ffffff');
        r.style.setProperty('--card', '#ffffff');
        r.style.setProperty('--text', '#000000');
        r.style.setProperty('--gray', '#464E5E');
        r.style.setProperty('--blue', '#76838A');
    }
    // If light, set to dark
    if (currentBgColour === '#EBEBEB') {
        r.style.setProperty('--background', '#22252A');
        r.style.setProperty('--sidebar', '#393E44');
        r.style.setProperty('--card', '#393E44');
        r.style.setProperty('--text', '#f0f1f5');
        r.style.setProperty('--gray', '#464E5E');
        r.style.setProperty('--blue', '#059AFA');
    }
}



/**
 * Created by Ati on 8/27/15.
 */

// Grab the form element
var joinForm = document.getElementById("signup");

// Add an 'action' attribute to load the gallery page upon form submission
joinForm.setAttribute("action", "gallery.html");

// Grab the list of input element of the form (using querySelectorAll)
var joinFormInputs = document.querySelectorAll("#signup input");

var nameBox = joinFormInputs[0];
var usernameBox = joinFormInputs[1];
var emailBox = joinFormInputs[2];
var submitButton = joinFormInputs[3];

// Event handler - click on submit button
function validateInput(e) {
    // Validate name - at least one alphabetic character (case insensitive)
    var nameRE = /[a-z]+/i;
    if (!nameRE.test(nameBox.value)) {
        nameBox.focus();
        e.preventDefault();
    }

    // Validate username - at least one alphabetic character (case insensitive)
    if (!nameRE.test(usernameBox.value)) {
        usernameBox.focus();
        e.preventDefault();
    }

    // Validate email
    var emailRE = /[A-Z0-9._%+-]+@[A-Z0-9.-]+.[A-Z]{2,4}/igm;
    if (!emailRE.test(emailBox.value)) {
        emailBox.focus();
        e.preventDefault();
    }

    // When all form fields are valid, store name to use on gallery page
    localStorage.setItem('name', nameBox.value);
}

// Add event listener - click on submit button
submitButton.addEventListener('click', function (e) {
    validateInput(e);
}, false);


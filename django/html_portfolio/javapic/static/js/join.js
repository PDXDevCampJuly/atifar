/**
 * Created by Ati on 8/27/15.
 */

// Grab the form element
var joinForm = document.getElementById("signup");

// Grab the list of input element of the form (using querySelectorAll)
var joinFormInputs = document.querySelectorAll("#signup input");

var nameBox = joinFormInputs[0];
var usernameBox = joinFormInputs[1];
var emailBox = joinFormInputs[2];
var submitButton = joinFormInputs[3];

// Event handler - click on submit button
function validateInput(e) {
    var nameRE = /[a-z]+/i;
    var emailRE = /[A-Z0-9._%+-]+@[A-Z0-9.-]+.[A-Z]{2,4}/igm;

    // Prevent the form post operation
    e.preventDefault();

    // Remove any previous popups
    var popups = document.getElementsByClassName("popup");
    console.log(popups);
    for (i= popups.length - 1; i >= 0 ; i--) {
        joinForm.removeChild(popups[i]);
        console.log("Removed popup");
    }

    // Catch validation failure condition
    var valid = true;

    // Validate name - at least one alphabetic character (case insensitive)
    if (!nameRE.test(nameBox.value)) {

        // Create a new message box
        var newMsgBox = document.createElement("p");
        // Create the text node of the message
        var newText = document.createTextNode("Name can't be empty and must consist of only letters.");
        // Attach new text node to message box
        newMsgBox.appendChild(newText);
        // Insert the message box in DOM tree
        nameBox.parentNode.insertBefore(newMsgBox, nameBox.nextSibling);
        // Make the text inside message box red and smaller
        newMsgBox.style.color = "red";
        newMsgBox.style.fontSize = "0.6em";
        // Attach a class to the message box so it can be removed.
        newMsgBox.setAttribute("class", "popup");

        valid = false;
    }

    // Validate username - at least one alphabetic character (case insensitive)
    if (!nameRE.test(usernameBox.value)) {
        // Create a new message box
        var newMsgBox = document.createElement("p");
        // Create the text node of the message
        var newText = document.createTextNode("Username can't be empty and must consist of only letters.");
        // Attach new text node to message box
        newMsgBox.appendChild(newText);
        // Insert the message box in DOM tree
        usernameBox.parentNode.insertBefore(newMsgBox, usernameBox.nextSibling);
        // Make the text inside message box red and smaller
        newMsgBox.style.color = "red";
        newMsgBox.style.fontSize = "0.6em";
        // Attach a class to the message box so it can be removed.
        newMsgBox.setAttribute("class", "popup");

        valid = false;
    }

    // Validate email
    if (!emailRE.test(emailBox.value)) {
        // Create a new message box
        var newMsgBox = document.createElement("p");
        // Create the text node of the message
        var newText = document.createTextNode("Email must be of proper form.");
        // Attach new text node to message box
        newMsgBox.appendChild(newText);
        // Insert the message box in DOM tree
        emailBox.parentNode.insertBefore(newMsgBox, emailBox.nextSibling);
        // Make the text inside message box red and smaller
        newMsgBox.style.color = "red";
        newMsgBox.style.fontSize = "0.6em";
        // Attach a class to the message box so it can be removed.
        newMsgBox.setAttribute("class", "popup");

        valid = false;
    }

    // When all form fields are valid, store name to use on gallery page
    if (valid) {
        sessionStorage.setItem('name', nameBox.value);
        location.href="gallery.html";
    }
}

// Add event listener - click on submit button
submitButton.addEventListener('click', function (e) {
    validateInput(e);

}, false);


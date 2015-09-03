/**
 * Created by Ati on 8/27/15.
 */

$(function () {
    // Add an 'action' attribute to load the gallery page upon form submission
    $('#signup').attr('action', 'gallery.html');
    // Add listener to catch form submission
    $('#signup').submit(function(e) {
        validateInput(e);
    });
});

function validateInput(e) {
    var nameRE = /^([a-zA-Z]+)$/;
    var emailRE = /[A-Z0-9._%+-]+@[A-Z0-9.-]+.[A-Z]{2,4}/igm;
    var name = $('#signup input:eq(0)').val();
    var username = $('#signup input:eq(1)').val();
    var email = $('#signup input:eq(2)').val();

    // Remove any previous popups
    $('.popup').remove();

    // Validate name - at least one alphabetic character (case insensitive)
    if (!nameRE.test(name)) {
        // Create a new message paragraph
        $('#signup input:eq(0)').after('<p class="popup">"Name cannot be empty and must consist of only letters."</p>');
        // Make the text inside message box red and smaller
        $('.popup').css({
            'fontSize': '0.6em',
            'color': 'red'
        });
        e.preventDefault();
    }

        // Validate username - at least one alphabetic character (case insensitive)
     if (!nameRE.test(username)) {
        // Create a new message paragraph
        $('#signup input:eq(1)').after('<p class="popup">"Username cannot be empty and must consist of only letters."</p>');
        // Make the text inside message box red and smaller
        $('.popup').css({
            'fontSize': '0.6em',
            'color': 'red'
        });
        e.preventDefault();
     }

     // Validate email
     if (!emailRE.test(email)) {
        // Create a new message paragraph
        $('#signup input:eq(2)').after('<p class="popup">"Email must be of proper form."</p>');
        // Make the text inside message box red and smaller
        $('.popup').css({
            'fontSize': '0.6em',
            'color': 'red'
        });
        e.preventDefault();
     }

    // When the name field is valid, store name to use on gallery page
    if (nameRE.test(name)) {
        sessionStorage.setItem('name', name);
    }
}


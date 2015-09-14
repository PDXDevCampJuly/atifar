/**
 * Created by Ati on 8/28/15.
 */

function populateGallery() {
    // Loop over images 1-60 in the images folder
    for (var i = 1; i < 61; i++) {
        // Build the image file path
        var imageNumber = i.toString();
        if (imageNumber.length == 1) {
            imageNumber = "0" + imageNumber;
        }
        var imagePath = "../static/images/pdxcg_" + imageNumber + ".jpg";

        // Grab the section that holds the image gallery
        //$('#gallery').prepend('<li><img src =""/></li>');
        //$('#gallery li:first img').attr('src', imagePath);
        $('#gallery').append('<li><img src =""/></li>');
        $('#gallery li:last img').attr('src', imagePath);

    }

    $('img').on('click', function (e) {
        showLargeImage(e);
    });

    $('body').on('click', function (e) {
        removeLargeImage(e);
    });
}


// Event handler - click on image in gallery
function showLargeImage(e) {
    // If a large preview image is already showing, allow event to bubble up
    if (sessionStorage.getItem("largeImage") == null) {
        console.log(e.target);
        var imagePath = "../static/" + e.target.attributes.src.value;
        console.log(imagePath);

        $('#image_show img').attr('src', imagePath);
        $('#image_show').addClass('display_img').removeClass('display_none');

        sessionStorage.setItem("largeImage", imagePath);
        // Stop event propagation
        e.stopPropagation();
    }
}

// Event handler - click anywhere on page to remove large preview
function removeLargeImage(e) {
    // Hide large preview
    $('#image_show').addClass('display_none').removeClass('display_img');
    sessionStorage.removeItem("largeImage");
}

$(function () {
    // Fetch the name for sessionStorage, which would be set by the join page
    var validName = sessionStorage.getItem("name");

// If a valid name was fetched above, update the gallery tagline with the
// name from the join page.
    if (validName != null) {
        var taglineText = $('.tagline').text();
        $('.tagline').text(taglineText.replace("tiffany", validName));
    }

    populateGallery();
});

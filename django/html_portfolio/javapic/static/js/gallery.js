/**
 * Created by Ati on 8/28/15.
 */

// Fetch the name for localStorage, which would be set by the join page
var validName = sessionStorage.getItem("name");

// If a valid name was fetched above, update the gallery tagline with the
// name from the join page.
if(validName != null) {
    var taglineSpan = document.getElementsByClassName("tagline");
    var taglineText = taglineSpan[0].textContent;
    var customTagline = taglineText.replace("tiffany", validName);
    taglineSpan[0].textContent = customTagline;
}

// Grab the section that holds the image gallery
var gallerySection = document.getElementById("gallery");

// Grab container for large image preview
var largeImageDiv = document.getElementById("image_show");

// Event handler - click on image in gallery
function showLargeImage(e) {
    var imagePath = "../static/" + e.target.attributes.src.nodeValue;

    console.log(e.target);
    console.log(imagePath);

    // Select the clicked image for loading
    largeImageDiv.firstElementChild.src = imagePath;

    // Display large preview
    largeImageDiv.className = "display_img";

    // Stop event propagation
    e.stopPropagation();
}

// Event handler - click anywhere on page to remove large preview
function removeLargeImage(e) {
    // Hide large preview
    largeImageDiv.className = "display_none";

    // Stop event propagation
    e.stopPropagation();
}

// Loop over images 1-60 in the images folder
for (var i = 1; i < 61; i++) {
    // Build the image file path
    var imageNumber = i.toString();
    if (imageNumber.length == 1) {
        imageNumber = "0" + imageNumber;
    }
    var imagePath = "../static/images/pdxcg_" + imageNumber + ".jpg";

    // Build the new list item with the image
    var newImageCell = document.createElement("li");
    var newImage = document.createElement("img");
    newImage.src = imagePath;
    newImageCell.appendChild(newImage);

    // Add the list item to the gallery
    gallerySection.appendChild(newImageCell);
}

// Add event listener - click on a gallery image
gallerySection.addEventListener('click', function (e) {
    showLargeImage(e);
});

// Add event listener - click on large preview prevents its removal
largeImageDiv.firstElementChild.addEventListener('click', function (e) {
    e.stopPropagation();
});

// Add event listener - click outside of large preview removes it
largeImageDiv.addEventListener('click', function (e) {
    removeLargeImage(e);
});


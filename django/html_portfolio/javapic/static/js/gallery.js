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

// Grab entire page
var galleryPage = document.getElementsByTagName("html")[0];

// Grab container for large image preview
var largeImageDiv = document.getElementById("image_show");

// The event flow on this page defaults to bubble. Once an image is shown in
// enlarged preview, the event flow is set to capture by the showLargeImage
// handler, so that the next click anywhere on the page is captured by the
// removeLargeImage handler. The removeLargeImage handler sets the event
// propagation back to bubble.
var eventFlowCapture = false;

// Event handler - click on image in gallery
function showLargeImage(e) {
    var imagePath = "../static/" + e.target.attributes.src.nodeValue;

    // Select the clicked image for loading
    largeImageDiv.firstElementChild.src = imagePath;

    // Display large preview
    largeImageDiv.className = "display_img";

    // Stop event propagation
    e.stopPropagation();

    // Set the event flow to capture
    eventFlowCapture = true;
}

// Event handler - click anywhere on page to remove large preview
function removeLargeImage(e) {
    // Hide large preview
    largeImageDiv.className = "display_none";

    // Stop event propagation
    e.stopPropagation();

    // Set the event flow to bubble
    eventFlowCapture = false;
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

    // Add event listener - click on an image
    newImage.addEventListener('click', function (e) {
        showLargeImage(e);
    }, eventFlowCapture);
}

// Add event listener - click anywhere on page
galleryPage.addEventListener('click', function (e) {
    removeLargeImage(e);
}, eventFlowCapture);


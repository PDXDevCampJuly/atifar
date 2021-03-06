/**
 * Created by Ati on 8/27/15.
 */

// Jumbotron picture set to rotate through - image file paths
var jumboPics = [
    "images/pdxcg_01.jpg",
    "images/pdxcg_02.jpg",
    "images/pdxcg_03.jpg",
    "images/pdxcg_04.jpg",
    "images/pdxcg_05.jpg",
    "images/pdxcg_06.jpg",
    "images/pdxcg_07.jpg",
    "images/pdxcg_08.jpg",
    "images/pdxcg_09.jpg",
    "images/pdxcg_10.jpg"
];

// Starting picture index
var jumboPicIdx = 4;

// Grab the jumbotron element
var $jumbotronDiv = $('div#jumbotron');

function jumbotronRotatePic() {
    // Update the array index
    jumboPicIdx = (jumboPicIdx + 1) % jumboPics.length;

    // Build image file URL
    var picUrl = "url(" + jumboPics[jumboPicIdx] + ")";

    // Update the background picture
    $jumbotronDiv.css('backgroundImage', picUrl);
}

// Rotate through first ten images in the jumbotron, switching images every
// 20 seconds.
$(function() {
    setInterval(function() {
        jumbotronRotatePic();
    }, 20000);
});


'use strict';
// Post to and get forum entries from a Google spreadsheet

$(function() {

  //
  ///////////////////////////////////////
  // Test GET method using jQuery
  $.get('https://spreadsheets.google.com/feeds/list/1ntmcFZk4R0Owmez5eKc0bcu_PftAKwWyXDWTqmypPgI/default/public/values?alt=json-in-script', function(data){
    // console.log("Inside callback.");
    // console.log(data);
    // console.log(data.feed.entry);
    var entries = data.feed.entry;
    // Loop through the forum entries
    for (var i=0; i < entries.length; i++) {
      $('main').append('<setion class="post"><p class="title"></p><p class="body"></p></section>');
      var title = entries[i].gsx$posttitle["$t"];
      // console.log(title);
      var body = entries[i].gsx$postbody["$t"];
      // console.log(body);
      $('.post:last p.title').append(title);
      $('.post:last p.body').append(body);
    };
  }, 'jsonp');
  console.log("Got past the get request.");

  function sendNewPost(e) {
    var new_title = $('#new_title').val();
    var new_body = $('#new_body').val();
    var send_data = {
      "entry_434124687": new_title,
      "entry_1823097801": new_body
    };
    console.log(send_data);
    var jqxr = $.post('https://docs.google.com/forms/d/1blH7mM6udvlyJ0SrPmbXoNPZg8XCqDQaxHTPrK0HQbA/formResponse', send_data, function() {
      alert("success");
    }).always( function() {
      console.log("Trying to refresh the page.");
      location.reload(true);
    });
  }
  console.log("Got past the send def.");

  $('#new_post_form').on('submit', function(e) {
    e.preventDefault();
    console.log('Posting...');
    sendNewPost(e);
  });

});
  // Test POST method

/*  var data = {
    "entry_434124687": "Howdy",
    "entry_1823097801": "This is a test post body."
  }
  var jqxr = $.post('https://docs.google.com/forms/d/1blH7mM6udvlyJ0SrPmbXoNPZg8XCqDQaxHTPrK0HQbA/formResponse', data, function() {
    alert("success");
  });
  console.log(jqxr);
*/

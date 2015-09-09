// Post to and get forum entries from a Google spreadsheet

console.log("Show me anything!");

$(function(){
  //
  ///////////////////////////////////////
  // Test GET method using jQuery
  $.get('https://spreadsheets.google.com/feeds/list/1ntmcFZk4R0Owmez5eKc0bcu_PftAKwWyXDWTqmypPgI/default/public/values?alt=json-in-script', function(data){
    console.log("Inside callback.");
    console.log(data);
    console.log(data.feed.entry);
    var entries = data.feed.entry;
    // Loop through the forum entries
    for (var i=0; i < entries.length; i++) {
      $('main').append('<setion class="post"><p class="title"></p><p class="body"></p></section>');
      var title = JSON.stringify(entries[i].gsx$posttitle);
      console.log(title.$t);
      var body = JSON.stringify(entries[i].gsx$postbody);
      console.log(body);
      // $('.post:last p.title').append()
    }
  }, 'jsonp');
  console.log("Got past the get request.");


  //
  ///////////////////////////////////////
  // Test POST method
  // Build test JSON object
/*  var data = {
    "entry_434124687": "Howdy",
    "entry_1823097801": "This is a test post body."
  }

  console.log(data);

  var jqxr = $.post('https://docs.google.com/forms/d/1blH7mM6udvlyJ0SrPmbXoNPZg8XCqDQaxHTPrK0HQbA/formResponse', data, function() {
    alert("success");
  });
  console.log(jqxr);
*/
});

var dropdown = document.getElementById("langs");
dropdown?.addEventListener("change", OnChange);

var textbox = document.getElementById("text");

function OnChange(){
  console.log("new lang selected");

  var lang = dropdown?.value;

  //send a request to the route
  fetch('/translate/' + lang)
  .then(function (response) {
    //THEN return the json returned from the page
    return response.json();
  }).then(function (text) {
    //THEN do whatever with the data
    if (textbox){
      textbox.textContent = text.lang;
    }
  });
}
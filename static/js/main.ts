var dropdown = document.getElementById("langs");
dropdown?.addEventListener("change", OnChange);

var textbox = document.getElementById("text");

//run functions when the page is loaded to get the list of languages that can be translated into
window.onload = OnLoad;

function OnLoad(){
  function AddOption(item){
    var option = document.createElement("option");
    option.text = item.language;
    option.value = item.language_code;

    dropdown?.add(option);
  }
  
  fetch("/languages")
  .then(function (response) {
    return response.json();
  }).then(function (text) {
    //text will be the list of dictionary with languages and codes
    text.forEach(AddOption);
  });
}

function OnChange(){
  console.log("new lang selected");

  var lang = dropdown?.value;

  //send a request to the route
  fetch("/translate/" + lang)
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
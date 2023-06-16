//typescript is type sensitive so if theres no property or there is a chance that the property is null then it returns an error,
//but the program still works even with these errors

var dropdown = document.getElementById("langs");
dropdown?.addEventListener("change", OnChange);

var textbox = document.getElementById("text");

//run functions when the page is loaded to get the list of languages that can be translated into
window.onload = OnLoad;


function OnLoad(){
  OnChange();

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
  if (lang == null || lang == undefined || lang == ""){
    console.log("lang is null");
    lang = "en";
  }
  

  //send a request to the route
  fetch("/translate/" + lang)
  .then(function (response) {
    //THEN return the json returned from the page
    return response.json();
  }).then(function (text) {
    //THEN add the text to text element
    OrderText(text.lang);
  });
}

function OrderText(text){
  textbox.textContent = "";
  text.forEach(function(item){
    textbox.textContent += item + "\r\n";
  })

  //testing
  console.log(textbox.textContent);
}
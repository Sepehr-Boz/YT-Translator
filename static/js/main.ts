const button = document.getElementById("clickButton");
button?.addEventListener("click", myFunc)

var para = document.getElementById("p");

function myFunc(){
    console.log("button clicked");
    //send a request to the route
    fetch('/getmethod')
      .then(function (response) {
        //THEN return the json returned from the page
        return response.json();
      }).then(function (text) {
        //THEN do whatever with the data
        if (para){
            para.textContent += text.greeting;
        }
      });
}
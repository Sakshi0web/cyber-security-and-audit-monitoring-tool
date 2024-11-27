function toggleTextBox() {
    var textBox = document.getElementById("additionalTextBox");
    textBox.style.display = document.getElementById("checkbox").checked ? "block" : "none";
  }



// popup

let popup = document.getElementById("popup");

function openPopup(){
    popup.classList.add("open-popup");
       
    popup.addEventListener('click', function() {
   
    location.reload();
});
    
}
function closePopup(){
    popup.classList.remove("open-popup");   
} 
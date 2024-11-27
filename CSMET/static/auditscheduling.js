function toggleFields() {
  var additionalFields = document.getElementById("additionalFields");
  if (additionalFields.style.display === "none") {
    additionalFields.style.display = "block";
  } else {
    additionalFields.style.display = "none";
  }
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
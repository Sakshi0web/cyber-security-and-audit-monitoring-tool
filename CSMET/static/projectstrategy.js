function toggleCheckbox1() {
    var checkbox1 = document.getElementById("checkbox1");
    var checkbox2Container = document.getElementById("checkbox2Container");
    var dropdownContainer1 = document.getElementById("dropdownContainer1");
    var dropdownContainer2 = document.getElementById("dropdownContainer2");
    var dropdownContainer3 = document.getElementById("dropdownContainer3");

    if (checkbox1.checked) {
      checkbox2Container.classList.remove("hidden");
    } else {
      checkbox2Container.classList.add("hidden");
      dropdownContainer1.classList.add("hidden");
      dropdownContainer2.classList.add("hidden");
      dropdownContainer3.classList.add("hidden");
    }
  }

  function toggleCheckbox2() {
    var checkbox2 = document.getElementById("checkbox2");
    var dropdownContainer1 = document.getElementById("dropdownContainer1");

    if (checkbox2.checked) {
      dropdownContainer1.classList.remove("hidden");
    } else {
      dropdownContainer1.classList.add("hidden");
    }
  }

  function toggleCheckbox3() {
    var checkbox3 = document.getElementById("checkbox3");
    var dropdownContainer2 = document.getElementById("dropdownContainer2");

    if (checkbox3.checked) {
      dropdownContainer2.classList.remove("hidden");
    } else {
      dropdownContainer2.classList.add("hidden");
    }
  }

  function toggleCheckbox4() {
    var checkbox4 = document.getElementById("checkbox4");
    var dropdownContainer3 = document.getElementById("dropdownContainer3");

    if (checkbox4.checked) {
      dropdownContainer3.classList.remove("hidden");
    } else {
      dropdownContainer3.classList.add("hidden");
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
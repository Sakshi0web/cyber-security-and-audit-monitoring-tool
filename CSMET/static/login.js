// let popup = document.getElementById("popup");

// function openPopup(){
//     popup.classList.add("open-popup");
// }
// function closePopup(){
//     popup.classList.remove("open-popup");
// }

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




// password eye

function togglePasswordVisibility() {
    const passwordInput = document.getElementById('passwordInput');
    const eyeIcon = document.querySelector('.toggle-password ion-icon');

    if (passwordInput.type === 'password') {
        passwordInput.type = 'text';
        eyeIcon.setAttribute('name', 'eye-off');
    } else {
        passwordInput.type = 'password';
        eyeIcon.setAttribute('name', 'eye');
    }
}


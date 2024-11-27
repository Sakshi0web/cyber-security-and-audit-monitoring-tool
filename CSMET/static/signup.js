

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

function togglePasswordVisibility() {
    const passwordInput = document.getElementById('passwordInput');
    const eyeIcon = document.querySelector('.toggle-password ion-icon');

    if (passwordInput.type === 'confrimpassword') {
        passwordInput.type = 'text';
        eyeIcon.setAttribute('name', 'eye-off');
    } else {
        passwordInput.type = 'confrimpassword';
        eyeIcon.setAttribute('name', 'eye');
    }
}
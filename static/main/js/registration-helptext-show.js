// ******************
// Script processes the appearance of a prompt for the fields of the new user registration form.
// ******************

// Handler for the appearance of tooltip text for the field: "Login" of the registration form
document.addEventListener('DOMContentLoaded', function() {
    var inputField = document.getElementById('id_username');
    var infoBlock = document.querySelector('.helptext-info-block-username');
    inputField.addEventListener('focus', function() {
        infoBlock.style.display = 'block';
    });
    inputField.addEventListener('blur', function() {
        infoBlock.style.display = 'none';
    });
});

// Handler for the appearance of tooltip text for the field: "Email" of the registration form
document.addEventListener('DOMContentLoaded', function() {
    var inputField = document.getElementById('id_email');
    var infoBlock = document.querySelector('.helptext-info-block-email');
    inputField.addEventListener('focus', function() {
        infoBlock.style.display = 'block';
    });
    inputField.addEventListener('blur', function() {
        infoBlock.style.display = 'none';
    });
});

// Handler for the appearance of hint text for the field: "Password" of the registration form
document.addEventListener('DOMContentLoaded', function() {
    var inputField = document.getElementById('id_password1');
    var infoBlock = document.querySelector('.helptext-info-block-password1');
    inputField.addEventListener('focus', function() {
        infoBlock.style.display = 'block';
    });
    inputField.addEventListener('blur', function() {
        infoBlock.style.display = 'none';
    });
});

// Handler for the appearance of hint text for the field: "Password Confirmation" of the registration form
document.addEventListener('DOMContentLoaded', function() {
    var inputField = document.getElementById('id_password2');
    var infoBlock = document.querySelector('.helptext-info-block-password2');
    inputField.addEventListener('focus', function() {
        infoBlock.style.display = 'block';
    });
    inputField.addEventListener('blur', function() {
        infoBlock.style.display = 'none';
    });
});
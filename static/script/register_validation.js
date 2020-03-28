$(document).ready(function () {
    $('form').submit(function(event){
        var password1 = $('#id_password1').val()
        var password2 = $('#id_password2').val()
        if (password1.length<6){
            alert("Password should not be less than 6 characters!");
            event.preventDefault();
        }              
        if (password1 !=password2){
            alert('Passwords are not the same! Please confirm your password again');
            event.preventDefault();
        }              
    })
})
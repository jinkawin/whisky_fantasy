window.fbAsyncInit = function() {
    FB.init({
    appId      : '132424584856143',
    cookie     : true,
    xfbml      : true,
    version    : 'v6.0'
    });

    FB.AppEvents.logPageView();
};

(function(d, s, id){
    var js, fjs = d.getElementsByTagName(s)[0];
    if (d.getElementById(id)) {return;}
    js = d.createElement(s); js.id = id;
    js.src = "https://connect.facebook.net/en_US/sdk.js";
    fjs.parentNode.insertBefore(js, fjs);
}(document, 'script', 'facebook-jssdk'));


$(document).ready(function(){
    var csrftoken = $("[name=csrfmiddlewaretoken]").val();

    $("#facebook-button").click(function(){
        FB.login(function(response) {
            if (response.status === 'connected') {
                console.log('Welcome!  Fetching your information.... ');

                access_token = response.authResponse.accessToken; //get access token
                user_id = response.authResponse.userID; //get FB UID

                FB.api('/me', {"fields":"email,first_name,last_name"}, function (response) {
                    console.log(response);
                    $.post( "facebook_login", { 'fb_obj': response, 'csrfmiddlewaretoken': csrftoken }, function(data) {
                        console.log(data);
                    });
                });

            } else {
                //user hit cancel button
                console.log('User cancelled login or did not fully authorize.');

            }
        }, {
            scope: 'public_profile,email'
        });
    });
});
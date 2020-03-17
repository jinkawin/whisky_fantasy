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
        var loginUrl = $("#facebook-button")[0].getAttribute('data-url');
        var redirect = $("#facebook-button")[0].getAttribute('data-redirect');

        FB.login(function(response) {
            if (response.status === 'connected') {

                access_token = response.authResponse.accessToken; //get access token
                user_id = response.authResponse.userID; //get FB UID

                FB.api('/me', {"fields":"email,first_name,last_name"}, function (response) {

                    var data = {
                        'role': 0,
                        'cust_fb_id': response.id,
                        'username': response.first_name + response.last_name,
                        'email': response.email,
                        'csrfmiddlewaretoken': csrftoken
                    }

                    $.post(loginUrl, data, function(response) {
                        if(response.isSuccess){
                            window.location.replace(redirect);
                        }
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
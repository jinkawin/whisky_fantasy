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

function checkLoginState() {
    FB.getLoginStatus(function(response) {
        statusChangeCallback(response);
    });
}

function statusChangeCallback(response) {
    if (response.status === 'connected') {
        console.log('Welcome!  Fetching your information.... ');
        FB.api('/me', {"fields":"email"}, function (response) {
            console.log(response);

            // console.log('Successful login for: ' + response.name);
            // document.getElementById('status').innerHTML =
            //   'Thanks for logging in, ' + response.name + '!';
        });
    } else {
        // The person is not logged into your app or we are unable to tell.
        console.log("Else")
        // document.getElementById('status').innerHTML = 'Please log ' +
        //   'into this app.';
    }
}
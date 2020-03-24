$(document).ready(function(){
    var searchUrl = $('#id_location')[0].getAttribute('data-url');

    $.get(searchUrl, {'key': ''}, function(response) {
        $(".autocomplete").autocomplete({
            source: response.locationList
        });
    });
})
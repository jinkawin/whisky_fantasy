$(document).ready(function() {
    $('#search-input').keyup(function() {
        var query;
        query = $(this).val();
        console.log(query);
        $.get('/app/suggest/',
            {'suggestion': query},
            function(data) {
                $('#whisky-listing').html(data);
            })
    });
});
